# شريحة — app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt (الأسطر 1–13)

```
1: package com.bitchat.android.geohash
```
> هذا السطر يُعرّف الحزمة (package) التي ينتمي إليها الملف، وهي com.bitchat.android.geohash. [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:2]

```
3: import android.location.Address
```
> هذا السطر يستورد (import) الصنف Address من حزمة android.location. [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:4]

```
5: /**
```
> تعليق: بداية كتلة تعليق توثيقي (يبدأ بـ /**). [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:5]

```
6:  * Interface for reverse geocoding providers.
```
> تعليق: واجهة لمزوّدي الترميز الجغرافي العكسي (reverse geocoding). [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:6]

```
7:  */
```
> تعليق: نهاية كتلة التعليق التوثيقي (تنتهي بـ */). [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:7]

```
8: interface GeocoderProvider {
```
> هذا السطر يُعرّف واجهة (interface) باسم GeocoderProvider ويفتح نطاقها. [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:8]

```
9:     /**
```
> تعليق: بداية كتلة تعليق توثيقي (يبدأ بـ /**). [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:9]

```
10:      * Get a list of Address objects from latitude and longitude.
```
> تعليق: احصل على قائمة من كائنات Address انطلاقاً من خط العرض (latitude) وخط الطول (longitude). [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:10]

```
11:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي (تنتهي بـ */). [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:11]

```
12:     suspend fun getFromLocation(latitude: Double, longitude: Double, maxResults: Int): List<Address>
```
> هذا السطر يُعرّف دالة معلّقة (suspend fun) باسم getFromLocation تأخذ ثلاثة معطيات: latitude من نوع Double، وlongitude من نوع Double، وmaxResults من نوع Int، وتُعيد قائمة (List) من كائنات Address. [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:12]

```
13: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeocoderProvider.kt:13]
