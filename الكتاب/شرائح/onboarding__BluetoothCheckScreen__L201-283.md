# شريحة — app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt (الأسطر 201–283)

```
201:             ),
```
> إغلاق نطاق لمعاملات استدعاء، يلي قوس الإغلاق فاصلة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:201]

```
202:             elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
```
> يُضبَط معامل الارتفاع (elevation) بقيمة ناتجة عن استدعاء ارتفاع البطاقة (CardDefaults.cardElevation) مع ضبط الارتفاع الافتراضي (defaultElevation) على ٢ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:202]

```
203:         ) {
```
> إغلاق قائمة معاملات الاستدعاء بقوس، يلي ذلك قوس معقوف يفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:203]

```
204:             Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:204]

```
205:                 text = stringResource(R.string.bluetooth_unsupported_explanation),
```
> يُضبَط معامل النص (text) بقيمة مصدر نصّي (stringResource) للمعرّف R.string.bluetooth_unsupported_explanation. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:205]

```
206:                 style = MaterialTheme.typography.bodyMedium.copy(
```
> يُضبَط معامل النمط (style) بنسخة معدّلة (copy) من نمط النص المتوسط (bodyMedium) لطباعة سمة ماتيريال (MaterialTheme.typography). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:206]

```
207:                     fontFamily = FontFamily.Monospace,
```
> يُضبَط معامل عائلة الخط (fontFamily) بقيمة الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:207]

```
208:                     color = colorScheme.onSurface
```
> يُضبَط معامل اللون (color) بقيمة لون «على السطح» (onSurface) من نظام الألوان (colorScheme). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:208]

```
209:                 ),
```
> إغلاق نطاق استدعاء النسخ (copy)، يلي قوس الإغلاق فاصلة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:209]

```
210:                 modifier = Modifier.padding(16.dp),
```
> يُضبَط معامل المُعدِّل (modifier) بقيمة مُعدِّل (Modifier) مع حشوة (padding) قدرها ١٦ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:210]

```
211:                 textAlign = TextAlign.Center
```
> يُضبَط معامل محاذاة النص (textAlign) بقيمة المحاذاة إلى الوسط (TextAlign.Center). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:211]

```
212:             )
```
> إغلاق نطاق معاملات استدعاء مكوّن النص (Text) بقوس. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:212]

```
213:         }
```
> إغلاق نطاق كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:213]

```
214: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:214]

```
215:         Button(
```
> يُستدعى مكوّن الزر (Button) مع فتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:215]

```
216:             onClick = onSkip,
```
> يُضبَط معامل عند النقر (onClick) بقيمة دالة التخطّي (onSkip). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:216]

```
217:             modifier = Modifier.fillMaxWidth(),
```
> يُضبَط معامل المُعدِّل (modifier) بقيمة مُعدِّل (Modifier) مع ملء العرض الأقصى (fillMaxWidth). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:217]

```
218:             colors = ButtonDefaults.buttonColors(
```
> يُضبَط معامل الألوان (colors) بقيمة ناتجة عن استدعاء ألوان الزر (ButtonDefaults.buttonColors) مع فتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:218]

```
219:                 containerColor = colorScheme.secondary
```
> يُضبَط معامل لون الحاوية (containerColor) بقيمة اللون الثانوي (secondary) من نظام الألوان (colorScheme). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:219]

```
220:             )
```
> إغلاق نطاق معاملات استدعاء ألوان الزر (buttonColors) بقوس. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:220]

```
221:         ) {
```
> إغلاق قائمة معاملات استدعاء الزر بقوس، يلي ذلك قوس معقوف يفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:221]

```
222:             Text(text = stringResource(R.string.continue_btn))
```
> يُستدعى مكوّن النص (Text) مع ضبط معامل النص (text) بقيمة مصدر نصّي (stringResource) للمعرّف R.string.continue_btn. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:222]

```
223:         }
```
> إغلاق نطاق كتلة محتوى الزر. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:223]

```
224:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:224]

```
225: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:225]

```
226: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:226]

```
227: @Composable
```
> توسيم بمُحدِّد قابل للتركيب (Composable@) للدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:227]

```
228: private fun BluetoothCheckingContent(
```
> تُعرَّف دالة خاصة (private) باسم محتوى فحص البلوتوث (BluetoothCheckingContent) مع فتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:228]

```
229:     colorScheme: ColorScheme
```
> يُعرَّف معامل نظام الألوان (colorScheme) من نوع نظام الألوان (ColorScheme). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:229]

```
230: ) {
```
> إغلاق قائمة معاملات الدالة بقوس، يلي ذلك قوس معقوف يفتح جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:230]

```
231:     Column(
```
> يُستدعى مكوّن العمود (Column) مع فتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:231]

```
232:         verticalArrangement = Arrangement.spacedBy(32.dp),
```
> يُضبَط معامل الترتيب العمودي (verticalArrangement) بقيمة ترتيب متباعد (Arrangement.spacedBy) بمسافة ٣٢ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:232]

```
233:         horizontalAlignment = Alignment.CenterHorizontally
```
> يُضبَط معامل المحاذاة الأفقية (horizontalAlignment) بقيمة التوسيط الأفقي (Alignment.CenterHorizontally). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:233]

```
234:     ) {
```
> إغلاق قائمة معاملات استدعاء العمود بقوس، يلي ذلك قوس معقوف يفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:234]

```
235:         Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:235]

```
236:             text = stringResource(R.string.app_name),
```
> يُضبَط معامل النص (text) بقيمة مصدر نصّي (stringResource) للمعرّف R.string.app_name. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:236]

```
237:             style = MaterialTheme.typography.headlineLarge.copy(
```
> يُضبَط معامل النمط (style) بنسخة معدّلة (copy) من نمط العنوان الكبير (headlineLarge) لطباعة سمة ماتيريال (MaterialTheme.typography). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:237]

```
238:                 fontFamily = FontFamily.Monospace,
```
> يُضبَط معامل عائلة الخط (fontFamily) بقيمة الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:238]

```
239:                 fontWeight = FontWeight.Bold,
```
> يُضبَط معامل وزن الخط (fontWeight) بقيمة الوزن العريض (FontWeight.Bold). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:239]

```
240:                 color = colorScheme.primary
```
> يُضبَط معامل اللون (color) بقيمة اللون الأساسي (primary) من نظام الألوان (colorScheme). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:240]

```
241:             ),
```
> إغلاق نطاق استدعاء النسخ (copy)، يلي قوس الإغلاق فاصلة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:241]

```
242:             textAlign = TextAlign.Center
```
> يُضبَط معامل محاذاة النص (textAlign) بقيمة المحاذاة إلى الوسط (TextAlign.Center). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:242]

```
243:         )
```
> إغلاق نطاق معاملات استدعاء مكوّن النص (Text) بقوس. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:243]

```
244: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:244]

```
245:         BluetoothLoadingIndicator()
```
> يُستدعى مؤشّر تحميل البلوتوث (BluetoothLoadingIndicator) دون وسائط. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:245]

```
246: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:246]

```
247:         Text(
```
> يُستدعى مكوّن النص (Text) مع فتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:247]

```
248:             text = stringResource(R.string.checking_bluetooth_status),
```
> يُضبَط معامل النص (text) بقيمة مصدر نصّي (stringResource) للمعرّف R.string.checking_bluetooth_status. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:248]

```
249:             style = MaterialTheme.typography.bodyLarge.copy(
```
> يُضبَط معامل النمط (style) بنسخة معدّلة (copy) من نمط النص الكبير (bodyLarge) لطباعة سمة ماتيريال (MaterialTheme.typography). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:249]

```
250:                 fontFamily = FontFamily.Monospace,
```
> يُضبَط معامل عائلة الخط (fontFamily) بقيمة الخط أحادي المسافة (FontFamily.Monospace). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:250]

```
251:                 color = colorScheme.onSurface.copy(alpha = 0.7f)
```
> يُضبَط معامل اللون (color) بنسخة (copy) من لون «على السطح» (onSurface) من نظام الألوان (colorScheme) مع ضبط الشفافية (alpha) على ٠٫٧. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:251]

```
252:             )
```
> إغلاق نطاق معاملات استدعاء النسخ (copy) بقوس. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:252]

```
253:         )
```
> إغلاق نطاق معاملات استدعاء مكوّن النص (Text) بقوس. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:253]

```
254:     }
```
> إغلاق نطاق كتلة محتوى العمود. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:254]

```
255: }
```
> إغلاق نطاق جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:255]

```
256: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:256]

```
257: @Composable
```
> توسيم بمُحدِّد قابل للتركيب (Composable@) للدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:257]

```
258: private fun BluetoothLoadingIndicator() {
```
> تُعرَّف دالة خاصة (private) باسم مؤشّر تحميل البلوتوث (BluetoothLoadingIndicator) بلا معاملات، يلي ذلك قوس معقوف يفتح جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:258]

```
259:     // Animated rotation for the loading indicator
```
> تعليق: دوران متحرّك لمؤشّر التحميل. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:259]

```
260:     val infiniteTransition = rememberInfiniteTransition(label = "bluetooth_loading")
```
> يُعرَّف ثابت الانتقال اللانهائي (infiniteTransition) بقيمة ناتجة عن تذكّر انتقال لانهائي (rememberInfiniteTransition) مع ضبط الوسم (label) على "bluetooth_loading". [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:260]

```
261:     val rotationAngle by infiniteTransition.animateFloat(
```
> يُعرَّف ثابت زاوية الدوران (rotationAngle) بتفويض (by) قيمته إلى تحريك عدد عشري (animateFloat) من الانتقال اللانهائي (infiniteTransition) مع فتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:261]

```
262:         initialValue = 0f,
```
> يُضبَط معامل القيمة الابتدائية (initialValue) بقيمة ٠ عشري. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:262]

```
263:         targetValue = 360f,
```
> يُضبَط معامل القيمة الهدف (targetValue) بقيمة ٣٦٠ عشري. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:263]

```
264:         animationSpec = infiniteRepeatable(
```
> يُضبَط معامل مواصفة التحريك (animationSpec) بقيمة ناتجة عن تكرار لانهائي (infiniteRepeatable) مع فتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:264]

```
265:             animation = tween(durationMillis = 2000, easing = LinearEasing),
```
> يُضبَط معامل التحريك (animation) بقيمة تدرّج (tween) مع ضبط مدّة بالمللي ثانية (durationMillis) على ٢٠٠٠ والتخفيف (easing) على التخفيف الخطّي (LinearEasing). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:265]

```
266:             repeatMode = RepeatMode.Restart
```
> يُضبَط معامل وضع التكرار (repeatMode) بقيمة إعادة البدء (RepeatMode.Restart). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:266]

```
267:         ),
```
> إغلاق نطاق معاملات التكرار اللانهائي (infiniteRepeatable)، يلي قوس الإغلاق فاصلة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:267]

```
268:         label = "rotation"
```
> يُضبَط معامل الوسم (label) بقيمة "rotation". [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:268]

```
269:     )
```
> إغلاق نطاق معاملات استدعاء تحريك العدد العشري (animateFloat) بقوس. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:269]

```
270: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:270]

```
271:     Box(
```
> يُستدعى مكوّن الصندوق (Box) مع فتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:271]

```
272:         modifier = Modifier.size(60.dp),
```
> يُضبَط معامل المُعدِّل (modifier) بقيمة مُعدِّل (Modifier) مع ضبط الحجم (size) على ٦٠ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:272]

```
273:         contentAlignment = Alignment.Center
```
> يُضبَط معامل محاذاة المحتوى (contentAlignment) بقيمة التوسيط (Alignment.Center). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:273]

```
274:     ) {
```
> إغلاق قائمة معاملات استدعاء الصندوق بقوس، يلي ذلك قوس معقوف يفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:274]

```
275:         CircularProgressIndicator(
```
> يُستدعى مكوّن مؤشّر التقدّم الدائري (CircularProgressIndicator) مع فتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:275]

```
276:             modifier = Modifier
```
> يُضبَط معامل المُعدِّل (modifier) بقيمة مُعدِّل (Modifier) يتبعه سلسلة استدعاءات. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:276]

```
277:                 .fillMaxSize()
```
> يُستدعى ملء الحجم الأقصى (fillMaxSize) على المُعدِّل. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:277]

```
278:                 .rotate(rotationAngle),
```
> يُستدعى التدوير (rotate) على المُعدِّل بقيمة زاوية الدوران (rotationAngle)، يلي ذلك فاصلة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:278]

```
279:             color = Color(0xFF2196F3), // Bluetooth blue
```
> يُضبَط معامل اللون (color) بقيمة لون (Color) من القيمة السداسية العشرية 0xFF2196F3؛ تعليق: أزرق البلوتوث. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:279]

```
280:             strokeWidth = 3.dp
```
> يُضبَط معامل عرض الخط (strokeWidth) بقيمة ٣ بكسل مستقل الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:280]

```
281:         )
```
> إغلاق نطاق معاملات استدعاء مؤشّر التقدّم الدائري (CircularProgressIndicator) بقوس. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:281]

```
282:     }
```
> إغلاق نطاق كتلة محتوى الصندوق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:282]

```
283: }
```
> إغلاق نطاق جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:283]
