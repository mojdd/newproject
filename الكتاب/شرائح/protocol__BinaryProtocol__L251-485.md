# شريحة — app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt (الأسطر 251–485)

```
251:             buffer.put(flags.toByte())
```
> يضع في المخزن المؤقت (buffer) قيمة الأعلام (flags) بعد تحويلها إلى بايت بالدالة toByte. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:251]

```
252:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:252]

```
253:             // Payload length (2 or 4 bytes, big-endian) - includes original size if compressed
```
> تعليق: طول الحمولة (٢ أو ٤ بايت، ترتيب البايت الكبير أولاً) - يتضمن الحجم الأصلي إن كانت مضغوطة. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:253]

```
254:             val payloadDataSize = payload.size + sizeFieldBytes
```
> يعرّف متغيّراً ثابتاً (val) باسم حجم بيانات الحمولة (payloadDataSize) قيمته حجم الحمولة (payload.size) مضافاً إليه عدد بايتات حقل الحجم (sizeFieldBytes). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:254]

```
255:             if (packet.version >= 2u.toUByte()) {
```
> يبدأ شرطاً يتحقق إن كان إصدار الحزمة (packet.version) أكبر من أو يساوي الرقم ٢ غير المُوقَّع (2u.toUByte). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:255]

```
256:                 buffer.putInt(payloadDataSize)  // 4 bytes for v2+
```
> يضع حجم بيانات الحمولة (payloadDataSize) في المخزن المؤقت كعدد صحيح بالدالة putInt؛ تعليق: ٤ بايتات للإصدار الثاني فأعلى. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:256]

```
257:             } else {
```
> إغلاق نطاق الشرط، وبدء فرع البديل (else). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:257]

```
258:                 if (payloadDataSize > 0xFFFF || (originalPayloadSize ?: 0) > 0xFFFF) {
```
> يبدأ شرطاً يتحقق إن كان حجم بيانات الحمولة (payloadDataSize) أكبر من القيمة 0xFFFF (٦٥٥٣٥)، أو كان حجم الحمولة الأصلي (originalPayloadSize) — أو الصفر إن كان معدوماً — أكبر من 0xFFFF. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:258]

```
259:                     Log.w("BinaryProtocol", "Cannot encode oversized v1 packet payload: $payloadDataSize bytes")
```
> يسجّل تحذيراً (Log.w) بالوسم "BinaryProtocol" نصّه: تعذّر ترميز حمولة حزمة من الإصدار الأول مفرطة الحجم بمقدار قيمة payloadDataSize بايت. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:259]

```
260:                     return null
```
> يعيد القيمة المعدومة (null). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:260]

```
261:                 }
```
> إغلاق نطاق الشرط الداخلي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:261]

```
262:                 buffer.putShort(payloadDataSize.toShort())  // 2 bytes for v1
```
> يضع حجم بيانات الحمولة (payloadDataSize) بعد تحويله إلى عدد قصير بالدالة toShort في المخزن المؤقت بالدالة putShort؛ تعليق: ٢ بايت للإصدار الأول. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:262]

```
263:             }
```
> إغلاق نطاق فرع البديل (else). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:263]

```
264:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:264]

```
265:             // SenderID (exactly 8 bytes)
```
> تعليق: معرّف المُرسِل (SenderID) (٨ بايتات بالضبط). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:265]

```
266:             val senderBytes = packet.senderID.take(SENDER_ID_SIZE).toByteArray()
```
> يعرّف متغيّراً ثابتاً باسم بايتات المُرسِل (senderBytes) قيمته أول عدد من بايتات معرّف المُرسِل (packet.senderID) مقداره ثابت حجم معرّف المُرسِل (SENDER_ID_SIZE) محوَّلاً إلى مصفوفة بايتات بالدالة toByteArray. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:266]

```
267:             buffer.put(senderBytes)
```
> يضع بايتات المُرسِل (senderBytes) في المخزن المؤقت. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:267]

```
268:             if (senderBytes.size < SENDER_ID_SIZE) {
```
> يبدأ شرطاً يتحقق إن كان حجم بايتات المُرسِل (senderBytes.size) أصغر من ثابت حجم معرّف المُرسِل (SENDER_ID_SIZE). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:268]

```
269:                 buffer.put(ByteArray(SENDER_ID_SIZE - senderBytes.size))
```
> يضع في المخزن المؤقت مصفوفة بايتات (ByteArray) طولها ثابت حجم معرّف المُرسِل (SENDER_ID_SIZE) ناقص حجم بايتات المُرسِل (senderBytes.size). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:269]

```
270:             }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:270]

```
271:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:271]

```
272:             // RecipientID (if present)
```
> تعليق: معرّف المُستقبِل (RecipientID) (إن وُجد). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:272]

```
273:             packet.recipientID?.let { recipientID ->
```
> ينفّذ الكتلة التالية على معرّف المُستقبِل (packet.recipientID) عبر الدالة let إن لم يكن معدوماً، ويسمّي القيمة recipientID. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:273]

```
274:                 val recipientBytes = recipientID.take(RECIPIENT_ID_SIZE).toByteArray()
```
> يعرّف متغيّراً ثابتاً باسم بايتات المُستقبِل (recipientBytes) قيمته أول عدد من بايتات معرّف المُستقبِل (recipientID) مقداره ثابت حجم معرّف المُستقبِل (RECIPIENT_ID_SIZE) محوَّلاً إلى مصفوفة بايتات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:274]

```
275:                 buffer.put(recipientBytes)
```
> يضع بايتات المُستقبِل (recipientBytes) في المخزن المؤقت. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:275]

```
276:                 if (recipientBytes.size < RECIPIENT_ID_SIZE) {
```
> يبدأ شرطاً يتحقق إن كان حجم بايتات المُستقبِل (recipientBytes.size) أصغر من ثابت حجم معرّف المُستقبِل (RECIPIENT_ID_SIZE). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:276]

```
277:                     buffer.put(ByteArray(RECIPIENT_ID_SIZE - recipientBytes.size))
```
> يضع في المخزن المؤقت مصفوفة بايتات طولها ثابت حجم معرّف المُستقبِل (RECIPIENT_ID_SIZE) ناقص حجم بايتات المُستقبِل (recipientBytes.size). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:277]

```
278:                 }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:278]

```
279:             }
```
> إغلاق نطاق كتلة let الخاصة بمعرّف المُستقبِل. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:279]

```
280: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:280]

```
281:             // Route (optional, v2+ only): 1 byte count + N*8 bytes
```
> تعليق: المسار (Route) (اختياري، للإصدار الثاني فأعلى فقط): بايت واحد للعدّ + N×٨ بايتات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:281]

```
282:             if (packet.version >= 2u.toUByte() && !packet.route.isNullOrEmpty()) {
```
> يبدأ شرطاً يتحقق إن كان إصدار الحزمة (packet.version) أكبر من أو يساوي ٢، وفي الوقت نفسه كان مسار الحزمة (packet.route) غير معدوم وغير فارغ (isNullOrEmpty منفيّة). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:282]

```
283:                 packet.route?.let { routeList ->
```
> ينفّذ الكتلة التالية على مسار الحزمة (packet.route) عبر let إن لم يكن معدوماً، ويسمّي القيمة قائمة المسار (routeList). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:283]

```
284:                     val cleaned = routeList.map { bytes -> bytes.take(SENDER_ID_SIZE).toByteArray().let { if (it.size < SENDER_ID_SIZE) it + ByteArray(SENDER_ID_SIZE - it.size) else it } }
```
> يعرّف متغيّراً ثابتاً باسم المسار المُنقّى (cleaned) قيمته تحويل كل عنصر بايتات (bytes) في قائمة المسار بأخذ أوائل بايتاته بمقدار ثابت حجم معرّف المُرسِل (SENDER_ID_SIZE) وتحويلها إلى مصفوفة بايتات، ثم إن كان حجمها أصغر من SENDER_ID_SIZE تُلحق بها مصفوفة بايتات لإتمام الطول، وإلا تُترك كما هي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:284]

```
285:                     val count = cleaned.size.coerceAtMost(255)
```
> يعرّف متغيّراً ثابتاً باسم العدّ (count) قيمته حجم المسار المُنقّى (cleaned.size) مقيّداً بحدّ أقصى ٢٥٥ بالدالة coerceAtMost. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:285]

```
286:                     buffer.put(count.toByte())
```
> يضع العدّ (count) بعد تحويله إلى بايت في المخزن المؤقت. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:286]

```
287:                     cleaned.take(count).forEach { hop -> buffer.put(hop) }
```
> يأخذ أوائل عناصر المسار المُنقّى بمقدار العدّ (count) ويضع كل قفزة (hop) منها في المخزن المؤقت بالدالة forEach. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:287]

```
288:                 }
```
> إغلاق نطاق كتلة let الخاصة بقائمة المسار. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:288]

```
289:             }
```
> إغلاق نطاق شرط المسار. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:289]

```
290:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:290]

```
291:             // Payload (with original size prepended if compressed)
```
> تعليق: الحمولة (Payload) (مع الحجم الأصلي مُسبَقاً أمامها إن كانت مضغوطة). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:291]

```
292:             if (isCompressed) {
```
> يبدأ شرطاً يتحقق إن كانت الحمولة مضغوطة (isCompressed). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:292]

```
293:                 val originalSize = originalPayloadSize
```
> يعرّف متغيّراً ثابتاً باسم الحجم الأصلي (originalSize) قيمته حجم الحمولة الأصلي (originalPayloadSize). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:293]

```
294:                 if (originalSize != null) {
```
> يبدأ شرطاً يتحقق إن كان الحجم الأصلي (originalSize) غير معدوم. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:294]

```
295:                     if (packet.version >= 2u.toUByte()) {
```
> يبدأ شرطاً يتحقق إن كان إصدار الحزمة (packet.version) أكبر من أو يساوي ٢. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:295]

```
296:                         buffer.putInt(originalSize.toInt())
```
> يضع الحجم الأصلي (originalSize) بعد تحويله إلى عدد صحيح في المخزن المؤقت بالدالة putInt. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:296]

```
297:                     } else {
```
> إغلاق نطاق الشرط، وبدء فرع البديل (else). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:297]

```
298:                         buffer.putShort(originalSize.toShort())
```
> يضع الحجم الأصلي (originalSize) بعد تحويله إلى عدد قصير في المخزن المؤقت بالدالة putShort. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:298]

```
299:                     }
```
> إغلاق نطاق فرع البديل (else). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:299]

```
300:                 }
```
> إغلاق نطاق شرط الحجم الأصلي غير المعدوم. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:300]

```
301:             }
```
> إغلاق نطاق شرط الضغط (isCompressed). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:301]

```
302:             buffer.put(payload)
```
> يضع الحمولة (payload) في المخزن المؤقت. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:302]

```
303:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:303]

```
304:             // Signature (if present)
```
> تعليق: التوقيع (Signature) (إن وُجد). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:304]

```
305:             packet.signature?.let { signature ->
```
> ينفّذ الكتلة التالية على توقيع الحزمة (packet.signature) عبر let إن لم يكن معدوماً، ويسمّي القيمة signature. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:305]

```
306:                 buffer.put(signature.take(SIGNATURE_SIZE).toByteArray())
```
> يضع في المخزن المؤقت أوائل بايتات التوقيع (signature) بمقدار ثابت حجم التوقيع (SIGNATURE_SIZE) محوَّلة إلى مصفوفة بايتات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:306]

```
307:             }
```
> إغلاق نطاق كتلة let الخاصة بالتوقيع. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:307]

```
308:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:308]

```
309:             val result = ByteArray(buffer.position())
```
> يعرّف متغيّراً ثابتاً باسم النتيجة (result) قيمته مصفوفة بايتات (ByteArray) طولها موضع المخزن المؤقت الحالي (buffer.position). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:309]

```
310:             buffer.rewind()
```
> يعيد المخزن المؤقت إلى بدايته بالدالة rewind. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:310]

```
311:             buffer.get(result)
```
> يقرأ من المخزن المؤقت ملء مصفوفة النتيجة (result) بالدالة get. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:311]

```
312:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:312]

```
313:             // Apply padding if requested (iOS-compatible: selective padding for privacy)
```
> تعليق: طبّق الحشو (padding) إن طُلب (متوافق مع iOS: حشو انتقائي للخصوصية). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:313]

```
314:             if (padding) {
```
> يبدأ شرطاً يتحقق إن كان مُعامِل الحشو (padding) صحيحاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:314]

```
315:                 val optimalSize = MessagePadding.optimalBlockSize(result.size)
```
> يعرّف متغيّراً ثابتاً باسم الحجم الأمثل (optimalSize) قيمته ناتج استدعاء دالة الحجم الأمثل للكتلة (MessagePadding.optimalBlockSize) على حجم النتيجة (result.size). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:315]

```
316:                 return MessagePadding.pad(result, optimalSize)
```
> يعيد ناتج استدعاء دالة الحشو (MessagePadding.pad) على النتيجة (result) والحجم الأمثل (optimalSize). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:316]

```
317:             }
```
> إغلاق نطاق شرط الحشو. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:317]

```
318:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:318]

```
319:             return result
```
> يعيد النتيجة (result). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:319]

```
320:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:320]

```
321:         } catch (e: Exception) {
```
> يلتقط استثناءً من النوع Exception ويسمّيه e. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:321]

```
322:             Log.e("BinaryProtocol", "Error encoding packet type ${packet.type}: ${e.message}")
```
> يسجّل خطأً (Log.e) بالوسم "BinaryProtocol" نصّه: خطأ في ترميز نوع الحزمة (packet.type) متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:322]

```
323:             return null
```
> يعيد القيمة المعدومة (null). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:323]

```
324:         }
```
> إغلاق نطاق كتلة التقاط الاستثناء (catch). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:324]

```
325:     }
```
> إغلاق نطاق دالة الترميز (encode). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:325]

```
326:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:326]

```
327:     fun decode(data: ByteArray): BitchatPacket? {
```
> يعرّف دالة فكّ الترميز (decode) تأخذ مصفوفة بايتات (data) من نوع ByteArray وتعيد حزمة بِت-تشات (BitchatPacket) قد تكون معدومة. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:327]

```
328:         // Try decode as-is first (robust when padding wasn't applied) - iOS fix
```
> تعليق: جرّب فكّ الترميز كما هي أولاً (متين حين لم يُطبَّق الحشو) - إصلاح iOS. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:328]

```
329:         decodeCore(data)?.let { return it }
```
> يستدعي دالة فكّ الترميز الجوهرية (decodeCore) على البيانات (data)، وإن لم تكن النتيجة معدومة يعيدها عبر let. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:329]

```
330:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:330]

```
331:         // If that fails, try after removing padding
```
> تعليق: إن فشل ذلك، جرّب بعد إزالة الحشو. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:331]

```
332:         val unpadded = MessagePadding.unpad(data)
```
> يعرّف متغيّراً ثابتاً باسم المنزوع الحشو (unpadded) قيمته ناتج استدعاء دالة نزع الحشو (MessagePadding.unpad) على البيانات (data). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:332]

```
333:         if (unpadded.contentEquals(data)) return null // No padding was removed, already failed
```
> يبدأ شرطاً يعيد القيمة المعدومة إن كان محتوى المنزوع الحشو (unpadded) مساوياً لمحتوى البيانات (data) عبر contentEquals؛ تعليق: لم يُزَل أي حشو، وقد فشلت سابقاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:333]

```
334:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:334]

```
335:         return decodeCore(unpadded)
```
> يعيد ناتج استدعاء دالة فكّ الترميز الجوهرية (decodeCore) على المنزوع الحشو (unpadded). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:335]

```
336:     }
```
> إغلاق نطاق دالة فكّ الترميز (decode). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:336]

```
337:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:337]

```
338:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:338]

```
339:      * Core decoding implementation used by decode() with and without padding removal - iOS fix
```
> تعليق: التنفيذ الجوهري لفكّ الترميز المستخدم من قِبل decode() مع إزالة الحشو وبدونها - إصلاح iOS. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:339]

```
340:      */
```
> نهاية التعليق التوثيقي (KDoc). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:340]

```
341:     private fun decodeCore(raw: ByteArray): BitchatPacket? {
```
> يعرّف دالة خاصة (private) باسم فكّ الترميز الجوهري (decodeCore) تأخذ مصفوفة بايتات خام (raw) من نوع ByteArray وتعيد حزمة بِت-تشات (BitchatPacket) قد تكون معدومة. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:341]

```
342:         try {
```
> يبدأ كتلة المحاولة (try). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:342]

```
343:             if (raw.size < HEADER_SIZE_V1 + SENDER_ID_SIZE) return null
```
> يبدأ شرطاً يعيد القيمة المعدومة إن كان حجم البيانات الخام (raw.size) أصغر من مجموع ثابت حجم ترويسة الإصدار الأول (HEADER_SIZE_V1) وثابت حجم معرّف المُرسِل (SENDER_ID_SIZE). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:343]

```
344: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:344]

```
345:             val buffer = ByteBuffer.wrap(raw).apply { order(ByteOrder.BIG_ENDIAN) }
```
> يعرّف متغيّراً ثابتاً باسم المخزن المؤقت (buffer) قيمته تغليف البيانات الخام (ByteBuffer.wrap على raw) مع ضبط ترتيب البايت إلى الكبير أولاً (ByteOrder.BIG_ENDIAN) بالدالة apply. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:345]

```
346: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:346]

```
347:             // Header
```
> تعليق: الترويسة (Header). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:347]

```
348:             val version = buffer.get().toUByte()
```
> يعرّف متغيّراً ثابتاً باسم الإصدار (version) قيمته بايت يُقرأ من المخزن المؤقت بالدالة get محوَّلاً إلى بايت غير مُوقَّع بالدالة toUByte. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:348]

```
349:             if (version.toUInt() != 1u && version.toUInt() != 2u) return null  // Support v1 and v2
```
> يبدأ شرطاً يعيد القيمة المعدومة إن كان الإصدار (version) لا يساوي ١ ولا يساوي ٢؛ تعليق: دعم الإصدارين الأول والثاني. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:349]

```
350: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:350]

```
351:             val headerSize = getHeaderSize(version)
```
> يعرّف متغيّراً ثابتاً باسم حجم الترويسة (headerSize) قيمته ناتج استدعاء دالة حجم الترويسة (getHeaderSize) على الإصدار (version). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:351]

```
352: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:352]

```
353:             val type = buffer.get().toUByte()
```
> يعرّف متغيّراً ثابتاً باسم النوع (type) قيمته بايت يُقرأ من المخزن المؤقت محوَّلاً إلى بايت غير مُوقَّع. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:353]

```
354:             val ttl = buffer.get().toUByte()
```
> يعرّف متغيّراً ثابتاً باسم مدّة البقاء (ttl) قيمته بايت يُقرأ من المخزن المؤقت محوَّلاً إلى بايت غير مُوقَّع. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:354]

```
355: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:355]

```
356:             // Timestamp
```
> تعليق: الطابع الزمني (Timestamp). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:356]

```
357:             val timestamp = buffer.getLong().toULong()
```
> يعرّف متغيّراً ثابتاً باسم الطابع الزمني (timestamp) قيمته عدد طويل يُقرأ من المخزن المؤقت بالدالة getLong محوَّلاً إلى عدد طويل غير مُوقَّع بالدالة toULong. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:357]

```
358: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:358]

```
359:             // Flags
```
> تعليق: الأعلام (Flags). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:359]

```
360:             val flags = buffer.get().toUByte()
```
> يعرّف متغيّراً ثابتاً باسم الأعلام (flags) قيمته بايت يُقرأ من المخزن المؤقت محوَّلاً إلى بايت غير مُوقَّع. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:360]

```
361:             val hasRecipient = (flags and Flags.HAS_RECIPIENT) != 0u.toUByte()
```
> يعرّف متغيّراً ثابتاً باسم وجود مُستقبِل (hasRecipient) قيمته صحيحة إن كان ناتج «و» المنطقي البِتّي بين الأعلام (flags) وعلَم وجود المُستقبِل (Flags.HAS_RECIPIENT) لا يساوي صفراً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:361]

```
362:             val hasSignature = (flags and Flags.HAS_SIGNATURE) != 0u.toUByte()
```
> يعرّف متغيّراً ثابتاً باسم وجود توقيع (hasSignature) قيمته صحيحة إن كان ناتج «و» البِتّي بين الأعلام (flags) وعلَم وجود التوقيع (Flags.HAS_SIGNATURE) لا يساوي صفراً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:362]

```
363:             val isCompressed = (flags and Flags.IS_COMPRESSED) != 0u.toUByte()
```
> يعرّف متغيّراً ثابتاً باسم الانضغاط (isCompressed) قيمته صحيحة إن كان ناتج «و» البِتّي بين الأعلام (flags) وعلَم الانضغاط (Flags.IS_COMPRESSED) لا يساوي صفراً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:363]

```
364:             // HAS_ROUTE is only valid for v2+ packets; ignore the flag for v1
```
> تعليق: علَم وجود المسار (HAS_ROUTE) صالح فقط لحزم الإصدار الثاني فأعلى؛ تجاهل العلَم للإصدار الأول. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:364]

```
365:             val hasRoute = (version >= 2u.toUByte()) && (flags and Flags.HAS_ROUTE) != 0u.toUByte()
```
> يعرّف متغيّراً ثابتاً باسم وجود مسار (hasRoute) قيمته صحيحة إن كان الإصدار (version) أكبر من أو يساوي ٢، وفي الوقت نفسه ناتج «و» البِتّي بين الأعلام (flags) وعلَم وجود المسار (Flags.HAS_ROUTE) لا يساوي صفراً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:365]

```
366: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:366]

```
367:             // Payload length - version-dependent (2 or 4 bytes)
```
> تعليق: طول الحمولة - يعتمد على الإصدار (٢ أو ٤ بايت). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:367]

```
368:             val payloadLength = if (version >= 2u.toUByte()) {
```
> يعرّف متغيّراً ثابتاً باسم طول الحمولة (payloadLength) بادئاً تعبيراً شرطياً يتحقق إن كان الإصدار (version) أكبر من أو يساوي ٢. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:368]

```
369:                 buffer.getInt().toUInt()  // 4 bytes for v2+
```
> يقرأ من المخزن المؤقت عدداً صحيحاً بالدالة getInt محوَّلاً إلى عدد صحيح غير مُوقَّع بالدالة toUInt؛ تعليق: ٤ بايتات للإصدار الثاني فأعلى. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:369]

```
370:             } else {
```
> إغلاق نطاق فرع الشرط، وبدء فرع البديل (else). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:370]

```
371:                 buffer.getShort().toUShort().toUInt()  // 2 bytes for v1, convert to UInt
```
> يقرأ من المخزن المؤقت عدداً قصيراً بالدالة getShort محوَّلاً إلى عدد قصير غير مُوقَّع ثم إلى عدد صحيح غير مُوقَّع (toUInt)؛ تعليق: ٢ بايت للإصدار الأول، يُحوَّل إلى UInt. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:371]

```
372:             }
```
> إغلاق نطاق التعبير الشرطي لطول الحمولة. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:372]

```
373: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:373]

```
374:             if (payloadLength > com.bitchat.android.util.AppConstants.Protocol.MAX_PAYLOAD_LENGTH.toUInt()) {
```
> يبدأ شرطاً يتحقق إن كان طول الحمولة (payloadLength) أكبر من ثابت أقصى طول للحمولة (AppConstants.Protocol.MAX_PAYLOAD_LENGTH) محوَّلاً إلى عدد صحيح غير مُوقَّع. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:374]

```
375:                 Log.w("BinaryProtocol", "Payload length ${payloadLength} exceeds maximum allowed (${com.bitchat.android.util.AppConstants.Protocol.MAX_PAYLOAD_LENGTH})")
```
> يسجّل تحذيراً (Log.w) بالوسم "BinaryProtocol" نصّه: طول الحمولة (payloadLength) يتجاوز الحدّ الأقصى المسموح (MAX_PAYLOAD_LENGTH). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:375]

```
376:                 return null
```
> يعيد القيمة المعدومة (null). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:376]

```
377:             }
```
> إغلاق نطاق شرط تجاوز طول الحمولة. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:377]

```
378: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:378]

```
379:             var expectedSize = headerSize + SENDER_ID_SIZE + payloadLength.toInt()
```
> يعرّف متغيّراً متبدّلاً (var) باسم الحجم المتوقَّع (expectedSize) قيمته مجموع حجم الترويسة (headerSize) وثابت حجم معرّف المُرسِل (SENDER_ID_SIZE) وطول الحمولة (payloadLength) محوَّلاً إلى عدد صحيح. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:379]

```
380:             if (hasRecipient) expectedSize += RECIPIENT_ID_SIZE
```
> يبدأ شرطاً يزيد الحجم المتوقَّع (expectedSize) بمقدار ثابت حجم معرّف المُستقبِل (RECIPIENT_ID_SIZE) إن كان وجود مُستقبِل (hasRecipient) صحيحاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:380]

```
381:             var routeCount = 0
```
> يعرّف متغيّراً متبدّلاً باسم عدّ المسار (routeCount) قيمته الابتدائية صفر. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:381]

```
382:             if (hasRoute) {
```
> يبدأ شرطاً يتحقق إن كان وجود مسار (hasRoute) صحيحاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:382]

```
383:                 // Peek count (1 byte) without consuming buffer for now
```
> تعليق: استطلِع العدّ (بايت واحد) دون استهلاك المخزن المؤقت حالياً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:383]

```
384:                 // The buffer is currently positioned at the start of SenderID (after fixed header)
```
> تعليق: المخزن المؤقت موضوعه الآن عند بداية معرّف المُرسِل (بعد الترويسة الثابتة). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:384]

```
385:                 // We must skip SenderID and RecipientID (if present) to find the route count
```
> تعليق: علينا تخطّي معرّف المُرسِل ومعرّف المُستقبِل (إن وُجد) لإيجاد عدّ المسار. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:385]

```
386:                 val currentPos = buffer.position()
```
> يعرّف متغيّراً ثابتاً باسم الموضع الحالي (currentPos) قيمته موضع المخزن المؤقت (buffer.position). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:386]

```
387:                 var routeOffset = currentPos + SENDER_ID_SIZE
```
> يعرّف متغيّراً متبدّلاً باسم إزاحة المسار (routeOffset) قيمته الموضع الحالي (currentPos) مضافاً إليه ثابت حجم معرّف المُرسِل (SENDER_ID_SIZE). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:387]

```
388:                 if (hasRecipient) {
```
> يبدأ شرطاً يتحقق إن كان وجود مُستقبِل (hasRecipient) صحيحاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:388]

```
389:                     routeOffset += RECIPIENT_ID_SIZE
```
> يزيد إزاحة المسار (routeOffset) بمقدار ثابت حجم معرّف المُستقبِل (RECIPIENT_ID_SIZE). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:389]

```
390:                 }
```
> إغلاق نطاق شرط وجود المُستقبِل. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:390]

```
391: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:391]

```
392:                 if (raw.size >= routeOffset + 1) {
```
> يبدأ شرطاً يتحقق إن كان حجم البيانات الخام (raw.size) أكبر من أو يساوي إزاحة المسار (routeOffset) زائد واحد. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:392]

```
393:                     routeCount = raw[routeOffset].toUByte().toInt()
```
> يضبط عدّ المسار (routeCount) إلى البايت الواقع في البيانات الخام عند إزاحة المسار (raw[routeOffset]) محوَّلاً إلى بايت غير مُوقَّع ثم إلى عدد صحيح. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:393]

```
394:                 }
```
> إغلاق نطاق شرط كفاية حجم البيانات الخام. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:394]

```
395:                 expectedSize += 1 + (routeCount * SENDER_ID_SIZE)
```
> يزيد الحجم المتوقَّع (expectedSize) بمقدار واحد زائد حاصل ضرب عدّ المسار (routeCount) في ثابت حجم معرّف المُرسِل (SENDER_ID_SIZE). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:395]

```
396:             }
```
> إغلاق نطاق شرط وجود المسار. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:396]

```
397:             if (hasSignature) expectedSize += SIGNATURE_SIZE
```
> يبدأ شرطاً يزيد الحجم المتوقَّع (expectedSize) بمقدار ثابت حجم التوقيع (SIGNATURE_SIZE) إن كان وجود توقيع (hasSignature) صحيحاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:397]

```
398: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:398]

```
399:             if (raw.size < expectedSize) return null
```
> يبدأ شرطاً يعيد القيمة المعدومة إن كان حجم البيانات الخام (raw.size) أصغر من الحجم المتوقَّع (expectedSize). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:399]

```
400:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:400]

```
401:             // SenderID
```
> تعليق: معرّف المُرسِل (SenderID). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:401]

```
402:             val senderID = ByteArray(SENDER_ID_SIZE)
```
> يعرّف متغيّراً ثابتاً باسم معرّف المُرسِل (senderID) قيمته مصفوفة بايتات (ByteArray) طولها ثابت حجم معرّف المُرسِل (SENDER_ID_SIZE). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:402]

```
403:             buffer.get(senderID)
```
> يقرأ من المخزن المؤقت ملء مصفوفة معرّف المُرسِل (senderID). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:403]

```
404:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:404]

```
405:             // RecipientID
```
> تعليق: معرّف المُستقبِل (RecipientID). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:405]

```
406:             val recipientID = if (hasRecipient) {
```
> يعرّف متغيّراً ثابتاً باسم معرّف المُستقبِل (recipientID) بادئاً تعبيراً شرطياً يتحقق إن كان وجود مُستقبِل (hasRecipient) صحيحاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:406]

```
407:                 val recipientBytes = ByteArray(RECIPIENT_ID_SIZE)
```
> يعرّف متغيّراً ثابتاً باسم بايتات المُستقبِل (recipientBytes) قيمته مصفوفة بايتات طولها ثابت حجم معرّف المُستقبِل (RECIPIENT_ID_SIZE). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:407]

```
408:                 buffer.get(recipientBytes)
```
> يقرأ من المخزن المؤقت ملء مصفوفة بايتات المُستقبِل (recipientBytes). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:408]

```
409:                 recipientBytes
```
> يعطي قيمة التعبير الشرطي وهي بايتات المُستقبِل (recipientBytes). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:409]

```
410:             } else null
```
> إغلاق نطاق فرع الشرط، وفرع البديل يعطي القيمة المعدومة (null). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:410]

```
411:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:411]

```
412:             // Route (optional)
```
> تعليق: المسار (Route) (اختياري). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:412]

```
413:             val route: List<ByteArray>? = if (hasRoute) {
```
> يعرّف متغيّراً ثابتاً باسم المسار (route) من نوع قائمة مصفوفات بايتات (List<ByteArray>) قد تكون معدومة، بادئاً تعبيراً شرطياً يتحقق إن كان وجود مسار (hasRoute) صحيحاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:413]

```
414:                 val count = buffer.get().toUByte().toInt()
```
> يعرّف متغيّراً ثابتاً باسم العدّ (count) قيمته بايت يُقرأ من المخزن المؤقت محوَّلاً إلى بايت غير مُوقَّع ثم إلى عدد صحيح. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:414]

```
415:                 if (count == 0) {
```
> يبدأ شرطاً يتحقق إن كان العدّ (count) يساوي صفراً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:415]

```
416:                     null // Treat empty route list as null to enforce canonical representation
```
> يعطي القيمة المعدومة (null)؛ تعليق: عامِل قائمة المسار الفارغة كقيمة معدومة لفرض التمثيل المعياري. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:416]

```
417:                 } else {
```
> إغلاق نطاق فرع الشرط، وبدء فرع البديل (else). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:417]

```
418:                     val hops = mutableListOf<ByteArray>()
```
> يعرّف متغيّراً ثابتاً باسم القفزات (hops) قيمته قائمة متبدّلة فارغة من مصفوفات بايتات (mutableListOf<ByteArray>). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:418]

```
419:                     repeat(count) {
```
> يكرّر الكتلة التالية عدداً من المرّات يساوي العدّ (count) بالدالة repeat. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:419]

```
420:                         val hop = ByteArray(SENDER_ID_SIZE)
```
> يعرّف متغيّراً ثابتاً باسم القفزة (hop) قيمته مصفوفة بايتات طولها ثابت حجم معرّف المُرسِل (SENDER_ID_SIZE). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:420]

```
421:                         buffer.get(hop)
```
> يقرأ من المخزن المؤقت ملء مصفوفة القفزة (hop). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:421]

```
422:                         hops.add(hop)
```
> يضيف القفزة (hop) إلى قائمة القفزات (hops) بالدالة add. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:422]

```
423:                     }
```
> إغلاق نطاق كتلة التكرار (repeat). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:423]

```
424:                     hops
```
> يعطي قيمة فرع البديل وهي قائمة القفزات (hops). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:424]

```
425:                 }
```
> إغلاق نطاق فرع البديل (else) الخاص بالعدّ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:425]

```
426:             } else null
```
> إغلاق نطاق فرع الشرط الخاص بوجود المسار، وفرع البديل يعطي القيمة المعدومة (null). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:426]

```
427: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:427]

```
428:             // Payload
```
> تعليق: الحمولة (Payload). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:428]

```
429:             val payload = if (isCompressed) {
```
> يعرّف متغيّراً ثابتاً باسم الحمولة (payload) بادئاً تعبيراً شرطياً يتحقق إن كان الانضغاط (isCompressed) صحيحاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:429]

```
430:                 val lengthFieldBytes = if (version >= 2u.toUByte()) 4 else 2
```
> يعرّف متغيّراً ثابتاً باسم بايتات حقل الطول (lengthFieldBytes) قيمته ٤ إن كان الإصدار (version) أكبر من أو يساوي ٢، وإلا فقيمته ٢. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:430]

```
431:                 if (payloadLength.toInt() < lengthFieldBytes) return null
```
> يبدأ شرطاً يعيد القيمة المعدومة إن كان طول الحمولة (payloadLength) محوَّلاً إلى عدد صحيح أصغر من بايتات حقل الطول (lengthFieldBytes). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:431]

```
432:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:432]

```
433:                 val originalSize = if (version >= 2u.toUByte()) {
```
> يعرّف متغيّراً ثابتاً باسم الحجم الأصلي (originalSize) بادئاً تعبيراً شرطياً يتحقق إن كان الإصدار (version) أكبر من أو يساوي ٢. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:433]

```
434:                     buffer.getInt()
```
> يقرأ من المخزن المؤقت عدداً صحيحاً بالدالة getInt. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:434]

```
435:                 } else {
```
> إغلاق نطاق فرع الشرط، وبدء فرع البديل (else). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:435]

```
436:                     buffer.getShort().toUShort().toInt()
```
> يقرأ من المخزن المؤقت عدداً قصيراً بالدالة getShort محوَّلاً إلى عدد قصير غير مُوقَّع ثم إلى عدد صحيح. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:436]

```
437:                 }
```
> إغلاق نطاق التعبير الشرطي للحجم الأصلي. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:437]

```
438:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:438]

```
439:                 // Compressed payload
```
> تعليق: الحمولة المضغوطة (Compressed payload). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:439]

```
440:                 val compressedSize = payloadLength.toInt() - lengthFieldBytes
```
> يعرّف متغيّراً ثابتاً باسم الحجم المضغوط (compressedSize) قيمته طول الحمولة (payloadLength) محوَّلاً إلى عدد صحيح ناقص بايتات حقل الطول (lengthFieldBytes). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:440]

```
441:                 val compressedPayload = ByteArray(compressedSize)
```
> يعرّف متغيّراً ثابتاً باسم الحمولة المضغوطة (compressedPayload) قيمته مصفوفة بايتات طولها الحجم المضغوط (compressedSize). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:441]

```
442:                 buffer.get(compressedPayload)
```
> يقرأ من المخزن المؤقت ملء مصفوفة الحمولة المضغوطة (compressedPayload). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:442]

```
443: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:443]

```
444:                 // Security check: Compression bomb protection
```
> تعليق: فحص أمني: حماية من قنبلة الضغط (Compression bomb). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:444]

```
445:                 if (compressedSize > 0) {
```
> يبدأ شرطاً يتحقق إن كان الحجم المضغوط (compressedSize) أكبر من صفر. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:445]

```
446:                     val ratio = originalSize.toDouble() / compressedSize.toDouble()
```
> يعرّف متغيّراً ثابتاً باسم النسبة (ratio) قيمته الحجم الأصلي (originalSize) محوَّلاً إلى عدد عشري مقسوماً على الحجم المضغوط (compressedSize) محوَّلاً إلى عدد عشري. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:446]

```
447:                     if (ratio > 50_000.0) {
```
> يبدأ شرطاً يتحقق إن كانت النسبة (ratio) أكبر من القيمة 50000.0. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:447]

```
448:                         Log.w("BinaryProtocol", "🚫 Suspicious compression ratio: ${ratio}:1")
```
> يسجّل تحذيراً (Log.w) بالوسم "BinaryProtocol" نصّه: 🚫 نسبة ضغط مشبوهة: قيمة النسبة (ratio) إلى ١. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:448]

```
449:                         return null
```
> يعيد القيمة المعدومة (null). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:449]

```
450:                     }
```
> إغلاق نطاق شرط النسبة المشبوهة. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:450]

```
451:                 }
```
> إغلاق نطاق شرط الحجم المضغوط الموجب. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:451]

```
452:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:452]

```
453:                 // Decompress
```
> تعليق: فكّ الضغط (Decompress). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:453]

```
454:                 CompressionUtil.decompress(compressedPayload, originalSize) ?: return null
```
> يستدعي دالة فكّ الضغط (CompressionUtil.decompress) على الحمولة المضغوطة (compressedPayload) والحجم الأصلي (originalSize)، وإن كان الناتج معدوماً يعيد القيمة المعدومة، وإلا يعطيه قيمة لفرع الشرط. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:454]

```
455:             } else {
```
> إغلاق نطاق فرع الشرط الخاص بالانضغاط، وبدء فرع البديل (else). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:455]

```
456:                 val payloadBytes = ByteArray(payloadLength.toInt())
```
> يعرّف متغيّراً ثابتاً باسم بايتات الحمولة (payloadBytes) قيمته مصفوفة بايتات طولها طول الحمولة (payloadLength) محوَّلاً إلى عدد صحيح. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:456]

```
457:                 buffer.get(payloadBytes)
```
> يقرأ من المخزن المؤقت ملء مصفوفة بايتات الحمولة (payloadBytes). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:457]

```
458:                 payloadBytes
```
> يعطي قيمة فرع البديل وهي بايتات الحمولة (payloadBytes). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:458]

```
459:             }
```
> إغلاق نطاق التعبير الشرطي للحمولة. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:459]

```
460:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:460]

```
461:             // Signature
```
> تعليق: التوقيع (Signature). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:461]

```
462:             val signature = if (hasSignature) {
```
> يعرّف متغيّراً ثابتاً باسم التوقيع (signature) بادئاً تعبيراً شرطياً يتحقق إن كان وجود توقيع (hasSignature) صحيحاً. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:462]

```
463:                 val signatureBytes = ByteArray(SIGNATURE_SIZE)
```
> يعرّف متغيّراً ثابتاً باسم بايتات التوقيع (signatureBytes) قيمته مصفوفة بايتات طولها ثابت حجم التوقيع (SIGNATURE_SIZE). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:463]

```
464:                 buffer.get(signatureBytes)
```
> يقرأ من المخزن المؤقت ملء مصفوفة بايتات التوقيع (signatureBytes). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:464]

```
465:                 signatureBytes
```
> يعطي قيمة التعبير الشرطي وهي بايتات التوقيع (signatureBytes). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:465]

```
466:             } else null
```
> إغلاق نطاق فرع الشرط، وفرع البديل يعطي القيمة المعدومة (null). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:466]

```
467:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:467]

```
468:             return BitchatPacket(
```
> يعيد حزمة بِت-تشات (BitchatPacket) جديدة بادئاً قائمة وسائطها. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:468]

```
469:                 version = version,
```
> يمرّر الوسيط الإصدار (version) بقيمة الإصدار (version). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:469]

```
470:                 type = type,
```
> يمرّر الوسيط النوع (type) بقيمة النوع (type). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:470]

```
471:                 senderID = senderID,
```
> يمرّر الوسيط معرّف المُرسِل (senderID) بقيمة معرّف المُرسِل (senderID). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:471]

```
472:                 recipientID = recipientID,
```
> يمرّر الوسيط معرّف المُستقبِل (recipientID) بقيمة معرّف المُستقبِل (recipientID). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:472]

```
473:                 timestamp = timestamp,
```
> يمرّر الوسيط الطابع الزمني (timestamp) بقيمة الطابع الزمني (timestamp). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:473]

```
474:                 payload = payload,
```
> يمرّر الوسيط الحمولة (payload) بقيمة الحمولة (payload). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:474]

```
475:                 signature = signature,
```
> يمرّر الوسيط التوقيع (signature) بقيمة التوقيع (signature). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:475]

```
476:                 ttl = ttl,
```
> يمرّر الوسيط مدّة البقاء (ttl) بقيمة مدّة البقاء (ttl). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:476]

```
477:                 route = route
```
> يمرّر الوسيط المسار (route) بقيمة المسار (route). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:477]

```
478:             )
```
> إغلاق قائمة وسائط مُنشئ حزمة بِت-تشات. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:478]

```
479:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:479]

```
480:         } catch (e: Throwable) {
```
> يلتقط رميةً من النوع Throwable ويسمّيها e. [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:480]

```
481:             Log.e("BinaryProtocol", "Error decoding packet: ${e.message}")
```
> يسجّل خطأً (Log.e) بالوسم "BinaryProtocol" نصّه: خطأ في فكّ ترميز الحزمة متبوعاً برسالة الرمية (e.message). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:481]

```
482:             return null
```
> يعيد القيمة المعدومة (null). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:482]

```
483:         }
```
> إغلاق نطاق كتلة التقاط الرمية (catch). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:483]

```
484:     }
```
> إغلاق نطاق دالة فكّ الترميز الجوهري (decodeCore). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:484]

```
485: }
```
> إغلاق نطاق صنف/كائن البروتوكول الثنائي (BinaryProtocol). [app/src/main/java/com/bitchat/android/protocol/BinaryProtocol.kt:485]
