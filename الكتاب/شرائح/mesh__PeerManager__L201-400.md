# شريحة — app/src/main/java/com/bitchat/android/mesh/PeerManager.kt (الأسطر 201–400)

```
201: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:201]

```
202:     // MARK: - Legacy Methods (maintained for compatibility)
```
> تعليق: علامة قسم «الدوال القديمة (مُحافَظ عليها للتوافق)». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:202]

```
203: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:203]

```
204:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:204]

```
205:      * Update peer last seen timestamp
```
> تعليق: «تحديث الطابع الزمني لآخر ظهور للنظير». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:205]

```
206:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:206]

```
207:     fun updatePeerLastSeen(peerID: String) {
```
> تعريف دالة (updatePeerLastSeen) تأخذ مُعرّف النظير (peerID) من نوع نص وتفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:207]

```
208:         if (peerID != "unknown") {
```
> شرط: إذا كان مُعرّف النظير لا يساوي النص «unknown» يُنفَّذ ما بداخله. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:208]

```
209:             peers[peerID]?.let { info ->
```
> يجلب قيمة الخريطة (peers) عند المُعرّف، وإن لم تكن فارغة يُنفّذ كتلة let مُسمّياً القيمة info. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:209]

```
210:                 peers[peerID] = info.copy(lastSeen = System.currentTimeMillis())
```
> يُسنِد إلى الخريطة (peers) عند المُعرّف نسخة من info مع تعديل آخر ظهور (lastSeen) إلى الوقت الحالي بالمللي ثانية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:210]

```
211:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:211]

```
212:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:212]

```
213:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:213]

```
214:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:214]

```
215:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:215]

```
216:      * Add or update peer with nickname
```
> تعليق: «إضافة نظير أو تحديثه مع الاسم المستعار». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:216]

```
217:      * Maintained for compatibility. Uses peers map exclusively now.
```
> تعليق: «مُحافَظ عليه للتوافق. يستعمل خريطة peers حصرياً الآن». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:217]

```
218:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:218]

```
219:     fun addOrUpdatePeer(peerID: String, nickname: String): Boolean {
```
> تعريف دالة (addOrUpdatePeer) تأخذ مُعرّف النظير واسماً مستعاراً (nickname) نصّيين وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:219]

```
220:         if (peerID == "unknown") return false
```
> شرط: إذا كان مُعرّف النظير يساوي النص «unknown» تُعيد الدالة القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:220]

```
221:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:221]

```
222:         // Clean up stale peer IDs with the same nickname (exact same logic as iOS)
```
> تعليق: «تنظيف مُعرّفات النظراء القديمة التي تحمل الاسم المستعار نفسه (المنطق نفسه تماماً كنظام iOS)». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:222]

```
223:         val now = System.currentTimeMillis()
```
> يُعرّف ثابتاً (now) ويُسنِد إليه الوقت الحالي بالمللي ثانية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:223]

```
224:         val stalePeerIDs = mutableListOf<String>()
```
> يُعرّف ثابتاً (stalePeerIDs) ويُسنِد إليه قائمة نصّية قابلة للتعديل فارغة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:224]

```
225:         peers.forEach { (existingPeerID, info) ->
```
> يمرّ على كل عنصر من الخريطة (peers) مُفكّكاً المفتاح إلى existingPeerID والقيمة إلى info. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:225]

```
226:             if (info.nickname == nickname && existingPeerID != peerID) {
```
> شرط: إذا كان اسم info المستعار يساوي الاسم المستعار المُمرّر، وكان existingPeerID لا يساوي مُعرّف النظير. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:226]

```
227:                 val wasRecentlySeen = (now - info.lastSeen) < 10000
```
> يُعرّف ثابتاً (wasRecentlySeen) يساوي نتيجة كون الفرق بين الوقت الحالي وآخر ظهور أصغر من 10000. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:227]

```
228:                 if (!wasRecentlySeen) {
```
> شرط: إذا كان wasRecentlySeen غير صحيح (أي لم يُرَ مؤخراً). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:228]

```
229:                     stalePeerIDs.add(existingPeerID)
```
> يضيف existingPeerID إلى قائمة المُعرّفات القديمة (stalePeerIDs). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:229]

```
230:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:230]

```
231:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:231]

```
232:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:232]

```
233:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:233]

```
234:         // Remove stale peer IDs
```
> تعليق: «إزالة مُعرّفات النظراء القديمة». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:234]

```
235:         stalePeerIDs.forEach { stalePeerID ->
```
> يمرّ على كل عنصر في قائمة المُعرّفات القديمة مُسمّياً العنصر stalePeerID. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:235]

```
236:             removePeer(stalePeerID, notifyDelegate = false)
```
> يستدعي الدالة removePeer للمُعرّف القديم مع تمرير notifyDelegate بقيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:236]

```
237:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:237]

```
238:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:238]

```
239:         // Check if this is a new peer announcement
```
> تعليق: «التحقق إن كان هذا إعلان نظير جديد». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:239]

```
240:         val isFirstAnnounce = !announcedPeers.contains(peerID)
```
> يُعرّف ثابتاً (isFirstAnnounce) يساوي نفي احتواء مجموعة النظراء المُعلَنين (announcedPeers) على المُعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:240]

```
241:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:241]

```
242:         // Update peer data
```
> تعليق: «تحديث بيانات النظير». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:242]

```
243:         val existing = peers[peerID]
```
> يُعرّف ثابتاً (existing) ويُسنِد إليه قيمة الخريطة (peers) عند المُعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:243]

```
244:         if (existing != null) {
```
> شرط: إذا كان existing لا يساوي قيمة فارغة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:244]

```
245:             peers[peerID] = existing.copy(nickname = nickname, lastSeen = now, isConnected = true)
```
> يُسنِد إلى الخريطة عند المُعرّف نسخة من existing مع الاسم المستعار، وآخر ظهور = now، والاتصال (isConnected) = true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:245]

```
246:         } else {
```
> وإلا (الفرع البديل للشرط). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:246]

```
247:             peers[peerID] = PeerInfo(
```
> يُسنِد إلى الخريطة عند المُعرّف كائن معلومات نظير (PeerInfo) جديداً وتُفتح وسائطه. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:247]

```
248:                 id = peerID,
```
> الوسيط id يساوي مُعرّف النظير. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:248]

```
249:                 nickname = nickname,
```
> الوسيط nickname يساوي الاسم المستعار المُمرّر. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:249]

```
250:                 isConnected = true,
```
> الوسيط isConnected يساوي true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:250]

```
251:                 isDirectConnection = false,
```
> الوسيط isDirectConnection (اتصال مباشر) يساوي false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:251]

```
252:                 noisePublicKey = null,
```
> الوسيط noisePublicKey (مفتاح Noise العام) يساوي قيمة فارغة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:252]

```
253:                 signingPublicKey = null,
```
> الوسيط signingPublicKey (مفتاح التوقيع العام) يساوي قيمة فارغة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:253]

```
254:                 isVerifiedNickname = false,
```
> الوسيط isVerifiedNickname (اسم مستعار مُوثَّق) يساوي false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:254]

```
255:                 lastSeen = now
```
> الوسيط lastSeen (آخر ظهور) يساوي now. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:255]

```
256:             )
```
> إغلاق وسائط مُنشئ PeerInfo. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:256]

```
257:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:257]

```
258:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:258]

```
259:         // Handle first announcement
```
> تعليق: «معالجة الإعلان الأول». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:259]

```
260:         if (isFirstAnnounce) {
```
> شرط: إذا كان isFirstAnnounce صحيحاً. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:260]

```
261:             announcedPeers.add(peerID)
```
> يضيف المُعرّف إلى مجموعة النظراء المُعلَنين (announcedPeers). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:261]

```
262:             notifyPeerListUpdate()
```
> يستدعي الدالة notifyPeerListUpdate (إشعار بتحديث قائمة النظراء). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:262]

```
263:             return true
```
> تُعيد الدالة القيمة true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:263]

```
264:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:264]

```
265:         Log.d(TAG, "Updated peer: $peerID ($nickname)")
```
> يسجّل رسالة تصحيح (debug) بالوسم TAG نصّها «Updated peer: <المُعرّف> (<الاسم المستعار>)». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:265]

```
266:         return false
```
> تُعيد الدالة القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:266]

```
267:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:267]

```
268:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:268]

```
269:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:269]

```
270:      * Remove peer
```
> تعليق: «إزالة نظير». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:270]

```
271:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:271]

```
272:     fun removePeer(peerID: String, notifyDelegate: Boolean = true) {
```
> تعريف دالة (removePeer) تأخذ مُعرّف النظير ووسيطاً منطقياً notifyDelegate قيمته الافتراضية true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:272]

```
273:         val removed = peers.remove(peerID)
```
> يُعرّف ثابتاً (removed) ويُسنِد إليه نتيجة إزالة المُعرّف من الخريطة (peers). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:273]

```
274:         peerRSSI.remove(peerID)
```
> يزيل المُعرّف من خريطة قوة الإشارة (peerRSSI). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:274]

```
275:         announcedPeers.remove(peerID)
```
> يزيل المُعرّف من مجموعة النظراء المُعلَنين (announcedPeers). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:275]

```
276:         announcedToPeers.remove(peerID)
```
> يزيل المُعرّف من مجموعة النظراء المُعلَن إليهم (announcedToPeers). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:276]

```
277:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:277]

```
278:         // Also remove fingerprint mappings
```
> تعليق: «إزالة تخطيطات البصمة أيضاً». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:278]

```
279:         fingerprintManager.removePeer(peerID)
```
> يستدعي removePeer على مدير البصمات (fingerprintManager) للمُعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:279]

```
280:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:280]

```
281:         if (notifyDelegate && removed != null) {
```
> شرط: إذا كان notifyDelegate صحيحاً وكان removed لا يساوي قيمة فارغة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:281]

```
282:             // Notify specific removal event then list update
```
> تعليق: «الإشعار بحدث إزالة مُحدَّد ثم تحديث القائمة». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:282]

```
283:             try { delegate?.onPeerRemoved(peerID) } catch (_: Exception) {}
```
> يحاول استدعاء onPeerRemoved على المُفوَّض (delegate) إن لم يكن فارغاً، ويلتقط أي استثناء (Exception) دون فعل. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:283]

```
284:             notifyPeerListUpdate()
```
> يستدعي الدالة notifyPeerListUpdate. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:284]

```
285:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:285]

```
286:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:286]

```
287:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:287]

```
288:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:288]

```
289:      * Update peer RSSI
```
> تعليق: «تحديث قوة إشارة النظير (RSSI)». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:289]

```
290:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:290]

```
291:     fun updatePeerRSSI(peerID: String, rssi: Int) {
```
> تعريف دالة (updatePeerRSSI) تأخذ مُعرّف النظير وقيمة قوة الإشارة (rssi) من نوع صحيح. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:291]

```
292:         if (peerID != "unknown") {
```
> شرط: إذا كان مُعرّف النظير لا يساوي النص «unknown». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:292]

```
293:             peerRSSI[peerID] = rssi
```
> يُسنِد إلى خريطة قوة الإشارة (peerRSSI) عند المُعرّف قيمة rssi. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:293]

```
294:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:294]

```
295:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:295]

```
296:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:296]

```
297:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:297]

```
298:      * Check if peer has been announced to
```
> تعليق: «التحقق إن كان النظير قد أُعلِن إليه». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:298]

```
299:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:299]

```
300:     fun hasAnnouncedToPeer(peerID: String): Boolean {
```
> تعريف دالة (hasAnnouncedToPeer) تأخذ مُعرّف النظير وتُعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:300]

```
301:         return announcedToPeers.contains(peerID)
```
> تُعيد نتيجة احتواء مجموعة النظراء المُعلَن إليهم (announcedToPeers) على المُعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:301]

```
302:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:302]

```
303:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:303]

```
304:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:304]

```
305:      * Mark peer as announced to
```
> تعليق: «وسم النظير بأنه قد أُعلِن إليه». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:305]

```
306:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:306]

```
307:     fun markPeerAsAnnouncedTo(peerID: String) {
```
> تعريف دالة (markPeerAsAnnouncedTo) تأخذ مُعرّف النظير. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:307]

```
308:         if (!announcedToPeers.contains(peerID)) {
```
> شرط: إذا كانت مجموعة النظراء المُعلَن إليهم لا تحتوي على المُعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:308]

```
309:             announcedToPeers.add(peerID)
```
> يضيف المُعرّف إلى مجموعة النظراء المُعلَن إليهم (announcedToPeers). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:309]

```
310:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:310]

```
311:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:311]

```
312:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:312]

```
313:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:313]

```
314:      * Check if peer is active
```
> تعليق: «التحقق إن كان النظير نشطاً». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:314]

```
315:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:315]

```
316:     fun isPeerActive(peerID: String): Boolean {
```
> تعريف دالة (isPeerActive) تأخذ مُعرّف النظير وتُعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:316]

```
317:         val info = peers[peerID] ?: return false
```
> يُعرّف ثابتاً (info) يساوي قيمة الخريطة عند المُعرّف، وإن كانت فارغة تُعيد الدالة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:317]

```
318:         return info.isConnected
```
> تُعيد قيمة isConnected (متّصل) من info. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:318]

```
319:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:319]

```
320:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:320]

```
321:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:321]

```
322:      * Get peer nickname
```
> تعليق: «جلب الاسم المستعار للنظير». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:322]

```
323:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:323]

```
324:     fun getPeerNickname(peerID: String): String? {
```
> تعريف دالة (getPeerNickname) تأخذ مُعرّف النظير وتُعيد نصّاً قابلاً للقيمة الفارغة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:324]

```
325:         return peers[peerID]?.nickname
```
> تُعيد الاسم المستعار من قيمة الخريطة عند المُعرّف إن لم تكن فارغة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:325]

```
326:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:326]

```
327:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:327]

```
328:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:328]

```
329:      * Get all peer nicknames
```
> تعليق: «جلب كل الأسماء المستعارة للنظراء». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:329]

```
330:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:330]

```
331:     fun getAllPeerNicknames(): Map<String, String> {
```
> تعريف دالة (getAllPeerNicknames) تُعيد خريطة من نص إلى نص. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:331]

```
332:         return peers.mapValues { it.value.nickname }
```
> تُعيد الخريطة (peers) بعد تحويل كل قيمة إلى اسمها المستعار. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:332]

```
333:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:333]

```
334:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:334]

```
335:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:335]

```
336:      * Get all peer RSSI values
```
> تعليق: «جلب كل قيم قوة الإشارة للنظراء». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:336]

```
337:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:337]

```
338:     fun getAllPeerRSSI(): Map<String, Int> {
```
> تعريف دالة (getAllPeerRSSI) تُعيد خريطة من نص إلى عدد صحيح. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:338]

```
339:         return peerRSSI.toMap()
```
> تُعيد خريطة قوة الإشارة (peerRSSI) محوّلة إلى خريطة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:339]

```
340:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:340]

```
341:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:341]

```
342:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:342]

```
343:      * Get list of active peer IDs
```
> تعليق: «جلب قائمة مُعرّفات النظراء النشطين». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:343]

```
344:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:344]

```
345:     fun getActivePeerIDs(): List<String> {
```
> تعريف دالة (getActivePeerIDs) تُعيد قائمة نصّية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:345]

```
346:         return peers.filterValues { it.isConnected }
```
> تُعيد الخريطة (peers) بعد تصفية القيم بمن isConnected لديه صحيح. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:346]

```
347:             .keys
```
> يأخذ مفاتيح الناتج (keys). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:347]

```
348:             .toList()
```
> يحوّل المفاتيح إلى قائمة (toList). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:348]

```
349:             .sorted()
```
> يرتّب القائمة تصاعدياً (sorted). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:349]

```
350:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:350]

```
351:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:351]

```
352:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:352]

```
353:      * Get active peer count
```
> تعليق: «جلب عدد النظراء النشطين». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:353]

```
354:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:354]

```
355:     fun getActivePeerCount(): Int {
```
> تعريف دالة (getActivePeerCount) تُعيد عدداً صحيحاً. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:355]

```
356:         return getActivePeerIDs().size
```
> تُعيد حجم (size) ناتج استدعاء getActivePeerIDs. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:356]

```
357:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:357]

```
358:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:358]

```
359:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:359]

```
360:      * Clear all peer data
```
> تعليق: «مسح كل بيانات النظراء». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:360]

```
361:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:361]

```
362:     fun clearAllPeers() {
```
> تعريف دالة (clearAllPeers) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:362]

```
363:         peers.clear()
```
> يمسح الخريطة (peers). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:363]

```
364:         peerRSSI.clear()
```
> يمسح خريطة قوة الإشارة (peerRSSI). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:364]

```
365:         announcedPeers.clear()
```
> يمسح مجموعة النظراء المُعلَنين (announcedPeers). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:365]

```
366:         announcedToPeers.clear()
```
> يمسح مجموعة النظراء المُعلَن إليهم (announcedToPeers). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:366]

```
367:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:367]

```
368:         // Also clear fingerprint mappings
```
> تعليق: «مسح تخطيطات البصمة أيضاً». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:368]

```
369:         fingerprintManager.clearAllFingerprints()
```
> يستدعي clearAllFingerprints على مدير البصمات (fingerprintManager). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:369]

```
370:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:370]

```
371:         notifyPeerListUpdate()
```
> يستدعي الدالة notifyPeerListUpdate. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:371]

```
372:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:372]

```
373:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:373]

```
374:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:374]

```
375:      * Get debug information
```
> تعليق: «جلب معلومات التصحيح». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:375]

```
376:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:376]

```
377:     fun getDebugInfo(addressPeerMap: Map<String, String>? = null): String {
```
> تعريف دالة (getDebugInfo) تأخذ خريطة عناوين-نظراء (addressPeerMap) من نص إلى نص قابلة للقيمة الفارغة بقيمة افتراضية null، وتُعيد نصّاً. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:377]

```
378:         val now = System.currentTimeMillis()
```
> يُعرّف ثابتاً (now) ويُسنِد إليه الوقت الحالي بالمللي ثانية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:378]

```
379:         val activeIds = getActivePeerIDs().toSet()
```
> يُعرّف ثابتاً (activeIds) يساوي ناتج getActivePeerIDs محوّلاً إلى مجموعة (toSet). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:379]

```
380:         return buildString {
```
> تُعيد الدالة ناتج باني النص (buildString) وتفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:380]

```
381:             appendLine("=== Peer Manager Debug Info ===")
```
> يُلحِق سطراً نصّه «=== Peer Manager Debug Info ===». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:381]

```
382:             appendLine("Active Peers: ${activeIds.size}")
```
> يُلحِق سطراً نصّه «Active Peers: <حجم activeIds>». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:382]

```
383:             peers.forEach { (peerID, storedInfo) ->
```
> يمرّ على كل عنصر من الخريطة (peers) مُفكّكاً المفتاح إلى peerID والقيمة إلى storedInfo. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:383]

```
384:                 // Use dynamic direct status for debug log accuracy
```
> تعليق: «استعمال حالة الاتصال المباشر الديناميكية لدقّة سجل التصحيح». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:384]

```
385:                 val isDirect = isPeerDirectlyConnected?.invoke(peerID) ?: false
```
> يُعرّف ثابتاً (isDirect) يساوي ناتج استدعاء الدالة isPeerDirectlyConnected للمُعرّف إن لم تكن فارغة، وإلا false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:385]

```
386:                 val info = if (storedInfo.isDirectConnection != isDirect) storedInfo.copy(isDirectConnection = isDirect) else storedInfo
```
> يُعرّف ثابتاً (info) يساوي نسخة من storedInfo بتعديل isDirectConnection إلى isDirect إن اختلفا، وإلا storedInfo نفسه. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:386]

```
387:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:387]

```
388:                 val timeSince = (now - info.lastSeen) / 1000
```
> يُعرّف ثابتاً (timeSince) يساوي الفرق بين الوقت الحالي وآخر ظهور مقسوماً على 1000. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:388]

```
389:                 val rssi = peerRSSI[peerID]?.let { "${it} dBm" } ?: "No RSSI"
```
> يُعرّف ثابتاً (rssi) يساوي نصّ «<القيمة> dBm» إن وُجدت قوة إشارة للمُعرّف، وإلا «No RSSI». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:389]

```
390:                 val deviceAddress = addressPeerMap?.entries?.find { it.value == peerID }?.key
```
> يُعرّف ثابتاً (deviceAddress) يساوي مفتاح أول مدخلة في خريطة العناوين-النظراء قيمتها تساوي المُعرّف، إن وُجدت. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:390]

```
391:                 val addressInfo = deviceAddress?.let { " [Device: $it]" } ?: " [Device: Unknown]"
```
> يُعرّف ثابتاً (addressInfo) يساوي نصّ « [Device: <العنوان>]» إن وُجد العنوان، وإلا « [Device: Unknown]». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:391]

```
392:                 val status = if (activeIds.contains(peerID)) "ACTIVE" else "INACTIVE"
```
> يُعرّف ثابتاً (status) يساوي «ACTIVE» إن احتوت مجموعة المُعرّفات النشطة على المُعرّف، وإلا «INACTIVE». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:392]

```
393:                 val direct = if (info.isDirectConnection) "DIRECT" else "ROUTED"
```
> يُعرّف ثابتاً (direct) يساوي «DIRECT» إن كان اتصال info مباشراً، وإلا «ROUTED». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:393]

```
394:                 appendLine("  - $peerID (${info.nickname})$addressInfo - $status/$direct, last seen ${timeSince}s ago, RSSI: $rssi")
```
> يُلحِق سطراً نصّه «  - <المُعرّف> (<الاسم المستعار>)<معلومات العنوان> - <الحالة>/<النوع>, last seen <الزمن>s ago, RSSI: <قوة الإشارة>». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:394]

```
395:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:395]

```
396:             appendLine("Announced Peers: ${announcedPeers.size}")
```
> يُلحِق سطراً نصّه «Announced Peers: <حجم announcedPeers>». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:396]

```
397:             appendLine("Announced To Peers: ${announcedToPeers.size}")
```
> يُلحِق سطراً نصّه «Announced To Peers: <حجم announcedToPeers>». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:397]

```
398:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:398]

```
399:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:399]

```
400:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:400]
