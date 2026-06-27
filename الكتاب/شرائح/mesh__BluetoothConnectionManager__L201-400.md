# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt (الأسطر 201–400)

```
201:             Log.e(TAG, "Missing Bluetooth permissions")
```
> يستدعي تسجيل خطأ (Log.e) بالوسم TAG والرسالة «Missing Bluetooth permissions» أي «أذونات بلوتوث مفقودة». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:201]

```
202:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:202]

```
203:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:203]

```
204:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:204]

```
205:         if (bluetoothAdapter?.isEnabled != true) {
```
> شرط if يفحص إن كانت الخاصية isEnabled لمحوّل البلوتوث (bluetoothAdapter) لا تساوي true (مع الوصول الآمن من الفراغ). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:205]

```
206:             Log.e(TAG, "Bluetooth is not enabled")
```
> يستدعي تسجيل خطأ (Log.e) بالوسم TAG والرسالة «Bluetooth is not enabled» أي «البلوتوث غير مفعَّل». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:206]

```
207:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:207]

```
208:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:208]

```
209:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:209]

```
210:         try {
```
> يبدأ كتلة try لمحاولة تنفيذ ما يليها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:210]

```
211:             isActive = true
```
> يضبط المتغيّر isActive (نشِط) إلى القيمة true. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:211]

```
212:             Log.d(TAG, "ConnectionManager activated (permissions and adapter OK)")
```
> يستدعي تسجيل تنقيح (Log.d) بالوسم TAG والرسالة «ConnectionManager activated (permissions and adapter OK)» أي «جرى تفعيل مدير الاتصال (الأذونات والمحوّل سليمة)». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:212]

```
213: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:213]

```
214:         // set the adapter's name to our 8-character peerID for iOS privacy, TODO: Make this configurable
```
> تعليق: «اضبط اسم المحوّل إلى معرّف النّظير (peerID) المؤلَّف من ٨ أحرف من أجل خصوصية iOS، مهمّة مؤجَّلة: اجعل هذا قابلاً للتهيئة». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:214]

```
215:         // try {
```
> تعليق: «try {». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:215]

```
216:         //     if (bluetoothAdapter?.name != myPeerID) {
```
> تعليق: «if (bluetoothAdapter?.name != myPeerID) {». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:216]

```
217:         //         bluetoothAdapter?.name = myPeerID
```
> تعليق: «bluetoothAdapter?.name = myPeerID». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:217]

```
218:         //         Log.d(TAG, "Set Bluetooth adapter name to peerID: $myPeerID for iOS compatibility.")
```
> تعليق: «Log.d(TAG, "Set Bluetooth adapter name to peerID: $myPeerID for iOS compatibility.")» أي تسجيل تنقيح بنصّ «جرى ضبط اسم محوّل البلوتوث إلى معرّف النّظير: $myPeerID لأجل توافق iOS». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:218]

```
219:         //     }
```
> تعليق: «}». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:219]

```
220:         // } catch (se: SecurityException) {
```
> تعليق: «} catch (se: SecurityException) {». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:220]

```
221:         //     Log.e(TAG, "Missing BLUETOOTH_CONNECT permission to set adapter name.", se)
```
> تعليق: «Log.e(TAG, "Missing BLUETOOTH_CONNECT permission to set adapter name.", se)» أي تسجيل خطأ بنصّ «إذن BLUETOOTH_CONNECT مفقود لضبط اسم المحوّل» مع الاستثناء se. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:221]

```
222:         // }
```
> تعليق: «}». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:222]

```
223: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:223]

```
224:             // Start all component managers
```
> تعليق: «ابدأ كل مديري المكوّنات». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:224]

```
225:             connectionScope.launch {
```
> يستدعي launch على نطاق الاتصال (connectionScope) لبدء كتلة كوروتين (coroutine) متزامنة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:225]

```
226:                 // Start connection tracker first
```
> تعليق: «ابدأ متعقّب الاتصال أولاً». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:226]

```
227:                 connectionTracker.start()
```
> يستدعي الدالة start على متعقّب الاتصال (connectionTracker). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:227]

```
228:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:228]

```
229:                 // Start power manager
```
> تعليق: «ابدأ مدير الطاقة». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:229]

```
230:                 powerManager.start()
```
> يستدعي الدالة start على مدير الطاقة (powerManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:230]

```
231:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:231]

```
232:                 // Start server/client based on debug settings
```
> تعليق: «ابدأ الخادم/العميل بناءً على إعدادات التنقيح». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:232]

```
233:                 val startServer = isGattServerEnabled()
```
> يعرّف متغيّراً ثابتاً startServer ويسنده قيمة استدعاء الدالة isGattServerEnabled (هل خادم GATT مفعَّل). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:233]

```
234:                 val startClient = isGattClientEnabled()
```
> يعرّف متغيّراً ثابتاً startClient ويسنده قيمة استدعاء الدالة isGattClientEnabled (هل عميل GATT مفعَّل). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:234]

```
235: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:235]

```
236:                 if (startServer) {
```
> شرط if يفحص إن كان startServer يساوي true. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:236]

```
237:                     if (!serverManager.start()) {
```
> شرط if يفحص إن كان استدعاء الدالة start على مدير الخادم (serverManager) يعيد false (النفي بـ !). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:237]

```
238:                         Log.e(TAG, "Failed to start server manager")
```
> يستدعي تسجيل خطأ (Log.e) بالوسم TAG والرسالة «Failed to start server manager» أي «فشل بدء مدير الخادم». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:238]

```
239:                         this@BluetoothConnectionManager.isActive = false
```
> يضبط الخاصية isActive للنسخة الخارجية BluetoothConnectionManager (عبر this@) إلى false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:239]

```
240:                         return@launch
```
> يعيد ويخرج من كتلة launch (الكوروتين) باستخدام التسمية @launch. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:240]

```
241:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:241]

```
242:                     Log.d(TAG, "GATT Server started")
```
> يستدعي تسجيل تنقيح (Log.d) بالوسم TAG والرسالة «GATT Server started» أي «بدأ خادم GATT». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:242]

```
243:                 } else {
```
> يبدأ فرع else (وإلّا) للشرط السابق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:243]

```
244:                     Log.i(TAG, "GATT Server disabled by debug settings; not starting")
```
> يستدعي تسجيل معلومة (Log.i) بالوسم TAG والرسالة «GATT Server disabled by debug settings; not starting» أي «خادم GATT معطَّل بإعدادات التنقيح؛ لن يبدأ». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:244]

```
245:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:245]

```
246: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:246]

```
247:                 if (startClient) {
```
> شرط if يفحص إن كان startClient يساوي true. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:247]

```
248:                     if (!clientManager.start()) {
```
> شرط if يفحص إن كان استدعاء الدالة start على مدير العميل (clientManager) يعيد false (النفي بـ !). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:248]

```
249:                         Log.e(TAG, "Failed to start client manager")
```
> يستدعي تسجيل خطأ (Log.e) بالوسم TAG والرسالة «Failed to start client manager» أي «فشل بدء مدير العميل». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:249]

```
250:                         this@BluetoothConnectionManager.isActive = false
```
> يضبط الخاصية isActive للنسخة الخارجية BluetoothConnectionManager (عبر this@) إلى false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:250]

```
251:                         return@launch
```
> يعيد ويخرج من كتلة launch (الكوروتين) باستخدام التسمية @launch. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:251]

```
252:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:252]

```
253:                     Log.d(TAG, "GATT Client started")
```
> يستدعي تسجيل تنقيح (Log.d) بالوسم TAG والرسالة «GATT Client started» أي «بدأ عميل GATT». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:253]

```
254:                 } else {
```
> يبدأ فرع else (وإلّا) للشرط السابق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:254]

```
255:                     Log.i(TAG, "GATT Client disabled by debug settings; not starting")
```
> يستدعي تسجيل معلومة (Log.i) بالوسم TAG والرسالة «GATT Client disabled by debug settings; not starting» أي «عميل GATT معطَّل بإعدادات التنقيح؛ لن يبدأ». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:255]

```
256:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:256]

```
257:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:257]

```
258:                 Log.i(TAG, "Bluetooth services started successfully")
```
> يستدعي تسجيل معلومة (Log.i) بالوسم TAG والرسالة «Bluetooth services started successfully» أي «بدأت خدمات البلوتوث بنجاح». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:258]

```
259:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:259]

```
260:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:260]

```
261:             return true
```
> يعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:261]

```
262:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:262]

```
263:         } catch (e: Exception) {
```
> يبدأ كتلة catch تلتقط استثناءً من نوع Exception باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:263]

```
264:             Log.e(TAG, "Failed to start Bluetooth services: ${e.message}")
```
> يستدعي تسجيل خطأ (Log.e) بالوسم TAG والرسالة «Failed to start Bluetooth services: ${e.message}» أي «فشل بدء خدمات البلوتوث» مع إدراج رسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:264]

```
265:             isActive = false
```
> يضبط المتغيّر isActive إلى false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:265]

```
266:             return false
```
> يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:266]

```
267:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:267]

```
268:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:268]

```
269: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:269]

```
270:     /**
```
> يبدأ تعليق توثيق (KDoc) متعدّد الأسطر. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:270]

```
271:      * Disable BLE without cancelling this manager's coroutine scope, so it can be re-enabled.
```
> تعليق: «عطِّل BLE دون إلغاء نطاق الكوروتين لهذا المدير، كي يمكن إعادة تفعيله». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:271]

```
272:      */
```
> يغلق تعليق التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:272]

```
273:     fun disableTransport() {
```
> يعرّف الدالة disableTransport (تعطيل النقل) دون وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:273]

```
274:         Log.i(TAG, "Disabling BLE transport")
```
> يستدعي تسجيل معلومة (Log.i) بالوسم TAG والرسالة «Disabling BLE transport» أي «جارٍ تعطيل نقل BLE». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:274]

```
275:         isActive = false
```
> يضبط المتغيّر isActive إلى false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:275]

```
276:         connectionScope.launch {
```
> يستدعي launch على نطاق الاتصال (connectionScope) لبدء كتلة كوروتين. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:276]

```
277:             clientManager.stop()
```
> يستدعي الدالة stop على مدير العميل (clientManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:277]

```
278:             serverManager.stop()
```
> يستدعي الدالة stop على مدير الخادم (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:278]

```
279:             connectionTracker.stop()
```
> يستدعي الدالة stop على متعقّب الاتصال (connectionTracker). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:279]

```
280:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:280]

```
281:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:281]

```
282:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:282]

```
283:     /**
```
> يبدأ تعليق توثيق (KDoc) متعدّد الأسطر. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:283]

```
284:      * Stop all Bluetooth services with proper cleanup
```
> تعليق: «أوقف كل خدمات البلوتوث مع تنظيف سليم». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:284]

```
285:      */
```
> يغلق تعليق التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:285]

```
286:     fun stopServices() {
```
> يعرّف الدالة stopServices (إيقاف الخدمات) دون وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:286]

```
287:         Log.i(TAG, "Stopping power-optimized Bluetooth services")
```
> يستدعي تسجيل معلومة (Log.i) بالوسم TAG والرسالة «Stopping power-optimized Bluetooth services» أي «جارٍ إيقاف خدمات البلوتوث المحسَّنة للطاقة». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:287]

```
288:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:288]

```
289:         isActive = false
```
> يضبط المتغيّر isActive إلى false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:289]

```
290:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:290]

```
291:         connectionScope.launch {
```
> يستدعي launch على نطاق الاتصال (connectionScope) لبدء كتلة كوروتين. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:291]

```
292:             Log.d(TAG, "Stopping client/server and power components...")
```
> يستدعي تسجيل تنقيح (Log.d) بالوسم TAG والرسالة «Stopping client/server and power components...» أي «جارٍ إيقاف مكوّنات العميل/الخادم والطاقة...». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:292]

```
293:             // Stop component managers
```
> تعليق: «أوقف مديري المكوّنات». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:293]

```
294:             clientManager.stop()
```
> يستدعي الدالة stop على مدير العميل (clientManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:294]

```
295:             serverManager.stop()
```
> يستدعي الدالة stop على مدير الخادم (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:295]

```
296:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:296]

```
297:             // Stop power manager
```
> تعليق: «أوقف مدير الطاقة». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:297]

```
298:             powerManager.stop()
```
> يستدعي الدالة stop على مدير الطاقة (powerManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:298]

```
299:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:299]

```
300:             // Stop connection tracker
```
> تعليق: «أوقف متعقّب الاتصال». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:300]

```
301:             connectionTracker.stop()
```
> يستدعي الدالة stop على متعقّب الاتصال (connectionTracker). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:301]

```
302:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:302]

```
303:             // Cancel the coroutine scope
```
> تعليق: «ألغِ نطاق الكوروتين». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:303]

```
304:             connectionScope.cancel()
```
> يستدعي الدالة cancel على نطاق الاتصال (connectionScope) لإلغائه. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:304]

```
305:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:305]

```
306:             Log.i(TAG, "All Bluetooth services stopped")
```
> يستدعي تسجيل معلومة (Log.i) بالوسم TAG والرسالة «All Bluetooth services stopped» أي «أُوقفت كل خدمات البلوتوث». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:306]

```
307:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:307]

```
308:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:308]

```
309: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:309]

```
310:     /**
```
> يبدأ تعليق توثيق (KDoc) متعدّد الأسطر. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:310]

```
311:      * Indicates whether this instance can be safely reused for a future start.
```
> تعليق: «يبيّن إن كانت هذه النسخة قابلة لإعادة الاستخدام بأمان لبدء مستقبلي». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:311]

```
312:      * Returns false if its coroutine scope has been cancelled.
```
> تعليق: «يعيد false إذا أُلغي نطاق الكوروتين الخاص به». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:312]

```
313:      */
```
> يغلق تعليق التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:313]

```
314:     fun isReusable(): Boolean {
```
> يعرّف الدالة isReusable (قابل لإعادة الاستخدام) التي تعيد قيمة من نوع Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:314]

```
315:         val active = connectionScope.isActive
```
> يعرّف متغيّراً ثابتاً active ويسنده قيمة الخاصية isActive لنطاق الاتصال (connectionScope). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:315]

```
316:         if (!active) {
```
> شرط if يفحص إن كان active يساوي false (النفي بـ !). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:316]

```
317:             Log.d(TAG, "BluetoothConnectionManager isReusable=false (scope cancelled)")
```
> يستدعي تسجيل تنقيح (Log.d) بالوسم TAG والرسالة «BluetoothConnectionManager isReusable=false (scope cancelled)» أي «BluetoothConnectionManager قابل لإعادة الاستخدام=false (النطاق مُلغى)». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:317]

```
318:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:318]

```
319:         return active
```
> يعيد قيمة المتغيّر active. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:319]

```
320:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:320]

```
321:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:321]

```
322:     /**
```
> يبدأ تعليق توثيق (KDoc) متعدّد الأسطر. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:322]

```
323:      * Broadcast packet to connected devices with connection limit enforcement
```
> تعليق: «بثّ الحزمة إلى الأجهزة المتّصلة مع فرض حدّ الاتصالات». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:323]

```
324:      * Automatically fragments large packets to fit within BLE MTU limits
```
> تعليق: «يجزّئ تلقائياً الحزم الكبيرة لتناسب حدود MTU الخاصة بـ BLE». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:324]

```
325:      */
```
> يغلق تعليق التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:325]

```
326:     fun broadcastPacket(routed: RoutedPacket) {
```
> يعرّف الدالة broadcastPacket (بثّ الحزمة) ذات وسيط routed من نوع RoutedPacket (حزمة موجَّهة). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:326]

```
327:         if (!isActive || !isBleTransportEnabled()) return
```
> شرط if يعيد (يخرج) إذا كان isActive يساوي false أو كان استدعاء isBleTransportEnabled (هل نقل BLE مفعَّل) يعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:327]

```
328:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:328]

```
329:         packetBroadcaster.broadcastPacket(
```
> يستدعي الدالة broadcastPacket على باثّ الحزم (packetBroadcaster) بفتح قائمة وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:329]

```
330:             routed,
```
> يمرّر الوسيط routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:330]

```
331:             serverManager.getGattServer(),
```
> يمرّر نتيجة استدعاء الدالة getGattServer على مدير الخادم (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:331]

```
332:             serverManager.getCharacteristic()
```
> يمرّر نتيجة استدعاء الدالة getCharacteristic على مدير الخادم (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:332]

```
333:         )
```
> يغلق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:333]

```
334:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:334]

```
335: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:335]

```
336:     fun sendToPeer(peerID: String, routed: RoutedPacket): Boolean {
```
> يعرّف الدالة sendToPeer (الإرسال إلى النّظير) بوسيطين peerID من نوع String وrouted من نوع RoutedPacket، وتعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:336]

```
337:         if (!isActive || !isBleTransportEnabled()) return false
```
> شرط if يعيد القيمة false إذا كان isActive يساوي false أو كان استدعاء isBleTransportEnabled يعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:337]

```
338:         return packetBroadcaster.sendToPeer(
```
> يعيد نتيجة استدعاء الدالة sendToPeer على باثّ الحزم (packetBroadcaster) بفتح قائمة وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:338]

```
339:             peerID,
```
> يمرّر الوسيط peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:339]

```
340:             routed,
```
> يمرّر الوسيط routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:340]

```
341:             serverManager.getGattServer(),
```
> يمرّر نتيجة استدعاء الدالة getGattServer على مدير الخادم (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:341]

```
342:             serverManager.getCharacteristic()
```
> يمرّر نتيجة استدعاء الدالة getCharacteristic على مدير الخادم (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:342]

```
343:         )
```
> يغلق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:343]

```
344:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:344]

```
345: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:345]

```
346:     fun cancelTransfer(transferId: String): Boolean {
```
> يعرّف الدالة cancelTransfer (إلغاء النقل) بوسيط transferId من نوع String، وتعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:346]

```
347:         return packetBroadcaster.cancelTransfer(transferId)
```
> يعيد نتيجة استدعاء الدالة cancelTransfer على باثّ الحزم (packetBroadcaster) مع الوسيط transferId. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:347]

```
348:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:348]

```
349: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:349]

```
350:     /**
```
> يبدأ تعليق توثيق (KDoc) متعدّد الأسطر. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:350]

```
351:      * Send a packet directly to a specific peer, without broadcasting to others.
```
> تعليق: «أرسل حزمة مباشرة إلى نظير محدّد، دون البثّ إلى الآخرين». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:351]

```
352:      */
```
> يغلق تعليق التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:352]

```
353:     fun sendPacketToPeer(peerID: String, packet: BitchatPacket): Boolean {
```
> يعرّف الدالة sendPacketToPeer (إرسال الحزمة إلى النّظير) بوسيطين peerID من نوع String وpacket من نوع BitchatPacket، وتعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:353]

```
354:         if (!isActive || !isBleTransportEnabled()) return false
```
> شرط if يعيد القيمة false إذا كان isActive يساوي false أو كان استدعاء isBleTransportEnabled يعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:354]

```
355:         return packetBroadcaster.sendPacketToPeer(
```
> يعيد نتيجة استدعاء الدالة sendPacketToPeer على باثّ الحزم (packetBroadcaster) بفتح قائمة وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:355]

```
356:             RoutedPacket(packet),
```
> يمرّر كائناً جديداً RoutedPacket مبنيّاً من الوسيط packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:356]

```
357:             peerID,
```
> يمرّر الوسيط peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:357]

```
358:             serverManager.getGattServer(),
```
> يمرّر نتيجة استدعاء الدالة getGattServer على مدير الخادم (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:358]

```
359:             serverManager.getCharacteristic()
```
> يمرّر نتيجة استدعاء الدالة getCharacteristic على مدير الخادم (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:359]

```
360:         )
```
> يغلق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:360]

```
361:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:361]

```
362:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:362]

```
363: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:363]

```
364:     // Expose role controls for debug UI
```
> تعليق: «اكشف ضوابط الدور لواجهة التنقيح». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:364]

```
365:     fun startServer() {
```
> يعرّف الدالة startServer (بدء الخادم) دون وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:365]

```
366:         if (!isActive || !isBleTransportEnabled()) return
```
> شرط if يعيد (يخرج) إذا كان isActive يساوي false أو كان استدعاء isBleTransportEnabled يعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:366]

```
367:         connectionScope.launch { if (isGattServerEnabled()) serverManager.start() }
```
> يستدعي launch على نطاق الاتصال (connectionScope) لتشغيل كتلة كوروتين تستدعي serverManager.start إن كان isGattServerEnabled يعيد true. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:367]

```
368:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:368]

```
369:     fun stopServer() { connectionScope.launch { serverManager.stop() } }
```
> يعرّف الدالة stopServer (إيقاف الخادم) التي تستدعي launch على نطاق الاتصال لتشغيل كتلة كوروتين تستدعي serverManager.stop. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:369]

```
370:     fun startClient() {
```
> يعرّف الدالة startClient (بدء العميل) دون وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:370]

```
371:         if (!isActive || !isBleTransportEnabled()) return
```
> شرط if يعيد (يخرج) إذا كان isActive يساوي false أو كان استدعاء isBleTransportEnabled يعيد false. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:371]

```
372:         connectionScope.launch { if (isGattClientEnabled()) clientManager.start() }
```
> يستدعي launch على نطاق الاتصال (connectionScope) لتشغيل كتلة كوروتين تستدعي clientManager.start إن كان isGattClientEnabled يعيد true. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:372]

```
373:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:373]

```
374:     fun stopClient() { connectionScope.launch { clientManager.stop() } }
```
> يعرّف الدالة stopClient (إيقاف العميل) التي تستدعي launch على نطاق الاتصال لتشغيل كتلة كوروتين تستدعي clientManager.stop. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:374]

```
375: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:375]

```
376:     // Inject nickname resolver for broadcaster logs
```
> تعليق: «احقن مُحلّل الاسم المستعار لسجلّات الباثّ». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:376]

```
377:     fun setNicknameResolver(resolver: (String) -> String?) { packetBroadcaster.setNicknameResolver(resolver) }
```
> يعرّف الدالة setNicknameResolver (ضبط مُحلّل الاسم المستعار) بوسيط resolver وهو دالة تأخذ String وتعيد String?، وتستدعي packetBroadcaster.setNicknameResolver مع تمرير resolver. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:377]

```
378: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:378]

```
379:     // Debug snapshots for connected devices
```
> تعليق: «لقطات تنقيح للأجهزة المتّصلة». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:379]

```
380:     fun getConnectedDeviceEntries(): List<Triple<String, Boolean, Int?>> {
```
> يعرّف الدالة getConnectedDeviceEntries (الحصول على مدخلات الأجهزة المتّصلة) التي تعيد قائمة List من ثلاثيّات Triple بأنواع String وBoolean وInt?. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:380]

```
381:         return try {
```
> يعيد نتيجة كتلة try (تعبير try). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:381]

```
382:             connectionTracker.getConnectedDevices().values.map { dc ->
```
> يستدعي getConnectedDevices على متعقّب الاتصال (connectionTracker) ثم يأخذ values ويطبّق map على كل عنصر باسم dc. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:382]

```
383:                 val rssi = if (dc.rssi != Int.MIN_VALUE) dc.rssi else null
```
> يعرّف متغيّراً ثابتاً rssi يساوي dc.rssi إن كان لا يساوي Int.MIN_VALUE، وإلّا يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:383]

```
384:                 Triple(dc.device.address, dc.isClient, rssi)
```
> ينشئ ثلاثيّة Triple من dc.device.address وdc.isClient وrssi. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:384]

```
385:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:385]

```
386:         } catch (e: Exception) {
```
> يبدأ كتلة catch تلتقط استثناءً من نوع Exception باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:386]

```
387:             emptyList()
```
> يعيد قائمة فارغة عبر استدعاء emptyList. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:387]

```
388:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:388]

```
389:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:389]

```
390: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:390]

```
391:     // Expose local adapter address for debug UI
```
> تعليق: «اكشف عنوان المحوّل المحلّي لواجهة التنقيح». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:391]

```
392:     fun getLocalAdapterAddress(): String? = try { bluetoothAdapter?.address } catch (e: Exception) { null }
```
> يعرّف الدالة getLocalAdapterAddress (الحصول على عنوان المحوّل المحلّي) التي تعيد String? وقيمتها نتيجة كتلة try تأخذ bluetoothAdapter?.address، وفي حال استثناء Exception تعيد null. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:392]

```
393: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:393]

```
394:     fun isClientConnection(address: String): Boolean? {
```
> يعرّف الدالة isClientConnection (هل الاتصال عميل) بوسيط address من نوع String، وتعيد Boolean?. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:394]

```
395:         return try { connectionTracker.getConnectedDevices()[address]?.isClient } catch (e: Exception) { null }
```
> يعيد نتيجة كتلة try التي تستدعي getConnectedDevices على متعقّب الاتصال وتقرأ العنصر ذا المفتاح address ثم خاصيته isClient (بوصول آمن)، وفي حال استثناء Exception تعيد null. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:395]

```
396:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:396]

```
397: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:397]

```
398:     /**
```
> يبدأ تعليق توثيق (KDoc) متعدّد الأسطر. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:398]

```
399:      * Public: connect/disconnect helpers for debug UI
```
> تعليق: «عام: مساعِدات الاتصال/قطع الاتصال لواجهة التنقيح». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:399]

```
400:      */
```
> يغلق تعليق التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:400]
