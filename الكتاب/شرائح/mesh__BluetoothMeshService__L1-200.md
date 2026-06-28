# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف Context من حزمة android.content. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف Log من حزمة android.util. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:4]

```
5: import com.bitchat.android.crypto.EncryptionService
```
> يستورد خدمة التشفير (EncryptionService) من حزمة com.bitchat.android.crypto. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:5]

```
6: import com.bitchat.android.model.BitchatMessage
```
> يستورد رسالة بِتشات (BitchatMessage) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:6]

```
7: import com.bitchat.android.protocol.MessagePadding
```
> يستورد حشو الرسالة (MessagePadding) من حزمة com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:7]

```
8: import com.bitchat.android.model.RoutedPacket
```
> يستورد الحزمة الموجَّهة (RoutedPacket) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:8]

```
9: import com.bitchat.android.model.IdentityAnnouncement
```
> يستورد إعلان الهوية (IdentityAnnouncement) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:9]

```
10: import com.bitchat.android.model.NoisePayload
```
> يستورد حمولة نويز (NoisePayload) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:10]

```
11: import com.bitchat.android.model.NoisePayloadType
```
> يستورد نوع حمولة نويز (NoisePayloadType) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:11]

```
12: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد حزمة بِتشات (BitchatPacket) من حزمة com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:12]

```
13: import com.bitchat.android.protocol.MessageType
```
> يستورد نوع الرسالة (MessageType) من حزمة com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:13]

```
14: import com.bitchat.android.protocol.SpecialRecipients
```
> يستورد المستلِمين الخاصّين (SpecialRecipients) من حزمة com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:14]

```
15: import com.bitchat.android.model.RequestSyncPacket
```
> يستورد حزمة طلب المزامنة (RequestSyncPacket) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:15]

```
16: import com.bitchat.android.sync.GossipSyncManager
```
> يستورد مدير مزامنة الإشاعة (GossipSyncManager) من حزمة com.bitchat.android.sync. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:16]

```
17: import com.bitchat.android.util.toHexString
```
> يستورد الدالة toHexString من حزمة com.bitchat.android.util. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:17]

```
18: import com.bitchat.android.services.VerificationService
```
> يستورد خدمة التحقّق (VerificationService) من حزمة com.bitchat.android.services. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:18]

```
19: import com.bitchat.android.service.TransportBridgeService
```
> يستورد خدمة جسر النقل (TransportBridgeService) من حزمة com.bitchat.android.service. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:19]

```
20: import kotlinx.coroutines.*
```
> يستورد كل العناصر العامّة من حزمة kotlinx.coroutines (الكوروتينات). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:20]

```
21: import java.util.*
```
> يستورد كل العناصر العامّة من حزمة java.util. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:21]

```
22: import kotlin.math.sign
```
> يستورد الدالة sign من حزمة kotlin.math. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:22]

```
23: import kotlin.random.Random
```
> يستورد الصنف Random من حزمة kotlin.random. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:24]

```
25: /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:25]

```
26:  * Bluetooth mesh service - REFACTORED to use component-based architecture
```
> تعليق: «خدمة شبكة بلوتوث المتشابكة - أُعيدت هيكلتها لاستخدام معمارية قائمة على المكوّنات». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:26]

```
27:  * 100% compatible with iOS version and maintains exact same UUIDs, packet format, and protocol logic
```
> تعليق: «متوافقة ١٠٠٪ مع نسخة iOS وتحافظ على نفس مُعرّفات UUID وصيغة الحزمة ومنطق البروتوكول بالضبط». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:27]

```
28:  * 
```
> تعليق: سطر فارغ داخل تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:28]

```
29:  * This is now a coordinator that orchestrates the following components:
```
> تعليق: «هذا الآن منسّق (coordinator) يُنظّم المكوّنات التالية:». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:29]

```
30:  * - PeerManager: Peer lifecycle management
```
> تعليق: «- PeerManager: إدارة دورة حياة النظير». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:30]

```
31:  * - FragmentManager: Message fragmentation and reassembly  
```
> تعليق: «- FragmentManager: تجزئة الرسالة وإعادة تجميعها». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:31]

```
32:  * - SecurityManager: Security, duplicate detection, encryption
```
> تعليق: «- SecurityManager: الأمان، وكشف التكرار، والتشفير». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:32]

```
33:  * - StoreForwardManager: Offline message caching
```
> تعليق: «- StoreForwardManager: تخزين الرسائل غير المتّصلة مؤقّتاً». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:33]

```
34:  * - MessageHandler: Message type processing and relay logic
```
> تعليق: «- MessageHandler: معالجة نوع الرسالة ومنطق الترحيل». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:34]

```
35:  * - BluetoothConnectionManager: BLE connections and GATT operations
```
> تعليق: «- BluetoothConnectionManager: اتصالات BLE وعمليات GATT». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:35]

```
36:  * - PacketProcessor: Incoming packet routing
```
> تعليق: «- PacketProcessor: توجيه الحزم الواردة». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:36]

```
37:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:37]

```
38: class BluetoothMeshService(private val context: Context) : TransportBridgeService.TransportLayer {
```
> يُعرّف الصنف خدمة شبكة بلوتوث المتشابكة (BluetoothMeshService) بمُنشئ يأخذ مُعاملاً خاصّاً للقراءة فقط باسم context من النوع Context، ويُنفّذ الواجهة TransportBridgeService.TransportLayer (طبقة النقل). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:38]

```
39:     private val debugManager by lazy { try { com.bitchat.android.ui.debug.DebugSettingsManager.getInstance() } catch (e: Exception) { null } }
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم مدير التنقيح (debugManager) تُهيَّأ بكسلٍ (lazy)، وقيمتها ناتج استدعاء getInstance على DebugSettingsManager داخل محاولة، وفي حال وقوع استثناء تعيد null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:39]

```
40:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:40]

```
41:     companion object {
```
> يبدأ كائناً مرافقاً (companion object) للصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:41]

```
42:         private const val TAG = "BluetoothMeshService"
```
> يُعرّف ثابتاً خاصّاً باسم TAG قيمته السلسلة النصّية "BluetoothMeshService". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:42]

```
43:         private val MAX_TTL: UByte = com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم MAX_TTL من النوع UByte (بايت غير مُوقّع) قيمتها AppConstants.MESSAGE_TTL_HOPS. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:43]

```
44:     }
```
> إغلاق نطاق (الكائن المرافق). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:44]

```
45:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:45]

```
46:     // Core components - each handling specific responsibilities
```
> تعليق: «المكوّنات الأساسية - كلٌّ يتولّى مسؤوليات محدّدة». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:46]

```
47:     private val encryptionService = EncryptionService(context)
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم خدمة التشفير (encryptionService) قيمتها كائن جديد من EncryptionService يأخذ context. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:47]

```
48: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:48]

```
49:     // My peer identification - derived from persisted Noise identity fingerprint (first 16 hex chars)
```
> تعليق: «مُعرّف نظيري - مُشتقّ من بصمة هوية نويز المحفوظة (أول ١٦ حرفاً ستّ عشريّاً)». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:49]

```
50:     val myPeerID: String = encryptionService.getIdentityFingerprint().take(16)
```
> يُعرّف خاصّية للقراءة فقط باسم مُعرّف نظيري (myPeerID) من النوع String قيمتها أول ١٦ حرفاً من ناتج getIdentityFingerprint على encryptionService. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:50]

```
51:     private val peerManager = PeerManager()
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم مدير النظراء (peerManager) قيمتها كائن جديد من PeerManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:51]

```
52:     private val fragmentManager = FragmentManager()
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم مدير الأجزاء (fragmentManager) قيمتها كائن جديد من FragmentManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:52]

```
53:     private val securityManager = SecurityManager(encryptionService, myPeerID)
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم مدير الأمان (securityManager) قيمتها كائن جديد من SecurityManager يأخذ encryptionService و myPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:53]

```
54:     private val storeForwardManager = StoreForwardManager()
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم مدير التخزين والإرسال (storeForwardManager) قيمتها كائن جديد من StoreForwardManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:54]

```
55:     private val messageHandler = MessageHandler(myPeerID, context.applicationContext)
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم معالج الرسائل (messageHandler) قيمتها كائن جديد من MessageHandler يأخذ myPeerID و context.applicationContext. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:55]

```
56:     internal val connectionManager = BluetoothConnectionManager(context, myPeerID, fragmentManager) // Made internal for access
```
> يُعرّف خاصّية داخلية (internal) للقراءة فقط باسم مدير الاتصال (connectionManager) قيمتها كائن جديد من BluetoothConnectionManager يأخذ context و myPeerID و fragmentManager، مع تعليق: «جُعلت داخلية لإتاحة الوصول». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:56]

```
57:     private val packetProcessor = PacketProcessor(myPeerID)
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم معالج الحزم (packetProcessor) قيمتها كائن جديد من PacketProcessor يأخذ myPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:57]

```
58:     private lateinit var gossipSyncManager: GossipSyncManager
```
> يُعرّف خاصّية خاصّة قابلة للتغيير باسم مدير مزامنة الإشاعة (gossipSyncManager) من النوع GossipSyncManager مع تأجيل التهيئة (lateinit). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:58]

```
59:     // Service-level notification manager for background (no-UI) DMs
```
> تعليق: «مدير إشعارات على مستوى الخدمة للرسائل المباشرة في الخلفية (بلا واجهة)». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:59]

```
60:     private val serviceNotificationManager = com.bitchat.android.ui.NotificationManager(
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم مدير إشعارات الخدمة (serviceNotificationManager) قيمتها كائن جديد من NotificationManager، وتبدأ قائمة الوُسطاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:60]

```
61:         context.applicationContext,
```
> يُمرّر context.applicationContext كوسيط أوّل للمُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:61]

```
62:         androidx.core.app.NotificationManagerCompat.from(context.applicationContext),
```
> يُمرّر ناتج NotificationManagerCompat.from لـ context.applicationContext كوسيط ثانٍ للمُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:62]

```
63:         com.bitchat.android.util.NotificationIntervalManager()
```
> يُمرّر كائناً جديداً من NotificationIntervalManager (مدير فترات الإشعار) كوسيط ثالث للمُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:63]

```
64:     )
```
> إغلاق نطاق (قائمة وُسطاء مُنشئ مدير إشعارات الخدمة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:64]

```
65:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:65]

```
66:     // Service state management
```
> تعليق: «إدارة حالة الخدمة». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:66]

```
67:     private var isActive = false
```
> يُعرّف خاصّية خاصّة قابلة للتغيير باسم نشط (isActive) قيمتها الابتدائية false. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:67]

```
68:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:68]

```
69:     // Delegate for message callbacks (maintains same interface)
```
> تعليق: «مُفوَّض لاستدعاءات الرسائل العائدة (يحافظ على نفس الواجهة)». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:69]

```
70:     var delegate: BluetoothMeshDelegate? = null
```
> يُعرّف خاصّية قابلة للتغيير باسم مُفوَّض (delegate) من النوع BluetoothMeshDelegate القابل لأن يكون null، قيمتها الابتدائية null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:70]

```
71:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:71]

```
72:     // Coroutines
```
> تعليق: «الكوروتينات». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:72]

```
73:     private val serviceScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يُعرّف خاصّية خاصّة للقراءة فقط باسم نطاق الخدمة (serviceScope) قيمتها CoroutineScope مُكوّن من مُوزِّع الإدخال/الإخراج Dispatchers.IO مضافاً إليه SupervisorJob. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:73]

```
74:     private var announceJob: Job? = null
```
> يُعرّف خاصّية خاصّة قابلة للتغيير باسم مهمّة الإعلان (announceJob) من النوع Job القابل لأن يكون null، قيمتها الابتدائية null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:74]

```
75:     // Tracks whether this instance has been terminated via stopServices()
```
> تعليق: «يتتبّع ما إذا كان هذا النسخة قد أُنهي عبر stopServices()». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:75]

```
76:     private var terminated = false
```
> يُعرّف خاصّية خاصّة قابلة للتغيير باسم مُنهَى (terminated) قيمتها الابتدائية false. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:76]

```
77:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:77]

```
78:     init {
```
> يبدأ كتلة التهيئة (init) للصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:78]

```
79:         Log.i(TAG, "Initializing BluetoothMeshService for peer=$myPeerID")
```
> يستدعي Log.i بالوسم TAG ورسالة معلومات نصّها "Initializing BluetoothMeshService for peer=" متبوعاً بقيمة myPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:79]

```
80:         VerificationService.configure(encryptionService)
```
> يستدعي configure على VerificationService مُمرّراً encryptionService. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:80]

```
81:         setupDelegates()
```
> يستدعي الدالة setupDelegates (تهيئة المُفوَّضين). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:81]

```
82:         messageHandler.packetProcessor = packetProcessor
```
> يُسنِد قيمة packetProcessor إلى الخاصّية packetProcessor في messageHandler. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:82]

```
83:         //startPeriodicDebugLogging()
```
> تعليق: استدعاء مُعطَّل لـ startPeriodicDebugLogging(). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:83]

```
84: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:84]

```
85:         // Initialize sync manager (needs serviceScope)
```
> تعليق: «تهيئة مدير المزامنة (يحتاج serviceScope)». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:85]

```
86:         gossipSyncManager = GossipSyncManager(
```
> يُسنِد إلى gossipSyncManager كائناً جديداً من GossipSyncManager، وتبدأ قائمة الوُسطاء المُسمّاة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:86]

```
87:             myPeerID = myPeerID,
```
> يُمرّر الوسيط المُسمّى myPeerID بقيمة الخاصّية myPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:87]

```
88:             scope = serviceScope,
```
> يُمرّر الوسيط المُسمّى scope بقيمة serviceScope. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:88]

```
89:             configProvider = object : GossipSyncManager.ConfigProvider {
```
> يُمرّر الوسيط المُسمّى configProvider بكائن مجهول (object) يُنفّذ الواجهة GossipSyncManager.ConfigProvider (مزوّد الإعدادات). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:89]

```
90:                 override fun seenCapacity(): Int = try {
```
> يُلغي ويُعرّف الدالة seenCapacity التي تُعيد Int، وقيمتها ناتج كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:90]

```
91:                     com.bitchat.android.ui.debug.DebugPreferenceManager.getSeenPacketCapacity(500)
```
> يستدعي getSeenPacketCapacity على DebugPreferenceManager مُمرّراً القيمة الافتراضية 500. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:91]

```
92:                 } catch (_: Exception) { 500 }
```
> يلتقط أي استثناء (باسم مُهمَل) ويُعيد القيمة 500. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:92]

```
93: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:93]

```
94:                 override fun gcsMaxBytes(): Int = try {
```
> يُلغي ويُعرّف الدالة gcsMaxBytes التي تُعيد Int، وقيمتها ناتج كتلة محاولة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:94]

```
95:                     com.bitchat.android.ui.debug.DebugPreferenceManager.getGcsMaxFilterBytes(400)
```
> يستدعي getGcsMaxFilterBytes على DebugPreferenceManager مُمرّراً القيمة الافتراضية 400. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:95]

```
96:                 } catch (_: Exception) { 400 }
```
> يلتقط أي استثناء (باسم مُهمَل) ويُعيد القيمة 400. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:96]

```
97: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:97]

```
98:                 override fun gcsTargetFpr(): Double = try {
```
> يُلغي ويُعرّف الدالة gcsTargetFpr التي تُعيد Double، وقيمتها ناتج كتلة محاولة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:98]

```
99:                     com.bitchat.android.ui.debug.DebugPreferenceManager.getGcsFprPercent(1.0) / 100.0
```
> يستدعي getGcsFprPercent على DebugPreferenceManager مُمرّراً القيمة 1.0 ثم يقسم الناتج على 100.0. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:99]

```
100:                 } catch (_: Exception) { 0.01 }
```
> يلتقط أي استثناء (باسم مُهمَل) ويُعيد القيمة 0.01. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:100]

```
101:             }
```
> إغلاق نطاق (الكائن المجهول المُنفّذ لـ ConfigProvider). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:101]

```
102:         )
```
> إغلاق نطاق (قائمة وُسطاء مُنشئ GossipSyncManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:102]

```
103: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:103]

```
104:         com.bitchat.android.service.MeshServiceHolder.setGossipManager(gossipSyncManager) { packet ->
```
> يستدعي setGossipManager على MeshServiceHolder مُمرّراً gossipSyncManager ولامبدا أخيرة وسيطها packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:104]

```
105:             signPacketBeforeBroadcast(packet)
```
> داخل اللامبدا يستدعي signPacketBeforeBroadcast (توقيع الحزمة قبل البثّ) مُمرّراً packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:105]

```
106:         }
```
> إغلاق نطاق (اللامبدا المُمرّرة لـ setGossipManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:106]

```
107:         if (isBleTransportEnabled()) {
```
> يبدأ شرط if يفحص ناتج الدالة isBleTransportEnabled (هل نقل BLE مُفعّل). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:107]

```
108:             TransportBridgeService.register("BLE", this)
```
> يستدعي register على TransportBridgeService مُمرّراً السلسلة "BLE" والكائن الحالي this. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:108]

```
109:         }
```
> إغلاق نطاق (شرط if). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:109]

```
110:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:110]

```
111:         // Inject dynamic direct connection check into PeerManager
```
> تعليق: «حقن فحص الاتصال المباشر الديناميكي داخل PeerManager». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:111]

```
112:         // Matches iOS logic: checks if we have an active hardware mapping for this peer
```
> تعليق: «يطابق منطق iOS: يفحص ما إذا كان لدينا تخطيط عتاد نشط لهذا النظير». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:112]

```
113:         peerManager.isPeerDirectlyConnected = { peerID ->
```
> يُسنِد إلى الخاصّية isPeerDirectlyConnected في peerManager لامبدا وسيطها peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:113]

```
114:             connectionManager.addressPeerMap.containsValue(peerID)
```
> داخل اللامبدا يُعيد ناتج containsValue على addressPeerMap في connectionManager للقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:114]

```
115:         }
```
> إغلاق نطاق (اللامبدا المُسنَدة لـ isPeerDirectlyConnected). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:115]

```
116:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:116]

```
117:         Log.d(TAG, "Delegates set up; GossipSyncManager initialized")
```
> يستدعي Log.d بالوسم TAG ورسالة تنقيح نصّها "Delegates set up; GossipSyncManager initialized". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:117]

```
118:     }
```
> إغلاق نطاق (كتلة init). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:118]

```
119: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:119]

```
120:     override fun send(packet: RoutedPacket) {
```
> يُلغي ويُعرّف الدالة send التي تأخذ مُعاملاً باسم packet من النوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:120]

```
121:         if (!isBleTransportEnabled()) return
```
> إن لم يكن نقل BLE مُفعّلاً يرجع فوراً (return). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:121]

```
122:         connectionManager.broadcastPacket(packet)
```
> يستدعي broadcastPacket على connectionManager مُمرّراً packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:122]

```
123:     }
```
> إغلاق نطاق (الدالة send). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:123]

```
124: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:124]

```
125:     override fun sendToPeer(peerID: String, packet: BitchatPacket) {
```
> يُلغي ويُعرّف الدالة sendToPeer التي تأخذ مُعاملاً باسم peerID من النوع String ومُعاملاً باسم packet من النوع BitchatPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:125]

```
126:         if (!isBleTransportEnabled()) return
```
> إن لم يكن نقل BLE مُفعّلاً يرجع فوراً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:126]

```
127:         connectionManager.sendPacketToPeer(peerID, packet)
```
> يستدعي sendPacketToPeer على connectionManager مُمرّراً peerID و packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:127]

```
128:     }
```
> إغلاق نطاق (الدالة sendToPeer). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:128]

```
129: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:129]

```
130:     private fun broadcastRoutedPacket(routed: RoutedPacket) {
```
> يُعرّف دالة خاصّة باسم broadcastRoutedPacket تأخذ مُعاملاً باسم routed من النوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:130]

```
131:         if (!isBleTransportEnabled()) return
```
> إن لم يكن نقل BLE مُفعّلاً يرجع فوراً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:131]

```
132:         connectionManager.broadcastPacket(routed)
```
> يستدعي broadcastPacket على connectionManager مُمرّراً routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:132]

```
133:         TransportBridgeService.broadcast("BLE", routed)
```
> يستدعي broadcast على TransportBridgeService مُمرّراً السلسلة "BLE" و routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:133]

```
134:     }
```
> إغلاق نطاق (الدالة broadcastRoutedPacket). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:134]

```
135: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:135]

```
136:     private fun isBleTransportEnabled(): Boolean {
```
> يُعرّف دالة خاصّة باسم isBleTransportEnabled تُعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:136]

```
137:         return try {
```
> يُعيد ناتج كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:137]

```
138:             com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().bleEnabled.value
```
> يقرأ الخاصّية value من bleEnabled على نسخة DebugSettingsManager المُعادة من getInstance. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:138]

```
139:         } catch (_: Exception) {
```
> يلتقط أي استثناء (باسم مُهمَل) ويبدأ كتلة معالجته. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:139]

```
140:             try { com.bitchat.android.ui.debug.DebugPreferenceManager.getBleEnabled(true) } catch (_: Exception) { true }
```
> داخل محاولة يستدعي getBleEnabled على DebugPreferenceManager بالقيمة الافتراضية true، وفي حال استثناء يُعيد true. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:140]

```
141:         }
```
> إغلاق نطاق (كتلة catch الخارجية). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:141]

```
142:     }
```
> إغلاق نطاق (الدالة isBleTransportEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:142]

```
143:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:143]

```
144:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:144]

```
145:      * Start periodic debug logging every 10 seconds
```
> تعليق: «بدء تسجيل تنقيح دوري كل ١٠ ثوانٍ». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:145]

```
146:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:146]

```
147:     private fun startPeriodicDebugLogging() {
```
> يُعرّف دالة خاصّة باسم startPeriodicDebugLogging (بدء التسجيل الدوري للتنقيح). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:147]

```
148:         serviceScope.launch {
```
> يُطلق كوروتين (launch) على serviceScope. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:148]

```
149:             Log.d(TAG, "Starting periodic debug logging loop")
```
> يستدعي Log.d بالوسم TAG ورسالة نصّها "Starting periodic debug logging loop". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:149]

```
150:             while (isActive) {
```
> يبدأ حلقة while تستمرّ ما دامت isActive صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:150]

```
151:                 try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:151]

```
152:                     delay(10000) // 10 seconds
```
> يُؤخّر التنفيذ 10000 ميلي ثانية مع تعليق: «١٠ ثوانٍ». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:152]

```
153:                     if (isActive) { // Double-check before logging
```
> يفحص شرط if قيمة isActive مع تعليق: «فحص مزدوج قبل التسجيل». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:153]

```
154:                         val debugInfo = getDebugStatus()
```
> يُعرّف متغيّراً محلّياً للقراءة فقط باسم معلومات التنقيح (debugInfo) قيمته ناتج getDebugStatus. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:154]

```
155:                         Log.d(TAG, "=== PERIODIC DEBUG STATUS ===\n$debugInfo\n=== END DEBUG STATUS ===")
```
> يستدعي Log.d بالوسم TAG ورسالة تحتوي "=== PERIODIC DEBUG STATUS ===" ثم سطراً جديداً وقيمة debugInfo ثم سطراً جديداً و"=== END DEBUG STATUS ===". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:155]

```
156:                     }
```
> إغلاق نطاق (شرط if). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:156]

```
157:                 } catch (e: Exception) {
```
> يلتقط استثناءً باسم e من النوع Exception ويبدأ كتلة معالجته. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:157]

```
158:                     Log.e(TAG, "Error in periodic debug logging: ${e.message}")
```
> يستدعي Log.e بالوسم TAG ورسالة خطأ نصّها "Error in periodic debug logging: " متبوعاً برسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:158]

```
159:                 }
```
> إغلاق نطاق (كتلة catch). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:159]

```
160:             }
```
> إغلاق نطاق (حلقة while). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:160]

```
161:             Log.d(TAG, "Periodic debug logging loop ended (isActive=$isActive)")
```
> يستدعي Log.d بالوسم TAG ورسالة نصّها "Periodic debug logging loop ended (isActive=" متبوعاً بقيمة isActive. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:161]

```
162:         }
```
> إغلاق نطاق (كوروتين launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:162]

```
163:     }
```
> إغلاق نطاق (الدالة startPeriodicDebugLogging). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:163]

```
164: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:164]

```
165:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:165]

```
166:      * Send broadcast announcement every 30 seconds
```
> تعليق: «إرسال إعلان بثّ كل ٣٠ ثانية». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:166]

```
167:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:167]

```
168:     private fun sendPeriodicBroadcastAnnounce() {
```
> يُعرّف دالة خاصّة باسم sendPeriodicBroadcastAnnounce (إرسال إعلان البثّ الدوري). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:168]

```
169:         announceJob?.cancel()
```
> يستدعي cancel على announceJob إن لم يكن null (إلغاء مهمّة الإعلان السابقة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:169]

```
170:         announceJob = serviceScope.launch {
```
> يُسنِد إلى announceJob كوروتيناً مُطلقاً (launch) على serviceScope. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:170]

```
171:             Log.d(TAG, "Starting periodic announce loop")
```
> يستدعي Log.d بالوسم TAG ورسالة نصّها "Starting periodic announce loop". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:171]

```
172:             while (isActive) {
```
> يبدأ حلقة while تستمرّ ما دامت isActive صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:172]

```
173:                 try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:173]

```
174:                     delay(30000) // 30 seconds
```
> يُؤخّر التنفيذ 30000 ميلي ثانية مع تعليق: «٣٠ ثانية». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:174]

```
175:                     sendBroadcastAnnounce()
```
> يستدعي الدالة sendBroadcastAnnounce (إرسال إعلان البثّ). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:175]

```
176:                 } catch (e: Exception) {
```
> يلتقط استثناءً باسم e من النوع Exception ويبدأ كتلة معالجته. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:176]

```
177:                     Log.e(TAG, "Error in periodic broadcast announce: ${e.message}")
```
> يستدعي Log.e بالوسم TAG ورسالة خطأ نصّها "Error in periodic broadcast announce: " متبوعاً برسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:177]

```
178:                 }
```
> إغلاق نطاق (كتلة catch). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:178]

```
179:             }
```
> إغلاق نطاق (حلقة while). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:179]

```
180:             Log.d(TAG, "Periodic announce loop ended (isActive=$isActive)")
```
> يستدعي Log.d بالوسم TAG ورسالة نصّها "Periodic announce loop ended (isActive=" متبوعاً بقيمة isActive. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:180]

```
181:         }
```
> إغلاق نطاق (كوروتين launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:181]

```
182:     }
```
> إغلاق نطاق (الدالة sendPeriodicBroadcastAnnounce). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:182]

```
183:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:183]

```
184:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:184]

```
185:      * Setup delegate connections between components
```
> تعليق: «تهيئة اتصالات المُفوَّضين بين المكوّنات». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:185]

```
186:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:186]

```
187:     private fun setupDelegates() {
```
> يُعرّف دالة خاصّة باسم setupDelegates (تهيئة المُفوَّضين). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:187]

```
188:         Log.d(TAG, "Setting up component delegates")
```
> يستدعي Log.d بالوسم TAG ورسالة نصّها "Setting up component delegates". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:188]

```
189:         // Provide nickname resolver to BLE broadcaster and debug manager
```
> تعليق: «تزويد مُحلِّل الاسم المستعار لباثّ BLE ومدير التنقيح». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:189]

```
190:         try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:190]

```
191:             val resolver: (String) -> String? = { pid -> peerManager.getPeerNickname(pid) }
```
> يُعرّف متغيّراً محلّياً للقراءة فقط باسم مُحلِّل (resolver) من نوع دالة تأخذ String وتُعيد String القابل لـ null، قيمته لامبدا وسيطها pid تُعيد ناتج getPeerNickname على peerManager للقيمة pid. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:191]

```
192:             connectionManager.setNicknameResolver(resolver)
```
> يستدعي setNicknameResolver على connectionManager مُمرّراً resolver. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:192]

```
193:             debugManager?.setNicknameResolver(resolver)
```
> يستدعي setNicknameResolver على debugManager إن لم يكن null مُمرّراً resolver. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:193]

```
194:         } catch (_: Exception) { }
```
> يلتقط أي استثناء (باسم مُهمَل) بكتلة معالجة فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:194]

```
195:         // PeerManager delegates to main mesh service delegate
```
> تعليق: «PeerManager يُفوّض إلى مُفوَّض خدمة الشبكة الرئيسي». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:195]

```
196:         peerManager.delegate = object : PeerManagerDelegate {
```
> يُسنِد إلى الخاصّية delegate في peerManager كائناً مجهولاً يُنفّذ الواجهة PeerManagerDelegate (مُفوَّض مدير النظراء). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:196]

```
197:             override fun onPeerListUpdated(peerIDs: List<String>) {
```
> يُلغي ويُعرّف الدالة onPeerListUpdated التي تأخذ مُعاملاً باسم peerIDs من النوع List<String> (قائمة مُعرّفات النظراء). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:197]

```
198:                 // Update process-wide state first
```
> تعليق: «تحديث الحالة على مستوى العملية أولاً». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:198]

```
199:                 try { com.bitchat.android.services.AppStateStore.setTransportPeers("BLE", peerIDs) } catch (_: Exception) { }
```
> داخل محاولة يستدعي setTransportPeers على AppStateStore مُمرّراً السلسلة "BLE" و peerIDs، ويلتقط أي استثناء بكتلة فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:199]

```
200:                 // Then notify UI delegate if attached
```
> تعليق: «ثم إبلاغ مُفوَّض الواجهة إن كان مُرفقاً». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:200]
