# شريحة — app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt (الأسطر 1–40)

```
1: package com.bitchat.android.geohash
```
> يُعرِّف هذا السطر الحزمة (package) باسم `com.bitchat.android.geohash` التي ينتمي إليها الملف. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:2]

```
3: import android.location.Location
```
> يستورد (import) الصنف `Location` من حزمة `android.location`. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:4]

```
5: /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:5]

```
6:  * Abstraction for location providers to support both
```
> تعليق: تجريد لمزوّدي الموقع لدعم كلٍّ من. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:6]

```
7:  * System (LocationManager) and Google Play Services (FusedLocationProvider).
```
> تعليق: النظام (LocationManager) وخدمات Google Play (FusedLocationProvider). [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:7]

```
8:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:8]

```
9: interface LocationProvider {
```
> يُعرِّف واجهة (interface) باسم `LocationProvider` (مزوِّد الموقع) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:9]

```
10:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:10]

```
11:      * Get the last known location from cache.
```
> تعليق: احصل على آخر موقع معروف من الذاكرة المؤقتة (cache). [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:11]

```
12:      * @param callback Called with the location or null if not found/error.
```
> تعليق: المعامل `callback` يُستدعى بالموقع أو بقيمة فارغة (null) إذا لم يُعثر عليه/حدث خطأ. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:12]

```
13:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:13]

```
14:     fun getLastKnownLocation(callback: (Location?) -> Unit)
```
> يُعلِن دالة (fun) باسم `getLastKnownLocation` تأخذ معاملاً `callback` من نوع دالة تستقبل `Location?` (موقعاً قد يكون فارغاً) وتُعيد `Unit`، دون جسم. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:14]

```
15: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:15]

```
16:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:16]

```
17:      * Request a single, fresh location update.
```
> تعليق: اطلب تحديث موقع واحداً وطازجاً. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:17]

```
18:      * @param callback Called with the location or null if failed.
```
> تعليق: المعامل `callback` يُستدعى بالموقع أو بقيمة فارغة (null) إذا فشل. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:18]

```
19:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:19]

```
20:     fun requestFreshLocation(callback: (Location?) -> Unit)
```
> يُعلِن دالة باسم `requestFreshLocation` تأخذ معاملاً `callback` من نوع دالة تستقبل `Location?` وتُعيد `Unit`، دون جسم. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:20]

```
21: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:21]

```
22:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:22]

```
23:      * Request continuous location updates.
```
> تعليق: اطلب تحديثات موقع مستمرة. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:23]

```
24:      * @param intervalMs Desired interval in milliseconds.
```
> تعليق: المعامل `intervalMs` هو الفترة المرغوبة بالميلي ثانية. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:24]

```
25:      * @param minDistanceMeters Minimum distance in meters.
```
> تعليق: المعامل `minDistanceMeters` هو أدنى مسافة بالأمتار. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:25]

```
26:      * @param callback Called when location updates.
```
> تعليق: المعامل `callback` يُستدعى عند تحديث الموقع. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:26]

```
27:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:27]

```
28:     fun requestLocationUpdates(intervalMs: Long, minDistanceMeters: Float, callback: (Location) -> Unit)
```
> يُعلِن دالة باسم `requestLocationUpdates` تأخذ `intervalMs` من نوع `Long` و`minDistanceMeters` من نوع `Float` و`callback` من نوع دالة تستقبل `Location` وتُعيد `Unit`، دون جسم. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:28]

```
29: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:29]

```
30:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:30]

```
31:      * Stop location updates.
```
> تعليق: أوقِف تحديثات الموقع. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:31]

```
32:      * @param callback The same callback instance passed to requestLocationUpdates.
```
> تعليق: المعامل `callback` هو نفس نسخة الـ callback المُمرَّرة إلى `requestLocationUpdates`. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:32]

```
33:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:33]

```
34:     fun removeLocationUpdates(callback: (Location) -> Unit)
```
> يُعلِن دالة باسم `removeLocationUpdates` تأخذ معاملاً `callback` من نوع دالة تستقبل `Location` وتُعيد `Unit`، دون جسم. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:34]

```
35: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:35]

```
36:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:36]

```
37:      * Cancel any pending one-shot location requests and cleanup resources.
```
> تعليق: ألغِ أي طلبات موقع لمرة واحدة معلّقة ونظّف الموارد. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:37]

```
38:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:38]

```
39:     fun cancel()
```
> يُعلِن دالة باسم `cancel` دون معاملات ودون جسم. [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:39]

```
40: }
```
> إغلاق نطاق (نهاية الواجهة `LocationProvider`). [app/src/main/java/com/bitchat/android/geohash/LocationProvider.kt:40]
