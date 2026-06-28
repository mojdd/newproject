# شريحة — app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt (الأسطر 201–328)

```
201:         val peerID = routed.peerID ?: "unknown"
```
> يُعرَّف متغيّر ثابت اسمه مُعرِّف-الند (peerID) ويُسنَد إليه قيمة الحقل peerID من الكائن routed، وإن كانت تلك القيمة فارغة (null) فتُسنَد السلسلة النصية "unknown" بدلاً منها. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:201]

```
202:         Log.d(TAG, "Processing announce from ${formatPeerForLog(peerID)}")
```
> تُستدعى دالة التسجيل Log.d بالوسم TAG ونصٍّ يقول "Processing announce from " متبوعاً بناتج استدعاء الدالة formatPeerForLog على peerID. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:202]

```
203:         delegate?.handleAnnounce(routed)
```
> تُستدعى دالة handleAnnounce على الكائن المُفوَّض (delegate) إن لم يكن فارغاً، مع تمرير الوسيط routed. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:203]

```
204:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:204]

```
205:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:205]

```
206:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:206]

```
207:      * Handle regular message
```
> تعليق: معالجة الرسالة العادية. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:207]

```
208:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:208]

```
209:     private suspend fun handleMessage(routed: RoutedPacket) {
```
> تُعرَّف دالة خاصّة معلّقة (suspend) اسمها معالجة-الرسالة (handleMessage) تأخذ وسيطاً اسمه routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:209]

```
210:         val peerID = routed.peerID ?: "unknown"
```
> يُعرَّف متغيّر ثابت اسمه peerID ويُسنَد إليه قيمة الحقل peerID من routed، وإن كانت فارغة فالسلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:210]

```
211:         Log.d(TAG, "Processing message from ${formatPeerForLog(peerID)}")
```
> تُستدعى دالة التسجيل Log.d بالوسم TAG ونصٍّ يقول "Processing message from " متبوعاً بناتج استدعاء formatPeerForLog على peerID. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:211]

```
212:         delegate?.handleMessage(routed)
```
> تُستدعى دالة handleMessage على الكائن المُفوَّض delegate إن لم يكن فارغاً، مع تمرير routed. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:212]

```
213:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:213]

```
214:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:214]

```
215:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:215]

```
216:      * Handle leave message
```
> تعليق: معالجة رسالة المغادرة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:216]

```
217:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:217]

```
218:     private suspend fun handleLeave(routed: RoutedPacket) {
```
> تُعرَّف دالة خاصّة معلّقة اسمها معالجة-المغادرة (handleLeave) تأخذ وسيطاً اسمه routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:218]

```
219:         val peerID = routed.peerID ?: "unknown"
```
> يُعرَّف متغيّر ثابت اسمه peerID ويُسنَد إليه قيمة الحقل peerID من routed، وإن كانت فارغة فالسلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:219]

```
220:         Log.d(TAG, "Processing leave from ${formatPeerForLog(peerID)}")
```
> تُستدعى دالة التسجيل Log.d بالوسم TAG ونصٍّ يقول "Processing leave from " متبوعاً بناتج استدعاء formatPeerForLog على peerID. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:220]

```
221:         delegate?.handleLeave(routed)
```
> تُستدعى دالة handleLeave على الكائن المُفوَّض delegate إن لم يكن فارغاً، مع تمرير routed. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:221]

```
222:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:222]

```
223:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:223]

```
224:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:224]

```
225:      * Handle message fragments
```
> تعليق: معالجة شظايا الرسالة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:225]

```
226:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:226]

```
227:     private suspend fun handleFragment(routed: RoutedPacket) {
```
> تُعرَّف دالة خاصّة معلّقة اسمها معالجة-الشظية (handleFragment) تأخذ وسيطاً اسمه routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:227]

```
228:         val peerID = routed.peerID ?: "unknown"
```
> يُعرَّف متغيّر ثابت اسمه peerID ويُسنَد إليه قيمة الحقل peerID من routed، وإن كانت فارغة فالسلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:228]

```
229:         Log.d(TAG, "Processing fragment from ${formatPeerForLog(peerID)}")
```
> تُستدعى دالة التسجيل Log.d بالوسم TAG ونصٍّ يقول "Processing fragment from " متبوعاً بناتج استدعاء formatPeerForLog على peerID. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:229]

```
230:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:230]

```
231:         val reassembledPacket = delegate?.handleFragment(routed.packet)
```
> يُعرَّف متغيّر ثابت اسمه الحُزمة-المُعاد-تجميعها (reassembledPacket) ويُسنَد إليه ناتج استدعاء handleFragment على الكائن المُفوَّض delegate إن لم يكن فارغاً، مع تمرير الحقل packet من routed. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:231]

```
232:         if (reassembledPacket != null) {
```
> شرط: إن لم تكن reassembledPacket فارغة (null) يُنفَّذ ما بين القوسين. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:232]

```
233:             Log.d(TAG, "Fragment reassembled, processing complete message")
```
> تُستدعى دالة التسجيل Log.d بالوسم TAG ونصٍّ يقول "Fragment reassembled, processing complete message". [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:233]

```
234:             handleReceivedPacket(RoutedPacket(reassembledPacket, routed.peerID, routed.relayAddress))
```
> تُستدعى دالة handleReceivedPacket مع تمرير كائن RoutedPacket جديد مُنشأ من reassembledPacket والحقل peerID من routed والحقل relayAddress من routed. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:234]

```
235:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:235]

```
236:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:236]

```
237:         // Fragment relay is now handled by centralized PacketRelayManager
```
> تعليق: تمرير الشظية يُعالَج الآن بواسطة PacketRelayManager المركزي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:237]

```
238:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:238]

```
239:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:239]

```
240:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:240]

```
241:      * Handle REQUEST_SYNC packets (public, TTL=1)
```
> تعليق: معالجة حُزم REQUEST_SYNC (عامّة، TTL=1). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:241]

```
242:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:242]

```
243:     private suspend fun handleRequestSync(routed: RoutedPacket) {
```
> تُعرَّف دالة خاصّة معلّقة اسمها معالجة-طلب-المزامنة (handleRequestSync) تأخذ وسيطاً اسمه routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:243]

```
244:         val peerID = routed.peerID ?: "unknown"
```
> يُعرَّف متغيّر ثابت اسمه peerID ويُسنَد إليه قيمة الحقل peerID من routed، وإن كانت فارغة فالسلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:244]

```
245:         Log.d(TAG, "Processing REQUEST_SYNC from ${formatPeerForLog(peerID)}")
```
> تُستدعى دالة التسجيل Log.d بالوسم TAG ونصٍّ يقول "Processing REQUEST_SYNC from " متبوعاً بناتج استدعاء formatPeerForLog على peerID. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:245]

```
246:         delegate?.handleRequestSync(routed)
```
> تُستدعى دالة handleRequestSync على الكائن المُفوَّض delegate إن لم يكن فارغاً، مع تمرير routed. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:246]

```
247:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:247]

```
248:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:248]

```
249:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:249]

```
250:      * Handle delivery acknowledgment
```
> تعليق: معالجة إقرار التسليم. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:250]

```
251:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:251]

```
252: //    private suspend fun handleDeliveryAck(routed: RoutedPacket) {
```
> تعليق: سطر مُعطَّل يُعرِّف دالة خاصّة معلّقة اسمها handleDeliveryAck تأخذ وسيطاً routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:252]

```
253: //        val peerID = routed.peerID ?: "unknown"
```
> تعليق: سطر مُعطَّل يُعرِّف peerID ويُسنِد إليه routed.peerID أو "unknown" عند الفراغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:253]

```
254: //        Log.d(TAG, "Processing delivery ACK from ${formatPeerForLog(peerID)}")
```
> تعليق: سطر مُعطَّل يستدعي Log.d بالوسم TAG ونصٍّ "Processing delivery ACK from " متبوعاً بناتج formatPeerForLog على peerID. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:254]

```
255: //        delegate?.handleDeliveryAck(routed)
```
> تعليق: سطر مُعطَّل يستدعي handleDeliveryAck على delegate إن لم يكن فارغاً مع تمرير routed. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:255]

```
256: //    }
```
> تعليق: سطر مُعطَّل يمثّل إغلاق نطاق الدالة المُعطَّلة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:256]

```
257:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:257]

```
258:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:258]

```
259:      * Get debug information
```
> تعليق: الحصول على معلومات التنقيح. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:259]

```
260:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:260]

```
261:     fun getDebugInfo(): String {
```
> تُعرَّف دالة عامّة اسمها الحصول-على-معلومات-التنقيح (getDebugInfo) تُعيد قيمة من نوع String. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:261]

```
262:         return buildString {
```
> تُعيد الدالة ناتج بانية-السلسلة buildString مع كتلة لمداء (lambda) تبني السلسلة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:262]

```
263:             appendLine("=== Packet Processor Debug Info ===")
```
> تُستدعى appendLine لإلحاق السطر "=== Packet Processor Debug Info ===". [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:263]

```
264:             appendLine("Processor Scope Active: ${processorScope.isActive}")
```
> تُستدعى appendLine لإلحاق السطر "Processor Scope Active: " متبوعاً بقيمة الحقل isActive من processorScope. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:264]

```
265:             appendLine("Active Peer Actors: ${actors.size}")
```
> تُستدعى appendLine لإلحاق السطر "Active Peer Actors: " متبوعاً بقيمة size من actors. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:265]

```
266:             appendLine("My Peer ID: $myPeerID")
```
> تُستدعى appendLine لإلحاق السطر "My Peer ID: " متبوعاً بقيمة myPeerID. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:266]

```
267:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:267]

```
268:             if (actors.isNotEmpty()) {
```
> شرط: إن كانت actors غير فارغة (isNotEmpty تُعيد صحيح) يُنفَّذ ما بين القوسين. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:268]

```
269:                 appendLine("Peer Actors:")
```
> تُستدعى appendLine لإلحاق السطر "Peer Actors:". [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:269]

```
270:                 actors.keys.forEach { peerID ->
```
> يُمَرّ على كل مفتاح من مفاتيح actors عبر forEach، وتُسمّى قيمة العنصر الحالي peerID. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:270]

```
271:                     appendLine("  - $peerID")
```
> تُستدعى appendLine لإلحاق السطر "  - " متبوعاً بقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:271]

```
272:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:272]

```
273:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:273]

```
274:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:274]

```
275:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:275]

```
276:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:276]

```
277:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:277]

```
278:      * Shutdown the processor and all peer actors
```
> تعليق: إيقاف المُعالِج وكل ممثّلي الأنداد. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:278]

```
279:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:279]

```
280:     fun shutdown() {
```
> تُعرَّف دالة عامّة اسمها إيقاف (shutdown) بلا وسائط ولا قيمة مُعادة صريحة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:280]

```
281:         Log.d(TAG, "Shutting down PacketProcessor and ${actors.size} peer actors")
```
> تُستدعى دالة التسجيل Log.d بالوسم TAG ونصٍّ يقول "Shutting down PacketProcessor and " متبوعاً بقيمة size من actors ثم " peer actors". [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:281]

```
282:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:282]

```
283:         // Close all peer actors gracefully
```
> تعليق: إغلاق كل ممثّلي الأنداد بلطف. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:283]

```
284:         actors.values.forEach { actor ->
```
> يُمَرّ على كل قيمة من قيم actors عبر forEach، وتُسمّى قيمة العنصر الحالي actor. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:284]

```
285:             actor.close()
```
> تُستدعى دالة close على actor. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:285]

```
286:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:286]

```
287:         actors.clear()
```
> تُستدعى دالة clear على actors لإفراغها. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:287]

```
288:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:288]

```
289:         // Shutdown the relay manager
```
> تعليق: إيقاف مدير التمرير. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:289]

```
290:         packetRelayManager.shutdown()
```
> تُستدعى دالة shutdown على packetRelayManager. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:290]

```
291:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:291]

```
292:         // Cancel the main scope
```
> تعليق: إلغاء النطاق الرئيسي. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:292]

```
293:         processorScope.cancel()
```
> تُستدعى دالة cancel على processorScope. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:293]

```
294:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:294]

```
295:         Log.d(TAG, "PacketProcessor shutdown complete")
```
> تُستدعى دالة التسجيل Log.d بالوسم TAG ونصٍّ يقول "PacketProcessor shutdown complete". [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:295]

```
296:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:296]

```
297: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:297]

```
298:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:298]

```
299: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:299]

```
300:  * Delegate interface for packet processor callbacks
```
> تعليق: واجهة المُفوَّض لردود نداء مُعالِج الحُزم. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:300]

```
301:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:301]

```
302: interface PacketProcessorDelegate {
```
> تُعرَّف واجهة (interface) اسمها مُفوَّض-مُعالِج-الحُزم (PacketProcessorDelegate). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:302]

```
303:     // Security validation
```
> تعليق: التحقق الأمني. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:303]

```
304:     fun validatePacketSecurity(packet: BitchatPacket, peerID: String): Boolean
```
> تُعلَن دالة اسمها التحقق-من-أمان-الحُزمة (validatePacketSecurity) تأخذ وسيطاً packet من نوع BitchatPacket ووسيطاً peerID من نوع String وتُعيد قيمة Boolean. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:304]

```
305:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:305]

```
306:     // Peer management
```
> تعليق: إدارة الأنداد. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:306]

```
307:     fun updatePeerLastSeen(peerID: String)
```
> تُعلَن دالة اسمها تحديث-آخر-ظهور-للند (updatePeerLastSeen) تأخذ وسيطاً peerID من نوع String دون قيمة مُعادة صريحة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:307]

```
308:     fun getPeerNickname(peerID: String): String?
```
> تُعلَن دالة اسمها الحصول-على-كنية-الند (getPeerNickname) تأخذ وسيطاً peerID من نوع String وتُعيد String قابلة للفراغ (nullable). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:308]

```
309:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:309]

```
310:     // Network information
```
> تعليق: معلومات الشبكة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:310]

```
311:     fun getNetworkSize(): Int
```
> تُعلَن دالة اسمها الحصول-على-حجم-الشبكة (getNetworkSize) بلا وسائط وتُعيد قيمة Int. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:311]

```
312:     fun getBroadcastRecipient(): ByteArray
```
> تُعلَن دالة اسمها الحصول-على-مستلِم-البثّ (getBroadcastRecipient) بلا وسائط وتُعيد قيمة ByteArray. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:312]

```
313:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:313]

```
314:     // Message type handlers
```
> تعليق: معالِجات أنواع الرسائل. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:314]

```
315:     fun handleNoiseHandshake(routed: RoutedPacket): Boolean
```
> تُعلَن دالة اسمها معالجة-مصافحة-نويز (handleNoiseHandshake) تأخذ وسيطاً routed من نوع RoutedPacket وتُعيد قيمة Boolean. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:315]

```
316:     fun handleNoiseEncrypted(routed: RoutedPacket)
```
> تُعلَن دالة اسمها معالجة-المُشفَّر-بنويز (handleNoiseEncrypted) تأخذ وسيطاً routed من نوع RoutedPacket دون قيمة مُعادة صريحة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:316]

```
317:     fun handleAnnounce(routed: RoutedPacket)
```
> تُعلَن دالة اسمها معالجة-الإعلان (handleAnnounce) تأخذ وسيطاً routed من نوع RoutedPacket دون قيمة مُعادة صريحة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:317]

```
318:     fun handleMessage(routed: RoutedPacket)
```
> تُعلَن دالة اسمها معالجة-الرسالة (handleMessage) تأخذ وسيطاً routed من نوع RoutedPacket دون قيمة مُعادة صريحة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:318]

```
319:     fun handleLeave(routed: RoutedPacket)
```
> تُعلَن دالة اسمها معالجة-المغادرة (handleLeave) تأخذ وسيطاً routed من نوع RoutedPacket دون قيمة مُعادة صريحة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:319]

```
320:     fun handleFragment(packet: BitchatPacket): BitchatPacket?
```
> تُعلَن دالة اسمها معالجة-الشظية (handleFragment) تأخذ وسيطاً packet من نوع BitchatPacket وتُعيد BitchatPacket قابلة للفراغ (nullable). [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:320]

```
321:     fun handleRequestSync(routed: RoutedPacket)
```
> تُعلَن دالة اسمها معالجة-طلب-المزامنة (handleRequestSync) تأخذ وسيطاً routed من نوع RoutedPacket دون قيمة مُعادة صريحة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:321]

```
322:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:322]

```
323:     // Communication
```
> تعليق: الاتصال. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:323]

```
324:     fun sendAnnouncementToPeer(peerID: String)
```
> تُعلَن دالة اسمها إرسال-الإعلان-إلى-الند (sendAnnouncementToPeer) تأخذ وسيطاً peerID من نوع String دون قيمة مُعادة صريحة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:324]

```
325:     fun sendCachedMessages(peerID: String)
```
> تُعلَن دالة اسمها إرسال-الرسائل-المخزَّنة (sendCachedMessages) تأخذ وسيطاً peerID من نوع String دون قيمة مُعادة صريحة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:325]

```
326:     fun relayPacket(routed: RoutedPacket)
```
> تُعلَن دالة اسمها تمرير-الحُزمة (relayPacket) تأخذ وسيطاً routed من نوع RoutedPacket دون قيمة مُعادة صريحة. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:326]

```
327:     fun sendToPeer(peerID: String, routed: RoutedPacket): Boolean
```
> تُعلَن دالة اسمها الإرسال-إلى-الند (sendToPeer) تأخذ وسيطاً peerID من نوع String ووسيطاً routed من نوع RoutedPacket وتُعيد قيمة Boolean. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:327]

```
328: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketProcessor.kt:328]
