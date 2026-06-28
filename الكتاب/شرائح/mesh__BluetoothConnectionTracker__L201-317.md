# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt (الأسطر 201–317)

```
201:         if (servers.size > maxServer) {
```
> شرط (if): إذا كان حجم قائمة الخوادم (servers) أكبر من الحد الأقصى للخادم (maxServer). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:201]

```
202:             toEvict.addAll(servers.take(servers.size - maxServer))
```
> يُضيف إلى قائمة الطرد (toEvict) كل عناصر أول جزء من الخوادم بعدد يساوي (حجم الخوادم ناقص maxServer) عبر take. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:202]

```
203:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:203]

```
204:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:204]

```
205:         // 2. Enforce Overall Limit
```
> تعليق: «2. فرض الحد الإجمالي». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:205]

```
206:         // Count how many would remain after the above evictions
```
> تعليق: «احسب كم سيبقى بعد عمليات الطرد أعلاه». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:206]

```
207:         val remaining = currentDevices.filter { !toEvict.contains(it) }
```
> يُعرّف ثابتاً (val) باسم الباقي (remaining) قيمته نتيجة تصفية (filter) الأجهزة الحالية (currentDevices) بإبقاء كل عنصر لا تحتويه قائمة الطرد (toEvict). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:207]

```
208:         if (remaining.size > maxOverall) {
```
> شرط (if): إذا كان حجم الباقي (remaining) أكبر من الحد الإجمالي الأقصى (maxOverall). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:208]

```
209:             val excessCount = remaining.size - maxOverall
```
> يُعرّف ثابتاً باسم عدد الفائض (excessCount) قيمته حجم الباقي ناقص maxOverall. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:209]

```
210:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:210]

```
211:             // Explicitly prefer evicting clients first
```
> تعليق: «فضّل صراحةً طرد العملاء أولاً». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:211]

```
212:             val clientCandidates = remaining.filter { it.isClient }.sortedBy { it.connectedAt }
```
> يُعرّف ثابتاً باسم مرشّحي العملاء (clientCandidates) قيمته الباقي مصفّى بإبقاء ما خاصيته isClient ثم مرتّباً تصاعدياً (sortedBy) حسب وقت الاتصال (connectedAt). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:212]

```
213:             val serverCandidates = remaining.filter { !it.isClient }.sortedBy { it.connectedAt }
```
> يُعرّف ثابتاً باسم مرشّحي الخوادم (serverCandidates) قيمته الباقي مصفّى بإبقاء ما خاصيته isClient غير صحيحة ثم مرتّباً تصاعدياً حسب وقت الاتصال (connectedAt). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:213]

```
214:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:214]

```
215:             var needed = excessCount
```
> يُعرّف متغيّراً (var) باسم المطلوب (needed) قيمته الابتدائية عدد الفائض (excessCount). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:215]

```
216:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:216]

```
217:             // Take from clients first
```
> تعليق: «خُذ من العملاء أولاً». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:217]

```
218:             val fromClients = clientCandidates.take(needed)
```
> يُعرّف ثابتاً باسم المأخوذ من العملاء (fromClients) قيمته أول عناصر مرشّحي العملاء بعدد يساوي المطلوب (needed) عبر take. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:218]

```
219:             toEvict.addAll(fromClients)
```
> يُضيف إلى قائمة الطرد (toEvict) كل عناصر المأخوذ من العملاء (fromClients). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:219]

```
220:             needed -= fromClients.size
```
> يُنقص قيمة المطلوب (needed) بمقدار حجم المأخوذ من العملاء (fromClients). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:220]

```
221:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:221]

```
222:             // If still need more, take from servers
```
> تعليق: «إن بقي مطلوب فخُذ من الخوادم». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:222]

```
223:             if (needed > 0) {
```
> شرط (if): إذا كان المطلوب (needed) أكبر من صفر. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:223]

```
224:                 val fromServers = serverCandidates.take(needed)
```
> يُعرّف ثابتاً باسم المأخوذ من الخوادم (fromServers) قيمته أول عناصر مرشّحي الخوادم بعدد يساوي المطلوب (needed) عبر take. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:224]

```
225:                 toEvict.addAll(fromServers)
```
> يُضيف إلى قائمة الطرد (toEvict) كل عناصر المأخوذ من الخوادم (fromServers). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:225]

```
226:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:226]

```
227:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:227]

```
228:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:228]

```
229:         return toEvict.toList()
```
> يُعيد (return) قائمة الطرد (toEvict) محوّلةً إلى قائمة (toList). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:229]

```
230:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:230]

```
231:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:231]

```
232:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:232]

```
233:      * Clean up a specific device connection
```
> تعليق: «نظّف اتصال جهاز محدّد». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:233]

```
234:      */
```
> تعليق: نهاية كتلة التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:234]

```
235:     fun cleanupDeviceConnection(deviceAddress: String) {
```
> يُعرّف دالة (fun) باسم تنظيف اتصال الجهاز (cleanupDeviceConnection) تستقبل وسيطاً نصّياً (String) باسم عنوان الجهاز (deviceAddress). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:235]

```
236:         connectedDevices.remove(deviceAddress)?.let { deviceConn ->
```
> يُزيل من خريطة الأجهزة المتصلة (connectedDevices) المدخل بمفتاح عنوان الجهاز (deviceAddress)، وإن لم تكن النتيجة null ينفّذ كتلة let مسمّياً القيمة اتصال الجهاز (deviceConn). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:236]

```
237:             subscribedDevices.removeAll { it.address == deviceAddress }
```
> يُزيل من الأجهزة المشتركة (subscribedDevices) كل عنصر يساوي عنوانه (address) عنوان الجهاز (deviceAddress) عبر removeAll. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:237]

```
238:             addressPeerMap.remove(deviceAddress)
```
> يُزيل من خريطة العنوان إلى النظير (addressPeerMap) المدخل بمفتاح عنوان الجهاز (deviceAddress). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:238]

```
239:         }
```
> إغلاق نطاق (إغلاق كتلة let). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:239]

```
240:         firstAnnounceSeen.remove(deviceAddress)
```
> يُزيل من خريطة رؤية أول إعلان (firstAnnounceSeen) المدخل بمفتاح عنوان الجهاز (deviceAddress). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:240]

```
241:         Log.d(TAG, "Cleaned up device connection for $deviceAddress")
```
> يستدعي تسجيلاً تصحيحياً (Log.d) بالوسم (TAG) ونصّ «Cleaned up device connection for» متبوعاً بقيمة عنوان الجهاز (deviceAddress). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:241]

```
242:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:242]

```
243:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:243]

```
244:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:244]

```
245:      * Clean up all connections
```
> تعليق: «نظّف كل الاتصالات». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:245]

```
246:      */
```
> تعليق: نهاية كتلة التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:246]

```
247:     private fun cleanupAllConnections() {
```
> يُعرّف دالة خاصة (private fun) باسم تنظيف كل الاتصالات (cleanupAllConnections) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:247]

```
248:         connectedDevices.values.forEach { deviceConn ->
```
> يمرّ على قيم خريطة الأجهزة المتصلة (connectedDevices.values) عبر forEach مسمّياً كل عنصر اتصال الجهاز (deviceConn). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:248]

```
249:             deviceConn.gatt?.disconnect()
```
> يستدعي على كائن gatt الخاص باتصال الجهاز (deviceConn)، إن لم يكن null، دالة قطع الاتصال (disconnect). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:249]

```
250:         }
```
> إغلاق نطاق (إغلاق كتلة forEach). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:250]

```
251:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:251]

```
252:         connectionScope.launch {
```
> يُطلق (launch) مهمّة متزامنة (coroutine) على نطاق الاتصال (connectionScope). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:252]

```
253:             delay(CLEANUP_DELAY)
```
> يستدعي تأخيراً (delay) بمقدار ثابت تأخير التنظيف (CLEANUP_DELAY). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:253]

```
254:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:254]

```
255:             connectedDevices.values.forEach { deviceConn ->
```
> يمرّ على قيم خريطة الأجهزة المتصلة (connectedDevices.values) عبر forEach مسمّياً كل عنصر اتصال الجهاز (deviceConn). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:255]

```
256:                 try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:256]

```
257:                     deviceConn.gatt?.close()
```
> يستدعي على كائن gatt الخاص باتصال الجهاز (deviceConn)، إن لم يكن null، دالة الإغلاق (close). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:257]

```
258:                 } catch (e: Exception) {
```
> يلتقط (catch) استثناءً (Exception) مسمّياً إيّاه e. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:258]

```
259:                     Log.w(TAG, "Error closing GATT during cleanup: ${e.message}")
```
> يستدعي تسجيل تحذير (Log.w) بالوسم (TAG) ونصّ «Error closing GATT during cleanup:» متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:259]

```
260:                 }
```
> إغلاق نطاق (إغلاق كتلة catch). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:260]

```
261:             }
```
> إغلاق نطاق (إغلاق كتلة forEach). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:261]

```
262:         }
```
> إغلاق نطاق (إغلاق كتلة launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:262]

```
263:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:263]

```
264:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:264]

```
265:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:265]

```
266:      * Clear all connection tracking
```
> تعليق: «امسح كل تتبّع الاتصالات». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:266]

```
267:      */
```
> تعليق: نهاية كتلة التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:267]

```
268:     private fun clearAllConnections() {
```
> يُعرّف دالة خاصة (private fun) باسم مسح كل الاتصالات (clearAllConnections) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:268]

```
269:         connectedDevices.clear()
```
> يستدعي مسح (clear) خريطة الأجهزة المتصلة (connectedDevices). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:269]

```
270:         subscribedDevices.clear()
```
> يستدعي مسح (clear) الأجهزة المشتركة (subscribedDevices). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:270]

```
271:         addressPeerMap.clear()
```
> يستدعي مسح (clear) خريطة العنوان إلى النظير (addressPeerMap). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:271]

```
272:         pendingConnections.clear()
```
> يستدعي مسح (clear) الاتصالات المعلّقة (pendingConnections). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:272]

```
273:         scanRSSI.clear()
```
> يستدعي مسح (clear) خريطة قوة إشارة المسح (scanRSSI). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:273]

```
274:         firstAnnounceSeen.clear()
```
> يستدعي مسح (clear) خريطة رؤية أول إعلان (firstAnnounceSeen). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:274]

```
275:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:275]

```
276:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:276]

```
277:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:277]

```
278:      * Mark that we have received the first ANNOUNCE over this device connection.
```
> تعليق: «علّم أننا استقبلنا أول إعلان (ANNOUNCE) عبر اتصال هذا الجهاز». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:278]

```
279:      */
```
> تعليق: نهاية كتلة التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:279]

```
280:     fun noteAnnounceReceived(deviceAddress: String) {
```
> يُعرّف دالة (fun) باسم تسجيل استقبال الإعلان (noteAnnounceReceived) تستقبل وسيطاً نصّياً (String) باسم عنوان الجهاز (deviceAddress). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:280]

```
281:         firstAnnounceSeen[deviceAddress] = true
```
> يضبط في خريطة رؤية أول إعلان (firstAnnounceSeen) قيمة المفتاح عنوان الجهاز (deviceAddress) إلى true. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:281]

```
282:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:282]

```
283:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:283]

```
284:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:284]

```
285:      * Check whether the first ANNOUNCE has been seen for a device connection.
```
> تعليق: «تحقّق مما إذا كان أول إعلان (ANNOUNCE) قد رُئي لاتصال جهاز». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:285]

```
286:      */
```
> تعليق: نهاية كتلة التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:286]

```
287:     fun hasSeenFirstAnnounce(deviceAddress: String): Boolean {
```
> يُعرّف دالة (fun) باسم هل رُئي أول إعلان (hasSeenFirstAnnounce) تستقبل وسيطاً نصّياً (String) باسم عنوان الجهاز (deviceAddress) وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:287]

```
288:         return firstAnnounceSeen[deviceAddress] == true
```
> يُعيد (return) نتيجة مقارنة قيمة مفتاح عنوان الجهاز (deviceAddress) في خريطة رؤية أول إعلان (firstAnnounceSeen) بالقيمة true. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:288]

```
289:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:289]

```
290:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:290]

```
291:     /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:291]

```
292:      * Get debug information
```
> تعليق: «احصل على معلومات التصحيح». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:292]

```
293:      */
```
> تعليق: نهاية كتلة التوثيق (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:293]

```
294:     fun getDebugInfo(): String {
```
> يُعرّف دالة (fun) باسم الحصول على معلومات التصحيح (getDebugInfo) بلا وسائط وتُعيد نصاً (String). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:294]

```
295:         return buildString {
```
> يُعيد (return) نتيجة بنّاء النص (buildString) ضمن كتلة لاحقة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:295]

```
296:             appendLine("Connected Devices: ${connectedDevices.size} / ${powerManager.getMaxConnections()}")
```
> يُلحق سطراً (appendLine) بنصّ «Connected Devices:» متبوعاً بحجم خريطة الأجهزة المتصلة (connectedDevices.size) ثم « / » ثم نتيجة استدعاء أقصى عدد اتصالات (powerManager.getMaxConnections()). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:296]

```
297:             connectedDevices.forEach { (address, deviceConn) ->
```
> يمرّ على مدخلات خريطة الأجهزة المتصلة (connectedDevices) عبر forEach مفكّكاً كل مدخل إلى العنوان (address) واتصال الجهاز (deviceConn). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:297]

```
298:                 val age = (System.currentTimeMillis() - deviceConn.connectedAt) / 1000
```
> يُعرّف ثابتاً باسم العمر (age) قيمته الوقت الحالي بالملّي ثانية (System.currentTimeMillis) ناقص وقت اتصال الجهاز (deviceConn.connectedAt) مقسوماً على 1000. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:298]

```
299:                 appendLine("  - $address (we're ${if (deviceConn.isClient) "client" else "server"}, ${age}s, RSSI: ${deviceConn.rssi})")
```
> يُلحق سطراً (appendLine) بنصّ يبدأ بـ«  - » ثم العنوان (address) ثم «(we're » ثم نتيجة شرط: إن كان deviceConn.isClient فالنص «client» وإلا «server»، ثم العمر (age) متبوعاً بـ«s» ثم «RSSI: » وقيمة قوة الإشارة (deviceConn.rssi). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:299]

```
300:             }
```
> إغلاق نطاق (إغلاق كتلة forEach). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:300]

```
301:             appendLine()
```
> يُلحق سطراً فارغاً (appendLine بلا وسائط). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:301]

```
302:             appendLine("Subscribed Devices (server mode): ${subscribedDevices.size}")
```
> يُلحق سطراً (appendLine) بنصّ «Subscribed Devices (server mode):» متبوعاً بحجم الأجهزة المشتركة (subscribedDevices.size). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:302]

```
303:             appendLine()
```
> يُلحق سطراً فارغاً (appendLine بلا وسائط). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:303]

```
304:             appendLine("Pending Connections: ${pendingConnections.size}")
```
> يُلحق سطراً (appendLine) بنصّ «Pending Connections:» متبوعاً بحجم الاتصالات المعلّقة (pendingConnections.size). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:304]

```
305:             val now = System.currentTimeMillis()
```
> يُعرّف ثابتاً باسم الآن (now) قيمته الوقت الحالي بالملّي ثانية (System.currentTimeMillis). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:305]

```
306:             pendingConnections.forEach { (address, attempt) ->
```
> يمرّ على مدخلات الاتصالات المعلّقة (pendingConnections) عبر forEach مفكّكاً كل مدخل إلى العنوان (address) والمحاولة (attempt). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:306]

```
307:                 val elapsed = (now - attempt.lastAttempt) / 1000
```
> يُعرّف ثابتاً باسم المنقضي (elapsed) قيمته الآن (now) ناقص آخر محاولة (attempt.lastAttempt) مقسوماً على 1000. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:307]

```
308:                 appendLine("  - $address: ${attempt.attempts} attempts, last ${elapsed}s ago")
```
> يُلحق سطراً (appendLine) بنصّ يبدأ بـ«  - » ثم العنوان (address) ثم «: » ثم عدد المحاولات (attempt.attempts) متبوعاً بـ«attempts, last » ثم المنقضي (elapsed) متبوعاً بـ«s ago». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:308]

```
309:             }
```
> إغلاق نطاق (إغلاق كتلة forEach). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:309]

```
310:             appendLine()
```
> يُلحق سطراً فارغاً (appendLine بلا وسائط). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:310]

```
311:             appendLine("Scan RSSI Cache: ${scanRSSI.size}")
```
> يُلحق سطراً (appendLine) بنصّ «Scan RSSI Cache:» متبوعاً بحجم خريطة قوة إشارة المسح (scanRSSI.size). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:311]

```
312:             scanRSSI.forEach { (address, rssi) ->
```
> يمرّ على مدخلات خريطة قوة إشارة المسح (scanRSSI) عبر forEach مفكّكاً كل مدخل إلى العنوان (address) وقوة الإشارة (rssi). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:312]

```
313:                 appendLine("  - $address: $rssi dBm")
```
> يُلحق سطراً (appendLine) بنصّ يبدأ بـ«  - » ثم العنوان (address) ثم «: » ثم قوة الإشارة (rssi) متبوعاً بـ«dBm». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:313]

```
314:             }
```
> إغلاق نطاق (إغلاق كتلة forEach). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:314]

```
315:         }
```
> إغلاق نطاق (إغلاق كتلة buildString). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:315]

```
316:     }
```
> إغلاق نطاق (إغلاق دالة getDebugInfo). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:316]

```
317: } 
```
> إغلاق نطاق (إغلاق الصنف/النطاق الأعلى). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionTracker.kt:317]
