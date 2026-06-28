# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يعلن انتماء الملف إلى الحزمة (package) ‏`com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:2]

```
3: import com.google.gson.*
```
> يستورد (import) كل العناصر العامة من حزمة ‏`com.google.gson`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:3]

```
4: import com.google.gson.annotations.SerializedName
```
> يستورد المُعرِّف ‏`SerializedName` من حزمة ‏`com.google.gson.annotations`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:4]

```
5: import java.lang.reflect.Type
```
> يستورد النوع ‏`Type` من حزمة ‏`java.lang.reflect`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:6]

```
7: /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:7]

```
8:  * Nostr event filter for subscriptions
```
> تعليق: مُرشّح أحداث Nostr للاشتراكات. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:8]

```
9:  * Compatible with iOS implementation
```
> تعليق: متوافق مع تطبيق iOS. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:9]

```
10:  */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:10]

```
11: data class NostrFilter(
```
> يعرّف صنف بيانات (data class) باسم ‏`NostrFilter` ويفتح قائمة معاملاته الأولية (constructor). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:11]

```
12:     val ids: List<String>? = null,
```
> يعرّف خاصية ثابتة (val) باسم ‏`ids` من نوع قائمة نصوص قابلة لأن تكون فارغة (nullable)، قيمتها الافتراضية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:12]

```
13:     val authors: List<String>? = null,
```
> يعرّف خاصية ثابتة باسم ‏`authors` (المؤلِّفون) من نوع قائمة نصوص قابلة للفراغ، قيمتها الافتراضية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:13]

```
14:     val kinds: List<Int>? = null,
```
> يعرّف خاصية ثابتة باسم ‏`kinds` (الأنواع) من نوع قائمة أعداد صحيحة قابلة للفراغ، قيمتها الافتراضية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:14]

```
15:     val since: Int? = null,
```
> يعرّف خاصية ثابتة باسم ‏`since` (منذ) من نوع عدد صحيح قابل للفراغ، قيمتها الافتراضية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:15]

```
16:     val until: Int? = null,
```
> يعرّف خاصية ثابتة باسم ‏`until` (حتى) من نوع عدد صحيح قابل للفراغ، قيمتها الافتراضية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:16]

```
17:     val limit: Int? = null,
```
> يعرّف خاصية ثابتة باسم ‏`limit` (الحد) من نوع عدد صحيح قابل للفراغ، قيمتها الافتراضية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:17]

```
18:     private val tagFilters: Map<String, List<String>>? = null
```
> يعرّف خاصية ثابتة خاصة (private) باسم ‏`tagFilters` (مُرشّحات الوسوم) من نوع خريطة من نص إلى قائمة نصوص قابلة للفراغ، قيمتها الافتراضية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:18]

```
19: ) {
```
> يغلق قائمة معاملات الباني ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:19]

```
20:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:20]

```
21:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:21]

```
22:         /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:22]

```
23:          * Create filter for NIP-17 gift wraps
```
> تعليق: أنشئ مُرشّحاً لأغلفة الهدايا (gift wraps) وفق NIP-17. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:23]

```
24:          */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:24]

```
25:         fun giftWrapsFor(pubkey: String, since: Long? = null): NostrFilter {
```
> يعرّف دالة (fun) باسم ‏`giftWrapsFor` تأخذ معامل نص ‏`pubkey` (المفتاح العام) ومعامل ‏`since` من نوع عدد طويل قابل للفراغ بقيمة افتراضية ‏`null`، وتعيد ‏`NostrFilter`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:25]

```
26:             return NostrFilter(
```
> يعيد كائن ‏`NostrFilter` جديداً ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:26]

```
27:                 kinds = listOf(NostrKind.GIFT_WRAP),
```
> يضبط ‏`kinds` على قائمة تحوي العنصر ‏`NostrKind.GIFT_WRAP`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:27]

```
28:                 since = since?.let { (it / 1000).toInt() },
```
> يضبط ‏`since` بحيث إذا كان المعامل ‏`since` غير فارغ يُقسَم على 1000 ويُحوَّل إلى عدد صحيح، وإلا يبقى ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:28]

```
29:                 tagFilters = mapOf("p" to listOf(pubkey)),
```
> يضبط ‏`tagFilters` على خريطة تربط المفتاح ‏`"p"` بقائمة تحوي ‏`pubkey`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:29]

```
30:                 limit = 100
```
> يضبط ‏`limit` على القيمة 100. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:30]

```
31:             )
```
> يغلق قائمة وسائط الباني. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:31]

```
32:         }
```
> إغلاق نطاق (إغلاق جسم الدالة ‏`giftWrapsFor`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:32]

```
33:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:33]

```
34:         /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:34]

```
35:          * Create filter for geohash-scoped ephemeral events (kind 20000 and 20001)
```
> تعليق: أنشئ مُرشّحاً للأحداث العابرة (ephemeral) المحصورة بنطاق geohash (النوعان 20000 و20001). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:35]

```
36:          */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:36]

```
37:         fun geohashEphemeral(geohash: String, since: Long? = null, limit: Int = 1000): NostrFilter {
```
> يعرّف دالة باسم ‏`geohashEphemeral` تأخذ معامل نص ‏`geohash`، ومعامل ‏`since` من نوع عدد طويل قابل للفراغ بقيمة افتراضية ‏`null`، ومعامل عدد صحيح ‏`limit` بقيمة افتراضية 1000، وتعيد ‏`NostrFilter`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:37]

```
38:             return NostrFilter(
```
> يعيد كائن ‏`NostrFilter` جديداً ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:38]

```
39:                 kinds = listOf(NostrKind.EPHEMERAL_EVENT, NostrKind.GEOHASH_PRESENCE),
```
> يضبط ‏`kinds` على قائمة تحوي العنصرين ‏`NostrKind.EPHEMERAL_EVENT` و‏`NostrKind.GEOHASH_PRESENCE`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:39]

```
40:                 since = since?.let { (it / 1000).toInt() },
```
> يضبط ‏`since` بحيث إذا كان المعامل ‏`since` غير فارغ يُقسَم على 1000 ويُحوَّل إلى عدد صحيح، وإلا يبقى ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:40]

```
41:                 tagFilters = mapOf("g" to listOf(geohash)),
```
> يضبط ‏`tagFilters` على خريطة تربط المفتاح ‏`"g"` بقائمة تحوي ‏`geohash`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:41]

```
42:                 limit = limit
```
> يضبط ‏`limit` على قيمة المعامل ‏`limit`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:42]

```
43:             )
```
> يغلق قائمة وسائط الباني. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:43]

```
44:         }
```
> إغلاق نطاق (إغلاق جسم الدالة ‏`geohashEphemeral`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:44]

```
45: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:45]

```
46:         /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:46]

```
47:          * Create filter for geohash-scoped chat messages only (kind 20000).
```
> تعليق: أنشئ مُرشّحاً لرسائل المحادثة المحصورة بنطاق geohash فقط (النوع 20000). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:47]

```
48:          * Low-volume; kept subscribed in the background so messages keep arriving.
```
> تعليق: حجمها منخفض؛ يبقى الاشتراك بها في الخلفية كي تستمر الرسائل في الوصول. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:48]

```
49:          */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:49]

```
50:         fun geohashMessages(geohash: String, since: Long? = null, limit: Int = 1000): NostrFilter {
```
> يعرّف دالة باسم ‏`geohashMessages` تأخذ معامل نص ‏`geohash`، ومعامل ‏`since` من نوع عدد طويل قابل للفراغ بقيمة افتراضية ‏`null`، ومعامل عدد صحيح ‏`limit` بقيمة افتراضية 1000، وتعيد ‏`NostrFilter`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:50]

```
51:             return NostrFilter(
```
> يعيد كائن ‏`NostrFilter` جديداً ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:51]

```
52:                 kinds = listOf(NostrKind.EPHEMERAL_EVENT),
```
> يضبط ‏`kinds` على قائمة تحوي العنصر ‏`NostrKind.EPHEMERAL_EVENT`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:52]

```
53:                 since = since?.let { (it / 1000).toInt() },
```
> يضبط ‏`since` بحيث إذا كان المعامل ‏`since` غير فارغ يُقسَم على 1000 ويُحوَّل إلى عدد صحيح، وإلا يبقى ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:53]

```
54:                 tagFilters = mapOf("g" to listOf(geohash)),
```
> يضبط ‏`tagFilters` على خريطة تربط المفتاح ‏`"g"` بقائمة تحوي ‏`geohash`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:54]

```
55:                 limit = limit
```
> يضبط ‏`limit` على قيمة المعامل ‏`limit`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:55]

```
56:             )
```
> يغلق قائمة وسائط الباني. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:56]

```
57:         }
```
> إغلاق نطاق (إغلاق جسم الدالة ‏`geohashMessages`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:57]

```
58: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:58]

```
59:         /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:59]

```
60:          * Create filter for geohash-scoped presence heartbeats only (kind 20001).
```
> تعليق: أنشئ مُرشّحاً لنبضات الحضور (presence heartbeats) المحصورة بنطاق geohash فقط (النوع 20001). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:60]

```
61:          * High-volume firehose (every participant rebroadcasts ~every 60s); only used
```
> تعليق: تدفق عالي الحجم (كل مشارك يعيد البث كل ٦٠ ثانية تقريباً)؛ يُستعمل فقط. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:61]

```
62:          * to refresh the participant list, so it is paused while backgrounded.
```
> تعليق: لتحديث قائمة المشاركين، لذا يُوقَف مؤقتاً أثناء العمل في الخلفية. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:62]

```
63:          */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:63]

```
64:         fun geohashPresence(geohash: String, since: Long? = null, limit: Int = 1000): NostrFilter {
```
> يعرّف دالة باسم ‏`geohashPresence` تأخذ معامل نص ‏`geohash`، ومعامل ‏`since` من نوع عدد طويل قابل للفراغ بقيمة افتراضية ‏`null`، ومعامل عدد صحيح ‏`limit` بقيمة افتراضية 1000، وتعيد ‏`NostrFilter`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:64]

```
65:             return NostrFilter(
```
> يعيد كائن ‏`NostrFilter` جديداً ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:65]

```
66:                 kinds = listOf(NostrKind.GEOHASH_PRESENCE),
```
> يضبط ‏`kinds` على قائمة تحوي العنصر ‏`NostrKind.GEOHASH_PRESENCE`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:66]

```
67:                 since = since?.let { (it / 1000).toInt() },
```
> يضبط ‏`since` بحيث إذا كان المعامل ‏`since` غير فارغ يُقسَم على 1000 ويُحوَّل إلى عدد صحيح، وإلا يبقى ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:67]

```
68:                 tagFilters = mapOf("g" to listOf(geohash)),
```
> يضبط ‏`tagFilters` على خريطة تربط المفتاح ‏`"g"` بقائمة تحوي ‏`geohash`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:68]

```
69:                 limit = limit
```
> يضبط ‏`limit` على قيمة المعامل ‏`limit`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:69]

```
70:             )
```
> يغلق قائمة وسائط الباني. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:70]

```
71:         }
```
> إغلاق نطاق (إغلاق جسم الدالة ‏`geohashPresence`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:71]

```
72:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:72]

```
73:         /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:73]

```
74:          * Create filter for text notes from specific authors
```
> تعليق: أنشئ مُرشّحاً للملاحظات النصية (text notes) من مؤلِّفين محدّدين. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:74]

```
75:          */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:75]

```
76:         fun textNotesFrom(authors: List<String>, since: Long? = null, limit: Int = 50): NostrFilter {
```
> يعرّف دالة باسم ‏`textNotesFrom` تأخذ معامل قائمة نصوص ‏`authors`، ومعامل ‏`since` من نوع عدد طويل قابل للفراغ بقيمة افتراضية ‏`null`، ومعامل عدد صحيح ‏`limit` بقيمة افتراضية 50، وتعيد ‏`NostrFilter`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:76]

```
77:             return NostrFilter(
```
> يعيد كائن ‏`NostrFilter` جديداً ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:77]

```
78:                 kinds = listOf(NostrKind.TEXT_NOTE),
```
> يضبط ‏`kinds` على قائمة تحوي العنصر ‏`NostrKind.TEXT_NOTE`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:78]

```
79:                 authors = authors,
```
> يضبط ‏`authors` على قيمة المعامل ‏`authors`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:79]

```
80:                 since = since?.let { (it / 1000).toInt() },
```
> يضبط ‏`since` بحيث إذا كان المعامل ‏`since` غير فارغ يُقسَم على 1000 ويُحوَّل إلى عدد صحيح، وإلا يبقى ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:80]

```
81:                 limit = limit
```
> يضبط ‏`limit` على قيمة المعامل ‏`limit`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:81]

```
82:             )
```
> يغلق قائمة وسائط الباني. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:82]

```
83:         }
```
> إغلاق نطاق (إغلاق جسم الدالة ‏`textNotesFrom`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:83]

```
84:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:84]

```
85:         /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:85]

```
86:          * Create filter for geohash-scoped text notes (kind=1 with g tag)
```
> تعليق: أنشئ مُرشّحاً للملاحظات النصية المحصورة بنطاق geohash (النوع=1 مع الوسم g). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:86]

```
87:          */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:87]

```
88:         fun geohashNotes(geohash: String, since: Long? = null, limit: Int = 200): NostrFilter {
```
> يعرّف دالة باسم ‏`geohashNotes` تأخذ معامل نص ‏`geohash`، ومعامل ‏`since` من نوع عدد طويل قابل للفراغ بقيمة افتراضية ‏`null`، ومعامل عدد صحيح ‏`limit` بقيمة افتراضية 200، وتعيد ‏`NostrFilter`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:88]

```
89:             return NostrFilter(
```
> يعيد كائن ‏`NostrFilter` جديداً ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:89]

```
90:                 kinds = listOf(NostrKind.TEXT_NOTE),
```
> يضبط ‏`kinds` على قائمة تحوي العنصر ‏`NostrKind.TEXT_NOTE`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:90]

```
91:                 since = since?.let { (it / 1000).toInt() },
```
> يضبط ‏`since` بحيث إذا كان المعامل ‏`since` غير فارغ يُقسَم على 1000 ويُحوَّل إلى عدد صحيح، وإلا يبقى ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:91]

```
92:                 tagFilters = mapOf("g" to listOf(geohash)),
```
> يضبط ‏`tagFilters` على خريطة تربط المفتاح ‏`"g"` بقائمة تحوي ‏`geohash`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:92]

```
93:                 limit = limit
```
> يضبط ‏`limit` على قيمة المعامل ‏`limit`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:93]

```
94:             )
```
> يغلق قائمة وسائط الباني. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:94]

```
95:         }
```
> إغلاق نطاق (إغلاق جسم الدالة ‏`geohashNotes`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:95]

```
96:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:96]

```
97:         /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:97]

```
98:          * Create filter for specific event IDs
```
> تعليق: أنشئ مُرشّحاً لمُعرّفات أحداث محدّدة. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:98]

```
99:          */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:99]

```
100:         fun forEvents(ids: List<String>): NostrFilter {
```
> يعرّف دالة باسم ‏`forEvents` تأخذ معامل قائمة نصوص ‏`ids` وتعيد ‏`NostrFilter`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:100]

```
101:             return NostrFilter(ids = ids)
```
> يعيد كائن ‏`NostrFilter` جديداً مع ضبط ‏`ids` على قيمة المعامل ‏`ids`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:101]

```
102:         }
```
> إغلاق نطاق (إغلاق جسم الدالة ‏`forEvents`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:102]

```
103:     }
```
> إغلاق نطاق (إغلاق الكائن المرافق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:103]

```
104:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:104]

```
105:     /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:105]

```
106:      * Custom JSON serializer to handle tag filters properly
```
> تعليق: مُسلسِل JSON مخصّص (serializer) للتعامل مع مُرشّحات الوسوم بشكل صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:106]

```
107:      */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:107]

```
108:     class FilterSerializer : JsonSerializer<NostrFilter> {
```
> يعرّف صنفاً باسم ‏`FilterSerializer` يُطبّق الواجهة ‏`JsonSerializer<NostrFilter>`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:108]

```
109:         override fun serialize(src: NostrFilter, typeOfSrc: Type, context: JsonSerializationContext): JsonElement {
```
> يتجاوز (override) دالة ‏`serialize` التي تأخذ مصدراً ‏`src` من نوع ‏`NostrFilter`، ونوعاً ‏`typeOfSrc` من نوع ‏`Type`، وسياقاً ‏`context` من نوع ‏`JsonSerializationContext`، وتعيد ‏`JsonElement`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:109]

```
110:             val jsonObject = JsonObject()
```
> يعرّف متغيراً ثابتاً ‏`jsonObject` ويسنده إلى كائن ‏`JsonObject` جديد. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:110]

```
111:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:111]

```
112:             // Standard fields
```
> تعليق: الحقول القياسية. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:112]

```
113:             src.ids?.let { jsonObject.add("ids", context.serialize(it)) }
```
> إذا كان ‏`src.ids` غير فارغ، يُضيف إلى ‏`jsonObject` خاصية باسم ‏`"ids"` قيمتها ناتج تسلسل ‏`it` عبر ‏`context`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:113]

```
114:             src.authors?.let { jsonObject.add("authors", context.serialize(it)) }
```
> إذا كان ‏`src.authors` غير فارغ، يُضيف إلى ‏`jsonObject` خاصية باسم ‏`"authors"` قيمتها ناتج تسلسل ‏`it` عبر ‏`context`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:114]

```
115:             src.kinds?.let { jsonObject.add("kinds", context.serialize(it)) }
```
> إذا كان ‏`src.kinds` غير فارغ، يُضيف إلى ‏`jsonObject` خاصية باسم ‏`"kinds"` قيمتها ناتج تسلسل ‏`it` عبر ‏`context`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:115]

```
116:             src.since?.let { jsonObject.addProperty("since", it) }
```
> إذا كان ‏`src.since` غير فارغ، يُضيف إلى ‏`jsonObject` خاصية باسم ‏`"since"` قيمتها ‏`it`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:116]

```
117:             src.until?.let { jsonObject.addProperty("until", it) }
```
> إذا كان ‏`src.until` غير فارغ، يُضيف إلى ‏`jsonObject` خاصية باسم ‏`"until"` قيمتها ‏`it`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:117]

```
118:             src.limit?.let { jsonObject.addProperty("limit", it) }
```
> إذا كان ‏`src.limit` غير فارغ، يُضيف إلى ‏`jsonObject` خاصية باسم ‏`"limit"` قيمتها ‏`it`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:118]

```
119:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:119]

```
120:             // Tag filters with # prefix
```
> تعليق: مُرشّحات الوسوم مع بادئة #. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:120]

```
121:             src.tagFilters?.forEach { (tag, values) ->
```
> إذا كان ‏`src.tagFilters` غير فارغ، يُكرّر على كل زوج (وسم ‏`tag`، قيم ‏`values`) فيه. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:121]

```
122:                 jsonObject.add("#$tag", context.serialize(values))
```
> يُضيف إلى ‏`jsonObject` خاصية اسمها ‏`"#"` متبوعاً بقيمة ‏`tag`، وقيمتها ناتج تسلسل ‏`values` عبر ‏`context`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:122]

```
123:             }
```
> إغلاق نطاق (إغلاق جسم حلقة ‏`forEach`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:123]

```
124:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:124]

```
125:             return jsonObject
```
> يعيد ‏`jsonObject`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:125]

```
126:         }
```
> إغلاق نطاق (إغلاق جسم الدالة ‏`serialize`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:126]

```
127:     }
```
> إغلاق نطاق (إغلاق الصنف ‏`FilterSerializer`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:127]

```
128:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:128]

```
129:     /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:129]

```
130:      * Create builder for complex filters
```
> تعليق: أنشئ بانياً (builder) للمُرشّحات المعقّدة. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:130]

```
131:      */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:131]

```
132:     class Builder {
```
> يعرّف صنفاً باسم ‏`Builder`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:132]

```
133:         private var ids: List<String>? = null
```
> يعرّف متغيراً خاصاً (private var) باسم ‏`ids` من نوع قائمة نصوص قابلة للفراغ، قيمته الابتدائية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:133]

```
134:         private var authors: List<String>? = null
```
> يعرّف متغيراً خاصاً باسم ‏`authors` من نوع قائمة نصوص قابلة للفراغ، قيمته الابتدائية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:134]

```
135:         private var kinds: List<Int>? = null
```
> يعرّف متغيراً خاصاً باسم ‏`kinds` من نوع قائمة أعداد صحيحة قابلة للفراغ، قيمته الابتدائية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:135]

```
136:         private var since: Int? = null
```
> يعرّف متغيراً خاصاً باسم ‏`since` من نوع عدد صحيح قابل للفراغ، قيمته الابتدائية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:136]

```
137:         private var until: Int? = null
```
> يعرّف متغيراً خاصاً باسم ‏`until` من نوع عدد صحيح قابل للفراغ، قيمته الابتدائية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:137]

```
138:         private var limit: Int? = null
```
> يعرّف متغيراً خاصاً باسم ‏`limit` من نوع عدد صحيح قابل للفراغ، قيمته الابتدائية ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:138]

```
139:         private val tagFilters = mutableMapOf<String, List<String>>()
```
> يعرّف متغيراً ثابتاً خاصاً باسم ‏`tagFilters` ويسنده إلى خريطة قابلة للتعديل (mutableMapOf) من نص إلى قائمة نصوص، فارغة ابتداءً. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:139]

```
140:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:140]

```
141:         fun ids(vararg ids: String) = apply { this.ids = ids.toList() }
```
> يعرّف دالة ‏`ids` تأخذ عدداً متغيراً (vararg) من النصوص، وتسند ‏`this.ids` إلى تحويل ‏`ids` إلى قائمة، وتعيد الكائن نفسه عبر ‏`apply`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:141]

```
142:         fun authors(vararg authors: String) = apply { this.authors = authors.toList() }
```
> يعرّف دالة ‏`authors` تأخذ عدداً متغيراً من النصوص، وتسند ‏`this.authors` إلى تحويل ‏`authors` إلى قائمة، وتعيد الكائن نفسه عبر ‏`apply`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:142]

```
143:         fun kinds(vararg kinds: Int) = apply { this.kinds = kinds.toList() }
```
> يعرّف دالة ‏`kinds` تأخذ عدداً متغيراً من الأعداد الصحيحة، وتسند ‏`this.kinds` إلى تحويل ‏`kinds` إلى قائمة، وتعيد الكائن نفسه عبر ‏`apply`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:143]

```
144:         fun since(timestamp: Long) = apply { this.since = (timestamp / 1000).toInt() }
```
> يعرّف دالة ‏`since` تأخذ ‏`timestamp` من نوع عدد طويل، وتسند ‏`this.since` إلى ‏`timestamp` مقسوماً على 1000 ومحوَّلاً إلى عدد صحيح، وتعيد الكائن نفسه عبر ‏`apply`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:144]

```
145:         fun until(timestamp: Long) = apply { this.until = (timestamp / 1000).toInt() }
```
> يعرّف دالة ‏`until` تأخذ ‏`timestamp` من نوع عدد طويل، وتسند ‏`this.until` إلى ‏`timestamp` مقسوماً على 1000 ومحوَّلاً إلى عدد صحيح، وتعيد الكائن نفسه عبر ‏`apply`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:145]

```
146:         fun limit(count: Int) = apply { this.limit = count }
```
> يعرّف دالة ‏`limit` تأخذ ‏`count` من نوع عدد صحيح، وتسند ‏`this.limit` إلى ‏`count`، وتعيد الكائن نفسه عبر ‏`apply`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:146]

```
147:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:147]

```
148:         fun tagP(vararg pubkeys: String) = apply { tagFilters["p"] = pubkeys.toList() }
```
> يعرّف دالة ‏`tagP` تأخذ عدداً متغيراً من النصوص ‏`pubkeys`، وتسند في ‏`tagFilters` عند المفتاح ‏`"p"` تحويل ‏`pubkeys` إلى قائمة، وتعيد الكائن نفسه عبر ‏`apply`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:148]

```
149:         fun tagE(vararg eventIds: String) = apply { tagFilters["e"] = eventIds.toList() }
```
> يعرّف دالة ‏`tagE` تأخذ عدداً متغيراً من النصوص ‏`eventIds`، وتسند في ‏`tagFilters` عند المفتاح ‏`"e"` تحويل ‏`eventIds` إلى قائمة، وتعيد الكائن نفسه عبر ‏`apply`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:149]

```
150:         fun tagG(vararg geohashes: String) = apply { tagFilters["g"] = geohashes.toList() }
```
> يعرّف دالة ‏`tagG` تأخذ عدداً متغيراً من النصوص ‏`geohashes`، وتسند في ‏`tagFilters` عند المفتاح ‏`"g"` تحويل ‏`geohashes` إلى قائمة، وتعيد الكائن نفسه عبر ‏`apply`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:150]

```
151:         fun tag(name: String, vararg values: String) = apply { tagFilters[name] = values.toList() }
```
> يعرّف دالة ‏`tag` تأخذ نصاً ‏`name` وعدداً متغيراً من النصوص ‏`values`، وتسند في ‏`tagFilters` عند المفتاح ‏`name` تحويل ‏`values` إلى قائمة، وتعيد الكائن نفسه عبر ‏`apply`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:151]

```
152:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:152]

```
153:         fun build(): NostrFilter {
```
> يعرّف دالة ‏`build` لا تأخذ معاملات وتعيد ‏`NostrFilter`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:153]

```
154:             return NostrFilter(
```
> يعيد كائن ‏`NostrFilter` جديداً ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:154]

```
155:                 ids = ids,
```
> يضبط ‏`ids` على قيمة الحقل ‏`ids`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:155]

```
156:                 authors = authors,
```
> يضبط ‏`authors` على قيمة الحقل ‏`authors`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:156]

```
157:                 kinds = kinds,
```
> يضبط ‏`kinds` على قيمة الحقل ‏`kinds`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:157]

```
158:                 since = since,
```
> يضبط ‏`since` على قيمة الحقل ‏`since`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:158]

```
159:                 until = until,
```
> يضبط ‏`until` على قيمة الحقل ‏`until`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:159]

```
160:                 limit = limit,
```
> يضبط ‏`limit` على قيمة الحقل ‏`limit`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:160]

```
161:                 tagFilters = tagFilters.toMap()
```
> يضبط ‏`tagFilters` على تحويل ‏`tagFilters` إلى خريطة غير قابلة للتعديل عبر ‏`toMap`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:161]

```
162:             )
```
> يغلق قائمة وسائط الباني. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:162]

```
163:         }
```
> إغلاق نطاق (إغلاق جسم الدالة ‏`build`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:163]

```
164:     }
```
> إغلاق نطاق (إغلاق الصنف ‏`Builder`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:164]

```
165:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:165]

```
166:     /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:166]

```
167:      * Check if this filter matches an event
```
> تعليق: تحقّق ممّا إذا كان هذا المُرشّح يطابق حدثاً. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:167]

```
168:      */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:168]

```
169:     fun matches(event: NostrEvent): Boolean {
```
> يعرّف دالة باسم ‏`matches` تأخذ معاملاً ‏`event` من نوع ‏`NostrEvent` وتعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:169]

```
170:         // Check IDs
```
> تعليق: تحقّق من المُعرّفات. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:170]

```
171:         if (ids != null && !ids.contains(event.id)) {
```
> إذا كان ‏`ids` غير فارغ ولا يحتوي على ‏`event.id`، يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:171]

```
172:             return false
```
> يعيد ‏`false`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:172]

```
173:         }
```
> إغلاق نطاق (إغلاق كتلة الشرط). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:173]

```
174:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:174]

```
175:         // Check authors
```
> تعليق: تحقّق من المؤلِّفين. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:175]

```
176:         if (authors != null && !authors.contains(event.pubkey)) {
```
> إذا كان ‏`authors` غير فارغ ولا يحتوي على ‏`event.pubkey`، يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:176]

```
177:             return false
```
> يعيد ‏`false`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:177]

```
178:         }
```
> إغلاق نطاق (إغلاق كتلة الشرط). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:178]

```
179:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:179]

```
180:         // Check kinds
```
> تعليق: تحقّق من الأنواع. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:180]

```
181:         if (kinds != null && !kinds.contains(event.kind)) {
```
> إذا كان ‏`kinds` غير فارغ ولا يحتوي على ‏`event.kind`، يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:181]

```
182:             return false
```
> يعيد ‏`false`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:182]

```
183:         }
```
> إغلاق نطاق (إغلاق كتلة الشرط). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:183]

```
184:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:184]

```
185:         // Check time bounds
```
> تعليق: تحقّق من حدود الزمن. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:185]

```
186:         if (since != null && event.createdAt < since) {
```
> إذا كان ‏`since` غير فارغ وكان ‏`event.createdAt` أصغر من ‏`since`، يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:186]

```
187:             return false
```
> يعيد ‏`false`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:187]

```
188:         }
```
> إغلاق نطاق (إغلاق كتلة الشرط). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:188]

```
189:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:189]

```
190:         if (until != null && event.createdAt > until) {
```
> إذا كان ‏`until` غير فارغ وكان ‏`event.createdAt` أكبر من ‏`until`، يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:190]

```
191:             return false
```
> يعيد ‏`false`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:191]

```
192:         }
```
> إغلاق نطاق (إغلاق كتلة الشرط). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:192]

```
193:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:193]

```
194:         // Check tag filters
```
> تعليق: تحقّق من مُرشّحات الوسوم. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:194]

```
195:         if (tagFilters != null) {
```
> إذا كان ‏`tagFilters` غير فارغ، يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:195]

```
196:             for ((tagName, requiredValues) in tagFilters) {
```
> يكرّر بحلقة ‏`for` على كل زوج (اسم الوسم ‏`tagName`، القيم المطلوبة ‏`requiredValues`) في ‏`tagFilters`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:196]

```
197:                 val eventTags = event.tags.filter { it.isNotEmpty() && it[0] == tagName }
```
> يعرّف متغيراً ثابتاً ‏`eventTags` ويسنده إلى تصفية ‏`event.tags` بالاحتفاظ بالعناصر غير الفارغة التي عنصرها الأول يساوي ‏`tagName`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:197]

```
198:                 val eventValues = eventTags.mapNotNull { tag ->
```
> يعرّف متغيراً ثابتاً ‏`eventValues` ويسنده إلى تطبيق ‏`mapNotNull` على ‏`eventTags` لكل عنصر ‏`tag`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:198]

```
199:                     if (tag.size > 1) tag[1] else null
```
> يعيد ‏`tag[1]` إذا كان حجم ‏`tag` أكبر من 1، وإلا يعيد ‏`null`. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:199]

```
200:                 }
```
> إغلاق نطاق (إغلاق جسم لامبدا ‏`mapNotNull`). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:200]
