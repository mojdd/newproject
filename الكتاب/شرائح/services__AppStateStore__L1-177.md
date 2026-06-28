# شريحة — app/src/main/java/com/bitchat/android/services/AppStateStore.kt (الأسطر 1–177)

```
1: package com.bitchat.android.services
```
> يعلن عن انتماء الملف للحزمة (package) باسم com.bitchat.android.services. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:2]

```
3: import com.bitchat.android.model.BitchatMessage
```
> يستورد الصنف رسالة بِت‌شات (BitchatMessage) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:3]

```
4: import com.bitchat.android.model.DeliveryStatus
```
> يستورد الصنف حالة التسليم (DeliveryStatus) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:4]

```
5: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد تدفّق الحالة القابل للتغيير (MutableStateFlow) من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:5]

```
6: import kotlinx.coroutines.flow.StateFlow
```
> يستورد تدفّق الحالة (StateFlow) من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:6]

```
7: import kotlinx.coroutines.flow.asStateFlow
```
> يستورد الدالة التحويلية asStateFlow من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:8]

```
9: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:9]

```
10:  * Process-wide in-memory state store that survives Activity recreation.
```
> تعليق: مخزن حالة في الذاكرة على مستوى العملية بأكملها يبقى حياً عند إعادة إنشاء النشاط (Activity). [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:10]

```
11:  * The foreground Mesh service updates this store; UI subscribes/hydrates from it.
```
> تعليق: خدمة الشبكة المتشابكة (Mesh) الأمامية تُحدّث هذا المخزن؛ وواجهة المستخدم تشترك فيه وتتغذّى منه. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:11]

```
12:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:12]

```
13: object AppStateStore {
```
> يعرّف كائناً مفرداً (object) باسم مخزن حالة التطبيق (AppStateStore) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:13]

```
14:     // Global de-dup set by message id to avoid duplicate keys in Compose lists
```
> تعليق: مجموعة إزالة التكرار العامة بحسب معرّف الرسالة لتجنّب المفاتيح المكرّرة في قوائم Compose. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:14]

```
15:     private val seenMessageIds = mutableSetOf<String>()
```
> يعرّف خاصية خاصّة ثابتة باسم معرّفات الرسائل المرئية (seenMessageIds) ويهيّئها بمجموعة قابلة للتغيير فارغة من نوع نص (String). [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:15]

```
16:     private val seenPublicMessageKeys = mutableSetOf<String>()
```
> يعرّف خاصية خاصّة ثابتة باسم مفاتيح الرسائل العامة المرئية (seenPublicMessageKeys) ويهيّئها بمجموعة قابلة للتغيير فارغة من نوع نص. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:16]

```
17:     private val peerIdsByTransport = mutableMapOf<String, Set<String>>()
```
> يعرّف خاصية خاصّة ثابتة باسم معرّفات الأقران بحسب الناقل (peerIdsByTransport) ويهيّئها بخريطة قابلة للتغيير فارغة مفتاحها نص وقيمتها مجموعة نصوص. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:17]

```
18:     // Direct (single-hop) peer IDs per transport, used to gossip a unified neighbor set.
```
> تعليق: معرّفات الأقران المباشرين (قفزة واحدة) لكل ناقل، تُستعمل لنشر مجموعة جيران موحّدة عبر الإشاعة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:18]

```
19:     private val directPeerIdsByTransport = mutableMapOf<String, Set<String>>()
```
> يعرّف خاصية خاصّة ثابتة باسم معرّفات الأقران المباشرين بحسب الناقل (directPeerIdsByTransport) ويهيّئها بخريطة قابلة للتغيير فارغة مفتاحها نص وقيمتها مجموعة نصوص. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:19]

```
20:     // Connected peer IDs (mesh ephemeral IDs)
```
> تعليق: معرّفات الأقران المتّصلين (معرّفات عابرة للشبكة المتشابكة). [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:20]

```
21:     private val _peers = MutableStateFlow<List<String>>(emptyList())
```
> يعرّف خاصية خاصّة ثابتة باسم الأقران الداخلي (_peers) ويهيّئها بتدفّق حالة قابل للتغيير من نوع قائمة نصوص بقيمة ابتدائية قائمة فارغة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:21]

```
22:     val peers: StateFlow<List<String>> = _peers.asStateFlow()
```
> يعرّف خاصية عامّة ثابتة باسم الأقران (peers) من نوع تدفّق حالة لقائمة نصوص ويسندها إلى نسخة للقراءة فقط من _peers عبر asStateFlow. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:22]

```
23: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:23]

```
24:     // Public mesh timeline messages (non-channel)
```
> تعليق: رسائل الخط الزمني العام للشبكة المتشابكة (غير المنتمية لقناة). [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:24]

```
25:     private val _publicMessages = MutableStateFlow<List<BitchatMessage>>(emptyList())
```
> يعرّف خاصية خاصّة ثابتة باسم الرسائل العامة الداخلي (_publicMessages) ويهيّئها بتدفّق حالة قابل للتغيير من نوع قائمة رسائل بِت‌شات بقيمة ابتدائية قائمة فارغة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:25]

```
26:     val publicMessages: StateFlow<List<BitchatMessage>> = _publicMessages.asStateFlow()
```
> يعرّف خاصية عامّة ثابتة باسم الرسائل العامة (publicMessages) من نوع تدفّق حالة لقائمة رسائل بِت‌شات ويسندها إلى نسخة للقراءة فقط من _publicMessages عبر asStateFlow. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:27]

```
28:     // Private messages by peerID
```
> تعليق: الرسائل الخاصة بحسب معرّف القرين (peerID). [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:28]

```
29:     private val _privateMessages = MutableStateFlow<Map<String, List<BitchatMessage>>>(emptyMap())
```
> يعرّف خاصية خاصّة ثابتة باسم الرسائل الخاصة الداخلي (_privateMessages) ويهيّئها بتدفّق حالة قابل للتغيير من نوع خريطة مفتاحها نص وقيمتها قائمة رسائل بِت‌شات بقيمة ابتدائية خريطة فارغة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:29]

```
30:     val privateMessages: StateFlow<Map<String, List<BitchatMessage>>> = _privateMessages.asStateFlow()
```
> يعرّف خاصية عامّة ثابتة باسم الرسائل الخاصة (privateMessages) من نوع تدفّق حالة لخريطة نص إلى قائمة رسائل بِت‌شات ويسندها إلى نسخة للقراءة فقط من _privateMessages عبر asStateFlow. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:30]

```
31: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:31]

```
32:     // Channel messages by channel name
```
> تعليق: رسائل القناة بحسب اسم القناة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:32]

```
33:     private val _channelMessages = MutableStateFlow<Map<String, List<BitchatMessage>>>(emptyMap())
```
> يعرّف خاصية خاصّة ثابتة باسم رسائل القنوات الداخلي (_channelMessages) ويهيّئها بتدفّق حالة قابل للتغيير من نوع خريطة مفتاحها نص وقيمتها قائمة رسائل بِت‌شات بقيمة ابتدائية خريطة فارغة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:33]

```
34:     val channelMessages: StateFlow<Map<String, List<BitchatMessage>>> = _channelMessages.asStateFlow()
```
> يعرّف خاصية عامّة ثابتة باسم رسائل القنوات (channelMessages) من نوع تدفّق حالة لخريطة نص إلى قائمة رسائل بِت‌شات ويسندها إلى نسخة للقراءة فقط من _channelMessages عبر asStateFlow. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:34]

```
35: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:35]

```
36:     fun setPeers(ids: List<String>) {
```
> يعرّف دالة باسم ضبط الأقران (setPeers) تأخذ وسيطاً ids من نوع قائمة نصوص ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:36]

```
37:         synchronized(this) {
```
> يفتح كتلة متزامنة (synchronized) على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:37]

```
38:             _peers.value = ids.distinct()
```
> يسند إلى قيمة _peers نتيجة إزالة المتكرّر من ids عبر distinct. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:38]

```
39:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:39]

```
40:     }
```
> إغلاق نطاق الدالة setPeers. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:40]

```
41: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:41]

```
42:     fun setTransportPeers(transportId: String, ids: List<String>) {
```
> يعرّف دالة باسم ضبط أقران الناقل (setTransportPeers) تأخذ وسيطاً transportId من نوع نص ووسيطاً ids من نوع قائمة نصوص ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:42]

```
43:         synchronized(this) {
```
> يفتح كتلة متزامنة على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:43]

```
44:             peerIdsByTransport[transportId] = ids.toSet()
```
> يسند إلى مفتاح transportId في خريطة peerIdsByTransport نتيجة تحويل ids إلى مجموعة عبر toSet. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:44]

```
45:             publishTransportPeersLocked()
```
> يستدعي الدالة نشر أقران النواقل تحت القفل (publishTransportPeersLocked). [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:45]

```
46:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:46]

```
47:     }
```
> إغلاق نطاق الدالة setTransportPeers. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:47]

```
48: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:48]

```
49:     fun clearTransportPeers(transportId: String) {
```
> يعرّف دالة باسم مسح أقران الناقل (clearTransportPeers) تأخذ وسيطاً transportId من نوع نص ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:49]

```
50:         synchronized(this) {
```
> يفتح كتلة متزامنة على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:50]

```
51:             peerIdsByTransport.remove(transportId)
```
> يحذف المدخل ذا المفتاح transportId من خريطة peerIdsByTransport عبر remove. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:51]

```
52:             publishTransportPeersLocked()
```
> يستدعي الدالة publishTransportPeersLocked. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:52]

```
53:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:53]

```
54:     }
```
> إغلاق نطاق الدالة clearTransportPeers. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:54]

```
55: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:55]

```
56:     private fun publishTransportPeersLocked() {
```
> يعرّف دالة خاصّة باسم publishTransportPeersLocked بلا وسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:56]

```
57:         _peers.value = peerIdsByTransport.values
```
> يبدأ إسناداً إلى قيمة _peers انطلاقاً من قيم خريطة peerIdsByTransport. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:57]

```
58:             .asSequence()
```
> يحوّل القيم إلى متتالية (Sequence) عبر asSequence. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:58]

```
59:             .flatten()
```
> يسطّح المتتالية (دمج مجموعات النصوص في تدفّق واحد) عبر flatten. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:59]

```
60:             .distinct()
```
> يزيل العناصر المتكرّرة عبر distinct. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:60]

```
61:             .toList()
```
> يحوّل النتيجة إلى قائمة عبر toList ليكتمل الإسناد إلى _peers. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:61]

```
62:     }
```
> إغلاق نطاق الدالة publishTransportPeersLocked. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:62]

```
63: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:63]

```
64:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:64]

```
65:      * Record the set of direct (single-hop) peers reachable over a given transport. Each transport
```
> تعليق: سجّل مجموعة الأقران المباشرين (قفزة واحدة) الذين يمكن الوصول إليهم عبر ناقل معيّن. كل ناقل. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:65]

```
66:      * (BLE, Wi-Fi Aware, ...) only knows its own direct peers; [getDirectPeers] unions them so every
```
> تعليق: (بلوتوث منخفض الطاقة BLE، واي-فاي أوير Wi-Fi Aware، ...) لا يعرف إلا أقرانه المباشرين؛ والدالة [getDirectPeers] توحّدهم كي يستطيع كل. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:66]

```
67:      * transport can gossip the same complete neighbor list under our shared node identity.
```
> تعليق: ناقل أن يشيع نفس قائمة الجيران الكاملة تحت هويّة عقدتنا المشتركة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:67]

```
68:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:68]

```
69:     fun setTransportDirectPeers(transportId: String, ids: Collection<String>) {
```
> يعرّف دالة باسم ضبط الأقران المباشرين للناقل (setTransportDirectPeers) تأخذ وسيطاً transportId من نوع نص ووسيطاً ids من نوع تجميعة نصوص (Collection) ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:69]

```
70:         synchronized(this) {
```
> يفتح كتلة متزامنة على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:70]

```
71:             directPeerIdsByTransport[transportId] = ids.toSet()
```
> يسند إلى مفتاح transportId في خريطة directPeerIdsByTransport نتيجة تحويل ids إلى مجموعة عبر toSet. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:71]

```
72:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:72]

```
73:     }
```
> إغلاق نطاق الدالة setTransportDirectPeers. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:73]

```
74: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:74]

```
75:     fun clearTransportDirectPeers(transportId: String) {
```
> يعرّف دالة باسم مسح الأقران المباشرين للناقل (clearTransportDirectPeers) تأخذ وسيطاً transportId من نوع نص ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:75]

```
76:         synchronized(this) {
```
> يفتح كتلة متزامنة على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:76]

```
77:             directPeerIdsByTransport.remove(transportId)
```
> يحذف المدخل ذا المفتاح transportId من خريطة directPeerIdsByTransport عبر remove. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:77]

```
78:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:78]

```
79:     }
```
> إغلاق نطاق الدالة clearTransportDirectPeers. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:79]

```
80: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:80]

```
81:     /** Union of direct peers across all transports. */
```
> تعليق توثيقي: اتحاد الأقران المباشرين عبر جميع النواقل. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:81]

```
82:     fun getDirectPeers(): Set<String> {
```
> يعرّف دالة باسم جلب الأقران المباشرين (getDirectPeers) بلا وسطاء تُعيد مجموعة نصوص ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:82]

```
83:         synchronized(this) {
```
> يفتح كتلة متزامنة على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:83]

```
84:             return directPeerIdsByTransport.values.flatten().toSet()
```
> يُعيد نتيجة تسطيح قيم خريطة directPeerIdsByTransport عبر flatten ثم تحويلها إلى مجموعة عبر toSet. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:84]

```
85:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:85]

```
86:     }
```
> إغلاق نطاق الدالة getDirectPeers. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:86]

```
87: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:87]

```
88:     fun addPublicMessage(msg: BitchatMessage) {
```
> يعرّف دالة باسم إضافة رسالة عامة (addPublicMessage) تأخذ وسيطاً msg من نوع رسالة بِت‌شات ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:88]

```
89:         synchronized(this) {
```
> يفتح كتلة متزامنة على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:89]

```
90:             val publicKey = publicMessageKey(msg)
```
> يعرّف متغيّراً ثابتاً محلّياً باسم المفتاح العام (publicKey) ويسند إليه نتيجة استدعاء الدالة publicMessageKey على msg. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:90]

```
91:             if (seenMessageIds.contains(msg.id) || seenPublicMessageKeys.contains(publicKey)) return
```
> يخرج من الدالة (return) إذا كانت seenMessageIds تحوي msg.id أو كانت seenPublicMessageKeys تحوي publicKey. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:91]

```
92:             seenMessageIds.add(msg.id)
```
> يضيف msg.id إلى مجموعة seenMessageIds عبر add. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:92]

```
93:             seenPublicMessageKeys.add(publicKey)
```
> يضيف publicKey إلى مجموعة seenPublicMessageKeys عبر add. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:93]

```
94:             _publicMessages.value = _publicMessages.value + msg
```
> يسند إلى قيمة _publicMessages قائمةً ناتجة عن جمع القيمة الحالية لـ _publicMessages مع msg. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:94]

```
95:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:95]

```
96:     }
```
> إغلاق نطاق الدالة addPublicMessage. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:96]

```
97: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:97]

```
98:     fun addPrivateMessage(peerID: String, msg: BitchatMessage) {
```
> يعرّف دالة باسم إضافة رسالة خاصة (addPrivateMessage) تأخذ وسيطاً peerID من نوع نص ووسيطاً msg من نوع رسالة بِت‌شات ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:98]

```
99:         synchronized(this) {
```
> يفتح كتلة متزامنة على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:99]

```
100:             if (seenMessageIds.contains(msg.id)) return
```
> يخرج من الدالة (return) إذا كانت seenMessageIds تحوي msg.id. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:100]

```
101:             seenMessageIds.add(msg.id)
```
> يضيف msg.id إلى مجموعة seenMessageIds عبر add. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:101]

```
102:             val map = _privateMessages.value.toMutableMap()
```
> يعرّف متغيّراً ثابتاً محلّياً باسم map ويسند إليه نسخة قابلة للتغيير من القيمة الحالية لـ _privateMessages عبر toMutableMap. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:102]

```
103:             val list = (map[peerID] ?: emptyList()) + msg
```
> يعرّف متغيّراً ثابتاً محلّياً باسم list ويسند إليه القائمة المرتبطة بـ peerID في map (أو قائمة فارغة إن غابت) مجموعةً إلى msg. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:103]

```
104:             map[peerID] = list
```
> يسند list إلى المفتاح peerID في الخريطة map. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:104]

```
105:             _privateMessages.value = map
```
> يسند الخريطة map إلى قيمة _privateMessages. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:105]

```
106:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:106]

```
107:     }
```
> إغلاق نطاق الدالة addPrivateMessage. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:107]

```
108: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:108]

```
109:     private fun statusPriority(status: DeliveryStatus?): Int = when (status) {
```
> يعرّف دالة خاصّة باسم أولوية الحالة (statusPriority) تأخذ وسيطاً status من نوع حالة تسليم يقبل العدم وتُعيد عدداً صحيحاً (Int) عبر تعبير when على status. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:109]

```
110:         null -> 0
```
> يطابق الحالة null ويُعيد القيمة 0. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:110]

```
111:         is DeliveryStatus.Sending -> 1
```
> يطابق الحالة من نوع جارٍ الإرسال (DeliveryStatus.Sending) ويُعيد القيمة 1. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:111]

```
112:         is DeliveryStatus.Sent -> 2
```
> يطابق الحالة من نوع أُرسِل (DeliveryStatus.Sent) ويُعيد القيمة 2. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:112]

```
113:         is DeliveryStatus.PartiallyDelivered -> 3
```
> يطابق الحالة من نوع سُلِّم جزئياً (DeliveryStatus.PartiallyDelivered) ويُعيد القيمة 3. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:113]

```
114:         is DeliveryStatus.Delivered -> 4
```
> يطابق الحالة من نوع سُلِّم (DeliveryStatus.Delivered) ويُعيد القيمة 4. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:114]

```
115:         is DeliveryStatus.Read -> 5
```
> يطابق الحالة من نوع قُرِئ (DeliveryStatus.Read) ويُعيد القيمة 5. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:115]

```
116:         is DeliveryStatus.Failed -> 0
```
> يطابق الحالة من نوع فشل (DeliveryStatus.Failed) ويُعيد القيمة 0. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:116]

```
117:     }
```
> إغلاق نطاق تعبير when ودالة statusPriority. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:117]

```
118: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:118]

```
119:     fun updatePrivateMessageStatus(messageID: String, status: DeliveryStatus) {
```
> يعرّف دالة باسم تحديث حالة الرسالة الخاصة (updatePrivateMessageStatus) تأخذ وسيطاً messageID من نوع نص ووسيطاً status من نوع حالة تسليم ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:119]

```
120:         synchronized(this) {
```
> يفتح كتلة متزامنة على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:120]

```
121:             val map = _privateMessages.value.toMutableMap()
```
> يعرّف متغيّراً ثابتاً محلّياً باسم map ويسند إليه نسخة قابلة للتغيير من القيمة الحالية لـ _privateMessages عبر toMutableMap. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:121]

```
122:             var changed = false
```
> يعرّف متغيّراً متغيّر القيمة محلّياً باسم تغيّر (changed) ويهيّئه بالقيمة false. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:122]

```
123:             map.keys.toList().forEach { peer ->
```
> يحوّل مفاتيح map إلى قائمة عبر toList ثم يكرّر على كل عنصر باسم peer عبر forEach ويفتح جسم اللامدا. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:123]

```
124:                 val list = map[peer]?.toMutableList() ?: mutableListOf()
```
> يعرّف متغيّراً ثابتاً محلّياً باسم list ويسند إليه نسخة قابلة للتغيير من قائمة map[peer] (أو قائمة قابلة للتغيير فارغة إن كانت عدماً). [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:124]

```
125:                 val idx = list.indexOfFirst { it.id == messageID }
```
> يعرّف متغيّراً ثابتاً محلّياً باسم idx ويسند إليه فهرس أول عنصر في list معرّفه it.id يساوي messageID عبر indexOfFirst. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:125]

```
126:                 if (idx >= 0) {
```
> يفتح شرطاً ينفّذ إذا كان idx أكبر من أو يساوي صفر. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:126]

```
127:                     val current = list[idx].deliveryStatus
```
> يعرّف متغيّراً ثابتاً محلّياً باسم الحالة الراهنة (current) ويسند إليه خاصية deliveryStatus للعنصر list[idx]. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:127]

```
128:                     // Do not downgrade (e.g., Read -> Delivered)
```
> تعليق: لا تخفّض الحالة (مثلاً من قُرِئ إلى سُلِّم). [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:128]

```
129:                     if (statusPriority(status) >= statusPriority(current)) {
```
> يفتح شرطاً ينفّذ إذا كانت أولوية status أكبر من أو تساوي أولوية current بحسب الدالة statusPriority. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:129]

```
130:                         list[idx] = list[idx].copy(deliveryStatus = status)
```
> يستبدل العنصر list[idx] بنسخة منه عبر copy مع ضبط deliveryStatus بالقيمة status. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:130]

```
131:                         map[peer] = list
```
> يسند list إلى المفتاح peer في الخريطة map. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:131]

```
132:                         changed = true
```
> يضبط المتغيّر changed بالقيمة true. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:132]

```
133:                     }
```
> إغلاق نطاق شرط الأولوية. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:133]

```
134:                 }
```
> إغلاق نطاق شرط idx. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:134]

```
135:             }
```
> إغلاق نطاق لامدا forEach. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:135]

```
136:             if (changed) {
```
> يفتح شرطاً ينفّذ إذا كانت قيمة changed صحيحة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:136]

```
137:                 _privateMessages.value = map
```
> يسند الخريطة map إلى قيمة _privateMessages. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:137]

```
138:             }
```
> إغلاق نطاق شرط changed. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:138]

```
139:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:139]

```
140:     }
```
> إغلاق نطاق الدالة updatePrivateMessageStatus. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:140]

```
141: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:141]

```
142:     fun addChannelMessage(channel: String, msg: BitchatMessage) {
```
> يعرّف دالة باسم إضافة رسالة قناة (addChannelMessage) تأخذ وسيطاً channel من نوع نص ووسيطاً msg من نوع رسالة بِت‌شات ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:142]

```
143:         synchronized(this) {
```
> يفتح كتلة متزامنة على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:143]

```
144:             if (seenMessageIds.contains(msg.id)) return
```
> يخرج من الدالة (return) إذا كانت seenMessageIds تحوي msg.id. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:144]

```
145:             seenMessageIds.add(msg.id)
```
> يضيف msg.id إلى مجموعة seenMessageIds عبر add. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:145]

```
146:             val map = _channelMessages.value.toMutableMap()
```
> يعرّف متغيّراً ثابتاً محلّياً باسم map ويسند إليه نسخة قابلة للتغيير من القيمة الحالية لـ _channelMessages عبر toMutableMap. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:146]

```
147:             val list = (map[channel] ?: emptyList()) + msg
```
> يعرّف متغيّراً ثابتاً محلّياً باسم list ويسند إليه القائمة المرتبطة بـ channel في map (أو قائمة فارغة إن غابت) مجموعةً إلى msg. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:147]

```
148:             map[channel] = list
```
> يسند list إلى المفتاح channel في الخريطة map. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:148]

```
149:             _channelMessages.value = map
```
> يسند الخريطة map إلى قيمة _channelMessages. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:149]

```
150:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:150]

```
151:     }
```
> إغلاق نطاق الدالة addChannelMessage. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:151]

```
152: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:152]

```
153:     // Clear all in-memory state (used for full app shutdown)
```
> تعليق: امسح كل الحالة في الذاكرة (تُستعمل عند إيقاف التطبيق الكامل). [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:153]

```
154:     fun clear() {
```
> يعرّف دالة باسم مسح (clear) بلا وسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:154]

```
155:         synchronized(this) {
```
> يفتح كتلة متزامنة على القفل this. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:155]

```
156:             seenMessageIds.clear()
```
> يفرّغ مجموعة seenMessageIds عبر clear. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:156]

```
157:             seenPublicMessageKeys.clear()
```
> يفرّغ مجموعة seenPublicMessageKeys عبر clear. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:157]

```
158:             peerIdsByTransport.clear()
```
> يفرّغ خريطة peerIdsByTransport عبر clear. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:158]

```
159:             directPeerIdsByTransport.clear()
```
> يفرّغ خريطة directPeerIdsByTransport عبر clear. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:159]

```
160:             _peers.value = emptyList()
```
> يسند قائمة فارغة إلى قيمة _peers. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:160]

```
161:             _publicMessages.value = emptyList()
```
> يسند قائمة فارغة إلى قيمة _publicMessages. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:161]

```
162:             _privateMessages.value = emptyMap()
```
> يسند خريطة فارغة إلى قيمة _privateMessages. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:162]

```
163:             _channelMessages.value = emptyMap()
```
> يسند خريطة فارغة إلى قيمة _channelMessages. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:163]

```
164:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:164]

```
165:     }
```
> إغلاق نطاق الدالة clear. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:165]

```
166: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:166]

```
167:     private fun publicMessageKey(msg: BitchatMessage): String {
```
> يعرّف دالة خاصّة باسم مفتاح الرسالة العامة (publicMessageKey) تأخذ وسيطاً msg من نوع رسالة بِت‌شات وتُعيد نصاً ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:167]

```
168:         val sender = msg.senderPeerID ?: msg.sender
```
> يعرّف متغيّراً ثابتاً محلّياً باسم المرسِل (sender) ويسند إليه msg.senderPeerID أو msg.sender إن كان الأول عدماً. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:168]

```
169:         return listOf(
```
> يبدأ إعادة قائمة (listOf) ويفتح وسطاءها. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:169]

```
170:             sender,
```
> العنصر الأول في القائمة هو sender. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:170]

```
171:             msg.timestamp.time.toString(),
```
> العنصر الثاني هو msg.timestamp.time محوّلاً إلى نص عبر toString. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:171]

```
172:             msg.type.name,
```
> العنصر الثالث هو اسم النوع msg.type.name. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:172]

```
173:             msg.channel ?: "",
```
> العنصر الرابع هو msg.channel أو نص فارغ إن كان عدماً. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:173]

```
174:             msg.content
```
> العنصر الخامس هو msg.content. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:174]

```
175:         ).joinToString("")
```
> يغلق القائمة ويدمج عناصرها في نص واحد مفصولاً بالمحرف "" عبر joinToString ليُعاد كنتيجة الدالة. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:175]

```
176:     }
```
> إغلاق نطاق الدالة publicMessageKey. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:176]

```
177: }
```
> إغلاق نطاق الكائن المفرد AppStateStore. [app/src/main/java/com/bitchat/android/services/AppStateStore.kt:177]
