# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseSession.kt (الأسطر 501–750)

```
501:     fun encrypt(data: ByteArray): ByteArray {
```
> تُعرَّف دالة باسم «تشفير» (encrypt) تأخذ مُعاملاً اسمه «بيانات» (data) من نوع مصفوفة بايتات (ByteArray) وتُعيد مصفوفة بايتات. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:501]

```
502:         // Pre-check state without holding cipher lock
```
> تعليق: فحص مسبق للحالة دون الإمساك بقفل المُشفِّر. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:502]

```
503:         if (!isEstablished()) {
```
> شرط: إذا لم تُعِد دالة «مُثبَّتة» (isEstablished) قيمة صحيحة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:503]

```
504:             throw IllegalStateException("Session not established")
```
> تُرمى استثناء حالة غير قانونية (IllegalStateException) برسالة «الجلسة غير مُثبَّتة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:504]

```
505:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:505]

```
506:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:506]

```
507:         // Critical section: Use dedicated cipher lock to protect CipherState nonce corruption
```
> تعليق: قسم حرج: استعمل قفل المُشفِّر المخصص لحماية حالة المُشفِّر من تلف القيمة المرة الواحدة (nonce). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:507]

```
508:         synchronized(cipherLock) {
```
> كتلة متزامنة (synchronized) على الكائن «قفل المُشفِّر» (cipherLock). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:508]

```
509:             // Double-check state inside lock
```
> تعليق: فحص مزدوج للحالة داخل القفل. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:509]

```
510:             if (!isEstablished()) {
```
> شرط: إذا لم تُعِد دالة «مُثبَّتة» قيمة صحيحة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:510]

```
511:                 throw IllegalStateException("Session not established during cipher operation")
```
> تُرمى استثناء حالة غير قانونية برسالة «الجلسة غير مُثبَّتة أثناء عملية التشفير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:511]

```
512:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:512]

```
513:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:513]

```
514:             if (sendCipher == null) {
```
> شرط: إذا كان «مُشفِّر الإرسال» (sendCipher) يساوي قيمة خالية (null). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:514]

```
515:                 throw IllegalStateException("Send cipher not available")
```
> تُرمى استثناء حالة غير قانونية برسالة «مُشفِّر الإرسال غير متاح». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:515]

```
516:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:516]

```
517:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:517]

```
518:             // Check if nonce exceeds 4-byte limit (UInt32 max value)
```
> تعليق: تحقّق إن كانت القيمة المرة الواحدة (nonce) تتجاوز حد الأربعة بايتات (قيمة UInt32 القصوى). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:518]

```
519:             if (messagesSent > UInt.MAX_VALUE.toLong() - 1) {
```
> شرط: إذا كان «الرسائل المُرسَلة» (messagesSent) أكبر من قيمة UInt القصوى محوّلةً إلى عدد طويل (toLong) ناقص واحد. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:519]

```
520:                 throw SessionError.NonceExceeded("Nonce value $messagesSent exceeds 4-byte limit")
```
> تُرمى خطأ الجلسة «تجاوز القيمة المرة الواحدة» (SessionError.NonceExceeded) برسالة تتضمن قيمة «الرسائل المُرسَلة» ونصاً «تتجاوز حد الأربعة بايتات». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:520]

```
521:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:521]

```
522:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:522]

```
523:             try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:523]

```
524:                 // assert that sendCipher!!.macLength is 16:
```
> تعليق: تأكيد أن طول رمز المصادقة (macLength) لمُشفِّر الإرسال يساوي ١٦. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:524]

```
525:                 if (sendCipher!!.macLength != 16) {
```
> شرط: إذا كان طول رمز المصادقة (macLength) لمُشفِّر الإرسال (مع التأكيد على عدم خلوّه بالعلامة !!) لا يساوي ١٦. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:525]

```
526:                     throw IllegalStateException("Send cipher MAC length is not 16")
```
> تُرمى استثناء حالة غير قانونية برسالة «طول رمز المصادقة لمُشفِّر الإرسال ليس ١٦». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:526]

```
527:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:527]

```
528:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:528]

```
529:                 // Encrypt the data first
```
> تعليق: شفّر البيانات أولاً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:529]

```
530:                 val ciphertext = ByteArray(data.size + sendCipher!!.macLength) // Add space for MAC tag
```
> يُعرَّف ثابت «النص المُشفَّر» (ciphertext) كمصفوفة بايتات حجمها حجم «البيانات» زائد طول رمز المصادقة لمُشفِّر الإرسال، مع تعليق: أضف مساحة لوسم رمز المصادقة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:530]

```
531:                 sendCipher!!.setNonce(messagesSent)
```
> يُستدعى على مُشفِّر الإرسال الدالة «ضبط القيمة المرة الواحدة» (setNonce) بالقيمة «الرسائل المُرسَلة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:531]

```
532:                 val ciphertextLength = sendCipher!!.encryptWithAd(null, data, 0, ciphertext, 0, data.size)
```
> يُعرَّف ثابت «طول النص المُشفَّر» (ciphertextLength) قيمته نتيجة استدعاء دالة «التشفير ببيانات مُلحقة» (encryptWithAd) على مُشفِّر الإرسال بوسائط: خالية، و«البيانات»، و٠، و«النص المُشفَّر»، و٠، وحجم «البيانات». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:532]

```
533:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:533]

```
534:                 // Get the current nonce before incrementing
```
> تعليق: احصل على القيمة المرة الواحدة الحالية قبل الزيادة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:534]

```
535:                 val currentNonce = messagesSent
```
> يُعرَّف ثابت «القيمة المرة الواحدة الحالية» (currentNonce) قيمته «الرسائل المُرسَلة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:535]

```
536:                 messagesSent++
```
> يُزاد «الرسائل المُرسَلة» بمقدار واحد. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:536]

```
537:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:537]

```
538:                 // Create combined payload: <nonce><ciphertext> (4 bytes for nonce)
```
> تعليق: أنشئ حمولة مُدمَجة: «قيمة مرة واحدة» ثم «نص مُشفَّر» (٤ بايتات للقيمة المرة الواحدة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:538]

```
539:                 val nonceBytes = nonceToBytes(currentNonce)
```
> يُعرَّف ثابت «بايتات القيمة المرة الواحدة» (nonceBytes) قيمته نتيجة دالة «تحويل القيمة المرة الواحدة إلى بايتات» (nonceToBytes) للوسيطة «القيمة المرة الواحدة الحالية». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:539]

```
540:                 val combinedPayload = ByteArray(NONCE_SIZE_BYTES + ciphertextLength)
```
> يُعرَّف ثابت «الحمولة المُدمَجة» (combinedPayload) كمصفوفة بايتات حجمها ثابت «حجم القيمة المرة الواحدة بالبايتات» (NONCE_SIZE_BYTES) زائد «طول النص المُشفَّر». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:540]

```
541:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:541]

```
542:                 // Copy nonce (first 4 bytes)
```
> تعليق: انسخ القيمة المرة الواحدة (أول ٤ بايتات). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:542]

```
543:                 System.arraycopy(nonceBytes, 0, combinedPayload, 0, NONCE_SIZE_BYTES)
```
> يُستدعى «نسخ المصفوفة» (System.arraycopy) من «بايتات القيمة المرة الواحدة» من الموضع ٠ إلى «الحمولة المُدمَجة» من الموضع ٠ بطول «حجم القيمة المرة الواحدة بالبايتات». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:543]

```
544:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:544]

```
545:                 // Copy ciphertext (remaining bytes)
```
> تعليق: انسخ النص المُشفَّر (البايتات المتبقية). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:545]

```
546:                 System.arraycopy(ciphertext, 0, combinedPayload, NONCE_SIZE_BYTES, ciphertextLength)
```
> يُستدعى «نسخ المصفوفة» من «النص المُشفَّر» من الموضع ٠ إلى «الحمولة المُدمَجة» من الموضع «حجم القيمة المرة الواحدة بالبايتات» بطول «طول النص المُشفَّر». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:546]

```
547:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:547]

```
548:                 // Log high nonce values that might indicate issues
```
> تعليق: سجّل قيم القيمة المرة الواحدة المرتفعة التي قد تشير إلى مشاكل. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:548]

```
549:                 if (currentNonce > HIGH_NONCE_WARNING_THRESHOLD) {
```
> شرط: إذا كانت «القيمة المرة الواحدة الحالية» أكبر من ثابت «عتبة تحذير القيمة المرة الواحدة المرتفعة» (HIGH_NONCE_WARNING_THRESHOLD). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:549]

```
550:                     Log.w(TAG, "High nonce value detected: $currentNonce - consider rekeying")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم (TAG) ورسالة «اكتُشِفت قيمة مرة واحدة مرتفعة:» تتضمن «القيمة المرة الواحدة الحالية» ونصاً «فكّر في إعادة التمفتح». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:550]

```
551:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:551]

```
552:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:552]

```
553:                 Log.d(TAG, "✅ ANDROID ENCRYPT: ${data.size} → ${combinedPayload.size} bytes (nonce: $currentNonce, ciphertextLength+TAG: ${ciphertextLength}) for $peerID (msg #$messagesSent, role: ${if (isInitiator) "INITIATOR" else "RESPONDER"})")
```
> يُستدعى تسجيل تنقيح (Log.d) بالوسم ورسالة تشفير أندرويد تتضمن حجم «البيانات» وحجم «الحمولة المُدمَجة» و«القيمة المرة الواحدة الحالية» و«طول النص المُشفَّر» و«معرّف النظير» (peerID) و«الرسائل المُرسَلة» والدور (INITIATOR إذا كان «بادئاً» (isInitiator) وإلا RESPONDER). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:553]

```
554:                 return combinedPayload
```
> تُعيد الدالة «الحمولة المُدمَجة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:554]

```
555:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:555]

```
556:             } catch (e: Exception) {
```
> بداية كتلة التقاط (catch) للاستثناء (Exception) المسمى e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:556]

```
557:                 Log.e(TAG, "Real encryption failed - exception: ${e.message}")
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم ورسالة «فشل التشفير الحقيقي - استثناء:» تتضمن رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:557]

```
558:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:558]

```
559:                 // ENHANCED: Log cipher state for debugging
```
> تعليق: مُحسَّن: سجّل حالة المُشفِّر للتنقيح. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:559]

```
560:                 if (sendCipher != null) {
```
> شرط: إذا كان «مُشفِّر الإرسال» لا يساوي خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:560]

```
561:                     Log.e(TAG, "Send cipher state: ${sendCipher!!.javaClass.simpleName}")
```
> يُستدعى تسجيل خطأ بالوسم ورسالة «حالة مُشفِّر الإرسال:» تتضمن الاسم البسيط لصنف جافا (javaClass.simpleName) لمُشفِّر الإرسال. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:561]

```
562:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:562]

```
563:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:563]

```
564:                 throw SessionError.EncryptionFailed
```
> تُرمى خطأ الجلسة «فشل التشفير» (SessionError.EncryptionFailed). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:564]

```
565:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:565]

```
566:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:566]

```
567:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:567]

```
568:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:568]

```
569:     /**
```
> بداية تعليق توثيقي (Javadoc). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:569]

```
570:      * Decrypt data in transport mode using real ChaCha20-Poly1305 with sliding window replay protection
```
> تعليق: فكّ تشفير البيانات في وضع النقل باستعمال ChaCha20-Poly1305 الحقيقي مع حماية من إعادة التشغيل بنافذة منزلقة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:570]

```
571:      * Expects: <nonce><ciphertext> where nonce is 4 bytes (matching iOS implementation)
```
> تعليق: يتوقع: «قيمة مرة واحدة» ثم «نص مُشفَّر» حيث القيمة المرة الواحدة ٤ بايتات (مطابقةً لتطبيق iOS). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:571]

```
572:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:572]

```
573:     fun decrypt(combinedPayload: ByteArray): ByteArray {
```
> تُعرَّف دالة باسم «فك التشفير» (decrypt) تأخذ مُعاملاً اسمه «الحمولة المُدمَجة» (combinedPayload) من نوع مصفوفة بايتات وتُعيد مصفوفة بايتات. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:573]

```
574:         // Pre-check state without holding cipher lock
```
> تعليق: فحص مسبق للحالة دون الإمساك بقفل المُشفِّر. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:574]

```
575:         if (!isEstablished()) {
```
> شرط: إذا لم تُعِد دالة «مُثبَّتة» قيمة صحيحة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:575]

```
576:             throw IllegalStateException("Session not established")
```
> تُرمى استثناء حالة غير قانونية برسالة «الجلسة غير مُثبَّتة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:576]

```
577:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:577]

```
578:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:578]

```
579:         // Critical section: Use dedicated cipher lock to protect CipherState nonce corruption
```
> تعليق: قسم حرج: استعمل قفل المُشفِّر المخصص لحماية حالة المُشفِّر من تلف القيمة المرة الواحدة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:579]

```
580:         synchronized(cipherLock) {
```
> كتلة متزامنة على الكائن «قفل المُشفِّر». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:580]

```
581:             // Double-check state inside lock
```
> تعليق: فحص مزدوج للحالة داخل القفل. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:581]

```
582:             if (!isEstablished()) {
```
> شرط: إذا لم تُعِد دالة «مُثبَّتة» قيمة صحيحة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:582]

```
583:                 throw IllegalStateException("Session not established during cipher operation")
```
> تُرمى استثناء حالة غير قانونية برسالة «الجلسة غير مُثبَّتة أثناء عملية التشفير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:583]

```
584:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:584]

```
585:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:585]

```
586:             if (receiveCipher == null) {
```
> شرط: إذا كان «مُشفِّر الاستقبال» (receiveCipher) يساوي خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:586]

```
587:                 throw IllegalStateException("Receive cipher not available")
```
> تُرمى استثناء حالة غير قانونية برسالة «مُشفِّر الاستقبال غير متاح». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:587]

```
588:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:588]

```
589:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:589]

```
590:             try {
```
> بداية كتلة محاولة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:590]

```
591:                 // Extract nonce and ciphertext from combined payload
```
> تعليق: استخرج القيمة المرة الواحدة والنص المُشفَّر من الحمولة المُدمَجة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:591]

```
592:                 val nonceAndCiphertext = extractNonceFromCiphertextPayload(combinedPayload)
```
> يُعرَّف ثابت «القيمة المرة الواحدة والنص المُشفَّر» (nonceAndCiphertext) قيمته نتيجة دالة «استخراج القيمة المرة الواحدة من حمولة النص المُشفَّر» (extractNonceFromCiphertextPayload) للوسيطة «الحمولة المُدمَجة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:592]

```
593:                 if (nonceAndCiphertext == null) {
```
> شرط: إذا كان «القيمة المرة الواحدة والنص المُشفَّر» يساوي خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:593]

```
594:                     Log.e(TAG, "Failed to extract nonce from payload for $peerID")
```
> يُستدعى تسجيل خطأ بالوسم ورسالة «فشل استخراج القيمة المرة الواحدة من الحمولة لـ» تتضمن «معرّف النظير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:594]

```
595:                     throw SessionError.DecryptionFailed
```
> تُرمى خطأ الجلسة «فشل فك التشفير» (SessionError.DecryptionFailed). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:595]

```
596:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:596]

```
597:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:597]

```
598:                 val (extractedNonce, ciphertext) = nonceAndCiphertext
```
> يُفكَّك «القيمة المرة الواحدة والنص المُشفَّر» إلى ثابتين: «القيمة المرة الواحدة المُستخرَجة» (extractedNonce) و«النص المُشفَّر» (ciphertext). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:598]

```
599:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:599]

```
600:                 if (ciphertext.size < receiveCipher!!.macLength) {
```
> شرط: إذا كان حجم «النص المُشفَّر» أصغر من طول رمز المصادقة (macLength) لمُشفِّر الاستقبال. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:600]

```
601:                     Log.w(TAG, "Ciphertext too short: ${ciphertext.size} < ${receiveCipher!!.macLength}")
```
> يُستدعى تسجيل تحذير بالوسم ورسالة «النص المُشفَّر قصير جداً:» تتضمن حجم «النص المُشفَّر» وطول رمز المصادقة لمُشفِّر الاستقبال. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:601]

```
602:                     throw SessionError.DecryptionFailed
```
> تُرمى خطأ الجلسة «فشل فك التشفير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:602]

```
603:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:603]

```
604:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:604]

```
605:                 // Validate nonce with sliding window replay protection
```
> تعليق: تحقّق من القيمة المرة الواحدة بحماية إعادة التشغيل بالنافذة المنزلقة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:605]

```
606:                 if (!isValidNonce(extractedNonce, highestReceivedNonce, replayWindow)) {
```
> شرط: إذا لم تُعِد دالة «قيمة مرة واحدة صالحة» (isValidNonce) صحيحاً للوسائط «القيمة المرة الواحدة المُستخرَجة» و«أعلى قيمة مرة واحدة مُستقبَلة» (highestReceivedNonce) و«نافذة إعادة التشغيل» (replayWindow). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:606]

```
607:                     Log.w(TAG, "Replay attack detected: nonce $extractedNonce rejected for $peerID")
```
> يُستدعى تسجيل تحذير بالوسم ورسالة «اكتُشِف هجوم إعادة تشغيل: رُفِضت القيمة المرة الواحدة» تتضمن «القيمة المرة الواحدة المُستخرَجة» و«معرّف النظير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:607]

```
608:                     throw SessionError.DecryptionFailed
```
> تُرمى خطأ الجلسة «فشل فك التشفير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:608]

```
609:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:609]

```
610:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:610]

```
611:                 // Use the extracted nonce for decryption
```
> تعليق: استعمل القيمة المرة الواحدة المُستخرَجة لفك التشفير. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:611]

```
612:                 val plaintext = ByteArray(ciphertext.size) 
```
> يُعرَّف ثابت «النص الصريح» (plaintext) كمصفوفة بايتات حجمها حجم «النص المُشفَّر». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:612]

```
613:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:613]

```
614:                  receiveCipher!!.setNonce(extractedNonce)
```
> يُستدعى على مُشفِّر الاستقبال الدالة «ضبط القيمة المرة الواحدة» (setNonce) بالقيمة «القيمة المرة الواحدة المُستخرَجة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:614]

```
615:                 val plaintextLength = receiveCipher!!.decryptWithAd(null, ciphertext, 0, plaintext, 0, ciphertext.size)
```
> يُعرَّف ثابت «طول النص الصريح» (plaintextLength) قيمته نتيجة دالة «فك التشفير ببيانات مُلحقة» (decryptWithAd) على مُشفِّر الاستقبال بوسائط: خالية، و«النص المُشفَّر»، و٠، و«النص الصريح»، و٠، وحجم «النص المُشفَّر». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:615]

```
616:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:616]

```
617:                 // Mark nonce as seen after successful decryption
```
> تعليق: علّم القيمة المرة الواحدة كمُشاهَدة بعد فك التشفير الناجح. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:617]

```
618:                 val (newHighestReceivedNonce, newReplayWindow) = markNonceAsSeen(extractedNonce, highestReceivedNonce, replayWindow)
```
> يُفكَّك ناتج دالة «تعليم القيمة المرة الواحدة كمُشاهَدة» (markNonceAsSeen) للوسائط «القيمة المرة الواحدة المُستخرَجة» و«أعلى قيمة مرة واحدة مُستقبَلة» و«نافذة إعادة التشغيل» إلى ثابتين: «أعلى قيمة مرة واحدة مُستقبَلة جديدة» (newHighestReceivedNonce) و«نافذة إعادة تشغيل جديدة» (newReplayWindow). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:618]

```
619:                 highestReceivedNonce = newHighestReceivedNonce
```
> يُسنَد إلى «أعلى قيمة مرة واحدة مُستقبَلة» القيمة «أعلى قيمة مرة واحدة مُستقبَلة جديدة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:619]

```
620:                 replayWindow = newReplayWindow
```
> يُسنَد إلى «نافذة إعادة التشغيل» القيمة «نافذة إعادة تشغيل جديدة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:620]

```
621:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:621]

```
622:                 // Log high nonce values that might indicate issues
```
> تعليق: سجّل قيم القيمة المرة الواحدة المرتفعة التي قد تشير إلى مشاكل. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:622]

```
623:                 if (extractedNonce > HIGH_NONCE_WARNING_THRESHOLD) {
```
> شرط: إذا كانت «القيمة المرة الواحدة المُستخرَجة» أكبر من ثابت «عتبة تحذير القيمة المرة الواحدة المرتفعة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:623]

```
624:                     Log.w(TAG, "High nonce value detected: $extractedNonce - consider rekeying")
```
> يُستدعى تسجيل تحذير بالوسم ورسالة «اكتُشِفت قيمة مرة واحدة مرتفعة:» تتضمن «القيمة المرة الواحدة المُستخرَجة» ونصاً «فكّر في إعادة التمفتح». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:624]

```
625:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:625]

```
626:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:626]

```
627:                 val result = plaintext.copyOf(plaintextLength)
```
> يُعرَّف ثابت «النتيجة» (result) قيمته نسخة من «النص الصريح» بطول «طول النص الصريح» عبر الدالة copyOf. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:627]

```
628:                 Log.d(TAG, "✅ ANDROID DECRYPT: ${combinedPayload.size} → ${result.size} bytes from $peerID (nonce: $extractedNonce, highest: $highestReceivedNonce, role: ${if (isInitiator) "INITIATOR" else "RESPONDER"})")
```
> يُستدعى تسجيل تنقيح بالوسم ورسالة فك تشفير أندرويد تتضمن حجم «الحمولة المُدمَجة» وحجم «النتيجة» و«معرّف النظير» و«القيمة المرة الواحدة المُستخرَجة» و«أعلى قيمة مرة واحدة مُستقبَلة» والدور (INITIATOR إذا كان «بادئاً» وإلا RESPONDER). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:628]

```
629:                 return result
```
> تُعيد الدالة «النتيجة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:629]

```
630:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:630]

```
631:             } catch (e: Exception) {
```
> بداية كتلة التقاط للاستثناء المسمى e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:631]

```
632:                 Log.e(TAG, "Decryption failed - exception: ${e.message}")
```
> يُستدعى تسجيل خطأ بالوسم ورسالة «فشل فك التشفير - استثناء:» تتضمن رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:632]

```
633:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:633]

```
634:                 // ENHANCED: Log cipher state and session details for debugging
```
> تعليق: مُحسَّن: سجّل حالة المُشفِّر وتفاصيل الجلسة للتنقيح. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:634]

```
635:                 if (receiveCipher != null) {
```
> شرط: إذا كان «مُشفِّر الاستقبال» لا يساوي خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:635]

```
636:                     Log.e(TAG, "Receive cipher state: ${receiveCipher!!.javaClass.simpleName}")
```
> يُستدعى تسجيل خطأ بالوسم ورسالة «حالة مُشفِّر الاستقبال:» تتضمن الاسم البسيط لصنف جافا لمُشفِّر الاستقبال. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:636]

```
637:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:637]

```
638:                 Log.e(TAG, "Session state: $state, highest received nonce: $highestReceivedNonce")
```
> يُستدعى تسجيل خطأ بالوسم ورسالة «حالة الجلسة:» تتضمن «الحالة» (state) و«أعلى قيمة مرة واحدة مُستقبَلة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:638]

```
639:                 Log.e(TAG, "Input data size: ${combinedPayload.size} bytes")
```
> يُستدعى تسجيل خطأ بالوسم ورسالة «حجم بيانات الإدخال:» تتضمن حجم «الحمولة المُدمَجة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:639]

```
640:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:640]

```
641:                 throw SessionError.DecryptionFailed
```
> تُرمى خطأ الجلسة «فشل فك التشفير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:641]

```
642:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:642]

```
643:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:643]

```
644:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:644]

```
645:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:645]

```
646:     // MARK: - Session Information
```
> تعليق: علامة تقسيم: معلومات الجلسة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:646]

```
647:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:647]

```
648:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:648]

```
649:      * Get remote static public key (available after handshake completion)
```
> تعليق: احصل على المفتاح العام الساكن البعيد (متاح بعد اكتمال المصافحة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:649]

```
650:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:650]

```
651:     fun getRemoteStaticPublicKey(): ByteArray? {
```
> تُعرَّف دالة باسم «احصل على المفتاح العام الساكن البعيد» (getRemoteStaticPublicKey) لا تأخذ مُعاملات وتُعيد مصفوفة بايتات قابلة للخلوّ (ByteArray?). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:651]

```
652:         return remoteStaticPublicKey?.clone()
```
> تُعيد الدالة نسخة (clone) من «المفتاح العام الساكن البعيد» (remoteStaticPublicKey) أو خالياً إن كان خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:652]

```
653:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:653]

```
654:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:654]

```
655:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:655]

```
656:      * Get handshake hash for channel binding
```
> تعليق: احصل على بصمة المصافحة (handshake hash) لربط القناة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:656]

```
657:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:657]

```
658:     fun getHandshakeHash(): ByteArray? {
```
> تُعرَّف دالة باسم «احصل على بصمة المصافحة» (getHandshakeHash) لا تأخذ مُعاملات وتُعيد مصفوفة بايتات قابلة للخلوّ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:658]

```
659:         return handshakeHash?.clone()
```
> تُعيد الدالة نسخة من «بصمة المصافحة» (handshakeHash) أو خالياً إن كانت خالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:659]

```
660:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:660]

```
661:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:661]

```
662:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:662]

```
663:      * Check if session needs rekeying
```
> تعليق: تحقّق إن كانت الجلسة تحتاج إعادة تمفتح. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:663]

```
664:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:664]

```
665:     fun needsRekey(): Boolean {
```
> تُعرَّف دالة باسم «تحتاج إعادة تمفتح» (needsRekey) لا تأخذ مُعاملات وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:665]

```
666:         if (!isEstablished()) return false
```
> شرط: إذا لم تُعِد دالة «مُثبَّتة» صحيحاً فتُعيد الدالة قيمة خاطئة (false). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:666]

```
667:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:667]

```
668:         val timeLimit = System.currentTimeMillis() - creationTime > REKEY_TIME_LIMIT
```
> يُعرَّف ثابت «حد الوقت» (timeLimit) قيمته نتيجة الشرط: الوقت الحالي بالميلي ثانية (System.currentTimeMillis) ناقص «وقت الإنشاء» (creationTime) أكبر من ثابت «حد وقت إعادة التمفتح» (REKEY_TIME_LIMIT). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:668]

```
669:         val messageLimit = (messagesSent + messagesReceived) > REKEY_MESSAGE_LIMIT
```
> يُعرَّف ثابت «حد الرسائل» (messageLimit) قيمته نتيجة الشرط: مجموع «الرسائل المُرسَلة» و«الرسائل المُستقبَلة» (messagesReceived) أكبر من ثابت «حد رسائل إعادة التمفتح» (REKEY_MESSAGE_LIMIT). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:669]

```
670:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:670]

```
671:         return timeLimit || messageLimit
```
> تُعيد الدالة نتيجة «أو» المنطقية بين «حد الوقت» و«حد الرسائل». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:671]

```
672:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:672]

```
673:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:673]

```
674:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:674]

```
675:      * Get session statistics
```
> تعليق: احصل على إحصاءات الجلسة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:675]

```
676:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:676]

```
677:     fun getSessionStats(): String = buildString {
```
> تُعرَّف دالة باسم «احصل على إحصاءات الجلسة» (getSessionStats) تُعيد سلسلة نصية (String) قيمتها نتيجة باني السلسلة (buildString). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:677]

```
678:         appendLine("NoiseSession with $peerID:")
```
> يُستدعى «إلحاق سطر» (appendLine) بالنص «جلسة Noise مع» تتضمن «معرّف النظير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:678]

```
679:         appendLine("  State: $state")
```
> يُستدعى «إلحاق سطر» بالنص «الحالة:» تتضمن «الحالة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:679]

```
680:         appendLine("  Role: ${if (isInitiator) "initiator" else "responder"}")
```
> يُستدعى «إلحاق سطر» بالنص «الدور:» يتضمن «بادئ» (initiator) إذا كان «بادئاً» وإلا «مُستجيب» (responder). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:680]

```
681:         appendLine("  Messages sent: $messagesSent")
```
> يُستدعى «إلحاق سطر» بالنص «الرسائل المُرسَلة:» تتضمن «الرسائل المُرسَلة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:681]

```
682:         appendLine("  Messages received: $messagesReceived")
```
> يُستدعى «إلحاق سطر» بالنص «الرسائل المُستقبَلة:» تتضمن «الرسائل المُستقبَلة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:682]

```
683:         appendLine("  Session age: ${(System.currentTimeMillis() - creationTime) / 1000}s")
```
> يُستدعى «إلحاق سطر» بالنص «عمر الجلسة:» يتضمن الوقت الحالي بالميلي ثانية ناقص «وقت الإنشاء» مقسوماً على ١٠٠٠ متبوعاً بحرف الثانية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:683]

```
684:         appendLine("  Needs rekey: ${needsRekey()}")
```
> يُستدعى «إلحاق سطر» بالنص «تحتاج إعادة تمفتح:» يتضمن ناتج دالة «تحتاج إعادة تمفتح». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:684]

```
685:         appendLine("  Has remote key: ${remoteStaticPublicKey != null}")
```
> يُستدعى «إلحاق سطر» بالنص «يملك مفتاحاً بعيداً:» يتضمن نتيجة الشرط: «المفتاح العام الساكن البعيد» لا يساوي خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:685]

```
686:         appendLine("  Has send cipher: ${sendCipher != null}")
```
> يُستدعى «إلحاق سطر» بالنص «يملك مُشفِّر إرسال:» يتضمن نتيجة الشرط: «مُشفِّر الإرسال» لا يساوي خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:686]

```
687:         appendLine("  Has receive cipher: ${receiveCipher != null}")
```
> يُستدعى «إلحاق سطر» بالنص «يملك مُشفِّر استقبال:» يتضمن نتيجة الشرط: «مُشفِّر الاستقبال» لا يساوي خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:687]

```
688:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:688]

```
689:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:689]

```
690:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:690]

```
691:      * Reset session state
```
> تعليق: أعد ضبط حالة الجلسة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:691]

```
692:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:692]

```
693:     @Synchronized
```
> تعليق توضيحي (annotation) «متزامن» (@Synchronized) على الدالة التالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:693]

```
694:     fun reset() {
```
> تُعرَّف دالة باسم «إعادة الضبط» (reset) لا تأخذ مُعاملات ولا تُعيد قيمة صريحة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:694]

```
695:         try {
```
> بداية كتلة محاولة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:695]

```
696:             // Destroy existing state
```
> تعليق: دمّر الحالة الموجودة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:696]

```
697:             destroy()
```
> يُستدعى دالة «التدمير» (destroy). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:697]

```
698:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:698]

```
699:             // Reset to uninitialized state (handshake will be initialized when needed)
```
> تعليق: أعد الضبط إلى حالة غير مُهيَّأة (ستُهيَّأ المصافحة عند الحاجة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:699]

```
700:             state = NoiseSessionState.Uninitialized
```
> يُسنَد إلى «الحالة» القيمة «غير مُهيَّأة» (NoiseSessionState.Uninitialized). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:700]

```
701:             messagesSent = 0
```
> يُسنَد إلى «الرسائل المُرسَلة» القيمة ٠. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:701]

```
702:             messagesReceived = 0
```
> يُسنَد إلى «الرسائل المُستقبَلة» القيمة ٠. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:702]

```
703:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:703]

```
704:             // Reset sliding window replay protection
```
> تعليق: أعد ضبط حماية إعادة التشغيل بالنافذة المنزلقة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:704]

```
705:             highestReceivedNonce = 0L
```
> يُسنَد إلى «أعلى قيمة مرة واحدة مُستقبَلة» القيمة ٠ من النوع الطويل (0L). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:705]

```
706:             replayWindow = ByteArray(REPLAY_WINDOW_BYTES)
```
> يُسنَد إلى «نافذة إعادة التشغيل» مصفوفة بايتات جديدة حجمها ثابت «بايتات نافذة إعادة التشغيل» (REPLAY_WINDOW_BYTES). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:706]

```
707:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:707]

```
708:             remoteStaticPublicKey = null
```
> يُسنَد إلى «المفتاح العام الساكن البعيد» القيمة الخالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:708]

```
709:             handshakeHash = null
```
> يُسنَد إلى «بصمة المصافحة» القيمة الخالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:709]

```
710:         } catch (e: Exception) {
```
> بداية كتلة التقاط للاستثناء المسمى e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:710]

```
711:             state = NoiseSessionState.Failed(e)
```
> يُسنَد إلى «الحالة» القيمة «فاشلة» (NoiseSessionState.Failed) المُمرَّر إليها الاستثناء e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:711]

```
712:             Log.e(TAG, "Failed to reset session: ${e.message}")
```
> يُستدعى تسجيل خطأ بالوسم ورسالة «فشل إعادة ضبط الجلسة:» تتضمن رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:712]

```
713:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:713]

```
714:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:714]

```
715:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:715]

```
716:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:716]

```
717:      * Clean up session resources securely
```
> تعليق: نظّف موارد الجلسة بأمان. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:717]

```
718:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:718]

```
719:     @Synchronized
```
> تعليق توضيحي «متزامن» على الدالة التالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:719]

```
720:     fun destroy() {
```
> تُعرَّف دالة باسم «التدمير» (destroy) لا تأخذ مُعاملات ولا تُعيد قيمة صريحة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:720]

```
721:         try {
```
> بداية كتلة محاولة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:721]

```
722:             // Destroy Noise objects
```
> تعليق: دمّر كائنات Noise. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:722]

```
723:             sendCipher?.destroy()
```
> يُستدعى دالة «التدمير» (destroy) على «مُشفِّر الإرسال» إن لم يكن خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:723]

```
724:             receiveCipher?.destroy()
```
> يُستدعى دالة «التدمير» على «مُشفِّر الاستقبال» إن لم يكن خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:724]

```
725:             handshakeState?.destroy()
```
> يُستدعى دالة «التدمير» على «حالة المصافحة» (handshakeState) إن لم تكن خالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:725]

```
726:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:726]

```
727:             // Clear sensitive data
```
> تعليق: امسح البيانات الحساسة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:727]

```
728:             remoteStaticPublicKey?.fill(0)
```
> يُستدعى دالة «الملء» (fill) بالقيمة ٠ على «المفتاح العام الساكن البعيد» إن لم يكن خالياً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:728]

```
729:             handshakeHash?.fill(0)
```
> يُستدعى دالة «الملء» بالقيمة ٠ على «بصمة المصافحة» إن لم تكن خالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:729]

```
730:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:730]

```
731:             // Null out references
```
> تعليق: صفّر المراجع إلى خالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:731]

```
732:             sendCipher = null
```
> يُسنَد إلى «مُشفِّر الإرسال» القيمة الخالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:732]

```
733:             receiveCipher = null
```
> يُسنَد إلى «مُشفِّر الاستقبال» القيمة الخالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:733]

```
734:             handshakeState = null
```
> يُسنَد إلى «حالة المصافحة» القيمة الخالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:734]

```
735:             remoteStaticPublicKey = null
```
> يُسنَد إلى «المفتاح العام الساكن البعيد» القيمة الخالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:735]

```
736:             handshakeHash = null
```
> يُسنَد إلى «بصمة المصافحة» القيمة الخالية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:736]

```
737:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:737]

```
738:             if (state !is NoiseSessionState.Failed) {
```
> شرط: إذا كانت «الحالة» ليست من نوع «فاشلة» (NoiseSessionState.Failed). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:738]

```
739:                 state = NoiseSessionState.Failed(Exception("Session destroyed"))
```
> يُسنَد إلى «الحالة» القيمة «فاشلة» المُمرَّر إليها استثناء جديد برسالة «الجلسة مُدمَّرة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:739]

```
740:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:740]

```
741:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:741]

```
742:             Log.d(TAG, "Session destroyed for $peerID")
```
> يُستدعى تسجيل تنقيح بالوسم ورسالة «الجلسة مُدمَّرة لـ» تتضمن «معرّف النظير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:742]

```
743:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:743]

```
744:         } catch (e: Exception) {
```
> بداية كتلة التقاط للاستثناء المسمى e. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:744]

```
745:             Log.w(TAG, "Error during session cleanup: ${e.message}")
```
> يُستدعى تسجيل تحذير بالوسم ورسالة «خطأ أثناء تنظيف الجلسة:» تتضمن رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:745]

```
746:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:746]

```
747:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:747]

```
748: }
```
> إغلاق نطاق (نهاية صنف الجلسة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:748]

```
749:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:749]

```
750: /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:750]
