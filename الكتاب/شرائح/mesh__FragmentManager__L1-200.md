# شريحة — app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) ‏`com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف ‏`Log` من ‏`android.util`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:3]

```
4: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف ‏`BitchatPacket` (حزمة بِت‑تشات) من ‏`com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:4]

```
5: import com.bitchat.android.protocol.MessageType
```
> يستورد الصنف ‏`MessageType` (نوع الرسالة) من ‏`com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:5]

```
6: import com.bitchat.android.protocol.MessagePadding
```
> يستورد الصنف ‏`MessagePadding` (حشو الرسالة) من ‏`com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:6]

```
7: import com.bitchat.android.model.FragmentPayload
```
> يستورد الصنف ‏`FragmentPayload` (حمولة الشظية) من ‏`com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:7]

```
8: import kotlinx.coroutines.*
```
> يستورد كل أعضاء ‏`kotlinx.coroutines` (الكوروتينات). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:8]

```
9: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف ‏`ConcurrentHashMap` (خريطة تجزئة متزامنة) من ‏`java.util.concurrent`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:9]

```
10: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:10]

```
11: /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:11]

```
12:  * Manages message fragmentation and reassembly - 100% iOS Compatible
```
> تعليق: «يدير تشظية الرسالة وإعادة تجميعها - متوافق ١٠٠٪ مع iOS». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:12]

```
13:  * 
```
> تعليق: سطر تعليقي فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:13]

```
14:  * This implementation exactly matches iOS SimplifiedBluetoothService fragmentation:
```
> تعليق: «هذا التنفيذ يطابق تماماً تشظية ‏SimplifiedBluetoothService في iOS:». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:14]

```
15:  * - Same fragment payload structure (13-byte header + data)
```
> تعليق: «- نفس بنية حمولة الشظية (ترويسة ١٣ بايت + بيانات)». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:15]

```
16:  * - Same MTU thresholds and fragment sizes
```
> تعليق: «- نفس عتبات ‏MTU وأحجام الشظايا». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:16]

```
17:  * - Same reassembly logic and timeout handling
```
> تعليق: «- نفس منطق إعادة التجميع ومعالجة المهلة». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:17]

```
18:  * - Uses new FragmentPayload model for type safety
```
> تعليق: «- يستعمل نموذج ‏FragmentPayload الجديد لأمان الأنواع». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:18]

```
19:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:19]

```
20: class FragmentManager {
```
> يعرّف الصنف ‏`FragmentManager` (مدير الشظايا) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:20]

```
21:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:21]

```
22:     companion object {
```
> يعرّف كائناً مرافقاً (companion object) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:22]

```
23:         private const val TAG = "FragmentManager"
```
> يعرّف ثابتاً خاصاً ‏`TAG` (وسم السجل) ويضبط قيمته إلى السلسلة ‏`"FragmentManager"`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:23]

```
24:         // iOS values: 512 MTU threshold, 469 max fragment size (512 MTU - headers)
```
> تعليق: «قيم iOS: عتبة ‏MTU ‏512، أقصى حجم شظية ‏469 (512 ‏MTU - الترويسات)». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:24]

```
25:         private const val FRAGMENT_SIZE_THRESHOLD = com.bitchat.android.util.AppConstants.Fragmentation.FRAGMENT_SIZE_THRESHOLD // Matches iOS: if data.count > 512
```
> يعرّف ثابتاً خاصاً ‏`FRAGMENT_SIZE_THRESHOLD` (عتبة حجم الشظية) ويضبط قيمته إلى ‏`AppConstants.Fragmentation.FRAGMENT_SIZE_THRESHOLD`، مع تعليق: «يطابق iOS: ‏if data.count > 512». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:25]

```
26:         private const val MAX_FRAGMENT_SIZE = com.bitchat.android.util.AppConstants.Fragmentation.MAX_FRAGMENT_SIZE        // Matches iOS: maxFragmentSize = 469 
```
> يعرّف ثابتاً خاصاً ‏`MAX_FRAGMENT_SIZE` (أقصى حجم شظية) ويضبط قيمته إلى ‏`AppConstants.Fragmentation.MAX_FRAGMENT_SIZE`، مع تعليق: «يطابق iOS: ‏maxFragmentSize = 469». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:26]

```
27:         private const val FRAGMENT_TIMEOUT = com.bitchat.android.util.AppConstants.Fragmentation.FRAGMENT_TIMEOUT_MS     // Matches iOS: 30 seconds cleanup
```
> يعرّف ثابتاً خاصاً ‏`FRAGMENT_TIMEOUT` (مهلة الشظية) ويضبط قيمته إلى ‏`AppConstants.Fragmentation.FRAGMENT_TIMEOUT_MS`، مع تعليق: «يطابق iOS: تنظيف بعد ٣٠ ثانية». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:27]

```
28:         private const val CLEANUP_INTERVAL = com.bitchat.android.util.AppConstants.Fragmentation.CLEANUP_INTERVAL_MS     // 10 seconds cleanup check
```
> يعرّف ثابتاً خاصاً ‏`CLEANUP_INTERVAL` (فترة التنظيف) ويضبط قيمته إلى ‏`AppConstants.Fragmentation.CLEANUP_INTERVAL_MS`، مع تعليق: «فحص تنظيف كل ١٠ ثوانٍ». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:28]

```
29:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:29]

```
30:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:30]

```
31:     // Fragment storage - iOS equivalent: incomingFragments: [String: [Int: Data]]
```
> تعليق: «تخزين الشظايا - مكافئ iOS: ‏incomingFragments: [String: [Int: Data]]». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:31]

```
32:     private val incomingFragments = ConcurrentHashMap<String, MutableMap<Int, ByteArray>>()
```
> يعرّف حقلاً خاصاً ‏`incomingFragments` (الشظايا الواردة) ويضبطه إلى ‏`ConcurrentHashMap` جديدة مفتاحها ‏`String` وقيمتها خريطة قابلة للتعديل من ‏`Int` إلى ‏`ByteArray`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:32]

```
33:     // iOS equivalent: fragmentMetadata: [String: (type: UInt8, total: Int, timestamp: Date)]
```
> تعليق: «مكافئ iOS: ‏fragmentMetadata: [String: (type: UInt8, total: Int, timestamp: Date)]». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:33]

```
34:     private val fragmentMetadata = ConcurrentHashMap<String, Triple<UByte, Int, Long>>() // originalType, totalFragments, timestamp
```
> يعرّف حقلاً خاصاً ‏`fragmentMetadata` (بيانات وصف الشظية) ويضبطه إلى ‏`ConcurrentHashMap` جديدة مفتاحها ‏`String` وقيمتها ثلاثية ‏`Triple` من ‏`UByte` و‏`Int` و‏`Long`، مع تعليق: «النوع الأصلي، إجمالي الشظايا، الطابع الزمني». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:34]

```
35:     private val fragmentCumulativeSize = ConcurrentHashMap<String, Int>()
```
> يعرّف حقلاً خاصاً ‏`fragmentCumulativeSize` (الحجم التراكمي للشظايا) ويضبطه إلى ‏`ConcurrentHashMap` جديدة مفتاحها ‏`String` وقيمتها ‏`Int`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:36]

```
37:     private val fragmentStateLock = Any()
```
> يعرّف حقلاً خاصاً ‏`fragmentStateLock` (قفل حالة الشظايا) ويضبطه إلى كائن ‏`Any()` جديد. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:37]

```
38:     private var globalBufferedBytes: Long = 0L
```
> يعرّف متغيراً خاصاً ‏`globalBufferedBytes` (البايتات المخزّنة عالمياً) من نوع ‏`Long` ويضبطه إلى ‏`0L`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:38]

```
39: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:39]

```
40:     // Delegate for callbacks
```
> تعليق: «مفوّض لردود النداء». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:40]

```
41:     var delegate: FragmentManagerDelegate? = null
```
> يعرّف متغيراً ‏`delegate` (المفوّض) من نوع ‏`FragmentManagerDelegate?` القابل لأن يكون فارغاً ويضبطه إلى ‏`null`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:41]

```
42:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:42]

```
43:     // Coroutines
```
> تعليق: «الكوروتينات». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:43]

```
44:     private val managerScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يعرّف حقلاً خاصاً ‏`managerScope` (نطاق المدير) ويضبطه إلى ‏`CoroutineScope` مكوّن من ‏`Dispatchers.IO` مجموعاً مع ‏`SupervisorJob()`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:44]

```
45:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:45]

```
46:     init {
```
> يفتح كتلة التهيئة (init). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:46]

```
47:         startPeriodicCleanup()
```
> يستدعي الدالة ‏`startPeriodicCleanup()` (بدء التنظيف الدوري). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:47]

```
48:     }
```
> إغلاق نطاق كتلة التهيئة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:48]

```
49:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:49]

```
50:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:50]

```
51:      * Create fragments from a large packet - 100% iOS Compatible
```
> تعليق: «أنشئ شظايا من حزمة كبيرة - متوافق ١٠٠٪ مع iOS». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:51]

```
52:      * Matches iOS sendFragmentedPacket() implementation exactly
```
> تعليق: «يطابق تماماً تنفيذ ‏sendFragmentedPacket() في iOS». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:52]

```
53:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:53]

```
54:     fun createFragments(packet: BitchatPacket): List<BitchatPacket> {
```
> يعرّف الدالة ‏`createFragments` (إنشاء الشظايا) تأخذ معامل ‏`packet` من نوع ‏`BitchatPacket` وتعيد ‏`List<BitchatPacket>`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:54]

```
55:         try {
```
> يفتح كتلة ‏`try`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:55]

```
56:             Log.d(TAG, "🔀 Creating fragments for packet type ${packet.type}, payload: ${packet.payload.size} bytes")
```
> يستدعي ‏`Log.d` مع الوسم ‏`TAG` ورسالة تصف نوع الحزمة ‏`packet.type` وحجم حمولتها ‏`packet.payload.size` بالبايت. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:56]

```
57:         val encoded = packet.toBinaryData()
```
> يعرّف متغيراً ‏`encoded` (المرمّز) ويضبطه إلى ناتج استدعاء ‏`packet.toBinaryData()`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:57]

```
58:             if (encoded == null) {
```
> يفتح شرطاً يفحص ما إذا كان ‏`encoded` مساوياً ‏`null`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:58]

```
59:                 Log.e(TAG, "❌ Failed to encode packet to binary data")
```
> يستدعي ‏`Log.e` مع الوسم ‏`TAG` والرسالة «فشل ترميز الحزمة إلى بيانات ثنائية». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:59]

```
60:                 return emptyList()
```
> يعيد قائمة فارغة عبر ‏`emptyList()`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:60]

```
61:             }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:61]

```
62:             Log.d(TAG, "📦 Encoded to ${encoded.size} bytes")
```
> يستدعي ‏`Log.d` مع الوسم ‏`TAG` ورسالة تذكر أن الترميز نتج عنه ‏`encoded.size` بايت. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:62]

```
63:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:63]

```
64:         // Fragment the unpadded frame; each fragment will be encoded (and padded) independently - iOS fix
```
> تعليق: «شظِّ الإطار غير المحشو؛ كل شظية ستُرمَّز (وتُحشى) باستقلال - تصحيح iOS». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:64]

```
65:         val fullData = try {
```
> يعرّف متغيراً ‏`fullData` (البيانات الكاملة) ويبدأ إسناده من نتيجة كتلة ‏`try`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:65]

```
66:                 MessagePadding.unpad(encoded)
```
> يستدعي ‏`MessagePadding.unpad(encoded)` لإزالة الحشو، وتُستعمل نتيجته قيمةً للكتلة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:66]

```
67:             } catch (e: Exception) {
```
> يلتقط استثناءً ‏`Exception` في المتغير ‏`e` ويفتح نطاق المعالجة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:67]

```
68:                 Log.e(TAG, "❌ Failed to unpad data: ${e.message}", e)
```
> يستدعي ‏`Log.e` مع الوسم ‏`TAG` ورسالة «فشل إزالة حشو البيانات» متبوعةً برسالة الاستثناء ‏`e.message` والاستثناء ‏`e`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:68]

```
69:                 return emptyList()
```
> يعيد قائمة فارغة عبر ‏`emptyList()`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:69]

```
70:             }
```
> إغلاق نطاق كتلة ‏`try/catch` لإسناد ‏`fullData`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:70]

```
71:             Log.d(TAG, "📏 Unpadded to ${fullData.size} bytes")
```
> يستدعي ‏`Log.d` مع الوسم ‏`TAG` ورسالة تذكر أن إزالة الحشو نتج عنها ‏`fullData.size` بايت. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:71]

```
72:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:72]

```
73:         // iOS logic: if data.count > 512 && packet.type != MessageType.fragment.rawValue
```
> تعليق: «منطق iOS: ‏if data.count > 512 && packet.type != MessageType.fragment.rawValue». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:73]

```
74:         if (fullData.size <= FRAGMENT_SIZE_THRESHOLD) {
```
> يفتح شرطاً يفحص ما إذا كان ‏`fullData.size` أصغر من أو يساوي ‏`FRAGMENT_SIZE_THRESHOLD`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:74]

```
75:             return listOf(packet) // No fragmentation needed
```
> يعيد قائمة تحتوي ‏`packet` وحده عبر ‏`listOf(packet)`، مع تعليق: «لا حاجة للتشظية». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:75]

```
76:         }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:76]

```
77:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:77]

```
78:         val fragments = mutableListOf<BitchatPacket>()
```
> يعرّف متغيراً ‏`fragments` (الشظايا) ويضبطه إلى قائمة قابلة للتعديل فارغة من نوع ‏`BitchatPacket` عبر ‏`mutableListOf()`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:78]

```
79:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:79]

```
80:         // iOS: let fragmentID = Data((0..<8).map { _ in UInt8.random(in: 0...255) })
```
> تعليق: «iOS: ‏let fragmentID = Data((0..<8).map { _ in UInt8.random(in: 0...255) })». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:80]

```
81:         val fragmentID = FragmentPayload.generateFragmentID()
```
> يعرّف متغيراً ‏`fragmentID` (معرّف الشظية) ويضبطه إلى ناتج استدعاء ‏`FragmentPayload.generateFragmentID()`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:81]

```
82:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:82]

```
83:         // iOS: stride(from: 0, to: fullData.count, by: maxFragmentSize)
```
> تعليق: «iOS: ‏stride(from: 0, to: fullData.count, by: maxFragmentSize)». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:83]

```
84:         // Calculate dynamic fragment size to fit in MTU (512)
```
> تعليق: «احسب حجم شظية ديناميكي يلائم ‏MTU ‏(512)». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:84]

```
85:         // Packet = Header + Sender + Recipient + Route + FragmentHeader + Payload + PaddingBuffer
```
> تعليق: «الحزمة = ترويسة + مُرسِل + مُستقبِل + مسار + ترويسة شظية + حمولة + مخزن حشو». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:85]

```
86:         val hasRoute = packet.route != null
```
> يعرّف متغيراً ‏`hasRoute` (يملك مساراً) ويضبطه إلى نتيجة فحص ما إذا كان ‏`packet.route` غير مساوٍ ‏`null`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:86]

```
87:         val version = if (hasRoute) 2 else 1
```
> يعرّف متغيراً ‏`version` (الإصدار) ويضبطه إلى ‏2 إن كان ‏`hasRoute` صحيحاً وإلا ‏1. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:87]

```
88:         val headerSize = if (version == 2) 15 else 13
```
> يعرّف متغيراً ‏`headerSize` (حجم الترويسة) ويضبطه إلى ‏15 إن كان ‏`version` يساوي ‏2 وإلا ‏13. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:88]

```
89:         val senderSize = 8
```
> يعرّف متغيراً ‏`senderSize` (حجم المُرسِل) ويضبطه إلى ‏8. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:89]

```
90:         val recipientSize = if (packet.recipientID != null) 8 else 0
```
> يعرّف متغيراً ‏`recipientSize` (حجم المُستقبِل) ويضبطه إلى ‏8 إن كان ‏`packet.recipientID` غير ‏`null` وإلا ‏0. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:90]

```
91:         // Route: 1 byte count + 8 bytes per hop
```
> تعليق: «المسار: ١ بايت للعدد + ٨ بايتات لكل قفزة». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:91]

```
92:         val routeSize = if (hasRoute) (1 + (packet.route?.size ?: 0) * 8) else 0
```
> يعرّف متغيراً ‏`routeSize` (حجم المسار) ويضبطه إلى ‏(1 + حجم ‏`packet.route` أو ‏0 مضروباً في ‏8) إن كان ‏`hasRoute` صحيحاً وإلا ‏0. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:92]

```
93:         val fragmentHeaderSize = 13 // FragmentPayload header
```
> يعرّف متغيراً ‏`fragmentHeaderSize` (حجم ترويسة الشظية) ويضبطه إلى ‏13، مع تعليق: «ترويسة ‏FragmentPayload». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:93]

```
94:         val paddingBuffer = 16 // MessagePadding.optimalBlockSize adds 16 bytes overhead
```
> يعرّف متغيراً ‏`paddingBuffer` (مخزن الحشو) ويضبطه إلى ‏16، مع تعليق: «‏MessagePadding.optimalBlockSize يضيف ‏16 بايت عبئاً». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:94]

```
95: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:95]

```
96:         // 512 - Overhead
```
> تعليق: «512 - العبء». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:96]

```
97:         val packetOverhead = headerSize + senderSize + recipientSize + routeSize + fragmentHeaderSize + paddingBuffer
```
> يعرّف متغيراً ‏`packetOverhead` (عبء الحزمة) ويضبطه إلى مجموع ‏`headerSize` و‏`senderSize` و‏`recipientSize` و‏`routeSize` و‏`fragmentHeaderSize` و‏`paddingBuffer`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:97]

```
98:         val maxDataSize = (512 - packetOverhead).coerceAtMost(MAX_FRAGMENT_SIZE)
```
> يعرّف متغيراً ‏`maxDataSize` (أقصى حجم بيانات) ويضبطه إلى ناتج طرح ‏`packetOverhead` من ‏512 محدوداً علوياً بـ‏`MAX_FRAGMENT_SIZE` عبر ‏`coerceAtMost`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:98]

```
99:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:99]

```
100:         if (maxDataSize <= 0) {
```
> يفتح شرطاً يفحص ما إذا كان ‏`maxDataSize` أصغر من أو يساوي ‏0. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:100]

```
101:             Log.e(TAG, "❌ Calculated maxDataSize is non-positive ($maxDataSize). Route too large?")
```
> يستدعي ‏`Log.e` مع الوسم ‏`TAG` ورسالة «قيمة ‏maxDataSize المحسوبة غير موجبة ($maxDataSize). هل المسار كبير جداً؟». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:101]

```
102:             return emptyList()
```
> يعيد قائمة فارغة عبر ‏`emptyList()`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:102]

```
103:         }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:103]

```
104: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:104]

```
105:         Log.d(TAG, "📏 Dynamic fragment size: $maxDataSize (MAX: $MAX_FRAGMENT_SIZE, Overhead: $packetOverhead)")
```
> يستدعي ‏`Log.d` مع الوسم ‏`TAG` ورسالة تذكر «حجم الشظية الديناميكي: ‏$maxDataSize (الأقصى: ‏$MAX_FRAGMENT_SIZE، العبء: ‏$packetOverhead)». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:105]

```
106:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:106]

```
107:         val fragmentChunks = stride(0, fullData.size, maxDataSize) { offset ->
```
> يعرّف متغيراً ‏`fragmentChunks` (قطع الشظايا) ويضبطه إلى ناتج استدعاء الدالة ‏`stride` بالوسائط ‏0 و‏`fullData.size` و‏`maxDataSize` مع لامبدا تأخذ ‏`offset` (الإزاحة)، ويفتح جسم اللامبدا. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:107]

```
108:             val endOffset = minOf(offset + maxDataSize, fullData.size)
```
> يعرّف متغيراً ‏`endOffset` (إزاحة النهاية) ويضبطه إلى أصغر القيمتين ‏(offset + maxDataSize) و‏`fullData.size` عبر ‏`minOf`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:108]

```
109:             fullData.sliceArray(offset..<endOffset)
```
> يعيد من اللامبدا شريحة مصفوفة من ‏`fullData` في المدى ‏`offset` حتى ما قبل ‏`endOffset` عبر ‏`sliceArray`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:109]

```
110:         }
```
> إغلاق نطاق اللامبدا واستدعاء ‏`stride`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:110]

```
111:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:111]

```
112:         Log.d(TAG, "Creating ${fragmentChunks.size} fragments for ${fullData.size} byte packet (iOS compatible)")
```
> يستدعي ‏`Log.d` مع الوسم ‏`TAG` ورسالة تذكر إنشاء ‏`fragmentChunks.size` شظية لحزمة بحجم ‏`fullData.size` بايت (متوافق مع iOS). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:112]

```
113:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:113]

```
114:         // iOS: for (index, fragment) in fragments.enumerated()
```
> تعليق: «iOS: ‏for (index, fragment) in fragments.enumerated()». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:114]

```
115:         for (index in fragmentChunks.indices) {
```
> يفتح حلقة ‏`for` تكرّر المتغير ‏`index` على فهارس ‏`fragmentChunks.indices`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:115]

```
116:             val fragmentData = fragmentChunks[index]
```
> يعرّف متغيراً ‏`fragmentData` (بيانات الشظية) ويضبطه إلى العنصر ذي الفهرس ‏`index` من ‏`fragmentChunks`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:116]

```
117:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:117]

```
118:             // Create iOS-compatible fragment payload
```
> تعليق: «أنشئ حمولة شظية متوافقة مع iOS». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:118]

```
119:             val fragmentPayload = FragmentPayload(
```
> يعرّف متغيراً ‏`fragmentPayload` (حمولة الشظية) ويبدأ بناء كائن ‏`FragmentPayload` بفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:119]

```
120:                 fragmentID = fragmentID,
```
> يمرّر الوسيط المسمّى ‏`fragmentID` بالقيمة ‏`fragmentID`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:120]

```
121:                 index = index,
```
> يمرّر الوسيط المسمّى ‏`index` بالقيمة ‏`index`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:121]

```
122:                 total = fragmentChunks.size,
```
> يمرّر الوسيط المسمّى ‏`total` بالقيمة ‏`fragmentChunks.size`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:122]

```
123:                 originalType = packet.type,
```
> يمرّر الوسيط المسمّى ‏`originalType` بالقيمة ‏`packet.type`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:123]

```
124:                 data = fragmentData
```
> يمرّر الوسيط المسمّى ‏`data` بالقيمة ‏`fragmentData`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:124]

```
125:             )
```
> إغلاق قائمة وسائط بناء ‏`FragmentPayload`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:125]

```
126:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:126]

```
127:             // iOS: MessageType.fragment.rawValue (single fragment type)
```
> تعليق: «iOS: ‏MessageType.fragment.rawValue (نوع شظية واحد)». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:127]

```
128:             // Fix: Fragments must inherit source route and use v2 if routed
```
> تعليق: «تصحيح: يجب أن ترث الشظايا مسار المصدر وتستعمل الإصدار ‏v2 إن كانت موجّهة». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:128]

```
129:             val fragmentPacket = BitchatPacket(
```
> يعرّف متغيراً ‏`fragmentPacket` (حزمة الشظية) ويبدأ بناء كائن ‏`BitchatPacket` بفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:129]

```
130:                 version = if (packet.route != null) 2u else 1u,
```
> يمرّر الوسيط المسمّى ‏`version` بالقيمة ‏`2u` إن كان ‏`packet.route` غير ‏`null` وإلا ‏`1u`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:130]

```
131:                 type = MessageType.FRAGMENT.value,
```
> يمرّر الوسيط المسمّى ‏`type` بالقيمة ‏`MessageType.FRAGMENT.value`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:131]

```
132:                 ttl = packet.ttl,
```
> يمرّر الوسيط المسمّى ‏`ttl` (مدة البقاء) بالقيمة ‏`packet.ttl`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:132]

```
133:                 senderID = packet.senderID,
```
> يمرّر الوسيط المسمّى ‏`senderID` (معرّف المُرسِل) بالقيمة ‏`packet.senderID`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:133]

```
134:                 recipientID = packet.recipientID,
```
> يمرّر الوسيط المسمّى ‏`recipientID` (معرّف المُستقبِل) بالقيمة ‏`packet.recipientID`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:134]

```
135:                 timestamp = packet.timestamp,
```
> يمرّر الوسيط المسمّى ‏`timestamp` (الطابع الزمني) بالقيمة ‏`packet.timestamp`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:135]

```
136:                 payload = fragmentPayload.encode(),
```
> يمرّر الوسيط المسمّى ‏`payload` (الحمولة) بناتج استدعاء ‏`fragmentPayload.encode()`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:136]

```
137:                 route = packet.route,
```
> يمرّر الوسيط المسمّى ‏`route` (المسار) بالقيمة ‏`packet.route`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:137]

```
138:                 signature = null // iOS: signature: nil
```
> يمرّر الوسيط المسمّى ‏`signature` (التوقيع) بالقيمة ‏`null`، مع تعليق: «iOS: ‏signature: nil». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:138]

```
139:             )
```
> إغلاق قائمة وسائط بناء ‏`BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:139]

```
140:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:140]

```
141:             fragments.add(fragmentPacket)
```
> يستدعي ‏`fragments.add(fragmentPacket)` لإضافة حزمة الشظية إلى القائمة. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:141]

```
142:         }
```
> إغلاق نطاق حلقة ‏`for`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:142]

```
143:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:143]

```
144:         Log.d(TAG, "✅ Created ${fragments.size} fragments successfully")
```
> يستدعي ‏`Log.d` مع الوسم ‏`TAG` ورسالة تذكر إنشاء ‏`fragments.size` شظية بنجاح. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:144]

```
145:             return fragments
```
> يعيد القائمة ‏`fragments`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:145]

```
146:         } catch (e: Exception) {
```
> يلتقط استثناءً ‏`Exception` في المتغير ‏`e` ويفتح نطاق المعالجة لكتلة ‏`try` الخارجية. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:146]

```
147:             Log.e(TAG, "❌ Fragment creation failed: ${e.message}", e)
```
> يستدعي ‏`Log.e` مع الوسم ‏`TAG` ورسالة «فشل إنشاء الشظية» متبوعةً برسالة الاستثناء ‏`e.message` والاستثناء ‏`e`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:147]

```
148:             Log.e(TAG, "❌ Packet type: ${packet.type}, payload: ${packet.payload.size} bytes")
```
> يستدعي ‏`Log.e` مع الوسم ‏`TAG` ورسالة تذكر نوع الحزمة ‏`packet.type` وحجم حمولتها ‏`packet.payload.size` بالبايت. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:148]

```
149:             return emptyList()
```
> يعيد قائمة فارغة عبر ‏`emptyList()`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:149]

```
150:         }
```
> إغلاق نطاق كتلة ‏`catch`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:150]

```
151:     }
```
> إغلاق نطاق الدالة ‏`createFragments`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:151]

```
152:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:152]

```
153:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:153]

```
154:      * Handle incoming fragment - 100% iOS Compatible  
```
> تعليق: «عالج شظية واردة - متوافق ١٠٠٪ مع iOS». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:154]

```
155:      * Matches iOS handleFragment() implementation exactly
```
> تعليق: «يطابق تماماً تنفيذ ‏handleFragment() في iOS». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:155]

```
156:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:156]

```
157:     fun handleFragment(packet: BitchatPacket): BitchatPacket? {
```
> يعرّف الدالة ‏`handleFragment` (معالجة الشظية) تأخذ معامل ‏`packet` من نوع ‏`BitchatPacket` وتعيد ‏`BitchatPacket?` القابل لأن يكون فارغاً، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:157]

```
158:         // iOS: guard packet.payload.count > 13 else { return }
```
> تعليق: «iOS: ‏guard packet.payload.count > 13 else { return }». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:158]

```
159:         if (packet.payload.size < FragmentPayload.HEADER_SIZE) {
```
> يفتح شرطاً يفحص ما إذا كان ‏`packet.payload.size` أصغر من ‏`FragmentPayload.HEADER_SIZE`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:159]

```
160:             Log.w(TAG, "Fragment packet too small: ${packet.payload.size}")
```
> يستدعي ‏`Log.w` مع الوسم ‏`TAG` ورسالة «حزمة الشظية صغيرة جداً: ‏${packet.payload.size}». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:160]

```
161:             return null
```
> يعيد ‏`null`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:161]

```
162:         }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:162]

```
163:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:163]

```
164:         // Don't process our own fragments - iOS equivalent check
```
> تعليق: «لا تعالج شظايانا الخاصة - فحص مكافئ لـ iOS». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:164]

```
165:         // This would be done at a higher level but we'll include for safety
```
> تعليق: «هذا يُفترض أن يُنجَز على مستوى أعلى لكننا سندرجه احتياطاً». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:165]

```
166:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:166]

```
167:         try {
```
> يفتح كتلة ‏`try`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:167]

```
168:             // Use FragmentPayload for type-safe decoding
```
> تعليق: «استعمل ‏FragmentPayload لفك ترميز آمن من حيث النوع». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:168]

```
169:             val fragmentPayload = FragmentPayload.decode(packet.payload)
```
> يعرّف متغيراً ‏`fragmentPayload` (حمولة الشظية) ويضبطه إلى ناتج استدعاء ‏`FragmentPayload.decode(packet.payload)`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:169]

```
170:             if (fragmentPayload == null || !fragmentPayload.isValid()) {
```
> يفتح شرطاً يفحص ما إذا كان ‏`fragmentPayload` مساوياً ‏`null` أو أن ‏`fragmentPayload.isValid()` يعيد خطأً. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:170]

```
171:                 Log.w(TAG, "Invalid fragment payload")
```
> يستدعي ‏`Log.w` مع الوسم ‏`TAG` والرسالة «حمولة شظية غير صالحة». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:171]

```
172:                 return null
```
> يعيد ‏`null`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:172]

```
173:             }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:173]

```
174:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:174]

```
175:             // iOS: let fragmentID = packet.payload[0..<8].map { String(format: "%02x", $0) }.joined()
```
> تعليق: «iOS: ‏let fragmentID = packet.payload[0..<8].map { String(format: "%02x", $0) }.joined()». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:175]

```
176:             val fragmentIDString = fragmentPayload.getFragmentIDString()
```
> يعرّف متغيراً ‏`fragmentIDString` (نص معرّف الشظية) ويضبطه إلى ناتج استدعاء ‏`fragmentPayload.getFragmentIDString()`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:176]

```
177:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:177]

```
178:             Log.d(TAG, "Received fragment ${fragmentPayload.index}/${fragmentPayload.total} for fragmentID: $fragmentIDString, originalType: ${fragmentPayload.originalType}")
```
> يستدعي ‏`Log.d` مع الوسم ‏`TAG` ورسالة «استُلمت الشظية ‏${fragmentPayload.index}/${fragmentPayload.total} للمعرّف ‏$fragmentIDString، النوع الأصلي ‏${fragmentPayload.originalType}». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:178]

```
179: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:179]

```
180:             val maxFragments = com.bitchat.android.util.AppConstants.Fragmentation.MAX_FRAGMENTS_PER_ID
```
> يعرّف متغيراً ‏`maxFragments` (أقصى عدد شظايا) ويضبطه إلى ‏`AppConstants.Fragmentation.MAX_FRAGMENTS_PER_ID`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:180]

```
181:             if (fragmentPayload.total > maxFragments) {
```
> يفتح شرطاً يفحص ما إذا كان ‏`fragmentPayload.total` أكبر من ‏`maxFragments`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:181]

```
182:                 Log.w(TAG, "Rejecting fragment with excessive total count: ${fragmentPayload.total} > $maxFragments")
```
> يستدعي ‏`Log.w` مع الوسم ‏`TAG` ورسالة «رفض شظية بعدد إجمالي مفرط: ‏${fragmentPayload.total} > $maxFragments». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:182]

```
183:                 return null
```
> يعيد ‏`null`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:183]

```
184:             }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:184]

```
185: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:185]

```
186:             synchronized(fragmentStateLock) {
```
> يفتح كتلة متزامنة ‏`synchronized` على القفل ‏`fragmentStateLock`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:186]

```
187:                 fragmentMetadata[fragmentIDString]?.let { (expectedType, expectedTotal, _) ->
```
> يصل إلى ‏`fragmentMetadata[fragmentIDString]` وإن لم يكن ‏`null` ينفّذ ‏`let` مفككاً الثلاثية إلى ‏`expectedType` (النوع المتوقّع) و‏`expectedTotal` (الإجمالي المتوقّع) وعنصر مهمل، ويفتح جسم اللامبدا. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:187]

```
188:                     if (expectedTotal != fragmentPayload.total || expectedType != fragmentPayload.originalType) {
```
> يفتح شرطاً يفحص ما إذا كان ‏`expectedTotal` لا يساوي ‏`fragmentPayload.total` أو ‏`expectedType` لا يساوي ‏`fragmentPayload.originalType`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:188]

```
189:                         Log.w(
```
> يبدأ استدعاء ‏`Log.w` بفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:189]

```
190:                             TAG,
```
> يمرّر الوسيط الأول ‏`TAG`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:190]

```
191:                             "Rejecting fragment for $fragmentIDString: inconsistent metadata " +
```
> يمرّر بداية سلسلة الرسالة «رفض شظية للمعرّف ‏$fragmentIDString: بيانات وصف غير متّسقة » مع عامل وصل ‏`+`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:191]

```
192:                                 "(expected type=$expectedType total=$expectedTotal, got type=${fragmentPayload.originalType} total=${fragmentPayload.total})"
```
> يكمل سلسلة الرسالة بـ«(المتوقّع type=$expectedType total=$expectedTotal، الوارد type=${fragmentPayload.originalType} total=${fragmentPayload.total})». [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:192]

```
193:                         )
```
> إغلاق قائمة وسائط استدعاء ‏`Log.w`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:193]

```
194:                         removeFragmentSetLocked(fragmentIDString)
```
> يستدعي ‏`removeFragmentSetLocked(fragmentIDString)` (إزالة مجموعة الشظايا تحت القفل). [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:194]

```
195:                         return null
```
> يعيد ‏`null`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:195]

```
196:                     }
```
> إغلاق نطاق الشرط الداخلي. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:196]

```
197:                 }
```
> إغلاق نطاق لامبدا ‏`let`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:197]

```
198: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:198]

```
199:                 val isNewSet = !incomingFragments.containsKey(fragmentIDString)
```
> يعرّف متغيراً ‏`isNewSet` (مجموعة جديدة) ويضبطه إلى نفي نتيجة ‏`incomingFragments.containsKey(fragmentIDString)`. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:199]

```
200:                 if (isNewSet) {
```
> يفتح شرطاً يفحص ما إذا كان ‏`isNewSet` صحيحاً. [app/src/main/java/com/bitchat/android/mesh/FragmentManager.kt:200]
