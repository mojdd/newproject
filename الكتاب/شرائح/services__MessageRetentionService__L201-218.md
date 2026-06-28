# شريحة — app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt (الأسطر 201–218)

```
201: //
```
> تعليق: سطر تعليق فارغ بعد علامتَي الشرطة المائلة، لا يحمل أي نص. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:201]

```
202: //    suspend fun getTotalStoredMessagesCount(): Int = withContext(Dispatchers.IO) {
```
> تعليق: تعريف دالة معلّقة معلّقة (مكتوبة كتعليق) باسم getTotalStoredMessagesCount معلّقة (دالة عدّ الرسائل المخزّنة الكلّي) من نوع suspend (دالة قابلة للتعليق)، تُعيد قيمة من نوع Int (عدد صحيح) وتُساوي ناتج استدعاء withContext (تنفيذ ضمن سياق) بالوسيط Dispatchers.IO (موزِّع الإدخال/الإخراج) ويفتح كتلة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:202]

```
203: //        var totalCount = 0
```
> تعليق: إعلان متغيّر متبدّل (var) باسم totalCount (العدد الكلّي) وتعيين قيمته الابتدائية صفراً. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:203]

```
204: //
```
> تعليق: سطر تعليق فارغ بعد علامتَي الشرطة المائلة، لا يحمل أي نص. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:204]

```
205: //        try {
```
> تعليق: بداية كتلة try (المحاولة) وفتح نطاقها. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:205]

```
206: //            retentionDir.listFiles()?.forEach { file ->
```
> تعليق: استدعاء الدالة listFiles (سرد الملفات) على retentionDir (دليل الاحتفاظ) مع استدعاء آمن (?.) ثم استدعاء forEach (لكلّ عنصر) بكتلة لامبدا تأخذ المعامل file (ملف). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:206]

```
207: //                if (file.name.startsWith("channel_") && file.name.endsWith(".dat")) {
```
> تعليق: شرط if (إذا) يتحقّق أنّ خاصية name (الاسم) للملف تبدأ بـ startsWith (يبدأ بـ) القيمة "channel_" وأنّ name تنتهي بـ endsWith (ينتهي بـ) القيمة ".dat"، مع عامل الوصل المنطقي && (و)، ويفتح كتلة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:207]

```
208: //                    val messages = loadMessagesFromFile(file)
```
> تعليق: إعلان قيمة ثابتة (val) باسم messages (الرسائل) وتعيينها ناتج استدعاء loadMessagesFromFile (تحميل الرسائل من ملف) بالوسيط file. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:208]

```
209: //                    totalCount += messages.size
```
> تعليق: زيادة المتغيّر totalCount بقيمة خاصية size (الحجم) لـ messages عبر عامل الجمع والتعيين (+=). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:209]

```
210: //                }
```
> تعليق: إغلاق نطاق كتلة الشرط if. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:210]

```
211: //            }
```
> تعليق: إغلاق نطاق كتلة لامبدا الخاصة بـ forEach. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:211]

```
212: //        } catch (e: Exception) {
```
> تعليق: إغلاق نطاق كتلة try وبداية كتلة catch (الالتقاط) التي تلتقط معامل e من نوع Exception (استثناء) وتفتح نطاقها. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:212]

```
213: //            Log.e(TAG, "Failed to count stored messages", e)
```
> تعليق: استدعاء الدالة Log.e (تسجيل خطأ) بالوسطاء TAG (الوسم) والنص "Failed to count stored messages" والاستثناء e. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:213]

```
214: //        }
```
> تعليق: إغلاق نطاق كتلة catch. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:214]

```
215: //
```
> تعليق: سطر تعليق فارغ بعد علامتَي الشرطة المائلة، لا يحمل أي نص. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:215]

```
216: //        totalCount
```
> تعليق: السطر يحمل المتغيّر totalCount وحده كقيمة معادة من كتلة withContext. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:216]

```
217: //    }
```
> تعليق: إغلاق نطاق دالة getTotalStoredMessagesCount. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:217]

```
218: //}
```
> تعليق: إغلاق نطاق الصنف (إغلاق القوس الأخير للملف). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:218]
