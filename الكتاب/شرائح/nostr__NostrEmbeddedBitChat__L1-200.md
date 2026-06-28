# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يعلن أن هذا الملف ينتمي إلى حُزمة (package) باسم `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:2]

```
3: import android.util.Base64
```
> يستورد (import) الصنف `Base64` من `android.util`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` من `android.util`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:4]

```
5: import com.bitchat.android.model.PrivateMessagePacket
```
> يستورد الصنف `PrivateMessagePacket` (رزمة الرسالة الخاصة) من حُزمة النماذج `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:5]

```
6: import com.bitchat.android.model.NoisePayloadType
```
> يستورد الصنف `NoisePayloadType` (نوع حمولة نويز) من حُزمة النماذج `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:6]

```
7: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف `BitchatPacket` (رزمة بِت‑تشات) من حُزمة البروتوكول `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:7]

```
8: import com.bitchat.android.protocol.MessageType
```
> يستورد الصنف `MessageType` (نوع الرسالة) من حُزمة البروتوكول `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:8]

```
9: import java.util.*
```
> يستورد كل عناصر حُزمة `java.util`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:9]

```
10: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:10]

```
11: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:11]

```
12:  * BitChat-over-Nostr Adapter
```
> تعليق: محوّل بِت‑تشات فوق نوستر (BitChat-over-Nostr Adapter). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:12]

```
13:  * Direct port from iOS implementation for 100% compatibility
```
> تعليق: نقل مباشر من تطبيق iOS لأجل توافق بنسبة ١٠٠٪. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:13]

```
14:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:14]

```
15: object NostrEmbeddedBitChat {
```
> يعرّف كائناً مفرداً (object) باسم `NostrEmbeddedBitChat` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:15]

```
16:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:16]

```
17:     private const val TAG = "NostrEmbeddedBitChat"
```
> يعرّف ثابتاً خاصاً (private const) باسم `TAG` بقيمة نصية `"NostrEmbeddedBitChat"`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:17]

```
18:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:18]

```
19:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:19]

```
20:      * Build a `bitchat1:` base64url-encoded BitChat packet carrying a private message for Nostr DMs.
```
> تعليق: ابْنِ رزمة بِت‑تشات مُرمَّزة بـ base64url بادئتها `bitchat1:` تحمل رسالة خاصة لرسائل نوستر المباشرة (DMs). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:20]

```
21:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:21]

```
22:     fun encodePMForNostr(
```
> يعرّف دالة (fun) باسم `encodePMForNostr` ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:22]

```
23:         content: String,
```
> يعلن معاملاً باسم `content` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:23]

```
24:         messageID: String,
```
> يعلن معاملاً باسم `messageID` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:24]

```
25:         recipientPeerID: String,
```
> يعلن معاملاً باسم `recipientPeerID` (معرّف نِدّ المستقبِل) من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:25]

```
26:         senderPeerID: String
```
> يعلن معاملاً باسم `senderPeerID` (معرّف نِدّ المرسِل) من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:26]

```
27:     ): String? {
```
> يُنهي قائمة المعاملات ويعلن أن نوع الإرجاع `String?` (نص قابل لأن يكون فارغاً) ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:27]

```
28:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:28]

```
29:             // TLV-encode the private message
```
> تعليق: رمِّز الرسالة الخاصة بصيغة TLV (نوع‑طول‑قيمة). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:29]

```
30:             val pm = PrivateMessagePacket(messageID = messageID, content = content)
```
> يعرّف متغيراً ثابتاً `pm` ويسند إليه كائن `PrivateMessagePacket` مُنشأً بالمعاملين `messageID = messageID` و`content = content`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:30]

```
31:             val tlv = pm.encode() ?: return null
```
> يعرّف متغيراً ثابتاً `tlv` ويسند إليه نتيجة استدعاء `pm.encode()`؛ وإن كانت فارغة (null) يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:31]

```
32:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:32]

```
33:             // Prefix with NoisePayloadType
```
> تعليق: ضع بادئة بنوع حمولة نويز (NoisePayloadType). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:33]

```
34:             val payload = ByteArray(1 + tlv.size)
```
> يعرّف متغيراً ثابتاً `payload` (الحمولة) ويسند إليه مصفوفة بايتات `ByteArray` بطول `1 + tlv.size`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:34]

```
35:             payload[0] = NoisePayloadType.PRIVATE_MESSAGE.value.toByte()
```
> يسند إلى العنصر `payload[0]` قيمة `NoisePayloadType.PRIVATE_MESSAGE.value` محوّلةً إلى بايت بـ `toByte()`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:35]

```
36:             System.arraycopy(tlv, 0, payload, 1, tlv.size)
```
> يستدعي `System.arraycopy` لنسخ `tlv` من الموضع `0` إلى `payload` بدءاً من الموضع `1` بعدد `tlv.size` عنصراً. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:36]

```
37:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:37]

```
38:             // Determine 8-byte recipient ID to embed
```
> تعليق: حدِّد معرّف المستقبِل بطول ٨ بايتات لتضمينه. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:38]

```
39:             val recipientIDHex = normalizeRecipientPeerID(recipientPeerID)
```
> يعرّف متغيراً ثابتاً `recipientIDHex` ويسند إليه نتيجة استدعاء `normalizeRecipientPeerID(recipientPeerID)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:39]

```
40:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:40]

```
41:             val packet = BitchatPacket(
```
> يعرّف متغيراً ثابتاً `packet` ويبدأ إسناد كائن `BitchatPacket` مُنشأً بفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:41]

```
42:                 version = 1u,
```
> يضبط الوسيط `version` على القيمة `1u` (عدد صحيح غير مُوقَّع). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:42]

```
43:                 type = MessageType.NOISE_ENCRYPTED.value,
```
> يضبط الوسيط `type` على القيمة `MessageType.NOISE_ENCRYPTED.value`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:43]

```
44:                 senderID = hexStringToByteArray(senderPeerID),
```
> يضبط الوسيط `senderID` على نتيجة استدعاء `hexStringToByteArray(senderPeerID)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:44]

```
45:                 recipientID = hexStringToByteArray(recipientIDHex),
```
> يضبط الوسيط `recipientID` على نتيجة استدعاء `hexStringToByteArray(recipientIDHex)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:45]

```
46:                 timestamp = System.currentTimeMillis().toULong(),
```
> يضبط الوسيط `timestamp` على `System.currentTimeMillis()` محوّلةً إلى عدد طويل غير مُوقَّع بـ `toULong()`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:46]

```
47:                 payload = payload,
```
> يضبط الوسيط `payload` على المتغير `payload`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:47]

```
48:                 signature = null,
```
> يضبط الوسيط `signature` (التوقيع) على `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:48]

```
49:                 ttl = com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS
```
> يضبط الوسيط `ttl` (مدة البقاء) على `com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:49]

```
50:             )
```
> يُغلق قائمة وُسطاء مُنشئ `BitchatPacket`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:50]

```
51:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:51]

```
52:             val data = packet.toBinaryData() ?: return null
```
> يعرّف متغيراً ثابتاً `data` ويسند إليه نتيجة `packet.toBinaryData()`؛ وإن كانت `null` يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:52]

```
53:             return "bitchat1:" + base64URLEncode(data)
```
> يُعيد ناتج وصل النص `"bitchat1:"` بنتيجة `base64URLEncode(data)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:53]

```
54:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:54]

```
55:             Log.e(TAG, "Failed to encode PM for Nostr: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ونص `"Failed to encode PM for Nostr: ${e.message}"` مُضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:55]

```
56:             return null
```
> يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:56]

```
57:         }
```
> إغلاق نطاق (كتلة `catch`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:57]

```
58:     }
```
> إغلاق نطاق (دالة `encodePMForNostr`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:58]

```
59:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:59]

```
60:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:60]

```
61:      * Build a `bitchat1:` base64url-encoded BitChat packet carrying a delivery/read ack for Nostr DMs.
```
> تعليق: ابْنِ رزمة بِت‑تشات مُرمَّزة بـ base64url بادئتها `bitchat1:` تحمل إشعار تسليم/قراءة (ack) لرسائل نوستر المباشرة. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:61]

```
62:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:62]

```
63:     fun encodeAckForNostr(
```
> يعرّف دالة باسم `encodeAckForNostr` ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:63]

```
64:         type: NoisePayloadType,
```
> يعلن معاملاً باسم `type` من نوع `NoisePayloadType`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:64]

```
65:         messageID: String,
```
> يعلن معاملاً باسم `messageID` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:65]

```
66:         recipientPeerID: String,
```
> يعلن معاملاً باسم `recipientPeerID` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:66]

```
67:         senderPeerID: String
```
> يعلن معاملاً باسم `senderPeerID` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:67]

```
68:     ): String? {
```
> يُنهي قائمة المعاملات ويعلن نوع الإرجاع `String?` ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:68]

```
69:         if (type != NoisePayloadType.DELIVERED && type != NoisePayloadType.READ_RECEIPT) {
```
> يبدأ شرطاً `if` يتحقق أن `type` لا يساوي `NoisePayloadType.DELIVERED` و`type` لا يساوي `NoisePayloadType.READ_RECEIPT`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:69]

```
70:             return null
```
> يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:70]

```
71:         }
```
> إغلاق نطاق (كتلة `if`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:71]

```
72:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:72]

```
73:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:73]

```
74:             val payload = ByteArray(1 + messageID.toByteArray(Charsets.UTF_8).size)
```
> يعرّف متغيراً ثابتاً `payload` ويسند إليه `ByteArray` بطول `1 + messageID.toByteArray(Charsets.UTF_8).size`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:74]

```
75:             payload[0] = type.value.toByte()
```
> يسند إلى العنصر `payload[0]` قيمة `type.value` محوّلةً إلى بايت بـ `toByte()`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:75]

```
76:             val messageIDBytes = messageID.toByteArray(Charsets.UTF_8)
```
> يعرّف متغيراً ثابتاً `messageIDBytes` ويسند إليه `messageID.toByteArray(Charsets.UTF_8)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:76]

```
77:             System.arraycopy(messageIDBytes, 0, payload, 1, messageIDBytes.size)
```
> يستدعي `System.arraycopy` لنسخ `messageIDBytes` من الموضع `0` إلى `payload` بدءاً من الموضع `1` بعدد `messageIDBytes.size` عنصراً. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:77]

```
78:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:78]

```
79:             val recipientIDHex = normalizeRecipientPeerID(recipientPeerID)
```
> يعرّف متغيراً ثابتاً `recipientIDHex` ويسند إليه نتيجة `normalizeRecipientPeerID(recipientPeerID)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:79]

```
80:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:80]

```
81:             val packet = BitchatPacket(
```
> يعرّف متغيراً ثابتاً `packet` ويبدأ إسناد كائن `BitchatPacket` بفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:81]

```
82:                 version = 1u,
```
> يضبط الوسيط `version` على `1u`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:82]

```
83:                 type = MessageType.NOISE_ENCRYPTED.value,
```
> يضبط الوسيط `type` على `MessageType.NOISE_ENCRYPTED.value`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:83]

```
84:                 senderID = hexStringToByteArray(senderPeerID),
```
> يضبط الوسيط `senderID` على نتيجة `hexStringToByteArray(senderPeerID)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:84]

```
85:                 recipientID = hexStringToByteArray(recipientIDHex),
```
> يضبط الوسيط `recipientID` على نتيجة `hexStringToByteArray(recipientIDHex)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:85]

```
86:                 timestamp = System.currentTimeMillis().toULong(),
```
> يضبط الوسيط `timestamp` على `System.currentTimeMillis()` محوّلةً بـ `toULong()`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:86]

```
87:                 payload = payload,
```
> يضبط الوسيط `payload` على المتغير `payload`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:87]

```
88:                 signature = null,
```
> يضبط الوسيط `signature` على `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:88]

```
89:                 ttl = com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS
```
> يضبط الوسيط `ttl` على `com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:89]

```
90:             )
```
> يُغلق قائمة وُسطاء مُنشئ `BitchatPacket`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:90]

```
91:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:91]

```
92:             val data = packet.toBinaryData() ?: return null
```
> يعرّف متغيراً ثابتاً `data` ويسند إليه `packet.toBinaryData()`؛ وإن كانت `null` يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:92]

```
93:             return "bitchat1:" + base64URLEncode(data)
```
> يُعيد وصل النص `"bitchat1:"` بنتيجة `base64URLEncode(data)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:93]

```
94:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:94]

```
95:             Log.e(TAG, "Failed to encode ACK for Nostr: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ونص `"Failed to encode ACK for Nostr: ${e.message}"` مُضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:95]

```
96:             return null
```
> يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:96]

```
97:         }
```
> إغلاق نطاق (كتلة `catch`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:97]

```
98:     }
```
> إغلاق نطاق (دالة `encodeAckForNostr`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:98]

```
99:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:99]

```
100:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:100]

```
101:      * Build a `bitchat1:` ACK (delivered/read) without an embedded recipient peer ID (geohash DMs).
```
> تعليق: ابْنِ إشعار `bitchat1:` (تسليم/قراءة) دون تضمين معرّف نِدّ المستقبِل (رسائل مباشرة بالـ geohash). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:101]

```
102:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:102]

```
103:     fun encodeAckForNostrNoRecipient(
```
> يعرّف دالة باسم `encodeAckForNostrNoRecipient` (ترميز إشعار لنوستر بلا مستقبِل) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:103]

```
104:         type: NoisePayloadType,
```
> يعلن معاملاً باسم `type` من نوع `NoisePayloadType`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:104]

```
105:         messageID: String,
```
> يعلن معاملاً باسم `messageID` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:105]

```
106:         senderPeerID: String
```
> يعلن معاملاً باسم `senderPeerID` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:106]

```
107:     ): String? {
```
> يُنهي قائمة المعاملات ويعلن نوع الإرجاع `String?` ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:107]

```
108:         if (type != NoisePayloadType.DELIVERED && type != NoisePayloadType.READ_RECEIPT) {
```
> يبدأ شرطاً `if` يتحقق أن `type` لا يساوي `NoisePayloadType.DELIVERED` و`type` لا يساوي `NoisePayloadType.READ_RECEIPT`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:108]

```
109:             return null
```
> يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:109]

```
110:         }
```
> إغلاق نطاق (كتلة `if`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:110]

```
111:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:111]

```
112:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:112]

```
113:             val payload = ByteArray(1 + messageID.toByteArray(Charsets.UTF_8).size)
```
> يعرّف متغيراً ثابتاً `payload` ويسند إليه `ByteArray` بطول `1 + messageID.toByteArray(Charsets.UTF_8).size`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:113]

```
114:             payload[0] = type.value.toByte()
```
> يسند إلى العنصر `payload[0]` قيمة `type.value` محوّلةً إلى بايت بـ `toByte()`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:114]

```
115:             val messageIDBytes = messageID.toByteArray(Charsets.UTF_8)
```
> يعرّف متغيراً ثابتاً `messageIDBytes` ويسند إليه `messageID.toByteArray(Charsets.UTF_8)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:115]

```
116:             System.arraycopy(messageIDBytes, 0, payload, 1, messageIDBytes.size)
```
> يستدعي `System.arraycopy` لنسخ `messageIDBytes` من الموضع `0` إلى `payload` بدءاً من الموضع `1` بعدد `messageIDBytes.size` عنصراً. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:116]

```
117:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:117]

```
118:             val packet = BitchatPacket(
```
> يعرّف متغيراً ثابتاً `packet` ويبدأ إسناد كائن `BitchatPacket` بفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:118]

```
119:                 version = 1u,
```
> يضبط الوسيط `version` على `1u`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:119]

```
120:                 type = MessageType.NOISE_ENCRYPTED.value,
```
> يضبط الوسيط `type` على `MessageType.NOISE_ENCRYPTED.value`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:120]

```
121:                 senderID = hexStringToByteArray(senderPeerID),
```
> يضبط الوسيط `senderID` على نتيجة `hexStringToByteArray(senderPeerID)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:121]

```
122:                 recipientID = null, // No recipient for geohash DMs
```
> يضبط الوسيط `recipientID` على `null`، مع تعليق: لا مستقبِل لرسائل الـ geohash المباشرة. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:122]

```
123:                 timestamp = System.currentTimeMillis().toULong(),
```
> يضبط الوسيط `timestamp` على `System.currentTimeMillis()` محوّلةً بـ `toULong()`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:123]

```
124:                 payload = payload,
```
> يضبط الوسيط `payload` على المتغير `payload`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:124]

```
125:                 signature = null,
```
> يضبط الوسيط `signature` على `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:125]

```
126:                 ttl = com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS
```
> يضبط الوسيط `ttl` على `com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:126]

```
127:             )
```
> يُغلق قائمة وُسطاء مُنشئ `BitchatPacket`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:127]

```
128:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:128]

```
129:             val data = packet.toBinaryData() ?: return null
```
> يعرّف متغيراً ثابتاً `data` ويسند إليه `packet.toBinaryData()`؛ وإن كانت `null` يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:129]

```
130:             return "bitchat1:" + base64URLEncode(data)
```
> يُعيد وصل النص `"bitchat1:"` بنتيجة `base64URLEncode(data)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:130]

```
131:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:131]

```
132:             Log.e(TAG, "Failed to encode ACK for Nostr (no recipient): ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ونص `"Failed to encode ACK for Nostr (no recipient): ${e.message}"` مُضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:132]

```
133:             return null
```
> يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:133]

```
134:         }
```
> إغلاق نطاق (كتلة `catch`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:134]

```
135:     }
```
> إغلاق نطاق (دالة `encodeAckForNostrNoRecipient`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:135]

```
136:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:136]

```
137:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:137]

```
138:      * Build a `bitchat1:` payload without an embedded recipient peer ID (used for geohash DMs).
```
> تعليق: ابْنِ حمولة `bitchat1:` دون تضمين معرّف نِدّ المستقبِل (تُستخدَم لرسائل الـ geohash المباشرة). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:138]

```
139:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:139]

```
140:     fun encodePMForNostrNoRecipient(
```
> يعرّف دالة باسم `encodePMForNostrNoRecipient` (ترميز رسالة خاصة لنوستر بلا مستقبِل) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:140]

```
141:         content: String,
```
> يعلن معاملاً باسم `content` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:141]

```
142:         messageID: String,
```
> يعلن معاملاً باسم `messageID` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:142]

```
143:         senderPeerID: String
```
> يعلن معاملاً باسم `senderPeerID` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:143]

```
144:     ): String? {
```
> يُنهي قائمة المعاملات ويعلن نوع الإرجاع `String?` ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:144]

```
145:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:145]

```
146:             val pm = PrivateMessagePacket(messageID = messageID, content = content)
```
> يعرّف متغيراً ثابتاً `pm` ويسند إليه كائن `PrivateMessagePacket` بالمعاملين `messageID = messageID` و`content = content`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:146]

```
147:             val tlv = pm.encode() ?: return null
```
> يعرّف متغيراً ثابتاً `tlv` ويسند إليه `pm.encode()`؛ وإن كانت `null` يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:147]

```
148:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:148]

```
149:             val payload = ByteArray(1 + tlv.size)
```
> يعرّف متغيراً ثابتاً `payload` ويسند إليه `ByteArray` بطول `1 + tlv.size`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:149]

```
150:             payload[0] = NoisePayloadType.PRIVATE_MESSAGE.value.toByte()
```
> يسند إلى العنصر `payload[0]` قيمة `NoisePayloadType.PRIVATE_MESSAGE.value` محوّلةً إلى بايت بـ `toByte()`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:150]

```
151:             System.arraycopy(tlv, 0, payload, 1, tlv.size)
```
> يستدعي `System.arraycopy` لنسخ `tlv` من الموضع `0` إلى `payload` بدءاً من الموضع `1` بعدد `tlv.size` عنصراً. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:151]

```
152:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:152]

```
153:             val packet = BitchatPacket(
```
> يعرّف متغيراً ثابتاً `packet` ويبدأ إسناد كائن `BitchatPacket` بفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:153]

```
154:                 version = 1u,
```
> يضبط الوسيط `version` على `1u`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:154]

```
155:                 type = MessageType.NOISE_ENCRYPTED.value,
```
> يضبط الوسيط `type` على `MessageType.NOISE_ENCRYPTED.value`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:155]

```
156:                 senderID = hexStringToByteArray(senderPeerID),
```
> يضبط الوسيط `senderID` على نتيجة `hexStringToByteArray(senderPeerID)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:156]

```
157:                 recipientID = null, // No recipient for geohash DMs
```
> يضبط الوسيط `recipientID` على `null`، مع تعليق: لا مستقبِل لرسائل الـ geohash المباشرة. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:157]

```
158:                 timestamp = System.currentTimeMillis().toULong(),
```
> يضبط الوسيط `timestamp` على `System.currentTimeMillis()` محوّلةً بـ `toULong()`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:158]

```
159:                 payload = payload,
```
> يضبط الوسيط `payload` على المتغير `payload`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:159]

```
160:                 signature = null,
```
> يضبط الوسيط `signature` على `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:160]

```
161:                 ttl = com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS
```
> يضبط الوسيط `ttl` على `com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:161]

```
162:             )
```
> يُغلق قائمة وُسطاء مُنشئ `BitchatPacket`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:162]

```
163:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:163]

```
164:             val data = packet.toBinaryData() ?: return null
```
> يعرّف متغيراً ثابتاً `data` ويسند إليه `packet.toBinaryData()`؛ وإن كانت `null` يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:164]

```
165:             return "bitchat1:" + base64URLEncode(data)
```
> يُعيد وصل النص `"bitchat1:"` بنتيجة `base64URLEncode(data)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:165]

```
166:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:166]

```
167:             Log.e(TAG, "Failed to encode PM for Nostr (no recipient): ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ونص `"Failed to encode PM for Nostr (no recipient): ${e.message}"` مُضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:167]

```
168:             return null
```
> يُعيد `null`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:168]

```
169:         }
```
> إغلاق نطاق (كتلة `catch`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:169]

```
170:     }
```
> إغلاق نطاق (دالة `encodePMForNostrNoRecipient`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:170]

```
171:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:171]

```
172:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:172]

```
173:      * Normalize recipient peer ID (matches iOS implementation)
```
> تعليق: تطبيع معرّف نِدّ المستقبِل (مطابق لتطبيق iOS). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:173]

```
174:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:174]

```
175:     private fun normalizeRecipientPeerID(recipientPeerID: String): String {
```
> يعرّف دالة خاصة (private fun) باسم `normalizeRecipientPeerID` بمعامل `recipientPeerID` من نوع `String` ونوع إرجاع `String`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:175]

```
176:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:176]

```
177:             val maybeData = hexStringToByteArray(recipientPeerID)
```
> يعرّف متغيراً ثابتاً `maybeData` ويسند إليه نتيجة `hexStringToByteArray(recipientPeerID)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:177]

```
178:             return when (maybeData.size) {
```
> يبدأ تعبير `return when` يفرّع على قيمة `maybeData.size`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:178]

```
179:                 32 -> {
```
> يبدأ فرع `when` عند تساوي الحجم مع `32` ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:179]

```
180:                     // Treat as Noise static public key; derive peerID from fingerprint
```
> تعليق: عامِله كمفتاح نويز العام الثابت؛ اشتق معرّف النِدّ من البصمة. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:180]

```
181:                     // For now, return first 8 bytes as hex (simplified)
```
> تعليق: حالياً، أعِد أول ٨ بايتات كنص ست‑عشري (مبسّط). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:181]

```
182:                     maybeData.take(8).joinToString("") { "%02x".format(it) }
```
> قيمة هذا الفرع: يأخذ أول ٨ عناصر من `maybeData` بـ `take(8)` ثم يصلها بـ `joinToString("")` حيث يُنسَّق كل عنصر `it` ست‑عشرياً بـ `"%02x".format(it)`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:182]

```
183:                 }
```
> إغلاق نطاق (كتلة فرع `32`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:183]

```
184:                 8 -> {
```
> يبدأ فرع `when` عند تساوي الحجم مع `8` ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:184]

```
185:                     // Already an 8-byte peer ID
```
> تعليق: هو أصلاً معرّف نِدّ بطول ٨ بايتات. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:185]

```
186:                     recipientPeerID
```
> قيمة هذا الفرع: المعامل `recipientPeerID` كما هو. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:186]

```
187:                 }
```
> إغلاق نطاق (كتلة فرع `8`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:187]

```
188:                 else -> {
```
> يبدأ فرع `else` (الحالة الافتراضية) في `when` ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:188]

```
189:                     // Fallback: return as-is (expecting 16 hex chars)
```
> تعليق: احتياطي: أعِده كما هو (مع توقّع ١٦ محرفاً ست‑عشرياً). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:189]

```
190:                     recipientPeerID
```
> قيمة هذا الفرع: المعامل `recipientPeerID` كما هو. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:190]

```
191:                 }
```
> إغلاق نطاق (كتلة فرع `else`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:191]

```
192:             }
```
> إغلاق نطاق (تعبير `when`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:192]

```
193:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:193]

```
194:             // Fallback: return as-is
```
> تعليق: احتياطي: أعِده كما هو. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:194]

```
195:             return recipientPeerID
```
> يُعيد المعامل `recipientPeerID` كما هو. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:195]

```
196:         }
```
> إغلاق نطاق (كتلة `catch`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:196]

```
197:     }
```
> إغلاق نطاق (دالة `normalizeRecipientPeerID`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:197]

```
198:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:198]

```
199:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:199]

```
200:      * Base64url encode without padding (matches iOS implementation)
```
> تعليق: ترميز Base64url دون حشو (مطابق لتطبيق iOS). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:200]
