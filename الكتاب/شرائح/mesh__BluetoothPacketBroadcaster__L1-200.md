# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt (الأسطر 1–200)

```
1: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:1]

```
2: package com.bitchat.android.mesh
```
> يُعرّف هذا الملف ضمن الحزمة (package) باسم `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:2]

```
3: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:3]

```
4: import android.bluetooth.BluetoothDevice
```
> يستورد (import) الصنف `BluetoothDevice` من حزمة `android.bluetooth`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:4]

```
5: import android.bluetooth.BluetoothGatt
```
> يستورد الصنف `BluetoothGatt` من حزمة `android.bluetooth`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:5]

```
6: import android.bluetooth.BluetoothGattCharacteristic
```
> يستورد الصنف `BluetoothGattCharacteristic` (خاصيّة جات) من حزمة `android.bluetooth`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:6]

```
7: import android.bluetooth.BluetoothGattServer
```
> يستورد الصنف `BluetoothGattServer` (خادم جات) من حزمة `android.bluetooth`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:7]

```
8: import android.util.Log
```
> يستورد الصنف `Log` (للتسجيل) من حزمة `android.util`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:8]

```
9: import com.bitchat.android.protocol.SpecialRecipients
```
> يستورد الكائن `SpecialRecipients` (المستلِمون الخاصون) من حزمة `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:9]

```
10: import com.bitchat.android.model.RoutedPacket
```
> يستورد الصنف `RoutedPacket` (الحزمة المُوجَّهة) من حزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:10]

```
11: import com.bitchat.android.protocol.MessageType
```
> يستورد الصنف `MessageType` (نوع الرسالة) من حزمة `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:11]

```
12: import com.bitchat.android.util.toHexString
```
> يستورد الدالة `toHexString` (التحويل إلى نص ست عشري) من حزمة `com.bitchat.android.util`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:12]

```
13: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف `CoroutineScope` (نطاق الكوروتين) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:13]

```
14: import kotlinx.coroutines.Dispatchers
```
> يستورد الكائن `Dispatchers` (المُوزِّعات) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:14]

```
15: import kotlinx.coroutines.SupervisorJob
```
> يستورد الدالة `SupervisorJob` (المهمّة المُشرِفة) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:15]

```
16: import kotlinx.coroutines.cancel
```
> يستورد الدالة `cancel` (الإلغاء) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:16]

```
17: import kotlinx.coroutines.delay
```
> يستورد الدالة `delay` (التأخير) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:17]

```
18: import kotlinx.coroutines.isActive
```
> يستورد الخاصيّة `isActive` (هل نشط) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:18]

```
19: import kotlinx.coroutines.launch
```
> يستورد الدالة `launch` (الإطلاق) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:19]

```
20: import kotlinx.coroutines.channels.Channel
```
> يستورد الصنف `Channel` (القناة) من حزمة `kotlinx.coroutines.channels`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:20]

```
21: import kotlinx.coroutines.channels.actor
```
> يستورد الدالة `actor` (المُمثِّل) من حزمة `kotlinx.coroutines.channels`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:21]

```
22: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:22]

```
23: /**
```
> تعليق: بداية كتلة توثيق (تعليق جافادوك). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:23]

```
24:  * Handles packet broadcasting to connected devices using actor pattern for serialization
```
> تعليق: «يتولّى بثّ الحزم إلى الأجهزة المتصلة باستخدام نمط المُمثِّل من أجل التسلسل». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:24]

```
25:  * 
```
> تعليق: سطر تعليق فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:25]

```
26:  * In Bluetooth Low Energy (BLE):
```
> تعليق: «في بلوتوث منخفض الطاقة (BLE):». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:26]

```
27:  *
```
> تعليق: سطر تعليق فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:27]

```
28:  * Peripheral (server):
```
> تعليق: «الطرف المحيطي (الخادم):». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:28]

```
29:  * Advertises.
```
> تعليق: «يُعلِن (يبثّ إعلانات وجوده)». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:29]

```
30:  * Accepts connections.
```
> تعليق: «يقبل الاتصالات». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:30]

```
31:  * Hosts a GATT server.
```
> تعليق: «يستضيف خادم GATT». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:31]

```
32:  * Remote devices read/write/subscribe to characteristics.
```
> تعليق: «الأجهزة البعيدة تقرأ/تكتب/تشترك في الخاصيّات». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:32]

```
33:  *
```
> تعليق: سطر تعليق فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:33]

```
34:  *  Central (client):
```
> تعليق: «المركزي (العميل):». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:34]

```
35:  * Scans.
```
> تعليق: «يمسح (يبحث عن الأجهزة)». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:35]

```
36:  * Initiates connections.
```
> تعليق: «يبدأ الاتصالات». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:36]

```
37:  * Hosts a GATT client.
```
> تعليق: «يستضيف عميل GATT». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:37]

```
38:  * Reads/writes to the peripheral’s characteristics.
```
> تعليق: «يقرأ/يكتب إلى خاصيّات الطرف المحيطي». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:38]

```
39:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:39]

```
40: class BluetoothPacketBroadcaster(
```
> يُعرّف الصنف `BluetoothPacketBroadcaster` (باثّ حزم البلوتوث) ويبدأ قائمة معاملات الباني الأساسي. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:40]

```
41:     private val connectionScope: CoroutineScope,
```
> يُعرّف معاملاً خاصاً ثابتاً `connectionScope` (نطاق الاتصال) من نوع `CoroutineScope`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:41]

```
42:     private val connectionTracker: BluetoothConnectionTracker,
```
> يُعرّف معاملاً خاصاً ثابتاً `connectionTracker` (مُتتبِّع الاتصال) من نوع `BluetoothConnectionTracker`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:42]

```
43:     private val fragmentManager: FragmentManager?,
```
> يُعرّف معاملاً خاصاً ثابتاً `fragmentManager` (مدير التجزئة) من نوع `FragmentManager` قابل لأن يكون فارغاً (nullable). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:43]

```
44:     private val myPeerID: String
```
> يُعرّف معاملاً خاصاً ثابتاً `myPeerID` (معرّف نِدّي الخاص) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:44]

```
45: ) {
```
> يُغلق قائمة معاملات الباني ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:45]

```
46:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:46]

```
47:     companion object {
```
> يفتح كائناً مُرافِقاً (companion object) داخل الصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:47]

```
48:         private const val TAG = "BluetoothPacketBroadcaster"
```
> يُعرّف ثابتاً خاصاً `TAG` (وسم التسجيل) بقيمة نصّية `"BluetoothPacketBroadcaster"`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:48]

```
49:         private const val CLEANUP_DELAY = com.bitchat.android.util.AppConstants.Mesh.BROADCAST_CLEANUP_DELAY_MS
```
> يُعرّف ثابتاً خاصاً `CLEANUP_DELAY` (تأخير التنظيف) بقيمة `AppConstants.Mesh.BROADCAST_CLEANUP_DELAY_MS`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:49]

```
50:     }
```
> إغلاق نطاق (نهاية الكائن المُرافِق). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:50]

```
51: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:51]

```
52:     // Optional nickname resolver injected by higher layer (peerID -> nickname?)
```
> تعليق: «محلّل اسم مستعار اختياري يُحقَن من طبقة أعلى (معرّف نِدّي ← اسم مستعار؟)». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:52]

```
53:     private var nicknameResolver: ((String) -> String?)? = null
```
> يُعرّف متغيّراً خاصاً `nicknameResolver` (محلّل الاسم المستعار) من نوع دالة تأخذ `String` وتُعيد `String?`، وهو نفسه قابل لأن يكون فارغاً، ويُهيّأ بالقيمة `null`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:53]

```
54: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:54]

```
55:     fun setNicknameResolver(resolver: (String) -> String?) {
```
> يُعرّف الدالة `setNicknameResolver` (ضبط محلّل الاسم المستعار) التي تأخذ معاملاً `resolver` من نوع دالة تأخذ `String` وتُعيد `String?`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:55]

```
56:         nicknameResolver = resolver
```
> يُسنِد قيمة المعامل `resolver` إلى المتغيّر `nicknameResolver`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:56]

```
57:     }
```
> إغلاق نطاق (نهاية الدالة `setNicknameResolver`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:57]

```
58:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:58]

```
59:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:59]

```
60:      * Debug logging helper - can be easily removed/disabled for production
```
> تعليق: «مساعد تسجيل لأغراض التنقيح - يمكن إزالته/تعطيله بسهولة للإنتاج». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:60]

```
61:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:61]

```
62:     private fun logPacketRelay(
```
> يُعرّف الدالة الخاصة `logPacketRelay` (تسجيل تمرير الحزمة) ويبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:62]

```
63:         typeName: String,
```
> يُعرّف معاملاً `typeName` (اسم النوع) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:63]

```
64:         senderPeerID: String,
```
> يُعرّف معاملاً `senderPeerID` (معرّف نِدّي المُرسِل) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:64]

```
65:         senderNick: String?,
```
> يُعرّف معاملاً `senderNick` (الاسم المستعار للمُرسِل) من نوع `String?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:65]

```
66:         incomingPeer: String?,
```
> يُعرّف معاملاً `incomingPeer` (النِّدّ الوارد) من نوع `String?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:66]

```
67:         incomingAddr: String?,
```
> يُعرّف معاملاً `incomingAddr` (العنوان الوارد) من نوع `String?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:67]

```
68:         toPeer: String?,
```
> يُعرّف معاملاً `toPeer` (إلى النِّدّ) من نوع `String?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:68]

```
69:         toDeviceAddress: String,
```
> يُعرّف معاملاً `toDeviceAddress` (عنوان الجهاز المستهدف) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:69]

```
70:         ttl: UByte,
```
> يُعرّف معاملاً `ttl` (مدّة البقاء، عدد القفزات) من نوع `UByte` (بايت بلا إشارة). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:70]

```
71:         packetVersion: UByte = 1u,
```
> يُعرّف معاملاً `packetVersion` (إصدار الحزمة) من نوع `UByte` بقيمة افتراضية `1u`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:71]

```
72:         routeInfo: String? = null
```
> يُعرّف معاملاً `routeInfo` (معلومات المسار) من نوع `String?` بقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:72]

```
73:     ) {
```
> يُغلق قائمة معاملات الدالة `logPacketRelay` ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:73]

```
74:         try {
```
> يفتح كتلة `try` (محاولة). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:74]

```
75:             val fromNick = incomingPeer?.let { nicknameResolver?.invoke(it) }
```
> يُعرّف ثابتاً محلياً `fromNick` (الاسم المستعار للمصدر) بحيث إذا لم يكن `incomingPeer` فارغاً يُستدعى `nicknameResolver` عليه عبر `invoke`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:75]

```
76:             val toNick = toPeer?.let { nicknameResolver?.invoke(it) }
```
> يُعرّف ثابتاً محلياً `toNick` (الاسم المستعار للوجهة) بحيث إذا لم يكن `toPeer` فارغاً يُستدعى `nicknameResolver` عليه عبر `invoke`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:76]

```
77:             val manager = com.bitchat.android.ui.debug.DebugSettingsManager.getInstance()
```
> يُعرّف ثابتاً محلياً `manager` (المدير) بقيمة ناتج استدعاء `DebugSettingsManager.getInstance()` (الحصول على النسخة الوحيدة من مدير إعدادات التنقيح). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:77]

```
78:             // Always log outgoing for the actual transmission target
```
> تعليق: «سجّل دائماً الصادر للهدف الفعلي للإرسال». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:78]

```
79:             manager.logOutgoing(
```
> يستدعي الدالة `logOutgoing` (تسجيل الصادر) على `manager` ويبدأ تمرير وسائطها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:79]

```
80:                 packetType = typeName,
```
> يُمرّر للوسيط المُسمّى `packetType` (نوع الحزمة) القيمة `typeName`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:80]

```
81:                 toPeerID = toPeer,
```
> يُمرّر للوسيط المُسمّى `toPeerID` القيمة `toPeer`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:81]

```
82:                 toNickname = toNick,
```
> يُمرّر للوسيط المُسمّى `toNickname` القيمة `toNick`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:82]

```
83:                 toDeviceAddress = toDeviceAddress,
```
> يُمرّر للوسيط المُسمّى `toDeviceAddress` القيمة `toDeviceAddress`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:83]

```
84:                 previousHopPeerID = incomingPeer,
```
> يُمرّر للوسيط المُسمّى `previousHopPeerID` (معرّف نِدّي القفزة السابقة) القيمة `incomingPeer`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:84]

```
85:                 packetVersion = packetVersion,
```
> يُمرّر للوسيط المُسمّى `packetVersion` القيمة `packetVersion`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:85]

```
86:                 routeInfo = routeInfo
```
> يُمرّر للوسيط المُسمّى `routeInfo` القيمة `routeInfo`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:86]

```
87:             )
```
> يُغلق استدعاء `logOutgoing`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:87]

```
88:             // Keep the verbose relay message for human readability
```
> تعليق: «احتفظ برسالة التمرير المُفصَّلة من أجل سهولة القراءة البشرية». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:88]

```
89:             manager.logPacketRelayDetailed(
```
> يستدعي الدالة `logPacketRelayDetailed` (تسجيل تمرير الحزمة المُفصّل) على `manager` ويبدأ تمرير وسائطها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:89]

```
90:                 packetType = typeName,
```
> يُمرّر للوسيط المُسمّى `packetType` القيمة `typeName`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:90]

```
91:                 senderPeerID = senderPeerID,
```
> يُمرّر للوسيط المُسمّى `senderPeerID` القيمة `senderPeerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:91]

```
92:                 senderNickname = senderNick,
```
> يُمرّر للوسيط المُسمّى `senderNickname` القيمة `senderNick`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:92]

```
93:                 fromPeerID = incomingPeer,
```
> يُمرّر للوسيط المُسمّى `fromPeerID` القيمة `incomingPeer`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:93]

```
94:                 fromNickname = fromNick,
```
> يُمرّر للوسيط المُسمّى `fromNickname` القيمة `fromNick`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:94]

```
95:                 fromDeviceAddress = incomingAddr,
```
> يُمرّر للوسيط المُسمّى `fromDeviceAddress` القيمة `incomingAddr`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:95]

```
96:                 toPeerID = toPeer,
```
> يُمرّر للوسيط المُسمّى `toPeerID` القيمة `toPeer`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:96]

```
97:                 toNickname = toNick,
```
> يُمرّر للوسيط المُسمّى `toNickname` القيمة `toNick`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:97]

```
98:                 toDeviceAddress = toDeviceAddress,
```
> يُمرّر للوسيط المُسمّى `toDeviceAddress` القيمة `toDeviceAddress`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:98]

```
99:                 ttl = ttl,
```
> يُمرّر للوسيط المُسمّى `ttl` القيمة `ttl`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:99]

```
100:                 isRelay = true,
```
> يُمرّر للوسيط المُسمّى `isRelay` (هل تمرير) القيمة `true`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:100]

```
101:                 packetVersion = packetVersion,
```
> يُمرّر للوسيط المُسمّى `packetVersion` القيمة `packetVersion`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:101]

```
102:                 routeInfo = routeInfo
```
> يُمرّر للوسيط المُسمّى `routeInfo` القيمة `routeInfo`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:102]

```
103:             )
```
> يُغلق استدعاء `logPacketRelayDetailed`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:103]

```
104:         } catch (_: Exception) { 
```
> يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط أي استثناء (Exception) دون تسميته. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:104]

```
105:             // Silently ignore debug logging failures
```
> تعليق: «تجاهل بصمت إخفاقات تسجيل التنقيح». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:105]

```
106:         }
```
> إغلاق نطاق (نهاية كتلة `catch`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:106]

```
107:     }
```
> إغلاق نطاق (نهاية الدالة `logPacketRelay`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:107]

```
108:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:108]

```
109:     // Data class to hold broadcast request information
```
> تعليق: «صنف بيانات لحمل معلومات طلب البثّ». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:109]

```
110:     private data class BroadcastRequest(
```
> يُعرّف صنف بيانات خاصاً `BroadcastRequest` (طلب البثّ) ويبدأ قائمة خصائصه. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:110]

```
111:         val routed: RoutedPacket,
```
> يُعرّف خاصيّة ثابتة `routed` (المُوجَّهة) من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:111]

```
112:         val gattServer: BluetoothGattServer?,
```
> يُعرّف خاصيّة ثابتة `gattServer` (خادم جات) من نوع `BluetoothGattServer?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:112]

```
113:         val characteristic: BluetoothGattCharacteristic?
```
> يُعرّف خاصيّة ثابتة `characteristic` (الخاصيّة) من نوع `BluetoothGattCharacteristic?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:113]

```
114:     )
```
> يُغلق قائمة خصائص صنف البيانات `BroadcastRequest`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:114]

```
115:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:115]

```
116:     // Actor scope for the broadcaster
```
> تعليق: «نطاق المُمثِّل للباثّ». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:116]

```
117:     private val broadcasterScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يُعرّف ثابتاً خاصاً `broadcasterScope` (نطاق الباثّ) بقيمة `CoroutineScope` مُكوَّن من `Dispatchers.IO` مع `SupervisorJob()`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:117]

```
118:     private val fragmentingSender = FragmentingPacketSender(connectionScope, fragmentManager, TAG)
```
> يُعرّف ثابتاً خاصاً `fragmentingSender` (مُرسِل التجزئة) بقيمة كائن `FragmentingPacketSender` مُنشأ بالوسائط `connectionScope` و`fragmentManager` و`TAG`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:118]

```
119:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:119]

```
120:     // SERIALIZATION: Actor to serialize all broadcast operations
```
> تعليق: «التسلسل: مُمثِّل لجعل كل عمليات البثّ متسلسلة». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:120]

```
121:     @OptIn(kotlinx.coroutines.ObsoleteCoroutinesApi::class)
```
> يُطبّق التعليق التوضيحي `@OptIn` للموافقة على استخدام واجهة `ObsoleteCoroutinesApi` (واجهة كوروتينات متقادمة). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:121]

```
122:     private val broadcasterActor = broadcasterScope.actor<BroadcastRequest>(
```
> يُعرّف ثابتاً خاصاً `broadcasterActor` (مُمثِّل الباثّ) بإنشاء مُمثِّل عبر `broadcasterScope.actor` من نوع عنصر `BroadcastRequest` ويبدأ تمرير وسائطه. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:122]

```
123:         capacity = Channel.UNLIMITED
```
> يُمرّر للوسيط المُسمّى `capacity` (السعة) القيمة `Channel.UNLIMITED` (غير محدودة). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:123]

```
124:     ) {
```
> يُغلق وسائط `actor` ويفتح جسم المُمثِّل (لامبدا). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:124]

```
125:         Log.d(TAG, "🎭 Created packet broadcaster actor")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بالوسم `TAG` ونصّها «🎭 Created packet broadcaster actor». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:125]

```
126:         try {
```
> يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:126]

```
127:             for (request in channel) {
```
> يفتح حلقة `for` تكرّر على كل `request` (طلب) في `channel` (قناة المُمثِّل). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:127]

```
128:                 broadcastSinglePacketInternal(request.routed, request.gattServer, request.characteristic)
```
> يستدعي الدالة `broadcastSinglePacketInternal` (بثّ حزمة مفردة داخلياً) بالوسائط `request.routed` و`request.gattServer` و`request.characteristic`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:128]

```
129:             }
```
> إغلاق نطاق (نهاية حلقة `for`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:129]

```
130:         } finally {
```
> يُغلق كتلة `try` ويفتح كتلة `finally` (تُنفَّذ على كل حال). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:130]

```
131:             Log.d(TAG, "🎭 Packet broadcaster actor terminated")
```
> يستدعي `Log.d` لتسجيل رسالة تنقيح بالوسم `TAG` ونصّها «🎭 Packet broadcaster actor terminated». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:131]

```
132:         }
```
> إغلاق نطاق (نهاية كتلة `finally`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:132]

```
133:     }
```
> إغلاق نطاق (نهاية جسم المُمثِّل `broadcasterActor`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:133]

```
134:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:134]

```
135:     fun broadcastPacket(
```
> يُعرّف الدالة العامة `broadcastPacket` (بثّ الحزمة) ويبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:135]

```
136:         routed: RoutedPacket,
```
> يُعرّف معاملاً `routed` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:136]

```
137:         gattServer: BluetoothGattServer?,
```
> يُعرّف معاملاً `gattServer` من نوع `BluetoothGattServer?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:137]

```
138:         characteristic: BluetoothGattCharacteristic?
```
> يُعرّف معاملاً `characteristic` من نوع `BluetoothGattCharacteristic?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:138]

```
139:     ) {
```
> يُغلق قائمة معاملات `broadcastPacket` ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:139]

```
140:         fragmentingSender.send(routed, "BLE broadcast") { packet ->
```
> يستدعي الدالة `send` على `fragmentingSender` بالوسيطين `routed` والنصّ `"BLE broadcast"` ويمرّر لامبدا يأخذ المعامل `packet`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:140]

```
141:             broadcastSinglePacket(packet, gattServer, characteristic)
```
> يستدعي الدالة `broadcastSinglePacket` (بثّ حزمة مفردة) بالوسائط `packet` و`gattServer` و`characteristic`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:141]

```
142:             true
```
> يُعيد القيمة `true` كنتيجة اللامبدا. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:142]

```
143:         }
```
> إغلاق نطاق (نهاية اللامبدا الممرّر إلى `send`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:143]

```
144:     }
```
> إغلاق نطاق (نهاية الدالة `broadcastPacket`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:144]

```
145: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:145]

```
146:     fun cancelTransfer(transferId: String): Boolean {
```
> يُعرّف الدالة العامة `cancelTransfer` (إلغاء النقل) التي تأخذ معاملاً `transferId` (معرّف النقل) من نوع `String` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:146]

```
147:         return fragmentingSender.cancelTransfer(transferId)
```
> يُعيد ناتج استدعاء `cancelTransfer` على `fragmentingSender` بالوسيط `transferId`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:147]

```
148:     }
```
> إغلاق نطاق (نهاية الدالة `cancelTransfer`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:148]

```
149: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:149]

```
150:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:150]

```
151:      * Send a packet to a specific peer only, without broadcasting.
```
> تعليق: «أرسِل حزمة إلى نِدّ محدّد فقط، دون بثّ». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:151]

```
152:      * Returns true if a direct path was found and used.
```
> تعليق: «يُعيد true إذا وُجِد مسار مباشر واستُخدِم». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:152]

```
153:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:153]

```
154:     fun sendPacketToPeer(
```
> يُعرّف الدالة العامة `sendPacketToPeer` (إرسال الحزمة إلى نِدّ) ويبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:154]

```
155:         routed: RoutedPacket,
```
> يُعرّف معاملاً `routed` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:155]

```
156:         targetPeerID: String,
```
> يُعرّف معاملاً `targetPeerID` (معرّف النِّدّ المستهدف) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:156]

```
157:         gattServer: BluetoothGattServer?,
```
> يُعرّف معاملاً `gattServer` من نوع `BluetoothGattServer?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:157]

```
158:         characteristic: BluetoothGattCharacteristic?
```
> يُعرّف معاملاً `characteristic` من نوع `BluetoothGattCharacteristic?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:158]

```
159:     ): Boolean {
```
> يُغلق قائمة معاملات `sendPacketToPeer`، ويُحدّد نوع الإرجاع `Boolean`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:159]

```
160:         if (!hasPeerConnection(targetPeerID)) return false
```
> إذا لم تكن نتيجة `hasPeerConnection` (هل يوجد اتصال بالنِّدّ) للوسيط `targetPeerID` صحيحة، يُعيد `false`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:160]

```
161:         return fragmentingSender.send(routed, "BLE peer ${targetPeerID.take(8)}") { packet ->
```
> يُعيد ناتج استدعاء `send` على `fragmentingSender` بالوسيطين `routed` ونصّ `"BLE peer "` متبوعاً بأول ثمانية محارف من `targetPeerID`، ويمرّر لامبدا يأخذ `packet`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:161]

```
162:             sendSinglePacketToPeer(packet, targetPeerID, gattServer, characteristic)
```
> يستدعي الدالة `sendSinglePacketToPeer` (إرسال حزمة مفردة إلى نِدّ) بالوسائط `packet` و`targetPeerID` و`gattServer` و`characteristic`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:162]

```
163:         }
```
> إغلاق نطاق (نهاية اللامبدا الممرّر إلى `send`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:163]

```
164:     }
```
> إغلاق نطاق (نهاية الدالة `sendPacketToPeer`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:164]

```
165: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:165]

```
166:     private fun sendSinglePacketToPeer(
```
> يُعرّف الدالة الخاصة `sendSinglePacketToPeer` ويبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:166]

```
167:         routed: RoutedPacket,
```
> يُعرّف معاملاً `routed` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:167]

```
168:         targetPeerID: String,
```
> يُعرّف معاملاً `targetPeerID` من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:168]

```
169:         gattServer: BluetoothGattServer?,
```
> يُعرّف معاملاً `gattServer` من نوع `BluetoothGattServer?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:169]

```
170:         characteristic: BluetoothGattCharacteristic?
```
> يُعرّف معاملاً `characteristic` من نوع `BluetoothGattCharacteristic?` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:170]

```
171:     ): Boolean {
```
> يُغلق قائمة معاملات `sendSinglePacketToPeer`، ويُحدّد نوع الإرجاع `Boolean`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:171]

```
172:         val packet = routed.packet
```
> يُعرّف ثابتاً محلياً `packet` (الحزمة) بقيمة الخاصيّة `routed.packet`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:172]

```
173:         // iOS-compatible: Use selective padding policy for BLE
```
> تعليق: «متوافق مع iOS: استخدم سياسة حشو انتقائية لـ BLE». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:173]

```
174:         val padForBLE = BLEPacketPaddingPolicy.shouldPadForBLE(packet.type)
```
> يُعرّف ثابتاً محلياً `padForBLE` (الحشو من أجل BLE) بقيمة ناتج استدعاء `BLEPacketPaddingPolicy.shouldPadForBLE` (هل ينبغي الحشو لـ BLE) بالوسيط `packet.type`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:174]

```
175:         val data = packet.toBinaryData(padding = padForBLE) ?: return false
```
> يُعرّف ثابتاً محلياً `data` (البيانات) بقيمة ناتج `packet.toBinaryData` مع الوسيط المُسمّى `padding = padForBLE`، وإن كان الناتج فارغاً يُعيد `false`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:175]

```
176:         val isFile = packet.type == MessageType.FILE_TRANSFER.value
```
> يُعرّف ثابتاً محلياً `isFile` (هل ملف) بنتيجة مقارنة `packet.type` بقيمة `MessageType.FILE_TRANSFER.value`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:176]

```
177:         if (isFile) {
```
> يفتح شرط `if` يتحقق إذا كانت `isFile` صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:177]

```
178:             Log.d(TAG, "📤 Broadcasting FILE_TRANSFER: ${packet.payload.size} bytes")
```
> يستدعي `Log.d` لتسجيل رسالة بالوسم `TAG` نصّها «📤 Broadcasting FILE_TRANSFER:» متبوعاً بحجم `packet.payload` ثم كلمة «bytes». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:178]

```
179:         }
```
> إغلاق نطاق (نهاية شرط `if`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:179]

```
180:         val typeName = MessageType.fromValue(packet.type)?.name ?: packet.type.toString()
```
> يُعرّف ثابتاً محلياً `typeName` بقيمة اسم نوع الرسالة الناتج عن `MessageType.fromValue(packet.type)?.name`، وإن كان فارغاً يستعمل `packet.type.toString()`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:180]

```
181:         val senderPeerID = routed.peerID ?: packet.senderID.toHexString()
```
> يُعرّف ثابتاً محلياً `senderPeerID` بقيمة `routed.peerID`، وإن كان فارغاً يستعمل `packet.senderID.toHexString()`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:181]

```
182:         val incomingAddr = routed.relayAddress
```
> يُعرّف ثابتاً محلياً `incomingAddr` بقيمة الخاصيّة `routed.relayAddress` (عنوان التمرير). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:182]

```
183:         val incomingPeer = incomingAddr?.let { connectionTracker.addressPeerMap[it] }
```
> يُعرّف ثابتاً محلياً `incomingPeer` بحيث إذا لم يكن `incomingAddr` فارغاً يُجلب القيد المقابل له من الخريطة `connectionTracker.addressPeerMap` (خريطة العنوان إلى النِّدّ). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:183]

```
184:         val senderNick = senderPeerID.let { pid -> nicknameResolver?.invoke(pid) }
```
> يُعرّف ثابتاً محلياً `senderNick` بتطبيق `let` على `senderPeerID` باسم `pid` واستدعاء `nicknameResolver` عليه عبر `invoke` إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:184]

```
185:         val route = packet.route
```
> يُعرّف ثابتاً محلياً `route` (المسار) بقيمة الخاصيّة `packet.route`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:185]

```
186:         val routeInfo = if (!route.isNullOrEmpty()) "routed: ${route.size} hops" else null
```
> يُعرّف ثابتاً محلياً `routeInfo` بقيمة نصّ «routed:» متبوعاً بحجم `route` ثم «hops» إن لم يكن `route` فارغاً ولا خالياً، وإلا `null`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:186]

```
187: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:187]

```
188:         // Prefer server-side subscriptions
```
> تعليق: «فضّل الاشتراكات في جانب الخادم». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:188]

```
189:         val serverTarget = connectionTracker.getSubscribedDevices()
```
> يُعرّف ثابتاً محلياً `serverTarget` (هدف الخادم) ويبدأ تعيينه بناتج استدعاء `connectionTracker.getSubscribedDevices()` (الأجهزة المشتركة). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:189]

```
190:             .firstOrNull { connectionTracker.addressPeerMap[it.address] == targetPeerID }
```
> يطبّق `firstOrNull` ليأخذ أوّل جهاز يكون القيد المقابل لعنوانه في `addressPeerMap` مساوياً لـ `targetPeerID`، أو `null`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:190]

```
191:         if (serverTarget != null) {
```
> يفتح شرط `if` يتحقق إذا كان `serverTarget` ليس فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:191]

```
192:             if (notifyDevice(serverTarget, data, gattServer, characteristic)) {
```
> يفتح شرط `if` يتحقق من ناتج استدعاء `notifyDevice` (إخطار الجهاز) بالوسائط `serverTarget` و`data` و`gattServer` و`characteristic`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:192]

```
193:                 logPacketRelay(typeName, senderPeerID, senderNick, incomingPeer, incomingAddr, targetPeerID, serverTarget.address, packet.ttl, packet.version, routeInfo)
```
> يستدعي الدالة `logPacketRelay` بالوسائط `typeName` و`senderPeerID` و`senderNick` و`incomingPeer` و`incomingAddr` و`targetPeerID` و`serverTarget.address` و`packet.ttl` و`packet.version` و`routeInfo` بالترتيب. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:193]

```
194:                 return true
```
> يُعيد `true`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:194]

```
195:             }
```
> إغلاق نطاق (نهاية شرط `if` الداخلي على `notifyDevice`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:195]

```
196:         }
```
> إغلاق نطاق (نهاية شرط `if` على `serverTarget`). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:196]

```
197: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:197]

```
198:         // Then client connections
```
> تعليق: «ثمّ اتصالات العميل». [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:198]

```
199:         val clientTarget = connectionTracker.getConnectedDevices().values
```
> يُعرّف ثابتاً محلياً `clientTarget` (هدف العميل) ويبدأ تعيينه بقِيَم (`values`) ناتج `connectionTracker.getConnectedDevices()` (الأجهزة المتصلة). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:199]

```
200:             .firstOrNull { connectionTracker.addressPeerMap[it.device.address] == targetPeerID }
```
> يطبّق `firstOrNull` ليأخذ أوّل عنصر يكون القيد المقابل لعنوان جهازه (`it.device.address`) في `addressPeerMap` مساوياً لـ `targetPeerID`، أو `null`. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:200]
