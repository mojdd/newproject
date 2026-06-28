# شريحة — app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.sync
```
> يُعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.sync. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف Log من android.util ليُستعمل في الطباعة للسجل. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:3]

```
4: import com.bitchat.android.mesh.BluetoothPacketBroadcaster
```
> يستورد الصنف BluetoothPacketBroadcaster (باثّ حزم البلوتوث) من حزمة mesh. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:4]

```
5: import com.bitchat.android.model.RequestSyncPacket
```
> يستورد الصنف RequestSyncPacket (حزمة طلب المزامنة) من حزمة model. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:5]

```
6: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف BitchatPacket (حزمة بِتشات) من حزمة protocol. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:6]

```
7: import com.bitchat.android.protocol.MessageType
```
> يستورد الصنف MessageType (نوع الرسالة) من حزمة protocol. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:7]

```
8: import com.bitchat.android.protocol.SpecialRecipients
```
> يستورد الصنف SpecialRecipients (المستلِمون الخاصون) من حزمة protocol. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:8]

```
9: import kotlinx.coroutines.*
```
> يستورد كل عناصر حزمة kotlinx.coroutines (الكوروتينات) باستعمال النجمة. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:9]

```
10: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف ConcurrentHashMap (خريطة تجزئة متزامنة) من java.util.concurrent. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:11]

```
12: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:12]

```
13:  * Gossip-based synchronization manager using on-demand GCS filters.
```
> تعليق: مدير مزامنة قائم على النميمة (Gossip) يستعمل مرشّحات GCS عند الطلب. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:13]

```
14:  * Tracks seen public packets (ANNOUNCE, broadcast MESSAGE) and periodically requests sync
```
> تعليق: يتتبّع الحزم العامة المرئية (ANNOUNCE، ورسالة MESSAGE البثّية) ويطلب المزامنة دورياً. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:14]

```
15:  * from neighbors. Responds to REQUEST_SYNC by sending missing packets.
```
> تعليق: من الجيران. يستجيب لطلب REQUEST_SYNC بإرسال الحزم المفقودة. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:15]

```
16:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:16]

```
17: class GossipSyncManager(
```
> يُعرّف الصنف GossipSyncManager (مدير مزامنة النميمة) مع بداية قائمة وُسطاء الباني. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:17]

```
18:     private val myPeerID: String,
```
> يُعرّف وسيطاً خاصاً ثابتاً اسمه myPeerID (معرّف نظيري) من نوع String. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:18]

```
19:     private val scope: CoroutineScope,
```
> يُعرّف وسيطاً خاصاً ثابتاً اسمه scope (نطاق) من نوع CoroutineScope. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:19]

```
20:     private val configProvider: ConfigProvider
```
> يُعرّف وسيطاً خاصاً ثابتاً اسمه configProvider (مزوّد الإعدادات) من نوع ConfigProvider. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:20]

```
21: ) {
```
> إغلاق قائمة وُسطاء الباني وبداية جسم الصنف. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:21]

```
22:     interface Delegate {
```
> يُعرّف واجهة (interface) داخلية اسمها Delegate (المفوّض). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:22]

```
23:         fun sendPacket(packet: BitchatPacket)
```
> يُصرّح بدالة sendPacket تأخذ وسيطاً packet من نوع BitchatPacket دون جسم. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:23]

```
24:         fun sendPacketToPeer(peerID: String, packet: BitchatPacket)
```
> يُصرّح بدالة sendPacketToPeer تأخذ peerID من نوع String و packet من نوع BitchatPacket دون جسم. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:24]

```
25:         fun signPacketForBroadcast(packet: BitchatPacket): BitchatPacket
```
> يُصرّح بدالة signPacketForBroadcast تأخذ packet من نوع BitchatPacket وتُعيد BitchatPacket دون جسم. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:25]

```
26:     }
```
> إغلاق نطاق واجهة Delegate. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:27]

```
28:     interface ConfigProvider {
```
> يُعرّف واجهة داخلية اسمها ConfigProvider (مزوّد الإعدادات). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:28]

```
29:         fun seenCapacity(): Int // max packets we sync per request (cap across types)
```
> يُصرّح بدالة seenCapacity تُعيد Int، مع تعليق: أقصى عدد حزم نزامنها لكل طلب (سقف عبر الأنواع). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:29]

```
30:         fun gcsMaxBytes(): Int
```
> يُصرّح بدالة gcsMaxBytes تُعيد Int دون جسم. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:30]

```
31:         fun gcsTargetFpr(): Double // percent -> 0.0..1.0
```
> يُصرّح بدالة gcsTargetFpr تُعيد Double، مع تعليق: نسبة مئوية تتحوّل إلى مدى 0.0..1.0. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:31]

```
32:     }
```
> إغلاق نطاق واجهة ConfigProvider. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:33]

```
34:     companion object {
```
> يُعرّف كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:34]

```
35:         private const val TAG = "GossipSyncManager"
```
> يُعرّف ثابتاً خاصاً اسمه TAG (وسم) قيمته السلسلة "GossipSyncManager". [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:35]

```
36:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:36]

```
37: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:37]

```
38:     var delegate: Delegate? = null
```
> يُعرّف خاصية متغيّرة اسمها delegate (المفوّض) من نوع Delegate القابل للعدم، قيمتها الابتدائية null. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:38]

```
39: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:39]

```
40:     // Defaults (configurable constants)
```
> تعليق: قيم افتراضية (ثوابت قابلة للضبط). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:40]

```
41:     private val defaultMaxBytes = SyncDefaults.DEFAULT_FILTER_BYTES
```
> يُعرّف ثابتاً خاصاً اسمه defaultMaxBytes (أقصى بايتات افتراضي) قيمته SyncDefaults.DEFAULT_FILTER_BYTES. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:41]

```
42:     private val defaultFpr = SyncDefaults.DEFAULT_FPR_PERCENT
```
> يُعرّف ثابتاً خاصاً اسمه defaultFpr (معدل إيجابي خاطئ افتراضي) قيمته SyncDefaults.DEFAULT_FPR_PERCENT. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:42]

```
43: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:43]

```
44:     // Stored packets for sync:
```
> تعليق: حزم مخزّنة للمزامنة. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:44]

```
45:     // - broadcast messages: keep up to seenCapacity() most recent, keyed by packetId
```
> تعليق: الرسائل البثّية: الاحتفاظ بحد أقصى seenCapacity() من الأحدث، مُفتَّحة بمعرّف الحزمة packetId. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:45]

```
46:     private val messages = LinkedHashMap<String, BitchatPacket>()
```
> يُعرّف ثابتاً خاصاً اسمه messages (رسائل) من نوع LinkedHashMap بمفتاح String وقيمة BitchatPacket، مهيّأ فارغاً. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:46]

```
47:     // - announcements: only keep latest per sender peerID
```
> تعليق: الإعلانات: الاحتفاظ فقط بالأحدث لكل معرّف مُرسِل peerID. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:47]

```
48:     private val latestAnnouncementByPeer = ConcurrentHashMap<String, Pair<String, BitchatPacket>>()
```
> يُعرّف ثابتاً خاصاً اسمه latestAnnouncementByPeer (أحدث إعلان لكل نظير) من نوع ConcurrentHashMap بمفتاح String وقيمة Pair من String و BitchatPacket، مهيّأ فارغاً. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:48]

```
49: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:49]

```
50:     private var periodicJob: Job? = null
```
> يُعرّف متغيّراً خاصاً اسمه periodicJob (مهمة دورية) من نوع Job القابل للعدم، قيمته الابتدائية null. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:50]

```
51:     private var cleanupJob: Job? = null
```
> يُعرّف متغيّراً خاصاً اسمه cleanupJob (مهمة تنظيف) من نوع Job القابل للعدم، قيمته الابتدائية null. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:51]

```
52:     fun start() {
```
> يُعرّف دالة عامة اسمها start (بدء) بلا وُسطاء، مع بداية جسمها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:52]

```
53:         periodicJob?.cancel()
```
> يستدعي cancel على periodicJob إن لم يكن null لإلغائه. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:53]

```
54:         periodicJob = scope.launch(Dispatchers.IO) {
```
> يُسنِد إلى periodicJob نتيجة scope.launch على المرسِل Dispatchers.IO مع بداية كتلة الكوروتين. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:54]

```
55:             while (isActive) {
```
> يبدأ حلقة while تستمر طالما isActive صحيح. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:55]

```
56:                 try {
```
> يبدأ كتلة try. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:56]

```
57:                     delay(30_000)
```
> يستدعي delay بقيمة 30000 (مللي ثانية) للتأخير. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:57]

```
58:                     sendRequestSync()
```
> يستدعي الدالة sendRequestSync (إرسال طلب المزامنة). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:58]

```
59:                 } catch (e: CancellationException) { throw e }
```
> يلتقط الاستثناء e من نوع CancellationException ويعيد رميه عبر throw e. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:59]

```
60:                 catch (e: Exception) { Log.e(TAG, "Periodic sync error: ${e.message}") }
```
> يلتقط الاستثناء e من نوع Exception ويطبع خطأ عبر Log.e بالوسم TAG والنص "Periodic sync error: " متبوعاً برسالة الاستثناء. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:60]

```
61:             }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:61]

```
62:         }
```
> إغلاق نطاق كتلة الكوروتين الخاصة بـ periodicJob. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:62]

```
63: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:63]

```
64:         // Start periodic cleanup of stale announcements and messages
```
> تعليق: بدء تنظيف دوري للإعلانات والرسائل القديمة. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:64]

```
65:         cleanupJob?.cancel()
```
> يستدعي cancel على cleanupJob إن لم يكن null لإلغائه. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:65]

```
66:         cleanupJob = scope.launch(Dispatchers.IO) {
```
> يُسنِد إلى cleanupJob نتيجة scope.launch على المرسِل Dispatchers.IO مع بداية كتلة الكوروتين. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:66]

```
67:             while (isActive) {
```
> يبدأ حلقة while تستمر طالما isActive صحيح. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:67]

```
68:                 try {
```
> يبدأ كتلة try. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:68]

```
69:                     delay(com.bitchat.android.util.AppConstants.Sync.CLEANUP_INTERVAL_MS)
```
> يستدعي delay بقيمة الثابت com.bitchat.android.util.AppConstants.Sync.CLEANUP_INTERVAL_MS (فترة التنظيف بالمللي ثانية). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:69]

```
70:                     pruneStaleAnnouncements()
```
> يستدعي الدالة pruneStaleAnnouncements (تقليم الإعلانات القديمة). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:70]

```
71:                 } catch (e: CancellationException) { throw e }
```
> يلتقط الاستثناء e من نوع CancellationException ويعيد رميه عبر throw e. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:71]

```
72:                 catch (e: Exception) { Log.e(TAG, "Periodic cleanup error: ${e.message}") }
```
> يلتقط الاستثناء e من نوع Exception ويطبع خطأ عبر Log.e بالوسم TAG والنص "Periodic cleanup error: " متبوعاً برسالة الاستثناء. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:72]

```
73:             }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:73]

```
74:         }
```
> إغلاق نطاق كتلة الكوروتين الخاصة بـ cleanupJob. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:74]

```
75:     }
```
> إغلاق نطاق الدالة start. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:75]

```
76: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:76]

```
77:     fun stop() {
```
> يُعرّف دالة عامة اسمها stop (إيقاف) بلا وُسطاء، مع بداية جسمها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:77]

```
78:         periodicJob?.cancel(); periodicJob = null
```
> يستدعي cancel على periodicJob إن لم يكن null، ثم يُسنِد إليه null. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:78]

```
79:         cleanupJob?.cancel(); cleanupJob = null
```
> يستدعي cancel على cleanupJob إن لم يكن null، ثم يُسنِد إليه null. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:79]

```
80:     }
```
> إغلاق نطاق الدالة stop. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:80]

```
81: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:81]

```
82:     fun scheduleInitialSync(delayMs: Long = 5_000L) {
```
> يُعرّف دالة عامة اسمها scheduleInitialSync (جدولة المزامنة الأولية) بوسيط delayMs من نوع Long قيمته الافتراضية 5000، مع بداية جسمها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:82]

```
83:         scope.launch(Dispatchers.IO) {
```
> يستدعي scope.launch على المرسِل Dispatchers.IO مع بداية كتلة الكوروتين. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:83]

```
84:             delay(delayMs)
```
> يستدعي delay بقيمة الوسيط delayMs للتأخير. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:84]

```
85:             sendRequestSync()
```
> يستدعي الدالة sendRequestSync. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:85]

```
86:         }
```
> إغلاق نطاق كتلة الكوروتين. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:86]

```
87:     }
```
> إغلاق نطاق الدالة scheduleInitialSync. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:87]

```
88: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:88]

```
89:     fun scheduleInitialSyncToPeer(peerID: String, delayMs: Long = 5_000L) {
```
> يُعرّف دالة عامة اسمها scheduleInitialSyncToPeer (جدولة المزامنة الأولية إلى نظير) بوسيط peerID من نوع String و delayMs من نوع Long قيمته الافتراضية 5000، مع بداية جسمها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:89]

```
90:         scope.launch(Dispatchers.IO) {
```
> يستدعي scope.launch على المرسِل Dispatchers.IO مع بداية كتلة الكوروتين. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:90]

```
91:             delay(delayMs)
```
> يستدعي delay بقيمة الوسيط delayMs للتأخير. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:91]

```
92:             sendRequestSyncToPeer(peerID)
```
> يستدعي الدالة sendRequestSyncToPeer بالوسيط peerID. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:92]

```
93:         }
```
> إغلاق نطاق كتلة الكوروتين. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:93]

```
94:     }
```
> إغلاق نطاق الدالة scheduleInitialSyncToPeer. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:94]

```
95: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:95]

```
96:     fun onPublicPacketSeen(packet: BitchatPacket) {
```
> يُعرّف دالة عامة اسمها onPublicPacketSeen (عند رؤية حزمة عامة) بوسيط packet من نوع BitchatPacket، مع بداية جسمها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:96]

```
97:         // Only ANNOUNCE or broadcast MESSAGE
```
> تعليق: فقط ANNOUNCE أو رسالة MESSAGE البثّية. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:97]

```
98:         val mt = MessageType.fromValue(packet.type)
```
> يُعرّف ثابتاً محلياً اسمه mt قيمته نتيجة MessageType.fromValue على packet.type. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:98]

```
99:         val isBroadcastMessage = (mt == MessageType.MESSAGE && (packet.recipientID == null || packet.recipientID.contentEquals(SpecialRecipients.BROADCAST)))
```
> يُعرّف ثابتاً محلياً اسمه isBroadcastMessage قيمته صحيحة عندما يساوي mt القيمة MessageType.MESSAGE ويكون packet.recipientID إمّا null أو مطابقاً محتوى SpecialRecipients.BROADCAST. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:99]

```
100:         val isAnnouncement = (mt == MessageType.ANNOUNCE)
```
> يُعرّف ثابتاً محلياً اسمه isAnnouncement قيمته صحيحة عندما يساوي mt القيمة MessageType.ANNOUNCE. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:100]

```
101:         if (!isBroadcastMessage && !isAnnouncement) return
```
> يُعيد (return) من الدالة إذا لم يكن isBroadcastMessage ولا isAnnouncement صحيحاً. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:101]

```
102: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:102]

```
103:         val idBytes = PacketIdUtil.computeIdBytes(packet)
```
> يُعرّف ثابتاً محلياً اسمه idBytes (بايتات المعرّف) قيمته نتيجة PacketIdUtil.computeIdBytes على packet. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:103]

```
104:         val id = idBytes.joinToString("") { b -> "%02x".format(b) }
```
> يُعرّف ثابتاً محلياً اسمه id قيمته دمج بايتات idBytes في سلسلة بلا فاصل، حيث يُنسَّق كل بايت b بصيغة ست عشرية بخانتين "%02x". [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:104]

```
105: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:105]

```
106:         if (isBroadcastMessage) {
```
> يبدأ كتلة if مشروطة بكون isBroadcastMessage صحيحاً. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:106]

```
107:             synchronized(messages) {
```
> يبدأ كتلة synchronized تتزامن على الكائن messages. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:107]

```
108:                 messages[id] = packet
```
> يُسنِد packet إلى الخريطة messages عند المفتاح id. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:108]

```
109:                 // Enforce capacity (remove oldest when exceeded)
```
> تعليق: فرض السعة (إزالة الأقدم عند التجاوز). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:109]

```
110:                 val cap = configProvider.seenCapacity().coerceAtLeast(1)
```
> يُعرّف ثابتاً محلياً اسمه cap (سعة) قيمته نتيجة configProvider.seenCapacity() مقيّدة بحد أدنى 1 عبر coerceAtLeast. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:110]

```
111:                 while (messages.size > cap) {
```
> يبدأ حلقة while تستمر طالما حجم messages أكبر من cap. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:111]

```
112:                     val it = messages.entries.iterator()
```
> يُعرّف ثابتاً محلياً اسمه it (مُكرِّر) قيمته مُكرِّر مدخلات messages.entries. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:112]

```
113:                     if (it.hasNext()) { it.next(); it.remove() } else break
```
> إذا كان للمكرّر عنصر تالٍ via hasNext فإنه يتقدّم بـ next ثم يزيل العنصر بـ remove، وإلّا يكسر الحلقة بـ break. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:113]

```
114:                 }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:114]

```
115:             }
```
> إغلاق نطاق كتلة synchronized. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:115]

```
116:         } else if (isAnnouncement) {
```
> يبدأ فرع else if مشروطاً بكون isAnnouncement صحيحاً. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:116]

```
117:             // Ignore stale announcements older than STALE_PEER_TIMEOUT
```
> تعليق: تجاهل الإعلانات القديمة الأقدم من STALE_PEER_TIMEOUT. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:117]

```
118:             val now = System.currentTimeMillis()
```
> يُعرّف ثابتاً محلياً اسمه now (الآن) قيمته الوقت الحالي بالمللي ثانية عبر System.currentTimeMillis(). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:118]

```
119:             val age = now - packet.timestamp.toLong()
```
> يُعرّف ثابتاً محلياً اسمه age (عُمر) قيمته now ناقص packet.timestamp محوَّلاً إلى Long. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:119]

```
120:             if (age > com.bitchat.android.util.AppConstants.Mesh.STALE_PEER_TIMEOUT_MS) {
```
> يبدأ كتلة if مشروطة بكون age أكبر من الثابت com.bitchat.android.util.AppConstants.Mesh.STALE_PEER_TIMEOUT_MS. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:120]

```
121:                 Log.d(TAG, "Ignoring stale ANNOUNCE (age=${age}ms > ${com.bitchat.android.util.AppConstants.Mesh.STALE_PEER_TIMEOUT_MS}ms)")
```
> يطبع تصحيحاً عبر Log.d بالوسم TAG والنص "Ignoring stale ANNOUNCE" متضمّناً قيمة age بالمللي ثانية وقيمة الثابت STALE_PEER_TIMEOUT_MS بالمللي ثانية. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:121]

```
122:                 return
```
> يُعيد (return) من الدالة. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:122]

```
123:             }
```
> إغلاق نطاق كتلة if الخاصة بالعُمر. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:123]

```
124:             // senderID is fixed-size 8 bytes; map to hex string for key
```
> تعليق: senderID بحجم ثابت 8 بايتات؛ يُحوَّل إلى سلسلة ست عشرية لتكون مفتاحاً. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:124]

```
125:             val sender = packet.senderID.joinToString("") { b -> "%02x".format(b) }
```
> يُعرّف ثابتاً محلياً اسمه sender (مُرسِل) قيمته دمج packet.senderID في سلسلة بلا فاصل، حيث يُنسَّق كل بايت b بصيغة ست عشرية بخانتين "%02x". [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:125]

```
126:             latestAnnouncementByPeer[sender] = id to packet
```
> يُسنِد إلى latestAnnouncementByPeer عند المفتاح sender الزوجَ المكوَّن من id و packet عبر to. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:126]

```
127:             // Enforce capacity (remove oldest when exceeded)
```
> تعليق: فرض السعة (إزالة الأقدم عند التجاوز). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:127]

```
128:             val cap = configProvider.seenCapacity().coerceAtLeast(1)
```
> يُعرّف ثابتاً محلياً اسمه cap قيمته نتيجة configProvider.seenCapacity() مقيّدة بحد أدنى 1 عبر coerceAtLeast. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:128]

```
129:             while (latestAnnouncementByPeer.size > cap) {
```
> يبدأ حلقة while تستمر طالما حجم latestAnnouncementByPeer أكبر من cap. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:129]

```
130:                 val it = latestAnnouncementByPeer.entries.iterator()
```
> يُعرّف ثابتاً محلياً اسمه it قيمته مُكرِّر مدخلات latestAnnouncementByPeer.entries. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:130]

```
131:                 if (it.hasNext()) { it.next(); it.remove() } else break
```
> إذا كان للمكرّر عنصر تالٍ via hasNext فإنه يتقدّم بـ next ثم يزيل العنصر بـ remove، وإلّا يكسر الحلقة بـ break. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:131]

```
132:             }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:132]

```
133:         }
```
> إغلاق نطاق فرع else if الخاص بالإعلان. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:133]

```
134:     }
```
> إغلاق نطاق الدالة onPublicPacketSeen. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:134]

```
135: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:135]

```
136:     private fun sendRequestSync() {
```
> يُعرّف دالة خاصة اسمها sendRequestSync (إرسال طلب المزامنة) بلا وُسطاء، مع بداية جسمها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:136]

```
137:         val payload = buildGcsPayload()
```
> يُعرّف ثابتاً محلياً اسمه payload (حمولة) قيمته نتيجة buildGcsPayload(). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:137]

```
138: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:138]

```
139:         val packet = BitchatPacket(
```
> يُعرّف ثابتاً محلياً اسمه packet قيمته كائن BitchatPacket جديد مع بداية قائمة وُسطائه. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:139]

```
140:             type = MessageType.REQUEST_SYNC.value,
```
> يضبط الوسيط type على قيمة MessageType.REQUEST_SYNC.value. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:140]

```
141:             senderID = hexStringToByteArray(myPeerID),
```
> يضبط الوسيط senderID على نتيجة hexStringToByteArray بالوسيط myPeerID. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:141]

```
142:             timestamp = System.currentTimeMillis().toULong(),
```
> يضبط الوسيط timestamp على الوقت الحالي بالمللي ثانية محوَّلاً إلى ULong. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:142]

```
143:             payload = payload,
```
> يضبط الوسيط payload على الثابت المحلي payload. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:143]

```
144:             ttl = com.bitchat.android.util.AppConstants.SYNC_TTL_HOPS // neighbors only
```
> يضبط الوسيط ttl على الثابت com.bitchat.android.util.AppConstants.SYNC_TTL_HOPS، مع تعليق: الجيران فقط. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:144]

```
145:         )
```
> إغلاق قائمة وُسطاء باني BitchatPacket. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:145]

```
146:         // Sign and broadcast
```
> تعليق: وقّع وابثّ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:146]

```
147:         val signed = delegate?.signPacketForBroadcast(packet) ?: packet
```
> يُعرّف ثابتاً محلياً اسمه signed (موقَّع) قيمته نتيجة delegate?.signPacketForBroadcast(packet)، أو packet نفسه إن كانت النتيجة null عبر مُشغّل elvis. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:147]

```
148:         delegate?.sendPacket(signed)
```
> يستدعي sendPacket بالوسيط signed على delegate إن لم يكن null. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:148]

```
149:     }
```
> إغلاق نطاق الدالة sendRequestSync. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:149]

```
150: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:150]

```
151:     private fun sendRequestSyncToPeer(peerID: String) {
```
> يُعرّف دالة خاصة اسمها sendRequestSyncToPeer (إرسال طلب المزامنة إلى نظير) بوسيط peerID من نوع String، مع بداية جسمها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:151]

```
152:         val payload = buildGcsPayload()
```
> يُعرّف ثابتاً محلياً اسمه payload قيمته نتيجة buildGcsPayload(). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:152]

```
153: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:153]

```
154:         val packet = BitchatPacket(
```
> يُعرّف ثابتاً محلياً اسمه packet قيمته كائن BitchatPacket جديد مع بداية قائمة وُسطائه. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:154]

```
155:             type = MessageType.REQUEST_SYNC.value,
```
> يضبط الوسيط type على قيمة MessageType.REQUEST_SYNC.value. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:155]

```
156:             senderID = hexStringToByteArray(myPeerID),
```
> يضبط الوسيط senderID على نتيجة hexStringToByteArray بالوسيط myPeerID. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:156]

```
157:             recipientID = hexStringToByteArray(peerID),
```
> يضبط الوسيط recipientID على نتيجة hexStringToByteArray بالوسيط peerID. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:157]

```
158:             timestamp = System.currentTimeMillis().toULong(),
```
> يضبط الوسيط timestamp على الوقت الحالي بالمللي ثانية محوَّلاً إلى ULong. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:158]

```
159:             payload = payload,
```
> يضبط الوسيط payload على الثابت المحلي payload. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:159]

```
160:             ttl = com.bitchat.android.util.AppConstants.SYNC_TTL_HOPS // neighbor only
```
> يضبط الوسيط ttl على الثابت com.bitchat.android.util.AppConstants.SYNC_TTL_HOPS، مع تعليق: الجار فقط. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:160]

```
161:         )
```
> إغلاق قائمة وُسطاء باني BitchatPacket. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:161]

```
162:         Log.d(TAG, "Sending sync request to $peerID (${payload.size} bytes)")
```
> يطبع تصحيحاً عبر Log.d بالوسم TAG والنص "Sending sync request to" متضمّناً peerID وحجم payload بالبايتات. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:162]

```
163:         // Sign and send directly to peer
```
> تعليق: وقّع وأرسل مباشرة إلى النظير. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:163]

```
164:         val signed = delegate?.signPacketForBroadcast(packet) ?: packet
```
> يُعرّف ثابتاً محلياً اسمه signed قيمته نتيجة delegate?.signPacketForBroadcast(packet)، أو packet نفسه إن كانت النتيجة null عبر مُشغّل elvis. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:164]

```
165:         delegate?.sendPacketToPeer(peerID, signed)
```
> يستدعي sendPacketToPeer بالوسيطين peerID و signed على delegate إن لم يكن null. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:165]

```
166:     }
```
> إغلاق نطاق الدالة sendRequestSyncToPeer. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:166]

```
167: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:167]

```
168:     fun handleRequestSync(fromPeerID: String, request: RequestSyncPacket) {
```
> يُعرّف دالة عامة اسمها handleRequestSync (معالجة طلب المزامنة) بوسيط fromPeerID من نوع String و request من نوع RequestSyncPacket، مع بداية جسمها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:168]

```
169:         // Decode GCS into sorted set for membership checks
```
> تعليق: فكّ ترميز GCS إلى مجموعة مرتّبة لفحوص العضوية. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:169]

```
170:         val sorted = GCSFilter.decodeToSortedSet(request.p, request.m, request.data)
```
> يُعرّف ثابتاً محلياً اسمه sorted (مرتّبة) قيمته نتيجة GCSFilter.decodeToSortedSet على الوُسطاء request.p و request.m و request.data. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:170]

```
171:         fun mightContain(id: ByteArray): Boolean {
```
> يُعرّف دالة محلية اسمها mightContain (قد يحتوي) بوسيط id من نوع ByteArray وتُعيد Boolean، مع بداية جسمها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:171]

```
172:             val v = GCSFilter.h64(id) % request.m
```
> يُعرّف ثابتاً محلياً اسمه v قيمته باقي قسمة GCSFilter.h64(id) على request.m. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:172]

```
173:             val nonZeroV = if (v == 0L) 1L else v
```
> يُعرّف ثابتاً محلياً اسمه nonZeroV (قيمة غير صفرية) قيمته 1 إذا كان v يساوي 0، وإلّا v نفسه. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:173]

```
174:             return GCSFilter.contains(sorted, nonZeroV)
```
> يُعيد نتيجة GCSFilter.contains على المجموعة sorted والقيمة nonZeroV. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:174]

```
175:         }
```
> إغلاق نطاق الدالة المحلية mightContain. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:175]

```
176: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:176]

```
177:         // 1) Announcements: send latest per peerID if remote doesn't have them
```
> تعليق: 1) الإعلانات: أرسل الأحدث لكل peerID إذا لم يملكها الطرف البعيد. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:177]

```
178:         for ((_, pair) in latestAnnouncementByPeer.entries) {
```
> يبدأ حلقة for على مدخلات latestAnnouncementByPeer.entries، متجاهلاً المفتاح بـ _ ومسمّياً القيمة pair. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:178]

```
179:             val (id, pkt) = pair
```
> يُفكّك الزوج pair إلى ثابتين محليين id و pkt. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:179]

```
180:             val idBytes = hexToBytes(id)
```
> يُعرّف ثابتاً محلياً اسمه idBytes قيمته نتيجة hexToBytes على id. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:180]

```
181:             if (!mightContain(idBytes)) {
```
> يبدأ كتلة if مشروطة بأنّ mightContain(idBytes) يُعيد قيمة غير صحيحة (أي لا يحتوي). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:181]

```
182:                 // Send original packet unchanged to requester only (keep local TTL)
```
> تعليق: أرسل الحزمة الأصلية دون تغيير إلى الطالب فقط (احتفظ بـ TTL المحلي). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:182]

```
183:                 val toSend = pkt.copy(ttl = com.bitchat.android.util.AppConstants.SYNC_TTL_HOPS)
```
> يُعرّف ثابتاً محلياً اسمه toSend (للإرسال) قيمته نسخة من pkt عبر copy مع ضبط ttl على الثابت com.bitchat.android.util.AppConstants.SYNC_TTL_HOPS. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:183]

```
184:                 delegate?.sendPacketToPeer(fromPeerID, toSend)
```
> يستدعي sendPacketToPeer بالوسيطين fromPeerID و toSend على delegate إن لم يكن null. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:184]

```
185:                 Log.d(TAG, "Sent sync announce: Type ${toSend.type} from ${toSend.senderID.toHexString()} to $fromPeerID packet id ${idBytes.toHexString()}")
```
> يطبع تصحيحاً عبر Log.d بالوسم TAG والنص "Sent sync announce" متضمّناً toSend.type و toSend.senderID بصيغة ست عشرية عبر toHexString و fromPeerID و idBytes بصيغة ست عشرية عبر toHexString. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:185]

```
186:             }
```
> إغلاق نطاق كتلة if الخاصة بالإعلان. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:186]

```
187:         }
```
> إغلاق نطاق حلقة for الخاصة بالإعلانات. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:187]

```
188: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:188]

```
189:         // 2) Broadcast messages: send all they lack
```
> تعليق: 2) الرسائل البثّية: أرسل كل ما ينقصهم. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:189]

```
190:         val toSendMsgs = synchronized(messages) { messages.values.toList() }
```
> يُعرّف ثابتاً محلياً اسمه toSendMsgs (رسائل للإرسال) قيمته قائمة من قيم messages عبر toList ضمن كتلة synchronized متزامنة على messages. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:190]

```
191:         for (pkt in toSendMsgs) {
```
> يبدأ حلقة for تكرّر على عناصر toSendMsgs مسمّياً كلّاً pkt. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:191]

```
192:             val idBytes = PacketIdUtil.computeIdBytes(pkt)
```
> يُعرّف ثابتاً محلياً اسمه idBytes قيمته نتيجة PacketIdUtil.computeIdBytes على pkt. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:192]

```
193:             if (!mightContain(idBytes)) {
```
> يبدأ كتلة if مشروطة بأنّ mightContain(idBytes) يُعيد قيمة غير صحيحة (أي لا يحتوي). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:193]

```
194:                 val toSend = pkt.copy(ttl = com.bitchat.android.util.AppConstants.SYNC_TTL_HOPS)
```
> يُعرّف ثابتاً محلياً اسمه toSend قيمته نسخة من pkt عبر copy مع ضبط ttl على الثابت com.bitchat.android.util.AppConstants.SYNC_TTL_HOPS. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:194]

```
195:                 delegate?.sendPacketToPeer(fromPeerID, toSend)
```
> يستدعي sendPacketToPeer بالوسيطين fromPeerID و toSend على delegate إن لم يكن null. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:195]

```
196:                 Log.d(TAG, "Sent sync message: Type ${toSend.type} to $fromPeerID packet id ${idBytes.toHexString()}")
```
> يطبع تصحيحاً عبر Log.d بالوسم TAG والنص "Sent sync message" متضمّناً toSend.type و fromPeerID و idBytes بصيغة ست عشرية عبر toHexString. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:196]

```
197:             }
```
> إغلاق نطاق كتلة if الخاصة بالرسالة. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:197]

```
198:         }
```
> إغلاق نطاق حلقة for الخاصة بالرسائل. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:198]

```
199:     }
```
> إغلاق نطاق الدالة handleRequestSync. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:199]

```
200: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:200]
