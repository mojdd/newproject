# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt (الأسطر 1201–1400)

```
1201: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1201]

```
1202:         // Track announce for sync
```
> تعليق: تتبّع الإعلان لأجل المزامنة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1202]

```
1203:         try { gossipSyncManager.onPublicPacketSeen(signedPacket) } catch (_: Exception) { }
```
> كتلة محاولة (try) تستدعي على مدير مزامنة الإشاعة (gossipSyncManager) الدالة onPublicPacketSeen ممرّرةً الحزمة الموقّعة (signedPacket)، وكتلة التقاط (catch) لأي استثناء (Exception) فارغة لا تفعل شيئاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1203]

```
1204:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1204]

```
1205: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1205]

```
1206:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1206]

```
1207:      * Collect up to 10 direct neighbors for gossip TLV.
```
> تعليق: اجمع حتى ١٠ جيران مباشرين لأجل بنية TLV الخاصة بالإشاعة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1207]

```
1208:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1208]

```
1209:     private fun getDirectPeerIDsForGossip(): List<String> {
```
> تعريف دالة خاصة (private) باسم getDirectPeerIDsForGossip لا تأخذ وسائط وتعيد قائمة (List) من سلاسل نصية (String). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1209]

```
1210:         return try {
```
> تعيد قيمة تعبير المحاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1210]

```
1211:             // Prefer verified peers that are currently marked as direct
```
> تعليق: فضّل الأقران المُتحقَّق منهم المُعلَّمين حالياً كمباشرين. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1211]

```
1212:             val verified = peerManager.getVerifiedPeers()
```
> تعريف متغيّر ثابت verified يُسنَد إليه ناتج استدعاء getVerifiedPeers على مدير الأقران (peerManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1212]

```
1213:             val direct = verified.filter { it.value.isDirectConnection }.keys.toSet()
```
> تعريف متغيّر ثابت direct يُسنَد إليه نتيجة ترشيح (filter) verified للعناصر التي قيمتها تحمل isDirectConnection ثم أخذ مفاتيحها (keys) وتحويلها إلى مجموعة (toSet). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1213]

```
1214:             // Publish this transport's direct peers and gossip the cross-transport union so a
```
> تعليق: انشر الأقران المباشرين لهذا الناقل وأشِع اتحاد النواقل المتقاطعة كي… (جزء أول من تعليق). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1214]

```
1215:             // node connected via multiple transports advertises a complete neighbor list.
```
> تعليق: …عقدة متصلة عبر نواقل متعددة تُعلِن قائمة جيران كاملة (تتمّة التعليق). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1215]

```
1216:             try { com.bitchat.android.services.AppStateStore.setTransportDirectPeers("BLE", direct) } catch (_: Exception) { }
```
> كتلة محاولة (try) تستدعي على مخزن حالة التطبيق (AppStateStore) الدالة setTransportDirectPeers ممرّرةً السلسلة "BLE" والمجموعة direct، وكتلة التقاط لأي استثناء فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1216]

```
1217:             val union = try {
```
> تعريف متغيّر ثابت union يُسنَد إليه قيمة تعبير المحاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1217]

```
1218:                 com.bitchat.android.services.AppStateStore.getDirectPeers().ifEmpty { direct }
```
> تستدعي على مخزن حالة التطبيق الدالة getDirectPeers، وإن كان الناتج فارغاً (ifEmpty) فتُرجِع direct بدلاً عنه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1218]

```
1219:             } catch (_: Exception) { direct }
```
> كتلة التقاط لأي استثناء تُرجِع direct. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1219]

```
1220:             union.distinct().take(10)
```
> تطبّق على union إزالة المكرّر (distinct) ثم تأخذ أول ١٠ عناصر (take). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1220]

```
1221:         } catch (_: Exception) {
```
> كتلة التقاط لأي استثناء. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1221]

```
1222:             emptyList()
```
> تُرجِع قائمة فارغة (emptyList). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1222]

```
1223:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1223]

```
1224:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1224]

```
1225: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1225]

```
1226:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1226]

```
1227:      * Send leave announcement
```
> تعليق: أرسِل إعلان المغادرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1227]

```
1228:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1228]

```
1229:     private fun sendLeaveAnnouncement() {
```
> تعريف دالة خاصة باسم sendLeaveAnnouncement لا تأخذ وسائط ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1229]

```
1230:         val packet = BitchatPacket(
```
> تعريف متغيّر ثابت packet يُسنَد إليه كائن حزمة بِتشات (BitchatPacket) منشأ بالوسائط التالية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1230]

```
1231:             type = MessageType.LEAVE.value,
```
> ضبط الوسيط type على قيمة (value) عنصر LEAVE من تعداد نوع الرسالة (MessageType). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1231]

```
1232:             ttl = MAX_TTL,
```
> ضبط الوسيط ttl (مدة البقاء) على الثابت MAX_TTL. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1232]

```
1233:             senderID = myPeerID,
```
> ضبط الوسيط senderID على معرّف القرين الخاص بي (myPeerID). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1233]

```
1234:             payload = byteArrayOf()
```
> ضبط الوسيط payload (الحمولة) على مصفوفة بايتات فارغة (byteArrayOf). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1234]

```
1235:         )
```
> إغلاق قائمة وسائط المُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1235]

```
1236:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1236]

```
1237:         // Sign the packet before broadcasting
```
> تعليق: وقّع الحزمة قبل البثّ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1237]

```
1238:         val signedPacket = signPacketBeforeBroadcast(packet)
```
> تعريف متغيّر ثابت signedPacket يُسنَد إليه ناتج استدعاء signPacketBeforeBroadcast ممرّراً packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1238]

```
1239:         broadcastRoutedPacket(RoutedPacket(signedPacket))
```
> استدعاء broadcastRoutedPacket ممرّراً كائن حزمة موجَّهة (RoutedPacket) منشأ من signedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1239]

```
1240:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1240]

```
1241:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1241]

```
1242:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1242]

```
1243:      * Get peer nicknames
```
> تعليق: احصل على ألقاب الأقران. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1243]

```
1244:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1244]

```
1245:     fun getPeerNicknames(): Map<String, String> = peerManager.getAllPeerNicknames()
```
> تعريف دالة عامة باسم getPeerNicknames تعيد خريطة (Map) من سلسلة إلى سلسلة، جسمها تعبيري يساوي ناتج getAllPeerNicknames على مدير الأقران. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1245]

```
1246:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1246]

```
1247:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1247]

```
1248:      * Get peer RSSI values  
```
> تعليق: احصل على قيم قوة الإشارة المستقبَلة (RSSI) للأقران. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1248]

```
1249:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1249]

```
1250:     fun getPeerRSSI(): Map<String, Int> = peerManager.getAllPeerRSSI()
```
> تعريف دالة عامة باسم getPeerRSSI تعيد خريطة من سلسلة إلى عدد صحيح (Int)، جسمها تعبيري يساوي ناتج getAllPeerRSSI على مدير الأقران. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1250]

```
1251:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1251]

```
1252:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1252]

```
1253:      * Check if we have an established Noise session with a peer  
```
> تعليق: تحقّق إن كانت لدينا جلسة نويز (Noise) مُنشأة مع قرين. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1253]

```
1254:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1254]

```
1255:     fun hasEstablishedSession(peerID: String): Boolean {
```
> تعريف دالة عامة باسم hasEstablishedSession تأخذ معرّف قرين (peerID) من نوع سلسلة وتعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1255]

```
1256:         return encryptionService.hasEstablishedSession(peerID)
```
> تُرجِع ناتج استدعاء hasEstablishedSession على خدمة التشفير (encryptionService) ممرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1256]

```
1257:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1257]

```
1258:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1258]

```
1259:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1259]

```
1260:      * Get session state for a peer (for UI state display)
```
> تعليق: احصل على حالة الجلسة لقرين (لعرض حالة واجهة المستخدم). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1260]

```
1261:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1261]

```
1262:     fun getSessionState(peerID: String): com.bitchat.android.noise.NoiseSession.NoiseSessionState {
```
> تعريف دالة عامة باسم getSessionState تأخذ peerID من نوع سلسلة وتعيد حالة جلسة نويز (NoiseSession.NoiseSessionState). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1262]

```
1263:         return encryptionService.getSessionState(peerID)
```
> تُرجِع ناتج استدعاء getSessionState على خدمة التشفير ممرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1263]

```
1264:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1264]

```
1265:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1265]

```
1266:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1266]

```
1267:      * Initiate Noise handshake with a specific peer (public API)
```
> تعليق: ابدأ مصافحة نويز (handshake) مع قرين محدّد (واجهة برمجية عامة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1267]

```
1268:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1268]

```
1269:     fun initiateNoiseHandshake(peerID: String) {
```
> تعريف دالة عامة باسم initiateNoiseHandshake تأخذ peerID من نوع سلسلة ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1269]

```
1270:         // Delegate to the existing implementation in the MessageHandler delegate
```
> تعليق: فوّض إلى التطبيق الموجود في مفوَّض معالج الرسائل (MessageHandler delegate). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1270]

```
1271:         messageHandler.delegate?.initiateNoiseHandshake(peerID)
```
> استدعاء آمن من العدم على مفوَّض (delegate) معالج الرسائل (messageHandler) الدالة initiateNoiseHandshake ممرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1271]

```
1272:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1272]

```
1273:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1273]

```
1274:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1274]

```
1275:      * Get peer fingerprint for identity management
```
> تعليق: احصل على بصمة القرين (fingerprint) لأجل إدارة الهوية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1275]

```
1276:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1276]

```
1277:     fun getPeerFingerprint(peerID: String): String? {
```
> تعريف دالة عامة باسم getPeerFingerprint تأخذ peerID من نوع سلسلة وتعيد سلسلة قابلة للعدم (String?). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1277]

```
1278:         return peerManager.getFingerprintForPeer(peerID)
```
> تُرجِع ناتج استدعاء getFingerprintForPeer على مدير الأقران ممرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1278]

```
1279:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1279]

```
1280: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1280]

```
1281:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1281]

```
1282:      * Get current active peer count (for status/notifications)
```
> تعليق: احصل على عدد الأقران النشطين الحالي (للحالة/الإشعارات). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1282]

```
1283:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1283]

```
1284:     fun getActivePeerCount(): Int {
```
> تعريف دالة عامة باسم getActivePeerCount لا تأخذ وسائط وتعيد عدداً صحيحاً (Int). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1284]

```
1285:         return try { peerManager.getActivePeerCount() } catch (_: Exception) { 0 }
```
> تُرجِع قيمة تعبير محاولة (try) يستدعي getActivePeerCount على مدير الأقران، وكتلة التقاط لأي استثناء تُرجِع صفراً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1285]

```
1286:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1286]

```
1287: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1287]

```
1288:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1288]

```
1289:      * Get peer info for verification purposes
```
> تعليق: احصل على معلومات القرين لأغراض التحقّق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1289]

```
1290:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1290]

```
1291:     fun getPeerInfo(peerID: String): PeerInfo? {
```
> تعريف دالة عامة باسم getPeerInfo تأخذ peerID من نوع سلسلة وتعيد معلومات قرين (PeerInfo) قابلة للعدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1291]

```
1292:         return peerManager.getPeerInfo(peerID)
```
> تُرجِع ناتج استدعاء getPeerInfo على مدير الأقران ممرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1292]

```
1293:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1293]

```
1294: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1294]

```
1295:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1295]

```
1296:      * Update peer information with verification data
```
> تعليق: حدّث معلومات القرين ببيانات التحقّق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1296]

```
1297:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1297]

```
1298:     fun updatePeerInfo(
```
> تعريف دالة عامة باسم updatePeerInfo تبدأ قائمة وسائطها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1298]

```
1299:         peerID: String,
```
> الوسيط peerID من نوع سلسلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1299]

```
1300:         nickname: String,
```
> الوسيط nickname (اللقب) من نوع سلسلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1300]

```
1301:         noisePublicKey: ByteArray,
```
> الوسيط noisePublicKey (مفتاح نويز العام) من نوع مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1301]

```
1302:         signingPublicKey: ByteArray,
```
> الوسيط signingPublicKey (مفتاح التوقيع العام) من نوع مصفوفة بايتات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1302]

```
1303:         isVerified: Boolean
```
> الوسيط isVerified (هل مُتحقَّق منه) من نوع منطقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1303]

```
1304:     ): Boolean {
```
> إغلاق قائمة الوسائط، والدالة تعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1304]

```
1305:         return peerManager.updatePeerInfo(peerID, nickname, noisePublicKey, signingPublicKey, isVerified)
```
> تُرجِع ناتج استدعاء updatePeerInfo على مدير الأقران ممرّراً peerID وnickname وnoisePublicKey وsigningPublicKey وisVerified. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1305]

```
1306:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1306]

```
1307:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1307]

```
1308:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1308]

```
1309:      * Get our identity fingerprint
```
> تعليق: احصل على بصمة هويّتنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1309]

```
1310:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1310]

```
1311:     fun getIdentityFingerprint(): String {
```
> تعريف دالة عامة باسم getIdentityFingerprint لا تأخذ وسائط وتعيد سلسلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1311]

```
1312:         return encryptionService.getIdentityFingerprint()
```
> تُرجِع ناتج استدعاء getIdentityFingerprint على خدمة التشفير. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1312]

```
1313:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1313]

```
1314: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1314]

```
1315:     fun getStaticNoisePublicKey(): ByteArray? {
```
> تعريف دالة عامة باسم getStaticNoisePublicKey لا تأخذ وسائط وتعيد مصفوفة بايتات قابلة للعدم (ByteArray?). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1315]

```
1316:         return encryptionService.getStaticPublicKey()
```
> تُرجِع ناتج استدعاء getStaticPublicKey على خدمة التشفير. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1316]

```
1317:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1317]

```
1318:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1318]

```
1319:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1319]

```
1320:      * Check if encryption icon should be shown for a peer
```
> تعليق: تحقّق إن كان ينبغي إظهار أيقونة التشفير لقرين. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1320]

```
1321:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1321]

```
1322:     fun shouldShowEncryptionIcon(peerID: String): Boolean {
```
> تعريف دالة عامة باسم shouldShowEncryptionIcon تأخذ peerID من نوع سلسلة وتعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1322]

```
1323:         return encryptionService.hasEstablishedSession(peerID)
```
> تُرجِع ناتج استدعاء hasEstablishedSession على خدمة التشفير ممرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1323]

```
1324:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1324]

```
1325:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1325]

```
1326:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1326]

```
1327:      * Get all peers with established encrypted sessions
```
> تعليق: احصل على كل الأقران ذوي الجلسات المشفّرة المُنشأة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1327]

```
1328:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1328]

```
1329:     fun getEncryptedPeers(): List<String> {
```
> تعريف دالة عامة باسم getEncryptedPeers لا تأخذ وسائط وتعيد قائمة من سلاسل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1329]

```
1330:         // SIMPLIFIED: Return empty list for now since we don't have direct access to sessionManager
```
> تعليق: مُبسَّط — أرجِع قائمة فارغة حالياً لأننا لا نملك وصولاً مباشراً إلى مدير الجلسات (sessionManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1330]

```
1331:         // This method is not critical for the session retention fix
```
> تعليق: هذه الدالة ليست حرجة لإصلاح الاحتفاظ بالجلسة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1331]

```
1332:         return emptyList()
```
> تُرجِع قائمة فارغة (emptyList). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1332]

```
1333:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1333]

```
1334:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1334]

```
1335:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1335]

```
1336:      * Get device address for a specific peer ID
```
> تعليق: احصل على عنوان الجهاز لمعرّف قرين محدّد. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1336]

```
1337:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1337]

```
1338:     fun getDeviceAddressForPeer(peerID: String): String? {
```
> تعريف دالة عامة باسم getDeviceAddressForPeer تأخذ peerID من نوع سلسلة وتعيد سلسلة قابلة للعدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1338]

```
1339:         return connectionManager.addressPeerMap.entries.find { it.value == peerID }?.key
```
> تُرجِع مفتاح (key) أول مُدخَل في خريطة عنوان-قرين (addressPeerMap) لمدير الاتصال (connectionManager) تساوي قيمته peerID، عبر find واستدعاء آمن من العدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1339]

```
1340:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1340]

```
1341:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1341]

```
1342:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1342]

```
1343:      * Get all device addresses mapped to their peer IDs
```
> تعليق: احصل على كل عناوين الأجهزة المربوطة بمعرّفات أقرانها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1343]

```
1344:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1344]

```
1345:     fun getDeviceAddressToPeerMapping(): Map<String, String> {
```
> تعريف دالة عامة باسم getDeviceAddressToPeerMapping لا تأخذ وسائط وتعيد خريطة من سلسلة إلى سلسلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1345]

```
1346:         return connectionManager.addressPeerMap.toMap()
```
> تُرجِع نسخة خريطة (toMap) من خريطة عنوان-قرين لمدير الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1346]

```
1347:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1347]

```
1348:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1348]

```
1349:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1349]

```
1350:      * Print device addresses for all connected peers
```
> تعليق: اطبع عناوين الأجهزة لكل الأقران المتصلين. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1350]

```
1351:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1351]

```
1352:     fun printDeviceAddressesForPeers(): String {
```
> تعريف دالة عامة باسم printDeviceAddressesForPeers لا تأخذ وسائط وتعيد سلسلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1352]

```
1353:         return peerManager.getDebugInfoWithDeviceAddresses(connectionManager.addressPeerMap)
```
> تُرجِع ناتج استدعاء getDebugInfoWithDeviceAddresses على مدير الأقران ممرّراً خريطة عنوان-قرين لمدير الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1353]

```
1354:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1354]

```
1355: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1355]

```
1356:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1356]

```
1357:      * Get debug status information
```
> تعليق: احصل على معلومات حالة التنقيح (debug). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1357]

```
1358:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1358]

```
1359:     fun getDebugStatus(): String {
```
> تعريف دالة عامة باسم getDebugStatus لا تأخذ وسائط وتعيد سلسلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1359]

```
1360:         return buildString {
```
> تُرجِع نتيجة بناء سلسلة (buildString) ضمن الكتلة التالية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1360]

```
1361:             appendLine("=== Bluetooth Mesh Service Debug Status ===")
```
> تستدعي appendLine لإلحاق السطر النصي "=== Bluetooth Mesh Service Debug Status ===". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1361]

```
1362:             appendLine("My Peer ID: $myPeerID")
```
> تستدعي appendLine لإلحاق سطر يحوي "My Peer ID: " متبوعاً بقيمة myPeerID المُدرَجة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1362]

```
1363:             appendLine()
```
> تستدعي appendLine دون وسيط لإلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1363]

```
1364:             appendLine(connectionManager.getDebugInfo())
```
> تستدعي appendLine لإلحاق ناتج getDebugInfo على مدير الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1364]

```
1365:             appendLine()
```
> تستدعي appendLine دون وسيط لإلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1365]

```
1366:             appendLine(peerManager.getDebugInfo(connectionManager.addressPeerMap))
```
> تستدعي appendLine لإلحاق ناتج getDebugInfo على مدير الأقران ممرّراً خريطة عنوان-قرين لمدير الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1366]

```
1367:             appendLine()
```
> تستدعي appendLine دون وسيط لإلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1367]

```
1368:             appendLine(peerManager.getFingerprintDebugInfo())
```
> تستدعي appendLine لإلحاق ناتج getFingerprintDebugInfo على مدير الأقران. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1368]

```
1369:             appendLine()
```
> تستدعي appendLine دون وسيط لإلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1369]

```
1370:             appendLine(fragmentManager.getDebugInfo())
```
> تستدعي appendLine لإلحاق ناتج getDebugInfo على مدير التجزئة (fragmentManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1370]

```
1371:             appendLine()
```
> تستدعي appendLine دون وسيط لإلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1371]

```
1372:             appendLine(securityManager.getDebugInfo())
```
> تستدعي appendLine لإلحاق ناتج getDebugInfo على مدير الأمان (securityManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1372]

```
1373:             appendLine()
```
> تستدعي appendLine دون وسيط لإلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1373]

```
1374:             appendLine(storeForwardManager.getDebugInfo())
```
> تستدعي appendLine لإلحاق ناتج getDebugInfo على مدير التخزين والتمرير (storeForwardManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1374]

```
1375:             appendLine()
```
> تستدعي appendLine دون وسيط لإلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1375]

```
1376:             appendLine(messageHandler.getDebugInfo())
```
> تستدعي appendLine لإلحاق ناتج getDebugInfo على معالج الرسائل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1376]

```
1377:             appendLine()
```
> تستدعي appendLine دون وسيط لإلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1377]

```
1378:             appendLine(packetProcessor.getDebugInfo())
```
> تستدعي appendLine لإلحاق ناتج getDebugInfo على معالج الحزم (packetProcessor). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1378]

```
1379:         }
```
> إغلاق نطاق كتلة بناء السلسلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1379]

```
1380:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1380]

```
1381:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1381]

```
1382:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1382]

```
1383:      * Convert hex string peer ID to binary data (8 bytes) - exactly same as iOS
```
> تعليق: حوّل معرّف القرين بصيغة سلسلة سداسية عشرية (hex) إلى بيانات ثنائية (٨ بايتات) — مطابق تماماً لنظام iOS. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1383]

```
1384:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1384]

```
1385:     private fun hexStringToByteArray(hexString: String): ByteArray {
```
> تعريف دالة خاصة باسم hexStringToByteArray تأخذ سلسلة سداسية عشرية (hexString) وتعيد مصفوفة بايتات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1385]

```
1386:         val result = ByteArray(8) { 0 } // Initialize with zeros, exactly 8 bytes
```
> تعريف متغيّر ثابت result يُسنَد إليه مصفوفة بايتات بطول ٨ مُهيّأة كل عناصرها بصفر؛ وتعليق: تهيئة بالأصفار، ٨ بايتات بالضبط. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1386]

```
1387:         var tempID = hexString
```
> تعريف متغيّر متغيّر القيمة (var) tempID يُسنَد إليه hexString. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1387]

```
1388:         var index = 0
```
> تعريف متغيّر متغيّر القيمة index يُسنَد إليه صفر. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1388]

```
1389:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1389]

```
1390:         while (tempID.length >= 2 && index < 8) {
```
> حلقة طالما (while) تستمرّ ما دام طول tempID لا يقلّ عن ٢ وindex أقل من ٨. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1390]

```
1391:             val hexByte = tempID.substring(0, 2)
```
> تعريف متغيّر ثابت hexByte يُسنَد إليه الجزء الفرعي (substring) من tempID من الموضع ٠ حتى ٢. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1391]

```
1392:             val byte = hexByte.toIntOrNull(16)?.toByte()
```
> تعريف متغيّر ثابت byte يُسنَد إليه تحويل hexByte إلى عدد صحيح بالأساس ١٦ (toIntOrNull) أو عدم، ثم تحويله إلى بايت (toByte) عبر استدعاء آمن من العدم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1392]

```
1393:             if (byte != null) {
```
> شرط إن (if) يتحقّق إذا لم يكن byte عدماً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1393]

```
1394:                 result[index] = byte
```
> إسناد byte إلى عنصر result عند الموضع index. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1394]

```
1395:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1395]

```
1396:             tempID = tempID.substring(2)
```
> إعادة إسناد tempID إلى الجزء الفرعي منه ابتداءً من الموضع ٢. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1396]

```
1397:             index++
```
> زيادة index بمقدار واحد. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1397]

```
1398:         }
```
> إغلاق نطاق حلقة الطالما. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1398]

```
1399:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1399]

```
1400:         return result
```
> تُرجِع result. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1400]
