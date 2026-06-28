# شريحة — app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt (الأسطر 1–138)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) المسماة com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف Log من android.util ليُستعمل لطباعة السجلّات (logging). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:3]

```
4: import com.bitchat.android.model.RoutedPacket
```
> يستورد الصنف RoutedPacket (الحزمة الموجَّهة) من com.bitchat.android.model. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:4]

```
5: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف BitchatPacket (حزمة بِت‌شات) من com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:5]

```
6: import com.bitchat.android.protocol.MessageType
```
> يستورد الصنف MessageType (نوع الرسالة) من com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:6]

```
7: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف CoroutineScope (نطاق الكوروتين) من kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:7]

```
8: import kotlinx.coroutines.CoroutineStart
```
> يستورد الصنف CoroutineStart (بدء الكوروتين) من kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:8]

```
9: import kotlinx.coroutines.Job
```
> يستورد الصنف Job (المهمّة) من kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:9]

```
10: import kotlinx.coroutines.delay
```
> يستورد الدالة delay (التأخير) من kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:10]

```
11: import kotlinx.coroutines.isActive
```
> يستورد الخاصية isActive (هل نشط) من kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:11]

```
12: import kotlinx.coroutines.launch
```
> يستورد الدالة launch (الإطلاق) من kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:12]

```
13: import java.security.MessageDigest
```
> يستورد الصنف MessageDigest (هاضم الرسالة) من java.security. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:13]

```
14: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف ConcurrentHashMap (خريطة هاش متزامنة) من java.util.concurrent. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:14]

```
15: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:15]

```
16: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:16]

```
17:  * Shared transport send wrapper that applies bitchat packet fragmentation and
```
> تعليق: غلاف إرسال نقلٍ مشترك يطبّق تجزئة حزمة بِت‌شات و. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:17]

```
18:  * transfer progress before a transport writes packets to its concrete medium.
```
> تعليق: تقدّمَ النقل قبل أن يكتب ناقلٌ الحزمَ إلى وسيطه الفعلي. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:18]

```
19:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:19]

```
20: class FragmentingPacketSender(
```
> يعرّف الصنف FragmentingPacketSender (مُرسِل الحزم المُجزِّئ) مع بداية قائمة معاملات المُنشئ (constructor). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:20]

```
21:     private val scope: CoroutineScope,
```
> يعرّف معاملاً خاصاً للقراءة فقط اسمه scope (النطاق) من نوع CoroutineScope. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:21]

```
22:     private val fragmentManager: FragmentManager?,
```
> يعرّف معاملاً خاصاً للقراءة فقط اسمه fragmentManager (مدير التجزئة) من نوع FragmentManager قابل لأن يكون فارغاً (nullable). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:22]

```
23:     private val logTag: String,
```
> يعرّف معاملاً خاصاً للقراءة فقط اسمه logTag (وسم السجلّ) من نوع String. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:23]

```
24:     private val interFragmentDelayMs: Long = 20L
```
> يعرّف معاملاً خاصاً للقراءة فقط اسمه interFragmentDelayMs (التأخير بين الأجزاء بالمللي ثانية) من نوع Long بقيمة افتراضية 20L. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:24]

```
25: ) {
```
> إغلاق قائمة معاملات المُنشئ وفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:25]

```
26:     private val transferJobs = ConcurrentHashMap<String, Job>()
```
> يعرّف خاصية خاصة للقراءة فقط اسمها transferJobs (مهمّات النقل) ويهيّئها بخريطة هاش متزامنة فارغة مفاتيحها String وقيمها Job. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:27]

```
28:     fun send(
```
> يعرّف الدالة send (أرسِل) مع بداية قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:28]

```
29:         routed: RoutedPacket,
```
> يعرّف المعامل routed (الموجَّه) من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:29]

```
30:         description: String,
```
> يعرّف المعامل description (الوصف) من نوع String. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:30]

```
31:         sendSingle: (RoutedPacket) -> Boolean
```
> يعرّف المعامل sendSingle (أرسِل واحدة) وهو دالة تأخذ RoutedPacket وتعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:31]

```
32:     ): Boolean {
```
> يُغلق قائمة المعاملات ويُصرّح أن الدالة send تعيد Boolean ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:32]

```
33:         val transferId = transferIdFor(routed)
```
> يعرّف متغيّراً للقراءة فقط اسمه transferId (مُعرّف النقل) ويُسنِد إليه ناتج استدعاء transferIdFor مع routed. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:33]

```
34:         val packets = packetsForTransport(routed.packet) ?: return false
```
> يعرّف متغيّراً للقراءة فقط اسمه packets (الحزم) ويُسنِد إليه ناتج packetsForTransport على routed.packet، وإن كان الناتج فارغاً (null) تعيد الدالة false. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:34]

```
35:         val total = packets.size
```
> يعرّف متغيّراً للقراءة فقط اسمه total (الإجمالي) ويُسنِد إليه حجم القائمة packets. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:36]

```
37:         if (total <= 1) {
```
> يبدأ شرطاً إذا كان total أصغر من أو يساوي 1. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:37]

```
38:             if (transferId != null) {
```
> يبدأ شرطاً داخلياً إذا كان transferId لا يساوي null. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:38]

```
39:                 TransferProgressManager.start(transferId, 1)
```
> يستدعي الدالة start من TransferProgressManager (مدير تقدّم النقل) مع transferId والعدد 1. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:39]

```
40:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:40]

```
41:             val sent = sendSingle(routed.copy(packet = packets.first(), transferId = transferId))
```
> يعرّف متغيّراً للقراءة فقط اسمه sent (أُرسِلت) ويُسنِد إليه ناتج استدعاء sendSingle على نسخة من routed عُدِّل فيها packet إلى أول عنصر من packets و transferId إلى transferId. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:41]

```
42:             if (sent && transferId != null) {
```
> يبدأ شرطاً إذا كان sent صحيحاً و transferId لا يساوي null. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:42]

```
43:                 TransferProgressManager.progress(transferId, 1, 1)
```
> يستدعي الدالة progress من TransferProgressManager مع transferId والقيمتين 1 و 1. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:43]

```
44:                 TransferProgressManager.complete(transferId, 1)
```
> يستدعي الدالة complete من TransferProgressManager مع transferId والعدد 1. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:44]

```
45:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:45]

```
46:             return sent
```
> تعيد الدالة قيمة sent. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:46]

```
47:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:47]

```
48: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:48]

```
49:         Log.d(logTag, "Fragmenting packet type ${routed.packet.type} into $total fragments for $description")
```
> يستدعي Log.d (سجلّ تصحيح) مع logTag ونصٍّ يقول إنه يُجزّئ نوع الحزمة routed.packet.type إلى total أجزاء من أجل description. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:49]

```
50:         if (transferId != null) {
```
> يبدأ شرطاً إذا كان transferId لا يساوي null. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:50]

```
51:             TransferProgressManager.start(transferId, total)
```
> يستدعي الدالة start من TransferProgressManager مع transferId و total. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:51]

```
52:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:52]

```
53: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:53]

```
54:         val job = scope.launch(start = CoroutineStart.LAZY) {
```
> يعرّف متغيّراً للقراءة فقط اسمه job (المهمّة) ويُسنِد إليه ناتج scope.launch ببدء كسول CoroutineStart.LAZY مع فتح كتلة الكوروتين. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:54]

```
55:             var sent = 0
```
> يعرّف متغيّراً قابلاً للتغيير اسمه sent ويهيّئه بالقيمة 0. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:55]

```
56:             for (packet in packets) {
```
> يبدأ حلقة تكرارية تمرّ على كل packet ضمن packets. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:56]

```
57:                 if (!isActive) return@launch
```
> إذا كان isActive غير صحيح (الكوروتين غير نشط) يخرج من كتلة launch. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:57]

```
58:                 if (transferId != null && transferJobs[transferId]?.isCancelled == true) return@launch
```
> إذا كان transferId لا يساوي null وكانت المهمّة المخزّنة في transferJobs تحت transferId ذات isCancelled يساوي true، يخرج من كتلة launch. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:58]

```
59: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:59]

```
60:                 val fragment = routed.copy(packet = packet, transferId = transferId)
```
> يعرّف متغيّراً للقراءة فقط اسمه fragment (الجزء) ويُسنِد إليه نسخة من routed عُدِّل فيها packet إلى packet و transferId إلى transferId. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:60]

```
61:                 val delivered = try {
```
> يعرّف متغيّراً للقراءة فقط اسمه delivered (سُلِّمت) ويُسنِد إليه ناتج كتلة try. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:61]

```
62:                     sendSingle(fragment)
```
> يستدعي sendSingle مع fragment ويكون ناتجه قيمة كتلة try. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:62]

```
63:                 } catch (e: Exception) {
```
> يبدأ كتلة catch تلتقط استثناءً (Exception) باسم e. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:63]

```
64:                     Log.e(logTag, "Fragment send failed for $description: ${e.message}", e)
```
> يستدعي Log.e (سجلّ خطأ) مع logTag ونصٍّ يقول إن إرسال الجزء فشل من أجل description مع رسالة الاستثناء e.message والاستثناء e. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:64]

```
65:                     false
```
> يجعل قيمة كتلة catch هي false. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:65]

```
66:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:66]

```
67: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:67]

```
68:                 if (!delivered) {
```
> يبدأ شرطاً إذا كان delivered غير صحيح. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:68]

```
69:                     Log.w(logTag, "Stopping fragmented send for $description after $sent/$total fragments")
```
> يستدعي Log.w (سجلّ تحذير) مع logTag ونصٍّ يقول إنه يوقف الإرسال المُجزّأ من أجل description بعد sent من أصل total أجزاء. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:69]

```
70:                     return@launch
```
> يخرج من كتلة launch. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:70]

```
71:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:71]

```
72: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:72]

```
73:                 sent += 1
```
> يزيد قيمة sent بمقدار 1. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:73]

```
74:                 if (transferId != null) {
```
> يبدأ شرطاً إذا كان transferId لا يساوي null. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:74]

```
75:                     TransferProgressManager.progress(transferId, sent, total)
```
> يستدعي الدالة progress من TransferProgressManager مع transferId و sent و total. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:75]

```
76:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:76]

```
77:                 if (sent < total) {
```
> يبدأ شرطاً إذا كان sent أصغر من total. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:77]

```
78:                     delay(interFragmentDelayMs)
```
> يستدعي الدالة delay بمقدار interFragmentDelayMs. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:78]

```
79:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:79]

```
80:             }
```
> إغلاق نطاق (نهاية حلقة for). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:80]

```
81: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:81]

```
82:             if (transferId != null) {
```
> يبدأ شرطاً إذا كان transferId لا يساوي null. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:82]

```
83:                 TransferProgressManager.complete(transferId, total)
```
> يستدعي الدالة complete من TransferProgressManager مع transferId و total. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:83]

```
84:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:84]

```
85:         }
```
> إغلاق نطاق (نهاية كتلة launch). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:85]

```
86: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:86]

```
87:         if (transferId != null) {
```
> يبدأ شرطاً إذا كان transferId لا يساوي null. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:87]

```
88:             transferJobs[transferId] = job
```
> يُسنِد job إلى المدخل transferId في الخريطة transferJobs. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:88]

```
89:             job.invokeOnCompletion { transferJobs.remove(transferId, job) }
```
> يستدعي job.invokeOnCompletion (نَفِّذ عند الاكتمال) ليُزيل من transferJobs المدخل transferId المقترن بـ job. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:89]

```
90:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:90]

```
91:         job.start()
```
> يستدعي job.start (ابدأ المهمّة). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:91]

```
92:         return true
```
> تعيد الدالة القيمة true. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:92]

```
93:     }
```
> إغلاق نطاق (نهاية الدالة send). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:93]

```
94: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:94]

```
95:     fun cancelTransfer(transferId: String): Boolean {
```
> يعرّف الدالة cancelTransfer (ألغِ النقل) التي تأخذ transferId من نوع String وتعيد Boolean ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:95]

```
96:         val job = transferJobs.remove(transferId) ?: return false
```
> يعرّف متغيّراً للقراءة فقط اسمه job ويُسنِد إليه ناتج إزالة المدخل transferId من transferJobs، وإن كان الناتج null تعيد الدالة false. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:96]

```
97:         job.cancel()
```
> يستدعي job.cancel (ألغِ المهمّة). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:97]

```
98:         return true
```
> تعيد الدالة القيمة true. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:98]

```
99:     }
```
> إغلاق نطاق (نهاية الدالة cancelTransfer). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:99]

```
100: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:100]

```
101:     private fun packetsForTransport(packet: BitchatPacket): List<BitchatPacket>? {
```
> يعرّف دالة خاصة اسمها packetsForTransport (حزم النقل) تأخذ packet من نوع BitchatPacket وتعيد قائمة List<BitchatPacket> قابلة لأن تكون null ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:101]

```
102:         if (packet.type == MessageType.FRAGMENT.value) {
```
> يبدأ شرطاً إذا كان packet.type يساوي MessageType.FRAGMENT.value (قيمة نوع الجزء). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:102]

```
103:             return listOf(packet)
```
> تعيد الدالة قائمة تحتوي على packet وحده. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:103]

```
104:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:104]

```
105: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:105]

```
106:         val manager = fragmentManager ?: return listOf(packet)
```
> يعرّف متغيّراً للقراءة فقط اسمه manager (المدير) ويُسنِد إليه fragmentManager، وإن كان null تعيد الدالة قائمة تحتوي على packet وحده. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:106]

```
107:         return try {
```
> تعيد الدالة قيمة كتلة try التي تبدأ هنا. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:107]

```
108:             val fragments = manager.createFragments(packet)
```
> يعرّف متغيّراً للقراءة فقط اسمه fragments (الأجزاء) ويُسنِد إليه ناتج استدعاء manager.createFragments على packet. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:108]

```
109:             if (fragments.isEmpty()) {
```
> يبدأ شرطاً إذا كانت fragments فارغة. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:109]

```
110:                 Log.e(logTag, "Fragment manager returned no packets for packet type ${packet.type}")
```
> يستدعي Log.e مع logTag ونصٍّ يقول إن مدير التجزئة لم يُعِد أي حزم لنوع الحزمة packet.type. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:110]

```
111:                 null
```
> يجعل قيمة هذا الفرع null. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:111]

```
112:             } else {
```
> يبدأ الفرع else. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:112]

```
113:                 fragments
```
> يجعل قيمة فرع else هي fragments. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:113]

```
114:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:114]

```
115:         } catch (e: Exception) {
```
> يبدأ كتلة catch تلتقط استثناءً Exception باسم e. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:115]

```
116:             Log.e(logTag, "Fragment creation failed for packet type ${packet.type}: ${e.message}", e)
```
> يستدعي Log.e مع logTag ونصٍّ يقول إن إنشاء الأجزاء فشل لنوع الحزمة packet.type مع رسالة الاستثناء e.message والاستثناء e. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:116]

```
117:             null
```
> يجعل قيمة كتلة catch هي null. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:117]

```
118:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:118]

```
119:     }
```
> إغلاق نطاق (نهاية الدالة packetsForTransport). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:119]

```
120: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:120]

```
121:     private fun transferIdFor(routed: RoutedPacket): String? {
```
> يعرّف دالة خاصة اسمها transferIdFor (مُعرّف النقل لِـ) تأخذ routed من نوع RoutedPacket وتعيد String قابلاً لأن يكون null ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:121]

```
122:         routed.transferId?.let { return it }
```
> إذا كان routed.transferId لا يساوي null، تعيد الدالة تلك القيمة. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:122]

```
123:         val packet = routed.packet
```
> يعرّف متغيّراً للقراءة فقط اسمه packet ويُسنِد إليه routed.packet. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:123]

```
124:         return if (packet.type == MessageType.FILE_TRANSFER.value) {
```
> تعيد الدالة ناتج تعبير شرطي if؛ شرطه أن packet.type يساوي MessageType.FILE_TRANSFER.value (قيمة نوع نقل الملف). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:124]

```
125:             sha256Hex(packet.payload)
```
> يجعل قيمة فرع الشرط الصحيح هي ناتج sha256Hex على packet.payload (الحمولة). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:125]

```
126:         } else {
```
> يبدأ الفرع else. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:126]

```
127:             null
```
> يجعل قيمة فرع else هي null. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:127]

```
128:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:128]

```
129:     }
```
> إغلاق نطاق (نهاية الدالة transferIdFor). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:129]

```
130: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:130]

```
131:     private fun sha256Hex(bytes: ByteArray): String = try {
```
> يعرّف دالة خاصة اسمها sha256Hex (سها٢٥٦ ست عشري) تأخذ bytes من نوع ByteArray وتعيد String، وقيمتها هي ناتج كتلة try التي تبدأ هنا. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:131]

```
132:         val md = MessageDigest.getInstance("SHA-256")
```
> يعرّف متغيّراً للقراءة فقط اسمه md ويُسنِد إليه نسخة MessageDigest عبر getInstance بالخوارزمية "SHA-256". [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:132]

```
133:         md.update(bytes)
```
> يستدعي md.update مع bytes. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:133]

```
134:         md.digest().joinToString("") { "%02x".format(it) }
```
> يستدعي md.digest() ثم يجمع بايتاته في نصٍّ بلا فاصل، حيث يُصاغ كل بايت it بالنمط الست عشري "%02x". [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:134]

```
135:     } catch (_: Exception) {
```
> يبدأ كتلة catch تلتقط استثناءً Exception دون تسميته. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:135]

```
136:         bytes.size.toString(16)
```
> يجعل قيمة كتلة catch هي حجم bytes محوَّلاً إلى نصٍّ بالأساس 16. [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:136]

```
137:     }
```
> إغلاق نطاق (نهاية كتلة try/catch ونهاية الدالة sha256Hex). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:137]

```
138: }
```
> إغلاق نطاق (نهاية الصنف FragmentingPacketSender). [app/src/main/java/com/bitchat/android/mesh/FragmentingPacketSender.kt:138]
