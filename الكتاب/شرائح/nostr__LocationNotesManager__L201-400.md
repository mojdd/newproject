# شريحة — app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt (الأسطر 201–400)

```
201:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:201]

```
202:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:202]

```
203:         val trimmed = content.trim()
```
> يُعرَّف متغيّر ثابت اسمه «المُشذَّب» (trimmed) ويُسنَد إليه ناتج استدعاء الدالة trim على المحتوى (content) التي تزيل الفراغات من الطرفين. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:203]

```
204:         if (trimmed.isEmpty()) {
```
> شرط: إذا كان «المُشذَّب» (trimmed) فارغاً (isEmpty يعيد صحيحاً). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:204]

```
205:             return
```
> يُعيد (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:205]

```
206:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:206]

```
207:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:207]

```
208:         // CRITICAL FIX: Get geo-specific relays for sending (matching iOS pattern)
```
> تعليق: إصلاح حَرِج: احصل على المُرحِّلات (relays) الخاصة بالموقع للإرسال (مطابقة لنمط iOS). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:208]

```
209:         // iOS: let relays = dependencies.relayLookup(geohash, TransportConfig.nostrGeoRelayCount)
```
> تعليق: iOS: let relays = dependencies.relayLookup(geohash, TransportConfig.nostrGeoRelayCount). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:209]

```
210:         val relays = try {
```
> يُعرَّف متغيّر ثابت اسمه «المُرحِّلات» (relays) ويُسنَد إليه ناتج كتلة try (محاولة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:210]

```
211:             com.bitchat.android.nostr.RelayDirectory.closestRelaysForGeohash(currentGeohash, 5)
```
> يستدعي الدالة closestRelaysForGeohash من «دليل المُرحِّلات» (RelayDirectory) مع الجيوهاش الحالي (currentGeohash) والعدد 5. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:211]

```
212:         } catch (e: Exception) {
```
> كتلة catch (التقاط) تلتقط استثناءً (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:212]

```
213:             Log.e(TAG, "Failed to lookup relays for geohash $currentGeohash: ${e.message}")
```
> يستدعي Log.e (تسجيل خطأ) بالوسم TAG ونص «Failed to lookup relays for geohash» مع الجيوهاش الحالي ورسالة الاستثناء. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:213]

```
214:             emptyList()
```
> يعيد قائمة فارغة (emptyList) كقيمة لكتلة catch. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:214]

```
215:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:215]

```
216:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:216]

```
217:         // Check if we have relays (iOS pattern: guard !relays.isEmpty())
```
> تعليق: تحقّق إن كان لدينا مُرحِّلات (نمط iOS: guard !relays.isEmpty()). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:217]

```
218:         if (relays.isEmpty()) {
```
> شرط: إذا كانت «المُرحِّلات» (relays) فارغة (isEmpty يعيد صحيحاً). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:218]

```
219:             Log.w(TAG, "Send blocked - no geo relays for geohash: $currentGeohash")
```
> يستدعي Log.w (تسجيل تحذير) بالوسم TAG ونص «Send blocked - no geo relays for geohash» مع الجيوهاش الحالي. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:219]

```
220:             _state.value = State.NO_RELAYS
```
> يُسنِد القيمة State.NO_RELAYS إلى الخاصية value الخاصة بـ _state (الحالة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:220]

```
221:             _errorMessage.value = "No relays available"
```
> يُسنِد النص «No relays available» إلى الخاصية value الخاصة بـ _errorMessage (رسالة الخطأ). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:221]

```
222:             return
```
> يُعيد (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:222]

```
223:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:223]

```
224:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:224]

```
225:         val deriveIdentity = deriveIdentityFunc
```
> يُعرَّف متغيّر ثابت اسمه «اشتقاق الهوية» (deriveIdentity) ويُسنَد إليه قيمة deriveIdentityFunc (دالة اشتقاق الهوية). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:225]

```
226:         if (deriveIdentity == null) {
```
> شرط: إذا كان «اشتقاق الهوية» (deriveIdentity) مساوياً لـ null (لا شيء). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:226]

```
227:             Log.e(TAG, "Cannot send note - deriveIdentity not initialized")
```
> يستدعي Log.e (تسجيل خطأ) بالوسم TAG ونص «Cannot send note - deriveIdentity not initialized». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:227]

```
228:             _errorMessage.value = "Not initialized"
```
> يُسنِد النص «Not initialized» إلى الخاصية value الخاصة بـ _errorMessage (رسالة الخطأ). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:228]

```
229:             return
```
> يُعيد (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:229]

```
230:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:230]

```
231:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:231]

```
232:         Log.d(TAG, "Sending note to geohash: $currentGeohash via ${relays.size} geo relays")
```
> يستدعي Log.d (تسجيل تصحيح) بالوسم TAG ونص «Sending note to geohash» مع الجيوهاش الحالي وعدد المُرحِّلات (relays.size). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:232]

```
233:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:233]

```
234:         scope.launch {
```
> يستدعي launch (إطلاق) على scope (النطاق) لبدء كوروتين (coroutine). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:234]

```
235:             try {
```
> بداية كتلة try (محاولة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:235]

```
236:                 val identity = withContext(Dispatchers.IO) {
```
> يُعرَّف متغيّر ثابت اسمه «الهوية» (identity) ويُسنَد إليه ناتج withContext على مُوزِّع الإدخال/الإخراج (Dispatchers.IO). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:236]

```
237:                     deriveIdentity(currentGeohash)
```
> يستدعي الدالة «اشتقاق الهوية» (deriveIdentity) مع الجيوهاش الحالي (currentGeohash). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:237]

```
238:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:238]

```
239:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:239]

```
240:                 val event = withContext(Dispatchers.IO) {
```
> يُعرَّف متغيّر ثابت اسمه «الحدث» (event) ويُسنَد إليه ناتج withContext على مُوزِّع الإدخال/الإخراج (Dispatchers.IO). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:240]

```
241:                     NostrProtocol.createGeohashTextNote(
```
> يستدعي الدالة createGeohashTextNote من «بروتوكول نوستر» (NostrProtocol). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:241]

```
242:                         content = trimmed,
```
> يمرّر للوسيط content القيمة «المُشذَّب» (trimmed). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:242]

```
243:                         geohash = currentGeohash,
```
> يمرّر للوسيط geohash قيمة الجيوهاش الحالي (currentGeohash). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:243]

```
244:                         senderIdentity = identity,
```
> يمرّر للوسيط senderIdentity (هوية المُرسِل) قيمة «الهوية» (identity). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:244]

```
245:                         nickname = nickname
```
> يمرّر للوسيط nickname (الاسم المستعار) قيمة nickname. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:245]

```
246:                     )
```
> إغلاق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:246]

```
247:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:247]

```
248:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:248]

```
249:                 // Optimistic local echo - add note immediately to UI
```
> تعليق: صدى محلّي متفائل - أضف الملاحظة فوراً إلى واجهة المستخدم. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:249]

```
250:                 val localNote = Note(
```
> يُعرَّف متغيّر ثابت اسمه «الملاحظة المحلّية» (localNote) ويُسنَد إليه كائن جديد من النوع Note (ملاحظة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:250]

```
251:                     id = event.id,
```
> يمرّر للوسيط id قيمة معرّف «الحدث» (event.id). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:251]

```
252:                     pubkey = event.pubkey,
```
> يمرّر للوسيط pubkey (المفتاح العام) قيمة event.pubkey. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:252]

```
253:                     content = trimmed,
```
> يمرّر للوسيط content القيمة «المُشذَّب» (trimmed). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:253]

```
254:                     createdAt = event.createdAt,
```
> يمرّر للوسيط createdAt (وقت الإنشاء) قيمة event.createdAt. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:254]

```
255:                     nickname = nickname
```
> يمرّر للوسيط nickname (الاسم المستعار) قيمة nickname. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:255]

```
256:                 )
```
> إغلاق قائمة وسائط المُنشئ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:256]

```
257:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:257]

```
258:                 if (!noteIDs.contains(event.id)) {
```
> شرط: إذا كانت مجموعة معرّفات الملاحظات (noteIDs) لا تحتوي على معرّف «الحدث» (event.id). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:258]

```
259:                     noteIDs.add(event.id)
```
> يستدعي add (إضافة) على noteIDs لإضافة معرّف «الحدث» (event.id). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:259]

```
260:                     val currentNotes = _notes.value ?: emptyList()
```
> يُعرَّف متغيّر ثابت اسمه «الملاحظات الحالية» (currentNotes) ويُسنَد إليه قيمة _notes.value أو قائمة فارغة (emptyList) إن كانت null. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:260]

```
261:                     _notes.value = (currentNotes + localNote).sortedByDescending { it.createdAt }
```
> يُسنِد إلى _notes.value قائمة «الملاحظات الحالية» مضافاً إليها «الملاحظة المحلّية» مرتّبة تنازلياً (sortedByDescending) حسب createdAt. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:261]

```
262:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:262]

```
263:                     // Trim if exceeds max
```
> تعليق: قُصّ إن تجاوز الحدّ الأقصى. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:263]

```
264:                     if (noteIDs.size > MAX_NOTES_IN_MEMORY) {
```
> شرط: إذا كان حجم noteIDs (noteIDs.size) أكبر من MAX_NOTES_IN_MEMORY (الحد الأقصى للملاحظات في الذاكرة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:264]

```
265:                         trimOldestNotes()
```
> يستدعي الدالة trimOldestNotes (قصّ أقدم الملاحظات). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:265]

```
266:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:266]

```
267:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:267]

```
268:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:268]

```
269:                 // CRITICAL FIX: Send to geo-specific relays (matching iOS pattern)
```
> تعليق: إصلاح حَرِج: أرسِل إلى المُرحِّلات الخاصة بالموقع (مطابقة لنمط iOS). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:269]

```
270:                 // iOS: dependencies.sendEvent(event, relays)
```
> تعليق: iOS: dependencies.sendEvent(event, relays). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:270]

```
271:                 withContext(Dispatchers.IO) {
```
> يستدعي withContext على مُوزِّع الإدخال/الإخراج (Dispatchers.IO). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:271]

```
272:                     sendEventFunc?.invoke(event, relays)
```
> يستدعي invoke على sendEventFunc (دالة إرسال الحدث) بأمان (?.) مع «الحدث» (event) و«المُرحِّلات» (relays). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:272]

```
273:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:273]

```
274:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:274]

```
275:                 Log.d(TAG, "✅ Note sent successfully to ${relays.size} geo relays: ${event.id.take(16)}...")
```
> يستدعي Log.d (تسجيل تصحيح) بالوسم TAG ونص «Note sent successfully to» مع عدد المُرحِّلات (relays.size) وأول 16 حرفاً من معرّف الحدث (event.id.take(16)). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:275]

```
276:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:276]

```
277:                 // Clear any error messages on successful send
```
> تعليق: امسح أي رسائل خطأ عند الإرسال الناجح. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:277]

```
278:                 _errorMessage.value = null
```
> يُسنِد القيمة null (لا شيء) إلى الخاصية value الخاصة بـ _errorMessage (رسالة الخطأ). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:278]

```
279:                 _state.value = State.READY
```
> يُسنِد القيمة State.READY إلى الخاصية value الخاصة بـ _state (الحالة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:279]

```
280:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:280]

```
281:             } catch (e: Exception) {
```
> كتلة catch (التقاط) تلتقط استثناءً (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:281]

```
282:                 Log.e(TAG, "Failed to send note: ${e.message}")
```
> يستدعي Log.e (تسجيل خطأ) بالوسم TAG ونص «Failed to send note» مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:282]

```
283:                 _errorMessage.value = "Failed to send: ${e.message}"
```
> يُسنِد النص «Failed to send» مع رسالة الاستثناء (e.message) إلى الخاصية value الخاصة بـ _errorMessage (رسالة الخطأ). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:283]

```
284:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:284]

```
285:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:285]

```
286:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:286]

```
287:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:287]

```
288:     /**
```
> بداية تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:288]

```
289:      * Subscribe to location notes for current geohash
```
> تعليق: اشترِك في ملاحظات الموقع للجيوهاش الحالي. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:289]

```
290:      */
```
> إغلاق تعليق التوثيق (KDoc). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:290]

```
291:     private fun subscribeAll() {
```
> يُعرَّف دالة خاصة (private) اسمها «الاشتراك في الكل» (subscribeAll) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:291]

```
292:         val currentGeohash = _geohash.value
```
> يُعرَّف متغيّر ثابت اسمه «الجيوهاش الحالي» (currentGeohash) ويُسنَد إليه قيمة _geohash.value. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:292]

```
293:         if (currentGeohash == null) {
```
> شرط: إذا كان «الجيوهاش الحالي» (currentGeohash) مساوياً لـ null (لا شيء). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:293]

```
294:             Log.w(TAG, "Cannot subscribe - no geohash set")
```
> يستدعي Log.w (تسجيل تحذير) بالوسم TAG ونص «Cannot subscribe - no geohash set». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:294]

```
295:             _state.value = State.IDLE
```
> يُسنِد القيمة State.IDLE إلى الخاصية value الخاصة بـ _state (الحالة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:295]

```
296:             return
```
> يُعيد (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:296]

```
297:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:297]

```
298:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:298]

```
299:         val subscribe = subscribeFunc
```
> يُعرَّف متغيّر ثابت اسمه «اشتراك» (subscribe) ويُسنَد إليه قيمة subscribeFunc (دالة الاشتراك). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:299]

```
300:         if (subscribe == null) {
```
> شرط: إذا كان «اشتراك» (subscribe) مساوياً لـ null (لا شيء). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:300]

```
301:             Log.e(TAG, "Cannot subscribe - subscribe function not initialized; will retry shortly")
```
> يستدعي Log.e (تسجيل خطأ) بالوسم TAG ونص «Cannot subscribe - subscribe function not initialized; will retry shortly». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:301]

```
302:             _state.value = State.LOADING
```
> يُسنِد القيمة State.LOADING إلى الخاصية value الخاصة بـ _state (الحالة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:302]

```
303:             // Retry a few times in case initialization is racing the sheet open
```
> تعليق: أعِد المحاولة بضع مرّات في حال كانت التهيئة تتسابق مع فتح الورقة (sheet). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:303]

```
304:             scope.launch {
```
> يستدعي launch (إطلاق) على scope (النطاق) لبدء كوروتين. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:304]

```
305:                 var attempts = 0
```
> يُعرَّف متغيّر متغيّر (var) اسمه «المحاولات» (attempts) ويُسنَد إليه القيمة 0. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:305]

```
306:                 while (attempts < 10 && subscribeFunc == null) {
```
> حلقة while (طالما) تستمر ما دامت «المحاولات» أقل من 10 و subscribeFunc مساوياً لـ null. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:306]

```
307:                     delay(300)
```
> يستدعي delay (تأخير) بـ 300 (مللي ثانية). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:307]

```
308:                     attempts++
```
> يزيد «المحاولات» (attempts) بمقدار واحد. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:308]

```
309:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:309]

```
310:                 val subNow = subscribeFunc
```
> يُعرَّف متغيّر ثابت اسمه «الاشتراك الآن» (subNow) ويُسنَد إليه قيمة subscribeFunc. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:310]

```
311:                 if (subNow != null) {
```
> شرط: إذا كان «الاشتراك الآن» (subNow) غير مساوٍ لـ null. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:311]

```
312:                     // Try again now that dependencies are ready
```
> تعليق: حاول مجدداً الآن بعد أن أصبحت التبعيات (dependencies) جاهزة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:312]

```
313:                     subscribeAll()
```
> يستدعي الدالة «الاشتراك في الكل» (subscribeAll). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:313]

```
314:                 } else {
```
> وإلّا (else). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:314]

```
315:                     // Give UI a chance to show empty state rather than spinner forever
```
> تعليق: امنح واجهة المستخدم فرصة لإظهار الحالة الفارغة بدل المُحمِّل الدوّار (spinner) إلى الأبد. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:315]

```
316:                     if (!_initialLoadComplete.value!!) {
```
> شرط: إذا كانت قيمة _initialLoadComplete.value (اكتمال التحميل الأولي) ليست صحيحة (نفي مع تأكيد عدم العدم !!). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:316]

```
317:                         _initialLoadComplete.value = true
```
> يُسنِد القيمة true (صحيح) إلى الخاصية value الخاصة بـ _initialLoadComplete (اكتمال التحميل الأولي). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:317]

```
318:                         _state.value = State.READY
```
> يُسنِد القيمة State.READY إلى الخاصية value الخاصة بـ _state (الحالة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:318]

```
319:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:319]

```
320:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:320]

```
321:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:321]

```
322:             return
```
> يُعيد (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:322]

```
323:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:323]

```
324:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:324]

```
325:         _state.value = State.LOADING
```
> يُسنِد القيمة State.LOADING إلى الخاصية value الخاصة بـ _state (الحالة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:325]

```
326:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:326]

```
327:         // Subscribe for each geohash in the ±1 set
```
> تعليق: اشترِك لكل جيوهاش في مجموعة ±1. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:327]

```
328:         subscribedGeohashes.forEach { gh ->
```
> يستدعي forEach (لكل) على «الجيوهاشات المشترَك بها» (subscribedGeohashes) مع معامل لكل عنصر اسمه gh. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:328]

```
329:             val filter = NostrFilter.geohashNotes(
```
> يُعرَّف متغيّر ثابت اسمه «مُرشِّح» (filter) ويُسنَد إليه ناتج geohashNotes من NostrFilter (مُرشِّح نوستر). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:329]

```
330:                 geohash = gh,
```
> يمرّر للوسيط geohash قيمة gh. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:330]

```
331:                 since = null,
```
> يمرّر للوسيط since (منذ) القيمة null (لا شيء). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:331]

```
332:                 limit = 200
```
> يمرّر للوسيط limit (الحد) القيمة 200. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:332]

```
333:             )
```
> إغلاق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:333]

```
334:             val subId = "location-notes-$gh"
```
> يُعرَّف متغيّر ثابت اسمه «معرّف الاشتراك» (subId) ويُسنَد إليه النص «location-notes-» مع قيمة gh. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:334]

```
335:             Log.d(TAG, "📡 Subscribing to location notes: $subId")
```
> يستدعي Log.d (تسجيل تصحيح) بالوسم TAG ونص «Subscribing to location notes» مع «معرّف الاشتراك» (subId). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:335]

```
336:             try {
```
> بداية كتلة try (محاولة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:336]

```
337:                 val id = subscribe(filter, subId) { event -> handleEvent(event) }
```
> يُعرَّف متغيّر ثابت اسمه «معرّف» (id) ويُسنَد إليه ناتج استدعاء «اشتراك» (subscribe) مع «المُرشِّح» و«معرّف الاشتراك» ولمدا تستدعي handleEvent على «الحدث» (event). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:337]

```
338:                 subscriptionIDs[gh] = id
```
> يُسنِد «المعرّف» (id) إلى عنصر «معرّفات الاشتراكات» (subscriptionIDs) عند المفتاح gh. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:338]

```
339:             } catch (e: Exception) {
```
> كتلة catch (التقاط) تلتقط استثناءً (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:339]

```
340:                 Log.e(TAG, "Failed to subscribe for $gh: ${e.message}")
```
> يستدعي Log.e (تسجيل خطأ) بالوسم TAG ونص «Failed to subscribe for» مع gh ورسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:340]

```
341:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:341]

```
342:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:342]

```
343:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:343]

```
344:         // Mark initial load complete after brief delay to allow relay responses
```
> تعليق: علّم اكتمال التحميل الأولي بعد تأخير قصير للسماح بردود المُرحِّلات. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:344]

```
345:         scope.launch {
```
> يستدعي launch (إطلاق) على scope (النطاق) لبدء كوروتين. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:345]

```
346:             delay(2000) // Wait 2 seconds for initial batch
```
> يستدعي delay (تأخير) بـ 2000 (مللي ثانية) مع تعليق: انتظر ثانيتين للدفعة الأولى. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:346]

```
347:             if (!_initialLoadComplete.value!!) {
```
> شرط: إذا كانت قيمة _initialLoadComplete.value (اكتمال التحميل الأولي) ليست صحيحة (نفي مع تأكيد عدم العدم !!). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:347]

```
348:                 _initialLoadComplete.value = true
```
> يُسنِد القيمة true (صحيح) إلى الخاصية value الخاصة بـ _initialLoadComplete (اكتمال التحميل الأولي). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:348]

```
349:                 _state.value = State.READY
```
> يُسنِد القيمة State.READY إلى الخاصية value الخاصة بـ _state (الحالة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:349]

```
350:                 Log.d(TAG, "Initial load complete for geohash: $currentGeohash (${noteIDs.size} notes)")
```
> يستدعي Log.d (تسجيل تصحيح) بالوسم TAG ونص «Initial load complete for geohash» مع الجيوهاش الحالي وعدد معرّفات الملاحظات (noteIDs.size). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:350]

```
351:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:351]

```
352:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:352]

```
353:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:353]

```
354:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:354]

```
355:     /**
```
> بداية تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:355]

```
356:      * Handle incoming event from subscription
```
> تعليق: عالِج الحدث الوارد من الاشتراك. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:356]

```
357:      */
```
> إغلاق تعليق التوثيق (KDoc). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:357]

```
358:     private fun handleEvent(event: NostrEvent) {
```
> يُعرَّف دالة خاصة (private) اسمها «معالجة الحدث» (handleEvent) تأخذ وسيطاً event من النوع NostrEvent (حدث نوستر). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:358]

```
359:         // Validate event
```
> تعليق: تحقّق من صحة الحدث. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:359]

```
360:         if (event.kind != NostrKind.TEXT_NOTE) {
```
> شرط: إذا كان نوع الحدث (event.kind) لا يساوي NostrKind.TEXT_NOTE (ملاحظة نصية). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:360]

```
361:             Log.v(TAG, "Ignoring non-text-note event: kind=${event.kind}")
```
> يستدعي Log.v (تسجيل مُسهَب) بالوسم TAG ونص «Ignoring non-text-note event: kind=» مع نوع الحدث (event.kind). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:361]

```
362:             return
```
> يُعيد (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:362]

```
363:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:363]

```
364:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:364]

```
365:         // Check for geohash tag
```
> تعليق: ابحث عن وسم الجيوهاش. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:365]

```
366:         val geohashTag = event.tags.firstOrNull { it.size >= 2 && it[0] == "g" }
```
> يُعرَّف متغيّر ثابت اسمه «وسم الجيوهاش» (geohashTag) ويُسنَد إليه أول عنصر (firstOrNull) من وسوم الحدث (event.tags) حجمه ≥ 2 وعنصره الأول يساوي «g». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:366]

```
367:         if (geohashTag == null) {
```
> شرط: إذا كان «وسم الجيوهاش» (geohashTag) مساوياً لـ null (لا شيء). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:367]

```
368:             Log.v(TAG, "Ignoring event without geohash tag: ${event.id.take(16)}...")
```
> يستدعي Log.v (تسجيل مُسهَب) بالوسم TAG ونص «Ignoring event without geohash tag» مع أول 16 حرفاً من معرّف الحدث (event.id.take(16)). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:368]

```
369:             return
```
> يُعيد (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:369]

```
370:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:370]

```
371:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:371]

```
372:         // Check if matches current geohash
```
> تعليق: تحقّق إن كان يطابق الجيوهاش الحالي. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:372]

```
373:         val eventGeohash = geohashTag[1]
```
> يُعرَّف متغيّر ثابت اسمه «جيوهاش الحدث» (eventGeohash) ويُسنَد إليه العنصر الثاني من «وسم الجيوهاش» (geohashTag[1]). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:373]

```
374:         if (!subscribedGeohashes.contains(eventGeohash)) {
```
> شرط: إذا كانت «الجيوهاشات المشترَك بها» (subscribedGeohashes) لا تحتوي على «جيوهاش الحدث» (eventGeohash). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:374]

```
375:             Log.v(TAG, "Ignoring event for non-subscribed geohash: $eventGeohash")
```
> يستدعي Log.v (تسجيل مُسهَب) بالوسم TAG ونص «Ignoring event for non-subscribed geohash» مع «جيوهاش الحدث» (eventGeohash). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:375]

```
376:             return
```
> يُعيد (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:376]

```
377:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:377]

```
378:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:378]

```
379:         // Deduplicate
```
> تعليق: أزِل التكرار. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:379]

```
380:         if (noteIDs.contains(event.id)) {
```
> شرط: إذا كانت «معرّفات الملاحظات» (noteIDs) تحتوي على معرّف الحدث (event.id). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:380]

```
381:             return
```
> يُعيد (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:381]

```
382:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:382]

```
383:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:383]

```
384:         // Extract nickname from tags
```
> تعليق: استخرج الاسم المستعار من الوسوم. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:384]

```
385:         val nicknameTag = event.tags.firstOrNull { it.size >= 2 && it[0] == "n" }
```
> يُعرَّف متغيّر ثابت اسمه «وسم الاسم المستعار» (nicknameTag) ويُسنَد إليه أول عنصر (firstOrNull) من وسوم الحدث (event.tags) حجمه ≥ 2 وعنصره الأول يساوي «n». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:385]

```
386:         val nickname = nicknameTag?.get(1)
```
> يُعرَّف متغيّر ثابت اسمه «الاسم المستعار» (nickname) ويُسنَد إليه العنصر الثاني من «وسم الاسم المستعار» بأمان (nicknameTag?.get(1)). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:386]

```
387:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:387]

```
388:         // Create note
```
> تعليق: أنشئ ملاحظة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:388]

```
389:         val note = Note(
```
> يُعرَّف متغيّر ثابت اسمه «ملاحظة» (note) ويُسنَد إليه كائن جديد من النوع Note (ملاحظة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:389]

```
390:             id = event.id,
```
> يمرّر للوسيط id قيمة معرّف الحدث (event.id). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:390]

```
391:             pubkey = event.pubkey,
```
> يمرّر للوسيط pubkey (المفتاح العام) قيمة event.pubkey. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:391]

```
392:             content = event.content,
```
> يمرّر للوسيط content قيمة محتوى الحدث (event.content). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:392]

```
393:             createdAt = event.createdAt,
```
> يمرّر للوسيط createdAt (وقت الإنشاء) قيمة event.createdAt. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:393]

```
394:             nickname = nickname
```
> يمرّر للوسيط nickname (الاسم المستعار) قيمة nickname. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:394]

```
395:         )
```
> إغلاق قائمة وسائط المُنشئ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:395]

```
396:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:396]

```
397:         // Add to collection
```
> تعليق: أضِف إلى المجموعة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:397]

```
398:         noteIDs.add(event.id)
```
> يستدعي add (إضافة) على «معرّفات الملاحظات» (noteIDs) لإضافة معرّف الحدث (event.id). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:398]

```
399:         val currentNotes = _notes.value ?: emptyList()
```
> يُعرَّف متغيّر ثابت اسمه «الملاحظات الحالية» (currentNotes) ويُسنَد إليه قيمة _notes.value أو قائمة فارغة (emptyList) إن كانت null. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:399]

```
400:         _notes.value = (currentNotes + note).sortedByDescending { it.createdAt }
```
> يُسنِد إلى _notes.value قائمة «الملاحظات الحالية» مضافاً إليها «الملاحظة» مرتّبة تنازلياً (sortedByDescending) حسب createdAt. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:400]
