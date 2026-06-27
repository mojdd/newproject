# شريحة — app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt (الأسطر 201–398)

```
201:                     val maxActive = com.bitchat.android.util.AppConstants.Fragmentation.MAX_ACTIVE_FRAGMENT_SETS
```
> يُعرَّف متغيّر ثابت محلي اسمه «أقصى عدد نشط» (maxActive) ويُسنَد إليه الثابت MAX_ACTIVE_FRAGMENT_SETS من الكائن AppConstants.Fragmentation. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:201]

```
202:                     if (incomingFragments.size >= maxActive) {
```
> شرط: إذا كان حجم خريطة الشظايا الواردة (incomingFragments) أكبر من أو يساوي قيمة maxActive. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:202]

```
203:                         Log.w(TAG, "Rejecting new fragment set $fragmentIDString: active fragment sets ${incomingFragments.size} >= $maxActive")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم TAG ونص يفيد رفض مجموعة شظايا جديدة باسم fragmentIDString مع ذكر حجم الشظايا الواردة وقيمة maxActive. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:203]

```
204:                         return null
```
> يُعاد null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:204]

```
205:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:205]

```
206: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:206]

```
207:                     incomingFragments[fragmentIDString] = mutableMapOf()
```
> يُسنَد إلى المفتاح fragmentIDString داخل incomingFragments خريطة قابلة للتعديل فارغة (mutableMapOf). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:207]

```
208:                     fragmentMetadata[fragmentIDString] = Triple(
```
> يُسنَد إلى المفتاح fragmentIDString داخل بيانات وصف الشظايا (fragmentMetadata) ثلاثية (Triple) تبدأ هنا. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:208]

```
209:                         fragmentPayload.originalType,
```
> العنصر الأول للثلاثية: النوع الأصلي (originalType) من حمولة الشظية (fragmentPayload). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:209]

```
210:                         fragmentPayload.total,
```
> العنصر الثاني للثلاثية: المجموع (total) من حمولة الشظية. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:210]

```
211:                         System.currentTimeMillis()
```
> العنصر الثالث للثلاثية: الوقت الحالي بالمللي ثانية عبر System.currentTimeMillis(). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:211]

```
212:                     )
```
> إغلاق قوس استدعاء الثلاثية Triple. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:212]

```
213:                     fragmentCumulativeSize[fragmentIDString] = 0
```
> يُسنَد إلى المفتاح fragmentIDString داخل الحجم التراكمي للشظايا (fragmentCumulativeSize) القيمة صفر. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:213]

```
214:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:214]

```
215: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:215]

```
216:                 val fragmentMap = incomingFragments[fragmentIDString]
```
> يُعرَّف متغيّر محلي اسمه خريطة الشظايا (fragmentMap) ويُسنَد إليه القيمة المخزّنة في incomingFragments عند المفتاح fragmentIDString. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:216]

```
217:                 if (fragmentMap == null) {
```
> شرط: إذا كانت fragmentMap تساوي null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:217]

```
218:                     Log.w(TAG, "Dropping fragment set $fragmentIDString due to missing fragment map")
```
> يُستدعى تسجيل تحذير بالوسم TAG ونص يفيد إسقاط مجموعة الشظايا fragmentIDString بسبب فقدان خريطة الشظايا. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:218]

```
219:                     removeFragmentSetLocked(fragmentIDString)
```
> يُستدعى الإجراء removeFragmentSetLocked على fragmentIDString. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:219]

```
220:                     return null
```
> يُعاد null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:220]

```
221:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:221]

```
222: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:222]

```
223:                 val currentSize = fragmentCumulativeSize[fragmentIDString]
```
> يُعرَّف متغيّر محلي اسمه الحجم الحالي (currentSize) ويُسنَد إليه القيمة المخزّنة في fragmentCumulativeSize عند المفتاح fragmentIDString. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:223]

```
224:                 if (currentSize == null) {
```
> شرط: إذا كانت currentSize تساوي null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:224]

```
225:                     Log.w(TAG, "Dropping fragment set $fragmentIDString due to missing size tracker")
```
> يُستدعى تسجيل تحذير بالوسم TAG ونص يفيد إسقاط مجموعة الشظايا fragmentIDString بسبب فقدان متتبّع الحجم. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:225]

```
226:                     removeFragmentSetLocked(fragmentIDString)
```
> يُستدعى الإجراء removeFragmentSetLocked على fragmentIDString. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:226]

```
227:                     return null
```
> يُعاد null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:227]

```
228:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:228]

```
229: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:229]

```
230:                 val oldEntrySize = fragmentMap[fragmentPayload.index]?.size ?: 0
```
> يُعرَّف متغيّر محلي اسمه حجم المدخل القديم (oldEntrySize) ويُسنَد إليه حجم (size) العنصر في fragmentMap عند الفهرس fragmentPayload.index، أو صفر إذا كان null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:230]

```
231:                 val newSize = currentSize - oldEntrySize + fragmentPayload.data.size
```
> يُعرَّف متغيّر محلي اسمه الحجم الجديد (newSize) ويُسنَد إليه الحجم الحالي ناقص حجم المدخل القديم زائد حجم بيانات الحمولة (fragmentPayload.data.size). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:231]

```
232:                 val maxTotalBytes = com.bitchat.android.util.AppConstants.Fragmentation.MAX_FRAGMENT_TOTAL_BYTES
```
> يُعرَّف متغيّر محلي اسمه أقصى مجموع بايتات (maxTotalBytes) ويُسنَد إليه الثابت MAX_FRAGMENT_TOTAL_BYTES من AppConstants.Fragmentation. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:232]

```
233:                 if (newSize > maxTotalBytes) {
```
> شرط: إذا كان newSize أكبر من maxTotalBytes. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:233]

```
234:                     Log.w(TAG, "Rejecting fragment for $fragmentIDString: cumulative size $newSize exceeds cap $maxTotalBytes")
```
> يُستدعى تسجيل تحذير بالوسم TAG ونص يفيد رفض شظية لـ fragmentIDString لأن الحجم التراكمي newSize يتجاوز السقف maxTotalBytes. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:234]

```
235:                     removeFragmentSetLocked(fragmentIDString)
```
> يُستدعى الإجراء removeFragmentSetLocked على fragmentIDString. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:235]

```
236:                     return null
```
> يُعاد null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:236]

```
237:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:237]

```
238: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:238]

```
239:                 val delta = (fragmentPayload.data.size - oldEntrySize).toLong()
```
> يُعرَّف متغيّر محلي اسمه الفرق (delta) ويُسنَد إليه حجم بيانات الحمولة ناقص حجم المدخل القديم محوّلاً إلى نوع طويل (toLong). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:239]

```
240:                 val maxGlobalBytes = com.bitchat.android.util.AppConstants.Fragmentation.MAX_GLOBAL_FRAGMENT_TOTAL_BYTES
```
> يُعرَّف متغيّر محلي اسمه أقصى بايتات عامة (maxGlobalBytes) ويُسنَد إليه الثابت MAX_GLOBAL_FRAGMENT_TOTAL_BYTES من AppConstants.Fragmentation. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:240]

```
241:                 if (globalBufferedBytes + delta > maxGlobalBytes) {
```
> شرط: إذا كان مجموع البايتات العامة المخزّنة مؤقتاً (globalBufferedBytes) زائد delta أكبر من maxGlobalBytes. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:241]

```
242:                     Log.w(
```
> يُستدعى تسجيل تحذير (Log.w) ويبدأ قوس وسائطه هنا. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:242]

```
243:                         TAG,
```
> الوسيط الأول: الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:243]

```
244:                         "Rejecting fragment for $fragmentIDString: global buffered bytes ${(globalBufferedBytes + delta)} exceeds cap $maxGlobalBytes"
```
> الوسيط الثاني: نص يفيد رفض شظية لـ fragmentIDString لأن مجموع البايتات العامة المخزّنة (globalBufferedBytes + delta) يتجاوز السقف maxGlobalBytes. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:244]

```
245:                     )
```
> إغلاق قوس استدعاء Log.w. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:245]

```
246:                     if (isNewSet) {
```
> شرط: إذا كان المتغيّر «مجموعة جديدة» (isNewSet) صحيحاً. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:246]

```
247:                         removeFragmentSetLocked(fragmentIDString)
```
> يُستدعى الإجراء removeFragmentSetLocked على fragmentIDString. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:247]

```
248:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:248]

```
249:                     return null
```
> يُعاد null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:249]

```
250:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:250]

```
251: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:251]

```
252:                 fragmentMap[fragmentPayload.index] = fragmentPayload.data
```
> يُسنَد إلى fragmentMap عند الفهرس fragmentPayload.index قيمة بيانات الحمولة fragmentPayload.data. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:252]

```
253:                 fragmentCumulativeSize[fragmentIDString] = newSize
```
> يُسنَد إلى fragmentCumulativeSize عند المفتاح fragmentIDString القيمة newSize. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:253]

```
254:                 globalBufferedBytes += delta
```
> تُزاد قيمة globalBufferedBytes بمقدار delta. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:254]

```
255: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:255]

```
256:                 val expectedTotal = fragmentMetadata[fragmentIDString]?.second ?: fragmentPayload.total
```
> يُعرَّف متغيّر محلي اسمه المجموع المتوقّع (expectedTotal) ويُسنَد إليه العنصر الثاني (second) للثلاثية في fragmentMetadata عند fragmentIDString، أو fragmentPayload.total إذا كان null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:256]

```
257:                 if (fragmentMap.size == expectedTotal) {
```
> شرط: إذا كان حجم fragmentMap يساوي expectedTotal. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:257]

```
258:                     Log.d(TAG, "All fragments received for $fragmentIDString, reassembling...")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم TAG ونص يفيد استلام كل الشظايا لـ fragmentIDString وأنه يُعاد التجميع. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:258]

```
259: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:259]

```
260:                     // iOS reassembly logic: for i in 0..<total { if let fragment = fragments[i] { reassembled.append(fragment) } }
```
> تعليق: منطق إعادة التجميع في iOS: for i in 0..<total { if let fragment = fragments[i] { reassembled.append(fragment) } }. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:260]

```
261:                     val reassembledData = mutableListOf<Byte>()
```
> يُعرَّف متغيّر محلي اسمه بيانات معاد تجميعها (reassembledData) ويُسنَد إليه قائمة بايتات قابلة للتعديل فارغة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:261]

```
262:                     for (i in 0 until expectedTotal) {
```
> حلقة تكرار: المتغيّر i من 0 حتى expectedTotal (غير شامل). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:262]

```
263:                         fragmentMap[i]?.let { data ->
```
> إن لم يكن fragmentMap عند الفهرس i يساوي null، يُنفَّذ بلوك let بمعامل اسمه data. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:263]

```
264:                             reassembledData.addAll(data.asIterable())
```
> تُضاف كل عناصر data (محوّلة عبر asIterable) إلى reassembledData. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:264]

```
265:                         }
```
> إغلاق نطاق بلوك let. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:265]

```
266:                     }
```
> إغلاق نطاق حلقة التكرار. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:266]

```
267: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:267]

```
268:                     val originalPacket = BitchatPacket.fromBinaryData(reassembledData.toByteArray())
```
> يُعرَّف متغيّر محلي اسمه الرزمة الأصلية (originalPacket) ويُسنَد إليه ناتج استدعاء BitchatPacket.fromBinaryData على reassembledData محوّلة إلى مصفوفة بايتات (toByteArray). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:268]

```
269:                     if (originalPacket != null) {
```
> شرط: إذا كانت originalPacket لا تساوي null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:269]

```
270:                         removeFragmentSetLocked(fragmentIDString)
```
> يُستدعى الإجراء removeFragmentSetLocked على fragmentIDString. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:270]

```
271: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:271]

```
272:                         val suppressedTtlPacket = originalPacket.copy(ttl = 0u.toUByte())
```
> يُعرَّف متغيّر محلي اسمه رزمة مكبوتة العمر (suppressedTtlPacket) ويُسنَد إليه نسخة (copy) من originalPacket مع ضبط ttl إلى 0 محوّلاً إلى UByte عبر 0u.toUByte(). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:272]

```
273:                         Log.d(TAG, "Successfully reassembled original (${reassembledData.size} bytes); set TTL=0 to suppress relay")
```
> يُستدعى تسجيل تصحيح بالوسم TAG ونص يفيد نجاح إعادة تجميع الأصل مع حجم reassembledData بالبايت وضبط TTL=0 لكبت الترحيل. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:273]

```
274:                         return suppressedTtlPacket
```
> يُعاد suppressedTtlPacket. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:274]

```
275:                     } else {
```
> وإلا (else لشرط originalPacket != null). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:275]

```
276:                         val metadata = fragmentMetadata[fragmentIDString]
```
> يُعرَّف متغيّر محلي اسمه بيانات الوصف (metadata) ويُسنَد إليه القيمة في fragmentMetadata عند fragmentIDString. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:276]

```
277:                         Log.e(TAG, "Failed to decode reassembled packet (type=${metadata?.first}, total=${metadata?.second})")
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم TAG ونص يفيد فشل فك ترميز الرزمة المعاد تجميعها مع ذكر العنصر الأول (type) والثاني (total) من metadata. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:277]

```
278:                     }
```
> إغلاق نطاق else. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:278]

```
279:                 } else {
```
> وإلا (else لشرط fragmentMap.size == expectedTotal). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:279]

```
280:                     val received = fragmentMap.size
```
> يُعرَّف متغيّر محلي اسمه المُستلَم (received) ويُسنَد إليه حجم fragmentMap. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:280]

```
281:                     Log.d(TAG, "Fragment ${fragmentPayload.index} stored, have $received/$expectedTotal fragments for $fragmentIDString")
```
> يُستدعى تسجيل تصحيح بالوسم TAG ونص يفيد تخزين الشظية ذات الفهرس fragmentPayload.index مع ذكر received من expectedTotal شظايا لـ fragmentIDString. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:281]

```
282:                 }
```
> إغلاق نطاق else. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:282]

```
283:             }
```
> إغلاق نطاق (نطاق المزامنة synchronized). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:283]

```
284:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:284]

```
285:         } catch (e: Exception) {
```
> بلوك التقاط استثناء (catch) بمعامل اسمه e من نوع Exception. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:285]

```
286:             Log.e(TAG, "Failed to handle fragment: ${e.message}")
```
> يُستدعى تسجيل خطأ بالوسم TAG ونص يفيد فشل معالجة شظية مع رسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:286]

```
287:         }
```
> إغلاق نطاق catch. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:287]

```
288:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:288]

```
289:         return null
```
> يُعاد null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:289]

```
290:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:290]

```
291: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:291]

```
292:     private fun removeFragmentSetLocked(fragmentIDString: String) {
```
> تُعرَّف دالة خاصة (private) اسمها removeFragmentSetLocked تأخذ معاملاً fragmentIDString من نوع String. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:292]

```
293:         incomingFragments.remove(fragmentIDString)
```
> يُحذَف المدخل عند المفتاح fragmentIDString من incomingFragments. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:293]

```
294:         fragmentMetadata.remove(fragmentIDString)
```
> يُحذَف المدخل عند المفتاح fragmentIDString من fragmentMetadata. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:294]

```
295:         val bytes = fragmentCumulativeSize.remove(fragmentIDString)?.toLong() ?: 0L
```
> يُعرَّف متغيّر محلي اسمه بايتات (bytes) ويُسنَد إليه القيمة المحذوفة من fragmentCumulativeSize عند fragmentIDString محوّلة إلى Long، أو 0L إذا كانت null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:295]

```
296:         if (bytes != 0L) {
```
> شرط: إذا كانت bytes لا تساوي 0L. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:296]

```
297:             globalBufferedBytes = (globalBufferedBytes - bytes).coerceAtLeast(0L)
```
> يُسنَد إلى globalBufferedBytes ناتج طرح bytes منها مقيّداً بحد أدنى 0L عبر coerceAtLeast. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:297]

```
298:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:298]

```
299:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:299]

```
300:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:300]

```
301:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:301]

```
302:      * Helper function to match iOS stride functionality
```
> تعليق: دالة مساعدة لمطابقة وظيفة stride في iOS. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:302]

```
303:      * stride(from: 0, to: fullData.count, by: maxFragmentSize)
```
> تعليق: stride(from: 0, to: fullData.count, by: maxFragmentSize). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:303]

```
304:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:304]

```
305:     private fun <T> stride(from: Int, to: Int, by: Int, transform: (Int) -> T): List<T> {
```
> تُعرَّف دالة خاصة معمّمة بمعامل النوع T اسمها stride تأخذ from وto وby من نوع Int ودالة تحويل transform من Int إلى T، وتعيد List<T>. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:305]

```
306:         val result = mutableListOf<T>()
```
> يُعرَّف متغيّر محلي اسمه النتيجة (result) ويُسنَد إليه قائمة قابلة للتعديل فارغة من النوع T. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:306]

```
307:         var current = from
```
> يُعرَّف متغيّر محلي قابل للتغيير اسمه الحالي (current) ويُسنَد إليه قيمة from. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:307]

```
308:         while (current < to) {
```
> حلقة طالما (while): ما دامت current أصغر من to. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:308]

```
309:             result.add(transform(current))
```
> يُضاف إلى result ناتج استدعاء transform على current. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:309]

```
310:             current += by
```
> تُزاد current بمقدار by. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:310]

```
311:         }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:311]

```
312:         return result
```
> يُعاد result. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:312]

```
313:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:313]

```
314:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:314]

```
315:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:315]

```
316:      * iOS cleanup - exactly matching performCleanup() implementation
```
> تعليق: تنظيف iOS - مطابق تماماً لتنفيذ performCleanup(). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:316]

```
317:      * Clean old fragments (> 30 seconds old)
```
> تعليق: تنظيف الشظايا القديمة (أقدم من 30 ثانية). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:317]

```
318:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:318]

```
319:     private fun cleanupOldFragments() {
```
> تُعرَّف دالة خاصة اسمها cleanupOldFragments بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:319]

```
320:         synchronized(fragmentStateLock) {
```
> يُفتَح بلوك مزامنة (synchronized) على القفل fragmentStateLock. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:320]

```
321:             val now = System.currentTimeMillis()
```
> يُعرَّف متغيّر محلي اسمه الآن (now) ويُسنَد إليه الوقت الحالي بالمللي ثانية. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:321]

```
322:             val cutoff = now - FRAGMENT_TIMEOUT
```
> يُعرَّف متغيّر محلي اسمه الحد الفاصل (cutoff) ويُسنَد إليه now ناقص FRAGMENT_TIMEOUT. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:322]

```
323: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:323]

```
324:             // iOS: let oldFragments = fragmentMetadata.filter { $0.value.timestamp < cutoff }.map { $0.key }
```
> تعليق: iOS: let oldFragments = fragmentMetadata.filter { $0.value.timestamp < cutoff }.map { $0.key }. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:324]

```
325:             val oldFragments = fragmentMetadata.filter { it.value.third < cutoff }.map { it.key }
```
> يُعرَّف متغيّر محلي اسمه الشظايا القديمة (oldFragments) ويُسنَد إليه مفاتيح مدخلات fragmentMetadata التي يكون العنصر الثالث (third) لقيمتها أصغر من cutoff، عبر filter ثم map. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:325]

```
326: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:326]

```
327:             for (fragmentID in oldFragments) {
```
> حلقة تكرار: المتغيّر fragmentID على عناصر oldFragments. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:327]

```
328:                 removeFragmentSetLocked(fragmentID)
```
> يُستدعى الإجراء removeFragmentSetLocked على fragmentID. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:328]

```
329:             }
```
> إغلاق نطاق حلقة التكرار. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:329]

```
330: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:330]

```
331:             if (oldFragments.isNotEmpty()) {
```
> شرط: إذا كانت oldFragments غير فارغة (isNotEmpty). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:331]

```
332:                 Log.d(TAG, "Cleaned up ${oldFragments.size} old fragment sets (iOS compatible)")
```
> يُستدعى تسجيل تصحيح بالوسم TAG ونص يفيد تنظيف عدد oldFragments.size من مجموعات الشظايا القديمة (متوافق مع iOS). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:332]

```
333:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:333]

```
334:         }
```
> إغلاق نطاق بلوك المزامنة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:334]

```
335:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:335]

```
336:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:336]

```
337:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:337]

```
338:      * Get debug information - matches iOS debugging
```
> تعليق: الحصول على معلومات التصحيح - يطابق تصحيح iOS. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:338]

```
339:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:339]

```
340:     fun getDebugInfo(): String {
```
> تُعرَّف دالة عامة اسمها getDebugInfo بلا معاملات وتعيد String. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:340]

```
341:         synchronized(fragmentStateLock) {
```
> يُفتَح بلوك مزامنة على القفل fragmentStateLock. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:341]

```
342:             return buildString {
```
> يُعاد ناتج بناء سلسلة عبر buildString ويبدأ بلوكه هنا. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:342]

```
343:                 appendLine("=== Fragment Manager Debug Info (iOS Compatible) ===")
```
> يُستدعى appendLine لإلحاق سطر نصه "=== Fragment Manager Debug Info (iOS Compatible) ===". [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:343]

```
344:                 appendLine("Active Fragment Sets: ${incomingFragments.size}")
```
> يُستدعى appendLine لإلحاق سطر يذكر "Active Fragment Sets" مع حجم incomingFragments. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:344]

```
345:                 appendLine("Fragment Size Threshold: $FRAGMENT_SIZE_THRESHOLD bytes")
```
> يُستدعى appendLine لإلحاق سطر يذكر "Fragment Size Threshold" مع قيمة FRAGMENT_SIZE_THRESHOLD بالبايت. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:345]

```
346:                 appendLine("Max Fragment Size: $MAX_FRAGMENT_SIZE bytes")
```
> يُستدعى appendLine لإلحاق سطر يذكر "Max Fragment Size" مع قيمة MAX_FRAGMENT_SIZE بالبايت. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:346]

```
347:                 appendLine("Global Buffered Bytes: $globalBufferedBytes")
```
> يُستدعى appendLine لإلحاق سطر يذكر "Global Buffered Bytes" مع قيمة globalBufferedBytes. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:347]

```
348: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:348]

```
349:                 fragmentMetadata.forEach { (fragmentID, metadata) ->
```
> يُستدعى forEach على fragmentMetadata بمعاملين مفكّكين هما fragmentID وmetadata. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:349]

```
350:                     val (originalType, totalFragments, timestamp) = metadata
```
> يُفكَّك metadata إلى ثلاثة متغيّرات: النوع الأصلي (originalType) ومجموع الشظايا (totalFragments) والطابع الزمني (timestamp). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:350]

```
351:                     val received = incomingFragments[fragmentID]?.size ?: 0
```
> يُعرَّف متغيّر محلي اسمه المُستلَم (received) ويُسنَد إليه حجم incomingFragments عند fragmentID، أو صفر إذا كان null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:351]

```
352:                     val ageSeconds = (System.currentTimeMillis() - timestamp) / 1000
```
> يُعرَّف متغيّر محلي اسمه العمر بالثواني (ageSeconds) ويُسنَد إليه الوقت الحالي ناقص timestamp مقسوماً على 1000. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:352]

```
353:                     val bytes = fragmentCumulativeSize[fragmentID] ?: 0
```
> يُعرَّف متغيّر محلي اسمه بايتات (bytes) ويُسنَد إليه قيمة fragmentCumulativeSize عند fragmentID، أو صفر إذا كان null. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:353]

```
354:                     appendLine("  - $fragmentID: $received/$totalFragments fragments, bytes=$bytes, type: $originalType, age: ${ageSeconds}s")
```
> يُستدعى appendLine لإلحاق سطر يذكر fragmentID وreceived من totalFragments وbytes وoriginalType وageSeconds. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:354]

```
355:                 }
```
> إغلاق نطاق بلوك forEach. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:355]

```
356:             }
```
> إغلاق نطاق بلوك buildString. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:356]

```
357:         }
```
> إغلاق نطاق بلوك المزامنة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:357]

```
358:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:358]

```
359:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:359]

```
360:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:360]

```
361:      * Start periodic cleanup of old fragments - matches iOS maintenance timer
```
> تعليق: بدء التنظيف الدوري للشظايا القديمة - يطابق مؤقّت الصيانة في iOS. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:361]

```
362:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:362]

```
363:     private fun startPeriodicCleanup() {
```
> تُعرَّف دالة خاصة اسمها startPeriodicCleanup بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:363]

```
364:         managerScope.launch {
```
> يُستدعى launch على نطاق المدير (managerScope) ويبدأ بلوك الكوروتين هنا. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:364]

```
365:             while (isActive) {
```
> حلقة طالما (while): ما دام isActive صحيحاً. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:365]

```
366:                 delay(CLEANUP_INTERVAL)
```
> يُستدعى التعليق المؤقّت (delay) بمقدار CLEANUP_INTERVAL. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:366]

```
367:                 cleanupOldFragments()
```
> يُستدعى الإجراء cleanupOldFragments. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:367]

```
368:             }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:368]

```
369:         }
```
> إغلاق نطاق بلوك الكوروتين launch. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:369]

```
370:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:370]

```
371:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:371]

```
372:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:372]

```
373:      * Clear all fragments
```
> تعليق: مسح كل الشظايا. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:373]

```
374:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:374]

```
375:     fun clearAllFragments() {
```
> تُعرَّف دالة عامة اسمها clearAllFragments بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:375]

```
376:         synchronized(fragmentStateLock) {
```
> يُفتَح بلوك مزامنة على القفل fragmentStateLock. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:376]

```
377:             incomingFragments.clear()
```
> يُمسَح محتوى incomingFragments عبر clear. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:377]

```
378:             fragmentMetadata.clear()
```
> يُمسَح محتوى fragmentMetadata عبر clear. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:378]

```
379:             fragmentCumulativeSize.clear()
```
> يُمسَح محتوى fragmentCumulativeSize عبر clear. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:379]

```
380:             globalBufferedBytes = 0L
```
> يُسنَد إلى globalBufferedBytes القيمة 0L. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:380]

```
381:         }
```
> إغلاق نطاق بلوك المزامنة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:381]

```
382:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:382]

```
383:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:383]

```
384:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:384]

```
385:      * Shutdown the manager
```
> تعليق: إيقاف المدير. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:385]

```
386:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:386]

```
387:     fun shutdown() {
```
> تُعرَّف دالة عامة اسمها shutdown بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:387]

```
388:         managerScope.cancel()
```
> يُستدعى cancel على managerScope. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:388]

```
389:         clearAllFragments()
```
> يُستدعى الإجراء clearAllFragments. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:389]

```
390:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:390]

```
391: }
```
> إغلاق نطاق الصنف (class FragmentManager). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:391]

```
392: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:392]

```
393: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:393]

```
394:  * Delegate interface for fragment manager callbacks
```
> تعليق: واجهة مفوّض لردود نداء مدير الشظايا. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:394]

```
395:  */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:395]

```
396: interface FragmentManagerDelegate {
```
> تُعرَّف واجهة (interface) اسمها FragmentManagerDelegate. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:396]

```
397:     fun onPacketReassembled(packet: BitchatPacket)
```
> يُعرَّف توقيع دالة اسمها onPacketReassembled تأخذ معاملاً packet من نوع BitchatPacket. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:397]

```
398: }
```
> إغلاق نطاق الواجهة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:398]
