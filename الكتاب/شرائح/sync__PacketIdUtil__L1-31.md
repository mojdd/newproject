# شريحة — app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt (الأسطر 1–31)

```
1: package com.bitchat.android.sync
```
> يُعرّف انتماء الملف إلى الحُزمة (package) باسم `com.bitchat.android.sync`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:2]

```
3: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد (import) الصنف `BitchatPacket` من الحُزمة `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:3]

```
4: import java.security.MessageDigest
```
> يستورد الصنف `MessageDigest` من الحُزمة `java.security`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:5]

```
6: /**
```
> تعليق: بداية كتلة توثيق (تعليق وثائقي). [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:6]

```
7:  * Deterministic packet ID helper for sync purposes.
```
> تعليق: «مساعد معرّف حُزمة حتمي لأغراض المزامنة». [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:7]

```
8:  * Uses SHA-256 over a canonical subset of packet fields:
```
> تعليق: «يستعمل SHA-256 على مجموعة جزئية معيارية من حقول الحُزمة:». [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:8]

```
9:  * [type | senderID | timestamp | payload] to generate a stable ID.
```
> تعليق: «[النوع | معرّف المُرسِل | الطابع الزمني | الحمولة] لتوليد معرّف ثابت». [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:9]

```
10:  * Returns a 16-byte (128-bit) truncated hash for compactness.
```
> تعليق: «يُعيد تجزئة (hash) مقطوعة بطول 16 بايت (128 بِت) من أجل الإيجاز». [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:10]

```
11:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:11]

```
12: object PacketIdUtil {
```
> يُعرّف كائناً مفرداً (object) باسم `PacketIdUtil` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:12]

```
13:     fun computeIdBytes(packet: BitchatPacket): ByteArray {
```
> يُعرّف دالّة (fun) باسم `computeIdBytes` تأخذ وسيطاً `packet` من نوع `BitchatPacket` وتُعيد قيمة من نوع `ByteArray`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:13]

```
14:         val md = MessageDigest.getInstance("SHA-256")
```
> يُعرّف متغيّراً ثابتاً (val) باسم `md` ويضبط قيمته على ناتج استدعاء `MessageDigest.getInstance` بالوسيط النصّي `"SHA-256"`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:14]

```
15:         md.update(packet.type.toByte())
```
> يستدعي `update` على `md` بوسيط هو ناتج استدعاء `toByte` على الحقل `packet.type`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:15]

```
16:         md.update(packet.senderID)
```
> يستدعي `update` على `md` بوسيط هو الحقل `packet.senderID`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:16]

```
17:         // Timestamp as 8 bytes big-endian
```
> تعليق: «الطابع الزمني كـ 8 بايت بترتيب البايت الأكبر أولاً (big-endian)». [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:17]

```
18:         val ts = packet.timestamp.toLong()
```
> يُعرّف متغيّراً ثابتاً (val) باسم `ts` ويضبط قيمته على ناتج استدعاء `toLong` على الحقل `packet.timestamp`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:18]

```
19:         for (i in 7 downTo 0) {
```
> يفتح حلقة `for` يأخذ فيها المتغيّر `i` القيم من 7 تنازلياً حتى 0 (downTo)، ويفتح جسمها. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:19]

```
20:             md.update(((ts ushr (i * 8)) and 0xFF).toByte())
```
> يستدعي `update` على `md` بوسيط هو ناتج استدعاء `toByte` على القيمة الناتجة عن إجراء عملية «و» المنطقية (and) مع `0xFF` على ناتج إزاحة `ts` يميناً بلا إشارة (ushr) بمقدار `(i * 8)`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:20]

```
21:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:21]

```
22:         md.update(packet.payload)
```
> يستدعي `update` على `md` بوسيط هو الحقل `packet.payload`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:22]

```
23:         val digest = md.digest()
```
> يُعرّف متغيّراً ثابتاً (val) باسم `digest` ويضبط قيمته على ناتج استدعاء `digest` على `md`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:23]

```
24:         return digest.copyOf(16) // 128-bit ID
```
> يُعيد ناتج استدعاء `copyOf` على `digest` بالوسيط `16`؛ وفي آخر السطر تعليق: «معرّف بطول 128 بِت». [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:24]

```
25:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:25]

```
26: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:26]

```
27:     fun computeIdHex(packet: BitchatPacket): String {
```
> يُعرّف دالّة (fun) باسم `computeIdHex` تأخذ وسيطاً `packet` من نوع `BitchatPacket` وتُعيد قيمة من نوع `String`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:27]

```
28:         return computeIdBytes(packet).joinToString("") { b -> "%02x".format(b) }
```
> يُعيد ناتج استدعاء `joinToString` بالفاصل النصّي الفارغ `""` على ناتج استدعاء `computeIdBytes(packet)`، مع دالّة لامدا (lambda) تأخذ العنصر `b` وتُعيد ناتج استدعاء `format` على النصّ `"%02x"` بالوسيط `b`. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:28]

```
29:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:29]

```
30: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:30]

```
31: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/PacketIdUtil.kt:31]
