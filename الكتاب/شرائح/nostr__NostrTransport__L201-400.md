# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt (الأسطر 201–400)

```
201:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:201]

```
202:                giftWraps.forEach { event ->
```
> يستدعي على قائمة الأغلفة الهديّة (giftWraps) دالّة المرور لكل عنصر (forEach)، ويسمّي كل عنصر حدثاً (event). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:202]

```
203:                    Log.d(TAG, "NostrTransport: sending READ ack giftWrap id=${event.id.take(16)}...")
```
> يكتب رسالة تنقيح (Log.d) بالوسم (TAG) نصّها أنّ نوسترترانسبورت يُرسِل غلاف هديّة إقرار قراءة، مع أوّل ١٦ محرفاً من معرّف الحدث (event.id). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:203]

```
204:                    NostrRelayManager.getInstance(context).sendEvent(event)
```
> يأخذ النسخة الوحيدة من مدير مُرحِّلات نوستر (NostrRelayManager.getInstance) بالسياق (context) ويستدعي إرسال الحدث (sendEvent) للحدث الحالي. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:204]

```
205:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:205]

```
206:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:206]

```
207:                scheduleNextReadAck()
```
> يستدعي دالّة جدولة إقرار القراءة التالي (scheduleNextReadAck). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:207]

```
208:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:208]

```
209:            } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) ويسمّيه (e) ويبدأ كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:209]

```
210:                Log.e(TAG, "Failed to send read receipt via Nostr: ${e.message}")
```
> يكتب رسالة خطأ (Log.e) بالوسم (TAG) نصّها فشل إرسال إيصال القراءة عبر نوستر، مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:210]

```
211:                scheduleNextReadAck()
```
> يستدعي دالّة جدولة إقرار القراءة التالي (scheduleNextReadAck). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:211]

```
212:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:212]

```
213:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:213]

```
214:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:214]

```
215:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:215]

```
216:    private fun scheduleNextReadAck() {
```
> يعرّف دالّة خاصّة (private fun) باسم جدولة إقرار القراءة التالي (scheduleNextReadAck) بلا وسائط ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:216]

```
217:        transportScope.launch {
```
> يطلق عملاً متزامناً (launch) داخل نطاق النقل (transportScope) ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:217]

```
218:            delay(READ_ACK_INTERVAL)
```
> يستدعي تأخيراً (delay) بمقدار ثابت فترة إقرار القراءة (READ_ACK_INTERVAL). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:218]

```
219:            isSendingReadAcks = false
```
> يضبط المتغيّر «يُرسِل إقرارات القراءة» (isSendingReadAcks) على القيمة «خطأ» (false). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:219]

```
220:            processReadQueueIfNeeded()
```
> يستدعي دالّة معالجة طابور القراءة عند الحاجة (processReadQueueIfNeeded). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:220]

```
221:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:221]

```
222:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:222]

```
223:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:223]

```
224:    fun sendFavoriteNotification(to: String, isFavorite: Boolean) {
```
> يعرّف دالّة (fun) باسم إرسال إشعار التفضيل (sendFavoriteNotification) تأخذ وسيطاً «إلى» (to) من نوع نصّ (String) ووسيطاً «هل مُفضَّل» (isFavorite) من نوع منطقي (Boolean) ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:224]

```
225:        transportScope.launch {
```
> يطلق عملاً متزامناً (launch) داخل نطاق النقل (transportScope) ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:225]

```
226:            try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:226]

```
227:                var recipientNostrPubkey: String? = null
```
> يعلن متغيّراً قابلاً للتغيير (var) باسم مفتاح نوستر العامّ للمستلِم (recipientNostrPubkey) من نوع نصّ يقبل العدم (String?) ويُهيّئه بالعدم (null). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:227]

```
228:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:228]

```
229:                // Try to resolve from favorites persistence service
```
> تعليق: حاوِل الحصول عليه من خدمة حفظ المفضّلات. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:229]

```
230:                recipientNostrPubkey = resolveNostrPublicKey(to)
```
> يُسنِد إلى مفتاح نوستر العامّ للمستلِم (recipientNostrPubkey) ناتج استدعاء دالّة حلّ مفتاح نوستر العامّ (resolveNostrPublicKey) بالوسيط «إلى» (to). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:230]

```
231:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:231]

```
232:                if (recipientNostrPubkey == null) {
```
> يفحص شرطاً (if): هل مفتاح نوستر العامّ للمستلِم (recipientNostrPubkey) يساوي العدم (null)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:232]

```
233:                    Log.w(TAG, "No Nostr public key found for favorite notification to: $to")
```
> يكتب رسالة تحذير (Log.w) بالوسم (TAG) نصّها لا يوجد مفتاح نوستر عامّ لإشعار التفضيل إلى، مع قيمة «إلى» (to). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:233]

```
234:                    return@launch
```
> يخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:234]

```
235:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:235]

```
236:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:236]

```
237:                val senderIdentity = NostrIdentityBridge.getCurrentNostrIdentity(context)
```
> يعلن ثابتاً (val) باسم هويّة المُرسِل (senderIdentity) ويُسنِد إليه ناتج استدعاء جسر هويّة نوستر للحصول على هويّة نوستر الحاليّة (NostrIdentityBridge.getCurrentNostrIdentity) بالسياق (context). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:237]

```
238:                if (senderIdentity == null) {
```
> يفحص شرطاً (if): هل هويّة المُرسِل (senderIdentity) تساوي العدم (null)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:238]

```
239:                    Log.e(TAG, "No Nostr identity available for favorite notification")
```
> يكتب رسالة خطأ (Log.e) بالوسم (TAG) نصّها لا تتوفّر هويّة نوستر لإشعار التفضيل. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:239]

```
240:                    return@launch
```
> يخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:240]

```
241:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:241]

```
242:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:242]

```
243:                val content = if (isFavorite) "[FAVORITED]:${senderIdentity.npub}" else "[UNFAVORITED]:${senderIdentity.npub}"
```
> يعلن ثابتاً (val) باسم المحتوى (content) ويُسنِد إليه نصّاً شرطياً: إن كان «هل مُفضَّل» (isFavorite) صحيحاً فالنصّ «[FAVORITED]:» متبوعاً بـ npub لهويّة المُرسِل (senderIdentity.npub)، وإلّا «[UNFAVORITED]:» متبوعاً بنفس القيمة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:243]

```
244:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:244]

```
245:                Log.d(TAG, "NostrTransport: preparing FAVORITE($isFavorite) to ${recipientNostrPubkey.take(16)}...")
```
> يكتب رسالة تنقيح (Log.d) بالوسم (TAG) نصّها أنّ نوسترترانسبورت يُحضِّر تفضيلاً بقيمة «هل مُفضَّل» (isFavorite) إلى أوّل ١٦ محرفاً من مفتاح نوستر العامّ للمستلِم (recipientNostrPubkey.take). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:245]

```
246:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:246]

```
247:                // Convert recipient npub -> hex
```
> تعليق: حوّل npub المستلِم إلى ست عشري. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:247]

```
248:                val recipientHex = try {
```
> يعلن ثابتاً (val) باسم ست عشري المستلِم (recipientHex) ويُسنِد إليه ناتج كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:248]

```
249:                    val (hrp, data) = Bech32.decode(recipientNostrPubkey)
```
> يفكّك إلى ثابتين (val) هما البادئة المقروءة بشريّاً (hrp) والبيانات (data) ناتجَ فكّ ترميز بيك٣٢ (Bech32.decode) لمفتاح نوستر العامّ للمستلِم (recipientNostrPubkey). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:249]

```
250:                    if (hrp != "npub") return@launch
```
> يفحص شرطاً (if): إن لم تساوِ البادئة (hrp) النصّ "npub" فاخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:250]

```
251:                    data.joinToString("") { "%02x".format(it) }
```
> يدمج البيانات (data) في نصّ واحد بلا فاصل (joinToString) بتنسيق كل عنصر (it) ست عشرياً من خانتين بصيغة "%02x". [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:251]

```
252:                } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) ويسمّيه (e) ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:252]

```
253:                    return@launch
```
> يخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:253]

```
254:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:254]

```
255:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:255]

```
256:                val embedded = NostrEmbeddedBitChat.encodePMForNostr(
```
> يعلن ثابتاً (val) باسم المضمَّن (embedded) ويُسنِد إليه ناتج استدعاء ترميز رسالة خاصّة لنوستر (NostrEmbeddedBitChat.encodePMForNostr) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:256]

```
257:                    content = content,
```
> يمرّر الوسيط المحتوى (content) بقيمة الثابت المحتوى (content). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:257]

```
258:                    messageID = UUID.randomUUID().toString(),
```
> يمرّر الوسيط معرّف الرسالة (messageID) بقيمة معرّف عالمي عشوائي (UUID.randomUUID) محوَّل إلى نصّ (toString). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:258]

```
259:                    recipientPeerID = to,
```
> يمرّر الوسيط معرّف نظير المستلِم (recipientPeerID) بقيمة «إلى» (to). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:259]

```
260:                    senderPeerID = senderPeerID
```
> يمرّر الوسيط معرّف نظير المُرسِل (senderPeerID) بقيمة الحقل معرّف نظير المُرسِل (senderPeerID). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:260]

```
261:                )
```
> إغلاق قائمة الوسائط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:261]

```
262:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:262]

```
263:                if (embedded == null) {
```
> يفحص شرطاً (if): هل المضمَّن (embedded) يساوي العدم (null)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:263]

```
264:                    Log.e(TAG, "NostrTransport: failed to embed favorite notification")
```
> يكتب رسالة خطأ (Log.e) بالوسم (TAG) نصّها أنّ نوسترترانسبورت فشل في تضمين إشعار التفضيل. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:264]

```
265:                    return@launch
```
> يخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:265]

```
266:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:266]

```
267:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:267]

```
268:                val giftWraps = NostrProtocol.createPrivateMessage(
```
> يعلن ثابتاً (val) باسم الأغلفة الهديّة (giftWraps) ويُسنِد إليه ناتج استدعاء إنشاء رسالة خاصّة لبروتوكول نوستر (NostrProtocol.createPrivateMessage) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:268]

```
269:                    content = embedded,
```
> يمرّر الوسيط المحتوى (content) بقيمة الثابت المضمَّن (embedded). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:269]

```
270:                    recipientPubkey = recipientHex,
```
> يمرّر الوسيط مفتاح المستلِم العامّ (recipientPubkey) بقيمة ست عشري المستلِم (recipientHex). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:270]

```
271:                    senderIdentity = senderIdentity
```
> يمرّر الوسيط هويّة المُرسِل (senderIdentity) بقيمة الثابت هويّة المُرسِل (senderIdentity). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:271]

```
272:                )
```
> إغلاق قائمة الوسائط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:272]

```
273:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:273]

```
274:                giftWraps.forEach { event ->
```
> يستدعي على الأغلفة الهديّة (giftWraps) دالّة المرور لكل عنصر (forEach)، ويسمّي كل عنصر حدثاً (event). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:274]

```
275:                    Log.d(TAG, "NostrTransport: sending favorite giftWrap id=${event.id.take(16)}...")
```
> يكتب رسالة تنقيح (Log.d) بالوسم (TAG) نصّها أنّ نوسترترانسبورت يُرسِل غلاف هديّة تفضيل، مع أوّل ١٦ محرفاً من معرّف الحدث (event.id). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:275]

```
276:                    NostrRelayManager.getInstance(context).sendEvent(event)
```
> يأخذ النسخة الوحيدة من مدير مُرحِّلات نوستر (NostrRelayManager.getInstance) بالسياق (context) ويستدعي إرسال الحدث (sendEvent) للحدث الحالي. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:276]

```
277:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:277]

```
278:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:278]

```
279:            } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) ويسمّيه (e) ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:279]

```
280:                Log.e(TAG, "Failed to send favorite notification via Nostr: ${e.message}")
```
> يكتب رسالة خطأ (Log.e) بالوسم (TAG) نصّها فشل إرسال إشعار التفضيل عبر نوستر، مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:280]

```
281:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:281]

```
282:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:282]

```
283:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:283]

```
284:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:284]

```
285:    fun sendDeliveryAck(messageID: String, to: String) {
```
> يعرّف دالّة (fun) باسم إرسال إقرار التسليم (sendDeliveryAck) تأخذ وسيطاً معرّف الرسالة (messageID) من نوع نصّ (String) ووسيطاً «إلى» (to) من نوع نصّ (String) ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:285]

```
286:        transportScope.launch {
```
> يطلق عملاً متزامناً (launch) داخل نطاق النقل (transportScope) ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:286]

```
287:            try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:287]

```
288:                var recipientNostrPubkey: String? = null
```
> يعلن متغيّراً قابلاً للتغيير (var) باسم مفتاح نوستر العامّ للمستلِم (recipientNostrPubkey) من نوع نصّ يقبل العدم (String?) ويُهيّئه بالعدم (null). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:288]

```
289:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:289]

```
290:                // Try to resolve from favorites persistence service
```
> تعليق: حاوِل الحصول عليه من خدمة حفظ المفضّلات. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:290]

```
291:                recipientNostrPubkey = resolveNostrPublicKey(to)
```
> يُسنِد إلى مفتاح نوستر العامّ للمستلِم (recipientNostrPubkey) ناتج استدعاء دالّة حلّ مفتاح نوستر العامّ (resolveNostrPublicKey) بالوسيط «إلى» (to). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:291]

```
292:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:292]

```
293:                if (recipientNostrPubkey == null) {
```
> يفحص شرطاً (if): هل مفتاح نوستر العامّ للمستلِم (recipientNostrPubkey) يساوي العدم (null)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:293]

```
294:                    Log.w(TAG, "No Nostr public key found for delivery ack to: $to")
```
> يكتب رسالة تحذير (Log.w) بالوسم (TAG) نصّها لا يوجد مفتاح نوستر عامّ لإقرار التسليم إلى، مع قيمة «إلى» (to). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:294]

```
295:                    return@launch
```
> يخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:295]

```
296:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:296]

```
297:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:297]

```
298:                val senderIdentity = NostrIdentityBridge.getCurrentNostrIdentity(context)
```
> يعلن ثابتاً (val) باسم هويّة المُرسِل (senderIdentity) ويُسنِد إليه ناتج استدعاء جسر هويّة نوستر للحصول على هويّة نوستر الحاليّة (NostrIdentityBridge.getCurrentNostrIdentity) بالسياق (context). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:298]

```
299:                if (senderIdentity == null) {
```
> يفحص شرطاً (if): هل هويّة المُرسِل (senderIdentity) تساوي العدم (null)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:299]

```
300:                    Log.e(TAG, "No Nostr identity available for delivery ack")
```
> يكتب رسالة خطأ (Log.e) بالوسم (TAG) نصّها لا تتوفّر هويّة نوستر لإقرار التسليم. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:300]

```
301:                    return@launch
```
> يخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:301]

```
302:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:302]

```
303:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:303]

```
304:                Log.d(TAG, "NostrTransport: preparing DELIVERED ack for id=${messageID.take(8)}... to ${recipientNostrPubkey.take(16)}...")
```
> يكتب رسالة تنقيح (Log.d) بالوسم (TAG) نصّها أنّ نوسترترانسبورت يُحضِّر إقرار «تمّ التسليم» للمعرّف بأوّل ٨ محارف من معرّف الرسالة (messageID.take) إلى أوّل ١٦ محرفاً من مفتاح نوستر العامّ للمستلِم (recipientNostrPubkey.take). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:304]

```
305:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:305]

```
306:                val recipientHex = try {
```
> يعلن ثابتاً (val) باسم ست عشري المستلِم (recipientHex) ويُسنِد إليه ناتج كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:306]

```
307:                    val (hrp, data) = Bech32.decode(recipientNostrPubkey)
```
> يفكّك إلى ثابتين (val) هما البادئة المقروءة بشريّاً (hrp) والبيانات (data) ناتجَ فكّ ترميز بيك٣٢ (Bech32.decode) لمفتاح نوستر العامّ للمستلِم (recipientNostrPubkey). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:307]

```
308:                    if (hrp != "npub") return@launch
```
> يفحص شرطاً (if): إن لم تساوِ البادئة (hrp) النصّ "npub" فاخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:308]

```
309:                    data.joinToString("") { "%02x".format(it) }
```
> يدمج البيانات (data) في نصّ واحد بلا فاصل (joinToString) بتنسيق كل عنصر (it) ست عشرياً من خانتين بصيغة "%02x". [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:309]

```
310:                } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) ويسمّيه (e) ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:310]

```
311:                    return@launch
```
> يخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:311]

```
312:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:312]

```
313:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:313]

```
314:                val ack = NostrEmbeddedBitChat.encodeAckForNostr(
```
> يعلن ثابتاً (val) باسم الإقرار (ack) ويُسنِد إليه ناتج استدعاء ترميز إقرار لنوستر (NostrEmbeddedBitChat.encodeAckForNostr) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:314]

```
315:                    type = NoisePayloadType.DELIVERED,
```
> يمرّر الوسيط النوع (type) بقيمة «تمّ التسليم» من تعداد نوع حمولة نويز (NoisePayloadType.DELIVERED). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:315]

```
316:                    messageID = messageID,
```
> يمرّر الوسيط معرّف الرسالة (messageID) بقيمة الوسيط معرّف الرسالة (messageID). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:316]

```
317:                    recipientPeerID = to,
```
> يمرّر الوسيط معرّف نظير المستلِم (recipientPeerID) بقيمة «إلى» (to). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:317]

```
318:                    senderPeerID = senderPeerID
```
> يمرّر الوسيط معرّف نظير المُرسِل (senderPeerID) بقيمة الحقل معرّف نظير المُرسِل (senderPeerID). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:318]

```
319:                )
```
> إغلاق قائمة الوسائط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:319]

```
320:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:320]

```
321:                if (ack == null) {
```
> يفحص شرطاً (if): هل الإقرار (ack) يساوي العدم (null)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:321]

```
322:                    Log.e(TAG, "NostrTransport: failed to embed DELIVERED ack")
```
> يكتب رسالة خطأ (Log.e) بالوسم (TAG) نصّها أنّ نوسترترانسبورت فشل في تضمين إقرار «تمّ التسليم». [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:322]

```
323:                    return@launch
```
> يخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:323]

```
324:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:324]

```
325:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:325]

```
326:                val giftWraps = NostrProtocol.createPrivateMessage(
```
> يعلن ثابتاً (val) باسم الأغلفة الهديّة (giftWraps) ويُسنِد إليه ناتج استدعاء إنشاء رسالة خاصّة لبروتوكول نوستر (NostrProtocol.createPrivateMessage) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:326]

```
327:                    content = ack,
```
> يمرّر الوسيط المحتوى (content) بقيمة الثابت الإقرار (ack). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:327]

```
328:                    recipientPubkey = recipientHex,
```
> يمرّر الوسيط مفتاح المستلِم العامّ (recipientPubkey) بقيمة ست عشري المستلِم (recipientHex). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:328]

```
329:                    senderIdentity = senderIdentity
```
> يمرّر الوسيط هويّة المُرسِل (senderIdentity) بقيمة الثابت هويّة المُرسِل (senderIdentity). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:329]

```
330:                )
```
> إغلاق قائمة الوسائط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:330]

```
331:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:331]

```
332:                giftWraps.forEach { event ->
```
> يستدعي على الأغلفة الهديّة (giftWraps) دالّة المرور لكل عنصر (forEach)، ويسمّي كل عنصر حدثاً (event). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:332]

```
333:                    Log.d(TAG, "NostrTransport: sending DELIVERED ack giftWrap id=${event.id.take(16)}...")
```
> يكتب رسالة تنقيح (Log.d) بالوسم (TAG) نصّها أنّ نوسترترانسبورت يُرسِل غلاف هديّة إقرار «تمّ التسليم»، مع أوّل ١٦ محرفاً من معرّف الحدث (event.id). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:333]

```
334:                    NostrRelayManager.getInstance(context).sendEvent(event)
```
> يأخذ النسخة الوحيدة من مدير مُرحِّلات نوستر (NostrRelayManager.getInstance) بالسياق (context) ويستدعي إرسال الحدث (sendEvent) للحدث الحالي. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:334]

```
335:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:335]

```
336:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:336]

```
337:            } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) ويسمّيه (e) ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:337]

```
338:                Log.e(TAG, "Failed to send delivery ack via Nostr: ${e.message}")
```
> يكتب رسالة خطأ (Log.e) بالوسم (TAG) نصّها فشل إرسال إقرار التسليم عبر نوستر، مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:338]

```
339:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:339]

```
340:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:340]

```
341:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:341]

```
342:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:342]

```
343:    // MARK: - Geohash ACK helpers (for per-geohash identity DMs)
```
> تعليق: علامة — مساعِدات إقرار التجزئة الجغرافيّة (لرسائل مباشرة بهويّة لكلّ تجزئة جغرافيّة). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:343]

```
344:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:344]

```
345:    fun sendDeliveryAckGeohash(
```
> يعرّف دالّة (fun) باسم إرسال إقرار تسليم بالتجزئة الجغرافيّة (sendDeliveryAckGeohash) ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:345]

```
346:        messageID: String,
```
> يعلن وسيطاً معرّف الرسالة (messageID) من نوع نصّ (String). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:346]

```
347:        toRecipientHex: String,
```
> يعلن وسيطاً ست عشري المستلِم (toRecipientHex) من نوع نصّ (String). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:347]

```
348:        fromIdentity: NostrIdentity
```
> يعلن وسيطاً «من الهويّة» (fromIdentity) من نوع هويّة نوستر (NostrIdentity). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:348]

```
349:    ) {
```
> إغلاق قائمة الوسائط وفتح جسم الدالّة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:349]

```
350:        transportScope.launch {
```
> يطلق عملاً متزامناً (launch) داخل نطاق النقل (transportScope) ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:350]

```
351:            try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:351]

```
352:                Log.d(TAG, "GeoDM: send DELIVERED -> recip=${toRecipientHex.take(8)}... mid=${messageID.take(8)}... from=${fromIdentity.publicKeyHex.take(8)}...")
```
> يكتب رسالة تنقيح (Log.d) بالوسم (TAG) نصّها رسالة مباشرة جغرافيّة (GeoDM): إرسال «تمّ التسليم» إلى مستلِم بأوّل ٨ محارف من ست عشري المستلِم (toRecipientHex.take)، مع أوّل ٨ محارف من معرّف الرسالة (messageID.take)، ومن أوّل ٨ محارف من المفتاح العامّ الست عشري للهويّة (fromIdentity.publicKeyHex.take). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:352]

```
353:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:353]

```
354:                val embedded = NostrEmbeddedBitChat.encodeAckForNostrNoRecipient(
```
> يعلن ثابتاً (val) باسم المضمَّن (embedded) ويُسنِد إليه ناتج استدعاء ترميز إقرار لنوستر بلا مستلِم (NostrEmbeddedBitChat.encodeAckForNostrNoRecipient) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:354]

```
355:                    type = NoisePayloadType.DELIVERED,
```
> يمرّر الوسيط النوع (type) بقيمة «تمّ التسليم» من تعداد نوع حمولة نويز (NoisePayloadType.DELIVERED). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:355]

```
356:                    messageID = messageID,
```
> يمرّر الوسيط معرّف الرسالة (messageID) بقيمة الوسيط معرّف الرسالة (messageID). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:356]

```
357:                    senderPeerID = senderPeerID
```
> يمرّر الوسيط معرّف نظير المُرسِل (senderPeerID) بقيمة الحقل معرّف نظير المُرسِل (senderPeerID). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:357]

```
358:                )
```
> إغلاق قائمة الوسائط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:358]

```
359:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:359]

```
360:                if (embedded == null) return@launch
```
> يفحص شرطاً (if): إن كان المضمَّن (embedded) يساوي العدم (null) فاخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:360]

```
361:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:361]

```
362:                val giftWraps = NostrProtocol.createPrivateMessage(
```
> يعلن ثابتاً (val) باسم الأغلفة الهديّة (giftWraps) ويُسنِد إليه ناتج استدعاء إنشاء رسالة خاصّة لبروتوكول نوستر (NostrProtocol.createPrivateMessage) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:362]

```
363:                    content = embedded,
```
> يمرّر الوسيط المحتوى (content) بقيمة الثابت المضمَّن (embedded). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:363]

```
364:                    recipientPubkey = toRecipientHex,
```
> يمرّر الوسيط مفتاح المستلِم العامّ (recipientPubkey) بقيمة ست عشري المستلِم (toRecipientHex). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:364]

```
365:                    senderIdentity = fromIdentity
```
> يمرّر الوسيط هويّة المُرسِل (senderIdentity) بقيمة الوسيط «من الهويّة» (fromIdentity). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:365]

```
366:                )
```
> إغلاق قائمة الوسائط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:366]

```
367:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:367]

```
368:                // Register pending gift wrap for deduplication and send all
```
> تعليق: سجّل الغلاف الهديّة المعلَّق لإزالة التكرار وأرسِل الكلّ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:368]

```
369:                giftWraps.forEach { event ->
```
> يستدعي على الأغلفة الهديّة (giftWraps) دالّة المرور لكل عنصر (forEach)، ويسمّي كل عنصر حدثاً (event). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:369]

```
370:                    NostrRelayManager.registerPendingGiftWrap(event.id)
```
> يستدعي على مدير مُرحِّلات نوستر (NostrRelayManager) دالّة تسجيل الغلاف الهديّة المعلَّق (registerPendingGiftWrap) بمعرّف الحدث (event.id). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:370]

```
371:                    NostrRelayManager.getInstance(context).sendEvent(event)
```
> يأخذ النسخة الوحيدة من مدير مُرحِّلات نوستر (NostrRelayManager.getInstance) بالسياق (context) ويستدعي إرسال الحدث (sendEvent) للحدث الحالي. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:371]

```
372:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:372]

```
373:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:373]

```
374:            } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) ويسمّيه (e) ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:374]

```
375:                Log.e(TAG, "Failed to send geohash delivery ack: ${e.message}")
```
> يكتب رسالة خطأ (Log.e) بالوسم (TAG) نصّها فشل إرسال إقرار التسليم بالتجزئة الجغرافيّة، مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:375]

```
376:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:376]

```
377:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:377]

```
378:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:378]

```
379:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:379]

```
380:    fun sendReadReceiptGeohash(
```
> يعرّف دالّة (fun) باسم إرسال إيصال قراءة بالتجزئة الجغرافيّة (sendReadReceiptGeohash) ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:380]

```
381:        messageID: String,
```
> يعلن وسيطاً معرّف الرسالة (messageID) من نوع نصّ (String). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:381]

```
382:        toRecipientHex: String,
```
> يعلن وسيطاً ست عشري المستلِم (toRecipientHex) من نوع نصّ (String). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:382]

```
383:        fromIdentity: NostrIdentity
```
> يعلن وسيطاً «من الهويّة» (fromIdentity) من نوع هويّة نوستر (NostrIdentity). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:383]

```
384:    ) {
```
> إغلاق قائمة الوسائط وفتح جسم الدالّة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:384]

```
385:        transportScope.launch {
```
> يطلق عملاً متزامناً (launch) داخل نطاق النقل (transportScope) ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:385]

```
386:            try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:386]

```
387:                Log.d(TAG, "GeoDM: send READ -> recip=${toRecipientHex.take(8)}... mid=${messageID.take(8)}... from=${fromIdentity.publicKeyHex.take(8)}...")
```
> يكتب رسالة تنقيح (Log.d) بالوسم (TAG) نصّها رسالة مباشرة جغرافيّة (GeoDM): إرسال «قراءة» إلى مستلِم بأوّل ٨ محارف من ست عشري المستلِم (toRecipientHex.take)، مع أوّل ٨ محارف من معرّف الرسالة (messageID.take)، ومن أوّل ٨ محارف من المفتاح العامّ الست عشري للهويّة (fromIdentity.publicKeyHex.take). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:387]

```
388:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:388]

```
389:                val embedded = NostrEmbeddedBitChat.encodeAckForNostrNoRecipient(
```
> يعلن ثابتاً (val) باسم المضمَّن (embedded) ويُسنِد إليه ناتج استدعاء ترميز إقرار لنوستر بلا مستلِم (NostrEmbeddedBitChat.encodeAckForNostrNoRecipient) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:389]

```
390:                    type = NoisePayloadType.READ_RECEIPT,
```
> يمرّر الوسيط النوع (type) بقيمة «إيصال القراءة» من تعداد نوع حمولة نويز (NoisePayloadType.READ_RECEIPT). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:390]

```
391:                    messageID = messageID,
```
> يمرّر الوسيط معرّف الرسالة (messageID) بقيمة الوسيط معرّف الرسالة (messageID). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:391]

```
392:                    senderPeerID = senderPeerID
```
> يمرّر الوسيط معرّف نظير المُرسِل (senderPeerID) بقيمة الحقل معرّف نظير المُرسِل (senderPeerID). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:392]

```
393:                )
```
> إغلاق قائمة الوسائط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:393]

```
394:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:394]

```
395:                if (embedded == null) return@launch
```
> يفحص شرطاً (if): إن كان المضمَّن (embedded) يساوي العدم (null) فاخرج من كتلة الإطلاق (return@launch). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:395]

```
396:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:396]

```
397:                val giftWraps = NostrProtocol.createPrivateMessage(
```
> يعلن ثابتاً (val) باسم الأغلفة الهديّة (giftWraps) ويُسنِد إليه ناتج استدعاء إنشاء رسالة خاصّة لبروتوكول نوستر (NostrProtocol.createPrivateMessage) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:397]

```
398:                    content = embedded,
```
> يمرّر الوسيط المحتوى (content) بقيمة الثابت المضمَّن (embedded). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:398]

```
399:                    recipientPubkey = toRecipientHex,
```
> يمرّر الوسيط مفتاح المستلِم العامّ (recipientPubkey) بقيمة ست عشري المستلِم (toRecipientHex). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:399]

```
400:                    senderIdentity = fromIdentity
```
> يمرّر الوسيط هويّة المُرسِل (senderIdentity) بقيمة الوسيط «من الهويّة» (fromIdentity). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:400]
