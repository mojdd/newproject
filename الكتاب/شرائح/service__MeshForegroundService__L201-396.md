# شريحة — app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt (الأسطر 201–396)

```
201:                 while (isActive) {
```
> حلقة تكرار (while) تستمر طالما القيمة المنطقية «نشِط» (isActive) صحيحة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:201]

```
202:                     // Retry enabling mesh/foreground once permissions become available
```
> تعليق: إعادة محاولة تفعيل الشبكة/الواجهة الأمامية بمجرد أن تصبح الأذونات متاحة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:202]

```
203:                     ensureMeshStarted()
```
> استدعاء الدالة «تأكّد من بدء الشبكة» (ensureMeshStarted) بلا وسائط. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:203]

```
204:                     val eligible = MeshServicePreferences.isBackgroundEnabled(true) && hasAllRequiredPermissions()
```
> تعريف قيمة ثابتة باسم «مؤهَّل» (eligible) تساوي نتيجة الدالة «هل الخلفية مفعَّلة» (isBackgroundEnabled) من «تفضيلات خدمة الشبكة» (MeshServicePreferences) بوسيط افتراضي true، مقترنة بعامل «و» المنطقي مع نتيجة الدالة «يملك كل الأذونات المطلوبة» (hasAllRequiredPermissions). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:204]

```
205:                     if (eligible) {
```
> شرط (if): إذا كانت القيمة «مؤهَّل» (eligible) صحيحة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:205]

```
206:                         // Only update the notification; do not re-call startForeground()
```
> تعليق: حدّث الإشعار فقط؛ لا تُعِد استدعاء startForeground(). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:206]

```
207:                         updateNotification(force = false)
```
> استدعاء الدالة «تحديث الإشعار» (updateNotification) بالوسيط المسمّى «إجبار» (force) بقيمة false. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:207]

```
208:                     } else {
```
> فرع «وإلا» (else) للشرط السابق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:208]

```
209:                         // If disabled or perms missing, ensure we are not in foreground and clear notif
```
> تعليق: إذا كانت معطَّلة أو الأذونات ناقصة، تأكّد من أننا لسنا في الواجهة الأمامية وامسح الإشعار. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:209]

```
210:                         if (isInForeground) {
```
> شرط (if): إذا كانت القيمة المنطقية «في الواجهة الأمامية» (isInForeground) صحيحة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:210]

```
211:                             try { stopForeground(false) } catch (_: Exception) { }
```
> كتلة محاولة (try) تستدعي الدالة «إيقاف الواجهة الأمامية» (stopForeground) بالوسيط false، مع كتلة التقاط (catch) لاستثناء (Exception) مُهمَل بلا جسم. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:211]

```
212:                             isInForeground = false
```
> إسناد القيمة false إلى المتغيّر «في الواجهة الأمامية» (isInForeground). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:212]

```
213:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:213]

```
214:                         notificationManager.cancel(NOTIFICATION_ID)
```
> استدعاء الدالة «إلغاء» (cancel) على «مدير الإشعارات» (notificationManager) بالوسيط «معرّف الإشعار» (NOTIFICATION_ID). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:214]

```
215:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:215]

```
216:                     delay(5000)
```
> استدعاء الدالة «تأخير» (delay) بالوسيط 5000 (ميلي ثانية). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:216]

```
217:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:217]

```
218:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:218]

```
219:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:219]

```
220: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:220]

```
221:         return START_STICKY
```
> إعادة (return) القيمة الثابتة «بدء لاصق» (START_STICKY). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:221]

```
222:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:222]

```
223: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:223]

```
224:     private fun ensureMeshStarted() {
```
> تعريف دالة خاصّة (private fun) باسم «تأكّد من بدء الشبكة» (ensureMeshStarted) بلا وسائط ولا نوع إعادة مصرَّح. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:224]

```
225:         if (isShuttingDown) return
```
> شرط (if): إذا كانت القيمة المنطقية «جارٍ الإيقاف» (isShuttingDown) صحيحة فأعِد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:225]

```
226:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:226]

```
227:             com.bitchat.android.wifiaware.WifiAwareController.startIfPossible()
```
> استدعاء الدالة «ابدأ إن أمكن» (startIfPossible) على «متحكّم واي فاي أوير» (WifiAwareController) ضمن الحزمة com.bitchat.android.wifiaware. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:227]

```
228:         } catch (e: Exception) {
```
> كتلة التقاط (catch) لاستثناء (Exception) باسم المتغيّر e. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:228]

```
229:             android.util.Log.e("MeshForegroundService", "Failed to ensure Wi-Fi Aware transport: ${e.message}")
```
> استدعاء الدالة «خطأ» (Log.e) من android.util.Log بوسمٍ نصّي "MeshForegroundService" ورسالة نصّية "Failed to ensure Wi-Fi Aware transport: " متبوعة بقيمة «الرسالة» (e.message) للاستثناء. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:229]

```
230:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:230]

```
231: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:231]

```
232:         val bleEnabled = try {
```
> تعريف قيمة ثابتة باسم «بلوتوث منخفض الطاقة مفعَّل» (bleEnabled) تساوي نتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:232]

```
233:             com.bitchat.android.ui.debug.DebugPreferenceManager.getBleEnabled(true)
```
> استدعاء الدالة «احصل على تفعيل البلوتوث» (getBleEnabled) من «مدير تفضيلات التنقيح» (DebugPreferenceManager) ضمن الحزمة com.bitchat.android.ui.debug بالوسيط true. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:233]

```
234:         } catch (_: Exception) {
```
> كتلة التقاط (catch) لاستثناء (Exception) باسم مُهمَل. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:234]

```
235:             true
```
> القيمة true كنتيجة كتلة الالتقاط. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:235]

```
236:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:236]

```
237:         if (!bleEnabled) {
```
> شرط (if): إذا كانت القيمة «بلوتوث منخفض الطاقة مفعَّل» (bleEnabled) غير صحيحة (نفي). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:237]

```
238:             try { meshService?.setBleTransportEnabled(false) } catch (_: Exception) { }
```
> كتلة محاولة (try) تستدعي الدالة «اضبط تفعيل ناقل البلوتوث» (setBleTransportEnabled) بالوسيط false على «خدمة الشبكة» (meshService) باستدعاء آمن (?.)، مع كتلة التقاط استثناء مُهمَل بلا جسم. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:238]

```
239:             return
```
> إعادة (return) بلا قيمة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:239]

```
240:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:240]

```
241:         if (!hasBluetoothPermissions()) return
```
> شرط (if): إذا كانت نتيجة الدالة «يملك أذونات البلوتوث» (hasBluetoothPermissions) غير صحيحة (نفي) فأعِد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:241]

```
242:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:242]

```
243:             android.util.Log.d("MeshForegroundService", "Ensuring mesh service is started")
```
> استدعاء الدالة «تنقيح» (Log.d) من android.util.Log بوسمٍ نصّي "MeshForegroundService" ورسالة نصّية "Ensuring mesh service is started". [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:243]

```
244:             val service = MeshServiceHolder.getOrCreate(applicationContext)
```
> تعريف قيمة ثابتة باسم «خدمة» (service) تساوي نتيجة الدالة «احصل أو أنشئ» (getOrCreate) من «حامل خدمة الشبكة» (MeshServiceHolder) بالوسيط «سياق التطبيق» (applicationContext). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:244]

```
245:             service.startServices()
```
> استدعاء الدالة «ابدأ الخدمات» (startServices) على القيمة «خدمة» (service). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:245]

```
246:         } catch (e: Exception) {
```
> كتلة التقاط (catch) لاستثناء (Exception) باسم المتغيّر e. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:246]

```
247:             android.util.Log.e("MeshForegroundService", "Failed to start mesh service: ${e.message}")
```
> استدعاء الدالة «خطأ» (Log.e) من android.util.Log بوسمٍ نصّي "MeshForegroundService" ورسالة نصّية "Failed to start mesh service: " متبوعة بقيمة «الرسالة» (e.message) للاستثناء. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:247]

```
248:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:248]

```
249:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:249]

```
250: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:250]

```
251:     private fun updateNotification(force: Boolean) {
```
> تعريف دالة خاصّة (private fun) باسم «تحديث الإشعار» (updateNotification) بوسيط واحد «إجبار» (force) من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:251]

```
252:         if (isShuttingDown) {
```
> شرط (if): إذا كانت القيمة المنطقية «جارٍ الإيقاف» (isShuttingDown) صحيحة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:252]

```
253:             notificationManager.cancel(NOTIFICATION_ID)
```
> استدعاء الدالة «إلغاء» (cancel) على «مدير الإشعارات» (notificationManager) بالوسيط «معرّف الإشعار» (NOTIFICATION_ID). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:253]

```
254:             return
```
> إعادة (return) بلا قيمة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:254]

```
255:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:255]

```
256:         val count = getUnifiedActivePeerCount()
```
> تعريف قيمة ثابتة باسم «عدد» (count) تساوي نتيجة الدالة «احصل على عدد الأقران النشطين الموحَّد» (getUnifiedActivePeerCount). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:256]

```
257:         val notification = buildNotification(count)
```
> تعريف قيمة ثابتة باسم «إشعار» (notification) تساوي نتيجة الدالة «ابنِ الإشعار» (buildNotification) بالوسيط «عدد» (count). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:257]

```
258:         if (MeshServicePreferences.isBackgroundEnabled(true) && hasAllRequiredPermissions()) {
```
> شرط (if): إذا كانت نتيجة الدالة «هل الخلفية مفعَّلة» (isBackgroundEnabled) من «تفضيلات خدمة الشبكة» (MeshServicePreferences) بوسيط true، مقترنة بعامل «و» المنطقي مع نتيجة الدالة «يملك كل الأذونات المطلوبة» (hasAllRequiredPermissions). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:258]

```
259:             notificationManager.notify(NOTIFICATION_ID, notification)
```
> استدعاء الدالة «أبلِغ» (notify) على «مدير الإشعارات» (notificationManager) بالوسيطين «معرّف الإشعار» (NOTIFICATION_ID) و«إشعار» (notification). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:259]

```
260:         } else if (force) {
```
> فرع «وإلا إذا» (else if): إذا كانت القيمة «إجبار» (force) صحيحة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:260]

```
261:             // If disabled and forced, make sure to remove any prior foreground state
```
> تعليق: إذا كانت معطَّلة ومُجبَرة، تأكّد من إزالة أي حالة واجهة أمامية سابقة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:261]

```
262:             try { stopForeground(false) } catch (_: Exception) { }
```
> كتلة محاولة (try) تستدعي الدالة «إيقاف الواجهة الأمامية» (stopForeground) بالوسيط false، مع كتلة التقاط استثناء مُهمَل بلا جسم. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:262]

```
263:             notificationManager.cancel(NOTIFICATION_ID)
```
> استدعاء الدالة «إلغاء» (cancel) على «مدير الإشعارات» (notificationManager) بالوسيط «معرّف الإشعار» (NOTIFICATION_ID). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:263]

```
264:             isInForeground = false
```
> إسناد القيمة false إلى المتغيّر «في الواجهة الأمامية» (isInForeground). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:264]

```
265:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:265]

```
266:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:266]

```
267: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:267]

```
268:     private fun hasAllRequiredPermissions(): Boolean {
```
> تعريف دالة خاصّة (private fun) باسم «يملك كل الأذونات المطلوبة» (hasAllRequiredPermissions) بلا وسائط ونوع إعادة منطقي (Boolean). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:268]

```
269:         // For starting FGS with connectedDevice|dataSync, we need:
```
> تعليق: لبدء الخدمة الأمامية (FGS) بنوع connectedDevice|dataSync نحتاج إلى:. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:269]

```
270:         // - Foreground service permissions (declared in manifest)
```
> تعليق: - أذونات الخدمة الأمامية (مُصرَّحة في ملف البيان/manifest). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:270]

```
271:         // - One of the device-related permissions (we request BL perms at runtime)
```
> تعليق: - أحد الأذونات المتعلّقة بالجهاز (نطلب أذونات البلوتوث عند التشغيل). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:271]

```
272:         // - On Android 13+, POST_NOTIFICATIONS to actually show notification
```
> تعليق: - على أندرويد 13 فأعلى، إذن POST_NOTIFICATIONS لإظهار الإشعار فعلياً. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:272]

```
273:         return hasBluetoothPermissions() && hasNotificationPermission()
```
> إعادة (return) نتيجة الدالة «يملك أذونات البلوتوث» (hasBluetoothPermissions) مقترنة بعامل «و» المنطقي مع نتيجة الدالة «يملك إذن الإشعار» (hasNotificationPermission). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:273]

```
274:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:274]

```
275: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:275]

```
276:     private fun getUnifiedActivePeerCount(): Int {
```
> تعريف دالة خاصّة (private fun) باسم «احصل على عدد الأقران النشطين الموحَّد» (getUnifiedActivePeerCount) بلا وسائط ونوع إعادة عدد صحيح (Int). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:276]

```
277:         return try {
```
> إعادة (return) نتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:277]

```
278:             unifiedMeshService?.getActivePeerCount() ?: meshService?.getActivePeerCount() ?: 0
```
> استدعاء الدالة «احصل على عدد الأقران النشطين» (getActivePeerCount) على «خدمة الشبكة الموحَّدة» (unifiedMeshService) باستدعاء آمن (?.)، وإن كانت القيمة فارغة (null) فاستدعاؤها على «خدمة الشبكة» (meshService) باستدعاء آمن عبر معامل إلفيس (?:)، وإن كانت فارغة كذلك فالقيمة 0. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:278]

```
279:         } catch (_: Exception) {
```
> كتلة التقاط (catch) لاستثناء (Exception) باسم مُهمَل. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:279]

```
280:             0
```
> القيمة 0 كنتيجة كتلة الالتقاط. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:280]

```
281:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:281]

```
282:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:282]

```
283: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:283]

```
284:     private fun hasBluetoothPermissions(): Boolean {
```
> تعريف دالة خاصّة (private fun) باسم «يملك أذونات البلوتوث» (hasBluetoothPermissions) بلا وسائط ونوع إعادة منطقي (Boolean). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:284]

```
285:         return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
```
> إعادة (return) نتيجة شرط (if): إذا كان «رقم إصدار حزمة التطوير» (Build.VERSION.SDK_INT) أكبر من أو يساوي رمز الإصدار S (Build.VERSION_CODES.S). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:285]

```
286:             androidx.core.content.ContextCompat.checkSelfPermission(this, android.Manifest.permission.BLUETOOTH_ADVERTISE) == android.content.pm.PackageManager.PERMISSION_GRANTED &&
```
> استدعاء الدالة «افحص الإذن الذاتي» (checkSelfPermission) من ContextCompat بالوسيطين this وإذن BLUETOOTH_ADVERTISE، ومقارنته بالمساواة مع الثابت PERMISSION_GRANTED، مقترناً بعامل «و» المنطقي. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:286]

```
287:             androidx.core.content.ContextCompat.checkSelfPermission(this, android.Manifest.permission.BLUETOOTH_CONNECT) == android.content.pm.PackageManager.PERMISSION_GRANTED &&
```
> استدعاء الدالة «افحص الإذن الذاتي» (checkSelfPermission) من ContextCompat بالوسيطين this وإذن BLUETOOTH_CONNECT، ومقارنته بالمساواة مع الثابت PERMISSION_GRANTED، مقترناً بعامل «و» المنطقي. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:287]

```
288:             androidx.core.content.ContextCompat.checkSelfPermission(this, android.Manifest.permission.BLUETOOTH_SCAN) == android.content.pm.PackageManager.PERMISSION_GRANTED
```
> استدعاء الدالة «افحص الإذن الذاتي» (checkSelfPermission) من ContextCompat بالوسيطين this وإذن BLUETOOTH_SCAN، ومقارنته بالمساواة مع الثابت PERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:288]

```
289:         } else {
```
> فرع «وإلا» (else) للشرط. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:289]

```
290:             // Prior to S, scanning requires location permissions
```
> تعليق: قبل الإصدار S، يتطلّب المسح أذونات الموقع. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:290]

```
291:             val fine = androidx.core.content.ContextCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) == android.content.pm.PackageManager.PERMISSION_GRANTED
```
> تعريف قيمة ثابتة باسم «دقيق» (fine) تساوي نتيجة مقارنة استدعاء «افحص الإذن الذاتي» (checkSelfPermission) لإذن ACCESS_FINE_LOCATION بالمساواة مع الثابت PERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:291]

```
292:             val coarse = androidx.core.content.ContextCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) == android.content.pm.PackageManager.PERMISSION_GRANTED
```
> تعريف قيمة ثابتة باسم «خشن» (coarse) تساوي نتيجة مقارنة استدعاء «افحص الإذن الذاتي» (checkSelfPermission) لإذن ACCESS_COARSE_LOCATION بالمساواة مع الثابت PERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:292]

```
293:             fine || coarse
```
> القيمة «دقيق» (fine) مقترنة بعامل «أو» المنطقي مع القيمة «خشن» (coarse) كنتيجة الفرع. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:293]

```
294:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:294]

```
295:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:295]

```
296: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:296]

```
297:     private fun hasNotificationPermission(): Boolean {
```
> تعريف دالة خاصّة (private fun) باسم «يملك إذن الإشعار» (hasNotificationPermission) بلا وسائط ونوع إعادة منطقي (Boolean). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:297]

```
298:         return if (Build.VERSION.SDK_INT >= 33) {
```
> إعادة (return) نتيجة شرط (if): إذا كان «رقم إصدار حزمة التطوير» (Build.VERSION.SDK_INT) أكبر من أو يساوي 33. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:298]

```
299:             androidx.core.content.ContextCompat.checkSelfPermission(this, android.Manifest.permission.POST_NOTIFICATIONS) == android.content.pm.PackageManager.PERMISSION_GRANTED
```
> استدعاء الدالة «افحص الإذن الذاتي» (checkSelfPermission) من ContextCompat بالوسيطين this وإذن POST_NOTIFICATIONS، ومقارنته بالمساواة مع الثابت PERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:299]

```
300:         } else true
```
> فرع «وإلا» (else) يعيد القيمة true. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:300]

```
301:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:301]

```
302: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:302]

```
303:     private fun buildNotification(activePeers: Int): Notification {
```
> تعريف دالة خاصّة (private fun) باسم «ابنِ الإشعار» (buildNotification) بوسيط واحد «الأقران النشطون» (activePeers) من نوع عدد صحيح (Int) ونوع إعادة «إشعار» (Notification). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:303]

```
304:         val openIntent = Intent(this, MainActivity::class.java)
```
> تعريف قيمة ثابتة باسم «نيّة الفتح» (openIntent) تساوي كائن نيّة (Intent) جديداً بالوسيطين this وصنف «النشاط الرئيسي» (MainActivity::class.java). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:304]

```
305:         val pendingIntent = PendingIntent.getActivity(
```
> تعريف قيمة ثابتة باسم «نيّة معلَّقة» (pendingIntent) تساوي نتيجة الدالة «احصل على نشاط» (PendingIntent.getActivity) بوسائط تبدأ هنا. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:305]

```
306:             this, 0, openIntent,
```
> الوسائط: this، والرمز 0، و«نيّة الفتح» (openIntent). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:306]

```
307:             PendingIntent.FLAG_UPDATE_CURRENT or (if (Build.VERSION.SDK_INT >= 23) PendingIntent.FLAG_IMMUTABLE else 0)
```
> الوسيط الأخير: الراية FLAG_UPDATE_CURRENT مدموجة بعامل «أو» البتّي (or) مع تعبير شرطي يعيد الراية FLAG_IMMUTABLE إن كان SDK_INT أكبر من أو يساوي 23 وإلا 0. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:307]

```
308:         )
```
> إغلاق قائمة الوسائط. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:308]

```
309: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:309]

```
310:         // Action: Quit Bitchat
```
> تعليق: إجراء: إنهاء بِت‌تشات (Quit Bitchat). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:310]

```
311:         val quitIntent = Intent(this, MeshForegroundService::class.java).apply { action = ACTION_QUIT }
```
> تعريف قيمة ثابتة باسم «نيّة الإنهاء» (quitIntent) تساوي كائن نيّة (Intent) جديداً بالوسيطين this وصنف MeshForegroundService::class.java، ثم تطبيق (apply) يسند إلى الخاصية «الإجراء» (action) قيمة الثابت «إجراء الإنهاء» (ACTION_QUIT). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:311]

```
312:         val quitPendingIntent = PendingIntent.getService(
```
> تعريف قيمة ثابتة باسم «نيّة الإنهاء المعلَّقة» (quitPendingIntent) تساوي نتيجة الدالة «احصل على خدمة» (PendingIntent.getService) بوسائط تبدأ هنا. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:312]

```
313:             this, 1, quitIntent,
```
> الوسائط: this، والرمز 1، و«نيّة الإنهاء» (quitIntent). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:313]

```
314:             PendingIntent.FLAG_UPDATE_CURRENT or (if (Build.VERSION.SDK_INT >= 23) PendingIntent.FLAG_IMMUTABLE else 0)
```
> الوسيط الأخير: الراية FLAG_UPDATE_CURRENT مدموجة بعامل «أو» البتّي (or) مع تعبير شرطي يعيد الراية FLAG_IMMUTABLE إن كان SDK_INT أكبر من أو يساوي 23 وإلا 0. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:314]

```
315:         )
```
> إغلاق قائمة الوسائط. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:315]

```
316: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:316]

```
317:         val title = getString(R.string.app_name)
```
> تعريف قيمة ثابتة باسم «عنوان» (title) تساوي نتيجة الدالة «احصل على نص» (getString) للمورد R.string.app_name. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:317]

```
318:         val content = getString(R.string.mesh_service_notification_content, activePeers)
```
> تعريف قيمة ثابتة باسم «محتوى» (content) تساوي نتيجة الدالة «احصل على نص» (getString) للمورد R.string.mesh_service_notification_content بوسيط التنسيق «الأقران النشطون» (activePeers). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:318]

```
319: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:319]

```
320:         return NotificationCompat.Builder(this, CHANNEL_ID)
```
> إعادة (return) كائن «باني» (Builder) من NotificationCompat بالوسيطين this و«معرّف القناة» (CHANNEL_ID)، ويُتبَع بسلسلة استدعاءات. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:320]

```
321:             .setContentTitle(title)
```
> استدعاء الدالة «اضبط عنوان المحتوى» (setContentTitle) بالوسيط «عنوان» (title). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:321]

```
322:             .setContentText(content)
```
> استدعاء الدالة «اضبط نص المحتوى» (setContentText) بالوسيط «محتوى» (content). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:322]

```
323:             .setSmallIcon(R.mipmap.ic_launcher)
```
> استدعاء الدالة «اضبط الأيقونة الصغيرة» (setSmallIcon) بالوسيط المورد R.mipmap.ic_launcher. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:323]

```
324:             .setOngoing(true)
```
> استدعاء الدالة «اضبط مستمرّ» (setOngoing) بالوسيط true. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:324]

```
325:             .setOnlyAlertOnce(true)
```
> استدعاء الدالة «اضبط التنبيه مرّة واحدة فقط» (setOnlyAlertOnce) بالوسيط true. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:325]

```
326:             .setPriority(NotificationCompat.PRIORITY_LOW)
```
> استدعاء الدالة «اضبط الأولوية» (setPriority) بالثابت «أولوية منخفضة» (PRIORITY_LOW) من NotificationCompat. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:326]

```
327:             .setCategory(NotificationCompat.CATEGORY_SERVICE)
```
> استدعاء الدالة «اضبط الفئة» (setCategory) بالثابت «فئة الخدمة» (CATEGORY_SERVICE) من NotificationCompat. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:327]

```
328:             .setContentIntent(pendingIntent)
```
> استدعاء الدالة «اضبط نيّة المحتوى» (setContentIntent) بالوسيط «نيّة معلَّقة» (pendingIntent). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:328]

```
329:             // Add an action button that appears when notification is expanded
```
> تعليق: أضِف زرّ إجراء يظهر عند توسيع الإشعار. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:329]

```
330:             .addAction(
```
> استدعاء الدالة «أضِف إجراءً» (addAction) بوسائط تبدأ هنا. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:330]

```
331:                 android.R.drawable.ic_menu_close_clear_cancel,
```
> الوسيط الأول: المورد android.R.drawable.ic_menu_close_clear_cancel (أيقونة). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:331]

```
332:                 getString(R.string.notification_action_quit_bitchat),
```
> الوسيط الثاني: نتيجة الدالة «احصل على نص» (getString) للمورد R.string.notification_action_quit_bitchat. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:332]

```
333:                 quitPendingIntent
```
> الوسيط الثالث: «نيّة الإنهاء المعلَّقة» (quitPendingIntent). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:333]

```
334:             )
```
> إغلاق قائمة وسائط «أضِف إجراءً» (addAction). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:334]

```
335:             .build()
```
> استدعاء الدالة «ابنِ» (build) لإنتاج كائن الإشعار. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:335]

```
336:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:336]

```
337: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:337]

```
338:     private fun createChannel() {
```
> تعريف دالة خاصّة (private fun) باسم «أنشئ القناة» (createChannel) بلا وسائط ولا نوع إعادة مصرَّح. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:338]

```
339:         if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
```
> شرط (if): إذا كان «رقم إصدار حزمة التطوير» (Build.VERSION.SDK_INT) أكبر من أو يساوي رمز الإصدار O (Build.VERSION_CODES.O). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:339]

```
340:             val channel = NotificationChannel(
```
> تعريف قيمة ثابتة باسم «قناة» (channel) تساوي كائن «قناة إشعار» (NotificationChannel) جديداً بوسائط تبدأ هنا. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:340]

```
341:                 CHANNEL_ID,
```
> الوسيط الأول: «معرّف القناة» (CHANNEL_ID). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:341]

```
342:                 getString(R.string.mesh_service_channel_name),
```
> الوسيط الثاني: نتيجة الدالة «احصل على نص» (getString) للمورد R.string.mesh_service_channel_name. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:342]

```
343:                 NotificationManager.IMPORTANCE_LOW
```
> الوسيط الثالث: الثابت «أهمّية منخفضة» (IMPORTANCE_LOW) من NotificationManager. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:343]

```
344:             ).apply {
```
> إغلاق قائمة وسائط المُنشِئ وبدء كتلة تطبيق (apply). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:344]

```
345:                 description = getString(R.string.mesh_service_channel_desc)
```
> إسناد قيمة الدالة «احصل على نص» (getString) للمورد R.string.mesh_service_channel_desc إلى الخاصية «وصف» (description). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:345]

```
346:                 setShowBadge(false)
```
> استدعاء الدالة «اضبط إظهار الشارة» (setShowBadge) بالوسيط false. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:346]

```
347:             }
```
> إغلاق نطاق كتلة التطبيق (apply). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:347]

```
348:             (getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager)
```
> استدعاء الدالة «احصل على خدمة النظام» (getSystemService) بالثابت Context.NOTIFICATION_SERVICE مع تحويل النوع (as) إلى «مدير الإشعارات» (NotificationManager). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:348]

```
349:                 .createNotificationChannel(channel)
```
> استدعاء الدالة «أنشئ قناة إشعار» (createNotificationChannel) بالوسيط «قناة» (channel). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:349]

```
350:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:350]

```
351:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:351]

```
352: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:352]

```
353:     private fun hasLocationPermission(): Boolean {
```
> تعريف دالة خاصّة (private fun) باسم «يملك إذن الموقع» (hasLocationPermission) بلا وسائط ونوع إعادة منطقي (Boolean). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:353]

```
354:         val fine = androidx.core.content.ContextCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) == android.content.pm.PackageManager.PERMISSION_GRANTED
```
> تعريف قيمة ثابتة باسم «دقيق» (fine) تساوي نتيجة مقارنة استدعاء «افحص الإذن الذاتي» (checkSelfPermission) لإذن ACCESS_FINE_LOCATION بالمساواة مع الثابت PERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:354]

```
355:         val coarse = androidx.core.content.ContextCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) == android.content.pm.PackageManager.PERMISSION_GRANTED
```
> تعريف قيمة ثابتة باسم «خشن» (coarse) تساوي نتيجة مقارنة استدعاء «افحص الإذن الذاتي» (checkSelfPermission) لإذن ACCESS_COARSE_LOCATION بالمساواة مع الثابت PERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:355]

```
356:         return fine || coarse
```
> إعادة (return) القيمة «دقيق» (fine) مقترنة بعامل «أو» المنطقي مع القيمة «خشن» (coarse). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:356]

```
357:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:357]

```
358: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:358]

```
359:     private fun startForegroundCompat(notification: Notification) {
```
> تعريف دالة خاصّة (private fun) باسم «بدء الواجهة الأمامية المتوافق» (startForegroundCompat) بوسيط واحد «إشعار» (notification) من نوع «إشعار» (Notification). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:359]

```
360:         if (Build.VERSION.SDK_INT >= 34) {
```
> شرط (if): إذا كان «رقم إصدار حزمة التطوير» (Build.VERSION.SDK_INT) أكبر من أو يساوي 34. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:360]

```
361:             val type = if (hasLocationPermission()) {
```
> تعريف قيمة ثابتة باسم «نوع» (type) تساوي نتيجة شرط (if): إذا كانت نتيجة الدالة «يملك إذن الموقع» (hasLocationPermission) صحيحة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:361]

```
362:                 ServiceInfo.FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE or ServiceInfo.FOREGROUND_SERVICE_TYPE_LOCATION
```
> الثابت FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE مدموج بعامل «أو» البتّي (or) مع الثابت FOREGROUND_SERVICE_TYPE_LOCATION، كلاهما من ServiceInfo. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:362]

```
363:             } else {
```
> فرع «وإلا» (else) للشرط. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:363]

```
364:                 ServiceInfo.FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE
```
> الثابت FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE من ServiceInfo كنتيجة الفرع. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:364]

```
365:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:365]

```
366:             try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:366]

```
367:                 startForeground(NOTIFICATION_ID, notification, type)
```
> استدعاء الدالة «بدء الواجهة الأمامية» (startForeground) بالوسائط «معرّف الإشعار» (NOTIFICATION_ID) و«إشعار» (notification) و«نوع» (type). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:367]

```
368:             } catch (e: SecurityException) {
```
> كتلة التقاط (catch) لاستثناء أمني (SecurityException) باسم المتغيّر e. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:368]

```
369:                 // Fallback for cases where "While In Use" permission exists but background start is restricted
```
> تعليق: حلّ بديل للحالات التي يوجد فيها إذن "أثناء الاستخدام" لكن البدء في الخلفية مقيَّد. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:369]

```
370:                 if (type and ServiceInfo.FOREGROUND_SERVICE_TYPE_LOCATION != 0) {
```
> شرط (if): إذا كان ناتج عامل «و» البتّي (and) بين «نوع» (type) والثابت FOREGROUND_SERVICE_TYPE_LOCATION لا يساوي 0. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:370]

```
371:                      android.util.Log.w("MeshForegroundService", "Failed to start with LOCATION type, falling back to CONNECTED_DEVICE: ${e.message}")
```
> استدعاء الدالة «تحذير» (Log.w) من android.util.Log بوسمٍ نصّي "MeshForegroundService" ورسالة نصّية "Failed to start with LOCATION type, falling back to CONNECTED_DEVICE: " متبوعة بقيمة «الرسالة» (e.message) للاستثناء. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:371]

```
372:                      startForeground(NOTIFICATION_ID, notification, ServiceInfo.FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE)
```
> استدعاء الدالة «بدء الواجهة الأمامية» (startForeground) بالوسائط «معرّف الإشعار» (NOTIFICATION_ID) و«إشعار» (notification) والثابت FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE من ServiceInfo. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:372]

```
373:                 } else {
```
> فرع «وإلا» (else) للشرط. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:373]

```
374:                     throw e
```
> رمي (throw) الاستثناء e. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:374]

```
375:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:375]

```
376:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:376]

```
377:         } else {
```
> فرع «وإلا» (else) للشرط على رقم الإصدار. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:377]

```
378:             startForeground(NOTIFICATION_ID, notification)
```
> استدعاء الدالة «بدء الواجهة الأمامية» (startForeground) بالوسيطين «معرّف الإشعار» (NOTIFICATION_ID) و«إشعار» (notification). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:378]

```
379:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:379]

```
380:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:380]

```
381: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:381]

```
382:     override fun onDestroy() {
```
> تعريف دالة متجاوِزة (override fun) باسم «عند الإتلاف» (onDestroy) بلا وسائط. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:382]

```
383:         updateJob?.cancel()
```
> استدعاء الدالة «إلغاء» (cancel) على «مهمّة التحديث» (updateJob) باستدعاء آمن (?.). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:383]

```
384:         updateJob = null
```
> إسناد القيمة الفارغة (null) إلى المتغيّر «مهمّة التحديث» (updateJob). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:384]

```
385:         // Cancel the service coroutine scope to prevent leaks
```
> تعليق: ألغِ نطاق كوروتين الخدمة لمنع التسريبات. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:385]

```
386:         try { serviceJob.cancel() } catch (_: Exception) { }
```
> كتلة محاولة (try) تستدعي الدالة «إلغاء» (cancel) على «مهمّة الخدمة» (serviceJob)، مع كتلة التقاط استثناء مُهمَل بلا جسم. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:386]

```
387:         // Best-effort ensure we are not marked foreground
```
> تعليق: بأفضل جهد، تأكّد من أننا غير معلَّمين كواجهة أمامية. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:387]

```
388:         if (isInForeground) {
```
> شرط (if): إذا كانت القيمة المنطقية «في الواجهة الأمامية» (isInForeground) صحيحة. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:388]

```
389:             try { stopForeground(true) } catch (_: Exception) { }
```
> كتلة محاولة (try) تستدعي الدالة «إيقاف الواجهة الأمامية» (stopForeground) بالوسيط true، مع كتلة التقاط استثناء مُهمَل بلا جسم. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:389]

```
390:             isInForeground = false
```
> إسناد القيمة false إلى المتغيّر «في الواجهة الأمامية» (isInForeground). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:390]

```
391:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:391]

```
392:         super.onDestroy()
```
> استدعاء الدالة «عند الإتلاف» (onDestroy) من الصنف الأب (super). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:392]

```
393:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:393]

```
394: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:394]

```
395:     override fun onBind(intent: Intent?): IBinder? = null
```
> تعريف دالة متجاوِزة (override fun) باسم «عند الربط» (onBind) بوسيط «نيّة» (intent) من نوع نيّة قابلة للإفراغ (Intent?) ونوع إعادة «رابط» (IBinder?) قابل للإفراغ، يساوي القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:395]

```
396: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/MeshForegroundService.kt:396]
