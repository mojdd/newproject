# شريحة — app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt (الأسطر 1–250)

```
1: package com.bitchat.android.net
```
> يُعرِّف اسم الحزمة (package) للملف بأنه‏ com.bitchat.android.net. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:2]

```
3: import android.app.Application
```
> يستورد الصنف Application من حزمة android.app. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف Log (سجلّ) من حزمة android.util. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:4]

```
5: import com.bitchat.android.util.AppConstants
```
> يستورد الصنف AppConstants (ثوابت التطبيق) من حزمة com.bitchat.android.util. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:5]

```
6: import info.guardianproject.arti.ArtiLogListener
```
> يستورد الصنف ArtiLogListener (مستمع سجلّ آرتي) من حزمة info.guardianproject.arti. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:6]

```
7: import info.guardianproject.arti.ArtiProxy
```
> يستورد الصنف ArtiProxy (وكيل آرتي) من حزمة info.guardianproject.arti. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:7]

```
8: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف CoroutineScope (نطاق المتعاونات/الكوروتينات) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:8]

```
9: import kotlinx.coroutines.Dispatchers
```
> يستورد الكائن Dispatchers (الموزِّعات) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:9]

```
10: import kotlinx.coroutines.SupervisorJob
```
> يستورد الدالة SupervisorJob (مهمة مشرفة) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:10]

```
11: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد الصنف MutableStateFlow (تدفّق حالة قابل للتغيير) من حزمة kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:11]

```
12: import kotlinx.coroutines.flow.StateFlow
```
> يستورد الصنف StateFlow (تدفّق الحالة) من حزمة kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:12]

```
13: import kotlinx.coroutines.flow.asStateFlow
```
> يستورد الدالة asStateFlow (تحويل إلى تدفّق حالة) من حزمة kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:13]

```
14: import kotlinx.coroutines.flow.first
```
> يستورد الدالة first (الأول) من حزمة kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:14]

```
15: import kotlinx.coroutines.flow.update
```
> يستورد الدالة update (تحديث) من حزمة kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:15]

```
16: import kotlinx.coroutines.sync.Mutex
```
> يستورد الصنف Mutex (قفل تبادلي) من حزمة kotlinx.coroutines.sync. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:16]

```
17: import kotlinx.coroutines.sync.withLock
```
> يستورد الدالة withLock (تنفيذ مع قفل) من حزمة kotlinx.coroutines.sync. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:17]

```
18: import kotlinx.coroutines.launch
```
> يستورد الدالة launch (إطلاق) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:18]

```
19: import kotlinx.coroutines.delay
```
> يستورد الدالة delay (تأخير) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:19]

```
20: import kotlinx.coroutines.Job
```
> يستورد الصنف Job (مهمة) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:20]

```
21: import kotlinx.coroutines.withTimeoutOrNull
```
> يستورد الدالة withTimeoutOrNull (تنفيذ بمهلة أو إرجاع فارغ) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:21]

```
22: import kotlinx.coroutines.CompletableDeferred
```
> يستورد الصنف CompletableDeferred (مؤجَّل قابل للإكمال) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:22]

```
23: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:23]

```
24: import java.net.InetSocketAddress
```
> يستورد الصنف InetSocketAddress (عنوان مقبس إنترنت) من حزمة java.net. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:24]

```
25: import java.util.concurrent.atomic.AtomicReference
```
> يستورد الصنف AtomicReference (مرجع ذرّي) من حزمة java.util.concurrent.atomic. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:25]

```
26: import java.util.concurrent.atomic.AtomicLong
```
> يستورد الصنف AtomicLong (عدد طويل ذرّي) من حزمة java.util.concurrent.atomic. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:27]

```
28: /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:28]

```
29:  * Tor provider implementation using custom-built Arti (Tor-in-Rust).
```
> تعليق: تنفيذ مزوِّد تور باستخدام آرتي مبنيٍّ خصيصاً (تور-في-رست). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:29]

```
30:  *
```
> تعليق: سطر فارغ داخل كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:30]

```
31:  * This singleton provides Tor anonymity features using a custom Arti build
```
> تعليق: هذا الكائن المُفرد (singleton) يوفّر ميزات إخفاء الهوية لتور باستخدام بناء آرتي مخصّص. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:31]

```
32:  * compiled with 16KB page size support for Google Play compliance.
```
> تعليق: مُترجَم مع دعم حجم صفحة ١٦ كيلوبايت للتوافق مع متجر جوجل بلاي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:32]

```
33:  *
```
> تعليق: سطر فارغ داخل كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:33]

```
34:  * Based on the original TorManager implementation.
```
> تعليق: مبنيٌّ على تنفيذ مدير تور الأصلي (TorManager). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:34]

```
35:  */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:35]

```
36: class ArtiTorManager private constructor() {
```
> يُعرِّف الصنف ArtiTorManager (مدير تور آرتي) ببانٍ (constructor) خاص (private) لا معاملات له، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:36]

```
37:     enum class TorState {
```
> يُعرِّف صنفاً تعدادياً (enum) باسم TorState (حالة تور)، ويفتح جسمه. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:37]

```
38:         OFF,
```
> يُعرِّف عنصر التعداد OFF (مُطفأ). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:38]

```
39:         STARTING,
```
> يُعرِّف عنصر التعداد STARTING (قيد البدء). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:39]

```
40:         BOOTSTRAPPING,
```
> يُعرِّف عنصر التعداد BOOTSTRAPPING (قيد الإقلاع/التهيئة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:40]

```
41:         RUNNING,
```
> يُعرِّف عنصر التعداد RUNNING (قيد التشغيل). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:41]

```
42:         STOPPING,
```
> يُعرِّف عنصر التعداد STOPPING (قيد التوقّف). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:42]

```
43:         ERROR
```
> يُعرِّف عنصر التعداد ERROR (خطأ). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:43]

```
44:     }
```
> إغلاق نطاق (نهاية الصنف التعدادي TorState). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:44]

```
45: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:45]

```
46:     data class TorStatus(
```
> يُعرِّف صنف بيانات (data class) باسم TorStatus (حالة تور التفصيلية)، ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:46]

```
47:         val mode: TorMode = TorMode.OFF,
```
> يُعرِّف خاصيّة ثابتة mode (الوضع) من النوع TorMode بقيمة افتراضية TorMode.OFF. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:47]

```
48:         val running: Boolean = false,
```
> يُعرِّف خاصيّة ثابتة running (يعمل) من النوع المنطقي Boolean بقيمة افتراضية false. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:48]

```
49:         val bootstrapPercent: Int = 0,
```
> يُعرِّف خاصيّة ثابتة bootstrapPercent (نسبة الإقلاع) من النوع الصحيح Int بقيمة افتراضية 0. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:49]

```
50:         val lastLogLine: String = "",
```
> يُعرِّف خاصيّة ثابتة lastLogLine (آخر سطر سجلّ) من النوع النصّي String بقيمة افتراضية نصّ فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:50]

```
51:         val state: TorState = TorState.OFF
```
> يُعرِّف خاصيّة ثابتة state (الحالة) من النوع TorState بقيمة افتراضية TorState.OFF. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:51]

```
52:     )
```
> إغلاق نطاق (نهاية قائمة معاملات صنف البيانات TorStatus). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:52]

```
53: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:53]

```
54:     companion object {
```
> يُعرِّف كائناً مرافقاً (companion object)، ويفتح جسمه. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:54]

```
55:         private const val TAG = "ArtiTorManager"
```
> يُعرِّف ثابتاً خاصّاً TAG (وسم) من النوع النصّي بقيمة "ArtiTorManager". [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:55]

```
56:         private const val DEFAULT_SOCKS_PORT = AppConstants.Tor.DEFAULT_SOCKS_PORT
```
> يُعرِّف ثابتاً خاصّاً DEFAULT_SOCKS_PORT (منفذ سوكس الافتراضي) بقيمة AppConstants.Tor.DEFAULT_SOCKS_PORT. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:56]

```
57:         private const val RESTART_DELAY_MS = AppConstants.Tor.RESTART_DELAY_MS
```
> يُعرِّف ثابتاً خاصّاً RESTART_DELAY_MS (تأخير إعادة التشغيل بالميلي ثانية) بقيمة AppConstants.Tor.RESTART_DELAY_MS. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:57]

```
58:         private const val INACTIVITY_TIMEOUT_MS = AppConstants.Tor.INACTIVITY_TIMEOUT_MS
```
> يُعرِّف ثابتاً خاصّاً INACTIVITY_TIMEOUT_MS (مهلة الخمول بالميلي ثانية) بقيمة AppConstants.Tor.INACTIVITY_TIMEOUT_MS. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:58]

```
59:         private const val MAX_RETRY_ATTEMPTS = AppConstants.Tor.MAX_RETRY_ATTEMPTS
```
> يُعرِّف ثابتاً خاصّاً MAX_RETRY_ATTEMPTS (أقصى عدد محاولات إعادة) بقيمة AppConstants.Tor.MAX_RETRY_ATTEMPTS. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:59]

```
60:         private const val STOP_TIMEOUT_MS = AppConstants.Tor.STOP_TIMEOUT_MS
```
> يُعرِّف ثابتاً خاصّاً STOP_TIMEOUT_MS (مهلة التوقّف بالميلي ثانية) بقيمة AppConstants.Tor.STOP_TIMEOUT_MS. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:60]

```
61: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:61]

```
62:         @Volatile
```
> يضع التعليق التوضيحي @Volatile (متطاير) على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:62]

```
63:         private var INSTANCE: ArtiTorManager? = null
```
> يُعرِّف متغيّراً خاصّاً INSTANCE (المثيل) من النوع ArtiTorManager القابل لأن يكون فارغاً بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:63]

```
64: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:64]

```
65:         fun getInstance(): ArtiTorManager {
```
> يُعرِّف الدالة getInstance (إحضار المثيل) التي تُعيد قيمة من النوع ArtiTorManager، ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:65]

```
66:             return INSTANCE ?: synchronized(this) {
```
> يُعيد INSTANCE إن لم يكن فارغاً، وإلا يدخل كتلة متزامنة (synchronized) على this. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:66]

```
67:                 INSTANCE ?: ArtiTorManager().also { INSTANCE = it }
```
> يُعيد INSTANCE إن لم يكن فارغاً، وإلا يُنشئ ArtiTorManager جديداً ويُسنده عبر also إلى INSTANCE. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:67]

```
68:             }
```
> إغلاق نطاق (نهاية الكتلة المتزامنة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:68]

```
69:         }
```
> إغلاق نطاق (نهاية الدالة getInstance). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:69]

```
70:     }
```
> إغلاق نطاق (نهاية الكائن المرافق). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:70]

```
71: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:71]

```
72:     private val appScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يُعرِّف خاصيّة خاصّة ثابتة appScope (نطاق التطبيق) بقيمة CoroutineScope مبنيّ من Dispatchers.IO مضافاً إليه SupervisorJob. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:72]

```
73: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:73]

```
74:     @Volatile
```
> يضع التعليق التوضيحي @Volatile على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:74]

```
75:     private var initialized = false
```
> يُعرِّف متغيّراً خاصّاً initialized (مُهيَّأ) بقيمة ابتدائية false. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:75]

```
76:     @Volatile
```
> يضع التعليق التوضيحي @Volatile على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:76]

```
77:     private var socksAddr: InetSocketAddress? = null
```
> يُعرِّف متغيّراً خاصّاً socksAddr (عنوان سوكس) من النوع InetSocketAddress القابل لأن يكون فارغاً بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:77]

```
78:     @Volatile
```
> يضع التعليق التوضيحي @Volatile على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:78]

```
79:     private var artiProxy: ArtiProxy? = null
```
> يُعرِّف متغيّراً خاصّاً artiProxy (وكيل آرتي) من النوع ArtiProxy القابل لأن يكون فارغاً بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:79]

```
80:     @Volatile
```
> يضع التعليق التوضيحي @Volatile على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:80]

```
81:     private var lastMode: TorMode = TorMode.OFF
```
> يُعرِّف متغيّراً خاصّاً lastMode (آخر وضع) من النوع TorMode بقيمة ابتدائية TorMode.OFF. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:81]

```
82:     private val applyMutex = Mutex()
```
> يُعرِّف خاصيّة خاصّة ثابتة applyMutex (قفل التطبيق) بقيمة كائن Mutex جديد. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:82]

```
83:     @Volatile
```
> يضع التعليق التوضيحي @Volatile على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:83]

```
84:     private var desiredMode: TorMode = TorMode.OFF
```
> يُعرِّف متغيّراً خاصّاً desiredMode (الوضع المرغوب) من النوع TorMode بقيمة ابتدائية TorMode.OFF. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:84]

```
85:     @Volatile
```
> يضع التعليق التوضيحي @Volatile على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:85]

```
86:     private var currentSocksPort: Int = DEFAULT_SOCKS_PORT
```
> يُعرِّف متغيّراً خاصّاً currentSocksPort (منفذ سوكس الحالي) من النوع الصحيح Int بقيمة ابتدائية DEFAULT_SOCKS_PORT. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:86]

```
87:     @Volatile
```
> يضع التعليق التوضيحي @Volatile على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:87]

```
88:     private var lastLogTime = AtomicLong(0L)
```
> يُعرِّف متغيّراً خاصّاً lastLogTime (وقت آخر سجلّ) بقيمة كائن AtomicLong مبدوء بالقيمة 0L. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:88]

```
89:     @Volatile
```
> يضع التعليق التوضيحي @Volatile على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:89]

```
90:     private var retryAttempts = 0
```
> يُعرِّف متغيّراً خاصّاً retryAttempts (محاولات الإعادة) بقيمة ابتدائية 0. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:90]

```
91:     @Volatile
```
> يضع التعليق التوضيحي @Volatile على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:91]

```
92:     private var bindRetryAttempts = 0
```
> يُعرِّف متغيّراً خاصّاً bindRetryAttempts (محاولات إعادة الربط) بقيمة ابتدائية 0. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:92]

```
93:     private var inactivityJob: Job? = null
```
> يُعرِّف متغيّراً خاصّاً inactivityJob (مهمة الخمول) من النوع Job القابل لأن يكون فارغاً بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:93]

```
94:     private var retryJob: Job? = null
```
> يُعرِّف متغيّراً خاصّاً retryJob (مهمة الإعادة) من النوع Job القابل لأن يكون فارغاً بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:94]

```
95:     private var currentApplication: Application? = null
```
> يُعرِّف متغيّراً خاصّاً currentApplication (التطبيق الحالي) من النوع Application القابل لأن يكون فارغاً بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:95]

```
96: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:96]

```
97:     private enum class LifecycleState { STOPPED, STARTING, RUNNING, STOPPING }
```
> يُعرِّف صنفاً تعدادياً خاصّاً LifecycleState (حالة دورة الحياة) بعناصر STOPPED (متوقّف) وSTARTING (قيد البدء) وRUNNING (قيد التشغيل) وSTOPPING (قيد التوقّف). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:97]

```
98: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:98]

```
99:     @Volatile
```
> يضع التعليق التوضيحي @Volatile على المُعرَّف التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:99]

```
100:     private var lifecycleState: LifecycleState = LifecycleState.STOPPED
```
> يُعرِّف متغيّراً خاصّاً lifecycleState (حالة دورة الحياة) من النوع LifecycleState بقيمة ابتدائية LifecycleState.STOPPED. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:100]

```
101: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:101]

```
102:     private val _statusFlow = MutableStateFlow(
```
> يُعرِّف خاصيّة خاصّة ثابتة ‏_statusFlow (تدفّق الحالة الداخلي) بقيمة MutableStateFlow، ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:102]

```
103:         TorStatus(
```
> يُنشئ كائن TorStatus كقيمة ابتدائية للتدفّق، ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:103]

```
104:             mode = TorMode.OFF,
```
> يضبط الوسيط mode على TorMode.OFF. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:104]

```
105:             running = false,
```
> يضبط الوسيط running على false. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:105]

```
106:             bootstrapPercent = 0,
```
> يضبط الوسيط bootstrapPercent على 0. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:106]

```
107:             lastLogLine = "",
```
> يضبط الوسيط lastLogLine على نصّ فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:107]

```
108:             state = TorState.OFF
```
> يضبط الوسيط state على TorState.OFF. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:108]

```
109:         )
```
> إغلاق نطاق (نهاية قائمة وسائط TorStatus). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:109]

```
110:     )
```
> إغلاق نطاق (نهاية قائمة وسائط MutableStateFlow). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:110]

```
111: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:111]

```
112:     val statusFlow: StateFlow<TorStatus> = _statusFlow.asStateFlow()
```
> يُعرِّف خاصيّة عامّة ثابتة statusFlow (تدفّق الحالة) من النوع StateFlow<TorStatus> بقيمة ناتجة عن استدعاء asStateFlow على ‏_statusFlow. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:112]

```
113: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:113]

```
114:     private val stateChangeDeferred = AtomicReference<CompletableDeferred<TorState>?>(null)
```
> يُعرِّف خاصيّة خاصّة ثابتة stateChangeDeferred (مؤجَّل تغيّر الحالة) من النوع AtomicReference يحمل CompletableDeferred<TorState> قابلاً لأن يكون فارغاً بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:114]

```
115: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:115]

```
116:     fun isProxyEnabled(): Boolean {
```
> يُعرِّف الدالة isProxyEnabled (هل الوكيل مُفعَّل) التي تُعيد قيمة منطقية Boolean، ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:116]

```
117:         val s = _statusFlow.value
```
> يُعرِّف متغيّراً ثابتاً s بقيمة الحالة الحالية ‏_statusFlow.value. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:117]

```
118:         return s.mode != TorMode.OFF && s.running && s.bootstrapPercent >= 100 &&
```
> يُعيد نتيجة شرط مركّب: أن mode لا يساوي TorMode.OFF، وأن running صحيح، وأن bootstrapPercent أكبر من أو يساوي 100، ويتابع الشرط في السطر التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:118]

```
119:                 socksAddr != null && s.state == TorState.RUNNING
```
> يتابع الشرط: أن socksAddr لا يساوي null، وأن state يساوي TorState.RUNNING. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:119]

```
120:     }
```
> إغلاق نطاق (نهاية الدالة isProxyEnabled). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:120]

```
121: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:121]

```
122:     fun init(application: Application) {
```
> يُعرِّف الدالة init (تهيئة) التي تأخذ معاملاً application من النوع Application، ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:122]

```
123:         if (initialized) return
```
> إن كان initialized صحيحاً يخرج من الدالة فوراً. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:123]

```
124:         synchronized(this) {
```
> يدخل كتلة متزامنة (synchronized) على this، ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:124]

```
125:             if (initialized) return
```
> إن كان initialized صحيحاً يخرج من الدالة فوراً (فحص ثانٍ داخل الكتلة المتزامنة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:125]

```
126:             initialized = true
```
> يضبط initialized على القيمة true. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:126]

```
127:             currentApplication = application
```
> يُسند المعامل application إلى المتغيّر currentApplication. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:127]

```
128:             TorPreferenceManager.init(application)
```
> يستدعي الدالة init على TorPreferenceManager (مدير تفضيلات تور) مع المعامل application. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:128]

```
129: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:129]

```
130:             val logListener = ArtiLogListener { logLine ->
```
> يُعرِّف متغيّراً ثابتاً logListener (مستمع السجلّ) بقيمة كائن ArtiLogListener بتعبير لامبدا يأخذ المعامل logLine، ويفتح جسم اللامبدا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:130]

```
131:                 val text = logLine ?: return@ArtiLogListener
```
> يُعرِّف متغيّراً ثابتاً text بقيمة logLine، وإن كان فارغاً يخرج من لامبدا ArtiLogListener. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:131]

```
132:                 val s = text
```
> يُعرِّف متغيّراً ثابتاً s بقيمة text. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:132]

```
133:                 Log.i(TAG, "arti: $s")
```
> يستدعي Log.i (سجلّ معلوماتي) بالوسم TAG والنصّ "arti: $s" حيث يُدرَج محتوى s. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:133]

```
134:                 lastLogTime.set(System.currentTimeMillis())
```
> يستدعي set على lastLogTime بقيمة الوقت الحالي بالميلي ثانية System.currentTimeMillis. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:134]

```
135:                 _statusFlow.update { it.copy(lastLogLine = s) }
```
> يستدعي update على ‏_statusFlow لينسخ الحالة الحالية it مع ضبط lastLogLine على s. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:135]

```
136:                 handleArtiLogLine(s)
```
> يستدعي الدالة handleArtiLogLine (معالجة سطر سجلّ آرتي) مع الوسيط s. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:136]

```
137:             }
```
> إغلاق نطاق (نهاية لامبدا مستمع السجلّ). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:137]

```
138: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:138]

```
139:             artiProxy = ArtiProxy.Builder(application)
```
> يُسند إلى artiProxy نتيجة بناء عبر ArtiProxy.Builder بالمعامل application، ويبدأ سلسلة استدعاءات الباني. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:139]

```
140:                 .setSocksPort(currentSocksPort)
```
> يستدعي setSocksPort (ضبط منفذ سوكس) على الباني بقيمة currentSocksPort. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:140]

```
141:                 .setDnsPort(currentSocksPort + 1)
```
> يستدعي setDnsPort (ضبط منفذ نظام أسماء النطاقات) على الباني بقيمة currentSocksPort مضافاً إليه 1. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:141]

```
142:                 .setLogListener(logListener)
```
> يستدعي setLogListener (ضبط مستمع السجلّ) على الباني بالقيمة logListener. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:142]

```
143:                 .build()
```
> يستدعي build (بناء) على الباني لإنشاء كائن ArtiProxy. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:143]

```
144: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:144]

```
145:             val savedMode = TorPreferenceManager.get(application)
```
> يُعرِّف متغيّراً ثابتاً savedMode (الوضع المحفوظ) بقيمة ناتجة عن استدعاء get على TorPreferenceManager بالمعامل application. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:145]

```
146:             if (savedMode == TorMode.ON) {
```
> إن كان savedMode يساوي TorMode.ON يدخل الكتلة التالية. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:146]

```
147:                 if (currentSocksPort < DEFAULT_SOCKS_PORT) {
```
> إن كان currentSocksPort أصغر من DEFAULT_SOCKS_PORT يدخل الكتلة التالية. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:147]

```
148:                     currentSocksPort = DEFAULT_SOCKS_PORT
```
> يضبط currentSocksPort على DEFAULT_SOCKS_PORT. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:148]

```
149:                 }
```
> إغلاق نطاق (نهاية شرط منفذ سوكس). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:149]

```
150:                 desiredMode = savedMode
```
> يضبط desiredMode على قيمة savedMode. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:150]

```
151:                 socksAddr = InetSocketAddress("127.0.0.1", currentSocksPort)
```
> يضبط socksAddr على كائن InetSocketAddress بالعنوان "127.0.0.1" والمنفذ currentSocksPort. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:151]

```
152:                 try {
```
> يفتح كتلة try (محاولة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:152]

```
153:                     OkHttpProvider.reset()
```
> يستدعي reset (إعادة ضبط) على OkHttpProvider (مزوِّد أوك‌إتش‌تي‌تي‌بي). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:153]

```
154:                 } catch (_: Throwable) {
```
> يلتقط أيّ Throwable (قابل للرمي) متجاهلاً اسمه، ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:154]

```
155:                 }  // Only reset OkHttp during init
```
> إغلاق نطاق (نهاية كتلة catch)؛ تعليق: إعادة ضبط أوك‌إتش‌تي‌تي‌بي فقط أثناء التهيئة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:155]

```
156:             }
```
> إغلاق نطاق (نهاية شرط savedMode == TorMode.ON). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:156]

```
157:             appScope.launch {
```
> يستدعي launch على appScope لإطلاق متعاونة جديدة، ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:157]

```
158:                 applyMode(application, savedMode)
```
> يستدعي الدالة applyMode (تطبيق الوضع) بالمعاملين application وsavedMode. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:158]

```
159:             }
```
> إغلاق نطاق (نهاية المتعاونة المُطلَقة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:159]

```
160: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:160]

```
161:             appScope.launch {
```
> يستدعي launch على appScope لإطلاق متعاونة جديدة، ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:161]

```
162:                 TorPreferenceManager.modeFlow.collect { mode ->
```
> يستدعي collect (جمع) على TorPreferenceManager.modeFlow (تدفّق الوضع) بتعبير لامبدا يأخذ المعامل mode، ويفتح جسم اللامبدا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:162]

```
163:                     applyMode(application, mode)
```
> يستدعي الدالة applyMode بالمعاملين application وmode. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:163]

```
164:                 }
```
> إغلاق نطاق (نهاية لامبدا collect). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:164]

```
165:             }
```
> إغلاق نطاق (نهاية المتعاونة المُطلَقة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:165]

```
166:         }
```
> إغلاق نطاق (نهاية الكتلة المتزامنة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:166]

```
167:     }
```
> إغلاق نطاق (نهاية الدالة init). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:167]

```
168: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:168]

```
169:     fun currentSocksAddress(): InetSocketAddress? = socksAddr
```
> يُعرِّف الدالة currentSocksAddress (عنوان سوكس الحالي) التي تُعيد InetSocketAddress قابلاً لأن يكون فارغاً بقيمة socksAddr. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:169]

```
170: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:170]

```
171:     suspend fun applyMode(application: Application, mode: TorMode) {
```
> يُعرِّف دالة معلَّقة (suspend) باسم applyMode تأخذ المعاملين application من النوع Application وmode من النوع TorMode، ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:171]

```
172:         applyMutex.withLock {
```
> يستدعي withLock على applyMutex لتنفيذ الكتلة تحت القفل، ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:172]

```
173:             try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:173]

```
174:                 desiredMode = mode
```
> يضبط desiredMode على قيمة mode. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:174]

```
175:                 lastMode = mode
```
> يضبط lastMode على قيمة mode. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:175]

```
176:                 val s = _statusFlow.value
```
> يُعرِّف متغيّراً ثابتاً s بقيمة الحالة الحالية ‏_statusFlow.value. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:176]

```
177:                 if (mode == s.mode && mode != TorMode.OFF &&
```
> يفتح شرطاً مركّباً: أن mode يساوي s.mode، وأن mode لا يساوي TorMode.OFF، ويتابع في السطر التالي. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:177]

```
178:                     (lifecycleState == LifecycleState.STARTING || lifecycleState == LifecycleState.RUNNING)
```
> يتابع الشرط: أن lifecycleState يساوي LifecycleState.STARTING أو يساوي LifecycleState.RUNNING. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:178]

```
179:                 ) {
```
> يُغلق قوس الشرط ويفتح كتلة التنفيذ المرتبطة به. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:179]

```
180:                     Log.i(
```
> يبدأ استدعاء Log.i (سجلّ معلوماتي)، ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:180]

```
181:                         TAG,
```
> يمرّر الوسم TAG كوسيط أول. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:181]

```
182:                         "applyMode: already in progress/running mode=$mode, state=$lifecycleState; skip"
```
> يمرّر النصّ "applyMode: already in progress/running mode=$mode, state=$lifecycleState; skip" مع إدراج قيمتي mode وlifecycleState. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:182]

```
183:                     )
```
> إغلاق نطاق (نهاية قائمة وسائط Log.i). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:183]

```
184:                     return
```
> يخرج من الدالة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:184]

```
185:                 }
```
> إغلاق نطاق (نهاية كتلة الشرط المركّب). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:185]

```
186:                 when (mode) {
```
> يفتح تعبير when (عند) على mode للتفريع حسب قيمته. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:186]

```
187:                     TorMode.OFF -> {
```
> يبدأ فرع when للحالة TorMode.OFF، ويفتح كتلته. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:187]

```
188:                         Log.i(TAG, "applyMode: OFF -> stopping tor")
```
> يستدعي Log.i بالوسم TAG والنصّ "applyMode: OFF -> stopping tor". [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:188]

```
189:                         lifecycleState = LifecycleState.STOPPING
```
> يضبط lifecycleState على LifecycleState.STOPPING. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:189]

```
190:                         _statusFlow.value = _statusFlow.value.copy(
```
> يُسند إلى ‏_statusFlow.value نسخة من الحالة الحالية مع تعديلات، ويفتح قائمة الوسائط. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:190]

```
191:                             mode = TorMode.OFF,
```
> يضبط الوسيط mode على TorMode.OFF. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:191]

```
192:                             running = false,
```
> يضبط الوسيط running على false. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:192]

```
193:                             bootstrapPercent = 0,
```
> يضبط الوسيط bootstrapPercent على 0. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:193]

```
194:                             state = TorState.STOPPING
```
> يضبط الوسيط state على TorState.STOPPING. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:194]

```
195:                         )
```
> إغلاق نطاق (نهاية قائمة وسائط copy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:195]

```
196:                         stopArti()
```
> يستدعي الدالة stopArti (إيقاف آرتي). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:196]

```
197:                         waitForStateTransition(target = TorState.OFF, timeoutMs = STOP_TIMEOUT_MS)
```
> يستدعي الدالة waitForStateTransition (انتظار انتقال الحالة) بالوسيط target = TorState.OFF والوسيط timeoutMs = STOP_TIMEOUT_MS. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:197]

```
198:                         socksAddr = null
```
> يضبط socksAddr على null. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:198]

```
199:                         _statusFlow.value = _statusFlow.value.copy(
```
> يُسند إلى ‏_statusFlow.value نسخة من الحالة الحالية مع تعديلات، ويفتح قائمة الوسائط. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:199]

```
200:                             mode = TorMode.OFF,
```
> يضبط الوسيط mode على TorMode.OFF. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:200]

```
201:                             running = false,
```
> يضبط الوسيط running على false. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:201]

```
202:                             bootstrapPercent = 0,
```
> يضبط الوسيط bootstrapPercent على 0. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:202]

```
203:                             state = TorState.OFF
```
> يضبط الوسيط state على TorState.OFF. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:203]

```
204:                         )
```
> إغلاق نطاق (نهاية قائمة وسائط copy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:204]

```
205:                         currentSocksPort = DEFAULT_SOCKS_PORT
```
> يضبط currentSocksPort على DEFAULT_SOCKS_PORT. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:205]

```
206:                         bindRetryAttempts = 0
```
> يضبط bindRetryAttempts على 0. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:206]

```
207:                         lifecycleState = LifecycleState.STOPPED
```
> يضبط lifecycleState على LifecycleState.STOPPED. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:207]

```
208:                         resetNetworkConnections()
```
> يستدعي الدالة resetNetworkConnections (إعادة ضبط اتصالات الشبكة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:208]

```
209:                     }
```
> إغلاق نطاق (نهاية فرع TorMode.OFF). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:209]

```
210: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:210]

```
211:                     TorMode.ON -> {
```
> يبدأ فرع when للحالة TorMode.ON، ويفتح كتلته. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:211]

```
212:                         Log.i(TAG, "applyMode: ON -> starting arti")
```
> يستدعي Log.i بالوسم TAG والنصّ "applyMode: ON -> starting arti". [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:212]

```
213:                         if (currentSocksPort < DEFAULT_SOCKS_PORT) {
```
> إن كان currentSocksPort أصغر من DEFAULT_SOCKS_PORT يدخل الكتلة التالية. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:213]

```
214:                             currentSocksPort = DEFAULT_SOCKS_PORT
```
> يضبط currentSocksPort على DEFAULT_SOCKS_PORT. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:214]

```
215:                         }
```
> إغلاق نطاق (نهاية شرط منفذ سوكس). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:215]

```
216:                         bindRetryAttempts = 0
```
> يضبط bindRetryAttempts على 0. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:216]

```
217:                         lifecycleState = LifecycleState.STARTING
```
> يضبط lifecycleState على LifecycleState.STARTING. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:217]

```
218:                         _statusFlow.value = _statusFlow.value.copy(
```
> يُسند إلى ‏_statusFlow.value نسخة من الحالة الحالية مع تعديلات، ويفتح قائمة الوسائط. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:218]

```
219:                             mode = TorMode.ON,
```
> يضبط الوسيط mode على TorMode.ON. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:219]

```
220:                             running = false,
```
> يضبط الوسيط running على false. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:220]

```
221:                             bootstrapPercent = 0,
```
> يضبط الوسيط bootstrapPercent على 0. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:221]

```
222:                             state = TorState.STARTING
```
> يضبط الوسيط state على TorState.STARTING. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:222]

```
223:                         )
```
> إغلاق نطاق (نهاية قائمة وسائط copy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:223]

```
224:                         socksAddr = InetSocketAddress("127.0.0.1", currentSocksPort)
```
> يضبط socksAddr على كائن InetSocketAddress بالعنوان "127.0.0.1" والمنفذ currentSocksPort. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:224]

```
225:                         resetNetworkConnections()
```
> يستدعي الدالة resetNetworkConnections. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:225]

```
226:                         startArti(application, useDelay = false)
```
> يستدعي الدالة startArti (بدء آرتي) بالمعامل application والوسيط useDelay = false. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:226]

```
227:                         appScope.launch {
```
> يستدعي launch على appScope لإطلاق متعاونة جديدة، ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:227]

```
228:                             waitUntilBootstrapped()
```
> يستدعي الدالة waitUntilBootstrapped (الانتظار حتى اكتمال الإقلاع). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:228]

```
229:                             if (_statusFlow.value.running && desiredMode == TorMode.ON) {
```
> إن كانت running في الحالة الحالية صحيحة وكان desiredMode يساوي TorMode.ON يدخل الكتلة التالية. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:229]

```
230:                                 socksAddr = InetSocketAddress("127.0.0.1", currentSocksPort)
```
> يضبط socksAddr على كائن InetSocketAddress بالعنوان "127.0.0.1" والمنفذ currentSocksPort. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:230]

```
231:                                 Log.i(TAG, "Tor ON: proxy set to ${socksAddr}")
```
> يستدعي Log.i بالوسم TAG والنصّ "Tor ON: proxy set to ${socksAddr}" مع إدراج قيمة socksAddr. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:231]

```
232:                                 resetNetworkConnections()
```
> يستدعي الدالة resetNetworkConnections. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:232]

```
233:                             }
```
> إغلاق نطاق (نهاية شرط running و desiredMode). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:233]

```
234:                         }
```
> إغلاق نطاق (نهاية المتعاونة المُطلَقة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:234]

```
235:                     }
```
> إغلاق نطاق (نهاية فرع TorMode.ON). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:235]

```
236:                 }
```
> إغلاق نطاق (نهاية تعبير when). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:236]

```
237:             } catch (e: Exception) {
```
> يلتقط استثناءً Exception باسم e، ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:237]

```
238:                 Log.e(TAG, "Failed to apply Arti mode: ${e.message}")
```
> يستدعي Log.e (سجلّ خطأ) بالوسم TAG والنصّ "Failed to apply Arti mode: ${e.message}" مع إدراج رسالة الاستثناء. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:238]

```
239:             }
```
> إغلاق نطاق (نهاية كتلة catch). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:239]

```
240:         }
```
> إغلاق نطاق (نهاية كتلة withLock). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:240]

```
241:     }
```
> إغلاق نطاق (نهاية الدالة applyMode). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:241]

```
242: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:242]

```
243:     private suspend fun startArti(application: Application, useDelay: Boolean = false) {
```
> يُعرِّف دالة معلَّقة خاصّة باسم startArti تأخذ المعامل application من النوع Application والمعامل useDelay من النوع المنطقي بقيمة افتراضية false، ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:243]

```
244:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:244]

```
245:             stopArtiAndWait()
```
> يستدعي الدالة stopArtiAndWait (إيقاف آرتي والانتظار). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:245]

```
246:             Log.i(TAG, "Starting Arti on port $currentSocksPort…")
```
> يستدعي Log.i بالوسم TAG والنصّ "Starting Arti on port $currentSocksPort…" مع إدراج قيمة currentSocksPort. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:246]

```
247:             if (useDelay) {
```
> إن كان useDelay صحيحاً يدخل الكتلة التالية. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:247]

```
248:                 delay(RESTART_DELAY_MS)
```
> يستدعي الدالة delay (تأخير) بمقدار RESTART_DELAY_MS. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:248]

```
249:             }
```
> إغلاق نطاق (نهاية شرط useDelay). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:249]

```
250: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:250]
