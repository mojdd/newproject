# شريحة — app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt (الأسطر 1–200)

```
1: package com.bitchat.android.geohash
```
> يُعرّف اسم الحزمة (package) بأنها com.bitchat.android.geohash. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:2]

```
3: import android.Manifest
```
> يستورد الصنف android.Manifest. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:3]

```
4: import android.annotation.SuppressLint
```
> يستورد التعليق التوضيحي (annotation) كَتم تحذير لِنت (SuppressLint) من android.annotation. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:4]

```
5: import android.content.Context
```
> يستورد الصنف السياق (Context) من android.content. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:5]

```
6: import android.content.pm.PackageManager
```
> يستورد الصنف مدير الحزم (PackageManager) من android.content.pm. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:6]

```
7: import android.location.Location
```
> يستورد الصنف الموقع (Location) من android.location. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:7]

```
8: import android.location.LocationListener
```
> يستورد الصنف مُستمِع الموقع (LocationListener) من android.location. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:8]

```
9: import android.location.LocationManager
```
> يستورد الصنف مدير الموقع (LocationManager) من android.location. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:9]

```
10: import android.os.Build
```
> يستورد الصنف بِيلد (Build) من android.os. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:10]

```
11: import android.os.Bundle
```
> يستورد الصنف الحزمة (Bundle) من android.os. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:11]

```
12: import android.util.Log
```
> يستورد الصنف السجل (Log) من android.util. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:12]

```
13: import androidx.core.app.ActivityCompat
```
> يستورد الصنف متوافق النشاط (ActivityCompat) من androidx.core.app. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:13]

```
14: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:14]

```
15: class SystemLocationProvider(private val context: Context) : LocationProvider {
```
> يُعرّف الصنف مزوّد موقع النظام (SystemLocationProvider) الذي يأخذ مُعامِلاً خاصاً غير قابل للتغيير اسمه السياق (context) من النوع Context، ويُنفّذ الواجهة مزوّد الموقع (LocationProvider). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:16]

```
17:     companion object {
```
> يبدأ تعريف الكائن المرافق (companion object). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:17]

```
18:         private const val TAG = "SystemLocationProvider"
```
> يُعرّف ثابتاً خاصاً اسمه الوسم (TAG) وقيمته النص "SystemLocationProvider". [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:18]

```
19:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:19]

```
20: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:20]

```
21:     private val locationManager = context.getSystemService(Context.LOCATION_SERVICE) as LocationManager
```
> يُعرّف خاصية خاصة غير قابلة للتغيير اسمها مدير الموقع (locationManager) قيمتها ناتج استدعاء getSystemService على السياق بالوسيط Context.LOCATION_SERVICE مع تحويل النوع (as) إلى LocationManager. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:21]

```
22:     private val handler = android.os.Handler(android.os.Looper.getMainLooper())
```
> يُعرّف خاصية خاصة غير قابلة للتغيير اسمها المُعالِج (handler) قيمتها كائن Handler مُنشأ بوسيط ناتج استدعاء Looper.getMainLooper(). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:22]

```
23:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:23]

```
24:     // Map to keep track of listeners to unregister them later
```
> تعليق: خريطة لتتبّع المُستمِعين كي يُلغى تسجيلهم لاحقاً. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:24]

```
25:     private val activeListeners = mutableMapOf<(Location) -> Unit, LocationListener>()
```
> يُعرّف خاصية خاصة غير قابلة للتغيير اسمها المُستمِعون النشِطون (activeListeners) قيمتها خريطة قابلة للتغيير مفاتيحها دوال من النوع (Location) -> Unit وقيمها من النوع LocationListener. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:25]

```
26:     private val activeOneShotListeners = mutableMapOf<(Location?) -> Unit, LocationListener>()
```
> يُعرّف خاصية خاصة غير قابلة للتغيير اسمها مُستمِعو اللقطة الواحدة النشِطون (activeOneShotListeners) قيمتها خريطة قابلة للتغيير مفاتيحها دوال من النوع (Location?) -> Unit وقيمها من النوع LocationListener. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:26]

```
27:     private val activeOneShotRunnables = mutableMapOf<(Location?) -> Unit, Runnable>()
```
> يُعرّف خاصية خاصة غير قابلة للتغيير اسمها مهامّ اللقطة الواحدة النشِطة (activeOneShotRunnables) قيمتها خريطة قابلة للتغيير مفاتيحها دوال من النوع (Location?) -> Unit وقيمها من النوع Runnable. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:28]

```
29:     private fun hasLocationPermission(): Boolean {
```
> يُعرّف دالة خاصة اسمها يملك إذن الموقع (hasLocationPermission) تُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:29]

```
30:         return ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED ||
```
> يُعيد نتيجة مقارنة ناتج checkSelfPermission على ActivityCompat بالوسيطين السياق وManifest.permission.ACCESS_FINE_LOCATION مع PackageManager.PERMISSION_GRANTED، مربوطة بمُعامِل أو المنطقي (||). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:30]

```
31:                 ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED
```
> الطرف الثاني للمقارنة: ناتج checkSelfPermission على ActivityCompat بالوسيطين السياق وManifest.permission.ACCESS_COARSE_LOCATION يساوي PackageManager.PERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:31]

```
32:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:33]

```
34:     @SuppressLint("MissingPermission")
```
> يضع تعليقاً توضيحياً كَتم تحذير لِنت بقيمة "MissingPermission". [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:34]

```
35:     override fun getLastKnownLocation(callback: (Location?) -> Unit) {
```
> يُعرّف دالة مُعاد تعريفها (override) اسمها جلب آخر موقع معروف (getLastKnownLocation) تأخذ مُعامِلاً اسمه ردّ النداء (callback) من النوع (Location?) -> Unit. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:35]

```
36:         if (!hasLocationPermission()) {
```
> يبدأ شرطاً إذا كانت دالة يملك إذن الموقع تُعيد كاذباً (بالنفي !). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:36]

```
37:             callback(null)
```
> يستدعي ردّ النداء بالقيمة null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:37]

```
38:             return
```
> يُنهي الدالة بعبارة return بلا قيمة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:38]

```
39:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:39]

```
40: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:40]

```
41:         try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:41]

```
42:             var bestLocation: Location? = null
```
> يُعرّف متغيّراً قابلاً للتغيير اسمه أفضل موقع (bestLocation) من النوع Location? وقيمته الابتدائية null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:42]

```
43:             val providers = locationManager.getProviders(true)
```
> يُعرّف خاصية غير قابلة للتغيير اسمها المزوّدون (providers) قيمتها ناتج استدعاء getProviders على مدير الموقع بالوسيط true. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:43]

```
44:             for (provider in providers) {
```
> يبدأ حلقة for تمرّ على كل عنصر اسمه المزوّد (provider) في المزوّدين. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:44]

```
45:                 val location = locationManager.getLastKnownLocation(provider)
```
> يُعرّف خاصية غير قابلة للتغيير اسمها الموقع (location) قيمتها ناتج استدعاء getLastKnownLocation على مدير الموقع بالوسيط المزوّد. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:45]

```
46:                 if (location != null) {
```
> يبدأ شرطاً إذا كان الموقع لا يساوي null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:46]

```
47:                     if (bestLocation == null || location.time > bestLocation.time) {
```
> يبدأ شرطاً إذا كان أفضل موقع يساوي null أو كان زمن الموقع (location.time) أكبر من زمن أفضل موقع (bestLocation.time). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:47]

```
48:                         bestLocation = location
```
> يُسنِد الموقع إلى أفضل موقع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:48]

```
49:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:49]

```
50:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:50]

```
51:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:51]

```
52:             callback(bestLocation)
```
> يستدعي ردّ النداء بالقيمة أفضل موقع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:52]

```
53:         } catch (e: Exception) {
```
> يبدأ كتلة التقاط (catch) للاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:53]

```
54:             Log.e(TAG, "Error getting last known location: ${e.message}")
```
> يستدعي Log.e بالوسيطين الوسم والنص "Error getting last known location: " متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:54]

```
55:             callback(null)
```
> يستدعي ردّ النداء بالقيمة null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:55]

```
56:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:56]

```
57:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:57]

```
58: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:58]

```
59:     @SuppressLint("MissingPermission")
```
> يضع تعليقاً توضيحياً كَتم تحذير لِنت بقيمة "MissingPermission". [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:59]

```
60:     override fun requestFreshLocation(callback: (Location?) -> Unit) {
```
> يُعرّف دالة مُعاد تعريفها اسمها طلب موقع طازج (requestFreshLocation) تأخذ مُعامِلاً اسمه ردّ النداء من النوع (Location?) -> Unit. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:60]

```
61:         if (!hasLocationPermission()) {
```
> يبدأ شرطاً إذا كانت دالة يملك إذن الموقع تُعيد كاذباً (بالنفي !). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:61]

```
62:             callback(null)
```
> يستدعي ردّ النداء بالقيمة null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:62]

```
63:             return
```
> يُنهي الدالة بعبارة return بلا قيمة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:63]

```
64:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:65]

```
66:         try {
```
> يبدأ كتلة محاولة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:66]

```
67:             val providers = listOf(
```
> يُعرّف خاصية غير قابلة للتغيير اسمها المزوّدون قيمتها قائمة (listOf) تبدأ هنا. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:67]

```
68:                 LocationManager.GPS_PROVIDER,
```
> عنصر القائمة الأول: LocationManager.GPS_PROVIDER. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:68]

```
69:                 LocationManager.NETWORK_PROVIDER,
```
> عنصر القائمة الثاني: LocationManager.NETWORK_PROVIDER. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:69]

```
70:                 LocationManager.PASSIVE_PROVIDER
```
> عنصر القائمة الثالث: LocationManager.PASSIVE_PROVIDER. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:70]

```
71:             )
```
> إغلاق قوس استدعاء listOf. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:71]

```
72: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:72]

```
73:             var providerFound = false
```
> يُعرّف متغيّراً قابلاً للتغيير اسمه وُجِد مزوّد (providerFound) وقيمته الابتدائية false. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:73]

```
74:             for (provider in providers) {
```
> يبدأ حلقة for تمرّ على كل عنصر اسمه المزوّد في المزوّدين. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:74]

```
75:                 if (locationManager.isProviderEnabled(provider)) {
```
> يبدأ شرطاً إذا كان ناتج استدعاء isProviderEnabled على مدير الموقع بالوسيط المزوّد صحيحاً. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:75]

```
76:                     Log.d(TAG, "Requesting fresh location from $provider")
```
> يستدعي Log.d بالوسيطين الوسم والنص "Requesting fresh location from " متبوعاً بقيمة المزوّد. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:76]

```
77:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:77]

```
78:                     if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
```
> يبدأ شرطاً إذا كان Build.VERSION.SDK_INT أكبر من أو يساوي Build.VERSION_CODES.R. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:78]

```
79:                         locationManager.getCurrentLocation(
```
> يستدعي getCurrentLocation على مدير الموقع، وتبدأ وسائطه هنا. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:79]

```
80:                             provider,
```
> الوسيط الأول: المزوّد. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:80]

```
81:                             null,
```
> الوسيط الثاني: null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:81]

```
82:                             context.mainExecutor
```
> الوسيط الثالث: مُنفّذ السياق الرئيسي (context.mainExecutor). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:82]

```
83:                         ) { location ->
```
> يُغلق قوس الوسائط ويبدأ تعبير لامدا وسيطه اسمه الموقع (location). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:83]

```
84:                             callback(location)
```
> يستدعي ردّ النداء بالقيمة الموقع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:84]

```
85:                         }
```
> إغلاق نطاق لامدا. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:85]

```
86:                     } else {
```
> يُغلق فرع if ويبدأ فرع else. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:86]

```
87:                         // For older versions, use requestSingleUpdate with timeout mechanism
```
> تعليق: للإصدارات الأقدم، استخدم requestSingleUpdate مع آلية مهلة زمنية. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:87]

```
88:                         val timeoutRunnable = Runnable {
```
> يُعرّف خاصية غير قابلة للتغيير اسمها مهمّة المهلة (timeoutRunnable) قيمتها كائن Runnable يبدأ جسمه هنا. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:88]

```
89:                             Log.w(TAG, "Location request timed out")
```
> يستدعي Log.w بالوسيطين الوسم والنص "Location request timed out". [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:89]

```
90:                             synchronized(activeOneShotListeners) {
```
> يبدأ كتلة متزامنة (synchronized) قُفلها مُستمِعو اللقطة الواحدة النشِطون. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:90]

```
91:                                 val listener = activeOneShotListeners.remove(callback)
```
> يُعرّف خاصية غير قابلة للتغيير اسمها المُستمِع (listener) قيمتها ناتج إزالة المفتاح ردّ النداء من مُستمِعي اللقطة الواحدة النشِطين. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:91]

```
92:                                 activeOneShotRunnables.remove(callback)
```
> يُزيل المفتاح ردّ النداء من مهامّ اللقطة الواحدة النشِطة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:92]

```
93:                                 if (listener != null) {
```
> يبدأ شرطاً إذا كان المُستمِع لا يساوي null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:93]

```
94:                                     try {
```
> يبدأ كتلة محاولة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:94]

```
95:                                         locationManager.removeUpdates(listener)
```
> يستدعي removeUpdates على مدير الموقع بالوسيط المُستمِع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:95]

```
96:                                     } catch (e: Exception) {
```
> يبدأ كتلة التقاط للاستثناء باسم e. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:96]

```
97:                                         Log.e(TAG, "Error removing timed out listener: ${e.message}")
```
> يستدعي Log.e بالوسيطين الوسم والنص "Error removing timed out listener: " متبوعاً برسالة الاستثناء. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:97]

```
98:                                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:98]

```
99:                                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:99]

```
100:                             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:100]

```
101:                             callback(null)
```
> يستدعي ردّ النداء بالقيمة null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:101]

```
102:                         }
```
> إغلاق نطاق مهمّة المهلة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:102]

```
103: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:103]

```
104:                         val listener = object : LocationListener {
```
> يُعرّف خاصية غير قابلة للتغيير اسمها المُستمِع قيمتها كائن مجهول (object) يُنفّذ LocationListener ويبدأ جسمه هنا. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:104]

```
105:                             override fun onLocationChanged(location: Location) {
```
> يُعرّف دالة مُعاد تعريفها اسمها عند تغيّر الموقع (onLocationChanged) تأخذ مُعامِلاً اسمه الموقع من النوع Location. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:105]

```
106:                                 synchronized(activeOneShotListeners) {
```
> يبدأ كتلة متزامنة قُفلها مُستمِعو اللقطة الواحدة النشِطون. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:106]

```
107:                                     activeOneShotListeners.remove(callback)
```
> يُزيل المفتاح ردّ النداء من مُستمِعي اللقطة الواحدة النشِطين. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:107]

```
108:                                     val runnable = activeOneShotRunnables.remove(callback)
```
> يُعرّف خاصية غير قابلة للتغيير اسمها المهمّة (runnable) قيمتها ناتج إزالة المفتاح ردّ النداء من مهامّ اللقطة الواحدة النشِطة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:108]

```
109:                                     if (runnable != null) {
```
> يبدأ شرطاً إذا كانت المهمّة لا تساوي null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:109]

```
110:                                         handler.removeCallbacks(runnable)
```
> يستدعي removeCallbacks على المُعالِج بالوسيط المهمّة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:110]

```
111:                                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:111]

```
112:                                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:112]

```
113:                                 try {
```
> يبدأ كتلة محاولة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:113]

```
114:                                     locationManager.removeUpdates(this)
```
> يستدعي removeUpdates على مدير الموقع بالوسيط this (الكائن المُستمِع الحالي). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:114]

```
115:                                 } catch (e: Exception) {
```
> يبدأ كتلة التقاط للاستثناء باسم e. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:115]

```
116:                                     Log.e(TAG, "Error removing updates in callback: ${e.message}")
```
> يستدعي Log.e بالوسيطين الوسم والنص "Error removing updates in callback: " متبوعاً برسالة الاستثناء. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:116]

```
117:                                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:117]

```
118:                                 callback(location)
```
> يستدعي ردّ النداء بالقيمة الموقع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:118]

```
119:                             }
```
> إغلاق نطاق دالة عند تغيّر الموقع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:119]

```
120:                             override fun onStatusChanged(provider: String?, status: Int, extras: Bundle?) {}
```
> يُعرّف دالة مُعاد تعريفها اسمها عند تغيّر الحالة (onStatusChanged) تأخذ المزوّد من النوع String? والحالة (status) من النوع Int والإضافات (extras) من النوع Bundle? وجسمها فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:120]

```
121:                             override fun onProviderEnabled(provider: String) {}
```
> يُعرّف دالة مُعاد تعريفها اسمها عند تفعيل المزوّد (onProviderEnabled) تأخذ المزوّد من النوع String وجسمها فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:121]

```
122:                             override fun onProviderDisabled(provider: String) {}
```
> يُعرّف دالة مُعاد تعريفها اسمها عند تعطيل المزوّد (onProviderDisabled) تأخذ المزوّد من النوع String وجسمها فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:122]

```
123:                         }
```
> إغلاق نطاق الكائن المجهول المُستمِع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:123]

```
124: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:124]

```
125:                         synchronized(activeOneShotListeners) {
```
> يبدأ كتلة متزامنة قُفلها مُستمِعو اللقطة الواحدة النشِطون. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:125]

```
126:                             activeOneShotListeners[callback] = listener
```
> يُسنِد المُستمِع إلى المفتاح ردّ النداء في مُستمِعي اللقطة الواحدة النشِطين. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:126]

```
127:                             activeOneShotRunnables[callback] = timeoutRunnable
```
> يُسنِد مهمّة المهلة إلى المفتاح ردّ النداء في مهامّ اللقطة الواحدة النشِطة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:127]

```
128:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:128]

```
129:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:129]

```
130:                         locationManager.requestSingleUpdate(provider, listener, null)
```
> يستدعي requestSingleUpdate على مدير الموقع بالوسائط المزوّد والمُستمِع وnull. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:130]

```
131:                         handler.postDelayed(timeoutRunnable, 30000L) // 30s timeout
```
> يستدعي postDelayed على المُعالِج بالوسيطين مهمّة المهلة والقيمة الطويلة 30000L، مع تعليق: مهلة 30 ثانية. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:131]

```
132:                     }
```
> إغلاق نطاق فرع else. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:132]

```
133:                     providerFound = true
```
> يُسنِد القيمة true إلى وُجِد مزوّد. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:133]

```
134:                     break
```
> يُنهي حلقة for بعبارة break. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:134]

```
135:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:135]

```
136:             }
```
> إغلاق نطاق حلقة for. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:136]

```
137: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:137]

```
138:             if (!providerFound) {
```
> يبدأ شرطاً إذا كان وُجِد مزوّد كاذباً (بالنفي !). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:138]

```
139:                 Log.w(TAG, "No location providers available for fresh location")
```
> يستدعي Log.w بالوسيطين الوسم والنص "No location providers available for fresh location". [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:139]

```
140:                 callback(null)
```
> يستدعي ردّ النداء بالقيمة null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:140]

```
141:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:141]

```
142:         } catch (e: Exception) {
```
> يبدأ كتلة التقاط للاستثناء باسم e. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:142]

```
143:             Log.e(TAG, "Error requesting fresh location: ${e.message}")
```
> يستدعي Log.e بالوسيطين الوسم والنص "Error requesting fresh location: " متبوعاً برسالة الاستثناء. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:143]

```
144:             callback(null)
```
> يستدعي ردّ النداء بالقيمة null. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:144]

```
145:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:145]

```
146:     }
```
> إغلاق نطاق دالة طلب موقع طازج. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:146]

```
147: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:147]

```
148:     @SuppressLint("MissingPermission")
```
> يضع تعليقاً توضيحياً كَتم تحذير لِنت بقيمة "MissingPermission". [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:148]

```
149:     override fun requestLocationUpdates(
```
> يُعرّف دالة مُعاد تعريفها اسمها طلب تحديثات الموقع (requestLocationUpdates) وتبدأ مُعامِلاتها هنا. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:149]

```
150:         intervalMs: Long,
```
> المُعامِل الأول: الفترة بالملّي ثانية (intervalMs) من النوع Long. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:150]

```
151:         minDistanceMeters: Float,
```
> المُعامِل الثاني: أدنى مسافة بالأمتار (minDistanceMeters) من النوع Float. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:151]

```
152:         callback: (Location) -> Unit
```
> المُعامِل الثالث: ردّ النداء من النوع (Location) -> Unit. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:152]

```
153:     ) {
```
> يُغلق قوس المُعامِلات ويبدأ جسم الدالة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:153]

```
154:         if (!hasLocationPermission()) return
```
> يبدأ شرطاً إذا كانت دالة يملك إذن الموقع تُعيد كاذباً فإنه يُنهي الدالة بعبارة return. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:154]

```
155: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:155]

```
156:         try {
```
> يبدأ كتلة محاولة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:156]

```
157:             val listener = object : LocationListener {
```
> يُعرّف خاصية غير قابلة للتغيير اسمها المُستمِع قيمتها كائن مجهول يُنفّذ LocationListener ويبدأ جسمه هنا. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:157]

```
158:                 override fun onLocationChanged(location: Location) {
```
> يُعرّف دالة مُعاد تعريفها اسمها عند تغيّر الموقع تأخذ مُعامِلاً اسمه الموقع من النوع Location. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:158]

```
159:                     callback(location)
```
> يستدعي ردّ النداء بالقيمة الموقع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:159]

```
160:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:160]

```
161:                 override fun onStatusChanged(provider: String?, status: Int, extras: Bundle?) {}
```
> يُعرّف دالة مُعاد تعريفها اسمها عند تغيّر الحالة تأخذ المزوّد من النوع String? والحالة من النوع Int والإضافات من النوع Bundle? وجسمها فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:161]

```
162:                 override fun onProviderEnabled(provider: String) {}
```
> يُعرّف دالة مُعاد تعريفها اسمها عند تفعيل المزوّد تأخذ المزوّد من النوع String وجسمها فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:162]

```
163:                 override fun onProviderDisabled(provider: String) {}
```
> يُعرّف دالة مُعاد تعريفها اسمها عند تعطيل المزوّد تأخذ المزوّد من النوع String وجسمها فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:163]

```
164:             }
```
> إغلاق نطاق الكائن المجهول المُستمِع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:164]

```
165: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:165]

```
166:             // Store the listener so we can remove it later
```
> تعليق: خزّن المُستمِع كي نتمكّن من إزالته لاحقاً. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:166]

```
167:             synchronized(activeListeners) {
```
> يبدأ كتلة متزامنة قُفلها المُستمِعون النشِطون. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:167]

```
168:                 activeListeners[callback] = listener
```
> يُسنِد المُستمِع إلى المفتاح ردّ النداء في المُستمِعين النشِطين. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:168]

```
169:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:169]

```
170: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:170]

```
171:             val providers = listOf(LocationManager.GPS_PROVIDER, LocationManager.NETWORK_PROVIDER)
```
> يُعرّف خاصية غير قابلة للتغيير اسمها المزوّدون قيمتها قائمة تضمّ LocationManager.GPS_PROVIDER وLocationManager.NETWORK_PROVIDER. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:171]

```
172:             var registered = false
```
> يُعرّف متغيّراً قابلاً للتغيير اسمه مُسجَّل (registered) وقيمته الابتدائية false. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:172]

```
173:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:173]

```
174:             for (provider in providers) {
```
> يبدأ حلقة for تمرّ على كل عنصر اسمه المزوّد في المزوّدين. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:174]

```
175:                 if (locationManager.isProviderEnabled(provider)) {
```
> يبدأ شرطاً إذا كان ناتج استدعاء isProviderEnabled على مدير الموقع بالوسيط المزوّد صحيحاً. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:175]

```
176:                     locationManager.requestLocationUpdates(
```
> يستدعي requestLocationUpdates على مدير الموقع، وتبدأ وسائطه هنا. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:176]

```
177:                         provider,
```
> الوسيط الأول: المزوّد. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:177]

```
178:                         intervalMs,
```
> الوسيط الثاني: الفترة بالملّي ثانية. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:178]

```
179:                         minDistanceMeters,
```
> الوسيط الثالث: أدنى مسافة بالأمتار. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:179]

```
180:                         listener
```
> الوسيط الرابع: المُستمِع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:180]

```
181:                     )
```
> إغلاق قوس استدعاء requestLocationUpdates. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:181]

```
182:                     registered = true
```
> يُسنِد القيمة true إلى مُسجَّل. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:182]

```
183:                     Log.d(TAG, "Registered updates for $provider")
```
> يستدعي Log.d بالوسيطين الوسم والنص "Registered updates for " متبوعاً بقيمة المزوّد. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:183]

```
184:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:184]

```
185:             }
```
> إغلاق نطاق حلقة for. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:185]

```
186:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:186]

```
187:             if (!registered) {
```
> يبدأ شرطاً إذا كان مُسجَّل كاذباً (بالنفي !). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:187]

```
188:                 Log.w(TAG, "No providers enabled for continuous updates")
```
> يستدعي Log.w بالوسيطين الوسم والنص "No providers enabled for continuous updates". [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:188]

```
189:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:189]

```
190: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:190]

```
191:         } catch (e: Exception) {
```
> يبدأ كتلة التقاط للاستثناء باسم e. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:191]

```
192:             Log.e(TAG, "Error requesting location updates: ${e.message}")
```
> يستدعي Log.e بالوسيطين الوسم والنص "Error requesting location updates: " متبوعاً برسالة الاستثناء. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:192]

```
193:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:193]

```
194:     }
```
> إغلاق نطاق دالة طلب تحديثات الموقع. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:194]

```
195: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:195]

```
196:     override fun removeLocationUpdates(callback: (Location) -> Unit) {
```
> يُعرّف دالة مُعاد تعريفها اسمها إزالة تحديثات الموقع (removeLocationUpdates) تأخذ مُعامِلاً اسمه ردّ النداء من النوع (Location) -> Unit. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:196]

```
197:         try {
```
> يبدأ كتلة محاولة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:197]

```
198:             val listener = synchronized(activeListeners) {
```
> يُعرّف خاصية غير قابلة للتغيير اسمها المُستمِع قيمتها ناتج كتلة متزامنة قُفلها المُستمِعون النشِطون تبدأ هنا. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:198]

```
199:                 activeListeners.remove(callback)
```
> يُزيل المفتاح ردّ النداء من المُستمِعين النشِطين (وهو القيمة المُعادة من الكتلة المتزامنة). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:199]

```
200:             }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:200]
