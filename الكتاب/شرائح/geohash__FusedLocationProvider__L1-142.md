# شريحة — app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt (الأسطر 1–142)

```
1: package com.bitchat.android.geohash
```
> يعرّف الحزمة (package) التي ينتمي إليها هذا الملف باسم `com.bitchat.android.geohash`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:2]

```
3: import android.Manifest
```
> يستورد (import) الصنف `android.Manifest`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:3]

```
4: import android.annotation.SuppressLint
```
> يستورد الوسم `android.annotation.SuppressLint` (كاتم التحذير). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:4]

```
5: import android.content.Context
```
> يستورد الصنف `android.content.Context` (السياق). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:5]

```
6: import android.content.pm.PackageManager
```
> يستورد الصنف `android.content.pm.PackageManager` (مدير الحزم). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:6]

```
7: import android.location.Location
```
> يستورد الصنف `android.location.Location` (الموقع). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:7]

```
8: import android.os.Looper
```
> يستورد الصنف `android.os.Looper` (حلقة الرسائل). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:8]

```
9: import android.util.Log
```
> يستورد الصنف `android.util.Log` (السجل). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:9]

```
10: import androidx.core.app.ActivityCompat
```
> يستورد الصنف `androidx.core.app.ActivityCompat`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:10]

```
11: import com.google.android.gms.location.*
```
> يستورد كل الأصناف ضمن الحزمة `com.google.android.gms.location` باستخدام علامة النجمة. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:11]

```
12: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:12]

```
13: class FusedLocationProvider(private val context: Context) : LocationProvider {
```
> يعرّف الصنف `FusedLocationProvider` (مزوّد الموقع المدمج) بوسيط مُنشئ خاص للقراءة فقط اسمه `context` من نوع `Context`، ويُحقّق الواجهة `LocationProvider`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:13]

```
14: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:14]

```
15:     companion object {
```
> يبدأ كائن المرافقة (companion object) للصنف. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:15]

```
16:         private const val TAG = "FusedLocationProvider"
```
> يعرّف ثابتاً خاصاً اسمه `TAG` (الوسم) بقيمة نصية `"FusedLocationProvider"`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:16]

```
17:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:17]

```
18: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:18]

```
19:     private val fusedLocationClient: FusedLocationProviderClient = LocationServices.getFusedLocationProviderClient(context)
```
> يعرّف خاصية خاصة للقراءة فقط اسمها `fusedLocationClient` (عميل الموقع المدمج) من نوع `FusedLocationProviderClient`، ويضبط قيمتها بنتيجة استدعاء `LocationServices.getFusedLocationProviderClient(context)`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:19]

```
20:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:20]

```
21:     // Map to keep track of callbacks to remove them later
```
> تعليق: خريطة لتتبّع دوال الاستدعاء الراجعة لإزالتها لاحقاً. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:21]

```
22:     private val activeCallbacks = mutableMapOf<(Location) -> Unit, LocationCallback>()
```
> يعرّف خاصية خاصة للقراءة فقط اسمها `activeCallbacks` (دوال الاستدعاء النشطة)، ويضبط قيمتها بخريطة قابلة للتعديل مفاتيحها دوال من نوع `(Location) -> Unit` وقيمها من نوع `LocationCallback`، فارغة عند الإنشاء. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:22]

```
23: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:23]

```
24:     private fun hasLocationPermission(): Boolean {
```
> يعرّف دالة خاصة اسمها `hasLocationPermission` (هل يملك إذن الموقع) بلا وسائط تُعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:24]

```
25:         return ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED ||
```
> يُعيد نتيجة مقارنة استدعاء `ActivityCompat.checkSelfPermission` بالسياق وبإذن `ACCESS_FINE_LOCATION` (الموقع الدقيق) مع `PackageManager.PERMISSION_GRANTED` (الإذن ممنوح)، مربوطة بعامل «أو» المنطقي مع السطر التالي. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:25]

```
26:                 ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED
```
> يُكمل التعبير بمقارنة استدعاء `ActivityCompat.checkSelfPermission` بالسياق وبإذن `ACCESS_COARSE_LOCATION` (الموقع التقريبي) مع `PackageManager.PERMISSION_GRANTED`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:26]

```
27:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:28]

```
29:     @SuppressLint("MissingPermission")
```
> يضع الوسم `@SuppressLint` بقيمة `"MissingPermission"` (كتم تحذير الإذن المفقود). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:29]

```
30:     override fun getLastKnownLocation(callback: (Location?) -> Unit) {
```
> يتجاوز (override) ويعرّف دالة اسمها `getLastKnownLocation` (احصل على آخر موقع معروف) بوسيط اسمه `callback` من نوع دالة `(Location?) -> Unit`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:30]

```
31:         if (!hasLocationPermission()) {
```
> شرط: إذا كانت نتيجة `hasLocationPermission()` غير صحيحة (لا يوجد إذن). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:31]

```
32:             callback(null)
```
> يستدعي `callback` ممرّراً القيمة `null`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:32]

```
33:             return
```
> يُعيد التنفيذ ويخرج من الدالة. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:33]

```
34:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:34]

```
35: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:35]

```
36:         try {
```
> يبدأ كتلة `try` (محاولة). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:36]

```
37:             fusedLocationClient.lastLocation
```
> يصل إلى الخاصية `lastLocation` (آخر موقع) من `fusedLocationClient`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:37]

```
38:                 .addOnSuccessListener { location ->
```
> يضيف مستمع نجاح `addOnSuccessListener` بلامبدا وسيطها `location`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:38]

```
39:                     callback(location)
```
> يستدعي `callback` ممرّراً `location`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:39]

```
40:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:40]

```
41:                 .addOnFailureListener { e ->
```
> يضيف مستمع فشل `addOnFailureListener` بلامبدا وسيطها `e` (الاستثناء). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:41]

```
42:                     Log.e(TAG, "Error getting last known fused location: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` وبرسالة نصية `"Error getting last known fused location: "` مُلحقاً بها `e.message` (رسالة الاستثناء). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:42]

```
43:                     callback(null)
```
> يستدعي `callback` ممرّراً القيمة `null`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:43]

```
44:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:44]

```
45:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً اسمه `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:45]

```
46:             Log.e(TAG, "Exception getting last known fused location: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` وبرسالة نصية `"Exception getting last known fused location: "` مُلحقاً بها `e.message`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:46]

```
47:             callback(null)
```
> يستدعي `callback` ممرّراً القيمة `null`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:47]

```
48:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:48]

```
49:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:49]

```
50: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:50]

```
51:     @SuppressLint("MissingPermission")
```
> يضع الوسم `@SuppressLint` بقيمة `"MissingPermission"`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:51]

```
52:     override fun requestFreshLocation(callback: (Location?) -> Unit) {
```
> يتجاوز ويعرّف دالة اسمها `requestFreshLocation` (اطلب موقعاً جديداً) بوسيط اسمه `callback` من نوع دالة `(Location?) -> Unit`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:52]

```
53:         if (!hasLocationPermission()) {
```
> شرط: إذا كانت نتيجة `hasLocationPermission()` غير صحيحة. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:53]

```
54:             callback(null)
```
> يستدعي `callback` ممرّراً القيمة `null`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:54]

```
55:             return
```
> يُعيد التنفيذ ويخرج من الدالة. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:55]

```
56:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:56]

```
57: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:57]

```
58:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:58]

```
59:             val request = CurrentLocationRequest.Builder()
```
> يعرّف متغيراً للقراءة فقط اسمه `request` (الطلب)، ويبدأ بناءه بإنشاء `CurrentLocationRequest.Builder()` (باني طلب الموقع الحالي). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:59]

```
60:                 .setPriority(Priority.PRIORITY_HIGH_ACCURACY)
```
> يستدعي `setPriority` ضابطاً الأولوية بقيمة `Priority.PRIORITY_HIGH_ACCURACY` (الدقة العالية). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:60]

```
61:                 .setDurationMillis(30000)
```
> يستدعي `setDurationMillis` ضابطاً المدة بقيمة `30000` ميلّي ثانية. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:61]

```
62:                 .build()
```
> يستدعي `build()` لإنشاء كائن الطلب النهائي. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:62]

```
63: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:63]

```
64:             fusedLocationClient.getCurrentLocation(request, null)
```
> يستدعي `getCurrentLocation` على `fusedLocationClient` ممرّراً `request` والقيمة `null`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:64]

```
65:                 .addOnSuccessListener { location ->
```
> يضيف مستمع نجاح `addOnSuccessListener` بلامبدا وسيطها `location`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:65]

```
66:                     callback(location)
```
> يستدعي `callback` ممرّراً `location`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:66]

```
67:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:67]

```
68:                 .addOnFailureListener { e ->
```
> يضيف مستمع فشل `addOnFailureListener` بلامبدا وسيطها `e`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:68]

```
69:                     Log.e(TAG, "Error getting fresh fused location: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` وبرسالة نصية `"Error getting fresh fused location: "` مُلحقاً بها `e.message`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:69]

```
70:                     callback(null)
```
> يستدعي `callback` ممرّراً القيمة `null`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:70]

```
71:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:71]

```
72:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً اسمه `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:72]

```
73:             Log.e(TAG, "Exception getting fresh fused location: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` وبرسالة نصية `"Exception getting fresh fused location: "` مُلحقاً بها `e.message`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:73]

```
74:             callback(null)
```
> يستدعي `callback` ممرّراً القيمة `null`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:74]

```
75:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:75]

```
76:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:76]

```
77: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:77]

```
78:     @SuppressLint("MissingPermission")
```
> يضع الوسم `@SuppressLint` بقيمة `"MissingPermission"`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:78]

```
79:     override fun requestLocationUpdates(
```
> يتجاوز ويبدأ تعريف دالة اسمها `requestLocationUpdates` (اطلب تحديثات الموقع) بقائمة وسائط على أسطر تالية. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:79]

```
80:         intervalMs: Long,
```
> يعرّف الوسيط `intervalMs` (الفترة بالميلّي ثانية) من نوع `Long`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:80]

```
81:         minDistanceMeters: Float,
```
> يعرّف الوسيط `minDistanceMeters` (أدنى مسافة بالأمتار) من نوع `Float`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:81]

```
82:         callback: (Location) -> Unit
```
> يعرّف الوسيط `callback` من نوع دالة `(Location) -> Unit`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:82]

```
83:     ) {
```
> يغلق قائمة الوسائط ويبدأ جسم الدالة. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:83]

```
84:         if (!hasLocationPermission()) return
```
> شرط: إذا كانت نتيجة `hasLocationPermission()` غير صحيحة فيُعيد التنفيذ ويخرج من الدالة. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:84]

```
85: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:85]

```
86:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:86]

```
87:             val request = LocationRequest.Builder(intervalMs)
```
> يعرّف متغيراً للقراءة فقط اسمه `request`، ويبدأ بناءه بإنشاء `LocationRequest.Builder(intervalMs)` (باني طلب الموقع) ممرّراً `intervalMs`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:87]

```
88:                 .setMinUpdateDistanceMeters(minDistanceMeters)
```
> يستدعي `setMinUpdateDistanceMeters` ممرّراً `minDistanceMeters` (أدنى مسافة تحديث بالأمتار). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:88]

```
89:                 .setPriority(Priority.PRIORITY_HIGH_ACCURACY)
```
> يستدعي `setPriority` ضابطاً الأولوية بقيمة `Priority.PRIORITY_HIGH_ACCURACY`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:89]

```
90:                 .build()
```
> يستدعي `build()` لإنشاء كائن الطلب النهائي. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:90]

```
91: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:91]

```
92:             val locationCallback = object : LocationCallback() {
```
> يعرّف متغيراً للقراءة فقط اسمه `locationCallback` (دالة استدعاء الموقع) كائناً مجهولاً يرث `LocationCallback()`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:92]

```
93:                 override fun onLocationResult(result: LocationResult) {
```
> يتجاوز ويعرّف دالة اسمها `onLocationResult` (عند نتيجة الموقع) بوسيط اسمه `result` من نوع `LocationResult`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:93]

```
94:                     result.lastLocation?.let { callback(it) }
```
> إن لم يكن `result.lastLocation` فارغاً فيستدعي `callback` ممرّراً إياه `it` عبر `let`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:94]

```
95:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:95]

```
96:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:96]

```
97: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:97]

```
98:             synchronized(activeCallbacks) {
```
> يبدأ كتلة `synchronized` (متزامنة) مقفلة على الكائن `activeCallbacks`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:98]

```
99:                 activeCallbacks[callback] = locationCallback
```
> يضبط مدخلاً في الخريطة `activeCallbacks` مفتاحه `callback` وقيمته `locationCallback`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:99]

```
100:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:100]

```
101: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:101]

```
102:             fusedLocationClient.requestLocationUpdates(
```
> يبدأ استدعاء `requestLocationUpdates` على `fusedLocationClient` بوسائط على أسطر تالية. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:102]

```
103:                 request,
```
> يمرّر الوسيط `request`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:103]

```
104:                 locationCallback,
```
> يمرّر الوسيط `locationCallback`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:104]

```
105:                 Looper.getMainLooper()
```
> يمرّر نتيجة `Looper.getMainLooper()` (حلقة الرسائل الرئيسة) كوسيط. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:105]

```
106:             )
```
> يغلق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:106]

```
107:             Log.d(TAG, "Registered fused updates")
```
> يستدعي `Log.d` بالوسم `TAG` وبرسالة نصية `"Registered fused updates"`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:107]

```
108: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:108]

```
109:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً اسمه `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:109]

```
110:             Log.e(TAG, "Error requesting fused updates: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` وبرسالة نصية `"Error requesting fused updates: "` مُلحقاً بها `e.message`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:110]

```
111:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:111]

```
112:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:112]

```
113: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:113]

```
114:     override fun removeLocationUpdates(callback: (Location) -> Unit) {
```
> يتجاوز ويعرّف دالة اسمها `removeLocationUpdates` (أزِل تحديثات الموقع) بوسيط اسمه `callback` من نوع دالة `(Location) -> Unit`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:114]

```
115:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:115]

```
116:             val locationCallback = synchronized(activeCallbacks) {
```
> يعرّف متغيراً للقراءة فقط اسمه `locationCallback` ويضبط قيمته بنتيجة كتلة `synchronized` المقفلة على `activeCallbacks`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:116]

```
117:                 activeCallbacks.remove(callback)
```
> يستدعي `remove` على `activeCallbacks` ممرّراً `callback`، وتكون قيمته المُزالة نتيجة الكتلة. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:117]

```
118:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:118]

```
119: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:119]

```
120:             if (locationCallback != null) {
```
> شرط: إذا كان `locationCallback` لا يساوي `null`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:120]

```
121:                 fusedLocationClient.removeLocationUpdates(locationCallback)
```
> يستدعي `removeLocationUpdates` على `fusedLocationClient` ممرّراً `locationCallback`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:121]

```
122:                 Log.d(TAG, "Removed fused updates")
```
> يستدعي `Log.d` بالوسم `TAG` وبرسالة نصية `"Removed fused updates"`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:122]

```
123:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:123]

```
124:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً اسمه `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:124]

```
125:             Log.e(TAG, "Error removing fused updates: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` وبرسالة نصية `"Error removing fused updates: "` مُلحقاً بها `e.message`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:125]

```
126:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:126]

```
127:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:127]

```
128: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:128]

```
129:     override fun cancel() {
```
> يتجاوز ويعرّف دالة اسمها `cancel` (ألغِ) بلا وسائط. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:129]

```
130:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:130]

```
131:             synchronized(activeCallbacks) {
```
> يبدأ كتلة `synchronized` مقفلة على `activeCallbacks`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:131]

```
132:                 for ((callback, locationCallback) in activeCallbacks) {
```
> يبدأ حلقة `for` تكرّر مداخل `activeCallbacks` مفكِّكاً كل مدخل إلى `callback` و`locationCallback`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:132]

```
133:                     fusedLocationClient.removeLocationUpdates(locationCallback)
```
> يستدعي `removeLocationUpdates` على `fusedLocationClient` ممرّراً `locationCallback`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:133]

```
134:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:134]

```
135:                 activeCallbacks.clear()
```
> يستدعي `clear()` على `activeCallbacks` لتفريغ الخريطة. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:135]

```
136:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:136]

```
137:             Log.d(TAG, "Cancelled all fused updates")
```
> يستدعي `Log.d` بالوسم `TAG` وبرسالة نصية `"Cancelled all fused updates"`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:137]

```
138:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً اسمه `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:138]

```
139:             Log.e(TAG, "Error cancelling fused provider: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` وبرسالة نصية `"Error cancelling fused provider: "` مُلحقاً بها `e.message`. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:139]

```
140:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:140]

```
141:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:141]

```
142: }
```
> إغلاق نطاق (نهاية الصنف). [app/src/main/java/com/bitchat/android/geohash/FusedLocationProvider.kt:142]
