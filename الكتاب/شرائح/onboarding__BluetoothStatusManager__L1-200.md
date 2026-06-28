# شريحة — app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.onboarding
```
> يُعرّف حزمة (package) الملف باسم com.bitchat.android.onboarding. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:2]

```
3: import android.bluetooth.BluetoothAdapter
```
> يستورد (import) الصنف BluetoothAdapter من حزمة android.bluetooth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:3]

```
4: import android.bluetooth.BluetoothManager
```
> يستورد الصنف BluetoothManager من حزمة android.bluetooth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:4]

```
5: import android.content.BroadcastReceiver
```
> يستورد الصنف BroadcastReceiver من حزمة android.content. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:5]

```
6: import android.content.Context
```
> يستورد الصنف Context من حزمة android.content. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:6]

```
7: import android.content.Intent
```
> يستورد الصنف Intent من حزمة android.content. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:7]

```
8: import android.content.IntentFilter
```
> يستورد الصنف IntentFilter من حزمة android.content. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:8]

```
9: import android.util.Log
```
> يستورد الصنف Log من حزمة android.util. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:9]

```
10: import androidx.activity.ComponentActivity
```
> يستورد الصنف ComponentActivity من حزمة androidx.activity. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:10]

```
11: import androidx.activity.result.ActivityResultLauncher
```
> يستورد الصنف ActivityResultLauncher من حزمة androidx.activity.result. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:11]

```
12: import androidx.activity.result.contract.ActivityResultContracts
```
> يستورد الصنف ActivityResultContracts من حزمة androidx.activity.result.contract. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:12]

```
13: import androidx.core.content.ContextCompat
```
> يستورد الصنف ContextCompat من حزمة androidx.core.content. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:13]

```
14: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:14]

```
15: /**
```
> تعليق: بداية كتلة توثيق (تعليق KDoc). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:15]

```
16:  * Manages Bluetooth enable/disable state and user prompts
```
> تعليق: «يدير حالة تمكين/تعطيل البلوتوث ومطالبات المستخدم». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:16]

```
17:  * Checks Bluetooth status on every app startup
```
> تعليق: «يفحص حالة البلوتوث عند كل بدء تشغيل للتطبيق». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:17]

```
18:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:18]

```
19: class BluetoothStatusManager(
```
> يعرّف صنفاً (class) باسم BluetoothStatusManager (مدير حالة البلوتوث) ويبدأ قائمة وسائط بانيه الأساسي. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:19]

```
20:     private val activity: ComponentActivity,
```
> يعرّف خاصية خاصة باسم activity (النشاط) من النوع ComponentActivity كوسيط للباني. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:20]

```
21:     private val context: Context,
```
> يعرّف خاصية خاصة باسم context (السياق) من النوع Context كوسيط للباني. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:21]

```
22:     private val onBluetoothEnabled: () -> Unit,
```
> يعرّف خاصية خاصة باسم onBluetoothEnabled (عند تمكين البلوتوث) من النوع دالة بلا وسائط تُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:22]

```
23:     private val onBluetoothDisabled: (String) -> Unit
```
> يعرّف خاصية خاصة باسم onBluetoothDisabled (عند تعطيل البلوتوث) من النوع دالة تأخذ نصاً (String) وتُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:23]

```
24: ) {
```
> ينهي قائمة وسائط الباني ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:25]

```
26:     companion object {
```
> يفتح كائناً مرافقاً (companion object) داخل الصنف. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:26]

```
27:         private const val TAG = "BluetoothStatusManager"
```
> يعرّف ثابتاً خاصاً (const) باسم TAG بقيمة النص "BluetoothStatusManager". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:27]

```
28:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:28]

```
29: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:29]

```
30:     private var bluetoothEnableLauncher: ActivityResultLauncher<Intent>? = null
```
> يعرّف متغيراً خاصاً قابلاً للتغيير باسم bluetoothEnableLauncher (مُطلِق تمكين البلوتوث) من النوع ActivityResultLauncher<Intent> القابل للقيمة الفارغة، ويُسند إليه null. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:30]

```
31:     private var bluetoothAdapter: BluetoothAdapter? = null
```
> يعرّف متغيراً خاصاً قابلاً للتغيير باسم bluetoothAdapter (مهايئ البلوتوث) من النوع BluetoothAdapter القابل للقيمة الفارغة، ويُسند إليه null. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:31]

```
32: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:32]

```
33:     init {
```
> يفتح كتلة التهيئة (init) للصنف. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:33]

```
34:         setupBluetoothAdapter()
```
> يستدعي الدالة setupBluetoothAdapter (إعداد مهايئ البلوتوث). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:34]

```
35:         setupBluetoothEnableLauncher()
```
> يستدعي الدالة setupBluetoothEnableLauncher (إعداد مُطلِق تمكين البلوتوث). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:35]

```
36:     }
```
> إغلاق نطاق كتلة التهيئة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:36]

```
37: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:37]

```
38:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:38]

```
39:      * Setup Bluetooth adapter reference
```
> تعليق: «إعداد مرجع مهايئ البلوتوث». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:39]

```
40:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:40]

```
41:     private fun setupBluetoothAdapter() {
```
> يعرّف دالة خاصة باسم setupBluetoothAdapter بلا وسائط ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:41]

```
42:         try {
```
> يفتح كتلة try (محاولة). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:42]

```
43:             val bluetoothManager = context.getSystemService(Context.BLUETOOTH_SERVICE) as BluetoothManager
```
> يعرّف متغيراً ثابتاً باسم bluetoothManager (مدير البلوتوث) ويُسند إليه ناتج استدعاء context.getSystemService بالوسيط Context.BLUETOOTH_SERVICE مُحوَّلاً (as) إلى النوع BluetoothManager. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:43]

```
44:             bluetoothAdapter = bluetoothManager.adapter
```
> يُسند إلى bluetoothAdapter قيمة الخاصية adapter من bluetoothManager. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:44]

```
45:             Log.d(TAG, "Bluetooth adapter initialized: ${bluetoothAdapter != null}")
```
> يستدعي Log.d بالوسم TAG ونصٍّ "Bluetooth adapter initialized: " متبوع بنتيجة المقارنة bluetoothAdapter != null. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:45]

```
46:         } catch (e: Exception) {
```
> يغلق كتلة try ويفتح كتلة catch تلتقط استثناءً باسم e من النوع Exception. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:46]

```
47:             Log.e(TAG, "Failed to initialize Bluetooth adapter", e)
```
> يستدعي Log.e بالوسم TAG والنص "Failed to initialize Bluetooth adapter" والاستثناء e. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:47]

```
48:             bluetoothAdapter = null
```
> يُسند إلى bluetoothAdapter القيمة null. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:48]

```
49:         }
```
> إغلاق نطاق كتلة catch. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:49]

```
50:     }
```
> إغلاق نطاق الدالة setupBluetoothAdapter. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:50]

```
51: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:51]

```
52:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:52]

```
53:      * Setup launcher for Bluetooth enable request
```
> تعليق: «إعداد المُطلِق لطلب تمكين البلوتوث». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:53]

```
54:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:54]

```
55:     private fun setupBluetoothEnableLauncher() {
```
> يعرّف دالة خاصة باسم setupBluetoothEnableLauncher بلا وسائط ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:55]

```
56:         bluetoothEnableLauncher = activity.registerForActivityResult(
```
> يُسند إلى bluetoothEnableLauncher ناتج استدعاء activity.registerForActivityResult ويبدأ تمرير وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:56]

```
57:             ActivityResultContracts.StartActivityForResult()
```
> يمرّر كائن العقد ActivityResultContracts.StartActivityForResult() كوسيط أول. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:57]

```
58:         ) { result ->
```
> يغلق قائمة الوسائط ويبدأ تعبيراً لامبدا (lambda) بمعامل باسم result (النتيجة). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:58]

```
59:             val isEnabled = bluetoothAdapter?.isEnabled == true
```
> يعرّف متغيراً ثابتاً باسم isEnabled (مُمكَّن) ويُسند إليه نتيجة المقارنة bluetoothAdapter?.isEnabled == true. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:59]

```
60:             Log.d(TAG, "Bluetooth enable request result: $isEnabled (result code: ${result.resultCode})")
```
> يستدعي Log.d بالوسم TAG ونصٍّ "Bluetooth enable request result: " متبوع بقيمة isEnabled و"(result code: " متبوع بقيمة result.resultCode. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:60]

```
61:             if (isEnabled) {
```
> يفتح شرط if على القيمة isEnabled. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:61]

```
62:                 onBluetoothEnabled()
```
> يستدعي الدالة onBluetoothEnabled. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:62]

```
63:             } else {
```
> يغلق فرع if ويفتح فرع else. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:63]

```
64:                 onBluetoothDisabled("Bluetooth is required for bitchat to discover and connect to nearby users. Please enable Bluetooth to continue.")
```
> يستدعي الدالة onBluetoothDisabled بنصٍّ "Bluetooth is required for bitchat to discover and connect to nearby users. Please enable Bluetooth to continue.". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:64]

```
65:             }
```
> إغلاق نطاق فرع else. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:65]

```
66:         }
```
> إغلاق نطاق تعبير اللامبدا. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:66]

```
67:     }
```
> إغلاق نطاق الدالة setupBluetoothEnableLauncher. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:67]

```
68: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:68]

```
69:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:69]

```
70:      * Check if Bluetooth is supported on this device
```
> تعليق: «يفحص ما إذا كان البلوتوث مدعوماً على هذا الجهاز». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:70]

```
71:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:71]

```
72:     fun isBluetoothSupported(): Boolean {
```
> يعرّف دالة عامة باسم isBluetoothSupported (هل البلوتوث مدعوم) تُعيد قيمة منطقية (Boolean) ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:72]

```
73:         return bluetoothAdapter != null
```
> يُعيد نتيجة المقارنة bluetoothAdapter != null. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:73]

```
74:     }
```
> إغلاق نطاق الدالة isBluetoothSupported. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:74]

```
75: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:75]

```
76:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:76]

```
77:      * Check if Bluetooth is currently enabled (permission-safe)
```
> تعليق: «يفحص ما إذا كان البلوتوث مُمكَّناً حالياً (آمن من ناحية الأذونات)». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:77]

```
78:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:78]

```
79:     fun isBluetoothEnabled(): Boolean {
```
> يعرّف دالة عامة باسم isBluetoothEnabled (هل البلوتوث مُمكَّن) تُعيد قيمة منطقية ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:79]

```
80:         return try {
```
> يُعيد ناتج كتلة try التي تُفتح هنا. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:80]

```
81:             bluetoothAdapter?.isEnabled == true
```
> ينتج نتيجة المقارنة bluetoothAdapter?.isEnabled == true كقيمة كتلة try. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:81]

```
82:         } catch (securityException: SecurityException) {
```
> يغلق كتلة try ويفتح كتلة catch تلتقط استثناءً باسم securityException من النوع SecurityException. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:82]

```
83:             // If we can't check due to permissions, assume disabled
```
> تعليق: «إذا تعذّر الفحص بسبب الأذونات، افترض أنه معطّل». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:83]

```
84:             Log.w(TAG, "Cannot check Bluetooth enabled state due to missing permissions")
```
> يستدعي Log.w بالوسم TAG والنص "Cannot check Bluetooth enabled state due to missing permissions". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:84]

```
85:             false
```
> ينتج القيمة false كقيمة كتلة catch. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:85]

```
86:         } catch (e: Exception) {
```
> يغلق كتلة catch السابقة ويفتح كتلة catch أخرى تلتقط استثناءً باسم e من النوع Exception. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:86]

```
87:             Log.w(TAG, "Error checking Bluetooth enabled state: ${e.message}")
```
> يستدعي Log.w بالوسم TAG ونصٍّ "Error checking Bluetooth enabled state: " متبوع بقيمة e.message. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:87]

```
88:             false
```
> ينتج القيمة false كقيمة كتلة catch. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:88]

```
89:         }
```
> إغلاق نطاق كتلة catch الثانية. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:89]

```
90:     }
```
> إغلاق نطاق الدالة isBluetoothEnabled. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:90]

```
91: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:91]

```
92:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:92]

```
93:      * Check Bluetooth status and handle accordingly (permission-safe)
```
> تعليق: «يفحص حالة البلوتوث ويعالجها وفق ذلك (آمن من ناحية الأذونات)». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:93]

```
94:      * This should be called on every app startup
```
> تعليق: «ينبغي استدعاء هذا عند كل بدء تشغيل للتطبيق». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:94]

```
95:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:95]

```
96:     fun checkBluetoothStatus(): BluetoothStatus {
```
> يعرّف دالة عامة باسم checkBluetoothStatus (فحص حالة البلوتوث) تُعيد قيمة من النوع BluetoothStatus ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:96]

```
97:         // Log.d(TAG, "Checking Bluetooth status")
```
> تعليق: سطر مُعطَّل بالتعليق نصّه Log.d(TAG, "Checking Bluetooth status"). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:97]

```
98:         
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:98]

```
99:         return when {
```
> يُعيد ناتج تعبير when بلا موضوع (when الشرطية) المفتوح هنا. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:99]

```
100:             bluetoothAdapter == null -> {
```
> يفتح فرع when عند تحقّق الشرط bluetoothAdapter == null. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:100]

```
101:                 Log.e(TAG, "Bluetooth not supported on this device")
```
> يستدعي Log.e بالوسم TAG والنص "Bluetooth not supported on this device". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:101]

```
102:                 BluetoothStatus.NOT_SUPPORTED
```
> ينتج قيمة التعداد BluetoothStatus.NOT_SUPPORTED كقيمة هذا الفرع. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:102]

```
103:             }
```
> إغلاق نطاق فرع when الأول. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:103]

```
104:             !isBluetoothEnabled() -> {
```
> يفتح فرع when عند تحقّق الشرط نفي ناتج isBluetoothEnabled(). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:104]

```
105:                 Log.w(TAG, "Bluetooth is disabled or cannot be checked")
```
> يستدعي Log.w بالوسم TAG والنص "Bluetooth is disabled or cannot be checked". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:105]

```
106:                 BluetoothStatus.DISABLED
```
> ينتج قيمة التعداد BluetoothStatus.DISABLED كقيمة هذا الفرع. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:106]

```
107:             }
```
> إغلاق نطاق فرع when الثاني. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:107]

```
108:             else -> {
```
> يفتح فرع when الافتراضي else. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:108]

```
109:                 // Log.d(TAG, "Bluetooth is enabled and ready")
```
> تعليق: سطر مُعطَّل بالتعليق نصّه Log.d(TAG, "Bluetooth is enabled and ready"). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:109]

```
110:                 BluetoothStatus.ENABLED
```
> ينتج قيمة التعداد BluetoothStatus.ENABLED كقيمة هذا الفرع. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:110]

```
111:             }
```
> إغلاق نطاق فرع else. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:111]

```
112:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:112]

```
113:     }
```
> إغلاق نطاق الدالة checkBluetoothStatus. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:113]

```
114: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:114]

```
115:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:115]

```
116:      * Request user to enable Bluetooth (permission-aware)
```
> تعليق: «يطلب من المستخدم تمكين البلوتوث (مدرك للأذونات)». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:116]

```
117:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:117]

```
118:     fun requestEnableBluetooth() {
```
> يعرّف دالة عامة باسم requestEnableBluetooth (طلب تمكين البلوتوث) بلا وسائط ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:118]

```
119:         Log.d(TAG, "Requesting user to enable Bluetooth")
```
> يستدعي Log.d بالوسم TAG والنص "Requesting user to enable Bluetooth". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:119]

```
120:         
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:120]

```
121:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:121]

```
122:             val enableBluetoothIntent = Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE)
```
> يعرّف متغيراً ثابتاً باسم enableBluetoothIntent (نية تمكين البلوتوث) ويُسند إليه كائن Intent مُنشأً بالوسيط BluetoothAdapter.ACTION_REQUEST_ENABLE. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:122]

```
123:             bluetoothEnableLauncher?.launch(enableBluetoothIntent)
```
> يستدعي الدالة launch على bluetoothEnableLauncher (إن لم يكن null) بالوسيط enableBluetoothIntent. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:123]

```
124:         } catch (securityException: SecurityException) {
```
> يغلق كتلة try ويفتح كتلة catch تلتقط استثناءً باسم securityException من النوع SecurityException. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:124]

```
125:             // Permission not granted yet - this is expected during onboarding
```
> تعليق: «الإذن لم يُمنح بعد - هذا متوقَّع أثناء التهيئة الأولية». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:125]

```
126:             Log.w(TAG, "Cannot request Bluetooth enable due to missing BLUETOOTH_CONNECT permission")
```
> يستدعي Log.w بالوسم TAG والنص "Cannot request Bluetooth enable due to missing BLUETOOTH_CONNECT permission". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:126]

```
127:             onBluetoothDisabled("Bluetooth permissions are required before enabling Bluetooth. Please grant permissions first.")
```
> يستدعي الدالة onBluetoothDisabled بنصٍّ "Bluetooth permissions are required before enabling Bluetooth. Please grant permissions first.". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:127]

```
128:         } catch (e: Exception) {
```
> يغلق كتلة catch السابقة ويفتح كتلة catch أخرى تلتقط استثناءً باسم e من النوع Exception. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:128]

```
129:             Log.e(TAG, "Failed to request Bluetooth enable", e)
```
> يستدعي Log.e بالوسم TAG والنص "Failed to request Bluetooth enable" والاستثناء e. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:129]

```
130:             onBluetoothDisabled("Failed to request Bluetooth enable: ${e.message}")
```
> يستدعي الدالة onBluetoothDisabled بنصٍّ "Failed to request Bluetooth enable: " متبوع بقيمة e.message. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:130]

```
131:         }
```
> إغلاق نطاق كتلة catch الثانية. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:131]

```
132:     }
```
> إغلاق نطاق الدالة requestEnableBluetooth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:132]

```
133: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:133]

```
134:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:134]

```
135:      * Handle Bluetooth status check result
```
> تعليق: «يعالج نتيجة فحص حالة البلوتوث». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:135]

```
136:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:136]

```
137:     fun handleBluetoothStatus(status: BluetoothStatus) {
```
> يعرّف دالة عامة باسم handleBluetoothStatus (معالجة حالة البلوتوث) تأخذ وسيطاً باسم status (الحالة) من النوع BluetoothStatus ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:137]

```
138:         when (status) {
```
> يفتح تعبير when على الموضوع status. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:138]

```
139:             BluetoothStatus.ENABLED -> {
```
> يفتح فرع when عند مطابقة القيمة BluetoothStatus.ENABLED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:139]

```
140:                 Log.d(TAG, "Bluetooth is enabled, proceeding")
```
> يستدعي Log.d بالوسم TAG والنص "Bluetooth is enabled, proceeding". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:140]

```
141:                 onBluetoothEnabled()
```
> يستدعي الدالة onBluetoothEnabled. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:141]

```
142:             }
```
> إغلاق نطاق فرع ENABLED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:142]

```
143:             BluetoothStatus.DISABLED -> {
```
> يفتح فرع when عند مطابقة القيمة BluetoothStatus.DISABLED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:143]

```
144:                 Log.d(TAG, "Bluetooth is disabled, requesting enable")
```
> يستدعي Log.d بالوسم TAG والنص "Bluetooth is disabled, requesting enable". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:144]

```
145:                 requestEnableBluetooth()
```
> يستدعي الدالة requestEnableBluetooth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:145]

```
146:             }
```
> إغلاق نطاق فرع DISABLED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:146]

```
147:             BluetoothStatus.NOT_SUPPORTED -> {
```
> يفتح فرع when عند مطابقة القيمة BluetoothStatus.NOT_SUPPORTED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:147]

```
148:                 Log.e(TAG, "Bluetooth not supported")
```
> يستدعي Log.e بالوسم TAG والنص "Bluetooth not supported". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:148]

```
149:                 onBluetoothDisabled("This device doesn't support Bluetooth, which is required for bitchat to function.")
```
> يستدعي الدالة onBluetoothDisabled بنصٍّ "This device doesn't support Bluetooth, which is required for bitchat to function.". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:149]

```
150:             }
```
> إغلاق نطاق فرع NOT_SUPPORTED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:150]

```
151:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:151]

```
152:     }
```
> إغلاق نطاق الدالة handleBluetoothStatus. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:152]

```
153: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:153]

```
154:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:154]

```
155:      * Get user-friendly status message
```
> تعليق: «يحصل على رسالة حالة ودودة للمستخدم». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:155]

```
156:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:156]

```
157:     fun getStatusMessage(status: BluetoothStatus): String {
```
> يعرّف دالة عامة باسم getStatusMessage (جلب رسالة الحالة) تأخذ وسيطاً باسم status من النوع BluetoothStatus وتُعيد نصاً (String) ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:157]

```
158:         return when (status) {
```
> يُعيد ناتج تعبير when على الموضوع status المفتوح هنا. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:158]

```
159:             BluetoothStatus.ENABLED -> "Bluetooth is enabled and ready"
```
> ينتج النص "Bluetooth is enabled and ready" عند مطابقة BluetoothStatus.ENABLED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:159]

```
160:             BluetoothStatus.DISABLED -> "Bluetooth is disabled. Please enable Bluetooth to use bitchat."
```
> ينتج النص "Bluetooth is disabled. Please enable Bluetooth to use bitchat." عند مطابقة BluetoothStatus.DISABLED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:160]

```
161:             BluetoothStatus.NOT_SUPPORTED -> "This device doesn't support Bluetooth."
```
> ينتج النص "This device doesn't support Bluetooth." عند مطابقة BluetoothStatus.NOT_SUPPORTED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:161]

```
162:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:162]

```
163:     }
```
> إغلاق نطاق الدالة getStatusMessage. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:163]

```
164: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:164]

```
165:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:165]

```
166:      * Get detailed diagnostics (permission-safe)
```
> تعليق: «يحصل على تشخيصات مفصّلة (آمن من ناحية الأذونات)». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:166]

```
167:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:167]

```
168:     fun getDiagnostics(): String {
```
> يعرّف دالة عامة باسم getDiagnostics (جلب التشخيصات) بلا وسائط وتُعيد نصاً (String) ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:168]

```
169:         return buildString {
```
> يُعيد ناتج استدعاء buildString مع تعبير لامبدا يُفتح هنا. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:169]

```
170:             appendLine("Bluetooth Status Diagnostics:")
```
> يستدعي appendLine بالنص "Bluetooth Status Diagnostics:". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:170]

```
171:             appendLine("Adapter available: ${bluetoothAdapter != null}")
```
> يستدعي appendLine بنصٍّ "Adapter available: " متبوع بنتيجة المقارنة bluetoothAdapter != null. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:171]

```
172:             appendLine("Bluetooth supported: ${isBluetoothSupported()}")
```
> يستدعي appendLine بنصٍّ "Bluetooth supported: " متبوع بناتج isBluetoothSupported(). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:172]

```
173:             appendLine("Bluetooth enabled: ${isBluetoothEnabled()}")
```
> يستدعي appendLine بنصٍّ "Bluetooth enabled: " متبوع بناتج isBluetoothEnabled(). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:173]

```
174:             appendLine("Current status: ${checkBluetoothStatus()}")
```
> يستدعي appendLine بنصٍّ "Current status: " متبوع بناتج checkBluetoothStatus(). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:174]

```
175:             
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:175]

```
176:             // Only access adapter details if we have permission and adapter is available
```
> تعليق: «لا تصل إلى تفاصيل المهايئ إلا إذا كان لدينا الإذن والمهايئ متاح». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:176]

```
177:             bluetoothAdapter?.let { adapter ->
```
> يستدعي الدالة let على bluetoothAdapter (إن لم يكن null) بتعبير لامبدا معامله باسم adapter (المهايئ). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:177]

```
178:                 try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:178]

```
179:                     // These calls require BLUETOOTH_CONNECT permission on Android 12+
```
> تعليق: «هذه الاستدعاءات تتطلب إذن BLUETOOTH_CONNECT على أندرويد 12 فأعلى». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:179]

```
180:                     appendLine("Adapter name: ${adapter.name ?: "Unknown"}")
```
> يستدعي appendLine بنصٍّ "Adapter name: " متبوع بقيمة adapter.name أو "Unknown" إن كانت null. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:180]

```
181:                     appendLine("Adapter address: ${adapter.address ?: "Unknown"}")
```
> يستدعي appendLine بنصٍّ "Adapter address: " متبوع بقيمة adapter.address أو "Unknown" إن كانت null. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:181]

```
182:                 } catch (securityException: SecurityException) {
```
> يغلق كتلة try ويفتح كتلة catch تلتقط استثناءً باسم securityException من النوع SecurityException. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:182]

```
183:                     // Permission not granted yet, skip detailed info
```
> تعليق: «الإذن لم يُمنح بعد، تخطَّ المعلومات المفصّلة». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:183]

```
184:                     appendLine("Adapter details: [Permission required]")
```
> يستدعي appendLine بالنص "Adapter details: [Permission required]". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:184]

```
185:                 } catch (e: Exception) {
```
> يغلق كتلة catch السابقة ويفتح كتلة catch أخرى تلتقط استثناءً باسم e من النوع Exception. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:185]

```
186:                     appendLine("Adapter details: [Error: ${e.message}]")
```
> يستدعي appendLine بنصٍّ "Adapter details: [Error: " متبوع بقيمة e.message ثم "]". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:186]

```
187:                 }
```
> إغلاق نطاق كتلة catch الثانية. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:187]

```
188:                 appendLine("Adapter state: ${getAdapterStateName(adapter.state)}")
```
> يستدعي appendLine بنصٍّ "Adapter state: " متبوع بناتج getAdapterStateName(adapter.state). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:188]

```
189:             }
```
> إغلاق نطاق تعبير لامبدا الخاص بـ let. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:189]

```
190:         }
```
> إغلاق نطاق تعبير لامبدا الخاص بـ buildString. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:190]

```
191:     }
```
> إغلاق نطاق الدالة getDiagnostics. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:191]

```
192: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:192]

```
193:     private fun getAdapterStateName(state: Int): String {
```
> يعرّف دالة خاصة باسم getAdapterStateName (جلب اسم حالة المهايئ) تأخذ وسيطاً باسم state (الحالة) من النوع Int وتُعيد نصاً (String) ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:193]

```
194:         return when (state) {
```
> يُعيد ناتج تعبير when على الموضوع state المفتوح هنا. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:194]

```
195:             BluetoothAdapter.STATE_OFF -> "OFF"
```
> ينتج النص "OFF" عند مطابقة القيمة BluetoothAdapter.STATE_OFF. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:195]

```
196:             BluetoothAdapter.STATE_TURNING_ON -> "TURNING_ON"
```
> ينتج النص "TURNING_ON" عند مطابقة القيمة BluetoothAdapter.STATE_TURNING_ON. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:196]

```
197:             BluetoothAdapter.STATE_ON -> "ON"
```
> ينتج النص "ON" عند مطابقة القيمة BluetoothAdapter.STATE_ON. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:197]

```
198:             BluetoothAdapter.STATE_TURNING_OFF -> "TURNING_OFF"
```
> ينتج النص "TURNING_OFF" عند مطابقة القيمة BluetoothAdapter.STATE_TURNING_OFF. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:198]

```
199:             else -> "UNKNOWN($state)"
```
> ينتج في الفرع الافتراضي else النص "UNKNOWN(" متبوعاً بقيمة state ثم ")". [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:199]

```
200:             }
```
> غير مؤكّد — السطر يحوي قوس إغلاق مزاحاً ضمن المدى؛ في الملف الكامل (271 سطراً) هو إغلاق نطاق تعبير when الخاص بـ getAdapterStateName وما بعده مقطوع عن هذا المدى. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:200]
