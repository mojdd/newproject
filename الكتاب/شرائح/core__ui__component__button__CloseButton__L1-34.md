# شريحة — app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt (الأسطر 1–34)

```
1: package com.bitchat.android.core.ui.component.button
```
> يُعرّف هذا السطر الحزمة (package) التي ينتمي إليها الملف باسم `com.bitchat.android.core.ui.component.button`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:2]

```
3: import androidx.compose.foundation.layout.size
```
> يستورد (import) المُعدِّل `size` من حزمة `androidx.compose.foundation.layout`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:3]

```
4: import androidx.compose.material.icons.Icons
```
> يستورد (import) الكائن `Icons` من حزمة `androidx.compose.material.icons`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:4]

```
5: import androidx.compose.material.icons.filled.Close
```
> يستورد (import) الأيقونة `Close` (إغلاق) من حزمة `androidx.compose.material.icons.filled`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:5]

```
6: import androidx.compose.material3.Icon
```
> يستورد (import) المُكوِّن `Icon` (أيقونة) من حزمة `androidx.compose.material3`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:6]

```
7: import androidx.compose.material3.IconButton
```
> يستورد (import) المُكوِّن `IconButton` (زرّ الأيقونة) من حزمة `androidx.compose.material3`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:7]

```
8: import androidx.compose.material3.IconButtonDefaults
```
> يستورد (import) الكائن `IconButtonDefaults` (افتراضيات زرّ الأيقونة) من حزمة `androidx.compose.material3`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:8]

```
9: import androidx.compose.material3.MaterialTheme
```
> يستورد (import) الكائن `MaterialTheme` (سمة ماتيريال) من حزمة `androidx.compose.material3`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:9]

```
10: import androidx.compose.runtime.Composable
```
> يستورد (import) التعليق التوضيحي `Composable` (قابل للتركيب) من حزمة `androidx.compose.runtime`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:10]

```
11: import androidx.compose.ui.Modifier
```
> يستورد (import) الصنف `Modifier` (المُعدِّل) من حزمة `androidx.compose.ui`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:11]

```
12: import androidx.compose.ui.unit.dp
```
> يستورد (import) الامتداد `dp` (وحدة البكسل المستقل عن الكثافة) من حزمة `androidx.compose.ui.unit`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:12]

```
13: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:13]

```
14: @Composable
```
> يضع التعليق التوضيحي `@Composable` (قابل للتركيب) على الدالة التالية ليجعلها دالة تركيب لواجهة المستخدم. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:14]

```
15: fun CloseButton(
```
> يُعرّف الدالة `CloseButton` (زرّ الإغلاق) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:15]

```
16:     onClick: () -> Unit,
```
> يُعرّف المعامل `onClick` (عند النقر) من نوع دالة لا تأخذ مدخلات وتُعيد `Unit` (لا شيء). [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:16]

```
17:     modifier: Modifier = Modifier.Companion
```
> يُعرّف المعامل `modifier` (المُعدِّل) من نوع `Modifier` بقيمة افتراضية هي الكائن المرافق `Modifier.Companion`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:17]

```
18: ) {
```
> يُغلق قائمة معاملات الدالة `CloseButton` ويفتح جسمها. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:18]

```
19:     IconButton(
```
> يستدعي المُكوِّن `IconButton` (زرّ الأيقونة) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:19]

```
20:         onClick = onClick,
```
> يمرّر الوسيط `onClick` للمُكوِّن `IconButton` بقيمة المعامل `onClick` الممرَّر للدالة. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:20]

```
21:         modifier = modifier
```
> يمرّر الوسيط `modifier` للمُكوِّن `IconButton` ابتداءً بقيمة المعامل `modifier` ثم يُكمَّل في السطر التالي. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:21]

```
22:             .size(32.dp),
```
> يستدعي المُعدِّل `size` على `modifier` بقيمة `32.dp` لضبط حجم الزرّ إلى ٣٢ وحدة بكسل مستقلة عن الكثافة. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:22]

```
23:         colors = IconButtonDefaults.iconButtonColors(
```
> يمرّر الوسيط `colors` للمُكوِّن `IconButton` عبر استدعاء الدالة `iconButtonColors` من `IconButtonDefaults` ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:23]

```
24:             contentColor = MaterialTheme.colorScheme.onBackground.copy(alpha = 0.6f),
```
> يضبط الوسيط `contentColor` (لون المحتوى) إلى لون `onBackground` من مخطّط ألوان `MaterialTheme` بعد نسخه بقيمة شفافية `alpha` تساوي `0.6f`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:24]

```
25:             containerColor = MaterialTheme.colorScheme.onBackground.copy(alpha = 0.1f)
```
> يضبط الوسيط `containerColor` (لون الحاوية) إلى لون `onBackground` من مخطّط ألوان `MaterialTheme` بعد نسخه بقيمة شفافية `alpha` تساوي `0.1f`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:25]

```
26:         )
```
> يُغلق قائمة وسائط استدعاء الدالة `iconButtonColors`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:26]

```
27:     ) {
```
> يُغلق قائمة وسائط المُكوِّن `IconButton` ويفتح كتلة محتواه (لامبدا المحتوى). [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:27]

```
28:         Icon(
```
> يستدعي المُكوِّن `Icon` (أيقونة) ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:28]

```
29:             imageVector = Icons.Default.Close,
```
> يضبط الوسيط `imageVector` (متجه الصورة) إلى الأيقونة `Icons.Default.Close` (أيقونة الإغلاق الافتراضية). [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:29]

```
30:             contentDescription = "Close",
```
> يضبط الوسيط `contentDescription` (وصف المحتوى) إلى السلسلة الحرفية `"Close"`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:30]

```
31:             modifier = Modifier.Companion.size(18.dp)
```
> يضبط الوسيط `modifier` للمُكوِّن `Icon` إلى الكائن المرافق `Modifier.Companion` مع استدعاء المُعدِّل `size` بقيمة `18.dp` لضبط حجم الأيقونة إلى ١٨ وحدة بكسل مستقلة عن الكثافة. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:31]

```
32:         )
```
> يُغلق قائمة وسائط المُكوِّن `Icon`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:32]

```
33:     }
```
> إغلاق نطاق كتلة محتوى المُكوِّن `IconButton`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:33]

```
34: }
```
> إغلاق نطاق جسم الدالة `CloseButton`. [app/src/main/java/com/bitchat/android/core/ui/component/button/CloseButton.kt:34]
