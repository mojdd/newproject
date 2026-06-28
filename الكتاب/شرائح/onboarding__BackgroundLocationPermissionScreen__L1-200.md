# شريحة — app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt (الأسطر 1–200)

```
1: package com.bitchat.android.onboarding
```
> يُعلِن أن هذا الملف ينتمي إلى الحُزمة (package) باسم `com.bitchat.android.onboarding`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:2]

```
3: import androidx.compose.foundation.layout.Arrangement
```
> يستورد (import) الكائن `Arrangement` من حزمة تخطيط Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:3]

```
4: import androidx.compose.foundation.layout.Box
```
> يستورد العنصر `Box` (صندوق) من حزمة تخطيط Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:4]

```
5: import androidx.compose.foundation.layout.Column
```
> يستورد العنصر `Column` (عمود) من حزمة تخطيط Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:5]

```
6: import androidx.compose.foundation.layout.Row
```
> يستورد العنصر `Row` (صف) من حزمة تخطيط Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:6]

```
7: import androidx.compose.foundation.layout.Spacer
```
> يستورد العنصر `Spacer` (فاصل) من حزمة تخطيط Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:7]

```
8: import androidx.compose.foundation.layout.fillMaxSize
```
> يستورد المُعدِّل `fillMaxSize` (ملء كامل الحجم) من حزمة تخطيط Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:8]

```
9: import androidx.compose.foundation.layout.fillMaxWidth
```
> يستورد المُعدِّل `fillMaxWidth` (ملء كامل العرض) من حزمة تخطيط Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:9]

```
10: import androidx.compose.foundation.layout.height
```
> يستورد المُعدِّل `height` (الارتفاع) من حزمة تخطيط Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:10]

```
11: import androidx.compose.foundation.layout.padding
```
> يستورد المُعدِّل `padding` (الحشو) من حزمة تخطيط Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:11]

```
12: import androidx.compose.foundation.layout.size
```
> يستورد المُعدِّل `size` (الحجم) من حزمة تخطيط Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:12]

```
13: import androidx.compose.foundation.rememberScrollState
```
> يستورد الدالة `rememberScrollState` (تذكّر حالة التمرير) من حزمة foundation في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:13]

```
14: import androidx.compose.foundation.shape.RoundedCornerShape
```
> يستورد الشكل `RoundedCornerShape` (شكل بزوايا مُدوّرة) من حزمة الأشكال في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:14]

```
15: import androidx.compose.foundation.verticalScroll
```
> يستورد المُعدِّل `verticalScroll` (التمرير العمودي) من حزمة foundation في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:15]

```
16: import androidx.compose.material.icons.Icons
```
> يستورد الكائن `Icons` (الأيقونات) من حزمة material في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:16]

```
17: import androidx.compose.material.icons.filled.LocationOn
```
> يستورد الأيقونة `LocationOn` (الموقع مُفعّل) من حزمة الأيقونات المملوءة في material. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:17]

```
18: import androidx.compose.material.icons.filled.Security
```
> يستورد الأيقونة `Security` (الأمان) من حزمة الأيقونات المملوءة في material. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:18]

```
19: import androidx.compose.material3.Button
```
> يستورد العنصر `Button` (زر) من حزمة material3. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:19]

```
20: import androidx.compose.material3.ButtonDefaults
```
> يستورد الكائن `ButtonDefaults` (القيم الافتراضية للزر) من حزمة material3. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:20]

```
21: import androidx.compose.material3.ColorScheme
```
> يستورد النوع `ColorScheme` (مخطط الألوان) من حزمة material3. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:21]

```
22: import androidx.compose.material3.Icon
```
> يستورد العنصر `Icon` (أيقونة) من حزمة material3. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:22]

```
23: import androidx.compose.material3.MaterialTheme
```
> يستورد الكائن `MaterialTheme` (سمة ماتيريال) من حزمة material3. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:23]

```
24: import androidx.compose.material3.OutlinedButton
```
> يستورد العنصر `OutlinedButton` (زر مُحاط بإطار) من حزمة material3. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:24]

```
25: import androidx.compose.material3.Surface
```
> يستورد العنصر `Surface` (سطح) من حزمة material3. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:25]

```
26: import androidx.compose.material3.Text
```
> يستورد العنصر `Text` (نص) من حزمة material3. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:26]

```
27: import androidx.compose.material3.TextButton
```
> يستورد العنصر `TextButton` (زر نصّي) من حزمة material3. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:27]

```
28: import androidx.compose.runtime.Composable
```
> يستورد التعليق التوضيحي `Composable` (قابل للتركيب) من حزمة runtime في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:28]

```
29: import androidx.compose.ui.Alignment
```
> يستورد الكائن `Alignment` (المحاذاة) من حزمة ui في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:29]

```
30: import androidx.compose.ui.Modifier
```
> يستورد النوع `Modifier` (المُعدِّل) من حزمة ui في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:30]

```
31: import androidx.compose.ui.text.font.FontFamily
```
> يستورد النوع `FontFamily` (عائلة الخط) من حزمة الخطوط في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:31]

```
32: import androidx.compose.ui.text.font.FontWeight
```
> يستورد النوع `FontWeight` (وزن الخط) من حزمة الخطوط في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:32]

```
33: import androidx.compose.ui.unit.dp
```
> يستورد الوحدة `dp` (بكسل مستقل عن الكثافة) من حزمة الوحدات في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:33]

```
34: import androidx.compose.ui.unit.sp
```
> يستورد الوحدة `sp` (بكسل قابل للتحجيم) من حزمة الوحدات في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:34]

```
35: import androidx.compose.ui.res.stringResource
```
> يستورد الدالة `stringResource` (مورد نصّي) من حزمة الموارد في Compose. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:35]

```
36: import com.bitchat.android.R
```
> يستورد فئة الموارد `R` من حزمة `com.bitchat.android`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:36]

```
37: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:37]

```
38: /**
```
> تعليق: بداية كتلة توثيق (تعليق توثيقي). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:38]

```
39:  * Explanation screen shown before requesting background location permission.
```
> تعليق: شاشة شرح تُعرَض قبل طلب إذن الموقع في الخلفية. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:39]

```
40:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:40]

```
41: @Composable
```
> يضع التعليق التوضيحي `@Composable` على الدالة التالية ليجعلها قابلة للتركيب. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:41]

```
42: fun BackgroundLocationPermissionScreen(
```
> يُعرِّف الدالة `BackgroundLocationPermissionScreen` (شاشة إذن موقع الخلفية) ويبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:42]

```
43:     modifier: Modifier,
```
> يُعرِّف المعامل `modifier` من النوع `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:43]

```
44:     onContinue: () -> Unit,
```
> يُعرِّف المعامل `onContinue` (عند المتابعة) دالةً لا تأخذ وسائط وتُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:44]

```
45:     onRetry: () -> Unit,
```
> يُعرِّف المعامل `onRetry` (عند إعادة المحاولة) دالةً لا تأخذ وسائط وتُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:45]

```
46:     onSkip: () -> Unit
```
> يُعرِّف المعامل `onSkip` (عند التخطّي) دالةً لا تأخذ وسائط وتُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:46]

```
47: ) {
```
> يُغلق قائمة المعاملات ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:47]

```
48:     val colorScheme = MaterialTheme.colorScheme
```
> يُعرِّف المتغيّر الثابت `colorScheme` ويُسنِد إليه `MaterialTheme.colorScheme` (مخطط ألوان السمة الحالية). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:48]

```
49:     val scrollState = rememberScrollState()
```
> يُعرِّف المتغيّر الثابت `scrollState` ويُسنِد إليه ناتج استدعاء `rememberScrollState()`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:49]

```
50: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:50]

```
51:     Box(modifier = modifier) {
```
> يستدعي العنصر `Box` مُمرِّراً إليه المعامل `modifier` بقيمة المتغيّر `modifier`، ويفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:51]

```
52:         Column(
```
> يستدعي العنصر `Column` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:52]

```
53:             modifier = Modifier
```
> يُسنِد المعامل `modifier` إلى مُعدِّل يبدأ من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:53]

```
54:                 .fillMaxSize()
```
> يربط المُعدِّل `fillMaxSize()` ليملأ كامل الحجم المتاح. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:54]

```
55:                 .padding(horizontal = 24.dp)
```
> يربط المُعدِّل `padding` بحشو أفقي مقداره `24.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:55]

```
56:                 .padding(bottom = 88.dp)
```
> يربط المُعدِّل `padding` بحشو سفلي مقداره `88.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:56]

```
57:                 .verticalScroll(scrollState),
```
> يربط المُعدِّل `verticalScroll` مُمرِّراً إليه `scrollState`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:57]

```
58:             verticalArrangement = Arrangement.spacedBy(16.dp)
```
> يُسنِد المعامل `verticalArrangement` إلى `Arrangement.spacedBy(16.dp)` (ترتيب عمودي بمسافة 16.dp). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:58]

```
59:         ) {
```
> يُغلق وسائط `Column` ويفتح كتلة محتواها. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:59]

```
60:             Spacer(modifier = Modifier.height(24.dp))
```
> يستدعي العنصر `Spacer` بمُعدِّل ارتفاع `24.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:60]

```
61: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:61]

```
62:             HeaderSection(colorScheme)
```
> يستدعي الدالة `HeaderSection` (قسم الترويسة) مُمرِّراً إليها `colorScheme`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:62]

```
63: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:63]

```
64:             Surface(
```
> يستدعي العنصر `Surface` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:64]

```
65:                 modifier = Modifier.fillMaxWidth(),
```
> يُسنِد المعامل `modifier` إلى `Modifier.fillMaxWidth()` ليملأ كامل العرض. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:65]

```
66:                 color = colorScheme.surfaceVariant.copy(alpha = 0.25f),
```
> يُسنِد المعامل `color` إلى `colorScheme.surfaceVariant` بنسخة شفافيتها `alpha = 0.25f`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:66]

```
67:                 shape = RoundedCornerShape(12.dp)
```
> يُسنِد المعامل `shape` إلى `RoundedCornerShape(12.dp)` (زوايا مُدوّرة نصف قطرها 12.dp). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:67]

```
68:             ) {
```
> يُغلق وسائط `Surface` ويفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:68]

```
69:                 Column(
```
> يستدعي العنصر `Column` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:69]

```
70:                     modifier = Modifier.padding(16.dp),
```
> يُسنِد المعامل `modifier` إلى `Modifier.padding(16.dp)` (حشو 16.dp من كل الجوانب). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:70]

```
71:                     verticalArrangement = Arrangement.spacedBy(8.dp)
```
> يُسنِد المعامل `verticalArrangement` إلى `Arrangement.spacedBy(8.dp)`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:71]

```
72:                 ) {
```
> يُغلق وسائط `Column` ويفتح كتلة محتواها. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:72]

```
73:                     Row(
```
> يستدعي العنصر `Row` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:73]

```
74:                         verticalAlignment = Alignment.Top,
```
> يُسنِد المعامل `verticalAlignment` إلى `Alignment.Top` (محاذاة عمودية للأعلى). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:74]

```
75:                         horizontalArrangement = Arrangement.spacedBy(12.dp)
```
> يُسنِد المعامل `horizontalArrangement` إلى `Arrangement.spacedBy(12.dp)`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:75]

```
76:                     ) {
```
> يُغلق وسائط `Row` ويفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:76]

```
77:                         Icon(
```
> يستدعي العنصر `Icon` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:77]

```
78:                             imageVector = Icons.Filled.LocationOn,
```
> يُسنِد المعامل `imageVector` إلى الأيقونة `Icons.Filled.LocationOn`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:78]

```
79:                             contentDescription = stringResource(R.string.cd_location_services),
```
> يُسنِد المعامل `contentDescription` إلى نص المورد `R.string.cd_location_services`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:79]

```
80:                             tint = colorScheme.primary,
```
> يُسنِد المعامل `tint` (لون التظليل) إلى `colorScheme.primary`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:80]

```
81:                             modifier = Modifier
```
> يُسنِد المعامل `modifier` إلى مُعدِّل يبدأ من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:81]

```
82:                                 .padding(top = 2.dp)
```
> يربط المُعدِّل `padding` بحشو علوي مقداره `2.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:82]

```
83:                                 .size(20.dp)
```
> يربط المُعدِّل `size` بحجم `20.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:83]

```
84:                         )
```
> يُغلق استدعاء `Icon`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:84]

```
85:                         Column {
```
> يستدعي العنصر `Column` ويفتح كتلة محتواه بلا وسائط صريحة. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:85]

```
86:                             Text(
```
> يستدعي العنصر `Text` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:86]

```
87:                                 text = stringResource(R.string.background_location_required_title),
```
> يُسنِد المعامل `text` إلى نص المورد `R.string.background_location_required_title`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:87]

```
88:                                 style = MaterialTheme.typography.titleMedium,
```
> يُسنِد المعامل `style` إلى `MaterialTheme.typography.titleMedium`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:88]

```
89:                                 fontWeight = FontWeight.Medium,
```
> يُسنِد المعامل `fontWeight` إلى `FontWeight.Medium`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:89]

```
90:                                 color = colorScheme.onBackground
```
> يُسنِد المعامل `color` إلى `colorScheme.onBackground`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:90]

```
91:                             )
```
> يُغلق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:91]

```
92:                             Spacer(modifier = Modifier.height(4.dp))
```
> يستدعي العنصر `Spacer` بمُعدِّل ارتفاع `4.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:92]

```
93:                             Text(
```
> يستدعي العنصر `Text` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:93]

```
94:                                 text = stringResource(R.string.background_location_explanation),
```
> يُسنِد المعامل `text` إلى نص المورد `R.string.background_location_explanation`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:94]

```
95:                                 style = MaterialTheme.typography.bodySmall,
```
> يُسنِد المعامل `style` إلى `MaterialTheme.typography.bodySmall`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:95]

```
96:                                 color = colorScheme.onBackground.copy(alpha = 0.8f)
```
> يُسنِد المعامل `color` إلى `colorScheme.onBackground` بنسخة شفافيتها `alpha = 0.8f`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:96]

```
97:                             )
```
> يُغلق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:97]

```
98:                             Spacer(modifier = Modifier.height(8.dp))
```
> يستدعي العنصر `Spacer` بمُعدِّل ارتفاع `8.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:98]

```
99:                             Text(
```
> يستدعي العنصر `Text` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:99]

```
100:                                 text = stringResource(R.string.background_location_settings_tip),
```
> يُسنِد المعامل `text` إلى نص المورد `R.string.background_location_settings_tip`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:100]

```
101:                                 style = MaterialTheme.typography.bodySmall.copy(
```
> يُسنِد المعامل `style` إلى نسخة من `MaterialTheme.typography.bodySmall` ويبدأ تعديل خصائصها. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:101]

```
102:                                     fontFamily = FontFamily.Monospace
```
> يُسنِد داخل النسخة الخاصية `fontFamily` إلى `FontFamily.Monospace` (خط ثابت العرض). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:102]

```
103:                                 ),
```
> يُغلق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:103]

```
104:                                 color = colorScheme.onBackground.copy(alpha = 0.8f)
```
> يُسنِد المعامل `color` إلى `colorScheme.onBackground` بنسخة شفافيتها `alpha = 0.8f`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:104]

```
105:                             )
```
> يُغلق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:105]

```
106:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:106]

```
107:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:107]

```
108:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:108]

```
109:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:109]

```
110: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:110]

```
111:             Surface(
```
> يستدعي العنصر `Surface` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:111]

```
112:                 modifier = Modifier.fillMaxWidth(),
```
> يُسنِد المعامل `modifier` إلى `Modifier.fillMaxWidth()` ليملأ كامل العرض. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:112]

```
113:                 color = colorScheme.surfaceVariant.copy(alpha = 0.25f),
```
> يُسنِد المعامل `color` إلى `colorScheme.surfaceVariant` بنسخة شفافيتها `alpha = 0.25f`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:113]

```
114:                 shape = RoundedCornerShape(12.dp)
```
> يُسنِد المعامل `shape` إلى `RoundedCornerShape(12.dp)`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:114]

```
115:             ) {
```
> يُغلق وسائط `Surface` ويفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:115]

```
116:                 Column(
```
> يستدعي العنصر `Column` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:116]

```
117:                     modifier = Modifier.padding(16.dp),
```
> يُسنِد المعامل `modifier` إلى `Modifier.padding(16.dp)`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:117]

```
118:                     verticalArrangement = Arrangement.spacedBy(8.dp)
```
> يُسنِد المعامل `verticalArrangement` إلى `Arrangement.spacedBy(8.dp)`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:118]

```
119:                 ) {
```
> يُغلق وسائط `Column` ويفتح كتلة محتواها. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:119]

```
120:                     Row(
```
> يستدعي العنصر `Row` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:120]

```
121:                         verticalAlignment = Alignment.Top,
```
> يُسنِد المعامل `verticalAlignment` إلى `Alignment.Top`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:121]

```
122:                         horizontalArrangement = Arrangement.spacedBy(12.dp)
```
> يُسنِد المعامل `horizontalArrangement` إلى `Arrangement.spacedBy(12.dp)`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:122]

```
123:                     ) {
```
> يُغلق وسائط `Row` ويفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:123]

```
124:                         Icon(
```
> يستدعي العنصر `Icon` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:124]

```
125:                             imageVector = Icons.Filled.Security,
```
> يُسنِد المعامل `imageVector` إلى الأيقونة `Icons.Filled.Security`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:125]

```
126:                             contentDescription = stringResource(R.string.cd_privacy_protected),
```
> يُسنِد المعامل `contentDescription` إلى نص المورد `R.string.cd_privacy_protected`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:126]

```
127:                             tint = colorScheme.primary,
```
> يُسنِد المعامل `tint` إلى `colorScheme.primary`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:127]

```
128:                             modifier = Modifier
```
> يُسنِد المعامل `modifier` إلى مُعدِّل يبدأ من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:128]

```
129:                                 .padding(top = 2.dp)
```
> يربط المُعدِّل `padding` بحشو علوي مقداره `2.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:129]

```
130:                                 .size(20.dp)
```
> يربط المُعدِّل `size` بحجم `20.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:130]

```
131:                         )
```
> يُغلق استدعاء `Icon`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:131]

```
132:                         Column {
```
> يستدعي العنصر `Column` ويفتح كتلة محتواه بلا وسائط صريحة. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:132]

```
133:                             Text(
```
> يستدعي العنصر `Text` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:133]

```
134:                                 text = stringResource(R.string.background_location_needs_for),
```
> يُسنِد المعامل `text` إلى نص المورد `R.string.background_location_needs_for`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:134]

```
135:                                 style = MaterialTheme.typography.titleMedium,
```
> يُسنِد المعامل `style` إلى `MaterialTheme.typography.titleMedium`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:135]

```
136:                                 fontWeight = FontWeight.Medium,
```
> يُسنِد المعامل `fontWeight` إلى `FontWeight.Medium`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:136]

```
137:                                 color = colorScheme.onBackground
```
> يُسنِد المعامل `color` إلى `colorScheme.onBackground`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:137]

```
138:                             )
```
> يُغلق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:138]

```
139:                             Spacer(modifier = Modifier.height(4.dp))
```
> يستدعي العنصر `Spacer` بمُعدِّل ارتفاع `4.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:139]

```
140:                             Text(
```
> يستدعي العنصر `Text` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:140]

```
141:                                 text = stringResource(R.string.background_location_needs_bullets),
```
> يُسنِد المعامل `text` إلى نص المورد `R.string.background_location_needs_bullets`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:141]

```
142:                                 style = MaterialTheme.typography.bodySmall,
```
> يُسنِد المعامل `style` إلى `MaterialTheme.typography.bodySmall`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:142]

```
143:                                 fontFamily = FontFamily.Monospace,
```
> يُسنِد المعامل `fontFamily` إلى `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:143]

```
144:                                 color = colorScheme.onBackground.copy(alpha = 0.8f)
```
> يُسنِد المعامل `color` إلى `colorScheme.onBackground` بنسخة شفافيتها `alpha = 0.8f`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:144]

```
145:                             )
```
> يُغلق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:145]

```
146:                             Spacer(modifier = Modifier.height(8.dp))
```
> يستدعي العنصر `Spacer` بمُعدِّل ارتفاع `8.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:146]

```
147:                             Text(
```
> يستدعي العنصر `Text` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:147]

```
148:                                 text = stringResource(R.string.background_location_privacy_note),
```
> يُسنِد المعامل `text` إلى نص المورد `R.string.background_location_privacy_note`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:148]

```
149:                                 style = MaterialTheme.typography.bodySmall.copy(
```
> يُسنِد المعامل `style` إلى نسخة من `MaterialTheme.typography.bodySmall` ويبدأ تعديل خصائصها. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:149]

```
150:                                     fontFamily = FontFamily.Monospace,
```
> يُسنِد داخل النسخة الخاصية `fontFamily` إلى `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:150]

```
151:                                     fontWeight = FontWeight.Medium
```
> يُسنِد داخل النسخة الخاصية `fontWeight` إلى `FontWeight.Medium`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:151]

```
152:                                 ),
```
> يُغلق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:152]

```
153:                                 color = colorScheme.onBackground
```
> يُسنِد المعامل `color` إلى `colorScheme.onBackground`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:153]

```
154:                             )
```
> يُغلق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:154]

```
155:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:155]

```
156:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:156]

```
157:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:157]

```
158:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:158]

```
159: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:159]

```
160:             Spacer(modifier = Modifier.height(24.dp))
```
> يستدعي العنصر `Spacer` بمُعدِّل ارتفاع `24.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:160]

```
161:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:161]

```
162: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:162]

```
163:         Surface(
```
> يستدعي العنصر `Surface` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:163]

```
164:             modifier = Modifier
```
> يُسنِد المعامل `modifier` إلى مُعدِّل يبدأ من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:164]

```
165:                 .align(Alignment.BottomCenter)
```
> يربط المُعدِّل `align` بمحاذاة `Alignment.BottomCenter` (أسفل الوسط). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:165]

```
166:                 .fillMaxWidth(),
```
> يربط المُعدِّل `fillMaxWidth()` ليملأ كامل العرض. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:166]

```
167:             color = colorScheme.surface,
```
> يُسنِد المعامل `color` إلى `colorScheme.surface`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:167]

```
168:             shadowElevation = 8.dp
```
> يُسنِد المعامل `shadowElevation` (ارتفاع الظل) إلى `8.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:168]

```
169:         ) {
```
> يُغلق وسائط `Surface` ويفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:169]

```
170:             Column(
```
> يستدعي العنصر `Column` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:170]

```
171:                 modifier = Modifier
```
> يُسنِد المعامل `modifier` إلى مُعدِّل يبدأ من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:171]

```
172:                     .fillMaxWidth()
```
> يربط المُعدِّل `fillMaxWidth()` ليملأ كامل العرض. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:172]

```
173:                     .padding(horizontal = 24.dp, vertical = 16.dp),
```
> يربط المُعدِّل `padding` بحشو أفقي `24.dp` وحشو عمودي `16.dp`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:173]

```
174:                 verticalArrangement = Arrangement.spacedBy(12.dp)
```
> يُسنِد المعامل `verticalArrangement` إلى `Arrangement.spacedBy(12.dp)`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:174]

```
175:             ) {
```
> يُغلق وسائط `Column` ويفتح كتلة محتواها. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:175]

```
176:                 Button(
```
> يستدعي العنصر `Button` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:176]

```
177:                     onClick = onContinue,
```
> يُسنِد المعامل `onClick` إلى الدالة `onContinue`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:177]

```
178:                     modifier = Modifier.fillMaxWidth(),
```
> يُسنِد المعامل `modifier` إلى `Modifier.fillMaxWidth()`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:178]

```
179:                     colors = ButtonDefaults.buttonColors(
```
> يُسنِد المعامل `colors` إلى استدعاء `ButtonDefaults.buttonColors` ويبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:179]

```
180:                         containerColor = colorScheme.primary
```
> يُسنِد المعامل `containerColor` (لون الحاوية) إلى `colorScheme.primary`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:180]

```
181:                     )
```
> يُغلق استدعاء `ButtonDefaults.buttonColors`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:181]

```
182:                 ) {
```
> يُغلق وسائط `Button` ويفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:182]

```
183:                     Text(
```
> يستدعي العنصر `Text` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:183]

```
184:                         text = stringResource(R.string.grant_background_location),
```
> يُسنِد المعامل `text` إلى نص المورد `R.string.grant_background_location`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:184]

```
185:                         style = MaterialTheme.typography.bodyMedium.copy(
```
> يُسنِد المعامل `style` إلى نسخة من `MaterialTheme.typography.bodyMedium` ويبدأ تعديل خصائصها. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:185]

```
186:                             fontFamily = FontFamily.Monospace,
```
> يُسنِد داخل النسخة الخاصية `fontFamily` إلى `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:186]

```
187:                             fontWeight = FontWeight.Bold
```
> يُسنِد داخل النسخة الخاصية `fontWeight` إلى `FontWeight.Bold`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:187]

```
188:                         ),
```
> يُغلق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:188]

```
189:                         modifier = Modifier.padding(vertical = 4.dp)
```
> يُسنِد المعامل `modifier` إلى `Modifier.padding(vertical = 4.dp)` (حشو عمودي 4.dp). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:189]

```
190:                     )
```
> يُغلق استدعاء `Text`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:190]

```
191:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:191]

```
192: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:192]

```
193:                 Row(
```
> يستدعي العنصر `Row` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:193]

```
194:                     modifier = Modifier.fillMaxWidth(),
```
> يُسنِد المعامل `modifier` إلى `Modifier.fillMaxWidth()`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:194]

```
195:                     horizontalArrangement = Arrangement.spacedBy(12.dp)
```
> يُسنِد المعامل `horizontalArrangement` إلى `Arrangement.spacedBy(12.dp)`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:195]

```
196:                 ) {
```
> يُغلق وسائط `Row` ويفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:196]

```
197:                     OutlinedButton(
```
> يستدعي العنصر `OutlinedButton` ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:197]

```
198:                         onClick = onRetry,
```
> يُسنِد المعامل `onClick` إلى الدالة `onRetry`. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:198]

```
199:                         modifier = Modifier.weight(1f)
```
> يُسنِد المعامل `modifier` إلى `Modifier.weight(1f)` (وزن نسبي 1). [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:199]

```
200:                     ) {
```
> يُغلق وسائط `OutlinedButton` ويفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BackgroundLocationPermissionScreen.kt:200]
