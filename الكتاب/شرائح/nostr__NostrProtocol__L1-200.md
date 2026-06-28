# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يُعرّف هذا السطر الحزمة (package) باسم `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف `Log` من `android.util`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:3]

```
4: import com.google.gson.Gson
```
> يستورد الصنف `Gson` من `com.google.gson`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:4]

```
5: import com.google.gson.JsonParser
```
> يستورد الصنف `JsonParser` من `com.google.gson`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:5]

```
6: import kotlinx.coroutines.Dispatchers
```
> يستورد `Dispatchers` (الموزِّعات) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:6]

```
7: import kotlinx.coroutines.withContext
```
> يستورد الدالة `withContext` من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:8]

```
9: /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:9]

```
10:  * NIP-17 Protocol Implementation for Private Direct Messages
```
> تعليق: تنفيذ بروتوكول NIP-17 للرسائل المباشرة الخاصة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:10]

```
11:  * Compatible with iOS implementation
```
> تعليق: متوافق مع تنفيذ iOS. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:11]

```
12:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:12]

```
13: object NostrProtocol {
```
> يُعرّف كائناً مفرداً (object) باسم `NostrProtocol` (بروتوكول نوستر) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:13]

```
14:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:14]

```
15:     private const val TAG = "NostrProtocol"
```
> يُعرّف ثابتاً خاصاً (private const) باسم `TAG` (الوسم) وقيمته النصية `"NostrProtocol"`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:15]

```
16:     private val gson = Gson()
```
> يُعرّف متغيّراً خاصاً غير قابل للتغيير باسم `gson` ويضبط قيمته باستدعاء بانِئ `Gson()`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:16]

```
17:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:17]

```
18:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:18]

```
19:      * Create NIP-17 private message gift-wrap (receiver copy only per iOS)
```
> تعليق: إنشاء غلاف هدية لرسالة NIP-17 خاصة (نسخة المستلِم فقط وفق iOS). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:19]

```
20:      * Returns a single gift-wrapped event ready for relay broadcast
```
> تعليق: يُعيد حدثاً واحداً مُغلّفاً كهدية جاهزاً للبثّ عبر المُرحِّل (relay). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:20]

```
21:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:21]

```
22:     fun createPrivateMessage(
```
> يُعرّف دالة (fun) باسم `createPrivateMessage` (إنشاء رسالة خاصة) ويفتح قائمة وُسطائها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:22]

```
23:         content: String,
```
> يُعرّف وسيطاً باسم `content` (المحتوى) من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:23]

```
24:         recipientPubkey: String,
```
> يُعرّف وسيطاً باسم `recipientPubkey` (المفتاح العام للمستلِم) من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:24]

```
25:         senderIdentity: NostrIdentity
```
> يُعرّف وسيطاً باسم `senderIdentity` (هوية المُرسِل) من نوع `NostrIdentity`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:25]

```
26:     ): List<NostrEvent> {
```
> يُغلق قائمة الوُسطاء ويُعلن أنّ نوع الإرجاع `List<NostrEvent>` (قائمة من أحداث نوستر) ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:26]

```
27:         Log.d(TAG, "Creating private message for recipient: ${recipientPubkey.take(16)}...")
```
> يستدعي `Log.d` بالوسم `TAG` ونصّ يقول "إنشاء رسالة خاصة للمستلِم:" متبوعاً بأول ١٦ محرفاً من `recipientPubkey` ثم "...". [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:27]

```
28:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:28]

```
29:         // 1. Create the rumor (unsigned kind 14) with p-tag
```
> تعليق: ١. إنشاء الإشاعة (rumor) (غير مُوقّعة من النوع 14) مع وسم p. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:29]

```
30:         val rumorBase = NostrEvent(
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `rumorBase` (أساس الإشاعة) ويضبط قيمته باستدعاء بانِئ `NostrEvent(`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:30]

```
31:             pubkey = senderIdentity.publicKeyHex,
```
> يضبط الوسيط `pubkey` (المفتاح العام) على قيمة `senderIdentity.publicKeyHex`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:31]

```
32:             createdAt = (System.currentTimeMillis() / 1000).toInt(),
```
> يضبط الوسيط `createdAt` (وقت الإنشاء) على ناتج `System.currentTimeMillis()` مقسوماً على 1000 محوّلاً إلى عدد صحيح `toInt()`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:32]

```
33:             kind = NostrKind.DIRECT_MESSAGE,
```
> يضبط الوسيط `kind` (النوع) على القيمة `NostrKind.DIRECT_MESSAGE`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:33]

```
34:             tags = listOf(listOf("p", recipientPubkey)),
```
> يضبط الوسيط `tags` (الوسوم) على قائمة تحوي قائمة واحدة عناصرها `"p"` و`recipientPubkey`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:34]

```
35:             content = content
```
> يضبط الوسيط `content` على قيمة المتغيّر `content`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:35]

```
36:         )
```
> إغلاق استدعاء بانِئ `NostrEvent`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:36]

```
37:         val rumorId = rumorBase.computeEventIdHex()
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `rumorId` (معرّف الإشاعة) ويضبط قيمته باستدعاء `rumorBase.computeEventIdHex()`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:37]

```
38:         val rumor = rumorBase.copy(id = rumorId)
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `rumor` ويضبط قيمته بنسخ `rumorBase` عبر `copy` مع ضبط الوسيط `id` على `rumorId`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:38]

```
39:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:39]

```
40:         // 2. Seal the rumor (kind 13) signed by sender, timestamp randomized up to 2 days
```
> تعليق: ٢. ختم (seal) الإشاعة (النوع 13) مُوقّعة من المُرسِل، والطابع الزمني مُعشّى حتى يومين. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:40]

```
41:         val sealedEvent = createSeal(
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `sealedEvent` (الحدث المختوم) ويضبط قيمته باستدعاء `createSeal(`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:41]

```
42:             rumor = rumor,
```
> يضبط الوسيط `rumor` على قيمة المتغيّر `rumor`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:42]

```
43:             recipientPubkey = recipientPubkey,
```
> يضبط الوسيط `recipientPubkey` على قيمة المتغيّر `recipientPubkey`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:43]

```
44:             senderPrivateKey = senderIdentity.privateKeyHex,
```
> يضبط الوسيط `senderPrivateKey` (المفتاح الخاص للمُرسِل) على قيمة `senderIdentity.privateKeyHex`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:44]

```
45:             senderPublicKey = senderIdentity.publicKeyHex
```
> يضبط الوسيط `senderPublicKey` (المفتاح العام للمُرسِل) على قيمة `senderIdentity.publicKeyHex`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:45]

```
46:         )
```
> إغلاق استدعاء `createSeal`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:46]

```
47:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:47]

```
48:         // 3. Gift wrap to recipient (kind 1059)
```
> تعليق: ٣. تغليف الهدية (gift wrap) للمستلِم (النوع 1059). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:48]

```
49:         val giftWrapToRecipient = createGiftWrap(
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `giftWrapToRecipient` (غلاف الهدية إلى المستلِم) ويضبط قيمته باستدعاء `createGiftWrap(`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:49]

```
50:             seal = sealedEvent,
```
> يضبط الوسيط `seal` (الختم) على قيمة `sealedEvent`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:50]

```
51:             recipientPubkey = recipientPubkey
```
> يضبط الوسيط `recipientPubkey` على قيمة المتغيّر `recipientPubkey`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:51]

```
52:         )
```
> إغلاق استدعاء `createGiftWrap`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:52]

```
53:         Log.d(TAG, "Created gift wrap: toRecipient=${giftWrapToRecipient.id.take(16)}...")
```
> يستدعي `Log.d` بالوسم `TAG` ونصّ يقول "تمّ إنشاء غلاف الهدية: toRecipient=" متبوعاً بأول ١٦ محرفاً من `giftWrapToRecipient.id` ثم "...". [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:53]

```
54:         return listOf(giftWrapToRecipient)
```
> يُعيد قائمة تحوي العنصر `giftWrapToRecipient`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:54]

```
55:     }
```
> إغلاق نطاق (نهاية الدالة `createPrivateMessage`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:55]

```
56:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:56]

```
57:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:57]

```
58:      * Decrypt a received NIP-17 message
```
> تعليق: فكّ تعمية رسالة NIP-17 مُستلَمة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:58]

```
59:      * Returns (content, senderPubkey, timestamp) or null if decryption fails
```
> تعليق: يُعيد (المحتوى، المفتاح العام للمُرسِل، الطابع الزمني) أو null إن فشل فكّ التعمية. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:59]

```
60:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:60]

```
61:     fun decryptPrivateMessage(
```
> يُعرّف دالة باسم `decryptPrivateMessage` (فكّ تعمية رسالة خاصة) ويفتح قائمة وُسطائها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:61]

```
62:         giftWrap: NostrEvent,
```
> يُعرّف وسيطاً باسم `giftWrap` (غلاف الهدية) من نوع `NostrEvent`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:62]

```
63:         recipientIdentity: NostrIdentity
```
> يُعرّف وسيطاً باسم `recipientIdentity` (هوية المستلِم) من نوع `NostrIdentity`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:63]

```
64:     ): Triple<String, String, Int>? {
```
> يُغلق قائمة الوُسطاء ويُعلن أنّ نوع الإرجاع `Triple<String, String, Int>?` (ثلاثيّة قابلة لأن تكون null) ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:64]

```
65:         Log.v(TAG, "Starting decryption of gift wrap: ${giftWrap.id.take(16)}...")
```
> يستدعي `Log.v` بالوسم `TAG` ونصّ يقول "بدء فكّ تعمية غلاف الهدية:" متبوعاً بأول ١٦ محرفاً من `giftWrap.id` ثم "...". [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:65]

```
66:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:66]

```
67:         return try {
```
> يبدأ تعبير إرجاع `return` على كتلة `try` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:67]

```
68:             // 1. Unwrap the gift wrap
```
> تعليق: ١. فكّ غلاف الهدية. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:68]

```
69:             val seal = unwrapGiftWrap(giftWrap, recipientIdentity.privateKeyHex)
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `seal` (الختم) ويضبط قيمته باستدعاء `unwrapGiftWrap` بالوسيطين `giftWrap` و`recipientIdentity.privateKeyHex`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:69]

```
70:                 ?: run {
```
> يستعمل مُعامِل إلفيس `?:` فإن كانت النتيجة null يُشغّل كتلة `run` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:70]

```
71:                     Log.w(TAG, "❌ Failed to unwrap gift wrap")
```
> يستدعي `Log.w` بالوسم `TAG` ونصّ "❌ فشل فكّ غلاف الهدية". [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:71]

```
72:                     return null
```
> يُعيد القيمة null. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:72]

```
73:                 }
```
> إغلاق نطاق (نهاية كتلة `run`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:73]

```
74:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:74]

```
75:             Log.v(TAG, "Successfully unwrapped gift wrap from: ${seal.pubkey.take(16)}...")
```
> يستدعي `Log.v` بالوسم `TAG` ونصّ يقول "تمّ فكّ غلاف الهدية بنجاح من:" متبوعاً بأول ١٦ محرفاً من `seal.pubkey` ثم "...". [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:75]

```
76: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:76]

```
77:             if (seal.kind != NostrKind.SEAL || !seal.isValidSignature()) {
```
> يبدأ شرط `if` يتحقّق إن كان `seal.kind` لا يساوي `NostrKind.SEAL` أو كان `seal.isValidSignature()` غير صحيح، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:77]

```
78:                 Log.w(TAG, "❌ Invalid NIP-17 seal signature")
```
> يستدعي `Log.w` بالوسم `TAG` ونصّ "❌ توقيع ختم NIP-17 غير صالح". [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:78]

```
79:                 return null
```
> يُعيد القيمة null. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:79]

```
80:             }
```
> إغلاق نطاق (نهاية كتلة `if`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:80]

```
81: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:81]

```
82:             // 2. Open the seal
```
> تعليق: ٢. فتح الختم. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:82]

```
83:             val rumor = openSeal(seal, recipientIdentity.privateKeyHex)
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `rumor` ويضبط قيمته باستدعاء `openSeal` بالوسيطين `seal` و`recipientIdentity.privateKeyHex`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:83]

```
84:                 ?: run {
```
> يستعمل مُعامِل إلفيس `?:` فإن كانت النتيجة null يُشغّل كتلة `run` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:84]

```
85:                     Log.w(TAG, "❌ Failed to open seal")
```
> يستدعي `Log.w` بالوسم `TAG` ونصّ "❌ فشل فتح الختم". [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:85]

```
86:                     return null
```
> يُعيد القيمة null. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:86]

```
87:                 }
```
> إغلاق نطاق (نهاية كتلة `run`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:87]

```
88: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:88]

```
89:             if (seal.pubkey != rumor.pubkey) {
```
> يبدأ شرط `if` يتحقّق إن كان `seal.pubkey` لا يساوي `rumor.pubkey`، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:89]

```
90:                 Log.w(TAG, "❌ NIP-17 seal pubkey does not match rumor pubkey")
```
> يستدعي `Log.w` بالوسم `TAG` ونصّ "❌ المفتاح العام لختم NIP-17 لا يطابق المفتاح العام للإشاعة". [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:90]

```
91:                 return null
```
> يُعيد القيمة null. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:91]

```
92:             }
```
> إغلاق نطاق (نهاية كتلة `if`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:92]

```
93: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:93]

```
94:             Log.v(TAG, "Successfully opened seal")
```
> يستدعي `Log.v` بالوسم `TAG` ونصّ "تمّ فتح الختم بنجاح". [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:94]

```
95:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:95]

```
96:             Triple(rumor.content, rumor.pubkey, rumor.createdAt)
```
> يُنشئ ثلاثيّة `Triple` بقيم `rumor.content` و`rumor.pubkey` و`rumor.createdAt` (وهي القيمة الناتجة عن كتلة `try`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:96]

```
97:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط الاستثناء `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:97]

```
98:             Log.w(TAG, "Failed to decrypt private message: ${e.message}")
```
> يستدعي `Log.w` بالوسم `TAG` ونصّ يقول "فشل فكّ تعمية الرسالة الخاصة:" متبوعاً بـ`e.message`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:98]

```
99:             null
```
> يُنتج القيمة null كنتيجة لكتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:99]

```
100:         }
```
> إغلاق نطاق (نهاية كتلة `try/catch`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:100]

```
101:     }
```
> إغلاق نطاق (نهاية الدالة `decryptPrivateMessage`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:101]

```
102:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:102]

```
103:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:103]

```
104:      * Create a geohash-scoped text note (kind 1) with optional nickname
```
> تعليق: إنشاء ملاحظة نصية محصورة بترميز جغرافي (geohash) (النوع 1) مع اسم مستعار اختياري. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:104]

```
105:      * This creates a persistent text note that can be retrieved later
```
> تعليق: هذا يُنشئ ملاحظة نصية دائمة يمكن استرجاعها لاحقاً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:105]

```
106:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:106]

```
107:     suspend fun createGeohashTextNote(
```
> يُعرّف دالة معلّقة (suspend fun) باسم `createGeohashTextNote` (إنشاء ملاحظة نصية بترميز جغرافي) ويفتح قائمة وُسطائها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:107]

```
108:         content: String,
```
> يُعرّف وسيطاً باسم `content` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:108]

```
109:         geohash: String,
```
> يُعرّف وسيطاً باسم `geohash` (الترميز الجغرافي) من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:109]

```
110:         senderIdentity: NostrIdentity,
```
> يُعرّف وسيطاً باسم `senderIdentity` من نوع `NostrIdentity`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:110]

```
111:         nickname: String? = null
```
> يُعرّف وسيطاً باسم `nickname` (الاسم المستعار) من نوع `String?` بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:111]

```
112:     ): NostrEvent = withContext(Dispatchers.Default) {
```
> يُغلق قائمة الوُسطاء، ويُعلن أنّ نوع الإرجاع `NostrEvent`، ويسند جسم الدالة إلى استدعاء `withContext(Dispatchers.Default)` ويفتح نطاق كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:112]

```
113:         val tags = mutableListOf<List<String>>()
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `tags` ويضبط قيمته على قائمة قابلة للتغيير فارغة `mutableListOf<List<String>>()`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:113]

```
114:         tags.add(listOf("g", geohash))
```
> يستدعي `tags.add` لإضافة قائمة عناصرها `"g"` و`geohash`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:114]

```
115:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:115]

```
116:         if (!nickname.isNullOrEmpty()) {
```
> يبدأ شرط `if` يتحقّق إن كان `nickname` ليس فارغاً ولا null (نفي `isNullOrEmpty()`)، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:116]

```
117:             tags.add(listOf("n", nickname))
```
> يستدعي `tags.add` لإضافة قائمة عناصرها `"n"` و`nickname`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:117]

```
118:         }
```
> إغلاق نطاق (نهاية كتلة `if`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:118]

```
119:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:119]

```
120:         val event = NostrEvent(
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `event` (الحدث) ويضبط قيمته باستدعاء بانِئ `NostrEvent(`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:120]

```
121:             pubkey = senderIdentity.publicKeyHex,
```
> يضبط الوسيط `pubkey` على قيمة `senderIdentity.publicKeyHex`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:121]

```
122:             createdAt = (System.currentTimeMillis() / 1000).toInt(),
```
> يضبط الوسيط `createdAt` على ناتج `System.currentTimeMillis()` مقسوماً على 1000 محوّلاً إلى عدد صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:122]

```
123:             kind = NostrKind.TEXT_NOTE,
```
> يضبط الوسيط `kind` على القيمة `NostrKind.TEXT_NOTE`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:123]

```
124:             tags = tags,
```
> يضبط الوسيط `tags` على قيمة المتغيّر `tags`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:124]

```
125:             content = content
```
> يضبط الوسيط `content` على قيمة المتغيّر `content`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:125]

```
126:         )
```
> إغلاق استدعاء بانِئ `NostrEvent`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:126]

```
127:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:127]

```
128:         return@withContext senderIdentity.signEvent(event)
```
> يُعيد من كتلة `withContext` نتيجة استدعاء `senderIdentity.signEvent(event)`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:128]

```
129:     }
```
> إغلاق نطاق (نهاية كتلة `withContext` ودالة `createGeohashTextNote`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:129]

```
130: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:130]

```
131:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:131]

```
132:      * Create a geohash-scoped presence event (kind 20001)
```
> تعليق: إنشاء حدث حضور (presence) محصور بترميز جغرافي (النوع 20001). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:132]

```
133:      * Has no content and no nickname, used for participant counting
```
> تعليق: ليس له محتوى ولا اسم مستعار، يُستعمل لعدّ المشاركين. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:133]

```
134:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:134]

```
135:     suspend fun createGeohashPresenceEvent(
```
> يُعرّف دالة معلّقة باسم `createGeohashPresenceEvent` (إنشاء حدث حضور بترميز جغرافي) ويفتح قائمة وُسطائها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:135]

```
136:         geohash: String,
```
> يُعرّف وسيطاً باسم `geohash` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:136]

```
137:         senderIdentity: NostrIdentity
```
> يُعرّف وسيطاً باسم `senderIdentity` من نوع `NostrIdentity`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:137]

```
138:     ): NostrEvent = withContext(Dispatchers.Default) {
```
> يُغلق قائمة الوُسطاء، ويُعلن نوع الإرجاع `NostrEvent`، ويسند جسم الدالة إلى `withContext(Dispatchers.Default)` ويفتح نطاق كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:138]

```
139:         val tags = mutableListOf<List<String>>()
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `tags` ويضبط قيمته على قائمة قابلة للتغيير فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:139]

```
140:         tags.add(listOf("g", geohash))
```
> يستدعي `tags.add` لإضافة قائمة عناصرها `"g"` و`geohash`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:140]

```
141: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:141]

```
142:         val event = NostrEvent(
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `event` ويضبط قيمته باستدعاء بانِئ `NostrEvent(`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:142]

```
143:             pubkey = senderIdentity.publicKeyHex,
```
> يضبط الوسيط `pubkey` على قيمة `senderIdentity.publicKeyHex`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:143]

```
144:             createdAt = (System.currentTimeMillis() / 1000).toInt(),
```
> يضبط الوسيط `createdAt` على ناتج `System.currentTimeMillis()` مقسوماً على 1000 محوّلاً إلى عدد صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:144]

```
145:             kind = NostrKind.GEOHASH_PRESENCE,
```
> يضبط الوسيط `kind` على القيمة `NostrKind.GEOHASH_PRESENCE`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:145]

```
146:             tags = tags,
```
> يضبط الوسيط `tags` على قيمة المتغيّر `tags`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:146]

```
147:             content = ""
```
> يضبط الوسيط `content` على سلسلة نصية فارغة `""`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:147]

```
148:         )
```
> إغلاق استدعاء بانِئ `NostrEvent`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:148]

```
149: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:149]

```
150:         return@withContext senderIdentity.signEvent(event)
```
> يُعيد من كتلة `withContext` نتيجة استدعاء `senderIdentity.signEvent(event)`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:150]

```
151:     }
```
> إغلاق نطاق (نهاية كتلة `withContext` ودالة `createGeohashPresenceEvent`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:151]

```
152:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:152]

```
153:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:153]

```
154:      * Create a geohash-scoped ephemeral public message (kind 20000)
```
> تعليق: إنشاء رسالة عامة عابرة (ephemeral) محصورة بترميز جغرافي (النوع 20000). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:154]

```
155:      * Includes Proof of Work mining if enabled in settings
```
> تعليق: يتضمّن تعدين إثبات العمل (Proof of Work) إن كان مُفعّلاً في الإعدادات. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:155]

```
156:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:156]

```
157:     suspend fun createEphemeralGeohashEvent(
```
> يُعرّف دالة معلّقة باسم `createEphemeralGeohashEvent` (إنشاء حدث جغرافي عابر) ويفتح قائمة وُسطائها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:157]

```
158:         content: String,
```
> يُعرّف وسيطاً باسم `content` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:158]

```
159:         geohash: String,
```
> يُعرّف وسيطاً باسم `geohash` من نوع `String`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:159]

```
160:         senderIdentity: NostrIdentity,
```
> يُعرّف وسيطاً باسم `senderIdentity` من نوع `NostrIdentity`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:160]

```
161:         nickname: String? = null,
```
> يُعرّف وسيطاً باسم `nickname` من نوع `String?` بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:161]

```
162:         teleported: Boolean = false
```
> يُعرّف وسيطاً باسم `teleported` (مُنتقَل آنياً) من نوع `Boolean` بقيمة افتراضية false. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:162]

```
163:     ): NostrEvent = withContext(Dispatchers.Default) {
```
> يُغلق قائمة الوُسطاء، ويُعلن نوع الإرجاع `NostrEvent`، ويسند جسم الدالة إلى `withContext(Dispatchers.Default)` ويفتح نطاق كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:163]

```
164:         val tags = mutableListOf<List<String>>()
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `tags` ويضبط قيمته على قائمة قابلة للتغيير فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:164]

```
165:         tags.add(listOf("g", geohash))
```
> يستدعي `tags.add` لإضافة قائمة عناصرها `"g"` و`geohash`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:165]

```
166:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:166]

```
167:         if (!nickname.isNullOrEmpty()) {
```
> يبدأ شرط `if` يتحقّق إن كان `nickname` ليس فارغاً ولا null، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:167]

```
168:             tags.add(listOf("n", nickname))
```
> يستدعي `tags.add` لإضافة قائمة عناصرها `"n"` و`nickname`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:168]

```
169:         }
```
> إغلاق نطاق (نهاية كتلة `if`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:169]

```
170:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:170]

```
171:         if (teleported) {
```
> يبدأ شرط `if` يتحقّق إن كان `teleported` صحيحاً، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:171]

```
172:             // Use tag consistent with event handlers ("t","teleport")
```
> تعليق: استعمال وسم متّسق مع معالِجات الأحداث ("t","teleport"). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:172]

```
173:             tags.add(listOf("t", "teleport"))
```
> يستدعي `tags.add` لإضافة قائمة عناصرها `"t"` و`"teleport"`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:173]

```
174:         }
```
> إغلاق نطاق (نهاية كتلة `if`). [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:174]

```
175:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:175]

```
176:         var event = NostrEvent(
```
> يُعرّف متغيّراً قابلاً للتغيير (var) باسم `event` ويضبط قيمته باستدعاء بانِئ `NostrEvent(`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:176]

```
177:             pubkey = senderIdentity.publicKeyHex,
```
> يضبط الوسيط `pubkey` على قيمة `senderIdentity.publicKeyHex`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:177]

```
178:             createdAt = (System.currentTimeMillis() / 1000).toInt(),
```
> يضبط الوسيط `createdAt` على ناتج `System.currentTimeMillis()` مقسوماً على 1000 محوّلاً إلى عدد صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:178]

```
179:             kind = NostrKind.EPHEMERAL_EVENT,
```
> يضبط الوسيط `kind` على القيمة `NostrKind.EPHEMERAL_EVENT`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:179]

```
180:             tags = tags,
```
> يضبط الوسيط `tags` على قيمة المتغيّر `tags`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:180]

```
181:             content = content
```
> يضبط الوسيط `content` على قيمة المتغيّر `content`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:181]

```
182:         )
```
> إغلاق استدعاء بانِئ `NostrEvent`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:182]

```
183:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:183]

```
184:         // Check if Proof of Work is enabled
```
> تعليق: التحقّق إن كان إثبات العمل مُفعّلاً. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:184]

```
185:         val powSettings = PoWPreferenceManager.getCurrentSettings()
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `powSettings` (إعدادات إثبات العمل) ويضبط قيمته باستدعاء `PoWPreferenceManager.getCurrentSettings()`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:185]

```
186:         if (powSettings.enabled && powSettings.difficulty > 0) {
```
> يبدأ شرط `if` يتحقّق إن كان `powSettings.enabled` صحيحاً و`powSettings.difficulty` أكبر من 0، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:186]

```
187:             Log.d(TAG, "PoW enabled for geohash event: difficulty=${powSettings.difficulty}")
```
> يستدعي `Log.d` بالوسم `TAG` ونصّ يقول "إثبات العمل مُفعّل لحدث جغرافي: difficulty=" متبوعاً بـ`powSettings.difficulty`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:187]

```
188:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:188]

```
189:             try {
```
> يفتح كتلة `try` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:189]

```
190:                 // Start mining state for animated indicators
```
> تعليق: بدء حالة التعدين للمؤشّرات المتحرّكة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:190]

```
191:                 PoWPreferenceManager.startMining()
```
> يستدعي `PoWPreferenceManager.startMining()`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:191]

```
192:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:192]

```
193:                 // Mine the event before signing
```
> تعليق: تعدين الحدث قبل التوقيع. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:193]

```
194:                 val minedEvent = NostrProofOfWork.mineEvent(
```
> يُعرّف متغيّراً غير قابل للتغيير باسم `minedEvent` (الحدث المُعدَّن) ويضبط قيمته باستدعاء `NostrProofOfWork.mineEvent(`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:194]

```
195:                     event = event,
```
> يضبط الوسيط `event` على قيمة المتغيّر `event`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:195]

```
196:                     targetDifficulty = powSettings.difficulty,
```
> يضبط الوسيط `targetDifficulty` (الصعوبة المستهدَفة) على قيمة `powSettings.difficulty`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:196]

```
197:                     maxIterations = 2_000_000 // Allow up to 2M iterations for reasonable mining time
```
> يضبط الوسيط `maxIterations` (أقصى عدد تكرارات) على القيمة `2_000_000`؛ تعليق: السماح بحتى مليونَي تكرار لزمن تعدين معقول. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:197]

```
198:                 )
```
> إغلاق استدعاء `NostrProofOfWork.mineEvent`. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:198]

```
199:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:199]

```
200:                 if (minedEvent != null) {
```
> يبدأ شرط `if` يتحقّق إن كان `minedEvent` لا يساوي null، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrProtocol.kt:200]
