# شريحة — app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt (الأسطر 201–251)

```
201:                         Text(
```
> استدعاء مُركِّب نصي (Text) يبدأ هنا بفتح قوسه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:201]

```
202:                             text = stringResource(R.string.check_again),
```
> ضبط الوسيط نص (text) إلى قيمة مورد نصّي (stringResource) المُعرَّف بالمُعرِّف R.string.check_again. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:202]

```
203:                             style = MaterialTheme.typography.bodyMedium.copy(
```
> ضبط الوسيط نمط (style) إلى نسخة (copy) من نمط الطباعة المتوسط (bodyMedium) المأخوذ من طباعة MaterialTheme، مع فتح قوس النسخ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:203]

```
204:                                 fontFamily = FontFamily.Monospace
```
> ضبط عائلة الخط (fontFamily) إلى الخط أحادي المسافة (Monospace). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:204]

```
205:                             )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:205]

```
206:                         )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:206]

```
207:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:207]

```
208: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:208]

```
209:                     TextButton(
```
> استدعاء مُركِّب زر نصّي (TextButton) يبدأ هنا بفتح قوسه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:209]

```
210:                         onClick = onSkip,
```
> ضبط الوسيط عند النقر (onClick) إلى الدالة المُمرَّرة onSkip. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:210]

```
211:                         modifier = Modifier.weight(1f)
```
> ضبط الوسيط مُعدِّل (modifier) إلى Modifier مع تطبيق الوزن (weight) بقيمة 1f. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:211]

```
212:                     ) {
```
> إغلاق قوس وسائط الاستدعاء وفتح كتلة المحتوى المُركِّب (lambda) بقوس معقوف. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:212]

```
213:                         Text(
```
> استدعاء مُركِّب نصي (Text) يبدأ هنا بفتح قوسه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:213]

```
214:                             text = stringResource(R.string.battery_optimization_skip),
```
> ضبط الوسيط نص (text) إلى قيمة مورد نصّي (stringResource) المُعرَّف بالمُعرِّف R.string.battery_optimization_skip. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:214]

```
215:                             style = MaterialTheme.typography.bodyMedium.copy(
```
> ضبط الوسيط نمط (style) إلى نسخة (copy) من نمط الطباعة المتوسط (bodyMedium) المأخوذ من طباعة MaterialTheme، مع فتح قوس النسخ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:215]

```
216:                                 fontFamily = FontFamily.Monospace
```
> ضبط عائلة الخط (fontFamily) إلى الخط أحادي المسافة (Monospace). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:216]

```
217:                             )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:217]

```
218:                         )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:218]

```
219:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:219]

```
220:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:220]

```
221:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:221]

```
222:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:222]

```
223:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:223]

```
224: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:224]

```
225: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:225]

```
226: @Composable
```
> توسيم (annotation) المُركِّب (Composable) المطبَّق على الدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:226]

```
227: private fun HeaderSection(colorScheme: ColorScheme) {
```
> تعريف دالة خاصّة (private) باسم قسم الترويسة (HeaderSection) تستقبل وسيطاً باسم مخطط الألوان (colorScheme) من نوع ColorScheme، مع فتح جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:227]

```
228:     Column(
```
> استدعاء مُركِّب عمود (Column) يبدأ هنا بفتح قوسه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:228]

```
229:         modifier = Modifier
```
> ضبط الوسيط مُعدِّل (modifier) إلى Modifier، مع متابعة تسلسل المُعدِّلات في الأسطر التالية. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:229]

```
230:             .fillMaxWidth()
```
> تطبيق المُعدِّل ملء العرض الأقصى (fillMaxWidth). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:230]

```
231:             .padding(bottom = 16.dp),
```
> تطبيق المُعدِّل حشوة (padding) مع ضبط الأسفل (bottom) إلى 16.dp. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:231]

```
232:         verticalArrangement = Arrangement.spacedBy(8.dp)
```
> ضبط الوسيط الترتيب العمودي (verticalArrangement) إلى مباعدة (spacedBy) بقيمة 8.dp. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:232]

```
233:     ) {
```
> إغلاق قوس وسائط الاستدعاء وفتح كتلة المحتوى المُركِّب (lambda) بقوس معقوف. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:233]

```
234:         Text(
```
> استدعاء مُركِّب نصي (Text) يبدأ هنا بفتح قوسه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:234]

```
235:             text = stringResource(R.string.app_name),
```
> ضبط الوسيط نص (text) إلى قيمة مورد نصّي (stringResource) المُعرَّف بالمُعرِّف R.string.app_name. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:235]

```
236:             style = MaterialTheme.typography.headlineLarge.copy(
```
> ضبط الوسيط نمط (style) إلى نسخة (copy) من نمط العنوان الكبير (headlineLarge) المأخوذ من طباعة MaterialTheme، مع فتح قوس النسخ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:236]

```
237:                 fontFamily = FontFamily.Monospace,
```
> ضبط عائلة الخط (fontFamily) إلى الخط أحادي المسافة (Monospace). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:237]

```
238:                 fontWeight = FontWeight.Bold,
```
> ضبط وزن الخط (fontWeight) إلى العريض (Bold). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:238]

```
239:                 fontSize = 32.sp
```
> ضبط حجم الخط (fontSize) إلى 32.sp. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:239]

```
240:             ),
```
> إغلاق قوس النسخ (copy) متبوعاً بفاصلة. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:240]

```
241:             color = colorScheme.onBackground
```
> ضبط الوسيط لون (color) إلى لون فوق الخلفية (onBackground) من مخطط الألوان colorScheme. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:241]

```
242:         )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:242]

```
243: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:243]

```
244:         Text(
```
> استدعاء مُركِّب نصي (Text) يبدأ هنا بفتح قوسه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:244]

```
245:             text = stringResource(R.string.background_location_required_subtitle),
```
> ضبط الوسيط نص (text) إلى قيمة مورد نصّي (stringResource) المُعرَّف بالمُعرِّف R.string.background_location_required_subtitle. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:245]

```
246:             fontSize = 12.sp,
```
> ضبط الوسيط حجم الخط (fontSize) إلى 12.sp. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:246]

```
247:             fontFamily = FontFamily.Monospace,
```
> ضبط الوسيط عائلة الخط (fontFamily) إلى الخط أحادي المسافة (Monospace). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:247]

```
248:             color = colorScheme.onBackground.copy(alpha = 0.7f)
```
> ضبط الوسيط لون (color) إلى نسخة (copy) من لون فوق الخلفية (onBackground) من مخطط الألوان colorScheme مع ضبط الشفافية (alpha) إلى 0.7f. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:248]

```
249:         )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:249]

```
250:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:250]

```
251: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:251]
