# شريحة — app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt (الأسطر 1–94)

```
1: package com.bitchat.android.services
```
> يُعرّف هذا السطر اسم الحزمة (package) بالقيمة `com.bitchat.android.services`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `android.content.Context`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `android.util.Log`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:4]

```
5: import com.bitchat.android.identity.SecureIdentityStateManager
```
> يستورد الصنف `com.bitchat.android.identity.SecureIdentityStateManager` (مدير حالة الهوية الآمنة). [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:5]

```
6: import com.google.gson.Gson
```
> يستورد الصنف `com.google.gson.Gson`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:6]

```
7: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:7]

```
8: /**
```
> تعليق: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:8]

```
9:  * Persistent store for message IDs we've already acknowledged (DELIVERED) or READ.
```
> تعليق: «مخزن دائم لمعرّفات الرسائل التي سبق أن أقررنا باستلامها (DELIVERED) أو قرأناها (READ)». [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:9]

```
10:  * Limits to last MAX_IDS entries per set to avoid memory bloat.
```
> تعليق: «يحدّد آخر MAX_IDS مُدخلاً لكل مجموعة لتجنّب تضخّم الذاكرة». [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:10]

```
11:  */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:11]

```
12: class SeenMessageStore private constructor(private val context: Context) {
```
> يُعرّف الصنف `SeenMessageStore` (مخزن الرسائل المرئية) ببانٍ (constructor) خاص `private` يأخذ مُعاملاً خاصاً للقراءة فقط `context` من نوع `Context`، ويفتح نطاق جسم الصنف. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:12]

```
13:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:13]

```
14:         private const val TAG = "SeenMessageStore"
```
> يُعرّف ثابتاً خاصاً للقراءة فقط `TAG` ويضبط قيمته إلى السلسلة `"SeenMessageStore"`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:14]

```
15:         private const val STORAGE_KEY = "seen_message_store_v1"
```
> يُعرّف ثابتاً خاصاً `STORAGE_KEY` (مفتاح التخزين) ويضبط قيمته إلى السلسلة `"seen_message_store_v1"`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:15]

```
16:         private const val MAX_IDS = com.bitchat.android.util.AppConstants.Services.SEEN_MESSAGE_MAX_IDS
```
> يُعرّف ثابتاً خاصاً `MAX_IDS` (أقصى عدد للمعرّفات) ويضبط قيمته إلى `com.bitchat.android.util.AppConstants.Services.SEEN_MESSAGE_MAX_IDS`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:17]

```
18:         @Volatile private var INSTANCE: SeenMessageStore? = null
```
> يُعرّف متغيراً خاصاً متطايراً (Volatile) `INSTANCE` من نوع `SeenMessageStore?` ويضبط قيمته الابتدائية إلى `null`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:18]

```
19:         fun getInstance(appContext: Context): SeenMessageStore {
```
> يُعرّف دالة `getInstance` تأخذ مُعاملاً `appContext` من نوع `Context` وتُعيد قيمة من نوع `SeenMessageStore`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:19]

```
20:             return INSTANCE ?: synchronized(this) {
```
> يُعيد `INSTANCE` إن لم يكن `null`، وإلا يدخل كتلة متزامنة (synchronized) على `this`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:20]

```
21:                 INSTANCE ?: SeenMessageStore(appContext.applicationContext).also { INSTANCE = it }
```
> يُقيّم `INSTANCE` إن لم يكن `null`، وإلا يُنشئ `SeenMessageStore` بالمُعامل `appContext.applicationContext` ثم يُسند الكائن الجديد إلى `INSTANCE` داخل `also`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:21]

```
22:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:22]

```
23:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:23]

```
24:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:25]

```
26:     private val gson = Gson()
```
> يُعرّف خاصية خاصة للقراءة فقط `gson` ويضبط قيمتها إلى كائن `Gson()` جديد. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:26]

```
27:     private val secure = SecureIdentityStateManager(context)
```
> يُعرّف خاصية خاصة للقراءة فقط `secure` ويضبط قيمتها إلى كائن `SecureIdentityStateManager` مُنشأ بالمُعامل `context`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:28]

```
29:     private val delivered = LinkedHashSet<String>(MAX_IDS)
```
> يُعرّف خاصية خاصة للقراءة فقط `delivered` (المُسلَّمة) ويضبط قيمتها إلى `LinkedHashSet<String>` بسعة ابتدائية `MAX_IDS`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:29]

```
30:     private val read = LinkedHashSet<String>(MAX_IDS)
```
> يُعرّف خاصية خاصة للقراءة فقط `read` (المقروءة) ويضبط قيمتها إلى `LinkedHashSet<String>` بسعة ابتدائية `MAX_IDS`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:30]

```
31: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:31]

```
32:     init { load() }
```
> كتلة تهيئة (init) تستدعي الدالة `load()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:33]

```
34:     @Synchronized fun hasDelivered(id: String) = delivered.contains(id)
```
> يُعرّف دالة متزامنة (Synchronized) `hasDelivered` تأخذ مُعاملاً `id` من نوع `String` وتُعيد نتيجة `delivered.contains(id)`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:34]

```
35:     @Synchronized fun hasRead(id: String) = read.contains(id)
```
> يُعرّف دالة متزامنة `hasRead` تأخذ مُعاملاً `id` من نوع `String` وتُعيد نتيجة `read.contains(id)`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:36]

```
37:     @Synchronized fun markDelivered(id: String) {
```
> يُعرّف دالة متزامنة `markDelivered` تأخذ مُعاملاً `id` من نوع `String`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:37]

```
38:         if (delivered.remove(id)) delivered.add(id) else {
```
> إن نجح `delivered.remove(id)` فإنه يستدعي `delivered.add(id)`، وإلا يفتح نطاق الكتلة البديلة `else`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:38]

```
39:             delivered.add(id)
```
> يستدعي `delivered.add(id)`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:39]

```
40:             trim(delivered)
```
> يستدعي الدالة `trim` بالمُعامل `delivered`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:40]

```
41:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:41]

```
42:         persist()
```
> يستدعي الدالة `persist()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:42]

```
43:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:43]

```
44: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:44]

```
45:     @Synchronized fun markRead(id: String) {
```
> يُعرّف دالة متزامنة `markRead` تأخذ مُعاملاً `id` من نوع `String`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:45]

```
46:         if (read.remove(id)) read.add(id) else {
```
> إن نجح `read.remove(id)` فإنه يستدعي `read.add(id)`، وإلا يفتح نطاق الكتلة البديلة `else`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:46]

```
47:             read.add(id)
```
> يستدعي `read.add(id)`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:47]

```
48:             trim(read)
```
> يستدعي الدالة `trim` بالمُعامل `read`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:48]

```
49:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:49]

```
50:         persist()
```
> يستدعي الدالة `persist()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:50]

```
51:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:51]

```
52: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:52]

```
53:     @Synchronized fun clear() {
```
> يُعرّف دالة متزامنة `clear` بلا مُعاملات، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:53]

```
54:         delivered.clear()
```
> يستدعي `delivered.clear()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:54]

```
55:         read.clear()
```
> يستدعي `read.clear()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:55]

```
56:         persist()
```
> يستدعي الدالة `persist()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:56]

```
57:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:57]

```
58: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:58]

```
59:     private fun trim(set: LinkedHashSet<String>) {
```
> يُعرّف دالة خاصة `trim` (تقليم) تأخذ مُعاملاً `set` من نوع `LinkedHashSet<String>`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:59]

```
60:         if (set.size <= MAX_IDS) return
```
> إن كان `set.size` أصغر من أو يساوي `MAX_IDS` فإنه يُعيد (return) دون قيمة. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:60]

```
61:         val it = set.iterator()
```
> يُعرّف متغيراً للقراءة فقط `it` ويضبط قيمته إلى `set.iterator()` (مُكرِّر المجموعة). [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:61]

```
62:         while (set.size > MAX_IDS && it.hasNext()) {
```
> يبدأ حلقة `while` تستمر طالما أن `set.size` أكبر من `MAX_IDS` و`it.hasNext()` صحيح، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:62]

```
63:             it.next(); it.remove()
```
> يستدعي `it.next()` ثم `it.remove()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:63]

```
64:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:64]

```
65:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:65]

```
66: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:66]

```
67:     @Synchronized private fun load() {
```
> يُعرّف دالة خاصة متزامنة `load` (تحميل) بلا مُعاملات، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:67]

```
68:         try {
```
> يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:68]

```
69:             val json = secure.getSecureValue(STORAGE_KEY) ?: return
```
> يُعرّف متغيراً للقراءة فقط `json` ويضبط قيمته إلى `secure.getSecureValue(STORAGE_KEY)`، وإن كانت `null` فإنه يُعيد (return). [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:69]

```
70:             val data = gson.fromJson(json, StorePayload::class.java) ?: return
```
> يُعرّف متغيراً للقراءة فقط `data` ويضبط قيمته إلى `gson.fromJson(json, StorePayload::class.java)`، وإن كانت `null` فإنه يُعيد (return). [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:70]

```
71:             delivered.clear(); read.clear()
```
> يستدعي `delivered.clear()` ثم `read.clear()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:71]

```
72:             data.delivered.takeLast(MAX_IDS).forEach { delivered.add(it) }
```
> يأخذ آخر `MAX_IDS` عنصراً من `data.delivered` عبر `takeLast`، ولكل عنصر يستدعي `delivered.add(it)`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:72]

```
73:             data.read.takeLast(MAX_IDS).forEach { read.add(it) }
```
> يأخذ آخر `MAX_IDS` عنصراً من `data.read` عبر `takeLast`، ولكل عنصر يستدعي `read.add(it)`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:73]

```
74:             Log.d(TAG, "Loaded delivered=${delivered.size}, read=${read.size}")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"Loaded delivered=${delivered.size}, read=${read.size}"`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:74]

```
75:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:75]

```
76:             Log.e(TAG, "Failed to load SeenMessageStore: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` والرسالة `"Failed to load SeenMessageStore: ${e.message}"`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:76]

```
77:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:77]

```
78:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:78]

```
79: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:79]

```
80:     @Synchronized private fun persist() {
```
> يُعرّف دالة خاصة متزامنة `persist` (حفظ دائم) بلا مُعاملات، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:80]

```
81:         try {
```
> يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:81]

```
82:             val payload = StorePayload(delivered.toList(), read.toList())
```
> يُعرّف متغيراً للقراءة فقط `payload` ويضبط قيمته إلى `StorePayload` مُنشأ بـ `delivered.toList()` و`read.toList()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:82]

```
83:             val json = gson.toJson(payload)
```
> يُعرّف متغيراً للقراءة فقط `json` ويضبط قيمته إلى `gson.toJson(payload)`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:83]

```
84:             secure.storeSecureValue(STORAGE_KEY, json)
```
> يستدعي `secure.storeSecureValue` بالمُعاملين `STORAGE_KEY` و`json`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:84]

```
85:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:85]

```
86:             Log.e(TAG, "Failed to persist SeenMessageStore: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` والرسالة `"Failed to persist SeenMessageStore: ${e.message}"`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:86]

```
87:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:87]

```
88:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:88]

```
89: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:89]

```
90:     private data class StorePayload(
```
> يُعرّف صنف بيانات خاص `StorePayload` (حمولة المخزن)، ويفتح نطاق قائمة مُعاملاته. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:90]

```
91:         val delivered: List<String> = emptyList(),
```
> يُعرّف خاصية للقراءة فقط `delivered` من نوع `List<String>` بقيمة افتراضية `emptyList()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:91]

```
92:         val read: List<String> = emptyList()
```
> يُعرّف خاصية للقراءة فقط `read` من نوع `List<String>` بقيمة افتراضية `emptyList()`. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:92]

```
93:     )
```
> إغلاق قائمة مُعاملات صنف البيانات. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:93]

```
94: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/SeenMessageStore.kt:94]
