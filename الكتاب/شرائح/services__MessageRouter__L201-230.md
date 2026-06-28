# شريحة — app/src/main/java/com/bitchat/android/services/MessageRouter.kt (الأسطر 201–230)

```
201:     private fun resolvePeerForNoiseHex(noiseHex: String, service: MeshService): String? {
```
> تُعرَّف دالة خاصة (private) اسمها «حلّ القرين من نويز هكس» (resolvePeerForNoiseHex) تأخذ وسيطاً نصياً اسمه noiseHex من نوع String ووسيطاً اسمه service من نوع MeshService، وتُعيد نصاً قابلاً للعدم (String?). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:201]

```
202:         return try {
```
> تُعيد الدالة نتيجة كتلة المحاولة (try). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:202]

```
203:             service.getPeerNicknames().keys.firstOrNull { pid ->
```
> تُستدعى دالة getPeerNicknames على الخدمة (service)، ثم يُؤخذ مفاتيحها (keys)، ويُطلب أول عنصر يُحقّق الشرط أو عدم (firstOrNull) مع متغيّر القرين اسمه pid. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:203]

```
204:                 val info = service.getPeerInfo(pid)
```
> يُعرَّف متغيّر ثابت (val) اسمه info ويُضبَط بنتيجة استدعاء getPeerInfo على الخدمة بالوسيط pid. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:204]

```
205:                 val keyHex = info?.noisePublicKey?.joinToString("") { b -> "%02x".format(b) }
```
> يُعرَّف متغيّر ثابت اسمه keyHex ويُضبَط بضمّ بايتات المفتاح العام لنويز (noisePublicKey) من info — إن لم يكن عدماً — في نص واحد بفاصل فارغ، حيث يُنسَّق كل بايت b بصيغة «02x» الست عشرية. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:205]

```
206:                 keyHex != null && keyHex.equals(noiseHex, ignoreCase = true)
```
> يُعاد شرط: أن keyHex لا يساوي عدماً وأن keyHex يساوي noiseHex بتجاهل حالة الأحرف (ignoreCase = true). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:206]

```
207:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:207]

```
208:         } catch (_: Exception) { null }
```
> تُغلَق كتلة المحاولة، وتُلتقط الاستثناءات (Exception) باسم متجاهَل (_)، وتُعاد القيمة عدماً (null). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:208]

```
209:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:209]

```
210: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:210]

```
211:     // Called when mesh peer list changes; attempt to flush any matching outbox entries
```
> تعليق: تُستدعى عند تغيّر قائمة قرناء الشبكة (mesh peer list)؛ تُحاول دفع أي مدخلات صندوق صادر (outbox) مطابِقة. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:211]

```
212:     fun onPeersUpdated(peers: List<String>) {
```
> تُعرَّف دالة اسمها «عند تحديث القرناء» (onPeersUpdated) تأخذ وسيطاً اسمه peers من نوع قائمة نصوص (List<String>). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:212]

```
213:         peers.forEach { pid ->
```
> يُمرّ على كل عنصر في peers (forEach) مع متغيّر القرين اسمه pid. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:213]

```
214:             flushOutboxFor(pid)
```
> تُستدعى دالة «دفع الصندوق الصادر لأجل» (flushOutboxFor) بالوسيط pid. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:214]

```
215:             val noiseHex = try {
```
> يُعرَّف متغيّر ثابت اسمه noiseHex ويُضبَط بنتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:215]

```
216:                 mesh.getPeerInfo(pid)?.noisePublicKey?.joinToString("") { b -> "%02x".format(b) }
```
> تُستدعى getPeerInfo على الشبكة (mesh) بالوسيط pid، ثم — إن لم تكن عدماً — يُضمّ المفتاح العام لنويز (noisePublicKey) في نص واحد بفاصل فارغ بتنسيق كل بايت b بصيغة «02x» الست عشرية. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:216]

```
217:             } catch (_: Exception) { null }
```
> تُغلَق كتلة المحاولة، وتُلتقط الاستثناءات (Exception) باسم متجاهَل (_)، وتُعاد القيمة عدماً (null). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:217]

```
218:             noiseHex?.let { flushOutboxFor(it) }
```
> إن لم يكن noiseHex عدماً فيُنفَّذ let وتُستدعى flushOutboxFor بالقيمة it. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:218]

```
219:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:219]

```
220:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:220]

```
221: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:221]

```
222:     // Called when a Noise session becomes established; flush both the mesh peerID and its noiseHex alias
```
> تعليق: تُستدعى عند نشوء جلسة نويز (Noise session) قائمة؛ ادفع كلاً من معرّف قرين الشبكة (peerID) ولقبه noiseHex. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:222]

```
223:     fun onSessionEstablished(peerID: String) {
```
> تُعرَّف دالة اسمها «عند تأسّس الجلسة» (onSessionEstablished) تأخذ وسيطاً اسمه peerID من نوع String. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:223]

```
224:         flushOutboxFor(peerID)
```
> تُستدعى flushOutboxFor بالوسيط peerID. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:224]

```
225:         val noiseHex = try {
```
> يُعرَّف متغيّر ثابت اسمه noiseHex ويُضبَط بنتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:225]

```
226:             mesh.getPeerInfo(peerID)?.noisePublicKey?.joinToString("") { b -> "%02x".format(b) }
```
> تُستدعى getPeerInfo على الشبكة (mesh) بالوسيط peerID، ثم — إن لم تكن عدماً — يُضمّ المفتاح العام لنويز (noisePublicKey) في نص واحد بفاصل فارغ بتنسيق كل بايت b بصيغة «02x» الست عشرية. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:226]

```
227:         } catch (_: Exception) { null }
```
> تُغلَق كتلة المحاولة، وتُلتقط الاستثناءات (Exception) باسم متجاهَل (_)، وتُعاد القيمة عدماً (null). [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:227]

```
228:         noiseHex?.let { flushOutboxFor(it) }
```
> إن لم يكن noiseHex عدماً فيُنفَّذ let وتُستدعى flushOutboxFor بالقيمة it. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:228]

```
229:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:229]

```
230: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/MessageRouter.kt:230]
