# شريحة — app/src/main/java/com/bitchat/android/model/FragmentPayload.kt (الأسطر 1–155)

```
1: package com.bitchat.android.model
```
> يُعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:2]

```
3: import com.bitchat.android.protocol.MessageType
```
> يستورد (import) النوع `MessageType` من الحزمة `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:4]

```
5: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:5]

```
6:  * FragmentPayload - 100% iOS-compatible fragment payload structure
```
> تعليق: «حمولة الشظية (FragmentPayload) - بنية حمولة شظية متوافقة ١٠٠٪ مع نظام iOS». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:6]

```
7:  * 
```
> تعليق: سطر فارغ داخل التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:7]

```
8:  * This class handles the encoding and decoding of fragment payloads exactly
```
> تعليق: «هذا الصنف يتولّى ترميز وفك ترميز حمولات الشظايا تماماً». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:8]

```
9:  * as implemented in iOS bitchat SimplifiedBluetoothService.
```
> تعليق: «كما هو مطبَّق في خدمة iOS bitchat باسم SimplifiedBluetoothService». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:9]

```
10:  * 
```
> تعليق: سطر فارغ داخل التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:10]

```
11:  * Fragment payload structure (matching iOS):
```
> تعليق: «بنية حمولة الشظية (مطابِقة لنظام iOS):». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:11]

```
12:  * - 8 bytes: Fragment ID (random bytes)
```
> تعليق: «- ٨ بايتات: معرّف الشظية (بايتات عشوائية)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:12]

```
13:  * - 2 bytes: Index (big-endian) 
```
> تعليق: «- ٢ بايت: الفهرس (بترتيب البايت الكبير big-endian)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:13]

```
14:  * - 2 bytes: Total count (big-endian)
```
> تعليق: «- ٢ بايت: العدد الإجمالي (بترتيب البايت الكبير big-endian)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:14]

```
15:  * - 1 byte: Original message type
```
> تعليق: «- ١ بايت: نوع الرسالة الأصلي». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:15]

```
16:  * - Variable: Fragment data
```
> تعليق: «- متغيّر الطول: بيانات الشظية». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:16]

```
17:  * 
```
> تعليق: سطر فارغ داخل التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:17]

```
18:  * Total header size: 13 bytes
```
> تعليق: «الحجم الإجمالي للترويسة: ١٣ بايت». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:18]

```
19:  */
```
> نهاية التعليق التوثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:19]

```
20: data class FragmentPayload(
```
> يُعرّف صنف بيانات (data class) باسم `FragmentPayload` (حمولة الشظية) ويبدأ قائمة معاملات بانيه الأساسي. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:20]

```
21:     val fragmentID: ByteArray,      // 8 bytes - random fragment identifier
```
> يُعرّف خاصية ثابتة (val) باسم `fragmentID` (معرّف الشظية) من نوع `ByteArray` (مصفوفة بايتات)، مع تعليق: «٨ بايتات - معرّف شظية عشوائي». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:21]

```
22:     val index: Int,                 // Fragment index (0-based)
```
> يُعرّف خاصية ثابتة (val) باسم `index` (الفهرس) من نوع `Int` (عدد صحيح)، مع تعليق: «فهرس الشظية (يبدأ من الصفر)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:22]

```
23:     val total: Int,                 // Total number of fragments
```
> يُعرّف خاصية ثابتة (val) باسم `total` (الإجمالي) من نوع `Int` (عدد صحيح)، مع تعليق: «العدد الإجمالي للشظايا». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:23]

```
24:     val originalType: UByte,        // Original message type before fragmentation
```
> يُعرّف خاصية ثابتة (val) باسم `originalType` (النوع الأصلي) من نوع `UByte` (بايت غير مُوقَّع)، مع تعليق: «نوع الرسالة الأصلي قبل التشظية». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:24]

```
25:     val data: ByteArray             // Fragment data
```
> يُعرّف خاصية ثابتة (val) باسم `data` (البيانات) من نوع `ByteArray` (مصفوفة بايتات)، مع تعليق: «بيانات الشظية». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:25]

```
26: ) {
```
> يُغلق قائمة معاملات الباني ويفتح جسم الصنف `FragmentPayload`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:26]

```
27:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:27]

```
28:     companion object {
```
> يفتح كائناً مصاحباً (companion object) لاحتواء الأعضاء الساكنة للصنف. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:28]

```
29:         const val HEADER_SIZE = 13
```
> يُعرّف ثابتاً وقت التصريف (const val) باسم `HEADER_SIZE` (حجم الترويسة) بالقيمة الحرفية `13`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:29]

```
30:         const val FRAGMENT_ID_SIZE = 8
```
> يُعرّف ثابتاً وقت التصريف (const val) باسم `FRAGMENT_ID_SIZE` (حجم معرّف الشظية) بالقيمة الحرفية `8`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:30]

```
31:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:31]

```
32:         /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:32]

```
33:          * Decode fragment payload from binary data
```
> تعليق: «فكّ ترميز حمولة الشظية من بيانات ثنائية». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:33]

```
34:          * Matches iOS implementation exactly
```
> تعليق: «يطابق تطبيق iOS تماماً». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:34]

```
35:          */
```
> نهاية التعليق التوثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:35]

```
36:         fun decode(payloadData: ByteArray): FragmentPayload? {
```
> يُعرّف دالة (fun) باسم `decode` (فكّ الترميز) تأخذ معاملاً `payloadData` (بيانات الحمولة) من نوع `ByteArray`، وتُعيد `FragmentPayload?` (حمولة شظية قابلة للقيمة الفارغة null). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:36]

```
37:             if (payloadData.size < HEADER_SIZE) {
```
> يبدأ شرطاً (if) يفحص إن كان حجم `payloadData` أصغر من `HEADER_SIZE` (أي أصغر من ١٣). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:37]

```
38:                 return null
```
> يُعيد `null` (قيمة فارغة) عند تحقّق الشرط السابق. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:38]

```
39:             }
```
> إغلاق نطاق كتلة الشرط (if). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:39]

```
40:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:40]

```
41:             try {
```
> يفتح كتلة محاولة (try) لالتقاط الاستثناءات. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:41]

```
42:                 // Extract fragment ID (8 bytes)
```
> تعليق: «استخراج معرّف الشظية (٨ بايتات)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:42]

```
43:                 val fragmentID = payloadData.sliceArray(0..<FRAGMENT_ID_SIZE)
```
> يُعرّف متغيّراً ثابتاً (val) باسم `fragmentID` يساوي شريحة من `payloadData` بالدالة `sliceArray` ضمن المدى `0` حتى ما قبل `FRAGMENT_ID_SIZE` (أي البايتات من ٠ إلى ٧). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:43]

```
44:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:44]

```
45:                 // Extract index (2 bytes, big-endian) - matching iOS
```
> تعليق: «استخراج الفهرس (٢ بايت، بترتيب البايت الكبير big-endian) - مطابِق لنظام iOS». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:45]

```
46:                 val index = ((payloadData[8].toInt() and 0xFF) shl 8) or 
```
> يُعرّف متغيّراً ثابتاً (val) باسم `index` يبدأ حسابه بأخذ البايت ذي الفهرس ٨ من `payloadData`، تحويله إلى عدد صحيح بـ`toInt()`، تطبيق «و» الثنائي مع `0xFF`، ثم إزاحته يساراً بـ`shl 8`، ثم عامل «أو» الثنائي (or). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:46]

```
47:                            (payloadData[9].toInt() and 0xFF)
```
> يكمل تعريف `index` بأخذ البايت ذي الفهرس ٩ من `payloadData`، تحويله إلى عدد صحيح، وتطبيق «و» الثنائي مع `0xFF`، فيُدمَج مع الجزء السابق عبر «أو» الثنائي. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:47]

```
48:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:48]

```
49:                 // Extract total (2 bytes, big-endian) - matching iOS  
```
> تعليق: «استخراج الإجمالي (٢ بايت، بترتيب البايت الكبير big-endian) - مطابِق لنظام iOS». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:49]

```
50:                 val total = ((payloadData[10].toInt() and 0xFF) shl 8) or
```
> يُعرّف متغيّراً ثابتاً (val) باسم `total` يبدأ حسابه بأخذ البايت ذي الفهرس ١٠ من `payloadData`، تحويله إلى عدد صحيح، «و» الثنائي مع `0xFF`، إزاحته يساراً بـ`shl 8`، ثم عامل «أو» الثنائي (or). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:50]

```
51:                            (payloadData[11].toInt() and 0xFF)
```
> يكمل تعريف `total` بأخذ البايت ذي الفهرس ١١ من `payloadData`، تحويله إلى عدد صحيح، و«و» الثنائي مع `0xFF`، فيُدمَج مع الجزء السابق عبر «أو» الثنائي. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:51]

```
52:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:52]

```
53:                 // Extract original type (1 byte)
```
> تعليق: «استخراج النوع الأصلي (١ بايت)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:53]

```
54:                 val originalType = payloadData[12].toUByte()
```
> يُعرّف متغيّراً ثابتاً (val) باسم `originalType` يساوي البايت ذا الفهرس ١٢ من `payloadData` بعد تحويله إلى `UByte` بالدالة `toUByte()`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:54]

```
55:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:55]

```
56:                 // Extract fragment data (remaining bytes)
```
> تعليق: «استخراج بيانات الشظية (البايتات المتبقية)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:56]

```
57:                 val data = if (payloadData.size > HEADER_SIZE) {
```
> يُعرّف متغيّراً ثابتاً (val) باسم `data` بقيمة تعبير شرطي (if) يفحص إن كان حجم `payloadData` أكبر من `HEADER_SIZE` (أكبر من ١٣). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:57]

```
58:                     payloadData.sliceArray(HEADER_SIZE..<payloadData.size)
```
> عند تحقّق الشرط: يأخذ شريحة من `payloadData` بالدالة `sliceArray` ضمن المدى من `HEADER_SIZE` حتى ما قبل حجم `payloadData` (أي البايتات من ١٣ إلى النهاية). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:58]

```
59:                 } else {
```
> يُغلق فرع التحقّق ويفتح الفرع البديل (else) للتعبير الشرطي. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:59]

```
60:                     ByteArray(0)
```
> في الفرع البديل: يُنشئ مصفوفة بايتات (ByteArray) فارغة بطول صفر. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:60]

```
61:                 }
```
> إغلاق نطاق التعبير الشرطي (if/else) الذي يُسنِد قيمة `data`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:61]

```
62:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:62]

```
63:                 return FragmentPayload(fragmentID, index, total, originalType, data)
```
> يُعيد كائناً جديداً من `FragmentPayload` مُنشأً بالقيم `fragmentID` و`index` و`total` و`originalType` و`data`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:63]

```
64:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:64]

```
65:             } catch (e: Exception) {
```
> يُغلق كتلة المحاولة (try) ويفتح كتلة الالتقاط (catch) لاستثناء `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:65]

```
66:                 return null
```
> يُعيد `null` (قيمة فارغة) عند وقوع أي استثناء. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:66]

```
67:             }
```
> إغلاق نطاق كتلة الالتقاط (catch). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:67]

```
68:         }
```
> إغلاق نطاق الدالة `decode`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:68]

```
69:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:69]

```
70:         /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:70]

```
71:          * Generate random fragment ID (8 bytes)
```
> تعليق: «توليد معرّف شظية عشوائي (٨ بايتات)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:71]

```
72:          * Matches iOS implementation: Data((0..<8).map { _ in UInt8.random(in: 0...255) })
```
> تعليق: «يطابق تطبيق iOS: Data((0..<8).map { _ in UInt8.random(in: 0...255) })». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:72]

```
73:          */
```
> نهاية التعليق التوثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:73]

```
74:         fun generateFragmentID(): ByteArray {
```
> يُعرّف دالة (fun) باسم `generateFragmentID` (توليد معرّف الشظية) لا تأخذ معاملات وتُعيد `ByteArray` (مصفوفة بايتات). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:74]

```
75:             val fragmentID = ByteArray(FRAGMENT_ID_SIZE)
```
> يُعرّف متغيّراً ثابتاً (val) باسم `fragmentID` يساوي مصفوفة بايتات جديدة بطول `FRAGMENT_ID_SIZE` (أي ٨). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:75]

```
76:             kotlin.random.Random.nextBytes(fragmentID)
```
> يستدعي `kotlin.random.Random.nextBytes` لملء المصفوفة `fragmentID` ببايتات عشوائية. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:76]

```
77:             return fragmentID
```
> يُعيد المصفوفة `fragmentID`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:77]

```
78:         }
```
> إغلاق نطاق الدالة `generateFragmentID`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:78]

```
79:     }
```
> إغلاق نطاق الكائن المصاحب (companion object). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:79]

```
80:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:80]

```
81:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:81]

```
82:      * Encode fragment payload to binary data
```
> تعليق: «ترميز حمولة الشظية إلى بيانات ثنائية». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:82]

```
83:      * Matches iOS implementation exactly
```
> تعليق: «يطابق تطبيق iOS تماماً». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:83]

```
84:      */
```
> نهاية التعليق التوثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:84]

```
85:     fun encode(): ByteArray {
```
> يُعرّف دالة (fun) باسم `encode` (الترميز) لا تأخذ معاملات وتُعيد `ByteArray` (مصفوفة بايتات). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:85]

```
86:         val payload = ByteArray(HEADER_SIZE + data.size)
```
> يُعرّف متغيّراً ثابتاً (val) باسم `payload` (الحمولة) يساوي مصفوفة بايتات جديدة بطول مجموع `HEADER_SIZE` وحجم `data`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:86]

```
87:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:87]

```
88:         // Fragment ID (8 bytes)
```
> تعليق: «معرّف الشظية (٨ بايتات)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:88]

```
89:         System.arraycopy(fragmentID, 0, payload, 0, FRAGMENT_ID_SIZE)
```
> يستدعي `System.arraycopy` لنسخ من المصفوفة `fragmentID` بدءاً من الموضع ٠ إلى المصفوفة `payload` بدءاً من الموضع ٠ بطول `FRAGMENT_ID_SIZE` (٨ بايتات). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:89]

```
90:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:90]

```
91:         // Index (2 bytes, big-endian) - matching iOS withUnsafeBytes(of: UInt16(index).bigEndian)
```
> تعليق: «الفهرس (٢ بايت، بترتيب البايت الكبير big-endian) - مطابِق لنظام iOS withUnsafeBytes(of: UInt16(index).bigEndian)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:91]

```
92:         payload[8] = ((index shr 8) and 0xFF).toByte()
```
> يُسنِد إلى الموضع ٨ من `payload` قيمة `index` بعد إزاحته يميناً بـ`shr 8` و«و» الثنائي مع `0xFF` ثم تحويله إلى بايت بـ`toByte()` (البايت الأعلى من الفهرس). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:92]

```
93:         payload[9] = (index and 0xFF).toByte()
```
> يُسنِد إلى الموضع ٩ من `payload` قيمة `index` بعد «و» الثنائي مع `0xFF` ثم تحويله إلى بايت (البايت الأدنى من الفهرس). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:93]

```
94:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:94]

```
95:         // Total (2 bytes, big-endian) - matching iOS withUnsafeBytes(of: UInt16(fragments.count).bigEndian)
```
> تعليق: «الإجمالي (٢ بايت، بترتيب البايت الكبير big-endian) - مطابِق لنظام iOS withUnsafeBytes(of: UInt16(fragments.count).bigEndian)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:95]

```
96:         payload[10] = ((total shr 8) and 0xFF).toByte()
```
> يُسنِد إلى الموضع ١٠ من `payload` قيمة `total` بعد إزاحته يميناً بـ`shr 8` و«و» الثنائي مع `0xFF` ثم تحويله إلى بايت (البايت الأعلى من الإجمالي). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:96]

```
97:         payload[11] = (total and 0xFF).toByte()
```
> يُسنِد إلى الموضع ١١ من `payload` قيمة `total` بعد «و» الثنائي مع `0xFF` ثم تحويله إلى بايت (البايت الأدنى من الإجمالي). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:97]

```
98:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:98]

```
99:         // Original type (1 byte)
```
> تعليق: «النوع الأصلي (١ بايت)». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:99]

```
100:         payload[12] = originalType.toByte()
```
> يُسنِد إلى الموضع ١٢ من `payload` قيمة `originalType` بعد تحويلها إلى بايت بـ`toByte()`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:100]

```
101:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:101]

```
102:         // Fragment data
```
> تعليق: «بيانات الشظية». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:102]

```
103:         if (data.isNotEmpty()) {
```
> يبدأ شرطاً (if) يفحص إن كانت `data` غير فارغة بالدالة `isNotEmpty()`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:103]

```
104:             System.arraycopy(data, 0, payload, HEADER_SIZE, data.size)
```
> يستدعي `System.arraycopy` لنسخ من المصفوفة `data` بدءاً من الموضع ٠ إلى `payload` بدءاً من الموضع `HEADER_SIZE` (١٣) بطول حجم `data`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:104]

```
105:         }
```
> إغلاق نطاق كتلة الشرط (if). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:105]

```
106:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:106]

```
107:         return payload
```
> يُعيد المصفوفة `payload`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:107]

```
108:     }
```
> إغلاق نطاق الدالة `encode`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:108]

```
109:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:109]

```
110:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:110]

```
111:      * Get fragment ID as hex string for logging/debugging
```
> تعليق: «الحصول على معرّف الشظية كسلسلة ست عشرية (hex) للتسجيل/التنقيح». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:111]

```
112:      */
```
> نهاية التعليق التوثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:112]

```
113:     fun getFragmentIDString(): String {
```
> يُعرّف دالة (fun) باسم `getFragmentIDString` (الحصول على نص معرّف الشظية) لا تأخذ معاملات وتُعيد `String` (سلسلة نصية). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:113]

```
114:         return fragmentID.joinToString("") { "%02x".format(it) }
```
> يُعيد ناتج دمج عناصر `fragmentID` بالدالة `joinToString` بفاصل فارغ، حيث يُنسَّق كل عنصر `it` بالصيغة `"%02x"` (ست عشري بخانتين). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:114]

```
115:     }
```
> إغلاق نطاق الدالة `getFragmentIDString`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:115]

```
116:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:116]

```
117:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:117]

```
118:      * Validate fragment payload constraints
```
> تعليق: «التحقّق من قيود حمولة الشظية». [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:118]

```
119:      */
```
> نهاية التعليق التوثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:119]

```
120:     fun isValid(): Boolean {
```
> يُعرّف دالة (fun) باسم `isValid` (هل صالحة) لا تأخذ معاملات وتُعيد `Boolean` (قيمة منطقية). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:120]

```
121:         return fragmentID.size == FRAGMENT_ID_SIZE &&
```
> يبدأ إعادة تعبير منطقي يفحص أن حجم `fragmentID` يساوي `FRAGMENT_ID_SIZE` (٨)، متبوعاً بعامل «و» المنطقي (&&). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:121]

```
122:                index >= 0 &&
```
> يكمل التعبير المنطقي بفحص أن `index` أكبر من أو يساوي ٠، متبوعاً بعامل «و» المنطقي (&&). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:122]

```
123:                total > 0 &&
```
> يكمل التعبير المنطقي بفحص أن `total` أكبر من ٠، متبوعاً بعامل «و» المنطقي (&&). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:123]

```
124:                index < total &&
```
> يكمل التعبير المنطقي بفحص أن `index` أصغر من `total`، متبوعاً بعامل «و» المنطقي (&&). [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:124]

```
125:                data.isNotEmpty()
```
> يُنهي التعبير المنطقي بفحص أن `data` غير فارغة بالدالة `isNotEmpty()`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:125]

```
126:     }
```
> إغلاق نطاق الدالة `isValid`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:126]

```
127:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:127]

```
128:     override fun equals(other: Any?): Boolean {
```
> يُعرّف دالة مُعاد تعريفها (override fun) باسم `equals` (المساواة) تأخذ معاملاً `other` من نوع `Any?` (أي نوع قابل للقيمة الفارغة) وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:128]

```
129:         if (this === other) return true
```
> يفحص بشرط إن كان الكائن الحالي `this` هو نفس مرجع `other` بعامل الهوية (===)، ويُعيد `true` عند ذلك. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:129]

```
130:         if (javaClass != other?.javaClass) return false
```
> يفحص بشرط إن كان `javaClass` للكائن الحالي لا يساوي `javaClass` لـ`other` (مع وصول آمن `?.`)، ويُعيد `false` عند ذلك. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:130]

```
131:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:131]

```
132:         other as FragmentPayload
```
> يُجري تحويل نوع (cast) للكائن `other` إلى النوع `FragmentPayload`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:132]

```
133:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:133]

```
134:         if (!fragmentID.contentEquals(other.fragmentID)) return false
```
> يفحص بشرط إن كان محتوى `fragmentID` لا يساوي محتوى `other.fragmentID` بالدالة `contentEquals` (مع النفي `!`)، ويُعيد `false` عند ذلك. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:134]

```
135:         if (index != other.index) return false
```
> يفحص بشرط إن كان `index` لا يساوي `other.index`، ويُعيد `false` عند ذلك. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:135]

```
136:         if (total != other.total) return false
```
> يفحص بشرط إن كان `total` لا يساوي `other.total`، ويُعيد `false` عند ذلك. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:136]

```
137:         if (originalType != other.originalType) return false
```
> يفحص بشرط إن كان `originalType` لا يساوي `other.originalType`، ويُعيد `false` عند ذلك. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:137]

```
138:         if (!data.contentEquals(other.data)) return false
```
> يفحص بشرط إن كان محتوى `data` لا يساوي محتوى `other.data` بالدالة `contentEquals` (مع النفي `!`)، ويُعيد `false` عند ذلك. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:138]

```
139:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:139]

```
140:         return true
```
> يُعيد `true` عند اجتياز جميع الفحوص السابقة. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:140]

```
141:     }
```
> إغلاق نطاق الدالة `equals`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:141]

```
142:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:142]

```
143:     override fun hashCode(): Int {
```
> يُعرّف دالة مُعاد تعريفها (override fun) باسم `hashCode` (الرمز التجزيئي) لا تأخذ معاملات وتُعيد `Int`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:143]

```
144:         var result = fragmentID.contentHashCode()
```
> يُعرّف متغيّراً قابلاً للتغيير (var) باسم `result` يساوي الرمز التجزيئي لمحتوى `fragmentID` بالدالة `contentHashCode()`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:144]

```
145:         result = 31 * result + index
```
> يُعيد إسناد `result` ليساوي ٣١ مضروباً في `result` السابق مضافاً إليه `index`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:145]

```
146:         result = 31 * result + total
```
> يُعيد إسناد `result` ليساوي ٣١ مضروباً في `result` السابق مضافاً إليه `total`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:146]

```
147:         result = 31 * result + originalType.hashCode()
```
> يُعيد إسناد `result` ليساوي ٣١ مضروباً في `result` السابق مضافاً إليه الرمز التجزيئي لـ`originalType` بالدالة `hashCode()`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:147]

```
148:         result = 31 * result + data.contentHashCode()
```
> يُعيد إسناد `result` ليساوي ٣١ مضروباً في `result` السابق مضافاً إليه الرمز التجزيئي لمحتوى `data` بالدالة `contentHashCode()`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:148]

```
149:         return result
```
> يُعيد قيمة `result`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:149]

```
150:     }
```
> إغلاق نطاق الدالة `hashCode`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:150]

```
151:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:151]

```
152:     override fun toString(): String {
```
> يُعرّف دالة مُعاد تعريفها (override fun) باسم `toString` (التحويل إلى نص) لا تأخذ معاملات وتُعيد `String`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:152]

```
153:         return "FragmentPayload(fragmentID=${getFragmentIDString()}, index=$index, total=$total, originalType=$originalType, dataSize=${data.size})"
```
> يُعيد سلسلة نصية تمثّل الكائن تحتوي على نص معرّف الشظية عبر `getFragmentIDString()`، وقيم `index` و`total` و`originalType` وحجم `data`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:153]

```
154:     }
```
> إغلاق نطاق الدالة `toString`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:154]

```
155: }
```
> إغلاق نطاق الصنف `FragmentPayload`. [app/src/main/java/com/bitchat/android/model/FragmentPayload.kt:155]
