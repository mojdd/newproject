# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يُعلن أنّ هذا الملف ينتمي إلى الحزمة (package) المسماة com.bitchat.android.nostr. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف Context من android.content. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف Log من android.util. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:4]

```
5: import com.bitchat.android.identity.SecureIdentityStateManager
```
> يستورد الصنف SecureIdentityStateManager من com.bitchat.android.identity. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:5]

```
6: import java.security.MessageDigest
```
> يستورد الصنف MessageDigest من java.security. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:6]

```
7: import java.security.SecureRandom
```
> يستورد الصنف SecureRandom من java.security. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:8]

```
9: /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:9]

```
10:  * Manages Nostr identity (secp256k1 keypair) for NIP-17 private messaging
```
> تعليق: يدير هوية Nostr (زوج مفاتيح secp256k1) للرسائل الخاصة وفق NIP-17. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:10]

```
11:  * Compatible with iOS implementation
```
> تعليق: متوافق مع تطبيق iOS. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:11]

```
12:  */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:12]

```
13: data class NostrIdentity(
```
> يُعرّف صنف بيانات (data class) باسم NostrIdentity (هوية نوستر) ويبدأ قائمة معاملاته. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:13]

```
14:     val privateKeyHex: String,
```
> يُعرّف خاصية ثابتة privateKeyHex (المفتاح الخاص الست عشري) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:14]

```
15:     val publicKeyHex: String,
```
> يُعرّف خاصية ثابتة publicKeyHex (المفتاح العام الست عشري) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:15]

```
16:     val npub: String,
```
> يُعرّف خاصية ثابتة npub (المعرّف العام) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:16]

```
17:     val createdAt: Long
```
> يُعرّف خاصية ثابتة createdAt (وقت الإنشاء) من نوع Long. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:17]

```
18: ) {
```
> يُغلق قائمة معاملات صنف البيانات ويفتح جسمه. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:18]

```
19:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:19]

```
20:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:20]

```
21:         private const val TAG = "NostrIdentity"
```
> يُعرّف ثابتاً خاصاً TAG (وسم السجل) ويضبط قيمته على النص "NostrIdentity". [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:21]

```
22:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:22]

```
23:         /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:23]

```
24:          * Generate a new Nostr identity
```
> تعليق: ولّد هوية Nostr جديدة. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:24]

```
25:          */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:25]

```
26:         fun generate(): NostrIdentity {
```
> يُعرّف دالة generate (توليد) التي تُعيد كائن NostrIdentity ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:26]

```
27:             val (privateKeyHex, publicKeyHex) = NostrCrypto.generateKeyPair()
```
> يستدعي NostrCrypto.generateKeyPair() ويفكّك ناتجه إلى المتغيرين privateKeyHex و publicKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:27]

```
28:             val npub = Bech32.encode("npub", publicKeyHex.hexToByteArrayLocal())
```
> يضبط npub بناتج استدعاء Bech32.encode بالوسيط "npub" وبتحويل publicKeyHex إلى مصفوفة بايتات عبر hexToByteArrayLocal(). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:28]

```
29:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:29]

```
30:             Log.d(TAG, "Generated new Nostr identity: npub=$npub")
```
> يستدعي Log.d بالوسم TAG ونص "Generated new Nostr identity: npub=" متبوعاً بقيمة npub. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:30]

```
31:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:31]

```
32:             return NostrIdentity(
```
> يبدأ إعادة كائن NostrIdentity جديد ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:32]

```
33:                 privateKeyHex = privateKeyHex,
```
> يضبط الوسيط privateKeyHex على قيمة المتغير privateKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:33]

```
34:                 publicKeyHex = publicKeyHex,
```
> يضبط الوسيط publicKeyHex على قيمة المتغير publicKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:34]

```
35:                 npub = npub,
```
> يضبط الوسيط npub على قيمة المتغير npub. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:35]

```
36:                 createdAt = System.currentTimeMillis()
```
> يضبط الوسيط createdAt على ناتج System.currentTimeMillis(). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:36]

```
37:             )
```
> يُغلق قائمة وسائط الكائن المُعاد. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:37]

```
38:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:38]

```
39:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:39]

```
40:         /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:40]

```
41:          * Create from existing private key
```
> تعليق: أنشئ من مفتاح خاص موجود. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:41]

```
42:          */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:42]

```
43:         fun fromPrivateKey(privateKeyHex: String): NostrIdentity {
```
> يُعرّف دالة fromPrivateKey (من المفتاح الخاص) تأخذ privateKeyHex من نوع String وتُعيد NostrIdentity ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:43]

```
44:             require(NostrCrypto.isValidPrivateKey(privateKeyHex)) { 
```
> يستدعي require للتحقق من شرط NostrCrypto.isValidPrivateKey(privateKeyHex) ويفتح كتلة رسالة الخطأ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:44]

```
45:                 "Invalid private key" 
```
> يحدّد نص رسالة الخطأ "Invalid private key". [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:45]

```
46:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:46]

```
47:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:47]

```
48:             val publicKeyHex = NostrCrypto.derivePublicKey(privateKeyHex)
```
> يضبط publicKeyHex بناتج استدعاء NostrCrypto.derivePublicKey(privateKeyHex). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:48]

```
49:             val npub = Bech32.encode("npub", publicKeyHex.hexToByteArrayLocal())
```
> يضبط npub بناتج Bech32.encode بالوسيط "npub" وبتحويل publicKeyHex إلى مصفوفة بايتات عبر hexToByteArrayLocal(). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:49]

```
50:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:50]

```
51:             return NostrIdentity(
```
> يبدأ إعادة كائن NostrIdentity جديد ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:51]

```
52:                 privateKeyHex = privateKeyHex,
```
> يضبط الوسيط privateKeyHex على قيمة المعامل privateKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:52]

```
53:                 publicKeyHex = publicKeyHex,
```
> يضبط الوسيط publicKeyHex على قيمة المتغير publicKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:53]

```
54:                 npub = npub,
```
> يضبط الوسيط npub على قيمة المتغير npub. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:54]

```
55:                 createdAt = System.currentTimeMillis()
```
> يضبط الوسيط createdAt على ناتج System.currentTimeMillis(). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:55]

```
56:             )
```
> يُغلق قائمة وسائط الكائن المُعاد. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:56]

```
57:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:57]

```
58:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:58]

```
59:         /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:59]

```
60:          * Create from a deterministic seed (for demo purposes)
```
> تعليق: أنشئ من بذرة حتمية (لأغراض العرض التوضيحي). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:60]

```
61:          */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:61]

```
62:         fun fromSeed(seed: String): NostrIdentity {
```
> يُعرّف دالة fromSeed (من البذرة) تأخذ seed من نوع String وتُعيد NostrIdentity ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:62]

```
63:             // Hash the seed to create a private key
```
> تعليق: جزّئ البذرة لإنشاء مفتاح خاص. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:63]

```
64:             val digest = MessageDigest.getInstance("SHA-256")
```
> يضبط digest بكائن MessageDigest الناتج عن getInstance بالوسيط "SHA-256". [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:64]

```
65:             val seedBytes = seed.toByteArray(Charsets.UTF_8)
```
> يضبط seedBytes بتحويل seed إلى مصفوفة بايتات بترميز Charsets.UTF_8. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:65]

```
66:             val privateKeyBytes = digest.digest(seedBytes)
```
> يضبط privateKeyBytes بناتج digest.digest(seedBytes). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:66]

```
67:             val privateKeyHex = privateKeyBytes.joinToString("") { "%02x".format(it) }
```
> يضبط privateKeyHex بدمج privateKeyBytes في نص بفاصل فارغ، مع تنسيق كل بايت بالصيغة "%02x". [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:67]

```
68:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:68]

```
69:             return fromPrivateKey(privateKeyHex)
```
> يُعيد ناتج استدعاء fromPrivateKey(privateKeyHex). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:69]

```
70:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:70]

```
71:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:71]

```
72:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:72]

```
73:     /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:73]

```
74:      * Sign a Nostr event
```
> تعليق: وقّع حدث Nostr. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:74]

```
75:      */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:75]

```
76:     fun signEvent(event: NostrEvent): NostrEvent {
```
> يُعرّف دالة signEvent (توقيع الحدث) تأخذ event من نوع NostrEvent وتُعيد NostrEvent ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:76]

```
77:         return event.sign(privateKeyHex)
```
> يُعيد ناتج استدعاء event.sign(privateKeyHex). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:77]

```
78:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:78]

```
79:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:79]

```
80:     /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:80]

```
81:      * Get short display format
```
> تعليق: احصل على صيغة عرض قصيرة. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:81]

```
82:      */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:82]

```
83:     fun getShortNpub(): String {
```
> يُعرّف دالة getShortNpub (المعرّف العام المختصر) التي تُعيد String ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:83]

```
84:         return if (npub.length > 16) {
```
> يبدأ إعادة قيمة شرطية تتحقق إن كان طول npub أكبر من 16 ويفتح فرع الصواب. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:84]

```
85:             "${npub.take(8)}...${npub.takeLast(8)}"
```
> يبني نصاً يجمع أول 8 محارف من npub عبر take(8) ثم "..." ثم آخر 8 محارف عبر takeLast(8). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:85]

```
86:         } else {
```
> يُغلق فرع الصواب ويفتح فرع else. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:86]

```
87:             npub
```
> يُعيد قيمة npub كما هي في فرع else. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:87]

```
88:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:88]

```
89:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:89]

```
90: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:90]

```
91: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:91]

```
92: /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:92]

```
93:  * Bridge between Noise and Nostr identities
```
> تعليق: جسر بين هويتَي Noise و Nostr. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:93]

```
94:  * Manages persistent storage and per-geohash identity derivation
```
> تعليق: يدير التخزين الدائم واشتقاق الهوية لكل geohash. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:94]

```
95:  */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:95]

```
96: object NostrIdentityBridge {
```
> يُعرّف كائناً مفرداً (object) باسم NostrIdentityBridge (جسر هوية نوستر) ويفتح جسمه. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:96]

```
97:     private const val TAG = "NostrIdentityBridge"
```
> يُعرّف ثابتاً خاصاً TAG (وسم السجل) ويضبط قيمته على النص "NostrIdentityBridge". [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:97]

```
98:     private const val NOSTR_PRIVATE_KEY = "nostr_private_key"
```
> يُعرّف ثابتاً خاصاً NOSTR_PRIVATE_KEY (مفتاح نوستر الخاص) ويضبط قيمته على النص "nostr_private_key". [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:98]

```
99:     private const val DEVICE_SEED_KEY = "nostr_device_seed"
```
> يُعرّف ثابتاً خاصاً DEVICE_SEED_KEY (مفتاح بذرة الجهاز) ويضبط قيمته على النص "nostr_device_seed". [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:99]

```
100:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:100]

```
101:     // Cache for derived geohash identities to avoid repeated crypto operations
```
> تعليق: ذاكرة مؤقتة لهويات geohash المشتقّة لتجنّب تكرار عمليات التعمية. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:101]

```
102:     private val geohashIdentityCache = mutableMapOf<String, NostrIdentity>()
```
> يُعرّف خاصية خاصة ثابتة geohashIdentityCache (ذاكرة هويات geohash) ويضبطها بخريطة قابلة للتعديل من مفتاح String إلى قيمة NostrIdentity عبر mutableMapOf. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:102]

```
103:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:103]

```
104:     /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:104]

```
105:      * Get or create the current Nostr identity
```
> تعليق: احصل على هوية Nostr الحالية أو أنشئها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:105]

```
106:      */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:106]

```
107:     fun getCurrentNostrIdentity(context: Context): NostrIdentity? {
```
> يُعرّف دالة getCurrentNostrIdentity (الهوية الحالية) تأخذ context من نوع Context وتُعيد NostrIdentity أو null ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:107]

```
108:         val stateManager = SecureIdentityStateManager(context)
```
> يضبط stateManager بكائن SecureIdentityStateManager مُنشأ بالوسيط context. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:108]

```
109:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:109]

```
110:         // Try to load existing Nostr private key
```
> تعليق: حاول تحميل مفتاح Nostr الخاص الموجود. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:110]

```
111:         val existingKey = loadNostrPrivateKey(stateManager)
```
> يضبط existingKey بناتج استدعاء loadNostrPrivateKey(stateManager). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:111]

```
112:         if (existingKey != null) {
```
> يبدأ شرط if يتحقق إن كان existingKey لا يساوي null ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:112]

```
113:             return try {
```
> يبدأ إعادة ناتج كتلة try ويفتحها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:113]

```
114:                 NostrIdentity.fromPrivateKey(existingKey)
```
> يستدعي NostrIdentity.fromPrivateKey(existingKey) كقيمة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:114]

```
115:             } catch (e: Exception) {
```
> يُغلق كتلة try ويفتح كتلة catch تلتقط استثناء e من نوع Exception. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:115]

```
116:                 Log.e(TAG, "Failed to create identity from stored key: ${e.message}")
```
> يستدعي Log.e بالوسم TAG ونص "Failed to create identity from stored key: " متبوعاً بقيمة e.message. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:116]

```
117:                 null
```
> يُعيد القيمة null كقيمة كتلة catch. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:117]

```
118:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:118]

```
119:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:119]

```
120:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:120]

```
121:         // Generate new identity
```
> تعليق: ولّد هوية جديدة. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:121]

```
122:         val newIdentity = NostrIdentity.generate()
```
> يضبط newIdentity بناتج استدعاء NostrIdentity.generate(). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:122]

```
123:         saveNostrPrivateKey(stateManager, newIdentity.privateKeyHex)
```
> يستدعي saveNostrPrivateKey بالوسيطين stateManager و newIdentity.privateKeyHex. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:123]

```
124:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:124]

```
125:         Log.i(TAG, "Created new Nostr identity: ${newIdentity.getShortNpub()}")
```
> يستدعي Log.i بالوسم TAG ونص "Created new Nostr identity: " متبوعاً بناتج newIdentity.getShortNpub(). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:125]

```
126:         return newIdentity
```
> يُعيد قيمة newIdentity. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:126]

```
127:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:127]

```
128:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:128]

```
129:     /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:129]

```
130:      * Derive a deterministic, unlinkable Nostr identity for a given geohash
```
> تعليق: اشتق هوية Nostr حتمية وغير قابلة للربط لـ geohash معيّن. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:130]

```
131:      * Uses HMAC-SHA256(deviceSeed, geohash) as private key material with fallback rehashing
```
> تعليق: يستخدم HMAC-SHA256(deviceSeed, geohash) كمادة مفتاح خاص مع إعادة تجزئة احتياطية. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:131]

```
132:      * if the candidate is not a valid secp256k1 private key.
```
> تعليق: إذا لم يكن المرشّح مفتاحاً خاصاً صالحاً وفق secp256k1. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:132]

```
133:      * 
```
> تعليق: سطر تعليق فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:133]

```
134:      * Direct port from iOS implementation for 100% compatibility
```
> تعليق: نقل مباشر من تطبيق iOS لتوافق بنسبة 100%. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:134]

```
135:      * OPTIMIZED: Cached for UI responsiveness
```
> تعليق: مُحسَّن: مخزَّن مؤقتاً من أجل استجابة واجهة المستخدم. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:135]

```
136:      */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:136]

```
137:     fun deriveIdentity(forGeohash: String, context: Context): NostrIdentity {
```
> يُعرّف دالة deriveIdentity (اشتقاق الهوية) تأخذ forGeohash من نوع String و context من نوع Context وتُعيد NostrIdentity ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:137]

```
138:         // Check cache first for immediate response
```
> تعليق: تحقق من الذاكرة المؤقتة أولاً لاستجابة فورية. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:138]

```
139:         geohashIdentityCache[forGeohash]?.let { cachedIdentity ->
```
> يصل إلى geohashIdentityCache بالمفتاح forGeohash، وإن لم يكن null ينفّذ let مع تسمية القيمة cachedIdentity. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:139]

```
140:             //Log.v(TAG, "Using cached geohash identity for $forGeohash")
```
> تعليق: //Log.v(TAG, "Using cached geohash identity for $forGeohash") سطر مُعطّل بالتعليق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:140]

```
141:             return cachedIdentity
```
> يُعيد قيمة cachedIdentity من داخل كتلة let. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:141]

```
142:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:142]

```
143:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:143]

```
144:         val stateManager = SecureIdentityStateManager(context)
```
> يضبط stateManager بكائن SecureIdentityStateManager مُنشأ بالوسيط context. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:144]

```
145:         val seed = getOrCreateDeviceSeed(stateManager)
```
> يضبط seed بناتج استدعاء getOrCreateDeviceSeed(stateManager). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:145]

```
146:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:146]

```
147:         val geohashBytes = forGeohash.toByteArray(Charsets.UTF_8)
```
> يضبط geohashBytes بتحويل forGeohash إلى مصفوفة بايتات بترميز Charsets.UTF_8. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:147]

```
148:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:148]

```
149:         // Try a few iterations to ensure a valid key can be formed (exactly like iOS)
```
> تعليق: جرّب بضع تكرارات لضمان تكوين مفتاح صالح (تماماً مثل iOS). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:149]

```
150:         for (i in 0 until 10) {
```
> يبدأ حلقة for بالمتغير i من 0 حتى 10 غير شاملة ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:150]

```
151:             val candidateKey = candidateKey(seed, geohashBytes, i.toUInt())
```
> يضبط candidateKey بناتج استدعاء الدالة candidateKey بالوسائط seed و geohashBytes و i محوّلاً إلى UInt عبر toUInt(). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:151]

```
152:             val candidateKeyHex = candidateKey.toHexStringLocal()
```
> يضبط candidateKeyHex بناتج candidateKey.toHexStringLocal(). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:152]

```
153:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:153]

```
154:             if (NostrCrypto.isValidPrivateKey(candidateKeyHex)) {
```
> يبدأ شرط if يتحقق من NostrCrypto.isValidPrivateKey(candidateKeyHex) ويفتح كتلته. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:154]

```
155:                 val identity = NostrIdentity.fromPrivateKey(candidateKeyHex)
```
> يضبط identity بناتج استدعاء NostrIdentity.fromPrivateKey(candidateKeyHex). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:155]

```
156:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:156]

```
157:                 // Cache the result for future UI responsiveness
```
> تعليق: خزّن النتيجة مؤقتاً لاستجابة واجهة المستخدم مستقبلاً. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:157]

```
158:                 geohashIdentityCache[forGeohash] = identity
```
> يُسند identity إلى geohashIdentityCache عند المفتاح forGeohash. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:158]

```
159:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:159]

```
160:                 Log.d(TAG, "Derived geohash identity for $forGeohash (iteration $i)")
```
> يستدعي Log.d بالوسم TAG ونص "Derived geohash identity for " متبوعاً بقيمة forGeohash ثم " (iteration " وقيمة i. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:160]

```
161:                 return identity
```
> يُعيد قيمة identity. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:161]

```
162:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:162]

```
163:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:163]

```
164:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:164]

```
165:         // As a final fallback, hash the seed+msg and try again (exactly like iOS)
```
> تعليق: كبديل أخير، جزّئ seed+msg وحاول مجدداً (تماماً مثل iOS). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:165]

```
166:         val combined = seed + geohashBytes
```
> يضبط combined بنتيجة دمج seed و geohashBytes عبر العامل +. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:166]

```
167:         val digest = MessageDigest.getInstance("SHA-256")
```
> يضبط digest بكائن MessageDigest الناتج عن getInstance بالوسيط "SHA-256". [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:167]

```
168:         val fallbackKey = digest.digest(combined)
```
> يضبط fallbackKey بناتج digest.digest(combined). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:168]

```
169:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:169]

```
170:         val fallbackIdentity = NostrIdentity.fromPrivateKey(fallbackKey.toHexStringLocal())
```
> يضبط fallbackIdentity بناتج NostrIdentity.fromPrivateKey مع تحويل fallbackKey إلى نص ست عشري عبر toHexStringLocal(). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:170]

```
171:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:171]

```
172:         // Cache the fallback result too
```
> تعليق: خزّن النتيجة الاحتياطية مؤقتاً أيضاً. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:172]

```
173:         geohashIdentityCache[forGeohash] = fallbackIdentity
```
> يُسند fallbackIdentity إلى geohashIdentityCache عند المفتاح forGeohash. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:173]

```
174:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:174]

```
175:         Log.d(TAG, "Used fallback identity derivation for $forGeohash")
```
> يستدعي Log.d بالوسم TAG ونص "Used fallback identity derivation for " متبوعاً بقيمة forGeohash. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:175]

```
176:         return fallbackIdentity
```
> يُعيد قيمة fallbackIdentity. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:176]

```
177:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:177]

```
178:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:178]

```
179:     /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:179]

```
180:      * Generate candidate key for a specific iteration (matches iOS implementation)
```
> تعليق: ولّد مفتاحاً مرشّحاً لتكرار معيّن (يطابق تطبيق iOS). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:180]

```
181:      */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:181]

```
182:     private fun candidateKey(seed: ByteArray, message: ByteArray, iteration: UInt): ByteArray {
```
> يُعرّف دالة خاصة candidateKey (المفتاح المرشّح) تأخذ seed و message من نوع ByteArray و iteration من نوع UInt وتُعيد ByteArray ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:182]

```
183:         val input = message + iteration.toLittleEndianBytes()
```
> يضبط input بدمج message مع ناتج iteration.toLittleEndianBytes() عبر العامل +. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:183]

```
184:         return hmacSha256(seed, input)
```
> يُعيد ناتج استدعاء hmacSha256(seed, input). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:184]

```
185:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:185]

```
186:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:186]

```
187:     /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:187]

```
188:      * Associate a Nostr identity with a Noise public key (for favorites)
```
> تعليق: اربط هوية Nostr بمفتاح Noise العام (للمفضّلة). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:188]

```
189:      */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:189]

```
190:     fun associateNostrIdentity(nostrPubkey: String, noisePublicKey: ByteArray, context: Context) {
```
> يُعرّف دالة associateNostrIdentity (ربط هوية نوستر) تأخذ nostrPubkey من نوع String و noisePublicKey من نوع ByteArray و context من نوع Context ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:190]

```
191:         val stateManager = SecureIdentityStateManager(context)
```
> يضبط stateManager بكائن SecureIdentityStateManager مُنشأ بالوسيط context. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:191]

```
192:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:192]

```
193:         // We'll use the existing signing key storage mechanism for associations
```
> تعليق: سنستخدم آلية تخزين مفتاح التوقيع الموجودة من أجل الروابط. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:193]

```
194:         // For now, we'll store this as a preference since it's just for favorites mapping
```
> تعليق: حالياً، سنخزّن هذا كتفضيل لأنه مجرّد ربط للمفضّلة. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:194]

```
195:         // In a full implementation, you'd want a proper association storage system
```
> تعليق: في تطبيق كامل، ستحتاج إلى نظام تخزين روابط مناسب. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:195]

```
196:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:196]

```
197:         Log.d(TAG, "Associated Nostr pubkey ${nostrPubkey.take(16)}... with Noise key")
```
> يستدعي Log.d بالوسم TAG ونص "Associated Nostr pubkey " متبوعاً بأول 16 محرفاً من nostrPubkey عبر take(16) ثم "... with Noise key". [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:197]

```
198:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:198]

```
199:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:199]

```
200:     /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/nostr/NostrIdentity.kt:200]
