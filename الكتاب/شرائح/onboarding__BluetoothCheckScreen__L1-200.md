# شريحة — app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt (الأسطر 1–200)

```
1: package com.bitchat.android.onboarding
```
> يُعرِّف حُزمة (package) الملف باسم com.bitchat.android.onboarding. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:2]

```
3: import androidx.compose.animation.core.*
```
> يستورد كل ما في حزمة androidx.compose.animation.core (نواة الحركة). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:3]

```
4: import androidx.compose.foundation.layout.*
```
> يستورد كل ما في حزمة androidx.compose.foundation.layout (تخطيط الأساس). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:4]

```
5: import androidx.compose.material.icons.Icons
```
> يستورد الكائن Icons (الأيقونات) من حزمة androidx.compose.material.icons. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:5]

```
6: import androidx.compose.material.icons.outlined.*
```
> يستورد كل ما في حزمة androidx.compose.material.icons.outlined (الأيقونات المُحدَّدة بالخط). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:6]

```
7: import androidx.compose.material3.*
```
> يستورد كل ما في حزمة androidx.compose.material3. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:7]

```
8: import androidx.compose.runtime.*
```
> يستورد كل ما في حزمة androidx.compose.runtime (زمن التشغيل). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:8]

```
9: import androidx.compose.ui.Alignment
```
> يستورد الصنف Alignment (المحاذاة) من حزمة androidx.compose.ui. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:9]

```
10: import androidx.compose.ui.Modifier
```
> يستورد الصنف Modifier (المُعدِّل) من حزمة androidx.compose.ui. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:10]

```
11: import androidx.compose.ui.draw.rotate
```
> يستورد الدالة rotate (التدوير) من حزمة androidx.compose.ui.draw. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:11]

```
12: import androidx.compose.ui.graphics.Color
```
> يستورد الصنف Color (اللون) من حزمة androidx.compose.ui.graphics. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:12]

```
13: import androidx.compose.ui.text.font.FontFamily
```
> يستورد الصنف FontFamily (عائلة الخط) من حزمة androidx.compose.ui.text.font. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:13]

```
14: import androidx.compose.ui.text.font.FontWeight
```
> يستورد الصنف FontWeight (وزن الخط) من حزمة androidx.compose.ui.text.font. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:14]

```
15: import androidx.compose.ui.text.style.TextAlign
```
> يستورد الصنف TextAlign (محاذاة النص) من حزمة androidx.compose.ui.text.style. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:15]

```
16: import androidx.compose.ui.unit.dp
```
> يستورد الامتداد dp (وحدة البكسل المستقل عن الكثافة) من حزمة androidx.compose.ui.unit. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:16]

```
17: import androidx.compose.ui.res.stringResource
```
> يستورد الدالة stringResource (مورد النص) من حزمة androidx.compose.ui.res. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:17]

```
18: import com.bitchat.android.R
```
> يستورد الصنف R (موارد المشروع) من حزمة com.bitchat.android. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:18]

```
19: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:19]

```
20: /**
```
> بداية تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:20]

```
21:  * Screen shown when checking Bluetooth status or requesting Bluetooth enable
```
> تعليق: شاشة تُعرَض عند فحص حالة البلوتوث أو طلب تفعيل البلوتوث. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:21]

```
22:  */
```
> نهاية تعليق التوثيق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:22]

```
23: @Composable
```
> يضع الوسم @Composable (قابل للتركيب) على الدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:23]

```
24: fun BluetoothCheckScreen(
```
> يُعرِّف دالة باسم BluetoothCheckScreen (شاشة فحص البلوتوث) وتبدأ قائمة وُسطائها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:24]

```
25:     modifier: Modifier,
```
> وسيط باسم modifier (المُعدِّل) من نوع Modifier. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:25]

```
26:     status: BluetoothStatus,
```
> وسيط باسم status (الحالة) من نوع BluetoothStatus (حالة البلوتوث). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:26]

```
27:     onEnableBluetooth: () -> Unit,
```
> وسيط باسم onEnableBluetooth (عند تفعيل البلوتوث) من نوع دالة لا تأخذ وُسطاء وتُعيد Unit (لا شيء). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:27]

```
28:     onRetry: () -> Unit,
```
> وسيط باسم onRetry (عند إعادة المحاولة) من نوع دالة لا تأخذ وُسطاء وتُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:28]

```
29:     onSkip: () -> Unit,
```
> وسيط باسم onSkip (عند التخطّي) من نوع دالة لا تأخذ وُسطاء وتُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:29]

```
30:     isLoading: Boolean = false
```
> وسيط باسم isLoading (هل قيد التحميل) من نوع Boolean (منطقي) بقيمة افتراضية false. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:30]

```
31: ) {
```
> إغلاق قائمة الوُسطاء وبداية جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:31]

```
32:     val colorScheme = MaterialTheme.colorScheme
```
> يُعرِّف ثابتاً باسم colorScheme (مخطط الألوان) ويُسنِد إليه قيمة MaterialTheme.colorScheme. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:33]

```
34:     Box(
```
> يستدعي المُركِّب Box (الصندوق) وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:34]

```
35:         modifier = modifier.padding(32.dp),
```
> يُسنِد للوسيط modifier قيمة modifier مع تطبيق padding (حشوة) مقدارها 32 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:35]

```
36:         contentAlignment = Alignment.Center
```
> يُسنِد للوسيط contentAlignment (محاذاة المحتوى) قيمة Alignment.Center (المركز). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:36]

```
37:     ) {
```
> إغلاق قائمة وُسطاء Box وبداية كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:37]

```
38:         when (status) {
```
> يبدأ تعبير when (عندما) يفحص قيمة status. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:38]

```
39:             BluetoothStatus.DISABLED -> {
```
> فرع للحالة BluetoothStatus.DISABLED (مُعطَّل) وبداية كتلته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:39]

```
40:                 BluetoothDisabledContent(
```
> يستدعي المُركِّب BluetoothDisabledContent (محتوى البلوتوث المُعطَّل) وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:40]

```
41:                     onEnableBluetooth = onEnableBluetooth,
```
> يُسنِد للوسيط onEnableBluetooth قيمة onEnableBluetooth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:41]

```
42:                     onRetry = onRetry,
```
> يُسنِد للوسيط onRetry قيمة onRetry. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:42]

```
43:                     onSkip = onSkip,
```
> يُسنِد للوسيط onSkip قيمة onSkip. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:43]

```
44:                     colorScheme = colorScheme,
```
> يُسنِد للوسيط colorScheme قيمة colorScheme. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:44]

```
45:                     isLoading = isLoading
```
> يُسنِد للوسيط isLoading قيمة isLoading. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:45]

```
46:                 )
```
> إغلاق استدعاء BluetoothDisabledContent. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:46]

```
47:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:47]

```
48:             BluetoothStatus.NOT_SUPPORTED -> {
```
> فرع للحالة BluetoothStatus.NOT_SUPPORTED (غير مدعوم) وبداية كتلته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:48]

```
49:                 BluetoothNotSupportedContent(
```
> يستدعي المُركِّب BluetoothNotSupportedContent (محتوى البلوتوث غير المدعوم) وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:49]

```
50:                     colorScheme = colorScheme,
```
> يُسنِد للوسيط colorScheme قيمة colorScheme. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:50]

```
51:                     onSkip = onSkip
```
> يُسنِد للوسيط onSkip قيمة onSkip. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:51]

```
52:                 )
```
> إغلاق استدعاء BluetoothNotSupportedContent. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:52]

```
53:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:53]

```
54:             BluetoothStatus.ENABLED -> {
```
> فرع للحالة BluetoothStatus.ENABLED (مُفعَّل) وبداية كتلته. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:54]

```
55:                 BluetoothCheckingContent(
```
> يستدعي المُركِّب BluetoothCheckingContent (محتوى فحص البلوتوث) وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:55]

```
56:                     colorScheme = colorScheme
```
> يُسنِد للوسيط colorScheme قيمة colorScheme. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:56]

```
57:                 )
```
> إغلاق استدعاء BluetoothCheckingContent. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:57]

```
58:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:58]

```
59:         }
```
> إغلاق نطاق (إغلاق تعبير when). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:59]

```
60:     }
```
> إغلاق نطاق (إغلاق كتلة محتوى Box). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:60]

```
61: }
```
> إغلاق نطاق (إغلاق دالة BluetoothCheckScreen). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:61]

```
62: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:62]

```
63: @Composable
```
> يضع الوسم @Composable على الدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:63]

```
64: private fun BluetoothDisabledContent(
```
> يُعرِّف دالة خاصة (private) باسم BluetoothDisabledContent وتبدأ قائمة وُسطائها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:64]

```
65:     onEnableBluetooth: () -> Unit,
```
> وسيط باسم onEnableBluetooth من نوع دالة لا تأخذ وُسطاء وتُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:65]

```
66:     onRetry: () -> Unit,
```
> وسيط باسم onRetry من نوع دالة لا تأخذ وُسطاء وتُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:66]

```
67:     onSkip: () -> Unit,
```
> وسيط باسم onSkip من نوع دالة لا تأخذ وُسطاء وتُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:67]

```
68:     colorScheme: ColorScheme,
```
> وسيط باسم colorScheme من نوع ColorScheme (مخطط الألوان). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:68]

```
69:     isLoading: Boolean
```
> وسيط باسم isLoading من نوع Boolean. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:69]

```
70: ) {
```
> إغلاق قائمة الوُسطاء وبداية جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:70]

```
71:     Column(
```
> يستدعي المُركِّب Column (العمود) وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:71]

```
72:         verticalArrangement = Arrangement.spacedBy(24.dp),
```
> يُسنِد للوسيط verticalArrangement (الترتيب العمودي) قيمة Arrangement.spacedBy بمسافة 24 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:72]

```
73:         horizontalAlignment = Alignment.CenterHorizontally
```
> يُسنِد للوسيط horizontalAlignment (المحاذاة الأفقية) قيمة Alignment.CenterHorizontally (التوسيط الأفقي). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:73]

```
74:     ) {
```
> إغلاق قائمة وُسطاء Column وبداية كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:74]

```
75:         // Bluetooth icon - using Bluetooth outlined icon in app's green color
```
> تعليق: أيقونة البلوتوث - باستخدام أيقونة البلوتوث ذات الخط الخارجي بلون التطبيق الأخضر. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:75]

```
76:         Icon(
```
> يستدعي المُركِّب Icon (الأيقونة) وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:76]

```
77:             imageVector = Icons.Outlined.Bluetooth,
```
> يُسنِد للوسيط imageVector (متّجه الصورة) قيمة Icons.Outlined.Bluetooth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:77]

```
78:             contentDescription = stringResource(R.string.cd_bluetooth),
```
> يُسنِد للوسيط contentDescription (وصف المحتوى) قيمة النص المُحمَّل من المورد R.string.cd_bluetooth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:78]

```
79:             modifier = Modifier.size(64.dp),
```
> يُسنِد للوسيط modifier قيمة Modifier مع تطبيق size (الحجم) بمقدار 64 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:79]

```
80:             tint = Color(0xFF00C851) // App's main green color
```
> يُسنِد للوسيط tint (الصبغة) لوناً قيمته 0xFF00C851، مع تعليق: لون التطبيق الأخضر الرئيسي. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:80]

```
81:         )
```
> إغلاق استدعاء Icon. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:81]

```
82: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:82]

```
83:         Text(
```
> يستدعي المُركِّب Text (النص) وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:83]

```
84:             text = stringResource(R.string.bluetooth_recommended),
```
> يُسنِد للوسيط text قيمة النص المُحمَّل من المورد R.string.bluetooth_recommended. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:84]

```
85:             style = MaterialTheme.typography.headlineSmall.copy(
```
> يُسنِد للوسيط style (النمط) نسخة معدَّلة من MaterialTheme.typography.headlineSmall وتبدأ تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:85]

```
86:                 fontFamily = FontFamily.Monospace,
```
> يُسنِد للخاصية fontFamily قيمة FontFamily.Monospace (الخط أحادي العرض). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:86]

```
87:                 fontWeight = FontWeight.Bold,
```
> يُسنِد للخاصية fontWeight قيمة FontWeight.Bold (عريض). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:87]

```
88:                 color = colorScheme.primary
```
> يُسنِد للخاصية color قيمة colorScheme.primary (اللون الأساسي). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:88]

```
89:             ),
```
> إغلاق استدعاء copy المُسنَد إلى style. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:89]

```
90:             textAlign = TextAlign.Center
```
> يُسنِد للوسيط textAlign قيمة TextAlign.Center (التوسيط). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:90]

```
91:         )
```
> إغلاق استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:91]

```
92: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:92]

```
93:         Card(
```
> يستدعي المُركِّب Card (البطاقة) وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:93]

```
94:             modifier = Modifier.fillMaxWidth(),
```
> يُسنِد للوسيط modifier قيمة Modifier مع تطبيق fillMaxWidth (ملء العرض الأقصى). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:94]

```
95:             colors = CardDefaults.cardColors(
```
> يُسنِد للوسيط colors نتيجة استدعاء CardDefaults.cardColors وتبدأ وُسطاؤها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:95]

```
96:                 containerColor = colorScheme.surfaceVariant.copy(alpha = 0.3f)
```
> يُسنِد للوسيط containerColor (لون الحاوية) نسخة من colorScheme.surfaceVariant بشفافية alpha قيمتها 0.3. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:96]

```
97:             ),
```
> إغلاق استدعاء CardDefaults.cardColors. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:97]

```
98:             elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
```
> يُسنِد للوسيط elevation (الارتفاع) نتيجة CardDefaults.cardElevation بقيمة defaultElevation مقدارها 2 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:98]

```
99:         ) {
```
> إغلاق قائمة وُسطاء Card وبداية كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:99]

```
100:             Column(
```
> يستدعي المُركِّب Column وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:100]

```
101:                 modifier = Modifier.padding(16.dp),
```
> يُسنِد للوسيط modifier قيمة Modifier مع تطبيق padding مقدارها 16 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:101]

```
102:                 verticalArrangement = Arrangement.spacedBy(8.dp)
```
> يُسنِد للوسيط verticalArrangement قيمة Arrangement.spacedBy بمسافة 8 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:102]

```
103:             ) {
```
> إغلاق قائمة وُسطاء Column وبداية كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:103]

```
104:                     Text(
```
> يستدعي المُركِّب Text وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:104]

```
105:                         text = stringResource(R.string.bluetooth_needs_for),
```
> يُسنِد للوسيط text قيمة النص المُحمَّل من المورد R.string.bluetooth_needs_for. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:105]

```
106:                     style = MaterialTheme.typography.bodyMedium.copy(
```
> يُسنِد للوسيط style نسخة معدَّلة من MaterialTheme.typography.bodyMedium وتبدأ تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:106]

```
107:                         fontWeight = FontWeight.Medium,
```
> يُسنِد للخاصية fontWeight قيمة FontWeight.Medium (متوسط). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:107]

```
108:                         color = colorScheme.onSurface
```
> يُسنِد للخاصية color قيمة colorScheme.onSurface (اللون فوق السطح). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:108]

```
109:                     ),
```
> إغلاق استدعاء copy المُسنَد إلى style. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:109]

```
110:                     textAlign = TextAlign.Center,
```
> يُسنِد للوسيط textAlign قيمة TextAlign.Center. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:110]

```
111:                     modifier = Modifier.fillMaxWidth()
```
> يُسنِد للوسيط modifier قيمة Modifier مع تطبيق fillMaxWidth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:111]

```
112:                 )
```
> إغلاق استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:112]

```
113:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:113]

```
114:                     Text(
```
> يستدعي المُركِّب Text وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:114]

```
115:                         text = stringResource(R.string.bluetooth_needs_bullets),
```
> يُسنِد للوسيط text قيمة النص المُحمَّل من المورد R.string.bluetooth_needs_bullets. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:115]

```
116:                     style = MaterialTheme.typography.bodySmall.copy(
```
> يُسنِد للوسيط style نسخة معدَّلة من MaterialTheme.typography.bodySmall وتبدأ تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:116]

```
117:                         fontFamily = FontFamily.Monospace,
```
> يُسنِد للخاصية fontFamily قيمة FontFamily.Monospace. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:117]

```
118:                         color = colorScheme.onSurface.copy(alpha = 0.8f)
```
> يُسنِد للخاصية color نسخة من colorScheme.onSurface بشفافية alpha قيمتها 0.8. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:118]

```
119:                     )
```
> إغلاق استدعاء copy المُسنَد إلى style. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:119]

```
120:                 )
```
> إغلاق استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:120]

```
121:             }
```
> إغلاق نطاق (إغلاق كتلة محتوى Column الداخلي). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:121]

```
122:         }
```
> إغلاق نطاق (إغلاق كتلة محتوى Card). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:122]

```
123: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:123]

```
124:         if (isLoading) {
```
> يبدأ شرط if يفحص قيمة isLoading. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:124]

```
125:             BluetoothLoadingIndicator()
```
> يستدعي المُركِّب BluetoothLoadingIndicator (مؤشّر تحميل البلوتوث) بلا وُسطاء. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:125]

```
126:         } else {
```
> إغلاق كتلة if وبداية كتلة else (وإلّا). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:126]

```
127:             Column(
```
> يستدعي المُركِّب Column وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:127]

```
128:                 verticalArrangement = Arrangement.spacedBy(12.dp),
```
> يُسنِد للوسيط verticalArrangement قيمة Arrangement.spacedBy بمسافة 12 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:128]

```
129:                 horizontalAlignment = Alignment.CenterHorizontally
```
> يُسنِد للوسيط horizontalAlignment قيمة Alignment.CenterHorizontally. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:129]

```
130:             ) {
```
> إغلاق قائمة وُسطاء Column وبداية كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:130]

```
131:                 Button(
```
> يستدعي المُركِّب Button (الزر) وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:131]

```
132:                     onClick = onEnableBluetooth,
```
> يُسنِد للوسيط onClick (عند النقر) قيمة onEnableBluetooth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:132]

```
133:                     modifier = Modifier.fillMaxWidth(),
```
> يُسنِد للوسيط modifier قيمة Modifier مع تطبيق fillMaxWidth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:133]

```
134:                     colors = ButtonDefaults.buttonColors(
```
> يُسنِد للوسيط colors نتيجة استدعاء ButtonDefaults.buttonColors وتبدأ وُسطاؤها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:134]

```
135:                         containerColor = Color(0xFF00C851) // App's main green color
```
> يُسنِد للوسيط containerColor لوناً قيمته 0xFF00C851، مع تعليق: لون التطبيق الأخضر الرئيسي. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:135]

```
136:                     )
```
> إغلاق استدعاء ButtonDefaults.buttonColors. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:136]

```
137:                 ) {
```
> إغلاق قائمة وُسطاء Button وبداية كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:137]

```
138:                         Text(
```
> يستدعي المُركِّب Text وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:138]

```
139:                             text = stringResource(R.string.enable_bluetooth),
```
> يُسنِد للوسيط text قيمة النص المُحمَّل من المورد R.string.enable_bluetooth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:139]

```
140:                         style = MaterialTheme.typography.bodyMedium.copy(
```
> يُسنِد للوسيط style نسخة معدَّلة من MaterialTheme.typography.bodyMedium وتبدأ تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:140]

```
141:                             fontFamily = FontFamily.Monospace,
```
> يُسنِد للخاصية fontFamily قيمة FontFamily.Monospace. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:141]

```
142:                             fontWeight = FontWeight.Bold
```
> يُسنِد للخاصية fontWeight قيمة FontWeight.Bold. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:142]

```
143:                         ),
```
> إغلاق استدعاء copy المُسنَد إلى style. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:143]

```
144:                         modifier = Modifier.padding(vertical = 4.dp)
```
> يُسنِد للوسيط modifier قيمة Modifier مع تطبيق padding عمودي (vertical) مقدارها 4 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:144]

```
145:                     )
```
> إغلاق استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:145]

```
146:                 }
```
> إغلاق نطاق (إغلاق كتلة محتوى Button). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:146]

```
147: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:147]

```
148:                 TextButton(
```
> يستدعي المُركِّب TextButton (الزر النصّي) وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:148]

```
149:                     onClick = onSkip,
```
> يُسنِد للوسيط onClick قيمة onSkip. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:149]

```
150:                     modifier = Modifier.fillMaxWidth()
```
> يُسنِد للوسيط modifier قيمة Modifier مع تطبيق fillMaxWidth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:150]

```
151:                 ) {
```
> إغلاق قائمة وُسطاء TextButton وبداية كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:151]

```
152:                     Text(
```
> يستدعي المُركِّب Text وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:152]

```
153:                         text = stringResource(R.string.skip),
```
> يُسنِد للوسيط text قيمة النص المُحمَّل من المورد R.string.skip. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:153]

```
154:                         style = MaterialTheme.typography.labelLarge.copy(
```
> يُسنِد للوسيط style نسخة معدَّلة من MaterialTheme.typography.labelLarge وتبدأ تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:154]

```
155:                             color = colorScheme.onSurface.copy(alpha = 0.7f)
```
> يُسنِد للخاصية color نسخة من colorScheme.onSurface بشفافية alpha قيمتها 0.7. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:155]

```
156:                         )
```
> إغلاق استدعاء copy المُسنَد إلى style. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:156]

```
157:                     )
```
> إغلاق استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:157]

```
158:                 }
```
> إغلاق نطاق (إغلاق كتلة محتوى TextButton). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:158]

```
159:             }
```
> إغلاق نطاق (إغلاق كتلة محتوى Column في فرع else). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:159]

```
160:         }
```
> إغلاق نطاق (إغلاق كتلة else). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:160]

```
161:     }
```
> إغلاق نطاق (إغلاق كتلة محتوى Column الخارجي). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:161]

```
162: }
```
> إغلاق نطاق (إغلاق دالة BluetoothDisabledContent). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:162]

```
163: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:163]

```
164: @Composable
```
> يضع الوسم @Composable على الدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:164]

```
165: private fun BluetoothNotSupportedContent(
```
> يُعرِّف دالة خاصة باسم BluetoothNotSupportedContent وتبدأ قائمة وُسطائها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:165]

```
166:     colorScheme: ColorScheme,
```
> وسيط باسم colorScheme من نوع ColorScheme. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:166]

```
167:     onSkip: () -> Unit
```
> وسيط باسم onSkip من نوع دالة لا تأخذ وُسطاء وتُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:167]

```
168: ) {
```
> إغلاق قائمة الوُسطاء وبداية جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:168]

```
169:     Column(
```
> يستدعي المُركِّب Column وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:169]

```
170:         verticalArrangement = Arrangement.spacedBy(24.dp),
```
> يُسنِد للوسيط verticalArrangement قيمة Arrangement.spacedBy بمسافة 24 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:170]

```
171:         horizontalAlignment = Alignment.CenterHorizontally
```
> يُسنِد للوسيط horizontalAlignment قيمة Alignment.CenterHorizontally. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:171]

```
172:     ) {
```
> إغلاق قائمة وُسطاء Column وبداية كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:172]

```
173:         // Error icon
```
> تعليق: أيقونة الخطأ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:173]

```
174:         Card(
```
> يستدعي المُركِّب Card وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:174]

```
175:             colors = CardDefaults.cardColors(
```
> يُسنِد للوسيط colors نتيجة استدعاء CardDefaults.cardColors وتبدأ وُسطاؤها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:175]

```
176:                 containerColor = Color(0xFFFFEBEE)
```
> يُسنِد للوسيط containerColor لوناً قيمته 0xFFFFEBEE. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:176]

```
177:             ),
```
> إغلاق استدعاء CardDefaults.cardColors. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:177]

```
178:             elevation = CardDefaults.cardElevation(defaultElevation = 4.dp)
```
> يُسنِد للوسيط elevation نتيجة CardDefaults.cardElevation بقيمة defaultElevation مقدارها 4 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:178]

```
179:         ) {
```
> إغلاق قائمة وُسطاء Card وبداية كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:179]

```
180:             Text(
```
> يستدعي المُركِّب Text وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:180]

```
181:                 text = stringResource(R.string.warning_emoji),
```
> يُسنِد للوسيط text قيمة النص المُحمَّل من المورد R.string.warning_emoji. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:181]

```
182:                 style = MaterialTheme.typography.headlineLarge,
```
> يُسنِد للوسيط style قيمة MaterialTheme.typography.headlineLarge. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:182]

```
183:                 modifier = Modifier.padding(16.dp)
```
> يُسنِد للوسيط modifier قيمة Modifier مع تطبيق padding مقدارها 16 dp. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:183]

```
184:             )
```
> إغلاق استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:184]

```
185:         }
```
> إغلاق نطاق (إغلاق كتلة محتوى Card). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:185]

```
186: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:186]

```
187:         Text(
```
> يستدعي المُركِّب Text وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:187]

```
188:             text = stringResource(R.string.bluetooth_not_supported),
```
> يُسنِد للوسيط text قيمة النص المُحمَّل من المورد R.string.bluetooth_not_supported. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:188]

```
189:             style = MaterialTheme.typography.headlineSmall.copy(
```
> يُسنِد للوسيط style نسخة معدَّلة من MaterialTheme.typography.headlineSmall وتبدأ تعديلاتها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:189]

```
190:                 fontFamily = FontFamily.Monospace,
```
> يُسنِد للخاصية fontFamily قيمة FontFamily.Monospace. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:190]

```
191:                 fontWeight = FontWeight.Bold,
```
> يُسنِد للخاصية fontWeight قيمة FontWeight.Bold. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:191]

```
192:                 color = colorScheme.error
```
> يُسنِد للخاصية color قيمة colorScheme.error (لون الخطأ). [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:192]

```
193:             ),
```
> إغلاق استدعاء copy المُسنَد إلى style. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:193]

```
194:             textAlign = TextAlign.Center
```
> يُسنِد للوسيط textAlign قيمة TextAlign.Center. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:194]

```
195:         )
```
> إغلاق استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:195]

```
196: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:196]

```
197:         Card(
```
> يستدعي المُركِّب Card وتبدأ قائمة وُسطائه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:197]

```
198:             modifier = Modifier.fillMaxWidth(),
```
> يُسنِد للوسيط modifier قيمة Modifier مع تطبيق fillMaxWidth. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:198]

```
199:             colors = CardDefaults.cardColors(
```
> يُسنِد للوسيط colors نتيجة استدعاء CardDefaults.cardColors وتبدأ وُسطاؤها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:199]

```
200:                 containerColor = colorScheme.errorContainer.copy(alpha = 0.1f)
```
> يُسنِد للوسيط containerColor نسخة من colorScheme.errorContainer (حاوية الخطأ) بشفافية alpha قيمتها 0.1. [app/src/main/java/com/bitchat/android/onboarding/BluetoothCheckScreen.kt:200]
