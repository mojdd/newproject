# شريحة — app/src/main/java/com/bitchat/android/model/FileSharingManager.kt (الأسطر 1–92)

```
1: package com.bitchat.android.model
```
> يُعلِن أنّ هذا الملف ينتمي إلى الحزمة (package) المسمّاة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:2]

```
3: import android.content.Context
```
> يستورد (import) النوع `Context` من حزمة أندرويد `android.content`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:3]

```
4: import android.net.Uri
```
> يستورد النوع `Uri` (المعرّف الموحّد للمورد) من حزمة `android.net`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:4]

```
5: import android.util.Log
```
> يستورد الأداة `Log` (التسجيل) من حزمة `android.util`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:5]

```
6: import com.bitchat.android.features.file.FileUtils
```
> يستورد الكائن `FileUtils` (أدوات الملفات) من حزمة `com.bitchat.android.features.file`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:6]

```
7: import java.io.File
```
> يستورد النوع `File` (الملف) من حزمة جافا `java.io`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:8]

```
9: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:9]

```
10:  * Business logic for file sharing operations
```
> تعليق: «منطق العمل لعمليات مشاركة الملفات». [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:10]

```
11:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:11]

```
12: object FileSharingManager {
```
> يُعرِّف كائناً مفرداً (object) باسم `FileSharingManager` (مدير مشاركة الملفات) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:12]

```
13: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:13]

```
14:     private const val TAG = "FileSharingManager"
```
> يُعرِّف ثابتاً خاصاً (private const) باسم `TAG` (الوسم) قيمته الحرفية السلسلة `"FileSharingManager"`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:14]

```
15: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:15]

```
16:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:16]

```
17:      * Create a file packet from URI for sending
```
> تعليق: «أنشئ حزمة ملف من المعرّف الموحّد (URI) للإرسال». [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:17]

```
18:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:18]

```
19:     fun createFilePacketFromUri(
```
> يُعرِّف الدالة `createFilePacketFromUri` (إنشاء حزمة ملف من المعرّف الموحّد) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:19]

```
20:         context: Context,
```
> يُعرِّف المعامل `context` من النوع `Context`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:20]

```
21:         uri: Uri,
```
> يُعرِّف المعامل `uri` من النوع `Uri`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:21]

```
22:         originalName: String? = null
```
> يُعرِّف المعامل `originalName` (الاسم الأصلي) من النوع نص قابل للإفراغ (`String?`) بقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:22]

```
23:     ): BitchatFilePacket? {
```
> يُغلق قائمة المعاملات ويُحدِّد نوع الإرجاع `BitchatFilePacket?` (حزمة ملف بِتشات قابلة للإفراغ) ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:23]

```
24:         return try {
```
> يبدأ تعليمة الإرجاع (return) بقيمة كتلة `try` (المحاولة). [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:24]

```
25:             // Get file name from URI or use original name
```
> تعليق: «احصل على اسم الملف من المعرّف الموحّد أو استعمل الاسم الأصلي». [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:25]

```
26:             val fileName = originalName ?: getFileNameFromUri(context, uri) ?: "unknown_file"
```
> يُعرِّف المتغيّر `fileName` (اسم الملف) قيمته `originalName`، فإن كان فارغاً فنتيجة استدعاء `getFileNameFromUri(context, uri)`، فإن كانت فارغة فالسلسلة الحرفية `"unknown_file"`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:27]

```
28:             // Copy file to our temp storage for sending
```
> تعليق: «انسخ الملف إلى تخزيننا المؤقّت للإرسال». [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:28]

```
29:             val localPath = FileUtils.copyFileForSending(context, uri) ?: return null
```
> يُعرِّف المتغيّر `localPath` (المسار المحلّي) من نتيجة استدعاء `FileUtils.copyFileForSending(context, uri)`، وإن كانت النتيجة فارغة يُرجِع `null` من الدالة. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:29]

```
30: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:30]

```
31:             // Determine MIME type
```
> تعليق: «حدِّد نوع MIME». [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:31]

```
32:             val mimeType = FileUtils.getMimeTypeFromExtension(fileName)
```
> يُعرِّف المتغيّر `mimeType` (نوع MIME) من نتيجة استدعاء `FileUtils.getMimeTypeFromExtension(fileName)`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:33]

```
34:             // Read file content
```
> تعليق: «اقرأ محتوى الملف». [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:34]

```
35:             val file = File(localPath)
```
> يُعرِّف المتغيّر `file` (الملف) بإنشاء كائن `File` من المسار `localPath`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:35]

```
36:             val content = file.readBytes()
```
> يُعرِّف المتغيّر `content` (المحتوى) من نتيجة استدعاء `file.readBytes()` التي تقرأ بايتات الملف. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:36]

```
37:             val fileSize = file.length()
```
> يُعرِّف المتغيّر `fileSize` (حجم الملف) من نتيجة استدعاء `file.length()` التي تُعيد طول الملف. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:37]

```
38: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:38]

```
39:             // Clean up temp file
```
> تعليق: «نظِّف الملف المؤقّت». [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:39]

```
40:             file.delete()
```
> يستدعي `file.delete()` لحذف الملف. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:40]

```
41: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:41]

```
42:             val packet = BitchatFilePacket(
```
> يُعرِّف المتغيّر `packet` (الحزمة) بإنشاء كائن `BitchatFilePacket` ويفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:42]

```
43:                 fileName = fileName,
```
> يمرّر للوسيط `fileName` قيمة المتغيّر `fileName`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:43]

```
44:                 fileSize = fileSize,
```
> يمرّر للوسيط `fileSize` قيمة المتغيّر `fileSize`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:44]

```
45:                 mimeType = mimeType,
```
> يمرّر للوسيط `mimeType` قيمة المتغيّر `mimeType`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:45]

```
46:                 content = content
```
> يمرّر للوسيط `content` قيمة المتغيّر `content`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:46]

```
47:             )
```
> يُغلق قائمة وُسطاء إنشاء `BitchatFilePacket`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:47]

```
48: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:48]

```
49:             Log.d(TAG, "Created file packet: name=$fileName, size=${FileUtils.formatFileSize(fileSize)}, mime=$mimeType")
```
> يستدعي `Log.d` بالوسم `TAG` لتسجيل رسالة تصحيح نصّها «Created file packet:» متبوعةً بقيمة `fileName` والحجم المنسّق عبر `FileUtils.formatFileSize(fileSize)` ونوع `mimeType`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:49]

```
50:             packet
```
> يجعل المتغيّر `packet` قيمة كتلة `try` المُعادة. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:50]

```
51: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:51]

```
52:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويفتح كتلة `catch` (الالتقاط) التي تلتقط اعتراضاً `e` من النوع `Exception`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:52]

```
53:             Log.e(TAG, "Failed to create file packet from URI", e)
```
> يستدعي `Log.e` بالوسم `TAG` لتسجيل خطأ نصّه «Failed to create file packet from URI» مع الاعتراض `e`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:53]

```
54:             null
```
> يجعل `null` قيمة كتلة `catch` المُعادة. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:54]

```
55:         }
```
> إغلاق نطاق كتلة `try/catch`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:55]

```
56:     }
```
> إغلاق نطاق الدالة `createFilePacketFromUri`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:56]

```
57: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:57]

```
58:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:58]

```
59:      * Extract filename from URI
```
> تعليق: «استخرج اسم الملف من المعرّف الموحّد (URI)». [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:59]

```
60:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:60]

```
61:     private fun getFileNameFromUri(context: Context, uri: Uri): String? {
```
> يُعرِّف دالة خاصة `getFileNameFromUri` (الحصول على اسم الملف من المعرّف الموحّد) تأخذ `context: Context` و`uri: Uri` وتُعيد نصاً قابلاً للإفراغ `String?` ويفتح جسمها. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:61]

```
62:         return try {
```
> يبدأ تعليمة الإرجاع (return) بقيمة كتلة `try`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:62]

```
63:             context.contentResolver.query(uri, null, null, null, null)?.use { cursor ->
```
> يستدعي `context.contentResolver.query` على `uri` بقيم `null` للمعاملات الأربعة الباقية، وإن لم تكن النتيجة فارغة يستعملها بـ`use` مُسمّياً النتيجة `cursor` (المؤشّر). [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:63]

```
64:                 val nameIndex = cursor.getColumnIndex(android.provider.MediaStore.MediaColumns.DISPLAY_NAME)
```
> يُعرِّف المتغيّر `nameIndex` (فهرس الاسم) من نتيجة `cursor.getColumnIndex` للعمود `android.provider.MediaStore.MediaColumns.DISPLAY_NAME`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:64]

```
65:                 cursor.moveToFirst()
```
> يستدعي `cursor.moveToFirst()` لنقل المؤشّر إلى أوّل صفّ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:65]

```
66:                 cursor.getString(nameIndex)
```
> يُعيد قيمة `cursor.getString(nameIndex)` كنتيجة كتلة `use`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:66]

```
67:             } ?: uri.lastPathSegment
```
> يُغلق كتلة `use`، وإن كانت قيمتها فارغة فيستعمل `uri.lastPathSegment` (آخر مقطع من مسار المعرّف الموحّد) بدلاً منها. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:67]

```
68:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويفتح كتلة `catch` التي تلتقط اعتراضاً `e` من النوع `Exception`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:68]

```
69:             Log.w(TAG, "Failed to get filename from URI", e)
```
> يستدعي `Log.w` بالوسم `TAG` لتسجيل تحذير نصّه «Failed to get filename from URI» مع الاعتراض `e`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:69]

```
70:             uri.lastPathSegment
```
> يجعل `uri.lastPathSegment` قيمة كتلة `catch` المُعادة. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:70]

```
71:         }
```
> إغلاق نطاق كتلة `try/catch`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:71]

```
72:     }
```
> إغلاق نطاق الدالة `getFileNameFromUri`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:72]

```
73: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:73]

```
74:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:74]

```
75:      * Process a received file packet and return file info
```
> تعليق: «عالِج حزمة ملف مُستلَمة وأعِد معلومات الملف». [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:75]

```
76:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:76]

```
77:     data class ReceivedFileInfo(
```
> يُعرِّف صنف بيانات (data class) باسم `ReceivedFileInfo` (معلومات الملف المُستلَم) ويفتح قائمة خصائصه. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:77]

```
78:         val fileName: String,
```
> يُعرِّف الخاصية `fileName` من النوع `String`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:78]

```
79:         val fileSize: Long,
```
> يُعرِّف الخاصية `fileSize` من النوع `Long` (عدد صحيح طويل). [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:79]

```
80:         val mimeType: String,
```
> يُعرِّف الخاصية `mimeType` من النوع `String`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:80]

```
81:         val content: ByteArray
```
> يُعرِّف الخاصية `content` من النوع `ByteArray` (مصفوفة بايتات). [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:81]

```
82:     )
```
> يُغلق قائمة خصائص صنف البيانات `ReceivedFileInfo`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:82]

```
83: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:83]

```
84:     fun processReceivedFile(packet: BitchatFilePacket): ReceivedFileInfo {
```
> يُعرِّف الدالة `processReceivedFile` (معالجة الملف المُستلَم) تأخذ `packet: BitchatFilePacket` وتُعيد `ReceivedFileInfo` ويفتح جسمها. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:84]

```
85:         return ReceivedFileInfo(
```
> يُرجِع كائن `ReceivedFileInfo` جديداً ويفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:85]

```
86:             fileName = packet.fileName,
```
> يمرّر للوسيط `fileName` قيمة `packet.fileName`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:86]

```
87:             fileSize = packet.fileSize,
```
> يمرّر للوسيط `fileSize` قيمة `packet.fileSize`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:87]

```
88:             mimeType = packet.mimeType,
```
> يمرّر للوسيط `mimeType` قيمة `packet.mimeType`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:88]

```
89:             content = packet.content
```
> يمرّر للوسيط `content` قيمة `packet.content`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:89]

```
90:         )
```
> يُغلق قائمة وُسطاء إنشاء `ReceivedFileInfo` المُعاد. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:90]

```
91:     }
```
> إغلاق نطاق الدالة `processReceivedFile`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:91]

```
92: }
```
> إغلاق نطاق الكائن المفرد `FileSharingManager`. [app/src/main/java/com/bitchat/android/model/FileSharingManager.kt:92]
