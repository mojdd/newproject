# شريحة — app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يُعلِن أنّ هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف `Log` من `android.util` لتسجيل الرسائل. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:3]

```
4: import com.bitchat.android.model.BitchatMessage
```
> يستورد الصنف `BitchatMessage` (رسالة بِت‑شات) من حزمة النماذج. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:4]

```
5: import com.bitchat.android.model.BitchatMessageType
```
> يستورد الصنف `BitchatMessageType` (نوع رسالة بِت‑شات) من حزمة النماذج. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:5]

```
6: import com.bitchat.android.model.IdentityAnnouncement
```
> يستورد الصنف `IdentityAnnouncement` (إعلان الهويّة) من حزمة النماذج. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:6]

```
7: import com.bitchat.android.model.RoutedPacket
```
> يستورد الصنف `RoutedPacket` (حزمة موجَّهة) من حزمة النماذج. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:7]

```
8: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف `BitchatPacket` (حزمة بِت‑شات) من حزمة البروتوكول. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:8]

```
9: import com.bitchat.android.protocol.MessageType
```
> يستورد الصنف `MessageType` (نوع الرسالة) من حزمة البروتوكول. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:9]

```
10: import com.bitchat.android.sync.PacketIdUtil
```
> يستورد الصنف `PacketIdUtil` (أداة معرّف الحزمة) من حزمة المزامنة (sync). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:10]

```
11: import com.bitchat.android.util.toHexString
```
> يستورد الدالة `toHexString` (التحويل إلى نصّ سداسي عشري) من حزمة الأدوات. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:11]

```
12: import kotlinx.coroutines.*
```
> يستورد كلّ ما في حزمة `kotlinx.coroutines` (الكوروتينات/الإجراءات المتزامنة). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:12]

```
13: import java.util.*
```
> يستورد كلّ ما في حزمة `java.util`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:13]

```
14: import kotlin.random.Random
```
> يستورد الصنف `Random` (المولّد العشوائي) من `kotlin.random`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:14]

```
15: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:15]

```
16: /**
```
> تعليق: بداية كتلة توثيق (تعليق Javadoc/KDoc). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:16]

```
17:  * Handles processing of different message types
```
> تعليق: «يتولّى معالجة أنواع الرسائل المختلفة». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:17]

```
18:  * Extracted from BluetoothMeshService for better separation of concerns
```
> تعليق: «مُستخرَج من BluetoothMeshService لفصلٍ أفضل للاهتمامات». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:18]

```
19:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:19]

```
20: class MessageHandler(private val myPeerID: String, private val appContext: android.content.Context) {
```
> يُعرِّف الصنف `MessageHandler` (معالِج الرسائل) ببانٍ يأخذ خاصّيتين خاصّتين: `myPeerID` من نوع نصّ (معرّف نظيري الخاص)، و`appContext` من نوع `android.content.Context` (سياق التطبيق)، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:20]

```
21:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:21]

```
22:     companion object {
```
> يفتح كائناً مرافقاً (companion object) للصنف. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:22]

```
23:         private const val TAG = "MessageHandler"
```
> يُعرِّف ثابتاً خاصّاً `TAG` بقيمة نصّية `"MessageHandler"` (وسم التسجيل). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:23]

```
24:         private const val ANNOUNCE_CLOCK_SKEW_TOLERANCE_MS = 10 * 60 * 1000L
```
> يُعرِّف ثابتاً خاصّاً `ANNOUNCE_CLOCK_SKEW_TOLERANCE_MS` (تسامح انحراف الساعة للإعلان بالملّي‑ثانية) بقيمة حاصل ضرب 10 × 60 × 1000 من نوع طويل (Long). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:24]

```
25:     }
```
> إغلاق نطاق (نهاية الكائن المرافق). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:25]

```
26:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:26]

```
27:     // Delegate for callbacks
```
> تعليق: «مُفوَّض (delegate) لردود النداء». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:27]

```
28:     var delegate: MessageHandlerDelegate? = null
```
> يُعرِّف خاصّية متغيّرة `delegate` (المُفوَّض) من نوع `MessageHandlerDelegate?` قابل للإبطال بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:28]

```
29:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:29]

```
30:     // Reference to PacketProcessor for recursive packet handling
```
> تعليق: «مرجع إلى PacketProcessor لمعالجة الحِزَم بالاستدعاء الذاتي (recursive)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:30]

```
31:     var packetProcessor: PacketProcessor? = null
```
> يُعرِّف خاصّية متغيّرة `packetProcessor` (معالِج الحِزَم) من نوع `PacketProcessor?` قابل للإبطال بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:31]

```
32:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:32]

```
33:     // Coroutines
```
> تعليق: «الكوروتينات». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:33]

```
34:     private val handlerScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يُعرِّف خاصّية خاصّة ثابتة `handlerScope` (نطاق المعالِج) بقيمة `CoroutineScope` مُركَّبة من `Dispatchers.IO` (موزّع الإدخال/الإخراج) جُمِع إليه `SupervisorJob()` (مهمّة مشرفة). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:34]

```
35:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:35]

```
36:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:36]

```
37:      * Handle Noise encrypted transport message - SIMPLIFIED iOS-compatible version
```
> تعليق: «تعامُل مع رسالة نقل مُعمّاة بـ Noise — نسخة مبسّطة متوافقة مع iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:37]

```
38:      * Uses NoisePayloadType system exactly like iOS SimplifiedBluetoothService
```
> تعليق: «يستعمل نظام NoisePayloadType تماماً مثل SimplifiedBluetoothService في iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:38]

```
39:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:39]

```
40:     suspend fun handleNoiseEncrypted(routed: RoutedPacket) {
```
> يُعرِّف دالّة مُعلّقة (suspend) باسم `handleNoiseEncrypted` (التعامل مع المُعمّى بـ Noise) تأخذ وسيطاً `routed` من نوع `RoutedPacket`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:40]

```
41:         val packet = routed.packet
```
> يُعرِّف ثابتاً محلّياً `packet` (الحزمة) بقيمة الخاصّية `packet` من الكائن `routed`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:41]

```
42:         val peerID = routed.peerID ?: "unknown"
```
> يُعرِّف ثابتاً محلّياً `peerID` (معرّف النظير) بقيمة `routed.peerID`، وإن كانت `null` فبالقيمة البديلة النصّية `"unknown"`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:42]

```
43:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:43]

```
44:         Log.d(TAG, "Processing Noise encrypted message from $peerID (${packet.payload.size} bytes)")
```
> يستدعي `Log.d` بالوسم `TAG` لتسجيل رسالة تصحيح نصّها «معالجة رسالة Noise مُعمّاة من $peerID» مع حجم حمولة الحزمة `packet.payload.size` بالبايتات. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:44]

```
45:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:45]

```
46:         // Skip our own messages
```
> تعليق: «تخطّي رسائلنا الخاصّة». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:46]

```
47:         if (peerID == myPeerID) return
```
> إن كان `peerID` يساوي `myPeerID` يخرج من الدالّة (return). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:47]

```
48:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:48]

```
49:         // Check if this message is for us
```
> تعليق: «التحقّق ممّا إذا كانت هذه الرسالة موجَّهة إلينا». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:49]

```
50:         val recipientID = packet.recipientID?.toHexString()
```
> يُعرِّف ثابتاً محلّياً `recipientID` (معرّف المستلِم) بنتيجة استدعاء `toHexString()` على `packet.recipientID` إن لم يكن `null` (استدعاء آمن). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:50]

```
51:         if (recipientID != myPeerID) {
```
> يفتح شرطاً: إن كان `recipientID` لا يساوي `myPeerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:51]

```
52:             Log.d(TAG, "🔐 Encrypted message not for me (for $recipientID, I am $myPeerID)")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح نصّها «الرسالة المُعمّاة ليست لي (لِـ $recipientID، وأنا $myPeerID)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:52]

```
53:             return
```
> يخرج من الدالّة (return). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:53]

```
54:         }
```
> إغلاق نطاق (نهاية الشرط). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:54]

```
55:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:55]

```
56:         try {
```
> يفتح كتلة `try` (محاولة). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:56]

```
57:             // Decrypt the message using the Noise service
```
> تعليق: «فكّ تعمية الرسالة باستعمال خدمة Noise». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:57]

```
58:             val decryptedData = delegate?.decryptFromPeer(packet.payload, peerID)
```
> يُعرِّف ثابتاً محلّياً `decryptedData` (البيانات المفكوكة) بنتيجة استدعاء آمن `delegate?.decryptFromPeer` بالوسيطين `packet.payload` و`peerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:58]

```
59:             if (decryptedData == null) {
```
> يفتح شرطاً: إن كان `decryptedData` يساوي `null`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:59]

```
60:                 Log.w(TAG, "Failed to decrypt Noise message from $peerID - may need handshake")
```
> يستدعي `Log.w` لتسجيل تحذير نصّه «فشل فكّ تعمية رسالة Noise من $peerID — قد يلزم تصافُح (handshake)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:60]

```
61:                 return
```
> يخرج من الدالّة (return). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:61]

```
62:             }
```
> إغلاق نطاق (نهاية الشرط). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:62]

```
63:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:63]

```
64:             if (decryptedData.isEmpty()) {
```
> يفتح شرطاً: إن كانت `decryptedData` فارغة (`isEmpty()`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:64]

```
65:                 Log.w(TAG, "Decrypted data is empty from $peerID")
```
> يستدعي `Log.w` لتسجيل تحذير نصّه «البيانات المفكوكة فارغة من $peerID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:65]

```
66:                 return
```
> يخرج من الدالّة (return). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:66]

```
67:             }
```
> إغلاق نطاق (نهاية الشرط). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:67]

```
68:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:68]

```
69:             // NEW: Use NoisePayload system exactly like iOS
```
> تعليق: «جديد: استعمال نظام NoisePayload تماماً مثل iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:69]

```
70:             val noisePayload = com.bitchat.android.model.NoisePayload.decode(decryptedData)
```
> يُعرِّف ثابتاً محلّياً `noisePayload` (حمولة Noise) بنتيجة استدعاء `NoisePayload.decode` على `decryptedData`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:70]

```
71:             if (noisePayload == null) {
```
> يفتح شرطاً: إن كان `noisePayload` يساوي `null`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:71]

```
72:                 Log.w(TAG, "Failed to parse NoisePayload from $peerID")
```
> يستدعي `Log.w` لتسجيل تحذير نصّه «فشل تحليل NoisePayload من $peerID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:72]

```
73:                 return
```
> يخرج من الدالّة (return). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:73]

```
74:             }
```
> إغلاق نطاق (نهاية الشرط). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:74]

```
75:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:75]

```
76:             Log.d(TAG, "🔓 Decrypted NoisePayload type ${noisePayload.type} from $peerID")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح نصّها «فُكّت تعمية NoisePayload من النوع ${noisePayload.type} من $peerID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:76]

```
77:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:77]

```
78:             when (noisePayload.type) {
```
> يفتح تعبير `when` (مطابقة) على قيمة `noisePayload.type` (نوع الحمولة). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:78]

```
79:                 com.bitchat.android.model.NoisePayloadType.PRIVATE_MESSAGE -> {
```
> فرع `when`: عند مطابقة `NoisePayloadType.PRIVATE_MESSAGE` (رسالة خاصّة) يفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:79]

```
80:                     // Decode TLV private message exactly like iOS
```
> تعليق: «فكّ ترميز رسالة خاصّة بصيغة TLV تماماً مثل iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:80]

```
81:                     val privateMessage = com.bitchat.android.model.PrivateMessagePacket.decode(noisePayload.data)
```
> يُعرِّف ثابتاً محلّياً `privateMessage` (الرسالة الخاصّة) بنتيجة استدعاء `PrivateMessagePacket.decode` على `noisePayload.data`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:81]

```
82:                     if (privateMessage != null) {
```
> يفتح شرطاً: إن كان `privateMessage` لا يساوي `null`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:82]

```
83:                         Log.d(TAG, "🔓 Decrypted TLV PM from $peerID: ${privateMessage.content.take(30)}...")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح نصّها «فُكّت رسالة خاصّة TLV من $peerID:» مع أوّل 30 محرفاً من `privateMessage.content` عبر `take(30)`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:83]

```
84: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:84]

```
85:                         // Handle favorite/unfavorite notifications embedded as PMs
```
> تعليق: «التعامُل مع إشعارات التفضيل/إلغاء التفضيل المُضمَّنة كرسائل خاصّة». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:85]

```
86:                         val pmContent = privateMessage.content
```
> يُعرِّف ثابتاً محلّياً `pmContent` (محتوى الرسالة الخاصّة) بقيمة `privateMessage.content`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:86]

```
87:                         if (pmContent.startsWith("[FAVORITED]") || pmContent.startsWith("[UNFAVORITED]")) {
```
> يفتح شرطاً: إن كان `pmContent` يبدأ بـ `"[FAVORITED]"` أو يبدأ بـ `"[UNFAVORITED]"`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:87]

```
88:                             handleFavoriteNotificationFromMesh(pmContent, peerID)
```
> يستدعي الدالّة `handleFavoriteNotificationFromMesh` (التعامل مع إشعار التفضيل من الشبكة المتشابكة) بالوسيطين `pmContent` و`peerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:88]

```
89:                             // Acknowledge delivery for UX parity
```
> تعليق: «إقرار التسليم لمماثلة تجربة المستخدم (UX parity)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:89]

```
90:                             sendDeliveryAck(privateMessage.messageID, peerID)
```
> يستدعي الدالّة `sendDeliveryAck` (إرسال إقرار التسليم) بالوسيطين `privateMessage.messageID` و`peerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:90]

```
91:                             return
```
> يخرج من الدالّة (return). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:91]

```
92:                         }
```
> إغلاق نطاق (نهاية الشرط). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:92]

```
93:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:93]

```
94:                         // Create BitchatMessage - preserve source packet timestamp
```
> تعليق: «إنشاء BitchatMessage — مع الحفاظ على الطابع الزمني لحزمة المصدر». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:94]

```
95:                         val message = BitchatMessage(
```
> يُعرِّف ثابتاً محلّياً `message` (الرسالة) بإنشاء كائن `BitchatMessage`، ويفتح قائمة وسائط البانِي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:95]

```
96:                             id = privateMessage.messageID,
```
> يضبط الوسيط `id` (المعرّف) بقيمة `privateMessage.messageID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:96]

```
97:                             sender = delegate?.getPeerNickname(peerID) ?: "Unknown",
```
> يضبط الوسيط `sender` (المُرسِل) بنتيجة `delegate?.getPeerNickname(peerID)`، وإن كانت `null` فبالقيمة البديلة `"Unknown"`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:97]

```
98:                             content = privateMessage.content,
```
> يضبط الوسيط `content` (المحتوى) بقيمة `privateMessage.content`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:98]

```
99:                             timestamp = java.util.Date(packet.timestamp.toLong()),
```
> يضبط الوسيط `timestamp` (الطابع الزمني) بكائن `java.util.Date` مُنشأ من `packet.timestamp.toLong()`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:99]

```
100:                             isRelay = false,
```
> يضبط الوسيط `isRelay` (هل هو تمرير/ترحيل) بقيمة `false`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:100]

```
101:                             originalSender = null,
```
> يضبط الوسيط `originalSender` (المُرسِل الأصلي) بقيمة `null`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:101]

```
102:                             isPrivate = true,
```
> يضبط الوسيط `isPrivate` (هل هي خاصّة) بقيمة `true`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:102]

```
103:                             recipientNickname = delegate?.getMyNickname(),
```
> يضبط الوسيط `recipientNickname` (كنية المستلِم) بنتيجة الاستدعاء الآمن `delegate?.getMyNickname()`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:103]

```
104:                             senderPeerID = peerID,
```
> يضبط الوسيط `senderPeerID` (معرّف نظير المُرسِل) بقيمة `peerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:104]

```
105:                             mentions = null // TODO: Parse mentions if needed
```
> يضبط الوسيط `mentions` (الإشارات/المناداة) بقيمة `null`، مع تعليق: «مهمّة لاحقة: حلّل الإشارات إن لزم». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:105]

```
106:                         )
```
> إغلاق نطاق (نهاية وسائط بانِي `BitchatMessage`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:106]

```
107:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:107]

```
108:                         // Notify delegate
```
> تعليق: «إخطار المُفوَّض». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:108]

```
109:                         delegate?.onMessageReceived(message)
```
> يستدعي استدعاءً آمناً `delegate?.onMessageReceived` بالوسيط `message`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:109]

```
110:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:110]

```
111:                         // Send delivery ACK exactly like iOS
```
> تعليق: «إرسال إقرار التسليم تماماً مثل iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:111]

```
112:                         sendDeliveryAck(privateMessage.messageID, peerID)
```
> يستدعي الدالّة `sendDeliveryAck` بالوسيطين `privateMessage.messageID` و`peerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:112]

```
113:                     }
```
> إغلاق نطاق (نهاية شرط `privateMessage != null`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:113]

```
114:                 }
```
> إغلاق نطاق (نهاية فرع `PRIVATE_MESSAGE`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:114]

```
115:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:115]

```
116:                 com.bitchat.android.model.NoisePayloadType.FILE_TRANSFER -> {
```
> فرع `when`: عند مطابقة `NoisePayloadType.FILE_TRANSFER` (نقل ملفّ) يفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:116]

```
117:                     // Handle encrypted file transfer; generate unique message ID
```
> تعليق: «التعامُل مع نقل ملفّ مُعمّى؛ توليد معرّف رسالة فريد». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:117]

```
118:                     val file = com.bitchat.android.model.BitchatFilePacket.decode(noisePayload.data)
```
> يُعرِّف ثابتاً محلّياً `file` (الملفّ) بنتيجة استدعاء `BitchatFilePacket.decode` على `noisePayload.data`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:118]

```
119:                     if (file != null) {
```
> يفتح شرطاً: إن كان `file` لا يساوي `null`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:119]

```
120:                         Log.d(TAG, "🔓 Decrypted encrypted file from $peerID: name='${file.fileName}', size=${file.fileSize}, mime='${file.mimeType}'")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح تذكر فكّ تعمية ملفّ من $peerID مع اسمه `file.fileName` وحجمه `file.fileSize` ونوعه `file.mimeType`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:120]

```
121:                         val uniqueMsgId = java.util.UUID.randomUUID().toString().uppercase()
```
> يُعرِّف ثابتاً محلّياً `uniqueMsgId` (معرّف رسالة فريد) بمعرّف UUID عشوائي مُحوَّل إلى نصّ ثمّ إلى أحرف كبيرة عبر `uppercase()`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:121]

```
122:                         val savedPath = com.bitchat.android.features.file.FileUtils.saveIncomingFile(appContext, file)
```
> يُعرِّف ثابتاً محلّياً `savedPath` (المسار المحفوظ) بنتيجة استدعاء `FileUtils.saveIncomingFile` بالوسيطين `appContext` و`file`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:122]

```
123:                         val message = BitchatMessage(
```
> يُعرِّف ثابتاً محلّياً `message` بإنشاء كائن `BitchatMessage`، ويفتح قائمة وسائط البانِي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:123]

```
124:                             id = uniqueMsgId,
```
> يضبط الوسيط `id` بقيمة `uniqueMsgId`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:124]

```
125:                             sender = delegate?.getPeerNickname(peerID) ?: "Unknown",
```
> يضبط الوسيط `sender` بنتيجة `delegate?.getPeerNickname(peerID)`، وإن كانت `null` فبالقيمة البديلة `"Unknown"`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:125]

```
126:                             content = savedPath,
```
> يضبط الوسيط `content` بقيمة `savedPath`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:126]

```
127:                             type = com.bitchat.android.features.file.FileUtils.messageTypeForMime(file.mimeType),
```
> يضبط الوسيط `type` (النوع) بنتيجة استدعاء `FileUtils.messageTypeForMime` على `file.mimeType`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:127]

```
128:                             timestamp = java.util.Date(packet.timestamp.toLong()),
```
> يضبط الوسيط `timestamp` بكائن `java.util.Date` مُنشأ من `packet.timestamp.toLong()`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:128]

```
129:                             isRelay = false,
```
> يضبط الوسيط `isRelay` بقيمة `false`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:129]

```
130:                             isPrivate = true,
```
> يضبط الوسيط `isPrivate` بقيمة `true`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:130]

```
131:                             recipientNickname = delegate?.getMyNickname(),
```
> يضبط الوسيط `recipientNickname` بنتيجة الاستدعاء الآمن `delegate?.getMyNickname()`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:131]

```
132:                             senderPeerID = peerID
```
> يضبط الوسيط `senderPeerID` بقيمة `peerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:132]

```
133:                         )
```
> إغلاق نطاق (نهاية وسائط بانِي `BitchatMessage`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:133]

```
134: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:134]

```
135:                         Log.d(TAG, "📄 Saved encrypted incoming file to $savedPath (msgId=$uniqueMsgId)")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح نصّها «حُفِظ الملفّ الوارد المُعمّى في $savedPath (msgId=$uniqueMsgId)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:135]

```
136:                         delegate?.onMessageReceived(message)
```
> يستدعي استدعاءً آمناً `delegate?.onMessageReceived` بالوسيط `message`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:136]

```
137: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:137]

```
138:                         // Send delivery ACK with generated message ID
```
> تعليق: «إرسال إقرار التسليم بمعرّف الرسالة المُولَّد». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:138]

```
139:                         sendDeliveryAck(uniqueMsgId, peerID)
```
> يستدعي الدالّة `sendDeliveryAck` بالوسيطين `uniqueMsgId` و`peerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:139]

```
140:                     } else {
```
> يفتح فرع `else` (وإلّا) لشرط `file != null`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:140]

```
141:                         Log.w(TAG, "⚠️ Failed to decode encrypted file transfer from $peerID")
```
> يستدعي `Log.w` لتسجيل تحذير نصّه «فشل فكّ ترميز نقل الملفّ المُعمّى من $peerID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:141]

```
142:                     }
```
> إغلاق نطاق (نهاية `else`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:142]

```
143:                 }
```
> إغلاق نطاق (نهاية فرع `FILE_TRANSFER`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:143]

```
144:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:144]

```
145:                 com.bitchat.android.model.NoisePayloadType.DELIVERED -> {
```
> فرع `when`: عند مطابقة `NoisePayloadType.DELIVERED` (تمّ التسليم) يفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:145]

```
146:                     // Handle delivery ACK exactly like iOS
```
> تعليق: «التعامُل مع إقرار التسليم تماماً مثل iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:146]

```
147:                     val messageID = String(noisePayload.data, Charsets.UTF_8)
```
> يُعرِّف ثابتاً محلّياً `messageID` (معرّف الرسالة) بإنشاء نصّ من `noisePayload.data` بترميز `UTF_8`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:147]

```
148:                     Log.d(TAG, "📬 Delivery ACK received from $peerID for message $messageID")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح نصّها «وصل إقرار تسليم من $peerID للرسالة $messageID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:148]

```
149:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:149]

```
150:                     // Simplified: Call delegate with messageID and peerID directly
```
> تعليق: «مبسّط: استدعِ المُفوَّض بـ messageID و peerID مباشرة». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:150]

```
151:                     delegate?.onDeliveryAckReceived(messageID, peerID)
```
> يستدعي استدعاءً آمناً `delegate?.onDeliveryAckReceived` بالوسيطين `messageID` و`peerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:151]

```
152:                 }
```
> إغلاق نطاق (نهاية فرع `DELIVERED`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:152]

```
153:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:153]

```
154:                 com.bitchat.android.model.NoisePayloadType.READ_RECEIPT -> {
```
> فرع `when`: عند مطابقة `NoisePayloadType.READ_RECEIPT` (إيصال القراءة) يفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:154]

```
155:                     // Handle read receipt exactly like iOS
```
> تعليق: «التعامُل مع إيصال القراءة تماماً مثل iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:155]

```
156:                     val messageID = String(noisePayload.data, Charsets.UTF_8)
```
> يُعرِّف ثابتاً محلّياً `messageID` بإنشاء نصّ من `noisePayload.data` بترميز `UTF_8`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:156]

```
157:                     Log.d(TAG, "👁️ Read receipt received from $peerID for message $messageID")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح نصّها «وصل إيصال قراءة من $peerID للرسالة $messageID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:157]

```
158:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:158]

```
159:                     // Simplified: Call delegate with messageID and peerID directly
```
> تعليق: «مبسّط: استدعِ المُفوَّض بـ messageID و peerID مباشرة». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:159]

```
160:                     delegate?.onReadReceiptReceived(messageID, peerID)
```
> يستدعي استدعاءً آمناً `delegate?.onReadReceiptReceived` بالوسيطين `messageID` و`peerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:160]

```
161:                 }
```
> إغلاق نطاق (نهاية فرع `READ_RECEIPT`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:161]

```
162:                 com.bitchat.android.model.NoisePayloadType.VERIFY_CHALLENGE -> {
```
> فرع `when`: عند مطابقة `NoisePayloadType.VERIFY_CHALLENGE` (تحدّي التحقّق) يفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:162]

```
163:                     Log.d(TAG, "🔐 Verify challenge received from $peerID (${noisePayload.data.size} bytes)")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح نصّها «وصل تحدّي تحقّق من $peerID» مع حجم `noisePayload.data.size` بالبايتات. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:163]

```
164:                     delegate?.onVerifyChallengeReceived(peerID, noisePayload.data, packet.timestamp.toLong())
```
> يستدعي استدعاءً آمناً `delegate?.onVerifyChallengeReceived` بالوسائط `peerID` و`noisePayload.data` و`packet.timestamp.toLong()`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:164]

```
165:                 }
```
> إغلاق نطاق (نهاية فرع `VERIFY_CHALLENGE`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:165]

```
166:                 com.bitchat.android.model.NoisePayloadType.VERIFY_RESPONSE -> {
```
> فرع `when`: عند مطابقة `NoisePayloadType.VERIFY_RESPONSE` (ردّ التحقّق) يفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:166]

```
167:                     Log.d(TAG, "🔐 Verify response received from $peerID (${noisePayload.data.size} bytes)")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح نصّها «وصل ردّ تحقّق من $peerID» مع حجم `noisePayload.data.size` بالبايتات. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:167]

```
168:                     delegate?.onVerifyResponseReceived(peerID, noisePayload.data, packet.timestamp.toLong())
```
> يستدعي استدعاءً آمناً `delegate?.onVerifyResponseReceived` بالوسائط `peerID` و`noisePayload.data` و`packet.timestamp.toLong()`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:168]

```
169:                 }
```
> إغلاق نطاق (نهاية فرع `VERIFY_RESPONSE`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:169]

```
170:             }
```
> إغلاق نطاق (نهاية تعبير `when`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:170]

```
171:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:171]

```
172:         } catch (e: Exception) {
```
> يُغلق `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:172]

```
173:             Log.e(TAG, "Error processing Noise encrypted message from $peerID: ${e.message}")
```
> يستدعي `Log.e` لتسجيل خطأ نصّه «خطأ في معالجة رسالة Noise المُعمّاة من $peerID:» مع رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:173]

```
174:         }
```
> إغلاق نطاق (نهاية كتلة `catch`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:174]

```
175:     }
```
> إغلاق نطاق (نهاية الدالّة `handleNoiseEncrypted`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:175]

```
176:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:176]

```
177:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:177]

```
178:      * Send delivery ACK for a received private message - exactly like iOS
```
> تعليق: «إرسال إقرار تسليم لرسالة خاصّة مُستلَمة — تماماً مثل iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:178]

```
179:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:179]

```
180:     private suspend fun sendDeliveryAck(messageID: String, senderPeerID: String) {
```
> يُعرِّف دالّة خاصّة مُعلّقة (private suspend) باسم `sendDeliveryAck` تأخذ وسيطين: `messageID` و`senderPeerID` كلاهما نصّ، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:180]

```
181:         try {
```
> يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:181]

```
182:             // Create ACK payload: [type byte] + [message ID] - exactly like iOS
```
> تعليق: «إنشاء حمولة الإقرار: [بايت النوع] + [معرّف الرسالة] — تماماً مثل iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:182]

```
183:             val ackPayload = com.bitchat.android.model.NoisePayload(
```
> يُعرِّف ثابتاً محلّياً `ackPayload` (حمولة الإقرار) بإنشاء كائن `NoisePayload`، ويفتح قائمة وسائط البانِي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:183]

```
184:                 type = com.bitchat.android.model.NoisePayloadType.DELIVERED,
```
> يضبط الوسيط `type` بقيمة `NoisePayloadType.DELIVERED`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:184]

```
185:                 data = messageID.toByteArray(Charsets.UTF_8)
```
> يضبط الوسيط `data` (البيانات) بتحويل `messageID` إلى مصفوفة بايتات بترميز `UTF_8`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:185]

```
186:             )
```
> إغلاق نطاق (نهاية وسائط بانِي `NoisePayload`). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:186]

```
187:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:187]

```
188:             // Encrypt the payload
```
> تعليق: «تعمية الحمولة». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:188]

```
189:             val encryptedPayload = delegate?.encryptForPeer(ackPayload.encode(), senderPeerID)
```
> يُعرِّف ثابتاً محلّياً `encryptedPayload` (الحمولة المُعمّاة) بنتيجة الاستدعاء الآمن `delegate?.encryptForPeer` بالوسيطين `ackPayload.encode()` و`senderPeerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:189]

```
190:             if (encryptedPayload == null) {
```
> يفتح شرطاً: إن كان `encryptedPayload` يساوي `null`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:190]

```
191:                 Log.w(TAG, "Failed to encrypt delivery ACK for $senderPeerID")
```
> يستدعي `Log.w` لتسجيل تحذير نصّه «فشل تعمية إقرار التسليم لِـ $senderPeerID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:191]

```
192:                 return
```
> يخرج من الدالّة (return). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:192]

```
193:             }
```
> إغلاق نطاق (نهاية الشرط). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:193]

```
194:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:194]

```
195:             // Create NOISE_ENCRYPTED packet exactly like iOS
```
> تعليق: «إنشاء حزمة NOISE_ENCRYPTED تماماً مثل iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:195]

```
196:                 val packet = BitchatPacket(
```
> يُعرِّف ثابتاً محلّياً `packet` بإنشاء كائن `BitchatPacket`، ويفتح قائمة وسائط البانِي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:196]

```
197:                     version = 1u,
```
> يضبط الوسيط `version` (الإصدار) بقيمة `1u` من نوع عدد صحيح موجب (UInt). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:197]

```
198:                     type = MessageType.NOISE_ENCRYPTED.value,
```
> يضبط الوسيط `type` بقيمة `MessageType.NOISE_ENCRYPTED.value`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:198]

```
199:                     senderID = hexStringToByteArray(myPeerID),
```
> يضبط الوسيط `senderID` (معرّف المُرسِل) بنتيجة استدعاء `hexStringToByteArray` على `myPeerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:199]

```
200:                     recipientID = hexStringToByteArray(senderPeerID),
```
> يضبط الوسيط `recipientID` (معرّف المستلِم) بنتيجة استدعاء `hexStringToByteArray` على `senderPeerID`. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:200]
