# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt (الأسطر 201–400)

```
201:         rssiMonitoringJob = connectionScope.launch {
```
> يُسنَد إلى المتغيّر «مهمة مراقبة قوة الإشارة» (rssiMonitoringJob) ناتجُ إطلاق مهمّة (launch) داخل نطاق الاتصال (connectionScope). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:201]

```
202:             while (isActive) {
```
> حلقة «طالما» (while) تستمر ما دامت «نشِط» (isActive) صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:202]

```
203:                 try {
```
> بداية كتلة «حاوِل» (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:203]

```
204:                     // Request RSSI from all client connections
```
> تعليق: اطلب قوة الإشارة من كل اتصالات العميل. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:204]

```
205:                     val connectedDevices = connectionTracker.getConnectedDevices()
```
> يُسنَد إلى الثابت «الأجهزة المتّصلة» (connectedDevices) ناتجُ استدعاء getConnectedDevices على «متتبّع الاتصال» (connectionTracker). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:205]

```
206:                     connectedDevices.values.filter { it.isClient && it.gatt != null }.forEach { deviceConn ->
```
> على قِيَم «الأجهزة المتّصلة» يُطبَّق ترشيح (filter) يُبقي ما هو عميل (isClient) وله كائن gatt غير فارغ، ثم تكرار (forEach) لكل اتصال جهاز باسم deviceConn. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:206]

```
207:                         try {
```
> بداية كتلة «حاوِل» (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:207]

```
208:                             Log.d(TAG, "Requesting RSSI from ${deviceConn.device.address}")
```
> يُستدعى Log.d بالوسم TAG ونص «طلب قوة الإشارة من» متبوعاً بعنوان جهاز deviceConn. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:208]

```
209:                             deviceConn.gatt?.readRemoteRssi()
```
> يُستدعى readRemoteRssi على كائن gatt الخاص بـ deviceConn إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:209]

```
210:                         } catch (e: Exception) {
```
> إغلاق كتلة «حاوِل» وبداية «أمسِك» (catch) باستثناء e من نوع Exception. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:210]

```
211:                             Log.w(TAG, "Failed to request RSSI from ${deviceConn.device.address}: ${e.message}")
```
> يُستدعى Log.w بالوسم TAG ونص «فشل طلب قوة الإشارة من» متبوعاً بعنوان جهاز deviceConn ورسالة الاستثناء e. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:211]

```
212:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:212]

```
213:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:213]

```
214:                     delay(AppConstants.Mesh.RSSI_UPDATE_INTERVAL_MS)
```
> يُستدعى تأخير (delay) بقيمة الثابت RSSI_UPDATE_INTERVAL_MS من AppConstants.Mesh. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:214]

```
215:                 } catch (e: Exception) {
```
> إغلاق كتلة «حاوِل» وبداية «أمسِك» (catch) باستثناء e من نوع Exception. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:215]

```
216:                     Log.w(TAG, "Error in RSSI monitoring: ${e.message}")
```
> يُستدعى Log.w بالوسم TAG ونص «خطأ في مراقبة قوة الإشارة» متبوعاً برسالة الاستثناء e. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:216]

```
217:                     delay(AppConstants.Mesh.RSSI_UPDATE_INTERVAL_MS)
```
> يُستدعى تأخير (delay) بقيمة الثابت RSSI_UPDATE_INTERVAL_MS من AppConstants.Mesh. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:217]

```
218:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:218]

```
219:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:219]

```
220:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:220]

```
221:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:221]

```
222:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:222]

```
223:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:223]

```
224:      * Stop RSSI monitoring
```
> تعليق: أوقف مراقبة قوة الإشارة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:224]

```
225:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:225]

```
226:     private fun stopRSSIMonitoring() {
```
> تعريف دالّة خاصّة (private) باسم «أوقف مراقبة قوة الإشارة» (stopRSSIMonitoring) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:226]

```
227:         rssiMonitoringJob?.cancel()
```
> يُستدعى إلغاء (cancel) على «مهمة مراقبة قوة الإشارة» إن لم تكن فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:227]

```
228:         rssiMonitoringJob = null
```
> يُسنَد إلى «مهمة مراقبة قوة الإشارة» القيمة فارغ (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:228]

```
229:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:229]

```
230:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:230]

```
231:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:231]

```
232:      * Start scanning with rate limiting
```
> تعليق: ابدأ المسح مع تحديد المعدّل. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:232]

```
233:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:233]

```
234:     @Suppress("DEPRECATION")
```
> تعليق توضيحي (annotation) باسم Suppress بالقيمة "DEPRECATION" لكتم تحذير الإهمال. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:234]

```
235:     private fun startScanning() {
```
> تعريف دالّة خاصّة (private) باسم «ابدأ المسح» (startScanning) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:235]

```
236:         // Respect debug setting
```
> تعليق: احترِم إعداد التنقيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:236]

```
237:         val enabled = isClientRoleEnabled()
```
> يُسنَد إلى الثابت «مُفعّل» (enabled) ناتجُ استدعاء «هل دور العميل مُفعّل» (isClientRoleEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:237]

```
238:         if (!permissionManager.hasBluetoothPermissions() || bleScanner == null || !isActive || !enabled) return
```
> شرط: إذا لم يملك «مدير الأذونات» (permissionManager) أذونات البلوتوث أو كان «ماسح BLE» (bleScanner) فارغاً أو لم يكن نشطاً أو لم يكن «مُفعّل» صحيحاً فاخرج (return). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:238]

```
239:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:239]

```
240:         // Rate limit scan starts to prevent "scanning too frequently" errors
```
> تعليق: حدِّد معدّل بدايات المسح لمنع أخطاء «المسح متكرر جداً». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:240]

```
241:         val currentTime = System.currentTimeMillis()
```
> يُسنَد إلى الثابت «الوقت الحالي» (currentTime) ناتجُ System.currentTimeMillis. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:241]

```
242:         if (isCurrentlyScanning) {
```
> شرط: إذا كان «يجري المسح حالياً» (isCurrentlyScanning) صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:242]

```
243:             Log.d(TAG, "Scan already in progress, skipping start request")
```
> يُستدعى Log.d بالوسم TAG ونص «المسح جارٍ بالفعل، تخطّي طلب البدء». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:243]

```
244:             return
```
> اخرج من الدالّة (return). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:244]

```
245:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:245]

```
246:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:246]

```
247:         val timeSinceLastStart = currentTime - lastScanStartTime
```
> يُسنَد إلى الثابت «الوقت منذ آخر بدء» (timeSinceLastStart) فرقُ «الوقت الحالي» ناقص «وقت آخر بدء مسح» (lastScanStartTime). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:247]

```
248:         if (timeSinceLastStart < scanRateLimit) {
```
> شرط: إذا كان «الوقت منذ آخر بدء» أصغر من «حدّ معدّل المسح» (scanRateLimit). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:248]

```
249:             val remainingWait = scanRateLimit - timeSinceLastStart
```
> يُسنَد إلى الثابت «الانتظار المتبقّي» (remainingWait) فرقُ «حدّ معدّل المسح» ناقص «الوقت منذ آخر بدء». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:249]

```
250:             Log.w(TAG, "Scan rate limited: need to wait ${remainingWait}ms before starting scan")
```
> يُستدعى Log.w بالوسم TAG ونص «المسح محدود المعدّل: يجب الانتظار» متبوعاً بـ «الانتظار المتبقّي» بالميلي ثانية قبل بدء المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:250]

```
251:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:251]

```
252:             // Schedule delayed scan start
```
> تعليق: جدوِل بدء مسح مؤجّل. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:252]

```
253:             connectionScope.launch {
```
> يُطلَق (launch) عملٌ داخل «نطاق الاتصال» (connectionScope). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:253]

```
254:                 delay(remainingWait)
```
> يُستدعى تأخير (delay) بقيمة «الانتظار المتبقّي». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:254]

```
255:                 if (isActive && !isCurrentlyScanning && isClientRoleEnabled()) {
```
> شرط: إذا كان نشطاً ولم يكن «يجري المسح حالياً» وكان «دور العميل مُفعّلاً». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:255]

```
256:                     startScanning()
```
> يُستدعى «ابدأ المسح» (startScanning). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:256]

```
257:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:257]

```
258:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:258]

```
259:             return
```
> اخرج من الدالّة (return). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:259]

```
260:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:260]

```
261:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:261]

```
262:         val scanFilter = ScanFilter.Builder()
```
> يُسنَد إلى الثابت «مرشِّح المسح» (scanFilter) كائنُ بانٍ (Builder) لـ ScanFilter. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:262]

```
263:             .setServiceUuid(ParcelUuid(AppConstants.Mesh.Gatt.SERVICE_UUID))
```
> يُستدعى setServiceUuid بمعرّف خدمة ParcelUuid مبنيٍّ من الثابت SERVICE_UUID في AppConstants.Mesh.Gatt. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:263]

```
264:             .build()
```
> يُستدعى build لبناء «مرشِّح المسح». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:264]

```
265:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:265]

```
266:         val scanFilters = listOf(scanFilter) 
```
> يُسنَد إلى الثابت «مرشِّحات المسح» (scanFilters) قائمةٌ (listOf) تحوي «مرشِّح المسح». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:266]

```
267:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:267]

```
268:         Log.d(TAG, "Starting BLE scan with target service UUID: ${AppConstants.Mesh.Gatt.SERVICE_UUID}")
```
> يُستدعى Log.d بالوسم TAG ونص «بدء مسح BLE بمعرّف الخدمة الهدف» متبوعاً بقيمة SERVICE_UUID. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:268]

```
269:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:269]

```
270:         scanCallback = object : ScanCallback() {
```
> يُسنَد إلى «استدعاء المسح» (scanCallback) كائنٌ مجهولٌ يرث ScanCallback. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:270]

```
271:             override fun onScanResult(callbackType: Int, result: ScanResult) {
```
> تجاوز (override) للدالّة onScanResult بوسيطين: callbackType من نوع Int وresult من نوع ScanResult. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:271]

```
272:                 // Log.d(TAG, "Scan result received: ${result.device.address}")
```
> تعليق: سطر مُعلَّق يستدعي Log.d بنص «نتيجة مسح مستلمة» متبوعاً بعنوان جهاز النتيجة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:272]

```
273:                 handleScanResult(result)
```
> يُستدعى «عالِج نتيجة المسح» (handleScanResult) بالوسيط result. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:273]

```
274:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:274]

```
275:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:275]

```
276:             override fun onBatchScanResults(results: MutableList<ScanResult>) {
```
> تجاوز (override) للدالّة onBatchScanResults بوسيط results من نوع قائمة قابلة للتغيير من ScanResult. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:276]

```
277:                 Log.d(TAG, "Batch scan results received: ${results.size} devices")
```
> يُستدعى Log.d بالوسم TAG ونص «نتائج مسح دُفعيّة مستلمة» متبوعاً بحجم results وكلمة devices. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:277]

```
278:                 results.forEach { result ->
```
> تكرار (forEach) على results لكل عنصر باسم result. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:278]

```
279:                     handleScanResult(result)
```
> يُستدعى «عالِج نتيجة المسح» (handleScanResult) بالوسيط result. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:279]

```
280:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:280]

```
281:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:281]

```
282:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:282]

```
283:             override fun onScanFailed(errorCode: Int) {
```
> تجاوز (override) للدالّة onScanFailed بوسيط errorCode من نوع Int. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:283]

```
284:                 Log.e(TAG, "Scan failed: $errorCode")
```
> يُستدعى Log.e بالوسم TAG ونص «فشل المسح» متبوعاً بـ errorCode. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:284]

```
285:                 isCurrentlyScanning = false
```
> يُسنَد إلى «يجري المسح حالياً» القيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:285]

```
286:                 lastScanStopTime = System.currentTimeMillis()
```
> يُسنَد إلى «وقت آخر إيقاف مسح» (lastScanStopTime) ناتجُ System.currentTimeMillis. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:286]

```
287:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:287]

```
288:                 when (errorCode) {
```
> تفريع «حين» (when) على قيمة errorCode. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:288]

```
289:                     1 -> {
```
> الحالة 1 تؤدّي إلى كتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:289]

```
290:                         // Already started: the stack thinks a scan is running. Re-arm from a clean
```
> تعليق: بدأ بالفعل: الكومة (stack) تظنّ أن مسحاً يعمل. أعِد التسليح من حالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:290]

```
291:                         // state so we don't stay wedged (stop then restart with backoff).
```
> تعليق: نظيفة كي لا نبقى عالقين (أوقِف ثم أعِد البدء مع تراجع زمني). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:291]

```
292:                         Log.e(TAG, "SCAN_FAILED_ALREADY_STARTED")
```
> يُستدعى Log.e بالوسم TAG ونص "SCAN_FAILED_ALREADY_STARTED". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:292]

```
293:                         stopScanning()
```
> يُستدعى «أوقف المسح» (stopScanning). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:293]

```
294:                         scheduleScanRestart("already-started", SCAN_RETRY_BASE_MS)
```
> يُستدعى «جدوِل إعادة بدء المسح» (scheduleScanRestart) بالسبب "already-started" وبالقيمة SCAN_RETRY_BASE_MS. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:294]

```
295:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:295]

```
296:                     2 -> {
```
> الحالة 2 تؤدّي إلى كتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:296]

```
297:                         // App registration failed: common transient stack fault. Previously had NO
```
> تعليق: فشل تسجيل التطبيق: عطل كومة عابر شائع. سابقاً لم يكن هناك. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:297]

```
298:                         // retry, which left discovery dead until a manual BLE toggle.
```
> تعليق: إعادة محاولة، مما ترك الاكتشاف ميّتاً حتى تبديل BLE يدوي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:298]

```
299:                         Log.e(TAG, "SCAN_FAILED_APPLICATION_REGISTRATION_FAILED")
```
> يُستدعى Log.e بالوسم TAG ونص "SCAN_FAILED_APPLICATION_REGISTRATION_FAILED". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:299]

```
300:                         scheduleScanRestart("registration-failed", SCAN_RETRY_BASE_MS)
```
> يُستدعى «جدوِل إعادة بدء المسح» بالسبب "registration-failed" وبالقيمة SCAN_RETRY_BASE_MS. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:300]

```
301:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:301]

```
302:                     3 -> {
```
> الحالة 3 تؤدّي إلى كتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:302]

```
303:                         Log.e(TAG, "SCAN_FAILED_INTERNAL_ERROR")
```
> يُستدعى Log.e بالوسم TAG ونص "SCAN_FAILED_INTERNAL_ERROR". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:303]

```
304:                         scheduleScanRestart("internal-error", SCAN_RETRY_BASE_MS)
```
> يُستدعى «جدوِل إعادة بدء المسح» بالسبب "internal-error" وبالقيمة SCAN_RETRY_BASE_MS. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:304]

```
305:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:305]

```
306:                     4 -> Log.e(TAG, "SCAN_FAILED_FEATURE_UNSUPPORTED") // permanent: don't retry
```
> الحالة 4 تستدعي Log.e بالوسم TAG ونص "SCAN_FAILED_FEATURE_UNSUPPORTED"؛ تعليق: دائم: لا تُعِد المحاولة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:306]

```
307:                     5 -> {
```
> الحالة 5 تؤدّي إلى كتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:307]

```
308:                         // Out of hardware resources: back off longer so other scanners/connections
```
> تعليق: نفاد موارد العتاد: تراجَع أطول كي تستطيع ماسحات/اتصالات أخرى. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:308]

```
309:                         // can free up before we try again.
```
> تعليق: أن تتحرّر قبل أن نحاول مجدداً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:309]

```
310:                         Log.e(TAG, "SCAN_FAILED_OUT_OF_HARDWARE_RESOURCES")
```
> يُستدعى Log.e بالوسم TAG ونص "SCAN_FAILED_OUT_OF_HARDWARE_RESOURCES". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:310]

```
311:                         scheduleScanRestart("out-of-resources", SCAN_RETRY_BASE_MS * 3)
```
> يُستدعى «جدوِل إعادة بدء المسح» بالسبب "out-of-resources" وبالقيمة SCAN_RETRY_BASE_MS مضروبة في ٣. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:311]

```
312:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:312]

```
313:                     6 -> {
```
> الحالة 6 تؤدّي إلى كتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:313]

```
314:                         Log.e(TAG, "SCAN_FAILED_SCANNING_TOO_FREQUENTLY")
```
> يُستدعى Log.e بالوسم TAG ونص "SCAN_FAILED_SCANNING_TOO_FREQUENTLY". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:314]

```
315:                         Log.w(TAG, "Scan failed due to rate limiting - will retry after delay")
```
> يُستدعى Log.w بالوسم TAG ونص «فشل المسح بسبب تحديد المعدّل - ستُعاد المحاولة بعد تأخير». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:315]

```
316:                         scheduleScanRestart("too-frequently", 10_000L)
```
> يُستدعى «جدوِل إعادة بدء المسح» بالسبب "too-frequently" وبالقيمة 10000 من نوع Long. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:316]

```
317:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:317]

```
318:                     else -> {
```
> الحالة الافتراضية (else) تؤدّي إلى كتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:318]

```
319:                         Log.e(TAG, "Unknown scan failure code: $errorCode")
```
> يُستدعى Log.e بالوسم TAG ونص «رمز فشل مسح غير معروف» متبوعاً بـ errorCode. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:319]

```
320:                         scheduleScanRestart("unknown-$errorCode", SCAN_RETRY_BASE_MS)
```
> يُستدعى «جدوِل إعادة بدء المسح» بالسبب "unknown-" متبوعاً بـ errorCode وبالقيمة SCAN_RETRY_BASE_MS. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:320]

```
321:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:321]

```
322:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:322]

```
323:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:323]

```
324:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:324]

```
325:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:325]

```
326:         try {
```
> بداية كتلة «حاوِل» (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:326]

```
327:             lastScanStartTime = currentTime
```
> يُسنَد إلى «وقت آخر بدء مسح» (lastScanStartTime) قيمةُ «الوقت الحالي». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:327]

```
328:             isCurrentlyScanning = true
```
> يُسنَد إلى «يجري المسح حالياً» القيمة صحيح (true). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:328]

```
329:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:329]

```
330:             bleScanner.startScan(scanFilters, powerManager.getScanSettings(), scanCallback)
```
> يُستدعى startScan على «ماسح BLE» بالوسائط «مرشِّحات المسح» وإعدادات المسح من «مدير الطاقة» (powerManager) و«استدعاء المسح». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:330]

```
331:             Log.d(TAG, "BLE scan started successfully")
```
> يُستدعى Log.d بالوسم TAG ونص «بدأ مسح BLE بنجاح». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:331]

```
332:         } catch (e: Exception) {
```
> إغلاق كتلة «حاوِل» وبداية «أمسِك» (catch) باستثناء e من نوع Exception. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:332]

```
333:             Log.e(TAG, "Exception starting scan: ${e.message}")
```
> يُستدعى Log.e بالوسم TAG ونص «استثناء عند بدء المسح» متبوعاً برسالة الاستثناء e. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:333]

```
334:             isCurrentlyScanning = false
```
> يُسنَد إلى «يجري المسح حالياً» القيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:334]

```
335:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:335]

```
336:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:336]

```
337:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:337]

```
338:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:338]

```
339:      * Stop scanning
```
> تعليق: أوقف المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:339]

```
340:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:340]

```
341:     @Suppress("DEPRECATION")
```
> تعليق توضيحي (annotation) باسم Suppress بالقيمة "DEPRECATION" لكتم تحذير الإهمال. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:341]

```
342:     private fun stopScanning() {
```
> تعريف دالّة خاصّة (private) باسم «أوقف المسح» (stopScanning) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:342]

```
343:         if (!permissionManager.hasBluetoothPermissions() || bleScanner == null) return
```
> شرط: إذا لم يملك «مدير الأذونات» أذونات البلوتوث أو كان «ماسح BLE» فارغاً فاخرج (return). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:343]

```
344:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:344]

```
345:         if (isCurrentlyScanning) {
```
> شرط: إذا كان «يجري المسح حالياً» صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:345]

```
346:             try {
```
> بداية كتلة «حاوِل» (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:346]

```
347:                 scanCallback?.let { 
```
> إذا لم يكن «استدعاء المسح» فارغاً فطبّق عليه كتلة let. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:347]

```
348:                     bleScanner.stopScan(it)
```
> يُستدعى stopScan على «ماسح BLE» بالوسيط it أي «استدعاء المسح». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:348]

```
349:                     Log.d(TAG, "BLE scan stopped successfully")
```
> يُستدعى Log.d بالوسم TAG ونص «توقّف مسح BLE بنجاح». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:349]

```
350:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:350]

```
351:             } catch (e: Exception) {
```
> إغلاق كتلة «حاوِل» وبداية «أمسِك» (catch) باستثناء e من نوع Exception. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:351]

```
352:                 Log.w(TAG, "Error stopping scan: ${e.message}")
```
> يُستدعى Log.w بالوسم TAG ونص «خطأ عند إيقاف المسح» متبوعاً برسالة الاستثناء e. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:352]

```
353:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:353]

```
354:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:354]

```
355:             isCurrentlyScanning = false
```
> يُسنَد إلى «يجري المسح حالياً» القيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:355]

```
356:             lastScanStopTime = System.currentTimeMillis()
```
> يُسنَد إلى «وقت آخر إيقاف مسح» (lastScanStopTime) ناتجُ System.currentTimeMillis. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:356]

```
357:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:357]

```
358:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:358]

```
359:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:359]

```
360:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:360]

```
361:      * Schedule a scan restart with incremental backoff. Used to recover from transient scan
```
> تعليق: جدوِل إعادة بدء مسح مع تراجع زمني تدريجي. يُستخدم للتعافي من فشل مسح عابر. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:361]

```
362:      * failures that previously had no retry path (codes 2/3/5), leaving discovery dead until a
```
> تعليق: لم يكن له مسار إعادة محاولة سابقاً (الرموز 2/3/5)، مما ترك الاكتشاف ميّتاً حتى. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:362]

```
363:      * manual BLE toggle.
```
> تعليق: تبديل BLE يدوي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:363]

```
364:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:364]

```
365:     private fun scheduleScanRestart(reason: String, baseDelayMs: Long) {
```
> تعريف دالّة خاصّة (private) باسم «جدوِل إعادة بدء المسح» (scheduleScanRestart) بوسيطين: reason من نوع String وbaseDelayMs من نوع Long. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:365]

```
366:         scanRetryCount++
```
> يُزاد «عدّاد إعادة محاولة المسح» (scanRetryCount) بمقدار واحد. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:366]

```
367:         val delayMs = (baseDelayMs * scanRetryCount).coerceAtMost(SCAN_MAX_RETRY_DELAY_MS)
```
> يُسنَد إلى الثابت «التأخير بالميلي ثانية» (delayMs) حاصلُ ضرب baseDelayMs في «عدّاد إعادة المحاولة» محصوراً ألا يتجاوز SCAN_MAX_RETRY_DELAY_MS. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:367]

```
368:         Log.w(TAG, "Scheduling scan restart in ${delayMs}ms (attempt $scanRetryCount, reason=$reason)")
```
> يُستدعى Log.w بالوسم TAG ونص «جدولة إعادة بدء المسح خلال» متبوعاً بـ delayMs بالميلي ثانية و«عدّاد المحاولة» والسبب reason. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:368]

```
369:         connectionScope.launch {
```
> يُطلَق (launch) عملٌ داخل «نطاق الاتصال» (connectionScope). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:369]

```
370:             delay(delayMs)
```
> يُستدعى تأخير (delay) بقيمة «التأخير بالميلي ثانية». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:370]

```
371:             if (isActive && scanningDesired && isClientRoleEnabled() && !isCurrentlyScanning) {
```
> شرط: إذا كان نشطاً و«المسح مرغوب» (scanningDesired) و«دور العميل مُفعّل» ولم يكن «يجري المسح حالياً». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:371]

```
372:                 startScanning()
```
> يُستدعى «ابدأ المسح» (startScanning). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:372]

```
373:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:373]

```
374:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:374]

```
375:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:375]

```
376:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:376]

```
377:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:377]

```
378:      * Periodic watchdog that self-heals the scanner. Android can stop a scan without ever invoking
```
> تعليق: مُراقِب دوري يُصلِح الماسح ذاتياً. أندرويد قد يوقف مسحاً دون استدعاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:378]

```
379:      * onScanFailed (internal stack reset, Doze, background throttling), which leaves the app
```
> تعليق: onScanFailed (إعادة ضبط كومة داخلية، وضع السكون Doze، خنق الخلفية)، مما يترك التطبيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:379]

```
380:      * believing it is scanning while it is not. This re-arms the scanner in those cases.
```
> تعليق: يظنّ أنه يمسح بينما هو ليس كذلك. هذا يعيد تسليح الماسح في تلك الحالات. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:380]

```
381:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:381]

```
382:     private fun startScanWatchdog() {
```
> تعريف دالّة خاصّة (private) باسم «ابدأ مراقِب المسح» (startScanWatchdog) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:382]

```
383:         scanWatchdogJob?.cancel()
```
> يُستدعى إلغاء (cancel) على «مهمة مراقِب المسح» (scanWatchdogJob) إن لم تكن فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:383]

```
384:         scanWatchdogJob = connectionScope.launch {
```
> يُسنَد إلى «مهمة مراقِب المسح» ناتجُ إطلاق مهمّة (launch) داخل «نطاق الاتصال». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:384]

```
385:             while (isActive) {
```
> حلقة «طالما» (while) تستمر ما دامت «نشِط» (isActive) صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:385]

```
386:                 delay(SCAN_WATCHDOG_INTERVAL_MS)
```
> يُستدعى تأخير (delay) بقيمة الثابت SCAN_WATCHDOG_INTERVAL_MS. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:386]

```
387:                 try {
```
> بداية كتلة «حاوِل» (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:387]

```
388:                     // Only act when we are supposed to be scanning. Honors duty-cycle OFF windows
```
> تعليق: تصرّف فقط حين يُفترض أن نمسح. يحترم نوافذ إيقاف دورة العمل. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:388]

```
389:                     // and the client-disabled state via scanningDesired.
```
> تعليق: وحالة تعطيل العميل عبر scanningDesired. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:389]

```
390:                     if (!isActive || !scanningDesired || !isClientRoleEnabled()) continue
```
> شرط: إذا لم يكن نشطاً أو لم يكن «المسح مرغوب» أو لم يكن «دور العميل مُفعّل» فتابِع (continue) إلى الدورة التالية. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:390]

```
391:                     if (!permissionManager.hasBluetoothPermissions() || bluetoothAdapter?.isEnabled != true) continue
```
> شرط: إذا لم يملك «مدير الأذونات» أذونات البلوتوث أو لم يكن «مُحوّل البلوتوث» (bluetoothAdapter) مُفعّلاً بقيمة true فتابِع (continue). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:391]

```
392:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:392]

```
393:                     val now = System.currentTimeMillis()
```
> يُسنَد إلى الثابت «الآن» (now) ناتجُ System.currentTimeMillis. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:393]

```
394:                     if (!isCurrentlyScanning) {
```
> شرط: إذا لم يكن «يجري المسح حالياً» صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:394]

```
395:                         Log.w(TAG, "Watchdog: scan desired but not running -> restarting scan")
```
> يُستدعى Log.w بالوسم TAG ونص «المراقِب: المسح مرغوب لكنه لا يعمل -> إعادة بدء المسح». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:395]

```
396:                         startScanning()
```
> يُستدعى «ابدأ المسح» (startScanning). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:396]

```
397:                     } else if (lastScanResultTime > 0L &&
```
> وإلا إذا كان «وقت آخر نتيجة مسح» (lastScanResultTime) أكبر من صفر Long و... (الشرط يتبع). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:397]

```
398:                         now - lastScanResultTime > SCAN_STALE_RESULT_MS &&
```
> تتمّة الشرط: وفرقُ «الآن» ناقص «وقت آخر نتيجة مسح» أكبر من SCAN_STALE_RESULT_MS و... [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:398]

```
399:                         now - lastScanStartTime > SCAN_STALE_RESULT_MS) {
```
> تتمّة الشرط: وفرقُ «الآن» ناقص «وقت آخر بدء مسح» أكبر من SCAN_STALE_RESULT_MS، ثم بداية الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:399]

```
400:                         // We think we're scanning but haven't seen anything for a long time. The scan
```
> تعليق: نظنّ أننا نمسح لكننا لم نرَ شيئاً منذ وقت طويل. المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:400]
