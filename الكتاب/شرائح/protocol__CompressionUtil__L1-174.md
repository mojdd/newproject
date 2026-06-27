# شريحة — app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt (الأسطر 1–174)

```
1: package com.bitchat.android.protocol
```
> يعلن الحزمة (package) التي ينتمي إليها الملف باسم «com.bitchat.android.protocol». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:2]

```
3: import android.util.Log
```
> يستورد صنف التسجيل (Log) من حزمة «android.util». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:3]

```
4: import java.io.ByteArrayOutputStream
```
> يستورد صنف مجرى الإخراج إلى مصفوفة بايتات (ByteArrayOutputStream) من حزمة «java.io». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:4]

```
5: import java.util.zip.Deflater
```
> يستورد صنف الضاغط (Deflater) من حزمة «java.util.zip». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:5]

```
6: import java.util.zip.Inflater
```
> يستورد صنف فاكّ الضغط (Inflater) من حزمة «java.util.zip». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:6]

```
7: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:7]

```
8: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:8]

```
9:  * Compression utilities - 100% iOS-compatible zlib implementation
```
> تعليق: «أدوات ضغط - تطبيق zlib متوافق ١٠٠٪ مع iOS». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:9]

```
10:  * Uses the same zlib algorithm as iOS CompressionUtil.swift
```
> تعليق: «يستعمل نفس خوارزمية zlib المستعملة في CompressionUtil.swift على iOS». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:10]

```
11:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:11]

```
12: object CompressionUtil {
```
> يعرّف كائناً مفرداً (object) باسم أداة الضغط (CompressionUtil) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:12]

```
13:     private const val COMPRESSION_THRESHOLD = com.bitchat.android.util.AppConstants.Protocol.COMPRESSION_THRESHOLD_BYTES  // bytes - same as iOS
```
> يعرّف ثابتاً خاصاً باسم عتبة الضغط (COMPRESSION_THRESHOLD) وتُسنَد إليه قيمة «AppConstants.Protocol.COMPRESSION_THRESHOLD_BYTES» من حزمة «com.bitchat.android.util»، مع تعليق: «بايتات - نفس iOS». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:13]

```
14:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:14]

```
15:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:15]

```
16:      * Helper to check if compression is worth it - exact same logic as iOS
```
> تعليق: «مساعد للتحقق إن كان الضغط يستحق - نفس منطق iOS بالضبط». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:16]

```
17:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:17]

```
18:     fun shouldCompress(data: ByteArray): Boolean {
```
> يعرّف دالة «هل ينبغي الضغط» (shouldCompress) التي تأخذ وسيطاً «data» من نوع مصفوفة بايتات (ByteArray) وتعيد قيمة منطقية (Boolean) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:18]

```
19:         // Don't compress if:
```
> تعليق: «لا تضغط إذا:». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:19]

```
20:         // 1. Data is too small
```
> تعليق: «١. البيانات صغيرة جداً». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:20]

```
21:         // 2. Data appears to be already compressed (high entropy)
```
> تعليق: «٢. تبدو البيانات مضغوطة سلفاً (عشوائية عالية)». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:21]

```
22:         if (data.size < COMPRESSION_THRESHOLD) return false
```
> يعيد القيمة المنطقية «false» إن كان حجم «data» أصغر من عتبة الضغط (COMPRESSION_THRESHOLD). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:22]

```
23:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:23]

```
24:         // Simple entropy check - count unique bytes (exact same as iOS)
```
> تعليق: «فحص عشوائية بسيط - عدّ البايتات الفريدة (نفس iOS بالضبط)». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:24]

```
25:         val byteFrequency = mutableMapOf<Byte, Int>()
```
> يعرّف متغيراً ثابت المرجع باسم تردد البايتات (byteFrequency) ويُسنِد إليه خريطة قابلة للتعديل مفاتيحها من نوع بايت (Byte) وقيمها من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:25]

```
26:         for (byte in data) {
```
> يبدأ حلقة تكرارية تمر على كل عنصر «byte» في «data» ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:26]

```
27:             byteFrequency[byte] = (byteFrequency[byte] ?: 0) + 1
```
> يضبط قيمة المفتاح «byte» في خريطة تردد البايتات (byteFrequency) لتساوي قيمتها الحالية (أو صفر إن كانت غير موجودة) مضافاً إليها واحد. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:27]

```
28:         }
```
> إغلاق نطاق الحلقة التكرارية. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:28]

```
29:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:29]

```
30:         // If we have very high byte diversity, data is likely already compressed
```
> تعليق: «إن كان تنوّع البايتات عالياً جداً، فالبيانات على الأرجح مضغوطة سلفاً». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:30]

```
31:         val uniqueByteRatio = byteFrequency.size.toDouble() / minOf(data.size, 256).toDouble()
```
> يعرّف متغيراً باسم نسبة البايتات الفريدة (uniqueByteRatio) ويُسنِد إليه ناتج قسمة حجم خريطة تردد البايتات (كعدد عشري) على أصغر القيمتين بين حجم «data» والعدد ٢٥٦ (كعدد عشري). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:31]

```
32:         return uniqueByteRatio < 0.9 // Compress if less than 90% unique bytes
```
> يعيد نتيجة المقارنة المنطقية «نسبة البايتات الفريدة (uniqueByteRatio) أصغر من ٠٫٩»، مع تعليق: «اضغط إن كان أقل من ٩٠٪ بايتات فريدة». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:32]

```
33:     }
```
> إغلاق نطاق دالة «هل ينبغي الضغط» (shouldCompress). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:33]

```
34:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:34]

```
35:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:35]

```
36:      * Compress data using deflate algorithm - exact same as iOS
```
> تعليق: «اضغط البيانات باستعمال خوارزمية deflate - نفس iOS بالضبط». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:36]

```
37:      * iOS COMPRESSION_ZLIB actually produces raw deflate data (no zlib headers)
```
> تعليق: «COMPRESSION_ZLIB على iOS ينتج فعلياً بيانات deflate خام (بلا ترويسات zlib)». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:37]

```
38:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:38]

```
39:     fun compress(data: ByteArray): ByteArray? {
```
> يعرّف دالة «الضغط» (compress) التي تأخذ وسيطاً «data» من نوع مصفوفة بايتات (ByteArray) وتعيد مصفوفة بايتات قابلة لأن تكون فارغة (ByteArray?) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:39]

```
40:         // Skip compression for small data
```
> تعليق: «تخطَّ الضغط للبيانات الصغيرة». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:40]

```
41:         if (data.size < COMPRESSION_THRESHOLD) return null
```
> يعيد القيمة الفارغة «null» إن كان حجم «data» أصغر من عتبة الضغط (COMPRESSION_THRESHOLD). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:41]

```
42:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:42]

```
43:         try {
```
> يبدأ كتلة محاولة (try) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:43]

```
44:             // Use raw deflate format (no headers) to match iOS COMPRESSION_ZLIB behavior
```
> تعليق: «استعمل صيغة deflate الخام (بلا ترويسات) لمطابقة سلوك COMPRESSION_ZLIB على iOS». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:44]

```
45:             val deflater = Deflater(Deflater.DEFAULT_COMPRESSION, true) // true = raw deflate, no headers
```
> يعرّف متغيراً باسم الضاغط (deflater) ويُسنِد إليه كائن ضاغط (Deflater) منشأ بمستوى الضغط الافتراضي «Deflater.DEFAULT_COMPRESSION» والقيمة المنطقية «true»، مع تعليق: «true = deflate خام، بلا ترويسات». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:45]

```
46:             deflater.setInput(data)
```
> يستدعي على الضاغط (deflater) دالة «ضبط المدخل» (setInput) ممرّراً إليها «data». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:46]

```
47:             deflater.finish()
```
> يستدعي على الضاغط (deflater) دالة «الإنهاء» (finish). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:47]

```
48:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:48]

```
49:             val outputStream = ByteArrayOutputStream(data.size)
```
> يعرّف متغيراً باسم مجرى الإخراج (outputStream) ويُسنِد إليه كائن مجرى إخراج إلى مصفوفة بايتات (ByteArrayOutputStream) منشأ بسعة مبدئية تساوي حجم «data». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:49]

```
50:             val buffer = ByteArray(1024)
```
> يعرّف متغيراً باسم الذاكرة الوسيطة (buffer) ويُسنِد إليه مصفوفة بايتات حجمها ١٠٢٤. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:50]

```
51:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:51]

```
52:             while (!deflater.finished()) {
```
> يبدأ حلقة «طالما» تستمر ما دامت دالة «انتهى» (finished) على الضاغط (deflater) تعيد «false»، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:52]

```
53:                 val count = deflater.deflate(buffer)
```
> يعرّف متغيراً باسم العدد (count) ويُسنِد إليه ناتج استدعاء دالة «الضغط» (deflate) على الضاغط (deflater) ممرّراً إليها الذاكرة الوسيطة (buffer). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:53]

```
54:                 outputStream.write(buffer, 0, count)
```
> يستدعي على مجرى الإخراج (outputStream) دالة «الكتابة» (write) ممرّراً الذاكرة الوسيطة (buffer) والإزاحة صفر والعدد (count). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:54]

```
55:             }
```
> إغلاق نطاق حلقة «طالما». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:55]

```
56:             deflater.end()
```
> يستدعي على الضاغط (deflater) دالة «الإنهاء وتحرير الموارد» (end). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:56]

```
57:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:57]

```
58:             val compressedData = outputStream.toByteArray()
```
> يعرّف متغيراً باسم البيانات المضغوطة (compressedData) ويُسنِد إليه ناتج استدعاء دالة «التحويل إلى مصفوفة بايتات» (toByteArray) على مجرى الإخراج (outputStream). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:58]

```
59:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:59]

```
60:             // Only return if compression was beneficial (same logic as iOS)
```
> تعليق: «أعِد فقط إن كان الضغط مفيداً (نفس منطق iOS)». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:60]

```
61:             return if (compressedData.size > 0 && compressedData.size < data.size) {
```
> يبدأ تعبير إعادة شرطياً بشرط «حجم البيانات المضغوطة (compressedData) أكبر من صفر وأصغر من حجم data» ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:61]

```
62:                 compressedData
```
> قيمة الفرع الموجب: البيانات المضغوطة (compressedData). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:62]

```
63:             } else {
```
> يغلق نطاق الفرع الموجب ويبدأ فرع «وإلا» ويفتح نطاقه. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:63]

```
64:                 null
```
> قيمة فرع «وإلا»: القيمة الفارغة «null». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:64]

```
65:             }
```
> إغلاق نطاق فرع «وإلا» في تعبير الإعادة الشرطي. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:65]

```
66:         } catch (e: Exception) {
```
> يغلق نطاق كتلة المحاولة ويبدأ كتلة التقاط (catch) تمسك استثناءً «e» من نوع استثناء (Exception) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:66]

```
67:             return null
```
> يعيد القيمة الفارغة «null». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:67]

```
68:         }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:68]

```
69:     }
```
> إغلاق نطاق دالة «الضغط» (compress). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:69]

```
70:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:70]

```
71:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:71]

```
72:      * Decompress deflate compressed data - exact same as iOS
```
> تعليق: «فكّ ضغط بيانات deflate المضغوطة - نفس iOS بالضبط». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:72]

```
73:      * iOS COMPRESSION_ZLIB produces raw deflate data (no headers)
```
> تعليق: «COMPRESSION_ZLIB على iOS ينتج بيانات deflate خام (بلا ترويسات)». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:73]

```
74:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:74]

```
75:     fun decompress(compressedData: ByteArray, originalSize: Int): ByteArray? {
```
> يعرّف دالة «فكّ الضغط» (decompress) التي تأخذ وسيطين «compressedData» من نوع مصفوفة بايتات (ByteArray) و«originalSize» من نوع عدد صحيح (Int) وتعيد مصفوفة بايتات قابلة لأن تكون فارغة (ByteArray?) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:75]

```
76:         // iOS COMPRESSION_ZLIB produces raw deflate format (no headers)
```
> تعليق: «COMPRESSION_ZLIB على iOS ينتج صيغة deflate خام (بلا ترويسات)». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:76]

```
77:         try {
```
> يبدأ كتلة محاولة (try) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:77]

```
78:             val inflater = Inflater(true) // true = raw deflate, no headers
```
> يعرّف متغيراً باسم فاكّ الضغط (inflater) ويُسنِد إليه كائن فاكّ ضغط (Inflater) منشأ بالقيمة المنطقية «true»، مع تعليق: «true = deflate خام، بلا ترويسات». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:78]

```
79:             inflater.setInput(compressedData)
```
> يستدعي على فاكّ الضغط (inflater) دالة «ضبط المدخل» (setInput) ممرّراً إليها البيانات المضغوطة (compressedData). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:79]

```
80:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:80]

```
81:             val decompressedBuffer = ByteArray(originalSize)
```
> يعرّف متغيراً باسم ذاكرة فكّ الضغط الوسيطة (decompressedBuffer) ويُسنِد إليه مصفوفة بايتات حجمها يساوي الحجم الأصلي «originalSize». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:81]

```
82:             val actualSize = inflater.inflate(decompressedBuffer)
```
> يعرّف متغيراً باسم الحجم الفعلي (actualSize) ويُسنِد إليه ناتج استدعاء دالة «فكّ الضغط» (inflate) على فاكّ الضغط (inflater) ممرّراً ذاكرة فكّ الضغط الوسيطة (decompressedBuffer). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:82]

```
83:             inflater.end()
```
> يستدعي على فاكّ الضغط (inflater) دالة «الإنهاء وتحرير الموارد» (end). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:83]

```
84:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:84]

```
85:             // Verify decompressed size matches expected (same validation as iOS)
```
> تعليق: «تحقّق أن حجم فكّ الضغط يطابق المتوقع (نفس تحقق iOS)». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:85]

```
86:             return if (actualSize == originalSize) {
```
> يبدأ تعبير إعادة شرطياً بشرط «الحجم الفعلي (actualSize) يساوي الحجم الأصلي (originalSize)» ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:86]

```
87:                 decompressedBuffer
```
> قيمة الفرع الموجب: ذاكرة فكّ الضغط الوسيطة (decompressedBuffer). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:87]

```
88:             } else if (actualSize > 0) {
```
> يغلق نطاق الفرع السابق ويبدأ فرع «وإلا إن» بشرط «الحجم الفعلي (actualSize) أكبر من صفر» ويفتح نطاقه. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:88]

```
89:                 // Handle case where actual size is different
```
> تعليق: «عالِج الحالة التي يكون فيها الحجم الفعلي مختلفاً». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:89]

```
90:                 decompressedBuffer.copyOfRange(0, actualSize)
```
> قيمة فرع «وإلا إن»: ناتج استدعاء دالة «نسخ مدى» (copyOfRange) على ذاكرة فكّ الضغط الوسيطة (decompressedBuffer) من الموضع صفر إلى الحجم الفعلي (actualSize). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:90]

```
91:             } else {
```
> يغلق نطاق فرع «وإلا إن» ويبدأ فرع «وإلا» ويفتح نطاقه. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:91]

```
92:                 null
```
> قيمة فرع «وإلا»: القيمة الفارغة «null». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:92]

```
93:             }
```
> إغلاق نطاق فرع «وإلا» في تعبير الإعادة الشرطي. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:93]

```
94:         } catch (e: Exception) {
```
> يغلق نطاق كتلة المحاولة ويبدأ كتلة التقاط (catch) تمسك استثناءً «e» من نوع استثناء (Exception) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:94]

```
95:             Log.d("CompressionUtil", "Raw deflate decompression failed: ${e.message}, trying with zlib headers...")
```
> يستدعي دالة التسجيل التشخيصي (Log.d) بالوسم «CompressionUtil» ورسالة «Raw deflate decompression failed: » متبوعةً برسالة الاستثناء «e.message» ثم «, trying with zlib headers...». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:95]

```
96:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:96]

```
97:             // Fallback: try with zlib headers in case of mixed usage
```
> تعليق: «خطة بديلة: جرّب بترويسات zlib تحسّباً لاستعمال مختلط». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:97]

```
98:             try {
```
> يبدأ كتلة محاولة (try) داخلية ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:98]

```
99:                 val inflater = Inflater(false) // false = expect zlib headers
```
> يعرّف متغيراً باسم فاكّ الضغط (inflater) ويُسنِد إليه كائن فاكّ ضغط (Inflater) منشأ بالقيمة المنطقية «false»، مع تعليق: «false = توقّع ترويسات zlib». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:99]

```
100:                 inflater.setInput(compressedData)
```
> يستدعي على فاكّ الضغط (inflater) دالة «ضبط المدخل» (setInput) ممرّراً إليها البيانات المضغوطة (compressedData). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:100]

```
101:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:101]

```
102:                 val decompressedBuffer = ByteArray(originalSize)
```
> يعرّف متغيراً باسم ذاكرة فكّ الضغط الوسيطة (decompressedBuffer) ويُسنِد إليه مصفوفة بايتات حجمها يساوي الحجم الأصلي «originalSize». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:102]

```
103:                 val actualSize = inflater.inflate(decompressedBuffer)
```
> يعرّف متغيراً باسم الحجم الفعلي (actualSize) ويُسنِد إليه ناتج استدعاء دالة «فكّ الضغط» (inflate) على فاكّ الضغط (inflater) ممرّراً ذاكرة فكّ الضغط الوسيطة (decompressedBuffer). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:103]

```
104:                 inflater.end()
```
> يستدعي على فاكّ الضغط (inflater) دالة «الإنهاء وتحرير الموارد» (end). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:104]

```
105:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:105]

```
106:                 return if (actualSize == originalSize) {
```
> يبدأ تعبير إعادة شرطياً بشرط «الحجم الفعلي (actualSize) يساوي الحجم الأصلي (originalSize)» ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:106]

```
107:                     decompressedBuffer
```
> قيمة الفرع الموجب: ذاكرة فكّ الضغط الوسيطة (decompressedBuffer). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:107]

```
108:                 } else if (actualSize > 0) {
```
> يغلق نطاق الفرع السابق ويبدأ فرع «وإلا إن» بشرط «الحجم الفعلي (actualSize) أكبر من صفر» ويفتح نطاقه. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:108]

```
109:                     decompressedBuffer.copyOfRange(0, actualSize)
```
> قيمة فرع «وإلا إن»: ناتج استدعاء دالة «نسخ مدى» (copyOfRange) على ذاكرة فكّ الضغط الوسيطة (decompressedBuffer) من الموضع صفر إلى الحجم الفعلي (actualSize). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:109]

```
110:                 } else {
```
> يغلق نطاق فرع «وإلا إن» ويبدأ فرع «وإلا» ويفتح نطاقه. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:110]

```
111:                     null
```
> قيمة فرع «وإلا»: القيمة الفارغة «null». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:111]

```
112:                 }
```
> إغلاق نطاق فرع «وإلا» في تعبير الإعادة الشرطي الداخلي. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:112]

```
113:             } catch (fallbackException: Exception) {
```
> يغلق نطاق كتلة المحاولة الداخلية ويبدأ كتلة التقاط (catch) تمسك استثناءً «fallbackException» من نوع استثناء (Exception) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:113]

```
114:                 Log.e("CompressionUtil", "Both raw deflate and zlib decompression failed: ${fallbackException.message}")
```
> يستدعي دالة التسجيل الخطئي (Log.e) بالوسم «CompressionUtil» ورسالة «Both raw deflate and zlib decompression failed: » متبوعةً برسالة الاستثناء البديل «fallbackException.message». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:114]

```
115:                 return null
```
> يعيد القيمة الفارغة «null». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:115]

```
116:             }
```
> إغلاق نطاق كتلة الالتقاط الداخلية. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:116]

```
117:         }
```
> إغلاق نطاق كتلة الالتقاط الخارجية. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:117]

```
118:     }
```
> إغلاق نطاق دالة «فكّ الضغط» (decompress). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:118]

```
119:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:119]

```
120:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:120]

```
121:      * Test function to verify deflate compression works correctly
```
> تعليق: «دالة اختبار للتحقق من أن ضغط deflate يعمل بشكل صحيح». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:121]

```
122:      * This can be called during app initialization to ensure compatibility
```
> تعليق: «يمكن استدعاؤها أثناء تهيئة التطبيق لضمان التوافق». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:122]

```
123:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:123]

```
124:     fun testCompression(): Boolean {
```
> يعرّف دالة «اختبار الضغط» (testCompression) التي لا تأخذ وسائط وتعيد قيمة منطقية (Boolean) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:124]

```
125:         try {
```
> يبدأ كتلة محاولة (try) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:125]

```
126:             // Create test data that should compress well (repeating pattern like iOS would use)
```
> تعليق: «أنشئ بيانات اختبار ينبغي أن تنضغط جيداً (نمط متكرر كما يستعمل iOS)». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:126]

```
127:             val testMessage = "This is a test message that should compress well. ".repeat(10)
```
> يعرّف متغيراً باسم رسالة الاختبار (testMessage) ويُسنِد إليه النص «This is a test message that should compress well. » مكرراً عشر مرات عبر دالة «التكرار» (repeat). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:127]

```
128:             val originalData = testMessage.toByteArray()
```
> يعرّف متغيراً باسم البيانات الأصلية (originalData) ويُسنِد إليه ناتج استدعاء دالة «التحويل إلى مصفوفة بايتات» (toByteArray) على رسالة الاختبار (testMessage). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:128]

```
129:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:129]

```
130:             Log.d("CompressionUtil", "Testing deflate compression with ${originalData.size} bytes")
```
> يستدعي دالة التسجيل التشخيصي (Log.d) بالوسم «CompressionUtil» ورسالة «Testing deflate compression with » متبوعةً بحجم البيانات الأصلية «originalData.size» ثم « bytes». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:130]

```
131:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:131]

```
132:             // Test shouldCompress
```
> تعليق: «اختبر دالة shouldCompress». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:132]

```
133:             val shouldCompress = shouldCompress(originalData)
```
> يعرّف متغيراً محلياً باسم «هل ينبغي الضغط» (shouldCompress) ويُسنِد إليه ناتج استدعاء دالة «هل ينبغي الضغط» (shouldCompress) ممرّراً إليها البيانات الأصلية (originalData). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:133]

```
134:             Log.d("CompressionUtil", "shouldCompress() returned: $shouldCompress")
```
> يستدعي دالة التسجيل التشخيصي (Log.d) بالوسم «CompressionUtil» ورسالة «shouldCompress() returned: » متبوعةً بقيمة المتغير «shouldCompress». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:134]

```
135:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:135]

```
136:             if (!shouldCompress) {
```
> يبدأ شرط «إن» يتحقق حين تكون قيمة المتغير «shouldCompress» تساوي «false» (أي نفيها صحيح) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:136]

```
137:                 Log.e("CompressionUtil", "shouldCompress failed for test data")
```
> يستدعي دالة التسجيل الخطئي (Log.e) بالوسم «CompressionUtil» ورسالة «shouldCompress failed for test data». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:137]

```
138:                 return false
```
> يعيد القيمة المنطقية «false». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:138]

```
139:             }
```
> إغلاق نطاق شرط «إن». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:139]

```
140:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:140]

```
141:             // Test compression
```
> تعليق: «اختبر الضغط». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:141]

```
142:             val compressed = compress(originalData)
```
> يعرّف متغيراً باسم المضغوط (compressed) ويُسنِد إليه ناتج استدعاء دالة «الضغط» (compress) ممرّراً إليها البيانات الأصلية (originalData). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:142]

```
143:             if (compressed == null) {
```
> يبدأ شرط «إن» يتحقق حين تكون قيمة المتغير «compressed» مساوية للقيمة الفارغة «null» ويفتح نطاقه. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:143]

```
144:                 Log.e("CompressionUtil", "Compression failed")
```
> يستدعي دالة التسجيل الخطئي (Log.e) بالوسم «CompressionUtil» ورسالة «Compression failed». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:144]

```
145:                 return false
```
> يعيد القيمة المنطقية «false». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:145]

```
146:             }
```
> إغلاق نطاق شرط «إن». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:146]

```
147:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:147]

```
148:             Log.d("CompressionUtil", "Compressed ${originalData.size} bytes to ${compressed.size} bytes (${(compressed.size.toDouble() / originalData.size * 100).toInt()}%)")
```
> يستدعي دالة التسجيل التشخيصي (Log.d) بالوسم «CompressionUtil» ورسالة تذكر حجم البيانات الأصلية «originalData.size» وحجم المضغوط «compressed.size» ونسبتهما المئوية المحسوبة بقسمة حجم المضغوط (كعدد عشري) على حجم البيانات الأصلية مضروباً في ١٠٠ ومحوّلاً إلى عدد صحيح. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:148]

```
149:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:149]

```
150:             // Test decompression
```
> تعليق: «اختبر فكّ الضغط». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:150]

```
151:             val decompressed = decompress(compressed, originalData.size)
```
> يعرّف متغيراً باسم المفكوك (decompressed) ويُسنِد إليه ناتج استدعاء دالة «فكّ الضغط» (decompress) ممرّراً المضغوط (compressed) وحجم البيانات الأصلية «originalData.size». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:151]

```
152:             if (decompressed == null) {
```
> يبدأ شرط «إن» يتحقق حين تكون قيمة المتغير «decompressed» مساوية للقيمة الفارغة «null» ويفتح نطاقه. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:152]

```
153:                 Log.e("CompressionUtil", "Decompression failed")
```
> يستدعي دالة التسجيل الخطئي (Log.e) بالوسم «CompressionUtil» ورسالة «Decompression failed». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:153]

```
154:                 return false
```
> يعيد القيمة المنطقية «false». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:154]

```
155:             }
```
> إغلاق نطاق شرط «إن». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:155]

```
156:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:156]

```
157:             // Verify data integrity
```
> تعليق: «تحقّق من سلامة البيانات». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:157]

```
158:             val isIdentical = originalData.contentEquals(decompressed)
```
> يعرّف متغيراً باسم «هل متطابق» (isIdentical) ويُسنِد إليه ناتج استدعاء دالة «تساوي المحتوى» (contentEquals) على البيانات الأصلية (originalData) ممرّراً المفكوك (decompressed). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:158]

```
159:             Log.d("CompressionUtil", "Data integrity check: $isIdentical")
```
> يستدعي دالة التسجيل التشخيصي (Log.d) بالوسم «CompressionUtil» ورسالة «Data integrity check: » متبوعةً بقيمة المتغير «isIdentical». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:159]

```
160:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:160]

```
161:             if (!isIdentical) {
```
> يبدأ شرط «إن» يتحقق حين تكون قيمة المتغير «isIdentical» تساوي «false» (أي نفيها صحيح) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:161]

```
162:                 Log.e("CompressionUtil", "Decompressed data doesn't match original")
```
> يستدعي دالة التسجيل الخطئي (Log.e) بالوسم «CompressionUtil» ورسالة «Decompressed data doesn't match original». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:162]

```
163:                 return false
```
> يعيد القيمة المنطقية «false». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:163]

```
164:             }
```
> إغلاق نطاق شرط «إن». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:164]

```
165:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:165]

```
166:             Log.i("CompressionUtil", "✅ deflate compression test PASSED - ready for iOS compatibility")
```
> يستدعي دالة التسجيل المعلوماتي (Log.i) بالوسم «CompressionUtil» ورسالة «✅ deflate compression test PASSED - ready for iOS compatibility». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:166]

```
167:             return true
```
> يعيد القيمة المنطقية «true». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:167]

```
168:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:168]

```
169:         } catch (e: Exception) {
```
> يغلق نطاق كتلة المحاولة ويبدأ كتلة التقاط (catch) تمسك استثناءً «e» من نوع استثناء (Exception) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:169]

```
170:             Log.e("CompressionUtil", "deflate compression test failed: ${e.message}")
```
> يستدعي دالة التسجيل الخطئي (Log.e) بالوسم «CompressionUtil» ورسالة «deflate compression test failed: » متبوعةً برسالة الاستثناء «e.message». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:170]

```
171:             return false
```
> يعيد القيمة المنطقية «false». [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:171]

```
172:         }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:172]

```
173:     }
```
> إغلاق نطاق دالة «اختبار الضغط» (testCompression). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:173]

```
174: }
```
> إغلاق نطاق الكائن المفرد أداة الضغط (CompressionUtil). [app/src/main/java/com/bitchat/android/protocol/CompressionUtil.kt:174]
