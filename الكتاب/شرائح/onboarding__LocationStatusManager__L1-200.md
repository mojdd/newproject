# شريحة — app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.onboarding
```
> يعلن انتماء الملف إلى الحزمة (package) ‏`com.bitchat.android.onboarding`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:2]

```
3: import android.content.BroadcastReceiver
```
> يستورد الصنف ‏`BroadcastReceiver` (مستقبِل البث) من ‏`android.content`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:3]

```
4: import android.content.Context
```
> يستورد الصنف ‏`Context` (السياق) من ‏`android.content`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:4]

```
5: import android.content.Intent
```
> يستورد الصنف ‏`Intent` (النيّة) من ‏`android.content`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:5]

```
6: import android.content.IntentFilter
```
> يستورد الصنف ‏`IntentFilter` (مرشّح النيّات) من ‏`android.content`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:6]

```
7: import android.location.LocationManager
```
> يستورد الصنف ‏`LocationManager` (مدير الموقع) من ‏`android.location`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:7]

```
8: import android.os.Build
```
> يستورد الصنف ‏`Build` (معلومات البناء) من ‏`android.os`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:8]

```
9: import android.provider.Settings
```
> يستورد الصنف ‏`Settings` (الإعدادات) من ‏`android.provider`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:9]

```
10: import android.util.Log
```
> يستورد الصنف ‏`Log` (سجل التتبّع) من ‏`android.util`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:10]

```
11: import androidx.activity.ComponentActivity
```
> يستورد الصنف ‏`ComponentActivity` (نشاط المكوّن) من ‏`androidx.activity`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:11]

```
12: import androidx.activity.result.ActivityResultLauncher
```
> يستورد الصنف ‏`ActivityResultLauncher` (مُطلِق نتيجة النشاط) من ‏`androidx.activity.result`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:12]

```
13: import androidx.activity.result.contract.ActivityResultContracts
```
> يستورد الصنف ‏`ActivityResultContracts` (عقود نتيجة النشاط) من ‏`androidx.activity.result.contract`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:13]

```
14: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:14]

```
15: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:15]

```
16:  * Manages Location Services enable/disable state and user prompts
```
> تعليق: يدير حالة تفعيل/تعطيل خدمات الموقع ومطالبات المستخدم. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:16]

```
17:  * Checks location services status on every app startup
```
> تعليق: يفحص حالة خدمات الموقع عند كل تشغيل للتطبيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:17]

```
18:  * Note: This is for system location services, not location permissions
```
> تعليق: ملاحظة: هذا لخدمات الموقع في النظام، وليس لأذونات الموقع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:18]

```
19:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:19]

```
20: class LocationStatusManager(
```
> يعرّف الصنف ‏`LocationStatusManager` (مدير حالة الموقع) ويفتح قائمة معاملات الباني. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:20]

```
21:     private val activity: ComponentActivity,
```
> يعرّف خاصية الباني الخاصة ‏`activity` من نوع ‏`ComponentActivity`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:21]

```
22:     private val context: Context,
```
> يعرّف خاصية الباني الخاصة ‏`context` من نوع ‏`Context`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:22]

```
23:     private val onLocationEnabled: () -> Unit,
```
> يعرّف خاصية الباني الخاصة ‏`onLocationEnabled` (عند تفعيل الموقع) دالةً بلا معاملات تُعيد ‏`Unit`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:23]

```
24:     private val onLocationDisabled: (String) -> Unit
```
> يعرّف خاصية الباني الخاصة ‏`onLocationDisabled` (عند تعطيل الموقع) دالةً تأخذ ‏`String` وتُعيد ‏`Unit`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:24]

```
25: ) {
```
> يُغلق قائمة معاملات الباني ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:25]

```
26: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:26]

```
27:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:27]

```
28:         private const val TAG = "LocationStatusManager"
```
> يعرّف ثابتاً خاصاً ‏`TAG` (وسم السجل) بقيمة نصّية ‏`"LocationStatusManager"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:28]

```
29:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:29]

```
30: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:30]

```
31:     private var locationSettingsLauncher: ActivityResultLauncher<Intent>? = null
```
> يعرّف متغيّراً خاصاً ‏`locationSettingsLauncher` (مُطلِق إعدادات الموقع) من نوع ‏`ActivityResultLauncher<Intent>` القابل للعدم بقيمة ابتدائية ‏`null`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:31]

```
32:     private var locationManager: LocationManager? = null
```
> يعرّف متغيّراً خاصاً ‏`locationManager` من نوع ‏`LocationManager` القابل للعدم بقيمة ابتدائية ‏`null`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:32]

```
33:     private var locationStateReceiver: BroadcastReceiver? = null
```
> يعرّف متغيّراً خاصاً ‏`locationStateReceiver` (مستقبِل حالة الموقع) من نوع ‏`BroadcastReceiver` القابل للعدم بقيمة ابتدائية ‏`null`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:33]

```
34: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:34]

```
35:     init {
```
> يفتح كتلة التهيئة ‏`init`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:35]

```
36:         setupLocationManager()
```
> يستدعي الدالة ‏`setupLocationManager` (تهيئة مدير الموقع). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:36]

```
37:         setupLocationSettingsLauncher()
```
> يستدعي الدالة ‏`setupLocationSettingsLauncher` (تهيئة مُطلِق إعدادات الموقع). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:37]

```
38:         setupLocationStateReceiver()
```
> يستدعي الدالة ‏`setupLocationStateReceiver` (تهيئة مستقبِل حالة الموقع). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:38]

```
39:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:39]

```
40: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:40]

```
41:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:41]

```
42:      * Setup LocationManager reference
```
> تعليق: تهيئة مرجع ‏`LocationManager`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:42]

```
43:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:43]

```
44:     private fun setupLocationManager() {
```
> يعرّف الدالة الخاصة ‏`setupLocationManager` بلا معاملات ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:44]

```
45:         try {
```
> يفتح كتلة ‏`try` (محاولة). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:45]

```
46:             locationManager = context.getSystemService(Context.LOCATION_SERVICE) as LocationManager
```
> يُسند إلى ‏`locationManager` نتيجة ‏`context.getSystemService(Context.LOCATION_SERVICE)` بعد تحويلها (cast) إلى ‏`LocationManager`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:46]

```
47:             Log.d(TAG, "LocationManager initialized: ${locationManager != null}")
```
> يستدعي ‏`Log.d` بالوسم ‏`TAG` ونص ‏`"LocationManager initialized: "` متبوعاً بنتيجة ‏`locationManager != null`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:47]

```
48:         } catch (e: Exception) {
```
> يُغلق ‏`try` ويفتح كتلة ‏`catch` تلتقط استثناءً ‏`e` من نوع ‏`Exception`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:48]

```
49:             Log.e(TAG, "Failed to initialize LocationManager", e)
```
> يستدعي ‏`Log.e` بالوسم ‏`TAG` ونص ‏`"Failed to initialize LocationManager"` والاستثناء ‏`e`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:49]

```
50:             locationManager = null
```
> يُسند ‏`null` إلى ‏`locationManager`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:50]

```
51:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:51]

```
52:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:52]

```
53: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:53]

```
54:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:54]

```
55:      * Setup launcher for location settings request
```
> تعليق: تهيئة المُطلِق لطلب إعدادات الموقع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:55]

```
56:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:56]

```
57:     private fun setupLocationSettingsLauncher() {
```
> يعرّف الدالة الخاصة ‏`setupLocationSettingsLauncher` بلا معاملات ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:57]

```
58:         locationSettingsLauncher = activity.registerForActivityResult(
```
> يُسند إلى ‏`locationSettingsLauncher` نتيجة استدعاء ‏`activity.registerForActivityResult(` ويفتح قائمة الوسائط. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:58]

```
59:             ActivityResultContracts.StartActivityForResult()
```
> يمرّر الوسيط ‏`ActivityResultContracts.StartActivityForResult()` (عقد بدء نشاط لأجل نتيجة). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:59]

```
60:         ) { result ->
```
> يُغلق قائمة الوسائط ويفتح تعبيراً لامبدا بمعامل ‏`result`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:60]

```
61:             val isEnabled = isLocationEnabled()
```
> يعرّف المتغيّر ‏`isEnabled` ويُسند إليه نتيجة استدعاء ‏`isLocationEnabled()`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:61]

```
62:             Log.d(TAG, "Location settings request result: $isEnabled (result code: ${result.resultCode})")
```
> يستدعي ‏`Log.d` بالوسم ‏`TAG` ونص يحوي قيمة ‏`isEnabled` و ‏`result.resultCode`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:62]

```
63:             if (isEnabled) {
```
> يفتح شرط ‏`if` يختبر ‏`isEnabled`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:63]

```
64:                 onLocationEnabled()
```
> يستدعي دالة الرد ‏`onLocationEnabled()`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:64]

```
65:             } else {
```
> يُغلق فرع ‏`if` ويفتح فرع ‏`else`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:65]

```
66:                 onLocationDisabled("Location services are required for Bluetooth scanning on Android. Please enable location services to continue.")
```
> يستدعي ‏`onLocationDisabled` بالنص ‏`"Location services are required for Bluetooth scanning on Android. Please enable location services to continue."`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:66]

```
67:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:67]

```
68:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:68]

```
69:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:69]

```
70: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:70]

```
71:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:71]

```
72:      * Setup broadcast receiver to listen for location settings changes
```
> تعليق: تهيئة مستقبِل البث للاستماع لتغيّرات إعدادات الموقع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:72]

```
73:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:73]

```
74:     private fun setupLocationStateReceiver() {
```
> يعرّف الدالة الخاصة ‏`setupLocationStateReceiver` بلا معاملات ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:74]

```
75:         locationStateReceiver = object : BroadcastReceiver() {
```
> يُسند إلى ‏`locationStateReceiver` كائناً مجهولاً يرث ‏`BroadcastReceiver()`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:75]

```
76:             override fun onReceive(context: Context, intent: Intent) {
```
> يُعيد تعريف الدالة ‏`onReceive` بمعاملين ‏`context` من ‏`Context` و ‏`intent` من ‏`Intent`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:76]

```
77:                 if (intent.action == LocationManager.MODE_CHANGED_ACTION || 
```
> يفتح شرط ‏`if` يختبر مساواة ‏`intent.action` لـ ‏`LocationManager.MODE_CHANGED_ACTION` متبوعاً بمعامل «أو» ‏`||`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:77]

```
78:                     intent.action == LocationManager.PROVIDERS_CHANGED_ACTION) {
```
> يتمّ شرط ‏`if` باختبار مساواة ‏`intent.action` لـ ‏`LocationManager.PROVIDERS_CHANGED_ACTION` ويفتح الكتلة. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:78]

```
79:                     Log.d(TAG, "Location settings changed, checking status")
```
> يستدعي ‏`Log.d` بالوسم ‏`TAG` والنص ‏`"Location settings changed, checking status"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:79]

```
80:                     val isEnabled = isLocationEnabled()
```
> يعرّف المتغيّر ‏`isEnabled` ويُسند إليه نتيجة ‏`isLocationEnabled()`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:80]

```
81:                     if (isEnabled) {
```
> يفتح شرط ‏`if` يختبر ‏`isEnabled`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:81]

```
82:                         onLocationEnabled()
```
> يستدعي دالة الرد ‏`onLocationEnabled()`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:82]

```
83:                     } else {
```
> يُغلق فرع ‏`if` ويفتح فرع ‏`else`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:83]

```
84:                         onLocationDisabled("Location services have been disabled.")
```
> يستدعي ‏`onLocationDisabled` بالنص ‏`"Location services have been disabled."`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:84]

```
85:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:85]

```
86:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:86]

```
87:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:87]

```
88:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:88]

```
89: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:89]

```
90:         // Register receiver for location changes
```
> تعليق: تسجيل المستقبِل لتغيّرات الموقع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:90]

```
91:         val filter = IntentFilter().apply {
```
> يعرّف المتغيّر ‏`filter` ويُسند إليه كائن ‏`IntentFilter()` ضمن كتلة ‏`apply`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:91]

```
92:             addAction(LocationManager.MODE_CHANGED_ACTION)
```
> يستدعي ‏`addAction` بالقيمة ‏`LocationManager.MODE_CHANGED_ACTION`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:92]

```
93:             addAction(LocationManager.PROVIDERS_CHANGED_ACTION)
```
> يستدعي ‏`addAction` بالقيمة ‏`LocationManager.PROVIDERS_CHANGED_ACTION`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:93]

```
94:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:94]

```
95:         context.registerReceiver(locationStateReceiver, filter)
```
> يستدعي ‏`context.registerReceiver` بالمستقبِل ‏`locationStateReceiver` والمرشّح ‏`filter`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:95]

```
96:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:96]

```
97: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:97]

```
98:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:98]

```
99:      * Check if location services are enabled (system-wide setting)
```
> تعليق: فحص ما إذا كانت خدمات الموقع مفعّلة (إعداد على مستوى النظام). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:99]

```
100:      * Uses proper API depending on Android version
```
> تعليق: يستخدم الواجهة البرمجية المناسبة بحسب إصدار أندرويد. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:100]

```
101:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:101]

```
102:     fun isLocationEnabled(): Boolean {
```
> يعرّف الدالة ‏`isLocationEnabled` بلا معاملات تُعيد ‏`Boolean` ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:102]

```
103:         return try {
```
> يُعيد نتيجة كتلة ‏`try`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:103]

```
104:             locationManager?.let { lm ->
```
> يستدعي ‏`let` على ‏`locationManager` بأمان العدم بمعامل ‏`lm`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:104]

```
105:                 if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
```
> يفتح شرط ‏`if` يختبر أن ‏`Build.VERSION.SDK_INT` أكبر من أو يساوي ‏`Build.VERSION_CODES.P`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:105]

```
106:                     // API 28+ (Android 9) - Modern approach
```
> تعليق: واجهة برمجية ‏28 فأعلى (أندرويد ‏9) — المنهج الحديث. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:106]

```
107:                     lm.isLocationEnabled
```
> يقرأ الخاصية ‏`lm.isLocationEnabled` كقيمة الفرع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:107]

```
108:                 } else {
```
> يُغلق فرع ‏`if` ويفتح فرع ‏`else`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:108]

```
109:                     // Older devices - Check individual providers
```
> تعليق: الأجهزة الأقدم — فحص المزوّدين كلٌّ على حدة. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:109]

```
110:                     lm.isProviderEnabled(LocationManager.GPS_PROVIDER) ||
```
> يستدعي ‏`lm.isProviderEnabled(LocationManager.GPS_PROVIDER)` متبوعاً بمعامل «أو» ‏`||`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:110]

```
111:                     lm.isProviderEnabled(LocationManager.NETWORK_PROVIDER)
```
> يستدعي ‏`lm.isProviderEnabled(LocationManager.NETWORK_PROVIDER)` كطرف ثانٍ للمعامل «أو». [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:111]

```
112:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:112]

```
113:             } ?: false
```
> يُغلق كتلة ‏`let` ويستخدم معامل إلفيس ‏`?:` ليُعيد ‏`false` إذا كانت النتيجة عدماً. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:113]

```
114:         } catch (e: Exception) {
```
> يُغلق ‏`try` ويفتح ‏`catch` تلتقط استثناءً ‏`e` من نوع ‏`Exception`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:114]

```
115:             Log.w(TAG, "Error checking location enabled state: ${e.message}")
```
> يستدعي ‏`Log.w` بالوسم ‏`TAG` ونص ‏`"Error checking location enabled state: "` متبوعاً بـ ‏`e.message`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:115]

```
116:             false
```
> يُعيد ‏`false` كقيمة كتلة ‏`catch`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:116]

```
117:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:117]

```
118:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:118]

```
119: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:119]

```
120:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:120]

```
121:      * Check location services status
```
> تعليق: فحص حالة خدمات الموقع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:121]

```
122:      * This should be called on every app startup
```
> تعليق: ينبغي استدعاء هذا عند كل تشغيل للتطبيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:122]

```
123:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:123]

```
124:     fun checkLocationStatus(): LocationStatus {
```
> يعرّف الدالة ‏`checkLocationStatus` بلا معاملات تُعيد ‏`LocationStatus` ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:124]

```
125:         Log.d(TAG, "Checking location services status")
```
> يستدعي ‏`Log.d` بالوسم ‏`TAG` والنص ‏`"Checking location services status"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:125]

```
126:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:126]

```
127:         return when {
```
> يُعيد نتيجة تعبير ‏`when` بلا وسيط ويفتحه. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:127]

```
128:             locationManager == null -> {
```
> يفتح فرع ‏`when` بشرط مساواة ‏`locationManager` لـ ‏`null`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:128]

```
129:                 Log.e(TAG, "LocationManager not available on this device")
```
> يستدعي ‏`Log.e` بالوسم ‏`TAG` والنص ‏`"LocationManager not available on this device"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:129]

```
130:                 LocationStatus.NOT_AVAILABLE
```
> يُعيد ‏`LocationStatus.NOT_AVAILABLE` كقيمة الفرع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:130]

```
131:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:131]

```
132:             !isLocationEnabled() -> {
```
> يفتح فرع ‏`when` بشرط نفي نتيجة ‏`isLocationEnabled()`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:132]

```
133:                 Log.w(TAG, "Location services are disabled")
```
> يستدعي ‏`Log.w` بالوسم ‏`TAG` والنص ‏`"Location services are disabled"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:133]

```
134:                 LocationStatus.DISABLED
```
> يُعيد ‏`LocationStatus.DISABLED` كقيمة الفرع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:134]

```
135:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:135]

```
136:             else -> {
```
> يفتح الفرع الافتراضي ‏`else` في ‏`when`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:136]

```
137:                 Log.d(TAG, "Location services are enabled and ready")
```
> يستدعي ‏`Log.d` بالوسم ‏`TAG` والنص ‏`"Location services are enabled and ready"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:137]

```
138:                 LocationStatus.ENABLED
```
> يُعيد ‏`LocationStatus.ENABLED` كقيمة الفرع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:138]

```
139:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:139]

```
140:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:140]

```
141:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:141]

```
142: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:142]

```
143:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:143]

```
144:      * Request user to enable location services
```
> تعليق: طلب من المستخدم تفعيل خدمات الموقع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:144]

```
145:      * Opens system location settings screen
```
> تعليق: يفتح شاشة إعدادات موقع النظام. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:145]

```
146:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:146]

```
147:     fun requestEnableLocation() {
```
> يعرّف الدالة ‏`requestEnableLocation` بلا معاملات ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:147]

```
148:         Log.d(TAG, "Requesting user to enable location services")
```
> يستدعي ‏`Log.d` بالوسم ‏`TAG` والنص ‏`"Requesting user to enable location services"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:148]

```
149:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:149]

```
150:         try {
```
> يفتح كتلة ‏`try`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:150]

```
151:             val enableLocationIntent = Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS)
```
> يعرّف المتغيّر ‏`enableLocationIntent` ويُسند إليه كائن ‏`Intent` بالوسيط ‏`Settings.ACTION_LOCATION_SOURCE_SETTINGS`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:151]

```
152:             locationSettingsLauncher?.launch(enableLocationIntent)
```
> يستدعي ‏`launch` بأمان العدم على ‏`locationSettingsLauncher` بالوسيط ‏`enableLocationIntent`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:152]

```
153:         } catch (e: Exception) {
```
> يُغلق ‏`try` ويفتح ‏`catch` تلتقط استثناءً ‏`e` من نوع ‏`Exception`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:153]

```
154:             Log.e(TAG, "Failed to request location enable", e)
```
> يستدعي ‏`Log.e` بالوسم ‏`TAG` والنص ‏`"Failed to request location enable"` والاستثناء ‏`e`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:154]

```
155:             onLocationDisabled("Failed to open location settings: ${e.message}")
```
> يستدعي ‏`onLocationDisabled` بنص ‏`"Failed to open location settings: "` متبوعاً بـ ‏`e.message`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:155]

```
156:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:156]

```
157:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:157]

```
158: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:158]

```
159:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:159]

```
160:      * Handle location status check result
```
> تعليق: معالجة نتيجة فحص حالة الموقع. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:160]

```
161:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:161]

```
162:     fun handleLocationStatus(status: LocationStatus) {
```
> يعرّف الدالة ‏`handleLocationStatus` بمعامل ‏`status` من نوع ‏`LocationStatus` ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:162]

```
163:         when (status) {
```
> يفتح تعبير ‏`when` على الوسيط ‏`status`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:163]

```
164:             LocationStatus.ENABLED -> {
```
> يفتح فرع ‏`when` لقيمة ‏`LocationStatus.ENABLED`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:164]

```
165:                 Log.d(TAG, "Location services enabled, proceeding")
```
> يستدعي ‏`Log.d` بالوسم ‏`TAG` والنص ‏`"Location services enabled, proceeding"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:165]

```
166:                 onLocationEnabled()
```
> يستدعي دالة الرد ‏`onLocationEnabled()`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:166]

```
167:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:167]

```
168:             LocationStatus.DISABLED -> {
```
> يفتح فرع ‏`when` لقيمة ‏`LocationStatus.DISABLED`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:168]

```
169:                 Log.d(TAG, "Location services disabled, requesting enable")
```
> يستدعي ‏`Log.d` بالوسم ‏`TAG` والنص ‏`"Location services disabled, requesting enable"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:169]

```
170:                 requestEnableLocation()
```
> يستدعي الدالة ‏`requestEnableLocation()`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:170]

```
171:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:171]

```
172:             LocationStatus.NOT_AVAILABLE -> {
```
> يفتح فرع ‏`when` لقيمة ‏`LocationStatus.NOT_AVAILABLE`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:172]

```
173:                 Log.e(TAG, "Location services not available")
```
> يستدعي ‏`Log.e` بالوسم ‏`TAG` والنص ‏`"Location services not available"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:173]

```
174:                 onLocationDisabled("Location services are not available on this device.")
```
> يستدعي ‏`onLocationDisabled` بالنص ‏`"Location services are not available on this device."`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:174]

```
175:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:175]

```
176:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:176]

```
177:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:177]

```
178: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:178]

```
179:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:179]

```
180:      * Get user-friendly status message
```
> تعليق: الحصول على رسالة حالة سهلة على المستخدم. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:180]

```
181:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:181]

```
182:     fun getStatusMessage(status: LocationStatus): String {
```
> يعرّف الدالة ‏`getStatusMessage` بمعامل ‏`status` من نوع ‏`LocationStatus` تُعيد ‏`String` ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:182]

```
183:         return when (status) {
```
> يُعيد نتيجة تعبير ‏`when` على الوسيط ‏`status`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:183]

```
184:             LocationStatus.ENABLED -> "Location services are enabled and ready"
```
> يُعيد لقيمة ‏`LocationStatus.ENABLED` النص ‏`"Location services are enabled and ready"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:184]

```
185:             LocationStatus.DISABLED -> "Location services are disabled. Please enable location services for Bluetooth scanning."
```
> يُعيد لقيمة ‏`LocationStatus.DISABLED` النص ‏`"Location services are disabled. Please enable location services for Bluetooth scanning."`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:185]

```
186:             LocationStatus.NOT_AVAILABLE -> "Location services are not available on this device."
```
> يُعيد لقيمة ‏`LocationStatus.NOT_AVAILABLE` النص ‏`"Location services are not available on this device."`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:186]

```
187:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:187]

```
188:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:188]

```
189: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:189]

```
190:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:190]

```
191:      * Get detailed diagnostics
```
> تعليق: الحصول على تشخيصات مفصّلة. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:191]

```
192:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:192]

```
193:     fun getDiagnostics(): String {
```
> يعرّف الدالة ‏`getDiagnostics` بلا معاملات تُعيد ‏`String` ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:193]

```
194:         return buildString {
```
> يُعيد نتيجة استدعاء ‏`buildString` ويفتح كتلتها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:194]

```
195:             appendLine("Location Services Status Diagnostics:")
```
> يستدعي ‏`appendLine` بالنص ‏`"Location Services Status Diagnostics:"`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:195]

```
196:             appendLine("LocationManager available: ${locationManager != null}")
```
> يستدعي ‏`appendLine` بنص ‏`"LocationManager available: "` متبوعاً بنتيجة ‏`locationManager != null`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:196]

```
197:             appendLine("Location services enabled: ${isLocationEnabled()}")
```
> يستدعي ‏`appendLine` بنص ‏`"Location services enabled: "` متبوعاً بنتيجة ‏`isLocationEnabled()`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:197]

```
198:             appendLine("Current status: ${checkLocationStatus()}")
```
> يستدعي ‏`appendLine` بنص ‏`"Current status: "` متبوعاً بنتيجة ‏`checkLocationStatus()`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:198]

```
199:             appendLine("Android version: ${Build.VERSION.SDK_INT}")
```
> يستدعي ‏`appendLine` بنص ‏`"Android version: "` متبوعاً بقيمة ‏`Build.VERSION.SDK_INT`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:199]

```
200: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:200]
