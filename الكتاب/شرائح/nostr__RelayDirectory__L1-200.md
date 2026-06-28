# شريحة — app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يضبط هذا السطر اسم الحزمة (package) ليكون `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:2]

```
3: import android.app.Application
```
> يستورد (import) الصنف `Application` من `android.app`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:3]

```
4: import android.content.SharedPreferences
```
> يستورد الصنف `SharedPreferences` من `android.content`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:4]

```
5: import android.util.Log
```
> يستورد الصنف `Log` من `android.util`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:5]

```
6: import java.io.BufferedReader
```
> يستورد الصنف `BufferedReader` من `java.io`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:6]

```
7: import java.io.File
```
> يستورد الصنف `File` من `java.io`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:7]

```
8: import java.io.FileInputStream
```
> يستورد الصنف `FileInputStream` من `java.io`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:8]

```
9: import java.io.FileOutputStream
```
> يستورد الصنف `FileOutputStream` من `java.io`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:9]

```
10: import java.io.InputStream
```
> يستورد الصنف `InputStream` من `java.io`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:10]

```
11: import java.io.InputStreamReader
```
> يستورد الصنف `InputStreamReader` من `java.io`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:11]

```
12: import java.security.MessageDigest
```
> يستورد الصنف `MessageDigest` من `java.security`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:12]

```
13: import java.util.concurrent.TimeUnit
```
> يستورد الصنف `TimeUnit` من `java.util.concurrent`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:13]

```
14: import kotlin.math.*
```
> يستورد كل العناصر (`*`) من حزمة `kotlin.math`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:14]

```
15: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف `CoroutineScope` من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:15]

```
16: import kotlinx.coroutines.Dispatchers
```
> يستورد الكائن `Dispatchers` من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:16]

```
17: import kotlinx.coroutines.SupervisorJob
```
> يستورد `SupervisorJob` من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:17]

```
18: import kotlinx.coroutines.delay
```
> يستورد الدالة `delay` من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:18]

```
19: import kotlinx.coroutines.launch
```
> يستورد الدالة `launch` من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:19]

```
20: import okhttp3.OkHttpClient
```
> يستورد الصنف `OkHttpClient` من `okhttp3`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:20]

```
21: import okhttp3.Request
```
> يستورد الصنف `Request` من `okhttp3`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:21]

```
22: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:22]

```
23: /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:23]

```
24:  * Loads relay coordinates from assets and provides nearest-relay lookup by geohash.
```
> تعليق: «يُحمّل إحداثيات المُرحِّلات (relay) من الأصول ويوفّر بحثاً عن أقرب مُرحِّل بحسب الـ geohash». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:24]

```
25:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:25]

```
26: object RelayDirectory {
```
> يُعرّف كائناً مفرداً (object) باسم `RelayDirectory` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:27]

```
28:     private const val TAG = "RelayDirectory"
```
> يُعرّف ثابتاً خاصاً (private const) باسم `TAG` بقيمة نصية `"RelayDirectory"`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:28]

```
29:     private const val ASSET_FILE_URL = "https://raw.githubusercontent.com/permissionlesstech/georelays/refs/heads/main/nostr_relays.csv"
```
> يُعرّف ثابتاً خاصاً باسم `ASSET_FILE_URL` بقيمة الرابط النصي `"https://raw.githubusercontent.com/permissionlesstech/georelays/refs/heads/main/nostr_relays.csv"`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:29]

```
30:     private const val ASSET_FILE = "nostr_relays.csv"
```
> يُعرّف ثابتاً خاصاً باسم `ASSET_FILE` بقيمة نصية `"nostr_relays.csv"`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:30]

```
31:     private const val DOWNLOADED_FILE = "nostr_relays_latest.csv"
```
> يُعرّف ثابتاً خاصاً باسم `DOWNLOADED_FILE` بقيمة نصية `"nostr_relays_latest.csv"`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:31]

```
32:     private const val PREFS_NAME = "relay_directory_prefs"
```
> يُعرّف ثابتاً خاصاً باسم `PREFS_NAME` بقيمة نصية `"relay_directory_prefs"`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:32]

```
33:     private const val KEY_LAST_UPDATE_MS = "last_update_ms"
```
> يُعرّف ثابتاً خاصاً باسم `KEY_LAST_UPDATE_MS` بقيمة نصية `"last_update_ms"`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:33]

```
34:     private val ONE_DAY_MS = TimeUnit.DAYS.toMillis(1)
```
> يُعرّف متغيراً خاصاً للقراءة فقط (val) باسم `ONE_DAY_MS` بقيمة `TimeUnit.DAYS.toMillis(1)`، أي عدد الميلي ثانية في يوم واحد. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:34]

```
35: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:35]

```
36:     private val ioScope = CoroutineScope(SupervisorJob() + Dispatchers.IO)
```
> يُعرّف متغيراً خاصاً للقراءة فقط باسم `ioScope` بقيمة نطاق كوروتين `CoroutineScope` مُركَّب من `SupervisorJob()` مجموعاً مع `Dispatchers.IO`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:36]

```
37:     private val httpClient: OkHttpClient
```
> يُعرّف متغيراً خاصاً للقراءة فقط باسم `httpClient` من النوع `OkHttpClient` (مع مُحصِّل في السطر التالي). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:37]

```
38:         get() = com.bitchat.android.net.OkHttpProvider.httpClient()
```
> يُعرّف مُحصِّلاً (get) للمتغيّر `httpClient` يُعيد ناتج استدعاء `com.bitchat.android.net.OkHttpProvider.httpClient()`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:38]

```
39: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:39]

```
40:     data class RelayInfo(
```
> يُعرّف صنف بيانات (data class) باسم `RelayInfo` ويفتح قائمة معطياته. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:40]

```
41:         val url: String,
```
> يُعرّف معطىً للقراءة فقط باسم `url` من النوع `String`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:41]

```
42:         val latitude: Double,
```
> يُعرّف معطىً للقراءة فقط باسم `latitude` (خط العرض) من النوع `Double`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:42]

```
43:         val longitude: Double
```
> يُعرّف معطىً للقراءة فقط باسم `longitude` (خط الطول) من النوع `Double`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:43]

```
44:     )
```
> إغلاق قائمة معطيات صنف البيانات `RelayInfo`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:44]

```
45: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:45]

```
46:     @Volatile
```
> يضع تعليقاً توضيحياً (annotation) باسم `@Volatile` على العنصر التالي. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:46]

```
47:     private var initialized: Boolean = false
```
> يُعرّف متغيراً خاصاً قابلاً للتغيير (var) باسم `initialized` من النوع `Boolean` بقيمة ابتدائية `false`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:47]

```
48: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:48]

```
49:     private val relays: MutableList<RelayInfo> = mutableListOf()
```
> يُعرّف متغيراً خاصاً للقراءة فقط باسم `relays` من النوع `MutableList<RelayInfo>` بقيمة قائمة فارغة قابلة للتغيير `mutableListOf()`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:49]

```
50:     private val relaysLock = Any()
```
> يُعرّف متغيراً خاصاً للقراءة فقط باسم `relaysLock` بقيمة كائن جديد `Any()`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:50]

```
51: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:51]

```
52:     fun initialize(application: Application) {
```
> يُعرّف دالة عامة باسم `initialize` تأخذ معطى `application` من النوع `Application` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:52]

```
53:         if (initialized) return
```
> يفحص: إذا كان `initialized` صحيحاً فإنه يرجع (`return`) دون متابعة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:53]

```
54:         synchronized(this) {
```
> يبدأ كتلة متزامنة (synchronized) على القفل `this` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:54]

```
55:             if (initialized) return
```
> يفحص: إذا كان `initialized` صحيحاً فإنه يرجع دون متابعة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:55]

```
56:             try {
```
> يبدأ كتلة `try` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:56]

```
57:                 val downloaded = getDownloadedFile(application)
```
> يُعرّف متغيراً للقراءة فقط باسم `downloaded` بقيمة ناتج استدعاء `getDownloadedFile(application)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:57]

```
58:                 val loadedFromDownloaded = if (downloaded.exists() && downloaded.canRead()) {
```
> يُعرّف متغيراً للقراءة فقط باسم `loadedFromDownloaded` بقيمة تعبير شرطي `if`: إذا كان `downloaded.exists()` و`downloaded.canRead()` معاً صحيحين. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:58]

```
59:                     loadFromFile(downloaded, sourceLabel = "downloaded")
```
> في حالة الصدق يُسند ناتج استدعاء `loadFromFile(downloaded, sourceLabel = "downloaded")`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:59]

```
60:                 } else {
```
> يُغلق فرع الصدق ويفتح فرع `else`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:60]

```
61:                     false
```
> في حالة `else` تكون القيمة `false`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:61]

```
62:                 }
```
> إغلاق نطاق التعبير الشرطي `if/else`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:62]

```
63: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:63]

```
64:                 if (!loadedFromDownloaded) {
```
> يفحص: إذا كان `loadedFromDownloaded` غير صحيح (`!`) ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:64]

```
65:                     loadFromAssets(application)
```
> يستدعي `loadFromAssets(application)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:65]

```
66:                 }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:66]

```
67: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:67]

```
68:                 initialized = true
```
> يُسند القيمة `true` إلى المتغيّر `initialized`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:68]

```
69: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:69]

```
70:                 // Trigger an immediate fetch if the data is stale (older than 24h)
```
> تعليق: «أطلِق جلباً فورياً إذا كانت البيانات قديمة (أقدم من 24 ساعة)». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:70]

```
71:                 ioScope.launch {
```
> يستدعي `ioScope.launch` لبدء كوروتين ويفتح نطاق كتلته. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:71]

```
72:                     if (isStale(application)) {
```
> يفحص: إذا كان ناتج `isStale(application)` صحيحاً ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:72]

```
73:                         fetchAndMaybeSwap(application)
```
> يستدعي `fetchAndMaybeSwap(application)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:73]

```
74:                     }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:74]

```
75:                 }
```
> إغلاق نطاق كتلة `ioScope.launch`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:75]

```
76: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:76]

```
77:                 // Start periodic staleness check every minute
```
> تعليق: «ابدأ فحص القِدَم الدوري كل دقيقة». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:77]

```
78:                 startPeriodicRefresh(application)
```
> يستدعي `startPeriodicRefresh(application)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:78]

```
79:             } catch (e: Exception) {
```
> يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من النوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:79]

```
80:                 Log.e(TAG, "Failed to initialize RelayDirectory: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ورسالة «Failed to initialize RelayDirectory:» متبوعة برسالة الاستثناء `${e.message}`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:80]

```
81:             }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:81]

```
82:         }
```
> إغلاق نطاق الكتلة المتزامنة `synchronized`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:82]

```
83:     }
```
> إغلاق نطاق الدالة `initialize`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:83]

```
84: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:84]

```
85:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:85]

```
86:      * Return up to nRelays closest relay URLs to the geohash center.
```
> تعليق: «أعِد حتى عدد nRelays من أقرب روابط المُرحِّلات إلى مركز الـ geohash». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:86]

```
87:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:87]

```
88:     fun closestRelaysForGeohash(geohash: String, nRelays: Int): List<String> {
```
> يُعرّف دالة عامة باسم `closestRelaysForGeohash` تأخذ `geohash` من النوع `String` و`nRelays` من النوع `Int` وتُعيد `List<String>`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:88]

```
89:         val snapshot = synchronized(relaysLock) { relays.toList() }
```
> يُعرّف متغيراً للقراءة فقط باسم `snapshot` بقيمة ناتج كتلة متزامنة على `relaysLock` تُعيد `relays.toList()` (نسخة من القائمة). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:89]

```
90:         if (snapshot.isEmpty()) return emptyList()
```
> يفحص: إذا كان `snapshot` فارغاً فإنه يُعيد قائمة فارغة `emptyList()`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:90]

```
91:         val center = try {
```
> يُعرّف متغيراً للقراءة فقط باسم `center` بقيمة ناتج كتلة `try` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:91]

```
92:             val c = com.bitchat.android.geohash.Geohash.decodeToCenter(geohash)
```
> يُعرّف متغيراً للقراءة فقط باسم `c` بقيمة ناتج استدعاء `com.bitchat.android.geohash.Geohash.decodeToCenter(geohash)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:92]

```
93:             c
```
> يُرجِع قيمة `c` كناتج لكتلة `try`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:93]

```
94:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من النوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:94]

```
95:             Log.e(TAG, "Failed to decode geohash '$geohash': ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ورسالة «Failed to decode geohash '$geohash':» متبوعة برسالة الاستثناء `${e.message}`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:95]

```
96:             return emptyList()
```
> يُعيد قائمة فارغة `emptyList()` خروجاً من الدالة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:96]

```
97:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:97]

```
98: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:98]

```
99:         val (lat, lon) = center
```
> يُفكِّك (destructuring) الكائن `center` إلى متغيرين للقراءة فقط هما `lat` و`lon`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:99]

```
100:         return snapshot
```
> يبدأ تعبير `return` يُعيد سلسلة عمليات على `snapshot` (تستمر في الأسطر التالية). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:100]

```
101:             .asSequence()
```
> يستدعي `.asSequence()` لتحويل القائمة إلى متتالية كسولة (sequence). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:101]

```
102:             .sortedBy { haversineMeters(lat, lon, it.latitude, it.longitude) }
```
> يستدعي `.sortedBy` بترتيب العناصر بحسب ناتج `haversineMeters(lat, lon, it.latitude, it.longitude)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:102]

```
103:             .take(nRelays.coerceAtLeast(0))
```
> يستدعي `.take` لأخذ عدد من العناصر يساوي `nRelays.coerceAtLeast(0)` (أي `nRelays` مقيّداً ليكون صفراً على الأقل). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:103]

```
104:             .map { it.url }
```
> يستدعي `.map` لتحويل كل عنصر إلى حقله `it.url`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:104]

```
105:             .toList()
```
> يستدعي `.toList()` لتحويل المتتالية إلى قائمة (وهي القيمة المُعادة). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:105]

```
106:     }
```
> إغلاق نطاق الدالة `closestRelaysForGeohash`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:106]

```
107: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:107]

```
108:     private fun haversineMeters(lat1: Double, lon1: Double, lat2: Double, lon2: Double): Double {
```
> يُعرّف دالة خاصة باسم `haversineMeters` تأخذ `lat1`, `lon1`, `lat2`, `lon2` من النوع `Double` وتُعيد `Double`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:108]

```
109:         val R = 6371000.0 // meters
```
> يُعرّف متغيراً للقراءة فقط باسم `R` بقيمة `6371000.0` مع تعليق: «أمتار». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:109]

```
110:         val dLat = Math.toRadians(lat2 - lat1)
```
> يُعرّف متغيراً للقراءة فقط باسم `dLat` بقيمة `Math.toRadians(lat2 - lat1)` (الفرق بين خطّي العرض بالراديان). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:110]

```
111:         val dLon = Math.toRadians(lon2 - lon1)
```
> يُعرّف متغيراً للقراءة فقط باسم `dLon` بقيمة `Math.toRadians(lon2 - lon1)` (الفرق بين خطّي الطول بالراديان). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:111]

```
112:         val a = sin(dLat / 2).pow(2.0) + cos(Math.toRadians(lat1)) * cos(Math.toRadians(lat2)) * sin(dLon / 2).pow(2.0)
```
> يُعرّف متغيراً للقراءة فقط باسم `a` بقيمة `sin(dLat / 2).pow(2.0) + cos(Math.toRadians(lat1)) * cos(Math.toRadians(lat2)) * sin(dLon / 2).pow(2.0)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:112]

```
113:         val c = 2 * atan2(sqrt(a), sqrt(1 - a))
```
> يُعرّف متغيراً للقراءة فقط باسم `c` بقيمة `2 * atan2(sqrt(a), sqrt(1 - a))`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:113]

```
114:         return R * c
```
> يُعيد ناتج `R * c`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:114]

```
115:     }
```
> إغلاق نطاق الدالة `haversineMeters`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:115]

```
116: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:116]

```
117:     private fun normalizeRelayUrl(raw: String): String {
```
> يُعرّف دالة خاصة باسم `normalizeRelayUrl` تأخذ `raw` من النوع `String` وتُعيد `String`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:117]

```
118:         val trimmed = raw.trim()
```
> يُعرّف متغيراً للقراءة فقط باسم `trimmed` بقيمة `raw.trim()` (النص بعد إزالة الفراغات الطرفية). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:118]

```
119:         if (trimmed.isEmpty()) return trimmed
```
> يفحص: إذا كان `trimmed` فارغاً فإنه يُعيد `trimmed`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:119]

```
120:         return if ("://" in trimmed) trimmed else "wss://$trimmed"
```
> يُعيد تعبيراً شرطياً: إذا احتوى `trimmed` على `"://"` فيُعيد `trimmed`، وإلا يُعيد `"wss://$trimmed"`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:120]

```
121:     }
```
> إغلاق نطاق الدالة `normalizeRelayUrl`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:121]

```
122: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:122]

```
123:     // ===== Implementation details =====
```
> تعليق: «===== تفاصيل التنفيذ =====». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:123]

```
124: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:124]

```
125:     private fun getPrefs(application: Application): SharedPreferences =
```
> يُعرّف دالة خاصة باسم `getPrefs` تأخذ `application` من النوع `Application` وتُعيد `SharedPreferences` بتعبير واحد (يستمر في السطر التالي). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:125]

```
126:         application.getSharedPreferences(PREFS_NAME, Application.MODE_PRIVATE)
```
> القيمة المُعادة هي ناتج `application.getSharedPreferences(PREFS_NAME, Application.MODE_PRIVATE)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:126]

```
127: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:127]

```
128:     private fun getDownloadedFile(application: Application): File =
```
> يُعرّف دالة خاصة باسم `getDownloadedFile` تأخذ `application` من النوع `Application` وتُعيد `File` بتعبير واحد (يستمر في السطر التالي). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:128]

```
129:         File(application.filesDir, DOWNLOADED_FILE)
```
> القيمة المُعادة هي كائن `File` جديد بالمسار `application.filesDir` والاسم `DOWNLOADED_FILE`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:129]

```
130: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:130]

```
131:     private fun isStale(application: Application): Boolean {
```
> يُعرّف دالة خاصة باسم `isStale` تأخذ `application` من النوع `Application` وتُعيد `Boolean`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:131]

```
132:         val last = getPrefs(application).getLong(KEY_LAST_UPDATE_MS, 0L)
```
> يُعرّف متغيراً للقراءة فقط باسم `last` بقيمة `getPrefs(application).getLong(KEY_LAST_UPDATE_MS, 0L)` (القيمة المخزّنة أو `0L` افتراضاً). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:132]

```
133:         val now = System.currentTimeMillis()
```
> يُعرّف متغيراً للقراءة فقط باسم `now` بقيمة `System.currentTimeMillis()` (الوقت الحالي بالميلي ثانية). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:133]

```
134:         return now - last >= ONE_DAY_MS
```
> يُعيد نتيجة المقارنة `now - last >= ONE_DAY_MS`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:134]

```
135:     }
```
> إغلاق نطاق الدالة `isStale`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:135]

```
136: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:136]

```
137:     private fun startPeriodicRefresh(application: Application) {
```
> يُعرّف دالة خاصة باسم `startPeriodicRefresh` تأخذ `application` من النوع `Application` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:137]

```
138:         ioScope.launch {
```
> يستدعي `ioScope.launch` لبدء كوروتين ويفتح نطاق كتلته. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:138]

```
139:             while (true) {
```
> يبدأ حلقة `while` بشرط `true` (لا نهائية) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:139]

```
140:                 try {
```
> يبدأ كتلة `try` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:140]

```
141:                     if (isStale(application)) {
```
> يفحص: إذا كان ناتج `isStale(application)` صحيحاً ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:141]

```
142:                         fetchAndMaybeSwap(application)
```
> يستدعي `fetchAndMaybeSwap(application)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:142]

```
143:                     }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:143]

```
144:                 } catch (e: Exception) {
```
> يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من النوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:144]

```
145:                     Log.w(TAG, "Periodic refresh encountered an error: ${e.message}")
```
> يستدعي `Log.w` بالوسم `TAG` ورسالة «Periodic refresh encountered an error:» متبوعة برسالة الاستثناء `${e.message}`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:145]

```
146:                 }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:146]

```
147:                 delay(TimeUnit.MINUTES.toMillis(1))
```
> يستدعي `delay` بقيمة `TimeUnit.MINUTES.toMillis(1)` (تأخير دقيقة واحدة بالميلي ثانية). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:147]

```
148:             }
```
> إغلاق نطاق حلقة `while`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:148]

```
149:         }
```
> إغلاق نطاق كتلة `ioScope.launch`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:149]

```
150:     }
```
> إغلاق نطاق الدالة `startPeriodicRefresh`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:150]

```
151: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:151]

```
152:     private fun fetchAndMaybeSwap(application: Application) {
```
> يُعرّف دالة خاصة باسم `fetchAndMaybeSwap` تأخذ `application` من النوع `Application` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:152]

```
153:         try {
```
> يبدأ كتلة `try` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:153]

```
154:             val tmpFile = File.createTempFile("relays_", ".csv", application.cacheDir)
```
> يُعرّف متغيراً للقراءة فقط باسم `tmpFile` بقيمة `File.createTempFile("relays_", ".csv", application.cacheDir)` (ملف مؤقت). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:154]

```
155:             val ok = downloadToFile(ASSET_FILE_URL, tmpFile)
```
> يُعرّف متغيراً للقراءة فقط باسم `ok` بقيمة ناتج `downloadToFile(ASSET_FILE_URL, tmpFile)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:155]

```
156:             if (!ok) {
```
> يفحص: إذا كان `ok` غير صحيح (`!`) ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:156]

```
157:                 Log.w(TAG, "Failed to fetch latest relays; keeping current list (will fallback to bundled if none)")
```
> يستدعي `Log.w` بالوسم `TAG` ورسالة «Failed to fetch latest relays; keeping current list (will fallback to bundled if none)». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:157]

```
158:                 tmpFile.delete()
```
> يستدعي `tmpFile.delete()` لحذف الملف المؤقت. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:158]

```
159:                 return
```
> يرجع (`return`) خروجاً من الدالة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:159]

```
160:             }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:160]

```
161: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:161]

```
162:             val parsed = parseCsv(FileInputStream(tmpFile))
```
> يُعرّف متغيراً للقراءة فقط باسم `parsed` بقيمة ناتج `parseCsv(FileInputStream(tmpFile))`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:162]

```
163:             if (parsed.isEmpty()) {
```
> يفحص: إذا كان `parsed` فارغاً ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:163]

```
164:                 Log.w(TAG, "Downloaded relay CSV parsed to 0 entries; ignoring")
```
> يستدعي `Log.w` بالوسم `TAG` ورسالة «Downloaded relay CSV parsed to 0 entries; ignoring». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:164]

```
165:                 tmpFile.delete()
```
> يستدعي `tmpFile.delete()` لحذف الملف المؤقت. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:165]

```
166:                 return
```
> يرجع (`return`) خروجاً من الدالة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:166]

```
167:             }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:167]

```
168: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:168]

```
169:             val dest = getDownloadedFile(application)
```
> يُعرّف متغيراً للقراءة فقط باسم `dest` بقيمة ناتج `getDownloadedFile(application)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:169]

```
170:             tmpFile.inputStream().use { input ->
```
> يستدعي `tmpFile.inputStream().use` ويسمّي مجرى الدخل `input` ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:170]

```
171:                 FileOutputStream(dest, false).use { output ->
```
> يُنشئ `FileOutputStream(dest, false)` ويستدعي `.use` ويسمّي مجرى الخرج `output` ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:171]

```
172:                     input.copyTo(output)
```
> يستدعي `input.copyTo(output)` لنسخ محتوى الدخل إلى الخرج. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:172]

```
173:                 }
```
> إغلاق نطاق كتلة `output.use`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:173]

```
174:             }
```
> إغلاق نطاق كتلة `input.use`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:174]

```
175:             tmpFile.delete()
```
> يستدعي `tmpFile.delete()` لحذف الملف المؤقت. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:175]

```
176: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:176]

```
177:             val hash = fileSha256Hex(dest)
```
> يُعرّف متغيراً للقراءة فقط باسم `hash` بقيمة ناتج `fileSha256Hex(dest)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:177]

```
178:             val entries = parsed.size
```
> يُعرّف متغيراً للقراءة فقط باسم `entries` بقيمة `parsed.size` (عدد عناصر القائمة المُحلّلة). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:178]

```
179: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:179]

```
180:             synchronized(relaysLock) {
```
> يبدأ كتلة متزامنة على `relaysLock` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:180]

```
181:                 relays.clear()
```
> يستدعي `relays.clear()` لتفريغ القائمة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:181]

```
182:                 relays.addAll(parsed)
```
> يستدعي `relays.addAll(parsed)` لإضافة كل عناصر `parsed` إلى القائمة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:182]

```
183:             }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:183]

```
184: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:184]

```
185:             getPrefs(application).edit().putLong(KEY_LAST_UPDATE_MS, System.currentTimeMillis()).apply()
```
> يستدعي `getPrefs(application).edit().putLong(KEY_LAST_UPDATE_MS, System.currentTimeMillis()).apply()` لتخزين الوقت الحالي تحت مفتاح `KEY_LAST_UPDATE_MS`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:185]

```
186: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:186]

```
187:             Log.i(TAG, "✅ Using downloaded relay list (${dest.absolutePath}), entries=$entries, sha256=$hash, updatedAtMs=${getPrefs(application).getLong(KEY_LAST_UPDATE_MS, 0L)}")
```
> يستدعي `Log.i` بالوسم `TAG` ورسالة «✅ Using downloaded relay list (${dest.absolutePath}), entries=$entries, sha256=$hash, updatedAtMs=...» مُضمّناً قيمة `getPrefs(application).getLong(KEY_LAST_UPDATE_MS, 0L)`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:187]

```
188:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من النوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:188]

```
189:             Log.w(TAG, "Failed to fetch and swap relay list: ${e.message}")
```
> يستدعي `Log.w` بالوسم `TAG` ورسالة «Failed to fetch and swap relay list:» متبوعة برسالة الاستثناء `${e.message}`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:189]

```
190:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:190]

```
191:     }
```
> إغلاق نطاق الدالة `fetchAndMaybeSwap`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:191]

```
192: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:192]

```
193:     private fun downloadToFile(url: String, dest: File): Boolean {
```
> يُعرّف دالة خاصة باسم `downloadToFile` تأخذ `url` من النوع `String` و`dest` من النوع `File` وتُعيد `Boolean`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:193]

```
194:         return try {
```
> يبدأ تعبير `return` يُعيد ناتج كتلة `try` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:194]

```
195:             val req = Request.Builder().url(url).get().build()
```
> يُعرّف متغيراً للقراءة فقط باسم `req` بقيمة `Request.Builder().url(url).get().build()` (طلب HTTP من نوع GET). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:195]

```
196:             httpClient.newCall(req).execute().use { resp ->
```
> يستدعي `httpClient.newCall(req).execute().use` ويسمّي الاستجابة `resp` ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:196]

```
197:                 if (!resp.isSuccessful) {
```
> يفحص: إذا كانت `resp.isSuccessful` غير صحيحة (`!`) ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:197]

```
198:                     Log.w(TAG, "HTTP ${'$'}{resp.code} when fetching $url")
```
> يستدعي `Log.w` بالوسم `TAG` ورسالة «HTTP ${'$'}{resp.code} when fetching $url»؛ حيث `${'$'}` يُدرِج رمز الدولار حرفياً متبوعاً بـ `{resp.code}` و`$url`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:198]

```
199:                     return false
```
> يُعيد `false` خروجاً من الدالة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:199]

```
200:                 }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:200]
