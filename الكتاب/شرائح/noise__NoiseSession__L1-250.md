# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseSession.kt (الأسطر 1–250)

```
1: package com.bitchat.android.noise
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.noise`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:2]

```
3: import android.util.Log
```
> يستورد (import) صنف التسجيل `Log` من حزمة `android.util`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:3]

```
4: import com.bitchat.android.noise.southernstorm.protocol.*
```
> يستورد كل الأنواع العامة من حزمة البروتوكول `com.bitchat.android.noise.southernstorm.protocol` باستعمال العلامة النجمية `*`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:4]

```
5: import com.bitchat.android.util.toHexString
```
> يستورد الدالة الممتدّة `toHexString` من حزمة `com.bitchat.android.util`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:5]

```
6: import java.security.SecureRandom
```
> يستورد صنف المولّد العشوائي الآمن `SecureRandom` من حزمة `java.security`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:6]

```
7: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:8]

```
9: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:9]

```
10:  * Individual Noise session for a specific peer - REAL IMPLEMENTATION with noise-java
```
> تعليق: «جلسة Noise فردية لنظير محدّد - تنفيذ حقيقي باستعمال noise-java». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:10]

```
11:  * 100% compatible with iOS bitchat Noise Protocol
```
> تعليق: «متوافق ١٠٠٪ مع بروتوكول Noise الخاص بتطبيق bitchat على iOS». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:11]

```
12:  */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:12]

```
13: class NoiseSession(
```
> يعرّف الصنف (class) «جلسة-التشويش» (NoiseSession) ويفتح قائمة معاملات المُنشئ الأساسي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:13]

```
14:     private val peerID: String,
```
> يعرّف خاصية المُنشئ الخاصة «معرّف-النظير» (peerID) من نوع نص `String`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:14]

```
15:     private val isInitiator: Boolean,
```
> يعرّف خاصية المُنشئ الخاصة «هل-هو-البادئ» (isInitiator) من نوع منطقي `Boolean`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:15]

```
16:     private val localStaticPrivateKey: ByteArray,
```
> يعرّف خاصية المُنشئ الخاصة «المفتاح-الخاص-الثابت-المحلي» (localStaticPrivateKey) من نوع مصفوفة بايتات `ByteArray`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:16]

```
17:     private val localStaticPublicKey: ByteArray
```
> يعرّف خاصية المُنشئ الخاصة «المفتاح-العام-الثابت-المحلي» (localStaticPublicKey) من نوع مصفوفة بايتات `ByteArray`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:17]

```
18: ) {
```
> يغلق قائمة معاملات المُنشئ ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:18]

```
19:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:19]

```
20:     companion object {
```
> يفتح الكائن المصاحب (companion object) الذي يحوي الأعضاء الساكنة للصنف. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:20]

```
21:         private const val TAG = "NoiseSession"
```
> يعرّف الثابت الخاص «الوسم» (TAG) ويسند إليه النص الحرفي `"NoiseSession"`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:21]

```
22:         private const val NOISE_XX_PATTERN_LENGTH = 3
```
> يعرّف الثابت الخاص «طول-نمط-XX» (NOISE_XX_PATTERN_LENGTH) ويسند إليه القيمة العددية `3`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:22]

```
23:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:23]

```
24:         // Noise Protocol Configuration (exactly matching iOS)
```
> تعليق: «إعداد بروتوكول Noise (مطابق تماماً لنسخة iOS)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:24]

```
25:         private const val PROTOCOL_NAME = "Noise_XX_25519_ChaChaPoly_SHA256"
```
> يعرّف الثابت الخاص «اسم-البروتوكول» (PROTOCOL_NAME) ويسند إليه النص الحرفي `"Noise_XX_25519_ChaChaPoly_SHA256"`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:25]

```
26:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:26]

```
27:         // Rekey thresholds (same as iOS)
```
> تعليق: «عتبات إعادة-التمفتح (مثل نسخة iOS)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:27]

```
28:         private const val REKEY_TIME_LIMIT = com.bitchat.android.util.AppConstants.Noise.REKEY_TIME_LIMIT_MS // 1 hour
```
> يعرّف الثابت الخاص «حدّ-زمن-إعادة-التمفتح» (REKEY_TIME_LIMIT) ويسند إليه قيمة الثابت `AppConstants.Noise.REKEY_TIME_LIMIT_MS`؛ تعليق: «ساعة واحدة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:28]

```
29:         private const val REKEY_MESSAGE_LIMIT = com.bitchat.android.util.AppConstants.Noise.REKEY_MESSAGE_LIMIT_SESSION // 10k messages
```
> يعرّف الثابت الخاص «حدّ-رسائل-إعادة-التمفتح» (REKEY_MESSAGE_LIMIT) ويسند إليه قيمة الثابت `AppConstants.Noise.REKEY_MESSAGE_LIMIT_SESSION`؛ تعليق: «١٠ آلاف رسالة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:29]

```
30:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:30]

```
31:         // XX Pattern Message Sizes (exactly matching iOS implementation)
```
> تعليق: «أحجام رسائل نمط XX (مطابقة تماماً لتنفيذ iOS)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:31]

```
32:         private const val XX_MESSAGE_1_SIZE = 32      // -> e (ephemeral key only)
```
> يعرّف الثابت الخاص «حجم-رسالة-XX-الأولى» (XX_MESSAGE_1_SIZE) ويسند إليه القيمة `32`؛ تعليق: «-> e (المفتاح الزائل فقط)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:32]

```
33:         private const val XX_MESSAGE_2_SIZE = 96      // <- e, ee, s, es (32 + 48) + 16 (MAC)
```
> يعرّف الثابت الخاص «حجم-رسالة-XX-الثانية» (XX_MESSAGE_2_SIZE) ويسند إليه القيمة `96`؛ تعليق: «<- e, ee, s, es (32 + 48) + 16 (رمز توثيق الرسالة MAC)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:33]

```
34:         private const val XX_MESSAGE_3_SIZE = 48      // -> s, se (encrypted static key)
```
> يعرّف الثابت الخاص «حجم-رسالة-XX-الثالثة» (XX_MESSAGE_3_SIZE) ويسند إليه القيمة `48`؛ تعليق: «-> s, se (المفتاح الثابت المشفّر)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:34]

```
35:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:35]

```
36:         // Maximum payload size for safety
```
> تعليق: «أقصى حجم للحمولة من أجل الأمان». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:36]

```
37:         private const val MAX_PAYLOAD_SIZE = com.bitchat.android.util.AppConstants.Noise.MAX_PAYLOAD_SIZE_BYTES
```
> يعرّف الثابت الخاص «أقصى-حجم-حمولة» (MAX_PAYLOAD_SIZE) ويسند إليه قيمة الثابت `AppConstants.Noise.MAX_PAYLOAD_SIZE_BYTES`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:37]

```
38:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:38]

```
39:         // Constants for replay protection (matching iOS implementation)
```
> تعليق: «ثوابت الحماية من إعادة الإرسال (مطابقة لتنفيذ iOS)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:39]

```
40:         private const val NONCE_SIZE_BYTES = 4
```
> يعرّف الثابت الخاص «حجم-اللاعدد-بالبايتات» (NONCE_SIZE_BYTES) ويسند إليه القيمة `4`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:40]

```
41:         private const val REPLAY_WINDOW_SIZE = 1024
```
> يعرّف الثابت الخاص «حجم-نافذة-إعادة-الإرسال» (REPLAY_WINDOW_SIZE) ويسند إليه القيمة `1024`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:41]

```
42:         private const val REPLAY_WINDOW_BYTES = REPLAY_WINDOW_SIZE / 8 // 128 bytes
```
> يعرّف الثابت الخاص «بايتات-نافذة-إعادة-الإرسال» (REPLAY_WINDOW_BYTES) ويسند إليه ناتج قسمة `REPLAY_WINDOW_SIZE` على `8`؛ تعليق: «128 بايت». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:42]

```
43:         private const val HIGH_NONCE_WARNING_THRESHOLD = com.bitchat.android.util.AppConstants.Noise.HIGH_NONCE_WARNING_THRESHOLD
```
> يعرّف الثابت الخاص «عتبة-تحذير-اللاعدد-المرتفع» (HIGH_NONCE_WARNING_THRESHOLD) ويسند إليه قيمة الثابت `AppConstants.Noise.HIGH_NONCE_WARNING_THRESHOLD`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:43]

```
44:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:44]

```
45:         // MARK: - Sliding Window Replay Protection
```
> تعليق: «MARK: - الحماية من إعادة الإرسال بالنافذة المنزلقة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:45]

```
46:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:46]

```
47:         /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:47]

```
48:          * Check if nonce is valid for replay protection (matching iOS implementation)
```
> تعليق: «تحقّق من صلاحية اللاعدد للحماية من إعادة الإرسال (مطابق لتنفيذ iOS)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:48]

```
49:          */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:49]

```
50:         private fun isValidNonce(receivedNonce: Long, highestReceivedNonce: Long, replayWindow: ByteArray): Boolean {
```
> يعرّف الدالة الخاصة «هل-اللاعدد-صالح» (isValidNonce) التي تأخذ «اللاعدد-المستلَم» (receivedNonce) و«أعلى-لاعدد-مستلَم» (highestReceivedNonce) من نوع `Long` و«نافذة-إعادة-الإرسال» (replayWindow) من نوع `ByteArray`، وتعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:50]

```
51:             if (receivedNonce + REPLAY_WINDOW_SIZE <= highestReceivedNonce) {
```
> شرط: إذا كان مجموع `receivedNonce` و`REPLAY_WINDOW_SIZE` أصغر من أو يساوي `highestReceivedNonce`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:51]

```
52:                 return false  // Too old, outside window
```
> يعيد القيمة `false`؛ تعليق: «قديم جداً، خارج النافذة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:52]

```
53:             }
```
> إغلاق نطاق جملة الشرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:53]

```
54:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:54]

```
55:             if (receivedNonce > highestReceivedNonce) {
```
> شرط: إذا كان `receivedNonce` أكبر من `highestReceivedNonce`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:55]

```
56:                 return true  // Always accept newer nonces
```
> يعيد القيمة `true`؛ تعليق: «اقبل دائماً الأعداد الأحدث». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:56]

```
57:             }
```
> إغلاق نطاق جملة الشرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:57]

```
58:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:58]

```
59:             val offset = (highestReceivedNonce - receivedNonce).toInt()
```
> يعرّف المتغيّر المحلي «الإزاحة» (offset) ويسند إليه الفرق بين `highestReceivedNonce` و`receivedNonce` محوّلاً إلى عدد صحيح بدالة `toInt`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:59]

```
60:             val byteIndex = offset / 8
```
> يعرّف المتغيّر المحلي «فهرس-البايت» (byteIndex) ويسند إليه ناتج قسمة `offset` على `8`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:60]

```
61:             val bitIndex = offset % 8
```
> يعرّف المتغيّر المحلي «فهرس-البِت» (bitIndex) ويسند إليه باقي قسمة `offset` على `8`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:61]

```
62:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:62]

```
63:             return (replayWindow[byteIndex].toInt() and (1 shl bitIndex)) == 0  // Not yet seen
```
> يعيد نتيجة المقارنة: هل ناتج عملية «و» المنطقية البِتية بين البايت في `replayWindow[byteIndex]` (محوّلاً بدالة `toInt`) والقيمة `1` المُزاحة يساراً بمقدار `bitIndex` يساوي صفراً؛ تعليق: «لم يُشاهَد بعد». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:63]

```
64:         }
```
> إغلاق نطاق الدالة `isValidNonce`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:64]

```
65:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:65]

```
66:         /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:66]

```
67:          * Mark nonce as seen in replay window (matching iOS implementation)
```
> تعليق: «علّم اللاعدد كمُشاهَد في نافذة إعادة الإرسال (مطابق لتنفيذ iOS)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:67]

```
68:          */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:68]

```
69:         private fun markNonceAsSeen(receivedNonce: Long, highestReceivedNonce: Long, replayWindow: ByteArray): Pair<Long, ByteArray> {
```
> يعرّف الدالة الخاصة «علّم-اللاعدد-كمُشاهَد» (markNonceAsSeen) التي تأخذ `receivedNonce` و`highestReceivedNonce` من نوع `Long` و`replayWindow` من نوع `ByteArray`، وتعيد زوجاً `Pair<Long, ByteArray>`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:69]

```
70:             var newHighestReceivedNonce = highestReceivedNonce
```
> يعرّف المتغيّر القابل للتغيير «أعلى-لاعدد-مستلَم-جديد» (newHighestReceivedNonce) ويسند إليه قيمة `highestReceivedNonce`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:70]

```
71:             val newReplayWindow = replayWindow.copyOf()
```
> يعرّف المتغيّر المحلي «نافذة-إعادة-إرسال-جديدة» (newReplayWindow) ويسند إليه نسخة من `replayWindow` بدالة `copyOf`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:71]

```
72:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:72]

```
73:             if (receivedNonce > highestReceivedNonce) {
```
> شرط: إذا كان `receivedNonce` أكبر من `highestReceivedNonce`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:73]

```
74:                 val shift = (receivedNonce - highestReceivedNonce).toInt()
```
> يعرّف المتغيّر المحلي «الإزاحة» (shift) ويسند إليه الفرق بين `receivedNonce` و`highestReceivedNonce` محوّلاً بدالة `toInt`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:74]

```
75:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:75]

```
76:                 if (shift >= REPLAY_WINDOW_SIZE) {
```
> شرط: إذا كان `shift` أكبر من أو يساوي `REPLAY_WINDOW_SIZE`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:76]

```
77:                     // Clear entire window - shift is too large
```
> تعليق: «امسح النافذة كاملة - الإزاحة كبيرة جداً». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:77]

```
78:                     newReplayWindow.fill(0)
```
> يملأ المصفوفة `newReplayWindow` كلها بالقيمة `0` بدالة `fill`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:78]

```
79:                 } else {
```
> يغلق نطاق `if` ويفتح نطاق `else`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:79]

```
80:                     // Shift window right by `shift` bits
```
> تعليق: «أزِح النافذة يميناً بمقدار `shift` بِتاً». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:80]

```
81:                     for (i in (REPLAY_WINDOW_BYTES - 1) downTo 0) {
```
> حلقة تكرار `for` بالمتغيّر `i` من `REPLAY_WINDOW_BYTES - 1` تنازلياً (`downTo`) حتى `0`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:81]

```
82:                         val sourceByteIndex = i - shift / 8
```
> يعرّف المتغيّر المحلي «فهرس-بايت-المصدر» (sourceByteIndex) ويسند إليه `i` ناقص ناتج قسمة `shift` على `8`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:82]

```
83:                         var newByte = 0
```
> يعرّف المتغيّر القابل للتغيير «البايت-الجديد» (newByte) ويسند إليه القيمة `0`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:83]

```
84:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:84]

```
85:                         if (sourceByteIndex >= 0) {
```
> شرط: إذا كان `sourceByteIndex` أكبر من أو يساوي `0`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:85]

```
86:                             newByte = (newReplayWindow[sourceByteIndex].toInt() and 0xFF) ushr (shift % 8)
```
> يسند إلى `newByte` ناتج إزاحة بِتية يمينية غير مُوقَّعة (`ushr`) بمقدار باقي قسمة `shift` على `8`، مطبَّقة على البايت `newReplayWindow[sourceByteIndex]` بعد دمجه بـ«و» المنطقية مع `0xFF`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:86]

```
87:                             if (sourceByteIndex > 0 && shift % 8 != 0) {
```
> شرط: إذا كان `sourceByteIndex` أكبر من `0` وكان باقي قسمة `shift` على `8` لا يساوي `0`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:87]

```
88:                                 newByte = newByte or ((newReplayWindow[sourceByteIndex - 1].toInt() and 0xFF) shl (8 - shift % 8))
```
> يسند إلى `newByte` ناتج «أو» المنطقية البِتية بينه وبين البايت `newReplayWindow[sourceByteIndex - 1]` (مدموجاً مع `0xFF`) مُزاحاً يساراً (`shl`) بمقدار `8` ناقص باقي قسمة `shift` على `8`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:88]

```
89:                             }
```
> إغلاق نطاق جملة الشرط `if` الداخلية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:89]

```
90:                         }
```
> إغلاق نطاق جملة الشرط `if` الخاصة بـ`sourceByteIndex >= 0`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:90]

```
91:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:91]

```
92:                         newReplayWindow[i] = (newByte and 0xFF).toByte()
```
> يسند إلى الخانة `newReplayWindow[i]` ناتج «و» المنطقية بين `newByte` و`0xFF` محوّلاً إلى بايت بدالة `toByte`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:92]

```
93:                     }
```
> إغلاق نطاق حلقة `for`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:93]

```
94:                 }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:94]

```
95:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:95]

```
96:                 newHighestReceivedNonce = receivedNonce
```
> يسند إلى `newHighestReceivedNonce` قيمة `receivedNonce`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:96]

```
97:                 newReplayWindow[0] = (newReplayWindow[0].toInt() or 1).toByte()  // Mark most recent bit as seen
```
> يسند إلى الخانة `newReplayWindow[0]` ناتج «أو» المنطقية بين قيمتها الحالية والقيمة `1` محوّلاً إلى بايت؛ تعليق: «علّم البِت الأحدث كمُشاهَد». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:97]

```
98:             } else {
```
> يغلق نطاق `if` ويفتح نطاق `else`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:98]

```
99:                 val offset = (highestReceivedNonce - receivedNonce).toInt()
```
> يعرّف المتغيّر المحلي `offset` ويسند إليه الفرق بين `highestReceivedNonce` و`receivedNonce` محوّلاً بدالة `toInt`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:99]

```
100:                 val byteIndex = offset / 8
```
> يعرّف المتغيّر المحلي `byteIndex` ويسند إليه ناتج قسمة `offset` على `8`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:100]

```
101:                 val bitIndex = offset % 8
```
> يعرّف المتغيّر المحلي `bitIndex` ويسند إليه باقي قسمة `offset` على `8`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:101]

```
102:                 newReplayWindow[byteIndex] = (newReplayWindow[byteIndex].toInt() or (1 shl bitIndex)).toByte()
```
> يسند إلى الخانة `newReplayWindow[byteIndex]` ناتج «أو» المنطقية بين قيمتها الحالية والقيمة `1` المُزاحة يساراً بمقدار `bitIndex` محوّلاً إلى بايت. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:102]

```
103:             }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:103]

```
104:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:104]

```
105:             return Pair(newHighestReceivedNonce, newReplayWindow)
```
> يعيد زوجاً `Pair` يتكوّن من `newHighestReceivedNonce` و`newReplayWindow`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:105]

```
106:         }
```
> إغلاق نطاق الدالة `markNonceAsSeen`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:106]

```
107:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:107]

```
108:         /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:108]

```
109:          * Extract nonce from combined payload <nonce><ciphertext> (matching iOS implementation)
```
> تعليق: «استخرج اللاعدد من الحمولة المجمّعة <لاعدد><نص مشفّر> (مطابق لتنفيذ iOS)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:109]

```
110:          * Returns Pair of (nonce, ciphertext) or null if invalid
```
> تعليق: «يعيد زوجاً من (اللاعدد، النص المشفّر) أو null إذا كان غير صالح». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:110]

```
111:          */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:111]

```
112:         private fun extractNonceFromCiphertextPayload(combinedPayload: ByteArray): Pair<Long, ByteArray>? {
```
> يعرّف الدالة الخاصة «استخرج-اللاعدد-من-حمولة-النص-المشفّر» (extractNonceFromCiphertextPayload) التي تأخذ «الحمولة-المجمّعة» (combinedPayload) من نوع `ByteArray`، وتعيد زوجاً `Pair<Long, ByteArray>` قابلاً لأن يكون فارغاً (`?`). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:112]

```
113:             if (combinedPayload.size < NONCE_SIZE_BYTES) {
```
> شرط: إذا كان حجم `combinedPayload` أصغر من `NONCE_SIZE_BYTES`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:113]

```
114:                 Log.w(TAG, "Combined payload too small: ${combinedPayload.size} < $NONCE_SIZE_BYTES")
```
> يسجّل تحذيراً (`Log.w`) بالوسم `TAG` ونصّ «Combined payload too small» مع إدراج حجم الحمولة وقيمة `NONCE_SIZE_BYTES`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:114]

```
115:                 throw Exception("Combined payload too small: ${combinedPayload.size} < $NONCE_SIZE_BYTES")
```
> يرمي استثناءً (`Exception`) برسالة «Combined payload too small» مع إدراج حجم الحمولة وقيمة `NONCE_SIZE_BYTES`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:115]

```
116:             }
```
> إغلاق نطاق جملة الشرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:116]

```
117:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:117]

```
118:             try {
```
> يفتح كتلة المحاولة `try`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:118]

```
119:                 // Extract 4-byte nonce (big-endian)
```
> تعليق: «استخرج اللاعدد ذا الأربعة بايتات (ترتيب البايت الكبير big-endian)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:119]

```
120:                 var extractedNonce = 0L
```
> يعرّف المتغيّر القابل للتغيير «اللاعدد-المُستخرَج» (extractedNonce) ويسند إليه القيمة `0L` من نوع `Long`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:120]

```
121:                 for (i in 0 until NONCE_SIZE_BYTES) {
```
> حلقة تكرار `for` بالمتغيّر `i` من `0` حتى `NONCE_SIZE_BYTES` غير شاملة (`until`). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:121]

```
122:                     extractedNonce = (extractedNonce shl 8) or (combinedPayload[i].toLong() and 0xFF)
```
> يسند إلى `extractedNonce` ناتج «أو» المنطقية بين قيمته مُزاحة يساراً بمقدار `8` بِتات والبايت `combinedPayload[i]` (محوّلاً بدالة `toLong` ومدموجاً مع `0xFF`). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:122]

```
123:                 }
```
> إغلاق نطاق حلقة `for`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:123]

```
124:                 // Extract ciphertext (remaining bytes)
```
> تعليق: «استخرج النص المشفّر (البايتات المتبقية)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:124]

```
125:                 val ciphertext = combinedPayload.copyOfRange(NONCE_SIZE_BYTES, combinedPayload.size)
```
> يعرّف المتغيّر المحلي «النص-المشفّر» (ciphertext) ويسند إليه نطاقاً مقطوعاً من `combinedPayload` بدالة `copyOfRange` من `NONCE_SIZE_BYTES` حتى نهاية الحمولة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:125]

```
126:                 Log.d(TAG, "Extracted nonce: $extractedNonce, ciphertext size: ${ciphertext.size}")
```
> يسجّل رسالة تتبّع (`Log.d`) بالوسم `TAG` تعرض `extractedNonce` وحجم `ciphertext`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:126]

```
127:                 return Pair(extractedNonce, ciphertext)
```
> يعيد زوجاً `Pair` يتكوّن من `extractedNonce` و`ciphertext`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:127]

```
128:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:128]

```
129:             } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة الالتقاط `catch` التي تلتقط استثناءً (`Exception`) باسم `e`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:129]

```
130:                 throw Exception("Failed to extract nonce from payload: ${e.message}")
```
> يرمي استثناءً (`Exception`) برسالة «Failed to extract nonce from payload» مع إدراج رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:130]

```
131:             }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:131]

```
132:         }
```
> إغلاق نطاق الدالة `extractNonceFromCiphertextPayload`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:132]

```
133:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:133]

```
134:         /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:134]

```
135:          * Convert nonce to 4-byte array (big-endian) (matching iOS implementation)
```
> تعليق: «حوّل اللاعدد إلى مصفوفة من أربعة بايتات (ترتيب البايت الكبير big-endian) (مطابق لتنفيذ iOS)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:135]

```
136:          */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:136]

```
137:         private fun nonceToBytes(nonce: Long): ByteArray {
```
> يعرّف الدالة الخاصة «اللاعدد-إلى-بايتات» (nonceToBytes) التي تأخذ «اللاعدد» (nonce) من نوع `Long`، وتعيد مصفوفة بايتات `ByteArray`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:137]

```
138:             val bytes = ByteArray(NONCE_SIZE_BYTES)
```
> يعرّف المتغيّر المحلي «البايتات» (bytes) ويسند إليه مصفوفة بايتات جديدة بطول `NONCE_SIZE_BYTES`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:138]

```
139:             var value = nonce
```
> يعرّف المتغيّر القابل للتغيير «القيمة» (value) ويسند إليه قيمة `nonce`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:139]

```
140:             for (i in (NONCE_SIZE_BYTES - 1) downTo 0) {
```
> حلقة تكرار `for` بالمتغيّر `i` من `NONCE_SIZE_BYTES - 1` تنازلياً (`downTo`) حتى `0`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:140]

```
141:                 bytes[i] = (value and 0xFF).toByte()
```
> يسند إلى الخانة `bytes[i]` ناتج «و» المنطقية بين `value` و`0xFF` محوّلاً إلى بايت بدالة `toByte`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:141]

```
142:                 value = value ushr 8
```
> يسند إلى `value` قيمته مُزاحة يميناً بإزاحة غير مُوقَّعة (`ushr`) بمقدار `8` بِتات. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:142]

```
143:             }
```
> إغلاق نطاق حلقة `for`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:143]

```
144:             return bytes
```
> يعيد المصفوفة `bytes`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:144]

```
145:         }
```
> إغلاق نطاق الدالة `nonceToBytes`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:145]

```
146:     }
```
> إغلاق نطاق الكائن المصاحب `companion object`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:146]

```
147:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:147]

```
148:     // Noise Protocol objects
```
> تعليق: «كائنات بروتوكول Noise». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:148]

```
149:     private var handshakeState: HandshakeState? = null
```
> يعرّف الخاصية الخاصة القابلة للتغيير «حالة-المصافحة» (handshakeState) من نوع `HandshakeState` القابل لأن يكون فارغاً، ويسند إليها `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:149]

```
150:     private var sendCipher: CipherState? = null
```
> يعرّف الخاصية الخاصة القابلة للتغيير «مُشفّر-الإرسال» (sendCipher) من نوع `CipherState` القابل لأن يكون فارغاً، ويسند إليها `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:150]

```
151:     private var receiveCipher: CipherState? = null
```
> يعرّف الخاصية الخاصة القابلة للتغيير «مُشفّر-الاستقبال» (receiveCipher) من نوع `CipherState` القابل لأن يكون فارغاً، ويسند إليها `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:151]

```
152:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:152]

```
153:     // Session state
```
> تعليق: «حالة الجلسة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:153]

```
154:     private var state: NoiseSessionState = NoiseSessionState.Uninitialized
```
> يعرّف الخاصية الخاصة القابلة للتغيير «الحالة» (state) من نوع `NoiseSessionState`، ويسند إليها القيمة `NoiseSessionState.Uninitialized` (غير مُهيّأة). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:154]

```
155:     private val creationTime = System.currentTimeMillis()
```
> يعرّف الخاصية الخاصة «زمن-الإنشاء» (creationTime) ويسند إليها الوقت الحالي بالمللي ثانية بدالة `System.currentTimeMillis`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:155]

```
156:     private var handshakeStartMs: Long? = null
```
> يعرّف الخاصية الخاصة القابلة للتغيير «زمن-بدء-المصافحة-بالمللي» (handshakeStartMs) من نوع `Long` القابل لأن يكون فارغاً، ويسند إليها `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:156]

```
157:     private var lastHandshakeActivityMs: Long? = null
```
> يعرّف الخاصية الخاصة القابلة للتغيير «زمن-آخر-نشاط-مصافحة-بالمللي» (lastHandshakeActivityMs) من نوع `Long` القابل لأن يكون فارغاً، ويسند إليها `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:157]

```
158:     private var handshakeMessage1: ByteArray? = null
```
> يعرّف الخاصية الخاصة القابلة للتغيير «رسالة-المصافحة-الأولى» (handshakeMessage1) من نوع `ByteArray` القابل لأن يكون فارغاً، ويسند إليها `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:158]

```
159: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:159]

```
160:     // Session counters
```
> تعليق: «عدّادات الجلسة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:160]

```
161:     private var currentPattern = 0;
```
> يعرّف الخاصية الخاصة القابلة للتغيير «النمط-الحالي» (currentPattern) ويسند إليها القيمة `0`، تنتهي بفاصلة منقوطة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:161]

```
162:     private var messagesSent = 0L
```
> يعرّف الخاصية الخاصة القابلة للتغيير «الرسائل-المُرسَلة» (messagesSent) ويسند إليها القيمة `0L` من نوع `Long`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:162]

```
163:     private var messagesReceived = 0L
```
> يعرّف الخاصية الخاصة القابلة للتغيير «الرسائل-المُستلَمة» (messagesReceived) ويسند إليها القيمة `0L` من نوع `Long`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:163]

```
164:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:164]

```
165:     // Sliding window replay protection (used during transport encryption/decryption)
```
> تعليق: «الحماية من إعادة الإرسال بالنافذة المنزلقة (تُستعمل أثناء تشفير/فكّ تشفير النقل)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:165]

```
166:     private var highestReceivedNonce = 0L
```
> يعرّف الخاصية الخاصة القابلة للتغيير «أعلى-لاعدد-مستلَم» (highestReceivedNonce) ويسند إليها القيمة `0L` من نوع `Long`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:166]

```
167:     private var replayWindow = ByteArray(REPLAY_WINDOW_BYTES)
```
> يعرّف الخاصية الخاصة القابلة للتغيير «نافذة-إعادة-الإرسال» (replayWindow) ويسند إليها مصفوفة بايتات جديدة بطول `REPLAY_WINDOW_BYTES`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:167]

```
168:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:168]

```
169:     // CRITICAL FIX: Enhanced thread safety for cipher operations
```
> تعليق: «إصلاح حرج: أمان مُحسّن للخيوط في عمليات التشفير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:169]

```
170:     // The noise-java CipherState objects are NOT thread-safe. Multiple concurrent
```
> تعليق: «كائنات CipherState في noise-java ليست آمنة للخيوط. عدة عمليات متزامنة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:170]

```
171:     // decrypt/encrypt operations can corrupt the internal nonce state.
```
> تعليق: «لفكّ التشفير/التشفير يمكن أن تُفسد حالة اللاعدد الداخلية». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:171]

```
172:     private val cipherLock = Any() // Dedicated lock for cipher operations
```
> يعرّف الخاصية الخاصة «قفل-التشفير» (cipherLock) ويسند إليها كائناً جديداً من `Any`؛ تعليق: «قفل مخصّص لعمليات التشفير». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:172]

```
173:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:173]

```
174:     // Remote peer information  
```
> تعليق: «معلومات النظير البعيد». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:174]

```
175:     private var remoteStaticPublicKey: ByteArray? = null
```
> يعرّف الخاصية الخاصة القابلة للتغيير «المفتاح-العام-الثابت-البعيد» (remoteStaticPublicKey) من نوع `ByteArray` القابل لأن يكون فارغاً، ويسند إليها `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:175]

```
176:     private var handshakeHash: ByteArray? = null
```
> يعرّف الخاصية الخاصة القابلة للتغيير «بصمة-المصافحة» (handshakeHash) من نوع `ByteArray` القابل لأن يكون فارغاً، ويسند إليها `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:176]

```
177:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:177]

```
178:     // MARK: - Session State
```
> تعليق: «MARK: - حالة الجلسة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:178]

```
179:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:179]

```
180:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:180]

```
181:      * Session states matching iOS implementation
```
> تعليق: «حالات الجلسة المطابقة لتنفيذ iOS». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:181]

```
182:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:182]

```
183:     sealed class NoiseSessionState {
```
> يعرّف الصنف المُغلق (sealed class) «حالة-جلسة-التشويش» (NoiseSessionState) ويفتح جسمه. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:183]

```
184:         object Uninitialized : NoiseSessionState()
```
> يعرّف الكائن المفرد «غير-مُهيّأة» (Uninitialized) الوارث من `NoiseSessionState`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:184]

```
185:         object Handshaking : NoiseSessionState()
```
> يعرّف الكائن المفرد «قيد-المصافحة» (Handshaking) الوارث من `NoiseSessionState`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:185]

```
186:         object Established : NoiseSessionState()
```
> يعرّف الكائن المفرد «مُقامة» (Established) الوارث من `NoiseSessionState`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:186]

```
187:         data class Failed(val error: Throwable) : NoiseSessionState()
```
> يعرّف صنف البيانات «فاشلة» (Failed) الوارث من `NoiseSessionState`، ويحوي الخاصية «الخطأ» (error) من نوع `Throwable`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:187]

```
188:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:188]

```
189:         override fun toString(): String = when (this) {
```
> يعيد تعريف (`override`) الدالة `toString` التي تعيد نصاً `String` عبر تعبير `when` المطبَّق على `this`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:189]

```
190:             is Uninitialized -> "uninitialized"
```
> فرع `when`: إذا كانت الحالة من نوع `Uninitialized` يعيد النص `"uninitialized"`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:190]

```
191:             is Handshaking -> "handshaking"
```
> فرع `when`: إذا كانت الحالة من نوع `Handshaking` يعيد النص `"handshaking"`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:191]

```
192:             is Established -> "established"
```
> فرع `when`: إذا كانت الحالة من نوع `Established` يعيد النص `"established"`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:192]

```
193:             is Failed -> "failed: ${error.message}"
```
> فرع `when`: إذا كانت الحالة من نوع `Failed` يعيد النص `"failed: "` مع إدراج رسالة الخطأ `error.message`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:193]

```
194:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:194]

```
195:     }
```
> إغلاق نطاق الصنف المُغلق `NoiseSessionState`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:195]

```
196:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:196]

```
197:     fun getState(): NoiseSessionState = state
```
> يعرّف الدالة «احصل-على-الحالة» (getState) التي تعيد قيمة الخاصية `state` من نوع `NoiseSessionState`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:197]

```
198:     fun isEstablished(): Boolean = state is NoiseSessionState.Established
```
> يعرّف الدالة «هل-مُقامة» (isEstablished) التي تعيد قيمة منطقية تساوي ما إذا كانت `state` من نوع `NoiseSessionState.Established`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:198]

```
199:     fun isHandshaking(): Boolean = state is NoiseSessionState.Handshaking
```
> يعرّف الدالة «هل-قيد-المصافحة» (isHandshaking) التي تعيد قيمة منطقية تساوي ما إذا كانت `state` من نوع `NoiseSessionState.Handshaking`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:199]

```
200:     fun getCreationTime(): Long = creationTime
```
> يعرّف الدالة «احصل-على-زمن-الإنشاء» (getCreationTime) التي تعيد قيمة الخاصية `creationTime` من نوع `Long`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:200]

```
201:     fun isInitiatorRole(): Boolean = isInitiator
```
> يعرّف الدالة «هل-دور-البادئ» (isInitiatorRole) التي تعيد قيمة الخاصية `isInitiator` المنطقية. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:201]

```
202:     fun getHandshakeStartMs(): Long? = handshakeStartMs
```
> يعرّف الدالة «احصل-على-زمن-بدء-المصافحة» (getHandshakeStartMs) التي تعيد قيمة الخاصية `handshakeStartMs` من نوع `Long` القابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:202]

```
203:     fun getLastHandshakeActivityMs(): Long? = lastHandshakeActivityMs
```
> يعرّف الدالة «احصل-على-زمن-آخر-نشاط-مصافحة» (getLastHandshakeActivityMs) التي تعيد قيمة الخاصية `lastHandshakeActivityMs` من نوع `Long` القابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:203]

```
204: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:204]

```
205:     internal fun getHandshakeMessage1(): ByteArray? = handshakeMessage1?.clone()
```
> يعرّف الدالة الداخلية (`internal`) «احصل-على-رسالة-المصافحة-الأولى» (getHandshakeMessage1) التي تعيد نسخة مستنسخة (`clone`) من الخاصية `handshakeMessage1` إن لم تكن فارغة، من نوع `ByteArray` قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:205]

```
206:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:206]

```
207:     internal fun setLastHandshakeActivityForTest(timestampMs: Long) {
```
> يعرّف الدالة الداخلية (`internal`) «اضبط-آخر-نشاط-مصافحة-للاختبار» (setLastHandshakeActivityForTest) التي تأخذ «الطابع-الزمني-بالمللي» (timestampMs) من نوع `Long`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:207]

```
208:         lastHandshakeActivityMs = timestampMs
```
> يسند إلى الخاصية `lastHandshakeActivityMs` قيمة المعامل `timestampMs`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:208]

```
209:     }
```
> إغلاق نطاق الدالة `setLastHandshakeActivityForTest`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:209]

```
210:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:210]

```
211:     init {
```
> يفتح كتلة التهيئة (`init`) الخاصة بالمُنشئ الأساسي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:211]

```
212:         try {
```
> يفتح كتلة المحاولة `try`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:212]

```
213:             // Validate static keys
```
> تعليق: «تحقّق من المفاتيح الثابتة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:213]

```
214:             validateStaticKeys()
```
> يستدعي الدالة `validateStaticKeys` للتحقّق من المفاتيح الثابتة. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:214]

```
215:             Log.d(TAG, "Created ${if (isInitiator) "initiator" else "responder"} session for $peerID")
```
> يسجّل رسالة تتبّع (`Log.d`) بالوسم `TAG` تعلن إنشاء جلسة بنوع «initiator» إن كان `isInitiator` صحيحاً وإلا «responder»، مع إدراج `peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:215]

```
216:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة الالتقاط `catch` التي تلتقط استثناءً (`Exception`) باسم `e`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:216]

```
217:             state = NoiseSessionState.Failed(e)
```
> يسند إلى الخاصية `state` قيمة `NoiseSessionState.Failed` مُمرّراً إليها الاستثناء `e`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:217]

```
218:             Log.e(TAG, "Failed to initialize Noise session: ${e.message}")
```
> يسجّل رسالة خطأ (`Log.e`) بالوسم `TAG` ونصّ «Failed to initialize Noise session» مع إدراج رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:218]

```
219:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:219]

```
220:     }
```
> إغلاق نطاق كتلة التهيئة `init`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:220]

```
221:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:221]

```
222:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:222]

```
223:      * Validate static keys before using them
```
> تعليق: «تحقّق من المفاتيح الثابتة قبل استعمالها». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:223]

```
224:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:224]

```
225:     private fun validateStaticKeys() {
```
> يعرّف الدالة الخاصة «تحقّق-من-المفاتيح-الثابتة» (validateStaticKeys) ويفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:225]

```
226:         if (localStaticPrivateKey.size != 32) {
```
> شرط: إذا كان حجم `localStaticPrivateKey` لا يساوي `32`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:226]

```
227:             throw IllegalArgumentException("Local static private key must be 32 bytes, got ${localStaticPrivateKey.size}")
```
> يرمي استثناء وسيط غير صالح (`IllegalArgumentException`) برسالة «Local static private key must be 32 bytes» مع إدراج الحجم الفعلي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:227]

```
228:         }
```
> إغلاق نطاق جملة الشرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:228]

```
229:         if (localStaticPublicKey.size != 32) {
```
> شرط: إذا كان حجم `localStaticPublicKey` لا يساوي `32`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:229]

```
230:             throw IllegalArgumentException("Local static public key must be 32 bytes, got ${localStaticPublicKey.size}")
```
> يرمي استثناء وسيط غير صالح (`IllegalArgumentException`) برسالة «Local static public key must be 32 bytes» مع إدراج الحجم الفعلي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:230]

```
231:         }
```
> إغلاق نطاق جملة الشرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:231]

```
232:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:232]

```
233:         // Check for all-zero keys (invalid)
```
> تعليق: «تحقّق من المفاتيح التي كل بايتاتها أصفار (غير صالحة)». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:233]

```
234:         if (localStaticPrivateKey.all { it == 0.toByte() }) {
```
> شرط: إذا كانت كل بايتات `localStaticPrivateKey` تساوي البايت `0` (عبر دالة `all`). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:234]

```
235:             throw IllegalArgumentException("Local static private key cannot be all zeros")
```
> يرمي استثناء وسيط غير صالح (`IllegalArgumentException`) برسالة «Local static private key cannot be all zeros». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:235]

```
236:         }
```
> إغلاق نطاق جملة الشرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:236]

```
237:         if (localStaticPublicKey.all { it == 0.toByte() }) {
```
> شرط: إذا كانت كل بايتات `localStaticPublicKey` تساوي البايت `0` (عبر دالة `all`). [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:237]

```
238:             throw IllegalArgumentException("Local static public key cannot be all zeros")
```
> يرمي استثناء وسيط غير صالح (`IllegalArgumentException`) برسالة «Local static public key cannot be all zeros». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:238]

```
239:         }
```
> إغلاق نطاق جملة الشرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:239]

```
240:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:240]

```
241:         Log.d(TAG, "Static keys validated successfully - private: ${localStaticPrivateKey.size} bytes, public: ${localStaticPublicKey.size} bytes")
```
> يسجّل رسالة تتبّع (`Log.d`) بالوسم `TAG` تعلن نجاح التحقّق من المفاتيح مع إدراج حجمَي المفتاح الخاص والعام. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:241]

```
242:     }
```
> إغلاق نطاق الدالة `validateStaticKeys`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:242]

```
243:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:243]

```
244:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:244]

```
245:      * Initialize the Noise handshake - NOW USES PERSISTENT KEYS with our local fork
```
> تعليق: «هيّئ مصافحة Noise - الآن يستعمل مفاتيح دائمة مع نسختنا المحلية المتفرّعة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:245]

```
246:      * Our local fork properly supports setting pre-existing keys, enabling persistent identity
```
> تعليق: «نسختنا المحلية المتفرّعة تدعم بشكل صحيح ضبط مفاتيح موجودة مسبقاً، ما يتيح هوية دائمة». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:246]

```
247:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:247]

```
248:     private fun initializeNoiseHandshake(role: Int) {
```
> يعرّف الدالة الخاصة «هيّئ-مصافحة-التشويش» (initializeNoiseHandshake) التي تأخذ «الدور» (role) من نوع عدد صحيح `Int`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:248]

```
249:         try {
```
> يفتح كتلة المحاولة `try`. [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:249]

```
250:             Log.d(TAG, "Creating HandshakeState with role: ${if (role == HandshakeState.INITIATOR) "INITIATOR" else "RESPONDER"}")
```
> يسجّل رسالة تتبّع (`Log.d`) بالوسم `TAG` تعلن إنشاء `HandshakeState` بدور «INITIATOR» إن كان `role` يساوي `HandshakeState.INITIATOR` وإلا «RESPONDER». [app/src/main/java/com/bitchat/android/noise/NoiseSession.kt:250]
