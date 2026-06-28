# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt (الأسطر 201–400)

```
201:         // Ensure relays are tracked for UI/status
```
> تعليق: تأكَّد أن المُرحِّلات (relays) مُتتبَّعة لواجهة المستخدم أو الحالة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:201]

```
202:         relayUrls.forEach { url ->
```
> يمرّ على كل عنصر في قائمة عناوين المُرحِّلات (relayUrls) ويسمّي كل عنصر url. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:202]

```
203:             if (relaysList.none { it.url == url }) {
```
> شرط: إذا لم يوجد في قائمة المُرحِّلات (relaysList) أي عنصر عنوانه (url) يساوي url. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:203]

```
204:                 relaysList.add(Relay(url))
```
> يضيف إلى قائمة المُرحِّلات (relaysList) كائن مُرحِّل (Relay) منشأ من url. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:204]

```
205:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:205]

```
206:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:206]

```
207:         updateRelaysList()
```
> يستدعي الدالة تحديث قائمة المُرحِّلات (updateRelaysList) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:207]

```
208: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:208]

```
209:         scope.launch {
```
> يطلق كتلة تنفيذ غير متزامن (launch) داخل النطاق (scope). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:209]

```
210:             relayUrls.forEach { relayUrl ->
```
> يمرّ على كل عنصر في عناوين المُرحِّلات (relayUrls) ويسمّي كل عنصر relayUrl. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:210]

```
211:                 launch {
```
> يطلق كتلة تنفيذ غير متزامن (launch) فرعية. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:211]

```
212:                     if (!connections.containsKey(relayUrl)) {
```
> شرط: إذا لم تحتوِ خريطة الاتصالات (connections) على المفتاح relayUrl. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:212]

```
213:                         connectToRelay(relayUrl)
```
> يستدعي دالة الاتصال بمُرحِّل (connectToRelay) ممرِّراً relayUrl. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:213]

```
214:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:214]

```
215:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:215]

```
216:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:216]

```
217:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:217]

```
218:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:218]

```
219: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:219]

```
220:     init {
```
> يبدأ كتلة التهيئة (init) للصنف. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:220]

```
221:         // Initialize with default relays - avoid static initialization order issues
```
> تعليق: تهيئة بمُرحِّلات افتراضية — تجنّب مشاكل ترتيب التهيئة الساكنة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:221]

```
222:         try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:222]

```
223:             val defaultRelayUrls = listOf(
```
> يعرّف متغيراً ثابتاً اسمه عناوين المُرحِّلات الافتراضية (defaultRelayUrls) بقيمة قائمة (listOf). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:223]

```
224:                 "wss://relay.damus.io",
```
> عنصر نصّي في القائمة قيمته "wss://relay.damus.io". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:224]

```
225:                 "wss://relay.primal.net",
```
> عنصر نصّي في القائمة قيمته "wss://relay.primal.net". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:225]

```
226:                 "wss://offchain.pub",
```
> عنصر نصّي في القائمة قيمته "wss://offchain.pub". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:226]

```
227:                 "wss://nostr21.com"
```
> عنصر نصّي في القائمة قيمته "wss://nostr21.com". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:227]

```
228:             )
```
> إغلاق نطاق استدعاء القائمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:228]

```
229:             relaysList.addAll(defaultRelayUrls.map { Relay(it) })
```
> يضيف إلى قائمة المُرحِّلات (relaysList) كل عناصر defaultRelayUrls بعد تحويل كل عنوان إلى كائن مُرحِّل (Relay). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:229]

```
230:             _relays.value = relaysList.toList()
```
> يضبط قيمة الحقل ‎_relays‎ بنسخة قائمة من relaysList. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:230]

```
231:             updateConnectionStatus()
```
> يستدعي دالة تحديث حالة الاتصال (updateConnectionStatus) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:231]

```
232:             Log.d(TAG, "✅ NostrRelayManager initialized with ${relaysList.size} default relays")
```
> يسجّل رسالة تنقيح (Log.d) بالوسم TAG نصّها أن NostrRelayManager هُيِّئ بعدد relaysList.size من المُرحِّلات الافتراضية. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:232]

```
233:         } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) ويسمّيه e. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:233]

```
234:             Log.e(TAG, "Failed to initialize NostrRelayManager: ${e.message}", e)
```
> يسجّل رسالة خطأ (Log.e) بالوسم TAG نصّها فشل تهيئة NostrRelayManager مع رسالة الاستثناء، ويمرّر الاستثناء e. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:234]

```
235:             // Initialize with empty list as fallback
```
> تعليق: تهيئة بقائمة فارغة كحلٍّ احتياطي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:235]

```
236:             _relays.value = emptyList()
```
> يضبط قيمة الحقل ‎_relays‎ بقائمة فارغة (emptyList). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:236]

```
237:             _isConnected.value = false
```
> يضبط قيمة الحقل ‎_isConnected‎ إلى false. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:237]

```
238:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:238]

```
239:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:239]

```
240:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:240]

```
241:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:241]

```
242:      * Connect to all configured relays
```
> تعليق: الاتصال بكل المُرحِّلات المُهيَّأة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:242]

```
243:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:243]

```
244:     fun connect() {
```
> يعرّف دالة عامة اسمها الاتصال (connect) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:244]

```
245:         Log.d(TAG, "🌐 Connecting to ${relaysList.size} Nostr relays")
```
> يسجّل رسالة تنقيح (Log.d) بالوسم TAG نصّها أنه يتصل بعدد relaysList.size من مُرحِّلات Nostr. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:245]

```
246:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:246]

```
247:         scope.launch {
```
> يطلق كتلة تنفيذ غير متزامن (launch) داخل النطاق (scope). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:247]

```
248:             relaysList.forEach { relay ->
```
> يمرّ على كل عنصر في قائمة المُرحِّلات (relaysList) ويسمّي كل عنصر relay. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:248]

```
249:                 launch {
```
> يطلق كتلة تنفيذ غير متزامن (launch) فرعية. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:249]

```
250:                     connectToRelay(relay.url)
```
> يستدعي دالة الاتصال بمُرحِّل (connectToRelay) ممرِّراً عنوان المُرحِّل relay.url. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:250]

```
251:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:251]

```
252:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:252]

```
253:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:253]

```
254:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:254]

```
255:         // Start periodic subscription validation
```
> تعليق: بدء التحقق الدوري من الاشتراكات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:255]

```
256:         startSubscriptionValidation()
```
> يستدعي دالة بدء التحقق من الاشتراك (startSubscriptionValidation) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:256]

```
257:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:257]

```
258:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:258]

```
259:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:259]

```
260:      * Disconnect from all relays
```
> تعليق: قطع الاتصال عن كل المُرحِّلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:260]

```
261:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:261]

```
262:     fun disconnect() {
```
> يعرّف دالة عامة اسمها قطع الاتصال (disconnect) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:262]

```
263:         Log.d(TAG, "Disconnecting from all relays")
```
> يسجّل رسالة تنقيح (Log.d) بالوسم TAG نصّها قطع الاتصال عن كل المُرحِّلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:263]

```
264:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:264]

```
265:         // Stop subscription validation
```
> تعليق: إيقاف التحقق من الاشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:265]

```
266:         stopSubscriptionValidation()
```
> يستدعي دالة إيقاف التحقق من الاشتراك (stopSubscriptionValidation) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:266]

```
267:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:267]

```
268:         connections.values.forEach { webSocket ->
```
> يمرّ على كل قيم خريطة الاتصالات (connections.values) ويسمّي كل قيمة webSocket. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:268]

```
269:             webSocket.close(1000, "Manual disconnect")
```
> يستدعي إغلاق المقبس (webSocket.close) برمز 1000 وسبب "Manual disconnect". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:269]

```
270:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:270]

```
271:         connections.clear()
```
> يفرّغ خريطة الاتصالات (connections.clear). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:271]

```
272:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:272]

```
273:         // Clear subscriptions
```
> تعليق: تفريغ الاشتراكات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:273]

```
274:         subscriptions.clear()
```
> يفرّغ خريطة الاشتراكات (subscriptions.clear). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:274]

```
275:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:275]

```
276:         updateConnectionStatus()
```
> يستدعي دالة تحديث حالة الاتصال (updateConnectionStatus) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:276]

```
277:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:277]

```
278:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:278]

```
279:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:279]

```
280:      * Send an event to specified relays (or all if none specified)
```
> تعليق: إرسال حدث إلى مُرحِّلات محدَّدة (أو الكل إن لم يُحدَّد شيء). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:280]

```
281:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:281]

```
282:     fun sendEvent(event: NostrEvent, relayUrls: List<String>? = null) {
```
> يعرّف دالة عامة اسمها إرسال حدث (sendEvent) تأخذ حدث Nostr (event من نوع NostrEvent) وقائمة عناوين مُرحِّلات اختيارية (relayUrls) قيمتها الافتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:282]

```
283:         val targetRelays = relayUrls ?: relaysList.map { it.url }
```
> يعرّف متغيراً ثابتاً اسمه المُرحِّلات المستهدفة (targetRelays) قيمته relayUrls إن لم يكن null، وإلا قائمة عناوين relaysList. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:283]

```
284:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:284]

```
285:         // Add to queue for reliability
```
> تعليق: الإضافة إلى الطابور لأجل الموثوقية. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:285]

```
286:         synchronized(messageQueueLock) {
```
> يبدأ كتلة متزامنة (synchronized) على قفل طابور الرسائل (messageQueueLock). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:286]

```
287:             messageQueue.add(Pair(event, targetRelays))
```
> يضيف إلى طابور الرسائل (messageQueue) زوجاً (Pair) من الحدث event والمُرحِّلات المستهدفة targetRelays. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:287]

```
288:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:288]

```
289:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:289]

```
290:         // Attempt immediate send
```
> تعليق: محاولة الإرسال الفوري. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:290]

```
291:         scope.launch {
```
> يطلق كتلة تنفيذ غير متزامن (launch) داخل النطاق (scope). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:291]

```
292:             targetRelays.forEach { relayUrl ->
```
> يمرّ على كل عنصر في المُرحِّلات المستهدفة (targetRelays) ويسمّي كل عنصر relayUrl. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:292]

```
293:                 val webSocket = connections[relayUrl]
```
> يعرّف متغيراً ثابتاً اسمه webSocket قيمته القيمة المقابلة للمفتاح relayUrl في خريطة الاتصالات (connections). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:293]

```
294:                 if (webSocket != null) {
```
> شرط: إذا لم يكن webSocket مساوياً لـ null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:294]

```
295:                     sendToRelay(event, webSocket, relayUrl)
```
> يستدعي دالة الإرسال إلى مُرحِّل (sendToRelay) ممرِّراً الحدث event والمقبس webSocket والعنوان relayUrl. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:295]

```
296:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:296]

```
297:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:297]

```
298:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:298]

```
299:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:299]

```
300:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:300]

```
301:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:301]

```
302:      * Subscribe to events matching a filter
```
> تعليق: الاشتراك في الأحداث المطابقة لمُرشِّح. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:302]

```
303:      * The subscription will be automatically re-established on reconnection
```
> تعليق: سيُعاد إنشاء الاشتراك تلقائياً عند إعادة الاتصال. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:303]

```
304:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:304]

```
305:     fun subscribe(
```
> يعرّف دالة عامة اسمها اشترك (subscribe) وتبدأ قائمة وسائطها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:305]

```
306:         filter: NostrFilter,
```
> وسيط اسمه مُرشِّح (filter) من نوع NostrFilter. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:306]

```
307:         id: String = generateSubscriptionId(),
```
> وسيط اسمه المعرّف (id) من نوع String قيمته الافتراضية ناتج دالة توليد معرّف الاشتراك (generateSubscriptionId). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:307]

```
308:         handler: (NostrEvent) -> Unit,
```
> وسيط اسمه المعالِج (handler) دالة تأخذ NostrEvent وتعيد Unit. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:308]

```
309:         targetRelayUrls: List<String>? = null
```
> وسيط اسمه عناوين المُرحِّلات المستهدفة (targetRelayUrls) قائمة نصوص اختيارية قيمته الافتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:309]

```
310:     ): String {
```
> تُغلق قائمة الوسائط وتُحدِّد نوع الإرجاع String ثم تفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:310]

```
311:         // Store subscription info for persistent tracking
```
> تعليق: تخزين معلومات الاشتراك للتتبّع الدائم. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:311]

```
312:         val subscriptionInfo = SubscriptionInfo(
```
> يعرّف متغيراً ثابتاً اسمه معلومات الاشتراك (subscriptionInfo) منشأ من الباني SubscriptionInfo. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:312]

```
313:             id = id,
```
> يضبط الوسيط المسمّى id بقيمة المتغير id. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:313]

```
314:             filter = filter,
```
> يضبط الوسيط المسمّى filter بقيمة المتغير filter. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:314]

```
315:             handler = handler,
```
> يضبط الوسيط المسمّى handler بقيمة المتغير handler. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:315]

```
316:             targetRelayUrls = targetRelayUrls?.toSet()
```
> يضبط الوسيط المسمّى targetRelayUrls بمجموعة (toSet) من targetRelayUrls إن لم يكن null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:316]

```
317:         )
```
> إغلاق نطاق استدعاء الباني. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:317]

```
318:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:318]

```
319:         activeSubscriptions[id] = subscriptionInfo
```
> يضبط في خريطة الاشتراكات النشطة (activeSubscriptions) القيمة subscriptionInfo عند المفتاح id. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:319]

```
320:         messageHandlers[id] = handler
```
> يضبط في خريطة معالِجات الرسائل (messageHandlers) القيمة handler عند المفتاح id. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:320]

```
321:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:321]

```
322:         Log.d(TAG, "📡 Subscribing to Nostr filter id=$id ${filter.getDebugDescription()}")
```
> يسجّل رسالة تنقيح (Log.d) بالوسم TAG نصّها أنه يشترك في مُرشِّح Nostr بمعرّف id ووصف التنقيح للمُرشِّح من getDebugDescription. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:322]

```
323:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:323]

```
324:         // Send subscription to appropriate relays
```
> تعليق: إرسال الاشتراك إلى المُرحِّلات المناسبة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:324]

```
325:         sendSubscriptionToRelays(subscriptionInfo)
```
> يستدعي دالة إرسال الاشتراك إلى المُرحِّلات (sendSubscriptionToRelays) ممرِّراً subscriptionInfo. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:325]

```
326:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:326]

```
327:         return id
```
> يعيد المعرّف id. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:327]

```
328:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:328]

```
329:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:329]

```
330:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:330]

```
331:      * Send a subscription to the appropriate relays
```
> تعليق: إرسال اشتراك إلى المُرحِّلات المناسبة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:331]

```
332:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:332]

```
333:     private fun sendSubscriptionToRelays(subscriptionInfo: SubscriptionInfo) {
```
> يعرّف دالة خاصة (private) اسمها إرسال الاشتراك إلى المُرحِّلات (sendSubscriptionToRelays) تأخذ معلومات الاشتراك (subscriptionInfo من نوع SubscriptionInfo). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:333]

```
334:         val request = NostrRequest.Subscribe(subscriptionInfo.id, listOf(subscriptionInfo.filter))
```
> يعرّف متغيراً ثابتاً اسمه طلب (request) منشأ من NostrRequest.Subscribe بمعرّف الاشتراك وقائمة فيها مُرشِّح الاشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:334]

```
335:         val message = gson.toJson(request, NostrRequest::class.java)
```
> يعرّف متغيراً ثابتاً اسمه رسالة (message) قيمته تحويل request إلى JSON عبر gson بنوع NostrRequest. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:335]

```
336:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:336]

```
337:         // DEBUG: Log the actual serialized message format
```
> تعليق: تنقيح — سجّل صيغة الرسالة المُسلسَلة الفعلية. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:337]

```
338:         Log.v(TAG, "🔍 DEBUG: Serialized subscription message: $message")
```
> يسجّل رسالة مطوّلة (Log.v) بالوسم TAG نصّها رسالة الاشتراك المُسلسَلة message. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:338]

```
339:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:339]

```
340:         scope.launch {
```
> يطلق كتلة تنفيذ غير متزامن (launch) داخل النطاق (scope). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:340]

```
341:             val targetRelays = subscriptionInfo.targetRelayUrls?.toList() ?: connections.keys.toList()
```
> يعرّف متغيراً ثابتاً اسمه المُرحِّلات المستهدفة (targetRelays) قيمته قائمة من targetRelayUrls إن لم تكن null، وإلا قائمة مفاتيح خريطة الاتصالات (connections.keys). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:341]

```
342:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:342]

```
343:             targetRelays.forEach { relayUrl ->
```
> يمرّ على كل عنصر في المُرحِّلات المستهدفة (targetRelays) ويسمّي كل عنصر relayUrl. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:343]

```
344:                 val webSocket = connections[relayUrl]
```
> يعرّف متغيراً ثابتاً اسمه webSocket قيمته القيمة المقابلة للمفتاح relayUrl في خريطة الاتصالات (connections). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:344]

```
345:                 if (webSocket != null) {
```
> شرط: إذا لم يكن webSocket مساوياً لـ null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:345]

```
346:                     try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:346]

```
347:                         val success = webSocket.send(message)
```
> يعرّف متغيراً ثابتاً اسمه نجاح (success) قيمته ناتج إرسال message عبر webSocket.send. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:347]

```
348:                         if (success) {
```
> شرط: إذا كانت قيمة success صحيحة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:348]

```
349:                             // Track subscription for this relay
```
> تعليق: تتبّع الاشتراك لهذا المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:349]

```
350:                             val currentSubs = subscriptions[relayUrl] ?: emptySet()
```
> يعرّف متغيراً ثابتاً اسمه الاشتراكات الحالية (currentSubs) قيمته قيمة subscriptions عند relayUrl، وإلا مجموعة فارغة (emptySet). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:350]

```
351:                             subscriptions[relayUrl] = currentSubs + subscriptionInfo.id
```
> يضبط في خريطة الاشتراكات (subscriptions) عند المفتاح relayUrl قيمة currentSubs مضافاً إليها معرّف الاشتراك subscriptionInfo.id. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:351]

```
352:                             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:352]

```
353:                             Log.v(TAG, "✅ Subscription '${subscriptionInfo.id}' sent to relay: $relayUrl")
```
> يسجّل رسالة مطوّلة (Log.v) بالوسم TAG نصّها أن الاشتراك بمعرّف subscriptionInfo.id أُرسل إلى المُرحِّل relayUrl. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:353]

```
354:                         } else {
```
> وإلا (else) إن لم تكن success صحيحة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:354]

```
355:                             Log.w(TAG, "❌ Failed to send subscription to $relayUrl: WebSocket send failed")
```
> يسجّل رسالة تحذير (Log.w) بالوسم TAG نصّها فشل إرسال الاشتراك إلى relayUrl لأن إرسال المقبس فشل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:355]

```
356:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:356]

```
357:                     } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) ويسمّيه e. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:357]

```
358:                         Log.e(TAG, "❌ Failed to send subscription to $relayUrl: ${e.message}")
```
> يسجّل رسالة خطأ (Log.e) بالوسم TAG نصّها فشل إرسال الاشتراك إلى relayUrl مع رسالة الاستثناء. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:358]

```
359:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:359]

```
360:                 } else {
```
> وإلا (else) إن كان webSocket مساوياً لـ null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:360]

```
361:                     Log.v(TAG, "⏳ Relay $relayUrl not connected, subscription will be sent on reconnection")
```
> يسجّل رسالة مطوّلة (Log.v) بالوسم TAG نصّها أن المُرحِّل relayUrl غير متصل وأن الاشتراك سيُرسَل عند إعادة الاتصال. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:361]

```
362:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:362]

```
363:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:363]

```
364:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:364]

```
365:             if (connections.isEmpty()) {
```
> شرط: إذا كانت خريطة الاتصالات (connections) فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:365]

```
366:                 Log.w(TAG, "⚠️ No relay connections available for subscription, will retry on reconnection")
```
> يسجّل رسالة تحذير (Log.w) بالوسم TAG نصّها أنه لا توجد اتصالات مُرحِّلات متاحة للاشتراك وسيُعاد المحاولة عند إعادة الاتصال. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:366]

```
367:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:367]

```
368:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:368]

```
369:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:369]

```
370:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:370]

```
371:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:371]

```
372:      * Unsubscribe from a subscription
```
> تعليق: إلغاء الاشتراك من اشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:372]

```
373:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:373]

```
374:     fun unsubscribe(id: String) {
```
> يعرّف دالة عامة اسمها إلغاء الاشتراك (unsubscribe) تأخذ المعرّف (id من نوع String). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:374]

```
375:         // Remove from persistent tracking
```
> تعليق: الإزالة من التتبّع الدائم. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:375]

```
376:         val subscriptionInfo = activeSubscriptions.remove(id)
```
> يعرّف متغيراً ثابتاً اسمه معلومات الاشتراك (subscriptionInfo) قيمته ناتج إزالة المفتاح id من خريطة الاشتراكات النشطة (activeSubscriptions). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:376]

```
377:         messageHandlers.remove(id)
```
> يزيل المفتاح id من خريطة معالِجات الرسائل (messageHandlers). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:377]

```
378:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:378]

```
379:         if (subscriptionInfo == null) {
```
> شرط: إذا كان subscriptionInfo مساوياً لـ null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:379]

```
380:             Log.w(TAG, "⚠️ Attempted to unsubscribe from unknown subscription: $id")
```
> يسجّل رسالة تحذير (Log.w) بالوسم TAG نصّها محاولة إلغاء الاشتراك من اشتراك غير معروف id. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:380]

```
381:             return
```
> يعيد من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:381]

```
382:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:382]

```
383:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:383]

```
384:         Log.d(TAG, "🚫 Unsubscribing from subscription: $id")
```
> يسجّل رسالة تنقيح (Log.d) بالوسم TAG نصّها إلغاء الاشتراك من الاشتراك id. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:384]

```
385:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:385]

```
386:         val request = NostrRequest.Close(id)
```
> يعرّف متغيراً ثابتاً اسمه طلب (request) منشأ من NostrRequest.Close بالمعرّف id. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:386]

```
387:         val message = gson.toJson(request, NostrRequest::class.java)
```
> يعرّف متغيراً ثابتاً اسمه رسالة (message) قيمته تحويل request إلى JSON عبر gson بنوع NostrRequest. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:387]

```
388:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:388]

```
389:         scope.launch {
```
> يطلق كتلة تنفيذ غير متزامن (launch) داخل النطاق (scope). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:389]

```
390:             connections.forEach { (relayUrl, webSocket) ->
```
> يمرّ على كل مدخل في خريطة الاتصالات (connections) ويفكّك كل مدخل إلى relayUrl وwebSocket. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:390]

```
391:                 val currentSubs = subscriptions[relayUrl]
```
> يعرّف متغيراً ثابتاً اسمه الاشتراكات الحالية (currentSubs) قيمته قيمة subscriptions عند relayUrl. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:391]

```
392:                 if (currentSubs?.contains(id) == true) {
```
> شرط: إذا كانت currentSubs غير null وتحتوي على id. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:392]

```
393:                     try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:393]

```
394:                         webSocket.send(message)
```
> يرسل message عبر المقبس webSocket.send. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:394]

```
395:                         subscriptions[relayUrl] = currentSubs - id
```
> يضبط في خريطة الاشتراكات (subscriptions) عند المفتاح relayUrl قيمة currentSubs بعد إزالة id. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:395]

```
396:                         Log.v(TAG, "Unsubscribed '$id' from relay: $relayUrl")
```
> يسجّل رسالة مطوّلة (Log.v) بالوسم TAG نصّها أن الاشتراك id أُلغي من المُرحِّل relayUrl. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:396]

```
397:                     } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) ويسمّيه e. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:397]

```
398:                         Log.e(TAG, "Failed to unsubscribe from $relayUrl: ${e.message}")
```
> يسجّل رسالة خطأ (Log.e) بالوسم TAG نصّها فشل إلغاء الاشتراك من relayUrl مع رسالة الاستثناء. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:398]

```
399:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:399]

```
400:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:400]
