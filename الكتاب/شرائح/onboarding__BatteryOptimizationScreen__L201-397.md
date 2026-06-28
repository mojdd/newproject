# شريحة — app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt (الأسطر 201–397)

```
201:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:201]

```
202:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:202]

```
203:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:203]

```
204:         // Fixed buttons at the bottom
```
> تعليق: أزرار ثابتة في الأسفل. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:204]

```
205:         Column(
```
> يُستدعى مكوّن العمود (Column) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:205]

```
206:             verticalArrangement = Arrangement.spacedBy(12.dp),
```
> يُضبط التنظيم الرأسي (verticalArrangement) على ترتيب متباعد (Arrangement.spacedBy) بمقدار ١٢ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:206]

```
207:             horizontalAlignment = Alignment.CenterHorizontally
```
> يُضبط المحاذاة الأفقية (horizontalAlignment) على التوسيط الأفقي (Alignment.CenterHorizontally). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:207]

```
208:         ) {
```
> إغلاق قائمة المُعاملات وفتح نطاق المحتوى اللمسي (lambda) للعمود. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:208]

```
209:             Button(
```
> يُستدعى مكوّن الزر (Button) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:209]

```
210:                 onClick = onDisableBatteryOptimization,
```
> يُضبط مُعامل النقر (onClick) على الدالة الواردة لتعطيل تحسين البطارية (onDisableBatteryOptimization). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:210]

```
211:                 modifier = Modifier.fillMaxWidth(),
```
> يُضبط المُعدِّل (modifier) على ملء العرض الأقصى (fillMaxWidth). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:211]

```
212:                 enabled = !isLoading,
```
> يُضبط مُعامل التمكين (enabled) على نفي حالة التحميل (isLoading). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:212]

```
213:                 colors = ButtonDefaults.buttonColors(
```
> يُضبط مُعامل الألوان (colors) باستدعاء ألوان الزر الافتراضية (ButtonDefaults.buttonColors) مع فتح قائمة مُعاملاتها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:213]

```
214:                     containerColor = colorScheme.primary
```
> يُضبط لون الحاوية (containerColor) على اللون الأساسي (colorScheme.primary) من نظام الألوان. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:214]

```
215:                 )
```
> إغلاق قائمة مُعاملات ألوان الزر. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:215]

```
216:             ) {
```
> إغلاق قائمة مُعاملات الزر وفتح نطاق محتواه اللمسي (lambda). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:216]

```
217:                 if (isLoading) {
```
> شرط: إذا كانت حالة التحميل (isLoading) صحيحة فيُفتح نطاق التنفيذ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:217]

```
218:                     CircularProgressIndicator(
```
> يُستدعى مؤشر التقدّم الدائري (CircularProgressIndicator) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:218]

```
219:                         modifier = Modifier.size(16.dp),
```
> يُضبط المُعدِّل (modifier) على حجم (size) قدره ١٦ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:219]

```
220:                         strokeWidth = 2.dp,
```
> يُضبط عرض الخط (strokeWidth) على ٢ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:220]

```
221:                         color = colorScheme.onPrimary
```
> يُضبط اللون (color) على لون ما فوق الأساسي (colorScheme.onPrimary) من نظام الألوان. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:221]

```
222:                     )
```
> إغلاق قائمة مُعاملات مؤشر التقدّم الدائري. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:222]

```
223:                     Spacer(modifier = Modifier.width(8.dp))
```
> يُستدعى الفاصل (Spacer) مع مُعدِّل (modifier) يضبط العرض (width) على ٨ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:223]

```
224:                 }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:224]

```
225:                     Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:225]

```
226:                         text = stringResource(R.string.disable_battery_optimization),
```
> يُضبط مُعامل النص (text) على المورد النصي (stringResource) المعرّف بـ R.string.disable_battery_optimization. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:226]

```
227:                     style = MaterialTheme.typography.bodyMedium.copy(
```
> يُضبط النمط (style) على نسخة (copy) من نمط النص المتوسط (typography.bodyMedium) من سمة المواد (MaterialTheme) مع فتح قائمة التعديلات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:227]

```
228:                         fontFamily = FontFamily.Monospace,
```
> يُضبط عائلة الخط (fontFamily) على الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:228]

```
229:                         fontWeight = FontWeight.Bold
```
> يُضبط وزن الخط (fontWeight) على العريض (FontWeight.Bold). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:229]

```
230:                     )
```
> إغلاق قائمة تعديلات النسخة (copy) للنمط. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:230]

```
231:                 )
```
> إغلاق قائمة مُعاملات مكوّن النص. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:231]

```
232:             }
```
> إغلاق نطاق محتوى الزر. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:232]

```
233:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:233]

```
234:             Row(
```
> يُستدعى مكوّن الصف (Row) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:234]

```
235:                 modifier = Modifier.fillMaxWidth(),
```
> يُضبط المُعدِّل (modifier) على ملء العرض الأقصى (fillMaxWidth). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:235]

```
236:                 horizontalArrangement = Arrangement.spacedBy(12.dp)
```
> يُضبط التنظيم الأفقي (horizontalArrangement) على ترتيب متباعد (Arrangement.spacedBy) بمقدار ١٢ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:236]

```
237:             ) {
```
> إغلاق قائمة مُعاملات الصف وفتح نطاق محتواه اللمسي (lambda). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:237]

```
238:                 OutlinedButton(
```
> يُستدعى الزر المُحدَّد بإطار (OutlinedButton) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:238]

```
239:                     onClick = onRetry,
```
> يُضبط مُعامل النقر (onClick) على الدالة الواردة لإعادة المحاولة (onRetry). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:239]

```
240:                     modifier = Modifier.weight(1f),
```
> يُضبط المُعدِّل (modifier) على وزن (weight) قدره ١ من نوع عشري. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:240]

```
241:                     enabled = !isLoading
```
> يُضبط مُعامل التمكين (enabled) على نفي حالة التحميل (isLoading). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:241]

```
242:                 ) {
```
> إغلاق قائمة مُعاملات الزر المُحدَّد بإطار وفتح نطاق محتواه اللمسي (lambda). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:242]

```
243:                         Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:243]

```
244:                             text = stringResource(R.string.check_again),
```
> يُضبط مُعامل النص (text) على المورد النصي (stringResource) المعرّف بـ R.string.check_again. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:244]

```
245:                         style = MaterialTheme.typography.bodyMedium.copy(
```
> يُضبط النمط (style) على نسخة (copy) من نمط النص المتوسط (typography.bodyMedium) من سمة المواد (MaterialTheme) مع فتح قائمة التعديلات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:245]

```
246:                             fontFamily = FontFamily.Monospace
```
> يُضبط عائلة الخط (fontFamily) على الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:246]

```
247:                         )
```
> إغلاق قائمة تعديلات النسخة (copy) للنمط. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:247]

```
248:                     )
```
> إغلاق قائمة مُعاملات مكوّن النص. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:248]

```
249:                 }
```
> إغلاق نطاق محتوى الزر المُحدَّد بإطار. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:249]

```
250:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:250]

```
251:                 TextButton(
```
> يُستدعى الزر النصي (TextButton) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:251]

```
252:                     onClick = {
```
> يُضبط مُعامل النقر (onClick) على نطاق لمسي (lambda) مفتوح. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:252]

```
253:                         BatteryOptimizationPreferenceManager.setSkipped(context, true)
```
> يُستدعى تعيين حالة التخطّي (setSkipped) من مدير تفضيلات تحسين البطارية (BatteryOptimizationPreferenceManager) مع تمرير السياق (context) والقيمة صحيح (true). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:253]

```
254:                         onSkip()
```
> تُستدعى الدالة الواردة للتخطّي (onSkip) بلا مُعاملات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:254]

```
255:                     },
```
> إغلاق نطاق دالة النقر اللمسي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:255]

```
256:                     modifier = Modifier.weight(1f),
```
> يُضبط المُعدِّل (modifier) على وزن (weight) قدره ١ من نوع عشري. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:256]

```
257:                     enabled = !isLoading
```
> يُضبط مُعامل التمكين (enabled) على نفي حالة التحميل (isLoading). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:257]

```
258:                 ) {
```
> إغلاق قائمة مُعاملات الزر النصي وفتح نطاق محتواه اللمسي (lambda). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:258]

```
259:                         Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:259]

```
260:                             text = stringResource(R.string.battery_optimization_skip),
```
> يُضبط مُعامل النص (text) على المورد النصي (stringResource) المعرّف بـ R.string.battery_optimization_skip. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:260]

```
261:                         style = MaterialTheme.typography.bodyMedium.copy(
```
> يُضبط النمط (style) على نسخة (copy) من نمط النص المتوسط (typography.bodyMedium) من سمة المواد (MaterialTheme) مع فتح قائمة التعديلات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:261]

```
262:                             fontFamily = FontFamily.Monospace
```
> يُضبط عائلة الخط (fontFamily) على الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:262]

```
263:                         )
```
> إغلاق قائمة تعديلات النسخة (copy) للنمط. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:263]

```
264:                     )
```
> إغلاق قائمة مُعاملات مكوّن النص. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:264]

```
265:                 }
```
> إغلاق نطاق محتوى الزر النصي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:265]

```
266:             }
```
> إغلاق نطاق محتوى الصف. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:266]

```
267:         }
```
> إغلاق نطاق محتوى العمود. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:267]

```
268:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:268]

```
269: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:269]

```
270: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:270]

```
271: @Composable
```
> توضيح (annotation) يصف الدالة بأنها قابلة للتركيب (Composable). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:271]

```
272: private fun BatteryOptimizationCheckingContent(
```
> تُعرَّف دالة خاصة (private fun) باسم محتوى فحص تحسين البطارية (BatteryOptimizationCheckingContent) مع فتح قائمة مُعاملاتها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:272]

```
273:     colorScheme: ColorScheme
```
> يُعرَّف المُعامل نظام الألوان (colorScheme) من نوع نظام الألوان (ColorScheme). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:273]

```
274: ) {
```
> إغلاق قائمة مُعاملات الدالة وفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:274]

```
275:     Column(
```
> يُستدعى مكوّن العمود (Column) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:275]

```
276:         verticalArrangement = Arrangement.spacedBy(24.dp),
```
> يُضبط التنظيم الرأسي (verticalArrangement) على ترتيب متباعد (Arrangement.spacedBy) بمقدار ٢٤ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:276]

```
277:         horizontalAlignment = Alignment.CenterHorizontally
```
> يُضبط المحاذاة الأفقية (horizontalAlignment) على التوسيط الأفقي (Alignment.CenterHorizontally). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:277]

```
278:     ) {
```
> إغلاق قائمة مُعاملات العمود وفتح نطاق محتواه اللمسي (lambda). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:278]

```
279:         // Header Section - matching AboutSheet style
```
> تعليق: قسم الترويسة - مطابق لنمط ورقة "حول" (AboutSheet). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:279]

```
280:         Column(
```
> يُستدعى مكوّن العمود (Column) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:280]

```
281:             verticalArrangement = Arrangement.spacedBy(8.dp),
```
> يُضبط التنظيم الرأسي (verticalArrangement) على ترتيب متباعد (Arrangement.spacedBy) بمقدار ٨ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:281]

```
282:             horizontalAlignment = Alignment.CenterHorizontally
```
> يُضبط المحاذاة الأفقية (horizontalAlignment) على التوسيط الأفقي (Alignment.CenterHorizontally). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:282]

```
283:         ) {
```
> إغلاق قائمة مُعاملات العمود وفتح نطاق محتواه اللمسي (lambda). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:283]

```
284:             Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:284]

```
285:                 text = stringResource(R.string.app_name),
```
> يُضبط مُعامل النص (text) على المورد النصي (stringResource) المعرّف بـ R.string.app_name. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:285]

```
286:                 style = MaterialTheme.typography.headlineLarge.copy(
```
> يُضبط النمط (style) على نسخة (copy) من نمط العنوان الكبير (typography.headlineLarge) من سمة المواد (MaterialTheme) مع فتح قائمة التعديلات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:286]

```
287:                     fontFamily = FontFamily.Monospace,
```
> يُضبط عائلة الخط (fontFamily) على الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:287]

```
288:                     fontWeight = FontWeight.Bold,
```
> يُضبط وزن الخط (fontWeight) على العريض (FontWeight.Bold). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:288]

```
289:                     fontSize = 32.sp
```
> يُضبط حجم الخط (fontSize) على ٣٢ بكسل قابل للتحجيم (sp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:289]

```
290:                 ),
```
> إغلاق قائمة تعديلات النسخة (copy) للنمط. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:290]

```
291:                 color = colorScheme.onBackground
```
> يُضبط اللون (color) على لون ما فوق الخلفية (colorScheme.onBackground) من نظام الألوان. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:291]

```
292:             )
```
> إغلاق قائمة مُعاملات مكوّن النص. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:292]

```
293: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:293]

```
294:                 Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:294]

```
295:                     text = stringResource(R.string.battery_optimization_disabled_title),
```
> يُضبط مُعامل النص (text) على المورد النصي (stringResource) المعرّف بـ R.string.battery_optimization_disabled_title. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:295]

```
296:                 fontSize = 12.sp,
```
> يُضبط حجم الخط (fontSize) على ١٢ بكسل قابل للتحجيم (sp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:296]

```
297:                 fontFamily = FontFamily.Monospace,
```
> يُضبط عائلة الخط (fontFamily) على الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:297]

```
298:                 color = colorScheme.onBackground.copy(alpha = 0.7f)
```
> يُضبط اللون (color) على نسخة (copy) من لون ما فوق الخلفية (colorScheme.onBackground) بشفافية (alpha) قدرها ٠٫٧ عشري. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:298]

```
299:             )
```
> إغلاق قائمة مُعاملات مكوّن النص. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:299]

```
300:         }
```
> إغلاق نطاق محتوى العمود الداخلي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:300]

```
301:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:301]

```
302:         val infiniteTransition = rememberInfiniteTransition(label = "rotation")
```
> يُعرَّف متغيّر ثابت (val) باسم الانتقال اللانهائي (infiniteTransition) بقيمة استدعاء تذكّر الانتقال اللانهائي (rememberInfiniteTransition) مع مُعامل اللصيقة (label) بالقيمة "rotation". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:302]

```
303:         val rotation by infiniteTransition.animateFloat(
```
> يُعرَّف متغيّر ثابت (val) باسم الدوران (rotation) بالتفويض (by) إلى تحريك عشري (animateFloat) من الانتقال اللانهائي مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:303]

```
304:             initialValue = 0f,
```
> يُضبط القيمة الابتدائية (initialValue) على ٠ عشري. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:304]

```
305:             targetValue = 360f,
```
> يُضبط القيمة الهدف (targetValue) على ٣٦٠ عشري. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:305]

```
306:             animationSpec = infiniteRepeatable(
```
> يُضبط مواصفة التحريك (animationSpec) على تكرار لانهائي (infiniteRepeatable) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:306]

```
307:                 animation = tween(2000, easing = LinearEasing),
```
> يُضبط التحريك (animation) على دالة الانتقال (tween) بمدة ٢٠٠٠ وبتنعيم (easing) خطّي (LinearEasing). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:307]

```
308:                 repeatMode = RepeatMode.Restart
```
> يُضبط وضع التكرار (repeatMode) على إعادة البدء (RepeatMode.Restart). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:308]

```
309:             ),
```
> إغلاق قائمة مُعاملات التكرار اللانهائي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:309]

```
310:             label = "rotation"
```
> يُضبط مُعامل اللصيقة (label) على القيمة "rotation". [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:310]

```
311:         )
```
> إغلاق قائمة مُعاملات التحريك العشري. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:311]

```
312:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:312]

```
313:         Icon(
```
> يُستدعى مكوّن الأيقونة (Icon) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:313]

```
314:             imageVector = Icons.Filled.BatteryStd,
```
> يُضبط متّجه الصورة (imageVector) على أيقونة البطارية القياسية الممتلئة (Icons.Filled.BatteryStd). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:314]

```
315:             contentDescription = stringResource(R.string.cd_checking_battery_optimization),
```
> يُضبط وصف المحتوى (contentDescription) على المورد النصي (stringResource) المعرّف بـ R.string.cd_checking_battery_optimization. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:315]

```
316:             modifier = Modifier
```
> يُضبط المُعدِّل (modifier) على الكائن المُعدِّل (Modifier) مع بدء سلسلة استدعاءات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:316]

```
317:                 .size(64.dp)
```
> يُطبّق الحجم (size) قدره ٦٤ بكسل مستقل الكثافة (dp) على المُعدِّل. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:317]

```
318:                 .rotate(rotation),
```
> يُطبّق الدوران (rotate) بقيمة متغيّر الدوران (rotation) على المُعدِّل. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:318]

```
319:             tint = colorScheme.primary
```
> يُضبط لون التلوين (tint) على اللون الأساسي (colorScheme.primary) من نظام الألوان. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:319]

```
320:         )
```
> إغلاق قائمة مُعاملات الأيقونة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:320]

```
321:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:321]

```
322:             Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:322]

```
323:                 text = stringResource(R.string.battery_optimization_success_message),
```
> يُضبط مُعامل النص (text) على المورد النصي (stringResource) المعرّف بـ R.string.battery_optimization_success_message. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:323]

```
324:             style = MaterialTheme.typography.bodyMedium.copy(
```
> يُضبط النمط (style) على نسخة (copy) من نمط النص المتوسط (typography.bodyMedium) من سمة المواد (MaterialTheme) مع فتح قائمة التعديلات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:324]

```
325:                 fontFamily = FontFamily.Monospace,
```
> يُضبط عائلة الخط (fontFamily) على الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:325]

```
326:                 color = colorScheme.onBackground.copy(alpha = 0.8f)
```
> يُضبط اللون (color) على نسخة (copy) من لون ما فوق الخلفية (colorScheme.onBackground) بشفافية (alpha) قدرها ٠٫٨ عشري. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:326]

```
327:             ),
```
> إغلاق قائمة تعديلات النسخة (copy) للنمط. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:327]

```
328:             textAlign = TextAlign.Center
```
> يُضبط محاذاة النص (textAlign) على التوسيط (TextAlign.Center). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:328]

```
329:         )
```
> إغلاق قائمة مُعاملات مكوّن النص. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:329]

```
330:     }
```
> إغلاق نطاق محتوى العمود الخارجي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:330]

```
331: }
```
> إغلاق نطاق جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:331]

```
332: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:332]

```
333: @Composable
```
> توضيح (annotation) يصف الدالة بأنها قابلة للتركيب (Composable). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:333]

```
334: private fun BatteryOptimizationNotSupportedContent(
```
> تُعرَّف دالة خاصة (private fun) باسم محتوى عدم دعم تحسين البطارية (BatteryOptimizationNotSupportedContent) مع فتح قائمة مُعاملاتها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:334]

```
335:     onRetry: () -> Unit,
```
> يُعرَّف المُعامل إعادة المحاولة (onRetry) من نوع دالة بلا مُعاملات تُعيد الوحدة (Unit). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:335]

```
336:     colorScheme: ColorScheme
```
> يُعرَّف المُعامل نظام الألوان (colorScheme) من نوع نظام الألوان (ColorScheme). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:336]

```
337: ) {
```
> إغلاق قائمة مُعاملات الدالة وفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:337]

```
338:     Column(
```
> يُستدعى مكوّن العمود (Column) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:338]

```
339:         verticalArrangement = Arrangement.spacedBy(24.dp),
```
> يُضبط التنظيم الرأسي (verticalArrangement) على ترتيب متباعد (Arrangement.spacedBy) بمقدار ٢٤ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:339]

```
340:         horizontalAlignment = Alignment.CenterHorizontally
```
> يُضبط المحاذاة الأفقية (horizontalAlignment) على التوسيط الأفقي (Alignment.CenterHorizontally). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:340]

```
341:     ) {
```
> إغلاق قائمة مُعاملات العمود وفتح نطاق محتواه اللمسي (lambda). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:341]

```
342:         // Header Section - matching AboutSheet style
```
> تعليق: قسم الترويسة - مطابق لنمط ورقة "حول" (AboutSheet). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:342]

```
343:         Column(
```
> يُستدعى مكوّن العمود (Column) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:343]

```
344:             verticalArrangement = Arrangement.spacedBy(8.dp),
```
> يُضبط التنظيم الرأسي (verticalArrangement) على ترتيب متباعد (Arrangement.spacedBy) بمقدار ٨ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:344]

```
345:             horizontalAlignment = Alignment.CenterHorizontally
```
> يُضبط المحاذاة الأفقية (horizontalAlignment) على التوسيط الأفقي (Alignment.CenterHorizontally). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:345]

```
346:         ) {
```
> إغلاق قائمة مُعاملات العمود وفتح نطاق محتواه اللمسي (lambda). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:346]

```
347:             Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:347]

```
348:                 text = stringResource(R.string.app_name),
```
> يُضبط مُعامل النص (text) على المورد النصي (stringResource) المعرّف بـ R.string.app_name. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:348]

```
349:                 style = MaterialTheme.typography.headlineLarge.copy(
```
> يُضبط النمط (style) على نسخة (copy) من نمط العنوان الكبير (typography.headlineLarge) من سمة المواد (MaterialTheme) مع فتح قائمة التعديلات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:349]

```
350:                     fontFamily = FontFamily.Monospace,
```
> يُضبط عائلة الخط (fontFamily) على الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:350]

```
351:                     fontWeight = FontWeight.Bold,
```
> يُضبط وزن الخط (fontWeight) على العريض (FontWeight.Bold). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:351]

```
352:                     fontSize = 32.sp
```
> يُضبط حجم الخط (fontSize) على ٣٢ بكسل قابل للتحجيم (sp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:352]

```
353:                 ),
```
> إغلاق قائمة تعديلات النسخة (copy) للنمط. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:353]

```
354:                 color = colorScheme.onBackground
```
> يُضبط اللون (color) على لون ما فوق الخلفية (colorScheme.onBackground) من نظام الألوان. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:354]

```
355:             )
```
> إغلاق قائمة مُعاملات مكوّن النص. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:355]

```
356: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:356]

```
357:             Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:357]

```
358:                 text = stringResource(R.string.battery_optimization_not_required),
```
> يُضبط مُعامل النص (text) على المورد النصي (stringResource) المعرّف بـ R.string.battery_optimization_not_required. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:358]

```
359:                 fontSize = 12.sp,
```
> يُضبط حجم الخط (fontSize) على ١٢ بكسل قابل للتحجيم (sp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:359]

```
360:                 fontFamily = FontFamily.Monospace,
```
> يُضبط عائلة الخط (fontFamily) على الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:360]

```
361:                 color = colorScheme.onBackground.copy(alpha = 0.7f)
```
> يُضبط اللون (color) على نسخة (copy) من لون ما فوق الخلفية (colorScheme.onBackground) بشفافية (alpha) قدرها ٠٫٧ عشري. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:361]

```
362:             )
```
> إغلاق قائمة مُعاملات مكوّن النص. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:362]

```
363:         }
```
> إغلاق نطاق محتوى العمود الداخلي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:363]

```
364:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:364]

```
365:         Icon(
```
> يُستدعى مكوّن الأيقونة (Icon) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:365]

```
366:             imageVector = Icons.Filled.CheckCircle,
```
> يُضبط متّجه الصورة (imageVector) على أيقونة دائرة الاختيار الممتلئة (Icons.Filled.CheckCircle). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:366]

```
367:             contentDescription = stringResource(R.string.cd_not_supported_battery_optimization),
```
> يُضبط وصف المحتوى (contentDescription) على المورد النصي (stringResource) المعرّف بـ R.string.cd_not_supported_battery_optimization. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:367]

```
368:             modifier = Modifier.size(64.dp),
```
> يُضبط المُعدِّل (modifier) على حجم (size) قدره ٦٤ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:368]

```
369:             tint = colorScheme.primary
```
> يُضبط لون التلوين (tint) على اللون الأساسي (colorScheme.primary) من نظام الألوان. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:369]

```
370:         )
```
> إغلاق قائمة مُعاملات الأيقونة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:370]

```
371:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:371]

```
372:         Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:372]

```
373:             text = stringResource(R.string.battery_optimization_not_supported_message),
```
> يُضبط مُعامل النص (text) على المورد النصي (stringResource) المعرّف بـ R.string.battery_optimization_not_supported_message. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:373]

```
374:             style = MaterialTheme.typography.bodyMedium.copy(
```
> يُضبط النمط (style) على نسخة (copy) من نمط النص المتوسط (typography.bodyMedium) من سمة المواد (MaterialTheme) مع فتح قائمة التعديلات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:374]

```
375:                 fontFamily = FontFamily.Monospace,
```
> يُضبط عائلة الخط (fontFamily) على الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:375]

```
376:                 color = colorScheme.onBackground.copy(alpha = 0.8f)
```
> يُضبط اللون (color) على نسخة (copy) من لون ما فوق الخلفية (colorScheme.onBackground) بشفافية (alpha) قدرها ٠٫٨ عشري. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:376]

```
377:             ),
```
> إغلاق قائمة تعديلات النسخة (copy) للنمط. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:377]

```
378:             textAlign = TextAlign.Center
```
> يُضبط محاذاة النص (textAlign) على التوسيط (TextAlign.Center). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:378]

```
379:         )
```
> إغلاق قائمة مُعاملات مكوّن النص. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:379]

```
380:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:380]

```
381:         Button(
```
> يُستدعى مكوّن الزر (Button) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:381]

```
382:             onClick = onRetry,
```
> يُضبط مُعامل النقر (onClick) على الدالة الواردة لإعادة المحاولة (onRetry). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:382]

```
383:             modifier = Modifier.fillMaxWidth(),
```
> يُضبط المُعدِّل (modifier) على ملء العرض الأقصى (fillMaxWidth). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:383]

```
384:             colors = ButtonDefaults.buttonColors(
```
> يُضبط مُعامل الألوان (colors) باستدعاء ألوان الزر الافتراضية (ButtonDefaults.buttonColors) مع فتح قائمة مُعاملاتها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:384]

```
385:                 containerColor = colorScheme.primary
```
> يُضبط لون الحاوية (containerColor) على اللون الأساسي (colorScheme.primary) من نظام الألوان. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:385]

```
386:             )
```
> إغلاق قائمة مُعاملات ألوان الزر. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:386]

```
387:         ) {
```
> إغلاق قائمة مُعاملات الزر وفتح نطاق محتواه اللمسي (lambda). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:387]

```
388:                 Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:388]

```
389:                     text = stringResource(R.string.continue_btn),
```
> يُضبط مُعامل النص (text) على المورد النصي (stringResource) المعرّف بـ R.string.continue_btn. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:389]

```
390:                 style = MaterialTheme.typography.bodyMedium.copy(
```
> يُضبط النمط (style) على نسخة (copy) من نمط النص المتوسط (typography.bodyMedium) من سمة المواد (MaterialTheme) مع فتح قائمة التعديلات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:390]

```
391:                     fontFamily = FontFamily.Monospace,
```
> يُضبط عائلة الخط (fontFamily) على الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:391]

```
392:                     fontWeight = FontWeight.Bold
```
> يُضبط وزن الخط (fontWeight) على العريض (FontWeight.Bold). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:392]

```
393:                 )
```
> إغلاق قائمة تعديلات النسخة (copy) للنمط. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:393]

```
394:             )
```
> إغلاق قائمة مُعاملات مكوّن النص. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:394]

```
395:         }
```
> إغلاق نطاق محتوى الزر. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:395]

```
396:     }
```
> إغلاق نطاق محتوى العمود الخارجي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:396]

```
397: }
```
> إغلاق نطاق جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:397]
