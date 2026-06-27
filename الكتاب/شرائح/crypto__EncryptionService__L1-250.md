# شريحة — app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt (الأسطر 1–250)

```
1: package com.bitchat.android.crypto
```
> يعلن هذا السطر أن الملف ينتمي إلى الحزمة (package) المسمّاة `com.bitchat.android.crypto`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:2]

```
3: import android.content.Context
```
> يستورد (import) النوع `Context` من حزمة أندرويد `android.content` لاستعماله في الملف. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:3]

```
4: import android.content.SharedPreferences
```
> يستورد النوع `SharedPreferences` من حزمة `android.content` وهو واجهة تخزين أزواج مفتاح‑قيمة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:4]

```
5: import android.util.Base64
```
> يستورد الصنف `Base64` من حزمة `android.util` لترميز وفك ترميز البيانات. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:5]

```
6: import android.util.Log
```
> يستورد الصنف `Log` من حزمة `android.util` لكتابة رسائل السجل (logging). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:6]

```
7: import androidx.security.crypto.EncryptedSharedPreferences
```
> يستورد الصنف `EncryptedSharedPreferences` من مكتبة الأمان في `androidx.security.crypto` وهو تخزين مفضّلات مشفّر. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:7]

```
8: import androidx.security.crypto.MasterKey
```
> يستورد الصنف `MasterKey` من `androidx.security.crypto` وهو المفتاح الرئيس المستخدم في التشفير. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:8]

```
9: import com.bitchat.android.noise.NoiseEncryptionService
```
> يستورد الصنف `NoiseEncryptionService` من حزمة `com.bitchat.android.noise` وهو خدمة تشفير بروتوكول Noise. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:9]

```
10: import org.bouncycastle.crypto.AsymmetricCipherKeyPair
```
> يستورد النوع `AsymmetricCipherKeyPair` من مكتبة BouncyCastle وهو زوج مفاتيح تشفير غير متماثل. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:10]

```
11: import org.bouncycastle.crypto.generators.Ed25519KeyPairGenerator
```
> يستورد الصنف `Ed25519KeyPairGenerator` من BouncyCastle وهو مولّد أزواج مفاتيح Ed25519. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:11]

```
12: import org.bouncycastle.crypto.params.Ed25519KeyGenerationParameters
```
> يستورد الصنف `Ed25519KeyGenerationParameters` من BouncyCastle وهو معاملات توليد مفاتيح Ed25519. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:12]

```
13: import org.bouncycastle.crypto.params.Ed25519PrivateKeyParameters
```
> يستورد الصنف `Ed25519PrivateKeyParameters` من BouncyCastle وهو معاملات المفتاح الخاص Ed25519. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:13]

```
14: import org.bouncycastle.crypto.params.Ed25519PublicKeyParameters
```
> يستورد الصنف `Ed25519PublicKeyParameters` من BouncyCastle وهو معاملات المفتاح العام Ed25519. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:14]

```
15: import org.bouncycastle.crypto.signers.Ed25519Signer
```
> يستورد الصنف `Ed25519Signer` من BouncyCastle وهو موقّع التواقيع بخوارزمية Ed25519. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:15]

```
16: import java.security.SecureRandom
```
> يستورد الصنف `SecureRandom` من `java.security` وهو مولّد أعداد عشوائية آمن تشفيرياً. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:16]

```
17: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف `ConcurrentHashMap` من `java.util.concurrent` وهو خريطة تجزئة آمنة للاستخدام المتزامن. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:17]

```
18: import androidx.core.content.edit
```
> يستورد دالة الامتداد `edit` من `androidx.core.content` لتعديل المفضّلات. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:18]

```
19: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:19]

```
20: /**
```
> تعليق: بداية كتلة توثيق (KDoc) متعدّدة الأسطر. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:20]

```
21:  * Encryption service that now uses NoiseEncryptionService internally
```
> تعليق: «خدمة تشفير تستخدم الآن خدمة تشفير Noise داخلياً». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:21]

```
22:  * Maintains the same public API for backward compatibility
```
> تعليق: «تحافظ على نفس الواجهة البرمجية العامة من أجل التوافق مع الإصدارات السابقة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:22]

```
23:  * 
```
> تعليق: سطر فارغ داخل كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:23]

```
24:  * This is the main interface for all encryption/decryption operations in bitchat.
```
> تعليق: «هذه هي الواجهة الرئيسة لجميع عمليات التشفير وفك التشفير في bitchat». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:24]

```
25:  * It now uses the Noise protocol for secure transport encryption with proper session management.
```
> تعليق: «تستخدم الآن بروتوكول Noise لتشفير نقل آمن مع إدارة جلسات سليمة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:25]

```
26:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:26]

```
27: open class EncryptionService(private val context: Context) {
```
> يعرّف الصنف المفتوح للتوريث (open class) المسمّى `EncryptionService` (خدمة التشفير) الذي يأخذ في بانيه معاملاً خاصاً `context` من النوع `Context`، ويفتح نطاق جسم الصنف. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:27]

```
28:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:28]

```
29:     companion object {
```
> يفتح كائن المرافقة (companion object) لتعريف أعضاء ثابتة على مستوى الصنف. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:29]

```
30:         private const val TAG = "EncryptionService"
```
> يعرّف الثابت الخاص `TAG` (الوسم) ويضبط قيمته إلى السلسلة الحرفية `"EncryptionService"`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:30]

```
31:         private const val ED25519_PRIVATE_KEY_PREF = "ed25519_signing_private_key"
```
> يعرّف الثابت الخاص `ED25519_PRIVATE_KEY_PREF` (مفتاح تفضيل المفتاح الخاص) ويضبط قيمته إلى السلسلة الحرفية `"ed25519_signing_private_key"`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:31]

```
32:         private const val OLD_PREFS_NAME = "bitchat_crypto"
```
> يعرّف الثابت الخاص `OLD_PREFS_NAME` (اسم المفضّلات القديم) ويضبط قيمته إلى السلسلة الحرفية `"bitchat_crypto"`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:32]

```
33:         private const val SECURE_PREFS_NAME = "bitchat_crypto_secure"
```
> يعرّف الثابت الخاص `SECURE_PREFS_NAME` (اسم المفضّلات الآمن) ويضبط قيمته إلى السلسلة الحرفية `"bitchat_crypto_secure"`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:33]

```
34:     }
```
> إغلاق نطاق كائن المرافقة (companion object). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:34]

```
35:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:35]

```
36:     // Core Noise encryption service
```
> تعليق: «خدمة تشفير Noise الأساسية». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:36]

```
37:     private val noiseService: NoiseEncryptionService by lazy { NoiseEncryptionService(context) }
```
> يعرّف المتغيّر الخاص الثابت `noiseService` (خدمة Noise) من النوع `NoiseEncryptionService` ويهيّئه تهيئة كسولة (lazy) بإنشاء كائن `NoiseEncryptionService(context)` عند أول استعمال. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:37]

```
38:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:38]

```
39:     // Session tracking for established connections
```
> تعليق: «تتبّع الجلسات للاتصالات المؤسَّسة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:39]

```
40:     private val establishedSessions = ConcurrentHashMap<String, String>() // peerID -> fingerprint
```
> يعرّف المتغيّر الخاص الثابت `establishedSessions` (الجلسات المؤسَّسة) ويسنده إلى كائن `ConcurrentHashMap` بمفاتيح `String` وقيم `String`، مع تعليق: «معرّف النِّد ← البصمة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:40]

```
41:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:41]

```
42:     // Ed25519 signing keys (separate from Noise static keys)
```
> تعليق: «مفاتيح توقيع Ed25519 (منفصلة عن مفاتيح Noise الثابتة)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:42]

```
43:     private lateinit var ed25519PrivateKey: Ed25519PrivateKeyParameters
```
> يعرّف المتغيّر الخاص المؤجَّل التهيئة (lateinit) `ed25519PrivateKey` (المفتاح الخاص Ed25519) من النوع `Ed25519PrivateKeyParameters`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:43]

```
44:     private lateinit var ed25519PublicKey: Ed25519PublicKeyParameters
```
> يعرّف المتغيّر الخاص المؤجَّل التهيئة `ed25519PublicKey` (المفتاح العام Ed25519) من النوع `Ed25519PublicKeyParameters`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:44]

```
45:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:45]

```
46:     // Callbacks for UI state updates
```
> تعليق: «دوال ردّ النداء لتحديثات حالة واجهة المستخدم». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:46]

```
47:     var onSessionEstablished: ((String) -> Unit)? = null // peerID
```
> يعرّف المتغيّر العام `onSessionEstablished` (عند تأسيس الجلسة) من نوع دالة تقبل `String` وتعيد `Unit` وقابل للعدم، ويضبط قيمته الابتدائية إلى `null`، مع تعليق: «معرّف النِّد». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:47]

```
48:     var onSessionLost: ((String) -> Unit)? = null // peerID
```
> يعرّف المتغيّر العام `onSessionLost` (عند فقدان الجلسة) من نوع دالة تقبل `String` وتعيد `Unit` وقابل للعدم، ويضبط قيمته الابتدائية إلى `null`، مع تعليق: «معرّف النِّد». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:48]

```
49:     var onHandshakeRequired: ((String) -> Unit)? = null // peerID
```
> يعرّف المتغيّر العام `onHandshakeRequired` (عند لزوم المصافحة) من نوع دالة تقبل `String` وتعيد `Unit` وقابل للعدم، ويضبط قيمته الابتدائية إلى `null`، مع تعليق: «معرّف النِّد». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:49]

```
50:     private lateinit var prefs: SharedPreferences
```
> يعرّف المتغيّر الخاص المؤجَّل التهيئة `prefs` (المفضّلات) من النوع `SharedPreferences`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:50]

```
51:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:51]

```
52:     init {
```
> يفتح كتلة التهيئة (init) التي تُنفَّذ عند إنشاء كائن الصنف. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:52]

```
53:         initialize()
```
> يستدعي الدالة `initialize` (التهيئة) داخل كتلة التهيئة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:53]

```
54:     }
```
> إغلاق نطاق كتلة التهيئة (init). [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:54]

```
55: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:55]

```
56:     private fun setUpEncryptedPrefs() {
```
> يعرّف الدالة الخاصة `setUpEncryptedPrefs` (إعداد المفضّلات المشفّرة) بلا معاملات، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:56]

```
57:         val masterKey = MasterKey.Builder(context, MasterKey.DEFAULT_MASTER_KEY_ALIAS)
```
> يعرّف المتغيّر الثابت `masterKey` (المفتاح الرئيس) ويبدأ سلسلة بناء عبر `MasterKey.Builder` ممرِّراً `context` و`MasterKey.DEFAULT_MASTER_KEY_ALIAS`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:57]

```
58:             .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
```
> يستدعي `setKeyScheme` على البنّاء ويمرّر مخطط المفتاح `MasterKey.KeyScheme.AES256_GCM`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:58]

```
59:             .build()
```
> يستدعي `build` على البنّاء لإنشاء كائن `MasterKey` وإسناده إلى `masterKey`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:59]

```
60: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:60]

```
61:         // Create encrypted shared preferences
```
> تعليق: «إنشاء مفضّلات مشتركة مشفّرة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:61]

```
62:         prefs = EncryptedSharedPreferences.create(
```
> يسند إلى المتغيّر `prefs` نتيجة استدعاء `EncryptedSharedPreferences.create` ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:62]

```
63:             context,
```
> يمرّر الوسيط `context` إلى دالة `create`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:63]

```
64:             SECURE_PREFS_NAME,
```
> يمرّر الثابت `SECURE_PREFS_NAME` (اسم المفضّلات الآمن) إلى دالة `create`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:64]

```
65:             masterKey,
```
> يمرّر المتغيّر `masterKey` إلى دالة `create`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:65]

```
66:             EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
```
> يمرّر مخطط تشفير المفاتيح `EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV` إلى دالة `create`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:66]

```
67:             EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
```
> يمرّر مخطط تشفير القيم `EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM` إلى دالة `create`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:67]

```
68:         )
```
> يغلق قائمة وسائط استدعاء `create`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:68]

```
69:     }
```
> إغلاق نطاق الدالة `setUpEncryptedPrefs`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:69]

```
70: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:70]

```
71:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:71]

```
72:      * Initialization logic moved to method to allow overriding in tests
```
> تعليق: «منطق التهيئة نُقل إلى دالة للسماح بإعادة تعريفه في الاختبارات». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:72]

```
73:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:73]

```
74:     protected open fun initialize() {
```
> يعرّف الدالة المحمية المفتوحة للتوريث `initialize` (التهيئة) بلا معاملات، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:74]

```
75:         setUpEncryptedPrefs()
```
> يستدعي الدالة `setUpEncryptedPrefs` لإعداد المفضّلات المشفّرة. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:75]

```
76:         // Initialize or load Ed25519 signing keys
```
> تعليق: «تهيئة أو تحميل مفاتيح توقيع Ed25519». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:76]

```
77:         val keyPair = loadOrCreateEd25519KeyPair()
```
> يعرّف المتغيّر الثابت `keyPair` (زوج المفاتيح) ويسنده إلى نتيجة استدعاء `loadOrCreateEd25519KeyPair`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:77]

```
78:         ed25519PrivateKey = keyPair.private as Ed25519PrivateKeyParameters
```
> يسند إلى `ed25519PrivateKey` عضو `private` من `keyPair` بعد تحويله (cast) إلى `Ed25519PrivateKeyParameters`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:78]

```
79:         ed25519PublicKey = keyPair.public as Ed25519PublicKeyParameters
```
> يسند إلى `ed25519PublicKey` عضو `public` من `keyPair` بعد تحويله إلى `Ed25519PublicKeyParameters`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:79]

```
80:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:80]

```
81:         Log.d(TAG, "✅ Ed25519 signing keys initialized")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"✅ Ed25519 signing keys initialized"` لتسجيل تهيئة مفاتيح التوقيع. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:81]

```
82:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:82]

```
83:         // Set up NoiseEncryptionService callbacks
```
> تعليق: «إعداد دوال ردّ النداء لخدمة تشفير Noise». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:83]

```
84:         noiseService.onPeerAuthenticated = { peerID, fingerprint ->
```
> يسند إلى الخاصية `onPeerAuthenticated` (عند مصادقة النِّد) في `noiseService` تعبيراً لامبدا يأخذ المعاملين `peerID` و`fingerprint`، ويفتح جسم اللامبدا. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:84]

```
85:             Log.d(TAG, "✅ Noise session established with $peerID, fingerprint: ${fingerprint.take(16)}...")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة تتضمّن قيمة `peerID` وأول ١٦ محرفاً من `fingerprint` عبر `take(16)` متبوعة بثلاث نقاط. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:85]

```
86:             establishedSessions[peerID] = fingerprint
```
> يخزّن في خريطة `establishedSessions` قيمة `fingerprint` تحت المفتاح `peerID`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:86]

```
87:             onSessionEstablished?.invoke(peerID)
```
> يستدعي دالة ردّ النداء `onSessionEstablished` إن لم تكن عدماً، ممرِّراً `peerID` عبر `invoke`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:87]

```
88:         }
```
> إغلاق نطاق تعبير اللامبدا المسند إلى `onPeerAuthenticated`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:88]

```
89:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:89]

```
90:         noiseService.onHandshakeRequired = { peerID ->
```
> يسند إلى الخاصية `onHandshakeRequired` (عند لزوم المصافحة) في `noiseService` تعبير لامبدا يأخذ المعامل `peerID`، ويفتح جسم اللامبدا. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:90]

```
91:             Log.d(TAG, "🤝 Handshake required for $peerID")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"🤝 Handshake required for $peerID"` متضمّنة قيمة `peerID`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:91]

```
92:             onHandshakeRequired?.invoke(peerID)
```
> يستدعي دالة ردّ النداء `onHandshakeRequired` إن لم تكن عدماً، ممرِّراً `peerID` عبر `invoke`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:92]

```
93:         }
```
> إغلاق نطاق تعبير اللامبدا المسند إلى `onHandshakeRequired`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:93]

```
94:     }
```
> إغلاق نطاق الدالة `initialize`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:94]

```
95:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:95]

```
96:     // MARK: - Public API (Maintains backward compatibility)
```
> تعليق: «علامة قسم: الواجهة البرمجية العامة (تحافظ على التوافق مع الإصدارات السابقة)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:96]

```
97:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:97]

```
98:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:98]

```
99:      * Get our static public key data (32 bytes for Noise)
```
> تعليق: «احصل على بيانات مفتاحنا العام الثابت (٣٢ بايت لبروتوكول Noise)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:99]

```
100:      * This replaces the old 96-byte combined key format
```
> تعليق: «هذا يحلّ محلّ صيغة المفتاح المدمج القديمة بحجم ٩٦ بايت». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:100]

```
101:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:101]

```
102:     fun getCombinedPublicKeyData(): ByteArray {
```
> يعرّف الدالة العامة `getCombinedPublicKeyData` (الحصول على بيانات المفتاح العام المدمج) التي تعيد `ByteArray`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:102]

```
103:         return noiseService.getStaticPublicKeyData()
```
> يعيد نتيجة استدعاء `getStaticPublicKeyData` على `noiseService`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:103]

```
104:     }
```
> إغلاق نطاق الدالة `getCombinedPublicKeyData`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:104]

```
105:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:105]

```
106:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:106]

```
107:      * Get our static public key for Noise protocol (for identity announcements)
```
> تعليق: «احصل على مفتاحنا العام الثابت لبروتوكول Noise (لإعلانات الهوية)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:107]

```
108:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:108]

```
109:     fun getStaticPublicKey(): ByteArray? {
```
> يعرّف الدالة العامة `getStaticPublicKey` (الحصول على المفتاح العام الثابت) التي تعيد `ByteArray` قابلاً للعدم، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:109]

```
110:         return noiseService.getStaticPublicKeyData()
```
> يعيد نتيجة استدعاء `getStaticPublicKeyData` على `noiseService`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:110]

```
111:     }
```
> إغلاق نطاق الدالة `getStaticPublicKey`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:111]

```
112:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:112]

```
113:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:113]

```
114:      * Get our signing public key for Ed25519 signatures (for identity announcements)
```
> تعليق: «احصل على مفتاح التوقيع العام لتواقيع Ed25519 (لإعلانات الهوية)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:114]

```
115:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:115]

```
116:     fun getSigningPublicKey(): ByteArray? {
```
> يعرّف الدالة العامة `getSigningPublicKey` (الحصول على مفتاح التوقيع العام) التي تعيد `ByteArray` قابلاً للعدم، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:116]

```
117:         return ed25519PublicKey.encoded
```
> يعيد قيمة الخاصية `encoded` من `ed25519PublicKey`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:117]

```
118:     }
```
> إغلاق نطاق الدالة `getSigningPublicKey`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:118]

```
119:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:119]

```
120:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:120]

```
121:      * Sign data using our Ed25519 signing key (for identity announcements)
```
> تعليق: «وقّع البيانات باستخدام مفتاح توقيع Ed25519 الخاص بنا (لإعلانات الهوية)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:121]

```
122:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:122]

```
123:     fun signData(data: ByteArray): ByteArray? {
```
> يعرّف الدالة العامة `signData` (توقيع البيانات) التي تأخذ المعامل `data` من النوع `ByteArray` وتعيد `ByteArray` قابلاً للعدم، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:123]

```
124:         return try {
```
> يبدأ بإعادة نتيجة كتلة `try` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:124]

```
125:             val signer = Ed25519Signer()
```
> يعرّف المتغيّر الثابت `signer` (الموقّع) ويسنده إلى كائن جديد من `Ed25519Signer`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:125]

```
126:             signer.init(true, ed25519PrivateKey)
```
> يستدعي `init` على `signer` بالقيمة `true` (وضع التوقيع) والمفتاح `ed25519PrivateKey`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:126]

```
127:             signer.update(data, 0, data.size)
```
> يستدعي `update` على `signer` ممرِّراً `data` والإزاحة `0` والطول `data.size`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:127]

```
128:             val signature = signer.generateSignature()
```
> يعرّف المتغيّر الثابت `signature` (التوقيع) ويسنده إلى نتيجة استدعاء `generateSignature` على `signer`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:128]

```
129:             Log.d(TAG, "✅ Generated Ed25519 signature (${signature.size} bytes)")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة تتضمّن حجم `signature` عبر `signature.size`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:129]

```
130:             signature
```
> يجعل قيمة `signature` آخر تعبير في كتلة `try` ومن ثَمّ القيمة المعادة منها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:130]

```
131:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة `catch` لالتقاط استثناء من النوع `Exception` باسم `e`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:131]

```
132:             Log.e(TAG, "❌ Failed to sign data with Ed25519: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ورسالة خطأ تتضمّن `e.message`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:132]

```
133:             null
```
> يجعل `null` آخر تعبير في كتلة `catch` ومن ثَمّ القيمة المعادة عند الاستثناء. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:133]

```
134:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:134]

```
135:     }
```
> إغلاق نطاق الدالة `signData`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:135]

```
136:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:136]

```
137:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:137]

```
138:      * Add peer's public key and start handshake if needed
```
> تعليق: «أضف المفتاح العام للنِّد وابدأ المصافحة إذا لزم». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:138]

```
139:      * For backward compatibility with old key exchange packets
```
> تعليق: «من أجل التوافق مع حِزَم تبادل المفاتيح القديمة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:139]

```
140:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:140]

```
141:     @Throws(Exception::class)
```
> يضع التعليق التوضيحي `@Throws(Exception::class)` للإشارة إلى أن الدالة التالية قد تطرح استثناء من النوع `Exception`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:141]

```
142:     fun addPeerPublicKey(peerID: String, publicKeyData: ByteArray) {
```
> يعرّف الدالة العامة `addPeerPublicKey` (إضافة المفتاح العام للنِّد) التي تأخذ `peerID` من النوع `String` و`publicKeyData` من النوع `ByteArray`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:142]

```
143:         Log.d(TAG, "Legacy addPeerPublicKey called for $peerID with ${publicKeyData.size} bytes")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة تتضمّن `peerID` وحجم `publicKeyData` عبر `publicKeyData.size`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:143]

```
144:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:144]

```
145:         // If this is from old key exchange format, initiate new Noise handshake
```
> تعليق: «إذا كان هذا من صيغة تبادل المفاتيح القديمة، ابدأ مصافحة Noise جديدة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:145]

```
146:         if (!hasEstablishedSession(peerID)) {
```
> يبدأ شرط `if` يتحقّق من نفي نتيجة `hasEstablishedSession(peerID)` أي عدم وجود جلسة مؤسَّسة، ويفتح كتلته. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:146]

```
147:             Log.d(TAG, "No Noise session with $peerID, initiating handshake")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"No Noise session with $peerID, initiating handshake"` متضمّنة `peerID`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:147]

```
148:             initiateHandshake(peerID)
```
> يستدعي الدالة `initiateHandshake` (بدء المصافحة) ممرِّراً `peerID`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:148]

```
149:         }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:149]

```
150:     }
```
> إغلاق نطاق الدالة `addPeerPublicKey`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:150]

```
151:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:151]

```
152:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:152]

```
153:      * Get peer's identity key (fingerprint) for favorites
```
> تعليق: «احصل على مفتاح هوية النِّد (البصمة) للمفضّلين». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:153]

```
154:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:154]

```
155:     fun getPeerIdentityKey(peerID: String): ByteArray? {
```
> يعرّف الدالة العامة `getPeerIdentityKey` (الحصول على مفتاح هوية النِّد) التي تأخذ `peerID` من النوع `String` وتعيد `ByteArray` قابلاً للعدم، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:155]

```
156:         val fingerprint = getPeerFingerprint(peerID) ?: return null
```
> يعرّف المتغيّر الثابت `fingerprint` (البصمة) ويسنده إلى نتيجة `getPeerFingerprint(peerID)`، وإن كانت عدماً يعيد `null` فوراً عبر معامل إلفيس. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:156]

```
157:         return fingerprint.toByteArray()
```
> يعيد تحويل `fingerprint` إلى مصفوفة بايتات عبر `toByteArray`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:157]

```
158:     }
```
> إغلاق نطاق الدالة `getPeerIdentityKey`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:158]

```
159:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:159]

```
160:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:160]

```
161:      * Clear persistent identity (for panic mode)
```
> تعليق: «امسح الهوية الدائمة (لوضع الذعر)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:161]

```
162:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:162]

```
163:     fun clearPersistentIdentity() {
```
> يعرّف الدالة العامة `clearPersistentIdentity` (مسح الهوية الدائمة) بلا معاملات، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:163]

```
164:         noiseService.clearPersistentIdentity()
```
> يستدعي `clearPersistentIdentity` على `noiseService`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:164]

```
165:         establishedSessions.clear()
```
> يستدعي `clear` على خريطة `establishedSessions` لإفراغها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:165]

```
166:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:166]

```
167:         // Clear Ed25519 signing key from preferences
```
> تعليق: «امسح مفتاح توقيع Ed25519 من المفضّلات». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:167]

```
168:         try {
```
> يفتح كتلة `try` لتنفيذ شيفرة قد تطرح استثناء. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:168]

```
169:             prefs.edit { remove(ED25519_PRIVATE_KEY_PREF) }
```
> يستدعي دالة الامتداد `edit` على `prefs` وداخل اللامبدا يستدعي `remove` على المفتاح `ED25519_PRIVATE_KEY_PREF` لحذفه. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:169]

```
170:             Log.d(TAG, "🗑️ Cleared Ed25519 signing keys from preferences")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"🗑️ Cleared Ed25519 signing keys from preferences"`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:170]

```
171: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:171]

```
172:             // Generate new keys immediately
```
> تعليق: «ولّد مفاتيح جديدة فوراً». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:172]

```
173:             val keyPair = loadOrCreateEd25519KeyPair()
```
> يعرّف المتغيّر الثابت `keyPair` (زوج المفاتيح) ويسنده إلى نتيجة استدعاء `loadOrCreateEd25519KeyPair`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:173]

```
174:             ed25519PrivateKey = keyPair.private as Ed25519PrivateKeyParameters
```
> يسند إلى `ed25519PrivateKey` عضو `private` من `keyPair` بعد تحويله إلى `Ed25519PrivateKeyParameters`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:174]

```
175:             ed25519PublicKey = keyPair.public as Ed25519PublicKeyParameters
```
> يسند إلى `ed25519PublicKey` عضو `public` من `keyPair` بعد تحويله إلى `Ed25519PublicKeyParameters`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:175]

```
176:             Log.d(TAG, "✅ Rotated Ed25519 signing keys in memory")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"✅ Rotated Ed25519 signing keys in memory"`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:176]

```
177:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة `catch` لالتقاط استثناء من النوع `Exception` باسم `e`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:177]

```
178:             Log.e(TAG, "❌ Failed to clear Ed25519 keys: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ورسالة خطأ تتضمّن `e.message`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:178]

```
179:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:179]

```
180:     }
```
> إغلاق نطاق الدالة `clearPersistentIdentity`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:180]

```
181:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:181]

```
182:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:182]

```
183:      * Encrypt data for a specific peer using Noise transport encryption
```
> تعليق: «شفّر البيانات لنِدّ محدّد باستخدام تشفير النقل في Noise». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:183]

```
184:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:184]

```
185:     @Throws(Exception::class)
```
> يضع التعليق التوضيحي `@Throws(Exception::class)` للإشارة إلى أن الدالة التالية قد تطرح استثناء من النوع `Exception`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:185]

```
186:     fun encrypt(data: ByteArray, peerID: String): ByteArray {
```
> يعرّف الدالة العامة `encrypt` (التشفير) التي تأخذ `data` من النوع `ByteArray` و`peerID` من النوع `String` وتعيد `ByteArray`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:186]

```
187:         val encrypted = noiseService.encrypt(data, peerID)
```
> يعرّف المتغيّر الثابت `encrypted` (المشفَّر) ويسنده إلى نتيجة استدعاء `encrypt(data, peerID)` على `noiseService`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:187]

```
188:         if (encrypted == null) {
```
> يبدأ شرط `if` يتحقّق من كون `encrypted` يساوي `null`، ويفتح كتلته. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:188]

```
189:             throw Exception("Failed to encrypt for $peerID")
```
> يطرح استثناء `Exception` برسالة `"Failed to encrypt for $peerID"` متضمّنة `peerID`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:189]

```
190:         }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:190]

```
191:         return encrypted
```
> يعيد قيمة المتغيّر `encrypted`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:191]

```
192:     }
```
> إغلاق نطاق الدالة `encrypt`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:192]

```
193:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:193]

```
194:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:194]

```
195:      * Decrypt data from a specific peer using Noise transport encryption
```
> تعليق: «فُكَّ تشفير البيانات من نِدّ محدّد باستخدام تشفير النقل في Noise». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:195]

```
196:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:196]

```
197:     @Throws(Exception::class)
```
> يضع التعليق التوضيحي `@Throws(Exception::class)` للإشارة إلى أن الدالة التالية قد تطرح استثناء من النوع `Exception`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:197]

```
198:     fun decrypt(data: ByteArray, peerID: String): ByteArray {
```
> يعرّف الدالة العامة `decrypt` (فك التشفير) التي تأخذ `data` من النوع `ByteArray` و`peerID` من النوع `String` وتعيد `ByteArray`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:198]

```
199:         val decrypted = noiseService.decrypt(data, peerID)
```
> يعرّف المتغيّر الثابت `decrypted` (المفكوك تشفيره) ويسنده إلى نتيجة استدعاء `decrypt(data, peerID)` على `noiseService`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:199]

```
200:         if (decrypted == null) {
```
> يبدأ شرط `if` يتحقّق من كون `decrypted` يساوي `null`، ويفتح كتلته. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:200]

```
201:             throw Exception("Failed to decrypt from $peerID")
```
> يطرح استثناء `Exception` برسالة `"Failed to decrypt from $peerID"` متضمّنة `peerID`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:201]

```
202:         }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:202]

```
203:         return decrypted
```
> يعيد قيمة المتغيّر `decrypted`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:203]

```
204:     }
```
> إغلاق نطاق الدالة `decrypt`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:204]

```
205:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:205]

```
206:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:206]

```
207:      * Sign data using our static identity key
```
> تعليق: «وقّع البيانات باستخدام مفتاح هويتنا الثابت». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:207]

```
208:      * Note: This is now done at the packet level, not per-message
```
> تعليق: «ملاحظة: يتمّ هذا الآن على مستوى الحزمة، لا لكل رسالة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:208]

```
209:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:209]

```
210:     @Throws(Exception::class)
```
> يضع التعليق التوضيحي `@Throws(Exception::class)` للإشارة إلى أن الدالة التالية قد تطرح استثناء من النوع `Exception`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:210]

```
211:     fun sign(data: ByteArray): ByteArray {
```
> يعرّف الدالة العامة `sign` (التوقيع) التي تأخذ `data` من النوع `ByteArray` وتعيد `ByteArray`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:211]

```
212:         // Note: In Noise protocol, authentication is built into the handshake
```
> تعليق: «ملاحظة: في بروتوكول Noise، المصادقة مدمجة في المصافحة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:212]

```
213:         // For compatibility, we return empty signature
```
> تعليق: «من أجل التوافق، نعيد توقيعاً فارغاً». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:213]

```
214:         return ByteArray(0)
```
> يعيد مصفوفة بايتات فارغة بطول صفر عبر `ByteArray(0)`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:214]

```
215:     }
```
> إغلاق نطاق الدالة `sign`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:215]

```
216:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:216]

```
217:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:217]

```
218:      * Verify signature using peer's identity key
```
> تعليق: «تحقّق من التوقيع باستخدام مفتاح هوية النِّد». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:218]

```
219:      * Note: This is now done at the packet level, not per-message
```
> تعليق: «ملاحظة: يتمّ هذا الآن على مستوى الحزمة، لا لكل رسالة». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:219]

```
220:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:220]

```
221:     @Throws(Exception::class)
```
> يضع التعليق التوضيحي `@Throws(Exception::class)` للإشارة إلى أن الدالة التالية قد تطرح استثناء من النوع `Exception`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:221]

```
222:     fun verify(signature: ByteArray, data: ByteArray, peerID: String): Boolean {
```
> يعرّف الدالة العامة `verify` (التحقّق) التي تأخذ `signature` و`data` من النوع `ByteArray` و`peerID` من النوع `String` وتعيد `Boolean`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:222]

```
223:         // Note: In Noise protocol, authentication is built into the transport
```
> تعليق: «ملاحظة: في بروتوكول Noise، المصادقة مدمجة في طبقة النقل». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:223]

```
224:         // Messages are authenticated automatically when decrypted
```
> تعليق: «تُصادَق الرسائل تلقائياً عند فكّ تشفيرها». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:224]

```
225:         return hasEstablishedSession(peerID)
```
> يعيد نتيجة استدعاء `hasEstablishedSession(peerID)`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:225]

```
226:     }
```
> إغلاق نطاق الدالة `verify`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:226]

```
227:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:227]

```
228:     // MARK: - Noise Protocol Interface
```
> تعليق: «علامة قسم: واجهة بروتوكول Noise». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:228]

```
229:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:229]

```
230:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:230]

```
231:      * Check if we have an established Noise session with a peer
```
> تعليق: «تحقّق إن كانت لدينا جلسة Noise مؤسَّسة مع نِدّ». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:231]

```
232:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:232]

```
233:     fun hasEstablishedSession(peerID: String): Boolean {
```
> يعرّف الدالة العامة `hasEstablishedSession` (وجود جلسة مؤسَّسة) التي تأخذ `peerID` من النوع `String` وتعيد `Boolean`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:233]

```
234:         return noiseService.hasEstablishedSession(peerID)
```
> يعيد نتيجة استدعاء `hasEstablishedSession(peerID)` على `noiseService`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:234]

```
235:     }
```
> إغلاق نطاق الدالة `hasEstablishedSession`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:235]

```
236:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:236]

```
237:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:237]

```
238:      * Get session state for a peer (for UI state display)
```
> تعليق: «احصل على حالة الجلسة لنِدّ (لعرض حالة واجهة المستخدم)». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:238]

```
239:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:239]

```
240:     fun getSessionState(peerID: String): com.bitchat.android.noise.NoiseSession.NoiseSessionState {
```
> يعرّف الدالة العامة `getSessionState` (الحصول على حالة الجلسة) التي تأخذ `peerID` من النوع `String` وتعيد النوع `com.bitchat.android.noise.NoiseSession.NoiseSessionState`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:240]

```
241:         return noiseService.getSessionState(peerID)
```
> يعيد نتيجة استدعاء `getSessionState(peerID)` على `noiseService`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:241]

```
242:     }
```
> إغلاق نطاق الدالة `getSessionState`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:242]

```
243:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:243]

```
244:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:244]

```
245:      * Get encryption icon state for UI
```
> تعليق: «احصل على حالة أيقونة التشفير لواجهة المستخدم». [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:245]

```
246:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:246]

```
247:     fun shouldShowEncryptionIcon(peerID: String): Boolean {
```
> يعرّف الدالة العامة `shouldShowEncryptionIcon` (هل تُعرض أيقونة التشفير) التي تأخذ `peerID` من النوع `String` وتعيد `Boolean`، ويفتح نطاق جسمها. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:247]

```
248:         return hasEstablishedSession(peerID)
```
> يعيد نتيجة استدعاء `hasEstablishedSession(peerID)`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:248]

```
249:     }
```
> إغلاق نطاق الدالة `shouldShowEncryptionIcon`. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:249]

```
250:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/crypto/EncryptionService.kt:250]
