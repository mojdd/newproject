# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يُعرِّف اسم الحزمة (package) للملف بأنه `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:2]

```
3: import android.bluetooth.BluetoothDevice
```
> يستورد (import) الصنف `BluetoothDevice` من `android.bluetooth`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:3]

```
4: import android.bluetooth.BluetoothGatt
```
> يستورد الصنف `BluetoothGatt` من `android.bluetooth`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:4]

```
5: import android.bluetooth.BluetoothGattCharacteristic
```
> يستورد الصنف `BluetoothGattCharacteristic` من `android.bluetooth`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:5]

```
6: import android.util.Log
```
> يستورد الصنف `Log` من `android.util`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:6]

```
7: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف `CoroutineScope` من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:7]

```
8: import kotlinx.coroutines.delay
```
> يستورد الدالة `delay` من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:8]

```
9: import kotlinx.coroutines.launch
```
> يستورد الدالة `launch` من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:9]

```
10: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف `ConcurrentHashMap` من `java.util.concurrent`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:10]

```
11: import java.util.concurrent.CopyOnWriteArrayList
```
> يستورد الصنف `CopyOnWriteArrayList` من `java.util.concurrent`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:11]

```
12: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:12]

```
13: /**
```
> بداية تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:13]

```
14:  * Tracks all Bluetooth connections and handles cleanup
```
> تعليق: يتتبّع كل اتصالات البلوتوث ويتولّى التنظيف. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:14]

```
15:  */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:15]

```
16: class BluetoothConnectionTracker(
```
> يُعرِّف الصنف `BluetoothConnectionTracker` (متتبّع اتصال البلوتوث) ويفتح قائمة معاملات المُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:16]

```
17:     private val connectionScope: CoroutineScope,
```
> يُعرِّف معامل مُنشئ خاصاً للقراءة فقط `connectionScope` (نطاق الاتصال) من نوع `CoroutineScope`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:17]

```
18:     private val powerManager: PowerManager
```
> يُعرِّف معامل مُنشئ خاصاً للقراءة فقط `powerManager` (مدير الطاقة) من نوع `PowerManager`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:18]

```
19: ) : MeshConnectionTracker(connectionScope, TAG) {
```
> يُغلق قائمة المعاملات ويُعلن أن الصنف يرث من `MeshConnectionTracker` مُمرِّراً `connectionScope` و`TAG` ثم يفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:19]

```
20:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:20]

```
21:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:21]

```
22:         private const val TAG = "BluetoothConnectionTracker"
```
> يُعرِّف ثابتاً خاصاً `TAG` بالقيمة النصية `"BluetoothConnectionTracker"`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:22]

```
23:         private const val CLEANUP_DELAY = com.bitchat.android.util.AppConstants.Mesh.CONNECTION_CLEANUP_DELAY_MS
```
> يُعرِّف ثابتاً خاصاً `CLEANUP_DELAY` (تأخير التنظيف) ويضبط قيمته إلى `AppConstants.Mesh.CONNECTION_CLEANUP_DELAY_MS`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:23]

```
24:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:24]

```
25:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:25]

```
26:     // Connection tracking - reduced memory footprint
```
> تعليق: تتبّع الاتصال — بصمة ذاكرة مُخفَّضة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:26]

```
27:     private val connectedDevices = ConcurrentHashMap<String, DeviceConnection>()
```
> يُعرِّف حقلاً خاصاً للقراءة فقط `connectedDevices` (الأجهزة المتصلة) ويضبطه إلى `ConcurrentHashMap` بمفتاح نصي وقيمة `DeviceConnection`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:27]

```
28:     private val subscribedDevices = CopyOnWriteArrayList<BluetoothDevice>()
```
> يُعرِّف حقلاً خاصاً للقراءة فقط `subscribedDevices` (الأجهزة المشتركة) ويضبطه إلى `CopyOnWriteArrayList` من `BluetoothDevice`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:28]

```
29:     val addressPeerMap = ConcurrentHashMap<String, String>()
```
> يُعرِّف حقلاً عاماً للقراءة فقط `addressPeerMap` (خريطة العنوان إلى النِّد) ويضبطه إلى `ConcurrentHashMap` بمفتاح نصي وقيمة نصية. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:29]

```
30:     // Track whether we have seen the first ANNOUNCE on a given device connection
```
> تعليق: تتبّع ما إذا كنّا قد رأينا أول إعلان (ANNOUNCE) على اتصال جهاز معيّن. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:30]

```
31:     private val firstAnnounceSeen = ConcurrentHashMap<String, Boolean>()
```
> يُعرِّف حقلاً خاصاً للقراءة فقط `firstAnnounceSeen` (رؤية أول إعلان) ويضبطه إلى `ConcurrentHashMap` بمفتاح نصي وقيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:31]

```
32:     // RSSI tracking from scan results (for devices we discover but may connect as servers)
```
> تعليق: تتبّع شدة الإشارة (RSSI) من نتائج المسح (للأجهزة التي نكتشفها لكن قد نتصل بها كخوادم). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:32]

```
33:     private val scanRSSI = ConcurrentHashMap<String, Int>()
```
> يُعرِّف حقلاً خاصاً للقراءة فقط `scanRSSI` (شدة إشارة المسح) ويضبطه إلى `ConcurrentHashMap` بمفتاح نصي وقيمة عددية صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:33]

```
34:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:34]

```
35:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:35]

```
36:      * Consolidated device connection information
```
> تعليق: معلومات اتصال جهاز مُجمَّعة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:36]

```
37:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:37]

```
38:     data class DeviceConnection(
```
> يُعرِّف صنف بيانات (data class) باسم `DeviceConnection` (اتصال الجهاز) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:38]

```
39:         val device: BluetoothDevice,
```
> يُعرِّف خاصية للقراءة فقط `device` (الجهاز) من نوع `BluetoothDevice`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:39]

```
40:         val gatt: BluetoothGatt? = null,
```
> يُعرِّف خاصية للقراءة فقط `gatt` من نوع `BluetoothGatt?` قابلة للعدم بقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:40]

```
41:         val characteristic: BluetoothGattCharacteristic? = null,
```
> يُعرِّف خاصية للقراءة فقط `characteristic` (الخاصية) من نوع `BluetoothGattCharacteristic?` قابلة للعدم بقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:41]

```
42:         val rssi: Int = Int.MIN_VALUE,
```
> يُعرِّف خاصية للقراءة فقط `rssi` (شدة الإشارة) من نوع عددي صحيح بقيمة افتراضية `Int.MIN_VALUE`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:42]

```
43:         val isClient: Boolean = false,
```
> يُعرِّف خاصية للقراءة فقط `isClient` (أهو عميل) من نوع منطقي بقيمة افتراضية `false`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:43]

```
44:         val connectedAt: Long = System.currentTimeMillis(),
```
> يُعرِّف خاصية للقراءة فقط `connectedAt` (وقت الاتصال) من نوع `Long` بقيمة افتراضية `System.currentTimeMillis()`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:44]

```
45:         val peerID: String? = null
```
> يُعرِّف خاصية للقراءة فقط `peerID` (معرّف النِّد) من نوع نصي قابل للعدم بقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:45]

```
46:     )
```
> يُغلق قائمة معاملات صنف البيانات. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:46]

```
47:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:47]

```
48:     override fun start() {
```
> يُعرِّف دالة `start` (بدء) مُتجاوِزة للمُورَّثة ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:48]

```
49:         super.start()
```
> يستدعي دالة `start` في الصنف الأب. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:49]

```
50:     }
```
> إغلاق نطاق دالة `start`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:50]

```
51:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:51]

```
52:     override fun stop() {
```
> يُعرِّف دالة `stop` (إيقاف) مُتجاوِزة للمُورَّثة ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:52]

```
53:         super.stop()
```
> يستدعي دالة `stop` في الصنف الأب. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:53]

```
54:         cleanupAllConnections()
```
> يستدعي دالة `cleanupAllConnections` (تنظيف كل الاتصالات). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:54]

```
55:         clearAllConnections()
```
> يستدعي دالة `clearAllConnections` (مسح كل الاتصالات). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:55]

```
56:     }
```
> إغلاق نطاق دالة `stop`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:56]

```
57: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:57]

```
58:     // Abstract implementations
```
> تعليق: تطبيقات مجرّدة (Abstract implementations). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:58]

```
59:     override fun isConnected(id: String): Boolean = connectedDevices.containsKey(id)
```
> يُعرِّف دالة `isConnected` (أمُتّصل) مُتجاوِزة تأخذ `id` نصياً وتُعيد منطقياً ناتج `connectedDevices.containsKey(id)`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:59]

```
60:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:60]

```
61:     override fun disconnect(id: String) {
```
> يُعرِّف دالة `disconnect` (قطع الاتصال) مُتجاوِزة تأخذ `id` نصياً ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:61]

```
62:         connectedDevices[id]?.gatt?.let {
```
> يصل إلى عنصر `connectedDevices[id]` ثم خاصيته `gatt` بأمان، ويُنفّذ كتلة `let` إن لم تكن عدماً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:62]

```
63:             try { it.disconnect() } catch (_: Exception) { }
```
> يحاول استدعاء `it.disconnect()` ويلتقط أي استثناء `Exception` دون فعل شيء. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:63]

```
64:         }
```
> إغلاق نطاق كتلة `let`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:64]

```
65:         cleanupDeviceConnection(id)
```
> يستدعي دالة `cleanupDeviceConnection` (تنظيف اتصال الجهاز) مُمرِّراً `id`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:65]

```
66:         Log.d(TAG, "Requested disconnect for $id")
```
> يكتب سجلاً تصحيحياً عبر `Log.d` بالوسم `TAG` والنص `"Requested disconnect for $id"`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:66]

```
67:     }
```
> إغلاق نطاق دالة `disconnect`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:67]

```
68: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:68]

```
69:     override fun getConnectionCount(): Int = connectedDevices.size
```
> يُعرِّف دالة `getConnectionCount` (جلب عدد الاتصالات) مُتجاوِزة تُعيد عدداً صحيحاً هو `connectedDevices.size`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:69]

```
70:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:70]

```
71:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:71]

```
72:      * Add a device connection
```
> تعليق: إضافة اتصال جهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:72]

```
73:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:73]

```
74:     fun addDeviceConnection(deviceAddress: String, deviceConn: DeviceConnection) {
```
> يُعرِّف دالة `addDeviceConnection` (إضافة اتصال جهاز) تأخذ `deviceAddress` نصياً و`deviceConn` من نوع `DeviceConnection` ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:74]

```
75:         Log.d(TAG, "Tracker: Adding device connection for $deviceAddress (isClient: ${deviceConn.isClient}")
```
> يكتب سجلاً تصحيحياً عبر `Log.d` بالوسم `TAG` والنص الذي يضمّ `deviceAddress` وقيمة `deviceConn.isClient`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:75]

```
76:         connectedDevices[deviceAddress] = deviceConn
```
> يضبط عنصر `connectedDevices[deviceAddress]` إلى `deviceConn`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:76]

```
77:         removePendingConnection(deviceAddress)
```
> يستدعي دالة `removePendingConnection` (إزالة الاتصال المعلّق) مُمرِّراً `deviceAddress`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:77]

```
78:         // Mark as awaiting first ANNOUNCE on this connection
```
> تعليق: وسمه على أنه ينتظر أول إعلان (ANNOUNCE) على هذا الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:78]

```
79:         firstAnnounceSeen[deviceAddress] = false
```
> يضبط عنصر `firstAnnounceSeen[deviceAddress]` إلى `false`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:79]

```
80:     }
```
> إغلاق نطاق دالة `addDeviceConnection`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:80]

```
81:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:81]

```
82:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:82]

```
83:      * Update a device connection
```
> تعليق: تحديث اتصال جهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:83]

```
84:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:84]

```
85:     fun updateDeviceConnection(deviceAddress: String, deviceConn: DeviceConnection) {
```
> يُعرِّف دالة `updateDeviceConnection` (تحديث اتصال جهاز) تأخذ `deviceAddress` نصياً و`deviceConn` من نوع `DeviceConnection` ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:85]

```
86:         connectedDevices[deviceAddress] = deviceConn
```
> يضبط عنصر `connectedDevices[deviceAddress]` إلى `deviceConn`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:86]

```
87:     }
```
> إغلاق نطاق دالة `updateDeviceConnection`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:87]

```
88:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:88]

```
89:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:89]

```
90:      * Get a device connection
```
> تعليق: جلب اتصال جهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:90]

```
91:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:91]

```
92:     fun getDeviceConnection(deviceAddress: String): DeviceConnection? {
```
> يُعرِّف دالة `getDeviceConnection` (جلب اتصال جهاز) تأخذ `deviceAddress` نصياً وتُعيد `DeviceConnection?` قابلاً للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:92]

```
93:         return connectedDevices[deviceAddress]
```
> يُعيد عنصر `connectedDevices[deviceAddress]`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:93]

```
94:     }
```
> إغلاق نطاق دالة `getDeviceConnection`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:94]

```
95:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:95]

```
96:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:96]

```
97:      * Get all connected devices
```
> تعليق: جلب كل الأجهزة المتصلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:97]

```
98:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:98]

```
99:     fun getConnectedDevices(): Map<String, DeviceConnection> {
```
> يُعرِّف دالة `getConnectedDevices` (جلب الأجهزة المتصلة) تُعيد `Map` بمفتاح نصي وقيمة `DeviceConnection`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:99]

```
100:         return connectedDevices.toMap()
```
> يُعيد `connectedDevices.toMap()` (نسخة خريطة). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:100]

```
101:     }
```
> إغلاق نطاق دالة `getConnectedDevices`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:101]

```
102:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:102]

```
103:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:103]

```
104:      * Get subscribed devices (for server connections)
```
> تعليق: جلب الأجهزة المشتركة (لاتصالات الخادم). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:104]

```
105:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:105]

```
106:     fun getSubscribedDevices(): List<BluetoothDevice> {
```
> يُعرِّف دالة `getSubscribedDevices` (جلب الأجهزة المشتركة) تُعيد `List` من `BluetoothDevice`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:106]

```
107:         return subscribedDevices.toList()
```
> يُعيد `subscribedDevices.toList()` (نسخة قائمة). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:107]

```
108:     }
```
> إغلاق نطاق دالة `getSubscribedDevices`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:108]

```
109:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:109]

```
110:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:110]

```
111:      * Get current RSSI for a device address
```
> تعليق: جلب شدة الإشارة (RSSI) الحالية لعنوان جهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:111]

```
112:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:112]

```
113:     fun getDeviceRSSI(deviceAddress: String): Int? {
```
> يُعرِّف دالة `getDeviceRSSI` (جلب شدة إشارة الجهاز) تأخذ `deviceAddress` نصياً وتُعيد عدداً صحيحاً قابلاً للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:113]

```
114:         return connectedDevices[deviceAddress]?.rssi?.takeIf { it != Int.MIN_VALUE }
```
> يُعيد `rssi` لعنصر `connectedDevices[deviceAddress]` بشرط أن يختلف عن `Int.MIN_VALUE` وإلا فيُعيد عدماً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:114]

```
115:     }
```
> إغلاق نطاق دالة `getDeviceRSSI`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:115]

```
116:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:116]

```
117:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:117]

```
118:      * Store RSSI from scan results
```
> تعليق: تخزين شدة الإشارة (RSSI) من نتائج المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:118]

```
119:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:119]

```
120:     fun updateScanRSSI(deviceAddress: String, rssi: Int) {
```
> يُعرِّف دالة `updateScanRSSI` (تحديث شدة إشارة المسح) تأخذ `deviceAddress` نصياً و`rssi` عدداً صحيحاً، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:120]

```
121:         scanRSSI[deviceAddress] = rssi
```
> يضبط عنصر `scanRSSI[deviceAddress]` إلى قيمة `rssi`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:121]

```
122:     }
```
> إغلاق نطاق دالة `updateScanRSSI`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:122]

```
123:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:123]

```
124:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:124]

```
125:      * Get best available RSSI for a device (connection RSSI preferred, then scan RSSI)
```
> تعليق: جلب أفضل شدة إشارة (RSSI) متاحة لجهاز (تُفضَّل شدة الاتصال ثم شدة المسح). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:125]

```
126:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:126]

```
127:     fun getBestRSSI(deviceAddress: String): Int? {
```
> يُعرِّف دالة `getBestRSSI` (جلب أفضل شدة إشارة) تأخذ `deviceAddress` نصياً وتُعيد عدداً صحيحاً قابلاً للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:127]

```
128:         // Prefer connection RSSI if available and valid
```
> تعليق: فضِّل شدة إشارة الاتصال إن كانت متاحة وصالحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:128]

```
129:         connectedDevices[deviceAddress]?.rssi?.takeIf { it != Int.MIN_VALUE }?.let { return it }
```
> يأخذ `rssi` لعنصر `connectedDevices[deviceAddress]` بشرط اختلافه عن `Int.MIN_VALUE`، فإن وُجِد يُعيده عبر `return`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:129]

```
130:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:130]

```
131:         // Fall back to scan RSSI
```
> تعليق: ارجِع إلى شدة إشارة المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:131]

```
132:         return scanRSSI[deviceAddress]
```
> يُعيد عنصر `scanRSSI[deviceAddress]`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:132]

```
133:     }
```
> إغلاق نطاق دالة `getBestRSSI`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:133]

```
134:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:134]

```
135:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:135]

```
136:      * Add a subscribed device
```
> تعليق: إضافة جهاز مشترك. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:136]

```
137:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:137]

```
138:     fun addSubscribedDevice(device: BluetoothDevice) {
```
> يُعرِّف دالة `addSubscribedDevice` (إضافة جهاز مشترك) تأخذ `device` من نوع `BluetoothDevice`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:138]

```
139:         subscribedDevices.add(device)
```
> يستدعي `subscribedDevices.add(device)` لإضافة الجهاز إلى القائمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:139]

```
140:     }
```
> إغلاق نطاق دالة `addSubscribedDevice`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:140]

```
141:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:141]

```
142:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:142]

```
143:      * Remove a subscribed device
```
> تعليق: إزالة جهاز مشترك. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:143]

```
144:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:144]

```
145:     fun removeSubscribedDevice(device: BluetoothDevice) {
```
> يُعرِّف دالة `removeSubscribedDevice` (إزالة جهاز مشترك) تأخذ `device` من نوع `BluetoothDevice`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:145]

```
146:         subscribedDevices.remove(device)
```
> يستدعي `subscribedDevices.remove(device)` لإزالة الجهاز من القائمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:146]

```
147:     }
```
> إغلاق نطاق دالة `removeSubscribedDevice`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:147]

```
148:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:148]

```
149:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:149]

```
150:      * Check if device is already connected
```
> تعليق: تحقّق ممّا إذا كان الجهاز متصلاً بالفعل. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:150]

```
151:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:151]

```
152:     fun isDeviceConnected(deviceAddress: String): Boolean = isConnected(deviceAddress)
```
> يُعرِّف دالة `isDeviceConnected` (أمُتّصل الجهاز) تأخذ `deviceAddress` نصياً وتُعيد منطقياً ناتج `isConnected(deviceAddress)`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:152]

```
153: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:153]

```
154:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:154]

```
155:      * Check if a peer is already connected (by PeerID)
```
> تعليق: تحقّق ممّا إذا كان النِّد متصلاً بالفعل (عبر معرّف النِّد). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:155]

```
156:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:156]

```
157:     fun isPeerConnected(peerID: String): Boolean {
```
> يُعرِّف دالة `isPeerConnected` (أمُتّصل النِّد) تأخذ `peerID` نصياً وتُعيد منطقياً، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:157]

```
158:         // Only consider actual connected devices that have identified themselves
```
> تعليق: لا تعتبر سوى الأجهزة المتصلة فعلاً التي عرّفت عن نفسها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:158]

```
159:         return connectedDevices.values.any { it.peerID == peerID }
```
> يُعيد ناتج `connectedDevices.values.any` الذي يفحص وجود أي قيمة خاصيتها `peerID` تساوي `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:159]

```
160:     }
```
> إغلاق نطاق دالة `isPeerConnected`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:160]

```
161:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:161]

```
162:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:162]

```
163:      * Disconnect a specific device (by MAC address)
```
> تعليق: قطع اتصال جهاز محدّد (عبر عنوان MAC). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:163]

```
164:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:164]

```
165:     fun disconnectDevice(deviceAddress: String) = disconnect(deviceAddress)
```
> يُعرِّف دالة `disconnectDevice` (قطع اتصال جهاز) تأخذ `deviceAddress` نصياً وتُكافئ استدعاء `disconnect(deviceAddress)`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:165]

```
166:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:166]

```
167:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:167]

```
168:      * Get connected device count
```
> تعليق: جلب عدد الأجهزة المتصلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:168]

```
169:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:169]

```
170:     fun getConnectedDeviceCount(): Int = getConnectionCount()
```
> يُعرِّف دالة `getConnectedDeviceCount` (جلب عدد الأجهزة المتصلة) تُعيد عدداً صحيحاً ناتج `getConnectionCount()`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:170]

```
171:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:171]

```
172:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:172]

```
173:      * Check if connection limit is reached
```
> تعليق: تحقّق ممّا إذا كان حدّ الاتصال قد بُلِغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:173]

```
174:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:174]

```
175:     /**
```
> بداية تعليق توثيق (ثانٍ متتالٍ). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:175]

```
176:      * Check if a new client connection is allowed based on limits
```
> تعليق: تحقّق ممّا إذا كان يُسمَح باتصال عميل جديد بناءً على الحدود. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:176]

```
177:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:177]

```
178:     fun canConnectAsClient(maxOverall: Int, maxClient: Int): Boolean {
```
> يُعرِّف دالة `canConnectAsClient` (أيمكن الاتصال كعميل) تأخذ `maxOverall` (الحدّ الكلي) و`maxClient` (حدّ العملاء) عددين صحيحين وتُعيد منطقياً، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:178]

```
179:         val total = connectedDevices.size
```
> يُعرِّف متغيراً للقراءة فقط `total` (المجموع) ويضبطه إلى `connectedDevices.size`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:179]

```
180:         val clients = connectedDevices.values.count { it.isClient }
```
> يُعرِّف متغيراً للقراءة فقط `clients` (العملاء) ويضبطه إلى عدد القيم التي خاصيتها `isClient` صادقة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:180]

```
181:         return total < maxOverall && clients < maxClient
```
> يُعيد منطقياً صادقاً إذا كان `total` أصغر من `maxOverall` و`clients` أصغر من `maxClient` معاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:181]

```
182:     }
```
> إغلاق نطاق دالة `canConnectAsClient`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:182]

```
183:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:183]

```
184:     /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:184]

```
185:      * Calculate which connections should be evicted to satisfy limits.
```
> تعليق: احسب أي الاتصالات يجب طردها لتحقيق الحدود. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:185]

```
186:      * Logic:
```
> تعليق: المنطق:. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:186]

```
187:      * 1. Enforce strict role limits (maxClient, maxServer) - evict oldest excess.
```
> تعليق: ١. افرض حدود الأدوار الصارمة (maxClient، maxServer) — اطرد الفائض الأقدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:187]

```
188:      * 2. Enforce overall limit (maxOverall) - evict oldest remaining, preferring clients.
```
> تعليق: ٢. افرض الحدّ الكلي (maxOverall) — اطرد الأقدم المتبقّي مع تفضيل العملاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:188]

```
189:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:189]

```
190:     fun getConnectionsToEvict(maxOverall: Int, maxServer: Int, maxClient: Int): List<DeviceConnection> {
```
> يُعرِّف دالة `getConnectionsToEvict` (جلب الاتصالات الواجب طردها) تأخذ `maxOverall` و`maxServer` و`maxClient` أعداداً صحيحة وتُعيد `List` من `DeviceConnection`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:190]

```
191:         val toEvict = mutableSetOf<DeviceConnection>()
```
> يُعرِّف متغيراً للقراءة فقط `toEvict` (للطرد) ويضبطه إلى مجموعة قابلة للتعديل `mutableSetOf` من `DeviceConnection`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:191]

```
192:         val currentDevices = connectedDevices.values.toList()
```
> يُعرِّف متغيراً للقراءة فقط `currentDevices` (الأجهزة الحالية) ويضبطه إلى `connectedDevices.values.toList()`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:192]

```
193:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:193]

```
194:         // 1. Enforce Role Limits
```
> تعليق: ١. افرض حدود الأدوار. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:194]

```
195:         val clients = currentDevices.filter { it.isClient }.sortedBy { it.connectedAt }
```
> يُعرِّف متغيراً للقراءة فقط `clients` (العملاء) ويضبطه إلى عناصر `currentDevices` التي خاصيتها `isClient` صادقة، مرتّبةً تصاعدياً حسب `connectedAt`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:195]

```
196:         if (clients.size > maxClient) {
```
> يفتح شرطاً يتحقّق ممّا إذا كان `clients.size` أكبر من `maxClient`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:196]

```
197:             toEvict.addAll(clients.take(clients.size - maxClient))
```
> يضيف إلى `toEvict` أول `clients.size - maxClient` عنصراً من `clients` عبر `take`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:197]

```
198:         }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:198]

```
199:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:199]

```
200:         val servers = currentDevices.filter { !it.isClient }.sortedBy { it.connectedAt }
```
> يُعرِّف متغيراً للقراءة فقط `servers` (الخوادم) ويضبطه إلى عناصر `currentDevices` التي خاصيتها `isClient` كاذبة، مرتّبةً تصاعدياً حسب `connectedAt`. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:200]
