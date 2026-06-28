# شريحة — app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt (الأسطر 201–349)

```
201:             listOf(
```
> يبدأ بناء قائمة (listOf) ويفتح قوسها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:201]

```
202:                 Manifest.permission.BLUETOOTH,
```
> يضع داخل القائمة عنصر إذن البلوتوث (Manifest.permission.BLUETOOTH). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:202]

```
203:                 Manifest.permission.BLUETOOTH_ADMIN
```
> يضع داخل القائمة عنصر إذن إدارة البلوتوث (Manifest.permission.BLUETOOTH_ADMIN). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:203]

```
204:             )
```
> إغلاق قوس القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:204]

```
205:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:205]

```
206: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:206]

```
207:         categories.add(
```
> يستدعي إضافة (add) إلى متغيّر الفئات (categories) ويفتح قوس الوسيط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:207]

```
208:             PermissionCategory(
```
> ينشئ كائن فئة إذن (PermissionCategory) ويفتح قوس وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:208]

```
209:                 type = PermissionType.NEARBY_DEVICES,
```
> يضبط الوسيط type على القيمة PermissionType.NEARBY_DEVICES (نوع الأجهزة القريبة). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:209]

```
210:                 description = "Required to discover bitchat users via Bluetooth",
```
> يضبط الوسيط description (الوصف) على النص "Required to discover bitchat users via Bluetooth". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:210]

```
211:                 permissions = bluetoothPermissions,
```
> يضبط الوسيط permissions (الأذونات) على المتغيّر bluetoothPermissions (أذونات البلوتوث). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:211]

```
212:                 isGranted = bluetoothPermissions.all { isPermissionGranted(it) },
```
> يضبط الوسيط isGranted (هل مُنح) على نتيجة all على bluetoothPermissions التي تتحقق أنّ كل عنصر it يحقق isPermissionGranted (هل الإذن ممنوح). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:212]

```
213:                 systemDescription = "Allow bitchat to connect to nearby devices"
```
> يضبط الوسيط systemDescription (وصف النظام) على النص "Allow bitchat to connect to nearby devices". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:213]

```
214:             )
```
> إغلاق قوس وسائط PermissionCategory. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:214]

```
215:         )
```
> إغلاق قوس استدعاء add. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:215]

```
216: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:216]

```
217:         // Location category
```
> تعليق: فئة الموقع. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:217]

```
218:         val locationPermissions = listOf(
```
> يعرّف متغيّراً ثابتاً locationPermissions (أذونات الموقع) ويسنده إلى قائمة listOf ويفتح قوسها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:218]

```
219:             Manifest.permission.ACCESS_COARSE_LOCATION,
```
> يضع في القائمة عنصر إذن الموقع التقريبي (Manifest.permission.ACCESS_COARSE_LOCATION). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:219]

```
220:             Manifest.permission.ACCESS_FINE_LOCATION
```
> يضع في القائمة عنصر إذن الموقع الدقيق (Manifest.permission.ACCESS_FINE_LOCATION). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:220]

```
221:         )
```
> إغلاق قوس القائمة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:221]

```
222: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:222]

```
223:         categories.add(
```
> يستدعي إضافة add إلى categories ويفتح قوس الوسيط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:223]

```
224:             PermissionCategory(
```
> ينشئ كائن PermissionCategory ويفتح قوس وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:224]

```
225:                 type = PermissionType.PRECISE_LOCATION,
```
> يضبط الوسيط type على القيمة PermissionType.PRECISE_LOCATION (نوع الموقع الدقيق). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:225]

```
226:                 description = "Required by Android to discover nearby bitchat users via Bluetooth",
```
> يضبط الوسيط description على النص "Required by Android to discover nearby bitchat users via Bluetooth". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:226]

```
227:                 permissions = locationPermissions,
```
> يضبط الوسيط permissions على المتغيّر locationPermissions. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:227]

```
228:                 isGranted = locationPermissions.all { isPermissionGranted(it) },
```
> يضبط الوسيط isGranted على نتيجة all على locationPermissions التي تتحقق أنّ كل عنصر it يحقق isPermissionGranted. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:228]

```
229:                 systemDescription = "bitchat needs this to scan for nearby devices"
```
> يضبط الوسيط systemDescription على النص "bitchat needs this to scan for nearby devices". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:229]

```
230:             )
```
> إغلاق قوس وسائط PermissionCategory. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:230]

```
231:         )
```
> إغلاق قوس استدعاء add. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:231]

```
232: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:232]

```
233:         // Wi‑Fi Aware category (Android 13+)
```
> تعليق: فئة واي-فاي أوير (Android 13+). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:233]

```
234:         if (shouldRequireWifiAwarePermission()) {
```
> شرط if يستدعي الدالة shouldRequireWifiAwarePermission (هل يجب طلب إذن واي-فاي أوير) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:234]

```
235:             val wifiAwarePermissions = listOf(Manifest.permission.NEARBY_WIFI_DEVICES)
```
> يعرّف متغيّراً ثابتاً wifiAwarePermissions (أذونات واي-فاي أوير) ويسنده إلى قائمة listOf فيها عنصر إذن أجهزة الواي-فاي القريبة (Manifest.permission.NEARBY_WIFI_DEVICES). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:235]

```
236:             categories.add(
```
> يستدعي إضافة add إلى categories ويفتح قوس الوسيط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:236]

```
237:                 PermissionCategory(
```
> ينشئ كائن PermissionCategory ويفتح قوس وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:237]

```
238:                     type = PermissionType.WIFI_AWARE,
```
> يضبط الوسيط type على القيمة PermissionType.WIFI_AWARE (نوع واي-فاي أوير). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:238]

```
239:                     description = "Enable Wi‑Fi Aware to discover and connect to nearby bitchat users over Wi‑Fi.",
```
> يضبط الوسيط description على النص "Enable Wi‑Fi Aware to discover and connect to nearby bitchat users over Wi‑Fi.". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:239]

```
240:                     permissions = wifiAwarePermissions,
```
> يضبط الوسيط permissions على المتغيّر wifiAwarePermissions. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:240]

```
241:                     isGranted = wifiAwarePermissions.all { isPermissionGranted(it) },
```
> يضبط الوسيط isGranted على نتيجة all على wifiAwarePermissions التي تتحقق أنّ كل عنصر it يحقق isPermissionGranted. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:241]

```
242:                     systemDescription = "Allow bitchat to discover nearby Wi‑Fi devices"
```
> يضبط الوسيط systemDescription على النص "Allow bitchat to discover nearby Wi‑Fi devices". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:242]

```
243:                 )
```
> إغلاق قوس وسائط PermissionCategory. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:243]

```
244:             )
```
> إغلاق قوس استدعاء add. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:244]

```
245:         }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:245]

```
246: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:246]

```
247:         if (needsBackgroundLocationPermission()) {
```
> شرط if يستدعي الدالة needsBackgroundLocationPermission (هل يلزم إذن موقع الخلفية) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:247]

```
248:             val backgroundPermission = listOf(Manifest.permission.ACCESS_BACKGROUND_LOCATION)
```
> يعرّف متغيّراً ثابتاً backgroundPermission (إذن الخلفية) ويسنده إلى قائمة listOf فيها عنصر إذن الوصول إلى موقع الخلفية (Manifest.permission.ACCESS_BACKGROUND_LOCATION). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:248]

```
249:             categories.add(
```
> يستدعي إضافة add إلى categories ويفتح قوس الوسيط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:249]

```
250:                 PermissionCategory(
```
> ينشئ كائن PermissionCategory ويفتح قوس وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:250]

```
251:                     type = PermissionType.BACKGROUND_LOCATION,
```
> يضبط الوسيط type على القيمة PermissionType.BACKGROUND_LOCATION (نوع موقع الخلفية). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:251]

```
252:                     description = context.getString(R.string.perm_background_location_desc),
```
> يضبط الوسيط description على نتيجة context.getString للمورد النصّي R.string.perm_background_location_desc. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:252]

```
253:                     permissions = backgroundPermission,
```
> يضبط الوسيط permissions على المتغيّر backgroundPermission. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:253]

```
254:                     isGranted = backgroundPermission.all { isPermissionGranted(it) },
```
> يضبط الوسيط isGranted على نتيجة all على backgroundPermission التي تتحقق أنّ كل عنصر it يحقق isPermissionGranted. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:254]

```
255:                     systemDescription = context.getString(R.string.perm_background_location_system)
```
> يضبط الوسيط systemDescription على نتيجة context.getString للمورد النصّي R.string.perm_background_location_system. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:255]

```
256:                 )
```
> إغلاق قوس وسائط PermissionCategory. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:256]

```
257:             )
```
> إغلاق قوس استدعاء add. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:257]

```
258:         }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:258]

```
259: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:259]

```
260:         // Notifications category (if applicable)
```
> تعليق: فئة الإشعارات (إن كانت قابلة للتطبيق). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:260]

```
261:         if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
```
> شرط if يقارن Build.VERSION.SDK_INT بأن يكون أكبر من أو يساوي Build.VERSION_CODES.TIRAMISU ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:261]

```
262:             categories.add(
```
> يستدعي إضافة add إلى categories ويفتح قوس الوسيط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:262]

```
263:                 PermissionCategory(
```
> ينشئ كائن PermissionCategory ويفتح قوس وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:263]

```
264:                     type = PermissionType.NOTIFICATIONS,
```
> يضبط الوسيط type على القيمة PermissionType.NOTIFICATIONS (نوع الإشعارات). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:264]

```
265:                     description = "Receive notifications when you receive private messages",
```
> يضبط الوسيط description على النص "Receive notifications when you receive private messages". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:265]

```
266:                     permissions = listOf(Manifest.permission.POST_NOTIFICATIONS),
```
> يضبط الوسيط permissions على قائمة listOf فيها عنصر إذن نشر الإشعارات (Manifest.permission.POST_NOTIFICATIONS). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:266]

```
267:                     isGranted = isPermissionGranted(Manifest.permission.POST_NOTIFICATIONS),
```
> يضبط الوسيط isGranted على نتيجة استدعاء isPermissionGranted للإذن Manifest.permission.POST_NOTIFICATIONS. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:267]

```
268:                     systemDescription = "Allow bitchat to send you notifications"
```
> يضبط الوسيط systemDescription على النص "Allow bitchat to send you notifications". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:268]

```
269:                 )
```
> إغلاق قوس وسائط PermissionCategory. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:269]

```
270:             )
```
> إغلاق قوس استدعاء add. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:270]

```
271:         }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:271]

```
272: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:272]

```
273:         // Microphone category removed from onboarding
```
> تعليق: أُزيلت فئة الميكروفون من التهيئة الأولى. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:273]

```
274: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:274]

```
275:         // Battery optimization category (if applicable)
```
> تعليق: فئة تحسين البطارية (إن كانت قابلة للتطبيق). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:275]

```
276:         if (isBatteryOptimizationSupported()) {
```
> شرط if يستدعي الدالة isBatteryOptimizationSupported (هل تحسين البطارية مدعوم) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:276]

```
277:             categories.add(
```
> يستدعي إضافة add إلى categories ويفتح قوس الوسيط. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:277]

```
278:                 PermissionCategory(
```
> ينشئ كائن PermissionCategory ويفتح قوس وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:278]

```
279:                     type = PermissionType.BATTERY_OPTIMIZATION,
```
> يضبط الوسيط type على القيمة PermissionType.BATTERY_OPTIMIZATION (نوع تحسين البطارية). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:279]

```
280:                     description = "Disable battery optimization to ensure bitchat runs reliably in the background and maintains mesh network connections",
```
> يضبط الوسيط description على النص "Disable battery optimization to ensure bitchat runs reliably in the background and maintains mesh network connections". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:280]

```
281:                     permissions = listOf("BATTERY_OPTIMIZATION"), // Custom identifier
```
> يضبط الوسيط permissions على قائمة listOf فيها النص "BATTERY_OPTIMIZATION"، مع تعليق: معرّف مخصّص. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:281]

```
282:                     isGranted = isBatteryOptimizationDisabled(),
```
> يضبط الوسيط isGranted على نتيجة استدعاء الدالة isBatteryOptimizationDisabled (هل تحسين البطارية مُعطَّل). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:282]

```
283:                     systemDescription = "Allow bitchat to run without battery restrictions"
```
> يضبط الوسيط systemDescription على النص "Allow bitchat to run without battery restrictions". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:283]

```
284:                 )
```
> إغلاق قوس وسائط PermissionCategory. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:284]

```
285:             )
```
> إغلاق قوس استدعاء add. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:285]

```
286:         }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:286]

```
287: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:287]

```
288:         return categories
```
> يُعيد المتغيّر categories. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:288]

```
289:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:289]

```
290: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:290]

```
291:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:291]

```
292:      * Get detailed diagnostic information about permission status
```
> تعليق: احصل على معلومات تشخيصية مفصّلة عن حالة الأذونات. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:292]

```
293:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:293]

```
294:     fun getPermissionDiagnostics(): String {
```
> يعرّف الدالة getPermissionDiagnostics (تشخيصات الأذونات) التي تُعيد نوع String ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:294]

```
295:         return buildString {
```
> يُعيد نتيجة buildString (بناء نص) ويفتح نطاق المُستقبِل لها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:295]

```
296:             appendLine("Permission Diagnostics:")
```
> يستدعي appendLine (إلحاق سطر) بالنص "Permission Diagnostics:". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:296]

```
297:             appendLine("Android SDK: ${Build.VERSION.SDK_INT}")
```
> يستدعي appendLine بالنص "Android SDK: " مع القيمة المُستبدَلة Build.VERSION.SDK_INT. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:297]

```
298:             appendLine("First time launch: ${isFirstTimeLaunch()}")
```
> يستدعي appendLine بالنص "First time launch: " مع نتيجة استدعاء الدالة isFirstTimeLaunch (هل أول إطلاق). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:298]

```
299:             appendLine("Required permissions granted: ${areAllPermissionsGranted()}")
```
> يستدعي appendLine بالنص "Required permissions granted: " مع نتيجة استدعاء الدالة areAllPermissionsGranted (هل كل الأذونات ممنوحة). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:299]

```
300:             appendLine()
```
> يستدعي appendLine دون وسيط (إلحاق سطر فارغ). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:300]

```
301:             
```
> سطر فارغ (يحوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:301]

```
302:             getCategorizedPermissions().forEach { category ->
```
> يستدعي الدالة getCategorizedPermissions (الأذونات المصنّفة) ثم forEach على نتيجتها بمعامل lambda اسمه category ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:302]

```
303:                 appendLine("${category.type.nameValue}: ${if (category.isGranted) "✅ GRANTED" else "❌ MISSING"}")
```
> يستدعي appendLine بنص يدمج category.type.nameValue ثم تعبير if يعطي "✅ GRANTED" إن كان category.isGranted صحيحاً وإلا "❌ MISSING". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:303]

```
304:                 category.permissions.forEach { permission ->
```
> يستدعي forEach على category.permissions بمعامل lambda اسمه permission ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:304]

```
305:                     val granted = isPermissionGranted(permission)
```
> يعرّف متغيّراً ثابتاً granted (مُنح) ويسنده إلى نتيجة استدعاء isPermissionGranted للوسيط permission. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:305]

```
306:                     appendLine("  - ${permission.substringAfterLast(".")}: ${if (granted) "✅" else "❌"}")
```
> يستدعي appendLine بنص يبدأ بـ "  - " ثم permission.substringAfterLast(".") (الجزء بعد آخر نقطة) ثم تعبير if يعطي "✅" إن كان granted صحيحاً وإلا "❌". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:306]

```
307:                 }
```
> إغلاق نطاق forEach الداخلي. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:307]

```
308:                 appendLine()
```
> يستدعي appendLine دون وسيط (إلحاق سطر فارغ). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:308]

```
309:             }
```
> إغلاق نطاق forEach الخارجي. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:309]

```
310:             
```
> سطر فارغ (يحوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:310]

```
311:             val missing = getMissingPermissions() + getMissingBackgroundLocationPermission()
```
> يعرّف متغيّراً ثابتاً missing (المفقودة) ويسنده إلى ناتج جمع نتيجة getMissingPermissions (الأذونات المفقودة) مع نتيجة getMissingBackgroundLocationPermission (إذن موقع الخلفية المفقود). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:311]

```
312:             if (missing.isNotEmpty()) {
```
> شرط if يتحقق أنّ missing ليست فارغة عبر isNotEmpty ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:312]

```
313:                 appendLine("Missing permissions:")
```
> يستدعي appendLine بالنص "Missing permissions:". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:313]

```
314:                 missing.forEach { permission ->
```
> يستدعي forEach على missing بمعامل lambda اسمه permission ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:314]

```
315:                     appendLine("- $permission")
```
> يستدعي appendLine بالنص "- " مع القيمة المُستبدَلة permission. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:315]

```
316:                 }
```
> إغلاق نطاق forEach. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:316]

```
317:             }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:317]

```
318:         }
```
> إغلاق نطاق buildString. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:318]

```
319:     }
```
> إغلاق نطاق الدالة getPermissionDiagnostics. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:319]

```
320: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:320]

```
321:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:321]

```
322:      * Log permission status for debugging
```
> تعليق: سجّل حالة الأذونات لأغراض التصحيح. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:322]

```
323:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:323]

```
324:     fun logPermissionStatus() {
```
> يعرّف الدالة logPermissionStatus (تسجيل حالة الأذونات) دون نوع إرجاع مُصرّح ويفتح نطاقها. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:324]

```
325:         Log.d(TAG, getPermissionDiagnostics())
```
> يستدعي Log.d (تسجيل مستوى التصحيح) بالوسم TAG ونتيجة استدعاء getPermissionDiagnostics. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:325]

```
326:     }
```
> إغلاق نطاق الدالة logPermissionStatus. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:326]

```
327: }
```
> إغلاق نطاق الصنف. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:327]

```
328: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:328]

```
329: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:329]

```
330:  * Data class representing a category of related permissions
```
> تعليق: صنف بيانات يمثّل فئة من الأذونات المترابطة. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:330]

```
331:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:331]

```
332: data class PermissionCategory(
```
> يعرّف صنف بيانات (data class) باسم PermissionCategory (فئة إذن) ويفتح قوس معاملاته الأساسية. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:332]

```
333:     val type: PermissionType,
```
> يعرّف خاصية ثابتة type من النوع PermissionType. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:333]

```
334:     val description: String,
```
> يعرّف خاصية ثابتة description من النوع String. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:334]

```
335:     val permissions: List<String>,
```
> يعرّف خاصية ثابتة permissions من النوع List<String> (قائمة نصوص). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:335]

```
336:     val isGranted: Boolean,
```
> يعرّف خاصية ثابتة isGranted من النوع Boolean (منطقي). [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:336]

```
337:     val systemDescription: String
```
> يعرّف خاصية ثابتة systemDescription من النوع String. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:337]

```
338: )
```
> إغلاق قوس معاملات صنف البيانات. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:338]

```
339: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:339]

```
340: enum class PermissionType(val nameValue: String) {
```
> يعرّف صنف تعداد (enum class) باسم PermissionType (نوع الإذن) بمعامل خاصية ثابتة nameValue من النوع String ويفتح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:340]

```
341:     NEARBY_DEVICES("Nearby Devices"),
```
> يعرّف ثابت التعداد NEARBY_DEVICES بقيمة nameValue النص "Nearby Devices". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:341]

```
342:     PRECISE_LOCATION("Precise Location"),
```
> يعرّف ثابت التعداد PRECISE_LOCATION بقيمة nameValue النص "Precise Location". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:342]

```
343:     BACKGROUND_LOCATION("Background Location"),
```
> يعرّف ثابت التعداد BACKGROUND_LOCATION بقيمة nameValue النص "Background Location". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:343]

```
344:     MICROPHONE("Microphone"),
```
> يعرّف ثابت التعداد MICROPHONE بقيمة nameValue النص "Microphone". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:344]

```
345:     NOTIFICATIONS("Notifications"),
```
> يعرّف ثابت التعداد NOTIFICATIONS بقيمة nameValue النص "Notifications". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:345]

```
346:     WIFI_AWARE("Wi‑Fi Aware"),
```
> يعرّف ثابت التعداد WIFI_AWARE بقيمة nameValue النص "Wi‑Fi Aware". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:346]

```
347:     BATTERY_OPTIMIZATION("Battery Optimization"),
```
> يعرّف ثابت التعداد BATTERY_OPTIMIZATION بقيمة nameValue النص "Battery Optimization". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:347]

```
348:     OTHER("Other")
```
> يعرّف ثابت التعداد OTHER بقيمة nameValue النص "Other". [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:348]

```
349: }
```
> إغلاق نطاق صنف التعداد. [app/src/main/java/com/bitchat/android/onboarding/PermissionManager.kt:349]
