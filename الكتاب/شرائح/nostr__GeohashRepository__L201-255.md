# شريحة — app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt (الأسطر 201–255)

```
201:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:201]

```
202:         val nick = geoNicknames[lower] ?: "anon"
```
> تعريف قيمة ثابتة اسمها (nick) تساوي القيمة الموجودة في خريطة الأسماء الجغرافية (geoNicknames) عند المفتاح (lower)، وإن كانت معدومة (null) تساوي النص "anon". [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:202]

```
203:         return "$nick#$suffix"
```
> يُعيد نصاً مكوناً من قيمة (nick) ثم علامة (#) ثم قيمة اللاحقة (suffix). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:203]

```
204:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:204]

```
205: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:205]

```
206:     fun displayNameForNostrPubkeyUI(pubkeyHex: String): String {
```
> تعريف دالة (fun) اسمها (displayNameForNostrPubkeyUI) أي اسم العرض لمفتاح نوستر العام للواجهة، تأخذ وسيطاً اسمه (pubkeyHex) من نوع نص (String) وتُعيد نصاً (String). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:206]

```
207:         val lower = pubkeyHex.lowercase()
```
> تعريف قيمة ثابتة اسمها (lower) تساوي الوسيط (pubkeyHex) بعد تحويله إلى حروف صغيرة عبر الدالة (lowercase). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:207]

```
208:         val suffix = pubkeyHex.takeLast(4)
```
> تعريف قيمة ثابتة اسمها (suffix) أي اللاحقة تساوي آخر أربعة محارف من الوسيط (pubkeyHex) عبر الدالة (takeLast) بالقيمة 4. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:208]

```
209:         val current = currentGeohash
```
> تعريف قيمة ثابتة اسمها (current) تساوي قيمة المتغير (currentGeohash) أي التجزئة الجغرافية الحالية. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:209]

```
210:         val base: String = try {
```
> تعريف قيمة ثابتة اسمها (base) أي الأساس من نوع نص (String) تساوي ناتج كتلة المحاولة (try). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:210]

```
211:             if (current != null) {
```
> شرط: إذا كانت قيمة (current) لا تساوي المعدوم (null). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:211]

```
212:                 val my = NostrIdentityBridge.deriveIdentity(current, application)
```
> تعريف قيمة ثابتة اسمها (my) تساوي ناتج استدعاء الدالة (deriveIdentity) أي اشتقاق الهوية من الكائن (NostrIdentityBridge) بالوسيطين (current) و(application). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:212]

```
213:                 if (my.publicKeyHex.equals(lower, true)) {
```
> شرط: إذا كان الحقل (publicKeyHex) أي المفتاح العام الست عشري من الكائن (my) يساوي القيمة (lower) عبر الدالة (equals) مع تمرير القيمة true لتجاهل حالة الأحرف. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:213]

```
214:                     state.getNicknameValue() ?: "anon"
```
> ناتج استدعاء الدالة (getNicknameValue) أي قيمة الاسم المستعار من الكائن (state)، وإن كان معدوماً (null) فالنص "anon". [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:214]

```
215:                 } else geoNicknames[lower] ?: "anon"
```
> وإلا (else) قيمة خريطة الأسماء الجغرافية (geoNicknames) عند المفتاح (lower)، وإن كانت معدومة (null) فالنص "anon". [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:215]

```
216:             } else geoNicknames[lower] ?: "anon"
```
> وإلا (else) للشرط الخارجي قيمة خريطة الأسماء الجغرافية (geoNicknames) عند المفتاح (lower)، وإن كانت معدومة (null) فالنص "anon". [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:216]

```
217:         } catch (_: Exception) { geoNicknames[lower] ?: "anon" }
```
> كتلة الالتقاط (catch) لأي استثناء (Exception) بمعامل مهمَل، تُعيد قيمة خريطة الأسماء الجغرافية (geoNicknames) عند المفتاح (lower)، وإن كانت معدومة (null) فالنص "anon". [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:217]

```
218:         if (current == null) return base
```
> شرط: إذا كانت قيمة (current) تساوي المعدوم (null) يُعيد قيمة (base). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:218]

```
219:         return try {
```
> يُعيد ناتج كتلة المحاولة (try) التالية. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:219]

```
220:             val cutoff = Date(System.currentTimeMillis() - 5 * 60 * 1000)
```
> تعريف قيمة ثابتة اسمها (cutoff) أي الحد الفاصل تساوي تاريخاً (Date) مبنياً من الوقت الحالي بالمللي ثانية (currentTimeMillis) مطروحاً منه حاصل ضرب 5 في 60 في 1000. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:220]

```
221:             val participants = geohashParticipants[current] ?: emptyMap()
```
> تعريف قيمة ثابتة اسمها (participants) أي المشاركون تساوي قيمة خريطة مشاركي التجزئة الجغرافية (geohashParticipants) عند المفتاح (current)، وإن كانت معدومة (null) فخريطة فارغة (emptyMap). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:221]

```
222:             var count = 0
```
> تعريف متغير قابل للتغيير اسمه (count) أي العدّاد يساوي 0. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:222]

```
223:             for ((k, t) in participants) {
```
> حلقة تكرار (for) على عناصر (participants) بتفكيك كل عنصر إلى مفتاح (k) وقيمة (t). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:223]

```
224:                 if (dataManager.isGeohashUserBlocked(k)) continue
```
> شرط: إذا أعادت الدالة (isGeohashUserBlocked) أي هل مستخدم التجزئة الجغرافية محظور من الكائن (dataManager) قيمة صحيحة للمفتاح (k) فتابِع (continue) إلى الدورة التالية. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:224]

```
225:                 if (t.before(cutoff)) continue
```
> شرط: إذا كانت القيمة (t) سابقة (before) للحد الفاصل (cutoff) فتابِع (continue) إلى الدورة التالية. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:225]

```
226:                 val name = if (k.equals(lower, true)) base else (geoNicknames[k.lowercase()] ?: "anon")
```
> تعريف قيمة ثابتة اسمها (name) تساوي: إذا كان المفتاح (k) يساوي (lower) عبر (equals) مع تجاهل حالة الأحرف فقيمة (base)، وإلا قيمة خريطة الأسماء الجغرافية (geoNicknames) عند المفتاح (k) بحروف صغيرة (lowercase)، وإن كانت معدومة (null) فالنص "anon". [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:226]

```
227:                 if (name.equals(base, true)) { count++; if (count > 1) break }
```
> شرط: إذا كان (name) يساوي (base) عبر (equals) مع تجاهل حالة الأحرف فزِد العدّاد (count) بواحد، وإذا صار العدّاد أكبر من 1 فاكسر الحلقة (break). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:227]

```
228:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:228]

```
229:             if (!participants.containsKey(lower)) count += 1
```
> شرط: إذا لم تحتوِ (containsKey) خريطة (participants) على المفتاح (lower) فزِد العدّاد (count) بمقدار 1. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:229]

```
230:             if (count > 1) "$base#$suffix" else base
```
> شرط: إذا كان العدّاد (count) أكبر من 1 فالنص المكوّن من (base) ثم علامة (#) ثم (suffix)، وإلا قيمة (base). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:230]

```
231:         } catch (_: Exception) { base }
```
> كتلة الالتقاط (catch) لأي استثناء (Exception) بمعامل مهمَل، تُعيد قيمة (base). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:231]

```
232:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:232]

```
233: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:233]

```
234:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:234]

```
235:      * Get display name for any geohash (not just current one) for header titles
```
> تعليق: احصل على اسم العرض لأي تجزئة جغرافية (وليس الحالية فقط) لعناوين الترويسة. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:235]

```
236:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:236]

```
237:     fun displayNameForGeohashConversation(pubkeyHex: String, sourceGeohash: String): String {
```
> تعريف دالة (fun) اسمها (displayNameForGeohashConversation) أي اسم العرض لمحادثة التجزئة الجغرافية، تأخذ وسيطين هما (pubkeyHex) و(sourceGeohash) كلاهما نص (String) وتُعيد نصاً (String). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:237]

```
238:         val lower = pubkeyHex.lowercase()
```
> تعريف قيمة ثابتة اسمها (lower) تساوي الوسيط (pubkeyHex) بعد تحويله إلى حروف صغيرة عبر الدالة (lowercase). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:238]

```
239:         val suffix = pubkeyHex.takeLast(4)
```
> تعريف قيمة ثابتة اسمها (suffix) أي اللاحقة تساوي آخر أربعة محارف من الوسيط (pubkeyHex) عبر الدالة (takeLast) بالقيمة 4. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:239]

```
240:         val base = geoNicknames[lower] ?: "anon"
```
> تعريف قيمة ثابتة اسمها (base) أي الأساس تساوي قيمة خريطة الأسماء الجغرافية (geoNicknames) عند المفتاح (lower)، وإن كانت معدومة (null) فالنص "anon". [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:240]

```
241:         return try {
```
> يُعيد ناتج كتلة المحاولة (try) التالية. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:241]

```
242:             val cutoff = Date(System.currentTimeMillis() - 5 * 60 * 1000)
```
> تعريف قيمة ثابتة اسمها (cutoff) أي الحد الفاصل تساوي تاريخاً (Date) مبنياً من الوقت الحالي بالمللي ثانية (currentTimeMillis) مطروحاً منه حاصل ضرب 5 في 60 في 1000. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:242]

```
243:             val participants = geohashParticipants[sourceGeohash] ?: emptyMap()
```
> تعريف قيمة ثابتة اسمها (participants) أي المشاركون تساوي قيمة خريطة مشاركي التجزئة الجغرافية (geohashParticipants) عند المفتاح (sourceGeohash) أي التجزئة الجغرافية المصدر، وإن كانت معدومة (null) فخريطة فارغة (emptyMap). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:243]

```
244:             var count = 0
```
> تعريف متغير قابل للتغيير اسمه (count) أي العدّاد يساوي 0. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:244]

```
245:             for ((k, t) in participants) {
```
> حلقة تكرار (for) على عناصر (participants) بتفكيك كل عنصر إلى مفتاح (k) وقيمة (t). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:245]

```
246:                 if (dataManager.isGeohashUserBlocked(k)) continue
```
> شرط: إذا أعادت الدالة (isGeohashUserBlocked) أي هل مستخدم التجزئة الجغرافية محظور من الكائن (dataManager) قيمة صحيحة للمفتاح (k) فتابِع (continue) إلى الدورة التالية. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:246]

```
247:                 if (t.before(cutoff)) continue
```
> شرط: إذا كانت القيمة (t) سابقة (before) للحد الفاصل (cutoff) فتابِع (continue) إلى الدورة التالية. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:247]

```
248:                 val name = if (k.equals(lower, true)) base else (geoNicknames[k.lowercase()] ?: "anon")
```
> تعريف قيمة ثابتة اسمها (name) تساوي: إذا كان المفتاح (k) يساوي (lower) عبر (equals) مع تجاهل حالة الأحرف فقيمة (base)، وإلا قيمة خريطة الأسماء الجغرافية (geoNicknames) عند المفتاح (k) بحروف صغيرة (lowercase)، وإن كانت معدومة (null) فالنص "anon". [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:248]

```
249:                 if (name.equals(base, true)) { count++; if (count > 1) break }
```
> شرط: إذا كان (name) يساوي (base) عبر (equals) مع تجاهل حالة الأحرف فزِد العدّاد (count) بواحد، وإذا صار العدّاد أكبر من 1 فاكسر الحلقة (break). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:249]

```
250:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:250]

```
251:             if (!participants.containsKey(lower)) count += 1
```
> شرط: إذا لم تحتوِ (containsKey) خريطة (participants) على المفتاح (lower) فزِد العدّاد (count) بمقدار 1. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:251]

```
252:             if (count > 1) "$base#$suffix" else base
```
> شرط: إذا كان العدّاد (count) أكبر من 1 فالنص المكوّن من (base) ثم علامة (#) ثم (suffix)، وإلا قيمة (base). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:252]

```
253:         } catch (_: Exception) { base }
```
> كتلة الالتقاط (catch) لأي استثناء (Exception) بمعامل مهمَل، تُعيد قيمة (base). [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:253]

```
254:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:254]

```
255: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashRepository.kt:255]
