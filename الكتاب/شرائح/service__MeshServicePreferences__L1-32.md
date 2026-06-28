# شريحة — app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt (الأسطر 1–32)

```
1: package com.bitchat.android.service
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.service`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من `android.content`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:3]

```
4: import android.content.SharedPreferences
```
> يستورد (import) الصنف `SharedPreferences` من `android.content`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:5]

```
6: object MeshServicePreferences {
```
> يعرّف كائناً مفرداً (object) باسم `MeshServicePreferences` (تفضيلات خدمة الشبكة المتشابكة) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:6]

```
7:     private const val PREFS_NAME = "bitchat_mesh_service_prefs"
```
> يعرّف ثابتاً خاصاً (private const) باسم `PREFS_NAME` (اسم ملف التفضيلات) وقيمته النصية `"bitchat_mesh_service_prefs"`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:7]

```
8:     private const val KEY_AUTO_START = "auto_start_on_boot"
```
> يعرّف ثابتاً خاصاً (private const) باسم `KEY_AUTO_START` (مفتاح التشغيل التلقائي) وقيمته النصية `"auto_start_on_boot"`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:8]

```
9:     private const val KEY_BACKGROUND_ENABLED = "background_enabled"
```
> يعرّف ثابتاً خاصاً (private const) باسم `KEY_BACKGROUND_ENABLED` (مفتاح تفعيل الخلفية) وقيمته النصية `"background_enabled"`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:9]

```
10: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:10]

```
11:     private lateinit var prefs: SharedPreferences
```
> يعرّف متغيّراً خاصاً مؤجّل التهيئة (private lateinit var) باسم `prefs` من النوع `SharedPreferences`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:11]

```
12: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:12]

```
13:     fun init(context: Context) {
```
> يعرّف دالة (fun) باسم `init` تأخذ وسيطاً باسم `context` من النوع `Context` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:13]

```
14:         prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُسنِد إلى `prefs` نتيجة استدعاء `context.getSharedPreferences` بالوسيطين `PREFS_NAME` و`Context.MODE_PRIVATE`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:14]

```
15:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:16]

```
17:     fun isAutoStartEnabled(default: Boolean = true): Boolean {
```
> يعرّف دالة (fun) باسم `isAutoStartEnabled` تأخذ وسيطاً باسم `default` من النوع `Boolean` قيمته الافتراضية `true` وتُعيد `Boolean` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:17]

```
18:         return prefs.getBoolean(KEY_AUTO_START, default)
```
> يُعيد نتيجة استدعاء `prefs.getBoolean` بالوسيطين `KEY_AUTO_START` و`default`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:18]

```
19:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:19]

```
20: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:20]

```
21:     fun setAutoStartEnabled(enabled: Boolean) {
```
> يعرّف دالة (fun) باسم `setAutoStartEnabled` تأخذ وسيطاً باسم `enabled` من النوع `Boolean` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:21]

```
22:         prefs.edit().putBoolean(KEY_AUTO_START, enabled).apply()
```
> يستدعي `prefs.edit()` ثم `putBoolean` بالوسيطين `KEY_AUTO_START` و`enabled` ثم `apply()`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:22]

```
23:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:24]

```
25:     fun isBackgroundEnabled(default: Boolean = true): Boolean {
```
> يعرّف دالة (fun) باسم `isBackgroundEnabled` تأخذ وسيطاً باسم `default` من النوع `Boolean` قيمته الافتراضية `true` وتُعيد `Boolean` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:25]

```
26:         return prefs.getBoolean(KEY_BACKGROUND_ENABLED, default)
```
> يُعيد نتيجة استدعاء `prefs.getBoolean` بالوسيطين `KEY_BACKGROUND_ENABLED` و`default`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:26]

```
27:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:28]

```
29:     fun setBackgroundEnabled(enabled: Boolean) {
```
> يعرّف دالة (fun) باسم `setBackgroundEnabled` تأخذ وسيطاً باسم `enabled` من النوع `Boolean` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:29]

```
30:         prefs.edit().putBoolean(KEY_BACKGROUND_ENABLED, enabled).apply()
```
> يستدعي `prefs.edit()` ثم `putBoolean` بالوسيطين `KEY_BACKGROUND_ENABLED` و`enabled` ثم `apply()`. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:30]

```
31:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:31]

```
32: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshServicePreferences.kt:32]
