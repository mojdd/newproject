# شريحة — app/src/main/java/com/bitchat/android/features/file/FileUtils.kt (الأسطر 1–200)

```
1: package com.bitchat.android.features.file
```
> تُعرَّف حُزمة (package) الملف باسم `com.bitchat.android.features.file`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:2]

```
3: import android.content.Context
```
> يُستورَد الصِّنف `Context` من `android.content`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:3]

```
4: import android.net.Uri
```
> يُستورَد الصِّنف `Uri` (المُعرِّف الموحَّد للمورد) من `android.net`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:4]

```
5: import android.os.Environment
```
> يُستورَد الصِّنف `Environment` من `android.os`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:5]

```
6: import android.util.Log
```
> يُستورَد الصِّنف `Log` (التسجيل) من `android.util`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:6]

```
7: import androidx.core.content.FileProvider
```
> يُستورَد الصِّنف `FileProvider` (مزوِّد الملفات) من `androidx.core.content`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:7]

```
8: import java.io.File
```
> يُستورَد الصِّنف `File` (الملف) من `java.io`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:8]

```
9: import java.io.FileOutputStream
```
> يُستورَد الصِّنف `FileOutputStream` (تيّار إخراج الملف) من `java.io`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:9]

```
10: import java.io.InputStream
```
> يُستورَد الصِّنف `InputStream` (تيّار الإدخال) من `java.io`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:10]

```
11: import java.text.SimpleDateFormat
```
> يُستورَد الصِّنف `SimpleDateFormat` (تنسيق التاريخ البسيط) من `java.text`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:11]

```
12: import java.util.*
```
> تُستورَد كلّ الأصناف من حُزمة `java.util` بالرمز النجمي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:12]

```
13: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:13]

```
14: object FileUtils {
```
> يُعلَن كائن مُفرد (object) باسم `FileUtils` (أدوات الملفات) ويُفتح نطاقه. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:14]

```
15: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:15]

```
16:     private const val TAG = "FileUtils"
```
> يُعرَّف ثابت خاصّ (private const) باسم `TAG` (الوسم) وقيمته السلسلة النصية `"FileUtils"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:17]

```
18:     /**
```
> تعليق توثيقي (بدايته): فتح كتلة تعليق `/**`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:18]

```
19:      * Save a file from URI to app's file directory with unique filename
```
> تعليق: «احفظ ملفاً من المُعرِّف الموحَّد (URI) إلى دليل ملفات التطبيق باسم فريد». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:19]

```
20:      */
```
> تعليق توثيقي (نهايته): إغلاق كتلة التعليق `*/`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:20]

```
21:     fun saveFileFromUri(
```
> تُعرَّف دالّة باسم `saveFileFromUri` (حفظ الملف من المُعرِّف الموحَّد) ويُفتح سرد مُعاملاتها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:21]

```
22:         context: Context,
```
> مُعامل أوّل باسم `context` (السياق) من نوع `Context`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:22]

```
23:         uri: Uri,
```
> مُعامل ثانٍ باسم `uri` من نوع `Uri`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:23]

```
24:         originalName: String? = null
```
> مُعامل ثالث باسم `originalName` (الاسم الأصلي) من نوع سلسلة نصية قابلة لأن تكون فارغة `String?` وقيمته الافتراضية `null`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:24]

```
25:     ): String? {
```
> يُغلَق سرد المُعاملات، ونوع القيمة المُعادة سلسلة نصية قابلة لأن تكون فارغة `String?`، ويُفتح جسم الدالّة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:25]

```
26:         return try {
```
> يُعاد ناتج كتلة `try` (المحاولة) ويُفتح نطاقها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:26]

```
27:             val inputStream = context.contentResolver.openInputStream(uri)
```
> يُعرَّف متغيّر ثابت `inputStream` (تيّار الإدخال) ويُسنَد إليه ناتج استدعاء `context.contentResolver.openInputStream(uri)` لفتح تيّار قراءة من المُعرِّف الموحَّد. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:27]

```
28:             if (inputStream == null) {
```
> شرط `if`: إن كان `inputStream` يساوي `null` يُفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:28]

```
29:                 Log.e(TAG, "❌ Failed to open input stream for URI: $uri")
```
> يُستدعى `Log.e` لتسجيل خطأ بالوسم `TAG` ونصّ «❌ Failed to open input stream for URI: » متبوعاً بقيمة `uri`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:29]

```
30:                 return null
```
> تُعيد الدالّة القيمة `null`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:30]

```
31:             }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:31]

```
32:             Log.d(TAG, "📂 Opened input stream successfully")
```
> يُستدعى `Log.d` لتسجيل رسالة تنقيح (debug) بالوسم `TAG` ونصّ «📂 Opened input stream successfully». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:33]

```
34:             // Determine file extension
```
> تعليق: «حدِّد امتداد الملف». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:34]

```
35:             val extension = originalName?.substringAfterLast(".") ?: "bin"
```
> يُعرَّف متغيّر ثابت `extension` (الامتداد) ويُسنَد إليه ما بعد آخر نقطة في `originalName` عبر `substringAfterLast(".")`، وإن كان `originalName` فارغاً فالقيمة `"bin"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:35]

```
36:             val fileName = "file_${System.currentTimeMillis()}.$extension"
```
> يُعرَّف متغيّر ثابت `fileName` (اسم الملف) ويُسنَد إليه السلسلة `"file_"` متبوعةً بقيمة `System.currentTimeMillis()` (الوقت الحالي بالميلّي ثانية) ثمّ نقطة ثمّ قيمة `extension`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:36]

```
37: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:37]

```
38:             // Create incoming dir if needed
```
> تعليق: «أنشئ دليل الوارد إن لزم». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:38]

```
39:             val incomingDir = File(context.filesDir, "files/incoming").apply {
```
> يُعرَّف متغيّر ثابت `incomingDir` (دليل الوارد) ويُسنَد إليه كائن `File` بالمسار الأب `context.filesDir` والمسار الفرعي `"files/incoming"`، ويُفتح نطاق `apply`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:39]

```
40:                 if (!exists()) mkdirs()
```
> شرط `if`: إن لم يكن الدليل موجوداً `!exists()` يُستدعى `mkdirs()` لإنشاء الأدلّة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:40]

```
41:             }
```
> إغلاق نطاق كتلة `apply`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:41]

```
42: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:42]

```
43:             val file = File(incomingDir, fileName)
```
> يُعرَّف متغيّر ثابت `file` ويُسنَد إليه كائن `File` بالدليل الأب `incomingDir` واسم الملف `fileName`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:43]

```
44: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:44]

```
45:             inputStream.use { input ->
```
> يُستدعى `use` على `inputStream` (يضمن إغلاقه) بمُعامل لامبدا باسم `input`، ويُفتح نطاقه. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:45]

```
46:                 FileOutputStream(file).use { output ->
```
> يُنشأ `FileOutputStream` للملف `file` ويُستدعى `use` عليه (يضمن إغلاقه) بمُعامل لامبدا باسم `output`، ويُفتح نطاقه. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:46]

```
47:                     input.copyTo(output)
```
> يُستدعى `input.copyTo(output)` لنسخ محتوى تيّار الإدخال إلى تيّار الإخراج. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:47]

```
48:                 }
```
> إغلاق نطاق لامبدا `output`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:48]

```
49:             }
```
> إغلاق نطاق لامبدا `input`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:49]

```
50: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:50]

```
51:             Log.d(TAG, "Saved file to: ${file.absolutePath}")
```
> يُستدعى `Log.d` لتسجيل رسالة تنقيح بالوسم `TAG` ونصّ «Saved file to: » متبوعاً بقيمة `file.absolutePath` (المسار المُطلق للملف). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:51]

```
52:             file.absolutePath
```
> القيمة الأخيرة في كتلة `try`: `file.absolutePath`، وهي ما يُعاد. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:52]

```
53: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:53]

```
54:         } catch (e: Exception) {
```
> يُغلَق نطاق `try` وتُفتح كتلة `catch` تلتقط استثناءً باسم `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:54]

```
55:             Log.e(TAG, "Failed to save file from URI", e)
```
> يُستدعى `Log.e` لتسجيل خطأ بالوسم `TAG` ونصّ «Failed to save file from URI» والاستثناء `e`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:55]

```
56:             null
```
> القيمة الأخيرة في كتلة `catch`: `null`، وهي ما يُعاد عند الخطأ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:56]

```
57:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:57]

```
58:     }
```
> إغلاق نطاق دالّة `saveFileFromUri`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:58]

```
59: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:59]

```
60:     /**
```
> تعليق توثيقي (بدايته): فتح كتلة تعليق `/**`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:60]

```
61:      * Copy file to app's outgoing directory for sending
```
> تعليق: «انسخ الملف إلى دليل الصادر في التطبيق لأجل الإرسال». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:61]

```
62:      */
```
> تعليق توثيقي (نهايته): إغلاق كتلة التعليق `*/`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:62]

```
63:     fun copyFileForSending(context: Context, uri: Uri, originalName: String? = null): String? {
```
> تُعرَّف دالّة باسم `copyFileForSending` (نسخ الملف للإرسال) بمُعاملات: `context` من نوع `Context`، و`uri` من نوع `Uri`، و`originalName` من نوع `String?` بقيمة افتراضية `null`، ونوع القيمة المُعادة `String?`، ويُفتح جسمها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:63]

```
64:         Log.d(TAG, "🔄 Starting file copy from URI: $uri")
```
> يُستدعى `Log.d` لتسجيل رسالة تنقيح بالوسم `TAG` ونصّ «🔄 Starting file copy from URI: » متبوعاً بقيمة `uri`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:64]

```
65:         return try {
```
> يُعاد ناتج كتلة `try` ويُفتح نطاقها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:65]

```
66:             val inputStream = context.contentResolver.openInputStream(uri)
```
> يُعرَّف متغيّر ثابت `inputStream` ويُسنَد إليه ناتج `context.contentResolver.openInputStream(uri)` لفتح تيّار قراءة من المُعرِّف الموحَّد. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:66]

```
67:             if (inputStream == null) {
```
> شرط `if`: إن كان `inputStream` يساوي `null` يُفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:67]

```
68:                 Log.e(TAG, "❌ Failed to open input stream for URI: $uri")
```
> يُستدعى `Log.e` لتسجيل خطأ بالوسم `TAG` ونصّ «❌ Failed to open input stream for URI: » متبوعاً بقيمة `uri`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:68]

```
69:                 return null
```
> تُعيد الدالّة القيمة `null`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:69]

```
70:             }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:70]

```
71:             Log.d(TAG, "📂 Opened input stream successfully")
```
> يُستدعى `Log.d` لتسجيل رسالة تنقيح بالوسم `TAG` ونصّ «📂 Opened input stream successfully». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:71]

```
72: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:72]

```
73:             // Determine original filename and extension if available
```
> تعليق: «حدِّد اسم الملف الأصلي وامتداده إن توفّر». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:73]

```
74:             val displayName = originalName ?: run {
```
> يُعرَّف متغيّر ثابت `displayName` (الاسم المعروض) ويُسنَد إليه `originalName`، وإن كان فارغاً فناتج كتلة `run` التي يُفتح نطاقها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:74]

```
75:                 try {
```
> تُفتح كتلة `try`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:75]

```
76:                     context.contentResolver.query(uri, null, null, null, null)?.use { cursor ->
```
> يُستدعى `context.contentResolver.query` على `uri` بمُعاملات `null` خمسة، ثمّ `use` على المؤشّر الناتج (إن لم يكن فارغاً) بمُعامل لامبدا باسم `cursor` (المؤشّر)، ويُفتح نطاقه. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:76]

```
77:                         val nameIndex = cursor.getColumnIndex(android.provider.MediaStore.MediaColumns.DISPLAY_NAME)
```
> يُعرَّف متغيّر ثابت `nameIndex` (فهرس الاسم) ويُسنَد إليه ناتج `cursor.getColumnIndex` للعمود `android.provider.MediaStore.MediaColumns.DISPLAY_NAME`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:77]

```
78:                         if (nameIndex >= 0 && cursor.moveToFirst()) cursor.getString(nameIndex) else null
```
> شرط `if`: إن كان `nameIndex` أكبر من أو يساوي صفراً ونجح `cursor.moveToFirst()` يُعاد `cursor.getString(nameIndex)`، وإلّا `null`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:78]

```
79:                     }
```
> إغلاق نطاق لامبدا `cursor`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:79]

```
80:                 } catch (_: Exception) { null }
```
> تُغلَق كتلة `try` وتُفتح كتلة `catch` تلتقط استثناءً مُهمَل الاسم `_` من نوع `Exception` وتُعيد `null`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:80]

```
81:             }
```
> إغلاق نطاق كتلة `run`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:81]

```
82:             val extension = displayName?.substringAfterLast('.', missingDelimiterValue = "")?.takeIf { it.isNotBlank() }
```
> يُعرَّف متغيّر ثابت `extension` ويُسنَد إليه ما بعد آخر نقطة في `displayName` عبر `substringAfterLast('.', missingDelimiterValue = "")` (القيمة عند غياب الفاصل سلسلة فارغة)، ثمّ `takeIf` تُبقيه فقط إن كان غير فارغ `it.isNotBlank()`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:82]

```
83:                 ?: run {
```
> مُعامل إلفيس `?:`: إن كانت القيمة السابقة فارغة يُؤخَذ ناتج كتلة `run` التي يُفتح نطاقها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:83]

```
84:                     // Try mime type to extension
```
> تعليق: «جرّب تحويل نوع الميديا (mime) إلى امتداد». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:84]

```
85:                     val mime = try { context.contentResolver.getType(uri) } catch (_: Exception) { null }
```
> يُعرَّف متغيّر ثابت `mime` (نوع الميديا) ويُسنَد إليه ناتج `context.contentResolver.getType(uri)` داخل `try`، وعند الاستثناء `null` عبر `catch`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:85]

```
86:                     android.webkit.MimeTypeMap.getSingleton().getExtensionFromMimeType(mime) ?: "bin"
```
> يُستدعى `android.webkit.MimeTypeMap.getSingleton().getExtensionFromMimeType(mime)` لاشتقاق الامتداد من نوع الميديا، وإن كان فارغاً فالقيمة `"bin"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:86]

```
87:                 }
```
> إغلاق نطاق كتلة `run`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:87]

```
88:             // Preserve original filename (without artificial prefixes), ensure uniqueness
```
> تعليق: «احتفظ باسم الملف الأصلي (دون بادئات مصطنعة)، واضمن تفرّده». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:88]

```
89:             val baseName = displayName?.substringBeforeLast('.')?.take(64)?.replace(Regex("[^A-Za-z0-9._-]"), "_")
```
> يُعرَّف متغيّر ثابت `baseName` (الاسم الأساس) ويُسنَد إليه ما قبل آخر نقطة في `displayName` عبر `substringBeforeLast('.')`، ثمّ `take(64)` لأخذ أوّل أربعة وستين محرفاً، ثمّ `replace` باستبدال كلّ محرف لا يطابق التعبير النمطي `[^A-Za-z0-9._-]` بـ `"_"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:89]

```
90:                 ?: "file"
```
> مُعامل إلفيس `?:`: إن كانت القيمة السابقة فارغة فالقيمة `"file"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:90]

```
91:             var fileName = if (extension.isNotBlank()) "$baseName.$extension" else baseName
```
> يُعرَّف متغيّر مُتبدِّل `fileName` ويُسنَد إليه (إن كان `extension` غير فارغ) السلسلة `baseName` ونقطة و`extension`، وإلّا `baseName` وحده. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:91]

```
92: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:92]

```
93:             // Create outgoing dir if needed
```
> تعليق: «أنشئ دليل الصادر إن لزم». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:93]

```
94:             val outgoingDir = File(context.filesDir, "files/outgoing").apply {
```
> يُعرَّف متغيّر ثابت `outgoingDir` (دليل الصادر) ويُسنَد إليه كائن `File` بالمسار الأب `context.filesDir` والمسار الفرعي `"files/outgoing"`، ويُفتح نطاق `apply`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:94]

```
95:                 if (!exists()) mkdirs()
```
> شرط `if`: إن لم يكن الدليل موجوداً `!exists()` يُستدعى `mkdirs()` لإنشاء الأدلّة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:95]

```
96:             }
```
> إغلاق نطاق كتلة `apply`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:96]

```
97: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:97]

```
98:             var target = File(outgoingDir, fileName)
```
> يُعرَّف متغيّر مُتبدِّل `target` (الهدف) ويُسنَد إليه كائن `File` بالدليل الأب `outgoingDir` واسم الملف `fileName`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:98]

```
99:             if (target.exists()) {
```
> شرط `if`: إن كان `target` موجوداً يُفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:99]

```
100:                 var idx = 1
```
> يُعرَّف متغيّر مُتبدِّل `idx` (الفهرس) وقيمته الابتدائية `1`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:100]

```
101:                 val pureBase = baseName
```
> يُعرَّف متغيّر ثابت `pureBase` (الأساس الصافي) ويُسنَد إليه `baseName`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:101]

```
102:                 val dotExt = if (extension.isNotBlank()) ".${extension}" else ""
```
> يُعرَّف متغيّر ثابت `dotExt` (نقطة-الامتداد) ويُسنَد إليه (إن كان `extension` غير فارغ) نقطة متبوعةً بقيمة `extension`، وإلّا سلسلة فارغة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:102]

```
103:                 while (target.exists() && idx < 1000) {
```
> حلقة `while`: تستمرّ ما دام `target` موجوداً و`idx` أصغر من `1000`، ويُفتح نطاقها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:103]

```
104:                     fileName = "$pureBase ($idx)$dotExt"
```
> يُسنَد إلى `fileName` السلسلة `pureBase` متبوعةً بمسافة وقوس مفتوح وقيمة `idx` وقوس مغلق ثمّ `dotExt`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:104]

```
105:                     target = File(outgoingDir, fileName)
```
> يُعاد إسناد `target` إلى كائن `File` جديد بالدليل `outgoingDir` واسم الملف `fileName`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:105]

```
106:                     idx++
```
> يُزاد `idx` بمقدار واحد. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:106]

```
107:                 }
```
> إغلاق نطاق حلقة `while`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:107]

```
108:             }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:108]

```
109: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:109]

```
110:             inputStream.use { input ->
```
> يُستدعى `use` على `inputStream` (يضمن إغلاقه) بمُعامل لامبدا باسم `input`، ويُفتح نطاقه. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:110]

```
111:                 FileOutputStream(target).use { output ->
```
> يُنشأ `FileOutputStream` للهدف `target` ويُستدعى `use` عليه (يضمن إغلاقه) بمُعامل لامبدا باسم `output`، ويُفتح نطاقه. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:111]

```
112:                     input.copyTo(output)
```
> يُستدعى `input.copyTo(output)` لنسخ محتوى تيّار الإدخال إلى تيّار الإخراج. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:112]

```
113:                 }
```
> إغلاق نطاق لامبدا `output`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:113]

```
114:             }
```
> إغلاق نطاق لامبدا `input`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:114]

```
115: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:115]

```
116:             Log.d(TAG, "✅ Successfully copied file for sending: ${target.absolutePath}")
```
> يُستدعى `Log.d` لتسجيل رسالة تنقيح بالوسم `TAG` ونصّ «✅ Successfully copied file for sending: » متبوعاً بقيمة `target.absolutePath`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:116]

```
117:             Log.d(TAG, "📊 Final file size: ${target.length()} bytes")
```
> يُستدعى `Log.d` لتسجيل رسالة تنقيح بالوسم `TAG` ونصّ «📊 Final file size: » متبوعاً بقيمة `target.length()` (حجم الملف) ثمّ كلمة «bytes». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:117]

```
118:             target.absolutePath
```
> القيمة الأخيرة في كتلة `try`: `target.absolutePath`، وهي ما يُعاد. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:118]

```
119: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:119]

```
120:         } catch (e: Exception) {
```
> يُغلَق نطاق `try` وتُفتح كتلة `catch` تلتقط استثناءً باسم `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:120]

```
121:             Log.e(TAG, "❌ CRITICAL: Failed to copy file for sending", e)
```
> يُستدعى `Log.e` لتسجيل خطأ بالوسم `TAG` ونصّ «❌ CRITICAL: Failed to copy file for sending» والاستثناء `e`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:121]

```
122:             Log.e(TAG, "❌ Source URI: $uri")
```
> يُستدعى `Log.e` لتسجيل خطأ بالوسم `TAG` ونصّ «❌ Source URI: » متبوعاً بقيمة `uri`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:122]

```
123:             Log.e(TAG, "❌ Original name: $originalName")
```
> يُستدعى `Log.e` لتسجيل خطأ بالوسم `TAG` ونصّ «❌ Original name: » متبوعاً بقيمة `originalName`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:123]

```
124:             Log.e(TAG, "❌ Error type: ${e.javaClass.simpleName}")
```
> يُستدعى `Log.e` لتسجيل خطأ بالوسم `TAG` ونصّ «❌ Error type: » متبوعاً بقيمة `e.javaClass.simpleName` (الاسم البسيط لصِنف الاستثناء). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:124]

```
125:             null
```
> القيمة الأخيرة في كتلة `catch`: `null`، وهي ما يُعاد عند الخطأ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:125]

```
126:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:126]

```
127:     }
```
> إغلاق نطاق دالّة `copyFileForSending`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:127]

```
128: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:128]

```
129:     /**
```
> تعليق توثيقي (بدايته): فتح كتلة تعليق `/**`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:129]

```
130:      * Get MIME type for a file based on extension
```
> تعليق: «احصل على نوع الميديا (MIME) لملف بناءً على الامتداد». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:130]

```
131:      */
```
> تعليق توثيقي (نهايته): إغلاق كتلة التعليق `*/`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:131]

```
132:     fun getMimeTypeFromExtension(fileName: String): String {
```
> تُعرَّف دالّة باسم `getMimeTypeFromExtension` (الحصول على نوع الميديا من الامتداد) بمُعامل `fileName` من نوع `String`، ونوع القيمة المُعادة `String`، ويُفتح جسمها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:132]

```
133:         return when (fileName.substringAfterLast(".", "").lowercase()) {
```
> يُعاد ناتج تعبير `when` (اختيار) المبني على ما بعد آخر نقطة في `fileName` عبر `substringAfterLast(".", "")` ثمّ `lowercase()` (تحويله لحروف صغيرة)، ويُفتح نطاقه. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:133]

```
134:             "pdf" -> "application/pdf"
```
> فرع `when`: عند `"pdf"` تُعاد `"application/pdf"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:134]

```
135:             "doc" -> "application/msword"
```
> فرع `when`: عند `"doc"` تُعاد `"application/msword"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:135]

```
136:             "docx" -> "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
```
> فرع `when`: عند `"docx"` تُعاد `"application/vnd.openxmlformats-officedocument.wordprocessingml.document"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:136]

```
137:             "xls" -> "application/vnd.ms-excel"
```
> فرع `when`: عند `"xls"` تُعاد `"application/vnd.ms-excel"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:137]

```
138:             "xlsx" -> "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
```
> فرع `when`: عند `"xlsx"` تُعاد `"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:138]

```
139:             "ppt" -> "application/vnd.ms-powerpoint"
```
> فرع `when`: عند `"ppt"` تُعاد `"application/vnd.ms-powerpoint"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:139]

```
140:             "pptx" -> "application/vnd.openxmlformats-officedocument.presentationml.presentation"
```
> فرع `when`: عند `"pptx"` تُعاد `"application/vnd.openxmlformats-officedocument.presentationml.presentation"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:140]

```
141:             "txt" -> "text/plain"
```
> فرع `when`: عند `"txt"` تُعاد `"text/plain"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:141]

```
142:             "json" -> "application/json"
```
> فرع `when`: عند `"json"` تُعاد `"application/json"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:142]

```
143:             "xml" -> "application/xml"
```
> فرع `when`: عند `"xml"` تُعاد `"application/xml"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:143]

```
144:             "csv" -> "text/csv"
```
> فرع `when`: عند `"csv"` تُعاد `"text/csv"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:144]

```
145:             "html", "htm" -> "text/html"
```
> فرع `when`: عند `"html"` أو `"htm"` تُعاد `"text/html"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:145]

```
146:             "jpg", "jpeg" -> "image/jpeg"
```
> فرع `when`: عند `"jpg"` أو `"jpeg"` تُعاد `"image/jpeg"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:146]

```
147:             "png" -> "image/png"
```
> فرع `when`: عند `"png"` تُعاد `"image/png"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:147]

```
148:             "gif" -> "image/gif"
```
> فرع `when`: عند `"gif"` تُعاد `"image/gif"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:148]

```
149:             "bmp" -> "image/bmp"
```
> فرع `when`: عند `"bmp"` تُعاد `"image/bmp"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:149]

```
150:             "webp" -> "image/webp"
```
> فرع `when`: عند `"webp"` تُعاد `"image/webp"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:150]

```
151:             "svg" -> "image/svg+xml"
```
> فرع `when`: عند `"svg"` تُعاد `"image/svg+xml"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:151]

```
152:             "mp3" -> "audio/mpeg"
```
> فرع `when`: عند `"mp3"` تُعاد `"audio/mpeg"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:152]

```
153:             "wav" -> "audio/wav"
```
> فرع `when`: عند `"wav"` تُعاد `"audio/wav"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:153]

```
154:             "m4a" -> "audio/mp4"
```
> فرع `when`: عند `"m4a"` تُعاد `"audio/mp4"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:154]

```
155:             "mp4" -> "video/mp4"
```
> فرع `when`: عند `"mp4"` تُعاد `"video/mp4"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:155]

```
156:             "avi" -> "video/x-msvideo"
```
> فرع `when`: عند `"avi"` تُعاد `"video/x-msvideo"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:156]

```
157:             "mov" -> "video/quicktime"
```
> فرع `when`: عند `"mov"` تُعاد `"video/quicktime"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:157]

```
158:             "zip" -> "application/zip"
```
> فرع `when`: عند `"zip"` تُعاد `"application/zip"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:158]

```
159:             "rar" -> "application/vnd.rar"
```
> فرع `when`: عند `"rar"` تُعاد `"application/vnd.rar"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:159]

```
160:             "7z" -> "application/x-7z-compressed"
```
> فرع `when`: عند `"7z"` تُعاد `"application/x-7z-compressed"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:160]

```
161:             else -> "application/octet-stream"
```
> فرع `when` الافتراضي `else`: تُعاد `"application/octet-stream"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:161]

```
162:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:162]

```
163:     }
```
> إغلاق نطاق دالّة `getMimeTypeFromExtension`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:163]

```
164: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:164]

```
165:     /**
```
> تعليق توثيقي (بدايته): فتح كتلة تعليق `/**`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:165]

```
166:      * Format file size for display
```
> تعليق: «نسِّق حجم الملف للعرض». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:166]

```
167:      */
```
> تعليق توثيقي (نهايته): إغلاق كتلة التعليق `*/`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:167]

```
168:     fun formatFileSize(bytes: Long): String {
```
> تُعرَّف دالّة باسم `formatFileSize` (تنسيق حجم الملف) بمُعامل `bytes` (البايتات) من نوع `Long`، ونوع القيمة المُعادة `String`، ويُفتح جسمها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:168]

```
169:         val units = arrayOf("B", "KB", "MB", "GB")
```
> يُعرَّف متغيّر ثابت `units` (الوحدات) ويُسنَد إليه مصفوفة عبر `arrayOf` تحوي `"B"` و`"KB"` و`"MB"` و`"GB"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:169]

```
170:         var size = bytes.toDouble()
```
> يُعرَّف متغيّر مُتبدِّل `size` (الحجم) ويُسنَد إليه `bytes.toDouble()` (تحويل البايتات إلى عدد عشري). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:170]

```
171:         var unitIndex = 0
```
> يُعرَّف متغيّر مُتبدِّل `unitIndex` (فهرس الوحدة) وقيمته الابتدائية `0`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:171]

```
172:         while (size >= 1024 && unitIndex < units.size - 1) {
```
> حلقة `while`: تستمرّ ما دام `size` أكبر من أو يساوي `1024` و`unitIndex` أصغر من حجم المصفوفة ناقص واحد `units.size - 1`، ويُفتح نطاقها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:172]

```
173:             size /= 1024.0
```
> يُقسَم `size` على `1024.0` ويُسنَد الناتج إليه. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:173]

```
174:             unitIndex++
```
> يُزاد `unitIndex` بمقدار واحد. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:174]

```
175:         }
```
> إغلاق نطاق حلقة `while`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:175]

```
176:         return "%.1f %s".format(size, units[unitIndex])
```
> تُعاد سلسلة منسَّقة عبر `format` على القالب `"%.1f %s"` بقيمتي `size` (عدد عشري بمنزلة واحدة) و`units[unitIndex]` (الوحدة عند الفهرس). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:176]

```
177:     }
```
> إغلاق نطاق دالّة `formatFileSize`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:177]

```
178: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:178]

```
179:     /**
```
> تعليق توثيقي (بدايته): فتح كتلة تعليق `/**`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:179]

```
180:      * Check if file is viewable in system viewer
```
> تعليق: «تحقّق ممّا إذا كان الملف قابلاً للعرض في عارض النظام». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:180]

```
181:      */
```
> تعليق توثيقي (نهايته): إغلاق كتلة التعليق `*/`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:181]

```
182:     fun isFileViewable(fileName: String): Boolean {
```
> تُعرَّف دالّة باسم `isFileViewable` (هل الملف قابل للعرض) بمُعامل `fileName` من نوع `String`، ونوع القيمة المُعادة `Boolean`، ويُفتح جسمها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:182]

```
183:         val extension = fileName.substringAfterLast(".", "").lowercase()
```
> يُعرَّف متغيّر ثابت `extension` ويُسنَد إليه ما بعد آخر نقطة في `fileName` عبر `substringAfterLast(".", "")` ثمّ `lowercase()`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:183]

```
184:         return extension in listOf(
```
> يُعاد ناتج فحص عضوية `extension` ضمن قائمة `listOf` التي يُفتح سردها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:184]

```
185:             "pdf", "txt", "json", "xml", "html", "htm", "csv",
```
> عناصر القائمة: `"pdf"` و`"txt"` و`"json"` و`"xml"` و`"html"` و`"htm"` و`"csv"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:185]

```
186:             "jpg", "jpeg", "png", "gif", "bmp", "webp", "svg"
```
> بقيّة عناصر القائمة: `"jpg"` و`"jpeg"` و`"png"` و`"gif"` و`"bmp"` و`"webp"` و`"svg"`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:186]

```
187:         )
```
> إغلاق سرد `listOf`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:187]

```
188:     }
```
> إغلاق نطاق دالّة `isFileViewable`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:188]

```
189: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:189]

```
190:     /**
```
> تعليق توثيقي (بدايته): فتح كتلة تعليق `/**`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:190]

```
191:      * Save an incoming file packet to app storage and return absolute path.
```
> تعليق: «احفظ رزمة ملف واردة في تخزين التطبيق وأعِد المسار المُطلق». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:191]

```
192:      * Mirrors existing behavior used in MessageHandler (preserves names and folders).
```
> تعليق: «يحاكي السلوك القائم المستخدَم في `MessageHandler` (يحفظ الأسماء والمجلّدات)». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:192]

```
193:      */
```
> تعليق توثيقي (نهايته): إغلاق كتلة التعليق `*/`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:193]

```
194:     fun saveIncomingFile(
```
> تُعرَّف دالّة باسم `saveIncomingFile` (حفظ الملف الوارد) ويُفتح سرد مُعاملاتها. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:194]

```
195:         context: Context,
```
> مُعامل أوّل باسم `context` من نوع `Context`. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:195]

```
196:         file: com.bitchat.android.model.BitchatFilePacket
```
> مُعامل ثانٍ باسم `file` من نوع `com.bitchat.android.model.BitchatFilePacket` (رزمة ملف بِت-تشات). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:196]

```
197:     ): String {
```
> يُغلَق سرد المُعاملات، ونوع القيمة المُعادة `String`، ويُفتح جسم الدالّة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:197]

```
198:         val lowerMime = file.mimeType.lowercase()
```
> يُعرَّف متغيّر ثابت `lowerMime` (الميديا بأحرف صغيرة) ويُسنَد إليه `file.mimeType.lowercase()` (نوع الميديا للملف محوَّلاً لحروف صغيرة). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:198]

```
199:         val isImage = lowerMime.startsWith("image/")
```
> يُعرَّف متغيّر ثابت `isImage` (هل صورة) ويُسنَد إليه نتيجة `lowerMime.startsWith("image/")` (هل يبدأ نوع الميديا بـ `"image/"`). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:199]

```
200:         // FIX: Use cacheDir instead of filesDir to prevent storage exhaustion attacks (Issue #592)
```
> تعليق: «إصلاح: استخدم `cacheDir` بدل `filesDir` لمنع هجمات استنزاف التخزين (المشكلة رقم ٥٩٢)». [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:200]
