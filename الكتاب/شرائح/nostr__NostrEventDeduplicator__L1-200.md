# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يُعرّف اسم الحزمة (package) بأنها com.bitchat.android.nostr. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:2]

```
3: import android.util.Log
```
> يستورد الصنف Log من android.util. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:3]

```
4: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف ConcurrentHashMap من java.util.concurrent. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:5]

```
6: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:6]

```
7:  * Efficient LRU-based Nostr event deduplication system
```
> تعليق: نظام كفؤ لإزالة تكرار أحداث Nostr قائم على LRU (الأقل استخداماً مؤخراً). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:7]

```
8:  * 
```
> تعليق: سطر فارغ داخل التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:8]

```
9:  * This class provides thread-safe deduplication of Nostr events based on their event IDs.
```
> تعليق: هذا الصنف يوفّر إزالة تكرار آمنة على مستوى الخيوط لأحداث Nostr اعتماداً على معرّفات أحداثها. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:9]

```
10:  * It maintains an LRU cache of up to 10,000 event IDs to prevent memory bloat while ensuring
```
> تعليق: يحتفظ بمخزن مؤقت من نوع LRU يسع حتى 10,000 معرّف حدث لمنع تضخّم الذاكرة مع ضمان. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:10]

```
11:  * duplicate events (which commonly arrive via different relays) are processed only once.
```
> تعليق: أنّ الأحداث المكرّرة (التي تصل عادةً عبر مُرحِّلات (relays) مختلفة) تُعالَج مرة واحدة فقط. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:11]

```
12:  * 
```
> تعليق: سطر فارغ داخل التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:12]

```
13:  * Features:
```
> تعليق: المزايا. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:13]

```
14:  * - Thread-safe concurrent access
```
> تعليق: وصول متزامن آمن على مستوى الخيوط. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:14]

```
15:  * - LRU eviction when capacity is exceeded
```
> تعليق: إخراج (eviction) وفق LRU عند تجاوز السعة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:15]

```
16:  * - Configurable capacity (default 10,000)
```
> تعليق: سعة قابلة للضبط (الافتراضي 10,000). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:16]

```
17:  * - Efficient O(1) lookup and insertion
```
> تعليق: بحث وإدراج كفؤان بتعقيد O(1). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:17]

```
18:  * - Memory-bounded to prevent unbounded growth
```
> تعليق: محدود الذاكرة لمنع النمو غير المحدود. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:18]

```
19:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:19]

```
20: class NostrEventDeduplicator(
```
> يُعرّف الصنف مُزيل تكرار أحداث نوستر (NostrEventDeduplicator) مع بداية قائمة معاملات المُنشئ الأساسي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:20]

```
21:     private val maxCapacity: Int = DEFAULT_CAPACITY
```
> يُعرّف خاصية خاصة باسم السعة القصوى (maxCapacity) من النوع Int وقيمتها الافتراضية DEFAULT_CAPACITY. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:21]

```
22: ) {
```
> إغلاق قائمة معاملات المُنشئ وفتح جسم الصنف. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:22]

```
23:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:23]

```
24:         private const val TAG = "NostrDeduplicator"
```
> يُعرّف ثابتاً خاصاً باسم TAG وقيمته النصية "NostrDeduplicator". [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:24]

```
25:         private const val DEFAULT_CAPACITY = com.bitchat.android.util.AppConstants.Nostr.DEFAULT_DEDUP_CAPACITY
```
> يُعرّف ثابتاً خاصاً باسم السعة الافتراضية (DEFAULT_CAPACITY) وقيمته com.bitchat.android.util.AppConstants.Nostr.DEFAULT_DEDUP_CAPACITY. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:25]

```
26:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:26]

```
27:         @Volatile
```
> تعليق توضيحي (annotation) ‎@Volatile‎ يُطبّق على ما يليه. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:27]

```
28:         private var INSTANCE: NostrEventDeduplicator? = null
```
> يُعرّف متغيراً خاصاً باسم INSTANCE من النوع NostrEventDeduplicator القابل لأن يكون فارغاً وقيمته الابتدائية null. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:28]

```
29:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:29]

```
30:         /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:30]

```
31:          * Get the singleton instance of the deduplicator
```
> تعليق: احصل على نسخة مفردة (singleton) من مُزيل التكرار. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:31]

```
32:          */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:32]

```
33:         fun getInstance(): NostrEventDeduplicator {
```
> يُعرّف الدالة getInstance التي تُعيد قيمة من النوع NostrEventDeduplicator، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:33]

```
34:             return INSTANCE ?: synchronized(this) {
```
> يُعيد INSTANCE إن لم يكن null، وإلا يدخل كتلة متزامنة (synchronized) على this. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:34]

```
35:                 INSTANCE ?: NostrEventDeduplicator().also { INSTANCE = it }
```
> يُعيد INSTANCE إن لم يكن null، وإلا يُنشئ NostrEventDeduplicator جديداً ويُسند الناتج إلى INSTANCE عبر also. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:35]

```
36:             }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:36]

```
37:         }
```
> إغلاق نطاق الدالة getInstance. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:37]

```
38:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:38]

```
39:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:39]

```
40:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:40]

```
41:      * Node for the doubly-linked list used in LRU implementation
```
> تعليق: عقدة (node) للقائمة المترابطة المزدوجة المستعملة في تنفيذ LRU. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:41]

```
42:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:42]

```
43:     private data class LRUNode(
```
> يُعرّف صنف بيانات خاص باسم عقدة LRU (LRUNode) مع بداية قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:43]

```
44:         val eventId: String,
```
> يُعرّف خاصية ثابتة باسم معرّف الحدث (eventId) من النوع String. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:44]

```
45:         var prev: LRUNode? = null,
```
> يُعرّف خاصية متغيرة باسم السابق (prev) من النوع LRUNode القابل لأن يكون فارغاً وقيمتها الابتدائية null. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:45]

```
46:         var next: LRUNode? = null
```
> يُعرّف خاصية متغيرة باسم التالي (next) من النوع LRUNode القابل لأن يكون فارغاً وقيمتها الابتدائية null. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:46]

```
47:     )
```
> إغلاق قائمة معاملات صنف البيانات LRUNode. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:47]

```
48:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:48]

```
49:     // Hash map for O(1) lookup - maps event ID to node
```
> تعليق: خريطة تجزئة (hash map) للبحث بتعقيد O(1) - تربط معرّف الحدث بالعقدة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:49]

```
50:     private val nodeMap = ConcurrentHashMap<String, LRUNode>()
```
> يُعرّف خاصية ثابتة خاصة باسم خريطة العقد (nodeMap) قيمتها كائن ConcurrentHashMap من String إلى LRUNode. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:50]

```
51:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:51]

```
52:     // Doubly-linked list for LRU ordering
```
> تعليق: قائمة مترابطة مزدوجة لترتيب LRU. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:52]

```
53:     private val head = LRUNode("HEAD") // Dummy head node
```
> يُعرّف خاصية ثابتة خاصة باسم الرأس (head) قيمتها عقدة LRUNode بمعرّف "HEAD"، مع تعليق: عقدة رأس وهمية. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:53]

```
54:     private val tail = LRUNode("TAIL") // Dummy tail node
```
> يُعرّف خاصية ثابتة خاصة باسم الذيل (tail) قيمتها عقدة LRUNode بمعرّف "TAIL"، مع تعليق: عقدة ذيل وهمية. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:54]

```
55:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:55]

```
56:     // Lock for thread-safe LRU operations
```
> تعليق: قفل (lock) لعمليات LRU الآمنة على مستوى الخيوط. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:56]

```
57:     private val lruLock = Any()
```
> يُعرّف خاصية ثابتة خاصة باسم قفل LRU (lruLock) قيمتها كائن Any. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:57]

```
58:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:58]

```
59:     // Statistics
```
> تعليق: إحصاءات. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:59]

```
60:     @Volatile
```
> تعليق توضيحي ‎@Volatile‎ يُطبّق على ما يليه. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:60]

```
61:     private var totalChecks = 0L
```
> يُعرّف متغيراً خاصاً باسم إجمالي الفحوص (totalChecks) وقيمته الابتدائية 0L (من نوع Long). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:61]

```
62:     @Volatile
```
> تعليق توضيحي ‎@Volatile‎ يُطبّق على ما يليه. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:62]

```
63:     private var duplicateCount = 0L
```
> يُعرّف متغيراً خاصاً باسم عدّ المكرّرات (duplicateCount) وقيمته الابتدائية 0L. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:63]

```
64:     @Volatile
```
> تعليق توضيحي ‎@Volatile‎ يُطبّق على ما يليه. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:64]

```
65:     private var evictionCount = 0L
```
> يُعرّف متغيراً خاصاً باسم عدّ الإخراجات (evictionCount) وقيمته الابتدائية 0L. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:65]

```
66:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:66]

```
67:     init {
```
> يفتح كتلة التهيئة (init). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:67]

```
68:         // Initialize the doubly-linked list
```
> تعليق: هيّئ القائمة المترابطة المزدوجة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:68]

```
69:         head.next = tail
```
> يُسند tail إلى الخاصية next للعقدة head. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:69]

```
70:         tail.prev = head
```
> يُسند head إلى الخاصية prev للعقدة tail. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:70]

```
71:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:71]

```
72:         Log.d(TAG, "Initialized NostrEventDeduplicator with capacity: $maxCapacity")
```
> يستدعي Log.d بالوسم TAG ونص "Initialized NostrEventDeduplicator with capacity: $maxCapacity" مع إدراج قيمة maxCapacity. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:72]

```
73:     }
```
> إغلاق نطاق كتلة التهيئة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:73]

```
74:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:74]

```
75:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:75]

```
76:      * Check if an event has been seen before and mark it as seen
```
> تعليق: افحص ما إذا كان الحدث قد شوهد من قبل وعَلِّمه بأنه شوهد. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:76]

```
77:      * 
```
> تعليق: سطر فارغ داخل التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:77]

```
78:      * @param eventId The Nostr event ID to check
```
> تعليق: المعامل eventId هو معرّف حدث Nostr المراد فحصه. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:78]

```
79:      * @return true if the event is a duplicate (already seen), false if it's new
```
> تعليق: يُعيد true إن كان الحدث مكرّراً (شوهد سابقاً)، و false إن كان جديداً. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:79]

```
80:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:80]

```
81:     fun isDuplicate(eventId: String): Boolean {
```
> يُعرّف الدالة isDuplicate التي تأخذ المعامل eventId من النوع String وتُعيد Boolean، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:81]

```
82:         totalChecks++
```
> يزيد قيمة totalChecks بمقدار واحد. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:82]

```
83:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:83]

```
84:         synchronized(lruLock) {
```
> يدخل كتلة متزامنة (synchronized) على lruLock. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:84]

```
85:             val existingNode = nodeMap[eventId]
```
> يُعرّف ثابتاً محلياً باسم العقدة الموجودة (existingNode) قيمته نتيجة الوصول إلى nodeMap بالمفتاح eventId. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:85]

```
86:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:86]

```
87:             if (existingNode != null) {
```
> يبدأ شرطاً يختبر ما إذا كان existingNode لا يساوي null. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:87]

```
88:                 // Event is a duplicate - move to front (most recently used)
```
> تعليق: الحدث مكرّر - انقله إلى المقدمة (الأكثر استخداماً مؤخراً). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:88]

```
89:                 moveToFront(existingNode)
```
> يستدعي الدالة moveToFront ممرّراً existingNode. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:89]

```
90:                 duplicateCount++
```
> يزيد قيمة duplicateCount بمقدار واحد. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:90]

```
91:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:91]

```
92:                 if (duplicateCount % 100 == 0L) {
```
> يبدأ شرطاً يختبر ما إذا كان باقي قسمة duplicateCount على 100 يساوي 0L. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:92]

```
93:                     Log.v(TAG, "Duplicate event detected: $eventId (${duplicateCount} total duplicates)")
```
> يستدعي Log.v بالوسم TAG ونص "Duplicate event detected: $eventId (${duplicateCount} total duplicates)" مع إدراج قيمتي eventId و duplicateCount. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:93]

```
94:                 }
```
> إغلاق نطاق شرط باقي القسمة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:94]

```
95:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:95]

```
96:                 return true
```
> يُعيد القيمة true. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:96]

```
97:             } else {
```
> يُغلق فرع if ويبدأ فرع else. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:97]

```
98:                 // New event - add to front
```
> تعليق: حدث جديد - أضِفه إلى المقدمة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:98]

```
99:                 addToFront(eventId)
```
> يستدعي الدالة addToFront ممرّراً eventId. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:99]

```
100:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:100]

```
101:                 // Check if we need to evict oldest entries
```
> تعليق: افحص ما إذا كنا بحاجة لإخراج أقدم المدخلات. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:101]

```
102:                 if (nodeMap.size > maxCapacity) {
```
> يبدأ شرطاً يختبر ما إذا كان حجم nodeMap أكبر من maxCapacity. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:102]

```
103:                     evictOldest()
```
> يستدعي الدالة evictOldest. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:103]

```
104:                 }
```
> إغلاق نطاق شرط فحص الحجم. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:104]

```
105:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:105]

```
106:                 return false
```
> يُعيد القيمة false. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:106]

```
107:             }
```
> إغلاق نطاق فرع else. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:107]

```
108:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:108]

```
109:     }
```
> إغلاق نطاق الدالة isDuplicate. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:109]

```
110:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:110]

```
111:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:111]

```
112:      * Process a Nostr event with deduplication
```
> تعليق: عالِج حدث Nostr مع إزالة التكرار. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:112]

```
113:      * 
```
> تعليق: سطر فارغ داخل التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:113]

```
114:      * @param event The Nostr event to process
```
> تعليق: المعامل event هو حدث Nostr المراد معالجته. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:114]

```
115:      * @param processor Function to call if the event is not a duplicate
```
> تعليق: المعامل processor دالة تُستدعى إن لم يكن الحدث مكرّراً. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:115]

```
116:      * @return true if the event was processed (not a duplicate), false if it was deduplicated
```
> تعليق: يُعيد true إن عُولج الحدث (غير مكرّر)، و false إن أُزيل تكراره. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:116]

```
117:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:117]

```
118:     fun processEvent(event: NostrEvent, processor: (NostrEvent) -> Unit): Boolean {
```
> يُعرّف الدالة processEvent التي تأخذ المعامل event من النوع NostrEvent والمعامل processor من نوع دالة تأخذ NostrEvent وتُعيد Unit، وتُعيد الدالة Boolean، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:118]

```
119:         return if (!isDuplicate(event.id)) {
```
> يُعيد نتيجة تعبير if الذي يختبر نفي isDuplicate المطبّقة على event.id. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:119]

```
120:             processor(event)
```
> يستدعي الدالة processor ممرّراً event. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:120]

```
121:             true
```
> القيمة المُعادة من فرع if هي true. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:121]

```
122:         } else {
```
> يُغلق فرع if ويبدأ فرع else. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:122]

```
123:             false
```
> القيمة المُعادة من فرع else هي false. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:123]

```
124:         }
```
> إغلاق نطاق تعبير if/else. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:124]

```
125:     }
```
> إغلاق نطاق الدالة processEvent. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:125]

```
126:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:126]

```
127:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:127]

```
128:      * Get current statistics about the deduplicator
```
> تعليق: احصل على الإحصاءات الحالية عن مُزيل التكرار. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:128]

```
129:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:129]

```
130:     fun getStats(): DeduplicationStats {
```
> يُعرّف الدالة getStats التي تُعيد قيمة من النوع DeduplicationStats، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:130]

```
131:         synchronized(lruLock) {
```
> يدخل كتلة متزامنة على lruLock. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:131]

```
132:             return DeduplicationStats(
```
> يُعيد كائن DeduplicationStats مع بداية قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:132]

```
133:                 capacity = maxCapacity,
```
> يُسند maxCapacity إلى الوسيط المُسمّى capacity. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:133]

```
134:                 currentSize = nodeMap.size,
```
> يُسند nodeMap.size إلى الوسيط المُسمّى currentSize. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:134]

```
135:                 totalChecks = totalChecks,
```
> يُسند totalChecks إلى الوسيط المُسمّى totalChecks. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:135]

```
136:                 duplicateCount = duplicateCount,
```
> يُسند duplicateCount إلى الوسيط المُسمّى duplicateCount. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:136]

```
137:                 evictionCount = evictionCount,
```
> يُسند evictionCount إلى الوسيط المُسمّى evictionCount. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:137]

```
138:                 hitRate = if (totalChecks > 0) (duplicateCount.toDouble() / totalChecks.toDouble()) else 0.0
```
> يُسند إلى الوسيط المُسمّى hitRate نتيجةَ تعبير if: إن كان totalChecks أكبر من 0 فقسمة duplicateCount.toDouble على totalChecks.toDouble، وإلا 0.0. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:138]

```
139:             )
```
> إغلاق قائمة وسائط DeduplicationStats. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:139]

```
140:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:140]

```
141:     }
```
> إغلاق نطاق الدالة getStats. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:141]

```
142:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:142]

```
143:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:143]

```
144:      * Clear all cached event IDs (useful for testing or resetting state)
```
> تعليق: امسح كل معرّفات الأحداث المخزّنة (مفيد للاختبار أو إعادة ضبط الحالة). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:144]

```
145:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:145]

```
146:     fun clear() {
```
> يُعرّف الدالة clear بلا معاملات ولا قيمة معادة صريحة، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:146]

```
147:         synchronized(lruLock) {
```
> يدخل كتلة متزامنة على lruLock. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:147]

```
148:             nodeMap.clear()
```
> يستدعي الدالة clear على nodeMap. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:148]

```
149:             head.next = tail
```
> يُسند tail إلى الخاصية next للعقدة head. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:149]

```
150:             tail.prev = head
```
> يُسند head إلى الخاصية prev للعقدة tail. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:150]

```
151:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:151]

```
152:             // Reset statistics
```
> تعليق: أعِد ضبط الإحصاءات. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:152]

```
153:             totalChecks = 0L
```
> يُسند 0L إلى totalChecks. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:153]

```
154:             duplicateCount = 0L
```
> يُسند 0L إلى duplicateCount. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:154]

```
155:             evictionCount = 0L
```
> يُسند 0L إلى evictionCount. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:155]

```
156:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:156]

```
157:             Log.d(TAG, "Cleared all cached event IDs")
```
> يستدعي Log.d بالوسم TAG ونص "Cleared all cached event IDs". [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:157]

```
158:         }
```
> إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:158]

```
159:     }
```
> إغلاق نطاق الدالة clear. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:159]

```
160:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:160]

```
161:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:161]

```
162:      * Check if the deduplicator contains a specific event ID
```
> تعليق: افحص ما إذا كان مُزيل التكرار يحتوي معرّف حدث معيّن. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:162]

```
163:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:163]

```
164:     fun contains(eventId: String): Boolean {
```
> يُعرّف الدالة contains التي تأخذ المعامل eventId من النوع String وتُعيد Boolean، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:164]

```
165:         return nodeMap.containsKey(eventId)
```
> يُعيد نتيجة استدعاء nodeMap.containsKey ممرّراً eventId. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:165]

```
166:     }
```
> إغلاق نطاق الدالة contains. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:166]

```
167:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:167]

```
168:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:168]

```
169:      * Get the current size of the cache
```
> تعليق: احصل على الحجم الحالي للمخزن المؤقت. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:169]

```
170:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:170]

```
171:     fun size(): Int = nodeMap.size
```
> يُعرّف الدالة size التي تُعيد Int، وقيمتها المعادة هي nodeMap.size عبر تعبير مفرد. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:171]

```
172:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:172]

```
173:     // MARK: - Private LRU Implementation Methods
```
> تعليق: MARK: - دوال تنفيذ LRU الخاصة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:173]

```
174:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:174]

```
175:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:175]

```
176:      * Add a new event ID to the front of the LRU list
```
> تعليق: أضِف معرّف حدث جديداً إلى مقدمة قائمة LRU. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:176]

```
177:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:177]

```
178:     private fun addToFront(eventId: String) {
```
> يُعرّف الدالة الخاصة addToFront التي تأخذ المعامل eventId من النوع String، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:178]

```
179:         val newNode = LRUNode(eventId)
```
> يُعرّف ثابتاً محلياً باسم العقدة الجديدة (newNode) قيمته كائن LRUNode مُنشأ بالمعرّف eventId. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:179]

```
180:         nodeMap[eventId] = newNode
```
> يُسند newNode إلى المدخل ذي المفتاح eventId في nodeMap. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:180]

```
181:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:181]

```
182:         // Insert after head
```
> تعليق: أدرِج بعد الرأس. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:182]

```
183:         newNode.next = head.next
```
> يُسند head.next إلى الخاصية next للعقدة newNode. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:183]

```
184:         newNode.prev = head
```
> يُسند head إلى الخاصية prev للعقدة newNode. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:184]

```
185:         head.next?.prev = newNode
```
> يُسند newNode إلى الخاصية prev لـ head.next إن لم يكن head.next فارغاً. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:185]

```
186:         head.next = newNode
```
> يُسند newNode إلى الخاصية next للعقدة head. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:186]

```
187:     }
```
> إغلاق نطاق الدالة addToFront. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:187]

```
188:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:188]

```
189:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:189]

```
190:      * Move an existing node to the front (most recently used position)
```
> تعليق: انقل عقدة موجودة إلى المقدمة (موضع الأكثر استخداماً مؤخراً). [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:190]

```
191:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:191]

```
192:     private fun moveToFront(node: LRUNode) {
```
> يُعرّف الدالة الخاصة moveToFront التي تأخذ المعامل node من النوع LRUNode، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:192]

```
193:         // Remove from current position
```
> تعليق: أزِل من الموضع الحالي. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:193]

```
194:         node.prev?.next = node.next
```
> يُسند node.next إلى الخاصية next لـ node.prev إن لم يكن node.prev فارغاً. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:194]

```
195:         node.next?.prev = node.prev
```
> يُسند node.prev إلى الخاصية prev لـ node.next إن لم يكن node.next فارغاً. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:195]

```
196:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:196]

```
197:         // Insert at front
```
> تعليق: أدرِج في المقدمة. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:197]

```
198:         node.next = head.next
```
> يُسند head.next إلى الخاصية next للعقدة node. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:198]

```
199:         node.prev = head
```
> يُسند head إلى الخاصية prev للعقدة node. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:199]

```
200:         head.next?.prev = node
```
> يُسند node إلى الخاصية prev لـ head.next إن لم يكن head.next فارغاً. [app/src/main/java/com/bitchat/android/nostr/NostrEventDeduplicator.kt:200]
