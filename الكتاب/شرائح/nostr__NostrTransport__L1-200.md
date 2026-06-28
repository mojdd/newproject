# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يعلن أن هذا الملف يتبع الحزمة (package) باسم `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من `android.content`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` من `android.util`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:4]

```
5: import com.bitchat.android.model.ReadReceipt
```
> يستورد الصنف `ReadReceipt` (إيصال القراءة) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:5]

```
6: import com.bitchat.android.model.NoisePayloadType
```
> يستورد الصنف `NoisePayloadType` (نوع حمولة نويز) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:6]

```
7: import kotlinx.coroutines.*
```
> يستورد كل العناصر من حزمة الكوروتينات (coroutines) `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:7]

```
8: import java.util.*
```
> يستورد كل العناصر من حزمة `java.util`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:8]

```
9: import java.util.concurrent.ConcurrentLinkedQueue
```
> يستورد الصنف `ConcurrentLinkedQueue` (طابور متزامن مترابط) من `java.util.concurrent`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:9]

```
10: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:10]

```
11: /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:11]

```
12:  * Minimal Nostr transport for offline sending
```
> تعليق: «ناقل Nostr بسيط للإرسال دون اتصال». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:12]

```
13:  * Direct port from iOS NostrTransport for 100% compatibility
```
> تعليق: «نقل مباشر من NostrTransport الخاص بنظام iOS لتوافق بنسبة 100%». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:13]

```
14:  */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:14]

```
15: class NostrTransport(
```
> يعرّف الصنف `NostrTransport` (ناقل Nostr) ويبدأ قائمة بارامترات الباني (constructor). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:15]

```
16:     private val context: Context,
```
> يعرّف بارامتر باني خاصاً غير قابل للتغيير `context` من نوع `Context`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:16]

```
17:     var senderPeerID: String = ""
```
> يعرّف خاصية قابلة للتغيير `senderPeerID` (معرّف القرين المرسِل) من نوع `String` بقيمة ابتدائية سلسلة فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:17]

```
18: ) {
```
> يغلق قائمة بارامترات الباني ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:18]

```
19:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:19]

```
20:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:20]

```
21:         private const val TAG = "NostrTransport"
```
> يعرّف ثابتاً خاصاً `TAG` (الوسم) بالقيمة النصية `"NostrTransport"`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:21]

```
22:         private const val READ_ACK_INTERVAL = com.bitchat.android.util.AppConstants.Nostr.READ_ACK_INTERVAL_MS // ~3 per second (0.35s interval like iOS)
```
> يعرّف ثابتاً خاصاً `READ_ACK_INTERVAL` (فاصل تأكيد القراءة) بقيمة `AppConstants.Nostr.READ_ACK_INTERVAL_MS`، مع تعليق: «نحو 3 في الثانية (فاصل 0.35 ثانية كما في iOS)». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:22]

```
23:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:23]

```
24:         @Volatile
```
> يضع التعليق التوضيحي (annotation) ‏`@Volatile` على العنصر التالي. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:24]

```
25:         private var INSTANCE: NostrTransport? = null
```
> يعرّف خاصية خاصة قابلة للتغيير `INSTANCE` (النسخة) من نوع `NostrTransport?` بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:25]

```
26:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:26]

```
27:         fun getInstance(context: Context): NostrTransport {
```
> يعرّف الدالة `getInstance` (احصل على النسخة) التي تأخذ بارامتراً `context` من نوع `Context` وتعيد نوع `NostrTransport`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:27]

```
28:             return INSTANCE ?: synchronized(this) {
```
> يعيد قيمة `INSTANCE`، وإن كانت `null` يدخل كتلة متزامنة (synchronized) على `this`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:28]

```
29:                 INSTANCE ?: NostrTransport(context.applicationContext).also { INSTANCE = it }
```
> يعيد قيمة `INSTANCE`، وإن كانت `null` يُنشئ `NostrTransport` بـ `context.applicationContext` ويسند الناتج إلى `INSTANCE` عبر `also`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:29]

```
30:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:30]

```
31:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:31]

```
32:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:32]

```
33:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:33]

```
34:     // Throttle READ receipts to avoid relay rate limits (like iOS)
```
> تعليق: «تخفيض معدل إيصالات القراءة لتجنّب حدود معدل المُرحِّل (كما في iOS)». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:34]

```
35:     private data class QueuedRead(
```
> يعرّف صنف بيانات (data class) خاصاً `QueuedRead` (قراءة مُصفوفة في طابور) ويبدأ بارامتراته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:35]

```
36:         val receipt: ReadReceipt,
```
> يعرّف خاصية غير قابلة للتغيير `receipt` (الإيصال) من نوع `ReadReceipt`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:36]

```
37:         val peerID: String
```
> يعرّف خاصية غير قابلة للتغيير `peerID` (معرّف القرين) من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:37]

```
38:     )
```
> يغلق بارامترات صنف البيانات `QueuedRead`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:38]

```
39:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:39]

```
40:     private val readQueue = ConcurrentLinkedQueue<QueuedRead>()
```
> يعرّف خاصية خاصة غير قابلة للتغيير `readQueue` (طابور القراءة) بقيمة نسخة جديدة من `ConcurrentLinkedQueue<QueuedRead>`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:40]

```
41:     private var isSendingReadAcks = false
```
> يعرّف خاصية خاصة قابلة للتغيير `isSendingReadAcks` (هل يُرسَل تأكيدات القراءة) بقيمة ابتدائية `false`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:41]

```
42:     private val transportScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يعرّف خاصية خاصة غير قابلة للتغيير `transportScope` (نطاق الناقل) بقيمة `CoroutineScope` مبني من `Dispatchers.IO` مع `SupervisorJob()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:42]

```
43:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:43]

```
44:     // MARK: - Transport Interface Methods
```
> تعليق: «MARK: - دوال واجهة الناقل». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:44]

```
45:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:45]

```
46:     val myPeerID: String get() = senderPeerID
```
> يعرّف خاصية غير قابلة للتغيير `myPeerID` (معرّف قريني) من نوع `String` بمُحصِّل (getter) يعيد `senderPeerID`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:46]

```
47:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:47]

```
48:     fun sendPrivateMessage(
```
> يعرّف الدالة `sendPrivateMessage` (أرسل رسالة خاصة) ويبدأ بارامتراتها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:48]

```
49:         content: String,
```
> يعرّف بارامتر `content` (المحتوى) من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:49]

```
50:         to: String,
```
> يعرّف بارامتر `to` (إلى) من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:50]

```
51:         recipientNickname: String,
```
> يعرّف بارامتر `recipientNickname` (اسم المستلِم المستعار) من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:51]

```
52:         messageID: String
```
> يعرّف بارامتر `messageID` (معرّف الرسالة) من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:52]

```
53:     ) {
```
> يغلق بارامترات الدالة ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:53]

```
54:         transportScope.launch {
```
> يطلق كوروتيناً (launch) على النطاق `transportScope`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:54]

```
55:             try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:55]

```
56:                 // Resolve favorite by full noise key or by short peerID fallback
```
> تعليق: «حلّ المُفضَّل بمفتاح نويز الكامل أو بالرجوع إلى معرّف القرين القصير». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:56]

```
57:                 var recipientNostrPubkey: String? = null
```
> يعرّف متغيراً محلياً قابلاً للتغيير `recipientNostrPubkey` (مفتاح Nostr العام للمستلِم) من نوع `String?` بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:57]

```
58:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:58]

```
59:                 // Resolve by peerID first (new peerID→npub index), then fall back to noise key mapping
```
> تعليق: «حلّ بمعرّف القرين أولاً (فهرس peerID→npub الجديد)، ثم ارجع إلى ربط مفتاح نويز». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:59]

```
60:                 recipientNostrPubkey = resolveNostrPublicKey(to)
```
> يسند إلى `recipientNostrPubkey` ناتج استدعاء `resolveNostrPublicKey(to)`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:60]

```
61:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:61]

```
62:                 if (recipientNostrPubkey == null) {
```
> يبدأ شرطاً يختبر إن كان `recipientNostrPubkey` يساوي `null`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:62]

```
63:                     Log.w(TAG, "No Nostr public key found for peerID: $to")
```
> يستدعي `Log.w` بالوسم `TAG` والرسالة «لم يُعثر على مفتاح Nostr عام لمعرّف القرين: $to». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:63]

```
64:                     return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:64]

```
65:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:65]

```
66:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:66]

```
67:                 val senderIdentity = NostrIdentityBridge.getCurrentNostrIdentity(context)
```
> يعرّف متغيراً محلياً غير قابل للتغيير `senderIdentity` (هوية المرسِل) بقيمة ناتج `NostrIdentityBridge.getCurrentNostrIdentity(context)`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:67]

```
68:                 if (senderIdentity == null) {
```
> يبدأ شرطاً يختبر إن كان `senderIdentity` يساوي `null`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:68]

```
69:                     Log.e(TAG, "No Nostr identity available")
```
> يستدعي `Log.e` بالوسم `TAG` والرسالة «لا توجد هوية Nostr متاحة». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:69]

```
70:                     return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:70]

```
71:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:71]

```
72:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:72]

```
73:                 Log.d(TAG, "NostrTransport: preparing PM to ${recipientNostrPubkey.take(16)}... for peerID ${to.take(8)}... id=${messageID.take(8)}...")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة تصحيح تعرض أول 16 محرفاً من `recipientNostrPubkey` وأول 8 من `to` وأول 8 من `messageID`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:73]

```
74:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:74]

```
75:                 // Convert recipient npub -> hex (x-only)
```
> تعليق: «حوّل npub المستلِم إلى ست عشري (x-only)». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:75]

```
76:                 val recipientHex = try {
```
> يعرّف متغيراً غير قابل للتغيير `recipientHex` (ست عشري المستلِم) بقيمة ناتج كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:76]

```
77:                     val (hrp, data) = Bech32.decode(recipientNostrPubkey)
```
> يفكّك ناتج `Bech32.decode(recipientNostrPubkey)` إلى المتغيرين `hrp` و`data`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:77]

```
78:                     if (hrp != "npub") {
```
> يبدأ شرطاً يختبر إن كان `hrp` لا يساوي `"npub"`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:78]

```
79:                         Log.e(TAG, "NostrTransport: recipient key not npub (hrp=$hrp)")
```
> يستدعي `Log.e` بالوسم `TAG` والرسالة «مفتاح المستلِم ليس npub (hrp=$hrp)». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:79]

```
80:                         return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:80]

```
81:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:81]

```
82:                     data.joinToString("") { "%02x".format(it) }
```
> يعيد كقيمة للكتلة سلسلة دمج عناصر `data` بفاصل فارغ، حيث يُنسَّق كل عنصر `it` كست عشري بخانتين عبر `"%02x".format(it)`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:82]

```
83:                 } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) في المتغير `e`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:83]

```
84:                     Log.e(TAG, "NostrTransport: failed to decode npub -> hex: $e")
```
> يستدعي `Log.e` بالوسم `TAG` والرسالة «فشل فكّ npub إلى ست عشري: $e». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:84]

```
85:                     return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:85]

```
86:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:86]

```
87:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:87]

```
88:                 // Strict: lookup the recipient's current BitChat peer ID using favorites mapping
```
> تعليق: «صارم: ابحث عن معرّف قرين BitChat الحالي للمستلِم باستخدام ربط المُفضَّلات». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:88]

```
89:                 val recipientPeerIDForEmbed = try {
```
> يعرّف متغيراً غير قابل للتغيير `recipientPeerIDForEmbed` (معرّف قرين المستلِم للتضمين) بقيمة ناتج كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:89]

```
90:                     com.bitchat.android.favorites.FavoritesPersistenceService.shared
```
> يصل إلى الكائن `shared` من `FavoritesPersistenceService` (خدمة استمرار المُفضَّلات) ضمن `com.bitchat.android.favorites`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:90]

```
91:                         .findPeerIDForNostrPubkey(recipientNostrPubkey)
```
> يستدعي `findPeerIDForNostrPubkey(recipientNostrPubkey)` على الكائن السابق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:91]

```
92:                 } catch (_: Exception) { null }
```
> يلتقط استثناءً (Exception) دون تسمية ويعيد `null` كقيمة للكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:92]

```
93:                 if (recipientPeerIDForEmbed.isNullOrBlank()) {
```
> يبدأ شرطاً يختبر إن كان `recipientPeerIDForEmbed` فارغاً أو `null` عبر `isNullOrBlank()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:93]

```
94:                     Log.e(TAG, "NostrTransport: no peerID stored for recipient npub; cannot embed PM. npub=${recipientNostrPubkey.take(16)}...")
```
> يستدعي `Log.e` بالوسم `TAG` والرسالة «لا معرّف قرين مخزّن لـ npub المستلِم؛ تعذّر تضمين الرسالة الخاصة. npub=» مع أول 16 محرفاً من `recipientNostrPubkey`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:94]

```
95:                     return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:95]

```
96:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:96]

```
97:                 val embedded = NostrEmbeddedBitChat.encodePMForNostr(
```
> يعرّف متغيراً غير قابل للتغيير `embedded` (المُضمَّن) بقيمة ناتج استدعاء `NostrEmbeddedBitChat.encodePMForNostr(...)` ويبدأ تمرير معطياته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:97]

```
98:                     content = content,
```
> يمرّر المعطى `content` بقيمة المتغير `content`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:98]

```
99:                     messageID = messageID,
```
> يمرّر المعطى `messageID` بقيمة المتغير `messageID`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:99]

```
100:                     recipientPeerID = recipientPeerIDForEmbed,
```
> يمرّر المعطى `recipientPeerID` بقيمة المتغير `recipientPeerIDForEmbed`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:100]

```
101:                     senderPeerID = senderPeerID
```
> يمرّر المعطى `senderPeerID` بقيمة الخاصية `senderPeerID`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:101]

```
102:                 )
```
> يغلق استدعاء `encodePMForNostr`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:102]

```
103:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:103]

```
104:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:104]

```
105:                 if (embedded == null) {
```
> يبدأ شرطاً يختبر إن كان `embedded` يساوي `null`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:105]

```
106:                     Log.e(TAG, "NostrTransport: failed to embed PM packet")
```
> يستدعي `Log.e` بالوسم `TAG` والرسالة «فشل تضمين حزمة الرسالة الخاصة». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:106]

```
107:                     return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:107]

```
108:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:108]

```
109:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:109]

```
110:                 val giftWraps = NostrProtocol.createPrivateMessage(
```
> يعرّف متغيراً غير قابل للتغيير `giftWraps` (أغلفة الهدية) بقيمة ناتج استدعاء `NostrProtocol.createPrivateMessage(...)` ويبدأ تمرير معطياته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:110]

```
111:                     content = embedded,
```
> يمرّر المعطى `content` بقيمة المتغير `embedded`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:111]

```
112:                     recipientPubkey = recipientHex,
```
> يمرّر المعطى `recipientPubkey` بقيمة المتغير `recipientHex`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:112]

```
113:                     senderIdentity = senderIdentity
```
> يمرّر المعطى `senderIdentity` بقيمة المتغير `senderIdentity`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:113]

```
114:                 )
```
> يغلق استدعاء `createPrivateMessage`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:114]

```
115:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:115]

```
116:                 giftWraps.forEach { event ->
```
> يكرّر على عناصر `giftWraps` عبر `forEach` مسمّياً كل عنصر `event`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:116]

```
117:                     Log.d(TAG, "NostrTransport: sending PM giftWrap id=${event.id.take(16)}...")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة تعرض أول 16 محرفاً من `event.id`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:117]

```
118:                     NostrRelayManager.getInstance(context).sendEvent(event)
```
> يستدعي `sendEvent(event)` على نسخة `NostrRelayManager.getInstance(context)` (مدير مُرحِّل Nostr). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:118]

```
119:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:119]

```
120:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:120]

```
121:             } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) في المتغير `e`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:121]

```
122:                 Log.e(TAG, "Failed to send private message via Nostr: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` والرسالة «فشل إرسال الرسالة الخاصة عبر Nostr: » مع `e.message`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:122]

```
123:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:123]

```
124:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:124]

```
125:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:125]

```
126:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:126]

```
127:     fun sendReadReceipt(receipt: ReadReceipt, to: String) {
```
> يعرّف الدالة `sendReadReceipt` (أرسل إيصال القراءة) التي تأخذ `receipt` من نوع `ReadReceipt` و`to` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:127]

```
128:         // Enqueue and process with throttling to avoid relay rate limits
```
> تعليق: «أدخِل في الطابور وعالِج مع تخفيض المعدل لتجنّب حدود معدل المُرحِّل». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:128]

```
129:         readQueue.offer(QueuedRead(receipt, to))
```
> يستدعي `offer` على `readQueue` مضيفاً نسخة جديدة من `QueuedRead(receipt, to)`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:129]

```
130:         processReadQueueIfNeeded()
```
> يستدعي الدالة `processReadQueueIfNeeded()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:130]

```
131:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:131]

```
132:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:132]

```
133:     private fun processReadQueueIfNeeded() {
```
> يعرّف الدالة الخاصة `processReadQueueIfNeeded` (عالِج طابور القراءة عند الحاجة). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:133]

```
134:         if (isSendingReadAcks) return
```
> يعيد (يخرج من الدالة) إن كان `isSendingReadAcks` صحيحاً. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:134]

```
135:         if (readQueue.isEmpty()) return
```
> يعيد (يخرج من الدالة) إن كان `readQueue` فارغاً عبر `isEmpty()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:135]

```
136:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:136]

```
137:         isSendingReadAcks = true
```
> يسند القيمة `true` إلى `isSendingReadAcks`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:137]

```
138:         sendNextReadAck()
```
> يستدعي الدالة `sendNextReadAck()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:138]

```
139:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:139]

```
140:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:140]

```
141:     private fun sendNextReadAck() {
```
> يعرّف الدالة الخاصة `sendNextReadAck` (أرسل تأكيد القراءة التالي). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:141]

```
142:         val item = readQueue.poll()
```
> يعرّف متغيراً غير قابل للتغيير `item` (العنصر) بقيمة ناتج `readQueue.poll()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:142]

```
143:         if (item == null) {
```
> يبدأ شرطاً يختبر إن كان `item` يساوي `null`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:143]

```
144:             isSendingReadAcks = false
```
> يسند القيمة `false` إلى `isSendingReadAcks`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:144]

```
145:             return
```
> يعيد (يخرج من الدالة). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:145]

```
146:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:146]

```
147:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:147]

```
148:         transportScope.launch {
```
> يطلق كوروتيناً (launch) على النطاق `transportScope`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:148]

```
149:             try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:149]

```
150:                 var recipientNostrPubkey: String? = null
```
> يعرّف متغيراً محلياً قابلاً للتغيير `recipientNostrPubkey` (مفتاح Nostr العام للمستلِم) من نوع `String?` بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:150]

```
151:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:151]

```
152:                 // Try to resolve from favorites persistence service
```
> تعليق: «حاول الحلّ من خدمة استمرار المُفضَّلات». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:152]

```
153:                 recipientNostrPubkey = resolveNostrPublicKey(item.peerID)
```
> يسند إلى `recipientNostrPubkey` ناتج `resolveNostrPublicKey(item.peerID)`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:153]

```
154:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:154]

```
155:                 if (recipientNostrPubkey == null) {
```
> يبدأ شرطاً يختبر إن كان `recipientNostrPubkey` يساوي `null`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:155]

```
156:                     Log.w(TAG, "No Nostr public key found for read receipt to: ${item.peerID}")
```
> يستدعي `Log.w` بالوسم `TAG` والرسالة «لم يُعثر على مفتاح Nostr عام لإيصال القراءة إلى: » مع `item.peerID`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:156]

```
157:                     scheduleNextReadAck()
```
> يستدعي الدالة `scheduleNextReadAck()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:157]

```
158:                     return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:158]

```
159:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:159]

```
160:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:160]

```
161:                 val senderIdentity = NostrIdentityBridge.getCurrentNostrIdentity(context)
```
> يعرّف متغيراً غير قابل للتغيير `senderIdentity` (هوية المرسِل) بقيمة ناتج `NostrIdentityBridge.getCurrentNostrIdentity(context)`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:161]

```
162:                 if (senderIdentity == null) {
```
> يبدأ شرطاً يختبر إن كان `senderIdentity` يساوي `null`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:162]

```
163:                     Log.e(TAG, "No Nostr identity available for read receipt")
```
> يستدعي `Log.e` بالوسم `TAG` والرسالة «لا توجد هوية Nostr متاحة لإيصال القراءة». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:163]

```
164:                     scheduleNextReadAck()
```
> يستدعي الدالة `scheduleNextReadAck()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:164]

```
165:                     return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:165]

```
166:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:166]

```
167:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:167]

```
168:                 Log.d(TAG, "NostrTransport: preparing READ ack for id=${item.receipt.originalMessageID.take(8)}... to ${recipientNostrPubkey.take(16)}...")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة تعرض أول 8 محارف من `item.receipt.originalMessageID` وأول 16 من `recipientNostrPubkey`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:168]

```
169:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:169]

```
170:                 // Convert recipient npub -> hex
```
> تعليق: «حوّل npub المستلِم إلى ست عشري». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:170]

```
171:                 val recipientHex = try {
```
> يعرّف متغيراً غير قابل للتغيير `recipientHex` (ست عشري المستلِم) بقيمة ناتج كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:171]

```
172:                     val (hrp, data) = Bech32.decode(recipientNostrPubkey)
```
> يفكّك ناتج `Bech32.decode(recipientNostrPubkey)` إلى المتغيرين `hrp` و`data`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:172]

```
173:                     if (hrp != "npub") {
```
> يبدأ شرطاً يختبر إن كان `hrp` لا يساوي `"npub"`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:173]

```
174:                         scheduleNextReadAck()
```
> يستدعي الدالة `scheduleNextReadAck()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:174]

```
175:                         return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:175]

```
176:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:176]

```
177:                     data.joinToString("") { "%02x".format(it) }
```
> يعيد كقيمة للكتلة سلسلة دمج عناصر `data` بفاصل فارغ، حيث يُنسَّق كل عنصر `it` كست عشري بخانتين عبر `"%02x".format(it)`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:177]

```
178:                 } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) في المتغير `e`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:178]

```
179:                     scheduleNextReadAck()
```
> يستدعي الدالة `scheduleNextReadAck()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:179]

```
180:                     return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:180]

```
181:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:181]

```
182:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:182]

```
183:                 val ack = NostrEmbeddedBitChat.encodeAckForNostr(
```
> يعرّف متغيراً غير قابل للتغيير `ack` (التأكيد) بقيمة ناتج استدعاء `NostrEmbeddedBitChat.encodeAckForNostr(...)` ويبدأ تمرير معطياته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:183]

```
184:                     type = NoisePayloadType.READ_RECEIPT,
```
> يمرّر المعطى `type` بقيمة `NoisePayloadType.READ_RECEIPT`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:184]

```
185:                     messageID = item.receipt.originalMessageID,
```
> يمرّر المعطى `messageID` بقيمة `item.receipt.originalMessageID`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:185]

```
186:                     recipientPeerID = item.peerID,
```
> يمرّر المعطى `recipientPeerID` بقيمة `item.peerID`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:186]

```
187:                     senderPeerID = senderPeerID
```
> يمرّر المعطى `senderPeerID` بقيمة الخاصية `senderPeerID`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:187]

```
188:                 )
```
> يغلق استدعاء `encodeAckForNostr`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:188]

```
189:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:189]

```
190:                 if (ack == null) {
```
> يبدأ شرطاً يختبر إن كان `ack` يساوي `null`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:190]

```
191:                     Log.e(TAG, "NostrTransport: failed to embed READ ack")
```
> يستدعي `Log.e` بالوسم `TAG` والرسالة «فشل تضمين تأكيد القراءة». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:191]

```
192:                     scheduleNextReadAck()
```
> يستدعي الدالة `scheduleNextReadAck()`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:192]

```
193:                     return@launch
```
> يخرج من الكوروتين المطلق عبر `return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:193]

```
194:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:194]

```
195:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:195]

```
196:                 val giftWraps = NostrProtocol.createPrivateMessage(
```
> يعرّف متغيراً غير قابل للتغيير `giftWraps` (أغلفة الهدية) بقيمة ناتج استدعاء `NostrProtocol.createPrivateMessage(...)` ويبدأ تمرير معطياته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:196]

```
197:                     content = ack,
```
> يمرّر المعطى `content` بقيمة المتغير `ack`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:197]

```
198:                     recipientPubkey = recipientHex,
```
> يمرّر المعطى `recipientPubkey` بقيمة المتغير `recipientHex`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:198]

```
199:                     senderIdentity = senderIdentity
```
> يمرّر المعطى `senderIdentity` بقيمة المتغير `senderIdentity`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:199]

```
200:                 )
```
> يغلق استدعاء `createPrivateMessage`. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:200]
