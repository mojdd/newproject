# شريحة — app/src/main/java/com/bitchat/android/nostr/Bech32.kt (الأسطر 1–132)

```
1: package com.bitchat.android.nostr
```
> يُعرّف الحزمة (package) باسم `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:2]

```
3: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:3]

```
4:  * Bech32 encoding/decoding implementation for Nostr
```
> تعليق: تنفيذ ترميز/فك ترميز Bech32 لأجل Nostr. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:4]

```
5:  * Used for npub/nsec encoding
```
> تعليق: يُستعمَل لترميز npub/nsec. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:5]

```
6:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:6]

```
7: object Bech32 {
```
> يُعرّف كائناً مفرداً (object) باسم `Bech32` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:7]

```
8:     private const val CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
```
> يُعرّف ثابتاً خاصاً (CHARSET) من نوع نص قيمته `"qpzry9x8gf2tvdw0s3jn54khce6mua7l"`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:8]

```
9:     private val GENERATOR = intArrayOf(0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3)
```
> يُعرّف متغيّراً ثابتاً خاصاً (GENERATOR) من نوع مصفوفة أعداد صحيحة قيمها `0x3b6a57b2` و`0x26508e6d` و`0x1ea119fa` و`0x3d4233dd` و`0x2a1462b3`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:9]

```
10:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:10]

```
11:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:11]

```
12:      * Encode data with HRP (Human Readable Part)
```
> تعليق: ترميز البيانات مع HRP (الجزء المقروء بشرياً). [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:12]

```
13:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:13]

```
14:     fun encode(hrp: String, data: ByteArray): String {
```
> يُعرّف دالة (encode) تأخذ نصاً `hrp` ومصفوفة بايتات `data` وتُعيد نصاً، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:14]

```
15:         val values = convertBits(data, 8, 5, true).toList()
```
> يُعرّف قيمة (values) ناتجة عن استدعاء `convertBits` بالوسائط `data` و`8` و`5` و`true` ثم تحويلها إلى قائمة. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:15]

```
16:         val checksum = createChecksum(hrp, values)
```
> يُعرّف قيمة (checksum) ناتجة عن استدعاء `createChecksum` بالوسيطين `hrp` و`values`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:16]

```
17:         val combined = values + checksum
```
> يُعرّف قيمة (combined) تساوي ضمّ `values` و`checksum`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:17]

```
18:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:18]

```
19:         return hrp + "1" + combined.map { CHARSET[it] }.joinToString("")
```
> يُعيد ضمّ `hrp` والنص `"1"` ونتيجة تحويل كل عنصر في `combined` إلى الحرف `CHARSET[it]` ثم وصلها بنص فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:19]

```
20:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:20]

```
21:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:21]

```
22:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:22]

```
23:      * Decode bech32 string
```
> تعليق: فكّ ترميز نص bech32. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:23]

```
24:      * Returns (hrp, data) pair
```
> تعليق: يُعيد زوجاً (hrp, data). [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:24]

```
25:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:25]

```
26:     fun decode(bech32String: String): Pair<String, ByteArray> {
```
> يُعرّف دالة (decode) تأخذ نصاً `bech32String` وتُعيد زوجاً (Pair) من نص ومصفوفة بايتات، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:26]

```
27:         val separatorIndex = bech32String.lastIndexOf('1')
```
> يُعرّف قيمة (separatorIndex) تساوي موضع آخر ظهور للحرف `'1'` في `bech32String`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:27]

```
28:         require(separatorIndex >= 0) { "No separator found" }
```
> يستدعي `require` بشرط أن يكون `separatorIndex >= 0` ورسالة الخطأ `"No separator found"`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:28]

```
29:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:29]

```
30:         val hrp = bech32String.substring(0, separatorIndex)
```
> يُعرّف قيمة (hrp) تساوي المقطع النصي من `bech32String` من الموضع `0` حتى `separatorIndex`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:30]

```
31:         val dataString = bech32String.substring(separatorIndex + 1)
```
> يُعرّف قيمة (dataString) تساوي المقطع النصي من `bech32String` ابتداءً من الموضع `separatorIndex + 1`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:31]

```
32:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:32]

```
33:         // Validate HRP contains only ASCII
```
> تعليق: التحقّق أنّ HRP يحتوي محارف ASCII فقط. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:33]

```
34:         require(hrp.all { it.code < 128 }) { "Invalid HRP characters" }
```
> يستدعي `require` بشرط أن تكون شيفرة كل محرف في `hrp` أصغر من `128` ورسالة الخطأ `"Invalid HRP characters"`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:34]

```
35:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:35]

```
36:         // Convert characters to values
```
> تعليق: تحويل المحارف إلى قيم. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:36]

```
37:         val values = dataString.map { char ->
```
> يُعرّف قيمة (values) عبر تطبيق `map` على `dataString` مع متغيّر المحرف `char` ويفتح نطاق اللامدا. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:37]

```
38:             val index = CHARSET.indexOf(char)
```
> يُعرّف قيمة (index) تساوي موضع `char` داخل `CHARSET`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:38]

```
39:             require(index >= 0) { "Invalid character: $char" }
```
> يستدعي `require` بشرط أن يكون `index >= 0` ورسالة الخطأ `"Invalid character: $char"` المُدمَجة فيها قيمة `char`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:39]

```
40:             index
```
> يُعيد `index` كقيمة لِلامدا. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:40]

```
41:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:41]

```
42:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:42]

```
43:         // Verify checksum
```
> تعليق: التحقّق من المجموع الاختباري (checksum). [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:43]

```
44:         require(values.size >= 6) { "Data too short" }
```
> يستدعي `require` بشرط أن يكون حجم `values` أكبر من أو يساوي `6` ورسالة الخطأ `"Data too short"`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:44]

```
45:         val payloadValues = values.dropLast(6)
```
> يُعرّف قيمة (payloadValues) تساوي `values` بعد إسقاط آخر `6` عناصر. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:45]

```
46:         val checksum = values.takeLast(6)
```
> يُعرّف قيمة (checksum) تساوي آخر `6` عناصر من `values`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:46]

```
47:         val expectedChecksum = createChecksum(hrp, payloadValues)
```
> يُعرّف قيمة (expectedChecksum) ناتجة عن استدعاء `createChecksum` بالوسيطين `hrp` و`payloadValues`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:47]

```
48:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:48]

```
49:         require(checksum == expectedChecksum) { "Invalid checksum" }
```
> يستدعي `require` بشرط أن يساوي `checksum` قيمة `expectedChecksum` ورسالة الخطأ `"Invalid checksum"`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:49]

```
50:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:50]

```
51:         // Convert back to bytes
```
> تعليق: التحويل عودةً إلى بايتات. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:51]

```
52:         val bytesInt = convertBits(payloadValues.toIntArray(), 5, 8, false)
```
> يُعرّف قيمة (bytesInt) ناتجة عن استدعاء `convertBits` بالوسائط `payloadValues.toIntArray()` و`5` و`8` و`false`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:52]

```
53:         val bytes = bytesInt.map { it.toByte() }.toByteArray()
```
> يُعرّف قيمة (bytes) ناتجة عن تحويل كل عنصر في `bytesInt` إلى بايت ثم جمعها في مصفوفة بايتات. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:53]

```
54:         return Pair(hrp, bytes)
```
> يُعيد زوجاً (Pair) مكوّناً من `hrp` و`bytes`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:54]

```
55:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:55]

```
56:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:56]

```
57:     private fun convertBits(data: ByteArray, fromBits: Int, toBits: Int, pad: Boolean): IntArray {
```
> يُعرّف دالة خاصة (convertBits) تأخذ مصفوفة بايتات `data` وعددين صحيحين `fromBits` و`toBits` وقيمة منطقية `pad` وتُعيد مصفوفة أعداد صحيحة، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:57]

```
58:         return convertBits(data.map { it.toInt() and 0xFF }.toIntArray(), fromBits, toBits, pad)
```
> يُعيد استدعاء `convertBits` بعد تحويل كل بايت في `data` إلى عدد صحيح مقنّع بـ`0xFF` وجمعه في مصفوفة أعداد، مع تمرير `fromBits` و`toBits` و`pad`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:58]

```
59:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:59]

```
60:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:60]

```
61:     private fun convertBits(data: IntArray, fromBits: Int, toBits: Int, pad: Boolean): IntArray {
```
> يُعرّف دالة خاصة (convertBits) تأخذ مصفوفة أعداد صحيحة `data` وعددين `fromBits` و`toBits` وقيمة منطقية `pad` وتُعيد مصفوفة أعداد صحيحة، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:61]

```
62:         var acc = 0
```
> يُعرّف متغيّراً قابلاً للتغيير (acc) قيمته الابتدائية `0`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:62]

```
63:         var bits = 0
```
> يُعرّف متغيّراً قابلاً للتغيير (bits) قيمته الابتدائية `0`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:63]

```
64:         val result = mutableListOf<Int>()
```
> يُعرّف قيمة (result) قائمةً قابلة للتغيير من أعداد صحيحة فارغة. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:64]

```
65:         val maxv = (1 shl toBits) - 1
```
> يُعرّف قيمة (maxv) تساوي `1` مزاحاً يساراً بمقدار `toBits` ناقص `1`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:65]

```
66:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:66]

```
67:         for (value in data) {
```
> يفتح حلقة `for` تكرّر على كل عنصر `value` في `data`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:67]

```
68:             acc = (acc shl fromBits) or value
```
> يُسنِد إلى `acc` نتيجة إزاحة `acc` يساراً بمقدار `fromBits` ثم تطبيق «أو» الثنائية مع `value`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:68]

```
69:             bits += fromBits
```
> يزيد `bits` بمقدار `fromBits`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:69]

```
70:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:70]

```
71:             while (bits >= toBits) {
```
> يفتح حلقة `while` تستمرّ ما دام `bits >= toBits`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:71]

```
72:                 bits -= toBits
```
> يُنقص `bits` بمقدار `toBits`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:72]

```
73:                 result.add((acc shr bits) and maxv)
```
> يضيف إلى `result` نتيجة إزاحة `acc` يميناً بمقدار `bits` ثم تطبيق «و» الثنائية مع `maxv`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:73]

```
74:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:74]

```
75:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:75]

```
76:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:76]

```
77:         if (pad && bits > 0) {
```
> يفتح شرط `if` يتحقّق إذا كان `pad` صحيحاً و`bits` أكبر من `0`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:77]

```
78:             result.add((acc shl (toBits - bits)) and maxv)
```
> يضيف إلى `result` نتيجة إزاحة `acc` يساراً بمقدار `toBits - bits` ثم تطبيق «و» الثنائية مع `maxv`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:78]

```
79:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:79]

```
80:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:80]

```
81:         return result.toIntArray()
```
> يُعيد `result` محوّلةً إلى مصفوفة أعداد صحيحة. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:81]

```
82:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:82]

```
83:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:83]

```
84:     private fun convertBits(data: List<Int>, fromBits: Int, toBits: Int, pad: Boolean): IntArray {
```
> يُعرّف دالة خاصة (convertBits) تأخذ قائمة أعداد صحيحة `data` وعددين `fromBits` و`toBits` وقيمة منطقية `pad` وتُعيد مصفوفة أعداد صحيحة، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:84]

```
85:         return convertBits(data.toIntArray(), fromBits, toBits, pad)
```
> يُعيد استدعاء `convertBits` بعد تحويل `data` إلى مصفوفة أعداد، مع تمرير `fromBits` و`toBits` و`pad`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:85]

```
86:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:86]

```
87:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:87]

```
88:     private fun createChecksum(hrp: String, values: List<Int>): List<Int> {
```
> يُعرّف دالة خاصة (createChecksum) تأخذ نصاً `hrp` وقائمة أعداد صحيحة `values` وتُعيد قائمة أعداد صحيحة، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:88]

```
89:         val checksumValues = hrpExpand(hrp) + values + intArrayOf(0, 0, 0, 0, 0, 0)
```
> يُعرّف قيمة (checksumValues) تساوي ضمّ ناتج `hrpExpand(hrp)` و`values` ومصفوفة الأعداد `0, 0, 0, 0, 0, 0`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:89]

```
90:         val polymod = polymod(checksumValues) xor 1
```
> يُعرّف قيمة (polymod) تساوي ناتج استدعاء `polymod(checksumValues)` بعد تطبيق «أو الحصرية» (xor) مع `1`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:90]

```
91:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:91]

```
92:         return (0 until 6).map { i ->
```
> يُعيد نتيجة تطبيق `map` على المدى من `0` حتى `6` (غير شامل) مع متغيّر `i` ويفتح نطاق اللامدا. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:92]

```
93:             (polymod shr (5 * (5 - i))) and 31
```
> يُنتِج لكل `i` نتيجة إزاحة `polymod` يميناً بمقدار `5 * (5 - i)` ثم تطبيق «و» الثنائية مع `31`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:93]

```
94:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:94]

```
95:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:95]

```
96:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:96]

```
97:     private fun hrpExpand(hrp: String): IntArray {
```
> يُعرّف دالة خاصة (hrpExpand) تأخذ نصاً `hrp` وتُعيد مصفوفة أعداد صحيحة، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:97]

```
98:         val result = mutableListOf<Int>()
```
> يُعرّف قيمة (result) قائمةً قابلة للتغيير من أعداد صحيحة فارغة. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:98]

```
99:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:99]

```
100:         // High bits
```
> تعليق: البِتّات العليا. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:100]

```
101:         hrp.forEach { c ->
```
> يستدعي `forEach` على `hrp` مع متغيّر المحرف `c` ويفتح نطاق اللامدا. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:101]

```
102:             result.add(c.code shr 5)
```
> يضيف إلى `result` نتيجة إزاحة شيفرة المحرف `c` يميناً بمقدار `5`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:102]

```
103:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:103]

```
104:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:104]

```
105:         // Separator
```
> تعليق: الفاصل. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:105]

```
106:         result.add(0)
```
> يضيف إلى `result` القيمة `0`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:106]

```
107:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:107]

```
108:         // Low bits
```
> تعليق: البِتّات الدنيا. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:108]

```
109:         hrp.forEach { c ->
```
> يستدعي `forEach` على `hrp` مع متغيّر المحرف `c` ويفتح نطاق اللامدا. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:109]

```
110:             result.add(c.code and 31)
```
> يضيف إلى `result` نتيجة تطبيق «و» الثنائية بين شيفرة المحرف `c` و`31`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:110]

```
111:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:111]

```
112:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:112]

```
113:         return result.toIntArray()
```
> يُعيد `result` محوّلةً إلى مصفوفة أعداد صحيحة. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:113]

```
114:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:114]

```
115:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:115]

```
116:     private fun polymod(values: IntArray): Int {
```
> يُعرّف دالة خاصة (polymod) تأخذ مصفوفة أعداد صحيحة `values` وتُعيد عدداً صحيحاً، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:116]

```
117:         var chk = 1
```
> يُعرّف متغيّراً قابلاً للتغيير (chk) قيمته الابتدائية `1`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:117]

```
118:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:118]

```
119:         for (value in values) {
```
> يفتح حلقة `for` تكرّر على كل عنصر `value` في `values`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:119]

```
120:             val b = chk shr 25
```
> يُعرّف قيمة (b) تساوي إزاحة `chk` يميناً بمقدار `25`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:120]

```
121:             chk = (chk and 0x1ffffff) shl 5 xor value
```
> يُسنِد إلى `chk` نتيجة تطبيق «و» بين `chk` و`0x1ffffff` ثم الإزاحة يساراً بمقدار `5` ثم «أو الحصرية» (xor) مع `value`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:121]

```
122:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:122]

```
123:             for (i in 0 until 5) {
```
> يفتح حلقة `for` على المدى من `0` حتى `5` (غير شامل) بالمتغيّر `i`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:123]

```
124:                 if ((b shr i) and 1 == 1) {
```
> يفتح شرط `if` يتحقّق إذا كان ناتج إزاحة `b` يميناً بمقدار `i` ثم «و» مع `1` يساوي `1`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:124]

```
125:                     chk = chk xor GENERATOR[i]
```
> يُسنِد إلى `chk` نتيجة «أو الحصرية» (xor) بين `chk` والعنصر `GENERATOR[i]`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:125]

```
126:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:126]

```
127:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:127]

```
128:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:128]

```
129:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:129]

```
130:         return chk
```
> يُعيد قيمة `chk`. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:130]

```
131:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:131]

```
132: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/Bech32.kt:132]
