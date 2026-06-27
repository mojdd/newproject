# شريحة — app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يُعلِن أنّ هذا الملف ينتمي إلى الحزمة (package) المسمّاة `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف `Log` من `android.util` لاستعماله في تسجيل الرسائل. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:3]

```
4: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف `BitchatPacket` (حزمة بِت‑شات) من `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:4]

```
5: import com.bitchat.android.protocol.MessageType
```
> يستورد الصنف `MessageType` (نوع الرسالة) من `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:5]

```
6: import com.bitchat.android.model.RoutedPacket
```
> يستورد الصنف `RoutedPacket` (حزمة مُوجَّهة) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:6]

```
7: import kotlinx.coroutines.*
```
> يستورد كل العناصر العامّة من حزمة `kotlinx.coroutines` (الكوروتينات) باستعمال علامة النجمة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:7]

```
8: import kotlinx.coroutines.channels.Channel
```
> يستورد الصنف `Channel` (القناة) من `kotlinx.coroutines.channels`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:8]

```
9: import kotlinx.coroutines.channels.actor
```
> يستورد الدالة `actor` (المُمثِّل/الفاعل) من `kotlinx.coroutines.channels`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:9]

```
10: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:10]

```
11: /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:11]

```
12:  * Processes incoming packets and routes them to appropriate handlers
```
> تعليق: «يُعالِج الحزم الواردة ويُوجِّهها إلى المُعالِجات المناسبة». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:12]

```
13:  * 
```
> تعليق: سطر تعليق فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:13]

```
14:  * Per-peer packet serialization using Kotlin coroutine actors
```
> تعليق: «تسلسُل الحزم لكل نظير على حِدة باستعمال مُمثِّلات الكوروتين في كوتلن». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:14]

```
15:  * Prevents race condition where multiple threads process packets
```
> تعليق: «يمنع حالة التسابق حيث تُعالِج خيوط متعدّدة الحزم». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:15]

```
16:  * from the same peer simultaneously, causing session management conflicts.
```
> تعليق: «من النظير نفسه في آنٍ واحد، مُسبِّبة تعارضات في إدارة الجلسة». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:16]

```
17:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:17]

```
18: class PacketProcessor(private val myPeerID: String) {
```
> يُعرِّف الصنف `PacketProcessor` (مُعالِج الحزم) بِبانٍ يأخذ مُعامِلاً خاصّاً ثابتاً `myPeerID` من نوع نص (String). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:18]

```
19:     private val debugManager by lazy { try { com.bitchat.android.ui.debug.DebugSettingsManager.getInstance() } catch (e: Exception) { null } }
```
> يُعرِّف خاصّية خاصّة ثابتة `debugManager` (مدير التنقيح) تُهيَّأ كسولاً (lazy) باستدعاء `DebugSettingsManager.getInstance()`، وتُعيد `null` إذا رُمي استثناء. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:19]

```
20:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:20]

```
21:     companion object {
```
> يفتح كائناً مُرافِقاً (companion object) لاحتواء أعضاء على مستوى الصنف. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:21]

```
22:         private const val TAG = "PacketProcessor"
```
> يُعرِّف ثابتاً خاصّاً `TAG` (الوسم) بقيمة نصّية `"PacketProcessor"`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:22]

```
23:     }
```
> إغلاق نطاق الكائن المُرافِق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:23]

```
24:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:24]

```
25:     // Delegate for callbacks
```
> تعليق: «المُفوَّض إليه للنداءات المرتجعة». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:25]

```
26:     var delegate: PacketProcessorDelegate? = null
```
> يُعرِّف خاصّية متغيّرة `delegate` (المُفوَّض إليه) من نوع `PacketProcessorDelegate` قابل لِأن يكون فارغاً، قيمتها الابتدائية `null`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:26]

```
27:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:27]

```
28:     // Helper function to format peer ID with nickname for logging
```
> تعليق: «دالة مساعِدة لتنسيق معرّف النظير مع الاسم المستعار للتسجيل». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:28]

```
29:     private fun formatPeerForLog(peerID: String): String {
```
> يُعرِّف دالة خاصّة `formatPeerForLog` (تنسيق النظير للتسجيل) تأخذ `peerID` نصّاً وتُعيد نصّاً. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:29]

```
30:         val nickname = delegate?.getPeerNickname(peerID)
```
> يُعرِّف متغيّراً ثابتاً `nickname` (الاسم المستعار) بقيمة ناتج استدعاء `getPeerNickname(peerID)` على المُفوَّض إليه إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:30]

```
31:         return if (nickname != null) "$peerID ($nickname)" else peerID
```
> يُعيد نصّاً يدمج `peerID` مع الاسم المستعار بين قوسين إذا كان `nickname` غير فارغ، وإلّا يُعيد `peerID` وحده. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:31]

```
32:     }
```
> إغلاق نطاق الدالة `formatPeerForLog`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:32]

```
33:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:33]

```
34:     // Packet relay manager for centralized relay decisions
```
> تعليق: «مدير ترحيل الحزم لقرارات الترحيل المركزية». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:34]

```
35:     private val packetRelayManager = PacketRelayManager(myPeerID)
```
> يُعرِّف خاصّية خاصّة ثابتة `packetRelayManager` (مدير ترحيل الحزم) بإنشاء كائن `PacketRelayManager` مُمرِّراً إليه `myPeerID`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:35]

```
36:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:36]

```
37:     // Coroutines
```
> تعليق: «الكوروتينات». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:37]

```
38:     private val processorScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يُعرِّف خاصّية خاصّة ثابتة `processorScope` (نطاق المُعالِج) بإنشاء `CoroutineScope` مكوّن من مُوزِّع الإدخال/الإخراج `Dispatchers.IO` مع مهمّة مُشرِفة `SupervisorJob()`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:38]

```
39:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:39]

```
40:     // Per-peer actors to serialize packet processing
```
> تعليق: «مُمثِّلات لكل نظير لتسلسُل معالجة الحزم». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:40]

```
41:     // Each peer gets its own actor that processes packets sequentially
```
> تعليق: «كل نظير يحصل على مُمثِّله الخاص الذي يُعالِج الحزم تتابُعياً». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:41]

```
42:     // This prevents race conditions in session management
```
> تعليق: «هذا يمنع حالات التسابق في إدارة الجلسة». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:42]

```
43:     private val peerActors = mutableMapOf<String, CompletableDeferred<Unit>>()
```
> يُعرِّف خاصّية خاصّة ثابتة `peerActors` (مُمثِّلو النظراء) كخريطة قابلة للتعديل مفاتيحها نصوص وقيمها `CompletableDeferred<Unit>`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:43]

```
44:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:44]

```
45:     @OptIn(ObsoleteCoroutinesApi::class)
```
> يضع توضيحاً (annotation) `@OptIn` لقبول استعمال واجهة الكوروتينات المهجورة `ObsoleteCoroutinesApi`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:45]

```
46:     private fun getOrCreateActorForPeer(peerID: String) = processorScope.actor<RoutedPacket>(
```
> يُعرِّف دالة خاصّة `getOrCreateActorForPeer` (جلب أو إنشاء مُمثِّل للنظير) تأخذ `peerID` نصّاً، وتُعيد ناتج استدعاء `processorScope.actor` بنوع عناصر `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:46]

```
47:         capacity = Channel.UNLIMITED
```
> يُمرِّر المُعامِل `capacity` (السَّعة) بقيمة `Channel.UNLIMITED` أي سعة غير محدودة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:47]

```
48:     ) {
```
> يُغلِق قائمة مُعامِلات استدعاء `actor` ويفتح جسم الكوروتين (lambda). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:48]

```
49:         Log.d(TAG, "🎭 Created packet actor for peer: ${formatPeerForLog(peerID)}")
```
> يستدعي `Log.d` بالوسم `TAG` ونصّ يقول «🎭 Created packet actor for peer:» متبوعاً بنتيجة `formatPeerForLog(peerID)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:49]

```
50:         try {
```
> يفتح كتلة `try` (محاولة). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:50]

```
51:             for (packet in channel) {
```
> يبدأ حلقة `for` تكرّر على كل عنصر `packet` مأخوذ من القناة `channel`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:51]

```
52:                 Log.d(TAG, "📦 Processing packet type ${packet.packet.type} from ${formatPeerForLog(peerID)} (serialized)")
```
> يستدعي `Log.d` بنصّ «📦 Processing packet type» متبوعاً بنوع الحزمة `packet.packet.type` ومصدرها `formatPeerForLog(peerID)` وكلمة «(serialized)». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:52]

```
53:                 handleReceivedPacket(packet)
```
> يستدعي الدالة `handleReceivedPacket` (معالجة الحزمة المُستلَمة) مُمرِّراً `packet`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:53]

```
54:                 Log.d(TAG, "Completed packet type ${packet.packet.type} from ${formatPeerForLog(peerID)}")
```
> يستدعي `Log.d` بنصّ «Completed packet type» متبوعاً بنوع الحزمة ومصدرها. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:54]

```
55:             }
```
> إغلاق نطاق حلقة `for`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:55]

```
56:         } finally {
```
> يُغلِق كتلة `try` ويفتح كتلة `finally` (في النهاية). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:56]

```
57:             Log.d(TAG, "🎭 Packet actor for ${formatPeerForLog(peerID)} terminated")
```
> يستدعي `Log.d` بنصّ «🎭 Packet actor for» متبوعاً بمصدر النظير وكلمة «terminated». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:57]

```
58:         }
```
> إغلاق نطاق كتلة `finally`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:58]

```
59:     }
```
> إغلاق نطاق جسم الكوروتين ودالة `getOrCreateActorForPeer`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:59]

```
60:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:60]

```
61:     // Cache actors to reuse them
```
> تعليق: «خزّن المُمثِّلين مؤقّتاً لإعادة استعمالهم». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:61]

```
62:     private val actors = mutableMapOf<String, kotlinx.coroutines.channels.SendChannel<RoutedPacket>>()
```
> يُعرِّف خاصّية خاصّة ثابتة `actors` (المُمثِّلون) كخريطة قابلة للتعديل مفاتيحها نصوص وقيمها قنوات إرسال `SendChannel<RoutedPacket>`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:62]

```
63:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:63]

```
64:     init {
```
> يفتح كتلة التهيئة `init` للصنف. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:64]

```
65:         // Set up the packet relay manager delegate immediately
```
> تعليق: «اضبط مُفوَّض مدير ترحيل الحزم فوراً». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:65]

```
66:         setupRelayManager()
```
> يستدعي الدالة `setupRelayManager` (ضبط مدير الترحيل). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:66]

```
67:     }
```
> إغلاق نطاق كتلة `init`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:67]

```
68:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:68]

```
69:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:69]

```
70:      * Process received packet - main entry point for all incoming packets
```
> تعليق: «معالجة الحزمة المُستلَمة - نقطة الدخول الرئيسية لكل الحزم الواردة». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:70]

```
71:      * SURGICAL FIX: Route to per-peer actor for serialized processing
```
> تعليق: «إصلاح جراحي: وجِّه إلى مُمثِّل لكل نظير من أجل المعالجة المتسلسلة». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:71]

```
72:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:72]

```
73:     fun processPacket(routed: RoutedPacket) {
```
> يُعرِّف دالة عامّة `processPacket` (معالجة الحزمة) تأخذ مُعامِلاً `routed` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:73]

```
74:         Log.d(TAG, "processPacket ${routed.packet.type}")
```
> يستدعي `Log.d` بنصّ «processPacket» متبوعاً بنوع الحزمة `routed.packet.type`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:74]

```
75:         val peerID = routed.peerID
```
> يُعرِّف متغيّراً ثابتاً `peerID` بقيمة `routed.peerID` (معرّف نظير الحزمة المُوجَّهة). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:75]

```
76: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:76]

```
77:         if (peerID == null) {
```
> يفتح شرطاً يفحص ما إذا كان `peerID` يساوي `null`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:77]

```
78:             Log.w(TAG, "Received packet with no peer ID, skipping")
```
> يستدعي `Log.w` (تحذير) بنصّ «Received packet with no peer ID, skipping». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:78]

```
79:             return
```
> يُنفِّذ `return` للخروج من الدالة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:79]

```
80:         }
```
> إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:80]

```
81:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:81]

```
82:         // Get or create actor for this peer
```
> تعليق: «اجلب أو أنشئ مُمثِّلاً لهذا النظير». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:82]

```
83:         val actor = actors.getOrPut(peerID) { getOrCreateActorForPeer(peerID) }
```
> يُعرِّف متغيّراً ثابتاً `actor` (المُمثِّل) بقيمة المُخزَّنة في الخريطة `actors` لمفتاح `peerID`، وإن لم توجد يُنشئها عبر `getOrCreateActorForPeer(peerID)` ويضعها. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:83]

```
84:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:84]

```
85:         // Send packet to peer's dedicated actor for serialized processing
```
> تعليق: «أرسل الحزمة إلى المُمثِّل المخصّص للنظير من أجل المعالجة المتسلسلة». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:85]

```
86:         processorScope.launch {
```
> يستدعي `processorScope.launch` لإطلاق كوروتين جديد ويفتح جسمه. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:86]

```
87:             try {
```
> يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:87]

```
88:                 actor.send(routed)
```
> يستدعي `actor.send` مُمرِّراً `routed` لإرسال الحزمة إلى قناة المُمثِّل. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:88]

```
89:             } catch (e: Exception) {
```
> يُغلِق `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:89]

```
90:                 Log.w(TAG, "Failed to send packet to actor for ${formatPeerForLog(peerID)}: ${e.message}")
```
> يستدعي `Log.w` بنصّ «Failed to send packet to actor for» متبوعاً بمصدر النظير ورسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:90]

```
91:                 // Fallback to direct processing if actor fails
```
> تعليق: «الرجوع إلى المعالجة المباشرة إذا فشل المُمثِّل». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:91]

```
92:                 handleReceivedPacket(routed)
```
> يستدعي `handleReceivedPacket` مُمرِّراً `routed` كمعالجة احتياطية مباشرة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:92]

```
93:             }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:93]

```
94:         }
```
> إغلاق نطاق جسم الكوروتين المُطلَق بـ `launch`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:94]

```
95:     }
```
> إغلاق نطاق دالة `processPacket`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:95]

```
96:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:96]

```
97:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:97]

```
98:      * Set up the packet relay manager with its delegate
```
> تعليق: «اضبط مدير ترحيل الحزم مع مُفوَّضه». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:98]

```
99:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:99]

```
100:     fun setupRelayManager() {
```
> يُعرِّف دالة عامّة `setupRelayManager` (ضبط مدير الترحيل) بلا مُعامِلات. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:100]

```
101:         packetRelayManager.delegate = object : PacketRelayManagerDelegate {
```
> يُسنِد إلى `packetRelayManager.delegate` كائناً مجهولاً (object) يُحقِّق الواجهة `PacketRelayManagerDelegate`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:101]

```
102:             override fun getNetworkSize(): Int {
```
> يُعيد تعريف (override) الدالة `getNetworkSize` (حجم الشبكة) التي تُعيد عدداً صحيحاً `Int`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:102]

```
103:                 return delegate?.getNetworkSize() ?: 1
```
> يُعيد ناتج `getNetworkSize()` على المُفوَّض إليه إن لم يكن فارغاً، وإلّا القيمة `1`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:103]

```
104:             }
```
> إغلاق نطاق الدالة `getNetworkSize`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:104]

```
105:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:105]

```
106:             override fun getBroadcastRecipient(): ByteArray {
```
> يُعيد تعريف الدالة `getBroadcastRecipient` (مُستلِم البثّ) التي تُعيد مصفوفة بايتات `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:106]

```
107:                 return delegate?.getBroadcastRecipient() ?: ByteArray(0)
```
> يُعيد ناتج `getBroadcastRecipient()` على المُفوَّض إليه إن لم يكن فارغاً، وإلّا مصفوفة بايتات طولها صفر `ByteArray(0)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:107]

```
108:             }
```
> إغلاق نطاق الدالة `getBroadcastRecipient`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:108]

```
109:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:109]

```
110:             override fun broadcastPacket(routed: RoutedPacket) {
```
> يُعيد تعريف الدالة `broadcastPacket` (بثّ الحزمة) التي تأخذ `routed` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:110]

```
111:                 delegate?.relayPacket(routed)
```
> يستدعي `relayPacket(routed)` على المُفوَّض إليه إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:111]

```
112:             }
```
> إغلاق نطاق الدالة `broadcastPacket`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:112]

```
113:             override fun sendToPeer(peerID: String, routed: RoutedPacket): Boolean {
```
> يُعيد تعريف الدالة `sendToPeer` (الإرسال إلى النظير) التي تأخذ `peerID` نصّاً و`routed` من نوع `RoutedPacket` وتُعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:113]

```
114:                 return delegate?.sendToPeer(peerID, routed) ?: false
```
> يُعيد ناتج `sendToPeer(peerID, routed)` على المُفوَّض إليه إن لم يكن فارغاً، وإلّا القيمة `false`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:114]

```
115:             }
```
> إغلاق نطاق الدالة `sendToPeer`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:115]

```
116:         }
```
> إغلاق نطاق الكائن المجهول المُحقِّق للواجهة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:116]

```
117:     }
```
> إغلاق نطاق دالة `setupRelayManager`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:117]

```
118:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:118]

```
119:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:119]

```
120:      * Handle received packet - core protocol logic (exact same as iOS)
```
> تعليق: «معالجة الحزمة المُستلَمة - منطق البروتوكول الأساسي (مطابق تماماً لِـ iOS)». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:120]

```
121:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:121]

```
122:     private suspend fun handleReceivedPacket(routed: RoutedPacket) {
```
> يُعرِّف دالة خاصّة مُعلَّقة (suspend) `handleReceivedPacket` تأخذ `routed` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:122]

```
123:         val packet = routed.packet
```
> يُعرِّف متغيّراً ثابتاً `packet` (الحزمة) بقيمة `routed.packet`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:123]

```
124:         val peerID = routed.peerID ?: "unknown"
```
> يُعرِّف متغيّراً ثابتاً `peerID` بقيمة `routed.peerID` إن لم يكن فارغاً، وإلّا النصّ `"unknown"`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:124]

```
125: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:125]

```
126:         // Basic validation and security checks
```
> تعليق: «تحقّق أساسي وفحوص أمنية». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:126]

```
127:         if (!delegate?.validatePacketSecurity(packet, peerID)!!) {
```
> يفتح شرطاً ينفي ناتج `validatePacketSecurity(packet, peerID)` المستدعى على المُفوَّض إليه مع عامل التأكيد على عدم الفراغ `!!`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:127]

```
128:             Log.d(TAG, "Packet failed security validation from ${formatPeerForLog(peerID)}")
```
> يستدعي `Log.d` بنصّ «Packet failed security validation from» متبوعاً بمصدر النظير. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:128]

```
129:             return
```
> يُنفِّذ `return` للخروج من الدالة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:129]

```
130:         }
```
> إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:130]

```
131: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:131]

```
132:         var validPacket = true
```
> يُعرِّف متغيّراً قابلاً للتغيير `validPacket` (حزمة صالحة) بقيمة ابتدائية `true`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:132]

```
133:         val messageType = MessageType.fromValue(packet.type)
```
> يُعرِّف متغيّراً ثابتاً `messageType` (نوع الرسالة) بناتج `MessageType.fromValue(packet.type)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:133]

```
134:         Log.d(TAG, "Processing packet type ${messageType} from ${formatPeerForLog(peerID)}")
```
> يستدعي `Log.d` بنصّ «Processing packet type» متبوعاً بـ `messageType` ومصدر النظير. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:134]

```
135:         // Verbose logging to debug manager (and chat via ChatViewModel observer)
```
> تعليق: «تسجيل مُفصَّل إلى مدير التنقيح (وإلى المحادثة عبر مُراقِب ChatViewModel)». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:135]

```
136:         try {
```
> يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:136]

```
137:             val mt = messageType?.name ?: packet.type.toString()
```
> يُعرِّف متغيّراً ثابتاً `mt` بقيمة `messageType.name` إن لم يكن فارغاً، وإلّا نصّ `packet.type.toString()`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:137]

```
138:             val routeDevice = routed.relayAddress
```
> يُعرِّف متغيّراً ثابتاً `routeDevice` (جهاز التوجيه) بقيمة `routed.relayAddress` (عنوان المُرحِّل). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:138]

```
139:             val nick = delegate?.getPeerNickname(peerID)
```
> يُعرِّف متغيّراً ثابتاً `nick` بناتج `getPeerNickname(peerID)` المستدعى على المُفوَّض إليه إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:139]

```
140:             debugManager?.logIncomingPacket(peerID, nick, mt, routeDevice)
```
> يستدعي `logIncomingPacket(peerID, nick, mt, routeDevice)` على `debugManager` إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:140]

```
141:         } catch (_: Exception) { }
```
> يُغلِق `try` ويلتقط استثناءً مُهمَلاً من نوع `Exception` بجسم فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:141]

```
142:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:142]

```
143:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:143]

```
144:         // Handle public packet types (no address check needed)
```
> تعليق: «عالِج أنواع الحزم العامّة (لا حاجة لفحص العنوان)». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:144]

```
145:         when (messageType) {
```
> يفتح تعبير `when` يتفرّع بحسب قيمة `messageType`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:145]

```
146:             MessageType.ANNOUNCE -> handleAnnounce(routed)
```
> إذا كان النوع `MessageType.ANNOUNCE` (إعلان) يستدعي `handleAnnounce(routed)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:146]

```
147:             MessageType.MESSAGE -> handleMessage(routed)
```
> إذا كان النوع `MessageType.MESSAGE` (رسالة) يستدعي `handleMessage(routed)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:147]

```
148:             MessageType.FILE_TRANSFER -> handleMessage(routed) // treat same routing path; parsing happens in handler
```
> إذا كان النوع `MessageType.FILE_TRANSFER` (نقل ملف) يستدعي `handleMessage(routed)`؛ تعليق: «عامِله بنفس مسار التوجيه؛ التحليل يحدث في المُعالِج». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:148]

```
149:             MessageType.LEAVE -> handleLeave(routed)
```
> إذا كان النوع `MessageType.LEAVE` (مغادرة) يستدعي `handleLeave(routed)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:149]

```
150:             MessageType.FRAGMENT -> handleFragment(routed)
```
> إذا كان النوع `MessageType.FRAGMENT` (جزء/شظيّة) يستدعي `handleFragment(routed)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:150]

```
151:             MessageType.REQUEST_SYNC -> handleRequestSync(routed)
```
> إذا كان النوع `MessageType.REQUEST_SYNC` (طلب مزامنة) يستدعي `handleRequestSync(routed)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:151]

```
152:             else -> {
```
> يفتح فرع `else` (وإلّا) للحالات الأخرى. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:152]

```
153:                 // Handle private packet types (address check required)
```
> تعليق: «عالِج أنواع الحزم الخاصّة (فحص العنوان مطلوب)». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:153]

```
154:                 if (packetRelayManager.isPacketAddressedToMe(packet)) {
```
> يفتح شرطاً يفحص ناتج `isPacketAddressedToMe(packet)` على `packetRelayManager` (هل الحزمة موجَّهة إليّ). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:154]

```
155:                     when (messageType) {
```
> يفتح تعبير `when` داخلي يتفرّع بحسب `messageType`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:155]

```
156:                         MessageType.NOISE_HANDSHAKE -> handleNoiseHandshake(routed)
```
> إذا كان النوع `MessageType.NOISE_HANDSHAKE` (مصافحة Noise) يستدعي `handleNoiseHandshake(routed)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:156]

```
157:                         MessageType.NOISE_ENCRYPTED -> handleNoiseEncrypted(routed)
```
> إذا كان النوع `MessageType.NOISE_ENCRYPTED` (مُشفَّر بـ Noise) يستدعي `handleNoiseEncrypted(routed)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:157]

```
158:                         MessageType.FILE_TRANSFER -> handleMessage(routed)
```
> إذا كان النوع `MessageType.FILE_TRANSFER` (نقل ملف) يستدعي `handleMessage(routed)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:158]

```
159:                         else -> {
```
> يفتح فرع `else` داخلياً للحالات الأخرى. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:159]

```
160:                             validPacket = false
```
> يُسنِد القيمة `false` للمتغيّر `validPacket`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:160]

```
161:                             Log.w(TAG, "Unknown message type: ${packet.type}")
```
> يستدعي `Log.w` بنصّ «Unknown message type:» متبوعاً بـ `packet.type`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:161]

```
162:                         }
```
> إغلاق نطاق فرع `else` الداخلي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:162]

```
163:                     }
```
> إغلاق نطاق تعبير `when` الداخلي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:163]

```
164:                 } else {
```
> يُغلِق كتلة `if` ويفتح كتلة `else` المقابِلة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:164]

```
165:                     Log.d(TAG, "Private packet type ${messageType} not addressed to us (from: ${formatPeerForLog(peerID)} to ${packet.recipientID?.let { it.joinToString("") { b -> "%02x".format(b) } }}), skipping")
```
> يستدعي `Log.d` بنصّ يقول إنّ نوع الحزمة الخاصّة `messageType` غير موجَّه إلينا، مع ذكر المصدر `formatPeerForLog(peerID)` والمُستلِم المُحوَّل من `packet.recipientID` إلى نصّ سُداسي عشري عبر `joinToString` و`"%02x".format(b)`، ثمّ كلمة «skipping». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:165]

```
166:                 }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:166]

```
167:             }
```
> إغلاق نطاق فرع `else` الخارجي لتعبير `when`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:167]

```
168:         }
```
> إغلاق نطاق تعبير `when` الخارجي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:168]

```
169:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:169]

```
170:         // Update last seen timestamp
```
> تعليق: «حدِّث الطابع الزمني لآخر ظهور». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:170]

```
171:         if (validPacket) {
```
> يفتح شرطاً يفحص ما إذا كان `validPacket` صحيحاً. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:171]

```
172:             delegate?.updatePeerLastSeen(peerID)
```
> يستدعي `updatePeerLastSeen(peerID)` على المُفوَّض إليه إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:172]

```
173:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:173]

```
174:             // CENTRALIZED RELAY LOGIC: Handle relay decisions for all packets not addressed to us
```
> تعليق: «منطق ترحيل مركزي: عالِج قرارات الترحيل لكل الحزم غير الموجَّهة إلينا». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:174]

```
175:             packetRelayManager.handlePacketRelay(routed)
```
> يستدعي `handlePacketRelay(routed)` على `packetRelayManager`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:175]

```
176:         }
```
> إغلاق نطاق كتلة الشرط `if (validPacket)`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:176]

```
177:     }
```
> إغلاق نطاق دالة `handleReceivedPacket`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:177]

```
178:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:178]

```
179:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:179]

```
180:      * Handle Noise handshake message - SIMPLIFIED iOS-compatible version
```
> تعليق: «معالجة رسالة مصافحة Noise - نسخة مُبسَّطة متوافقة مع iOS». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:180]

```
181:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:181]

```
182:     private suspend fun handleNoiseHandshake(routed: RoutedPacket) {
```
> يُعرِّف دالة خاصّة مُعلَّقة `handleNoiseHandshake` (معالجة مصافحة Noise) تأخذ `routed` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:182]

```
183:         val peerID = routed.peerID ?: "unknown"
```
> يُعرِّف متغيّراً ثابتاً `peerID` بقيمة `routed.peerID` إن لم يكن فارغاً، وإلّا النصّ `"unknown"`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:183]

```
184:         Log.d(TAG, "Processing Noise handshake from ${formatPeerForLog(peerID)}")
```
> يستدعي `Log.d` بنصّ «Processing Noise handshake from» متبوعاً بمصدر النظير. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:184]

```
185:         delegate?.handleNoiseHandshake(routed)
```
> يستدعي `handleNoiseHandshake(routed)` على المُفوَّض إليه إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:185]

```
186:     }
```
> إغلاق نطاق دالة `handleNoiseHandshake`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:186]

```
187:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:187]

```
188:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:188]

```
189:      * Handle Noise encrypted transport message
```
> تعليق: «معالجة رسالة النقل المُشفَّرة بـ Noise». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:189]

```
190:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:190]

```
191:     private suspend fun handleNoiseEncrypted(routed: RoutedPacket) {
```
> يُعرِّف دالة خاصّة مُعلَّقة `handleNoiseEncrypted` (معالجة المُشفَّر بـ Noise) تأخذ `routed` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:191]

```
192:         val peerID = routed.peerID ?: "unknown"
```
> يُعرِّف متغيّراً ثابتاً `peerID` بقيمة `routed.peerID` إن لم يكن فارغاً، وإلّا النصّ `"unknown"`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:192]

```
193:         Log.d(TAG, "Processing Noise encrypted message from ${formatPeerForLog(peerID)}")
```
> يستدعي `Log.d` بنصّ «Processing Noise encrypted message from» متبوعاً بمصدر النظير. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:193]

```
194:         delegate?.handleNoiseEncrypted(routed)
```
> يستدعي `handleNoiseEncrypted(routed)` على المُفوَّض إليه إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:194]

```
195:     }
```
> إغلاق نطاق دالة `handleNoiseEncrypted`. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:195]

```
196:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:196]

```
197:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:197]

```
198:      * Handle announce message
```
> تعليق: «معالجة رسالة الإعلان». [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:198]

```
199:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:199]

```
200:     private suspend fun handleAnnounce(routed: RoutedPacket) {
```
> يُعرِّف دالة خاصّة مُعلَّقة `handleAnnounce` (معالجة الإعلان) تأخذ `routed` من نوع `RoutedPacket`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:200]
