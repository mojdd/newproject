# شريحة — app/src/main/java/com/bitchat/android/mesh/PowerManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يُعلِن أنّ هذا الملف ينتمي إلى الحزمة (package) المسماة `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:2]

```
3: import android.bluetooth.le.AdvertiseSettings
```
> يستورد (import) الصنف `AdvertiseSettings` الخاص بإعدادات الإعلان البلوتوثي منخفض الطاقة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:3]

```
4: import android.bluetooth.le.ScanSettings
```
> يستورد الصنف `ScanSettings` الخاص بإعدادات المسح (Scan) البلوتوثي منخفض الطاقة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:4]

```
5: import android.content.BroadcastReceiver
```
> يستورد الصنف `BroadcastReceiver` الخاص بمستقبِل البثّ (مستقبل الرسائل العامة في أندرويد). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:5]

```
6: import android.content.Context
```
> يستورد الصنف `Context` الذي يمثّل سياق التطبيق في أندرويد. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:6]

```
7: import android.content.Intent
```
> يستورد الصنف `Intent` الذي يمثّل النيّة (رسالة الطلب) في أندرويد. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:7]

```
8: import android.content.IntentFilter
```
> يستورد الصنف `IntentFilter` الذي يصفّي أنواع النيّات (Intent) المراد استقبالها. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:8]

```
9: import android.os.BatteryManager
```
> يستورد الصنف `BatteryManager` الخاص بإدارة معلومات البطارية في أندرويد. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:9]

```
10: import android.os.Handler
```
> يستورد الصنف `Handler` الخاص بمعالِج إرسال المهام إلى طابور رسائل خيط معيّن. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:10]

```
11: import android.os.Looper
```
> يستورد الصنف `Looper` الخاص بحلقة معالجة الرسائل لخيط معيّن. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:11]

```
12: import android.util.Log
```
> يستورد الصنف `Log` الخاص بتسجيل رسائل السجل (Log) في أندرويد. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:12]

```
13: import androidx.lifecycle.Lifecycle
```
> يستورد الصنف `Lifecycle` الخاص بدورة حياة المكوّنات في أندرويد. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:13]

```
14: import androidx.lifecycle.LifecycleEventObserver
```
> يستورد الواجهة `LifecycleEventObserver` (مراقِب أحداث دورة الحياة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:14]

```
15: import androidx.lifecycle.LifecycleOwner
```
> يستورد الواجهة `LifecycleOwner` (مالك دورة الحياة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:15]

```
16: import androidx.lifecycle.ProcessLifecycleOwner
```
> يستورد الصنف `ProcessLifecycleOwner` (مالك دورة حياة العملية كاملةً). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:16]

```
17: import kotlinx.coroutines.*
```
> يستورد كل العناصر من حزمة الكوروتينات (coroutines) في كوتلن. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:17]

```
18: import kotlin.math.max
```
> يستورد الدالة `max` (أكبر قيمة) من حزمة الرياضيات في كوتلن. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:18]

```
19: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:19]

```
20: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:20]

```
21:  * Power-aware Bluetooth management for bitchat
```
> تعليق: إدارة بلوتوث واعية للطاقة لتطبيق bitchat. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:21]

```
22:  * Adjusts scanning, advertising, and connection behavior based on battery state
```
> تعليق: تضبط سلوك المسح والإعلان والاتصال بناءً على حالة البطارية. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:22]

```
23:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:23]

```
24: class PowerManager(private val context: Context) : LifecycleEventObserver {
```
> يعرّف الصنف `PowerManager` (مدير الطاقة) الذي يأخذ في بانيه معاملاً خاصاً للقراءة فقط اسمه `context` من نوع `Context`، ويُحقّق الواجهة `LifecycleEventObserver`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:24]

```
25:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:25]

```
26:     companion object {
```
> يفتح كائن المرافقة (companion object) لحمل الأعضاء الساكنة للصنف. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:26]

```
27:         private const val TAG = "PowerManager"
```
> يعرّف ثابتاً خاصاً اسمه `TAG` (وسم السجل) بقيمة نصية `"PowerManager"`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:27]

```
28:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:28]

```
29:         // Battery thresholds
```
> تعليق: عتبات البطارية. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:29]

```
30:         private const val CRITICAL_BATTERY = com.bitchat.android.util.AppConstants.Power.CRITICAL_BATTERY_PERCENT
```
> يعرّف ثابتاً خاصاً اسمه `CRITICAL_BATTERY` (بطارية حرجة) قيمته `AppConstants.Power.CRITICAL_BATTERY_PERCENT`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:30]

```
31:         private const val LOW_BATTERY = com.bitchat.android.util.AppConstants.Power.LOW_BATTERY_PERCENT
```
> يعرّف ثابتاً خاصاً اسمه `LOW_BATTERY` (بطارية منخفضة) قيمته `AppConstants.Power.LOW_BATTERY_PERCENT`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:31]

```
32:         private const val MEDIUM_BATTERY = com.bitchat.android.util.AppConstants.Power.MEDIUM_BATTERY_PERCENT
```
> يعرّف ثابتاً خاصاً اسمه `MEDIUM_BATTERY` (بطارية متوسطة) قيمته `AppConstants.Power.MEDIUM_BATTERY_PERCENT`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:32]

```
33:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:33]

```
34:         // Scan duty cycle periods (ms)
```
> تعليق: فترات دورة عمل المسح (بالمللي ثانية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:34]

```
35:         private const val SCAN_ON_DURATION_NORMAL = com.bitchat.android.util.AppConstants.Power.SCAN_ON_DURATION_NORMAL_MS    // 8 seconds on
```
> يعرّف ثابتاً خاصاً اسمه `SCAN_ON_DURATION_NORMAL` (مدة تشغيل المسح العادية) قيمته `AppConstants.Power.SCAN_ON_DURATION_NORMAL_MS`، مع تعليق: ٨ ثوانٍ تشغيل. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:35]

```
36:         private const val SCAN_OFF_DURATION_NORMAL = com.bitchat.android.util.AppConstants.Power.SCAN_OFF_DURATION_NORMAL_MS   // 2 seconds off
```
> يعرّف ثابتاً خاصاً اسمه `SCAN_OFF_DURATION_NORMAL` (مدة إيقاف المسح العادية) قيمته `AppConstants.Power.SCAN_OFF_DURATION_NORMAL_MS`، مع تعليق: ٢ ثانية إيقاف. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:36]

```
37:         private const val SCAN_ON_DURATION_POWER_SAVE = com.bitchat.android.util.AppConstants.Power.SCAN_ON_DURATION_POWER_SAVE_MS    // 2 seconds on
```
> يعرّف ثابتاً خاصاً اسمه `SCAN_ON_DURATION_POWER_SAVE` (مدة تشغيل المسح في وضع توفير الطاقة) قيمته `AppConstants.Power.SCAN_ON_DURATION_POWER_SAVE_MS`، مع تعليق: ٢ ثانية تشغيل. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:37]

```
38:         private const val SCAN_OFF_DURATION_POWER_SAVE = com.bitchat.android.util.AppConstants.Power.SCAN_OFF_DURATION_POWER_SAVE_MS  // 8 seconds off
```
> يعرّف ثابتاً خاصاً اسمه `SCAN_OFF_DURATION_POWER_SAVE` (مدة إيقاف المسح في وضع توفير الطاقة) قيمته `AppConstants.Power.SCAN_OFF_DURATION_POWER_SAVE_MS`، مع تعليق: ٨ ثوانٍ إيقاف. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:38]

```
39:         private const val SCAN_ON_DURATION_ULTRA_LOW = com.bitchat.android.util.AppConstants.Power.SCAN_ON_DURATION_ULTRA_LOW_MS      // 1 second on
```
> يعرّف ثابتاً خاصاً اسمه `SCAN_ON_DURATION_ULTRA_LOW` (مدة تشغيل المسح في الوضع فائق الانخفاض) قيمته `AppConstants.Power.SCAN_ON_DURATION_ULTRA_LOW_MS`، مع تعليق: ١ ثانية تشغيل. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:39]

```
40:         private const val SCAN_OFF_DURATION_ULTRA_LOW = com.bitchat.android.util.AppConstants.Power.SCAN_OFF_DURATION_ULTRA_LOW_MS   // 10 seconds off
```
> يعرّف ثابتاً خاصاً اسمه `SCAN_OFF_DURATION_ULTRA_LOW` (مدة إيقاف المسح في الوضع فائق الانخفاض) قيمته `AppConstants.Power.SCAN_OFF_DURATION_ULTRA_LOW_MS`، مع تعليق: ١٠ ثوانٍ إيقاف. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:40]

```
41:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:41]

```
42:         // Connection limits
```
> تعليق: حدود الاتصال. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:42]

```
43:         private const val MAX_CONNECTIONS_NORMAL = com.bitchat.android.util.AppConstants.Power.MAX_CONNECTIONS_NORMAL
```
> يعرّف ثابتاً خاصاً اسمه `MAX_CONNECTIONS_NORMAL` (أقصى اتصالات في الوضع العادي) قيمته `AppConstants.Power.MAX_CONNECTIONS_NORMAL`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:43]

```
44:         private const val MAX_CONNECTIONS_POWER_SAVE = com.bitchat.android.util.AppConstants.Power.MAX_CONNECTIONS_POWER_SAVE
```
> يعرّف ثابتاً خاصاً اسمه `MAX_CONNECTIONS_POWER_SAVE` (أقصى اتصالات في وضع توفير الطاقة) قيمته `AppConstants.Power.MAX_CONNECTIONS_POWER_SAVE`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:44]

```
45:         private const val MAX_CONNECTIONS_ULTRA_LOW = com.bitchat.android.util.AppConstants.Power.MAX_CONNECTIONS_ULTRA_LOW
```
> يعرّف ثابتاً خاصاً اسمه `MAX_CONNECTIONS_ULTRA_LOW` (أقصى اتصالات في الوضع فائق الانخفاض) قيمته `AppConstants.Power.MAX_CONNECTIONS_ULTRA_LOW`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:45]

```
46:     }
```
> إغلاق نطاق (نهاية كائن المرافقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:46]

```
47:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:47]

```
48:     enum class PowerMode {
```
> يعرّف صنف تعداد (enum) اسمه `PowerMode` (وضع الطاقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:48]

```
49:         PERFORMANCE,    // Full power, no restrictions
```
> يعرّف قيمة التعداد `PERFORMANCE` (الأداء)، مع تعليق: طاقة كاملة بلا قيود. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:49]

```
50:         BALANCED,       // Moderate power saving
```
> يعرّف قيمة التعداد `BALANCED` (متوازن)، مع تعليق: توفير طاقة معتدل. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:50]

```
51:         POWER_SAVER,    // Aggressive power saving
```
> يعرّف قيمة التعداد `POWER_SAVER` (موفّر الطاقة)، مع تعليق: توفير طاقة عدواني (شديد). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:51]

```
52:         ULTRA_LOW_POWER // Minimal operations only
```
> يعرّف قيمة التعداد `ULTRA_LOW_POWER` (طاقة فائقة الانخفاض)، مع تعليق: عمليات دنيا فقط. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:52]

```
53:     }
```
> إغلاق نطاق (نهاية صنف التعداد). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:53]

```
54:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:54]

```
55:     private var currentMode = PowerMode.BALANCED
```
> يعرّف متغيّراً خاصاً اسمه `currentMode` (الوضع الحالي) ويسند إليه القيمة `PowerMode.BALANCED`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:55]

```
56:     private var isCharging = false
```
> يعرّف متغيّراً خاصاً اسمه `isCharging` (هل يشحن) ويسند إليه القيمة `false`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:56]

```
57:     private var batteryLevel = 100
```
> يعرّف متغيّراً خاصاً اسمه `batteryLevel` (مستوى البطارية) ويسند إليه القيمة `100`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:57]

```
58:     private var isAppInBackground = true
```
> يعرّف متغيّراً خاصاً اسمه `isAppInBackground` (هل التطبيق في الخلفية) ويسند إليه القيمة `true`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:58]

```
59:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:59]

```
60:     private val powerScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يعرّف قيمة خاصة للقراءة فقط اسمها `powerScope` (نطاق الطاقة) ويسند إليها نطاق كوروتين `CoroutineScope` مبنياً على موزّع الإدخال/الإخراج `Dispatchers.IO` مع مهمة مشرفة `SupervisorJob`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:60]

```
61:     private var dutyCycleJob: Job? = null
```
> يعرّف متغيّراً خاصاً اسمه `dutyCycleJob` (مهمة دورة العمل) من نوع `Job` القابل لِلَّاشيء، ويسند إليه `null`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:61]

```
62:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:62]

```
63:     var delegate: PowerManagerDelegate? = null
```
> يعرّف متغيّراً عاماً اسمه `delegate` (المفوَّض) من نوع `PowerManagerDelegate` القابل لِلَّاشيء، ويسند إليه `null`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:63]

```
64:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:64]

```
65:     // Battery monitoring
```
> تعليق: مراقبة البطارية. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:65]

```
66:     private val batteryReceiver = object : BroadcastReceiver() {
```
> يعرّف قيمة خاصة للقراءة فقط اسمها `batteryReceiver` (مستقبِل البطارية) ويسند إليها كائناً مجهولاً يرث `BroadcastReceiver`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:66]

```
67:         override fun onReceive(context: Context?, intent: Intent?) {
```
> يعيد تعريف الدالة `onReceive` (عند الاستقبال) التي تأخذ `context` و`intent` كلاهما قابل لِلَّاشيء. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:67]

```
68:             when (intent?.action) {
```
> يبدأ تعبير `when` (عندما) يفرّع على `intent?.action` (فعل النيّة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:68]

```
69:                 Intent.ACTION_BATTERY_CHANGED -> {
```
> فرع: إذا كان الفعل `Intent.ACTION_BATTERY_CHANGED` (تغيّرت البطارية) يفتح كتلة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:69]

```
70:                     val level = intent.getIntExtra(BatteryManager.EXTRA_LEVEL, -1)
```
> يعرّف قيمة للقراءة فقط اسمها `level` (المستوى) ويسند إليها قيمة `BatteryManager.EXTRA_LEVEL` المستخرجة من النيّة بقيمة افتراضية `-1`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:70]

```
71:                     val scale = intent.getIntExtra(BatteryManager.EXTRA_SCALE, -1)
```
> يعرّف قيمة للقراءة فقط اسمها `scale` (المقياس) ويسند إليها قيمة `BatteryManager.EXTRA_SCALE` المستخرجة من النيّة بقيمة افتراضية `-1`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:71]

```
72:                     if (level != -1 && scale != -1) {
```
> شرط: إذا كان `level` لا يساوي `-1` و`scale` لا يساوي `-1` يفتح كتلة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:72]

```
73:                         batteryLevel = (level * 100) / scale
```
> يسند إلى `batteryLevel` ناتج قسمة (`level` مضروباً في `100`) على `scale`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:73]

```
74:                     }
```
> إغلاق نطاق (نهاية شرط if). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:74]

```
75:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:75]

```
76:                     val status = intent.getIntExtra(BatteryManager.EXTRA_STATUS, -1)
```
> يعرّف قيمة للقراءة فقط اسمها `status` (الحالة) ويسند إليها قيمة `BatteryManager.EXTRA_STATUS` المستخرجة من النيّة بقيمة افتراضية `-1`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:76]

```
77:                     isCharging = status == BatteryManager.BATTERY_STATUS_CHARGING ||
```
> يسند إلى `isCharging` نتيجة المقارنة: هل `status` يساوي `BATTERY_STATUS_CHARGING` (يشحن)، أو (تكملة الشرط في السطر التالي). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:77]

```
78:                                 status == BatteryManager.BATTERY_STATUS_FULL
```
> تكملة الشرط: أو هل `status` يساوي `BATTERY_STATUS_FULL` (ممتلئة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:78]

```
79:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:79]

```
80:                     updatePowerMode()
```
> يستدعي الدالة `updatePowerMode` (تحديث وضع الطاقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:80]

```
81:                 }
```
> إغلاق نطاق (نهاية فرع تغيّر البطارية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:81]

```
82:                 Intent.ACTION_POWER_CONNECTED -> {
```
> فرع: إذا كان الفعل `Intent.ACTION_POWER_CONNECTED` (وُصِّلت الطاقة) يفتح كتلة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:82]

```
83:                     isCharging = true
```
> يسند إلى `isCharging` القيمة `true`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:83]

```
84:                     updatePowerMode()
```
> يستدعي الدالة `updatePowerMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:84]

```
85:                 }
```
> إغلاق نطاق (نهاية فرع توصيل الطاقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:85]

```
86:                 Intent.ACTION_POWER_DISCONNECTED -> {
```
> فرع: إذا كان الفعل `Intent.ACTION_POWER_DISCONNECTED` (فُصِلت الطاقة) يفتح كتلة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:86]

```
87:                     isCharging = false
```
> يسند إلى `isCharging` القيمة `false`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:87]

```
88:                     updatePowerMode()
```
> يستدعي الدالة `updatePowerMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:88]

```
89:                 }
```
> إغلاق نطاق (نهاية فرع فصل الطاقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:89]

```
90:             }
```
> إغلاق نطاق (نهاية تعبير when). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:90]

```
91:         }
```
> إغلاق نطاق (نهاية الدالة onReceive). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:91]

```
92:     }
```
> إغلاق نطاق (نهاية الكائن المجهول batteryReceiver). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:92]

```
93:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:93]

```
94:     init {
```
> يفتح كتلة التهيئة (init) التي تُنفَّذ عند إنشاء الكائن. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:94]

```
95:         registerBatteryReceiver()
```
> يستدعي الدالة `registerBatteryReceiver` (تسجيل مستقبِل البطارية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:95]

```
96:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:96]

```
97:         // Register for process lifecycle events on the main thread
```
> تعليق: التسجيل لأحداث دورة حياة العملية على الخيط الرئيسي. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:97]

```
98:         Handler(Looper.getMainLooper()).post {
```
> ينشئ `Handler` مرتبطاً بحلقة الخيط الرئيسي `Looper.getMainLooper()` ويرسل إليه كتلة لتُنفَّذ عبر `post`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:98]

```
99:             try {
```
> يفتح كتلة `try` (محاولة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:99]

```
100:                 ProcessLifecycleOwner.get().lifecycle.addObserver(this)
```
> يضيف هذا الكائن (`this`) مراقباً إلى دورة حياة `ProcessLifecycleOwner.get().lifecycle` عبر `addObserver`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:100]

```
101:             } catch (e: Exception) {
```
> يلتقط الاستثناء `Exception` في المتغيّر `e`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:101]

```
102:                 Log.e(TAG, "Failed to register lifecycle observer: ${e.message}")
```
> يسجّل خطأً عبر `Log.e` بالوسم `TAG` ونصّ "Failed to register lifecycle observer:" متبوعاً برسالة الاستثناء `e.message` (فشل تسجيل مراقب دورة الحياة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:102]

```
103:             }
```
> إغلاق نطاق (نهاية كتلة try/catch). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:103]

```
104:         }
```
> إغلاق نطاق (نهاية كتلة post الخاصة بالـ Handler). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:104]

```
105:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:105]

```
106:         updatePowerMode()
```
> يستدعي الدالة `updatePowerMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:106]

```
107:     }
```
> إغلاق نطاق (نهاية كتلة init). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:107]

```
108:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:108]

```
109:     fun start() {
```
> يعرّف الدالة `start` (ابدأ) دون معاملات. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:109]

```
110:         Log.i(TAG, "Starting power management")
```
> يسجّل معلومة عبر `Log.i` بالوسم `TAG` ونصّ "Starting power management" (بدء إدارة الطاقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:110]

```
111:         startDutyCycle()
```
> يستدعي الدالة `startDutyCycle` (بدء دورة العمل). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:111]

```
112:     }
```
> إغلاق نطاق (نهاية الدالة start). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:112]

```
113:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:113]

```
114:     fun stop() {
```
> يعرّف الدالة `stop` (أوقِف) دون معاملات. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:114]

```
115:         Log.i(TAG, "Stopping power management")
```
> يسجّل معلومة عبر `Log.i` بالوسم `TAG` ونصّ "Stopping power management" (إيقاف إدارة الطاقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:115]

```
116:         powerScope.cancel()
```
> يلغي نطاق الكوروتين `powerScope` عبر `cancel`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:116]

```
117:         unregisterBatteryReceiver()
```
> يستدعي الدالة `unregisterBatteryReceiver` (إلغاء تسجيل مستقبِل البطارية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:117]

```
118:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:118]

```
119:         // Unregister lifecycle observer
```
> تعليق: إلغاء تسجيل مراقب دورة الحياة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:119]

```
120:         Handler(Looper.getMainLooper()).post {
```
> ينشئ `Handler` مرتبطاً بحلقة الخيط الرئيسي `Looper.getMainLooper()` ويرسل إليه كتلة لتُنفَّذ عبر `post`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:120]

```
121:             try {
```
> يفتح كتلة `try` (محاولة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:121]

```
122:                 ProcessLifecycleOwner.get().lifecycle.removeObserver(this)
```
> يزيل هذا الكائن (`this`) من مراقبي دورة حياة `ProcessLifecycleOwner.get().lifecycle` عبر `removeObserver`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:122]

```
123:             } catch (e: Exception) {
```
> يلتقط الاستثناء `Exception` في المتغيّر `e`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:123]

```
124:                  Log.e(TAG, "Failed to remove lifecycle observer: ${e.message}")
```
> يسجّل خطأً عبر `Log.e` بالوسم `TAG` ونصّ "Failed to remove lifecycle observer:" متبوعاً برسالة الاستثناء `e.message` (فشل إزالة مراقب دورة الحياة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:124]

```
125:             }
```
> إغلاق نطاق (نهاية كتلة try/catch). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:125]

```
126:         }
```
> إغلاق نطاق (نهاية كتلة post الخاصة بالـ Handler). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:126]

```
127:     }
```
> إغلاق نطاق (نهاية الدالة stop). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:127]

```
128:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:128]

```
129:     override fun onStateChanged(source: LifecycleOwner, event: Lifecycle.Event) {
```
> يعيد تعريف الدالة `onStateChanged` (عند تغيّر الحالة) التي تأخذ `source` من نوع `LifecycleOwner` و`event` من نوع `Lifecycle.Event`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:129]

```
130:         when (event) {
```
> يبدأ تعبير `when` يفرّع على `event` (الحدث). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:130]

```
131:             Lifecycle.Event.ON_START -> {
```
> فرع: إذا كان الحدث `Lifecycle.Event.ON_START` (عند البدء) يفتح كتلة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:131]

```
132:                 Log.d(TAG, "Process lifecycle: ON_START (App coming to foreground)")
```
> يسجّل تنقيحاً عبر `Log.d` بالوسم `TAG` ونصّ "Process lifecycle: ON_START (App coming to foreground)" (دورة حياة العملية: البدء، التطبيق يأتي إلى المقدمة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:132]

```
133:                 isAppInBackground = false
```
> يسند إلى `isAppInBackground` القيمة `false`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:133]

```
134:                 updatePowerMode()
```
> يستدعي الدالة `updatePowerMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:134]

```
135:             }
```
> إغلاق نطاق (نهاية فرع ON_START). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:135]

```
136:             Lifecycle.Event.ON_STOP -> {
```
> فرع: إذا كان الحدث `Lifecycle.Event.ON_STOP` (عند التوقف) يفتح كتلة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:136]

```
137:                 Log.d(TAG, "Process lifecycle: ON_STOP (App going to background)")
```
> يسجّل تنقيحاً عبر `Log.d` بالوسم `TAG` ونصّ "Process lifecycle: ON_STOP (App going to background)" (دورة حياة العملية: التوقف، التطبيق يذهب إلى الخلفية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:137]

```
138:                 isAppInBackground = true
```
> يسند إلى `isAppInBackground` القيمة `true`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:138]

```
139:                 updatePowerMode()
```
> يستدعي الدالة `updatePowerMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:139]

```
140:             }
```
> إغلاق نطاق (نهاية فرع ON_STOP). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:140]

```
141:             else -> {}
```
> فرع: في أي حالة أخرى (`else`) كتلة فارغة لا تفعل شيئاً. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:141]

```
142:         }
```
> إغلاق نطاق (نهاية تعبير when). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:142]

```
143:     }
```
> إغلاق نطاق (نهاية الدالة onStateChanged). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:143]

```
144:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:144]

```
145:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:145]

```
146:      * Get scan settings optimized for current power mode
```
> تعليق: احصل على إعدادات المسح المحسّنة لوضع الطاقة الحالي. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:146]

```
147:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:147]

```
148:     fun getScanSettings(): ScanSettings {
```
> يعرّف الدالة `getScanSettings` (احصل على إعدادات المسح) التي تعيد قيمة من نوع `ScanSettings`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:148]

```
149:         val builder = ScanSettings.Builder()
```
> يعرّف قيمة للقراءة فقط اسمها `builder` (الباني) ويسند إليها كائن `ScanSettings.Builder()`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:149]

```
150:             .setCallbackType(ScanSettings.CALLBACK_TYPE_ALL_MATCHES)
```
> يضبط نوع رد النداء على `ScanSettings.CALLBACK_TYPE_ALL_MATCHES` (كل المطابقات) عبر `setCallbackType`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:150]

```
151: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:151]

```
152:         when (currentMode) {
```
> يبدأ تعبير `when` يفرّع على `currentMode` (الوضع الحالي). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:152]

```
153:             PowerMode.PERFORMANCE -> builder
```
> فرع: إذا كان الوضع `PowerMode.PERFORMANCE` (الأداء) يطبّق على `builder` (تتمة في الأسطر التالية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:153]

```
154:                 .setScanMode(ScanSettings.SCAN_MODE_LOW_LATENCY)
```
> يضبط وضع المسح على `ScanSettings.SCAN_MODE_LOW_LATENCY` (زمن استجابة منخفض) عبر `setScanMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:154]

```
155:                 .setMatchMode(ScanSettings.MATCH_MODE_AGGRESSIVE)
```
> يضبط وضع المطابقة على `ScanSettings.MATCH_MODE_AGGRESSIVE` (عدواني) عبر `setMatchMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:155]

```
156:                 .setNumOfMatches(ScanSettings.MATCH_NUM_MAX_ADVERTISEMENT)
```
> يضبط عدد المطابقات على `ScanSettings.MATCH_NUM_MAX_ADVERTISEMENT` (أقصى عدد إعلانات) عبر `setNumOfMatches`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:156]

```
157: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:157]

```
158:             PowerMode.BALANCED -> builder
```
> فرع: إذا كان الوضع `PowerMode.BALANCED` (متوازن) يطبّق على `builder` (تتمة في الأسطر التالية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:158]

```
159:                 .setScanMode(ScanSettings.SCAN_MODE_BALANCED)
```
> يضبط وضع المسح على `ScanSettings.SCAN_MODE_BALANCED` (متوازن) عبر `setScanMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:159]

```
160:                 .setMatchMode(ScanSettings.MATCH_MODE_AGGRESSIVE)
```
> يضبط وضع المطابقة على `ScanSettings.MATCH_MODE_AGGRESSIVE` (عدواني) عبر `setMatchMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:160]

```
161:                 .setNumOfMatches(ScanSettings.MATCH_NUM_ONE_ADVERTISEMENT)
```
> يضبط عدد المطابقات على `ScanSettings.MATCH_NUM_ONE_ADVERTISEMENT` (إعلان واحد) عبر `setNumOfMatches`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:161]

```
162: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:162]

```
163:             PowerMode.POWER_SAVER -> builder
```
> فرع: إذا كان الوضع `PowerMode.POWER_SAVER` (موفّر الطاقة) يطبّق على `builder` (تتمة في الأسطر التالية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:163]

```
164:                 .setScanMode(ScanSettings.SCAN_MODE_LOW_POWER)
```
> يضبط وضع المسح على `ScanSettings.SCAN_MODE_LOW_POWER` (طاقة منخفضة) عبر `setScanMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:164]

```
165:                 .setMatchMode(ScanSettings.MATCH_MODE_STICKY)
```
> يضبط وضع المطابقة على `ScanSettings.MATCH_MODE_STICKY` (لاصق/ثابت) عبر `setMatchMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:165]

```
166:                 .setNumOfMatches(ScanSettings.MATCH_NUM_ONE_ADVERTISEMENT)
```
> يضبط عدد المطابقات على `ScanSettings.MATCH_NUM_ONE_ADVERTISEMENT` (إعلان واحد) عبر `setNumOfMatches`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:166]

```
167: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:167]

```
168:             PowerMode.ULTRA_LOW_POWER -> builder
```
> فرع: إذا كان الوضع `PowerMode.ULTRA_LOW_POWER` (طاقة فائقة الانخفاض) يطبّق على `builder` (تتمة في الأسطر التالية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:168]

```
169:                 .setScanMode(ScanSettings.SCAN_MODE_LOW_POWER)
```
> يضبط وضع المسح على `ScanSettings.SCAN_MODE_LOW_POWER` (طاقة منخفضة) عبر `setScanMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:169]

```
170:                 .setMatchMode(ScanSettings.MATCH_MODE_STICKY)
```
> يضبط وضع المطابقة على `ScanSettings.MATCH_MODE_STICKY` (لاصق/ثابت) عبر `setMatchMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:170]

```
171:                 .setNumOfMatches(ScanSettings.MATCH_NUM_ONE_ADVERTISEMENT)
```
> يضبط عدد المطابقات على `ScanSettings.MATCH_NUM_ONE_ADVERTISEMENT` (إعلان واحد) عبر `setNumOfMatches`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:171]

```
172:         }
```
> إغلاق نطاق (نهاية تعبير when). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:172]

```
173: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:173]

```
174:         return builder.setReportDelay(0).build()
```
> يعيد نتيجة استدعاء `setReportDelay(0)` (تأخير التقرير صفر) ثم `build()` على `builder`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:174]

```
175:     }
```
> إغلاق نطاق (نهاية الدالة getScanSettings). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:175]

```
176:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:176]

```
177:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:177]

```
178:      * Get advertising settings optimized for current power mode
```
> تعليق: احصل على إعدادات الإعلان المحسّنة لوضع الطاقة الحالي. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:178]

```
179:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:179]

```
180:     fun getAdvertiseSettings(): AdvertiseSettings {
```
> يعرّف الدالة `getAdvertiseSettings` (احصل على إعدادات الإعلان) التي تعيد قيمة من نوع `AdvertiseSettings`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:180]

```
181:         return when (currentMode) {
```
> يعيد نتيجة تعبير `when` الذي يفرّع على `currentMode` (الوضع الحالي). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:181]

```
182:             PowerMode.PERFORMANCE -> AdvertiseSettings.Builder()
```
> فرع: إذا كان الوضع `PowerMode.PERFORMANCE` (الأداء) ينشئ كائن `AdvertiseSettings.Builder()` (تتمة في الأسطر التالية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:182]

```
183:                 .setAdvertiseMode(AdvertiseSettings.ADVERTISE_MODE_LOW_LATENCY)
```
> يضبط وضع الإعلان على `AdvertiseSettings.ADVERTISE_MODE_LOW_LATENCY` (زمن استجابة منخفض) عبر `setAdvertiseMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:183]

```
184:                 .setTxPowerLevel(AdvertiseSettings.ADVERTISE_TX_POWER_HIGH)
```
> يضبط مستوى طاقة الإرسال على `AdvertiseSettings.ADVERTISE_TX_POWER_HIGH` (عالٍ) عبر `setTxPowerLevel`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:184]

```
185:                 .setConnectable(true)
```
> يضبط قابلية الاتصال على `true` عبر `setConnectable`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:185]

```
186:                 .setTimeout(0)
```
> يضبط المهلة على `0` عبر `setTimeout`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:186]

```
187:                 .build()
```
> يبني الكائن النهائي عبر `build()`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:187]

```
188:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:188]

```
189:             PowerMode.BALANCED -> AdvertiseSettings.Builder()
```
> فرع: إذا كان الوضع `PowerMode.BALANCED` (متوازن) ينشئ كائن `AdvertiseSettings.Builder()` (تتمة في الأسطر التالية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:189]

```
190:                 .setAdvertiseMode(AdvertiseSettings.ADVERTISE_MODE_BALANCED)
```
> يضبط وضع الإعلان على `AdvertiseSettings.ADVERTISE_MODE_BALANCED` (متوازن) عبر `setAdvertiseMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:190]

```
191:                 .setTxPowerLevel(AdvertiseSettings.ADVERTISE_TX_POWER_MEDIUM)
```
> يضبط مستوى طاقة الإرسال على `AdvertiseSettings.ADVERTISE_TX_POWER_MEDIUM` (متوسط) عبر `setTxPowerLevel`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:191]

```
192:                 .setConnectable(true)
```
> يضبط قابلية الاتصال على `true` عبر `setConnectable`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:192]

```
193:                 .setTimeout(0)
```
> يضبط المهلة على `0` عبر `setTimeout`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:193]

```
194:                 .build()
```
> يبني الكائن النهائي عبر `build()`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:194]

```
195:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:195]

```
196:             PowerMode.POWER_SAVER -> AdvertiseSettings.Builder()
```
> فرع: إذا كان الوضع `PowerMode.POWER_SAVER` (موفّر الطاقة) ينشئ كائن `AdvertiseSettings.Builder()` (تتمة في الأسطر التالية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:196]

```
197:                 .setAdvertiseMode(AdvertiseSettings.ADVERTISE_MODE_LOW_POWER)
```
> يضبط وضع الإعلان على `AdvertiseSettings.ADVERTISE_MODE_LOW_POWER` (طاقة منخفضة) عبر `setAdvertiseMode`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:197]

```
198:                 .setTxPowerLevel(AdvertiseSettings.ADVERTISE_TX_POWER_LOW)
```
> يضبط مستوى طاقة الإرسال على `AdvertiseSettings.ADVERTISE_TX_POWER_LOW` (منخفض) عبر `setTxPowerLevel`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:198]

```
199:                 .setConnectable(true)
```
> يضبط قابلية الاتصال على `true` عبر `setConnectable`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:199]

```
200:                 .setTimeout(0)
```
> يضبط المهلة على `0` عبر `setTimeout`. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:200]
