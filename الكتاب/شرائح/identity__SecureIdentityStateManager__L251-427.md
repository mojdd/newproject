# شريحة — app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt (الأسطر 251–427)

```
251:         }
```
> إغلاق نطاق كتلة داخلية (غالباً كتلة `synchronized` أو شرط سابق) ضمن دالة أعلى المدى. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:251]

```
252:     }
```
> إغلاق نطاق دالة سابقة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:252]

```
253: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:253]

```
254:     fun getCachedNoiseFingerprint(noiseKeyHex: String): String? {
```
> تعريف دالة «جلب بصمة الضجيج المخزّنة» (getCachedNoiseFingerprint) تأخذ وسيطاً نصياً اسمه `noiseKeyHex` من النوع `String` وتُعيد `String?` (نصاً قابلاً للعدم). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:254]

```
255:         val key = noiseKeyHex.lowercase()
```
> إسناد إلى متغيّر ثابت محلي اسمه «المفتاح» (key) قيمته نتيجة تحويل `noiseKeyHex` إلى أحرف صغيرة عبر `lowercase()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:255]

```
256:         val entries = prefs.getStringSet(KEY_CACHED_NOISE_FINGERPRINTS, emptySet()) ?: return null
```
> إسناد إلى متغيّر محلي «المدخلات» (entries) قيمته مجموعة النصوص المخزّنة في التفضيلات `prefs` تحت المفتاح الثابت `KEY_CACHED_NOISE_FINGERPRINTS` بقيمة افتراضية مجموعة فارغة، وإن كانت النتيجة عدماً تُعيد الدالة `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:256]

```
257:         val entry = entries.firstOrNull { it.startsWith("$key=") } ?: return null
```
> إسناد إلى متغيّر محلي «المدخلة» (entry) قيمته أول عنصر في `entries` يبدأ بالنص `"$key="`، وإن لم يوجد تُعيد الدالة `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:257]

```
258:         return entry.substringAfter('=').takeIf { isValidFingerprint(it) }
```
> تُعيد الدالة الجزء النصي الواقع بعد أول `=` من `entry`، شريطة أن يجتاز فحص «بصمة صحيحة» (isValidFingerprint)، وإلا تُعيد `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:258]

```
259:     }
```
> إغلاق نطاق الدالة `getCachedNoiseFingerprint`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:259]

```
260: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:260]

```
261:     fun cacheNoiseFingerprint(noiseKeyHex: String, fingerprint: String) {
```
> تعريف دالة «تخزين بصمة الضجيج» (cacheNoiseFingerprint) تأخذ وسيطين نصيين `noiseKeyHex` و`fingerprint` ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:261]

```
262:         if (!isValidFingerprint(fingerprint)) return
```
> شرط: إن لم يكن `fingerprint` بصمة صحيحة حسب `isValidFingerprint` تخرج الدالة فوراً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:262]

```
263:         if (!noiseKeyHex.matches(Regex("^[a-fA-F0-9]{64}$"))) return
```
> شرط: إن لم يطابق `noiseKeyHex` التعبير النمطي `^[a-fA-F0-9]{64}$` (أربعة وستون رمزاً ست عشرياً بالضبط) تخرج الدالة فوراً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:263]

```
264:         val key = noiseKeyHex.lowercase()
```
> إسناد إلى متغيّر محلي `key` قيمته `noiseKeyHex` محوّلاً إلى أحرف صغيرة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:264]

```
265:         synchronized(lock) {
```
> بدء كتلة متزامنة `synchronized` على كائن القفل `lock` لمنع التداخل بين الخيوط. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:265]

```
266:             val current = prefs.getStringSet(KEY_CACHED_NOISE_FINGERPRINTS, emptySet())?.toMutableSet() ?: mutableSetOf()
```
> إسناد إلى متغيّر محلي «الحالي» (current) قيمته مجموعة النصوص المخزّنة تحت `KEY_CACHED_NOISE_FINGERPRINTS` محوّلة إلى مجموعة قابلة للتعديل عبر `toMutableSet()`، وإن كانت عدماً فمجموعة فارغة قابلة للتعديل عبر `mutableSetOf()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:266]

```
267:             current.removeAll { it.startsWith("$key=") }
```
> حذف كل عنصر من `current` يبدأ بالنص `"$key="` عبر `removeAll`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:267]

```
268:             current.add("$key=$fingerprint")
```
> إضافة العنصر النصي `"$key=$fingerprint"` إلى المجموعة `current`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:268]

```
269:             prefs.edit { putStringSet(KEY_CACHED_NOISE_FINGERPRINTS, current) }
```
> تحرير التفضيلات `prefs` لكتابة مجموعة النصوص `current` تحت المفتاح `KEY_CACHED_NOISE_FINGERPRINTS` عبر `putStringSet`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:269]

```
270:         }
```
> إغلاق نطاق كتلة `synchronized`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:270]

```
271:     }
```
> إغلاق نطاق الدالة `cacheNoiseFingerprint`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:271]

```
272: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:272]

```
273:     fun getCachedFingerprintNickname(fingerprint: String): String? {
```
> تعريف دالة «جلب اسم اللقب المخزّن للبصمة» (getCachedFingerprintNickname) تأخذ وسيطاً نصياً `fingerprint` وتُعيد `String?`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:273]

```
274:         if (!isValidFingerprint(fingerprint)) return null
```
> شرط: إن لم يكن `fingerprint` بصمة صحيحة تُعيد الدالة `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:274]

```
275:         val key = fingerprint.lowercase()
```
> إسناد إلى متغيّر محلي `key` قيمته `fingerprint` محوّلاً إلى أحرف صغيرة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:275]

```
276:         val entries = prefs.getStringSet(KEY_CACHED_FINGERPRINT_NICKNAMES, emptySet()) ?: return null
```
> إسناد إلى متغيّر محلي `entries` قيمته مجموعة النصوص المخزّنة تحت `KEY_CACHED_FINGERPRINT_NICKNAMES` بقيمة افتراضية مجموعة فارغة، وإن كانت عدماً تُعيد الدالة `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:276]

```
277:         val entry = entries.firstOrNull { it.startsWith("$key=") } ?: return null
```
> إسناد إلى متغيّر محلي `entry` قيمته أول عنصر في `entries` يبدأ بالنص `"$key="`، وإن لم يوجد تُعيد الدالة `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:277]

```
278:         val encoded = entry.substringAfter('=')
```
> إسناد إلى متغيّر محلي «المُرمَّز» (encoded) قيمته الجزء النصي الواقع بعد أول `=` من `entry`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:278]

```
279:         return runCatching {
```
> تُعيد الدالة نتيجة كتلة `runCatching` التي تنفّذ ما يليها وتلتقط أي استثناء. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:279]

```
280:             val bytes = Base64.decode(encoded, Base64.NO_WRAP)
```
> إسناد إلى متغيّر محلي «البايتات» (bytes) قيمته فك ترميز `encoded` من Base64 بالعلم `Base64.NO_WRAP`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:280]

```
281:             String(bytes, Charsets.UTF_8)
```
> إنشاء نص من المصفوفة `bytes` بترميز `UTF_8`، وهو القيمة الأخيرة المُعادة من كتلة `runCatching`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:281]

```
282:         }.getOrNull()
```
> استخراج القيمة الناجحة من نتيجة `runCatching` عبر `getOrNull`، وإن وقع استثناء فالناتج `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:282]

```
283:     }
```
> إغلاق نطاق الدالة `getCachedFingerprintNickname`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:283]

```
284: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:284]

```
285:     fun cacheFingerprintNickname(fingerprint: String, nickname: String) {
```
> تعريف دالة «تخزين اسم اللقب للبصمة» (cacheFingerprintNickname) تأخذ وسيطين نصيين `fingerprint` و«اللقب» (nickname) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:285]

```
286:         if (!isValidFingerprint(fingerprint)) return
```
> شرط: إن لم يكن `fingerprint` بصمة صحيحة تخرج الدالة فوراً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:286]

```
287:         val key = fingerprint.lowercase()
```
> إسناد إلى متغيّر محلي `key` قيمته `fingerprint` محوّلاً إلى أحرف صغيرة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:287]

```
288:         val encoded = Base64.encodeToString(nickname.toByteArray(Charsets.UTF_8), Base64.NO_WRAP)
```
> إسناد إلى متغيّر محلي `encoded` قيمته ترميز بايتات `nickname` (بترميز `UTF_8`) إلى نص Base64 بالعلم `Base64.NO_WRAP`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:288]

```
289:         synchronized(lock) {
```
> بدء كتلة متزامنة `synchronized` على كائن القفل `lock`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:289]

```
290:             val current = prefs.getStringSet(KEY_CACHED_FINGERPRINT_NICKNAMES, emptySet())?.toMutableSet() ?: mutableSetOf()
```
> إسناد إلى متغيّر محلي `current` قيمته مجموعة النصوص المخزّنة تحت `KEY_CACHED_FINGERPRINT_NICKNAMES` محوّلة إلى مجموعة قابلة للتعديل، وإن كانت عدماً فمجموعة فارغة قابلة للتعديل. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:290]

```
291:             current.removeAll { it.startsWith("$key=") }
```
> حذف كل عنصر من `current` يبدأ بالنص `"$key="`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:291]

```
292:             current.add("$key=$encoded")
```
> إضافة العنصر النصي `"$key=$encoded"` إلى المجموعة `current`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:292]

```
293:             prefs.edit { putStringSet(KEY_CACHED_FINGERPRINT_NICKNAMES, current) }
```
> تحرير التفضيلات لكتابة المجموعة `current` تحت المفتاح `KEY_CACHED_FINGERPRINT_NICKNAMES` عبر `putStringSet`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:293]

```
294:         }
```
> إغلاق نطاق كتلة `synchronized`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:294]

```
295:     }
```
> إغلاق نطاق الدالة `cacheFingerprintNickname`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:295]

```
296:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:296]

```
297:     // MARK: - Peer ID Rotation Management (removed)
```
> تعليق: علامة قسم «إدارة تدوير معرّف القرين (أُزيلت)». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:297]

```
298:     // Android now derives peer ID from the persisted Noise identity fingerprint.
```
> تعليق: «أندرويد الآن يشتق معرّف القرين من بصمة هوية الضجيج المحفوظة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:298]

```
299:     // No timed peer ID rotation is performed here.
```
> تعليق: «لا يُجرى هنا أي تدوير زمني لمعرّف القرين». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:299]

```
300:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:300]

```
301:     // MARK: - Identity Validation
```
> تعليق: علامة قسم «التحقق من الهوية». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:301]

```
302:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:302]

```
303:     /**
```
> تعليق توثيقي: بداية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:303]

```
304:      * Validate that a public key is valid for Curve25519
```
> تعليق توثيقي: «التحقق من أن المفتاح العام صالح لمنحنى Curve25519». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:304]

```
305:      */
```
> تعليق توثيقي: نهاية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:305]

```
306:     fun validatePublicKey(publicKey: ByteArray): Boolean {
```
> تعريف دالة «التحقق من المفتاح العام» (validatePublicKey) تأخذ وسيطاً «المفتاح العام» (publicKey) من النوع `ByteArray` وتُعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:306]

```
307:         if (publicKey.size != 32) return false
```
> شرط: إن لم يكن طول `publicKey` يساوي ٣٢ تُعيد الدالة `false`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:307]

```
308:         
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:308]

```
309:         // Check for all-zero key (invalid point)
```
> تعليق: «فحص المفتاح المكوّن من أصفار كلياً (نقطة غير صالحة)». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:309]

```
310:         if (publicKey.all { it == 0.toByte() }) return false
```
> شرط: إن كانت كل بايتات `publicKey` تساوي البايت صفر تُعيد الدالة `false`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:310]

```
311:         
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:311]

```
312:         // Check for other known invalid points
```
> تعليق: «فحص نقاط أخرى معروفة بأنها غير صالحة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:312]

```
313:         val invalidPoints = setOf(
```
> إسناد إلى متغيّر محلي «النقاط غير الصالحة» (invalidPoints) قيمته مجموعة `setOf` تبدأ عناصرها فيما يلي. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:313]

```
314:             ByteArray(32) { 0x00.toByte() }, // All zeros
```
> عنصر أول في المجموعة: مصفوفة بايتات بطول ٣٢ كل عناصرها البايت `0x00`، مع تعليق: «كلها أصفار». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:314]

```
315:             ByteArray(32) { 0xFF.toByte() }, // All ones
```
> عنصر ثانٍ في المجموعة: مصفوفة بايتات بطول ٣٢ كل عناصرها البايت `0xFF`، مع تعليق: «كلها آحاد». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:315]

```
316:             // Add other known invalid Curve25519 points if needed
```
> تعليق: «أضِف نقاط Curve25519 أخرى معروفة بعدم صلاحيتها عند الحاجة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:316]

```
317:         )
```
> إغلاق قائمة وسائط استدعاء `setOf`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:317]

```
318:         
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:318]

```
319:         return !invalidPoints.any { it.contentEquals(publicKey) }
```
> تُعيد الدالة نفي وجود أي عنصر في `invalidPoints` يطابق `publicKey` بمحتواه عبر `contentEquals`؛ أي تُعيد `true` فقط إن لم يطابق أيّ نقطة غير صالحة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:319]

```
320:     }
```
> إغلاق نطاق الدالة `validatePublicKey`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:320]

```
321:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:321]

```
322:     /**
```
> تعليق توثيقي: بداية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:322]

```
323:      * Validate that a private key is valid for Curve25519
```
> تعليق توثيقي: «التحقق من أن المفتاح الخاص صالح لمنحنى Curve25519». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:323]

```
324:      */
```
> تعليق توثيقي: نهاية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:324]

```
325:     fun validatePrivateKey(privateKey: ByteArray): Boolean {
```
> تعريف دالة «التحقق من المفتاح الخاص» (validatePrivateKey) تأخذ وسيطاً «المفتاح الخاص» (privateKey) من النوع `ByteArray` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:325]

```
326:         if (privateKey.size != 32) return false
```
> شرط: إن لم يكن طول `privateKey` يساوي ٣٢ تُعيد الدالة `false`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:326]

```
327:         
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:327]

```
328:         // Check for all-zero key
```
> تعليق: «فحص المفتاح المكوّن من أصفار كلياً». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:328]

```
329:         if (privateKey.all { it == 0.toByte() }) return false
```
> شرط: إن كانت كل بايتات `privateKey` تساوي البايت صفر تُعيد الدالة `false`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:329]

```
330:         
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:330]

```
331:         // Check that clamping bits are correct for Curve25519
```
> تعليق: «التحقق من أن بتات التثبيت (clamping) صحيحة لمنحنى Curve25519». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:331]

```
332:         val clampedKey = privateKey.clone()
```
> إسناد إلى متغيّر محلي «المفتاح المُثبَّت» (clampedKey) قيمته نسخة من `privateKey` عبر `clone()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:332]

```
333:         clampedKey[0] = (clampedKey[0].toInt() and 248).toByte()
```
> إسناد إلى البايت رقم 0 من `clampedKey` نتيجة عملية «و» الثنائية بين قيمته الصحيحة والعدد ٢٤٨ ثم تحويلها إلى بايت. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:333]

```
334:         clampedKey[31] = (clampedKey[31].toInt() and 127).toByte()
```
> إسناد إلى البايت رقم 31 من `clampedKey` نتيجة عملية «و» الثنائية بين قيمته الصحيحة والعدد ١٢٧ ثم تحويلها إلى بايت. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:334]

```
335:         clampedKey[31] = (clampedKey[31].toInt() or 64).toByte()
```
> إسناد إلى البايت رقم 31 من `clampedKey` نتيجة عملية «أو» الثنائية بين قيمته الصحيحة والعدد ٦٤ ثم تحويلها إلى بايت. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:335]

```
336:         
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:336]

```
337:         // After clamping, the key should not be all zeros
```
> تعليق: «بعد التثبيت، يجب ألّا يكون المفتاح كله أصفاراً». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:337]

```
338:         return !clampedKey.all { it == 0.toByte() }
```
> تُعيد الدالة نفي كون كل بايتات `clampedKey` صفراً؛ أي تُعيد `true` إن لم تكن جميعها أصفاراً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:338]

```
339:     }
```
> إغلاق نطاق الدالة `validatePrivateKey`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:339]

```
340:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:340]

```
341:     // MARK: - Debug Information
```
> تعليق: علامة قسم «معلومات التتبّع/التصحيح». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:341]

```
342:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:342]

```
343:     /**
```
> تعليق توثيقي: بداية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:343]

```
344:      * Get debug information about identity state
```
> تعليق توثيقي: «الحصول على معلومات تصحيح عن حالة الهوية». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:344]

```
345:      */
```
> تعليق توثيقي: نهاية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:345]

```
346:     fun getDebugInfo(): String = buildString {
```
> تعريف دالة «جلب معلومات التصحيح» (getDebugInfo) تُعيد `String` بقيمة تُبنى عبر كتلة `buildString`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:346]

```
347:         appendLine("=== Identity State Manager Debug ===")
```
> إلحاق سطر نصي ثابت "=== Identity State Manager Debug ===" إلى النص المبني عبر `appendLine`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:347]

```
348:         
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:348]

```
349:         val hasIdentity = prefs.contains(KEY_STATIC_PRIVATE_KEY)
```
> إسناد إلى متغيّر محلي «يملك هوية» (hasIdentity) قيمته نتيجة فحص احتواء التفضيلات `prefs` على المفتاح `KEY_STATIC_PRIVATE_KEY` عبر `contains`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:349]

```
350:         appendLine("Has identity: $hasIdentity")
```
> إلحاق سطر نصي يدمج العبارة "Has identity: " مع قيمة `hasIdentity`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:350]

```
351:         
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:351]

```
352:         if (hasIdentity) {
```
> بداية كتلة شرطية تُنفَّذ إن كانت `hasIdentity` صحيحة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:352]

```
353:             try {
```
> بداية كتلة `try` لالتقاط الاستثناءات. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:353]

```
354:                 val keyPair = loadStaticKey()
```
> إسناد إلى متغيّر محلي «زوج المفاتيح» (keyPair) قيمته نتيجة استدعاء دالة «تحميل المفتاح الثابت» (loadStaticKey). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:354]

```
355:                 if (keyPair != null) {
```
> بداية كتلة شرطية تُنفَّذ إن لم يكن `keyPair` عدماً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:355]

```
356:                     val fingerprint = generateFingerprint(keyPair.second)
```
> إسناد إلى متغيّر محلي «البصمة» (fingerprint) قيمته نتيجة دالة «توليد البصمة» (generateFingerprint) مطبَّقة على العنصر الثاني من `keyPair` (المفتاح العام). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:356]

```
357:                     appendLine("Identity fingerprint: ${fingerprint.take(16)}...")
```
> إلحاق سطر نصي يدمج العبارة "Identity fingerprint: " مع أول ١٦ رمزاً من `fingerprint` عبر `take(16)` متبوعةً بـ"...". [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:357]

```
358:                     appendLine("Key validation: private=${validatePrivateKey(keyPair.first)}, public=${validatePublicKey(keyPair.second)}")
```
> إلحاق سطر نصي يعرض نتيجة `validatePrivateKey` على العنصر الأول من `keyPair` (المفتاح الخاص) ونتيجة `validatePublicKey` على العنصر الثاني (المفتاح العام). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:358]

```
359:                 }
```
> إغلاق نطاق كتلة الشرط `if (keyPair != null)`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:359]

```
360:             } catch (e: Exception) {
```
> بداية كتلة `catch` تلتقط استثناءً اسمه `e` من النوع `Exception`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:360]

```
361:                 appendLine("Key validation failed: ${e.message}")
```
> إلحاق سطر نصي يدمج العبارة "Key validation failed: " مع رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:361]

```
362:             }
```
> إغلاق نطاق كتلة `try/catch`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:362]

```
363:         }
```
> إغلاق نطاق كتلة الشرط `if (hasIdentity)`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:363]

```
364:     }
```
> إغلاق نطاق كتلة `buildString` وبذلك نهاية الدالة `getDebugInfo`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:364]

```
365:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:365]

```
366:     // MARK: - Emergency Clear
```
> تعليق: علامة قسم «المسح الطارئ». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:366]

```
367:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:367]

```
368:     /**
```
> تعليق توثيقي: بداية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:368]

```
369:      * Clear all identity data (for panic mode)
```
> تعليق توثيقي: «مسح كل بيانات الهوية (لوضع الذعر/panic)». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:369]

```
370:      */
```
> تعليق توثيقي: نهاية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:370]

```
371:     fun clearIdentityData() {
```
> تعريف دالة «مسح بيانات الهوية» (clearIdentityData) لا تأخذ وسائط ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:371]

```
372:         try {
```
> بداية كتلة `try` لالتقاط الاستثناءات. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:372]

```
373:             prefs.edit().clear().apply()
```
> تحرير التفضيلات `prefs` ومسح كل محتواها عبر `clear()` ثم تطبيق التغيير عبر `apply()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:373]

```
374:             Log.w(TAG, "All identity data cleared")
```
> تسجيل رسالة تحذير عبر `Log.w` بالوسم `TAG` ونصها "All identity data cleared". [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:374]

```
375:         } catch (e: Exception) {
```
> بداية كتلة `catch` تلتقط استثناءً اسمه `e` من النوع `Exception`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:375]

```
376:             Log.e(TAG, "Failed to clear identity data: ${e.message}")
```
> تسجيل رسالة خطأ عبر `Log.e` بالوسم `TAG` تدمج العبارة "Failed to clear identity data: " مع رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:376]

```
377:         }
```
> إغلاق نطاق كتلة `try/catch`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:377]

```
378:     }
```
> إغلاق نطاق الدالة `clearIdentityData`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:378]

```
379:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:379]

```
380:     /**
```
> تعليق توثيقي: بداية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:380]

```
381:      * Check if identity data exists
```
> تعليق توثيقي: «التحقق مما إذا كانت بيانات الهوية موجودة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:381]

```
382:      */
```
> تعليق توثيقي: نهاية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:382]

```
383:     fun hasIdentityData(): Boolean {
```
> تعريف دالة «يملك بيانات هوية» (hasIdentityData) لا تأخذ وسائط وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:383]

```
384:         return prefs.contains(KEY_STATIC_PRIVATE_KEY) && prefs.contains(KEY_STATIC_PUBLIC_KEY)
```
> تُعيد الدالة `true` إن احتوت التفضيلات `prefs` على المفتاح `KEY_STATIC_PRIVATE_KEY` وأيضاً المفتاح `KEY_STATIC_PUBLIC_KEY` معاً عبر العامل `&&`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:384]

```
385:     }
```
> إغلاق نطاق الدالة `hasIdentityData`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:385]

```
386:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:386]

```
387:     // MARK: - Public SharedPreferences Access (for favorites and Nostr data)
```
> تعليق: علامة قسم «وصول عام إلى التفضيلات المشتركة (لبيانات المفضّلات وNostr)». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:387]

```
388:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:388]

```
389:     /**
```
> تعليق توثيقي: بداية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:389]

```
390:      * Store a string value in secure preferences
```
> تعليق توثيقي: «تخزين قيمة نصية في التفضيلات الآمنة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:390]

```
391:      */
```
> تعليق توثيقي: نهاية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:391]

```
392:     fun storeSecureValue(key: String, value: String) {
```
> تعريف دالة «تخزين قيمة آمنة» (storeSecureValue) تأخذ وسيطين نصيين «المفتاح» (key) و«القيمة» (value) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:392]

```
393:         prefs.edit().putString(key, value).apply()
```
> تحرير التفضيلات لكتابة القيمة النصية `value` تحت المفتاح `key` عبر `putString` ثم تطبيق التغيير عبر `apply()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:393]

```
394:     }
```
> إغلاق نطاق الدالة `storeSecureValue`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:394]

```
395:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:395]

```
396:     /**
```
> تعليق توثيقي: بداية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:396]

```
397:      * Retrieve a string value from secure preferences
```
> تعليق توثيقي: «استرجاع قيمة نصية من التفضيلات الآمنة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:397]

```
398:      */
```
> تعليق توثيقي: نهاية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:398]

```
399:     fun getSecureValue(key: String): String? {
```
> تعريف دالة «جلب قيمة آمنة» (getSecureValue) تأخذ وسيطاً نصياً `key` وتُعيد `String?`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:399]

```
400:         return prefs.getString(key, null)
```
> تُعيد الدالة القيمة النصية المخزّنة تحت `key` في التفضيلات `prefs` بقيمة افتراضية `null` عبر `getString`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:400]

```
401:     }
```
> إغلاق نطاق الدالة `getSecureValue`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:401]

```
402:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:402]

```
403:     /**
```
> تعليق توثيقي: بداية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:403]

```
404:      * Remove a value from secure preferences
```
> تعليق توثيقي: «إزالة قيمة من التفضيلات الآمنة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:404]

```
405:      */
```
> تعليق توثيقي: نهاية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:405]

```
406:     fun removeSecureValue(key: String) {
```
> تعريف دالة «إزالة قيمة آمنة» (removeSecureValue) تأخذ وسيطاً نصياً `key` ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:406]

```
407:         prefs.edit().remove(key).apply()
```
> تحرير التفضيلات لإزالة المدخلة ذات المفتاح `key` عبر `remove` ثم تطبيق التغيير عبر `apply()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:407]

```
408:     }
```
> إغلاق نطاق الدالة `removeSecureValue`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:408]

```
409:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:409]

```
410:     /**
```
> تعليق توثيقي: بداية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:410]

```
411:      * Check if a key exists in secure preferences
```
> تعليق توثيقي: «التحقق مما إذا كان مفتاح موجوداً في التفضيلات الآمنة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:411]

```
412:      */
```
> تعليق توثيقي: نهاية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:412]

```
413:     fun hasSecureValue(key: String): Boolean {
```
> تعريف دالة «يملك قيمة آمنة» (hasSecureValue) تأخذ وسيطاً نصياً `key` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:413]

```
414:         return prefs.contains(key)
```
> تُعيد الدالة نتيجة فحص احتواء التفضيلات `prefs` على المفتاح `key` عبر `contains`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:414]

```
415:     }
```
> إغلاق نطاق الدالة `hasSecureValue`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:415]

```
416:     
```
> سطر فارغ (يحوي مسافات فقط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:416]

```
417:     /**
```
> تعليق توثيقي: بداية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:417]

```
418:      * Clear specific keys from secure preferences
```
> تعليق توثيقي: «مسح مفاتيح محدّدة من التفضيلات الآمنة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:418]

```
419:      */
```
> تعليق توثيقي: نهاية كتلة تعليق KDoc. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:419]

```
420:     fun clearSecureValues(vararg keys: String) {
```
> تعريف دالة «مسح قيم آمنة» (clearSecureValues) تأخذ عدداً متغيّراً من الوسائط النصية `keys` عبر `vararg` ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:420]

```
421:         val editor = prefs.edit()
```
> إسناد إلى متغيّر محلي «المحرّر» (editor) قيمته كائن تحرير التفضيلات الناتج عن `prefs.edit()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:421]

```
422:         keys.forEach { key ->
```
> بدء حلقة `forEach` تمرّ على كل عنصر من `keys` مسمّاةً إياه `key`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:422]

```
423:             editor.remove(key)
```
> إزالة المدخلة ذات المفتاح `key` من المحرّر `editor` عبر `remove`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:423]

```
424:         }
```
> إغلاق نطاق حلقة `forEach`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:424]

```
425:         editor.apply()
```
> تطبيق التغييرات المتراكمة في المحرّر `editor` عبر `apply()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:425]

```
426:     }
```
> إغلاق نطاق الدالة `clearSecureValues`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:426]

```
427: }
```
> إغلاق نطاق الصنف `SecureIdentityStateManager`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:427]
