# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt (الأسطر 201–299)

```
201:      * Get Nostr public key associated with a Noise public key
```
> تعليق: احصل على مفتاح نوستر العام (Nostr public key) المرتبط بمفتاح نويز العام (Noise public key). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:201]

```
202:      */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:202]

```
203:     fun getNostrPublicKey(noisePublicKey: ByteArray, context: Context): String? {
```
> تعريف دالة باسم «احصل على مفتاح نوستر العام» (getNostrPublicKey) تأخذ وسيطاً «مفتاح نويز العام» (noisePublicKey) من نوع مصفوفة بايتات (ByteArray) ووسيطاً «سياق» (context) من نوع Context، وتُعيد نصاً (String) قابلاً للإفراغ (nullable). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:203]

```
204:         // This would need proper implementation based on your favorites storage system
```
> تعليق: هذا سيحتاج إلى تنفيذ سليم مبني على نظام تخزين المفضّلة (favorites storage system) الخاص بك. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:204]

```
205:         // For now, return null as we don't have the full association system
```
> تعليق: في الوقت الحالي، أعِد null لأننا لا نملك نظام الربط (association system) الكامل. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:205]

```
206:         return null
```
> تُعيد القيمة null. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:206]

```
207:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:207]

```
208:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:208]

```
209:     /**
```
> فتح كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:209]

```
210:      * Clear all Nostr identity data
```
> تعليق: امسح كل بيانات هوية نوستر (Nostr identity data). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:210]

```
211:      */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:211]

```
212:     fun clearAllAssociations(context: Context) {
```
> تعريف دالة باسم «امسح كل الروابط» (clearAllAssociations) تأخذ وسيطاً «سياق» (context) من نوع Context، ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:212]

```
213:         val stateManager = SecureIdentityStateManager(context)
```
> يُعرَّف متغيّر ثابت «مدير الحالة» (stateManager) ويُسنَد إليه كائن جديد من «مدير حالة الهوية الآمن» (SecureIdentityStateManager) مُمرَّراً إليه السياق context. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:213]

```
214:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:214]

```
215:         // Clear cache first
```
> تعليق: امسح المخبأ (cache) أولاً. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:215]

```
216:         geohashIdentityCache.clear()
```
> يُستدعى التابع clear على «مخبأ هوية الجيوهاش» (geohashIdentityCache) لتفريغ محتوياته. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:216]

```
217:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:217]

```
218:         // Clear Nostr private key using public methods instead of reflection
```
> تعليق: امسح مفتاح نوستر الخاص (Nostr private key) باستخدام التوابع العامة (public methods) بدلاً من الانعكاس (reflection). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:218]

```
219:         try {
```
> بداية كتلة المحاولة try. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:219]

```
220:             stateManager.clearSecureValues(NOSTR_PRIVATE_KEY, DEVICE_SEED_KEY)
```
> يُستدعى التابع «امسح القيم الآمنة» (clearSecureValues) على stateManager مُمرَّراً إليه الثابتين NOSTR_PRIVATE_KEY و DEVICE_SEED_KEY. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:220]

```
221:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:221]

```
222:             Log.i(TAG, "Cleared all Nostr identity data and cache")
```
> يُستدعى التابع Log.i (تسجيل معلومات) بالوسم TAG والرسالة «Cleared all Nostr identity data and cache» (مُسِحَت كل بيانات هوية نوستر والمخبأ). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:222]

```
223:         } catch (e: Exception) {
```
> إغلاق كتلة try وبداية كتلة الالتقاط catch لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:223]

```
224:             Log.e(TAG, "Failed to clear Nostr data: ${e.message}")
```
> يُستدعى التابع Log.e (تسجيل خطأ) بالوسم TAG والرسالة «Failed to clear Nostr data: » متبوعةً بقيمة e.message (رسالة الاستثناء). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:224]

```
225:         }
```
> إغلاق نطاق كتلة catch. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:225]

```
226:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:226]

```
227:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:227]

```
228:     // MARK: - Private Methods
```
> تعليق: علامة قسم: التوابع الخاصة (Private Methods). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:228]

```
229:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:229]

```
230:     private fun loadNostrPrivateKey(stateManager: SecureIdentityStateManager): String? {
```
> تعريف دالة خاصة (private) باسم «حمّل مفتاح نوستر الخاص» (loadNostrPrivateKey) تأخذ وسيطاً «مدير الحالة» (stateManager) من نوع SecureIdentityStateManager، وتُعيد نصاً (String) قابلاً للإفراغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:230]

```
231:         return try {
```
> تُعيد ناتج كتلة المحاولة try التي تبدأ هنا. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:231]

```
232:             // Use public methods instead of reflection to access the encrypted preferences
```
> تعليق: استخدم التوابع العامة بدلاً من الانعكاس للوصول إلى التفضيلات المُشفَّرة (encrypted preferences). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:232]

```
233:             stateManager.getSecureValue(NOSTR_PRIVATE_KEY)
```
> يُستدعى التابع «احصل على القيمة الآمنة» (getSecureValue) على stateManager مُمرَّراً إليه الثابت NOSTR_PRIVATE_KEY، وناتجه هو قيمة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:233]

```
234:         } catch (e: Exception) {
```
> إغلاق كتلة try وبداية كتلة الالتقاط catch لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:234]

```
235:             Log.e(TAG, "Failed to load Nostr private key: ${e.message}")
```
> يُستدعى التابع Log.e (تسجيل خطأ) بالوسم TAG والرسالة «Failed to load Nostr private key: » متبوعةً بقيمة e.message. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:235]

```
236:             null
```
> القيمة null هي ناتج كتلة catch. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:236]

```
237:         }
```
> إغلاق نطاق كتلة catch. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:237]

```
238:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:238]

```
239:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:239]

```
240:     private fun saveNostrPrivateKey(stateManager: SecureIdentityStateManager, privateKeyHex: String) {
```
> تعريف دالة خاصة باسم «احفظ مفتاح نوستر الخاص» (saveNostrPrivateKey) تأخذ وسيطاً «مدير الحالة» (stateManager) من نوع SecureIdentityStateManager ووسيطاً «المفتاح الخاص بصيغة ست عشرية» (privateKeyHex) من نوع String، ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:240]

```
241:         try {
```
> بداية كتلة المحاولة try. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:241]

```
242:             // Use public methods instead of reflection to access the encrypted preferences
```
> تعليق: استخدم التوابع العامة بدلاً من الانعكاس للوصول إلى التفضيلات المُشفَّرة. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:242]

```
243:             stateManager.storeSecureValue(NOSTR_PRIVATE_KEY, privateKeyHex)
```
> يُستدعى التابع «خزّن القيمة الآمنة» (storeSecureValue) على stateManager مُمرَّراً إليه الثابت NOSTR_PRIVATE_KEY والقيمة privateKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:243]

```
244:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:244]

```
245:             Log.d(TAG, "Saved Nostr private key to secure storage")
```
> يُستدعى التابع Log.d (تسجيل تنقيح) بالوسم TAG والرسالة «Saved Nostr private key to secure storage» (حُفِظ مفتاح نوستر الخاص في التخزين الآمن). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:245]

```
246:         } catch (e: Exception) {
```
> إغلاق كتلة try وبداية كتلة الالتقاط catch لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:246]

```
247:             Log.e(TAG, "Failed to save Nostr private key: ${e.message}")
```
> يُستدعى التابع Log.e (تسجيل خطأ) بالوسم TAG والرسالة «Failed to save Nostr private key: » متبوعةً بقيمة e.message. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:247]

```
248:             throw e
```
> تُرمى (throw) إعادةُ الاستثناء e. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:248]

```
249:         }
```
> إغلاق نطاق كتلة catch. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:249]

```
250:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:250]

```
251:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:251]

```
252:     private fun getOrCreateDeviceSeed(stateManager: SecureIdentityStateManager): ByteArray {
```
> تعريف دالة خاصة باسم «احصل على بذرة الجهاز أو أنشئها» (getOrCreateDeviceSeed) تأخذ وسيطاً «مدير الحالة» (stateManager) من نوع SecureIdentityStateManager، وتُعيد مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:252]

```
253:         try {
```
> بداية كتلة المحاولة try. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:253]

```
254:             // Use public methods instead of reflection to access the encrypted preferences
```
> تعليق: استخدم التوابع العامة بدلاً من الانعكاس للوصول إلى التفضيلات المُشفَّرة. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:254]

```
255:             val existingSeed = stateManager.getSecureValue(DEVICE_SEED_KEY)
```
> يُعرَّف متغيّر ثابت «البذرة الموجودة» (existingSeed) ويُسنَد إليه ناتج استدعاء getSecureValue على stateManager مُمرَّراً إليه الثابت DEVICE_SEED_KEY. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:255]

```
256:             if (existingSeed != null) {
```
> شرط: إذا كانت البذرة الموجودة existingSeed لا تساوي null. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:256]

```
257:                 return android.util.Base64.decode(existingSeed, android.util.Base64.DEFAULT)
```
> تُعيد ناتج فكّ ترميز Base64 (android.util.Base64.decode) للبذرة الموجودة existingSeed بالعَلَم DEFAULT. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:257]

```
258:             }
```
> إغلاق نطاق كتلة if. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:258]

```
259:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:259]

```
260:             // Generate new seed
```
> تعليق: ولّد بذرة جديدة (new seed). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:260]

```
261:             val seed = ByteArray(32)
```
> يُعرَّف متغيّر ثابت «بذرة» (seed) ويُسنَد إليه مصفوفة بايتات (ByteArray) بطول 32. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:261]

```
262:             SecureRandom().nextBytes(seed)
```
> يُنشَأ كائن «عشوائي آمن» (SecureRandom) ويُستدعى عليه التابع nextBytes مُمرَّراً إليه seed لملئها ببايتات عشوائية. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:262]

```
263:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:263]

```
264:             val seedBase64 = android.util.Base64.encodeToString(seed, android.util.Base64.DEFAULT)
```
> يُعرَّف متغيّر ثابت «البذرة بصيغة Base64» (seedBase64) ويُسنَد إليه ناتج ترميز seed نصاً عبر android.util.Base64.encodeToString بالعَلَم DEFAULT. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:264]

```
265:             stateManager.storeSecureValue(DEVICE_SEED_KEY, seedBase64)
```
> يُستدعى التابع storeSecureValue على stateManager مُمرَّراً إليه الثابت DEVICE_SEED_KEY والقيمة seedBase64. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:265]

```
266:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:266]

```
267:             Log.d(TAG, "Generated new device seed for geohash identity derivation")
```
> يُستدعى التابع Log.d (تسجيل تنقيح) بالوسم TAG والرسالة «Generated new device seed for geohash identity derivation» (وُلِّدت بذرة جهاز جديدة لاشتقاق هوية الجيوهاش). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:267]

```
268:             return seed
```
> تُعيد البذرة seed. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:268]

```
269:         } catch (e: Exception) {
```
> إغلاق كتلة try وبداية كتلة الالتقاط catch لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:269]

```
270:             Log.e(TAG, "Failed to get/create device seed: ${e.message}")
```
> يُستدعى التابع Log.e (تسجيل خطأ) بالوسم TAG والرسالة «Failed to get/create device seed: » متبوعةً بقيمة e.message. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:270]

```
271:             throw e
```
> تُرمى (throw) إعادةُ الاستثناء e. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:271]

```
272:         }
```
> إغلاق نطاق كتلة catch. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:272]

```
273:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:273]

```
274:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:274]

```
275:     private fun hmacSha256(key: ByteArray, message: ByteArray): ByteArray {
```
> تعريف دالة خاصة باسم «hmacSha256» تأخذ وسيطاً «مفتاح» (key) من نوع ByteArray ووسيطاً «رسالة» (message) من نوع ByteArray، وتُعيد مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:275]

```
276:         val mac = javax.crypto.Mac.getInstance("HmacSHA256")
```
> يُعرَّف متغيّر ثابت «mac» ويُسنَد إليه كائن من javax.crypto.Mac عبر getInstance بالخوارزمية النصية «HmacSHA256». [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:276]

```
277:         val secretKeySpec = javax.crypto.spec.SecretKeySpec(key, "HmacSHA256")
```
> يُعرَّف متغيّر ثابت «مواصفة المفتاح السري» (secretKeySpec) ويُسنَد إليه كائن جديد من javax.crypto.spec.SecretKeySpec مُمرَّراً إليه key والخوارزمية النصية «HmacSHA256». [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:277]

```
278:         mac.init(secretKeySpec)
```
> يُستدعى التابع init على mac مُمرَّراً إليه secretKeySpec للتهيئة. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:278]

```
279:         return mac.doFinal(message)
```
> تُعيد ناتج استدعاء doFinal على mac مُمرَّراً إليه message. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:279]

```
280:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:280]

```
281: }
```
> إغلاق نطاق (إغلاق الصنف/الكائن المحتوي). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:281]

```
282: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:282]

```
283: // Extension functions for data conversion
```
> تعليق: دوال امتداد (Extension functions) لتحويل البيانات. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:283]

```
284: private fun String.hexToByteArrayLocal(): ByteArray {
```
> تعريف دالة امتداد خاصة على النوع String باسم «hexToByteArrayLocal» (ست عشري إلى مصفوفة بايتات محلياً) لا تأخذ وسائط وتُعيد مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:284]

```
285:     return chunked(2).map { it.toInt(16).toByte() }.toByteArray()
```
> تُعيد ناتجَ تقطيع النص إلى أزواج (chunked(2))، ثم تحويل كل زوج إلى عدد صحيح بالأساس 16 (toInt(16)) فإلى بايت (toByte)، ثم جمع النتائج في مصفوفة بايتات (toByteArray). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:285]

```
286: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:286]

```
287: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:287]

```
288: private fun ByteArray.toHexStringLocal(): String {
```
> تعريف دالة امتداد خاصة على النوع ByteArray باسم «toHexStringLocal» (مصفوفة بايتات إلى نص ست عشري محلياً) لا تأخذ وسائط وتُعيد نصاً (String). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:288]

```
289:     return joinToString("") { "%02x".format(it) }
```
> تُعيد ناتج ضمّ العناصر بنص فاصل فارغ (joinToString("")) حيث يُنسَّق كل عنصر بالصيغة «%02x» (ست عشري بخانتين مع تصفير بادئ). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:289]

```
290: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:290]

```
291: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:291]

```
292: private fun UInt.toLittleEndianBytes(): ByteArray {
```
> تعريف دالة امتداد خاصة على النوع UInt باسم «toLittleEndianBytes» (إلى بايتات بترتيب صغير-أولاً) لا تأخذ وسائط وتُعيد مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:292]

```
293:     val bytes = ByteArray(4)
```
> يُعرَّف متغيّر ثابت «bytes» ويُسنَد إليه مصفوفة بايتات (ByteArray) بطول 4. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:293]

```
294:     bytes[0] = (this and 0xFFu).toByte()
```
> يُسنَد إلى العنصر ذي الفهرس 0 من bytes ناتجُ (this and 0xFFu) المحوَّل إلى بايت (toByte): أي البايت الأدنى من القيمة. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:294]

```
295:     bytes[1] = ((this shr 8) and 0xFFu).toByte()
```
> يُسنَد إلى العنصر ذي الفهرس 1 من bytes ناتجُ إزاحة القيمة يميناً 8 بتات ((this shr 8)) ثم and مع 0xFFu ثم toByte. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:295]

```
296:     bytes[2] = ((this shr 16) and 0xFFu).toByte()
```
> يُسنَد إلى العنصر ذي الفهرس 2 من bytes ناتجُ إزاحة القيمة يميناً 16 بتاً ((this shr 16)) ثم and مع 0xFFu ثم toByte. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:296]

```
297:     bytes[3] = ((this shr 24) and 0xFFu).toByte()
```
> يُسنَد إلى العنصر ذي الفهرس 3 من bytes ناتجُ إزاحة القيمة يميناً 24 بتاً ((this shr 24)) ثم and مع 0xFFu ثم toByte. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:297]

```
298:     return bytes
```
> تُعيد المصفوفة bytes. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:298]

```
299: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:299]
