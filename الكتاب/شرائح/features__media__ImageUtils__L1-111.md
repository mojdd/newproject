# شريحة — app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt (الأسطر 1–111)

```
1: package com.bitchat.android.features.media
```
> يُعرّف الحزمة (package) باسم com.bitchat.android.features.media. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:2]

```
3: import android.content.Context
```
> يستورد صنف السياق (Context) من android.content. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:3]

```
4: import android.graphics.Bitmap
```
> يستورد صنف الصورة النقطية (Bitmap) من android.graphics. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:4]

```
5: import android.graphics.BitmapFactory
```
> يستورد مصنع الصور النقطية (BitmapFactory) من android.graphics. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:5]

```
6: import android.graphics.Matrix
```
> يستورد صنف المصفوفة (Matrix) من android.graphics. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:6]

```
7: import android.net.Uri
```
> يستورد صنف المعرّف الموحّد للمورد (Uri) من android.net. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:7]

```
8: import androidx.exifinterface.media.ExifInterface
```
> يستورد واجهة بيانات Exif (ExifInterface) من androidx.exifinterface.media. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:8]

```
9: import java.io.File
```
> يستورد صنف الملف (File) من java.io. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:9]

```
10: import java.io.FileOutputStream
```
> يستورد صنف تيار إخراج الملف (FileOutputStream) من java.io. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:10]

```
11: import java.io.InputStream
```
> يستورد صنف تيار الإدخال (InputStream) من java.io. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:11]

```
12: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:12]

```
13: object ImageUtils {
```
> يُعرّف كائناً مفرداً (object) باسم أدوات الصور (ImageUtils) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:13]

```
14:     fun downscaleAndSaveToAppFiles(context: Context, uri: Uri, maxDim: Int = 512, quality: Int = 85): String? {
```
> يُعرّف دالة التصغير والحفظ في ملفات التطبيق (downscaleAndSaveToAppFiles) بمعاملات: السياق context، والمعرّف uri، والبُعد الأقصى maxDim بقيمة افتراضية 512، والجودة quality بقيمة افتراضية 85، وتُعيد نصاً (String) قابلاً لأن يكون null، وتفتح نطاقها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:14]

```
15:         return try {
```
> يُعيد نتيجة كتلة try ويفتحها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:15]

```
16:             val resolver = context.contentResolver
```
> يُعرّف متغيّراً ثابتاً resolver ويضبطه على مُحلّل المحتوى (contentResolver) من السياق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:16]

```
17:             val exifRotation = resolver.openInputStream(uri)?.use { getRotationDegreesFromExif(it) } ?: 0
```
> يُعرّف متغيّراً ثابتاً exifRotation ويضبطه على نتيجة فتح تيار إدخال للمعرّف uri عبر openInputStream واستعماله use باستدعاء getRotationDegreesFromExif على التيار، وإن كانت النتيجة null فالقيمة 0. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:17]

```
18: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:18]

```
19:             // Reopen for decode as the previous stream is consumed
```
> تعليق: إعادة الفتح لفكّ الترميز لأن التيار السابق قد استُهلك. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:19]

```
20:             val input = resolver.openInputStream(uri) ?: return null
```
> يُعرّف متغيّراً ثابتاً input ويضبطه على فتح تيار إدخال للمعرّف uri عبر openInputStream، وإن كان null يُعيد null. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:20]

```
21:             val original = BitmapFactory.decodeStream(input)
```
> يُعرّف متغيّراً ثابتاً original ويضبطه على فكّ ترميز التيار input عبر BitmapFactory.decodeStream. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:21]

```
22:             input.close()
```
> يستدعي close لإغلاق التيار input. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:22]

```
23:             original ?: return null
```
> إن كان original مساوياً null يُعيد null. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:24]

```
25:             val oriented = if (exifRotation != 0) rotateBitmap(original, exifRotation) else original
```
> يُعرّف متغيّراً ثابتاً oriented ويضبطه على: إن كان exifRotation لا يساوي 0 فنتيجة rotateBitmap للصورة original بزاوية exifRotation، وإلا فالصورة original نفسها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:25]

```
26: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:26]

```
27:             val w = oriented.width
```
> يُعرّف متغيّراً ثابتاً w ويضبطه على عرض (width) الصورة oriented. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:27]

```
28:             val h = oriented.height
```
> يُعرّف متغيّراً ثابتاً h ويضبطه على ارتفاع (height) الصورة oriented. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:28]

```
29:             val scale = (maxOf(w, h).toFloat() / maxDim.toFloat()).coerceAtLeast(1f)
```
> يُعرّف متغيّراً ثابتاً scale ويضبطه على أكبر قيمة بين w و h (maxOf) محوّلة إلى عدد عشري مقسومة على maxDim المحوّل إلى عدد عشري، مع فرض حدّ أدنى 1f عبر coerceAtLeast. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:29]

```
30:             val newW = (w / scale).toInt().coerceAtLeast(1)
```
> يُعرّف متغيّراً ثابتاً newW ويضبطه على w مقسوماً على scale محوّلاً إلى عدد صحيح، مع فرض حدّ أدنى 1 عبر coerceAtLeast. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:30]

```
31:             val newH = (h / scale).toInt().coerceAtLeast(1)
```
> يُعرّف متغيّراً ثابتاً newH ويضبطه على h مقسوماً على scale محوّلاً إلى عدد صحيح، مع فرض حدّ أدنى 1 عبر coerceAtLeast. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:31]

```
32:             val scaled = if (scale > 1f) Bitmap.createScaledBitmap(oriented, newW, newH, true) else oriented
```
> يُعرّف متغيّراً ثابتاً scaled ويضبطه على: إن كان scale أكبر من 1f فصورة مُحجّمة عبر Bitmap.createScaledBitmap من oriented بأبعاد newW و newH مع الفلترة true، وإلا فالصورة oriented نفسها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:32]

```
33:             val dir = File(context.filesDir, "images/outgoing").apply { mkdirs() }
```
> يُعرّف متغيّراً ثابتاً dir ويضبطه على ملف (File) داخل filesDir من السياق بالمسار "images/outgoing"، ويطبّق عليه mkdirs لإنشاء المجلدات. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:33]

```
34:             val outFile = File(dir, "img_${System.currentTimeMillis()}.jpg")
```
> يُعرّف متغيّراً ثابتاً outFile ويضبطه على ملف داخل dir باسم "img_" متبوعاً بالوقت الحالي بالمليّ ثانية (System.currentTimeMillis) ولاحقة ".jpg". [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:34]

```
35:             FileOutputStream(outFile).use { fos ->
```
> ينشئ تيار إخراج ملف (FileOutputStream) للملف outFile ويستعمله use بمعامل fos، ويفتح النطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:35]

```
36:                 scaled.compress(Bitmap.CompressFormat.JPEG, quality, fos)
```
> يستدعي compress على الصورة scaled بصيغة JPEG (Bitmap.CompressFormat.JPEG) وجودة quality والكتابة إلى fos. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:36]

```
37:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:37]

```
38:             try { if (oriented !== original) original.recycle() } catch (_: Exception) {}
```
> كتلة try: إن كانت oriented لا تطابق original مرجعياً (!==) يستدعي recycle على original، مع كتلة catch تلتقط أي Exception وتتجاهلها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:38]

```
39:             try { if (scaled !== oriented) oriented.recycle() } catch (_: Exception) {}
```
> كتلة try: إن كانت scaled لا تطابق oriented مرجعياً (!==) يستدعي recycle على oriented، مع كتلة catch تلتقط أي Exception وتتجاهلها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:39]

```
40:             outFile.absolutePath
```
> يُعيد المسار المطلق (absolutePath) للملف outFile كقيمة كتلة try. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:40]

```
41:         } catch (e: Exception) {
```
> يُغلق نطاق try ويفتح كتلة catch تلتقط استثناءً e من نوع Exception. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:41]

```
42:             null
```
> يُعيد null كقيمة كتلة catch. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:42]

```
43:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:43]

```
44:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:44]

```
45: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:45]

```
46:     fun downscalePathAndSaveToAppFiles(context: Context, path: String, maxDim: Int = 512, quality: Int = 85): String? {
```
> يُعرّف دالة تصغير المسار والحفظ في ملفات التطبيق (downscalePathAndSaveToAppFiles) بمعاملات: السياق context، والمسار path نصّاً، والبُعد الأقصى maxDim بقيمة افتراضية 512، والجودة quality بقيمة افتراضية 85، وتُعيد نصاً قابلاً لأن يكون null، وتفتح نطاقها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:46]

```
47:         return try {
```
> يُعيد نتيجة كتلة try ويفتحها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:47]

```
48:             val original = BitmapFactory.decodeFile(path) ?: return null
```
> يُعرّف متغيّراً ثابتاً original ويضبطه على فكّ ترميز الملف بالمسار path عبر BitmapFactory.decodeFile، وإن كان null يُعيد null. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:48]

```
49:             val exifRotation = getRotationDegreesFromExif(path)
```
> يُعرّف متغيّراً ثابتاً exifRotation ويضبطه على نتيجة getRotationDegreesFromExif للمسار path. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:49]

```
50:             val oriented = if (exifRotation != 0) rotateBitmap(original, exifRotation) else original
```
> يُعرّف متغيّراً ثابتاً oriented ويضبطه على: إن كان exifRotation لا يساوي 0 فنتيجة rotateBitmap للصورة original بزاوية exifRotation، وإلا فالصورة original نفسها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:50]

```
51: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:51]

```
52:             val w = oriented.width
```
> يُعرّف متغيّراً ثابتاً w ويضبطه على عرض الصورة oriented. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:52]

```
53:             val h = oriented.height
```
> يُعرّف متغيّراً ثابتاً h ويضبطه على ارتفاع الصورة oriented. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:53]

```
54:             val scale = (maxOf(w, h).toFloat() / maxDim.toFloat()).coerceAtLeast(1f)
```
> يُعرّف متغيّراً ثابتاً scale ويضبطه على أكبر قيمة بين w و h محوّلة إلى عدد عشري مقسومة على maxDim المحوّل إلى عدد عشري، مع فرض حدّ أدنى 1f. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:54]

```
55:             val newW = (w / scale).toInt().coerceAtLeast(1)
```
> يُعرّف متغيّراً ثابتاً newW ويضبطه على w مقسوماً على scale محوّلاً إلى عدد صحيح، مع فرض حدّ أدنى 1. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:55]

```
56:             val newH = (h / scale).toInt().coerceAtLeast(1)
```
> يُعرّف متغيّراً ثابتاً newH ويضبطه على h مقسوماً على scale محوّلاً إلى عدد صحيح، مع فرض حدّ أدنى 1. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:56]

```
57:             val scaled = if (scale > 1f) Bitmap.createScaledBitmap(oriented, newW, newH, true) else oriented
```
> يُعرّف متغيّراً ثابتاً scaled ويضبطه على: إن كان scale أكبر من 1f فصورة مُحجّمة عبر Bitmap.createScaledBitmap من oriented بأبعاد newW و newH مع الفلترة true، وإلا فالصورة oriented نفسها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:57]

```
58:             val dir = File(context.filesDir, "images/outgoing").apply { mkdirs() }
```
> يُعرّف متغيّراً ثابتاً dir ويضبطه على ملف داخل filesDir من السياق بالمسار "images/outgoing"، ويطبّق عليه mkdirs لإنشاء المجلدات. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:58]

```
59:             val outFile = File(dir, "img_${System.currentTimeMillis()}.jpg")
```
> يُعرّف متغيّراً ثابتاً outFile ويضبطه على ملف داخل dir باسم "img_" متبوعاً بالوقت الحالي بالمليّ ثانية ولاحقة ".jpg". [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:59]

```
60:             FileOutputStream(outFile).use { fos ->
```
> ينشئ تيار إخراج ملف (FileOutputStream) للملف outFile ويستعمله use بمعامل fos، ويفتح النطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:60]

```
61:                 scaled.compress(Bitmap.CompressFormat.JPEG, quality, fos)
```
> يستدعي compress على الصورة scaled بصيغة JPEG وجودة quality والكتابة إلى fos. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:61]

```
62:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:62]

```
63:             try { if (oriented !== original) original.recycle() } catch (_: Exception) {}
```
> كتلة try: إن كانت oriented لا تطابق original مرجعياً يستدعي recycle على original، مع كتلة catch تلتقط أي Exception وتتجاهلها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:63]

```
64:             try { if (scaled !== oriented) oriented.recycle() } catch (_: Exception) {}
```
> كتلة try: إن كانت scaled لا تطابق oriented مرجعياً يستدعي recycle على oriented، مع كتلة catch تلتقط أي Exception وتتجاهلها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:64]

```
65:             outFile.absolutePath
```
> يُعيد المسار المطلق للملف outFile كقيمة كتلة try. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:65]

```
66:         } catch (e: Exception) {
```
> يُغلق نطاق try ويفتح كتلة catch تلتقط استثناءً e من نوع Exception. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:66]

```
67:             null
```
> يُعيد null كقيمة كتلة catch. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:67]

```
68:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:68]

```
69:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:69]

```
70: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:70]

```
71:     fun loadBitmapWithExifOrientation(path: String): Bitmap? {
```
> يُعرّف دالة تحميل الصورة باتجاه Exif (loadBitmapWithExifOrientation) بمعامل المسار path نصّاً، وتُعيد صورة نقطية (Bitmap) قابلة لأن تكون null، وتفتح نطاقها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:71]

```
72:         return try {
```
> يُعيد نتيجة كتلة try ويفتحها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:72]

```
73:             val base = BitmapFactory.decodeFile(path) ?: return null
```
> يُعرّف متغيّراً ثابتاً base ويضبطه على فكّ ترميز الملف بالمسار path عبر BitmapFactory.decodeFile، وإن كان null يُعيد null. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:73]

```
74:             val rotation = getRotationDegreesFromExif(path)
```
> يُعرّف متغيّراً ثابتاً rotation ويضبطه على نتيجة getRotationDegreesFromExif للمسار path. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:74]

```
75:             if (rotation != 0) rotateBitmap(base, rotation) else base
```
> إن كان rotation لا يساوي 0 فنتيجة rotateBitmap للصورة base بزاوية rotation، وإلا فالصورة base نفسها، كقيمة كتلة try. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:75]

```
76:         } catch (_: Exception) {
```
> يُغلق نطاق try ويفتح كتلة catch تلتقط استثناءً من نوع Exception دون تسميته. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:76]

```
77:             null
```
> يُعيد null كقيمة كتلة catch. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:77]

```
78:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:78]

```
79:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:79]

```
80: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:80]

```
81:     private fun rotateBitmap(src: Bitmap, degrees: Int): Bitmap {
```
> يُعرّف دالة خاصة (private) لتدوير الصورة (rotateBitmap) بمعاملي المصدر src صورةً والدرجات degrees عدداً صحيحاً، وتُعيد صورة نقطية (Bitmap)، وتفتح نطاقها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:81]

```
82:         return try {
```
> يُعيد نتيجة كتلة try ويفتحها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:82]

```
83:             val m = Matrix()
```
> يُعرّف متغيّراً ثابتاً m ويضبطه على نسخة جديدة من المصفوفة (Matrix). [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:83]

```
84:             m.postRotate(degrees.toFloat())
```
> يستدعي postRotate على المصفوفة m بقيمة degrees محوّلة إلى عدد عشري. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:84]

```
85:             Bitmap.createBitmap(src, 0, 0, src.width, src.height, m, true).also {
```
> ينشئ صورة عبر Bitmap.createBitmap من src بدءاً من الإحداثيين 0 و0 وبعرض src.width وارتفاع src.height مع المصفوفة m والفلترة true، ويطبّق عليها also ويفتح نطاقه. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:85]

```
86:                 try { src.recycle() } catch (_: Exception) {}
```
> كتلة try تستدعي recycle على src، مع كتلة catch تلتقط أي Exception وتتجاهلها. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:86]

```
87:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:87]

```
88:         } catch (_: Exception) {
```
> يُغلق نطاق try ويفتح كتلة catch تلتقط استثناءً من نوع Exception دون تسميته. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:88]

```
89:             src
```
> يُعيد src كقيمة كتلة catch. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:89]

```
90:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:90]

```
91:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:91]

```
92: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:92]

```
93:     private fun getRotationDegreesFromExif(path: String): Int = try {
```
> يُعرّف دالة خاصة لجلب درجات التدوير من Exif (getRotationDegreesFromExif) بمعامل المسار path نصّاً، وتُعيد عدداً صحيحاً (Int) بقيمة كتلة try التي تفتح. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:93]

```
94:         val exif = ExifInterface(path)
```
> يُعرّف متغيّراً ثابتاً exif ويضبطه على نسخة جديدة من ExifInterface مبنية على المسار path. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:94]

```
95:         orientationToDegrees(exif.getAttributeInt(ExifInterface.TAG_ORIENTATION, ExifInterface.ORIENTATION_NORMAL))
```
> يستدعي orientationToDegrees على قيمة السمة الصحيحة getAttributeInt للوسم TAG_ORIENTATION بقيمة افتراضية ORIENTATION_NORMAL من exif، كقيمة كتلة try. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:95]

```
96:     } catch (_: Exception) { 0 }
```
> يُغلق نطاق try ويفتح كتلة catch تلتقط استثناءً من نوع Exception دون تسميته وتُعيد 0. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:96]

```
97: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:97]

```
98:     private fun getRotationDegreesFromExif(stream: InputStream): Int = try {
```
> يُعرّف دالة خاصة محمّلة بنفس الاسم (getRotationDegreesFromExif) بمعامل التيار stream من نوع InputStream، وتُعيد عدداً صحيحاً بقيمة كتلة try التي تفتح. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:98]

```
99:         val exif = ExifInterface(stream)
```
> يُعرّف متغيّراً ثابتاً exif ويضبطه على نسخة جديدة من ExifInterface مبنية على التيار stream. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:99]

```
100:         orientationToDegrees(exif.getAttributeInt(ExifInterface.TAG_ORIENTATION, ExifInterface.ORIENTATION_NORMAL))
```
> يستدعي orientationToDegrees على قيمة السمة الصحيحة getAttributeInt للوسم TAG_ORIENTATION بقيمة افتراضية ORIENTATION_NORMAL من exif، كقيمة كتلة try. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:100]

```
101:     } catch (_: Exception) { 0 }
```
> يُغلق نطاق try ويفتح كتلة catch تلتقط استثناءً من نوع Exception دون تسميته وتُعيد 0. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:101]

```
102: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:102]

```
103:     private fun orientationToDegrees(orientation: Int): Int = when (orientation) {
```
> يُعرّف دالة خاصة لتحويل الاتجاه إلى درجات (orientationToDegrees) بمعامل الاتجاه orientation عدداً صحيحاً، وتُعيد عدداً صحيحاً بقيمة تعبير when على orientation الذي يفتح. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:103]

```
104:         ExifInterface.ORIENTATION_ROTATE_90 -> 90
```
> فرع when: عند ORIENTATION_ROTATE_90 تكون القيمة 90. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:104]

```
105:         ExifInterface.ORIENTATION_ROTATE_180 -> 180
```
> فرع when: عند ORIENTATION_ROTATE_180 تكون القيمة 180. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:105]

```
106:         ExifInterface.ORIENTATION_ROTATE_270 -> 270
```
> فرع when: عند ORIENTATION_ROTATE_270 تكون القيمة 270. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:106]

```
107:         ExifInterface.ORIENTATION_TRANSPOSE -> 90
```
> فرع when: عند ORIENTATION_TRANSPOSE تكون القيمة 90. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:107]

```
108:         ExifInterface.ORIENTATION_TRANSVERSE -> 270
```
> فرع when: عند ORIENTATION_TRANSVERSE تكون القيمة 270. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:108]

```
109:         else -> 0
```
> فرع when الافتراضي else: القيمة 0. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:109]

```
110:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:110]

```
111: }
```
> إغلاق نطاق الكائن المفرد ImageUtils. [app/src/main/java/com/bitchat/android/features/media/ImageUtils.kt:111]
