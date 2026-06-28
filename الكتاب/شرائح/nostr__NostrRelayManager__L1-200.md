# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يُعرِّف اسم الحزمة (package) للملف بأنه com.bitchat.android.nostr. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف Log من android.util. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:3]

```
4: import com.google.gson.Gson
```
> يستورد الصنف Gson من com.google.gson. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:4]

```
5: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد الصنف MutableStateFlow من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:5]

```
6: import kotlinx.coroutines.flow.StateFlow
```
> يستورد الصنف StateFlow من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:6]

```
7: import kotlinx.coroutines.flow.asStateFlow
```
> يستورد الدالة asStateFlow من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:7]

```
8: import com.google.gson.JsonArray
```
> يستورد الصنف JsonArray من com.google.gson. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:8]

```
9: import com.google.gson.JsonParser
```
> يستورد الصنف JsonParser من com.google.gson. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:9]

```
10: import kotlinx.coroutines.*
```
> يستورد كل العناصر العامة من حزمة kotlinx.coroutines باستعمال علامة النجمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:10]

```
11: import okhttp3.*
```
> يستورد كل العناصر العامة من حزمة okhttp3 باستعمال علامة النجمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:11]

```
12: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف ConcurrentHashMap من java.util.concurrent. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:12]

```
13: import java.util.concurrent.TimeUnit
```
> يستورد الصنف TimeUnit من java.util.concurrent. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:13]

```
14: import kotlin.math.min
```
> يستورد الدالة min من kotlin.math. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:14]

```
15: import kotlin.math.pow
```
> يستورد الدالة pow من kotlin.math. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:16]

```
17: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:17]

```
18:  * Manages WebSocket connections to Nostr relays
```
> تعليق: يدير اتصالات WebSocket بمُرحّلات (relays) نوسْتر. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:18]

```
19:  * Compatible with iOS implementation with Android-specific optimizations
```
> تعليق: متوافق مع تنفيذ iOS مع تحسينات خاصة بأندرويد. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:19]

```
20:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:20]

```
21: class NostrRelayManager private constructor() {
```
> يُعرِّف الصنف NostrRelayManager (مدير مُرحّلات نوسْتر) ببانٍ (constructor) خاص private بلا معاملات، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:21]

```
22:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:22]

```
23:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:23]

```
24:         @JvmStatic
```
> يضع الموسوم @JvmStatic على العنصر التالي ليجعله ساكناً عند الاستدعاء من جافا. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:24]

```
25:         val shared = NostrRelayManager()
```
> يُعرِّف الخاصية الثابتة shared ويهيّئها بنسخة جديدة من NostrRelayManager. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:25]

```
26:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:26]

```
27:         private const val TAG = "NostrRelayManager"
```
> يُعرِّف الثابت الخاص TAG بالقيمة النصية "NostrRelayManager". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:27]

```
28:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:28]

```
29:         /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:29]

```
30:          * Get instance for Android compatibility (context-aware calls)
```
> تعليق: احصل على نسخة من أجل توافق أندرويد (استدعاءات واعية بالسياق context). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:30]

```
31:          */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:31]

```
32:         fun getInstance(context: android.content.Context): NostrRelayManager {
```
> يُعرِّف الدالة getInstance التي تأخذ معاملاً context من نوع android.content.Context وتُعيد NostrRelayManager، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:32]

```
33:             return shared
```
> يُعيد الخاصية shared. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:33]

```
34:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:34]

```
35: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:35]

```
36:         // Default relay list (same as iOS)
```
> تعليق: قائمة المُرحّلات الافتراضية (نفسها كما في iOS). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:36]

```
37:         private val DEFAULT_RELAYS = listOf(
```
> يُعرِّف الخاصية الخاصة DEFAULT_RELAYS ويهيّئها بقائمة تُنشأ عبر listOf، ويفتح وسائط القائمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:37]

```
38:             "wss://relay.damus.io",
```
> عنصر نصي في القائمة بقيمة "wss://relay.damus.io". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:38]

```
39:             "wss://relay.primal.net",
```
> عنصر نصي في القائمة بقيمة "wss://relay.primal.net". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:39]

```
40:             "wss://offchain.pub",
```
> عنصر نصي في القائمة بقيمة "wss://offchain.pub". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:40]

```
41:             "wss://nostr21.com"
```
> عنصر نصي في القائمة بقيمة "wss://nostr21.com". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:41]

```
42:         )
```
> إغلاق وسائط دالة listOf. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:42]

```
43:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:43]

```
44:         // Exponential backoff configuration (same as iOS)
```
> تعليق: ضبط التراجع الأُسّي (exponential backoff) (نفسه كما في iOS). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:44]

```
45:         private const val INITIAL_BACKOFF_INTERVAL = com.bitchat.android.util.AppConstants.Nostr.INITIAL_BACKOFF_INTERVAL_MS  // 1 second
```
> يُعرِّف الثابت الخاص INITIAL_BACKOFF_INTERVAL ويهيّئه بقيمة AppConstants.Nostr.INITIAL_BACKOFF_INTERVAL_MS، مع تعليق: ثانية واحدة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:45]

```
46:         private const val MAX_BACKOFF_INTERVAL = com.bitchat.android.util.AppConstants.Nostr.MAX_BACKOFF_INTERVAL_MS    // 5 minutes
```
> يُعرِّف الثابت الخاص MAX_BACKOFF_INTERVAL ويهيّئه بقيمة AppConstants.Nostr.MAX_BACKOFF_INTERVAL_MS، مع تعليق: خمس دقائق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:46]

```
47:         private const val BACKOFF_MULTIPLIER = com.bitchat.android.util.AppConstants.Nostr.BACKOFF_MULTIPLIER
```
> يُعرِّف الثابت الخاص BACKOFF_MULTIPLIER (مُضاعِف التراجع) ويهيّئه بقيمة AppConstants.Nostr.BACKOFF_MULTIPLIER. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:47]

```
48:         private const val MAX_RECONNECT_ATTEMPTS = com.bitchat.android.util.AppConstants.Nostr.MAX_RECONNECT_ATTEMPTS
```
> يُعرِّف الثابت الخاص MAX_RECONNECT_ATTEMPTS (أقصى محاولات إعادة الاتصال) ويهيّئه بقيمة AppConstants.Nostr.MAX_RECONNECT_ATTEMPTS. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:48]

```
49:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:49]

```
50:         // Track gift-wraps we initiated for logging
```
> تعليق: تتبّع أغلفة الهدايا (gift-wraps) التي بدأناها من أجل التسجيل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:50]

```
51:         private val pendingGiftWrapIDs = ConcurrentHashMap.newKeySet<String>()
```
> يُعرِّف الخاصية الخاصة pendingGiftWrapIDs ويهيّئها بمجموعة مفاتيح متزامنة من نوع String عبر ConcurrentHashMap.newKeySet. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:51]

```
52:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:52]

```
53:         fun registerPendingGiftWrap(id: String) {
```
> يُعرِّف الدالة registerPendingGiftWrap التي تأخذ معاملاً id من نوع String، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:53]

```
54:             pendingGiftWrapIDs.add(id)
```
> يستدعي add على pendingGiftWrapIDs لإضافة id إليها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:54]

```
55:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:55]

```
56: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:56]

```
57:         fun defaultRelays(): List<String> = DEFAULT_RELAYS
```
> يُعرِّف الدالة defaultRelays التي تُعيد List<String> وقيمتها DEFAULT_RELAYS باستعمال صيغة المساواة المختصرة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:57]

```
58:     }
```
> إغلاق نطاق (نهاية الكائن المرافق). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:58]

```
59:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:59]

```
60:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:60]

```
61:      * Relay status information
```
> تعليق: معلومات حالة المُرحّل (relay). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:61]

```
62:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:62]

```
63:     data class Relay(
```
> يُعرِّف صنف بيانات (data class) باسم Relay (مُرحّل)، ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:63]

```
64:         val url: String,
```
> يُعرِّف الخاصية url من نوع String (للقراءة فقط). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:64]

```
65:         var isConnected: Boolean = false,
```
> يُعرِّف الخاصية المتغيّرة isConnected من نوع Boolean بقيمة افتراضية false. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:65]

```
66:         var lastError: Throwable? = null,
```
> يُعرِّف الخاصية المتغيّرة lastError من نوع Throwable القابل للعدم بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:66]

```
67:         var lastConnectedAt: Long? = null,
```
> يُعرِّف الخاصية المتغيّرة lastConnectedAt من نوع Long القابل للعدم بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:67]

```
68:         var messagesSent: Int = 0,
```
> يُعرِّف الخاصية المتغيّرة messagesSent من نوع Int بقيمة افتراضية 0. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:68]

```
69:         var messagesReceived: Int = 0,
```
> يُعرِّف الخاصية المتغيّرة messagesReceived من نوع Int بقيمة افتراضية 0. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:69]

```
70:         var reconnectAttempts: Int = 0,
```
> يُعرِّف الخاصية المتغيّرة reconnectAttempts من نوع Int بقيمة افتراضية 0. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:70]

```
71:         var lastDisconnectedAt: Long? = null,
```
> يُعرِّف الخاصية المتغيّرة lastDisconnectedAt من نوع Long القابل للعدم بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:71]

```
72:         var nextReconnectTime: Long? = null
```
> يُعرِّف الخاصية المتغيّرة nextReconnectTime من نوع Long القابل للعدم بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:72]

```
73:     )
```
> إغلاق قائمة معاملات صنف البيانات Relay. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:73]

```
74:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:74]

```
75:     // Published state
```
> تعليق: الحالة المنشورة (Published state). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:75]

```
76:     private val _relays = MutableStateFlow<List<Relay>>(emptyList())
```
> يُعرِّف الخاصية الخاصة ‎_relays ويهيّئها بـ MutableStateFlow من نوع List<Relay> بقيمة ابتدائية قائمة فارغة عبر emptyList. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:76]

```
77:     val relays: StateFlow<List<Relay>> = _relays.asStateFlow()
```
> يُعرِّف الخاصية العامة relays من نوع StateFlow<List<Relay>> وقيمتها ‎_relays.asStateFlow() (نسخة للقراءة فقط). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:77]

```
78:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:78]

```
79:     private val _isConnected = MutableStateFlow<Boolean>(false)
```
> يُعرِّف الخاصية الخاصة ‎_isConnected ويهيّئها بـ MutableStateFlow من نوع Boolean بقيمة ابتدائية false. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:79]

```
80:     val isConnected: StateFlow<Boolean> = _isConnected.asStateFlow()
```
> يُعرِّف الخاصية العامة isConnected من نوع StateFlow<Boolean> وقيمتها ‎_isConnected.asStateFlow() (نسخة للقراءة فقط). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:80]

```
81:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:81]

```
82:     // Internal state
```
> تعليق: الحالة الداخلية (Internal state). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:82]

```
83:     private val relaysList = mutableListOf<Relay>()
```
> يُعرِّف الخاصية الخاصة relaysList ويهيّئها بقائمة قابلة للتغيير من نوع Relay عبر mutableListOf. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:83]

```
84:     private val connections = ConcurrentHashMap<String, WebSocket>()
```
> يُعرِّف الخاصية الخاصة connections ويهيّئها بـ ConcurrentHashMap مفاتيحها String وقيمها WebSocket. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:84]

```
85:     private val subscriptions = ConcurrentHashMap<String, Set<String>>() // relay URL -> subscription IDs
```
> يُعرِّف الخاصية الخاصة subscriptions ويهيّئها بـ ConcurrentHashMap مفاتيحها String وقيمها Set<String>، مع تعليق: عنوان المُرحّل إلى معرّفات الاشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:85]

```
86:     private val messageHandlers = ConcurrentHashMap<String, (NostrEvent) -> Unit>()
```
> يُعرِّف الخاصية الخاصة messageHandlers ويهيّئها بـ ConcurrentHashMap مفاتيحها String وقيمها دوال تأخذ NostrEvent وتُعيد Unit. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:86]

```
87:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:87]

```
88:     // Persistent subscription tracking for robust reconnection
```
> تعليق: تتبّع الاشتراكات الدائم من أجل إعادة اتصال متينة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:88]

```
89:     private val activeSubscriptions = ConcurrentHashMap<String, SubscriptionInfo>() // subscription ID -> info
```
> يُعرِّف الخاصية الخاصة activeSubscriptions ويهيّئها بـ ConcurrentHashMap مفاتيحها String وقيمها SubscriptionInfo، مع تعليق: معرّف الاشتراك إلى المعلومات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:89]

```
90:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:90]

```
91:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:91]

```
92:      * Information about an active subscription that needs to be maintained across reconnections
```
> تعليق: معلومات عن اشتراك نشط يلزم الحفاظ عليه عبر إعادات الاتصال. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:92]

```
93:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:93]

```
94:     data class SubscriptionInfo(
```
> يُعرِّف صنف بيانات باسم SubscriptionInfo (معلومات الاشتراك)، ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:94]

```
95:         val id: String,
```
> يُعرِّف الخاصية id من نوع String (للقراءة فقط). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:95]

```
96:         val filter: NostrFilter,
```
> يُعرِّف الخاصية filter من نوع NostrFilter (مُرشِّح نوسْتر) (للقراءة فقط). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:96]

```
97:         val handler: (NostrEvent) -> Unit,
```
> يُعرِّف الخاصية handler وهي دالة تأخذ NostrEvent وتُعيد Unit (للقراءة فقط). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:97]

```
98:         val targetRelayUrls: Set<String>? = null, // null means all relays
```
> يُعرِّف الخاصية targetRelayUrls من نوع Set<String> القابل للعدم بقيمة افتراضية null، مع تعليق: null يعني كل المُرحّلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:98]

```
99:         val createdAt: Long = System.currentTimeMillis(),
```
> يُعرِّف الخاصية createdAt من نوع Long بقيمة افتراضية ناتج System.currentTimeMillis(). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:99]

```
100:         val originGeohash: String? = null // used for logging and grouping
```
> يُعرِّف الخاصية originGeohash من نوع String القابل للعدم بقيمة افتراضية null، مع تعليق: تُستعمل للتسجيل والتجميع. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:100]

```
101:     )
```
> إغلاق قائمة معاملات صنف البيانات SubscriptionInfo. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:101]

```
102:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:102]

```
103:     // Event deduplication system
```
> تعليق: نظام إزالة تكرار الأحداث (Event deduplication). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:103]

```
104:     private val eventDeduplicator = NostrEventDeduplicator.getInstance()
```
> يُعرِّف الخاصية الخاصة eventDeduplicator (مُزيل التكرار) ويهيّئها بناتج NostrEventDeduplicator.getInstance(). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:104]

```
105:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:105]

```
106:     // Message queue for reliability
```
> تعليق: طابور الرسائل (Message queue) من أجل الموثوقية. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:106]

```
107:     private val messageQueue = mutableListOf<Pair<NostrEvent, List<String>>>()
```
> يُعرِّف الخاصية الخاصة messageQueue ويهيّئها بقائمة قابلة للتغيير من أزواج Pair عناصرها NostrEvent وList<String> عبر mutableListOf. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:107]

```
108:     private val messageQueueLock = Any()
```
> يُعرِّف الخاصية الخاصة messageQueueLock (قفل طابور الرسائل) ويهيّئها بكائن جديد عبر Any(). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:108]

```
109:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:109]

```
110:     // Coroutine scope for background operations
```
> تعليق: نطاق الكوروتين (Coroutine scope) من أجل العمليات في الخلفية. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:110]

```
111:     private val scope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يُعرِّف الخاصية الخاصة scope ويهيّئها بـ CoroutineScope مكوّن من Dispatchers.IO مضافاً إليه SupervisorJob(). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:111]

```
112:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:112]

```
113:     // Subscription validation timer
```
> تعليق: مؤقّت التحقق من الاشتراكات (Subscription validation timer). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:113]

```
114:     private var subscriptionValidationJob: Job? = null
```
> يُعرِّف الخاصية المتغيّرة الخاصة subscriptionValidationJob من نوع Job القابل للعدم بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:114]

```
115:     private val SUBSCRIPTION_VALIDATION_INTERVAL = com.bitchat.android.util.AppConstants.Nostr.SUBSCRIPTION_VALIDATION_INTERVAL_MS // 30 seconds
```
> يُعرِّف الخاصية الخاصة SUBSCRIPTION_VALIDATION_INTERVAL ويهيّئها بقيمة AppConstants.Nostr.SUBSCRIPTION_VALIDATION_INTERVAL_MS، مع تعليق: ثلاثون ثانية. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:115]

```
116:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:116]

```
117:     // OkHttp client for WebSocket connections (via provider to honor Tor)
```
> تعليق: عميل OkHttp لاتصالات WebSocket (عبر مزوّد provider لاحترام Tor). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:117]

```
118:     private val httpClient: OkHttpClient
```
> يُعرِّف الخاصية الخاصة httpClient من نوع OkHttpClient (يتبعها مُحصِّل get في السطر التالي). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:118]

```
119:         get() = com.bitchat.android.net.OkHttpProvider.webSocketClient()
```
> يُعرِّف مُحصِّل (getter) الخاصية httpClient بحيث يُعيد ناتج OkHttpProvider.webSocketClient(). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:119]

```
120:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:120]

```
121:     private val gson by lazy { NostrRequest.createGson() }
```
> يُعرِّف الخاصية الخاصة gson بتهيئة كسولة (lazy) تُعيد ناتج NostrRequest.createGson(). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:121]

```
122:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:122]

```
123:     // Per-geohash relay selection
```
> تعليق: اختيار المُرحّل لكل geohash (per-geohash). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:123]

```
124:     private val geohashToRelays = ConcurrentHashMap<String, Set<String>>() // geohash -> relay URLs
```
> يُعرِّف الخاصية الخاصة geohashToRelays ويهيّئها بـ ConcurrentHashMap مفاتيحها String وقيمها Set<String>، مع تعليق: geohash إلى عناوين المُرحّلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:124]

```
125: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:125]

```
126:     // --- Public API for geohash-specific operation ---
```
> تعليق: واجهة برمجة عامة (Public API) للعملية الخاصة بـ geohash. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:126]

```
127: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:127]

```
128:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:128]

```
129:      * Compute and connect to relays for a given geohash (nearest + optional defaults), cache the mapping.
```
> تعليق: احسب واتصل بالمُرحّلات لِـ geohash معطى (الأقرب + الافتراضيات الاختيارية)، وخزّن الربط في الذاكرة المؤقتة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:129]

```
130:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:130]

```
131:     fun ensureGeohashRelaysConnected(geohash: String, nRelays: Int = 5, includeDefaults: Boolean = false) {
```
> يُعرِّف الدالة ensureGeohashRelaysConnected التي تأخذ geohash من نوع String وnRelays من نوع Int افتراضيه 5 وincludeDefaults من نوع Boolean افتراضيه false، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:131]

```
132:         try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:132]

```
133:             val nearest = RelayDirectory.closestRelaysForGeohash(geohash, nRelays)
```
> يُعرِّف المتغيّر nearest ويهيّئه بناتج RelayDirectory.closestRelaysForGeohash بالوسيطين geohash وnRelays. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:133]

```
134:             val selected = if (includeDefaults) {
```
> يُعرِّف المتغيّر selected ويبدأ إسناده بتعبير شرطي if مبني على includeDefaults، ويفتح فرع الصواب. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:134]

```
135:                 (nearest + Companion.defaultRelays()).toSet()
```
> في فرع الصواب: يحسب اتحاد nearest مع ناتج Companion.defaultRelays() ثم يحوّله إلى مجموعة عبر toSet. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:135]

```
136:             } else nearest.toSet()
```
> يُغلق فرع الصواب، وفي فرع else يحوّل nearest إلى مجموعة عبر toSet. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:136]

```
137:             if (selected.isEmpty()) {
```
> يبدأ شرط if يختبر ما إذا كانت selected فارغة عبر isEmpty، ويفتح جسمه. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:137]

```
138:                 Log.w(TAG, "No relays selected for geohash=$geohash")
```
> يستدعي Log.w بالوسم TAG ورسالة "No relays selected for geohash=$geohash" مع إدراج قيمة geohash. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:138]

```
139:                 return
```
> يُعيد من الدالة بلا قيمة (return). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:139]

```
140:             }
```
> إغلاق نطاق (نهاية شرط if). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:140]

```
141:             geohashToRelays[geohash] = selected
```
> يُسند selected إلى المفتاح geohash في الخريطة geohashToRelays. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:141]

```
142:             Log.i(TAG, "🌐 Geohash $geohash using ${selected.size} relays: ${selected.joinToString()}")
```
> يستدعي Log.i بالوسم TAG ورسالة تتضمن geohash وحجم selected عبر selected.size والقائمة المجمّعة عبر selected.joinToString(). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:142]

```
143:             ensureConnectionsFor(selected)
```
> يستدعي الدالة ensureConnectionsFor بالوسيط selected. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:143]

```
144:         } catch (e: Exception) {
```
> يُغلق كتلة try ويفتح كتلة catch التي تلتقط استثناءً e من نوع Exception. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:144]

```
145:             Log.e(TAG, "Failed to ensure relays for $geohash: ${e.message}")
```
> يستدعي Log.e بالوسم TAG ورسالة "Failed to ensure relays for $geohash: ${e.message}" مع إدراج geohash ونص الاستثناء e.message. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:145]

```
146:         }
```
> إغلاق نطاق (نهاية كتلة catch). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:146]

```
147:     }
```
> إغلاق نطاق (نهاية الدالة ensureGeohashRelaysConnected). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:147]

```
148: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:148]

```
149:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:149]

```
150:      * Get relays mapped to a geohash (empty list if none configured).
```
> تعليق: احصل على المُرحّلات المربوطة بـ geohash (قائمة فارغة إن لم يُضبط أي منها). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:150]

```
151:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:151]

```
152:     fun getRelaysForGeohash(geohash: String): List<String> {
```
> يُعرِّف الدالة getRelaysForGeohash التي تأخذ geohash من نوع String وتُعيد List<String>، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:152]

```
153:         return geohashToRelays[geohash]?.toList() ?: emptyList()
```
> يُعيد ناتج geohashToRelays[geohash] محوّلاً إلى قائمة عبر toList، أو قائمة فارغة عبر emptyList عند العدم باستعمال معامل إلفيس ‎?:‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:153]

```
154:     }
```
> إغلاق نطاق (نهاية الدالة getRelaysForGeohash). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:154]

```
155: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:155]

```
156:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:156]

```
157:      * Subscribe with explicit geohash routing; ensures connections exist, then targets only those relays.
```
> تعليق: اشترك مع توجيه geohash صريح؛ يضمن وجود الاتصالات ثم يستهدف تلك المُرحّلات فقط. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:157]

```
158:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:158]

```
159:     fun subscribeForGeohash(
```
> يُعرِّف الدالة subscribeForGeohash ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:159]

```
160:         geohash: String,
```
> يُعرِّف المعامل geohash من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:160]

```
161:         filter: NostrFilter,
```
> يُعرِّف المعامل filter من نوع NostrFilter. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:161]

```
162:         id: String = generateSubscriptionId(),
```
> يُعرِّف المعامل id من نوع String بقيمة افتراضية ناتج generateSubscriptionId(). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:162]

```
163:         handler: (NostrEvent) -> Unit,
```
> يُعرِّف المعامل handler وهو دالة تأخذ NostrEvent وتُعيد Unit. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:163]

```
164:         includeDefaults: Boolean = false,
```
> يُعرِّف المعامل includeDefaults من نوع Boolean بقيمة افتراضية false. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:164]

```
165:         nRelays: Int = 5
```
> يُعرِّف المعامل nRelays من نوع Int بقيمة افتراضية 5. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:165]

```
166:     ): String {
```
> يُغلق قائمة المعاملات ويحدّد نوع الإرجاع String ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:166]

```
167:         ensureGeohashRelaysConnected(geohash, nRelays, includeDefaults)
```
> يستدعي الدالة ensureGeohashRelaysConnected بالوسائط geohash وnRelays وincludeDefaults. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:167]

```
168:         val relayUrls = getRelaysForGeohash(geohash)
```
> يُعرِّف المتغيّر relayUrls ويهيّئه بناتج getRelaysForGeohash بالوسيط geohash. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:168]

```
169:         Log.d(TAG, "📡 Subscribing id=$id for geohash=$geohash on ${relayUrls.size} relays")
```
> يستدعي Log.d بالوسم TAG ورسالة تتضمن id وgeohash وحجم relayUrls عبر relayUrls.size. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:169]

```
170:         return subscribe(
```
> يبدأ إرجاع ناتج استدعاء الدالة subscribe، ويفتح وسائطها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:170]

```
171:             filter = filter,
```
> يمرّر الوسيط المسمّى filter بقيمة filter إلى subscribe. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:171]

```
172:             id = id,
```
> يمرّر الوسيط المسمّى id بقيمة id إلى subscribe. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:172]

```
173:             handler = handler,
```
> يمرّر الوسيط المسمّى handler بقيمة handler إلى subscribe. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:173]

```
174:             targetRelayUrls = relayUrls
```
> يمرّر الوسيط المسمّى targetRelayUrls بقيمة relayUrls إلى subscribe. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:174]

```
175:         ).also {
```
> يُغلق وسائط subscribe ويربط دالة also على الناتج، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:175]

```
176:             // update origin geohash for this subscription
```
> تعليق: حدّث geohash الأصل لهذا الاشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:176]

```
177:             activeSubscriptions[it]?.let { sub ->
```
> يصل إلى activeSubscriptions بالمفتاح it (ناتج subscribe) ويستدعي let عليه عند عدم العدم مسمّياً العنصر sub، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:177]

```
178:                 activeSubscriptions[it] = sub.copy(originGeohash = geohash)
```
> يُسند إلى activeSubscriptions عند المفتاح it نسخة من sub عبر copy مع تعيين originGeohash إلى geohash. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:178]

```
179:             }
```
> إغلاق نطاق (نهاية كتلة let). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:179]

```
180:         }
```
> إغلاق نطاق (نهاية كتلة also). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:180]

```
181:     }
```
> إغلاق نطاق (نهاية الدالة subscribeForGeohash). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:181]

```
182: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:182]

```
183:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:183]

```
184:      * Send an event specifically to a geohash's relays (+ optional defaults).
```
> تعليق: أرسل حدثاً تحديداً إلى مُرحّلات geohash (+ الافتراضيات الاختيارية). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:184]

```
185:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:185]

```
186:     fun sendEventToGeohash(event: NostrEvent, geohash: String, includeDefaults: Boolean = false, nRelays: Int = 5) {
```
> يُعرِّف الدالة sendEventToGeohash التي تأخذ event من نوع NostrEvent وgeohash من نوع String وincludeDefaults من نوع Boolean افتراضيه false وnRelays من نوع Int افتراضيه 5، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:186]

```
187:         ensureGeohashRelaysConnected(geohash, nRelays, includeDefaults)
```
> يستدعي الدالة ensureGeohashRelaysConnected بالوسائط geohash وnRelays وincludeDefaults. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:187]

```
188:         val relayUrls = getRelaysForGeohash(geohash)
```
> يُعرِّف المتغيّر relayUrls ويهيّئه بناتج getRelaysForGeohash بالوسيط geohash. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:188]

```
189:         if (relayUrls.isEmpty()) {
```
> يبدأ شرط if يختبر ما إذا كانت relayUrls فارغة عبر isEmpty، ويفتح جسمه. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:189]

```
190:             Log.w(TAG, "No target relays to send event for geohash=$geohash; falling back to defaults")
```
> يستدعي Log.w بالوسم TAG ورسالة "No target relays to send event for geohash=$geohash; falling back to defaults" مع إدراج geohash. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:190]

```
191:             sendEvent(event, Companion.defaultRelays())
```
> يستدعي الدالة sendEvent بالوسيطين event وناتج Companion.defaultRelays(). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:191]

```
192:             return
```
> يُعيد من الدالة بلا قيمة (return). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:192]

```
193:         }
```
> إغلاق نطاق (نهاية شرط if). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:193]

```
194:         Log.v(TAG, "📤 Sending event kind=${event.kind} to ${relayUrls.size} relays for geohash=$geohash")
```
> يستدعي Log.v بالوسم TAG ورسالة تتضمن نوع الحدث event.kind وحجم relayUrls عبر relayUrls.size وgeohash. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:194]

```
195:         sendEvent(event, relayUrls)
```
> يستدعي الدالة sendEvent بالوسيطين event وrelayUrls. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:195]

```
196:     }
```
> إغلاق نطاق (نهاية الدالة sendEventToGeohash). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:196]

```
197: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:197]

```
198:     // --- Internal helpers ---
```
> تعليق: مساعدات داخلية (Internal helpers). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:198]

```
199: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:199]

```
200:     private fun ensureConnectionsFor(relayUrls: Set<String>) {
```
> يُعرِّف الدالة الخاصة ensureConnectionsFor التي تأخذ relayUrls من نوع Set<String>، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:200]
