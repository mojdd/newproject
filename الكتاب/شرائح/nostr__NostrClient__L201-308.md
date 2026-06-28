# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrClient.kt (الأسطر 201–308)

```
201:             geohash = geohash,
```
> يُمرَّر للوسيط المسمّى «geohash» (المنطقة الجغرافية المختصرة) قيمة المتغيّر geohash. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:201]

```
202:             since = System.currentTimeMillis() - 3600000L, // Last hour
```
> يُمرَّر للوسيط المسمّى «since» (منذ) ناتج طرح العدد 3600000L من القيمة الزمنية الحاليّة بالميلّي ثانية System.currentTimeMillis()؛ والتعليق: الساعة الأخيرة. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:202]

```
203:             limit = 200
```
> يُمرَّر للوسيط المسمّى «limit» (الحدّ) القيمة 200. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:203]

```
204:         )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:204]

```
205:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:205]

```
206:         relayManager.subscribe(filter, "geohash-$geohash", { event ->
```
> يُستدعى التابع subscribe (الاشتراك) من مدير المُرحِّلات relayManager بثلاثة وسطاء: المرشّح filter، والنصّ "geohash-$geohash"، ودالّة لمبدا تأخذ المعامل event (الحدث). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:206]

```
207:             scope.launch {
```
> يُستدعى التابع launch (الإطلاق) من النطاق scope مع كتلة لمبدا. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:207]

```
208:                 handleGeohashMessage(event, handler)
```
> يُستدعى التابع handleGeohashMessage (معالجة رسالة المنطقة الجغرافية) بوسيطين: الحدث event والمعالج handler. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:208]

```
209:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:209]

```
210:         })
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:210]

```
211:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:211]

```
212:         Log.i(TAG, "🌍 Subscribed to geohash channel: #$geohash")
```
> يُستدعى التابع i (مستوى المعلومات) من السجلّ Log بوسيطين: الوسم TAG والنصّ "🌍 Subscribed to geohash channel: #$geohash". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:212]

```
213:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:213]

```
214:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:214]

```
215:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:215]

```
216:      * Unsubscribe from a geohash channel
```
> تعليق: إلغاء الاشتراك من قناة منطقة جغرافية. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:216]

```
217:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:217]

```
218:     fun unsubscribeFromGeohash(geohash: String) {
```
> يُعرَّف التابع unsubscribeFromGeohash (إلغاء الاشتراك من المنطقة الجغرافية) الذي يأخذ معاملاً geohash من نوع نصّ String. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:218]

```
219:         relayManager.unsubscribe("geohash-$geohash")
```
> يُستدعى التابع unsubscribe (إلغاء الاشتراك) من مدير المُرحِّلات relayManager بوسيط نصّي "geohash-$geohash". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:219]

```
220:         Log.i(TAG, "Unsubscribed from geohash channel: #$geohash")
```
> يُستدعى التابع i من السجلّ Log بوسيطين: الوسم TAG والنصّ "Unsubscribed from geohash channel: #$geohash". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:220]

```
221:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:221]

```
222:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:222]

```
223:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:223]

```
224:      * Get current identity information
```
> تعليق: الحصول على معلومات الهويّة الحاليّة. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:224]

```
225:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:225]

```
226:     fun getCurrentIdentity(): NostrIdentity? = currentIdentity
```
> يُعرَّف التابع getCurrentIdentity (الحصول على الهويّة الحاليّة) الذي يُعيد قيمة من نوع NostrIdentity قابلة للعدم (?)، وقيمته هي المتغيّر currentIdentity. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:226]

```
227:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:227]

```
228:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:228]

```
229:      * Get relay connection status
```
> تعليق: الحصول على حالة اتّصال المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:229]

```
230:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:230]

```
231:     val relayConnectionStatus: StateFlow<Boolean> = relayManager.isConnected
```
> يُعرَّف الخاصّيّة الثابتة relayConnectionStatus (حالة اتّصال المُرحِّل) من نوع StateFlow<Boolean> (تدفّق حالة منطقي)، وقيمتها هي الخاصّيّة isConnected من مدير المُرحِّلات relayManager. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:231]

```
232:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:232]

```
233:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:233]

```
234:      * Get relay information
```
> تعليق: الحصول على معلومات المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:234]

```
235:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:235]

```
236:     val relayInfo: StateFlow<List<NostrRelayManager.Relay>> = relayManager.relays
```
> يُعرَّف الخاصّيّة الثابتة relayInfo (معلومات المُرحِّل) من نوع StateFlow<List<NostrRelayManager.Relay>> (تدفّق حالة لقائمة من مُرحِّلات NostrRelayManager.Relay)، وقيمتها هي الخاصّيّة relays من مدير المُرحِّلات relayManager. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:236]

```
237:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:237]

```
238:     // MARK: - Private Methods
```
> تعليق: علامة فاصلة — التوابع الخاصّة (Private Methods). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:238]

```
239:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:239]

```
240:     private suspend fun handlePrivateMessage(
```
> يُعرَّف التابع الخاصّ المعلّق suspend (القابل للتعليق) المسمّى handlePrivateMessage (معالجة الرسالة الخاصّة) وبداية قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:240]

```
241:         giftWrap: NostrEvent,
```
> يُعرَّف المعامل giftWrap (الغلاف الهديّة) من نوع NostrEvent (حدث نوستر). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:241]

```
242:         handler: (content: String, senderNpub: String, timestamp: Int) -> Unit
```
> يُعرَّف المعامل handler (المعالج) من نوع دالّة تأخذ content من نصّ String وsenderNpub من نصّ String وtimestamp من عدد صحيح Int وتُعيد Unit (لا شيء). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:242]

```
243:     ) {
```
> إغلاق قائمة المعاملات وبداية جسم التابع. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:243]

```
244:         // Age filtering (24h + 15min buffer for randomized timestamps)
```
> تعليق: تصفية حسب العمر (٢٤ ساعة + ١٥ دقيقة هامش للأختام الزمنية العشوائية). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:244]

```
245:         val messageAge = System.currentTimeMillis() / 1000 - giftWrap.createdAt
```
> يُعرَّف المتغيّر الثابت messageAge (عمر الرسالة) وقيمته ناتج طرح خاصّيّة createdAt من giftWrap من القيمة الزمنية الحاليّة بالميلّي ثانية مقسومة على 1000. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:245]

```
246:         if (messageAge > 173700) { // 48 hours + 15 minutes
```
> شرط: إذا كان messageAge أكبر من 173700؛ والتعليق: ٤٨ ساعة + ١٥ دقيقة. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:246]

```
247:             Log.v(TAG, "Ignoring old private message")
```
> يُستدعى التابع v (مستوى التتبّع) من السجلّ Log بوسيطين: الوسم TAG والنصّ "Ignoring old private message". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:247]

```
248:             return
```
> يُعيد التحكّم (الخروج من التابع). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:248]

```
249:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:249]

```
250:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:250]

```
251:         val identity = currentIdentity ?: return
```
> يُعرَّف المتغيّر الثابت identity (الهويّة) وقيمته currentIdentity؛ وإن كانت عدماً فيُعاد التحكّم (الخروج من التابع). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:251]

```
252:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:252]

```
253:         try {
```
> بداية كتلة المحاولة try. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:253]

```
254:             val decryptResult = NostrProtocol.decryptPrivateMessage(giftWrap, identity)
```
> يُعرَّف المتغيّر الثابت decryptResult (نتيجة فكّ التشفير) وقيمته ناتج استدعاء التابع decryptPrivateMessage (فكّ تشفير الرسالة الخاصّة) من NostrProtocol بوسيطين: giftWrap وidentity. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:254]

```
255:             if (decryptResult != null) {
```
> شرط: إذا كان decryptResult لا يساوي عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:255]

```
256:                 val (content, senderPubkey, timestamp) = decryptResult
```
> يُفكَّك decryptResult إلى ثلاثة متغيّرات ثابتة: content (المحتوى) وsenderPubkey (مفتاح المرسِل العامّ) وtimestamp (الختم الزمني). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:256]

```
257:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:257]

```
258:                 // Convert sender pubkey to npub
```
> تعليق: تحويل مفتاح المرسِل العامّ إلى npub. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:258]

```
259:                 val senderNpub = try {
```
> يُعرَّف المتغيّر الثابت senderNpub (npub المرسِل) وقيمته ناتج كتلة المحاولة try. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:259]

```
260:                     Bech32.encode("npub", senderPubkey.hexToByteArray())
```
> يُستدعى التابع encode (التشفير/الترميز) من Bech32 بوسيطين: النصّ "npub" وناتج التابع hexToByteArray (تحويل الستّ عشري إلى مصفوفة بايتات) من senderPubkey. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:260]

```
261:                 } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وبداية كتلة التقاط الاستثناء catch بالمعامل e من نوع Exception (استثناء). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:261]

```
262:                     Log.w(TAG, "Failed to encode sender npub: ${e.message}")
```
> يُستدعى التابع w (مستوى التحذير) من السجلّ Log بوسيطين: الوسم TAG والنصّ "Failed to encode sender npub: ${e.message}". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:262]

```
263:                     "npub_decode_error"
```
> النصّ "npub_decode_error" كقيمة ناتجة لكتلة التقاط الاستثناء. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:263]

```
264:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:264]

```
265:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:265]

```
266:                 Log.d(TAG, "📥 Received private message from ${senderNpub.take(16)}...")
```
> يُستدعى التابع d (مستوى التصحيح) من السجلّ Log بوسيطين: الوسم TAG والنصّ "📥 Received private message from ${senderNpub.take(16)}..." حيث take(16) يأخذ أوّل ١٦ محرفاً من senderNpub. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:266]

```
267:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:267]

```
268:                 // Dispatch to main thread for handler
```
> تعليق: التوجيه إلى الخيط الرئيسي للمعالج. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:268]

```
269:                 withContext(Dispatchers.Main) {
```
> يُستدعى التابع withContext (مع السياق) بوسيط Dispatchers.Main (موزّع الخيط الرئيسي) مع كتلة لمبدا. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:269]

```
270:                     handler(content, senderNpub, timestamp)
```
> يُستدعى المعالج handler بثلاثة وسطاء: content وsenderNpub وtimestamp. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:270]

```
271:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:271]

```
272:             } else {
```
> إغلاق نطاق الشرط وبداية كتلة وإلّا else. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:272]

```
273:                 Log.w(TAG, "Failed to decrypt private message")
```
> يُستدعى التابع w من السجلّ Log بوسيطين: الوسم TAG والنصّ "Failed to decrypt private message". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:273]

```
274:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:274]

```
275:         } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وبداية كتلة التقاط الاستثناء catch بالمعامل e من نوع Exception. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:275]

```
276:             Log.e(TAG, "Error handling private message: ${e.message}")
```
> يُستدعى التابع e (مستوى الخطأ) من السجلّ Log بوسيطين: الوسم TAG والنصّ "Error handling private message: ${e.message}". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:276]

```
277:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:277]

```
278:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:278]

```
279:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:279]

```
280:     private suspend fun handleGeohashMessage(
```
> يُعرَّف التابع الخاصّ المعلّق suspend المسمّى handleGeohashMessage (معالجة رسالة المنطقة الجغرافية) وبداية قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:280]

```
281:         event: NostrEvent,
```
> يُعرَّف المعامل event (الحدث) من نوع NostrEvent. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:281]

```
282:         handler: (content: String, senderPubkey: String, nickname: String?, timestamp: Int) -> Unit
```
> يُعرَّف المعامل handler من نوع دالّة تأخذ content من نصّ String وsenderPubkey من نصّ String وnickname من نصّ String قابل للعدم (?) وtimestamp من عدد صحيح Int وتُعيد Unit. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:282]

```
283:     ) {
```
> إغلاق قائمة المعاملات وبداية جسم التابع. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:283]

```
284:         try {
```
> بداية كتلة المحاولة try. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:284]

```
285:             // Check Proof of Work validation for incoming geohash events
```
> تعليق: التحقّق من تصديق إثبات العمل لأحداث المنطقة الجغرافية الواردة. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:285]

```
286:             val powSettings = PoWPreferenceManager.getCurrentSettings()
```
> يُعرَّف المتغيّر الثابت powSettings (إعدادات إثبات العمل) وقيمته ناتج التابع getCurrentSettings (الحصول على الإعدادات الحاليّة) من PoWPreferenceManager. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:286]

```
287:             if (powSettings.enabled && powSettings.difficulty > 0) {
```
> شرط: إذا كانت خاصّيّة enabled (مُفعَّل) من powSettings صحيحة وخاصّيّة difficulty (الصعوبة) أكبر من 0. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:287]

```
288:                 if (!NostrProofOfWork.validateDifficulty(event, powSettings.difficulty)) {
```
> شرط: إذا كان نفي ناتج التابع validateDifficulty (تصديق الصعوبة) من NostrProofOfWork المُستدعى بوسيطين: event وpowSettings.difficulty. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:288]

```
289:                     Log.w(TAG, "🚫 Rejecting geohash event ${event.id.take(8)}... due to insufficient PoW (required: ${powSettings.difficulty})")
```
> يُستدعى التابع w من السجلّ Log بوسيطين: الوسم TAG والنصّ "🚫 Rejecting geohash event ${event.id.take(8)}... due to insufficient PoW (required: ${powSettings.difficulty})" حيث take(8) يأخذ أوّل ٨ محارف من event.id. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:289]

```
290:                     return
```
> يُعيد التحكّم (الخروج من التابع). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:290]

```
291:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:291]

```
292:                 Log.v(TAG, "✅ PoW validation passed for geohash event ${event.id.take(8)}...")
```
> يُستدعى التابع v من السجلّ Log بوسيطين: الوسم TAG والنصّ "✅ PoW validation passed for geohash event ${event.id.take(8)}..." حيث take(8) يأخذ أوّل ٨ محارف من event.id. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:292]

```
293:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:293]

```
294:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:294]

```
295:             // Extract nickname from tags
```
> تعليق: استخراج الاسم المستعار من الوسوم. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:295]

```
296:             val nickname = event.tags.find { it.size >= 2 && it[0] == "n" }?.get(1)
```
> يُعرَّف المتغيّر الثابت nickname (الاسم المستعار) وقيمته ناتج التابع find (البحث) على tags من event عن أوّل عنصر حجمه size أكبر من أو يساوي 2 وعنصره الأوّل [0] يساوي النصّ "n"، ثمّ get(1) لجلب العنصر الثاني إن وُجد. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:296]

```
297:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:297]

```
298:             Log.v(TAG, "📥 Received geohash message from ${event.pubkey.take(16)}...")
```
> يُستدعى التابع v من السجلّ Log بوسيطين: الوسم TAG والنصّ "📥 Received geohash message from ${event.pubkey.take(16)}..." حيث take(16) يأخذ أوّل ١٦ محرفاً من event.pubkey. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:298]

```
299:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:299]

```
300:             // Dispatch to main thread for handler
```
> تعليق: التوجيه إلى الخيط الرئيسي للمعالج. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:300]

```
301:             withContext(Dispatchers.Main) {
```
> يُستدعى التابع withContext بوسيط Dispatchers.Main مع كتلة لمبدا. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:301]

```
302:                 handler(event.content, event.pubkey, nickname, event.createdAt)
```
> يُستدعى المعالج handler بأربعة وسطاء: content من event وpubkey من event وnickname وcreatedAt من event. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:302]

```
303:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:303]

```
304:         } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وبداية كتلة التقاط الاستثناء catch بالمعامل e من نوع Exception. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:304]

```
305:             Log.e(TAG, "Error handling geohash message: ${e.message}")
```
> يُستدعى التابع e من السجلّ Log بوسيطين: الوسم TAG والنصّ "Error handling geohash message: ${e.message}". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:305]

```
306:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:306]

```
307:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:307]

```
308: }
```
> إغلاق نطاق (إغلاق الصنف). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:308]
