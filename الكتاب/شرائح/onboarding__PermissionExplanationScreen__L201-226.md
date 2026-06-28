# شريحة — app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt (الأسطر 201–226)

```
201:                 fontWeight = FontWeight.Medium,
```
> يضبط معامل وزن الخط (fontWeight) على القيمة FontWeight.Medium (متوسط). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:201]

```
202:                 color = colorScheme.onBackground
```
> يضبط معامل اللون (color) على القيمة colorScheme.onBackground (اللون فوق الخلفية في نظام الألوان). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:202]

```
203:             )
```
> إغلاق نطاق (إغلاق قوس استدعاء). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:203]

```
204:             Spacer(modifier = Modifier.height(4.dp))
```
> يستدعي العنصر الفاصل (Spacer) ويمرّر له المُعدِّل (modifier) المساوي لـ Modifier.height(4.dp) أي ارتفاع مقداره 4 وحدات كثافة مستقلة (dp). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:204]

```
205:             Text(
```
> يستدعي عنصر النص (Text) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:205]

```
206:                 text = category.description,
```
> يضبط معامل النص (text) على القيمة category.description (وصف الفئة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:206]

```
207:                 style = MaterialTheme.typography.bodySmall,
```
> يضبط معامل النمط (style) على القيمة MaterialTheme.typography.bodySmall (نمط النص الصغير من طباعة سمة ماتيريال). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:207]

```
208:                 color = colorScheme.onBackground.copy(alpha = 0.8f)
```
> يضبط معامل اللون (color) على القيمة colorScheme.onBackground مع استدعاء النسخ (copy) وتعيين الشفافية (alpha) إلى 0.8 من نوع float. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:208]

```
209:             )
```
> إغلاق نطاق (إغلاق قوس استدعاء). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:209]

```
210: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:210]

```
211:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:211]

```
212:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:212]

```
213: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:213]

```
214: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:214]

```
215: private fun getPermissionIcon(permissionType: PermissionType): ImageVector {
```
> يُعرّف دالة خاصة (private) باسم getPermissionIcon (الحصول على أيقونة الإذن) تأخذ معامِلاً باسم permissionType (نوع الإذن) من نوع PermissionType (نوع الإذن) وتُعيد قيمة من نوع ImageVector (متجه الصورة)، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:215]

```
216:     return when (permissionType) {
```
> يُعيد (return) نتيجة تعبير when (عندما) المبني على المعامل permissionType، ويفتح فروع المطابقة. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:216]

```
217:         PermissionType.NEARBY_DEVICES -> Icons.Filled.Bluetooth
```
> عند مطابقة القيمة PermissionType.NEARBY_DEVICES (الأجهزة القريبة) تُعاد القيمة Icons.Filled.Bluetooth (أيقونة بلوتوث المملوءة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:217]

```
218:         PermissionType.PRECISE_LOCATION -> Icons.Filled.LocationOn
```
> عند مطابقة القيمة PermissionType.PRECISE_LOCATION (الموقع الدقيق) تُعاد القيمة Icons.Filled.LocationOn (أيقونة الموقع المُفعَّل المملوءة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:218]

```
219:         PermissionType.BACKGROUND_LOCATION -> Icons.Filled.LocationOn
```
> عند مطابقة القيمة PermissionType.BACKGROUND_LOCATION (موقع الخلفية) تُعاد القيمة Icons.Filled.LocationOn (أيقونة الموقع المُفعَّل المملوءة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:219]

```
220:         PermissionType.MICROPHONE -> Icons.Filled.Mic
```
> عند مطابقة القيمة PermissionType.MICROPHONE (الميكروفون) تُعاد القيمة Icons.Filled.Mic (أيقونة الميكروفون المملوءة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:220]

```
221:         PermissionType.NOTIFICATIONS -> Icons.Filled.Notifications
```
> عند مطابقة القيمة PermissionType.NOTIFICATIONS (الإشعارات) تُعاد القيمة Icons.Filled.Notifications (أيقونة الإشعارات المملوءة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:221]

```
222:         PermissionType.WIFI_AWARE -> Icons.Filled.Wifi
```
> عند مطابقة القيمة PermissionType.WIFI_AWARE (واي فاي أوير) تُعاد القيمة Icons.Filled.Wifi (أيقونة واي فاي المملوءة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:222]

```
223:         PermissionType.BATTERY_OPTIMIZATION -> Icons.Filled.Power
```
> عند مطابقة القيمة PermissionType.BATTERY_OPTIMIZATION (تحسين البطارية) تُعاد القيمة Icons.Filled.Power (أيقونة الطاقة المملوءة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:223]

```
224:         PermissionType.OTHER -> Icons.Filled.Settings
```
> عند مطابقة القيمة PermissionType.OTHER (أخرى) تُعاد القيمة Icons.Filled.Settings (أيقونة الإعدادات المملوءة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:224]

```
225:     }
```
> إغلاق نطاق (إغلاق تعبير when). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:225]

```
226: }
```
> إغلاق نطاق (إغلاق جسم الدالة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:226]
