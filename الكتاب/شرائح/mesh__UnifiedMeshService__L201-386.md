# شريحة — app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt (الأسطر 201–386)

```
201: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:201]

```
202:     override fun getPeerInfo(peerID: String): PeerInfo? {
```
> تعريف دالة معاد تعريفها (override) باسم «احصل على معلومات النظير» (getPeerInfo) تأخذ معاملاً نصياً اسمه «معرّف النظير» (peerID) وتعيد قيمة من نوع «معلومات النظير» (PeerInfo) قابلة لأن تكون عدماً (null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:202]

```
203:         val ble = try { bluetooth.getPeerInfo(peerID) } catch (_: Exception) { null }
```
> تعريف متغيّر ثابت اسمه «بلوتوث» (ble) تُسنَد إليه نتيجة استدعاء `bluetooth.getPeerInfo(peerID)` داخل كتلة محاولة، وإذا حدث استثناء (Exception) تُسنَد إليه قيمة العدم (null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:203]

```
204:         val wifi = try { wifiService()?.getPeerInfo(peerID) } catch (_: Exception) { null }
```
> تعريف متغيّر ثابت اسمه «واي فاي» (wifi) تُسنَد إليه نتيجة استدعاء `wifiService()?.getPeerInfo(peerID)` (مع استدعاء آمن من العدم) داخل كتلة محاولة، وإذا حدث استثناء تُسنَد إليه قيمة العدم. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:204]

```
205:         return when {
```
> بدء إعادة (return) تعبير `when` بلا وسيط للمطابقة على الشروط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:205]

```
206:             ble?.isConnected == true && hasEstablishedSessionOnBluetooth(peerID) -> ble
```
> فرع: إذا كان `ble?.isConnected` يساوي `true` وكان `hasEstablishedSessionOnBluetooth(peerID)` صحيحاً، يُعاد المتغيّر `ble`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:206]

```
207:             wifi?.isConnected == true && wifiService()?.hasEstablishedSession(peerID) == true -> wifi
```
> فرع: إذا كان `wifi?.isConnected` يساوي `true` وكان `wifiService()?.hasEstablishedSession(peerID)` يساوي `true`، يُعاد المتغيّر `wifi`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:207]

```
208:             ble?.isConnected == true -> ble
```
> فرع: إذا كان `ble?.isConnected` يساوي `true`، يُعاد المتغيّر `ble`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:208]

```
209:             wifi?.isConnected == true -> wifi
```
> فرع: إذا كان `wifi?.isConnected` يساوي `true`، يُعاد المتغيّر `wifi`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:209]

```
210:             else -> ble ?: wifi
```
> فرع غير ذلك (else): يُعاد `ble`، وإن كان عدماً فيُعاد `wifi` (عبر مُعامل الدمج العدمي). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:210]

```
211:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:211]

```
212:     }
```
> إغلاق نطاق الدالة `getPeerInfo`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:212]

```
213: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:213]

```
214:     override fun updatePeerInfo(
```
> بدء تعريف دالة معاد تعريفها باسم «حدّث معلومات النظير» (updatePeerInfo) مع فتح قائمة المعاملات. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:214]

```
215:         peerID: String,
```
> معامل نصي اسمه «معرّف النظير» (peerID). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:215]

```
216:         nickname: String,
```
> معامل نصي اسمه «الاسم المستعار» (nickname). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:216]

```
217:         noisePublicKey: ByteArray,
```
> معامل من نوع مصفوفة بايت (ByteArray) اسمه «مفتاح نويز العام» (noisePublicKey). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:217]

```
218:         signingPublicKey: ByteArray,
```
> معامل من نوع مصفوفة بايت اسمه «مفتاح التوقيع العام» (signingPublicKey). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:218]

```
219:         isVerified: Boolean
```
> معامل منطقي (Boolean) اسمه «مُتحقَّق منه» (isVerified). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:219]

```
220:     ): Boolean {
```
> إغلاق قائمة المعاملات وتحديد نوع الإرجاع منطقياً (Boolean) وفتح جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:220]

```
221:         val bleUpdated = try {
```
> تعريف متغيّر ثابت اسمه «بلوتوث مُحدَّث» (bleUpdated) بفتح كتلة محاولة لإسناد قيمته. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:221]

```
222:             bluetooth.updatePeerInfo(peerID, nickname, noisePublicKey, signingPublicKey, isVerified)
```
> استدعاء `bluetooth.updatePeerInfo` بالمعاملات peerID وnickname وnoisePublicKey وsigningPublicKey وisVerified، وقيمته هي ناتج كتلة المحاولة. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:222]

```
223:         } catch (_: Exception) {
```
> فتح كتلة التقاط الاستثناء (Exception) بلا اسم للمتغيّر. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:223]

```
224:             false
```
> قيمة كتلة الالتقاط هي «خطأ» (false). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:224]

```
225:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط الخاصة بـ `bleUpdated`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:225]

```
226:         val wifiUpdated = try {
```
> تعريف متغيّر ثابت اسمه «واي فاي مُحدَّث» (wifiUpdated) بفتح كتلة محاولة لإسناد قيمته. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:226]

```
227:             wifiService()?.updatePeerInfo(peerID, nickname, noisePublicKey, signingPublicKey, isVerified) == true
```
> قيمة الكتلة هي نتيجة مقارنة `wifiService()?.updatePeerInfo(...)` (باستدعاء آمن من العدم وبنفس المعاملات الخمسة) بـ `true`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:227]

```
228:         } catch (_: Exception) {
```
> فتح كتلة التقاط الاستثناء بلا اسم للمتغيّر. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:228]

```
229:             false
```
> قيمة كتلة الالتقاط هي «خطأ» (false). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:229]

```
230:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط الخاصة بـ `wifiUpdated`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:230]

```
231:         return bleUpdated || wifiUpdated
```
> إعادة نتيجة عملية «أو» المنطقية بين `bleUpdated` و`wifiUpdated`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:231]

```
232:     }
```
> إغلاق نطاق الدالة `updatePeerInfo`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:232]

```
233: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:233]

```
234:     override fun getIdentityFingerprint(): String = bluetooth.getIdentityFingerprint()
```
> تعريف دالة معاد تعريفها باسم «احصل على بصمة الهوية» (getIdentityFingerprint) تعيد نصاً (String) قيمته نتيجة استدعاء `bluetooth.getIdentityFingerprint()`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:234]

```
235: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:235]

```
236:     override fun getStaticNoisePublicKey(): ByteArray? {
```
> تعريف دالة معاد تعريفها باسم «احصل على مفتاح نويز العام الثابت» (getStaticNoisePublicKey) تعيد مصفوفة بايت قابلة لأن تكون عدماً. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:236]

```
237:         return bluetooth.getStaticNoisePublicKey() ?: wifiService()?.getStaticNoisePublicKey()
```
> إعادة `bluetooth.getStaticNoisePublicKey()`، وإن كانت عدماً فتُعاد `wifiService()?.getStaticNoisePublicKey()` (عبر مُعامل الدمج العدمي والاستدعاء الآمن). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:237]

```
238:     }
```
> إغلاق نطاق الدالة `getStaticNoisePublicKey`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:238]

```
239: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:239]

```
240:     override fun shouldShowEncryptionIcon(peerID: String): Boolean {
```
> تعريف دالة معاد تعريفها باسم «هل يُظهَر أيقونة التشفير» (shouldShowEncryptionIcon) تأخذ معاملاً نصياً اسمه peerID وتعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:240]

```
241:         return hasEstablishedSession(peerID)
```
> إعادة نتيجة استدعاء `hasEstablishedSession(peerID)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:241]

```
242:     }
```
> إغلاق نطاق الدالة `shouldShowEncryptionIcon`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:242]

```
243: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:243]

```
244:     override fun getEncryptedPeers(): List<String> {
```
> تعريف دالة معاد تعريفها باسم «احصل على النظراء المشفّرين» (getEncryptedPeers) تعيد قائمة (List) من نصوص. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:244]

```
245:         val encrypted = linkedSetOf<String>()
```
> تعريف متغيّر ثابت اسمه «مشفّر» (encrypted) يُسنَد إليه مجموعة مرتبطة فارغة (linkedSetOf) من نصوص. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:245]

```
246:         try { encrypted.addAll(bluetooth.getEncryptedPeers()) } catch (_: Exception) { }
```
> داخل كتلة محاولة يُضاف إلى `encrypted` كل عناصر `bluetooth.getEncryptedPeers()`، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:246]

```
247:         try { encrypted.addAll(wifiService()?.getEncryptedPeers().orEmpty()) } catch (_: Exception) { }
```
> داخل كتلة محاولة يُضاف إلى `encrypted` كل عناصر `wifiService()?.getEncryptedPeers()`، وإن كانت عدماً فقائمة فارغة (orEmpty)، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:247]

```
248:         mergedPeerIDs().filterTo(encrypted) { hasEstablishedSession(it) }
```
> استدعاء `mergedPeerIDs()` ثم تصفية عناصره إلى `encrypted` (filterTo) للذين يحقق لهم `hasEstablishedSession(it)` القيمة الصحيحة. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:248]

```
249:         return encrypted.toList()
```
> إعادة `encrypted` محوّلةً إلى قائمة (toList). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:249]

```
250:     }
```
> إغلاق نطاق الدالة `getEncryptedPeers`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:250]

```
251: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:251]

```
252:     override fun getDeviceAddressForPeer(peerID: String): String? {
```
> تعريف دالة معاد تعريفها باسم «احصل على عنوان الجهاز للنظير» (getDeviceAddressForPeer) تأخذ معاملاً نصياً اسمه peerID وتعيد نصاً قابلاً لأن يكون عدماً. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:252]

```
253:         return try { bluetooth.getDeviceAddressForPeer(peerID) } catch (_: Exception) { null }
```
> إعادة نتيجة `bluetooth.getDeviceAddressForPeer(peerID)` داخل كتلة محاولة، وعند الاستثناء قيمة العدم. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:253]

```
254:             ?: try { wifiService()?.getDeviceAddressForPeer(peerID) } catch (_: Exception) { null }
```
> وإن كان الناتج السابق عدماً (عبر مُعامل الدمج العدمي) فتُعاد نتيجة `wifiService()?.getDeviceAddressForPeer(peerID)` داخل كتلة محاولة، وعند الاستثناء قيمة العدم. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:254]

```
255:     }
```
> إغلاق نطاق الدالة `getDeviceAddressForPeer`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:255]

```
256: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:256]

```
257:     override fun getDeviceAddressToPeerMapping(): Map<String, String> {
```
> تعريف دالة معاد تعريفها باسم «احصل على ربط عنوان الجهاز بالنظير» (getDeviceAddressToPeerMapping) تعيد خريطة (Map) من نص إلى نص. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:257]

```
258:         val merged = linkedMapOf<String, String>()
```
> تعريف متغيّر ثابت اسمه «مدموج» (merged) يُسنَد إليه خريطة مرتبطة فارغة (linkedMapOf) من نص إلى نص. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:258]

```
259:         try { merged.putAll(wifiService()?.getDeviceAddressToPeerMapping().orEmpty()) } catch (_: Exception) { }
```
> داخل كتلة محاولة تُوضَع في `merged` كل أزواج `wifiService()?.getDeviceAddressToPeerMapping()`، وإن كانت عدماً فخريطة فارغة (orEmpty)، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:259]

```
260:         try { merged.putAll(bluetooth.getDeviceAddressToPeerMapping()) } catch (_: Exception) { }
```
> داخل كتلة محاولة تُوضَع في `merged` كل أزواج `bluetooth.getDeviceAddressToPeerMapping()`، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:260]

```
261:         return merged
```
> إعادة المتغيّر `merged`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:261]

```
262:     }
```
> إغلاق نطاق الدالة `getDeviceAddressToPeerMapping`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:262]

```
263: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:263]

```
264:     override fun printDeviceAddressesForPeers(): String {
```
> تعريف دالة معاد تعريفها باسم «اطبع عناوين الأجهزة للنظراء» (printDeviceAddressesForPeers) تعيد نصاً. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:264]

```
265:         return buildString {
```
> إعادة نتيجة بناء نص عبر `buildString` بفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:265]

```
266:             appendLine(bluetooth.printDeviceAddressesForPeers())
```
> إلحاق سطر (appendLine) بناتج `bluetooth.printDeviceAddressesForPeers()`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:266]

```
267:             wifiService()?.let {
```
> استدعاء آمن لـ `wifiService()` ثم تنفيذ كتلة `let` على الكائن غير العدمي. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:267]

```
268:                 appendLine()
```
> إلحاق سطر فارغ (appendLine بلا وسيط). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:268]

```
269:                 appendLine(it.printDeviceAddressesForPeers())
```
> إلحاق سطر بناتج `it.printDeviceAddressesForPeers()` حيث `it` هو خدمة الواي فاي. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:269]

```
270:             }
```
> إغلاق نطاق كتلة `let`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:270]

```
271:         }
```
> إغلاق نطاق كتلة `buildString`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:271]

```
272:     }
```
> إغلاق نطاق الدالة `printDeviceAddressesForPeers`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:272]

```
273: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:273]

```
274:     override fun getDebugStatus(): String {
```
> تعريف دالة معاد تعريفها باسم «احصل على حالة التنقيح» (getDebugStatus) تعيد نصاً. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:274]

```
275:         return buildString {
```
> إعادة نتيجة بناء نص عبر `buildString` بفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:275]

```
276:             appendLine("=== Unified Mesh Service Debug Status ===")
```
> إلحاق سطر بالنص الحرفي `"=== Unified Mesh Service Debug Status ==="`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:276]

```
277:             appendLine("My Peer ID: $myPeerID")
```
> إلحاق سطر بالنص `"My Peer ID: "` متبوعاً بقيمة المتغيّر `myPeerID` المُدمَجة. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:277]

```
278:             appendLine("Merged Peers: ${mergedPeerIDs().joinToString(", ")}")
```
> إلحاق سطر بالنص `"Merged Peers: "` متبوعاً بناتج `mergedPeerIDs().joinToString(", ")` المُدمَج (دمج العناصر بفاصلة ومسافة). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:278]

```
279:             appendLine()
```
> إلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:279]

```
280:             appendLine(bluetooth.getDebugStatus())
```
> إلحاق سطر بناتج `bluetooth.getDebugStatus()`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:280]

```
281:             wifiService()?.let {
```
> استدعاء آمن لـ `wifiService()` ثم تنفيذ كتلة `let` على الكائن غير العدمي. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:281]

```
282:                 appendLine()
```
> إلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:282]

```
283:                 appendLine(it.getDebugStatus())
```
> إلحاق سطر بناتج `it.getDebugStatus()` حيث `it` هو خدمة الواي فاي. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:283]

```
284:             }
```
> إغلاق نطاق كتلة `let`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:284]

```
285:         }
```
> إغلاق نطاق كتلة `buildString`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:285]

```
286:     }
```
> إغلاق نطاق الدالة `getDebugStatus`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:286]

```
287: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:287]

```
288:     override fun clearAllInternalData() {
```
> تعريف دالة معاد تعريفها باسم «امسح كل البيانات الداخلية» (clearAllInternalData) بلا معاملات وبلا نوع إرجاع مُصرَّح. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:288]

```
289:         try { bluetooth.clearAllInternalData() } catch (_: Exception) { }
```
> داخل كتلة محاولة يُستدعى `bluetooth.clearAllInternalData()`، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:289]

```
290:         try { wifiService()?.clearAllInternalData() } catch (_: Exception) { }
```
> داخل كتلة محاولة يُستدعى `wifiService()?.clearAllInternalData()` (باستدعاء آمن)، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:290]

```
291:     }
```
> إغلاق نطاق الدالة `clearAllInternalData`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:291]

```
292: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:292]

```
293:     override fun clearAllEncryptionData() {
```
> تعريف دالة معاد تعريفها باسم «امسح كل بيانات التشفير» (clearAllEncryptionData) بلا معاملات وبلا نوع إرجاع مُصرَّح. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:293]

```
294:         try { bluetooth.clearAllEncryptionData() } catch (_: Exception) { }
```
> داخل كتلة محاولة يُستدعى `bluetooth.clearAllEncryptionData()`، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:294]

```
295:         try { wifiService()?.clearAllEncryptionData() } catch (_: Exception) { }
```
> داخل كتلة محاولة يُستدعى `wifiService()?.clearAllEncryptionData()` (باستدعاء آمن)، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:295]

```
296:     }
```
> إغلاق نطاق الدالة `clearAllEncryptionData`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:296]

```
297: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:297]

```
298:     override fun didReceiveMessage(message: BitchatMessage) {
```
> تعريف دالة معاد تعريفها باسم «استُلِمت رسالة» (didReceiveMessage) تأخذ معاملاً اسمه «رسالة» (message) من نوع «رسالة بِت‌شات» (BitchatMessage). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:298]

```
299:         delegate?.didReceiveMessage(message)
```
> استدعاء آمن `delegate?.didReceiveMessage(message)` على المُفوَّض (delegate). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:299]

```
300:     }
```
> إغلاق نطاق الدالة `didReceiveMessage`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:300]

```
301: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:301]

```
302:     override fun didUpdatePeerList(peers: List<String>) {
```
> تعريف دالة معاد تعريفها باسم «حُدِّثت قائمة النظراء» (didUpdatePeerList) تأخذ معاملاً اسمه «النظراء» (peers) قائمةً من نصوص. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:302]

```
303:         delegate?.didUpdatePeerList(mergedPeerIDs().ifEmpty { peers.distinct() })
```
> استدعاء آمن `delegate?.didUpdatePeerList(...)` بوسيط هو `mergedPeerIDs()`، وإن كان فارغاً (ifEmpty) فيُستعمل `peers.distinct()` (العناصر المتمايزة). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:303]

```
304:     }
```
> إغلاق نطاق الدالة `didUpdatePeerList`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:304]

```
305: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:305]

```
306:     override fun didReceiveChannelLeave(channel: String, fromPeer: String) {
```
> تعريف دالة معاد تعريفها باسم «استُلِم مغادرة قناة» (didReceiveChannelLeave) تأخذ معاملاً نصياً اسمه «قناة» (channel) ومعاملاً نصياً اسمه «من نظير» (fromPeer). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:306]

```
307:         delegate?.didReceiveChannelLeave(channel, fromPeer)
```
> استدعاء آمن `delegate?.didReceiveChannelLeave(channel, fromPeer)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:307]

```
308:     }
```
> إغلاق نطاق الدالة `didReceiveChannelLeave`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:308]

```
309: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:309]

```
310:     override fun didReceiveDeliveryAck(messageID: String, recipientPeerID: String) {
```
> تعريف دالة معاد تعريفها باسم «استُلِم إقرار تسليم» (didReceiveDeliveryAck) تأخذ معاملاً نصياً اسمه «معرّف الرسالة» (messageID) ومعاملاً نصياً اسمه «معرّف النظير المستلِم» (recipientPeerID). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:310]

```
311:         delegate?.didReceiveDeliveryAck(messageID, recipientPeerID)
```
> استدعاء آمن `delegate?.didReceiveDeliveryAck(messageID, recipientPeerID)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:311]

```
312:     }
```
> إغلاق نطاق الدالة `didReceiveDeliveryAck`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:312]

```
313: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:313]

```
314:     override fun didReceiveReadReceipt(messageID: String, recipientPeerID: String) {
```
> تعريف دالة معاد تعريفها باسم «استُلِم إيصال قراءة» (didReceiveReadReceipt) تأخذ معاملاً نصياً اسمه messageID ومعاملاً نصياً اسمه recipientPeerID. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:314]

```
315:         delegate?.didReceiveReadReceipt(messageID, recipientPeerID)
```
> استدعاء آمن `delegate?.didReceiveReadReceipt(messageID, recipientPeerID)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:315]

```
316:     }
```
> إغلاق نطاق الدالة `didReceiveReadReceipt`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:316]

```
317: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:317]

```
318:     override fun didReceiveVerifyChallenge(peerID: String, payload: ByteArray, timestampMs: Long) {
```
> تعريف دالة معاد تعريفها باسم «استُلِم تحدّي تحقّق» (didReceiveVerifyChallenge) تأخذ معاملاً نصياً اسمه peerID ومعاملاً من مصفوفة بايت اسمه «الحمولة» (payload) ومعاملاً طويلاً (Long) اسمه «الطابع الزمني بالمللي ثانية» (timestampMs). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:318]

```
319:         delegate?.didReceiveVerifyChallenge(peerID, payload, timestampMs)
```
> استدعاء آمن `delegate?.didReceiveVerifyChallenge(peerID, payload, timestampMs)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:319]

```
320:     }
```
> إغلاق نطاق الدالة `didReceiveVerifyChallenge`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:320]

```
321: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:321]

```
322:     override fun didReceiveVerifyResponse(peerID: String, payload: ByteArray, timestampMs: Long) {
```
> تعريف دالة معاد تعريفها باسم «استُلِم ردّ تحقّق» (didReceiveVerifyResponse) تأخذ معاملاً نصياً اسمه peerID ومعاملاً من مصفوفة بايت اسمه payload ومعاملاً طويلاً اسمه timestampMs. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:322]

```
323:         delegate?.didReceiveVerifyResponse(peerID, payload, timestampMs)
```
> استدعاء آمن `delegate?.didReceiveVerifyResponse(peerID, payload, timestampMs)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:323]

```
324:     }
```
> إغلاق نطاق الدالة `didReceiveVerifyResponse`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:324]

```
325: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:325]

```
326:     override fun decryptChannelMessage(encryptedContent: ByteArray, channel: String): String? {
```
> تعريف دالة معاد تعريفها باسم «فُكّ تشفير رسالة القناة» (decryptChannelMessage) تأخذ معاملاً من مصفوفة بايت اسمه «المحتوى المشفّر» (encryptedContent) ومعاملاً نصياً اسمه channel وتعيد نصاً قابلاً لأن يكون عدماً. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:326]

```
327:         return delegate?.decryptChannelMessage(encryptedContent, channel)
```
> إعادة نتيجة الاستدعاء الآمن `delegate?.decryptChannelMessage(encryptedContent, channel)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:327]

```
328:     }
```
> إغلاق نطاق الدالة `decryptChannelMessage`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:328]

```
329: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:329]

```
330:     override fun getNickname(): String? = delegate?.getNickname()
```
> تعريف دالة معاد تعريفها باسم «احصل على الاسم المستعار» (getNickname) تعيد نصاً قابلاً لأن يكون عدماً قيمته نتيجة الاستدعاء الآمن `delegate?.getNickname()`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:330]

```
331: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:331]

```
332:     override fun isFavorite(peerID: String): Boolean = delegate?.isFavorite(peerID) ?: false
```
> تعريف دالة معاد تعريفها باسم «هل مُفضَّل» (isFavorite) تأخذ معاملاً نصياً اسمه peerID وتعيد قيمة منطقية هي نتيجة `delegate?.isFavorite(peerID)`، وإن كانت عدماً فقيمة «خطأ» (false) عبر مُعامل الدمج العدمي. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:332]

```
333: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:333]

```
334:     private fun mergedPeerIDs(): List<String> {
```
> تعريف دالة خاصة (private) باسم «معرّفات النظراء المدموجة» (mergedPeerIDs) تعيد قائمة من نصوص. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:334]

```
335:         val ids = linkedSetOf<String>()
```
> تعريف متغيّر ثابت اسمه «معرّفات» (ids) يُسنَد إليه مجموعة مرتبطة فارغة (linkedSetOf) من نصوص. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:335]

```
336:         try { ids.addAll(com.bitchat.android.services.AppStateStore.peers.value) } catch (_: Exception) { }
```
> داخل كتلة محاولة يُضاف إلى `ids` كل عناصر `com.bitchat.android.services.AppStateStore.peers.value`، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:336]

```
337:         try { ids.addAll(bluetooth.getPeerNicknames().keys) } catch (_: Exception) { }
```
> داخل كتلة محاولة يُضاف إلى `ids` مفاتيح (keys) خريطة `bluetooth.getPeerNicknames()`، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:337]

```
338:         try { ids.addAll(wifiService()?.getPeerNicknames()?.keys.orEmpty()) } catch (_: Exception) { }
```
> داخل كتلة محاولة يُضاف إلى `ids` مفاتيح خريطة `wifiService()?.getPeerNicknames()` (باستدعاء آمن)، وإن كانت عدماً فمجموعة فارغة (orEmpty)، وعند الاستثناء لا يُنفَّذ شيء. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:338]

```
339:         return ids.toList()
```
> إعادة `ids` محوّلةً إلى قائمة (toList). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:339]

```
340:     }
```
> إغلاق نطاق الدالة `mergedPeerIDs`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:340]

```
341: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:341]

```
342:     private fun wifiService(): MeshService? {
```
> تعريف دالة خاصة باسم «خدمة الواي فاي» (wifiService) تعيد كائناً من نوع «خدمة الشبكة» (MeshService) قابلاً لأن يكون عدماً. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:342]

```
343:         return try {
```
> بدء إعادة قيمة كتلة محاولة (try) بفتحها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:343]

```
344:             WifiAwareController.getService()?.also { service ->
```
> استدعاء آمن `WifiAwareController.getService()` ثم تنفيذ كتلة `also` على الكائن غير العدمي بمعامل اسمه «خدمة» (service). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:344]

```
345:                 if (delegate != null && service.delegate !== this) {
```
> شرط `if`: إذا كان `delegate` غير عدم وكان `service.delegate` لا يساوي مرجعياً (!==) هذا الكائن `this`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:345]

```
346:                     service.delegate = this
```
> إسناد `this` إلى `service.delegate`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:346]

```
347:                 }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:347]

```
348:             }
```
> إغلاق نطاق كتلة `also`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:348]

```
349:         } catch (_: Exception) {
```
> فتح كتلة التقاط الاستثناء بلا اسم للمتغيّر. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:349]

```
350:             null
```
> قيمة كتلة الالتقاط هي العدم (null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:350]

```
351:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:351]

```
352:     }
```
> إغلاق نطاق الدالة `wifiService`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:352]

```
353: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:353]

```
354:     private fun isBleEnabled(): Boolean {
```
> تعريف دالة خاصة باسم «هل البلوتوث مُفعَّل» (isBleEnabled) تعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:354]

```
355:         return try {
```
> بدء إعادة قيمة كتلة محاولة بفتحها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:355]

```
356:             com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().bleEnabled.value
```
> قيمة الكتلة هي `com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().bleEnabled.value`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:356]

```
357:         } catch (_: Exception) {
```
> فتح كتلة التقاط الاستثناء بلا اسم للمتغيّر. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:357]

```
358:             try { com.bitchat.android.ui.debug.DebugPreferenceManager.getBleEnabled(true) } catch (_: Exception) { true }
```
> داخل كتلة الالتقاط: قيمتها هي `com.bitchat.android.ui.debug.DebugPreferenceManager.getBleEnabled(true)` ضمن محاولة، وعند استثناء داخلي قيمة «صحيح» (true). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:358]

```
359:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:359]

```
360:     }
```
> إغلاق نطاق الدالة `isBleEnabled`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:360]

```
361: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:361]

```
362:     private fun isBleConnected(peerID: String): Boolean {
```
> تعريف دالة خاصة باسم «هل البلوتوث متّصل» (isBleConnected) تأخذ معاملاً نصياً اسمه peerID وتعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:362]

```
363:         return try { bluetooth.getPeerInfo(peerID)?.isConnected == true } catch (_: Exception) { false }
```
> إعادة نتيجة مقارنة `bluetooth.getPeerInfo(peerID)?.isConnected` (باستدعاء آمن) بـ `true` ضمن محاولة، وعند الاستثناء قيمة «خطأ» (false). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:363]

```
364:     }
```
> إغلاق نطاق الدالة `isBleConnected`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:364]

```
365: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:365]

```
366:     private fun isWifiConnected(peerID: String): Boolean {
```
> تعريف دالة خاصة باسم «هل الواي فاي متّصل» (isWifiConnected) تأخذ معاملاً نصياً اسمه peerID وتعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:366]

```
367:         return try { wifiService()?.getPeerInfo(peerID)?.isConnected == true } catch (_: Exception) { false }
```
> إعادة نتيجة مقارنة `wifiService()?.getPeerInfo(peerID)?.isConnected` (باستدعاءات آمنة) بـ `true` ضمن محاولة، وعند الاستثناء قيمة «خطأ» (false). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:367]

```
368:     }
```
> إغلاق نطاق الدالة `isWifiConnected`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:368]

```
369: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:369]

```
370:     private fun isBleReady(peerID: String): Boolean {
```
> تعريف دالة خاصة باسم «هل البلوتوث جاهز» (isBleReady) تأخذ معاملاً نصياً اسمه peerID وتعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:370]

```
371:         return isBleConnected(peerID) && hasEstablishedSessionOnBluetooth(peerID)
```
> إعادة نتيجة عملية «و» المنطقية بين `isBleConnected(peerID)` و`hasEstablishedSessionOnBluetooth(peerID)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:371]

```
372:     }
```
> إغلاق نطاق الدالة `isBleReady`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:372]

```
373: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:373]

```
374:     private fun isWifiReady(peerID: String): Boolean {
```
> تعريف دالة خاصة باسم «هل الواي فاي جاهز» (isWifiReady) تأخذ معاملاً نصياً اسمه peerID وتعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:374]

```
375:         return try {
```
> بدء إعادة قيمة كتلة محاولة بفتحها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:375]

```
376:             val wifi = wifiService()
```
> تعريف متغيّر ثابت اسمه «واي فاي» (wifi) يُسنَد إليه ناتج `wifiService()`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:376]

```
377:             wifi?.getPeerInfo(peerID)?.isConnected == true && wifi.hasEstablishedSession(peerID)
```
> قيمة الكتلة هي نتيجة عملية «و» المنطقية بين كون `wifi?.getPeerInfo(peerID)?.isConnected` يساوي `true` وبين `wifi.hasEstablishedSession(peerID)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:377]

```
378:         } catch (_: Exception) {
```
> فتح كتلة التقاط الاستثناء بلا اسم للمتغيّر. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:378]

```
379:             false
```
> قيمة كتلة الالتقاط هي «خطأ» (false). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:379]

```
380:         }
```
> إغلاق نطاق كتلة المحاولة/الالتقاط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:380]

```
381:     }
```
> إغلاق نطاق الدالة `isWifiReady`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:381]

```
382: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:382]

```
383:     private fun hasEstablishedSessionOnBluetooth(peerID: String): Boolean {
```
> تعريف دالة خاصة باسم «هل أُنشئت جلسة على البلوتوث» (hasEstablishedSessionOnBluetooth) تأخذ معاملاً نصياً اسمه peerID وتعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:383]

```
384:         return try { bluetooth.hasEstablishedSession(peerID) } catch (_: Exception) { false }
```
> إعادة نتيجة `bluetooth.hasEstablishedSession(peerID)` ضمن محاولة، وعند الاستثناء قيمة «خطأ» (false). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:384]

```
385:     }
```
> إغلاق نطاق الدالة `hasEstablishedSessionOnBluetooth`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:385]

```
386: }
```
> إغلاق نطاق الصنف (class) الذي يضم هذه الدوال. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:386]
