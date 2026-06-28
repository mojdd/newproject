# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt (الأسطر 251–271)

```
251:     
```
> سطر فارغ (فيه مسافات فقط). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:251]

```
252:     /**
```
> بداية تعليق توثيق (مثل ورقة تعريف ملصقة فوق الدالة). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:252]

```
253:      * Shutdown manager and clean up all sessions
```
> تعليق: «أوقِف المدير ونظّف كل الجلسات». [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:253]

```
254:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:254]

```
255:     fun shutdown() {
```
> تعريف دالة باسم «الإيقاف» (shutdown) بلا وُسطاء وبلا قيمة مُعادة مذكورة، وفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:255]

```
256:         sessions.values.forEach { it.destroy() }
```
> لكل قيمة من قيم خزانة الجلسات (sessions) يُستدعى عليها التابع «التدمير» (destroy)، أي يُمَرّ على كل واحدة ويُهدمها واحدة واحدة. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:256]

```
257:         sessions.clear()
```
> يُستدعى التابع «المسح» (clear) على خزانة الجلسات (sessions) ليُفرغها كلها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:257]

```
258:         Log.d(TAG, "Noise session manager shut down")
```
> يُستدعى تابع التسجيل التشخيصي (Log.d) بالوسم (TAG) والنص «Noise session manager shut down» (مدير جلسات Noise أُوقِف). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:258]

```
259:     }
```
> إغلاق نطاق دالة الإيقاف (shutdown). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:259]

```
260: }
```
> إغلاق نطاق الصنف المُحتوي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:260]

```
261: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:261]

```
262: /**
```
> بداية تعليق توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:262]

```
263:  * Session-related errors
```
> تعليق: «أخطاء متعلّقة بالجلسة». [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:263]

```
264:  */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:264]

```
265: sealed class NoiseSessionError(message: String, cause: Throwable? = null) : Exception(message, cause) {
```
> تعريف صنف مُغلق (sealed class) باسم «خطأ جلسة Noise» (NoiseSessionError) يأخذ وسيطاً نصياً «الرسالة» (message) ووسيطاً «السبب» (cause) من نوع قابل للرمي (Throwable) قيمته الافتراضية لا شيء (null)، ويرث من «استثناء» (Exception) مُمرّراً إليه الرسالة والسبب، وفتح جسمه. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:265]

```
266:     object SessionNotFound : NoiseSessionError("Session not found")
```
> تعريف كائن مفرد (object) باسم «الجلسة غير موجودة» (SessionNotFound) يرث من «خطأ جلسة Noise» (NoiseSessionError) مُمرّراً إليه النص «Session not found» (الجلسة غير موجودة). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:266]

```
267:     object SessionNotEstablished : NoiseSessionError("Session not established")
```
> تعريف كائن مفرد (object) باسم «الجلسة غير مُقامة» (SessionNotEstablished) يرث من «خطأ جلسة Noise» (NoiseSessionError) مُمرّراً إليه النص «Session not established» (الجلسة غير مُقامة). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:267]

```
268:     object InvalidState : NoiseSessionError("Session in invalid state")
```
> تعريف كائن مفرد (object) باسم «حالة غير صالحة» (InvalidState) يرث من «خطأ جلسة Noise» (NoiseSessionError) مُمرّراً إليه النص «Session in invalid state» (الجلسة في حالة غير صالحة). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:268]

```
269:     object HandshakeFailed : NoiseSessionError("Handshake failed")
```
> تعريف كائن مفرد (object) باسم «فشل المصافحة» (HandshakeFailed) يرث من «خطأ جلسة Noise» (NoiseSessionError) مُمرّراً إليه النص «Handshake failed» (فشلت المصافحة). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:269]

```
270:     object AlreadyEstablished : NoiseSessionError("Session already established")
```
> تعريف كائن مفرد (object) باسم «مُقامة سلفاً» (AlreadyEstablished) يرث من «خطأ جلسة Noise» (NoiseSessionError) مُمرّراً إليه النص «Session already established» (الجلسة مُقامة سلفاً). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:270]

```
271: }
```
> إغلاق نطاق الصنف المُغلق «خطأ جلسة Noise» (NoiseSessionError). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:271]
