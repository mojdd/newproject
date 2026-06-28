# شريحة — app/src/main/java/com/bitchat/android/features/file/FileUtils.kt (الأسطر 201–326)

```
201:         // Files in cacheDir are eligible for automatic system cleanup when space is low
```
> تعليق: الملفات في مجلد التخزين المؤقت (cacheDir) مؤهَّلة للحذف التلقائي من النظام عندما تقل المساحة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:201]

```
202:         val baseDir = context.cacheDir
```
> يُعرَّف متغيّر ثابت اسمه المجلد الأساسي (baseDir) ويُسنَد إليه قيمة مجلد التخزين المؤقت (cacheDir) المأخوذ من السياق (context). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:202]

```
203:         val subdir = if (isImage) "images/incoming" else "files/incoming"
```
> يُعرَّف متغيّر ثابت اسمه المجلد الفرعي (subdir) ويُسنَد إليه النص "images/incoming" إذا كان (isImage) صحيحاً وإلا النص "files/incoming". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:203]

```
204:         val dir = java.io.File(baseDir, subdir).apply { mkdirs() }
```
> يُعرَّف متغيّر ثابت اسمه المجلد (dir) ويُسنَد إليه كائن ملف (java.io.File) مبني من المجلد الأساسي والمجلد الفرعي، ثم يُستدعى عليه عبر apply الدالة mkdirs لإنشاء المجلدات. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:204]

```
205: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:205]

```
206:         fun extFromMime(m: String): String = when (m.lowercase()) {
```
> تُعرَّف دالة محلية اسمها الامتداد من نوع الميمي (extFromMime) تأخذ نصاً اسمه m وتُعيد نصاً (String)، وقيمتها تعبير when على m بعد تحويله إلى حروف صغيرة (lowercase). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:206]

```
207:             "image/jpeg", "image/jpg" -> ".jpg"
```
> في حالة كان النص "image/jpeg" أو "image/jpg" تُعاد القيمة ".jpg". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:207]

```
208:             "image/png" -> ".png"
```
> في حالة كان النص "image/png" تُعاد القيمة ".png". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:208]

```
209:             "image/webp" -> ".webp"
```
> في حالة كان النص "image/webp" تُعاد القيمة ".webp". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:209]

```
210:             "application/pdf" -> ".pdf"
```
> في حالة كان النص "application/pdf" تُعاد القيمة ".pdf". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:210]

```
211:             "text/plain" -> ".txt"
```
> في حالة كان النص "text/plain" تُعاد القيمة ".txt". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:211]

```
212:             else -> if (isImage) ".jpg" else ".bin"
```
> في الحالة الافتراضية (else) تُعاد القيمة ".jpg" إذا كان (isImage) صحيحاً وإلا القيمة ".bin". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:212]

```
213:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:213]

```
214: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:214]

```
215:         // Prefer transmitted original name; ensure uniqueness to avoid overwrites
```
> تعليق: فضِّل الاسم الأصلي المُرسَل؛ اضمن التفرّد لتجنّب الكتابة فوق الملفات. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:215]

```
216:         val baseName = (file.fileName.takeIf { it.isNotBlank() }
```
> يُعرَّف متغيّر ثابت اسمه الاسم الأساسي (baseName) ويُسنَد إليه اسم الملف (file.fileName) عبر takeIf الذي يُبقيه إذا لم يكن فارغاً (isNotBlank). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:216]

```
217:             ?: (if (isImage) "img" else "file"))
```
> وفي حال كانت القيمة السابقة فارغة (?:) يُستعمل النص "img" إذا كان (isImage) صحيحاً وإلا النص "file". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:217]

```
218:             .replace(Regex("[^A-Za-z0-9._-]"), "_")
```
> يُستدعى على النتيجة replace باستعمال تعبير نمطي (Regex) يطابق كل محرف ليس حرفاً أو رقماً أو نقطة أو شرطة سفلية أو شرطة، ويستبدله بشرطة سفلية "_". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:218]

```
219:         val ext = extFromMime(lowerMime)
```
> يُعرَّف متغيّر ثابت اسمه الامتداد (ext) ويُسنَد إليه ناتج استدعاء الدالة extFromMime على المتغيّر lowerMime. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:219]

```
220:         var safeName = if (baseName.contains('.')) baseName else baseName + ext
```
> يُعرَّف متغيّر متبدّل اسمه الاسم الآمن (safeName) ويُسنَد إليه الاسم الأساسي إذا كان يحتوي نقطة (contains '.') وإلا الاسم الأساسي مضافاً إليه الامتداد. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:220]

```
221:         var idx = 1
```
> يُعرَّف متغيّر متبدّل اسمه الفهرس (idx) ويُسنَد إليه القيمة 1. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:221]

```
222:         while (java.io.File(dir, safeName).exists() && idx < 1000) {
```
> حلقة while تستمر طالما أن ملفاً (java.io.File) مبنياً من المجلد والاسم الآمن موجود (exists) والفهرس أقل من 1000. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:222]

```
223:             val dot = safeName.lastIndexOf('.')
```
> يُعرَّف متغيّر ثابت اسمه النقطة (dot) ويُسنَد إليه آخر موضع للنقطة (lastIndexOf '.') في الاسم الآمن. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:223]

```
224:             safeName = if (dot > 0) {
```
> يُعاد إسناد الاسم الآمن بقيمة تعبير شرطي: إذا كان موضع النقطة أكبر من 0. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:224]

```
225:                 val b = safeName.substring(0, dot)
```
> يُعرَّف متغيّر ثابت اسمه b ويُسنَد إليه المقطع الفرعي (substring) من الاسم الآمن من الموضع 0 حتى موضع النقطة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:225]

```
226:                 val e = safeName.substring(dot)
```
> يُعرَّف متغيّر ثابت اسمه e ويُسنَد إليه المقطع الفرعي (substring) من الاسم الآمن ابتداءً من موضع النقطة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:226]

```
227:                 "$b ($idx)$e"
```
> القيمة المُعادة من هذا الفرع هي نص مُركَّب يتألف من b ثم مسافة وقوس يحوي الفهرس ثم e. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:227]

```
228:             } else {
```
> بداية الفرع الآخر (else) للتعبير الشرطي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:228]

```
229:                 "$safeName ($idx)"
```
> القيمة المُعادة من هذا الفرع هي نص مُركَّب يتألف من الاسم الآمن ثم مسافة وقوس يحوي الفهرس. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:229]

```
230:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:230]

```
231:             idx++
```
> يُزاد الفهرس (idx) بمقدار واحد. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:231]

```
232:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:232]

```
233: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:233]

```
234:         return try {
```
> تُعاد (return) قيمة كتلة try التي تبدأ هنا. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:234]

```
235:             val out = java.io.File(dir, safeName)
```
> يُعرَّف متغيّر ثابت اسمه الخرج (out) ويُسنَد إليه كائن ملف (java.io.File) مبني من المجلد والاسم الآمن. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:235]

```
236:             out.outputStream().use { it.write(file.content) }
```
> يُستدعى على الخرج تدفّق الإخراج (outputStream) ضمن كتلة use التي تكتب (write) محتوى الملف (file.content). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:236]

```
237:             out.absolutePath
```
> قيمة كتلة try هي المسار المطلق (absolutePath) للخرج. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:237]

```
238:         } catch (_: Exception) {
```
> بداية كتلة catch تلتقط استثناءً (Exception) دون تسمية متغيّره. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:238]

```
239:             // Fallback to cache dir with uniqueness
```
> تعليق: الرجوع الاحتياطي إلى مجلد التخزين المؤقت مع ضمان التفرّد. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:239]

```
240:             try {
```
> بداية كتلة try داخلية. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:240]

```
241:                 var fallback = safeName
```
> يُعرَّف متغيّر متبدّل اسمه الاحتياطي (fallback) ويُسنَد إليه الاسم الآمن. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:241]

```
242:                 var idx2 = 1
```
> يُعرَّف متغيّر متبدّل اسمه الفهرس الثاني (idx2) ويُسنَد إليه القيمة 1. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:242]

```
243:                 while (java.io.File(context.cacheDir, fallback).exists() && idx2 < 1000) {
```
> حلقة while تستمر طالما أن ملفاً (java.io.File) مبنياً من مجلد التخزين المؤقت والاسم الاحتياطي موجود (exists) والفهرس الثاني أقل من 1000. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:243]

```
244:                     val dot = fallback.lastIndexOf('.')
```
> يُعرَّف متغيّر ثابت اسمه النقطة (dot) ويُسنَد إليه آخر موضع للنقطة (lastIndexOf '.') في الاسم الاحتياطي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:244]

```
245:                     fallback = if (dot > 0) {
```
> يُعاد إسناد الاسم الاحتياطي بقيمة تعبير شرطي: إذا كان موضع النقطة أكبر من 0. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:245]

```
246:                         val b = fallback.substring(0, dot)
```
> يُعرَّف متغيّر ثابت اسمه b ويُسنَد إليه المقطع الفرعي (substring) من الاسم الاحتياطي من الموضع 0 حتى موضع النقطة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:246]

```
247:                         val e = fallback.substring(dot)
```
> يُعرَّف متغيّر ثابت اسمه e ويُسنَد إليه المقطع الفرعي (substring) من الاسم الاحتياطي ابتداءً من موضع النقطة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:247]

```
248:                         "$b ($idx2)$e"
```
> القيمة المُعادة من هذا الفرع هي نص مُركَّب يتألف من b ثم مسافة وقوس يحوي الفهرس الثاني ثم e. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:248]

```
249:                     } else {
```
> بداية الفرع الآخر (else) للتعبير الشرطي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:249]

```
250:                         "$fallback ($idx2)"
```
> القيمة المُعادة من هذا الفرع هي نص مُركَّب يتألف من الاسم الاحتياطي ثم مسافة وقوس يحوي الفهرس الثاني. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:250]

```
251:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:251]

```
252:                     idx2++
```
> يُزاد الفهرس الثاني (idx2) بمقدار واحد. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:252]

```
253:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:253]

```
254:                 val out = java.io.File(context.cacheDir, fallback)
```
> يُعرَّف متغيّر ثابت اسمه الخرج (out) ويُسنَد إليه كائن ملف (java.io.File) مبني من مجلد التخزين المؤقت والاسم الاحتياطي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:254]

```
255:                 out.outputStream().use { it.write(file.content) }
```
> يُستدعى على الخرج تدفّق الإخراج (outputStream) ضمن كتلة use التي تكتب (write) محتوى الملف (file.content). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:255]

```
256:                 out.absolutePath
```
> قيمة كتلة try الداخلية هي المسار المطلق (absolutePath) للخرج. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:256]

```
257:             } catch (_: Exception) {
```
> بداية كتلة catch داخلية تلتقط استثناءً (Exception) دون تسمية متغيّره. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:257]

```
258:                 val tmp = java.io.File.createTempFile(if (isImage) "img_" else "file_", if (isImage) ".jpg" else ".bin")
```
> يُعرَّف متغيّر ثابت اسمه المؤقّت (tmp) ويُسنَد إليه ناتج createTempFile ببادئة "img_" إن كان (isImage) صحيحاً وإلا "file_"، ولاحقة ".jpg" إن كان صحيحاً وإلا ".bin". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:258]

```
259:                 tmp.writeBytes(file.content)
```
> يُستدعى على المؤقّت writeBytes لكتابة محتوى الملف (file.content) بايتاتٍ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:259]

```
260:                 tmp.absolutePath
```
> قيمة كتلة catch الداخلية هي المسار المطلق (absolutePath) للمؤقّت. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:260]

```
261:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:261]

```
262:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:262]

```
263:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:263]

```
264: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:264]

```
265:     /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:265]

```
266:      * Classify BitchatMessageType from MIME string used in file messages.
```
> تعليق: تصنيف نوع رسالة بِتشات (BitchatMessageType) من نص الميمي المُستعمل في رسائل الملفات. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:266]

```
267:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:267]

```
268:     fun messageTypeForMime(mime: String): com.bitchat.android.model.BitchatMessageType {
```
> تُعرَّف دالة اسمها نوع الرسالة للميمي (messageTypeForMime) تأخذ نصاً اسمه mime وتُعيد نوع رسالة بِتشات (com.bitchat.android.model.BitchatMessageType). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:268]

```
269:         val lower = mime.lowercase()
```
> يُعرَّف متغيّر ثابت اسمه الصغير (lower) ويُسنَد إليه نص mime بعد تحويله إلى حروف صغيرة (lowercase). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:269]

```
270:         return when {
```
> تُعاد (return) قيمة تعبير when بلا موضوع. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:270]

```
271:             lower.startsWith("image/") -> com.bitchat.android.model.BitchatMessageType.Image
```
> إذا كان الصغير يبدأ بـ "image/" (startsWith) تُعاد القيمة نوع الرسالة صورة (BitchatMessageType.Image). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:271]

```
272:             lower.startsWith("audio/") -> com.bitchat.android.model.BitchatMessageType.Audio
```
> إذا كان الصغير يبدأ بـ "audio/" (startsWith) تُعاد القيمة نوع الرسالة صوت (BitchatMessageType.Audio). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:272]

```
273:             else -> com.bitchat.android.model.BitchatMessageType.File
```
> في الحالة الافتراضية (else) تُعاد القيمة نوع الرسالة ملف (BitchatMessageType.File). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:273]

```
274:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:274]

```
275:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:275]

```
276: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:276]

```
277:     /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:277]

```
278:      * Recursively delete all media files (incoming and outgoing)
```
> تعليق: حذف كل ملفات الوسائط تكرارياً (الواردة والصادرة). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:278]

```
279:      * Used for Panic Mode cleanup
```
> تعليق: يُستعمل لتنظيف وضع الذعر (Panic Mode). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:279]

```
280:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:280]

```
281:     fun clearAllMedia(context: Context) {
```
> تُعرَّف دالة اسمها مسح كل الوسائط (clearAllMedia) تأخذ معاملاً اسمه السياق (context) من نوع Context. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:281]

```
282:         try {
```
> بداية كتلة try. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:282]

```
283:             // Clear files dir subdirectories (legacy storage and outgoing)
```
> تعليق: امسح المجلدات الفرعية لمجلد الملفات (التخزين القديم والصادر). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:283]

```
284:             val filesDir = context.filesDir
```
> يُعرَّف متغيّر ثابت اسمه مجلد الملفات (filesDir) ويُسنَد إليه مجلد الملفات (filesDir) المأخوذ من السياق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:284]

```
285:             val dirsToClear = listOf(
```
> يُعرَّف متغيّر ثابت اسمه المجلدات الواجب مسحها (dirsToClear) ويُسنَد إليه قائمة (listOf) تبدأ هنا. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:285]

```
286:                 "files/incoming",
```
> عنصر القائمة: النص "files/incoming". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:286]

```
287:                 "files/outgoing",
```
> عنصر القائمة: النص "files/outgoing". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:287]

```
288:                 "images/incoming",
```
> عنصر القائمة: النص "images/incoming". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:288]

```
289:                 "images/outgoing",
```
> عنصر القائمة: النص "images/outgoing". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:289]

```
290:                 "voicenotes"
```
> عنصر القائمة: النص "voicenotes". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:290]

```
291:             )
```
> إغلاق نطاق استدعاء القائمة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:291]

```
292: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:292]

```
293:             dirsToClear.forEach { subDir ->
```
> يُستدعى على المجلدات الواجب مسحها forEach مع معامل لمدا اسمه المجلد الفرعي (subDir). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:293]

```
294:                 val dir = File(filesDir, subDir)
```
> يُعرَّف متغيّر ثابت اسمه المجلد (dir) ويُسنَد إليه كائن ملف (File) مبني من مجلد الملفات والمجلد الفرعي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:294]

```
295:                 if (dir.exists()) {
```
> شرط if: إذا كان المجلد موجوداً (exists). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:295]

```
296:                     dir.deleteRecursively()
```
> يُستدعى على المجلد deleteRecursively لحذفه تكرارياً. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:296]

```
297:                     Log.d(TAG, "Deleted media directory from filesDir: $subDir")
```
> يُستدعى Log.d بالوسم (TAG) ونصٍّ "Deleted media directory from filesDir:" متبوعاً بالمجلد الفرعي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:297]

```
298:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:298]

```
299:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:299]

```
300:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:300]

```
301:             // Clear cache dir subdirectories (new incoming storage)
```
> تعليق: امسح المجلدات الفرعية لمجلد التخزين المؤقت (تخزين الوارد الجديد). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:301]

```
302:             // Note: cacheDir.deleteRecursively() below would handle this, but being explicit ensures these
```
> تعليق: ملاحظة: deleteRecursively على مجلد التخزين المؤقت أدناه سيتولى هذا، لكن التصريح يضمن أنّ هذه. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:302]

```
303:             // specific media folders are targeted even if full cache clear fails or is modified later.
```
> تعليق: مجلدات الوسائط المحددة تُستهدَف حتى لو فشل المسح الكامل للتخزين المؤقت أو عُدِّل لاحقاً. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:303]

```
304:             val cacheDir = context.cacheDir
```
> يُعرَّف متغيّر ثابت اسمه مجلد التخزين المؤقت (cacheDir) ويُسنَد إليه مجلد التخزين المؤقت (cacheDir) المأخوذ من السياق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:304]

```
305:             val cacheDirsToClear = listOf(
```
> يُعرَّف متغيّر ثابت اسمه مجلدات التخزين المؤقت الواجب مسحها (cacheDirsToClear) ويُسنَد إليه قائمة (listOf) تبدأ هنا. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:305]

```
306:                 "files/incoming",
```
> عنصر القائمة: النص "files/incoming". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:306]

```
307:                 "images/incoming"
```
> عنصر القائمة: النص "images/incoming". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:307]

```
308:             )
```
> إغلاق نطاق استدعاء القائمة. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:308]

```
309:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:309]

```
310:             cacheDirsToClear.forEach { subDir ->
```
> يُستدعى على مجلدات التخزين المؤقت الواجب مسحها forEach مع معامل لمدا اسمه المجلد الفرعي (subDir). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:310]

```
311:                 val dir = File(cacheDir, subDir)
```
> يُعرَّف متغيّر ثابت اسمه المجلد (dir) ويُسنَد إليه كائن ملف (File) مبني من مجلد التخزين المؤقت والمجلد الفرعي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:311]

```
312:                 if (dir.exists()) {
```
> شرط if: إذا كان المجلد موجوداً (exists). [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:312]

```
313:                     dir.deleteRecursively()
```
> يُستدعى على المجلد deleteRecursively لحذفه تكرارياً. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:313]

```
314:                     Log.d(TAG, "Deleted media directory from cacheDir: $subDir")
```
> يُستدعى Log.d بالوسم (TAG) ونصٍّ "Deleted media directory from cacheDir:" متبوعاً بالمجلد الفرعي. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:314]

```
315:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:315]

```
316:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:316]

```
317:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:317]

```
318:             // Also clear entire cache dir as a catch-all
```
> تعليق: امسح أيضاً مجلد التخزين المؤقت بأكمله كإجراء شامل. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:318]

```
319:             context.cacheDir.deleteRecursively()
```
> يُستدعى على مجلد التخزين المؤقت المأخوذ من السياق deleteRecursively لحذفه تكرارياً. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:319]

```
320:             Log.d(TAG, "Cleared entire cache directory")
```
> يُستدعى Log.d بالوسم (TAG) والنص "Cleared entire cache directory". [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:320]

```
321: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:321]

```
322:         } catch (e: Exception) {
```
> بداية كتلة catch تلتقط استثناءً (Exception) في متغيّر اسمه e. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:322]

```
323:             Log.e(TAG, "Failed to clear media files", e)
```
> يُستدعى Log.e بالوسم (TAG) والنص "Failed to clear media files" والاستثناء e. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:323]

```
324:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:324]

```
325:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:325]

```
326: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/file/FileUtils.kt:326]
