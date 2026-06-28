# شريحة — app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt (الأسطر 1–21)

```
1: package com.bitchat.android.onboarding
```
> يُعلِن انتماء الملف إلى الحزمة (package) ‏`com.bitchat.android.onboarding`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف ‏`Context` من الحزمة ‏`android.content`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:4]

```
5: /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:5]

```
6:  * Preference manager for background location skip choice.
```
> تعليق: «مدير تفضيلات لاختيار تخطّي موقع الخلفية». [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:6]

```
7:  */
```
> تعليق توثيقي: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:7]

```
8: object BackgroundLocationPreferenceManager {
```
> يُعرِّف كائناً مفرداً (object) باسم ‏`BackgroundLocationPreferenceManager` (مدير تفضيلات موقع الخلفية) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:8]

```
9:     private const val PREFS_NAME = "bitchat_settings"
```
> يُعرِّف ثابتاً خاصاً (private const val) باسم ‏`PREFS_NAME` (اسم التفضيلات) ويضبط قيمته إلى السلسلة النصية ‏`"bitchat_settings"`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:9]

```
10:     private const val KEY_BACKGROUND_LOCATION_SKIP = "background_location_skipped"
```
> يُعرِّف ثابتاً خاصاً (private const val) باسم ‏`KEY_BACKGROUND_LOCATION_SKIP` (مفتاح تخطّي موقع الخلفية) ويضبط قيمته إلى السلسلة النصية ‏`"background_location_skipped"`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:11]

```
12:     fun setSkipped(context: Context, skipped: Boolean) {
```
> يُعرِّف دالة (fun) باسم ‏`setSkipped` (اضبط التخطّي) تأخذ وسيطاً ‏`context` من نوع ‏`Context` ووسيطاً ‏`skipped` من نوع منطقي ‏`Boolean`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:12]

```
13:         val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُعرِّف متغيّراً ثابتاً (val) باسم ‏`prefs` ويضبط قيمته إلى ناتج استدعاء ‏`context.getSharedPreferences` بالوسيطين ‏`PREFS_NAME` و‏`Context.MODE_PRIVATE`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:13]

```
14:         prefs.edit().putBoolean(KEY_BACKGROUND_LOCATION_SKIP, skipped).apply()
```
> يستدعي ‏`prefs.edit()` ثم ‏`putBoolean` بالمفتاح ‏`KEY_BACKGROUND_LOCATION_SKIP` والقيمة ‏`skipped` ثم ‏`apply()`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:14]

```
15:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:16]

```
17:     fun isSkipped(context: Context): Boolean {
```
> يُعرِّف دالة (fun) باسم ‏`isSkipped` (هل تمّ التخطّي) تأخذ وسيطاً ‏`context` من نوع ‏`Context` وتُعيد قيمة منطقية ‏`Boolean`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:17]

```
18:         val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُعرِّف متغيّراً ثابتاً (val) باسم ‏`prefs` ويضبط قيمته إلى ناتج استدعاء ‏`context.getSharedPreferences` بالوسيطين ‏`PREFS_NAME` و‏`Context.MODE_PRIVATE`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:18]

```
19:         return prefs.getBoolean(KEY_BACKGROUND_LOCATION_SKIP, false)
```
> يُعيد (return) ناتج استدعاء ‏`prefs.getBoolean` بالمفتاح ‏`KEY_BACKGROUND_LOCATION_SKIP` والقيمة الافتراضية ‏`false`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:19]

```
20:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:20]

```
21: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPreferenceManager.kt:21]
