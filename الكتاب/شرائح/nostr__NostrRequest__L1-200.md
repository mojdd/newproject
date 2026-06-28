# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يُعلِن هذا السطر أن الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.nostr. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:2]

```
3: import com.google.gson.*
```
> يستورد (import) كل الرموز العامة من حزمة com.google.gson باستعمال النجمة. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:3]

```
4: import java.lang.reflect.Type
```
> يستورد الصنف Type من حزمة java.lang.reflect (الانعكاس/reflect). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:5]

```
6: /**
```
> تعليق: بداية كتلة توثيق (تعليق وثائقي). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:6]

```
7:  * Nostr protocol request messages
```
> تعليق: رسائل طلب بروتوكول Nostr. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:7]

```
8:  * Supports EVENT, REQ, and CLOSE message types
```
> تعليق: يدعم أنواع الرسائل EVENT و REQ و CLOSE. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:8]

```
9:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:9]

```
10: sealed class NostrRequest {
```
> يُعرِّف صنفاً مختوماً (sealed class) باسم طلب Nostr (NostrRequest) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:10]

```
11:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:11]

```
12:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:12]

```
13:      * EVENT message - publish an event
```
> تعليق: رسالة EVENT - نشر حدث. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:13]

```
14:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:14]

```
15:     data class Event(val event: NostrEvent) : NostrRequest()
```
> يُعرِّف صنف بيانات (data class) باسم حدث (Event) يحمل خاصية للقراءة فقط باسم event من نوع NostrEvent، ويرث من NostrRequest. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:15]

```
16:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:16]

```
17:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:17]

```
18:      * REQ message - subscribe to events
```
> تعليق: رسالة REQ - الاشتراك في الأحداث. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:18]

```
19:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:19]

```
20:     data class Subscribe(
```
> يُعرِّف صنف بيانات باسم اشتراك (Subscribe) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:20]

```
21:         val subscriptionId: String,
```
> يُعرِّف خاصية للقراءة فقط باسم معرّف الاشتراك (subscriptionId) من نوع نص (String). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:21]

```
22:         val filters: List<NostrFilter>
```
> يُعرِّف خاصية للقراءة فقط باسم مرشّحات (filters) من نوع قائمة (List) عناصرها من نوع NostrFilter. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:22]

```
23:     ) : NostrRequest()
```
> يغلق قائمة المعاملات ويجعل الصنف Subscribe يرث من NostrRequest. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:23]

```
24:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:24]

```
25:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:25]

```
26:      * CLOSE message - close a subscription
```
> تعليق: رسالة CLOSE - إغلاق اشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:26]

```
27:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:27]

```
28:     data class Close(val subscriptionId: String) : NostrRequest()
```
> يُعرِّف صنف بيانات باسم إغلاق (Close) يحمل خاصية للقراءة فقط باسم subscriptionId من نوع نص، ويرث من NostrRequest. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:28]

```
29:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:29]

```
30:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:30]

```
31:      * Custom JSON serializer for NostrRequest
```
> تعليق: مُسلسِل JSON مخصّص لطلب NostrRequest. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:31]

```
32:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:32]

```
33:     class RequestSerializer : JsonSerializer<NostrRequest> {
```
> يُعرِّف صنفاً باسم مُسلسِل الطلب (RequestSerializer) يحقّق الواجهة JsonSerializer ذات النوع NostrRequest، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:33]

```
34:         override fun serialize(src: NostrRequest, typeOfSrc: Type, context: JsonSerializationContext): JsonElement {
```
> يُعيد تعريف (override) دالة serialize التي تأخذ المصدر src من نوع NostrRequest، ونوع المصدر typeOfSrc من نوع Type، وسياق context من نوع JsonSerializationContext، وتُعيد قيمة من نوع JsonElement، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:34]

```
35:             val array = JsonArray()
```
> يُعرِّف متغيّراً للقراءة فقط باسم array ويُسنِد إليه كائن JsonArray جديداً. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:35]

```
36:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:36]

```
37:             when (src) {
```
> يبدأ تعبير when يفحص قيمة المصدر src، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:37]

```
38:                 is Event -> {
```
> فرع when: إذا كان src من النوع Event، ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:38]

```
39:                     array.add("EVENT")
```
> يستدعي add على array مضيفاً النص "EVENT". [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:39]

```
40:                     array.add(context.serialize(src.event))
```
> يستدعي add على array مضيفاً ناتج استدعاء context.serialize على src.event. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:40]

```
41:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:41]

```
42:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:42]

```
43:                 is Subscribe -> {
```
> فرع when: إذا كان src من النوع Subscribe، ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:43]

```
44:                     array.add("REQ")
```
> يستدعي add على array مضيفاً النص "REQ". [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:44]

```
45:                     array.add(src.subscriptionId)
```
> يستدعي add على array مضيفاً src.subscriptionId. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:45]

```
46:                     src.filters.forEach { filter ->
```
> يستدعي forEach على src.filters ويفتح كتلة لامبدا (lambda) معاملها filter. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:46]

```
47:                         array.add(context.serialize(filter, NostrFilter::class.java))
```
> يستدعي add على array مضيفاً ناتج استدعاء context.serialize على filter بنوع الصنف NostrFilter (NostrFilter::class.java). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:47]

```
48:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:48]

```
49:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:49]

```
50:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:50]

```
51:                 is Close -> {
```
> فرع when: إذا كان src من النوع Close، ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:51]

```
52:                     array.add("CLOSE")
```
> يستدعي add على array مضيفاً النص "CLOSE". [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:52]

```
53:                     array.add(src.subscriptionId)
```
> يستدعي add على array مضيفاً src.subscriptionId. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:53]

```
54:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:54]

```
55:             }
```
> إغلاق نطاق (نهاية تعبير when). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:55]

```
56:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:56]

```
57:             return array
```
> يُعيد (return) المتغيّر array. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:57]

```
58:         }
```
> إغلاق نطاق (نهاية دالة serialize). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:58]

```
59:     }
```
> إغلاق نطاق (نهاية الصنف RequestSerializer). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:59]

```
60:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:60]

```
61:     companion object {
```
> يُعرِّف كائناً مرافقاً (companion object) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:61]

```
62:         /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:62]

```
63:          * Create Gson instance with proper serializers
```
> تعليق: إنشاء نسخة Gson مع المُسلسِلات المناسبة. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:63]

```
64:          */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:64]

```
65:         fun createGson(): Gson {
```
> يُعرِّف دالة باسم إنشاء Gson (createGson) لا تأخذ معاملات وتُعيد قيمة من نوع Gson، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:65]

```
66:             return GsonBuilder()
```
> يبدأ عبارة return بإنشاء كائن GsonBuilder جديد. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:66]

```
67:                 .registerTypeAdapter(NostrRequest::class.java, RequestSerializer())
```
> يستدعي registerTypeAdapter مسجّلاً لنوع الصنف NostrRequest محوّلاً هو كائن RequestSerializer جديد. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:67]

```
68:                 .registerTypeAdapter(NostrFilter::class.java, NostrFilter.FilterSerializer())
```
> يستدعي registerTypeAdapter مسجّلاً لنوع الصنف NostrFilter محوّلاً هو كائن NostrFilter.FilterSerializer جديد. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:68]

```
69:                 .disableHtmlEscaping()
```
> يستدعي disableHtmlEscaping (تعطيل تهريب HTML). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:69]

```
70:                 .create()
```
> يستدعي create لإنشاء كائن Gson النهائي المُعاد. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:70]

```
71:         }
```
> إغلاق نطاق (نهاية دالة createGson). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:71]

```
72:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:72]

```
73:         /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:73]

```
74:          * Serialize request to JSON string
```
> تعليق: تسلسل الطلب إلى سلسلة JSON نصية. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:74]

```
75:          */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:75]

```
76:         fun toJson(request: NostrRequest): String {
```
> يُعرِّف دالة باسم toJson تأخذ معاملاً باسم request من نوع NostrRequest وتُعيد قيمة من نوع نص (String)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:76]

```
77:             return createGson().toJson(request)
```
> يُعيد ناتج استدعاء toJson على كائن createGson() مع تمرير request. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:77]

```
78:         }
```
> إغلاق نطاق (نهاية دالة toJson). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:78]

```
79:     }
```
> إغلاق نطاق (نهاية الكائن المرافق). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:79]

```
80: }
```
> إغلاق نطاق (نهاية الصنف NostrRequest). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:80]

```
81: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:81]

```
82: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:82]

```
83:  * Nostr protocol response messages
```
> تعليق: رسائل استجابة بروتوكول Nostr. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:83]

```
84:  * Handles EVENT, EOSE, OK, and NOTICE responses
```
> تعليق: يعالج استجابات EVENT و EOSE و OK و NOTICE. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:84]

```
85:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:85]

```
86: sealed class NostrResponse {
```
> يُعرِّف صنفاً مختوماً (sealed class) باسم استجابة Nostr (NostrResponse) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:86]

```
87:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:87]

```
88:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:88]

```
89:      * EVENT response - received event from subscription
```
> تعليق: استجابة EVENT - حدث مُستلَم من الاشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:89]

```
90:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:90]

```
91:     data class Event(
```
> يُعرِّف صنف بيانات باسم حدث (Event) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:91]

```
92:         val subscriptionId: String,
```
> يُعرِّف خاصية للقراءة فقط باسم subscriptionId من نوع نص. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:92]

```
93:         val event: NostrEvent
```
> يُعرِّف خاصية للقراءة فقط باسم event من نوع NostrEvent. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:93]

```
94:     ) : NostrResponse()
```
> يغلق قائمة المعاملات ويجعل الصنف Event يرث من NostrResponse. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:94]

```
95:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:95]

```
96:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:96]

```
97:      * EOSE response - end of stored events
```
> تعليق: استجابة EOSE - نهاية الأحداث المخزَّنة. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:97]

```
98:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:98]

```
99:     data class EndOfStoredEvents(
```
> يُعرِّف صنف بيانات باسم نهاية الأحداث المخزَّنة (EndOfStoredEvents) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:99]

```
100:         val subscriptionId: String
```
> يُعرِّف خاصية للقراءة فقط باسم subscriptionId من نوع نص. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:100]

```
101:     ) : NostrResponse()
```
> يغلق قائمة المعاملات ويجعل الصنف EndOfStoredEvents يرث من NostrResponse. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:101]

```
102:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:102]

```
103:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:103]

```
104:      * OK response - event publication result
```
> تعليق: استجابة OK - نتيجة نشر الحدث. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:104]

```
105:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:105]

```
106:     data class Ok(
```
> يُعرِّف صنف بيانات باسم موافقة/نجاح (Ok) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:106]

```
107:         val eventId: String,
```
> يُعرِّف خاصية للقراءة فقط باسم معرّف الحدث (eventId) من نوع نص. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:107]

```
108:         val accepted: Boolean,
```
> يُعرِّف خاصية للقراءة فقط باسم مقبول (accepted) من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:108]

```
109:         val message: String?
```
> يُعرِّف خاصية للقراءة فقط باسم رسالة (message) من نوع نص قابل أن يكون فارغاً (String?). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:109]

```
110:     ) : NostrResponse()
```
> يغلق قائمة المعاملات ويجعل الصنف Ok يرث من NostrResponse. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:110]

```
111:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:111]

```
112:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:112]

```
113:      * NOTICE response - relay notice
```
> تعليق: استجابة NOTICE - إشعار من المُرحِّل (relay). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:113]

```
114:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:114]

```
115:     data class Notice(
```
> يُعرِّف صنف بيانات باسم إشعار (Notice) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:115]

```
116:         val message: String
```
> يُعرِّف خاصية للقراءة فقط باسم message من نوع نص. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:116]

```
117:     ) : NostrResponse()
```
> يغلق قائمة المعاملات ويجعل الصنف Notice يرث من NostrResponse. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:117]

```
118:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:118]

```
119:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:119]

```
120:      * Unknown response type
```
> تعليق: نوع استجابة غير معروف. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:120]

```
121:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:121]

```
122:     data class Unknown(
```
> يُعرِّف صنف بيانات باسم غير معروف (Unknown) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:122]

```
123:         val raw: String
```
> يُعرِّف خاصية للقراءة فقط باسم خام (raw) من نوع نص. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:123]

```
124:     ) : NostrResponse()
```
> يغلق قائمة المعاملات ويجعل الصنف Unknown يرث من NostrResponse. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:124]

```
125:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:125]

```
126:     companion object {
```
> يُعرِّف كائناً مرافقاً (companion object) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:126]

```
127:         /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:127]

```
128:          * Parse JSON array response
```
> تعليق: تحليل استجابة مصفوفة JSON. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:128]

```
129:          */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:129]

```
130:         fun fromJsonArray(jsonArray: JsonArray): NostrResponse {
```
> يُعرِّف دالة باسم fromJsonArray تأخذ معاملاً باسم jsonArray من نوع JsonArray وتُعيد قيمة من نوع NostrResponse، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:130]

```
131:             return try {
```
> يبدأ عبارة return بكتلة try (محاولة) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:131]

```
132:                 when (val type = jsonArray[0].asString) {
```
> يبدأ تعبير when يُعرّف داخله متغيّراً للقراءة فقط باسم type يُسنَد إليه العنصر الأول من jsonArray كنص (asString)، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:132]

```
133:                     "EVENT" -> {
```
> فرع when: إذا ساوى type النص "EVENT"، ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:133]

```
134:                         if (jsonArray.size() >= 3) {
```
> يبدأ شرط if يفحص ما إذا كان حجم jsonArray (size()) أكبر من أو يساوي 3، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:134]

```
135:                             val subscriptionId = jsonArray[1].asString
```
> يُعرِّف متغيّراً للقراءة فقط باسم subscriptionId ويُسنِد إليه العنصر الثاني من jsonArray كنص. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:135]

```
136:                             val eventJson = jsonArray[2].asJsonObject
```
> يُعرِّف متغيّراً للقراءة فقط باسم eventJson ويُسنِد إليه العنصر الثالث من jsonArray ككائن JSON (asJsonObject). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:136]

```
137:                             val event = parseEventFromJson(eventJson)
```
> يُعرِّف متغيّراً للقراءة فقط باسم event ويُسنِد إليه ناتج استدعاء parseEventFromJson على eventJson. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:137]

```
138:                             Event(subscriptionId, event)
```
> يُنشئ كائن Event بتمرير subscriptionId و event (وهو قيمة الفرع). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:138]

```
139:                         } else {
```
> يغلق نطاق if ويفتح نطاق else (وإلا). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:139]

```
140:                             Unknown(jsonArray.toString())
```
> يُنشئ كائن Unknown بتمرير ناتج jsonArray.toString() (وهو قيمة الفرع). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:140]

```
141:                         }
```
> إغلاق نطاق (نهاية else). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:141]

```
142:                     }
```
> إغلاق نطاق (نهاية فرع "EVENT"). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:142]

```
143:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:143]

```
144:                     "EOSE" -> {
```
> فرع when: إذا ساوى type النص "EOSE"، ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:144]

```
145:                         if (jsonArray.size() >= 2) {
```
> يبدأ شرط if يفحص ما إذا كان حجم jsonArray أكبر من أو يساوي 2، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:145]

```
146:                             val subscriptionId = jsonArray[1].asString
```
> يُعرِّف متغيّراً للقراءة فقط باسم subscriptionId ويُسنِد إليه العنصر الثاني من jsonArray كنص. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:146]

```
147:                             EndOfStoredEvents(subscriptionId)
```
> يُنشئ كائن EndOfStoredEvents بتمرير subscriptionId (وهو قيمة الفرع). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:147]

```
148:                         } else {
```
> يغلق نطاق if ويفتح نطاق else. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:148]

```
149:                             Unknown(jsonArray.toString())
```
> يُنشئ كائن Unknown بتمرير ناتج jsonArray.toString() (وهو قيمة الفرع). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:149]

```
150:                         }
```
> إغلاق نطاق (نهاية else). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:150]

```
151:                     }
```
> إغلاق نطاق (نهاية فرع "EOSE"). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:151]

```
152:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:152]

```
153:                     "OK" -> {
```
> فرع when: إذا ساوى type النص "OK"، ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:153]

```
154:                         if (jsonArray.size() >= 3) {
```
> يبدأ شرط if يفحص ما إذا كان حجم jsonArray أكبر من أو يساوي 3، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:154]

```
155:                             val eventId = jsonArray[1].asString
```
> يُعرِّف متغيّراً للقراءة فقط باسم eventId ويُسنِد إليه العنصر الثاني من jsonArray كنص. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:155]

```
156:                             val accepted = jsonArray[2].asBoolean
```
> يُعرِّف متغيّراً للقراءة فقط باسم accepted ويُسنِد إليه العنصر الثالث من jsonArray كقيمة منطقية (asBoolean). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:156]

```
157:                             val message = if (jsonArray.size() >= 4) {
```
> يُعرِّف متغيّراً للقراءة فقط باسم message ويُسنِد إليه نتيجة تعبير if يفحص ما إذا كان حجم jsonArray أكبر من أو يساوي 4، ويفتح نطاق فرع الصواب. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:157]

```
158:                                 jsonArray[3].asString
```
> يأخذ العنصر الرابع من jsonArray كنص (قيمة فرع الصواب). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:158]

```
159:                             } else null
```
> يغلق نطاق فرع الصواب، وفي حالة else تكون القيمة null. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:159]

```
160:                             Ok(eventId, accepted, message)
```
> يُنشئ كائن Ok بتمرير eventId و accepted و message (وهو قيمة الفرع). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:160]

```
161:                         } else {
```
> يغلق نطاق if ويفتح نطاق else. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:161]

```
162:                             Unknown(jsonArray.toString())
```
> يُنشئ كائن Unknown بتمرير ناتج jsonArray.toString() (وهو قيمة الفرع). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:162]

```
163:                         }
```
> إغلاق نطاق (نهاية else). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:163]

```
164:                     }
```
> إغلاق نطاق (نهاية فرع "OK"). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:164]

```
165:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:165]

```
166:                     "NOTICE" -> {
```
> فرع when: إذا ساوى type النص "NOTICE"، ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:166]

```
167:                         if (jsonArray.size() >= 2) {
```
> يبدأ شرط if يفحص ما إذا كان حجم jsonArray أكبر من أو يساوي 2، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:167]

```
168:                             val message = jsonArray[1].asString
```
> يُعرِّف متغيّراً للقراءة فقط باسم message ويُسنِد إليه العنصر الثاني من jsonArray كنص. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:168]

```
169:                             Notice(message)
```
> يُنشئ كائن Notice بتمرير message (وهو قيمة الفرع). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:169]

```
170:                         } else {
```
> يغلق نطاق if ويفتح نطاق else. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:170]

```
171:                             Unknown(jsonArray.toString())
```
> يُنشئ كائن Unknown بتمرير ناتج jsonArray.toString() (وهو قيمة الفرع). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:171]

```
172:                         }
```
> إغلاق نطاق (نهاية else). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:172]

```
173:                     }
```
> إغلاق نطاق (نهاية فرع "NOTICE"). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:173]

```
174:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:174]

```
175:                     else -> Unknown(jsonArray.toString())
```
> فرع when الافتراضي else: يُنشئ كائن Unknown بتمرير ناتج jsonArray.toString(). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:175]

```
176:                 }
```
> إغلاق نطاق (نهاية تعبير when). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:176]

```
177:             } catch (e: Exception) {
```
> يغلق نطاق try ويفتح كتلة catch (التقاط) لاستثناء باسم e من نوع Exception. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:177]

```
178:                 Unknown(jsonArray.toString())
```
> يُنشئ كائن Unknown بتمرير ناتج jsonArray.toString() (وهو قيمة كتلة catch). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:178]

```
179:             }
```
> إغلاق نطاق (نهاية كتلة catch). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:179]

```
180:         }
```
> إغلاق نطاق (نهاية دالة fromJsonArray). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:180]

```
181:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:181]

```
182:         private fun parseEventFromJson(jsonObject: JsonObject): NostrEvent {
```
> يُعرِّف دالة خاصة (private) باسم parseEventFromJson تأخذ معاملاً باسم jsonObject من نوع JsonObject وتُعيد قيمة من نوع NostrEvent، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:182]

```
183:             return NostrEvent(
```
> يبدأ عبارة return بإنشاء كائن NostrEvent ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:183]

```
184:                 id = jsonObject.get("id")?.asString ?: "",
```
> يُسنِد للوسيط id قيمة جلب المفتاح "id" من jsonObject كنص، أو نصاً فارغاً "" إن كان null. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:184]

```
185:                 pubkey = jsonObject.get("pubkey")?.asString ?: "",
```
> يُسنِد للوسيط pubkey (المفتاح العام) قيمة جلب المفتاح "pubkey" من jsonObject كنص، أو نصاً فارغاً "" إن كان null. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:185]

```
186:                 createdAt = jsonObject.get("created_at")?.asInt ?: 0,
```
> يُسنِد للوسيط createdAt (وقت الإنشاء) قيمة جلب المفتاح "created_at" من jsonObject كعدد صحيح (asInt)، أو 0 إن كان null. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:186]

```
187:                 kind = jsonObject.get("kind")?.asInt ?: 0,
```
> يُسنِد للوسيط kind (النوع) قيمة جلب المفتاح "kind" من jsonObject كعدد صحيح، أو 0 إن كان null. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:187]

```
188:                 tags = parseTagsFromJson(jsonObject.get("tags")?.asJsonArray),
```
> يُسنِد للوسيط tags (الوسوم) ناتج استدعاء parseTagsFromJson على قيمة جلب المفتاح "tags" من jsonObject كمصفوفة JSON (asJsonArray). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:188]

```
189:                 content = jsonObject.get("content")?.asString ?: "",
```
> يُسنِد للوسيط content (المحتوى) قيمة جلب المفتاح "content" من jsonObject كنص، أو نصاً فارغاً "" إن كان null. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:189]

```
190:                 sig = jsonObject.get("sig")?.asString
```
> يُسنِد للوسيط sig (التوقيع) قيمة جلب المفتاح "sig" من jsonObject كنص (قد تكون null). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:190]

```
191:             )
```
> إغلاق نطاق (نهاية قائمة وسائط NostrEvent). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:191]

```
192:         }
```
> إغلاق نطاق (نهاية دالة parseEventFromJson). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:192]

```
193:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:193]

```
194:         private fun parseTagsFromJson(tagsArray: JsonArray?): List<List<String>> {
```
> يُعرِّف دالة خاصة (private) باسم parseTagsFromJson تأخذ معاملاً باسم tagsArray من نوع JsonArray قابل أن يكون null، وتُعيد قائمة من قوائم نصوص (List<List<String>>)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:194]

```
195:             if (tagsArray == null) return emptyList()
```
> شرط if: إذا كان tagsArray يساوي null يُعيد قائمة فارغة (emptyList()). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:195]

```
196:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:196]

```
197:             return try {
```
> يبدأ عبارة return بكتلة try ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:197]

```
198:                 tagsArray.map { tagElement ->
```
> يستدعي map على tagsArray ويفتح كتلة لامبدا معاملها tagElement. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:198]

```
199:                     if (tagElement.isJsonArray) {
```
> شرط if: يفحص ما إذا كان tagElement مصفوفة JSON (isJsonArray)، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:199]

```
200:                         val tagArray = tagElement.asJsonArray
```
> يُعرِّف متغيّراً للقراءة فقط باسم tagArray ويُسنِد إليه tagElement كمصفوفة JSON (asJsonArray). [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:200]
