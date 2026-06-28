# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt (الأسطر 201–260)

```
201:         head.next = node
```
> يُسنِد العقدة (node) إلى الحقل التالي (next) للعقدة الرأس (head). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:201]

```
202:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:202]

```
203:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:203]

```
204:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:204]

```
205:      * Remove and return the least recently used node (at the tail)
```
> تعليق: أزِل وأعِد العقدة الأقل استخداماً مؤخراً (least recently used) عند الذيل (tail). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:205]

```
206:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:206]

```
207:     private fun removeTail(): LRUNode? {
```
> يُعرِّف دالة خاصة (private) باسم إزالة الذيل (removeTail) تُعيد عقدة من نوع LRUNode قابلة للقيمة الفارغة (nullable). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:207]

```
208:         val lastNode = tail.prev
```
> يُعرِّف متغيّراً ثابتاً باسم العقدة الأخيرة (lastNode) ويُسنِد إليه الحقل السابق (prev) للذيل (tail). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:208]

```
209:         if (lastNode == head) {
```
> شرط: إذا كانت العقدة الأخيرة (lastNode) تساوي الرأس (head). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:209]

```
210:             return null // Empty list
```
> يُعيد القيمة الفارغة (null). تعليق: قائمة فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:210]

```
211:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:211]

```
212:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:212]

```
213:         // Remove from linked list
```
> تعليق: أزِل من القائمة المتصلة (linked list). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:213]

```
214:         lastNode?.prev?.next = tail
```
> يُسنِد الذيل (tail) إلى الحقل التالي (next) الخاص بالحقل السابق (prev) للعقدة الأخيرة (lastNode)، باستدعاء آمن من القيمة الفارغة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:214]

```
215:         tail.prev = lastNode?.prev
```
> يُسنِد الحقل السابق (prev) للعقدة الأخيرة (lastNode) إلى الحقل السابق (prev) للذيل (tail)، باستدعاء آمن من القيمة الفارغة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:215]

```
216:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:216]

```
217:         // Remove from hash map
```
> تعليق: أزِل من خريطة التجزئة (hash map). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:217]

```
218:         if (lastNode != null) {
```
> شرط: إذا لم تكن العقدة الأخيرة (lastNode) قيمة فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:218]

```
219:             nodeMap.remove(lastNode.eventId)
```
> يستدعي دالة الإزالة (remove) على خريطة العقد (nodeMap) بمفتاح معرّف الحدث (eventId) للعقدة الأخيرة (lastNode). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:219]

```
220:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:220]

```
221:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:221]

```
222:         return lastNode
```
> يُعيد العقدة الأخيرة (lastNode). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:222]

```
223:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:223]

```
224:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:224]

```
225:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:225]

```
226:      * Evict the oldest (least recently used) entries when capacity is exceeded
```
> تعليق: اطرُد المُدخلات الأقدم (الأقل استخداماً مؤخراً) عند تجاوز السعة (capacity). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:226]

```
227:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:227]

```
228:     private fun evictOldest() {
```
> يُعرِّف دالة خاصة (private) باسم طرد الأقدم (evictOldest) بلا قيمة معادة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:228]

```
229:         while (nodeMap.size > maxCapacity) {
```
> حلقة طالما (while): تتكرّر طالما كان حجم (size) خريطة العقد (nodeMap) أكبر من السعة القصوى (maxCapacity). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:229]

```
230:             val evictedNode = removeTail()
```
> يُعرِّف متغيّراً ثابتاً باسم العقدة المطرودة (evictedNode) ويُسنِد إليه ناتج استدعاء دالة إزالة الذيل (removeTail). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:230]

```
231:             if (evictedNode != null) {
```
> شرط: إذا لم تكن العقدة المطرودة (evictedNode) قيمة فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:231]

```
232:                 evictionCount++
```
> يزيد عدّاد الطرد (evictionCount) بمقدار واحد. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:232]

```
233:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:233]

```
234:                 if (evictionCount % 500 == 0L) {
```
> شرط: إذا كان باقي قسمة عدّاد الطرد (evictionCount) على 500 يساوي صفراً من نوع Long. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:234]

```
235:                     Log.v(TAG, "Evicted event ID: ${evictedNode.eventId} (${evictionCount} total evictions)")
```
> يستدعي تسجيل مطوّل (Log.v) بالوسم (TAG) ونص يحوي معرّف الحدث (eventId) للعقدة المطرودة وعدّاد الطرد (evictionCount). نص الرسالة: "معرّف الحدث المطرود: <eventId> (<evictionCount> إجمالي عمليات الطرد)". [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:235]

```
236:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:236]

```
237:             } else {
```
> وإلّا (else). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:237]

```
238:                 break // Should not happen, but safety check
```
> يكسر الحلقة (break). تعليق: لا ينبغي أن يحدث، لكنه فحص أمان. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:238]

```
239:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:239]

```
240:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:240]

```
241:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:241]

```
242: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:242]

```
243: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:243]

```
244: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:244]

```
245:  * Statistics about the deduplication system
```
> تعليق: إحصائيات عن نظام إزالة التكرار (deduplication). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:245]

```
246:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:246]

```
247: data class DeduplicationStats(
```
> يُعرِّف صنف بيانات (data class) باسم إحصائيات إزالة التكرار (DeduplicationStats) ويبدأ قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:247]

```
248:     val capacity: Int,
```
> يُعرِّف خاصية ثابتة باسم السعة (capacity) من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:248]

```
249:     val currentSize: Int,
```
> يُعرِّف خاصية ثابتة باسم الحجم الحالي (currentSize) من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:249]

```
250:     val totalChecks: Long,
```
> يُعرِّف خاصية ثابتة باسم إجمالي الفحوصات (totalChecks) من نوع Long. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:250]

```
251:     val duplicateCount: Long,
```
> يُعرِّف خاصية ثابتة باسم عدّاد التكرار (duplicateCount) من نوع Long. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:251]

```
252:     val evictionCount: Long,
```
> يُعرِّف خاصية ثابتة باسم عدّاد الطرد (evictionCount) من نوع Long. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:252]

```
253:     val hitRate: Double
```
> يُعرِّف خاصية ثابتة باسم معدّل الإصابة (hitRate) من نوع عدد عشري مزدوج (Double). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:253]

```
254: ) {
```
> يُغلق قائمة معاملات الصنف ويبدأ جسمه. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:254]

```
255:     override fun toString(): String {
```
> يُعيد تعريف (override) دالة التحويل إلى نص (toString) التي تُعيد قيمة من نوع نص (String). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:255]

```
256:         return "DeduplicationStats(capacity=$capacity, size=$currentSize, " +
```
> يُعيد نصاً يبدأ بـ "DeduplicationStats(capacity=" متبوعاً بقيمة السعة (capacity) ثم "size=" متبوعاً بقيمة الحجم الحالي (currentSize)، مع وصلٍ بمعامل الجمع النصّي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:256]

```
257:                "checks=$totalChecks, duplicates=$duplicateCount, evictions=$evictionCount, " +
```
> يتابع النص بـ "checks=" متبوعاً بإجمالي الفحوصات (totalChecks) ثم "duplicates=" متبوعاً بعدّاد التكرار (duplicateCount) ثم "evictions=" متبوعاً بعدّاد الطرد (evictionCount)، مع وصلٍ بمعامل الجمع النصّي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:257]

```
258:                "hitRate=${"%.2f".format(hitRate * 100)}%)"
```
> يتابع النص بـ "hitRate=" متبوعاً بقيمة معدّل الإصابة (hitRate) مضروبة في 100 ومنسّقة بمنزلتين عشريتين عبر الصيغة "%.2f"، ثم العلامة "%)". [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:258]

```
259:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:259]

```
260: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:260]
