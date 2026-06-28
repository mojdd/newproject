# شريحة — app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt (الأسطر 201–400)

```
201:     fun decryptFromPeer(encryptedData: ByteArray, senderPeerID: String): ByteArray? {
```
> تُعرَّف دالة عامة اسمها «فكّ التشفير من القرين» (decryptFromPeer) تأخذ معامِلين: «بيانات مشفّرة» (encryptedData) من نوع مصفوفة بايت، و«معرّف القرين المُرسِل» (senderPeerID) من نوع نص، وتُعيد مصفوفة بايت قابلة لأن تكون فارغة (null). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:201]

```
202:         return try {
```
> تُعيد نتيجة كتلة «حاوِل» (try). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:202]

```
203:             encryptionService.decrypt(encryptedData, senderPeerID)
```
> تُستدعى دالة «فُكّ التشفير» (decrypt) من «خدمة التشفير» (encryptionService) بتمرير البيانات المشفّرة ومعرّف القرين المُرسِل، وتُعاد قيمتها. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:203]

```
204:         } catch (e: Exception) {
```
> تُلتقط حالة استثناء (Exception) باسم «e». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:204]

```
205:             Log.e(TAG, "Failed to decrypt from $senderPeerID: ${e.message}")
```
> يُسجَّل خطأ عبر Log.e بوسم TAG ونصّ «فشل فكّ التشفير من» متبوعاً بمعرّف القرين المُرسِل ثمّ رسالة الاستثناء. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:205]

```
206:             null
```
> تُعاد القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:206]

```
207:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:207]

```
208:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:208]

```
209:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:209]

```
210:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:210]

```
211:      * Get combined public key data for key exchange
```
> تعليق: احصل على بيانات المفتاح العام المجمَّعة لتبادل المفاتيح. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:211]

```
212:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:212]

```
213:     fun getCombinedPublicKeyData(): ByteArray {
```
> تُعرَّف دالة عامة اسمها «احصل على بيانات المفتاح العام المجمَّعة» (getCombinedPublicKeyData) لا تأخذ معامِلات وتُعيد مصفوفة بايت. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:213]

```
214:         return encryptionService.getCombinedPublicKeyData()
```
> تُستدعى دالة «احصل على بيانات المفتاح العام المجمَّعة» من «خدمة التشفير» وتُعاد قيمتها. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:214]

```
215:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:215]

```
216:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:216]

```
217:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:217]

```
218:      * Generate message ID for duplicate detection
```
> تعليق: ولّد معرّف رسالة لكشف التكرار. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:218]

```
219:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:219]

```
220:     private fun generateMessageID(packet: BitchatPacket, peerID: String): String {
```
> تُعرَّف دالة خاصة اسمها «ولّد معرّف الرسالة» (generateMessageID) تأخذ معامِلين: «الرزمة» (packet) من نوع BitchatPacket و«معرّف القرين» (peerID) من نوع نص، وتُعيد نصاً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:220]

```
221:         return when (MessageType.fromValue(packet.type)) {
```
> تُعيد نتيجة تعبير «عندما» (when) المبني على نوع الرسالة المُشتقّ من قيمة نوع الرزمة عبر MessageType.fromValue. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:221]

```
222:             MessageType.FRAGMENT -> {
```
> فرع المطابقة للقيمة MessageType.FRAGMENT (الشظية). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:222]

```
223:                 // For fragments, include the payload hash to distinguish different fragments
```
> تعليق: للشظايا، أدرِج بصمة الحمولة للتمييز بين الشظايا المختلفة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:223]

```
224:                 "${packet.timestamp}-$peerID-${packet.type}-${packet.payload.contentHashCode()}"
```
> يُكوَّن نص يتألّف من الطابع الزمني للرزمة ثم شرطة ومعرّف القرين ثم شرطة ونوع الرزمة ثم شرطة وبصمة محتوى الحمولة (contentHashCode). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:224]

```
225:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:225]

```
226:             else -> {
```
> فرع المطابقة الافتراضي «وإلّا» (else). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:226]

```
227:                 // For other messages, use a truncated payload hash
```
> تعليق: للرسائل الأخرى، استعمل بصمة حمولة مقتطعة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:227]

```
228:                 val payloadHash = packet.payload.sliceArray(0 until minOf(64, packet.payload.size)).contentHashCode()
```
> يُعرَّف متغيّر ثابت اسمه «بصمة الحمولة» (payloadHash) قيمته بصمة محتوى مقطع من الحمولة يبدأ من الصفر حتى الأصغر بين 64 وحجم الحمولة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:228]

```
229:                 "${packet.timestamp}-$peerID-$payloadHash"
```
> يُكوَّن نص يتألّف من الطابع الزمني للرزمة ثم شرطة ومعرّف القرين ثم شرطة وبصمة الحمولة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:229]

```
230:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:230]

```
231:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:231]

```
232:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:232]

```
233:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:233]

```
234:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:234]

```
235:      * Verify packet signature using peer's signing public key
```
> تعليق: تحقّق من توقيع الرزمة باستعمال مفتاح التوقيع العام للقرين. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:235]

```
236:      * Returns true only if signature is present and valid
```
> تعليق: يُعيد القيمة صحيح فقط إذا كان التوقيع موجوداً وصالحاً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:236]

```
237:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:237]

```
238:     private fun verifyPacketSignature(packet: BitchatPacket, peerID: String): Boolean {
```
> تُعرَّف دالة خاصة اسمها «تحقّق من توقيع الرزمة» (verifyPacketSignature) تأخذ معامِلين: «الرزمة» من نوع BitchatPacket و«معرّف القرين» من نوع نص، وتُعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:238]

```
239:         try {
```
> بداية كتلة «حاوِل» (try). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:239]

```
240:             // only verify ANNOUNCE, MESSAGE, and FILE_TRANSFER
```
> تعليق: تحقّق فقط من ANNOUNCE وMESSAGE وFILE_TRANSFER. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:240]

```
241:             if (MessageType.fromValue(packet.type) !in setOf(
```
> شرط «إذا» (if): إذا كان نوع الرسالة المُشتقّ من قيمة نوع الرزمة غير موجود في مجموعة (setOf). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:241]

```
242:                     MessageType.ANNOUNCE,
```
> العنصر MessageType.ANNOUNCE (الإعلان) ضمن المجموعة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:242]

```
243:                     MessageType.MESSAGE,
```
> العنصر MessageType.MESSAGE (الرسالة) ضمن المجموعة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:243]

```
244:                     MessageType.FILE_TRANSFER
```
> العنصر MessageType.FILE_TRANSFER (نقل الملف) ضمن المجموعة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:244]

```
245:                 )) {
```
> إغلاق استدعاء setOf وفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:245]

```
246:                 return true
```
> تُعاد القيمة صحيح (true). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:246]

```
247:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:247]

```
248:             // 1. Mandatory Signature Check
```
> تعليق: 1. فحص التوقيع الإلزامي. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:248]

```
249:             if (packet.signature == null) {
```
> شرط «إذا»: إذا كان توقيع الرزمة (signature) مساوياً للقيمة الفارغة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:249]

```
250:                 Log.w(TAG, "❌ Signature check for $peerID: NO_SIGNATURE (packet type ${packet.type})")
```
> يُسجَّل تحذير عبر Log.w بوسم TAG ونصّ يحوي علامة ❌ و«فحص التوقيع لـ» متبوعاً بمعرّف القرين ثم «NO_SIGNATURE» ونوع الرزمة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:250]

```
251:                 return false
```
> تُعاد القيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:251]

```
252:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:252]

```
253:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:253]

```
254:             // 2. Get Signing Public Key
```
> تعليق: 2. احصل على مفتاح التوقيع العام. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:254]

```
255:             var signingPublicKey: ByteArray? = null
```
> يُعرَّف متغيّر متغيّر القيمة اسمه «مفتاح التوقيع العام» (signingPublicKey) من نوع مصفوفة بايت قابلة لأن تكون فارغة، وقيمته الابتدائية فارغة (null). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:255]

```
256:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:256]

```
257:             if (MessageType.fromValue(packet.type) == MessageType.ANNOUNCE) {
```
> شرط «إذا»: إذا كان نوع الرسالة المُشتقّ من قيمة نوع الرزمة مساوياً MessageType.ANNOUNCE. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:257]

```
258:                 // Special Case: ANNOUNCE packets carry their own signing key
```
> تعليق: حالة خاصة: رزم ANNOUNCE تحمل مفتاح توقيعها الخاص. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:258]

```
259:                 try {
```
> بداية كتلة «حاوِل». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:259]

```
260:                     val announcement = com.bitchat.android.model.IdentityAnnouncement.decode(packet.payload)
```
> يُعرَّف متغيّر ثابت اسمه «الإعلان» (announcement) قيمته نتيجة استدعاء دالة «فُكّ الترميز» (decode) من النوع IdentityAnnouncement بتمرير حمولة الرزمة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:260]

```
261:                     signingPublicKey = announcement?.signingPublicKey
```
> يُسنَد إلى «مفتاح التوقيع العام» قيمة حقل «مفتاح التوقيع العام» (signingPublicKey) من الإعلان عبر استدعاء آمن (?.). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:261]

```
262:                 } catch (e: Exception) {
```
> تُلتقط حالة استثناء باسم «e». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:262]

```
263:                     Log.w(TAG, "Failed to decode announcement for key extraction: ${e.message}")
```
> يُسجَّل تحذير عبر Log.w بوسم TAG ونصّ «فشل فكّ ترميز الإعلان لاستخراج المفتاح» متبوعاً برسالة الاستثناء. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:263]

```
264:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:264]

```
265:             } else {
```
> فرع «وإلّا» (else). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:265]

```
266:                 // Standard Case: Get key from known peer info
```
> تعليق: الحالة القياسية: احصل على المفتاح من معلومات القرين المعروف. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:266]

```
267:                 val peerInfo = delegate?.getPeerInfo(peerID)
```
> يُعرَّف متغيّر ثابت اسمه «معلومات القرين» (peerInfo) قيمته نتيجة استدعاء «احصل على معلومات القرين» (getPeerInfo) من «المفوَّض» (delegate) عبر استدعاء آمن بتمرير معرّف القرين. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:267]

```
268:                 signingPublicKey = peerInfo?.signingPublicKey
```
> يُسنَد إلى «مفتاح التوقيع العام» قيمة حقل «مفتاح التوقيع العام» من معلومات القرين عبر استدعاء آمن. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:268]

```
269:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:269]

```
270:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:270]

```
271:             if (signingPublicKey == null) {
```
> شرط «إذا»: إذا كان «مفتاح التوقيع العام» مساوياً للقيمة الفارغة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:271]

```
272:                 // If we don't have a key (and it's not an announce), we can't verify.
```
> تعليق: إذا لم يكن لدينا مفتاح (وليست إعلاناً)، لا يمكننا التحقّق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:272]

```
273:                 // For security, we must reject packets from unknown peers unless it's an announce.
```
> تعليق: للأمان، يجب أن نرفض الرزم من القرناء غير المعروفين ما لم تكن إعلاناً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:273]

```
274:                 Log.w(TAG, "❌ Signature check for $peerID: NO_SIGNING_KEY_AVAILABLE (packet type ${packet.type})")
```
> يُسجَّل تحذير عبر Log.w بوسم TAG ونصّ يحوي علامة ❌ و«فحص التوقيع لـ» متبوعاً بمعرّف القرين ثم «NO_SIGNING_KEY_AVAILABLE» ونوع الرزمة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:274]

```
275:                 return false
```
> تُعاد القيمة خطأ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:275]

```
276:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:276]

```
277:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:277]

```
278:             // 3. Get Canonical Data
```
> تعليق: 3. احصل على البيانات المعياريّة (Canonical). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:278]

```
279:             val packetDataForSigning = packet.toBinaryDataForSigning()
```
> يُعرَّف متغيّر ثابت اسمه «بيانات الرزمة للتوقيع» (packetDataForSigning) قيمته نتيجة استدعاء دالة «إلى بيانات ثنائية للتوقيع» (toBinaryDataForSigning) من الرزمة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:279]

```
280:             if (packetDataForSigning == null) {
```
> شرط «إذا»: إذا كانت «بيانات الرزمة للتوقيع» مساوية للقيمة الفارغة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:280]

```
281:                 Log.w(TAG, "❌ Signature check for $peerID: ENCODING_ERROR (packet type ${packet.type})")
```
> يُسجَّل تحذير عبر Log.w بوسم TAG ونصّ يحوي علامة ❌ و«فحص التوقيع لـ» متبوعاً بمعرّف القرين ثم «ENCODING_ERROR» ونوع الرزمة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:281]

```
282:                 return false
```
> تُعاد القيمة خطأ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:282]

```
283:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:283]

```
284:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:284]

```
285:             // 4. Verify Signature
```
> تعليق: 4. تحقّق من التوقيع. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:285]

```
286:             val signature = packet.signature!!
```
> يُعرَّف متغيّر ثابت اسمه «التوقيع» (signature) قيمته توقيع الرزمة مع تأكيد عدم الفراغ (!!). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:286]

```
287:             val isSignatureValid = encryptionService.verifyEd25519Signature(
```
> يُعرَّف متغيّر ثابت اسمه «هل التوقيع صالح» (isSignatureValid) قيمته نتيجة استدعاء دالة «تحقّق من توقيع Ed25519» (verifyEd25519Signature) من «خدمة التشفير». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:287]

```
288:                 signature,
```
> الوسيط الأول: «التوقيع». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:288]

```
289:                 packetDataForSigning,
```
> الوسيط الثاني: «بيانات الرزمة للتوقيع». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:289]

```
290:                 signingPublicKey
```
> الوسيط الثالث: «مفتاح التوقيع العام». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:290]

```
291:             )
```
> إغلاق استدعاء الدالة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:291]

```
292:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:292]

```
293:             if (isSignatureValid) {
```
> شرط «إذا»: إذا كان «هل التوقيع صالح» صحيحاً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:293]

```
294:                 // Log.v(TAG, "✅ Signature verified for $peerID (type ${packet.type})")
```
> تعليق: سطر تسجيل معطَّل عبر Log.v بنصّ يحوي علامة ✅ و«تمّ التحقّق من التوقيع لـ» متبوعاً بمعرّف القرين ونوع الرزمة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:294]

```
295:                 return true
```
> تُعاد القيمة صحيح. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:295]

```
296:             } else {
```
> فرع «وإلّا». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:296]

```
297:                 Log.w(TAG, "❌ Signature INVALID for $peerID (type ${packet.type})")
```
> يُسجَّل تحذير عبر Log.w بوسم TAG ونصّ يحوي علامة ❌ و«التوقيع غير صالح لـ» متبوعاً بمعرّف القرين ونوع الرزمة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:297]

```
298:                 return false
```
> تُعاد القيمة خطأ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:298]

```
299:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:299]

```
300:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:300]

```
301:         } catch (e: Exception) {
```
> تُلتقط حالة استثناء باسم «e». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:301]

```
302:             Log.e(TAG, "❌ Signature verification error for $peerID: ${e.message}")
```
> يُسجَّل خطأ عبر Log.e بوسم TAG ونصّ يحوي علامة ❌ و«خطأ في التحقّق من التوقيع لـ» متبوعاً بمعرّف القرين ثم رسالة الاستثناء. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:302]

```
303:             return false
```
> تُعاد القيمة خطأ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:303]

```
304:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:304]

```
305:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:305]

```
306:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:306]

```
307:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:307]

```
308:      * Check if we have encryption keys for a peer
```
> تعليق: تحقّق إن كان لدينا مفاتيح تشفير لقرين. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:308]

```
309:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:309]

```
310:     fun hasKeysForPeer(peerID: String): Boolean {
```
> تُعرَّف دالة عامة اسمها «هل توجد مفاتيح للقرين» (hasKeysForPeer) تأخذ معامِلاً واحداً «معرّف القرين» من نوع نص وتُعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:310]

```
311:         return encryptionService.hasEstablishedSession(peerID)
```
> تُستدعى دالة «هل هناك جلسة مؤسَّسة» (hasEstablishedSession) من «خدمة التشفير» بتمرير معرّف القرين وتُعاد قيمتها. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:311]

```
312:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:312]

```
313:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:313]

```
314:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:314]

```
315:      * Get debug information
```
> تعليق: احصل على معلومات التنقيح. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:315]

```
316:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:316]

```
317:     fun getDebugInfo(): String {
```
> تُعرَّف دالة عامة اسمها «احصل على معلومات التنقيح» (getDebugInfo) لا تأخذ معامِلات وتُعيد نصاً. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:317]

```
318:         return buildString {
```
> تُعاد نتيجة باني النصّ (buildString) مع كتلة بناء. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:318]

```
319:             appendLine("=== Security Manager Debug Info ===")
```
> يُضاف سطر «=== Security Manager Debug Info ===» إلى النصّ المبني عبر appendLine. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:319]

```
320:             appendLine("Processed Messages: ${processedMessages.size}")
```
> يُضاف سطر «Processed Messages:» متبوعاً بحجم مجموعة «الرسائل المعالَجة» (processedMessages). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:320]

```
321:             appendLine("Processed Key Exchanges: ${processedKeyExchanges.size}")
```
> يُضاف سطر «Processed Key Exchanges:» متبوعاً بحجم مجموعة «تبادلات المفاتيح المعالَجة» (processedKeyExchanges). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:321]

```
322:             appendLine("Message Timestamps: ${messageTimestamps.size}")
```
> يُضاف سطر «Message Timestamps:» متبوعاً بحجم «الطوابع الزمنية للرسائل» (messageTimestamps). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:322]

```
323:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:323]

```
324:             if (processedKeyExchanges.isNotEmpty()) {
```
> شرط «إذا»: إذا كانت مجموعة «تبادلات المفاتيح المعالَجة» غير فارغة (isNotEmpty). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:324]

```
325:                 appendLine("Key Exchange History:")
```
> يُضاف سطر «Key Exchange History:». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:325]

```
326:                 processedKeyExchanges.take(10).forEach { exchange ->
```
> يُؤخَذ أول عشرة عناصر (take) من «تبادلات المفاتيح المعالَجة» ويُكرَّر على كلّ منها (forEach) بمتغيّر «تبادل» (exchange). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:326]

```
327:                     appendLine("  - $exchange")
```
> يُضاف سطر يبدأ بمسافتين وشرطة ثم قيمة «التبادل». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:327]

```
328:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:328]

```
329:                 if (processedKeyExchanges.size > 10) {
```
> شرط «إذا»: إذا كان حجم «تبادلات المفاتيح المعالَجة» أكبر من 10. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:329]

```
330:                     appendLine("  ... and ${processedKeyExchanges.size - 10} more")
```
> يُضاف سطر «  ... and» متبوعاً بحجم «تبادلات المفاتيح المعالَجة» ناقص 10 ثم «more». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:330]

```
331:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:331]

```
332:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:332]

```
333:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:333]

```
334:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:334]

```
335:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:335]

```
336:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:336]

```
337:      * Start periodic cleanup
```
> تعليق: ابدأ التنظيف الدوري. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:337]

```
338:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:338]

```
339:     private fun startPeriodicCleanup() {
```
> تُعرَّف دالة خاصة اسمها «ابدأ التنظيف الدوري» (startPeriodicCleanup) لا تأخذ معامِلات ولا تُعيد قيمة معلَنة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:339]

```
340:         managerScope.launch {
```
> يُطلَق كوروتين (launch) ضمن «نطاق المدير» (managerScope) مع كتلة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:340]

```
341:             while (isActive) {
```
> حلقة «طالما» (while) شرطها أن يكون الكوروتين نشطاً (isActive). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:341]

```
342:                 delay(CLEANUP_INTERVAL)
```
> يُؤخَّر التنفيذ (delay) بمقدار الثابت «فترة التنظيف» (CLEANUP_INTERVAL). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:342]

```
343:                 cleanupOldData()
```
> تُستدعى دالة «نظّف البيانات القديمة» (cleanupOldData). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:343]

```
344:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:344]

```
345:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:345]

```
346:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:346]

```
347:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:347]

```
348:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:348]

```
349:      * Clean up old processed messages and timestamps
```
> تعليق: نظّف الرسائل المعالَجة القديمة والطوابع الزمنية. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:349]

```
350:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:350]

```
351:     private fun cleanupOldData() {
```
> تُعرَّف دالة خاصة اسمها «نظّف البيانات القديمة» (cleanupOldData) لا تأخذ معامِلات ولا تُعيد قيمة معلَنة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:351]

```
352:         val cutoffTime = System.currentTimeMillis() - MESSAGE_TIMEOUT
```
> يُعرَّف متغيّر ثابت اسمه «زمن القطع» (cutoffTime) قيمته الوقت الحالي بالميلي ثانية ناقص الثابت «مهلة الرسالة» (MESSAGE_TIMEOUT). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:352]

```
353:         var removedCount = 0
```
> يُعرَّف متغيّر متغيّر القيمة اسمه «عدد المحذوفات» (removedCount) قيمته الابتدائية صفر. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:353]

```
354:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:354]

```
355:         // Clean up old message timestamps and corresponding processed messages
```
> تعليق: نظّف الطوابع الزمنية القديمة للرسائل والرسائل المعالَجة المقابلة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:355]

```
356:         val messagesToRemove = messageTimestamps.entries.filter { (_, timestamp) ->
```
> يُعرَّف متغيّر ثابت اسمه «الرسائل المطلوب حذفها» (messagesToRemove) قيمته نتيجة ترشيح (filter) مدخلات «الطوابع الزمنية للرسائل» بمتغيّرين أولهما مهمَل (_) والثاني «الطابع الزمني» (timestamp). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:356]

```
357:             timestamp < cutoffTime
```
> شرط الترشيح: أن يكون «الطابع الزمني» أصغر من «زمن القطع». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:357]

```
358:         }.map { it.key }
```
> إغلاق كتلة الترشيح ثم تحويل (map) كلّ مدخل إلى مفتاحه (it.key). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:358]

```
359:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:359]

```
360:         messagesToRemove.forEach { messageId ->
```
> يُكرَّر على كلّ عنصر من «الرسائل المطلوب حذفها» بمتغيّر «معرّف الرسالة» (messageId). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:360]

```
361:             messageTimestamps.remove(messageId)
```
> يُحذَف المدخل ذو «معرّف الرسالة» من «الطوابع الزمنية للرسائل» عبر remove. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:361]

```
362:             if (processedMessages.remove(messageId)) {
```
> شرط «إذا»: إذا نجح حذف «معرّف الرسالة» من مجموعة «الرسائل المعالَجة» (يُعيد remove صحيح). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:362]

```
363:                 removedCount++
```
> تُزاد قيمة «عدد المحذوفات» بمقدار واحد. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:363]

```
364:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:364]

```
365:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:365]

```
366:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:366]

```
367:         // Limit the size of processed messages set
```
> تعليق: حُدّ من حجم مجموعة الرسائل المعالَجة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:367]

```
368:         if (processedMessages.size > MAX_PROCESSED_MESSAGES) {
```
> شرط «إذا»: إذا كان حجم «الرسائل المعالَجة» أكبر من الثابت «الحدّ الأقصى للرسائل المعالَجة» (MAX_PROCESSED_MESSAGES). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:368]

```
369:             val excess = processedMessages.size - MAX_PROCESSED_MESSAGES
```
> يُعرَّف متغيّر ثابت اسمه «الفائض» (excess) قيمته حجم «الرسائل المعالَجة» ناقص «الحدّ الأقصى للرسائل المعالَجة». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:369]

```
370:             val toRemove = processedMessages.take(excess)
```
> يُعرَّف متغيّر ثابت اسمه «المطلوب حذفه» (toRemove) قيمته أول عناصر بعدد «الفائض» من «الرسائل المعالَجة». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:370]

```
371:             processedMessages.removeAll(toRemove.toSet())
```
> تُحذَف جميع عناصر «المطلوب حذفه» (محوَّلة إلى مجموعة toSet) من «الرسائل المعالَجة» عبر removeAll. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:371]

```
372:             removeFromMessageTimestamps(toRemove)
```
> تُستدعى دالة «احذف من الطوابع الزمنية للرسائل» (removeFromMessageTimestamps) بتمرير «المطلوب حذفه». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:372]

```
373:             removedCount += excess
```
> تُزاد قيمة «عدد المحذوفات» بمقدار «الفائض». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:373]

```
374:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:374]

```
375:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:375]

```
376:         // Limit the size of processed key exchanges set
```
> تعليق: حُدّ من حجم مجموعة تبادلات المفاتيح المعالَجة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:376]

```
377:         if (processedKeyExchanges.size > MAX_PROCESSED_KEY_EXCHANGES) {
```
> شرط «إذا»: إذا كان حجم «تبادلات المفاتيح المعالَجة» أكبر من الثابت «الحدّ الأقصى لتبادلات المفاتيح المعالَجة» (MAX_PROCESSED_KEY_EXCHANGES). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:377]

```
378:             val excess = processedKeyExchanges.size - MAX_PROCESSED_KEY_EXCHANGES
```
> يُعرَّف متغيّر ثابت اسمه «الفائض» (excess) قيمته حجم «تبادلات المفاتيح المعالَجة» ناقص «الحدّ الأقصى لتبادلات المفاتيح المعالَجة». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:378]

```
379:             val toRemove = processedKeyExchanges.take(excess)
```
> يُعرَّف متغيّر ثابت اسمه «المطلوب حذفه» (toRemove) قيمته أول عناصر بعدد «الفائض» من «تبادلات المفاتيح المعالَجة». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:379]

```
380:             processedKeyExchanges.removeAll(toRemove.toSet())
```
> تُحذَف جميع عناصر «المطلوب حذفه» (محوَّلة إلى مجموعة) من «تبادلات المفاتيح المعالَجة» عبر removeAll. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:380]

```
381:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:381]

```
382:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:382]

```
383:         if (removedCount > 0) {
```
> شرط «إذا»: إذا كان «عدد المحذوفات» أكبر من صفر. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:383]

```
384:             Log.d(TAG, "Cleaned up $removedCount old processed messages")
```
> يُسجَّل تنقيح عبر Log.d بوسم TAG ونصّ «Cleaned up» متبوعاً بـ«عدد المحذوفات» ثم «old processed messages». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:384]

```
385:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:385]

```
386:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:386]

```
387:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:387]

```
388:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:388]

```
389:      * Helper to remove entries from messageTimestamps
```
> تعليق: مساعد لحذف المدخلات من messageTimestamps. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:389]

```
390:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:390]

```
391:     private fun removeFromMessageTimestamps(messageIds: List<String>) {
```
> تُعرَّف دالة خاصة اسمها «احذف من الطوابع الزمنية للرسائل» (removeFromMessageTimestamps) تأخذ معامِلاً واحداً «معرّفات الرسائل» (messageIds) من نوع قائمة نصوص ولا تُعيد قيمة معلَنة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:391]

```
392:         messageIds.forEach { messageId ->
```
> يُكرَّر على كلّ عنصر من «معرّفات الرسائل» بمتغيّر «معرّف الرسالة» (messageId). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:392]

```
393:             messageTimestamps.remove(messageId)
```
> يُحذَف المدخل ذو «معرّف الرسالة» من «الطوابع الزمنية للرسائل» عبر remove. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:393]

```
394:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:394]

```
395:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:395]

```
396:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:396]

```
397:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:397]

```
398:      * Clear all security data
```
> تعليق: امسح جميع بيانات الأمان. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:398]

```
399:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:399]

```
400:     fun clearAllData() {
```
> تُعرَّف دالة عامة اسمها «امسح جميع البيانات» (clearAllData) لا تأخذ معامِلات وتفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:400]
