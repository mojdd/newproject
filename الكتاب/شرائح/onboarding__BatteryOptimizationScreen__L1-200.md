# شريحة — app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt (الأسطر 1–200)

```
1: package com.bitchat.android.onboarding
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.onboarding. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:2]

```
3: import androidx.compose.animation.core.*
```
> يستورد (import) كل ما في الحزمة androidx.compose.animation.core. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:3]

```
4: import androidx.compose.foundation.layout.*
```
> يستورد كل ما في حزمة التخطيط androidx.compose.foundation.layout. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:4]

```
5: import androidx.compose.foundation.rememberScrollState
```
> يستورد الدالة rememberScrollState من حزمة androidx.compose.foundation. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:5]

```
6: import androidx.compose.foundation.shape.RoundedCornerShape
```
> يستورد الشكل RoundedCornerShape (شكل بزوايا دائرية) من حزمة androidx.compose.foundation.shape. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:6]

```
7: import androidx.compose.foundation.verticalScroll
```
> يستورد المُعدِّل verticalScroll (تمرير عمودي) من حزمة androidx.compose.foundation. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:7]

```
8: import androidx.compose.material.icons.Icons
```
> يستورد الكائن Icons من حزمة androidx.compose.material.icons. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:8]

```
9: import androidx.compose.material.icons.filled.*
```
> يستورد كل الأيقونات المملوءة (filled) من حزمة androidx.compose.material.icons.filled. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:9]

```
10: import androidx.compose.material.icons.outlined.*
```
> يستورد كل الأيقونات المُحاطة بإطار (outlined) من حزمة androidx.compose.material.icons.outlined. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:10]

```
11: import androidx.compose.material3.*
```
> يستورد كل ما في حزمة androidx.compose.material3. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:11]

```
12: import androidx.compose.runtime.*
```
> يستورد كل ما في حزمة وقت التشغيل androidx.compose.runtime. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:12]

```
13: import androidx.compose.ui.Alignment
```
> يستورد Alignment (المحاذاة) من حزمة androidx.compose.ui. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:13]

```
14: import androidx.compose.ui.Modifier
```
> يستورد Modifier (المُعدِّل) من حزمة androidx.compose.ui. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:14]

```
15: import androidx.compose.ui.draw.rotate
```
> يستورد المُعدِّل rotate (تدوير) من حزمة androidx.compose.ui.draw. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:15]

```
16: import androidx.compose.ui.platform.LocalContext
```
> يستورد LocalContext (السياق المحلي) من حزمة androidx.compose.ui.platform. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:16]

```
17: import androidx.compose.ui.res.stringResource
```
> يستورد الدالة stringResource (مورد نصّي) من حزمة androidx.compose.ui.res. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:17]

```
18: import androidx.compose.ui.text.font.FontFamily
```
> يستورد FontFamily (عائلة الخط) من حزمة androidx.compose.ui.text.font. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:18]

```
19: import androidx.compose.ui.text.font.FontWeight
```
> يستورد FontWeight (سُمك الخط) من حزمة androidx.compose.ui.text.font. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:19]

```
20: import androidx.compose.ui.text.style.TextAlign
```
> يستورد TextAlign (محاذاة النص) من حزمة androidx.compose.ui.text.style. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:20]

```
21: import androidx.compose.ui.unit.dp
```
> يستورد الوحدة dp (وحدة بكسل مستقلة عن الكثافة) من حزمة androidx.compose.ui.unit. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:21]

```
22: import androidx.compose.ui.unit.sp
```
> يستورد الوحدة sp (وحدة حجم النص) من حزمة androidx.compose.ui.unit. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:22]

```
23: import com.bitchat.android.R
```
> يستورد الفئة R (مولّد الموارد) من حزمة com.bitchat.android. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:24]

```
25: /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:25]

```
26:  * Screen shown when checking battery optimization status or requesting battery optimization disable
```
> تعليق: شاشة تُعرض عند فحص حالة تحسين البطارية أو طلب تعطيل تحسين البطارية. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:26]

```
27:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:28]

```
29: @Composable
```
> توسيم بالشارة @Composable للدالة التالية ليجعلها دالة قابلة للتركيب في Compose. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:29]

```
30: fun BatteryOptimizationScreen(
```
> يُعرّف دالة (fun) باسم BatteryOptimizationScreen (شاشة تحسين البطارية) وتبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:30]

```
31:     modifier: Modifier,
```
> يعلن معاملاً باسم modifier من نوع Modifier. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:31]

```
32:     status: BatteryOptimizationStatus,
```
> يعلن معاملاً باسم status من نوع BatteryOptimizationStatus (حالة تحسين البطارية). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:32]

```
33:     onDisableBatteryOptimization: () -> Unit,
```
> يعلن معاملاً باسم onDisableBatteryOptimization (عند تعطيل تحسين البطارية) من نوع دالة لا تأخذ وسائط ولا تعيد قيمة (Unit). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:33]

```
34:     onRetry: () -> Unit,
```
> يعلن معاملاً باسم onRetry (عند إعادة المحاولة) من نوع دالة لا تأخذ وسائط ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:34]

```
35:     onSkip: () -> Unit,
```
> يعلن معاملاً باسم onSkip (عند التخطّي) من نوع دالة لا تأخذ وسائط ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:35]

```
36:     isLoading: Boolean = false
```
> يعلن معاملاً باسم isLoading (هل يجري التحميل) من نوع Boolean بقيمة افتراضية false. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:36]

```
37: ) {
```
> إغلاق قائمة المعاملات وبدء جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:37]

```
38:     val context = LocalContext.current
```
> يعرّف قيمة ثابتة (val) باسم context تُسند إليها القيمة الحالية LocalContext.current. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:38]

```
39:     val colorScheme = MaterialTheme.colorScheme
```
> يعرّف قيمة ثابتة باسم colorScheme تُسند إليها MaterialTheme.colorScheme (نظام ألوان السمة). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:39]

```
40:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:40]

```
41:     // Initialize preference manager
```
> تعليق: تهيئة مدير التفضيلات. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:41]

```
42:     LaunchedEffect(Unit) {
```
> يستدعي LaunchedEffect مع المفتاح Unit ويبدأ كتلته (تأثير يُشغَّل مرة واحدة). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:42]

```
43:         BatteryOptimizationPreferenceManager.init(context)
```
> يستدعي الدالة init على الكائن BatteryOptimizationPreferenceManager (مدير تفضيلات تحسين البطارية) ويمرّر إليها context. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:43]

```
44:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:44]

```
45: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:45]

```
46:     Box(
```
> يستدعي العنصر القابل للتركيب Box ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:46]

```
47:         modifier = modifier.padding(24.dp),
```
> يضبط الوسيط modifier على modifier مع تطبيق padding (حشوة) بمقدار 24.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:47]

```
48:         contentAlignment = Alignment.Center
```
> يضبط الوسيط contentAlignment (محاذاة المحتوى) على Alignment.Center (المركز). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:48]

```
49:     ) {
```
> إغلاق وسائط Box وبدء كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:49]

```
50:         when (status) {
```
> يبدأ تعبير when يفحص قيمة status. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:50]

```
51:             BatteryOptimizationStatus.ENABLED -> {
```
> فرع when للقيمة BatteryOptimizationStatus.ENABLED (مُفعَّل) وبدء كتلته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:51]

```
52:                 BatteryOptimizationEnabledContent(
```
> يستدعي الدالة BatteryOptimizationEnabledContent (محتوى حالة التفعيل) ويبدأ قائمة وسائطها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:52]

```
53:                     onDisableBatteryOptimization = onDisableBatteryOptimization,
```
> يمرّر الوسيط onDisableBatteryOptimization مُسنَداً إلى المعامل onDisableBatteryOptimization. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:53]

```
54:                     onRetry = onRetry,
```
> يمرّر الوسيط onRetry مُسنَداً إلى المعامل onRetry. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:54]

```
55:                     onSkip = onSkip,
```
> يمرّر الوسيط onSkip مُسنَداً إلى المعامل onSkip. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:55]

```
56:                     colorScheme = colorScheme,
```
> يمرّر الوسيط colorScheme مُسنَداً إلى المعامل colorScheme. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:56]

```
57:                     isLoading = isLoading
```
> يمرّر الوسيط isLoading مُسنَداً إلى المعامل isLoading. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:57]

```
58:                 )
```
> إغلاق وسائط استدعاء BatteryOptimizationEnabledContent. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:58]

```
59:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:59]

```
60:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:60]

```
61:             BatteryOptimizationStatus.DISABLED -> {
```
> فرع when للقيمة BatteryOptimizationStatus.DISABLED (مُعطَّل) وبدء كتلته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:61]

```
62:                 BatteryOptimizationCheckingContent(
```
> يستدعي الدالة BatteryOptimizationCheckingContent (محتوى حالة الفحص) ويبدأ قائمة وسائطها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:62]

```
63:                     colorScheme = colorScheme
```
> يمرّر الوسيط colorScheme مُسنَداً إلى المعامل colorScheme. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:63]

```
64:                 )
```
> إغلاق وسائط استدعاء BatteryOptimizationCheckingContent. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:64]

```
65:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:65]

```
66:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:66]

```
67:             BatteryOptimizationStatus.NOT_SUPPORTED -> {
```
> فرع when للقيمة BatteryOptimizationStatus.NOT_SUPPORTED (غير مدعوم) وبدء كتلته. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:67]

```
68:                 BatteryOptimizationNotSupportedContent(
```
> يستدعي الدالة BatteryOptimizationNotSupportedContent (محتوى حالة عدم الدعم) ويبدأ قائمة وسائطها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:68]

```
69:                     onRetry = onRetry,
```
> يمرّر الوسيط onRetry مُسنَداً إلى المعامل onRetry. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:69]

```
70:                     colorScheme = colorScheme
```
> يمرّر الوسيط colorScheme مُسنَداً إلى المعامل colorScheme. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:70]

```
71:                 )
```
> إغلاق وسائط استدعاء BatteryOptimizationNotSupportedContent. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:71]

```
72:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:72]

```
73:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:73]

```
74:     }
```
> إغلاق نطاق كتلة Box. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:74]

```
75: }
```
> إغلاق نطاق دالة BatteryOptimizationScreen. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:75]

```
76: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:76]

```
77: @Composable
```
> توسيم بالشارة @Composable للدالة التالية. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:77]

```
78: private fun BatteryOptimizationEnabledContent(
```
> يُعرّف دالة خاصة (private fun) باسم BatteryOptimizationEnabledContent وتبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:78]

```
79:     onDisableBatteryOptimization: () -> Unit,
```
> يعلن معاملاً باسم onDisableBatteryOptimization من نوع دالة لا تأخذ وسائط ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:79]

```
80:     onRetry: () -> Unit,
```
> يعلن معاملاً باسم onRetry من نوع دالة لا تأخذ وسائط ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:80]

```
81:     onSkip: () -> Unit,
```
> يعلن معاملاً باسم onSkip من نوع دالة لا تأخذ وسائط ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:81]

```
82:     colorScheme: ColorScheme,
```
> يعلن معاملاً باسم colorScheme من نوع ColorScheme. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:82]

```
83:     isLoading: Boolean
```
> يعلن معاملاً باسم isLoading من نوع Boolean. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:83]

```
84: ) {
```
> إغلاق قائمة المعاملات وبدء جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:84]

```
85:     val context = LocalContext.current
```
> يعرّف قيمة ثابتة باسم context تُسند إليها LocalContext.current. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:85]

```
86:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:86]

```
87:     Column(
```
> يستدعي العنصر القابل للتركيب Column (عمود) ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:87]

```
88:         modifier = Modifier.fillMaxSize()
```
> يضبط الوسيط modifier على Modifier مع fillMaxSize (ملء كامل الحجم). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:88]

```
89:     ) {
```
> إغلاق وسائط Column وبدء كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:89]

```
90:         // Scrollable content area
```
> تعليق: منطقة محتوى قابلة للتمرير. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:90]

```
91:         Column(
```
> يستدعي العنصر القابل للتركيب Column ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:91]

```
92:             modifier = Modifier
```
> يبدأ ضبط الوسيط modifier على Modifier (يتبعه سلسلة مُعدِّلات). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:92]

```
93:                 .weight(1f)
```
> يطبّق المُعدِّل weight (الوزن) بقيمة 1f. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:93]

```
94:                 .verticalScroll(rememberScrollState())
```
> يطبّق المُعدِّل verticalScroll (تمرير عمودي) ويمرّر إليه rememberScrollState(). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:94]

```
95:                 .padding(bottom = 16.dp),
```
> يطبّق المُعدِّل padding بحشوة سفلية (bottom) مقدارها 16.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:95]

```
96:             verticalArrangement = Arrangement.spacedBy(16.dp)
```
> يضبط الوسيط verticalArrangement (الترتيب العمودي) على Arrangement.spacedBy بمسافة 16.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:96]

```
97:         ) {
```
> إغلاق وسائط Column وبدء كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:97]

```
98:             // Header Section - matching AboutSheet style
```
> تعليق: قسم العنوان - مطابق لأسلوب AboutSheet. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:98]

```
99:             Column(
```
> يستدعي العنصر القابل للتركيب Column ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:99]

```
100:                 modifier = Modifier
```
> يبدأ ضبط الوسيط modifier على Modifier (يتبعه سلسلة مُعدِّلات). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:100]

```
101:                     .fillMaxWidth()
```
> يطبّق المُعدِّل fillMaxWidth (ملء كامل العرض). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:101]

```
102:                     .padding(bottom = 16.dp),
```
> يطبّق المُعدِّل padding بحشوة سفلية مقدارها 16.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:102]

```
103:                 verticalArrangement = Arrangement.spacedBy(8.dp)
```
> يضبط الوسيط verticalArrangement على Arrangement.spacedBy بمسافة 8.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:103]

```
104:             ) {
```
> إغلاق وسائط Column وبدء كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:104]

```
105:                     Text(
```
> يستدعي العنصر القابل للتركيب Text (نص) ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:105]

```
106:                         text = stringResource(R.string.app_name),
```
> يضبط الوسيط text على نتيجة stringResource للمورد R.string.app_name (اسم التطبيق). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:106]

```
107:                     style = MaterialTheme.typography.headlineLarge.copy(
```
> يضبط الوسيط style على MaterialTheme.typography.headlineLarge مع استدعاء copy لبدء تعديل خصائصه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:107]

```
108:                         fontFamily = FontFamily.Monospace,
```
> يضبط الخاصية fontFamily على FontFamily.Monospace (خط أحادي المسافة). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:108]

```
109:                         fontWeight = FontWeight.Bold,
```
> يضبط الخاصية fontWeight على FontWeight.Bold (عريض). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:109]

```
110:                         fontSize = 32.sp
```
> يضبط الخاصية fontSize (حجم الخط) على 32.sp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:110]

```
111:                     ),
```
> إغلاق استدعاء copy للنمط. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:111]

```
112:                     color = colorScheme.onBackground
```
> يضبط الوسيط color على colorScheme.onBackground (لون فوق الخلفية). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:112]

```
113:                 )
```
> إغلاق وسائط استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:113]

```
114: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:114]

```
115:                     Text(
```
> يستدعي العنصر القابل للتركيب Text ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:115]

```
116:                         text = stringResource(R.string.battery_optimization_detected_title),
```
> يضبط الوسيط text على نتيجة stringResource للمورد R.string.battery_optimization_detected_title (عنوان اكتشاف تحسين البطارية). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:116]

```
117:                     fontSize = 12.sp,
```
> يضبط الوسيط fontSize على 12.sp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:117]

```
118:                     fontFamily = FontFamily.Monospace,
```
> يضبط الوسيط fontFamily على FontFamily.Monospace. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:118]

```
119:                     color = colorScheme.onBackground.copy(alpha = 0.7f)
```
> يضبط الوسيط color على colorScheme.onBackground مع copy تضبط alpha (الشفافية) على 0.7f. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:119]

```
120:                 )
```
> إغلاق وسائط استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:120]

```
121:             }
```
> إغلاق نطاق كتلة Column. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:121]

```
122:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:122]

```
123:             // Battery optimization info section
```
> تعليق: قسم معلومات تحسين البطارية. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:123]

```
124:             Surface(
```
> يستدعي العنصر القابل للتركيب Surface (سطح) ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:124]

```
125:                 modifier = Modifier.fillMaxWidth(),
```
> يضبط الوسيط modifier على Modifier مع fillMaxWidth. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:125]

```
126:                 color = colorScheme.surfaceVariant.copy(alpha = 0.25f),
```
> يضبط الوسيط color على colorScheme.surfaceVariant مع copy تضبط alpha على 0.25f. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:126]

```
127:                 shape = RoundedCornerShape(12.dp)
```
> يضبط الوسيط shape (الشكل) على RoundedCornerShape بزوايا 12.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:127]

```
128:             ) {
```
> إغلاق وسائط Surface وبدء كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:128]

```
129:                 Column(
```
> يستدعي العنصر القابل للتركيب Column ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:129]

```
130:                     modifier = Modifier.padding(16.dp),
```
> يضبط الوسيط modifier على Modifier مع padding بمقدار 16.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:130]

```
131:                     verticalArrangement = Arrangement.spacedBy(8.dp)
```
> يضبط الوسيط verticalArrangement على Arrangement.spacedBy بمسافة 8.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:131]

```
132:                 ) {
```
> إغلاق وسائط Column وبدء كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:132]

```
133:                     Row(
```
> يستدعي العنصر القابل للتركيب Row (صف) ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:133]

```
134:                         verticalAlignment = Alignment.Top,
```
> يضبط الوسيط verticalAlignment (المحاذاة العمودية) على Alignment.Top (الأعلى). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:134]

```
135:                         horizontalArrangement = Arrangement.spacedBy(12.dp)
```
> يضبط الوسيط horizontalArrangement (الترتيب الأفقي) على Arrangement.spacedBy بمسافة 12.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:135]

```
136:                     ) {
```
> إغلاق وسائط Row وبدء كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:136]

```
137:                         Icon(
```
> يستدعي العنصر القابل للتركيب Icon (أيقونة) ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:137]

```
138:                             imageVector = Icons.Filled.Power,
```
> يضبط الوسيط imageVector (المتجه الصوري) على Icons.Filled.Power (أيقونة الطاقة المملوءة). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:138]

```
139:                             contentDescription = stringResource(R.string.cd_battery_optimization),
```
> يضبط الوسيط contentDescription (وصف المحتوى) على نتيجة stringResource للمورد R.string.cd_battery_optimization. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:139]

```
140:                             tint = colorScheme.primary,
```
> يضبط الوسيط tint (الصبغة) على colorScheme.primary (اللون الأساسي). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:140]

```
141:                             modifier = Modifier
```
> يبدأ ضبط الوسيط modifier على Modifier (يتبعه سلسلة مُعدِّلات). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:141]

```
142:                                 .padding(top = 2.dp)
```
> يطبّق المُعدِّل padding بحشوة علوية (top) مقدارها 2.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:142]

```
143:                                 .size(20.dp)
```
> يطبّق المُعدِّل size (الحجم) بمقدار 20.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:143]

```
144:                         )
```
> إغلاق وسائط استدعاء Icon. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:144]

```
145:                         Column {
```
> يستدعي العنصر القابل للتركيب Column ويبدأ كتلة محتواه مباشرة (بلا وسائط). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:145]

```
146:                                 Text(
```
> يستدعي العنصر القابل للتركيب Text ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:146]

```
147:                                     text = stringResource(R.string.battery_optimization_enabled_title),
```
> يضبط الوسيط text على نتيجة stringResource للمورد R.string.battery_optimization_enabled_title (عنوان تفعيل تحسين البطارية). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:147]

```
148:                                 style = MaterialTheme.typography.titleMedium,
```
> يضبط الوسيط style على MaterialTheme.typography.titleMedium. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:148]

```
149:                                 fontWeight = FontWeight.Medium,
```
> يضبط الوسيط fontWeight على FontWeight.Medium (متوسط). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:149]

```
150:                                 color = colorScheme.onBackground
```
> يضبط الوسيط color على colorScheme.onBackground. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:150]

```
151:                             )
```
> إغلاق وسائط استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:151]

```
152:                             Spacer(modifier = Modifier.height(4.dp))
```
> يستدعي العنصر القابل للتركيب Spacer (فاصل) مع modifier على Modifier بارتفاع height مقداره 4.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:152]

```
153:                                 Text(
```
> يستدعي العنصر القابل للتركيب Text ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:153]

```
154:                                     text = stringResource(R.string.battery_optimization_explanation_short),
```
> يضبط الوسيط text على نتيجة stringResource للمورد R.string.battery_optimization_explanation_short (شرح مختصر لتحسين البطارية). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:154]

```
155:                                 style = MaterialTheme.typography.bodySmall,
```
> يضبط الوسيط style على MaterialTheme.typography.bodySmall. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:155]

```
156:                                 color = colorScheme.onBackground.copy(alpha = 0.8f)
```
> يضبط الوسيط color على colorScheme.onBackground مع copy تضبط alpha على 0.8f. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:156]

```
157:                             )
```
> إغلاق وسائط استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:157]

```
158:                         }
```
> إغلاق نطاق كتلة Column. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:158]

```
159:                     }
```
> إغلاق نطاق كتلة Row. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:159]

```
160:                 }
```
> إغلاق نطاق كتلة Column. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:160]

```
161:             }
```
> إغلاق نطاق كتلة Surface. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:161]

```
162:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:162]

```
163:             // Benefits section
```
> تعليق: قسم الفوائد. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:163]

```
164:             Surface(
```
> يستدعي العنصر القابل للتركيب Surface ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:164]

```
165:                 modifier = Modifier.fillMaxWidth(),
```
> يضبط الوسيط modifier على Modifier مع fillMaxWidth. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:165]

```
166:                 color = colorScheme.surfaceVariant.copy(alpha = 0.25f),
```
> يضبط الوسيط color على colorScheme.surfaceVariant مع copy تضبط alpha على 0.25f. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:166]

```
167:                 shape = RoundedCornerShape(12.dp)
```
> يضبط الوسيط shape على RoundedCornerShape بزوايا 12.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:167]

```
168:             ) {
```
> إغلاق وسائط Surface وبدء كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:168]

```
169:                 Column(
```
> يستدعي العنصر القابل للتركيب Column ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:169]

```
170:                     modifier = Modifier.padding(16.dp),
```
> يضبط الوسيط modifier على Modifier مع padding بمقدار 16.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:170]

```
171:                     verticalArrangement = Arrangement.spacedBy(8.dp)
```
> يضبط الوسيط verticalArrangement على Arrangement.spacedBy بمسافة 8.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:171]

```
172:                 ) {
```
> إغلاق وسائط Column وبدء كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:172]

```
173:                     Row(
```
> يستدعي العنصر القابل للتركيب Row ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:173]

```
174:                         verticalAlignment = Alignment.Top,
```
> يضبط الوسيط verticalAlignment على Alignment.Top. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:174]

```
175:                         horizontalArrangement = Arrangement.spacedBy(12.dp)
```
> يضبط الوسيط horizontalArrangement على Arrangement.spacedBy بمسافة 12.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:175]

```
176:                     ) {
```
> إغلاق وسائط Row وبدء كتلة محتواه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:176]

```
177:                         Icon(
```
> يستدعي العنصر القابل للتركيب Icon ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:177]

```
178:                             imageVector = Icons.Filled.CheckCircle,
```
> يضبط الوسيط imageVector على Icons.Filled.CheckCircle (أيقونة دائرة الصح المملوءة). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:178]

```
179:                             contentDescription = stringResource(R.string.cd_benefits),
```
> يضبط الوسيط contentDescription على نتيجة stringResource للمورد R.string.cd_benefits. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:179]

```
180:                             tint = colorScheme.primary,
```
> يضبط الوسيط tint على colorScheme.primary. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:180]

```
181:                             modifier = Modifier
```
> يبدأ ضبط الوسيط modifier على Modifier (يتبعه سلسلة مُعدِّلات). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:181]

```
182:                                 .padding(top = 2.dp)
```
> يطبّق المُعدِّل padding بحشوة علوية مقدارها 2.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:182]

```
183:                                 .size(20.dp)
```
> يطبّق المُعدِّل size بمقدار 20.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:183]

```
184:                         )
```
> إغلاق وسائط استدعاء Icon. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:184]

```
185:                         Column {
```
> يستدعي العنصر القابل للتركيب Column ويبدأ كتلة محتواه مباشرة (بلا وسائط). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:185]

```
186:                                 Text(
```
> يستدعي العنصر القابل للتركيب Text ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:186]

```
187:                                     text = stringResource(R.string.benefits_of_disabling),
```
> يضبط الوسيط text على نتيجة stringResource للمورد R.string.benefits_of_disabling (فوائد التعطيل). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:187]

```
188:                                 style = MaterialTheme.typography.titleMedium,
```
> يضبط الوسيط style على MaterialTheme.typography.titleMedium. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:188]

```
189:                                 fontWeight = FontWeight.Medium,
```
> يضبط الوسيط fontWeight على FontWeight.Medium. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:189]

```
190:                                 color = colorScheme.onBackground
```
> يضبط الوسيط color على colorScheme.onBackground. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:190]

```
191:                             )
```
> إغلاق وسائط استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:191]

```
192:                             Spacer(modifier = Modifier.height(4.dp))
```
> يستدعي العنصر القابل للتركيب Spacer مع modifier على Modifier بارتفاع height مقداره 4.dp. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:192]

```
193:                                 Text(
```
> يستدعي العنصر القابل للتركيب Text ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:193]

```
194:                                     text = stringResource(R.string.battery_benefits_short),
```
> يضبط الوسيط text على نتيجة stringResource للمورد R.string.battery_benefits_short (فوائد البطارية المختصرة). [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:194]

```
195:                                 style = MaterialTheme.typography.bodySmall,
```
> يضبط الوسيط style على MaterialTheme.typography.bodySmall. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:195]

```
196:                                 color = colorScheme.onBackground.copy(alpha = 0.8f)
```
> يضبط الوسيط color على colorScheme.onBackground مع copy تضبط alpha على 0.8f. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:196]

```
197:                             )
```
> إغلاق وسائط استدعاء Text. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:197]

```
198:                         }
```
> إغلاق نطاق كتلة Column. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:198]

```
199:                     }
```
> إغلاق نطاق كتلة Row. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:199]

```
200:                 }
```
> إغلاق نطاق كتلة Column. [app/src/main/java/com/bitchat/android/onboarding/BatteryOptimizationScreen.kt:200]
