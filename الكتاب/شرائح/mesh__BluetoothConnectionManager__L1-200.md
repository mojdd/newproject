# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يُعلِن أنّ هذا الملف ينتمي إلى الحزمة (package) المسماة com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:2]

```
3: import android.bluetooth.*
```
> يستورد (import) كل الأصناف من حزمة android.bluetooth. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:3]

```
4: import android.content.Context
```
> يستورد الصنف Context من حزمة android.content. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:4]

```
5: import android.util.Log
```
> يستورد الصنف Log من حزمة android.util. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:5]

```
6: import com.bitchat.android.model.RoutedPacket
```
> يستورد الصنف RoutedPacket (الرزمة المُوجَّهة) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:6]

```
7: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف BitchatPacket (رزمة بِت‑شات) من حزمة com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:7]

```
8: import kotlinx.coroutines.*
```
> يستورد كل الأصناف من حزمة kotlinx.coroutines (الكوروتينات). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:8]

```
9: import kotlinx.coroutines.flow.collect
```
> يستورد الدالة collect من حزمة kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:9]

```
10: import kotlinx.coroutines.flow.combine
```
> يستورد الدالة combine من حزمة kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:11]

```
12: /**
```
> تعليق: بداية تعليق توثيق (KDoc) متعدد الأسطر. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:12]

```
13:  * Power-optimized Bluetooth connection manager with comprehensive memory management
```
> تعليق: مدير اتصال بلوتوث مُحسَّن للطاقة مع إدارة ذاكرة شاملة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:13]

```
14:  * Integrates with PowerManager for adaptive power consumption
```
> تعليق: يتكامل مع PowerManager (مدير الطاقة) لاستهلاك طاقة متكيّف. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:14]

```
15:  * Coordinates smaller, focused components for better maintainability
```
> تعليق: ينسّق مكوّنات أصغر ومركّزة لتحسين قابلية الصيانة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:15]

```
16:  */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:16]

```
17: class BluetoothConnectionManager(
```
> يُعرِّف الصنف (class) المسمى BluetoothConnectionManager (مدير اتصال البلوتوث) ويبدأ قائمة معاملات الباني (constructor). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:17]

```
18:     private val context: Context, 
```
> يُعرِّف معاملاً خاصاً ثابتاً اسمه context من نوع Context. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:18]

```
19:     private val myPeerID: String,
```
> يُعرِّف معاملاً خاصاً ثابتاً اسمه myPeerID (معرّف ندّي الخاص) من نوع String. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:19]

```
20:     private val fragmentManager: FragmentManager? = null
```
> يُعرِّف معاملاً خاصاً ثابتاً اسمه fragmentManager (مدير التجزئة) من نوع FragmentManager القابل لأن يكون فارغاً، بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:20]

```
21: ) : PowerManagerDelegate {
```
> يُنهي قائمة معاملات الباني، ويُعلِن أنّ الصنف يُحقّق الواجهة PowerManagerDelegate (مفوَّض مدير الطاقة)، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:21]

```
22:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:22]

```
23:     companion object {
```
> يفتح كائناً مرافقاً (companion object) للصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:23]

```
24:         private const val TAG = "BluetoothConnectionManager"
```
> يُعرِّف ثابتاً خاصاً اسمه TAG (وسم) بالقيمة النصية "BluetoothConnectionManager". [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:24]

```
25:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:25]

```
26:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:26]

```
27:     // Core Bluetooth components
```
> تعليق: مكوّنات البلوتوث الأساسية. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:27]

```
28:     private val bluetoothManager: BluetoothManager = 
```
> يُعرِّف حقلاً خاصاً ثابتاً اسمه bluetoothManager (مدير البلوتوث) من نوع BluetoothManager، ويبدأ تعيين قيمته. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:28]

```
29:         context.getSystemService(Context.BLUETOOTH_SERVICE) as BluetoothManager
```
> يستدعي context.getSystemService بالوسيط Context.BLUETOOTH_SERVICE، ويحوّل الناتج بالنوع (as) إلى BluetoothManager ليكون قيمة الحقل bluetoothManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:29]

```
30:     private val bluetoothAdapter: BluetoothAdapter? = bluetoothManager.adapter
```
> يُعرِّف حقلاً خاصاً ثابتاً اسمه bluetoothAdapter (محوّل البلوتوث) من نوع BluetoothAdapter القابل لأن يكون فارغاً، بقيمة bluetoothManager.adapter. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:30]

```
31:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:31]

```
32:     // Power management
```
> تعليق: إدارة الطاقة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:32]

```
33:     private val powerManager = PowerManager(context.applicationContext)
```
> يُعرِّف حقلاً خاصاً ثابتاً اسمه powerManager (مدير الطاقة) بقيمة كائن PowerManager جديد منشأ بالوسيط context.applicationContext. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:33]

```
34:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:34]

```
35:     // Coroutines
```
> تعليق: الكوروتينات. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:35]

```
36:     private val connectionScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يُعرِّف حقلاً خاصاً ثابتاً اسمه connectionScope (نطاق الاتصال) بقيمة كائن CoroutineScope منشأ بدمج Dispatchers.IO مع SupervisorJob(). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:36]

```
37:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:37]

```
38:     // Component managers
```
> تعليق: مديرو المكوّنات. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:38]

```
39:     private val permissionManager = BluetoothPermissionManager(context)
```
> يُعرِّف حقلاً خاصاً ثابتاً اسمه permissionManager (مدير الأذونات) بقيمة كائن BluetoothPermissionManager جديد منشأ بالوسيط context. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:39]

```
40:     private val connectionTracker = BluetoothConnectionTracker(connectionScope, powerManager)
```
> يُعرِّف حقلاً خاصاً ثابتاً اسمه connectionTracker (متتبّع الاتصال) بقيمة كائن BluetoothConnectionTracker جديد منشأ بالوسيطين connectionScope وpowerManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:40]

```
41:     private val packetBroadcaster = BluetoothPacketBroadcaster(connectionScope, connectionTracker, fragmentManager, myPeerID)
```
> يُعرِّف حقلاً خاصاً ثابتاً اسمه packetBroadcaster (مذيع الرزم) بقيمة كائن BluetoothPacketBroadcaster جديد منشأ بالوسائط connectionScope وconnectionTracker وfragmentManager وmyPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:41]

```
42:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:42]

```
43:     // Delegate for component managers to call back to main manager
```
> تعليق: مفوَّض لمديري المكوّنات لاستدعاء المدير الرئيسي عكسياً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:43]

```
44:     private val componentDelegate = object : BluetoothConnectionManagerDelegate {
```
> يُعرِّف حقلاً خاصاً ثابتاً اسمه componentDelegate (مفوَّض المكوّن) بقيمة كائن مجهول (object) يُحقّق الواجهة BluetoothConnectionManagerDelegate. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:44]

```
45:         override fun onPacketReceived(packet: BitchatPacket, peerID: String, device: BluetoothDevice?) {
```
> يَتجاوز (override) الدالة onPacketReceived (عند استلام رزمة) بالمعاملات packet من نوع BitchatPacket وpeerID من نوع String وdevice من نوع BluetoothDevice القابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:45]

```
46:             Log.d(TAG, "onPacketReceived: Packet received from ${device?.address} ($peerID)")
```
> يستدعي Log.d بالوسم TAG ونصّ تسجيل يصف استلام رزمة من device?.address ومن peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:46]

```
47:             device?.let { bluetoothDevice ->
```
> يستدعي let على device إن لم يكن فارغاً، مُسمّياً المتغير الداخلي bluetoothDevice. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:47]

```
48:                 // Get current RSSI for this device and update if available
```
> تعليق: احصل على RSSI (قوة الإشارة) الحالية لهذا الجهاز وحدّثها إن توفّرت. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:48]

```
49:                 val currentRSSI = connectionTracker.getBestRSSI(bluetoothDevice.address)
```
> يُعرِّف متغيراً ثابتاً اسمه currentRSSI بقيمة ناتج connectionTracker.getBestRSSI بالوسيط bluetoothDevice.address. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:49]

```
50:                 if (currentRSSI != null) {
```
> يفحص إن كانت currentRSSI ليست null. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:50]

```
51:                     delegate?.onRSSIUpdated(bluetoothDevice.address, currentRSSI)
```
> يستدعي delegate?.onRSSIUpdated (عند تحديث RSSI) بالوسيطين bluetoothDevice.address وcurrentRSSI إن لم يكن delegate فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:51]

```
52:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:52]

```
53:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:53]

```
54: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:54]

```
55:             if (peerID == myPeerID) return // Ignore messages from self
```
> يَرجع (return) من الدالة إن كان peerID مساوياً myPeerID؛ تعليق: تجاهل الرسائل من الذات. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:55]

```
56: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:56]

```
57:             delegate?.onPacketReceived(packet, peerID, device)
```
> يستدعي delegate?.onPacketReceived بالوسائط packet وpeerID وdevice إن لم يكن delegate فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:57]

```
58:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:58]

```
59:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:59]

```
60:         override fun onDeviceConnected(device: BluetoothDevice) {
```
> يَتجاوز الدالة onDeviceConnected (عند اتصال جهاز) بالمعامل device من نوع BluetoothDevice. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:60]

```
61:             // Trigger limit enforcement immediately upon any new connection
```
> تعليق: شغّل فرض الحدود فوراً عند أي اتصال جديد. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:61]

```
62:             enforceStrictLimits()
```
> يستدعي الدالة enforceStrictLimits (فرض الحدود الصارمة). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:62]

```
63:             delegate?.onDeviceConnected(device)
```
> يستدعي delegate?.onDeviceConnected بالوسيط device إن لم يكن delegate فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:63]

```
64:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:65]

```
66:         override fun onDeviceDisconnected(device: BluetoothDevice) {
```
> يَتجاوز الدالة onDeviceDisconnected (عند قطع اتصال جهاز) بالمعامل device من نوع BluetoothDevice. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:66]

```
67:             delegate?.onDeviceDisconnected(device)
```
> يستدعي delegate?.onDeviceDisconnected بالوسيط device إن لم يكن delegate فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:67]

```
68:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:68]

```
69:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:69]

```
70:         override fun onRSSIUpdated(deviceAddress: String, rssi: Int) {
```
> يَتجاوز الدالة onRSSIUpdated بالمعاملين deviceAddress (عنوان الجهاز) من نوع String وrssi من نوع Int. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:70]

```
71:             delegate?.onRSSIUpdated(deviceAddress, rssi)
```
> يستدعي delegate?.onRSSIUpdated بالوسيطين deviceAddress وrssi إن لم يكن delegate فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:71]

```
72:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:72]

```
73:     }
```
> إغلاق نطاق (نهاية الكائن المجهول componentDelegate). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:73]

```
74:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:74]

```
75:     private val serverManager = BluetoothGattServerManager(
```
> يُعرِّف حقلاً خاصاً ثابتاً اسمه serverManager (مدير الخادم) بقيمة كائن BluetoothGattServerManager جديد، ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:75]

```
76:         context, connectionScope, connectionTracker, permissionManager, powerManager, componentDelegate, myPeerID
```
> يمرّر الوسائط context وconnectionScope وconnectionTracker وpermissionManager وpowerManager وcomponentDelegate وmyPeerID إلى باني serverManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:76]

```
77:     )
```
> يُغلق قائمة وسائط باني serverManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:77]

```
78:     private val clientManager = BluetoothGattClientManager(
```
> يُعرِّف حقلاً خاصاً ثابتاً اسمه clientManager (مدير العميل) بقيمة كائن BluetoothGattClientManager جديد، ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:78]

```
79:         context, connectionScope, connectionTracker, permissionManager, powerManager, componentDelegate
```
> يمرّر الوسائط context وconnectionScope وconnectionTracker وpermissionManager وpowerManager وcomponentDelegate إلى باني clientManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:79]

```
80:     )
```
> يُغلق قائمة وسائط باني clientManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:80]

```
81:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:81]

```
82:     // Service state
```
> تعليق: حالة الخدمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:82]

```
83:     private var isActive = false
```
> يُعرِّف متغيراً خاصاً قابلاً للتغيير اسمه isActive (نشط) بالقيمة الابتدائية false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:83]

```
84:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:84]

```
85:     // Delegate for callbacks
```
> تعليق: مفوَّض للنداءات العكسية. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:85]

```
86:     var delegate: BluetoothConnectionManagerDelegate? = null
```
> يُعرِّف متغيراً عاماً قابلاً للتغيير اسمه delegate (مفوَّض) من نوع BluetoothConnectionManagerDelegate القابل لأن يكون فارغاً، بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:86]

```
87:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:87]

```
88:     // Public property for address-peer mapping
```
> تعليق: خاصية عامة لتعيين العنوان إلى الندّ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:88]

```
89:     val addressPeerMap get() = connectionTracker.addressPeerMap
```
> يُعرِّف خاصية ثابتة اسمها addressPeerMap (خريطة العنوان‑الندّ) بمُسترجِع (getter) يُعيد connectionTracker.addressPeerMap. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:89]

```
90:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:90]

```
91:     private fun isBleTransportEnabled(): Boolean {
```
> يُعرِّف دالة خاصة اسمها isBleTransportEnabled (هل نقل BLE مُفعَّل) تُعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:91]

```
92:         return try {
```
> يَرجع نتيجة كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:92]

```
93:             com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().bleEnabled.value
```
> يستدعي DebugSettingsManager.getInstance() ثم يقرأ bleEnabled.value ليكون قيمة الإرجاع. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:93]

```
94:         } catch (_: Exception) {
```
> يلتقط أي استثناء (Exception) دون تسميته، ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:94]

```
95:             try { com.bitchat.android.ui.debug.DebugPreferenceManager.getBleEnabled(true) } catch (_: Exception) { true }
```
> يحاول إرجاع DebugPreferenceManager.getBleEnabled(true)؛ وعند أي استثناء يُعيد true. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:95]

```
96:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:96]

```
97:     }
```
> إغلاق نطاق (نهاية الدالة isBleTransportEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:97]

```
98:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:98]

```
99:     private fun isGattServerEnabled(): Boolean {
```
> يُعرِّف دالة خاصة اسمها isGattServerEnabled (هل خادم GATT مُفعَّل) تُعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:99]

```
100:         return isBleTransportEnabled() &&
```
> يَرجع نتيجة عملية «و» المنطقية (&&) بين isBleTransportEnabled() والشرط التالي. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:100]

```
101:             (try { com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().gattServerEnabled.value } catch (_: Exception) { true })
```
> يحاول قراءة gattServerEnabled.value من DebugSettingsManager.getInstance()؛ وعند أي استثناء يُعطي true، كطرف ثانٍ للعملية المنطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:101]

```
102:     }
```
> إغلاق نطاق (نهاية الدالة isGattServerEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:102]

```
103:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:103]

```
104:     private fun isGattClientEnabled(): Boolean {
```
> يُعرِّف دالة خاصة اسمها isGattClientEnabled (هل عميل GATT مُفعَّل) تُعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:104]

```
105:         return isBleTransportEnabled() &&
```
> يَرجع نتيجة عملية «و» المنطقية (&&) بين isBleTransportEnabled() والشرط التالي. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:105]

```
106:             (try { com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().gattClientEnabled.value } catch (_: Exception) { true })
```
> يحاول قراءة gattClientEnabled.value من DebugSettingsManager.getInstance()؛ وعند أي استثناء يُعطي true، كطرف ثانٍ للعملية المنطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:106]

```
107:     }
```
> إغلاق نطاق (نهاية الدالة isGattClientEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:107]

```
108:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:108]

```
109:     init {
```
> يفتح كتلة التهيئة (init) للصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:109]

```
110:         powerManager.delegate = this
```
> يُسنِد this (هذا الكائن) إلى الخاصية delegate في powerManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:110]

```
111:         // Observe debug settings to enforce role state while active
```
> تعليق: راقب إعدادات التصحيح لفرض حالة الدور أثناء النشاط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:111]

```
112:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:112]

```
113:             val dbg = com.bitchat.android.ui.debug.DebugSettingsManager.getInstance()
```
> يُعرِّف متغيراً ثابتاً اسمه dbg بقيمة DebugSettingsManager.getInstance(). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:113]

```
114:             // Master transport enable/disable
```
> تعليق: تفعيل/تعطيل النقل الرئيسي. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:114]

```
115:             connectionScope.launch {
```
> يُطلق كوروتيناً (launch) في النطاق connectionScope. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:115]

```
116:                 dbg.bleEnabled.collect { enabled ->
```
> يَجمع (collect) قيم التدفق dbg.bleEnabled، مُسمّياً كل قيمة enabled. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:116]

```
117:                     if (enabled) return@collect
```
> يَرجع من كتلة collect إن كانت enabled صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:117]

```
118:                     if (isActive) {
```
> يفحص إن كان isActive صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:118]

```
119:                         disableTransport()
```
> يستدعي الدالة disableTransport (تعطيل النقل). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:119]

```
120:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:120]

```
121:                 }
```
> إغلاق نطاق (نهاية كتلة collect). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:121]

```
122:             }
```
> إغلاق نطاق (نهاية كتلة launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:122]

```
123:             // Role enable/disable
```
> تعليق: تفعيل/تعطيل الدور. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:123]

```
124:             connectionScope.launch {
```
> يُطلق كوروتيناً في النطاق connectionScope. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:124]

```
125:                 dbg.gattServerEnabled.collect { enabled ->
```
> يَجمع قيم التدفق dbg.gattServerEnabled، مُسمّياً كل قيمة enabled. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:125]

```
126:                     if (!isActive) return@collect
```
> يَرجع من كتلة collect إن لم يكن isActive صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:126]

```
127:                     if (enabled && isBleTransportEnabled()) startServer() else stopServer()
```
> إن كانت enabled صحيحة وكان isBleTransportEnabled() صحيحاً يستدعي startServer()، وإلا يستدعي stopServer(). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:127]

```
128:                 }
```
> إغلاق نطاق (نهاية كتلة collect). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:128]

```
129:             }
```
> إغلاق نطاق (نهاية كتلة launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:129]

```
130:             connectionScope.launch {
```
> يُطلق كوروتيناً في النطاق connectionScope. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:130]

```
131:                 dbg.gattClientEnabled.collect { enabled ->
```
> يَجمع قيم التدفق dbg.gattClientEnabled، مُسمّياً كل قيمة enabled. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:131]

```
132:                     if (!isActive) return@collect
```
> يَرجع من كتلة collect إن لم يكن isActive صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:132]

```
133:                     if (enabled && isBleTransportEnabled()) startClient() else stopClient()
```
> إن كانت enabled صحيحة وكان isBleTransportEnabled() صحيحاً يستدعي startClient()، وإلا يستدعي stopClient(). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:133]

```
134:                 }
```
> إغلاق نطاق (نهاية كتلة collect). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:134]

```
135:             }
```
> إغلاق نطاق (نهاية كتلة launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:135]

```
136:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:136]

```
137:             // Centralized limit enforcement on any setting change
```
> تعليق: فرض الحدود المركزي عند أي تغيير إعداد. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:137]

```
138:             connectionScope.launch {
```
> يُطلق كوروتيناً في النطاق connectionScope. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:138]

```
139:                 combine(
```
> يستدعي الدالة combine (دمج التدفقات)، ويبدأ قائمة وسائطها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:139]

```
140:                     dbg.maxConnectionsOverall,
```
> يمرّر التدفق dbg.maxConnectionsOverall (الحد الأقصى للاتصالات الإجمالي) كوسيط أول إلى combine. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:140]

```
141:                     dbg.maxServerConnections,
```
> يمرّر التدفق dbg.maxServerConnections (الحد الأقصى لاتصالات الخادم) كوسيط ثانٍ إلى combine. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:141]

```
142:                     dbg.maxClientConnections
```
> يمرّر التدفق dbg.maxClientConnections (الحد الأقصى لاتصالات العميل) كوسيط ثالث إلى combine. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:142]

```
143:                 ) { _, _, _ -> 
```
> يُغلق قائمة وسائط combine، ويبدأ دالة الدمج بثلاثة معاملات مُهملة (_). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:143]

```
144:                     // We don't need the values here, we just need to trigger enforcement
```
> تعليق: لا نحتاج القيم هنا، نحتاج فقط لتشغيل الفرض. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:144]

```
145:                     Unit 
```
> يُنتج القيمة Unit كنتيجة دالة الدمج. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:145]

```
146:                 }.collect {
```
> يُغلق دالة الدمج ويستدعي عليها collect، ويبدأ كتلة الجمع. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:146]

```
147:                     if (isActive) {
```
> يفحص إن كان isActive صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:147]

```
148:                         enforceStrictLimits()
```
> يستدعي الدالة enforceStrictLimits. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:148]

```
149:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:149]

```
150:                 }
```
> إغلاق نطاق (نهاية كتلة collect). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:150]

```
151:             }
```
> إغلاق نطاق (نهاية كتلة launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:151]

```
152:         } catch (_: Exception) { }
```
> يلتقط أي استثناء دون تسميته ويتجاهله بكتلة فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:152]

```
153:     }
```
> إغلاق نطاق (نهاية كتلة init). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:153]

```
154:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:154]

```
155:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:155]

```
156:      * Centralized connection limit enforcement
```
> تعليق: فرض حدّ الاتصال المركزي. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:156]

```
157:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:157]

```
158:     private fun enforceStrictLimits() {
```
> يُعرِّف دالة خاصة اسمها enforceStrictLimits (فرض الحدود الصارمة) بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:158]

```
159:         if (!isActive) return
```
> يَرجع من الدالة إن لم يكن isActive صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:159]

```
160:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:160]

```
161:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:161]

```
162:             val dbg = com.bitchat.android.ui.debug.DebugSettingsManager.getInstance()
```
> يُعرِّف متغيراً ثابتاً اسمه dbg بقيمة DebugSettingsManager.getInstance(). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:162]

```
163:             val maxOverall = dbg.maxConnectionsOverall.value
```
> يُعرِّف متغيراً ثابتاً اسمه maxOverall بقيمة dbg.maxConnectionsOverall.value. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:163]

```
164:             val maxServer = dbg.maxServerConnections.value
```
> يُعرِّف متغيراً ثابتاً اسمه maxServer بقيمة dbg.maxServerConnections.value. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:164]

```
165:             val maxClient = dbg.maxClientConnections.value
```
> يُعرِّف متغيراً ثابتاً اسمه maxClient بقيمة dbg.maxClientConnections.value. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:165]

```
166:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:166]

```
167:             // Get list of connections to evict to satisfy all constraints
```
> تعليق: احصل على قائمة الاتصالات الواجب طردها لتلبية كل القيود. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:167]

```
168:             val toEvict = connectionTracker.getConnectionsToEvict(maxOverall, maxServer, maxClient)
```
> يُعرِّف متغيراً ثابتاً اسمه toEvict (الواجب طرده) بقيمة ناتج connectionTracker.getConnectionsToEvict بالوسائط maxOverall وmaxServer وmaxClient. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:168]

```
169:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:169]

```
170:             if (toEvict.isNotEmpty()) {
```
> يفحص إن كانت toEvict ليست فارغة (isNotEmpty). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:170]

```
171:                 Log.i(TAG, "Enforcing limits (max: $maxOverall, s: $maxServer, c: $maxClient) - evicting ${toEvict.size} connections")
```
> يستدعي Log.i بالوسم TAG ونصّ تسجيل يبيّن القيم maxOverall وmaxServer وmaxClient وعدد toEvict.size اتصالاً يُطرَد. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:171]

```
172:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:172]

```
173:                 toEvict.forEach { conn ->
```
> يكرّر (forEach) على عناصر toEvict، مُسمّياً كل عنصر conn. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:173]

```
174:                     if (conn.isClient) {
```
> يفحص إن كانت conn.isClient (هل العنصر عميل) صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:174]

```
175:                         Log.d(TAG, "Evicting client ${conn.device.address}")
```
> يستدعي Log.d بالوسم TAG ونصّ يذكر طرد العميل ذي العنوان conn.device.address. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:175]

```
176:                         try { conn.gatt?.disconnect() } catch (_: Exception) { }
```
> يحاول استدعاء conn.gatt?.disconnect() إن لم يكن gatt فارغاً، ويتجاهل أي استثناء. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:176]

```
177:                     } else {
```
> يفتح فرع else (وإلا). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:177]

```
178:                         Log.d(TAG, "Evicting server ${conn.device.address}")
```
> يستدعي Log.d بالوسم TAG ونصّ يذكر طرد الخادم ذي العنوان conn.device.address. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:178]

```
179:                         serverManager.disconnectDevice(conn.device)
```
> يستدعي serverManager.disconnectDevice بالوسيط conn.device. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:179]

```
180:                     }
```
> إغلاق نطاق (نهاية فرع else). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:180]

```
181:                 }
```
> إغلاق نطاق (نهاية كتلة forEach). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:181]

```
182:             }
```
> إغلاق نطاق (نهاية كتلة if). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:182]

```
183:         } catch (e: Exception) {
```
> يلتقط أي استثناء مُسمّياً إياه e، ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:183]

```
184:             Log.e(TAG, "Error enforcing limits: ${e.message}")
```
> يستدعي Log.e بالوسم TAG ونصّ خطأ يتضمّن e.message. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:184]

```
185:         }
```
> إغلاق نطاق (نهاية كتلة catch). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:185]

```
186:     }
```
> إغلاق نطاق (نهاية الدالة enforceStrictLimits). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:186]

```
187:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:187]

```
188:     /**
```
> تعليق: بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:188]

```
189:      * Start all Bluetooth services with power optimization
```
> تعليق: ابدأ كل خدمات البلوتوث مع تحسين الطاقة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:189]

```
190:      */
```
> تعليق: نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:190]

```
191:     fun startServices(): Boolean {
```
> يُعرِّف دالة عامة اسمها startServices (بدء الخدمات) تُعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:191]

```
192:         Log.i(TAG, "Starting power-optimized Bluetooth services...")
```
> يستدعي Log.i بالوسم TAG ونصّ يذكر بدء خدمات البلوتوث المُحسَّنة للطاقة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:192]

```
193:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:193]

```
194:         if (!isBleTransportEnabled()) {
```
> يفحص إن كان isBleTransportEnabled() غير صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:194]

```
195:             Log.i(TAG, "BLE transport disabled by debug settings; not starting Bluetooth services")
```
> يستدعي Log.i بالوسم TAG ونصّ يذكر أنّ نقل BLE معطّل بإعدادات التصحيح وأنّ خدمات البلوتوث لن تبدأ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:195]

```
196:             disableTransport()
```
> يستدعي الدالة disableTransport. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:196]

```
197:             return false
```
> يَرجع القيمة false من الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:197]

```
198:         }
```
> إغلاق نطاق (نهاية كتلة if). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:198]

```
199:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:199]

```
200:         if (!permissionManager.hasBluetoothPermissions()) {
```
> يفحص إن كان permissionManager.hasBluetoothPermissions() (هل يملك أذونات البلوتوث) غير صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:200]
