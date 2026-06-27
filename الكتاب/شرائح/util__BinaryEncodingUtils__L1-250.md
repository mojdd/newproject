# شريحة — app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt (الأسطر 1–250)

```
1: package com.bitchat.android.util
```
> يُعرّف هذا السطر اسم الحزمة (package) التي ينتمي إليها الملف وهو com.bitchat.android.util. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:2]

```
3: import java.nio.ByteBuffer
```
> يستورد هذا السطر الصنف ByteBuffer من حزمة java.nio. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:3]

```
4: import java.nio.ByteOrder
```
> يستورد هذا السطر الصنف ByteOrder من حزمة java.nio. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:4]

```
5: import java.util.*
```
> يستورد هذا السطر جميع الأنواع من حزمة java.util بالنجمة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:6]

```
7: /**
```
> بداية تعليق توثيقي بصيغة KDoc. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:7]

```
8:  * Binary encoding utilities for efficient protocol messages
```
> تعليق: «أدوات ترميز ثنائي لرسائل بروتوكول فعّالة». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:8]

```
9:  * Compatible with iOS version BinaryEncodingUtils.swift
```
> تعليق: «متوافق مع نسخة iOS الملف BinaryEncodingUtils.swift». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:9]

```
10:  */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:11]

```
12: // MARK: - Hex Encoding/Decoding Extensions
```
> تعليق: «علامة قسم: امتدادات ترميز/فك ترميز سداسي عشري». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:12]

```
13: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:13]

```
14: fun ByteArray.hexEncodedString(): String {
```
> يُعرّف دالة امتداد (hexEncodedString) للنوع ByteArray تُعيد قيمة من نوع String. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:14]

```
15:     if (this.isEmpty()) {
```
> يفحص ما إذا كان المصفوفة الحالية (this) فارغة باستدعاء isEmpty. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:15]

```
16:         return ""
```
> يُعيد سلسلة نصية فارغة في حال كانت المصفوفة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:16]

```
17:     }
```
> إغلاق نطاق جملة الشرط if. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:17]

```
18:     return this.joinToString("") { "%02x".format(it) }
```
> يُعيد ناتج دمج عناصر المصفوفة في سلسلة بفاصل فارغ مع تنسيق كل بايت (it) إلى رقمين سداسيين عشريين بالصيغة "%02x". [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:18]

```
19: }
```
> إغلاق نطاق دالة الترميز السداسي (hexEncodedString). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:19]

```
20: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:20]

```
21: fun String.dataFromHexString(): ByteArray? {
```
> يُعرّف دالة امتداد (dataFromHexString) للنوع String تُعيد قيمة من نوع ByteArray قابلة للعدم. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:21]

```
22:     val len = this.length / 2
```
> يُعرّف متغيّراً ثابتاً (len) يساوي طول السلسلة مقسوماً على اثنين. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:22]

```
23:     val data = ByteArray(len)
```
> يُعرّف متغيّراً ثابتاً (data) كمصفوفة بايتات بطول len. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:23]

```
24:     var index = 0
```
> يُعرّف متغيّراً متغيّر القيمة (index) ويهيّئه بالقيمة صفر. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:24]

```
25:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:25]

```
26:     for (i in 0 until len) {
```
> يبدأ حلقة تكرار بالمتغيّر i من صفر حتى len غير شامل. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:26]

```
27:         val hexByte = this.substring(i * 2, i * 2 + 2)
```
> يُعرّف متغيّراً ثابتاً (hexByte) كقطعة فرعية من السلسلة من الموضع i*2 إلى الموضع i*2+2. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:27]

```
28:         val byte = hexByte.toIntOrNull(16)?.toByte() ?: return null
```
> يُعرّف متغيّراً ثابتاً (byte) بتحويل hexByte إلى عدد صحيح بالأساس 16 ثم إلى بايت، وإن فشل التحويل يُعيد عدماً. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:28]

```
29:         data[index++] = byte
```
> يُسند قيمة byte إلى عنصر المصفوفة data عند الموضع index ثم يزيد index بواحد. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:29]

```
30:     }
```
> إغلاق نطاق حلقة التكرار for. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:30]

```
31:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:31]

```
32:     return data
```
> يُعيد مصفوفة البايتات data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:32]

```
33: }
```
> إغلاق نطاق دالة التحويل من سداسي (dataFromHexString). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:33]

```
34: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:34]

```
35: // MARK: - Binary Encoding Utilities
```
> تعليق: «علامة قسم: أدوات الترميز الثنائي». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:36]

```
37: class BinaryDataBuilder {
```
> يُعرّف صنفاً (BinaryDataBuilder) أي باني البيانات الثنائية. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:37]

```
38:     private val _buffer = mutableListOf<Byte>()
```
> يُعرّف متغيّراً ثابتاً خاصاً (_buffer) كقائمة قابلة للتغيير من بايتات وتُهيّأ فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:38]

```
39:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:39]

```
40:     // Make buffer accessible for direct manipulation when needed
```
> تعليق: «جعل المخزن المؤقت متاحاً للتعديل المباشر عند الحاجة». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:40]

```
41:     val buffer: MutableList<Byte> get() = _buffer
```
> يُعرّف خاصية ثابتة (buffer) من نوع قائمة بايتات قابلة للتغيير، وجالبها (getter) يُعيد _buffer. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:41]

```
42:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:42]

```
43:     // MARK: Writing
```
> تعليق: «علامة قسم: الكتابة». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:43]

```
44:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:44]

```
45:     fun appendUInt8(value: UByte) {
```
> يُعرّف دالة (appendUInt8) أي إلحاق عدد صحيح غير موقّع 8-بِت، تأخذ معاملاً value من نوع UByte. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:45]

```
46:         buffer.add(value.toByte())
```
> يضيف إلى buffer قيمة value بعد تحويلها إلى بايت. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:46]

```
47:     }
```
> إغلاق نطاق دالة الإلحاق ثماني-بِت (appendUInt8). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:47]

```
48:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:48]

```
49:     fun appendUInt16(value: UShort) {
```
> يُعرّف دالة (appendUInt16) أي إلحاق عدد صحيح غير موقّع 16-بِت، تأخذ معاملاً value من نوع UShort. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:49]

```
50:         buffer.add(((value.toInt() shr 8) and 0xFF).toByte())
```
> يضيف إلى buffer البايت الأعلى بإزاحة value إلى اليمين 8 بتات ثم تطبيق قناع 0xFF وتحويل الناتج إلى بايت. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:50]

```
51:         buffer.add((value.toInt() and 0xFF).toByte())
```
> يضيف إلى buffer البايت الأدنى بتطبيق قناع 0xFF على value وتحويل الناتج إلى بايت. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:51]

```
52:     }
```
> إغلاق نطاق دالة الإلحاق ستة-عشر-بِت (appendUInt16). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:52]

```
53:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:53]

```
54:     fun appendUInt32(value: UInt) {
```
> يُعرّف دالة (appendUInt32) أي إلحاق عدد صحيح غير موقّع 32-بِت، تأخذ معاملاً value من نوع UInt. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:54]

```
55:         buffer.add(((value.toLong() shr 24) and 0xFF).toByte())
```
> يضيف إلى buffer البايت الأول بإزاحة value إلى اليمين 24 بِت وتطبيق قناع 0xFF وتحويل الناتج إلى بايت. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:55]

```
56:         buffer.add(((value.toLong() shr 16) and 0xFF).toByte())
```
> يضيف إلى buffer البايت الثاني بإزاحة value إلى اليمين 16 بِت وتطبيق قناع 0xFF وتحويل الناتج إلى بايت. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:56]

```
57:         buffer.add(((value.toLong() shr 8) and 0xFF).toByte())
```
> يضيف إلى buffer البايت الثالث بإزاحة value إلى اليمين 8 بتات وتطبيق قناع 0xFF وتحويل الناتج إلى بايت. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:57]

```
58:         buffer.add((value.toLong() and 0xFF).toByte())
```
> يضيف إلى buffer البايت الرابع بتطبيق قناع 0xFF على value وتحويل الناتج إلى بايت. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:58]

```
59:     }
```
> إغلاق نطاق دالة الإلحاق اثنان-وثلاثون-بِت (appendUInt32). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:59]

```
60:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:60]

```
61:     fun appendUInt64(value: ULong) {
```
> يُعرّف دالة (appendUInt64) أي إلحاق عدد صحيح غير موقّع 64-بِت، تأخذ معاملاً value من نوع ULong. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:61]

```
62:         for (i in 7 downTo 0) {
```
> يبدأ حلقة تكرار بالمتغيّر i من 7 تنازلياً حتى 0 شاملاً. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:62]

```
63:             buffer.add(((value.toLong() shr (i * 8)) and 0xFF).toByte())
```
> يضيف إلى buffer البايت الناتج من إزاحة value إلى اليمين بمقدار i*8 بِت وتطبيق قناع 0xFF وتحويله إلى بايت. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:63]

```
64:         }
```
> إغلاق نطاق حلقة التكرار for. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:64]

```
65:     }
```
> إغلاق نطاق دالة الإلحاق أربعة-وستون-بِت (appendUInt64). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:65]

```
66:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:66]

```
67:     fun appendString(string: String, maxLength: Int = 255) {
```
> يُعرّف دالة (appendString) أي إلحاق سلسلة نصية، تأخذ معاملاً string من نوع String ومعاملاً maxLength من نوع Int بقيمة افتراضية 255. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:67]

```
68:         val data = string.toByteArray(Charsets.UTF_8)
```
> يُعرّف متغيّراً ثابتاً (data) بتحويل string إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:68]

```
69:         val length = minOf(data.size, maxLength)
```
> يُعرّف متغيّراً ثابتاً (length) يساوي الأصغر بين حجم data وقيمة maxLength. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:69]

```
70:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:70]

```
71:         if (maxLength <= 255) {
```
> يفحص ما إذا كان maxLength أصغر من أو يساوي 255. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:71]

```
72:             buffer.add(length.toByte())
```
> يضيف إلى buffer قيمة length بعد تحويلها إلى بايت واحد. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:72]

```
73:         } else {
```
> بداية الفرع البديل (else) للشرط. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:73]

```
74:             appendUInt16(length.toUShort())
```
> يستدعي appendUInt16 لإلحاق length بعد تحويلها إلى UShort. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:74]

```
75:         }
```
> إغلاق نطاق جملة الشرط if/else. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:75]

```
76:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:76]

```
77:         buffer.addAll(data.take(length).toList())
```
> يضيف إلى buffer جميع أول length عنصراً من data بعد تحويلها إلى قائمة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:77]

```
78:     }
```
> إغلاق نطاق دالة إلحاق السلسلة (appendString). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:78]

```
79:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:79]

```
80:     fun appendData(data: ByteArray, maxLength: Int = 65535) {
```
> يُعرّف دالة (appendData) أي إلحاق بيانات، تأخذ معاملاً data من نوع ByteArray ومعاملاً maxLength من نوع Int بقيمة افتراضية 65535. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:80]

```
81:         val length = minOf(data.size, maxLength)
```
> يُعرّف متغيّراً ثابتاً (length) يساوي الأصغر بين حجم data وقيمة maxLength. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:81]

```
82:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:82]

```
83:         if (maxLength <= 255) {
```
> يفحص ما إذا كان maxLength أصغر من أو يساوي 255. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:83]

```
84:             buffer.add(length.toByte())
```
> يضيف إلى buffer قيمة length بعد تحويلها إلى بايت واحد. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:84]

```
85:         } else {
```
> بداية الفرع البديل (else) للشرط. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:85]

```
86:             appendUInt16(length.toUShort())
```
> يستدعي appendUInt16 لإلحاق length بعد تحويلها إلى UShort. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:86]

```
87:         }
```
> إغلاق نطاق جملة الشرط if/else. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:87]

```
88:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:88]

```
89:         buffer.addAll(data.take(length).toList())
```
> يضيف إلى buffer جميع أول length عنصراً من data بعد تحويلها إلى قائمة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:89]

```
90:     }
```
> إغلاق نطاق دالة إلحاق البيانات (appendData). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:90]

```
91:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:91]

```
92:     fun appendDate(date: Date) {
```
> يُعرّف دالة (appendDate) أي إلحاق تاريخ، تأخذ معاملاً date من نوع Date. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:92]

```
93:         val timestamp = (date.time).toULong() // milliseconds
```
> يُعرّف متغيّراً ثابتاً (timestamp) بتحويل خاصية time للتاريخ إلى ULong، مع تعليق: «أجزاء من الألف من الثانية». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:93]

```
94:         appendUInt64(timestamp)
```
> يستدعي appendUInt64 لإلحاق timestamp. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:94]

```
95:     }
```
> إغلاق نطاق دالة إلحاق التاريخ (appendDate). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:95]

```
96:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:96]

```
97:     fun appendUUID(uuid: String) {
```
> يُعرّف دالة (appendUUID) أي إلحاق معرّف فريد عالمي، تأخذ معاملاً uuid من نوع String. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:97]

```
98:         // Convert UUID string to 16 bytes
```
> تعليق: «تحويل سلسلة المعرّف الفريد إلى 16 بايت». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:98]

```
99:         val uuidData = ByteArray(16)
```
> يُعرّف متغيّراً ثابتاً (uuidData) كمصفوفة بايتات بطول 16. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:99]

```
100:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:100]

```
101:         val cleanUUID = uuid.replace("-", "")
```
> يُعرّف متغيّراً ثابتاً (cleanUUID) بإزالة جميع الشرطات "-" من uuid. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:101]

```
102:         var index = 0
```
> يُعرّف متغيّراً متغيّر القيمة (index) ويهيّئه بالقيمة صفر. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:102]

```
103:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:103]

```
104:         for (i in 0 until 16) {
```
> يبدأ حلقة تكرار بالمتغيّر i من صفر حتى 16 غير شامل. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:104]

```
105:             if (index + 1 < cleanUUID.length) {
```
> يفحص ما إذا كان index زائد واحد أصغر من طول cleanUUID. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:105]

```
106:                 val hexByte = cleanUUID.substring(index, index + 2)
```
> يُعرّف متغيّراً ثابتاً (hexByte) كقطعة فرعية من cleanUUID من الموضع index إلى index+2. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:106]

```
107:                 uuidData[i] = hexByte.toIntOrNull(16)?.toByte() ?: 0
```
> يُسند إلى uuidData عند الموضع i ناتج تحويل hexByte إلى عدد صحيح بالأساس 16 ثم إلى بايت، وإن فشل التحويل فالقيمة صفر. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:107]

```
108:                 index += 2
```
> يزيد قيمة index بمقدار اثنين. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:108]

```
109:             }
```
> إغلاق نطاق جملة الشرط if الداخلية. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:109]

```
110:         }
```
> إغلاق نطاق حلقة التكرار for. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:110]

```
111:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:111]

```
112:         buffer.addAll(uuidData.toList())
```
> يضيف إلى buffer جميع عناصر uuidData بعد تحويلها إلى قائمة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:112]

```
113:     }
```
> إغلاق نطاق دالة إلحاق المعرّف الفريد (appendUUID). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:113]

```
114:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:114]

```
115:     fun toByteArray(): ByteArray {
```
> يُعرّف دالة (toByteArray) أي التحويل إلى مصفوفة بايتات، تُعيد قيمة من نوع ByteArray. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:115]

```
116:         return buffer.toByteArray()
```
> يُعيد buffer بعد تحويله إلى مصفوفة بايتات. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:116]

```
117:     }
```
> إغلاق نطاق دالة التحويل إلى مصفوفة (toByteArray). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:117]

```
118: }
```
> إغلاق نطاق صنف باني البيانات الثنائية (BinaryDataBuilder). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:118]

```
119: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:119]

```
120: // MARK: - Binary Data Reading Extensions
```
> تعليق: «علامة قسم: امتدادات قراءة البيانات الثنائية». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:120]

```
121: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:121]

```
122: class BinaryDataReader(private val data: ByteArray) {
```
> يُعرّف صنفاً (BinaryDataReader) أي قارئ البيانات الثنائية، بمعامل مُنشئ خاص ثابت data من نوع ByteArray. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:122]

```
123:     private var offset = 0
```
> يُعرّف متغيّراً خاصاً متغيّر القيمة (offset) ويهيّئه بالقيمة صفر. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:123]

```
124:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:124]

```
125:     // MARK: Reading
```
> تعليق: «علامة قسم: القراءة». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:125]

```
126:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:126]

```
127:     fun readUInt8(): UByte? {
```
> يُعرّف دالة (readUInt8) أي قراءة عدد صحيح غير موقّع 8-بِت، تُعيد قيمة من نوع UByte قابلة للعدم. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:127]

```
128:         if (offset >= data.size) return null
```
> يُعيد عدماً إذا كان offset أكبر من أو يساوي حجم data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:128]

```
129:         val value = data[offset].toUByte()
```
> يُعرّف متغيّراً ثابتاً (value) بقيمة البايت عند الموضع offset بعد تحويله إلى UByte. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:129]

```
130:         offset += 1
```
> يزيد قيمة offset بمقدار واحد. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:130]

```
131:         return value
```
> يُعيد القيمة value. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:131]

```
132:     }
```
> إغلاق نطاق دالة قراءة ثماني-بِت (readUInt8). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:132]

```
133:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:133]

```
134:     fun readUInt16(): UShort? {
```
> يُعرّف دالة (readUInt16) أي قراءة عدد صحيح غير موقّع 16-بِت، تُعيد قيمة من نوع UShort قابلة للعدم. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:134]

```
135:         if (offset + 2 > data.size) return null
```
> يُعيد عدماً إذا كان offset زائد 2 أكبر من حجم data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:135]

```
136:         val value = ((data[offset].toUByte().toInt() shl 8) or 
```
> يبدأ تعريف متغيّر ثابت (value) بإزاحة البايت عند offset (محوّلاً إلى UByte ثم Int) إلى اليسار 8 بتات ودمجه بأو (or) مع التتمة في السطر التالي. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:136]

```
137:                     (data[offset + 1].toUByte().toInt())).toUShort()
```
> يكمل تعريف value بدمج البايت عند offset+1 (محوّلاً إلى UByte ثم Int) ثم تحويل الناتج الكلي إلى UShort. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:137]

```
138:         offset += 2
```
> يزيد قيمة offset بمقدار اثنين. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:138]

```
139:         return value
```
> يُعيد القيمة value. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:139]

```
140:     }
```
> إغلاق نطاق دالة قراءة ستة-عشر-بِت (readUInt16). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:140]

```
141:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:141]

```
142:     fun readUInt32(): UInt? {
```
> يُعرّف دالة (readUInt32) أي قراءة عدد صحيح غير موقّع 32-بِت، تُعيد قيمة من نوع UInt قابلة للعدم. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:142]

```
143:         if (offset + 4 > data.size) return null
```
> يُعيد عدماً إذا كان offset زائد 4 أكبر من حجم data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:143]

```
144:         val value = ((data[offset].toUByte().toUInt() shl 24) or
```
> يبدأ تعريف متغيّر ثابت (value) بإزاحة البايت عند offset (محوّلاً إلى UByte ثم UInt) إلى اليسار 24 بِت ودمجه بأو (or) مع التتمة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:144]

```
145:                     (data[offset + 1].toUByte().toUInt() shl 16) or
```
> يكمل تعريف value بإزاحة البايت عند offset+1 (محوّلاً إلى UByte ثم UInt) إلى اليسار 16 بِت ودمجه بأو (or). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:145]

```
146:                     (data[offset + 2].toUByte().toUInt() shl 8) or
```
> يكمل تعريف value بإزاحة البايت عند offset+2 (محوّلاً إلى UByte ثم UInt) إلى اليسار 8 بتات ودمجه بأو (or). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:146]

```
147:                     (data[offset + 3].toUByte().toUInt()))
```
> يكمل تعريف value بدمج البايت عند offset+3 (محوّلاً إلى UByte ثم UInt) دون إزاحة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:147]

```
148:         offset += 4
```
> يزيد قيمة offset بمقدار أربعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:148]

```
149:         return value
```
> يُعيد القيمة value. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:149]

```
150:     }
```
> إغلاق نطاق دالة قراءة اثنان-وثلاثون-بِت (readUInt32). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:150]

```
151:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:151]

```
152:     fun readUInt64(): ULong? {
```
> يُعرّف دالة (readUInt64) أي قراءة عدد صحيح غير موقّع 64-بِت، تُعيد قيمة من نوع ULong قابلة للعدم. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:152]

```
153:         if (offset + 8 > data.size) return null
```
> يُعيد عدماً إذا كان offset زائد 8 أكبر من حجم data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:153]

```
154:         var value = 0UL
```
> يُعرّف متغيّراً متغيّر القيمة (value) ويهيّئه بالقيمة صفر من نوع ULong. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:154]

```
155:         for (i in 0 until 8) {
```
> يبدأ حلقة تكرار بالمتغيّر i من صفر حتى 8 غير شامل. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:155]

```
156:             value = (value shl 8) or data[offset + i].toUByte().toULong()
```
> يُسند إلى value ناتج إزاحته إلى اليسار 8 بتات ودمجه بأو (or) مع البايت عند offset+i محوّلاً إلى UByte ثم ULong. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:156]

```
157:         }
```
> إغلاق نطاق حلقة التكرار for. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:157]

```
158:         offset += 8
```
> يزيد قيمة offset بمقدار ثمانية. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:158]

```
159:         return value
```
> يُعيد القيمة value. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:159]

```
160:     }
```
> إغلاق نطاق دالة قراءة أربعة-وستون-بِت (readUInt64). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:160]

```
161:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:161]

```
162:     fun readString(maxLength: Int = 255): String? {
```
> يُعرّف دالة (readString) أي قراءة سلسلة نصية، تأخذ معاملاً maxLength من نوع Int بقيمة افتراضية 255 وتُعيد String قابلة للعدم. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:162]

```
163:         val length: Int = if (maxLength <= 255) {
```
> يُعرّف متغيّراً ثابتاً (length) من نوع Int، تُسند له قيمة حسب شرط ما إذا كان maxLength أصغر من أو يساوي 255. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:163]

```
164:             readUInt8()?.toInt() ?: return null
```
> يقرأ بايتاً واحداً باستدعاء readUInt8 ويحوّله إلى Int، وإن كان عدماً يُعيد عدماً من الدالة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:164]

```
165:         } else {
```
> بداية الفرع البديل (else) لتحديد قيمة length. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:165]

```
166:             readUInt16()?.toInt() ?: return null
```
> يقرأ كلمتين باستدعاء readUInt16 ويحوّلهما إلى Int، وإن كان عدماً يُعيد عدماً من الدالة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:166]

```
167:         }
```
> إغلاق نطاق تعبير if/else المُسنِد لقيمة length. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:167]

```
168:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:168]

```
169:         if (offset + length > data.size) return null
```
> يُعيد عدماً إذا كان offset زائد length أكبر من حجم data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:169]

```
170:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:170]

```
171:         val stringData = data.sliceArray(offset until offset + length)
```
> يُعرّف متغيّراً ثابتاً (stringData) كشريحة من data من الموضع offset حتى offset+length غير شامل. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:171]

```
172:         offset += length
```
> يزيد قيمة offset بمقدار length. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:172]

```
173:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:173]

```
174:         return String(stringData, Charsets.UTF_8)
```
> يُعيد سلسلة نصية مبنية من stringData بترميز UTF-8. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:174]

```
175:     }
```
> إغلاق نطاق دالة قراءة السلسلة (readString). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:175]

```
176:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:176]

```
177:     fun readData(maxLength: Int = 65535): ByteArray? {
```
> يُعرّف دالة (readData) أي قراءة بيانات، تأخذ معاملاً maxLength من نوع Int بقيمة افتراضية 65535 وتُعيد ByteArray قابلة للعدم. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:177]

```
178:         val length: Int = if (maxLength <= 255) {
```
> يُعرّف متغيّراً ثابتاً (length) من نوع Int، تُسند له قيمة حسب شرط ما إذا كان maxLength أصغر من أو يساوي 255. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:178]

```
179:             readUInt8()?.toInt() ?: return null
```
> يقرأ بايتاً واحداً باستدعاء readUInt8 ويحوّله إلى Int، وإن كان عدماً يُعيد عدماً من الدالة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:179]

```
180:         } else {
```
> بداية الفرع البديل (else) لتحديد قيمة length. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:180]

```
181:             readUInt16()?.toInt() ?: return null
```
> يقرأ كلمتين باستدعاء readUInt16 ويحوّلهما إلى Int، وإن كان عدماً يُعيد عدماً من الدالة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:181]

```
182:         }
```
> إغلاق نطاق تعبير if/else المُسنِد لقيمة length. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:182]

```
183:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:183]

```
184:         if (offset + length > data.size) return null
```
> يُعيد عدماً إذا كان offset زائد length أكبر من حجم data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:184]

```
185:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:185]

```
186:         val data = this.data.sliceArray(offset until offset + length)
```
> يُعرّف متغيّراً ثابتاً محلياً (data) كشريحة من this.data من الموضع offset حتى offset+length غير شامل. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:186]

```
187:         offset += length
```
> يزيد قيمة offset بمقدار length. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:187]

```
188:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:188]

```
189:         return data
```
> يُعيد المتغيّر المحلي data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:189]

```
190:     }
```
> إغلاق نطاق دالة قراءة البيانات (readData). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:190]

```
191:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:191]

```
192:     fun readDate(): Date? {
```
> يُعرّف دالة (readDate) أي قراءة تاريخ، تُعيد قيمة من نوع Date قابلة للعدم. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:192]

```
193:         val timestamp = readUInt64() ?: return null
```
> يُعرّف متغيّراً ثابتاً (timestamp) بقراءة readUInt64، وإن كان عدماً يُعيد عدماً من الدالة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:193]

```
194:         return Date(timestamp.toLong())
```
> يُعيد كائن Date مبنياً من timestamp بعد تحويله إلى Long. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:194]

```
195:     }
```
> إغلاق نطاق دالة قراءة التاريخ (readDate). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:195]

```
196:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:196]

```
197:     fun readUUID(): String? {
```
> يُعرّف دالة (readUUID) أي قراءة معرّف فريد عالمي، تُعيد قيمة من نوع String قابلة للعدم. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:197]

```
198:         if (offset + 16 > data.size) return null
```
> يُعيد عدماً إذا كان offset زائد 16 أكبر من حجم data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:198]

```
199:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:199]

```
200:         val uuidData = data.sliceArray(offset until offset + 16)
```
> يُعرّف متغيّراً ثابتاً (uuidData) كشريحة من data من الموضع offset حتى offset+16 غير شامل. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:200]

```
201:         offset += 16
```
> يزيد قيمة offset بمقدار ستة عشر. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:201]

```
202:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:202]

```
203:         // Convert 16 bytes to UUID string format
```
> تعليق: «تحويل 16 بايت إلى صيغة سلسلة المعرّف الفريد». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:203]

```
204:         val uuid = uuidData.joinToString("") { "%02x".format(it) }
```
> يُعرّف متغيّراً ثابتاً (uuid) بدمج عناصر uuidData في سلسلة بفاصل فارغ مع تنسيق كل بايت إلى رقمين سداسيين عشريين بالصيغة "%02x". [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:204]

```
205:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:205]

```
206:         // Insert hyphens at proper positions: 8-4-4-4-12
```
> تعليق: «إدراج الشرطات في المواضع الصحيحة: 8-4-4-4-12». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:206]

```
207:         val result = StringBuilder()
```
> يُعرّف متغيّراً ثابتاً (result) ككائن StringBuilder جديد فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:207]

```
208:         for ((index, char) in uuid.withIndex()) {
```
> يبدأ حلقة تكرار على uuid مع الفهرس، حيث index هو الموضع وchar هو المحرف. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:208]

```
209:             if (index == 8 || index == 12 || index == 16 || index == 20) {
```
> يفحص ما إذا كان index يساوي 8 أو 12 أو 16 أو 20. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:209]

```
210:                 result.append("-")
```
> يُلحق شرطة "-" إلى result. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:210]

```
211:             }
```
> إغلاق نطاق جملة الشرط if الداخلية. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:211]

```
212:             result.append(char)
```
> يُلحق المحرف char إلى result. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:212]

```
213:         }
```
> إغلاق نطاق حلقة التكرار for. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:213]

```
214:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:214]

```
215:         return result.toString().uppercase()
```
> يُعيد محتوى result كسلسلة نصية بعد تحويلها إلى أحرف كبيرة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:215]

```
216:     }
```
> إغلاق نطاق دالة قراءة المعرّف الفريد (readUUID). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:216]

```
217:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:217]

```
218:     fun readFixedBytes(count: Int): ByteArray? {
```
> يُعرّف دالة (readFixedBytes) أي قراءة عدد ثابت من البايتات، تأخذ معاملاً count من نوع Int وتُعيد ByteArray قابلة للعدم. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:218]

```
219:         if (offset + count > data.size) return null
```
> يُعيد عدماً إذا كان offset زائد count أكبر من حجم data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:219]

```
220:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:220]

```
221:         val data = this.data.sliceArray(offset until offset + count)
```
> يُعرّف متغيّراً ثابتاً محلياً (data) كشريحة من this.data من الموضع offset حتى offset+count غير شامل. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:221]

```
222:         offset += count
```
> يزيد قيمة offset بمقدار count. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:222]

```
223:         
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:223]

```
224:         return data
```
> يُعيد المتغيّر المحلي data. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:224]

```
225:     }
```
> إغلاق نطاق دالة قراءة البايتات الثابتة (readFixedBytes). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:225]

```
226:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:226]

```
227:     // Get current offset position
```
> تعليق: «الحصول على موضع الإزاحة الحالي». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:227]

```
228:     val currentOffset: Int get() = offset
```
> يُعرّف خاصية ثابتة (currentOffset) من نوع Int، وجالبها (getter) يُعيد offset. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:228]

```
229: }
```
> إغلاق نطاق صنف قارئ البيانات الثنائية (BinaryDataReader). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:229]

```
230: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:230]

```
231: // MARK: - Binary Message Protocol
```
> تعليق: «علامة قسم: بروتوكول الرسائل الثنائية». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:231]

```
232: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:232]

```
233: interface BinaryEncodable {
```
> يُعرّف واجهة (BinaryEncodable) أي القابل للترميز الثنائي. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:233]

```
234:     fun toBinaryData(): ByteArray
```
> يُعرّف داخل الواجهة دالة مجردة (toBinaryData) أي التحويل إلى بيانات ثنائية، تُعيد ByteArray. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:234]

```
235: }
```
> إغلاق نطاق واجهة القابل للترميز الثنائي (BinaryEncodable). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:235]

```
236: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:236]

```
237: // MARK: - Message Type Registry
```
> تعليق: «علامة قسم: سجل أنواع الرسائل». [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:237]

```
238: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:238]

```
239: enum class BinaryMessageType(val value: UByte) {
```
> يُعرّف صنفاً تعدادياً (BinaryMessageType) أي نوع الرسالة الثنائية، بخاصية ثابتة value من نوع UByte لكل عنصر. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:239]

```
240:     DELIVERY_ACK(0x01u),
```
> يُعرّف عنصر التعداد (DELIVERY_ACK) أي إقرار التسليم بالقيمة 0x01 غير الموقّعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:240]

```
241:     READ_RECEIPT(0x02u),
```
> يُعرّف عنصر التعداد (READ_RECEIPT) أي إيصال القراءة بالقيمة 0x02 غير الموقّعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:241]

```
242:     CHANNEL_KEY_VERIFY_REQUEST(0x03u),
```
> يُعرّف عنصر التعداد (CHANNEL_KEY_VERIFY_REQUEST) أي طلب التحقق من مفتاح القناة بالقيمة 0x03 غير الموقّعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:242]

```
243:     CHANNEL_KEY_VERIFY_RESPONSE(0x04u),
```
> يُعرّف عنصر التعداد (CHANNEL_KEY_VERIFY_RESPONSE) أي استجابة التحقق من مفتاح القناة بالقيمة 0x04 غير الموقّعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:243]

```
244:     CHANNEL_PASSWORD_UPDATE(0x05u),
```
> يُعرّف عنصر التعداد (CHANNEL_PASSWORD_UPDATE) أي تحديث كلمة مرور القناة بالقيمة 0x05 غير الموقّعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:244]

```
245:     CHANNEL_METADATA(0x06u),
```
> يُعرّف عنصر التعداد (CHANNEL_METADATA) أي بيانات القناة الوصفية بالقيمة 0x06 غير الموقّعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:245]

```
246:     VERSION_HELLO(0x07u),
```
> يُعرّف عنصر التعداد (VERSION_HELLO) أي تحية الإصدار بالقيمة 0x07 غير الموقّعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:246]

```
247:     VERSION_ACK(0x08u),
```
> يُعرّف عنصر التعداد (VERSION_ACK) أي إقرار الإصدار بالقيمة 0x08 غير الموقّعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:247]

```
248:     NOISE_IDENTITY_ANNOUNCEMENT(0x09u),
```
> يُعرّف عنصر التعداد (NOISE_IDENTITY_ANNOUNCEMENT) أي إعلان هوية بروتوكول Noise بالقيمة 0x09 غير الموقّعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:248]

```
249:     NOISE_MESSAGE(0x0Au);
```
> يُعرّف عنصر التعداد (NOISE_MESSAGE) أي رسالة بروتوكول Noise بالقيمة 0x0A غير الموقّعة، وتنتهي قائمة العناصر بفاصلة منقوطة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:249]

```
250:     
```
> سطر فارغ (يحتوي مسافات بيضاء فقط)، ويقع داخل جسم الصنف التعدادي BinaryMessageType. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:250]
