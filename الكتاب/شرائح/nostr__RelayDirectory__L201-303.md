# شريحة — app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt (الأسطر 201–303)

```
201:                 val body = resp.body ?: return false
```
> يُعرَّف متغير ثابت اسمه «جسم الرد» (body) ويُسنَد إليه جسم الاستجابة (resp.body)، وإن كان فارغاً (null) تُعاد القيمة false من الدالة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:201]

```
202:                 FileOutputStream(dest).use { out ->
```
> يُنشأ تدفّق إخراج ملف (FileOutputStream) على الوجهة (dest) ويُستعمل داخل كتلة use باسم out. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:202]

```
203:                     body.byteStream().use { input ->
```
> يُستدعى byteStream على جسم الرد (body) لإنتاج تدفّق بايتات يُستعمل داخل كتلة use باسم input. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:203]

```
204:                         input.copyTo(out)
```
> يُستدعى copyTo على input لنسخ محتواه إلى out. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:204]

```
205:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:205]

```
206:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:206]

```
207:                 true
```
> تُعاد القيمة true كقيمة الكتلة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:207]

```
208:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:208]

```
209:         } catch (e: Exception) {
```
> تُلتقط استثناءات من نوع Exception في متغير اسمه e. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:209]

```
210:             Log.w(TAG, "Download error: ${e.message}")
```
> يُستدعى Log.w بوسم TAG ونص «Download error:» متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:210]

```
211:             false
```
> تُعاد القيمة false كقيمة كتلة الالتقاط. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:211]

```
212:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:212]

```
213:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:213]

```
214: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:214]

```
215:     private fun loadFromFile(file: File, sourceLabel: String): Boolean {
```
> تُعرَّف دالة خاصة (private) اسمها «التحميل من ملف» (loadFromFile) تأخذ معاملاً file من نوع File ومعاملاً sourceLabel من نوع String وتُعيد قيمة من نوع Boolean. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:215]

```
216:         return try {
```
> تُعاد قيمة كتلة try التالية. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:216]

```
217:             val list = parseCsv(FileInputStream(file))
```
> يُعرَّف متغير ثابت اسمه list ويُسنَد إليه ناتج استدعاء parseCsv على تدفّق إدخال ملف (FileInputStream) للملف file. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:217]

```
218:             if (list.isEmpty()) {
```
> شرط: إذا كانت list فارغة (isEmpty). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:218]

```
219:                 Log.w(TAG, "${sourceLabel} relay CSV has 0 entries; ignoring")
```
> يُستدعى Log.w بوسم TAG ونص يحوي قيمة sourceLabel متبوعة بعبارة «relay CSV has 0 entries; ignoring». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:219]

```
220:                 false
```
> تُعاد القيمة false كقيمة فرع if. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:220]

```
221:             } else {
```
> بداية فرع else. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:221]

```
222:                 synchronized(relaysLock) {
```
> تُنفَّذ كتلة متزامنة (synchronized) باستعمال القفل relaysLock. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:222]

```
223:                     relays.clear()
```
> يُستدعى clear على المجموعة relays لإفراغها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:223]

```
224:                     relays.addAll(list)
```
> يُستدعى addAll على المجموعة relays لإضافة كل عناصر list. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:224]

```
225:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:225]

```
226:                 val hash = fileSha256Hex(file)
```
> يُعرَّف متغير ثابت اسمه hash ويُسنَد إليه ناتج استدعاء fileSha256Hex على الملف file. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:226]

```
227:                 Log.i(TAG, "📄 Loaded ${list.size} relay entries from ${sourceLabel} file (${file.absolutePath}), sha256=$hash")
```
> يُستدعى Log.i بوسم TAG ونص يحوي حجم list (list.size) وقيمة sourceLabel والمسار المطلق للملف (file.absolutePath) وقيمة hash. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:227]

```
228:                 true
```
> تُعاد القيمة true كقيمة فرع else. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:228]

```
229:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:229]

```
230:         } catch (e: Exception) {
```
> تُلتقط استثناءات من نوع Exception في متغير اسمه e. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:230]

```
231:             Log.w(TAG, "Failed loading ${sourceLabel} relay file: ${e.message}")
```
> يُستدعى Log.w بوسم TAG ونص «Failed loading» متبوعاً بقيمة sourceLabel وعبارة «relay file:» ورسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:231]

```
232:             false
```
> تُعاد القيمة false كقيمة كتلة الالتقاط. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:232]

```
233:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:233]

```
234:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:234]

```
235: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:235]

```
236:     private fun loadFromAssets(application: Application) {
```
> تُعرَّف دالة خاصة (private) اسمها «التحميل من الأصول» (loadFromAssets) تأخذ معاملاً application من نوع Application. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:236]

```
237:         val list = try {
```
> يُعرَّف متغير ثابت اسمه list ويُسنَد إليه ناتج كتلة try التالية. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:237]

```
238:             parseCsv(application.assets.open(ASSET_FILE))
```
> يُستدعى parseCsv على التدفّق الناتج من فتح (open) الأصل ASSET_FILE من أصول التطبيق (application.assets). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:238]

```
239:         } catch (e: Exception) {
```
> تُلتقط استثناءات من نوع Exception في متغير اسمه e. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:239]

```
240:             Log.e(TAG, "Failed to open asset $ASSET_FILE: ${e.message}")
```
> يُستدعى Log.e بوسم TAG ونص «Failed to open asset» متبوعاً بقيمة ASSET_FILE ورسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:240]

```
241:             emptyList()
```
> تُعاد قائمة فارغة (emptyList) كقيمة كتلة الالتقاط. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:241]

```
242:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:242]

```
243:         synchronized(relaysLock) {
```
> تُنفَّذ كتلة متزامنة (synchronized) باستعمال القفل relaysLock. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:243]

```
244:             relays.clear()
```
> يُستدعى clear على المجموعة relays لإفراغها. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:244]

```
245:             relays.addAll(list)
```
> يُستدعى addAll على المجموعة relays لإضافة كل عناصر list. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:245]

```
246:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:246]

```
247:         // Compute asset hash for logging
```
> تعليق: احسب بصمة الأصل (hash) لأجل التسجيل. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:247]

```
248:         val hash = try {
```
> يُعرَّف متغير ثابت اسمه hash ويُسنَد إليه ناتج كتلة try التالية. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:248]

```
249:             application.assets.open(ASSET_FILE).use { input ->
```
> يُفتح الأصل ASSET_FILE من أصول التطبيق (application.assets) ويُستعمل داخل كتلة use باسم input. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:249]

```
250:                 streamSha256Hex(input)
```
> يُستدعى streamSha256Hex على input. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:250]

```
251:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:251]

```
252:         } catch (e: Exception) {
```
> تُلتقط استثناءات من نوع Exception في متغير اسمه e. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:252]

```
253:             "error:${'$'}{e.message}"
```
> تُعاد سلسلة نصية تبدأ بـ «error:» متبوعة برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:253]

```
254:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:254]

```
255:         Log.i(TAG, "📦 Loaded ${list.size} relay entries from assets/$ASSET_FILE, sha256=$hash")
```
> يُستدعى Log.i بوسم TAG ونص يحوي حجم list (list.size) وعبارة «relay entries from assets/» متبوعة بقيمة ASSET_FILE وقيمة hash. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:255]

```
256:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:256]

```
257: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:257]

```
258:     private fun parseCsv(input: InputStream): List<RelayInfo> {
```
> تُعرَّف دالة خاصة (private) اسمها «تحليل CSV» (parseCsv) تأخذ معاملاً input من نوع InputStream وتُعيد قائمة (List) من RelayInfo. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:258]

```
259:         val result = mutableListOf<RelayInfo>()
```
> يُعرَّف متغير ثابت اسمه result ويُسنَد إليه قائمة قابلة للتعديل (mutableListOf) من نوع RelayInfo. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:259]

```
260:         BufferedReader(InputStreamReader(input)).use { reader ->
```
> يُنشأ قارئ مُخزَّن (BufferedReader) يلف قارئ تدفّق إدخال (InputStreamReader) على input ويُستعمل داخل كتلة use باسم reader. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:260]

```
261:             var line: String?
```
> يُعرَّف متغير متغيّر (var) اسمه line من نوع String قابل للنُل (nullable). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:261]

```
262:             while (true) {
```
> تبدأ حلقة while بشرط true (حلقة لا تنتهي إلا بكسر داخلي). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:262]

```
263:                 line = reader.readLine()
```
> يُسنَد إلى line ناتج استدعاء readLine على reader. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:263]

```
264:                 if (line == null) break
```
> شرط: إذا كان line يساوي null يُكسَر (break) من الحلقة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:264]

```
265:                 val trimmed = line!!.trim()
```
> يُعرَّف متغير ثابت اسمه trimmed ويُسنَد إليه ناتج trim على line (بعد تأكيد عدم النُل بـ !!). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:265]

```
266:                 if (trimmed.isEmpty()) continue
```
> شرط: إذا كان trimmed فارغاً (isEmpty) يُتابَع (continue) إلى التكرار التالي. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:266]

```
267:                 if (trimmed.lowercase().startsWith("relay url")) continue
```
> شرط: إذا كان trimmed بعد تحويله إلى أحرف صغيرة (lowercase) يبدأ بـ «relay url» يُتابَع (continue). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:267]

```
268:                 val parts = trimmed.split(",")
```
> يُعرَّف متغير ثابت اسمه parts ويُسنَد إليه ناتج تقسيم (split) trimmed على الفاصلة «,». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:268]

```
269:                 if (parts.size < 3) continue
```
> شرط: إذا كان حجم parts أقل من 3 يُتابَع (continue). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:269]

```
270:                 val url = normalizeRelayUrl(parts[0].trim())
```
> يُعرَّف متغير ثابت اسمه url ويُسنَد إليه ناتج normalizeRelayUrl على العنصر الأول من parts بعد trim. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:270]

```
271:                 val lat = parts[1].trim().toDoubleOrNull()
```
> يُعرَّف متغير ثابت اسمه lat ويُسنَد إليه تحويل العنصر الثاني من parts بعد trim إلى عدد عشري أو null (toDoubleOrNull). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:271]

```
272:                 val lon = parts[2].trim().toDoubleOrNull()
```
> يُعرَّف متغير ثابت اسمه lon ويُسنَد إليه تحويل العنصر الثالث من parts بعد trim إلى عدد عشري أو null (toDoubleOrNull). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:272]

```
273:                 if (url.isEmpty() || lat == null || lon == null) continue
```
> شرط: إذا كان url فارغاً أو lat يساوي null أو lon يساوي null يُتابَع (continue). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:273]

```
274:                 result.add(RelayInfo(url = url, latitude = lat, longitude = lon))
```
> يُستدعى add على result لإضافة عنصر RelayInfo بقيم url للحقل url وlat للحقل latitude وlon للحقل longitude. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:274]

```
275:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:275]

```
276:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:276]

```
277:         return result
```
> تُعاد القائمة result. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:277]

```
278:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:278]

```
279: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:279]

```
280:     private fun fileSha256Hex(file: File): String = try {
```
> تُعرَّف دالة خاصة (private) اسمها «بصمة الملف SHA256 بالست عشري» (fileSha256Hex) تأخذ معاملاً file من نوع File وتُعيد String، وقيمتها ناتج كتلة try التالية. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:280]

```
281:         FileInputStream(file).use { input ->
```
> يُنشأ تدفّق إدخال ملف (FileInputStream) على file ويُستعمل داخل كتلة use باسم input. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:281]

```
282:             streamSha256Hex(input)
```
> يُستدعى streamSha256Hex على input. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:282]

```
283:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:283]

```
284:     } catch (_: Exception) { "error" }
```
> تُلتقط استثناءات من نوع Exception بمعامل مُهمَل (_) وتُعاد سلسلة «error». [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:284]

```
285: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:285]

```
286:     private fun streamSha256Hex(input: InputStream): String {
```
> تُعرَّف دالة خاصة (private) اسمها «بصمة التدفّق SHA256 بالست عشري» (streamSha256Hex) تأخذ معاملاً input من نوع InputStream وتُعيد String. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:286]

```
287:         val digest = MessageDigest.getInstance("SHA-256")
```
> يُعرَّف متغير ثابت اسمه digest ويُسنَد إليه نسخة MessageDigest بخوارزمية «SHA-256» عبر getInstance. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:287]

```
288:         val buf = ByteArray(8192)
```
> يُعرَّف متغير ثابت اسمه buf ويُسنَد إليه مصفوفة بايتات (ByteArray) بحجم 8192. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:288]

```
289:         var read: Int
```
> يُعرَّف متغير متغيّر (var) اسمه read من نوع Int. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:289]

```
290:         while (true) {
```
> تبدأ حلقة while بشرط true (حلقة لا تنتهي إلا بكسر داخلي). [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:290]

```
291:             read = input.read(buf)
```
> يُسنَد إلى read ناتج استدعاء read على input بتمرير buf. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:291]

```
292:             if (read <= 0) break
```
> شرط: إذا كان read أقل من أو يساوي 0 يُكسَر (break) من الحلقة. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:292]

```
293:             digest.update(buf, 0, read)
```
> يُستدعى update على digest بتمرير buf والإزاحة 0 والطول read. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:293]

```
294:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:294]

```
295:         val bytes = digest.digest()
```
> يُعرَّف متغير ثابت اسمه bytes ويُسنَد إليه ناتج استدعاء digest على digest. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:295]

```
296:         return bytes.joinToString("") { b ->
```
> تُعاد سلسلة ناتجة من joinToString على bytes بفاصل فارغ، ولكل عنصر b تُطبَّق الكتلة التالية. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:296]

```
297:             val v = b.toInt() and 0xff
```
> يُعرَّف متغير ثابت اسمه v ويُسنَد إليه تحويل b إلى Int (toInt) مع تطبيق AND ثنائي بـ 0xff. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:297]

```
298:             val s = Integer.toHexString(v)
```
> يُعرَّف متغير ثابت اسمه s ويُسنَد إليه التمثيل الست عشري لـ v عبر Integer.toHexString. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:298]

```
299:             if (s.length == 1) "0$s" else s
```
> شرط: إذا كان طول s يساوي 1 تُعاد «0» متبوعة بـ s، وإلا تُعاد s. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:299]

```
300:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:300]

```
301:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:301]

```
302: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:302]

```
303: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/RelayDirectory.kt:303]
