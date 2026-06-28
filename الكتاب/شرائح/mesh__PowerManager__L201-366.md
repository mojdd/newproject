# شريحة — app/src/main/java/com/bitchat/android/mesh/PowerManager.kt (الأسطر 201–366)

```
201:                 .build()
```
> استدعاء التابع build لإنشاء كائن إعدادات الإعلان (AdvertiseSettings) من البنّاء (Builder). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:201]

```
202:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:202]

```
203:             PowerMode.ULTRA_LOW_POWER -> AdvertiseSettings.Builder()
```
> حالة وضع الطاقة فائق الانخفاض (ULTRA_LOW_POWER) تُعيد بنّاء إعدادات إعلان جديداً عبر AdvertiseSettings.Builder. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:203]

```
204:                 .setAdvertiseMode(AdvertiseSettings.ADVERTISE_MODE_LOW_POWER)
```
> ضبط نمط الإعلان (setAdvertiseMode) إلى القيمة ADVERTISE_MODE_LOW_POWER أي نمط الإعلان منخفض الطاقة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:204]

```
205:                 .setTxPowerLevel(AdvertiseSettings.ADVERTISE_TX_POWER_ULTRA_LOW)
```
> ضبط مستوى قدرة الإرسال (setTxPowerLevel) إلى القيمة ADVERTISE_TX_POWER_ULTRA_LOW أي قدرة إرسال فائقة الانخفاض. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:205]

```
206:                 .setConnectable(true)
```
> ضبط قابلية الاتصال (setConnectable) إلى القيمة true أي قابل للاتصال. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:206]

```
207:                 .setTimeout(0)
```
> ضبط المهلة (setTimeout) إلى القيمة صفر. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:207]

```
208:                 .build()
```
> استدعاء التابع build لإنشاء كائن إعدادات الإعلان من البنّاء. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:208]

```
209:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:209]

```
210:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:210]

```
211:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:211]

```
212:     /**
```
> تعليق توثيقي: بداية كتلة تعليق (/**). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:212]

```
213:      * Get maximum allowed connections for current power mode
```
> تعليق: الحصول على أقصى عدد مسموح من الاتصالات لوضع الطاقة الحالي. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:213]

```
214:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي (*/). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:214]

```
215:     fun getMaxConnections(): Int {
```
> تعريف الدالة getMaxConnections (الحصول على أقصى الاتصالات) التي تُعيد قيمة من نوع Int صحيح. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:215]

```
216:         return when (currentMode) {
```
> إعادة نتيجة تعبير when المبني على الوضع الحالي (currentMode). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:216]

```
217:             PowerMode.PERFORMANCE -> MAX_CONNECTIONS_NORMAL
```
> حالة وضع الأداء (PERFORMANCE) تُعيد القيمة MAX_CONNECTIONS_NORMAL (أقصى اتصالات عادي). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:217]

```
218:             PowerMode.BALANCED -> MAX_CONNECTIONS_NORMAL
```
> حالة الوضع المتوازن (BALANCED) تُعيد القيمة MAX_CONNECTIONS_NORMAL. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:218]

```
219:             PowerMode.POWER_SAVER -> MAX_CONNECTIONS_POWER_SAVE
```
> حالة وضع توفير الطاقة (POWER_SAVER) تُعيد القيمة MAX_CONNECTIONS_POWER_SAVE (أقصى اتصالات توفير الطاقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:219]

```
220:             PowerMode.ULTRA_LOW_POWER -> MAX_CONNECTIONS_ULTRA_LOW
```
> حالة وضع الطاقة فائق الانخفاض (ULTRA_LOW_POWER) تُعيد القيمة MAX_CONNECTIONS_ULTRA_LOW (أقصى اتصالات فائق الانخفاض). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:220]

```
221:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:221]

```
222:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:222]

```
223:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:223]

```
224:     /**
```
> تعليق توثيقي: بداية كتلة تعليق (/**). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:224]

```
225:      * Get RSSI filter threshold for current power mode
```
> تعليق: الحصول على عتبة مُرشِّح قوة الإشارة المستقبَلة (RSSI) لوضع الطاقة الحالي. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:225]

```
226:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي (*/). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:226]

```
227:     fun getRSSIThreshold(): Int {
```
> تعريف الدالة getRSSIThreshold (الحصول على عتبة قوة الإشارة) التي تُعيد قيمة من نوع Int صحيح. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:227]

```
228:         return when (currentMode) {
```
> إعادة نتيجة تعبير when المبني على الوضع الحالي (currentMode). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:228]

```
229:             PowerMode.PERFORMANCE -> -95
```
> حالة وضع الأداء (PERFORMANCE) تُعيد القيمة سالب خمسة وتسعين. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:229]

```
230:             PowerMode.BALANCED -> -85
```
> حالة الوضع المتوازن (BALANCED) تُعيد القيمة سالب خمسة وثمانين. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:230]

```
231:             PowerMode.POWER_SAVER -> -75
```
> حالة وضع توفير الطاقة (POWER_SAVER) تُعيد القيمة سالب خمسة وسبعين. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:231]

```
232:             PowerMode.ULTRA_LOW_POWER -> -65
```
> حالة وضع الطاقة فائق الانخفاض (ULTRA_LOW_POWER) تُعيد القيمة سالب خمسة وستين. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:232]

```
233:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:233]

```
234:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:234]

```
235:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:235]

```
236:     /**
```
> تعليق توثيقي: بداية كتلة تعليق (/**). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:236]

```
237:      * Check if duty cycling should be used
```
> تعليق: التحقق ممّا إذا كان ينبغي استخدام دورة التشغيل (duty cycling). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:237]

```
238:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي (*/). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:238]

```
239:     fun shouldUseDutyCycle(): Boolean {
```
> تعريف الدالة shouldUseDutyCycle (هل ينبغي استخدام دورة التشغيل) التي تُعيد قيمة من نوع Boolean منطقي. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:239]

```
240:         return currentMode != PowerMode.PERFORMANCE
```
> إعادة نتيجة المقارنة: الوضع الحالي (currentMode) لا يساوي وضع الأداء (PERFORMANCE). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:240]

```
241:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:241]

```
242:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:242]

```
243:     /**
```
> تعليق توثيقي: بداية كتلة تعليق (/**). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:243]

```
244:      * Get current power mode information
```
> تعليق: الحصول على معلومات وضع الطاقة الحالي. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:244]

```
245:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي (*/). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:245]

```
246:     fun getPowerInfo(): String {
```
> تعريف الدالة getPowerInfo (الحصول على معلومات الطاقة) التي تُعيد قيمة من نوع String نصّي. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:246]

```
247:         return buildString {
```
> إعادة نتيجة باني السلسلة النصية (buildString) مع كتلة بناء. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:247]

```
248:             appendLine("=== Power Manager Status ===")
```
> إلحاق سطر (appendLine) بالنص الحرفي "=== Power Manager Status ===". [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:248]

```
249:             appendLine("Current Mode: $currentMode")
```
> إلحاق سطر بالنص "Current Mode: " متبوعاً بقيمة المتغير currentMode (الوضع الحالي). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:249]

```
250:             appendLine("Battery Level: $batteryLevel%")
```
> إلحاق سطر بالنص "Battery Level: " متبوعاً بقيمة المتغير batteryLevel (مستوى البطارية) وعلامة النسبة المئوية. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:250]

```
251:             appendLine("Is Charging: $isCharging")
```
> إلحاق سطر بالنص "Is Charging: " متبوعاً بقيمة المتغير isCharging (هل يشحن). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:251]

```
252:             appendLine("App In Background: $isAppInBackground")
```
> إلحاق سطر بالنص "App In Background: " متبوعاً بقيمة المتغير isAppInBackground (هل التطبيق في الخلفية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:252]

```
253:             appendLine("Max Connections: ${getMaxConnections()}")
```
> إلحاق سطر بالنص "Max Connections: " متبوعاً بنتيجة استدعاء الدالة getMaxConnections. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:253]

```
254:             appendLine("RSSI Threshold: ${getRSSIThreshold()} dBm")
```
> إلحاق سطر بالنص "RSSI Threshold: " متبوعاً بنتيجة استدعاء الدالة getRSSIThreshold ثم الوحدة "dBm". [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:254]

```
255:             appendLine("Use Duty Cycle: ${shouldUseDutyCycle()}")
```
> إلحاق سطر بالنص "Use Duty Cycle: " متبوعاً بنتيجة استدعاء الدالة shouldUseDutyCycle. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:255]

```
256:         }
```
> إغلاق نطاق كتلة buildString. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:256]

```
257:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:257]

```
258:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:258]

```
259:     private fun updatePowerMode() {
```
> تعريف دالة خاصة (private) باسم updatePowerMode (تحديث وضع الطاقة) بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:259]

```
260:         // Determine the base mode from battery/charging state only
```
> تعليق: تحديد الوضع الأساسي من حالة البطارية/الشحن فقط. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:260]

```
261:         val baseMode = when {
```
> تعريف متغير ثابت (val) باسم baseMode (الوضع الأساسي) قيمته نتيجة تعبير when بلا وسيط. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:261]

```
262:             // Charging in foreground may use performance
```
> تعليق: الشحن في الواجهة الأمامية قد يستخدم وضع الأداء. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:262]

```
263:             isCharging && !isAppInBackground -> PowerMode.PERFORMANCE
```
> شرط: إذا كان isCharging صحيحاً والتطبيق ليس في الخلفية (نفي isAppInBackground) فالنتيجة وضع الأداء (PERFORMANCE). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:263]

```
264:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:264]

```
265:             // Critical battery - force ultra low power regardless of foreground/background
```
> تعليق: بطارية حرجة - فرض الطاقة فائقة الانخفاض بصرف النظر عن الواجهة الأمامية/الخلفية. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:265]

```
266:             batteryLevel <= CRITICAL_BATTERY -> PowerMode.ULTRA_LOW_POWER
```
> شرط: إذا كان مستوى البطارية أقل من أو يساوي CRITICAL_BATTERY (البطارية الحرجة) فالنتيجة وضع الطاقة فائق الانخفاض (ULTRA_LOW_POWER). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:266]

```
267:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:267]

```
268:             // Low battery - prefer power saver
```
> تعليق: بطارية منخفضة - تفضيل وضع توفير الطاقة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:268]

```
269:             batteryLevel <= LOW_BATTERY -> PowerMode.POWER_SAVER
```
> شرط: إذا كان مستوى البطارية أقل من أو يساوي LOW_BATTERY (البطارية المنخفضة) فالنتيجة وضع توفير الطاقة (POWER_SAVER). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:269]

```
270:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:270]

```
271:             // Otherwise balanced
```
> تعليق: خلاف ذلك متوازن. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:271]

```
272:             else -> PowerMode.BALANCED
```
> الحالة الافتراضية (else) تُعيد الوضع المتوازن (BALANCED). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:272]

```
273:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:273]

```
274:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:274]

```
275:         // If app is in background (including when running as a foreground service),
```
> تعليق: إذا كان التطبيق في الخلفية (بما في ذلك عند تشغيله كخدمة أمامية)،. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:275]

```
276:         // cap the power mode to at least POWER_SAVER. Preserve ULTRA_LOW_POWER.
```
> تعليق: حُدّ وضع الطاقة بما لا يقل عن POWER_SAVER. احفظ ULTRA_LOW_POWER. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:276]

```
277:         val newMode = if (isAppInBackground) {
```
> تعريف متغير ثابت (val) باسم newMode (الوضع الجديد) قيمته نتيجة شرط if على isAppInBackground (هل التطبيق في الخلفية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:277]

```
278:             if (baseMode == PowerMode.ULTRA_LOW_POWER) PowerMode.ULTRA_LOW_POWER else PowerMode.POWER_SAVER
```
> شرط: إذا كان baseMode يساوي ULTRA_LOW_POWER فالقيمة ULTRA_LOW_POWER وإلا POWER_SAVER. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:278]

```
279:         } else {
```
> فرع else لشرط if الخاص بـ isAppInBackground. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:279]

```
280:             baseMode
```
> القيمة في فرع else هي baseMode (الوضع الأساسي). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:280]

```
281:         }
```
> إغلاق نطاق تعبير if/else. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:281]

```
282:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:282]

```
283:         if (newMode != currentMode) {
```
> شرط: إذا كان newMode (الوضع الجديد) لا يساوي currentMode (الوضع الحالي). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:283]

```
284:             val oldMode = currentMode
```
> تعريف متغير ثابت (val) باسم oldMode (الوضع القديم) قيمته currentMode (الوضع الحالي). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:284]

```
285:             currentMode = newMode
```
> إسناد قيمة newMode (الوضع الجديد) إلى المتغير currentMode (الوضع الحالي). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:285]

```
286:             Log.i(TAG, "Power mode changed: $oldMode → $newMode (battery: $batteryLevel%, charging: $isCharging, background: $isAppInBackground)")
```
> استدعاء Log.i لتسجيل رسالة معلومات بوسم TAG ونص "Power mode changed: " يتضمّن oldMode وnewMode وbatteryLevel وisCharging وisAppInBackground. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:286]

```
287:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:287]

```
288:             delegate?.onPowerModeChanged(currentMode)
```
> استدعاء آمن من العدم (?.) للتابع onPowerModeChanged على المفوَّض (delegate) مع تمرير currentMode (الوضع الحالي). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:288]

```
289:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:289]

```
290:             // Restart duty cycle with new parameters
```
> تعليق: إعادة تشغيل دورة التشغيل بمعاملات جديدة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:290]

```
291:             if (shouldUseDutyCycle()) {
```
> شرط: إذا أعادت الدالة shouldUseDutyCycle قيمة صحيحة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:291]

```
292:                 startDutyCycle()
```
> استدعاء الدالة startDutyCycle (بدء دورة التشغيل). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:292]

```
293:             } else {
```
> فرع else للشرط السابق. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:293]

```
294:                 stopDutyCycle()
```
> استدعاء الدالة stopDutyCycle (إيقاف دورة التشغيل). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:294]

```
295:             }
```
> إغلاق نطاق تعبير if/else. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:295]

```
296:         }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:296]

```
297:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:297]

```
298:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:298]

```
299:     private fun startDutyCycle() {
```
> تعريف دالة خاصة (private) باسم startDutyCycle (بدء دورة التشغيل) بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:299]

```
300:         stopDutyCycle()
```
> استدعاء الدالة stopDutyCycle (إيقاف دورة التشغيل). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:300]

```
301:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:301]

```
302:         if (!shouldUseDutyCycle()) {
```
> شرط: إذا كانت نتيجة الدالة shouldUseDutyCycle منفيّة (أي يجب عدم استخدام دورة التشغيل). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:302]

```
303:             delegate?.onScanStateChanged(true) // Always scan in performance mode
```
> استدعاء آمن من العدم للتابع onScanStateChanged على المفوَّض مع تمرير true، وتعليق: المسح دوماً في وضع الأداء. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:303]

```
304:             return
```
> إعادة (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:304]

```
305:         }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:305]

```
306:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:306]

```
307:         val (onDuration, offDuration) = when (currentMode) {
```
> تعريف متغيرين ثابتين عبر التفكيك (onDuration مدة التشغيل، offDuration مدة الإيقاف) من نتيجة تعبير when المبني على currentMode. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:307]

```
308:             PowerMode.BALANCED -> SCAN_ON_DURATION_NORMAL to SCAN_OFF_DURATION_NORMAL
```
> حالة الوضع المتوازن (BALANCED) تُعيد الزوج SCAN_ON_DURATION_NORMAL مع SCAN_OFF_DURATION_NORMAL عبر to. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:308]

```
309:             PowerMode.POWER_SAVER -> SCAN_ON_DURATION_POWER_SAVE to SCAN_OFF_DURATION_POWER_SAVE
```
> حالة وضع توفير الطاقة (POWER_SAVER) تُعيد الزوج SCAN_ON_DURATION_POWER_SAVE مع SCAN_OFF_DURATION_POWER_SAVE عبر to. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:309]

```
310:             PowerMode.ULTRA_LOW_POWER -> SCAN_ON_DURATION_ULTRA_LOW to SCAN_OFF_DURATION_ULTRA_LOW
```
> حالة وضع الطاقة فائق الانخفاض (ULTRA_LOW_POWER) تُعيد الزوج SCAN_ON_DURATION_ULTRA_LOW مع SCAN_OFF_DURATION_ULTRA_LOW عبر to. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:310]

```
311:             PowerMode.PERFORMANCE -> return // No duty cycle
```
> حالة وضع الأداء (PERFORMANCE) تنفّذ return للخروج من الدالة، وتعليق: لا دورة تشغيل. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:311]

```
312:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:312]

```
313:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:313]

```
314:         dutyCycleJob = powerScope.launch {
```
> إسناد إلى المتغير dutyCycleJob (مهمة دورة التشغيل) نتيجة استدعاء launch على النطاق powerScope (نطاق الطاقة) مع كتلة معلَّقة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:314]

```
315:             while (isActive && shouldUseDutyCycle()) {
```
> حلقة while تستمر ما دام isActive صحيحاً ونتيجة shouldUseDutyCycle صحيحة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:315]

```
316:                 // Scan ON period
```
> تعليق: فترة تشغيل المسح. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:316]

```
317:                 Log.d(TAG, "Duty cycle: Scan ON for ${onDuration}ms")
```
> استدعاء Log.d لتسجيل رسالة تصحيح بوسم TAG ونص "Duty cycle: Scan ON for " متبوعاً بقيمة onDuration والوحدة ms. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:317]

```
318:                 delegate?.onScanStateChanged(true)
```
> استدعاء آمن من العدم للتابع onScanStateChanged على المفوَّض مع تمرير true. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:318]

```
319:                 delay(onDuration)
```
> استدعاء دالة التأخير المعلَّقة delay لمدة onDuration. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:319]

```
320:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:320]

```
321:                 // Scan OFF period (keep advertising active)
```
> تعليق: فترة إيقاف المسح (إبقاء الإعلان نشطاً). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:321]

```
322:                 if (isActive && shouldUseDutyCycle()) {
```
> شرط: إذا كان isActive صحيحاً ونتيجة shouldUseDutyCycle صحيحة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:322]

```
323:                     Log.d(TAG, "Duty cycle: Scan OFF for ${offDuration}ms")
```
> استدعاء Log.d لتسجيل رسالة تصحيح بوسم TAG ونص "Duty cycle: Scan OFF for " متبوعاً بقيمة offDuration والوحدة ms. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:323]

```
324:                     delegate?.onScanStateChanged(false)
```
> استدعاء آمن من العدم للتابع onScanStateChanged على المفوَّض مع تمرير false. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:324]

```
325:                     delay(offDuration)
```
> استدعاء دالة التأخير المعلَّقة delay لمدة offDuration. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:325]

```
326:                 }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:326]

```
327:             }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:327]

```
328:         }
```
> إغلاق نطاق كتلة launch. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:328]

```
329:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:329]

```
330:         Log.i(TAG, "Started duty cycle: ${onDuration}ms ON, ${offDuration}ms OFF")
```
> استدعاء Log.i لتسجيل رسالة معلومات بوسم TAG ونص "Started duty cycle: " متبوعاً بقيمة onDuration والوحدة ms ON ثم offDuration والوحدة ms OFF. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:330]

```
331:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:331]

```
332:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:332]

```
333:     private fun stopDutyCycle() {
```
> تعريف دالة خاصة (private) باسم stopDutyCycle (إيقاف دورة التشغيل) بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:333]

```
334:         dutyCycleJob?.cancel()
```
> استدعاء آمن من العدم للتابع cancel على المتغير dutyCycleJob (مهمة دورة التشغيل). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:334]

```
335:         dutyCycleJob = null
```
> إسناد القيمة null (العدم) إلى المتغير dutyCycleJob. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:335]

```
336:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:336]

```
337:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:337]

```
338:     private fun registerBatteryReceiver() {
```
> تعريف دالة خاصة (private) باسم registerBatteryReceiver (تسجيل مستقبِل البطارية) بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:338]

```
339:         try {
```
> بداية كتلة try (محاولة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:339]

```
340:             val filter = IntentFilter().apply {
```
> تعريف متغير ثابت (val) باسم filter (مُرشِّح) قيمته كائن IntentFilter جديد مع كتلة apply. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:340]

```
341:                 addAction(Intent.ACTION_BATTERY_CHANGED)
```
> استدعاء addAction لإضافة الإجراء Intent.ACTION_BATTERY_CHANGED (تغيّر البطارية). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:341]

```
342:                 addAction(Intent.ACTION_POWER_CONNECTED)
```
> استدعاء addAction لإضافة الإجراء Intent.ACTION_POWER_CONNECTED (توصيل الطاقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:342]

```
343:                 addAction(Intent.ACTION_POWER_DISCONNECTED)
```
> استدعاء addAction لإضافة الإجراء Intent.ACTION_POWER_DISCONNECTED (فصل الطاقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:343]

```
344:             }
```
> إغلاق نطاق كتلة apply. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:344]

```
345:             context.registerReceiver(batteryReceiver, filter)
```
> استدعاء registerReceiver على السياق (context) لتسجيل المستقبِل batteryReceiver مع المُرشِّح filter. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:345]

```
346:         } catch (e: Exception) {
```
> بداية كتلة catch لالتقاط استثناء من نوع Exception باسم e. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:346]

```
347:             Log.w(TAG, "Failed to register battery receiver: ${e.message}")
```
> استدعاء Log.w لتسجيل رسالة تحذير بوسم TAG ونص "Failed to register battery receiver: " متبوعاً بقيمة e.message (رسالة الاستثناء). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:347]

```
348:         }
```
> إغلاق نطاق كتلة try/catch. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:348]

```
349:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:349]

```
350:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:350]

```
351:     private fun unregisterBatteryReceiver() {
```
> تعريف دالة خاصة (private) باسم unregisterBatteryReceiver (إلغاء تسجيل مستقبِل البطارية) بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:351]

```
352:         try {
```
> بداية كتلة try (محاولة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:352]

```
353:             context.unregisterReceiver(batteryReceiver)
```
> استدعاء unregisterReceiver على السياق (context) لإلغاء تسجيل المستقبِل batteryReceiver. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:353]

```
354:         } catch (e: Exception) {
```
> بداية كتلة catch لالتقاط استثناء من نوع Exception باسم e. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:354]

```
355:             Log.w(TAG, "Failed to unregister battery receiver: ${e.message}")
```
> استدعاء Log.w لتسجيل رسالة تحذير بوسم TAG ونص "Failed to unregister battery receiver: " متبوعاً بقيمة e.message (رسالة الاستثناء). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:355]

```
356:         }
```
> إغلاق نطاق كتلة try/catch. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:356]

```
357:     }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:357]

```
358: }
```
> إغلاق نطاق الصنف PowerManager. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:358]

```
359:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:359]

```
360: /**
```
> تعليق توثيقي: بداية كتلة تعليق (/**). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:360]

```
361:  * Delegate interface for power management callbacks
```
> تعليق: واجهة المفوَّض لاستدعاءات إدارة الطاقة الراجعة (callbacks). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:361]

```
362:  */
```
> تعليق: نهاية كتلة التعليق التوثيقي (*/). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:362]

```
363: interface PowerManagerDelegate {
```
> تعريف الواجهة (interface) باسم PowerManagerDelegate (مفوَّض مدير الطاقة). [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:363]

```
364:     fun onPowerModeChanged(newMode: PowerManager.PowerMode)
```
> تصريح التابع المجرّد onPowerModeChanged (عند تغيّر وضع الطاقة) بمعامل newMode من النوع PowerManager.PowerMode. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:364]

```
365:     fun onScanStateChanged(shouldScan: Boolean)
```
> تصريح التابع المجرّد onScanStateChanged (عند تغيّر حالة المسح) بمعامل shouldScan من النوع Boolean منطقي. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:365]

```
366: }
```
> إغلاق نطاق الواجهة PowerManagerDelegate. [app/src/main/java/com/bitchat/android/mesh/PowerManager.kt:366]
