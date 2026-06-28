# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يعرّف انتماء الملف للحزمة (package) باسم com.bitchat.android.nostr. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:2]

```
3: import android.util.Log
```
> يستورد صنف السجلّ (Log) من حزمة android.util. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:3]

```
4: import kotlinx.coroutines.Dispatchers
```
> يستورد الموزّعات (Dispatchers) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:4]

```
5: import kotlinx.coroutines.withContext
```
> يستورد الدالة withContext من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:5]

```
6: import java.security.MessageDigest
```
> يستورد صنف ملخّص الرسالة (MessageDigest) من حزمة java.security. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:6]

```
7: import kotlin.random.Random
```
> يستورد صنف العشوائي (Random) من حزمة kotlin.random. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:8]

```
9: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:9]

```
10:  * Nostr Proof of Work (PoW) implementation following NIP-13
```
> تعليق: تنفيذ إثبات العمل (Proof of Work) لنوستر باتّباع المعيار NIP-13. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:10]

```
11:  * 
```
> تعليق: سطر فارغ داخل كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:11]

```
12:  * This implements the Proof of Work system for Nostr events to provide spam deterrence.
```
> تعليق: هذا يُنفّذ نظام إثبات العمل لأحداث نوستر لتوفير ردع للرسائل المزعجة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:12]

```
13:  * The difficulty is defined as the number of leading zero bits in the event ID.
```
> تعليق: الصعوبة معرّفة بأنها عدد بتّات الصفر البادئة في معرّف الحدث. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:13]

```
14:  * 
```
> تعليق: سطر فارغ داخل كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:14]

```
15:  * Reference: https://github.com/nostr-protocol/nips/blob/master/13.md
```
> تعليق: المرجع هو الرابط المذكور لمعيار NIP-13. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:15]

```
16:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:16]

```
17: object NostrProofOfWork {
```
> يعرّف كائناً مفرداً (object) باسم إثبات عمل نوستر (NostrProofOfWork) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:17]

```
18:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:18]

```
19:     private const val TAG = "NostrProofOfWork"
```
> يعرّف ثابتاً خاصاً (private const) باسم TAG وقيمته السلسلة النصية "NostrProofOfWork". [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:19]

```
20:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:20]

```
21:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:21]

```
22:      * Calculate the difficulty (number of leading zero bits) of an event ID
```
> تعليق: احسب الصعوبة (عدد بتّات الصفر البادئة) لمعرّف حدث. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:22]

```
23:      * @param eventIdHex The hexadecimal event ID
```
> تعليق: المعامل eventIdHex هو معرّف الحدث بالنظام الست عشري. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:23]

```
24:      * @return The number of leading zero bits
```
> تعليق: تُعيد الدالة عدد بتّات الصفر البادئة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:24]

```
25:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:25]

```
26:     fun calculateDifficulty(eventIdHex: String): Int {
```
> يعرّف دالة باسم احسب الصعوبة (calculateDifficulty) تأخذ معامل eventIdHex من نوع سلسلة نصية وتُعيد عدداً صحيحاً، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:26]

```
27:         var count = 0
```
> يعرّف متغيّراً (var) باسم count ويضبط قيمته الابتدائية على الصفر. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:27]

```
28:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:28]

```
29:         for (i in eventIdHex.indices) {
```
> يبدأ حلقة تكرار (for) بالمتغيّر i على مدى فهارس السلسلة eventIdHex، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:29]

```
30:             val nibble = eventIdHex[i].toString().toInt(16)
```
> يعرّف قيمة ثابتة (val) باسم nibble وتُحسب بتحويل الحرف عند الفهرس i إلى سلسلة ثم إلى عدد صحيح بالأساس ١٦. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:30]

```
31:             if (nibble == 0) {
```
> يفحص شرطاً (if): إن كانت القيمة nibble تساوي صفراً، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:31]

```
32:                 count += 4
```
> يزيد المتغيّر count بمقدار ٤. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:32]

```
33:             } else {
```
> يغلق نطاق if ويفتح نطاق else (وإلّا). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:33]

```
34:                 // Count leading zeros in the nibble
```
> تعليق: احسب الأصفار البادئة في النِّبل (nibble). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:34]

```
35:                 count += when (nibble) {
```
> يزيد المتغيّر count بناتج تعبير when (عند) المطبّق على القيمة nibble، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:35]

```
36:                     1 -> 3  // 0001
```
> في تعبير when: إن كانت القيمة ١ فالناتج ٣، والتعليق: 0001. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:36]

```
37:                     2, 3 -> 2  // 001x
```
> في تعبير when: إن كانت القيمة ٢ أو ٣ فالناتج ٢، والتعليق: 001x. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:37]

```
38:                     4, 5, 6, 7 -> 1  // 01xx
```
> في تعبير when: إن كانت القيمة ٤ أو ٥ أو ٦ أو ٧ فالناتج ١، والتعليق: 01xx. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:38]

```
39:                     else -> 0  // 1xxx
```
> في تعبير when: في الحالة الأخرى (else) الناتج ٠، والتعليق: 1xxx. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:39]

```
40:                 }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:40]

```
41:                 break
```
> ينفّذ break فيخرج من حلقة التكرار. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:41]

```
42:             }
```
> إغلاق نطاق else. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:42]

```
43:         }
```
> إغلاق نطاق حلقة for. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:43]

```
44:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:44]

```
45:         return count
```
> يُعيد قيمة المتغيّر count. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:45]

```
46:     }
```
> إغلاق نطاق دالة calculateDifficulty. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:46]

```
47:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:47]

```
48:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:48]

```
49:      * Validate that an event meets the minimum difficulty requirement
```
> تعليق: تحقّق من أن الحدث يحقّق متطلّب الصعوبة الأدنى. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:49]

```
50:      * @param event The Nostr event to validate
```
> تعليق: المعامل event هو حدث نوستر المراد التحقّق منه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:50]

```
51:      * @param minimumDifficulty The minimum required difficulty
```
> تعليق: المعامل minimumDifficulty هو الصعوبة الدنيا المطلوبة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:51]

```
52:      * @return true if the event meets the difficulty requirement
```
> تعليق: تُعيد القيمة true إن كان الحدث يحقّق متطلّب الصعوبة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:52]

```
53:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:53]

```
54:     fun validateDifficulty(event: NostrEvent, minimumDifficulty: Int): Boolean {
```
> يعرّف دالة باسم تحقّق من الصعوبة (validateDifficulty) تأخذ معامل event من نوع NostrEvent ومعامل minimumDifficulty من نوع عدد صحيح وتُعيد قيمة منطقية، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:54]

```
55:         if (minimumDifficulty <= 0) return true
```
> يفحص شرطاً: إن كانت minimumDifficulty أصغر من أو تساوي صفراً فيُعيد true. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:55]

```
56:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:56]

```
57:         // Require explicit nonce tag to recognize PoW per NIP-13 intent
```
> تعليق: اطلب وسماً صريحاً للقيمة العشوائية (nonce) للاعتراف بإثبات العمل وفق مقصد NIP-13. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:57]

```
58:         if (!hasNonce(event)) {
```
> يفحص شرطاً: إن لم يكن للحدث event قيمة عشوائية (نتيجة hasNonce هي false)، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:58]

```
59:             Log.w(TAG, "Event ${event.id.take(16)}... missing nonce tag; treating as no PoW")
```
> يستدعي Log.w لتسجيل تحذير بالوسم TAG ونصّ يضمّ أول ١٦ محرفاً من معرّف الحدث ورسالة أن وسم nonce مفقود ويُعامل بلا إثبات عمل. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:59]

```
60:             return false
```
> يُعيد القيمة false. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:60]

```
61:         }
```
> إغلاق نطاق if. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:61]

```
62:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:62]

```
63:         val actualDifficulty = calculateDifficulty(event.id)
```
> يعرّف قيمة ثابتة باسم actualDifficulty تُحسب باستدعاء calculateDifficulty على معرّف الحدث event.id. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:63]

```
64:         val committedDifficulty = getCommittedDifficulty(event)
```
> يعرّف قيمة ثابتة باسم committedDifficulty تُحسب باستدعاء getCommittedDifficulty على الحدث event. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:64]

```
65:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:65]

```
66:         Log.d(TAG, "Validating PoW: actual=$actualDifficulty, required=$minimumDifficulty, committed=$committedDifficulty")
```
> يستدعي Log.d لتسجيل رسالة تصحيح بالوسم TAG تعرض قيم actualDifficulty وminimumDifficulty وcommittedDifficulty. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:66]

```
67:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:67]

```
68:         // Check if actual difficulty meets requirement
```
> تعليق: افحص ما إذا كانت الصعوبة الفعلية تحقّق المتطلّب. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:68]

```
69:         if (actualDifficulty < minimumDifficulty) {
```
> يفحص شرطاً: إن كانت actualDifficulty أصغر من minimumDifficulty، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:69]

```
70:             Log.w(TAG, "Event ${event.id.take(16)}... has insufficient difficulty: $actualDifficulty < $minimumDifficulty")
```
> يستدعي Log.w لتسجيل تحذير بالوسم TAG ونصّ يضمّ أول ١٦ محرفاً من معرّف الحدث وأن صعوبته غير كافية مع عرض actualDifficulty وminimumDifficulty. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:70]

```
71:             return false
```
> يُعيد القيمة false. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:71]

```
72:         }
```
> إغلاق نطاق if. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:72]

```
73:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:73]

```
74:         // If there's a committed difficulty, it should match or exceed the minimum
```
> تعليق: إن وُجدت صعوبة ملتزَم بها فيجب أن تساوي الحدّ الأدنى أو تتجاوزه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:74]

```
75:         if (committedDifficulty != null && committedDifficulty < minimumDifficulty) {
```
> يفحص شرطاً: إن كانت committedDifficulty ليست null وأصغر من minimumDifficulty، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:75]

```
76:             Log.w(TAG, "Event ${event.id.take(16)}... has committed difficulty $committedDifficulty but achieved $actualDifficulty (possible spam)")
```
> يستدعي Log.w لتسجيل تحذير بالوسم TAG ونصّ يضمّ أول ١٦ محرفاً من معرّف الحدث وقيمة committedDifficulty وactualDifficulty مع إشارة (احتمال رسالة مزعجة). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:76]

```
77:             return false
```
> يُعيد القيمة false. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:77]

```
78:         }
```
> إغلاق نطاق if. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:78]

```
79:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:79]

```
80:         return true
```
> يُعيد القيمة true. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:80]

```
81:     }
```
> إغلاق نطاق دالة validateDifficulty. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:81]

```
82:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:82]

```
83:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:83]

```
84:      * Mine a Nostr event to achieve the target difficulty
```
> تعليق: عدّن (mine) حدث نوستر لتحقيق الصعوبة المستهدفة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:84]

```
85:      * @param event The event to mine (will be modified with nonce tag)
```
> تعليق: المعامل event هو الحدث المراد تعدينه (سيُعدّل بإضافة وسم nonce). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:85]

```
86:      * @param targetDifficulty The target difficulty to achieve
```
> تعليق: المعامل targetDifficulty هو الصعوبة المستهدفة المراد تحقيقها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:86]

```
87:      * @param maxIterations Maximum number of iterations before giving up (default: 1,000,000)
```
> تعليق: المعامل maxIterations هو أقصى عدد للتكرارات قبل الاستسلام (الافتراضي: ١٬٠٠٠٬٠٠٠). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:87]

```
88:      * @return The mined event with nonce tag, or null if mining failed
```
> تعليق: تُعيد الحدث المعدَّن مع وسم nonce، أو null إن فشل التعدين. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:88]

```
89:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:89]

```
90:     suspend fun mineEvent(
```
> يعرّف دالة معلَّقة (suspend) باسم عدّن الحدث (mineEvent) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:90]

```
91:         event: NostrEvent,
```
> يعرّف المعامل event من نوع NostrEvent. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:91]

```
92:         targetDifficulty: Int,
```
> يعرّف المعامل targetDifficulty من نوع عدد صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:92]

```
93:         maxIterations: Int = 1_000_000
```
> يعرّف المعامل maxIterations من نوع عدد صحيح بقيمة افتراضية ١٬٠٠٠٬٠٠٠. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:93]

```
94:     ): NostrEvent? = withContext(Dispatchers.Default) {
```
> يغلق قائمة المعاملات ويحدّد نوع الإعادة NostrEvent اختياري، ويُسند جسم الدالة إلى استدعاء withContext بالموزّع Dispatchers.Default، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:94]

```
95:         if (targetDifficulty <= 0) return@withContext event
```
> يفحص شرطاً: إن كانت targetDifficulty أصغر من أو تساوي صفراً فيُعيد event من كتلة withContext. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:95]

```
96:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:96]

```
97:         Log.d(TAG, "Starting PoW mining for difficulty $targetDifficulty...")
```
> يستدعي Log.d لتسجيل رسالة تصحيح بالوسم TAG تفيد ببدء تعدين إثبات العمل للصعوبة targetDifficulty. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:97]

```
98:         val startTime = System.currentTimeMillis()
```
> يعرّف قيمة ثابتة باسم startTime تُسند إليها قيمة الوقت الحالي بالملّي ثانية من System.currentTimeMillis. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:98]

```
99:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:99]

```
100:         var nonce = Random.nextLong(0, 1_000_000).toString()
```
> يعرّف متغيّراً باسم nonce يُسند إليه عدد عشوائي طويل بين ٠ و١٬٠٠٠٬٠٠٠ محوّلاً إلى سلسلة نصية. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:100]

```
101:         var iterations = 0
```
> يعرّف متغيّراً باسم iterations ويضبط قيمته الابتدائية على الصفر. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:101]

```
102:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:102]

```
103:         while (iterations < maxIterations) {
```
> يبدأ حلقة while تستمرّ ما دامت iterations أصغر من maxIterations، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:103]

```
104:             // Create a copy of the event with the nonce tag
```
> تعليق: أنشئ نسخة من الحدث مع وسم nonce. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:104]

```
105:             val eventWithNonce = addNonceTag(event, nonce, targetDifficulty)
```
> يعرّف قيمة ثابتة باسم eventWithNonce تُحسب باستدعاء addNonceTag بالمعاملات event وnonce وtargetDifficulty. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:105]

```
106:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:106]

```
107:             // Calculate the event ID
```
> تعليق: احسب معرّف الحدث. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:107]

```
108:             val eventId = eventWithNonce.computeEventIdHex()
```
> يعرّف قيمة ثابتة باسم eventId تُحسب باستدعاء computeEventIdHex على eventWithNonce. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:108]

```
109:             val actualDifficulty = calculateDifficulty(eventId)
```
> يعرّف قيمة ثابتة باسم actualDifficulty تُحسب باستدعاء calculateDifficulty على eventId. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:109]

```
110:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:110]

```
111:             if (actualDifficulty >= targetDifficulty) {
```
> يفحص شرطاً: إن كانت actualDifficulty أكبر من أو تساوي targetDifficulty، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:111]

```
112:                 val timeElapsed = System.currentTimeMillis() - startTime
```
> يعرّف قيمة ثابتة باسم timeElapsed تساوي الوقت الحالي بالملّي ثانية ناقص startTime. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:112]

```
113:                 Log.i(TAG, "✅ PoW mining successful! Difficulty: $actualDifficulty, iterations: $iterations, time: ${timeElapsed}ms")
```
> يستدعي Log.i لتسجيل رسالة معلوماتية بالوسم TAG تفيد بنجاح تعدين إثبات العمل مع عرض actualDifficulty وiterations وtimeElapsed بالملّي ثانية. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:113]

```
114:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:114]

```
115:                 // Return the event with the computed ID
```
> تعليق: أعِد الحدث مع المعرّف المحسوب. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:115]

```
116:                 return@withContext eventWithNonce.copy(id = eventId)
```
> يُعيد من كتلة withContext نسخة من eventWithNonce مع تعيين الحقل id إلى eventId. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:116]

```
117:             }
```
> إغلاق نطاق if. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:117]

```
118:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:118]

```
119:             // Increment nonce and try again
```
> تعليق: زِد القيمة العشوائية وأعِد المحاولة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:119]

```
120:             nonce = (nonce.toLongOrNull()?.plus(1) ?: Random.nextLong()).toString()
```
> يُسند إلى nonce نتيجة تحويله إلى عدد طويل وزيادته بواحد، وإن تعذّر التحويل فعدد عشوائي طويل، محوّلاً إلى سلسلة نصية. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:120]

```
121:             iterations++
```
> يزيد المتغيّر iterations بمقدار واحد. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:121]

```
122:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:122]

```
123:             // Log progress every 100,000 iterations
```
> تعليق: سجّل التقدّم كل ١٠٠٬٠٠٠ تكرار. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:123]

```
124:             if (iterations % 100_000 == 0) {
```
> يفحص شرطاً: إن كان باقي قسمة iterations على ١٠٠٬٠٠٠ يساوي صفراً، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:124]

```
125:                 val timeElapsed = System.currentTimeMillis() - startTime
```
> يعرّف قيمة ثابتة باسم timeElapsed تساوي الوقت الحالي بالملّي ثانية ناقص startTime. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:125]

```
126:                 Log.d(TAG, "PoW mining progress: $iterations iterations, ${timeElapsed}ms elapsed")
```
> يستدعي Log.d لتسجيل رسالة تصحيح بالوسم TAG تعرض عدد iterations وtimeElapsed المنقضي بالملّي ثانية. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:126]

```
127:             }
```
> إغلاق نطاق if. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:127]

```
128:         }
```
> إغلاق نطاق حلقة while. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:128]

```
129:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:129]

```
130:         val timeElapsed = System.currentTimeMillis() - startTime
```
> يعرّف قيمة ثابتة باسم timeElapsed تساوي الوقت الحالي بالملّي ثانية ناقص startTime. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:130]

```
131:         Log.w(TAG, "❌ PoW mining failed after $maxIterations iterations (${timeElapsed}ms)")
```
> يستدعي Log.w لتسجيل تحذير بالوسم TAG يفيد بفشل تعدين إثبات العمل بعد maxIterations تكرار مع عرض timeElapsed بالملّي ثانية. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:131]

```
132:         return@withContext null
```
> يُعيد من كتلة withContext القيمة null. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:132]

```
133:     }
```
> إغلاق نطاق دالة mineEvent. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:133]

```
134:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:134]

```
135:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:135]

```
136:      * Add or update the nonce tag in an event
```
> تعليق: أضِف وسم nonce أو حدّثه في حدث. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:136]

```
137:      * @param event The original event
```
> تعليق: المعامل event هو الحدث الأصلي. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:137]

```
138:      * @param nonce The nonce value
```
> تعليق: المعامل nonce هو قيمة nonce. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:138]

```
139:      * @param targetDifficulty The target difficulty being attempted
```
> تعليق: المعامل targetDifficulty هو الصعوبة المستهدفة المحاوَلة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:139]

```
140:      * @return A new event with the nonce tag added/updated
```
> تعليق: تُعيد حدثاً جديداً مع وسم nonce مضافاً/محدَّثاً. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:140]

```
141:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:141]

```
142:     private fun addNonceTag(event: NostrEvent, nonce: String, targetDifficulty: Int): NostrEvent {
```
> يعرّف دالة خاصة باسم أضِف وسم nonce (addNonceTag) تأخذ event من نوع NostrEvent وnonce من نوع سلسلة نصية وtargetDifficulty من نوع عدد صحيح وتُعيد NostrEvent، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:142]

```
143:         val newTags = event.tags.toMutableList()
```
> يعرّف قيمة ثابتة باسم newTags تُسند إليها وسوم الحدث event.tags محوّلة إلى قائمة قابلة للتعديل. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:143]

```
144:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:144]

```
145:         // Remove existing nonce tag if present
```
> تعليق: أزِل وسم nonce الموجود إن كان حاضراً. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:145]

```
146:         newTags.removeAll { tag -> tag.isNotEmpty() && tag[0] == "nonce" }
```
> يستدعي removeAll على newTags لإزالة كل وسم tag غير فارغ وعنصره الأول يساوي "nonce". [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:146]

```
147:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:147]

```
148:         // Add new nonce tag with format: ["nonce", nonce_value, target_difficulty]
```
> تعليق: أضِف وسم nonce جديداً بالصيغة: ["nonce", nonce_value, target_difficulty]. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:148]

```
149:         newTags.add(listOf("nonce", nonce, targetDifficulty.toString()))
```
> يستدعي add على newTags لإضافة قائمة تضمّ "nonce" وقيمة nonce وtargetDifficulty محوّلاً إلى سلسلة نصية. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:149]

```
150:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:150]

```
151:         // Update created_at as recommended by NIP-13
```
> تعليق: حدّث created_at كما يوصي NIP-13. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:151]

```
152:         val updatedCreatedAt = (System.currentTimeMillis() / 1000).toInt()
```
> يعرّف قيمة ثابتة باسم updatedCreatedAt تساوي الوقت الحالي بالملّي ثانية مقسوماً على ١٠٠٠ محوّلاً إلى عدد صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:152]

```
153:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:153]

```
154:         return event.copy(
```
> يُعيد نسخة من event باستدعاء copy ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:154]

```
155:             tags = newTags,
```
> يعيّن الحقل tags إلى newTags في استدعاء copy. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:155]

```
156:             createdAt = updatedCreatedAt
```
> يعيّن الحقل createdAt إلى updatedCreatedAt في استدعاء copy. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:156]

```
157:         )
```
> إغلاق قائمة معاملات استدعاء copy. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:157]

```
158:     }
```
> إغلاق نطاق دالة addNonceTag. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:158]

```
159:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:159]

```
160:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:160]

```
161:      * Get the committed difficulty from an event's nonce tag
```
> تعليق: احصل على الصعوبة الملتزَم بها من وسم nonce للحدث. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:161]

```
162:      * @param event The event to check
```
> تعليق: المعامل event هو الحدث المراد فحصه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:162]

```
163:      * @return The committed difficulty, or null if not present
```
> تعليق: تُعيد الصعوبة الملتزَم بها، أو null إن لم تكن حاضرة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:163]

```
164:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:164]

```
165:     private fun getCommittedDifficulty(event: NostrEvent): Int? {
```
> يعرّف دالة خاصة باسم احصل على الصعوبة الملتزَم بها (getCommittedDifficulty) تأخذ event من نوع NostrEvent وتُعيد عدداً صحيحاً اختيارياً، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:165]

```
166:         val nonceTag = event.tags.find { tag -> 
```
> يعرّف قيمة ثابتة باسم nonceTag تُسند إليها نتيجة استدعاء find على event.tags بدالة على المتغيّر tag، ويفتح نطاق الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:166]

```
167:             tag.isNotEmpty() && tag[0] == "nonce" && tag.size >= 3 
```
> شرط البحث: الوسم tag غير فارغ وعنصره الأول يساوي "nonce" وحجمه أكبر من أو يساوي ٣. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:167]

```
168:         }
```
> إغلاق نطاق دالة find. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:168]

```
169:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:169]

```
170:         return nonceTag?.get(2)?.toIntOrNull()
```
> يُعيد العنصر عند الفهرس ٢ من nonceTag (إن لم يكن null) محوّلاً إلى عدد صحيح أو null. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:170]

```
171:     }
```
> إغلاق نطاق دالة getCommittedDifficulty. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:171]

```
172:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:172]

```
173:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:173]

```
174:      * Check if an event has a nonce tag (indicating it was mined)
```
> تعليق: افحص ما إذا كان للحدث وسم nonce (دلالة على أنه عُدّن). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:174]

```
175:      * @param event The event to check
```
> تعليق: المعامل event هو الحدث المراد فحصه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:175]

```
176:      * @return true if the event has a nonce tag
```
> تعليق: تُعيد true إن كان للحدث وسم nonce. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:176]

```
177:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:177]

```
178:     fun hasNonce(event: NostrEvent): Boolean {
```
> يعرّف دالة باسم لديه nonce (hasNonce) تأخذ event من نوع NostrEvent وتُعيد قيمة منطقية، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:178]

```
179:         return event.tags.any { tag -> tag.isNotEmpty() && tag[0] == "nonce" }
```
> يُعيد نتيجة استدعاء any على event.tags الذي يتحقّق إن وُجد وسم tag غير فارغ وعنصره الأول يساوي "nonce". [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:179]

```
180:     }
```
> إغلاق نطاق دالة hasNonce. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:180]

```
181:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:181]

```
182:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:182]

```
183:      * Get the nonce value from an event
```
> تعليق: احصل على قيمة nonce من حدث. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:183]

```
184:      * @param event The event to check
```
> تعليق: المعامل event هو الحدث المراد فحصه. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:184]

```
185:      * @return The nonce value, or null if not present
```
> تعليق: تُعيد قيمة nonce، أو null إن لم تكن حاضرة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:185]

```
186:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:186]

```
187:     fun getNonce(event: NostrEvent): String? {
```
> يعرّف دالة باسم احصل على nonce (getNonce) تأخذ event من نوع NostrEvent وتُعيد سلسلة نصية اختيارية، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:187]

```
188:         val nonceTag = event.tags.find { tag -> 
```
> يعرّف قيمة ثابتة باسم nonceTag تُسند إليها نتيجة استدعاء find على event.tags بدالة على المتغيّر tag، ويفتح نطاق الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:188]

```
189:             tag.isNotEmpty() && tag[0] == "nonce" && tag.size >= 2 
```
> شرط البحث: الوسم tag غير فارغ وعنصره الأول يساوي "nonce" وحجمه أكبر من أو يساوي ٢. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:189]

```
190:         }
```
> إغلاق نطاق دالة find. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:190]

```
191:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:191]

```
192:         return nonceTag?.get(1)
```
> يُعيد العنصر عند الفهرس ١ من nonceTag (إن لم يكن null). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:192]

```
193:     }
```
> إغلاق نطاق دالة getNonce. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:193]

```
194:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:194]

```
195:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:195]

```
196:      * Estimate the computational work required for a given difficulty
```
> تعليق: قدّر العمل الحسابي المطلوب لصعوبة معيّنة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:196]

```
197:      * @param difficulty The target difficulty
```
> تعليق: المعامل difficulty هو الصعوبة المستهدفة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:197]

```
198:      * @return Estimated number of hash operations required
```
> تعليق: تُعيد العدد المقدَّر لعمليات التجزئة (hash) المطلوبة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:198]

```
199:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:199]

```
200:     fun estimateWork(difficulty: Int): Long {
```
> يعرّف دالة باسم قدّر العمل (estimateWork) تأخذ difficulty من نوع عدد صحيح وتُعيد عدداً طويلاً (Long)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:200]
