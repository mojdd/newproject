# شريحة — app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt (الأسطر 201–295)

```
201:         // Error icon
```
> تعليق: أيقونة الخطأ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:201]

```
202:         Icon(
```
> استدعاء مكوّن أيقونة (Icon) وفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:202]

```
203:             imageVector = Icons.Filled.ErrorOutline,
```
> يضبط الوسيط صورة-المتجه (imageVector) على الأيقونة Icons.Filled.ErrorOutline. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:203]

```
204:             contentDescription = stringResource(R.string.cd_error),
```
> يضبط الوسيط وصف-المحتوى (contentDescription) على نصّ المورد stringResource(R.string.cd_error). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:204]

```
205:             modifier = Modifier.size(64.dp),
```
> يضبط الوسيط المُعدِّل (modifier) على Modifier.size بقيمة 64.dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:205]

```
206:             tint = colorScheme.error
```
> يضبط الوسيط الصبغة (tint) على colorScheme.error. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:206]

```
207:         )
```
> إغلاق قائمة وُسطاء استدعاء الأيقونة. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:207]

```
208: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:208]

```
209:         Text(
```
> استدعاء مكوّن نصّ (Text) وفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:209]

```
210:             text = stringResource(R.string.location_services_unavailable),
```
> يضبط الوسيط النصّ (text) على نصّ المورد stringResource(R.string.location_services_unavailable). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:210]

```
211:             style = MaterialTheme.typography.headlineSmall.copy(
```
> يضبط الوسيط النمط (style) على MaterialTheme.typography.headlineSmall مع استدعاء النسخ copy وفتح وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:211]

```
212:                 fontFamily = FontFamily.Monospace,
```
> يضبط الوسيط عائلة-الخطّ (fontFamily) على FontFamily.Monospace. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:212]

```
213:                 fontWeight = FontWeight.Bold,
```
> يضبط الوسيط وزن-الخطّ (fontWeight) على FontWeight.Bold. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:213]

```
214:                 color = colorScheme.error
```
> يضبط الوسيط اللون (color) على colorScheme.error. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:214]

```
215:             ),
```
> إغلاق قائمة وُسطاء استدعاء النسخ copy. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:215]

```
216:             textAlign = TextAlign.Center
```
> يضبط الوسيط محاذاة-النصّ (textAlign) على TextAlign.Center. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:216]

```
217:         )
```
> إغلاق قائمة وُسطاء استدعاء النصّ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:217]

```
218: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:218]

```
219:         Card(
```
> استدعاء مكوّن البطاقة (Card) وفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:219]

```
220:             modifier = Modifier.fillMaxWidth(),
```
> يضبط الوسيط المُعدِّل (modifier) على Modifier.fillMaxWidth. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:220]

```
221:             colors = CardDefaults.cardColors(
```
> يضبط الوسيط الألوان (colors) على استدعاء CardDefaults.cardColors وفتح وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:221]

```
222:                 containerColor = colorScheme.errorContainer.copy(alpha = 0.1f)
```
> يضبط الوسيط لون-الحاوية (containerColor) على colorScheme.errorContainer مع استدعاء النسخ copy بضبط alpha على 0.1f. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:222]

```
223:             ),
```
> إغلاق قائمة وُسطاء استدعاء CardDefaults.cardColors. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:223]

```
224:             elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
```
> يضبط الوسيط الارتفاع (elevation) على استدعاء CardDefaults.cardElevation بضبط defaultElevation على 2.dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:224]

```
225:         ) {
```
> إغلاق قائمة وُسطاء استدعاء البطاقة وفتح كتلة المحتوى اللاحقة (lambda). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:225]

```
226:             Text(
```
> استدعاء مكوّن نصّ (Text) وفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:226]

```
227:                 text = stringResource(R.string.location_unavailable_explanation),
```
> يضبط الوسيط النصّ (text) على نصّ المورد stringResource(R.string.location_unavailable_explanation). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:227]

```
228:                 style = MaterialTheme.typography.bodyMedium.copy(
```
> يضبط الوسيط النمط (style) على MaterialTheme.typography.bodyMedium مع استدعاء النسخ copy وفتح وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:228]

```
229:                     fontFamily = FontFamily.Monospace,
```
> يضبط الوسيط عائلة-الخطّ (fontFamily) على FontFamily.Monospace. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:229]

```
230:                     color = colorScheme.onSurface
```
> يضبط الوسيط اللون (color) على colorScheme.onSurface. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:230]

```
231:                 ),
```
> إغلاق قائمة وُسطاء استدعاء النسخ copy. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:231]

```
232:                 modifier = Modifier.padding(16.dp),
```
> يضبط الوسيط المُعدِّل (modifier) على Modifier.padding بقيمة 16.dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:232]

```
233:                 textAlign = TextAlign.Center
```
> يضبط الوسيط محاذاة-النصّ (textAlign) على TextAlign.Center. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:233]

```
234:             )
```
> إغلاق قائمة وُسطاء استدعاء النصّ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:234]

```
235:         }
```
> إغلاق نطاق كتلة محتوى البطاقة. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:235]

```
236:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:236]

```
237: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:237]

```
238: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:238]

```
239: @Composable
```
> تعليق توضيحي (Composable@) يدلّ على أنّ الدالّة التالية دالّة تأليف واجهة. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:239]

```
240: private fun LocationCheckingContent(
```
> تعريف دالّة خاصّة (private) باسم محتوى-فحص-الموقع (LocationCheckingContent) وفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:240]

```
241:     colorScheme: ColorScheme
```
> يعرّف المعامل نظام-الألوان (colorScheme) من النوع ColorScheme. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:241]

```
242: ) {
```
> إغلاق قائمة المعاملات وفتح جسم الدالّة. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:242]

```
243:     Column(
```
> استدعاء مكوّن العمود (Column) وفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:243]

```
244:         verticalArrangement = Arrangement.spacedBy(32.dp),
```
> يضبط الوسيط الترتيب-الرأسي (verticalArrangement) على Arrangement.spacedBy بقيمة 32.dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:244]

```
245:         horizontalAlignment = Alignment.CenterHorizontally
```
> يضبط الوسيط المحاذاة-الأفقية (horizontalAlignment) على Alignment.CenterHorizontally. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:245]

```
246:     ) {
```
> إغلاق قائمة وُسطاء العمود وفتح كتلة محتواه اللاحقة (lambda). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:246]

```
247:         Text(
```
> استدعاء مكوّن نصّ (Text) وفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:247]

```
248:             text = stringResource(R.string.app_name),
```
> يضبط الوسيط النصّ (text) على نصّ المورد stringResource(R.string.app_name). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:248]

```
249:             style = MaterialTheme.typography.headlineLarge.copy(
```
> يضبط الوسيط النمط (style) على MaterialTheme.typography.headlineLarge مع استدعاء النسخ copy وفتح وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:249]

```
250:                 fontFamily = FontFamily.Monospace,
```
> يضبط الوسيط عائلة-الخطّ (fontFamily) على FontFamily.Monospace. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:250]

```
251:                 fontWeight = FontWeight.Bold,
```
> يضبط الوسيط وزن-الخطّ (fontWeight) على FontWeight.Bold. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:251]

```
252:                 color = colorScheme.primary
```
> يضبط الوسيط اللون (color) على colorScheme.primary. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:252]

```
253:             ),
```
> إغلاق قائمة وُسطاء استدعاء النسخ copy. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:253]

```
254:             textAlign = TextAlign.Center
```
> يضبط الوسيط محاذاة-النصّ (textAlign) على TextAlign.Center. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:254]

```
255:         )
```
> إغلاق قائمة وُسطاء استدعاء النصّ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:255]

```
256: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:256]

```
257:         LocationLoadingIndicator()
```
> استدعاء الدالّة مؤشّر-تحميل-الموقع (LocationLoadingIndicator) بلا وُسطاء. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:257]

```
258: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:258]

```
259:         Text(
```
> استدعاء مكوّن نصّ (Text) وفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:259]

```
260:             text = stringResource(R.string.checking_location_services),
```
> يضبط الوسيط النصّ (text) على نصّ المورد stringResource(R.string.checking_location_services). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:260]

```
261:             style = MaterialTheme.typography.bodyLarge.copy(
```
> يضبط الوسيط النمط (style) على MaterialTheme.typography.bodyLarge مع استدعاء النسخ copy وفتح وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:261]

```
262:                 fontFamily = FontFamily.Monospace,
```
> يضبط الوسيط عائلة-الخطّ (fontFamily) على FontFamily.Monospace. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:262]

```
263:                 color = colorScheme.onSurface.copy(alpha = 0.7f)
```
> يضبط الوسيط اللون (color) على colorScheme.onSurface مع استدعاء النسخ copy بضبط alpha على 0.7f. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:263]

```
264:             )
```
> إغلاق قائمة وُسطاء استدعاء النسخ copy. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:264]

```
265:         )
```
> إغلاق قائمة وُسطاء استدعاء النصّ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:265]

```
266:     }
```
> إغلاق نطاق كتلة محتوى العمود. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:266]

```
267: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:267]

```
268: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:268]

```
269: @Composable
```
> تعليق توضيحي (Composable@) يدلّ على أنّ الدالّة التالية دالّة تأليف واجهة. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:269]

```
270: private fun LocationLoadingIndicator() {
```
> تعريف دالّة خاصّة (private) باسم مؤشّر-تحميل-الموقع (LocationLoadingIndicator) بلا معاملات وفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:270]

```
271:     // Animated rotation for the loading indicator
```
> تعليق: دوران متحرّك لمؤشّر التحميل. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:271]

```
272:     val infiniteTransition = rememberInfiniteTransition(label = "location_loading")
```
> يعرّف ثابتاً باسم الانتقال-اللانهائي (infiniteTransition) قيمته نتيجة rememberInfiniteTransition بضبط label على "location_loading". [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:272]

```
273:     val rotationAngle by infiniteTransition.animateFloat(
```
> يعرّف ثابتاً باسم زاوية-الدوران (rotationAngle) عبر تفويض by إلى استدعاء infiniteTransition.animateFloat وفتح وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:273]

```
274:         initialValue = 0f,
```
> يضبط الوسيط القيمة-الابتدائية (initialValue) على 0f. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:274]

```
275:         targetValue = 360f,
```
> يضبط الوسيط القيمة-الهدف (targetValue) على 360f. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:275]

```
276:         animationSpec = infiniteRepeatable(
```
> يضبط الوسيط مواصفة-الحركة (animationSpec) على استدعاء infiniteRepeatable وفتح وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:276]

```
277:             animation = tween(durationMillis = 2000, easing = LinearEasing),
```
> يضبط الوسيط الحركة (animation) على استدعاء tween بضبط durationMillis على 2000 وeasing على LinearEasing. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:277]

```
278:             repeatMode = RepeatMode.Restart
```
> يضبط الوسيط وضع-التكرار (repeatMode) على RepeatMode.Restart. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:278]

```
279:         ),
```
> إغلاق قائمة وُسطاء استدعاء infiniteRepeatable. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:279]

```
280:         label = "rotation"
```
> يضبط الوسيط التسمية (label) على "rotation". [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:280]

```
281:     )
```
> إغلاق قائمة وُسطاء استدعاء animateFloat. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:281]

```
282: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:282]

```
283:     Box(
```
> استدعاء مكوّن الصندوق (Box) وفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:283]

```
284:         modifier = Modifier.size(60.dp),
```
> يضبط الوسيط المُعدِّل (modifier) على Modifier.size بقيمة 60.dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:284]

```
285:         contentAlignment = Alignment.Center
```
> يضبط الوسيط محاذاة-المحتوى (contentAlignment) على Alignment.Center. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:285]

```
286:     ) {
```
> إغلاق قائمة وُسطاء الصندوق وفتح كتلة محتواه اللاحقة (lambda). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:286]

```
287:         CircularProgressIndicator(
```
> استدعاء مكوّن مؤشّر-التقدّم-الدائري (CircularProgressIndicator) وفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:287]

```
288:             modifier = Modifier
```
> يضبط الوسيط المُعدِّل (modifier) على Modifier ويبدأ سلسلة استدعاءاته. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:288]

```
289:                 .fillMaxSize()
```
> يستدعي على المُعدِّل fillMaxSize. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:289]

```
290:                 .rotate(rotationAngle),
```
> يستدعي على المُعدِّل rotate بتمرير rotationAngle. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:290]

```
291:             color = Color(0xFF4CAF50), // Location green
```
> يضبط الوسيط اللون (color) على Color(0xFF4CAF50) متبوعاً بتعليق: أخضر الموقع. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:291]

```
292:             strokeWidth = 3.dp
```
> يضبط الوسيط عرض-الخطّ (strokeWidth) على 3.dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:292]

```
293:         )
```
> إغلاق قائمة وُسطاء استدعاء مؤشّر-التقدّم-الدائري. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:293]

```
294:     }
```
> إغلاق نطاق كتلة محتوى الصندوق. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:294]

```
295: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:295]
