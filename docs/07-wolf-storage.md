# 🪨 وحش ٧ — التخزين المحلي أولاً (Local-First Storage)

## المشكلة

كل شي لازم يشتغل ويُحفظ **بلا نت**. القاعدة المحلية هي مصدر الحقيقة الوحيد؛ النت
**ما "يجيب" بيانات — بس يصرّف المخزون** لمن يتوفّر.

اختبار النجاح: **كل البيانات تُكتب/تُقرأ مشفّرة محلياً؛ تنظيف دوري يشطّب المنتهي
بلا نزف ذاكرة.**

---

## ١. التقنية

- **Room** — طبقة ORM فوق SQLite.
- **SQLCipher** — تشفير **عند الراحة (at rest)** لكل القاعدة. مفتاح القاعدة
  مشتق/محمي عبر [Keystore](04-wolf-crypto-identity.md) (مفتاح AES رئيسي).

## ٢. الكيانات الأساسية (Entities)

تفاصيل الحقول والعلاقات الكاملة بـ [وثيقة 08 — نموذج البيانات](08-data-model.md).

| الكيان | الغرض |
|--------|-------|
| `Identity` | المفاتيح (مراجع/ciphertext)، `NodeId` |
| `TrustedContact` | مفتاح عام، اسم ظاهر |
| `Message` | payload، type، state، TTL (قفزات + زمن)، origin، destination، timestamps |
| `SeenMessageCache` | MessageIds الأخيرة (dedup، [وحش ٢](02-wolf-routing.md)) |
| `AggregateRecord` | بيانات تجميعية منتظرة الرفع ([وحش ٥](05-wolf-gateway.md)) |
| `DeliveryReceipt` | الإيصالات ([وحش ٣](03-wolf-store-and-forward.md)) |

## ٣. التنظيف الدوري (Reaping)

مهام دورية (مثلاً عبر coroutine مجدولة بالخدمة):

- **شطب الرزم المنتهية** (`EXPIRED`، تجاوزت 24–48h أو ACKed).
- **تقليم seen-cache** — إزالة الإدخالات الأقدم من `SEEN_SET_TTL`.
- **تقليم الجيران المتقادمين** بجدول الجيران.
- **حدّ أقصى للحجم** — لو امتلأت القاعدة، أسقط الأقدم/الأقل أولوية (الطوارئ تبقى).

## ٤. مبادئ

- **أوفلاين أولاً:** كل عملية UI تقرأ من Room (عبر Flow) — ما تنتظر شبكة أبداً.
- **مصدر الحقيقة واحد:** Room. الـ mesh والـ gateway يصرّفون منه ويكتبون إليه.
- **التشفير عند الراحة إلزامي** — ماكو بيانات حساسة plaintext على القرص.

## ٥. واجهة مقترحة (DAOs مختصرة)

```kotlin
@Dao interface MessageDao {
    @Insert suspend fun insert(m: MessageEntity)
    @Query("UPDATE messages SET state=:s WHERE id=:id")
    suspend fun setState(id: String, s: Int)
    @Query("SELECT * FROM messages WHERE state IN (:active) AND expiresAt > :now")
    suspend fun dueForRebroadcast(active: List<Int>, now: Long): List<MessageEntity>
    @Query("DELETE FROM messages WHERE expiresAt <= :now OR state=:expired")
    suspend fun reap(now: Long, expired: Int): Int
    @Query("SELECT * FROM messages WHERE id=:id")
    fun observe(id: String): Flow<MessageEntity?>
}
```

## ٦. حالات اختبار (instrumented — Room بحاجة بيئة أندرويد)

- [ ] كتابة/قراءة مشفّرة (فتح ملف القاعدة خام ما يكشف plaintext).
- [ ] `reap` يشطّب المنتهي ويترك النشط.
- [ ] `dueForRebroadcast` يرجّع الصح حسب الحالة والوقت.
- [ ] عند امتلاء الحجم، الطوارئ تبقى والأقدم يُسقَط.

## التبعيات

- يخدم كل الوحوش (مستودع مشترك). مفتاح القاعدة من [وحش ٤](04-wolf-crypto-identity.md).
- milestone: **M3** ([وثيقة 11](11-build-plan.md)) — **يحتاج بيئة أندرويد
  (Room/SQLCipher)؛ المنطق اللي فوقه (آلة الحالة) قابل لاختبار JVM بمستودع وهمي.**
