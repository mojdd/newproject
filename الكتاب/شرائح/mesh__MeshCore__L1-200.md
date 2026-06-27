# شريحة — app/src/main/java/com/bitchat/android/mesh/MeshCore.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يعلن أنّ هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من `android.content`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` من `android.util`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:4]

```
5: import com.bitchat.android.crypto.EncryptionService
```
> يستورد صنف خدمة التشفير (EncryptionService) من `com.bitchat.android.crypto`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:5]

```
6: import com.bitchat.android.model.BitchatMessage
```
> يستورد صنف رسالة بِتشات (BitchatMessage) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:6]

```
7: import com.bitchat.android.model.BitchatFilePacket
```
> يستورد صنف حُزمة ملف بِتشات (BitchatFilePacket) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:7]

```
8: import com.bitchat.android.model.IdentityAnnouncement
```
> يستورد صنف إعلان الهويّة (IdentityAnnouncement) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:8]

```
9: import com.bitchat.android.model.NoisePayload
```
> يستورد صنف حمولة نويز (NoisePayload) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:9]

```
10: import com.bitchat.android.model.NoisePayloadType
```
> يستورد صنف نوع حمولة نويز (NoisePayloadType) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:10]

```
11: import com.bitchat.android.model.PrivateMessagePacket
```
> يستورد صنف حُزمة الرسالة الخاصّة (PrivateMessagePacket) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:11]

```
12: import com.bitchat.android.model.RequestSyncPacket
```
> يستورد صنف حُزمة طلب المزامنة (RequestSyncPacket) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:12]

```
13: import com.bitchat.android.model.RoutedPacket
```
> يستورد صنف الحُزمة الموجَّهة (RoutedPacket) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:13]

```
14: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد صنف حُزمة بِتشات (BitchatPacket) من `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:14]

```
15: import com.bitchat.android.protocol.MessageType
```
> يستورد صنف نوع الرسالة (MessageType) من `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:15]

```
16: import com.bitchat.android.protocol.SpecialRecipients
```
> يستورد صنف المستلِمين الخاصّين (SpecialRecipients) من `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:16]

```
17: import com.bitchat.android.service.TransportBridgeService
```
> يستورد صنف خدمة جسر النقل (TransportBridgeService) من `com.bitchat.android.service`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:17]

```
18: import com.bitchat.android.sync.GossipSyncManager
```
> يستورد صنف مدير مزامنة الإشاعة (GossipSyncManager) من `com.bitchat.android.sync`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:18]

```
19: import com.bitchat.android.util.toHexString
```
> يستورد الدالّة الموسِّعة `toHexString` من `com.bitchat.android.util`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:19]

```
20: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف `CoroutineScope` (نطاق الكوروتين) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:20]

```
21: import kotlinx.coroutines.Job
```
> يستورد الصنف `Job` (مهمّة) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:21]

```
22: import kotlinx.coroutines.delay
```
> يستورد الدالّة `delay` (تأخير) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:22]

```
23: import kotlinx.coroutines.launch
```
> يستورد الدالّة `launch` (إطلاق) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:23]

```
24: import kotlinx.coroutines.runBlocking
```
> يستورد الدالّة `runBlocking` (تشغيل حاجِب) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:24]

```
25: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف `ConcurrentHashMap` (خريطة تجزئة متزامنة) من `java.util.concurrent`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:25]

```
26: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:26]

```
27: /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:27]

```
28:  * Shared mesh coordinator that wires all mesh-layer components and provides common APIs
```
> تعليق: «منسِّق شبكة مشترَك يربط جميع مكوّنات طبقة الشبكة ويوفّر واجهات برمجية مشترَكة». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:28]

```
29:  * for send/receive operations across transports.
```
> تعليق: «لعمليّات الإرسال/الاستقبال عبر وسائل النقل». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:29]

```
30:  */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:30]

```
31: class MeshCore(
```
> يعرّف الصنف `MeshCore` (نواة الشبكة) وبداية قائمة معامِلات الباني الأوّلي. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:31]

```
32:     private val context: Context,
```
> معامِل بانٍ خاصّ غير قابل للتغيير باسم `context` من نوع `Context`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:32]

```
33:     private val scope: CoroutineScope,
```
> معامِل بانٍ خاصّ غير قابل للتغيير باسم `scope` من نوع `CoroutineScope`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:33]

```
34:     private val transport: MeshTransport,
```
> معامِل بانٍ خاصّ غير قابل للتغيير باسم `transport` (وسيلة نقل الشبكة، MeshTransport). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:34]

```
35:     private val encryptionService: EncryptionService,
```
> معامِل بانٍ خاصّ غير قابل للتغيير باسم `encryptionService` من نوع `EncryptionService`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:35]

```
36:     val myPeerID: String,
```
> معامِل بانٍ عامّ غير قابل للتغيير باسم `myPeerID` (معرّف نِدّي الخاصّ) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:36]

```
37:     private val maxTtl: UByte,
```
> معامِل بانٍ خاصّ غير قابل للتغيير باسم `maxTtl` (أقصى مدّة بقاء، Time To Live) من نوع `UByte`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:37]

```
38:     sharedGossipManager: GossipSyncManager?,
```
> معامِل بانٍ باسم `sharedGossipManager` (مدير مزامنة إشاعة مشترَك) من نوع `GossipSyncManager` يقبل القيمة الفارغة (nullable). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:38]

```
39:     gossipConfigProvider: GossipSyncManager.ConfigProvider,
```
> معامِل بانٍ باسم `gossipConfigProvider` (مزوِّد إعدادات الإشاعة) من النوع المتداخِل `GossipSyncManager.ConfigProvider`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:39]

```
40:     private val hooks: Hooks = Hooks()
```
> معامِل بانٍ خاصّ غير قابل للتغيير باسم `hooks` (خطّافات) من نوع `Hooks` قيمته الافتراضية كائن `Hooks()` جديد. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:40]

```
41: ) {
```
> إغلاق قائمة معامِلات الباني وبداية جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:41]

```
42:     data class Hooks(
```
> يعرّف صنف بيانات (data class) باسم `Hooks` وبداية قائمة معامِلاته. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:42]

```
43:         val onMessageReceived: ((BitchatMessage) -> Unit)? = null,
```
> خاصّيّة `onMessageReceived` (عند استقبال رسالة) من نوع دالّة تأخذ `BitchatMessage` وتُعيد `Unit`، تقبل القيمة الفارغة وقيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:43]

```
44:         val onPeerIdBindingUpdated: ((String, String, ByteArray, String?) -> Unit)? = null,
```
> خاصّيّة `onPeerIdBindingUpdated` (عند تحديث ربط معرّف النِدّ) من نوع دالّة تأخذ `String` و`String` و`ByteArray` و`String` فارغًا اختياريًّا وتُعيد `Unit`، تقبل القيمة الفارغة وقيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:44]

```
45:         val onAnnounceProcessed: ((RoutedPacket, Boolean) -> Unit)? = null,
```
> خاصّيّة `onAnnounceProcessed` (عند معالجة الإعلان) من نوع دالّة تأخذ `RoutedPacket` و`Boolean` وتُعيد `Unit`، تقبل القيمة الفارغة وقيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:45]

```
46:         val readReceiptInterceptor: ((String, String) -> Boolean)? = null,
```
> خاصّيّة `readReceiptInterceptor` (مُعترِض إيصال القراءة) من نوع دالّة تأخذ `String` و`String` وتُعيد `Boolean`، تقبل القيمة الفارغة وقيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:46]

```
47:         val onReadReceiptSent: ((String) -> Unit)? = null,
```
> خاصّيّة `onReadReceiptSent` (عند إرسال إيصال القراءة) من نوع دالّة تأخذ `String` وتُعيد `Unit`، تقبل القيمة الفارغة وقيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:47]

```
48:         val announcementNicknameProvider: (() -> String?)? = null,
```
> خاصّيّة `announcementNicknameProvider` (مزوِّد اسم مستعار للإعلان) من نوع دالّة بلا معامِلات تُعيد `String` فارغًا اختياريًّا، تقبل القيمة الفارغة وقيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:48]

```
49:         val leavePayloadProvider: (() -> ByteArray)? = null
```
> خاصّيّة `leavePayloadProvider` (مزوِّد حمولة المغادرة) من نوع دالّة بلا معامِلات تُعيد `ByteArray`، تقبل القيمة الفارغة وقيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:49]

```
50:     )
```
> إغلاق قائمة معامِلات صنف البيانات `Hooks`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:50]

```
51: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:51]

```
52:     private val peerManager = PeerManager()
```
> يعرّف خاصّيّة خاصّة غير قابلة للتغيير باسم `peerManager` (مدير الأنداد) ويُسنِد إليها كائن `PeerManager()` جديدًا. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:52]

```
53:     val fragmentManager = FragmentManager()
```
> يعرّف خاصّيّة عامّة غير قابلة للتغيير باسم `fragmentManager` (مدير الشظايا) ويُسنِد إليها كائن `FragmentManager()` جديدًا. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:53]

```
54:     private val securityManager = SecurityManager(encryptionService, myPeerID)
```
> يعرّف خاصّيّة خاصّة غير قابلة للتغيير باسم `securityManager` (مدير الأمان) ويُسنِد إليها كائن `SecurityManager` مبنيًّا بالمعامِلين `encryptionService` و`myPeerID`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:54]

```
55:     private val storeForwardManager = StoreForwardManager()
```
> يعرّف خاصّيّة خاصّة غير قابلة للتغيير باسم `storeForwardManager` (مدير التخزين وإعادة التوجيه) ويُسنِد إليها كائن `StoreForwardManager()` جديدًا. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:55]

```
56:     private val messageHandler = MessageHandler(myPeerID, context.applicationContext)
```
> يعرّف خاصّيّة خاصّة غير قابلة للتغيير باسم `messageHandler` (معالِج الرسائل) ويُسنِد إليها كائن `MessageHandler` مبنيًّا بالمعامِلين `myPeerID` و`context.applicationContext`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:56]

```
57:     private val packetProcessor = PacketProcessor(myPeerID)
```
> يعرّف خاصّيّة خاصّة غير قابلة للتغيير باسم `packetProcessor` (مُعالِج الحُزَم) ويُسنِد إليها كائن `PacketProcessor` مبنيًّا بالمعامِل `myPeerID`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:57]

```
58:     private val directPeers = ConcurrentHashMap.newKeySet<String>()
```
> يعرّف خاصّيّة خاصّة غير قابلة للتغيير باسم `directPeers` (الأنداد المباشرون) ويُسنِد إليها مجموعة مفاتيح متزامنة من النوع `String` عبر `ConcurrentHashMap.newKeySet`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:58]

```
59: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:59]

```
60:     val gossipSyncManager: GossipSyncManager =
```
> يعرّف خاصّيّة عامّة غير قابلة للتغيير باسم `gossipSyncManager` من نوع `GossipSyncManager` وبداية تعبير الإسناد على السطر التالي. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:60]

```
61:         sharedGossipManager ?: GossipSyncManager(myPeerID = myPeerID, scope = scope, configProvider = gossipConfigProvider)
```
> يُسنِد `sharedGossipManager` إن لم يكن فارغًا، وإلّا يبني كائن `GossipSyncManager` جديدًا بالمعامِلات المُسمّاة `myPeerID` و`scope` و`configProvider`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:61]

```
62:     private val ownsGossipManager: Boolean = sharedGossipManager == null
```
> يعرّف خاصّيّة خاصّة غير قابلة للتغيير باسم `ownsGossipManager` (يملك مدير الإشاعة) من نوع `Boolean` قيمتها نتيجة المقارنة `sharedGossipManager == null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:62]

```
63: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:63]

```
64:     var delegate: MeshDelegate? = null
```
> يعرّف خاصّيّة عامّة قابلة للتغيير باسم `delegate` (مفوَّض) من نوع `MeshDelegate` تقبل القيمة الفارغة وقيمتها الابتدائية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:65]

```
66:     private var announceJob: Job? = null
```
> يعرّف خاصّيّة خاصّة قابلة للتغيير باسم `announceJob` (مهمّة الإعلان) من نوع `Job` تقبل القيمة الفارغة وقيمتها الابتدائية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:66]

```
67:     private var isActive = false
```
> يعرّف خاصّيّة خاصّة قابلة للتغيير باسم `isActive` (هل هو فعّال) قيمتها الابتدائية `false`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:67]

```
68: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:68]

```
69:     init {
```
> بداية كتلة التهيئة (init) للصنف. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:69]

```
70:         messageHandler.packetProcessor = packetProcessor
```
> يُسنِد `packetProcessor` إلى خاصّيّة `packetProcessor` في `messageHandler`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:70]

```
71:         peerManager.isPeerDirectlyConnected = { peerID -> directPeers.contains(peerID) }
```
> يُسنِد إلى خاصّيّة `isPeerDirectlyConnected` في `peerManager` دالّة لمدا تأخذ `peerID` وتُعيد ما إذا كانت مجموعة `directPeers` تحتويه. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:71]

```
72:         setupDelegates()
```
> يستدعي الدالّة `setupDelegates` (تهيئة المفوَّضين). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:72]

```
73: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:73]

```
74:         if (sharedGossipManager == null) {
```
> شرط: إذا كان `sharedGossipManager` يساوي `null` فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:74]

```
75:             gossipSyncManager.delegate = object : GossipSyncManager.Delegate {
```
> يُسنِد إلى خاصّيّة `delegate` في `gossipSyncManager` كائنًا مجهولًا (object) يحقّق الواجهة `GossipSyncManager.Delegate`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:75]

```
76:                 override fun sendPacket(packet: BitchatPacket) {
```
> يتجاوز (override) الدالّة `sendPacket` التي تأخذ معامِلًا `packet` من نوع `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:76]

```
77:                     dispatchGlobal(RoutedPacket(packet))
```
> يستدعي `dispatchGlobal` ممرِّرًا كائن `RoutedPacket` مبنيًّا من `packet`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:77]

```
78:                 }
```
> إغلاق نطاق الدالّة `sendPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:78]

```
79: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:79]

```
80:                 override fun sendPacketToPeer(peerID: String, packet: BitchatPacket) {
```
> يتجاوز الدالّة `sendPacketToPeer` التي تأخذ `peerID` من نوع `String` و`packet` من نوع `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:80]

```
81:                     transport.sendPacketToPeer(peerID, packet)
```
> يستدعي `transport.sendPacketToPeer` ممرِّرًا `peerID` و`packet`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:81]

```
82:                     TransportBridgeService.sendToPeer(transport.id, peerID, packet)
```
> يستدعي `TransportBridgeService.sendToPeer` ممرِّرًا `transport.id` و`peerID` و`packet`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:82]

```
83:                 }
```
> إغلاق نطاق الدالّة `sendPacketToPeer`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:83]

```
84: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:84]

```
85:                 override fun signPacketForBroadcast(packet: BitchatPacket): BitchatPacket {
```
> يتجاوز الدالّة `signPacketForBroadcast` التي تأخذ `packet` من نوع `BitchatPacket` وتُعيد `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:85]

```
86:                     return signPacketBeforeBroadcast(packet)
```
> يُعيد ناتج استدعاء `signPacketBeforeBroadcast` على `packet`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:86]

```
87:                 }
```
> إغلاق نطاق الدالّة `signPacketForBroadcast`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:87]

```
88:             }
```
> إغلاق نطاق الكائن المجهول المحقِّق لواجهة `GossipSyncManager.Delegate`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:88]

```
89:         }
```
> إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:89]

```
90:     }
```
> إغلاق نطاق كتلة التهيئة `init`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:90]

```
91: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:91]

```
92:     fun startCore() {
```
> يعرّف الدالّة العامّة `startCore` (تشغيل النواة) بلا معامِلات. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:92]

```
93:         if (isActive) return
```
> إذا كانت `isActive` صحيحة فاخرُج من الدالّة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:93]

```
94:         isActive = true
```
> يُسنِد القيمة `true` إلى `isActive`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:94]

```
95:         startPeriodicBroadcastAnnounce()
```
> يستدعي الدالّة `startPeriodicBroadcastAnnounce` (بدء الإعلان الدوري بالبثّ). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:95]

```
96:         if (ownsGossipManager) {
```
> شرط: إذا كانت `ownsGossipManager` صحيحة فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:96]

```
97:             gossipSyncManager.start()
```
> يستدعي `gossipSyncManager.start` (بدء مدير مزامنة الإشاعة). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:97]

```
98:         }
```
> إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:98]

```
99:     }
```
> إغلاق نطاق الدالّة `startCore`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:99]

```
100: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:100]

```
101:     fun stopCore() {
```
> يعرّف الدالّة العامّة `stopCore` (إيقاف النواة) بلا معامِلات. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:101]

```
102:         if (!isActive) return
```
> إذا لم تكن `isActive` صحيحة فاخرُج من الدالّة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:102]

```
103:         isActive = false
```
> يُسنِد القيمة `false` إلى `isActive`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:103]

```
104:         announceJob?.cancel()
```
> يستدعي `cancel` على `announceJob` إن لم يكن فارغًا (إلغاء مهمّة الإعلان). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:104]

```
105:         announceJob = null
```
> يُسنِد القيمة `null` إلى `announceJob`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:105]

```
106:         if (ownsGossipManager) {
```
> شرط: إذا كانت `ownsGossipManager` صحيحة فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:106]

```
107:             gossipSyncManager.stop()
```
> يستدعي `gossipSyncManager.stop` (إيقاف مدير مزامنة الإشاعة). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:107]

```
108:         }
```
> إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:108]

```
109:     }
```
> إغلاق نطاق الدالّة `stopCore`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:109]

```
110: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:110]

```
111:     fun shutdown() {
```
> يعرّف الدالّة العامّة `shutdown` (إيقاف تامّ) بلا معامِلات. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:111]

```
112:         peerManager.shutdown()
```
> يستدعي `peerManager.shutdown` (إيقاف مدير الأنداد). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:112]

```
113:         fragmentManager.shutdown()
```
> يستدعي `fragmentManager.shutdown` (إيقاف مدير الشظايا). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:113]

```
114:         securityManager.shutdown()
```
> يستدعي `securityManager.shutdown` (إيقاف مدير الأمان). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:114]

```
115:         storeForwardManager.shutdown()
```
> يستدعي `storeForwardManager.shutdown` (إيقاف مدير التخزين وإعادة التوجيه). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:115]

```
116:         messageHandler.shutdown()
```
> يستدعي `messageHandler.shutdown` (إيقاف معالِج الرسائل). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:116]

```
117:         packetProcessor.shutdown()
```
> يستدعي `packetProcessor.shutdown` (إيقاف مُعالِج الحُزَم). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:117]

```
118:     }
```
> إغلاق نطاق الدالّة `shutdown`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:118]

```
119: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:119]

```
120:     fun processIncoming(packet: BitchatPacket, peerID: String?, relayAddress: String?) {
```
> يعرّف الدالّة العامّة `processIncoming` (معالجة الوارد) بمعامِلات `packet` من نوع `BitchatPacket` و`peerID` و`relayAddress` كنصّين يقبلان القيمة الفارغة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:120]

```
121:         packetProcessor.processPacket(RoutedPacket(packet, peerID, relayAddress))
```
> يستدعي `packetProcessor.processPacket` ممرِّرًا كائن `RoutedPacket` مبنيًّا من `packet` و`peerID` و`relayAddress`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:121]

```
122:     }
```
> إغلاق نطاق الدالّة `processIncoming`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:122]

```
123: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:123]

```
124:     fun sendFromBridge(packet: RoutedPacket) {
```
> يعرّف الدالّة العامّة `sendFromBridge` (الإرسال من الجسر) بمعامِل `packet` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:124]

```
125:         transport.broadcastPacket(packet)
```
> يستدعي `transport.broadcastPacket` ممرِّرًا `packet`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:125]

```
126:     }
```
> إغلاق نطاق الدالّة `sendFromBridge`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:126]

```
127: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:127]

```
128:     private fun dispatchGlobal(routed: RoutedPacket) {
```
> يعرّف الدالّة الخاصّة `dispatchGlobal` (التوزيع العامّ) بمعامِل `routed` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:128]

```
129:         transport.broadcastPacket(routed)
```
> يستدعي `transport.broadcastPacket` ممرِّرًا `routed`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:129]

```
130:         TransportBridgeService.broadcast(transport.id, routed)
```
> يستدعي `TransportBridgeService.broadcast` ممرِّرًا `transport.id` و`routed`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:130]

```
131:     }
```
> إغلاق نطاق الدالّة `dispatchGlobal`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:131]

```
132: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:132]

```
133:     private fun startPeriodicBroadcastAnnounce() {
```
> يعرّف الدالّة الخاصّة `startPeriodicBroadcastAnnounce` (بدء الإعلان الدوري بالبثّ) بلا معامِلات. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:133]

```
134:         announceJob?.cancel()
```
> يستدعي `cancel` على `announceJob` إن لم يكن فارغًا. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:134]

```
135:         announceJob = scope.launch {
```
> يُسنِد إلى `announceJob` نتيجة `scope.launch` التي تُطلِق كوروتين جديدًا، وبداية جسمه. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:135]

```
136:             while (isActive) {
```
> حلقة `while` تتكرّر ما دامت `isActive` صحيحة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:136]

```
137:                 try {
```
> بداية كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:137]

```
138:                     delay(30_000)
```
> يستدعي `delay` بقيمة ٣٠٬٠٠٠ (ملّي ثانية أي ثلاثون ثانية تأخيرًا). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:138]

```
139:                     sendBroadcastAnnounce()
```
> يستدعي الدالّة `sendBroadcastAnnounce` (إرسال إعلان البثّ). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:139]

```
140:                 } catch (_: Exception) { }
```
> كتلة `catch` تلتقط أيّ `Exception` بمعامِل مهمَل وجسمها فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:140]

```
141:             }
```
> إغلاق نطاق حلقة `while`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:141]

```
142:         }
```
> إغلاق نطاق كوروتين `scope.launch`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:142]

```
143:     }
```
> إغلاق نطاق الدالّة `startPeriodicBroadcastAnnounce`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:143]

```
144: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:144]

```
145:     private fun setupDelegates() {
```
> يعرّف الدالّة الخاصّة `setupDelegates` (تهيئة المفوَّضين) بلا معامِلات. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:145]

```
146:         peerManager.delegate = object : PeerManagerDelegate {
```
> يُسنِد إلى خاصّيّة `delegate` في `peerManager` كائنًا مجهولًا يحقّق الواجهة `PeerManagerDelegate`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:146]

```
147:             override fun onPeerListUpdated(peerIDs: List<String>) {
```
> يتجاوز الدالّة `onPeerListUpdated` (عند تحديث قائمة الأنداد) التي تأخذ `peerIDs` من نوع `List<String>`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:147]

```
148:                 try { com.bitchat.android.services.AppStateStore.setTransportPeers(transport.id, peerIDs) } catch (_: Exception) { }
```
> يحاول استدعاء `AppStateStore.setTransportPeers` ممرِّرًا `transport.id` و`peerIDs`، ويلتقط أيّ `Exception` بجسم فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:148]

```
149:                 delegate?.didUpdatePeerList(peerIDs)
```
> يستدعي `didUpdatePeerList` على `delegate` إن لم يكن فارغًا ممرِّرًا `peerIDs`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:149]

```
150:             }
```
> إغلاق نطاق الدالّة `onPeerListUpdated`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:150]

```
151: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:151]

```
152:             override fun onPeerRemoved(peerID: String) {
```
> يتجاوز الدالّة `onPeerRemoved` (عند إزالة نِدّ) التي تأخذ `peerID` من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:152]

```
153:                 try { gossipSyncManager.removeAnnouncementForPeer(peerID) } catch (_: Exception) { }
```
> يحاول استدعاء `gossipSyncManager.removeAnnouncementForPeer` ممرِّرًا `peerID`، ويلتقط أيّ `Exception` بجسم فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:153]

```
154:                 try { encryptionService.removePeer(peerID) } catch (_: Exception) { }
```
> يحاول استدعاء `encryptionService.removePeer` ممرِّرًا `peerID`، ويلتقط أيّ `Exception` بجسم فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:154]

```
155:                 try { peerManager.refreshPeerList() } catch (_: Exception) { }
```
> يحاول استدعاء `peerManager.refreshPeerList` (تحديث قائمة الأنداد)، ويلتقط أيّ `Exception` بجسم فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:155]

```
156:             }
```
> إغلاق نطاق الدالّة `onPeerRemoved`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:156]

```
157:         }
```
> إغلاق نطاق الكائن المجهول المحقِّق لواجهة `PeerManagerDelegate`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:157]

```
158: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:158]

```
159:         securityManager.delegate = object : SecurityManagerDelegate {
```
> يُسنِد إلى خاصّيّة `delegate` في `securityManager` كائنًا مجهولًا يحقّق الواجهة `SecurityManagerDelegate`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:159]

```
160:             override fun onKeyExchangeCompleted(peerID: String, peerPublicKeyData: ByteArray) {
```
> يتجاوز الدالّة `onKeyExchangeCompleted` (عند اكتمال تبادل المفاتيح) التي تأخذ `peerID` من نوع `String` و`peerPublicKeyData` من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:160]

```
161:                 scope.launch {
```
> يستدعي `scope.launch` لإطلاق كوروتين جديد، وبداية جسمه. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:161]

```
162:                     delay(100)
```
> يستدعي `delay` بقيمة ١٠٠ (ملّي ثانية تأخيرًا). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:162]

```
163:                     sendAnnouncementToPeer(peerID)
```
> يستدعي الدالّة `sendAnnouncementToPeer` (إرسال الإعلان إلى النِدّ) ممرِّرًا `peerID`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:163]

```
164:                     delay(1000)
```
> يستدعي `delay` بقيمة ١٠٠٠ (ملّي ثانية أي ثانية واحدة تأخيرًا). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:164]

```
165:                     storeForwardManager.sendCachedMessages(peerID)
```
> يستدعي `storeForwardManager.sendCachedMessages` (إرسال الرسائل المخزَّنة) ممرِّرًا `peerID`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:165]

```
166:                 }
```
> إغلاق نطاق كوروتين `scope.launch`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:166]

```
167:             }
```
> إغلاق نطاق الدالّة `onKeyExchangeCompleted`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:167]

```
168: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:168]

```
169:             override fun sendHandshakeResponse(peerID: String, response: ByteArray) {
```
> يتجاوز الدالّة `sendHandshakeResponse` (إرسال ردّ المصافحة) التي تأخذ `peerID` من نوع `String` و`response` من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:169]

```
170:                 val responsePacket = BitchatPacket(
```
> يعرّف متغيّرًا محلّيًّا غير قابل للتغيير باسم `responsePacket` ويبدأ بناء كائن `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:170]

```
171:                     version = 1u,
```
> يُسنِد للمعامِل المُسمّى `version` القيمة `1u` (واحد بلا إشارة). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:171]

```
172:                     type = MessageType.NOISE_HANDSHAKE.value,
```
> يُسنِد للمعامِل المُسمّى `type` قيمة `MessageType.NOISE_HANDSHAKE.value` (قيمة نوع مصافحة نويز). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:172]

```
173:                     senderID = MeshPacketUtils.hexStringToByteArray(myPeerID),
```
> يُسنِد للمعامِل المُسمّى `senderID` ناتج `MeshPacketUtils.hexStringToByteArray` على `myPeerID` (تحويل نصّ ستّ عشري إلى مصفوفة بايتات). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:173]

```
174:                     recipientID = MeshPacketUtils.hexStringToByteArray(peerID),
```
> يُسنِد للمعامِل المُسمّى `recipientID` ناتج `MeshPacketUtils.hexStringToByteArray` على `peerID`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:174]

```
175:                     timestamp = System.currentTimeMillis().toULong(),
```
> يُسنِد للمعامِل المُسمّى `timestamp` الوقت الحالي بالملّي ثانية من `System.currentTimeMillis` محوَّلًا إلى `ULong`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:175]

```
176:                     payload = response,
```
> يُسنِد للمعامِل المُسمّى `payload` القيمة `response`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:176]

```
177:                     ttl = maxTtl
```
> يُسنِد للمعامِل المُسمّى `ttl` القيمة `maxTtl` (أقصى مدّة بقاء). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:177]

```
178:                 )
```
> إغلاق قائمة معامِلات بناء كائن `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:178]

```
179:                 dispatchGlobal(RoutedPacket(signPacketBeforeBroadcast(responsePacket)))
```
> يستدعي `dispatchGlobal` ممرِّرًا كائن `RoutedPacket` مبنيًّا من ناتج `signPacketBeforeBroadcast` على `responsePacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:179]

```
180:             }
```
> إغلاق نطاق الدالّة `sendHandshakeResponse`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:180]

```
181: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:181]

```
182:             override fun getPeerInfo(peerID: String): PeerInfo? = peerManager.getPeerInfo(peerID)
```
> يتجاوز الدالّة `getPeerInfo` (جلب معلومات النِدّ) التي تأخذ `peerID` من نوع `String` وتُعيد `PeerInfo` فارغًا اختياريًّا بإسناد ناتج `peerManager.getPeerInfo(peerID)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:182]

```
183:         }
```
> إغلاق نطاق الكائن المجهول المحقِّق لواجهة `SecurityManagerDelegate`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:183]

```
184: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:184]

```
185:         storeForwardManager.delegate = object : StoreForwardManagerDelegate {
```
> يُسنِد إلى خاصّيّة `delegate` في `storeForwardManager` كائنًا مجهولًا يحقّق الواجهة `StoreForwardManagerDelegate`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:185]

```
186:             override fun isFavorite(peerID: String): Boolean {
```
> يتجاوز الدالّة `isFavorite` (هل هو مفضَّل) التي تأخذ `peerID` من نوع `String` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:186]

```
187:                 return delegate?.isFavorite(peerID) ?: false
```
> يُعيد ناتج `isFavorite(peerID)` على `delegate` إن لم يكن فارغًا، وإلّا `false`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:187]

```
188:             }
```
> إغلاق نطاق الدالّة `isFavorite`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:188]

```
189: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:189]

```
190:             override fun isPeerOnline(peerID: String): Boolean {
```
> يتجاوز الدالّة `isPeerOnline` (هل النِدّ متّصل) التي تأخذ `peerID` من نوع `String` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:190]

```
191:                 return peerManager.isPeerActive(peerID)
```
> يُعيد ناتج `peerManager.isPeerActive(peerID)` (هل النِدّ فعّال). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:191]

```
192:             }
```
> إغلاق نطاق الدالّة `isPeerOnline`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:192]

```
193: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:193]

```
194:             override fun sendPacket(packet: BitchatPacket) {
```
> يتجاوز الدالّة `sendPacket` (إرسال حُزمة) التي تأخذ `packet` من نوع `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:194]

```
195:                 dispatchGlobal(RoutedPacket(packet))
```
> يستدعي `dispatchGlobal` ممرِّرًا كائن `RoutedPacket` مبنيًّا من `packet`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:195]

```
196:             }
```
> إغلاق نطاق الدالّة `sendPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:196]

```
197:         }
```
> إغلاق نطاق الكائن المجهول المحقِّق لواجهة `StoreForwardManagerDelegate`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:197]

```
198: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:198]

```
199:         messageHandler.delegate = object : MessageHandlerDelegate {
```
> يُسنِد إلى خاصّيّة `delegate` في `messageHandler` كائنًا مجهولًا يحقّق الواجهة `MessageHandlerDelegate`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:199]

```
200:             override fun addOrUpdatePeer(peerID: String, nickname: String): Boolean {
```
> يتجاوز الدالّة `addOrUpdatePeer` (إضافة نِدّ أو تحديثه) التي تأخذ `peerID` من نوع `String` و`nickname` من نوع `String` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:200]
