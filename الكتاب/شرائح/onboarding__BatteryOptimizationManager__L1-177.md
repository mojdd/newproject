# شريحة — app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt (الأسطر 1–177)

```
1: package com.bitchat.android.onboarding
```
> يُعرّف انتماء الملف إلى الحزمة (package) باسم com.bitchat.android.onboarding. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف Context من android.content. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:3]

```
4: import android.content.Intent
```
> يستورد الصنف Intent من android.content. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:4]

```
5: import android.net.Uri
```
> يستورد الصنف Uri من android.net. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:5]

```
6: import android.os.Build
```
> يستورد الصنف Build من android.os. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:6]

```
7: import android.os.PowerManager
```
> يستورد الصنف PowerManager من android.os. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:7]

```
8: import android.provider.Settings
```
> يستورد الصنف Settings من android.provider. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:8]

```
9: import android.util.Log
```
> يستورد الصنف Log من android.util. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:9]

```
10: import androidx.activity.ComponentActivity
```
> يستورد الصنف ComponentActivity من androidx.activity. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:10]

```
11: import androidx.activity.result.ActivityResultLauncher
```
> يستورد الصنف ActivityResultLauncher من androidx.activity.result. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:11]

```
12: import androidx.activity.result.contract.ActivityResultContracts
```
> يستورد الصنف ActivityResultContracts من androidx.activity.result.contract. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:12]

```
13: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:13]

```
14: /**
```
> بداية تعليق توثيقي (comment). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:14]

```
15:  * Manages battery optimization settings for the app
```
> تعليق: يدير إعدادات تحسين البطارية (battery optimization) الخاصة بالتطبيق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:15]

```
16:  * Handles checking if the app is whitelisted from battery optimization
```
> تعليق: يتولّى التحقق ممّا إذا كان التطبيق مُستثنى (whitelisted) من تحسين البطارية. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:16]

```
17:  * and requesting the user to disable battery optimization
```
> تعليق: ويطلب من المستخدم تعطيل تحسين البطارية. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:17]

```
18:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:18]

```
19: class BatteryOptimizationManager(
```
> يُعرّف الصنف (class) باسم BatteryOptimizationManager (مدير تحسين البطارية) مع بداية قائمة مُعاملات بانيه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:19]

```
20:     private val activity: ComponentActivity,
```
> يُعرّف مُعامِلاً خاصاً ثابتاً (private val) باسم activity (النشاط) من النوع ComponentActivity. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:20]

```
21:     private val context: Context,
```
> يُعرّف مُعامِلاً خاصاً ثابتاً باسم context (السياق) من النوع Context. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:21]

```
22:     private val onBatteryOptimizationDisabled: () -> Unit,
```
> يُعرّف مُعامِلاً خاصاً ثابتاً باسم onBatteryOptimizationDisabled (عند تعطيل تحسين البطارية) من نوع دالة لا تأخذ معاملات وتُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:22]

```
23:     private val onBatteryOptimizationFailed: (String) -> Unit
```
> يُعرّف مُعامِلاً خاصاً ثابتاً باسم onBatteryOptimizationFailed (عند فشل تحسين البطارية) من نوع دالة تأخذ String وتُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:23]

```
24: ) {
```
> إغلاق قائمة معاملات الباني وبداية جسم الصنف. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:25]

```
26:     companion object {
```
> يبدأ كائناً رفيقاً (companion object). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:26]

```
27:         private const val TAG = "BatteryOptimizationManager"
```
> يُعرّف ثابتاً خاصاً (private const val) باسم TAG (الوسم) بالقيمة النصية "BatteryOptimizationManager". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:27]

```
28:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:28]

```
29: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:29]

```
30:     private var batteryOptimizationLauncher: ActivityResultLauncher<Intent>? = null
```
> يُعرّف متغيراً خاصاً (private var) باسم batteryOptimizationLauncher (مُطلِق تحسين البطارية) من النوع ActivityResultLauncher<Intent> القابل للعدم ويضبط قيمته الابتدائية إلى null. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:30]

```
31: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:31]

```
32:     init {
```
> يبدأ كتلة التهيئة (init). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:32]

```
33:         setupBatteryOptimizationLauncher()
```
> يستدعي الدالة setupBatteryOptimizationLauncher (إعداد مُطلِق تحسين البطارية). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:33]

```
34:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:34]

```
35: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:35]

```
36:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:36]

```
37:      * Setup the battery optimization request launcher
```
> تعليق: إعداد مُطلِق طلب تحسين البطارية. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:37]

```
38:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:38]

```
39:     private fun setupBatteryOptimizationLauncher() {
```
> يُعرّف دالة خاصة (private fun) باسم setupBatteryOptimizationLauncher لا تأخذ معاملات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:39]

```
40:         batteryOptimizationLauncher = activity.registerForActivityResult(
```
> يُسنِد إلى batteryOptimizationLauncher نتيجة استدعاء activity.registerForActivityResult مع بداية معاملاتها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:40]

```
41:             ActivityResultContracts.StartActivityForResult()
```
> يمرّر كمعامل أول كائن ActivityResultContracts.StartActivityForResult. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:41]

```
42:         ) { result ->
```
> يُغلق قائمة المعاملات ويبدأ دالة لامدا (lambda) معاملها result. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:42]

```
43:             Log.d(TAG, "Battery optimization request result: ${result.resultCode}")
```
> يستدعي Log.d بالوسم TAG ورسالة "Battery optimization request result: " متبوعة بقيمة result.resultCode. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:43]

```
44:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:44]

```
45:             // Check if battery optimization is now disabled
```
> تعليق: تحقّق ممّا إذا كان تحسين البطارية مُعطّلاً الآن. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:45]

```
46:             if (isBatteryOptimizationDisabled()) {
```
> يبدأ شرط if يختبر القيمة المُعادة من استدعاء isBatteryOptimizationDisabled. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:46]

```
47:                 Log.d(TAG, "Battery optimization successfully disabled")
```
> يستدعي Log.d بالوسم TAG والرسالة "Battery optimization successfully disabled". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:47]

```
48:                 onBatteryOptimizationDisabled()
```
> يستدعي دالة الاسترجاع onBatteryOptimizationDisabled. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:48]

```
49:             } else {
```
> إغلاق كتلة if وبداية كتلة else. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:49]

```
50:                 Log.w(TAG, "Battery optimization still enabled after user interaction")
```
> يستدعي Log.w بالوسم TAG والرسالة "Battery optimization still enabled after user interaction". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:50]

```
51:                 // Don't treat this as a failure - user might have chosen not to disable it
```
> تعليق: لا تعامل هذا كفشل — ربما اختار المستخدم ألّا يُعطّله. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:51]

```
52:                 // We'll proceed anyway but log the status
```
> تعليق: سنُتابع على أي حال لكن نُسجّل الحالة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:52]

```
53:                 onBatteryOptimizationDisabled()
```
> يستدعي دالة الاسترجاع onBatteryOptimizationDisabled. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:53]

```
54:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:54]

```
55:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:55]

```
56:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:56]

```
57: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:57]

```
58:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:58]

```
59:      * Check if battery optimization is disabled for this app
```
> تعليق: تحقّق ممّا إذا كان تحسين البطارية مُعطّلاً لهذا التطبيق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:59]

```
60:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:60]

```
61:     fun isBatteryOptimizationDisabled(): Boolean {
```
> يُعرّف دالة عامة (fun) باسم isBatteryOptimizationDisabled لا تأخذ معاملات وتُعيد Boolean. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:61]

```
62:         return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
```
> يُعيد نتيجة تعبير if يختبر ما إذا كان Build.VERSION.SDK_INT أكبر من أو يساوي Build.VERSION_CODES.M. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:62]

```
63:             try {
```
> يبدأ كتلة try. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:63]

```
64:                 val powerManager = context.getSystemService(Context.POWER_SERVICE) as PowerManager
```
> يُعرّف ثابتاً (val) باسم powerManager (مدير الطاقة) يساوي نتيجة context.getSystemService(Context.POWER_SERVICE) المُحوَّلة (as) إلى PowerManager. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:64]

```
65:                 val isIgnoring = powerManager.isIgnoringBatteryOptimizations(context.packageName)
```
> يُعرّف ثابتاً باسم isIgnoring (هل يتجاهل) يساوي نتيجة powerManager.isIgnoringBatteryOptimizations مع المعامل context.packageName. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:65]

```
66:                 Log.d(TAG, "Battery optimization disabled: $isIgnoring")
```
> يستدعي Log.d بالوسم TAG والرسالة "Battery optimization disabled: " متبوعة بقيمة isIgnoring. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:66]

```
67:                 isIgnoring
```
> يُنتج القيمة isIgnoring كنتيجة لكتلة try. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:67]

```
68:             } catch (e: Exception) {
```
> إغلاق كتلة try وبداية كتلة catch تلتقط استثناءً (Exception) باسم e. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:68]

```
69:                 Log.e(TAG, "Error checking battery optimization status", e)
```
> يستدعي Log.e بالوسم TAG والرسالة "Error checking battery optimization status" والاستثناء e. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:69]

```
70:                 // If we can't check, assume it's enabled (more conservative)
```
> تعليق: إن لم نستطع التحقق، فافترض أنه مُفعَّل (أكثر تحفّظاً). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:70]

```
71:                 false
```
> يُنتج القيمة false كنتيجة لكتلة catch. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:71]

```
72:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:72]

```
73:         } else {
```
> إغلاق فرع if وبداية فرع else. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:73]

```
74:             // Battery optimization doesn't exist on Android < 6.0
```
> تعليق: تحسين البطارية غير موجود على أندرويد أقل من 6.0. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:74]

```
75:             Log.d(TAG, "Battery optimization not applicable for Android < 6.0")
```
> يستدعي Log.d بالوسم TAG والرسالة "Battery optimization not applicable for Android < 6.0". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:75]

```
76:             true
```
> يُنتج القيمة true كنتيجة لفرع else. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:76]

```
77:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:77]

```
78:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:78]

```
79: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:79]

```
80:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:80]

```
81:      * Request to disable battery optimization for this app
```
> تعليق: اطلب تعطيل تحسين البطارية لهذا التطبيق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:81]

```
82:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:82]

```
83:     fun requestDisableBatteryOptimization() {
```
> يُعرّف دالة عامة باسم requestDisableBatteryOptimization (طلب تعطيل تحسين البطارية) لا تأخذ معاملات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:83]

```
84:         if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
```
> يبدأ شرط if يختبر ما إذا كان Build.VERSION.SDK_INT أكبر من أو يساوي Build.VERSION_CODES.M. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:84]

```
85:             try {
```
> يبدأ كتلة try. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:85]

```
86:                 Log.d(TAG, "Requesting to disable battery optimization")
```
> يستدعي Log.d بالوسم TAG والرسالة "Requesting to disable battery optimization". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:86]

```
87:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:87]

```
88:                 val intent = Intent().apply {
```
> يُعرّف ثابتاً باسم intent (النية) يساوي كائن Intent جديداً مع بداية كتلة apply. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:88]

```
89:                     action = Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS
```
> يضبط الخاصية action على القيمة Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:89]

```
90:                     data = Uri.parse("package:${context.packageName}")
```
> يضبط الخاصية data على نتيجة Uri.parse للنص "package:" متبوعاً بقيمة context.packageName. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:90]

```
91:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:91]

```
92:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:92]

```
93:                 // Check if the intent can be resolved
```
> تعليق: تحقّق ممّا إذا كان يمكن تحليل النية (intent). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:93]

```
94:                 if (intent.resolveActivity(context.packageManager) != null) {
```
> يبدأ شرط if يختبر ما إذا كانت نتيجة intent.resolveActivity مع المعامل context.packageManager لا تساوي null. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:94]

```
95:                     batteryOptimizationLauncher?.launch(intent)
```
> يستدعي launch مع المعامل intent على batteryOptimizationLauncher إن لم يكن null (استدعاء آمن). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:95]

```
96:                 } else {
```
> إغلاق كتلة if وبداية كتلة else. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:96]

```
97:                     Log.w(TAG, "Battery optimization settings not available, opening general settings")
```
> يستدعي Log.w بالوسم TAG والرسالة "Battery optimization settings not available, opening general settings". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:97]

```
98:                     openBatteryOptimizationSettings()
```
> يستدعي الدالة openBatteryOptimizationSettings (فتح إعدادات تحسين البطارية). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:98]

```
99:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:99]

```
100:             } catch (e: Exception) {
```
> إغلاق كتلة try وبداية كتلة catch تلتقط استثناءً باسم e. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:100]

```
101:                 Log.e(TAG, "Error requesting battery optimization disable", e)
```
> يستدعي Log.e بالوسم TAG والرسالة "Error requesting battery optimization disable" والاستثناء e. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:101]

```
102:                 onBatteryOptimizationFailed("Unable to open battery optimization settings: ${e.message}")
```
> يستدعي دالة الاسترجاع onBatteryOptimizationFailed بالنص "Unable to open battery optimization settings: " متبوعاً بقيمة e.message. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:102]

```
103:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:103]

```
104:         } else {
```
> إغلاق كتلة if وبداية كتلة else. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:104]

```
105:             Log.d(TAG, "Battery optimization not applicable for Android < 6.0")
```
> يستدعي Log.d بالوسم TAG والرسالة "Battery optimization not applicable for Android < 6.0". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:105]

```
106:             onBatteryOptimizationDisabled()
```
> يستدعي دالة الاسترجاع onBatteryOptimizationDisabled. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:106]

```
107:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:107]

```
108:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:108]

```
109: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:109]

```
110:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:110]

```
111:      * Open general battery optimization settings if direct request fails
```
> تعليق: افتح إعدادات تحسين البطارية العامة إن فشل الطلب المباشر. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:111]

```
112:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:112]

```
113:     private fun openBatteryOptimizationSettings() {
```
> يُعرّف دالة خاصة باسم openBatteryOptimizationSettings لا تأخذ معاملات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:113]

```
114:         try {
```
> يبدأ كتلة try. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:114]

```
115:             val intent = Intent().apply {
```
> يُعرّف ثابتاً باسم intent يساوي كائن Intent جديداً مع بداية كتلة apply. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:115]

```
116:                 action = Settings.ACTION_IGNORE_BATTERY_OPTIMIZATION_SETTINGS
```
> يضبط الخاصية action على القيمة Settings.ACTION_IGNORE_BATTERY_OPTIMIZATION_SETTINGS. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:116]

```
117:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:117]

```
118:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:118]

```
119:             if (intent.resolveActivity(context.packageManager) != null) {
```
> يبدأ شرط if يختبر ما إذا كانت نتيجة intent.resolveActivity مع المعامل context.packageManager لا تساوي null. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:119]

```
120:                 batteryOptimizationLauncher?.launch(intent)
```
> يستدعي launch مع المعامل intent على batteryOptimizationLauncher إن لم يكن null. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:120]

```
121:             } else {
```
> إغلاق كتلة if وبداية كتلة else. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:121]

```
122:                 // Fallback to general application settings
```
> تعليق: ارتدّ إلى إعدادات التطبيق العامة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:122]

```
123:                 openAppSettings()
```
> يستدعي الدالة openAppSettings (فتح إعدادات التطبيق). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:123]

```
124:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:124]

```
125:         } catch (e: Exception) {
```
> إغلاق كتلة try وبداية كتلة catch تلتقط استثناءً باسم e. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:125]

```
126:             Log.e(TAG, "Error opening battery optimization settings", e)
```
> يستدعي Log.e بالوسم TAG والرسالة "Error opening battery optimization settings" والاستثناء e. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:126]

```
127:             onBatteryOptimizationFailed("Unable to open settings: ${e.message}")
```
> يستدعي دالة الاسترجاع onBatteryOptimizationFailed بالنص "Unable to open settings: " متبوعاً بقيمة e.message. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:127]

```
128:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:128]

```
129:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:129]

```
130: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:130]

```
131:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:131]

```
132:      * Open app settings as a last resort
```
> تعليق: افتح إعدادات التطبيق كملاذ أخير. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:132]

```
133:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:133]

```
134:     private fun openAppSettings() {
```
> يُعرّف دالة خاصة باسم openAppSettings لا تأخذ معاملات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:134]

```
135:         try {
```
> يبدأ كتلة try. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:135]

```
136:             val intent = Intent().apply {
```
> يُعرّف ثابتاً باسم intent يساوي كائن Intent جديداً مع بداية كتلة apply. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:136]

```
137:                 action = Settings.ACTION_APPLICATION_DETAILS_SETTINGS
```
> يضبط الخاصية action على القيمة Settings.ACTION_APPLICATION_DETAILS_SETTINGS. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:137]

```
138:                 data = Uri.fromParts("package", context.packageName, null)
```
> يضبط الخاصية data على نتيجة Uri.fromParts بالمعاملات "package" و context.packageName و null. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:138]

```
139:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:139]

```
140:             batteryOptimizationLauncher?.launch(intent)
```
> يستدعي launch مع المعامل intent على batteryOptimizationLauncher إن لم يكن null. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:140]

```
141:         } catch (e: Exception) {
```
> إغلاق كتلة try وبداية كتلة catch تلتقط استثناءً باسم e. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:141]

```
142:             Log.e(TAG, "Error opening app settings", e)
```
> يستدعي Log.e بالوسم TAG والرسالة "Error opening app settings" والاستثناء e. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:142]

```
143:             onBatteryOptimizationFailed("Unable to open app settings: ${e.message}")
```
> يستدعي دالة الاسترجاع onBatteryOptimizationFailed بالنص "Unable to open app settings: " متبوعاً بقيمة e.message. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:143]

```
144:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:144]

```
145:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:145]

```
146: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:146]

```
147:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:147]

```
148:      * Check if battery optimization is supported on this device
```
> تعليق: تحقّق ممّا إذا كان تحسين البطارية مدعوماً على هذا الجهاز. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:148]

```
149:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:149]

```
150:     fun isBatteryOptimizationSupported(): Boolean {
```
> يُعرّف دالة عامة باسم isBatteryOptimizationSupported (هل تحسين البطارية مدعوم) لا تأخذ معاملات وتُعيد Boolean. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:150]

```
151:         return Build.VERSION.SDK_INT >= Build.VERSION_CODES.M
```
> يُعيد نتيجة المقارنة بين Build.VERSION.SDK_INT و Build.VERSION_CODES.M (أكبر من أو يساوي). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:151]

```
152:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:152]

```
153: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:153]

```
154:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:154]

```
155:      * Get battery optimization status for logging
```
> تعليق: احصل على حالة تحسين البطارية لغرض التسجيل. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:155]

```
156:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:156]

```
157:     fun getBatteryOptimizationStatus(): String {
```
> يُعرّف دالة عامة باسم getBatteryOptimizationStatus (الحصول على حالة تحسين البطارية) لا تأخذ معاملات وتُعيد String. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:157]

```
158:         return when {
```
> يُعيد نتيجة تعبير when بلا وسيط مع بداية فروعه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:158]

```
159:             !isBatteryOptimizationSupported() -> "Not supported (Android < 6.0)"
```
> فرع when: إن كانت نتيجة isBatteryOptimizationSupported منفيّة (غير مدعوم) يُعيد النص "Not supported (Android < 6.0)". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:159]

```
160:             isBatteryOptimizationDisabled() -> "Disabled (app is whitelisted)"
```
> فرع when: إن كانت نتيجة isBatteryOptimizationDisabled صحيحة يُعيد النص "Disabled (app is whitelisted)". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:160]

```
161:             else -> "Enabled (app is being optimized)"
```
> فرع when الافتراضي (else): يُعيد النص "Enabled (app is being optimized)". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:161]

```
162:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:162]

```
163:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:163]

```
164: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:164]

```
165:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:165]

```
166:      * Log battery optimization status for debugging
```
> تعليق: سجّل حالة تحسين البطارية لغرض تصحيح الأخطاء (debugging). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:166]

```
167:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:167]

```
168:     fun logBatteryOptimizationStatus() {
```
> يُعرّف دالة عامة باسم logBatteryOptimizationStatus (تسجيل حالة تحسين البطارية) لا تأخذ معاملات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:168]

```
169:         Log.d(TAG, "Battery optimization status: ${getBatteryOptimizationStatus()}")
```
> يستدعي Log.d بالوسم TAG والرسالة "Battery optimization status: " متبوعة بنتيجة استدعاء getBatteryOptimizationStatus. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:169]

```
170:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:170]

```
171: }
```
> إغلاق نطاق الصنف BatteryOptimizationManager. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:171]

```
172: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:172]

```
173: enum class BatteryOptimizationStatus {
```
> يُعرّف صنفاً تعدادياً (enum class) باسم BatteryOptimizationStatus (حالة تحسين البطارية) مع بداية جسمه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:173]

```
174:     ENABLED,
```
> يُعرّف قيمة تعدادية باسم ENABLED (مُفعَّل). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:174]

```
175:     DISABLED,
```
> يُعرّف قيمة تعدادية باسم DISABLED (مُعطَّل). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:175]

```
176:     NOT_SUPPORTED
```
> يُعرّف قيمة تعدادية باسم NOT_SUPPORTED (غير مدعوم). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:176]

```
177: }
```
> إغلاق نطاق الصنف التعدادي BatteryOptimizationStatus. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationManager.kt:177]
