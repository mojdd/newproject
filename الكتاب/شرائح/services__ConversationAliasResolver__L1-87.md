# شريحة — app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt (الأسطر 1–87)

```
1: package com.bitchat.android.services
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.services`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:2]

```
3: import com.bitchat.android.ui.ChatState
```
> يستورد (import) الصنف `ChatState` من الحزمة `com.bitchat.android.ui`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:4]

```
5: object ConversationAliasResolver {
```
> يعرّف كائناً مفرداً (object) باسم `ConversationAliasResolver` (محلّل أسماء المحادثات البديلة) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:6]

```
7:     fun resolveCanonicalPeerID(
```
> يعرّف دالة (fun) باسم `resolveCanonicalPeerID` (حلّ المعرّف القياسي للنظير) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:7]

```
8:         selectedPeerID: String,
```
> يعرّف المعامل `selectedPeerID` (المعرّف المختار للنظير) من نوع نصّ `String`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:8]

```
9:         connectedPeers: List<String>,
```
> يعرّف المعامل `connectedPeers` (النظراء المتصلون) من نوع قائمة نصوص `List<String>`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:9]

```
10:         meshNoiseKeyForPeer: (String) -> ByteArray?,
```
> يعرّف المعامل `meshNoiseKeyForPeer` (مفتاح Noise للشبكة لكل نظير) وهو دالة تأخذ نصّاً وتعيد مصفوفة بايتات `ByteArray?` قابلة لأن تكون فارغة (null). [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:10]

```
11:         meshHasPeer: (String) -> Boolean,
```
> يعرّف المعامل `meshHasPeer` (هل الشبكة تملك النظير) وهو دالة تأخذ نصّاً وتعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:11]

```
12:         nostrPubHexForAlias: (String) -> String?,
```
> يعرّف المعامل `nostrPubHexForAlias` (مفتاح Nostr العام بالنظام الستّ عشري للاسم البديل) وهو دالة تأخذ نصّاً وتعيد نصّاً `String?` قابلاً لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:12]

```
13:         findNoiseKeyForNostr: (String) -> ByteArray?
```
> يعرّف المعامل `findNoiseKeyForNostr` (إيجاد مفتاح Noise مقابل Nostr) وهو دالة تأخذ نصّاً وتعيد مصفوفة بايتات `ByteArray?` قابلة لأن تكون فارغة. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:13]

```
14:     ): String {
```
> يغلق قائمة المعاملات ويحدّد أن نوع القيمة المُعادة من الدالة هو نصّ `String`، ثم يفتح جسم الدالة. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:14]

```
15:         var peer = selectedPeerID
```
> يعرّف متغيّراً قابلاً للتغيير (var) باسم `peer` ويسند إليه قيمة `selectedPeerID`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:15]

```
16:         try {
```
> يفتح كتلة محاولة (try) لتنفيذ الكود الذي قد يرمي استثناءً. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:16]

```
17:             if (peer.startsWith("nostr_")) {
```
> يفحص ما إذا كان `peer` يبدأ بالنصّ `"nostr_"`، وإذا تحقّق يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:17]

```
18:                 val pubHex = nostrPubHexForAlias(peer)
```
> يعرّف ثابتاً (val) باسم `pubHex` ويسند إليه ناتج استدعاء الدالة `nostrPubHexForAlias` بالوسيط `peer`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:18]

```
19:                 if (pubHex != null) {
```
> يفحص ما إذا كان `pubHex` ليس فارغاً (null)، وإذا تحقّق يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:19]

```
20:                     val noiseKey = findNoiseKeyForNostr(pubHex)
```
> يعرّف ثابتاً باسم `noiseKey` (مفتاح Noise) ويسند إليه ناتج استدعاء الدالة `findNoiseKeyForNostr` بالوسيط `pubHex`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:20]

```
21:                     if (noiseKey != null) {
```
> يفحص ما إذا كان `noiseKey` ليس فارغاً (null)، وإذا تحقّق يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:21]

```
22:                         val noiseHex = noiseKey.joinToString("") { b -> "%02x".format(b) }
```
> يعرّف ثابتاً باسم `noiseHex` (مفتاح Noise بالنظام الستّ عشري) ويسند إليه دمج بايتات `noiseKey` في نصّ واحد بلا فاصل، إذ يُحوّل كل بايت `b` إلى نصّ ستّ عشري من خانتين عبر `"%02x".format(b)`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:22]

```
23:                         // Prefer a connected mesh peer that matches this noise key
```
> تعليق: فضّل نظير شبكة متصلاً يطابق مفتاح Noise هذا. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:23]

```
24:                         val meshPeer = connectedPeers.firstOrNull { pid ->
```
> يعرّف ثابتاً باسم `meshPeer` (نظير الشبكة) ويسند إليه أوّل عنصر من `connectedPeers` يحقّق الشرط أو فارغاً إن لم يوجد (firstOrNull)، حيث يُسمّى كل عنصر `pid`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:24]

```
25:                             meshNoiseKeyForPeer(pid)?.contentEquals(noiseKey) == true
```
> الشرط: استدعاء `meshNoiseKeyForPeer(pid)` ثم مقارنة محتواه مع `noiseKey` عبر `contentEquals` بشرط ألا يكون فارغاً، وأن تساوي النتيجة `true`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:25]

```
26:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:26]

```
27:                         peer = meshPeer ?: noiseHex
```
> يسند إلى `peer` قيمة `meshPeer`، وإن كانت فارغة (null) فيسند قيمة `noiseHex` بدلاً عنها عبر معامل الدمج (?:). [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:27]

```
28:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:28]

```
29:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:29]

```
30:             } else if (peer.length == 64 && peer.matches(Regex("^[0-9a-fA-F]+$"))) {
```
> يغلق كتلة الشرط السابقة ويفتح شرطاً بديلاً (else if): إذا كان طول `peer` يساوي 64 وكان يطابق التعبير النمطي `^[0-9a-fA-F]+$` (نصّ ستّ عشري فقط)، يفتح كتلته. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:30]

```
31:                 // Peer is full noise key hex: upgrade to active mesh peer if available
```
> تعليق: النظير هو مفتاح Noise كامل بالنظام الستّ عشري؛ رقِّه إلى نظير شبكة نشط إن توفّر. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:31]

```
32:                 val noiseKey = peer.chunked(2).map { it.toInt(16).toByte() }.toByteArray()
```
> يعرّف ثابتاً باسم `noiseKey` ويسند إليه: تقطيع `peer` إلى مقاطع من خانتين (chunked(2))، ثم تحويل كل مقطع `it` من نصّ ستّ عشري إلى عدد صحيح بأساس 16 ثم إلى بايت، ثم جمعها في مصفوفة بايتات (toByteArray). [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:32]

```
33:                 val meshPeer = connectedPeers.firstOrNull { pid ->
```
> يعرّف ثابتاً باسم `meshPeer` ويسند إليه أوّل عنصر من `connectedPeers` يحقّق الشرط أو فارغاً إن لم يوجد (firstOrNull)، حيث يُسمّى كل عنصر `pid`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:33]

```
34:                     meshNoiseKeyForPeer(pid)?.contentEquals(noiseKey) == true
```
> الشرط: استدعاء `meshNoiseKeyForPeer(pid)` ثم مقارنة محتواه مع `noiseKey` عبر `contentEquals` بشرط ألا يكون فارغاً، وأن تساوي النتيجة `true`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:34]

```
35:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:35]

```
36:                 if (meshPeer != null) {
```
> يفحص ما إذا كان `meshPeer` ليس فارغاً (null)، وإذا تحقّق يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:36]

```
37:                     peer = meshPeer
```
> يسند إلى `peer` قيمة `meshPeer`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:37]

```
38:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:38]

```
39:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:39]

```
40:         } catch (_: Exception) { /* no-op */ }
```
> يغلق كتلة المحاولة (try) ويفتح كتلة التقاط (catch) لأيّ استثناء `Exception` بمعامل مُهمَل (_)، وجسمها فارغ يحوي تعليقاً: لا عملية (no-op). [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:40]

```
41:         return peer
```
> يُعيد قيمة `peer` من الدالة. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:41]

```
42:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:42]

```
43: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:43]

```
44:     fun unifyChatsIntoPeer(
```
> يعرّف دالة باسم `unifyChatsIntoPeer` (توحيد المحادثات داخل نظير) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:44]

```
45:         state: ChatState,
```
> يعرّف المعامل `state` (الحالة) من نوع `ChatState`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:45]

```
46:         targetPeerID: String,
```
> يعرّف المعامل `targetPeerID` (المعرّف الهدف للنظير) من نوع نصّ `String`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:46]

```
47:         keysToMerge: List<String>
```
> يعرّف المعامل `keysToMerge` (المفاتيح المراد دمجها) من نوع قائمة نصوص `List<String>`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:47]

```
48:     ) {
```
> يغلق قائمة المعاملات ويفتح جسم الدالة (بلا قيمة مُعادة محدّدة). [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:48]

```
49:         if (keysToMerge.isEmpty()) return
```
> يفحص ما إذا كانت `keysToMerge` فارغة (isEmpty)، وإذا تحقّق يُنهي الدالة بـ return. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:49]

```
50:         val currentChats = state.getPrivateChatsValue().toMutableMap()
```
> يعرّف ثابتاً باسم `currentChats` (المحادثات الحالية) ويسند إليه ناتج استدعاء `state.getPrivateChatsValue()` محوّلاً إلى خريطة قابلة للتعديل (toMutableMap). [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:50]

```
51:         val targetList = currentChats[targetPeerID]?.toMutableList() ?: mutableListOf()
```
> يعرّف ثابتاً باسم `targetList` (القائمة الهدف) ويسند إليه قيمة `currentChats` عند المفتاح `targetPeerID` محوّلة إلى قائمة قابلة للتعديل، وإن كانت فارغة (null) فقائمة فارغة قابلة للتعديل عبر `mutableListOf()`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:51]

```
52:         var didMerge = false
```
> يعرّف متغيّراً قابلاً للتغيير باسم `didMerge` (هل تمّ الدمج) ويسند إليه قيمة `false`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:52]

```
53:         keysToMerge.distinct().forEach { key ->
```
> يأخذ القيم الفريدة من `keysToMerge` عبر `distinct()` ثم يكرّر على كل عنصر مُسمّى `key` عبر `forEach`، ويفتح جسم التكرار. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:53]

```
54:             if (key == targetPeerID) return@forEach
```
> يفحص ما إذا كان `key` يساوي `targetPeerID`، وإذا تحقّق يتخطّى الدورة الحالية من `forEach` عبر `return@forEach`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:54]

```
55:             val list = currentChats[key]
```
> يعرّف ثابتاً باسم `list` (القائمة) ويسند إليه قيمة `currentChats` عند المفتاح `key`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:55]

```
56:             if (!list.isNullOrEmpty()) {
```
> يفحص ما إذا كانت `list` ليست فارغة ولا null (نفي isNullOrEmpty)، وإذا تحقّق يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:56]

```
57:                 targetList.addAll(list)
```
> يضيف كل عناصر `list` إلى `targetList` عبر `addAll`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:57]

```
58:                 currentChats.remove(key)
```
> يحذف المُدخَل ذا المفتاح `key` من `currentChats` عبر `remove`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:58]

```
59:                 didMerge = true
```
> يسند إلى `didMerge` قيمة `true`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:59]

```
60:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:60]

```
61:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:61]

```
62:         if (didMerge) {
```
> يفحص ما إذا كانت `didMerge` صحيحة (true)، وإذا تحقّق يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:62]

```
63:             // Preserve arrival order; do not sort by timestamp
```
> تعليق: حافظ على ترتيب الوصول؛ لا تُرتّب حسب الطابع الزمني. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:63]

```
64:             currentChats[targetPeerID] = targetList
```
> يسند `targetList` إلى `currentChats` عند المفتاح `targetPeerID`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:64]

```
65:             state.setPrivateChats(currentChats)
```
> يستدعي `state.setPrivateChats` بالوسيط `currentChats`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:65]

```
66: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:66]

```
67:             // Move unread flags
```
> تعليق: انقل أعلام غير المقروء. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:67]

```
68:             val unread = state.getUnreadPrivateMessagesValue().toMutableSet()
```
> يعرّف ثابتاً باسم `unread` (غير المقروء) ويسند إليه ناتج استدعاء `state.getUnreadPrivateMessagesValue()` محوّلاً إلى مجموعة قابلة للتعديل (toMutableSet). [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:68]

```
69:             var hadUnread = false
```
> يعرّف متغيّراً قابلاً للتغيير باسم `hadUnread` (هل كان هناك غير مقروء) ويسند إليه قيمة `false`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:69]

```
70:             keysToMerge.forEach { key -> if (unread.remove(key)) hadUnread = true }
```
> يكرّر على كل عنصر مُسمّى `key` من `keysToMerge` عبر `forEach`، وإن نجح حذف `key` من `unread` عبر `remove` أُسند إلى `hadUnread` قيمة `true`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:70]

```
71:             if (hadUnread) unread.add(targetPeerID)
```
> يفحص ما إذا كانت `hadUnread` صحيحة، وإذا تحقّق يضيف `targetPeerID` إلى `unread` عبر `add`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:71]

```
72:             state.setUnreadPrivateMessages(unread)
```
> يستدعي `state.setUnreadPrivateMessages` بالوسيط `unread`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:72]

```
73: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:73]

```
74:             // Switch selection if currently viewing an alias that got merged
```
> تعليق: بدّل التحديد إذا كان المعروض حالياً اسماً بديلاً تمّ دمجه. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:74]

```
75:             val selected = state.getSelectedPrivateChatPeerValue()
```
> يعرّف ثابتاً باسم `selected` (المُحدَّد) ويسند إليه ناتج استدعاء `state.getSelectedPrivateChatPeerValue()`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:75]

```
76:             if (selected != null && keysToMerge.contains(selected)) {
```
> يفحص ما إذا كان `selected` ليس فارغاً (null) وكانت `keysToMerge` تحتوي `selected` عبر `contains`، وإذا تحقّق الشرطان يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:76]

```
77:                 state.setSelectedPrivateChatPeer(targetPeerID)
```
> يستدعي `state.setSelectedPrivateChatPeer` بالوسيط `targetPeerID`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:77]

```
78:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:78]

```
79:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:79]

```
80:             // Switch sheet peer if currently viewing an alias that got merged
```
> تعليق: بدّل نظير الورقة (sheet) إذا كان المعروض حالياً اسماً بديلاً تمّ دمجه. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:80]

```
81:             val sheetPeer = state.getPrivateChatSheetPeerValue()
```
> يعرّف ثابتاً باسم `sheetPeer` (نظير الورقة) ويسند إليه ناتج استدعاء `state.getPrivateChatSheetPeerValue()`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:81]

```
82:             if (sheetPeer != null && keysToMerge.contains(sheetPeer)) {
```
> يفحص ما إذا كان `sheetPeer` ليس فارغاً (null) وكانت `keysToMerge` تحتوي `sheetPeer` عبر `contains`، وإذا تحقّق الشرطان يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:82]

```
83:                 state.setPrivateChatSheetPeer(targetPeerID)
```
> يستدعي `state.setPrivateChatSheetPeer` بالوسيط `targetPeerID`. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:83]

```
84:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:84]

```
85:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:85]

```
86:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:86]

```
87: }
```
> إغلاق نطاق (نهاية الكائن `ConversationAliasResolver`). [app/src/main/java/com/bitchat/android/services/ConversationAliasResolver.kt:87]
