# شريحة — app/src/main/java/com/bitchat/android/services/MessageRouter.kt (الأسطر 1–200)

```
1: package com.bitchat.android.services
```
> يعلن أنّ هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.services`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من حزمة أندرويد `android.content`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` (سجلّ) من حزمة أندرويد `android.util`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:4]

```
5: import com.bitchat.android.mesh.MeshService
```
> يستورد الصنف `MeshService` (خدمة الشبكة المتشابكة) من حزمة `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:5]

```
6: import com.bitchat.android.model.ReadReceipt
```
> يستورد الصنف `ReadReceipt` (إيصال القراءة) من حزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:6]

```
7: import com.bitchat.android.nostr.NostrTransport
```
> يستورد الصنف `NostrTransport` (ناقل Nostr) من حزمة `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:8]

```
9: /**
```
> بداية تعليق توثيقي (KDoc). تعليق: بداية الكتلة التوثيقية. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:9]

```
10:  * Routes messages between local mesh transports and Nostr, matching iOS behavior.
```
> تعليق: يوجّه الرسائل بين نواقل الشبكة المتشابكة المحلية وNostr، بما يطابق سلوك iOS. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:10]

```
11:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:11]

```
12: class MessageRouter private constructor(
```
> يعرّف الصنف `MessageRouter` (موجّه الرسائل) ببانٍ (constructor) خاص (private)، وتبدأ قائمة معاملاته. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:12]

```
13:     private val context: Context,
```
> يعرّف معامل الباني `context` من نوع `Context` كحقل ثابت خاص (private val). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:13]

```
14:     private var mesh: MeshService,
```
> يعرّف معامل الباني `mesh` من نوع `MeshService` كحقل متغيّر خاص (private var). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:14]

```
15:     private val nostr: NostrTransport
```
> يعرّف معامل الباني `nostr` من نوع `NostrTransport` كحقل ثابت خاص (private val). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:15]

```
16: ) {
```
> إغلاق قائمة معاملات الباني وفتح جسم الصنف. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:16]

```
17:     companion object {
```
> يفتح كائناً مرافقاً (companion object) للصنف. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:17]

```
18:         private const val TAG = "MessageRouter"
```
> يعرّف ثابتاً خاصاً وقت الترجمة `TAG` (وسم) بقيمة نصية `"MessageRouter"`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:18]

```
19:         @Volatile private var INSTANCE: MessageRouter? = null
```
> يعرّف حقلاً متغيّراً خاصاً `INSTANCE` (النسخة) من نوع `MessageRouter?` قابل للعدم بقيمة ابتدائية `null`، موسوماً بـ`@Volatile` (متطاير). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:19]

```
20:         fun tryGetInstance(): MessageRouter? = INSTANCE
```
> يعرّف الدالة `tryGetInstance` (محاولة الحصول على النسخة) التي تُعيد قيمة `INSTANCE` من نوع `MessageRouter?`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:20]

```
21:         fun getInstance(context: Context, mesh: MeshService): MessageRouter {
```
> يعرّف الدالة `getInstance` (الحصول على النسخة) بمعاملين `context` من نوع `Context` و`mesh` من نوع `MeshService`، وتُعيد `MessageRouter`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:21]

```
22:             val instance = INSTANCE ?: synchronized(this) {
```
> يعرّف المتغيّر `instance` بقيمة `INSTANCE`، وإن كان عدماً يُنفّذ كتلة `synchronized(this)` (متزامنة على الكائن المرافق). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:22]

```
23:                 INSTANCE ?: run {
```
> داخل الكتلة المتزامنة، يُعيد `INSTANCE`، وإن كان عدماً يُنفّذ كتلة `run`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:23]

```
24:                     val nostr = NostrTransport.getInstance(context)
```
> يعرّف المتغيّر `nostr` بنتيجة استدعاء `NostrTransport.getInstance(context)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:24]

```
25:                     MessageRouter(context.applicationContext, mesh, nostr).also { instance ->
```
> يُنشئ نسخة `MessageRouter` بالمعاملات `context.applicationContext` و`mesh` و`nostr`، ثم يستدعي `also` معطياً النسخة الاسم `instance`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:25]

```
26:                         // Register for favorites changes to flush outbox
```
> تعليق: التسجيل لتغيّرات المفضّلين لتفريغ صندوق الصادر. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:26]

```
27:                         try {
```
> يفتح كتلة `try` (محاولة) لالتقاط الاستثناءات. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:27]

```
28:                             com.bitchat.android.favorites.FavoritesPersistenceService.shared.addListener(instance.favoriteListener)
```
> يستدعي `addListener` على `FavoritesPersistenceService.shared` (خدمة حفظ المفضّلين، النسخة المشتركة) مُمرِّراً `instance.favoriteListener`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:28]

```
29:                         } catch (_: Exception) {}
```
> يلتقط أيّ `Exception` (استثناء) باسم مُهمَل ويتجاهله بجسم فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:29]

```
30:                         INSTANCE = instance
```
> يُسند `instance` إلى الحقل `INSTANCE`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:30]

```
31:                     }
```
> إغلاق نطاق كتلة `also`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:31]

```
32:                 }
```
> إغلاق نطاق كتلة `run`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:32]

```
33:             }
```
> إغلاق نطاق الكتلة المتزامنة `synchronized`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:33]

```
34:             // Always update mesh reference and sync peer ID
```
> تعليق: حدِّث دائماً مرجع الشبكة المتشابكة وزامِن معرّف النِّد. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:34]

```
35:             instance.mesh = mesh
```
> يُسند `mesh` إلى الحقل `instance.mesh`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:35]

```
36:             instance.nostr.senderPeerID = mesh.myPeerID
```
> يُسند `mesh.myPeerID` إلى الخاصية `instance.nostr.senderPeerID` (معرّف نِدّ المرسِل). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:36]

```
37:             return instance
```
> يُعيد `instance`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:37]

```
38:         }
```
> إغلاق نطاق الدالة `getInstance`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:38]

```
39:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:39]

```
40: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:40]

```
41:     // Outbox: peerID -> queued (content, nickname, messageID)
```
> تعليق: صندوق الصادر: معرّف النِّد ⇐ مصفوفة منتظِرة من (المحتوى، الاسم المستعار، معرّف الرسالة). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:41]

```
42:     private val outbox = mutableMapOf<String, MutableList<Triple<String, String, String>>>()
```
> يعرّف الحقل الثابت الخاص `outbox` (صندوق الصادر) كخريطة قابلة للتغيير مفاتيحها `String` وقيمها قائمة قابلة للتغيير من `Triple<String, String, String>`، مهيَّأة فارغة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:42]

```
43: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:43]

```
44:     // Listener for favorites changes to flush outbox when npub mapping appears/changes
```
> تعليق: مستمِع لتغيّرات المفضّلين لتفريغ صندوق الصادر عند ظهور/تغيّر ربط الـnpub. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:44]

```
45:     private val favoriteListener = object: com.bitchat.android.favorites.FavoritesChangeListener {
```
> يعرّف الحقل الثابت الخاص `favoriteListener` (مستمِع المفضّلين) ككائن مجهول يحقّق الواجهة `FavoritesChangeListener` (مستمِع تغيّر المفضّلين). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:45]

```
46: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:46]

```
47:         override fun onFavoriteChanged(noiseKeyHex: String) {
```
> يُعيد تعريف (override) الدالة `onFavoriteChanged` (عند تغيّر المفضّل) بمعامل `noiseKeyHex` من نوع `String`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:47]

```
48:             flushOutboxFor(noiseKeyHex)
```
> يستدعي `flushOutboxFor` مُمرِّراً `noiseKeyHex`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:48]

```
49:             // Also try 16-hex short id commonly used in UI if any client used that
```
> تعليق: جرّب أيضاً المعرّف القصير ذا الستّ عشرة خانة ست عشرية الشائع في الواجهة إن استعمله أيّ عميل. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:49]

```
50:             val shortId = noiseKeyHex.take(16)
```
> يعرّف المتغيّر `shortId` (المعرّف القصير) بنتيجة `noiseKeyHex.take(16)` أي أوّل ست عشرة محرفاً. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:50]

```
51:             flushOutboxFor(shortId)
```
> يستدعي `flushOutboxFor` مُمرِّراً `shortId`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:51]

```
52:         }
```
> إغلاق نطاق الدالة `onFavoriteChanged`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:52]

```
53:         override fun onAllCleared() {
```
> يُعيد تعريف الدالة `onAllCleared` (عند مسح الكلّ) بلا معاملات. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:53]

```
54:             // Nothing special; leave queued items until routing becomes possible
```
> تعليق: لا شيء خاص؛ اترك العناصر المنتظِرة حتى يصبح التوجيه ممكناً. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:54]

```
55:         }
```
> إغلاق نطاق الدالة `onAllCleared` (وجسمها فارغ من التنفيذ). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:55]

```
56:     }
```
> إغلاق نطاق الكائن المجهول `favoriteListener`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:56]

```
57: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:57]

```
58:     fun sendPrivate(content: String, toPeerID: String, recipientNickname: String, messageID: String) {
```
> يعرّف الدالة `sendPrivate` (إرسال خاص) بمعاملات `content` و`toPeerID` و`recipientNickname` و`messageID` كلّها من نوع `String`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:58]

```
59:         // First: if this is a geohash DM alias (nostr_<pub16>), route via Nostr using global registry
```
> تعليق: أولاً: إن كان هذا اسماً مستعاراً لرسالة مباشرة بترميز جغرافي (nostr_<pub16>)، فوجِّه عبر Nostr باستعمال السجلّ العالمي. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:59]

```
60:         if (com.bitchat.android.nostr.GeohashAliasRegistry.contains(toPeerID)) {
```
> يفحص بـ`if` ما إذا كان `GeohashAliasRegistry` (سجلّ الأسماء المستعارة للترميز الجغرافي) يحتوي `toPeerID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:60]

```
61:             Log.d(TAG, "Routing PM via Nostr (geohash) to alias ${toPeerID.take(12)}… id=${messageID.take(8)}…")
```
> يسجّل رسالة تنقيح (Log.d) بالوسم `TAG` نصّها يوجّه رسالة خاصة عبر Nostr (ترميز جغرافي) إلى الاسم المستعار بأوّل اثني عشر محرفاً من `toPeerID` ومعرّف بأوّل ثمانية محارف من `messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:61]

```
62:             val recipientHex = com.bitchat.android.nostr.GeohashAliasRegistry.get(toPeerID)
```
> يعرّف المتغيّر `recipientHex` (سداسي المستقبِل) بنتيجة `GeohashAliasRegistry.get(toPeerID)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:62]

```
63:             if (recipientHex != null) {
```
> يفحص بـ`if` ما إذا كان `recipientHex` ليس عدماً. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:63]

```
64:                 // Resolve the conversation's source geohash, so we can send from anywhere
```
> تعليق: استخرِج الترميز الجغرافي المصدر للمحادثة، لكي نستطيع الإرسال من أيّ مكان. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:64]

```
65:                 val sourceGeohash = com.bitchat.android.nostr.GeohashConversationRegistry.get(toPeerID)
```
> يعرّف المتغيّر `sourceGeohash` (الترميز الجغرافي المصدر) بنتيجة `GeohashConversationRegistry.get(toPeerID)` (سجلّ محادثات الترميز الجغرافي). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:65]

```
66: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:66]

```
67:                 // If repository knows the source geohash, pass it so NostrTransport derives the correct identity
```
> تعليق: إن كان المستودع يعرف الترميز الجغرافي المصدر، فمرّره لكي يشتقّ NostrTransport الهويّة الصحيحة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:67]

```
68:                 nostr.sendPrivateMessageGeohash(content, recipientHex, messageID, sourceGeohash)
```
> يستدعي `nostr.sendPrivateMessageGeohash` (إرسال رسالة خاصة بترميز جغرافي) مُمرِّراً `content` و`recipientHex` و`messageID` و`sourceGeohash`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:68]

```
69:                 return
```
> يُنهي الدالة بالعودة (return) بلا قيمة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:69]

```
70:             }
```
> إغلاق نطاق كتلة `if (recipientHex != null)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:70]

```
71:         }
```
> إغلاق نطاق كتلة `if` الخاصة باحتواء السجلّ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:71]

```
72: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:72]

```
73:         val hasMesh = isConnected(mesh, toPeerID)
```
> يعرّف المتغيّر `hasMesh` (يملك شبكة متشابكة) بنتيجة استدعاء `isConnected(mesh, toPeerID)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:73]

```
74:         if (isReady(mesh, toPeerID)) {
```
> يفحص بـ`if` نتيجة `isReady(mesh, toPeerID)` (هل جاهز). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:74]

```
75:             Log.d(TAG, "Routing PM via mesh to ${toPeerID} msg_id=${messageID.take(8)}…")
```
> يسجّل رسالة تنقيح نصّها يوجّه رسالة خاصة عبر الشبكة المتشابكة إلى `toPeerID` مع معرّف الرسالة بأوّل ثمانية محارف من `messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:75]

```
76:             mesh.sendPrivateMessage(content, toPeerID, recipientNickname, messageID)
```
> يستدعي `mesh.sendPrivateMessage` مُمرِّراً `content` و`toPeerID` و`recipientNickname` و`messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:76]

```
77:         } else if (canSendViaNostr(toPeerID)) {
```
> فرع `else if` يفحص نتيجة `canSendViaNostr(toPeerID)` (هل يمكن الإرسال عبر Nostr). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:77]

```
78:             Log.d(TAG, "Routing PM via Nostr to ${toPeerID.take(32)}… msg_id=${messageID.take(8)}…")
```
> يسجّل رسالة تنقيح نصّها يوجّه رسالة خاصة عبر Nostr إلى أوّل اثنين وثلاثين محرفاً من `toPeerID` مع معرّف الرسالة بأوّل ثمانية محارف من `messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:78]

```
79:             nostr.sendPrivateMessage(content, toPeerID, recipientNickname, messageID)
```
> يستدعي `nostr.sendPrivateMessage` مُمرِّراً `content` و`toPeerID` و`recipientNickname` و`messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:79]

```
80:         } else {
```
> فرع `else` (وإلّا). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:80]

```
81:             Log.d(TAG, "Queued PM for ${toPeerID} (no mesh, no Nostr mapping) msg_id=${messageID.take(8)}…")
```
> يسجّل رسالة تنقيح نصّها وضع رسالة خاصة في الانتظار لـ`toPeerID` (لا شبكة متشابكة، لا ربط Nostr) مع معرّف الرسالة بأوّل ثمانية محارف من `messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:81]

```
82:             val q = outbox.getOrPut(toPeerID) { mutableListOf() }
```
> يعرّف المتغيّر `q` بنتيجة `outbox.getOrPut(toPeerID)` التي تُعيد القائمة الموجودة أو تُنشئ قائمة قابلة للتغيير فارغة وتضعها. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:82]

```
83:             q.add(Triple(content, recipientNickname, messageID))
```
> يستدعي `q.add` مُضيفاً ثلاثيّة `Triple` من `content` و`recipientNickname` و`messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:83]

```
84:             Log.d(TAG, "Initiating noise handshake after queueing PM for ${toPeerID.take(8)}…")
```
> يسجّل رسالة تنقيح نصّها بدء مصافحة Noise بعد وضع الرسالة الخاصة في الانتظار لأوّل ثمانية محارف من `toPeerID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:84]

```
85:             if (hasMesh) mesh.initiateNoiseHandshake(toPeerID)
```
> إن كان `hasMesh` صحيحاً يستدعي `mesh.initiateNoiseHandshake(toPeerID)` (بدء مصافحة Noise). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:85]

```
86:         }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:86]

```
87:     }
```
> إغلاق نطاق الدالة `sendPrivate`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:87]

```
88: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:88]

```
89:     fun sendReadReceipt(receipt: ReadReceipt, toPeerID: String) {
```
> يعرّف الدالة `sendReadReceipt` (إرسال إيصال قراءة) بمعاملين `receipt` من نوع `ReadReceipt` و`toPeerID` من نوع `String`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:89]

```
90:         if (isReady(mesh, toPeerID)) {
```
> يفحص بـ`if` نتيجة `isReady(mesh, toPeerID)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:90]

```
91:             Log.d(TAG, "Routing READ via mesh to ${toPeerID.take(8)}… id=${receipt.originalMessageID.take(8)}…")
```
> يسجّل رسالة تنقيح نصّها يوجّه إيصال قراءة عبر الشبكة المتشابكة إلى أوّل ثمانية محارف من `toPeerID` مع معرّف بأوّل ثمانية محارف من `receipt.originalMessageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:91]

```
92:             mesh.sendReadReceipt(receipt.originalMessageID, toPeerID, mesh.getPeerNicknames()[toPeerID] ?: mesh.myPeerID)
```
> يستدعي `mesh.sendReadReceipt` مُمرِّراً `receipt.originalMessageID` و`toPeerID` والاسم المستعار من `mesh.getPeerNicknames()[toPeerID]` أو `mesh.myPeerID` عند العدم. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:92]

```
93:         } else {
```
> فرع `else`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:93]

```
94:             Log.d(TAG, "Routing READ via Nostr to ${toPeerID.take(8)}… id=${receipt.originalMessageID.take(8)}…")
```
> يسجّل رسالة تنقيح نصّها يوجّه إيصال قراءة عبر Nostr إلى أوّل ثمانية محارف من `toPeerID` مع معرّف بأوّل ثمانية محارف من `receipt.originalMessageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:94]

```
95:             nostr.sendReadReceipt(receipt, toPeerID)
```
> يستدعي `nostr.sendReadReceipt` مُمرِّراً `receipt` و`toPeerID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:95]

```
96:         }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:96]

```
97:     }
```
> إغلاق نطاق الدالة `sendReadReceipt`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:97]

```
98: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:98]

```
99:     fun sendDeliveryAck(messageID: String, toPeerID: String) {
```
> يعرّف الدالة `sendDeliveryAck` (إرسال إقرار تسليم) بمعاملين `messageID` و`toPeerID` كلاهما من نوع `String`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:99]

```
100:         // Mesh delivery ACKs are sent by the receiver automatically.
```
> تعليق: إقرارات تسليم الشبكة المتشابكة يرسلها المستقبِل تلقائياً. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:100]

```
101:         // Only route via Nostr when mesh path isn't available or when this is a geohash alias
```
> تعليق: وجّه عبر Nostr فقط حين لا يتوفّر مسار الشبكة المتشابكة أو حين يكون هذا اسماً مستعاراً بترميز جغرافي. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:101]

```
102:         if (com.bitchat.android.nostr.GeohashAliasRegistry.contains(toPeerID)) {
```
> يفحص بـ`if` ما إذا كان `GeohashAliasRegistry` يحتوي `toPeerID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:102]

```
103:             val recipientHex = com.bitchat.android.nostr.GeohashAliasRegistry.get(toPeerID)
```
> يعرّف المتغيّر `recipientHex` بنتيجة `GeohashAliasRegistry.get(toPeerID)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:103]

```
104:             if (recipientHex != null) {
```
> يفحص بـ`if` ما إذا كان `recipientHex` ليس عدماً. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:104]

```
105:                 nostr.sendDeliveryAckGeohash(messageID, recipientHex, try { com.bitchat.android.nostr.NostrIdentityBridge.getCurrentNostrIdentity(context)!! } catch (_: Exception) { return })
```
> يستدعي `nostr.sendDeliveryAckGeohash` (إقرار تسليم بترميز جغرافي) مُمرِّراً `messageID` و`recipientHex` والهويّة من `NostrIdentityBridge.getCurrentNostrIdentity(context)!!` ضمن `try`، وعند الاستثناء يعود (return) من الدالة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:105]

```
106:                 return
```
> يُنهي الدالة بالعودة بلا قيمة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:106]

```
107:             }
```
> إغلاق نطاق كتلة `if (recipientHex != null)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:107]

```
108:         }
```
> إغلاق نطاق كتلة `if` الخاصة باحتواء السجلّ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:108]

```
109:         if (!((mesh.getPeerInfo(toPeerID)?.isConnected == true) && mesh.hasEstablishedSession(toPeerID))) {
```
> يفحص بـ`if` نفي شرط مركّب: أنّ `mesh.getPeerInfo(toPeerID)?.isConnected` يساوي صحيحاً ويوجد جلسة مؤسَّسة عبر `mesh.hasEstablishedSession(toPeerID)`؛ أي ينفِّذ عند عدم التحقّق. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:109]

```
110:             nostr.sendDeliveryAck(messageID, toPeerID)
```
> يستدعي `nostr.sendDeliveryAck` مُمرِّراً `messageID` و`toPeerID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:110]

```
111:         }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:111]

```
112:     }
```
> إغلاق نطاق الدالة `sendDeliveryAck`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:112]

```
113: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:113]

```
114:     fun sendFavoriteNotification(toPeerID: String, isFavorite: Boolean) {
```
> يعرّف الدالة `sendFavoriteNotification` (إرسال إشعار مفضّل) بمعاملين `toPeerID` من نوع `String` و`isFavorite` من نوع `Boolean`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:114]

```
115:         if (mesh.getPeerInfo(toPeerID)?.isConnected == true && mesh.hasEstablishedSession(toPeerID)) {
```
> يفحص بـ`if` أنّ `mesh.getPeerInfo(toPeerID)?.isConnected` يساوي صحيحاً وأنّ `mesh.hasEstablishedSession(toPeerID)` صحيح. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:115]

```
116:             val myNpub = try { com.bitchat.android.nostr.NostrIdentityBridge.getCurrentNostrIdentity(context)?.npub } catch (_: Exception) { null }
```
> يعرّف المتغيّر `myNpub` (الـnpub الخاص بي) بقيمة `NostrIdentityBridge.getCurrentNostrIdentity(context)?.npub` ضمن `try`، وعند الاستثناء بقيمة `null`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:116]

```
117:             val content = if (isFavorite) "[FAVORITED]:${myNpub ?: ""}" else "[UNFAVORITED]:${myNpub ?: ""}"
```
> يعرّف المتغيّر `content` بنصّ `"[FAVORITED]:"` متبوعاً بـ`myNpub` أو نصّ فارغ إن كان `isFavorite` صحيحاً، وإلّا `"[UNFAVORITED]:"` متبوعاً بالمثل. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:117]

```
118:             val nickname = mesh.getPeerNicknames()[toPeerID] ?: toPeerID
```
> يعرّف المتغيّر `nickname` (الاسم المستعار) بقيمة `mesh.getPeerNicknames()[toPeerID]` أو `toPeerID` عند العدم. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:118]

```
119:             mesh.sendPrivateMessage(content, toPeerID, nickname, null)
```
> يستدعي `mesh.sendPrivateMessage` مُمرِّراً `content` و`toPeerID` و`nickname` و`null` لمعرّف الرسالة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:119]

```
120:         } else {
```
> فرع `else`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:120]

```
121:             nostr.sendFavoriteNotification(toPeerID, isFavorite)
```
> يستدعي `nostr.sendFavoriteNotification` مُمرِّراً `toPeerID` و`isFavorite`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:121]

```
122:         }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:122]

```
123:     }
```
> إغلاق نطاق الدالة `sendFavoriteNotification`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:123]

```
124: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:124]

```
125:     // Flush any queued messages for a specific peerID
```
> تعليق: فرِّغ أيّ رسائل منتظِرة لمعرّف نِدّ محدّد. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:125]

```
126:     fun flushOutboxFor(peerID: String) {
```
> يعرّف الدالة `flushOutboxFor` (تفريغ صندوق الصادر لـ) بمعامل `peerID` من نوع `String`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:126]

```
127:         val queued = outbox[peerID] ?: return
```
> يعرّف المتغيّر `queued` (المنتظِر) بقيمة `outbox[peerID]`، وعند العدم يعود (return) من الدالة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:127]

```
128:         if (queued.isEmpty()) return
```
> إن كانت `queued` فارغة يعود من الدالة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:128]

```
129:         Log.d(TAG, "Flushing outbox for ${peerID.take(8)}… count=${queued.size}")
```
> يسجّل رسالة تنقيح نصّها تفريغ صندوق الصادر لأوّل ثمانية محارف من `peerID` مع العدد `queued.size`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:129]

```
130:         val iterator = queued.iterator()
```
> يعرّف المتغيّر `iterator` (المُكرِّر) بنتيجة `queued.iterator()`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:130]

```
131:         while (iterator.hasNext()) {
```
> حلقة `while` تستمرّ ما دام `iterator.hasNext()` صحيحاً (يوجد عنصر تالٍ). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:131]

```
132:             val (content, nickname, messageID) = iterator.next()
```
> يفكّك العنصر التالي من `iterator.next()` إلى المتغيّرات `content` و`nickname` و`messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:132]

```
133:             val hasMesh = isReady(mesh, peerID)
```
> يعرّف المتغيّر `hasMesh` بنتيجة `isReady(mesh, peerID)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:133]

```
134:             // If this is a noiseHex key, see if there is a connected mesh peer for this identity
```
> تعليق: إن كان هذا مفتاح noiseHex، فانظر هل يوجد نِدّ شبكة متشابكة متصل لهذه الهويّة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:134]

```
135:             if (!hasMesh && peerID.length == 64 && peerID.matches(Regex("^[0-9a-fA-F]+$"))) {
```
> يفحص بـ`if` أنّ `hasMesh` غير صحيح وطول `peerID` يساوي 64 ويطابق التعبير النمطي `^[0-9a-fA-F]+$` (ست عشري). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:135]

```
136:                 val meshPeer = resolvePeerForNoiseHex(peerID, mesh)
```
> يعرّف المتغيّر `meshPeer` (نِدّ الشبكة المتشابكة) بنتيجة `resolvePeerForNoiseHex(peerID, mesh)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:136]

```
137:                 if (meshPeer != null && isReady(mesh, meshPeer)) {
```
> يفحص بـ`if` أنّ `meshPeer` ليس عدماً وأنّ `isReady(mesh, meshPeer)` صحيح. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:137]

```
138:                     mesh.sendPrivateMessage(content, meshPeer, nickname, messageID)
```
> يستدعي `mesh.sendPrivateMessage` مُمرِّراً `content` و`meshPeer` و`nickname` و`messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:138]

```
139:                     iterator.remove()
```
> يستدعي `iterator.remove()` لحذف العنصر الحالي من القائمة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:139]

```
140:                     continue
```
> يتابع (continue) إلى التكرار التالي في الحلقة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:140]

```
141:                 }
```
> إغلاق نطاق كتلة `if (meshPeer != null && ...)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:141]

```
142:             }
```
> إغلاق نطاق كتلة `if (!hasMesh && ...)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:142]

```
143:             val canNostr = canSendViaNostr(peerID)
```
> يعرّف المتغيّر `canNostr` (يمكن Nostr) بنتيجة `canSendViaNostr(peerID)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:143]

```
144:             if (hasMesh) {
```
> يفحص بـ`if` ما إذا كان `hasMesh` صحيحاً. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:144]

```
145:                 mesh.sendPrivateMessage(content, peerID, nickname, messageID)
```
> يستدعي `mesh.sendPrivateMessage` مُمرِّراً `content` و`peerID` و`nickname` و`messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:145]

```
146:                 iterator.remove()
```
> يستدعي `iterator.remove()` لحذف العنصر الحالي. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:146]

```
147:             } else if (canNostr) {
```
> فرع `else if` يفحص ما إذا كان `canNostr` صحيحاً. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:147]

```
148:                 nostr.sendPrivateMessage(content, peerID, nickname, messageID)
```
> يستدعي `nostr.sendPrivateMessage` مُمرِّراً `content` و`peerID` و`nickname` و`messageID`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:148]

```
149:                 iterator.remove()
```
> يستدعي `iterator.remove()` لحذف العنصر الحالي. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:149]

```
150:             }
```
> إغلاق نطاق كتلة `if/else if`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:150]

```
151:         }
```
> إغلاق نطاق حلقة `while`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:151]

```
152:         if (queued.isEmpty()) {
```
> يفحص بـ`if` ما إذا كانت `queued` فارغة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:152]

```
153:             outbox.remove(peerID)
```
> يستدعي `outbox.remove(peerID)` لحذف مدخل المعرّف من الخريطة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:153]

```
154:         }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:154]

```
155:     }
```
> إغلاق نطاق الدالة `flushOutboxFor`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:155]

```
156: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:156]

```
157:     // Flush everything (rarely used)
```
> تعليق: فرِّغ كلّ شيء (نادر الاستعمال). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:157]

```
158:     fun flushAllOutbox() {
```
> يعرّف الدالة `flushAllOutbox` (تفريغ كلّ صندوق الصادر) بلا معاملات. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:158]

```
159:         outbox.keys.toList().forEach { flushOutboxFor(it) }
```
> يحوّل `outbox.keys` إلى قائمة ثمّ يكرّر بـ`forEach` مستدعياً `flushOutboxFor(it)` لكلّ مفتاح. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:159]

```
160:     }
```
> إغلاق نطاق الدالة `flushAllOutbox`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:160]

```
161: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:161]

```
162:     private fun canSendViaNostr(peerID: String): Boolean {
```
> يعرّف الدالة الخاصة `canSendViaNostr` بمعامل `peerID` من نوع `String` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:162]

```
163:         return try {
```
> يُعيد نتيجة كتلة `try`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:163]

```
164:             // Full Noise key hex
```
> تعليق: مفتاح Noise الكامل بالست عشري. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:164]

```
165:             if (peerID.length == 64 && peerID.matches(Regex("^[0-9a-fA-F]+$"))) {
```
> يفحص بـ`if` أنّ طول `peerID` يساوي 64 ويطابق التعبير النمطي الست عشري `^[0-9a-fA-F]+$`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:165]

```
166:                 val noiseKey = hexToBytes(peerID)
```
> يعرّف المتغيّر `noiseKey` (مفتاح Noise) بنتيجة `hexToBytes(peerID)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:166]

```
167:                 val fav = com.bitchat.android.favorites.FavoritesPersistenceService.shared.getFavoriteStatus(noiseKey)
```
> يعرّف المتغيّر `fav` (المفضّل) بنتيجة `FavoritesPersistenceService.shared.getFavoriteStatus(noiseKey)` (حالة المفضّل). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:167]

```
168:                 fav?.isMutual == true && fav.peerNostrPublicKey != null
```
> تُقيِّم تعبيراً يساوي صحيحاً إن كان `fav?.isMutual` صحيحاً (متبادل) و`fav.peerNostrPublicKey` ليس عدماً (المفتاح العام Nostr للنِّد). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:168]

```
169:             } else if (peerID.length == 16 && peerID.matches(Regex("^[0-9a-fA-F]+$"))) {
```
> فرع `else if` يفحص أنّ طول `peerID` يساوي 16 ويطابق التعبير النمطي الست عشري. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:169]

```
170:                 // Ephemeral 16-hex mesh ID: resolve via prefix match in favorites
```
> تعليق: معرّف شبكة متشابكة سريع الزوال ذو ست عشرة خانة ست عشرية: حلّه عبر مطابقة البادئة في المفضّلين. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:170]

```
171:                 val fav = com.bitchat.android.favorites.FavoritesPersistenceService.shared.getFavoriteStatus(peerID)
```
> يعرّف المتغيّر `fav` بنتيجة `FavoritesPersistenceService.shared.getFavoriteStatus(peerID)`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:171]

```
172:                 fav?.isMutual == true && fav.peerNostrPublicKey != null
```
> تُقيِّم تعبيراً يساوي صحيحاً إن كان `fav?.isMutual` صحيحاً و`fav.peerNostrPublicKey` ليس عدماً. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:172]

```
173:             } else {
```
> فرع `else`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:173]

```
174:                 false
```
> تُقيِّم القيمة `false` (خطأ). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:174]

```
175:             }
```
> إغلاق نطاق سلسلة `if/else if/else`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:175]

```
176:         } catch (_: Exception) { false }
```
> يلتقط أيّ `Exception` باسم مُهمَل ويُعيد `false`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:176]

```
177:     }
```
> إغلاق نطاق الدالة `canSendViaNostr`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:177]

```
178: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:178]

```
179:     private fun hexToBytes(hex: String): ByteArray {
```
> يعرّف الدالة الخاصة `hexToBytes` (ست عشري إلى بايتات) بمعامل `hex` من نوع `String` وتُعيد `ByteArray`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:179]

```
180:         val clean = if (hex.length % 2 == 0) hex else "0$hex"
```
> يعرّف المتغيّر `clean` (النظيف) بقيمة `hex` إن كان طوله زوجياً، وإلّا `hex` مسبوقاً بصفر `"0"`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:180]

```
181:         return clean.chunked(2).map { it.toInt(16).toByte() }.toByteArray()
```
> يُعيد `clean` مقطّعاً إلى أزواج بـ`chunked(2)`، يحوّل كلّ زوج إلى عدد بأساس 16 ثمّ إلى بايت، ويجمعها في `ByteArray`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:181]

```
182:     }
```
> إغلاق نطاق الدالة `hexToBytes`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:182]

```
183: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:183]

```
184:     private fun isConnected(service: MeshService, peerID: String): Boolean {
```
> يعرّف الدالة الخاصة `isConnected` (هل متصل) بمعاملين `service` من نوع `MeshService` و`peerID` من نوع `String` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:184]

```
185:         return try {
```
> يُعيد نتيجة كتلة `try`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:185]

```
186:             service.getPeerInfo(peerID)?.isConnected == true
```
> تُقيِّم ما إذا كان `service.getPeerInfo(peerID)?.isConnected` يساوي صحيحاً. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:186]

```
187:         } catch (_: Exception) {
```
> يلتقط أيّ `Exception` باسم مُهمَل. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:187]

```
188:             false
```
> تُقيِّم القيمة `false`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:188]

```
189:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:189]

```
190:     }
```
> إغلاق نطاق الدالة `isConnected`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:190]

```
191: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:191]

```
192:     private fun isReady(service: MeshService, peerID: String): Boolean {
```
> يعرّف الدالة الخاصة `isReady` (هل جاهز) بمعاملين `service` من نوع `MeshService` و`peerID` من نوع `String` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:192]

```
193:         return try {
```
> يُعيد نتيجة كتلة `try`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:193]

```
194:             service.getPeerInfo(peerID)?.isConnected == true &&
```
> تُقيِّم الجزء الأوّل من شرط مركّب: أنّ `service.getPeerInfo(peerID)?.isConnected` يساوي صحيحاً، ويتبعه `&&` للسطر التالي. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:194]

```
195:                 service.hasEstablishedSession(peerID)
```
> تُقيِّم الجزء الثاني من الشرط: نتيجة `service.hasEstablishedSession(peerID)` (هل أسّس جلسة). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:195]

```
196:         } catch (_: Exception) {
```
> يلتقط أيّ `Exception` باسم مُهمَل. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:196]

```
197:             false
```
> تُقيِّم القيمة `false`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:197]

```
198:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:198]

```
199:     }
```
> إغلاق نطاق الدالة `isReady`. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:199]

```
200: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:200]
