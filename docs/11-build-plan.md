# 11 — خطة البناء (Build Plan)

## المبدأ: الأنظمة القاتلة أول

**لا تُبنى الميزات قبل البنية.** الترتيب مقصود — لو فشل أول وحشين، التطبيق ميت.
كل milestone **يُبنى ويشتغل** قبل التالي.

---

## Milestones

| M | العنوان | الوحوش | اختبار النجاح | يحتاج أجهزة؟ |
|---|---------|--------|----------------|--------------|
| **M1** | الخلفية + النقل | [١](01-wolf-background-survival.md) + [٦](06-wolf-ble-transport.md) | جهازان يشوفون بعض ويبقون نشطين بالخلفية | ✅ نعم |
| **M2** | التوجيه | [٢](02-wolf-routing.md) | رسالة تقطع ≥٥ قفزات بلا عاصفة | 🟡 منطق JVM + تأكيد بأجهزة |
| **M3** | التخزين والتسليم | [٣](03-wolf-store-and-forward.md) + [٧](07-wolf-storage.md) | ⏳→✓ تشتغل أوفلاين | 🟡 منطق JVM + Room بأندرويد |
| **M4** | التشفير والهوية | [٤](04-wolf-crypto-identity.md) | relay ما يقرأ؛ التوقيع يُتحقَّق | 🟡 منطق JVM + Keystore بأندرويد |
| **M5** | البوابة | [٥](05-wolf-gateway.md) | عقدة واحدة ترفع، السيرفر يستبعد التكرار | 🟡 منطق JVM + شبكة |
| **M6** | الميزات | [القسم ٩](09-features.md) | فوق البنية، مع احترام [الخطوط الحمراء](10-red-lines.md) | ✅ |
| **M7** | الواجهة | Compose | تلميع، مؤشرات حالة، شاشات إرشاد | ✅ |

> 🟡 = جزء كبير منه **منطق نقي قابل لاختبار JVM** بلا أجهزة (انظر
> [وثيقة 13](13-environment-and-status.md) لما يُمكن إنجازه بالبيئة الحالية).

---

## تسلسل الـ init (الفتح الأول)

```
٠. فحص الإقلاع: أول مرة؟ → كمّل ١–٧ | متكرّر؟ → حمّل DB + شغّل mesh فوراً
١. توليد المفاتيح محلياً (Ed25519 + X25519؛ AES رئيسي بالKeystore يشفّرها)
٢. ملف شخصي أدنى (اسم/كنية للموثوقين فقط — لا إيميل/رقم)
٣. الصلاحيات بالتسلسل مع شرح:
      BLE → موقع (neverForLocation) → إشعارات → إعفاء بطارية
٤. تشغيل mesh: Foreground Service + advertising + scanning + GATT
٥. تهيئة التخزين المحلي المشفّر (Room + SQLCipher)
٦. دائرة الثقة (QR وجهاً لوجه)
٧. مزامنة انتهازية مع السيرفر (مفتاح مثبّت، رفع المسموح فقط)
```

---

## هيكل المشروع المقترح

```
app/
 ├─ ui/            (Compose: شاشات، مكوّنات، تصميم)
 ├─ features/      (موقع، رسائل، مبيت، تجميعي، صحة، موردين، sos…)
 ├─ crypto/        (هوية، sealed boxes، توقيع، Keystore wrapper)
 ├─ mesh/
 │   ├─ routing/   (controlled flooding، TTL، seen-set، suppression)
 │   ├─ forward/   (store-and-forward، state machine، receipts)
 │   └─ gateway/   (انتخاب البوابة، رفع، server pinning)
 ├─ transport/     (BLE GATT، advertising، MTU، fragmentation، Wi-Fi Aware)
 ├─ background/    (Foreground Service، BootReceiver، OEM handling)
 └─ data/          (Room entities، DAOs، SQLCipher، تنظيف)
```

### تقسيم Gradle مقترح (يفصل المنطق النقي عن أندرويد)

عشان نكدر نختبر "الوحوش المنطقية" على JVM بلا SDK/أجهزة:

```
:core   (JVM pure Kotlin) → routing، forward state machine، crypto engine،
         wire format، fragmenter، gateway election.  ← unit tests JVM
:app    (Android)         → transport (BLE)، background، data (Room/SQLCipher)،
         KeyVault (Keystore)، ui (Compose).  ← يعتمد على :core
```

> هذا التقسيم يخلّي **M2 + M4 + منطق M3/M5/M6** قابل للبناء والاختبار **حتى بدون
> Android SDK** (Maven Central يكفي). انظر [وثيقة 13](13-environment-and-status.md).

---

## قواعد التنفيذ (تذكير)

- **أوفلاين أولاً** بكل سطر — ولا شي ينتظر سيرفر.
- **توقّف وأبلغ بأمانة** عند أي فشل أو نقص — لا تخفي فشل تحت كود يبيّن شغّال.
- **[الخطوط الحمراء](10-red-lines.md) لا تُتجاوز.**
- اسأل عند أي قرار معماري غير محسوم بالوثائق.
