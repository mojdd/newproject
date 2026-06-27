# شريحة — app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt (الأسطر 1–32)

```
1: package com.bitchat.android.core.ui.component.sheet
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.core.ui.component.sheet`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:2]

```
3: import androidx.compose.foundation.layout.ColumnScope
```
> يستورد النوع نطاق العمود (ColumnScope) من حزمة `androidx.compose.foundation.layout`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:3]

```
4: import androidx.compose.foundation.layout.statusBarsPadding
```
> يستورد الدالة حشوة شريط الحالة (statusBarsPadding) من حزمة `androidx.compose.foundation.layout`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:4]

```
5: import androidx.compose.foundation.shape.RoundedCornerShape
```
> يستورد النوع شكل الزوايا المدوّرة (RoundedCornerShape) من حزمة `androidx.compose.foundation.shape`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:5]

```
6: import androidx.compose.material3.ExperimentalMaterial3Api
```
> يستورد التأشيرة واجهة ماتيريال٣ التجريبية (ExperimentalMaterial3Api) من حزمة `androidx.compose.material3`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:6]

```
7: import androidx.compose.material3.MaterialTheme
```
> يستورد الكائن سمة ماتيريال (MaterialTheme) من حزمة `androidx.compose.material3`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:7]

```
8: import androidx.compose.material3.ModalBottomSheet
```
> يستورد الدالة الورقة السفلية الحوارية (ModalBottomSheet) من حزمة `androidx.compose.material3`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:8]

```
9: import androidx.compose.material3.SheetState
```
> يستورد النوع حالة الورقة (SheetState) من حزمة `androidx.compose.material3`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:9]

```
10: import androidx.compose.material3.rememberModalBottomSheetState
```
> يستورد الدالة تذكُّر حالة الورقة السفلية الحوارية (rememberModalBottomSheetState) من حزمة `androidx.compose.material3`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:10]

```
11: import androidx.compose.runtime.Composable
```
> يستورد التأشيرة قابل للتركيب (Composable) من حزمة `androidx.compose.runtime`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:11]

```
12: import androidx.compose.ui.Modifier
```
> يستورد النوع المُعدِّل (Modifier) من حزمة `androidx.compose.ui`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:12]

```
13: import androidx.compose.ui.unit.dp
```
> يستورد الامتداد بكسل مستقل الكثافة (dp) من حزمة `androidx.compose.ui.unit`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:13]

```
14: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:14]

```
15: @OptIn(ExperimentalMaterial3Api::class)
```
> يضع التأشيرة الاشتراك الصريح (OptIn) للموافقة على استعمال صنف الواجهة التجريبية `ExperimentalMaterial3Api`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:15]

```
16: @Composable
```
> يضع التأشيرة قابل للتركيب (Composable) على الدالة التي تليه. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:16]

```
17: fun BitchatBottomSheet(
```
> يعرّف الدالة القابلة للتركيب ورقة بِتشات السفلية (BitchatBottomSheet) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:17]

```
18:     modifier: Modifier = Modifier,
```
> يعرّف المعامل المُعدِّل (modifier) من النوع `Modifier` بقيمة افتراضية هي الكائن `Modifier` الفارغ. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:18]

```
19:     sheetState: SheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true),
```
> يعرّف المعامل حالة الورقة (sheetState) من النوع `SheetState` بقيمة افتراضية ناتجة عن استدعاء `rememberModalBottomSheetState` مع المعامل `skipPartiallyExpanded` مضبوطاً على `true`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:19]

```
20:     onDismissRequest: () -> Unit,
```
> يعرّف المعامل طلب الإغلاق (onDismissRequest) كدالة بلا وسائط تُعيد `Unit`، بلا قيمة افتراضية. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:20]

```
21:     content: @Composable (ColumnScope.() -> Unit),
```
> يعرّف المعامل المحتوى (content) كدالة قابلة للتركيب موسومة بـ`@Composable` ومستقبِلها هو `ColumnScope` وتُعيد `Unit`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:21]

```
22: ) {
```
> يُغلق قائمة معاملات الدالة ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:22]

```
23:     ModalBottomSheet(
```
> يستدعي الدالة `ModalBottomSheet` ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:23]

```
24:         modifier = modifier.statusBarsPadding(),
```
> يمرّر الوسيط `modifier` بقيمة المعامل `modifier` بعد استدعاء `statusBarsPadding()` عليه. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:24]

```
25:         onDismissRequest = onDismissRequest,
```
> يمرّر الوسيط `onDismissRequest` بقيمة المعامل `onDismissRequest`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:25]

```
26:         sheetState = sheetState,
```
> يمرّر الوسيط `sheetState` بقيمة المعامل `sheetState`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:26]

```
27:         dragHandle = null,
```
> يمرّر الوسيط مقبض السحب (dragHandle) بالقيمة `null`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:27]

```
28:         shape = RoundedCornerShape(topStart = 28.dp, topEnd = 28.dp),
```
> يمرّر الوسيط الشكل (shape) بكائن `RoundedCornerShape` بزاوية بداية علوية `28.dp` وزاوية نهاية علوية `28.dp`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:28]

```
29:         containerColor = MaterialTheme.colorScheme.background,
```
> يمرّر الوسيط لون الحاوية (containerColor) بقيمة `background` من مخطط ألوان `MaterialTheme.colorScheme`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:29]

```
30:         content = content,
```
> يمرّر الوسيط `content` بقيمة المعامل `content`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:30]

```
31:     )
```
> يُغلق قائمة وسائط استدعاء `ModalBottomSheet`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:31]

```
32: }
```
> إغلاق نطاق جسم الدالة `BitchatBottomSheet`. [app/src/main/java/com/bitchat/android/core/ui/component/sheet/BitchatBottomSheet.kt:32]
