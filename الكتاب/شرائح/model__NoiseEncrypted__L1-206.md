# شريحة — app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt (الأسطر 1–206)

```
1: package com.bitchat.android.model
```
> يُعرّف هذا السطر الحزمة (package) باسم `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:2]

```
3: import android.os.Parcelable
```
> يستورد الواجهة (Parcelable) من `android.os` التي تسمح بنقل الكائن بين مكوّنات أندرويد. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:3]

```
4: import kotlinx.parcelize.Parcelize
```
> يستورد التعليق التوضيحي (Parcelize) من `kotlinx.parcelize` الذي يولّد كود التحويل تلقائياً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:5]

```
6: /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:6]

```
7:  * Noise encrypted payload types and handling - 100% compatible with iOS SimplifiedBluetoothService
```
> تعليق: «أنواع الحمولة المشفّرة بنويز ومعالجتها - متوافق ١٠٠٪ مع خدمة البلوتوث المبسّطة في iOS». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:7]

```
8:  * 
```
> تعليق: سطر فارغ داخل كتلة التعليق. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:8]

```
9:  * This handles all encrypted content that goes through noiseEncrypted packets:
```
> تعليق: «هذا يعالج كل المحتوى المشفّر الذي يمرّ عبر حزم noiseEncrypted:». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:9]

```
10:  * - Private messages with TLV encoding
```
> تعليق: «- الرسائل الخاصة بترميز TLV». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:10]

```
11:  * - Delivery acknowledgments
```
> تعليق: «- إيصالات التسليم». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:11]

```
12:  * - Read receipts
```
> تعليق: «- إيصالات القراءة». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:12]

```
13:  * - Future encrypted payload types
```
> تعليق: «- أنواع حمولة مشفّرة مستقبلية». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:13]

```
14:  */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:14]

```
15: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:15]

```
16: /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:16]

```
17:  * Types of payloads embedded within noiseEncrypted messages
```
> تعليق: «أنواع الحمولات المضمّنة داخل رسائل noiseEncrypted». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:17]

```
18:  * Matches iOS NoisePayloadType exactly
```
> تعليق: «يطابق NoisePayloadType في iOS تماماً». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:18]

```
19:  */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:19]

```
20: enum class NoisePayloadType(val value: UByte) {
```
> يُعرّف صنف التعداد (NoisePayloadType) «نوع حمولة نويز» مع خاصيّة `value` من نوع `UByte` (بايت غير مُوقَّع). [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:20]

```
21:     PRIVATE_MESSAGE(0x01u),     // Private chat message with TLV encoding
```
> يُعرّف عضو التعداد `PRIVATE_MESSAGE` «رسالة خاصة» بالقيمة الحرفية `0x01u`؛ تعليق: «رسالة محادثة خاصة بترميز TLV». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:21]

```
22:     READ_RECEIPT(0x02u),        // Message was read
```
> يُعرّف عضو التعداد `READ_RECEIPT` «إيصال قراءة» بالقيمة الحرفية `0x02u`؛ تعليق: «تمّت قراءة الرسالة». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:22]

```
23:     DELIVERED(0x03u),           // Message was delivered
```
> يُعرّف عضو التعداد `DELIVERED` «مُسلَّمة» بالقيمة الحرفية `0x03u`؛ تعليق: «تمّ تسليم الرسالة». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:23]

```
24:     VERIFY_CHALLENGE(0x10u),    // Verification challenge
```
> يُعرّف عضو التعداد `VERIFY_CHALLENGE` «تحدّي تحقّق» بالقيمة الحرفية `0x10u`؛ تعليق: «تحدّي التحقّق». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:24]

```
25:     VERIFY_RESPONSE(0x11u),     // Verification response
```
> يُعرّف عضو التعداد `VERIFY_RESPONSE` «ردّ تحقّق» بالقيمة الحرفية `0x11u`؛ تعليق: «ردّ التحقّق». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:25]

```
26:     FILE_TRANSFER(0x20u);
```
> يُعرّف عضو التعداد `FILE_TRANSFER` «نقل ملف» بالقيمة الحرفية `0x20u`، ثم فاصلة منقوطة تُنهي قائمة أعضاء التعداد. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:28]

```
29:     companion object {
```
> يبدأ تعريف الكائن المرافق (companion object) داخل صنف التعداد. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:29]

```
30:         fun fromValue(value: UByte): NoisePayloadType? {
```
> يُعرّف الدالة (fromValue) «من القيمة» التي تأخذ معامل `value` من نوع `UByte` وتعيد `NoisePayloadType?` (قد يكون فارغاً). [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:30]

```
31:             return values().find { it.value == value }
```
> يعيد أوّل عضو تعداد من `values()` تتساوى خاصيّته `value` مع المعامل `value`، أو فارغاً إن لم يوجد. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:31]

```
32:         }
```
> إغلاق نطاق الدالة `fromValue`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:32]

```
33:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:33]

```
34: }
```
> إغلاق نطاق صنف التعداد `NoisePayloadType`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:34]

```
35: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:35]

```
36: /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:36]

```
37:  * Helper class for creating and parsing Noise payloads
```
> تعليق: «صنف مساعد لإنشاء حمولات نويز وتحليلها». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:37]

```
38:  * Matches iOS NoisePayload helper exactly
```
> تعليق: «يطابق مساعد NoisePayload في iOS تماماً». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:38]

```
39:  */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:39]

```
40: @Parcelize
```
> يضع التعليق التوضيحي `@Parcelize` على الصنف التالي ليولّد كود التحويل القابل للنقل تلقائياً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:40]

```
41: data class NoisePayload(
```
> يُعرّف صنف البيانات (NoisePayload) «حمولة نويز» ويبدأ قائمة معاملاته. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:41]

```
42:     val type: NoisePayloadType,
```
> يُعرّف الخاصيّة `type` «النوع» من نوع `NoisePayloadType`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:42]

```
43:     val data: ByteArray
```
> يُعرّف الخاصيّة `data` «البيانات» من نوع `ByteArray` (مصفوفة بايتات). [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:43]

```
44: ) : Parcelable {
```
> يُنهي قائمة المعاملات ويُعلن أنّ الصنف يُنفّذ الواجهة `Parcelable`، ثم يفتح جسم الصنف. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:44]

```
45: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:45]

```
46:     /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:46]

```
47:      * Encode payload with type prefix - exactly like iOS
```
> تعليق: «ترميز الحمولة ببادئة النوع - تماماً مثل iOS». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:47]

```
48:      * Format: [type_byte][payload_data]
```
> تعليق: «الصيغة: [بايت_النوع][بيانات_الحمولة]». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:48]

```
49:      */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:49]

```
50:     fun encode(): ByteArray {
```
> يُعرّف الدالة (encode) «ترميز» التي لا تأخذ معاملات وتعيد `ByteArray`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:50]

```
51:         val result = ByteArray(1 + data.size)
```
> يُنشئ متغيّراً `result` «النتيجة» كمصفوفة بايتات طولها واحد زائد حجم `data`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:51]

```
52:         result[0] = type.value.toByte()
```
> يضع في الموضع صفر من `result` قيمة `type.value` بعد تحويلها إلى `Byte`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:52]

```
53:         data.copyInto(result, destinationOffset = 1)
```
> ينسخ محتوى `data` داخل `result` ابتداءً من الإزاحة الوجهة `1`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:53]

```
54:         return result
```
> يعيد المصفوفة `result`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:54]

```
55:     }
```
> إغلاق نطاق الدالة `encode`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:55]

```
56: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:56]

```
57:     companion object {
```
> يبدأ تعريف الكائن المرافق داخل صنف `NoisePayload`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:57]

```
58:         /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:58]

```
59:          * Decode payload from data - exactly like iOS
```
> تعليق: «فكّ ترميز الحمولة من البيانات - تماماً مثل iOS». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:59]

```
60:          * Expects: [type_byte][payload_data]
```
> تعليق: «يتوقّع: [بايت_النوع][بيانات_الحمولة]». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:60]

```
61:          */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:61]

```
62:         fun decode(data: ByteArray): NoisePayload? {
```
> يُعرّف الدالة (decode) «فكّ الترميز» التي تأخذ `data` من نوع `ByteArray` وتعيد `NoisePayload?`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:62]

```
63:             if (data.isEmpty()) return null
```
> إن كانت `data` فارغة، يعيد فارغاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:63]

```
64:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:64]

```
65:             val typeValue = data[0].toUByte()
```
> يُنشئ متغيّراً `typeValue` «قيمة النوع» من البايت الأوّل في `data` بعد تحويله إلى `UByte`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:65]

```
66:             val type = NoisePayloadType.fromValue(typeValue) ?: return null
```
> يُنشئ متغيّراً `type` بنتيجة `NoisePayloadType.fromValue(typeValue)`، وإن كانت فارغة يعيد فارغاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:66]

```
67:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:67]

```
68:             // Extract payload data (remaining bytes after type byte)
```
> تعليق: «استخراج بيانات الحمولة (البايتات المتبقّية بعد بايت النوع)». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:68]

```
69:             val payloadData = if (data.size > 1) {
```
> يُنشئ متغيّراً `payloadData` «بيانات الحمولة» بشرط: إن كان حجم `data` أكبر من واحد. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:69]

```
70:                 data.copyOfRange(1, data.size)
```
> في حالة الشرط الصادق، يأخذ نسخة من `data` من الموضع `1` حتى نهايتها. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:70]

```
71:             } else {
```
> بداية فرع «وإلا» للشرط. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:71]

```
72:                 ByteArray(0)
```
> في حالة الشرط الكاذب، ينتج مصفوفة بايتات فارغة طولها صفر. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:72]

```
73:             }
```
> إغلاق نطاق تعبير الشرط `if/else`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:73]

```
74:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:74]

```
75:             return NoisePayload(type, payloadData)
```
> يعيد كائن `NoisePayload` مُنشأً بـ `type` و`payloadData`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:75]

```
76:         }
```
> إغلاق نطاق الدالة `decode`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:76]

```
77:     }
```
> إغلاق نطاق الكائن المرافق لصنف `NoisePayload`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:77]

```
78: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:78]

```
79:     // Override equals and hashCode since we use ByteArray
```
> تعليق: «تجاوز equals و hashCode لأننا نستعمل ByteArray». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:79]

```
80:     override fun equals(other: Any?): Boolean {
```
> يتجاوز الدالة (equals) «يساوي» التي تأخذ معاملاً `other` من نوع `Any?` وتعيد `Boolean`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:80]

```
81:         if (this === other) return true
```
> إن كان هذا الكائن هو نفسه `other` بالمرجع، يعيد صحيحاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:81]

```
82:         if (javaClass != other?.javaClass) return false
```
> إن اختلف الصنف الفعلي عن صنف `other`، يعيد خاطئاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:82]

```
83:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:83]

```
84:         other as NoisePayload
```
> يحوّل `other` تحويلاً صريحاً إلى نوع `NoisePayload`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:84]

```
85: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:85]

```
86:         if (type != other.type) return false
```
> إن اختلفت `type` عن `other.type`، يعيد خاطئاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:86]

```
87:         if (!data.contentEquals(other.data)) return false
```
> إن لم يتطابق محتوى `data` مع محتوى `other.data`، يعيد خاطئاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:87]

```
88:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:88]

```
89:         return true
```
> يعيد صحيحاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:89]

```
90:     }
```
> إغلاق نطاق الدالة `equals`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:90]

```
91: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:91]

```
92:     override fun hashCode(): Int {
```
> يتجاوز الدالة (hashCode) «رمز التجزئة» التي لا تأخذ معاملات وتعيد `Int`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:92]

```
93:         var result = type.hashCode()
```
> يُنشئ متغيّراً متغيّر القيمة `result` بقيمة `type.hashCode()`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:93]

```
94:         result = 31 * result + data.contentHashCode()
```
> يُسند إلى `result` ناتج ضرب `31` في `result` مضافاً إليه `data.contentHashCode()`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:94]

```
95:         return result
```
> يعيد `result`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:95]

```
96:     }
```
> إغلاق نطاق الدالة `hashCode`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:96]

```
97: }
```
> إغلاق نطاق صنف `NoisePayload`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:97]

```
98: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:98]

```
99: /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:99]

```
100:  * Private message packet with TLV encoding - matches iOS PrivateMessagePacket exactly
```
> تعليق: «حزمة رسالة خاصة بترميز TLV - تطابق PrivateMessagePacket في iOS تماماً». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:100]

```
101:  */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:101]

```
102: @Parcelize
```
> يضع التعليق التوضيحي `@Parcelize` على الصنف التالي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:102]

```
103: data class PrivateMessagePacket(
```
> يُعرّف صنف البيانات (PrivateMessagePacket) «حزمة رسالة خاصة» ويبدأ قائمة معاملاته. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:103]

```
104:     val messageID: String,
```
> يُعرّف الخاصيّة `messageID` «معرّف الرسالة» من نوع `String`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:104]

```
105:     val content: String
```
> يُعرّف الخاصيّة `content` «المحتوى» من نوع `String`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:105]

```
106: ) : Parcelable {
```
> يُنهي قائمة المعاملات ويُعلن تنفيذ الواجهة `Parcelable`، ثم يفتح جسم الصنف. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:106]

```
107: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:107]

```
108:     /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:108]

```
109:      * TLV types matching iOS implementation exactly
```
> تعليق: «أنواع TLV تطابق تنفيذ iOS تماماً». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:109]

```
110:      */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:110]

```
111:     private enum class TLVType(val value: UByte) {
```
> يُعرّف صنف التعداد الخاص (TLVType) «نوع TLV» بمُعدِّل الوصول `private` مع خاصيّة `value` من نوع `UByte`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:111]

```
112:         MESSAGE_ID(0x00u),
```
> يُعرّف عضو التعداد `MESSAGE_ID` «معرّف الرسالة» بالقيمة الحرفية `0x00u`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:112]

```
113:         CONTENT(0x01u);
```
> يُعرّف عضو التعداد `CONTENT` «المحتوى» بالقيمة الحرفية `0x01u`، ثم فاصلة منقوطة تُنهي قائمة الأعضاء. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:113]

```
114:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:114]

```
115:         companion object {
```
> يبدأ تعريف الكائن المرافق داخل صنف التعداد `TLVType`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:115]

```
116:             fun fromValue(value: UByte): TLVType? {
```
> يُعرّف الدالة `fromValue` التي تأخذ `value` من نوع `UByte` وتعيد `TLVType?`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:116]

```
117:                 return values().find { it.value == value }
```
> يعيد أوّل عضو من `values()` تتساوى خاصيّته `value` مع المعامل `value`، أو فارغاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:117]

```
118:             }
```
> إغلاق نطاق الدالة `fromValue`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:118]

```
119:         }
```
> إغلاق نطاق الكائن المرافق لصنف `TLVType`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:119]

```
120:     }
```
> إغلاق نطاق صنف التعداد `TLVType`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:120]

```
121: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:121]

```
122:     /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:122]

```
123:      * Encode to TLV binary data - exactly like iOS
```
> تعليق: «ترميز إلى بيانات TLV ثنائية - تماماً مثل iOS». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:123]

```
124:      * Format: [type][length][value] for each field
```
> تعليق: «الصيغة: [نوع][طول][قيمة] لكل حقل». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:124]

```
125:      */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:125]

```
126:     fun encode(): ByteArray? {
```
> يُعرّف الدالة `encode` «ترميز» التي لا تأخذ معاملات وتعيد `ByteArray?`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:126]

```
127:         val messageIDData = messageID.toByteArray(Charsets.UTF_8)
```
> يُنشئ متغيّراً `messageIDData` بتحويل `messageID` إلى مصفوفة بايتات بترميز `UTF_8`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:127]

```
128:         val contentData = content.toByteArray(Charsets.UTF_8)
```
> يُنشئ متغيّراً `contentData` بتحويل `content` إلى مصفوفة بايتات بترميز `UTF_8`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:128]

```
129:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:129]

```
130:         // Check size limits (TLV length field is 1 byte = max 255)
```
> تعليق: «فحص حدود الحجم (حقل طول TLV بايت واحد = أقصى ٢٥٥)». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:130]

```
131:         if (messageIDData.size > 255 || contentData.size > 255) {
```
> إن كان حجم `messageIDData` أكبر من `255` أو حجم `contentData` أكبر من `255`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:131]

```
132:             return null
```
> يعيد فارغاً في حال تحقّق الشرط. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:132]

```
133:         }
```
> إغلاق نطاق جملة الشرط `if`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:133]

```
134:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:134]

```
135:         val result = mutableListOf<Byte>()
```
> يُنشئ متغيّراً `result` كقائمة قابلة للتعديل من نوع `Byte`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:135]

```
136:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:136]

```
137:         // TLV for messageID
```
> تعليق: «TLV لمعرّف الرسالة». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:137]

```
138:         result.add(TLVType.MESSAGE_ID.value.toByte())
```
> يضيف إلى `result` قيمة `TLVType.MESSAGE_ID.value` بعد تحويلها إلى `Byte`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:138]

```
139:         result.add(messageIDData.size.toByte())
```
> يضيف إلى `result` حجم `messageIDData` بعد تحويله إلى `Byte`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:139]

```
140:         result.addAll(messageIDData.toList())
```
> يضيف إلى `result` كل عناصر `messageIDData` بعد تحويلها إلى قائمة. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:140]

```
141:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:141]

```
142:         // TLV for content
```
> تعليق: «TLV للمحتوى». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:142]

```
143:         result.add(TLVType.CONTENT.value.toByte())
```
> يضيف إلى `result` قيمة `TLVType.CONTENT.value` بعد تحويلها إلى `Byte`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:143]

```
144:         result.add(contentData.size.toByte())
```
> يضيف إلى `result` حجم `contentData` بعد تحويله إلى `Byte`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:144]

```
145:         result.addAll(contentData.toList())
```
> يضيف إلى `result` كل عناصر `contentData` بعد تحويلها إلى قائمة. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:145]

```
146:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:146]

```
147:         return result.toByteArray()
```
> يعيد `result` بعد تحويلها إلى مصفوفة بايتات. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:147]

```
148:     }
```
> إغلاق نطاق الدالة `encode`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:148]

```
149:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:149]

```
150:     companion object {
```
> يبدأ تعريف الكائن المرافق داخل صنف `PrivateMessagePacket`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:150]

```
151:         /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:151]

```
152:          * Decode from TLV binary data - exactly like iOS
```
> تعليق: «فكّ الترميز من بيانات TLV ثنائية - تماماً مثل iOS». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:152]

```
153:          */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:153]

```
154:         fun decode(data: ByteArray): PrivateMessagePacket? {
```
> يُعرّف الدالة `decode` «فكّ الترميز» التي تأخذ `data` من نوع `ByteArray` وتعيد `PrivateMessagePacket?`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:154]

```
155:             var offset = 0
```
> يُنشئ متغيّراً متغيّر القيمة `offset` «الإزاحة» بقيمة `0`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:155]

```
156:             var messageID: String? = null
```
> يُنشئ متغيّراً متغيّر القيمة `messageID` من نوع `String?` بقيمة فارغة. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:156]

```
157:             var content: String? = null
```
> يُنشئ متغيّراً متغيّر القيمة `content` من نوع `String?` بقيمة فارغة. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:157]

```
158:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:158]

```
159:             while (offset + 2 <= data.size) {
```
> يبدأ حلقة `while` تستمرّ ما دام `offset` زائد `2` أصغر من أو يساوي حجم `data`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:159]

```
160:                 // Read TLV type
```
> تعليق: «قراءة نوع TLV». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:160]

```
161:                 val typeValue = data[offset].toUByte()
```
> يُنشئ متغيّراً `typeValue` من البايت عند `offset` في `data` بعد تحويله إلى `UByte`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:161]

```
162:                 val type = TLVType.fromValue(typeValue) ?: return null
```
> يُنشئ متغيّراً `type` بنتيجة `TLVType.fromValue(typeValue)`، وإن كانت فارغة يعيد فارغاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:162]

```
163:                 offset += 1
```
> يزيد `offset` بمقدار `1`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:163]

```
164:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:164]

```
165:                 // Read TLV length
```
> تعليق: «قراءة طول TLV». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:165]

```
166:                 val length = data[offset].toUByte().toInt()
```
> يُنشئ متغيّراً `length` «الطول» من البايت عند `offset` بعد تحويله إلى `UByte` ثم إلى `Int`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:166]

```
167:                 offset += 1
```
> يزيد `offset` بمقدار `1`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:167]

```
168:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:168]

```
169:                 // Check bounds
```
> تعليق: «فحص الحدود». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:169]

```
170:                 if (offset + length > data.size) return null
```
> إن كان `offset` زائد `length` أكبر من حجم `data`، يعيد فارغاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:170]

```
171:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:171]

```
172:                 // Read TLV value
```
> تعليق: «قراءة قيمة TLV». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:172]

```
173:                 val value = data.copyOfRange(offset, offset + length)
```
> يُنشئ متغيّراً `value` بنسخة من `data` من الموضع `offset` حتى `offset + length`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:173]

```
174:                 offset += length
```
> يزيد `offset` بمقدار `length`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:174]

```
175:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:175]

```
176:                 when (type) {
```
> يبدأ تعبير `when` يوزّع بحسب قيمة `type`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:176]

```
177:                     TLVType.MESSAGE_ID -> {
```
> حالة `when`: إذا كان `type` يساوي `TLVType.MESSAGE_ID`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:177]

```
178:                         messageID = String(value, Charsets.UTF_8)
```
> يُسند إلى `messageID` نصاً مُنشأً من `value` بترميز `UTF_8`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:178]

```
179:                     }
```
> إغلاق نطاق فرع `MESSAGE_ID`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:179]

```
180:                     TLVType.CONTENT -> {
```
> حالة `when`: إذا كان `type` يساوي `TLVType.CONTENT`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:180]

```
181:                         content = String(value, Charsets.UTF_8)
```
> يُسند إلى `content` نصاً مُنشأً من `value` بترميز `UTF_8`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:181]

```
182:                     }
```
> إغلاق نطاق فرع `CONTENT`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:182]

```
183:                 }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:183]

```
184:             }
```
> إغلاق نطاق حلقة `while`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:184]

```
185:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:185]

```
186:             return if (messageID != null && content != null) {
```
> يعيد بحسب شرط: إن كان `messageID` غير فارغ و`content` غير فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:186]

```
187:                 PrivateMessagePacket(messageID, content)
```
> في حالة الشرط الصادق، يعيد كائن `PrivateMessagePacket` مُنشأً بـ `messageID` و`content`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:187]

```
188:             } else {
```
> بداية فرع «وإلا» للشرط. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:188]

```
189:                 null
```
> في حالة الشرط الكاذب، يعيد فارغاً. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:189]

```
190:             }
```
> إغلاق نطاق تعبير الشرط `if/else`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:190]

```
191:         }
```
> إغلاق نطاق الدالة `decode`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:191]

```
192:     }
```
> إغلاق نطاق الكائن المرافق لصنف `PrivateMessagePacket`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:192]

```
193:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:193]

```
194:     override fun toString(): String {
```
> يتجاوز الدالة (toString) «إلى نص» التي لا تأخذ معاملات وتعيد `String`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:194]

```
195:         return "PrivateMessagePacket(messageID='$messageID', content='${content.take(50)}${if (content.length > 50) "..." else ""}')"
```
> يعيد نصاً يحتوي اسم الصنف و`messageID` وأوّل `50` حرفاً من `content` متبوعةً بـ `...` إن كان طول `content` أكبر من `50` وإلا بسلسلة فارغة. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:195]

```
196:     }
```
> إغلاق نطاق الدالة `toString`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:196]

```
197: }
```
> إغلاق نطاق صنف `PrivateMessagePacket`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:197]

```
198: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:198]

```
199: /**
```
> بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:199]

```
200:  * Read receipt data class for transport compatibility
```
> تعليق: «صنف بيانات إيصال القراءة من أجل توافق النقل». [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:200]

```
201:  */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:201]

```
202: @Parcelize
```
> يضع التعليق التوضيحي `@Parcelize` على الصنف التالي. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:202]

```
203: data class ReadReceipt(
```
> يُعرّف صنف البيانات (ReadReceipt) «إيصال قراءة» ويبدأ قائمة معاملاته. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:203]

```
204:     val originalMessageID: String,
```
> يُعرّف الخاصيّة `originalMessageID` «معرّف الرسالة الأصلية» من نوع `String`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:204]

```
205:     val readerPeerID: String? = null
```
> يُعرّف الخاصيّة `readerPeerID` «معرّف القارئ النِّدّ» من نوع `String?` بقيمة افتراضية فارغة. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:205]

```
206: ) : Parcelable
```
> يُنهي قائمة معاملات `ReadReceipt` ويُعلن أنّ الصنف يُنفّذ الواجهة `Parcelable`. [app/src/main/java/com/bitchat/android/model/NoiseEncrypted.kt:206]
