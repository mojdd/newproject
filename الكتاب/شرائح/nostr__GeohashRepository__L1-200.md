# شريحة — app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يعرّف اسم الحزمة (package) للملف بأنه `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:2]

```
3: import android.app.Application
```
> يستورد الصنف `Application` من حزمة `android.app`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` (السجل) من حزمة `android.util`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:4]

```
5: import com.bitchat.android.ui.ChatState
```
> يستورد الصنف `ChatState` (حالة المحادثة) من حزمة `com.bitchat.android.ui`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:5]

```
6: import com.bitchat.android.ui.GeoPerson
```
> يستورد الصنف `GeoPerson` (شخص الموقع الجغرافي) من حزمة `com.bitchat.android.ui`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:6]

```
7: import java.util.Date
```
> يستورد الصنف `Date` (التاريخ) من حزمة `java.util`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:8]

```
9: /**
```
> تعليق: بداية تعليق توثيقي (Javadoc/KDoc). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:9]

```
10:  * GeohashRepository
```
> تعليق: «GeohashRepository» (مستودع الموقع الجغرافي). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:10]

```
11:  * - Owns geohash participant tracking and nickname caching
```
> تعليق: «- يملك تتبّع مشاركي الموقع الجغرافي وتخزين الأسماء المستعارة مؤقتاً». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:11]

```
12:  * - Maintains lightweight state for geohash-related UI
```
> تعليق: «- يحافظ على حالة خفيفة لواجهة المستخدم المتعلقة بالموقع الجغرافي». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:12]

```
13:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:13]

```
14: class GeohashRepository(
```
> يعرّف الصنف `GeohashRepository` (مستودع الموقع الجغرافي) ويفتح قائمة معاملات منشئه. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:14]

```
15:     private val application: Application,
```
> يعرّف معامل منشئ خاصاً للقراءة فقط باسم `application` من النوع `Application`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:15]

```
16:     private val state: ChatState,
```
> يعرّف معامل منشئ خاصاً للقراءة فقط باسم `state` (الحالة) من النوع `ChatState`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:16]

```
17:     private val dataManager: com.bitchat.android.ui.DataManager
```
> يعرّف معامل منشئ خاصاً للقراءة فقط باسم `dataManager` (مدير البيانات) من النوع `com.bitchat.android.ui.DataManager`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:17]

```
18: ) {
```
> يغلق قائمة معاملات المنشئ ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:18]

```
19:     companion object { private const val TAG = "GeohashRepository" }
```
> يعرّف كائناً مرافقاً (companion object) يحتوي ثابتاً خاصاً باسم `TAG` (الوسم) قيمته السلسلة `"GeohashRepository"`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:19]

```
20: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:20]

```
21:     // geohash -> (participant pubkeyHex -> lastSeen)
```
> تعليق: «geohash -> (participant pubkeyHex -> lastSeen)» أي الموقع الجغرافي يقابل (المفتاح العام السداسي للمشارك يقابل آخر ظهور). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:21]

```
22:     private val geohashParticipants: MutableMap<String, MutableMap<String, Date>> = mutableMapOf()
```
> يعرّف حقلاً خاصاً للقراءة فقط باسم `geohashParticipants` (مشاركو الموقع الجغرافي) من النوع خريطة قابلة للتغيير من سلسلة إلى خريطة قابلة للتغيير من سلسلة إلى `Date`، ويهيّئه بخريطة فارغة قابلة للتغيير. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:22]

```
23: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:24]

```
25:     // pubkeyHex(lowercase) -> nickname (without #hash)
```
> تعليق: «pubkeyHex(lowercase) -> nickname (without #hash)» أي المفتاح العام السداسي بحروف صغيرة يقابل الاسم المستعار (بدون لاحقة #hash). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:25]

```
26:     private val geoNicknames: MutableMap<String, String> = mutableMapOf()
```
> يعرّف حقلاً خاصاً للقراءة فقط باسم `geoNicknames` (الأسماء المستعارة الجغرافية) من النوع خريطة قابلة للتغيير من سلسلة إلى سلسلة، ويهيّئه بخريطة فارغة قابلة للتغيير. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:27]

```
28:     // conversation key (e.g., "nostr_<pub16>") -> source geohash it belongs to
```
> تعليق: «conversation key (e.g., "nostr_<pub16>") -> source geohash it belongs to» أي مفتاح المحادثة (مثلاً "nostr_<pub16>") يقابل الموقع الجغرافي المصدر الذي ينتمي إليه. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:28]

```
29:     private val conversationGeohash: MutableMap<String, String> = mutableMapOf()
```
> يعرّف حقلاً خاصاً للقراءة فقط باسم `conversationGeohash` (موقع المحادثة الجغرافي) من النوع خريطة قابلة للتغيير من سلسلة إلى سلسلة، ويهيّئه بخريطة فارغة قابلة للتغيير. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:29]

```
30: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:30]

```
31:     fun setConversationGeohash(convKey: String, geohash: String) {
```
> يعرّف الدالة `setConversationGeohash` (تعيين موقع المحادثة الجغرافي) التي تأخذ معاملين سلسلة `convKey` و `geohash`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:31]

```
32:         if (geohash.isNotEmpty()) {
```
> يفحص ما إذا كان `geohash` غير فارغ (isNotEmpty)، ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:32]

```
33:             conversationGeohash[convKey] = geohash
```
> يسند القيمة `geohash` إلى الخريطة `conversationGeohash` عند المفتاح `convKey`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:33]

```
34:         }
```
> إغلاق نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:34]

```
35:     }
```
> إغلاق نطاق الدالة `setConversationGeohash`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:36]

```
37:     fun getConversationGeohash(convKey: String): String? = conversationGeohash[convKey]
```
> يعرّف الدالة `getConversationGeohash` (جلب موقع المحادثة الجغرافي) التي تأخذ معاملاً سلسلة `convKey` وتعيد سلسلة قابلة للعدم تساوي قيمة الخريطة `conversationGeohash` عند المفتاح `convKey`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:37]

```
38: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:38]

```
39:     fun findPubkeyByNickname(targetNickname: String): String? {
```
> يعرّف الدالة `findPubkeyByNickname` (إيجاد المفتاح العام بالاسم المستعار) التي تأخذ معاملاً سلسلة `targetNickname` وتعيد سلسلة قابلة للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:39]

```
40:         return geoNicknames.entries.firstOrNull { (_, nickname) ->
```
> يعيد نتيجة استدعاء `firstOrNull` على مدخلات الخريطة `geoNicknames` مع دالة لامبدا تفكّك المدخل وتتجاهل المفتاح وتسمي القيمة `nickname`، ويفتح جسم اللامبدا. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:40]

```
41:             val base = nickname.split("#").firstOrNull() ?: nickname
```
> يعرّف متغيراً للقراءة فقط باسم `base` (الأساس) يساوي أول عنصر من تقسيم `nickname` على الرمز "#"، أو `nickname` نفسه إن كان الأول عدماً. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:41]

```
42:             base == targetNickname
```
> يقيّم تساوي `base` مع `targetNickname` كقيمة إرجاع للامبدا. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:42]

```
43:         }?.key
```
> يغلق اللامبدا، ويصل بأمان (?.) إلى الخاصية `key` (المفتاح) من المدخل الناتج. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:43]

```
44:     }
```
> إغلاق نطاق الدالة `findPubkeyByNickname`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:44]

```
45: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:45]

```
46:     fun findPubkeyByShortId(shortId: String): String? {
```
> يعرّف الدالة `findPubkeyByShortId` (إيجاد المفتاح العام بالمعرّف القصير) التي تأخذ معاملاً سلسلة `shortId` وتعيد سلسلة قابلة للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:46]

```
47:         // First check cached nicknames (fastest)
```
> تعليق: «أولاً افحص الأسماء المستعارة المخزّنة مؤقتاً (الأسرع)». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:47]

```
48:         var found = geoNicknames.keys.firstOrNull { it.startsWith(shortId, ignoreCase = true) }
```
> يعرّف متغيراً قابلاً للتغيير باسم `found` (الموجود) يساوي أول مفتاح من مفاتيح `geoNicknames` يبدأ بـ `shortId` مع تجاهل حالة الأحرف (ignoreCase = true). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:48]

```
49:         if (found != null) return found
```
> إذا كان `found` غير عدم فإنه يعيد `found`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:49]

```
50: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:50]

```
51:         // If not found in nicknames (e.g. anon user), check all known participants across all geohashes
```
> تعليق: «إن لم يُوجد في الأسماء المستعارة (مثلاً مستخدم مجهول)، افحص كل المشاركين المعروفين عبر كل المواقع الجغرافية». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:51]

```
52:         for (participants in geohashParticipants.values) {
```
> يبدأ حلقة `for` تكرّر على قيم الخريطة `geohashParticipants` وتسمي كل قيمة `participants`، ويفتح جسم الحلقة. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:52]

```
53:             found = participants.keys.firstOrNull { it.startsWith(shortId, ignoreCase = true) }
```
> يسند إلى `found` أول مفتاح من مفاتيح `participants` يبدأ بـ `shortId` مع تجاهل حالة الأحرف. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:53]

```
54:             if (found != null) return found
```
> إذا كان `found` غير عدم فإنه يعيد `found`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:54]

```
55:         }
```
> إغلاق نطاق حلقة `for`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:55]

```
56:         
```
> سطر فارغ (يحوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:56]

```
57:         return null
```
> يعيد `null` (عدم). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:57]

```
58:     }
```
> إغلاق نطاق الدالة `findPubkeyByShortId`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:58]

```
59: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:59]

```
60:     // peerID alias -> nostr pubkey mapping for geohash DMs and temp aliases
```
> تعليق: «peerID alias -> nostr pubkey mapping for geohash DMs and temp aliases» أي تعيين الاسم البديل لمعرّف النظير إلى مفتاح nostr العام للرسائل المباشرة الجغرافية والأسماء البديلة المؤقتة. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:60]

```
61:     private val nostrKeyMapping: MutableMap<String, String> = mutableMapOf()
```
> يعرّف حقلاً خاصاً للقراءة فقط باسم `nostrKeyMapping` (تعيين مفاتيح nostr) من النوع خريطة قابلة للتغيير من سلسلة إلى سلسلة، ويهيّئه بخريطة فارغة قابلة للتغيير. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:61]

```
62: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:62]

```
63:     // Current geohash in view
```
> تعليق: «الموقع الجغرافي الحالي في العرض». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:63]

```
64:     private var currentGeohash: String? = null
```
> يعرّف حقلاً خاصاً قابلاً للتغيير باسم `currentGeohash` (الموقع الجغرافي الحالي) من النوع سلسلة قابلة للعدم، ويهيّئه بـ `null`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:65]

```
66:     fun setCurrentGeohash(geo: String?) { currentGeohash = geo }
```
> يعرّف الدالة `setCurrentGeohash` (تعيين الموقع الجغرافي الحالي) التي تأخذ معاملاً سلسلة قابلاً للعدم `geo` وتسند قيمته إلى الحقل `currentGeohash`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:66]

```
67:     fun getCurrentGeohash(): String? = currentGeohash
```
> يعرّف الدالة `getCurrentGeohash` (جلب الموقع الجغرافي الحالي) التي تعيد سلسلة قابلة للعدم تساوي الحقل `currentGeohash`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:67]

```
68: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:68]

```
69:     fun clearAll() {
```
> يعرّف الدالة `clearAll` (مسح الكل) بلا معاملات، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:69]

```
70:         geohashParticipants.clear()
```
> يستدعي `clear` على الخريطة `geohashParticipants` لتفريغها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:70]

```
71:         geoNicknames.clear()
```
> يستدعي `clear` على الخريطة `geoNicknames` لتفريغها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:71]

```
72:         nostrKeyMapping.clear()
```
> يستدعي `clear` على الخريطة `nostrKeyMapping` لتفريغها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:72]

```
73:         state.setGeohashPeople(emptyList())
```
> يستدعي `setGeohashPeople` على `state` ممرّراً قائمة فارغة (emptyList). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:73]

```
74:         state.setTeleportedGeo(emptySet())
```
> يستدعي `setTeleportedGeo` على `state` ممرّراً مجموعة فارغة (emptySet). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:74]

```
75:         state.setGeohashParticipantCounts(emptyMap())
```
> يستدعي `setGeohashParticipantCounts` على `state` ممرّراً خريطة فارغة (emptyMap). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:75]

```
76:         currentGeohash = null
```
> يسند `null` إلى الحقل `currentGeohash`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:76]

```
77:     }
```
> إغلاق نطاق الدالة `clearAll`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:77]

```
78: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:78]

```
79:     fun cacheNickname(pubkeyHex: String, nickname: String) {
```
> يعرّف الدالة `cacheNickname` (تخزين الاسم المستعار مؤقتاً) التي تأخذ معاملين سلسلة `pubkeyHex` و `nickname`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:79]

```
80:         val lower = pubkeyHex.lowercase()
```
> يعرّف متغيراً للقراءة فقط باسم `lower` (الصغير) يساوي `pubkeyHex` محوّلاً إلى حروف صغيرة (lowercase). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:80]

```
81:         val previous = geoNicknames[lower]
```
> يعرّف متغيراً للقراءة فقط باسم `previous` (السابق) يساوي قيمة الخريطة `geoNicknames` عند المفتاح `lower`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:81]

```
82:         geoNicknames[lower] = nickname
```
> يسند القيمة `nickname` إلى الخريطة `geoNicknames` عند المفتاح `lower`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:82]

```
83:         if (previous != nickname && currentGeohash != null) {
```
> يفحص ما إذا كان `previous` لا يساوي `nickname` و `currentGeohash` غير عدم، ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:83]

```
84:             refreshGeohashPeople()
```
> يستدعي الدالة `refreshGeohashPeople` (تحديث أشخاص الموقع الجغرافي). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:84]

```
85:         }
```
> إغلاق نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:85]

```
86:     }
```
> إغلاق نطاق الدالة `cacheNickname`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:86]

```
87: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:87]

```
88:     fun getCachedNickname(pubkeyHex: String): String? = geoNicknames[pubkeyHex.lowercase()]
```
> يعرّف الدالة `getCachedNickname` (جلب الاسم المستعار المخزّن) التي تأخذ معاملاً سلسلة `pubkeyHex` وتعيد سلسلة قابلة للعدم تساوي قيمة الخريطة `geoNicknames` عند مفتاح `pubkeyHex` بحروف صغيرة. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:88]

```
89: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:89]

```
90:     fun markTeleported(pubkeyHex: String) {
```
> يعرّف الدالة `markTeleported` (وسم بأنه منتقل آنياً) التي تأخذ معاملاً سلسلة `pubkeyHex`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:90]

```
91:         val set = state.getTeleportedGeoValue().toMutableSet()
```
> يعرّف متغيراً للقراءة فقط باسم `set` (المجموعة) يساوي ناتج `getTeleportedGeoValue` من `state` محوّلاً إلى مجموعة قابلة للتغيير (toMutableSet). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:91]

```
92:         val key = pubkeyHex.lowercase()
```
> يعرّف متغيراً للقراءة فقط باسم `key` (المفتاح) يساوي `pubkeyHex` بحروف صغيرة. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:92]

```
93:         if (!set.contains(key)) {
```
> يفحص ما إذا كانت المجموعة `set` لا تحتوي `key`، ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:93]

```
94:             set.add(key)
```
> يضيف `key` إلى المجموعة `set`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:94]

```
95:             // Background safe update
```
> تعليق: «تحديث آمن في الخلفية». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:95]

```
96:             state.postTeleportedGeo(set)
```
> يستدعي `postTeleportedGeo` على `state` ممرّراً المجموعة `set`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:96]

```
97:         }
```
> إغلاق نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:97]

```
98:     }
```
> إغلاق نطاق الدالة `markTeleported`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:98]

```
99: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:99]

```
100:     fun isPersonTeleported(pubkeyHex: String): Boolean {
```
> يعرّف الدالة `isPersonTeleported` (هل الشخص منتقل آنياً) التي تأخذ معاملاً سلسلة `pubkeyHex` وتعيد قيمة منطقية، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:100]

```
101:         return state.getTeleportedGeoValue().contains(pubkeyHex.lowercase())
```
> يعيد نتيجة فحص ما إذا كان ناتج `getTeleportedGeoValue` من `state` يحتوي `pubkeyHex` بحروف صغيرة. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:101]

```
102:     }
```
> إغلاق نطاق الدالة `isPersonTeleported`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:102]

```
103: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:103]

```
104:     fun updateParticipant(geohash: String, participantId: String, lastSeen: Date) {
```
> يعرّف الدالة `updateParticipant` (تحديث مشارك) التي تأخذ معاملين سلسلة `geohash` و `participantId` ومعاملاً `lastSeen` من النوع `Date`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:104]

```
105:         val participants = geohashParticipants.getOrPut(geohash) { mutableMapOf() }
```
> يعرّف متغيراً للقراءة فقط باسم `participants` (المشاركون) يساوي ناتج `getOrPut` على `geohashParticipants` بالمفتاح `geohash`، ويهيّئ بخريطة فارغة قابلة للتغيير إن لم يوجد. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:105]

```
106:         // Cap to now: prevents future-timestamped events (clock skew / malicious created_at)
```
> تعليق: «حدّ بالوقت الحالي: يمنع الأحداث ذات الطابع الزمني المستقبلي (انحراف الساعة / created_at خبيث)». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:106]

```
107:         // from pinning lastSeen and blocking subsequent normal heartbeats.
```
> تعليق: «من تثبيت lastSeen ومنع نبضات القلب العادية اللاحقة». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:107]

```
108:         // Also keeps max: relays send events newest-first, so subsequent older events for
```
> تعليق: «كما يبقي الأقصى: المرحّلات (relays) ترسل الأحداث الأحدث أولاً، فالأحداث الأقدم اللاحقة لـ». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:108]

```
109:         // the same user must not overwrite a fresher lastSeen.
```
> تعليق: «المستخدم نفسه يجب ألا تكتب فوق lastSeen أحدث». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:109]

```
110:         val now = Date()
```
> يعرّف متغيراً للقراءة فقط باسم `now` (الآن) يساوي كائن `Date` جديداً (الوقت الحالي). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:110]

```
111:         val effective = if (lastSeen.after(now)) now else lastSeen
```
> يعرّف متغيراً للقراءة فقط باسم `effective` (الفعّال) يساوي `now` إن كان `lastSeen` بعد `now`، وإلا يساوي `lastSeen`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:111]

```
112:         val existing = participants[participantId]
```
> يعرّف متغيراً للقراءة فقط باسم `existing` (الموجود) يساوي قيمة الخريطة `participants` عند المفتاح `participantId`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:112]

```
113:         if (existing == null || effective.after(existing)) {
```
> يفحص ما إذا كان `existing` عدماً أو كان `effective` بعد `existing`، ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:113]

```
114:             participants[participantId] = effective
```
> يسند القيمة `effective` إلى الخريطة `participants` عند المفتاح `participantId`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:114]

```
115:         }
```
> إغلاق نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:115]

```
116:         if (currentGeohash == geohash) refreshGeohashPeople()
```
> يفحص ما إذا كان `currentGeohash` يساوي `geohash`، وإن صحّ يستدعي `refreshGeohashPeople`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:116]

```
117:         updateReactiveParticipantCounts()
```
> يستدعي الدالة `updateReactiveParticipantCounts` (تحديث أعداد المشاركين التفاعلية). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:117]

```
118:     }
```
> إغلاق نطاق الدالة `updateParticipant`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:118]

```
119: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:119]

```
120:     fun geohashParticipantCount(geohash: String): Int {
```
> يعرّف الدالة `geohashParticipantCount` (عدد مشاركي الموقع الجغرافي) التي تأخذ معاملاً سلسلة `geohash` وتعيد عدداً صحيحاً (Int)، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:120]

```
121:         val cutoff = Date(System.currentTimeMillis() - 5 * 60 * 1000)
```
> يعرّف متغيراً للقراءة فقط باسم `cutoff` (الحدّ القاطع) يساوي كائن `Date` من الوقت الحالي بالمللي ثانية مطروحاً منه 5×60×1000 (خمس دقائق). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:121]

```
122:         val participants = geohashParticipants[geohash] ?: return 0
```
> يعرّف متغيراً للقراءة فقط باسم `participants` يساوي قيمة `geohashParticipants` عند المفتاح `geohash`، وإن كانت عدماً يعيد الدالة القيمة 0. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:122]

```
123:         // prune expired
```
> تعليق: «قُصّ المنتهي». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:123]

```
124:         val it = participants.iterator()
```
> يعرّف متغيراً للقراءة فقط باسم `it` (المكرّر) يساوي مكرّر (iterator) الخريطة `participants`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:124]

```
125:         while (it.hasNext()) {
```
> يبدأ حلقة `while` تستمر ما دام للمكرّر `it` عنصر تالٍ (hasNext)، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:125]

```
126:             val e = it.next()
```
> يعرّف متغيراً للقراءة فقط باسم `e` (المدخل) يساوي العنصر التالي من المكرّر `it`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:126]

```
127:             if (e.value.before(cutoff)) it.remove()
```
> يفحص ما إذا كانت قيمة المدخل `e` (التاريخ) قبل `cutoff`، وإن صحّ يحذف العنصر عبر `it.remove`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:127]

```
128:         }
```
> إغلاق نطاق حلقة `while`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:128]

```
129:         // exclude blocked users
```
> تعليق: «استبعد المستخدمين المحظورين». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:129]

```
130:         return participants.keys.count { !dataManager.isGeohashUserBlocked(it) }
```
> يعيد عدد مفاتيح `participants` التي يكون لها `isGeohashUserBlocked` من `dataManager` بقيمة كاذبة (أي غير محظورة). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:130]

```
131:     }
```
> إغلاق نطاق الدالة `geohashParticipantCount`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:131]

```
132: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:132]

```
133:     fun refreshGeohashPeople() {
```
> يعرّف الدالة `refreshGeohashPeople` (تحديث أشخاص الموقع الجغرافي) بلا معاملات، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:133]

```
134:         val geohash = currentGeohash
```
> يعرّف متغيراً للقراءة فقط باسم `geohash` يساوي قيمة الحقل `currentGeohash`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:134]

```
135:         if (geohash == null) {
```
> يفحص ما إذا كان `geohash` عدماً، ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:135]

```
136:             // Use postValue for thread safety - this can be called from background threads
```
> تعليق: «استعمل postValue لأمان الخيوط - يمكن استدعاء هذا من خيوط الخلفية». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:136]

```
137:             state.setGeohashPeople(emptyList())
```
> يستدعي `setGeohashPeople` على `state` ممرّراً قائمة فارغة. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:137]

```
138:             return
```
> يعيد من الدالة (إرجاع بلا قيمة). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:138]

```
139:         }
```
> إغلاق نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:139]

```
140:         val cutoff = Date(System.currentTimeMillis() - 5 * 60 * 1000)
```
> يعرّف متغيراً للقراءة فقط باسم `cutoff` يساوي كائن `Date` من الوقت الحالي بالمللي ثانية مطروحاً منه 5×60×1000 (خمس دقائق). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:140]

```
141:         val participants = geohashParticipants[geohash] ?: mutableMapOf()
```
> يعرّف متغيراً للقراءة فقط باسم `participants` يساوي قيمة `geohashParticipants` عند المفتاح `geohash`، أو خريطة فارغة قابلة للتغيير إن كانت عدماً. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:141]

```
142:         // prune expired
```
> تعليق: «قُصّ المنتهي». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:142]

```
143:         val it = participants.iterator()
```
> يعرّف متغيراً للقراءة فقط باسم `it` يساوي مكرّر الخريطة `participants`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:143]

```
144:         while (it.hasNext()) {
```
> يبدأ حلقة `while` تستمر ما دام للمكرّر `it` عنصر تالٍ، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:144]

```
145:             val e = it.next()
```
> يعرّف متغيراً للقراءة فقط باسم `e` يساوي العنصر التالي من المكرّر `it`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:145]

```
146:             if (e.value.before(cutoff)) it.remove()
```
> يفحص ما إذا كانت قيمة المدخل `e` قبل `cutoff`، وإن صحّ يحذف العنصر عبر `it.remove`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:146]

```
147:         }
```
> إغلاق نطاق حلقة `while`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:147]

```
148:         geohashParticipants[geohash] = participants
```
> يسند `participants` إلى الخريطة `geohashParticipants` عند المفتاح `geohash`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:148]

```
149:         // exclude blocked users from people list
```
> تعليق: «استبعد المستخدمين المحظورين من قائمة الأشخاص». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:149]

```
150:         val people = participants.filterKeys { !dataManager.isGeohashUserBlocked(it) }
```
> يعرّف متغيراً للقراءة فقط باسم `people` (الأشخاص) يبدأ بترشيح مفاتيح `participants` (filterKeys) لإبقاء غير المحظورين عبر نفي `isGeohashUserBlocked` من `dataManager`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:150]

```
151:             .map { (pubkeyHex, lastSeen) ->
```
> يحوّل (map) كل مدخل مفكَّكاً إلى `pubkeyHex` و `lastSeen`، ويفتح جسم اللامبدا. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:151]

```
152:             // Use our actual nickname for self; otherwise use cached nickname or anon
```
> تعليق: «استعمل اسمنا المستعار الفعلي للذات؛ وإلا استعمل الاسم المخزّن أو مجهول». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:152]

```
153:             val base = try {
```
> يعرّف متغيراً للقراءة فقط باسم `base` يساوي نتيجة كتلة `try`، ويفتح كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:153]

```
154:                 val myHex = currentGeohash?.let { NostrIdentityBridge.deriveIdentity(it, application).publicKeyHex }
```
> يعرّف متغيراً للقراءة فقط باسم `myHex` يساوي — إن كان `currentGeohash` غير عدم — `publicKeyHex` الناتج من `NostrIdentityBridge.deriveIdentity` ممرّراً الموقع الجغرافي و `application`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:154]

```
155:                 if (myHex != null && myHex.equals(pubkeyHex, true)) {
```
> يفحص ما إذا كان `myHex` غير عدم ويساوي `pubkeyHex` مع تجاهل حالة الأحرف (true)، ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:155]

```
156:                     state.getNicknameValue() ?: "anon"
```
> يقيّم ناتج `getNicknameValue` من `state`، أو السلسلة `"anon"` (مجهول) إن كان عدماً، كقيمة لكتلة `try`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:156]

```
157:                 } else {
```
> يغلق كتلة الشرط ويفتح كتلة `else`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:157]

```
158:                     getCachedNickname(pubkeyHex) ?: "anon"
```
> يقيّم ناتج `getCachedNickname` بـ `pubkeyHex`، أو السلسلة `"anon"` إن كان عدماً، كقيمة لكتلة `else`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:158]

```
159:                 }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:159]

```
160:             } catch (_: Exception) { getCachedNickname(pubkeyHex) ?: "anon" }
```
> يلتقط أي استثناء (Exception) بلا تسمية ويعيد ناتج `getCachedNickname` بـ `pubkeyHex`، أو `"anon"` إن كان عدماً. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:160]

```
161:             GeoPerson(
```
> يبني كائن `GeoPerson` (شخص جغرافي) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:161]

```
162:                 id = pubkeyHex.lowercase(),
```
> يمرّر الوسيطة المسمّاة `id` بقيمة `pubkeyHex` بحروف صغيرة. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:162]

```
163:                 displayName = base, // UI can add #hash if necessary
```
> يمرّر الوسيطة المسمّاة `displayName` (اسم العرض) بقيمة `base`؛ تعليق: «واجهة المستخدم يمكن أن تضيف #hash عند الحاجة». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:163]

```
164:                 lastSeen = lastSeen
```
> يمرّر الوسيطة المسمّاة `lastSeen` بقيمة `lastSeen`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:164]

```
165:             )
```
> يغلق قائمة وسائط بناء `GeoPerson`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:165]

```
166:         }.sortedByDescending { it.lastSeen }
```
> يغلق لامبدا التحويل ثم يرتّب النتائج تنازلياً (sortedByDescending) حسب `lastSeen`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:166]

```
167:         // Use postValue for thread safety - this can be called from background threads
```
> تعليق: «استعمل postValue لأمان الخيوط - يمكن استدعاء هذا من خيوط الخلفية». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:167]

```
168:         state.setGeohashPeople(people)
```
> يستدعي `setGeohashPeople` على `state` ممرّراً القائمة `people`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:168]

```
169:     }
```
> إغلاق نطاق الدالة `refreshGeohashPeople`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:169]

```
170: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:170]

```
171:     fun updateReactiveParticipantCounts() {
```
> يعرّف الدالة `updateReactiveParticipantCounts` (تحديث أعداد المشاركين التفاعلية) بلا معاملات، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:171]

```
172:         val cutoff = Date(System.currentTimeMillis() - 5 * 60 * 1000)
```
> يعرّف متغيراً للقراءة فقط باسم `cutoff` يساوي كائن `Date` من الوقت الحالي بالمللي ثانية مطروحاً منه 5×60×1000 (خمس دقائق). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:172]

```
173:         val counts = mutableMapOf<String, Int>()
```
> يعرّف متغيراً للقراءة فقط باسم `counts` (الأعداد) يساوي خريطة فارغة قابلة للتغيير من سلسلة إلى عدد صحيح. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:173]

```
174:         for ((gh, participants) in geohashParticipants) {
```
> يبدأ حلقة `for` تكرّر على مدخلات `geohashParticipants` مفكِّكة كل مدخل إلى `gh` و `participants`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:174]

```
175:             val active = participants.filterKeys { !dataManager.isGeohashUserBlocked(it) }
```
> يعرّف متغيراً للقراءة فقط باسم `active` (النشطون) يبدأ بترشيح مفاتيح `participants` لإبقاء غير المحظورين عبر نفي `isGeohashUserBlocked` من `dataManager`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:175]

```
176:                 .values.count { !it.before(cutoff) }
```
> يأخذ قيم الخريطة المرشّحة ويعدّ (count) منها ما ليس قبل `cutoff` (أي التواريخ غير المنتهية). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:176]

```
177:             counts[gh] = active
```
> يسند العدد `active` إلى الخريطة `counts` عند المفتاح `gh`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:177]

```
178:         }
```
> إغلاق نطاق حلقة `for`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:178]

```
179:         // Use postValue for thread safety - this can be called from background threads  
```
> تعليق: «استعمل postValue لأمان الخيوط - يمكن استدعاء هذا من خيوط الخلفية». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:179]

```
180:         state.setGeohashParticipantCounts(counts)
```
> يستدعي `setGeohashParticipantCounts` على `state` ممرّراً الخريطة `counts`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:180]

```
181:     }
```
> إغلاق نطاق الدالة `updateReactiveParticipantCounts`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:181]

```
182: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:182]

```
183:     fun putNostrKeyMapping(tempKeyOrPeer: String, pubkeyHex: String) {
```
> يعرّف الدالة `putNostrKeyMapping` (وضع تعيين مفتاح nostr) التي تأخذ معاملين سلسلة `tempKeyOrPeer` و `pubkeyHex`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:183]

```
184:         nostrKeyMapping[tempKeyOrPeer] = pubkeyHex
```
> يسند القيمة `pubkeyHex` إلى الخريطة `nostrKeyMapping` عند المفتاح `tempKeyOrPeer`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:184]

```
185:     }
```
> إغلاق نطاق الدالة `putNostrKeyMapping`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:185]

```
186: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:186]

```
187:     fun getNostrKeyMapping(): Map<String, String> = nostrKeyMapping.toMap()
```
> يعرّف الدالة `getNostrKeyMapping` (جلب تعيين مفاتيح nostr) التي تعيد خريطة من سلسلة إلى سلسلة تساوي نسخة من `nostrKeyMapping` عبر `toMap`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:187]

```
188: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:188]

```
189:     fun displayNameForNostrPubkey(pubkeyHex: String): String {
```
> يعرّف الدالة `displayNameForNostrPubkey` (اسم العرض لمفتاح nostr العام) التي تأخذ معاملاً سلسلة `pubkeyHex` وتعيد سلسلة، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:189]

```
190:         val suffix = pubkeyHex.takeLast(4)
```
> يعرّف متغيراً للقراءة فقط باسم `suffix` (اللاحقة) يساوي آخر أربعة محارف من `pubkeyHex` عبر `takeLast(4)`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:190]

```
191:         val lower = pubkeyHex.lowercase()
```
> يعرّف متغيراً للقراءة فقط باسم `lower` يساوي `pubkeyHex` بحروف صغيرة. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:191]

```
192:         // Self nickname if matches current identity of current geohash
```
> تعليق: «الاسم المستعار للذات إن طابق الهوية الحالية للموقع الجغرافي الحالي». [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:192]

```
193:         val current = currentGeohash
```
> يعرّف متغيراً للقراءة فقط باسم `current` (الحالي) يساوي قيمة الحقل `currentGeohash`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:193]

```
194:         if (current != null) {
```
> يفحص ما إذا كان `current` غير عدم، ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:194]

```
195:             try {
```
> يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:195]

```
196:                 val my = NostrIdentityBridge.deriveIdentity(current, application)
```
> يعرّف متغيراً للقراءة فقط باسم `my` (هويتي) يساوي ناتج `NostrIdentityBridge.deriveIdentity` ممرّراً `current` و `application`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:196]

```
197:                 if (my.publicKeyHex.equals(lower, true)) {
```
> يفحص ما إذا كان `publicKeyHex` من `my` يساوي `lower` مع تجاهل حالة الأحرف (true)، ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:197]

```
198:                     return "${state.getNicknameValue()}#$suffix"
```
> يعيد سلسلة مُركّبة من ناتج `getNicknameValue` من `state` متبوعاً بـ "#" ثم `suffix`. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:198]

```
199:                 }
```
> إغلاق نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:199]

```
200:             } catch (_: Exception) {}
```
> يلتقط أي استثناء (Exception) بلا تسمية بجسم فارغ (لا يفعل شيئاً). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:200]
