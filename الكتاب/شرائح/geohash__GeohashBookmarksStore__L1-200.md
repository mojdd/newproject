# شريحة — app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt (الأسطر 1–200)

```
1: package com.bitchat.android.geohash
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.geohash. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف Context من android.content. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:3]

```
4: import android.location.Geocoder
```
> يستورد الصنف Geocoder من android.location. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:4]

```
5: import android.location.Location
```
> يستورد الصنف Location من android.location. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:5]

```
6: import android.location.LocationManager
```
> يستورد الصنف LocationManager من android.location. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:6]

```
7: import android.util.Log
```
> يستورد الصنف Log من android.util. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:7]

```
8: import com.google.gson.Gson
```
> يستورد الصنف Gson من com.google.gson. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:8]

```
9: import com.google.gson.reflect.TypeToken
```
> يستورد الصنف TypeToken من com.google.gson.reflect. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:9]

```
10: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف CoroutineScope من kotlinx.coroutines. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:10]

```
11: import kotlinx.coroutines.Dispatchers
```
> يستورد الكائن Dispatchers من kotlinx.coroutines. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:11]

```
12: import kotlinx.coroutines.launch
```
> يستورد الدالة launch من kotlinx.coroutines. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:12]

```
13: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد الصنف MutableStateFlow من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:13]

```
14: import kotlinx.coroutines.flow.StateFlow
```
> يستورد الصنف StateFlow من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:14]

```
15: import kotlinx.coroutines.flow.asStateFlow
```
> يستورد الدالة asStateFlow من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:15]

```
16: import java.util.Locale
```
> يستورد الصنف Locale من java.util. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:17]

```
18: /**
```
> تعليق: بداية كتلة توثيق (تعليق متعدد الأسطر). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:18]

```
19:  * Stores a user-maintained list of bookmarked geohash channels.
```
> تعليق: يخزّن قائمة قنوات geohash المُعلَّمة كمفضّلة والتي يحافظ عليها المستخدم. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:19]

```
20:  * - Persistence: SharedPreferences (JSON string array)
```
> تعليق: الحفظ يتم عبر SharedPreferences (مصفوفة نصوص بصيغة JSON). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:20]

```
21:  * - Semantics: geohashes are normalized to lowercase base32 and de-duplicated
```
> تعليق: الدلالة هي أن قيم geohash تُطبَّع إلى base32 بأحرف صغيرة وتُزال منها التكرارات. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:21]

```
22:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:22]

```
23: class GeohashBookmarksStore private constructor(private val context: Context) {
```
> يعرّف الصنف مخزن مفضّلات الجيوهاش (GeohashBookmarksStore) ببانٍ (constructor) خاص private يأخذ معاملاً خاصاً للقراءة فقط باسم context من النوع Context، ويفتح نطاق الصنف. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:24]

```
25:     companion object {
```
> يفتح كائناً مرافقاً (companion object) داخل الصنف. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:25]

```
26:         private const val TAG = "GeohashBookmarksStore"
```
> يعرّف ثابتاً خاصاً TAG من نوع نص وقيمته "GeohashBookmarksStore". [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:26]

```
27:         private const val STORE_KEY = "locationChannel.bookmarks"
```
> يعرّف ثابتاً خاصاً STORE_KEY من نوع نص وقيمته "locationChannel.bookmarks". [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:27]

```
28:         private const val NAMES_STORE_KEY = "locationChannel.bookmarkNames"
```
> يعرّف ثابتاً خاصاً NAMES_STORE_KEY من نوع نص وقيمته "locationChannel.bookmarkNames". [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:28]

```
29: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:29]

```
30:         @Volatile private var INSTANCE: GeohashBookmarksStore? = null
```
> يعرّف متغيراً خاصاً قابلاً للتغيير INSTANCE موسوماً بـ@Volatile من النوع GeohashBookmarksStore القابل لأن يكون فارغاً، وقيمته الابتدائية null. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:30]

```
31:         fun getInstance(context: Context): GeohashBookmarksStore {
```
> يعرّف الدالة getInstance التي تأخذ معاملاً context من النوع Context وتُعيد كائناً من النوع GeohashBookmarksStore، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:31]

```
32:             return INSTANCE ?: synchronized(this) {
```
> يُعيد INSTANCE إن لم يكن null، وإلا فيدخل كتلة synchronized على this ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:32]

```
33:                 INSTANCE ?: GeohashBookmarksStore(context.applicationContext).also { INSTANCE = it }
```
> يُعيد INSTANCE إن لم يكن null، وإلا يُنشئ GeohashBookmarksStore بسياق التطبيق context.applicationContext ويسند الكائن الجديد إلى INSTANCE عبر also. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:33]

```
34:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:34]

```
35:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:36]

```
37:         private val allowedChars = "0123456789bcdefghjkmnpqrstuvwxyz".toSet()
```
> يعرّف قيمة خاصة للقراءة فقط allowedChars (الأحرف المسموحة) بتحويل النص "0123456789bcdefghjkmnpqrstuvwxyz" إلى مجموعة عبر toSet. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:37]

```
38:         fun normalize(raw: String): String {
```
> يعرّف الدالة normalize (التطبيع) التي تأخذ معاملاً raw من نوع نص وتُعيد نصاً، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:38]

```
39:             return raw.trim().lowercase(Locale.US)
```
> يُعيد raw بعد إزالة الفراغات الطرفية بـtrim وتحويله إلى أحرف صغيرة بـlowercase وفق Locale.US، ثم يكمل بسلسلة عمليات في الأسطر التالية. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:39]

```
40:                 .replace("#", "")
```
> يستبدل كل ظهور للنص "#" بنص فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:40]

```
41:                 .filter { allowedChars.contains(it) }
```
> يرشّح بـfilter محتفظاً بالأحرف التي تحتويها مجموعة allowedChars فقط. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:41]

```
42:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:42]

```
43:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:43]

```
44: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:44]

```
45:     private val gson = Gson()
```
> يعرّف قيمة خاصة للقراءة فقط gson بإنشاء كائن Gson جديد. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:45]

```
46:     private val prefs = context.getSharedPreferences("geohash_prefs", Context.MODE_PRIVATE)
```
> يعرّف قيمة خاصة للقراءة فقط prefs (التفضيلات) باستدعاء getSharedPreferences على context باسم الملف "geohash_prefs" والوضع Context.MODE_PRIVATE. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:46]

```
47: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:47]

```
48:     private val membership = mutableSetOf<String>()
```
> يعرّف قيمة خاصة للقراءة فقط membership (العضوية) بإنشاء مجموعة قابلة للتغيير من نصوص فارغة عبر mutableSetOf. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:48]

```
49: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:49]

```
50:     private val _bookmarks = MutableStateFlow<List<String>>(emptyList())
```
> يعرّف قيمة خاصة للقراءة فقط _bookmarks بإنشاء MutableStateFlow من نوع قائمة نصوص بقيمة ابتدائية قائمة فارغة emptyList. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:50]

```
51:     val bookmarks: StateFlow<List<String>> = _bookmarks.asStateFlow()
```
> يعرّف قيمة عامة للقراءة فقط bookmarks (المفضّلات) من النوع StateFlow لقائمة نصوص، مسندة من _bookmarks عبر asStateFlow. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:51]

```
52: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:52]

```
53:     private val _bookmarkNames = MutableStateFlow<Map<String, String>>(emptyMap())
```
> يعرّف قيمة خاصة للقراءة فقط _bookmarkNames بإنشاء MutableStateFlow من نوع خريطة نص إلى نص بقيمة ابتدائية خريطة فارغة emptyMap. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:53]

```
54:     val bookmarkNames: StateFlow<Map<String, String>> = _bookmarkNames.asStateFlow()
```
> يعرّف قيمة عامة للقراءة فقط bookmarkNames (أسماء المفضّلات) من النوع StateFlow لخريطة نص إلى نص، مسندة من _bookmarkNames عبر asStateFlow. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:54]

```
55: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:55]

```
56:     // For throttling / preventing duplicate geocode lookups
```
> تعليق: لأجل التحكم بالمعدّل / منع عمليات البحث الجغرافي (geocode) المكرّرة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:56]

```
57:     private val resolving = mutableSetOf<String>()
```
> يعرّف قيمة خاصة للقراءة فقط resolving (قيد الحل) بإنشاء مجموعة قابلة للتغيير من نصوص فارغة عبر mutableSetOf. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:57]

```
58: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:58]

```
59:     init { load() }
```
> يعرّف كتلة تهيئة init تستدعي الدالة load. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:59]

```
60: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:60]

```
61:     fun isBookmarked(geohash: String): Boolean = membership.contains(normalize(geohash))
```
> يعرّف الدالة isBookmarked (هل هو مفضّل) التي تأخذ معاملاً geohash من نوع نص وتُعيد قيمة منطقية، بإرجاع نتيجة استدعاء contains على membership للقيمة normalize(geohash). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:61]

```
62: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:62]

```
63:     fun toggle(geohash: String) {
```
> يعرّف الدالة toggle (التبديل) التي تأخذ معاملاً geohash من نوع نص، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:63]

```
64:         val gh = normalize(geohash)
```
> يعرّف قيمة محلية للقراءة فقط gh بنتيجة normalize(geohash). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:64]

```
65:         if (membership.contains(gh)) remove(gh) else add(gh)
```
> إذا كانت membership تحتوي gh فيستدعي remove(gh)، وإلا فيستدعي add(gh). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:65]

```
66:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:66]

```
67: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:67]

```
68:     fun add(geohash: String) {
```
> يعرّف الدالة add (الإضافة) التي تأخذ معاملاً geohash من نوع نص، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:68]

```
69:         val gh = normalize(geohash)
```
> يعرّف قيمة محلية للقراءة فقط gh بنتيجة normalize(geohash). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:69]

```
70:         if (gh.isEmpty() || membership.contains(gh)) return
```
> إذا كان gh فارغاً عبر isEmpty أو كانت membership تحتوي gh فيعود من الدالة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:70]

```
71:         membership.add(gh)
```
> يضيف gh إلى membership عبر add. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:71]

```
72:         val updated = listOf(gh) + (_bookmarks.value)
```
> يعرّف قيمة محلية للقراءة فقط updated (المحدّثة) بدمج قائمة تحوي gh مع قيمة _bookmarks الحالية. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:72]

```
73:         _bookmarks.value = updated
```
> يسند updated إلى خاصية value الخاصة بـ_bookmarks. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:73]

```
74:         persist(updated)
```
> يستدعي persist بالوسيط updated. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:74]

```
75:         // Resolve friendly name asynchronously
```
> تعليق: يحلّ الاسم الودود (الاسم المقروء) بشكل غير متزامن. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:75]

```
76:         resolveNameIfNeeded(gh)
```
> يستدعي resolveNameIfNeeded بالوسيط gh. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:76]

```
77:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:77]

```
78: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:78]

```
79:     fun remove(geohash: String) {
```
> يعرّف الدالة remove (الإزالة) التي تأخذ معاملاً geohash من نوع نص، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:79]

```
80:         val gh = normalize(geohash)
```
> يعرّف قيمة محلية للقراءة فقط gh بنتيجة normalize(geohash). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:80]

```
81:         if (!membership.contains(gh)) return
```
> إذا لم تكن membership تحتوي gh فيعود من الدالة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:81]

```
82:         membership.remove(gh)
```
> يزيل gh من membership عبر remove. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:82]

```
83:         val updated = (_bookmarks.value).filterNot { it == gh }
```
> يعرّف قيمة محلية للقراءة فقط updated بترشيح قيمة _bookmarks الحالية عبر filterNot مستبعداً العناصر المساوية لـgh. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:83]

```
84:         _bookmarks.value = updated
```
> يسند updated إلى خاصية value الخاصة بـ_bookmarks. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:84]

```
85:         // Remove stored name to avoid stale cache growth
```
> تعليق: يزيل الاسم المخزّن لتفادي تضخّم ذاكرة مؤقتة قديمة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:85]

```
86:         val names = _bookmarkNames.value.toMutableMap()
```
> يعرّف قيمة محلية للقراءة فقط names بتحويل قيمة _bookmarkNames الحالية إلى خريطة قابلة للتغيير عبر toMutableMap. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:86]

```
87:         if (names.remove(gh) != null) {
```
> إذا كانت نتيجة remove للمفتاح gh من names لا تساوي null فيفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:87]

```
88:             _bookmarkNames.value = names
```
> يسند names إلى خاصية value الخاصة بـ_bookmarkNames. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:88]

```
89:             persistNames(names)
```
> يستدعي persistNames بالوسيط names. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:89]

```
90:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:90]

```
91:         persist(updated)
```
> يستدعي persist بالوسيط updated. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:91]

```
92:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:92]

```
93: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:93]

```
94:     // MARK: - Persistence
```
> تعليق: علامة قسم — الحفظ (Persistence). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:94]

```
95: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:95]

```
96:     private fun load() {
```
> يعرّف الدالة الخاصة load (التحميل) دون معاملات، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:96]

```
97:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:97]

```
98:             val arrJson = prefs.getString(STORE_KEY, null)
```
> يعرّف قيمة محلية للقراءة فقط arrJson باستدعاء getString على prefs بالمفتاح STORE_KEY وقيمة افتراضية null. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:98]

```
99:             if (!arrJson.isNullOrEmpty()) {
```
> إذا لم يكن arrJson فارغاً أو null عبر isNullOrEmpty فيفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:99]

```
100:                 val listType = object : TypeToken<List<String>>() {}.type
```
> يعرّف قيمة محلية للقراءة فقط listType بإنشاء كائن مجهول يمدّ TypeToken لقائمة نصوص ثم أخذ خاصية type منه. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:100]

```
101:                 val arr = gson.fromJson<List<String>>(arrJson, listType)
```
> يعرّف قيمة محلية للقراءة فقط arr باستدعاء fromJson على gson من النص arrJson وفق النوع listType، مُعيداً قائمة نصوص. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:101]

```
102:                 val seen = mutableSetOf<String>()
```
> يعرّف قيمة محلية للقراءة فقط seen (المرئية) بإنشاء مجموعة قابلة للتغيير من نصوص فارغة عبر mutableSetOf. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:102]

```
103:                 val ordered = mutableListOf<String>()
```
> يعرّف قيمة محلية للقراءة فقط ordered (المرتّبة) بإنشاء قائمة قابلة للتغيير من نصوص فارغة عبر mutableListOf. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:103]

```
104:                 arr.forEach { raw ->
```
> يكرّر على عناصر arr عبر forEach مسمياً العنصر الحالي raw، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:104]

```
105:                     val gh = normalize(raw)
```
> يعرّف قيمة محلية للقراءة فقط gh بنتيجة normalize(raw). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:105]

```
106:                     if (gh.isNotEmpty() && !seen.contains(gh)) {
```
> إذا كان gh غير فارغ عبر isNotEmpty ولم تكن seen تحتوي gh فيفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:106]

```
107:                         seen.add(gh)
```
> يضيف gh إلى seen عبر add. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:107]

```
108:                         ordered.add(gh)
```
> يضيف gh إلى ordered عبر add. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:108]

```
109:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:109]

```
110:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:110]

```
111:                 membership.clear(); membership.addAll(seen)
```
> يفرّغ membership عبر clear ثم يضيف إليها كل عناصر seen عبر addAll. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:111]

```
112:                 _bookmarks.value = ordered
```
> يسند ordered إلى خاصية value الخاصة بـ_bookmarks. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:112]

```
113:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:113]

```
114:         } catch (e: Exception) {
```
> يلتقط استثناءً من النوع Exception مسمياً إياه e، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:114]

```
115:             Log.e(TAG, "Failed to load bookmarks: ${e.message}")
```
> يسجّل خطأً عبر Log.e بالوسم TAG ورسالة "Failed to load bookmarks: " متبوعة بـe.message. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:115]

```
116:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:116]

```
117:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:117]

```
118:             val namesJson = prefs.getString(NAMES_STORE_KEY, null)
```
> يعرّف قيمة محلية للقراءة فقط namesJson باستدعاء getString على prefs بالمفتاح NAMES_STORE_KEY وقيمة افتراضية null. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:118]

```
119:             if (!namesJson.isNullOrEmpty()) {
```
> إذا لم يكن namesJson فارغاً أو null عبر isNullOrEmpty فيفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:119]

```
120:                 val mapType = object : TypeToken<Map<String, String>>() {}.type
```
> يعرّف قيمة محلية للقراءة فقط mapType بإنشاء كائن مجهول يمدّ TypeToken لخريطة نص إلى نص ثم أخذ خاصية type منه. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:120]

```
121:                 val dict = gson.fromJson<Map<String, String>>(namesJson, mapType)
```
> يعرّف قيمة محلية للقراءة فقط dict (القاموس) باستدعاء fromJson على gson من النص namesJson وفق النوع mapType، مُعيداً خريطة نص إلى نص. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:121]

```
122:                 _bookmarkNames.value = dict
```
> يسند dict إلى خاصية value الخاصة بـ_bookmarkNames. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:122]

```
123:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:123]

```
124:         } catch (e: Exception) {
```
> يلتقط استثناءً من النوع Exception مسمياً إياه e، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:124]

```
125:             Log.e(TAG, "Failed to load bookmark names: ${e.message}")
```
> يسجّل خطأً عبر Log.e بالوسم TAG ورسالة "Failed to load bookmark names: " متبوعة بـe.message. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:125]

```
126:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:126]

```
127:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:127]

```
128: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:128]

```
129:     private fun persist() {
```
> يعرّف الدالة الخاصة persist (الحفظ) دون معاملات، ويفتح نطاقها. غير مؤكّد — في الأسطر 74 و91 يُستدعى persist بوسيط واحد، لكن هذا التعريف بلا معاملات. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:129]

```
130:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:130]

```
131:             val json = gson.toJson(_bookmarks.value)
```
> يعرّف قيمة محلية للقراءة فقط json باستدعاء toJson على gson لقيمة _bookmarks الحالية. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:131]

```
132:             prefs.edit().putString(STORE_KEY, json).apply()
```
> يفتح محرّر prefs عبر edit ويكتب json تحت المفتاح STORE_KEY عبر putString ثم يطبّق التغيير عبر apply. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:132]

```
133:         } catch (_: Exception) {}
```
> يلتقط استثناءً من النوع Exception مع تجاهل اسمه ويترك جسم الكتلة فارغاً. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:133]

```
134:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:134]

```
135: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:135]

```
136:     private fun persistNames() {
```
> يعرّف الدالة الخاصة persistNames (حفظ الأسماء) دون معاملات، ويفتح نطاقها. غير مؤكّد — في السطر 89 يُستدعى persistNames بوسيط واحد، لكن هذا التعريف بلا معاملات. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:136]

```
137:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:137]

```
138:             val json = gson.toJson(_bookmarkNames.value)
```
> يعرّف قيمة محلية للقراءة فقط json باستدعاء toJson على gson لقيمة _bookmarkNames الحالية. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:138]

```
139:             prefs.edit().putString(NAMES_STORE_KEY, json).apply()
```
> يفتح محرّر prefs عبر edit ويكتب json تحت المفتاح NAMES_STORE_KEY عبر putString ثم يطبّق التغيير عبر apply. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:139]

```
140:         } catch (_: Exception) {}
```
> يلتقط استثناءً من النوع Exception مع تجاهل اسمه ويترك جسم الكتلة فارغاً. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:140]

```
141:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:141]

```
142: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:142]

```
143:     // MARK: - Destructive Reset
```
> تعليق: علامة قسم — إعادة ضبط متلفة للبيانات (Destructive Reset). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:143]

```
144: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:144]

```
145:     fun clearAll() {
```
> يعرّف الدالة clearAll (مسح الكل) دون معاملات، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:145]

```
146:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:146]

```
147:             membership.clear()
```
> يفرّغ membership عبر clear. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:147]

```
148:             _bookmarks.value = emptyList()
```
> يسند قائمة فارغة emptyList إلى خاصية value الخاصة بـ_bookmarks. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:148]

```
149:             _bookmarkNames.value = emptyMap()
```
> يسند خريطة فارغة emptyMap إلى خاصية value الخاصة بـ_bookmarkNames. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:149]

```
150:             prefs.edit()
```
> يفتح محرّر prefs عبر edit، ويكمل سلسلة العمليات في الأسطر التالية. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:150]

```
151:                 .remove(STORE_KEY)
```
> يزيل المدخل ذا المفتاح STORE_KEY من المحرّر عبر remove. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:151]

```
152:                 .remove(NAMES_STORE_KEY)
```
> يزيل المدخل ذا المفتاح NAMES_STORE_KEY من المحرّر عبر remove. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:152]

```
153:                 .apply()
```
> يطبّق تغييرات المحرّر عبر apply. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:153]

```
154:             // Clear any in-flight resolutions to avoid repopulating
```
> تعليق: يمسح أي عمليات حل جارية لتفادي إعادة ملء البيانات. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:154]

```
155:             resolving.clear()
```
> يفرّغ resolving عبر clear. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:155]

```
156:             Log.i(TAG, "Cleared all geohash bookmarks and names")
```
> يسجّل معلومة عبر Log.i بالوسم TAG ورسالة "Cleared all geohash bookmarks and names". [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:156]

```
157:         } catch (e: Exception) {
```
> يلتقط استثناءً من النوع Exception مسمياً إياه e، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:157]

```
158:             Log.e(TAG, "Failed to clear geohash bookmarks: ${e.message}")
```
> يسجّل خطأً عبر Log.e بالوسم TAG ورسالة "Failed to clear geohash bookmarks: " متبوعة بـe.message. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:158]

```
159:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:159]

```
160:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:160]

```
161: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:161]

```
162: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:162]

```
163:     // MARK: - Friendly Name Resolution
```
> تعليق: علامة قسم — حل الاسم الودود (Friendly Name Resolution). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:163]

```
164: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:164]

```
165:     fun resolveNameIfNeeded(geohash: String) {
```
> يعرّف الدالة resolveNameIfNeeded (حل الاسم عند الحاجة) التي تأخذ معاملاً geohash من نوع نص، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:165]

```
166:         val gh = normalize(geohash)
```
> يعرّف قيمة محلية للقراءة فقط gh بنتيجة normalize(geohash). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:166]

```
167:         if (gh.isEmpty()) return
```
> إذا كان gh فارغاً عبر isEmpty فيعود من الدالة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:167]

```
168:         if (_bookmarkNames.value?.containsKey(gh) == true) return
```
> إذا كانت قيمة _bookmarkNames الحالية (مع وصول آمن من الفراغ) تحتوي المفتاح gh عبر containsKey بنتيجة true فيعود من الدالة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:168]

```
169:         if (resolving.contains(gh)) return
```
> إذا كانت resolving تحتوي gh فيعود من الدالة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:169]

```
170: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:170]

```
171:         resolving.add(gh)
```
> يضيف gh إلى resolving عبر add. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:171]

```
172:         CoroutineScope(Dispatchers.IO).launch {
```
> يُنشئ CoroutineScope بمرسل الإدخال/الإخراج Dispatchers.IO ويطلق كوروتين عبر launch، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:172]

```
173:             try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:173]

```
174:                 val geocoderProvider = GeocoderFactory.get(context)
```
> يعرّف قيمة محلية للقراءة فقط geocoderProvider (مزوّد المُرمِّز الجغرافي) باستدعاء get على GeocoderFactory بالوسيط context. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:174]

```
175:                 val name: String? = if (gh.length <= 2) {
```
> يعرّف قيمة محلية للقراءة فقط name من نوع نص قابل لأن يكون null، مسندة بتعبير if يختبر إن كان طول gh عبر length أصغر من أو يساوي 2، ويفتح نطاق فرع then. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:175]

```
176:                     // Composite admin name from multiple points
```
> تعليق: اسم إداري مركّب من نقاط متعددة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:176]

```
177:                     val b = Geohash.decodeToBounds(gh)
```
> يعرّف قيمة محلية للقراءة فقط b بنتيجة decodeToBounds على Geohash بالوسيط gh. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:177]

```
178:                     val points = listOf(
```
> يعرّف قيمة محلية للقراءة فقط points (النقاط) بإنشاء قائمة عبر listOf، ويفتح نطاق وسائطها. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:178]

```
179:                         Location(LocationManager.GPS_PROVIDER).apply { latitude = (b.latMin + b.latMax) / 2; longitude = (b.lonMin + b.lonMax) / 2 },
```
> يُنشئ Location بمزوّد LocationManager.GPS_PROVIDER ويضبط عبر apply خاصية latitude إلى متوسط b.latMin وb.latMax وخاصية longitude إلى متوسط b.lonMin وb.lonMax. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:179]

```
180:                         Location(LocationManager.GPS_PROVIDER).apply { latitude = b.latMin; longitude = b.lonMin },
```
> يُنشئ Location بمزوّد LocationManager.GPS_PROVIDER ويضبط عبر apply خاصية latitude إلى b.latMin وخاصية longitude إلى b.lonMin. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:180]

```
181:                         Location(LocationManager.GPS_PROVIDER).apply { latitude = b.latMin; longitude = b.lonMax },
```
> يُنشئ Location بمزوّد LocationManager.GPS_PROVIDER ويضبط عبر apply خاصية latitude إلى b.latMin وخاصية longitude إلى b.lonMax. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:181]

```
182:                         Location(LocationManager.GPS_PROVIDER).apply { latitude = b.latMax; longitude = b.lonMin },
```
> يُنشئ Location بمزوّد LocationManager.GPS_PROVIDER ويضبط عبر apply خاصية latitude إلى b.latMax وخاصية longitude إلى b.lonMin. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:182]

```
183:                         Location(LocationManager.GPS_PROVIDER).apply { latitude = b.latMax; longitude = b.lonMax }
```
> يُنشئ Location بمزوّد LocationManager.GPS_PROVIDER ويضبط عبر apply خاصية latitude إلى b.latMax وخاصية longitude إلى b.lonMax. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:183]

```
184:                     )
```
> إغلاق نطاق وسائط listOf. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:184]

```
185:                     val admins = linkedSetOf<String>()
```
> يعرّف قيمة محلية للقراءة فقط admins (المناطق الإدارية) بإنشاء مجموعة مرتبطة محافظة على الترتيب من نصوص فارغة عبر linkedSetOf. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:185]

```
186:                     for (loc in points) {
```
> يكرّر بحلقة for على عناصر points مسمياً العنصر الحالي loc، ويفتح نطاق الحلقة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:186]

```
187:                         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:187]

```
188:                             val list = geocoderProvider.getFromLocation(loc.latitude, loc.longitude, 1)
```
> يعرّف قيمة محلية للقراءة فقط list باستدعاء getFromLocation على geocoderProvider بـloc.latitude وloc.longitude وعدد نتائج أقصى 1. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:188]

```
189:                             val a = list.firstOrNull()
```
> يعرّف قيمة محلية للقراءة فقط a بأول عنصر من list أو null عبر firstOrNull. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:189]

```
190:                             val admin = a?.adminArea?.takeIf { !it.isNullOrEmpty() }
```
> يعرّف قيمة محلية للقراءة فقط admin بخاصية adminArea من a (مع وصول آمن من الفراغ) إذا اجتازت takeIf شرط أنها ليست فارغة أو null، وإلا فـnull. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:190]

```
191:                             val country = a?.countryName?.takeIf { !it.isNullOrEmpty() }
```
> يعرّف قيمة محلية للقراءة فقط country بخاصية countryName من a (مع وصول آمن من الفراغ) إذا اجتازت takeIf شرط أنها ليست فارغة أو null، وإلا فـnull. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:191]

```
192:                             if (admin != null) admins.add(admin)
```
> إذا لم يكن admin مساوياً null فيضيفه إلى admins عبر add. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:192]

```
193:                             else if (country != null) admins.add(country)
```
> وإلا إذا لم يكن country مساوياً null فيضيفه إلى admins عبر add. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:193]

```
194:                         } catch (_: Exception) {}
```
> يلتقط استثناءً من النوع Exception مع تجاهل اسمه ويترك جسم الكتلة فارغاً. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:194]

```
195:                         if (admins.size >= 2) break
```
> إذا كان حجم admins عبر size أكبر من أو يساوي 2 فيخرج من الحلقة عبر break. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:195]

```
196:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:196]

```
197:                     when (admins.size) {
```
> يفتح تعبير when على حجم admins عبر size، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:197]

```
198:                         0 -> null
```
> في حالة كون الحجم 0 تكون النتيجة null. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:198]

```
199:                         1 -> admins.first()
```
> في حالة كون الحجم 1 تكون النتيجة أول عنصر من admins عبر first. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:199]

```
200:                         else -> admins.elementAt(0) + " and " + admins.elementAt(1)
```
> في الحالة غير ذلك تكون النتيجة دمج العنصر صفر من admins عبر elementAt مع النص " and " مع العنصر واحد من admins عبر elementAt. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:200]
