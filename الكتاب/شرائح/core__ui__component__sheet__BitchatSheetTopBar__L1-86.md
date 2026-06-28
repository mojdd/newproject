# شريحة — app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt (الأسطر 1–86)

```
1: package com.bitchat.android.core.ui.component.sheet
```
> يُعلِن أنّ هذا الملف ينتمي إلى حزمة (package) باسم `com.bitchat.android.core.ui.component.sheet`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:2]

```
3: import androidx.compose.foundation.layout.RowScope
```
> يستورد النوع `RowScope` (نطاق الصف) من مكتبة androidx.compose.foundation.layout. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:3]

```
4: import androidx.compose.foundation.layout.padding
```
> يستورد الدالة `padding` (الحاشية) من مكتبة androidx.compose.foundation.layout. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:4]

```
5: import androidx.compose.material3.CenterAlignedTopAppBar
```
> يستورد الدالة `CenterAlignedTopAppBar` (شريط علوي محاذى للوسط) من مكتبة androidx.compose.material3. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:5]

```
6: import androidx.compose.material3.ExperimentalMaterial3Api
```
> يستورد المُعلِّم `ExperimentalMaterial3Api` (واجهة برمجة تجريبية) من مكتبة androidx.compose.material3. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:6]

```
7: import androidx.compose.material3.MaterialTheme
```
> يستورد الكائن `MaterialTheme` (سمة ماتيريال) من مكتبة androidx.compose.material3. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:7]

```
8: import androidx.compose.material3.Text
```
> يستورد الدالة `Text` (النص) من مكتبة androidx.compose.material3. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:8]

```
9: import androidx.compose.material3.TopAppBar
```
> يستورد الدالة `TopAppBar` (شريط علوي) من مكتبة androidx.compose.material3. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:9]

```
10: import androidx.compose.material3.TopAppBarDefaults
```
> يستورد الكائن `TopAppBarDefaults` (إعدادات الشريط العلوي الافتراضية) من مكتبة androidx.compose.material3. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:10]

```
11: import androidx.compose.runtime.Composable
```
> يستورد المُعلِّم `Composable` (قابل للتركيب) من مكتبة androidx.compose.runtime. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:11]

```
12: import androidx.compose.ui.Modifier
```
> يستورد النوع `Modifier` (المُعدِّل) من مكتبة androidx.compose.ui. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:12]

```
13: import androidx.compose.ui.text.font.FontFamily
```
> يستورد النوع `FontFamily` (عائلة الخط) من مكتبة androidx.compose.ui.text.font. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:13]

```
14: import androidx.compose.ui.text.font.FontWeight
```
> يستورد النوع `FontWeight` (وزن الخط) من مكتبة androidx.compose.ui.text.font. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:14]

```
15: import androidx.compose.ui.unit.dp
```
> يستورد الامتداد `dp` (وحدة البكسل المستقلة عن الكثافة) من مكتبة androidx.compose.ui.unit. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:15]

```
16: import com.bitchat.android.core.ui.component.button.CloseButton
```
> يستورد الدالة `CloseButton` (زر الإغلاق) من حزمة com.bitchat.android.core.ui.component.button. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:17]

```
18: @OptIn(ExperimentalMaterial3Api::class)
```
> يضع المُعلِّم `@OptIn` ليقبل استعمال واجهة `ExperimentalMaterial3Api` التجريبية. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:18]

```
19: @Composable
```
> يضع المُعلِّم `@Composable` ليجعل الدالة التالية قابلة للتركيب في واجهة Compose. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:19]

```
20: fun BitchatSheetTopBar(
```
> يُعرِّف الدالة `BitchatSheetTopBar` (شريط علوي للورقة) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:20]

```
21:     onClose: () -> Unit,
```
> يُعرِّف المعامل `onClose` (عند الإغلاق) من نوع دالة لا تأخذ مدخلاً وتعيد `Unit` (لا شيء). [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:21]

```
22:     modifier: Modifier = Modifier,
```
> يُعرِّف المعامل `modifier` (المُعدِّل) من نوع `Modifier` بقيمة افتراضية هي الكائن `Modifier` الفارغ. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:22]

```
23:     backgroundAlpha: Float = 0.98f,
```
> يُعرِّف المعامل `backgroundAlpha` (شفافية الخلفية) من نوع `Float` بقيمة افتراضية حرفية `0.98f`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:23]

```
24:     title: @Composable () -> Unit,
```
> يُعرِّف المعامل `title` (العنوان) من نوع دالة قابلة للتركيب لا تأخذ مدخلاً وتعيد `Unit`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:24]

```
25:     navigationIcon: (@Composable () -> Unit)? = null,
```
> يُعرِّف المعامل `navigationIcon` (أيقونة التنقّل) من نوع دالة قابلة للتركيب اختيارية (قابلة للقيمة الفارغة) بقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:25]

```
26:     actions: @Composable RowScope.() -> Unit = {}
```
> يُعرِّف المعامل `actions` (الإجراءات) من نوع دالة قابلة للتركيب بمستقبِل `RowScope` بقيمة افتراضية دالة فارغة `{}`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:26]

```
27: ) {
```
> يُغلق قائمة المعاملات ويفتح جسم الدالة `BitchatSheetTopBar`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:27]

```
28:     TopAppBar(
```
> يستدعي الدالة `TopAppBar` ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:28]

```
29:         title = title,
```
> يمرّر إلى الوسيط `title` قيمة المعامل `title`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:29]

```
30:         navigationIcon = { navigationIcon?.invoke() },
```
> يمرّر إلى الوسيط `navigationIcon` دالة تستدعي المعامل `navigationIcon` عبر `invoke` بشرط عدم كونه فارغاً (استدعاء آمن). [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:30]

```
31:         actions = {
```
> يبدأ تمرير قيمة الوسيط `actions` كدالة قابلة للتركيب يفتح جسمها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:31]

```
32:             actions()
```
> يستدعي المعامل `actions` داخل جسم الوسيط. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:32]

```
33:             CloseButton(
```
> يستدعي الدالة `CloseButton` ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:33]

```
34:                 onClick = onClose,
```
> يمرّر إلى الوسيط `onClick` قيمة المعامل `onClose`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:34]

```
35:                 modifier = Modifier.padding(horizontal = 16.dp)
```
> يمرّر إلى الوسيط `modifier` مُعدِّلاً ناتجاً من `Modifier.padding` بحاشية أفقية مقدارها `16.dp`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:35]

```
36:             )
```
> يُغلق قائمة وسائط استدعاء `CloseButton`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:36]

```
37:         },
```
> يُغلق جسم دالة الوسيط `actions` وينهي تمرير ذلك الوسيط. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:37]

```
38:         colors = TopAppBarDefaults.topAppBarColors(
```
> يمرّر إلى الوسيط `colors` ناتج استدعاء `TopAppBarDefaults.topAppBarColors` ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:38]

```
39:             containerColor = MaterialTheme.colorScheme.background.copy(alpha = backgroundAlpha),
```
> يمرّر إلى الوسيط `containerColor` لون الخلفية `background` من نظام ألوان `MaterialTheme` بعد نسخه بقيمة شفافية `alpha` تساوي `backgroundAlpha`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:39]

```
40:             titleContentColor = MaterialTheme.colorScheme.onSurface,
```
> يمرّر إلى الوسيط `titleContentColor` اللون `onSurface` من نظام ألوان `MaterialTheme`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:40]

```
41:             navigationIconContentColor = MaterialTheme.colorScheme.onSurface,
```
> يمرّر إلى الوسيط `navigationIconContentColor` اللون `onSurface` من نظام ألوان `MaterialTheme`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:41]

```
42:             actionIconContentColor = MaterialTheme.colorScheme.onSurface
```
> يمرّر إلى الوسيط `actionIconContentColor` اللون `onSurface` من نظام ألوان `MaterialTheme`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:42]

```
43:         ),
```
> يُغلق قائمة وسائط `topAppBarColors` وينهي تمرير الوسيط `colors`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:43]

```
44:         modifier = modifier
```
> يمرّر إلى الوسيط `modifier` قيمة المعامل `modifier`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:44]

```
45:     )
```
> يُغلق قائمة وسائط استدعاء `TopAppBar`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:45]

```
46: }
```
> إغلاق نطاق جسم الدالة `BitchatSheetTopBar`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:46]

```
47: @OptIn(ExperimentalMaterial3Api::class)
```
> يضع المُعلِّم `@OptIn` ليقبل استعمال واجهة `ExperimentalMaterial3Api` التجريبية. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:47]

```
48: @Composable
```
> يضع المُعلِّم `@Composable` ليجعل الدالة التالية قابلة للتركيب في واجهة Compose. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:48]

```
49: fun BitchatSheetCenterTopBar(
```
> يُعرِّف الدالة `BitchatSheetCenterTopBar` (شريط علوي للورقة محاذى للوسط) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:49]

```
50:     onClose: () -> Unit,
```
> يُعرِّف المعامل `onClose` (عند الإغلاق) من نوع دالة لا تأخذ مدخلاً وتعيد `Unit`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:50]

```
51:     modifier: Modifier = Modifier,
```
> يُعرِّف المعامل `modifier` من نوع `Modifier` بقيمة افتراضية هي الكائن `Modifier` الفارغ. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:51]

```
52:     backgroundAlpha: Float = 0.98f,
```
> يُعرِّف المعامل `backgroundAlpha` من نوع `Float` بقيمة افتراضية حرفية `0.98f`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:52]

```
53:     title: @Composable () -> Unit,
```
> يُعرِّف المعامل `title` من نوع دالة قابلة للتركيب لا تأخذ مدخلاً وتعيد `Unit`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:53]

```
54:     navigationIcon: (@Composable () -> Unit)? = null,
```
> يُعرِّف المعامل `navigationIcon` من نوع دالة قابلة للتركيب اختيارية بقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:54]

```
55:     actions: @Composable RowScope.() -> Unit = {}
```
> يُعرِّف المعامل `actions` من نوع دالة قابلة للتركيب بمستقبِل `RowScope` بقيمة افتراضية دالة فارغة `{}`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:55]

```
56: ) {
```
> يُغلق قائمة المعاملات ويفتح جسم الدالة `BitchatSheetCenterTopBar`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:56]

```
57:     CenterAlignedTopAppBar(
```
> يستدعي الدالة `CenterAlignedTopAppBar` ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:57]

```
58:         title = title,
```
> يمرّر إلى الوسيط `title` قيمة المعامل `title`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:58]

```
59:         navigationIcon = { navigationIcon?.invoke() },
```
> يمرّر إلى الوسيط `navigationIcon` دالة تستدعي المعامل `navigationIcon` عبر `invoke` بشرط عدم كونه فارغاً (استدعاء آمن). [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:59]

```
60:         actions = {
```
> يبدأ تمرير قيمة الوسيط `actions` كدالة قابلة للتركيب يفتح جسمها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:60]

```
61:             actions()
```
> يستدعي المعامل `actions` داخل جسم الوسيط. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:61]

```
62:             CloseButton(
```
> يستدعي الدالة `CloseButton` ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:62]

```
63:                 onClick = onClose,
```
> يمرّر إلى الوسيط `onClick` قيمة المعامل `onClose`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:63]

```
64:                 modifier = Modifier.padding(horizontal = 16.dp)
```
> يمرّر إلى الوسيط `modifier` مُعدِّلاً ناتجاً من `Modifier.padding` بحاشية أفقية مقدارها `16.dp`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:64]

```
65:             )
```
> يُغلق قائمة وسائط استدعاء `CloseButton`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:65]

```
66:         },
```
> يُغلق جسم دالة الوسيط `actions` وينهي تمرير ذلك الوسيط. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:66]

```
67:         colors = TopAppBarDefaults.topAppBarColors(
```
> يمرّر إلى الوسيط `colors` ناتج استدعاء `TopAppBarDefaults.topAppBarColors` ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:67]

```
68:             containerColor = MaterialTheme.colorScheme.background.copy(alpha = backgroundAlpha),
```
> يمرّر إلى الوسيط `containerColor` لون الخلفية `background` من نظام ألوان `MaterialTheme` بعد نسخه بقيمة شفافية `alpha` تساوي `backgroundAlpha`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:68]

```
69:             titleContentColor = MaterialTheme.colorScheme.onSurface,
```
> يمرّر إلى الوسيط `titleContentColor` اللون `onSurface` من نظام ألوان `MaterialTheme`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:69]

```
70:             navigationIconContentColor = MaterialTheme.colorScheme.onSurface,
```
> يمرّر إلى الوسيط `navigationIconContentColor` اللون `onSurface` من نظام ألوان `MaterialTheme`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:70]

```
71:             actionIconContentColor = MaterialTheme.colorScheme.onSurface
```
> يمرّر إلى الوسيط `actionIconContentColor` اللون `onSurface` من نظام ألوان `MaterialTheme`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:71]

```
72:         ),
```
> يُغلق قائمة وسائط `topAppBarColors` وينهي تمرير الوسيط `colors`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:72]

```
73:         modifier = modifier
```
> يمرّر إلى الوسيط `modifier` قيمة المعامل `modifier`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:73]

```
74:     )
```
> يُغلق قائمة وسائط استدعاء `CenterAlignedTopAppBar`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:74]

```
75: }
```
> إغلاق نطاق جسم الدالة `BitchatSheetCenterTopBar`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:75]

```
76: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:76]

```
77: @Composable
```
> يضع المُعلِّم `@Composable` ليجعل الدالة التالية قابلة للتركيب في واجهة Compose. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:77]

```
78: fun BitchatSheetTitle(text: String) {
```
> يُعرِّف الدالة `BitchatSheetTitle` (عنوان الورقة) بمعامل واحد `text` من نوع `String` ويفتح جسمها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:78]

```
79:     Text(
```
> يستدعي الدالة `Text` ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:79]

```
80:         text = text,
```
> يمرّر إلى الوسيط `text` قيمة المعامل `text`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:80]

```
81:         style = MaterialTheme.typography.titleMedium.copy(
```
> يمرّر إلى الوسيط `style` نمط الخط `titleMedium` من طباعة `MaterialTheme` بعد نسخه بتعديلات، ويفتح قائمة وسائط `copy`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:81]

```
82:             fontWeight = FontWeight.Bold,
```
> يمرّر إلى الوسيط `fontWeight` القيمة `FontWeight.Bold` (خط عريض). [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:82]

```
83:             fontFamily = FontFamily.Monospace
```
> يمرّر إلى الوسيط `fontFamily` القيمة `FontFamily.Monospace` (خط أحادي العرض). [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:83]

```
84:         )
```
> يُغلق قائمة وسائط استدعاء `copy` على نمط `titleMedium`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:84]

```
85:     )
```
> يُغلق قائمة وسائط استدعاء `Text`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:85]

```
86: }
```
> إغلاق نطاق جسم الدالة `BitchatSheetTitle`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatSheetTopBar.kt:86]
