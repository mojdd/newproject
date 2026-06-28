# شريحة — app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يعرّف حزمة (package) الملف باسم `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:2]

```
3: import android.util.Log
```
> يستورد صنف السجل (Log) من `android.util`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:3]

```
4: import androidx.annotation.MainThread
```
> يستورد التعليق التوضيحي «الخيط الرئيسي» (MainThread) من `androidx.annotation`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:4]

```
5: import kotlinx.coroutines.*
```
> يستورد كل عناصر حزمة الإجراءات المتزامنة (coroutines) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:5]

```
6: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد «تدفّق الحالة القابل للتغيير» (MutableStateFlow) من `kotlinx.coroutines.flow`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:6]

```
7: import kotlinx.coroutines.flow.StateFlow
```
> يستورد «تدفّق الحالة» (StateFlow) من `kotlinx.coroutines.flow`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:7]

```
8: import kotlinx.coroutines.flow.asStateFlow
```
> يستورد الدالة `asStateFlow` التي تحوّل التدفّق إلى «تدفّق حالة» للقراءة فقط، من `kotlinx.coroutines.flow`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:9]

```
10: /**
```
> تعليق: بداية كتلة توثيق (KDoc). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:10]

```
11:  * Manages location notes (kind=1 text notes with geohash tags)
```
> تعليق: «يدير ملاحظات الموقع (ملاحظات نصية من النوع kind=1 مع وسوم جيوهاش)». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:11]

```
12:  * iOS-compatible implementation with StateFlow for Android UI binding
```
> تعليق: «تنفيذ متوافق مع iOS باستعمال StateFlow لربط واجهة أندرويد». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:12]

```
13:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:13]

```
14: @MainThread
```
> يضع التعليق التوضيحي `@MainThread` على ما يليه، أي يصرّح بأنه يُنفَّذ على الخيط الرئيسي. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:14]

```
15: class LocationNotesManager private constructor() {
```
> يعرّف صنف «مدير ملاحظات الموقع» (LocationNotesManager) ذا بانٍ خاص (private constructor) بلا وسائط، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:15]

```
16:     
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:16]

```
17:     companion object {
```
> يفتح «الكائن المرافق» (companion object) للصنف. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:17]

```
18:         private const val TAG = "LocationNotesManager"
```
> يعرّف ثابتاً خاصاً `TAG` من نوع نصي بقيمة `"LocationNotesManager"`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:18]

```
19:         private const val MAX_NOTES_IN_MEMORY = 500
```
> يعرّف ثابتاً خاصاً «الحد الأقصى للملاحظات في الذاكرة» (MAX_NOTES_IN_MEMORY) بقيمة `500`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:19]

```
20:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:20]

```
21:         @Volatile
```
> يضع التعليق التوضيحي `@Volatile` على ما يليه، أي يجعل الحقل التالي متطايراً (لا يُخزَّن مؤقتاً بين الخيوط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:21]

```
22:         private var INSTANCE: LocationNotesManager? = null
```
> يعرّف متغيراً خاصاً `INSTANCE` من نوع `LocationNotesManager` القابل للقيمة الفارغة، بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:22]

```
23:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:23]

```
24:         fun getInstance(): LocationNotesManager {
```
> يعرّف الدالة `getInstance` التي تُعيد كائناً من نوع `LocationNotesManager`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:24]

```
25:             return INSTANCE ?: synchronized(this) {
```
> يُعيد `INSTANCE` إن لم يكن فارغاً، وإلا يدخل كتلة متزامنة (synchronized) على `this`، ويفتح هذه الكتلة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:25]

```
26:                 INSTANCE ?: LocationNotesManager().also { INSTANCE = it }
```
> يُعيد `INSTANCE` إن لم يكن فارغاً، وإلا يُنشئ كائن `LocationNotesManager` جديداً ويسنده إلى `INSTANCE` عبر `also` ثم يُعيده. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:26]

```
27:             }
```
> إغلاق نطاق (الكتلة المتزامنة). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:27]

```
28:         }
```
> إغلاق نطاق (دالة `getInstance`). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:28]

```
29:     }
```
> إغلاق نطاق (الكائن المرافق). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:29]

```
30:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:30]

```
31:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:31]

```
32:      * Note data class matching iOS implementation
```
> تعليق: «صنف بيانات الملاحظة (Note) مطابق لتنفيذ iOS». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:32]

```
33:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:33]

```
34:     data class Note(
```
> يعرّف «صنف بيانات الملاحظة» (data class Note) ويفتح قائمة وسائط بانيه. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:34]

```
35:         val id: String,
```
> يعرّف خاصية `id` من نوع نصي للقراءة فقط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:35]

```
36:         val pubkey: String,
```
> يعرّف خاصية «المفتاح العام» (pubkey) من نوع نصي للقراءة فقط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:36]

```
37:         val content: String,
```
> يعرّف خاصية `content` (المحتوى) من نوع نصي للقراءة فقط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:37]

```
38:         val createdAt: Int,
```
> يعرّف خاصية «وقت الإنشاء» (createdAt) من نوع عدد صحيح للقراءة فقط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:38]

```
39:         val nickname: String?
```
> يعرّف خاصية `nickname` (الاسم المستعار) من نوع نصي قابل للقيمة الفارغة للقراءة فقط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:39]

```
40:     ) {
```
> يغلق قائمة وسائط البانٍ ويفتح جسم صنف البيانات `Note`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:40]

```
41:         /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:41]

```
42:          * Display name for the note - matches iOS exactly
```
> تعليق: «اسم العرض للملاحظة - مطابق لـ iOS تماماً». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:42]

```
43:          * Format: "nickname#abcd" or "anon#abcd" where abcd is last 4 chars of pubkey
```
> تعليق: «الصيغة: "nickname#abcd" أو "anon#abcd" حيث abcd هي آخر 4 محارف من المفتاح العام». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:43]

```
44:          */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:44]

```
45:         val displayName: String
```
> يعرّف خاصية «اسم العرض» (displayName) من نوع نصي للقراءة فقط (بدون تهيئة مباشرة هنا). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:45]

```
46:             get() {
```
> يفتح «الجالب» (getter) المخصص لخاصية `displayName`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:46]

```
47:                 val suffix = pubkey.takeLast(4)
```
> يعرّف متغيراً محلياً `suffix` (لاحقة) بقيمة آخر 4 محارف من `pubkey`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:47]

```
48:                 val nick = nickname?.trim()
```
> يعرّف متغيراً محلياً `nick` بقيمة `nickname` بعد إزالة الفراغات الطرفية (trim)، أو `null` إن كان `nickname` فارغاً. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:48]

```
49:                 return if (!nick.isNullOrEmpty()) {
```
> يبدأ تعبير إعادة شرطياً: إن لم يكن `nick` فارغاً ولا `null` فيفتح فرع «صحيح». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:49]

```
50:                     "$nick#$suffix"
```
> القيمة المُعادة في فرع الصحيح: سلسلة نصية تجمع `nick` ثم محرف `#` ثم `suffix`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:50]

```
51:                 } else {
```
> يغلق فرع الصحيح ويفتح فرع «خلاف ذلك» (else). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:51]

```
52:                     "anon#$suffix"
```
> القيمة المُعادة في فرع else: سلسلة نصية تجمع `"anon"` ثم محرف `#` ثم `suffix`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:52]

```
53:                 }
```
> إغلاق نطاق (تعبير if/else). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:53]

```
54:             }
```
> إغلاق نطاق (الجالب getter). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:54]

```
55:     }
```
> إغلاق نطاق (صنف البيانات `Note`). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:55]

```
56:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:56]

```
57:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:57]

```
58:      * Manager state enum
```
> تعليق: «تعداد حالة المدير». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:58]

```
59:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:59]

```
60:     enum class State {
```
> يعرّف صنف تعداد (enum class) باسم «الحالة» (State) ويفتح جسمه. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:60]

```
61:         IDLE,
```
> يعرّف عنصر التعداد `IDLE` (خامل). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:61]

```
62:         LOADING,
```
> يعرّف عنصر التعداد `LOADING` (قيد التحميل). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:62]

```
63:         READY,
```
> يعرّف عنصر التعداد `READY` (جاهز). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:63]

```
64:         NO_RELAYS
```
> يعرّف عنصر التعداد `NO_RELAYS` (لا مُرحِّلات). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:64]

```
65:     }
```
> إغلاق نطاق (صنف التعداد `State`). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:65]

```
66:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:66]

```
67:     // Published state (StateFlow for Android)
```
> تعليق: «الحالة المنشورة (StateFlow لأندرويد)». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:67]

```
68:     private val _notes = MutableStateFlow<List<Note>>(emptyList())
```
> يعرّف حقلاً خاصاً `_notes` من نوع «تدفّق حالة قابل للتغيير» يحمل قائمة `Note`، بقيمة ابتدائية قائمة فارغة (emptyList). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:68]

```
69:     val notes: StateFlow<List<Note>> = _notes.asStateFlow()
```
> يعرّف خاصية عامة `notes` من نوع «تدفّق حالة» للقراءة فقط، مسندة من `_notes` عبر `asStateFlow()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:69]

```
70:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:70]

```
71:     private val _geohash = MutableStateFlow<String?>(null)
```
> يعرّف حقلاً خاصاً `_geohash` من نوع «تدفّق حالة قابل للتغيير» يحمل نصاً قابلاً للقيمة الفارغة، بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:71]

```
72:     val geohash: StateFlow<String?> = _geohash.asStateFlow()
```
> يعرّف خاصية عامة `geohash` من نوع «تدفّق حالة» للقراءة فقط لنص قابل للفراغ، مسندة من `_geohash` عبر `asStateFlow()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:72]

```
73:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:73]

```
74:     private val _initialLoadComplete = MutableStateFlow(false)
```
> يعرّف حقلاً خاصاً «اكتمال التحميل الأولي» (_initialLoadComplete) من نوع «تدفّق حالة قابل للتغيير» منطقي، بقيمة ابتدائية `false`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:74]

```
75:     val initialLoadComplete: StateFlow<Boolean> = _initialLoadComplete.asStateFlow()
```
> يعرّف خاصية عامة `initialLoadComplete` من نوع «تدفّق حالة» منطقي للقراءة فقط، مسندة من `_initialLoadComplete` عبر `asStateFlow()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:75]

```
76:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:76]

```
77:     private val _state = MutableStateFlow(State.IDLE)
```
> يعرّف حقلاً خاصاً `_state` من نوع «تدفّق حالة قابل للتغيير»، بقيمة ابتدائية `State.IDLE`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:77]

```
78:     val state: StateFlow<State> = _state.asStateFlow()
```
> يعرّف خاصية عامة `state` من نوع «تدفّق حالة» من نوع `State` للقراءة فقط، مسندة من `_state` عبر `asStateFlow()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:78]

```
79:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:79]

```
80:     private val _errorMessage = MutableStateFlow<String?>(null)
```
> يعرّف حقلاً خاصاً «رسالة الخطأ» (_errorMessage) من نوع «تدفّق حالة قابل للتغيير» يحمل نصاً قابلاً للفراغ، بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:80]

```
81:     val errorMessage: StateFlow<String?> = _errorMessage.asStateFlow()
```
> يعرّف خاصية عامة `errorMessage` من نوع «تدفّق حالة» لنص قابل للفراغ للقراءة فقط، مسندة من `_errorMessage` عبر `asStateFlow()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:81]

```
82:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:82]

```
83:     // Private state
```
> تعليق: «الحالة الخاصة». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:83]

```
84:     private var subscriptionIDs: MutableMap<String, String> = mutableMapOf()
```
> يعرّف متغيراً خاصاً «معرّفات الاشتراك» (subscriptionIDs) من نوع خريطة قابلة للتغيير من نص إلى نص، بقيمة ابتدائية خريطة فارغة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:84]

```
85:     private val noteIDs = mutableSetOf<String>() // For deduplication
```
> يعرّف حقلاً خاصاً «معرّفات الملاحظات» (noteIDs) من نوع مجموعة نصوص قابلة للتغيير فارغة؛ والتعليق: «لإزالة التكرار». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:85]

```
86:     private var subscribedGeohashes: Set<String> = emptySet()
```
> يعرّف متغيراً خاصاً «الجيوهاشات المشترَك بها» (subscribedGeohashes) من نوع مجموعة نصوص، بقيمة ابتدائية مجموعة فارغة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:86]

```
87:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:87]

```
88:     // Dependencies (injected via setters for flexibility)
```
> تعليق: «التبعيات (تُحقَن عبر مُسندات للمرونة)». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:88]

```
89:     private var relayLookup: (() -> NostrRelayManager)? = null
```
> يعرّف متغيراً خاصاً «باحث المُرحِّل» (relayLookup) من نوع دالة بلا وسائط تُعيد `NostrRelayManager`، قابلة للفراغ، بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:89]

```
90:     private var subscribeFunc: ((NostrFilter, String, (NostrEvent) -> Unit) -> String)? = null
```
> يعرّف متغيراً خاصاً «دالة الاشتراك» (subscribeFunc) من نوع دالة تأخذ `NostrFilter` ونصاً ودالة تستقبل `NostrEvent` وتُعيد `Unit`، وتُعيد نصاً، قابلة للفراغ، بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:90]

```
91:     private var unsubscribeFunc: ((String) -> Unit)? = null
```
> يعرّف متغيراً خاصاً «دالة إلغاء الاشتراك» (unsubscribeFunc) من نوع دالة تأخذ نصاً وتُعيد `Unit`، قابلة للفراغ، بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:91]

```
92:     private var sendEventFunc: ((NostrEvent, List<String>?) -> Unit)? = null
```
> يعرّف متغيراً خاصاً «دالة إرسال الحدث» (sendEventFunc) من نوع دالة تأخذ `NostrEvent` وقائمة نصوص قابلة للفراغ وتُعيد `Unit`، قابلة للفراغ، بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:92]

```
93:     private var deriveIdentityFunc: ((String) -> NostrIdentity)? = null
```
> يعرّف متغيراً خاصاً «دالة اشتقاق الهوية» (deriveIdentityFunc) من نوع دالة تأخذ نصاً وتُعيد `NostrIdentity`، قابلة للفراغ، بقيمة ابتدائية `null`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:93]

```
94:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:94]

```
95:     // Coroutine scope for background operations
```
> تعليق: «نطاق إجراءات متزامنة للعمليات الخلفية». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:95]

```
96:     private val scope = CoroutineScope(Dispatchers.Main + SupervisorJob())
```
> يعرّف حقلاً خاصاً «النطاق» (scope) بقيمة `CoroutineScope` مبني على موزّع الخيط الرئيسي `Dispatchers.Main` مضافاً إليه «مهمة مشرفة» (SupervisorJob). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:96]

```
97:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:97]

```
98:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:98]

```
99:      * Initialize dependencies
```
> تعليق: «تهيئة التبعيات». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:99]

```
100:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:100]

```
101:     fun initialize(
```
> يعرّف الدالة `initialize` (تهيئة) ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:101]

```
102:         relayManager: () -> NostrRelayManager,
```
> يعرّف الوسيط `relayManager` من نوع دالة بلا وسائط تُعيد `NostrRelayManager`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:102]

```
103:         subscribe: (NostrFilter, String, (NostrEvent) -> Unit) -> String,
```
> يعرّف الوسيط `subscribe` من نوع دالة تأخذ `NostrFilter` ونصاً ودالة تستقبل `NostrEvent` وتُعيد `Unit`، وتُعيد نصاً. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:103]

```
104:         unsubscribe: (String) -> Unit,
```
> يعرّف الوسيط `unsubscribe` من نوع دالة تأخذ نصاً وتُعيد `Unit`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:104]

```
105:         sendEvent: (NostrEvent, List<String>?) -> Unit,
```
> يعرّف الوسيط `sendEvent` من نوع دالة تأخذ `NostrEvent` وقائمة نصوص قابلة للفراغ وتُعيد `Unit`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:105]

```
106:         deriveIdentity: (String) -> NostrIdentity
```
> يعرّف الوسيط `deriveIdentity` من نوع دالة تأخذ نصاً وتُعيد `NostrIdentity`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:106]

```
107:     ) {
```
> يغلق قائمة وسائط `initialize` ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:107]

```
108:         this.relayLookup = relayManager
```
> يُسند الوسيط `relayManager` إلى الحقل `this.relayLookup`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:108]

```
109:         this.subscribeFunc = subscribe
```
> يُسند الوسيط `subscribe` إلى الحقل `this.subscribeFunc`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:109]

```
110:         this.unsubscribeFunc = unsubscribe
```
> يُسند الوسيط `unsubscribe` إلى الحقل `this.unsubscribeFunc`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:110]

```
111:         this.sendEventFunc = sendEvent
```
> يُسند الوسيط `sendEvent` إلى الحقل `this.sendEventFunc`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:111]

```
112:         this.deriveIdentityFunc = deriveIdentity
```
> يُسند الوسيط `deriveIdentity` إلى الحقل `this.deriveIdentityFunc`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:112]

```
113:     }
```
> إغلاق نطاق (دالة `initialize`). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:113]

```
114:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:114]

```
115:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:115]

```
116:      * Set geohash and start subscription
```
> تعليق: «ضبط الجيوهاش وبدء الاشتراك». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:116]

```
117:      * iOS: Validates building-level precision (8 characters)
```
> تعليق: «iOS: يتحقق من دقّة مستوى المبنى (8 محارف)». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:117]

```
118:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:118]

```
119:     fun setGeohash(newGeohash: String) {
```
> يعرّف الدالة `setGeohash` التي تأخذ وسيطاً نصياً `newGeohash` ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:119]

```
120:         val normalized = newGeohash.lowercase()
```
> يعرّف متغيراً محلياً «المُطبَّع» (normalized) بقيمة `newGeohash` بعد تحويله إلى حروف صغيرة عبر `lowercase()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:120]

```
121:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:121]

```
122:         if (_geohash.value == normalized) {
```
> يبدأ شرطاً: إن كانت قيمة `_geohash` تساوي `normalized` فيفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:122]

```
123:             Log.d(TAG, "Geohash unchanged, skipping: $normalized")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة «Geohash unchanged, skipping: » متبوعة بقيمة `normalized` (تسجيل تنقيح). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:123]

```
124:             return
```
> يُعيد (يخرج من الدالة) بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:124]

```
125:         }
```
> إغلاق نطاق (كتلة الشرط `if`). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:125]

```
126:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:126]

```
127:         // Validate geohash (building-level precision: 8 chars) - matches iOS
```
> تعليق: «التحقق من الجيوهاش (دقّة مستوى المبنى: 8 محارف) - مطابق لـ iOS». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:127]

```
128:         if (!isValidBuildingGeohash(normalized)) {
```
> يبدأ شرطاً: إن كان `isValidBuildingGeohash(normalized)` يُعيد خطأً (أي الجيوهاش غير صالح) فيفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:128]

```
129:             Log.w(TAG, "LocationNotesManager: rejecting invalid geohash '$normalized' (expected 8 valid base32 chars)")
```
> يستدعي `Log.w` بالوسم `TAG` ورسالة تحذير «LocationNotesManager: rejecting invalid geohash '...' (expected 8 valid base32 chars)» مع قيمة `normalized`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:129]

```
130:             return
```
> يُعيد (يخرج من الدالة) بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:130]

```
131:         }
```
> إغلاق نطاق (كتلة شرط التحقق). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:131]

```
132:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:132]

```
133:         Log.d(TAG, "Setting geohash: $normalized")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة «Setting geohash: » متبوعة بقيمة `normalized` (تسجيل تنقيح). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:133]

```
134:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:134]

```
135:         // Cancel existing subscription
```
> تعليق: «إلغاء الاشتراك القائم». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:135]

```
136:         cancel()
```
> يستدعي الدالة `cancel()` (المعرّفة في مكان آخر من الصنف). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:136]

```
137:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:137]

```
138:         // Set loading state before clearing to prevent empty state flicker (iOS pattern)
```
> تعليق: «ضبط حالة التحميل قبل المسح لمنع وميض الحالة الفارغة (نمط iOS)». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:138]

```
139:         _state.value = State.LOADING
```
> يُسند `State.LOADING` إلى قيمة `_state`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:139]

```
140:         _initialLoadComplete.value = false
```
> يُسند `false` إلى قيمة `_initialLoadComplete`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:140]

```
141:         _errorMessage.value = null
```
> يُسند `null` إلى قيمة `_errorMessage`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:141]

```
142:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:142]

```
143:         // Clear notes
```
> تعليق: «مسح الملاحظات». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:143]

```
144:         _notes.value = emptyList()
```
> يُسند قائمة فارغة (emptyList) إلى قيمة `_notes`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:144]

```
145:         noteIDs.clear()
```
> يستدعي `clear()` على `noteIDs` لإفراغ مجموعة معرّفات الملاحظات. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:145]

```
146:         _geohash.value = normalized
```
> يُسند `normalized` إلى قيمة `_geohash`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:146]

```
147:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:147]

```
148:         // Compute target geohashes: center + neighbors (±1)
```
> تعليق: «حساب الجيوهاشات المستهدفة: المركز + الجيران (±1)». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:148]

```
149:         val neighbors = try {
```
> يعرّف متغيراً محلياً «الجيران» (neighbors) ويبدأ تعبير `try` لإسناد قيمته. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:149]

```
150:             com.bitchat.android.geohash.Geohash.neighborsSamePrecision(normalized)
```
> يستدعي `com.bitchat.android.geohash.Geohash.neighborsSamePrecision` بالوسيط `normalized` (يحسب الجيران بالدقّة نفسها). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:150]

```
151:         } catch (_: Exception) { emptySet() }
```
> يغلق كتلة `try` ويعرّف `catch` يلتقط أي `Exception` (باسم مهمَل `_`) ويُعيد في حالة الالتقاط مجموعة فارغة (emptySet). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:151]

```
152:         subscribedGeohashes = (neighbors + normalized).toSet()
```
> يُسند إلى `subscribedGeohashes` مجموعة ناتجة عن دمج `neighbors` مع `normalized` ثم تحويلها إلى مجموعة عبر `toSet()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:152]

```
153: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:153]

```
154:         // Start new subscriptions for all cells
```
> تعليق: «بدء اشتراكات جديدة لكل الخلايا». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:154]

```
155:         subscribeAll()
```
> يستدعي الدالة `subscribeAll()` (المعرّفة في مكان آخر من الصنف). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:155]

```
156:     }
```
> إغلاق نطاق (دالة `setGeohash`). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:156]

```
157:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:157]

```
158:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:158]

```
159:      * Validate building-level geohash (precision 8) - matches iOS Geohash.isValidBuildingGeohash
```
> تعليق: «التحقق من جيوهاش مستوى المبنى (دقّة 8) - مطابق لـ iOS Geohash.isValidBuildingGeohash». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:159]

```
160:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:160]

```
161:     private fun isValidBuildingGeohash(geohash: String): Boolean {
```
> يعرّف دالة خاصة «هل جيوهاش المبنى صالح» (isValidBuildingGeohash) تأخذ نصاً `geohash` وتُعيد قيمة منطقية، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:161]

```
162:         if (geohash.length != 8) return false
```
> يُعيد `false` إذا كان طول `geohash` لا يساوي 8. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:162]

```
163:         val base32Chars = "0123456789bcdefghjkmnpqrstuvwxyz"
```
> يعرّف متغيراً محلياً «محارف base32» (base32Chars) بالقيمة النصية `"0123456789bcdefghjkmnpqrstuvwxyz"`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:163]

```
164:         return geohash.all { it in base32Chars }
```
> يُعيد نتيجة `all` على `geohash`، أي صحيح إن كان كل محرف `it` موجوداً ضمن `base32Chars`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:164]

```
165:     }
```
> إغلاق نطاق (دالة `isValidBuildingGeohash`). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:165]

```
166:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:166]

```
167:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:167]

```
168:      * Refresh notes for current geohash
```
> تعليق: «تحديث الملاحظات للجيوهاش الحالي». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:168]

```
169:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:169]

```
170:     fun refresh() {
```
> يعرّف الدالة `refresh` (تحديث) بلا وسائط ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:170]

```
171:         val currentGeohash = _geohash.value
```
> يعرّف متغيراً محلياً «الجيوهاش الحالي» (currentGeohash) بقيمة `_geohash.value`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:171]

```
172:         if (currentGeohash == null) {
```
> يبدأ شرطاً: إن كان `currentGeohash` يساوي `null` فيفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:172]

```
173:             Log.w(TAG, "Cannot refresh - no geohash set")
```
> يستدعي `Log.w` بالوسم `TAG` ورسالة تحذير «Cannot refresh - no geohash set». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:173]

```
174:             return
```
> يُعيد (يخرج من الدالة) بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:174]

```
175:         }
```
> إغلاق نطاق (كتلة الشرط `if`). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:175]

```
176:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:176]

```
177:         Log.d(TAG, "Refreshing notes for geohash: $currentGeohash")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة «Refreshing notes for geohash: » متبوعة بقيمة `currentGeohash` (تسجيل تنقيح). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:177]

```
178:         
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:178]

```
179:         // Cancel and restart subscriptions for current ±1 set
```
> تعليق: «إلغاء وإعادة بدء الاشتراكات لمجموعة ±1 الحالية». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:179]

```
180:         cancel()
```
> يستدعي الدالة `cancel()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:180]

```
181:         _notes.value = emptyList()
```
> يُسند قائمة فارغة (emptyList) إلى قيمة `_notes`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:181]

```
182:         noteIDs.clear()
```
> يستدعي `clear()` على `noteIDs` لإفراغ مجموعة معرّفات الملاحظات. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:182]

```
183:         _initialLoadComplete.value = false
```
> يُسند `false` إلى قيمة `_initialLoadComplete`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:183]

```
184:         // Rebuild subscribedGeohashes and resubscribe
```
> تعليق: «إعادة بناء subscribedGeohashes وإعادة الاشتراك». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:184]

```
185:         val neighbors = try {
```
> يعرّف متغيراً محلياً «الجيران» (neighbors) ويبدأ تعبير `try` لإسناد قيمته. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:185]

```
186:             com.bitchat.android.geohash.Geohash.neighborsSamePrecision(currentGeohash)
```
> يستدعي `com.bitchat.android.geohash.Geohash.neighborsSamePrecision` بالوسيط `currentGeohash`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:186]

```
187:         } catch (_: Exception) { emptySet() }
```
> يغلق كتلة `try` ويعرّف `catch` يلتقط أي `Exception` (باسم مهمَل `_`) ويُعيد في حالة الالتقاط مجموعة فارغة (emptySet). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:187]

```
188:         subscribedGeohashes = (neighbors + currentGeohash).toSet()
```
> يُسند إلى `subscribedGeohashes` مجموعة ناتجة عن دمج `neighbors` مع `currentGeohash` ثم تحويلها إلى مجموعة عبر `toSet()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:188]

```
189:         subscribeAll()
```
> يستدعي الدالة `subscribeAll()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:189]

```
190:     }
```
> إغلاق نطاق (دالة `refresh`). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:190]

```
191:     
```
> سطر فارغ (مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:191]

```
192:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:192]

```
193:      * Send a new location note
```
> تعليق: «إرسال ملاحظة موقع جديدة». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:193]

```
194:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:194]

```
195:     fun send(content: String, nickname: String?) {
```
> يعرّف الدالة `send` (إرسال) التي تأخذ نصاً `content` ونصاً قابلاً للفراغ `nickname` ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:195]

```
196:         val currentGeohash = _geohash.value
```
> يعرّف متغيراً محلياً «الجيوهاش الحالي» (currentGeohash) بقيمة `_geohash.value`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:196]

```
197:         if (currentGeohash == null) {
```
> يبدأ شرطاً: إن كان `currentGeohash` يساوي `null` فيفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:197]

```
198:             Log.w(TAG, "Cannot send note - no geohash set")
```
> يستدعي `Log.w` بالوسم `TAG` ورسالة تحذير «Cannot send note - no geohash set». [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:198]

```
199:             _errorMessage.value = "No location set"
```
> يُسند النص `"No location set"` إلى قيمة `_errorMessage`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:199]

```
200:             return
```
> يُعيد (يخرج من الدالة) بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:200]
