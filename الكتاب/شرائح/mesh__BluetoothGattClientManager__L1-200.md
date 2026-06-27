# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يُعرّف اسم الحزمة (package) ويجعله com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:2]

```
3: import android.bluetooth.*
```
> يستورد (import) كل ما في حزمة android.bluetooth. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:3]

```
4: import android.bluetooth.le.BluetoothLeScanner
```
> يستورد الصنف ماسح البلوتوث منخفض الطاقة (BluetoothLeScanner). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:4]

```
5: import android.bluetooth.le.ScanCallback
```
> يستورد الصنف ردّ نداء المسح (ScanCallback). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:5]

```
6: import android.bluetooth.le.ScanFilter
```
> يستورد الصنف مرشّح المسح (ScanFilter). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:6]

```
7: import android.bluetooth.le.ScanResult
```
> يستورد الصنف نتيجة المسح (ScanResult). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:7]

```
8: import android.content.Context
```
> يستورد الصنف السياق (Context). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:8]

```
9: import android.os.ParcelUuid
```
> يستورد الصنف المعرّف الفريد القابل للنقل (ParcelUuid). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:9]

```
10: import android.util.Log
```
> يستورد الصنف السجلّ (Log). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:10]

```
11: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف حزمة بِتشات (BitchatPacket). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:11]

```
12: import com.bitchat.android.util.AppConstants
```
> يستورد الصنف ثوابت التطبيق (AppConstants). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:12]

```
13: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف نطاق الكوروتين (CoroutineScope). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:13]

```
14: import kotlinx.coroutines.delay
```
> يستورد الدالة تأخير (delay). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:14]

```
15: import kotlinx.coroutines.launch
```
> يستورد الدالة إطلاق (launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:15]

```
16: import java.util.*
```
> يستورد كل ما في حزمة java.util. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:16]

```
17: import kotlinx.coroutines.Job
```
> يستورد الصنف المهمّة (Job). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:17]

```
18: import com.bitchat.android.ui.debug.DebugSettingsManager
```
> يستورد الصنف مدير إعدادات التنقيح (DebugSettingsManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:18]

```
19: import com.bitchat.android.ui.debug.DebugScanResult
```
> يستورد الصنف نتيجة مسح التنقيح (DebugScanResult). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:19]

```
20: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:20]

```
21: /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:21]

```
22:  * Manages GATT client operations, scanning, and client-side connections
```
> تعليق: يُدير عمليات عميل GATT والمسح والاتصالات من جهة العميل. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:22]

```
23:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:23]

```
24: class BluetoothGattClientManager(
```
> يُعرّف الصنف مدير عميل GATT للبلوتوث (BluetoothGattClientManager) ويفتح قائمة معاملات المُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:24]

```
25:     private val context: Context,
```
> يُعرّف خاصية خاصّة للقراءة فقط باسم السياق (context) من نوع Context. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:25]

```
26:     private val connectionScope: CoroutineScope,
```
> يُعرّف خاصية خاصّة للقراءة فقط باسم نطاق الاتصال (connectionScope) من نوع CoroutineScope. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:26]

```
27:     private val connectionTracker: BluetoothConnectionTracker,
```
> يُعرّف خاصية خاصّة للقراءة فقط باسم متتبّع الاتصال (connectionTracker) من نوع BluetoothConnectionTracker. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:27]

```
28:     private val permissionManager: BluetoothPermissionManager,
```
> يُعرّف خاصية خاصّة للقراءة فقط باسم مدير الأذونات (permissionManager) من نوع BluetoothPermissionManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:28]

```
29:     private val powerManager: PowerManager,
```
> يُعرّف خاصية خاصّة للقراءة فقط باسم مدير الطاقة (powerManager) من نوع PowerManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:29]

```
30:     private val delegate: BluetoothConnectionManagerDelegate?
```
> يُعرّف خاصية خاصّة للقراءة فقط باسم المفوَّض (delegate) من نوع BluetoothConnectionManagerDelegate قابل للقيمة الفارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:30]

```
31: ) {
```
> يُغلق قائمة معاملات المُنشئ ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:31]

```
32:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:32]

```
33:     companion object {
```
> يفتح الكائن المرافق (companion object). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:33]

```
34:         private const val TAG = "BluetoothGattClientManager"
```
> يُعرّف ثابتاً خاصّاً باسم الوسم (TAG) بقيمة نصية "BluetoothGattClientManager". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:34]

```
35:         // Self-healing scan recovery tuning
```
> تعليق: ضبط استرداد المسح ذاتي الإصلاح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:35]

```
36:         private const val SCAN_RETRY_BASE_MS = 3_000L          // base backoff for transient scan failures
```
> يُعرّف ثابتاً خاصّاً باسم زمن التراجع الأساس للمسح (SCAN_RETRY_BASE_MS) بقيمة 3000 ميلي ثانية من نوع Long، مع تعليق: تراجع أساس لإخفاقات المسح العابرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:36]

```
37:         private const val SCAN_MAX_RETRY_DELAY_MS = 30_000L    // cap on backoff delay
```
> يُعرّف ثابتاً خاصّاً باسم أقصى تأخير إعادة محاولة المسح (SCAN_MAX_RETRY_DELAY_MS) بقيمة 30000 ميلي ثانية من نوع Long، مع تعليق: سقف على تأخير التراجع. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:37]

```
38:         private const val SCAN_WATCHDOG_INTERVAL_MS = 30_000L  // how often to verify the scanner is alive
```
> يُعرّف ثابتاً خاصّاً باسم فترة كلب حراسة المسح (SCAN_WATCHDOG_INTERVAL_MS) بقيمة 30000 ميلي ثانية من نوع Long، مع تعليق: كم مرّة يُتحقَّق أنّ الماسح حيّ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:38]

```
39:         private const val SCAN_STALE_RESULT_MS = 120_000L      // force a scan restart if no results for this long
```
> يُعرّف ثابتاً خاصّاً باسم زمن النتيجة القديمة للمسح (SCAN_STALE_RESULT_MS) بقيمة 120000 ميلي ثانية من نوع Long، مع تعليق: يفرض إعادة تشغيل المسح إن لم تَرِد نتائج طوال هذه المدة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:39]

```
40:     }
```
> إغلاق نطاق (إغلاق الكائن المرافق). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:40]

```
41:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:41]

```
42:     // Core Bluetooth components
```
> تعليق: مكوّنات البلوتوث الأساسية. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:42]

```
43:     private val bluetoothManager: BluetoothManager = 
```
> يُعرّف خاصية خاصّة للقراءة فقط باسم مدير البلوتوث (bluetoothManager) من نوع BluetoothManager ويبدأ إسناد قيمتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:43]

```
44:         context.getSystemService(Context.BLUETOOTH_SERVICE) as BluetoothManager
```
> يستدعي من السياق الدالة getSystemService بوسيط Context.BLUETOOTH_SERVICE ويحوّل الناتج بالتحويل as إلى BluetoothManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:44]

```
45:     private val bluetoothAdapter: BluetoothAdapter? = bluetoothManager.adapter
```
> يُعرّف خاصية خاصّة للقراءة فقط باسم مهايئ البلوتوث (bluetoothAdapter) من نوع BluetoothAdapter قابل للقيمة الفارغة ويُسند إليها bluetoothManager.adapter. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:45]

```
46:     private val bleScanner: BluetoothLeScanner? = bluetoothAdapter?.bluetoothLeScanner
```
> يُعرّف خاصية خاصّة للقراءة فقط باسم ماسح BLE‏ (bleScanner) من نوع BluetoothLeScanner قابل للقيمة الفارغة ويُسند إليها bluetoothAdapter?.bluetoothLeScanner بالوصول الآمن. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:46]

```
47: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:47]

```
48:     private fun isBleTransportEnabled(): Boolean {
```
> يُعرّف دالة خاصّة باسم هل نقل BLE مُفعَّل (isBleTransportEnabled) تُعيد Boolean ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:48]

```
49:         return try {
```
> يبدأ عبارة return بكتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:49]

```
50:             com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().bleEnabled.value
```
> يستدعي getInstance على DebugSettingsManager ثم يقرأ القيمة value من الخاصية bleEnabled. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:50]

```
51:         } catch (_: Exception) {
```
> يُغلق كتلة try ويفتح كتلة catch تلتقط أيّ Exception دون تسمية متغيّرها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:51]

```
52:             try { com.bitchat.android.ui.debug.DebugPreferenceManager.getBleEnabled(true) } catch (_: Exception) { true }
```
> يستدعي ضمن try داخليّ الدالة getBleEnabled على DebugPreferenceManager بوسيط true، وعند الالتقاط لأيّ Exception يُعيد true. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:52]

```
53:         }
```
> إغلاق نطاق (إغلاق كتلة catch). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:53]

```
54:     }
```
> إغلاق نطاق (إغلاق الدالة isBleTransportEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:54]

```
55: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:55]

```
56:     private fun isClientRoleEnabled(): Boolean {
```
> يُعرّف دالة خاصّة باسم هل دور العميل مُفعَّل (isClientRoleEnabled) تُعيد Boolean ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:56]

```
57:         return isBleTransportEnabled() &&
```
> يبدأ عبارة return بحاصل العبارة المنطقية: استدعاء isBleTransportEnabled مع عامل «و» المنطقي &&. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:57]

```
58:             (try { com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().gattClientEnabled.value } catch (_: Exception) { true })
```
> يُكمل الطرف الثاني للعبارة: ضمن try يقرأ value من gattClientEnabled عبر getInstance على DebugSettingsManager، وعند الالتقاط لأيّ Exception يُعيد true. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:58]

```
59:     }
```
> إغلاق نطاق (إغلاق الدالة isClientRoleEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:59]

```
60:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:60]

```
61:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:61]

```
62:      * Public: Connect to a device by MAC address (for debug UI)
```
> تعليق: عامّ: الاتصال بجهاز عبر عنوان MAC (لواجهة التنقيح). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:62]

```
63:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:63]

```
64:     fun connectToAddress(deviceAddress: String): Boolean {
```
> يُعرّف دالة عامّة باسم الاتصال بعنوان (connectToAddress) تأخذ معاملاً نصيّاً اسمه عنوان الجهاز (deviceAddress) وتُعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:64]

```
65:         if (!isClientRoleEnabled()) {
```
> يفتح شرط if يفحص نفي استدعاء isClientRoleEnabled. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:65]

```
66:             Log.i(TAG, "connectToAddress skipped: BLE client disabled")
```
> يستدعي Log.i بالوسم TAG والرسالة "connectToAddress skipped: BLE client disabled". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:66]

```
67:             return false
```
> يُعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:67]

```
68:         }
```
> إغلاق نطاق (إغلاق شرط if). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:68]

```
69:         val device = bluetoothAdapter?.getRemoteDevice(deviceAddress)
```
> يُعرّف متغيّراً للقراءة فقط باسم الجهاز (device) ويُسند إليه ناتج استدعاء getRemoteDevice بالوسيط deviceAddress على bluetoothAdapter بالوصول الآمن. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:69]

```
70:         return if (device != null) {
```
> يبدأ عبارة return بتعبير if يفحص أنّ device لا يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:70]

```
71:             val rssi = connectionTracker.getBestRSSI(deviceAddress) ?: -50
```
> يُعرّف متغيّراً للقراءة فقط باسم قوّة الإشارة (rssi) ويُسند إليه ناتج getBestRSSI بالوسيط deviceAddress على connectionTracker، أو القيمة ‑50 عند كون الناتج فارغاً عبر عامل إلفيس. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:71]

```
72:             connectToDevice(device, rssi)
```
> يستدعي الدالة connectToDevice بالوسيطين device و rssi. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:72]

```
73:             true
```
> قيمة الفرع true (قيمة تعبير if في هذا الفرع). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:73]

```
74:         } else {
```
> يُغلق فرع then ويفتح فرع else. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:74]

```
75:             Log.w(TAG, "connectToAddress: No device for $deviceAddress")
```
> يستدعي Log.w بالوسم TAG والرسالة "connectToAddress: No device for $deviceAddress" مع إقحام قيمة deviceAddress. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:75]

```
76:             false
```
> قيمة الفرع false (قيمة تعبير if في فرع else). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:76]

```
77:         }
```
> إغلاق نطاق (إغلاق فرع else). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:77]

```
78:     }
```
> إغلاق نطاق (إغلاق الدالة connectToAddress). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:78]

```
79: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:79]

```
80:     // Scan management
```
> تعليق: إدارة المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:80]

```
81:     private var scanCallback: ScanCallback? = null
```
> يُعرّف خاصية خاصّة قابلة للتغيير باسم ردّ نداء المسح (scanCallback) من نوع ScanCallback قابل للقيمة الفارغة ويُسند إليها null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:81]

```
82:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:82]

```
83:     // Scan rate limiting to prevent "scanning too frequently" errors
```
> تعليق: تحديد معدّل المسح لمنع أخطاء "المسح بتواتر مفرط". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:83]

```
84:     private var lastScanStartTime = 0L
```
> يُعرّف خاصية خاصّة قابلة للتغيير باسم زمن آخر بدء مسح (lastScanStartTime) ويُسند إليها 0 من نوع Long. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:84]

```
85:     private var lastScanStopTime = 0L
```
> يُعرّف خاصية خاصّة قابلة للتغيير باسم زمن آخر إيقاف مسح (lastScanStopTime) ويُسند إليها 0 من نوع Long. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:85]

```
86:     @Volatile private var isCurrentlyScanning = false
```
> يُعرّف خاصية خاصّة قابلة للتغيير ومُعلَّمة بالشارح @Volatile باسم هل يجري المسح حالياً (isCurrentlyScanning) ويُسند إليها false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:86]

```
87:     private val scanRateLimit = 5000L // Minimum 5 seconds between scan start attempts
```
> يُعرّف خاصية خاصّة للقراءة فقط باسم حدّ معدّل المسح (scanRateLimit) بقيمة 5000 من نوع Long، مع تعليق: 5 ثوانٍ كحدّ أدنى بين محاولات بدء المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:87]

```
88: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:88]

```
89:     // Self-healing scan state.
```
> تعليق: حالة المسح ذاتي الإصلاح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:89]

```
90:     // scanningDesired distinguishes "we want to be scanning but it isn't running" (a fault to recover
```
> تعليق: المتغيّر scanningDesired يميّز "نريد أن نمسح لكنّه لا يعمل" (عطل يجب التعافي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:90]

```
91:     // from) from "scanning is intentionally off" (e.g. duty-cycle OFF window or client disabled).
```
> تعليق: منه) عن "المسح مُطفأ عمداً" (مثل نافذة إطفاء دورة العمل أو تعطيل العميل). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:91]

```
92:     @Volatile private var scanningDesired = false
```
> يُعرّف خاصية خاصّة قابلة للتغيير ومُعلَّمة بالشارح @Volatile باسم المسح مرغوب (scanningDesired) ويُسند إليها false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:92]

```
93:     @Volatile private var lastScanResultTime = 0L
```
> يُعرّف خاصية خاصّة قابلة للتغيير ومُعلَّمة بالشارح @Volatile باسم زمن آخر نتيجة مسح (lastScanResultTime) ويُسند إليها 0 من نوع Long. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:93]

```
94:     private var scanRetryCount = 0
```
> يُعرّف خاصية خاصّة قابلة للتغيير باسم عدّاد إعادة محاولة المسح (scanRetryCount) ويُسند إليها 0. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:94]

```
95:     private var scanWatchdogJob: Job? = null
```
> يُعرّف خاصية خاصّة قابلة للتغيير باسم مهمّة كلب حراسة المسح (scanWatchdogJob) من نوع Job قابل للقيمة الفارغة ويُسند إليها null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:95]

```
96:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:96]

```
97:     // RSSI monitoring state
```
> تعليق: حالة مراقبة قوّة الإشارة RSSI. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:97]

```
98:     private var rssiMonitoringJob: Job? = null
```
> يُعرّف خاصية خاصّة قابلة للتغيير باسم مهمّة مراقبة قوّة الإشارة (rssiMonitoringJob) من نوع Job قابل للقيمة الفارغة ويُسند إليها null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:98]

```
99:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:99]

```
100:     // State management
```
> تعليق: إدارة الحالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:100]

```
101:     private var isActive = false
```
> يُعرّف خاصية خاصّة قابلة للتغيير باسم هل نشط (isActive) ويُسند إليها false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:101]

```
102:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:102]

```
103:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:103]

```
104:      * Start client manager
```
> تعليق: بدء مدير العميل. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:104]

```
105:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:105]

```
106:     fun start(): Boolean {
```
> يُعرّف دالة عامّة باسم بدء (start) تُعيد Boolean ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:106]

```
107:         // Respect debug setting
```
> تعليق: احترام إعداد التنقيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:107]

```
108:         if (!isClientRoleEnabled()) {
```
> يفتح شرط if يفحص نفي استدعاء isClientRoleEnabled. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:108]

```
109:             Log.i(TAG, "Client start skipped: BLE/GATT Client disabled in debug settings")
```
> يستدعي Log.i بالوسم TAG والرسالة "Client start skipped: BLE/GATT Client disabled in debug settings". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:109]

```
110:             return false
```
> يُعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:110]

```
111:         }
```
> إغلاق نطاق (إغلاق شرط if). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:111]

```
112: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:112]

```
113:         if (isActive) {
```
> يفتح شرط if يفحص أنّ isActive يساوي true. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:113]

```
114:             Log.d(TAG, "GATT client already active; start is a no-op")
```
> يستدعي Log.d بالوسم TAG والرسالة "GATT client already active; start is a no-op". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:114]

```
115:             return true
```
> يُعيد true. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:115]

```
116:         }
```
> إغلاق نطاق (إغلاق شرط if). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:116]

```
117:         if (!permissionManager.hasBluetoothPermissions()) {
```
> يفتح شرط if يفحص نفي استدعاء hasBluetoothPermissions على permissionManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:117]

```
118:             Log.e(TAG, "Missing Bluetooth permissions")
```
> يستدعي Log.e بالوسم TAG والرسالة "Missing Bluetooth permissions". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:118]

```
119:             return false
```
> يُعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:119]

```
120:         }
```
> إغلاق نطاق (إغلاق شرط if). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:120]

```
121:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:121]

```
122:         if (bluetoothAdapter?.isEnabled != true) {
```
> يفتح شرط if يفحص أنّ bluetoothAdapter?.isEnabled لا يساوي true عبر الوصول الآمن. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:122]

```
123:             Log.e(TAG, "Bluetooth is not enabled")
```
> يستدعي Log.e بالوسم TAG والرسالة "Bluetooth is not enabled". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:123]

```
124:             return false
```
> يُعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:124]

```
125:         }
```
> إغلاق نطاق (إغلاق شرط if). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:125]

```
126:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:126]

```
127:         if (bleScanner == null) {
```
> يفتح شرط if يفحص أنّ bleScanner يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:127]

```
128:             Log.e(TAG, "BLE scanner not available")
```
> يستدعي Log.e بالوسم TAG والرسالة "BLE scanner not available". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:128]

```
129:             return false
```
> يُعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:129]

```
130:         }
```
> إغلاق نطاق (إغلاق شرط if). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:130]

```
131:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:131]

```
132:         isActive = true
```
> يُسند القيمة true إلى الخاصية isActive. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:132]

```
133:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:133]

```
134:         connectionScope.launch {
```
> يستدعي launch على connectionScope ويفتح لمدا الكوروتين. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:134]

```
135:             if (powerManager.shouldUseDutyCycle()) {
```
> يفتح شرط if يفحص استدعاء shouldUseDutyCycle على powerManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:135]

```
136:                 Log.i(TAG, "Using power-aware duty cycling")
```
> يستدعي Log.i بالوسم TAG والرسالة "Using power-aware duty cycling". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:136]

```
137:                 // Duty cycle drives onScanStateChanged(true/false); scanningDesired follows that.
```
> تعليق: دورة العمل تقود onScanStateChanged(true/false)؛ وscanningDesired يتبعها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:137]

```
138:             } else {
```
> يُغلق فرع then ويفتح فرع else. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:138]

```
139:                 scanningDesired = true
```
> يُسند القيمة true إلى الخاصية scanningDesired. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:139]

```
140:                 startScanning()
```
> يستدعي الدالة startScanning. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:140]

```
141:             }
```
> إغلاق نطاق (إغلاق فرع else). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:141]

```
142:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:142]

```
143:             // Start RSSI monitoring
```
> تعليق: بدء مراقبة قوّة الإشارة RSSI. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:143]

```
144:             startRSSIMonitoring()
```
> يستدعي الدالة startRSSIMonitoring. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:144]

```
145:             // Start the scan watchdog so a silently-dead or wedged scanner self-heals.
```
> تعليق: بدء كلب حراسة المسح كي يتعافى ذاتياً الماسح الميّت بصمت أو المنحشر. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:145]

```
146:             startScanWatchdog()
```
> يستدعي الدالة startScanWatchdog. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:146]

```
147:         }
```
> إغلاق نطاق (إغلاق لمدا الكوروتين). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:147]

```
148:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:148]

```
149:         return true
```
> يُعيد true. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:149]

```
150:     }
```
> إغلاق نطاق (إغلاق الدالة start). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:150]

```
151:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:151]

```
152:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:152]

```
153:      * Stop client manager
```
> تعليق: إيقاف مدير العميل. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:153]

```
154:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:154]

```
155:     fun stop() {
```
> يُعرّف دالة عامّة باسم إيقاف (stop) بلا قيمة مُعادة ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:155]

```
156:         scanningDesired = false
```
> يُسند القيمة false إلى الخاصية scanningDesired. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:156]

```
157:         stopScanWatchdog()
```
> يستدعي الدالة stopScanWatchdog. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:157]

```
158:         if (!isActive) {
```
> يفتح شرط if يفحص نفي isActive. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:158]

```
159:             // Idempotent stop
```
> تعليق: إيقاف متعادل (يُعطي النتيجة نفسها عند تكراره). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:159]

```
160:             stopScanning()
```
> يستدعي الدالة stopScanning. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:160]

```
161:             stopRSSIMonitoring()
```
> يستدعي الدالة stopRSSIMonitoring. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:161]

```
162:             Log.i(TAG, "GATT client manager stopped (already inactive)")
```
> يستدعي Log.i بالوسم TAG والرسالة "GATT client manager stopped (already inactive)". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:162]

```
163:             return
```
> يُعيد من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:163]

```
164:         }
```
> إغلاق نطاق (إغلاق شرط if). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:164]

```
165: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:165]

```
166:         isActive = false
```
> يُسند القيمة false إلى الخاصية isActive. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:166]

```
167:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:167]

```
168:         connectionScope.launch {
```
> يستدعي launch على connectionScope ويفتح لمدا الكوروتين. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:168]

```
169:             // Disconnect all client connections decisively
```
> تعليق: قطع كل اتصالات العميل بشكل حاسم. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:169]

```
170:             try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:170]

```
171:                 val conns = connectionTracker.getConnectedDevices().values.filter { it.isClient && it.gatt != null }
```
> يُعرّف متغيّراً للقراءة فقط باسم الاتصالات (conns) ويُسند إليه القيم values من getConnectedDevices على connectionTracker بعد ترشيحها بأن يكون it.isClient محقّقاً و it.gatt لا يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:171]

```
172:                 conns.forEach { dc ->
```
> يستدعي forEach على conns بمعامل لمدا اسمه dc ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:172]

```
173:                     try { dc.gatt?.disconnect() } catch (_: Exception) { }
```
> يستدعي ضمن try الدالة disconnect على dc.gatt بالوصول الآمن، وعند الالتقاط لأيّ Exception لا يفعل شيئاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:173]

```
174:                 }
```
> إغلاق نطاق (إغلاق لمدا forEach). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:174]

```
175:             } catch (_: Exception) { }
```
> يُغلق كتلة try ويفتح كتلة catch تلتقط أيّ Exception دون فعل شيء. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:175]

```
176:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:176]

```
177:             stopScanning()
```
> يستدعي الدالة stopScanning. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:177]

```
178:             stopRSSIMonitoring()
```
> يستدعي الدالة stopRSSIMonitoring. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:178]

```
179:             Log.i(TAG, "GATT client manager stopped")
```
> يستدعي Log.i بالوسم TAG والرسالة "GATT client manager stopped". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:179]

```
180:         }
```
> إغلاق نطاق (إغلاق لمدا الكوروتين). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:180]

```
181:     }
```
> إغلاق نطاق (إغلاق الدالة stop). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:181]

```
182:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:182]

```
183:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:183]

```
184:      * Handle scan state changes from power manager
```
> تعليق: معالجة تغيّرات حالة المسح القادمة من مدير الطاقة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:184]

```
185:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:185]

```
186:     fun onScanStateChanged(shouldScan: Boolean) {
```
> يُعرّف دالة عامّة باسم عند تغيّر حالة المسح (onScanStateChanged) تأخذ معاملاً منطقيّاً اسمه ينبغي المسح (shouldScan) بلا قيمة مُعادة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:186]

```
187:         val enabled = isClientRoleEnabled()
```
> يُعرّف متغيّراً للقراءة فقط باسم مُفعَّل (enabled) ويُسند إليه ناتج استدعاء isClientRoleEnabled. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:187]

```
188:         scanningDesired = shouldScan && enabled
```
> يُسند إلى scanningDesired حاصل العبارة المنطقية shouldScan «و» enabled. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:188]

```
189:         if (shouldScan && enabled) {
```
> يفتح شرط if يفحص أنّ shouldScan «و» enabled محقّقان. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:189]

```
190:             startScanning()
```
> يستدعي الدالة startScanning. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:190]

```
191:         } else {
```
> يُغلق فرع then ويفتح فرع else. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:191]

```
192:             stopScanning()
```
> يستدعي الدالة stopScanning. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:192]

```
193:         }
```
> إغلاق نطاق (إغلاق فرع else). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:193]

```
194:     }
```
> إغلاق نطاق (إغلاق الدالة onScanStateChanged). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:194]

```
195:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:195]

```
196:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:196]

```
197:      * Start periodic RSSI monitoring for all client connections
```
> تعليق: بدء مراقبة دورية لقوّة الإشارة RSSI لكل اتصالات العميل. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:197]

```
198:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:198]

```
199:     private fun startRSSIMonitoring() {
```
> يُعرّف دالة خاصّة باسم بدء مراقبة قوّة الإشارة (startRSSIMonitoring) بلا قيمة مُعادة ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:199]

```
200:         rssiMonitoringJob?.cancel()
```
> يستدعي الدالة cancel على rssiMonitoringJob بالوصول الآمن. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:200]
