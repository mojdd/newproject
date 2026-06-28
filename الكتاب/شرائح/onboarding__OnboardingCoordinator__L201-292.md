# شريحة — app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt (الأسطر 201–292)

```
201:         Log.w(TAG, "Partial permissions granted: $message")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم TAG ونصّ «Partial permissions granted: » متبوعاً بقيمة المتغيّر message. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:201]

```
202:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:202]

```
203:         // For now, we'll proceed anyway and let the user experience the limitations
```
> تعليق: في الوقت الحالي، سنتابع على أي حال وندع المستخدم يختبر القيود. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:203]

```
204:         // In a production app, you might want to show a dialog explaining the limitations
```
> تعليق: في تطبيق إنتاجي، قد ترغب بعرض مربّع حوار يشرح القيود. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:204]

```
205:         completeOnboarding()
```
> تُستدعى الدالة إتمام التهيئة (completeOnboarding). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:205]

```
206:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:206]

```
207: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:207]

```
208:     /**
```
> بداية تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:208]

```
209:      * Handle permission denial scenarios
```
> تعليق: التعامل مع سيناريوهات رفض الأذونات. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:209]

```
210:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:210]

```
211:     private fun handlePermissionDenial(permissions: Map<String, Boolean>) {
```
> تُعرَّف دالة خاصة (private) باسم التعامل مع رفض الأذونات (handlePermissionDenial) تأخذ معامِلاً اسمه permissions من نوع خريطة (Map) مفاتيحها نصوص وقيمها قيم منطقية. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:211]

```
212:         val deniedCritical = permissions.filter { !it.value && getCriticalPermissions().contains(it.key) }
```
> يُعرَّف متغيّر ثابت (val) باسم المرفوض الحَرِج (deniedCritical) يساوي ناتج تصفية (filter) الخريطة permissions على العناصر التي قيمتها false وفي الوقت ذاته يحتوي ناتج getCriticalPermissions على مفتاحها. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:212]

```
213:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:213]

```
214:         if (deniedCritical.isNotEmpty()) {
```
> تُفتح جملة شرطية (if) شرطها أن deniedCritical ليس فارغاً (isNotEmpty). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:214]

```
215:             val message = buildString {
```
> يُعرَّف متغيّر ثابت (val) باسم message يساوي ناتج بناء نص (buildString) عبر كتلة لاحقة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:215]

```
216:                 append("Critical permissions were denied. bitchat requires these permissions to function:\n")
```
> يُلحَق (append) إلى النص العبارة «Critical permissions were denied. bitchat requires these permissions to function:» متبوعة بسطر جديد. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:216]

```
217:                 deniedCritical.keys.forEach { permission ->
```
> يُكرَّر (forEach) على مفاتيح (keys) deniedCritical مع تسمية كل عنصر permission. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:217]

```
218:                     append("- ${getPermissionDisplayName(permission)}\n")
```
> يُلحَق إلى النص شرطة وفراغ ثم ناتج getPermissionDisplayName للمعامل permission متبوعاً بسطر جديد. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:218]

```
219:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:219]

```
220:                 append("\nPlease grant these permissions in Settings to use bitchat.")
```
> يُلحَق إلى النص سطر جديد ثم العبارة «Please grant these permissions in Settings to use bitchat.». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:220]

```
221:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:221]

```
222:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:222]

```
223:             Log.e(TAG, "Critical permissions denied: $deniedCritical")
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم TAG ونصّ «Critical permissions denied: » متبوعاً بقيمة deniedCritical. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:223]

```
224:             onOnboardingFailed(message)
```
> تُستدعى دالة الاستدعاء عند فشل التهيئة (onOnboardingFailed) ممرَّراً إليها message. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:224]

```
225:         } else {
```
> إغلاق نطاق الـ if وفتح فرع وإلا (else). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:225]

```
226:             // Shouldn't happen given our logic above, but handle gracefully
```
> تعليق: لا ينبغي أن يحدث بالنظر إلى منطقنا أعلاه، لكن نعالجه بلطف. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:226]

```
227:             completeOnboarding()
```
> تُستدعى الدالة إتمام التهيئة (completeOnboarding). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:227]

```
228:         }
```
> إغلاق نطاق فرع else. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:228]

```
229:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:229]

```
230: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:230]

```
231:     /**
```
> بداية تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:231]

```
232:      * Complete the onboarding process and initialize the app
```
> تعليق: إتمام عملية التهيئة وتهيئة التطبيق. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:232]

```
233:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:233]

```
234:     private fun completeOnboarding() {
```
> تُعرَّف دالة خاصة (private) باسم إتمام التهيئة (completeOnboarding) بلا معامِلات. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:234]

```
235:         Log.d(TAG, "Completing onboarding process")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم TAG ونصّ «Completing onboarding process». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:235]

```
236:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:236]

```
237:         // Mark onboarding as complete
```
> تعليق: وسم التهيئة على أنها مكتملة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:237]

```
238:         permissionManager.markOnboardingComplete()
```
> يُستدعى من مدير الأذونات (permissionManager) دالة وسم اكتمال التهيئة (markOnboardingComplete). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:238]

```
239:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:239]

```
240:         // Log final permission status
```
> تعليق: تسجيل حالة الأذونات النهائية. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:240]

```
241:         permissionManager.logPermissionStatus()
```
> يُستدعى من مدير الأذونات دالة تسجيل حالة الأذونات (logPermissionStatus). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:241]

```
242:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:242]

```
243:         // Notify completion with a small delay to ensure everything is ready
```
> تعليق: الإخطار بالاكتمال مع تأخير صغير لضمان جاهزية كل شيء. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:243]

```
244:         activity.lifecycleScope.launch {
```
> يُطلَق (launch) كوروتين (coroutine) ضمن نطاق دورة حياة (lifecycleScope) التابع لـ activity عبر كتلة لاحقة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:244]

```
245:             kotlinx.coroutines.delay(100) // Small delay for UI state to settle
```
> تُستدعى دالة التأخير (kotlinx.coroutines.delay) بقيمة 100، وتعليق: تأخير صغير ليستقرّ حال واجهة المستخدم. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:245]

```
246:             onOnboardingComplete()
```
> تُستدعى دالة الاستدعاء عند اكتمال التهيئة (onOnboardingComplete). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:246]

```
247:         }
```
> إغلاق نطاق كتلة الإطلاق (launch). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:247]

```
248:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:248]

```
249: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:249]

```
250:     /**
```
> بداية تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:250]

```
251:      * Open app settings for manual permission management
```
> تعليق: فتح إعدادات التطبيق لإدارة الأذونات يدوياً. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:251]

```
252:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:252]

```
253:     fun openAppSettings() {
```
> تُعرَّف دالة عامة باسم فتح إعدادات التطبيق (openAppSettings) بلا معامِلات. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:253]

```
254:         try {
```
> تُفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:254]

```
255:             val intent = Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS).apply {
```
> يُعرَّف متغيّر ثابت (val) باسم intent يساوي كائن نيّة (Intent) منشأ بالفعل Settings.ACTION_APPLICATION_DETAILS_SETTINGS مع كتلة apply لاحقة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:255]

```
256:                 data = android.net.Uri.fromParts("package", activity.packageName, null)
```
> تُسنَد الخاصية data إلى ناتج android.net.Uri.fromParts بالمعامِلات «package» واسم حزمة activity (activity.packageName) وقيمة null. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:256]

```
257:                 addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
```
> تُستدعى دالة إضافة الرايات (addFlags) بالقيمة Intent.FLAG_ACTIVITY_NEW_TASK. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:257]

```
258:             }
```
> إغلاق نطاق كتلة apply. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:258]

```
259:             activity.startActivity(intent)
```
> تُستدعى من activity دالة بدء النشاط (startActivity) ممرَّراً إليها intent. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:259]

```
260:             Log.d(TAG, "Opened app settings for manual permission management")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم TAG ونصّ «Opened app settings for manual permission management». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:260]

```
261:         } catch (e: Exception) {
```
> إغلاق نطاق try وفتح كتلة التقاط (catch) لاستثناء (Exception) اسمه e. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:261]

```
262:             Log.e(TAG, "Failed to open app settings", e)
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم TAG ونصّ «Failed to open app settings» والاستثناء e. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:262]

```
263:         }
```
> إغلاق نطاق كتلة catch. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:263]

```
264:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:264]

```
265: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:265]

```
266:     /**
```
> بداية تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:266]

```
267:      * Convert permission string to user-friendly display name
```
> تعليق: تحويل نص الإذن إلى اسم عرض سهل على المستخدم. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:267]

```
268:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:268]

```
269:     private fun getPermissionDisplayName(permission: String): String {
```
> تُعرَّف دالة خاصة (private) باسم جلب اسم عرض الإذن (getPermissionDisplayName) تأخذ معامِلاً نصياً اسمه permission وتُعيد نصاً (String). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:269]

```
270:         return when {
```
> تُعاد قيمة تعبير when بلا وسيط (شروط منطقية). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:270]

```
271:             permission.contains("BLUETOOTH") -> "Bluetooth/Nearby Devices"
```
> إذا احتوى permission على «BLUETOOTH» تُعاد القيمة «Bluetooth/Nearby Devices». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:271]

```
272:             permission.contains("BACKGROUND") -> "Background Location"
```
> إذا احتوى permission على «BACKGROUND» تُعاد القيمة «Background Location». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:272]

```
273:             permission.contains("LOCATION") -> "Location (for Bluetooth scanning)"
```
> إذا احتوى permission على «LOCATION» تُعاد القيمة «Location (for Bluetooth scanning)». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:273]

```
274:             permission.contains("NEARBY_WIFI") -> "Nearby Wi‑Fi Devices (for Wi‑Fi Aware)"
```
> إذا احتوى permission على «NEARBY_WIFI» تُعاد القيمة «Nearby Wi‑Fi Devices (for Wi‑Fi Aware)». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:274]

```
275:             permission.contains("NOTIFICATION") -> "Notifications"
```
> إذا احتوى permission على «NOTIFICATION» تُعاد القيمة «Notifications». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:275]

```
276:             else -> permission.substringAfterLast(".")
```
> في الحالة الأخرى (else) تُعاد القيمة الناتجة عن substringAfterLast للنص permission بفاصل النقطة «.». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:276]

```
277:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:277]

```
278:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:278]

```
279: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:279]

```
280:     /**
```
> بداية تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:280]

```
281:      * Get diagnostic information for troubleshooting
```
> تعليق: جلب معلومات تشخيصية لاستكشاف الأخطاء. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:281]

```
282:      */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:282]

```
283:     fun getDiagnostics(): String {
```
> تُعرَّف دالة عامة باسم جلب التشخيصات (getDiagnostics) بلا معامِلات وتُعيد نصاً (String). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:283]

```
284:         return buildString {
```
> تُعاد قيمة ناتج بناء نص (buildString) عبر كتلة لاحقة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:284]

```
285:             appendLine("Onboarding Coordinator Diagnostics:")
```
> يُلحَق سطر (appendLine) بالنص «Onboarding Coordinator Diagnostics:». [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:285]

```
286:             appendLine("Activity: ${activity::class.simpleName}")
```
> يُلحَق سطر (appendLine) بالنص «Activity: » متبوعاً بالاسم المبسّط (simpleName) لصنف activity. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:286]

```
287:             appendLine("Permission launcher: ${permissionLauncher != null}")
```
> يُلحَق سطر (appendLine) بالنص «Permission launcher: » متبوعاً بنتيجة مقارنة permissionLauncher بأنه لا يساوي null. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:287]

```
288:             appendLine()
```
> يُلحَق سطر فارغ (appendLine) بلا وسيط. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:288]

```
289:             append(permissionManager.getPermissionDiagnostics())
```
> يُلحَق (append) ناتج استدعاء getPermissionDiagnostics من مدير الأذونات (permissionManager). [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:289]

```
290:         }
```
> إغلاق نطاق كتلة buildString. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:290]

```
291:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:291]

```
292: }
```
> إغلاق نطاق الصنف. [app/src/main/java/com/bitchat/android/onboarding/OnboardingCoordinator.kt:292]
