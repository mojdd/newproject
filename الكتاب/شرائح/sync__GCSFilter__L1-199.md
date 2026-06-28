# شريحة — app/src/main/java/com/bitchat/android/sync/GCSFilter.kt (الأسطر 1–199)

```
1: package com.bitchat.android.sync
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) المسماة com.bitchat.android.sync. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:2]

```
3: import java.security.MessageDigest
```
> يستورد (import) الصنف MessageDigest من حزمة java.security. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:3]

```
4: import kotlin.math.ceil
```
> يستورد الدالة ceil (التقريب لأعلى) من حزمة kotlin.math. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:4]

```
5: import kotlin.math.ln
```
> يستورد الدالة ln (اللوغاريتم الطبيعي) من حزمة kotlin.math. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:6]

```
7: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:7]

```
8:  * Golomb-Coded Set (GCS) filter implementation for sync.
```
> تعليق: تنفيذ مرشّح المجموعة المرمّزة بغولومب (Golomb-Coded Set) من أجل المزامنة. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:8]

```
9:  *
```
> تعليق: سطر فاصل في كتلة التوثيق. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:9]

```
10:  * Hashing:
```
> تعليق: التجزئة (Hashing). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:10]

```
11:  * - h64(id) = first 8 bytes of SHA-256 over the 16-byte PacketId (big-endian unsigned)
```
> تعليق: h64(id) هي أول 8 بايتات من SHA-256 على معرّف الرزمة (PacketId) ذي الـ16 بايتاً (تمثيل كبير النهاية غير مُوقَّع). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:11]

```
12:  * - Map to range [0, M) via (h64 % M)
```
> تعليق: التحويل إلى المدى [0, M) عبر (h64 % M). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:12]

```
13:  *
```
> تعليق: سطر فاصل في كتلة التوثيق. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:13]

```
14:  * Encoding (v1):
```
> تعليق: الترميز (Encoding) النسخة الأولى. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:14]

```
15:  * - Sort mapped values ascending; encode deltas (first is v0, then vi - v{i-1}) as positive integers
```
> تعليق: رتّب القيم المُحوَّلة تصاعدياً؛ رمّز الفروق (delta) (الأول هو v0 ثم vi - v{i-1}) كأعداد صحيحة موجبة. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:15]

```
16:  * - For each delta x >= 1, write Golomb-Rice code with parameter P:
```
> تعليق: لكل فرق x أكبر من أو يساوي 1، اكتب رمز غولومب-رايس (Golomb-Rice) بالمَعلَمة P. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:16]

```
17:  *   q = (x - 1) >> P (unary q ones followed by a zero), then P low bits r = (x - 1) & ((1<<P)-1)
```
> تعليق: q = (x - 1) >> P (q من الآحاد بالترميز الأحادي يتبعها صفر)، ثم P من البتات الدنيا r = (x - 1) & ((1<<P)-1). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:17]

```
18:  * - Bitstream is packed MSB-first in each byte.
```
> تعليق: تيار البتات (bitstream) مُعبّأ بدءاً من البت الأعلى أهمية (MSB-first) في كل بايت. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:18]

```
19:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:19]

```
20: object GCSFilter {
```
> يعرّف كائناً مفرداً (object) باسم GCSFilter ويفتح نطاقه. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:20]

```
21:     data class Params(
```
> يعرّف صنف بيانات (data class) باسم Params (المَعلَمات) ويفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:21]

```
22:         val p: Int,         // Golomb-Rice parameter (>= 1)
```
> يعرّف خاصية ثابتة p من نوع Int؛ تعليق: مَعلَمة غولومب-رايس (>= 1). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:22]

```
23:         val m: Long,        // Range M = N * 2^P
```
> يعرّف خاصية ثابتة m من نوع Long؛ تعليق: المدى M = N * 2^P. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:23]

```
24:         val data: ByteArray // Encoded GR bitstream
```
> يعرّف خاصية ثابتة data من نوع ByteArray (مصفوفة بايتات)؛ تعليق: تيار بتات غولومب-رايس المُرمّز. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:24]

```
25:     )
```
> إغلاق قائمة وُسطاء صنف البيانات Params. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:25]

```
26: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:26]

```
27:     // Derive P from target FPR; FPR ~= 1 / 2^P
```
> تعليق: اشتقاق P من معدّل الإيجابيات الكاذبة المستهدف (target FPR)؛ FPR يقارب 1 / 2^P. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:27]

```
28:     fun deriveP(targetFpr: Double): Int {
```
> يعرّف الدالة deriveP (اشتقاق P) التي تأخذ targetFpr من نوع Double وتُعيد Int، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:28]

```
29:         val f = targetFpr.coerceIn(0.000001, 0.25)
```
> يعرّف ثابتاً f مساوياً لـ targetFpr مقيّداً ضمن المدى [0.000001، 0.25]. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:29]

```
30:         return ceil(ln(1.0 / f) / ln(2.0)).toInt().coerceAtLeast(1)
```
> يُعيد التقريب لأعلى لـ (ln(1.0/f) / ln(2.0)) محوّلاً إلى Int ومقيّداً ليكون 1 على الأقل. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:30]

```
31:     }
```
> إغلاق نطاق الدالة deriveP. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:31]

```
32: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:32]

```
33:     // Rough capacity estimate: expected bits per element ~= P + 2 (quotient unary ~ around 2 bits)
```
> تعليق: تقدير تقريبي للسعة: عدد البتات المتوقّع لكل عنصر يقارب P + 2 (الخارج بالترميز الأحادي يقارب نحو 2 بت). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:33]

```
34:     fun estimateMaxElementsForSize(bytes: Int, p: Int): Int {
```
> يعرّف الدالة estimateMaxElementsForSize (تقدير أقصى عدد عناصر لحجم) التي تأخذ bytes و p من نوع Int وتُعيد Int، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:34]

```
35:         val bits = (bytes * 8).coerceAtLeast(8)
```
> يعرّف ثابتاً bits مساوياً لـ (bytes * 8) مقيّداً ليكون 8 على الأقل. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:35]

```
36:         val per = (p + 2).coerceAtLeast(3)
```
> يعرّف ثابتاً per مساوياً لـ (p + 2) مقيّداً ليكون 3 على الأقل. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:36]

```
37:         return (bits / per).coerceAtLeast(1)
```
> يُعيد ناتج القسمة (bits / per) مقيّداً ليكون 1 على الأقل. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:37]

```
38:     }
```
> إغلاق نطاق الدالة estimateMaxElementsForSize. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:38]

```
39: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:39]

```
40:     fun buildFilter(
```
> يعرّف الدالة buildFilter (بناء المرشّح) ويفتح قائمة وُسطائها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:40]

```
41:         ids: List<ByteArray>, // 16-byte PacketId bytes
```
> يعرّف الوسيط ids من نوع List<ByteArray> (قائمة مصفوفات بايتات)؛ تعليق: بايتات معرّف الرزمة ذي الـ16 بايتاً. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:41]

```
42:         maxBytes: Int,
```
> يعرّف الوسيط maxBytes (أقصى عدد بايتات) من نوع Int. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:42]

```
43:         targetFpr: Double
```
> يعرّف الوسيط targetFpr (معدّل الإيجابيات الكاذبة المستهدف) من نوع Double. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:43]

```
44:     ): Params {
```
> يحدّد نوع إرجاع الدالة buildFilter بأنه Params ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:44]

```
45:         val p = deriveP(targetFpr)
```
> يعرّف ثابتاً p مساوياً لنتيجة استدعاء deriveP بالوسيط targetFpr. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:45]

```
46:         val nCap = estimateMaxElementsForSize(maxBytes, p)
```
> يعرّف ثابتاً nCap (سقف العدد) مساوياً لنتيجة estimateMaxElementsForSize بالوسيطين maxBytes و p. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:46]

```
47:         var trimmedN = ids.size.coerceAtMost(nCap)
```
> يعرّف متغيّراً trimmedN (العدد المقتطَع) مساوياً لحجم ids مقيّداً ليكون nCap على الأكثر. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:47]

```
48: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:48]

```
49:         var finalM = (trimmedN.toLong() shl p).coerceAtLeast(1L)
```
> يعرّف متغيّراً finalM (المدى النهائي M) مساوياً لـ trimmedN محوّلاً إلى Long مزاحاً يساراً بمقدار p، مقيّداً ليكون 1L على الأقل. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:49]

```
50:         var selected = ids.take(trimmedN)
```
> يعرّف متغيّراً selected (المُختار) مساوياً لأول trimmedN عنصراً من ids. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:50]

```
51:         var mapped = selected.map { id ->
```
> يعرّف متغيّراً mapped (المُحوَّل) مساوياً لتطبيق دالة على كل عنصر id من selected، ويفتح جسم الدالة اللامية (lambda). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:51]

```
52:             val v = h64(id) % finalM
```
> يعرّف ثابتاً v مساوياً لباقي قسمة h64(id) على finalM. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:52]

```
53:             if (v == 0L) 1L else v
```
> يُعيد القيمة 1L إذا كان v يساوي 0L وإلا يُعيد v. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:53]

```
54:         }.distinct().sorted()
```
> يغلق الدالة اللامية ثم يطبّق distinct (إزالة المكرّرات) ثم sorted (ترتيب تصاعدي) على النتيجة. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:54]

```
55:         var encoded = encode(mapped, p)
```
> يعرّف متغيّراً encoded (المُرمَّز) مساوياً لنتيجة استدعاء encode بالوسيطين mapped و p. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:55]

```
56: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:56]

```
57:         // If estimate was too optimistic, trim until it fits
```
> تعليق: إذا كان التقدير متفائلاً أكثر من اللازم، اقتطع حتى يلائم الحجم. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:57]

```
58:         while (encoded.size > maxBytes && trimmedN > 0) {
```
> يفتح حلقة while تستمرّ ما دام حجم encoded أكبر من maxBytes و trimmedN أكبر من 0. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:58]

```
59:             trimmedN = (trimmedN * 9) / 10 // drop 10%
```
> يسند إلى trimmedN ناتج (trimmedN * 9) / 10؛ تعليق: إنقاص 10%. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:59]

```
60:             finalM = (trimmedN.toLong() shl p).coerceAtLeast(1L)
```
> يسند إلى finalM قيمة trimmedN محوّلاً إلى Long مزاحاً يساراً بمقدار p، مقيّداً ليكون 1L على الأقل. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:60]

```
61:             selected = ids.take(trimmedN)
```
> يسند إلى selected أول trimmedN عنصراً من ids. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:61]

```
62:             mapped = selected.map { id ->
```
> يسند إلى mapped تطبيق دالة على كل عنصر id من selected، ويفتح جسم الدالة اللامية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:62]

```
63:                 val v = h64(id) % finalM
```
> يعرّف ثابتاً v مساوياً لباقي قسمة h64(id) على finalM. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:63]

```
64:                 if (v == 0L) 1L else v
```
> يُعيد القيمة 1L إذا كان v يساوي 0L وإلا يُعيد v. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:64]

```
65:             }.distinct().sorted()
```
> يغلق الدالة اللامية ثم يطبّق distinct ثم sorted على النتيجة. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:65]

```
66:             encoded = encode(mapped, p)
```
> يسند إلى encoded نتيجة استدعاء encode بالوسيطين mapped و p. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:66]

```
67:         }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:67]

```
68: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:68]

```
69:         return Params(p = p, m = finalM, data = encoded)
```
> يُعيد كائن Params بالقيم p = p و m = finalM و data = encoded. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:69]

```
70:     }
```
> إغلاق نطاق الدالة buildFilter. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:70]

```
71: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:71]

```
72:     fun decodeToSortedSet(p: Int, m: Long, data: ByteArray): LongArray {
```
> يعرّف الدالة decodeToSortedSet (فك الترميز إلى مجموعة مرتّبة) التي تأخذ p من نوع Int و m من نوع Long و data من نوع ByteArray وتُعيد LongArray، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:72]

```
73:         val values = ArrayList<Long>()
```
> يعرّف ثابتاً values مساوياً لقائمة ArrayList فارغة من نوع Long. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:73]

```
74:         val reader = BitReader(data)
```
> يعرّف ثابتاً reader (القارئ) مساوياً لكائن جديد BitReader مُنشأ بالوسيط data. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:74]

```
75:         var acc = 0L
```
> يعرّف متغيّراً acc (المُراكِم) مبدئياً بالقيمة 0L. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:75]

```
76:         val mask = (1L shl p) - 1L
```
> يعرّف ثابتاً mask (القناع) مساوياً لـ (1L مزاحاً يساراً بمقدار p) ناقص 1L. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:76]

```
77:         while (!reader.eof()) {
```
> يفتح حلقة while تستمرّ ما دام reader.eof() (بلوغ نهاية البيانات) غير صحيح. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:77]

```
78:             // Read unary quotient (q ones terminated by zero)
```
> تعليق: اقرأ الخارج بالترميز الأحادي (q من الآحاد ينتهي بصفر). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:78]

```
79:             var q = 0L
```
> يعرّف متغيّراً q مبدئياً بالقيمة 0L. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:79]

```
80:             while (true) {
```
> يفتح حلقة while لا نهائية الشرط (true). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:80]

```
81:                 val b = reader.readBit() ?: break
```
> يعرّف ثابتاً b مساوياً لنتيجة reader.readBit()، وإن كانت null فاكسر الحلقة. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:81]

```
82:                 if (b == 1) q++ else break
```
> إذا كان b يساوي 1 فزِد q بمقدار 1، وإلا فاكسر الحلقة. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:82]

```
83:             }
```
> إغلاق نطاق حلقة while الداخلية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:83]

```
84:             if (reader.lastWasEOF) break
```
> إذا كانت الخاصية reader.lastWasEOF صحيحة فاكسر الحلقة الخارجية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:84]

```
85:             // Read remainder
```
> تعليق: اقرأ الباقي (remainder). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:85]

```
86:             val r = reader.readBits(p) ?: break
```
> يعرّف ثابتاً r مساوياً لنتيجة reader.readBits(p)، وإن كانت null فاكسر الحلقة. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:86]

```
87:             val x = (q shl p) + r + 1
```
> يعرّف ثابتاً x مساوياً لـ (q مزاحاً يساراً بمقدار p) زائد r زائد 1. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:87]

```
88:             acc += x
```
> يزيد acc بمقدار x. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:88]

```
89:             if (acc >= m) break // out of range safeguard
```
> إذا كان acc أكبر من أو يساوي m فاكسر الحلقة؛ تعليق: حماية من تجاوز المدى. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:89]

```
90:             values.add(acc)
```
> يضيف القيمة acc إلى القائمة values. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:90]

```
91:         }
```
> إغلاق نطاق حلقة while الخارجية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:91]

```
92:         return values.toLongArray()
```
> يُعيد القائمة values محوّلةً إلى LongArray (مصفوفة Long). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:92]

```
93:     }
```
> إغلاق نطاق الدالة decodeToSortedSet. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:93]

```
94: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:94]

```
95:     fun contains(sortedValues: LongArray, candidate: Long): Boolean {
```
> يعرّف الدالة contains (يحتوي) التي تأخذ sortedValues من نوع LongArray و candidate من نوع Long وتُعيد Boolean، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:95]

```
96:         var lo = 0
```
> يعرّف متغيّراً lo (الأدنى) مبدئياً بالقيمة 0. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:96]

```
97:         var hi = sortedValues.size - 1
```
> يعرّف متغيّراً hi (الأعلى) مساوياً لحجم sortedValues ناقص 1. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:97]

```
98:         while (lo <= hi) {
```
> يفتح حلقة while تستمرّ ما دام lo أصغر من أو يساوي hi. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:98]

```
99:             val mid = (lo + hi) ushr 1
```
> يعرّف ثابتاً mid (الأوسط) مساوياً لـ (lo + hi) مزاحاً يميناً منطقياً بمقدار 1. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:99]

```
100:             val v = sortedValues[mid]
```
> يعرّف ثابتاً v مساوياً لعنصر sortedValues عند الفهرس mid. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:100]

```
101:             if (v == candidate) return true
```
> إذا كان v يساوي candidate فأعِد true. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:101]

```
102:             if (v < candidate) lo = mid + 1 else hi = mid - 1
```
> إذا كان v أصغر من candidate فأسند lo = mid + 1 وإلا فأسند hi = mid - 1. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:102]

```
103:         }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:103]

```
104:         return false
```
> يُعيد false. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:104]

```
105:     }
```
> إغلاق نطاق الدالة contains. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:105]

```
106: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:106]

```
107:     internal fun h64(id16: ByteArray): Long {
```
> يعرّف الدالة الداخلية (internal) h64 التي تأخذ id16 من نوع ByteArray وتُعيد Long، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:107]

```
108:         val md = MessageDigest.getInstance("SHA-256")
```
> يعرّف ثابتاً md مساوياً لنسخة MessageDigest من خوارزمية "SHA-256". [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:108]

```
109:         md.update(id16)
```
> يستدعي md.update مُمرِّراً id16 لتغذية المُلخِّص بالبيانات. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:109]

```
110:         val d = md.digest()
```
> يعرّف ثابتاً d مساوياً لنتيجة md.digest() (الملخّص النهائي). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:110]

```
111:         var x = 0L
```
> يعرّف متغيّراً x مبدئياً بالقيمة 0L. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:111]

```
112:         for (i in 0 until 8) {
```
> يفتح حلقة for بالمتغيّر i من 0 حتى ما قبل 8. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:112]

```
113:             x = (x shl 8) or ((d[i].toLong() and 0xFF))
```
> يسند إلى x نتيجة (x مزاحاً يساراً بمقدار 8) دمجاً بـ OR مع (d[i] محوّلاً إلى Long ومقنّعاً بـ 0xFF). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:113]

```
114:         }
```
> إغلاق نطاق حلقة for. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:114]

```
115:         return x and 0x7fff_ffff_ffff_ffffL // positive
```
> يُعيد x مقنّعاً بـ 0x7fff_ffff_ffff_ffffL؛ تعليق: موجب. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:115]

```
116:     }
```
> إغلاق نطاق الدالة h64. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:116]

```
117: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:117]

```
118:     private fun encode(sorted: List<Long>, p: Int): ByteArray {
```
> يعرّف الدالة الخاصة (private) encode التي تأخذ sorted من نوع List<Long> و p من نوع Int وتُعيد ByteArray، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:118]

```
119:         val bw = BitWriter()
```
> يعرّف ثابتاً bw (الكاتب) مساوياً لكائن جديد BitWriter. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:119]

```
120:         var prev = 0L
```
> يعرّف متغيّراً prev (السابق) مبدئياً بالقيمة 0L. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:120]

```
121:         val mask = (1L shl p) - 1L
```
> يعرّف ثابتاً mask مساوياً لـ (1L مزاحاً يساراً بمقدار p) ناقص 1L. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:121]

```
122:         for (v in sorted) {
```
> يفتح حلقة for تمرّ على كل عنصر v في sorted. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:122]

```
123:             val delta = v - prev
```
> يعرّف ثابتاً delta (الفرق) مساوياً لـ v ناقص prev. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:123]

```
124:             prev = v
```
> يسند إلى prev قيمة v. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:124]

```
125:             val x = delta
```
> يعرّف ثابتاً x مساوياً لـ delta. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:125]

```
126:             val q = (x - 1) ushr p
```
> يعرّف ثابتاً q مساوياً لـ (x - 1) مزاحاً يميناً منطقياً بمقدار p. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:126]

```
127:             val r = (x - 1) and mask
```
> يعرّف ثابتاً r مساوياً لـ (x - 1) مقنّعاً بـ mask. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:127]

```
128:             // unary q ones then a zero
```
> تعليق: q من الآحاد بالترميز الأحادي ثم صفر. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:128]

```
129:             repeat(q.toInt()) { bw.writeBit(1) }
```
> يكرّر q (محوّلاً إلى Int) مرّةً استدعاءَ bw.writeBit(1). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:129]

```
130:             bw.writeBit(0)
```
> يستدعي bw.writeBit(0) لكتابة بت صفر. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:130]

```
131:             // then P bits of r (MSB-first)
```
> تعليق: ثم P بتاً من r (بدءاً من البت الأعلى أهمية). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:131]

```
132:             bw.writeBits(r, p)
```
> يستدعي bw.writeBits بالوسيطين r و p لكتابة p بتاً من r. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:132]

```
133:         }
```
> إغلاق نطاق حلقة for. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:133]

```
134:         return bw.toByteArray()
```
> يُعيد نتيجة bw.toByteArray(). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:134]

```
135:     }
```
> إغلاق نطاق الدالة encode. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:135]

```
136: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:136]

```
137:     // Simple MSB-first bit writer
```
> تعليق: كاتب بتات بسيط يبدأ من البت الأعلى أهمية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:137]

```
138:     private class BitWriter {
```
> يعرّف الصنف الخاص BitWriter (كاتب البتات) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:138]

```
139:         private val buf = ArrayList<Byte>()
```
> يعرّف خاصية خاصة ثابتة buf (المخزن) مساوية لقائمة ArrayList فارغة من نوع Byte. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:139]

```
140:         private var cur = 0
```
> يعرّف خاصية خاصة متغيّرة cur (الحالي) مبدئية بالقيمة 0. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:140]

```
141:         private var nbits = 0
```
> يعرّف خاصية خاصة متغيّرة nbits (عدد البتات) مبدئية بالقيمة 0. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:141]

```
142:         fun writeBit(bit: Int) {
```
> يعرّف الدالة writeBit (اكتب بت) التي تأخذ bit من نوع Int، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:142]

```
143:             cur = (cur shl 1) or (bit and 1)
```
> يسند إلى cur نتيجة (cur مزاحاً يساراً بمقدار 1) دمجاً بـ OR مع (bit مقنّعاً بـ 1). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:143]

```
144:             nbits++
```
> يزيد nbits بمقدار 1. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:144]

```
145:             if (nbits == 8) {
```
> إذا كان nbits يساوي 8 يفتح كتلة شرطية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:145]

```
146:                 buf.add(cur.toByte())
```
> يضيف cur محوّلاً إلى Byte إلى buf. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:146]

```
147:                 cur = 0; nbits = 0
```
> يسند إلى cur القيمة 0 وإلى nbits القيمة 0. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:147]

```
148:             }
```
> إغلاق نطاق الكتلة الشرطية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:148]

```
149:         }
```
> إغلاق نطاق الدالة writeBit. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:149]

```
150:         fun writeBits(value: Long, count: Int) {
```
> يعرّف الدالة writeBits (اكتب بتات) التي تأخذ value من نوع Long و count من نوع Int، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:150]

```
151:             if (count <= 0) return
```
> إذا كان count أصغر من أو يساوي 0 فارجع (أنهِ الدالة). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:151]

```
152:             for (i in count - 1 downTo 0) {
```
> يفتح حلقة for بالمتغيّر i من (count - 1) تنازلياً حتى 0. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:152]

```
153:                 val bit = ((value ushr i) and 1L).toInt()
```
> يعرّف ثابتاً bit مساوياً لـ ((value مزاحاً يميناً منطقياً بمقدار i) مقنّعاً بـ 1L) محوّلاً إلى Int. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:153]

```
154:                 writeBit(bit)
```
> يستدعي writeBit بالوسيط bit. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:154]

```
155:             }
```
> إغلاق نطاق حلقة for. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:155]

```
156:         }
```
> إغلاق نطاق الدالة writeBits. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:156]

```
157:         fun toByteArray(): ByteArray {
```
> يعرّف الدالة toByteArray التي تُعيد ByteArray، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:157]

```
158:             if (nbits > 0) {
```
> إذا كان nbits أكبر من 0 يفتح كتلة شرطية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:158]

```
159:                 val rem = cur shl (8 - nbits)
```
> يعرّف ثابتاً rem (الباقي) مساوياً لـ cur مزاحاً يساراً بمقدار (8 - nbits). [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:159]

```
160:                 buf.add(rem.toByte())
```
> يضيف rem محوّلاً إلى Byte إلى buf. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:160]

```
161:                 cur = 0; nbits = 0
```
> يسند إلى cur القيمة 0 وإلى nbits القيمة 0. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:161]

```
162:             }
```
> إغلاق نطاق الكتلة الشرطية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:162]

```
163:             return buf.toByteArray()
```
> يُعيد buf محوّلاً إلى ByteArray. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:163]

```
164:         }
```
> إغلاق نطاق الدالة toByteArray. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:164]

```
165:     }
```
> إغلاق نطاق الصنف BitWriter. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:165]

```
166: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:166]

```
167:     // Simple MSB-first bit reader
```
> تعليق: قارئ بتات بسيط يبدأ من البت الأعلى أهمية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:167]

```
168:     private class BitReader(private val data: ByteArray) {
```
> يعرّف الصنف الخاص BitReader (قارئ البتات) بمُنشئ يأخذ خاصية خاصة ثابتة data من نوع ByteArray، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:168]

```
169:         private var i = 0
```
> يعرّف خاصية خاصة متغيّرة i مبدئية بالقيمة 0. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:169]

```
170:         private var nleft = 8
```
> يعرّف خاصية خاصة متغيّرة nleft (المتبقّي) مبدئية بالقيمة 8. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:170]

```
171:         private var cur = if (data.isNotEmpty()) (data[0].toInt() and 0xFF) else 0
```
> يعرّف خاصية خاصة متغيّرة cur مساوية لـ (data[0] محوّلاً إلى Int ومقنّعاً بـ 0xFF) إذا كانت data غير فارغة، وإلا 0. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:171]

```
172:         var lastWasEOF: Boolean = false
```
> يعرّف خاصية متغيّرة lastWasEOF (آخرها كان نهاية الملف) من نوع Boolean مبدئية بـ false. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:172]

```
173:             private set
```
> يجعل أداة الضبط (setter) لهذه الخاصية خاصة. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:173]

```
174:         fun eof() = i >= data.size
```
> يعرّف الدالة eof التي تُعيد نتيجة المقارنة i >= data.size. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:174]

```
175:         fun readBit(): Int? {
```
> يعرّف الدالة readBit (اقرأ بت) التي تُعيد Int? (قابل لأن يكون null)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:175]

```
176:             if (i >= data.size) { lastWasEOF = true; return null }
```
> إذا كان i أكبر من أو يساوي data.size يسند true إلى lastWasEOF ويُعيد null. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:176]

```
177:             val bit = (cur ushr 7) and 1
```
> يعرّف ثابتاً bit مساوياً لـ (cur مزاحاً يميناً منطقياً بمقدار 7) مقنّعاً بـ 1. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:177]

```
178:             cur = (cur shl 1) and 0xFF
```
> يسند إلى cur نتيجة (cur مزاحاً يساراً بمقدار 1) مقنّعاً بـ 0xFF. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:178]

```
179:             nleft--
```
> ينقص nleft بمقدار 1. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:179]

```
180:             if (nleft == 0) {
```
> إذا كان nleft يساوي 0 يفتح كتلة شرطية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:180]

```
181:                 i++
```
> يزيد i بمقدار 1. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:181]

```
182:                 if (i < data.size) {
```
> إذا كان i أصغر من data.size يفتح كتلة شرطية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:182]

```
183:                     cur = data[i].toInt() and 0xFF
```
> يسند إلى cur قيمة data[i] محوّلاً إلى Int ومقنّعاً بـ 0xFF. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:183]

```
184:                     nleft = 8
```
> يسند إلى nleft القيمة 8. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:184]

```
185:                 }
```
> إغلاق نطاق الكتلة الشرطية الداخلية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:185]

```
186:             }
```
> إغلاق نطاق الكتلة الشرطية الخارجية. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:186]

```
187:             return bit
```
> يُعيد bit. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:187]

```
188:         }
```
> إغلاق نطاق الدالة readBit. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:188]

```
189:         fun readBits(count: Int): Long? {
```
> يعرّف الدالة readBits (اقرأ بتات) التي تأخذ count من نوع Int وتُعيد Long? (قابل لأن يكون null)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:189]

```
190:             var v = 0L
```
> يعرّف متغيّراً v مبدئياً بالقيمة 0L. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:190]

```
191:             for (k in 0 until count) {
```
> يفتح حلقة for بالمتغيّر k من 0 حتى ما قبل count. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:191]

```
192:                 val b = readBit() ?: return null
```
> يعرّف ثابتاً b مساوياً لنتيجة readBit()، وإن كانت null فأعِد null. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:192]

```
193:                 v = (v shl 1) or b.toLong()
```
> يسند إلى v نتيجة (v مزاحاً يساراً بمقدار 1) دمجاً بـ OR مع b محوّلاً إلى Long. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:193]

```
194:             }
```
> إغلاق نطاق حلقة for. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:194]

```
195:             return v
```
> يُعيد v. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:195]

```
196:         }
```
> إغلاق نطاق الدالة readBits. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:196]

```
197:     }
```
> إغلاق نطاق الصنف BitReader. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:197]

```
198: }
```
> إغلاق نطاق الكائن GCSFilter. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:198]

```
199: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/GCSFilter.kt:199]
