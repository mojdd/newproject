# شريحة — app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt (الأسطر 1–200)

```
1: package com.bitchat.android.onboarding
```
> يُعرّف اسم الحزمة (package) بأنها `com.bitchat.android.onboarding`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:2]

```
3: import androidx.compose.foundation.layout.*
```
> يستورد (import) كل عناصر حزمة التخطيط `androidx.compose.foundation.layout`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:3]

```
4: import androidx.compose.foundation.rememberScrollState
```
> يستورد الدالة `rememberScrollState` من `androidx.compose.foundation`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:4]

```
5: import androidx.compose.foundation.shape.RoundedCornerShape
```
> يستورد الشكل `RoundedCornerShape` (المستطيل ذو الزوايا الدائرية) من `androidx.compose.foundation.shape`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:5]

```
6: import androidx.compose.foundation.verticalScroll
```
> يستورد المُعدِّل `verticalScroll` (التمرير العمودي) من `androidx.compose.foundation`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:6]

```
7: import androidx.compose.material.icons.Icons
```
> يستورد الكائن `Icons` (الأيقونات) من `androidx.compose.material.icons`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:7]

```
8: import androidx.compose.material.icons.filled.Bluetooth
```
> يستورد أيقونة `Bluetooth` (البلوتوث) من حزمة الأيقونات المملوءة `filled`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:8]

```
9: import androidx.compose.material.icons.filled.LocationOn
```
> يستورد أيقونة `LocationOn` (الموقع مُفعَّل) من حزمة الأيقونات المملوءة `filled`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:9]

```
10: import androidx.compose.material.icons.filled.Notifications
```
> يستورد أيقونة `Notifications` (الإشعارات) من حزمة الأيقونات المملوءة `filled`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:10]

```
11: import androidx.compose.material.icons.filled.Power
```
> يستورد أيقونة `Power` (الطاقة) من حزمة الأيقونات المملوءة `filled`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:11]

```
12: import androidx.compose.material.icons.filled.Mic
```
> يستورد أيقونة `Mic` (الميكروفون) من حزمة الأيقونات المملوءة `filled`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:12]

```
13: import androidx.compose.material.icons.filled.Security
```
> يستورد أيقونة `Security` (الأمان) من حزمة الأيقونات المملوءة `filled`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:13]

```
14: import androidx.compose.material.icons.filled.Wifi
```
> يستورد أيقونة `Wifi` (الواي فاي) من حزمة الأيقونات المملوءة `filled`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:14]

```
15: import androidx.compose.material.icons.filled.Settings
```
> يستورد أيقونة `Settings` (الإعدادات) من حزمة الأيقونات المملوءة `filled`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:15]

```
16: import androidx.compose.material3.*
```
> يستورد كل عناصر حزمة `androidx.compose.material3` (المادّة الثالثة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:16]

```
17: import androidx.compose.runtime.*
```
> يستورد كل عناصر حزمة `androidx.compose.runtime` (زمن التشغيل). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:17]

```
18: import androidx.compose.ui.Alignment
```
> يستورد الكائن `Alignment` (المحاذاة) من `androidx.compose.ui`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:18]

```
19: import androidx.compose.ui.Modifier
```
> يستورد `Modifier` (المُعدِّل) من `androidx.compose.ui`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:19]

```
20: import androidx.compose.ui.graphics.vector.ImageVector
```
> يستورد النوع `ImageVector` (صورة المتجه) من `androidx.compose.ui.graphics.vector`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:20]

```
21: import androidx.compose.ui.text.font.FontFamily
```
> يستورد `FontFamily` (عائلة الخط) من `androidx.compose.ui.text.font`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:21]

```
22: import androidx.compose.ui.text.font.FontWeight
```
> يستورد `FontWeight` (وزن الخط) من `androidx.compose.ui.text.font`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:22]

```
23: import androidx.compose.ui.text.style.TextAlign
```
> يستورد `TextAlign` (محاذاة النص) من `androidx.compose.ui.text.style`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:23]

```
24: import androidx.compose.ui.unit.dp
```
> يستورد الوحدة `dp` (البكسل المستقل عن الكثافة) من `androidx.compose.ui.unit`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:24]

```
25: import androidx.compose.ui.unit.sp
```
> يستورد الوحدة `sp` (البكسل المُقيَّس) من `androidx.compose.ui.unit`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:25]

```
26: import androidx.compose.ui.res.stringResource
```
> يستورد الدالة `stringResource` (مورد النص) من `androidx.compose.ui.res`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:26]

```
27: import com.bitchat.android.R
```
> يستورد فئة الموارد `R` من `com.bitchat.android`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:28]

```
29: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:29]

```
30:  * Permission explanation screen shown before requesting permissions
```
> تعليق: شاشة شرح الأذونات تُعرَض قبل طلب الأذونات. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:30]

```
31:  * Explains why bitchat needs each permission and reassures users about privacy
```
> تعليق: تشرح لماذا يحتاج bitchat كل إذن وتطمئن المستخدمين بشأن الخصوصية. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:31]

```
32:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:32]

```
33: @Composable
```
> تُوضَع السمة `@Composable` (قابل للتركيب) على الدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:33]

```
34: fun PermissionExplanationScreen(
```
> تُعرَّف الدالة `PermissionExplanationScreen` (شاشة شرح الأذونات) وتبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:34]

```
35:     modifier: Modifier,
```
> تُعرَّف المعامِلة `modifier` من النوع `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:35]

```
36:     permissionCategories: List<PermissionCategory>,
```
> تُعرَّف المعامِلة `permissionCategories` (فئات الأذونات) من نوع قائمة `List<PermissionCategory>`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:36]

```
37:     onContinue: () -> Unit
```
> تُعرَّف المعامِلة `onContinue` (عند المتابعة) من نوع دالة بلا وسائط تُعيد `Unit`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:37]

```
38: ) {
```
> إغلاق قائمة المعاملات وفتح جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:38]

```
39:     val colorScheme = MaterialTheme.colorScheme
```
> يُعرَّف المتغيّر الثابت `colorScheme` (مخطط الألوان) ويُسنَد إليه `MaterialTheme.colorScheme`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:39]

```
40:     val scrollState = rememberScrollState()
```
> يُعرَّف المتغيّر الثابت `scrollState` (حالة التمرير) ويُسنَد إليه ناتج استدعاء `rememberScrollState()`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:40]

```
41: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:41]

```
42:     Box(
```
> يُستدعى المُركّب `Box` (الصندوق) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:42]

```
43:         modifier = modifier
```
> يُضبَط الوسيط `modifier` على قيمة المعامِلة `modifier`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:43]

```
44:     ) {
```
> إغلاق وسائط `Box` وفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:44]

```
45:         // Scrollable content
```
> تعليق: محتوى قابل للتمرير. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:45]

```
46:         Column(
```
> يُستدعى المُركّب `Column` (العمود) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:46]

```
47:             modifier = Modifier
```
> يُضبَط الوسيط `modifier` ويبدأ بناؤه من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:47]

```
48:                 .fillMaxSize()
```
> يُطبَّق المُعدِّل `fillMaxSize` (ملء الحجم الأقصى). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:48]

```
49:                 .padding(horizontal = 24.dp)
```
> يُطبَّق المُعدِّل `padding` (الحشو) أفقياً بقيمة `24.dp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:49]

```
50:                 .padding(bottom = 88.dp) // Leave space for the fixed button
```
> يُطبَّق المُعدِّل `padding` من الأسفل بقيمة `88.dp`، مع تعليق: ترك مساحة للزر الثابت. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:50]

```
51:                 .verticalScroll(scrollState),
```
> يُطبَّق المُعدِّل `verticalScroll` (التمرير العمودي) بالحالة `scrollState`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:51]

```
52:             verticalArrangement = Arrangement.spacedBy(16.dp)
```
> يُضبَط الوسيط `verticalArrangement` (الترتيب العمودي) على `Arrangement.spacedBy(16.dp)` (تباعد ١٦ بكسلاً). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:52]

```
53:         ) {
```
> إغلاق وسائط `Column` وفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:53]

```
54:             Spacer(modifier = Modifier.height(24.dp))
```
> يُستدعى المُركّب `Spacer` (الفاصل) بمُعدِّل ارتفاع `height(24.dp)`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:54]

```
55:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:55]

```
56:             // Header Section - matching AboutSheet style
```
> تعليق: قسم الترويسة - يطابق أسلوب AboutSheet. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:56]

```
57:             Column(
```
> يُستدعى المُركّب `Column` (العمود) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:57]

```
58:                 modifier = Modifier
```
> يُضبَط الوسيط `modifier` ويبدأ بناؤه من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:58]

```
59:                     .fillMaxWidth()
```
> يُطبَّق المُعدِّل `fillMaxWidth` (ملء العرض الأقصى). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:59]

```
60:                     .padding(bottom = 16.dp),
```
> يُطبَّق المُعدِّل `padding` من الأسفل بقيمة `16.dp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:60]

```
61:                 verticalArrangement = Arrangement.spacedBy(8.dp)
```
> يُضبَط الوسيط `verticalArrangement` على `Arrangement.spacedBy(8.dp)` (تباعد ٨ بكسلاً). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:61]

```
62:             ) {
```
> إغلاق وسائط `Column` وفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:62]

```
63:                 Row(
```
> يُستدعى المُركّب `Row` (الصف) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:63]

```
64:                     horizontalArrangement = Arrangement.spacedBy(8.dp),
```
> يُضبَط الوسيط `horizontalArrangement` (الترتيب الأفقي) على `Arrangement.spacedBy(8.dp)` (تباعد ٨ بكسلاً). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:64]

```
65:                     verticalAlignment = Alignment.Bottom,
```
> يُضبَط الوسيط `verticalAlignment` (المحاذاة العمودية) على `Alignment.Bottom` (الأسفل). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:65]

```
66:                     modifier = Modifier.fillMaxWidth()
```
> يُضبَط الوسيط `modifier` على `Modifier.fillMaxWidth()` (ملء العرض الأقصى). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:66]

```
67:                 ) {
```
> إغلاق وسائط `Row` وفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:67]

```
68:                     Text(
```
> يُستدعى المُركّب `Text` (النص) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:68]

```
69:                         text = stringResource(R.string.app_name),
```
> يُضبَط الوسيط `text` على مورد النص `R.string.app_name` (اسم التطبيق). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:69]

```
70:                         style = MaterialTheme.typography.headlineLarge.copy(
```
> يُضبَط الوسيط `style` على نسخة معدَّلة من `MaterialTheme.typography.headlineLarge` (نمط العنوان الكبير). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:70]

```
71:                             fontFamily = FontFamily.Monospace,
```
> يُضبَط `fontFamily` (عائلة الخط) على `FontFamily.Monospace` (الخط أحادي المسافة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:71]

```
72:                             fontWeight = FontWeight.Bold,
```
> يُضبَط `fontWeight` (وزن الخط) على `FontWeight.Bold` (عريض). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:72]

```
73:                             fontSize = 32.sp
```
> يُضبَط `fontSize` (حجم الخط) على `32.sp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:73]

```
74:                         ),
```
> إغلاق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:74]

```
75:                         color = colorScheme.onBackground
```
> يُضبَط الوسيط `color` (اللون) على `colorScheme.onBackground` (لون فوق الخلفية). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:75]

```
76:                     )
```
> إغلاق استدعاء المُركّب `Text`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:76]

```
77:                 }
```
> إغلاق نطاق `Row`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:77]

```
78: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:78]

```
79:                 Text(
```
> يُستدعى المُركّب `Text` (النص) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:79]

```
80:                     text = stringResource(R.string.about_tagline),
```
> يُضبَط الوسيط `text` على مورد النص `R.string.about_tagline` (الشعار التعريفي). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:80]

```
81:                     fontSize = 12.sp,
```
> يُضبَط الوسيط `fontSize` (حجم الخط) على `12.sp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:81]

```
82:                     fontFamily = FontFamily.Monospace,
```
> يُضبَط الوسيط `fontFamily` (عائلة الخط) على `FontFamily.Monospace` (الخط أحادي المسافة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:82]

```
83:                     color = colorScheme.onBackground.copy(alpha = 0.7f)
```
> يُضبَط الوسيط `color` على `colorScheme.onBackground` بشفافية `alpha = 0.7f`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:83]

```
84:                 )
```
> إغلاق استدعاء المُركّب `Text`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:84]

```
85:             }
```
> إغلاق نطاق `Column` (الترويسة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:85]

```
86: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:86]

```
87:             // Privacy assurance section - matching AboutSheet card style
```
> تعليق: قسم طمأنة الخصوصية - يطابق أسلوب بطاقة AboutSheet. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:87]

```
88:             Surface(
```
> يُستدعى المُركّب `Surface` (السطح) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:88]

```
89:                 modifier = Modifier.fillMaxWidth(),
```
> يُضبَط الوسيط `modifier` على `Modifier.fillMaxWidth()` (ملء العرض الأقصى). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:89]

```
90:                 color = colorScheme.surfaceVariant.copy(alpha = 0.25f),
```
> يُضبَط الوسيط `color` على `colorScheme.surfaceVariant` بشفافية `alpha = 0.25f`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:90]

```
91:                 shape = RoundedCornerShape(12.dp)
```
> يُضبَط الوسيط `shape` (الشكل) على `RoundedCornerShape(12.dp)` (زوايا دائرية نصف قطرها ١٢ بكسلاً). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:91]

```
92:             ) {
```
> إغلاق وسائط `Surface` وفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:92]

```
93:                 Column(
```
> يُستدعى المُركّب `Column` (العمود) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:93]

```
94:                     modifier = Modifier.padding(16.dp),
```
> يُضبَط الوسيط `modifier` على `Modifier.padding(16.dp)` (حشو ١٦ بكسلاً). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:94]

```
95:                     verticalArrangement = Arrangement.spacedBy(8.dp)
```
> يُضبَط الوسيط `verticalArrangement` على `Arrangement.spacedBy(8.dp)` (تباعد ٨ بكسلاً). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:95]

```
96:                 ) {
```
> إغلاق وسائط `Column` وفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:96]

```
97:                     Row(
```
> يُستدعى المُركّب `Row` (الصف) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:97]

```
98:                         verticalAlignment = Alignment.Top,
```
> يُضبَط الوسيط `verticalAlignment` (المحاذاة العمودية) على `Alignment.Top` (الأعلى). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:98]

```
99:                         horizontalArrangement = Arrangement.spacedBy(12.dp)
```
> يُضبَط الوسيط `horizontalArrangement` على `Arrangement.spacedBy(12.dp)` (تباعد ١٢ بكسلاً). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:99]

```
100:                     ) {
```
> إغلاق وسائط `Row` وفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:100]

```
101:                         Icon(
```
> يُستدعى المُركّب `Icon` (الأيقونة) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:101]

```
102:                             imageVector = Icons.Filled.Security,
```
> يُضبَط الوسيط `imageVector` (صورة المتجه) على `Icons.Filled.Security` (أيقونة الأمان المملوءة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:102]

```
103:                             contentDescription = stringResource(R.string.cd_privacy_protected),
```
> يُضبَط الوسيط `contentDescription` (وصف المحتوى) على مورد النص `R.string.cd_privacy_protected` (الخصوصية محمية). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:103]

```
104:                             tint = colorScheme.primary,
```
> يُضبَط الوسيط `tint` (لون الصبغة) على `colorScheme.primary` (اللون الأساسي). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:104]

```
105:                             modifier = Modifier
```
> يُضبَط الوسيط `modifier` ويبدأ بناؤه من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:105]

```
106:                                 .padding(top = 2.dp)
```
> يُطبَّق المُعدِّل `padding` من الأعلى بقيمة `2.dp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:106]

```
107:                                 .size(20.dp)
```
> يُطبَّق المُعدِّل `size` (الحجم) بقيمة `20.dp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:107]

```
108:                         )
```
> إغلاق استدعاء المُركّب `Icon`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:108]

```
109:                         Column {
```
> يُستدعى المُركّب `Column` (العمود) وتُفتَح كتلة محتواه مباشرة بلا وسائط. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:109]

```
110:                             Text(
```
> يُستدعى المُركّب `Text` (النص) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:110]

```
111:                                 text = stringResource(R.string.privacy_protected),
```
> يُضبَط الوسيط `text` على مورد النص `R.string.privacy_protected` (الخصوصية محمية). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:111]

```
112:                                 style = MaterialTheme.typography.titleMedium,
```
> يُضبَط الوسيط `style` على `MaterialTheme.typography.titleMedium` (نمط العنوان المتوسط). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:112]

```
113:                                 fontWeight = FontWeight.Medium,
```
> يُضبَط الوسيط `fontWeight` (وزن الخط) على `FontWeight.Medium` (متوسط). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:113]

```
114:                                 color = colorScheme.onBackground
```
> يُضبَط الوسيط `color` على `colorScheme.onBackground` (لون فوق الخلفية). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:114]

```
115:                             )
```
> إغلاق استدعاء المُركّب `Text`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:115]

```
116:                             Spacer(modifier = Modifier.height(4.dp))
```
> يُستدعى المُركّب `Spacer` (الفاصل) بمُعدِّل ارتفاع `height(4.dp)`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:116]

```
117:                             Text(
```
> يُستدعى المُركّب `Text` (النص) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:117]

```
118:                                 text = stringResource(R.string.privacy_bullets),
```
> يُضبَط الوسيط `text` على مورد النص `R.string.privacy_bullets` (نقاط الخصوصية). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:118]

```
119:                                 style = MaterialTheme.typography.bodySmall,
```
> يُضبَط الوسيط `style` على `MaterialTheme.typography.bodySmall` (نمط المتن الصغير). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:119]

```
120:                                 fontFamily = FontFamily.Monospace,
```
> يُضبَط الوسيط `fontFamily` (عائلة الخط) على `FontFamily.Monospace` (الخط أحادي المسافة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:120]

```
121:                                 color = colorScheme.onBackground.copy(alpha = 0.8f)
```
> يُضبَط الوسيط `color` على `colorScheme.onBackground` بشفافية `alpha = 0.8f`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:121]

```
122:                             )
```
> إغلاق استدعاء المُركّب `Text`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:122]

```
123:                         }
```
> إغلاق نطاق `Column` الداخلي. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:123]

```
124:                     }
```
> إغلاق نطاق `Row`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:124]

```
125:                 }
```
> إغلاق نطاق `Column`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:125]

```
126:             }
```
> إغلاق نطاق `Surface`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:126]

```
127: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:127]

```
128:             // Section header
```
> تعليق: ترويسة القسم. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:128]

```
129:             Text(
```
> يُستدعى المُركّب `Text` (النص) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:129]

```
130:                 text = stringResource(R.string.permissions_header),
```
> يُضبَط الوسيط `text` على مورد النص `R.string.permissions_header` (ترويسة الأذونات). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:130]

```
131:                 style = MaterialTheme.typography.labelLarge,
```
> يُضبَط الوسيط `style` على `MaterialTheme.typography.labelLarge` (نمط التسمية الكبيرة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:131]

```
132:                 color = colorScheme.onBackground.copy(alpha = 0.7f),
```
> يُضبَط الوسيط `color` على `colorScheme.onBackground` بشفافية `alpha = 0.7f`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:132]

```
133:                 modifier = Modifier.padding(top = 8.dp, bottom = 8.dp)
```
> يُضبَط الوسيط `modifier` على `Modifier.padding` بحشو من الأعلى `8.dp` ومن الأسفل `8.dp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:133]

```
134:             )
```
> إغلاق استدعاء المُركّب `Text`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:134]

```
135: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:135]

```
136:             // Permission categories
```
> تعليق: فئات الأذونات. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:136]

```
137:             permissionCategories.forEach { category ->
```
> تُستدعى الدالة `forEach` (لكل عنصر) على `permissionCategories`، مع معامِلة لامبدا `category` (فئة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:137]

```
138:                 PermissionCategoryCard(
```
> يُستدعى المُركّب `PermissionCategoryCard` (بطاقة فئة الإذن) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:138]

```
139:                     category = category,
```
> يُضبَط الوسيط `category` (الفئة) على قيمة معامِلة اللامبدا `category`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:139]

```
140:                     colorScheme = colorScheme
```
> يُضبَط الوسيط `colorScheme` على المتغيّر `colorScheme`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:140]

```
141:                 )
```
> إغلاق استدعاء المُركّب `PermissionCategoryCard`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:141]

```
142:             }
```
> إغلاق نطاق لامبدا `forEach`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:142]

```
143: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:143]

```
144:             Spacer(modifier = Modifier.height(24.dp))
```
> يُستدعى المُركّب `Spacer` (الفاصل) بمُعدِّل ارتفاع `height(24.dp)`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:144]

```
145:         }
```
> إغلاق نطاق `Column` (المحتوى القابل للتمرير). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:145]

```
146: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:146]

```
147:         // Fixed button at bottom
```
> تعليق: زر ثابت في الأسفل. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:147]

```
148:         Surface(
```
> يُستدعى المُركّب `Surface` (السطح) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:148]

```
149:             modifier = Modifier
```
> يُضبَط الوسيط `modifier` ويبدأ بناؤه من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:149]

```
150:                 .align(Alignment.BottomCenter)
```
> يُطبَّق المُعدِّل `align` (المحاذاة) بقيمة `Alignment.BottomCenter` (وسط الأسفل). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:150]

```
151:                 .fillMaxWidth(),
```
> يُطبَّق المُعدِّل `fillMaxWidth` (ملء العرض الأقصى). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:151]

```
152:             color = colorScheme.surface,
```
> يُضبَط الوسيط `color` على `colorScheme.surface` (لون السطح). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:152]

```
153:             shadowElevation = 8.dp
```
> يُضبَط الوسيط `shadowElevation` (ارتفاع الظل) على `8.dp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:153]

```
154:         ) {
```
> إغلاق وسائط `Surface` وفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:154]

```
155:             Button(
```
> يُستدعى المُركّب `Button` (الزر) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:155]

```
156:                 onClick = onContinue,
```
> يُضبَط الوسيط `onClick` (عند النقر) على معامِلة الدالة `onContinue`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:156]

```
157:                 modifier = Modifier
```
> يُضبَط الوسيط `modifier` ويبدأ بناؤه من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:157]

```
158:                     .fillMaxWidth()
```
> يُطبَّق المُعدِّل `fillMaxWidth` (ملء العرض الأقصى). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:158]

```
159:                     .padding(horizontal = 24.dp, vertical = 16.dp),
```
> يُطبَّق المُعدِّل `padding` بحشو أفقي `24.dp` وعمودي `16.dp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:159]

```
160:                 colors = ButtonDefaults.buttonColors(
```
> يُضبَط الوسيط `colors` (الألوان) على ناتج `ButtonDefaults.buttonColors` وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:160]

```
161:                     containerColor = colorScheme.primary
```
> يُضبَط الوسيط `containerColor` (لون الحاوية) على `colorScheme.primary` (اللون الأساسي). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:161]

```
162:                 )
```
> إغلاق استدعاء `ButtonDefaults.buttonColors`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:162]

```
163:             ) {
```
> إغلاق وسائط `Button` وفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:163]

```
164:                 Text(
```
> يُستدعى المُركّب `Text` (النص) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:164]

```
165:                     text = stringResource(R.string.grant_permissions),
```
> يُضبَط الوسيط `text` على مورد النص `R.string.grant_permissions` (منح الأذونات). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:165]

```
166:                     style = MaterialTheme.typography.bodyMedium.copy(
```
> يُضبَط الوسيط `style` على نسخة معدَّلة من `MaterialTheme.typography.bodyMedium` (نمط المتن المتوسط). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:166]

```
167:                         fontFamily = FontFamily.Monospace,
```
> يُضبَط `fontFamily` (عائلة الخط) على `FontFamily.Monospace` (الخط أحادي المسافة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:167]

```
168:                         fontWeight = FontWeight.Bold
```
> يُضبَط `fontWeight` (وزن الخط) على `FontWeight.Bold` (عريض). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:168]

```
169:                     ),
```
> إغلاق استدعاء `copy` للنمط. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:169]

```
170:                     modifier = Modifier.padding(vertical = 4.dp)
```
> يُضبَط الوسيط `modifier` على `Modifier.padding(vertical = 4.dp)` (حشو عمودي ٤ بكسلاً). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:170]

```
171:                 )
```
> إغلاق استدعاء المُركّب `Text`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:171]

```
172:             }
```
> إغلاق نطاق `Button`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:172]

```
173:         }
```
> إغلاق نطاق `Surface` (الزر الثابت). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:173]

```
174:     }
```
> إغلاق نطاق `Box`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:174]

```
175: }
```
> إغلاق نطاق الدالة `PermissionExplanationScreen`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:175]

```
176: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:176]

```
177: @Composable
```
> تُوضَع السمة `@Composable` (قابل للتركيب) على الدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:177]

```
178: private fun PermissionCategoryCard(
```
> تُعرَّف الدالة الخاصة `private` المسماة `PermissionCategoryCard` (بطاقة فئة الإذن) وتبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:178]

```
179:     category: PermissionCategory,
```
> تُعرَّف المعامِلة `category` (الفئة) من النوع `PermissionCategory`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:179]

```
180:     colorScheme: ColorScheme
```
> تُعرَّف المعامِلة `colorScheme` (مخطط الألوان) من النوع `ColorScheme`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:180]

```
181: ) {
```
> إغلاق قائمة المعاملات وفتح جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:181]

```
182:     Row(
```
> يُستدعى المُركّب `Row` (الصف) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:182]

```
183:         verticalAlignment = Alignment.Top,
```
> يُضبَط الوسيط `verticalAlignment` (المحاذاة العمودية) على `Alignment.Top` (الأعلى). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:183]

```
184:         modifier = Modifier
```
> يُضبَط الوسيط `modifier` ويبدأ بناؤه من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:184]

```
185:             .fillMaxWidth()
```
> يُطبَّق المُعدِّل `fillMaxWidth` (ملء العرض الأقصى). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:185]

```
186:             .padding(vertical = 8.dp)
```
> يُطبَّق المُعدِّل `padding` بحشو عمودي `8.dp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:186]

```
187:     ) {
```
> إغلاق وسائط `Row` وفتح كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:187]

```
188:         Icon(
```
> يُستدعى المُركّب `Icon` (الأيقونة) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:188]

```
189:             imageVector = getPermissionIcon(category.type),
```
> يُضبَط الوسيط `imageVector` على ناتج استدعاء `getPermissionIcon(category.type)` (جلب أيقونة الإذن لنوع الفئة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:189]

```
190:             contentDescription = category.type.nameValue,
```
> يُضبَط الوسيط `contentDescription` (وصف المحتوى) على `category.type.nameValue` (قيمة اسم نوع الفئة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:190]

```
191:             tint = colorScheme.primary,
```
> يُضبَط الوسيط `tint` (لون الصبغة) على `colorScheme.primary` (اللون الأساسي). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:191]

```
192:             modifier = Modifier
```
> يُضبَط الوسيط `modifier` ويبدأ بناؤه من `Modifier`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:192]

```
193:                 .padding(top = 2.dp)
```
> يُطبَّق المُعدِّل `padding` من الأعلى بقيمة `2.dp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:193]

```
194:                 .size(20.dp)
```
> يُطبَّق المُعدِّل `size` (الحجم) بقيمة `20.dp`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:194]

```
195:         )
```
> إغلاق استدعاء المُركّب `Icon`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:195]

```
196:         Spacer(modifier = Modifier.width(16.dp))
```
> يُستدعى المُركّب `Spacer` (الفاصل) بمُعدِّل عرض `width(16.dp)`. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:196]

```
197:         Column {
```
> يُستدعى المُركّب `Column` (العمود) وتُفتَح كتلة محتواه مباشرة بلا وسائط. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:197]

```
198:             Text(
```
> يُستدعى المُركّب `Text` (النص) وتبدأ وسائطه. [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:198]

```
199:                 text = category.type.nameValue,
```
> يُضبَط الوسيط `text` على `category.type.nameValue` (قيمة اسم نوع الفئة). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:199]

```
200:                 style = MaterialTheme.typography.titleMedium,
```
> يُضبَط الوسيط `style` على `MaterialTheme.typography.titleMedium` (نمط العنوان المتوسط). [app/src/main/java/com/bitchat/android/onboarding/PermissionExplanationScreen.kt:200]
