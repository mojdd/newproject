# شريحة — app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt (الأسطر 1–50)

```
1: package com.bitchat.android.nostr
```
> يُعرّف الحزمة (package) باسم com.bitchat.android.nostr. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف Context من android.content. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:3]

```
4: import android.content.SharedPreferences
```
> يستورد الصنف SharedPreferences (التفضيلات المشتركة) من android.content. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:4]

```
5: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف ConcurrentHashMap (خريطة التجزئة المتزامنة) من java.util.concurrent. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:6]

```
7: /**
```
> تعليق: بداية تعليق توثيقي (block comment). [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:7]

```
8:  * GeohashAliasRegistry
```
> تعليق: GeohashAliasRegistry. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:8]

```
9:  * - Global, thread-safe registry for alias->Nostr pubkey mappings (e.g., nostr_<pub16> -> pubkeyHex)
```
> تعليق: سجلّ شامل وآمن للخيوط لربط الاسم المستعار بمفتاح Nostr العام (مثال: nostr_<pub16> -> pubkeyHex). [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:9]

```
10:  * - Persisted to SharedPreferences to survive app restarts.
```
> تعليق: محفوظ إلى SharedPreferences لكي يبقى بعد إعادة تشغيل التطبيق. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:10]

```
11:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:11]

```
12: object GeohashAliasRegistry {
```
> يعرّف كائناً مفرداً (object) باسم GeohashAliasRegistry (سجلّ أسماء الجيوهاش المستعارة) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:12]

```
13:     private val map: MutableMap<String, String> = ConcurrentHashMap()
```
> يعرّف خاصية خاصة ثابتة المرجع (val) باسم map من النوع MutableMap<String, String> ويسند إليها كائن ConcurrentHashMap جديداً. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:13]

```
14:     private const val PREFS_NAME = "geohash_alias_registry"
```
> يعرّف ثابتاً خاصاً وقت الترجمة (const val) باسم PREFS_NAME وقيمته السلسلة "geohash_alias_registry". [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:14]

```
15:     private var prefs: SharedPreferences? = null
```
> يعرّف خاصية خاصة قابلة للتغيير (var) باسم prefs من النوع SharedPreferences? القابل للعدم ويسند إليها null. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:16]

```
17:     fun initialize(context: Context) {
```
> يعرّف دالة (fun) باسم initialize تأخذ معاملاً واحداً اسمه context من النوع Context ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:17]

```
18:         if (prefs == null) {
```
> يبدأ جملة شرطية تتحقق من أن prefs يساوي null ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:18]

```
19:             prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
```
> يسند إلى prefs نتيجة استدعاء context.getSharedPreferences مع الوسيطين PREFS_NAME و Context.MODE_PRIVATE. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:19]

```
20:             loadFromPrefs()
```
> يستدعي الدالة loadFromPrefs بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:20]

```
21:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:21]

```
22:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:22]

```
23: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:23]

```
24:     private fun loadFromPrefs() {
```
> يعرّف دالة خاصة باسم loadFromPrefs بلا معاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:24]

```
25:         prefs?.let { p ->
```
> يستدعي let على prefs استدعاءً آمناً من العدم (?.) ويسمّي معامل الدالة الضمنية p ويفتح نطاق الدالة الضمنية. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:25]

```
26:             val allEntries = p.all
```
> يعرّف متغيراً محلياً ثابت المرجع (val) باسم allEntries ويسند إليه خاصية p.all. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:26]

```
27:             for ((key, value) in allEntries) {
```
> يبدأ حلقة for تكرّر على allEntries مفكّكاً كل عنصر إلى key و value ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:27]

```
28:                 if (key is String && value is String) {
```
> يبدأ جملة شرطية تتحقق من أن key من نوع String و value من نوع String ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:28]

```
29:                     map[key] = value
```
> يسند إلى العنصر ذي المفتاح key في map القيمة value. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:29]

```
30:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:30]

```
31:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:31]

```
32:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:32]

```
33:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:33]

```
34: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:34]

```
35:     fun put(alias: String, pubkeyHex: String) {
```
> يعرّف دالة باسم put تأخذ معاملين: alias من النوع String و pubkeyHex من النوع String ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:35]

```
36:         map[alias] = pubkeyHex
```
> يسند إلى العنصر ذي المفتاح alias في map القيمة pubkeyHex. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:36]

```
37:         prefs?.edit()?.putString(alias, pubkeyHex)?.apply()
```
> يستدعي على prefs استدعاءً آمناً من العدم edit ثم putString بالوسيطين alias و pubkeyHex ثم apply. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:37]

```
38:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:38]

```
39: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:39]

```
40:     fun get(alias: String): String? = map[alias]
```
> يعرّف دالة باسم get تأخذ معاملاً alias من النوع String وتعيد قيمة من النوع String? القابل للعدم تساوي map[alias]. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:40]

```
41: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:41]

```
42:     fun contains(alias: String): Boolean = map.containsKey(alias)
```
> يعرّف دالة باسم contains تأخذ معاملاً alias من النوع String وتعيد قيمة منطقية (Boolean) تساوي map.containsKey(alias). [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:42]

```
43: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:43]

```
44:     fun snapshot(): Map<String, String> = HashMap(map)
```
> يعرّف دالة باسم snapshot (لقطة) بلا معاملات وتعيد قيمة من النوع Map<String, String> تساوي كائن HashMap جديداً مبنياً من map. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:44]

```
45: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:45]

```
46:     fun clear() {
```
> يعرّف دالة باسم clear بلا معاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:46]

```
47:         map.clear()
```
> يستدعي clear على map. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:47]

```
48:         prefs?.edit()?.clear()?.apply()
```
> يستدعي على prefs استدعاءً آمناً من العدم edit ثم clear ثم apply. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:48]

```
49:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:49]

```
50: }
```
> إغلاق نطاق (نهاية الكائن المفرد GeohashAliasRegistry). [app/src/main/java/com/bitchat/android/nostr/GeohashAliasRegistry.kt:50]
