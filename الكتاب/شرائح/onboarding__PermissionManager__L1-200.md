# شريحة — app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.onboarding
```
> يُعرّف الحزمة (package) باسم com.bitchat.android.onboarding. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:2]

```
3: import android.Manifest
```
> يستورد (import) الصنف android.Manifest. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:3]

```
4: import android.content.Context
```
> يستورد الصنف android.content.Context (السياق). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:4]

```
5: import android.content.pm.PackageManager
```
> يستورد الصنف android.content.pm.PackageManager (مدير الحِزَم). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:5]

```
6: import android.os.Build
```
> يستورد الصنف android.os.Build (معلومات البناء). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:6]

```
7: import android.os.PowerManager
```
> يستورد الصنف android.os.PowerManager (مدير الطاقة). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:7]

```
8: import android.util.Log
```
> يستورد الصنف android.util.Log (السجل). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:8]

```
9: import androidx.core.content.ContextCompat
```
> يستورد الصنف androidx.core.content.ContextCompat (توافق السياق). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:9]

```
10: import com.bitchat.android.R
```
> يستورد الصنف com.bitchat.android.R (مصادر التطبيق). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:11]

```
12: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:12]

```
13:  * Centralized permission management for bitchat app
```
> تعليق: إدارة أذونات مركزية لتطبيق bitchat. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:13]

```
14:  * Handles all Bluetooth and notification permissions required for the app to function
```
> تعليق: يتولّى كل أذونات البلوتوث والإشعارات اللازمة لعمل التطبيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:14]

```
15:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:15]

```
16: class PermissionManager(private val context: Context) {
```
> يُعرّف الصنف مدير الأذونات (PermissionManager) بمُنشئ يأخذ مُعاملاً خاصاً اسمه context من نوع Context، ويفتح نطاق الصنف. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:17]

```
18:     companion object {
```
> يفتح كائن مُرافق (companion object) للصنف. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:18]

```
19:         private const val TAG = "PermissionManager"
```
> يُعرّف ثابتاً خاصاً TAG بقيمة نصية "PermissionManager". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:19]

```
20:         private const val PREFS_NAME = "bitchat_permissions"
```
> يُعرّف ثابتاً خاصاً PREFS_NAME (اسم التفضيلات) بقيمة نصية "bitchat_permissions". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:20]

```
21:         private const val KEY_FIRST_TIME_COMPLETE = "first_time_onboarding_complete"
```
> يُعرّف ثابتاً خاصاً KEY_FIRST_TIME_COMPLETE (مفتاح اكتمال أول مرة) بقيمة نصية "first_time_onboarding_complete". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:21]

```
22:     }
```
> إغلاق نطاق الكائن المُرافق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:22]

```
23: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:23]

```
24:     private val sharedPrefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يُعرّف خاصية خاصة sharedPrefs (التفضيلات المشتركة) ويسندها بنتيجة استدعاء context.getSharedPreferences بالاسم PREFS_NAME والنمط Context.MODE_PRIVATE. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:25]

```
26:     private fun shouldRequireWifiAwarePermission(): Boolean {
```
> يُعرّف دالة خاصة shouldRequireWifiAwarePermission (هل يلزم إذن واي‑فاي أوير) تُعيد Boolean، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:26]

```
27:         if (Build.VERSION.SDK_INT < Build.VERSION_CODES.TIRAMISU) return false
```
> إذا كان Build.VERSION.SDK_INT أصغر من Build.VERSION_CODES.TIRAMISU فيُعيد false. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:27]

```
28:         val enabled = try {
```
> يُعرّف متغيراً enabled (مُفعَّل) ويُسنده بنتيجة كتلة try، ويفتح كتلة try. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:28]

```
29:             com.bitchat.android.ui.debug.DebugPreferenceManager.getWifiAwareEnabled(false)
```
> يستدعي com.bitchat.android.ui.debug.DebugPreferenceManager.getWifiAwareEnabled بالمُعامل false. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:29]

```
30:         } catch (_: Exception) {
```
> يلتقط استثناءً (Exception) دون تسميته، ويفتح كتلة catch. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:30]

```
31:             false
```
> يُعيد القيمة false كنتيجة لكتلة catch. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:31]

```
32:         }
```
> إغلاق نطاق كتلة try/catch. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:32]

```
33:         if (!enabled) return false
```
> إذا كان enabled غير صحيح (منفيّاً) فيُعيد false. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:33]

```
34: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:34]

```
35:         return try {
```
> يُعيد نتيجة كتلة try، ويفتح كتلة try. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:35]

```
36:             com.bitchat.android.wifiaware.WifiAwareSupport.isSupported(context)
```
> يستدعي com.bitchat.android.wifiaware.WifiAwareSupport.isSupported بالمُعامل context. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:36]

```
37:         } catch (_: Exception) {
```
> يلتقط استثناءً (Exception) دون تسميته، ويفتح كتلة catch. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:37]

```
38:             false
```
> يُعيد القيمة false كنتيجة لكتلة catch. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:38]

```
39:         }
```
> إغلاق نطاق كتلة try/catch. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:39]

```
40:     }
```
> إغلاق نطاق الدالة shouldRequireWifiAwarePermission. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:40]

```
41: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:41]

```
42:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:42]

```
43:      * Check if this is the first time the user is launching the app
```
> تعليق: التحقّق إن كانت هذه أول مرة يُشغّل فيها المستخدم التطبيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:43]

```
44:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:44]

```
45:     fun isFirstTimeLaunch(): Boolean {
```
> يُعرّف دالة isFirstTimeLaunch (هل أول تشغيل) تُعيد Boolean، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:45]

```
46:         return !sharedPrefs.getBoolean(KEY_FIRST_TIME_COMPLETE, false)
```
> يُعيد نفي القيمة المنطقية المقروءة من sharedPrefs.getBoolean بالمفتاح KEY_FIRST_TIME_COMPLETE والقيمة الافتراضية false. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:46]

```
47:     }
```
> إغلاق نطاق الدالة isFirstTimeLaunch. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:47]

```
48: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:48]

```
49:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:49]

```
50:      * Mark the first-time onboarding as complete
```
> تعليق: وضع علامة على اكتمال إعداد أول مرة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:50]

```
51:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:51]

```
52:     fun markOnboardingComplete() {
```
> يُعرّف دالة markOnboardingComplete (وسم اكتمال الإعداد) بلا قيمة إرجاع معلنة، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:52]

```
53:         sharedPrefs.edit()
```
> يستدعي sharedPrefs.edit() لبدء تحرير التفضيلات. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:53]

```
54:             .putBoolean(KEY_FIRST_TIME_COMPLETE, true)
```
> يستدعي putBoolean على محرّر التفضيلات بالمفتاح KEY_FIRST_TIME_COMPLETE والقيمة true. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:54]

```
55:             .apply()
```
> يستدعي apply() لتطبيق التغييرات على التفضيلات. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:55]

```
56:         Log.d(TAG, "First-time onboarding marked as complete")
```
> يستدعي Log.d بالوسم TAG والرسالة "First-time onboarding marked as complete". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:56]

```
57:     }
```
> إغلاق نطاق الدالة markOnboardingComplete. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:57]

```
58: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:58]

```
59:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:59]

```
60:      * Get required permissions that can be requested together.
```
> تعليق: الحصول على الأذونات اللازمة التي يمكن طلبها معاً. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:60]

```
61:      * Background location is handled separately to ensure correct request order.
```
> تعليق: موقع الخلفية يُعالَج على حدة لضمان ترتيب الطلب الصحيح. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:61]

```
62:      * Note: Notification permission is optional and not included here,
```
> تعليق: ملاحظة: إذن الإشعار اختياري وغير مُضمَّن هنا. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:62]

```
63:      * so the app works without notification access.
```
> تعليق: لذا يعمل التطبيق دون صلاحية الإشعارات. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:63]

```
64:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:64]

```
65:     fun getRequiredPermissions(): List<String> {
```
> يُعرّف دالة getRequiredPermissions (الأذونات اللازمة) تُعيد List<String>، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:65]

```
66:         val permissions = mutableListOf<String>()
```
> يُعرّف متغيراً permissions ويُسنده بقائمة نصية قابلة للتعديل فارغة عبر mutableListOf<String>(). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:66]

```
67: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:67]

```
68:         // Bluetooth permissions (API level dependent)
```
> تعليق: أذونات البلوتوث (معتمدة على مستوى الـ API). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:68]

```
69:         if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
```
> إذا كان Build.VERSION.SDK_INT أكبر من أو يساوي Build.VERSION_CODES.S فيفتح نطاق الشرط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:69]

```
70:             permissions.addAll(listOf(
```
> يستدعي permissions.addAll بقائمة مُنشأة عبر listOf، ويفتح وسائط القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:70]

```
71:                 Manifest.permission.BLUETOOTH_ADVERTISE,
```
> يُضيف العنصر Manifest.permission.BLUETOOTH_ADVERTISE إلى القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:71]

```
72:                 Manifest.permission.BLUETOOTH_CONNECT,
```
> يُضيف العنصر Manifest.permission.BLUETOOTH_CONNECT إلى القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:72]

```
73:                 Manifest.permission.BLUETOOTH_SCAN
```
> يُضيف العنصر Manifest.permission.BLUETOOTH_SCAN إلى القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:73]

```
74:             ))
```
> إغلاق وسائط listOf واستدعاء addAll. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:74]

```
75:         } else {
```
> إغلاق نطاق فرع if وفتح نطاق فرع else. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:75]

```
76:             permissions.addAll(listOf(
```
> يستدعي permissions.addAll بقائمة مُنشأة عبر listOf، ويفتح وسائط القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:76]

```
77:                 Manifest.permission.BLUETOOTH,
```
> يُضيف العنصر Manifest.permission.BLUETOOTH إلى القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:77]

```
78:                 Manifest.permission.BLUETOOTH_ADMIN
```
> يُضيف العنصر Manifest.permission.BLUETOOTH_ADMIN إلى القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:78]

```
79:             ))
```
> إغلاق وسائط listOf واستدعاء addAll. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:79]

```
80:         }
```
> إغلاق نطاق فرع else. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:80]

```
81: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:81]

```
82:         // Location permissions (required for Bluetooth LE scanning)
```
> تعليق: أذونات الموقع (لازمة لمسح بلوتوث منخفض الطاقة LE). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:82]

```
83:         permissions.addAll(listOf(
```
> يستدعي permissions.addAll بقائمة مُنشأة عبر listOf، ويفتح وسائط القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:83]

```
84:             Manifest.permission.ACCESS_COARSE_LOCATION,
```
> يُضيف العنصر Manifest.permission.ACCESS_COARSE_LOCATION إلى القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:84]

```
85:             Manifest.permission.ACCESS_FINE_LOCATION
```
> يُضيف العنصر Manifest.permission.ACCESS_FINE_LOCATION إلى القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:85]

```
86:         ))
```
> إغلاق وسائط listOf واستدعاء addAll. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:86]

```
87: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:87]

```
88:         // Wi‑Fi Aware: Android 13+ requires NEARBY_WIFI_DEVICES runtime permission
```
> تعليق: واي‑فاي أوير: أندرويد 13 فأعلى يتطلّب إذن وقت التشغيل NEARBY_WIFI_DEVICES. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:88]

```
89:         if (shouldRequireWifiAwarePermission()) {
```
> إذا أعادت shouldRequireWifiAwarePermission() القيمة true فيفتح نطاق الشرط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:89]

```
90:             permissions.add(Manifest.permission.NEARBY_WIFI_DEVICES)
```
> يستدعي permissions.add بالعنصر Manifest.permission.NEARBY_WIFI_DEVICES. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:90]

```
91:         }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:91]

```
92: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:92]

```
93:         // Notification permission intentionally excluded to keep it optional
```
> تعليق: إذن الإشعار مُستثنى عمداً لإبقائه اختيارياً. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:93]

```
94: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:94]

```
95:         return permissions
```
> يُعيد القائمة permissions. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:95]

```
96:     }
```
> إغلاق نطاق الدالة getRequiredPermissions. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:96]

```
97: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:97]

```
98:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:98]

```
99:      * Background location permission is required on Android 10+ for background BLE scanning.
```
> تعليق: إذن موقع الخلفية لازم على أندرويد 10 فأعلى لمسح بلوتوث LE في الخلفية. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:99]

```
100:      * Must be requested after foreground location permissions are granted.
```
> تعليق: يجب طلبه بعد مَنح أذونات موقع المقدّمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:100]

```
101:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:101]

```
102:     fun needsBackgroundLocationPermission(): Boolean {
```
> يُعرّف دالة needsBackgroundLocationPermission (هل يلزم إذن موقع الخلفية) تُعيد Boolean، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:102]

```
103:         return Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q
```
> يُعيد نتيجة المقارنة: هل Build.VERSION.SDK_INT أكبر من أو يساوي Build.VERSION_CODES.Q. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:103]

```
104:     }
```
> إغلاق نطاق الدالة needsBackgroundLocationPermission. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:104]

```
105: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:105]

```
106:     fun getBackgroundLocationPermission(): String? {
```
> يُعرّف دالة getBackgroundLocationPermission (إذن موقع الخلفية) تُعيد String? (نصاً قابلاً لأن يكون فارغاً)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:106]

```
107:         return if (needsBackgroundLocationPermission()) {
```
> يُعيد نتيجة تعبير if، فإذا أعادت needsBackgroundLocationPermission() القيمة true يفتح فرع الإرجاع. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:107]

```
108:             Manifest.permission.ACCESS_BACKGROUND_LOCATION
```
> يُعيد القيمة Manifest.permission.ACCESS_BACKGROUND_LOCATION. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:108]

```
109:         } else {
```
> إغلاق فرع if وفتح فرع else. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:109]

```
110:             null
```
> يُعيد القيمة null. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:110]

```
111:         }
```
> إغلاق فرع else. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:111]

```
112:     }
```
> إغلاق نطاق الدالة getBackgroundLocationPermission. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:112]

```
113: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:113]

```
114:     fun isBackgroundLocationGranted(): Boolean {
```
> يُعرّف دالة isBackgroundLocationGranted (هل مُنح موقع الخلفية) تُعيد Boolean، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:114]

```
115:         val permission = getBackgroundLocationPermission() ?: return true
```
> يُعرّف متغيراً permission ويُسنده بنتيجة getBackgroundLocationPermission()، فإن كانت null يُعيد true عبر عامل elvis. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:115]

```
116:         return isPermissionGranted(permission)
```
> يُعيد نتيجة استدعاء isPermissionGranted بالمُعامل permission. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:116]

```
117:     }
```
> إغلاق نطاق الدالة isBackgroundLocationGranted. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:117]

```
118: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:118]

```
119:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:119]

```
120:      * Get optional permissions that improve the experience but aren't required.
```
> تعليق: الحصول على أذونات اختيارية تُحسّن التجربة لكنها غير لازمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:120]

```
121:      * Currently includes POST_NOTIFICATIONS on Android 13+.
```
> تعليق: تتضمّن حالياً POST_NOTIFICATIONS على أندرويد 13 فأعلى. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:121]

```
122:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:122]

```
123:     fun getOptionalPermissions(): List<String> {
```
> يُعرّف دالة getOptionalPermissions (الأذونات الاختيارية) تُعيد List<String>، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:123]

```
124:         val optional = mutableListOf<String>()
```
> يُعرّف متغيراً optional ويُسنده بقائمة نصية قابلة للتعديل فارغة عبر mutableListOf<String>(). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:124]

```
125:         // Notifications on Android 13+
```
> تعليق: الإشعارات على أندرويد 13 فأعلى. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:125]

```
126:         if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
```
> إذا كان Build.VERSION.SDK_INT أكبر من أو يساوي Build.VERSION_CODES.TIRAMISU فيفتح نطاق الشرط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:126]

```
127:             optional.add(Manifest.permission.POST_NOTIFICATIONS)
```
> يستدعي optional.add بالعنصر Manifest.permission.POST_NOTIFICATIONS. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:127]

```
128:         }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:128]

```
129:         return optional
```
> يُعيد القائمة optional. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:129]

```
130:     }
```
> إغلاق نطاق الدالة getOptionalPermissions. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:130]

```
131: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:131]

```
132:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:132]

```
133:      * Check if a specific permission is granted
```
> تعليق: التحقّق إن كان إذن مُعيّن قد مُنح. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:133]

```
134:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:134]

```
135:     fun isPermissionGranted(permission: String): Boolean {
```
> يُعرّف دالة isPermissionGranted (هل مُنح الإذن) تأخذ مُعاملاً permission من نوع String وتُعيد Boolean، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:135]

```
136:         return ContextCompat.checkSelfPermission(context, permission) == PackageManager.PERMISSION_GRANTED
```
> يُعيد نتيجة مقارنة ContextCompat.checkSelfPermission(context, permission) بالمساواة مع PackageManager.PERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:136]

```
137:     }
```
> إغلاق نطاق الدالة isPermissionGranted. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:137]

```
138: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:138]

```
139:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:139]

```
140:      * Check if all required permissions are granted (background location is optional).
```
> تعليق: التحقّق إن كانت كل الأذونات اللازمة قد مُنحت (موقع الخلفية اختياري). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:140]

```
141:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:141]

```
142:     fun areAllPermissionsGranted(): Boolean {
```
> يُعرّف دالة areAllPermissionsGranted (هل مُنحت كل الأذونات) تُعيد Boolean، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:142]

```
143:         return areRequiredPermissionsGranted()
```
> يُعيد نتيجة استدعاء areRequiredPermissionsGranted(). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:143]

```
144:     }
```
> إغلاق نطاق الدالة areAllPermissionsGranted. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:144]

```
145: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:145]

```
146:     fun areRequiredPermissionsGranted(): Boolean {
```
> يُعرّف دالة areRequiredPermissionsGranted (هل مُنحت الأذونات اللازمة) تُعيد Boolean، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:146]

```
147:         return getRequiredPermissions().all { isPermissionGranted(it) }
```
> يُعيد نتيجة all على getRequiredPermissions()، حيث يتحقّق لكل عنصر it من isPermissionGranted(it). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:147]

```
148:     }
```
> إغلاق نطاق الدالة areRequiredPermissionsGranted. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:148]

```
149: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:149]

```
150:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:150]

```
151:      * Check if battery optimization is disabled for this app
```
> تعليق: التحقّق إن كان تحسين البطارية مُعطّلاً لهذا التطبيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:151]

```
152:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:152]

```
153:     fun isBatteryOptimizationDisabled(): Boolean {
```
> يُعرّف دالة isBatteryOptimizationDisabled (هل تحسين البطارية مُعطّل) تُعيد Boolean، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:153]

```
154:         return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
```
> يُعيد نتيجة تعبير if، فإذا كان Build.VERSION.SDK_INT أكبر من أو يساوي Build.VERSION_CODES.M يفتح فرع if. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:154]

```
155:             try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:155]

```
156:                 val powerManager = context.getSystemService(Context.POWER_SERVICE) as PowerManager
```
> يُعرّف متغيراً powerManager ويُسنده بنتيجة context.getSystemService(Context.POWER_SERVICE) مع تحويلها (cast) إلى PowerManager. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:156]

```
157:                 powerManager.isIgnoringBatteryOptimizations(context.packageName)
```
> يستدعي powerManager.isIgnoringBatteryOptimizations بالمُعامل context.packageName ويُعيد نتيجته. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:157]

```
158:             } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) باسم e، ويفتح كتلة catch. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:158]

```
159:                 Log.e(TAG, "Error checking battery optimization status", e)
```
> يستدعي Log.e بالوسم TAG والرسالة "Error checking battery optimization status" والاستثناء e. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:159]

```
160:                 false
```
> يُعيد القيمة false كنتيجة لكتلة catch. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:160]

```
161:             }
```
> إغلاق نطاق كتلة try/catch. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:161]

```
162:         } else {
```
> إغلاق فرع if وفتح فرع else. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:162]

```
163:             // Battery optimization doesn't exist on Android < 6.0
```
> تعليق: تحسين البطارية غير موجود على أندرويد أقل من 6.0. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:163]

```
164:             true
```
> يُعيد القيمة true كنتيجة لفرع else. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:164]

```
165:         }
```
> إغلاق فرع else. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:165]

```
166:     }
```
> إغلاق نطاق الدالة isBatteryOptimizationDisabled. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:166]

```
167: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:167]

```
168:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:168]

```
169:      * Check if battery optimization is supported on this device
```
> تعليق: التحقّق إن كان تحسين البطارية مدعوماً على هذا الجهاز. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:169]

```
170:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:170]

```
171:     fun isBatteryOptimizationSupported(): Boolean {
```
> يُعرّف دالة isBatteryOptimizationSupported (هل تحسين البطارية مدعوم) تُعيد Boolean، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:171]

```
172:         return Build.VERSION.SDK_INT >= Build.VERSION_CODES.M
```
> يُعيد نتيجة المقارنة: هل Build.VERSION.SDK_INT أكبر من أو يساوي Build.VERSION_CODES.M. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:172]

```
173:     }
```
> إغلاق نطاق الدالة isBatteryOptimizationSupported. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:173]

```
174: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:174]

```
175:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:175]

```
176:      * Get the list of permissions that are missing
```
> تعليق: الحصول على قائمة الأذونات المفقودة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:176]

```
177:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:177]

```
178:     fun getMissingPermissions(): List<String> {
```
> يُعرّف دالة getMissingPermissions (الأذونات المفقودة) تُعيد List<String>، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:178]

```
179:         return getRequiredPermissions().filter { !isPermissionGranted(it) }
```
> يُعيد نتيجة filter على getRequiredPermissions()، مُبقياً العناصر it التي لم يُمنح إذنها (نفي isPermissionGranted(it)). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:179]

```
180:     }
```
> إغلاق نطاق الدالة getMissingPermissions. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:180]

```
181: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:181]

```
182:     fun getMissingBackgroundLocationPermission(): List<String> {
```
> يُعرّف دالة getMissingBackgroundLocationPermission (إذن موقع الخلفية المفقود) تُعيد List<String>، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:182]

```
183:         val permission = getBackgroundLocationPermission() ?: return emptyList()
```
> يُعرّف متغيراً permission ويُسنده بنتيجة getBackgroundLocationPermission()، فإن كانت null يُعيد قائمة فارغة emptyList() عبر عامل elvis. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:183]

```
184:         return if (isPermissionGranted(permission)) emptyList() else listOf(permission)
```
> يُعيد قائمة فارغة emptyList() إن كان isPermissionGranted(permission) صحيحاً، وإلا قائمة listOf(permission). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:184]

```
185:     }
```
> إغلاق نطاق الدالة getMissingBackgroundLocationPermission. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:185]

```
186: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:186]

```
187:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:187]

```
188:      * Get categorized permission information for display
```
> تعليق: الحصول على معلومات الأذونات مُصنّفة للعرض. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:188]

```
189:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:189]

```
190:     fun getCategorizedPermissions(): List<PermissionCategory> {
```
> يُعرّف دالة getCategorizedPermissions (الأذونات المُصنّفة) تُعيد List<PermissionCategory>، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:190]

```
191:         val categories = mutableListOf<PermissionCategory>()
```
> يُعرّف متغيراً categories ويُسنده بقائمة قابلة للتعديل فارغة من نوع PermissionCategory عبر mutableListOf<PermissionCategory>(). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:191]

```
192: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:192]

```
193:         // Bluetooth/Nearby Devices category
```
> تعليق: صنف البلوتوث/الأجهزة القريبة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:193]

```
194:         val bluetoothPermissions = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
```
> يُعرّف متغيراً bluetoothPermissions ويُسنده بنتيجة تعبير if، فإذا كان Build.VERSION.SDK_INT أكبر من أو يساوي Build.VERSION_CODES.S يفتح فرع if. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:194]

```
195:             listOf(
```
> يُنشئ قائمة عبر listOf ويفتح وسائطها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:195]

```
196:                 Manifest.permission.BLUETOOTH_ADVERTISE,
```
> يُدرج العنصر Manifest.permission.BLUETOOTH_ADVERTISE في القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:196]

```
197:                 Manifest.permission.BLUETOOTH_CONNECT,
```
> يُدرج العنصر Manifest.permission.BLUETOOTH_CONNECT في القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:197]

```
198:                 Manifest.permission.BLUETOOTH_SCAN
```
> يُدرج العنصر Manifest.permission.BLUETOOTH_SCAN في القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:198]

```
199:             )
```
> إغلاق وسائط listOf. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:199]

```
200:         } else {
```
> إغلاق فرع if وفتح فرع else. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:200]
