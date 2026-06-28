# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt (الأسطر 201–361)

```
201:                     event = minedEvent
```
> يُسنِد (assign) قيمة المتغيّر `minedEvent` (الحدث المُعدَّن) إلى المتغيّر `event` (الحدث). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:201]

```
202:                     val actualDifficulty = NostrProofOfWork.calculateDifficulty(event.id)
```
> يُعرّف ثابتاً محلّياً اسمه `actualDifficulty` (الصعوبة الفعلية) ويضبط قيمته بنتيجة استدعاء الدالة `calculateDifficulty` (حساب الصعوبة) من الكائن `NostrProofOfWork` (إثبات العمل في نوستر) ممرِّراً الوسيط `event.id` (معرّف الحدث). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:202]

```
203:                     Log.d(TAG, "✅ PoW mining successful: target=${powSettings.difficulty}, actual=$actualDifficulty, nonce=${NostrProofOfWork.getNonce(event)}")
```
> يستدعي الدالة `Log.d` (تسجيل تصحيحي) ممرِّراً الوسم `TAG` ونصاً يقول «نجح تعدين إثبات العمل» مع إقحام قيمة `powSettings.difficulty` (الصعوبة الهدف) وقيمة `actualDifficulty` (الصعوبة الفعلية) ونتيجة استدعاء `NostrProofOfWork.getNonce(event)` (الرقم العشوائي للحدث). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:203]

```
204:                 } else {
```
> إغلاق كتلة `if` وبداية فرع `else` (وإلا). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:204]

```
205:                     Log.w(TAG, "❌ PoW mining failed, proceeding without PoW")
```
> يستدعي الدالة `Log.w` (تسجيل تحذيري) ممرِّراً الوسم `TAG` ونصاً يقول «فشل تعدين إثبات العمل، يُتابَع بدون إثبات عمل». [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:205]

```
206:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:206]

```
207:             } finally {
```
> إغلاق كتلة `try` وبداية كتلة `finally` (أخيراً). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:207]

```
208:                 // Always stop mining state when done (success or failure)
```
> تعليق: أوقف دائماً حالة التعدين عند الانتهاء (نجاحاً أو فشلاً). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:208]

```
209:                 PoWPreferenceManager.stopMining()
```
> يستدعي الدالة `stopMining` (إيقاف التعدين) من الكائن `PoWPreferenceManager` (مدير تفضيلات إثبات العمل) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:209]

```
210:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:210]

```
211:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:211]

```
212:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:212]

```
213:         return@withContext senderIdentity.signEvent(event)
```
> يعيد من كتلة `withContext` (داخل السياق) نتيجة استدعاء الدالة `signEvent` (توقيع الحدث) على الكائن `senderIdentity` (هوية المُرسِل) ممرِّراً الوسيط `event` (الحدث). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:213]

```
214:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:214]

```
215:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:215]

```
216:     // MARK: - Private Methods
```
> تعليق: علامة — الدوال الخاصة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:216]

```
217:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:217]

```
218:     private fun createSeal(
```
> يُعرّف دالة خاصة (private) اسمها `createSeal` (إنشاء الختم) وبداية قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:218]

```
219:         rumor: NostrEvent,
```
> يُعرّف معاملاً اسمه `rumor` (الشائعة) من النوع `NostrEvent` (حدث نوستر). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:219]

```
220:         recipientPubkey: String,
```
> يُعرّف معاملاً اسمه `recipientPubkey` (المفتاح العام للمستلِم) من النوع `String` (سلسلة نصية). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:220]

```
221:         senderPrivateKey: String,
```
> يُعرّف معاملاً اسمه `senderPrivateKey` (المفتاح الخاص للمُرسِل) من النوع `String` (سلسلة نصية). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:221]

```
222:         senderPublicKey: String
```
> يُعرّف معاملاً اسمه `senderPublicKey` (المفتاح العام للمُرسِل) من النوع `String` (سلسلة نصية). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:222]

```
223:     ): NostrEvent {
```
> ينهي قائمة المعاملات ويحدّد نوع القيمة المُعادة بأنه `NostrEvent` (حدث نوستر) ويبدأ جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:223]

```
224:         val rumorJSON = gson.toJson(rumor)
```
> يُعرّف ثابتاً محلّياً اسمه `rumorJSON` (شائعة بصيغة JSON) ويضبط قيمته بنتيجة استدعاء الدالة `toJson` على الكائن `gson` ممرِّراً الوسيط `rumor` (الشائعة). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:224]

```
225:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:225]

```
226:         val encrypted = NostrCrypto.encryptNIP44(
```
> يُعرّف ثابتاً محلّياً اسمه `encrypted` (المُعمّى) ويضبط قيمته بنتيجة استدعاء الدالة `encryptNIP44` (تعمية وفق NIP44) من الكائن `NostrCrypto` (تعمية نوستر) وبداية وسائطها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:226]

```
227:             plaintext = rumorJSON,
```
> يمرّر للوسيط المُسمّى `plaintext` (النص الصريح) القيمة `rumorJSON` (الشائعة بصيغة JSON). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:227]

```
228:             recipientPublicKeyHex = recipientPubkey,
```
> يمرّر للوسيط المُسمّى `recipientPublicKeyHex` (المفتاح العام للمستلِم بالنظام الست عشري) القيمة `recipientPubkey` (المفتاح العام للمستلِم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:228]

```
229:             senderPrivateKeyHex = senderPrivateKey
```
> يمرّر للوسيط المُسمّى `senderPrivateKeyHex` (المفتاح الخاص للمُرسِل بالنظام الست عشري) القيمة `senderPrivateKey` (المفتاح الخاص للمُرسِل). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:229]

```
230:         )
```
> إغلاق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:230]

```
231:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:231]

```
232:         val seal = NostrEvent(
```
> يُعرّف ثابتاً محلّياً اسمه `seal` (الختم) ويضبط قيمته بإنشاء كائن `NostrEvent` (حدث نوستر) وبداية وسائط منشئه. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:232]

```
233:             pubkey = senderPublicKey,
```
> يمرّر للوسيط المُسمّى `pubkey` (المفتاح العام) القيمة `senderPublicKey` (المفتاح العام للمُرسِل). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:233]

```
234:             createdAt = NostrCrypto.randomizeTimestampUpToPast(),
```
> يمرّر للوسيط المُسمّى `createdAt` (وقت الإنشاء) نتيجة استدعاء الدالة `randomizeTimestampUpToPast` (تعشية الطابع الزمني إلى الماضي) من الكائن `NostrCrypto` (تعمية نوستر). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:234]

```
235:             kind = NostrKind.SEAL,
```
> يمرّر للوسيط المُسمّى `kind` (النوع) القيمة `SEAL` (الختم) من `NostrKind` (نوع نوستر). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:235]

```
236:             tags = emptyList(),
```
> يمرّر للوسيط المُسمّى `tags` (الوسوم) قائمة فارغة بنتيجة استدعاء `emptyList()`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:236]

```
237:             content = encrypted
```
> يمرّر للوسيط المُسمّى `content` (المحتوى) القيمة `encrypted` (المُعمّى). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:237]

```
238:         )
```
> إغلاق قائمة وسائط منشئ الكائن. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:238]

```
239:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:239]

```
240:         // NIP-17 requires the seal to be signed by the sender identity key.
```
> تعليق: المعيار NIP-17 يتطلّب توقيع الختم بمفتاح هوية المُرسِل. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:240]

```
241:         return seal.sign(senderPrivateKey)
```
> يعيد نتيجة استدعاء الدالة `sign` (توقيع) على الكائن `seal` (الختم) ممرِّراً الوسيط `senderPrivateKey` (المفتاح الخاص للمُرسِل). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:241]

```
242:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:242]

```
243:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:243]

```
244:     private fun createGiftWrap(
```
> يُعرّف دالة خاصة (private) اسمها `createGiftWrap` (إنشاء غلاف الهدية) وبداية قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:244]

```
245:         seal: NostrEvent,
```
> يُعرّف معاملاً اسمه `seal` (الختم) من النوع `NostrEvent` (حدث نوستر). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:245]

```
246:         recipientPubkey: String
```
> يُعرّف معاملاً اسمه `recipientPubkey` (المفتاح العام للمستلِم) من النوع `String` (سلسلة نصية). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:246]

```
247:     ): NostrEvent {
```
> ينهي قائمة المعاملات ويحدّد نوع القيمة المُعادة بأنه `NostrEvent` (حدث نوستر) ويبدأ جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:247]

```
248:         val sealJSON = gson.toJson(seal)
```
> يُعرّف ثابتاً محلّياً اسمه `sealJSON` (الختم بصيغة JSON) ويضبط قيمته بنتيجة استدعاء الدالة `toJson` على الكائن `gson` ممرِّراً الوسيط `seal` (الختم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:248]

```
249:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:249]

```
250:         // Create new ephemeral key for gift wrap
```
> تعليق: أنشئ مفتاحاً عابراً جديداً لغلاف الهدية. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:250]

```
251:         val (wrapPrivateKey, wrapPublicKey) = NostrCrypto.generateKeyPair()
```
> يُعرّف بالتفكيك ثابتين محلّيين اسمهما `wrapPrivateKey` (المفتاح الخاص للغلاف) و`wrapPublicKey` (المفتاح العام للغلاف) ويضبط قيمتهما بنتيجة استدعاء الدالة `generateKeyPair` (توليد زوج المفاتيح) من الكائن `NostrCrypto` (تعمية نوستر). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:251]

```
252:         Log.v(TAG, "Creating gift wrap with ephemeral key")
```
> يستدعي الدالة `Log.v` (تسجيل تفصيلي) ممرِّراً الوسم `TAG` ونصاً يقول «يُنشَأ غلاف الهدية بمفتاح عابر». [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:252]

```
253:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:253]

```
254:         // Encrypt the seal with the new ephemeral key
```
> تعليق: عمِّ الختم بالمفتاح العابر الجديد. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:254]

```
255:         val encrypted = NostrCrypto.encryptNIP44(
```
> يُعرّف ثابتاً محلّياً اسمه `encrypted` (المُعمّى) ويضبط قيمته بنتيجة استدعاء الدالة `encryptNIP44` (تعمية وفق NIP44) من الكائن `NostrCrypto` (تعمية نوستر) وبداية وسائطها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:255]

```
256:             plaintext = sealJSON,
```
> يمرّر للوسيط المُسمّى `plaintext` (النص الصريح) القيمة `sealJSON` (الختم بصيغة JSON). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:256]

```
257:             recipientPublicKeyHex = recipientPubkey,
```
> يمرّر للوسيط المُسمّى `recipientPublicKeyHex` (المفتاح العام للمستلِم بالنظام الست عشري) القيمة `recipientPubkey` (المفتاح العام للمستلِم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:257]

```
258:             senderPrivateKeyHex = wrapPrivateKey
```
> يمرّر للوسيط المُسمّى `senderPrivateKeyHex` (المفتاح الخاص للمُرسِل بالنظام الست عشري) القيمة `wrapPrivateKey` (المفتاح الخاص للغلاف). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:258]

```
259:         )
```
> إغلاق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:259]

```
260:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:260]

```
261:         val giftWrap = NostrEvent(
```
> يُعرّف ثابتاً محلّياً اسمه `giftWrap` (غلاف الهدية) ويضبط قيمته بإنشاء كائن `NostrEvent` (حدث نوستر) وبداية وسائط منشئه. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:261]

```
262:             pubkey = wrapPublicKey,
```
> يمرّر للوسيط المُسمّى `pubkey` (المفتاح العام) القيمة `wrapPublicKey` (المفتاح العام للغلاف). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:262]

```
263:             createdAt = NostrCrypto.randomizeTimestampUpToPast(),
```
> يمرّر للوسيط المُسمّى `createdAt` (وقت الإنشاء) نتيجة استدعاء الدالة `randomizeTimestampUpToPast` (تعشية الطابع الزمني إلى الماضي) من الكائن `NostrCrypto` (تعمية نوستر). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:263]

```
264:             kind = NostrKind.GIFT_WRAP,
```
> يمرّر للوسيط المُسمّى `kind` (النوع) القيمة `GIFT_WRAP` (غلاف الهدية) من `NostrKind` (نوع نوستر). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:264]

```
265:             tags = listOf(listOf("p", recipientPubkey)), // Tag recipient
```
> يمرّر للوسيط المُسمّى `tags` (الوسوم) قائمة تحوي قائمة واحدة عناصرها السلسلة `"p"` والقيمة `recipientPubkey` (المفتاح العام للمستلِم)، مع تعليق: وسم المستلِم. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:265]

```
266:             content = encrypted
```
> يمرّر للوسيط المُسمّى `content` (المحتوى) القيمة `encrypted` (المُعمّى). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:266]

```
267:         )
```
> إغلاق قائمة وسائط منشئ الكائن. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:267]

```
268:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:268]

```
269:         // Sign with the gift wrap ephemeral key
```
> تعليق: وقِّع بمفتاح غلاف الهدية العابر. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:269]

```
270:         return giftWrap.sign(wrapPrivateKey)
```
> يعيد نتيجة استدعاء الدالة `sign` (توقيع) على الكائن `giftWrap` (غلاف الهدية) ممرِّراً الوسيط `wrapPrivateKey` (المفتاح الخاص للغلاف). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:270]

```
271:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:271]

```
272:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:272]

```
273:     private fun unwrapGiftWrap(
```
> يُعرّف دالة خاصة (private) اسمها `unwrapGiftWrap` (فك غلاف الهدية) وبداية قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:273]

```
274:         giftWrap: NostrEvent,
```
> يُعرّف معاملاً اسمه `giftWrap` (غلاف الهدية) من النوع `NostrEvent` (حدث نوستر). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:274]

```
275:         recipientPrivateKey: String
```
> يُعرّف معاملاً اسمه `recipientPrivateKey` (المفتاح الخاص للمستلِم) من النوع `String` (سلسلة نصية). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:275]

```
276:     ): NostrEvent? {
```
> ينهي قائمة المعاملات ويحدّد نوع القيمة المُعادة بأنه `NostrEvent?` (حدث نوستر قابل للعدم) ويبدأ جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:276]

```
277:         Log.d(TAG, "Unwrapping gift wrap; content prefix='${giftWrap.content.take(3)}' length=${giftWrap.content.length}")
```
> يستدعي الدالة `Log.d` (تسجيل تصحيحي) ممرِّراً الوسم `TAG` ونصاً يقول «يُفَكّ غلاف الهدية» مع إقحام أول ثلاثة محارف من `giftWrap.content` بنتيجة `take(3)` وطول المحتوى بقيمة `giftWrap.content.length`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:277]

```
278:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:278]

```
279:         return try {
```
> يعيد قيمة كتلة `try` (محاولة) ويبدأها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:279]

```
280:             val decrypted = NostrCrypto.decryptNIP44(
```
> يُعرّف ثابتاً محلّياً اسمه `decrypted` (المُفكّ تعميته) ويضبط قيمته بنتيجة استدعاء الدالة `decryptNIP44` (فك التعمية وفق NIP44) من الكائن `NostrCrypto` (تعمية نوستر) وبداية وسائطها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:280]

```
281:                 ciphertext = giftWrap.content,
```
> يمرّر للوسيط المُسمّى `ciphertext` (النص المُعمّى) القيمة `giftWrap.content` (محتوى غلاف الهدية). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:281]

```
282:                 senderPublicKeyHex = giftWrap.pubkey,
```
> يمرّر للوسيط المُسمّى `senderPublicKeyHex` (المفتاح العام للمُرسِل بالنظام الست عشري) القيمة `giftWrap.pubkey` (المفتاح العام لغلاف الهدية). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:282]

```
283:                 recipientPrivateKeyHex = recipientPrivateKey
```
> يمرّر للوسيط المُسمّى `recipientPrivateKeyHex` (المفتاح الخاص للمستلِم بالنظام الست عشري) القيمة `recipientPrivateKey` (المفتاح الخاص للمستلِم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:283]

```
284:             )
```
> إغلاق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:284]

```
285:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:285]

```
286:             val jsonElement = JsonParser.parseString(decrypted)
```
> يُعرّف ثابتاً محلّياً اسمه `jsonElement` (عنصر JSON) ويضبط قيمته بنتيجة استدعاء الدالة `parseString` (تحليل السلسلة) من الكائن `JsonParser` (مُحلّل JSON) ممرِّراً الوسيط `decrypted` (المُفكّ تعميته). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:286]

```
287:             if (!jsonElement.isJsonObject) {
```
> يبدأ كتلة شرطية `if` تتحقّق من نفي `jsonElement.isJsonObject` (أي إن لم يكن العنصر كائن JSON). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:287]

```
288:                 Log.w(TAG, "Decrypted gift wrap is not a JSON object")
```
> يستدعي الدالة `Log.w` (تسجيل تحذيري) ممرِّراً الوسم `TAG` ونصاً يقول «غلاف الهدية المُفكّ تعميته ليس كائن JSON». [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:288]

```
289:                 return null
```
> يعيد القيمة `null` (العدم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:289]

```
290:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:290]

```
291:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:291]

```
292:             val jsonObject = jsonElement.asJsonObject
```
> يُعرّف ثابتاً محلّياً اسمه `jsonObject` (كائن JSON) ويضبط قيمته بقيمة `jsonElement.asJsonObject` (تحويل العنصر إلى كائن JSON). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:292]

```
293:             val seal = NostrEvent(
```
> يُعرّف ثابتاً محلّياً اسمه `seal` (الختم) ويضبط قيمته بإنشاء كائن `NostrEvent` (حدث نوستر) وبداية وسائط منشئه. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:293]

```
294:                 id = jsonObject.get("id")?.asString ?: "",
```
> يمرّر للوسيط المُسمّى `id` (المعرّف) قيمة المفتاح `"id"` من `jsonObject` كسلسلة عبر `asString`، أو سلسلة فارغة `""` إن كانت عدماً عبر مُعامل إلفيس `?:`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:294]

```
295:                 pubkey = jsonObject.get("pubkey")?.asString ?: "",
```
> يمرّر للوسيط المُسمّى `pubkey` (المفتاح العام) قيمة المفتاح `"pubkey"` من `jsonObject` كسلسلة عبر `asString`، أو سلسلة فارغة `""` إن كانت عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:295]

```
296:                 createdAt = jsonObject.get("created_at")?.asInt ?: 0,
```
> يمرّر للوسيط المُسمّى `createdAt` (وقت الإنشاء) قيمة المفتاح `"created_at"` من `jsonObject` كعدد صحيح عبر `asInt`، أو القيمة `0` إن كانت عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:296]

```
297:                 kind = jsonObject.get("kind")?.asInt ?: 0,
```
> يمرّر للوسيط المُسمّى `kind` (النوع) قيمة المفتاح `"kind"` من `jsonObject` كعدد صحيح عبر `asInt`، أو القيمة `0` إن كانت عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:297]

```
298:                 tags = parseTagsFromJson(jsonObject.get("tags")?.asJsonArray) ?: emptyList(),
```
> يمرّر للوسيط المُسمّى `tags` (الوسوم) نتيجة استدعاء الدالة `parseTagsFromJson` (تحليل الوسوم من JSON) ممرِّراً قيمة المفتاح `"tags"` من `jsonObject` كمصفوفة JSON عبر `asJsonArray`، أو قائمة فارغة `emptyList()` إن كانت النتيجة عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:298]

```
299:                 content = jsonObject.get("content")?.asString ?: "",
```
> يمرّر للوسيط المُسمّى `content` (المحتوى) قيمة المفتاح `"content"` من `jsonObject` كسلسلة عبر `asString`، أو سلسلة فارغة `""` إن كانت عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:299]

```
300:                 sig = jsonObject.get("sig")?.asString
```
> يمرّر للوسيط المُسمّى `sig` (التوقيع) قيمة المفتاح `"sig"` من `jsonObject` كسلسلة عبر `asString` (قد تكون عدماً). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:300]

```
301:             )
```
> إغلاق قائمة وسائط منشئ الكائن. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:301]

```
302:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:302]

```
303:             Log.v(TAG, "Unwrapped seal with kind: ${seal.kind}")
```
> يستدعي الدالة `Log.v` (تسجيل تفصيلي) ممرِّراً الوسم `TAG` ونصاً يقول «فُكَّ الختم بنوع» مع إقحام قيمة `seal.kind` (نوع الختم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:303]

```
304:             seal
```
> يقيّم التعبير `seal` (الختم) كقيمة أخيرة لكتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:304]

```
305:         } catch (e: Exception) {
```
> إغلاق كتلة `try` وبداية كتلة `catch` (التقاط) تلتقط استثناءً اسمه `e` من النوع `Exception` (استثناء). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:305]

```
306:             Log.w(TAG, "Failed to unwrap gift wrap: ${e.message}")
```
> يستدعي الدالة `Log.w` (تسجيل تحذيري) ممرِّراً الوسم `TAG` ونصاً يقول «فشل فك غلاف الهدية» مع إقحام `e.message` (رسالة الاستثناء). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:306]

```
307:             null
```
> يقيّم القيمة `null` (العدم) كقيمة أخيرة لكتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:307]

```
308:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:308]

```
309:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:309]

```
310:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:310]

```
311:     private fun openSeal(
```
> يُعرّف دالة خاصة (private) اسمها `openSeal` (فتح الختم) وبداية قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:311]

```
312:         seal: NostrEvent,
```
> يُعرّف معاملاً اسمه `seal` (الختم) من النوع `NostrEvent` (حدث نوستر). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:312]

```
313:         recipientPrivateKey: String
```
> يُعرّف معاملاً اسمه `recipientPrivateKey` (المفتاح الخاص للمستلِم) من النوع `String` (سلسلة نصية). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:313]

```
314:     ): NostrEvent? {
```
> ينهي قائمة المعاملات ويحدّد نوع القيمة المُعادة بأنه `NostrEvent?` (حدث نوستر قابل للعدم) ويبدأ جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:314]

```
315:         return try {
```
> يعيد قيمة كتلة `try` (محاولة) ويبدأها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:315]

```
316:             val decrypted = NostrCrypto.decryptNIP44(
```
> يُعرّف ثابتاً محلّياً اسمه `decrypted` (المُفكّ تعميته) ويضبط قيمته بنتيجة استدعاء الدالة `decryptNIP44` (فك التعمية وفق NIP44) من الكائن `NostrCrypto` (تعمية نوستر) وبداية وسائطها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:316]

```
317:                 ciphertext = seal.content,
```
> يمرّر للوسيط المُسمّى `ciphertext` (النص المُعمّى) القيمة `seal.content` (محتوى الختم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:317]

```
318:                 senderPublicKeyHex = seal.pubkey,
```
> يمرّر للوسيط المُسمّى `senderPublicKeyHex` (المفتاح العام للمُرسِل بالنظام الست عشري) القيمة `seal.pubkey` (المفتاح العام للختم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:318]

```
319:                 recipientPrivateKeyHex = recipientPrivateKey
```
> يمرّر للوسيط المُسمّى `recipientPrivateKeyHex` (المفتاح الخاص للمستلِم بالنظام الست عشري) القيمة `recipientPrivateKey` (المفتاح الخاص للمستلِم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:319]

```
320:             )
```
> إغلاق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:320]

```
321:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:321]

```
322:             val jsonElement = JsonParser.parseString(decrypted)
```
> يُعرّف ثابتاً محلّياً اسمه `jsonElement` (عنصر JSON) ويضبط قيمته بنتيجة استدعاء الدالة `parseString` (تحليل السلسلة) من الكائن `JsonParser` (مُحلّل JSON) ممرِّراً الوسيط `decrypted` (المُفكّ تعميته). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:322]

```
323:             if (!jsonElement.isJsonObject) {
```
> يبدأ كتلة شرطية `if` تتحقّق من نفي `jsonElement.isJsonObject` (أي إن لم يكن العنصر كائن JSON). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:323]

```
324:                 Log.w(TAG, "Decrypted seal is not a JSON object")
```
> يستدعي الدالة `Log.w` (تسجيل تحذيري) ممرِّراً الوسم `TAG` ونصاً يقول «الختم المُفكّ تعميته ليس كائن JSON». [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:324]

```
325:                 return null
```
> يعيد القيمة `null` (العدم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:325]

```
326:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:326]

```
327:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:327]

```
328:             val jsonObject = jsonElement.asJsonObject
```
> يُعرّف ثابتاً محلّياً اسمه `jsonObject` (كائن JSON) ويضبط قيمته بقيمة `jsonElement.asJsonObject` (تحويل العنصر إلى كائن JSON). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:328]

```
329:             NostrEvent(
```
> ينشئ كائن `NostrEvent` (حدث نوستر) وبداية وسائط منشئه كقيمة أخيرة لكتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:329]

```
330:                 id = jsonObject.get("id")?.asString ?: "",
```
> يمرّر للوسيط المُسمّى `id` (المعرّف) قيمة المفتاح `"id"` من `jsonObject` كسلسلة عبر `asString`، أو سلسلة فارغة `""` إن كانت عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:330]

```
331:                 pubkey = jsonObject.get("pubkey")?.asString ?: "",
```
> يمرّر للوسيط المُسمّى `pubkey` (المفتاح العام) قيمة المفتاح `"pubkey"` من `jsonObject` كسلسلة عبر `asString`، أو سلسلة فارغة `""` إن كانت عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:331]

```
332:                 createdAt = jsonObject.get("created_at")?.asInt ?: 0,
```
> يمرّر للوسيط المُسمّى `createdAt` (وقت الإنشاء) قيمة المفتاح `"created_at"` من `jsonObject` كعدد صحيح عبر `asInt`، أو القيمة `0` إن كانت عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:332]

```
333:                 kind = jsonObject.get("kind")?.asInt ?: 0,
```
> يمرّر للوسيط المُسمّى `kind` (النوع) قيمة المفتاح `"kind"` من `jsonObject` كعدد صحيح عبر `asInt`، أو القيمة `0` إن كانت عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:333]

```
334:                 tags = parseTagsFromJson(jsonObject.get("tags")?.asJsonArray) ?: emptyList(),
```
> يمرّر للوسيط المُسمّى `tags` (الوسوم) نتيجة استدعاء الدالة `parseTagsFromJson` (تحليل الوسوم من JSON) ممرِّراً قيمة المفتاح `"tags"` من `jsonObject` كمصفوفة JSON عبر `asJsonArray`، أو قائمة فارغة `emptyList()` إن كانت النتيجة عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:334]

```
335:                 content = jsonObject.get("content")?.asString ?: "",
```
> يمرّر للوسيط المُسمّى `content` (المحتوى) قيمة المفتاح `"content"` من `jsonObject` كسلسلة عبر `asString`، أو سلسلة فارغة `""` إن كانت عدماً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:335]

```
336:                 sig = jsonObject.get("sig")?.asString
```
> يمرّر للوسيط المُسمّى `sig` (التوقيع) قيمة المفتاح `"sig"` من `jsonObject` كسلسلة عبر `asString` (قد تكون عدماً). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:336]

```
337:             )
```
> إغلاق قائمة وسائط منشئ الكائن. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:337]

```
338:         } catch (e: Exception) {
```
> إغلاق كتلة `try` وبداية كتلة `catch` (التقاط) تلتقط استثناءً اسمه `e` من النوع `Exception` (استثناء). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:338]

```
339:             Log.w(TAG, "Failed to open seal: ${e.message}")
```
> يستدعي الدالة `Log.w` (تسجيل تحذيري) ممرِّراً الوسم `TAG` ونصاً يقول «فشل فتح الختم» مع إقحام `e.message` (رسالة الاستثناء). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:339]

```
340:             null
```
> يقيّم القيمة `null` (العدم) كقيمة أخيرة لكتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:340]

```
341:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:341]

```
342:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:342]

```
343:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:343]

```
344:     private fun parseTagsFromJson(tagsArray: com.google.gson.JsonArray?): List<List<String>>? {
```
> يُعرّف دالة خاصة (private) اسمها `parseTagsFromJson` (تحليل الوسوم من JSON) تأخذ معاملاً اسمه `tagsArray` (مصفوفة الوسوم) من النوع `com.google.gson.JsonArray?` (مصفوفة JSON قابلة للعدم) وتعيد `List<List<String>>?` (قائمة قوائم سلاسل قابلة للعدم). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:344]

```
345:         if (tagsArray == null) return emptyList()
```
> يبدأ كتلة شرطية `if` تتحقّق من تساوي `tagsArray` (مصفوفة الوسوم) مع `null` (العدم)، وإن تحقّق يعيد قائمة فارغة بنتيجة `emptyList()`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:345]

```
346:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:346]

```
347:         return try {
```
> يعيد قيمة كتلة `try` (محاولة) ويبدأها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:347]

```
348:             tagsArray.map { tagElement ->
```
> يستدعي الدالة `map` (تحويل) على `tagsArray` (مصفوفة الوسوم) مع لامدا معاملها `tagElement` (عنصر الوسم) وبداية جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:348]

```
349:                 if (tagElement.isJsonArray) {
```
> يبدأ كتلة شرطية `if` تتحقّق من `tagElement.isJsonArray` (أي إن كان عنصر الوسم مصفوفة JSON). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:349]

```
350:                     val tagArray = tagElement.asJsonArray
```
> يُعرّف ثابتاً محلّياً اسمه `tagArray` (مصفوفة الوسم) ويضبط قيمته بقيمة `tagElement.asJsonArray` (تحويل عنصر الوسم إلى مصفوفة JSON). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:350]

```
351:                     tagArray.map { it.asString }
```
> يستدعي الدالة `map` (تحويل) على `tagArray` (مصفوفة الوسم) مع لامدا تعيد لكل عنصر قيمته كسلسلة عبر `it.asString`، كقيمة لفرع `if`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:351]

```
352:                 } else {
```
> إغلاق كتلة `if` وبداية فرع `else` (وإلا). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:352]

```
353:                     emptyList()
```
> يقيّم قائمة فارغة بنتيجة `emptyList()` كقيمة لفرع `else`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:353]

```
354:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:354]

```
355:             }
```
> إغلاق نطاق لامدا الدالة `map`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:355]

```
356:         } catch (e: Exception) {
```
> إغلاق كتلة `try` وبداية كتلة `catch` (التقاط) تلتقط استثناءً اسمه `e` من النوع `Exception` (استثناء). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:356]

```
357:             Log.e(TAG, "Failed to parse tags: ${e.message}")
```
> يستدعي الدالة `Log.e` (تسجيل خطأ) ممرِّراً الوسم `TAG` ونصاً يقول «فشل تحليل الوسوم» مع إقحام `e.message` (رسالة الاستثناء). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:357]

```
358:             null
```
> يقيّم القيمة `null` (العدم) كقيمة أخيرة لكتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:358]

```
359:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:359]

```
360:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:360]

```
361: }
```
> إغلاق نطاق الصنف. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:361]
