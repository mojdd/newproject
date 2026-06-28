# شريحة — app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt (الأسطر 201–245)

```
201:                Text(
```
> استدعاء عنصر نصّ (Text) ببدء قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:201]

```
202:                    text = errorMessage,
```
> ضبط الوسيط النصّي (text) على قيمة المتغيّر رسالة-الخطأ (errorMessage). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:202]

```
203:                    style = MaterialTheme.typography.bodyMedium.copy(
```
> ضبط الوسيط النمط (style) على نسخة (copy) من نمط الجسم-المتوسّط (bodyMedium) المأخوذ من طِباعة (typography) سمة-ماتيريال (MaterialTheme) ببدء قائمة وسائط النسخة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:203]

```
204:                        fontFamily = FontFamily.Monospace,
```
> ضبط الوسيط عائلة-الخط (fontFamily) على القيمة أحادي-المسافة (Monospace) من عائلة-الخط (FontFamily). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:204]

```
205:                        color = colorScheme.onSurface
```
> ضبط الوسيط اللون (color) على القيمة على-السطح (onSurface) من مخطّط-الألوان (colorScheme). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:205]

```
206:                    ),
```
> إغلاق قائمة وسائط استدعاء النسخة (copy) وإنهاء قيمة الوسيط النمط بفاصلة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:206]

```
207:                    modifier = Modifier.padding(16.dp),
```
> ضبط الوسيط المُعدِّل (modifier) على المُعدِّل (Modifier) مع تطبيق حشوة (padding) بمقدار ١٦ بكسل-مستقل-الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:207]

```
208:                    textAlign = TextAlign.Center
```
> ضبط الوسيط محاذاة-النص (textAlign) على القيمة وسط (Center) من محاذاة-النص (TextAlign). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:208]

```
209:                )
```
> إغلاق قائمة وسائط استدعاء عنصر النصّ (Text). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:209]

```
210:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:210]

```
211:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:211]

```
212:            Column(
```
> استدعاء عنصر العمود (Column) ببدء قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:212]

```
213:                verticalArrangement = Arrangement.spacedBy(12.dp),
```
> ضبط الوسيط الترتيب-العمودي (verticalArrangement) على ترتيب (Arrangement) متباعد-بـ (spacedBy) بمقدار ١٢ بكسل-مستقل-الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:213]

```
214:                horizontalAlignment = Alignment.CenterHorizontally
```
> ضبط الوسيط المحاذاة-الأفقية (horizontalAlignment) على القيمة وسط-أفقياً (CenterHorizontally) من المحاذاة (Alignment). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:214]

```
215:            ) {
```
> إغلاق قائمة وسائط العمود (Column) وفتح كتلة المحتوى اللامية (lambda). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:215]

```
216:                Button(
```
> استدعاء عنصر الزر (Button) ببدء قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:216]

```
217:                    onClick = onRetry,
```
> ضبط الوسيط عند-النقر (onClick) على دالّة-المُعامِل إعادة-المحاولة (onRetry). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:217]

```
218:                    modifier = Modifier.fillMaxWidth()
```
> ضبط الوسيط المُعدِّل (modifier) على المُعدِّل (Modifier) مع تطبيق ملء-العرض-الأقصى (fillMaxWidth). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:218]

```
219:                ) {
```
> إغلاق قائمة وسائط الزر (Button) وفتح كتلة المحتوى اللامية (lambda). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:219]

```
220:                    Text(
```
> استدعاء عنصر النصّ (Text) ببدء قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:220]

```
221:                        text = stringResource(R.string.try_again),
```
> ضبط الوسيط النصّي (text) على مورد-النص (stringResource) للمورد حاول-مجدداً (try_again) من الموارد (R.string). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:221]

```
222:                        style = MaterialTheme.typography.bodyMedium.copy(
```
> ضبط الوسيط النمط (style) على نسخة (copy) من نمط الجسم-المتوسّط (bodyMedium) المأخوذ من طِباعة (typography) سمة-ماتيريال (MaterialTheme) ببدء قائمة وسائط النسخة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:222]

```
223:                            fontFamily = FontFamily.Monospace,
```
> ضبط الوسيط عائلة-الخط (fontFamily) على القيمة أحادي-المسافة (Monospace) من عائلة-الخط (FontFamily). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:223]

```
224:                            fontWeight = FontWeight.Bold
```
> ضبط الوسيط وزن-الخط (fontWeight) على القيمة عريض (Bold) من وزن-الخط (FontWeight). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:224]

```
225:                        ),
```
> إغلاق قائمة وسائط استدعاء النسخة (copy) وإنهاء قيمة الوسيط النمط بفاصلة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:225]

```
226:                        modifier = Modifier.padding(vertical = 4.dp)
```
> ضبط الوسيط المُعدِّل (modifier) على المُعدِّل (Modifier) مع تطبيق حشوة (padding) عمودية (vertical) بمقدار ٤ بكسل-مستقل-الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:226]

```
227:                    )
```
> إغلاق قائمة وسائط استدعاء عنصر النصّ (Text). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:227]

```
228:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:228]

```
229:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:229]

```
230:                OutlinedButton(
```
> استدعاء عنصر الزر-المُحاط-بإطار (OutlinedButton) ببدء قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:230]

```
231:                    onClick = onOpenSettings,
```
> ضبط الوسيط عند-النقر (onClick) على دالّة-المُعامِل فتح-الإعدادات (onOpenSettings). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:231]

```
232:                    modifier = Modifier.fillMaxWidth()
```
> ضبط الوسيط المُعدِّل (modifier) على المُعدِّل (Modifier) مع تطبيق ملء-العرض-الأقصى (fillMaxWidth). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:232]

```
233:                ) {
```
> إغلاق قائمة وسائط الزر-المُحاط-بإطار (OutlinedButton) وفتح كتلة المحتوى اللامية (lambda). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:233]

```
234:                    Text(
```
> استدعاء عنصر النصّ (Text) ببدء قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:234]

```
235:                        text = stringResource(R.string.open_settings),
```
> ضبط الوسيط النصّي (text) على مورد-النص (stringResource) للمورد فتح-الإعدادات (open_settings) من الموارد (R.string). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:235]

```
236:                        style = MaterialTheme.typography.bodyMedium.copy(
```
> ضبط الوسيط النمط (style) على نسخة (copy) من نمط الجسم-المتوسّط (bodyMedium) المأخوذ من طِباعة (typography) سمة-ماتيريال (MaterialTheme) ببدء قائمة وسائط النسخة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:236]

```
237:                            fontFamily = FontFamily.Monospace
```
> ضبط الوسيط عائلة-الخط (fontFamily) على القيمة أحادي-المسافة (Monospace) من عائلة-الخط (FontFamily). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:237]

```
238:                        ),
```
> إغلاق قائمة وسائط استدعاء النسخة (copy) وإنهاء قيمة الوسيط النمط بفاصلة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:238]

```
239:                        modifier = Modifier.padding(vertical = 4.dp)
```
> ضبط الوسيط المُعدِّل (modifier) على المُعدِّل (Modifier) مع تطبيق حشوة (padding) عمودية (vertical) بمقدار ٤ بكسل-مستقل-الكثافة (dp). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:239]

```
240:                    )
```
> إغلاق قائمة وسائط استدعاء عنصر النصّ (Text). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:240]

```
241:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:241]

```
242:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:242]

```
243:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:243]

```
244:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:244]

```
245:}
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:245]
