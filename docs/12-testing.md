# 12 — استراتيجية الاختبار

## ١. اختبارات الوحدة (Unit — JVM، بلا أجهزة)

تغطّي **المنطق النقي** (قابل للتشغيل بالبيئة السحابية الحالية عبر `:core`):

- **التوجيه** ([وحش ٢](02-wolf-routing.md)): TTL، dedup (seen-set/Bloom)،
  suppression، أولوية الطوارئ.
- **آلة الحالة** ([وحش ٣](03-wolf-store-and-forward.md)): الانتقالات، مطابقة
  الإيصالات، الـ expiry.
- **التشفير** ([وحش ٤](04-wolf-crypto-identity.md)): seal/unseal، sign/verify،
  رفض التزوير — عبر `lazysodium-java`.
- **wire format / fragmentation**: ترميز/فك، split/reassemble، حقول معطوبة.
- **انتخاب البوابة** ([وحش ٥](05-wolf-gateway.md)): مقارنة score، idempotency.

## ٢. اختبارات التكامل (Instrumented — أجهزة حقيقية)

- **لا يكفي محاكي للـ BLE** — لازم أجهزة فعلية متعددة.
- Room + SQLCipher، Keystore، Foreground Service، BLE GATT، advertising/scanning.

## ٣. محاكاة الكثافة (Density Simulation)

- اختبر بـ **٥ → ١٠ → ٢٠+ جهاز** لرصد سلوك الفيضان والعاصفة.
- عاير معاملات [وحش ٢](02-wolf-routing.md) (TTL، نافذة suppression، threshold)
  حسب النتائج.
- **محاكاة منطقية على JVM ممكنة جزئياً:** نموذج عقد افتراضية (in-memory graph)
  يمرّر رزم عبر `Router` النقي → نقيس عدد الإعادات، الوصول، الحلقات. مفيد لتعيير
  الخوارزمية قبل الأجهزة.

## ٤. صمود الخلفية (Background Survival)

- اترك الجهاز **ساعة** بالخلفية + أعد تشغيله، وتأكد إنه يبقى عقدة relay.
- اختبر عبر OEMات مختلفة (Xiaomi، Huawei، Samsung، Oppo) — كل واحد سلوك مختلف.

## ٥. البطارية

- قِس الاستهلاك بالخلفية على مدى ساعات، عبر power profiles
  ([وحش ١](01-wolf-background-survival.md)).
- تحقّق إن WakeLock ما يُمسَك إلا أثناء معالجة فعلية.

---

## ما يُمكن اختباره **الآن** (البيئة السحابية الحالية)

| القسم | قابل للاختبار JVM؟ |
|-------|---------------------|
| التوجيه (TTL/dedup/suppression) | ✅ كامل |
| آلة الحالة (store-and-forward) | ✅ كامل (بمستودع وهمي) |
| التشفير (seal/sign/verify) | ✅ كامل (lazysodium-java) |
| wire format / fragmentation | ✅ كامل |
| انتخاب البوابة | ✅ المنطق |
| محاكاة الكثافة المنطقية | ✅ جزئياً (in-memory) |
| كل ما يخص BLE/الخلفية/Room/Keystore/UI | ⛔ يحتاج SDK + أجهزة |

تفاصيل القيود: [وثيقة 13](13-environment-and-status.md).
