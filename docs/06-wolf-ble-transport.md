# 🪨 وحش ٦ — طبقة نقل BLE (BLE Transport Mechanics)

## المشكلة

BLE مصمَّم لأجهزة صغيرة وحمولات ضئيلة، **مو لنقل بيانات كثيفة بين مئات الأجهزة**.
لازم نطوّعه ليصير ناقل mesh.

اختبار النجاح: **جهازان يكتشفون بعض ويتبادلون رزمة كاملة (أكبر من MTU، مجزّأة
ومعاد تجميعها) بنجاح، بالخلفية.**

---

## ١. Advertising (إعلان الحضور)

- **Legacy advertising:** حمولة صغيرة ~31 بايت.
- **Extended advertising (BLE 5):** حتى ~255 بايت (لمن الجهاز يدعمها).
- يُستعمل لـ **beacon الحضور فقط**: يبثّ `NodeId` + flags (قدرة بوابة، مستوى
  بطارية تقريبي اختياري) — **مو لنقل الرزم**.
- يخلّي الجيران يكتشفون بعض بلا اتصال (سلبي، موفّر للطاقة).

## ٢. GATT Connections (النقل الفعلي)

- النقل الحقيقي للرزم يصير عبر **GATT connection** بين عقدتين.
- service/characteristics مخصّصة للتطبيق: characteristic للكتابة (إرسال رزمة)
  و characteristic للإشعار (notify) لاستقبال رزم.

## ٣. MTU Negotiation

- اطلب **MTU أكبر** (حتى **517** بايت) بعد الاتصال → يقلّل التجزئة بشكل كبير.
- الـ MTU الفعلي يُتفاوض عليه؛ تعامل مع أي قيمة يرجّعها النظام.

## ٤. التجزئة وإعادة التجميع (Fragmentation / Reassembly)

- الرزم الأكبر من (MTU − overhead) تُقسَّم لـ **fragments**.
- كل fragment يحمل: `packetId`، `fragmentIndex`، `totalFragments`.
- المستقبل يجمّعها لمن تكتمل؛ يتعامل مع وصول مبعثر/ناقص (timeout + تجاهل غير
  المكتمل).

```text
fragment header: [ packetId(16B) | idx(2B) | total(2B) | payloadChunk... ]
reassembly: buffer[packetId] = array(total); on complete → deliver to Router
```

> **منطق التجزئة/التجميع نقي قابل لاختبار JVM** (بايتات داخلة/طالعة)؛ فقط الراديو
> الفعلي أندرويد.

## ٥. مجدول الاتصالات (Connection Scheduler)

- التلفون يمسك عدد محدود من GATT connections متزامنة (**~4–8** عملياً).
- **scheduler** يدوّر بينها: يتصل بجار → ينقل ما عنده → يقطع → ينتقل لجار ثاني.
- يوازن بين: تغطية أكبر عدد جيران، وعدم إرهاق الراديو/البطارية.
- يفضّل الجيران بـ RSSI أقوى وآخر ظهور أحدث.

## ٦. Wi-Fi Aware (NAN) للباندويث الأعلى

- عند الحاجة لنقل بيانات أكبر، استعمل **Wi-Fi Aware** (أو Wi-Fi Direct fallback).
- **الدعم يختلف بين الأجهزة** — **اكشف التوفّر** (`isAvailable`) وارجع لـ BLE عند
  غيابه. لا تفترض وجوده.
- يُستعمل انتقائياً (يصرف طاقة أكثر) — مثلاً نقل دفعات كبيرة بين بوابة وجيرانها.

## ٧. جدول الجيران (Neighbor Table)

لكل جار معروف:

| الحقل | الاستعمال |
|-------|-----------|
| `NodeId` | الهوية |
| `rssi` | قوة الإشارة → ترتيب الجدولة |
| `lastSeen` | آخر ظهور → تقادم/شطب |
| `batteryHint` | إن شُورِكَت → انتخاب البوابة |
| `gatewayCapable` | flag من الـ advertising |

## ٨. واجهة مقترحة

```kotlin
interface MeshTransport {                     // أندرويد (BLE/Wi-Fi Aware)
    fun startAdvertising(beacon: PresenceBeacon)
    fun startScanning()
    val neighbors: StateFlow<List<Neighbor>>
    suspend fun send(packet: ByteArray, to: PeerId)   // يتولّى MTU + fragmentation
    val incoming: Flow<ReceivedPacket>
}

object Fragmenter {                           // pure Kotlin — JVM-testable
    fun split(packet: ByteArray, maxChunk: Int): List<Fragment>
    fun reassemble(fragments: List<Fragment>): ByteArray?   // null لو ناقص
}
```

## ٩. حالات اختبار

- وحدات (JVM): `reassemble(split(p)) == p` لأحجام مختلفة؛ fragment ناقص →
  `null`؛ ترتيب وصول مبعثر يُجمَّع صح.
- أجهزة (instrumented): اكتشاف جارين؛ نقل رزمة > MTU؛ نقل بالخلفية؛ scheduler
  يدوّر بين عدة جيران.

## التبعيات

- يستضيفه [وحش ١](01-wolf-background-survival.md) (Foreground Service)، يغذّي
  [وحش ٢](02-wolf-routing.md).
- milestone: **M1** (اكتشاف + نقل أساسي) ويكتمل عبر المراحل — **النقل الفعلي
  يحتاج أجهزة حقيقية؛ منطق Fragmenter قابل لاختبار JVM.**
