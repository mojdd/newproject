# شريحة — app/src/main/java/com/bitchat/android/geohash/Geohash.kt (الأسطر 1–150)

```
1: package com.bitchat.android.geohash
```
> يُعلن أنّ هذا الملف ينتمي إلى الحزمة (package) المسمّاة `com.bitchat.android.geohash`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:2]

```
3: /**
```
> تعليق: بداية تعليق توثيق (مستند) متعدّد الأسطر. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:3]

```
4:  * Lightweight Geohash encoder used for Location Channels.
```
> تعليق: مُرمِّز جيوهاش (Geohash) خفيف يُستعمَل لقنوات الموقع. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:4]

```
5:  * Encodes latitude/longitude to base32 geohash with a fixed precision.
```
> تعليق: يُرمِّز خط العرض/خط الطول إلى جيوهاش بنظام base32 بدقّة ثابتة. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:5]

```
6:  * 
```
> تعليق: سطر فارغ داخل تعليق التوثيق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:6]

```
7:  * Port of iOS implementation for 100% compatibility
```
> تعليق: نقل (port) لتطبيق iOS لتحقيق توافق بنسبة ١٠٠٪. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:7]

```
8:  */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:8]

```
9: object Geohash {
```
> يُعرِّف كائناً مفرداً (object) باسم `Geohash` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:9]

```
10:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:10]

```
11:     private val base32Chars = "0123456789bcdefghjkmnpqrstuvwxyz".toCharArray()
```
> يُعرِّف ثابتاً خاصّاً (private val) باسم `base32Chars` يُسنَد إليه نصّ الأحرف `"0123456789bcdefghjkmnpqrstuvwxyz"` محوّلاً إلى مصفوفة أحرف باستدعاء `toCharArray()`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:11]

```
12:     private val charToValue: Map<Char, Int> = base32Chars.withIndex().associate { it.value to it.index }
```
> يُعرِّف ثابتاً خاصّاً باسم `charToValue` من نوع خريطة `Map<Char, Int>`، يُبنى بأخذ `base32Chars` مع فهارسها عبر `withIndex()` ثمّ `associate` الذي يربط كلّ حرف `it.value` بفهرسه `it.index`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:12]

```
13: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:13]

```
14:     data class Bounds(val latMin: Double, val latMax: Double, val lonMin: Double, val lonMax: Double)
```
> يُعرِّف صنف بيانات (data class) باسم `Bounds` (حدود) بأربعة ثوابت من نوع `Double`: `latMin` و`latMax` و`lonMin` و`lonMax`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:14]

```
15: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:15]

```
16:     /**
```
> تعليق: بداية تعليق توثيق متعدّد الأسطر. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:16]

```
17:      * Encodes the provided coordinates into a geohash string.
```
> تعليق: يُرمِّز الإحداثيات المُعطاة إلى نصّ جيوهاش. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:17]

```
18:      * @param latitude Latitude in degrees (-90...90)
```
> تعليق: المعامل `latitude` خط العرض بالدرجات (-90...90). [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:18]

```
19:      * @param longitude Longitude in degrees (-180...180)
```
> تعليق: المعامل `longitude` خط الطول بالدرجات (-180...180). [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:19]

```
20:      * @param precision Number of geohash characters (2-12 typical). Values <= 0 return an empty string.
```
> تعليق: المعامل `precision` عدد أحرف الجيوهاش (٢-١٢ نموذجياً). القيم الأصغر من أو تساوي ٠ تُعيد نصّاً فارغاً. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:20]

```
21:      * @return Base32 geohash string of length `precision`.
```
> تعليق: يُعيد نصّ جيوهاش base32 بطول `precision`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:21]

```
22:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:22]

```
23:     fun encode(latitude: Double, longitude: Double, precision: Int): String {
```
> يُعرِّف دالّة (fun) باسم `encode` بمعاملات `latitude` من نوع `Double` و`longitude` من نوع `Double` و`precision` من نوع `Int`، وتُعيد قيمة من نوع `String`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:23]

```
24:         if (precision <= 0) return ""
```
> إذا كان `precision` أصغر من أو يساوي ٠ فإنّها تُعيد نصّاً فارغاً `""`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:25]

```
26:         var latInterval = -90.0 to 90.0
```
> يُعرِّف متغيّراً (var) باسم `latInterval` يُسنَد إليه الزوج `-90.0 to 90.0`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:26]

```
27:         var lonInterval = -180.0 to 180.0
```
> يُعرِّف متغيّراً باسم `lonInterval` يُسنَد إليه الزوج `-180.0 to 180.0`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:28]

```
29:         var isEven = true
```
> يُعرِّف متغيّراً باسم `isEven` (هل هو زوجي) يُسنَد إليه القيمة `true`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:29]

```
30:         var bit = 0
```
> يُعرِّف متغيّراً باسم `bit` (بِت) يُسنَد إليه القيمة `0`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:30]

```
31:         var ch = 0
```
> يُعرِّف متغيّراً باسم `ch` يُسنَد إليه القيمة `0`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:31]

```
32:         val geohash = StringBuilder()
```
> يُعرِّف ثابتاً باسم `geohash` يُسنَد إليه كائن `StringBuilder()` جديد. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:33]

```
34:         val lat = latitude.coerceIn(-90.0, 90.0)
```
> يُعرِّف ثابتاً باسم `lat` يُسنَد إليه `latitude` بعد حصره بين `-90.0` و`90.0` عبر `coerceIn`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:34]

```
35:         val lon = longitude.coerceIn(-180.0, 180.0)
```
> يُعرِّف ثابتاً باسم `lon` يُسنَد إليه `longitude` بعد حصره بين `-180.0` و`180.0` عبر `coerceIn`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:36]

```
37:         while (geohash.length < precision) {
```
> يفتح حلقة `while` تستمرّ ما دام طول `geohash` أصغر من `precision`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:37]

```
38:             if (isEven) {
```
> يفتح شرط `if` يُختبَر فيه ما إذا كان `isEven` صحيحاً. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:38]

```
39:                 val mid = (lonInterval.first + lonInterval.second) / 2
```
> يُعرِّف ثابتاً باسم `mid` (الوسط) يُسنَد إليه ناتج جمع `lonInterval.first` و`lonInterval.second` مقسوماً على ٢. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:39]

```
40:                 if (lon >= mid) {
```
> يفتح شرط `if` يُختبَر فيه ما إذا كان `lon` أكبر من أو يساوي `mid`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:40]

```
41:                     ch = ch or (1 shl (4 - bit))
```
> يُسنِد إلى `ch` ناتج عملية «أو» الثنائية (or) بين `ch` والقيمة `1` مُزاحة لليسار (shl) بمقدار `4 - bit`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:41]

```
42:                     lonInterval = mid to lonInterval.second
```
> يُسنِد إلى `lonInterval` الزوج `mid to lonInterval.second`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:42]

```
43:                 } else {
```
> إغلاق فرع `if` وفتح فرع `else`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:43]

```
44:                     lonInterval = lonInterval.first to mid
```
> يُسنِد إلى `lonInterval` الزوج `lonInterval.first to mid`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:44]

```
45:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:45]

```
46:             } else {
```
> إغلاق فرع `if (isEven)` وفتح فرع `else`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:46]

```
47:                 val mid = (latInterval.first + latInterval.second) / 2
```
> يُعرِّف ثابتاً باسم `mid` يُسنَد إليه ناتج جمع `latInterval.first` و`latInterval.second` مقسوماً على ٢. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:47]

```
48:                 if (lat >= mid) {
```
> يفتح شرط `if` يُختبَر فيه ما إذا كان `lat` أكبر من أو يساوي `mid`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:48]

```
49:                     ch = ch or (1 shl (4 - bit))
```
> يُسنِد إلى `ch` ناتج عملية «أو» الثنائية بين `ch` والقيمة `1` مُزاحة لليسار بمقدار `4 - bit`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:49]

```
50:                     latInterval = mid to latInterval.second
```
> يُسنِد إلى `latInterval` الزوج `mid to latInterval.second`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:50]

```
51:                 } else {
```
> إغلاق فرع `if` وفتح فرع `else`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:51]

```
52:                     latInterval = latInterval.first to mid
```
> يُسنِد إلى `latInterval` الزوج `latInterval.first to mid`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:52]

```
53:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:53]

```
54:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:54]

```
55: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:55]

```
56:             isEven = !isEven
```
> يُسنِد إلى `isEven` نفيه (`!isEven`). [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:56]

```
57:             if (bit < 4) {
```
> يفتح شرط `if` يُختبَر فيه ما إذا كان `bit` أصغر من `4`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:57]

```
58:                 bit += 1
```
> يزيد `bit` بمقدار `1`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:58]

```
59:             } else {
```
> إغلاق فرع `if` وفتح فرع `else`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:59]

```
60:                 geohash.append(base32Chars[ch])
```
> يستدعي `geohash.append` لإلحاق الحرف `base32Chars[ch]` (الحرف عند الفهرس `ch`). [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:60]

```
61:                 bit = 0
```
> يُسنِد إلى `bit` القيمة `0`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:61]

```
62:                 ch = 0
```
> يُسنِد إلى `ch` القيمة `0`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:62]

```
63:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:63]

```
64:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:65]

```
66:         return geohash.toString()
```
> تُعيد ناتج استدعاء `geohash.toString()`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:66]

```
67:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:67]

```
68: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:68]

```
69:     /**
```
> تعليق: بداية تعليق توثيق متعدّد الأسطر. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:69]

```
70:      * Decodes a geohash string to the center latitude/longitude of its cell.
```
> تعليق: يفكّ ترميز نصّ جيوهاش إلى خط العرض/خط الطول المركزي لخليّته. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:70]

```
71:      * @return Pair(latitude, longitude)
```
> تعليق: يُعيد زوجاً `Pair(latitude, longitude)`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:71]

```
72:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:72]

```
73:     fun decodeToCenter(geohash: String): Pair<Double, Double> {
```
> يُعرِّف دالّة باسم `decodeToCenter` (فكّ الترميز إلى المركز) بمعامل `geohash` من نوع `String`، وتُعيد قيمة من نوع `Pair<Double, Double>`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:73]

```
74:         val b = decodeToBounds(geohash)
```
> يُعرِّف ثابتاً باسم `b` يُسنَد إليه ناتج استدعاء `decodeToBounds(geohash)`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:74]

```
75:         val latCenter = (b.latMin + b.latMax) / 2
```
> يُعرِّف ثابتاً باسم `latCenter` يُسنَد إليه ناتج جمع `b.latMin` و`b.latMax` مقسوماً على ٢. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:75]

```
76:         val lonCenter = (b.lonMin + b.lonMax) / 2
```
> يُعرِّف ثابتاً باسم `lonCenter` يُسنَد إليه ناتج جمع `b.lonMin` و`b.lonMax` مقسوماً على ٢. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:76]

```
77:         return latCenter to lonCenter
```
> تُعيد الزوج `latCenter to lonCenter`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:77]

```
78:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:78]

```
79: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:79]

```
80:     /**
```
> تعليق: بداية تعليق توثيق متعدّد الأسطر. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:80]

```
81:      * Decodes a geohash string to bounding box (lat/lon min/max).
```
> تعليق: يفكّ ترميز نصّ جيوهاش إلى صندوق محيط (أدنى/أقصى لخط العرض/خط الطول). [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:81]

```
82:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:82]

```
83:     fun decodeToBounds(geohash: String): Bounds {
```
> يُعرِّف دالّة باسم `decodeToBounds` (فكّ الترميز إلى حدود) بمعامل `geohash` من نوع `String`، وتُعيد قيمة من نوع `Bounds`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:83]

```
84:         if (geohash.isEmpty()) return Bounds(0.0, 0.0, 0.0, 0.0)
```
> إذا كان `geohash` فارغاً (`isEmpty()`) فإنّها تُعيد `Bounds(0.0, 0.0, 0.0, 0.0)`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:84]

```
85: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:85]

```
86:         var latInterval = -90.0 to 90.0
```
> يُعرِّف متغيّراً باسم `latInterval` يُسنَد إليه الزوج `-90.0 to 90.0`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:86]

```
87:         var lonInterval = -180.0 to 180.0
```
> يُعرِّف متغيّراً باسم `lonInterval` يُسنَد إليه الزوج `-180.0 to 180.0`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:87]

```
88:         var isEven = true
```
> يُعرِّف متغيّراً باسم `isEven` يُسنَد إليه القيمة `true`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:88]

```
89: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:89]

```
90:         geohash.lowercase().forEach { ch ->
```
> يستدعي `geohash.lowercase()` لتحويل النصّ إلى أحرف صغيرة، ثمّ `forEach` يمرّ على كلّ حرف مسمّى `ch`، ويفتح جسم اللامدا. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:90]

```
91:             val cd = charToValue[ch] ?: return Bounds(0.0, 0.0, 0.0, 0.0)
```
> يُعرِّف ثابتاً باسم `cd` يُسنَد إليه `charToValue[ch]`، وإن كان `null` فإنّها تُعيد `Bounds(0.0, 0.0, 0.0, 0.0)` عبر معامل إلفيس (`?:`). [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:91]

```
92:             for (mask in intArrayOf(16, 8, 4, 2, 1)) {
```
> يفتح حلقة `for` تمرّ على المتغيّر `mask` ضمن مصفوفة الأعداد الصحيحة `intArrayOf(16, 8, 4, 2, 1)`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:92]

```
93:                 if (isEven) {
```
> يفتح شرط `if` يُختبَر فيه ما إذا كان `isEven` صحيحاً. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:93]

```
94:                     val mid = (lonInterval.first + lonInterval.second) / 2
```
> يُعرِّف ثابتاً باسم `mid` يُسنَد إليه ناتج جمع `lonInterval.first` و`lonInterval.second` مقسوماً على ٢. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:94]

```
95:                     if ((cd and mask) != 0) {
```
> يفتح شرط `if` يُختبَر فيه ما إذا كان ناتج عملية «و» الثنائية (and) بين `cd` و`mask` لا يساوي `0`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:95]

```
96:                         lonInterval = mid to lonInterval.second
```
> يُسنِد إلى `lonInterval` الزوج `mid to lonInterval.second`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:96]

```
97:                     } else {
```
> إغلاق فرع `if` وفتح فرع `else`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:97]

```
98:                         lonInterval = lonInterval.first to mid
```
> يُسنِد إلى `lonInterval` الزوج `lonInterval.first to mid`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:98]

```
99:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:99]

```
100:                 } else {
```
> إغلاق فرع `if (isEven)` وفتح فرع `else`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:100]

```
101:                     val mid = (latInterval.first + latInterval.second) / 2
```
> يُعرِّف ثابتاً باسم `mid` يُسنَد إليه ناتج جمع `latInterval.first` و`latInterval.second` مقسوماً على ٢. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:101]

```
102:                     if ((cd and mask) != 0) {
```
> يفتح شرط `if` يُختبَر فيه ما إذا كان ناتج عملية «و» الثنائية بين `cd` و`mask` لا يساوي `0`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:102]

```
103:                         latInterval = mid to latInterval.second
```
> يُسنِد إلى `latInterval` الزوج `mid to latInterval.second`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:103]

```
104:                     } else {
```
> إغلاق فرع `if` وفتح فرع `else`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:104]

```
105:                         latInterval = latInterval.first to mid
```
> يُسنِد إلى `latInterval` الزوج `latInterval.first to mid`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:105]

```
106:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:106]

```
107:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:107]

```
108:                 isEven = !isEven
```
> يُسنِد إلى `isEven` نفيه (`!isEven`). [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:108]

```
109:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:109]

```
110:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:110]

```
111:         return Bounds(
```
> تُعيد كائن `Bounds(` مع فتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:111]

```
112:             latMin = minOf(latInterval.first, latInterval.second),
```
> يُسنِد إلى الوسيط `latMin` ناتج `minOf(latInterval.first, latInterval.second)` (الأصغر بينهما). [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:112]

```
113:             latMax = maxOf(latInterval.first, latInterval.second),
```
> يُسنِد إلى الوسيط `latMax` ناتج `maxOf(latInterval.first, latInterval.second)` (الأكبر بينهما). [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:113]

```
114:             lonMin = minOf(lonInterval.first, lonInterval.second),
```
> يُسنِد إلى الوسيط `lonMin` ناتج `minOf(lonInterval.first, lonInterval.second)`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:114]

```
115:             lonMax = maxOf(lonInterval.first, lonInterval.second)
```
> يُسنِد إلى الوسيط `lonMax` ناتج `maxOf(lonInterval.first, lonInterval.second)`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:115]

```
116:         )
```
> إغلاق قائمة وسائط `Bounds`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:116]

```
117:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:117]

```
118: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:118]

```
119:     /**
```
> تعليق: بداية تعليق توثيق متعدّد الأسطر. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:119]

```
120:      * Returns the 8 neighboring geohash cells at the same precision as the input.
```
> تعليق: يُعيد خلايا الجيوهاش المجاورة الثماني بنفس دقّة المُدخَل. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:120]

```
121:      * Neighbors include N, NE, E, SE, S, SW, W, NW, even when crossing parent cell boundaries.
```
> تعليق: المجاورات تشمل الشمال والشمال الشرقي والشرق والجنوب الشرقي والجنوب والجنوب الغربي والغرب والشمال الغربي، حتّى عند عبور حدود الخليّة الأمّ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:121]

```
122:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:122]

```
123:     fun neighborsSamePrecision(geohash: String): Set<String> {
```
> يُعرِّف دالّة باسم `neighborsSamePrecision` (المجاورات بنفس الدقّة) بمعامل `geohash` من نوع `String`، وتُعيد قيمة من نوع `Set<String>`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:123]

```
124:         if (geohash.isEmpty()) return emptySet()
```
> إذا كان `geohash` فارغاً فإنّها تُعيد مجموعة فارغة عبر `emptySet()`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:124]

```
125:         val p = geohash.length
```
> يُعرِّف ثابتاً باسم `p` يُسنَد إليه طول `geohash` (`geohash.length`). [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:125]

```
126:         val b = decodeToBounds(geohash)
```
> يُعرِّف ثابتاً باسم `b` يُسنَد إليه ناتج استدعاء `decodeToBounds(geohash)`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:126]

```
127:         val dLat = b.latMax - b.latMin
```
> يُعرِّف ثابتاً باسم `dLat` يُسنَد إليه ناتج طرح `b.latMin` من `b.latMax`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:127]

```
128:         val dLon = b.lonMax - b.lonMin
```
> يُعرِّف ثابتاً باسم `dLon` يُسنَد إليه ناتج طرح `b.lonMin` من `b.lonMax`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:128]

```
129: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:129]

```
130:         fun wrapLon(lon: Double): Double {
```
> يُعرِّف دالّة محليّة باسم `wrapLon` (لفّ خط الطول) بمعامل `lon` من نوع `Double`، وتُعيد قيمة من نوع `Double`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:130]

```
131:             var x = lon
```
> يُعرِّف متغيّراً باسم `x` يُسنَد إليه `lon`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:131]

```
132:             while (x > 180.0) x -= 360.0
```
> حلقة `while` تستمرّ ما دام `x` أكبر من `180.0`، وتنقص `x` بمقدار `360.0` في كلّ دورة. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:132]

```
133:             while (x < -180.0) x += 360.0
```
> حلقة `while` تستمرّ ما دام `x` أصغر من `-180.0`، وتزيد `x` بمقدار `360.0` في كلّ دورة. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:133]

```
134:             return x
```
> تُعيد قيمة `x`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:134]

```
135:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:135]

```
136: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:136]

```
137:         val neighbors = mutableSetOf<String>()
```
> يُعرِّف ثابتاً باسم `neighbors` (المجاورات) يُسنَد إليه مجموعة قابلة للتعديل من نوع `String` عبر `mutableSetOf<String>()`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:137]

```
138:         for (dy in -1..1) {
```
> يفتح حلقة `for` تمرّ على المتغيّر `dy` ضمن المدى `-1..1`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:138]

```
139:             for (dx in -1..1) {
```
> يفتح حلقة `for` تمرّ على المتغيّر `dx` ضمن المدى `-1..1`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:139]

```
140:                 if (dx == 0 && dy == 0) continue // skip center
```
> إذا كان `dx` يساوي `0` و`dy` يساوي `0` فإنّها تتخطّى الدورة عبر `continue`؛ تعليق: تخطّي المركز. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:140]

```
141:                 val centerLat = (b.latMin + b.latMax) / 2 + dy * dLat
```
> يُعرِّف ثابتاً باسم `centerLat` يُسنَد إليه ناتج جمع `b.latMin` و`b.latMax` مقسوماً على ٢ مضافاً إليه `dy * dLat`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:141]

```
142:                 val rawLonCenter = (b.lonMin + b.lonMax) / 2 + dx * dLon
```
> يُعرِّف ثابتاً باسم `rawLonCenter` يُسنَد إليه ناتج جمع `b.lonMin` و`b.lonMax` مقسوماً على ٢ مضافاً إليه `dx * dLon`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:142]

```
143:                 val centerLon = wrapLon(rawLonCenter)
```
> يُعرِّف ثابتاً باسم `centerLon` يُسنَد إليه ناتج استدعاء `wrapLon(rawLonCenter)`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:143]

```
144:                 val enc = encode(centerLat.coerceIn(-90.0, 90.0), centerLon, p)
```
> يُعرِّف ثابتاً باسم `enc` يُسنَد إليه ناتج استدعاء `encode` بوسائط `centerLat` محصوراً بين `-90.0` و`90.0` عبر `coerceIn`، و`centerLon`، و`p`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:144]

```
145:                 if (enc.isNotEmpty() && enc != geohash) neighbors.add(enc)
```
> إذا كان `enc` غير فارغ (`isNotEmpty()`) و`enc` لا يساوي `geohash` فإنّها تضيف `enc` إلى `neighbors` عبر `add`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:145]

```
146:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:146]

```
147:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:147]

```
148:         return neighbors
```
> تُعيد `neighbors`. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:148]

```
149:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:149]

```
150: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/Geohash.kt:150]
