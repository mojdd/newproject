# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يُعلِن أن هذا الملف يتبع الحزمة (package) باسم com.bitchat.android.nostr. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:2]

```
3: import com.google.gson.Gson
```
> يستورد (import) الصنف Gson من مكتبة com.google.gson. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:3]

```
4: import com.google.gson.GsonBuilder
```
> يستورد الصنف GsonBuilder من مكتبة com.google.gson. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:4]

```
5: import com.google.gson.annotations.SerializedName
```
> يستورد التعليق التوضيحي SerializedName من مكتبة com.google.gson.annotations. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:5]

```
6: import java.security.MessageDigest
```
> يستورد الصنف MessageDigest (مُلخِّص الرسالة) من java.security. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:6]

```
7: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:7]

```
8: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:8]

```
9:  * Nostr Event structure following NIP-01
```
> تعليق: «بنية حدث Nostr تتبع المعيار NIP-01». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:9]

```
10:  * Compatible with iOS implementation
```
> تعليق: «متوافقة مع تطبيق iOS». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:10]

```
11:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:11]

```
12: data class NostrEvent(
```
> يُعرِّف صنف بيانات (data class) باسم NostrEvent مع بداية قائمة معاملات الباني (constructor). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:12]

```
13:     var id: String = "",
```
> يُعرِّف خاصية متغيّرة (var) باسم id من نوع String بقيمة ابتدائية نص فارغ "". [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:13]

```
14:     val pubkey: String,
```
> يُعرِّف خاصية ثابتة (val) باسم pubkey (المفتاح العام) من نوع String بلا قيمة ابتدائية. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:14]

```
15:     @SerializedName("created_at") val createdAt: Int,
```
> يُعرِّف خاصية ثابتة باسم createdAt من نوع Int، مع تسمية تسلسل (SerializedName) في JSON باسم "created_at". [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:15]

```
16:     val kind: Int,
```
> يُعرِّف خاصية ثابتة باسم kind (النوع) من نوع Int. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:16]

```
17:     val tags: List<List<String>>,
```
> يُعرِّف خاصية ثابتة باسم tags (الوسوم) من نوع قائمة من قوائم نصوص List<List<String>>. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:17]

```
18:     val content: String,
```
> يُعرِّف خاصية ثابتة باسم content (المحتوى) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:18]

```
19:     var sig: String? = null
```
> يُعرِّف خاصية متغيّرة باسم sig (التوقيع) من نوع String قابل للإفراغ (nullable) بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:19]

```
20: ) {
```
> إغلاق قائمة معاملات الباني وبداية جسم الصنف. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:20]

```
21:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:21]

```
22:     companion object {
```
> يُعرِّف كائناً مرافقاً (companion object) وبداية جسمه. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:22]

```
23:         /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:23]

```
24:          * Create from JSON dictionary
```
> تعليق: «إنشاء من قاموس JSON». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:24]

```
25:          */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:25]

```
26:         fun fromJson(json: Map<String, Any>): NostrEvent? {
```
> يُعرِّف دالة (fun) باسم fromJson تأخذ معامل json من نوع Map<String, Any> وتعيد NostrEvent قابلاً للإفراغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:26]

```
27:             return try {
```
> يبدأ بإعادة (return) نتيجة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:27]

```
28:                 NostrEvent(
```
> يُنشئ مثيلاً من NostrEvent مع بداية قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:28]

```
29:                     id = json["id"] as? String ?: "",
```
> يُسنِد للمعامل id قيمة json["id"] محوّلة بأمان إلى String، وإن فشل فالنص الفارغ "". [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:29]

```
30:                     pubkey = json["pubkey"] as? String ?: return null,
```
> يُسنِد للمعامل pubkey قيمة json["pubkey"] محوّلة بأمان إلى String، وإن فشل فإنه يعيد null. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:30]

```
31:                     createdAt = (json["created_at"] as? Number)?.toInt() ?: return null,
```
> يُسنِد للمعامل createdAt قيمة json["created_at"] محوّلة بأمان إلى Number ثم إلى Int، وإن فشل فإنه يعيد null. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:31]

```
32:                     kind = (json["kind"] as? Number)?.toInt() ?: return null,
```
> يُسنِد للمعامل kind قيمة json["kind"] محوّلة بأمان إلى Number ثم إلى Int، وإن فشل فإنه يعيد null. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:32]

```
33:                     tags = (json["tags"] as? List<List<String>>) ?: return null,
```
> يُسنِد للمعامل tags قيمة json["tags"] محوّلة بأمان إلى List<List<String>>، وإن فشل فإنه يعيد null. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:33]

```
34:                     content = json["content"] as? String ?: return null,
```
> يُسنِد للمعامل content قيمة json["content"] محوّلة بأمان إلى String، وإن فشل فإنه يعيد null. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:34]

```
35:                     sig = json["sig"] as? String?
```
> يُسنِد للمعامل sig قيمة json["sig"] محوّلة بأمان إلى String قابل للإفراغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:35]

```
36:                 )
```
> إغلاق قائمة وسائط باني NostrEvent. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:36]

```
37:             } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) باسم e وبداية كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:37]

```
38:                 null
```
> يُعيد null كقيمة لكتلة try عند وقوع الاستثناء. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:38]

```
39:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:39]

```
40:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:40]

```
41:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:41]

```
42:         /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:42]

```
43:          * Create from JSON string
```
> تعليق: «إنشاء من نص JSON». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:43]

```
44:          */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:44]

```
45:         fun fromJsonString(jsonString: String): NostrEvent? {
```
> يُعرِّف دالة باسم fromJsonString تأخذ معامل jsonString من نوع String وتعيد NostrEvent قابلاً للإفراغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:45]

```
46:             return try {
```
> يبدأ بإعادة نتيجة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:46]

```
47:                 val gson = Gson()
```
> يُعرِّف متغيّراً ثابتاً باسم gson ويُسنِد إليه مثيلاً جديداً من Gson(). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:47]

```
48:                 gson.fromJson(jsonString, NostrEvent::class.java)
```
> يستدعي gson.fromJson مع jsonString وصنف NostrEvent::class.java لينتج مثيلاً منه. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:48]

```
49:             } catch (e: Exception) {
```
> يلتقط استثناءً باسم e وبداية كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:49]

```
50:                 null
```
> يُعيد null كقيمة لكتلة try عند وقوع الاستثناء. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:50]

```
51:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:51]

```
52:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:52]

```
53:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:53]

```
54:         /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:54]

```
55:          * Create a new text note event
```
> تعليق: «إنشاء حدث ملاحظة نصية جديد». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:55]

```
56:          */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:56]

```
57:         fun createTextNote(
```
> يُعرِّف دالة باسم createTextNote مع بداية قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:57]

```
58:             content: String,
```
> يُعرِّف معاملاً باسم content من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:58]

```
59:             publicKeyHex: String,
```
> يُعرِّف معاملاً باسم publicKeyHex (المفتاح العام بالنظام الست عشري) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:59]

```
60:             privateKeyHex: String,
```
> يُعرِّف معاملاً باسم privateKeyHex (المفتاح الخاص بالنظام الست عشري) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:60]

```
61:             tags: List<List<String>> = emptyList(),
```
> يُعرِّف معاملاً باسم tags من نوع List<List<String>> بقيمة ابتدائية قائمة فارغة emptyList(). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:61]

```
62:             createdAt: Int = (System.currentTimeMillis() / 1000).toInt()
```
> يُعرِّف معاملاً باسم createdAt من نوع Int بقيمة ابتدائية: الوقت الحالي بالملّي ثانية System.currentTimeMillis() مقسوماً على 1000 ثم محوّلاً إلى Int. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:62]

```
63:         ): NostrEvent {
```
> إغلاق قائمة المعاملات وتحديد نوع الإرجاع NostrEvent وبداية جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:63]

```
64:             val event = NostrEvent(
```
> يُعرِّف متغيّراً ثابتاً باسم event ويبدأ إسناد مثيل NostrEvent إليه. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:64]

```
65:                 pubkey = publicKeyHex,
```
> يُسنِد للمعامل pubkey قيمة publicKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:65]

```
66:                 createdAt = createdAt,
```
> يُسنِد للمعامل createdAt قيمة المعامل createdAt. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:66]

```
67:                 kind = NostrKind.TEXT_NOTE,
```
> يُسنِد للمعامل kind قيمة الثابت NostrKind.TEXT_NOTE. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:67]

```
68:                 tags = tags,
```
> يُسنِد للمعامل tags قيمة المعامل tags. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:68]

```
69:                 content = content
```
> يُسنِد للمعامل content قيمة المعامل content. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:69]

```
70:             )
```
> إغلاق قائمة وسائط باني NostrEvent. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:70]

```
71:             return event.sign(privateKeyHex)
```
> يُعيد نتيجة استدعاء event.sign مع المعامل privateKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:71]

```
72:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:72]

```
73:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:73]

```
74:         /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:74]

```
75:          * Create a new metadata event (kind 0)
```
> تعليق: «إنشاء حدث بيانات وصفية جديد (النوع 0)». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:75]

```
76:          */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:76]

```
77:         fun createMetadata(
```
> يُعرِّف دالة باسم createMetadata مع بداية قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:77]

```
78:             metadata: String,
```
> يُعرِّف معاملاً باسم metadata (بيانات وصفية) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:78]

```
79:             publicKeyHex: String,
```
> يُعرِّف معاملاً باسم publicKeyHex من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:79]

```
80:             privateKeyHex: String,
```
> يُعرِّف معاملاً باسم privateKeyHex من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:80]

```
81:             createdAt: Int = (System.currentTimeMillis() / 1000).toInt()
```
> يُعرِّف معاملاً باسم createdAt من نوع Int بقيمة ابتدائية: الوقت الحالي بالملّي ثانية مقسوماً على 1000 ثم محوّلاً إلى Int. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:81]

```
82:         ): NostrEvent {
```
> إغلاق قائمة المعاملات وتحديد نوع الإرجاع NostrEvent وبداية جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:82]

```
83:             val event = NostrEvent(
```
> يُعرِّف متغيّراً ثابتاً باسم event ويبدأ إسناد مثيل NostrEvent إليه. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:83]

```
84:                 pubkey = publicKeyHex,
```
> يُسنِد للمعامل pubkey قيمة publicKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:84]

```
85:                 createdAt = createdAt,
```
> يُسنِد للمعامل createdAt قيمة المعامل createdAt. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:85]

```
86:                 kind = NostrKind.METADATA,
```
> يُسنِد للمعامل kind قيمة الثابت NostrKind.METADATA. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:86]

```
87:                 tags = emptyList(),
```
> يُسنِد للمعامل tags قيمة قائمة فارغة emptyList(). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:87]

```
88:                 content = metadata
```
> يُسنِد للمعامل content قيمة المعامل metadata. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:88]

```
89:             )
```
> إغلاق قائمة وسائط باني NostrEvent. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:89]

```
90:             return event.sign(privateKeyHex)
```
> يُعيد نتيجة استدعاء event.sign مع المعامل privateKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:90]

```
91:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:91]

```
92:     }
```
> إغلاق نطاق (نهاية الكائن المرافق). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:92]

```
93:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:93]

```
94:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:94]

```
95:      * Sign event with secp256k1 private key
```
> تعليق: «توقيع الحدث بمفتاح secp256k1 الخاص». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:95]

```
96:      * Returns signed event with id and signature set
```
> تعليق: «يعيد حدثاً موقّعاً مع ضبط المعرّف id والتوقيع signature». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:96]

```
97:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:97]

```
98:     fun sign(privateKeyHex: String): NostrEvent {
```
> يُعرِّف دالة باسم sign تأخذ معامل privateKeyHex من نوع String وتعيد NostrEvent. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:98]

```
99:         val (eventId, eventIdHash) = calculateEventId()
```
> يُعرِّف بالتفكيك (destructuring) متغيّرين ثابتين eventId و eventIdHash من نتيجة استدعاء calculateEventId(). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:99]

```
100:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:100]

```
101:         // Create signature using secp256k1
```
> تعليق: «إنشاء التوقيع باستخدام secp256k1». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:101]

```
102:         val signature = signHash(eventIdHash, privateKeyHex)
```
> يُعرِّف متغيّراً ثابتاً باسم signature ويُسنِد إليه نتيجة استدعاء signHash مع eventIdHash و privateKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:102]

```
103:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:103]

```
104:         return this.copy(
```
> يُعيد نسخة (copy) من الكائن الحالي this مع بداية قائمة التعديلات. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:104]

```
105:             id = eventId,
```
> يُسنِد في النسخة للخاصية id قيمة eventId. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:105]

```
106:             sig = signature
```
> يُسنِد في النسخة للخاصية sig قيمة signature. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:106]

```
107:         )
```
> إغلاق قائمة وسائط copy. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:107]

```
108:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:108]

```
109:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:109]

```
110:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:110]

```
111:      * Compute event ID (NIP-01) without signing
```
> تعليق: «حساب معرّف الحدث (NIP-01) دون توقيع». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:111]

```
112:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:112]

```
113:     fun computeEventIdHex(): String {
```
> يُعرِّف دالة باسم computeEventIdHex بلا معاملات وتعيد String. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:113]

```
114:         val (eventId, _) = calculateEventId()
```
> يُعرِّف بالتفكيك متغيّراً ثابتاً eventId من نتيجة calculateEventId() ويتجاهل العنصر الثاني بالشرطة السفلية _. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:114]

```
115:         return eventId
```
> يُعيد قيمة eventId. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:115]

```
116:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:116]

```
117:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:117]

```
118:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:118]

```
119:      * Calculate event ID according to NIP-01
```
> تعليق: «حساب معرّف الحدث وفق المعيار NIP-01». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:119]

```
120:      * Returns (hex_id, hash_bytes)
```
> تعليق: «يعيد (المعرّف الست عشري hex_id، بايتات التجزئة hash_bytes)». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:120]

```
121:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:121]

```
122:     private fun calculateEventId(): Pair<String, ByteArray> {
```
> يُعرِّف دالة خاصة (private) باسم calculateEventId بلا معاملات وتعيد زوجاً Pair<String, ByteArray>. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:122]

```
123:         // Create serialized array for hashing according to NIP-01
```
> تعليق: «إنشاء مصفوفة مُسلسَلة للتجزئة وفق NIP-01». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:123]

```
124:         val serialized = listOf(
```
> يُعرِّف متغيّراً ثابتاً باسم serialized ويبدأ إسناد قائمة listOf مع بداية عناصرها. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:124]

```
125:             0,
```
> العنصر الأول في القائمة هو الرقم 0. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:125]

```
126:             pubkey,
```
> العنصر التالي في القائمة هو قيمة pubkey. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:126]

```
127:             createdAt,
```
> العنصر التالي في القائمة هو قيمة createdAt. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:127]

```
128:             kind,
```
> العنصر التالي في القائمة هو قيمة kind. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:128]

```
129:             tags,
```
> العنصر التالي في القائمة هو قيمة tags. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:129]

```
130:             content
```
> العنصر الأخير في القائمة هو قيمة content. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:130]

```
131:         )
```
> إغلاق قائمة listOf. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:131]

```
132:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:132]

```
133:         // Convert to JSON without escaping slashes (compact format)
```
> تعليق: «تحويل إلى JSON دون تهريب الشُّرَط المائلة (صيغة مدمجة)». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:133]

```
134:         val gson = GsonBuilder().disableHtmlEscaping().create()
```
> يُعرِّف متغيّراً ثابتاً باسم gson ويُسنِد إليه نتيجة GsonBuilder().disableHtmlEscaping().create() (باني Gson مع تعطيل تهريب HTML). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:134]

```
135:         val jsonString = gson.toJson(serialized)
```
> يُعرِّف متغيّراً ثابتاً باسم jsonString ويُسنِد إليه نتيجة gson.toJson مطبَّقاً على serialized. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:135]

```
136:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:136]

```
137:         // SHA256 hash of the JSON string
```
> تعليق: «تجزئة SHA256 لنص JSON». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:137]

```
138:         val digest = MessageDigest.getInstance("SHA-256")
```
> يُعرِّف متغيّراً ثابتاً باسم digest ويُسنِد إليه مثيل MessageDigest.getInstance لخوارزمية "SHA-256". [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:138]

```
139:         val jsonBytes = jsonString.toByteArray(Charsets.UTF_8)
```
> يُعرِّف متغيّراً ثابتاً باسم jsonBytes ويُسنِد إليه تحويل jsonString إلى مصفوفة بايتات بترميز Charsets.UTF_8. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:139]

```
140:         val hash = digest.digest(jsonBytes)
```
> يُعرِّف متغيّراً ثابتاً باسم hash ويُسنِد إليه نتيجة digest.digest مطبَّقاً على jsonBytes. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:140]

```
141:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:141]

```
142:         // Convert to hex
```
> تعليق: «تحويل إلى النظام الست عشري». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:142]

```
143:         val hexId = hash.joinToString("") { "%02x".format(it) }
```
> يُعرِّف متغيّراً ثابتاً باسم hexId ويُسنِد إليه دمج بايتات hash بفاصل فارغ "" عبر joinToString، إذ يُنسَّق كل بايت it بالصيغة "%02x". [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:143]

```
144:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:144]

```
145:         return Pair(hexId, hash)
```
> يُعيد زوجاً Pair يحوي hexId و hash. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:145]

```
146:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:146]

```
147:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:147]

```
148:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:148]

```
149:      * Sign hash using BIP-340 Schnorr signatures
```
> تعليق: «توقيع التجزئة باستخدام توقيعات Schnorr وفق BIP-340». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:149]

```
150:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:150]

```
151:     private fun signHash(hash: ByteArray, privateKeyHex: String): String {
```
> يُعرِّف دالة خاصة باسم signHash تأخذ معامل hash من نوع ByteArray ومعامل privateKeyHex من نوع String وتعيد String. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:151]

```
152:         return try {
```
> يبدأ بإعادة نتيجة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:152]

```
153:             // Use the real BIP-340 Schnorr signature from NostrCrypto
```
> تعليق: «استخدام توقيع Schnorr الحقيقي وفق BIP-340 من NostrCrypto». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:153]

```
154:             NostrCrypto.schnorrSign(hash, privateKeyHex)
```
> يستدعي NostrCrypto.schnorrSign مع hash و privateKeyHex ليكون قيمة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:154]

```
155:         } catch (e: Exception) {
```
> يلتقط استثناءً باسم e وبداية كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:155]

```
156:             throw RuntimeException("Failed to sign event: ${e.message}", e)
```
> يرمي (throw) استثناء RuntimeException برسالة "Failed to sign event: " متبوعة برسالة الاستثناء ${e.message}، مع تمرير السبب e. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:156]

```
157:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:157]

```
158:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:158]

```
159:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:159]

```
160:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:160]

```
161:      * Convert to JSON string
```
> تعليق: «تحويل إلى نص JSON». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:161]

```
162:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:162]

```
163:     fun toJsonString(): String {
```
> يُعرِّف دالة باسم toJsonString بلا معاملات وتعيد String. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:163]

```
164:         val gson = Gson()
```
> يُعرِّف متغيّراً ثابتاً باسم gson ويُسنِد إليه مثيلاً جديداً من Gson(). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:164]

```
165:         return gson.toJson(this)
```
> يُعيد نتيجة gson.toJson مطبَّقاً على الكائن الحالي this. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:165]

```
166:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:166]

```
167:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:167]

```
168:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:168]

```
169:      * Validate event signature using BIP-340 Schnorr verification
```
> تعليق: «التحقق من توقيع الحدث باستخدام تحقق Schnorr وفق BIP-340». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:169]

```
170:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:170]

```
171:     fun isValidSignature(): Boolean {
```
> يُعرِّف دالة باسم isValidSignature بلا معاملات وتعيد Boolean. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:171]

```
172:         return try {
```
> يبدأ بإعادة نتيجة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:172]

```
173:             val signatureHex = sig ?: return false
```
> يُعرِّف متغيّراً ثابتاً باسم signatureHex ويُسنِد إليه قيمة sig، وإن كانت null فإنه يعيد false. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:173]

```
174:             if (id.isEmpty() || pubkey.isEmpty()) return false
```
> إن كان id فارغاً أو pubkey فارغاً فإنه يعيد false. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:174]

```
175:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:175]

```
176:             // Recalculate the event ID hash for verification
```
> تعليق: «إعادة حساب تجزئة معرّف الحدث للتحقق». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:176]

```
177:             val (calculatedId, messageHash) = calculateEventId()
```
> يُعرِّف بالتفكيك متغيّرين ثابتين calculatedId و messageHash من نتيجة calculateEventId(). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:177]

```
178:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:178]

```
179:             // Check if the calculated ID matches the stored ID
```
> تعليق: «التحقق إن كان المعرّف المحسوب يطابق المعرّف المخزّن». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:179]

```
180:             if (calculatedId != id) return false
```
> إن كان calculatedId لا يساوي id فإنه يعيد false. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:180]

```
181:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:181]

```
182:             // Verify the Schnorr signature
```
> تعليق: «التحقق من توقيع Schnorr». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:182]

```
183:             NostrCrypto.schnorrVerify(messageHash, signatureHex, pubkey)
```
> يستدعي NostrCrypto.schnorrVerify مع messageHash و signatureHex و pubkey ليكون قيمة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:183]

```
184:         } catch (e: Exception) {
```
> يلتقط استثناءً باسم e وبداية كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:184]

```
185:             false
```
> يُعيد false كقيمة لكتلة try عند وقوع الاستثناء. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:185]

```
186:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:186]

```
187:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:187]

```
188:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:188]

```
189:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:189]

```
190:      * Validate event structure and signature
```
> تعليق: «التحقق من بنية الحدث وتوقيعه». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:190]

```
191:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:191]

```
192:     fun isValid(): Boolean {
```
> يُعرِّف دالة باسم isValid بلا معاملات وتعيد Boolean. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:192]

```
193:         return try {
```
> يبدأ بإعادة نتيجة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:193]

```
194:             // Basic field validation
```
> تعليق: «تحقق أساسي من الحقول». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:194]

```
195:             if (pubkey.isEmpty() || content.isEmpty()) return false
```
> إن كان pubkey فارغاً أو content فارغاً فإنه يعيد false. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:195]

```
196:             if (createdAt <= 0 || kind < 0) return false
```
> إن كان createdAt أصغر من أو يساوي 0 أو kind أصغر من 0 فإنه يعيد false. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:196]

```
197:             if (!NostrCrypto.isValidPublicKey(pubkey)) return false
```
> إن كانت NostrCrypto.isValidPublicKey(pubkey) غير صحيحة (نفي) فإنه يعيد false. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:197]

```
198:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:198]

```
199:             // Signature validation
```
> تعليق: «تحقق من التوقيع». [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:199]

```
200:             isValidSignature()
```
> يستدعي isValidSignature() ليكون قيمة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:200]
