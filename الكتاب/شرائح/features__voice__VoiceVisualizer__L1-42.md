# شريحة — app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt (الأسطر 1–42)

```
1: package com.bitchat.android.features.voice
```
> يُعرّف الحزمة (package) باسم `com.bitchat.android.features.voice`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:2]

```
3: import androidx.compose.animation.core.LinearEasing
```
> يستورد (import) المُيسِّر الخطّي `LinearEasing` من `androidx.compose.animation.core`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:3]

```
4: import androidx.compose.animation.core.animateFloatAsState
```
> يستورد الدالة `animateFloatAsState` (تحريك حالة عدد عشري) من `androidx.compose.animation.core`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:4]

```
5: import androidx.compose.animation.core.tween
```
> يستورد الدالة `tween` (مواصفة تحريك بيني) من `androidx.compose.animation.core`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:5]

```
6: import androidx.compose.foundation.Canvas
```
> يستورد العنصر `Canvas` (لوحة رسم) من `androidx.compose.foundation`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:6]

```
7: import androidx.compose.foundation.layout.fillMaxWidth
```
> يستورد المُعدِّل `fillMaxWidth` (ملء أقصى عرض) من `androidx.compose.foundation.layout`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:7]

```
8: import androidx.compose.foundation.layout.height
```
> يستورد المُعدِّل `height` (ارتفاع) من `androidx.compose.foundation.layout`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:8]

```
9: import androidx.compose.runtime.Composable
```
> يستورد التوسيمة `Composable` (قابل للتركيب) من `androidx.compose.runtime`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:9]

```
10: import androidx.compose.runtime.getValue
```
> يستورد الدالة `getValue` (جلب القيمة) من `androidx.compose.runtime`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:10]

```
11: import androidx.compose.ui.Modifier
```
> يستورد الصنف `Modifier` (المُعدِّل) من `androidx.compose.ui`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:11]

```
12: import androidx.compose.ui.graphics.Color
```
> يستورد الصنف `Color` (اللون) من `androidx.compose.ui.graphics`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:12]

```
13: import androidx.compose.ui.graphics.drawscope.drawIntoCanvas
```
> يستورد الدالة `drawIntoCanvas` (الرسم داخل اللوحة) من `androidx.compose.ui.graphics.drawscope`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:13]

```
14: import androidx.compose.ui.unit.dp
```
> يستورد الوحدة `dp` (بكسل مستقل عن الكثافة) من `androidx.compose.ui.unit`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:14]

```
15: import kotlin.math.min
```
> يستورد الدالة `min` (الأصغر) من `kotlin.math`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:16]

```
17: @Composable
```
> توسيمة `@Composable` تُعلِّم الدالة التالية بأنها قابلة للتركيب. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:17]

```
18: fun CyberpunkVisualizer(amplitude: Int, color: Color, modifier: Modifier = Modifier) {
```
> يُعرّف الدالة `CyberpunkVisualizer` (مُصوِّر السايبربانك) ذات الوسائط: `amplitude` (السَّعة) من نوع `Int`، و`color` من نوع `Color`، و`modifier` من نوع `Modifier` بقيمة افتراضية `Modifier`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:18]

```
19:     val norm = min(1f, amplitude / 20_000f)
```
> يُعرّف القيمة الثابتة `norm` (المُطبَّعة) وتساوي الأصغر بين `1f` وناتج قسمة `amplitude` على `20_000f`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:19]

```
20:     val heightFrac by animateFloatAsState(
```
> يُعرّف القيمة `heightFrac` (كسر الارتفاع) عبر مُفوِّض `by` من الدالة `animateFloatAsState` ويفتح وسائطها. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:20]

```
21:         targetValue = 0.1f + 0.9f * norm,
```
> يُضبَط الوسيط `targetValue` (القيمة الهدف) على `0.1f` زائد حاصل ضرب `0.9f` في `norm`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:21]

```
22:         animationSpec = tween(120, easing = LinearEasing), label = "amp"
```
> يُضبَط الوسيط `animationSpec` (مواصفة التحريك) على `tween` بمدة `120` ومُيسِّر `LinearEasing`، ويُضبَط الوسيط `label` (التسمية) على النص `"amp"`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:22]

```
23:     )
```
> إغلاق نطاق وسائط `animateFloatAsState`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:23]

```
24:     Canvas(
```
> يستدعي العنصر `Canvas` ويفتح وسائطه. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:24]

```
25:         modifier = modifier
```
> يُضبَط الوسيط `modifier` على المُعدِّل `modifier`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:25]

```
26:             .fillMaxWidth()
```
> يطبّق المُعدِّل `fillMaxWidth` (ملء أقصى عرض) على المُعدِّل. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:26]

```
27:             .height(48.dp)
```
> يطبّق المُعدِّل `height` (ارتفاع) بقيمة `48.dp`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:27]

```
28:     ) {
```
> إغلاق وسائط `Canvas` وفتح كتلة الرسم الخاصة بها. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:28]

```
29:         val w = size.width
```
> يُعرّف القيمة الثابتة `w` (العرض) وتساوي `size.width`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:29]

```
30:         val h = size.height
```
> يُعرّف القيمة الثابتة `h` (الارتفاع) وتساوي `size.height`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:30]

```
31:         val barCount = 24
```
> يُعرّف القيمة الثابتة `barCount` (عدد الأعمدة) وتساوي `24`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:31]

```
32:         val gap = 6f
```
> يُعرّف القيمة الثابتة `gap` (الفجوة) وتساوي `6f`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:32]

```
33:         val bw = (w - gap * (barCount - 1)) / barCount
```
> يُعرّف القيمة الثابتة `bw` (عرض العمود) وتساوي ناتج قسمة (`w` ناقص حاصل ضرب `gap` في (`barCount` ناقص `1`)) على `barCount`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:33]

```
34:         for (i in 0 until barCount) {
```
> يبدأ حلقة `for` بالمتغيّر `i` من `0` حتى `barCount` غير شامل، ويفتح جسمها. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:34]

```
35:             val phase = (i.toFloat() / barCount)
```
> يُعرّف القيمة الثابتة `phase` (الطور) وتساوي ناتج قسمة `i` المحوَّل إلى عدد عشري على `barCount`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:35]

```
36:             val barH = (0.2f + heightFrac * (0.8f * (0.5f + 0.5f * kotlin.math.sin(phase * Math.PI * 2).toFloat()))) * h
```
> يُعرّف القيمة الثابتة `barH` (ارتفاع العمود) وتساوي حاصل ضرب (`0.2f` زائد `heightFrac` مضروباً في (`0.8f` مضروباً في (`0.5f` زائد `0.5f` مضروباً في جيب (`kotlin.math.sin`) قيمة `phase * Math.PI * 2` المحوَّل إلى عدد عشري))) في `h`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:36]

```
37:             val x = i * (bw + gap)
```
> يُعرّف القيمة الثابتة `x` وتساوي حاصل ضرب `i` في (`bw` زائد `gap`). [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:37]

```
38:             val y = (h - barH) / 2f
```
> يُعرّف القيمة الثابتة `y` وتساوي ناتج قسمة (`h` ناقص `barH`) على `2f`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:38]

```
39:             drawRect(color.copy(alpha = 0.85f), topLeft = androidx.compose.ui.geometry.Offset(x, y), size = androidx.compose.ui.geometry.Size(bw, barH))
```
> يستدعي الدالة `drawRect` (رسم مستطيل) باللون `color.copy` بقيمة `alpha = 0.85f`، والوسيط `topLeft` (الزاوية العليا اليسرى) بإزاحة `Offset(x, y)`، والوسيط `size` (الحجم) بقيمة `Size(bw, barH)`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:39]

```
40:         }
```
> إغلاق نطاق حلقة `for`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:40]

```
41:     }
```
> إغلاق نطاق كتلة `Canvas`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:41]

```
42: }
```
> إغلاق نطاق الدالة `CyberpunkVisualizer`. [app/src/main/java/com/bitchat/android/features/voice/VoiceVisualizer.kt:42]
