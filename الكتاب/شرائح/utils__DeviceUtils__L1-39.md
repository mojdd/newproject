# شريحة — app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt (الأسطر 1–39)

```
1: package com.bitchat.android.utils
```
> يُعلِن هذا السطر أن الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.utils`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من حزمة أندرويد `android.content`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:3]

```
4: import android.content.res.Configuration
```
> يستورد الصنف `Configuration` من حزمة `android.content.res`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:4]

```
5: import android.util.DisplayMetrics
```
> يستورد الصنف `DisplayMetrics` من حزمة `android.util`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:5]

```
6: import android.view.WindowManager
```
> يستورد الصنف `WindowManager` من حزمة `android.view`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:6]

```
7: import androidx.core.content.getSystemService
```
> يستورد الدالة الموسِّعة `getSystemService` من حزمة `androidx.core.content`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:7]

```
8: import kotlin.math.sqrt
```
> يستورد الدالة `sqrt` (الجذر التربيعي) من حزمة `kotlin.math`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:9]

```
10: object DeviceUtils {
```
> يُعرِّف كائناً مفرداً (object) باسم `DeviceUtils` (أدوات الجهاز) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:11]

```
12:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:12]

```
13:      * Determines if the current device is a tablet based on screen size and density.
```
> تعليق: «يحدّد ما إذا كان الجهاز الحالي لوحياً بناءً على حجم الشاشة وكثافتها». [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:13]

```
14:      * Uses multiple criteria to accurately detect tablets vs phones.
```
> تعليق: «يستعمل معايير متعددة لتمييز اللوحيات عن الهواتف بدقّة». [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:14]

```
15:      */
```
> تعليق: نهاية كتلة التوثيق (KDoc). [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:15]

```
16:     fun isTablet(context: Context): Boolean {
```
> يُعرِّف دالة (fun) باسم `isTablet` (هل لوحي) تأخذ مُعامِلاً `context` من نوع `Context` وتُعيد قيمة منطقية `Boolean`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:16]

```
17:         val windowManager = context.getSystemService<WindowManager>()
```
> يُعرِّف متغيّراً ثابتاً `windowManager` (مدير النافذة) ويُسنِد إليه ناتج استدعاء `getSystemService` بنوع `WindowManager` على `context`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:17]

```
18:         val displayMetrics = DisplayMetrics()
```
> يُعرِّف متغيّراً ثابتاً `displayMetrics` (مقاييس العرض) ويُسنِد إليه نسخة جديدة من `DisplayMetrics`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:18]

```
19:         windowManager?.defaultDisplay?.getMetrics(displayMetrics)
```
> يستدعي `getMetrics` على `defaultDisplay` لِـ `windowManager` مع تمرير `displayMetrics`، باستعمال الاستدعاء الآمن `?.` على `windowManager` و `defaultDisplay`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:19]

```
20: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:20]

```
21:         // Calculate screen size in inches
```
> تعليق: «احسب حجم الشاشة بالبوصة». [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:21]

```
22:         val widthInches = displayMetrics.widthPixels / displayMetrics.xdpi
```
> يُعرِّف متغيّراً ثابتاً `widthInches` (العرض بالبوصة) ويُسنِد إليه ناتج قسمة `widthPixels` على `xdpi` من `displayMetrics`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:22]

```
23:         val heightInches = displayMetrics.heightPixels / displayMetrics.ydpi
```
> يُعرِّف متغيّراً ثابتاً `heightInches` (الارتفاع بالبوصة) ويُسنِد إليه ناتج قسمة `heightPixels` على `ydpi` من `displayMetrics`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:23]

```
24:         val diagonalInches = sqrt((widthInches * widthInches) + (heightInches * heightInches))
```
> يُعرِّف متغيّراً ثابتاً `diagonalInches` (القطر بالبوصة) ويُسنِد إليه ناتج `sqrt` لمجموع مربّع `widthInches` ومربّع `heightInches`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:25]

```
26:         // Check if device has tablet configuration
```
> تعليق: «تحقّق ما إذا كان للجهاز إعداد لوحي». [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:26]

```
27:         val configuration = context.resources.configuration
```
> يُعرِّف متغيّراً ثابتاً `configuration` (الإعداد) ويُسنِد إليه `configuration` المأخوذ من `resources` لِـ `context`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:27]

```
28:         val isLargeScreen = (configuration.screenLayout and Configuration.SCREENLAYOUT_SIZE_MASK) >= Configuration.SCREENLAYOUT_SIZE_LARGE
```
> يُعرِّف متغيّراً ثابتاً `isLargeScreen` (شاشة كبيرة) ويُسنِد إليه ناتج المقارنة: نتيجة عملية «و» الثنائية (`and`) بين `screenLayout` و `SCREENLAYOUT_SIZE_MASK` تكون أكبر من أو تساوي `SCREENLAYOUT_SIZE_LARGE`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:28]

```
29:         val isXLargeScreen = (configuration.screenLayout and Configuration.SCREENLAYOUT_SIZE_MASK) == Configuration.SCREENLAYOUT_SIZE_XLARGE
```
> يُعرِّف متغيّراً ثابتاً `isXLargeScreen` (شاشة كبيرة جداً) ويُسنِد إليه ناتج المقارنة: نتيجة عملية «و» الثنائية (`and`) بين `screenLayout` و `SCREENLAYOUT_SIZE_MASK` تساوي `SCREENLAYOUT_SIZE_XLARGE`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:29]

```
30: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:30]

```
31:         // A device is considered a tablet if:
```
> تعليق: «يُعدّ الجهاز لوحياً إذا:». [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:31]

```
32:         // 1. Screen diagonal is 7 inches or larger, OR
```
> تعليق: «١. قطر الشاشة سبع بوصات أو أكثر، أو». [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:32]

```
33:         // 2. Configuration indicates large or xlarge screen, OR
```
> تعليق: «٢. الإعداد يشير إلى شاشة كبيرة أو كبيرة جداً، أو». [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:33]

```
34:         // 3. Smallest width is 600dp or more (sw600dp)
```
> تعليق: «٣. أصغر عرض هو ٦٠٠ وحدة كثافة مستقلة أو أكثر (sw600dp)». [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:34]

```
35:         val smallestWidthDp = context.resources.configuration.smallestScreenWidthDp
```
> يُعرِّف متغيّراً ثابتاً `smallestWidthDp` (أصغر عرض بوحدة dp) ويُسنِد إليه `smallestScreenWidthDp` المأخوذ من `configuration` ضمن `resources` لِـ `context`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:36]

```
37:         return diagonalInches >= 7.0 || isLargeScreen || isXLargeScreen || smallestWidthDp >= 600
```
> يُعيد (return) ناتج العملية المنطقية «أو» (`||`) بين أربعة شروط: `diagonalInches` أكبر من أو يساوي 7.0، أو `isLargeScreen`، أو `isXLargeScreen`، أو `smallestWidthDp` أكبر من أو يساوي 600. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:37]

```
38:     }
```
> إغلاق نطاق الدالة `isTablet`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:38]

```
39: }
```
> إغلاق نطاق الكائن المفرد `DeviceUtils`. [app/src/main/java/com/bitchat/android/utils/DeviceUtils.kt:39]
