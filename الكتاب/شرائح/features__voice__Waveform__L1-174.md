# شريحة — app/src/main/java/com/bitchat/android/features/voice/Waveform.kt (الأسطر 1–174)

```
1: package com.bitchat.android.features.voice
```
> يعلن انتماء الملف إلى الحزمة (package) ‏`com.bitchat.android.features.voice`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:2]

```
3: import android.media.MediaCodec
```
> يستورد الصنف `MediaCodec` من `android.media`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:3]

```
4: import android.media.MediaExtractor
```
> يستورد الصنف `MediaExtractor` من `android.media`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:4]

```
5: import android.media.MediaFormat
```
> يستورد الصنف `MediaFormat` من `android.media`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:5]

```
6: import android.util.Log
```
> يستورد الصنف `Log` من `android.util`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:6]

```
7: import kotlinx.coroutines.CoroutineScope
```
> يستورد `CoroutineScope` (نطاق المهام المتزامنة) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:7]

```
8: import kotlinx.coroutines.Dispatchers
```
> يستورد `Dispatchers` (الموزِّعات) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:8]

```
9: import kotlinx.coroutines.SupervisorJob
```
> يستورد `SupervisorJob` (المهمة المُشرِفة) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:9]

```
10: import kotlinx.coroutines.launch
```
> يستورد الدالة `launch` (إطلاق المهمة) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:10]

```
11: import java.nio.ByteBuffer
```
> يستورد الصنف `ByteBuffer` (مخزن البايتات) من `java.nio`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:11]

```
12: import java.nio.ByteOrder
```
> يستورد الصنف `ByteOrder` (ترتيب البايتات) من `java.nio`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:12]

```
13: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف `ConcurrentHashMap` (خريطة تجزئة متزامنة) من `java.util.concurrent`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:13]

```
14: import kotlin.math.abs
```
> يستورد الدالة `abs` (القيمة المطلقة) من `kotlin.math`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:14]

```
15: import kotlin.math.ln
```
> يستورد الدالة `ln` (اللوغاريتم الطبيعي) من `kotlin.math`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:15]

```
16: import kotlin.math.max
```
> يستورد الدالة `max` (الأكبر) من `kotlin.math`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:16]

```
17: import kotlin.math.min
```
> يستورد الدالة `min` (الأصغر) من `kotlin.math`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:17]

```
18: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:18]

```
19: object VoiceWaveformCache {
```
> يعرّف كائناً مفرداً (object) باسم `VoiceWaveformCache` (مخزن مؤقت لموجات الصوت) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:19]

```
20:     private val map = ConcurrentHashMap<String, FloatArray>()
```
> يعرّف خاصية خاصة ثابتة `map` ويهيئها بنسخة جديدة من `ConcurrentHashMap` مفتاحها `String` وقيمتها `FloatArray` (مصفوفة أعداد عشرية). [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:20]

```
21:     fun put(path: String, samples: FloatArray) { map[path] = samples }
```
> يعرّف الدالة `put` بمعاملين `path` من نوع `String` و`samples` من نوع `FloatArray`، وجسمها يسند `samples` إلى `map` عند المفتاح `path`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:21]

```
22:     fun get(path: String): FloatArray? = map[path]
```
> يعرّف الدالة `get` بمعامل `path` من نوع `String`، وتُعيد `FloatArray?` (قد تكون فارغة) بقيمة `map[path]`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:22]

```
23: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:24]

```
25: fun normalizeAmplitudeSample(amp: Int): Float {
```
> يعرّف دالة `normalizeAmplitudeSample` (تطبيع عيّنة السعة) بمعامل `amp` من نوع `Int` وتُعيد `Float`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:25]

```
26:     val a = max(0, amp)
```
> يعرّف الثابت `a` ويهيئه بقيمة `max(0, amp)` أي الأكبر بين الصفر و`amp`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:26]

```
27:     val norm = ln(1.0 + a.toDouble()) / ln(1.0 + 32768.0)
```
> يعرّف الثابت `norm` ويهيئه بناتج قسمة `ln(1.0 + a.toDouble())` على `ln(1.0 + 32768.0)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:27]

```
28:     return norm.toFloat().coerceIn(0f, 1f)
```
> يُعيد قيمة `norm` محوّلة إلى `Float` ومحصورة بين `0f` و`1f` بدالة `coerceIn`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:28]

```
29: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:29]

```
30: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:30]

```
31: fun resampleWave(values: FloatArray, target: Int): FloatArray {
```
> يعرّف دالة `resampleWave` (إعادة أخذ عيّنات الموجة) بمعاملين `values` من نوع `FloatArray` و`target` من نوع `Int`، وتُعيد `FloatArray`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:31]

```
32:     if (values.isEmpty() || target <= 0) return FloatArray(target) { 0f }
```
> إذا كانت `values` فارغة أو `target` أصغر من أو يساوي الصفر، يُعيد مصفوفة `FloatArray` بطول `target` كل عناصرها `0f`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:32]

```
33:     if (values.size == target) return values
```
> إذا كان حجم `values` يساوي `target`، يُعيد `values` كما هي. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:33]

```
34:     val out = FloatArray(target)
```
> يعرّف الثابت `out` ويهيئه بمصفوفة `FloatArray` بطول `target`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:34]

```
35:     val step = (values.size - 1).toFloat() / (target - 1).toFloat()
```
> يعرّف الثابت `step` (الخطوة) ويهيئه بناتج قسمة `(values.size - 1)` المحوّلة إلى `Float` على `(target - 1)` المحوّلة إلى `Float`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:35]

```
36:     var x = 0f
```
> يعرّف المتغير `x` ويهيئه بالقيمة `0f`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:36]

```
37:     for (i in 0 until target) {
```
> يبدأ حلقة `for` يأخذ فيها `i` القيم من `0` حتى ما قبل `target`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:37]

```
38:         val idx = x.toInt()
```
> يعرّف الثابت `idx` ويهيئه بقيمة `x` محوّلة إلى `Int`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:38]

```
39:         val frac = x - idx
```
> يعرّف الثابت `frac` (الكسر) ويهيئه بناتج طرح `idx` من `x`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:39]

```
40:         val a = values[idx]
```
> يعرّف الثابت `a` ويهيئه بالعنصر `values[idx]`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:40]

```
41:         val b = values[min(values.size - 1, idx + 1)]
```
> يعرّف الثابت `b` ويهيئه بالعنصر `values` عند الفهرس `min(values.size - 1, idx + 1)` أي الأصغر بين آخر فهرس و`idx + 1`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:41]

```
42:         out[i] = (a + (b - a) * frac).coerceIn(0f, 1f)
```
> يسند إلى `out[i]` قيمة `(a + (b - a) * frac)` (استيفاء خطي) محصورة بين `0f` و`1f`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:42]

```
43:         x += step
```
> يزيد `x` بمقدار `step`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:43]

```
44:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:44]

```
45:     return out
```
> يُعيد المصفوفة `out`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:45]

```
46: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:46]

```
47: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:47]

```
48: object AudioWaveformExtractor {
```
> يعرّف كائناً مفرداً (object) باسم `AudioWaveformExtractor` (مستخرِج موجة الصوت) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:48]

```
49:     private val scope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يعرّف خاصية خاصة ثابتة `scope` ويهيئها بنسخة `CoroutineScope` مبنية على `Dispatchers.IO` مجموعاً مع `SupervisorJob()`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:49]

```
50: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:50]

```
51:     fun extractAsync(path: String, sampleCount: Int = 120, onComplete: (FloatArray?) -> Unit) {
```
> يعرّف الدالة `extractAsync` (الاستخراج غير المتزامن) بمعاملات `path` من نوع `String`، و`sampleCount` من نوع `Int` بقيمة افتراضية `120`، و`onComplete` دالة تأخذ `FloatArray?` وتُعيد `Unit`؛ ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:51]

```
52:         scope.launch {
```
> يستدعي `launch` على `scope` لإطلاق مهمة متزامنة، ويفتح نطاق كتلتها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:52]

```
53:             onComplete(runCatching { extract(path, sampleCount) }.getOrNull())
```
> يستدعي `onComplete` ممرراً نتيجة `runCatching { extract(path, sampleCount) }.getOrNull()` أي ناتج `extract` أو `null` عند حدوث استثناء. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:53]

```
54:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:54]

```
55:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:55]

```
56: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:56]

```
57:     private fun extract(path: String, sampleCount: Int): FloatArray? {
```
> يعرّف دالة خاصة `extract` (الاستخراج) بمعاملين `path` من نوع `String` و`sampleCount` من نوع `Int`، وتُعيد `FloatArray?`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:57]

```
58:         val extractor = MediaExtractor()
```
> يعرّف الثابت `extractor` ويهيئه بنسخة جديدة من `MediaExtractor`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:58]

```
59:         extractor.setDataSource(path)
```
> يستدعي `setDataSource` على `extractor` ممرراً `path`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:59]

```
60:         val trackIndex = (0 until extractor.trackCount).firstOrNull { idx ->
```
> يعرّف الثابت `trackIndex` (فهرس المسار) ويهيئه بأول قيمة `idx` في المدى `0 until extractor.trackCount` تحقق الشرط في الكتلة، ويفتح نطاق اللامدا. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:60]

```
61:             val fmt = extractor.getTrackFormat(idx)
```
> يعرّف الثابت `fmt` ويهيئه بناتج `extractor.getTrackFormat(idx)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:61]

```
62:             val mime = fmt.getString(MediaFormat.KEY_MIME) ?: ""
```
> يعرّف الثابت `mime` ويهيئه بناتج `fmt.getString(MediaFormat.KEY_MIME)` أو السلسلة الفارغة عند كونه `null`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:62]

```
63:             mime.startsWith("audio/")
```
> يُقيّم التعبير `mime.startsWith("audio/")` كقيمة إرجاع اللامدا أي هل يبدأ `mime` بالنص `"audio/"`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:63]

```
64:         } ?: return null
```
> يُغلق نطاق اللامدا، وإذا كانت نتيجة `firstOrNull` تساوي `null` فإنه يُعيد `null`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:64]

```
65:         extractor.selectTrack(trackIndex)
```
> يستدعي `selectTrack` على `extractor` ممرراً `trackIndex`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:65]

```
66:         val format = extractor.getTrackFormat(trackIndex)
```
> يعرّف الثابت `format` ويهيئه بناتج `extractor.getTrackFormat(trackIndex)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:66]

```
67:         val mime = format.getString(MediaFormat.KEY_MIME) ?: return null
```
> يعرّف الثابت `mime` ويهيئه بناتج `format.getString(MediaFormat.KEY_MIME)`، وإذا كان `null` يُعيد `null`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:67]

```
68:         val codec = MediaCodec.createDecoderByType(mime)
```
> يعرّف الثابت `codec` ويهيئه بناتج `MediaCodec.createDecoderByType(mime)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:68]

```
69:         codec.configure(format, null, null, 0)
```
> يستدعي `configure` على `codec` ممرراً `format` و`null` و`null` و`0`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:69]

```
70:         codec.start()
```
> يستدعي `start` على `codec`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:70]

```
71: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:71]

```
72:         val durationUs = if (format.containsKey(MediaFormat.KEY_DURATION)) format.getLong(MediaFormat.KEY_DURATION) else 0L
```
> يعرّف الثابت `durationUs` (المدة بالميكروثانية) ويهيئه بـ`format.getLong(MediaFormat.KEY_DURATION)` إذا احتوى `format` المفتاح، وإلا بـ`0L`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:72]

```
73:         val desiredBins = sampleCount.coerceAtLeast(32)
```
> يعرّف الثابت `desiredBins` (عدد الصناديق المطلوب) ويهيئه بقيمة `sampleCount` مرفوعة إلى ما لا يقل عن `32` بدالة `coerceAtLeast`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:73]

```
74:         val bins = FloatArray(desiredBins) { 0f }
```
> يعرّف الثابت `bins` (الصناديق) ويهيئه بمصفوفة `FloatArray` بطول `desiredBins` كل عناصرها `0f`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:74]

```
75:         val counts = IntArray(desiredBins) { 0 }
```
> يعرّف الثابت `counts` (العدّادات) ويهيئه بمصفوفة `IntArray` بطول `desiredBins` كل عناصرها `0`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:75]

```
76: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:76]

```
77:         val inBuffers = codec.inputBuffers
```
> يعرّف الثابت `inBuffers` (مخازن الدخل) ويهيئه بقيمة `codec.inputBuffers`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:77]

```
78:         val outInfo = MediaCodec.BufferInfo()
```
> يعرّف الثابت `outInfo` (معلومات مخزن الخرج) ويهيئه بنسخة جديدة من `MediaCodec.BufferInfo`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:78]

```
79: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:79]

```
80:         var sawEOS = false
```
> يعرّف المتغير `sawEOS` (شوهدت نهاية الدفق) ويهيئه بالقيمة `false`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:80]

```
81:         while (!sawEOS) {
```
> يبدأ حلقة `while` تستمر ما دام `sawEOS` غير صحيح، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:81]

```
82:             // Queue input
```
> تعليق: صفّ الدخل. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:82]

```
83:             val inIndex = codec.dequeueInputBuffer(10_000)
```
> يعرّف الثابت `inIndex` (فهرس الدخل) ويهيئه بناتج `codec.dequeueInputBuffer(10_000)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:83]

```
84:             if (inIndex >= 0) {
```
> يبدأ شرط `if` يتحقق إذا كان `inIndex` أكبر من أو يساوي الصفر، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:84]

```
85:                 val buffer = codec.getInputBuffer(inIndex) ?: inBuffers[inIndex]
```
> يعرّف الثابت `buffer` ويهيئه بناتج `codec.getInputBuffer(inIndex)` أو بـ`inBuffers[inIndex]` عند كونه `null`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:85]

```
86:                 val sampleSize = extractor.readSampleData(buffer, 0)
```
> يعرّف الثابت `sampleSize` (حجم العيّنة) ويهيئه بناتج `extractor.readSampleData(buffer, 0)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:86]

```
87:                 if (sampleSize < 0) {
```
> يبدأ شرط `if` يتحقق إذا كان `sampleSize` أصغر من الصفر، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:87]

```
88:                     codec.queueInputBuffer(inIndex, 0, 0, 0L, MediaCodec.BUFFER_FLAG_END_OF_STREAM)
```
> يستدعي `queueInputBuffer` على `codec` ممرراً `inIndex` و`0` و`0` و`0L` والعَلَم `MediaCodec.BUFFER_FLAG_END_OF_STREAM`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:88]

```
89:                 } else {
```
> يُغلق نطاق `if` ويبدأ فرع `else` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:89]

```
90:                     val presentationTimeUs = extractor.sampleTime
```
> يعرّف الثابت `presentationTimeUs` (زمن العرض بالميكروثانية) ويهيئه بقيمة `extractor.sampleTime`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:90]

```
91:                     codec.queueInputBuffer(inIndex, 0, sampleSize, presentationTimeUs, 0)
```
> يستدعي `queueInputBuffer` على `codec` ممرراً `inIndex` و`0` و`sampleSize` و`presentationTimeUs` و`0`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:91]

```
92:                     extractor.advance()
```
> يستدعي `advance` على `extractor`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:92]

```
93:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:93]

```
94:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:94]

```
95: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:95]

```
96:             // Dequeue output
```
> تعليق: سحب الخرج من الصفّ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:96]

```
97:             var outIndex = codec.dequeueOutputBuffer(outInfo, 10_000)
```
> يعرّف المتغير `outIndex` (فهرس الخرج) ويهيئه بناتج `codec.dequeueOutputBuffer(outInfo, 10_000)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:97]

```
98:             while (outIndex >= 0) {
```
> يبدأ حلقة `while` تستمر ما دام `outIndex` أكبر من أو يساوي الصفر، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:98]

```
99:                 val outBuf = codec.getOutputBuffer(outIndex)
```
> يعرّف الثابت `outBuf` (مخزن الخرج) ويهيئه بناتج `codec.getOutputBuffer(outIndex)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:99]

```
100:                 if (outBuf != null && outInfo.size > 0) {
```
> يبدأ شرط `if` يتحقق إذا كان `outBuf` غير `null` و`outInfo.size` أكبر من الصفر، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:100]

```
101:                     outBuf.order(ByteOrder.LITTLE_ENDIAN)
```
> يستدعي `order` على `outBuf` ممرراً `ByteOrder.LITTLE_ENDIAN` (الترتيب صغير النهاية). [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:101]

```
102:                     val shortCount = outInfo.size / 2
```
> يعرّف الثابت `shortCount` (عدد القيم القصيرة) ويهيئه بناتج قسمة `outInfo.size` على `2`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:102]

```
103:                     val shorts = ShortArray(shortCount)
```
> يعرّف الثابت `shorts` ويهيئه بمصفوفة `ShortArray` بطول `shortCount`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:103]

```
104:                     outBuf.asShortBuffer().get(shorts)
```
> يستدعي `asShortBuffer()` على `outBuf` ثم `get(shorts)` لنسخ المحتوى إلى `shorts`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:104]

```
105: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:105]

```
106:                     // Map this buffer to bins using timestamp range
```
> تعليق: ربط هذا المخزن بالصناديق باستخدام مدى الطابع الزمني. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:106]

```
107:                     val startUs = outInfo.presentationTimeUs
```
> يعرّف الثابت `startUs` (بداية بالميكروثانية) ويهيئه بقيمة `outInfo.presentationTimeUs`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:107]

```
108:                     val endUs = startUs + bufferDurationUs(format, outInfo.size)
```
> يعرّف الثابت `endUs` (نهاية بالميكروثانية) ويهيئه بمجموع `startUs` و`bufferDurationUs(format, outInfo.size)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:108]

```
109:                     val startBin = binForTime(startUs, durationUs, desiredBins)
```
> يعرّف الثابت `startBin` (صندوق البداية) ويهيئه بناتج `binForTime(startUs, durationUs, desiredBins)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:109]

```
110:                     val endBin = binForTime(endUs, durationUs, desiredBins).coerceAtMost(desiredBins - 1)
```
> يعرّف الثابت `endBin` (صندوق النهاية) ويهيئه بناتج `binForTime(endUs, durationUs, desiredBins)` محصوراً بحد أقصى `desiredBins - 1` بدالة `coerceAtMost`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:110]

```
111: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:111]

```
112:                     var idx = 0
```
> يعرّف المتغير `idx` ويهيئه بالقيمة `0`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:112]

```
113:                     for (bin in startBin..endBin) {
```
> يبدأ حلقة `for` يأخذ فيها `bin` القيم من `startBin` حتى `endBin` شاملاً، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:113]

```
114:                         // aggregate portion of buffer to this bin
```
> تعليق: تجميع جزء من المخزن إلى هذا الصندوق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:114]

```
115:                         val window = shorts.size / max(1, (endBin - startBin + 1))
```
> يعرّف الثابت `window` (النافذة) ويهيئه بناتج قسمة `shorts.size` على `max(1, (endBin - startBin + 1))`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:115]

```
116:                         val begin = idx
```
> يعرّف الثابت `begin` (البداية) ويهيئه بقيمة `idx`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:116]

```
117:                         val finish = min(shorts.size, idx + window)
```
> يعرّف الثابت `finish` (النهاية) ويهيئه بناتج `min(shorts.size, idx + window)` أي الأصغر بين حجم `shorts` و`idx + window`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:117]

```
118:                         var acc = 0.0
```
> يعرّف المتغير `acc` (المُراكِم) ويهيئه بالقيمة `0.0`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:118]

```
119:                         var cnt = 0
```
> يعرّف المتغير `cnt` (العدّاد) ويهيئه بالقيمة `0`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:119]

```
120:                         for (i in begin until finish) {
```
> يبدأ حلقة `for` يأخذ فيها `i` القيم من `begin` حتى ما قبل `finish`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:120]

```
121:                             acc += abs(shorts[i].toInt())
```
> يزيد `acc` بقيمة `abs(shorts[i].toInt())` أي القيمة المطلقة للعنصر `shorts[i]` محوّلاً إلى `Int`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:121]

```
122:                             cnt += 1
```
> يزيد `cnt` بمقدار `1`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:122]

```
123:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:123]

```
124:                         val avg = if (cnt > 0) (acc / cnt) else 0.0
```
> يعرّف الثابت `avg` (المتوسط) ويهيئه بناتج `acc / cnt` إذا كان `cnt` أكبر من الصفر، وإلا بـ`0.0`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:124]

```
125:                         val norm = (avg / 32768.0).coerceIn(0.0, 1.0).toFloat()
```
> يعرّف الثابت `norm` ويهيئه بناتج قسمة `avg` على `32768.0` محصوراً بين `0.0` و`1.0` ثم محوّلاً إلى `Float`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:125]

```
126:                         bins[bin] = max(bins[bin], norm)
```
> يسند إلى `bins[bin]` الأكبر بين قيمته الحالية `bins[bin]` و`norm`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:126]

```
127:                         counts[bin] += 1
```
> يزيد `counts[bin]` بمقدار `1`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:127]

```
128:                         idx += window
```
> يزيد `idx` بمقدار `window`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:128]

```
129:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:129]

```
130:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:130]

```
131:                 codec.releaseOutputBuffer(outIndex, false)
```
> يستدعي `releaseOutputBuffer` على `codec` ممرراً `outIndex` و`false`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:131]

```
132:                 outIndex = codec.dequeueOutputBuffer(outInfo, 0)
```
> يسند إلى `outIndex` ناتج `codec.dequeueOutputBuffer(outInfo, 0)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:132]

```
133:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:133]

```
134: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:134]

```
135:             if (outInfo.flags and MediaCodec.BUFFER_FLAG_END_OF_STREAM != 0) {
```
> يبدأ شرط `if` يتحقق إذا كان ناتج `outInfo.flags and MediaCodec.BUFFER_FLAG_END_OF_STREAM` لا يساوي الصفر، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:135]

```
136:                 sawEOS = true
```
> يسند إلى `sawEOS` القيمة `true`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:136]

```
137:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:137]

```
138:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:138]

```
139: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:139]

```
140:         codec.stop()
```
> يستدعي `stop` على `codec`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:140]

```
141:         codec.release()
```
> يستدعي `release` على `codec`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:141]

```
142:         extractor.release()
```
> يستدعي `release` على `extractor`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:142]

```
143: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:143]

```
144:         // Smooth + normalize
```
> تعليق: تنعيم + تطبيع. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:144]

```
145:         var maxVal = 0f
```
> يعرّف المتغير `maxVal` (القيمة العظمى) ويهيئه بالقيمة `0f`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:145]

```
146:         for (i in bins.indices) {
```
> يبدأ حلقة `for` يأخذ فيها `i` فهارس `bins`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:146]

```
147:             if (counts[i] == 0) continue
```
> إذا كان `counts[i]` يساوي الصفر، ينفّذ `continue` لتخطّي بقية التكرار. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:147]

```
148:             maxVal = max(maxVal, bins[i])
```
> يسند إلى `maxVal` الأكبر بين `maxVal` و`bins[i]`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:148]

```
149:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:149]

```
150:         if (maxVal <= 0f) maxVal = 1f
```
> إذا كان `maxVal` أصغر من أو يساوي `0f`، يسند إليه القيمة `1f`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:150]

```
151:         for (i in bins.indices) {
```
> يبدأ حلقة `for` يأخذ فيها `i` فهارس `bins`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:151]

```
152:             bins[i] = (bins[i] / maxVal).coerceIn(0f, 1f)
```
> يسند إلى `bins[i]` ناتج قسمة `bins[i]` على `maxVal` محصوراً بين `0f` و`1f`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:152]

```
153:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:153]

```
154: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:154]

```
155:         return bins
```
> يُعيد المصفوفة `bins`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:155]

```
156:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:156]

```
157: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:157]

```
158:     private fun bufferDurationUs(format: MediaFormat, bytes: Int): Long {
```
> يعرّف دالة خاصة `bufferDurationUs` (مدة المخزن بالميكروثانية) بمعاملين `format` من نوع `MediaFormat` و`bytes` من نوع `Int`، وتُعيد `Long`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:158]

```
159:         return try {
```
> يبدأ تعبير `return try` لإرجاع ناتج كتلة `try`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:159]

```
160:             val sampleRate = format.getInteger(MediaFormat.KEY_SAMPLE_RATE)
```
> يعرّف الثابت `sampleRate` (معدّل العيّنات) ويهيئه بناتج `format.getInteger(MediaFormat.KEY_SAMPLE_RATE)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:160]

```
161:             val channels = format.getInteger(MediaFormat.KEY_CHANNEL_COUNT)
```
> يعرّف الثابت `channels` (عدد القنوات) ويهيئه بناتج `format.getInteger(MediaFormat.KEY_CHANNEL_COUNT)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:161]

```
162:             val samples = bytes / 2 / max(1, channels)
```
> يعرّف الثابت `samples` (العيّنات) ويهيئه بناتج قسمة `bytes` على `2` ثم على `max(1, channels)`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:162]

```
163:             (samples * 1_000_000L) / max(1, sampleRate)
```
> يُقيّم التعبير `(samples * 1_000_000L) / max(1, sampleRate)` كقيمة إرجاع كتلة `try`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:163]

```
164:         } catch (e: Exception) {
```
> يُغلق نطاق `try` ويبدأ كتلة `catch` تلتقط `e` من نوع `Exception`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:164]

```
165:             0L
```
> يُقيّم القيمة `0L` كقيمة إرجاع كتلة `catch`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:165]

```
166:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:166]

```
167:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:167]

```
168: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:168]

```
169:     private fun binForTime(presentationUs: Long, durationUs: Long, bins: Int): Int {
```
> يعرّف دالة خاصة `binForTime` (صندوق لزمن معيّن) بمعاملات `presentationUs` و`durationUs` من نوع `Long` و`bins` من نوع `Int`، وتُعيد `Int`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:169]

```
170:         if (durationUs <= 0L) return 0
```
> إذا كان `durationUs` أصغر من أو يساوي `0L`، يُعيد `0`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:170]

```
171:         val frac = presentationUs.toDouble() / durationUs.toDouble()
```
> يعرّف الثابت `frac` (الكسر) ويهيئه بناتج قسمة `presentationUs` المحوّل إلى `Double` على `durationUs` المحوّل إلى `Double`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:171]

```
172:         return (frac * bins).toInt().coerceIn(0, bins - 1)
```
> يُعيد ناتج `(frac * bins)` محوّلاً إلى `Int` ومحصوراً بين `0` و`bins - 1`. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:172]

```
173:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:173]

```
174: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/Waveform.kt:174]
