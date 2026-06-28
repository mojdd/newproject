# شريحة — app/src/main/java/com/bitchat/android/mesh/MeshCore.kt (الأسطر 201–400)

```
201:                 return peerManager.addOrUpdatePeer(peerID, nickname)
```
> يُعيد نتيجة استدعاء الدالة «addOrUpdatePeer» على مدير الأقران (peerManager) ممرِّراً معرّف القرين (peerID) والاسم المستعار (nickname). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:201]

```
202:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:202]

```
203: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:203]

```
204:             override fun removePeer(peerID: String) {
```
> تعريف دالة متجاوِزة (override) باسم «removePeer» تأخذ معامِلاً «peerID» من نوع النص (String) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:204]

```
205:                 peerManager.removePeer(peerID)
```
> يستدعي الدالة «removePeer» على مدير الأقران (peerManager) ممرِّراً معرّف القرين (peerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:205]

```
206:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:206]

```
207: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:207]

```
208:             override fun updatePeerNickname(peerID: String, nickname: String) {
```
> تعريف دالة متجاوِزة (override) باسم «updatePeerNickname» تأخذ معامِلَين «peerID» و«nickname» كلاهما من نوع النص (String) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:208]

```
209:                 peerManager.addOrUpdatePeer(peerID, nickname)
```
> يستدعي الدالة «addOrUpdatePeer» على مدير الأقران (peerManager) ممرِّراً معرّف القرين (peerID) والاسم المستعار (nickname). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:209]

```
210:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:210]

```
211: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:211]

```
212:             override fun getPeerNickname(peerID: String): String? {
```
> تعريف دالة متجاوِزة (override) باسم «getPeerNickname» تأخذ معامِلاً «peerID» من نوع النص (String) وتُعيد نصاً قابلاً للإفراغ (String?). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:212]

```
213:                 return peerManager.getPeerNickname(peerID)
```
> يُعيد نتيجة استدعاء الدالة «getPeerNickname» على مدير الأقران (peerManager) ممرِّراً معرّف القرين (peerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:213]

```
214:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:214]

```
215: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:215]

```
216:             override fun getNetworkSize(): Int {
```
> تعريف دالة متجاوِزة (override) باسم «getNetworkSize» بلا معامِلات وتُعيد عدداً صحيحاً (Int). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:216]

```
217:                 return peerManager.getActivePeerCount()
```
> يُعيد نتيجة استدعاء الدالة «getActivePeerCount» على مدير الأقران (peerManager) بلا معامِلات. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:217]

```
218:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:218]

```
219: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:219]

```
220:             override fun getMyNickname(): String? {
```
> تعريف دالة متجاوِزة (override) باسم «getMyNickname» بلا معامِلات وتُعيد نصاً قابلاً للإفراغ (String?). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:220]

```
221:                 return delegate?.getNickname()
```
> يُعيد نتيجة استدعاء الدالة «getNickname» على المفوَّض (delegate) باستعمال الاستدعاء الآمن (?.) الذي يُعيد القيمة الفارغة إذا كان المفوَّض فارغاً. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:221]

```
222:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:222]

```
223: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:223]

```
224:             override fun getPeerInfo(peerID: String): PeerInfo? {
```
> تعريف دالة متجاوِزة (override) باسم «getPeerInfo» تأخذ معامِلاً «peerID» من نوع النص (String) وتُعيد كائن معلومات القرين (PeerInfo) قابلاً للإفراغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:224]

```
225:                 return peerManager.getPeerInfo(peerID)
```
> يُعيد نتيجة استدعاء الدالة «getPeerInfo» على مدير الأقران (peerManager) ممرِّراً معرّف القرين (peerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:225]

```
226:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:226]

```
227: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:227]

```
228:             override fun updatePeerInfo(
```
> بداية تعريف دالة متجاوِزة (override) باسم «updatePeerInfo» تُفتح قائمة معامِلاتها على أسطر تالية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:228]

```
229:                 peerID: String,
```
> المعامِل الأول «peerID» من نوع النص (String). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:229]

```
230:                 nickname: String,
```
> المعامِل الثاني «nickname» من نوع النص (String). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:230]

```
231:                 noisePublicKey: ByteArray,
```
> المعامِل الثالث «noisePublicKey» (مفتاح نويز العمومي) من نوع مصفوفة بايت (ByteArray). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:231]

```
232:                 signingPublicKey: ByteArray,
```
> المعامِل الرابع «signingPublicKey» (مفتاح التوقيع العمومي) من نوع مصفوفة بايت (ByteArray). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:232]

```
233:                 isVerified: Boolean
```
> المعامِل الخامس «isVerified» (مُتحقَّق منه) من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:233]

```
234:             ): Boolean {
```
> إغلاق قائمة المعامِلات وتحديد نوع القيمة المُعادة بأنها منطقي (Boolean). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:234]

```
235:                 return peerManager.updatePeerInfo(peerID, nickname, noisePublicKey, signingPublicKey, isVerified)
```
> يُعيد نتيجة استدعاء الدالة «updatePeerInfo» على مدير الأقران (peerManager) ممرِّراً المعامِلات الخمسة: peerID وnickname وnoisePublicKey وsigningPublicKey وisVerified. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:235]

```
236:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:236]

```
237: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:237]

```
238:             override fun sendPacket(packet: BitchatPacket) {
```
> تعريف دالة متجاوِزة (override) باسم «sendPacket» تأخذ معامِلاً «packet» من نوع حزمة بِتشات (BitchatPacket) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:238]

```
239:                 val signedPacket = signPacketBeforeBroadcast(packet)
```
> يُعرِّف متغيّراً ثابتاً «signedPacket» (الحزمة الموقَّعة) بقيمة نتيجة استدعاء الدالة «signPacketBeforeBroadcast» ممرِّراً الحزمة «packet». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:239]

```
240:                 dispatchGlobal(RoutedPacket(signedPacket))
```
> يستدعي الدالة «dispatchGlobal» ممرِّراً كائن حزمة موجَّهة (RoutedPacket) مُنشأً من الحزمة الموقَّعة «signedPacket». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:240]

```
241:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:241]

```
242: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:242]

```
243:             override fun relayPacket(routed: RoutedPacket) {
```
> تعريف دالة متجاوِزة (override) باسم «relayPacket» تأخذ معامِلاً «routed» من نوع الحزمة الموجَّهة (RoutedPacket) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:243]

```
244:                 dispatchGlobal(routed)
```
> يستدعي الدالة «dispatchGlobal» ممرِّراً الحزمة الموجَّهة «routed». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:244]

```
245:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:245]

```
246: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:246]

```
247:             override fun getBroadcastRecipient(): ByteArray {
```
> تعريف دالة متجاوِزة (override) باسم «getBroadcastRecipient» بلا معامِلات وتُعيد مصفوفة بايت (ByteArray). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:247]

```
248:                 return SpecialRecipients.BROADCAST
```
> يُعيد الثابت «BROADCAST» من الكائن «SpecialRecipients» (المستقبِلون الخاصّون). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:248]

```
249:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:249]

```
250: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:250]

```
251:             override fun verifySignature(packet: BitchatPacket, peerID: String): Boolean {
```
> تعريف دالة متجاوِزة (override) باسم «verifySignature» تأخذ معامِلَين «packet» من نوع حزمة بِتشات (BitchatPacket) و«peerID» من نوع النص (String) وتُعيد منطقياً (Boolean). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:251]

```
252:                 return securityManager.verifySignature(packet, peerID)
```
> يُعيد نتيجة استدعاء الدالة «verifySignature» على مدير الأمن (securityManager) ممرِّراً الحزمة «packet» ومعرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:252]

```
253:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:253]

```
254: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:254]

```
255:             override fun encryptForPeer(data: ByteArray, recipientPeerID: String): ByteArray? {
```
> تعريف دالة متجاوِزة (override) باسم «encryptForPeer» تأخذ معامِلَين «data» من نوع مصفوفة بايت (ByteArray) و«recipientPeerID» (معرّف القرين المستقبِل) من نوع النص (String) وتُعيد مصفوفة بايت قابلة للإفراغ (ByteArray?). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:255]

```
256:                 return securityManager.encryptForPeer(data, recipientPeerID)
```
> يُعيد نتيجة استدعاء الدالة «encryptForPeer» على مدير الأمن (securityManager) ممرِّراً البيانات «data» ومعرّف القرين المستقبِل «recipientPeerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:256]

```
257:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:257]

```
258: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:258]

```
259:             override fun decryptFromPeer(encryptedData: ByteArray, senderPeerID: String): ByteArray? {
```
> تعريف دالة متجاوِزة (override) باسم «decryptFromPeer» تأخذ معامِلَين «encryptedData» (البيانات المشفَّرة) من نوع مصفوفة بايت (ByteArray) و«senderPeerID» (معرّف القرين المُرسِل) من نوع النص (String) وتُعيد مصفوفة بايت قابلة للإفراغ (ByteArray?). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:259]

```
260:                 return securityManager.decryptFromPeer(encryptedData, senderPeerID)
```
> يُعيد نتيجة استدعاء الدالة «decryptFromPeer» على مدير الأمن (securityManager) ممرِّراً البيانات المشفَّرة «encryptedData» ومعرّف القرين المُرسِل «senderPeerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:260]

```
261:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:261]

```
262: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:262]

```
263:             override fun verifyEd25519Signature(signature: ByteArray, data: ByteArray, publicKey: ByteArray): Boolean {
```
> تعريف دالة متجاوِزة (override) باسم «verifyEd25519Signature» تأخذ ثلاثة معامِلات «signature» (التوقيع) و«data» (البيانات) و«publicKey» (المفتاح العمومي) كلها من نوع مصفوفة بايت (ByteArray) وتُعيد منطقياً (Boolean). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:263]

```
264:                 return encryptionService.verifyEd25519Signature(signature, data, publicKey)
```
> يُعيد نتيجة استدعاء الدالة «verifyEd25519Signature» على خدمة التشفير (encryptionService) ممرِّراً التوقيع «signature» والبيانات «data» والمفتاح العمومي «publicKey». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:264]

```
265:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:265]

```
266: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:266]

```
267:             override fun hasNoiseSession(peerID: String): Boolean {
```
> تعريف دالة متجاوِزة (override) باسم «hasNoiseSession» (هل توجد جلسة نويز) تأخذ معامِلاً «peerID» من نوع النص (String) وتُعيد منطقياً (Boolean). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:267]

```
268:                 return encryptionService.hasEstablishedSession(peerID)
```
> يُعيد نتيجة استدعاء الدالة «hasEstablishedSession» (هل أُنشئت جلسة) على خدمة التشفير (encryptionService) ممرِّراً معرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:268]

```
269:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:269]

```
270: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:270]

```
271:             override fun initiateNoiseHandshake(peerID: String) {
```
> تعريف دالة متجاوِزة (override) باسم «initiateNoiseHandshake» (بدء مصافحة نويز) تأخذ معامِلاً «peerID» من نوع النص (String) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:271]

```
272:                 this@MeshCore.initiateNoiseHandshake(peerID)
```
> يستدعي الدالة «initiateNoiseHandshake» على نسخة الصنف الخارجي «MeshCore» (عبر this@MeshCore) ممرِّراً معرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:272]

```
273:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:273]

```
274: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:274]

```
275:             override fun processNoiseHandshakeMessage(payload: ByteArray, peerID: String): ByteArray? {
```
> تعريف دالة متجاوِزة (override) باسم «processNoiseHandshakeMessage» (معالجة رسالة مصافحة نويز) تأخذ معامِلَين «payload» (الحمولة) من نوع مصفوفة بايت (ByteArray) و«peerID» من نوع النص (String) وتُعيد مصفوفة بايت قابلة للإفراغ (ByteArray?). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:275]

```
276:                 return try {
```
> يبدأ إعادة قيمة كتلة محاولة (try) تُسنَد قيمتها كنتيجة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:276]

```
277:                     encryptionService.processHandshakeMessage(payload, peerID)
```
> القيمة المُعادة من كتلة المحاولة هي نتيجة استدعاء الدالة «processHandshakeMessage» على خدمة التشفير (encryptionService) ممرِّراً الحمولة «payload» ومعرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:277]

```
278:                 } catch (_: Exception) {
```
> بداية كتلة التقاط (catch) تلتقط أي استثناء (Exception) متجاهِلةً مرجعه (_). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:278]

```
279:                     null
```
> القيمة المُعادة عند وقوع الاستثناء هي القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:279]

```
280:                 }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:280]

```
281:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:281]

```
282: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:282]

```
283:             override fun updatePeerIDBinding(
```
> بداية تعريف دالة متجاوِزة (override) باسم «updatePeerIDBinding» (تحديث ربط معرّف القرين) تُفتح قائمة معامِلاتها على أسطر تالية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:283]

```
284:                 newPeerID: String,
```
> المعامِل الأول «newPeerID» (معرّف القرين الجديد) من نوع النص (String). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:284]

```
285:                 nickname: String,
```
> المعامِل الثاني «nickname» (الاسم المستعار) من نوع النص (String). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:285]

```
286:                 publicKey: ByteArray,
```
> المعامِل الثالث «publicKey» (المفتاح العمومي) من نوع مصفوفة بايت (ByteArray). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:286]

```
287:                 previousPeerID: String?
```
> المعامِل الرابع «previousPeerID» (معرّف القرين السابق) من نوع النص القابل للإفراغ (String?). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:287]

```
288:             ) {
```
> إغلاق قائمة المعامِلات وفتح جسم الدالة، بلا قيمة مُعادة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:288]

```
289:                 peerManager.addOrUpdatePeer(newPeerID, nickname)
```
> يستدعي الدالة «addOrUpdatePeer» على مدير الأقران (peerManager) ممرِّراً معرّف القرين الجديد «newPeerID» والاسم المستعار «nickname». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:289]

```
290:                 val fingerprint = peerManager.storeFingerprintForPeer(newPeerID, publicKey)
```
> يُعرِّف متغيّراً ثابتاً «fingerprint» (البصمة) بقيمة نتيجة استدعاء الدالة «storeFingerprintForPeer» على مدير الأقران ممرِّراً معرّف القرين الجديد «newPeerID» والمفتاح العمومي «publicKey». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:290]

```
291:                 previousPeerID?.let { peerManager.removePeer(it) }
```
> إذا لم يكن «previousPeerID» فارغاً، يُنفِّذ داخل دالة «let» استدعاءَ الدالة «removePeer» على مدير الأقران ممرِّراً القيمة الحالية (it) أي معرّف القرين السابق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:291]

```
292:                 Log.d("MeshCore", "Updated peer ID binding: $newPeerID fp=${fingerprint.take(16)}")
```
> يستدعي الدالة «d» (تصحيح/debug) على «Log» بوسم «MeshCore» ونصٍّ يحتوي العبارة «Updated peer ID binding:» مع معرّف القرين الجديد «newPeerID» و«fp=» متبوعاً بأول ستة عشر محرفاً من البصمة عبر «fingerprint.take(16)». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:292]

```
293:                 hooks.onPeerIdBindingUpdated?.invoke(newPeerID, nickname, publicKey, previousPeerID)
```
> يستدعي عبر «invoke» باستعمال الاستدعاء الآمن (?.) دالةَ الخطّاف «onPeerIdBindingUpdated» من الكائن «hooks» (الخطّافات) ممرِّراً newPeerID وnickname وpublicKey وpreviousPeerID، فلا يُنفِّذ إن كانت الدالة فارغة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:293]

```
294:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:294]

```
295: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:295]

```
296:             override fun decryptChannelMessage(encryptedContent: ByteArray, channel: String): String? {
```
> تعريف دالة متجاوِزة (override) باسم «decryptChannelMessage» (فكّ تشفير رسالة القناة) تأخذ معامِلَين «encryptedContent» (المحتوى المشفَّر) من نوع مصفوفة بايت (ByteArray) و«channel» (القناة) من نوع النص (String) وتُعيد نصاً قابلاً للإفراغ (String?). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:296]

```
297:                 return delegate?.decryptChannelMessage(encryptedContent, channel)
```
> يُعيد نتيجة استدعاء الدالة «decryptChannelMessage» على المفوَّض (delegate) باستعمال الاستدعاء الآمن (?.) ممرِّراً المحتوى المشفَّر «encryptedContent» والقناة «channel»، فيُعيد فارغاً إن كان المفوَّض فارغاً. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:297]

```
298:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:298]

```
299: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:299]

```
300:             override fun onMessageReceived(message: BitchatMessage) {
```
> تعريف دالة متجاوِزة (override) باسم «onMessageReceived» (عند استقبال رسالة) تأخذ معامِلاً «message» من نوع رسالة بِتشات (BitchatMessage) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:300]

```
301:                 hooks.onMessageReceived?.invoke(message)
```
> يستدعي عبر «invoke» باستعمال الاستدعاء الآمن (?.) دالةَ الخطّاف «onMessageReceived» من الكائن «hooks» ممرِّراً الرسالة «message». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:301]

```
302:                 delegate?.didReceiveMessage(message)
```
> يستدعي الدالة «didReceiveMessage» على المفوَّض (delegate) باستعمال الاستدعاء الآمن (?.) ممرِّراً الرسالة «message». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:302]

```
303:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:303]

```
304: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:304]

```
305:             override fun onChannelLeave(channel: String, fromPeer: String) {
```
> تعريف دالة متجاوِزة (override) باسم «onChannelLeave» (عند مغادرة القناة) تأخذ معامِلَين «channel» (القناة) و«fromPeer» (من القرين) كلاهما من نوع النص (String) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:305]

```
306:                 delegate?.didReceiveChannelLeave(channel, fromPeer)
```
> يستدعي الدالة «didReceiveChannelLeave» على المفوَّض (delegate) باستعمال الاستدعاء الآمن (?.) ممرِّراً القناة «channel» والقرين المصدر «fromPeer». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:306]

```
307:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:307]

```
308: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:308]

```
309:             override fun onDeliveryAckReceived(messageID: String, peerID: String) {
```
> تعريف دالة متجاوِزة (override) باسم «onDeliveryAckReceived» (عند استقبال إقرار التسليم) تأخذ معامِلَين «messageID» (معرّف الرسالة) و«peerID» (معرّف القرين) كلاهما من نوع النص (String) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:309]

```
310:                 delegate?.didReceiveDeliveryAck(messageID, peerID)
```
> يستدعي الدالة «didReceiveDeliveryAck» على المفوَّض (delegate) باستعمال الاستدعاء الآمن (?.) ممرِّراً معرّف الرسالة «messageID» ومعرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:310]

```
311:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:311]

```
312: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:312]

```
313:             override fun onReadReceiptReceived(messageID: String, peerID: String) {
```
> تعريف دالة متجاوِزة (override) باسم «onReadReceiptReceived» (عند استقبال إيصال القراءة) تأخذ معامِلَين «messageID» (معرّف الرسالة) و«peerID» (معرّف القرين) كلاهما من نوع النص (String) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:313]

```
314:                 delegate?.didReceiveReadReceipt(messageID, peerID)
```
> يستدعي الدالة «didReceiveReadReceipt» على المفوَّض (delegate) باستعمال الاستدعاء الآمن (?.) ممرِّراً معرّف الرسالة «messageID» ومعرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:314]

```
315:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:315]

```
316: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:316]

```
317:             override fun onVerifyChallengeReceived(peerID: String, payload: ByteArray, timestampMs: Long) {
```
> تعريف دالة متجاوِزة (override) باسم «onVerifyChallengeReceived» (عند استقبال تحدّي التحقّق) تأخذ ثلاثة معامِلات «peerID» من نوع النص (String) و«payload» (الحمولة) من نوع مصفوفة بايت (ByteArray) و«timestampMs» (الطابع الزمني بالمللي ثانية) من نوع عدد طويل (Long) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:317]

```
318:                 delegate?.didReceiveVerifyChallenge(peerID, payload, timestampMs)
```
> يستدعي الدالة «didReceiveVerifyChallenge» على المفوَّض (delegate) باستعمال الاستدعاء الآمن (?.) ممرِّراً معرّف القرين «peerID» والحمولة «payload» والطابع الزمني «timestampMs». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:318]

```
319:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:319]

```
320: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:320]

```
321:             override fun onVerifyResponseReceived(peerID: String, payload: ByteArray, timestampMs: Long) {
```
> تعريف دالة متجاوِزة (override) باسم «onVerifyResponseReceived» (عند استقبال ردّ التحقّق) تأخذ ثلاثة معامِلات «peerID» من نوع النص (String) و«payload» (الحمولة) من نوع مصفوفة بايت (ByteArray) و«timestampMs» (الطابع الزمني بالمللي ثانية) من نوع عدد طويل (Long) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:321]

```
322:                 delegate?.didReceiveVerifyResponse(peerID, payload, timestampMs)
```
> يستدعي الدالة «didReceiveVerifyResponse» على المفوَّض (delegate) باستعمال الاستدعاء الآمن (?.) ممرِّراً معرّف القرين «peerID» والحمولة «payload» والطابع الزمني «timestampMs». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:322]

```
323:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:323]

```
324:         }
```
> إغلاق نطاق (نهاية الكائن المجهول المُسنَد إلى المفوَّض). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:324]

```
325: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:325]

```
326:         packetProcessor.delegate = object : PacketProcessorDelegate {
```
> يُسنِد إلى الخاصّية «delegate» في «packetProcessor» (معالِج الحِزَم) كائناً مجهولاً يُنفِّذ الواجهة «PacketProcessorDelegate» (مفوَّض معالِج الحِزَم). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:326]

```
327:             override fun validatePacketSecurity(packet: BitchatPacket, peerID: String): Boolean {
```
> تعريف دالة متجاوِزة (override) باسم «validatePacketSecurity» (التحقّق من أمن الحزمة) تأخذ معامِلَين «packet» من نوع حزمة بِتشات (BitchatPacket) و«peerID» من نوع النص (String) وتُعيد منطقياً (Boolean). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:327]

```
328:                 return securityManager.validatePacket(packet, peerID)
```
> يُعيد نتيجة استدعاء الدالة «validatePacket» على مدير الأمن (securityManager) ممرِّراً الحزمة «packet» ومعرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:328]

```
329:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:329]

```
330: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:330]

```
331:             override fun updatePeerLastSeen(peerID: String) {
```
> تعريف دالة متجاوِزة (override) باسم «updatePeerLastSeen» (تحديث آخر ظهور للقرين) تأخذ معامِلاً «peerID» من نوع النص (String) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:331]

```
332:                 peerManager.updatePeerLastSeen(peerID)
```
> يستدعي الدالة «updatePeerLastSeen» على مدير الأقران (peerManager) ممرِّراً معرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:332]

```
333:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:333]

```
334: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:334]

```
335:             override fun getPeerNickname(peerID: String): String? {
```
> تعريف دالة متجاوِزة (override) باسم «getPeerNickname» تأخذ معامِلاً «peerID» من نوع النص (String) وتُعيد نصاً قابلاً للإفراغ (String?). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:335]

```
336:                 return peerManager.getPeerNickname(peerID)
```
> يُعيد نتيجة استدعاء الدالة «getPeerNickname» على مدير الأقران (peerManager) ممرِّراً معرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:336]

```
337:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:337]

```
338: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:338]

```
339:             override fun getNetworkSize(): Int {
```
> تعريف دالة متجاوِزة (override) باسم «getNetworkSize» بلا معامِلات وتُعيد عدداً صحيحاً (Int). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:339]

```
340:                 return peerManager.getActivePeerCount()
```
> يُعيد نتيجة استدعاء الدالة «getActivePeerCount» على مدير الأقران (peerManager) بلا معامِلات. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:340]

```
341:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:341]

```
342: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:342]

```
343:             override fun getBroadcastRecipient(): ByteArray {
```
> تعريف دالة متجاوِزة (override) باسم «getBroadcastRecipient» بلا معامِلات وتُعيد مصفوفة بايت (ByteArray). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:343]

```
344:                 return SpecialRecipients.BROADCAST
```
> يُعيد الثابت «BROADCAST» من الكائن «SpecialRecipients» (المستقبِلون الخاصّون). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:344]

```
345:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:345]

```
346: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:346]

```
347:             override fun handleNoiseHandshake(routed: RoutedPacket): Boolean {
```
> تعريف دالة متجاوِزة (override) باسم «handleNoiseHandshake» (معالجة مصافحة نويز) تأخذ معامِلاً «routed» من نوع الحزمة الموجَّهة (RoutedPacket) وتُعيد منطقياً (Boolean). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:347]

```
348:                 return runBlocking { securityManager.handleNoiseHandshake(routed) }
```
> يُعيد نتيجة كتلة «runBlocking» (تشغيل حاجِب) التي تستدعي بداخلها الدالة المعلَّقة «handleNoiseHandshake» على مدير الأمن (securityManager) ممرِّراً الحزمة الموجَّهة «routed». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:348]

```
349:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:349]

```
350: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:350]

```
351:             override fun handleNoiseEncrypted(routed: RoutedPacket) {
```
> تعريف دالة متجاوِزة (override) باسم «handleNoiseEncrypted» (معالجة المشفَّر بنويز) تأخذ معامِلاً «routed» من نوع الحزمة الموجَّهة (RoutedPacket) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:351]

```
352:                 scope.launch { messageHandler.handleNoiseEncrypted(routed) }
```
> يُطلِق عبر «launch» على النطاق التزامُني (scope) معاملةً تستدعي الدالة «handleNoiseEncrypted» على معالِج الرسائل (messageHandler) ممرِّراً الحزمة الموجَّهة «routed». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:352]

```
353:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:353]

```
354: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:354]

```
355:             override fun handleAnnounce(routed: RoutedPacket) {
```
> تعريف دالة متجاوِزة (override) باسم «handleAnnounce» (معالجة الإعلان) تأخذ معامِلاً «routed» من نوع الحزمة الموجَّهة (RoutedPacket) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:355]

```
356:                 scope.launch {
```
> يُطلِق عبر «launch» على النطاق التزامُني (scope) معاملةً تُفتح كتلتها على أسطر تالية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:356]

```
357:                     val isFirst = messageHandler.handleAnnounce(routed)
```
> يُعرِّف متغيّراً ثابتاً «isFirst» (هل هو الأول) بقيمة نتيجة استدعاء الدالة «handleAnnounce» على معالِج الرسائل (messageHandler) ممرِّراً الحزمة الموجَّهة «routed». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:357]

```
358:                     hooks.onAnnounceProcessed?.invoke(routed, isFirst)
```
> يستدعي عبر «invoke» باستعمال الاستدعاء الآمن (?.) دالةَ الخطّاف «onAnnounceProcessed» من الكائن «hooks» ممرِّراً الحزمة الموجَّهة «routed» والقيمة «isFirst». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:358]

```
359:                     try { gossipSyncManager.onPublicPacketSeen(routed.packet) } catch (_: Exception) { }
```
> في كتلة محاولة (try) يستدعي الدالة «onPublicPacketSeen» على مدير مزامنة الإشاعة (gossipSyncManager) ممرِّراً «routed.packet» (حزمة الكائن الموجَّه)، وفي كتلة الالتقاط (catch) لأي استثناء (Exception) لا يفعل شيئاً. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:359]

```
360:                 }
```
> إغلاق نطاق كتلة الإطلاق (launch). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:360]

```
361:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:361]

```
362: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:362]

```
363:             override fun handleMessage(routed: RoutedPacket) {
```
> تعريف دالة متجاوِزة (override) باسم «handleMessage» (معالجة الرسالة) تأخذ معامِلاً «routed» من نوع الحزمة الموجَّهة (RoutedPacket) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:363]

```
364:                 scope.launch { messageHandler.handleMessage(routed) }
```
> يُطلِق عبر «launch» على النطاق التزامُني (scope) معاملةً تستدعي الدالة «handleMessage» على معالِج الرسائل (messageHandler) ممرِّراً الحزمة الموجَّهة «routed». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:364]

```
365:                 try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:365]

```
366:                     val pkt = routed.packet
```
> يُعرِّف متغيّراً ثابتاً «pkt» (الحزمة) بقيمة الخاصّية «packet» من الكائن الموجَّه «routed». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:366]

```
367:                     val isBroadcast = (pkt.recipientID == null || pkt.recipientID.contentEquals(SpecialRecipients.BROADCAST))
```
> يُعرِّف متغيّراً ثابتاً «isBroadcast» (هل هي بثّ) قيمته صحيحة إذا كان «recipientID» (معرّف المستقبِل) في الحزمة فارغاً (null) أو كان مساوياً بمحتواه للثابت «SpecialRecipients.BROADCAST». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:367]

```
368:                     if (isBroadcast && pkt.type == MessageType.MESSAGE.value) {
```
> شرط: إذا كانت «isBroadcast» صحيحة وكان نوع الحزمة «pkt.type» مساوياً لقيمة «MessageType.MESSAGE.value» (قيمة نوع الرسالة RSALH). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:368]

```
369:                         gossipSyncManager.onPublicPacketSeen(pkt)
```
> يستدعي الدالة «onPublicPacketSeen» على مدير مزامنة الإشاعة (gossipSyncManager) ممرِّراً الحزمة «pkt». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:369]

```
370:                     }
```
> إغلاق نطاق كتلة الشرط (if). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:370]

```
371:                 } catch (_: Exception) { }
```
> كتلة التقاط (catch) لأي استثناء (Exception) متجاهِلةً مرجعه (_) لا تفعل شيئاً. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:371]

```
372:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:372]

```
373: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:373]

```
374:             override fun handleLeave(routed: RoutedPacket) {
```
> تعريف دالة متجاوِزة (override) باسم «handleLeave» (معالجة المغادرة) تأخذ معامِلاً «routed» من نوع الحزمة الموجَّهة (RoutedPacket) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:374]

```
375:                 scope.launch { messageHandler.handleLeave(routed) }
```
> يُطلِق عبر «launch» على النطاق التزامُني (scope) معاملةً تستدعي الدالة «handleLeave» على معالِج الرسائل (messageHandler) ممرِّراً الحزمة الموجَّهة «routed». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:375]

```
376:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:376]

```
377: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:377]

```
378:             override fun handleFragment(packet: BitchatPacket): BitchatPacket? {
```
> تعريف دالة متجاوِزة (override) باسم «handleFragment» (معالجة الجزء/الشظيّة) تأخذ معامِلاً «packet» من نوع حزمة بِتشات (BitchatPacket) وتُعيد حزمة بِتشات قابلة للإفراغ (BitchatPacket?). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:378]

```
379:                 try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:379]

```
380:                     val isBroadcast = (packet.recipientID == null || packet.recipientID.contentEquals(SpecialRecipients.BROADCAST))
```
> يُعرِّف متغيّراً ثابتاً «isBroadcast» (هل هي بثّ) قيمته صحيحة إذا كان «recipientID» (معرّف المستقبِل) في الحزمة فارغاً (null) أو كان مساوياً بمحتواه للثابت «SpecialRecipients.BROADCAST». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:380]

```
381:                     if (isBroadcast && packet.type == MessageType.FRAGMENT.value) {
```
> شرط: إذا كانت «isBroadcast» صحيحة وكان نوع الحزمة «packet.type» مساوياً لقيمة «MessageType.FRAGMENT.value» (قيمة نوع الجزء/الشظيّة). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:381]

```
382:                         gossipSyncManager.onPublicPacketSeen(packet)
```
> يستدعي الدالة «onPublicPacketSeen» على مدير مزامنة الإشاعة (gossipSyncManager) ممرِّراً الحزمة «packet». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:382]

```
383:                     }
```
> إغلاق نطاق كتلة الشرط (if). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:383]

```
384:                 } catch (_: Exception) { }
```
> كتلة التقاط (catch) لأي استثناء (Exception) متجاهِلةً مرجعه (_) لا تفعل شيئاً. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:384]

```
385:                 return fragmentManager.handleFragment(packet)
```
> يُعيد نتيجة استدعاء الدالة «handleFragment» على مدير الأجزاء (fragmentManager) ممرِّراً الحزمة «packet». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:385]

```
386:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:386]

```
387: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:387]

```
388:             override fun sendAnnouncementToPeer(peerID: String) {
```
> تعريف دالة متجاوِزة (override) باسم «sendAnnouncementToPeer» (إرسال الإعلان إلى القرين) تأخذ معامِلاً «peerID» من نوع النص (String) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:388]

```
389:                 this@MeshCore.sendAnnouncementToPeer(peerID)
```
> يستدعي الدالة «sendAnnouncementToPeer» على نسخة الصنف الخارجي «MeshCore» (عبر this@MeshCore) ممرِّراً معرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:389]

```
390:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:390]

```
391: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:391]

```
392:             override fun sendCachedMessages(peerID: String) {
```
> تعريف دالة متجاوِزة (override) باسم «sendCachedMessages» (إرسال الرسائل المُخزَّنة مؤقتاً) تأخذ معامِلاً «peerID» من نوع النص (String) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:392]

```
393:                 storeForwardManager.sendCachedMessages(peerID)
```
> يستدعي الدالة «sendCachedMessages» على مدير التخزين والتمرير (storeForwardManager) ممرِّراً معرّف القرين «peerID». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:393]

```
394:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:394]

```
395: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:395]

```
396:             override fun relayPacket(routed: RoutedPacket) {
```
> تعريف دالة متجاوِزة (override) باسم «relayPacket» (تمرير الحزمة) تأخذ معامِلاً «routed» من نوع الحزمة الموجَّهة (RoutedPacket) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:396]

```
397:                 dispatchGlobal(routed)
```
> يستدعي الدالة «dispatchGlobal» ممرِّراً الحزمة الموجَّهة «routed». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:397]

```
398:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:398]

```
399: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:399]

```
400:             override fun sendToPeer(peerID: String, routed: RoutedPacket): Boolean {
```
> بداية تعريف دالة متجاوِزة (override) باسم «sendToPeer» (الإرسال إلى القرين) تأخذ معامِلَين «peerID» من نوع النص (String) و«routed» من نوع الحزمة الموجَّهة (RoutedPacket) وتُعيد منطقياً (Boolean)؛ جسمها يمتدّ خارج المدى المشروح. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:400]
