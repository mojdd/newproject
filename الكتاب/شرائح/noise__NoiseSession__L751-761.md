# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseSession.kt (الأسطر 751–761)

```
751:  * Session-specific errors
```
> تعليق: أخطاء خاصة بالجلسة (Session-specific errors). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:751]

```
752:  */
```
> تعليق: إغلاق كتلة التعليق التوثيقي (نهاية تعليق KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:752]

```
753: sealed class SessionError(message: String, cause: Throwable? = null) : Exception(message, cause) {
```
> يُعرَّف صنف مختوم (sealed class) باسم «خطأ الجلسة» (SessionError) يأخذ معاملاً نصياً اسمه «الرسالة» (message) من نوع String ومعاملاً اسمه «السبب» (cause) من نوع Throwable القابل للإفراغ بقيمة افتراضية null، ويرث من «استثناء» (Exception) ممرراً إليه الرسالة والسبب. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:753]

```
754:     object InvalidState : SessionError("Session in invalid state")
```
> يُعرَّف كائن مفرد (object) باسم «حالة غير صالحة» (InvalidState) يرث من «خطأ الجلسة» (SessionError) ممرراً النص "Session in invalid state". [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:754]

```
755:     object NotEstablished : SessionError("Session not established")
```
> يُعرَّف كائن مفرد (object) باسم «غير مُؤسَّسة» (NotEstablished) يرث من «خطأ الجلسة» (SessionError) ممرراً النص "Session not established". [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:755]

```
756:     object HandshakeFailed : SessionError("Handshake failed")
```
> يُعرَّف كائن مفرد (object) باسم «فشل المصافحة» (HandshakeFailed) يرث من «خطأ الجلسة» (SessionError) ممرراً النص "Handshake failed". [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:756]

```
757:     object EncryptionFailed : SessionError("Encryption failed")
```
> يُعرَّف كائن مفرد (object) باسم «فشل التعمية» (EncryptionFailed) يرث من «خطأ الجلسة» (SessionError) ممرراً النص "Encryption failed". [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:757]

```
758:     object DecryptionFailed : SessionError("Decryption failed")
```
> يُعرَّف كائن مفرد (object) باسم «فشل فكّ التعمية» (DecryptionFailed) يرث من «خطأ الجلسة» (SessionError) ممرراً النص "Decryption failed". [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:758]

```
759:     class HandshakeInitializationFailed(message: String) : SessionError("Handshake initialization failed: $message")
```
> يُعرَّف صنف (class) باسم «فشل تهيئة المصافحة» (HandshakeInitializationFailed) يأخذ معاملاً نصياً اسمه «الرسالة» (message) من نوع String، ويرث من «خطأ الجلسة» (SessionError) ممرراً النص "Handshake initialization failed: $message" المدموج فيه قيمة الرسالة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:759]

```
760:     class NonceExceeded(message: String) : SessionError(message)
```
> يُعرَّف صنف (class) باسم «تجاوز العدد المرّة-واحدة» (NonceExceeded) يأخذ معاملاً نصياً اسمه «الرسالة» (message) من نوع String، ويرث من «خطأ الجلسة» (SessionError) ممرراً إليه الرسالة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:760]

```
761: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:761]
