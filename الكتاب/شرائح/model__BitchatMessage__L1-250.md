# شريحة — app/src/main/java/com/bitchat/android/model/BitchatMessage.kt (الأسطر 1–250)

```
1: package com.bitchat.android.model
```
> تعريف حزمة (package) باسم `com.bitchat.android.model` التي ينتمي إليها هذا الملف. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:2]

```
3: import android.os.Parcelable
```
> استيراد (import) الواجهة `Parcelable` من حزمة أندرويد `android.os`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:3]

```
4: import com.google.gson.GsonBuilder
```
> استيراد الصنف `GsonBuilder` من مكتبة `com.google.gson`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:4]

```
5: import kotlinx.parcelize.Parcelize
```
> استيراد التعليق التوضيحي (annotation) `Parcelize` من `kotlinx.parcelize`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:5]

```
6: import java.nio.ByteBuffer
```
> استيراد الصنف `ByteBuffer` من حزمة `java.nio`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:6]

```
7: import java.nio.ByteOrder
```
> استيراد الصنف `ByteOrder` من حزمة `java.nio`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:7]

```
8: import java.util.*
```
> استيراد كل المحتويات من حزمة `java.util` باستخدام علامة النجمة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:9]

```
10: @Parcelize
```
> وضع التعليق التوضيحي `@Parcelize` فوق التعريف الذي يليه ليجعله قابلاً للحزم (Parcelable). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:10]

```
11: enum class BitchatMessageType : Parcelable {
```
> تعريف صنف تعدادي (نوع الرسالة - BitchatMessageType) يطبّق الواجهة `Parcelable`، وفتح نطاقه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:11]

```
12:     Message,
```
> تعريف القيمة التعدادية `Message`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:12]

```
13:     Audio,
```
> تعريف القيمة التعدادية `Audio`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:13]

```
14:     Image,
```
> تعريف القيمة التعدادية `Image`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:14]

```
15:     File
```
> تعريف القيمة التعدادية `File`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:15]

```
16: }
```
> إغلاق نطاق الصنف التعدادي `BitchatMessageType`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:17]

```
18: /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:18]

```
19:  * Delivery status for messages - exact same as iOS version
```
> تعليق: «حالة التسليم للرسائل - مطابقة تماماً لنسخة iOS». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:19]

```
20:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:20]

```
21: sealed class DeliveryStatus : Parcelable {
```
> تعريف صنف مُغلق (حالة التسليم - DeliveryStatus) يطبّق الواجهة `Parcelable`، وفتح نطاقه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:21]

```
22:     @Parcelize
```
> وضع التعليق التوضيحي `@Parcelize` فوق التعريف الذي يليه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:22]

```
23:     object Sending : DeliveryStatus()
```
> تعريف كائن مفرد (Sending) يرث من الصنف `DeliveryStatus`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:24]

```
25:     @Parcelize
```
> وضع التعليق التوضيحي `@Parcelize` فوق التعريف الذي يليه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:25]

```
26:     object Sent : DeliveryStatus()
```
> تعريف كائن مفرد (Sent) يرث من الصنف `DeliveryStatus`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:27]

```
28:     @Parcelize
```
> وضع التعليق التوضيحي `@Parcelize` فوق التعريف الذي يليه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:28]

```
29:     data class Delivered(val to: String, val at: Date) : DeliveryStatus()
```
> تعريف صنف بيانات (Delivered) يرث من `DeliveryStatus` وله خاصيّتان: `to` من نوع نص (String) و`at` من نوع تاريخ (Date). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:29]

```
30: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:30]

```
31:     @Parcelize
```
> وضع التعليق التوضيحي `@Parcelize` فوق التعريف الذي يليه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:31]

```
32:     data class Read(val by: String, val at: Date) : DeliveryStatus()
```
> تعريف صنف بيانات (Read) يرث من `DeliveryStatus` وله خاصيّتان: `by` من نوع نص (String) و`at` من نوع تاريخ (Date). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:33]

```
34:     @Parcelize
```
> وضع التعليق التوضيحي `@Parcelize` فوق التعريف الذي يليه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:34]

```
35:     data class Failed(val reason: String) : DeliveryStatus()
```
> تعريف صنف بيانات (Failed) يرث من `DeliveryStatus` وله خاصيّة واحدة: `reason` من نوع نص (String). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:36]

```
37:     @Parcelize
```
> وضع التعليق التوضيحي `@Parcelize` فوق التعريف الذي يليه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:37]

```
38:     data class PartiallyDelivered(val reached: Int, val total: Int) : DeliveryStatus()
```
> تعريف صنف بيانات (مُسلَّمة جزئياً - PartiallyDelivered) يرث من `DeliveryStatus` وله خاصيّتان: `reached` من نوع عدد صحيح (Int) و`total` من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:38]

```
39: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:39]

```
40:     fun getDisplayText(): String {
```
> تعريف دالة (نص العرض - getDisplayText) لا تأخذ معاملات وتعيد نصاً (String)، وفتح نطاقها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:40]

```
41:         return when (this) {
```
> إعادة نتيجة تعبير `when` يفرّع على الكائن الحالي `this`، وفتح نطاقه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:41]

```
42:             is Sending -> "Sending..."
```
> إذا كان الكائن من نوع `Sending` يُعاد النص الحرفي `"Sending..."`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:42]

```
43:             is Sent -> "Sent"
```
> إذا كان الكائن من نوع `Sent` يُعاد النص الحرفي `"Sent"`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:43]

```
44:             is Delivered -> "Delivered to ${this.to}"
```
> إذا كان الكائن من نوع `Delivered` يُعاد النص `"Delivered to "` مع إدراج قيمة الخاصيّة `to`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:44]

```
45:             is Read -> "Read by ${this.by}"
```
> إذا كان الكائن من نوع `Read` يُعاد النص `"Read by "` مع إدراج قيمة الخاصيّة `by`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:45]

```
46:             is Failed -> "Failed: ${this.reason}"
```
> إذا كان الكائن من نوع `Failed` يُعاد النص `"Failed: "` مع إدراج قيمة الخاصيّة `reason`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:46]

```
47:             is PartiallyDelivered -> "Delivered to ${this.reached}/${this.total}"
```
> إذا كان الكائن من نوع `PartiallyDelivered` يُعاد النص `"Delivered to "` مع إدراج قيمة `reached` ثم شَرطة مائلة ثم قيمة `total`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:47]

```
48:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:48]

```
49:     }
```
> إغلاق نطاق الدالة `getDisplayText`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:49]

```
50: }
```
> إغلاق نطاق الصنف `DeliveryStatus`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:50]

```
51: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:51]

```
52: /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:52]

```
53:  * BitchatMessage - 100% compatible with iOS version
```
> تعليق: «BitchatMessage - متوافقة 100% مع نسخة iOS». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:53]

```
54:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:54]

```
55: @Parcelize
```
> وضع التعليق التوضيحي `@Parcelize` فوق التعريف الذي يليه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:55]

```
56: data class BitchatMessage(
```
> تعريف صنف بيانات (رسالة بِت‑شات - BitchatMessage) وفتح قائمة معاملات بانيه الأساسي. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:56]

```
57:     val id: String = UUID.randomUUID().toString().uppercase(),
```
> تعريف خاصيّة `id` من نوع نص (String) قيمتها الافتراضية معرّف عشوائي UUID محوّل إلى نص بأحرف كبيرة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:57]

```
58:     val sender: String,
```
> تعريف خاصيّة `sender` (المرسِل) من نوع نص (String) بلا قيمة افتراضية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:58]

```
59:     val content: String,
```
> تعريف خاصيّة `content` (المحتوى) من نوع نص (String) بلا قيمة افتراضية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:59]

```
60:     val type: BitchatMessageType = BitchatMessageType.Message,
```
> تعريف خاصيّة `type` (النوع) من نوع `BitchatMessageType` قيمتها الافتراضية `BitchatMessageType.Message`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:60]

```
61:     val timestamp: Date,
```
> تعريف خاصيّة `timestamp` (الطابع الزمني) من نوع تاريخ (Date) بلا قيمة افتراضية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:61]

```
62:     val isRelay: Boolean = false,
```
> تعريف خاصيّة `isRelay` (هل مُمرَّرة) من نوع منطقي (Boolean) قيمتها الافتراضية `false`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:62]

```
63:     val originalSender: String? = null,
```
> تعريف خاصيّة `originalSender` (المرسِل الأصلي) من نوع نص قابل للعدم (String?) قيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:63]

```
64:     val isPrivate: Boolean = false,
```
> تعريف خاصيّة `isPrivate` (هل خاصة) من نوع منطقي (Boolean) قيمتها الافتراضية `false`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:64]

```
65:     val recipientNickname: String? = null,
```
> تعريف خاصيّة `recipientNickname` (لقب المستلِم) من نوع نص قابل للعدم (String?) قيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:65]

```
66:     val senderPeerID: String? = null,
```
> تعريف خاصيّة `senderPeerID` (معرّف نظير المرسِل) من نوع نص قابل للعدم (String?) قيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:66]

```
67:     val mentions: List<String>? = null,
```
> تعريف خاصيّة `mentions` (الإشارات) من نوع قائمة نصوص قابلة للعدم (List<String>?) قيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:67]

```
68:     val channel: String? = null,
```
> تعريف خاصيّة `channel` (القناة) من نوع نص قابل للعدم (String?) قيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:68]

```
69:     val encryptedContent: ByteArray? = null,
```
> تعريف خاصيّة `encryptedContent` (المحتوى المشفّر) من نوع مصفوفة بايتات قابلة للعدم (ByteArray?) قيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:69]

```
70:     val isEncrypted: Boolean = false,
```
> تعريف خاصيّة `isEncrypted` (هل مشفّرة) من نوع منطقي (Boolean) قيمتها الافتراضية `false`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:70]

```
71:     val deliveryStatus: DeliveryStatus? = null,
```
> تعريف خاصيّة `deliveryStatus` (حالة التسليم) من نوع `DeliveryStatus?` قابل للعدم قيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:71]

```
72:     val powDifficulty: Int? = null
```
> تعريف خاصيّة `powDifficulty` (صعوبة إثبات العمل) من نوع عدد صحيح قابل للعدم (Int?) قيمتها الافتراضية `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:72]

```
73: ) : Parcelable {
```
> إغلاق قائمة معاملات البانِي مع إعلان أن الصنف `BitchatMessage` يطبّق الواجهة `Parcelable`، وفتح نطاق جسم الصنف. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:73]

```
74: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:74]

```
75:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:75]

```
76:      * Convert message to binary payload format - exactly same as iOS version
```
> تعليق: «تحويل الرسالة إلى صيغة حمولة ثنائية - مطابقة تماماً لنسخة iOS». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:76]

```
77:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:77]

```
78:     fun toBinaryPayload(): ByteArray? {
```
> تعريف دالة (إلى حمولة ثنائية - toBinaryPayload) لا تأخذ معاملات وتعيد مصفوفة بايتات قابلة للعدم (ByteArray?)، وفتح نطاقها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:78]

```
79:         try {
```
> بدء كتلة `try` لمحاولة تنفيذ التعليمات مع التقاط الاستثناءات، وفتح نطاقها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:79]

```
80:             val buffer = ByteBuffer.allocate(4096).apply { order(ByteOrder.BIG_ENDIAN) }
```
> تعريف متغيّر `buffer` بإنشاء مخزن بايتات (ByteBuffer) بسعة 4096 بايت، وضبط ترتيب بايتاته على الترتيب الكبير أولاً (BIG_ENDIAN). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:80]

```
81: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:81]

```
82:             // Message format:
```
> تعليق: «صيغة الرسالة:». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:82]

```
83:             // - Flags: 1 byte (bit flags for optional fields)
```
> تعليق: «- الأعلام: بايت واحد (أعلام بِتّية للحقول الاختيارية)». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:83]

```
84:             // - Timestamp: 8 bytes (milliseconds since epoch, big-endian)
```
> تعليق: «- الطابع الزمني: 8 بايتات (ميلي‑ثانية منذ بداية الحقبة، الترتيب الكبير أولاً)». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:84]

```
85:             // - ID length: 1 byte + ID data
```
> تعليق: «- طول المعرّف: بايت واحد + بيانات المعرّف». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:85]

```
86:             // - Sender length: 1 byte + sender data
```
> تعليق: «- طول المرسِل: بايت واحد + بيانات المرسِل». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:86]

```
87:             // - Content length: 2 bytes + content data (or encrypted content)
```
> تعليق: «- طول المحتوى: 2 بايت + بيانات المحتوى (أو المحتوى المشفّر)». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:87]

```
88:             // Optional fields based on flags...
```
> تعليق: «حقول اختيارية بناءً على الأعلام...». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:88]

```
89: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:89]

```
90:             var flags: UByte = 0u
```
> تعريف متغيّر قابل للتغيير `flags` (الأعلام) من نوع بايت غير مُوقَّع (UByte) قيمته الابتدائية صفر. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:90]

```
91:             if (isRelay) flags = flags or 0x01u
```
> إذا كانت `isRelay` صحيحة تُدمَج القيمة `0x01` في `flags` بعملية «أو» البِتّية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:91]

```
92:             if (isPrivate) flags = flags or 0x02u
```
> إذا كانت `isPrivate` صحيحة تُدمَج القيمة `0x02` في `flags` بعملية «أو» البِتّية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:92]

```
93:             if (originalSender != null) flags = flags or 0x04u
```
> إذا كانت `originalSender` ليست عدماً تُدمَج القيمة `0x04` في `flags` بعملية «أو» البِتّية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:93]

```
94:             if (recipientNickname != null) flags = flags or 0x08u
```
> إذا كانت `recipientNickname` ليست عدماً تُدمَج القيمة `0x08` في `flags` بعملية «أو» البِتّية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:94]

```
95:             if (senderPeerID != null) flags = flags or 0x10u
```
> إذا كانت `senderPeerID` ليست عدماً تُدمَج القيمة `0x10` في `flags` بعملية «أو» البِتّية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:95]

```
96:             if (mentions != null && mentions.isNotEmpty()) flags = flags or 0x20u
```
> إذا كانت `mentions` ليست عدماً وليست فارغة تُدمَج القيمة `0x20` في `flags` بعملية «أو» البِتّية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:96]

```
97:             if (channel != null) flags = flags or 0x40u
```
> إذا كانت `channel` ليست عدماً تُدمَج القيمة `0x40` في `flags` بعملية «أو» البِتّية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:97]

```
98:             if (isEncrypted) flags = flags or 0x80u
```
> إذا كانت `isEncrypted` صحيحة تُدمَج القيمة `0x80` في `flags` بعملية «أو» البِتّية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:98]

```
99: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:99]

```
100:             buffer.put(flags.toByte())
```
> وضع قيمة `flags` (محوّلة إلى بايت) في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:100]

```
101: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:101]

```
102:             // Timestamp (in milliseconds, 8 bytes big-endian)
```
> تعليق: «الطابع الزمني (بالميلي‑ثانية، 8 بايتات بالترتيب الكبير أولاً)». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:102]

```
103:             val timestampMillis = timestamp.time
```
> تعريف متغيّر `timestampMillis` بقيمة `time` من الخاصيّة `timestamp` (عدد الميلي‑ثواني). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:103]

```
104:             buffer.putLong(timestampMillis)
```
> وضع قيمة `timestampMillis` (عدد طويل من 8 بايتات) في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:104]

```
105: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:105]

```
106:             // ID
```
> تعليق: «المعرّف». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:106]

```
107:             val idBytes = id.toByteArray(Charsets.UTF_8)
```
> تعريف متغيّر `idBytes` بتحويل الخاصيّة `id` إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:107]

```
108:             buffer.put(minOf(idBytes.size, 255).toByte())
```
> وضع بايت يساوي أصغر قيمة بين حجم `idBytes` والعدد 255 في المخزن (طول المعرّف). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:108]

```
109:             buffer.put(idBytes.take(255).toByteArray())
```
> وضع أول 255 بايتاً على الأكثر من `idBytes` في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:109]

```
110: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:110]

```
111:             // Sender
```
> تعليق: «المرسِل». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:111]

```
112:             val senderBytes = sender.toByteArray(Charsets.UTF_8)
```
> تعريف متغيّر `senderBytes` بتحويل الخاصيّة `sender` إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:112]

```
113:             buffer.put(minOf(senderBytes.size, 255).toByte())
```
> وضع بايت يساوي أصغر قيمة بين حجم `senderBytes` والعدد 255 في المخزن (طول المرسِل). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:113]

```
114:             buffer.put(senderBytes.take(255).toByteArray())
```
> وضع أول 255 بايتاً على الأكثر من `senderBytes` في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:114]

```
115: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:115]

```
116:             // Content or encrypted content
```
> تعليق: «المحتوى أو المحتوى المشفّر». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:116]

```
117:             if (isEncrypted && encryptedContent != null) {
```
> شرط: إذا كانت `isEncrypted` صحيحة و`encryptedContent` ليست عدماً، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:117]

```
118:                 val length = minOf(encryptedContent.size, 65535)
```
> تعريف متغيّر `length` بأصغر قيمة بين حجم `encryptedContent` والعدد 65535. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:118]

```
119:                 buffer.putShort(length.toShort())
```
> وضع قيمة `length` (عدد قصير من بايتين) في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:119]

```
120:                 buffer.put(encryptedContent.take(length).toByteArray())
```
> وضع أول `length` بايتاً من `encryptedContent` في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:120]

```
121:             } else {
```
> إغلاق كتلة `if` وفتح كتلة `else`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:121]

```
122:                 val contentBytes = content.toByteArray(Charsets.UTF_8)
```
> تعريف متغيّر `contentBytes` بتحويل الخاصيّة `content` إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:122]

```
123:                 val length = minOf(contentBytes.size, 65535)
```
> تعريف متغيّر `length` بأصغر قيمة بين حجم `contentBytes` والعدد 65535. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:123]

```
124:                 buffer.putShort(length.toShort())
```
> وضع قيمة `length` (عدد قصير من بايتين) في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:124]

```
125:                 buffer.put(contentBytes.take(length).toByteArray())
```
> وضع أول `length` بايتاً من `contentBytes` في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:125]

```
126:             }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:126]

```
127: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:127]

```
128:             // Optional fields
```
> تعليق: «حقول اختيارية». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:128]

```
129:             originalSender?.let { origSender ->
```
> استدعاء `let` على `originalSender` إن لم تكن عدماً، بإسناد قيمتها للمعامل `origSender`، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:129]

```
130:                 val origBytes = origSender.toByteArray(Charsets.UTF_8)
```
> تعريف متغيّر `origBytes` بتحويل `origSender` إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:130]

```
131:                 buffer.put(minOf(origBytes.size, 255).toByte())
```
> وضع بايت يساوي أصغر قيمة بين حجم `origBytes` والعدد 255 في المخزن. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:131]

```
132:                 buffer.put(origBytes.take(255).toByteArray())
```
> وضع أول 255 بايتاً على الأكثر من `origBytes` في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:132]

```
133:             }
```
> إغلاق نطاق كتلة `let` الخاصة بـ `originalSender`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:133]

```
134: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:134]

```
135:             recipientNickname?.let { recipient ->
```
> استدعاء `let` على `recipientNickname` إن لم تكن عدماً، بإسناد قيمتها للمعامل `recipient`، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:135]

```
136:                 val recipBytes = recipient.toByteArray(Charsets.UTF_8)
```
> تعريف متغيّر `recipBytes` بتحويل `recipient` إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:136]

```
137:                 buffer.put(minOf(recipBytes.size, 255).toByte())
```
> وضع بايت يساوي أصغر قيمة بين حجم `recipBytes` والعدد 255 في المخزن. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:137]

```
138:                 buffer.put(recipBytes.take(255).toByteArray())
```
> وضع أول 255 بايتاً على الأكثر من `recipBytes` في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:138]

```
139:             }
```
> إغلاق نطاق كتلة `let` الخاصة بـ `recipientNickname`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:139]

```
140: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:140]

```
141:             senderPeerID?.let { peerID ->
```
> استدعاء `let` على `senderPeerID` إن لم تكن عدماً، بإسناد قيمتها للمعامل `peerID`، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:141]

```
142:                 val peerBytes = peerID.toByteArray(Charsets.UTF_8)
```
> تعريف متغيّر `peerBytes` بتحويل `peerID` إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:142]

```
143:                 buffer.put(minOf(peerBytes.size, 255).toByte())
```
> وضع بايت يساوي أصغر قيمة بين حجم `peerBytes` والعدد 255 في المخزن. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:143]

```
144:                 buffer.put(peerBytes.take(255).toByteArray())
```
> وضع أول 255 بايتاً على الأكثر من `peerBytes` في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:144]

```
145:             }
```
> إغلاق نطاق كتلة `let` الخاصة بـ `senderPeerID`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:145]

```
146: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:146]

```
147:             // Mentions array
```
> تعليق: «مصفوفة الإشارات». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:147]

```
148:             mentions?.let { mentionList ->
```
> استدعاء `let` على `mentions` إن لم تكن عدماً، بإسناد قيمتها للمعامل `mentionList`، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:148]

```
149:                 buffer.put(minOf(mentionList.size, 255).toByte())
```
> وضع بايت يساوي أصغر قيمة بين عدد عناصر `mentionList` والعدد 255 في المخزن (عدد الإشارات). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:149]

```
150:                 mentionList.take(255).forEach { mention ->
```
> المرور على أول 255 عنصراً على الأكثر من `mentionList`، وإسناد كل عنصر للمعامل `mention`، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:150]

```
151:                     val mentionBytes = mention.toByteArray(Charsets.UTF_8)
```
> تعريف متغيّر `mentionBytes` بتحويل `mention` إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:151]

```
152:                     buffer.put(minOf(mentionBytes.size, 255).toByte())
```
> وضع بايت يساوي أصغر قيمة بين حجم `mentionBytes` والعدد 255 في المخزن. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:152]

```
153:                     buffer.put(mentionBytes.take(255).toByteArray())
```
> وضع أول 255 بايتاً على الأكثر من `mentionBytes` في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:153]

```
154:                 }
```
> إغلاق نطاق كتلة `forEach` على عناصر `mentionList`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:154]

```
155:             }
```
> إغلاق نطاق كتلة `let` الخاصة بـ `mentions`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:155]

```
156: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:156]

```
157:             // Channel hashtag
```
> تعليق: «وسم القناة (هاشتاغ)». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:157]

```
158:             channel?.let { channelName ->
```
> استدعاء `let` على `channel` إن لم تكن عدماً، بإسناد قيمتها للمعامل `channelName`، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:158]

```
159:                 val channelBytes = channelName.toByteArray(Charsets.UTF_8)
```
> تعريف متغيّر `channelBytes` بتحويل `channelName` إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:159]

```
160:                 buffer.put(minOf(channelBytes.size, 255).toByte())
```
> وضع بايت يساوي أصغر قيمة بين حجم `channelBytes` والعدد 255 في المخزن. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:160]

```
161:                 buffer.put(channelBytes.take(255).toByteArray())
```
> وضع أول 255 بايتاً على الأكثر من `channelBytes` في المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:161]

```
162:             }
```
> إغلاق نطاق كتلة `let` الخاصة بـ `channel`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:162]

```
163: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:163]

```
164:             val result = ByteArray(buffer.position())
```
> تعريف متغيّر `result` كمصفوفة بايتات بحجم يساوي الموضع الحالي للمخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:164]

```
165:             buffer.rewind()
```
> إعادة مؤشر المخزن `buffer` إلى البداية (الموضع صفر). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:165]

```
166:             buffer.get(result)
```
> قراءة بايتات من المخزن `buffer` وملء المصفوفة `result` بها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:166]

```
167:             return result
```
> إعادة المصفوفة `result` كنتيجة للدالة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:167]

```
168: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:168]

```
169:         } catch (e: Exception) {
```
> إغلاق كتلة `try` وبدء كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`، وفتح نطاقها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:169]

```
170:             return null
```
> إعادة القيمة `null` عند حدوث استثناء. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:170]

```
171:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:171]

```
172:     }
```
> إغلاق نطاق الدالة `toBinaryPayload`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:172]

```
173: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:173]

```
174:     companion object {
```
> تعريف كائن مصاحب (companion object) داخل الصنف، وفتح نطاقه. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:174]

```
175:         /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:175]

```
176:          * Parse message from binary payload - exactly same logic as iOS version
```
> تعليق: «تحليل الرسالة من الحمولة الثنائية - بنفس منطق نسخة iOS تماماً». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:176]

```
177:          */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:177]

```
178:         fun fromBinaryPayload(data: ByteArray): BitchatMessage? {
```
> تعريف دالة (من حمولة ثنائية - fromBinaryPayload) تأخذ معاملاً `data` من نوع مصفوفة بايتات (ByteArray) وتعيد `BitchatMessage?` قابلاً للعدم، وفتح نطاقها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:178]

```
179:             try {
```
> بدء كتلة `try` لمحاولة تنفيذ التعليمات مع التقاط الاستثناءات، وفتح نطاقها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:179]

```
180:                 if (data.size < 13) return null
```
> إذا كان حجم `data` أقل من 13 بايتاً تُعاد القيمة `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:180]

```
181: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:181]

```
182:                 val buffer = ByteBuffer.wrap(data).apply { order(ByteOrder.BIG_ENDIAN) }
```
> تعريف متغيّر `buffer` بلفّ المصفوفة `data` في مخزن بايتات (ByteBuffer)، وضبط ترتيب بايتاته على الترتيب الكبير أولاً (BIG_ENDIAN). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:182]

```
183: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:183]

```
184:                 // Flags
```
> تعليق: «الأعلام». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:184]

```
185:                 val flags = buffer.get().toUByte()
```
> تعريف متغيّر `flags` بقراءة بايت من المخزن وتحويله إلى بايت غير مُوقَّع (UByte). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:185]

```
186:                 val isRelay = (flags and 0x01u) != 0u.toUByte()
```
> تعريف متغيّر `isRelay` بنتيجة فحص ما إذا كان البِت `0x01` مضبوطاً في `flags`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:186]

```
187:                 val isPrivate = (flags and 0x02u) != 0u.toUByte()
```
> تعريف متغيّر `isPrivate` بنتيجة فحص ما إذا كان البِت `0x02` مضبوطاً في `flags`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:187]

```
188:                 val hasOriginalSender = (flags and 0x04u) != 0u.toUByte()
```
> تعريف متغيّر `hasOriginalSender` (هل يوجد مرسِل أصلي) بنتيجة فحص ما إذا كان البِت `0x04` مضبوطاً في `flags`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:188]

```
189:                 val hasRecipientNickname = (flags and 0x08u) != 0u.toUByte()
```
> تعريف متغيّر `hasRecipientNickname` (هل يوجد لقب مستلِم) بنتيجة فحص ما إذا كان البِت `0x08` مضبوطاً في `flags`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:189]

```
190:                 val hasSenderPeerID = (flags and 0x10u) != 0u.toUByte()
```
> تعريف متغيّر `hasSenderPeerID` (هل يوجد معرّف نظير مرسِل) بنتيجة فحص ما إذا كان البِت `0x10` مضبوطاً في `flags`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:190]

```
191:                 val hasMentions = (flags and 0x20u) != 0u.toUByte()
```
> تعريف متغيّر `hasMentions` (هل توجد إشارات) بنتيجة فحص ما إذا كان البِت `0x20` مضبوطاً في `flags`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:191]

```
192:                 val hasChannel = (flags and 0x40u) != 0u.toUByte()
```
> تعريف متغيّر `hasChannel` (هل توجد قناة) بنتيجة فحص ما إذا كان البِت `0x40` مضبوطاً في `flags`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:192]

```
193:                 val isEncrypted = (flags and 0x80u) != 0u.toUByte()
```
> تعريف متغيّر `isEncrypted` بنتيجة فحص ما إذا كان البِت `0x80` مضبوطاً في `flags`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:193]

```
194: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:194]

```
195:                 // Timestamp
```
> تعليق: «الطابع الزمني». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:195]

```
196:                 val timestampMillis = buffer.getLong()
```
> تعريف متغيّر `timestampMillis` بقراءة عدد طويل (8 بايتات) من المخزن `buffer`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:196]

```
197:                 val timestamp = Date(timestampMillis)
```
> تعريف متغيّر `timestamp` بإنشاء تاريخ (Date) من قيمة الميلي‑ثواني `timestampMillis`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:197]

```
198: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:198]

```
199:                 // ID
```
> تعليق: «المعرّف». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:199]

```
200:                 val idLength = buffer.get().toInt() and 0xFF
```
> تعريف متغيّر `idLength` (طول المعرّف) بقراءة بايت من المخزن وتحويله إلى عدد صحيح مع تطبيق قناع `0xFF`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:200]

```
201:                 if (buffer.remaining() < idLength) return null
```
> إذا كان عدد البايتات المتبقية في المخزن أقل من `idLength` تُعاد القيمة `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:201]

```
202:                 val idBytes = ByteArray(idLength)
```
> تعريف متغيّر `idBytes` كمصفوفة بايتات بحجم `idLength`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:202]

```
203:                 buffer.get(idBytes)
```
> قراءة بايتات من المخزن `buffer` وملء المصفوفة `idBytes` بها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:203]

```
204:                 val id = String(idBytes, Charsets.UTF_8)
```
> تعريف متغيّر `id` بتحويل المصفوفة `idBytes` إلى نص بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:204]

```
205: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:205]

```
206:                 // Sender
```
> تعليق: «المرسِل». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:206]

```
207:                 val senderLength = buffer.get().toInt() and 0xFF
```
> تعريف متغيّر `senderLength` (طول المرسِل) بقراءة بايت من المخزن وتحويله إلى عدد صحيح مع تطبيق قناع `0xFF`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:207]

```
208:                 if (buffer.remaining() < senderLength) return null
```
> إذا كان عدد البايتات المتبقية في المخزن أقل من `senderLength` تُعاد القيمة `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:208]

```
209:                 val senderBytes = ByteArray(senderLength)
```
> تعريف متغيّر `senderBytes` كمصفوفة بايتات بحجم `senderLength`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:209]

```
210:                 buffer.get(senderBytes)
```
> قراءة بايتات من المخزن `buffer` وملء المصفوفة `senderBytes` بها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:210]

```
211:                 val sender = String(senderBytes, Charsets.UTF_8)
```
> تعريف متغيّر `sender` بتحويل المصفوفة `senderBytes` إلى نص بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:211]

```
212: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:212]

```
213:                 // Content
```
> تعليق: «المحتوى». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:213]

```
214:                 val contentLength = buffer.getShort().toInt() and 0xFFFF
```
> تعريف متغيّر `contentLength` (طول المحتوى) بقراءة عدد قصير (بايتين) من المخزن وتحويله إلى عدد صحيح مع تطبيق قناع `0xFFFF`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:214]

```
215:                 if (buffer.remaining() < contentLength) return null
```
> إذا كان عدد البايتات المتبقية في المخزن أقل من `contentLength` تُعاد القيمة `null`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:215]

```
216: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:216]

```
217:                 val content: String
```
> إعلان متغيّر `content` من نوع نص (String) دون إسناد قيمة بعد. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:217]

```
218:                 val encryptedContent: ByteArray?
```
> إعلان متغيّر `encryptedContent` من نوع مصفوفة بايتات قابلة للعدم (ByteArray?) دون إسناد قيمة بعد. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:218]

```
219: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:219]

```
220:                 if (isEncrypted) {
```
> شرط: إذا كانت `isEncrypted` صحيحة، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:220]

```
221:                     val encryptedBytes = ByteArray(contentLength)
```
> تعريف متغيّر `encryptedBytes` كمصفوفة بايتات بحجم `contentLength`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:221]

```
222:                     buffer.get(encryptedBytes)
```
> قراءة بايتات من المخزن `buffer` وملء المصفوفة `encryptedBytes` بها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:222]

```
223:                     encryptedContent = encryptedBytes
```
> إسناد المصفوفة `encryptedBytes` إلى المتغيّر `encryptedContent`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:223]

```
224:                     content = "" // Empty placeholder
```
> إسناد نص فارغ إلى `content`، مع تعليق: «عنصر نائب فارغ». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:224]

```
225:                 } else {
```
> إغلاق كتلة `if` وفتح كتلة `else`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:225]

```
226:                     val contentBytes = ByteArray(contentLength)
```
> تعريف متغيّر `contentBytes` كمصفوفة بايتات بحجم `contentLength`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:226]

```
227:                     buffer.get(contentBytes)
```
> قراءة بايتات من المخزن `buffer` وملء المصفوفة `contentBytes` بها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:227]

```
228:                     content = String(contentBytes, Charsets.UTF_8)
```
> إسناد نص ناتج من تحويل `contentBytes` بترميز UTF-8 إلى المتغيّر `content`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:228]

```
229:                     encryptedContent = null
```
> إسناد القيمة `null` إلى المتغيّر `encryptedContent`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:229]

```
230:                 }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:230]

```
231: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:231]

```
232:                 // Optional fields
```
> تعليق: «حقول اختيارية». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:232]

```
233:                 val originalSender = if (hasOriginalSender && buffer.hasRemaining()) {
```
> تعريف متغيّر `originalSender` بقيمة تعبير `if` شرطه أن `hasOriginalSender` صحيحة وأن للمخزن بايتات متبقية، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:233]

```
234:                     val length = buffer.get().toInt() and 0xFF
```
> تعريف متغيّر `length` بقراءة بايت من المخزن وتحويله إلى عدد صحيح مع تطبيق قناع `0xFF`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:234]

```
235:                     if (buffer.remaining() >= length) {
```
> شرط: إذا كان عدد البايتات المتبقية في المخزن أكبر من أو يساوي `length`، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:235]

```
236:                         val bytes = ByteArray(length)
```
> تعريف متغيّر `bytes` كمصفوفة بايتات بحجم `length`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:236]

```
237:                         buffer.get(bytes)
```
> قراءة بايتات من المخزن `buffer` وملء المصفوفة `bytes` بها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:237]

```
238:                         String(bytes, Charsets.UTF_8)
```
> إنتاج نص من تحويل المصفوفة `bytes` بترميز UTF-8 كقيمة للكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:238]

```
239:                     } else null
```
> إغلاق كتلة `if` وإعادة `null` في حالة `else`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:239]

```
240:                 } else null
```
> إغلاق الكتلة الخارجية وإعادة `null` في حالة `else` (إذا لم يوجد مرسِل أصلي أو لا بايتات متبقية). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:240]

```
241: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:241]

```
242:                 val recipientNickname = if (hasRecipientNickname && buffer.hasRemaining()) {
```
> تعريف متغيّر `recipientNickname` بقيمة تعبير `if` شرطه أن `hasRecipientNickname` صحيحة وأن للمخزن بايتات متبقية، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:242]

```
243:                     val length = buffer.get().toInt() and 0xFF
```
> تعريف متغيّر `length` بقراءة بايت من المخزن وتحويله إلى عدد صحيح مع تطبيق قناع `0xFF`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:243]

```
244:                     if (buffer.remaining() >= length) {
```
> شرط: إذا كان عدد البايتات المتبقية في المخزن أكبر من أو يساوي `length`، وفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:244]

```
245:                         val bytes = ByteArray(length)
```
> تعريف متغيّر `bytes` كمصفوفة بايتات بحجم `length`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:245]

```
246:                         buffer.get(bytes)
```
> قراءة بايتات من المخزن `buffer` وملء المصفوفة `bytes` بها. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:246]

```
247:                         String(bytes, Charsets.UTF_8)
```
> إنتاج نص من تحويل المصفوفة `bytes` بترميز UTF-8 كقيمة للكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:247]

```
248:                     } else null
```
> إغلاق كتلة `if` وإعادة `null` في حالة `else`. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:248]

```
249:                 } else null
```
> إغلاق الكتلة الخارجية وإعادة `null` في حالة `else` (إذا لم يوجد لقب مستلِم أو لا بايتات متبقية). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:249]

```
250: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:250]
