# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseSession.kt (الأسطر 251–500)

```
251:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:251]

```
252:             // LOGGING: Track Android handshake initialization (matching iOS) 
```
> تعليق: تسجيل: تتبّع تهيئة مصافحة أندرويد (مطابق لـ iOS). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:252]

```
253:             Log.d(TAG, "=== ANDROID NOISE SESSION - BEFORE HANDSHAKE INIT ===")
```
> يستدعي تسجيل التصحيح (Log.d) بالوسم TAG ونصّاً ثابتاً يقول «جلسة Noise أندرويد - قبل تهيئة المصافحة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:253]

```
254:             Log.d(TAG, "Creating NoiseHandshakeState for peer: $peerID")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ يقول «إنشاء حالة مصافحة Noise للنظير» متبوعاً بقيمة معرّف النظير (peerID). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:254]

```
255:             Log.d(TAG, "Role: ${if (role == HandshakeState.INITIATOR) "INITIATOR" else "RESPONDER"}")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «Role:» متبوعاً بتعبير شرطي: إن كان الدور (role) يساوي HandshakeState.INITIATOR يطبع «INITIATOR» وإلا «RESPONDER». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:255]

```
256:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:256]

```
257:             handshakeState = HandshakeState(PROTOCOL_NAME, role)
```
> يُسند إلى حالة المصافحة (handshakeState) كائناً جديداً من HandshakeState مُنشأً باسم البروتوكول (PROTOCOL_NAME) والدور (role). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:257]

```
258:             Log.d(TAG, "HandshakeState created successfully")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ ثابت «أُنشئت HandshakeState بنجاح». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:258]

```
259:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:259]

```
260:             Log.d(TAG, "=== ANDROID NOISE SESSION - AFTER HANDSHAKE INIT ===")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ ثابت يقول «جلسة Noise أندرويد - بعد تهيئة المصافحة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:260]

```
261:             Log.d(TAG, "NoiseHandshakeState created and mixPreMessageKeys() completed")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ ثابت يقول «أُنشئت حالة مصافحة Noise واكتمل mixPreMessageKeys()». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:261]

```
262:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:262]

```
263:             if (handshakeState?.needsLocalKeyPair() == true) {
```
> يبدأ شرطاً: إذا كان استدعاء needsLocalKeyPair() على حالة المصافحة (مع استدعاء آمن) يساوي true. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:263]

```
264:                 Log.d(TAG, "Local static key pair is required for XX pattern")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ ثابت يقول «زوج المفاتيح الثابت المحلي مطلوب لنمط XX». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:264]

```
265:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:265]

```
266:                 val localKeyPair = handshakeState?.getLocalKeyPair()
```
> يُعرّف متغيراً ثابتاً باسم زوج المفاتيح المحلي (localKeyPair) ويُسند إليه نتيجة استدعاء getLocalKeyPair() على حالة المصافحة (مع استدعاء آمن). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:266]

```
267:                 if (localKeyPair != null) {
```
> يبدأ شرطاً: إذا كان زوج المفاتيح المحلي (localKeyPair) لا يساوي null. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:267]

```
268:                     // FIXED: Use the provided persistent identity keys with our local fork
```
> تعليق: مُصلَح: استخدم مفاتيح الهوية الدائمة المُعطاة مع نسختنا المحلية المتفرّعة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:268]

```
269:                     // Our local fork properly supports setting pre-existing keys
```
> تعليق: نسختنا المحلية المتفرّعة تدعم بشكل صحيح ضبط مفاتيح موجودة مسبقاً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:269]

```
270:                     Log.d(TAG, "Setting persistent static identity keys...")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ ثابت يقول «جارٍ ضبط مفاتيح الهوية الثابتة الدائمة...». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:270]

```
271:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:271]

```
272:                     localKeyPair.setPrivateKey(localStaticPrivateKey, 0)
```
> يستدعي setPrivateKey على زوج المفاتيح المحلي (localKeyPair) ممرّراً المفتاح الخاص الثابت المحلي (localStaticPrivateKey) والإزاحة 0. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:272]

```
273:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:273]

```
274:                     if (!localKeyPair.hasPrivateKey() || !localKeyPair.hasPublicKey()) {
```
> يبدأ شرطاً: إذا كان نفي hasPrivateKey() أو نفي hasPublicKey() على زوج المفاتيح المحلي (أي يفتقد المفتاح الخاص أو العام). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:274]

```
275:                         throw IllegalStateException("Failed to set static identity keys - local fork issue")
```
> يرمي استثناء حالة غير قانونية (IllegalStateException) بنصّ «فشل ضبط مفاتيح الهوية الثابتة - مشكلة في النسخة المتفرّعة المحلية». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:275]

```
276:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:276]

```
277:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:277]

```
278:                     Log.d(TAG, "✓ Successfully set persistent static identity keys")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ ثابت يقول «✓ ضُبطت مفاتيح الهوية الثابتة الدائمة بنجاح». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:278]

```
279:                     Log.d(TAG, "Algorithm: ${localKeyPair.dhName}")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «Algorithm:» متبوعاً بقيمة dhName لزوج المفاتيح المحلي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:279]

```
280:                     Log.d(TAG, "Private key length: ${localKeyPair.privateKeyLength}")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «Private key length:» متبوعاً بقيمة privateKeyLength لزوج المفاتيح المحلي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:280]

```
281:                     Log.d(TAG, "Public key length: ${localKeyPair.publicKeyLength}")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «Public key length:» متبوعاً بقيمة publicKeyLength لزوج المفاتيح المحلي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:281]

```
282:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:282]

```
283:                     // Verify the keys were set correctly
```
> تعليق: تحقّق من ضبط المفاتيح بشكل صحيح. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:283]

```
284:                     val verifyPrivate = ByteArray(32)
```
> يُعرّف متغيراً ثابتاً باسم تحقّق-خاص (verifyPrivate) ويُسند إليه مصفوفة بايتات (ByteArray) بطول 32. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:284]

```
285:                     val verifyPublic = ByteArray(32)
```
> يُعرّف متغيراً ثابتاً باسم تحقّق-عام (verifyPublic) ويُسند إليه مصفوفة بايتات (ByteArray) بطول 32. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:285]

```
286:                     localKeyPair.getPrivateKey(verifyPrivate, 0)
```
> يستدعي getPrivateKey على زوج المفاتيح المحلي ممرّراً المصفوفة verifyPrivate والإزاحة 0. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:286]

```
287:                     localKeyPair.getPublicKey(verifyPublic, 0)
```
> يستدعي getPublicKey على زوج المفاتيح المحلي ممرّراً المصفوفة verifyPublic والإزاحة 0. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:287]

```
288:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:288]

```
289:                     Log.d(TAG, "Persistent identity public key: ${localStaticPublicKey.joinToString("") { "%02x".format(it) }}")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «Persistent identity public key:» متبوعاً بالمفتاح العام الثابت المحلي (localStaticPublicKey) محوّلاً إلى سلسلة ست عشرية بدمج كل بايت بالصيغة «%02x». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:289]

```
290:                     Log.d(TAG, "Set public key:               ${verifyPublic.joinToString("") { "%02x".format(it) }}")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «Set public key:» متبوعاً بالمصفوفة verifyPublic محوّلة إلى سلسلة ست عشرية بدمج كل بايت بالصيغة «%02x». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:290]

```
291:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:291]

```
292:                 } else {
```
> يبدأ فرع وإلا (else) للشرط السابق على localKeyPair، مع إغلاق نطاق الفرع السابق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:292]

```
293:                     throw IllegalStateException("HandshakeState returned null for local key pair")
```
> يرمي استثناء حالة غير قانونية (IllegalStateException) بنصّ «أرجعت HandshakeState قيمة null لزوج المفاتيح المحلي». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:293]

```
294:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:294]

```
295:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:295]

```
296:             } else {
```
> يبدأ فرع وإلا (else) للشرط على needsLocalKeyPair()، مع إغلاق نطاق الفرع السابق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:296]

```
297:                 Log.d(TAG, "Local static key pair not needed for this handshake pattern/role")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ ثابت يقول «زوج المفاتيح الثابت المحلي غير مطلوب لنمط/دور هذه المصافحة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:297]

```
298:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:298]

```
299:             handshakeState?.start()
```
> يستدعي start() على حالة المصافحة (مع استدعاء آمن). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:299]

```
300:             Log.d(TAG, "Handshake state started successfully with persistent identity keys")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ ثابت يقول «بدأت حالة المصافحة بنجاح بمفاتيح الهوية الدائمة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:300]

```
301:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:301]

```
302:         } catch (e: Exception) {
```
> يبدأ فرع التقاط (catch) لاستثناء من نوع Exception باسم المتغير e، مع إغلاق نطاق كتلة try. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:302]

```
303:             Log.e(TAG, "Exception during handshake initialization: ${e.message}", e)
```
> يستدعي تسجيل الخطأ (Log.e) بنصّ «استثناء أثناء تهيئة المصافحة:» متبوعاً برسالة الاستثناء (e.message) ويمرّر الاستثناء e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:303]

```
304:             throw e
```
> يعيد رمي الاستثناء e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:304]

```
305:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:305]

```
306:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:306]

```
307:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:307]

```
308: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:308]

```
309: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:309]

```
310:     // MARK: - Real Handshake Implementation
```
> تعليق: علامة: التنفيذ الحقيقي للمصافحة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:310]

```
311:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:311]

```
312:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:312]

```
313:      * Start handshake as INITIATOR
```
> تعليق: ابدأ المصافحة بصفة بادئ (INITIATOR). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:313]

```
314:      * Returns e, the first handshake message for XX pattern (32 bytes)
```
> تعليق: يُرجع e، وهي رسالة المصافحة الأولى لنمط XX (32 بايت). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:314]

```
315:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:315]

```
316:     @Synchronized
```
> يضع التعليق التوضيحي @Synchronized (تزامُن) على الدالة التالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:316]

```
317:     fun startHandshake(): ByteArray {
```
> يُعرّف دالة باسم بدء-المصافحة (startHandshake) لا تأخذ وسائط وتُرجع مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:317]

```
318:         Log.d(TAG, "Starting noise XX handshake with $peerID as INITIATOR")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «بدء مصافحة Noise XX مع» متبوعاً بمعرّف النظير (peerID) وعبارة «بصفة بادئ». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:318]

```
319:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:319]

```
320:         if (!isInitiator) {
```
> يبدأ شرطاً: إذا كان نفي علم البادئ (isInitiator) أي ليس بادئاً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:320]

```
321:             throw IllegalStateException("Only initiator can start handshake")
```
> يرمي استثناء حالة غير قانونية (IllegalStateException) بنصّ «البادئ وحده يمكنه بدء المصافحة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:321]

```
322:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:322]

```
323:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:323]

```
324:         if (state != NoiseSessionState.Uninitialized) {
```
> يبدأ شرطاً: إذا كانت الحالة (state) لا تساوي NoiseSessionState.Uninitialized (غير مهيّأة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:324]

```
325:             throw IllegalStateException("Handshake already started")
```
> يرمي استثناء حالة غير قانونية (IllegalStateException) بنصّ «المصافحة بدأت بالفعل». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:325]

```
326:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:326]

```
327:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:327]

```
328:         try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:328]

```
329:             // Initialize handshake as initiator 
```
> تعليق: هيّئ المصافحة بصفة بادئ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:329]

```
330:             initializeNoiseHandshake(HandshakeState.INITIATOR)
```
> يستدعي دالة تهيئة مصافحة Noise (initializeNoiseHandshake) ممرّراً الثابت HandshakeState.INITIATOR. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:330]

```
331:             state = NoiseSessionState.Handshaking
```
> يُسند إلى الحالة (state) القيمة NoiseSessionState.Handshaking (قيد المصافحة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:331]

```
332:             if (handshakeStartMs == null) {
```
> يبدأ شرطاً: إذا كان وقت بدء المصافحة بالمللي ثانية (handshakeStartMs) يساوي null. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:332]

```
333:                 handshakeStartMs = System.currentTimeMillis()
```
> يُسند إلى وقت بدء المصافحة (handshakeStartMs) الوقت الحالي بالمللي ثانية من System.currentTimeMillis(). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:333]

```
334:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:334]

```
335:             lastHandshakeActivityMs = System.currentTimeMillis()
```
> يُسند إلى وقت آخر نشاط مصافحة بالمللي ثانية (lastHandshakeActivityMs) الوقت الحالي من System.currentTimeMillis(). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:335]

```
336:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:336]

```
337:             val messageBuffer = ByteArray(XX_MESSAGE_1_SIZE)
```
> يُعرّف متغيراً ثابتاً باسم مخزن-الرسالة (messageBuffer) ويُسند إليه مصفوفة بايتات بطول الثابت XX_MESSAGE_1_SIZE (حجم رسالة XX الأولى). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:337]

```
338:             val handshakeStateLocal = handshakeState ?: throw IllegalStateException("Handshake state is null")
```
> يُعرّف متغيراً ثابتاً باسم حالة-المصافحة-المحلية (handshakeStateLocal) ويُسند إليه حالة المصافحة، وإن كانت null يرمي استثناء حالة غير قانونية بنصّ «حالة المصافحة هي null». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:338]

```
339:             val messageLength = handshakeStateLocal.writeMessage(messageBuffer, 0, null, 0, 0)
```
> يُعرّف متغيراً ثابتاً باسم طول-الرسالة (messageLength) ويُسند إليه نتيجة writeMessage على حالة المصافحة المحلية ممرّراً مخزن الرسالة والإزاحة 0 ومدخلاً فارغاً null وإزاحة 0 وطولاً 0. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:339]

```
340:             currentPattern++
```
> يزيد العدّاد النمطي الحالي (currentPattern) بمقدار واحد. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:340]

```
341:             val firstMessage = messageBuffer.copyOf(messageLength)
```
> يُعرّف متغيراً ثابتاً باسم الرسالة-الأولى (firstMessage) ويُسند إليه نسخة من مخزن الرسالة بطول طول-الرسالة (messageLength). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:341]

```
342:             handshakeMessage1 = firstMessage
```
> يُسند إلى رسالة-المصافحة-١ (handshakeMessage1) قيمة الرسالة الأولى (firstMessage). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:342]

```
343:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:343]

```
344:             // Validate message size matches XX pattern expectations
```
> تعليق: تحقّق من مطابقة حجم الرسالة لتوقّعات نمط XX. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:344]

```
345:             if (firstMessage.size != XX_MESSAGE_1_SIZE) {
```
> يبدأ شرطاً: إذا كان حجم الرسالة الأولى (firstMessage.size) لا يساوي الثابت XX_MESSAGE_1_SIZE. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:345]

```
346:                 Log.w(TAG, "Warning: XX message 1 size ${firstMessage.size} != expected $XX_MESSAGE_1_SIZE")
```
> يستدعي تسجيل التحذير (Log.w) بنصّ «تحذير: حجم رسالة XX الأولى» متبوعاً بحجم الرسالة الأولى وعبارة «!= المتوقع» وقيمة XX_MESSAGE_1_SIZE. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:346]

```
347:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:347]

```
348:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:348]

```
349:             val ePrefix = firstMessage.take(4).toByteArray().toHexString()
```
> يُعرّف متغيراً ثابتاً باسم بادئة-e (ePrefix) ويُسند إليه أوّل 4 بايتات من الرسالة الأولى محوّلة إلى مصفوفة بايتات ثم إلى سلسلة ست عشرية عبر toHexString(). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:349]

```
350:             Log.d(TAG, "Sending XX handshake message 1 to $peerID (${firstMessage.size} bytes) e_prefix=$ePrefix currentPattern: $currentPattern")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «إرسال رسالة مصافحة XX الأولى إلى» متبوعاً بمعرّف النظير وحجم الرسالة الأولى وبادئة e (ePrefix) وقيمة العدّاد النمطي الحالي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:350]

```
351:             return firstMessage
```
> يُرجع الرسالة الأولى (firstMessage). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:351]

```
352:         } catch (e: Exception) {
```
> يبدأ فرع التقاط (catch) لاستثناء من نوع Exception باسم e، مع إغلاق نطاق كتلة try. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:352]

```
353:             state = NoiseSessionState.Failed(e)
```
> يُسند إلى الحالة (state) القيمة NoiseSessionState.Failed مُنشأة بالاستثناء e (فشل). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:353]

```
354:             Log.e(TAG, "Failed to start handshake: ${e.message}")
```
> يستدعي تسجيل الخطأ (Log.e) بنصّ «فشل بدء المصافحة:» متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:354]

```
355:             throw e
```
> يعيد رمي الاستثناء e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:355]

```
356:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:356]

```
357:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:357]

```
358:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:358]

```
359:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:359]

```
360:      * Process incoming handshake as RESPONDER
```
> تعليق: عالِج المصافحة الواردة بصفة مُجيب (RESPONDER). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:360]

```
361:      * Returns e, ee
```
> تعليق: يُرجع e، ee. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:361]

```
362:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:362]

```
363:     @Synchronized
```
> يضع التعليق التوضيحي @Synchronized (تزامُن) على الدالة التالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:363]

```
364:     fun processHandshakeMessage(message: ByteArray): ByteArray? {
```
> يُعرّف دالة باسم معالجة-رسالة-المصافحة (processHandshakeMessage) تأخذ وسيطاً message من نوع مصفوفة بايتات وتُرجع مصفوفة بايتات قابلة لأن تكون null. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:364]

```
365:         val inputPrefix = message.take(4).toByteArray().toHexString()
```
> يُعرّف متغيراً ثابتاً باسم بادئة-الإدخال (inputPrefix) ويُسند إليه أوّل 4 بايتات من الرسالة (message) محوّلة إلى مصفوفة بايتات ثم إلى سلسلة ست عشرية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:365]

```
366:         Log.d(TAG, "Processing handshake message from $peerID (${message.size} bytes) prefix=$inputPrefix")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «معالجة رسالة مصافحة من» متبوعاً بمعرّف النظير وحجم الرسالة وبادئة الإدخال (inputPrefix). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:366]

```
367:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:367]

```
368:         try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:368]

```
369:             // Initialize as responder if receiving first message
```
> تعليق: هيّئ بصفة مُجيب إذا كان يُستقبَل أوّل رسالة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:369]

```
370:             if (state == NoiseSessionState.Uninitialized && !isInitiator) {
```
> يبدأ شرطاً: إذا كانت الحالة تساوي NoiseSessionState.Uninitialized ولم يكن العقدة بادئاً (نفي isInitiator). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:370]

```
371:                 initializeNoiseHandshake(HandshakeState.RESPONDER)
```
> يستدعي دالة تهيئة مصافحة Noise (initializeNoiseHandshake) ممرّراً الثابت HandshakeState.RESPONDER. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:371]

```
372:                 state = NoiseSessionState.Handshaking
```
> يُسند إلى الحالة (state) القيمة NoiseSessionState.Handshaking (قيد المصافحة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:372]

```
373:                 if (handshakeStartMs == null) {
```
> يبدأ شرطاً: إذا كان وقت بدء المصافحة (handshakeStartMs) يساوي null. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:373]

```
374:                     handshakeStartMs = System.currentTimeMillis()
```
> يُسند إلى وقت بدء المصافحة (handshakeStartMs) الوقت الحالي بالمللي ثانية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:374]

```
375:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:375]

```
376:                 Log.d(TAG, "Initialized as RESPONDER for XX handshake with $peerID")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «تمت التهيئة بصفة مُجيب لمصافحة XX مع» متبوعاً بمعرّف النظير. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:376]

```
377:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:377]

```
378:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:378]

```
379:             if (state != NoiseSessionState.Handshaking) {
```
> يبدأ شرطاً: إذا كانت الحالة (state) لا تساوي NoiseSessionState.Handshaking. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:379]

```
380:                 throw IllegalStateException("Invalid state for handshake: $state")
```
> يرمي استثناء حالة غير قانونية (IllegalStateException) بنصّ «حالة غير صالحة للمصافحة:» متبوعاً بقيمة الحالة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:380]

```
381:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:381]

```
382:             lastHandshakeActivityMs = System.currentTimeMillis()
```
> يُسند إلى وقت آخر نشاط مصافحة (lastHandshakeActivityMs) الوقت الحالي بالمللي ثانية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:382]

```
383:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:383]

```
384:             val handshakeStateLocal = handshakeState ?: throw IllegalStateException("Handshake state is null")
```
> يُعرّف متغيراً ثابتاً باسم حالة-المصافحة-المحلية (handshakeStateLocal) ويُسند إليه حالة المصافحة، وإن كانت null يرمي استثناء حالة غير قانونية بنصّ «حالة المصافحة هي null». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:384]

```
385:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:385]

```
386:             // Let the Noise library validate message sizes and handle the flow
```
> تعليق: دع مكتبة Noise تتحقّق من أحجام الرسائل وتُدير التدفّق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:386]

```
387:             val payloadBuffer = ByteArray(XX_MESSAGE_2_SIZE + MAX_PAYLOAD_SIZE)  // Buffer for any payload data
```
> يُعرّف متغيراً ثابتاً باسم مخزن-الحمولة (payloadBuffer) ويُسند إليه مصفوفة بايتات بطول مجموع الثابتين XX_MESSAGE_2_SIZE وMAX_PAYLOAD_SIZE، مع تعليق: مخزن لأي بيانات حمولة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:387]

```
388:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:388]

```
389:             // Read the incoming message - the Noise library will handle validation
```
> تعليق: اقرأ الرسالة الواردة - مكتبة Noise ستتولّى التحقّق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:389]

```
390:             val payloadLength = handshakeStateLocal.readMessage(message, 0, message.size, payloadBuffer, 0)
```
> يُعرّف متغيراً ثابتاً باسم طول-الحمولة (payloadLength) ويُسند إليه نتيجة readMessage على حالة المصافحة المحلية ممرّراً الرسالة والإزاحة 0 وحجم الرسالة ومخزن الحمولة والإزاحة 0. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:390]

```
391:             currentPattern++
```
> يزيد العدّاد النمطي الحالي (currentPattern) بمقدار واحد. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:391]

```
392:             val readPrefix = message.take(4).toByteArray().toHexString()
```
> يُعرّف متغيراً ثابتاً باسم بادئة-القراءة (readPrefix) ويُسند إليه أوّل 4 بايتات من الرسالة محوّلة إلى مصفوفة بايتات ثم إلى سلسلة ست عشرية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:392]

```
393:             Log.d(TAG, "Read handshake message, payload length: $payloadLength prefix=$readPrefix currentPattern: $currentPattern")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «قُرئت رسالة المصافحة، طول الحمولة:» متبوعاً بطول الحمولة وبادئة القراءة وقيمة العدّاد النمطي الحالي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:393]

```
394:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:394]

```
395:             // Check what action the handshake state wants us to take next
```
> تعليق: تحقّق من الإجراء الذي تريد حالة المصافحة منّا اتخاذه تالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:395]

```
396:             val action = handshakeStateLocal.getAction()
```
> يُعرّف متغيراً ثابتاً باسم الإجراء (action) ويُسند إليه نتيجة getAction() على حالة المصافحة المحلية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:396]

```
397:             Log.d(TAG, "Handshake action after processing message: $action")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «إجراء المصافحة بعد معالجة الرسالة:» متبوعاً بقيمة الإجراء (action). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:397]

```
398:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:398]

```
399:             return when (action) {
```
> يُرجع نتيجة تعبير when (تطابُق) يفحص قيمة الإجراء (action). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:399]

```
400:                 HandshakeState.WRITE_MESSAGE -> {
```
> يبدأ فرع when للحالة HandshakeState.WRITE_MESSAGE (كتابة رسالة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:400]

```
401:                     // Noise library says we need to send a response
```
> تعليق: مكتبة Noise تقول إننا بحاجة إلى إرسال ردّ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:401]

```
402:                     val responseBuffer = ByteArray(XX_MESSAGE_2_SIZE + MAX_PAYLOAD_SIZE) // Large buffer for any response
```
> يُعرّف متغيراً ثابتاً باسم مخزن-الردّ (responseBuffer) ويُسند إليه مصفوفة بايتات بطول مجموع XX_MESSAGE_2_SIZE وMAX_PAYLOAD_SIZE، مع تعليق: مخزن كبير لأي ردّ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:402]

```
403:                     val responseLength = handshakeStateLocal.writeMessage(responseBuffer, 0, null, 0, 0)
```
> يُعرّف متغيراً ثابتاً باسم طول-الردّ (responseLength) ويُسند إليه نتيجة writeMessage على حالة المصافحة المحلية ممرّراً مخزن الردّ والإزاحة 0 ومدخلاً فارغاً null وإزاحة 0 وطولاً 0. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:403]

```
404:                     currentPattern++
```
> يزيد العدّاد النمطي الحالي (currentPattern) بمقدار واحد. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:404]

```
405:                     val response = responseBuffer.copyOf(responseLength)
```
> يُعرّف متغيراً ثابتاً باسم الردّ (response) ويُسند إليه نسخة من مخزن الردّ بطول طول-الردّ (responseLength). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:405]

```
406:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:406]

```
407:                     Log.d(TAG, "Generated handshake response: ${response.size} bytes, action still: ${handshakeStateLocal.getAction()} currentPattern: $currentPattern")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «وُلّد ردّ المصافحة:» متبوعاً بحجم الردّ وعبارة «الإجراء لا يزال:» وقيمة getAction() على حالة المصافحة المحلية وقيمة العدّاد النمطي الحالي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:407]

```
408:                     completeHandshake()
```
> يستدعي دالة إكمال-المصافحة (completeHandshake). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:408]

```
409:                     response
```
> القيمة المُرجَعة لهذا الفرع هي الردّ (response). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:409]

```
410:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:410]

```
411:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:411]

```
412:                 HandshakeState.SPLIT -> {
```
> يبدأ فرع when للحالة HandshakeState.SPLIT (انقسام/تقسيم). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:412]

```
413:                     // Handshake complete, split into transport keys
```
> تعليق: المصافحة مكتملة، انقسام إلى مفاتيح النقل. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:413]

```
414:                     completeHandshake()
```
> يستدعي دالة إكمال-المصافحة (completeHandshake). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:414]

```
415:                     Log.d(TAG, "SPLIT ✅ XX handshake completed with $peerID")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «SPLIT ✅ اكتملت مصافحة XX مع» متبوعاً بمعرّف النظير. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:415]

```
416:                     null
```
> القيمة المُرجَعة لهذا الفرع هي null. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:416]

```
417:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:417]

```
418:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:418]

```
419:                 HandshakeState.FAILED -> {
```
> يبدأ فرع when للحالة HandshakeState.FAILED (فشل). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:419]

```
420:                     throw Exception("Handshake failed - Noise library reported FAILED state")
```
> يرمي استثناء عام (Exception) بنصّ «فشلت المصافحة - أبلغت مكتبة Noise عن حالة فشل». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:420]

```
421:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:421]

```
422:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:422]

```
423:                 HandshakeState.READ_MESSAGE -> {
```
> يبدأ فرع when للحالة HandshakeState.READ_MESSAGE (قراءة رسالة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:423]

```
424:                     // Noise library expects us to read another message
```
> تعليق: مكتبة Noise تتوقّع منّا قراءة رسالة أخرى. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:424]

```
425:                     Log.d(TAG, "Handshake waiting for next message from $peerID")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «المصافحة تنتظر الرسالة التالية من» متبوعاً بمعرّف النظير. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:425]

```
426:                     null
```
> القيمة المُرجَعة لهذا الفرع هي null. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:426]

```
427:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:427]

```
428:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:428]

```
429:                 else -> {
```
> يبدأ الفرع الافتراضي (else) لتعبير when. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:429]

```
430:                     Log.d(TAG, "Handshake action: $action - no immediate action needed")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «إجراء المصافحة:» متبوعاً بقيمة الإجراء وعبارة «- لا حاجة لإجراء فوري». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:430]

```
431:                     null
```
> القيمة المُرجَعة لهذا الفرع هي null. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:431]

```
432:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:432]

```
433:             }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:433]

```
434:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:434]

```
435:         } catch (e: Exception) {
```
> يبدأ فرع التقاط (catch) لاستثناء من نوع Exception باسم e، مع إغلاق نطاق كتلة try. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:435]

```
436:             state = NoiseSessionState.Failed(e)
```
> يُسند إلى الحالة (state) القيمة NoiseSessionState.Failed مُنشأة بالاستثناء e (فشل). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:436]

```
437:             Log.e(TAG, "Handshake failed with $peerID: ${e.message}", e)
```
> يستدعي تسجيل الخطأ (Log.e) بنصّ «فشلت المصافحة مع» متبوعاً بمعرّف النظير ورسالة الاستثناء (e.message) ويمرّر الاستثناء e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:437]

```
438:             throw e
```
> يعيد رمي الاستثناء e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:438]

```
439:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:439]

```
440:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:440]

```
441:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:441]

```
442:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:442]

```
443:      * Complete handshake and derive transport keys
```
> تعليق: أكمِل المصافحة واشتقّ مفاتيح النقل. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:443]

```
444:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:444]

```
445:     @Synchronized
```
> يضع التعليق التوضيحي @Synchronized (تزامُن) على الدالة التالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:445]

```
446:     private fun completeHandshake() {
```
> يُعرّف دالة خاصّة (private) باسم إكمال-المصافحة (completeHandshake) لا تأخذ وسائط ولا تُرجع قيمة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:446]

```
447:         if (currentPattern < NOISE_XX_PATTERN_LENGTH) {
```
> يبدأ شرطاً: إذا كان العدّاد النمطي الحالي (currentPattern) أصغر من الثابت NOISE_XX_PATTERN_LENGTH (طول نمط XX). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:447]

```
448:             return
```
> يُرجع (خروج مبكر من الدالة) دون قيمة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:448]

```
449:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:449]

```
450:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:450]

```
451:         Log.d(TAG, "Completing XX handshake with $peerID")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «إكمال مصافحة XX مع» متبوعاً بمعرّف النظير. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:451]

```
452:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:452]

```
453:         try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:453]

```
454:             // Split handshake state into transport ciphers
```
> تعليق: قسّم حالة المصافحة إلى شفرات النقل (transport ciphers). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:454]

```
455:             val cipherPair = handshakeState?.split()
```
> يُعرّف متغيراً ثابتاً باسم زوج-الشفرات (cipherPair) ويُسند إليه نتيجة split() على حالة المصافحة (مع استدعاء آمن). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:455]

```
456:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:456]

```
457:             sendCipher = cipherPair?.getSender()
```
> يُسند إلى شفرة-الإرسال (sendCipher) نتيجة getSender() على زوج الشفرات (مع استدعاء آمن). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:457]

```
458:             receiveCipher = cipherPair?.getReceiver()
```
> يُسند إلى شفرة-الاستقبال (receiveCipher) نتيجة getReceiver() على زوج الشفرات (مع استدعاء آمن). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:458]

```
459:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:459]

```
460:             // Extract remote static key if available
```
> تعليق: استخرِج المفتاح الثابت البعيد إذا كان متاحاً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:460]

```
461:             if (handshakeState?.hasRemotePublicKey() == true) {
```
> يبدأ شرطاً: إذا كان استدعاء hasRemotePublicKey() على حالة المصافحة (مع استدعاء آمن) يساوي true. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:461]

```
462:                 val remoteDH = handshakeState?.getRemotePublicKey()
```
> يُعرّف متغيراً ثابتاً باسم ديفي-هيلمان-البعيد (remoteDH) ويُسند إليه نتيجة getRemotePublicKey() على حالة المصافحة (مع استدعاء آمن). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:462]

```
463:                 if (remoteDH != null) {
```
> يبدأ شرطاً: إذا كان remoteDH لا يساوي null. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:463]

```
464:                     remoteStaticPublicKey = ByteArray(32)
```
> يُسند إلى المفتاح العام الثابت البعيد (remoteStaticPublicKey) مصفوفة بايتات جديدة بطول 32. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:464]

```
465:                     remoteDH.getPublicKey(remoteStaticPublicKey!!, 0)
```
> يستدعي getPublicKey على remoteDH ممرّراً المفتاح العام الثابت البعيد (مع تأكيد عدم العدمية !!) والإزاحة 0. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:465]

```
466:                     Log.d(TAG, "Remote static public key: ${remoteStaticPublicKey!!.joinToString("") { "%02x".format(it) }}")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «المفتاح العام الثابت البعيد:» متبوعاً بالمفتاح (مع تأكيد عدم العدمية) محوّلاً إلى سلسلة ست عشرية بالصيغة «%02x» لكل بايت. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:466]

```
467:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:467]

```
468:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:468]

```
469:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:469]

```
470:             // Extract handshake hash for channel binding
```
> تعليق: استخرِج بصمة المصافحة (handshake hash) لربط القناة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:470]

```
471:             handshakeHash = handshakeState?.getHandshakeHash()
```
> يُسند إلى بصمة-المصافحة (handshakeHash) نتيجة getHandshakeHash() على حالة المصافحة (مع استدعاء آمن). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:471]

```
472:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:472]

```
473:             // Clean up handshake state
```
> تعليق: نظّف حالة المصافحة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:473]

```
474:             handshakeState?.destroy()
```
> يستدعي destroy() على حالة المصافحة (مع استدعاء آمن). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:474]

```
475:             handshakeState = null
```
> يُسند إلى حالة المصافحة (handshakeState) القيمة null. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:475]

```
476:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:476]

```
477:             messagesSent = 0
```
> يُسند إلى عدّاد الرسائل المُرسَلة (messagesSent) القيمة 0. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:477]

```
478:             messagesReceived = 0
```
> يُسند إلى عدّاد الرسائل المُستقبَلة (messagesReceived) القيمة 0. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:478]

```
479:             currentPattern = 0
```
> يُسند إلى العدّاد النمطي الحالي (currentPattern) القيمة 0. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:479]

```
480:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:480]

```
481:             // Reset sliding window replay protection for new transport phase
```
> تعليق: أعِد ضبط حماية إعادة التشغيل بنافذة منزلقة (sliding window replay protection) لطور النقل الجديد. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:481]

```
482:             highestReceivedNonce = 0L
```
> يُسند إلى أعلى رقم عشوائي مُستقبَل (highestReceivedNonce) القيمة 0L من نوع Long. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:482]

```
483:             replayWindow = ByteArray(REPLAY_WINDOW_BYTES)
```
> يُسند إلى نافذة-إعادة-التشغيل (replayWindow) مصفوفة بايتات جديدة بطول الثابت REPLAY_WINDOW_BYTES. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:483]

```
484:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:484]

```
485:             state = NoiseSessionState.Established
```
> يُسند إلى الحالة (state) القيمة NoiseSessionState.Established (مُؤسَّسة/قائمة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:485]

```
486:             Log.d(TAG, "Handshake completed with $peerID as isInitiator: $isInitiator - transport keys derived")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «اكتملت المصافحة مع» متبوعاً بمعرّف النظير وعبارة «بصفة isInitiator:» وقيمة علم البادئ وعبارة «- اشتُقّت مفاتيح النقل». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:486]

```
487:             Log.d(TAG, "✅ XX handshake completed with $peerID")
```
> يستدعي تسجيل التصحيح (Log.d) بنصّ «✅ اكتملت مصافحة XX مع» متبوعاً بمعرّف النظير. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:487]

```
488:         } catch (e: Exception) {
```
> يبدأ فرع التقاط (catch) لاستثناء من نوع Exception باسم e، مع إغلاق نطاق كتلة try. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:488]

```
489:             state = NoiseSessionState.Failed(e)
```
> يُسند إلى الحالة (state) القيمة NoiseSessionState.Failed مُنشأة بالاستثناء e (فشل). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:489]

```
490:             Log.e(TAG, "Failed to complete handshake: ${e.message}")
```
> يستدعي تسجيل الخطأ (Log.e) بنصّ «فشل إكمال المصافحة:» متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:490]

```
491:             throw e
```
> يعيد رمي الاستثناء e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:491]

```
492:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:492]

```
493:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:493]

```
494:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:494]

```
495:     // MARK: - Transport Encryption
```
> تعليق: علامة: تشفير النقل (Transport Encryption). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:495]

```
496:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:496]

```
497:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:497]

```
498:      * Encrypt data in transport mode using real ChaCha20-Poly1305 with nonce synchronization
```
> تعليق: شفّر البيانات في وضع النقل باستخدام ChaCha20-Poly1305 الحقيقي مع مزامنة الرقم العشوائي (nonce). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:498]

```
499:      * Returns: <nonce><ciphertext> where nonce is 4 bytes (matching iOS implementation)
```
> تعليق: يُرجع: <nonce><ciphertext> حيث الرقم العشوائي (nonce) 4 بايتات (مطابق لتطبيق iOS). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:499]

```
500:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:500]
