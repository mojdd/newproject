# شريحة — app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt (الأسطر 1–200)

```
1: package com.bitchat.android.service
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) المسماة com.bitchat.android.service. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:2]

```
3: import android.app.Notification
```
> يستورد (import) الصنف Notification من حزمة android.app. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:3]

```
4: import android.app.NotificationChannel
```
> يستورد الصنف NotificationChannel (قناة التنبيه) من حزمة android.app. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:4]

```
5: import android.app.NotificationManager
```
> يستورد الصنف NotificationManager (مدير التنبيهات) من حزمة android.app. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:5]

```
6: import android.app.PendingIntent
```
> يستورد الصنف PendingIntent (النيّة المعلّقة) من حزمة android.app. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:6]

```
7: import android.app.Service
```
> يستورد الصنف Service (الخدمة) من حزمة android.app. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:7]

```
8: import android.content.Context
```
> يستورد الصنف Context (السياق) من حزمة android.content. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:8]

```
9: import android.content.Intent
```
> يستورد الصنف Intent (النيّة) من حزمة android.content. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:9]

```
10: import android.content.pm.ServiceInfo
```
> يستورد الصنف ServiceInfo (معلومات الخدمة) من حزمة android.content.pm. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:10]

```
11: import android.os.Build
```
> يستورد الصنف Build (معلومات البناء/الإصدار) من حزمة android.os. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:11]

```
12: import android.os.IBinder
```
> يستورد الواجهة IBinder (الرابط) من حزمة android.os. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:12]

```
13: import android.util.Log
```
> يستورد الصنف Log (السجل) من حزمة android.util. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:13]

```
14: import androidx.core.app.NotificationCompat
```
> يستورد الصنف NotificationCompat (توافق التنبيه) من حزمة androidx.core.app. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:14]

```
15: import androidx.core.app.NotificationManagerCompat
```
> يستورد الصنف NotificationManagerCompat (توافق مدير التنبيهات) من حزمة androidx.core.app. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:15]

```
16: import com.bitchat.android.MainActivity
```
> يستورد الصنف MainActivity (النشاط الرئيسي) من حزمة com.bitchat.android. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:16]

```
17: import com.bitchat.android.R
```
> يستورد الصنف R (الموارد) من حزمة com.bitchat.android. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:17]

```
18: import com.bitchat.android.mesh.BluetoothMeshService
```
> يستورد الصنف BluetoothMeshService (خدمة شبكة بلوتوث المتشابكة) من حزمة com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:18]

```
19: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف CoroutineScope (نطاق الكوروتين) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:19]

```
20: import kotlinx.coroutines.Dispatchers
```
> يستورد الكائن Dispatchers (الموزِّعات) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:20]

```
21: import kotlinx.coroutines.Job
```
> يستورد الواجهة Job (المهمّة) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:21]

```
22: import kotlinx.coroutines.delay
```
> يستورد الدالة delay (التأخير) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:22]

```
23: import kotlinx.coroutines.isActive
```
> يستورد الخاصية isActive (هل نشط) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:23]

```
24: import kotlinx.coroutines.launch
```
> يستورد الدالة launch (الإطلاق) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:25]

```
26: class MeshForegroundService : Service() {
```
> يعرّف الصنف MeshForegroundService (خدمة الشبكة المتشابكة الأمامية) ويرثه من الصنف Service ويفتح نطاق الصنف. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:27]

```
28:     companion object {
```
> يفتح نطاق الكائن المرافق (companion object) للصنف. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:28]

```
29:         private const val CHANNEL_ID = "bitchat_mesh_service"
```
> يعرّف ثابتاً خاصاً CHANNEL_ID (معرّف القناة) بقيمة نصية "bitchat_mesh_service". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:29]

```
30:         private const val NOTIFICATION_ID = 10001
```
> يعرّف ثابتاً خاصاً NOTIFICATION_ID (معرّف التنبيه) بقيمة عددية 10001. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:30]

```
31: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:31]

```
32:         const val ACTION_START = "com.bitchat.android.service.START"
```
> يعرّف ثابتاً عاماً ACTION_START (إجراء البدء) بقيمة نصية "com.bitchat.android.service.START". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:32]

```
33:         const val ACTION_STOP = "com.bitchat.android.service.STOP"
```
> يعرّف ثابتاً عاماً ACTION_STOP (إجراء الإيقاف) بقيمة نصية "com.bitchat.android.service.STOP". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:33]

```
34:         const val ACTION_QUIT = "com.bitchat.android.service.QUIT"
```
> يعرّف ثابتاً عاماً ACTION_QUIT (إجراء الخروج) بقيمة نصية "com.bitchat.android.service.QUIT". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:34]

```
35:         const val ACTION_UPDATE_NOTIFICATION = "com.bitchat.android.service.UPDATE_NOTIFICATION"
```
> يعرّف ثابتاً عاماً ACTION_UPDATE_NOTIFICATION (إجراء تحديث التنبيه) بقيمة نصية "com.bitchat.android.service.UPDATE_NOTIFICATION". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:35]

```
36:         const val ACTION_NOTIFICATION_PERMISSION_GRANTED = "com.bitchat.android.action.NOTIFICATION_PERMISSION_GRANTED"
```
> يعرّف ثابتاً عاماً ACTION_NOTIFICATION_PERMISSION_GRANTED (إجراء منح إذن التنبيه) بقيمة نصية "com.bitchat.android.action.NOTIFICATION_PERMISSION_GRANTED". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:36]

```
37: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:37]

```
38:         fun start(context: Context) {
```
> يعرّف الدالة start (البدء) التي تأخذ معاملاً context من نوع Context ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:38]

```
39:             val intent = Intent(context, MeshForegroundService::class.java).apply { action = ACTION_START }
```
> يُنشئ متغيراً intent ككائن Intent موجّه إلى صنف MeshForegroundService، ويضبط ضمن apply خاصيته action إلى ACTION_START. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:39]

```
40: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:40]

```
41:             // Only launch as an FGS when onStartCommand can promote immediately.
```
> تعليق: لا تُطلق إلا كخدمة أمامية (FGS) عندما تستطيع onStartCommand الترقية فوراً. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:41]

```
42:             val shouldStartForeground = shouldStartAsForeground(context)
```
> يُنشئ متغيراً shouldStartForeground (هل يجب البدء أمامياً) ويسند إليه ناتج استدعاء الدالة shouldStartAsForeground مع context. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:42]

```
43: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:43]

```
44:             if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
```
> يفتح شرطاً يتحقق أن رقم إصدار النظام SDK_INT أكبر من أو يساوي إصدار O (أوريو). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:44]

```
45:                 if (shouldStartForeground) {
```
> يفتح شرطاً داخلياً يتحقق أن قيمة shouldStartForeground صحيحة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:45]

```
46:                     context.startForegroundService(intent)
```
> يستدعي على context الدالة startForegroundService (بدء خدمة أمامية) مع المعامل intent. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:46]

```
47:                 } else {
```
> يغلق نطاق الشرط ويفتح فرع البديل else. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:47]

```
48:                     android.util.Log.i(
```
> يستدعي الدالة android.util.Log.i (تسجيل معلومات) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:48]

```
49:                         "MeshForegroundService",
```
> يمرّر المعامل الأول وسماً نصياً "MeshForegroundService". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:49]

```
50:                         "Not starting service on API>=26 (shouldStartForeground=$shouldStartForeground)"
```
> يمرّر المعامل الثاني نصاً "Not starting service on API>=26 (shouldStartForeground=$shouldStartForeground)" مع إدراج قيمة shouldStartForeground. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:50]

```
51:                     )
```
> يغلق قائمة معاملات استدعاء Log.i. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:51]

```
52:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:52]

```
53:             } else {
```
> يغلق نطاق شرط الإصدار ويفتح فرع البديل else. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:53]

```
54:                 if (MeshServicePreferences.isBackgroundEnabled(true)) {
```
> يفتح شرطاً يستدعي MeshServicePreferences.isBackgroundEnabled (هل الخلفية مفعّلة) بقيمة افتراضية true. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:54]

```
55:                     context.startService(intent)
```
> يستدعي على context الدالة startService (بدء الخدمة) مع المعامل intent. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:55]

```
56:                 } else {
```
> يغلق نطاق الشرط ويفتح فرع البديل else. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:56]

```
57:                     android.util.Log.i("MeshForegroundService", "Background disabled; not starting service (pre-O)")
```
> يستدعي android.util.Log.i بوسم "MeshForegroundService" ونص "Background disabled; not starting service (pre-O)". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:57]

```
58:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:58]

```
59:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:59]

```
60:         }
```
> إغلاق نطاق (نهاية الدالة start). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:60]

```
61: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:61]

```
62:         /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:62]

```
63:          * Helper to be invoked right after POST_NOTIFICATIONS is granted to try
```
> تعليق: دالة مساعِدة تُستدعى مباشرة بعد منح POST_NOTIFICATIONS لمحاولة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:63]

```
64:          * promoting/starting the foreground service immediately without polling.
```
> تعليق: ترقية/بدء الخدمة الأمامية فوراً دون استطلاع متكرر (polling). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:64]

```
65:          */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:65]

```
66:         fun onNotificationPermissionGranted(context: Context) {
```
> يعرّف الدالة onNotificationPermissionGranted (عند منح إذن التنبيه) التي تأخذ معاملاً context من نوع Context ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:66]

```
67:             // If background is enabled and permission now granted, start/promo service
```
> تعليق: إذا كانت الخلفية مفعّلة والإذن مُنح الآن، ابدأ/رقِّ الخدمة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:67]

```
68:             if (!shouldStartAsForeground(context)) return
```
> يفتح شرطاً: إذا كان ناتج shouldStartAsForeground مع context خاطئاً فإنه يُنفّذ return (الرجوع/الخروج من الدالة). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:68]

```
69: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:69]

```
70:             val intent = Intent(context, MeshForegroundService::class.java).apply { action = ACTION_UPDATE_NOTIFICATION }
```
> يُنشئ متغيراً intent ككائن Intent موجّه إلى صنف MeshForegroundService، ويضبط ضمن apply خاصيته action إلى ACTION_UPDATE_NOTIFICATION. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:70]

```
71:             if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
```
> يفتح شرطاً يتحقق أن SDK_INT أكبر من أو يساوي إصدار O. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:71]

```
72:                 context.startForegroundService(intent)
```
> يستدعي على context الدالة startForegroundService مع المعامل intent. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:72]

```
73:             } else {
```
> يغلق نطاق الشرط ويفتح فرع البديل else. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:73]

```
74:                 context.startService(intent)
```
> يستدعي على context الدالة startService مع المعامل intent. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:74]

```
75:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:75]

```
76:         }
```
> إغلاق نطاق (نهاية الدالة onNotificationPermissionGranted). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:76]

```
77: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:77]

```
78:         fun stop(context: Context) {
```
> يعرّف الدالة stop (الإيقاف) التي تأخذ معاملاً context من نوع Context ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:78]

```
79:             val intent = Intent(context, MeshForegroundService::class.java).apply { action = ACTION_STOP }
```
> يُنشئ متغيراً intent ككائن Intent موجّه إلى صنف MeshForegroundService، ويضبط ضمن apply خاصيته action إلى ACTION_STOP. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:79]

```
80:             context.startService(intent)
```
> يستدعي على context الدالة startService مع المعامل intent. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:80]

```
81:         }
```
> إغلاق نطاق (نهاية الدالة stop). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:81]

```
82: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:82]

```
83:         private fun shouldStartAsForeground(context: Context): Boolean {
```
> يعرّف دالة خاصة shouldStartAsForeground (هل يجب البدء أمامياً) تأخذ context من نوع Context وتُعيد قيمة منطقية Boolean ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:83]

```
84:             return MeshServicePreferences.isBackgroundEnabled(true) &&
```
> يُعيد ناتج ربط منطقي بعامل && يبدأ باستدعاء MeshServicePreferences.isBackgroundEnabled بقيمة true. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:84]

```
85:                     hasBluetoothPermissionsStatic(context) &&
```
> يتابع التعبير المنطقي بعامل && مع استدعاء hasBluetoothPermissionsStatic مع context. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:85]

```
86:                     hasNotificationPermissionStatic(context)
```
> يختم التعبير المنطقي باستدعاء hasNotificationPermissionStatic مع context. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:86]

```
87:         }
```
> إغلاق نطاق (نهاية الدالة shouldStartAsForeground). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:87]

```
88: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:88]

```
89:         private fun hasBluetoothPermissionsStatic(ctx: Context): Boolean {
```
> يعرّف دالة خاصة hasBluetoothPermissionsStatic (امتلاك أذونات بلوتوث الساكنة) تأخذ ctx من نوع Context وتُعيد Boolean ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:89]

```
90:             return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
```
> يُعيد ناتج تعبير if يتحقق أن SDK_INT أكبر من أو يساوي إصدار S (أندرويد ١٢) ويفتح فرعه الأول. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:90]

```
91:                 androidx.core.content.ContextCompat.checkSelfPermission(ctx, android.Manifest.permission.BLUETOOTH_ADVERTISE) == android.content.pm.PackageManager.PERMISSION_GRANTED &&
```
> يتحقق أن ContextCompat.checkSelfPermission لإذن BLUETOOTH_ADVERTISE يساوي PERMISSION_GRANTED، مع ربط && للجزء التالي. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:91]

```
92:                 androidx.core.content.ContextCompat.checkSelfPermission(ctx, android.Manifest.permission.BLUETOOTH_CONNECT) == android.content.pm.PackageManager.PERMISSION_GRANTED &&
```
> يتحقق أن checkSelfPermission لإذن BLUETOOTH_CONNECT يساوي PERMISSION_GRANTED، مع ربط && للجزء التالي. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:92]

```
93:                 androidx.core.content.ContextCompat.checkSelfPermission(ctx, android.Manifest.permission.BLUETOOTH_SCAN) == android.content.pm.PackageManager.PERMISSION_GRANTED
```
> يتحقق أن checkSelfPermission لإذن BLUETOOTH_SCAN يساوي PERMISSION_GRANTED بوصفه آخر شرط في الفرع. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:93]

```
94:             } else {
```
> يغلق الفرع الأول ويفتح فرع البديل else. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:94]

```
95:                 val fine = androidx.core.content.ContextCompat.checkSelfPermission(ctx, android.Manifest.permission.ACCESS_FINE_LOCATION) == android.content.pm.PackageManager.PERMISSION_GRANTED
```
> يُنشئ متغيراً fine يساوي نتيجة المقارنة بين checkSelfPermission لإذن ACCESS_FINE_LOCATION (الموقع الدقيق) وPERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:95]

```
96:                 val coarse = androidx.core.content.ContextCompat.checkSelfPermission(ctx, android.Manifest.permission.ACCESS_COARSE_LOCATION) == android.content.pm.PackageManager.PERMISSION_GRANTED
```
> يُنشئ متغيراً coarse يساوي نتيجة المقارنة بين checkSelfPermission لإذن ACCESS_COARSE_LOCATION (الموقع التقريبي) وPERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:96]

```
97:                 fine || coarse
```
> يُعيد الفرع نتيجة الربط المنطقي بعامل || بين fine وcoarse. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:97]

```
98:             }
```
> إغلاق نطاق (نهاية تعبير if/else). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:98]

```
99:         }
```
> إغلاق نطاق (نهاية الدالة hasBluetoothPermissionsStatic). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:99]

```
100: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:100]

```
101:         private fun hasNotificationPermissionStatic(ctx: Context): Boolean {
```
> يعرّف دالة خاصة hasNotificationPermissionStatic (امتلاك إذن التنبيه الساكن) تأخذ ctx من نوع Context وتُعيد Boolean ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:101]

```
102:             return if (Build.VERSION.SDK_INT >= 33) {
```
> يُعيد ناتج تعبير if يتحقق أن SDK_INT أكبر من أو يساوي 33 ويفتح فرعه الأول. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:102]

```
103:                 androidx.core.content.ContextCompat.checkSelfPermission(ctx, android.Manifest.permission.POST_NOTIFICATIONS) == android.content.pm.PackageManager.PERMISSION_GRANTED
```
> يُعيد نتيجة المقارنة بين checkSelfPermission لإذن POST_NOTIFICATIONS (نشر التنبيهات) وPERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:103]

```
104:             } else true
```
> يغلق الفرع الأول ويُعيد في فرع else القيمة true. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:104]

```
105:         }
```
> إغلاق نطاق (نهاية الدالة hasNotificationPermissionStatic). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:105]

```
106:     }
```
> إغلاق نطاق (نهاية الكائن المرافق). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:106]

```
107: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:107]

```
108:     private lateinit var notificationManager: NotificationManagerCompat
```
> يعرّف متغيراً خاصاً متأخّر التهيئة (lateinit) باسم notificationManager من نوع NotificationManagerCompat. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:108]

```
109:     private var updateJob: Job? = null
```
> يعرّف متغيراً خاصاً قابلاً للتغيير updateJob (مهمّة التحديث) من نوع Job قابل للإفراغ بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:109]

```
110:     private val meshService: BluetoothMeshService?
```
> يعرّف خاصية خاصة meshService من نوع BluetoothMeshService قابل للإفراغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:110]

```
111:         get() = MeshServiceHolder.meshService
```
> يعرّف جالب (getter) الخاصية meshService بحيث يُعيد قيمة MeshServiceHolder.meshService. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:111]

```
112:     private val unifiedMeshService: com.bitchat.android.mesh.MeshService?
```
> يعرّف خاصية خاصة unifiedMeshService (خدمة الشبكة الموحّدة) من نوع com.bitchat.android.mesh.MeshService قابل للإفراغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:112]

```
113:         get() = MeshServiceHolder.unifiedMeshService
```
> يعرّف جالب الخاصية unifiedMeshService بحيث يُعيد قيمة MeshServiceHolder.unifiedMeshService. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:113]

```
114:     private val serviceJob = Job()
```
> يعرّف خاصية خاصة serviceJob (مهمّة الخدمة) ويسند إليها كائن Job جديد. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:114]

```
115:     private val scope = CoroutineScope(Dispatchers.Default + serviceJob)
```
> يعرّف خاصية خاصة scope (النطاق) ككائن CoroutineScope مبني من Dispatchers.Default مجموعاً مع serviceJob. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:115]

```
116:     private var isInForeground: Boolean = false
```
> يعرّف متغيراً خاصاً قابلاً للتغيير isInForeground (هل في المقدمة) من نوع Boolean بقيمة ابتدائية false. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:116]

```
117:     private var isShuttingDown: Boolean = false
```
> يعرّف متغيراً خاصاً قابلاً للتغيير isShuttingDown (هل يجري الإيقاف) من نوع Boolean بقيمة ابتدائية false. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:117]

```
118: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:118]

```
119:     override fun onCreate() {
```
> يعيد تعريف (override) الدالة onCreate (عند الإنشاء) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:119]

```
120:         super.onCreate()
```
> يستدعي تنفيذ الصنف الأب super.onCreate. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:120]

```
121:         notificationManager = NotificationManagerCompat.from(this)
```
> يسند إلى notificationManager ناتج NotificationManagerCompat.from مع this (هذه الخدمة). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:121]

```
122:         createChannel()
```
> يستدعي الدالة createChannel (إنشاء القناة). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:122]

```
123: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:123]

```
124:         // Ensure mesh service exists in holder (create if needed)
```
> تعليق: تأكّد من وجود خدمة الشبكة في الحامل (أنشئها عند الحاجة). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:124]

```
125:         val existing = MeshServiceHolder.meshService
```
> يُنشئ متغيراً existing (الموجود) ويسند إليه قيمة MeshServiceHolder.meshService. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:125]

```
126:         if (existing != null) {
```
> يفتح شرطاً يتحقق أن existing لا يساوي null. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:126]

```
127:             Log.d("MeshForegroundService", "Using existing BluetoothMeshService from holder")
```
> يستدعي Log.d (تسجيل تنقيح) بوسم "MeshForegroundService" ونص "Using existing BluetoothMeshService from holder". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:127]

```
128:         } else {
```
> يغلق نطاق الشرط ويفتح فرع البديل else. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:128]

```
129:             val created = MeshServiceHolder.getOrCreate(applicationContext)
```
> يُنشئ متغيراً created (المُنشأ) ويسند إليه ناتج MeshServiceHolder.getOrCreate مع applicationContext. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:129]

```
130:             Log.i("MeshForegroundService", "Created new BluetoothMeshService via holder")
```
> يستدعي Log.i (تسجيل معلومات) بوسم "MeshForegroundService" ونص "Created new BluetoothMeshService via holder". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:130]

```
131:             MeshServiceHolder.attach(created)
```
> يستدعي MeshServiceHolder.attach (ربط) مع المعامل created. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:131]

```
132:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:132]

```
133:         MeshServiceHolder.getUnifiedOrCreate(applicationContext)
```
> يستدعي MeshServiceHolder.getUnifiedOrCreate (جلب الموحّدة أو إنشاؤها) مع applicationContext. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:133]

```
134:     }
```
> إغلاق نطاق (نهاية الدالة onCreate). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:134]

```
135: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:135]

```
136:     override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
```
> يعيد تعريف الدالة onStartCommand (عند أمر البدء) التي تأخذ intent من نوع Intent قابل للإفراغ، وflags من نوع Int، وstartId من نوع Int، وتُعيد Int، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:136]

```
137:         if (isShuttingDown && intent?.action == ACTION_START) {
```
> يفتح شرطاً يتحقق أن isShuttingDown صحيحة وأن intent?.action يساوي ACTION_START. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:137]

```
138:             AppShutdownCoordinator.cancelPendingShutdown()
```
> يستدعي AppShutdownCoordinator.cancelPendingShutdown (إلغاء الإيقاف المُعلّق). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:138]

```
139:             isShuttingDown = false
```
> يسند القيمة false إلى المتغير isShuttingDown. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:139]

```
140:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:140]

```
141:         if (isShuttingDown && intent?.action != ACTION_QUIT) {
```
> يفتح شرطاً يتحقق أن isShuttingDown صحيحة وأن intent?.action لا يساوي ACTION_QUIT. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:141]

```
142:             return START_NOT_STICKY
```
> يُعيد القيمة START_NOT_STICKY. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:142]

```
143:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:143]

```
144:         when (intent?.action) {
```
> يفتح تعبير when (مطابقة) على قيمة intent?.action. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:144]

```
145:             ACTION_STOP -> {
```
> يفتح فرع المطابقة لقيمة ACTION_STOP. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:145]

```
146:                 // Stop FGS and mesh cleanly
```
> تعليق: أوقف الخدمة الأمامية والشبكة بنظافة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:146]

```
147:                 try { unifiedMeshService?.stopServices() ?: meshService?.stopServices() } catch (_: Exception) { }
```
> ضمن try يستدعي unifiedMeshService?.stopServices وإن كان null يستدعي meshService?.stopServices عبر عامل ?:، مع catch يبتلع أي Exception. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:147]

```
148:                 try { MeshServiceHolder.clear() } catch (_: Exception) { }
```
> ضمن try يستدعي MeshServiceHolder.clear (مسح)، مع catch يبتلع أي Exception. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:148]

```
149:                 try { stopForeground(true) } catch (_: Exception) { }
```
> ضمن try يستدعي stopForeground (إيقاف المقدمة) بالقيمة true، مع catch يبتلع أي Exception. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:149]

```
150:                 notificationManager.cancel(NOTIFICATION_ID)
```
> يستدعي notificationManager.cancel (إلغاء التنبيه) مع المعامل NOTIFICATION_ID. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:150]

```
151:                 isInForeground = false
```
> يسند القيمة false إلى المتغير isInForeground. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:151]

```
152:                 stopSelf()
```
> يستدعي stopSelf (إيقاف الخدمة نفسها). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:152]

```
153:                 return START_NOT_STICKY
```
> يُعيد القيمة START_NOT_STICKY. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:153]

```
154:             }
```
> إغلاق نطاق (نهاية فرع ACTION_STOP). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:154]

```
155:             ACTION_QUIT -> {
```
> يفتح فرع المطابقة لقيمة ACTION_QUIT. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:155]

```
156:                 isShuttingDown = true
```
> يسند القيمة true إلى المتغير isShuttingDown. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:156]

```
157:                 updateJob?.cancel()
```
> يستدعي على updateJob الدالة cancel (إلغاء) في حال لم يكن null. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:157]

```
158:                 updateJob = null
```
> يسند القيمة null إلى المتغير updateJob. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:158]

```
159:                 try { stopForeground(true) } catch (_: Exception) { }
```
> ضمن try يستدعي stopForeground بالقيمة true، مع catch يبتلع أي Exception. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:159]

```
160:                 notificationManager.cancel(NOTIFICATION_ID)
```
> يستدعي notificationManager.cancel مع المعامل NOTIFICATION_ID. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:160]

```
161:                 isInForeground = false
```
> يسند القيمة false إلى المتغير isInForeground. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:161]

```
162:                 // Fully stop all background activity, stop Tor (without changing setting), then kill the app
```
> تعليق: أوقف كل نشاط الخلفية كلياً، وأوقف Tor (دون تغيير الإعداد)، ثم اقتل التطبيق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:162]

```
163:                 AppShutdownCoordinator.requestFullShutdownAndKill(
```
> يستدعي AppShutdownCoordinator.requestFullShutdownAndKill (طلب الإيقاف الكامل والقتل) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:163]

```
164:                     app = application,
```
> يمرّر المعامل المسمّى app بقيمة الخاصية application. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:164]

```
165:                     mesh = unifiedMeshService,
```
> يمرّر المعامل المسمّى mesh بقيمة الخاصية unifiedMeshService. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:165]

```
166:                     notificationManager = notificationManager,
```
> يمرّر المعامل المسمّى notificationManager بقيمة الخاصية notificationManager. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:166]

```
167:                     stopForeground = {
```
> يمرّر المعامل المسمّى stopForeground ويفتح دالة لامدا (lambda) كقيمة له. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:167]

```
168:                         try { stopForeground(true) } catch (_: Exception) { }
```
> داخل اللامدا، ضمن try يستدعي stopForeground بالقيمة true، مع catch يبتلع أي Exception. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:168]

```
169:                         isInForeground = false
```
> داخل اللامدا، يسند القيمة false إلى المتغير isInForeground. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:169]

```
170:                     },
```
> يغلق دالة اللامدا الخاصة بـ stopForeground ويفصلها بفاصلة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:170]

```
171:                     stopService = { stopSelf() }
```
> يمرّر المعامل المسمّى stopService بدالة لامدا تستدعي stopSelf. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:171]

```
172:                 )
```
> يغلق قائمة معاملات استدعاء requestFullShutdownAndKill. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:172]

```
173:                 return START_NOT_STICKY
```
> يُعيد القيمة START_NOT_STICKY. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:173]

```
174:             }
```
> إغلاق نطاق (نهاية فرع ACTION_QUIT). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:174]

```
175:             ACTION_UPDATE_NOTIFICATION -> {
```
> يفتح فرع المطابقة لقيمة ACTION_UPDATE_NOTIFICATION. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:175]

```
176:                 // If we became eligible and are not in foreground yet, promote once
```
> تعليق: إن أصبحنا مؤهّلين ولسنا في المقدمة بعد، فرقِّ مرة واحدة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:176]

```
177:                 if (MeshServicePreferences.isBackgroundEnabled(true) && hasAllRequiredPermissions() && !isInForeground) {
```
> يفتح شرطاً يربط بـ && بين isBackgroundEnabled(true) وhasAllRequiredPermissions (امتلاك كل الأذونات المطلوبة) ونفي isInForeground. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:177]

```
178:                     val n = buildNotification(getUnifiedActivePeerCount())
```
> يُنشئ متغيراً n ويسند إليه ناتج buildNotification (بناء التنبيه) مع وسيط getUnifiedActivePeerCount (عدد النظائر النشطة الموحّد). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:178]

```
179:                     startForegroundCompat(n)
```
> يستدعي startForegroundCompat (بدء المقدمة بالتوافق) مع المعامل n. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:179]

```
180:                     isInForeground = true
```
> يسند القيمة true إلى المتغير isInForeground. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:180]

```
181:                 } else {
```
> يغلق نطاق الشرط ويفتح فرع البديل else. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:181]

```
182:                     updateNotification(force = true)
```
> يستدعي updateNotification (تحديث التنبيه) مع المعامل المسمّى force بقيمة true. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:182]

```
183:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:183]

```
184:             }
```
> إغلاق نطاق (نهاية فرع ACTION_UPDATE_NOTIFICATION). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:184]

```
185:             else -> { /* ACTION_START or null */ }
```
> يفتح فرع المطابقة الافتراضي else بجسم فارغ يحوي تعليقاً: ACTION_START أو null. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:185]

```
186:         }
```
> إغلاق نطاق (نهاية تعبير when). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:186]

```
187: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:187]

```
188:         // Ensure mesh is running (only after permissions are granted)
```
> تعليق: تأكّد أن الشبكة تعمل (فقط بعد منح الأذونات). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:188]

```
189:         ensureMeshStarted()
```
> يستدعي ensureMeshStarted (تأكيد بدء الشبكة). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:189]

```
190: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:190]

```
191:         // Promote exactly once when eligible, otherwise stay background (or stop)
```
> تعليق: رقِّ مرة واحدة بالضبط عند الأهلية، وإلا ابقَ في الخلفية (أو أوقف). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:191]

```
192:         if (MeshServicePreferences.isBackgroundEnabled(true) && hasAllRequiredPermissions() && !isInForeground) {
```
> يفتح شرطاً يربط بـ && بين isBackgroundEnabled(true) وhasAllRequiredPermissions ونفي isInForeground. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:192]

```
193:             val notification = buildNotification(getUnifiedActivePeerCount())
```
> يُنشئ متغيراً notification ويسند إليه ناتج buildNotification مع وسيط getUnifiedActivePeerCount. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:193]

```
194:             startForegroundCompat(notification)
```
> يستدعي startForegroundCompat مع المعامل notification. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:194]

```
195:             isInForeground = true
```
> يسند القيمة true إلى المتغير isInForeground. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:195]

```
196:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:196]

```
197: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:197]

```
198:         // Periodically refresh the notification with live network size
```
> تعليق: حدّث التنبيه دورياً بحجم الشبكة الحيّ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:198]

```
199:         if (updateJob == null) {
```
> يفتح شرطاً يتحقق أن updateJob يساوي null. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:199]

```
200:             updateJob = scope.launch {
```
> يسند إلى updateJob ناتج scope.launch ويفتح كتلة الكوروتين المُطلَقة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:200]
