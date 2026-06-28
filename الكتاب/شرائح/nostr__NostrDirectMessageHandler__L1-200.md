# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يُعرّف حُزمة الكود (package) باسم `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:2]

```
3: import android.app.Application
```
> يستورد الصنف `Application` من حزمة `android.app`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` من حزمة `android.util`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:4]

```
5: import com.bitchat.android.model.BitchatFilePacket
```
> يستورد الصنف «حزمة الملف» (BitchatFilePacket) من حزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:5]

```
6: import com.bitchat.android.model.BitchatMessage
```
> يستورد الصنف «الرسالة» (BitchatMessage) من حزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:6]

```
7: import com.bitchat.android.model.DeliveryStatus
```
> يستورد الصنف «حالة التسليم» (DeliveryStatus) من حزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:7]

```
8: import com.bitchat.android.model.NoisePayload
```
> يستورد الصنف «حمولة نويز» (NoisePayload) من حزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:8]

```
9: import com.bitchat.android.model.NoisePayloadType
```
> يستورد الصنف «نوع حمولة نويز» (NoisePayloadType) من حزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:9]

```
10: import com.bitchat.android.model.PrivateMessagePacket
```
> يستورد الصنف «حزمة الرسالة الخاصة» (PrivateMessagePacket) من حزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:10]

```
11: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف «الحزمة» (BitchatPacket) من حزمة `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:11]

```
12: import com.bitchat.android.services.SeenMessageStore
```
> يستورد الصنف «مخزن الرسائل المرئية» (SeenMessageStore) من حزمة `com.bitchat.android.services`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:12]

```
13: import com.bitchat.android.ui.ChatState
```
> يستورد الصنف «حالة الدردشة» (ChatState) من حزمة `com.bitchat.android.ui`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:13]

```
14: import com.bitchat.android.ui.MeshDelegateHandler
```
> يستورد الصنف «معالج وكيل الشبكة» (MeshDelegateHandler) من حزمة `com.bitchat.android.ui`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:14]

```
15: import com.bitchat.android.ui.PrivateChatManager
```
> يستورد الصنف «مدير الدردشة الخاصة» (PrivateChatManager) من حزمة `com.bitchat.android.ui`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:15]

```
16: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف «نطاق التزامن» (CoroutineScope) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:16]

```
17: import kotlinx.coroutines.Dispatchers
```
> يستورد الكائن «الموزِّعات» (Dispatchers) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:17]

```
18: import kotlinx.coroutines.launch
```
> يستورد الدالة «إطلاق» (launch) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:18]

```
19: import kotlinx.coroutines.withContext
```
> يستورد الدالة «بالسياق» (withContext) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:19]

```
20: import java.util.Date
```
> يستورد الصنف «التاريخ» (Date) من حزمة `java.util`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:20]

```
21: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:21]

```
22: class NostrDirectMessageHandler(
```
> يُعرّف الصنف «معالج رسائل نوستر المباشرة» (NostrDirectMessageHandler) ويبدأ قائمة معاملات المُنشئ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:22]

```
23:     private val application: Application,
```
> يُعرّف معامل مُنشئ خاصاً ثابتاً `application` من نوع `Application`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:23]

```
24:     private val state: ChatState,
```
> يُعرّف معامل مُنشئ خاصاً ثابتاً `state` من نوع `ChatState`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:24]

```
25:     private val privateChatManager: PrivateChatManager,
```
> يُعرّف معامل مُنشئ خاصاً ثابتاً `privateChatManager` من نوع `PrivateChatManager`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:25]

```
26:     private val meshDelegateHandler: MeshDelegateHandler,
```
> يُعرّف معامل مُنشئ خاصاً ثابتاً `meshDelegateHandler` من نوع `MeshDelegateHandler`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:26]

```
27:     private val scope: CoroutineScope,
```
> يُعرّف معامل مُنشئ خاصاً ثابتاً `scope` من نوع `CoroutineScope`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:27]

```
28:     private val repo: GeohashRepository,
```
> يُعرّف معامل مُنشئ خاصاً ثابتاً `repo` من نوع `GeohashRepository`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:28]

```
29:     private val dataManager: com.bitchat.android.ui.DataManager
```
> يُعرّف معامل مُنشئ خاصاً ثابتاً `dataManager` من نوع `com.bitchat.android.ui.DataManager`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:29]

```
30: ) {
```
> يُغلق قائمة معاملات المُنشئ ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:30]

```
31:     companion object { private const val TAG = "NostrDirectMessageHandler" }
```
> يُعرّف كائناً مرافقاً (companion object) يحوي ثابتاً خاصاً `TAG` بقيمة نصية `"NostrDirectMessageHandler"`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:31]

```
32: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:32]

```
33:     private val seenStore by lazy { SeenMessageStore.getInstance(application) }
```
> يُعرّف خاصية خاصة ثابتة `seenStore` تُهيَّأ بكسل (lazy) باستدعاء `SeenMessageStore.getInstance(application)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:33]

```
34: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:34]

```
35:     // Simple event deduplication
```
> تعليق: إزالة تكرار الأحداث بطريقة بسيطة. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:35]

```
36:     private val processedIds = ArrayDeque<String>()
```
> يُعرّف خاصية خاصة ثابتة `processedIds` من نوع `ArrayDeque<String>` مُهيَّأة بكائن جديد فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:36]

```
37:     private val seen = HashSet<String>()
```
> يُعرّف خاصية خاصة ثابتة `seen` من نوع `HashSet<String>` مُهيَّأة بكائن جديد فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:37]

```
38:     private val max = 2000
```
> يُعرّف خاصية خاصة ثابتة `max` بقيمة عددية `2000`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:38]

```
39: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:39]

```
40:     private fun dedupe(id: String): Boolean {
```
> يُعرّف دالة خاصة `dedupe` تأخذ معاملاً `id` من نوع `String` وتُعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:40]

```
41:         if (seen.contains(id)) return true
```
> إذا كانت المجموعة `seen` تحتوي على `id` فأعِد `true`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:41]

```
42:         seen.add(id)
```
> يُضيف `id` إلى المجموعة `seen`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:42]

```
43:         processedIds.addLast(id)
```
> يُضيف `id` إلى آخر الطابور `processedIds`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:43]

```
44:         if (processedIds.size > max) {
```
> إذا كان حجم `processedIds` أكبر من `max` فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:44]

```
45:             val old = processedIds.removeFirst()
```
> يُسند إلى المتغيّر الثابت `old` العنصر المُزال من أول الطابور `processedIds`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:45]

```
46:             seen.remove(old)
```
> يُزيل `old` من المجموعة `seen`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:46]

```
47:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:47]

```
48:         return false
```
> يُعيد `false`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:48]

```
49:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:49]

```
50: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:50]

```
51:     fun onGiftWrap(giftWrap: NostrEvent, geohash: String, identity: NostrIdentity) {
```
> يُعرّف دالة عامة `onGiftWrap` تأخذ المعاملات `giftWrap` من نوع `NostrEvent` و`geohash` من نوع `String` و`identity` من نوع `NostrIdentity`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:51]

```
52:         scope.launch(Dispatchers.Default) {
```
> يُطلق تزامناً (coroutine) على النطاق `scope` باستخدام الموزِّع `Dispatchers.Default` ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:52]

```
53:             try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:53]

```
54:                 if (dedupe(giftWrap.id)) return@launch
```
> إذا أعادت `dedupe(giftWrap.id)` قيمة `true` فاخرج من التزامن بـ`return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:54]

```
55: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:55]

```
56:                 val messageAge = System.currentTimeMillis() / 1000 - giftWrap.createdAt
```
> يُسند إلى المتغيّر الثابت `messageAge` ناتج طرح `giftWrap.createdAt` من الوقت الحالي بالملّي مقسوماً على `1000`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:56]

```
57:                 if (messageAge > 173700) return@launch // 48 hours + 15 mins
```
> إذا كان `messageAge` أكبر من `173700` فاخرج من التزامن بـ`return@launch`؛ تعليق: ٤٨ ساعة + ١٥ دقيقة. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:57]

```
58: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:58]

```
59:                 val decryptResult = NostrProtocol.decryptPrivateMessage(giftWrap, identity)
```
> يُسند إلى المتغيّر الثابت `decryptResult` ناتج استدعاء `NostrProtocol.decryptPrivateMessage(giftWrap, identity)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:59]

```
60:                 if (decryptResult == null) {
```
> إذا كان `decryptResult` يساوي `null` فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:60]

```
61:                     Log.w(TAG, "Failed to decrypt Nostr message")
```
> يسجّل تحذيراً (Log.w) بالوسم `TAG` ونصّ `"Failed to decrypt Nostr message"`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:61]

```
62:                     return@launch
```
> يخرج من التزامن بـ`return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:62]

```
63:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:63]

```
64: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:64]

```
65:                 val (content, rawSenderPubkey, rumorTimestamp) = decryptResult
```
> يُفكّك `decryptResult` إلى المتغيّرات الثابتة `content` و`rawSenderPubkey` و`rumorTimestamp`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:65]

```
66:                 val senderPubkey = rawSenderPubkey.lowercase()
```
> يُسند إلى المتغيّر الثابت `senderPubkey` ناتج تحويل `rawSenderPubkey` إلى أحرف صغيرة بـ`lowercase()`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:66]

```
67: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:67]

```
68:                 // If sender is blocked for geohash contexts, drop any events from this pubkey
```
> تعليق: إذا كان المرسِل محظوراً في سياقات الجيوهاش، أسقِط أي أحداث من هذا المفتاح العام. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:68]

```
69:                 // Applies to both geohash DMs (geohash != "") and account DMs (geohash == "")
```
> تعليق: ينطبق على رسائل الجيوهاش المباشرة (geohash != "") ورسائل الحساب المباشرة (geohash == "") معاً. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:69]

```
70:                 if (dataManager.isGeohashUserBlocked(senderPubkey)) return@launch
```
> إذا أعادت `dataManager.isGeohashUserBlocked(senderPubkey)` قيمة `true` فاخرج من التزامن بـ`return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:70]

```
71:                 if (!content.startsWith("bitchat1:")) return@launch
```
> إذا كان `content` لا يبدأ بالنص `"bitchat1:"` فاخرج من التزامن بـ`return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:71]

```
72: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:72]

```
73:                 val base64Content = content.removePrefix("bitchat1:")
```
> يُسند إلى المتغيّر الثابت `base64Content` ناتج إزالة البادئة `"bitchat1:"` من `content`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:73]

```
74:                 val packetData = base64URLDecode(base64Content) ?: return@launch
```
> يُسند إلى المتغيّر الثابت `packetData` ناتج `base64URLDecode(base64Content)`، وإن كان `null` فاخرج من التزامن بـ`return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:74]

```
75:                 val packet = BitchatPacket.fromBinaryData(packetData) ?: return@launch
```
> يُسند إلى المتغيّر الثابت `packet` ناتج `BitchatPacket.fromBinaryData(packetData)`، وإن كان `null` فاخرج من التزامن بـ`return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:75]

```
76: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:76]

```
77:                 if (packet.type != com.bitchat.android.protocol.MessageType.NOISE_ENCRYPTED.value) return@launch
```
> إذا كان `packet.type` لا يساوي `com.bitchat.android.protocol.MessageType.NOISE_ENCRYPTED.value` فاخرج من التزامن بـ`return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:77]

```
78: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:78]

```
79:                 val noisePayload = NoisePayload.decode(packet.payload) ?: return@launch
```
> يُسند إلى المتغيّر الثابت `noisePayload` ناتج `NoisePayload.decode(packet.payload)`، وإن كان `null` فاخرج من التزامن بـ`return@launch`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:79]

```
80:                 val messageTimestamp = Date(giftWrap.createdAt * 1000L)
```
> يُسند إلى المتغيّر الثابت `messageTimestamp` كائن `Date` مُنشأ من `giftWrap.createdAt` مضروباً في `1000L`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:80]

```
81:                 val convKey = "nostr_${senderPubkey.take(16)}"
```
> يُسند إلى المتغيّر الثابت `convKey` نصاً مكوّناً من `"nostr_"` متبوعاً بأول ١٦ حرفاً من `senderPubkey` عبر `take(16)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:81]

```
82:                 repo.putNostrKeyMapping(convKey, senderPubkey)
```
> يستدعي `repo.putNostrKeyMapping(convKey, senderPubkey)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:82]

```
83:                 com.bitchat.android.nostr.GeohashAliasRegistry.put(convKey, senderPubkey)
```
> يستدعي `com.bitchat.android.nostr.GeohashAliasRegistry.put(convKey, senderPubkey)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:83]

```
84:                 if (geohash.isNotEmpty()) {
```
> إذا كان `geohash` غير فارغ بـ`isNotEmpty()` فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:84]

```
85:                     // Remember which geohash this conversation belongs to so we can subscribe on-demand
```
> تعليق: تذكّر إلى أي جيوهاش تنتمي هذه المحادثة لنتمكّن من الاشتراك عند الطلب. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:85]

```
86:                     repo.setConversationGeohash(convKey, geohash)
```
> يستدعي `repo.setConversationGeohash(convKey, geohash)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:86]

```
87:                     GeohashConversationRegistry.set(convKey, geohash)
```
> يستدعي `GeohashConversationRegistry.set(convKey, geohash)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:87]

```
88:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:88]

```
89: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:89]

```
90:                 // Ensure sender appears in geohash people list even if they haven't posted publicly yet
```
> تعليق: تأكّد من ظهور المرسِل في قائمة أشخاص الجيوهاش حتى لو لم ينشر علناً بعد. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:90]

```
91:                 if (geohash.isNotEmpty()) {
```
> إذا كان `geohash` غير فارغ بـ`isNotEmpty()` فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:91]

```
92:                     // Cache a best-effort nickname and mark as participant
```
> تعليق: خزّن في الذاكرة المؤقتة اسماً مستعاراً بأفضل جهد ووسمه كمشارِك. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:92]

```
93:                     val cached = repo.getCachedNickname(senderPubkey)
```
> يُسند إلى المتغيّر الثابت `cached` ناتج `repo.getCachedNickname(senderPubkey)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:93]

```
94:                     if (cached == null) {
```
> إذا كان `cached` يساوي `null` فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:94]

```
95:                         val base = repo.displayNameForNostrPubkeyUI(senderPubkey).substringBefore("#")
```
> يُسند إلى المتغيّر الثابت `base` الجزء قبل العلامة `"#"` من ناتج `repo.displayNameForNostrPubkeyUI(senderPubkey)` عبر `substringBefore("#")`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:95]

```
96:                         repo.cacheNickname(senderPubkey, base)
```
> يستدعي `repo.cacheNickname(senderPubkey, base)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:96]

```
97:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:97]

```
98:                     repo.updateParticipant(geohash, senderPubkey, messageTimestamp)
```
> يستدعي `repo.updateParticipant(geohash, senderPubkey, messageTimestamp)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:98]

```
99:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:99]

```
100: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:100]

```
101:                 val senderNickname = repo.displayNameForNostrPubkeyUI(senderPubkey)
```
> يُسند إلى المتغيّر الثابت `senderNickname` ناتج `repo.displayNameForNostrPubkeyUI(senderPubkey)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:101]

```
102: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:102]

```
103:                 processNoisePayload(noisePayload, convKey, senderNickname, messageTimestamp, senderPubkey, identity)
```
> يستدعي `processNoisePayload` بالوسائط `noisePayload` و`convKey` و`senderNickname` و`messageTimestamp` و`senderPubkey` و`identity`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:103]

```
104: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:104]

```
105:             } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:105]

```
106:                 Log.e(TAG, "onGiftWrap error: ${e.message}")
```
> يسجّل خطأً (Log.e) بالوسم `TAG` ونصّ `"onGiftWrap error: "` متبوعاً بـ`e.message`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:106]

```
107:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:107]

```
108:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:108]

```
109:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:109]

```
110: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:110]

```
111:     private suspend fun processNoisePayload(
```
> يُعرّف دالة خاصة معلّقة (suspend) باسم `processNoisePayload` ويبدأ قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:111]

```
112:         payload: NoisePayload,
```
> يُعرّف المعامل `payload` من نوع `NoisePayload`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:112]

```
113:         convKey: String,
```
> يُعرّف المعامل `convKey` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:113]

```
114:         senderNickname: String,
```
> يُعرّف المعامل `senderNickname` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:114]

```
115:         timestamp: Date,
```
> يُعرّف المعامل `timestamp` من نوع `Date`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:115]

```
116:         senderPubkey: String,
```
> يُعرّف المعامل `senderPubkey` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:116]

```
117:         recipientIdentity: NostrIdentity
```
> يُعرّف المعامل `recipientIdentity` من نوع `NostrIdentity`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:117]

```
118:     ) {
```
> يُغلق قائمة المعاملات ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:118]

```
119:         when (payload.type) {
```
> يبدأ تعبير `when` على `payload.type`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:119]

```
120:             NoisePayloadType.PRIVATE_MESSAGE -> {
```
> فرع `when` لقيمة `NoisePayloadType.PRIVATE_MESSAGE` يفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:120]

```
121:                 val pm = PrivateMessagePacket.decode(payload.data) ?: return
```
> يُسند إلى المتغيّر الثابت `pm` ناتج `PrivateMessagePacket.decode(payload.data)`، وإن كان `null` فأعِد من الدالة بـ`return`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:121]

```
122:                 val existingMessages = state.getPrivateChatsValue()[convKey] ?: emptyList()
```
> يُسند إلى المتغيّر الثابت `existingMessages` قيمة المفتاح `convKey` من `state.getPrivateChatsValue()`، وإن كانت `null` فقائمة فارغة بـ`emptyList()`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:122]

```
123:                 if (existingMessages.any { it.id == pm.messageID }) return
```
> إذا احتوى `existingMessages` على أي عنصر معرّفه `it.id` يساوي `pm.messageID` فأعِد من الدالة بـ`return`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:123]

```
124: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:124]

```
125:                 val message = BitchatMessage(
```
> يُسند إلى المتغيّر الثابت `message` كائن `BitchatMessage` جديد ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:125]

```
126:                     id = pm.messageID,
```
> يضبط الوسيط `id` بقيمة `pm.messageID`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:126]

```
127:                     sender = senderNickname,
```
> يضبط الوسيط `sender` بقيمة `senderNickname`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:127]

```
128:                     content = pm.content,
```
> يضبط الوسيط `content` بقيمة `pm.content`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:128]

```
129:                     timestamp = timestamp,
```
> يضبط الوسيط `timestamp` بقيمة المعامل `timestamp`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:129]

```
130:                     isRelay = false,
```
> يضبط الوسيط `isRelay` بقيمة `false`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:130]

```
131:                     isPrivate = true,
```
> يضبط الوسيط `isPrivate` بقيمة `true`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:131]

```
132:                     recipientNickname = state.getNicknameValue(),
```
> يضبط الوسيط `recipientNickname` بقيمة `state.getNicknameValue()`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:132]

```
133:                     senderPeerID = convKey,
```
> يضبط الوسيط `senderPeerID` بقيمة `convKey`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:133]

```
134:                     deliveryStatus = DeliveryStatus.Delivered(to = state.getNicknameValue() ?: "Unknown", at = Date())
```
> يضبط الوسيط `deliveryStatus` بقيمة `DeliveryStatus.Delivered` حيث `to` هو `state.getNicknameValue()` أو `"Unknown"` إن كان `null`، و`at` كائن `Date` جديد. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:134]

```
135:                 )
```
> يُغلق قائمة وسائط `BitchatMessage`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:135]

```
136: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:136]

```
137:                 val isViewing = state.getSelectedPrivateChatPeerValue() == convKey
```
> يُسند إلى المتغيّر الثابت `isViewing` نتيجة المقارنة بين `state.getSelectedPrivateChatPeerValue()` و`convKey`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:137]

```
138:                 val suppressUnread = seenStore.hasRead(pm.messageID)
```
> يُسند إلى المتغيّر الثابت `suppressUnread` ناتج `seenStore.hasRead(pm.messageID)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:138]

```
139: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:139]

```
140:                 withContext(Dispatchers.Main) {
```
> يستدعي `withContext` بالموزِّع `Dispatchers.Main` ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:140]

```
141:                     privateChatManager.handleIncomingPrivateMessage(message, suppressUnread)
```
> يستدعي `privateChatManager.handleIncomingPrivateMessage(message, suppressUnread)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:141]

```
142:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:142]

```
143: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:143]

```
144:                 if (!seenStore.hasDelivered(pm.messageID)) {
```
> إذا كان `seenStore.hasDelivered(pm.messageID)` يساوي `false` فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:144]

```
145:                     val nostrTransport = NostrTransport.getInstance(application)
```
> يُسند إلى المتغيّر الثابت `nostrTransport` ناتج `NostrTransport.getInstance(application)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:145]

```
146:                     nostrTransport.sendDeliveryAckGeohash(pm.messageID, senderPubkey, recipientIdentity)
```
> يستدعي `nostrTransport.sendDeliveryAckGeohash(pm.messageID, senderPubkey, recipientIdentity)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:146]

```
147:                     seenStore.markDelivered(pm.messageID)
```
> يستدعي `seenStore.markDelivered(pm.messageID)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:147]

```
148:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:148]

```
149: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:149]

```
150:                 if (isViewing && !suppressUnread) {
```
> إذا كان `isViewing` صحيحاً و`suppressUnread` يساوي `false` فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:150]

```
151:                     val nostrTransport = NostrTransport.getInstance(application)
```
> يُسند إلى المتغيّر الثابت `nostrTransport` ناتج `NostrTransport.getInstance(application)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:151]

```
152:                     nostrTransport.sendReadReceiptGeohash(pm.messageID, senderPubkey, recipientIdentity)
```
> يستدعي `nostrTransport.sendReadReceiptGeohash(pm.messageID, senderPubkey, recipientIdentity)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:152]

```
153:                     seenStore.markRead(pm.messageID)
```
> يستدعي `seenStore.markRead(pm.messageID)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:153]

```
154:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:154]

```
155:             }
```
> إغلاق نطاق فرع `PRIVATE_MESSAGE`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:155]

```
156:             NoisePayloadType.DELIVERED -> {
```
> فرع `when` لقيمة `NoisePayloadType.DELIVERED` يفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:156]

```
157:                 val messageId = String(payload.data, Charsets.UTF_8)
```
> يُسند إلى المتغيّر الثابت `messageId` نصاً مُنشأ من `payload.data` بترميز `Charsets.UTF_8`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:157]

```
158:                 withContext(Dispatchers.Main) {
```
> يستدعي `withContext` بالموزِّع `Dispatchers.Main` ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:158]

```
159:                     meshDelegateHandler.didReceiveDeliveryAck(messageId, convKey)
```
> يستدعي `meshDelegateHandler.didReceiveDeliveryAck(messageId, convKey)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:159]

```
160:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:160]

```
161:             }
```
> إغلاق نطاق فرع `DELIVERED`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:161]

```
162:             NoisePayloadType.READ_RECEIPT -> {
```
> فرع `when` لقيمة `NoisePayloadType.READ_RECEIPT` يفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:162]

```
163:                 val messageId = String(payload.data, Charsets.UTF_8)
```
> يُسند إلى المتغيّر الثابت `messageId` نصاً مُنشأ من `payload.data` بترميز `Charsets.UTF_8`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:163]

```
164:                 withContext(Dispatchers.Main) {
```
> يستدعي `withContext` بالموزِّع `Dispatchers.Main` ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:164]

```
165:                     meshDelegateHandler.didReceiveReadReceipt(messageId, convKey)
```
> يستدعي `meshDelegateHandler.didReceiveReadReceipt(messageId, convKey)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:165]

```
166:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:166]

```
167:             }
```
> إغلاق نطاق فرع `READ_RECEIPT`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:167]

```
168:             NoisePayloadType.FILE_TRANSFER -> {
```
> فرع `when` لقيمة `NoisePayloadType.FILE_TRANSFER` يفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:168]

```
169:                 // Properly handle encrypted file transfer
```
> تعليق: عالِج نقل الملف المشفّر بشكل صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:169]

```
170:                 val file = BitchatFilePacket.decode(payload.data)
```
> يُسند إلى المتغيّر الثابت `file` ناتج `BitchatFilePacket.decode(payload.data)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:170]

```
171:                 if (file != null) {
```
> إذا كان `file` لا يساوي `null` فابدأ الكتلة التالية. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:171]

```
172:                     val uniqueMsgId = java.util.UUID.randomUUID().toString().uppercase()
```
> يُسند إلى المتغيّر الثابت `uniqueMsgId` نصاً من معرّف فريد `UUID.randomUUID()` محوّلاً إلى نص بـ`toString()` ثم إلى أحرف كبيرة بـ`uppercase()`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:172]

```
173:                     val savedPath = com.bitchat.android.features.file.FileUtils.saveIncomingFile(application, file)
```
> يُسند إلى المتغيّر الثابت `savedPath` ناتج `com.bitchat.android.features.file.FileUtils.saveIncomingFile(application, file)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:173]

```
174:                     val message = BitchatMessage(
```
> يُسند إلى المتغيّر الثابت `message` كائن `BitchatMessage` جديد ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:174]

```
175:                         id = uniqueMsgId,
```
> يضبط الوسيط `id` بقيمة `uniqueMsgId`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:175]

```
176:                         sender = senderNickname,
```
> يضبط الوسيط `sender` بقيمة `senderNickname`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:176]

```
177:                         content = savedPath,
```
> يضبط الوسيط `content` بقيمة `savedPath`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:177]

```
178:                         type = com.bitchat.android.features.file.FileUtils.messageTypeForMime(file.mimeType),
```
> يضبط الوسيط `type` بقيمة `com.bitchat.android.features.file.FileUtils.messageTypeForMime(file.mimeType)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:178]

```
179:                         timestamp = timestamp,
```
> يضبط الوسيط `timestamp` بقيمة المعامل `timestamp`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:179]

```
180:                         isRelay = false,
```
> يضبط الوسيط `isRelay` بقيمة `false`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:180]

```
181:                         isPrivate = true,
```
> يضبط الوسيط `isPrivate` بقيمة `true`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:181]

```
182:                         recipientNickname = state.getNicknameValue(),
```
> يضبط الوسيط `recipientNickname` بقيمة `state.getNicknameValue()`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:182]

```
183:                         senderPeerID = convKey
```
> يضبط الوسيط `senderPeerID` بقيمة `convKey`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:183]

```
184:                     )
```
> يُغلق قائمة وسائط `BitchatMessage`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:184]

```
185:                     Log.d(TAG, "📄 Saved Nostr encrypted incoming file to $savedPath (msgId=$uniqueMsgId)")
```
> يسجّل تصحيحاً (Log.d) بالوسم `TAG` ونصّ يحوي رمز ملف ثم `"Saved Nostr encrypted incoming file to "` متبوعاً بـ`savedPath` و`(msgId=`متبوعاً بـ`uniqueMsgId)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:185]

```
186:                     withContext(Dispatchers.Main) {
```
> يستدعي `withContext` بالموزِّع `Dispatchers.Main` ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:186]

```
187:                         privateChatManager.handleIncomingPrivateMessage(message, suppressUnread = false)
```
> يستدعي `privateChatManager.handleIncomingPrivateMessage(message, suppressUnread = false)`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:187]

```
188:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:188]

```
189:                 } else {
```
> يُغلق كتلة `if` ويبدأ كتلة `else`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:189]

```
190:                     Log.w(TAG, "⚠️ Failed to decode Nostr file transfer from $convKey")
```
> يسجّل تحذيراً (Log.w) بالوسم `TAG` ونصّ يحوي رمز تحذير ثم `"Failed to decode Nostr file transfer from "` متبوعاً بـ`convKey`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:190]

```
191:                 }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:191]

```
192:             }
```
> إغلاق نطاق فرع `FILE_TRANSFER`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:192]

```
193:             NoisePayloadType.VERIFY_CHALLENGE,
```
> يبدأ فرع `when` بقيمة `NoisePayloadType.VERIFY_CHALLENGE` (مجموعاً مع قيمة السطر التالي). [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:193]

```
194:             NoisePayloadType.VERIFY_RESPONSE -> Unit // Ignore verification payloads in Nostr direct messages
```
> فرع `when` للقيمة `NoisePayloadType.VERIFY_RESPONSE` (مع القيمة السابقة) يُعيد `Unit`؛ تعليق: تجاهل حمولات التحقّق في رسائل نوستر المباشرة. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:194]

```
195:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:195]

```
196:     }
```
> إغلاق نطاق دالة `processNoisePayload`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:196]

```
197: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:197]

```
198:     private fun base64URLDecode(input: String): ByteArray? {
```
> يُعرّف دالة خاصة `base64URLDecode` تأخذ معاملاً `input` من نوع `String` وتُعيد `ByteArray?` قابلاً للعدم. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:198]

```
199:         return try {
```
> يبدأ إعادة قيمة من تعبير `try`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:199]

```
200:             val padded = input.replace("-", "+")
```
> يُسند إلى المتغيّر الثابت `padded` ناتج استبدال `"-"` بـ`"+"` في `input` عبر `replace`. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:200]
