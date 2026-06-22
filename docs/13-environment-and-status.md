# 13 — البيئة والحالة (الصدق أولاً)

## الحالة الحالية

**ماكو كود بعد — هذه حزمة توثيق تصميم فقط.** السبب مباشر: البيئة السحابية الحالية
ما تكدر تبني تطبيق Android حقيقي.

## ما فُحِص فعلياً بالبيئة

| الأداة / المورد | الحالة |
|------------------|--------|
| Java | ✅ OpenJDK 21 |
| Gradle | ✅ 8.14.3 |
| Maven Central (`repo1.maven.org`) | ✅ متاح |
| Gradle plugins/services | ✅ متاح |
| GitHub | ✅ متاح |
| **Android SDK** | ⛔ غير منصَّب، و`ANDROID_HOME` فارغ |
| **`dl.google.com`** (تنزيل SDK) | ⛔ **محجوب** بالـ network allowlist |
| **`maven.google.com`** (AGP، AndroidX، Compose، Room) | ⛔ **محجوب** |
| `kotlinc` (CLI) | ⛔ غير منصَّب (لكن Gradle يجيب Kotlin من Maven Central) |
| أجهزة Android حقيقية | ⛔ ماكو |

## ليش هذا حاجز حاسم

1. بناء أي Android module يحتاج **Android Gradle Plugin** وكل مكتبات
   AndroidX/Compose/Room — كلها على `maven.google.com` **المحجوب**.
2. حتى لو توفّرت المكتبات، الـ compile يحتاج **Android SDK platform** اللي
   تنزيله من `dl.google.com` **المحجوب**.
3. **M1 و M6** (الخلفية + BLE) ما ينختبرون على محاكي أصلاً — يحتاجون **أجهزة
   حقيقية متعددة** غير موجودة هنا.

> بحسب **مبدأ التوقّف الأمين**: ما راح أكتب كود Android وأقول "شغّال" وهو ما
> انبنى ولا انختبر ولا مرة. هذا بالضبط الممنوع بالقسم ٠ من البرومبت.

## شنو **يُمكن** إنجازه بهذه البيئة (لو طُلب لاحقاً)

تقسيم Gradle لـ `:core` (JVM نقي) يخلّي قلب "الوحوش" المنطقي **يُبنى ويُختبَر
فعلاً هنا** باعتماد **Maven Central فقط**:

- 🪨 [وحش ٢ — التوجيه](02-wolf-routing.md): controlled flooding, TTL, seen-set,
  suppression. **(M2 كامل، منطق نقي)**
- 🪨 [وحش ٣ — المنطق](03-wolf-store-and-forward.md): آلة الحالة + الإيصالات +
  expiry (المستودع وهمي للاختبار).
- 🪨 [وحش ٤ — التشفير](04-wolf-crypto-identity.md): Ed25519 + X25519 sealed boxes
  عبر `lazysodium-java` (على Maven Central، يشتغل على JVM).
- [wire format](14-wire-format.md) + fragmentation (منطق التجزئة/التجميع).
- [انتخاب البوابة](05-wolf-gateway.md) (المنطق).
- محاكاة كثافة منطقية (in-memory graph) لتعيير الخوارزمية.

dependencies المتاحة من Maven Central: `kotlin-stdlib`,
`kotlinx-coroutines-core`, `com.goterl:lazysodium-java`, `net.java.dev.jna:jna`,
`junit`/`kotlin-test`.

## شنو **ما يُمكن** هنا (يحتاج بيئة فيها SDK + أجهزة)

- [وحش ١ — الخلفية](01-wolf-background-survival.md): Foreground Service،
  BootReceiver، Doze، OEM.
- [وحش ٦ — راديو BLE](06-wolf-ble-transport.md): GATT، advertising، MTU الفعلي.
- [وحش ٧ — Room/SQLCipher](07-wolf-storage.md) والـ KeyVault (Keystore).
- Compose UI.

## المسار للأمام (خيارات)

1. **أصلح البيئة:** أضف `maven.google.com` و`dl.google.com` للـ network
   allowlist بإعدادات البيئة، ثبّت Android SDK → عندها نبدأ بناء Android فعلي
   (M1 أول).
   مرجع إعدادات البيئة: https://code.claude.com/docs/en/claude-code-on-the-web
2. **ابنِ `:core` الآن:** نفّذ المنطق النقي (M2 + M4 + منطق M3/M5) بـ JVM tests
   خضراء فعلية هنا، وأجّل قشرة أندرويد لبيئة مجهّزة.
3. **توثيق فقط:** هذي الحزمة (الوضع الحالي حسب طلبك).

> هذه الوثائق مصمّمة كـ **spec قابل للتنفيذ مباشرة** عند توفّر البيئة الصحيحة.
