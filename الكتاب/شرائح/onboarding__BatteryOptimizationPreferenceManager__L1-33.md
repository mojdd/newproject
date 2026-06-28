# شريحة — app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt (الأسطر 1–33)

```
1: package com.bitchat.android.onboarding
```
> يُعلِن أنّ هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.onboarding`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصِّنف `Context` من `android.content`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:3]

```
4: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد الصِّنف `MutableStateFlow` (تدفّق حالة قابل للتغيير) من `kotlinx.coroutines.flow`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:4]

```
5: import kotlinx.coroutines.flow.StateFlow
```
> يستورد الصِّنف `StateFlow` (تدفّق حالة) من `kotlinx.coroutines.flow`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:6]

```
7: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:7]

```
8:  * Preference manager for battery optimization skip choice
```
> تعليق: مدير تفضيلات لاختيار تخطّي تحسين البطارية. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:8]

```
9:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:9]

```
10: object BatteryOptimizationPreferenceManager {
```
> يُعرِّف كائناً مفرداً (object) باسم `BatteryOptimizationPreferenceManager` (مدير تفضيلات تحسين البطارية) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:10]

```
11:     private const val PREFS_NAME = "bitchat_settings"
```
> يُعرِّف ثابتاً خاصاً (private const) باسم `PREFS_NAME` وقيمته النصّية `"bitchat_settings"`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:11]

```
12:     private const val KEY_BATTERY_SKIP = "battery_optimization_skipped"
```
> يُعرِّف ثابتاً خاصاً باسم `KEY_BATTERY_SKIP` وقيمته النصّية `"battery_optimization_skipped"`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:12]

```
13: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:13]

```
14:     private val _skipFlow = MutableStateFlow(false)
```
> يُعرِّف متغيّراً خاصاً ثابت الإسناد (val) باسم `_skipFlow` ويُسنِد إليه كائن `MutableStateFlow` بقيمة ابتدائية `false`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:14]

```
15:     val skipFlow: StateFlow<Boolean> = _skipFlow
```
> يُعرِّف متغيّراً عامّاً ثابت الإسناد باسم `skipFlow` من نوع `StateFlow<Boolean>` ويُسنِد إليه `_skipFlow`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:16]

```
17:     fun init(context: Context) {
```
> يُعرِّف دالّة (fun) باسم `init` تأخذ وسيطاً باسم `context` من نوع `Context` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:17]

```
18:         val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُعرِّف متغيّراً ثابت الإسناد باسم `prefs` ويُسنِد إليه ناتج استدعاء `context.getSharedPreferences` بالوسيطين `PREFS_NAME` و`Context.MODE_PRIVATE`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:18]

```
19:         val skipped = prefs.getBoolean(KEY_BATTERY_SKIP, false)
```
> يُعرِّف متغيّراً ثابت الإسناد باسم `skipped` ويُسنِد إليه ناتج استدعاء `prefs.getBoolean` بالمفتاح `KEY_BATTERY_SKIP` والقيمة الافتراضية `false`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:19]

```
20:         _skipFlow.value = skipped
```
> يُسنِد قيمة `skipped` إلى الخاصية `value` للمتغيّر `_skipFlow`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:20]

```
21:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:21]

```
22: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:22]

```
23:     fun setSkipped(context: Context, skipped: Boolean) {
```
> يُعرِّف دالّة باسم `setSkipped` تأخذ وسيطين: `context` من نوع `Context` و`skipped` من نوع `Boolean`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:23]

```
24:         val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُعرِّف متغيّراً ثابت الإسناد باسم `prefs` ويُسنِد إليه ناتج استدعاء `context.getSharedPreferences` بالوسيطين `PREFS_NAME` و`Context.MODE_PRIVATE`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:24]

```
25:         prefs.edit().putBoolean(KEY_BATTERY_SKIP, skipped).apply()
```
> يستدعي `prefs.edit()` ثم `putBoolean` بالمفتاح `KEY_BATTERY_SKIP` والقيمة `skipped` ثم `apply()`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:25]

```
26:         _skipFlow.value = skipped
```
> يُسنِد قيمة `skipped` إلى الخاصية `value` للمتغيّر `_skipFlow`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:26]

```
27:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:28]

```
29:     fun isSkipped(context: Context): Boolean {
```
> يُعرِّف دالّة باسم `isSkipped` تأخذ وسيطاً باسم `context` من نوع `Context` وتُعيد نوع `Boolean`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:29]

```
30:         val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُعرِّف متغيّراً ثابت الإسناد باسم `prefs` ويُسنِد إليه ناتج استدعاء `context.getSharedPreferences` بالوسيطين `PREFS_NAME` و`Context.MODE_PRIVATE`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:30]

```
31:         return prefs.getBoolean(KEY_BATTERY_SKIP, false)
```
> يُعيد ناتج استدعاء `prefs.getBoolean` بالمفتاح `KEY_BATTERY_SKIP` والقيمة الافتراضية `false`. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:31]

```
32:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:32]

```
33: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationPreferenceManager.kt:33]
