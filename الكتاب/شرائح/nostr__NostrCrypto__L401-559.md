# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt (الأسطر 401–559)

```
401:             null
```
> يُعيد القيمة العدمية (null). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:401]

```
402:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:402]

```
403:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:403]

```
404:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:404]

```
405:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:405]

```
406:      * BIP-340 Schnorr signature creation
```
> تعليق: إنشاء توقيع شنور (Schnorr) وفق المعيار BIP-340. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:406]

```
407:      * Returns 64-byte signature (r || s) as hex string
```
> تعليق: يُعيد توقيعاً بطول ٦٤ بايت (r متبوعاً بـ s) كسلسلة ست عشرية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:407]

```
408:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:408]

```
409:     fun schnorrSign(messageHash: ByteArray, privateKeyHex: String): String {
```
> تُعرَّف دالة التوقيع بشنور (schnorrSign) تأخذ مُعامِل بصمة الرسالة (messageHash) من نوع مصفوفة بايت ومُعامِل المفتاح الخاص الست عشري (privateKeyHex) من نوع نص، وتُعيد نصاً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:409]

```
410:         require(messageHash.size == 32) { "Message hash must be 32 bytes" }
```
> يُشترط (require) أن يساوي حجم بصمة الرسالة ٣٢، وإلا فالرسالة «يجب أن تكون بصمة الرسالة ٣٢ بايت». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:410]

```
411:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:411]

```
412:         val privateKeyBytes = privateKeyHex.hexToByteArray()
```
> يُعرَّف الثابت بايتات المفتاح الخاص (privateKeyBytes) بقيمة ناتجة عن تحويل المفتاح الخاص الست عشري إلى مصفوفة بايت عبر الدالة hexToByteArray. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:412]

```
413:         require(privateKeyBytes.size == 32) { "Private key must be 32 bytes" }
```
> يُشترط أن يساوي حجم بايتات المفتاح الخاص ٣٢، وإلا فالرسالة «يجب أن يكون المفتاح الخاص ٣٢ بايت». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:413]

```
414:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:414]

```
415:         val d = BigInteger(1, privateKeyBytes)
```
> يُعرَّف الثابت d بقيمة عدد صحيح كبير (BigInteger) موجب الإشارة (1) مبنيّ من بايتات المفتاح الخاص. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:415]

```
416:         require(d > BigInteger.ZERO && d < secp256k1Params.n) { "Invalid private key" }
```
> يُشترط أن يكون d أكبر من الصفر وأصغر من قيمة n لمعاملات المنحنى secp256k1Params، وإلا فالرسالة «مفتاح خاص غير صالح». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:416]

```
417:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:417]

```
418:         // Compute public key point P = d * G
```
> تعليق: حساب نقطة المفتاح العام P بضرب d في G. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:418]

```
419:         val P = secp256k1Params.g.multiply(d).normalize()
```
> يُعرَّف الثابت P بقيمة نقطة المولِّد g من معاملات secp256k1Params مضروبة في d ثم مُسوّاة عبر normalize. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:419]

```
420:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:420]

```
421:         // Ensure P has even y coordinate, adjust d if necessary
```
> تعليق: التأكّد من أن للنقطة P إحداثيّ y زوجيّاً، وتعديل d عند اللزوم. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:421]

```
422:         val (adjustedD, publicKeyBytes) = if (hasEvenY(P)) {
```
> يُعرَّف زوج الثوابت d المُعدَّل (adjustedD) وبايتات المفتاح العام (publicKeyBytes) عبر تفكيك ناتج تعبير شرطي إذا كان y للنقطة P زوجيّاً عبر الدالة hasEvenY. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:422]

```
423:             Pair(d, P.xCoord.encoded)
```
> يُعاد زوج (Pair) قيمته الأولى d والثانية الترميز encoded لإحداثيّ x للنقطة P. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:423]

```
424:         } else {
```
> وإلا (else) إغلاق فرع ثم بداية فرع بديل. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:424]

```
425:             Pair(secp256k1Params.n.subtract(d), P.xCoord.encoded)
```
> يُعاد زوج قيمته الأولى ناتج طرح d من n لمعاملات secp256k1Params والثانية ترميز إحداثيّ x للنقطة P. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:425]

```
426:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:426]

```
427:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:427]

```
428:         // Generate nonce
```
> تعليق: توليد القيمة المؤقتة (nonce). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:428]

```
429:         val k = generateNonce(adjustedD, messageHash, publicKeyBytes)
```
> يُعرَّف الثابت k بقيمة ناتجة عن استدعاء دالة توليد القيمة المؤقتة generateNonce بالوسائط d المُعدَّل وبصمة الرسالة وبايتات المفتاح العام. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:429]

```
430:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:430]

```
431:         // Compute R = k * G
```
> تعليق: حساب R بضرب k في G. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:431]

```
432:         val R = secp256k1Params.g.multiply(k).normalize()
```
> يُعرَّف الثابت R بقيمة نقطة المولِّد g مضروبة في k ثم مُسوّاة عبر normalize. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:432]

```
433:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:433]

```
434:         // Ensure R has even y coordinate
```
> تعليق: التأكّد من أن للنقطة R إحداثيّ y زوجيّاً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:434]

```
435:         val adjustedK = if (hasEvenY(R)) k else secp256k1Params.n.subtract(k)
```
> يُعرَّف الثابت k المُعدَّل (adjustedK) بقيمة k إذا كان y للنقطة R زوجيّاً، وإلا فناتج طرح k من n لمعاملات secp256k1Params. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:435]

```
436:         val r = R.xCoord.encoded
```
> يُعرَّف الثابت r بقيمة الترميز encoded لإحداثيّ x للنقطة R. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:436]

```
437:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:437]

```
438:         // Compute challenge e = H(r || P || m)
```
> تعليق: حساب التحدّي e بصورة بصمة لـ r متبوعاً بـ P متبوعاً بـ m. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:438]

```
439:         val challengeData = ByteArray(96) // 32 + 32 + 32
```
> يُعرَّف الثابت بيانات التحدّي (challengeData) بمصفوفة بايت بطول ٩٦، والتعليق: ٣٢ زائد ٣٢ زائد ٣٢. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:439]

```
440:         System.arraycopy(r, 0, challengeData, 0, 32)
```
> يُستدعى نسخ المصفوفة System.arraycopy لنسخ ٣٢ بايت من r ابتداءً من الموضع ٠ إلى بيانات التحدّي ابتداءً من الموضع ٠. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:440]

```
441:         System.arraycopy(publicKeyBytes, 0, challengeData, 32, 32)
```
> يُستدعى System.arraycopy لنسخ ٣٢ بايت من بايتات المفتاح العام ابتداءً من الموضع ٠ إلى بيانات التحدّي ابتداءً من الموضع ٣٢. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:441]

```
442:         System.arraycopy(messageHash, 0, challengeData, 64, 32)
```
> يُستدعى System.arraycopy لنسخ ٣٢ بايت من بصمة الرسالة ابتداءً من الموضع ٠ إلى بيانات التحدّي ابتداءً من الموضع ٦٤. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:442]

```
443:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:443]

```
444:         val eBytes = taggedHash("BIP0340/challenge", challengeData)
```
> يُعرَّف الثابت بايتات e (eBytes) بقيمة ناتجة عن استدعاء البصمة الموسومة taggedHash بالوسم النصّي "BIP0340/challenge" وبيانات التحدّي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:444]

```
445:         val e = BigInteger(1, eBytes).mod(secp256k1Params.n)
```
> يُعرَّف الثابت e بقيمة عدد صحيح كبير موجب الإشارة مبنيّ من بايتات e مأخوذاً بباقي القسمة mod على n لمعاملات secp256k1Params. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:445]

```
446:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:446]

```
447:         // Compute s = (k + e * d) mod n
```
> تعليق: حساب s مساوياً باقي قسمة (k زائد e مضروباً في d) على n. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:447]

```
448:         val s = adjustedK.add(e.multiply(adjustedD)).mod(secp256k1Params.n)
```
> يُعرَّف الثابت s بقيمة k المُعدَّل مضافاً إليه ناتج ضرب e في d المُعدَّل، مأخوذاً بباقي القسمة على n لمعاملات secp256k1Params. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:448]

```
449:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:449]

```
450:         // Return signature as r || s (64 bytes hex)
```
> تعليق: إعادة التوقيع بصورة r متبوعاً بـ s (٦٤ بايت ست عشريّاً). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:450]

```
451:         val rPadded = ByteArray(32)
```
> يُعرَّف الثابت r المُبطَّن (rPadded) بمصفوفة بايت بطول ٣٢. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:451]

```
452:         val sPadded = ByteArray(32)
```
> يُعرَّف الثابت s المُبطَّن (sPadded) بمصفوفة بايت بطول ٣٢. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:452]

```
453:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:453]

```
454:         val rBytes = r
```
> يُعرَّف الثابت بايتات r (rBytes) بقيمة r. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:454]

```
455:         val sBytes = s.toByteArray()
```
> يُعرَّف الثابت بايتات s (sBytes) بقيمة s محوّلاً إلى مصفوفة بايت عبر toByteArray. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:455]

```
456:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:456]

```
457:         // Pad r to 32 bytes (should already be 32)
```
> تعليق: تبطين r إلى ٣٢ بايت (يُفترض أنه ٣٢ أصلاً). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:457]

```
458:         System.arraycopy(rBytes, 0, rPadded, 0, minOf(32, rBytes.size))
```
> يُستدعى System.arraycopy لنسخ عدد بايتات يساوي أصغر القيمتين ٣٢ وحجم بايتات r من بايتات r ابتداءً من الموضع ٠ إلى r المُبطَّن ابتداءً من الموضع ٠. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:458]

```
459:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:459]

```
460:         // Pad s to 32 bytes - handle BigInteger padding correctly
```
> تعليق: تبطين s إلى ٣٢ بايت مع معالجة تبطين العدد الصحيح الكبير بشكل صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:460]

```
461:         if (sBytes.size <= 32) {
```
> شرط إذا كان حجم بايتات s أصغر من أو يساوي ٣٢. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:461]

```
462:             val srcStart = maxOf(0, sBytes.size - 32)
```
> يُعرَّف الثابت بداية المصدر (srcStart) بأكبر القيمتين ٠ و(حجم بايتات s ناقص ٣٢). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:462]

```
463:             val destStart = maxOf(0, 32 - sBytes.size)
```
> يُعرَّف الثابت بداية الوجهة (destStart) بأكبر القيمتين ٠ و(٣٢ ناقص حجم بايتات s). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:463]

```
464:             val length = minOf(sBytes.size, 32)
```
> يُعرَّف الثابت الطول (length) بأصغر القيمتين حجم بايتات s و٣٢. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:464]

```
465:             System.arraycopy(sBytes, srcStart, sPadded, destStart, length)
```
> يُستدعى System.arraycopy لنسخ عدد بايتات يساوي الطول من بايتات s ابتداءً من بداية المصدر إلى s المُبطَّن ابتداءً من بداية الوجهة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:465]

```
466:         } else {
```
> وإلا إغلاق فرع ثم بداية فرع بديل. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:466]

```
467:             // If BigInteger added a sign byte, skip it
```
> تعليق: إذا أضاف العدد الصحيح الكبير بايت إشارة فتجاوزه. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:467]

```
468:             System.arraycopy(sBytes, sBytes.size - 32, sPadded, 0, 32)
```
> يُستدعى System.arraycopy لنسخ ٣٢ بايت من بايتات s ابتداءً من الموضع (حجم بايتات s ناقص ٣٢) إلى s المُبطَّن ابتداءً من الموضع ٠. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:468]

```
469:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:469]

```
470:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:470]

```
471:         return (rPadded + sPadded).toHexString()
```
> يُعاد ناتج دمج r المُبطَّن مع s المُبطَّن محوّلاً إلى نص ست عشري عبر toHexString. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:471]

```
472:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:472]

```
473:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:473]

```
474:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:474]

```
475:      * BIP-340 Schnorr signature verification
```
> تعليق: التحقّق من توقيع شنور وفق المعيار BIP-340. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:475]

```
476:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:476]

```
477:     fun schnorrVerify(messageHash: ByteArray, signatureHex: String, publicKeyHex: String): Boolean {
```
> تُعرَّف دالة التحقّق من توقيع شنور (schnorrVerify) تأخذ مُعامِل بصمة الرسالة من نوع مصفوفة بايت ومُعامِل التوقيع الست عشري (signatureHex) من نوع نص ومُعامِل المفتاح العام الست عشري (publicKeyHex) من نوع نص، وتُعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:477]

```
478:         return try {
```
> يُعاد ناتج كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:478]

```
479:             require(messageHash.size == 32) { "Message hash must be 32 bytes" }
```
> يُشترط أن يساوي حجم بصمة الرسالة ٣٢، وإلا فالرسالة «يجب أن تكون بصمة الرسالة ٣٢ بايت». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:479]

```
480:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:480]

```
481:             val signatureBytes = signatureHex.hexToByteArray()
```
> يُعرَّف الثابت بايتات التوقيع (signatureBytes) بقيمة التوقيع الست عشري محوّلاً إلى مصفوفة بايت عبر hexToByteArray. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:481]

```
482:             require(signatureBytes.size == 64) { "Signature must be 64 bytes" }
```
> يُشترط أن يساوي حجم بايتات التوقيع ٦٤، وإلا فالرسالة «يجب أن يكون التوقيع ٦٤ بايت». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:482]

```
483:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:483]

```
484:             val publicKeyBytes = publicKeyHex.hexToByteArray()
```
> يُعرَّف الثابت بايتات المفتاح العام بقيمة المفتاح العام الست عشري محوّلاً إلى مصفوفة بايت عبر hexToByteArray. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:484]

```
485:             require(publicKeyBytes.size == 32) { "Public key must be 32 bytes" }
```
> يُشترط أن يساوي حجم بايتات المفتاح العام ٣٢، وإلا فالرسالة «يجب أن يكون المفتاح العام ٣٢ بايت». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:485]

```
486:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:486]

```
487:             // Parse signature
```
> تعليق: تحليل التوقيع. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:487]

```
488:             val r = signatureBytes.copyOfRange(0, 32)
```
> يُعرَّف الثابت r بقيمة نسخة من بايتات التوقيع في المدى من الموضع ٠ إلى ٣٢ عبر copyOfRange. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:488]

```
489:             val sBytes = signatureBytes.copyOfRange(32, 64)
```
> يُعرَّف الثابت بايتات s بقيمة نسخة من بايتات التوقيع في المدى من الموضع ٣٢ إلى ٦٤ عبر copyOfRange. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:489]

```
490:             val s = BigInteger(1, sBytes)
```
> يُعرَّف الثابت s بقيمة عدد صحيح كبير موجب الإشارة مبنيّ من بايتات s. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:490]

```
491:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:491]

```
492:             // Validate r and s
```
> تعليق: التحقّق من صحّة r و s. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:492]

```
493:             val rBigInt = BigInteger(1, r)
```
> يُعرَّف الثابت r كعدد كبير (rBigInt) بقيمة عدد صحيح كبير موجب الإشارة مبنيّ من r. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:493]

```
494:             if (rBigInt >= secp256k1Params.curve.field.characteristic) return false
```
> إذا كان r كعدد كبير أكبر من أو يساوي خاصّية characteristic لحقل field منحنى curve في معاملات secp256k1Params فيُعاد الباطل (false). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:494]

```
495:             if (s >= secp256k1Params.n) return false
```
> إذا كان s أكبر من أو يساوي n لمعاملات secp256k1Params فيُعاد الباطل. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:495]

```
496:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:496]

```
497:             // Lift public key
```
> تعليق: رفع المفتاح العام. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:497]

```
498:             val P = liftX(publicKeyBytes) ?: return false
```
> يُعرَّف الثابت P بقيمة ناتج استدعاء الدالة liftX على بايتات المفتاح العام، وإن كان عدميّاً فيُعاد الباطل. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:498]

```
499:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:499]

```
500:             // Compute challenge e = H(r || P || m)
```
> تعليق: حساب التحدّي e بصورة بصمة لـ r متبوعاً بـ P متبوعاً بـ m. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:500]

```
501:             val challengeData = ByteArray(96)
```
> يُعرَّف الثابت بيانات التحدّي بمصفوفة بايت بطول ٩٦. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:501]

```
502:             System.arraycopy(r, 0, challengeData, 0, 32)
```
> يُستدعى System.arraycopy لنسخ ٣٢ بايت من r ابتداءً من الموضع ٠ إلى بيانات التحدّي ابتداءً من الموضع ٠. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:502]

```
503:             System.arraycopy(publicKeyBytes, 0, challengeData, 32, 32)
```
> يُستدعى System.arraycopy لنسخ ٣٢ بايت من بايتات المفتاح العام ابتداءً من الموضع ٠ إلى بيانات التحدّي ابتداءً من الموضع ٣٢. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:503]

```
504:             System.arraycopy(messageHash, 0, challengeData, 64, 32)
```
> يُستدعى System.arraycopy لنسخ ٣٢ بايت من بصمة الرسالة ابتداءً من الموضع ٠ إلى بيانات التحدّي ابتداءً من الموضع ٦٤. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:504]

```
505:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:505]

```
506:             val eBytes = taggedHash("BIP0340/challenge", challengeData)
```
> يُعرَّف الثابت بايتات e بقيمة ناتجة عن استدعاء البصمة الموسومة taggedHash بالوسم "BIP0340/challenge" وبيانات التحدّي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:506]

```
507:             val e = BigInteger(1, eBytes).mod(secp256k1Params.n)
```
> يُعرَّف الثابت e بقيمة عدد صحيح كبير موجب الإشارة مبنيّ من بايتات e مأخوذاً بباقي القسمة على n لمعاملات secp256k1Params. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:507]

```
508:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:508]

```
509:             // Compute R = s * G - e * P
```
> تعليق: حساب R مساوياً (s مضروباً في G) ناقص (e مضروباً في P). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:509]

```
510:             val sG = secp256k1Params.g.multiply(s)
```
> يُعرَّف الثابت sG بقيمة نقطة المولِّد g من معاملات secp256k1Params مضروبة في s. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:510]

```
511:             val eP = P.multiply(e)
```
> يُعرَّف الثابت eP بقيمة النقطة P مضروبة في e. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:511]

```
512:             val R = sG.subtract(eP).normalize()
```
> يُعرَّف الثابت R بقيمة sG مطروحاً منه eP ثم مُسوّى عبر normalize. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:512]

```
513:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:513]

```
514:             // Check if R has even y and x coordinate matches r
```
> تعليق: فحص ما إذا كان للنقطة R إحداثيّ y زوجيّ وإحداثيّ x مطابق لـ r. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:514]

```
515:             if (!hasEvenY(R)) return false
```
> إذا لم يكن y للنقطة R زوجيّاً عبر hasEvenY فيُعاد الباطل. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:515]

```
516:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:516]

```
517:             val computedR = R.xCoord.encoded
```
> يُعرَّف الثابت R المحسوب (computedR) بقيمة الترميز encoded لإحداثيّ x للنقطة R. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:517]

```
518:             return r.contentEquals(computedR)
```
> يُعاد ناتج مقارنة محتوى r بمحتوى R المحسوب عبر contentEquals. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:518]

```
519:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:519]

```
520:         } catch (e: Exception) {
```
> التقاط (catch) استثناء من نوع Exception باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:520]

```
521:             false
```
> يُعاد الباطل. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:521]

```
522:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:522]

```
523:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:523]

```
524:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:524]

```
525:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:525]

```
526:      * Generate deterministic nonce for Schnorr signature (RFC 6979 style)
```
> تعليق: توليد قيمة مؤقتة حتميّة لتوقيع شنور (بأسلوب RFC 6979). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:526]

```
527:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:527]

```
528:     private fun generateNonce(privateKey: BigInteger, messageHash: ByteArray, publicKeyBytes: ByteArray): BigInteger {
```
> تُعرَّف دالة خاصّة (private) لتوليد القيمة المؤقتة generateNonce تأخذ مُعامِل المفتاح الخاص (privateKey) من نوع عدد صحيح كبير ومُعامِل بصمة الرسالة من نوع مصفوفة بايت ومُعامِل بايتات المفتاح العام من نوع مصفوفة بايت، وتُعيد عدداً صحيحاً كبيراً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:528]

```
529:         // Simple nonce generation - in production, use RFC 6979
```
> تعليق: توليد قيمة مؤقتة بسيط، وفي الإنتاج استعمل RFC 6979. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:529]

```
530:         // For now, use SHA256(private_key || message || public_key || random)
```
> تعليق: في الوقت الحالي، استعمل SHA256 لـ (المفتاح الخاص متبوعاً بالرسالة متبوعاً بالمفتاح العام متبوعاً بعشوائيّ). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:530]

```
531:         val random = ByteArray(32)
```
> يُعرَّف الثابت العشوائيّ (random) بمصفوفة بايت بطول ٣٢. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:531]

```
532:         secureRandom.nextBytes(random)
```
> يُستدعى nextBytes على المولِّد العشوائيّ الآمن secureRandom لملء المصفوفة العشوائيّة ببايتات. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:532]

```
533:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:533]

```
534:         val privateKeyBytes = privateKey.toByteArray()
```
> يُعرَّف الثابت بايتات المفتاح الخاص بقيمة المفتاح الخاص محوّلاً إلى مصفوفة بايت عبر toByteArray. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:534]

```
535:         val nonceInput = ByteArray(privateKeyBytes.size + messageHash.size + publicKeyBytes.size + random.size)
```
> يُعرَّف الثابت مُدخَل القيمة المؤقتة (nonceInput) بمصفوفة بايت بطول مجموع أحجام بايتات المفتاح الخاص وبصمة الرسالة وبايتات المفتاح العام والعشوائيّ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:535]

```
536:         var offset = 0
```
> يُعرَّف المتغيّر الإزاحة (offset) بقيمة ٠. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:536]

```
537:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:537]

```
538:         System.arraycopy(privateKeyBytes, 0, nonceInput, offset, privateKeyBytes.size)
```
> يُستدعى System.arraycopy لنسخ عدد بايتات يساوي حجم بايتات المفتاح الخاص من بايتات المفتاح الخاص ابتداءً من الموضع ٠ إلى مُدخَل القيمة المؤقتة ابتداءً من الإزاحة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:538]

```
539:         offset += privateKeyBytes.size
```
> تُزاد الإزاحة بمقدار حجم بايتات المفتاح الخاص. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:539]

```
540:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:540]

```
541:         System.arraycopy(messageHash, 0, nonceInput, offset, messageHash.size)
```
> يُستدعى System.arraycopy لنسخ عدد بايتات يساوي حجم بصمة الرسالة من بصمة الرسالة ابتداءً من الموضع ٠ إلى مُدخَل القيمة المؤقتة ابتداءً من الإزاحة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:541]

```
542:         offset += messageHash.size
```
> تُزاد الإزاحة بمقدار حجم بصمة الرسالة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:542]

```
543:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:543]

```
544:         System.arraycopy(publicKeyBytes, 0, nonceInput, offset, publicKeyBytes.size)
```
> يُستدعى System.arraycopy لنسخ عدد بايتات يساوي حجم بايتات المفتاح العام من بايتات المفتاح العام ابتداءً من الموضع ٠ إلى مُدخَل القيمة المؤقتة ابتداءً من الإزاحة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:544]

```
545:         offset += publicKeyBytes.size
```
> تُزاد الإزاحة بمقدار حجم بايتات المفتاح العام. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:545]

```
546:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:546]

```
547:         System.arraycopy(random, 0, nonceInput, offset, random.size)
```
> يُستدعى System.arraycopy لنسخ عدد بايتات يساوي حجم العشوائيّ من العشوائيّ ابتداءً من الموضع ٠ إلى مُدخَل القيمة المؤقتة ابتداءً من الإزاحة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:547]

```
548:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:548]

```
549:         val nonceHash = MessageDigest.getInstance("SHA-256").digest(nonceInput)
```
> يُعرَّف الثابت بصمة القيمة المؤقتة (nonceHash) بقيمة ناتج هضم digest لمُدخَل القيمة المؤقتة عبر مثيل MessageDigest للخوارزمية "SHA-256". [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:549]

```
550:         val nonce = BigInteger(1, nonceHash)
```
> يُعرَّف الثابت القيمة المؤقتة (nonce) بقيمة عدد صحيح كبير موجب الإشارة مبنيّ من بصمة القيمة المؤقتة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:550]

```
551:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:551]

```
552:         // Ensure nonce is in valid range
```
> تعليق: التأكّد من أن القيمة المؤقتة في المدى الصالح. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:552]

```
553:         return if (nonce >= secp256k1Params.n) {
```
> يُعاد ناتج تعبير شرطي إذا كانت القيمة المؤقتة أكبر من أو تساوي n لمعاملات secp256k1Params. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:553]

```
554:             nonce.mod(secp256k1Params.n)
```
> يُعاد القيمة المؤقتة مأخوذة بباقي القسمة mod على n لمعاملات secp256k1Params. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:554]

```
555:         } else {
```
> وإلا إغلاق فرع ثم بداية فرع بديل. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:555]

```
556:             nonce
```
> تُعاد القيمة المؤقتة كما هي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:556]

```
557:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:557]

```
558:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:558]

```
559: }
```
> إغلاق نطاق (نهاية الصنف/الكائن). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:559]
