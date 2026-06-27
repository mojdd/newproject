# شريحة — app/src/main/java/com/bitchat/android/model/BitchatMessage.kt (الأسطر 251–358)

```
251:                 val senderPeerID = if (hasSenderPeerID && buffer.hasRemaining()) {
```
> يُعرَّف متغيّر ثابت اسمه «معرّف ندّ المرسل» (senderPeerID) ويُسنَد إليه ناتج تعبير شرطي يبدأ شرطه بأن تكون الراية «يوجد معرّف ندّ مرسل» (hasSenderPeerID) صحيحة وأن يكون في المخزن المؤقّت (buffer) بايتات متبقّية عبر استدعاء الدالة «لديه متبقٍّ» (hasRemaining). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:251]

```
252:                     val length = buffer.get().toInt() and 0xFF
```
> يُعرَّف متغيّر ثابت اسمه «الطول» (length) ويُسنَد إليه قيمة بايت واحد مقروء من المخزن المؤقّت محوَّل إلى عدد صحيح ثم مُقنَّع بثنائيّة «و» مع القيمة الحرفية 0xFF لجعله بلا إشارة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:252]

```
253:                     if (buffer.remaining() >= length) {
```
> جملة شرطية تتحقّق من أن عدد البايتات المتبقّية في المخزن المؤقّت عبر الدالة «المتبقّي» (remaining) أكبر من أو يساوي «الطول». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:253]

```
254:                         val bytes = ByteArray(length)
```
> يُعرَّف متغيّر ثابت اسمه «بايتات» (bytes) ويُسنَد إليه مصفوفة بايتات (ByteArray) بحجم يساوي «الطول». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:254]

```
255:                         buffer.get(bytes)
```
> يُستدعى من المخزن المؤقّت الدالة «احصل» (get) لتعبئة مصفوفة «بايتات» بالبيانات المقروءة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:255]

```
256:                         String(bytes, Charsets.UTF_8)
```
> يُنشأ نص (String) من مصفوفة «بايتات» باستعمال ترميز «يو تي إف ٨» (UTF_8) كقيمة ناتجة للكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:256]

```
257:                     } else null
```
> إغلاق نطاق الجملة الشرطية مع فرع «وإلّا» (else) يعيد القيمة الفارغة (null) إذا لم يكفِ المتبقّي. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:257]

```
258:                 } else null
```
> إغلاق نطاق التعبير الشرطي الخارجي مع فرع «وإلّا» يعيد القيمة الفارغة (null) إذا لم تتحقّق الراية أو لا متبقّي. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:258]

```
259: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:259]

```
260:                 // Mentions array
```
> تعليق: «مصفوفة الإشارات/الذِّكر». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:260]

```
261:                 val mentions = if (hasMentions && buffer.hasRemaining()) {
```
> يُعرَّف متغيّر ثابت اسمه «الإشارات» (mentions) ويُسنَد إليه ناتج تعبير شرطي شرطه أن تكون الراية «يوجد إشارات» (hasMentions) صحيحة وأن يكون للمخزن المؤقّت بايتات متبقّية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:261]

```
262:                     val mentionCount = buffer.get().toInt() and 0xFF
```
> يُعرَّف متغيّر ثابت اسمه «عدد الإشارات» (mentionCount) ويُسنَد إليه بايت واحد مقروء من المخزن المؤقّت محوَّل إلى عدد صحيح ومُقنَّع مع 0xFF. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:262]

```
263:                     val mentionList = mutableListOf<String>()
```
> يُعرَّف متغيّر ثابت اسمه «قائمة الإشارات» (mentionList) ويُسنَد إليه قائمة قابلة للتعديل (mutableListOf) من نصوص فارغة ابتداءً. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:263]

```
264:                     repeat(mentionCount) {
```
> يُستدعى البناء «كرّر» (repeat) لتنفيذ الكتلة عدداً من المرّات يساوي «عدد الإشارات». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:264]

```
265:                         if (buffer.hasRemaining()) {
```
> جملة شرطية تتحقّق من أن المخزن المؤقّت لديه بايتات متبقّية عبر الدالة «لديه متبقٍّ». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:265]

```
266:                             val length = buffer.get().toInt() and 0xFF
```
> يُعرَّف متغيّر ثابت اسمه «الطول» (length) ويُسنَد إليه بايت واحد مقروء من المخزن المؤقّت محوَّل إلى عدد صحيح ومُقنَّع مع 0xFF. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:266]

```
267:                             if (buffer.remaining() >= length) {
```
> جملة شرطية تتحقّق من أن المتبقّي في المخزن المؤقّت أكبر من أو يساوي «الطول». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:267]

```
268:                                 val bytes = ByteArray(length)
```
> يُعرَّف متغيّر ثابت اسمه «بايتات» (bytes) ويُسنَد إليه مصفوفة بايتات بحجم يساوي «الطول». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:268]

```
269:                                 buffer.get(bytes)
```
> يُستدعى من المخزن المؤقّت الدالة «احصل» لتعبئة مصفوفة «بايتات». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:269]

```
270:                                 mentionList.add(String(bytes, Charsets.UTF_8))
```
> يُستدعى على «قائمة الإشارات» الدالة «أضف» (add) لإضافة نص مُنشأ من مصفوفة «بايتات» بترميز «يو تي إف ٨». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:270]

```
271:                             }
```
> إغلاق نطاق الجملة الشرطية الخاصة بالتحقّق من المتبقّي. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:271]

```
272:                         }
```
> إغلاق نطاق الجملة الشرطية الخاصة بـ«لديه متبقٍّ». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:272]

```
273:                     }
```
> إغلاق نطاق كتلة البناء «كرّر». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:273]

```
274:                     if (mentionList.isNotEmpty()) mentionList else null
```
> تعبير شرطي يعيد «قائمة الإشارات» إذا كانت غير فارغة عبر الدالة «ليست فارغة» (isNotEmpty)، وإلّا يعيد القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:274]

```
275:                 } else null
```
> إغلاق نطاق التعبير الشرطي مع فرع «وإلّا» يعيد القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:275]

```
276: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:276]

```
277:                 // Channel
```
> تعليق: «القناة». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:277]

```
278:                 val channel = if (hasChannel && buffer.hasRemaining()) {
```
> يُعرَّف متغيّر ثابت اسمه «القناة» (channel) ويُسنَد إليه ناتج تعبير شرطي شرطه أن تكون الراية «يوجد قناة» (hasChannel) صحيحة وأن يكون للمخزن المؤقّت بايتات متبقّية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:278]

```
279:                     val length = buffer.get().toInt() and 0xFF
```
> يُعرَّف متغيّر ثابت اسمه «الطول» (length) ويُسنَد إليه بايت واحد مقروء من المخزن المؤقّت محوَّل إلى عدد صحيح ومُقنَّع مع 0xFF. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:279]

```
280:                     if (buffer.remaining() >= length) {
```
> جملة شرطية تتحقّق من أن المتبقّي في المخزن المؤقّت أكبر من أو يساوي «الطول». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:280]

```
281:                         val bytes = ByteArray(length)
```
> يُعرَّف متغيّر ثابت اسمه «بايتات» (bytes) ويُسنَد إليه مصفوفة بايتات بحجم يساوي «الطول». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:281]

```
282:                         buffer.get(bytes)
```
> يُستدعى من المخزن المؤقّت الدالة «احصل» لتعبئة مصفوفة «بايتات». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:282]

```
283:                         String(bytes, Charsets.UTF_8)
```
> يُنشأ نص من مصفوفة «بايتات» بترميز «يو تي إف ٨» كقيمة ناتجة للكتلة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:283]

```
284:                     } else null
```
> إغلاق نطاق الجملة الشرطية مع فرع «وإلّا» يعيد القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:284]

```
285:                 } else null
```
> إغلاق نطاق التعبير الشرطي الخارجي مع فرع «وإلّا» يعيد القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:285]

```
286: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:286]

```
287:                 return BitchatMessage(
```
> جملة إعادة (return) تُنشئ كائناً من الصنف «رسالة بِت-شات» (BitchatMessage) وتعيده. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:287]

```
288:                     id = id,
```
> يُسنَد للوسيط المُسمّى «المعرّف» (id) قيمة المتغيّر «المعرّف» (id). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:288]

```
289:                     sender = sender,
```
> يُسنَد للوسيط المُسمّى «المرسل» (sender) قيمة المتغيّر «المرسل» (sender). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:289]

```
290:                     content = content,
```
> يُسنَد للوسيط المُسمّى «المحتوى» (content) قيمة المتغيّر «المحتوى» (content). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:290]

```
291:                     type = BitchatMessageType.Message,
```
> يُسنَد للوسيط المُسمّى «النوع» (type) القيمة «رسالة» (Message) من النوع المعدود «نوع رسالة بِت-شات» (BitchatMessageType). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:291]

```
292:                     timestamp = timestamp,
```
> يُسنَد للوسيط المُسمّى «الطابع الزمني» (timestamp) قيمة المتغيّر «الطابع الزمني» (timestamp). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:292]

```
293:                     isRelay = isRelay,
```
> يُسنَد للوسيط المُسمّى «هل هو ترحيل» (isRelay) قيمة المتغيّر «هل هو ترحيل» (isRelay). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:293]

```
294:                     originalSender = originalSender,
```
> يُسنَد للوسيط المُسمّى «المرسل الأصلي» (originalSender) قيمة المتغيّر «المرسل الأصلي» (originalSender). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:294]

```
295:                     isPrivate = isPrivate,
```
> يُسنَد للوسيط المُسمّى «هل هو خاص» (isPrivate) قيمة المتغيّر «هل هو خاص» (isPrivate). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:295]

```
296:                     recipientNickname = recipientNickname,
```
> يُسنَد للوسيط المُسمّى «لقب المستلِم» (recipientNickname) قيمة المتغيّر «لقب المستلِم» (recipientNickname). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:296]

```
297:                     senderPeerID = senderPeerID,
```
> يُسنَد للوسيط المُسمّى «معرّف ندّ المرسل» (senderPeerID) قيمة المتغيّر «معرّف ندّ المرسل» (senderPeerID). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:297]

```
298:                     mentions = mentions,
```
> يُسنَد للوسيط المُسمّى «الإشارات» (mentions) قيمة المتغيّر «الإشارات» (mentions). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:298]

```
299:                     channel = channel,
```
> يُسنَد للوسيط المُسمّى «القناة» (channel) قيمة المتغيّر «القناة» (channel). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:299]

```
300:                     encryptedContent = encryptedContent,
```
> يُسنَد للوسيط المُسمّى «المحتوى المشفّر» (encryptedContent) قيمة المتغيّر «المحتوى المشفّر» (encryptedContent). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:300]

```
301:                     isEncrypted = isEncrypted
```
> يُسنَد للوسيط المُسمّى «هل هو مشفّر» (isEncrypted) قيمة المتغيّر «هل هو مشفّر» (isEncrypted). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:301]

```
302:                 )
```
> إغلاق نطاق قائمة وسائط مُنشئ الصنف «رسالة بِت-شات». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:302]

```
303: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:303]

```
304:             } catch (e: Exception) {
```
> بداية كتلة «التقاط» (catch) تلتقط استثناءً اسمه «هـ» (e) من نوع «استثناء» (Exception). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:304]

```
305:                 return null
```
> جملة إعادة تعيد القيمة الفارغة (null) عند حدوث الاستثناء. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:305]

```
306:             }
```
> إغلاق نطاق كتلة «التقاط». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:306]

```
307:         }
```
> إغلاق نطاق الدالة (التي تحوي كتلتي «حاول/التقاط»). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:307]

```
308:     }
```
> إغلاق نطاق الكائن المرافق (companion object) أو الكتلة الحاوية للدالة. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:308]

```
309: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:309]

```
310:     override fun equals(other: Any?): Boolean {
```
> تعريف دالة متجاوِزة (override) اسمها «يساوي» (equals) تأخذ وسيطاً «الآخر» (other) من النوع «أيٌّ ممكن أن يكون فارغاً» (Any?) وتعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:310]

```
311:         if (this === other) return true
```
> جملة شرطية تعيد القيمة «صحيح» (true) إذا كان «هذا» (this) هو ذاته «الآخر» بالمطابقة المرجعية. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:311]

```
312:         if (javaClass != other?.javaClass) return false
```
> جملة شرطية تعيد القيمة «خطأ» (false) إذا اختلف صنف جافا (javaClass) لهذا الكائن عن صنف جافا للكائن «الآخر» (مع الوصول الآمن). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:312]

```
313: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:313]

```
314:         other as BitchatMessage
```
> يُحوَّل الكائن «الآخر» قسريّاً (as) إلى النوع «رسالة بِت-شات». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:314]

```
315: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:315]

```
316:         if (id != other.id) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «المعرّف» (id) عن قيمة «معرّف الآخر». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:316]

```
317:         if (sender != other.sender) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «المرسل» (sender) عن قيمة «مرسل الآخر». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:317]

```
318:         if (content != other.content) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «المحتوى» (content) عن قيمة «محتوى الآخر». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:318]

```
319:         if (type != other.type) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «النوع» (type) عن قيمة «نوع الآخر». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:319]

```
320:         if (timestamp != other.timestamp) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «الطابع الزمني» (timestamp) عن قيمة «طابع الآخر الزمني». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:320]

```
321:         if (isRelay != other.isRelay) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «هل هو ترحيل» (isRelay) عن قيمتها لدى الآخر. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:321]

```
322:         if (originalSender != other.originalSender) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «المرسل الأصلي» (originalSender) عن قيمتها لدى الآخر. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:322]

```
323:         if (isPrivate != other.isPrivate) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «هل هو خاص» (isPrivate) عن قيمتها لدى الآخر. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:323]

```
324:         if (recipientNickname != other.recipientNickname) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «لقب المستلِم» (recipientNickname) عن قيمتها لدى الآخر. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:324]

```
325:         if (senderPeerID != other.senderPeerID) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «معرّف ندّ المرسل» (senderPeerID) عن قيمتها لدى الآخر. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:325]

```
326:         if (mentions != other.mentions) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «الإشارات» (mentions) عن قيمتها لدى الآخر. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:326]

```
327:         if (channel != other.channel) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «القناة» (channel) عن قيمتها لدى الآخر. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:327]

```
328:         if (encryptedContent != null) {
```
> جملة شرطية تتحقّق من أن «المحتوى المشفّر» (encryptedContent) ليس القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:328]

```
329:             if (other.encryptedContent == null) return false
```
> جملة شرطية داخلية تعيد «خطأ» إذا كان «المحتوى المشفّر» لدى الآخر يساوي القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:329]

```
330:             if (!encryptedContent.contentEquals(other.encryptedContent)) return false
```
> جملة شرطية تعيد «خطأ» إذا لم يتطابق محتوى مصفوفة «المحتوى المشفّر» مع محتوى مصفوفة الآخر عبر الدالة «تساوي المحتوى» (contentEquals). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:330]

```
331:         } else if (other.encryptedContent != null) return false
```
> إغلاق نطاق الكتلة مع فرع «وإلّا إذا» (else if) يعيد «خطأ» إذا كان «المحتوى المشفّر» لدى الآخر ليس فارغاً بينما هو فارغ هنا. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:331]

```
332:         if (isEncrypted != other.isEncrypted) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «هل هو مشفّر» (isEncrypted) عن قيمتها لدى الآخر. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:332]

```
333:         if (deliveryStatus != other.deliveryStatus) return false
```
> جملة شرطية تعيد «خطأ» إذا اختلفت قيمة «حالة التسليم» (deliveryStatus) عن قيمتها لدى الآخر. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:333]

```
334: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:334]

```
335:         return true
```
> جملة إعادة تعيد القيمة «صحيح» (true) للدلالة على تساوي الكائنين. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:335]

```
336:     }
```
> إغلاق نطاق الدالة «يساوي». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:336]

```
337: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:337]

```
338:     override fun hashCode(): Int {
```
> تعريف دالة متجاوِزة اسمها «الشفرة المُجزّأة» (hashCode) لا تأخذ وسائط وتعيد عدداً صحيحاً (Int). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:338]

```
339:         var result = id.hashCode()
```
> يُعرَّف متغيّر قابل للتغيير (var) اسمه «النتيجة» (result) ويُسنَد إليه الشفرة المُجزّأة لقيمة «المعرّف». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:339]

```
340:         result = 31 * result + sender.hashCode()
```
> يُعاد إسناد «النتيجة» إلى حاصل ضرب القيمة الحرفية 31 في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «المرسل». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:340]

```
341:         result = 31 * result + content.hashCode()
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «المحتوى». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:341]

```
342:         result = 31 * result + type.hashCode()
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «النوع». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:342]

```
343:         result = 31 * result + timestamp.hashCode()
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «الطابع الزمني». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:343]

```
344:         result = 31 * result + isRelay.hashCode()
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «هل هو ترحيل». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:344]

```
345:         result = 31 * result + (originalSender?.hashCode() ?: 0)
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «المرسل الأصلي» (بوصول آمن) أو القيمة الحرفية 0 عند العدم عبر معامل «إلفيس» (?:). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:345]

```
346:         result = 31 * result + isPrivate.hashCode()
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «هل هو خاص». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:346]

```
347:         result = 31 * result + (recipientNickname?.hashCode() ?: 0)
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «لقب المستلِم» (بوصول آمن) أو 0 عند العدم. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:347]

```
348:         result = 31 * result + (senderPeerID?.hashCode() ?: 0)
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «معرّف ندّ المرسل» (بوصول آمن) أو 0 عند العدم. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:348]

```
349:         result = 31 * result + (mentions?.hashCode() ?: 0)
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «الإشارات» (بوصول آمن) أو 0 عند العدم. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:349]

```
350:         result = 31 * result + (channel?.hashCode() ?: 0)
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «القناة» (بوصول آمن) أو 0 عند العدم. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:350]

```
351:         result = 31 * result + (encryptedContent?.contentHashCode() ?: 0)
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لمحتوى مصفوفة «المحتوى المشفّر» عبر الدالة «شفرة محتوى مُجزّأة» (contentHashCode) أو 0 عند العدم. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:351]

```
352:         result = 31 * result + isEncrypted.hashCode()
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «هل هو مشفّر». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:352]

```
353:         result = 31 * result + (deliveryStatus?.hashCode() ?: 0)
```
> يُعاد إسناد «النتيجة» إلى 31 مضروباً في «النتيجة» مضافاً إليه الشفرة المُجزّأة لقيمة «حالة التسليم» (بوصول آمن) أو 0 عند العدم. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:353]

```
354:         return result
```
> جملة إعادة تعيد قيمة «النتيجة». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:354]

```
355:     }
```
> إغلاق نطاق الدالة «الشفرة المُجزّأة». [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:355]

```
356: }
```
> إغلاق نطاق الصنف «رسالة بِت-شات» (BitchatMessage). [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:356]

```
357: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:357]

```
358: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/BitchatMessage.kt:358]
