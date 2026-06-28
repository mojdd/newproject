# شريحة — app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt (الأسطر 1–111)

```
1: package com.bitchat.android.nostr
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.nostr. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:2]

```
3: import android.app.Application
```
> يستورد (import) الصنف Application من حزمة android.app. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف Log من حزمة android.util. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:4]

```
5: import com.bitchat.android.model.BitchatMessage
```
> يستورد الصنف رسالة-بِتشات (BitchatMessage) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:5]

```
6: import com.bitchat.android.ui.ChatState
```
> يستورد الصنف حالة-المحادثة (ChatState) من حزمة com.bitchat.android.ui. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:6]

```
7: import com.bitchat.android.ui.MessageManager
```
> يستورد الصنف مدير-الرسائل (MessageManager) من حزمة com.bitchat.android.ui. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:7]

```
8: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف نطاق-الكوروتين (CoroutineScope) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:8]

```
9: import kotlinx.coroutines.launch
```
> يستورد الدالة launch من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:9]

```
10: import java.util.Date
```
> يستورد الصنف Date من حزمة java.util. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:11]

```
12: /**
```
> تعليق: بداية كتلة توثيق (تعليق متعدد الأسطر). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:12]

```
13:  * GeohashMessageHandler
```
> تعليق: معالِج-رسائل-الجيوهاش (GeohashMessageHandler). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:13]

```
14:  * - Processes kind=20000 Nostr events for geohash channels
```
> تعليق: يعالج أحداث Nostr من النوع kind=20000 لقنوات الجيوهاش. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:14]

```
15:  * - Updates repository for participants + nicknames
```
> تعليق: يُحدّث المستودع للمشاركين والألقاب. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:15]

```
16:  * - Emits messages to MessageManager
```
> تعليق: يُرسل الرسائل إلى مدير-الرسائل (MessageManager). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:16]

```
17:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:17]

```
18: class GeohashMessageHandler(
```
> يعرّف الصنف معالِج-رسائل-الجيوهاش (GeohashMessageHandler) ويبدأ قائمة معاملات المُنشئ (constructor). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:18]

```
19:     private val application: Application,
```
> يعرّف خاصية مُنشئ خاصة (private val) باسم application من النوع Application. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:19]

```
20:     private val state: ChatState,
```
> يعرّف خاصية مُنشئ خاصة باسم state من النوع حالة-المحادثة (ChatState). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:20]

```
21:     private val messageManager: MessageManager,
```
> يعرّف خاصية مُنشئ خاصة باسم messageManager من النوع مدير-الرسائل (MessageManager). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:21]

```
22:     private val repo: GeohashRepository,
```
> يعرّف خاصية مُنشئ خاصة باسم repo (المستودع) من النوع مستودع-الجيوهاش (GeohashRepository). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:22]

```
23:     private val scope: CoroutineScope,
```
> يعرّف خاصية مُنشئ خاصة باسم scope من النوع نطاق-الكوروتين (CoroutineScope). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:23]

```
24:     private val dataManager: com.bitchat.android.ui.DataManager
```
> يعرّف خاصية مُنشئ خاصة باسم dataManager من النوع مدير-البيانات (DataManager) بمساره الكامل com.bitchat.android.ui.DataManager. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:24]

```
25: ) {
```
> يغلق قائمة معاملات المُنشئ ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:25]

```
26:     companion object { private const val TAG = "GeohashMessageHandler" }
```
> يعرّف كائناً مرافقاً (companion object) يحوي ثابتاً خاصاً (private const val) باسم TAG قيمته السلسلة "GeohashMessageHandler". [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:27]

```
28:     // Simple event deduplication
```
> تعليق: إزالة-تكرار بسيطة للأحداث. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:28]

```
29:     private val processedIds = ArrayDeque<String>()
```
> يعرّف خاصية خاصة باسم processedIds (المعرّفات-المعالَجة) ويهيئها بطابور-مزدوج (ArrayDeque) من سلاسل نصية فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:29]

```
30:     private val seen = HashSet<String>()
```
> يعرّف خاصية خاصة باسم seen (المرئية) ويهيئها بمجموعة-تجزئة (HashSet) من سلاسل نصية فارغة. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:30]

```
31:     private val max = 2000
```
> يعرّف خاصية خاصة باسم max قيمتها العدد 2000. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:31]

```
32: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:32]

```
33:     private fun dedupe(id: String): Boolean {
```
> يعرّف دالة خاصة باسم dedupe (إزالة-التكرار) تأخذ معامل id من نوع سلسلة وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:33]

```
34:         if (seen.contains(id)) return true
```
> إذا كانت مجموعة seen تحتوي المعرّف id فأعِد true. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:34]

```
35:         seen.add(id)
```
> يضيف المعرّف id إلى مجموعة seen. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:35]

```
36:         processedIds.addLast(id)
```
> يضيف المعرّف id إلى آخر طابور processedIds عبر addLast. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:36]

```
37:         if (processedIds.size > max) {
```
> إذا كان حجم processedIds أكبر من max فافتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:37]

```
38:             val old = processedIds.removeFirst()
```
> يعرّف متغيراً محلياً باسم old ويهيئه بنتيجة إزالة أول عنصر من processedIds عبر removeFirst. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:38]

```
39:             seen.remove(old)
```
> يزيل العنصر old من مجموعة seen. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:39]

```
40:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:40]

```
41:         return false
```
> يُعيد القيمة false. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:41]

```
42:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:42]

```
43: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:43]

```
44:     fun onEvent(event: NostrEvent, subscribedGeohash: String) {
```
> يعرّف دالة عامة باسم onEvent (عند-الحدث) تأخذ معاملين: event من النوع حدث-نوستر (NostrEvent) وsubscribedGeohash من نوع سلسلة. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:44]

```
45:         scope.launch {
```
> يستدعي launch على nطاق scope ويفتح كتلة الكوروتين. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:45]

```
46:             try {
```
> يفتح كتلة try (محاولة). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:46]

```
47:                 if (event.kind != NostrKind.EPHEMERAL_EVENT && event.kind != NostrKind.GEOHASH_PRESENCE) return@launch
```
> إذا كان نوع الحدث event.kind لا يساوي EPHEMERAL_EVENT ولا يساوي GEOHASH_PRESENCE فاخرج من الكوروتين عبر return@launch. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:47]

```
48:                 val tagGeo = event.tags.firstOrNull { it.size >= 2 && it[0] == "g" }?.getOrNull(1)
```
> يعرّف متغيراً باسم tagGeo ويهيئه بأول وسم في event.tags حجمه ٢ أو أكثر وعنصره الأول يساوي "g"، ثم يأخذ عنصره عند الفهرس 1 عبر getOrNull. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:48]

```
49:                 if (tagGeo == null || !tagGeo.equals(subscribedGeohash, true)) return@launch
```
> إذا كان tagGeo فارغاً أو لا يساوي subscribedGeohash (مع تجاهل حالة الأحرف بسبب true) فاخرج من الكوروتين. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:49]

```
50:                 if (dedupe(event.id)) return@launch
```
> إذا أعادت dedupe على معرّف الحدث event.id قيمة true فاخرج من الكوروتين. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:50]

```
51: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:51]

```
52:                 // PoW validation (if enabled) - apply to chat messages primarily
```
> تعليق: التحقق من إثبات-العمل (PoW) (إن كان مفعّلاً) - يُطبَّق على رسائل المحادثة بالأساس. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:52]

```
53:                 if (event.kind == NostrKind.EPHEMERAL_EVENT) {
```
> إذا كان نوع الحدث event.kind يساوي EPHEMERAL_EVENT فافتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:53]

```
54:                     val pow = PoWPreferenceManager.getCurrentSettings()
```
> يعرّف متغيراً باسم pow ويهيئه بنتيجة getCurrentSettings من مدير-تفضيلات-إثبات-العمل (PoWPreferenceManager). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:54]

```
55:                     if (pow.enabled && pow.difficulty > 0) {
```
> إذا كانت pow.enabled صحيحة وكانت pow.difficulty أكبر من 0 فافتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:55]

```
56:                         if (!NostrProofOfWork.validateDifficulty(event, pow.difficulty)) return@launch
```
> إذا لم تنجح validateDifficulty من إثبات-العمل-لنوستر (NostrProofOfWork) للحدث event بالصعوبة pow.difficulty فاخرج من الكوروتين. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:56]

```
57:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:57]

```
58:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:58]

```
59: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:59]

```
60:                 // Normalize pubkey to lowercase for consistent blocking and storage
```
> تعليق: توحيد المفتاح-العام (pubkey) إلى أحرف صغيرة لحجب وتخزين متّسقين. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:60]

```
61:                 val pubkey = event.pubkey.lowercase()
```
> يعرّف متغيراً باسم pubkey ويهيئه بمفتاح الحدث event.pubkey بعد تحويله إلى أحرف صغيرة عبر lowercase. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:61]

```
62: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:62]

```
63:                 // Blocked users check (use injected DataManager which has loaded state)
```
> تعليق: فحص المستخدمين المحجوبين (باستخدام مدير-البيانات المحقون الذي حمّل الحالة). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:63]

```
64:                 if (dataManager.isGeohashUserBlocked(pubkey)) return@launch
```
> إذا أعادت isGeohashUserBlocked من dataManager قيمة true للمفتاح pubkey فاخرج من الكوروتين. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:65]

```
66:                 // Update participant count (last seen) on BOTH Presence (20001) and Chat (20000) events
```
> تعليق: تحديث عدد المشاركين (آخر ظهور) على حدثَي الحضور (20001) والمحادثة (20000) معاً. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:66]

```
67:                 if (event.kind == NostrKind.GEOHASH_PRESENCE || event.kind == NostrKind.EPHEMERAL_EVENT) {
```
> إذا كان نوع الحدث event.kind يساوي GEOHASH_PRESENCE أو يساوي EPHEMERAL_EVENT فافتح كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:67]

```
68:                     repo.updateParticipant(subscribedGeohash, pubkey, Date(event.createdAt * 1000L))
```
> يستدعي updateParticipant على المستودع repo بالمعاملات subscribedGeohash وpubkey وتاريخ (Date) ناتج عن ضرب event.createdAt في 1000L. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:68]

```
69:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:69]

```
70:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:70]

```
71:                 event.tags.find { it.size >= 2 && it[0] == "n" }?.let { repo.cacheNickname(pubkey, it[1]) }
```
> يبحث في event.tags عن وسم حجمه ٢ أو أكثر وعنصره الأول يساوي "n"، وإن وُجد يستدعي cacheNickname على repo بالمفتاح pubkey والعنصر الثاني it[1]. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:71]

```
72:                 event.tags.find { it.size >= 2 && it[0] == "t" && it[1] == "teleport" }?.let { repo.markTeleported(pubkey) }
```
> يبحث في event.tags عن وسم حجمه ٢ أو أكثر عنصره الأول "t" وعنصره الثاني "teleport"، وإن وُجد يستدعي markTeleported على repo بالمفتاح pubkey. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:72]

```
73:                 // Register a geohash DM alias for this participant so MessageRouter can route DMs via Nostr
```
> تعليق: تسجيل اسم-بديل (alias) لرسائل خاصة (DM) لهذا المشارك ليتمكّن موجّه-الرسائل (MessageRouter) من توجيه الرسائل الخاصة عبر Nostr. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:73]

```
74:                 try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:74]

```
75:                     com.bitchat.android.nostr.GeohashAliasRegistry.put("nostr_${pubkey.take(16)}", pubkey)
```
> يستدعي put على سجل-أسماء-الجيوهاش-البديلة (GeohashAliasRegistry) بمفتاح هو السلسلة "nostr_" متبوعةً بأول ١٦ حرفاً من pubkey عبر take(16)، وبقيمة pubkey. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:75]

```
76:                 } catch (_: Exception) { }
```
> يلتقط أي استثناء (Exception) بمتغيّر مهمَل ولا يفعل شيئاً. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:76]

```
77: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:77]

```
78:                 // Stop here for presence events - they don't produce chat messages
```
> تعليق: التوقف هنا لأحداث الحضور - فهي لا تُنتج رسائل محادثة. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:78]

```
79:                 if (event.kind == NostrKind.GEOHASH_PRESENCE) return@launch
```
> إذا كان نوع الحدث event.kind يساوي GEOHASH_PRESENCE فاخرج من الكوروتين. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:79]

```
80: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:80]

```
81:                 // Skip our own events for message emission
```
> تعليق: تخطّي أحداثنا الذاتية عند إصدار الرسائل. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:81]

```
82:                 val my = NostrIdentityBridge.deriveIdentity(subscribedGeohash, application)
```
> يعرّف متغيراً باسم my ويهيئه بنتيجة deriveIdentity من جسر-هوية-نوستر (NostrIdentityBridge) بالمعاملين subscribedGeohash وapplication. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:82]

```
83:                 if (my.publicKeyHex.equals(pubkey, true)) return@launch
```
> إذا كان my.publicKeyHex يساوي pubkey (مع تجاهل حالة الأحرف بسبب true) فاخرج من الكوروتين. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:83]

```
84: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:84]

```
85:                 val isTeleportPresence = event.tags.any { it.size >= 2 && it[0] == "t" && it[1] == "teleport" } &&
```
> يعرّف متغيراً باسم isTeleportPresence ويهيئ جزءه الأول بفحص any على event.tags هل يوجد وسم حجمه ٢ أو أكثر عنصره الأول "t" والثاني "teleport"، مع عامل "و" منطقي يتبع في السطر التالي. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:85]

```
86:                                          event.content.trim().isEmpty()
```
> تكملة التعبير السابق: ويكون محتوى الحدث event.content بعد إزالة الفراغات عبر trim فارغاً (isEmpty). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:86]

```
87:                 if (isTeleportPresence) return@launch
```
> إذا كانت isTeleportPresence صحيحة فاخرج من الكوروتين. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:87]

```
88: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:88]

```
89:                 val senderName = repo.displayNameForNostrPubkeyUI(pubkey)
```
> يعرّف متغيراً باسم senderName ويهيئه بنتيجة displayNameForNostrPubkeyUI على repo بالمفتاح pubkey. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:89]

```
90:                 val hasNonce = try { NostrProofOfWork.hasNonce(event) } catch (_: Exception) { false }
```
> يعرّف متغيراً باسم hasNonce ويهيئه بنتيجة hasNonce من إثبات-العمل-لنوستر للحدث event داخل try، وعند أي استثناء يأخذ القيمة false. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:90]

```
91:                 val msg = BitchatMessage(
```
> يعرّف متغيراً باسم msg ويهيئه بإنشاء كائن رسالة-بِتشات (BitchatMessage) ويبدأ تمرير معاملاته. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:91]

```
92:                     id = event.id,
```
> يضبط المعامل id على معرّف الحدث event.id. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:92]

```
93:                     sender = senderName,
```
> يضبط المعامل sender على senderName. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:93]

```
94:                     content = event.content,
```
> يضبط المعامل content على محتوى الحدث event.content. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:94]

```
95:                     timestamp = Date(event.createdAt * 1000L),
```
> يضبط المعامل timestamp على تاريخ (Date) ناتج عن ضرب event.createdAt في 1000L. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:95]

```
96:                     isRelay = false,
```
> يضبط المعامل isRelay على القيمة false. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:96]

```
97:                     originalSender = repo.displayNameForNostrPubkey(pubkey),
```
> يضبط المعامل originalSender على نتيجة displayNameForNostrPubkey على repo بالمفتاح pubkey. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:97]

```
98:                     senderPeerID = "nostr:${pubkey.take(8)}",
```
> يضبط المعامل senderPeerID على السلسلة "nostr:" متبوعةً بأول ٨ أحرف من pubkey عبر take(8). [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:98]

```
99:                     mentions = null,
```
> يضبط المعامل mentions على القيمة null. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:99]

```
100:                     channel = "#$subscribedGeohash",
```
> يضبط المعامل channel على السلسلة "#" متبوعةً بقيمة subscribedGeohash. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:100]

```
101:                     powDifficulty = try {
```
> يضبط المعامل powDifficulty ويبدأ تهيئته بكتلة try. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:101]

```
102:                         if (hasNonce) NostrProofOfWork.calculateDifficulty(event.id).takeIf { it > 0 } else null
```
> إذا كانت hasNonce صحيحة فيحسب calculateDifficulty من إثبات-العمل-لنوستر لمعرّف الحدث event.id ويبقيها بـ takeIf إن كانت أكبر من 0 وإلا null، وإن لم تكن hasNonce صحيحة فالقيمة null. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:102]

```
103:                     } catch (_: Exception) { null }
```
> يلتقط أي استثناء بمتغيّر مهمَل ويُرجع القيمة null لكتلة powDifficulty. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:103]

```
104:                 )
```
> يغلق قائمة معاملات إنشاء رسالة-بِتشات. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:104]

```
105:                 messageManager.addChannelMessage("geo:$subscribedGeohash", msg)
```
> يستدعي addChannelMessage على مدير-الرسائل messageManager بالمفتاح "geo:" متبوعاً بقيمة subscribedGeohash والرسالة msg. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:105]

```
106:             } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) بالمتغيّر e ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:106]

```
107:                 Log.e(TAG, "onEvent error: ${e.message}")
```
> يستدعي Log.e بالوسم TAG والرسالة "onEvent error: " متبوعةً برسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:107]

```
108:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:108]

```
109:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:109]

```
110:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:110]

```
111: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/GeohashMessageHandler.kt:111]
