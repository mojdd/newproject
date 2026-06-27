# شريحة — app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) المسماة com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف Log من حزمة android.util لكتابة رسائل السجلّ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:3]

```
4: import com.bitchat.android.crypto.EncryptionService
```
> يستورد صنف خدمة التشفير (EncryptionService) من حزمة com.bitchat.android.crypto. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:4]

```
5: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد صنف الحزمة الشبكية (BitchatPacket) من حزمة com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:5]

```
6: import com.bitchat.android.protocol.MessageType
```
> يستورد صنف نوع الرسالة (MessageType) من حزمة com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:6]

```
7: import com.bitchat.android.model.RoutedPacket
```
> يستورد صنف الحزمة الموجَّهة (RoutedPacket) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:7]

```
8: import com.bitchat.android.util.toHexString
```
> يستورد الدالة toHexString (تحويل إلى نص ست عشري) من حزمة com.bitchat.android.util. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:8]

```
9: import kotlinx.coroutines.*
```
> يستورد كل العناصر من حزمة الكوروتينات (kotlinx.coroutines). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:9]

```
10: import java.util.*
```
> يستورد كل العناصر من حزمة java.util. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:10]

```
11: import kotlin.collections.mutableSetOf
```
> يستورد الدالة mutableSetOf (إنشاء مجموعة قابلة للتعديل) من حزمة kotlin.collections. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:11]

```
12: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:12]

```
13: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:13]

```
14:  * Manages security aspects of the mesh network including duplicate detection,
```
> تعليق: يدير جوانب الأمان في الشبكة المتشابكة بما في ذلك كشف التكرار. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:14]

```
15:  * replay attack protection, and key exchange handling
```
> تعليق: الحماية من هجوم الإعادة، ومعالجة تبادل المفاتيح. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:15]

```
16:  * Extracted from BluetoothMeshService for better separation of concerns
```
> تعليق: مُستخرَج من BluetoothMeshService لفصل أفضل للاهتمامات. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:16]

```
17:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:17]

```
18: class SecurityManager(private val encryptionService: EncryptionService, private val myPeerID: String) {
```
> يعرّف الصنف مدير الأمان (SecurityManager) ببانٍ يأخذ معاملاً خاصاً encryptionService من نوع EncryptionService ومعاملاً خاصاً myPeerID من نوع String. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:18]

```
19:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:19]

```
20:     companion object {
```
> يبدأ كائناً مرافقاً (companion object) للصنف. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:20]

```
21:         private const val TAG = "SecurityManager"
```
> يعرّف ثابتاً خاصاً اسمه TAG قيمته النص "SecurityManager". [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:21]

```
22:         private const val MESSAGE_TIMEOUT = com.bitchat.android.util.AppConstants.Security.MESSAGE_TIMEOUT_MS // 5 minutes (same as iOS)
```
> يعرّف ثابتاً خاصاً اسمه MESSAGE_TIMEOUT قيمته AppConstants.Security.MESSAGE_TIMEOUT_MS، مع تعليق: خمس دقائق (نفس iOS). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:22]

```
23:         private const val CLEANUP_INTERVAL = com.bitchat.android.util.AppConstants.Security.CLEANUP_INTERVAL_MS // 5 minutes
```
> يعرّف ثابتاً خاصاً اسمه CLEANUP_INTERVAL قيمته AppConstants.Security.CLEANUP_INTERVAL_MS، مع تعليق: خمس دقائق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:23]

```
24:         private const val MAX_PROCESSED_MESSAGES = com.bitchat.android.util.AppConstants.Security.MAX_PROCESSED_MESSAGES
```
> يعرّف ثابتاً خاصاً اسمه MAX_PROCESSED_MESSAGES قيمته AppConstants.Security.MAX_PROCESSED_MESSAGES. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:24]

```
25:         private const val MAX_PROCESSED_KEY_EXCHANGES = com.bitchat.android.util.AppConstants.Security.MAX_PROCESSED_KEY_EXCHANGES
```
> يعرّف ثابتاً خاصاً اسمه MAX_PROCESSED_KEY_EXCHANGES قيمته AppConstants.Security.MAX_PROCESSED_KEY_EXCHANGES. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:25]

```
26:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:26]

```
27:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:27]

```
28:     // Security tracking
```
> تعليق: تتبّع الأمان. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:28]

```
29:     private val processedMessages = Collections.synchronizedSet(mutableSetOf<String>())
```
> يعرّف حقلاً خاصاً اسمه processedMessages (الرسائل المعالَجة) ويسنده إلى مجموعة متزامنة (synchronizedSet) من نصوص قابلة للتعديل. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:29]

```
30:     private val processedKeyExchanges = Collections.synchronizedSet(mutableSetOf<String>())
```
> يعرّف حقلاً خاصاً اسمه processedKeyExchanges (تبادلات المفاتيح المعالَجة) ويسنده إلى مجموعة متزامنة من نصوص قابلة للتعديل. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:30]

```
31:     private val messageTimestamps = Collections.synchronizedMap(mutableMapOf<String, Long>())
```
> يعرّف حقلاً خاصاً اسمه messageTimestamps (طوابع وقت الرسائل) ويسنده إلى خريطة متزامنة (synchronizedMap) مفاتيحها نصوص وقيمها أعداد طويلة Long. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:31]

```
32:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:32]

```
33:     // Delegate for callbacks
```
> تعليق: مفوَّض (delegate) لاستدعاءات الرجوع. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:33]

```
34:     var delegate: SecurityManagerDelegate? = null
```
> يعرّف حقلاً متغيّراً اسمه delegate من نوع SecurityManagerDelegate قابل لأن يكون فارغاً ويسنده ابتداءً إلى null. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:34]

```
35:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:35]

```
36:     // Coroutines
```
> تعليق: الكوروتينات. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:36]

```
37:     private val managerScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يعرّف حقلاً خاصاً اسمه managerScope (نطاق المدير) ويسنده إلى نطاق كوروتين (CoroutineScope) مبني على موزّع الإدخال/الإخراج Dispatchers.IO مع مهمة مُشرِفة SupervisorJob. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:37]

```
38:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:38]

```
39:     init {
```
> يبدأ كتلة التهيئة (init) للصنف. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:39]

```
40:         startPeriodicCleanup()
```
> يستدعي الدالة startPeriodicCleanup (بدء التنظيف الدوري). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:40]

```
41:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:41]

```
42:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:42]

```
43:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:43]

```
44:      * Validate packet security (timestamp, replay attacks, duplicates, signatures)
```
> تعليق: تحقّق من أمان الحزمة (الطابع الزمني، هجمات الإعادة، التكرارات، التواقيع). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:44]

```
45:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:45]

```
46:     fun validatePacket(packet: BitchatPacket, peerID: String): Boolean {
```
> يعرّف الدالة validatePacket (التحقق من الحزمة) التي تأخذ معاملاً packet من نوع BitchatPacket ومعاملاً peerID من نوع String وتعيد قيمة منطقية Boolean. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:46]

```
47:         // Skip validation for our own packets
```
> تعليق: تجاوز التحقق من حِزمنا الخاصة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:47]

```
48:         if (peerID == myPeerID) {
```
> يفحص شرطاً: إذا كان peerID يساوي myPeerID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:48]

```
49:             Log.d(TAG, "Skipping validation for our own packet")
```
> يكتب رسالة سجلّ تصحيح (Log.d) بالوسم TAG ونصها "Skipping validation for our own packet". [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:49]

```
50:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:50]

```
51:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:51]

```
52:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:52]

```
53:         // Replay attack protection (same 5-minute window as iOS)
```
> تعليق: حماية من هجوم الإعادة (نفس نافذة الخمس دقائق في iOS). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:53]

```
54:         val currentTime = System.currentTimeMillis()
```
> يعرّف متغيراً اسمه currentTime ويسنده إلى الوقت الحالي بالملّي ثانية عبر System.currentTimeMillis. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:54]

```
55:         val messageType = MessageType.fromValue(packet.type)
```
> يعرّف متغيراً اسمه messageType ويسنده إلى نتيجة MessageType.fromValue للقيمة packet.type. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:55]

```
56: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:56]

```
57:         // Duplicate detection
```
> تعليق: كشف التكرار. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:57]

```
58:         val messageID = generateMessageID(packet, peerID)
```
> يعرّف متغيراً اسمه messageID (معرّف الرسالة) ويسنده إلى نتيجة استدعاء الدالة generateMessageID بالوسيطين packet و peerID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:58]

```
59:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:59]

```
60:         if (processedMessages.contains(messageID)) {
```
> يفحص شرطاً: إذا كانت مجموعة processedMessages تحتوي messageID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:60]

```
61:             // Check for ANNOUNCE exception: allow if it looks like a direct neighbor (max TTL)
```
> تعليق: افحص استثناء ANNOUNCE: اسمح إن بدت من جار مباشر (أقصى قيمة TTL). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:61]

```
62:             // This ensures we catch the "first announce" on a new connection for binding,
```
> تعليق: يضمن هذا التقاط "أول إعلان" على اتصال جديد لأجل الربط. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:62]

```
63:             // while still dropping looped/relayed duplicates.
```
> تعليق: مع الاستمرار في إسقاط التكرارات المُعاد بثّها أو المُكرَّرة حلقياً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:63]

```
64:             val isFreshAnnounce = messageType == MessageType.ANNOUNCE &&
```
> يعرّف متغيراً اسمه isFreshAnnounce (إعلان طازج) ويسنده إلى نتيجة شرط: messageType يساوي MessageType.ANNOUNCE وأيضاً (يتبع في السطر التالي). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:64]

```
65:                     packet.ttl >= com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS
```
> تتمة الشرط: وأن packet.ttl أكبر من أو يساوي AppConstants.MESSAGE_TTL_HOPS. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:65]

```
66: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:66]

```
67:             if (!isFreshAnnounce) {
```
> يفحص شرطاً: إذا لم يكن isFreshAnnounce صحيحاً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:67]

```
68:                 Log.d(TAG, "Dropping duplicate packet: $messageID")
```
> يكتب رسالة سجلّ تصحيح بالوسم TAG ونصها "Dropping duplicate packet:" متبوعاً بقيمة messageID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:68]

```
69:                 return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:69]

```
70:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:70]

```
71:             Log.d(TAG, "Allowing duplicate ANNOUNCE from direct neighbor: $messageID")
```
> يكتب رسالة سجلّ تصحيح بالوسم TAG ونصها "Allowing duplicate ANNOUNCE from direct neighbor:" متبوعاً بقيمة messageID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:71]

```
72:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:72]

```
73: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:73]

```
74:         // Add to processed messages
```
> تعليق: أضف إلى الرسائل المعالَجة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:74]

```
75:         processedMessages.add(messageID)
```
> يستدعي إضافة messageID إلى مجموعة processedMessages. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:75]

```
76:         messageTimestamps[messageID] = currentTime
```
> يسند القيمة currentTime للمفتاح messageID في خريطة messageTimestamps. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:76]

```
77:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:77]

```
78:         // Enforce mandatory signature verification
```
> تعليق: افرض التحقق الإلزامي من التوقيع. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:78]

```
79:         if (!verifyPacketSignature(packet, peerID)) {
```
> يفحص شرطاً: إذا لم تُرجِع الدالة verifyPacketSignature بالوسيطين packet و peerID قيمة صحيحة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:79]

```
80:             Log.w(TAG, "Dropping packet from $peerID due to signature verification failure")
```
> يكتب رسالة سجلّ تحذير (Log.w) بالوسم TAG ونصها "Dropping packet from" متبوعاً بقيمة peerID ثم "due to signature verification failure". [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:80]

```
81:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:81]

```
82:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:82]

```
83:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:83]

```
84:         Log.d(TAG, "Packet validation passed for $peerID, messageID: $messageID")
```
> يكتب رسالة سجلّ تصحيح بالوسم TAG ونصها "Packet validation passed for" متبوعاً بقيمة peerID ثم "messageID:" وقيمة messageID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:84]

```
85:         return true
```
> يعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:85]

```
86:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:86]

```
87:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:87]

```
88:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:88]

```
89:      * Handle Noise handshake packet - SIMPLIFIED iOS-compatible version
```
> تعليق: عالِج حزمة مصافحة Noise — نسخة مبسّطة متوافقة مع iOS. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:89]

```
90:      * Single handshake type with automatic response handling
```
> تعليق: نوع مصافحة واحد مع معالجة استجابة تلقائية. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:90]

```
91:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:91]

```
92:     suspend fun handleNoiseHandshake(routed: RoutedPacket): Boolean {
```
> يعرّف دالة معلَّقة (suspend) اسمها handleNoiseHandshake (معالجة مصافحة Noise) تأخذ معاملاً routed من نوع RoutedPacket وتعيد قيمة منطقية Boolean. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:92]

```
93:         val packet = routed.packet
```
> يعرّف متغيراً اسمه packet ويسنده إلى الخاصية packet من الكائن routed. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:93]

```
94:         val peerID = routed.peerID ?: "unknown"
```
> يعرّف متغيراً اسمه peerID ويسنده إلى routed.peerID، وإن كان فارغاً فإلى النص "unknown". [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:94]

```
95: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:95]

```
96:         // Skip handshakes not addressed to us
```
> تعليق: تجاوز المصافحات غير الموجَّهة إلينا. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:96]

```
97:         if (packet.recipientID?.toHexString() != myPeerID) {
```
> يفحص شرطاً: إذا كان packet.recipientID محوَّلاً بـ toHexString لا يساوي myPeerID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:97]

```
98:             Log.d(TAG, "Skipping handshake not addressed to us: $peerID")
```
> يكتب رسالة سجلّ تصحيح بالوسم TAG ونصها "Skipping handshake not addressed to us:" متبوعاً بقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:98]

```
99:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:99]

```
100:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:100]

```
101:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:101]

```
102:         // Skip our own handshake messages
```
> تعليق: تجاوز رسائل مصافحتنا الخاصة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:102]

```
103:         if (peerID == myPeerID) return false
```
> يفحص شرطاً: إذا كان peerID يساوي myPeerID فيعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:103]

```
104: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:104]

```
105:         // If we already have an established session but the peer is initiating a new handshake,
```
> تعليق: إن كانت لدينا جلسة قائمة بالفعل لكن النظير يبدأ مصافحة جديدة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:105]

```
106:         // drop the existing session so we can re-establish cleanly.
```
> تعليق: أسقط الجلسة القائمة لكي نعيد التأسيس بنظافة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:106]

```
107:         var forcedRehandshake = false
```
> يعرّف متغيراً اسمه forcedRehandshake (إعادة مصافحة مفروضة) ويسنده ابتداءً إلى false. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:107]

```
108:         if (encryptionService.hasEstablishedSession(peerID)) {
```
> يفحص شرطاً: إذا أعادت encryptionService.hasEstablishedSession للوسيط peerID قيمة صحيحة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:108]

```
109:             Log.d(TAG, "Received new Noise handshake from $peerID with an existing session. Dropping old session to re-handshake.")
```
> يكتب رسالة سجلّ تصحيح بالوسم TAG ونصها "Received new Noise handshake from" متبوعاً بقيمة peerID ثم "with an existing session. Dropping old session to re-handshake.". [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:109]

```
110:             try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:110]

```
111:                 encryptionService.removePeer(peerID)
```
> يستدعي encryptionService.removePeer بالوسيط peerID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:111]

```
112:                 forcedRehandshake = true
```
> يسند القيمة true للمتغير forcedRehandshake. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:112]

```
113:             } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) في المتغير e. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:113]

```
114:                 Log.w(TAG, "Failed to remove existing Noise session for $peerID: ${e.message}")
```
> يكتب رسالة سجلّ تحذير بالوسم TAG ونصها "Failed to remove existing Noise session for" متبوعاً بقيمة peerID ثم رسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:114]

```
115:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:115]

```
116:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:116]

```
117:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:117]

```
118:         if (packet.payload.isEmpty()) {
```
> يفحص شرطاً: إذا كانت الحمولة packet.payload فارغة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:118]

```
119:             Log.w(TAG, "Noise handshake packet has empty payload")
```
> يكتب رسالة سجلّ تحذير بالوسم TAG ونصها "Noise handshake packet has empty payload". [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:119]

```
120:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:120]

```
121:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:121]

```
122:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:122]

```
123:         // Prevent duplicate handshake processing
```
> تعليق: امنع معالجة المصافحة المكرَّرة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:123]

```
124:         val exchangeKey = "$peerID-${packet.payload.sliceArray(0 until minOf(16, packet.payload.size)).contentHashCode()}"
```
> يعرّف متغيراً اسمه exchangeKey (مفتاح التبادل) ويسنده إلى نص يجمع peerID وشَرطة ثم قيمة contentHashCode لشريحة من الحمولة من الفهرس 0 حتى أصغر العددين 16 وحجم الحمولة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:124]

```
125:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:125]

```
126:         if (!forcedRehandshake && processedKeyExchanges.contains(exchangeKey)) {
```
> يفحص شرطاً: إذا لم يكن forcedRehandshake صحيحاً وكانت مجموعة processedKeyExchanges تحتوي exchangeKey. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:126]

```
127:             Log.d(TAG, "Already processed handshake: $exchangeKey")
```
> يكتب رسالة سجلّ تصحيح بالوسم TAG ونصها "Already processed handshake:" متبوعاً بقيمة exchangeKey. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:127]

```
128:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:128]

```
129:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:129]

```
130:         Log.d(TAG, "Processing Noise handshake from $peerID (${packet.payload.size} bytes)")
```
> يكتب رسالة سجلّ تصحيح بالوسم TAG ونصها "Processing Noise handshake from" متبوعاً بقيمة peerID وحجم الحمولة packet.payload.size مع كلمة bytes. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:130]

```
131:         processedKeyExchanges.add(exchangeKey)
```
> يستدعي إضافة exchangeKey إلى مجموعة processedKeyExchanges. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:131]

```
132:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:132]

```
133:         try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:133]

```
134:             // Process the Noise handshake through the updated EncryptionService
```
> تعليق: عالِج مصافحة Noise عبر خدمة التشفير المُحدَّثة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:134]

```
135:             val response = encryptionService.processHandshakeMessage(packet.payload, peerID)
```
> يعرّف متغيراً اسمه response (استجابة) ويسنده إلى نتيجة encryptionService.processHandshakeMessage بالوسيطين packet.payload و peerID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:135]

```
136:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:136]

```
137:             if (response != null) {
```
> يفحص شرطاً: إذا كان response لا يساوي null. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:137]

```
138:                 Log.d(TAG, "Successfully processed Noise handshake from $peerID, sending response")
```
> يكتب رسالة سجلّ تصحيح بالوسم TAG ونصها "Successfully processed Noise handshake from" متبوعاً بقيمة peerID ثم "sending response". [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:138]

```
139:                 // Send handshake response through delegate
```
> تعليق: أرسل استجابة المصافحة عبر المفوَّض. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:139]

```
140:                 delegate?.sendHandshakeResponse(peerID, response)
```
> يستدعي على المفوَّض delegate الدالة sendHandshakeResponse بالوسيطين peerID و response، إن لم يكن delegate فارغاً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:140]

```
141:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:141]

```
142:             // Check if session is now established (handshake complete)
```
> تعليق: افحص ما إن أصبحت الجلسة قائمة الآن (اكتملت المصافحة). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:142]

```
143:             if (encryptionService.hasEstablishedSession(peerID)) {
```
> يفحص شرطاً: إذا أعادت encryptionService.hasEstablishedSession للوسيط peerID قيمة صحيحة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:143]

```
144:                 Log.d(TAG, "✅ Noise handshake completed with $peerID")
```
> يكتب رسالة سجلّ تصحيح بالوسم TAG ونصها "✅ Noise handshake completed with" متبوعاً بقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:144]

```
145:                 delegate?.onKeyExchangeCompleted(peerID, packet.payload)
```
> يستدعي على المفوَّض delegate الدالة onKeyExchangeCompleted بالوسيطين peerID و packet.payload، إن لم يكن delegate فارغاً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:145]

```
146:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:146]

```
147:             return true
```
> يعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:147]

```
148: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:148]

```
149:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:149]

```
150:         } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) في المتغير e. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:150]

```
151:             Log.e(TAG, "Failed to process Noise handshake from $peerID: ${e.message}")
```
> يكتب رسالة سجلّ خطأ (Log.e) بالوسم TAG ونصها "Failed to process Noise handshake from" متبوعاً بقيمة peerID ثم رسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:151]

```
152:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:152]

```
153:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:153]

```
154:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:154]

```
155: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:155]

```
156:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:156]

```
157:      * Verify packet signature
```
> تعليق: تحقّق من توقيع الحزمة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:157]

```
158:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:158]

```
159:     fun verifySignature(packet: BitchatPacket, peerID: String): Boolean {
```
> يعرّف الدالة verifySignature (التحقق من التوقيع) التي تأخذ معاملاً packet من نوع BitchatPacket ومعاملاً peerID من نوع String وتعيد قيمة منطقية Boolean. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:159]

```
160:         return packet.signature?.let { signature ->
```
> يعيد نتيجة تطبيق let على packet.signature (إن لم يكن فارغاً) مع تسمية القيمة signature. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:160]

```
161:             try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:161]

```
162:                 val isValid = encryptionService.verify(signature, packet.payload, peerID)
```
> يعرّف متغيراً اسمه isValid (صالح) ويسنده إلى نتيجة encryptionService.verify بالوسائط signature و packet.payload و peerID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:162]

```
163:                 if (!isValid) {
```
> يفحص شرطاً: إذا لم يكن isValid صحيحاً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:163]

```
164:                     Log.w(TAG, "Invalid signature for packet from $peerID")
```
> يكتب رسالة سجلّ تحذير بالوسم TAG ونصها "Invalid signature for packet from" متبوعاً بقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:164]

```
165:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:165]

```
166:                 isValid
```
> يُرجع قيمة isValid كنتيجة لكتلة try. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:166]

```
167:             } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) في المتغير e. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:167]

```
168:                 Log.e(TAG, "Failed to verify signature from $peerID: ${e.message}")
```
> يكتب رسالة سجلّ خطأ بالوسم TAG ونصها "Failed to verify signature from" متبوعاً بقيمة peerID ثم رسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:168]

```
169:                 false
```
> يُرجع القيمة false كنتيجة لكتلة catch. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:169]

```
170:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:170]

```
171:         } ?: true // No signature means verification passes
```
> يُكمل تعبير elvis: إن كان packet.signature فارغاً تُرجَع القيمة true، مع تعليق: غياب التوقيع يعني نجاح التحقق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:171]

```
172:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:172]

```
173:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:173]

```
174:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:174]

```
175:      * Sign packet payload
```
> تعليق: وقِّع حمولة الحزمة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:175]

```
176:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:176]

```
177:     fun signPacket(payload: ByteArray): ByteArray? {
```
> يعرّف الدالة signPacket (توقيع الحزمة) التي تأخذ معاملاً payload من نوع ByteArray وتعيد ByteArray قابلاً لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:177]

```
178:         return try {
```
> يعيد نتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:178]

```
179:             encryptionService.sign(payload)
```
> يستدعي encryptionService.sign بالوسيط payload ويُرجع نتيجته. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:179]

```
180:         } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) في المتغير e. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:180]

```
181:             Log.e(TAG, "Failed to sign packet: ${e.message}")
```
> يكتب رسالة سجلّ خطأ بالوسم TAG ونصها "Failed to sign packet:" متبوعاً برسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:181]

```
182:             null
```
> يُرجع القيمة null كنتيجة لكتلة catch. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:182]

```
183:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:183]

```
184:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:184]

```
185:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:185]

```
186:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:186]

```
187:      * Encrypt payload for specific peer
```
> تعليق: شفّر الحمولة لنظير محدَّد. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:187]

```
188:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:188]

```
189:     fun encryptForPeer(data: ByteArray, recipientPeerID: String): ByteArray? {
```
> يعرّف الدالة encryptForPeer (التشفير لنظير) التي تأخذ معاملاً data من نوع ByteArray ومعاملاً recipientPeerID من نوع String وتعيد ByteArray قابلاً لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:189]

```
190:         return try {
```
> يعيد نتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:190]

```
191:             encryptionService.encrypt(data, recipientPeerID)
```
> يستدعي encryptionService.encrypt بالوسيطين data و recipientPeerID ويُرجع نتيجته. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:191]

```
192:         } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) في المتغير e. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:192]

```
193:             Log.e(TAG, "Failed to encrypt for $recipientPeerID: ${e.message}")
```
> يكتب رسالة سجلّ خطأ بالوسم TAG ونصها "Failed to encrypt for" متبوعاً بقيمة recipientPeerID ثم رسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:193]

```
194:             null
```
> يُرجع القيمة null كنتيجة لكتلة catch. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:194]

```
195:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:195]

```
196:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:196]

```
197:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:197]

```
198:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:198]

```
199:      * Decrypt payload from specific peer
```
> تعليق: فُكَّ تشفير الحمولة من نظير محدَّد. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:199]

```
200:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:200]
