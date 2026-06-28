# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt (الأسطر 1–250)

```
1: package com.bitchat.android.noise
```
> يُعلِن أنّ هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.noise`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من حزمة أندرويد `android.content`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` من حزمة أندرويد `android.util` لتسجيل الرسائل. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:4]

```
5: import com.bitchat.android.identity.SecureIdentityStateManager
```
> يستورد الصنف `SecureIdentityStateManager` (مدير حالة الهوية الآمن) من حزمة `com.bitchat.android.identity`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:5]

```
6: import com.bitchat.android.mesh.PeerFingerprintManager
```
> يستورد الصنف `PeerFingerprintManager` (مدير بصمات الأقران) من حزمة `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:6]

```
7: import com.bitchat.android.noise.southernstorm.protocol.Noise
```
> يستورد الصنف `Noise` (نويز) من حزمة `com.bitchat.android.noise.southernstorm.protocol`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:7]

```
8: import java.security.MessageDigest
```
> يستورد الصنف `MessageDigest` (هاضم الرسالة) من حزمة `java.security` لحساب التجزئة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:8]

```
9: import java.security.SecureRandom
```
> يستورد الصنف `SecureRandom` (المولّد العشوائي الآمن) من حزمة `java.security`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:9]

```
10: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف `ConcurrentHashMap` (خريطة التجزئة المتزامنة) من حزمة `java.util.concurrent`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:11]

```
12: /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيق (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:12]

```
13:  * Main Noise encryption service - 100% compatible with iOS implementation
```
> تعليق: خدمة تشفير نويز الرئيسية - متوافقة ١٠٠٪ مع تطبيق iOS. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:13]

```
14:  * 
```
> تعليق: سطر فارغ داخل كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:14]

```
15:  * This service manages:
```
> تعليق: هذه الخدمة تدير ما يلي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:15]

```
16:  * - Static identity keys (persistent across sessions)
```
> تعليق: مفاتيح الهوية الثابتة (دائمة عبر الجلسات). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:16]

```
17:  * - Noise session management for each peer
```
> تعليق: إدارة جلسات نويز لكل قرين. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:17]

```
18:  * - Channel encryption using password-derived keys
```
> تعليق: تشفير القنوات باستعمال مفاتيح مشتقّة من كلمة المرور. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:18]

```
19:  * - Peer fingerprint mapping and identity persistence
```
> تعليق: ربط بصمات الأقران وإدامة الهوية. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:19]

```
20:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:20]

```
21: class NoiseEncryptionService(private val context: Context) {
```
> يُعرِّف الصنف `NoiseEncryptionService` (خدمة تشفير نويز) ببانٍ يستقبل مُعاملاً خاصاً ثابتاً `context` من نوع `Context` ويفتح نطاق الصنف. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:21]

```
22:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:22]

```
23:     companion object {
```
> يفتح كائناً رفيقاً (companion object) لحمل الأعضاء الساكنة للصنف. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:23]

```
24:         private const val TAG = "NoiseEncryptionService"
```
> يُعرِّف ثابتاً خاصاً `TAG` (الوسم) من نوع نصّي بالقيمة الحرفية `"NoiseEncryptionService"` يُستعمَل وسماً للتسجيل. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:24]

```
25:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:25]

```
26:         // Session limits for performance and security
```
> تعليق: حدود الجلسة للأداء والأمان. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:26]

```
27:         private const val REKEY_TIME_LIMIT = com.bitchat.android.util.AppConstants.Noise.REKEY_TIME_LIMIT_MS // 1 hour (same as iOS)
```
> يُعرِّف ثابتاً خاصاً `REKEY_TIME_LIMIT` (حدّ زمن إعادة التمفيت) قيمته `AppConstants.Noise.REKEY_TIME_LIMIT_MS`، مع تعليق: ساعة واحدة (مثل iOS). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:27]

```
28:         private const val REKEY_MESSAGE_LIMIT = com.bitchat.android.util.AppConstants.Noise.REKEY_MESSAGE_LIMIT_ENCRYPTION // 1k messages (matches iOS) (same as iOS)
```
> يُعرِّف ثابتاً خاصاً `REKEY_MESSAGE_LIMIT` (حدّ رسائل إعادة التمفيت) قيمته `AppConstants.Noise.REKEY_MESSAGE_LIMIT_ENCRYPTION`، مع تعليق: ألف رسالة (يطابق iOS) (مثل iOS). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:28]

```
29:     }
```
> إغلاق نطاق الكائن الرفيق (companion object). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:29]

```
30:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:30]

```
31:     // Static identity key (persistent across app restarts) - loaded from secure storage
```
> تعليق: مفتاح الهوية الثابت (دائم عبر إعادة تشغيل التطبيق) - محمّل من التخزين الآمن. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:31]

```
32:     private var staticIdentityPrivateKey: ByteArray
```
> يُعلِن متغيّراً خاصاً قابلاً للتغيير `staticIdentityPrivateKey` (المفتاح الخاص للهوية الثابتة) من نوع `ByteArray` (مصفوفة بايتات). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:32]

```
33:     private var staticIdentityPublicKey: ByteArray
```
> يُعلِن متغيّراً خاصاً قابلاً للتغيير `staticIdentityPublicKey` (المفتاح العام للهوية الثابتة) من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:33]

```
34:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:34]

```
35:     // Ed25519 signing key (persistent across app restarts) - loaded from secure storage
```
> تعليق: مفتاح التوقيع Ed25519 (دائم عبر إعادة تشغيل التطبيق) - محمّل من التخزين الآمن. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:35]

```
36:     private var signingPrivateKey: ByteArray
```
> يُعلِن متغيّراً خاصاً قابلاً للتغيير `signingPrivateKey` (مفتاح التوقيع الخاص) من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:36]

```
37:     private var signingPublicKey: ByteArray
```
> يُعلِن متغيّراً خاصاً قابلاً للتغيير `signingPublicKey` (مفتاح التوقيع العام) من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:37]

```
38:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:38]

```
39:     // Session management
```
> تعليق: إدارة الجلسات. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:39]

```
40:     private lateinit var sessionManager: NoiseSessionManager
```
> يُعلِن متغيّراً خاصاً مؤجّل التهيئة (lateinit) `sessionManager` (مدير الجلسات) من نوع `NoiseSessionManager`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:40]

```
41:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:41]

```
42:     // Channel encryption for password-protected channels
```
> تعليق: تشفير القنوات للقنوات المحميّة بكلمة مرور. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:42]

```
43:     private val channelEncryption = NoiseChannelEncryption()
```
> يُعرِّف متغيّراً خاصاً ثابتاً `channelEncryption` (تشفير القناة) ويهيّئه بكائن جديد من الصنف `NoiseChannelEncryption`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:43]

```
44:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:44]

```
45:     // Identity management for peer ID rotation support
```
> تعليق: إدارة الهوية لدعم تدوير معرّف القرين. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:45]

```
46:     private val identityStateManager: SecureIdentityStateManager
```
> يُعلِن متغيّراً خاصاً ثابتاً `identityStateManager` (مدير حالة الهوية) من نوع `SecureIdentityStateManager` دون تهيئة فورية. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:46]

```
47:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:47]

```
48:     // Centralized fingerprint management - NO LOCAL STORAGE
```
> تعليق: إدارة بصمات مركزية - لا تخزين محلي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:48]

```
49:     private val fingerprintManager = PeerFingerprintManager.getInstance()
```
> يُعرِّف متغيّراً خاصاً ثابتاً `fingerprintManager` (مدير البصمات) ويهيّئه بنتيجة استدعاء `PeerFingerprintManager.getInstance()` (الحصول على النسخة الوحيدة). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:49]

```
50:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:50]

```
51:     // Callbacks
```
> تعليق: ردود النداء (callbacks). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:51]

```
52:     var onPeerAuthenticated: ((String, String) -> Unit)? = null // (peerID, fingerprint)
```
> يُعرِّف متغيّراً عاماً قابلاً للتغيير `onPeerAuthenticated` (عند مصادقة القرين) من نوع دالة تستقبل نصّين وتُعيد `Unit`، قابل للإبطال، قيمته الابتدائية `null`، مع تعليق: (معرّف القرين، البصمة). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:52]

```
53:     var onHandshakeRequired: ((String) -> Unit)? = null // peerID needs handshake
```
> يُعرِّف متغيّراً عاماً قابلاً للتغيير `onHandshakeRequired` (عند الحاجة للمصافحة) من نوع دالة تستقبل نصّاً وتُعيد `Unit`، قابل للإبطال، قيمته الابتدائية `null`، مع تعليق: القرين يحتاج مصافحة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:53]

```
54:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:54]

```
55:     init {
```
> يفتح كتلة التهيئة (init) للصنف التي تُنفَّذ عند إنشاء كائن. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:55]

```
56:         // Initialize identity state manager for persistent storage
```
> تعليق: تهيئة مدير حالة الهوية للتخزين الدائم. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:56]

```
57:         identityStateManager = SecureIdentityStateManager(context)
```
> يُسنِد إلى `identityStateManager` كائناً جديداً من `SecureIdentityStateManager` مُمرِّراً `context`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:57]

```
58:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:58]

```
59:         // Load or create keys - temporary placeholders
```
> تعليق: تحميل أو إنشاء المفاتيح - عناصر نائبة مؤقتة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:59]

```
60:         staticIdentityPrivateKey = ByteArray(32)
```
> يُسنِد إلى `staticIdentityPrivateKey` مصفوفة بايتات جديدة طولها ٣٢ بايتاً. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:60]

```
61:         staticIdentityPublicKey = ByteArray(32)
```
> يُسنِد إلى `staticIdentityPublicKey` مصفوفة بايتات جديدة طولها ٣٢ بايتاً. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:61]

```
62:         signingPrivateKey = ByteArray(32)
```
> يُسنِد إلى `signingPrivateKey` مصفوفة بايتات جديدة طولها ٣٢ بايتاً. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:62]

```
63:         signingPublicKey = ByteArray(32)
```
> يُسنِد إلى `signingPublicKey` مصفوفة بايتات جديدة طولها ٣٢ بايتاً. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:63]

```
64:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:64]

```
65:         loadOrGenerateKeys()
```
> يستدعي الدالة `loadOrGenerateKeys` (تحميل أو توليد المفاتيح). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:65]

```
66:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:66]

```
67:         // Initialize session manager
```
> تعليق: تهيئة مدير الجلسات. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:67]

```
68:         initializeSessionManager()
```
> يستدعي الدالة `initializeSessionManager` (تهيئة مدير الجلسات). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:68]

```
69:     }
```
> إغلاق نطاق كتلة التهيئة (init). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:69]

```
70:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:70]

```
71:     private fun initializeSessionManager() {
```
> يُعرِّف الدالة الخاصة `initializeSessionManager` (تهيئة مدير الجلسات) بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:71]

```
72:         // Create new session manager with current keys
```
> تعليق: إنشاء مدير جلسات جديد بالمفاتيح الحالية. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:72]

```
73:         val localPeerID = calculateFingerprint(staticIdentityPublicKey).take(16)
```
> يُعرِّف متغيّراً ثابتاً `localPeerID` (معرّف القرين المحلي) قيمته أول ١٦ محرفاً من ناتج `calculateFingerprint(staticIdentityPublicKey)` عبر الدالة `take`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:73]

```
74:         sessionManager = NoiseSessionManager(staticIdentityPrivateKey, staticIdentityPublicKey, localPeerID)
```
> يُسنِد إلى `sessionManager` كائناً جديداً من `NoiseSessionManager` مُمرِّراً المفتاح الخاص الثابت والمفتاح العام الثابت ومعرّف القرين المحلي. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:74]

```
75:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:75]

```
76:         // Set up session callbacks
```
> تعليق: إعداد ردود نداء الجلسة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:76]

```
77:         sessionManager.onSessionEstablished = { peerID, remoteStaticKey ->
```
> يُسنِد إلى الخاصية `onSessionEstablished` (عند تأسيس الجلسة) لمدير الجلسات تعبيراً لامبدا يستقبل `peerID` و`remoteStaticKey` ويفتح جسده. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:77]

```
78:             handleSessionEstablished(peerID, remoteStaticKey)
```
> يستدعي الدالة `handleSessionEstablished` (معالجة تأسيس الجلسة) مُمرِّراً `peerID` و`remoteStaticKey`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:78]

```
79:         }
```
> إغلاق نطاق تعبير اللامبدا المُسنَد إلى `onSessionEstablished`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:79]

```
80:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:80]

```
81:         // Ensure any other callbacks are wired if needed
```
> تعليق: التأكّد من ربط أي ردود نداء أخرى إن لزم. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:81]

```
82:         // sessionManager.onSessionFailed could be wired if we exposed it
```
> تعليق: يمكن ربط `sessionManager.onSessionFailed` لو كشفناه. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:82]

```
83:     }
```
> إغلاق نطاق الدالة `initializeSessionManager`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:83]

```
84:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:84]

```
85:     private fun loadOrGenerateKeys() {
```
> يُعرِّف الدالة الخاصة `loadOrGenerateKeys` (تحميل أو توليد المفاتيح) بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:85]

```
86:         // Load or create static identity key (persistent across sessions)
```
> تعليق: تحميل أو إنشاء مفتاح الهوية الثابت (دائم عبر الجلسات). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:86]

```
87:         val loadedKeyPair = identityStateManager.loadStaticKey()
```
> يُعرِّف متغيّراً ثابتاً `loadedKeyPair` (زوج المفاتيح المحمّل) قيمته ناتج استدعاء `identityStateManager.loadStaticKey()` (تحميل المفتاح الثابت). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:87]

```
88:         if (loadedKeyPair != null) {
```
> يبدأ شرطاً يتحقّق إن كان `loadedKeyPair` لا يساوي `null`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:88]

```
89:             staticIdentityPrivateKey = loadedKeyPair.first
```
> يُسنِد إلى `staticIdentityPrivateKey` العنصر الأول (`first`) من زوج المفاتيح المحمّل. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:89]

```
90:             staticIdentityPublicKey = loadedKeyPair.second
```
> يُسنِد إلى `staticIdentityPublicKey` العنصر الثاني (`second`) من زوج المفاتيح المحمّل. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:90]

```
91:             Log.d(TAG, "Loaded existing static identity key: ${calculateFingerprint(staticIdentityPublicKey)}")
```
> يسجّل رسالة تصحيح (Log.d) بالوسم `TAG` نصّها "Loaded existing static identity key:" متبوعاً ببصمة `staticIdentityPublicKey` المحسوبة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:91]

```
92:         } else {
```
> يُغلق فرع `if` ويبدأ فرع `else` (وإلّا). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:92]

```
93:             // Generate new identity key pair
```
> تعليق: توليد زوج مفاتيح هوية جديد. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:93]

```
94:             val keyPair = generateKeyPair()
```
> يُعرِّف متغيّراً ثابتاً `keyPair` (زوج المفاتيح) قيمته ناتج استدعاء الدالة `generateKeyPair` (توليد زوج المفاتيح). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:94]

```
95:             staticIdentityPrivateKey = keyPair.first
```
> يُسنِد إلى `staticIdentityPrivateKey` العنصر الأول من `keyPair`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:95]

```
96:             staticIdentityPublicKey = keyPair.second
```
> يُسنِد إلى `staticIdentityPublicKey` العنصر الثاني من `keyPair`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:96]

```
97:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:97]

```
98:             // Save to secure storage
```
> تعليق: الحفظ في التخزين الآمن. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:98]

```
99:             identityStateManager.saveStaticKey(staticIdentityPrivateKey, staticIdentityPublicKey)
```
> يستدعي `identityStateManager.saveStaticKey` (حفظ المفتاح الثابت) مُمرِّراً المفتاح الخاص والمفتاح العام للهوية الثابتة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:99]

```
100:             Log.d(TAG, "Generated and saved new static identity key")
```
> يسجّل رسالة تصحيح بالوسم `TAG` نصّها "Generated and saved new static identity key". [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:100]

```
101:         }
```
> إغلاق نطاق فرع `else`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:101]

```
102:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:102]

```
103:         // Load or create Ed25519 signing key (persistent across sessions)
```
> تعليق: تحميل أو إنشاء مفتاح التوقيع Ed25519 (دائم عبر الجلسات). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:103]

```
104:         val loadedSigningKeyPair = identityStateManager.loadSigningKey()
```
> يُعرِّف متغيّراً ثابتاً `loadedSigningKeyPair` (زوج مفاتيح التوقيع المحمّل) قيمته ناتج `identityStateManager.loadSigningKey()` (تحميل مفتاح التوقيع). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:104]

```
105:         if (loadedSigningKeyPair != null) {
```
> يبدأ شرطاً يتحقّق إن كان `loadedSigningKeyPair` لا يساوي `null`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:105]

```
106:             signingPrivateKey = loadedSigningKeyPair.first
```
> يُسنِد إلى `signingPrivateKey` العنصر الأول من زوج مفاتيح التوقيع المحمّل. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:106]

```
107:             signingPublicKey = loadedSigningKeyPair.second
```
> يُسنِد إلى `signingPublicKey` العنصر الثاني من زوج مفاتيح التوقيع المحمّل. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:107]

```
108:             Log.d(TAG, "Loaded existing Ed25519 signing key")
```
> يسجّل رسالة تصحيح بالوسم `TAG` نصّها "Loaded existing Ed25519 signing key". [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:108]

```
109:         } else {
```
> يُغلق فرع `if` ويبدأ فرع `else`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:109]

```
110:             // Generate new Ed25519 signing key pair
```
> تعليق: توليد زوج مفاتيح توقيع Ed25519 جديد. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:110]

```
111:             val signingKeyPair = generateEd25519KeyPair()
```
> يُعرِّف متغيّراً ثابتاً `signingKeyPair` (زوج مفاتيح التوقيع) قيمته ناتج استدعاء الدالة `generateEd25519KeyPair` (توليد زوج مفاتيح Ed25519). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:111]

```
112:             signingPrivateKey = signingKeyPair.first
```
> يُسنِد إلى `signingPrivateKey` العنصر الأول من `signingKeyPair`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:112]

```
113:             signingPublicKey = signingKeyPair.second
```
> يُسنِد إلى `signingPublicKey` العنصر الثاني من `signingKeyPair`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:113]

```
114:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:114]

```
115:             // Save to secure storage
```
> تعليق: الحفظ في التخزين الآمن. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:115]

```
116:             identityStateManager.saveSigningKey(signingPrivateKey, signingPublicKey)
```
> يستدعي `identityStateManager.saveSigningKey` (حفظ مفتاح التوقيع) مُمرِّراً مفتاح التوقيع الخاص والعام. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:116]

```
117:             Log.d(TAG, "Generated and saved new Ed25519 signing key")
```
> يسجّل رسالة تصحيح بالوسم `TAG` نصّها "Generated and saved new Ed25519 signing key". [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:117]

```
118:         }
```
> إغلاق نطاق فرع `else`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:118]

```
119:     }
```
> إغلاق نطاق الدالة `loadOrGenerateKeys`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:119]

```
120: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:120]

```
121:     // MARK: - Public Interface
```
> تعليق: علامة قسم (MARK) - الواجهة العامة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:121]

```
122:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:122]

```
123:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:123]

```
124:      * Get our static public key data for sharing (32 bytes)
```
> تعليق: الحصول على بيانات مفتاحنا العام الثابت للمشاركة (٣٢ بايتاً). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:124]

```
125:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:125]

```
126:     fun getStaticPublicKeyData(): ByteArray {
```
> يُعرِّف الدالة العامة `getStaticPublicKeyData` (الحصول على بيانات المفتاح العام الثابت) التي تُعيد `ByteArray` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:126]

```
127:         return staticIdentityPublicKey.clone()
```
> يُعيد نسخة مستنسخة (`clone`) من `staticIdentityPublicKey`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:127]

```
128:     }
```
> إغلاق نطاق الدالة `getStaticPublicKeyData`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:128]

```
129: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:129]

```
130:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:130]

```
131:      * Get our signing public key data for sharing (32 bytes)
```
> تعليق: الحصول على بيانات مفتاح التوقيع العام للمشاركة (٣٢ بايتاً). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:131]

```
132:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:132]

```
133:     fun getSigningPublicKeyData(): ByteArray {
```
> يُعرِّف الدالة العامة `getSigningPublicKeyData` (الحصول على بيانات مفتاح التوقيع العام) التي تُعيد `ByteArray` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:133]

```
134:         return signingPublicKey.clone()
```
> يُعيد نسخة مستنسخة من `signingPublicKey`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:134]

```
135:     }
```
> إغلاق نطاق الدالة `getSigningPublicKeyData`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:135]

```
136:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:136]

```
137:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:137]

```
138:      * Get our identity fingerprint (SHA-256 hash of static public key)
```
> تعليق: الحصول على بصمة هويّتنا (تجزئة SHA-256 للمفتاح العام الثابت). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:138]

```
139:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:139]

```
140:     fun getIdentityFingerprint(): String {
```
> يُعرِّف الدالة العامة `getIdentityFingerprint` (الحصول على بصمة الهوية) التي تُعيد نصّاً (`String`) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:140]

```
141:         val digest = MessageDigest.getInstance("SHA-256")
```
> يُعرِّف متغيّراً ثابتاً `digest` (الهاضم) قيمته نسخة `MessageDigest` لخوارزمية `"SHA-256"`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:141]

```
142:         val hash = digest.digest(staticIdentityPublicKey)
```
> يُعرِّف متغيّراً ثابتاً `hash` (التجزئة) قيمته ناتج `digest.digest` على `staticIdentityPublicKey`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:142]

```
143:         return hash.joinToString("") { "%02x".format(it) }
```
> يُعيد نصّاً ناتجاً عن ضمّ بايتات `hash` بفاصل فارغ، حيث يُنسَّق كل بايت بصيغة سداسية عشرية من خانتين (`"%02x"`). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:143]

```
144:     }
```
> إغلاق نطاق الدالة `getIdentityFingerprint`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:144]

```
145:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:145]

```
146:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:146]

```
147:      * Get peer's public key data (if we have a session)
```
> تعليق: الحصول على بيانات المفتاح العام للقرين (إن كانت لدينا جلسة). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:147]

```
148:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:148]

```
149:     fun getPeerPublicKeyData(peerID: String): ByteArray? {
```
> يُعرِّف الدالة العامة `getPeerPublicKeyData` (الحصول على بيانات المفتاح العام للقرين) التي تستقبل `peerID` نصّياً وتُعيد `ByteArray` قابلاً للإبطال ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:149]

```
150:         return sessionManager.getRemoteStaticKey(peerID)
```
> يُعيد ناتج `sessionManager.getRemoteStaticKey(peerID)` (الحصول على المفتاح الثابت البعيد). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:150]

```
151:     }
```
> إغلاق نطاق الدالة `getPeerPublicKeyData`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:151]

```
152:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:152]

```
153:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:153]

```
154:      * Clear persistent identity (for panic mode)
```
> تعليق: مسح الهوية الدائمة (لوضع الذعر). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:154]

```
155:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:155]

```
156:     fun clearPersistentIdentity() {
```
> يُعرِّف الدالة العامة `clearPersistentIdentity` (مسح الهوية الدائمة) بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:156]

```
157:         Log.w(TAG, "🚨 Panic Mode: Clearing persistent identity and rotating in-memory keys")
```
> يسجّل رسالة تحذير (Log.w) بالوسم `TAG` نصّها "🚨 Panic Mode: Clearing persistent identity and rotating in-memory keys". [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:157]

```
158:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:158]

```
159:         // 1. Clear storage
```
> تعليق: ١. مسح التخزين. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:159]

```
160:         identityStateManager.clearIdentityData()
```
> يستدعي `identityStateManager.clearIdentityData()` (مسح بيانات الهوية). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:160]

```
161:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:161]

```
162:         // 2. Clear all sessions immediately
```
> تعليق: ٢. مسح كل الجلسات فوراً. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:162]

```
163:         if (::sessionManager.isInitialized) {
```
> يبدأ شرطاً يتحقّق إن كان المتغيّر `sessionManager` قد هُيّئ (`isInitialized`). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:163]

```
164:             sessionManager.shutdown()
```
> يستدعي `sessionManager.shutdown()` (إيقاف مدير الجلسات). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:164]

```
165:         }
```
> إغلاق نطاق شرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:165]

```
166:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:166]

```
167:         // 3. Regenerate keys immediately (in-memory rotation)
```
> تعليق: ٣. إعادة توليد المفاتيح فوراً (تدوير في الذاكرة). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:167]

```
168:         loadOrGenerateKeys()
```
> يستدعي الدالة `loadOrGenerateKeys` (تحميل أو توليد المفاتيح). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:168]

```
169:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:169]

```
170:         // 4. Re-initialize SessionManager with new keys
```
> تعليق: ٤. إعادة تهيئة مدير الجلسات بالمفاتيح الجديدة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:170]

```
171:         initializeSessionManager()
```
> يستدعي الدالة `initializeSessionManager` (تهيئة مدير الجلسات). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:171]

```
172:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:172]

```
173:         Log.d(TAG, "✅ Identity cleared and keys rotated")
```
> يسجّل رسالة تصحيح بالوسم `TAG` نصّها "✅ Identity cleared and keys rotated". [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:173]

```
174:     }
```
> إغلاق نطاق الدالة `clearPersistentIdentity`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:174]

```
175:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:175]

```
176:     // MARK: - Handshake Management
```
> تعليق: علامة قسم (MARK) - إدارة المصافحة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:176]

```
177:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:177]

```
178:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:178]

```
179:      * Initiate a Noise handshake with a peer
```
> تعليق: بدء مصافحة نويز مع قرين. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:179]

```
180:      * Returns the first handshake message to send
```
> تعليق: تُعيد أول رسالة مصافحة لإرسالها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:180]

```
181:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:181]

```
182:     fun initiateHandshake(peerID: String): ByteArray? {
```
> يُعرِّف الدالة العامة `initiateHandshake` (بدء المصافحة) التي تستقبل `peerID` نصّياً وتُعيد `ByteArray` قابلاً للإبطال ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:182]

```
183:         return try {
```
> يبدأ تعبير `try` (محاولة) تُعاد قيمته. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:183]

```
184:             sessionManager.initiateHandshake(peerID)
```
> يستدعي `sessionManager.initiateHandshake(peerID)` (بدء المصافحة) ويُعيد ناتجه. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:184]

```
185:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` (التقاط) للاستثناء `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:185]

```
186:             Log.e(TAG, "Failed to initiate handshake with $peerID: ${e.message}")
```
> يسجّل رسالة خطأ (Log.e) بالوسم `TAG` نصّها "Failed to initiate handshake with" متبوعاً بـ `peerID` ورسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:186]

```
187:             null
```
> يُعيد `null` كقيمة كتلة `catch`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:187]

```
188:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:188]

```
189:     }
```
> إغلاق نطاق الدالة `initiateHandshake`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:189]

```
190:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:190]

```
191:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:191]

```
192:      * Process an incoming handshake message
```
> تعليق: معالجة رسالة مصافحة واردة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:192]

```
193:      * Returns response message if needed, null if handshake complete or failed
```
> تعليق: تُعيد رسالة الرد إن لزم، و`null` إن اكتملت المصافحة أو فشلت. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:193]

```
194:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:194]

```
195:     fun processHandshakeMessage(data: ByteArray, peerID: String): ByteArray? {
```
> يُعرِّف الدالة العامة `processHandshakeMessage` (معالجة رسالة المصافحة) التي تستقبل `data` من نوع `ByteArray` و`peerID` نصّياً وتُعيد `ByteArray` قابلاً للإبطال ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:195]

```
196:         return try {
```
> يبدأ تعبير `try` تُعاد قيمته. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:196]

```
197:             sessionManager.processHandshakeMessage(peerID, data)
```
> يستدعي `sessionManager.processHandshakeMessage(peerID, data)` (معالجة رسالة المصافحة) ويُعيد ناتجه. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:197]

```
198:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` للاستثناء `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:198]

```
199:             Log.e(TAG, "Failed to process handshake from $peerID: ${e.message}")
```
> يسجّل رسالة خطأ بالوسم `TAG` نصّها "Failed to process handshake from" متبوعاً بـ `peerID` ورسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:199]

```
200:             null
```
> يُعيد `null` كقيمة كتلة `catch`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:200]

```
201:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:201]

```
202:     }
```
> إغلاق نطاق الدالة `processHandshakeMessage`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:202]

```
203:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:203]

```
204:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:204]

```
205:      * Check if we have an established session with a peer
```
> تعليق: التحقّق إن كانت لدينا جلسة مؤسَّسة مع قرين. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:205]

```
206:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:206]

```
207:     fun hasEstablishedSession(peerID: String): Boolean {
```
> يُعرِّف الدالة العامة `hasEstablishedSession` (هل توجد جلسة مؤسَّسة) التي تستقبل `peerID` نصّياً وتُعيد قيمة منطقية (`Boolean`) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:207]

```
208:         return sessionManager.hasEstablishedSession(peerID)
```
> يُعيد ناتج `sessionManager.hasEstablishedSession(peerID)`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:208]

```
209:     }
```
> إغلاق نطاق الدالة `hasEstablishedSession`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:209]

```
210:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:210]

```
211:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:211]

```
212:      * Get session state for a peer (for UI state display)
```
> تعليق: الحصول على حالة الجلسة لقرين (لعرض الحالة في الواجهة). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:212]

```
213:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:213]

```
214:     fun getSessionState(peerID: String): NoiseSession.NoiseSessionState {
```
> يُعرِّف الدالة العامة `getSessionState` (الحصول على حالة الجلسة) التي تستقبل `peerID` نصّياً وتُعيد نوع `NoiseSession.NoiseSessionState` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:214]

```
215:         return sessionManager.getSessionState(peerID)
```
> يُعيد ناتج `sessionManager.getSessionState(peerID)`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:215]

```
216:     }
```
> إغلاق نطاق الدالة `getSessionState`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:216]

```
217:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:217]

```
218:     // MARK: - Encryption/Decryption
```
> تعليق: علامة قسم (MARK) - التشفير/فك التشفير. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:218]

```
219:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:219]

```
220:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:220]

```
221:      * Encrypt data for a specific peer using established Noise session
```
> تعليق: تشفير البيانات لقرين محدّد باستعمال جلسة نويز المؤسَّسة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:221]

```
222:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:222]

```
223:     fun encrypt(data: ByteArray, peerID: String): ByteArray? {
```
> يُعرِّف الدالة العامة `encrypt` (التشفير) التي تستقبل `data` من نوع `ByteArray` و`peerID` نصّياً وتُعيد `ByteArray` قابلاً للإبطال ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:223]

```
224:         if (!hasEstablishedSession(peerID)) {
```
> يبدأ شرطاً يتحقّق إن لم تكن هناك جلسة مؤسَّسة مع `peerID` (نفي `hasEstablishedSession`). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:224]

```
225:             Log.w(TAG, "No established session with $peerID, handshake required. TODO: IMPLEMENT HANDSHAKE INIT")
```
> يسجّل رسالة تحذير بالوسم `TAG` نصّها "No established session with" متبوعاً بـ `peerID` و"handshake required. TODO: IMPLEMENT HANDSHAKE INIT". [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:225]

```
226:             onHandshakeRequired?.invoke(peerID)
```
> يستدعي ردّ النداء `onHandshakeRequired` بأمان (إن لم يكن `null`) مُمرِّراً `peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:226]

```
227:             return null
```
> يُعيد `null` خروجاً من الدالة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:227]

```
228:         }
```
> إغلاق نطاق شرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:228]

```
229:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:229]

```
230:         return try {
```
> يبدأ تعبير `try` تُعاد قيمته. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:230]

```
231:             sessionManager.encrypt(data, peerID)
```
> يستدعي `sessionManager.encrypt(data, peerID)` (التشفير) ويُعيد ناتجه. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:231]

```
232:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` للاستثناء `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:232]

```
233:             Log.e(TAG, "Failed to encrypt for $peerID: ${e.message}")
```
> يسجّل رسالة خطأ بالوسم `TAG` نصّها "Failed to encrypt for" متبوعاً بـ `peerID` ورسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:233]

```
234:             null
```
> يُعيد `null` كقيمة كتلة `catch`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:234]

```
235:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:235]

```
236:     }
```
> إغلاق نطاق الدالة `encrypt`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:236]

```
237:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:237]

```
238:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:238]

```
239:      * Decrypt data from a specific peer using established Noise session
```
> تعليق: فك تشفير البيانات من قرين محدّد باستعمال جلسة نويز المؤسَّسة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:239]

```
240:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:240]

```
241:     fun decrypt(encryptedData: ByteArray, peerID: String): ByteArray? {
```
> يُعرِّف الدالة العامة `decrypt` (فك التشفير) التي تستقبل `encryptedData` من نوع `ByteArray` و`peerID` نصّياً وتُعيد `ByteArray` قابلاً للإبطال ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:241]

```
242:         if (!hasEstablishedSession(peerID)) {
```
> يبدأ شرطاً يتحقّق إن لم تكن هناك جلسة مؤسَّسة مع `peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:242]

```
243:             Log.w(TAG, "No established session with $peerID")
```
> يسجّل رسالة تحذير بالوسم `TAG` نصّها "No established session with" متبوعاً بـ `peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:243]

```
244:             return null
```
> يُعيد `null` خروجاً من الدالة. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:244]

```
245:         }
```
> إغلاق نطاق شرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:245]

```
246:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:246]

```
247:         return try {
```
> يبدأ تعبير `try` تُعاد قيمته. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:247]

```
248:             sessionManager.decrypt(encryptedData, peerID)
```
> يستدعي `sessionManager.decrypt(encryptedData, peerID)` (فك التشفير) ويُعيد ناتجه. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:248]

```
249:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` للاستثناء `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:249]

```
250:             Log.e(TAG, "Failed to decrypt from $peerID: ${e.message}")
```
> يسجّل رسالة خطأ بالوسم `TAG` نصّها "Failed to decrypt from" متبوعاً بـ `peerID` ورسالة الاستثناء (يستمر السطر بعد المدى). [app/src/main/java/com/bitchat/android/noise/NoiseEncryptionService.kt:250]
