# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:2]

```
3: import android.bluetooth.*
```
> يستورد كل أسماء حزمة android.bluetooth باستعمال النجمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:3]

```
4: import android.bluetooth.le.AdvertiseCallback
```
> يستورد رد نداء الإعلان (AdvertiseCallback) من حزمة android.bluetooth.le. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:4]

```
5: import android.bluetooth.le.AdvertiseData
```
> يستورد بيانات الإعلان (AdvertiseData) من حزمة android.bluetooth.le. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:5]

```
6: import android.bluetooth.le.AdvertiseSettings
```
> يستورد إعدادات الإعلان (AdvertiseSettings) من حزمة android.bluetooth.le. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:6]

```
7: import android.bluetooth.le.BluetoothLeAdvertiser
```
> يستورد المُعلِن منخفض الطاقة (BluetoothLeAdvertiser) من حزمة android.bluetooth.le. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:7]

```
8: import android.content.Context
```
> يستورد السياق (Context) من حزمة android.content. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:8]

```
9: import android.os.ParcelUuid
```
> يستورد المُعرّف الفريد القابل للطرد (ParcelUuid) من حزمة android.os. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:9]

```
10: import android.util.Log
```
> يستورد أداة التسجيل (Log) من حزمة android.util. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:10]

```
11: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد حزمة البيانات (BitchatPacket) من حزمة com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:11]

```
12: import com.bitchat.android.util.AppConstants
```
> يستورد ثوابت التطبيق (AppConstants) من حزمة com.bitchat.android.util. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:12]

```
13: import kotlinx.coroutines.CoroutineScope
```
> يستورد نطاق الكوروتين (CoroutineScope) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:13]

```
14: import kotlinx.coroutines.delay
```
> يستورد دالة التأخير (delay) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:14]

```
15: import kotlinx.coroutines.launch
```
> يستورد دالة الإطلاق (launch) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:15]

```
16: import java.util.*
```
> يستورد كل أسماء حزمة java.util باستعمال النجمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:17]

```
18: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:18]

```
19:  * Manages GATT server operations, advertising, and server-side connections
```
> تعليق: يدير عمليات خادم GATT والإعلان والاتصالات من جهة الخادم. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:19]

```
20:  */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:20]

```
21: class BluetoothGattServerManager(
```
> يعرّف الصنف مدير خادم GATT للبلوتوث (BluetoothGattServerManager) ويبدأ قائمة معاملات المُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:21]

```
22:     private val context: Context,
```
> يعرّف خاصية المُنشئ الخاصة السياق (context) من نوع Context. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:22]

```
23:     private val connectionScope: CoroutineScope,
```
> يعرّف خاصية المُنشئ الخاصة نطاق الاتصال (connectionScope) من نوع CoroutineScope. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:23]

```
24:     private val connectionTracker: BluetoothConnectionTracker,
```
> يعرّف خاصية المُنشئ الخاصة متعقّب الاتصال (connectionTracker) من نوع BluetoothConnectionTracker. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:24]

```
25:     private val permissionManager: BluetoothPermissionManager,
```
> يعرّف خاصية المُنشئ الخاصة مدير الأذونات (permissionManager) من نوع BluetoothPermissionManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:25]

```
26:     private val powerManager: PowerManager,
```
> يعرّف خاصية المُنشئ الخاصة مدير الطاقة (powerManager) من نوع PowerManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:26]

```
27:     private val delegate: BluetoothConnectionManagerDelegate?,
```
> يعرّف خاصية المُنشئ الخاصة المفوَّض (delegate) من نوع BluetoothConnectionManagerDelegate القابل للقيمة الفارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:27]

```
28:     private val myPeerID: String
```
> يعرّف خاصية المُنشئ الخاصة معرّف نظيري (myPeerID) من نوع نص. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:28]

```
29: ) {
```
> يغلق قائمة معاملات المُنشئ ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:29]

```
30:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:30]

```
31:     companion object {
```
> يفتح الكائن المرافق (companion object) للصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:31]

```
32:         private const val TAG = "BluetoothGattServerManager"
```
> يعرّف الثابت الخاص الوسم (TAG) بالقيمة النصية "BluetoothGattServerManager". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:32]

```
33:         // Self-healing advertising recovery tuning
```
> تعليق: ضبط استرداد الإعلان ذاتي الإصلاح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:33]

```
34:         private const val ADVERTISE_RETRY_BASE_MS = 3_000L      // base backoff for transient advertise failures
```
> يعرّف الثابت الخاص أساس مهلة إعادة المحاولة بالملي ثانية (ADVERTISE_RETRY_BASE_MS) بالقيمة 3000 من النوع Long، مع تعليق: أساس التراجع لأخطاء الإعلان العابرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:34]

```
35:         private const val ADVERTISE_MAX_RETRY_DELAY_MS = 30_000L // cap on backoff delay
```
> يعرّف الثابت الخاص أقصى تأخير لإعادة المحاولة بالملي ثانية (ADVERTISE_MAX_RETRY_DELAY_MS) بالقيمة 30000 من النوع Long، مع تعليق: سقف تأخير التراجع. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:35]

```
36:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:36]

```
37:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:37]

```
38:     // Core Bluetooth components
```
> تعليق: مكونات البلوتوث الأساسية. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:38]

```
39:     private val bluetoothManager: BluetoothManager = 
```
> يعرّف الخاصية الخاصة مدير البلوتوث (bluetoothManager) من نوع BluetoothManager ويبدأ تهيئتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:39]

```
40:         context.getSystemService(Context.BLUETOOTH_SERVICE) as BluetoothManager
```
> يسند للخاصية ناتج استدعاء context.getSystemService بالوسيط Context.BLUETOOTH_SERVICE بعد تحويله إلى BluetoothManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:40]

```
41:     private val bluetoothAdapter: BluetoothAdapter? = bluetoothManager.adapter
```
> يعرّف الخاصية الخاصة محوّل البلوتوث (bluetoothAdapter) من نوع BluetoothAdapter القابل للفراغ ويسند لها bluetoothManager.adapter. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:41]

```
42:     private val bleAdvertiser: BluetoothLeAdvertiser? = bluetoothAdapter?.bluetoothLeAdvertiser
```
> يعرّف الخاصية الخاصة المُعلِن منخفض الطاقة (bleAdvertiser) من نوع BluetoothLeAdvertiser القابل للفراغ ويسند لها bluetoothAdapter?.bluetoothLeAdvertiser. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:42]

```
43:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:43]

```
44:     // GATT server for peripheral mode
```
> تعليق: خادم GATT لوضع الطرفية. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:44]

```
45:     private var gattServer: BluetoothGattServer? = null
```
> يعرّف المتغير الخاص خادم GATT (gattServer) من نوع BluetoothGattServer القابل للفراغ ويهيّئه بالقيمة null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:45]

```
46:     private var characteristic: BluetoothGattCharacteristic? = null
```
> يعرّف المتغير الخاص الخاصية الوصفية (characteristic) من نوع BluetoothGattCharacteristic القابل للفراغ ويهيّئه بالقيمة null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:46]

```
47:     private var advertiseCallback: AdvertiseCallback? = null
```
> يعرّف المتغير الخاص رد نداء الإعلان (advertiseCallback) من نوع AdvertiseCallback القابل للفراغ ويهيّئه بالقيمة null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:47]

```
48:     private var advertiseRetryCount = 0
```
> يعرّف المتغير الخاص عدّاد إعادة محاولة الإعلان (advertiseRetryCount) ويهيّئه بالقيمة 0. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:48]

```
49:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:49]

```
50:     // State management
```
> تعليق: إدارة الحالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:50]

```
51:     private var isActive = false
```
> يعرّف المتغير الخاص هل هو نشط (isActive) ويهيّئه بالقيمة false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:51]

```
52: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:52]

```
53:     private fun isBleTransportEnabled(): Boolean {
```
> يعرّف الدالة الخاصة هل نقل BLE مُفعَّل (isBleTransportEnabled) التي تعيد قيمة منطقية ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:53]

```
54:         return try {
```
> يبدأ عبارة الإرجاع بكتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:54]

```
55:             com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().bleEnabled.value
```
> يستدعي DebugSettingsManager.getInstance().bleEnabled.value ويعيد قيمته كنتيجة كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:55]

```
56:         } catch (_: Exception) {
```
> يلتقط أي استثناء (Exception) بمتغيّر مُهمل ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:56]

```
57:             try { com.bitchat.android.ui.debug.DebugPreferenceManager.getBleEnabled(true) } catch (_: Exception) { true }
```
> داخل كتلة المعالجة يحاول إعادة DebugPreferenceManager.getBleEnabled(true)، وإن وقع استثناء يعيد true. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:57]

```
58:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:58]

```
59:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:59]

```
60: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:60]

```
61:     private fun isServerRoleEnabled(): Boolean {
```
> يعرّف الدالة الخاصة هل دور الخادم مُفعَّل (isServerRoleEnabled) التي تعيد قيمة منطقية ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:61]

```
62:         return isBleTransportEnabled() &&
```
> يبدأ عبارة الإرجاع بنتيجة isBleTransportEnabled() مع عامل «و» المنطقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:62]

```
63:             (try { com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().gattServerEnabled.value } catch (_: Exception) { true })
```
> يكمّل الشرط بمحاولة قراءة DebugSettingsManager.getInstance().gattServerEnabled.value، وإن وقع استثناء يستخدم القيمة true. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:63]

```
64:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:65]

```
66:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:66]

```
67:      * Disconnect a specific device (used by ConnectionManager to enforce overall limits)
```
> تعليق: قطع اتصال جهاز محدد (يستعمله ConnectionManager لفرض الحدود الإجمالية). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:67]

```
68:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:68]

```
69:     fun disconnectDevice(device: BluetoothDevice) {
```
> يعرّف الدالة العامة قطع اتصال الجهاز (disconnectDevice) التي تأخذ معاملاً جهاز (device) من نوع BluetoothDevice ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:69]

```
70:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:70]

```
71:             gattServer?.cancelConnection(device)
```
> يستدعي gattServer?.cancelConnection بالوسيط device إن لم يكن gattServer فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:71]

```
72:         } catch (e: Exception) {
```
> يلتقط أي استثناء (Exception) في المتغير e ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:72]

```
73:             Log.w(TAG, "Error disconnecting device ${device.address}: ${e.message}")
```
> يسجّل تحذيراً بالوسم TAG ونصّ "Error disconnecting device" مع عنوان الجهاز ورسالة الاستثناء. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:73]

```
74:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:74]

```
75:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:75]

```
76:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:76]

```
77:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:77]

```
78:      * Start GATT server
```
> تعليق: بدء خادم GATT. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:78]

```
79:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:79]

```
80:     fun start(): Boolean {
```
> يعرّف الدالة العامة البدء (start) التي تعيد قيمة منطقية ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:80]

```
81:         // Respect debug setting
```
> تعليق: احترام إعداد التنقيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:81]

```
82:         if (!isServerRoleEnabled()) {
```
> يتحقق إن كانت دالة isServerRoleEnabled() تعيد false ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:82]

```
83:             Log.i(TAG, "Server start skipped: BLE/GATT Server disabled in debug settings")
```
> يسجّل معلومة بالوسم TAG ونصّ "Server start skipped: BLE/GATT Server disabled in debug settings". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:83]

```
84:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:84]

```
85:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:85]

```
86: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:86]

```
87:         if (isActive) {
```
> يتحقق إن كانت isActive صحيحة ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:87]

```
88:             Log.d(TAG, "GATT server already active; start is a no-op")
```
> يسجّل رسالة تصحيح بالوسم TAG ونصّ "GATT server already active; start is a no-op". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:88]

```
89:             return true
```
> يعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:89]

```
90:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:90]

```
91:         if (!permissionManager.hasBluetoothPermissions()) {
```
> يتحقق إن كانت permissionManager.hasBluetoothPermissions() تعيد false ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:91]

```
92:             Log.e(TAG, "Missing Bluetooth permissions")
```
> يسجّل خطأً بالوسم TAG ونصّ "Missing Bluetooth permissions". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:92]

```
93:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:93]

```
94:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:94]

```
95:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:95]

```
96:         if (bluetoothAdapter?.isEnabled != true) {
```
> يتحقق إن كانت bluetoothAdapter?.isEnabled لا تساوي true ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:96]

```
97:             Log.e(TAG, "Bluetooth is not enabled")
```
> يسجّل خطأً بالوسم TAG ونصّ "Bluetooth is not enabled". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:97]

```
98:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:98]

```
99:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:99]

```
100:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:100]

```
101:         if (bleAdvertiser == null) {
```
> يتحقق إن كانت bleAdvertiser تساوي null ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:101]

```
102:             Log.e(TAG, "BLE advertiser not available")
```
> يسجّل خطأً بالوسم TAG ونصّ "BLE advertiser not available". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:102]

```
103:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:103]

```
104:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:104]

```
105:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:105]

```
106:         isActive = true
```
> يسند للمتغير isActive القيمة true. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:106]

```
107:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:107]

```
108:         connectionScope.launch {
```
> يطلق كوروتيناً على نطاق connectionScope عبر launch ويفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:108]

```
109:             setupGattServer()
```
> يستدعي الدالة setupGattServer(). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:109]

```
110:             delay(300) // Brief delay to ensure GATT server is ready
```
> ينتظر 300 ملي ثانية عبر delay، مع تعليق: تأخير قصير لضمان جاهزية خادم GATT. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:110]

```
111:             startAdvertising()
```
> يستدعي الدالة startAdvertising(). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:111]

```
112:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:112]

```
113:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:113]

```
114:         return true
```
> يعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:114]

```
115:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:115]

```
116:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:116]

```
117:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:117]

```
118:      * Stop GATT server
```
> تعليق: إيقاف خادم GATT. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:118]

```
119:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:119]

```
120:     fun stop() {
```
> يعرّف الدالة العامة الإيقاف (stop) بلا معاملات ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:120]

```
121:         if (!isActive) {
```
> يتحقق إن كانت isActive غير صحيحة ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:121]

```
122:             // Idempotent stop
```
> تعليق: إيقاف غير متأثر بالتكرار (idempotent). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:122]

```
123:             stopAdvertising()
```
> يستدعي الدالة stopAdvertising(). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:123]

```
124:             // Ensure server is closed if present
```
> تعليق: ضمان إغلاق الخادم إن كان موجوداً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:124]

```
125:             gattServer?.close()
```
> يستدعي gattServer?.close() إن لم يكن gattServer فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:125]

```
126:             gattServer = null
```
> يسند للمتغير gattServer القيمة null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:126]

```
127:             Log.i(TAG, "GATT server stopped (already inactive)")
```
> يسجّل معلومة بالوسم TAG ونصّ "GATT server stopped (already inactive)". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:127]

```
128:             return
```
> يخرج من الدالة عبر return. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:128]

```
129:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:129]

```
130: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:130]

```
131:         isActive = false
```
> يسند للمتغير isActive القيمة false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:131]

```
132: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:132]

```
133:         connectionScope.launch {
```
> يطلق كوروتيناً على نطاق connectionScope عبر launch ويفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:133]

```
134:             stopAdvertising()
```
> يستدعي الدالة stopAdvertising(). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:134]

```
135:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:135]

```
136:             // Try to cancel any active connections explicitly before closing
```
> تعليق: محاولة إلغاء أي اتصالات نشطة صراحةً قبل الإغلاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:136]

```
137:             try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:137]

```
138:                 // Disconnect ALL server connections
```
> تعليق: قطع كل اتصالات الخادم. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:138]

```
139:                 val servers = connectionTracker.getConnectedDevices().values.filter { !it.isClient }
```
> يعرّف المتغير الخوادم (servers) ويسند له قيم الأجهزة المتصلة من connectionTracker بعد ترشيح ما ليس عميلاً (isClient غير صحيح). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:139]

```
140:                 servers.forEach { d ->
```
> يكرّر على كل عنصر d في servers عبر forEach ويفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:140]

```
141:                     try { gattServer?.cancelConnection(d.device) } catch (_: Exception) { }
```
> يحاول استدعاء gattServer?.cancelConnection(d.device)، وإن وقع استثناء يتجاهله بكتلة فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:141]

```
142:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:142]

```
143:             } catch (_: Exception) { }
```
> يلتقط أي استثناء بمتغيّر مُهمل ويتجاهله بكتلة فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:143]

```
144:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:144]

```
145:             // Close GATT server
```
> تعليق: إغلاق خادم GATT. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:145]

```
146:             gattServer?.close()
```
> يستدعي gattServer?.close() إن لم يكن gattServer فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:146]

```
147:             gattServer = null
```
> يسند للمتغير gattServer القيمة null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:147]

```
148:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:148]

```
149:             Log.i(TAG, "GATT server stopped")
```
> يسجّل معلومة بالوسم TAG ونصّ "GATT server stopped". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:149]

```
150:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:150]

```
151:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:151]

```
152:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:152]

```
153:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:153]

```
154:      * Get GATT server instance
```
> تعليق: الحصول على نسخة خادم GATT. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:154]

```
155:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:155]

```
156:     fun getGattServer(): BluetoothGattServer? = gattServer
```
> يعرّف الدالة العامة getGattServer التي تعيد BluetoothGattServer القابل للفراغ وتسند نتيجتها مباشرة إلى gattServer. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:156]

```
157:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:157]

```
158:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:158]

```
159:      * Get characteristic instance
```
> تعليق: الحصول على نسخة الخاصية الوصفية. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:159]

```
160:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:160]

```
161:     fun getCharacteristic(): BluetoothGattCharacteristic? = characteristic
```
> يعرّف الدالة العامة getCharacteristic التي تعيد BluetoothGattCharacteristic القابل للفراغ وتسند نتيجتها مباشرة إلى characteristic. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:161]

```
162:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:162]

```
163:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:163]

```
164:      * Setup GATT server with proper sequencing
```
> تعليق: إعداد خادم GATT بترتيب سليم. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:164]

```
165:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:165]

```
166:     @Suppress("DEPRECATION")
```
> يضيف التعليق التوضيحي Suppress بالوسيط "DEPRECATION" لكتم تحذيرات الإهمال. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:166]

```
167:     private fun setupGattServer() {
```
> يعرّف الدالة الخاصة إعداد خادم GATT (setupGattServer) بلا معاملات ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:167]

```
168:         if (!permissionManager.hasBluetoothPermissions()) return
```
> يخرج من الدالة عبر return إن كانت permissionManager.hasBluetoothPermissions() تعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:168]

```
169:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:169]

```
170:         val serverCallback = object : BluetoothGattServerCallback() {
```
> يعرّف المتغير رد نداء الخادم (serverCallback) ككائن مجهول يرث BluetoothGattServerCallback ويفتح جسمه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:170]

```
171:             override fun onConnectionStateChange(device: BluetoothDevice, status: Int, newState: Int) {
```
> يعيد تعريف الدالة عند تغيّر حالة الاتصال (onConnectionStateChange) بمعاملات جهاز (device) وحالة (status) وحالة جديدة (newState) ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:171]

```
172:                 // Guard against callbacks after service shutdown
```
> تعليق: الحماية من ردود النداء بعد إيقاف الخدمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:172]

```
173:                 if (!isActive) {
```
> يتحقق إن كانت isActive غير صحيحة ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:173]

```
174:                     Log.d(TAG, "Server: Ignoring connection state change after shutdown")
```
> يسجّل رسالة تصحيح بالوسم TAG ونصّ "Server: Ignoring connection state change after shutdown". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:174]

```
175:                     return
```
> يخرج من الدالة عبر return. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:175]

```
176:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:176]

```
177:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:177]

```
178:                 when (newState) {
```
> يبدأ تعبير when على القيمة newState ويفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:178]

```
179:                     BluetoothProfile.STATE_CONNECTED -> {
```
> يطابق الحالة BluetoothProfile.STATE_CONNECTED ويفتح فرعها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:179]

```
180:                         Log.i(TAG, "Server: Device connected ${device.address}")
```
> يسجّل معلومة بالوسم TAG ونصّ "Server: Device connected" مع عنوان الجهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:180]

```
181:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:181]

```
182:                         // Get best available RSSI (scan RSSI for server connections)
```
> تعليق: الحصول على أفضل قوة إشارة متاحة (RSSI من المسح لاتصالات الخادم). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:182]

```
183:                         val rssi = connectionTracker.getBestRSSI(device.address) ?: Int.MIN_VALUE
```
> يعرّف المتغير قوة الإشارة (rssi) ويسند له connectionTracker.getBestRSSI لعنوان الجهاز، أو Int.MIN_VALUE إن كانت النتيجة null. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:183]

```
184:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:184]

```
185:                         val deviceConn = BluetoothConnectionTracker.DeviceConnection(
```
> يعرّف المتغير اتصال الجهاز (deviceConn) ويبدأ إنشاء كائن BluetoothConnectionTracker.DeviceConnection. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:185]

```
186:                             device = device,
```
> يمرّر المعامل device بالقيمة device. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:186]

```
187:                             rssi = rssi,
```
> يمرّر المعامل rssi بالقيمة rssi. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:187]

```
188:                             isClient = false
```
> يمرّر المعامل isClient بالقيمة false. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:188]

```
189:                         )
```
> يغلق قائمة وسائط إنشاء الكائن DeviceConnection. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:189]

```
190:                         connectionTracker.addDeviceConnection(device.address, deviceConn)
```
> يستدعي connectionTracker.addDeviceConnection بعنوان الجهاز والكائن deviceConn. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:190]

```
191: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:191]

```
192:                         connectionScope.launch {
```
> يطلق كوروتيناً على نطاق connectionScope عبر launch ويفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:192]

```
193:                             delay(1000)
```
> ينتظر 1000 ملي ثانية عبر delay. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:193]

```
194:                             if (isActive) { // Check if still active
```
> يتحقق إن كانت isActive صحيحة ويفتح كتلة الشرط، مع تعليق: التحقق إن كان لا يزال نشطاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:194]

```
195:                                 delegate?.onDeviceConnected(device)
```
> يستدعي delegate?.onDeviceConnected بالوسيط device إن لم يكن delegate فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:195]

```
196:                             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:196]

```
197:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:197]

```
198:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:198]

```
199:                     BluetoothProfile.STATE_DISCONNECTED -> {
```
> يطابق الحالة BluetoothProfile.STATE_DISCONNECTED ويفتح فرعها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:199]

```
200:                         Log.i(TAG, "Server: Device disconnected ${device.address}")
```
> يسجّل معلومة بالوسم TAG ونصّ "Server: Device disconnected" مع عنوان الجهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:200]
