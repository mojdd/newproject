# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt (الأسطر 201–400)

```
201:         val out = ByteArray(33)
```
> يُعرّف متغيّراً ثابتاً اسمه «out» ويعطيه مصفوفة بايتات (ByteArray) طولها ٣٣ بايت. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:201]

```
202:         out[0] = prefix
```
> يضبط أوّل خانة (الخانة رقم صفر) في المصفوفة «out» على قيمة المتغيّر «prefix» (البادئة). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:202]

```
203:         System.arraycopy(x, 0, out, 1, 32)
```
> يستدعي الدالة «System.arraycopy» لنسخ ٣٢ بايتاً من المصفوفة «x» بدءاً من الموضع صفر، إلى المصفوفة «out» بدءاً من الموضع ١. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:203]

```
204:         return out
```
> يعيد المصفوفة «out». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:204]

```
205:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:205]

```
206:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:206]

```
207:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:207]

```
208:      * NIP-44 v2 key derivation using HKDF-SHA256
```
> تعليق: اشتقاق مفتاح NIP-44 الإصدار الثاني باستخدام HKDF-SHA256. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:208]

```
209:      * salt = empty, info = "nip44-v2", length = 32 bytes
```
> تعليق: الملح (salt) فارغ، والمعلومة (info) هي "nip44-v2"، والطول ٣٢ بايتاً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:209]

```
210:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:210]

```
211:     fun deriveNIP44Key(sharedSecret: ByteArray): ByteArray {
```
> يُعرّف دالة عامة اسمها «deriveNIP44Key» (اشتقاق مفتاح NIP-44) تأخذ معاملاً اسمه «sharedSecret» (السرّ المشترك) من نوع مصفوفة بايتات وتعيد مصفوفة بايتات. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:211]

```
212:         val zeroSalt = ByteArray(0)
```
> يُعرّف متغيّراً ثابتاً اسمه «zeroSalt» (الملح الصفري) ويعطيه مصفوفة بايتات طولها صفر. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:212]

```
213:         val prk = hkdfExtract(zeroSalt, sharedSecret)
```
> يُعرّف متغيّراً ثابتاً اسمه «prk» ويعطيه نتيجة استدعاء الدالة «hkdfExtract» بالمعاملين «zeroSalt» و«sharedSecret». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:213]

```
214:         return hkdfExpand(prk, info = "nip44-v2".toByteArray(Charsets.UTF_8), length = 32)
```
> يعيد نتيجة استدعاء الدالة «hkdfExpand» بالمعامل «prk»، والمعامل «info» مضبوطاً على النص "nip44-v2" محوّلاً إلى بايتات بترميز UTF-8، والمعامل «length» مضبوطاً على ٣٢. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:214]

```
215:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:215]

```
216: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:216]

```
217:     private fun hkdfExtract(salt: ByteArray, ikm: ByteArray): ByteArray {
```
> يُعرّف دالة خاصة (private) اسمها «hkdfExtract» (استخلاص HKDF) تأخذ معاملين «salt» (الملح) و«ikm» من نوع مصفوفة بايتات وتعيد مصفوفة بايتات. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:217]

```
218:         val hmac = HMac(SHA256Digest())
```
> يُعرّف متغيّراً ثابتاً اسمه «hmac» ويعطيه كائن «HMac» منشأً بكائن «SHA256Digest». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:218]

```
219:         hmac.init(KeyParameter(salt))
```
> يستدعي الدالة «init» على الكائن «hmac» بمعامل «KeyParameter» منشأ من «salt». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:219]

```
220:         hmac.update(ikm, 0, ikm.size)
```
> يستدعي الدالة «update» على الكائن «hmac» بالمصفوفة «ikm» من الموضع صفر بطول حجم «ikm». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:220]

```
221:         val prk = ByteArray(hmac.macSize)
```
> يُعرّف متغيّراً ثابتاً اسمه «prk» ويعطيه مصفوفة بايتات طولها قيمة «macSize» الخاصة بالكائن «hmac». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:221]

```
222:         hmac.doFinal(prk, 0)
```
> يستدعي الدالة «doFinal» على الكائن «hmac» ليكتب النتيجة في المصفوفة «prk» بدءاً من الموضع صفر. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:222]

```
223:         return prk
```
> يعيد المصفوفة «prk». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:223]

```
224:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:224]

```
225: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:225]

```
226:     private fun hkdfExpand(prk: ByteArray, info: ByteArray?, length: Int): ByteArray {
```
> يُعرّف دالة خاصة اسمها «hkdfExpand» (توسيع HKDF) تأخذ المعامل «prk» من نوع مصفوفة بايتات، والمعامل «info» من نوع مصفوفة بايتات قابلة لأن تكون فارغة (nullable)، والمعامل «length» (الطول) من نوع عدد صحيح، وتعيد مصفوفة بايتات. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:226]

```
227:         val hmac = HMac(SHA256Digest())
```
> يُعرّف متغيّراً ثابتاً اسمه «hmac» ويعطيه كائن «HMac» منشأً بكائن «SHA256Digest». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:227]

```
228:         hmac.init(KeyParameter(prk))
```
> يستدعي الدالة «init» على الكائن «hmac» بمعامل «KeyParameter» منشأ من «prk». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:228]

```
229:         if (info != null && info.isNotEmpty()) {
```
> يبدأ شرطاً (if): إذا كان «info» غير فارغ (not null) وليس مصفوفة خالية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:229]

```
230:             hmac.update(info, 0, info.size)
```
> يستدعي الدالة «update» على الكائن «hmac» بالمصفوفة «info» من الموضع صفر بطول حجم «info». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:230]

```
231:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:231]

```
232:         hmac.update(byteArrayOf(0x01), 0, 1)
```
> يستدعي الدالة «update» على الكائن «hmac» بمصفوفة بايتات تحوي القيمة 0x01 من الموضع صفر بطول ١. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:232]

```
233:         val t = ByteArray(hmac.macSize)
```
> يُعرّف متغيّراً ثابتاً اسمه «t» ويعطيه مصفوفة بايتات طولها قيمة «macSize» الخاصة بالكائن «hmac». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:233]

```
234:         hmac.doFinal(t, 0)
```
> يستدعي الدالة «doFinal» على الكائن «hmac» ليكتب النتيجة في المصفوفة «t» بدءاً من الموضع صفر. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:234]

```
235:         return t.copyOf(length)
```
> يعيد نسخة من المصفوفة «t» مقتطعة أو ممدودة إلى طول «length». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:235]

```
236:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:236]

```
237: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:237]

```
238:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:238]

```
239:      * NIP-44 v2 encryption using XChaCha20-Poly1305
```
> تعليق: تشفير NIP-44 الإصدار الثاني باستخدام XChaCha20-Poly1305. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:239]

```
240:      * Output format: "v2:" + base64url(nonce24 || ciphertext || tag)
```
> تعليق: صيغة الخرج هي "v2:" متبوعة بترميز base64url لـ (المُعَمَّى ٢٤ بايتاً ثم النص المُشفّر ثم الوسم). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:240]

```
241:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:241]

```
242:     fun encryptNIP44(
```
> يبدأ تعريف دالة عامة اسمها «encryptNIP44» (تشفير NIP-44). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:242]

```
243:         plaintext: String,
```
> معامل اسمه «plaintext» (النص الصريح) من نوع نص (String). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:243]

```
244:         recipientPublicKeyHex: String,
```
> معامل اسمه «recipientPublicKeyHex» (مفتاح المُستقبِل العام بصيغة ست عشرية) من نوع نص. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:244]

```
245:         senderPrivateKeyHex: String
```
> معامل اسمه «senderPrivateKeyHex» (مفتاح المُرسِل الخاص بصيغة ست عشرية) من نوع نص. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:245]

```
246:     ): String {
```
> إغلاق قائمة المعاملات، وتعيد الدالة نصاً (String)، وبداية جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:246]

```
247:         try {
```
> يبدأ كتلة «try» (محاولة). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:247]

```
248:             // Match iOS: derive HKDF input from the compressed shared point (33 bytes)
```
> تعليق: مطابقةً لنظام iOS، اشتقاق مُدخَل HKDF من النقطة المشتركة المضغوطة (٣٣ بايتاً). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:248]

```
249:             val sharedPoint = computeSharedPointWithParity(senderPrivateKeyHex, recipientPublicKeyHex, preferOddY = false)
```
> يُعرّف متغيّراً ثابتاً اسمه «sharedPoint» (النقطة المشتركة) ويعطيه نتيجة استدعاء «computeSharedPointWithParity» بالمعاملين «senderPrivateKeyHex» و«recipientPublicKeyHex» مع ضبط «preferOddY» (تفضيل صادية فردية) على false. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:249]

```
250:             val secretMaterial = compressedPoint(sharedPoint)
```
> يُعرّف متغيّراً ثابتاً اسمه «secretMaterial» (المادّة السرّية) ويعطيه نتيجة استدعاء «compressedPoint» بالمعامل «sharedPoint». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:250]

```
251:             val encryptionKey = deriveNIP44Key(secretMaterial)
```
> يُعرّف متغيّراً ثابتاً اسمه «encryptionKey» (مفتاح التشفير) ويعطيه نتيجة استدعاء «deriveNIP44Key» بالمعامل «secretMaterial». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:251]

```
252:             val aead = XChaCha20Poly1305(encryptionKey)
```
> يُعرّف متغيّراً ثابتاً اسمه «aead» ويعطيه كائن «XChaCha20Poly1305» منشأً بالمفتاح «encryptionKey». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:252]

```
253:             val combined = aead.encrypt(plaintext.toByteArray(Charsets.UTF_8), null) // nonce||ct||tag
```
> يُعرّف متغيّراً ثابتاً اسمه «combined» (المُجمَّع) ويعطيه نتيجة استدعاء «encrypt» على الكائن «aead» بالنص «plaintext» محوّلاً إلى بايتات بترميز UTF-8 ومعامل ثانٍ فارغ (null)؛ تعليق: المُعَمَّى ثم النص المشفّر ثم الوسم. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:253]

```
254:             val b64 = base64UrlNoPad(combined)
```
> يُعرّف متغيّراً ثابتاً اسمه «b64» ويعطيه نتيجة استدعاء «base64UrlNoPad» بالمعامل «combined». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:254]

```
255:             android.util.Log.d("NostrCrypto", "NIP44 v2 encrypt: len=${b64.length}")
```
> يستدعي «android.util.Log.d» بالوسم "NostrCrypto" والرسالة "NIP44 v2 encrypt: len=" مع طول النص «b64». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:255]

```
256:             return "v2:$b64"
```
> يعيد نصاً يتكوّن من "v2:" متبوعاً بقيمة «b64». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:256]

```
257:         } catch (e: Exception) {
```
> يبدأ كتلة «catch» تلتقط استثناءً (Exception) باسم «e». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:257]

```
258:             throw RuntimeException("NIP-44 v2 encryption failed: ${e.message}", e)
```
> يرمي استثناء «RuntimeException» برسالة "NIP-44 v2 encryption failed: " مع رسالة «e»، والسبب «e». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:258]

```
259:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:259]

```
260:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:260]

```
261: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:261]

```
262:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:262]

```
263:      * NIP-44 v2 decryption using XChaCha20-Poly1305
```
> تعليق: فك تشفير NIP-44 الإصدار الثاني باستخدام XChaCha20-Poly1305. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:263]

```
264:      * Only accepts the exact "v2:" base64url format.
```
> تعليق: يقبل فقط صيغة base64url ذات البادئة "v2:" بالضبط. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:264]

```
265:      * Tries both even/odd Y parities for x-only pubkeys.
```
> تعليق: يجرّب كلا تكافؤَي الصادية (الزوجي والفردي) لمفاتيح الخانة العامة ذات السينية فقط (x-only). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:265]

```
266:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:266]

```
267:     fun decryptNIP44(ciphertext: String, senderPublicKeyHex: String, recipientPrivateKeyHex: String): String {
```
> يُعرّف دالة عامة اسمها «decryptNIP44» (فك تشفير NIP-44) تأخذ المعاملات «ciphertext» (النص المشفّر) و«senderPublicKeyHex» (مفتاح المُرسِل العام ست عشرياً) و«recipientPrivateKeyHex» (مفتاح المُستقبِل الخاص ست عشرياً) كنصوص وتعيد نصاً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:267]

```
268:         try {
```
> يبدأ كتلة «try». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:268]

```
269:             require(ciphertext.startsWith("v2:")) { "Invalid NIP-44 version prefix" }
```
> يستدعي «require» مشترطاً أن يبدأ «ciphertext» بالنص "v2:"، وإلا فرسالة الخطأ "Invalid NIP-44 version prefix". [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:269]

```
270:             val encoded = ciphertext.substring(3)
```
> يُعرّف متغيّراً ثابتاً اسمه «encoded» (المُرمَّز) ويعطيه النص الفرعي من «ciphertext» بدءاً من الموضع ٣. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:270]

```
271:             val encryptedData = base64UrlDecode(encoded)
```
> يُعرّف متغيّراً ثابتاً اسمه «encryptedData» (البيانات المشفّرة) ويعطيه نتيجة استدعاء «base64UrlDecode» بالمعامل «encoded». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:271]

```
272:                 ?: throw IllegalArgumentException("Invalid base64url payload")
```
> إذا كانت القيمة فارغة (null) فيرمي استثناء «IllegalArgumentException» برسالة "Invalid base64url payload". [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:272]

```
273: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:273]

```
274:             var lastError: Exception? = null
```
> يُعرّف متغيّراً متبدّلاً (var) اسمه «lastError» (آخر خطأ) من نوع استثناء قابل لأن يكون فارغاً ويبدأ بقيمة null. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:274]

```
275:             // Try even-Y first, then odd-Y
```
> تعليق: جرّب الصادية الزوجية أولاً ثم الصادية الفردية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:275]

```
276:             for (preferOdd in listOf(false, true)) {
```
> يبدأ حلقة «for» يتكرّر فيها المتغيّر «preferOdd» (تفضيل الفردي) على القائمة المكوّنة من false ثم true. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:276]

```
277:                 try {
```
> يبدأ كتلة «try». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:277]

```
278:                     // Match iOS: derive HKDF input from the compressed shared point (33 bytes)
```
> تعليق: مطابقةً لنظام iOS، اشتقاق مُدخَل HKDF من النقطة المشتركة المضغوطة (٣٣ بايتاً). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:278]

```
279:                     val point = computeSharedPointWithParity(recipientPrivateKeyHex, senderPublicKeyHex, preferOddY = preferOdd)
```
> يُعرّف متغيّراً ثابتاً اسمه «point» (النقطة) ويعطيه نتيجة استدعاء «computeSharedPointWithParity» بالمعاملين «recipientPrivateKeyHex» و«senderPublicKeyHex» مع ضبط «preferOddY» على قيمة «preferOdd». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:279]

```
280:                     val secretMaterial = compressedPoint(point)
```
> يُعرّف متغيّراً ثابتاً اسمه «secretMaterial» (المادّة السرّية) ويعطيه نتيجة استدعاء «compressedPoint» بالمعامل «point». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:280]

```
281:                     val key = deriveNIP44Key(secretMaterial)
```
> يُعرّف متغيّراً ثابتاً اسمه «key» (المفتاح) ويعطيه نتيجة استدعاء «deriveNIP44Key» بالمعامل «secretMaterial». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:281]

```
282:                     val aead = XChaCha20Poly1305(key)
```
> يُعرّف متغيّراً ثابتاً اسمه «aead» ويعطيه كائن «XChaCha20Poly1305» منشأً بالمفتاح «key». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:282]

```
283:                     val pt = aead.decrypt(encryptedData, null) // expects nonce||ct||tag
```
> يُعرّف متغيّراً ثابتاً اسمه «pt» ويعطيه نتيجة استدعاء «decrypt» على الكائن «aead» بالمعامل «encryptedData» ومعامل ثانٍ فارغ (null)؛ تعليق: يتوقّع المُعَمَّى ثم النص المشفّر ثم الوسم. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:283]

```
284:                     return String(pt, Charsets.UTF_8)
```
> يعيد نصاً منشأً من المصفوفة «pt» بترميز UTF-8. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:284]

```
285:                 } catch (e: Exception) {
```
> يبدأ كتلة «catch» تلتقط استثناءً باسم «e». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:285]

```
286:                     lastError = e
```
> يضبط المتغيّر «lastError» على قيمة «e». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:286]

```
287:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:287]

```
288:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:288]

```
289:             throw lastError ?: RuntimeException("NIP-44 v2 decryption failed")
```
> يرمي قيمة «lastError»، وإن كانت فارغة (null) فيرمي استثناء «RuntimeException» برسالة "NIP-44 v2 decryption failed". [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:289]

```
290:         } catch (e: Exception) {
```
> يبدأ كتلة «catch» تلتقط استثناءً باسم «e». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:290]

```
291:             throw RuntimeException("NIP-44 v2 decryption failed: ${e.message}", e)
```
> يرمي استثناء «RuntimeException» برسالة "NIP-44 v2 decryption failed: " مع رسالة «e»، والسبب «e». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:291]

```
292:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:292]

```
293:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:293]

```
294: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:294]

```
295:     private fun base64UrlNoPad(data: ByteArray): String {
```
> يُعرّف دالة خاصة اسمها «base64UrlNoPad» (base64url بلا حشو) تأخذ معاملاً اسمه «data» من نوع مصفوفة بايتات وتعيد نصاً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:295]

```
296:         val b64 = android.util.Base64.encodeToString(data, android.util.Base64.NO_WRAP)
```
> يُعرّف متغيّراً ثابتاً اسمه «b64» ويعطيه نتيجة استدعاء «android.util.Base64.encodeToString» بالمعامل «data» والعَلَم «NO_WRAP». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:296]

```
297:         return b64.replace('+', '-').replace('/', '_').replace("=", "")
```
> يعيد النص «b64» بعد استبدال '+' بـ '-' و '/' بـ '_' وحذف علامة '='. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:297]

```
298:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:298]

```
299: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:299]

```
300:     private fun base64UrlDecode(s: String): ByteArray? {
```
> يُعرّف دالة خاصة اسمها «base64UrlDecode» (فك ترميز base64url) تأخذ معاملاً اسمه «s» من نوع نص وتعيد مصفوفة بايتات قابلة لأن تكون فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:300]

```
301:         var str = s.replace('-', '+').replace('_', '/')
```
> يُعرّف متغيّراً متبدّلاً اسمه «str» ويعطيه النص «s» بعد استبدال '-' بـ '+' و '_' بـ '/'. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:301]

```
302:         val pad = (4 - (str.length % 4)) % 4
```
> يُعرّف متغيّراً ثابتاً اسمه «pad» (الحشو) ويعطيه قيمة (٤ ناقص باقي قسمة طول «str» على ٤) ثم باقي قسمة الناتج على ٤. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:302]

```
303:         if (pad > 0) str += "=".repeat(pad)
```
> إذا كان «pad» أكبر من صفر، يضيف إلى «str» علامة '=' مكرّرة بعدد «pad». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:303]

```
304:         return try {
```
> يعيد نتيجة كتلة «try» التالية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:304]

```
305:             android.util.Base64.decode(str, android.util.Base64.NO_WRAP)
```
> يستدعي «android.util.Base64.decode» بالمعامل «str» والعَلَم «NO_WRAP» ويعيد ناتجه. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:305]

```
306:         } catch (_: IllegalArgumentException) {
```
> يبدأ كتلة «catch» تلتقط استثناء «IllegalArgumentException» بلا اسم (متجاهلاً المتغيّر). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:306]

```
307:             null
```
> يعيد قيمة فارغة (null). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:307]

```
308:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:308]

```
309:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:309]

```
310:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:310]

```
311:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:311]

```
312:      * Generate random timestamp offset for privacy (±15 minutes)
```
> تعليق: توليد إزاحة طابع زمني عشوائية لأجل الخصوصية (بحدود ±١٥ دقيقة). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:312]

```
313:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:313]

```
314:     fun randomizeTimestamp(baseTimestamp: Long = System.currentTimeMillis() / 1000): Int {
```
> يُعرّف دالة عامة اسمها «randomizeTimestamp» (عشوَأة الطابع الزمني) تأخذ معاملاً اسمه «baseTimestamp» (الطابع الزمني الأساس) من نوع عدد طويل (Long) بقيمة افتراضية هي الوقت الحالي بالمللي ثانية مقسوماً على ١٠٠٠، وتعيد عدداً صحيحاً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:314]

```
315:         val offset = secureRandom.nextInt(1800) - 900 // ±15 minutes in seconds
```
> يُعرّف متغيّراً ثابتاً اسمه «offset» (الإزاحة) ويعطيه عدداً عشوائياً من «secureRandom» في المدى [صفر، ١٨٠٠) ناقص ٩٠٠؛ تعليق: ±١٥ دقيقة بالثواني. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:315]

```
316:         return (baseTimestamp + offset).toInt()
```
> يعيد مجموع «baseTimestamp» و«offset» محوّلاً إلى عدد صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:316]

```
317:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:317]

```
318:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:318]

```
319:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:319]

```
320:      * Random timestamp up to maxPastSeconds in the past (default 2 days)
```
> تعليق: طابع زمني عشوائي يصل إلى «maxPastSeconds» ثانية في الماضي (افتراضياً يومان). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:320]

```
321:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:321]

```
322:     fun randomizeTimestampUpToPast(maxPastSeconds: Int = 172800): Int {
```
> يُعرّف دالة عامة اسمها «randomizeTimestampUpToPast» (عشوَأة الطابع الزمني حتى الماضي) تأخذ معاملاً اسمه «maxPastSeconds» (أقصى ثوانٍ ماضية) من نوع عدد صحيح بقيمة افتراضية ١٧٢٨٠٠، وتعيد عدداً صحيحاً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:322]

```
323:         val now = (System.currentTimeMillis() / 1000).toInt()
```
> يُعرّف متغيّراً ثابتاً اسمه «now» (الآن) ويعطيه الوقت الحالي بالمللي ثانية مقسوماً على ١٠٠٠ محوّلاً إلى عدد صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:323]

```
324:         val offset = if (maxPastSeconds > 0) secureRandom.nextInt(maxPastSeconds + 1) else 0
```
> يُعرّف متغيّراً ثابتاً اسمه «offset» ويعطيه — إن كان «maxPastSeconds» أكبر من صفر — عدداً عشوائياً من «secureRandom» في المدى [صفر، maxPastSeconds+1)، وإلا صفراً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:324]

```
325:         return now - offset
```
> يعيد «now» ناقص «offset». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:325]

```
326:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:326]

```
327:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:327]

```
328:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:328]

```
329:      * Validate secp256k1 private key
```
> تعليق: التحقّق من صحّة مفتاح secp256k1 الخاص. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:329]

```
330:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:330]

```
331:     fun isValidPrivateKey(privateKeyHex: String): Boolean {
```
> يُعرّف دالة عامة اسمها «isValidPrivateKey» (هل المفتاح الخاص صالح) تأخذ معاملاً اسمه «privateKeyHex» (المفتاح الخاص ست عشرياً) من نوع نص وتعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:331]

```
332:         return try {
```
> يعيد نتيجة كتلة «try» التالية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:332]

```
333:             val privateKeyBytes = privateKeyHex.hexToByteArray()
```
> يُعرّف متغيّراً ثابتاً اسمه «privateKeyBytes» (بايتات المفتاح الخاص) ويعطيه نتيجة استدعاء «hexToByteArray» على «privateKeyHex». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:333]

```
334:             if (privateKeyBytes.size != 32) return false
```
> إذا لم يكن حجم «privateKeyBytes» يساوي ٣٢ يعيد false. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:334]

```
335:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:335]

```
336:             val privateKeyBigInt = BigInteger(1, privateKeyBytes)
```
> يُعرّف متغيّراً ثابتاً اسمه «privateKeyBigInt» (المفتاح الخاص كعدد كبير) ويعطيه كائن «BigInteger» منشأً بالإشارة ١ (موجب) والبايتات «privateKeyBytes». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:336]

```
337:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:337]

```
338:             // Must be less than curve order and greater than 0
```
> تعليق: يجب أن يكون أصغر من رتبة المنحنى وأكبر من صفر. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:338]

```
339:             privateKeyBigInt > BigInteger.ZERO && privateKeyBigInt < secp256k1Params.n
```
> تعبير منطقي: «privateKeyBigInt» أكبر من الصفر «BigInteger.ZERO» وأصغر من «secp256k1Params.n» (رتبة المنحنى). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:339]

```
340:         } catch (e: Exception) {
```
> يبدأ كتلة «catch» تلتقط استثناءً باسم «e». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:340]

```
341:             false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:341]

```
342:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:342]

```
343:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:343]

```
344:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:344]

```
345:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:345]

```
346:      * Validate x-only public key
```
> تعليق: التحقّق من صحّة المفتاح العام ذي السينية فقط (x-only). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:346]

```
347:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:347]

```
348:     fun isValidPublicKey(publicKeyHex: String): Boolean {
```
> يُعرّف دالة عامة اسمها «isValidPublicKey» (هل المفتاح العام صالح) تأخذ معاملاً اسمه «publicKeyHex» (المفتاح العام ست عشرياً) من نوع نص وتعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:348]

```
349:         return try {
```
> يعيد نتيجة كتلة «try» التالية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:349]

```
350:             val publicKeyBytes = publicKeyHex.hexToByteArray()
```
> يُعرّف متغيّراً ثابتاً اسمه «publicKeyBytes» (بايتات المفتاح العام) ويعطيه نتيجة استدعاء «hexToByteArray» على «publicKeyHex». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:350]

```
351:             if (publicKeyBytes.size != 32) return false
```
> إذا لم يكن حجم «publicKeyBytes» يساوي ٣٢ يعيد false. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:351]

```
352:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:352]

```
353:             // Try to recover point
```
> تعليق: حاول استرجاع النقطة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:353]

```
354:             recoverPublicKeyPoint(publicKeyBytes)
```
> يستدعي الدالة «recoverPublicKeyPoint» بالمعامل «publicKeyBytes». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:354]

```
355:             true
```
> يعيد القيمة true. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:355]

```
356:         } catch (e: Exception) {
```
> يبدأ كتلة «catch» تلتقط استثناءً باسم «e». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:356]

```
357:             false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:357]

```
358:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:358]

```
359:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:359]

```
360:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:360]

```
361:     // ==============================================================================
```
> تعليق: سطر فاصل من علامات يساوي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:361]

```
362:     // BIP-340 Schnorr Signatures Implementation
```
> تعليق: تطبيق توقيعات شنور (Schnorr) وفق BIP-340. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:362]

```
363:     // ==============================================================================
```
> تعليق: سطر فاصل من علامات يساوي. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:363]

```
364:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:364]

```
365:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:365]

```
366:      * Tagged hash function for BIP-340
```
> تعليق: دالة التجزئة الموسومة (tagged hash) الخاصة بـ BIP-340. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:366]

```
367:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:367]

```
368:     private fun taggedHash(tag: String, data: ByteArray): ByteArray {
```
> يُعرّف دالة خاصة اسمها «taggedHash» (التجزئة الموسومة) تأخذ معاملاً اسمه «tag» (الوسم) من نوع نص ومعاملاً اسمه «data» من نوع مصفوفة بايتات وتعيد مصفوفة بايتات. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:368]

```
369:         val tagBytes = tag.toByteArray(Charsets.UTF_8)
```
> يُعرّف متغيّراً ثابتاً اسمه «tagBytes» (بايتات الوسم) ويعطيه «tag» محوّلاً إلى بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:369]

```
370:         val tagHash = MessageDigest.getInstance("SHA-256").digest(tagBytes)
```
> يُعرّف متغيّراً ثابتاً اسمه «tagHash» (تجزئة الوسم) ويعطيه ناتج استدعاء «digest» بالمعامل «tagBytes» على نسخة «MessageDigest» من نوع "SHA-256". [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:370]

```
371:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:371]

```
372:         val digest = MessageDigest.getInstance("SHA-256")
```
> يُعرّف متغيّراً ثابتاً اسمه «digest» ويعطيه نسخة «MessageDigest» من نوع "SHA-256". [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:372]

```
373:         digest.update(tagHash)
```
> يستدعي الدالة «update» على الكائن «digest» بالمصفوفة «tagHash». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:373]

```
374:         digest.update(tagHash)
```
> يستدعي الدالة «update» على الكائن «digest» بالمصفوفة «tagHash» (مرّة ثانية). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:374]

```
375:         digest.update(data)
```
> يستدعي الدالة «update» على الكائن «digest» بالمصفوفة «data». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:375]

```
376:         return digest.digest()
```
> يعيد ناتج استدعاء «digest» (بلا معامل) على الكائن «digest». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:376]

```
377:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:377]

```
378:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:378]

```
379:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:379]

```
380:      * Check if y coordinate is even
```
> تعليق: التحقّق إن كان الإحداثي الصادي (y) زوجياً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:380]

```
381:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:381]

```
382:     private fun hasEvenY(point: ECPoint): Boolean {
```
> يُعرّف دالة خاصة اسمها «hasEvenY» (هل الصادية زوجية) تأخذ معاملاً اسمه «point» من نوع «ECPoint» (نقطة على المنحنى الإهليلجي) وتعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:382]

```
383:         val yCoord = point.normalize().yCoord.encoded
```
> يُعرّف متغيّراً ثابتاً اسمه «yCoord» (الإحداثي الصادي) ويعطيه البايتات المُرمَّزة (encoded) للإحداثي الصادي «yCoord» للنقطة «point» بعد تطبيعها (normalize). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:383]

```
384:         return (yCoord[yCoord.size - 1].toInt() and 1) == 0
```
> يعيد نتيجة المقارنة: (البايت الأخير من «yCoord» محوّلاً إلى عدد صحيح ومُطبَّقاً عليه «و» الثنائي مع ١) يساوي صفراً. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:384]

```
385:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:385]

```
386:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:386]

```
387:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:387]

```
388:      * Lift x coordinate to point with even y
```
> تعليق: رفع الإحداثي السيني (x) إلى نقطة ذات صادية زوجية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:388]

```
389:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:389]

```
390:     private fun liftX(xBytes: ByteArray): ECPoint? {
```
> يُعرّف دالة خاصة اسمها «liftX» (رفع السينية) تأخذ معاملاً اسمه «xBytes» (بايتات السينية) من نوع مصفوفة بايتات وتعيد «ECPoint» قابلة لأن تكون فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:390]

```
391:         return try {
```
> يعيد نتيجة كتلة «try» التالية. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:391]

```
392:             val point = recoverPublicKeyPoint(xBytes)
```
> يُعرّف متغيّراً ثابتاً اسمه «point» ويعطيه نتيجة استدعاء «recoverPublicKeyPoint» بالمعامل «xBytes». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:392]

```
393:             val normalizedPoint = point.normalize()
```
> يُعرّف متغيّراً ثابتاً اسمه «normalizedPoint» (النقطة المُطبَّعة) ويعطيه نتيجة استدعاء «normalize» على «point». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:393]

```
394:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:394]

```
395:             if (hasEvenY(normalizedPoint)) {
```
> يبدأ شرطاً (if): إذا كانت «hasEvenY» على «normalizedPoint» صحيحة. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:395]

```
396:                 normalizedPoint
```
> القيمة الناتجة هي «normalizedPoint». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:396]

```
397:             } else {
```
> وإلا (else). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:397]

```
398:                 normalizedPoint.negate()
```
> القيمة الناتجة هي نتيجة استدعاء «negate» (النفي) على «normalizedPoint». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:398]

```
399:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:399]

```
400:         } catch (e: Exception) {
```
> يبدأ كتلة «catch» تلتقط استثناءً باسم «e». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:400]
