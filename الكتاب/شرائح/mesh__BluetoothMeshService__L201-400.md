# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt (الأسطر 201–400)

```
201:                 delegate?.didUpdatePeerList(peerIDs)
```
> يستدعي الدالة `didUpdatePeerList` على المفوَّض (delegate) إن لم يكن فارغاً، ويمرّر لها قائمة معرّفات الأقران (peerIDs). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:201]

```
202:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:202]

```
203:             override fun onPeerRemoved(peerID: String) {
```
> يعرّف بإعادة تعريف (override) دالةً اسمها `onPeerRemoved` تأخذ مُعامِلاً نصّياً اسمه `peerID` من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:203]

```
204:                 try { gossipSyncManager.removeAnnouncementForPeer(peerID) } catch (_: Exception) { }
```
> داخل كتلة `try` يستدعي `removeAnnouncementForPeer` على مدير مزامنة الإشاعة (gossipSyncManager) ممرّراً `peerID`، ويلتقط أيّ استثناء (Exception) بكتلة `catch` فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:204]

```
205:                 // Remove from mesh graph topology to prevent routing through stale peers
```
> تعليق: إزالة من طوبولوجيا رسم الشبكة المتشابكة لمنع التوجيه عبر أقران قديمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:205]

```
206:                 try { com.bitchat.android.services.meshgraph.MeshGraphService.getInstance().removePeer(peerID) } catch (_: Exception) { }
```
> داخل كتلة `try` يحصل على النسخة الوحيدة من خدمة رسم الشبكة (MeshGraphService) عبر `getInstance` ثم يستدعي `removePeer` ممرّراً `peerID`، ويلتقط أيّ استثناء بكتلة `catch` فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:206]

```
207: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:207]

```
208:                 // Also drop any Noise session state for this peer when they go offline
```
> تعليق: أيضاً أسقِط أيّ حالة جلسة نويز (Noise) لهذا القرين عندما يصير غير متّصل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:208]

```
209:                 try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:209]

```
210:                     encryptionService.removePeer(peerID)
```
> يستدعي `removePeer` على خدمة التشفير (encryptionService) ممرّراً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:210]

```
211:                     Log.d(TAG, "Removed Noise session for offline peer $peerID")
```
> يسجّل رسالة تنقيح (Log.d) بوسم `TAG` ونصّها «Removed Noise session for offline peer» متبوعاً بقيمة `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:211]

```
212:                 } catch (e: Exception) {
```
> يغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً اسمه `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:212]

```
213:                     Log.w(TAG, "Failed to remove Noise session for $peerID: ${e.message}")
```
> يسجّل رسالة تحذير (Log.w) بوسم `TAG` ونصّها «Failed to remove Noise session for» متبوعاً بقيمة `peerID` ثم رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:213]

```
214:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:214]

```
215:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:215]

```
216:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:216]

```
217:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:217]

```
218:         // SecurityManager delegate for key exchange notifications
```
> تعليق: مفوَّض مدير الأمن (SecurityManager) لإشعارات تبادل المفاتيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:218]

```
219:         securityManager.delegate = object : SecurityManagerDelegate {
```
> يُسنِد إلى الخاصية `delegate` في مدير الأمن (securityManager) كائناً مجهولاً (object) يحقّق الواجهة `SecurityManagerDelegate`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:219]

```
220:             override fun onKeyExchangeCompleted(peerID: String, peerPublicKeyData: ByteArray) {
```
> يعرّف بإعادة تعريف دالةً اسمها `onKeyExchangeCompleted` تأخذ مُعامِلاً نصّياً `peerID` ومُعامِلاً `peerPublicKeyData` من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:220]

```
221:                 // Send announcement and cached messages after key exchange
```
> تعليق: أرسل الإعلان والرسائل المخزّنة بعد تبادل المفاتيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:221]

```
222:                 serviceScope.launch {
```
> يطلق (launch) كوروتين (coroutine) ضمن نطاق الخدمة (serviceScope). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:222]

```
223:                     Log.d(TAG, "Key exchange completed with $peerID; sending follow-ups")
```
> يسجّل رسالة تنقيح بوسم `TAG` ونصّها «Key exchange completed with» متبوعاً بقيمة `peerID` ثم «; sending follow-ups». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:223]

```
224:                     delay(100)
```
> يستدعي `delay` بقيمة 100 (تأخير زمني بالمللي ثانية). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:224]

```
225:                     sendAnnouncementToPeer(peerID)
```
> يستدعي الدالة `sendAnnouncementToPeer` ممرّراً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:225]

```
226:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:226]

```
227:                     delay(1000)
```
> يستدعي `delay` بقيمة 1000 (تأخير زمني بالمللي ثانية). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:227]

```
228:                     storeForwardManager.sendCachedMessages(peerID)
```
> يستدعي `sendCachedMessages` على مدير التخزين والإرسال (storeForwardManager) ممرّراً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:228]

```
229:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:229]

```
230:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:230]

```
231:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:231]

```
232:             override fun sendHandshakeResponse(peerID: String, response: ByteArray) {
```
> يعرّف بإعادة تعريف دالةً اسمها `sendHandshakeResponse` تأخذ مُعامِلاً نصّياً `peerID` ومُعامِلاً `response` من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:232]

```
233:                 // Send Noise handshake response
```
> تعليق: أرسل ردّ مصافحة نويز (Noise handshake response). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:233]

```
234:                 val responsePacket = BitchatPacket(
```
> يعرّف ثابتاً اسمه `responsePacket` ويُسنِد إليه كائن حزمة بِت-تشات (BitchatPacket) عبر مُنشئ متعدّد الوسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:234]

```
235:                     version = 1u,
```
> يضبط الوسيط `version` على القيمة `1u` (عدد صحيح غير مُوقَّع). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:235]

```
236:                     type = MessageType.NOISE_HANDSHAKE.value,
```
> يضبط الوسيط `type` على القيمة `value` للعنصر `NOISE_HANDSHAKE` من التعداد `MessageType`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:236]

```
237:                     senderID = hexStringToByteArray(myPeerID),
```
> يضبط الوسيط `senderID` على ناتج تحويل `myPeerID` إلى مصفوفة بايتات عبر `hexStringToByteArray`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:237]

```
238:                     recipientID = hexStringToByteArray(peerID),
```
> يضبط الوسيط `recipientID` على ناتج تحويل `peerID` إلى مصفوفة بايتات عبر `hexStringToByteArray`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:238]

```
239:                     timestamp = System.currentTimeMillis().toULong(),
```
> يضبط الوسيط `timestamp` على الوقت الحالي بالمللي ثانية من `System.currentTimeMillis` محوَّلاً إلى عدد طويل غير مُوقَّع بـ `toULong`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:239]

```
240:                     payload = response,
```
> يضبط الوسيط `payload` على قيمة المُعامِل `response`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:240]

```
241:                     ttl = MAX_TTL
```
> يضبط الوسيط `ttl` (مدّة البقاء) على الثابت `MAX_TTL`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:241]

```
242:                 )
```
> إغلاق قائمة وسائط المُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:242]

```
243:                 // Sign the handshake response
```
> تعليق: وقِّع ردّ المصافحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:243]

```
244:                 val signedPacket = signPacketBeforeBroadcast(responsePacket)
```
> يعرّف ثابتاً اسمه `signedPacket` ويُسنِد إليه ناتج استدعاء `signPacketBeforeBroadcast` ممرّراً `responsePacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:244]

```
245:                 broadcastRoutedPacket(RoutedPacket(signedPacket))
```
> يستدعي `broadcastRoutedPacket` ممرّراً كائن حزمة مُوجَّهة (RoutedPacket) مُنشأً من `signedPacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:245]

```
246:                 Log.d(TAG, "Sent Noise handshake response to $peerID (${response.size} bytes)")
```
> يسجّل رسالة تنقيح بوسم `TAG` ونصّها «Sent Noise handshake response to» متبوعاً بقيمة `peerID` وحجم `response.size` متبوعاً بكلمة «bytes». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:246]

```
247:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:247]

```
248:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:248]

```
249:             override fun getPeerInfo(peerID: String): PeerInfo? {
```
> يعرّف بإعادة تعريف دالةً اسمها `getPeerInfo` تأخذ مُعامِلاً نصّياً `peerID` وتُعيد قيمةً من نوع `PeerInfo` قابلاً للعدم (nullable). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:249]

```
250:                 return peerManager.getPeerInfo(peerID)
```
> يُعيد ناتج استدعاء `getPeerInfo` على مدير الأقران (peerManager) ممرّراً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:250]

```
251:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:251]

```
252:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:252]

```
253:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:253]

```
254:         // StoreForwardManager delegates
```
> تعليق: مفوَّضات مدير التخزين والإرسال (StoreForwardManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:254]

```
255:         storeForwardManager.delegate = object : StoreForwardManagerDelegate {
```
> يُسنِد إلى الخاصية `delegate` في مدير التخزين والإرسال (storeForwardManager) كائناً مجهولاً يحقّق الواجهة `StoreForwardManagerDelegate`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:255]

```
256:             override fun isFavorite(peerID: String): Boolean {
```
> يعرّف بإعادة تعريف دالةً اسمها `isFavorite` تأخذ مُعامِلاً نصّياً `peerID` وتُعيد قيمةً منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:256]

```
257:                 return delegate?.isFavorite(peerID) ?: false
```
> يُعيد ناتج استدعاء `isFavorite` على المفوَّض إن لم يكن فارغاً ممرّراً `peerID`، وإلّا يُعيد `false` عبر عامل الإيلْفِس (Elvis). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:257]

```
258:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:258]

```
259:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:259]

```
260:             override fun isPeerOnline(peerID: String): Boolean {
```
> يعرّف بإعادة تعريف دالةً اسمها `isPeerOnline` تأخذ مُعامِلاً نصّياً `peerID` وتُعيد قيمةً منطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:260]

```
261:                 return peerManager.isPeerActive(peerID)
```
> يُعيد ناتج استدعاء `isPeerActive` على مدير الأقران ممرّراً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:261]

```
262:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:262]

```
263:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:263]

```
264:             override fun sendPacket(packet: BitchatPacket) {
```
> يعرّف بإعادة تعريف دالةً اسمها `sendPacket` تأخذ مُعامِلاً اسمه `packet` من نوع `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:264]

```
265:                 broadcastRoutedPacket(RoutedPacket(packet))
```
> يستدعي `broadcastRoutedPacket` ممرّراً كائن `RoutedPacket` مُنشأً من `packet`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:265]

```
266:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:266]

```
267:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:267]

```
268:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:268]

```
269:         // MessageHandler delegates
```
> تعليق: مفوَّضات معالِج الرسائل (MessageHandler). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:269]

```
270:         messageHandler.delegate = object : MessageHandlerDelegate {
```
> يُسنِد إلى الخاصية `delegate` في معالِج الرسائل (messageHandler) كائناً مجهولاً يحقّق الواجهة `MessageHandlerDelegate`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:270]

```
271:             // Peer management
```
> تعليق: إدارة الأقران. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:271]

```
272:             override fun addOrUpdatePeer(peerID: String, nickname: String): Boolean {
```
> يعرّف بإعادة تعريف دالةً اسمها `addOrUpdatePeer` تأخذ مُعامِلاً نصّياً `peerID` ومُعامِلاً نصّياً `nickname` وتُعيد قيمةً منطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:272]

```
273:                 return peerManager.addOrUpdatePeer(peerID, nickname)
```
> يُعيد ناتج استدعاء `addOrUpdatePeer` على مدير الأقران ممرّراً `peerID` و`nickname`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:273]

```
274:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:274]

```
275:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:275]

```
276:             override fun removePeer(peerID: String) {
```
> يعرّف بإعادة تعريف دالةً اسمها `removePeer` تأخذ مُعامِلاً نصّياً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:276]

```
277:                 peerManager.removePeer(peerID)
```
> يستدعي `removePeer` على مدير الأقران ممرّراً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:277]

```
278:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:278]

```
279:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:279]

```
280:             override fun updatePeerNickname(peerID: String, nickname: String) {
```
> يعرّف بإعادة تعريف دالةً اسمها `updatePeerNickname` تأخذ مُعامِلاً نصّياً `peerID` ومُعامِلاً نصّياً `nickname`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:280]

```
281:                 peerManager.addOrUpdatePeer(peerID, nickname)
```
> يستدعي `addOrUpdatePeer` على مدير الأقران ممرّراً `peerID` و`nickname`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:281]

```
282:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:282]

```
283:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:283]

```
284:             override fun getPeerNickname(peerID: String): String? {
```
> يعرّف بإعادة تعريف دالةً اسمها `getPeerNickname` تأخذ مُعامِلاً نصّياً `peerID` وتُعيد نصّاً قابلاً للعدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:284]

```
285:                 return peerManager.getPeerNickname(peerID)
```
> يُعيد ناتج استدعاء `getPeerNickname` على مدير الأقران ممرّراً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:285]

```
286:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:286]

```
287:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:287]

```
288:             override fun getNetworkSize(): Int {
```
> يعرّف بإعادة تعريف دالةً اسمها `getNetworkSize` بلا مُعامِلات وتُعيد عدداً صحيحاً (Int). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:288]

```
289:                 return peerManager.getActivePeerCount()
```
> يُعيد ناتج استدعاء `getActivePeerCount` على مدير الأقران. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:289]

```
290:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:290]

```
291:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:291]

```
292:             override fun getMyNickname(): String? {
```
> يعرّف بإعادة تعريف دالةً اسمها `getMyNickname` بلا مُعامِلات وتُعيد نصّاً قابلاً للعدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:292]

```
293:                 return delegate?.getNickname()
```
> يُعيد ناتج استدعاء `getNickname` على المفوَّض إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:293]

```
294:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:294]

```
295:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:295]

```
296:             override fun getPeerInfo(peerID: String): PeerInfo? {
```
> يعرّف بإعادة تعريف دالةً اسمها `getPeerInfo` تأخذ مُعامِلاً نصّياً `peerID` وتُعيد قيمةً من نوع `PeerInfo` قابلاً للعدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:296]

```
297:                 return peerManager.getPeerInfo(peerID)
```
> يُعيد ناتج استدعاء `getPeerInfo` على مدير الأقران ممرّراً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:297]

```
298:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:298]

```
299:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:299]

```
300:             override fun updatePeerInfo(peerID: String, nickname: String, noisePublicKey: ByteArray, signingPublicKey: ByteArray, isVerified: Boolean): Boolean {
```
> يعرّف بإعادة تعريف دالةً اسمها `updatePeerInfo` تأخذ `peerID` نصّياً و`nickname` نصّياً و`noisePublicKey` من نوع `ByteArray` و`signingPublicKey` من نوع `ByteArray` و`isVerified` منطقياً، وتُعيد قيمةً منطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:300]

```
301:                 return peerManager.updatePeerInfo(peerID, nickname, noisePublicKey, signingPublicKey, isVerified)
```
> يُعيد ناتج استدعاء `updatePeerInfo` على مدير الأقران ممرّراً `peerID` و`nickname` و`noisePublicKey` و`signingPublicKey` و`isVerified`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:301]

```
302:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:302]

```
303:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:303]

```
304:             // Packet operations
```
> تعليق: عمليات الحزمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:304]

```
305:             override fun sendPacket(packet: BitchatPacket) {
```
> يعرّف بإعادة تعريف دالةً اسمها `sendPacket` تأخذ مُعامِلاً اسمه `packet` من نوع `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:305]

```
306:                 // Sign the packet before broadcasting
```
> تعليق: وقِّع الحزمة قبل البثّ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:306]

```
307:                 val signedPacket = signPacketBeforeBroadcast(packet)
```
> يعرّف ثابتاً اسمه `signedPacket` ويُسنِد إليه ناتج استدعاء `signPacketBeforeBroadcast` ممرّراً `packet`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:307]

```
308:                 broadcastRoutedPacket(RoutedPacket(signedPacket))
```
> يستدعي `broadcastRoutedPacket` ممرّراً كائن `RoutedPacket` مُنشأً من `signedPacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:308]

```
309:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:309]

```
310:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:310]

```
311:             override fun relayPacket(routed: RoutedPacket) {
```
> يعرّف بإعادة تعريف دالةً اسمها `relayPacket` تأخذ مُعامِلاً اسمه `routed` من نوع `RoutedPacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:311]

```
312:                 broadcastRoutedPacket(routed)
```
> يستدعي `broadcastRoutedPacket` ممرّراً `routed`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:312]

```
313:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:313]

```
314:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:314]

```
315:             override fun getBroadcastRecipient(): ByteArray {
```
> يعرّف بإعادة تعريف دالةً اسمها `getBroadcastRecipient` بلا مُعامِلات وتُعيد قيمةً من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:315]

```
316:                 return SpecialRecipients.BROADCAST
```
> يُعيد الثابت `BROADCAST` من الكائن `SpecialRecipients`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:316]

```
317:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:317]

```
318:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:318]

```
319:             // Cryptographic operations
```
> تعليق: العمليات التشفيرية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:319]

```
320:             override fun verifySignature(packet: BitchatPacket, peerID: String): Boolean {
```
> يعرّف بإعادة تعريف دالةً اسمها `verifySignature` تأخذ مُعامِلاً `packet` من نوع `BitchatPacket` ومُعامِلاً نصّياً `peerID` وتُعيد قيمةً منطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:320]

```
321:                 return securityManager.verifySignature(packet, peerID)
```
> يُعيد ناتج استدعاء `verifySignature` على مدير الأمن ممرّراً `packet` و`peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:321]

```
322:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:322]

```
323:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:323]

```
324:             override fun encryptForPeer(data: ByteArray, recipientPeerID: String): ByteArray? {
```
> يعرّف بإعادة تعريف دالةً اسمها `encryptForPeer` تأخذ مُعامِلاً `data` من نوع `ByteArray` ومُعامِلاً نصّياً `recipientPeerID` وتُعيد `ByteArray` قابلاً للعدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:324]

```
325:                 return securityManager.encryptForPeer(data, recipientPeerID)
```
> يُعيد ناتج استدعاء `encryptForPeer` على مدير الأمن ممرّراً `data` و`recipientPeerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:325]

```
326:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:326]

```
327:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:327]

```
328:             override fun decryptFromPeer(encryptedData: ByteArray, senderPeerID: String): ByteArray? {
```
> يعرّف بإعادة تعريف دالةً اسمها `decryptFromPeer` تأخذ مُعامِلاً `encryptedData` من نوع `ByteArray` ومُعامِلاً نصّياً `senderPeerID` وتُعيد `ByteArray` قابلاً للعدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:328]

```
329:                 return securityManager.decryptFromPeer(encryptedData, senderPeerID)
```
> يُعيد ناتج استدعاء `decryptFromPeer` على مدير الأمن ممرّراً `encryptedData` و`senderPeerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:329]

```
330:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:330]

```
331:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:331]

```
332:             override fun verifyEd25519Signature(signature: ByteArray, data: ByteArray, publicKey: ByteArray): Boolean {
```
> يعرّف بإعادة تعريف دالةً اسمها `verifyEd25519Signature` تأخذ `signature` و`data` و`publicKey` كلَّها من نوع `ByteArray` وتُعيد قيمةً منطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:332]

```
333:                 return encryptionService.verifyEd25519Signature(signature, data, publicKey)
```
> يُعيد ناتج استدعاء `verifyEd25519Signature` على خدمة التشفير ممرّراً `signature` و`data` و`publicKey`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:333]

```
334:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:334]

```
335:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:335]

```
336:             // Noise protocol operations
```
> تعليق: عمليات بروتوكول نويز. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:336]

```
337:             override fun hasNoiseSession(peerID: String): Boolean {
```
> يعرّف بإعادة تعريف دالةً اسمها `hasNoiseSession` تأخذ مُعامِلاً نصّياً `peerID` وتُعيد قيمةً منطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:337]

```
338:                 return encryptionService.hasEstablishedSession(peerID)
```
> يُعيد ناتج استدعاء `hasEstablishedSession` على خدمة التشفير ممرّراً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:338]

```
339:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:339]

```
340:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:340]

```
341:             override fun initiateNoiseHandshake(peerID: String) {
```
> يعرّف بإعادة تعريف دالةً اسمها `initiateNoiseHandshake` تأخذ مُعامِلاً نصّياً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:341]

```
342:                 try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:342]

```
343:                     // Initiate proper Noise handshake with specific peer
```
> تعليق: ابدأ مصافحة نويز سليمة مع قرين محدّد. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:343]

```
344:                     val handshakeData = encryptionService.initiateHandshake(peerID)
```
> يعرّف ثابتاً اسمه `handshakeData` ويُسنِد إليه ناتج استدعاء `initiateHandshake` على خدمة التشفير ممرّراً `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:344]

```
345:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:345]

```
346:                     if (handshakeData != null) {
```
> شرط `if` يتحقّق إن كان `handshakeData` غير فارغ (لا يساوي `null`). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:346]

```
347:                         val packet = BitchatPacket(
```
> يعرّف ثابتاً اسمه `packet` ويُسنِد إليه كائن `BitchatPacket` عبر مُنشئ متعدّد الوسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:347]

```
348:                             version = 1u,
```
> يضبط الوسيط `version` على القيمة `1u`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:348]

```
349:                             type = MessageType.NOISE_HANDSHAKE.value,
```
> يضبط الوسيط `type` على القيمة `value` للعنصر `NOISE_HANDSHAKE` من التعداد `MessageType`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:349]

```
350:                             senderID = hexStringToByteArray(myPeerID),
```
> يضبط الوسيط `senderID` على ناتج تحويل `myPeerID` إلى مصفوفة بايتات عبر `hexStringToByteArray`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:350]

```
351:                             recipientID = hexStringToByteArray(peerID),
```
> يضبط الوسيط `recipientID` على ناتج تحويل `peerID` إلى مصفوفة بايتات عبر `hexStringToByteArray`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:351]

```
352:                             timestamp = System.currentTimeMillis().toULong(),
```
> يضبط الوسيط `timestamp` على الوقت الحالي بالمللي ثانية محوَّلاً بـ `toULong`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:352]

```
353:                             payload = handshakeData,
```
> يضبط الوسيط `payload` على قيمة `handshakeData`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:353]

```
354:                             ttl = MAX_TTL
```
> يضبط الوسيط `ttl` على الثابت `MAX_TTL`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:354]

```
355:                         )
```
> إغلاق قائمة وسائط المُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:355]

```
356:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:356]

```
357:                         // Sign the handshake packet before broadcasting
```
> تعليق: وقِّع حزمة المصافحة قبل البثّ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:357]

```
358:                         val signedPacket = signPacketBeforeBroadcast(packet)
```
> يعرّف ثابتاً اسمه `signedPacket` ويُسنِد إليه ناتج استدعاء `signPacketBeforeBroadcast` ممرّراً `packet`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:358]

```
359:                         broadcastRoutedPacket(RoutedPacket(signedPacket))
```
> يستدعي `broadcastRoutedPacket` ممرّراً كائن `RoutedPacket` مُنشأً من `signedPacket`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:359]

```
360:                         Log.d(TAG, "Initiated Noise handshake with $peerID (${handshakeData.size} bytes)")
```
> يسجّل رسالة تنقيح بوسم `TAG` ونصّها «Initiated Noise handshake with» متبوعاً بقيمة `peerID` وحجم `handshakeData.size` متبوعاً بكلمة «bytes». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:360]

```
361:                     } else {
```
> يغلق كتلة `if` ويبدأ كتلة `else`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:361]

```
362:                         Log.w(TAG, "Failed to generate Noise handshake data for $peerID")
```
> يسجّل رسالة تحذير بوسم `TAG` ونصّها «Failed to generate Noise handshake data for» متبوعاً بقيمة `peerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:362]

```
363:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:363]

```
364:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:364]

```
365:                 } catch (e: Exception) {
```
> يغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً اسمه `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:365]

```
366:                     Log.e(TAG, "Failed to initiate Noise handshake with $peerID: ${e.message}")
```
> يسجّل رسالة خطأ (Log.e) بوسم `TAG` ونصّها «Failed to initiate Noise handshake with» متبوعاً بقيمة `peerID` ثم رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:366]

```
367:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:367]

```
368:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:368]

```
369:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:369]

```
370:             override fun processNoiseHandshakeMessage(payload: ByteArray, peerID: String): ByteArray? {
```
> يعرّف بإعادة تعريف دالةً اسمها `processNoiseHandshakeMessage` تأخذ مُعامِلاً `payload` من نوع `ByteArray` ومُعامِلاً نصّياً `peerID` وتُعيد `ByteArray` قابلاً للعدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:370]

```
371:                 return try {
```
> يُعيد قيمة تعبير `try` الذي يبدأ في هذا السطر. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:371]

```
372:                     encryptionService.processHandshakeMessage(payload, peerID)
```
> يستدعي `processHandshakeMessage` على خدمة التشفير ممرّراً `payload` و`peerID` (وقيمته هي ناتج كتلة `try`). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:372]

```
373:                 } catch (e: Exception) {
```
> يغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً اسمه `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:373]

```
374:                     Log.e(TAG, "Failed to process handshake message from $peerID: ${e.message}")
```
> يسجّل رسالة خطأ بوسم `TAG` ونصّها «Failed to process handshake message from» متبوعاً بقيمة `peerID` ثم رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:374]

```
375:                     null
```
> القيمة `null` (وهي ناتج كتلة `catch`). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:375]

```
376:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:376]

```
377:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:377]

```
378:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:378]

```
379:             override fun updatePeerIDBinding(newPeerID: String, nickname: String,
```
> يعرّف بإعادة تعريف دالةً اسمها `updatePeerIDBinding` تأخذ مُعامِلاً نصّياً `newPeerID` ومُعامِلاً نصّياً `nickname` (وتتمّة المُعامِلات في السطر التالي). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:379]

```
380:                                            publicKey: ByteArray, previousPeerID: String?) {
```
> تتمّة مُعامِلات الدالة: `publicKey` من نوع `ByteArray` و`previousPeerID` نصّ قابل للعدم، ثم فتح جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:380]

```
381:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:381]

```
382:                 Log.d(TAG, "Updating peer ID binding: $newPeerID (was: $previousPeerID) with nickname: $nickname and public key: ${publicKey.toHexString().take(16)}...")
```
> يسجّل رسالة تنقيح بوسم `TAG` تتضمّن `newPeerID` و`previousPeerID` و`nickname` وأول ١٦ محرفاً من تمثيل `publicKey` السّتّ-عشري عبر `toHexString().take(16)`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:382]

```
383:                 // Update peer mapping in the PeerManager for peer ID rotation support
```
> تعليق: حدِّث ربط القرين في مدير الأقران (PeerManager) لدعم تدوير معرّف القرين. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:383]

```
384:                 peerManager.addOrUpdatePeer(newPeerID, nickname)
```
> يستدعي `addOrUpdatePeer` على مدير الأقران ممرّراً `newPeerID` و`nickname`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:384]

```
385:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:385]

```
386:                 // Store fingerprint for the peer via centralized fingerprint manager
```
> تعليق: خزِّن بصمة القرين عبر مدير البصمات المركزي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:386]

```
387:                 val fingerprint = peerManager.storeFingerprintForPeer(newPeerID, publicKey)
```
> يعرّف ثابتاً اسمه `fingerprint` ويُسنِد إليه ناتج استدعاء `storeFingerprintForPeer` على مدير الأقران ممرّراً `newPeerID` و`publicKey`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:387]

```
388:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:388]

```
389:                 // Index existing Nostr mapping by the new peerID if we have it
```
> تعليق: فهرِس ربط نوستر (Nostr) القائم بمعرّف القرين الجديد إن كان لدينا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:389]

```
390:                 try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:390]

```
391:                     com.bitchat.android.favorites.FavoritesPersistenceService.shared.findNostrPubkey(publicKey)?.let { npub ->
```
> يستدعي `findNostrPubkey` على النسخة المشتركة `shared` من خدمة استمرار المفضّلات (FavoritesPersistenceService) ممرّراً `publicKey`، وإن لم تكن النتيجة فارغة يدخل كتلة `let` بمتغيّر اسمه `npub`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:391]

```
392:                         com.bitchat.android.favorites.FavoritesPersistenceService.shared.updateNostrPublicKeyForPeerID(newPeerID, npub)
```
> يستدعي `updateNostrPublicKeyForPeerID` على النسخة المشتركة من خدمة استمرار المفضّلات ممرّراً `newPeerID` و`npub`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:392]

```
393:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:393]

```
394:                 } catch (_: Exception) { }
```
> يغلق كتلة `try` ويلتقط أيّ استثناء بكتلة `catch` فارغة دون تسمية الاستثناء. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:394]

```
395:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:395]

```
396:                 // If there was a previous peer ID, remove it to avoid duplicates
```
> تعليق: إن وُجِد معرّف قرين سابق، أزِله لتفادي التكرار. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:396]

```
397:                 previousPeerID?.let { oldPeerID ->
```
> إن لم يكن `previousPeerID` فارغاً يدخل كتلة `let` بمتغيّر اسمه `oldPeerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:397]

```
398:                     peerManager.removePeer(oldPeerID)
```
> يستدعي `removePeer` على مدير الأقران ممرّراً `oldPeerID`. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:398]

```
399:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:399]

```
400:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:400]
