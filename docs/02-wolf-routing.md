# 🪨 وحش ٢ — توجيه الرسائل بالـ mesh (Routing / Forwarding)

## المشكلة

عندك عشرات/مئات الجيران لكل عقدة، وطوبولوجيا (topology) تتغير كل ثانية (الناس
تمشي). لو كل واحد يعيد بث كل رزمة لكل من حوله → **عاصفة بث (broadcast storm)**
تسدّ الشبكة وتحرق البطاريات.

اختبار النجاح: **رسالة تقطع ≥٥ قفزات بين أجهزة، بلا تكرار لا نهائي، بلا انفجار
trafik.**

---

## القرار المعماري: Controlled Flooding

routing منظّم (يبني جداول مسارات) **مستحيل** بطوبولوجيا فوضوية متحركة. الحل
الواقعي لهذا الزحام هو **فيضان مُتحكَّم به**: كل عقدة تعيد بث الرزمة لجيرانها، لكن
بآليات تمنع الانفجار والدوران.

أربع آليات تتعاون:

### ١. Message ID (منع التكرار)

كل رزمة لها معرّف فريد = هاش على (المحتوى + المصدر + timestamp/nonce). يُستعمل
للـ dedup عبر الشبكة كلها.

### ٢. TTL (حدّ القفزات)

- حقل `ttl` يبدأ بقيمة (مثلاً **25**).
- كل قفزة يُنقَص بواحد قبل إعادة البث.
- عند الوصول للصفر → تتوقف الرزمة (ما تُعاد).
- رزم الطوارئ/SOS تاخذ TTL أعلى.

### ٣. Seen-set (ذاكرة الرزم المرئية)

- بنية تتذكّر `MessageId`ات الرزم اللي مرّت مؤخراً.
- لو وصلت رزمة معروفة سابقاً → **تُهمَل فوراً** (يمنع الدوران واللوبات).
- **التنفيذ:** LRU bounded + **Bloom filter** للحجم الكبير بكفاءة ذاكرة. الـ
  Bloom filter يقبل false-positives نادرة (نهمل رزمة جديدة أحياناً) لكن **ما
  يقبل false-negatives** (ما نعيد بث مكرر) — وهذا الاتجاه الآمن للـ mesh.
- يُدعَم بجدول DB (`SeenMessageCache`، [وثيقة 08](08-data-model.md)) للصمود عبر
  إعادة التشغيل.

### ٤. Suppression (تثبيط البث) — قلب منع العاصفة

قبل إعادة البث، **انتظر تأخير عشوائي قصير + أنصت**. لو سمعت جار ثاني بثّ نفس
الرزمة خلال الانتظار، **اسكت** (counter-based scheme). هذا يقلّل التكرار بشكل
كبير بالمناطق الكثيفة، لأن جار واحد يكفي يغطّي المنطقة.

```text
on receive(packet):
    if packet.id in seenSet:                 # آلية ٣
        recordDuplicateHeard(packet.id)      # يغذّي عدّاد suppression
        return
    seenSet.add(packet.id)
    if isForMe(packet): deliverUp(packet)    # وحش ٣

    packet.ttl -= 1                           # آلية ٢
    if packet.ttl <= 0: return

    if packet.priority == EMERGENCY:
        rebroadcast(packet)                   # طوارئ: بلا تأخير، طابور منفصل
        return

    delay = random(MIN_DELAY, MAX_DELAY)      # آلية ٤
    heardCount = 0
    wait(delay) while counting duplicates heard of packet.id → heardCount
    if heardCount >= SUPPRESS_THRESHOLD:      # جيران كفوا التغطية
        return                                # اسكت
    rebroadcast(packet)
```

---

## أنواع الرزم

| النوع | الوصف | الانتشار |
|-------|-------|----------|
| **Broadcast** | بيانات تجميعية، إعلانات مبيت — للكل | فيضان عادي |
| **Unicast** | لعقدة موثوقة محددة | يُفاض بالفيضان، لكن **يفكّ تشفيرها الهدف فقط** ([وحش ٤](04-wolf-crypto-identity.md)) |
| **Receipt** | إيصال تسليم يرجع نحو المصدر | فيضان موجّه نحو `originNodeId` ([وحش ٣](03-wolf-store-and-forward.md)) |

> الوسطاء يمرّرون unicast كـ **blob مشفّر** — ما يقرونه. التوجيه يشتغل على
> البيانات الوصفية (header) فقط، مو المحتوى.

## الأولوية والطوابير

- **طابور طوارئ منفصل** لرزم SOS: TTL أعلى، بلا تأخير suppression، أولوية إرسال.
- طابور عادي للباقي.
- عند ضغط الباندويث، رزم الطوارئ تسبق دائماً.

## معاملات قابلة للضبط (tuning)

| المعامل | قيمة ابتدائية مقترحة | ملاحظة |
|---------|----------------------|--------|
| `DEFAULT_TTL` | 25 | يُضبط بمحاكاة الكثافة |
| `EMERGENCY_TTL` | 40 | أعلى للطوارئ |
| `MIN_DELAY / MAX_DELAY` | 20ms / 200ms | نافذة suppression العشوائية |
| `SUPPRESS_THRESHOLD` | 2 | كم نسخة نسمعها قبل ما نسكت |
| `SEEN_SET_TTL` | 24–48h | عمر الإدخال بالـ seen-set |

كل هذي **تُعاير بمحاكاة الكثافة** (٥ → ١٠ → ٢٠+ جهاز، [وثيقة 12](12-testing.md)).

## واجهة مقترحة (pure Kotlin — قابلة لاختبار JVM)

```kotlin
interface Router {
    /** يقرر مصير رزمة واردة: تُهمَل / تُسلَّم لفوق / تُعاد بثها (مع/بلا تأخير). */
    suspend fun onPacketReceived(packet: Packet, fromPeer: PeerId): RouteDecision
    fun enqueueOriginated(packet: Packet)
}

sealed interface RouteDecision {
    object Drop : RouteDecision
    data class DeliverLocal(val packet: Packet) : RouteDecision
    data class Rebroadcast(val packet: Packet, val afterDelayMs: Long) : RouteDecision
}
```

## حالات اختبار (وحدات — JVM)

- [ ] رزمة معروفة (بالـ seen-set) → `Drop`.
- [ ] `ttl == 1` تُسلَّم/تُعالَج لكن ما تُعاد بثها (تصير 0).
- [ ] سماع نسختين ضمن نافذة التأخير → suppression يكتم الإعادة.
- [ ] رزمة EMERGENCY → بلا تأخير، طابور منفصل.
- [ ] Bloom filter: ماكو false-negative (ما يُعاد بث مكرر أبداً).
- [ ] رسالة عبر سلسلة محاكاة من ≥٥ عقد توصل بلا حلقات لا نهائية.

## التبعيات

- ينتج رزم تُخزَّن بـ [وحش ٣](03-wolf-store-and-forward.md) وتُنقَل عبر
  [وحش ٦](06-wolf-ble-transport.md).
- milestone: **M2** ([وثيقة 11](11-build-plan.md)) — **منطق نقي، قابل لاختبار JVM
  كامل بلا أجهزة.**
