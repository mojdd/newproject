# شريحة — app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt (الأسطر 201–374)

```
201:             )
```
> قوس إغلاق `)` لاستدعاء أو تعريف بدأ قبل هذا المدى. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:201]

```
202:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:202]

```
203: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:203]

```
204:         favorites[keyHex] = updated
```
> يضع داخل خريطة المفضّلات (favorites) عند المفتاح `keyHex` القيمة `updated`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:204]

```
205:         saveFavorites()
```
> يستدعي دالة حفظ المفضّلات (saveFavorites). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:205]

```
206:         notifyChanged(keyHex)
```
> يستدعي دالة الإبلاغ بالتغيير (notifyChanged) ممرّراً `keyHex`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:206]

```
207: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:207]

```
208:         Log.d(TAG, "Updated favorite status for $nickname: $isFavorite")
```
> يسجّل رسالة تصحيح (Log.d) بالوسم `TAG` نصّها «Updated favorite status for $nickname: $isFavorite» مع إدراج قيمة `nickname` وقيمة `isFavorite`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:208]

```
209:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:209]

```
210: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:210]

```
211:     /** Update peer favorited-us flag */
```
> تعليق: تحديث راية «النظير فضّلنا» (favorited-us). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:211]

```
212:     fun updatePeerFavoritedUs(noisePublicKey: ByteArray, theyFavoritedUs: Boolean) {
```
> يعرّف دالة `updatePeerFavoritedUs` تأخذ معامل `noisePublicKey` من نوع مصفوفة بايتات (ByteArray) ومعامل `theyFavoritedUs` من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:212]

```
213:         val keyHex = noisePublicKey.joinToString("") { "%02x".format(it) }
```
> يعرّف قيمة ثابتة `keyHex` ناتجة عن دمج (joinToString) بايتات `noisePublicKey` بفاصل فارغ، حيث يُنسَّق كل بايت `it` بصيغة سداسية عشرية من خانتين «%02x». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:213]

```
214:         val existing = favorites[keyHex]
```
> يعرّف قيمة ثابتة `existing` بقراءة عنصر خريطة المفضّلات (favorites) عند المفتاح `keyHex`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:214]

```
215: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:215]

```
216:         if (existing != null) {
```
> يفتح شرطاً `if` يتحقق أن `existing` لا يساوي null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:216]

```
217:             val updated = existing.copy(
```
> يعرّف قيمة ثابتة `updated` بنسخ (copy) الكائن `existing` مع تعديل حقول تُحدَّد في الأسطر التالية. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:217]

```
218:                 theyFavoritedUs = theyFavoritedUs,
```
> يضبط حقل `theyFavoritedUs` على قيمة المعامل `theyFavoritedUs`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:218]

```
219:                 lastUpdated = Date()
```
> يضبط حقل `lastUpdated` على كائن تاريخ `Date()` جديد (اللحظة الحالية). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:219]

```
220:             )
```
> قوس إغلاق `)` لاستدعاء النسخ (copy). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:220]

```
221:             favorites[keyHex] = updated
```
> يضع في خريطة المفضّلات (favorites) عند المفتاح `keyHex` القيمة `updated`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:221]

```
222:             saveFavorites()
```
> يستدعي دالة حفظ المفضّلات (saveFavorites). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:222]

```
223:             notifyChanged(keyHex)
```
> يستدعي دالة الإبلاغ بالتغيير (notifyChanged) ممرّراً `keyHex`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:223]

```
224: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:224]

```
225:             Log.d(TAG, "Updated peer favorited us for ${keyHex.take(16)}...: $theyFavoritedUs")
```
> يسجّل رسالة تصحيح (Log.d) بالوسم `TAG` نصّها «Updated peer favorited us for ${keyHex.take(16)}...: $theyFavoritedUs» حيث يأخذ أول 16 محرفاً من `keyHex` ويدرج قيمة `theyFavoritedUs`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:225]

```
226:         }
```
> إغلاق نطاق شرط `if`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:226]

```
227:     }
```
> إغلاق نطاق الدالة `updatePeerFavoritedUs`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:227]

```
228: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:228]

```
229:     fun getMutualFavorites(): List<FavoriteRelationship> = favorites.values.filter { it.isMutual }
```
> يعرّف دالة `getMutualFavorites` تعيد قائمة (List) من علاقات المفضّلة (FavoriteRelationship)، قيمتها قيم خريطة المفضّلات بعد ترشيحها (filter) لمن يكون `it.isMutual` صحيحاً. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:229]

```
230:     fun getOurFavorites(): List<FavoriteRelationship> = favorites.values.filter { it.isFavorite }
```
> يعرّف دالة `getOurFavorites` تعيد قائمة (List) من علاقات المفضّلة (FavoriteRelationship)، قيمتها قيم خريطة المفضّلات بعد ترشيحها (filter) لمن يكون `it.isFavorite` صحيحاً. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:230]

```
231: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:231]

```
232:     fun clearAllFavorites() {
```
> يعرّف دالة `clearAllFavorites` بلا معاملات. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:232]

```
233:         favorites.clear()
```
> يستدعي `clear` على خريطة المفضّلات (favorites) لإفراغها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:233]

```
234:         saveFavorites()
```
> يستدعي دالة حفظ المفضّلات (saveFavorites). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:234]

```
235:         peerIdIndex.clear()
```
> يستدعي `clear` على فهرس معرّفات النظراء (peerIdIndex) لإفراغه. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:235]

```
236:         savePeerIdIndex()
```
> يستدعي دالة حفظ فهرس معرّفات النظراء (savePeerIdIndex). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:236]

```
237:         Log.i(TAG, "Cleared all favorites")
```
> يسجّل رسالة معلومات (Log.i) بالوسم `TAG` نصّها «Cleared all favorites». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:237]

```
238:         notifyAllCleared()
```
> يستدعي دالة الإبلاغ بمسح الكل (notifyAllCleared). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:238]

```
239:     }
```
> إغلاق نطاق الدالة `clearAllFavorites`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:239]

```
240: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:240]

```
241:     /** Find Noise key by Nostr pubkey */
```
> تعليق: إيجاد مفتاح Noise بواسطة مفتاح Nostr العام (pubkey). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:241]

```
242:     fun findNoiseKey(forNostrPubkey: String): ByteArray? {
```
> يعرّف دالة `findNoiseKey` تأخذ معامل `forNostrPubkey` من نوع نص (String) وتعيد مصفوفة بايتات (ByteArray) قابلة لأن تكون null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:242]

```
243:         val targetHex = normalizeNostrKeyToHex(forNostrPubkey) ?: return null
```
> يعرّف قيمة ثابتة `targetHex` بنتيجة استدعاء دالة تطبيع مفتاح Nostr إلى سداسي (normalizeNostrKeyToHex) على `forNostrPubkey`، وإن كانت null يعيد null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:243]

```
244:         return favorites.values.firstOrNull { rel ->
```
> يعيد أول عنصر (firstOrNull) من قيم خريطة المفضّلات يحقّق الشرط على العنصر `rel`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:244]

```
245:             rel.peerNostrPublicKey?.let { stored -> normalizeNostrKeyToHex(stored) } == targetHex
```
> الشرط: إذا كان `rel.peerNostrPublicKey` غير null يُطبّقه عبر `let` باسم `stored` ويطبّعه بدالة normalizeNostrKeyToHex، ثم يقارن الناتج بمساواة (==) مع `targetHex`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:245]

```
246:         }?.peerNoisePublicKey
```
> إغلاق نطاق المرشّح، ثم إن لم يكن الناتج null يصل إلى حقل `peerNoisePublicKey` ويعيده. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:246]

```
247:     }
```
> إغلاق نطاق الدالة `findNoiseKey`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:247]

```
248: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:248]

```
249:     /** Find Nostr pubkey by Noise key */
```
> تعليق: إيجاد مفتاح Nostr العام (pubkey) بواسطة مفتاح Noise. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:249]

```
250:     fun findNostrPubkey(forNoiseKey: ByteArray): String? {
```
> يعرّف دالة `findNostrPubkey` تأخذ معامل `forNoiseKey` من نوع مصفوفة بايتات (ByteArray) وتعيد نصّاً (String) قابلاً لأن يكون null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:250]

```
251:         val keyHex = forNoiseKey.joinToString("") { "%02x".format(it) }
```
> يعرّف قيمة ثابتة `keyHex` بدمج بايتات `forNoiseKey` بفاصل فارغ، منسّقاً كل بايت `it` بصيغة سداسية من خانتين «%02x». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:251]

```
252:         return favorites[keyHex]?.peerNostrPublicKey
```
> يعيد قيمة الحقل `peerNostrPublicKey` لعنصر خريطة المفضّلات عند المفتاح `keyHex` إن لم يكن العنصر null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:252]

```
253:     }
```
> إغلاق نطاق الدالة `findNostrPubkey`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:253]

```
254: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:254]

```
255:     // MARK: - Persistence
```
> تعليق: علامة قسم «المثابرة/الحفظ» (Persistence). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:255]

```
256: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:256]

```
257:     private fun loadFavorites() {
```
> يعرّف دالة خاصة (private) `loadFavorites` بلا معاملات. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:257]

```
258:         try {
```
> يفتح كتلة محاولة `try`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:258]

```
259:             val favoritesJson = stateManager.getSecureValue(FAVORITES_KEY)
```
> يعرّف قيمة ثابتة `favoritesJson` بنتيجة استدعاء `getSecureValue` على مدير الحالة (stateManager) ممرّراً المفتاح `FAVORITES_KEY`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:259]

```
260:             if (favoritesJson != null) {
```
> يفتح شرطاً `if` يتحقق أن `favoritesJson` لا يساوي null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:260]

```
261:                 val type = object : TypeToken<Map<String, FavoriteRelationshipData>>() {}.type
```
> يعرّف قيمة ثابتة `type` من نوع كائن مجهول يرث TypeToken لخريطة من نص (String) إلى بيانات علاقة المفضّلة (FavoriteRelationshipData)، ويأخذ خاصيّته `type`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:261]

```
262:                 val data: Map<String, FavoriteRelationshipData> = gson.fromJson(favoritesJson, type)
```
> يعرّف قيمة ثابتة `data` من نوع خريطة من نص إلى FavoriteRelationshipData بفك ترميز (fromJson) النص `favoritesJson` باستخدام `gson` ونوع `type`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:262]

```
263: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:263]

```
264:                 favorites.clear()
```
> يستدعي `clear` على خريطة المفضّلات (favorites) لإفراغها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:264]

```
265:                 data.forEach { (key, relationshipData) ->
```
> يمرّ على كل عنصر في `data` بدالة `forEach` مفكّكاً إياه إلى `key` و`relationshipData`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:265]

```
266:                     favorites[key] = relationshipData.toFavoriteRelationship()
```
> يضع في خريطة المفضّلات عند المفتاح `key` ناتج استدعاء `toFavoriteRelationship` على `relationshipData`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:266]

```
267:                 }
```
> إغلاق نطاق `forEach`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:267]

```
268:                 Log.d(TAG, "Loaded ${favorites.size} favorite relationships")
```
> يسجّل رسالة تصحيح (Log.d) بالوسم `TAG` نصّها «Loaded ${favorites.size} favorite relationships» مدرجاً حجم خريطة المفضّلات (favorites.size). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:268]

```
269:             }
```
> إغلاق نطاق شرط `if`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:269]

```
270:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة التقاط `catch` للاستثناء `e` من نوع Exception. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:270]

```
271:             Log.e(TAG, "Failed to load favorites: ${e.message}")
```
> يسجّل رسالة خطأ (Log.e) بالوسم `TAG` نصّها «Failed to load favorites: ${e.message}» مدرجاً رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:271]

```
272:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:272]

```
273:     }
```
> إغلاق نطاق الدالة `loadFavorites`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:273]

```
274: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:274]

```
275:     private fun saveFavorites() {
```
> يعرّف دالة خاصة (private) `saveFavorites` بلا معاملات. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:275]

```
276:         try {
```
> يفتح كتلة محاولة `try`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:276]

```
277:             val data = favorites.mapValues { (_, relationship) ->
```
> يعرّف قيمة ثابتة `data` بتحويل قيم خريطة المفضّلات عبر `mapValues`، متجاهلاً المفتاح ومسمّياً القيمة `relationship`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:277]

```
278:                 FavoriteRelationshipData.fromFavoriteRelationship(relationship)
```
> ينتج لكل عنصر كائن بيانات بياستدعاء `fromFavoriteRelationship` على `FavoriteRelationshipData` ممرّراً `relationship`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:278]

```
279:             }
```
> إغلاق نطاق `mapValues`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:279]

```
280:             val favoritesJson = gson.toJson(data)
```
> يعرّف قيمة ثابتة `favoritesJson` بترميز `data` إلى نص JSON بياستدعاء `toJson` على `gson`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:280]

```
281:             stateManager.storeSecureValue(FAVORITES_KEY, favoritesJson)
```
> يستدعي `storeSecureValue` على مدير الحالة (stateManager) ممرّراً المفتاح `FAVORITES_KEY` والقيمة `favoritesJson`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:281]

```
282:             Log.d(TAG, "Saved ${favorites.size} favorite relationships")
```
> يسجّل رسالة تصحيح (Log.d) بالوسم `TAG` نصّها «Saved ${favorites.size} favorite relationships» مدرجاً حجم خريطة المفضّلات (favorites.size). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:282]

```
283:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة التقاط `catch` للاستثناء `e` من نوع Exception. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:283]

```
284:             Log.e(TAG, "Failed to save favorites: ${e.message}")
```
> يسجّل رسالة خطأ (Log.e) بالوسم `TAG` نصّها «Failed to save favorites: ${e.message}» مدرجاً رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:284]

```
285:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:285]

```
286:     }
```
> إغلاق نطاق الدالة `saveFavorites`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:286]

```
287: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:287]

```
288:     private fun loadPeerIdIndex() {
```
> يعرّف دالة خاصة (private) `loadPeerIdIndex` بلا معاملات. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:288]

```
289:         try {
```
> يفتح كتلة محاولة `try`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:289]

```
290:             val json = stateManager.getSecureValue(PEERID_INDEX_KEY)
```
> يعرّف قيمة ثابتة `json` بنتيجة استدعاء `getSecureValue` على مدير الحالة (stateManager) ممرّراً المفتاح `PEERID_INDEX_KEY`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:290]

```
291:             if (json != null) {
```
> يفتح شرطاً `if` يتحقق أن `json` لا يساوي null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:291]

```
292:                 val type = object : TypeToken<Map<String, String>>() {}.type
```
> يعرّف قيمة ثابتة `type` من كائن مجهول يرث TypeToken لخريطة من نص (String) إلى نص (String)، ويأخذ خاصيّته `type`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:292]

```
293:                 val data: Map<String, String> = gson.fromJson(json, type)
```
> يعرّف قيمة ثابتة `data` من نوع خريطة من نص إلى نص بفك ترميز (fromJson) النص `json` باستخدام `gson` ونوع `type`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:293]

```
294:                 peerIdIndex.clear()
```
> يستدعي `clear` على فهرس معرّفات النظراء (peerIdIndex) لإفراغه. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:294]

```
295:                 peerIdIndex.putAll(data)
```
> يستدعي `putAll` على فهرس معرّفات النظراء (peerIdIndex) لإضافة كل عناصر `data`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:295]

```
296:                 Log.d(TAG, "Loaded ${peerIdIndex.size} peerID→npub mappings")
```
> يسجّل رسالة تصحيح (Log.d) بالوسم `TAG` نصّها «Loaded ${peerIdIndex.size} peerID→npub mappings» مدرجاً حجم فهرس معرّفات النظراء (peerIdIndex.size). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:296]

```
297:             }
```
> إغلاق نطاق شرط `if`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:297]

```
298:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة التقاط `catch` للاستثناء `e` من نوع Exception. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:298]

```
299:             Log.e(TAG, "Failed to load peerID index: ${e.message}")
```
> يسجّل رسالة خطأ (Log.e) بالوسم `TAG` نصّها «Failed to load peerID index: ${e.message}» مدرجاً رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:299]

```
300:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:300]

```
301:     }
```
> إغلاق نطاق الدالة `loadPeerIdIndex`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:301]

```
302: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:302]

```
303:     private fun savePeerIdIndex() {
```
> يعرّف دالة خاصة (private) `savePeerIdIndex` بلا معاملات. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:303]

```
304:         try {
```
> يفتح كتلة محاولة `try`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:304]

```
305:             val json = gson.toJson(peerIdIndex)
```
> يعرّف قيمة ثابتة `json` بترميز فهرس معرّفات النظراء (peerIdIndex) إلى نص JSON بياستدعاء `toJson` على `gson`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:305]

```
306:             stateManager.storeSecureValue(PEERID_INDEX_KEY, json)
```
> يستدعي `storeSecureValue` على مدير الحالة (stateManager) ممرّراً المفتاح `PEERID_INDEX_KEY` والقيمة `json`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:306]

```
307:             Log.d(TAG, "Saved ${peerIdIndex.size} peerID→npub mappings")
```
> يسجّل رسالة تصحيح (Log.d) بالوسم `TAG` نصّها «Saved ${peerIdIndex.size} peerID→npub mappings» مدرجاً حجم فهرس معرّفات النظراء (peerIdIndex.size). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:307]

```
308:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة التقاط `catch` للاستثناء `e` من نوع Exception. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:308]

```
309:             Log.e(TAG, "Failed to save peerID index: ${e.message}")
```
> يسجّل رسالة خطأ (Log.e) بالوسم `TAG` نصّها «Failed to save peerID index: ${e.message}» مدرجاً رسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:309]

```
310:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:310]

```
311:     }
```
> إغلاق نطاق الدالة `savePeerIdIndex`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:311]

```
312: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:312]

```
313:     // MARK: - Listeners
```
> تعليق: علامة قسم «المستمعون» (Listeners). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:313]

```
314:     fun addListener(listener: FavoritesChangeListener) {
```
> يعرّف دالة `addListener` تأخذ معامل `listener` من نوع مستمع تغيّر المفضّلات (FavoritesChangeListener). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:314]

```
315:         synchronized(listeners) { if (!listeners.contains(listener)) listeners.add(listener) }
```
> يدخل كتلة متزامنة (synchronized) على قائمة المستمعين (listeners): إذا لم تكن القائمة تحتوي `listener` يضيفه عبر `add`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:315]

```
316:     }
```
> إغلاق نطاق الدالة `addListener`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:316]

```
317:     fun removeListener(listener: FavoritesChangeListener) {
```
> يعرّف دالة `removeListener` تأخذ معامل `listener` من نوع مستمع تغيّر المفضّلات (FavoritesChangeListener). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:317]

```
318:         synchronized(listeners) { listeners.remove(listener) }
```
> يدخل كتلة متزامنة (synchronized) على قائمة المستمعين (listeners) ويزيل `listener` عبر `remove`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:318]

```
319:     }
```
> إغلاق نطاق الدالة `removeListener`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:319]

```
320:     private fun notifyChanged(noiseKeyHex: String) {
```
> يعرّف دالة خاصة (private) `notifyChanged` تأخذ معامل `noiseKeyHex` من نوع نص (String). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:320]

```
321:         val snapshot = synchronized(listeners) { listeners.toList() }
```
> يعرّف قيمة ثابتة `snapshot` بنتيجة كتلة متزامنة (synchronized) على قائمة المستمعين تعيد نسخة قائمة (toList) منها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:321]

```
322:         snapshot.forEach { runCatching { it.onFavoriteChanged(noiseKeyHex) } }
```
> يمرّ على كل عنصر `it` في `snapshot` بدالة `forEach`، وداخل `runCatching` يستدعي `onFavoriteChanged` على العنصر ممرّراً `noiseKeyHex`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:322]

```
323:     }
```
> إغلاق نطاق الدالة `notifyChanged`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:323]

```
324:     private fun notifyAllCleared() {
```
> يعرّف دالة خاصة (private) `notifyAllCleared` بلا معاملات. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:324]

```
325:         val snapshot = synchronized(listeners) { listeners.toList() }
```
> يعرّف قيمة ثابتة `snapshot` بنتيجة كتلة متزامنة (synchronized) على قائمة المستمعين تعيد نسخة قائمة (toList) منها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:325]

```
326:         snapshot.forEach { runCatching { it.onAllCleared() } }
```
> يمرّ على كل عنصر `it` في `snapshot` بدالة `forEach`، وداخل `runCatching` يستدعي `onAllCleared` على العنصر. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:326]

```
327:     }
```
> إغلاق نطاق الدالة `notifyAllCleared`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:327]

```
328: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:328]

```
329:     /** Normalize a Nostr public key string (npub bech32 or hex) to lowercase hex */
```
> تعليق: تطبيع نص مفتاح Nostr العام (npub بترميز bech32 أو سداسي) إلى سداسي صغير الأحرف. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:329]

```
330:     private fun normalizeNostrKeyToHex(value: String): String? = try {
```
> يعرّف دالة خاصة (private) `normalizeNostrKeyToHex` تأخذ معامل `value` من نوع نص (String) وتعيد نصّاً قابلاً لأن يكون null، وقيمتها كتلة محاولة `try`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:330]

```
331:         if (value.startsWith("npub1")) {
```
> يفتح شرطاً `if` يتحقق أن `value` يبدأ (startsWith) بالنص «npub1». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:331]

```
332:             val (hrp, data) = com.bitchat.android.nostr.Bech32.decode(value)
```
> يعرّف زوج قيم ثابتة `hrp` و`data` بتفكيك ناتج استدعاء `decode` على `com.bitchat.android.nostr.Bech32` ممرّراً `value`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:332]

```
333:             if (hrp != "npub") null else data.joinToString("") { "%02x".format(it) }
```
> إذا كان `hrp` لا يساوي «npub» فالنتيجة null، وإلا يدمج بايتات `data` بفاصل فارغ منسّقاً كل بايت `it` بصيغة سداسية من خانتين «%02x». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:333]

```
334:         } else value.lowercase()
```
> وإلا (إن لم يبدأ بـ npub1) فالنتيجة `value` بعد تحويله إلى أحرف صغيرة (lowercase). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:334]

```
335:     } catch (_: Exception) { null }
```
> يغلق كتلة `try` ويلتقط أي استثناء (Exception) متجاهلاً اسمه، والنتيجة في هذه الحالة null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:335]

```
336: }
```
> إغلاق نطاق الصنف/الكائن الذي يضمّ الدوال السابقة. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:336]

```
337: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:337]

```
338: /** Serializable data for JSON storage */
```
> تعليق: بيانات قابلة للتسلسل (Serializable) من أجل التخزين بصيغة JSON. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:338]

```
339: private data class FavoriteRelationshipData(
```
> يعرّف صنف بيانات خاص (private data class) باسم بيانات علاقة المفضّلة (FavoriteRelationshipData) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:339]

```
340:     val peerNoisePublicKeyHex: String,
```
> يعرّف خاصيّة `peerNoisePublicKeyHex` من نوع نص (String). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:340]

```
341:     val peerNostrPublicKey: String?,
```
> يعرّف خاصيّة `peerNostrPublicKey` من نوع نص (String) قابل لأن يكون null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:341]

```
342:     val peerNickname: String,
```
> يعرّف خاصيّة `peerNickname` من نوع نص (String). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:342]

```
343:     val isFavorite: Boolean,
```
> يعرّف خاصيّة `isFavorite` من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:343]

```
344:     val theyFavoritedUs: Boolean,
```
> يعرّف خاصيّة `theyFavoritedUs` من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:344]

```
345:     val favoritedAt: Long,
```
> يعرّف خاصيّة `favoritedAt` من نوع عدد طويل (Long). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:345]

```
346:     val lastUpdated: Long
```
> يعرّف خاصيّة `lastUpdated` من نوع عدد طويل (Long). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:346]

```
347: ) {
```
> يغلق قائمة معاملات الصنف ويفتح جسمه. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:347]

```
348:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:348]

```
349:         fun fromFavoriteRelationship(relationship: FavoriteRelationship): FavoriteRelationshipData {
```
> يعرّف دالة `fromFavoriteRelationship` تأخذ معامل `relationship` من نوع علاقة المفضّلة (FavoriteRelationship) وتعيد بيانات علاقة المفضّلة (FavoriteRelationshipData). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:349]

```
350:             return FavoriteRelationshipData(
```
> يعيد كائن FavoriteRelationshipData جديداً ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:350]

```
351:                 peerNoisePublicKeyHex = relationship.peerNoisePublicKey.joinToString("") { "%02x".format(it) },
```
> يضبط `peerNoisePublicKeyHex` بدمج بايتات `relationship.peerNoisePublicKey` بفاصل فارغ منسّقاً كل بايت `it` بصيغة سداسية من خانتين «%02x». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:351]

```
352:                 peerNostrPublicKey = relationship.peerNostrPublicKey,
```
> يضبط `peerNostrPublicKey` على قيمة `relationship.peerNostrPublicKey`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:352]

```
353:                 peerNickname = relationship.peerNickname,
```
> يضبط `peerNickname` على قيمة `relationship.peerNickname`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:353]

```
354:                 isFavorite = relationship.isFavorite,
```
> يضبط `isFavorite` على قيمة `relationship.isFavorite`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:354]

```
355:                 theyFavoritedUs = relationship.theyFavoritedUs,
```
> يضبط `theyFavoritedUs` على قيمة `relationship.theyFavoritedUs`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:355]

```
356:                 favoritedAt = relationship.favoritedAt.time,
```
> يضبط `favoritedAt` على خاصيّة `time` من `relationship.favoritedAt` (الوقت بالملّي ثانية). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:356]

```
357:                 lastUpdated = relationship.lastUpdated.time
```
> يضبط `lastUpdated` على خاصيّة `time` من `relationship.lastUpdated` (الوقت بالملّي ثانية). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:357]

```
358:             )
```
> قوس إغلاق `)` لاستدعاء بانية FavoriteRelationshipData. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:358]

```
359:         }
```
> إغلاق نطاق الدالة `fromFavoriteRelationship`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:359]

```
360:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:360]

```
361: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:361]

```
362:     fun toFavoriteRelationship(): FavoriteRelationship {
```
> يعرّف دالة `toFavoriteRelationship` بلا معاملات تعيد علاقة المفضّلة (FavoriteRelationship). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:362]

```
363:         val noiseKeyBytes = peerNoisePublicKeyHex.chunked(2).map { it.toInt(16).toByte() }.toByteArray()
```
> يعرّف قيمة ثابتة `noiseKeyBytes` بتقطيع `peerNoisePublicKeyHex` إلى مقاطع من محرفين (chunked(2))، وتحويل كل مقطع `it` إلى عدد صحيح بأساس 16 (toInt(16)) ثم إلى بايت (toByte)، ثم تحويل الناتج إلى مصفوفة بايتات (toByteArray). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:363]

```
364:         return FavoriteRelationship(
```
> يعيد كائن FavoriteRelationship جديداً ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:364]

```
365:             peerNoisePublicKey = noiseKeyBytes,
```
> يضبط `peerNoisePublicKey` على القيمة `noiseKeyBytes`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:365]

```
366:             peerNostrPublicKey = peerNostrPublicKey,
```
> يضبط `peerNostrPublicKey` على خاصيّة `peerNostrPublicKey` الخاصة بالكائن الحالي. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:366]

```
367:             peerNickname = peerNickname,
```
> يضبط `peerNickname` على خاصيّة `peerNickname` الخاصة بالكائن الحالي. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:367]

```
368:             isFavorite = isFavorite,
```
> يضبط `isFavorite` على خاصيّة `isFavorite` الخاصة بالكائن الحالي. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:368]

```
369:             theyFavoritedUs = theyFavoritedUs,
```
> يضبط `theyFavoritedUs` على خاصيّة `theyFavoritedUs` الخاصة بالكائن الحالي. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:369]

```
370:             favoritedAt = Date(favoritedAt),
```
> يضبط `favoritedAt` على كائن تاريخ `Date` مبنيّ من القيمة `favoritedAt` (ملّي ثانية). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:370]

```
371:             lastUpdated = Date(lastUpdated)
```
> يضبط `lastUpdated` على كائن تاريخ `Date` مبنيّ من القيمة `lastUpdated` (ملّي ثانية). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:371]

```
372:         )
```
> قوس إغلاق `)` لاستدعاء بانية FavoriteRelationship. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:372]

```
373:     }
```
> إغلاق نطاق الدالة `toFavoriteRelationship`. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:373]

```
374: }
```
> إغلاق نطاق صنف البيانات FavoriteRelationshipData. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:374]
