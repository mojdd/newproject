# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt (الأسطر 201–243)

```
201:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:201]

```
202:                val hasMatch = requiredValues.any { requiredValue ->
```
> يُعرَّف متغيّر ثابت اسمه «يوجد تطابق» (hasMatch) وتُسنَد إليه نتيجة استدعاء الدالّة «أيّ واحد» (any) على المجموعة «القيم المطلوبة» (requiredValues)، حيث يُسمّى كل عنصر في الفحص «القيمة المطلوبة» (requiredValue). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:202]

```
203:                    eventValues.contains(requiredValue)
```
> داخل الفحص، يُستدعى التابع «يحتوي» (contains) على المجموعة «قيم الحدث» (eventValues) ويُمرَّر إليه «القيمة المطلوبة» (requiredValue)، ويُعاد ناتجه كقيمة شرط الفحص. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:203]

```
204:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:204]

```
205:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:205]

```
206:                if (!hasMatch) {
```
> تُفتَح جملة شرطية «إذا» (if) تتحقّق من نفي قيمة «يوجد تطابق» (hasMatch)، أي إذا كانت قيمته «غير صحيح». [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:206]

```
207:                    return false
```
> تُعيد الدالّة القيمة «غير صحيح» (false). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:207]

```
208:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:208]

```
209:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:209]

```
210:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:210]

```
211:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:211]

```
212:        return true
```
> تُعيد الدالّة القيمة «صحيح» (true). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:212]

```
213:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:213]

```
214:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:214]

```
215:    /**
```
> تعليق: بداية تعليق توثيقي (Javadoc/KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:215]

```
216:     * Get debug description
```
> تعليق: احصل على وصف التنقيح (debug description). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:216]

```
217:     */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:217]

```
218:    fun getDebugDescription(): String {
```
> تُعرَّف دالّة اسمها «احصل على وصف التنقيح» (getDebugDescription) بلا وُسطاء، ونوع المُعاد منها سلسلة نصّية (String). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:218]

```
219:        val parts = mutableListOf<String>()
```
> يُعرَّف متغيّر ثابت اسمه «الأجزاء» (parts) وتُسنَد إليه قائمة قابلة للتعديل (mutableListOf) من سلاسل نصّية (String) فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:219]

```
220:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:220]

```
221:        ids?.let { parts.add("ids=${it.size}") }
```
> على الخاصية «المعرّفات» (ids) إن لم تكن خالية (?.let) يُضاف إلى «الأجزاء» (parts) نصّ «ids=» متبوعاً بحجم (size) القيمة. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:221]

```
222:        authors?.let { parts.add("authors=${it.size}") }
```
> على الخاصية «المؤلّفون» (authors) إن لم تكن خالية (?.let) يُضاف إلى «الأجزاء» (parts) نصّ «authors=» متبوعاً بحجم (size) القيمة. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:222]

```
223:        kinds?.let { parts.add("kinds=$it") }
```
> على الخاصية «الأنواع» (kinds) إن لم تكن خالية (?.let) يُضاف إلى «الأجزاء» (parts) نصّ «kinds=» متبوعاً بالقيمة نفسها. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:223]

```
224:        since?.let { parts.add("since=$it") }
```
> على الخاصية «منذ» (since) إن لم تكن خالية (?.let) يُضاف إلى «الأجزاء» (parts) نصّ «since=» متبوعاً بالقيمة نفسها. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:224]

```
225:        until?.let { parts.add("until=$it") }
```
> على الخاصية «حتى» (until) إن لم تكن خالية (?.let) يُضاف إلى «الأجزاء» (parts) نصّ «until=» متبوعاً بالقيمة نفسها. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:225]

```
226:        limit?.let { parts.add("limit=$it") }
```
> على الخاصية «الحدّ» (limit) إن لم تكن خالية (?.let) يُضاف إلى «الأجزاء» (parts) نصّ «limit=» متبوعاً بالقيمة نفسها. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:226]

```
227:        tagFilters?.let { filters ->
```
> على الخاصية «مرشّحات الوسوم» (tagFilters) إن لم تكن خالية (?.let) يُنفَّذ مقطع، ويُسمّى محتواها داخل المقطع «المرشّحات» (filters). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:227]

```
228:            filters.forEach { (tag, values) ->
```
> يُستدعى التابع «لكلّ» (forEach) على «المرشّحات» (filters)، ويُفكَّك كل عنصر إلى «وسم» (tag) و«قيم» (values). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:228]

```
229:                parts.add("#$tag=${values.size}")
```
> يُضاف إلى «الأجزاء» (parts) نصّ يبدأ بـ «#» متبوعاً بقيمة «الوسم» (tag) ثم «=» ثم حجم (size) «القيم» (values). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:229]

```
230:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:230]

```
231:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:231]

```
232:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:232]

```
233:        return "NostrFilter(${parts.joinToString(", ")})"
```
> تُعيد الدالّة سلسلة نصّية تبدأ بـ «NostrFilter(» ثم نتيجة وصل عناصر «الأجزاء» (parts) بفاصل «, » عبر التابع «اوصل-إلى-نص» (joinToString) ثم «)». [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:233]

```
234:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:234]

```
235:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:235]

```
236:    /**
```
> تعليق: بداية تعليق توثيقي (Javadoc/KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:236]

```
237:     * Get geohash value from g tag filter (if present)
```
> تعليق: احصل على قيمة الترميز الجغرافي (geohash) من مرشّح الوسم «g» (إن وُجد). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:237]

```
238:     * Returns the first geohash in the filter or null if none
```
> تعليق: يُعيد أوّل ترميز جغرافي (geohash) في المرشّح، أو قيمة خالية (null) إن لم يوجد. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:238]

```
239:     */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:239]

```
240:    fun getGeohash(): String? {
```
> تُعرَّف دالّة اسمها «احصل على الترميز الجغرافي» (getGeohash) بلا وُسطاء، ونوع المُعاد منها سلسلة نصّية قابلة لأن تكون خالية (?String). [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:240]

```
241:        return tagFilters?.get("g")?.firstOrNull()
```
> تُعيد الدالّة نتيجة استدعاء التابع «احصل» (get) بالمفتاح «g» على «مرشّحات الوسوم» (tagFilters) إن لم تكن خالية، ثم التابع «أوّل عنصر أو خالي» (firstOrNull) على الناتج إن لم يكن خالياً. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:241]

```
242:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:242]

```
243:}
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrFilter.kt:243]
