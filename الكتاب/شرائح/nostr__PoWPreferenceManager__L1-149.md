# شريحة — app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt (الأسطر 1–149)

```
1: package com.bitchat.android.nostr
```
> يُعرّف انتماء الملف للحزمة (package) ‏com.bitchat.android.nostr. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف ‏Context من android.content. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:3]

```
4: import android.content.SharedPreferences
```
> يستورد الصنف ‏SharedPreferences (التفضيلات المشتركة) من android.content. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:4]

```
5: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد الصنف ‏MutableStateFlow (تدفّق الحالة القابل للتغيير) من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:5]

```
6: import kotlinx.coroutines.flow.StateFlow
```
> يستورد الصنف ‏StateFlow (تدفّق الحالة) من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:6]

```
7: import kotlinx.coroutines.flow.asStateFlow
```
> يستورد الدالّة ‏asStateFlow من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:8]

```
9: /**
```
> تعليق: بداية تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:9]

```
10:  * Manages Proof of Work preferences for Nostr events
```
> تعليق: يُدير تفضيلات إثبات العمل (Proof of Work) لأحداث Nostr. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:10]

```
11:  */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:11]

```
12: object PoWPreferenceManager {
```
> يُعرّف كائناً مفرداً (object) باسم ‏PoWPreferenceManager (مدير تفضيلات إثبات العمل) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:12]

```
13:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:13]

```
14:     private const val PREFS_NAME = "pow_preferences"
```
> يُعرّف ثابتاً خاصّاً (private const) باسم ‏PREFS_NAME (اسم التفضيلات) بقيمة نصيّة "pow_preferences". [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:14]

```
15:     private const val KEY_POW_ENABLED = "pow_enabled"
```
> يُعرّف ثابتاً خاصّاً باسم ‏KEY_POW_ENABLED (مفتاح تفعيل إثبات العمل) بقيمة نصيّة "pow_enabled". [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:15]

```
16:     private const val KEY_POW_DIFFICULTY = "pow_difficulty"
```
> يُعرّف ثابتاً خاصّاً باسم ‏KEY_POW_DIFFICULTY (مفتاح صعوبة إثبات العمل) بقيمة نصيّة "pow_difficulty". [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:16]

```
17:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:17]

```
18:     // Default values
```
> تعليق: القيم الافتراضية. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:18]

```
19:     private const val DEFAULT_POW_ENABLED = false
```
> يُعرّف ثابتاً خاصّاً باسم ‏DEFAULT_POW_ENABLED (تفعيل إثبات العمل الافتراضي) بقيمة منطقية false. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:19]

```
20:     private const val DEFAULT_POW_DIFFICULTY = 12 // Reasonable default for geohash spam prevention
```
> يُعرّف ثابتاً خاصّاً باسم ‏DEFAULT_POW_DIFFICULTY (صعوبة إثبات العمل الافتراضية) بقيمة عددية 12، مع تعليق: قيمة افتراضية معقولة لمنع البريد المزعج (spam) في الجيوهاش (geohash). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:20]

```
21:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:21]

```
22:     // State flows for reactive UI
```
> تعليق: تدفّقات الحالة للواجهة التفاعلية. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:22]

```
23:     private val _powEnabled = MutableStateFlow(DEFAULT_POW_ENABLED)
```
> يُعرّف متغيّراً خاصّاً باسم ‏_powEnabled وقيمته تدفّق حالة قابل للتغيير مُهيّأ بالقيمة ‏DEFAULT_POW_ENABLED. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:23]

```
24:     val powEnabled: StateFlow<Boolean> = _powEnabled.asStateFlow()
```
> يُعرّف خاصيّة عامّة باسم ‏powEnabled من نوع ‏StateFlow<Boolean> قيمتها ‏_powEnabled محوّلاً إلى تدفّق حالة عبر ‏asStateFlow(). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:24]

```
25:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:25]

```
26:     private val _powDifficulty = MutableStateFlow(DEFAULT_POW_DIFFICULTY)
```
> يُعرّف متغيّراً خاصّاً باسم ‏_powDifficulty وقيمته تدفّق حالة قابل للتغيير مُهيّأ بالقيمة ‏DEFAULT_POW_DIFFICULTY. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:26]

```
27:     val powDifficulty: StateFlow<Int> = _powDifficulty.asStateFlow()
```
> يُعرّف خاصيّة عامّة باسم ‏powDifficulty من نوع ‏StateFlow<Int> قيمتها ‏_powDifficulty محوّلاً إلى تدفّق حالة عبر ‏asStateFlow(). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:27]

```
28:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:28]

```
29:     // Mining state for animated indicators
```
> تعليق: حالة التعدين (mining) للمؤشّرات المتحرّكة. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:29]

```
30:     private val _isMining = MutableStateFlow(false)
```
> يُعرّف متغيّراً خاصّاً باسم ‏_isMining وقيمته تدفّق حالة قابل للتغيير مُهيّأ بالقيمة المنطقية false. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:30]

```
31:     val isMining: StateFlow<Boolean> = _isMining.asStateFlow()
```
> يُعرّف خاصيّة عامّة باسم ‏isMining من نوع ‏StateFlow<Boolean> قيمتها ‏_isMining محوّلاً إلى تدفّق حالة عبر ‏asStateFlow(). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:31]

```
32:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:32]

```
33:     private lateinit var sharedPrefs: SharedPreferences
```
> يُعرّف متغيّراً خاصّاً مؤجّل التهيئة (lateinit) باسم ‏sharedPrefs من نوع ‏SharedPreferences. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:33]

```
34:     private var isInitialized = false
```
> يُعرّف متغيّراً خاصّاً باسم ‏isInitialized (هل تمّت التهيئة) بقيمة منطقية ابتدائية false. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:34]

```
35:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:35]

```
36:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:36]

```
37:      * Initialize the preference manager with application context
```
> تعليق: تهيئة مدير التفضيلات بسياق التطبيق (application context). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:37]

```
38:      * Should be called once during app startup
```
> تعليق: ينبغي استدعاؤها مرة واحدة أثناء بدء تشغيل التطبيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:38]

```
39:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:39]

```
40:     fun init(context: Context) {
```
> يُعرّف دالّة باسم ‏init تأخذ معاملاً باسم ‏context من نوع ‏Context ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:40]

```
41:         if (isInitialized) return
```
> إن كانت ‏isInitialized صحيحة فيُرجَع من الدالّة دون تنفيذ ما بعدها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:41]

```
42:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:42]

```
43:         sharedPrefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُسنِد إلى ‏sharedPrefs نتيجة استدعاء ‏context.getSharedPreferences بالاسم ‏PREFS_NAME والوضع ‏Context.MODE_PRIVATE. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:43]

```
44:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:44]

```
45:         // Load current values
```
> تعليق: تحميل القيم الحالية. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:45]

```
46:         _powEnabled.value = sharedPrefs.getBoolean(KEY_POW_ENABLED, DEFAULT_POW_ENABLED)
```
> يُسنِد إلى ‏_powEnabled.value القيمة المنطقية المقروءة من ‏sharedPrefs بالمفتاح ‏KEY_POW_ENABLED وبقيمة افتراضية ‏DEFAULT_POW_ENABLED. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:46]

```
47:         _powDifficulty.value = sharedPrefs.getInt(KEY_POW_DIFFICULTY, DEFAULT_POW_DIFFICULTY)
```
> يُسنِد إلى ‏_powDifficulty.value القيمة العددية المقروءة من ‏sharedPrefs بالمفتاح ‏KEY_POW_DIFFICULTY وبقيمة افتراضية ‏DEFAULT_POW_DIFFICULTY. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:47]

```
48:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:48]

```
49:         isInitialized = true
```
> يُسنِد القيمة المنطقية true إلى ‏isInitialized. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:49]

```
50:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:50]

```
51:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:51]

```
52:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:52]

```
53:      * Get current PoW enabled state
```
> تعليق: الحصول على حالة تفعيل إثبات العمل الحالية. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:53]

```
54:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:54]

```
55:     fun isPowEnabled(): Boolean {
```
> يُعرّف دالّة باسم ‏isPowEnabled تُعيد قيمة من نوع ‏Boolean ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:55]

```
56:         return _powEnabled.value
```
> يُعيد قيمة ‏_powEnabled.value. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:56]

```
57:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:57]

```
58:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:58]

```
59:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:59]

```
60:      * Set PoW enabled state
```
> تعليق: ضبط حالة تفعيل إثبات العمل. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:60]

```
61:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:61]

```
62:     fun setPowEnabled(enabled: Boolean) {
```
> يُعرّف دالّة باسم ‏setPowEnabled تأخذ معاملاً باسم ‏enabled من نوع ‏Boolean ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:62]

```
63:         _powEnabled.value = enabled
```
> يُسنِد قيمة المعامل ‏enabled إلى ‏_powEnabled.value. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:63]

```
64:         if (::sharedPrefs.isInitialized) {
```
> إن كان المتغيّر ‏sharedPrefs قد هُيّئ (isInitialized) يُفتَح نطاق التنفيذ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:64]

```
65:             sharedPrefs.edit().putBoolean(KEY_POW_ENABLED, enabled).apply()
```
> يفتح محرّر ‏sharedPrefs.edit() ويضع القيمة المنطقية ‏enabled بالمفتاح ‏KEY_POW_ENABLED ثم يُطبّقها عبر ‏apply(). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:65]

```
66:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:66]

```
67:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:67]

```
68:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:68]

```
69:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:69]

```
70:      * Get current PoW difficulty setting
```
> تعليق: الحصول على إعداد صعوبة إثبات العمل الحالي. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:70]

```
71:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:71]

```
72:     fun getPowDifficulty(): Int {
```
> يُعرّف دالّة باسم ‏getPowDifficulty تُعيد قيمة من نوع ‏Int ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:72]

```
73:         return _powDifficulty.value
```
> يُعيد قيمة ‏_powDifficulty.value. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:73]

```
74:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:74]

```
75:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:75]

```
76:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:76]

```
77:      * Set PoW difficulty (clamped between 0 and 32)
```
> تعليق: ضبط صعوبة إثبات العمل (محصورة بين 0 و32). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:77]

```
78:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:78]

```
79:     fun setPowDifficulty(difficulty: Int) {
```
> يُعرّف دالّة باسم ‏setPowDifficulty تأخذ معاملاً باسم ‏difficulty من نوع ‏Int ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:79]

```
80:         val clampedDifficulty = difficulty.coerceIn(0, 32)
```
> يُعرّف متغيّراً باسم ‏clampedDifficulty (الصعوبة المحصورة) قيمته ‏difficulty محصورة بين 0 و32 عبر ‏coerceIn. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:80]

```
81:         _powDifficulty.value = clampedDifficulty
```
> يُسنِد ‏clampedDifficulty إلى ‏_powDifficulty.value. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:81]

```
82:         if (::sharedPrefs.isInitialized) {
```
> إن كان المتغيّر ‏sharedPrefs قد هُيّئ يُفتَح نطاق التنفيذ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:82]

```
83:             sharedPrefs.edit().putInt(KEY_POW_DIFFICULTY, clampedDifficulty).apply()
```
> يفتح محرّر ‏sharedPrefs.edit() ويضع القيمة العددية ‏clampedDifficulty بالمفتاح ‏KEY_POW_DIFFICULTY ثم يُطبّقها عبر ‏apply(). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:83]

```
84:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:84]

```
85:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:85]

```
86:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:86]

```
87:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:87]

```
88:      * Get current settings as a data class
```
> تعليق: الحصول على الإعدادات الحالية كصنف بيانات (data class). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:88]

```
89:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:89]

```
90:     data class PoWSettings(
```
> يُعرّف صنف بيانات (data class) باسم ‏PoWSettings (إعدادات إثبات العمل) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:90]

```
91:         val enabled: Boolean,
```
> يُعرّف خاصيّة باسم ‏enabled من نوع ‏Boolean. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:91]

```
92:         val difficulty: Int
```
> يُعرّف خاصيّة باسم ‏difficulty من نوع ‏Int. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:92]

```
93:     )
```
> إغلاق قائمة معاملات صنف البيانات. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:93]

```
94:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:94]

```
95:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:95]

```
96:      * Get current settings
```
> تعليق: الحصول على الإعدادات الحالية. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:96]

```
97:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:97]

```
98:     fun getCurrentSettings(): PoWSettings {
```
> يُعرّف دالّة باسم ‏getCurrentSettings تُعيد قيمة من نوع ‏PoWSettings ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:98]

```
99:         return PoWSettings(
```
> يُعيد كائناً جديداً من ‏PoWSettings ويفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:99]

```
100:             enabled = _powEnabled.value,
```
> يُمرّر للمعامل ‏enabled القيمة ‏_powEnabled.value. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:100]

```
101:             difficulty = _powDifficulty.value
```
> يُمرّر للمعامل ‏difficulty القيمة ‏_powDifficulty.value. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:101]

```
102:         )
```
> إغلاق قائمة الوُسطاء. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:102]

```
103:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:103]

```
104:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:104]

```
105:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:105]

```
106:      * Reset to default settings
```
> تعليق: إعادة الضبط إلى الإعدادات الافتراضية. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:106]

```
107:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:107]

```
108:     fun resetToDefaults() {
```
> يُعرّف دالّة باسم ‏resetToDefaults ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:108]

```
109:         setPowEnabled(DEFAULT_POW_ENABLED)
```
> يستدعي ‏setPowEnabled بالوسيط ‏DEFAULT_POW_ENABLED. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:109]

```
110:         setPowDifficulty(DEFAULT_POW_DIFFICULTY)
```
> يستدعي ‏setPowDifficulty بالوسيط ‏DEFAULT_POW_DIFFICULTY. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:110]

```
111:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:111]

```
112:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:112]

```
113:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:113]

```
114:      * Get difficulty levels with descriptions for UI
```
> تعليق: الحصول على مستويات الصعوبة مع أوصافها للواجهة. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:114]

```
115:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:115]

```
116:     fun getDifficultyLevels(): List<Pair<Int, String>> {
```
> يُعرّف دالّة باسم ‏getDifficultyLevels تُعيد قيمة من نوع ‏List<Pair<Int, String>> (قائمة أزواج عدد ونص) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:116]

```
117:         return listOf(
```
> يُعيد قائمة مُنشأة عبر ‏listOf ويفتح قائمة عناصرها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:117]

```
118:             0 to "Disabled (no PoW)",
```
> عنصر زوج يربط العدد 0 بالنص "Disabled (no PoW)" (معطّل، بلا إثبات عمل). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:118]

```
119:             8 to "Very Low (instant)",
```
> عنصر زوج يربط العدد 8 بالنص "Very Low (instant)" (منخفض جداً، فوري). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:119]

```
120:             12 to "Low (~0.1s)",
```
> عنصر زوج يربط العدد 12 بالنص "Low (~0.1s)" (منخفض، نحو 0.1 ثانية). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:120]

```
121:             16 to "Medium (~2s)",
```
> عنصر زوج يربط العدد 16 بالنص "Medium (~2s)" (متوسّط، نحو 2 ثانية). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:121]

```
122:             20 to "High (~30s)",
```
> عنصر زوج يربط العدد 20 بالنص "High (~30s)" (مرتفع، نحو 30 ثانية). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:122]

```
123:             24 to "Very High (~8m)",
```
> عنصر زوج يربط العدد 24 بالنص "Very High (~8m)" (مرتفع جداً، نحو 8 دقائق). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:123]

```
124:             28 to "Extreme (~2h)",
```
> عنصر زوج يربط العدد 28 بالنص "Extreme (~2h)" (متطرّف، نحو ساعتين). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:124]

```
125:             32 to "Maximum (~8h)"
```
> عنصر زوج يربط العدد 32 بالنص "Maximum (~8h)" (أقصى، نحو 8 ساعات). [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:125]

```
126:         )
```
> إغلاق قائمة عناصر ‏listOf. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:126]

```
127:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:127]

```
128:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:128]

```
129:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:129]

```
130:      * Get current mining state
```
> تعليق: الحصول على حالة التعدين الحالية. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:130]

```
131:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:131]

```
132:     fun isMining(): Boolean {
```
> يُعرّف دالّة باسم ‏isMining تُعيد قيمة من نوع ‏Boolean ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:132]

```
133:         return _isMining.value
```
> يُعيد قيمة ‏_isMining.value. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:133]

```
134:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:134]

```
135:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:135]

```
136:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:136]

```
137:      * Start mining state - triggers animated indicators
```
> تعليق: بدء حالة التعدين، يُطلق المؤشّرات المتحرّكة. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:137]

```
138:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:138]

```
139:     fun startMining() {
```
> يُعرّف دالّة باسم ‏startMining ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:139]

```
140:         _isMining.value = true
```
> يُسنِد القيمة المنطقية true إلى ‏_isMining.value. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:140]

```
141:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:141]

```
142:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:142]

```
143:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:143]

```
144:      * Stop mining state - stops animated indicators
```
> تعليق: إيقاف حالة التعدين، يوقف المؤشّرات المتحرّكة. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:144]

```
145:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:145]

```
146:     fun stopMining() {
```
> يُعرّف دالّة باسم ‏stopMining ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:146]

```
147:         _isMining.value = false
```
> يُسنِد القيمة المنطقية false إلى ‏_isMining.value. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:147]

```
148:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:148]

```
149: }
```
> إغلاق نطاق الكائن المفرد ‏PoWPreferenceManager. [app/src/main/java/com/bitchat/android/nostr/PoWPreferenceManager.kt:149]
