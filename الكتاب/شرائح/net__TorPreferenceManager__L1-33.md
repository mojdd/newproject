# شريحة — app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt (الأسطر 1–33)

```
1: package com.bitchat.android.net
```
> يُعرّف الحزمة (package) باسم com.bitchat.android.net. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف Context من android.content. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:3]

```
4: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد الصنف MutableStateFlow (تدفّق حالة قابل للتغيير) من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:4]

```
5: import kotlinx.coroutines.flow.StateFlow
```
> يستورد الصنف StateFlow (تدفّق حالة) من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:6]

```
7: object TorPreferenceManager {
```
> يُعرّف كائناً مفرداً (object) باسم TorPreferenceManager (مدير تفضيلات Tor) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:7]

```
8:     private const val PREFS_NAME = "bitchat_settings"
```
> يُعرّف ثابتاً خاصاً (private const val) باسم PREFS_NAME وقيمته السلسلة النصية "bitchat_settings". [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:8]

```
9:     private const val KEY_TOR_MODE = "tor_mode"
```
> يُعرّف ثابتاً خاصاً باسم KEY_TOR_MODE (مفتاح وضع Tor) وقيمته السلسلة النصية "tor_mode". [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:9]

```
10: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:10]

```
11:     private val _modeFlow = MutableStateFlow(TorMode.ON)
```
> يُعرّف متغيّراً خاصاً ثابت المرجع (private val) باسم ‎_modeFlow ويُسنِد إليه نسخة MutableStateFlow قيمتها الابتدائية TorMode.ON. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:11]

```
12:     val modeFlow: StateFlow<TorMode> = _modeFlow
```
> يُعرّف متغيّراً ثابت المرجع باسم modeFlow من نوع StateFlow<TorMode> ويُسنِد إليه ‎_modeFlow. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:12]

```
13: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:13]

```
14:     fun init(context: Context) {
```
> يُعرّف دالّة (fun) باسم init تأخذ وسيطاً باسم context من نوع Context ويفتح نطاقها. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:14]

```
15:         val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُعرّف متغيّراً ثابت المرجع باسم prefs ويُسنِد إليه ناتج استدعاء context.getSharedPreferences بالوسيطين PREFS_NAME و Context.MODE_PRIVATE. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:15]

```
16:         val saved = prefs.getString(KEY_TOR_MODE, TorMode.ON.name)
```
> يُعرّف متغيّراً ثابت المرجع باسم saved ويُسنِد إليه ناتج استدعاء prefs.getString بالمفتاح KEY_TOR_MODE والقيمة الافتراضية TorMode.ON.name. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:16]

```
17:         val mode = runCatching { TorMode.valueOf(saved ?: TorMode.ON.name) }.getOrDefault(TorMode.ON)
```
> يُعرّف متغيّراً ثابت المرجع باسم mode ويُسنِد إليه ناتج runCatching الذي يستدعي TorMode.valueOf على saved أو على TorMode.ON.name إن كان saved فارغاً (null)، ويُعيد عند الفشل القيمة الافتراضية TorMode.ON عبر getOrDefault. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:17]

```
18:         _modeFlow.value = mode
```
> يُسنِد قيمة mode إلى الخاصية value الخاصة بـ ‎_modeFlow. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:18]

```
19:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:19]

```
20: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:20]

```
21:     fun set(context: Context, mode: TorMode) {
```
> يُعرّف دالّة باسم set تأخذ وسيطاً باسم context من نوع Context ووسيطاً باسم mode من نوع TorMode ويفتح نطاقها. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:21]

```
22:         val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُعرّف متغيّراً ثابت المرجع باسم prefs ويُسنِد إليه ناتج استدعاء context.getSharedPreferences بالوسيطين PREFS_NAME و Context.MODE_PRIVATE. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:22]

```
23:         prefs.edit().putString(KEY_TOR_MODE, mode.name).apply()
```
> يستدعي prefs.edit ثم putString بالمفتاح KEY_TOR_MODE والقيمة mode.name ثم apply. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:23]

```
24:         _modeFlow.value = mode
```
> يُسنِد قيمة mode إلى الخاصية value الخاصة بـ ‎_modeFlow. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:24]

```
25:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:25]

```
26: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:26]

```
27:     fun get(context: Context): TorMode {
```
> يُعرّف دالّة باسم get تأخذ وسيطاً باسم context من نوع Context وتُعيد قيمة من نوع TorMode ويفتح نطاقها. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:27]

```
28:         val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُعرّف متغيّراً ثابت المرجع باسم prefs ويُسنِد إليه ناتج استدعاء context.getSharedPreferences بالوسيطين PREFS_NAME و Context.MODE_PRIVATE. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:28]

```
29:         val saved = prefs.getString(KEY_TOR_MODE, TorMode.ON.name)
```
> يُعرّف متغيّراً ثابت المرجع باسم saved ويُسنِد إليه ناتج استدعاء prefs.getString بالمفتاح KEY_TOR_MODE والقيمة الافتراضية TorMode.ON.name. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:29]

```
30:         return runCatching { TorMode.valueOf(saved ?: TorMode.ON.name) }.getOrDefault(TorMode.ON)
```
> يُعيد ناتج runCatching الذي يستدعي TorMode.valueOf على saved أو على TorMode.ON.name إن كان saved فارغاً (null)، ويُعيد عند الفشل القيمة الافتراضية TorMode.ON عبر getOrDefault. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:30]

```
31:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:31]

```
32: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/TorPreferenceManager.kt:33]
