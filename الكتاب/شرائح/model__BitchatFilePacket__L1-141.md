# شريحة — app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt (الأسطر 1–141)

```
1: package com.bitchat.android.model
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.model. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:2]

```
3: import java.nio.ByteBuffer
```
> يستورد (import) النوع ByteBuffer من المكتبة java.nio لاستعماله في القراءة والكتابة على ذاكرة بايتات. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:3]

```
4: import java.nio.ByteOrder
```
> يستورد (import) النوع ByteOrder من المكتبة java.nio لتحديد ترتيب البايتات. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:5]

```
6: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:6]

```
7:  * BitchatFilePacket: TLV-encoded file transfer payload for BLE mesh.
```
> تعليق: «حزمة ملف بِتشات (BitchatFilePacket): حمولة نقل ملف مرمَّزة بصيغة TLV لشبكة BLE المتشابكة». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:7]

```
8:  * TLVs:
```
> تعليق: «حقول TLV:». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:8]

```
9:  *  - 0x01: filename (UTF-8)
```
> تعليق: «‏0x01: اسم الملف (بترميز UTF-8)». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:9]

```
10:  *  - 0x02: file size (8 bytes, UInt64)
```
> تعليق: «‏0x02: حجم الملف (٨ بايتات، عدد صحيح موجب UInt64)». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:10]

```
11:  *  - 0x03: mime type (UTF-8)
```
> تعليق: «‏0x03: نوع المايم mime (بترميز UTF-8)». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:11]

```
12:  *  - 0x04: content (bytes) — may appear multiple times for large files
```
> تعليق: «‏0x04: المحتوى (بايتات) — قد يظهر عدة مرات للملفات الكبيرة». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:12]

```
13:  *
```
> تعليق: سطر فارغ داخل كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:13]

```
14:  * Length field for TLV is 2 bytes (UInt16, big-endian) for all TLVs.
```
> تعليق: «حقل الطول في TLV هو ٢ بايت (عدد صحيح موجب UInt16، ترتيب البايت الأكبر أولاً big-endian) لكل حقول TLV». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:14]

```
15:  * For large files, CONTENT is chunked into multiple TLVs of up to 65535 bytes each.
```
> تعليق: «للملفات الكبيرة، يُقسَّم المحتوى CONTENT إلى عدة حقول TLV حجم كل منها حتى ٦٥٥٣٥ بايت». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:15]

```
16:  * Note: The outer BitchatPacket uses version 2 (4-byte payload length), so this
```
> تعليق: «ملاحظة: الحزمة الخارجية BitchatPacket تستعمل الإصدار ٢ (طول حمولة من ٤ بايتات)، لذا هذه». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:16]

```
17:  * TLV payload can exceed 64 KiB even though each TLV value is limited to 65535 bytes.
```
> تعليق: «حمولة TLV يمكن أن تتجاوز ٦٤ كيبي بايت رغم أن قيمة كل TLV محدودة بـ٦٥٥٣٥ بايت». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:17]

```
18:  * Transport-level fragmentation then splits the final packet for BLE MTU.
```
> تعليق: «ثم يقوم التجزيء على مستوى النقل بتقسيم الحزمة النهائية لتناسب وحدة النقل القصوى MTU في BLE». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:18]

```
19:  */
```
> نهاية التعليق التوثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:19]

```
20: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:20]

```
21: data class BitchatFilePacket(
```
> يعرّف صنف بيانات (data class) باسم حزمة ملف بِتشات (BitchatFilePacket) ويبدأ قائمة معاملاته الأساسية. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:21]

```
22:     val fileName: String,
```
> يعرّف خاصية ثابتة باسم اسم الملف (fileName) من نوع نص (String). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:22]

```
23:     val fileSize: Long,
```
> يعرّف خاصية ثابتة باسم حجم الملف (fileSize) من نوع عدد طويل (Long). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:23]

```
24:     val mimeType: String,
```
> يعرّف خاصية ثابتة باسم نوع المايم (mimeType) من نوع نص (String). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:24]

```
25:     val content: ByteArray
```
> يعرّف خاصية ثابتة باسم المحتوى (content) من نوع مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:25]

```
26: ) {
```
> يغلق قائمة معاملات الصنف ويفتح نطاق جسم صنف BitchatFilePacket. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:26]

```
27:     private enum class TLVType(val v: UByte) {
```
> يعرّف صنفاً معدوداً (enum class) خاصاً (private) باسم نوع TLV (TLVType) له خاصية ثابتة باسم القيمة (v) من نوع بايت موجب (UByte). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:27]

```
28:         FILE_NAME(0x01u), FILE_SIZE(0x02u), MIME_TYPE(0x03u), CONTENT(0x04u);
```
> يعرّف عناصر المعدود: اسم الملف (FILE_NAME) بقيمة 0x01، وحجم الملف (FILE_SIZE) بقيمة 0x02، ونوع المايم (MIME_TYPE) بقيمة 0x03، والمحتوى (CONTENT) بقيمة 0x04. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:28]

```
29:         companion object { fun from(value: UByte) = values().find { it.v == value } }
```
> يعرّف كائناً مرافقاً (companion object) فيه دالة باسم from تأخذ قيمة (value) من نوع UByte وتعيد أول عنصر معدود قيمته v تساوي القيمة المعطاة. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:29]

```
30:     }
```
> إغلاق نطاق الصنف المعدود TLVType. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:30]

```
31: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:31]

```
32:     fun encode(): ByteArray? {
```
> يعرّف دالة باسم ترميز (encode) لا تأخذ معاملات وتعيد مصفوفة بايتات (ByteArray) قد تكون فارغة (nullable). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:32]

```
33:         try {
```
> يفتح كتلة محاولة (try) لالتقاط الاستثناءات. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:33]

```
34:             android.util.Log.d("BitchatFilePacket", "🔄 Encoding: name=$fileName, size=$fileSize, mime=$mimeType")
```
> يسجّل رسالة تنقيح (Log.d) بالوسم "BitchatFilePacket" تطبع بداية الترميز مع اسم الملف وحجمه ونوع مايمه. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:34]

```
35:         val nameBytes = fileName.toByteArray(Charsets.UTF_8)
```
> يحوّل اسم الملف إلى مصفوفة بايتات بترميز UTF-8 ويخزّنها في متغيّر ثابت باسم بايتات الاسم (nameBytes). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:35]

```
36:         val mimeBytes = mimeType.toByteArray(Charsets.UTF_8)
```
> يحوّل نوع المايم إلى مصفوفة بايتات بترميز UTF-8 ويخزّنها في متغيّر ثابت باسم بايتات المايم (mimeBytes). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:36]

```
37:         // Validate bounds for 2-byte TLV lengths (per-TLV). CONTENT may exceed 65535 and will be chunked.
```
> تعليق: «التحقّق من الحدود لأطوال TLV ذات البايتين (لكل TLV). المحتوى CONTENT قد يتجاوز ٦٥٥٣٥ وسيُقسَّم». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:37]

```
38:         if (nameBytes.size > 0xFFFF || mimeBytes.size > 0xFFFF) {
```
> يفحص شرطاً: إن كان حجم بايتات الاسم أو حجم بايتات المايم أكبر من 0xFFFF (٦٥٥٣٥). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:38]

```
39:                 android.util.Log.e("BitchatFilePacket", "❌ TLV field too large: name=${nameBytes.size}, mime=${mimeBytes.size} (max: 65535)")
```
> يسجّل رسالة خطأ (Log.e) تفيد بأن حقل TLV كبير جداً مع طباعة حجم بايتات الاسم وبايتات المايم والحدّ الأقصى ٦٥٥٣٥. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:39]

```
40:                 return null
```
> يعيد قيمة فارغة (null) لإنهاء الدالة بسبب تجاوز الحجم. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:40]

```
41:             }
```
> إغلاق نطاق كتلة الشرط if. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:41]

```
42:             if (content.size > 0xFFFF) {
```
> يفحص شرطاً: إن كان حجم المحتوى أكبر من 0xFFFF (٦٥٥٣٥). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:42]

```
43:                 android.util.Log.d("BitchatFilePacket", "📦 Content exceeds 65535 bytes (${content.size}); will be split into multiple CONTENT TLVs")
```
> يسجّل رسالة تنقيح (Log.d) تفيد بأن المحتوى يتجاوز ٦٥٥٣٥ بايت مع طباعة حجمه، وأنه سيُقسَّم إلى عدة حقول CONTENT TLV. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:43]

```
44:             } else {
```
> يغلق كتلة if ويفتح كتلة وإلّا (else). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:44]

```
45:                 android.util.Log.d("BitchatFilePacket", "📏 TLV sizes OK: name=${nameBytes.size}, mime=${mimeBytes.size}, content=${content.size}")
```
> يسجّل رسالة تنقيح (Log.d) تفيد بأن أحجام TLV سليمة مع طباعة أحجام بايتات الاسم وبايتات المايم والمحتوى. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:45]

```
46:             }
```
> إغلاق نطاق كتلة else. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:46]

```
47:         val sizeFieldLen = 4 // UInt32 for FILE_SIZE (changed from 8 bytes)
```
> يعرّف متغيّراً ثابتاً باسم طول حقل الحجم (sizeFieldLen) بقيمة ٤، مع تعليق: «‏UInt32 لحقل FILE_SIZE (تغيّر من ٨ بايتات)». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:47]

```
48:         val contentLenFieldLen = 4 // UInt32 for CONTENT TLV as requested
```
> يعرّف متغيّراً ثابتاً باسم طول حقل طول المحتوى (contentLenFieldLen) بقيمة ٤، مع تعليق: «‏UInt32 لحقل CONTENT TLV حسب الطلب». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:48]

```
49: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:49]

```
50:         // Compute capacity: header TLVs + single CONTENT TLV with 4-byte length
```
> تعليق: «حساب السعة: حقول TLV للترويسة + حقل CONTENT TLV واحد بطول من ٤ بايتات». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:50]

```
51:         val contentTLVBytes = 1 + contentLenFieldLen + content.size
```
> يعرّف متغيّراً ثابتاً باسم بايتات حقل المحتوى (contentTLVBytes) بقيمة جمع ١ (بايت النوع) وطول حقل طول المحتوى وحجم المحتوى. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:51]

```
52:         val capacity = (1 + 2 + nameBytes.size) + (1 + 2 + sizeFieldLen) + (1 + 2 + mimeBytes.size) + contentTLVBytes
```
> يعرّف متغيّراً ثابتاً باسم السعة (capacity) يساوي مجموع أطوال حقول الاسم والحجم والمايم (كلٌّ ١ بايت نوع + ٢ بايت طول + بياناته) مضافاً إليها بايتات حقل المحتوى. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:52]

```
53:         val buf = ByteBuffer.allocate(capacity).order(ByteOrder.BIG_ENDIAN)
```
> يعرّف متغيّراً ثابتاً باسم الموقّت (buf) بإنشاء مخزن بايتات ByteBuffer بحجم السعة وترتيب بايت أكبر أولاً (BIG_ENDIAN). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:53]

```
54: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:54]

```
55:         // FILE_NAME
```
> تعليق: «اسم الملف FILE_NAME». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:55]

```
56:         buf.put(TLVType.FILE_NAME.v.toByte())
```
> يكتب في المخزن buf بايت نوع عنصر FILE_NAME (0x01) بعد تحويله إلى بايت. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:56]

```
57:         buf.putShort(nameBytes.size.toShort())
```
> يكتب في المخزن buf حجم بايتات الاسم كعدد قصير (Short) من بايتين. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:57]

```
58:         buf.put(nameBytes)
```
> يكتب في المخزن buf بايتات الاسم نفسها. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:58]

```
59: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:59]

```
60:         // FILE_SIZE (4 bytes)
```
> تعليق: «حجم الملف FILE_SIZE (٤ بايتات)». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:60]

```
61:         buf.put(TLVType.FILE_SIZE.v.toByte())
```
> يكتب في المخزن buf بايت نوع عنصر FILE_SIZE (0x02) بعد تحويله إلى بايت. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:61]

```
62:         buf.putShort(sizeFieldLen.toShort())
```
> يكتب في المخزن buf طول حقل الحجم (٤) كعدد قصير (Short) من بايتين. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:62]

```
63:         buf.putInt(fileSize.toInt())
```
> يكتب في المخزن buf حجم الملف بعد تحويله إلى عدد صحيح (Int) من ٤ بايتات. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:63]

```
64: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:64]

```
65:         // MIME_TYPE
```
> تعليق: «نوع المايم MIME_TYPE». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:65]

```
66:         buf.put(TLVType.MIME_TYPE.v.toByte())
```
> يكتب في المخزن buf بايت نوع عنصر MIME_TYPE (0x03) بعد تحويله إلى بايت. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:66]

```
67:         buf.putShort(mimeBytes.size.toShort())
```
> يكتب في المخزن buf حجم بايتات المايم كعدد قصير (Short) من بايتين. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:67]

```
68:         buf.put(mimeBytes)
```
> يكتب في المخزن buf بايتات المايم نفسها. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:68]

```
69: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:69]

```
70:         // CONTENT (single TLV with 4-byte length)
```
> تعليق: «المحتوى CONTENT (حقل TLV واحد بطول من ٤ بايتات)». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:70]

```
71:         buf.put(TLVType.CONTENT.v.toByte())
```
> يكتب في المخزن buf بايت نوع عنصر CONTENT (0x04) بعد تحويله إلى بايت. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:71]

```
72:         buf.putInt(content.size)
```
> يكتب في المخزن buf حجم المحتوى كعدد صحيح (Int) من ٤ بايتات. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:72]

```
73:         buf.put(content)
```
> يكتب في المخزن buf بايتات المحتوى نفسها. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:73]

```
74: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:74]

```
75:         val result = buf.array()
```
> يعرّف متغيّراً ثابتاً باسم النتيجة (result) بقيمة مصفوفة البايتات المخزّنة في buf. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:75]

```
76:             android.util.Log.d("BitchatFilePacket", "✅ Encoded successfully: ${result.size} bytes total")
```
> يسجّل رسالة تنقيح (Log.d) تفيد بنجاح الترميز مع طباعة حجم النتيجة بالبايت. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:76]

```
77:             return result
```
> يعيد مصفوفة البايتات الناتجة من الدالة. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:77]

```
78:         } catch (e: Exception) {
```
> يغلق كتلة المحاولة try ويفتح كتلة التقاط (catch) لأي استثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:78]

```
79:             android.util.Log.e("BitchatFilePacket", "❌ Encoding failed: ${e.message}", e)
```
> يسجّل رسالة خطأ (Log.e) تفيد بفشل الترميز مع طباعة رسالة الاستثناء وتمرير الاستثناء e. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:79]

```
80:             return null
```
> يعيد قيمة فارغة (null) من الدالة عند حدوث استثناء. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:80]

```
81:         }
```
> إغلاق نطاق كتلة الالتقاط catch. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:81]

```
82:     }
```
> إغلاق نطاق دالة encode. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:82]

```
83: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:83]

```
84:     companion object {
```
> يفتح كائناً مرافقاً (companion object) للصنف. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:84]

```
85:         fun decode(data: ByteArray): BitchatFilePacket? {
```
> يعرّف دالة باسم فكّ الترميز (decode) تأخذ معامل البيانات (data) من نوع مصفوفة بايتات وتعيد حزمة BitchatFilePacket قد تكون فارغة (nullable). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:85]

```
86:             android.util.Log.d("BitchatFilePacket", "🔄 Decoding ${data.size} bytes")
```
> يسجّل رسالة تنقيح (Log.d) تفيد ببدء فكّ الترميز مع طباعة حجم البيانات بالبايت. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:86]

```
87:             try {
```
> يفتح كتلة محاولة (try) لالتقاط الاستثناءات. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:87]

```
88:                 var off = 0
```
> يعرّف متغيّراً متغيّر القيمة باسم الإزاحة (off) بقيمة ابتدائية ٠. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:88]

```
89:                 var name: String? = null
```
> يعرّف متغيّراً متغيّر القيمة باسم الاسم (name) من نوع نص قد يكون فارغاً بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:89]

```
90:                 var size: Long? = null
```
> يعرّف متغيّراً متغيّر القيمة باسم الحجم (size) من نوع عدد طويل قد يكون فارغاً بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:90]

```
91:                 var mime: String? = null
```
> يعرّف متغيّراً متغيّر القيمة باسم المايم (mime) من نوع نص قد يكون فارغاً بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:91]

```
92:                 var contentBytes: ByteArray? = null
```
> يعرّف متغيّراً متغيّر القيمة باسم بايتات المحتوى (contentBytes) من نوع مصفوفة بايتات قد تكون فارغة بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:92]

```
93:                 while (off + 3 <= data.size) { // minimum TLV header size (type + 2 bytes length)
```
> يفتح حلقة طالما (while) تستمر ما دامت الإزاحة زائد ٣ أصغر من أو تساوي حجم البيانات، مع تعليق: «أصغر حجم ترويسة TLV (نوع + ٢ بايت طول)». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:93]

```
94:                     val t = TLVType.from(data[off].toUByte()) ?: return null
```
> يعرّف متغيّراً ثابتاً باسم النوع (t) من نتيجة دالة from على البايت عند الإزاحة بعد تحويله إلى UByte، ويعيد null إن لم يُطابِق أي نوع. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:94]

```
95:                     off += 1
```
> يزيد الإزاحة off بمقدار ١ (تجاوز بايت النوع). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:95]

```
96:                     // CONTENT uses 4-byte length; others use 2-byte length
```
> تعليق: «المحتوى CONTENT يستعمل طولاً من ٤ بايتات؛ والباقي يستعمل طولاً من ٢ بايت». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:96]

```
97:                     val len: Int
```
> يعرّف متغيّراً ثابتاً باسم الطول (len) من نوع عدد صحيح (Int) دون إسناد قيمة بعد. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:97]

```
98:                     if (t == TLVType.CONTENT) {
```
> يفحص شرطاً: إن كان النوع t يساوي عنصر CONTENT. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:98]

```
99:                         if (off + 4 > data.size) return null
```
> يفحص شرطاً: إن كانت الإزاحة زائد ٤ أكبر من حجم البيانات فيعيد null. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:99]

```
100:                         len = ((data[off].toInt() and 0xFF) shl 24) or ((data[off + 1].toInt() and 0xFF) shl 16) or ((data[off + 2].toInt() and 0xFF) shl 8) or (data[off + 3].toInt() and 0xFF)
```
> يسند للطول len قيمة مجمّعة من أربعة بايتات بترتيب بايت أكبر أولاً عبر الإزاحة والدمج بعمليات shl و or. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:100]

```
101:                         off += 4
```
> يزيد الإزاحة off بمقدار ٤ (تجاوز حقل الطول من ٤ بايتات). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:101]

```
102:                     } else {
```
> يغلق كتلة if ويفتح كتلة وإلّا (else). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:102]

```
103:                         if (off + 2 > data.size) return null
```
> يفحص شرطاً: إن كانت الإزاحة زائد ٢ أكبر من حجم البيانات فيعيد null. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:103]

```
104:                         len = ((data[off].toInt() and 0xFF) shl 8) or (data[off + 1].toInt() and 0xFF)
```
> يسند للطول len قيمة مجمّعة من بايتين بترتيب بايت أكبر أولاً عبر الدمج بعمليات shl و or. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:104]

```
105:                         off += 2
```
> يزيد الإزاحة off بمقدار ٢ (تجاوز حقل الطول من ٢ بايت). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:105]

```
106:                     }
```
> إغلاق نطاق كتلة else. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:106]

```
107:                     if (len < 0 || off + len > data.size) return null
```
> يفحص شرطاً: إن كان الطول len سالباً أو إن كانت الإزاحة زائد الطول أكبر من حجم البيانات فيعيد null. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:107]

```
108:                     val value = data.copyOfRange(off, off + len)
```
> يعرّف متغيّراً ثابتاً باسم القيمة (value) بنسخ مدى من البيانات من الإزاحة off إلى off زائد len. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:108]

```
109:                     off += len
```
> يزيد الإزاحة off بمقدار الطول len (تجاوز قيمة الحقل). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:109]

```
110:                     when (t) {
```
> يفتح تعبير مطابقة (when) على النوع t. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:110]

```
111:                         TLVType.FILE_NAME -> name = String(value, Charsets.UTF_8)
```
> في حالة النوع FILE_NAME يسند للاسم name نصاً مبنياً من القيمة value بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:111]

```
112:                         TLVType.FILE_SIZE -> {
```
> يبدأ حالة النوع FILE_SIZE ويفتح كتلتها. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:112]

```
113:                             if (len != 4) return null
```
> يفحص شرطاً: إن كان الطول len لا يساوي ٤ فيعيد null. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:113]

```
114:                             val bb = ByteBuffer.wrap(value).order(ByteOrder.BIG_ENDIAN)
```
> يعرّف متغيّراً ثابتاً باسم bb بلفّ القيمة value في مخزن ByteBuffer بترتيب بايت أكبر أولاً (BIG_ENDIAN). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:114]

```
115:                             size = bb.int.toLong()
```
> يسند للحجم size قيمة العدد الصحيح المقروء من bb بعد تحويله إلى عدد طويل (Long). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:115]

```
116:                         }
```
> إغلاق نطاق كتلة حالة FILE_SIZE. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:116]

```
117:                         TLVType.MIME_TYPE -> mime = String(value, Charsets.UTF_8)
```
> في حالة النوع MIME_TYPE يسند للمايم mime نصاً مبنياً من القيمة value بترميز UTF-8. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:117]

```
118:                         TLVType.CONTENT -> {
```
> يبدأ حالة النوع CONTENT ويفتح كتلتها. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:118]

```
119:                             // Expect a single CONTENT TLV
```
> تعليق: «من المتوقّع حقل CONTENT TLV واحد». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:119]

```
120:                             if (contentBytes == null) contentBytes = value else {
```
> يفحص شرطاً: إن كانت بايتات المحتوى contentBytes فارغة فيسندها إلى value، وإلّا يفتح كتلة else. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:120]

```
121:                                 // If multiple CONTENT TLVs appear, concatenate for tolerance
```
> تعليق: «إن ظهرت عدة حقول CONTENT TLV، تُلصَق ببعضها تسامحاً». [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:121]

```
122:                                 contentBytes = (contentBytes!! + value)
```
> يسند لبايتات المحتوى contentBytes نتيجة لصق بايتات المحتوى الحالية (مع تأكيد عدم فراغها) مع القيمة value. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:122]

```
123:                             }
```
> إغلاق نطاق كتلة else الخاصة بحالة CONTENT. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:123]

```
124:                         }
```
> إغلاق نطاق كتلة حالة CONTENT. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:124]

```
125:                     }
```
> إغلاق نطاق تعبير المطابقة when. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:125]

```
126:                 }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:126]

```
127:                 val n = name ?: return null
```
> يعرّف متغيّراً ثابتاً باسم n يساوي الاسم name، أو يعيد null إن كان الاسم فارغاً. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:127]

```
128:                 val c = contentBytes ?: return null
```
> يعرّف متغيّراً ثابتاً باسم c يساوي بايتات المحتوى contentBytes، أو يعيد null إن كانت فارغة. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:128]

```
129:                 val s = size ?: c.size.toLong()
```
> يعرّف متغيّراً ثابتاً باسم s يساوي الحجم size، أو حجم c بعد تحويله إلى عدد طويل إن كان الحجم فارغاً. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:129]

```
130:                 val m = mime ?: "application/octet-stream"
```
> يعرّف متغيّراً ثابتاً باسم m يساوي المايم mime، أو النص "application/octet-stream" إن كان المايم فارغاً. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:130]

```
131:                 val result = BitchatFilePacket(n, s, m, c)
```
> يعرّف متغيّراً ثابتاً باسم النتيجة (result) بإنشاء حزمة BitchatFilePacket من الاسم n والحجم s والمايم m والمحتوى c. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:131]

```
132:                 android.util.Log.d("BitchatFilePacket", "✅ Decoded: name=$n, size=$s, mime=$m, content=${c.size} bytes")
```
> يسجّل رسالة تنقيح (Log.d) تفيد بنجاح فكّ الترميز مع طباعة الاسم n والحجم s والمايم m وحجم المحتوى c بالبايت. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:132]

```
133:                 return result
```
> يعيد حزمة BitchatFilePacket الناتجة من الدالة. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:133]

```
134:             } catch (e: Exception) {
```
> يغلق كتلة المحاولة try ويفتح كتلة التقاط (catch) لأي استثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:134]

```
135:                 android.util.Log.e("BitchatFilePacket", "❌ Decoding failed: ${e.message}", e)
```
> يسجّل رسالة خطأ (Log.e) تفيد بفشل فكّ الترميز مع طباعة رسالة الاستثناء وتمرير الاستثناء e. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:135]

```
136:                 return null
```
> يعيد قيمة فارغة (null) من الدالة عند حدوث استثناء. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:136]

```
137:             }
```
> إغلاق نطاق كتلة الالتقاط catch. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:137]

```
138:         }
```
> إغلاق نطاق دالة decode. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:138]

```
139:     }
```
> إغلاق نطاق الكائن المرافق companion object. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:139]

```
140: }
```
> إغلاق نطاق صنف BitchatFilePacket. [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:140]

```
141: 
```
> سطر فارغ (نهاية الملف). [app/src/main/java/com/bitchat/android/model/BitchatFilePacket.kt:141]
