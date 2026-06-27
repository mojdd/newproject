# شريحة — app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt (الأسطر 1–250)

```
1: package com.bitchat.android.protocol
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:2]

```
3: import android.os.Parcelable
```
> يستورد الواجهة (Parcelable) من android.os التي تسمح بنقل الكائن بين مكوّنات أندرويد. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:3]

```
4: import kotlinx.parcelize.Parcelize
```
> يستورد التعليق التوضيحي (Parcelize) من kotlinx.parcelize لتوليد كود التحزيم تلقائياً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:4]

```
5: import java.nio.ByteBuffer
```
> يستورد الصنف (ByteBuffer) من java.nio لإدارة مخزن من البايتات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:5]

```
6: import java.nio.ByteOrder
```
> يستورد الصنف (ByteOrder) من java.nio لتحديد ترتيب البايتات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:6]

```
7: import android.util.Log
```
> يستورد الصنف (Log) من android.util لتسجيل الرسائل. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:8]

```
9: /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:9]

```
10:  * Message types - exact same as iOS version with Noise Protocol support
```
> تعليق: «أنواع الرسائل - مطابقة تماماً لنسخة iOS مع دعم بروتوكول Noise». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:10]

```
11:  */
```
> تعليق توثيقي: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:11]

```
12: enum class MessageType(val value: UByte) {
```
> يُعرّف صنفاً تعدادياً (MessageType / نوع الرسالة) يحمل كل عنصر منه قيمة من نوع UByte اسمها value. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:12]

```
13:     ANNOUNCE(0x01u),
```
> يُعرّف العنصر (ANNOUNCE / إعلان) بالقيمة الست عشرية 0x01u. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:13]

```
14:     MESSAGE(0x02u),  // All user messages (private and broadcast)
```
> يُعرّف العنصر (MESSAGE / رسالة) بالقيمة الست عشرية 0x02u، مع تعليق: «كل رسائل المستخدم (الخاصة والبثّ)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:14]

```
15:     LEAVE(0x03u),
```
> يُعرّف العنصر (LEAVE / مغادرة) بالقيمة الست عشرية 0x03u. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:15]

```
16:     NOISE_HANDSHAKE(0x10u),  // Noise handshake
```
> يُعرّف العنصر (NOISE_HANDSHAKE / مصافحة Noise) بالقيمة الست عشرية 0x10u، مع تعليق: «مصافحة Noise». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:16]

```
17:     NOISE_ENCRYPTED(0x11u),  // Noise encrypted transport message
```
> يُعرّف العنصر (NOISE_ENCRYPTED / مشفّر Noise) بالقيمة الست عشرية 0x11u، مع تعليق: «رسالة نقل مشفّرة عبر Noise». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:17]

```
18:     FRAGMENT(0x20u), // Fragmentation for large packets
```
> يُعرّف العنصر (FRAGMENT / شظية) بالقيمة الست عشرية 0x20u، مع تعليق: «تجزئة للحزم الكبيرة». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:18]

```
19:     REQUEST_SYNC(0x21u), // GCS-based sync request
```
> يُعرّف العنصر (REQUEST_SYNC / طلب مزامنة) بالقيمة الست عشرية 0x21u، مع تعليق: «طلب مزامنة قائم على GCS». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:19]

```
20:     FILE_TRANSFER(0x22u); // New: File transfer packet (BLE voice notes, etc.)
```
> يُعرّف العنصر (FILE_TRANSFER / نقل ملف) بالقيمة الست عشرية 0x22u وينهي قائمة العناصر بفاصلة منقوطة، مع تعليق: «جديد: حزمة نقل ملف (ملاحظات صوتية عبر BLE، إلخ)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:20]

```
21: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:21]

```
22:     companion object {
```
> يفتح كائناً مرافقاً (companion object) داخل صنف MessageType. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:22]

```
23:         fun fromValue(value: UByte): MessageType? {
```
> يُعرّف دالة (fromValue / من قيمة) تأخذ معاملاً value من نوع UByte وتُعيد MessageType أو null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:23]

```
24:             return values().find { it.value == value }
```
> يُعيد أول عنصر من values() تتساوى قيمته value مع المعامل المُمرَّر. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:24]

```
25:         }
```
> إغلاق نطاق الدالة fromValue. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:25]

```
26:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:26]

```
27: }
```
> إغلاق نطاق الصنف التعدادي MessageType. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:28]

```
29: /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:29]

```
30:  * Special recipient IDs - exact same as iOS version
```
> تعليق: «معرّفات المستلِم الخاصة - مطابقة تماماً لنسخة iOS». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:30]

```
31:  */
```
> تعليق توثيقي: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:31]

```
32: object SpecialRecipients {
```
> يُعرّف كائناً مفرداً (SpecialRecipients / المستلِمون الخاصون). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:32]

```
33:     val BROADCAST = ByteArray(8) { 0xFF.toByte() }  // All 0xFF = broadcast
```
> يُعرّف الثابت (BROADCAST / البثّ) كمصفوفة بايتات طولها 8 كل عنصر فيها بقيمة 0xFF، مع تعليق: «كل البايتات 0xFF = بثّ». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:33]

```
34: }
```
> إغلاق نطاق الكائن SpecialRecipients. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:34]

```
35: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:35]

```
36: /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:36]

```
37:  * Binary packet format - 100% backward compatible with iOS version
```
> تعليق: «صيغة الحزمة الثنائية - متوافقة رجعياً 100% مع نسخة iOS». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:37]

```
38:  *
```
> تعليق: سطر فارغ داخل التعليق التوثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:38]

```
39:  * Header (14 bytes for v1, 16 bytes for v2):
```
> تعليق: «الترويسة (14 بايت للإصدار v1، 16 بايت للإصدار v2):». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:39]

```
40:  * - Version: 1 byte
```
> تعليق: «- الإصدار: 1 بايت». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:40]

```
41:  * - Type: 1 byte
```
> تعليق: «- النوع: 1 بايت». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:41]

```
42:  * - TTL: 1 byte
```
> تعليق: «- TTL (مدة البقاء): 1 بايت». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:42]

```
43:  * - Timestamp: 8 bytes (UInt64, big-endian)
```
> تعليق: «- الطابع الزمني: 8 بايتات (UInt64، ترتيب big-endian)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:43]

```
44:  * - Flags: 1 byte (bit 0: hasRecipient, bit 1: hasSignature, bit 2: isCompressed)
```
> تعليق: «- الأعلام: 1 بايت (البت 0: يوجد مستلِم، البت 1: يوجد توقيع، البت 2: مضغوط)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:44]

```
45:  * - PayloadLength: 2 bytes (v1) / 4 bytes (v2) (big-endian)
```
> تعليق: «- طول الحمولة: 2 بايت (v1) / 4 بايتات (v2) (ترتيب big-endian)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:45]

```
46:  *
```
> تعليق: سطر فارغ داخل التعليق التوثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:46]

```
47:  * Variable sections:
```
> تعليق: «الأقسام المتغيّرة:». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:47]

```
48:  * - SenderID: 8 bytes (fixed)
```
> تعليق: «- معرّف المُرسِل: 8 بايتات (ثابت)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:48]

```
49:  * - RecipientID: 8 bytes (if hasRecipient flag set)
```
> تعليق: «- معرّف المستلِم: 8 بايتات (إذا كان علم hasRecipient مضبوطاً)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:49]

```
50:  * - Payload: Variable length (includes original size if compressed)
```
> تعليق: «- الحمولة: طول متغيّر (تتضمّن الحجم الأصلي إن كانت مضغوطة)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:50]

```
51:  * - Signature: 64 bytes (if hasSignature flag set)
```
> تعليق: «- التوقيع: 64 بايتاً (إذا كان علم hasSignature مضبوطاً)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:51]

```
52:  */
```
> تعليق توثيقي: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:52]

```
53: @Parcelize
```
> يُطبّق التعليق التوضيحي (Parcelize) على الصنف التالي لتوليد كود التحزيم تلقائياً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:53]

```
54: data class BitchatPacket(
```
> يُعرّف صنف بيانات (BitchatPacket / حزمة بِتشات) ويفتح قائمة معاملاته الأولية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:54]

```
55:     val version: UByte = 1u,
```
> يُعرّف الخاصية (version / الإصدار) من نوع UByte بقيمة افتراضية 1u. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:55]

```
56:     val type: UByte,
```
> يُعرّف الخاصية (type / النوع) من نوع UByte بلا قيمة افتراضية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:56]

```
57:     val senderID: ByteArray,
```
> يُعرّف الخاصية (senderID / معرّف المُرسِل) من نوع مصفوفة بايتات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:57]

```
58:     val recipientID: ByteArray? = null,
```
> يُعرّف الخاصية (recipientID / معرّف المستلِم) من نوع مصفوفة بايتات قابلة لأن تكون null بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:58]

```
59:     val timestamp: ULong,
```
> يُعرّف الخاصية (timestamp / الطابع الزمني) من نوع ULong. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:59]

```
60:     val payload: ByteArray,
```
> يُعرّف الخاصية (payload / الحمولة) من نوع مصفوفة بايتات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:60]

```
61:     var signature: ByteArray? = null,  // Changed from val to var for packet signing
```
> يُعرّف الخاصية القابلة للتغيير (signature / التوقيع) من نوع مصفوفة بايتات قابلة لأن تكون null بقيمة افتراضية null، مع تعليق: «غُيّرت من val إلى var لأجل توقيع الحزمة». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:61]

```
62:     var ttl: UByte,
```
> يُعرّف الخاصية القابلة للتغيير (ttl / مدة البقاء) من نوع UByte. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:62]

```
63:     var route: List<ByteArray>? = null // Optional source route: ordered list of peerIDs (8 bytes each), not including sender and final recipient
```
> يُعرّف الخاصية القابلة للتغيير (route / المسار) كقائمة من مصفوفات بايتات قابلة لأن تكون null بقيمة افتراضية null، مع تعليق: «مسار مصدر اختياري: قائمة مرتّبة من معرّفات الأقران (8 بايتات لكل واحد)، لا تشمل المُرسِل والمستلِم النهائي». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:63]

```
64: ) : Parcelable {
```
> يُغلق قائمة المعاملات ويُعلن أن الصنف BitchatPacket يُطبّق الواجهة Parcelable ويفتح جسده. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:65]

```
66:     constructor(
```
> يبدأ تعريف بانٍ ثانوي (constructor) للصنف BitchatPacket ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:66]

```
67:         type: UByte,
```
> يُعرّف معامل البانِي (type) من نوع UByte. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:67]

```
68:         ttl: UByte,
```
> يُعرّف معامل البانِي (ttl) من نوع UByte. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:68]

```
69:         senderID: String,
```
> يُعرّف معامل البانِي (senderID) من نوع نص String. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:69]

```
70:         payload: ByteArray
```
> يُعرّف معامل البانِي (payload) من نوع مصفوفة بايتات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:70]

```
71:     ) : this(
```
> يُغلق معاملات البانِي الثانوي ويستدعي البانِي الأوّلي this مفتتحاً قائمة وسائطه. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:71]

```
72:         version = 1u,
```
> يمرّر للوسيط version القيمة 1u. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:72]

```
73:         type = type,
```
> يمرّر للوسيط type قيمة المعامل type. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:73]

```
74:         senderID = hexStringToByteArray(senderID),
```
> يمرّر للوسيط senderID ناتج تحويل النص senderID إلى مصفوفة بايتات عبر الدالة hexStringToByteArray. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:74]

```
75:         recipientID = null,
```
> يمرّر للوسيط recipientID القيمة null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:75]

```
76:         timestamp = (System.currentTimeMillis()).toULong(),
```
> يمرّر للوسيط timestamp الوقت الحالي بالميلي ثانية محوّلاً إلى ULong. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:76]

```
77:         payload = payload,
```
> يمرّر للوسيط payload قيمة المعامل payload. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:77]

```
78:         signature = null,
```
> يمرّر للوسيط signature القيمة null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:78]

```
79:         ttl = ttl
```
> يمرّر للوسيط ttl قيمة المعامل ttl. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:79]

```
80:     )
```
> يُغلق قائمة وسائط استدعاء البانِي الأوّلي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:80]

```
81: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:81]

```
82:     fun toBinaryData(padding: Boolean = true): ByteArray? {
```
> يُعرّف دالة (toBinaryData / إلى بيانات ثنائية) تأخذ معاملاً padding من نوع Boolean بقيمة افتراضية true وتُعيد مصفوفة بايتات أو null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:82]

```
83:         return BinaryProtocol.encode(this, padding = padding)
```
> يُعيد ناتج استدعاء الدالة encode في BinaryProtocol مع تمرير الحزمة الحالية this وقيمة padding. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:83]

```
84:     }
```
> إغلاق نطاق الدالة toBinaryData. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:84]

```
85: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:85]

```
86:     /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:86]

```
87:      * Create binary representation for signing (without signature and TTL fields)
```
> تعليق: «إنشاء تمثيل ثنائي لأجل التوقيع (بدون حقلي التوقيع و TTL)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:87]

```
88:      * TTL is excluded because it changes during packet relay operations
```
> تعليق: «يُستبعد TTL لأنه يتغيّر أثناء عمليات إعادة بثّ الحزمة». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:88]

```
89:      */
```
> تعليق توثيقي: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:89]

```
90:     fun toBinaryDataForSigning(): ByteArray? {
```
> يُعرّف دالة (toBinaryDataForSigning / إلى بيانات ثنائية للتوقيع) بلا معاملات وتُعيد مصفوفة بايتات أو null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:90]

```
91:         // Create a copy without signature and with fixed TTL for signing
```
> تعليق: «إنشاء نسخة بدون توقيع ومع TTL ثابت لأجل التوقيع». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:91]

```
92:         // TTL must be excluded because it changes during relay
```
> تعليق: «يجب استبعاد TTL لأنه يتغيّر أثناء إعادة البثّ». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:92]

```
93:         val unsignedPacket = BitchatPacket(
```
> يُعرّف المتغيّر (unsignedPacket / الحزمة غير الموقّعة) بإنشاء كائن BitchatPacket جديد. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:93]

```
94:             version = version,
```
> يمرّر للوسيط version قيمة الخاصية version الحالية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:94]

```
95:             type = type,
```
> يمرّر للوسيط type قيمة الخاصية type الحالية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:95]

```
96:             senderID = senderID,
```
> يمرّر للوسيط senderID قيمة الخاصية senderID الحالية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:96]

```
97:             recipientID = recipientID,
```
> يمرّر للوسيط recipientID قيمة الخاصية recipientID الحالية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:97]

```
98:             timestamp = timestamp,
```
> يمرّر للوسيط timestamp قيمة الخاصية timestamp الحالية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:98]

```
99:             payload = payload,
```
> يمرّر للوسيط payload قيمة الخاصية payload الحالية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:99]

```
100:             signature = null, // Remove signature for signing
```
> يمرّر للوسيط signature القيمة null، مع تعليق: «إزالة التوقيع لأجل التوقيع». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:100]

```
101:             route = route,
```
> يمرّر للوسيط route قيمة الخاصية route الحالية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:101]

```
102:             ttl = com.bitchat.android.util.AppConstants.SYNC_TTL_HOPS // Use fixed TTL=0 for signing to ensure relay compatibility
```
> يمرّر للوسيط ttl قيمة الثابت SYNC_TTL_HOPS من com.bitchat.android.util.AppConstants، مع تعليق: «استخدام TTL ثابت=0 لأجل التوقيع لضمان توافق إعادة البثّ». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:102]

```
103:         )
```
> يُغلق قائمة وسائط إنشاء كائن BitchatPacket. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:103]

```
104:         return BinaryProtocol.encode(unsignedPacket)
```
> يُعيد ناتج استدعاء الدالة encode في BinaryProtocol مع تمرير الحزمة غير الموقّعة unsignedPacket. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:104]

```
105:     }
```
> إغلاق نطاق الدالة toBinaryDataForSigning. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:105]

```
106: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:106]

```
107:     companion object {
```
> يفتح كائناً مرافقاً (companion object) داخل صنف BitchatPacket. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:107]

```
108:         fun fromBinaryData(data: ByteArray): BitchatPacket? {
```
> يُعرّف دالة (fromBinaryData / من بيانات ثنائية) تأخذ معاملاً data من نوع مصفوفة بايتات وتُعيد BitchatPacket أو null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:108]

```
109:             return BinaryProtocol.decode(data)
```
> يُعيد ناتج استدعاء الدالة decode في BinaryProtocol مع تمرير data. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:109]

```
110:         }
```
> إغلاق نطاق الدالة fromBinaryData. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:110]

```
111:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:111]

```
112:         /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:112]

```
113:          * Convert hex string peer ID to binary data (8 bytes) - exactly same as iOS
```
> تعليق: «تحويل معرّف القرين النصّي الست عشري إلى بيانات ثنائية (8 بايتات) - مطابق تماماً لـ iOS». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:113]

```
114:          */
```
> تعليق توثيقي: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:114]

```
115:         private fun hexStringToByteArray(hexString: String): ByteArray {
```
> يُعرّف دالة خاصة (hexStringToByteArray / نص ست عشري إلى مصفوفة بايتات) تأخذ معاملاً hexString من نوع نص وتُعيد مصفوفة بايتات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:115]

```
116:             val result = ByteArray(8) { 0 } // Initialize with zeros, exactly 8 bytes
```
> يُعرّف المتغيّر (result / النتيجة) كمصفوفة بايتات طولها 8 كل عناصرها 0، مع تعليق: «تهيئة بأصفار، 8 بايتات بالضبط». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:116]

```
117:             var tempID = hexString
```
> يُعرّف المتغيّر القابل للتغيير (tempID / المعرّف المؤقّت) ويُسند إليه قيمة hexString. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:117]

```
118:             var index = 0
```
> يُعرّف المتغيّر القابل للتغيير (index / الفهرس) ويُسند إليه القيمة 0. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:118]

```
119:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:119]

```
120:             while (tempID.length >= 2 && index < 8) {
```
> يبدأ حلقة while تتكرّر ما دام طول tempID لا يقل عن 2 و index أصغر من 8. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:120]

```
121:                 val hexByte = tempID.substring(0, 2)
```
> يُعرّف المتغيّر (hexByte / البايت الست عشري) كأول حرفين من tempID. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:121]

```
122:                 val byte = hexByte.toIntOrNull(16)?.toByte()
```
> يُعرّف المتغيّر (byte / البايت) بتحويل hexByte إلى عدد صحيح بالأساس 16 ثم إلى بايت، أو null إن فشل التحويل. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:122]

```
123:                 if (byte != null) {
```
> يفحص ما إذا كان byte ليس null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:123]

```
124:                     result[index] = byte
```
> يُسند قيمة byte إلى العنصر عند الفهرس index في المصفوفة result. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:124]

```
125:                 }
```
> إغلاق نطاق جملة if. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:125]

```
126:                 tempID = tempID.substring(2)
```
> يُعيد إسناد tempID إلى ما بعد أول حرفين منه. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:126]

```
127:                 index++
```
> يزيد قيمة index بمقدار واحد. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:127]

```
128:             }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:128]

```
129:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:129]

```
130:             return result
```
> يُعيد المصفوفة result. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:130]

```
131:         }
```
> إغلاق نطاق الدالة hexStringToByteArray. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:131]

```
132:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:132]

```
133: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:133]

```
134:     override fun equals(other: Any?): Boolean {
```
> يتجاوز الدالة (equals / يساوي) تأخذ معاملاً other من نوع Any قابل لأن يكون null وتُعيد Boolean. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:134]

```
135:         if (this === other) return true
```
> يُعيد true إن كان this هو نفس مرجع other. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:135]

```
136:         if (javaClass != other?.javaClass) return false
```
> يُعيد false إن اختلف صنف this عن صنف other أو كان other يساوي null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:136]

```
137: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:137]

```
138:         other as BitchatPacket
```
> يحوّل النوع (cast) للمتغيّر other إلى BitchatPacket. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:138]

```
139: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:139]

```
140:         if (version != other.version) return false
```
> يُعيد false إن اختلفت خاصية version عن version في other. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:140]

```
141:         if (type != other.type) return false
```
> يُعيد false إن اختلفت خاصية type عن type في other. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:141]

```
142:         if (!senderID.contentEquals(other.senderID)) return false
```
> يُعيد false إن لم يتطابق محتوى senderID مع محتوى senderID في other. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:142]

```
143:         if (recipientID != null) {
```
> يفحص ما إذا كانت خاصية recipientID ليست null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:143]

```
144:             if (other.recipientID == null) return false
```
> يُعيد false إن كانت recipientID في other تساوي null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:144]

```
145:             if (!recipientID.contentEquals(other.recipientID)) return false
```
> يُعيد false إن لم يتطابق محتوى recipientID مع محتوى recipientID في other. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:145]

```
146:         } else if (other.recipientID != null) return false
```
> يُغلق فرع if ويُعيد false إن كانت recipientID الحالية null بينما recipientID في other ليست null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:146]

```
147:         if (timestamp != other.timestamp) return false
```
> يُعيد false إن اختلفت خاصية timestamp عن timestamp في other. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:147]

```
148:         if (!payload.contentEquals(other.payload)) return false
```
> يُعيد false إن لم يتطابق محتوى payload مع محتوى payload في other. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:148]

```
149:         if (signature != null) {
```
> يفحص ما إذا كانت خاصية signature ليست null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:149]

```
150:             if (other.signature == null) return false
```
> يُعيد false إن كانت signature في other تساوي null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:150]

```
151:             if (!signature.contentEquals(other.signature)) return false
```
> يُعيد false إن لم يتطابق محتوى signature مع محتوى signature في other. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:151]

```
152:         } else if (other.signature != null) return false
```
> يُغلق فرع if ويُعيد false إن كانت signature الحالية null بينما signature في other ليست null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:152]

```
153:         if (ttl != other.ttl) return false
```
> يُعيد false إن اختلفت خاصية ttl عن ttl في other. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:153]

```
154:         if (route != null || other.route != null) {
```
> يفحص ما إذا كانت خاصية route ليست null أو route في other ليست null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:154]

```
155:             val a = route?.map { it.toList() } ?: emptyList()
```
> يُعرّف المتغيّر (a) كتحويل كل عنصر في route إلى قائمة، أو قائمة فارغة إن كانت route تساوي null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:155]

```
156:             val b = other.route?.map { it.toList() } ?: emptyList()
```
> يُعرّف المتغيّر (b) كتحويل كل عنصر في route الخاص بـ other إلى قائمة، أو قائمة فارغة إن كانت null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:156]

```
157:             if (a != b) return false
```
> يُعيد false إن اختلفت القائمة a عن القائمة b. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:157]

```
158:         }
```
> إغلاق نطاق فحص route. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:158]

```
159: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:159]

```
160:         return true
```
> يُعيد true دلالة على تساوي الكائنين. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:160]

```
161:     }
```
> إغلاق نطاق الدالة equals. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:161]

```
162: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:162]

```
163:     override fun hashCode(): Int {
```
> يتجاوز الدالة (hashCode / الرمز التجزيئي) التي لا تأخذ معاملات وتُعيد Int. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:163]

```
164:         var result = version.hashCode()
```
> يُعرّف المتغيّر القابل للتغيير (result / النتيجة) ويُسند إليه الرمز التجزيئي لخاصية version. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:164]

```
165:         result = 31 * result + type.hashCode()
```
> يُعيد إسناد result إلى ناتج ضرب القيمة الحالية في 31 مضافاً إليه الرمز التجزيئي لخاصية type. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:165]

```
166:         result = 31 * result + senderID.contentHashCode()
```
> يُعيد إسناد result إلى ناتج ضربه في 31 مضافاً إليه الرمز التجزيئي لمحتوى senderID. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:166]

```
167:         result = 31 * result + (recipientID?.contentHashCode() ?: 0)
```
> يُعيد إسناد result إلى ناتج ضربه في 31 مضافاً إليه الرمز التجزيئي لمحتوى recipientID أو 0 إن كانت null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:167]

```
168:         result = 31 * result + timestamp.hashCode()
```
> يُعيد إسناد result إلى ناتج ضربه في 31 مضافاً إليه الرمز التجزيئي لخاصية timestamp. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:168]

```
169:         result = 31 * result + payload.contentHashCode()
```
> يُعيد إسناد result إلى ناتج ضربه في 31 مضافاً إليه الرمز التجزيئي لمحتوى payload. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:169]

```
170:         result = 31 * result + (signature?.contentHashCode() ?: 0)
```
> يُعيد إسناد result إلى ناتج ضربه في 31 مضافاً إليه الرمز التجزيئي لمحتوى signature أو 0 إن كانت null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:170]

```
171:         result = 31 * result + ttl.hashCode()
```
> يُعيد إسناد result إلى ناتج ضربه في 31 مضافاً إليه الرمز التجزيئي لخاصية ttl. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:171]

```
172:         result = 31 * result + (route?.fold(1) { acc, bytes -> 31 * acc + bytes.contentHashCode() } ?: 0)
```
> يُعيد إسناد result إلى ناتج ضربه في 31 مضافاً إليه طيّ (fold) قائمة route ابتداءً من 1 بحيث يصبح المُجمّع acc مضروباً في 31 مضافاً إليه الرمز التجزيئي لمحتوى كل عنصر bytes، أو 0 إن كانت route تساوي null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:172]

```
173:         return result
```
> يُعيد قيمة result. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:173]

```
174:     }
```
> إغلاق نطاق الدالة hashCode. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:174]

```
175: }
```
> إغلاق نطاق صنف البيانات BitchatPacket. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:175]

```
176: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:176]

```
177: /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:177]

```
178:  * Binary Protocol implementation - supports v1 and v2, backward compatible
```
> تعليق: «تنفيذ البروتوكول الثنائي - يدعم v1 و v2، متوافق رجعياً». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:178]

```
179:  */
```
> تعليق توثيقي: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:179]

```
180: object BinaryProtocol {
```
> يُعرّف كائناً مفرداً (BinaryProtocol / البروتوكول الثنائي) ويفتح جسده. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:180]

```
181:     private const val HEADER_SIZE_V1 = 14
```
> يُعرّف الثابت الخاص (HEADER_SIZE_V1 / حجم ترويسة v1) بالقيمة 14. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:181]

```
182:     private const val HEADER_SIZE_V2 = 16
```
> يُعرّف الثابت الخاص (HEADER_SIZE_V2 / حجم ترويسة v2) بالقيمة 16. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:182]

```
183:     private const val SENDER_ID_SIZE = 8
```
> يُعرّف الثابت الخاص (SENDER_ID_SIZE / حجم معرّف المُرسِل) بالقيمة 8. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:183]

```
184:     private const val RECIPIENT_ID_SIZE = 8
```
> يُعرّف الثابت الخاص (RECIPIENT_ID_SIZE / حجم معرّف المستلِم) بالقيمة 8. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:184]

```
185:     private const val SIGNATURE_SIZE = 64
```
> يُعرّف الثابت الخاص (SIGNATURE_SIZE / حجم التوقيع) بالقيمة 64. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:185]

```
186: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:186]

```
187:     object Flags {
```
> يُعرّف كائناً مفرداً (Flags / الأعلام) داخل BinaryProtocol ويفتح جسده. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:187]

```
188:         const val HAS_RECIPIENT: UByte = 0x01u
```
> يُعرّف الثابت (HAS_RECIPIENT / يوجد مستلِم) من نوع UByte بالقيمة 0x01u. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:188]

```
189:         const val HAS_SIGNATURE: UByte = 0x02u
```
> يُعرّف الثابت (HAS_SIGNATURE / يوجد توقيع) من نوع UByte بالقيمة 0x02u. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:189]

```
190:         const val IS_COMPRESSED: UByte = 0x04u
```
> يُعرّف الثابت (IS_COMPRESSED / مضغوط) من نوع UByte بالقيمة 0x04u. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:190]

```
191:         const val HAS_ROUTE: UByte = 0x08u
```
> يُعرّف الثابت (HAS_ROUTE / يوجد مسار) من نوع UByte بالقيمة 0x08u. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:191]

```
192:     }
```
> إغلاق نطاق الكائن Flags. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:192]

```
193: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:193]

```
194:     private fun getHeaderSize(version: UByte): Int {
```
> يُعرّف دالة خاصة (getHeaderSize / احصل على حجم الترويسة) تأخذ معاملاً version من نوع UByte وتُعيد Int. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:194]

```
195:         return when (version) {
```
> يُعيد ناتج تعبير when الذي يفرّع حسب قيمة version. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:195]

```
196:             1u.toUByte() -> HEADER_SIZE_V1
```
> يُعيد HEADER_SIZE_V1 إذا كانت version تساوي 1u المحوّلة إلى UByte. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:196]

```
197:             else -> HEADER_SIZE_V2  // v2+ will use 4-byte payload length
```
> يُعيد HEADER_SIZE_V2 في الحالات الأخرى، مع تعليق: «v2 فأعلى ستستخدم طول حمولة من 4 بايتات». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:197]

```
198:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:198]

```
199:     }
```
> إغلاق نطاق الدالة getHeaderSize. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:199]

```
200:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:200]

```
201:     fun encode(packet: BitchatPacket, padding: Boolean = true): ByteArray? {
```
> يُعرّف دالة (encode / ترميز) تأخذ معاملاً packet من نوع BitchatPacket ومعاملاً padding من نوع Boolean بقيمة افتراضية true وتُعيد مصفوفة بايتات أو null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:201]

```
202:         try {
```
> يبدأ كتلة try لمعالجة الاستثناءات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:202]

```
203:             // Try to compress payload if beneficial
```
> تعليق: «محاولة ضغط الحمولة إن كان ذلك مفيداً». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:203]

```
204:             var payload = packet.payload
```
> يُعرّف المتغيّر القابل للتغيير (payload / الحمولة) ويُسند إليه payload من packet. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:204]

```
205:             var originalPayloadSize: Int? = null
```
> يُعرّف المتغيّر القابل للتغيير (originalPayloadSize / حجم الحمولة الأصلي) من نوع Int قابل لأن يكون null بقيمة null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:205]

```
206:             var isCompressed = false
```
> يُعرّف المتغيّر القابل للتغيير (isCompressed / مضغوط) ويُسند إليه false. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:206]

```
207:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:207]

```
208:             if (CompressionUtil.shouldCompress(payload)) {
```
> يفحص بنداء الدالة shouldCompress في CompressionUtil ما إذا كان ينبغي ضغط payload. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:208]

```
209:                 CompressionUtil.compress(payload)?.let { compressedPayload ->
```
> يستدعي الدالة compress في CompressionUtil على payload، وإن لم يكن الناتج null ينفّذ كتلة let مسمّياً الناتج compressedPayload. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:209]

```
210:                     originalPayloadSize = payload.size
```
> يُسند حجم payload الحالي إلى المتغيّر originalPayloadSize. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:210]

```
211:                     payload = compressedPayload
```
> يُعيد إسناد payload إلى الحمولة المضغوطة compressedPayload. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:211]

```
212:                     isCompressed = true
```
> يُعيد إسناد isCompressed إلى true. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:212]

```
213:                 }
```
> إغلاق نطاق كتلة let. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:213]

```
214:             }
```
> إغلاق نطاق جملة if الخاصة بفحص الضغط. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:214]

```
215:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:215]

```
216:             // Compute a safe capacity for the unpadded frame
```
> تعليق: «حساب سعة آمنة للإطار غير المبطّن». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:216]

```
217:             val headerSize = getHeaderSize(packet.version)
```
> يُعرّف المتغيّر (headerSize / حجم الترويسة) بنداء getHeaderSize على إصدار packet. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:217]

```
218:             val recipientBytes = if (packet.recipientID != null) RECIPIENT_ID_SIZE else 0
```
> يُعرّف المتغيّر (recipientBytes / بايتات المستلِم) بقيمة RECIPIENT_ID_SIZE إن كان recipientID في packet ليس null وإلا 0. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:218]

```
219:             val signatureBytes = if (packet.signature != null) SIGNATURE_SIZE else 0
```
> يُعرّف المتغيّر (signatureBytes / بايتات التوقيع) بقيمة SIGNATURE_SIZE إن كان signature في packet ليس null وإلا 0. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:219]

```
220:             val sizeFieldBytes = if (isCompressed) (if (packet.version >= 2u.toUByte()) 4 else 2) else 0
```
> يُعرّف المتغيّر (sizeFieldBytes / بايتات حقل الحجم) بقيمة 4 إن كان مضغوطاً وإصدار packet لا يقل عن 2، أو 2 إن كان مضغوطاً وأقل من 2، أو 0 إن لم يكن مضغوطاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:220]

```
221:             val payloadBytes = payload.size + sizeFieldBytes
```
> يُعرّف المتغيّر (payloadBytes / بايتات الحمولة) بمجموع حجم payload و sizeFieldBytes. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:221]

```
222:             val routeBytes = if (!packet.route.isNullOrEmpty() && packet.version >= 2u.toUByte()) {
```
> يُعرّف المتغيّر (routeBytes / بايتات المسار) ويفتح تعبيراً شرطياً ينفّذ إن كان route في packet ليس null ولا فارغاً وإصدار packet لا يقل عن 2. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:222]

```
223:                 1 + (packet.route!!.size.coerceAtMost(255) * SENDER_ID_SIZE)
```
> يُحسب القيمة كـ 1 مضافاً إليها حجم route (محدوداً بحدّ أقصى 255) مضروباً في SENDER_ID_SIZE. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:223]

```
224:             } else 0
```
> يُغلق الفرع الشرطي ويُسند 0 في الحالة الأخرى. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:224]

```
225:             val capacity = headerSize + SENDER_ID_SIZE + recipientBytes + payloadBytes + signatureBytes + routeBytes + 16 // small slack
```
> يُعرّف المتغيّر (capacity / السعة) بمجموع headerSize و SENDER_ID_SIZE و recipientBytes و payloadBytes و signatureBytes و routeBytes و16، مع تعليق: «هامش صغير». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:225]

```
226:             val buffer = ByteBuffer.allocate(capacity.coerceAtLeast(512)).apply { order(ByteOrder.BIG_ENDIAN) }
```
> يُعرّف المتغيّر (buffer / المخزن) بتخصيص ByteBuffer بسعة capacity مرفوعة لحدّ أدنى 512، ويضبط ترتيب بايتاته إلى BIG_ENDIAN عبر apply. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:226]

```
227:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:227]

```
228:             // Header
```
> تعليق: «الترويسة». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:228]

```
229:             buffer.put(packet.version.toByte())
```
> يكتب في المخزن buffer قيمة إصدار packet محوّلة إلى بايت. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:229]

```
230:             buffer.put(packet.type.toByte())
```
> يكتب في المخزن buffer قيمة نوع packet محوّلة إلى بايت. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:230]

```
231:             buffer.put(packet.ttl.toByte())
```
> يكتب في المخزن buffer قيمة ttl الخاصة بـ packet محوّلة إلى بايت. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:231]

```
232:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:232]

```
233:             // Timestamp (8 bytes, big-endian)
```
> تعليق: «الطابع الزمني (8 بايتات، big-endian)». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:233]

```
234:             buffer.putLong(packet.timestamp.toLong())
```
> يكتب في المخزن buffer قيمة timestamp الخاصة بـ packet محوّلة إلى Long (8 بايتات). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:234]

```
235:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:235]

```
236:             // Flags
```
> تعليق: «الأعلام». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:236]

```
237:             var flags: UByte = 0u
```
> يُعرّف المتغيّر القابل للتغيير (flags / الأعلام) من نوع UByte بقيمة 0u. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:237]

```
238:             if (packet.recipientID != null) {
```
> يفحص ما إذا كان recipientID في packet ليس null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:238]

```
239:                 flags = flags or Flags.HAS_RECIPIENT
```
> يضبط بت العلم HAS_RECIPIENT في flags عبر عملية OR ثنائية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:239]

```
240:             }
```
> إغلاق نطاق جملة if الخاصة بـ recipientID. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:240]

```
241:             if (packet.signature != null) {
```
> يفحص ما إذا كان signature في packet ليس null. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:241]

```
242:                 flags = flags or Flags.HAS_SIGNATURE
```
> يضبط بت العلم HAS_SIGNATURE في flags عبر عملية OR ثنائية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:242]

```
243:             }
```
> إغلاق نطاق جملة if الخاصة بـ signature. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:243]

```
244:             if (isCompressed) {
```
> يفحص ما إذا كانت isCompressed تساوي true. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:244]

```
245:                 flags = flags or Flags.IS_COMPRESSED
```
> يضبط بت العلم IS_COMPRESSED في flags عبر عملية OR ثنائية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:245]

```
246:             }
```
> إغلاق نطاق جملة if الخاصة بـ isCompressed. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:246]

```
247:             // HAS_ROUTE is only supported for v2+ packets
```
> تعليق: «العلم HAS_ROUTE مدعوم فقط لحزم v2 فأعلى». [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:247]

```
248:             if (!packet.route.isNullOrEmpty() && packet.version >= 2u.toUByte()) {
```
> يفحص ما إذا كان route في packet ليس null ولا فارغاً وإصدار packet لا يقل عن 2. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:248]

```
249:                 flags = flags or Flags.HAS_ROUTE
```
> يضبط بت العلم HAS_ROUTE في flags عبر عملية OR ثنائية. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:249]

```
250:             }
```
> إغلاق نطاق جملة if الخاصة بـ HAS_ROUTE. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:250]
