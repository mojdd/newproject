# شريحة — app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt (الأسطر 201–247)

```
201:             locationManager?.let { lm ->
```
> يستدعي الدالة `let` على مدير الموقع (locationManager) إن لم يكن فارغاً، ويسمّي القيمة الداخلية `lm`، ويفتح كتلة. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:201]

```
202:                 try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:202]

```
203:                     appendLine("GPS provider enabled: ${lm.isProviderEnabled(LocationManager.GPS_PROVIDER)}")
```
> يستدعي `appendLine` ليُلحق سطراً نصّه «GPS provider enabled: » متبوعاً بنتيجة `lm.isProviderEnabled` لمزوّد GPS الثابت `LocationManager.GPS_PROVIDER`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:203]

```
204:                     appendLine("Network provider enabled: ${lm.isProviderEnabled(LocationManager.NETWORK_PROVIDER)}")
```
> يستدعي `appendLine` ليُلحق سطراً نصّه «Network provider enabled: » متبوعاً بنتيجة `lm.isProviderEnabled` لمزوّد الشبكة الثابت `LocationManager.NETWORK_PROVIDER`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:204]

```
205:                 } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويفتح كتلة التقاط (catch) تلتقط استثناءً من نوع `Exception` وتسمّيه `e`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:205]

```
206:                     appendLine("Provider details: [Error: ${e.message}]")
```
> يستدعي `appendLine` ليُلحق سطراً نصّه «Provider details: [Error: » متبوعاً بـ `e.message` ثم «]». [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:206]

```
207:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:207]

```
208:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:208]

```
209:                 if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
```
> شرط (if) يقارن رقم نسخة الـ SDK `Build.VERSION.SDK_INT` بأنه أكبر من أو يساوي ثابت النسخة `Build.VERSION_CODES.P`، ويفتح كتلة. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:209]

```
210:                     appendLine("Using modern isLocationEnabled() API")
```
> يستدعي `appendLine` ليُلحق سطراً نصّه «Using modern isLocationEnabled() API». [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:210]

```
211:                 } else {
```
> يغلق كتلة الشرط ويفتح كتلة وإلا (else). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:211]

```
212:                     appendLine("Using legacy provider check API")
```
> يستدعي `appendLine` ليُلحق سطراً نصّه «Using legacy provider check API». [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:212]

```
213:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:213]

```
214:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:214]

```
215:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:215]

```
216:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:216]

```
217: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:217]

```
218:     /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:218]

```
219:      * Log current location status for debugging
```
> تعليق: «تسجيل حالة الموقع الحالية لأغراض التنقيح». [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:219]

```
220:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:220]

```
221:     fun logLocationStatus() {
```
> يُعرِّف دالة باسم `logLocationStatus` بلا وُسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:221]

```
222:         Log.d(TAG, getDiagnostics())
```
> يستدعي `Log.d` للتسجيل بمستوى تنقيح (debug) مع الوسم `TAG` ونتيجة استدعاء الدالة `getDiagnostics`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:222]

```
223:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:223]

```
224: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:224]

```
225:     /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:225]

```
226:      * Cleanup resources - call this when activity is destroyed
```
> تعليق: «تنظيف الموارد - استدعِ هذا عند تدمير النشاط (activity)». [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:226]

```
227:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:227]

```
228:     fun cleanup() {
```
> يُعرِّف دالة باسم `cleanup` (التنظيف) بلا وُسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:228]

```
229:         locationStateReceiver?.let { receiver ->
```
> يستدعي الدالة `let` على مستقبِل حالة الموقع (locationStateReceiver) إن لم يكن فارغاً، ويسمّي القيمة الداخلية `receiver`، ويفتح كتلة. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:229]

```
230:             try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:230]

```
231:                 context.unregisterReceiver(receiver)
```
> يستدعي `context.unregisterReceiver` لإلغاء تسجيل المستقبِل `receiver`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:231]

```
232:                 Log.d(TAG, "Location state receiver unregistered")
```
> يستدعي `Log.d` للتسجيل بمستوى تنقيح مع الوسم `TAG` والنص «Location state receiver unregistered». [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:232]

```
233:             } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويفتح كتلة التقاط (catch) تلتقط استثناءً من نوع `Exception` وتسمّيه `e`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:233]

```
234:                 Log.w(TAG, "Error unregistering location state receiver: ${e.message}")
```
> يستدعي `Log.w` للتسجيل بمستوى تحذير (warning) مع الوسم `TAG` والنص «Error unregistering location state receiver: » متبوعاً بـ `e.message`. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:234]

```
235:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:235]

```
236:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:236]

```
237:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:237]

```
238: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:238]

```
239: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:239]

```
240: /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:240]

```
241:  * Location services status enum
```
> تعليق: «تعداد حالة خدمات الموقع». [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:241]

```
242:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:242]

```
243: enum class LocationStatus {
```
> يُعرِّف صنف تعداد (enum class) باسم `LocationStatus` (حالة الموقع) ويفتح جسمه. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:243]

```
244:     ENABLED,
```
> يُعرِّف قيمة تعداد باسم `ENABLED` (مُمكَّنة) تتبعها فاصلة. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:244]

```
245:     DISABLED, 
```
> يُعرِّف قيمة تعداد باسم `DISABLED` (مُعطَّلة) تتبعها فاصلة. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:245]

```
246:     NOT_AVAILABLE
```
> يُعرِّف قيمة تعداد باسم `NOT_AVAILABLE` (غير متاحة). [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:246]

```
247: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationStatusManager.kt:247]
