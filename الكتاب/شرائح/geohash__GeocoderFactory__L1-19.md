# شريحة — app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt (الأسطر 1–19)

```
1: package com.bitchat.android.geohash
```
> يُعرِّف هذا السطر اسم الحزمة (package) ويضبطه على القيمة `com.bitchat.android.geohash`. [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من المسار `android.content`. [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:3]

```
4: import android.location.Geocoder
```
> يستورد (import) الصنف `Geocoder` من المسار `android.location`. [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:5]

```
6: /**
```
> تعليق: بداية كتلة توثيق (تعليق توثيقي مفتوح بالرمز `/**`). [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:6]

```
7:  * Factory to provide the best available geocoder.
```
> تعليق: «مصنع لتوفير أفضل مُرمِّز جغرافي متاح». [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:7]

```
8:  */
```
> تعليق: نهاية كتلة التوثيق (تُغلَق بالرمز `*/`). [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:8]

```
9: object GeocoderFactory {
```
> يُعرِّف كائناً مفرداً (object) باسم `GeocoderFactory` (مصنع المُرمِّز الجغرافي) ويفتح نطاق جسمه. [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:9]

```
10:     fun get(context: Context): GeocoderProvider {
```
> يُعرِّف دالة (fun) باسم `get` تأخذ وسيطاً باسم `context` من النوع `Context` وتُعيد قيمة من النوع `GeocoderProvider` (مزوِّد المُرمِّز الجغرافي)، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:10]

```
11:         // If Google Play Services Geocoder is present, use it.
```
> تعليق: «إذا كان مُرمِّز Google Play Services موجوداً، فاستعمله». [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:11]

```
12:         // Otherwise, fall back to OpenStreetMap.
```
> تعليق: «وإلا، فارجع احتياطياً إلى OpenStreetMap». [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:12]

```
13:         return if (Geocoder.isPresent()) {
```
> يُعيد (return) نتيجة تعبير شرطي `if` يَفحص شرطه باستدعاء الدالة `Geocoder.isPresent()`، ويفتح نطاق فرع الصواب. [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:13]

```
14:             AndroidGeocoderProvider(context)
```
> يُنشئ نسخة من الصنف `AndroidGeocoderProvider` (مزوِّد مُرمِّز أندرويد) ممرِّراً إليه الوسيط `context`، وهي قيمة فرع الصواب. [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:14]

```
15:         } else {
```
> يُغلق نطاق فرع الصواب ويفتح فرع `else` (فرع الخطأ). [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:15]

```
16:             OpenStreetMapGeocoderProvider()
```
> يُنشئ نسخة من الصنف `OpenStreetMapGeocoderProvider` (مزوِّد مُرمِّز OpenStreetMap) بدون وسائط، وهي قيمة فرع الخطأ. [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:16]

```
17:         }
```
> إغلاق نطاق (إغلاق فرع `else` ومعه نطاق التعبير الشرطي). [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:17]

```
18:     }
```
> إغلاق نطاق (إغلاق جسم الدالة `get`). [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:18]

```
19: }
```
> إغلاق نطاق (إغلاق جسم الكائن `GeocoderFactory`). [app/src/main/java/com/bitchat/android/geohash/GeocoderFactory.kt:19]
