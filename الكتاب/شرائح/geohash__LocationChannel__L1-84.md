# شريحة — app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt (الأسطر 1–84)

```
1: package com.bitchat.android.geohash
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) المسماة com.bitchat.android.geohash. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:2]

```
3: /**
```
> بداية تعليق توثيقي (doc comment). [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:3]

```
4:  * Levels of location channels mapped to geohash precisions.
```
> تعليق: «مستويات قنوات الموقع مربوطة بدرجات دقّة جيوهاش (geohash)». [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:4]

```
5:  * Direct port from iOS implementation for 100% compatibility
```
> تعليق: «نقل مباشر من تنفيذ iOS لأجل توافق بنسبة 100%». [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:5]

```
6:  */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:6]

```
7: enum class GeohashChannelLevel(val precision: Int, val displayName: String) {
```
> يعرّف صنفاً تعدادياً (enum class) باسم مستوى قناة الجيوهاش (GeohashChannelLevel)، وله خاصيّتان في باني الإنشاء: عددٌ صحيح للدقّة (precision) باسم precision، ونصٌّ للاسم المعروض (displayName) باسم displayName. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:7]

```
8:     BUILDING(8, "Building"), // iOS: precision 8 for building-level (used for Location Notes)
```
> يعرّف عضو التعداد المبنى (BUILDING) بقيمة دقّة 8 واسم معروض "Building"، ويلحقه تعليق: «iOS: دقّة 8 لمستوى المبنى (تُستعمل لملاحظات الموقع Location Notes)». [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:8]

```
9:     BLOCK(7, "Block"),
```
> يعرّف عضو التعداد الحَيّ/المربّع السكني (BLOCK) بقيمة دقّة 7 واسم معروض "Block". [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:9]

```
10:     NEIGHBORHOOD(6, "Neighborhood"),
```
> يعرّف عضو التعداد الجوار/الحَيّ (NEIGHBORHOOD) بقيمة دقّة 6 واسم معروض "Neighborhood". [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:10]

```
11:     CITY(5, "City"),
```
> يعرّف عضو التعداد المدينة (CITY) بقيمة دقّة 5 واسم معروض "City". [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:11]

```
12:     PROVINCE(4, "Province"),
```
> يعرّف عضو التعداد المحافظة/الإقليم (PROVINCE) بقيمة دقّة 4 واسم معروض "Province". [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:12]

```
13:     REGION(2, "REGION");
```
> يعرّف عضو التعداد المنطقة (REGION) بقيمة دقّة 2 واسم معروض "REGION"، وينتهي بفاصلة منقوطة تُنهي قائمة أعضاء التعداد. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:13]

```
14:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:14]

```
15:     companion object {
```
> يفتح كائناً مرافقاً (companion object) داخل التعداد. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:15]

```
16:         fun allCases(): List<GeohashChannelLevel> = values().toList()
```
> يعرّف دالّة باسم كل الحالات (allCases) تُعيد قائمة List من GeohashChannelLevel، وقيمتها هي نتيجة استدعاء values() ثم تحويلها إلى قائمة بـ toList(). [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:16]

```
17:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:17]

```
18: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:18]

```
19: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:19]

```
20: /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:20]

```
21:  * A computed geohash channel option.
```
> تعليق: «خيار قناة جيوهاش محسوب». [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:21]

```
22:  * Direct port from iOS implementation
```
> تعليق: «نقل مباشر من تنفيذ iOS». [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:22]

```
23:  */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:23]

```
24: data class GeohashChannel(
```
> يعرّف صنف بيانات (data class) باسم قناة الجيوهاش (GeohashChannel)، ويفتح قائمة معاملات بانيه. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:24]

```
25:     val level: GeohashChannelLevel,
```
> يعرّف خاصيّة في الباني باسم المستوى (level) من نوع GeohashChannelLevel. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:25]

```
26:     val geohash: String
```
> يعرّف خاصيّة في الباني باسم الجيوهاش (geohash) من نوع نصّ String. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:26]

```
27: ) {
```
> يغلق قائمة معاملات الباني ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:27]

```
28:     val id: String get() = "${level.name}-$geohash"
```
> يعرّف خاصيّة نصّية باسم المعرّف (id) لها جالب (getter) يُعيد نصّاً مكوّناً من اسم المستوى level.name ثم شَرطة "-" ثم قيمة geohash. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:28]

```
29:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:29]

```
30:     val displayName: String get() = "${level.displayName} • $geohash"
```
> يعرّف خاصيّة نصّية باسم الاسم المعروض (displayName) لها جالب يُعيد نصّاً مكوّناً من level.displayName ثم مسافة ورمز "•" ومسافة ثم قيمة geohash. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:30]

```
31: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:31]

```
32: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:32]

```
33: /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:33]

```
34:  * Identifier for current public chat channel (mesh or a location geohash).
```
> تعليق: «معرّف لقناة الدردشة العامّة الحاليّة (شبكة mesh أو جيوهاش موقع)». [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:34]

```
35:  * Direct port from iOS implementation
```
> تعليق: «نقل مباشر من تنفيذ iOS». [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:35]

```
36:  */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:36]

```
37: sealed class ChannelID {
```
> يعرّف صنفاً مختوماً (sealed class) باسم معرّف القناة (ChannelID) ويفتح جسمه. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:37]

```
38:     object Mesh : ChannelID()
```
> يعرّف كائناً مفرداً (object) باسم الشبكة (Mesh) يرث من ChannelID. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:38]

```
39:     data class Location(val channel: GeohashChannel) : ChannelID() {
```
> يعرّف صنف بيانات باسم الموقع (Location) له خاصيّة في الباني باسم القناة (channel) من نوع GeohashChannel، ويرث من ChannelID، ويفتح جسمه. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:39]

```
40:         companion object {
```
> يفتح كائناً مرافقاً داخل صنف Location. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:40]

```
41:             fun fromPersisted(levelName: String, geohash: String): Location? {
```
> يعرّف دالّة باسم من المحفوظ (fromPersisted) تأخذ معاملاً نصّياً اسم المستوى (levelName) ومعاملاً نصّياً geohash، وتُعيد Location قابلاً لأن يكون فارغاً (Location?). [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:41]

```
42:                 return try {
```
> يبدأ إعادة قيمة عبر كتلة محاولة (try). [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:42]

```
43:                     val level = GeohashChannelLevel.valueOf(levelName)
```
> يعرّف متغيّراً ثابتاً باسم level قيمته نتيجة استدعاء GeohashChannelLevel.valueOf(levelName) الذي يحوّل النصّ levelName إلى عضو التعداد المطابق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:43]

```
44:                     Location(GeohashChannel(level, geohash))
```
> ينشئ ويُعيد كائن Location مبنيّاً من GeohashChannel المُنشأ بالقيمتين level وgeohash. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:44]

```
45:                 } catch (_: IllegalArgumentException) {
```
> يلتقط استثناء وسيط غير صالح (IllegalArgumentException) متجاهلاً اسمه بالرمز "_"، ويفتح كتلة الالتقاط. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:45]

```
46:                     null
```
> يُعيد القيمة الفارغة null كنتيجة لكتلة الالتقاط. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:46]

```
47:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:47]

```
48:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:48]

```
49:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:49]

```
50:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:50]

```
51:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:51]

```
52:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:52]

```
53:      * Human readable name for UI.
```
> تعليق: «اسم مقروء للبشر لواجهة المستخدم UI». [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:53]

```
54:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:54]

```
55:     val displayName: String
```
> يعرّف خاصيّة نصّية باسم الاسم المعروض (displayName) من نوع String. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:55]

```
56:         get() = when (this) {
```
> يبدأ جالب الخاصيّة الذي قيمته تعبير when يفحص this (الكائن الحالي). [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:56]

```
57:             is Mesh -> "Mesh"
```
> إذا كان الكائن من نوع Mesh فالنتيجة النصّ "Mesh". [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:57]

```
58:             is Location -> channel.displayName
```
> إذا كان الكائن من نوع Location فالنتيجة قيمة channel.displayName. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:58]

```
59:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:59]

```
60:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:60]

```
61:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:61]

```
62:      * Nostr tag value for scoping (geohash), if applicable.
```
> تعليق: «قيمة وسم Nostr للتحديد النطاقي (جيوهاش)، إن كانت قابلة للتطبيق». [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:62]

```
63:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:63]

```
64:     val nostrGeohashTag: String?
```
> يعرّف خاصيّة باسم وسم جيوهاش نوستر (nostrGeohashTag) من نوع نصّ قابل لأن يكون فارغاً (String?). [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:64]

```
65:         get() = when (this) {
```
> يبدأ جالب الخاصيّة الذي قيمته تعبير when يفحص this. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:65]

```
66:             is Mesh -> null
```
> إذا كان الكائن من نوع Mesh فالنتيجة null. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:66]

```
67:             is Location -> channel.geohash
```
> إذا كان الكائن من نوع Location فالنتيجة قيمة channel.geohash. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:67]

```
68:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:68]

```
69:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:69]

```
70:     override fun equals(other: Any?): Boolean {
```
> يعيد تعريف (override) الدالّة يساوي (equals) التي تأخذ معاملاً باسم other من نوع Any? وتُعيد قيمة منطقية Boolean. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:70]

```
71:         return when {
```
> يبدأ إعادة قيمة تعبير when بلا موضوع (يفحص شروطاً منطقية). [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:71]

```
72:             this is Mesh && other is Mesh -> true
```
> إذا كان this من نوع Mesh و other من نوع Mesh فالنتيجة true. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:72]

```
73:             this is Location && other is Location -> this.channel == other.channel
```
> إذا كان this من نوع Location و other من نوع Location فالنتيجة نتيجة مقارنة this.channel == other.channel. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:73]

```
74:             else -> false
```
> في غير ذلك من الحالات فالنتيجة false. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:74]

```
75:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:75]

```
76:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:76]

```
77:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:77]

```
78:     override fun hashCode(): Int {
```
> يعيد تعريف الدالّة رمز التجزئة (hashCode) التي تُعيد عدداً صحيحاً Int. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:78]

```
79:         return when (this) {
```
> يبدأ إعادة قيمة تعبير when يفحص this. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:79]

```
80:             is Mesh -> "mesh".hashCode()
```
> إذا كان الكائن من نوع Mesh فالنتيجة قيمة استدعاء "mesh".hashCode() أي رمز تجزئة النصّ "mesh". [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:80]

```
81:             is Location -> channel.hashCode()
```
> إذا كان الكائن من نوع Location فالنتيجة قيمة channel.hashCode() أي رمز تجزئة channel. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:81]

```
82:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:82]

```
83:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:83]

```
84: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannel.kt:84]
