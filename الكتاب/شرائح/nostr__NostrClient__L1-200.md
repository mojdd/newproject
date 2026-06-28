# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrClient.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يعرّف الحزمة (package) باسم com.bitchat.android.nostr. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف Context من android.content. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف Log (السِجِل) من android.util. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:4]

```
5: import kotlinx.coroutines.*
```
> يستورد كل أعضاء حزمة kotlinx.coroutines (الإجراءات المتزامنة). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:5]

```
6: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد الصنف MutableStateFlow (تدفّق حالة قابل للتغيير) من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:6]

```
7: import kotlinx.coroutines.flow.StateFlow
```
> يستورد الصنف StateFlow (تدفّق حالة) من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:7]

```
8: import kotlinx.coroutines.flow.asStateFlow
```
> يستورد الدالة asStateFlow (تحويل إلى تدفّق حالة) من kotlinx.coroutines.flow. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:9]

```
10: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:10]

```
11:  * High-level Nostr client that manages identity, connections, and messaging
```
> تعليق: عميل Nostr عالي المستوى يدير الهوية والاتصالات والمراسلة. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:11]

```
12:  * Provides a simple API for the rest of the application
```
> تعليق: يوفّر واجهة برمجية بسيطة لبقية التطبيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:12]

```
13:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:13]

```
14: class NostrClient private constructor(private val context: Context) {
```
> يعرّف الصنف NostrClient (عميل نوستر) ببانٍ خاص (private constructor) يأخذ معاملاً خاصاً context من نوع Context. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:14]

```
15:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:15]

```
16:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:16]

```
17:         private const val TAG = "NostrClient"
```
> يعرّف ثابتاً خاصاً TAG (الوسم) بقيمة نصية "NostrClient". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:17]

```
18:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:18]

```
19:         @Volatile
```
> يضع التعليمة التوضيحية ‪@Volatile‬ (متطاير). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:19]

```
20:         private var INSTANCE: NostrClient? = null
```
> يعرّف متغيّراً خاصاً INSTANCE (النسخة) من نوع NostrClient قابل للعدم بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:20]

```
21:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:21]

```
22:         fun getInstance(context: Context): NostrClient {
```
> يعرّف الدالة getInstance (جلب النسخة) تأخذ context من نوع Context وتعيد NostrClient. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:22]

```
23:             return INSTANCE ?: synchronized(this) {
```
> يعيد INSTANCE إن لم تكن null، وإلا يدخل كتلة متزامنة synchronized على this. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:23]

```
24:                 INSTANCE ?: NostrClient(context.applicationContext).also { INSTANCE = it }
```
> يعيد INSTANCE إن لم تكن null، وإلا ينشئ NostrClient بسياق التطبيق context.applicationContext ويسنده إلى INSTANCE عبر also. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:24]

```
25:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:25]

```
26:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:26]

```
27:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:27]

```
28:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:28]

```
29:     // Core components
```
> تعليق: المكوّنات الأساسية. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:29]

```
30:     private val relayManager = NostrRelayManager.shared
```
> يعرّف متغيّراً ثابتاً خاصاً relayManager (مدير المُرحِّلات) بإسناد NostrRelayManager.shared. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:30]

```
31:     private var currentIdentity: NostrIdentity? = null
```
> يعرّف متغيّراً خاصاً currentIdentity (الهوية الحالية) من نوع NostrIdentity قابل للعدم بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:31]

```
32:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:32]

```
33:     // Client state
```
> تعليق: حالة العميل. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:33]

```
34:     private val _isInitialized = MutableStateFlow(false)
```
> يعرّف متغيّراً ثابتاً خاصاً ‪_isInitialized‬ (هل تم التهيئة) كتدفّق حالة قابل للتغيير بقيمة ابتدائية false. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:34]

```
35:     val isInitialized: StateFlow<Boolean> = _isInitialized.asStateFlow()
```
> يعرّف متغيّراً ثابتاً isInitialized من نوع StateFlow<Boolean> بإسناد ‪_isInitialized.asStateFlow()‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:35]

```
36:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:36]

```
37:     private val _currentNpub = MutableStateFlow<String?>(null)
```
> يعرّف متغيّراً ثابتاً خاصاً ‪_currentNpub‬ (المفتاح العام الحالي npub) كتدفّق حالة قابل للتغيير من نوع String قابل للعدم بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:37]

```
38:     val currentNpub: StateFlow<String?> = _currentNpub.asStateFlow()
```
> يعرّف متغيّراً ثابتاً currentNpub من نوع StateFlow<String?> بإسناد ‪_currentNpub.asStateFlow()‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:38]

```
39:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:39]

```
40:     // Message processing
```
> تعليق: معالجة الرسائل. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:40]

```
41:     private val scope = CoroutineScope(Dispatchers.Main + SupervisorJob())
```
> يعرّف متغيّراً ثابتاً خاصاً scope (النطاق) كـ CoroutineScope بمُرسِل Dispatchers.Main مضافاً إليه SupervisorJob. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:41]

```
42:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:42]

```
43:     init {
```
> يفتح كتلة التهيئة init. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:43]

```
44:         Log.d(TAG, "Initializing Nostr client")
```
> يستدعي Log.d (سجل تنقيح) بالوسم TAG والرسالة "Initializing Nostr client". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:44]

```
45:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:45]

```
46:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:46]

```
47:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:47]

```
48:      * Initialize the Nostr client with identity and relay connections
```
> تعليق: تهيئة عميل Nostr بالهوية واتصالات المُرحِّلات. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:48]

```
49:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:49]

```
50:     fun initialize() {
```
> يعرّف الدالة initialize (تهيئة) بلا معاملات. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:50]

```
51:         scope.launch {
```
> يطلق إجراءً متزامناً عبر scope.launch. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:51]

```
52:             try {
```
> يفتح كتلة try (محاولة). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:52]

```
53:                 // Load or create identity
```
> تعليق: تحميل الهوية أو إنشاؤها. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:53]

```
54:                 currentIdentity = NostrIdentityBridge.getCurrentNostrIdentity(context)
```
> يسند إلى currentIdentity نتيجة ‪NostrIdentityBridge.getCurrentNostrIdentity(context)‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:54]

```
55:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:55]

```
56:                 if (currentIdentity != null) {
```
> يبدأ شرطاً if يتحقق أن currentIdentity ليست null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:56]

```
57:                     _currentNpub.value = currentIdentity!!.npub
```
> يسند إلى ‪_currentNpub.value‬ القيمة ‪currentIdentity!!.npub‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:57]

```
58:                     Log.i(TAG, "✅ Nostr identity loaded: ${currentIdentity!!.getShortNpub()}")
```
> يستدعي Log.i (سجل معلومات) بالوسم TAG والرسالة "✅ Nostr identity loaded: " مع ‪currentIdentity!!.getShortNpub()‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:58]

```
59:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:59]

```
60:                     // Connect to relays
```
> تعليق: الاتصال بالمُرحِّلات. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:60]

```
61:                     relayManager.connect()
```
> يستدعي ‪relayManager.connect()‬ (اتصال). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:61]

```
62:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:62]

```
63:                     _isInitialized.value = true
```
> يسند إلى ‪_isInitialized.value‬ القيمة true. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:63]

```
64:                     Log.i(TAG, "✅ Nostr client initialized successfully")
```
> يستدعي Log.i بالوسم TAG والرسالة "✅ Nostr client initialized successfully". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:64]

```
65:                 } else {
```
> يبدأ فرع else للشرط السابق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:65]

```
66:                     Log.e(TAG, "❌ Failed to load/create Nostr identity")
```
> يستدعي Log.e (سجل خطأ) بالوسم TAG والرسالة "❌ Failed to load/create Nostr identity". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:66]

```
67:                     _isInitialized.value = false
```
> يسند إلى ‪_isInitialized.value‬ القيمة false. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:67]

```
68:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:68]

```
69:             } catch (e: Exception) {
```
> يبدأ كتلة catch تلتقط استثناءً e من نوع Exception. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:69]

```
70:                 Log.e(TAG, "❌ Failed to initialize Nostr client: ${e.message}")
```
> يستدعي Log.e بالوسم TAG والرسالة "❌ Failed to initialize Nostr client: " مع ‪e.message‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:70]

```
71:                 _isInitialized.value = false
```
> يسند إلى ‪_isInitialized.value‬ القيمة false. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:71]

```
72:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:72]

```
73:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:73]

```
74:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:74]

```
75:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:75]

```
76:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:76]

```
77:      * Shutdown the client and disconnect from relays
```
> تعليق: إيقاف العميل وقطع الاتصال عن المُرحِّلات. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:77]

```
78:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:78]

```
79:     fun shutdown() {
```
> يعرّف الدالة shutdown (إيقاف) بلا معاملات. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:79]

```
80:         Log.d(TAG, "Shutting down Nostr client")
```
> يستدعي Log.d بالوسم TAG والرسالة "Shutting down Nostr client". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:80]

```
81:         relayManager.disconnect()
```
> يستدعي ‪relayManager.disconnect()‬ (قطع الاتصال). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:81]

```
82:         _isInitialized.value = false
```
> يسند إلى ‪_isInitialized.value‬ القيمة false. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:82]

```
83:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:83]

```
84:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:84]

```
85:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:85]

```
86:      * Send a private message using NIP-17
```
> تعليق: إرسال رسالة خاصة باستخدام NIP-17. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:86]

```
87:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:87]

```
88:     fun sendPrivateMessage(
```
> يعرّف الدالة sendPrivateMessage (إرسال رسالة خاصة) وتبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:88]

```
89:         content: String,
```
> يعرّف المعامل content (المحتوى) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:89]

```
90:         recipientNpub: String,
```
> يعرّف المعامل recipientNpub (مفتاح المستلم npub) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:90]

```
91:         onSuccess: (() -> Unit)? = null,
```
> يعرّف المعامل onSuccess (عند النجاح) كدالة بلا معاملات تعيد Unit وقابلة للعدم بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:91]

```
92:         onError: ((String) -> Unit)? = null
```
> يعرّف المعامل onError (عند الخطأ) كدالة تأخذ String وتعيد Unit وقابلة للعدم بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:92]

```
93:     ) {
```
> يغلق قائمة المعاملات ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:93]

```
94:         val identity = currentIdentity
```
> يعرّف متغيّراً ثابتاً identity بإسناد currentIdentity. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:94]

```
95:         if (identity == null) {
```
> يبدأ شرطاً if يتحقق أن identity تساوي null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:95]

```
96:             onError?.invoke("Nostr client not initialized")
```
> يستدعي onError إن لم تكن null عبر invoke بالرسالة "Nostr client not initialized". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:96]

```
97:             return
```
> يعيد (يخرج من الدالة) بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:97]

```
98:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:98]

```
99:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:99]

```
100:         scope.launch {
```
> يطلق إجراءً متزامناً عبر scope.launch. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:100]

```
101:             try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:101]

```
102:                 // Decode recipient npub to hex pubkey
```
> تعليق: فكّ ترميز npub المستلم إلى مفتاح عام سداسي عشري. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:102]

```
103:                 val (hrp, pubkeyBytes) = Bech32.decode(recipientNpub)
```
> يعرّف متغيّرين ثابتين hrp وpubkeyBytes عبر تفكيك نتيجة ‪Bech32.decode(recipientNpub)‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:103]

```
104:                 if (hrp != "npub") {
```
> يبدأ شرطاً if يتحقق أن hrp لا يساوي "npub". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:104]

```
105:                     onError?.invoke("Invalid npub format")
```
> يستدعي onError إن لم تكن null عبر invoke بالرسالة "Invalid npub format". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:105]

```
106:                     return@launch
```
> يعيد من كتلة launch (يخرج من الإجراء المتزامن). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:106]

```
107:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:107]

```
108:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:108]

```
109:                 val recipientPubkeyHex = pubkeyBytes.toHexString()
```
> يعرّف متغيّراً ثابتاً recipientPubkeyHex بإسناد ‪pubkeyBytes.toHexString()‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:109]

```
110:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:110]

```
111:                 // Create and send gift wraps (receiver and sender copies)
```
> تعليق: إنشاء وإرسال أغلفة الهدية (نسخ المستلم والمرسل). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:111]

```
112:                 val giftWraps = NostrProtocol.createPrivateMessage(
```
> يعرّف متغيّراً ثابتاً giftWraps (أغلفة الهدية) بإسناد ناتج استدعاء ‪NostrProtocol.createPrivateMessage(...)‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:112]

```
113:                     content = content,
```
> يمرّر الوسيط content بالقيمة content. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:113]

```
114:                     recipientPubkey = recipientPubkeyHex,
```
> يمرّر الوسيط recipientPubkey بالقيمة recipientPubkeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:114]

```
115:                     senderIdentity = identity
```
> يمرّر الوسيط senderIdentity بالقيمة identity. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:115]

```
116:                 )
```
> يغلق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:116]

```
117:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:117]

```
118:                 // Track and send all gift wraps
```
> تعليق: تتبّع وإرسال كل أغلفة الهدية. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:118]

```
119:                 giftWraps.forEach { wrap ->
```
> يكرّر على عناصر giftWraps عبر forEach بمعامل wrap. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:119]

```
120:                     NostrRelayManager.registerPendingGiftWrap(wrap.id)
```
> يستدعي ‪NostrRelayManager.registerPendingGiftWrap(wrap.id)‬ (تسجيل غلاف هدية معلّق) بمعرّف الغلاف. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:120]

```
121:                     relayManager.sendEvent(wrap)
```
> يستدعي ‪relayManager.sendEvent(wrap)‬ (إرسال حدث) بالغلاف wrap. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:121]

```
122:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:122]

```
123:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:123]

```
124:                 Log.i(TAG, "📤 Sent private message to ${recipientNpub.take(16)}...")
```
> يستدعي Log.i بالوسم TAG والرسالة "📤 Sent private message to " مع ‪recipientNpub.take(16)‬ متبوعاً بـ "...". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:124]

```
125:                 onSuccess?.invoke()
```
> يستدعي onSuccess إن لم تكن null عبر invoke بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:125]

```
126:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:126]

```
127:             } catch (e: Exception) {
```
> يبدأ كتلة catch تلتقط استثناءً e من نوع Exception. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:127]

```
128:                 Log.e(TAG, "❌ Failed to send private message: ${e.message}")
```
> يستدعي Log.e بالوسم TAG والرسالة "❌ Failed to send private message: " مع ‪e.message‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:128]

```
129:                 onError?.invoke("Failed to send message: ${e.message}")
```
> يستدعي onError إن لم تكن null عبر invoke بالرسالة "Failed to send message: " مع ‪e.message‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:129]

```
130:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:130]

```
131:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:131]

```
132:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:132]

```
133:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:133]

```
134:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:134]

```
135:      * Subscribe to private messages for current identity
```
> تعليق: الاشتراك في الرسائل الخاصة للهوية الحالية. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:135]

```
136:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:136]

```
137:     fun subscribeToPrivateMessages(handler: (content: String, senderNpub: String, timestamp: Int) -> Unit) {
```
> يعرّف الدالة subscribeToPrivateMessages (الاشتراك في الرسائل الخاصة) بمعامل handler (معالج) من نوع دالة تأخذ content من نوع String وsenderNpub من نوع String وtimestamp من نوع Int وتعيد Unit. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:137]

```
138:         val identity = currentIdentity
```
> يعرّف متغيّراً ثابتاً identity بإسناد currentIdentity. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:138]

```
139:         if (identity == null) {
```
> يبدأ شرطاً if يتحقق أن identity تساوي null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:139]

```
140:             Log.e(TAG, "Cannot subscribe to private messages: client not initialized")
```
> يستدعي Log.e بالوسم TAG والرسالة "Cannot subscribe to private messages: client not initialized". [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:140]

```
141:             return
```
> يعيد (يخرج من الدالة) بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:141]

```
142:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:142]

```
143:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:143]

```
144:         val filter = NostrFilter.giftWrapsFor(
```
> يعرّف متغيّراً ثابتاً filter (المُرشِّح) بإسناد ناتج استدعاء ‪NostrFilter.giftWrapsFor(...)‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:144]

```
145:             pubkey = identity.publicKeyHex,
```
> يمرّر الوسيط pubkey بالقيمة ‪identity.publicKeyHex‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:145]

```
146:             since = System.currentTimeMillis() - 172800000L // Last 48 hours (align with NIP-17 randomization)
```
> يمرّر الوسيط since بالقيمة ‪System.currentTimeMillis()‬ مطروحاً منها 172800000L، مع تعليق: آخر 48 ساعة (محاذاةً لعشوائية NIP-17). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:146]

```
147:         )
```
> يغلق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:147]

```
148:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:148]

```
149:         relayManager.subscribe(filter, "private-messages", { giftWrap ->
```
> يستدعي ‪relayManager.subscribe(...)‬ (اشتراك) بالمُرشِّح filter ومعرّف "private-messages" ودالة تستقبل giftWrap. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:149]

```
150:             scope.launch {
```
> يطلق إجراءً متزامناً عبر scope.launch. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:150]

```
151:                 handlePrivateMessage(giftWrap, handler)
```
> يستدعي ‪handlePrivateMessage(giftWrap, handler)‬ (معالجة رسالة خاصة) بالغلاف giftWrap والمعالج handler. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:151]

```
152:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:152]

```
153:         })
```
> يغلق دالة الاستقبال ويغلق قائمة وسائط subscribe. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:153]

```
154:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:154]

```
155:         Log.i(TAG, "🔑 Subscribed to private messages for: ${identity.getShortNpub()}")
```
> يستدعي Log.i بالوسم TAG والرسالة "🔑 Subscribed to private messages for: " مع ‪identity.getShortNpub()‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:155]

```
156:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:156]

```
157:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:157]

```
158:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:158]

```
159:      * Send a public message to a geohash channel
```
> تعليق: إرسال رسالة عامة إلى قناة geohash. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:159]

```
160:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:160]

```
161:     fun sendGeohashMessage(
```
> يعرّف الدالة sendGeohashMessage (إرسال رسالة geohash) وتبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:161]

```
162:         content: String,
```
> يعرّف المعامل content من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:162]

```
163:         geohash: String,
```
> يعرّف المعامل geohash من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:163]

```
164:         nickname: String? = null,
```
> يعرّف المعامل nickname (الاسم المستعار) من نوع String قابل للعدم بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:164]

```
165:         onSuccess: (() -> Unit)? = null,
```
> يعرّف المعامل onSuccess كدالة بلا معاملات تعيد Unit وقابلة للعدم بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:165]

```
166:         onError: ((String) -> Unit)? = null
```
> يعرّف المعامل onError كدالة تأخذ String وتعيد Unit وقابلة للعدم بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:166]

```
167:     ) {
```
> يغلق قائمة المعاملات ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:167]

```
168:         scope.launch {
```
> يطلق إجراءً متزامناً عبر scope.launch. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:168]

```
169:             try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:169]

```
170:                 // Derive geohash-specific identity
```
> تعليق: اشتقاق هوية خاصة بـ geohash. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:170]

```
171:                 val geohashIdentity = NostrIdentityBridge.deriveIdentity(geohash, context)
```
> يعرّف متغيّراً ثابتاً geohashIdentity بإسناد ‪NostrIdentityBridge.deriveIdentity(geohash, context)‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:171]

```
172:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:172]

```
173:                 // Create ephemeral event (with PoW if enabled)
```
> تعليق: إنشاء حدث عابر (مع إثبات العمل PoW إن كان مفعّلاً). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:173]

```
174:                 val event = NostrProtocol.createEphemeralGeohashEvent(
```
> يعرّف متغيّراً ثابتاً event (حدث) بإسناد ناتج استدعاء ‪NostrProtocol.createEphemeralGeohashEvent(...)‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:174]

```
175:                     content = content,
```
> يمرّر الوسيط content بالقيمة content. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:175]

```
176:                     geohash = geohash,
```
> يمرّر الوسيط geohash بالقيمة geohash. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:176]

```
177:                     senderIdentity = geohashIdentity,
```
> يمرّر الوسيط senderIdentity بالقيمة geohashIdentity. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:177]

```
178:                     nickname = nickname
```
> يمرّر الوسيط nickname بالقيمة nickname. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:178]

```
179:                 )
```
> يغلق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:179]

```
180:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:180]

```
181:                 relayManager.sendEvent(event)
```
> يستدعي ‪relayManager.sendEvent(event)‬ (إرسال حدث) بالحدث event. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:181]

```
182:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:182]

```
183:                 Log.i(TAG, "📤 Sent geohash message to #$geohash")
```
> يستدعي Log.i بالوسم TAG والرسالة "📤 Sent geohash message to #" مع geohash. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:183]

```
184:                 onSuccess?.invoke()
```
> يستدعي onSuccess إن لم تكن null عبر invoke بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:184]

```
185:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:185]

```
186:             } catch (e: Exception) {
```
> يبدأ كتلة catch تلتقط استثناءً e من نوع Exception. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:186]

```
187:                 Log.e(TAG, "❌ Failed to send geohash message: ${e.message}")
```
> يستدعي Log.e بالوسم TAG والرسالة "❌ Failed to send geohash message: " مع ‪e.message‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:187]

```
188:                 onError?.invoke("Failed to send message: ${e.message}")
```
> يستدعي onError إن لم تكن null عبر invoke بالرسالة "Failed to send message: " مع ‪e.message‬. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:188]

```
189:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:189]

```
190:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:190]

```
191:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:191]

```
192:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:192]

```
193:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:193]

```
194:      * Subscribe to public messages in a geohash channel
```
> تعليق: الاشتراك في الرسائل العامة في قناة geohash. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:194]

```
195:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:195]

```
196:     fun subscribeToGeohash(
```
> يعرّف الدالة subscribeToGeohash (الاشتراك في geohash) وتبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:196]

```
197:         geohash: String,
```
> يعرّف المعامل geohash من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:197]

```
198:         handler: (content: String, senderPubkey: String, nickname: String?, timestamp: Int) -> Unit
```
> يعرّف المعامل handler من نوع دالة تأخذ content من نوع String وsenderPubkey من نوع String وnickname من نوع String قابل للعدم وtimestamp من نوع Int وتعيد Unit. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:198]

```
199:     ) {
```
> يغلق قائمة المعاملات ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:199]

```
200:         val filter = NostrFilter.geohashEphemeral(
```
> يعرّف متغيّراً ثابتاً filter بإسناد ناتج استدعاء ‪NostrFilter.geohashEphemeral(...)‬ (يبدأ الاستدعاء). [app/src/main/java/com/bitchat/android/nostr/NostrClient.kt:200]
