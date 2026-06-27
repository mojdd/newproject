# شريحة — app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt (الأسطر 251–477)

```
251:     /**
```
> بداية تعليق توثيقي (KDoc) للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:251]

```
252:      * Get peer fingerprint for favorites/blocking
```
> تعليق: «الحصول على بصمة النِّدّ للمفضّلة/الحظر». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:252]

```
253:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:253]

```
254:     fun getPeerFingerprint(peerID: String): String? {
```
> تعريف دالة جلب بصمة النِّدّ (getPeerFingerprint) تأخذ مُعرِّف النِّدّ (peerID) من نوع نص (String) وتُعيد نصاً قابلاً للقيمة الفارغة (String?). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:254]

```
255:         return noiseService.getPeerFingerprint(peerID)
```
> تُعيد الدالة نتيجة استدعاء getPeerFingerprint على خدمة نويز (noiseService) ممرِّرةً مُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:255]

```
256:     }
```
> إغلاق نطاق دالة getPeerFingerprint. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:256]

```
257:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:257]

```
258:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:258]

```
259:      * Get current peer ID for a fingerprint (for peer ID rotation)
```
> تعليق: «الحصول على مُعرِّف النِّدّ الحالي مقابل بصمة (لتدوير مُعرِّف النِّدّ)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:259]

```
260:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:260]

```
261:     fun getCurrentPeerID(fingerprint: String): String? {
```
> تعريف دالة جلب مُعرِّف النِّدّ الحالي (getCurrentPeerID) تأخذ بصمة (fingerprint) من نوع نص وتُعيد نصاً قابلاً للقيمة الفارغة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:261]

```
262:         return noiseService.getPeerID(fingerprint)
```
> تُعيد الدالة نتيجة استدعاء getPeerID على خدمة نويز ممرِّرةً البصمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:262]

```
263:     }
```
> إغلاق نطاق دالة getCurrentPeerID. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:263]

```
264:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:264]

```
265:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:265]

```
266:      * Initiate a Noise handshake with a peer
```
> تعليق: «بدء مصافحة نويز (Noise handshake) مع نِدّ». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:266]

```
267:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:267]

```
268:     fun initiateHandshake(peerID: String): ByteArray? {
```
> تعريف دالة بدء المصافحة (initiateHandshake) تأخذ مُعرِّف النِّدّ من نوع نص وتُعيد مصفوفة بايتات (ByteArray) قابلة للقيمة الفارغة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:268]

```
269:         Log.d(TAG, "🤝 Initiating Noise handshake with $peerID")
```
> تسجيل رسالة تصحيح (Log.d) بالوسم (TAG) نصها «🤝 بدء مصافحة نويز مع $peerID» مع إدراج قيمة مُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:269]

```
270:         return noiseService.initiateHandshake(peerID)
```
> تُعيد الدالة نتيجة استدعاء initiateHandshake على خدمة نويز ممرِّرةً مُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:270]

```
271:     }
```
> إغلاق نطاق دالة initiateHandshake. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:271]

```
272:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:272]

```
273:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:273]

```
274:      * Process an incoming handshake message
```
> تعليق: «معالجة رسالة مصافحة واردة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:274]

```
275:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:275]

```
276:     fun processHandshakeMessage(data: ByteArray, peerID: String): ByteArray? {
```
> تعريف دالة معالجة رسالة المصافحة (processHandshakeMessage) تأخذ بيانات (data) من نوع مصفوفة بايتات ومُعرِّف النِّدّ من نوع نص وتُعيد مصفوفة بايتات قابلة للقيمة الفارغة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:276]

```
277:         Log.d(TAG, "🤝 Processing handshake message from $peerID")
```
> تسجيل رسالة تصحيح بالوسم نصها «🤝 معالجة رسالة مصافحة من $peerID» مع إدراج مُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:277]

```
278:         return noiseService.processHandshakeMessage(data, peerID)
```
> تُعيد الدالة نتيجة استدعاء processHandshakeMessage على خدمة نويز ممرِّرةً البيانات ومُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:278]

```
279:     }
```
> إغلاق نطاق دالة processHandshakeMessage. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:279]

```
280:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:280]

```
281:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:281]

```
282:      * Remove a peer session (called when peer disconnects)
```
> تعليق: «إزالة جلسة نِدّ (تُستدعى عند انقطاع النِّدّ)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:282]

```
283:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:283]

```
284:     fun removePeer(peerID: String) {
```
> تعريف دالة إزالة النِّدّ (removePeer) تأخذ مُعرِّف النِّدّ من نوع نص ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:284]

```
285:         establishedSessions.remove(peerID)
```
> استدعاء remove على خريطة الجلسات المُنشأة (establishedSessions) لحذف المُدخَل المرتبط بمُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:285]

```
286:         noiseService.removePeer(peerID)
```
> استدعاء removePeer على خدمة نويز ممرِّراً مُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:286]

```
287:         onSessionLost?.invoke(peerID)
```
> استدعاء دالة الاستدعاء الخلفي عند فقد الجلسة (onSessionLost) إن لم تكن فارغة، ممرِّراً مُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:287]

```
288:         Log.d(TAG, "🗑️ Removed session for $peerID")
```
> تسجيل رسالة تصحيح بالوسم نصها «🗑️ أُزيلت الجلسة لـ $peerID» مع إدراج مُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:288]

```
289:     }
```
> إغلاق نطاق دالة removePeer. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:289]

```
290:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:290]

```
291:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:291]

```
292:      * Update peer ID mapping (for peer ID rotation)
```
> تعليق: «تحديث ربط مُعرِّف النِّدّ (لتدوير مُعرِّف النِّدّ)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:292]

```
293:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:293]

```
294:     fun updatePeerIDMapping(oldPeerID: String?, newPeerID: String, fingerprint: String) {
```
> تعريف دالة تحديث ربط مُعرِّف النِّدّ (updatePeerIDMapping) تأخذ مُعرِّف النِّدّ القديم (oldPeerID) نصاً قابلاً للقيمة الفارغة، ومُعرِّف النِّدّ الجديد (newPeerID) نصاً، وبصمة نصاً، ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:294]

```
295:         oldPeerID?.let { establishedSessions.remove(it) }
```
> إن لم يكن مُعرِّف النِّدّ القديم فارغاً، يُحذف المُدخَل المرتبط به من خريطة الجلسات المُنشأة عبر let وremove. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:295]

```
296:         establishedSessions[newPeerID] = fingerprint
```
> إسناد البصمة كقيمة لمفتاح مُعرِّف النِّدّ الجديد في خريطة الجلسات المُنشأة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:296]

```
297:         noiseService.updatePeerIDMapping(oldPeerID, newPeerID, fingerprint)
```
> استدعاء updatePeerIDMapping على خدمة نويز ممرِّراً مُعرِّف النِّدّ القديم والجديد والبصمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:297]

```
298:     }
```
> إغلاق نطاق دالة updatePeerIDMapping. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:298]

```
299:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:299]

```
300:     // MARK: - Channel Encryption
```
> تعليق: «MARK: - تشفير القناة» (علامة تقسيم للقسم). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:300]

```
301:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:301]

```
302:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:302]

```
303:      * Set password for a channel (derives encryption key using Argon2id)
```
> تعليق: «ضبط كلمة مرور لقناة (يشتق مفتاح التشفير باستخدام Argon2id)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:303]

```
304:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:304]

```
305:     fun setChannelPassword(password: String, channel: String) {
```
> تعريف دالة ضبط كلمة مرور القناة (setChannelPassword) تأخذ كلمة المرور (password) نصاً والقناة (channel) نصاً ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:305]

```
306:         noiseService.setChannelPassword(password, channel)
```
> استدعاء setChannelPassword على خدمة نويز ممرِّراً كلمة المرور والقناة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:306]

```
307:     }
```
> إغلاق نطاق دالة setChannelPassword. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:307]

```
308:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:308]

```
309:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:309]

```
310:      * Encrypt message for a password-protected channel
```
> تعليق: «تشفير رسالة لقناة محميّة بكلمة مرور». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:310]

```
311:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:311]

```
312:     fun encryptChannelMessage(message: String, channel: String): ByteArray? {
```
> تعريف دالة تشفير رسالة القناة (encryptChannelMessage) تأخذ الرسالة (message) نصاً والقناة نصاً وتُعيد مصفوفة بايتات قابلة للقيمة الفارغة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:312]

```
313:         return noiseService.encryptChannelMessage(message, channel)
```
> تُعيد الدالة نتيجة استدعاء encryptChannelMessage على خدمة نويز ممرِّرةً الرسالة والقناة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:313]

```
314:     }
```
> إغلاق نطاق دالة encryptChannelMessage. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:314]

```
315:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:315]

```
316:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:316]

```
317:      * Decrypt channel message
```
> تعليق: «فك تشفير رسالة القناة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:317]

```
318:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:318]

```
319:     fun decryptChannelMessage(encryptedData: ByteArray, channel: String): String? {
```
> تعريف دالة فك تشفير رسالة القناة (decryptChannelMessage) تأخذ البيانات المشفّرة (encryptedData) مصفوفة بايتات والقناة نصاً وتُعيد نصاً قابلاً للقيمة الفارغة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:319]

```
320:         return noiseService.decryptChannelMessage(encryptedData, channel)
```
> تُعيد الدالة نتيجة استدعاء decryptChannelMessage على خدمة نويز ممرِّرةً البيانات المشفّرة والقناة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:320]

```
321:     }
```
> إغلاق نطاق دالة decryptChannelMessage. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:321]

```
322:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:322]

```
323:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:323]

```
324:      * Remove channel password (when leaving channel)
```
> تعليق: «إزالة كلمة مرور القناة (عند مغادرة القناة)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:324]

```
325:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:325]

```
326:     fun removeChannelPassword(channel: String) {
```
> تعريف دالة إزالة كلمة مرور القناة (removeChannelPassword) تأخذ القناة نصاً ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:326]

```
327:         noiseService.removeChannelPassword(channel)
```
> استدعاء removeChannelPassword على خدمة نويز ممرِّراً القناة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:327]

```
328:     }
```
> إغلاق نطاق دالة removeChannelPassword. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:328]

```
329:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:329]

```
330:     // MARK: - Session Management
```
> تعليق: «MARK: - إدارة الجلسة» (علامة تقسيم للقسم). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:330]

```
331:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:331]

```
332:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:332]

```
333:      * Get all peers with established sessions
```
> تعليق: «الحصول على كل الأنداد ذوي الجلسات المُنشأة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:333]

```
334:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:334]

```
335:     fun getEstablishedPeers(): List<String> {
```
> تعريف دالة جلب الأنداد المُنشأة جلساتهم (getEstablishedPeers) لا تأخذ مُعطيات وتُعيد قائمة نصوص (List<String>). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:335]

```
336:         return establishedSessions.keys.toList()
```
> تُعيد الدالة مفاتيح خريطة الجلسات المُنشأة محوّلةً إلى قائمة عبر toList. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:336]

```
337:     }
```
> إغلاق نطاق دالة getEstablishedPeers. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:337]

```
338:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:338]

```
339:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:339]

```
340:      * Get sessions that need rekeying
```
> تعليق: «الحصول على الجلسات التي تحتاج إعادة توليد مفتاح». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:340]

```
341:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:341]

```
342:     fun getSessionsNeedingRekey(): List<String> {
```
> تعريف دالة جلب الجلسات المحتاجة لإعادة المفتاح (getSessionsNeedingRekey) لا تأخذ مُعطيات وتُعيد قائمة نصوص. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:342]

```
343:         return noiseService.getSessionsNeedingRekey()
```
> تُعيد الدالة نتيجة استدعاء getSessionsNeedingRekey على خدمة نويز. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:343]

```
344:     }
```
> إغلاق نطاق دالة getSessionsNeedingRekey. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:344]

```
345:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:345]

```
346:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:346]

```
347:      * Initiate rekey for a session
```
> تعليق: «بدء إعادة توليد المفتاح لجلسة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:347]

```
348:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:348]

```
349:     fun initiateRekey(peerID: String): ByteArray? {
```
> تعريف دالة بدء إعادة المفتاح (initiateRekey) تأخذ مُعرِّف النِّدّ نصاً وتُعيد مصفوفة بايتات قابلة للقيمة الفارغة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:349]

```
350:         Log.d(TAG, "🔄 Initiating rekey for $peerID")
```
> تسجيل رسالة تصحيح بالوسم نصها «🔄 بدء إعادة المفتاح لـ $peerID» مع إدراج مُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:350]

```
351:         establishedSessions.remove(peerID) // Will be re-added when new session is established
```
> حذف المُدخَل المرتبط بمُعرِّف النِّدّ من خريطة الجلسات المُنشأة، مع تعليق: «سيُعاد إضافته عند إنشاء جلسة جديدة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:351]

```
352:         return noiseService.initiateRekey(peerID)
```
> تُعيد الدالة نتيجة استدعاء initiateRekey على خدمة نويز ممرِّرةً مُعرِّف النِّدّ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:352]

```
353:     }
```
> إغلاق نطاق دالة initiateRekey. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:353]

```
354:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:354]

```
355:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:355]

```
356:      * Get our identity fingerprint
```
> تعليق: «الحصول على بصمة هويّتنا». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:356]

```
357:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:357]

```
358:     fun getIdentityFingerprint(): String {
```
> تعريف دالة جلب بصمة الهويّة (getIdentityFingerprint) لا تأخذ مُعطيات وتُعيد نصاً. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:358]

```
359:         return noiseService.getIdentityFingerprint()
```
> تُعيد الدالة نتيجة استدعاء getIdentityFingerprint على خدمة نويز. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:359]

```
360:     }
```
> إغلاق نطاق دالة getIdentityFingerprint. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:360]

```
361:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:361]

```
362:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:362]

```
363:      * Get debug information about encryption state
```
> تعليق: «الحصول على معلومات تصحيح عن حالة التشفير». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:363]

```
364:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:364]

```
365:     fun getDebugInfo(): String = buildString {
```
> تعريف دالة جلب معلومات التصحيح (getDebugInfo) تُعيد نصاً مبنيّاً عبر buildString، وجسمها تعبير لمبنى النص. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:365]

```
366:         appendLine("=== EncryptionService Debug ===")
```
> إلحاق سطر (appendLine) بالنص المبني نصه الحرفي «=== EncryptionService Debug ===». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:366]

```
367:         appendLine("Established Sessions: ${establishedSessions.size}")
```
> إلحاق سطر نصه «Established Sessions: » متبوعاً بحجم خريطة الجلسات المُنشأة (size). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:367]

```
368:         appendLine("Our Fingerprint: ${getIdentityFingerprint().take(16)}...")
```
> إلحاق سطر نصه «Our Fingerprint: » متبوعاً بأول ١٦ محرفاً من بصمة الهويّة (take(16)) ثم النقاط الثلاث «...». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:368]

```
369:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:369]

```
370:         if (establishedSessions.isNotEmpty()) {
```
> شرط: إن لم تكن خريطة الجلسات المُنشأة فارغة (isNotEmpty) يُنفَّذ ما بداخل الكتلة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:370]

```
371:             appendLine("Active Encrypted Sessions:")
```
> إلحاق سطر نصه الحرفي «Active Encrypted Sessions:». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:371]

```
372:             establishedSessions.forEach { (peerID, fingerprint) ->
```
> تكرار على كل مُدخَل في خريطة الجلسات المُنشأة (forEach) بتفكيك المفتاح إلى مُعرِّف النِّدّ والقيمة إلى البصمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:372]

```
373:                 appendLine("  $peerID -> ${fingerprint.take(16)}...")
```
> إلحاق سطر نصه مسافتان ثم مُعرِّف النِّدّ ثم « -> » ثم أول ١٦ محرفاً من البصمة ثم «...». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:373]

```
374:             }
```
> إغلاق نطاق كتلة forEach. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:374]

```
375:         }
```
> إغلاق نطاق كتلة الشرط if. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:375]

```
376:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:376]

```
377:         appendLine("")
```
> إلحاق سطر فارغ بالنص المبني (نص حرفي خالٍ). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:377]

```
378:         appendLine(noiseService.toString()) // Include NoiseService state
```
> إلحاق سطر بنتيجة toString على خدمة نويز، مع تعليق: «تضمين حالة NoiseService». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:378]

```
379:     }
```
> إغلاق نطاق دالة getDebugInfo. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:379]

```
380:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:380]

```
381:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:381]

```
382:      * Shutdown encryption service
```
> تعليق: «إيقاف خدمة التشفير». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:382]

```
383:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:383]

```
384:     fun shutdown() {
```
> تعريف دالة الإيقاف (shutdown) لا تأخذ مُعطيات ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:384]

```
385:         establishedSessions.clear()
```
> استدعاء clear على خريطة الجلسات المُنشأة لإفراغها من كل المُدخَلات. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:385]

```
386:         noiseService.shutdown()
```
> استدعاء shutdown على خدمة نويز. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:386]

```
387:         Log.d(TAG, "🔌 EncryptionService shut down")
```
> تسجيل رسالة تصحيح بالوسم نصها الحرفي «🔌 EncryptionService shut down». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:387]

```
388:     }
```
> إغلاق نطاق دالة shutdown. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:388]

```
389:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:389]

```
390:     // MARK: - Ed25519 Signature Verification
```
> تعليق: «MARK: - التحقق من توقيع Ed25519» (علامة تقسيم للقسم). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:390]

```
391:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:391]

```
392:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:392]

```
393:      * Verify Ed25519 signature against data using a public key
```
> تعليق: «التحقق من توقيع Ed25519 مقابل بيانات باستخدام مفتاح عام». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:393]

```
394:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:394]

```
395:     open fun verifyEd25519Signature(signature: ByteArray, data: ByteArray, publicKeyBytes: ByteArray): Boolean {
```
> تعريف دالة قابلة للتجاوز (open) للتحقق من توقيع Ed25519 (verifyEd25519Signature) تأخذ التوقيع (signature) ومصفوفة البيانات (data) وبايتات المفتاح العام (publicKeyBytes) كلها مصفوفات بايتات وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:395]

```
396:         return try {
```
> بدء كتلة محاولة (try) تُعاد قيمتها كنتيجة الدالة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:396]

```
397:             val publicKey = Ed25519PublicKeyParameters(publicKeyBytes, 0)
```
> تعريف متغيّر المفتاح العام (publicKey) بإنشاء كائن مُعاملات المفتاح العام Ed25519 (Ed25519PublicKeyParameters) من بايتات المفتاح العام بإزاحة (offset) صفر. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:397]

```
398:             val verifier = Ed25519Signer()
```
> تعريف متغيّر المُحقِّق (verifier) بإنشاء كائن موقِّع Ed25519 (Ed25519Signer). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:398]

```
399:             verifier.init(false, publicKey)
```
> استدعاء init على المُحقِّق بمُعطى false (وضع التحقق لا التوقيع) والمفتاح العام. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:399]

```
400:             verifier.update(data, 0, data.size)
```
> استدعاء update على المُحقِّق ممرِّراً البيانات من الإزاحة صفر بطول حجم البيانات (data.size). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:400]

```
401:             val isValid = verifier.verifySignature(signature)
```
> تعريف متغيّر الصلاحية (isValid) بنتيجة استدعاء verifySignature على المُحقِّق ممرِّراً التوقيع. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:401]

```
402:             Log.d(TAG, "✅ Ed25519 signature verification: $isValid")
```
> تسجيل رسالة تصحيح بالوسم نصها «✅ التحقق من توقيع Ed25519: $isValid» مع إدراج قيمة الصلاحية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:402]

```
403:             isValid
```
> قيمة الصلاحية تُمثِّل القيمة المُعادة من كتلة المحاولة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:403]

```
404:         } catch (e: Exception) {
```
> بدء كتلة التقاط الاستثناء (catch) للاستثناء (e) من نوع Exception. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:404]

```
405:             Log.e(TAG, "❌ Failed to verify Ed25519 signature: ${e.message}")
```
> تسجيل رسالة خطأ (Log.e) بالوسم نصها «❌ فشل التحقق من توقيع Ed25519: » متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:405]

```
406:             false
```
> قيمة false تُمثِّل القيمة المُعادة من كتلة التقاط الاستثناء. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:406]

```
407:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط (try/catch). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:407]

```
408:     }
```
> إغلاق نطاق دالة verifyEd25519Signature. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:408]

```
409:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:409]

```
410:     // MARK: - Private Key Management
```
> تعليق: «MARK: - إدارة المفتاح الخاص» (علامة تقسيم للقسم). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:410]

```
411:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:411]

```
412:     /**
```
> بداية تعليق توثيقي للدالة التالية. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:412]

```
413:      * Load existing Ed25519 key pair from preferences or create a new one
```
> تعليق: «تحميل زوج مفاتيح Ed25519 موجود من التفضيلات أو إنشاء زوج جديد». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:413]

```
414:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:414]

```
415:     private fun loadOrCreateEd25519KeyPair(): AsymmetricCipherKeyPair {
```
> تعريف دالة خاصّة (private) لتحميل أو إنشاء زوج مفاتيح Ed25519 (loadOrCreateEd25519KeyPair) لا تأخذ مُعطيات وتُعيد زوج مفاتيح تشفير غير متماثل (AsymmetricCipherKeyPair). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:415]

```
416:         // Migrate legacy plaintext Ed25519 key to encrypted storage if present
```
> تعليق: «ترحيل مفتاح Ed25519 القديم النصّي الصريح إلى تخزين مشفّر إن وُجد». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:416]

```
417:         migrateOldEd25519KeyIfNeeded()
```
> استدعاء دالة ترحيل المفتاح القديم عند الحاجة (migrateOldEd25519KeyIfNeeded). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:417]

```
418:         try {
```
> بدء كتلة محاولة (try). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:418]

```
419:             val storedKey = prefs.getString(ED25519_PRIVATE_KEY_PREF, null)
```
> تعريف متغيّر المفتاح المخزَّن (storedKey) بقراءة نص من التفضيلات (prefs) بمفتاح ثابت مفتاح Ed25519 الخاص (ED25519_PRIVATE_KEY_PREF) وقيمة افتراضية null. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:419]

```
420:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:420]

```
421:             if (storedKey != null) {
```
> شرط: إن لم يكن المفتاح المخزَّن فارغاً (null) يُنفَّذ ما بداخل الكتلة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:421]

```
422:                 // Load existing key
```
> تعليق: «تحميل المفتاح الموجود». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:422]

```
423:                 val privateKeyBytes = Base64.decode(storedKey, Base64.DEFAULT)
```
> تعريف متغيّر بايتات المفتاح الخاص (privateKeyBytes) بفكّ ترميز المفتاح المخزَّن من Base64 بالوضع الافتراضي (Base64.DEFAULT). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:423]

```
424:                 val privateKey = Ed25519PrivateKeyParameters(privateKeyBytes, 0)
```
> تعريف متغيّر المفتاح الخاص (privateKey) بإنشاء كائن مُعاملات المفتاح الخاص Ed25519 (Ed25519PrivateKeyParameters) من بايتات المفتاح بإزاحة صفر. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:424]

```
425:                 val publicKey = privateKey.generatePublicKey()
```
> تعريف متغيّر المفتاح العام (publicKey) باستدعاء generatePublicKey على المفتاح الخاص. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:425]

```
426:                 Log.d(TAG, "✅ Loaded existing Ed25519 signing key pair")
```
> تسجيل رسالة تصحيح بالوسم نصها الحرفي «✅ Loaded existing Ed25519 signing key pair». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:426]

```
427:                 return AsymmetricCipherKeyPair(publicKey, privateKey)
```
> إعادة كائن زوج مفاتيح تشفير غير متماثل مُنشأ من المفتاح العام والمفتاح الخاص. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:427]

```
428:             }
```
> إغلاق نطاق كتلة الشرط if. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:428]

```
429:         } catch (e: Exception) {
```
> بدء كتلة التقاط الاستثناء للاستثناء (e) من نوع Exception. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:429]

```
430:             Log.w(TAG, "⚠️ Failed to load existing Ed25519 key, creating new one: ${e.message}")
```
> تسجيل رسالة تحذير (Log.w) بالوسم نصها «⚠️ فشل تحميل مفتاح Ed25519 الموجود، إنشاء جديد: » متبوعاً برسالة الاستثناء. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:430]

```
431:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:431]

```
432:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:432]

```
433:         // Create new key pair
```
> تعليق: «إنشاء زوج مفاتيح جديد». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:433]

```
434:         return generateAndSaveEd25519KeyPair()
```
> إعادة نتيجة استدعاء دالة توليد وحفظ زوج مفاتيح Ed25519 (generateAndSaveEd25519KeyPair). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:434]

```
435:     }
```
> إغلاق نطاق دالة loadOrCreateEd25519KeyPair. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:435]

```
436:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:436]

```
437:     fun generateAndSaveEd25519KeyPair(): AsymmetricCipherKeyPair {
```
> تعريف دالة توليد وحفظ زوج مفاتيح Ed25519 (generateAndSaveEd25519KeyPair) لا تأخذ مُعطيات وتُعيد زوج مفاتيح تشفير غير متماثل. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:437]

```
438:         val keyGen = Ed25519KeyPairGenerator()
```
> تعريف متغيّر مولِّد المفاتيح (keyGen) بإنشاء كائن مولِّد زوج مفاتيح Ed25519 (Ed25519KeyPairGenerator). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:438]

```
439:         keyGen.init(Ed25519KeyGenerationParameters(SecureRandom()))
```
> استدعاء init على مولِّد المفاتيح بمُعطى مُعاملات توليد مفاتيح Ed25519 (Ed25519KeyGenerationParameters) مُنشأة بمولِّد عشوائي آمن (SecureRandom). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:439]

```
440:         val keyPair = keyGen.generateKeyPair()
```
> تعريف متغيّر زوج المفاتيح (keyPair) بنتيجة استدعاء generateKeyPair على مولِّد المفاتيح. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:440]

```
441:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:441]

```
442:         // Store private key in preferences
```
> تعليق: «تخزين المفتاح الخاص في التفضيلات». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:442]

```
443:         try {
```
> بدء كتلة محاولة (try). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:443]

```
444:             val privateKey = keyPair.private as Ed25519PrivateKeyParameters
```
> تعريف متغيّر المفتاح الخاص (privateKey) بأخذ الجزء الخاص من زوج المفاتيح وتحويله (as) إلى نوع مُعاملات المفتاح الخاص Ed25519. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:444]

```
445:             val privateKeyBytes = privateKey.encoded
```
> تعريف متغيّر بايتات المفتاح الخاص (privateKeyBytes) بقراءة الخاصيّة encoded من المفتاح الخاص. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:445]

```
446:             val encodedKey = Base64.encodeToString(privateKeyBytes, Base64.DEFAULT)
```
> تعريف متغيّر المفتاح المُرمَّز (encodedKey) بترميز بايتات المفتاح الخاص إلى نص Base64 بالوضع الافتراضي. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:446]

```
447:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:447]

```
448:             prefs.edit { putString(ED25519_PRIVATE_KEY_PREF, encodedKey) }
```
> تحرير التفضيلات عبر edit وكتابة نص (putString) بمفتاح ثابت مفتاح Ed25519 الخاص وقيمة المفتاح المُرمَّز. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:448]

```
449:             Log.d(TAG, "✅ Created and stored new Ed25519 signing key pair")
```
> تسجيل رسالة تصحيح بالوسم نصها الحرفي «✅ Created and stored new Ed25519 signing key pair». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:449]

```
450:         } catch (e: Exception) {
```
> بدء كتلة التقاط الاستثناء للاستثناء (e) من نوع Exception. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:450]

```
451:             Log.e(TAG, "❌ Failed to store Ed25519 private key: ${e.message}")
```
> تسجيل رسالة خطأ بالوسم نصها «❌ فشل تخزين مفتاح Ed25519 الخاص: » متبوعاً برسالة الاستثناء. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:451]

```
452:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:452]

```
453:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:453]

```
454:         return keyPair
```
> إعادة زوج المفاتيح. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:454]

```
455:     }
```
> إغلاق نطاق دالة generateAndSaveEd25519KeyPair. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:455]

```
456:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:456]

```
457:     private fun migrateOldEd25519KeyIfNeeded() {
```
> تعريف دالة خاصّة لترحيل المفتاح القديم عند الحاجة (migrateOldEd25519KeyIfNeeded) لا تأخذ مُعطيات ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:457]

```
458:         try {
```
> بدء كتلة محاولة (try). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:458]

```
459:             // old existing plain text preference
```
> تعليق: «تفضيل نصّي صريح قديم موجود». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:459]

```
460:             val oldPrefs = context.getSharedPreferences(OLD_PREFS_NAME, Context.MODE_PRIVATE)
```
> تعريف متغيّر التفضيلات القديمة (oldPrefs) بجلب تفضيلات مشتركة من السياق (context) باسم الثابت اسم التفضيلات القديمة (OLD_PREFS_NAME) ووضع خاص (Context.MODE_PRIVATE). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:460]

```
461:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:461]

```
462:             val oldKey = oldPrefs.getString(ED25519_PRIVATE_KEY_PREF, null)
```
> تعريف متغيّر المفتاح القديم (oldKey) بقراءة نص من التفضيلات القديمة بمفتاح ثابت مفتاح Ed25519 الخاص وقيمة افتراضية null. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:462]

```
463:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:463]

```
464:             if (oldKey != null && !prefs.contains(ED25519_PRIVATE_KEY_PREF)) {
```
> شرط: إن لم يكن المفتاح القديم فارغاً وفي الوقت ذاته لا تحتوي التفضيلات (prefs) على مفتاح Ed25519 الخاص (contains) يُنفَّذ ما بداخل الكتلة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:464]

```
465:                 prefs.edit {
```
> تحرير التفضيلات المشفّرة (prefs) عبر edit بفتح كتلة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:465]

```
466:                     putString(ED25519_PRIVATE_KEY_PREF, oldKey)
```
> كتابة نص (putString) بمفتاح ثابت مفتاح Ed25519 الخاص وقيمة المفتاح القديم. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:466]

```
467:                 }
```
> إغلاق نطاق كتلة تحرير التفضيلات. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:467]

```
468:                 oldPrefs.edit {
```
> تحرير التفضيلات القديمة (oldPrefs) عبر edit بفتح كتلة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:468]

```
469:                     remove(ED25519_PRIVATE_KEY_PREF)
```
> حذف (remove) المُدخَل بمفتاح ثابت مفتاح Ed25519 الخاص من التفضيلات القديمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:469]

```
470:                 }
```
> إغلاق نطاق كتلة تحرير التفضيلات القديمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:470]

```
471:                 Log.d(TAG, "🔁 Migrated Ed25519 key to EncryptedSharedPreferences")
```
> تسجيل رسالة تصحيح بالوسم نصها الحرفي «🔁 Migrated Ed25519 key to EncryptedSharedPreferences». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:471]

```
472:             }
```
> إغلاق نطاق كتلة الشرط if. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:472]

```
473:         } catch (e: Exception) {
```
> بدء كتلة التقاط الاستثناء للاستثناء (e) من نوع Exception. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:473]

```
474:             Log.w(TAG, "⚠️ Failed to migrate Ed25519 key; generating new identity: ${e.message}")
```
> تسجيل رسالة تحذير بالوسم نصها «⚠️ فشل ترحيل مفتاح Ed25519؛ توليد هويّة جديدة: » متبوعاً برسالة الاستثناء. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:474]

```
475:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:475]

```
476:     }
```
> إغلاق نطاق دالة migrateOldEd25519KeyIfNeeded. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:476]

```
477: }
```
> إغلاق نطاق صنف خدمة التشفير (EncryptionService). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:477]
