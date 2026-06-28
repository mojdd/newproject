# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt (الأسطر 201–276)

```
201:                     },
```
> إغلاق دالّة سهمية (lambda) متبوعة بفاصلة، أي نهاية وسيط ثم فاصل عن الوسيط التالي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:201]

```
202:                     onError = { error ->
```
> ضبط الوسيط المسمّى «عند الخطأ» (onError) بدالّة سهمية تأخذ بارامتراً اسمه «خطأ» (error). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:202]

```
203:                         Log.e(TAG, "❌ Loopback message failed: $error")
```
> استدعاء «Log.e» للتسجيل بمستوى الخطأ، بالوسم (TAG) ونص «❌ Loopback message failed: » متبوعاً بقيمة المتغيّر «error». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:203]

```
204:                     }
```
> إغلاق نطاق الدالّة السهمية الخاصة بـ «onError». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:204]

```
205:                 )
```
> إغلاق قائمة وسائط الاستدعاء (إغلاق قوس الدالّة المستدعاة). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:205]

```
206:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:206]

```
207:             } catch (e: Exception) {
```
> إغلاق كتلة «try» وبدء كتلة «catch» التي تلتقط استثناءً (Exception) في المتغيّر «e». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:207]

```
208:                 Log.e(TAG, "❌ Loopback test failed: ${e.message}", e)
```
> استدعاء «Log.e» للتسجيل بمستوى الخطأ، بالوسم (TAG) ونص «❌ Loopback test failed: » متبوعاً بـ «e.message» (رسالة الاستثناء)، وتمرير الاستثناء «e» كوسيط ثالث. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:208]

```
209:             }
```
> إغلاق نطاق كتلة «catch». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:209]

```
210:         }
```
> إغلاق نطاق الدالّة السهمية المُمرَّرة إلى «launch». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:210]

```
211:     }
```
> إغلاق نطاق الدالّة التي تحتوي الاستدعاء. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:211]

```
212:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:212]

```
213:     /**
```
> بدء تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:213]

```
214:      * Test sending a geohash message
```
> تعليق: اختبار إرسال رسالة جيوهاش (geohash). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:214]

```
215:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:215]

```
216:     fun testGeohashMessage() {
```
> تعريف دالّة عامة اسمها «testGeohashMessage» (اختبار رسالة الجيوهاش) بلا بارامترات. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:216]

```
217:         testScope.launch {
```
> استدعاء «launch» على «testScope» (نطاق الاختبار) لإطلاق كوروتين (coroutine) بدالّة سهمية لاحقة. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:217]

```
218:             try {
```
> بدء كتلة «try». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:218]

```
219:                 Log.i(TAG, "🌍 Testing geohash message...")
```
> استدعاء «Log.i» للتسجيل بمستوى المعلومات، بالوسم (TAG) ونص «🌍 Testing geohash message...». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:219]

```
220:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:220]

```
221:                 nostrClient.sendGeohashMessage(
```
> استدعاء الدالّة «sendGeohashMessage» (إرسال رسالة الجيوهاش) على «nostrClient» (عميل نوستر) مع بدء قائمة الوسائط. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:221]

```
222:                     content = "Test geohash message from Android at ${System.currentTimeMillis()}",
```
> ضبط الوسيط المسمّى «content» (المحتوى) بنص «Test geohash message from Android at » متبوعاً بقيمة «System.currentTimeMillis()» (الوقت الحالي بالمللي ثانية). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:222]

```
223:                     geohash = "u4pru",
```
> ضبط الوسيط المسمّى «geohash» (الجيوهاش) بالنص «u4pru». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:223]

```
224:                     nickname = "android-test",
```
> ضبط الوسيط المسمّى «nickname» (الاسم المستعار) بالنص «android-test». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:224]

```
225:                     onSuccess = {
```
> ضبط الوسيط المسمّى «عند النجاح» (onSuccess) بدالّة سهمية بلا بارامترات صريحة. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:225]

```
226:                         Log.i(TAG, "✅ Geohash message sent successfully")
```
> استدعاء «Log.i» للتسجيل بمستوى المعلومات، بالوسم (TAG) ونص «✅ Geohash message sent successfully». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:226]

```
227:                     },
```
> إغلاق الدالّة السهمية لـ «onSuccess» متبوعاً بفاصلة. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:227]

```
228:                     onError = { error ->
```
> ضبط الوسيط المسمّى «onError» (عند الخطأ) بدالّة سهمية تأخذ بارامتراً اسمه «error» (خطأ). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:228]

```
229:                         Log.e(TAG, "❌ Geohash message failed: $error")
```
> استدعاء «Log.e» للتسجيل بمستوى الخطأ، بالوسم (TAG) ونص «❌ Geohash message failed: » متبوعاً بقيمة المتغيّر «error». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:229]

```
230:                     }
```
> إغلاق نطاق الدالّة السهمية الخاصة بـ «onError». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:230]

```
231:                 )
```
> إغلاق قائمة وسائط استدعاء «sendGeohashMessage». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:231]

```
232:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:232]

```
233:             } catch (e: Exception) {
```
> إغلاق كتلة «try» وبدء كتلة «catch» التي تلتقط استثناءً (Exception) في المتغيّر «e». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:233]

```
234:                 Log.e(TAG, "❌ Geohash test failed: ${e.message}", e)
```
> استدعاء «Log.e» للتسجيل بمستوى الخطأ، بالوسم (TAG) ونص «❌ Geohash test failed: » متبوعاً بـ «e.message» (رسالة الاستثناء)، وتمرير الاستثناء «e» كوسيط ثالث. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:234]

```
235:             }
```
> إغلاق نطاق كتلة «catch». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:235]

```
236:         }
```
> إغلاق نطاق الدالّة السهمية المُمرَّرة إلى «launch». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:236]

```
237:     }
```
> إغلاق نطاق دالّة «testGeohashMessage». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:237]

```
238:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:238]

```
239:     /**
```
> بدء تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:239]

```
240:      * Get debug information about the Nostr client
```
> تعليق: الحصول على معلومات تصحيح (debug) عن عميل نوستر. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:240]

```
241:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:241]

```
242:     fun getDebugInfo(): String {
```
> تعريف دالّة عامة اسمها «getDebugInfo» (الحصول على معلومات التصحيح) بلا بارامترات وتُعيد قيمة من نوع «String» (سلسلة نصية). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:242]

```
243:         return buildString {
```
> إعادة ناتج «buildString» (بناء سلسلة نصية) مع دالّة سهمية لاحقة لبناء النص. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:243]

```
244:             appendLine("=== Nostr Client Debug Info ===")
```
> استدعاء «appendLine» (إلحاق سطر) لإضافة النص «=== Nostr Client Debug Info ===» يتبعه فاصل سطر. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:244]

```
245:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:245]

```
246:             val identity = nostrClient.getCurrentIdentity()
```
> تعريف متغيّر ثابت (val) اسمه «identity» (الهوية) وإسناد ناتج استدعاء «getCurrentIdentity» (الحصول على الهوية الحالية) على «nostrClient» إليه. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:246]

```
247:             if (identity != null) {
```
> شرط «if» يتحقق إن كان «identity» لا يساوي «null» (غير معدوم). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:247]

```
248:                 appendLine("Identity: ${identity.getShortNpub()}")
```
> استدعاء «appendLine» لإلحاق النص «Identity: » متبوعاً بناتج «identity.getShortNpub()» (الحصول على npub المختصر). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:248]

```
249:                 appendLine("Public Key: ${identity.publicKeyHex.take(16)}...")
```
> استدعاء «appendLine» لإلحاق النص «Public Key: » متبوعاً بأوّل ١٦ محرفاً من «identity.publicKeyHex» (المفتاح العام بالنظام السّت‌عشري) عبر «take(16)»، يليه «...». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:249]

```
250:                 appendLine("Created: ${java.util.Date(identity.createdAt)}")
```
> استدعاء «appendLine» لإلحاق النص «Created: » متبوعاً بكائن «java.util.Date» المبني من «identity.createdAt» (وقت الإنشاء). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:250]

```
251:             } else {
```
> إغلاق فرع «if» وبدء فرع «else». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:251]

```
252:                 appendLine("No identity loaded")
```
> استدعاء «appendLine» لإلحاق النص «No identity loaded». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:252]

```
253:             }
```
> إغلاق نطاق فرع «else». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:253]

```
254:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:254]

```
255:             val isInitialized = nostrClient.isInitialized.value ?: false
```
> تعريف متغيّر ثابت اسمه «isInitialized» (هل تمت التهيئة) وإسناد «nostrClient.isInitialized.value» إليه، وإن كان «null» يُسند «false» عبر معامل إلفيس (?:). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:255]

```
256:             appendLine("Initialized: $isInitialized")
```
> استدعاء «appendLine» لإلحاق النص «Initialized: » متبوعاً بقيمة «isInitialized». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:256]

```
257:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:257]

```
258:             val isConnected = nostrClient.relayConnectionStatus.value ?: false
```
> تعريف متغيّر ثابت اسمه «isConnected» (هل هو متصل) وإسناد «nostrClient.relayConnectionStatus.value» (حالة اتصال المُرحِّل) إليه، وإن كان «null» يُسند «false» عبر معامل إلفيس. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:258]

```
259:             appendLine("Relay Connected: $isConnected")
```
> استدعاء «appendLine» لإلحاق النص «Relay Connected: » متبوعاً بقيمة «isConnected». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:259]

```
260:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:260]

```
261:             val relays = nostrClient.relayInfo.value ?: emptyList()
```
> تعريف متغيّر ثابت اسمه «relays» (المُرحِّلات) وإسناد «nostrClient.relayInfo.value» (معلومات المُرحِّلات) إليه، وإن كان «null» يُسند قائمة فارغة «emptyList()» عبر معامل إلفيس. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:261]

```
262:             appendLine("Relays (${relays.size}):")
```
> استدعاء «appendLine» لإلحاق النص «Relays (» متبوعاً بحجم القائمة «relays.size» ثم «):». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:262]

```
263:             relays.forEach { relay ->
```
> استدعاء «forEach» (لكل عنصر) على «relays» بدالّة سهمية تأخذ بارامتراً اسمه «relay» (مُرحِّل). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:263]

```
264:                 appendLine("  ${relay.url}: ${if (relay.isConnected) "✅" else "❌"} (sent: ${relay.messagesSent}, received: ${relay.messagesReceived})")
```
> استدعاء «appendLine» لإلحاق نص يتضمن مسافتين ثم «relay.url» (عنوان المُرحِّل) ثم «: » ثم تعبير «if» يُنتج «✅» إن كان «relay.isConnected» صحيحاً وإلا «❌»، ثم « (sent: » مع «relay.messagesSent» (الرسائل المُرسَلة) و «, received: » مع «relay.messagesReceived» (الرسائل المُستقبَلة) ثم «)». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:264]

```
265:             }
```
> إغلاق نطاق الدالّة السهمية لـ «forEach». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:265]

```
266:         }
```
> إغلاق نطاق الدالّة السهمية لـ «buildString». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:266]

```
267:     }
```
> إغلاق نطاق دالّة «getDebugInfo». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:267]

```
268:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:268]

```
269:     /**
```
> بدء تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:269]

```
270:      * Shutdown test manager
```
> تعليق: إيقاف مدير الاختبار (test manager). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:270]

```
271:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:271]

```
272:     fun shutdown() {
```
> تعريف دالّة عامة اسمها «shutdown» (الإيقاف) بلا بارامترات. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:272]

```
273:         testScope.cancel()
```
> استدعاء «cancel» (إلغاء) على «testScope» لإلغاء نطاق الكوروتين. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:273]

```
274:         nostrClient.shutdown()
```
> استدعاء «shutdown» (الإيقاف) على «nostrClient». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:274]

```
275:     }
```
> إغلاق نطاق دالّة «shutdown». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:275]

```
276: }
```
> إغلاق نطاق الصنف (class) الحاوي «NostrTestManager». [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:276]
