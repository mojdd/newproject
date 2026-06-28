# شريحة — app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt (الأسطر 1–200)

```
1: package com.bitchat.android.onboarding
```
> يُعرِّف اسم الحزمة (package) بأنها `com.bitchat.android.onboarding`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:2]

```
3: import androidx.compose.animation.core.*
```
> يستورد (import) كل الرموز من حزمة `androidx.compose.animation.core`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:3]

```
4: import androidx.compose.foundation.layout.*
```
> يستورد كل الرموز من حزمة التخطيط `androidx.compose.foundation.layout`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:4]

```
5: import androidx.compose.material.icons.Icons
```
> يستورد الرمز `Icons` من حزمة أيقونات الماتيريال (material.icons). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:5]

```
6: import androidx.compose.material.icons.filled.*
```
> يستورد كل الرموز من حزمة الأيقونات الممتلئة (filled). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:6]

```
7: import androidx.compose.material.icons.outlined.*
```
> يستورد كل الرموز من حزمة الأيقونات المحدّدة بالحدّ (outlined). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:7]

```
8: import androidx.compose.material3.*
```
> يستورد كل الرموز من حزمة الماتيريال الثالثة (material3). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:8]

```
9: import androidx.compose.runtime.*
```
> يستورد كل الرموز من حزمة زمن التشغيل (runtime). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:9]

```
10: import androidx.compose.ui.Alignment
```
> يستورد الرمز `Alignment` (المحاذاة) من حزمة `androidx.compose.ui`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:10]

```
11: import androidx.compose.ui.Modifier
```
> يستورد الرمز `Modifier` (المعدِّل) من حزمة `androidx.compose.ui`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:11]

```
12: import androidx.compose.ui.draw.rotate
```
> يستورد الدالة `rotate` (الدوران) من حزمة `androidx.compose.ui.draw`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:12]

```
13: import androidx.compose.ui.graphics.Color
```
> يستورد الرمز `Color` (اللون) من حزمة `androidx.compose.ui.graphics`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:13]

```
14: import androidx.compose.ui.text.font.FontFamily
```
> يستورد الرمز `FontFamily` (عائلة الخط) من حزمة `androidx.compose.ui.text.font`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:14]

```
15: import androidx.compose.ui.text.font.FontWeight
```
> يستورد الرمز `FontWeight` (ثِقَل الخط) من حزمة `androidx.compose.ui.text.font`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:15]

```
16: import androidx.compose.ui.text.style.TextAlign
```
> يستورد الرمز `TextAlign` (محاذاة النص) من حزمة `androidx.compose.ui.text.style`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:16]

```
17: import androidx.compose.ui.unit.dp
```
> يستورد الوحدة `dp` (وحدة البكسل المستقلة عن الكثافة) من حزمة `androidx.compose.ui.unit`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:17]

```
18: import androidx.compose.ui.res.stringResource
```
> يستورد الدالة `stringResource` (مورد النص) من حزمة `androidx.compose.ui.res`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:18]

```
19: import com.bitchat.android.R
```
> يستورد فئة الموارد `R` من حزمة `com.bitchat.android`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:19]

```
20: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:20]

```
21: /**
```
> تعليق: بداية تعليق توثيقي بالنمط `/** `. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:21]

```
22:  * Screen shown when checking location services status or requesting location services enable
```
> تعليق: «شاشة تُعرَض عند فحص حالة خدمات الموقع أو عند طلب تفعيل خدمات الموقع». [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:22]

```
23:  */
```
> تعليق: نهاية التعليق التوثيقي `*/`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:23]

```
24: @Composable
```
> يضع التعليق التوصيفي (annotation) `@Composable` على الدالة التالية، أي إنها دالة قابلة للتركيب. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:24]

```
25: fun LocationCheckScreen(
```
> يُعرِّف دالة عامة باسم `LocationCheckScreen` (شاشة فحص الموقع) وبداية قائمة وُسطائها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:25]

```
26:     modifier: Modifier,
```
> يُعرِّف الوسيط `modifier` (المعدِّل) من النوع `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:26]

```
27:     status: LocationStatus,
```
> يُعرِّف الوسيط `status` (الحالة) من النوع `LocationStatus` (حالة الموقع). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:27]

```
28:     onEnableLocation: () -> Unit,
```
> يُعرِّف الوسيط `onEnableLocation` (عند تفعيل الموقع) دالةً بلا وُسطاء تُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:28]

```
29:     onRetry: () -> Unit,
```
> يُعرِّف الوسيط `onRetry` (عند إعادة المحاولة) دالةً بلا وُسطاء تُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:29]

```
30:     isLoading: Boolean = false
```
> يُعرِّف الوسيط `isLoading` (هل يحمّل) من النوع المنطقي `Boolean` بقيمة افتراضية `false`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:30]

```
31: ) {
```
> إغلاق قائمة الوُسطاء وبداية جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:31]

```
32:     val colorScheme = MaterialTheme.colorScheme
```
> يُعرِّف ثابتاً `colorScheme` (نظام الألوان) ويُسنِد إليه `MaterialTheme.colorScheme`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:33]

```
34:     Box(
```
> يستدعي المُركِّب `Box` (صندوق) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:34]

```
35:         modifier = modifier.padding(32.dp),
```
> يُسنِد للوسيط `modifier` قيمة `modifier.padding(32.dp)`، أي يضيف حشواً (padding) قدره 32 وحدة dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:35]

```
36:         contentAlignment = Alignment.Center
```
> يُسنِد للوسيط `contentAlignment` (محاذاة المحتوى) القيمة `Alignment.Center` أي التوسيط. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:36]

```
37:     ) {
```
> إغلاق وُسطاء `Box` وبداية جسم المُركِّب. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:37]

```
38:         when (status) {
```
> يبدأ تعبير `when` (عند) على القيمة `status`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:38]

```
39:             LocationStatus.DISABLED -> {
```
> فرع لمّا تكون `status` تساوي `LocationStatus.DISABLED` (معطّل)، وبداية جسمه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:39]

```
40:                 LocationDisabledContent(
```
> يستدعي المُركِّب `LocationDisabledContent` (محتوى الموقع المعطّل) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:40]

```
41:                     onEnableLocation = onEnableLocation,
```
> يُسنِد للوسيط `onEnableLocation` القيمة `onEnableLocation`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:41]

```
42:                     onRetry = onRetry,
```
> يُسنِد للوسيط `onRetry` القيمة `onRetry`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:42]

```
43:                     colorScheme = colorScheme,
```
> يُسنِد للوسيط `colorScheme` القيمة `colorScheme`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:43]

```
44:                     isLoading = isLoading
```
> يُسنِد للوسيط `isLoading` القيمة `isLoading`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:44]

```
45:                 )
```
> إغلاق استدعاء `LocationDisabledContent`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:45]

```
46:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:46]

```
47:             LocationStatus.NOT_AVAILABLE -> {
```
> فرع لمّا تكون `status` تساوي `LocationStatus.NOT_AVAILABLE` (غير متاح)، وبداية جسمه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:47]

```
48:                 LocationNotAvailableContent(
```
> يستدعي المُركِّب `LocationNotAvailableContent` (محتوى الموقع غير المتاح) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:48]

```
49:                     colorScheme = colorScheme
```
> يُسنِد للوسيط `colorScheme` القيمة `colorScheme`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:49]

```
50:                 )
```
> إغلاق استدعاء `LocationNotAvailableContent`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:50]

```
51:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:51]

```
52:             LocationStatus.ENABLED -> {
```
> فرع لمّا تكون `status` تساوي `LocationStatus.ENABLED` (مفعّل)، وبداية جسمه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:52]

```
53:                 LocationCheckingContent(
```
> يستدعي المُركِّب `LocationCheckingContent` (محتوى فحص الموقع) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:53]

```
54:                     colorScheme = colorScheme
```
> يُسنِد للوسيط `colorScheme` القيمة `colorScheme`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:54]

```
55:                 )
```
> إغلاق استدعاء `LocationCheckingContent`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:55]

```
56:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:56]

```
57:         }
```
> إغلاق تعبير `when`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:57]

```
58:     }
```
> إغلاق نطاق المُركِّب `Box`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:58]

```
59: }
```
> إغلاق نطاق الدالة `LocationCheckScreen`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:59]

```
60: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:60]

```
61: @Composable
```
> يضع التعليق التوصيفي `@Composable` على الدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:61]

```
62: private fun LocationDisabledContent(
```
> يُعرِّف دالة خاصة (private) باسم `LocationDisabledContent` وبداية قائمة وُسطائها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:62]

```
63:     onEnableLocation: () -> Unit,
```
> يُعرِّف الوسيط `onEnableLocation` دالةً بلا وُسطاء تُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:63]

```
64:     onRetry: () -> Unit,
```
> يُعرِّف الوسيط `onRetry` دالةً بلا وُسطاء تُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:64]

```
65:     colorScheme: ColorScheme,
```
> يُعرِّف الوسيط `colorScheme` من النوع `ColorScheme` (نظام الألوان). [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:65]

```
66:     isLoading: Boolean
```
> يُعرِّف الوسيط `isLoading` من النوع المنطقي `Boolean` بلا قيمة افتراضية. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:66]

```
67: ) {
```
> إغلاق قائمة الوُسطاء وبداية جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:67]

```
68:     Column(
```
> يستدعي المُركِّب `Column` (عمود) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:68]

```
69:         verticalArrangement = Arrangement.spacedBy(24.dp),
```
> يُسنِد للوسيط `verticalArrangement` (الترتيب الرأسي) القيمة `Arrangement.spacedBy(24.dp)` أي تباعد 24 وحدة dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:69]

```
70:         horizontalAlignment = Alignment.CenterHorizontally
```
> يُسنِد للوسيط `horizontalAlignment` (المحاذاة الأفقية) القيمة `Alignment.CenterHorizontally` أي التوسيط أفقياً. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:70]

```
71:     ) {
```
> إغلاق وُسطاء `Column` وبداية جسم المُركِّب. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:71]

```
72:         // Location icon - using LocationOn outlined icon in app's green color
```
> تعليق: «أيقونة الموقع - باستعمال أيقونة LocationOn المحدّدة بالحدّ بلون التطبيق الأخضر». [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:72]

```
73:         Icon(
```
> يستدعي المُركِّب `Icon` (أيقونة) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:73]

```
74:             imageVector = Icons.Outlined.LocationOn,
```
> يُسنِد للوسيط `imageVector` (متجه الصورة) القيمة `Icons.Outlined.LocationOn`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:74]

```
75:             contentDescription = stringResource(R.string.cd_location_services),
```
> يُسنِد للوسيط `contentDescription` (وصف المحتوى) نص المورد `R.string.cd_location_services`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:75]

```
76:             modifier = Modifier.size(64.dp),
```
> يُسنِد للوسيط `modifier` القيمة `Modifier.size(64.dp)` أي مقاس 64 وحدة dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:76]

```
77:             tint = Color(0xFF00C851) // App's main green color
```
> يُسنِد للوسيط `tint` (الصبغة) القيمة `Color(0xFF00C851)`، وتعليق: «لون التطبيق الأخضر الرئيسي». [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:77]

```
78:         )
```
> إغلاق استدعاء `Icon`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:78]

```
79: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:79]

```
80:         Text(
```
> يستدعي المُركِّب `Text` (نص) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:80]

```
81:             text = stringResource(R.string.location_services_required),
```
> يُسنِد للوسيط `text` (النص) نص المورد `R.string.location_services_required`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:81]

```
82:             style = MaterialTheme.typography.headlineSmall.copy(
```
> يُسنِد للوسيط `style` (النمط) نسخةً مُعدَّلة من `MaterialTheme.typography.headlineSmall` وبداية تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:82]

```
83:                 fontFamily = FontFamily.Monospace,
```
> يُسنِد للخاصية `fontFamily` القيمة `FontFamily.Monospace` أي الخط أحادي المسافة. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:83]

```
84:                 fontWeight = FontWeight.Bold,
```
> يُسنِد للخاصية `fontWeight` القيمة `FontWeight.Bold` أي الثقل العريض. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:84]

```
85:                 color = colorScheme.primary
```
> يُسنِد للخاصية `color` القيمة `colorScheme.primary` أي اللون الأساسي. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:85]

```
86:             ),
```
> إغلاق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:86]

```
87:             textAlign = TextAlign.Center
```
> يُسنِد للوسيط `textAlign` القيمة `TextAlign.Center` أي توسيط النص. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:87]

```
88:         )
```
> إغلاق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:88]

```
89: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:89]

```
90:         Card(
```
> يستدعي المُركِّب `Card` (بطاقة) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:90]

```
91:             modifier = Modifier.fillMaxWidth(),
```
> يُسنِد للوسيط `modifier` القيمة `Modifier.fillMaxWidth()` أي ملء العرض الأقصى. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:91]

```
92:             colors = CardDefaults.cardColors(
```
> يُسنِد للوسيط `colors` نتيجة استدعاء `CardDefaults.cardColors` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:92]

```
93:                 containerColor = colorScheme.surfaceVariant.copy(alpha = 0.3f)
```
> يُسنِد للوسيط `containerColor` (لون الحاوية) نسخةً من `colorScheme.surfaceVariant` بشفافية `alpha = 0.3f`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:93]

```
94:             ),
```
> إغلاق استدعاء `cardColors`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:94]

```
95:             elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
```
> يُسنِد للوسيط `elevation` (الارتفاع) نتيجة `CardDefaults.cardElevation` بوسيط `defaultElevation = 2.dp`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:95]

```
96:         ) {
```
> إغلاق وُسطاء `Card` وبداية جسم المُركِّب. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:96]

```
97:             Column(
```
> يستدعي المُركِّب `Column` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:97]

```
98:                 modifier = Modifier.padding(16.dp),
```
> يُسنِد للوسيط `modifier` القيمة `Modifier.padding(16.dp)` أي حشو 16 وحدة dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:98]

```
99:                 verticalArrangement = Arrangement.spacedBy(12.dp)
```
> يُسنِد للوسيط `verticalArrangement` القيمة `Arrangement.spacedBy(12.dp)` أي تباعد 12 وحدة dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:99]

```
100:             ) {
```
> إغلاق وُسطاء `Column` وبداية جسم المُركِّب. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:100]

```
101:                 // Privacy assurance section
```
> تعليق: «قسم توكيد الخصوصية». [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:101]

```
102:                 Row(
```
> يستدعي المُركِّب `Row` (صفّ) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:102]

```
103:                     verticalAlignment = Alignment.CenterVertically,
```
> يُسنِد للوسيط `verticalAlignment` القيمة `Alignment.CenterVertically` أي التوسيط رأسياً. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:103]

```
104:                     modifier = Modifier.fillMaxWidth()
```
> يُسنِد للوسيط `modifier` القيمة `Modifier.fillMaxWidth()` أي ملء العرض الأقصى. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:104]

```
105:                 ) {
```
> إغلاق وُسطاء `Row` وبداية جسم المُركِّب. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:105]

```
106:                     Icon(
```
> يستدعي المُركِّب `Icon` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:106]

```
107:                         imageVector = Icons.Filled.Security,
```
> يُسنِد للوسيط `imageVector` القيمة `Icons.Filled.Security` أي أيقونة الأمان الممتلئة. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:107]

```
108:                         contentDescription = stringResource(R.string.cd_privacy),
```
> يُسنِد للوسيط `contentDescription` نص المورد `R.string.cd_privacy`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:108]

```
109:                         tint = Color(0xFF4CAF50),
```
> يُسنِد للوسيط `tint` القيمة `Color(0xFF4CAF50)`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:109]

```
110:                         modifier = Modifier.size(20.dp)
```
> يُسنِد للوسيط `modifier` القيمة `Modifier.size(20.dp)` أي مقاس 20 وحدة dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:110]

```
111:                     )
```
> إغلاق استدعاء `Icon`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:111]

```
112:                     Spacer(modifier = Modifier.width(8.dp))
```
> يستدعي المُركِّب `Spacer` (فاصل) بوسيط `modifier = Modifier.width(8.dp)` أي عرض 8 وحدات dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:112]

```
113:                         Text(
```
> يستدعي المُركِّب `Text` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:113]

```
114:                             text = stringResource(R.string.privacy_first),
```
> يُسنِد للوسيط `text` نص المورد `R.string.privacy_first`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:114]

```
115:                         style = MaterialTheme.typography.bodyMedium.copy(
```
> يُسنِد للوسيط `style` نسخةً مُعدَّلة من `MaterialTheme.typography.bodyMedium` وبداية تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:115]

```
116:                             fontWeight = FontWeight.Bold,
```
> يُسنِد للخاصية `fontWeight` القيمة `FontWeight.Bold`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:116]

```
117:                             color = colorScheme.onSurface
```
> يُسنِد للخاصية `color` القيمة `colorScheme.onSurface`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:117]

```
118:                         )
```
> إغلاق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:118]

```
119:                     )
```
> إغلاق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:119]

```
120:                 }
```
> إغلاق نطاق المُركِّب `Row`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:120]

```
121:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:121]

```
122:                     Text(
```
> يستدعي المُركِّب `Text` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:122]

```
123:                         text = stringResource(R.string.location_explanation),
```
> يُسنِد للوسيط `text` نص المورد `R.string.location_explanation`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:123]

```
124:                     style = MaterialTheme.typography.bodySmall.copy(
```
> يُسنِد للوسيط `style` نسخةً مُعدَّلة من `MaterialTheme.typography.bodySmall` وبداية تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:124]

```
125:                         fontFamily = FontFamily.Monospace,
```
> يُسنِد للخاصية `fontFamily` القيمة `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:125]

```
126:                         color = colorScheme.onSurface.copy(alpha = 0.8f)
```
> يُسنِد للخاصية `color` نسخةً من `colorScheme.onSurface` بشفافية `alpha = 0.8f`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:126]

```
127:                     )
```
> إغلاق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:127]

```
128:                 )
```
> إغلاق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:128]

```
129: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:129]

```
130:                 Spacer(modifier = Modifier.height(4.dp))
```
> يستدعي المُركِّب `Spacer` بوسيط `modifier = Modifier.height(4.dp)` أي ارتفاع 4 وحدات dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:130]

```
131: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:131]

```
132:                     Text(
```
> يستدعي المُركِّب `Text` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:132]

```
133:                         text = stringResource(R.string.location_needs_for),
```
> يُسنِد للوسيط `text` نص المورد `R.string.location_needs_for`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:133]

```
134:                     style = MaterialTheme.typography.bodyMedium.copy(
```
> يُسنِد للوسيط `style` نسخةً مُعدَّلة من `MaterialTheme.typography.bodyMedium` وبداية تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:134]

```
135:                         fontWeight = FontWeight.Medium,
```
> يُسنِد للخاصية `fontWeight` القيمة `FontWeight.Medium` أي الثقل المتوسط. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:135]

```
136:                         color = colorScheme.onSurface
```
> يُسنِد للخاصية `color` القيمة `colorScheme.onSurface`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:136]

```
137:                     ),
```
> إغلاق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:137]

```
138:                     textAlign = TextAlign.Center,
```
> يُسنِد للوسيط `textAlign` القيمة `TextAlign.Center`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:138]

```
139:                     modifier = Modifier.fillMaxWidth()
```
> يُسنِد للوسيط `modifier` القيمة `Modifier.fillMaxWidth()`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:139]

```
140:                 )
```
> إغلاق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:140]

```
141:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:141]

```
142:                     Text(
```
> يستدعي المُركِّب `Text` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:142]

```
143:                         text = stringResource(R.string.location_needs_bullets),
```
> يُسنِد للوسيط `text` نص المورد `R.string.location_needs_bullets`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:143]

```
144:                     style = MaterialTheme.typography.bodySmall.copy(
```
> يُسنِد للوسيط `style` نسخةً مُعدَّلة من `MaterialTheme.typography.bodySmall` وبداية تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:144]

```
145:                         fontFamily = FontFamily.Monospace,
```
> يُسنِد للخاصية `fontFamily` القيمة `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:145]

```
146:                         color = colorScheme.onSurface.copy(alpha = 0.8f)
```
> يُسنِد للخاصية `color` نسخةً من `colorScheme.onSurface` بشفافية `alpha = 0.8f`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:146]

```
147:                     )
```
> إغلاق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:147]

```
148:                 )
```
> إغلاق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:148]

```
149:             }
```
> إغلاق نطاق المُركِّب `Column` الداخلي. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:149]

```
150:         }
```
> إغلاق نطاق المُركِّب `Card`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:150]

```
151: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:151]

```
152:         if (isLoading) {
```
> يبدأ شرطاً `if` على القيمة `isLoading`، وبداية جسمه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:152]

```
153:             LocationLoadingIndicator()
```
> يستدعي المُركِّب `LocationLoadingIndicator` (مؤشّر تحميل الموقع) بلا وُسطاء. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:153]

```
154:         } else {
```
> إغلاق جسم `if` وبداية فرع `else`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:154]

```
155:             Column(
```
> يستدعي المُركِّب `Column` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:155]

```
156:                 verticalArrangement = Arrangement.spacedBy(12.dp),
```
> يُسنِد للوسيط `verticalArrangement` القيمة `Arrangement.spacedBy(12.dp)` أي تباعد 12 وحدة dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:156]

```
157:                 horizontalAlignment = Alignment.CenterHorizontally
```
> يُسنِد للوسيط `horizontalAlignment` القيمة `Alignment.CenterHorizontally`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:157]

```
158:             ) {
```
> إغلاق وُسطاء `Column` وبداية جسم المُركِّب. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:158]

```
159:                 Button(
```
> يستدعي المُركِّب `Button` (زر) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:159]

```
160:                     onClick = onEnableLocation,
```
> يُسنِد للوسيط `onClick` (عند النقر) القيمة `onEnableLocation`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:160]

```
161:                     modifier = Modifier.fillMaxWidth(),
```
> يُسنِد للوسيط `modifier` القيمة `Modifier.fillMaxWidth()`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:161]

```
162:                     colors = ButtonDefaults.buttonColors(
```
> يُسنِد للوسيط `colors` نتيجة استدعاء `ButtonDefaults.buttonColors` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:162]

```
163:                         containerColor = Color(0xFF00C851) // App's main green color
```
> يُسنِد للوسيط `containerColor` القيمة `Color(0xFF00C851)`، وتعليق: «لون التطبيق الأخضر الرئيسي». [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:163]

```
164:                     )
```
> إغلاق استدعاء `buttonColors`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:164]

```
165:                 ) {
```
> إغلاق وُسطاء `Button` وبداية جسم المُركِّب. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:165]

```
166:                         Text(
```
> يستدعي المُركِّب `Text` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:166]

```
167:                             text = stringResource(R.string.open_location_settings),
```
> يُسنِد للوسيط `text` نص المورد `R.string.open_location_settings`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:167]

```
168:                         style = MaterialTheme.typography.bodyMedium.copy(
```
> يُسنِد للوسيط `style` نسخةً مُعدَّلة من `MaterialTheme.typography.bodyMedium` وبداية تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:168]

```
169:                             fontFamily = FontFamily.Monospace,
```
> يُسنِد للخاصية `fontFamily` القيمة `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:169]

```
170:                             fontWeight = FontWeight.Bold
```
> يُسنِد للخاصية `fontWeight` القيمة `FontWeight.Bold`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:170]

```
171:                         ),
```
> إغلاق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:171]

```
172:                         modifier = Modifier.padding(vertical = 4.dp)
```
> يُسنِد للوسيط `modifier` القيمة `Modifier.padding(vertical = 4.dp)` أي حشو رأسي قدره 4 وحدات dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:172]

```
173:                     )
```
> إغلاق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:173]

```
174:                 }
```
> إغلاق نطاق المُركِّب `Button`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:174]

```
175: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:175]

```
176:                 OutlinedButton(
```
> يستدعي المُركِّب `OutlinedButton` (زر محدّد بالحدّ) وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:176]

```
177:                     onClick = onRetry,
```
> يُسنِد للوسيط `onClick` القيمة `onRetry`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:177]

```
178:                     modifier = Modifier.fillMaxWidth()
```
> يُسنِد للوسيط `modifier` القيمة `Modifier.fillMaxWidth()`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:178]

```
179:                 ) {
```
> إغلاق وُسطاء `OutlinedButton` وبداية جسم المُركِّب. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:179]

```
180:                         Text(
```
> يستدعي المُركِّب `Text` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:180]

```
181:                             text = stringResource(R.string.check_again),
```
> يُسنِد للوسيط `text` نص المورد `R.string.check_again`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:181]

```
182:                         style = MaterialTheme.typography.bodyMedium.copy(
```
> يُسنِد للوسيط `style` نسخةً مُعدَّلة من `MaterialTheme.typography.bodyMedium` وبداية تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:182]

```
183:                             fontFamily = FontFamily.Monospace
```
> يُسنِد للخاصية `fontFamily` القيمة `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:183]

```
184:                         ),
```
> إغلاق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:184]

```
185:                         modifier = Modifier.padding(vertical = 4.dp)
```
> يُسنِد للوسيط `modifier` القيمة `Modifier.padding(vertical = 4.dp)` أي حشو رأسي قدره 4 وحدات dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:185]

```
186:                     )
```
> إغلاق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:186]

```
187:                 }
```
> إغلاق نطاق المُركِّب `OutlinedButton`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:187]

```
188:             }
```
> إغلاق نطاق المُركِّب `Column` في فرع `else`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:188]

```
189:         }
```
> إغلاق نطاق `else`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:189]

```
190:     }
```
> إغلاق نطاق المُركِّب `Column` الخارجي. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:190]

```
191: }
```
> إغلاق نطاق الدالة `LocationDisabledContent`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:191]

```
192: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:192]

```
193: @Composable
```
> يضع التعليق التوصيفي `@Composable` على الدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:193]

```
194: private fun LocationNotAvailableContent(
```
> يُعرِّف دالة خاصة (private) باسم `LocationNotAvailableContent` (محتوى الموقع غير المتاح) وبداية قائمة وُسطائها. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:194]

```
195:     colorScheme: ColorScheme
```
> يُعرِّف الوسيط `colorScheme` من النوع `ColorScheme`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:195]

```
196: ) {
```
> إغلاق قائمة الوُسطاء وبداية جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:196]

```
197:     Column(
```
> يستدعي المُركِّب `Column` وبداية وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:197]

```
198:         verticalArrangement = Arrangement.spacedBy(24.dp),
```
> يُسنِد للوسيط `verticalArrangement` القيمة `Arrangement.spacedBy(24.dp)` أي تباعد 24 وحدة dp. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:198]

```
199:         horizontalAlignment = Alignment.CenterHorizontally
```
> يُسنِد للوسيط `horizontalAlignment` القيمة `Alignment.CenterHorizontally`. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:199]

```
200:     ) {
```
> إغلاق وُسطاء `Column` وبداية جسم المُركِّب. [app/src/main/java/com/bitchat/android/onboarding/LocationCheckScreen.kt:200]
