# شريحة — app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt (الأسطر 1–200)

```
1: package com.bitchat.android.onboarding
```
> يُعلِن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.onboarding`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:2]

```
3: import androidx.compose.animation.core.*
```
> يستورد (import) كل العناصر من حزمة نواة الحركة `androidx.compose.animation.core`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:3]

```
4: import androidx.compose.foundation.layout.*
```
> يستورد كل عناصر التخطيط (layout) من `androidx.compose.foundation.layout`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:4]

```
5: import androidx.compose.material3.*
```
> يستورد كل عناصر مكتبة التصميم `material3`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:5]

```
6: import androidx.compose.runtime.*
```
> يستورد كل عناصر زمن التشغيل (runtime) من `androidx.compose.runtime`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:6]

```
7: import androidx.compose.ui.Alignment
```
> يستورد العنصر `Alignment` (المحاذاة). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:7]

```
8: import androidx.compose.ui.Modifier
```
> يستورد العنصر `Modifier` (المُعدِّل). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:8]

```
9: import androidx.compose.ui.draw.rotate
```
> يستورد الدالة `rotate` (التدوير) من حزمة الرسم. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:9]

```
10: import androidx.compose.ui.graphics.Color
```
> يستورد العنصر `Color` (اللون). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:10]

```
11: import androidx.compose.ui.text.font.FontFamily
```
> يستورد العنصر `FontFamily` (عائلة الخط). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:11]

```
12: import androidx.compose.ui.text.font.FontWeight
```
> يستورد العنصر `FontWeight` (وزن الخط). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:12]

```
13: import androidx.compose.ui.text.style.TextAlign
```
> يستورد العنصر `TextAlign` (محاذاة النص). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:13]

```
14: import androidx.compose.ui.unit.dp
```
> يستورد الوحدة `dp` (البكسل المستقل عن الكثافة). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:14]

```
15: import androidx.compose.ui.res.stringResource
```
> يستورد الدالة `stringResource` (مورد النص). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:15]

```
16: import com.bitchat.android.R
```
> يستورد فئة الموارد `R` الخاصة بالتطبيق `com.bitchat.android`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:17]

```
18: /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:18]

```
19:  * Loading screen shown during app initialization after permissions are granted
```
> تعليق: شاشة التحميل التي تُعرض أثناء تهيئة التطبيق بعد منح الأذونات. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:19]

```
20:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:20]

```
21: @Composable
```
> يضع التعليق التوضيحي `@Composable` على الدالة التالية ليجعلها دالة قابلة للتركيب (Composable). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:21]

```
22: fun InitializingScreen(modifier: Modifier) {
```
> يُعرِّف الدالة `InitializingScreen` (شاشة التهيئة) التي تأخذ مُعاملاً واحداً اسمه `modifier` من نوع `Modifier`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:22]

```
23:     val colorScheme = MaterialTheme.colorScheme
```
> يُعرِّف متغيّراً ثابتاً اسمه `colorScheme` (مخطط الألوان) ويُسنِد إليه `MaterialTheme.colorScheme`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:23]

```
24:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:24]

```
25:     // Animated rotation for the loading indicator
```
> تعليق: تدوير متحرّك لمؤشّر التحميل. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:25]

```
26:     val infiniteTransition = rememberInfiniteTransition(label = "loading")
```
> يُعرِّف متغيّراً ثابتاً اسمه `infiniteTransition` (الانتقال اللانهائي) ويُسنِد إليه ناتج `rememberInfiniteTransition` مع المُعامل `label` بقيمة `"loading"`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:26]

```
27:     val rotationAngle by infiniteTransition.animateFloat(
```
> يُعرِّف متغيّراً ثابتاً اسمه `rotationAngle` (زاوية التدوير) عبر التفويض `by` إلى ناتج استدعاء `infiniteTransition.animateFloat`، ويفتح قائمة المُعاملات. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:27]

```
28:         initialValue = 0f,
```
> يضبط المُعامل `initialValue` (القيمة الابتدائية) على `0f`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:28]

```
29:         targetValue = 360f,
```
> يضبط المُعامل `targetValue` (القيمة الهدف) على `360f`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:29]

```
30:         animationSpec = infiniteRepeatable(
```
> يضبط المُعامل `animationSpec` (مواصفة الحركة) على ناتج استدعاء `infiniteRepeatable`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:30]

```
31:             animation = tween(durationMillis = 2000, easing = LinearEasing),
```
> يضبط المُعامل `animation` على ناتج `tween` مع المُعامل `durationMillis` بقيمة `2000` والمُعامل `easing` بقيمة `LinearEasing` (تخفيف خطّي). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:31]

```
32:             repeatMode = RepeatMode.Restart
```
> يضبط المُعامل `repeatMode` (نمط التكرار) على `RepeatMode.Restart` (إعادة البدء). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:32]

```
33:         ),
```
> إغلاق قائمة مُعاملات `infiniteRepeatable`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:33]

```
34:         label = "rotation"
```
> يضبط المُعامل `label` على `"rotation"`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:34]

```
35:     )
```
> إغلاق قائمة مُعاملات `animateFloat`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:36]

```
37:     // Animated dots for loading text
```
> تعليق: نقاط متحرّكة لنص التحميل. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:37]

```
38:     val dotCount = 3
```
> يُعرِّف متغيّراً ثابتاً اسمه `dotCount` (عدد النقاط) ويُسنِد إليه القيمة `3`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:38]

```
39:     val animationDelay = 300
```
> يُعرِّف متغيّراً ثابتاً اسمه `animationDelay` (تأخير الحركة) ويُسنِد إليه القيمة `300`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:39]

```
40:     val dots = (0 until dotCount).map { index ->
```
> يُعرِّف متغيّراً ثابتاً اسمه `dots` (النقاط) ويُسنِد إليه ناتج تطبيق `map` على المدى `(0 until dotCount)` بمُعامل لامبدا اسمه `index`، ويفتح جسم اللامبدا. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:40]

```
41:         val alpha by infiniteTransition.animateFloat(
```
> يُعرِّف متغيّراً ثابتاً اسمه `alpha` (الشفافية) عبر التفويض `by` إلى ناتج `infiniteTransition.animateFloat`، ويفتح قائمة المُعاملات. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:41]

```
42:             initialValue = 0.3f,
```
> يضبط المُعامل `initialValue` على `0.3f`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:42]

```
43:             targetValue = 1f,
```
> يضبط المُعامل `targetValue` على `1f`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:43]

```
44:             animationSpec = infiniteRepeatable(
```
> يضبط المُعامل `animationSpec` على ناتج `infiniteRepeatable`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:44]

```
45:                 animation = tween(durationMillis = animationDelay * dotCount),
```
> يضبط المُعامل `animation` على ناتج `tween` مع المُعامل `durationMillis` بقيمة حاصل ضرب `animationDelay * dotCount`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:45]

```
46:                 repeatMode = RepeatMode.Reverse,
```
> يضبط المُعامل `repeatMode` على `RepeatMode.Reverse` (عكس). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:46]

```
47:                 initialStartOffset = StartOffset(animationDelay * index)
```
> يضبط المُعامل `initialStartOffset` (إزاحة البدء الابتدائية) على `StartOffset` بقيمة حاصل ضرب `animationDelay * index`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:47]

```
48:             ),
```
> إغلاق قائمة مُعاملات `infiniteRepeatable`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:48]

```
49:             label = "dot_$index"
```
> يضبط المُعامل `label` على سلسلة نصّية `"dot_$index"` تدمج قيمة `index`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:49]

```
50:         )
```
> إغلاق قائمة مُعاملات `animateFloat`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:50]

```
51:         alpha
```
> يُرجِع قيمة `alpha` كناتج للامبدا. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:51]

```
52:     }
```
> إغلاق جسم لامبدا الدالة `map`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:52]

```
53: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:53]

```
54:     Box(
```
> يستدعي العنصر القابل للتركيب `Box` (الصندوق)، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:54]

```
55:         modifier = modifier.padding(32.dp),
```
> يضبط المُعامل `modifier` على `modifier` المُمرَّر مع تطبيق `padding` (حشوة) بقيمة `32.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:55]

```
56:         contentAlignment = Alignment.Center
```
> يضبط المُعامل `contentAlignment` (محاذاة المحتوى) على `Alignment.Center` (المركز). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:56]

```
57:     ) {
```
> إغلاق قائمة مُعاملات `Box` وفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:57]

```
58:         Column(
```
> يستدعي العنصر القابل للتركيب `Column` (العمود)، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:58]

```
59:             verticalArrangement = Arrangement.spacedBy(32.dp),
```
> يضبط المُعامل `verticalArrangement` (الترتيب العمودي) على `Arrangement.spacedBy` بمسافة `32.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:59]

```
60:             horizontalAlignment = Alignment.CenterHorizontally
```
> يضبط المُعامل `horizontalAlignment` (المحاذاة الأفقية) على `Alignment.CenterHorizontally` (التوسيط الأفقي). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:60]

```
61:         ) {
```
> إغلاق قائمة مُعاملات `Column` وفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:61]

```
62:             // App title
```
> تعليق: عنوان التطبيق. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:62]

```
63:             Text(
```
> يستدعي العنصر القابل للتركيب `Text` (النص)، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:63]

```
64:                 text = stringResource(R.string.app_name),
```
> يضبط المُعامل `text` على ناتج `stringResource` للمورد `R.string.app_name`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:64]

```
65:                 style = MaterialTheme.typography.headlineLarge.copy(
```
> يضبط المُعامل `style` على نسخة معدَّلة من `MaterialTheme.typography.headlineLarge` عبر `copy`، ويفتح قائمة المُعاملات المعدَّلة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:65]

```
66:                     fontFamily = FontFamily.Monospace,
```
> يضبط المُعامل `fontFamily` على `FontFamily.Monospace` (الخط أحادي المسافة). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:66]

```
67:                     fontWeight = FontWeight.Bold,
```
> يضبط المُعامل `fontWeight` على `FontWeight.Bold` (عريض). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:67]

```
68:                     color = colorScheme.primary
```
> يضبط المُعامل `color` على `colorScheme.primary` (اللون الأساسي). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:68]

```
69:                 ),
```
> إغلاق قائمة مُعاملات `copy`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:69]

```
70:                 textAlign = TextAlign.Center
```
> يضبط المُعامل `textAlign` على `TextAlign.Center` (توسيط النص). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:70]

```
71:             )
```
> إغلاق قائمة مُعاملات `Text`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:71]

```
72: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:72]

```
73:             // Loading indicator
```
> تعليق: مؤشّر التحميل. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:73]

```
74:             Box(
```
> يستدعي العنصر القابل للتركيب `Box`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:74]

```
75:                 modifier = Modifier.size(60.dp),
```
> يضبط المُعامل `modifier` على `Modifier` مع تطبيق `size` (حجم) بقيمة `60.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:75]

```
76:                 contentAlignment = Alignment.Center
```
> يضبط المُعامل `contentAlignment` على `Alignment.Center`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:76]

```
77:             ) {
```
> إغلاق قائمة مُعاملات `Box` وفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:77]

```
78:                 CircularProgressIndicator(
```
> يستدعي العنصر القابل للتركيب `CircularProgressIndicator` (مؤشّر التقدّم الدائري)، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:78]

```
79:                     modifier = Modifier
```
> يضبط المُعامل `modifier` على `Modifier`، ويبدأ سلسلة استدعاءات عليه. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:79]

```
80:                         .fillMaxSize()
```
> يطبّق `fillMaxSize` (ملء أقصى حجم) على المُعدِّل. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:80]

```
81:                         .rotate(rotationAngle),
```
> يطبّق `rotate` (التدوير) بقيمة `rotationAngle` على المُعدِّل. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:81]

```
82:                     color = colorScheme.primary,
```
> يضبط المُعامل `color` على `colorScheme.primary`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:82]

```
83:                     strokeWidth = 3.dp
```
> يضبط المُعامل `strokeWidth` (عرض الخط) على `3.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:83]

```
84:                 )
```
> إغلاق قائمة مُعاملات `CircularProgressIndicator`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:84]

```
85:             }
```
> إغلاق كتلة محتوى `Box`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:85]

```
86: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:86]

```
87:             // Loading text with animated dots
```
> تعليق: نص التحميل مع نقاط متحرّكة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:87]

```
88:             Row(
```
> يستدعي العنصر القابل للتركيب `Row` (الصف)، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:88]

```
89:                 verticalAlignment = Alignment.CenterVertically,
```
> يضبط المُعامل `verticalAlignment` (المحاذاة العمودية) على `Alignment.CenterVertically` (التوسيط العمودي). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:89]

```
90:                 horizontalArrangement = Arrangement.Center
```
> يضبط المُعامل `horizontalArrangement` (الترتيب الأفقي) على `Arrangement.Center`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:90]

```
91:             ) {
```
> إغلاق قائمة مُعاملات `Row` وفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:91]

```
92:                 Text(
```
> يستدعي العنصر القابل للتركيب `Text`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:92]

```
93:                     text = stringResource(R.string.initializing_mesh_network),
```
> يضبط المُعامل `text` على ناتج `stringResource` للمورد `R.string.initializing_mesh_network`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:93]

```
94:                     style = MaterialTheme.typography.bodyLarge.copy(
```
> يضبط المُعامل `style` على نسخة معدَّلة من `MaterialTheme.typography.bodyLarge` عبر `copy`، ويفتح قائمة المُعاملات المعدَّلة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:94]

```
95:                         fontFamily = FontFamily.Monospace,
```
> يضبط المُعامل `fontFamily` على `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:95]

```
96:                         color = colorScheme.onSurface.copy(alpha = 0.7f)
```
> يضبط المُعامل `color` على `colorScheme.onSurface` بنسخة `copy` تضبط `alpha` على `0.7f`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:96]

```
97:                     )
```
> إغلاق قائمة مُعاملات `copy`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:97]

```
98:                 )
```
> إغلاق قائمة مُعاملات `Text`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:98]

```
99:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:99]

```
100:                 // Animated dots
```
> تعليق: نقاط متحرّكة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:100]

```
101:                 dots.forEach { alpha ->
```
> يستدعي `forEach` على `dots` بمُعامل لامبدا اسمه `alpha`، ويفتح جسم اللامبدا. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:101]

```
102:                     Text(
```
> يستدعي العنصر القابل للتركيب `Text`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:102]

```
103:                         text = stringResource(R.string.dot),
```
> يضبط المُعامل `text` على ناتج `stringResource` للمورد `R.string.dot`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:103]

```
104:                         style = MaterialTheme.typography.bodyLarge.copy(
```
> يضبط المُعامل `style` على نسخة معدَّلة من `MaterialTheme.typography.bodyLarge` عبر `copy`، ويفتح قائمة المُعاملات المعدَّلة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:104]

```
105:                             fontFamily = FontFamily.Monospace,
```
> يضبط المُعامل `fontFamily` على `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:105]

```
106:                             color = colorScheme.onSurface.copy(alpha = alpha)
```
> يضبط المُعامل `color` على `colorScheme.onSurface` بنسخة `copy` تضبط `alpha` على قيمة `alpha` المتحرّكة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:106]

```
107:                         )
```
> إغلاق قائمة مُعاملات `copy`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:107]

```
108:                     )
```
> إغلاق قائمة مُعاملات `Text`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:108]

```
109:                 }
```
> إغلاق جسم لامبدا `forEach`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:109]

```
110:             }
```
> إغلاق كتلة محتوى `Row`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:110]

```
111: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:111]

```
112:             Spacer(modifier = Modifier.height(16.dp))
```
> يستدعي العنصر القابل للتركيب `Spacer` (الفاصل) مع المُعامل `modifier` بقيمة `Modifier` بعد تطبيق `height` (ارتفاع) بقيمة `16.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:112]

```
113: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:113]

```
114:             // Status message
```
> تعليق: رسالة الحالة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:114]

```
115:             Card(
```
> يستدعي العنصر القابل للتركيب `Card` (البطاقة)، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:115]

```
116:                 modifier = Modifier.fillMaxWidth(),
```
> يضبط المُعامل `modifier` على `Modifier` مع تطبيق `fillMaxWidth` (ملء أقصى عرض). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:116]

```
117:                 colors = CardDefaults.cardColors(
```
> يضبط المُعامل `colors` على ناتج `CardDefaults.cardColors`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:117]

```
118:                     containerColor = colorScheme.surfaceVariant.copy(alpha = 0.3f)
```
> يضبط المُعامل `containerColor` (لون الحاوية) على `colorScheme.surfaceVariant` بنسخة `copy` تضبط `alpha` على `0.3f`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:118]

```
119:                 ),
```
> إغلاق قائمة مُعاملات `cardColors`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:119]

```
120:                 elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
```
> يضبط المُعامل `elevation` (الارتفاع/الظل) على ناتج `CardDefaults.cardElevation` مع المُعامل `defaultElevation` بقيمة `2.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:120]

```
121:             ) {
```
> إغلاق قائمة مُعاملات `Card` وفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:121]

```
122:                 Column(
```
> يستدعي العنصر القابل للتركيب `Column`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:122]

```
123:                     modifier = Modifier.padding(16.dp),
```
> يضبط المُعامل `modifier` على `Modifier` مع تطبيق `padding` بقيمة `16.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:123]

```
124:                     verticalArrangement = Arrangement.spacedBy(8.dp),
```
> يضبط المُعامل `verticalArrangement` على `Arrangement.spacedBy` بمسافة `8.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:124]

```
125:                     horizontalAlignment = Alignment.CenterHorizontally
```
> يضبط المُعامل `horizontalAlignment` على `Alignment.CenterHorizontally`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:125]

```
126:                 ) {
```
> إغلاق قائمة مُعاملات `Column` وفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:126]

```
127:                     Text(
```
> يستدعي العنصر القابل للتركيب `Text`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:127]

```
128:                         text = stringResource(R.string.setting_up_bluetooth),
```
> يضبط المُعامل `text` على ناتج `stringResource` للمورد `R.string.setting_up_bluetooth`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:128]

```
129:                         style = MaterialTheme.typography.bodyMedium.copy(
```
> يضبط المُعامل `style` على نسخة معدَّلة من `MaterialTheme.typography.bodyMedium` عبر `copy`، ويفتح قائمة المُعاملات المعدَّلة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:129]

```
130:                             fontFamily = FontFamily.Monospace,
```
> يضبط المُعامل `fontFamily` على `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:130]

```
131:                             color = colorScheme.onSurface.copy(alpha = 0.8f)
```
> يضبط المُعامل `color` على `colorScheme.onSurface` بنسخة `copy` تضبط `alpha` على `0.8f`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:131]

```
132:                         ),
```
> إغلاق قائمة مُعاملات `copy`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:132]

```
133:                         textAlign = TextAlign.Center
```
> يضبط المُعامل `textAlign` على `TextAlign.Center`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:133]

```
134:                     )
```
> إغلاق قائمة مُعاملات `Text`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:134]

```
135:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:135]

```
136:                     Text(
```
> يستدعي العنصر القابل للتركيب `Text`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:136]

```
137:                         text = stringResource(R.string.should_take_seconds),
```
> يضبط المُعامل `text` على ناتج `stringResource` للمورد `R.string.should_take_seconds`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:137]

```
138:                         style = MaterialTheme.typography.bodySmall.copy(
```
> يضبط المُعامل `style` على نسخة معدَّلة من `MaterialTheme.typography.bodySmall` عبر `copy`، ويفتح قائمة المُعاملات المعدَّلة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:138]

```
139:                             fontFamily = FontFamily.Monospace,
```
> يضبط المُعامل `fontFamily` على `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:139]

```
140:                             color = colorScheme.onSurface.copy(alpha = 0.6f)
```
> يضبط المُعامل `color` على `colorScheme.onSurface` بنسخة `copy` تضبط `alpha` على `0.6f`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:140]

```
141:                         ),
```
> إغلاق قائمة مُعاملات `copy`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:141]

```
142:                         textAlign = TextAlign.Center
```
> يضبط المُعامل `textAlign` على `TextAlign.Center`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:142]

```
143:                     )
```
> إغلاق قائمة مُعاملات `Text`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:143]

```
144:                 }
```
> إغلاق كتلة محتوى `Column` الداخلي. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:144]

```
145:             }
```
> إغلاق كتلة محتوى `Card`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:145]

```
146:         }
```
> إغلاق كتلة محتوى `Column` الخارجي. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:146]

```
147:     }
```
> إغلاق كتلة محتوى `Box` الخارجي. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:147]

```
148: }
```
> إغلاق جسم الدالة `InitializingScreen`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:148]

```
149: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:149]

```
150: /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:150]

```
151:  * Error screen shown if initialization fails
```
> تعليق: شاشة الخطأ التي تُعرض إذا فشلت التهيئة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:151]

```
152:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:152]

```
153: @Composable
```
> يضع التعليق التوضيحي `@Composable` على الدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:153]

```
154: fun InitializationErrorScreen(
```
> يُعرِّف الدالة `InitializationErrorScreen` (شاشة خطأ التهيئة)، ويفتح قائمة مُعاملاتها. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:154]

```
155:     modifier: Modifier,
```
> يُعرِّف المُعامل `modifier` من نوع `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:155]

```
156:     errorMessage: String,
```
> يُعرِّف المُعامل `errorMessage` (رسالة الخطأ) من نوع `String`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:156]

```
157:     onRetry: () -> Unit,
```
> يُعرِّف المُعامل `onRetry` (عند إعادة المحاولة) من نوع دالة بلا مُعاملات تُرجِع `Unit`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:157]

```
158:     onOpenSettings: () -> Unit
```
> يُعرِّف المُعامل `onOpenSettings` (عند فتح الإعدادات) من نوع دالة بلا مُعاملات تُرجِع `Unit`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:158]

```
159: ) {
```
> إغلاق قائمة مُعاملات الدالة وفتح جسمها. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:159]

```
160:     val colorScheme = MaterialTheme.colorScheme
```
> يُعرِّف متغيّراً ثابتاً اسمه `colorScheme` ويُسنِد إليه `MaterialTheme.colorScheme`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:160]

```
161: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:161]

```
162:     Box(
```
> يستدعي العنصر القابل للتركيب `Box`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:162]

```
163:         modifier = modifier.padding(32.dp),
```
> يضبط المُعامل `modifier` على `modifier` المُمرَّر مع تطبيق `padding` بقيمة `32.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:163]

```
164:         contentAlignment = Alignment.Center
```
> يضبط المُعامل `contentAlignment` على `Alignment.Center`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:164]

```
165:     ) {
```
> إغلاق قائمة مُعاملات `Box` وفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:165]

```
166:         Column(
```
> يستدعي العنصر القابل للتركيب `Column`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:166]

```
167:             verticalArrangement = Arrangement.spacedBy(24.dp),
```
> يضبط المُعامل `verticalArrangement` على `Arrangement.spacedBy` بمسافة `24.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:167]

```
168:             horizontalAlignment = Alignment.CenterHorizontally
```
> يضبط المُعامل `horizontalAlignment` على `Alignment.CenterHorizontally`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:168]

```
169:         ) {
```
> إغلاق قائمة مُعاملات `Column` وفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:169]

```
170:             // Error indicator
```
> تعليق: مؤشّر الخطأ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:170]

```
171:             Card(
```
> يستدعي العنصر القابل للتركيب `Card`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:171]

```
172:                 colors = CardDefaults.cardColors(
```
> يضبط المُعامل `colors` على ناتج `CardDefaults.cardColors`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:172]

```
173:                     containerColor = Color(0xFFFFEBEE)
```
> يضبط المُعامل `containerColor` على `Color` بالقيمة السداسية عشرية `0xFFFFEBEE`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:173]

```
174:                 ),
```
> إغلاق قائمة مُعاملات `cardColors`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:174]

```
175:                 elevation = CardDefaults.cardElevation(defaultElevation = 4.dp)
```
> يضبط المُعامل `elevation` على ناتج `CardDefaults.cardElevation` مع المُعامل `defaultElevation` بقيمة `4.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:175]

```
176:             ) {
```
> إغلاق قائمة مُعاملات `Card` وفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:176]

```
177:                 Text(
```
> يستدعي العنصر القابل للتركيب `Text`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:177]

```
178:                     text = stringResource(R.string.warning_emoji),
```
> يضبط المُعامل `text` على ناتج `stringResource` للمورد `R.string.warning_emoji`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:178]

```
179:                     style = MaterialTheme.typography.headlineLarge,
```
> يضبط المُعامل `style` على `MaterialTheme.typography.headlineLarge`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:179]

```
180:                     modifier = Modifier.padding(16.dp)
```
> يضبط المُعامل `modifier` على `Modifier` مع تطبيق `padding` بقيمة `16.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:180]

```
181:                 )
```
> إغلاق قائمة مُعاملات `Text`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:181]

```
182:             }
```
> إغلاق كتلة محتوى `Card`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:182]

```
183: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:183]

```
184:             Text(
```
> يستدعي العنصر القابل للتركيب `Text`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:184]

```
185:                 text = stringResource(R.string.setup_not_complete),
```
> يضبط المُعامل `text` على ناتج `stringResource` للمورد `R.string.setup_not_complete`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:185]

```
186:                 style = MaterialTheme.typography.headlineSmall.copy(
```
> يضبط المُعامل `style` على نسخة معدَّلة من `MaterialTheme.typography.headlineSmall` عبر `copy`، ويفتح قائمة المُعاملات المعدَّلة. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:186]

```
187:                     fontFamily = FontFamily.Monospace,
```
> يضبط المُعامل `fontFamily` على `FontFamily.Monospace`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:187]

```
188:                     fontWeight = FontWeight.Bold,
```
> يضبط المُعامل `fontWeight` على `FontWeight.Bold`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:188]

```
189:                     color = colorScheme.error
```
> يضبط المُعامل `color` على `colorScheme.error` (لون الخطأ). [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:189]

```
190:                 ),
```
> إغلاق قائمة مُعاملات `copy`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:190]

```
191:                 textAlign = TextAlign.Center
```
> يضبط المُعامل `textAlign` على `TextAlign.Center`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:191]

```
192:             )
```
> إغلاق قائمة مُعاملات `Text`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:192]

```
193: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:193]

```
194:             Card(
```
> يستدعي العنصر القابل للتركيب `Card`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:194]

```
195:                 modifier = Modifier.fillMaxWidth(),
```
> يضبط المُعامل `modifier` على `Modifier` مع تطبيق `fillMaxWidth`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:195]

```
196:                 colors = CardDefaults.cardColors(
```
> يضبط المُعامل `colors` على ناتج `CardDefaults.cardColors`، ويفتح قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:196]

```
197:                     containerColor = colorScheme.errorContainer.copy(alpha = 0.1f)
```
> يضبط المُعامل `containerColor` على `colorScheme.errorContainer` (حاوية الخطأ) بنسخة `copy` تضبط `alpha` على `0.1f`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:197]

```
198:                 ),
```
> إغلاق قائمة مُعاملات `cardColors`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:198]

```
199:                 elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
```
> يضبط المُعامل `elevation` على ناتج `CardDefaults.cardElevation` مع المُعامل `defaultElevation` بقيمة `2.dp`. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:199]

```
200:             ) {
```
> إغلاق قائمة مُعاملات `Card` وفتح كتلة المحتوى. [app/src/main/java/com/bitchat/android/onboarding/InitializingScreen.kt:200]
