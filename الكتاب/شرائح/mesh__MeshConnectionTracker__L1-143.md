# شريحة — app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt (الأسطر 1–143)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) ‎com.bitchat.android.mesh‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف ‎Log‎ من ‎android.util‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:3]

```
4: import kotlinx.coroutines.CancellationException
```
> يستورد صنف استثناء الإلغاء (CancellationException) من ‎kotlinx.coroutines‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:4]

```
5: import kotlinx.coroutines.CoroutineScope
```
> يستورد نطاق الكوروتين (CoroutineScope) من ‎kotlinx.coroutines‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:5]

```
6: import kotlinx.coroutines.delay
```
> يستورد دالة التأخير (delay) من ‎kotlinx.coroutines‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:6]

```
7: import kotlinx.coroutines.launch
```
> يستورد دالة الإطلاق (launch) من ‎kotlinx.coroutines‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:7]

```
8: import java.util.concurrent.ConcurrentHashMap
```
> يستورد صنف الخريطة المتزامنة (ConcurrentHashMap) من ‎java.util.concurrent‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:9]

```
10: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:10]

```
11:  * Abstract base tracker for mesh connections (BLE, Wi-Fi Aware, etc.)
```
> تعليق: متعقّب أساسي مجرّد لاتصالات الشبكة المتشابكة (BLE وWi-Fi Aware وغيرها). [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:11]

```
12:  * Encapsulates common state machine logic:
```
> تعليق: يغلّف منطق آلة الحالات المشترك. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:12]

```
13:  * - Connection attempt tracking (retries, backoff)
```
> تعليق: تتبّع محاولات الاتصال (إعادة المحاولة، التراجع). [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:13]

```
14:  * - Pending connection management
```
> تعليق: إدارة الاتصالات المعلّقة. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:14]

```
15:  * - Automatic cleanup of expired attempts
```
> تعليق: تنظيف تلقائي للمحاولات المنتهية الصلاحية. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:15]

```
16:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:16]

```
17: abstract class MeshConnectionTracker(
```
> يعرّف صنفاً مجرّداً (abstract class) باسم متعقّب اتصالات الشبكة المتشابكة (MeshConnectionTracker) ويبدأ قائمة معاملات الباني. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:17]

```
18:     private val scope: CoroutineScope,
```
> يعرّف خاصيّة خاصّة (private val) باسم النطاق (scope) من نوع نطاق الكوروتين. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:18]

```
19:     protected val tag: String
```
> يعرّف خاصيّة محميّة (protected val) باسم الوسم (tag) من نوع سلسلة نصية. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:19]

```
20: ) {
```
> يُغلق قائمة معاملات الباني ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:20]

```
21:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:21]

```
22:         const val CONNECTION_RETRY_DELAY = 5_000L
```
> يعرّف ثابتاً (const val) باسم تأخير إعادة محاولة الاتصال (CONNECTION_RETRY_DELAY) بقيمة ‎5_000L‎ من نوع Long. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:22]

```
23:         const val MAX_CONNECTION_ATTEMPTS = 3
```
> يعرّف ثابتاً باسم الحد الأقصى لمحاولات الاتصال (MAX_CONNECTION_ATTEMPTS) بقيمة ‎3‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:23]

```
24:         const val CLEANUP_INTERVAL = 30_000L
```
> يعرّف ثابتاً باسم فترة التنظيف (CLEANUP_INTERVAL) بقيمة ‎30_000L‎ من نوع Long. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:24]

```
25:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:25]

```
26: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:26]

```
27:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:27]

```
28:      * Connection attempt tracking with automatic expiry
```
> تعليق: تتبّع محاولة الاتصال مع انتهاء صلاحية تلقائي. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:28]

```
29:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:29]

```
30:     protected data class ConnectionAttempt(
```
> يعرّف صنف بيانات محمياً (protected data class) باسم محاولة الاتصال (ConnectionAttempt) ويبدأ معاملاته. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:30]

```
31:         val attempts: Int,
```
> يعرّف خاصيّة (val) باسم المحاولات (attempts) من نوع عدد صحيح Int. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:31]

```
32:         val lastAttempt: Long = System.currentTimeMillis()
```
> يعرّف خاصيّة باسم آخر محاولة (lastAttempt) من نوع Long بقيمة افتراضية هي الوقت الحالي بالمللي ثانية ‎System.currentTimeMillis()‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:32]

```
33:     ) {
```
> يُغلق معاملات صنف البيانات ويفتح جسمه. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:33]

```
34:         fun isExpired(): Boolean =
```
> يعرّف دالة باسم هل انتهت الصلاحية (isExpired) تعيد قيمة منطقية Boolean بصيغة تعبير. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:34]

```
35:             System.currentTimeMillis() - lastAttempt > CONNECTION_RETRY_DELAY * 2
```
> تعيد نتيجة المقارنة: الوقت الحالي بالمللي ثانية ناقص آخر محاولة أكبر من ‎CONNECTION_RETRY_DELAY‎ مضروباً في ‎2‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:36]

```
37:         fun shouldRetry(): Boolean =
```
> يعرّف دالة باسم هل يجب إعادة المحاولة (shouldRetry) تعيد قيمة منطقية Boolean بصيغة تعبير. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:37]

```
38:             attempts < MAX_CONNECTION_ATTEMPTS &&
```
> تبدأ التعبير المعاد: المحاولات أقل من ‎MAX_CONNECTION_ATTEMPTS‎ ومعطوفة بـ«و» المنطقية ‎&&‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:38]

```
39:                     System.currentTimeMillis() - lastAttempt > CONNECTION_RETRY_DELAY
```
> يكمل التعبير: الوقت الحالي بالمللي ثانية ناقص آخر محاولة أكبر من ‎CONNECTION_RETRY_DELAY‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:39]

```
40:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:40]

```
41: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:41]

```
42:     // Tracks in-progress or failed attempts
```
> تعليق: يتتبّع المحاولات الجارية أو الفاشلة. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:42]

```
43:     protected val pendingConnections = ConcurrentHashMap<String, ConnectionAttempt>()
```
> يعرّف خاصيّة محميّة باسم الاتصالات المعلّقة (pendingConnections) ويسندها إلى خريطة متزامنة جديدة مفتاحها سلسلة نصية وقيمتها محاولة اتصال. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:43]

```
44: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:44]

```
45:     private var isActive = false
```
> يعرّف متغيّراً خاصاً (private var) باسم هل نشط (isActive) بقيمة ابتدائية ‎false‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:45]

```
46: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:46]

```
47:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:47]

```
48:      * Start the tracker and its cleanup loop
```
> تعليق: ابدأ المتعقّب وحلقة التنظيف الخاصة به. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:48]

```
49:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:49]

```
50:     open fun start() {
```
> يعرّف دالة قابلة للتجاوز (open fun) باسم ابدأ (start) بلا معاملات ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:50]

```
51:         isActive = true
```
> يُسند القيمة ‎true‎ إلى المتغيّر هل نشط (isActive). [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:51]

```
52:         startPeriodicCleanup()
```
> يستدعي الدالة بدء التنظيف الدوري (startPeriodicCleanup). [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:52]

```
53:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:53]

```
54: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:54]

```
55:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:55]

```
56:      * Stop the tracker
```
> تعليق: أوقف المتعقّب. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:56]

```
57:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:57]

```
58:     open fun stop() {
```
> يعرّف دالة قابلة للتجاوز باسم أوقف (stop) بلا معاملات ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:58]

```
59:         isActive = false
```
> يُسند القيمة ‎false‎ إلى المتغيّر هل نشط (isActive). [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:59]

```
60:         pendingConnections.clear()
```
> يستدعي ‎clear()‎ على الاتصالات المعلّقة لإفراغها. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:60]

```
61:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:61]

```
62: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:62]

```
63:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:63]

```
64:      * Check if a connection attempt is allowed for this peer/address
```
> تعليق: افحص هل محاولة الاتصال مسموحة لهذا النِّد/العنوان. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:64]

```
65:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:65]

```
66:     fun isConnectionAttemptAllowed(id: String): Boolean {
```
> يعرّف دالة باسم هل محاولة الاتصال مسموحة (isConnectionAttemptAllowed) تأخذ معاملاً ‎id‎ من نوع سلسلة نصية وتعيد قيمة منطقية Boolean. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:66]

```
67:         // If already connected, usually no need to retry (subclasses can override logic if needed,
```
> تعليق: إذا كان متّصلاً بالفعل، فعادةً لا حاجة لإعادة المحاولة (يمكن للأصناف الفرعية تجاوز المنطق عند الحاجة، [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:67]

```
68:         // but typically the caller checks isConnected() first).
```
> تعليق: لكن عادةً يفحص المستدعي ‎isConnected()‎ أولاً). [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:68]

```
69:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:69]

```
70:         val existingAttempt = pendingConnections[id]
```
> يعرّف خاصيّة محليّة باسم المحاولة الموجودة (existingAttempt) ويسندها إلى قيمة الاتصالات المعلّقة عند المفتاح ‎id‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:70]

```
71:         return existingAttempt?.let {
```
> يعيد نتيجة استدعاء ‎let‎ الآمن من القيمة الخالية على المحاولة الموجودة ويفتح اللامدا. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:71]

```
72:             it.isExpired() || it.shouldRetry()
```
> تُقيّم: ‎isExpired()‎ أو ‎shouldRetry()‎ على العنصر ‎it‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:72]

```
73:         } ?: true
```
> يُغلق اللامدا ويوفّر القيمة البديلة ‎true‎ عند خلوّ المحاولة الموجودة (عامل إلفيس ‎?:‎). [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:73]

```
74:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:74]

```
75: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:75]

```
76:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:76]

```
77:      * Record a new connection attempt.
```
> تعليق: سجّل محاولة اتصال جديدة. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:77]

```
78:      * Returns true if the attempt was recorded (allowed), false if skipped.
```
> تعليق: تعيد ‎true‎ إذا سُجّلت المحاولة (مسموحة)، و‎false‎ إذا جرى تخطّيها. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:78]

```
79:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:79]

```
80:     fun addPendingConnection(id: String): Boolean {
```
> يعرّف دالة باسم أضف اتصالاً معلّقاً (addPendingConnection) تأخذ معاملاً ‎id‎ من نوع سلسلة نصية وتعيد قيمة منطقية Boolean. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:80]

```
81:         synchronized(pendingConnections) {
```
> يبدأ كتلة متزامنة (synchronized) مقفولة على الاتصالات المعلّقة. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:81]

```
82:             val currentAttempt = pendingConnections[id]
```
> يعرّف خاصيّة محليّة باسم المحاولة الحالية (currentAttempt) ويسندها إلى قيمة الاتصالات المعلّقة عند المفتاح ‎id‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:82]

```
83:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:83]

```
84:             // If strictly not allowed right now, reject
```
> تعليق: إذا لم يكن مسموحاً تماماً الآن، فارفض. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:84]

```
85:             if (currentAttempt != null && !currentAttempt.isExpired() && !currentAttempt.shouldRetry()) {
```
> يفحص شرطاً: المحاولة الحالية ليست خالية ‎و‎ ليست منتهية الصلاحية ‎و‎ لا يجب إعادة محاولتها، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:85]

```
86:                 Log.d(tag, "Connection attempt already in progress for $id")
```
> يستدعي ‎Log.d‎ بالوسم وبالرسالة «محاولة اتصال جارية بالفعل لـ ‎$id‎». [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:86]

```
87:                 return false
```
> يعيد القيمة ‎false‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:87]

```
88:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:88]

```
89: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:89]

```
90:             // Update attempt count
```
> تعليق: حدّث عدّاد المحاولات. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:90]

```
91:             // Reset to 1 if expired, otherwise increment
```
> تعليق: أعِد التعيين إلى ‎1‎ إن انتهت الصلاحية، وإلا فزِد بمقدار واحد. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:91]

```
92:             val attempts = if (currentAttempt?.isExpired() == true) 1 else (currentAttempt?.attempts ?: 0) + 1
```
> يعرّف خاصيّة محليّة باسم المحاولات (attempts) بقيمة ‎1‎ إذا كان ‎isExpired()‎ على المحاولة الحالية يساوي ‎true‎، وإلا فقيمة عدد محاولاتها (أو ‎0‎ عند الخلو) مضافاً إليها ‎1‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:92]

```
93:             pendingConnections[id] = ConnectionAttempt(attempts)
```
> يُسند إلى الاتصالات المعلّقة عند المفتاح ‎id‎ كائن محاولة اتصال جديداً مُنشَأً بقيمة ‎attempts‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:93]

```
94:             Log.d(tag, "Added pending connection for $id (attempts: $attempts)")
```
> يستدعي ‎Log.d‎ بالوسم وبالرسالة «أُضيف اتصال معلّق لـ ‎$id‎ (المحاولات: ‎$attempts‎)». [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:94]

```
95:             return true
```
> يعيد القيمة ‎true‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:95]

```
96:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:96]

```
97:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:97]

```
98: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:98]

```
99:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:99]

```
100:      * Remove a pending attempt (e.g., on success or fatal error)
```
> تعليق: أزِل محاولة معلّقة (مثلاً عند النجاح أو عند خطأ قاتل). [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:100]

```
101:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:101]

```
102:     fun removePendingConnection(id: String) {
```
> يعرّف دالة باسم أزِل اتصالاً معلّقاً (removePendingConnection) تأخذ معاملاً ‎id‎ من نوع سلسلة نصية بلا قيمة معادة صريحة. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:102]

```
103:         pendingConnections.remove(id)
```
> يستدعي ‎remove(id)‎ على الاتصالات المعلّقة لحذف المدخل ذي المفتاح ‎id‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:103]

```
104:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:104]

```
105: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:105]

```
106:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:106]

```
107:      * Abstract: Subclasses must define what "connected" means
```
> تعليق: مجرّد: على الأصناف الفرعية أن تحدّد معنى «متّصل». [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:107]

```
108:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:108]

```
109:     abstract fun isConnected(id: String): Boolean
```
> يعرّف دالة مجرّدة (abstract fun) باسم هل متّصل (isConnected) تأخذ معاملاً ‎id‎ من نوع سلسلة نصية وتعيد قيمة منطقية Boolean، دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:109]

```
110: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:110]

```
111:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:111]

```
112:      * Abstract: Subclasses must implement disconnect logic
```
> تعليق: مجرّد: على الأصناف الفرعية أن تنفّذ منطق قطع الاتصال. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:112]

```
113:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:113]

```
114:     abstract fun disconnect(id: String)
```
> يعرّف دالة مجرّدة باسم اقطع الاتصال (disconnect) تأخذ معاملاً ‎id‎ من نوع سلسلة نصية بلا قيمة معادة صريحة، دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:114]

```
115: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:115]

```
116:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:116]

```
117:      * Abstract: Subclasses report their active connection count
```
> تعليق: مجرّد: تُبلّغ الأصناف الفرعية عن عدد اتصالاتها النشطة. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:117]

```
118:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:118]

```
119:     abstract fun getConnectionCount(): Int
```
> يعرّف دالة مجرّدة باسم احصل على عدد الاتصالات (getConnectionCount) بلا معاملات وتعيد عدداً صحيحاً Int، دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:119]

```
120: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:120]

```
121:     private fun startPeriodicCleanup() {
```
> يعرّف دالة خاصّة باسم بدء التنظيف الدوري (startPeriodicCleanup) بلا معاملات ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:121]

```
122:         scope.launch {
```
> يستدعي ‎launch‎ على النطاق (scope) لإطلاق كوروتين ويفتح اللامدا. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:122]

```
123:             while (isActive) {
```
> يبدأ حلقة ‎while‎ تستمر ما دام هل نشط (isActive) صحيحاً. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:123]

```
124:                 try {
```
> يفتح كتلة ‎try‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:124]

```
125:                     delay(CLEANUP_INTERVAL)
```
> يستدعي دالة التأخير ‎delay‎ بمقدار ‎CLEANUP_INTERVAL‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:125]

```
126:                     if (!isActive) break
```
> يفحص: إن لم يكن هل نشط (isActive) صحيحاً فاكسر الحلقة بـ ‎break‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:126]

```
127: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:127]

```
128:                     // Clean up expired pending connections
```
> تعليق: نظّف الاتصالات المعلّقة المنتهية الصلاحية. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:128]

```
129:                     val expired = pendingConnections.filter { it.value.isExpired() }
```
> يعرّف خاصيّة محليّة باسم المنتهية (expired) ويسندها إلى ناتج ‎filter‎ على الاتصالات المعلّقة الذي يبقي المدخلات التي ‎isExpired()‎ على قيمتها يساوي صحيحاً. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:129]

```
130:                     expired.keys.forEach { pendingConnections.remove(it) }
```
> يمرّ على مفاتيح المنتهية بـ ‎forEach‎ ويستدعي ‎remove(it)‎ على الاتصالات المعلّقة لكل مفتاح. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:130]

```
131: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:131]

```
132:                     if (expired.isNotEmpty()) {
```
> يفحص شرطاً: إن لم تكن المنتهية فارغة ‎isNotEmpty()‎ ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:132]

```
133:                         Log.d(tag, "Cleaned up ${expired.size} expired connection attempts")
```
> يستدعي ‎Log.d‎ بالوسم وبالرسالة «جرى تنظيف ‎${expired.size}‎ محاولة اتصال منتهية الصلاحية». [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:133]

```
134:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:134]

```
135:                 } catch (e: CancellationException) {
```
> يُغلق كتلة ‎try‎ ويفتح كتلة ‎catch‎ تلتقط استثناء الإلغاء (CancellationException) في المتغيّر ‎e‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:135]

```
136:                     break
```
> يكسر الحلقة بـ ‎break‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:136]

```
137:                 } catch (e: Exception) {
```
> يُغلق كتلة ‎catch‎ السابقة ويفتح كتلة ‎catch‎ تلتقط الاستثناء العام (Exception) في المتغيّر ‎e‎. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:137]

```
138:                     Log.w(tag, "Error in periodic cleanup: ${e.message}")
```
> يستدعي ‎Log.w‎ بالوسم وبالرسالة «خطأ في التنظيف الدوري: ‎${e.message}‎». [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:138]

```
139:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:139]

```
140:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:140]

```
141:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:141]

```
142:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:142]

```
143: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshConnectionTracker.kt:143]
