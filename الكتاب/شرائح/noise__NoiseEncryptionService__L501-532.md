# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt (الأسطر 501–532)

```
501:             val publicKeyParams = org.bouncycastle.crypto.params.Ed25519PublicKeyParameters(publicKey, 0)
```
> يُعرَّف متغيّر ثابت اسمه (publicKeyParams) ويُسنَد إليه كائن جديد من نوع معاملات المفتاح العام إد٢٥٥١٩ (Ed25519PublicKeyParameters) من مكتبة بَاونسي كاسل، مُنشَأ من مصفوفة البايتات (publicKey) ابتداءً من الموضع 0. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:501]

```
502:             val verifier = org.bouncycastle.crypto.signers.Ed25519Signer()
```
> يُعرَّف متغيّر ثابت اسمه (verifier) ويُسنَد إليه كائن جديد من نوع موقّع إد٢٥٥١٩ (Ed25519Signer) من مكتبة بَاونسي كاسل. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:502]

```
503:             verifier.init(false, publicKeyParams)
```
> يُستدعى التابع (init) على الموقّق (verifier) بالوسيطَين: القيمة المنطقية false ومعاملات المفتاح العام (publicKeyParams). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:503]

```
504:             verifier.update(data, 0, data.size)
```
> يُستدعى التابع (update) على الموقّق (verifier) ليُمرَّر له مصفوفة البيانات (data) ابتداءً من الموضع 0 وبطول يساوي حجم المصفوفة (data.size). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:504]

```
505:             return verifier.verifySignature(signature)
```
> تُعاد القيمة الناتجة من استدعاء التابع (verifySignature) على الموقّق (verifier) مع تمرير مصفوفة التوقيع (signature). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:505]

```
506:         } catch (e: Exception) {
```
> بداية كتلة الالتقاط (catch) التي تلتقط الاستثناء (e) من نوع الاستثناء العام (Exception). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:506]

```
507:             Log.e(TAG, "Failed to verify Ed25519 signature: ${e.message}")
```
> يُستدعى التابع (e) على المُسجِّل (Log) ليُسجَّل رسالة خطأ تحت الوسم (TAG) نصّها "Failed to verify Ed25519 signature: " متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:507]

```
508:             return false
```
> تُعاد القيمة المنطقية false. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:508]

```
509:         }
```
> إغلاق نطاق كتلة الالتقاط (catch). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:509]

```
510:     }
```
> إغلاق نطاق الدالة (verifyWithEd25519). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:510]

```
511: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:511]

```
512:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:512]

```
513:      * Clean shutdown
```
> تعليق: إيقاف تشغيل نظيف. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:513]

```
514:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:514]

```
515:     fun shutdown() {
```
> تُعرَّف دالة عامة اسمها (shutdown) لا تأخذ وسائط ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:515]

```
516:         if (::sessionManager.isInitialized) {
```
> بداية شرط (if) يفحص ما إذا كان مدير الجلسة (sessionManager) قد جرى تهيئته عبر الخاصية (isInitialized). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:516]

```
517:             sessionManager.shutdown()
```
> يُستدعى التابع (shutdown) على مدير الجلسة (sessionManager). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:517]

```
518:         }
```
> إغلاق نطاق شرط (if). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:518]

```
519:         channelEncryption.clear()
```
> يُستدعى التابع (clear) على تشفير القناة (channelEncryption). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:519]

```
520:         // No need to clear fingerprints here - they are managed centrally
```
> تعليق: لا حاجة لمسح البصمات هنا - تُدار مركزياً. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:520]

```
521:     }
```
> إغلاق نطاق الدالة (shutdown). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:521]

```
522: }
```
> إغلاق نطاق الصنف (NoiseEncryptionService). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:522]

```
523: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:523]

```
524: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:524]

```
525:  * Noise-specific errors
```
> تعليق: أخطاء خاصة ببروتوكول نويز. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:525]

```
526:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:526]

```
527: sealed class NoiseEncryptionError(message: String) : Exception(message) {
```
> يُعرَّف صنف مُغلَق (sealed) اسمه خطأ تشفير نويز (NoiseEncryptionError) يأخذ في بانِيه نصاً اسمه (message) ويرث من الاستثناء العام (Exception) مُمرِّراً إليه (message). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:527]

```
528:     object HandshakeRequired : NoiseEncryptionError("Handshake required before encryption")
```
> يُعرَّف كائن مفرد اسمه المصافحة مطلوبة (HandshakeRequired) يرث من خطأ تشفير نويز (NoiseEncryptionError) بالرسالة "Handshake required before encryption". [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:528]

```
529:     object SessionNotEstablished : NoiseEncryptionError("No established Noise session")
```
> يُعرَّف كائن مفرد اسمه الجلسة غير مُنشأة (SessionNotEstablished) يرث من خطأ تشفير نويز (NoiseEncryptionError) بالرسالة "No established Noise session". [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:529]

```
530:     object InvalidMessage : NoiseEncryptionError("Invalid message format")
```
> يُعرَّف كائن مفرد اسمه الرسالة غير صالحة (InvalidMessage) يرث من خطأ تشفير نويز (NoiseEncryptionError) بالرسالة "Invalid message format". [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:530]

```
531:     class HandshakeFailed(cause: Throwable) : NoiseEncryptionError("Handshake failed: ${cause.message}")
```
> يُعرَّف صنف اسمه فشلت المصافحة (HandshakeFailed) يأخذ في بانِيه سبباً اسمه (cause) من نوع القابل للرمي (Throwable) ويرث من خطأ تشفير نويز (NoiseEncryptionError) بالرسالة "Handshake failed: " متبوعةً برسالة السبب (cause.message). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:531]

```
532: }
```
> إغلاق نطاق الصنف المُغلَق (NoiseEncryptionError). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:532]
