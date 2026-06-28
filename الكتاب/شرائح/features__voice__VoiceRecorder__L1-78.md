# شريحة — app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt (الأسطر 1–78)

```
1: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:1]

```
2: package com.bitchat.android.features.voice
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) ‏com.bitchat.android.features.voice. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:2]

```
3: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:3]

```
4: import android.content.Context
```
> يستورد (import) الصنف Context من حزمة android.content. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:4]

```
5: import android.media.MediaRecorder
```
> يستورد الصنف المُسَجِّل الإعلامي (MediaRecorder) من حزمة android.media. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:5]

```
6: import android.util.Log
```
> يستورد الصنف Log من حزمة android.util. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:6]

```
7: import kotlinx.coroutines.Dispatchers
```
> يستورد الكائن Dispatchers من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:7]

```
8: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد الصنف تدفُّق الحالة القابل للتغيير (MutableStateFlow) من حزمة kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:8]

```
9: import kotlinx.coroutines.flow.StateFlow
```
> يستورد الصنف تدفُّق الحالة (StateFlow) من حزمة kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:9]

```
10: import kotlinx.coroutines.flow.asStateFlow
```
> يستورد الدالة asStateFlow من حزمة kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:10]

```
11: import kotlinx.coroutines.withContext
```
> يستورد الدالة withContext من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:11]

```
12: import java.io.File
```
> يستورد الصنف File من حزمة java.io. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:12]

```
13: import java.text.SimpleDateFormat
```
> يستورد الصنف SimpleDateFormat من حزمة java.text. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:13]

```
14: import java.util.Date
```
> يستورد الصنف Date من حزمة java.util. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:14]

```
15: import java.util.Locale
```
> يستورد الصنف Locale من حزمة java.util. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:16]

```
17: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:17]

```
18:  * Simple MediaRecorder wrapper that records to M4A (AAC) for wide compatibility.
```
> تعليق: غلاف بسيط حول المُسَجِّل الإعلامي يُسجِّل إلى صيغة M4A (AAC) من أجل توافق واسع. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:18]

```
19:  * The resulting file has MIME audio/mp4.
```
> تعليق: الملف الناتج نوع MIME الخاص به audio/mp4. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:19]

```
20:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:20]

```
21: class VoiceRecorder(private val context: Context) {
```
> يُعرِّف الصنف مُسَجِّل الصوت (VoiceRecorder) بمُنشئ يستقبل مُعامِلاً خاصاً ثابتاً اسمه context من النوع Context. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:21]

```
22:     companion object { private const val TAG = "VoiceRecorder" }
```
> يُعرِّف كائناً مرافقاً (companion object) يحتوي ثابتاً خاصاً اسمه TAG قيمته النصية "VoiceRecorder". [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:22]

```
23: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:23]

```
24:     private var recorder: MediaRecorder? = null
```
> يُعرِّف متغيّراً خاصاً قابلاً للتغيير اسمه recorder من النوع MediaRecorder القابل للقيمة الفارغة، ويُهيِّئه بقيمة null. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:24]

```
25:     private val _amplitude = MutableStateFlow(0)
```
> يُعرِّف ثابتاً خاصاً اسمه ‎_amplitude‎ ويُسنده إلى تدفُّق حالة قابل للتغيير قيمته الابتدائية 0. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:25]

```
26:     val amplitude: StateFlow<Int> = _amplitude.asStateFlow()
```
> يُعرِّف ثابتاً عاماً اسمه amplitude (السَّعة) من النوع StateFlow<Int> ويُسنده إلى ناتج استدعاء asStateFlow على ‎_amplitude‎. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:27]

```
28:     private var outFile: File? = null
```
> يُعرِّف متغيّراً خاصاً قابلاً للتغيير اسمه outFile (ملف الإخراج) من النوع File القابل للقيمة الفارغة، ويُهيِّئه بقيمة null. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:28]

```
29: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:29]

```
30:     fun start(): File? {
```
> يُعرِّف الدالة start (ابدأ) التي تُعيد قيمة من النوع File القابل للقيمة الفارغة. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:30]

```
31:         stop() // ensure previous session closed
```
> يستدعي الدالة stop. تعليق: ضمان إغلاق الجلسة السابقة. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:31]

```
32:         return try {
```
> يبدأ كتلة try ويُعيد قيمتها. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:32]

```
33:             val dir = File(context.filesDir, "voicenotes/outgoing").apply { mkdirs() }
```
> يُعرِّف ثابتاً اسمه dir بإنشاء File داخل context.filesDir بالمسار "voicenotes/outgoing"، ويستدعي عليه mkdirs داخل apply. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:33]

```
34:             val name = "voice_" + SimpleDateFormat("yyyyMMdd_HHmmss", Locale.US).format(Date()) + ".m4a"
```
> يُعرِّف ثابتاً اسمه name بضمّ النص "voice_" إلى ناتج تنسيق التاريخ الحالي بنمط "yyyyMMdd_HHmmss" بإقليم Locale.US ثم النص ".m4a". [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:34]

```
35:             val file = File(dir, name)
```
> يُعرِّف ثابتاً اسمه file بإنشاء File داخل المجلّد dir باسم name. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:35]

```
36:             val rec = MediaRecorder()
```
> يُعرِّف ثابتاً اسمه rec بإنشاء كائن MediaRecorder جديد. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:36]

```
37:             rec.setAudioSource(MediaRecorder.AudioSource.MIC)
```
> يستدعي setAudioSource على rec بقيمة MediaRecorder.AudioSource.MIC (الميكروفون). [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:37]

```
38:             rec.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
```
> يستدعي setOutputFormat على rec بقيمة MediaRecorder.OutputFormat.MPEG_4. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:38]

```
39:             rec.setAudioEncoder(MediaRecorder.AudioEncoder.AAC)
```
> يستدعي setAudioEncoder على rec بقيمة MediaRecorder.AudioEncoder.AAC. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:39]

```
40:             rec.setAudioChannels(1)
```
> يستدعي setAudioChannels على rec بقيمة 1. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:40]

```
41:             // Target: 16 kHz AAC @ 20 kbps ≈ 2.5 KB/sec
```
> تعليق: الهدف 16 كيلوهرتز AAC عند 20 كيلوبت/ثانية ≈ 2.5 كيلوبايت/ثانية. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:41]

```
42:             // Lower sample rate and bitrate for compact, speech-optimized recordings
```
> تعليق: معدّل عيّنات ومعدّل بِت أقل من أجل تسجيلات مُدمجة مُحسَّنة للكلام. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:42]

```
43:             rec.setAudioSamplingRate(16000)
```
> يستدعي setAudioSamplingRate على rec بقيمة 16000. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:43]

```
44:             rec.setAudioEncodingBitRate(20_000)
```
> يستدعي setAudioEncodingBitRate على rec بقيمة 20000. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:44]

```
45:             rec.setOutputFile(file.absolutePath)
```
> يستدعي setOutputFile على rec بقيمة المسار المطلق للملف file.absolutePath. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:45]

```
46:             rec.prepare()
```
> يستدعي prepare على rec. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:46]

```
47:             rec.start() 
```
> يستدعي start على rec. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:47]

```
48:             recorder = rec
```
> يُسند المتغيّر recorder إلى الكائن rec. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:48]

```
49:             outFile = file
```
> يُسند المتغيّر outFile إلى file. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:49]

```
50:             file
```
> يُقيّم بقيمة file كقيمة ناتجة عن كتلة try. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:50]

```
51:         } catch (e: Exception) {
```
> يبدأ كتلة catch تلتقط اعتراضاً اسمه e من النوع Exception. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:51]

```
52:             Log.e(TAG, "Failed to start recording: ${e.message}")
```
> يستدعي Log.e بالوسم TAG والرسالة "Failed to start recording: " متبوعة برسالة الاعتراض e.message. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:52]

```
53:             null
```
> يُقيّم بقيمة null كقيمة ناتجة عن كتلة catch. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:53]

```
54:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:54]

```
55:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:55]

```
56: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:56]

```
57:     fun pollAmplitude(): Int {
```
> يُعرِّف الدالة pollAmplitude (استطلاع السَّعة) التي تُعيد قيمة من النوع Int. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:57]

```
58:         return try {
```
> يبدأ كتلة try ويُعيد قيمتها. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:58]

```
59:             val amp = recorder?.maxAmplitude ?: 0
```
> يُعرِّف ثابتاً اسمه amp بقيمة recorder?.maxAmplitude، فإن كانت null فالقيمة 0. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:59]

```
60:             _amplitude.value = amp
```
> يُسند قيمة ‎_amplitude.value‎ إلى amp. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:60]

```
61:             amp
```
> يُقيّم بقيمة amp كقيمة ناتجة عن كتلة try. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:61]

```
62:         } catch (_: Exception) { 0 }
```
> يبدأ كتلة catch تلتقط اعتراضاً من النوع Exception دون تسميته وتُقيّم بقيمة 0. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:62]

```
63:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:63]

```
64: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:64]

```
65:     fun stop(): File? {
```
> يُعرِّف الدالة stop (أوقِف) التي تُعيد قيمة من النوع File القابل للقيمة الفارغة. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:65]

```
66:         try {
```
> يبدأ كتلة try. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:66]

```
67:             recorder?.apply {
```
> يستدعي apply على recorder إن لم يكن null. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:67]

```
68:                 try { stop() } catch (_: Exception) {}
```
> يبدأ كتلة try تستدعي stop، وكتلة catch تلتقط Exception دون تسميته بجسم فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:68]

```
69:                 try { reset() } catch (_: Exception) {}
```
> يبدأ كتلة try تستدعي reset، وكتلة catch تلتقط Exception دون تسميته بجسم فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:69]

```
70:                 try { release() } catch (_: Exception) {}
```
> يبدأ كتلة try تستدعي release، وكتلة catch تلتقط Exception دون تسميته بجسم فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:70]

```
71:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:71]

```
72:         } catch (_: Exception) {}
```
> يبدأ كتلة catch تلتقط Exception دون تسميته بجسم فارغ. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:72]

```
73:         val f = outFile
```
> يُعرِّف ثابتاً اسمه f ويُسنده إلى قيمة outFile. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:73]

```
74:         recorder = null
```
> يُسند المتغيّر recorder إلى null. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:74]

```
75:         outFile = null
```
> يُسند المتغيّر outFile إلى null. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:75]

```
76:         return f
```
> يُعيد قيمة f. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:76]

```
77:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:77]

```
78: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/features/voice/VoiceRecorder.kt:78]
