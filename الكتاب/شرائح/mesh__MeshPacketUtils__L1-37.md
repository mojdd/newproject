# شريحة — app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt (الأسطر 1–37)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) المسماة com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:2]

```
3: /**
```
> تعليق توثيقي يبدأ هنا (بداية كتلة تعليق). [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:3]

```
4:  * Shared helpers for mesh packet handling.
```
> تعليق: مساعدات مشتركة للتعامل مع رزم الشبكة المتشابكة (mesh packet). [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:4]

```
5:  */
```
> نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:5]

```
6: object MeshPacketUtils {
```
> يعرّف كائناً مفرداً (object) اسمه أدوات رزم الشبكة (MeshPacketUtils) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:6]

```
7:     /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:7]

```
8:      * Convert hex string peer ID to binary data (8 bytes), matching iOS behavior.
```
> تعليق: حوّل معرّف النظير (peer ID) المكتوب كنص ست عشري إلى بيانات ثنائية (٨ بايتات)، بما يطابق سلوك iOS. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:8]

```
9:      */
```
> نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:9]

```
10:     fun hexStringToByteArray(hexString: String): ByteArray {
```
> يعرّف دالة (fun) اسمها من نص ست عشري إلى مصفوفة بايتات (hexStringToByteArray) تأخذ وسيطاً نصياً اسمه hexString وتعيد مصفوفة بايتات (ByteArray)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:10]

```
11:         val result = ByteArray(8) { 0 }
```
> يعرّف قيمة ثابتة (val) اسمها النتيجة (result) ويضبطها مصفوفة بايتات طولها ٨ كل عناصرها مضبوطة على الصفر. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:11]

```
12:         var tempID = hexString
```
> يعرّف متغيراً (var) اسمه المعرّف المؤقت (tempID) ويضبطه على قيمة الوسيط hexString. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:12]

```
13:         var index = 0
```
> يعرّف متغيراً (var) اسمه الفهرس (index) ويضبطه على الصفر. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:13]

```
14: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:14]

```
15:         while (tempID.length >= 2 && index < 8) {
```
> يبدأ حلقة طالما (while) تستمر ما دام طول tempID أكبر من أو يساوي ٢ وقيمة index أصغر من ٨، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:15]

```
16:             val hexByte = tempID.substring(0, 2)
```
> يعرّف قيمة ثابتة اسمها البايت الست عشري (hexByte) ويضبطها على المقطع الفرعي من tempID من الموضع ٠ حتى ٢ (أوّل حرفين). [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:16]

```
17:             val byte = hexByte.toIntOrNull(16)?.toByte()
```
> يعرّف قيمة ثابتة اسمها البايت (byte) ويضبطها على تحويل hexByte إلى عدد صحيح بالأساس ١٦ (أو قيمة لاغية إن فشل) ثم تحويله إلى بايت إن لم يكن لاغياً. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:17]

```
18:             if (byte != null) {
```
> يبدأ شرط إذا (if) كانت قيمة byte ليست لاغية، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:18]

```
19:                 result[index] = byte
```
> يضبط عنصر مصفوفة result عند الموضع index على قيمة byte. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:19]

```
20:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:20]

```
21:             tempID = tempID.substring(2)
```
> يعيد ضبط tempID على المقطع الفرعي منه ابتداءً من الموضع ٢ إلى نهايته. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:21]

```
22:             index++
```
> يزيد قيمة index بمقدار واحد. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:22]

```
23:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:23]

```
24:         return result
```
> يعيد قيمة result. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:24]

```
25:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:25]

```
26: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:26]

```
27:     /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:27]

```
28:      * Hash payloads to a stable hex ID for transfer tracking.
```
> تعليق: جزّئ (hash) الحمولات إلى معرّف ست عشري ثابت لأجل تتبع النقل (transfer tracking). [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:28]

```
29:      */
```
> نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:29]

```
30:     fun sha256Hex(bytes: ByteArray): String = try {
```
> يعرّف دالة اسمها sha256 ست عشري (sha256Hex) تأخذ وسيطاً اسمه bytes من نوع مصفوفة بايتات وتعيد نصاً (String)، وقيمتها هي نتيجة كتلة محاولة (try) تفتح هنا. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:30]

```
31:         val md = java.security.MessageDigest.getInstance("SHA-256")
```
> يعرّف قيمة ثابتة اسمها هاضم الرسالة (md) ويضبطها على نسخة من MessageDigest بالخوارزمية "SHA-256". [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:31]

```
32:         md.update(bytes)
```
> يستدعي على md الدالة update مزوّداً إياها بـ bytes. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:32]

```
33:         md.digest().joinToString("") { "%02x".format(it) }
```
> يستدعي md.digest() ثم يدمج عناصره في نص بفاصل فارغ، حيث يُنسَّق كل عنصر (it) بصيغة ست عشرية من خانتين. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:33]

```
34:     } catch (_: Exception) {
```
> يغلق كتلة المحاولة ويفتح كتلة التقاط (catch) لأي استثناء (Exception) متجاهلاً اسمه. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:34]

```
35:         bytes.size.toString(16)
```
> يعيد (كقيمة لكتلة catch) حجم bytes محوّلاً إلى نص بالأساس ١٦. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:35]

```
36:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:36]

```
37: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshPacketUtils.kt:37]
