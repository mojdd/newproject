# شريحة — app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt (الأسطر 1–106)

```
1: package com.bitchat.android.geohash
```
> يعلن أن هذا الملف يتبع الحزمة (package) المسماة com.bitchat.android.geohash. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:2]

```
3: import android.location.Address
```
> يستورد (import) الصنف Address من حزمة android.location. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف Log من حزمة android.util. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:4]

```
5: import com.bitchat.android.net.OkHttpProvider
```
> يستورد الصنف OkHttpProvider من حزمة com.bitchat.android.net. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:5]

```
6: import com.google.gson.Gson
```
> يستورد الصنف Gson من حزمة com.google.gson. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:6]

```
7: import okhttp3.Request
```
> يستورد الصنف Request من حزمة okhttp3. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:7]

```
8: import java.util.Locale
```
> يستورد الصنف Locale (المحلّية) من حزمة java.util. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:8]

```
9: import kotlinx.coroutines.Dispatchers
```
> يستورد الكائن Dispatchers (الموزّعات) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:9]

```
10: import kotlinx.coroutines.withContext
```
> يستورد الدالة withContext من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:11]

```
12: class OpenStreetMapGeocoderProvider : GeocoderProvider {
```
> يُعرّف الصنف (class) المسمى OpenStreetMapGeocoderProvider الذي يطبّق الواجهة GeocoderProvider، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:12]

```
13:     private val TAG = "OSMGeocoderProvider"
```
> يُعرّف خاصية ثابتة خاصة (private val) اسمها TAG وقيمتها النص "OSMGeocoderProvider". [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:13]

```
14:     private val gson = Gson()
```
> يُعرّف خاصية ثابتة خاصة اسمها gson وقيمتها كائن جديد من الصنف Gson. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:14]

```
15:     private val userAgent = "Bitchat-Android/1.0"
```
> يُعرّف خاصية ثابتة خاصة اسمها userAgent (وكيل المستخدم) وقيمتها النص "Bitchat-Android/1.0". [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:16]

```
17:     override suspend fun getFromLocation(latitude: Double, longitude: Double, maxResults: Int): List<Address> {
```
> يُعيد تعريف (override) دالة معلّقة (suspend fun) اسمها getFromLocation تأخذ المعاملات latitude من نوع Double وlongitude من نوع Double وmaxResults من نوع Int، وتُعيد قائمة List من Address، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:17]

```
18:         return withContext(Dispatchers.IO) {
```
> يُعيد نتيجة استدعاء الدالة withContext مع الموزّع Dispatchers.IO، ويفتح كتلة الشيفرة الممرَّرة لها. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:18]

```
19:             val lang = Locale.getDefault().toLanguageTag()
```
> يُعرّف ثابتاً محلياً اسمه lang وقيمته ناتج استدعاء toLanguageTag على المحلّية الافتراضية Locale.getDefault. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:19]

```
20:             // Using format=jsonv2 for structured address breakdown
```
> تعليق: استخدام format=jsonv2 من أجل تفصيل العنوان المنظَّم. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:20]

```
21:             val url = "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=$latitude&lon=$longitude&zoom=18&addressdetails=1&accept-language=$lang"
```
> يُعرّف ثابتاً محلياً اسمه url وقيمته نص العنوان "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=$latitude&lon=$longitude&zoom=18&addressdetails=1&accept-language=$lang" مع إدراج قيم latitude وlongitude وlang داخل النص. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:21]

```
22: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:22]

```
23:             try {
```
> يفتح كتلة try (محاولة). [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:23]

```
24:                 val request = Request.Builder()
```
> يُعرّف ثابتاً محلياً اسمه request ويبدأ سلسلة بناء عبر استدعاء Request.Builder. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:24]

```
25:                     .url(url)
```
> يستدعي الدالة url على البنّاء ويمرّر لها الثابت url. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:25]

```
26:                     .header("User-Agent", userAgent)
```
> يستدعي الدالة header على البنّاء ويمرّر لها المفتاح "User-Agent" والقيمة userAgent. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:26]

```
27:                     .build()
```
> يستدعي الدالة build على البنّاء لإنتاج كائن الطلب. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:28]

```
29:                 val response = OkHttpProvider.httpClient().newCall(request).execute()
```
> يُعرّف ثابتاً محلياً اسمه response وقيمته ناتج استدعاء newCall بالطلب request ثم execute على عميل HTTP المُعاد من OkHttpProvider.httpClient. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:29]

```
30:                 if (!response.isSuccessful) {
```
> يبدأ شرط if يتحقق من أن الخاصية isSuccessful للاستجابة response غير صحيحة (منفية)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:30]

```
31:                     Log.e(TAG, "OSM Request failed: ${response.code}")
```
> يستدعي Log.e بالوسم TAG والرسالة "OSM Request failed: ${response.code}" مع إدراج قيمة response.code داخل النص. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:31]

```
32:                     response.close()
```
> يستدعي الدالة close على الاستجابة response. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:32]

```
33:                     return@withContext emptyList<Address>()
```
> يُعيد من كتلة withContext قائمة فارغة من نوع Address عبر emptyList. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:33]

```
34:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:34]

```
35: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:35]

```
36:                 val body = response.body?.string()
```
> يُعرّف ثابتاً محلياً اسمه body وقيمته ناتج استدعاء string على body للاستجابة response مع استدعاء آمن (?.) يرجع null إن كان body فارغاً. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:36]

```
37:                 response.close()
```
> يستدعي الدالة close على الاستجابة response. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:37]

```
38: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:38]

```
39:                 if (body.isNullOrEmpty()) return@withContext emptyList<Address>()
```
> يتحقق شرط if من أن body فارغ أو null عبر isNullOrEmpty، وعندها يُعيد من كتلة withContext قائمة فارغة من نوع Address. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:39]

```
40: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:40]

```
41:                 try {
```
> يفتح كتلة try (محاولة) متداخلة. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:41]

```
42:                     val osmResponse = gson.fromJson(body, OsmResponse::class.java)
```
> يُعرّف ثابتاً محلياً اسمه osmResponse وقيمته ناتج استدعاء fromJson على gson بالنص body والصنف OsmResponse عبر OsmResponse::class.java. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:42]

```
43:                     if (osmResponse?.address == null) return@withContext emptyList<Address>()
```
> يتحقق شرط if من أن الخاصية address للكائن osmResponse (بوصول آمن) تساوي null، وعندها يُعيد من كتلة withContext قائمة فارغة من نوع Address. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:43]

```
44:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:44]

```
45:                     val address = mapToAddress(osmResponse, latitude, longitude)
```
> يُعرّف ثابتاً محلياً اسمه address وقيمته ناتج استدعاء الدالة mapToAddress بالوسائط osmResponse وlatitude وlongitude. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:45]

```
46:                     listOf(address)
```
> ينتج قائمة تحتوي العنصر address عبر listOf كقيمة كتلة try. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:46]

```
47:                 } catch (e: Exception) {
```
> يغلق كتلة try المتداخلة ويفتح كتلة catch تلتقط استثناءً اسمه e من نوع Exception. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:47]

```
48:                      Log.e(TAG, "OSM Parse failed: ${e.message}")
```
> يستدعي Log.e بالوسم TAG والرسالة "OSM Parse failed: ${e.message}" مع إدراج قيمة e.message داخل النص. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:48]

```
49:                      emptyList<Address>()
```
> ينتج قائمة فارغة من نوع Address عبر emptyList كقيمة كتلة catch. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:49]

```
50:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:50]

```
51:             } catch (e: Exception) {
```
> يغلق كتلة try الخارجية ويفتح كتلة catch تلتقط استثناءً اسمه e من نوع Exception. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:51]

```
52:                 Log.e(TAG, "OSM Geocoding failed", e)
```
> يستدعي Log.e بالوسم TAG والرسالة "OSM Geocoding failed" والاستثناء e. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:52]

```
53:                 emptyList<Address>()
```
> ينتج قائمة فارغة من نوع Address عبر emptyList كقيمة كتلة catch الخارجية. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:53]

```
54:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:54]

```
55:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:55]

```
56:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:56]

```
57: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:57]

```
58:     private fun mapToAddress(res: OsmResponse, lat: Double, lon: Double): Address {
```
> يُعرّف دالة خاصة (private fun) اسمها mapToAddress تأخذ res من نوع OsmResponse وlat من نوع Double وlon من نوع Double، وتُعيد كائناً من نوع Address، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:58]

```
59:         val address = Address(Locale.getDefault())
```
> يُعرّف ثابتاً محلياً اسمه address وقيمته كائن جديد من الصنف Address مُنشأ بالمحلّية الافتراضية Locale.getDefault. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:59]

```
60:         address.latitude = lat
```
> يضبط الخاصية latitude للكائن address على قيمة lat. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:60]

```
61:         address.longitude = lon
```
> يضبط الخاصية longitude للكائن address على قيمة lon. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:61]

```
62:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:62]

```
63:         val a = res.address ?: return address
```
> يُعرّف ثابتاً محلياً اسمه a وقيمته الخاصية address للكائن res، وإن كانت null يُعيد الكائن address عبر عامل إلفيس (?:). [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:63]

```
64: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:64]

```
65:         address.countryName = a.country
```
> يضبط الخاصية countryName للكائن address على قيمة الخاصية country من a. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:65]

```
66:         address.adminArea = a.state
```
> يضبط الخاصية adminArea للكائن address على قيمة الخاصية state من a. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:66]

```
67:         address.subAdminArea = a.county
```
> يضبط الخاصية subAdminArea للكائن address على قيمة الخاصية county من a. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:67]

```
68:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:68]

```
69:         // City logic similar to Google's mapping
```
> تعليق: منطق المدينة مشابه لتعيين Google. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:69]

```
70:         address.locality = a.city ?: a.town ?: a.village ?: a.hamlet
```
> يضبط الخاصية locality للكائن address على أول قيمة غير null من بين a.city ثم a.town ثم a.village ثم a.hamlet عبر سلسلة عوامل إلفيس (?:). [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:70]

```
71:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:71]

```
72:         // Neighborhood logic
```
> تعليق: منطق الحيّ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:72]

```
73:         address.subLocality = a.suburb ?: a.neighbourhood ?: a.residential ?: a.quarter
```
> يضبط الخاصية subLocality للكائن address على أول قيمة غير null من بين a.suburb ثم a.neighbourhood ثم a.residential ثم a.quarter عبر سلسلة عوامل إلفيس (?:). [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:73]

```
74:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:74]

```
75:         address.postalCode = a.postcode
```
> يضبط الخاصية postalCode للكائن address على قيمة الخاصية postcode من a. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:75]

```
76:         address.thoroughfare = a.road
```
> يضبط الخاصية thoroughfare للكائن address على قيمة الخاصية road من a. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:76]

```
77:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:77]

```
78:         // Feature name
```
> تعليق: اسم المَعلَم. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:78]

```
79:         address.featureName = res.name
```
> يضبط الخاصية featureName للكائن address على قيمة الخاصية name من res. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:79]

```
80: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:80]

```
81:         return address
```
> يُعيد الكائن address. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:81]

```
82:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:82]

```
83: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:83]

```
84:     // Data classes for JSON parsing
```
> تعليق: أصناف بيانات لتحليل JSON. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:84]

```
85:     private data class OsmResponse(
```
> يُعرّف صنف بيانات خاص (private data class) اسمه OsmResponse ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:85]

```
86:         val name: String?,
```
> يُعرّف خاصية ثابتة اسمها name من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:86]

```
87:         val display_name: String?,
```
> يُعرّف خاصية ثابتة اسمها display_name من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:87]

```
88:         val address: OsmAddress?
```
> يُعرّف خاصية ثابتة اسمها address من نوع OsmAddress قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:88]

```
89:     )
```
> إغلاق قائمة معاملات صنف البيانات OsmResponse. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:89]

```
90: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:90]

```
91:     private data class OsmAddress(
```
> يُعرّف صنف بيانات خاص اسمه OsmAddress ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:91]

```
92:         val country: String?,
```
> يُعرّف خاصية ثابتة اسمها country من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:92]

```
93:         val state: String?,
```
> يُعرّف خاصية ثابتة اسمها state من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:93]

```
94:         val county: String?,
```
> يُعرّف خاصية ثابتة اسمها county من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:94]

```
95:         val city: String?,
```
> يُعرّف خاصية ثابتة اسمها city من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:95]

```
96:         val town: String?,
```
> يُعرّف خاصية ثابتة اسمها town من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:96]

```
97:         val village: String?,
```
> يُعرّف خاصية ثابتة اسمها village من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:97]

```
98:         val hamlet: String?,
```
> يُعرّف خاصية ثابتة اسمها hamlet من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:98]

```
99:         val suburb: String?,
```
> يُعرّف خاصية ثابتة اسمها suburb من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:99]

```
100:         val neighbourhood: String?,
```
> يُعرّف خاصية ثابتة اسمها neighbourhood من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:100]

```
101:         val residential: String?,
```
> يُعرّف خاصية ثابتة اسمها residential من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:101]

```
102:         val quarter: String?,
```
> يُعرّف خاصية ثابتة اسمها quarter من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:102]

```
103:         val postcode: String?,
```
> يُعرّف خاصية ثابتة اسمها postcode من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:103]

```
104:         val road: String?
```
> يُعرّف خاصية ثابتة اسمها road من نوع String قابل لـ null. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:104]

```
105:     )
```
> إغلاق قائمة معاملات صنف البيانات OsmAddress. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:105]

```
106: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/OpenStreetMapGeocoderProvider.kt:106]
