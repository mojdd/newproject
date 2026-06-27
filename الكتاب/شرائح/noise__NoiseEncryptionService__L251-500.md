# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt (الأسطر 251–500)

```
251:             null
```
> يُعيد القيمة الفارغة (null) كنتيجة لفرع المعالجة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:251]

```
252:         }
```
> إغلاق نطاق كتلة (block) سابقة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:252]

```
253:     }
```
> إغلاق نطاق دالة (function) سابقة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:253]

```
254:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:254]

```
255:     // MARK: - Peer Management
```
> تعليق: علامة قسم «إدارة النِّدّ (Peer Management)». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:255]

```
256:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:256]

```
257:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:257]

```
258:      * Get fingerprint for a peer (returns null if peer unknown)
```
> تعليق: «احصل على البصمة (fingerprint) لنِدّ — يُعيد null إن كان النِّدّ مجهولاً». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:258]

```
259:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:259]

```
260:     fun getPeerFingerprint(peerID: String): String? {
```
> تعريف دالة عامة (getPeerFingerprint) تأخذ مُعرّف النِّدّ (peerID) من نوع نص (String) وتُعيد نصاً قابلاً للقيمة الفارغة (String?). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:260]

```
261:         return fingerprintManager.getFingerprintForPeer(peerID)
```
> تُعيد نتيجة استدعاء الدالة getFingerprintForPeer على مدير البصمات (fingerprintManager) مع تمرير peerID. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:261]

```
262:     }
```
> إغلاق نطاق الدالة getPeerFingerprint. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:262]

```
263:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:263]

```
264:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:264]

```
265:      * Get current peer ID for a fingerprint (returns null if not currently online)
```
> تعليق: «احصل على مُعرّف النِّدّ الحالي لبصمة — يُعيد null إن لم يكن متصلاً حالياً». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:265]

```
266:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:266]

```
267:     fun getPeerID(fingerprint: String): String? {
```
> تعريف دالة عامة (getPeerID) تأخذ بصمة (fingerprint) من نوع نص وتُعيد نصاً قابلاً للقيمة الفارغة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:267]

```
268:         return fingerprintManager.getPeerIDForFingerprint(fingerprint)
```
> تُعيد نتيجة استدعاء الدالة getPeerIDForFingerprint على مدير البصمات مع تمرير fingerprint. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:268]

```
269:     }
```
> إغلاق نطاق الدالة getPeerID. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:269]

```
270:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:270]

```
271:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:271]

```
272:      * Remove a peer session (called when peer disconnects)
```
> تعليق: «أزِل جلسة (session) نِدّ — يُستدعى عند فصل اتصال النِّدّ». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:272]

```
273:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:273]

```
274:     fun removePeer(peerID: String) {
```
> تعريف دالة عامة (removePeer) تأخذ peerID من نوع نص ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:274]

```
275:         sessionManager.removeSession(peerID)
```
> تستدعي الدالة removeSession على مدير الجلسات (sessionManager) مع تمرير peerID. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:275]

```
276:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:276]

```
277:         // Clean up fingerprint mappings via centralized manager
```
> تعليق: «نظّف ربط البصمات عبر المدير المركزي». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:277]

```
278:         fingerprintManager.removePeer(peerID)
```
> تستدعي الدالة removePeer على مدير البصمات مع تمرير peerID. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:278]

```
279:     }
```
> إغلاق نطاق الدالة removePeer. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:279]

```
280:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:280]

```
281:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:281]

```
282:      * Update peer ID mapping (for peer ID rotation)
```
> تعليق: «حدّث ربط مُعرّف النِّدّ — لأجل تدوير مُعرّف النِّدّ (peer ID rotation)». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:282]

```
283:      * This allows favorites/blocking to persist across peer ID changes
```
> تعليق: «هذا يسمح للمفضّلين/الحظر بالبقاء عبر تغيّرات مُعرّف النِّدّ». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:283]

```
284:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:284]

```
285:     fun updatePeerIDMapping(oldPeerID: String?, newPeerID: String, fingerprint: String) {
```
> تعريف دالة عامة (updatePeerIDMapping) تأخذ المُعرّف القديم (oldPeerID) نصاً قابلاً للقيمة الفارغة، والمُعرّف الجديد (newPeerID) نصاً، وبصمة (fingerprint) نصاً، ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:285]

```
286:         // Use centralized fingerprint manager for peer ID rotation
```
> تعليق: «استخدم مدير البصمات المركزي لتدوير مُعرّف النِّدّ». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:286]

```
287:         fingerprintManager.updatePeerIDMapping(oldPeerID, newPeerID, fingerprint)
```
> تستدعي الدالة updatePeerIDMapping على مدير البصمات مع تمرير oldPeerID وnewPeerID وfingerprint. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:287]

```
288:     }
```
> إغلاق نطاق الدالة updatePeerIDMapping. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:288]

```
289:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:289]

```
290:     // MARK: - Channel Encryption
```
> تعليق: علامة قسم «تشفير القناة (Channel Encryption)». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:290]

```
291:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:291]

```
292:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:292]

```
293:      * Set password for a channel (derives encryption key)
```
> تعليق: «اضبط كلمة سرّ (password) لقناة — يشتق مفتاح التشفير». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:293]

```
294:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:294]

```
295:     fun setChannelPassword(password: String, channel: String) {
```
> تعريف دالة عامة (setChannelPassword) تأخذ كلمة السرّ (password) نصاً والقناة (channel) نصاً، ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:295]

```
296:         channelEncryption.setChannelPassword(password, channel)
```
> تستدعي الدالة setChannelPassword على كائن تشفير القناة (channelEncryption) مع تمرير password وchannel. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:296]

```
297:     }
```
> إغلاق نطاق الدالة setChannelPassword. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:297]

```
298:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:298]

```
299:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:299]

```
300:      * Encrypt message for a password-protected channel
```
> تعليق: «شفّر رسالة لقناة محميّة بكلمة سرّ». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:300]

```
301:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:301]

```
302:     fun encryptChannelMessage(message: String, channel: String): ByteArray? {
```
> تعريف دالة عامة (encryptChannelMessage) تأخذ الرسالة (message) نصاً والقناة نصاً وتُعيد مصفوفة بايتات (ByteArray) قابلة للقيمة الفارغة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:302]

```
303:         return try {
```
> تبدأ بإرجاع نتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:303]

```
304:             channelEncryption.encryptChannelMessage(message, channel)
```
> تستدعي الدالة encryptChannelMessage على كائن تشفير القناة مع تمرير message وchannel كقيمة الكتلة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:304]

```
305:         } catch (e: Exception) {
```
> تلتقط أي استثناء (Exception) في المتغيّر e. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:305]

```
306:             Log.e(TAG, "Failed to encrypt channel message for $channel: ${e.message}")
```
> تسجّل خطأً عبر Log.e بالوسم (TAG) ونصّ «Failed to encrypt channel message for $channel: ${e.message}» مع إدراج اسم القناة ورسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:306]

```
307:             null
```
> تُعيد القيمة الفارغة (null) كنتيجة لكتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:307]

```
308:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:308]

```
309:     }
```
> إغلاق نطاق الدالة encryptChannelMessage. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:309]

```
310:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:310]

```
311:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:311]

```
312:      * Decrypt channel message
```
> تعليق: «فكّ تشفير رسالة قناة». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:312]

```
313:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:313]

```
314:     fun decryptChannelMessage(encryptedData: ByteArray, channel: String): String? {
```
> تعريف دالة عامة (decryptChannelMessage) تأخذ البيانات المشفّرة (encryptedData) مصفوفة بايتات والقناة نصاً وتُعيد نصاً قابلاً للقيمة الفارغة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:314]

```
315:         return try {
```
> تبدأ بإرجاع نتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:315]

```
316:             channelEncryption.decryptChannelMessage(encryptedData, channel)
```
> تستدعي الدالة decryptChannelMessage على كائن تشفير القناة مع تمرير encryptedData وchannel كقيمة الكتلة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:316]

```
317:         } catch (e: Exception) {
```
> تلتقط أي استثناء في المتغيّر e. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:317]

```
318:             Log.e(TAG, "Failed to decrypt channel message for $channel: ${e.message}")
```
> تسجّل خطأً عبر Log.e بالوسم ونصّ «Failed to decrypt channel message for $channel: ${e.message}» مع إدراج اسم القناة ورسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:318]

```
319:             null
```
> تُعيد القيمة الفارغة (null) كنتيجة لكتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:319]

```
320:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:320]

```
321:     }
```
> إغلاق نطاق الدالة decryptChannelMessage. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:321]

```
322:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:322]

```
323:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:323]

```
324:      * Remove channel password (when leaving channel)
```
> تعليق: «أزِل كلمة سرّ القناة — عند مغادرة القناة». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:324]

```
325:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:325]

```
326:     fun removeChannelPassword(channel: String) {
```
> تعريف دالة عامة (removeChannelPassword) تأخذ القناة نصاً ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:326]

```
327:         channelEncryption.removeChannelPassword(channel)
```
> تستدعي الدالة removeChannelPassword على كائن تشفير القناة مع تمرير channel. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:327]

```
328:     }
```
> إغلاق نطاق الدالة removeChannelPassword. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:328]

```
329:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:329]

```
330:     // MARK: - Session Maintenance
```
> تعليق: علامة قسم «صيانة الجلسة (Session Maintenance)». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:330]

```
331:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:331]

```
332:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:332]

```
333:      * Get sessions that need rekey based on time or message count
```
> تعليق: «احصل على الجلسات التي تحتاج إعادة توليد المفتاح (rekey) بناءً على الوقت أو عدد الرسائل». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:333]

```
334:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:334]

```
335:     fun getSessionsNeedingRekey(): List<String> {
```
> تعريف دالة عامة (getSessionsNeedingRekey) لا تأخذ معاملات وتُعيد قائمة نصوص (List<String>). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:335]

```
336:         return sessionManager.getSessionsNeedingRekey()
```
> تُعيد نتيجة استدعاء الدالة getSessionsNeedingRekey على مدير الجلسات. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:336]

```
337:     }
```
> إغلاق نطاق الدالة getSessionsNeedingRekey. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:337]

```
338:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:338]

```
339:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:339]

```
340:      * Initiate rekey for a session (replaces old session with new handshake)
```
> تعليق: «ابدأ إعادة توليد المفتاح لجلسة — يستبدل الجلسة القديمة بمصافحة (handshake) جديدة». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:340]

```
341:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:341]

```
342:     fun initiateRekey(peerID: String): ByteArray? {
```
> تعريف دالة عامة (initiateRekey) تأخذ peerID نصاً وتُعيد مصفوفة بايتات قابلة للقيمة الفارغة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:342]

```
343:         Log.d(TAG, "Initiating rekey for session with $peerID")
```
> تسجّل رسالة تصحيح عبر Log.d بالوسم ونصّ «Initiating rekey for session with $peerID» مع إدراج peerID. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:343]

```
344:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:344]

```
345:         // Remove old session
```
> تعليق: «أزِل الجلسة القديمة». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:345]

```
346:         sessionManager.removeSession(peerID)
```
> تستدعي الدالة removeSession على مدير الجلسات مع تمرير peerID. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:346]

```
347:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:347]

```
348:         // Start new handshake
```
> تعليق: «ابدأ مصافحة جديدة». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:348]

```
349:         return initiateHandshake(peerID)
```
> تُعيد نتيجة استدعاء الدالة initiateHandshake مع تمرير peerID. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:349]

```
350:     }
```
> إغلاق نطاق الدالة initiateRekey. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:350]

```
351:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:351]

```
352:     // MARK: - Private Helpers
```
> تعليق: علامة قسم «مساعِدات خاصة (Private Helpers)». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:352]

```
353:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:353]

```
354:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:354]

```
355:      * Generate a new Curve25519 key pair using the real Noise library
```
> تعليق: «ولّد زوج مفاتيح Curve25519 جديداً باستخدام مكتبة Noise الحقيقية». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:355]

```
356:      * Returns (privateKey, publicKey) as 32-byte arrays
```
> تعليق: «يُعيد (المفتاح الخاص، المفتاح العام) كمصفوفتي بايتات بطول ٣٢ بايت». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:356]

```
357:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:357]

```
358:     private fun generateKeyPair(): Pair<ByteArray, ByteArray> {
```
> تعريف دالة خاصة (generateKeyPair) لا تأخذ معاملات وتُعيد زوجاً (Pair) من مصفوفتي بايتات. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:358]

```
359:         try {
```
> تبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:359]

```
360:             val dhState = com.bitchat.android.noise.southernstorm.protocol.Noise.createDH("25519")
```
> تُعرّف متغيّراً ثابتاً (dhState) بنتيجة استدعاء Noise.createDH من حزمة southernstorm.protocol مع تمرير النص الحرفي «25519». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:360]

```
361:             dhState.generateKeyPair()
```
> تستدعي الدالة generateKeyPair على حالة ديفي-هيلمان (dhState). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:361]

```
362:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:362]

```
363:             val privateKey = ByteArray(32)
```
> تُعرّف متغيّراً ثابتاً (privateKey) كمصفوفة بايتات بطول ٣٢. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:363]

```
364:             val publicKey = ByteArray(32)
```
> تُعرّف متغيّراً ثابتاً (publicKey) كمصفوفة بايتات بطول ٣٢. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:364]

```
365:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:365]

```
366:             dhState.getPrivateKey(privateKey, 0)
```
> تستدعي الدالة getPrivateKey على dhState مع تمرير المصفوفة privateKey والإزاحة ٠. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:366]

```
367:             dhState.getPublicKey(publicKey, 0)
```
> تستدعي الدالة getPublicKey على dhState مع تمرير المصفوفة publicKey والإزاحة ٠. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:367]

```
368:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:368]

```
369:             dhState.destroy()
```
> تستدعي الدالة destroy على dhState لإتلاف الحالة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:369]

```
370:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:370]

```
371:             return Pair(privateKey, publicKey)
```
> تُعيد زوجاً (Pair) يحوي privateKey وpublicKey. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:371]

```
372:         } catch (e: Exception) {
```
> تلتقط أي استثناء في المتغيّر e. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:372]

```
373:             Log.e(TAG, "Failed to generate key pair: ${e.message}")
```
> تسجّل خطأً عبر Log.e بالوسم ونصّ «Failed to generate key pair: ${e.message}» مع إدراج رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:373]

```
374:             throw e
```
> تعيد رمي الاستثناء e. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:374]

```
375:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:375]

```
376:     }
```
> إغلاق نطاق الدالة generateKeyPair. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:376]

```
377:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:377]

```
378:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:378]

```
379:      * Handle session establishment (called when Noise handshake completes)
```
> تعليق: «عالِج تأسيس الجلسة — يُستدعى عند اكتمال مصافحة Noise». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:379]

```
380:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:380]

```
381:     private fun handleSessionEstablished(peerID: String, remoteStaticKey: ByteArray) {
```
> تعريف دالة خاصة (handleSessionEstablished) تأخذ peerID نصاً والمفتاح الساكن البعيد (remoteStaticKey) مصفوفة بايتات ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:381]

```
382:         // Store fingerprint mapping via centralized manager
```
> تعليق: «خزّن ربط البصمة عبر المدير المركزي». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:382]

```
383:         // This is the ONLY place where fingerprints are stored - after successful Noise handshake
```
> تعليق: «هذا هو المكان الوحيد الذي تُخزّن فيه البصمات — بعد نجاح مصافحة Noise». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:383]

```
384:         fingerprintManager.storeFingerprintForPeer(peerID, remoteStaticKey)
```
> تستدعي الدالة storeFingerprintForPeer على مدير البصمات مع تمرير peerID وremoteStaticKey. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:384]

```
385:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:385]

```
386:         // Calculate fingerprint for logging and callback
```
> تعليق: «احسب البصمة للتسجيل ونداء الاستدعاء العكسي (callback)». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:386]

```
387:         val fingerprint = calculateFingerprint(remoteStaticKey)
```
> تُعرّف متغيّراً ثابتاً (fingerprint) بنتيجة استدعاء calculateFingerprint مع تمرير remoteStaticKey. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:387]

```
388:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:388]

```
389:         Log.d(TAG, "Session established with $peerID, fingerprint: ${fingerprint.take(16)}...")
```
> تسجّل رسالة تصحيح عبر Log.d بالوسم ونصّ «Session established with $peerID, fingerprint: ${fingerprint.take(16)}...» مع إدراج peerID وأول ١٦ محرفاً من البصمة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:389]

```
390:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:390]

```
391:         // Notify about authentication
```
> تعليق: «أبلِغ عن المصادقة (authentication)». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:391]

```
392:         onPeerAuthenticated?.invoke(peerID, fingerprint)
```
> تستدعي بأمان الاستدعاء العكسي onPeerAuthenticated عبر invoke مع تمرير peerID وfingerprint إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:392]

```
393:     }
```
> إغلاق نطاق الدالة handleSessionEstablished. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:393]

```
394:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:394]

```
395:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:395]

```
396:      * Calculate fingerprint from public key (SHA-256 hash)
```
> تعليق: «احسب البصمة من المفتاح العام — تجزئة SHA-256». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:396]

```
397:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:397]

```
398:     private fun calculateFingerprint(publicKey: ByteArray): String {
```
> تعريف دالة خاصة (calculateFingerprint) تأخذ المفتاح العام (publicKey) مصفوفة بايتات وتُعيد نصاً. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:398]

```
399:         val digest = MessageDigest.getInstance("SHA-256")
```
> تُعرّف متغيّراً ثابتاً (digest) بنتيجة استدعاء MessageDigest.getInstance مع تمرير النص الحرفي «SHA-256». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:399]

```
400:         val hash = digest.digest(publicKey)
```
> تُعرّف متغيّراً ثابتاً (hash) بنتيجة استدعاء الدالة digest على digest مع تمرير publicKey. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:400]

```
401:         return hash.joinToString("") { "%02x".format(it) }
```
> تُعيد سلسلة نصية ناتجة عن دمج بايتات hash بفاصل فارغ، مع تنسيق كل بايت كرقم سداسي عشري من خانتين عبر «%02x». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:401]

```
402:     }
```
> إغلاق نطاق الدالة calculateFingerprint. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:402]

```
403:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:403]

```
404:     // MARK: - Packet Signing/Verification
```
> تعليق: علامة قسم «توقيع/تحقّق الرزمة (Packet Signing/Verification)». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:404]

```
405:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:405]

```
406:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:406]

```
407:      * Sign a BitchatPacket using our Ed25519 signing key
```
> تعليق: «وقّع رزمة BitchatPacket باستخدام مفتاح التوقيع Ed25519 الخاص بنا». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:407]

```
408:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:408]

```
409:     fun signPacket(packet: com.bitchat.android.protocol.BitchatPacket): com.bitchat.android.protocol.BitchatPacket? {
```
> تعريف دالة عامة (signPacket) تأخذ رزمة (packet) من نوع BitchatPacket وتُعيد BitchatPacket قابلاً للقيمة الفارغة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:409]

```
410:         // Create canonical packet bytes for signing
```
> تعليق: «أنشئ بايتات الرزمة القياسية (canonical) للتوقيع». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:410]

```
411:         val packetData = packet.toBinaryDataForSigning() ?: return null
```
> تُعرّف متغيّراً ثابتاً (packetData) بنتيجة packet.toBinaryDataForSigning، وتُعيد null إن كانت النتيجة فارغة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:411]

```
412:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:412]

```
413:         // Sign with our Ed25519 signing private key
```
> تعليق: «وقّع بمفتاح التوقيع الخاص Ed25519 الخاص بنا». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:413]

```
414:         val signature = signData(packetData) ?: return null
```
> تُعرّف متغيّراً ثابتاً (signature) بنتيجة signData مع تمرير packetData، وتُعيد null إن كانت النتيجة فارغة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:414]

```
415:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:415]

```
416:         // Return new packet with signature
```
> تعليق: «أعِد رزمة جديدة تحمل التوقيع». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:416]

```
417:         return packet.copy(signature = signature)
```
> تُعيد نسخة من packet عبر copy مع ضبط الحقل signature بالقيمة signature. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:417]

```
418:     }
```
> إغلاق نطاق الدالة signPacket. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:418]

```
419:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:419]

```
420:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:420]

```
421:      * Verify a BitchatPacket signature using the provided public key
```
> تعليق: «تحقّق من توقيع رزمة BitchatPacket باستخدام المفتاح العام المُمرَّر». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:421]

```
422:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:422]

```
423:     fun verifyPacketSignature(packet: com.bitchat.android.protocol.BitchatPacket, publicKey: ByteArray): Boolean {
```
> تعريف دالة عامة (verifyPacketSignature) تأخذ packet من نوع BitchatPacket وpublicKey مصفوفة بايتات وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:423]

```
424:         val signature = packet.signature ?: return false
```
> تُعرّف متغيّراً ثابتاً (signature) بحقل packet.signature، وتُعيد false إن كان فارغاً. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:424]

```
425:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:425]

```
426:         // Create canonical packet bytes for verification (without signature)
```
> تعليق: «أنشئ بايتات الرزمة القياسية للتحقّق — بدون التوقيع». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:426]

```
427:         val packetData = packet.toBinaryDataForSigning() ?: return false
```
> تُعرّف متغيّراً ثابتاً (packetData) بنتيجة packet.toBinaryDataForSigning، وتُعيد false إن كانت النتيجة فارغة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:427]

```
428:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:428]

```
429:         // Verify signature using the provided Ed25519 public key
```
> تعليق: «تحقّق من التوقيع باستخدام مفتاح Ed25519 العام المُمرَّر». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:429]

```
430:         return verifySignature(signature, packetData, publicKey)
```
> تُعيد نتيجة استدعاء verifySignature مع تمرير signature وpacketData وpublicKey. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:430]

```
431:     }
```
> إغلاق نطاق الدالة verifyPacketSignature. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:431]

```
432:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:432]

```
433:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:433]

```
434:      * Sign data with our Ed25519 signing key
```
> تعليق: «وقّع البيانات بمفتاح التوقيع Ed25519 الخاص بنا». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:434]

```
435:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:435]

```
436:     fun signData(data: ByteArray): ByteArray? {
```
> تعريف دالة عامة (signData) تأخذ البيانات (data) مصفوفة بايتات وتُعيد مصفوفة بايتات قابلة للقيمة الفارغة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:436]

```
437:         return try {
```
> تبدأ بإرجاع نتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:437]

```
438:             // For simplicity, we'll implement this using BouncyCastle which should be available
```
> تعليق: «للتبسيط، سننفّذ هذا باستخدام BouncyCastle التي يُفترض أن تكون متاحة». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:438]

```
439:             // In a production system, you might want to use the Android Keystore
```
> تعليق: «في نظام إنتاجي، قد ترغب باستخدام مخزن مفاتيح أندرويد (Android Keystore)». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:439]

```
440:             signWithEd25519(data, signingPrivateKey)
```
> تستدعي signWithEd25519 مع تمرير data ومفتاح التوقيع الخاص (signingPrivateKey) كقيمة الكتلة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:440]

```
441:         } catch (e: Exception) {
```
> تلتقط أي استثناء في المتغيّر e. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:441]

```
442:             Log.e(TAG, "Failed to sign data: ${e.message}")
```
> تسجّل خطأً عبر Log.e بالوسم ونصّ «Failed to sign data: ${e.message}» مع إدراج رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:442]

```
443:             null
```
> تُعيد القيمة الفارغة (null) كنتيجة لكتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:443]

```
444:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:444]

```
445:     }
```
> إغلاق نطاق الدالة signData. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:445]

```
446:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:446]

```
447:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:447]

```
448:      * Verify signature with a public key
```
> تعليق: «تحقّق من التوقيع بمفتاح عام». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:448]

```
449:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:449]

```
450:     fun verifySignature(signature: ByteArray, data: ByteArray, publicKey: ByteArray): Boolean {
```
> تعريف دالة عامة (verifySignature) تأخذ التوقيع (signature) والبيانات (data) والمفتاح العام (publicKey) كمصفوفات بايتات وتُعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:450]

```
451:         return try {
```
> تبدأ بإرجاع نتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:451]

```
452:             verifyWithEd25519(signature, data, publicKey)
```
> تستدعي verifyWithEd25519 مع تمرير signature وdata وpublicKey كقيمة الكتلة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:452]

```
453:         } catch (e: Exception) {
```
> تلتقط أي استثناء في المتغيّر e. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:453]

```
454:             Log.e(TAG, "Failed to verify signature: ${e.message}")
```
> تسجّل خطأً عبر Log.e بالوسم ونصّ «Failed to verify signature: ${e.message}» مع إدراج رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:454]

```
455:             false
```
> تُعيد القيمة المنطقية false كنتيجة لكتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:455]

```
456:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:456]

```
457:     }
```
> إغلاق نطاق الدالة verifySignature. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:457]

```
458:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:458]

```
459:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:459]

```
460:      * Generate a new Ed25519 key pair for signing using BouncyCastle
```
> تعليق: «ولّد زوج مفاتيح Ed25519 جديداً للتوقيع باستخدام BouncyCastle». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:460]

```
461:      * Returns (privateKey, publicKey) as 32-byte arrays
```
> تعليق: «يُعيد (المفتاح الخاص، المفتاح العام) كمصفوفتي بايتات بطول ٣٢ بايت». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:461]

```
462:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:462]

```
463:     private fun generateEd25519KeyPair(): Pair<ByteArray, ByteArray> {
```
> تعريف دالة خاصة (generateEd25519KeyPair) لا تأخذ معاملات وتُعيد زوجاً من مصفوفتي بايتات. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:463]

```
464:         try {
```
> تبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:464]

```
465:             // Use BouncyCastle for proper Ed25519 key generation
```
> تعليق: «استخدم BouncyCastle لتوليد مفاتيح Ed25519 سليم». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:465]

```
466:             val keyGen = org.bouncycastle.crypto.generators.Ed25519KeyPairGenerator()
```
> تُعرّف متغيّراً ثابتاً (keyGen) بكائن Ed25519KeyPairGenerator من حزمة bouncycastle.crypto.generators. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:466]

```
467:             keyGen.init(org.bouncycastle.crypto.params.Ed25519KeyGenerationParameters(SecureRandom()))
```
> تستدعي init على keyGen مع تمرير Ed25519KeyGenerationParameters المبنيّة بمولّد عشوائي آمن (SecureRandom). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:467]

```
468:             val keyPair = keyGen.generateKeyPair()
```
> تُعرّف متغيّراً ثابتاً (keyPair) بنتيجة استدعاء generateKeyPair على keyGen. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:468]

```
469:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:469]

```
470:             val privateKey = (keyPair.private as org.bouncycastle.crypto.params.Ed25519PrivateKeyParameters).encoded
```
> تُعرّف متغيّراً ثابتاً (privateKey) بقيمة الحقل encoded بعد تحويل keyPair.private إلى نوع Ed25519PrivateKeyParameters. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:470]

```
471:             val publicKey = (keyPair.public as org.bouncycastle.crypto.params.Ed25519PublicKeyParameters).encoded
```
> تُعرّف متغيّراً ثابتاً (publicKey) بقيمة الحقل encoded بعد تحويل keyPair.public إلى نوع Ed25519PublicKeyParameters. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:471]

```
472:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:472]

```
473:             return Pair(privateKey, publicKey)
```
> تُعيد زوجاً (Pair) يحوي privateKey وpublicKey. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:473]

```
474:         } catch (e: Exception) {
```
> تلتقط أي استثناء في المتغيّر e. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:474]

```
475:             Log.e(TAG, "Failed to generate Ed25519 key pair: ${e.message}")
```
> تسجّل خطأً عبر Log.e بالوسم ونصّ «Failed to generate Ed25519 key pair: ${e.message}» مع إدراج رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:475]

```
476:             throw e
```
> تعيد رمي الاستثناء e. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:476]

```
477:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:477]

```
478:     }
```
> إغلاق نطاق الدالة generateEd25519KeyPair. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:478]

```
479:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:479]

```
480:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:480]

```
481:      * Sign data with Ed25519 private key using BouncyCastle
```
> تعليق: «وقّع البيانات بمفتاح Ed25519 الخاص باستخدام BouncyCastle». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:481]

```
482:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:482]

```
483:     private fun signWithEd25519(data: ByteArray, privateKey: ByteArray): ByteArray {
```
> تعريف دالة خاصة (signWithEd25519) تأخذ data وprivateKey كمصفوفتي بايتات وتُعيد مصفوفة بايتات. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:483]

```
484:         try {
```
> تبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:484]

```
485:             val privateKeyParams = org.bouncycastle.crypto.params.Ed25519PrivateKeyParameters(privateKey, 0)
```
> تُعرّف متغيّراً ثابتاً (privateKeyParams) بكائن Ed25519PrivateKeyParameters المبنيّ من privateKey والإزاحة ٠. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:485]

```
486:             val signer = org.bouncycastle.crypto.signers.Ed25519Signer()
```
> تُعرّف متغيّراً ثابتاً (signer) بكائن Ed25519Signer من حزمة bouncycastle.crypto.signers. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:486]

```
487:             signer.init(true, privateKeyParams)
```
> تستدعي init على signer مع تمرير القيمة المنطقية true ووسائط المفتاح الخاص privateKeyParams. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:487]

```
488:             signer.update(data, 0, data.size)
```
> تستدعي update على signer مع تمرير data والإزاحة ٠ وطول data.size. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:488]

```
489:             return signer.generateSignature()
```
> تُعيد نتيجة استدعاء generateSignature على signer. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:489]

```
490:         } catch (e: Exception) {
```
> تلتقط أي استثناء في المتغيّر e. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:490]

```
491:             Log.e(TAG, "Failed to sign data with Ed25519: ${e.message}")
```
> تسجّل خطأً عبر Log.e بالوسم ونصّ «Failed to sign data with Ed25519: ${e.message}» مع إدراج رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:491]

```
492:             throw e
```
> تعيد رمي الاستثناء e. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:492]

```
493:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:493]

```
494:     }
```
> إغلاق نطاق الدالة signWithEd25519. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:494]

```
495:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:495]

```
496:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:496]

```
497:      * Verify Ed25519 signature using BouncyCastle
```
> تعليق: «تحقّق من توقيع Ed25519 باستخدام BouncyCastle». [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:497]

```
498:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:498]

```
499:     private fun verifyWithEd25519(signature: ByteArray, data: ByteArray, publicKey: ByteArray): Boolean {
```
> تعريف دالة خاصة (verifyWithEd25519) تأخذ signature وdata وpublicKey كمصفوفات بايتات وتُعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:499]

```
500:         try {
```
> تبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:500]
