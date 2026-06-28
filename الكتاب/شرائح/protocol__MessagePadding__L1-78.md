# شريحة — app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt (الأسطر 1–78)

```
1: package com.bitchat.android.protocol
```
> يُعلِن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:2]

```
3: import java.security.SecureRandom
```
> يستورد (import) الصنف SecureRandom من حزمة java.security، وهو مولّد أرقام عشوائية آمن (مولّد العشوائية الآمن - SecureRandom). [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:4]

```
5: /**
```
> بداية تعليق توثيقي (comment) متعدّد الأسطر. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:5]

```
6:  * Privacy-preserving padding utilities - exact same as iOS version
```
> تعليق: «أدوات حشو حافظة للخصوصية - مطابقة تماماً لنسخة iOS». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:6]

```
7:  * Provides traffic analysis resistance by normalizing message sizes
```
> تعليق: «توفّر مقاومة لتحليل حركة المرور عبر توحيد أحجام الرسائل». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:7]

```
8:  */
```
> نهاية التعليق التوثيقي المتعدّد الأسطر. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:8]

```
9: object MessagePadding {
```
> يُعرّف كائناً مفرداً (object) باسم MessagePadding (حاشِية الرسالة - MessagePadding)، ويفتح نطاق جسمه. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:9]

```
10:     // Standard block sizes for padding - exact same as iOS
```
> تعليق: «أحجام الكتل القياسية للحشو - مطابقة تماماً لـ iOS». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:10]

```
11:     private val blockSizes = listOf(256, 512, 1024, 2048)
```
> يُعرّف متغيّراً خاصاً (private) ثابت الإسناد (val) باسم blockSizes (أحجام الكتل - blockSizes) ويُسنِد إليه قائمة (listOf) قيمها الحرفية 256 و512 و1024 و2048. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:11]

```
12:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:12]

```
13:     /**
```
> بداية تعليق توثيقي متعدّد الأسطر. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:13]

```
14:      * Find optimal block size for data - exact same logic as iOS
```
> تعليق: «إيجاد حجم الكتلة الأمثل للبيانات - نفس منطق iOS تماماً». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:14]

```
15:      */
```
> نهاية التعليق التوثيقي المتعدّد الأسطر. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:15]

```
16:     fun optimalBlockSize(dataSize: Int): Int {
```
> يُعرّف دالة (fun) باسم optimalBlockSize (حجم الكتلة الأمثل - optimalBlockSize) تأخذ وسيطاً dataSize (حجم البيانات - dataSize) من نوع Int وتُعيد قيمة من نوع Int، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:16]

```
17:         // Account for encryption overhead (~16 bytes for AES-GCM tag)
```
> تعليق: «احتساب عبء التشفير (نحو 16 بايت لوسم AES-GCM)». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:17]

```
18:         val totalSize = dataSize + 16
```
> يُعرّف متغيّراً ثابت الإسناد (val) باسم totalSize (الحجم الكلّي - totalSize) ويُسنِد إليه ناتج جمع dataSize مع القيمة الحرفية 16. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:18]

```
19:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:19]

```
20:         // Find smallest block that fits
```
> تعليق: «إيجاد أصغر كتلة تتّسع». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:20]

```
21:         for (blockSize in blockSizes) {
```
> يبدأ حلقة تكرار (for) تمرّ بكل عنصر blockSize (حجم الكتلة - blockSize) في القائمة blockSizes، ويفتح نطاق جسم الحلقة. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:21]

```
22:             if (totalSize <= blockSize) {
```
> يختبر شرطاً (if): إن كان totalSize أصغر من أو يساوي blockSize، ويفتح نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:22]

```
23:                 return blockSize
```
> يُعيد قيمة blockSize ويُنهي الدالة. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:23]

```
24:             }
```
> إغلاق نطاق كتلة الشرط (if). [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:24]

```
25:         }
```
> إغلاق نطاق حلقة التكرار (for). [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:25]

```
26:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:26]

```
27:         // For very large messages, just use the original size
```
> تعليق: «للرسائل الكبيرة جداً، استعمل الحجم الأصلي فقط». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:27]

```
28:         // (will be fragmented anyway)
```
> تعليق: «(ستُجزّأ على أي حال)». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:28]

```
29:         return dataSize
```
> يُعيد قيمة dataSize ويُنهي الدالة. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:29]

```
30:     }
```
> إغلاق نطاق دالة optimalBlockSize. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:30]

```
31:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:31]

```
32:     /**
```
> بداية تعليق توثيقي متعدّد الأسطر. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:32]

```
33:      * Add PKCS#7-style padding to reach target size - FIXED: proper PKCS#7 (iOS compatible)
```
> تعليق: «إضافة حشو بنمط PKCS#7 للوصول إلى الحجم الهدف - مُصلَح: PKCS#7 سليم (متوافق مع iOS)». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:33]

```
34:      */
```
> نهاية التعليق التوثيقي المتعدّد الأسطر. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:34]

```
35:     fun pad(data: ByteArray, targetSize: Int): ByteArray {
```
> يُعرّف دالة (fun) باسم pad (الحشو - pad) تأخذ وسيطاً data (البيانات - data) من نوع ByteArray ووسيطاً targetSize (الحجم الهدف - targetSize) من نوع Int وتُعيد قيمة من نوع ByteArray، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:35]

```
36:         if (data.size >= targetSize) return data
```
> يختبر شرطاً (if): إن كان حجم data أكبر من أو يساوي targetSize، فيُعيد data كما هي. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:36]

```
37:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:37]

```
38:         val paddingNeeded = targetSize - data.size
```
> يُعرّف متغيّراً ثابت الإسناد (val) باسم paddingNeeded (الحشو المطلوب - paddingNeeded) ويُسنِد إليه ناتج طرح حجم data من targetSize. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:38]

```
39:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:39]

```
40:         // Constrain to 255 to fit a single-byte pad length marker
```
> تعليق: «التقييد بـ 255 ليتّسع علامة طول الحشو ذات البايت الواحد». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:40]

```
41:         if (paddingNeeded <= 0 || paddingNeeded > 255) return data
```
> يختبر شرطاً (if): إن كان paddingNeeded أصغر من أو يساوي 0 أو أكبر من 255، فيُعيد data كما هي. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:41]

```
42:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:42]

```
43:         val result = ByteArray(targetSize)
```
> يُعرّف متغيّراً ثابت الإسناد (val) باسم result (النتيجة - result) ويُسنِد إليه مصفوفة بايتات (ByteArray) جديدة طولها targetSize. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:43]

```
44:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:44]

```
45:         // Copy original data
```
> تعليق: «نسخ البيانات الأصلية». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:45]

```
46:         System.arraycopy(data, 0, result, 0, data.size)
```
> يستدعي System.arraycopy لنسخ من المصفوفة data بدءاً من الفهرس 0 إلى المصفوفة result بدءاً من الفهرس 0 بعدد عناصر يساوي حجم data. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:46]

```
47:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:47]

```
48:         // PKCS#7: All pad bytes are equal to the pad length (iOS fix)
```
> تعليق: «PKCS#7: كل بايتات الحشو تساوي طول الحشو (إصلاح iOS)». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:48]

```
49:         for (i in data.size until targetSize) {
```
> يبدأ حلقة تكرار (for) بالمتغيّر i من حجم data حتى (until) targetSize دون شموله، ويفتح نطاق جسم الحلقة. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:49]

```
50:             result[i] = paddingNeeded.toByte()
```
> يُسنِد إلى العنصر ذي الفهرس i في result قيمة paddingNeeded محوّلةً إلى بايت (toByte). [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:50]

```
51:         }
```
> إغلاق نطاق حلقة التكرار (for). [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:51]

```
52:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:52]

```
53:         return result
```
> يُعيد المصفوفة result ويُنهي الدالة. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:53]

```
54:     }
```
> إغلاق نطاق دالة pad. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:54]

```
55:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:55]

```
56:     /**
```
> بداية تعليق توثيقي متعدّد الأسطر. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:56]

```
57:      * Remove padding from data - FIXED: strict PKCS#7 validation (iOS compatible)
```
> تعليق: «إزالة الحشو من البيانات - مُصلَح: تحقّق صارم بنمط PKCS#7 (متوافق مع iOS)». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:57]

```
58:      */
```
> نهاية التعليق التوثيقي المتعدّد الأسطر. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:58]

```
59:     fun unpad(data: ByteArray): ByteArray {
```
> يُعرّف دالة (fun) باسم unpad (إزالة الحشو - unpad) تأخذ وسيطاً data من نوع ByteArray وتُعيد قيمة من نوع ByteArray، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:59]

```
60:         if (data.isEmpty()) return data
```
> يختبر شرطاً (if): إن كانت data فارغة (isEmpty)، فيُعيد data كما هي. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:60]

```
61:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:61]

```
62:         val last = data[data.size - 1]
```
> يُعرّف متغيّراً ثابت الإسناد (val) باسم last (الأخير - last) ويُسنِد إليه العنصر ذا الفهرس (حجم data ناقص 1) من المصفوفة data. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:62]

```
63:         val paddingLength = last.toInt() and 0xFF
```
> يُعرّف متغيّراً ثابت الإسناد (val) باسم paddingLength (طول الحشو - paddingLength) ويُسنِد إليه ناتج تحويل last إلى عدد صحيح (toInt) ثم تطبيق العملية الثنائية «و» (and) مع القيمة الحرفية 0xFF. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:63]

```
64:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:64]

```
65:         // Must have at least 1 pad byte and not exceed data length
```
> تعليق: «يجب أن يكون هناك بايت حشو واحد على الأقل وألّا يتجاوز طول البيانات». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:65]

```
66:         if (paddingLength <= 0 || paddingLength > data.size) return data
```
> يختبر شرطاً (if): إن كان paddingLength أصغر من أو يساوي 0 أو أكبر من حجم data، فيُعيد data كما هي. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:66]

```
67:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:67]

```
68:         // Verify PKCS#7: all last N bytes equal to pad length (iOS fix)
```
> تعليق: «التحقّق من PKCS#7: كل البايتات الـ N الأخيرة تساوي طول الحشو (إصلاح iOS)». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:68]

```
69:         val start = data.size - paddingLength
```
> يُعرّف متغيّراً ثابت الإسناد (val) باسم start (البداية - start) ويُسنِد إليه ناتج طرح paddingLength من حجم data. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:69]

```
70:         for (i in start until data.size) {
```
> يبدأ حلقة تكرار (for) بالمتغيّر i من start حتى (until) حجم data دون شموله، ويفتح نطاق جسم الحلقة. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:70]

```
71:             if (data[i] != last) {
```
> يختبر شرطاً (if): إن كان العنصر ذو الفهرس i في data لا يساوي last، ويفتح نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:71]

```
72:                 return data // Invalid padding, return original
```
> يُعيد data كما هي ويُنهي الدالة، مع تعليق: «حشو غير صالح، أعِد الأصل». [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:72]

```
73:             }
```
> إغلاق نطاق كتلة الشرط (if). [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:73]

```
74:         }
```
> إغلاق نطاق حلقة التكرار (for). [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:74]

```
75:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:75]

```
76:         return data.copyOfRange(0, start)
```
> يُعيد نسخة جزئية من المصفوفة data من الفهرس 0 حتى start (copyOfRange) ويُنهي الدالة. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:76]

```
77:     }
```
> إغلاق نطاق دالة unpad. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:77]

```
78: }
```
> إغلاق نطاق الكائن المفرد MessagePadding. [app/src/main/java/com/bitchat/android/protocol/MessagePadding.kt:78]
