# شريحة — app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt (الأسطر 1–52)

```
1: package com.bitchat.android.geohash
```
> يُعرِّف اسم الحزمة (package) ‏com.bitchat.android.geohash لهذا الملف. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:2]

```
3: import android.content.Context
```
> يستورد الصنف ‏Context (السياق) من حزمة ‏android.content. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:3]

```
4: import android.location.Address
```
> يستورد الصنف ‏Address (العنوان) من حزمة ‏android.location. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:4]

```
5: import android.location.Geocoder
```
> يستورد الصنف ‏Geocoder (المُرَمِّز الجغرافي) من حزمة ‏android.location. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:5]

```
6: import android.os.Build
```
> يستورد الصنف ‏Build (معلومات البناء) من حزمة ‏android.os. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:6]

```
7: import android.util.Log
```
> يستورد الصنف ‏Log (السجلّ) من حزمة ‏android.util. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:7]

```
8: import kotlinx.coroutines.suspendCancellableCoroutine
```
> يستورد الدالة ‏suspendCancellableCoroutine (روتين متعاون قابل للتعليق والإلغاء) من حزمة ‏kotlinx.coroutines. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:8]

```
9: import java.util.Locale
```
> يستورد الصنف ‏Locale (المحلّيّة) من حزمة ‏java.util. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:9]

```
10: import kotlin.coroutines.resume
```
> يستورد الدالة ‏resume (الاستئناف) من حزمة ‏kotlin.coroutines. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:10]

```
11: import kotlin.coroutines.resumeWithException
```
> يستورد الدالة ‏resumeWithException (الاستئناف باستثناء) من حزمة ‏kotlin.coroutines. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:11]

```
12: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:12]

```
13: class AndroidGeocoderProvider(context: Context) : GeocoderProvider {
```
> يُعرِّف الصنف ‏AndroidGeocoderProvider (مزوّد المُرَمِّز الجغرافي لأندرويد) الذي يأخذ مُعامِلاً بانياً ‏context من نوع ‏Context ويُحقِّق الواجهة ‏GeocoderProvider (مزوّد المُرَمِّز الجغرافي). [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:13]

```
14:     private val geocoder = Geocoder(context, Locale.getDefault())
```
> يُعرِّف خاصّيةً خاصّةً ثابتةً اسمها ‏geocoder ويُسنِد إليها كائن ‏Geocoder مُنشأً بالمُعامِلين ‏context و ‏Locale.getDefault() (المحلّيّة الافتراضية). [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:14]

```
15:     private val TAG = "AndroidGeocoderProvider"
```
> يُعرِّف خاصّيةً خاصّةً ثابتةً اسمها ‏TAG (الوسم) ويُسنِد إليها السلسلة النصّية "AndroidGeocoderProvider". [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:16]

```
17:     override suspend fun getFromLocation(latitude: Double, longitude: Double, maxResults: Int): List<Address> {
```
> يُعرِّف بإعادة تعريف (override) دالةً قابلةً للتعليق (suspend) اسمها ‏getFromLocation تأخذ المُعامِلات ‏latitude (خط العرض) من نوع ‏Double و ‏longitude (خط الطول) من نوع ‏Double و ‏maxResults (الحد الأقصى للنتائج) من نوع ‏Int وتُعيد قائمةً ‏List من ‏Address. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:17]

```
18:         return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
```
> يُعيد نتيجة جملة شرطية ‏if تختبر إن كان ‏Build.VERSION.SDK_INT (رقم مستوى واجهة النظام) أكبر من أو يساوي ‏Build.VERSION_CODES.TIRAMISU. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:18]

```
19:             suspendCancellableCoroutine { cont ->
```
> يستدعي الدالة ‏suspendCancellableCoroutine ويمرّر لها دالّةً لمدِيّةً مُعامِلها ‏cont (الاستمرارية/continuation). [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:19]

```
20:                 try {
```
> يبدأ كتلة ‏try (المحاولة). [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:20]

```
21:                     geocoder.getFromLocation(
```
> يستدعي الدالة ‏getFromLocation على الكائن ‏geocoder ويفتح قائمة وُسطائها. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:21]

```
22:                         latitude,
```
> يمرّر الوسيط ‏latitude. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:22]

```
23:                         longitude,
```
> يمرّر الوسيط ‏longitude. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:23]

```
24:                         maxResults,
```
> يمرّر الوسيط ‏maxResults. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:24]

```
25:                         object : Geocoder.GeocodeListener {
```
> يمرّر كوسيط كائناً مجهول الاسم (object) يُحقِّق الواجهة ‏Geocoder.GeocodeListener (مُستمِع الترميز الجغرافي). [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:25]

```
26:                             override fun onGeocode(addresses: MutableList<Address>) {
```
> يُعرِّف بإعادة تعريف الدالة ‏onGeocode التي تأخذ المُعامِل ‏addresses (العناوين) من نوع قائمة قابلة للتغيير ‏MutableList من ‏Address. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:26]

```
27:                                 if (cont.isActive) cont.resume(addresses)
```
> إن كانت الخاصّية ‏cont.isActive (الاستمرارية نشطة) صحيحةً يستدعي ‏cont.resume ممرِّراً ‏addresses. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:27]

```
28:                             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:28]

```
29: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:29]

```
30:                             override fun onError(errorMessage: String?) {
```
> يُعرِّف بإعادة تعريف الدالة ‏onError التي تأخذ المُعامِل ‏errorMessage (رسالة الخطأ) من نوع ‏String? القابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:30]

```
31:                                 if (cont.isActive) {
```
> يبدأ جملةً شرطية ‏if تختبر إن كانت ‏cont.isActive صحيحةً. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:31]

```
32:                                     Log.e(TAG, "Geocode error: $errorMessage")
```
> يستدعي ‏Log.e (تسجيل خطأ) ممرِّراً ‏TAG والسلسلة النصّية "Geocode error: $errorMessage" التي تُدمِج فيها قيمة ‏errorMessage. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:32]

```
33:                                     cont.resume(emptyList())
```
> يستدعي ‏cont.resume ممرِّراً ‏emptyList() (قائمة فارغة). [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:33]

```
34:                                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:34]

```
35:                             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:35]

```
36:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:36]

```
37:                     )
```
> يُغلِق قائمة وُسطاء استدعاء ‏geocoder.getFromLocation. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:37]

```
38:                 } catch (e: Exception) {
```
> يبدأ كتلة ‏catch (الالتقاط) التي تلتقط استثناءً ‏e من نوع ‏Exception. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:38]

```
39:                     if (cont.isActive) cont.resumeWithException(e)
```
> إن كانت ‏cont.isActive صحيحةً يستدعي ‏cont.resumeWithException ممرِّراً الاستثناء ‏e. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:39]

```
40:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:40]

```
41:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:41]

```
42:         } else {
```
> يبدأ الفرع البديل ‏else من جملة ‏if. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:42]

```
43:             @Suppress("DEPRECATION")
```
> يضع التعليق التوضيحي (annotation) ‏@Suppress بالوسيط "DEPRECATION" لكتم تحذير الإهمال. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:43]

```
44:             try {
```
> يبدأ كتلة ‏try. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:44]

```
45:                 geocoder.getFromLocation(latitude, longitude, maxResults) ?: emptyList()
```
> يستدعي ‏geocoder.getFromLocation بالوُسطاء ‏latitude و ‏longitude و ‏maxResults، وعند كون النتيجة فارغةً ‏null يُعيد ‏emptyList() عبر مُعامِل ‏الدمج-الفارغ (?:‎). [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:45]

```
46:             } catch (e: Exception) {
```
> يبدأ كتلة ‏catch التي تلتقط استثناءً ‏e من نوع ‏Exception. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:46]

```
47:                 Log.e(TAG, "Geocode failed", e)
```
> يستدعي ‏Log.e ممرِّراً ‏TAG والسلسلة النصّية "Geocode failed" والاستثناء ‏e. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:47]

```
48:                 emptyList()
```
> يُقَيِّم ‏emptyList() (قائمة فارغة) كقيمة ناتجة لكتلة ‏catch. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:48]

```
49:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:49]

```
50:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:50]

```
51:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:51]

```
52: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/AndroidGeocoderProvider.kt:52]
