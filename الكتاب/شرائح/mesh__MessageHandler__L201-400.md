# شريحة — app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt (الأسطر 201–400)

```
201:                     timestamp = System.currentTimeMillis().toULong(),
```
> يضبط معامل الطابع الزمني (timestamp) على قيمة الوقت الحالي بالمللي ثانية من النظام محوّلة إلى عدد صحيح موجب طويل (toULong). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:201]

```
202:                     payload = encryptedPayload,
```
> يضبط معامل الحمولة (payload) على قيمة الحمولة المشفّرة (encryptedPayload). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:202]

```
203:                     signature = null,
```
> يضبط معامل التوقيع (signature) على القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:203]

```
204:                     ttl = com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS // Same TTL as iOS messageTTL
```
> يضبط معامل مدة البقاء (ttl) على الثابت MESSAGE_TTL_HOPS من الصنف AppConstants، مع تعليق: «نفس مدة البقاء كما في messageTTL على iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:204]

```
205:                 )
```
> إغلاق نطاق (إغلاق قوس استدعاء بناء الحزمة). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:205]

```
206:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:206]

```
207:             delegate?.sendPacket(packet)
```
> يستدعي الدالة sendPacket على المفوّض (delegate) إن لم يكن فارغاً، مُمرّراً الحزمة (packet). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:207]

```
208:             Log.d(TAG, "📤 Sent delivery ACK to $senderPeerID for message $messageID")
```
> يسجّل رسالة تنقيح (Log.d) بالوسم TAG نصّها: «تم إرسال إقرار التسليم إلى senderPeerID للرسالة messageID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:208]

```
209:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:209]

```
210:         } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) باسم e ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:210]

```
211:             Log.e(TAG, "Failed to send delivery ACK to $senderPeerID: ${e.message}")
```
> يسجّل رسالة خطأ (Log.e) بالوسم TAG نصّها: «فشل إرسال إقرار التسليم إلى senderPeerID» متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:211]

```
212:         }
```
> إغلاق نطاق (إغلاق كتلة catch). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:212]

```
213:     }
```
> إغلاق نطاق (إغلاق الدالة). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:213]

```
214:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:214]

```
215:     /**
```
> تعليق توثيقي: بداية تعليق توثيقي (/**). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:215]

```
216:      * Handle announce message with TLV decoding and signature verification - exactly like iOS
```
> تعليق: «معالجة رسالة الإعلان مع فكّ ترميز TLV والتحقق من التوقيع - تماماً مثل iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:216]

```
217:      */
```
> تعليق توثيقي: نهاية التعليق التوثيقي (*/). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:217]

```
218:     suspend fun handleAnnounce(routed: RoutedPacket): Boolean {
```
> يعرّف دالة معلّقة (suspend) باسم handleAnnounce تأخذ وسيطاً routed من نوع RoutedPacket وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:218]

```
219:         val packet = routed.packet
```
> يعرّف ثابتاً (val) باسم packet ويسنده إلى الخاصية packet من الوسيط routed. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:219]

```
220:         val peerID = routed.peerID ?: "unknown"
```
> يعرّف ثابتاً باسم peerID ويسنده إلى الخاصية peerID من routed، وإن كانت فارغة فيسند السلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:220]

```
221: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:221]

```
222:         if (peerID == myPeerID) return false
```
> إذا كان peerID يساوي myPeerID فيُعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:222]

```
223: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:223]

```
224:         // Peers use wall-clock packet timestamps; tolerate moderate device clock skew
```
> تعليق: «الأقران يستعملون طوابع الحزمة الزمنية لساعة الحائط؛ تسامُح مع انحراف معتدل في ساعة الجهاز». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:224]

```
225:         // during identity learning, or later signed messages cannot be verified.
```
> تعليق: «أثناء تعلّم الهوية، وإلا فالرسائل الموقّعة لاحقاً لا يمكن التحقق منها». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:225]

```
226:         val now = System.currentTimeMillis()
```
> يعرّف ثابتاً باسم now ويسنده إلى الوقت الحالي بالمللي ثانية من النظام (System.currentTimeMillis). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:226]

```
227:         val clockSkewMs = kotlin.math.abs(now - packet.timestamp.toLong())
```
> يعرّف ثابتاً باسم clockSkewMs (انحراف الساعة بالمللي ثانية) ويسنده إلى القيمة المطلقة (abs) للفرق بين now وطابع الحزمة الزمني محوّلاً إلى عدد طويل (toLong). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:227]

```
228:         if (clockSkewMs > ANNOUNCE_CLOCK_SKEW_TOLERANCE_MS) {
```
> إذا كان clockSkewMs أكبر من الثابت ANNOUNCE_CLOCK_SKEW_TOLERANCE_MS فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:228]

```
229:             Log.w(TAG, "Ignoring ANNOUNCE from ${peerID.take(8)} with excessive clock skew (${clockSkewMs}ms > ${ANNOUNCE_CLOCK_SKEW_TOLERANCE_MS}ms)")
```
> يسجّل رسالة تحذير (Log.w) بالوسم TAG نصّها: «تجاهل ANNOUNCE من أول ثمانية محارف من peerID مع انحراف ساعة مفرط (clockSkewMs مللي ثانية > الثابت مللي ثانية)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:229]

```
230:             return false
```
> يُعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:230]

```
231:         } else if (clockSkewMs > com.bitchat.android.util.AppConstants.Mesh.STALE_PEER_TIMEOUT_MS) {
```
> وإلا إذا كان clockSkewMs أكبر من الثابت STALE_PEER_TIMEOUT_MS من AppConstants.Mesh فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:231]

```
232:             Log.w(TAG, "Accepting ANNOUNCE from ${peerID.take(8)} within clock skew tolerance (${clockSkewMs}ms)")
```
> يسجّل رسالة تحذير بالوسم TAG نصّها: «قبول ANNOUNCE من أول ثمانية محارف من peerID ضمن تسامُح انحراف الساعة (clockSkewMs مللي ثانية)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:232]

```
233:         }
```
> إغلاق نطاق (إغلاق كتلة else if). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:233]

```
234:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:234]

```
235:         // Try to decode as iOS-compatible IdentityAnnouncement with TLV format
```
> تعليق: «محاولة فكّ الترميز كإعلان هوية (IdentityAnnouncement) متوافق مع iOS بصيغة TLV». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:235]

```
236:         val announcement = IdentityAnnouncement.decode(packet.payload)
```
> يعرّف ثابتاً باسم announcement ويسنده إلى نتيجة استدعاء الدالة decode على IdentityAnnouncement مُمرّراً حمولة الحزمة (packet.payload). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:236]

```
237:         if (announcement == null) {
```
> إذا كان announcement فارغاً (null) فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:237]

```
238:             Log.w(TAG, "Failed to decode announce from $peerID as iOS-compatible TLV format")
```
> يسجّل رسالة تحذير بالوسم TAG نصّها: «فشل فكّ ترميز الإعلان من peerID بصيغة TLV المتوافقة مع iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:238]

```
239:             return false
```
> يُعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:239]

```
240:         }
```
> إغلاق نطاق (إغلاق كتلة if). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:240]

```
241:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:241]

```
242:         // Verify packet signature using the announced signing public key
```
> تعليق: «التحقق من توقيع الحزمة باستعمال مفتاح التوقيع العام المُعلَن». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:242]

```
243:         var verified = false
```
> يعرّف متغيّراً (var) باسم verified ويسنده إلى القيمة false. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:243]

```
244:         if (packet.signature != null) {
```
> إذا كان توقيع الحزمة (packet.signature) غير فارغ فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:244]

```
245:             // Verify that the packet was signed by the signing private key corresponding to the announced signing public key
```
> تعليق: «التحقق من أن الحزمة وُقّعت بمفتاح التوقيع الخاص المقابل لمفتاح التوقيع العام المُعلَن». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:245]

```
246:             verified = delegate?.verifyEd25519Signature(packet.signature!!, packet.toBinaryDataForSigning()!!, announcement.signingPublicKey) ?: false
```
> يسند إلى verified نتيجة استدعاء verifyEd25519Signature على المفوّض مُمرّراً توقيع الحزمة (مع تأكيد عدم الفراغ !!) والبيانات الثنائية للتوقيع (toBinaryDataForSigning مع تأكيد عدم الفراغ) ومفتاح التوقيع العام من announcement، وإن كانت النتيجة فارغة فيسند false. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:246]

```
247:             if (!verified) {
```
> إذا كان verified غير صحيح (نفي) فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:247]

```
248:                 Log.w(TAG, "⚠️ Signature verification for announce failed ${peerID.take(8)}")
```
> يسجّل رسالة تحذير بالوسم TAG نصّها: «فشل التحقق من توقيع الإعلان لأول ثمانية محارف من peerID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:248]

```
249:             }
```
> إغلاق نطاق (إغلاق كتلة if الداخلية). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:249]

```
250:         }
```
> إغلاق نطاق (إغلاق كتلة if للتوقيع). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:250]

```
251: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:251]

```
252:         // Check for existing peer with different noise public key
```
> تعليق: «التحقق من وجود قرين قائم بمفتاح Noise عام مختلف». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:252]

```
253:         // If existing peer has a different noise public key, do not consider this verified
```
> تعليق: «إذا كان للقرين القائم مفتاح Noise عام مختلف، فلا يُعتبر هذا مُتحقَّقاً منه». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:253]

```
254:         val existingPeer = delegate?.getPeerInfo(peerID)
```
> يعرّف ثابتاً باسم existingPeer ويسنده إلى نتيجة استدعاء getPeerInfo على المفوّض مُمرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:254]

```
255:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:255]

```
256:         if (existingPeer != null && existingPeer.noisePublicKey != null && !existingPeer.noisePublicKey!!.contentEquals(announcement.noisePublicKey)) {
```
> إذا كان existingPeer غير فارغ ومفتاح Noise العام له غير فارغ ولم يساوِ محتواه (contentEquals مع النفي) مفتاح Noise العام من announcement فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:256]

```
257:             Log.w(TAG, "⚠️ Announce key mismatch for ${peerID.take(8)}... — keeping unverified")
```
> يسجّل رسالة تحذير بالوسم TAG نصّها: «عدم تطابق مفتاح الإعلان لأول ثمانية محارف من peerID... — الإبقاء غير مُتحقَّق منه». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:257]

```
258:             verified = false
```
> يسند إلى verified القيمة false. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:258]

```
259:         }
```
> إغلاق نطاق (إغلاق كتلة if عدم التطابق). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:259]

```
260: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:260]

```
261:         // Require verified announce; ignore otherwise (no backward compatibility)
```
> تعليق: «اشتراط إعلان مُتحقَّق منه؛ التجاهل خلاف ذلك (لا توافق رجعي)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:261]

```
262:         if (!verified) {
```
> إذا كان verified غير صحيح (نفي) فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:262]

```
263:             Log.w(TAG, "❌ Ignoring unverified announce from ${peerID.take(8)}...")
```
> يسجّل رسالة تحذير بالوسم TAG نصّها: «تجاهل إعلان غير مُتحقَّق منه من أول ثمانية محارف من peerID...». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:263]

```
264:             return false
```
> يُعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:264]

```
265:         }
```
> إغلاق نطاق (إغلاق كتلة if). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:265]

```
266:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:266]

```
267:         // Successfully decoded TLV format exactly like iOS
```
> تعليق: «تم فكّ ترميز صيغة TLV بنجاح تماماً مثل iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:267]

```
268:         Log.d(TAG, "✅ Verified announce from $peerID: nickname=${announcement.nickname}, " +
```
> يسجّل رسالة تنقيح بالوسم TAG نصّها: «إعلان مُتحقَّق منه من peerID: الاسم المستعار = announcement.nickname،» متبوعاً بعملية ضمّ سلاسل (+). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:268]

```
269:                 "noisePublicKey=${announcement.noisePublicKey.joinToString("") { "%02x".format(it) }.take(16)}..., " +
```
> يتابع تكوين رسالة التسجيل بسلسلة: «noisePublicKey =» قيمة مفتاح Noise العام مُحوّلة إلى نص ست عشري (كل بايت بصيغة %02x) مضموماً بلا فاصل، مأخوذاً منه أول ستة عشر محرفاً، متبوعاً بعملية ضمّ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:269]

```
270:                 "signingPublicKey=${announcement.signingPublicKey.joinToString("") { "%02x".format(it) }.take(16)}...")
```
> يتابع تكوين رسالة التسجيل بسلسلة: «signingPublicKey =» قيمة مفتاح التوقيع العام مُحوّلة إلى نص ست عشري (كل بايت بصيغة %02x) مضموماً بلا فاصل، مأخوذاً منه أول ستة عشر محرفاً، وينهي الاستدعاء. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:270]

```
271:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:271]

```
272:         // Extract nickname and public keys from TLV data
```
> تعليق: «استخراج الاسم المستعار والمفاتيح العامة من بيانات TLV». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:272]

```
273:         val nickname = announcement.nickname
```
> يعرّف ثابتاً باسم nickname ويسنده إلى الخاصية nickname من announcement. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:273]

```
274:         val noisePublicKey = announcement.noisePublicKey
```
> يعرّف ثابتاً باسم noisePublicKey ويسنده إلى الخاصية noisePublicKey من announcement. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:274]

```
275:         val signingPublicKey = announcement.signingPublicKey
```
> يعرّف ثابتاً باسم signingPublicKey ويسنده إلى الخاصية signingPublicKey من announcement. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:275]

```
276:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:276]

```
277:         // Update peer info with verification status through new method
```
> تعليق: «تحديث معلومات القرين بحالة التحقق عبر الدالة الجديدة». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:277]

```
278:         val isFirstAnnounce = delegate?.updatePeerInfo(
```
> يعرّف ثابتاً باسم isFirstAnnounce ويسنده إلى نتيجة استدعاء updatePeerInfo على المفوّض (بداية الاستدعاء). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:278]

```
279:             peerID = peerID,
```
> يضبط معامل peerID على قيمة الثابت peerID. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:279]

```
280:             nickname = nickname,
```
> يضبط معامل nickname على قيمة الثابت nickname. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:280]

```
281:             noisePublicKey = noisePublicKey,
```
> يضبط معامل noisePublicKey على قيمة الثابت noisePublicKey. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:281]

```
282:             signingPublicKey = signingPublicKey,
```
> يضبط معامل signingPublicKey على قيمة الثابت signingPublicKey. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:282]

```
283:             isVerified = true
```
> يضبط معامل isVerified على القيمة true. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:283]

```
284:         ) ?: false
```
> يغلق استدعاء updatePeerInfo، وإن كانت نتيجته فارغة فيسند false. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:284]

```
285: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:285]

```
286:         // Update peer ID binding with noise public key for identity management
```
> تعليق: «تحديث ربط معرّف القرين بمفتاح Noise العام لإدارة الهوية». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:286]

```
287:         delegate?.updatePeerIDBinding(
```
> يستدعي الدالة updatePeerIDBinding على المفوّض إن لم يكن فارغاً (بداية الاستدعاء). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:287]

```
288:             newPeerID = peerID,
```
> يضبط معامل newPeerID على قيمة الثابت peerID. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:288]

```
289:             nickname = nickname,
```
> يضبط معامل nickname على قيمة الثابت nickname. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:289]

```
290:             publicKey = noisePublicKey,
```
> يضبط معامل publicKey على قيمة الثابت noisePublicKey. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:290]

```
291:             previousPeerID = null
```
> يضبط معامل previousPeerID على القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:291]

```
292:         )
```
> إغلاق نطاق (إغلاق استدعاء updatePeerIDBinding). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:292]

```
293:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:293]

```
294:         // Update mesh graph from gossip neighbors (only if TLV present)
```
> تعليق: «تحديث رسم الشبكة من جيران القيل والقال (gossip) (فقط إن وُجد TLV)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:294]

```
295:         try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:295]

```
296:             val neighborsOrNull = com.bitchat.android.services.meshgraph.GossipTLV.decodeNeighborsFromAnnouncementPayload(packet.payload)
```
> يعرّف ثابتاً باسم neighborsOrNull ويسنده إلى نتيجة استدعاء decodeNeighborsFromAnnouncementPayload على GossipTLV مُمرّراً حمولة الحزمة (packet.payload). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:296]

```
297:             com.bitchat.android.services.meshgraph.MeshGraphService.getInstance()
```
> يستدعي الدالة getInstance على MeshGraphService للحصول على المثيل الوحيد (بداية سلسلة استدعاءات). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:297]

```
298:                 .updateFromAnnouncement(peerID, nickname, neighborsOrNull, packet.timestamp)
```
> يستدعي على المثيل الدالة updateFromAnnouncement مُمرّراً peerID وnickname وneighborsOrNull وطابع الحزمة الزمني (packet.timestamp). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:298]

```
299:         } catch (_: Exception) { }
```
> يلتقط استثناءً (Exception) دون تسميته (_) ويترك كتلة المعالجة فارغة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:299]

```
300: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:300]

```
301:         Log.d(TAG, "✅ Processed verified TLV announce: stored identity for $peerID")
```
> يسجّل رسالة تنقيح بالوسم TAG نصّها: «تمت معالجة إعلان TLV مُتحقَّق منه: خُزّنت الهوية لـ peerID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:301]

```
302:         return isFirstAnnounce
```
> يُعيد قيمة الثابت isFirstAnnounce. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:302]

```
303:     }
```
> إغلاق نطاق (إغلاق دالة handleAnnounce). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:303]

```
304:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:304]

```
305:     /**
```
> تعليق توثيقي: بداية تعليق توثيقي (/**). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:305]

```
306:      * Handle Noise handshake - SIMPLIFIED iOS-compatible version
```
> تعليق: «معالجة مصافحة Noise - نسخة مبسّطة متوافقة مع iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:306]

```
307:      * Single handshake type (0x10) with response determined by payload analysis
```
> تعليق: «نوع مصافحة واحد (0x10) مع تحديد الردّ بتحليل الحمولة». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:307]

```
308:      */
```
> تعليق توثيقي: نهاية التعليق التوثيقي (*/). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:308]

```
309:     suspend fun handleNoiseHandshake(routed: RoutedPacket) {
```
> يعرّف دالة معلّقة (suspend) باسم handleNoiseHandshake تأخذ وسيطاً routed من نوع RoutedPacket دون قيمة معادة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:309]

```
310:         val packet = routed.packet
```
> يعرّف ثابتاً باسم packet ويسنده إلى الخاصية packet من routed. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:310]

```
311:         val peerID = routed.peerID ?: "unknown"
```
> يعرّف ثابتاً باسم peerID ويسنده إلى الخاصية peerID من routed، وإن كانت فارغة فيسند السلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:311]

```
312:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:312]

```
313:         Log.d(TAG, "Processing Noise handshake from $peerID (${packet.payload.size} bytes)")
```
> يسجّل رسالة تنقيح بالوسم TAG نصّها: «معالجة مصافحة Noise من peerID (حجم حمولة الحزمة بايت)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:313]

```
314:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:314]

```
315:         // Skip our own handshake messages
```
> تعليق: «تخطّي رسائل مصافحتنا الخاصة». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:315]

```
316:         if (peerID == myPeerID) return
```
> إذا كان peerID يساوي myPeerID فيُعيد (return) دون قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:316]

```
317:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:317]

```
318:         // Check if handshake is addressed to us
```
> تعليق: «التحقق إن كانت المصافحة موجّهة إلينا». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:318]

```
319:         val recipientID = packet.recipientID?.toHexString()
```
> يعرّف ثابتاً باسم recipientID ويسنده إلى معرّف المستلِم من الحزمة (packet.recipientID) محوّلاً إلى نص ست عشري (toHexString) إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:319]

```
320:         if (recipientID != myPeerID) {
```
> إذا كان recipientID لا يساوي myPeerID فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:320]

```
321:             Log.d(TAG, "Handshake not for me (for $recipientID, I am $myPeerID)")
```
> يسجّل رسالة تنقيح بالوسم TAG نصّها: «المصافحة ليست لي (لـ recipientID، وأنا myPeerID)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:321]

```
322:             return
```
> يُعيد (return) دون قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:322]

```
323:         }
```
> إغلاق نطاق (إغلاق كتلة if). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:323]

```
324:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:324]

```
325:         try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:325]

```
326:             // Process handshake message through delegate (simplified approach)
```
> تعليق: «معالجة رسالة المصافحة عبر المفوّض (نهج مبسّط)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:326]

```
327:             val response = delegate?.processNoiseHandshakeMessage(packet.payload, peerID)
```
> يعرّف ثابتاً باسم response ويسنده إلى نتيجة استدعاء processNoiseHandshakeMessage على المفوّض مُمرّراً حمولة الحزمة وpeerID. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:327]

```
328:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:328]

```
329:             if (response != null) {
```
> إذا كان response غير فارغ فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:329]

```
330:                 Log.d(TAG, "Generated handshake response for $peerID (${response.size} bytes)")
```
> يسجّل رسالة تنقيح بالوسم TAG نصّها: «تم توليد ردّ مصافحة لـ peerID (حجم الردّ بايت)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:330]

```
331:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:331]

```
332:                 // Send response using same packet type (simplified iOS approach)
```
> تعليق: «إرسال الردّ باستعمال نفس نوع الحزمة (نهج iOS المبسّط)». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:332]

```
333:                 val responsePacket = BitchatPacket(
```
> يعرّف ثابتاً باسم responsePacket ويسنده إلى مثيل جديد من BitchatPacket (بداية الاستدعاء البنائي). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:333]

```
334:                     version = 1u,
```
> يضبط معامل version على القيمة 1 كعدد صحيح موجب (1u). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:334]

```
335:                     type = MessageType.NOISE_HANDSHAKE.value,
```
> يضبط معامل type على قيمة العنصر NOISE_HANDSHAKE من التعداد MessageType (الخاصية value). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:335]

```
336:                     senderID = hexStringToByteArray(myPeerID),
```
> يضبط معامل senderID على نتيجة تحويل myPeerID من نص ست عشري إلى مصفوفة بايت (hexStringToByteArray). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:336]

```
337:                     recipientID = hexStringToByteArray(peerID),
```
> يضبط معامل recipientID على نتيجة تحويل peerID من نص ست عشري إلى مصفوفة بايت (hexStringToByteArray). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:337]

```
338:                     timestamp = System.currentTimeMillis().toULong(),
```
> يضبط معامل timestamp على الوقت الحالي بالمللي ثانية من النظام محوّلاً إلى عدد صحيح موجب طويل (toULong). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:338]

```
339:                     payload = response,
```
> يضبط معامل payload على قيمة الثابت response. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:339]

```
340:                     signature = null,
```
> يضبط معامل signature على القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:340]

```
341:                     ttl = com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS // Same TTL as iOS
```
> يضبط معامل ttl على الثابت MESSAGE_TTL_HOPS من AppConstants، مع تعليق: «نفس مدة البقاء كما في iOS». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:341]

```
342:                 )
```
> إغلاق نطاق (إغلاق الاستدعاء البنائي لـ BitchatPacket). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:342]

```
343:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:343]

```
344:                 delegate?.sendPacket(responsePacket)
```
> يستدعي الدالة sendPacket على المفوّض إن لم يكن فارغاً مُمرّراً responsePacket. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:344]

```
345:                 Log.d(TAG, "📤 Sent handshake response to $peerID")
```
> يسجّل رسالة تنقيح بالوسم TAG نصّها: «تم إرسال ردّ المصافحة إلى peerID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:345]

```
346:             }
```
> إغلاق نطاق (إغلاق كتلة if للردّ). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:346]

```
347:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:347]

```
348:             // Check if session is now established
```
> تعليق: «التحقق إن أُنشئت الجلسة الآن». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:348]

```
349:             val hasSession = delegate?.hasNoiseSession(peerID) ?: false
```
> يعرّف ثابتاً باسم hasSession ويسنده إلى نتيجة استدعاء hasNoiseSession على المفوّض مُمرّراً peerID، وإن كانت فارغة فيسند false. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:349]

```
350:             if (hasSession) {
```
> إذا كان hasSession صحيحاً فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:350]

```
351:                 Log.d(TAG, "✅ Noise session established with $peerID")
```
> يسجّل رسالة تنقيح بالوسم TAG نصّها: «أُنشئت جلسة Noise مع peerID». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:351]

```
352:             }
```
> إغلاق نطاق (إغلاق كتلة if للجلسة). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:352]

```
353:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:353]

```
354:         } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) باسم e ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:354]

```
355:             Log.e(TAG, "Failed to process Noise handshake from $peerID: ${e.message}")
```
> يسجّل رسالة خطأ بالوسم TAG نصّها: «فشل معالجة مصافحة Noise من peerID» متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:355]

```
356:         }
```
> إغلاق نطاق (إغلاق كتلة catch). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:356]

```
357:     }
```
> إغلاق نطاق (إغلاق دالة handleNoiseHandshake). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:357]

```
358:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:358]

```
359:     /**
```
> تعليق توثيقي: بداية تعليق توثيقي (/**). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:359]

```
360:      * Handle broadcast or private message
```
> تعليق: «معالجة رسالة بثّ أو رسالة خاصة». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:360]

```
361:      */
```
> تعليق توثيقي: نهاية التعليق التوثيقي (*/). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:361]

```
362:     suspend fun handleMessage(routed: RoutedPacket) {
```
> يعرّف دالة معلّقة (suspend) باسم handleMessage تأخذ وسيطاً routed من نوع RoutedPacket دون قيمة معادة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:362]

```
363:         val packet = routed.packet
```
> يعرّف ثابتاً باسم packet ويسنده إلى الخاصية packet من routed. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:363]

```
364:         val peerID = routed.peerID ?: "unknown"
```
> يعرّف ثابتاً باسم peerID ويسنده إلى الخاصية peerID من routed، وإن كانت فارغة فيسند السلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:364]

```
365:         if (peerID == myPeerID) return
```
> إذا كان peerID يساوي myPeerID فيُعيد (return) دون قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:365]

```
366:         val senderNickname = delegate?.getPeerNickname(peerID)
```
> يعرّف ثابتاً باسم senderNickname ويسنده إلى نتيجة استدعاء getPeerNickname على المفوّض مُمرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:366]

```
367:         if (senderNickname != null) {
```
> إذا كان senderNickname غير فارغ فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:367]

```
368:             Log.d(TAG, "Received message from $senderNickname")
```
> يسجّل رسالة تنقيح بالوسم TAG نصّها: «استُلمت رسالة من senderNickname». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:368]

```
369:             delegate?.updatePeerNickname(peerID, senderNickname)
```
> يستدعي الدالة updatePeerNickname على المفوّض إن لم يكن فارغاً مُمرّراً peerID وsenderNickname. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:369]

```
370:         }
```
> إغلاق نطاق (إغلاق كتلة if). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:370]

```
371:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:371]

```
372:         val recipientID = packet.recipientID?.takeIf { !it.contentEquals(delegate?.getBroadcastRecipient()) }
```
> يعرّف ثابتاً باسم recipientID ويسنده إلى معرّف المستلِم من الحزمة (packet.recipientID) إن لم يكن فارغاً وبشرط (takeIf) ألا يساوي محتواه (contentEquals مع النفي) قيمة getBroadcastRecipient من المفوّض. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:372]

```
373:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:373]

```
374:         if (recipientID == null) {
```
> إذا كان recipientID فارغاً (null) فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:374]

```
375:             // BROADCAST MESSAGE
```
> تعليق: «رسالة بثّ». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:375]

```
376:             handleBroadcastMessage(routed)
```
> يستدعي الدالة handleBroadcastMessage مُمرّراً routed. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:376]

```
377:         } else if (recipientID.toHexString() == myPeerID) {
```
> وإلا إذا كان recipientID محوّلاً إلى نص ست عشري (toHexString) يساوي myPeerID فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:377]

```
378:             // PRIVATE MESSAGE FOR US
```
> تعليق: «رسالة خاصة لنا». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:378]

```
379:             handlePrivateMessage(packet, peerID)
```
> يستدعي الدالة handlePrivateMessage مُمرّراً packet وpeerID. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:379]

```
380:         }
```
> إغلاق نطاق (إغلاق سلسلة if/else if). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:380]

```
381:         // Message relay is now handled by centralized PacketRelayManager
```
> تعليق: «إعادة بثّ الرسالة تُعالَج الآن بواسطة PacketRelayManager المركزي». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:381]

```
382:     }
```
> إغلاق نطاق (إغلاق دالة handleMessage). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:382]

```
383:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:383]

```
384:     /**
```
> تعليق توثيقي: بداية تعليق توثيقي (/**). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:384]

```
385:      * Handle broadcast message with verification enforcement
```
> تعليق: «معالجة رسالة البثّ مع فرض التحقق». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:385]

```
386:      */
```
> تعليق توثيقي: نهاية التعليق التوثيقي (*/). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:386]

```
387:     private suspend fun handleBroadcastMessage(routed: RoutedPacket) {
```
> يعرّف دالة خاصة معلّقة (private suspend) باسم handleBroadcastMessage تأخذ وسيطاً routed من نوع RoutedPacket دون قيمة معادة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:387]

```
388:         val packet = routed.packet
```
> يعرّف ثابتاً باسم packet ويسنده إلى الخاصية packet من routed. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:388]

```
389:         val peerID = routed.peerID ?: "unknown"
```
> يعرّف ثابتاً باسم peerID ويسنده إلى الخاصية peerID من routed، وإن كانت فارغة فيسند السلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:389]

```
390:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:390]

```
391:         // Enforce: only accept public messages from verified peers we know
```
> تعليق: «الفرض: قبول الرسائل العامة فقط من الأقران المُتحقَّق منهم الذين نعرفهم». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:391]

```
392:         val peerInfo = delegate?.getPeerInfo(peerID)
```
> يعرّف ثابتاً باسم peerInfo ويسنده إلى نتيجة استدعاء getPeerInfo على المفوّض مُمرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:392]

```
393:         if (peerInfo == null || !peerInfo.isVerifiedNickname) {
```
> إذا كان peerInfo فارغاً أو كانت خاصية isVerifiedNickname غير صحيحة (نفي) فيفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:393]

```
394:             Log.w(TAG, "🚫 Dropping public message from unverified or unknown peer ${peerID.take(8)}...")
```
> يسجّل رسالة تحذير بالوسم TAG نصّها: «إسقاط رسالة عامة من قرين غير مُتحقَّق منه أو غير معروف لأول ثمانية محارف من peerID...». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:394]

```
395:             return
```
> يُعيد (return) دون قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:395]

```
396:         }
```
> إغلاق نطاق (إغلاق كتلة if). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:396]

```
397:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:397]

```
398:         try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:398]

```
399:             // Try file packet first (voice, image, etc.) and log outcome for FILE_TRANSFER
```
> تعليق: «جرّب حزمة الملف أولاً (صوت، صورة، إلخ) وسجّل النتيجة لـ FILE_TRANSFER». [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:399]

```
400:             val isFileTransfer = com.bitchat.android.protocol.MessageType.fromValue(packet.type) == com.bitchat.android.protocol.MessageType.FILE_TRANSFER
```
> يعرّف ثابتاً باسم isFileTransfer ويسنده إلى نتيجة المقارنة بين تحويل نوع الحزمة (fromValue على MessageType مع packet.type) وعنصر FILE_TRANSFER من التعداد MessageType. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:400]
