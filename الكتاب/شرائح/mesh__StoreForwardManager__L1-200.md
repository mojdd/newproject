# شريحة — app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يُعرّف اسم الحزمة (package) بأنها com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:2]

```
3: import android.util.Log
```
> يستورد (import) صنف android.util.Log. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:3]

```
4: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد صنف الرزمة (BitchatPacket) من com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:4]

```
5: import com.bitchat.android.protocol.MessageType
```
> يستورد صنف نوع الرسالة (MessageType) من com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:5]

```
6: import com.bitchat.android.protocol.SpecialRecipients
```
> يستورد صنف المستلمين الخاصّين (SpecialRecipients) من com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:6]

```
7: import kotlinx.coroutines.*
```
> يستورد كل أعضاء حزمة الكوروتينات (kotlinx.coroutines). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:7]

```
8: import java.util.*
```
> يستورد كل أعضاء حزمة java.util. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:8]

```
9: import java.util.concurrent.ConcurrentHashMap
```
> يستورد صنف الخريطة المتزامنة (ConcurrentHashMap) من java.util.concurrent. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:9]

```
10: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:10]

```
11: /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:11]

```
12:  * Manages store-and-forward messaging for offline peers
```
> تعليق: يدير مراسلة التخزين والتمرير (store-and-forward) للأقران غير المتصلين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:12]

```
13:  * Extracted from BluetoothMeshService for better separation of concerns
```
> تعليق: مُستخرَج من BluetoothMeshService لفصل أفضل للاهتمامات. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:13]

```
14:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:14]

```
15: class StoreForwardManager {
```
> يُعرّف صنف مدير التخزين والتمرير (StoreForwardManager) ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:15]

```
16:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:16]

```
17:     companion object {
```
> يفتح كائن المرافقة (companion object). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:17]

```
18:         private const val TAG = "StoreForwardManager"
```
> يُعرّف ثابتاً خاصاً TAG ويضبط قيمته إلى السلسلة "StoreForwardManager". [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:18]

```
19:         private const val MESSAGE_CACHE_TIMEOUT = com.bitchat.android.util.AppConstants.StoreForward.MESSAGE_CACHE_TIMEOUT_MS  // 12 hours for regular peers
```
> يُعرّف ثابتاً خاصاً مهلة ذاكرة الرسائل (MESSAGE_CACHE_TIMEOUT) ويضبط قيمته إلى AppConstants.StoreForward.MESSAGE_CACHE_TIMEOUT_MS. تعليق: ١٢ ساعة للأقران العاديين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:19]

```
20:         private const val MAX_CACHED_MESSAGES = com.bitchat.android.util.AppConstants.StoreForward.MAX_CACHED_MESSAGES  // For regular peers
```
> يُعرّف ثابتاً خاصاً الحد الأقصى للرسائل المخزّنة (MAX_CACHED_MESSAGES) ويضبط قيمته إلى AppConstants.StoreForward.MAX_CACHED_MESSAGES. تعليق: للأقران العاديين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:20]

```
21:         private const val MAX_CACHED_MESSAGES_FAVORITES = com.bitchat.android.util.AppConstants.StoreForward.MAX_CACHED_MESSAGES_FAVORITES  // For favorites
```
> يُعرّف ثابتاً خاصاً الحد الأقصى للرسائل المخزّنة للمفضّلين (MAX_CACHED_MESSAGES_FAVORITES) ويضبط قيمته إلى AppConstants.StoreForward.MAX_CACHED_MESSAGES_FAVORITES. تعليق: للمفضّلين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:21]

```
22:         private const val CLEANUP_INTERVAL = com.bitchat.android.util.AppConstants.StoreForward.CLEANUP_INTERVAL_MS // 10 minutes
```
> يُعرّف ثابتاً خاصاً فترة التنظيف (CLEANUP_INTERVAL) ويضبط قيمته إلى AppConstants.StoreForward.CLEANUP_INTERVAL_MS. تعليق: ١٠ دقائق. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:22]

```
23:     }
```
> إغلاق نطاق كائن المرافقة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:23]

```
24:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:24]

```
25:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:25]

```
26:      * Data class for stored messages
```
> تعليق: صنف بيانات للرسائل المخزّنة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:26]

```
27:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:27]

```
28:     private data class StoredMessage(
```
> يُعرّف صنف بيانات خاصاً الرسالة المخزّنة (StoredMessage) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:28]

```
29:         val packet: BitchatPacket,
```
> يُعرّف خاصية ثابتة packet من نوع الرزمة (BitchatPacket). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:29]

```
30:         val timestamp: Long,
```
> يُعرّف خاصية ثابتة الطابع الزمني (timestamp) من نوع Long. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:30]

```
31:         val messageID: String,
```
> يُعرّف خاصية ثابتة معرّف الرسالة (messageID) من نوع String. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:31]

```
32:         val isForFavorite: Boolean
```
> يُعرّف خاصية ثابتة هل هي لمفضّل (isForFavorite) من نوع Boolean. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:32]

```
33:     )
```
> إغلاق قائمة معاملات صنف البيانات StoredMessage. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:33]

```
34:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:34]

```
35:     // Message storage
```
> تعليق: تخزين الرسائل. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:35]

```
36:     private val messageCache = Collections.synchronizedList(mutableListOf<StoredMessage>())
```
> يُعرّف خاصية ثابتة خاصة ذاكرة الرسائل (messageCache) ويضبطها إلى قائمة متزامنة عبر Collections.synchronizedList تغلّف قائمة قابلة للتعديل من StoredMessage. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:36]

```
37:     private val favoriteMessageQueue = ConcurrentHashMap<String, MutableList<StoredMessage>>()
```
> يُعرّف خاصية ثابتة خاصة طابور رسائل المفضّلين (favoriteMessageQueue) ويضبطها إلى ConcurrentHashMap مفاتيحها String وقيمها قوائم قابلة للتعديل من StoredMessage. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:37]

```
38:     private val deliveredMessages = Collections.synchronizedSet(mutableSetOf<String>())
```
> يُعرّف خاصية ثابتة خاصة الرسائل المُسلَّمة (deliveredMessages) ويضبطها إلى مجموعة متزامنة عبر Collections.synchronizedSet تغلّف مجموعة قابلة للتعديل من String. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:38]

```
39:     private val cachedMessagesSentToPeer = Collections.synchronizedSet(mutableSetOf<String>())
```
> يُعرّف خاصية ثابتة خاصة الرسائل المخزّنة المُرسَلة للقرين (cachedMessagesSentToPeer) ويضبطها إلى مجموعة متزامنة عبر Collections.synchronizedSet تغلّف مجموعة قابلة للتعديل من String. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:39]

```
40:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:40]

```
41:     // Delegate for callbacks
```
> تعليق: المفوَّض لردود النداء. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:41]

```
42:     var delegate: StoreForwardManagerDelegate? = null
```
> يُعرّف خاصية متغيّرة المفوَّض (delegate) من نوع StoreForwardManagerDelegate القابل للإفراغ ويضبط قيمتها الابتدائية إلى null. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:42]

```
43:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:43]

```
44:     // Coroutines
```
> تعليق: الكوروتينات. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:44]

```
45:     private val managerScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يُعرّف خاصية ثابتة خاصة نطاق المدير (managerScope) ويضبطها إلى CoroutineScope مكوَّن من Dispatchers.IO زائد SupervisorJob. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:45]

```
46:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:46]

```
47:     init {
```
> يفتح كتلة التهيئة (init). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:47]

```
48:         startPeriodicCleanup()
```
> يستدعي الدالة startPeriodicCleanup (بدء التنظيف الدوري). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:48]

```
49:     }
```
> إغلاق كتلة التهيئة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:49]

```
50:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:50]

```
51:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:51]

```
52:      * Cache message for offline delivery
```
> تعليق: خزّن الرسالة للتسليم غير المتصل. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:52]

```
53:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:53]

```
54:     fun cacheMessage(packet: BitchatPacket, messageID: String) {
```
> يُعرّف الدالة خزّن الرسالة (cacheMessage) التي تأخذ معامل packet من نوع BitchatPacket ومعامل messageID من نوع String ويفتح جسدها. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:54]

```
55:         // Skip certain message types (same as iOS)
```
> تعليق: تخطَّ أنواعاً معيّنة من الرسائل (مثل iOS). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:55]

```
56:         if (packet.type == MessageType.NOISE_HANDSHAKE.value ||
```
> يبدأ شرط if يقارن packet.type بقيمة MessageType.NOISE_HANDSHAKE.value مع عامل أو منطقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:56]

```
57:             packet.type == MessageType.NOISE_ENCRYPTED.value ||
```
> يتابع الشرط بمقارنة packet.type بقيمة MessageType.NOISE_ENCRYPTED.value مع عامل أو منطقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:57]

```
58:             packet.type == MessageType.ANNOUNCE.value ||
```
> يتابع الشرط بمقارنة packet.type بقيمة MessageType.ANNOUNCE.value مع عامل أو منطقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:58]

```
59:             packet.type == MessageType.LEAVE.value) {
```
> يُنهي الشرط بمقارنة packet.type بقيمة MessageType.LEAVE.value ويفتح جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:59]

```
60:             Log.d(TAG, "Skipping cache for message type: ${packet.type}")
```
> يستدعي Log.d بالوسم TAG ورسالة "Skipping cache for message type:" متبوعة بقيمة packet.type. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:60]

```
61:             return
```
> يُعيد من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:61]

```
62:         }
```
> إغلاق جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:62]

```
63:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:63]

```
64:         // Don't cache broadcast messages
```
> تعليق: لا تخزّن رسائل البثّ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:64]

```
65:         if (packet.recipientID != null && packet.recipientID.contentEquals(SpecialRecipients.BROADCAST)) {
```
> يبدأ شرط if يتحقق أن packet.recipientID ليس null وأنه يساوي بالمحتوى SpecialRecipients.BROADCAST ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:65]

```
66:             Log.d(TAG, "Skipping cache for broadcast message")
```
> يستدعي Log.d بالوسم TAG ورسالة "Skipping cache for broadcast message". [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:66]

```
67:             return
```
> يُعيد من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:67]

```
68:         }
```
> إغلاق جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:68]

```
69:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:69]

```
70:         // Determine if this is for a favorite peer
```
> تعليق: حدّد إن كانت هذه لقرين مفضّل. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:70]

```
71:         val recipientPeerID = packet.recipientID?.let { recipientID ->
```
> يُعرّف ثابتاً معرّف القرين المستلِم (recipientPeerID) ويبدأ تطبيق let على packet.recipientID مع تسمية الوسيط recipientID إن لم يكن null. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:71]

```
72:             String(recipientID).replace(" ", "")
```
> ينشئ سلسلة من recipientID ويستبدل كل محرف null ( ) بسلسلة فارغة كقيمة لـ let. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:72]

```
73:         }
```
> إغلاق كتلة let. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:73]

```
74:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:74]

```
75:         if (recipientPeerID.isNullOrEmpty()) {
```
> يبدأ شرط if يتحقق أن recipientPeerID فارغ أو null عبر isNullOrEmpty ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:75]

```
76:             Log.w(TAG, "Cannot cache message without valid recipient")
```
> يستدعي Log.w بالوسم TAG ورسالة "Cannot cache message without valid recipient". [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:76]

```
77:             return
```
> يُعيد من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:77]

```
78:         }
```
> إغلاق جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:78]

```
79:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:79]

```
80:         val isForFavorite = delegate?.isFavorite(recipientPeerID) ?: false
```
> يُعرّف ثابتاً isForFavorite ويضبطه إلى نتيجة delegate?.isFavorite(recipientPeerID)، وإن كانت null فإلى false عبر عامل إلفيس. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:80]

```
81:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:81]

```
82:         val storedMessage = StoredMessage(
```
> يُعرّف ثابتاً storedMessage ويبدأ إنشاء كائن StoredMessage ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:82]

```
83:             packet = packet,
```
> يمرّر الوسيط packet بقيمة المعامل packet. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:83]

```
84:             timestamp = System.currentTimeMillis(),
```
> يمرّر الوسيط timestamp بقيمة System.currentTimeMillis (الوقت الحالي بالملي ثانية). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:84]

```
85:             messageID = messageID,
```
> يمرّر الوسيط messageID بقيمة المعامل messageID. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:85]

```
86:             isForFavorite = isForFavorite
```
> يمرّر الوسيط isForFavorite بقيمة الثابت isForFavorite. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:86]

```
87:         )
```
> إغلاق قائمة وسائط إنشاء StoredMessage. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:87]

```
88:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:88]

```
89:         if (isForFavorite) {
```
> يبدأ شرط if يتحقق أن isForFavorite صحيح ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:89]

```
90:             // Store in favorite queue
```
> تعليق: خزّن في طابور المفضّلين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:90]

```
91:             if (!favoriteMessageQueue.containsKey(recipientPeerID)) {
```
> يبدأ شرط if يتحقق أن favoriteMessageQueue لا يحوي المفتاح recipientPeerID ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:91]

```
92:                 favoriteMessageQueue[recipientPeerID] = mutableListOf()
```
> يضبط قيمة المفتاح recipientPeerID في favoriteMessageQueue إلى قائمة قابلة للتعديل فارغة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:92]

```
93:             }
```
> إغلاق جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:93]

```
94:             favoriteMessageQueue[recipientPeerID]?.add(storedMessage)
```
> يضيف storedMessage إلى القائمة المرتبطة بالمفتاح recipientPeerID في favoriteMessageQueue إن لم تكن null. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:94]

```
95:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:95]

```
96:             // Limit favorite queue size
```
> تعليق: حُدّ حجم طابور المفضّلين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:96]

```
97:             if (favoriteMessageQueue[recipientPeerID]?.size ?: 0 > MAX_CACHED_MESSAGES_FAVORITES) {
```
> يبدأ شرط if يقارن حجم قائمة recipientPeerID (أو 0 إن كانت null عبر إلفيس) بأنه أكبر من MAX_CACHED_MESSAGES_FAVORITES ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:97]

```
98:                 favoriteMessageQueue[recipientPeerID]?.removeAt(0)
```
> يحذف العنصر عند الموضع 0 من قائمة recipientPeerID في favoriteMessageQueue إن لم تكن null. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:98]

```
99:             }
```
> إغلاق جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:99]

```
100:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:100]

```
101:             Log.d(TAG, "Cached message for favorite peer $recipientPeerID (${favoriteMessageQueue[recipientPeerID]?.size} total)")
```
> يستدعي Log.d بالوسم TAG ورسالة "Cached message for favorite peer" مع قيمة recipientPeerID وحجم قائمته الإجمالي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:101]

```
102:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:102]

```
103:         } else {
```
> يُغلق جسد if ويبدأ جسد else. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:103]

```
104:             // Store in regular cache
```
> تعليق: خزّن في الذاكرة العادية. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:104]

```
105:             cleanupMessageCache()
```
> يستدعي الدالة cleanupMessageCache (تنظيف ذاكرة الرسائل). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:105]

```
106:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:106]

```
107:             messageCache.add(storedMessage)
```
> يضيف storedMessage إلى messageCache. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:107]

```
108:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:108]

```
109:             // Limit cache size
```
> تعليق: حُدّ حجم الذاكرة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:109]

```
110:             if (messageCache.size > MAX_CACHED_MESSAGES) {
```
> يبدأ شرط if يتحقق أن حجم messageCache أكبر من MAX_CACHED_MESSAGES ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:110]

```
111:                 messageCache.removeAt(0)
```
> يحذف العنصر عند الموضع 0 من messageCache. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:111]

```
112:             }
```
> إغلاق جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:112]

```
113:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:113]

```
114:             Log.d(TAG, "Cached message for peer $recipientPeerID (${messageCache.size} total in cache)")
```
> يستدعي Log.d بالوسم TAG ورسالة "Cached message for peer" مع قيمة recipientPeerID وحجم messageCache الإجمالي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:114]

```
115:         }
```
> إغلاق جسد else. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:115]

```
116:     }
```
> إغلاق جسد الدالة cacheMessage. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:116]

```
117:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:117]

```
118:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:118]

```
119:      * Send cached messages to peer when they come online
```
> تعليق: أرسل الرسائل المخزّنة للقرين عند اتصاله. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:119]

```
120:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:120]

```
121:     fun sendCachedMessages(peerID: String) {
```
> يُعرّف الدالة أرسل الرسائل المخزّنة (sendCachedMessages) التي تأخذ معامل peerID من نوع String ويفتح جسدها. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:121]

```
122:         if (cachedMessagesSentToPeer.contains(peerID)) {
```
> يبدأ شرط if يتحقق أن cachedMessagesSentToPeer يحوي peerID ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:122]

```
123:             Log.d(TAG, "Already sent cached messages to $peerID")
```
> يستدعي Log.d بالوسم TAG ورسالة "Already sent cached messages to" مع قيمة peerID. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:123]

```
124:             return // Already sent cached messages to this peer
```
> يُعيد من الدالة دون قيمة. تعليق: سبق إرسال الرسائل المخزّنة لهذا القرين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:124]

```
125:         }
```
> إغلاق جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:125]

```
126:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:126]

```
127:         cachedMessagesSentToPeer.add(peerID)
```
> يضيف peerID إلى cachedMessagesSentToPeer. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:127]

```
128:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:128]

```
129:         managerScope.launch {
```
> يبدأ إطلاق كوروتين عبر managerScope.launch ويفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:129]

```
130:             cleanupMessageCache()
```
> يستدعي الدالة cleanupMessageCache. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:130]

```
131:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:131]

```
132:             val messagesToSend = mutableListOf<StoredMessage>()
```
> يُعرّف ثابتاً الرسائل المراد إرسالها (messagesToSend) ويضبطه إلى قائمة قابلة للتعديل فارغة من StoredMessage. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:132]

```
133:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:133]

```
134:             // Check favorite queue
```
> تعليق: افحص طابور المفضّلين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:134]

```
135:             favoriteMessageQueue[peerID]?.let { favoriteMessages ->
```
> يبدأ تطبيق let على قائمة peerID في favoriteMessageQueue مع تسمية الوسيط favoriteMessages إن لم تكن null. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:135]

```
136:                 val undeliveredFavorites = favoriteMessages.filter { !deliveredMessages.contains(it.messageID) }
```
> يُعرّف ثابتاً المفضّلات غير المُسلَّمة (undeliveredFavorites) ويضبطه إلى ترشيح favoriteMessages للعناصر التي لا يحوي deliveredMessages معرّفها. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:136]

```
137:                 messagesToSend.addAll(undeliveredFavorites)
```
> يضيف كل عناصر undeliveredFavorites إلى messagesToSend. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:137]

```
138:                 favoriteMessageQueue.remove(peerID)
```
> يحذف المدخل ذا المفتاح peerID من favoriteMessageQueue. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:138]

```
139:                 Log.d(TAG, "Found ${undeliveredFavorites.size} cached favorite messages for $peerID")
```
> يستدعي Log.d بالوسم TAG ورسالة "Found ... cached favorite messages for" مع حجم undeliveredFavorites وقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:139]

```
140:             }
```
> إغلاق كتلة let. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:140]

```
141:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:141]

```
142:             // Filter regular cached messages for this recipient
```
> تعليق: رشّح الرسائل المخزّنة العادية لهذا المستلِم. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:142]

```
143:             val recipientMessages = messageCache.filter { storedMessage ->
```
> يُعرّف ثابتاً رسائل المستلِم (recipientMessages) ويبدأ ترشيح messageCache مع تسمية الوسيط storedMessage ويفتح كتلة الترشيح. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:143]

```
144:                 !deliveredMessages.contains(storedMessage.messageID) &&
```
> شرط الترشيح: ألا يحوي deliveredMessages معرّف storedMessage مع عامل و منطقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:144]

```
145:                 storedMessage.packet.recipientID?.let { recipientID ->
```
> يتابع شرط الترشيح بتطبيق let على storedMessage.packet.recipientID مع تسمية الوسيط recipientID إن لم يكن null. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:145]

```
146:                     String(recipientID).replace(" ", "") == peerID
```
> داخل let: ينشئ سلسلة من recipientID ويستبدل محارف null بسلسلة فارغة ويقارن النتيجة بـ peerID. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:146]

```
147:                 } == true
```
> يُغلق كتلة let ويقارن نتيجتها بـ true (فيعتبر null غير مطابق). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:147]

```
148:             }
```
> إغلاق كتلة الترشيح. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:148]

```
149:             messagesToSend.addAll(recipientMessages)
```
> يضيف كل عناصر recipientMessages إلى messagesToSend. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:149]

```
150:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:150]

```
151:             if (recipientMessages.isNotEmpty()) {
```
> يبدأ شرط if يتحقق أن recipientMessages ليست فارغة ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:151]

```
152:                 Log.d(TAG, "Found ${recipientMessages.size} cached regular messages for $peerID")
```
> يستدعي Log.d بالوسم TAG ورسالة "Found ... cached regular messages for" مع حجم recipientMessages وقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:152]

```
153:             }
```
> إغلاق جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:153]

```
154:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:154]

```
155:             // Sort by timestamp
```
> تعليق: رتّب حسب الطابع الزمني. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:155]

```
156:             messagesToSend.sortBy { it.timestamp }
```
> يرتّب messagesToSend تصاعدياً حسب خاصية timestamp لكل عنصر. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:156]

```
157:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:157]

```
158:             if (messagesToSend.isNotEmpty()) {
```
> يبدأ شرط if يتحقق أن messagesToSend ليست فارغة ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:158]

```
159:                 Log.i(TAG, "Sending ${messagesToSend.size} cached messages to $peerID")
```
> يستدعي Log.i بالوسم TAG ورسالة "Sending ... cached messages to" مع حجم messagesToSend وقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:159]

```
160:             }
```
> إغلاق جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:160]

```
161:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:161]

```
162:             // Mark as delivered
```
> تعليق: علّمها كمُسلَّمة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:162]

```
163:             val messageIDsToRemove = messagesToSend.map { it.messageID }
```
> يُعرّف ثابتاً معرّفات الرسائل المراد حذفها (messageIDsToRemove) ويضبطه إلى تطبيق map على messagesToSend لاستخلاص خاصية messageID لكل عنصر. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:163]

```
164:             deliveredMessages.addAll(messageIDsToRemove)
```
> يضيف كل عناصر messageIDsToRemove إلى deliveredMessages. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:164]

```
165:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:165]

```
166:             // Send with delays to avoid overwhelming the connection
```
> تعليق: أرسل مع تأخيرات لتجنّب إغراق الاتصال. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:166]

```
167:             messagesToSend.forEachIndexed { index, storedMessage ->
```
> يبدأ تكراراً مفهرساً عبر forEachIndexed على messagesToSend مع تسمية الوسيطين index و storedMessage ويفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:167]

```
168:                 delay(index * 10L) // 10ms between messages
```
> يستدعي delay بمقدار index مضروباً في 10L. تعليق: ١٠ ملي ثانية بين الرسائل. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:168]

```
169:                 delegate?.sendPacket(storedMessage.packet)
```
> يستدعي delegate?.sendPacket مع storedMessage.packet إن لم يكن delegate null. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:169]

```
170:             }
```
> إغلاق كتلة forEachIndexed. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:170]

```
171:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:171]

```
172:             // Remove sent messages from cache
```
> تعليق: احذف الرسائل المُرسَلة من الذاكرة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:172]

```
173:             messageCache.removeAll { messageIDsToRemove.contains(it.messageID) }
```
> يحذف من messageCache كل عنصر يحوي messageIDsToRemove معرّفه. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:173]

```
174:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:174]

```
175:             if (messagesToSend.isNotEmpty()) {
```
> يبدأ شرط if يتحقق أن messagesToSend ليست فارغة ويفتح جسده. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:175]

```
176:                 Log.d(TAG, "Finished sending ${messagesToSend.size} cached messages to $peerID")
```
> يستدعي Log.d بالوسم TAG ورسالة "Finished sending ... cached messages to" مع حجم messagesToSend وقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:176]

```
177:             }
```
> إغلاق جسد if. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:177]

```
178:         }
```
> إغلاق كتلة managerScope.launch. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:178]

```
179:     }
```
> إغلاق جسد الدالة sendCachedMessages. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:179]

```
180:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:180]

```
181:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:181]

```
182:      * Check if message should be cached for peer
```
> تعليق: افحص إن كان ينبغي تخزين الرسالة للقرين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:182]

```
183:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:183]

```
184:     fun shouldCacheForPeer(recipientPeerID: String): Boolean {
```
> يُعرّف الدالة هل يُخزَّن للقرين (shouldCacheForPeer) التي تأخذ معامل recipientPeerID من نوع String وتُعيد Boolean ويفتح جسدها. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:184]

```
185:         // Check if recipient is offline and should cache for favorites
```
> تعليق: افحص إن كان المستلِم غير متصل وينبغي التخزين للمفضّلين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:185]

```
186:         val isOffline = !(delegate?.isPeerOnline(recipientPeerID) ?: false)
```
> يُعرّف ثابتاً غير متصل (isOffline) ويضبطه إلى نفي نتيجة delegate?.isPeerOnline(recipientPeerID) (أو false إن كانت null). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:186]

```
187:         val isRecipientFavorite = delegate?.isFavorite(recipientPeerID) ?: false
```
> يُعرّف ثابتاً المستلِم مفضّل (isRecipientFavorite) ويضبطه إلى نتيجة delegate?.isFavorite(recipientPeerID) (أو false إن كانت null). [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:187]

```
188:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:188]

```
189:         return isOffline && isRecipientFavorite
```
> يُعيد ناتج عامل و المنطقي بين isOffline و isRecipientFavorite. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:189]

```
190:     }
```
> إغلاق جسد الدالة shouldCacheForPeer. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:190]

```
191:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:191]

```
192:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:192]

```
193:      * Mark message as delivered
```
> تعليق: علّم الرسالة كمُسلَّمة. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:193]

```
194:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:194]

```
195:     fun markMessageAsDelivered(messageID: String) {
```
> يُعرّف الدالة علّم الرسالة كمُسلَّمة (markMessageAsDelivered) التي تأخذ معامل messageID من نوع String ويفتح جسدها. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:195]

```
196:         deliveredMessages.add(messageID)
```
> يضيف messageID إلى deliveredMessages. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:196]

```
197:     }
```
> إغلاق جسد الدالة markMessageAsDelivered. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:197]

```
198:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:198]

```
199:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:199]

```
200:      * Get cached message count for peer
```
> تعليق: احصل على عدد الرسائل المخزّنة للقرين. [app/src/main/java/com/bitchat/android/mesh/StoreForwardManager.kt:200]
