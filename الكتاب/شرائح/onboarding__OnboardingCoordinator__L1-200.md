# شريحة — app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt (الأسطر 1–200)

```
1: package com.bitchat.android.onboarding
```
> يحدّد الحزمة (package) التي ينتمي إليها الملف باسم `com.bitchat.android.onboarding`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:2]

```
3: import android.app.Activity
```
> يستورد الصنف `Activity` من حزمة `android.app`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:3]

```
4: import android.content.Context
```
> يستورد الصنف `Context` من حزمة `android.content`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:4]

```
5: import android.content.Intent
```
> يستورد الصنف `Intent` من حزمة `android.content`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:5]

```
6: import android.provider.Settings
```
> يستورد الصنف `Settings` من حزمة `android.provider`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:6]

```
7: import android.util.Log
```
> يستورد الصنف `Log` من حزمة `android.util`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:7]

```
8: import androidx.activity.ComponentActivity
```
> يستورد الصنف `ComponentActivity` من حزمة `androidx.activity`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:8]

```
9: import androidx.activity.result.ActivityResultLauncher
```
> يستورد الصنف `ActivityResultLauncher` (مُطلِق نتيجة النشاط) من حزمة `androidx.activity.result`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:9]

```
10: import androidx.activity.result.contract.ActivityResultContracts
```
> يستورد الصنف `ActivityResultContracts` (عقود نتيجة النشاط) من حزمة `androidx.activity.result.contract`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:10]

```
11: import androidx.lifecycle.lifecycleScope
```
> يستورد الخاصية `lifecycleScope` (نطاق دورة الحياة) من حزمة `androidx.lifecycle`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:11]

```
12: import kotlinx.coroutines.launch
```
> يستورد الدالة `launch` من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:12]

```
13: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:13]

```
14: /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:14]

```
15:  * Coordinates the complete onboarding flow including permission explanation,
```
> تعليق: «ينسّق مسار التهيئة الكامل بما في ذلك شرح الأذونات،». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:15]

```
16:  * permission requests, and initialization of the mesh service
```
> تعليق: «وطلبات الأذونات، وتهيئة خدمة الشبكة المتشابكة (mesh)». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:16]

```
17:  */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:17]

```
18: class OnboardingCoordinator(
```
> يعرّف الصنف `OnboardingCoordinator` (منسّق التهيئة) ويبدأ قائمة معاملات المُنشئ (constructor). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:18]

```
19:     private val activity: ComponentActivity,
```
> يعرّف معامِلاً ثابتاً خاصّاً باسم `activity` من النوع `ComponentActivity`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:19]

```
20:     private val permissionManager: PermissionManager,
```
> يعرّف معامِلاً ثابتاً خاصّاً باسم `permissionManager` (مدير الأذونات) من النوع `PermissionManager`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:20]

```
21:     private val onOnboardingComplete: () -> Unit,
```
> يعرّف معامِلاً ثابتاً خاصّاً باسم `onOnboardingComplete` (عند اكتمال التهيئة) من نوع دالّة بلا وُسطاء تُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:21]

```
22:     private val onBackgroundLocationRequired: () -> Unit,
```
> يعرّف معامِلاً ثابتاً خاصّاً باسم `onBackgroundLocationRequired` (عند لزوم موقع الخلفية) من نوع دالّة بلا وُسطاء تُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:22]

```
23:     private val onOnboardingFailed: (String) -> Unit
```
> يعرّف معامِلاً ثابتاً خاصّاً باسم `onOnboardingFailed` (عند فشل التهيئة) من نوع دالّة تأخذ نصّاً `String` وتُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:23]

```
24: ) {
```
> يُغلق قائمة معاملات المُنشئ ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:25]

```
26:     companion object {
```
> يبدأ تعريف الكائن المرافق (companion object). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:26]

```
27:         private const val TAG = "OnboardingCoordinator"
```
> يعرّف ثابتاً خاصّاً باسم `TAG` (وَسْم) بقيمة نصية `"OnboardingCoordinator"`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:27]

```
28:     }
```
> إغلاق نطاق (نهاية الكائن المرافق). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:28]

```
29: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:29]

```
30:     private var permissionLauncher: ActivityResultLauncher<Array<String>>? = null
```
> يعرّف متغيّراً خاصّاً باسم `permissionLauncher` (مُطلِق الأذونات) من نوع `ActivityResultLauncher` لمصفوفة نصوص قابل لأن يكون فارغاً، ويضبط قيمته الابتدائية إلى `null`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:30]

```
31:     private var backgroundLocationLauncher: ActivityResultLauncher<String>? = null
```
> يعرّف متغيّراً خاصّاً باسم `backgroundLocationLauncher` (مُطلِق موقع الخلفية) من نوع `ActivityResultLauncher` لنصّ قابل لأن يكون فارغاً، ويضبط قيمته الابتدائية إلى `null`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:31]

```
32: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:32]

```
33:     init {
```
> يبدأ كتلة التهيئة (init) للصنف. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:33]

```
34:         setupPermissionLauncher()
```
> يستدعي الدالة `setupPermissionLauncher` (إعداد مُطلِق الأذونات). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:34]

```
35:         setupBackgroundLocationLauncher()
```
> يستدعي الدالة `setupBackgroundLocationLauncher` (إعداد مُطلِق موقع الخلفية). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:35]

```
36:     }
```
> إغلاق نطاق (نهاية كتلة التهيئة). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:36]

```
37: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:37]

```
38:     /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:38]

```
39:      * Setup the permission request launcher
```
> تعليق: «إعداد مُطلِق طلب الأذونات». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:39]

```
40:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:40]

```
41:     private fun setupPermissionLauncher() {
```
> يعرّف دالّة خاصّة باسم `setupPermissionLauncher` بلا وُسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:41]

```
42:         permissionLauncher = activity.registerForActivityResult(
```
> يُسنِد إلى `permissionLauncher` ناتج استدعاء `activity.registerForActivityResult` (تسجيل لنتيجة نشاط) ويبدأ تمرير وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:42]

```
43:             ActivityResultContracts.RequestMultiplePermissions()
```
> يمرّر كوسيط أوّل كائناً من `ActivityResultContracts.RequestMultiplePermissions` (عقد طلب أذونات متعددة). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:43]

```
44:         ) { permissions ->
```
> يُغلق قائمة الوُسطاء ويبدأ تعبير لامدا (lambda) يأخذ معامِلاً باسم `permissions`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:44]

```
45:             handlePermissionResults(permissions)
```
> يستدعي الدالة `handlePermissionResults` (معالجة نتائج الأذونات) ممرِّراً `permissions`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:45]

```
46:         }
```
> إغلاق نطاق (نهاية تعبير اللامدا). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:46]

```
47:     }
```
> إغلاق نطاق (نهاية الدالة `setupPermissionLauncher`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:47]

```
48: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:48]

```
49:     private fun setupBackgroundLocationLauncher() {
```
> يعرّف دالّة خاصّة باسم `setupBackgroundLocationLauncher` بلا وُسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:49]

```
50:         backgroundLocationLauncher = activity.registerForActivityResult(
```
> يُسنِد إلى `backgroundLocationLauncher` ناتج استدعاء `activity.registerForActivityResult` ويبدأ تمرير وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:50]

```
51:             ActivityResultContracts.RequestPermission()
```
> يمرّر كوسيط أوّل كائناً من `ActivityResultContracts.RequestPermission` (عقد طلب إذن واحد). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:51]

```
52:         ) { granted ->
```
> يُغلق قائمة الوُسطاء ويبدأ تعبير لامدا يأخذ معامِلاً باسم `granted` (مُمنوح). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:52]

```
53:             handleBackgroundLocationResult(granted)
```
> يستدعي الدالة `handleBackgroundLocationResult` (معالجة نتيجة موقع الخلفية) ممرِّراً `granted`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:53]

```
54:         }
```
> إغلاق نطاق (نهاية تعبير اللامدا). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:54]

```
55:     }
```
> إغلاق نطاق (نهاية الدالة `setupBackgroundLocationLauncher`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:55]

```
56: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:56]

```
57:     /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:57]

```
58:      * Start the onboarding process
```
> تعليق: «بدء عملية التهيئة». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:58]

```
59:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:59]

```
60:     fun startOnboarding() {
```
> يعرّف دالّة عامّة باسم `startOnboarding` (بدء التهيئة) بلا وُسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:60]

```
61:         Log.d(TAG, "Starting onboarding process")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بالوَسْم `TAG` ونصّ «Starting onboarding process». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:61]

```
62:         permissionManager.logPermissionStatus()
```
> يستدعي `permissionManager.logPermissionStatus` (تسجيل حالة الأذونات). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:62]

```
63: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:63]

```
64:         if (permissionManager.areRequiredPermissionsGranted()) {
```
> يفتح شرطاً يختبر ناتج `permissionManager.areRequiredPermissionsGranted` (هل الأذونات المطلوبة ممنوحة). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:64]

```
65:             if (shouldRequestBackgroundLocation()) {
```
> يفتح شرطاً داخلياً يختبر ناتج `shouldRequestBackgroundLocation` (هل ينبغي طلب موقع الخلفية). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:65]

```
66:                 Log.d(TAG, "Foreground permissions granted; background location recommended")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «Foreground permissions granted; background location recommended». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:66]

```
67:                 onBackgroundLocationRequired()
```
> يستدعي الدالة `onBackgroundLocationRequired`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:67]

```
68:             } else {
```
> يُغلق فرع `if` الداخلي ويبدأ فرع `else`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:68]

```
69:                 Log.d(TAG, "Required permissions already granted, completing onboarding")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «Required permissions already granted, completing onboarding». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:69]

```
70:                 completeOnboarding()
```
> يستدعي الدالة `completeOnboarding` (إكمال التهيئة). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:70]

```
71:             }
```
> إغلاق نطاق (نهاية فرع `else` الداخلي). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:71]

```
72:         } else {
```
> يُغلق فرع `if` الخارجي ويبدأ فرع `else`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:72]

```
73:             Log.d(TAG, "Missing permissions, need to start explanation flow")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «Missing permissions, need to start explanation flow». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:73]

```
74:             // The explanation screen will be shown by the calling activity
```
> تعليق: «شاشة الشرح سيعرضها النشاط المُستدعِي». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:74]

```
75:         }
```
> إغلاق نطاق (نهاية فرع `else` الخارجي). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:75]

```
76:     }
```
> إغلاق نطاق (نهاية الدالة `startOnboarding`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:76]

```
77: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:77]

```
78:     /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:78]

```
79:      * Called when user accepts the permission explanation
```
> تعليق: «يُستدعى عندما يقبل المستخدم شرح الأذونات». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:79]

```
80:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:80]

```
81:     fun requestPermissions() {
```
> يعرّف دالّة عامّة باسم `requestPermissions` (طلب الأذونات) بلا وُسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:81]

```
82:         Log.d(TAG, "User accepted permission explanation, requesting permissions")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «User accepted permission explanation, requesting permissions». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:82]

```
83:         
```
> سطر فارغ (يحوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:83]

```
84:         // Required permissions
```
> تعليق: «الأذونات المطلوبة». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:84]

```
85:         val missingRequired = permissionManager.getMissingPermissions()
```
> يعرّف قيمة ثابتة باسم `missingRequired` (المطلوبة المفقودة) ويُسنِد إليها ناتج `permissionManager.getMissingPermissions` (جلب الأذونات المفقودة). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:85]

```
86: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:86]

```
87:         // Optional permissions (ask, but do not block if denied)
```
> تعليق: «الأذونات الاختيارية (تُطلَب، لكن لا تمنع إذا رُفضت)». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:87]

```
88:         val optionalToRequest = permissionManager
```
> يعرّف قيمة ثابتة باسم `optionalToRequest` (الاختيارية للطلب) ويبدأ إسناد سلسلة استدعاءات من `permissionManager`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:88]

```
89:             .getOptionalPermissions()
```
> يستدعي `getOptionalPermissions` (جلب الأذونات الاختيارية) على `permissionManager`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:89]

```
90:             .filter { !permissionManager.isPermissionGranted(it) }
```
> يطبّق `filter` (ترشيح) يُبقي العناصر التي ليست مُمنوحة بحسب `permissionManager.isPermissionGranted` المطبَّق على العنصر `it`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:90]

```
91: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:91]

```
92:         val missingPermissions = (missingRequired + optionalToRequest).distinct()
```
> يعرّف قيمة ثابتة باسم `missingPermissions` (الأذونات المفقودة) ويُسنِد إليها دمج `missingRequired` مع `optionalToRequest` بعد إزالة المكرّر عبر `distinct`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:92]

```
93: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:93]

```
94:         if (missingPermissions.isEmpty()) {
```
> يفتح شرطاً يختبر هل `missingPermissions` فارغة عبر `isEmpty`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:94]

```
95:             if (shouldRequestBackgroundLocation()) {
```
> يفتح شرطاً داخلياً يختبر ناتج `shouldRequestBackgroundLocation`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:95]

```
96:                 onBackgroundLocationRequired()
```
> يستدعي الدالة `onBackgroundLocationRequired`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:96]

```
97:             } else {
```
> يُغلق فرع `if` الداخلي ويبدأ فرع `else`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:97]

```
98:                 completeOnboarding()
```
> يستدعي الدالة `completeOnboarding`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:98]

```
99:             }
```
> إغلاق نطاق (نهاية فرع `else` الداخلي). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:99]

```
100:             return
```
> يُنفّذ عبارة `return` التي تُعيد من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:100]

```
101:         }
```
> إغلاق نطاق (نهاية شرط `if (missingPermissions.isEmpty())`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:101]

```
102: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:102]

```
103:         Log.d(TAG, "Requesting ${missingPermissions.size} permissions")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «Requesting » يتبعه عدد عناصر `missingPermissions` عبر `size` ثم « permissions». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:103]

```
104:         permissionLauncher?.launch(missingPermissions.toTypedArray())
```
> يستدعي `launch` على `permissionLauncher` (إن لم يكن فارغاً) ممرِّراً `missingPermissions` بعد تحويلها إلى مصفوفة عبر `toTypedArray`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:104]

```
105:     }
```
> إغلاق نطاق (نهاية الدالة `requestPermissions`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:105]

```
106: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:106]

```
107:     /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:107]

```
108:      * Handle permission request results
```
> تعليق: «معالجة نتائج طلب الأذونات». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:108]

```
109:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:109]

```
110:     private fun handlePermissionResults(permissions: Map<String, Boolean>) {
```
> يعرّف دالّة خاصّة باسم `handlePermissionResults` تأخذ معامِلاً `permissions` من نوع خريطة `Map` من نصّ إلى منطقي `Boolean`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:110]

```
111:         Log.d(TAG, "Received permission results:")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «Received permission results:». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:111]

```
112:         permissions.forEach { (permission, granted) ->
```
> يطبّق `forEach` (لكلّ عنصر) على `permissions` مفكّكاً كل مدخل إلى `permission` و`granted`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:112]

```
113:             Log.d(TAG, "  $permission: ${if (granted) "GRANTED" else "DENIED"}")
```
> يستدعي `Log.d` لتسجيل نصّ يبدأ بمسافتين ثم قيمة `permission` ثم نقطتين، ثم «GRANTED» إن كان `granted` صحيحاً وإلا «DENIED». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:113]

```
114:         }
```
> إغلاق نطاق (نهاية كتلة `forEach`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:114]

```
115: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:115]

```
116:         val allGranted = permissions.values.all { it }
```
> يعرّف قيمة ثابتة باسم `allGranted` (الكل مُمنوح) ويُسنِد إليها ناتج `all` على قيم `permissions` الذي يكون صحيحاً إذا كان كل عنصر `it` صحيحاً. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:116]

```
117:         val criticalPermissions = getCriticalPermissions()
```
> يعرّف قيمة ثابتة باسم `criticalPermissions` (الأذونات الحرجة) ويُسنِد إليها ناتج `getCriticalPermissions` (جلب الأذونات الحرجة). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:117]

```
118:         val criticalGranted = criticalPermissions.all { permissions[it] == true }
```
> يعرّف قيمة ثابتة باسم `criticalGranted` (الحرجة مُمنوحة) ويُسنِد إليها ناتج `all` على `criticalPermissions` الذي يكون صحيحاً إذا كانت قيمة كل عنصر `it` في `permissions` تساوي `true`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:118]

```
119: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:119]

```
120:         when {
```
> يفتح تعبير `when` بلا موضوع (متفرّع بشروط). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:120]

```
121:             criticalGranted -> {
```
> يبدأ فرعاً شرطه `criticalGranted` ويفتح كتلته. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:121]

```
122:                 if (shouldRequestBackgroundLocation()) {
```
> يفتح شرطاً يختبر ناتج `shouldRequestBackgroundLocation`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:122]

```
123:                     Log.d(TAG, "Foreground permissions granted; requesting background location next")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «Foreground permissions granted; requesting background location next». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:123]

```
124:                     onBackgroundLocationRequired()
```
> يستدعي الدالة `onBackgroundLocationRequired`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:124]

```
125:                     return
```
> يُنفّذ عبارة `return` التي تُعيد من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:125]

```
126:                 }
```
> إغلاق نطاق (نهاية شرط `if (shouldRequestBackgroundLocation())`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:126]

```
127:                 if (allGranted) {
```
> يفتح شرطاً يختبر `allGranted`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:127]

```
128:                     Log.d(TAG, "All permissions granted successfully")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «All permissions granted successfully». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:128]

```
129:                     completeOnboarding()
```
> يستدعي الدالة `completeOnboarding`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:129]

```
130:                 } else {
```
> يُغلق فرع `if (allGranted)` ويبدأ فرع `else`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:130]

```
131:                     Log.d(TAG, "Critical permissions granted, can proceed with limited functionality")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «Critical permissions granted, can proceed with limited functionality». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:131]

```
132:                     showPartialPermissionWarning(permissions)
```
> يستدعي الدالة `showPartialPermissionWarning` (عرض تحذير الأذونات الجزئية) ممرِّراً `permissions`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:132]

```
133:                 }
```
> إغلاق نطاق (نهاية فرع `else` لشرط `allGranted`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:133]

```
134:             }
```
> إغلاق نطاق (نهاية فرع `criticalGranted`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:134]

```
135:             else -> {
```
> يبدأ الفرع `else` (الحالة المتبقية) في تعبير `when` ويفتح كتلته. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:135]

```
136:                 Log.d(TAG, "Critical permissions denied")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «Critical permissions denied». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:136]

```
137:                 handlePermissionDenial(permissions)
```
> يستدعي الدالة `handlePermissionDenial` (معالجة رفض الأذونات) ممرِّراً `permissions`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:137]

```
138:             }
```
> إغلاق نطاق (نهاية فرع `else`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:138]

```
139:         }
```
> إغلاق نطاق (نهاية تعبير `when`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:139]

```
140:     }
```
> إغلاق نطاق (نهاية الدالة `handlePermissionResults`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:140]

```
141: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:141]

```
142:     fun requestBackgroundLocation() {
```
> يعرّف دالّة عامّة باسم `requestBackgroundLocation` (طلب موقع الخلفية) بلا وُسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:142]

```
143:         val permission = permissionManager.getBackgroundLocationPermission()
```
> يعرّف قيمة ثابتة باسم `permission` ويُسنِد إليها ناتج `permissionManager.getBackgroundLocationPermission` (جلب إذن موقع الخلفية). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:143]

```
144:         if (permission == null) {
```
> يفتح شرطاً يختبر هل `permission` يساوي `null`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:144]

```
145:             completeOnboarding()
```
> يستدعي الدالة `completeOnboarding`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:145]

```
146:             return
```
> يُنفّذ عبارة `return` التي تُعيد من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:146]

```
147:         }
```
> إغلاق نطاق (نهاية شرط `if (permission == null)`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:147]

```
148:         Log.d(TAG, "Requesting background location permission")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «Requesting background location permission». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:148]

```
149:         backgroundLocationLauncher?.launch(permission)
```
> يستدعي `launch` على `backgroundLocationLauncher` (إن لم يكن فارغاً) ممرِّراً `permission`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:149]

```
150:     }
```
> إغلاق نطاق (نهاية الدالة `requestBackgroundLocation`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:150]

```
151: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:151]

```
152:     private fun handleBackgroundLocationResult(granted: Boolean) {
```
> يعرّف دالّة خاصّة باسم `handleBackgroundLocationResult` تأخذ معامِلاً `granted` من نوع منطقي `Boolean`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:152]

```
153:         if (granted) {
```
> يفتح شرطاً يختبر `granted`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:153]

```
154:             Log.d(TAG, "Background location permission granted")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «Background location permission granted». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:154]

```
155:         } else {
```
> يُغلق فرع `if (granted)` ويبدأ فرع `else`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:155]

```
156:             Log.w(TAG, "Background location permission denied; continuing without it")
```
> يستدعي `Log.w` لتسجيل رسالة تحذير بنصّ «Background location permission denied; continuing without it». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:156]

```
157:         }
```
> إغلاق نطاق (نهاية فرع `else`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:157]

```
158:         completeOnboarding()
```
> يستدعي الدالة `completeOnboarding`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:158]

```
159:     }
```
> إغلاق نطاق (نهاية الدالة `handleBackgroundLocationResult`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:159]

```
160: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:160]

```
161:     fun skipBackgroundLocation() {
```
> يعرّف دالّة عامّة باسم `skipBackgroundLocation` (تخطّي موقع الخلفية) بلا وُسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:161]

```
162:         Log.d(TAG, "User skipped background location permission")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بنصّ «User skipped background location permission». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:162]

```
163:         BackgroundLocationPreferenceManager.setSkipped(activity, true)
```
> يستدعي `BackgroundLocationPreferenceManager.setSkipped` (ضبط التخطّي) ممرِّراً `activity` والقيمة `true`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:163]

```
164:         completeOnboarding()
```
> يستدعي الدالة `completeOnboarding`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:164]

```
165:     }
```
> إغلاق نطاق (نهاية الدالة `skipBackgroundLocation`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:165]

```
166: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:166]

```
167:     fun checkBackgroundLocationAndProceed() {
```
> يعرّف دالّة عامّة باسم `checkBackgroundLocationAndProceed` (فحص موقع الخلفية والمتابعة) بلا وُسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:167]

```
168:         if (!shouldRequestBackgroundLocation()) {
```
> يفتح شرطاً يختبر نفي ناتج `shouldRequestBackgroundLocation`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:168]

```
169:             completeOnboarding()
```
> يستدعي الدالة `completeOnboarding`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:169]

```
170:         }
```
> إغلاق نطاق (نهاية الشرط). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:170]

```
171:     }
```
> إغلاق نطاق (نهاية الدالة `checkBackgroundLocationAndProceed`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:171]

```
172: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:172]

```
173:     private fun shouldRequestBackgroundLocation(): Boolean {
```
> يعرّف دالّة خاصّة باسم `shouldRequestBackgroundLocation` بلا وُسطاء تُعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:173]

```
174:         return permissionManager.needsBackgroundLocationPermission() &&
```
> يبدأ عبارة `return` تُعيد ناتج `permissionManager.needsBackgroundLocationPermission` (هل يلزم إذن موقع الخلفية) مرتبطاً بعامل «و» المنطقي `&&`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:174]

```
175:             !permissionManager.isBackgroundLocationGranted() &&
```
> يُكمل التعبير بنفي ناتج `permissionManager.isBackgroundLocationGranted` (هل موقع الخلفية مُمنوح) مرتبطاً بعامل «و» المنطقي `&&`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:175]

```
176:             !BackgroundLocationPreferenceManager.isSkipped(activity)
```
> يُكمل التعبير بنفي ناتج `BackgroundLocationPreferenceManager.isSkipped` (هل تمّ التخطّي) المطبَّق على `activity`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:176]

```
177:     }
```
> إغلاق نطاق (نهاية الدالة `shouldRequestBackgroundLocation`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:177]

```
178: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:178]

```
179:     /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:179]

```
180:      * Get the list of critical permissions that are absolutely required
```
> تعليق: «جلب قائمة الأذونات الحرجة المطلوبة قطعاً». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:180]

```
181:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:181]

```
182:     private fun getCriticalPermissions(): List<String> {
```
> يعرّف دالّة خاصّة باسم `getCriticalPermissions` بلا وُسطاء تُعيد قائمة `List` من نصوص. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:182]

```
183:         // For bitchat, Bluetooth and location permissions are critical
```
> تعليق: «بالنسبة لـ bitchat، أذونات البلوتوث والموقع حرجة». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:183]

```
184:         // Notifications are nice-to-have but not critical and are not included in getRequiredPermissions()
```
> تعليق: «الإشعارات مستحبّة لكنها ليست حرجة وغير مُضمَّنة في getRequiredPermissions()». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:184]

```
185:         return permissionManager.getRequiredPermissions()
```
> يُنفّذ عبارة `return` تُعيد ناتج `permissionManager.getRequiredPermissions` (جلب الأذونات المطلوبة). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:185]

```
186:     }
```
> إغلاق نطاق (نهاية الدالة `getCriticalPermissions`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:186]

```
187: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:187]

```
188:     /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:188]

```
189:      * Show warning when some permissions are granted but others are denied
```
> تعليق: «عرض تحذير عندما تُمنح بعض الأذونات وتُرفض أخرى». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:189]

```
190:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:190]

```
191:     private fun showPartialPermissionWarning(permissions: Map<String, Boolean>) {
```
> يعرّف دالّة خاصّة باسم `showPartialPermissionWarning` تأخذ معامِلاً `permissions` من نوع خريطة `Map` من نصّ إلى منطقي `Boolean`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:191]

```
192:         val deniedPermissions = permissions.filter { !it.value }.keys
```
> يعرّف قيمة ثابتة باسم `deniedPermissions` (الأذونات المرفوضة) ويُسنِد إليها مفاتيح `keys` ناتجة عن ترشيح `permissions` بإبقاء المدخلات التي قيمتها `value` ليست صحيحة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:192]

```
193:         val message = buildString {
```
> يعرّف قيمة ثابتة باسم `message` (رسالة) ويبدأ بناءها عبر `buildString` (بناء نصّ). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:193]

```
194:             append("Some permissions were denied:\n")
```
> يستدعي `append` لإلحاق النصّ «Some permissions were denied:» متبوعاً بسطر جديد `\n`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:194]

```
195:             deniedPermissions.forEach { permission ->
```
> يطبّق `forEach` على `deniedPermissions` مع معامِل لامدا باسم `permission`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:195]

```
196:                 append("- ${getPermissionDisplayName(permission)}\n")
```
> يستدعي `append` لإلحاق شَرطة وفراغ ثم ناتج `getPermissionDisplayName` (جلب اسم العرض للإذن) المطبَّق على `permission` متبوعاً بسطر جديد `\n`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:196]

```
197:             }
```
> إغلاق نطاق (نهاية كتلة `forEach`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:197]

```
198:             append("\nbitchat may not work properly without all permissions.")
```
> يستدعي `append` لإلحاق سطر جديد `\n` ثم النصّ «bitchat may not work properly without all permissions.». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:198]

```
199:         }
```
> إغلاق نطاق (نهاية كتلة `buildString`). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:199]

```
200: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:200]
