# شريحة — app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt (الأسطر 1–51)

```
1: package com.bitchat.android.nostr
```
> يُعرّف انتماء الملف للحُزمة (package) باسم `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من `android.content`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:3]

```
4: import android.content.SharedPreferences
```
> يستورد الصنف `SharedPreferences` (التفضيلات المشتركة) من `android.content`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:4]

```
5: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف `ConcurrentHashMap` (خريطة تجزئة متزامنة) من `java.util.concurrent`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:6]

```
7: /**
```
> تعليق: بداية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:7]

```
8:  * GeohashConversationRegistry
```
> تعليق: «سجل محادثات الجيوهاش (GeohashConversationRegistry)». [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:8]

```
9:  * - Global, thread-safe registry of conversationKey (e.g., "nostr_<pub16>") -> source geohash
```
> تعليق: «سجل عالمي وآمن للخيوط لمفتاح المحادثة (conversationKey) (مثال "nostr_<pub16>") -> جيوهاش المصدر». [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:9]

```
10:  * - Enables routing geohash DMs from anywhere by providing the correct geohash identity
```
> تعليق: «يُمكّن من توجيه الرسائل المباشرة للجيوهاش من أي مكان عبر توفير هوية الجيوهاش الصحيحة». [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:10]

```
11:  * - Persisted to SharedPreferences to survive app restarts.
```
> تعليق: «محفوظ في التفضيلات المشتركة (SharedPreferences) ليبقى بعد إعادة تشغيل التطبيق». [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:11]

```
12:  */
```
> تعليق: نهاية كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:12]

```
13: object GeohashConversationRegistry {
```
> يُعرّف كائناً مفرداً (object) باسم `GeohashConversationRegistry` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:13]

```
14:     private val map = ConcurrentHashMap<String, String>()
```
> يُعرّف خاصية خاصة ثابتة `map` ويضبطها على نسخة جديدة من `ConcurrentHashMap` بمفتاح نصي وقيمة نصية. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:14]

```
15:     private const val PREFS_NAME = "geohash_conversation_registry"
```
> يُعرّف ثابتاً خاصاً وقت التصريف `PREFS_NAME` ويضبط قيمته على النص `"geohash_conversation_registry"`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:15]

```
16:     private var prefs: SharedPreferences? = null
```
> يُعرّف متغيراً خاصاً قابلاً للتغيير `prefs` من نوع `SharedPreferences` القابل لأن يكون فارغاً، ويضبط قيمته الابتدائية على `null`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:17]

```
18:     fun initialize(context: Context) {
```
> يُعرّف دالة `initialize` (تهيئة) تأخذ وسيطاً `context` من نوع `Context` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:18]

```
19:         if (prefs == null) {
```
> يفحص شرطاً: إن كان `prefs` يساوي `null`، ويفتح نطاق الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:19]

```
20:             prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يضبط `prefs` على ناتج استدعاء `context.getSharedPreferences` بالوسيطين `PREFS_NAME` و`Context.MODE_PRIVATE`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:20]

```
21:             loadFromPrefs()
```
> يستدعي الدالة `loadFromPrefs` (التحميل من التفضيلات). [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:21]

```
22:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:22]

```
23:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:24]

```
25:     private fun loadFromPrefs() {
```
> يُعرّف دالة خاصة `loadFromPrefs` بلا وسائط ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:25]

```
26:         prefs?.let { p ->
```
> يستدعي `let` على `prefs` بالاستدعاء الآمن، ويُسمّي القيمة `p`، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:26]

```
27:             val allEntries = p.all
```
> يُعرّف قيمة `allEntries` ويضبطها على خاصية `p.all`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:27]

```
28:             for ((key, value) in allEntries) {
```
> يبدأ حلقة `for` تفكّ كل عنصر في `allEntries` إلى `key` و`value`، ويفتح نطاق الحلقة. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:28]

```
29:                 if (key is String && value is String) {
```
> يفحص شرطاً: إن كان `key` من نوع `String` و`value` من نوع `String`، ويفتح نطاق الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:29]

```
30:                     map[key] = value
```
> يضبط في `map` المدخل ذا المفتاح `key` على القيمة `value`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:30]

```
31:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:31]

```
32:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:32]

```
33:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:33]

```
34:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:34]

```
35: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:35]

```
36:     fun set(convKey: String, geohash: String) {
```
> يُعرّف دالة `set` (ضبط) تأخذ وسيطين `convKey` من نوع `String` و`geohash` من نوع `String` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:36]

```
37:         if (geohash.isNotEmpty()) {
```
> يفحص شرطاً: إن كان `geohash` غير فارغ عبر `isNotEmpty`، ويفتح نطاق الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:37]

```
38:             map[convKey] = geohash
```
> يضبط في `map` المدخل ذا المفتاح `convKey` على القيمة `geohash`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:38]

```
39:             prefs?.edit()?.putString(convKey, geohash)?.apply()
```
> يستدعي بالاستدعاء الآمن على `prefs` الدالة `edit` ثم `putString` بالوسيطين `convKey` و`geohash` ثم `apply`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:39]

```
40:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:40]

```
41:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:41]

```
42: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:42]

```
43:     fun get(convKey: String): String? = map[convKey]
```
> يُعرّف دالة `get` (جلب) تأخذ وسيطاً `convKey` من نوع `String` وتُعيد `String` القابل لأن يكون فارغاً، وقيمتها المُعادة هي `map[convKey]`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:43]

```
44: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:44]

```
45:     fun snapshot(): Map<String, String> = map.toMap()
```
> يُعرّف دالة `snapshot` (لقطة) بلا وسائط تُعيد `Map<String, String>`، وقيمتها المُعادة هي ناتج استدعاء `map.toMap()`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:45]

```
46: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:46]

```
47:     fun clear() {
```
> يُعرّف دالة `clear` (مسح) بلا وسائط ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:47]

```
48:         map.clear()
```
> يستدعي `clear` على `map`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:48]

```
49:         prefs?.edit()?.clear()?.apply()
```
> يستدعي بالاستدعاء الآمن على `prefs` الدالة `edit` ثم `clear` ثم `apply`. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:49]

```
50:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:50]

```
51: }
```
> إغلاق نطاق (نهاية الكائن المفرد `GeohashConversationRegistry`). [app/src/main/java/com/bitchat/android/nostr/GeohashConversationRegistry.kt:51]
