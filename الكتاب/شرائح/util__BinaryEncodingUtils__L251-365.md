# شريحة — app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt (الأسطر 251–365)

```
251:     companion object {
```
> تعريف كائن مرافق (companion object) داخل الصنف، وهو صندوق ثابت يتبع الصنف نفسه. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:251]

```
252:         fun fromValue(value: UByte): BinaryMessageType? {
```
> تعريف دالة (fromValue) تأخذ وسيطاً اسمه (value) من نوع بايت غير موقّع (UByte) وتعيد نوع رسالة ثنائية (BinaryMessageType) أو قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:252]

```
253:             return values().find { it.value == value }
```
> إعادة أول عنصر من قائمة قيم التعداد (values) الذي تساوي خاصيته (value) القيمة الممرّرة (value). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:253]

```
254:         }
```
> إغلاق نطاق الدالة (fromValue). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:254]

```
255:     }
```
> إغلاق نطاق الكائن المرافق (companion object). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:255]

```
256: }
```
> إغلاق نطاق الصنف/التعداد المحيط. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:256]

```
257: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:257]

```
258: // Extension functions for ByteArray to support iOS-style data manipulation
```
> تعليق: دوال توسعة لمصفوفة البايتات (ByteArray) لدعم معالجة البيانات على نمط iOS. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:258]

```
259: fun ByteArray.readUInt8(at: IntArray): UByte? {
```
> تعريف دالة توسعة (readUInt8) على مصفوفة البايتات تأخذ وسيطاً اسمه (at) من نوع مصفوفة أعداد صحيحة (IntArray) وتعيد بايتاً غير موقّع (UByte) أو قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:259]

```
260:     val offset = at[0]
```
> تعريف متغيّر للقراءة فقط اسمه (offset) يساوي العنصر الأول من المصفوفة (at). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:260]

```
261:     if (offset >= this.size) return null
```
> إن كان (offset) أكبر من أو يساوي حجم المصفوفة الحالية (this.size) تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:261]

```
262:     val value = this[offset].toUByte()
```
> تعريف متغيّر اسمه (value) يساوي البايت عند الموضع (offset) محوّلاً إلى بايت غير موقّع (toUByte). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:262]

```
263:     at[0] += 1
```
> زيادة العنصر الأول من المصفوفة (at) بمقدار واحد. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:263]

```
264:     return value
```
> إعادة المتغيّر (value). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:264]

```
265: }
```
> إغلاق نطاق الدالة (readUInt8). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:265]

```
266: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:266]

```
267: fun ByteArray.readUInt16(at: IntArray): UShort? {
```
> تعريف دالة توسعة (readUInt16) على مصفوفة البايتات تأخذ وسيطاً اسمه (at) من نوع مصفوفة أعداد صحيحة (IntArray) وتعيد عدداً قصيراً غير موقّع (UShort) أو قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:267]

```
268:     val offset = at[0]
```
> تعريف متغيّر للقراءة فقط اسمه (offset) يساوي العنصر الأول من المصفوفة (at). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:268]

```
269:     if (offset + 2 > this.size) return null
```
> إن كان (offset) مضافاً إليه اثنان أكبر من حجم المصفوفة الحالية تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:269]

```
270:     val value = ((this[offset].toUByte().toInt() shl 8) or 
```
> تعريف متغيّر اسمه (value) يبدأ بأخذ البايت عند (offset) محوّلاً إلى بايت غير موقّع ثم إلى عدد صحيح ثم مُزاحاً يساراً ثماني بتات (shl 8) ثم دمجه بعملية أو (or). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:270]

```
271:                 (this[offset + 1].toUByte().toInt())).toUShort()
```
> تتمّة: دمج البايت عند (offset + 1) محوّلاً إلى بايت غير موقّع ثم إلى عدد صحيح، والنتيجة كلها محوّلة إلى عدد قصير غير موقّع (toUShort). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:271]

```
272:     at[0] += 2
```
> زيادة العنصر الأول من المصفوفة (at) بمقدار اثنين. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:272]

```
273:     return value
```
> إعادة المتغيّر (value). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:273]

```
274: }
```
> إغلاق نطاق الدالة (readUInt16). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:274]

```
275: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:275]

```
276: fun ByteArray.readUInt32(at: IntArray): UInt? {
```
> تعريف دالة توسعة (readUInt32) على مصفوفة البايتات تأخذ وسيطاً اسمه (at) من نوع مصفوفة أعداد صحيحة وتعيد عدداً صحيحاً غير موقّع (UInt) أو قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:276]

```
277:     val offset = at[0]
```
> تعريف متغيّر للقراءة فقط اسمه (offset) يساوي العنصر الأول من المصفوفة (at). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:277]

```
278:     if (offset + 4 > this.size) return null
```
> إن كان (offset) مضافاً إليه أربعة أكبر من حجم المصفوفة الحالية تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:278]

```
279:     val value = ((this[offset].toUByte().toUInt() shl 24) or
```
> تعريف متغيّر اسمه (value) يبدأ بأخذ البايت عند (offset) محوّلاً إلى بايت غير موقّع ثم إلى عدد صحيح غير موقّع ثم مُزاحاً يساراً أربعاً وعشرين بتة (shl 24) مع دمج بعملية أو. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:279]

```
280:                 (this[offset + 1].toUByte().toUInt() shl 16) or
```
> تتمّة: دمج البايت عند (offset + 1) محوّلاً إلى عدد صحيح غير موقّع ومُزاحاً يساراً ست عشرة بتة (shl 16) بعملية أو. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:280]

```
281:                 (this[offset + 2].toUByte().toUInt() shl 8) or
```
> تتمّة: دمج البايت عند (offset + 2) محوّلاً إلى عدد صحيح غير موقّع ومُزاحاً يساراً ثماني بتات (shl 8) بعملية أو. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:281]

```
282:                 (this[offset + 3].toUByte().toUInt()))
```
> تتمّة: دمج البايت عند (offset + 3) محوّلاً إلى بايت غير موقّع ثم إلى عدد صحيح غير موقّع، وإغلاق تعبير القيمة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:282]

```
283:     at[0] += 4
```
> زيادة العنصر الأول من المصفوفة (at) بمقدار أربعة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:283]

```
284:     return value
```
> إعادة المتغيّر (value). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:284]

```
285: }
```
> إغلاق نطاق الدالة (readUInt32). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:285]

```
286: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:286]

```
287: fun ByteArray.readUInt64(at: IntArray): ULong? {
```
> تعريف دالة توسعة (readUInt64) على مصفوفة البايتات تأخذ وسيطاً اسمه (at) من نوع مصفوفة أعداد صحيحة وتعيد عدداً طويلاً غير موقّع (ULong) أو قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:287]

```
288:     val offset = at[0]
```
> تعريف متغيّر للقراءة فقط اسمه (offset) يساوي العنصر الأول من المصفوفة (at). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:288]

```
289:     if (offset + 8 > this.size) return null
```
> إن كان (offset) مضافاً إليه ثمانية أكبر من حجم المصفوفة الحالية تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:289]

```
290:     var value = 0UL
```
> تعريف متغيّر قابل للتغيير اسمه (value) قيمته الابتدائية صفر من نوع عدد طويل غير موقّع (0UL). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:290]

```
291:     for (i in 0 until 8) {
```
> حلقة تكرار بمتغيّر (i) من صفر حتى ما قبل ثمانية. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:291]

```
292:         value = (value shl 8) or this[offset + i].toUByte().toULong()
```
> إسناد جديد للمتغيّر (value) يساوي قيمته مُزاحة يساراً ثماني بتات (shl 8) مدموجة بعملية أو مع البايت عند (offset + i) محوّلاً إلى بايت غير موقّع ثم إلى عدد طويل غير موقّع. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:292]

```
293:     }
```
> إغلاق نطاق حلقة التكرار (for). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:293]

```
294:     at[0] += 8
```
> زيادة العنصر الأول من المصفوفة (at) بمقدار ثمانية. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:294]

```
295:     return value
```
> إعادة المتغيّر (value). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:295]

```
296: }
```
> إغلاق نطاق الدالة (readUInt64). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:296]

```
297: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:297]

```
298: fun ByteArray.readString(at: IntArray, maxLength: Int = 255): String? {
```
> تعريف دالة توسعة (readString) على مصفوفة البايتات تأخذ وسيطاً (at) ووسيطاً (maxLength) من نوع عدد صحيح بقيمة افتراضية 255، وتعيد سلسلة نصية (String) أو قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:298]

```
299:     val length: Int = if (maxLength <= 255) {
```
> تعريف متغيّر اسمه (length) من نوع عدد صحيح يُسنَد إليه نتيجة شرط: إن كان (maxLength) أصغر من أو يساوي 255. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:299]

```
300:         readUInt8(at)?.toInt() ?: return null
```
> استدعاء (readUInt8) على المصفوفة وتحويل ناتجه إلى عدد صحيح، وإن كان فارغاً تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:300]

```
301:     } else {
```
> بداية فرع الحالة الأخرى (else) للشرط. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:301]

```
302:         readUInt16(at)?.toInt() ?: return null
```
> استدعاء (readUInt16) على المصفوفة وتحويل ناتجه إلى عدد صحيح، وإن كان فارغاً تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:302]

```
303:     }
```
> إغلاق نطاق تعبير الشرط (if/else) المُسنَد إلى (length). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:303]

```
304:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:304]

```
305:     val offset = at[0]
```
> تعريف متغيّر للقراءة فقط اسمه (offset) يساوي العنصر الأول من المصفوفة (at). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:305]

```
306:     if (offset + length > this.size) return null
```
> إن كان (offset) مضافاً إليه (length) أكبر من حجم المصفوفة الحالية تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:306]

```
307:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:307]

```
308:     val stringData = this.sliceArray(offset until offset + length)
```
> تعريف متغيّر اسمه (stringData) يساوي شريحة من المصفوفة (sliceArray) من (offset) حتى ما قبل (offset + length). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:308]

```
309:     at[0] += length
```
> زيادة العنصر الأول من المصفوفة (at) بمقدار (length). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:309]

```
310:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:310]

```
311:     return String(stringData, Charsets.UTF_8)
```
> إعادة سلسلة نصية مبنية من (stringData) بترميز يو تي إف-8 (Charsets.UTF_8). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:311]

```
312: }
```
> إغلاق نطاق الدالة (readString). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:312]

```
313: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:313]

```
314: fun ByteArray.readData(at: IntArray, maxLength: Int = 65535): ByteArray? {
```
> تعريف دالة توسعة (readData) على مصفوفة البايتات تأخذ وسيطاً (at) ووسيطاً (maxLength) من نوع عدد صحيح بقيمة افتراضية 65535، وتعيد مصفوفة بايتات (ByteArray) أو قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:314]

```
315:     val length: Int = if (maxLength <= 255) {
```
> تعريف متغيّر اسمه (length) من نوع عدد صحيح يُسنَد إليه نتيجة شرط: إن كان (maxLength) أصغر من أو يساوي 255. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:315]

```
316:         readUInt8(at)?.toInt() ?: return null
```
> استدعاء (readUInt8) على المصفوفة وتحويل ناتجه إلى عدد صحيح، وإن كان فارغاً تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:316]

```
317:     } else {
```
> بداية فرع الحالة الأخرى (else) للشرط. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:317]

```
318:         readUInt16(at)?.toInt() ?: return null
```
> استدعاء (readUInt16) على المصفوفة وتحويل ناتجه إلى عدد صحيح، وإن كان فارغاً تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:318]

```
319:     }
```
> إغلاق نطاق تعبير الشرط (if/else) المُسنَد إلى (length). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:319]

```
320:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:320]

```
321:     val offset = at[0]
```
> تعريف متغيّر للقراءة فقط اسمه (offset) يساوي العنصر الأول من المصفوفة (at). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:321]

```
322:     if (offset + length > this.size) return null
```
> إن كان (offset) مضافاً إليه (length) أكبر من حجم المصفوفة الحالية تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:322]

```
323:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:323]

```
324:     val data = this.sliceArray(offset until offset + length)
```
> تعريف متغيّر اسمه (data) يساوي شريحة من المصفوفة (sliceArray) من (offset) حتى ما قبل (offset + length). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:324]

```
325:     at[0] += length
```
> زيادة العنصر الأول من المصفوفة (at) بمقدار (length). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:325]

```
326:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:326]

```
327:     return data
```
> إعادة المتغيّر (data). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:327]

```
328: }
```
> إغلاق نطاق الدالة (readData). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:328]

```
329: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:329]

```
330: fun ByteArray.readDate(at: IntArray): Date? {
```
> تعريف دالة توسعة (readDate) على مصفوفة البايتات تأخذ وسيطاً (at) من نوع مصفوفة أعداد صحيحة وتعيد تاريخاً (Date) أو قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:330]

```
331:     val timestamp = readUInt64(at) ?: return null
```
> تعريف متغيّر اسمه (timestamp) يساوي ناتج استدعاء (readUInt64) على المصفوفة، وإن كان فارغاً تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:331]

```
332:     return Date(timestamp.toLong())
```
> إعادة كائن تاريخ (Date) مبني من (timestamp) محوّلاً إلى عدد طويل (toLong). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:332]

```
333: }
```
> إغلاق نطاق الدالة (readDate). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:333]

```
334: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:334]

```
335: fun ByteArray.readUUID(at: IntArray): String? {
```
> تعريف دالة توسعة (readUUID) على مصفوفة البايتات تأخذ وسيطاً (at) من نوع مصفوفة أعداد صحيحة وتعيد سلسلة نصية (String) أو قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:335]

```
336:     val offset = at[0]
```
> تعريف متغيّر للقراءة فقط اسمه (offset) يساوي العنصر الأول من المصفوفة (at). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:336]

```
337:     if (offset + 16 > this.size) return null
```
> إن كان (offset) مضافاً إليه ستة عشر أكبر من حجم المصفوفة الحالية تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:337]

```
338:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:338]

```
339:     val uuidData = this.sliceArray(offset until offset + 16)
```
> تعريف متغيّر اسمه (uuidData) يساوي شريحة من المصفوفة (sliceArray) من (offset) حتى ما قبل (offset + 16). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:339]

```
340:     at[0] += 16
```
> زيادة العنصر الأول من المصفوفة (at) بمقدار ستة عشر. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:340]

```
341:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:341]

```
342:     // Convert 16 bytes to UUID string format
```
> تعليق: تحويل ستة عشر بايتاً إلى صيغة سلسلة معرّف فريد عالمي (UUID). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:342]

```
343:     val uuid = uuidData.joinToString("") { "%02x".format(it) }
```
> تعريف متغيّر اسمه (uuid) يساوي دمج عناصر (uuidData) في سلسلة بلا فاصل، حيث يُنسَّق كل بايت كرقمين ست عشريين (%02x). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:343]

```
344:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:344]

```
345:     // Insert hyphens at proper positions: 8-4-4-4-12
```
> تعليق: إدراج شرطات في المواضع المناسبة بالنمط 8-4-4-4-12. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:345]

```
346:     val result = StringBuilder()
```
> تعريف متغيّر اسمه (result) يساوي كائن بنّاء سلاسل جديد (StringBuilder). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:346]

```
347:     for ((index, char) in uuid.withIndex()) {
```
> حلقة تكرار على (uuid) مع فهرسها (withIndex)، يفكّك كل عنصر إلى (index) و(char). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:347]

```
348:         if (index == 8 || index == 12 || index == 16 || index == 20) {
```
> شرط: إن كان (index) يساوي 8 أو 12 أو 16 أو 20. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:348]

```
349:             result.append("-")
```
> إلحاق شرطة ("-") بالبنّاء (result). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:349]

```
350:         }
```
> إغلاق نطاق الشرط (if). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:350]

```
351:         result.append(char)
```
> إلحاق الحرف (char) بالبنّاء (result). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:351]

```
352:     }
```
> إغلاق نطاق حلقة التكرار (for). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:352]

```
353:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:353]

```
354:     return result.toString().uppercase()
```
> إعادة محتوى البنّاء (result) محوّلاً إلى سلسلة ثم إلى أحرف كبيرة (uppercase). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:354]

```
355: }
```
> إغلاق نطاق الدالة (readUUID). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:355]

```
356: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:356]

```
357: fun ByteArray.readFixedBytes(at: IntArray, count: Int): ByteArray? {
```
> تعريف دالة توسعة (readFixedBytes) على مصفوفة البايتات تأخذ وسيطاً (at) ووسيطاً (count) من نوع عدد صحيح وتعيد مصفوفة بايتات (ByteArray) أو قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:357]

```
358:     val offset = at[0]
```
> تعريف متغيّر للقراءة فقط اسمه (offset) يساوي العنصر الأول من المصفوفة (at). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:358]

```
359:     if (offset + count > this.size) return null
```
> إن كان (offset) مضافاً إليه (count) أكبر من حجم المصفوفة الحالية تُعاد قيمة فارغة. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:359]

```
360:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:360]

```
361:     val data = this.sliceArray(offset until offset + count)
```
> تعريف متغيّر اسمه (data) يساوي شريحة من المصفوفة (sliceArray) من (offset) حتى ما قبل (offset + count). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:361]

```
362:     at[0] += count
```
> زيادة العنصر الأول من المصفوفة (at) بمقدار (count). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:362]

```
363:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:363]

```
364:     return data
```
> إعادة المتغيّر (data). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:364]

```
365: }
```
> إغلاق نطاق الدالة (readFixedBytes). [app/src/main/java/com/bitchat/android/util/BinaryEncodingUtils.kt:365]
