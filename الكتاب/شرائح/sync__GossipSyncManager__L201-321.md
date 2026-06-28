# شريحة — app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt (الأسطر 201–321)

```
201:     private fun hexStringToByteArray(hexString: String): ByteArray {
```
> تُعرَّف دالة خاصة (private) اسمها «hexStringToByteArray» (تحويل نص ست‑عشري إلى مصفوفة بايتات) تأخذ مُعاملاً نصياً (hexString) من نوع String وتُعيد مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:201]

```
202:         val result = ByteArray(8) { 0 }
```
> يُعرَّف متغيّر ثابت اسمه «result» (النتيجة) كمصفوفة بايتات طولها ٨، وكل عنصر فيها مضبوط بالقيمة ٠. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:202]

```
203:         var tempID = hexString
```
> يُعرَّف متغيّر قابل للتغيير اسمه «tempID» (المعرّف المؤقت) ويُضبط بقيمة المُعامل hexString. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:203]

```
204:         var index = 0
```
> يُعرَّف متغيّر قابل للتغيير اسمه «index» (الفهرس) ويُضبط بالقيمة ٠. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:204]

```
205:         while (tempID.length >= 2 && index < 8) {
```
> تبدأ حلقة «while» (طالما) تستمر طالما طول tempID أكبر من أو يساوي ٢ وفي الوقت نفسه index أصغر من ٨. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:205]

```
206:             val hexByte = tempID.substring(0, 2)
```
> يُعرَّف متغيّر ثابت اسمه «hexByte» (البايت الست‑عشري) ويُضبط بالنص الجزئي من tempID من الموضع ٠ إلى الموضع ٢ (الحرفان الأولان). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:206]

```
207:             val byte = hexByte.toIntOrNull(16)?.toByte()
```
> يُعرَّف متغيّر ثابت اسمه «byte» (البايت) ويُضبط بتحويل hexByte إلى عدد صحيح بالأساس ١٦ (toIntOrNull) ثم إلى بايت (toByte)، وتكون قيمته فارغة (null) إن فشل التحويل. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:207]

```
208:             if (byte != null) result[index] = byte
```
> إن كان byte غير فارغ (null) فيُضبط عنصر المصفوفة result عند الموضع index بقيمة byte. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:208]

```
209:             tempID = tempID.substring(2)
```
> يُعاد ضبط tempID بالنص الجزئي منه ابتداءً من الموضع ٢ (أي بحذف أول حرفين). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:209]

```
210:             index++
```
> يُزاد index بمقدار واحد. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:210]

```
211:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:211]

```
212:         return result
```
> تُعيد الدالة المصفوفة result. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:212]

```
213:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:213]

```
214: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:214]

```
215:     private fun hexToBytes(hex: String): ByteArray {
```
> تُعرَّف دالة خاصة (private) اسمها «hexToBytes» (ست‑عشري إلى بايتات) تأخذ مُعاملاً نصياً (hex) من نوع String وتُعيد مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:215]

```
216:         val clean = if (hex.length % 2 == 0) hex else "0$hex"
```
> يُعرَّف متغيّر ثابت اسمه «clean» (النظيف) ويُضبط بقيمة hex إن كان طوله زوجياً (باقي القسمة على ٢ يساوي ٠)، وإلا بقيمة hex مسبوقة بالحرف «0». [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:216]

```
217:         val out = ByteArray(clean.length / 2)
```
> يُعرَّف متغيّر ثابت اسمه «out» (الخرج) كمصفوفة بايتات طولها يساوي طول clean مقسوماً على ٢. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:217]

```
218:         var i = 0
```
> يُعرَّف متغيّر قابل للتغيير اسمه «i» ويُضبط بالقيمة ٠. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:218]

```
219:         while (i < clean.length) {
```
> تبدأ حلقة «while» (طالما) تستمر طالما i أصغر من طول clean. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:219]

```
220:             out[i/2] = clean.substring(i, i+2).toInt(16).toByte()
```
> يُضبط عنصر المصفوفة out عند الموضع i مقسوماً على ٢ بقيمة النص الجزئي من clean بين الموضعين i و i+2 بعد تحويله إلى عدد صحيح بالأساس ١٦ (toInt) ثم إلى بايت (toByte). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:220]

```
221:             i += 2
```
> يُزاد i بمقدار ٢. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:221]

```
222:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:222]

```
223:         return out
```
> تُعيد الدالة المصفوفة out. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:223]

```
224:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:224]

```
225: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:225]

```
226:     private fun buildGcsPayload(): ByteArray {
```
> تُعرَّف دالة خاصة (private) اسمها «buildGcsPayload» (بناء حمولة GCS) لا تأخذ مُعاملات وتُعيد مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:226]

```
227:         // Collect candidates: latest announcement per peer + recent broadcast messages
```
> تعليق: اجمع المرشّحين: آخر إعلان لكل قرين (peer) + رسائل البثّ الأخيرة. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:227]

```
228:         val list = ArrayList<BitchatPacket>()
```
> يُعرَّف متغيّر ثابت اسمه «list» (القائمة) كقائمة مصفوفية (ArrayList) من عناصر نوعها BitchatPacket (حزمة بِت‑شات). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:228]

```
229:         // announcements
```
> تعليق: الإعلانات. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:229]

```
230:         for ((_, pair) in latestAnnouncementByPeer) {
```
> تبدأ حلقة «for» تمرّ على عناصر latestAnnouncementByPeer (آخر إعلان حسب القرين)، متجاهلةً المفتاح (_) ومسمّيةً القيمة «pair» (الزوج). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:230]

```
231:             list.add(pair.second)
```
> يُضاف العنصر الثاني من pair (pair.second) إلى القائمة list. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:231]

```
232:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:232]

```
233:         // messages
```
> تعليق: الرسائل. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:233]

```
234:         synchronized(messages) {
```
> تبدأ كتلة متزامنة (synchronized) تقفل على الكائن messages (الرسائل). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:234]

```
235:             list.addAll(messages.values)
```
> تُضاف كل قيم messages (messages.values) إلى القائمة list. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:235]

```
236:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:236]

```
237:         // sort by timestamp desc, then take up to min(seenCapacity, fit capacity)
```
> تعليق: رتّب حسب الطابع الزمني تنازلياً، ثم خُذ حتى الحد الأدنى من (seenCapacity، السعة المناسبة). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:237]

```
238:         list.sortByDescending { it.timestamp.toLong() }
```
> تُرتَّب القائمة list تنازلياً (sortByDescending) حسب الطابع الزمني (timestamp) للعنصر محوَّلاً إلى عدد طويل (toLong). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:238]

```
239: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:239]

```
240:         val maxBytes = try { configProvider.gcsMaxBytes() } catch (_: Exception) { defaultMaxBytes }
```
> يُعرَّف متغيّر ثابت اسمه «maxBytes» (أقصى بايتات) ويُضبط بنتيجة استدعاء configProvider.gcsMaxBytes() داخل كتلة try، وعند حدوث استثناء (Exception) يُضبط بقيمة defaultMaxBytes (أقصى بايتات افتراضي). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:240]

```
241:         val fpr = try { configProvider.gcsTargetFpr() } catch (_: Exception) { defaultFpr }
```
> يُعرَّف متغيّر ثابت اسمه «fpr» (معدّل الإيجابيات الكاذبة) ويُضبط بنتيجة استدعاء configProvider.gcsTargetFpr() داخل كتلة try، وعند حدوث استثناء (Exception) يُضبط بقيمة defaultFpr (المعدّل الافتراضي). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:241]

```
242:         val p = GCSFilter.deriveP(fpr)
```
> يُعرَّف متغيّر ثابت اسمه «p» ويُضبط بنتيجة استدعاء GCSFilter.deriveP (اشتقاق p) ممرّراً fpr. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:242]

```
243:         val nMax = GCSFilter.estimateMaxElementsForSize(maxBytes, p)
```
> يُعرَّف متغيّر ثابت اسمه «nMax» (أقصى عدد) ويُضبط بنتيجة استدعاء GCSFilter.estimateMaxElementsForSize (تقدير أقصى عدد عناصر للحجم) ممرّراً maxBytes و p. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:243]

```
244:         val cap = configProvider.seenCapacity().coerceAtLeast(1)
```
> يُعرَّف متغيّر ثابت اسمه «cap» (السعة) ويُضبط بنتيجة استدعاء configProvider.seenCapacity() مقيَّدةً بحد أدنى ١ (coerceAtLeast). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:244]

```
245:         val takeN = minOf(nMax, cap, list.size)
```
> يُعرَّف متغيّر ثابت اسمه «takeN» (عدد المأخوذ) ويُضبط بأصغر القيم (minOf) من nMax و cap وحجم القائمة list.size. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:245]

```
246:         if (takeN <= 0) {
```
> تبدأ جملة شرطية «if» تتحقق إن كان takeN أصغر من أو يساوي ٠. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:246]

```
247:             val p0 = GCSFilter.deriveP(fpr)
```
> يُعرَّف متغيّر ثابت اسمه «p0» ويُضبط بنتيجة استدعاء GCSFilter.deriveP (اشتقاق p) ممرّراً fpr. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:247]

```
248:             return RequestSyncPacket(p = p0, m = 1, data = ByteArray(0)).encode()
```
> تُعيد الدالة نتيجة ترميز (encode) حزمة طلب مزامنة (RequestSyncPacket) منشأة بالوسائط p = p0 و m = 1 و data = مصفوفة بايتات فارغة (طولها ٠). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:248]

```
249:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:249]

```
250:         val ids = list.take(takeN).map { pkt -> PacketIdUtil.computeIdBytes(pkt) }
```
> يُعرَّف متغيّر ثابت اسمه «ids» (المعرّفات) ويُضبط بأخذ أول takeN عنصراً من list ثم تحويل (map) كل عنصر مسمّى «pkt» إلى نتيجة استدعاء PacketIdUtil.computeIdBytes (حساب بايتات معرّف الحزمة) ممرّراً pkt. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:250]

```
251:         val params = GCSFilter.buildFilter(ids, maxBytes, fpr)
```
> يُعرَّف متغيّر ثابت اسمه «params» (المعاملات) ويُضبط بنتيجة استدعاء GCSFilter.buildFilter (بناء مرشّح) ممرّراً ids و maxBytes و fpr. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:251]

```
252:         val mVal = if (params.m <= 0L) 1 else params.m
```
> يُعرَّف متغيّر ثابت اسمه «mVal» (قيمة m) ويُضبط بالقيمة ١ إن كان params.m أصغر من أو يساوي ٠ (طويل)، وإلا بقيمة params.m. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:252]

```
253:         return RequestSyncPacket(p = params.p, m = mVal, data = params.data).encode()
```
> تُعيد الدالة نتيجة ترميز (encode) حزمة طلب مزامنة (RequestSyncPacket) منشأة بالوسائط p = params.p و m = mVal و data = params.data. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:253]

```
254:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:254]

```
255: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:255]

```
256:     // Periodically remove stale announcements and all their messages
```
> تعليق: أزِل دورياً الإعلانات البائتة وكل رسائلها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:256]

```
257:     private fun pruneStaleAnnouncements() {
```
> تُعرَّف دالة خاصة (private) اسمها «pruneStaleAnnouncements» (تقليم الإعلانات البائتة) لا تأخذ مُعاملات. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:257]

```
258:         val now = System.currentTimeMillis()
```
> يُعرَّف متغيّر ثابت اسمه «now» (الآن) ويُضبط بالوقت الحالي بالمليّات (System.currentTimeMillis). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:258]

```
259:         val stalePeers = mutableListOf<String>()
```
> يُعرَّف متغيّر ثابت اسمه «stalePeers» (القرناء البائتون) كقائمة قابلة للتغيير (mutableListOf) من نصوص (String). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:259]

```
260: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:260]

```
261:         // Identify stale announcements by age
```
> تعليق: حدّد الإعلانات البائتة حسب العُمر. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:261]

```
262:         for ((peerID, pair) in latestAnnouncementByPeer.entries) {
```
> تبدأ حلقة «for» تمرّ على مُدخلات latestAnnouncementByPeer.entries، مسمّيةً المفتاح «peerID» (معرّف القرين) والقيمة «pair» (الزوج). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:262]

```
263:             val pkt = pair.second
```
> يُعرَّف متغيّر ثابت اسمه «pkt» (الحزمة) ويُضبط بالعنصر الثاني من pair (pair.second). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:263]

```
264:             val age = now - pkt.timestamp.toLong()
```
> يُعرَّف متغيّر ثابت اسمه «age» (العُمر) ويُضبط بناتج طرح الطابع الزمني للحزمة (pkt.timestamp محوَّلاً إلى طويل toLong) من now. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:264]

```
265:             if (age > com.bitchat.android.util.AppConstants.Mesh.STALE_PEER_TIMEOUT_MS) {
```
> تبدأ جملة شرطية «if» تتحقق إن كان age أكبر من الثابت com.bitchat.android.util.AppConstants.Mesh.STALE_PEER_TIMEOUT_MS (مهلة القرين البائت بالمليّات). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:265]

```
266:                 stalePeers.add(peerID)
```
> يُضاف peerID إلى القائمة stalePeers. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:266]

```
267:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:267]

```
268:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:268]

```
269: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:269]

```
270:         if (stalePeers.isEmpty()) return
```
> إن كانت القائمة stalePeers فارغة (isEmpty) فتُنهى الدالة بـ return. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:270]

```
271: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:271]

```
272:         // Remove announcements and their messages
```
> تعليق: أزِل الإعلانات ورسائلها. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:272]

```
273:         var totalPrunedMsgs = 0
```
> يُعرَّف متغيّر قابل للتغيير اسمه «totalPrunedMsgs» (إجمالي الرسائل المقلَّمة) ويُضبط بالقيمة ٠. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:273]

```
274:         for (peerID in stalePeers) {
```
> تبدأ حلقة «for» تمرّ على عناصر stalePeers مسمّيةً كلاً منها «peerID». [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:274]

```
275:             // Count messages to be pruned for logging
```
> تعليق: عُدّ الرسائل المراد تقليمها لأجل التسجيل. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:275]

```
276:             val toRemove = mutableListOf<String>()
```
> يُعرَّف متغيّر ثابت اسمه «toRemove» (المراد إزالته) كقائمة قابلة للتغيير (mutableListOf) من نصوص (String). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:276]

```
277:             synchronized(messages) {
```
> تبدأ كتلة متزامنة (synchronized) تقفل على الكائن messages. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:277]

```
278:                 for ((id, message) in messages) {
```
> تبدأ حلقة «for» تمرّ على messages مسمّيةً المفتاح «id» والقيمة «message» (الرسالة). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:278]

```
279:                     val sender = message.senderID.joinToString("") { b -> "%02x".format(b) }
```
> يُعرَّف متغيّر ثابت اسمه «sender» (المرسِل) ويُضبط بدمج (joinToString) عناصر message.senderID (معرّف المرسِل) بفاصل فارغ، مع تنسيق كل بايت b بصيغة ست‑عشرية من خانتين («%02x».format). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:279]

```
280:                     if (sender == peerID) toRemove.add(id)
```
> إن كان sender يساوي peerID فيُضاف id إلى القائمة toRemove. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:280]

```
281:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:281]

```
282:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:282]

```
283:             totalPrunedMsgs += toRemove.size
```
> يُزاد totalPrunedMsgs بمقدار حجم القائمة toRemove (toRemove.size). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:283]

```
284: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:284]

```
285:             // Reuse existing removal which also clears announcement entry
```
> تعليق: أعِد استعمال الإزالة الموجودة التي تمسح أيضاً مُدخل الإعلان. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:285]

```
286:             removeAnnouncementForPeer(peerID)
```
> تُستدعى الدالة removeAnnouncementForPeer (إزالة إعلان القرين) ممرّرةً peerID. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:286]

```
287:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:287]

```
288: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:288]

```
289:         Log.d(TAG, "Pruned ${stalePeers.size} stale announcements and $totalPrunedMsgs messages")
```
> يُستدعى Log.d (تسجيل تنقيح) ممرّراً TAG ونصاً يقول «Pruned» متبوعاً بحجم stalePeers (stalePeers.size) ثم «stale announcements and» ثم totalPrunedMsgs ثم «messages». [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:289]

```
290:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:290]

```
291: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:291]

```
292:     // Explicitly remove stored announcement for a given peer (hex ID)
```
> تعليق: أزِل صراحةً الإعلان المخزّن لقرين مُعطى (معرّف ست‑عشري). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:292]

```
293:     fun removeAnnouncementForPeer(peerID: String) {
```
> تُعرَّف دالة عمومية اسمها «removeAnnouncementForPeer» (إزالة إعلان القرين) تأخذ مُعاملاً نصياً (peerID) من نوع String. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:293]

```
294:         val key = peerID.lowercase()
```
> يُعرَّف متغيّر ثابت اسمه «key» (المفتاح) ويُضبط بقيمة peerID بحروف صغيرة (lowercase). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:294]

```
295:         if (latestAnnouncementByPeer.remove(key) != null) {
```
> تبدأ جملة شرطية «if» تتحقق إن كانت نتيجة إزالة المفتاح key من latestAnnouncementByPeer (remove) غير فارغة (null). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:295]

```
296:             Log.d(TAG, "Removed stored announcement for peer $peerID")
```
> يُستدعى Log.d (تسجيل تنقيح) ممرّراً TAG ونصاً يقول «Removed stored announcement for peer» متبوعاً بـ peerID. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:296]

```
297:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:297]

```
298: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:298]

```
299:         // Collect IDs to remove first to avoid modifying collection while iterating
```
> تعليق: اجمع المعرّفات المراد إزالتها أولاً لتفادي تعديل المجموعة أثناء التكرار. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:299]

```
300:         val idsToRemove = mutableListOf<String>()
```
> يُعرَّف متغيّر ثابت اسمه «idsToRemove» (المعرّفات المراد إزالتها) كقائمة قابلة للتغيير (mutableListOf) من نصوص (String). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:300]

```
301:         synchronized(messages) {
```
> تبدأ كتلة متزامنة (synchronized) تقفل على الكائن messages. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:301]

```
302:             for ((id, message) in messages) {
```
> تبدأ حلقة «for» تمرّ على messages مسمّيةً المفتاح «id» والقيمة «message». [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:302]

```
303:                 val sender = message.senderID.joinToString("") { b -> "%02x".format(b) }
```
> يُعرَّف متغيّر ثابت اسمه «sender» (المرسِل) ويُضبط بدمج (joinToString) عناصر message.senderID بفاصل فارغ، مع تنسيق كل بايت b بصيغة ست‑عشرية من خانتين («%02x».format). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:303]

```
304:                 if (sender == key) {
```
> تبدأ جملة شرطية «if» تتحقق إن كان sender يساوي key. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:304]

```
305:                     idsToRemove.add(id)
```
> يُضاف id إلى القائمة idsToRemove. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:305]

```
306:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:306]

```
307:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:307]

```
308:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:308]

```
309:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:309]

```
310:         // Now remove the collected IDs
```
> تعليق: الآن أزِل المعرّفات المجموعة. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:310]

```
311:         synchronized(messages) {
```
> تبدأ كتلة متزامنة (synchronized) تقفل على الكائن messages. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:311]

```
312:             for (id in idsToRemove) {
```
> تبدأ حلقة «for» تمرّ على عناصر idsToRemove مسمّيةً كلاً منها «id». [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:312]

```
313:                 messages.remove(id)
```
> تُزال من messages العنصر ذو المفتاح id (remove). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:313]

```
314:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:314]

```
315:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:315]

```
316:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:316]

```
317:         if (idsToRemove.isNotEmpty()) {
```
> تبدأ جملة شرطية «if» تتحقق إن كانت القائمة idsToRemove غير فارغة (isNotEmpty). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:317]

```
318:             Log.d(TAG, "Pruned ${idsToRemove.size} messages with senders without announcements")
```
> يُستدعى Log.d (تسجيل تنقيح) ممرّراً TAG ونصاً يقول «Pruned» متبوعاً بحجم idsToRemove (idsToRemove.size) ثم «messages with senders without announcements». [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:318]

```
319:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:319]

```
320:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:320]

```
321: }
```
> إغلاق نطاق (نهاية الصنف). [app/src/main/java/com/bitchat/android/sync/GossipSyncManager.kt:321]
