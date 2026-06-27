# شريحة — app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt (الأسطر 1–145)

```
1: package com.bitchat.android.model
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.model. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:2]

```
3: import android.os.Parcelable
```
> يستورد (import) الواجهة Parcelable من android.os. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:3]

```
4: import kotlinx.parcelize.Parcelize
```
> يستورد المُحلّي (Parcelize) من kotlinx.parcelize. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:4]

```
5: import com.bitchat.android.util.*
```
> يستورد كل العناصر العامة من الحزمة com.bitchat.android.util. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:6]

```
7: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:7]

```
8:  * Identity announcement structure with TLV encoding
```
> تعليق: بنية إعلان الهوية بترميز TLV. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:8]

```
9:  * Compatible with iOS AnnouncementPacket TLV format
```
> تعليق: متوافق مع صيغة TLV الخاصة بـ AnnouncementPacket في iOS. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:9]

```
10:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:10]

```
11: @Parcelize
```
> يضع التعليق التوضيحي (Parcelize) على الصنف لتوليد تنفيذ Parcelable تلقائياً. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:11]

```
12: data class IdentityAnnouncement(
```
> يعرّف صنف البيانات إعلان الهوية (IdentityAnnouncement) مع بداية قائمة معاملاته. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:12]

```
13:     val nickname: String,
```
> يعرّف خاصية اللقب (nickname) من النوع نص (String). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:13]

```
14:     val noisePublicKey: ByteArray,    // Noise static public key (Curve25519.KeyAgreement)
```
> يعرّف خاصية مفتاح نويز العام (noisePublicKey) من النوع مصفوفة بايتات (ByteArray)، وتعليق: مفتاح نويز الساكن العام (Curve25519.KeyAgreement). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:14]

```
15:     val signingPublicKey: ByteArray   // Ed25519 public key for signing
```
> يعرّف خاصية مفتاح التوقيع العام (signingPublicKey) من النوع مصفوفة بايتات (ByteArray)، وتعليق: مفتاح Ed25519 العام للتوقيع. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:15]

```
16: ) : Parcelable {
```
> يغلق قائمة المعاملات ويصرّح بأن الصنف يحقّق الواجهة Parcelable، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:17]

```
18:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:18]

```
19:      * TLV types matching iOS implementation
```
> تعليق: أنواع TLV المطابقة لتنفيذ iOS. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:19]

```
20:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:20]

```
21:     private enum class TLVType(val value: UByte) {
```
> يعرّف صنفاً تعداديّاً خاصّاً نوع TLV (TLVType) له خاصية قيمة (value) من النوع بايت غير موقّع (UByte). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:21]

```
22:         NICKNAME(0x01u),
```
> يعرّف الثابت التعدادي اللقب (NICKNAME) بقيمة 0x01 غير الموقّعة. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:22]

```
23:         NOISE_PUBLIC_KEY(0x02u),
```
> يعرّف الثابت التعدادي مفتاح نويز العام (NOISE_PUBLIC_KEY) بقيمة 0x02 غير الموقّعة. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:23]

```
24:         SIGNING_PUBLIC_KEY(0x03u);  // NEW: Ed25519 signing public key
```
> يعرّف الثابت التعدادي مفتاح التوقيع العام (SIGNING_PUBLIC_KEY) بقيمة 0x03 غير الموقّعة وينهي قائمة الثوابت بفاصلة منقوطة، وتعليق: جديد: مفتاح Ed25519 العام للتوقيع. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:24]

```
25:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:25]

```
26:         companion object {
```
> يفتح كائناً مرافقاً (companion object) داخل الصنف التعدادي. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:26]

```
27:             fun fromValue(value: UByte): TLVType? {
```
> يعرّف الدالة من القيمة (fromValue) التي تأخذ قيمة (value) من النوع بايت غير موقّع وتُعيد نوع TLV قابلاً للعدم (TLVType?). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:27]

```
28:                 return values().find { it.value == value }
```
> يُعيد أوّل ثابت تعدادي من قائمة القيم (values) تساوي خاصيته value القيمة المُمرّرة، أو لا شيء إن لم يوجد. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:28]

```
29:             }
```
> إغلاق نطاق الدالة fromValue. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:29]

```
30:         }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:30]

```
31:     }
```
> إغلاق نطاق الصنف التعدادي TLVType. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:31]

```
32: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:32]

```
33:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:33]

```
34:      * Encode to TLV binary data matching iOS implementation
```
> تعليق: التشفير إلى بيانات ثنائية بصيغة TLV المطابقة لتنفيذ iOS. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:34]

```
35:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:35]

```
36:     fun encode(): ByteArray? {
```
> يعرّف الدالة الترميز (encode) التي لا تأخذ معاملات وتُعيد مصفوفة بايتات قابلة للعدم (ByteArray?). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:36]

```
37:         val nicknameData = nickname.toByteArray(Charsets.UTF_8)
```
> يعرّف المتغيّر بيانات اللقب (nicknameData) ويسند إليه تحويل اللقب إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:37]

```
38:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:38]

```
39:         // Check size limits
```
> تعليق: التحقق من حدود الحجم. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:39]

```
40:         if (nicknameData.size > 255 || noisePublicKey.size > 255 || signingPublicKey.size > 255) {
```
> يتحقّق إن كان حجم بيانات اللقب أو مفتاح نويز العام أو مفتاح التوقيع العام يتجاوز 255، ويفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:40]

```
41:             return null
```
> يُعيد لا شيء (null) عند تحقّق الشرط. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:41]

```
42:         }
```
> إغلاق نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:42]

```
43:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:43]

```
44:         val result = mutableListOf<Byte>()
```
> يعرّف المتغيّر النتيجة (result) ويسند إليه قائمة بايتات قابلة للتعديل فارغة. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:44]

```
45:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:45]

```
46:         // TLV for nickname
```
> تعليق: TLV الخاص باللقب. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:46]

```
47:         result.add(TLVType.NICKNAME.value.toByte())
```
> يضيف إلى النتيجة قيمة الثابت NICKNAME محوّلة إلى بايت (وسم النوع). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:47]

```
48:         result.add(nicknameData.size.toByte())
```
> يضيف إلى النتيجة حجم بيانات اللقب محوّلاً إلى بايت (الطول). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:48]

```
49:         result.addAll(nicknameData.toList())
```
> يضيف إلى النتيجة كل بايتات بيانات اللقب محوّلة إلى قائمة (القيمة). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:49]

```
50:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:50]

```
51:         // TLV for noise public key
```
> تعليق: TLV الخاص بمفتاح نويز العام. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:51]

```
52:         result.add(TLVType.NOISE_PUBLIC_KEY.value.toByte())
```
> يضيف إلى النتيجة قيمة الثابت NOISE_PUBLIC_KEY محوّلة إلى بايت (وسم النوع). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:52]

```
53:         result.add(noisePublicKey.size.toByte())
```
> يضيف إلى النتيجة حجم مفتاح نويز العام محوّلاً إلى بايت (الطول). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:53]

```
54:         result.addAll(noisePublicKey.toList())
```
> يضيف إلى النتيجة كل بايتات مفتاح نويز العام محوّلة إلى قائمة (القيمة). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:54]

```
55:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:55]

```
56:         // TLV for signing public key
```
> تعليق: TLV الخاص بمفتاح التوقيع العام. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:56]

```
57:         result.add(TLVType.SIGNING_PUBLIC_KEY.value.toByte())
```
> يضيف إلى النتيجة قيمة الثابت SIGNING_PUBLIC_KEY محوّلة إلى بايت (وسم النوع). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:57]

```
58:         result.add(signingPublicKey.size.toByte())
```
> يضيف إلى النتيجة حجم مفتاح التوقيع العام محوّلاً إلى بايت (الطول). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:58]

```
59:         result.addAll(signingPublicKey.toList())
```
> يضيف إلى النتيجة كل بايتات مفتاح التوقيع العام محوّلة إلى قائمة (القيمة). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:59]

```
60:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:60]

```
61:         return result.toByteArray()
```
> يُعيد النتيجة محوّلة إلى مصفوفة بايتات. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:61]

```
62:     }
```
> إغلاق نطاق الدالة encode. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:62]

```
63:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:63]

```
64:     companion object {
```
> يفتح كائناً مرافقاً (companion object) داخل الصنف IdentityAnnouncement. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:64]

```
65:         /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:65]

```
66:          * Decode from TLV binary data matching iOS implementation
```
> تعليق: فك التشفير من بيانات TLV الثنائية المطابقة لتنفيذ iOS. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:66]

```
67:          */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:67]

```
68:         fun decode(data: ByteArray): IdentityAnnouncement? {
```
> يعرّف الدالة فك التشفير (decode) التي تأخذ بيانات (data) من النوع مصفوفة بايتات وتُعيد إعلان هوية قابلاً للعدم (IdentityAnnouncement?). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:68]

```
69:             // Create defensive copy
```
> تعليق: إنشاء نسخة دفاعية. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:69]

```
70:             val dataCopy = data.copyOf()
```
> يعرّف المتغيّر نسخة البيانات (dataCopy) ويسند إليه نسخة من مصفوفة البيانات. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:70]

```
71: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:71]

```
72:             var offset = 0
```
> يعرّف المتغيّر المتغيّر الإزاحة (offset) ويسند إليه القيمة 0. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:72]

```
73:             var nickname: String? = null
```
> يعرّف المتغيّر المتغيّر اللقب (nickname) من النوع نص قابل للعدم ويسند إليه لا شيء. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:73]

```
74:             var noisePublicKey: ByteArray? = null
```
> يعرّف المتغيّر المتغيّر مفتاح نويز العام (noisePublicKey) من النوع مصفوفة بايتات قابلة للعدم ويسند إليه لا شيء. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:74]

```
75:             var signingPublicKey: ByteArray? = null
```
> يعرّف المتغيّر المتغيّر مفتاح التوقيع العام (signingPublicKey) من النوع مصفوفة بايتات قابلة للعدم ويسند إليه لا شيء. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:75]

```
76:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:76]

```
77:             while (offset + 2 <= dataCopy.size) {
```
> يفتح حلقة طالما (while) تستمر ما دام مجموع الإزاحة واثنين أقل من أو يساوي حجم نسخة البيانات. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:77]

```
78:                 // Read TLV type
```
> تعليق: قراءة نوع TLV. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:78]

```
79:                 val typeValue = dataCopy[offset].toUByte()
```
> يعرّف المتغيّر قيمة النوع (typeValue) ويسند إليه البايت عند الإزاحة محوّلاً إلى بايت غير موقّع. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:79]

```
80:                 val type = TLVType.fromValue(typeValue)
```
> يعرّف المتغيّر النوع (type) ويسند إليه ناتج استدعاء fromValue على قيمة النوع. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:80]

```
81:                 offset += 1
```
> يزيد الإزاحة بمقدار واحد. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:81]

```
82:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:82]

```
83:                 // Read TLV length
```
> تعليق: قراءة طول TLV. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:83]

```
84:                 val length = dataCopy[offset].toUByte().toInt()
```
> يعرّف المتغيّر الطول (length) ويسند إليه البايت عند الإزاحة محوّلاً إلى بايت غير موقّع ثم إلى عدد صحيح. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:84]

```
85:                 offset += 1
```
> يزيد الإزاحة بمقدار واحد. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:85]

```
86:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:86]

```
87:                 // Check bounds
```
> تعليق: التحقق من الحدود. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:87]

```
88:                 if (offset + length > dataCopy.size) return null
```
> يتحقّق إن كان مجموع الإزاحة والطول يتجاوز حجم نسخة البيانات، فيُعيد لا شيء عندئذٍ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:88]

```
89:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:89]

```
90:                 // Read TLV value
```
> تعليق: قراءة قيمة TLV. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:90]

```
91:                 val value = dataCopy.sliceArray(offset until offset + length)
```
> يعرّف المتغيّر القيمة (value) ويسند إليه شريحة من نسخة البيانات من الإزاحة حتى الإزاحة زائد الطول (غير شامل). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:91]

```
92:                 offset += length
```
> يزيد الإزاحة بمقدار الطول. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:92]

```
93:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:93]

```
94:                 // Process known TLV types, skip unknown ones for forward compatibility
```
> تعليق: معالجة أنواع TLV المعروفة، وتخطّي غير المعروفة لأجل التوافق المستقبلي. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:94]

```
95:                 when (type) {
```
> يفتح تعبير المطابقة (when) على النوع. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:95]

```
96:                     TLVType.NICKNAME -> {
```
> يفتح فرع المطابقة على الثابت NICKNAME. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:96]

```
97:                         nickname = String(value, Charsets.UTF_8)
```
> يسند إلى المتغيّر اللقب نصاً مبنيّاً من القيمة بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:97]

```
98:                     }
```
> إغلاق نطاق فرع NICKNAME. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:98]

```
99:                     TLVType.NOISE_PUBLIC_KEY -> {
```
> يفتح فرع المطابقة على الثابت NOISE_PUBLIC_KEY. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:99]

```
100:                         noisePublicKey = value
```
> يسند إلى المتغيّر مفتاح نويز العام القيمة. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:100]

```
101:                     }
```
> إغلاق نطاق فرع NOISE_PUBLIC_KEY. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:101]

```
102:                     TLVType.SIGNING_PUBLIC_KEY -> {
```
> يفتح فرع المطابقة على الثابت SIGNING_PUBLIC_KEY. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:102]

```
103:                         signingPublicKey = value
```
> يسند إلى المتغيّر مفتاح التوقيع العام القيمة. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:103]

```
104:                     }
```
> إغلاق نطاق فرع SIGNING_PUBLIC_KEY. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:104]

```
105:                     null -> {
```
> يفتح فرع المطابقة على القيمة لا شيء (null). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:105]

```
106:                         // Unknown TLV; skip (tolerant decoder for forward compatibility)
```
> تعليق: TLV غير معروف؛ يُتخطّى (مفكّك متسامح لأجل التوافق المستقبلي). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:106]

```
107:                         continue
```
> ينتقل إلى التكرار التالي من الحلقة. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:107]

```
108:                     }
```
> إغلاق نطاق فرع null. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:108]

```
109:                 }
```
> إغلاق نطاق تعبير المطابقة when. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:109]

```
110:             }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:110]

```
111:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:111]

```
112:             // All three fields are required
```
> تعليق: الحقول الثلاثة كلها مطلوبة. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:112]

```
113:             return if (nickname != null && noisePublicKey != null && signingPublicKey != null) {
```
> يُعيد قيمة تعبير الشرط: إن كان اللقب ومفتاح نويز العام ومفتاح التوقيع العام كلها غير معدومة، يفتح كتلة الشرط الموجبة. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:113]

```
114:                 IdentityAnnouncement(nickname, noisePublicKey, signingPublicKey)
```
> ينشئ كائن إعلان هوية باللقب ومفتاح نويز العام ومفتاح التوقيع العام كقيمة الفرع الموجب. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:114]

```
115:             } else {
```
> يغلق الفرع الموجب ويفتح الفرع البديل (else). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:115]

```
116:                 null
```
> يجعل قيمة الفرع البديل لا شيء (null). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:116]

```
117:             }
```
> إغلاق نطاق الفرع البديل. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:117]

```
118:         }
```
> إغلاق نطاق الدالة decode. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:118]

```
119:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:119]

```
120:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:120]

```
121:     // Override equals and hashCode since we use ByteArray
```
> تعليق: إعادة تعريف equals وhashCode لأننا نستعمل ByteArray. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:121]

```
122:     override fun equals(other: Any?): Boolean {
```
> يعيد تعريف الدالة المساواة (equals) التي تأخذ آخر (other) من النوع أيّ قابل للعدم وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:122]

```
123:         if (this === other) return true
```
> يتحقّق إن كان هذا الكائن هو نفسه المرجع other، فيُعيد صحيح عندئذٍ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:123]

```
124:         if (javaClass != other?.javaClass) return false
```
> يتحقّق إن كان صنف هذا الكائن مختلفاً عن صنف other، فيُعيد خطأ عندئذٍ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:124]

```
125:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:125]

```
126:         other as IdentityAnnouncement
```
> يحوّل other قسريّاً إلى النوع إعلان هوية (IdentityAnnouncement). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:126]

```
127:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:127]

```
128:         if (nickname != other.nickname) return false
```
> يتحقّق إن كان لقب هذا الكائن مختلفاً عن لقب other، فيُعيد خطأ عندئذٍ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:128]

```
129:         if (!noisePublicKey.contentEquals(other.noisePublicKey)) return false
```
> يتحقّق إن كان محتوى مفتاح نويز العام غير مساوٍ لمحتوى مفتاح نويز العام في other، فيُعيد خطأ عندئذٍ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:129]

```
130:         if (!signingPublicKey.contentEquals(other.signingPublicKey)) return false
```
> يتحقّق إن كان محتوى مفتاح التوقيع العام غير مساوٍ لمحتوى مفتاح التوقيع العام في other، فيُعيد خطأ عندئذٍ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:130]

```
131:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:131]

```
132:         return true
```
> يُعيد صحيح (تساوي الكائنين). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:132]

```
133:     }
```
> إغلاق نطاق الدالة equals. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:133]

```
134:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:134]

```
135:     override fun hashCode(): Int {
```
> يعيد تعريف الدالة الرمز التجزيئي (hashCode) التي لا تأخذ معاملات وتُعيد عدداً صحيحاً (Int). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:135]

```
136:         var result = nickname.hashCode()
```
> يعرّف المتغيّر النتيجة (result) ويسند إليه الرمز التجزيئي للقب. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:136]

```
137:         result = 31 * result + noisePublicKey.contentHashCode()
```
> يسند إلى النتيجة حاصل ضرب 31 في النتيجة زائد الرمز التجزيئي لمحتوى مفتاح نويز العام. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:137]

```
138:         result = 31 * result + signingPublicKey.contentHashCode()
```
> يسند إلى النتيجة حاصل ضرب 31 في النتيجة زائد الرمز التجزيئي لمحتوى مفتاح التوقيع العام. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:138]

```
139:         return result
```
> يُعيد النتيجة. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:139]

```
140:     }
```
> إغلاق نطاق الدالة hashCode. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:140]

```
141:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:141]

```
142:     override fun toString(): String {
```
> يعيد تعريف الدالة التحويل إلى نص (toString) التي لا تأخذ معاملات وتُعيد نصاً (String). [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:142]

```
143:         return "IdentityAnnouncement(nickname='$nickname', noisePublicKey=${noisePublicKey.joinToString("") { "%02x".format(it) }.take(16)}..., signingPublicKey=${signingPublicKey.joinToString("") { "%02x".format(it) }.take(16)}...)"
```
> يُعيد نصاً يحوي اللقب وأوّل ١٦ محرفاً من تمثيل مفتاح نويز العام بالنظام السادس عشري وأوّل ١٦ محرفاً من تمثيل مفتاح التوقيع العام بالنظام السادس عشري، كلٌّ متبوع بثلاث نقاط. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:143]

```
144:     }
```
> إغلاق نطاق الدالة toString. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:144]

```
145: }
```
> إغلاق نطاق الصنف IdentityAnnouncement. [app/src/main/java/com/bitchat/android/model/IdentityAnnouncement.kt:145]
