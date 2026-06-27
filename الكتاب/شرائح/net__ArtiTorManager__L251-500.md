# شريحة — app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt (الأسطر 251–500)

```
251:             val proxy = artiProxy ?: run {
```
> يُعرَّف متغيّر ثابت باسم (proxy) ويُسنَد إليه قيمة الحقل (artiProxy)، وإذا كانت القيمة فارغة (null) فيُنفَّذ بلوك (run). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:251]

```
252:                 Log.e(TAG, "ArtiProxy not initialized! This should not happen.")
```
> يُستدعى (Log.e) لتسجيل خطأ بالوسم (TAG) ونص "ArtiProxy not initialized! This should not happen." (وكيل أرتي غير مُهيّأ! هذا يجب ألّا يحدث). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:252]

```
253:                 _statusFlow.update { it.copy(state = TorState.ERROR) }
```
> يُستدعى (update) على تدفّق الحالة (_statusFlow) لينسخ الحالة الراهنة مع ضبط الحقل (state) إلى القيمة (TorState.ERROR). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:253]

```
254:                 return
```
> يُعاد من الدالة بكلمة (return) دون قيمة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:254]

```
255:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:255]

```
256: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:256]

```
257:             proxy.start()
```
> يُستدعى التابع (start) على المتغيّر (proxy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:257]

```
258:             lastLogTime.set(System.currentTimeMillis())
```
> يُستدعى (set) على الحقل وقت آخر سجلّ (lastLogTime) ويُسنَد إليه الوقت الحالي بالميلّي ثانية عبر (System.currentTimeMillis). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:258]

```
259: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:259]

```
260:             _statusFlow.update {
```
> يُستدعى (update) على تدفّق الحالة (_statusFlow) ببلوك لامبدا يبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:260]

```
261:                 it.copy(
```
> يُستدعى (copy) على الحالة الراهنة (it) لإنشاء نسخة مع تعديل حقول تبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:261]

```
262:                     running = true,
```
> يُضبَط الحقل (running) إلى القيمة (true). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:262]

```
263:                     bootstrapPercent = 0,
```
> يُضبَط الحقل نسبة الإقلاع (bootstrapPercent) إلى القيمة (0). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:263]

```
264:                     state = TorState.STARTING
```
> يُضبَط الحقل (state) إلى القيمة (TorState.STARTING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:264]

```
265:                 )
```
> إغلاق قوس استدعاء (copy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:265]

```
266:             }
```
> إغلاق نطاق بلوك (update). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:266]

```
267:             lifecycleState = LifecycleState.RUNNING
```
> يُسنَد إلى حقل حالة دورة الحياة (lifecycleState) القيمة (LifecycleState.RUNNING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:267]

```
268:             startInactivityMonitoring()
```
> يُستدعى التابع بدء مراقبة الخمول (startInactivityMonitoring). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:268]

```
269: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:269]

```
270:         } catch (e: Exception) {
```
> يبدأ بلوك التقاط الاستثناء (catch) بمعامِل (e) من النوع (Exception). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:270]

```
271:             Log.e(TAG, "Error starting Arti on port $currentSocksPort: ${e.message}")
```
> يُستدعى (Log.e) لتسجيل خطأ بالوسم (TAG) ونص "Error starting Arti on port" (خطأ في بدء أرتي على المنفذ) متبوعاً بقيمة المنفذ الراهن (currentSocksPort) ورسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:271]

```
272:             _statusFlow.update { it.copy(state = TorState.ERROR) }
```
> يُستدعى (update) على تدفّق الحالة (_statusFlow) لينسخ الحالة الراهنة مع ضبط الحقل (state) إلى القيمة (TorState.ERROR). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:272]

```
273: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:273]

```
274:             val isBindError = isBindError(e)
```
> يُعرَّف متغيّر ثابت باسم (isBindError) ويُسنَد إليه ناتج استدعاء الدالة (isBindError) مع المعامِل (e). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:274]

```
275:             if (isBindError && bindRetryAttempts < MAX_RETRY_ATTEMPTS) {
```
> شرط (if): إذا كان (isBindError) صحيحاً وكان عدّاد محاولات إعادة الربط (bindRetryAttempts) أصغر من الحد الأقصى للمحاولات (MAX_RETRY_ATTEMPTS). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:275]

```
276:                 bindRetryAttempts++
```
> يُزاد عدّاد محاولات إعادة الربط (bindRetryAttempts) بمقدار واحد. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:276]

```
277:                 currentSocksPort++
```
> يُزاد المنفذ الراهن (currentSocksPort) بمقدار واحد. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:277]

```
278:                 Log.w(
```
> يُستدعى (Log.w) لتسجيل تحذير بوسائط تبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:278]

```
279:                     TAG,
```
> الوسيط الأول هو الوسم (TAG). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:279]

```
280:                     "Port bind failed (attempt $bindRetryAttempts/$MAX_RETRY_ATTEMPTS), retrying with port $currentSocksPort"
```
> الوسيط الثاني نص "Port bind failed (attempt)" (فشل ربط المنفذ، المحاولة) مع قيمة (bindRetryAttempts) من (MAX_RETRY_ATTEMPTS) ثم "retrying with port" (إعادة المحاولة بالمنفذ) مع قيمة (currentSocksPort). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:280]

```
281:                 )
```
> إغلاق قوس استدعاء (Log.w). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:281]

```
282:                 socksAddr = InetSocketAddress("127.0.0.1", currentSocksPort)
```
> يُسنَد إلى حقل عنوان (socksAddr) كائن (InetSocketAddress) بالعنوان "127.0.0.1" والمنفذ (currentSocksPort). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:282]

```
283:                 resetNetworkConnections()
```
> يُستدعى التابع إعادة ضبط اتصالات الشبكة (resetNetworkConnections). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:283]

```
284:                 startArti(application, useDelay = false)
```
> يُستدعى التابع (startArti) بالمعامِل (application) والمعامِل المسمّى (useDelay) بقيمة (false). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:284]

```
285:             } else if (isBindError) {
```
> فرع (else if): وإلّا إذا كان (isBindError) صحيحاً. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:285]

```
286:                 Log.e(TAG, "Max bind retry attempts reached ($MAX_RETRY_ATTEMPTS), giving up")
```
> يُستدعى (Log.e) لتسجيل خطأ بالوسم (TAG) ونص "Max bind retry attempts reached" (بلغ الحد الأقصى لمحاولات إعادة الربط) مع قيمة (MAX_RETRY_ATTEMPTS) ثم "giving up" (الاستسلام). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:286]

```
287:                 lifecycleState = LifecycleState.STOPPED
```
> يُسنَد إلى حقل حالة دورة الحياة (lifecycleState) القيمة (LifecycleState.STOPPED). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:287]

```
288:                 _statusFlow.update {
```
> يُستدعى (update) على تدفّق الحالة (_statusFlow) ببلوك لامبدا يبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:288]

```
289:                     it.copy(
```
> يُستدعى (copy) على الحالة الراهنة (it) لإنشاء نسخة مع تعديل حقول تبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:289]

```
290:                         running = false,
```
> يُضبَط الحقل (running) إلى القيمة (false). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:290]

```
291:                         bootstrapPercent = 0,
```
> يُضبَط الحقل نسبة الإقلاع (bootstrapPercent) إلى القيمة (0). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:291]

```
292:                         state = TorState.ERROR
```
> يُضبَط الحقل (state) إلى القيمة (TorState.ERROR). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:292]

```
293:                     )
```
> إغلاق قوس استدعاء (copy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:293]

```
294:                 }
```
> إغلاق نطاق بلوك (update). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:294]

```
295:             } else {
```
> فرع (else): وإلّا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:295]

```
296:                 scheduleRetry(application)
```
> يُستدعى التابع جدولة إعادة المحاولة (scheduleRetry) بالمعامِل (application). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:296]

```
297:             }
```
> إغلاق نطاق فرع (else). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:297]

```
298:         }
```
> إغلاق نطاق بلوك (catch). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:298]

```
299:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:299]

```
300: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:300]

```
301:     private fun isBindError(exception: Exception): Boolean {
```
> تُعرَّف دالة خاصة (private) باسم خطأ الربط (isBindError) تأخذ معامِلاً (exception) من النوع (Exception) وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:301]

```
302:         val message = exception.message?.lowercase() ?: ""
```
> يُعرَّف متغيّر ثابت (message) يُسنَد إليه رسالة الاستثناء (exception.message) محوّلة إلى أحرف صغيرة (lowercase)، وإذا كانت فارغة (null) فالقيمة سلسلة فارغة "". [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:302]

```
303:         return message.contains("bind") ||
```
> يُعاد ناتج: هل تحتوي (message) على "bind" (ربط)، أو (يستمر الشرط). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:303]

```
304:                 message.contains("address already in use") ||
```
> أو هل تحتوي (message) على "address already in use" (العنوان مستخدَم بالفعل)، أو (يستمر الشرط). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:304]

```
305:                 message.contains("port") && message.contains("use") ||
```
> أو هل تحتوي (message) على "port" (منفذ) وعلى "use" (استخدام)، أو (يستمر الشرط). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:305]

```
306:                 message.contains("permission denied") && message.contains("port") ||
```
> أو هل تحتوي (message) على "permission denied" (رُفض الإذن) وعلى "port" (منفذ)، أو (يستمر الشرط). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:306]

```
307:                 message.contains("could not bind")
```
> أو هل تحتوي (message) على "could not bind" (تعذّر الربط). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:307]

```
308:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:308]

```
309: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:309]

```
310:     /**
```
> تعليق توثيق (KDoc) يبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:310]

```
311:      * Reset network connections after Tor state changes.
```
> تعليق: إعادة ضبط اتصالات الشبكة بعد تغيّر حالة تور. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:311]

```
312:      * Rebuilds OkHttp clients and reconnects Nostr relays.
```
> تعليق: يُعيد بناء عملاء (OkHttp) ويُعيد الاتصال بمرحّلات (Nostr). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:312]

```
313:      */
```
> إغلاق تعليق التوثيق. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:313]

```
314:     private fun resetNetworkConnections() {
```
> تُعرَّف دالة خاصة (private) باسم إعادة ضبط اتصالات الشبكة (resetNetworkConnections) دون معاملات. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:314]

```
315:         try {
```
> يبدأ بلوك (try). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:315]

```
316:             OkHttpProvider.reset()
```
> يُستدعى التابع (reset) على المزوّد (OkHttpProvider). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:316]

```
317:         } catch (_: Throwable) {
```
> يبدأ بلوك التقاط (catch) باستثناء غير مُسمّى (_) من النوع (Throwable). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:317]

```
318:         }
```
> إغلاق نطاق بلوك (catch) فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:318]

```
319:         try {
```
> يبدأ بلوك (try) آخر. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:319]

```
320:             com.bitchat.android.nostr.NostrRelayManager.shared.resetAllConnections()
```
> يُستدعى التابع إعادة ضبط كل الاتصالات (resetAllConnections) على المثيل المشترك (shared) من مدير مرحّلات نوستر (com.bitchat.android.nostr.NostrRelayManager). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:320]

```
321:         } catch (_: Throwable) {
```
> يبدأ بلوك التقاط (catch) باستثناء غير مُسمّى (_) من النوع (Throwable). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:321]

```
322:         }
```
> إغلاق نطاق بلوك (catch) فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:322]

```
323:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:323]

```
324: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:324]

```
325:     private fun stopArtiInternal() {
```
> تُعرَّف دالة خاصة (private) باسم إيقاف أرتي الداخلي (stopArtiInternal) دون معاملات. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:325]

```
326:         try {
```
> يبدأ بلوك (try). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:326]

```
327:             val proxy = artiProxy
```
> يُعرَّف متغيّر ثابت (proxy) ويُسنَد إليه قيمة الحقل (artiProxy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:327]

```
328:             if (proxy != null) {
```
> شرط (if): إذا لم يكن (proxy) فارغاً (null). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:328]

```
329:                 Log.i(TAG, "Stopping Arti…")
```
> يُستدعى (Log.i) لتسجيل معلومة بالوسم (TAG) ونص "Stopping Arti…" (جارٍ إيقاف أرتي…). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:329]

```
330:                 try {
```
> يبدأ بلوك (try) داخلي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:330]

```
331:                     proxy.stop()
```
> يُستدعى التابع (stop) على المتغيّر (proxy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:331]

```
332:                 } catch (_: Throwable) {
```
> يبدأ بلوك التقاط (catch) باستثناء غير مُسمّى (_) من النوع (Throwable). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:332]

```
333:                 }
```
> إغلاق نطاق بلوك (catch) فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:333]

```
334:             }
```
> إغلاق نطاق شرط (if). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:334]

```
335:             stopInactivityMonitoring()
```
> يُستدعى التابع إيقاف مراقبة الخمول (stopInactivityMonitoring). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:335]

```
336:             stopRetryMonitoring()
```
> يُستدعى التابع إيقاف مراقبة إعادة المحاولة (stopRetryMonitoring). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:336]

```
337:         } catch (e: Exception) {
```
> يبدأ بلوك التقاط (catch) بمعامِل (e) من النوع (Exception). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:337]

```
338:             Log.w(TAG, "Error stopping Arti: ${e.message}")
```
> يُستدعى (Log.w) لتسجيل تحذير بالوسم (TAG) ونص "Error stopping Arti" (خطأ في إيقاف أرتي) مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:338]

```
339:         }
```
> إغلاق نطاق بلوك (catch). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:339]

```
340:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:340]

```
341: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:341]

```
342:     private fun stopArti() {
```
> تُعرَّف دالة خاصة (private) باسم إيقاف أرتي (stopArti) دون معاملات. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:342]

```
343:         stopArtiInternal()
```
> يُستدعى التابع إيقاف أرتي الداخلي (stopArtiInternal). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:343]

```
344:         socksAddr = null
```
> يُسنَد إلى حقل العنوان (socksAddr) القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:344]

```
345:         _statusFlow.value = _statusFlow.value.copy(
```
> يُسنَد إلى قيمة تدفّق الحالة (_statusFlow.value) نسخة من قيمته الراهنة عبر (copy) مع تعديل حقول تبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:345]

```
346:             running = false,
```
> يُضبَط الحقل (running) إلى القيمة (false). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:346]

```
347:             bootstrapPercent = 0,
```
> يُضبَط الحقل نسبة الإقلاع (bootstrapPercent) إلى القيمة (0). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:347]

```
348:             state = TorState.STOPPING
```
> يُضبَط الحقل (state) إلى القيمة (TorState.STOPPING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:348]

```
349:         )
```
> إغلاق قوس استدعاء (copy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:349]

```
350:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:350]

```
351: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:351]

```
352:     private suspend fun stopArtiAndWait(timeoutMs: Long = STOP_TIMEOUT_MS) {
```
> تُعرَّف دالة خاصة معلّقة (suspend) باسم إيقاف أرتي والانتظار (stopArtiAndWait) تأخذ معامِلاً (timeoutMs) من النوع (Long) بقيمة افتراضية (STOP_TIMEOUT_MS). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:352]

```
353:         stopArtiInternal()
```
> يُستدعى التابع إيقاف أرتي الداخلي (stopArtiInternal). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:353]

```
354:         waitForStateTransition(target = TorState.OFF, timeoutMs = timeoutMs)
```
> يُستدعى التابع انتظار انتقال الحالة (waitForStateTransition) بالمعامِل المسمّى (target) بقيمة (TorState.OFF) والمعامِل (timeoutMs) بقيمة (timeoutMs). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:354]

```
355:         delay(200)
```
> يُستدعى (delay) للتأخير 200 ميلّي ثانية. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:355]

```
356:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:356]

```
357: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:357]

```
358:     private suspend fun restartArti(application: Application) {
```
> تُعرَّف دالة خاصة معلّقة (suspend) باسم إعادة تشغيل أرتي (restartArti) تأخذ معامِلاً (application) من النوع (Application). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:358]

```
359:         Log.i(TAG, "Restarting Arti (keeping SOCKS proxy enabled)...")
```
> يُستدعى (Log.i) لتسجيل معلومة بالوسم (TAG) ونص "Restarting Arti (keeping SOCKS proxy enabled)..." (إعادة تشغيل أرتي مع إبقاء وكيل SOCKS مُفعَّلاً...). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:359]

```
360:         stopArtiAndWait()
```
> يُستدعى التابع إيقاف أرتي والانتظار (stopArtiAndWait). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:360]

```
361:         delay(RESTART_DELAY_MS)
```
> يُستدعى (delay) للتأخير بمقدار ثابت تأخير إعادة التشغيل (RESTART_DELAY_MS). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:361]

```
362:         startArti(application, useDelay = false)
```
> يُستدعى التابع (startArti) بالمعامِل (application) والمعامِل المسمّى (useDelay) بقيمة (false). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:362]

```
363:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:363]

```
364: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:364]

```
365:     private fun startInactivityMonitoring() {
```
> تُعرَّف دالة خاصة (private) باسم بدء مراقبة الخمول (startInactivityMonitoring) دون معاملات. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:365]

```
366:         inactivityJob?.cancel()
```
> يُستدعى (cancel) على مهمّة الخمول (inactivityJob) إن لم تكن فارغة (null). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:366]

```
367:         inactivityJob = appScope.launch {
```
> يُسنَد إلى مهمّة الخمول (inactivityJob) ناتج إطلاق كوروتين عبر (appScope.launch) ببلوك يبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:367]

```
368:             while (true) {
```
> تبدأ حلقة (while) بشرط دائم (true). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:368]

```
369:                 delay(INACTIVITY_TIMEOUT_MS)
```
> يُستدعى (delay) للتأخير بمقدار ثابت مهلة الخمول (INACTIVITY_TIMEOUT_MS). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:369]

```
370:                 val currentTime = System.currentTimeMillis()
```
> يُعرَّف متغيّر ثابت الوقت الحالي (currentTime) ويُسنَد إليه الوقت الحالي بالميلّي ثانية عبر (System.currentTimeMillis). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:370]

```
371:                 val lastActivity = lastLogTime.get()
```
> يُعرَّف متغيّر ثابت آخر نشاط (lastActivity) ويُسنَد إليه ناتج (get) على حقل وقت آخر سجلّ (lastLogTime). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:371]

```
372:                 val timeSinceLastActivity = currentTime - lastActivity
```
> يُعرَّف متغيّر ثابت الزمن منذ آخر نشاط (timeSinceLastActivity) ويُسنَد إليه الفرق (currentTime) ناقص (lastActivity). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:372]

```
373: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:373]

```
374:                 if (timeSinceLastActivity > INACTIVITY_TIMEOUT_MS) {
```
> شرط (if): إذا كان (timeSinceLastActivity) أكبر من ثابت مهلة الخمول (INACTIVITY_TIMEOUT_MS). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:374]

```
375:                     val currentMode = _statusFlow.value.mode
```
> يُعرَّف متغيّر ثابت الوضع الراهن (currentMode) ويُسنَد إليه الحقل (mode) من قيمة تدفّق الحالة (_statusFlow.value). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:375]

```
376:                     if (currentMode == TorMode.ON) {
```
> شرط (if): إذا كان (currentMode) يساوي (TorMode.ON). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:376]

```
377:                         val bootstrapPercent = _statusFlow.value.bootstrapPercent
```
> يُعرَّف متغيّر ثابت نسبة الإقلاع (bootstrapPercent) ويُسنَد إليه الحقل (bootstrapPercent) من قيمة تدفّق الحالة (_statusFlow.value). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:377]

```
378:                         if (bootstrapPercent < 100) {
```
> شرط (if): إذا كانت (bootstrapPercent) أصغر من 100. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:378]

```
379:                             Log.w(
```
> يُستدعى (Log.w) لتسجيل تحذير بوسائط تبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:379]

```
380:                                 TAG,
```
> الوسيط الأول هو الوسم (TAG). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:380]

```
381:                                 "Inactivity detected (${timeSinceLastActivity}ms), restarting Arti"
```
> الوسيط الثاني نص "Inactivity detected" (رُصد خمول) مع قيمة (timeSinceLastActivity) ووحدة "ms" ثم "restarting Arti" (إعادة تشغيل أرتي). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:381]

```
382:                             )
```
> إغلاق قوس استدعاء (Log.w). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:382]

```
383:                             currentApplication?.let { app ->
```
> يُستدعى (let) على حقل التطبيق الراهن (currentApplication) إن لم يكن فارغاً، بمعامِل (app) في بلوك يبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:383]

```
384:                                 appScope.launch {
```
> يُطلَق كوروتين عبر (appScope.launch) ببلوك يبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:384]

```
385:                                     restartArti(app)
```
> يُستدعى التابع إعادة تشغيل أرتي (restartArti) بالمعامِل (app). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:385]

```
386:                                 }
```
> إغلاق نطاق بلوك (launch). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:386]

```
387:                             }
```
> إغلاق نطاق بلوك (let). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:387]

```
388:                             break
```
> يُكسَر الخروج من الحلقة بكلمة (break). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:388]

```
389:                         }
```
> إغلاق نطاق شرط (bootstrapPercent < 100). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:389]

```
390:                     }
```
> إغلاق نطاق شرط (currentMode == TorMode.ON). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:390]

```
391:                 }
```
> إغلاق نطاق شرط (timeSinceLastActivity). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:391]

```
392:             }
```
> إغلاق نطاق حلقة (while). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:392]

```
393:         }
```
> إغلاق نطاق بلوك (launch). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:393]

```
394:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:394]

```
395: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:395]

```
396:     private fun stopInactivityMonitoring() {
```
> تُعرَّف دالة خاصة (private) باسم إيقاف مراقبة الخمول (stopInactivityMonitoring) دون معاملات. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:396]

```
397:         inactivityJob?.cancel()
```
> يُستدعى (cancel) على مهمّة الخمول (inactivityJob) إن لم تكن فارغة (null). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:397]

```
398:         inactivityJob = null
```
> يُسنَد إلى مهمّة الخمول (inactivityJob) القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:398]

```
399:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:399]

```
400: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:400]

```
401:     private fun scheduleRetry(application: Application) {
```
> تُعرَّف دالة خاصة (private) باسم جدولة إعادة المحاولة (scheduleRetry) تأخذ معامِلاً (application) من النوع (Application). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:401]

```
402:         retryJob?.cancel()
```
> يُستدعى (cancel) على مهمّة إعادة المحاولة (retryJob) إن لم تكن فارغة (null). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:402]

```
403:         if (retryAttempts < MAX_RETRY_ATTEMPTS) {
```
> شرط (if): إذا كان عدّاد محاولات إعادة المحاولة (retryAttempts) أصغر من الحد الأقصى للمحاولات (MAX_RETRY_ATTEMPTS). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:403]

```
404:             retryAttempts++
```
> يُزاد عدّاد محاولات إعادة المحاولة (retryAttempts) بمقدار واحد. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:404]

```
405:             val delayMs = (1000L * (1 shl retryAttempts)).coerceAtMost(30000L)
```
> يُعرَّف متغيّر ثابت زمن التأخير (delayMs) يُسنَد إليه حاصل ضرب (1000L) في (1 مُزاحاً يساراً بمقدار retryAttempts عبر shl)، محدوداً بحد أقصى (coerceAtMost) قدره (30000L). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:405]

```
406:             Log.w(TAG, "Scheduling Arti retry attempt $retryAttempts in ${delayMs}ms")
```
> يُستدعى (Log.w) لتسجيل تحذير بالوسم (TAG) ونص "Scheduling Arti retry attempt" (جدولة محاولة إعادة أرتي) مع قيمة (retryAttempts) ثم "in" مع قيمة (delayMs) ووحدة "ms". [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:406]

```
407:             retryJob = appScope.launch {
```
> يُسنَد إلى مهمّة إعادة المحاولة (retryJob) ناتج إطلاق كوروتين عبر (appScope.launch) ببلوك يبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:407]

```
408:                 delay(delayMs)
```
> يُستدعى (delay) للتأخير بمقدار (delayMs). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:408]

```
409:                 val currentMode = _statusFlow.value.mode
```
> يُعرَّف متغيّر ثابت الوضع الراهن (currentMode) ويُسنَد إليه الحقل (mode) من قيمة تدفّق الحالة (_statusFlow.value). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:409]

```
410:                 if (currentMode == TorMode.ON) {
```
> شرط (if): إذا كان (currentMode) يساوي (TorMode.ON). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:410]

```
411:                     Log.i(TAG, "Retrying Arti start (attempt $retryAttempts)")
```
> يُستدعى (Log.i) لتسجيل معلومة بالوسم (TAG) ونص "Retrying Arti start (attempt)" (إعادة محاولة بدء أرتي، المحاولة) مع قيمة (retryAttempts). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:411]

```
412:                     restartArti(application)
```
> يُستدعى التابع إعادة تشغيل أرتي (restartArti) بالمعامِل (application). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:412]

```
413:                 }
```
> إغلاق نطاق شرط (currentMode == TorMode.ON). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:413]

```
414:             }
```
> إغلاق نطاق بلوك (launch). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:414]

```
415:         } else {
```
> فرع (else): وإلّا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:415]

```
416:             Log.e(TAG, "Max retry attempts reached, giving up on Arti connection")
```
> يُستدعى (Log.e) لتسجيل خطأ بالوسم (TAG) ونص "Max retry attempts reached, giving up on Arti connection" (بلغ الحد الأقصى لمحاولات إعادة المحاولة، الاستسلام عن اتصال أرتي). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:416]

```
417:         }
```
> إغلاق نطاق فرع (else). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:417]

```
418:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:418]

```
419: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:419]

```
420:     private fun stopRetryMonitoring() {
```
> تُعرَّف دالة خاصة (private) باسم إيقاف مراقبة إعادة المحاولة (stopRetryMonitoring) دون معاملات. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:420]

```
421:         retryJob?.cancel()
```
> يُستدعى (cancel) على مهمّة إعادة المحاولة (retryJob) إن لم تكن فارغة (null). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:421]

```
422:         retryJob = null
```
> يُسنَد إلى مهمّة إعادة المحاولة (retryJob) القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:422]

```
423:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:423]

```
424: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:424]

```
425:     private suspend fun waitUntilBootstrapped() {
```
> تُعرَّف دالة خاصة معلّقة (suspend) باسم انتظر حتى الإقلاع (waitUntilBootstrapped) دون معاملات. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:425]

```
426:         val current = _statusFlow.value
```
> يُعرَّف متغيّر ثابت (current) ويُسنَد إليه قيمة تدفّق الحالة (_statusFlow.value). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:426]

```
427:         if (!current.running) return
```
> شرط (if): إذا لم يكن حقل (running) في (current) صحيحاً فيُعاد من الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:427]

```
428:         if (current.bootstrapPercent >= 100 && current.state == TorState.RUNNING) return
```
> شرط (if): إذا كانت (current.bootstrapPercent) أكبر من أو تساوي 100 وكانت (current.state) تساوي (TorState.RUNNING) فيُعاد من الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:428]

```
429:         while (true) {
```
> تبدأ حلقة (while) بشرط دائم (true). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:429]

```
430:             val s = statusFlow.first {
```
> يُعرَّف متغيّر ثابت (s) ويُسنَد إليه أول قيمة (first) من تدفّق الحالة (statusFlow) تحقّق الشرط في البلوك الذي يبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:430]

```
431:                 (it.bootstrapPercent >= 100 && it.state == TorState.RUNNING) ||
```
> شرط البلوك: إمّا أن تكون (it.bootstrapPercent) أكبر من أو تساوي 100 وتكون (it.state) تساوي (TorState.RUNNING)، أو (يستمر الشرط). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:431]

```
432:                         !it.running ||
```
> أو ألّا يكون (it.running) صحيحاً، أو (يستمر الشرط). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:432]

```
433:                         it.state == TorState.ERROR
```
> أو أن تكون (it.state) تساوي (TorState.ERROR). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:433]

```
434:             }
```
> إغلاق نطاق بلوك (first). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:434]

```
435:             if (!s.running || s.state == TorState.ERROR) return
```
> شرط (if): إذا لم يكن (s.running) صحيحاً أو كانت (s.state) تساوي (TorState.ERROR) فيُعاد من الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:435]

```
436:             if (s.bootstrapPercent >= 100 && s.state == TorState.RUNNING) return
```
> شرط (if): إذا كانت (s.bootstrapPercent) أكبر من أو تساوي 100 وكانت (s.state) تساوي (TorState.RUNNING) فيُعاد من الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:436]

```
437:         }
```
> إغلاق نطاق حلقة (while). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:437]

```
438:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:438]

```
439: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:439]

```
440:     private fun handleArtiLogLine(s: String) {
```
> تُعرَّف دالة خاصة (private) باسم معالجة سطر سجلّ أرتي (handleArtiLogLine) تأخذ معامِلاً (s) من النوع (String). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:440]

```
441:         val currentState = _statusFlow.value.state
```
> يُعرَّف متغيّر ثابت الحالة الراهنة (currentState) ويُسنَد إليه الحقل (state) من قيمة تدفّق الحالة (_statusFlow.value). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:441]

```
442:         val currentLifecycle = lifecycleState
```
> يُعرَّف متغيّر ثابت دورة الحياة الراهنة (currentLifecycle) ويُسنَد إليه قيمة حقل (lifecycleState). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:442]

```
443: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:443]

```
444:         when {
```
> يبدأ تعبير (when) دون موضوع، بفروع شرطية تبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:444]

```
445:             s.contains("AMEx: state changed to Initialized", ignoreCase = true) -> {
```
> فرع (when): إذا احتوى (s) على "AMEx: state changed to Initialized" (تغيّرت الحالة إلى مُهيّأة) مع تجاهل حالة الأحرف (ignoreCase = true). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:445]

```
446:                 if (currentLifecycle != LifecycleState.STARTING && currentLifecycle != LifecycleState.RUNNING) {
```
> شرط (if): إذا كانت (currentLifecycle) لا تساوي (LifecycleState.STARTING) ولا تساوي (LifecycleState.RUNNING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:446]

```
447:                     Log.w(TAG, "Ignoring stale 'Initialized' log (lifecycle: $currentLifecycle)")
```
> يُستدعى (Log.w) لتسجيل تحذير بالوسم (TAG) ونص "Ignoring stale 'Initialized' log (lifecycle:)" (تجاهل سجلّ 'مُهيّأة' القديم، دورة الحياة) مع قيمة (currentLifecycle). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:447]

```
448:                     return
```
> يُعاد من الدالة بكلمة (return). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:448]

```
449:                 }
```
> إغلاق نطاق شرط (if). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:449]

```
450:                 _statusFlow.update { it.copy(state = TorState.STARTING) }
```
> يُستدعى (update) على تدفّق الحالة (_statusFlow) لينسخ الحالة الراهنة مع ضبط الحقل (state) إلى القيمة (TorState.STARTING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:450]

```
451:                 completeWaitersIf(TorState.STARTING)
```
> يُستدعى التابع إكمال المنتظِرين عند (completeWaitersIf) بالمعامِل (TorState.STARTING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:451]

```
452:             }
```
> إغلاق نطاق فرع (when). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:452]

```
453: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:453]

```
454:             s.contains("AMEx: state changed to Starting", ignoreCase = true) -> {
```
> فرع (when): إذا احتوى (s) على "AMEx: state changed to Starting" (تغيّرت الحالة إلى جارٍ البدء) مع تجاهل حالة الأحرف (ignoreCase = true). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:454]

```
455:                 if (currentLifecycle != LifecycleState.STARTING && currentLifecycle != LifecycleState.RUNNING) {
```
> شرط (if): إذا كانت (currentLifecycle) لا تساوي (LifecycleState.STARTING) ولا تساوي (LifecycleState.RUNNING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:455]

```
456:                     Log.w(TAG, "Ignoring stale 'Starting' log (lifecycle: $currentLifecycle)")
```
> يُستدعى (Log.w) لتسجيل تحذير بالوسم (TAG) ونص "Ignoring stale 'Starting' log (lifecycle:)" (تجاهل سجلّ 'جارٍ البدء' القديم، دورة الحياة) مع قيمة (currentLifecycle). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:456]

```
457:                     return
```
> يُعاد من الدالة بكلمة (return). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:457]

```
458:                 }
```
> إغلاق نطاق شرط (if). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:458]

```
459:                 _statusFlow.update { it.copy(state = TorState.STARTING) }
```
> يُستدعى (update) على تدفّق الحالة (_statusFlow) لينسخ الحالة الراهنة مع ضبط الحقل (state) إلى القيمة (TorState.STARTING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:459]

```
460:                 completeWaitersIf(TorState.STARTING)
```
> يُستدعى التابع إكمال المنتظِرين عند (completeWaitersIf) بالمعامِل (TorState.STARTING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:460]

```
461:             }
```
> إغلاق نطاق فرع (when). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:461]

```
462: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:462]

```
463:             s.contains(
```
> فرع (when): يُستدعى (s.contains) بوسائط تبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:463]

```
464:                 "Sufficiently bootstrapped; system SOCKS now functional",
```
> الوسيط الأول نص "Sufficiently bootstrapped; system SOCKS now functional" (تم الإقلاع بقدرٍ كافٍ؛ نظام SOCKS يعمل الآن). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:464]

```
465:                 ignoreCase = true
```
> الوسيط المسمّى (ignoreCase) بقيمة (true). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:465]

```
466:             ) -> {
```
> إغلاق قوس (contains) وبداية نطاق فرع (when). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:466]

```
467:                 if (currentLifecycle != LifecycleState.RUNNING) {
```
> شرط (if): إذا كانت (currentLifecycle) لا تساوي (LifecycleState.RUNNING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:467]

```
468:                     Log.w(TAG, "Ignoring bootstrap log (lifecycle: $currentLifecycle)")
```
> يُستدعى (Log.w) لتسجيل تحذير بالوسم (TAG) ونص "Ignoring bootstrap log (lifecycle:)" (تجاهل سجلّ الإقلاع، دورة الحياة) مع قيمة (currentLifecycle). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:468]

```
469:                     return
```
> يُعاد من الدالة بكلمة (return). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:469]

```
470:                 }
```
> إغلاق نطاق شرط (if). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:470]

```
471:                 _statusFlow.update {
```
> يُستدعى (update) على تدفّق الحالة (_statusFlow) ببلوك لامبدا يبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:471]

```
472:                     it.copy(
```
> يُستدعى (copy) على الحالة الراهنة (it) لإنشاء نسخة مع تعديل حقول تبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:472]

```
473:                         bootstrapPercent = 75,
```
> يُضبَط الحقل نسبة الإقلاع (bootstrapPercent) إلى القيمة (75). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:473]

```
474:                         state = TorState.BOOTSTRAPPING
```
> يُضبَط الحقل (state) إلى القيمة (TorState.BOOTSTRAPPING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:474]

```
475:                     )
```
> إغلاق قوس استدعاء (copy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:475]

```
476:                 }
```
> إغلاق نطاق بلوك (update). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:476]

```
477:                 retryAttempts = 0
```
> يُسنَد إلى عدّاد محاولات إعادة المحاولة (retryAttempts) القيمة (0). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:477]

```
478:                 bindRetryAttempts = 0
```
> يُسنَد إلى عدّاد محاولات إعادة الربط (bindRetryAttempts) القيمة (0). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:478]

```
479:                 startInactivityMonitoring()
```
> يُستدعى التابع بدء مراقبة الخمول (startInactivityMonitoring). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:479]

```
480:             }
```
> إغلاق نطاق فرع (when). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:480]

```
481: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:481]

```
482:             s.contains("We have found that guard [scrubbed] is usable.", ignoreCase = true) -> {
```
> فرع (when): إذا احتوى (s) على "We have found that guard [scrubbed] is usable." (وجدنا أن الحارس [مُنقّى] قابل للاستخدام.) مع تجاهل حالة الأحرف (ignoreCase = true). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:482]

```
483:                 if (currentLifecycle != LifecycleState.RUNNING) {
```
> شرط (if): إذا كانت (currentLifecycle) لا تساوي (LifecycleState.RUNNING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:483]

```
484:                     Log.w(TAG, "Ignoring guard discovery log (lifecycle: $currentLifecycle)")
```
> يُستدعى (Log.w) لتسجيل تحذير بالوسم (TAG) ونص "Ignoring guard discovery log (lifecycle:)" (تجاهل سجلّ اكتشاف الحارس، دورة الحياة) مع قيمة (currentLifecycle). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:484]

```
485:                     return
```
> يُعاد من الدالة بكلمة (return). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:485]

```
486:                 }
```
> إغلاق نطاق شرط (if). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:486]

```
487:                 _statusFlow.update {
```
> يُستدعى (update) على تدفّق الحالة (_statusFlow) ببلوك لامبدا يبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:487]

```
488:                     it.copy(
```
> يُستدعى (copy) على الحالة الراهنة (it) لإنشاء نسخة مع تعديل حقول تبدأ هنا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:488]

```
489:                         state = TorState.RUNNING,
```
> يُضبَط الحقل (state) إلى القيمة (TorState.RUNNING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:489]

```
490:                         bootstrapPercent = 100,
```
> يُضبَط الحقل نسبة الإقلاع (bootstrapPercent) إلى القيمة (100). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:490]

```
491:                         running = true
```
> يُضبَط الحقل (running) إلى القيمة (true). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:491]

```
492:                     )
```
> إغلاق قوس استدعاء (copy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:492]

```
493:                 }
```
> إغلاق نطاق بلوك (update). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:493]

```
494:                 completeWaitersIf(TorState.RUNNING)
```
> يُستدعى التابع إكمال المنتظِرين عند (completeWaitersIf) بالمعامِل (TorState.RUNNING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:494]

```
495:             }
```
> إغلاق نطاق فرع (when). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:495]

```
496: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:496]

```
497:             s.contains("AMEx: state changed to Stopping", ignoreCase = true) -> {
```
> فرع (when): إذا احتوى (s) على "AMEx: state changed to Stopping" (تغيّرت الحالة إلى جارٍ الإيقاف) مع تجاهل حالة الأحرف (ignoreCase = true). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:497]

```
498:                 if (currentLifecycle != LifecycleState.STOPPING) {
```
> شرط (if): إذا كانت (currentLifecycle) لا تساوي (LifecycleState.STOPPING). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:498]

```
499:                     Log.w(TAG, "Ignoring stale 'Stopping' log (lifecycle: $currentLifecycle)")
```
> يُستدعى (Log.w) لتسجيل تحذير بالوسم (TAG) ونص "Ignoring stale 'Stopping' log (lifecycle:)" (تجاهل سجلّ 'جارٍ الإيقاف' القديم، دورة الحياة) مع قيمة (currentLifecycle). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:499]

```
500:                     return
```
> يُعاد من الدالة بكلمة (return) (السطر مقطوع عند نهاية المدى). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:500]
