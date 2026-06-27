# شريحة — app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt (الأسطر 1–57)

```
1: package com.bitchat.android.core.ui.utils
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) المسمّاة `com.bitchat.android.core.ui.utils`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:2]

```
3: import androidx.compose.foundation.clickable
```
> يستورد دالة القابلية للنقر (clickable) من مكتبة `androidx.compose.foundation`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:3]

```
4: import androidx.compose.runtime.*
```
> يستورد كل العناصر العامة من حزمة زمن التشغيل (runtime) في `androidx.compose`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:4]

```
5: import androidx.compose.ui.Modifier
```
> يستورد نوع المُعدِّل (Modifier) من حزمة `androidx.compose.ui`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:5]

```
6: import androidx.compose.ui.composed
```
> يستورد دالة المُركَّب (composed) من حزمة `androidx.compose.ui`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:6]

```
7: import kotlinx.coroutines.delay
```
> يستورد دالة التأخير (delay) من مكتبة الكوروتينات `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:7]

```
8: import kotlinx.coroutines.launch
```
> يستورد دالة الإطلاق (launch) من مكتبة الكوروتينات `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:9]

```
10: fun Modifier.singleOrTripleClickable(
```
> يُعرّف دالة امتداد (extension function) باسم النقر الفردي أو الثلاثي (singleOrTripleClickable) على النوع المُعدِّل (Modifier)، ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:10]

```
11:     onSingleClick: () -> Unit,
```
> يُعرّف معاملاً اسمه عند النقر الفردي (onSingleClick) من نوع دالة لا تأخذ وسائط وتُعيد لا شيء (Unit). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:11]

```
12:     onTripleClick: () -> Unit,
```
> يُعرّف معاملاً اسمه عند النقر الثلاثي (onTripleClick) من نوع دالة لا تأخذ وسائط وتُعيد لا شيء (Unit). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:12]

```
13:     clickTimeThreshold: Long = 300L
```
> يُعرّف معاملاً اسمه عتبة زمن النقر (clickTimeThreshold) من نوع عدد صحيح طويل (Long) بقيمة افتراضية حرفية تساوي `300L`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:13]

```
14: ): Modifier = composed {
```
> يُغلق قائمة المعاملات، ويحدّد أن نوع الإرجاع هو المُعدِّل (Modifier)، ويُسند جسم الدالة إلى استدعاء المُركَّب (composed) ويفتح كتلته. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:14]

```
15:     var tapCount by remember { mutableIntStateOf(0) }
```
> يُعرّف متغيّراً اسمه عدّاد النقرات (tapCount) مفوَّضاً بـ `remember` لحالة عدد صحيح قابلة للتغيّر (mutableIntStateOf) قيمتها الابتدائية الحرفية `0`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:15]

```
16:     var lastTapTime by remember { mutableLongStateOf(0L) }
```
> يُعرّف متغيّراً اسمه زمن آخر نقرة (lastTapTime) مفوَّضاً بـ `remember` لحالة عدد طويل قابلة للتغيّر (mutableLongStateOf) قيمتها الابتدائية الحرفية `0L`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:16]

```
17:     var singleClickJob by remember { mutableStateOf<kotlinx.coroutines.Job?>(null) }
```
> يُعرّف متغيّراً اسمه مهمّة النقر الفردي (singleClickJob) مفوَّضاً بـ `remember` لحالة قابلة للتغيّر (mutableStateOf) من نوع مهمّة كوروتين (Job) قابل لقيمة عدمية، قيمتها الابتدائية `null`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:17]

```
18:     val coroutineScope = rememberCoroutineScope()
```
> يُعرّف قيمة ثابتة اسمها نطاق الكوروتين (coroutineScope) بنتيجة استدعاء `rememberCoroutineScope`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:18]

```
19: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:19]

```
20:     this.clickable {
```
> يستدعي دالة القابلية للنقر (clickable) على المُعدِّل الحالي `this` ويفتح كتلة لمبدا معالِج النقر. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:20]

```
21:         val currentTime = System.currentTimeMillis()
```
> يُعرّف قيمة ثابتة اسمها الزمن الحالي (currentTime) بنتيجة استدعاء `System.currentTimeMillis()` الذي يُعيد الوقت بالملي ثانية. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:21]

```
22: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:22]

```
23:         if (currentTime - lastTapTime < clickTimeThreshold) {
```
> يفتح شرطاً يفحص ما إذا كان الفرق بين الزمن الحالي (currentTime) وزمن آخر نقرة (lastTapTime) أصغر من عتبة زمن النقر (clickTimeThreshold). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:23]

```
24:             tapCount++
```
> يزيد عدّاد النقرات (tapCount) بمقدار واحد. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:24]

```
25:         } else {
```
> يُغلق كتلة الشرط ويفتح كتلة البديل (else). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:25]

```
26:             tapCount = 1
```
> يُسند إلى عدّاد النقرات (tapCount) القيمة الحرفية `1`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:26]

```
27:         }
```
> إغلاق نطاق كتلة البديل (else). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:28]

```
29:         lastTapTime = currentTime
```
> يُسند إلى زمن آخر نقرة (lastTapTime) قيمة الزمن الحالي (currentTime). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:29]

```
30: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:30]

```
31:         // Cancel any pending single click action
```
> تعليق: «إلغاء أي إجراء نقر فردي معلّق». [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:31]

```
32:         singleClickJob?.cancel()
```
> يستدعي دالة الإلغاء `cancel()` على مهمّة النقر الفردي (singleClickJob) باستدعاء آمن من العدمية. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:32]

```
33:         singleClickJob = null
```
> يُسند إلى مهمّة النقر الفردي (singleClickJob) القيمة `null`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:33]

```
34: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:34]

```
35:         when (tapCount) {
```
> يفتح تعبير اختيار (when) يطابق على قيمة عدّاد النقرات (tapCount). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:35]

```
36:             1 -> {
```
> يحدّد فرع المطابقة للقيمة الحرفية `1` ويفتح كتلته. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:36]

```
37:                 // Wait to see if more taps come
```
> تعليق: «الانتظار لمعرفة ما إذا كانت ستأتي نقرات أخرى». [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:37]

```
38:                 singleClickJob = coroutineScope.launch {
```
> يُسند إلى مهمّة النقر الفردي (singleClickJob) نتيجة استدعاء `launch` على نطاق الكوروتين (coroutineScope) ويفتح كتلة الكوروتين. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:38]

```
39:                     delay(clickTimeThreshold)
```
> يستدعي دالة التأخير (delay) بمقدار عتبة زمن النقر (clickTimeThreshold). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:39]

```
40:                     if (tapCount == 1) {
```
> يفتح شرطاً يفحص ما إذا كان عدّاد النقرات (tapCount) يساوي القيمة الحرفية `1`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:40]

```
41:                         onSingleClick()
```
> يستدعي دالة عند النقر الفردي (onSingleClick). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:41]

```
42:                     }
```
> إغلاق نطاق كتلة الشرط الذي يفحص `tapCount == 1`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:42]

```
43:                 }
```
> إغلاق نطاق كتلة الكوروتين المُطلقة بـ `launch`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:43]

```
44:             }
```
> إغلاق نطاق فرع المطابقة للقيمة `1`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:44]

```
45:             3 -> {
```
> يحدّد فرع المطابقة للقيمة الحرفية `3` ويفتح كتلته. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:45]

```
46:                 // Triple click detected - execute immediately
```
> تعليق: «تم رصد نقر ثلاثي - نفّذ فوراً». [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:46]

```
47:                 onTripleClick()
```
> يستدعي دالة عند النقر الثلاثي (onTripleClick). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:47]

```
48:                 tapCount = 0
```
> يُسند إلى عدّاد النقرات (tapCount) القيمة الحرفية `0`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:48]

```
49:             }
```
> إغلاق نطاق فرع المطابقة للقيمة `3`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:49]

```
50:         }
```
> إغلاق نطاق تعبير الاختيار (when). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:50]

```
51: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:51]

```
52:         // Reset after threshold if no triple click
```
> تعليق: «إعادة التعيين بعد العتبة إذا لم يحدث نقر ثلاثي». [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:52]

```
53:         if (tapCount > 3) {
```
> يفتح شرطاً يفحص ما إذا كان عدّاد النقرات (tapCount) أكبر من القيمة الحرفية `3`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:53]

```
54:             tapCount = 0
```
> يُسند إلى عدّاد النقرات (tapCount) القيمة الحرفية `0`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:54]

```
55:         }
```
> إغلاق نطاق كتلة الشرط الذي يفحص `tapCount > 3`. [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:55]

```
56:     }
```
> إغلاق نطاق كتلة لمبدا القابلية للنقر (clickable). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:56]

```
57: }
```
> إغلاق نطاق دالة الامتداد النقر الفردي أو الثلاثي (singleOrTripleClickable) وكتلة المُركَّب (composed). [app/src/main/java/com/bitchat/android/core/ui/utils/ModifierExt.kt:57]
