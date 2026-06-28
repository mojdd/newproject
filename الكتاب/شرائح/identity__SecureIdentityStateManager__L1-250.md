# شريحة — app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt (الأسطر 1–250)

```
1: package com.bitchat.android.identity
```
> يُعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.identity`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من حزمة أندرويد `android.content`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:3]

```
4: import android.content.SharedPreferences
```
> يستورد الصنف `SharedPreferences` (التفضيلات المشتركة) من `android.content`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:4]

```
5: import androidx.security.crypto.EncryptedSharedPreferences
```
> يستورد الصنف `EncryptedSharedPreferences` (التفضيلات المشتركة المشفّرة) من مكتبة `androidx.security.crypto`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:5]

```
6: import androidx.security.crypto.MasterKey
```
> يستورد الصنف `MasterKey` (المفتاح الرئيسي) من مكتبة `androidx.security.crypto`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:6]

```
7: import java.security.MessageDigest
```
> يستورد الصنف `MessageDigest` (هاضِم الرسالة) من حزمة جافا الأمنية `java.security`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:7]

```
8: import android.util.Base64
```
> يستورد الصنف `Base64` (الترميز بأساس ٦٤) من `android.util`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:8]

```
9: import android.util.Log
```
> يستورد الصنف `Log` (السجلّ) من `android.util`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:9]

```
10: import com.bitchat.android.util.hexEncodedString
```
> يستورد الدالة الموسّعة `hexEncodedString` (السلسلة المرمَّزة ستّ عشرياً) من حزمة المشروع `com.bitchat.android.util`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:10]

```
11: import androidx.core.content.edit
```
> يستورد الدالة الموسّعة `edit` (التحرير) من `androidx.core.content`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:11]

```
12: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:12]

```
13: /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:13]

```
14:  * Manages persistent identity storage and peer ID rotation - 100% compatible with iOS implementation
```
> تعليق: «يدير تخزين الهوية الدائم وتدوير معرّف النِّد — متوافق ١٠٠٪ مع تطبيق iOS». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:14]

```
15:  * 
```
> تعليق: سطر فارغ داخل كتلة التوثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:15]

```
16:  * Handles:
```
> تعليق: «يتعامل مع:». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:16]

```
17:  * - Static identity key persistence across app sessions
```
> تعليق: «- استمرار مفتاح الهوية الثابت عبر جلسات التطبيق». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:17]

```
18:  * - Secure storage using Android EncryptedSharedPreferences
```
> تعليق: «- تخزين آمن باستخدام EncryptedSharedPreferences في أندرويد». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:18]

```
19:  * - Fingerprint calculation and identity validation
```
> تعليق: «- حساب البصمة والتحقق من صحة الهوية». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:19]

```
20:  */
```
> تعليق توثيقي: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:20]

```
21: class SecureIdentityStateManager(private val context: Context) {
```
> يُعرّف الصنف `SecureIdentityStateManager` (مدير حالة الهوية الآمنة) الذي يأخذ في بانيه معاملاً خاصاً `context` من نوع `Context` ويفتح جسد الصنف. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:21]

```
22:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:22]

```
23:     companion object {
```
> يبدأ تعريف الكائن الرفيق (companion object) المرتبط بالصنف. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:23]

```
24:         private const val TAG = "SecureIdentityStateManager"
```
> يُعرّف الثابت الخاص `TAG` (الوسم) بقيمة نصية حرفية `"SecureIdentityStateManager"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:24]

```
25:         private const val PREFS_NAME = "bitchat_identity"
```
> يُعرّف الثابت الخاص `PREFS_NAME` (اسم التفضيلات) بقيمة نصية حرفية `"bitchat_identity"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:25]

```
26:         private const val KEY_STATIC_PRIVATE_KEY = "static_private_key"
```
> يُعرّف الثابت الخاص `KEY_STATIC_PRIVATE_KEY` (مفتاح المفتاح الخاص الثابت) بقيمة نصية حرفية `"static_private_key"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:26]

```
27:         private const val KEY_STATIC_PUBLIC_KEY = "static_public_key"
```
> يُعرّف الثابت الخاص `KEY_STATIC_PUBLIC_KEY` (مفتاح المفتاح العام الثابت) بقيمة نصية حرفية `"static_public_key"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:27]

```
28:         private const val KEY_SIGNING_PRIVATE_KEY = "signing_private_key"
```
> يُعرّف الثابت الخاص `KEY_SIGNING_PRIVATE_KEY` (مفتاح مفتاح التوقيع الخاص) بقيمة نصية حرفية `"signing_private_key"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:28]

```
29:         private const val KEY_SIGNING_PUBLIC_KEY = "signing_public_key"
```
> يُعرّف الثابت الخاص `KEY_SIGNING_PUBLIC_KEY` (مفتاح مفتاح التوقيع العام) بقيمة نصية حرفية `"signing_public_key"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:29]

```
30:         private const val KEY_VERIFIED_FINGERPRINTS = "verified_fingerprints"
```
> يُعرّف الثابت الخاص `KEY_VERIFIED_FINGERPRINTS` (مفتاح البصمات المُوثّقة) بقيمة نصية حرفية `"verified_fingerprints"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:30]

```
31:         private const val KEY_CACHED_PEER_FINGERPRINTS = "cached_peer_fingerprints"
```
> يُعرّف الثابت الخاص `KEY_CACHED_PEER_FINGERPRINTS` (مفتاح بصمات النِّد المخزَّنة مؤقتاً) بقيمة نصية حرفية `"cached_peer_fingerprints"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:31]

```
32:         private const val KEY_CACHED_PEER_NOISE_KEYS = "cached_peer_noise_keys"
```
> يُعرّف الثابت الخاص `KEY_CACHED_PEER_NOISE_KEYS` (مفتاح مفاتيح Noise للنِّد المخزَّنة مؤقتاً) بقيمة نصية حرفية `"cached_peer_noise_keys"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:32]

```
33:         private const val KEY_CACHED_NOISE_FINGERPRINTS = "cached_noise_fingerprints"
```
> يُعرّف الثابت الخاص `KEY_CACHED_NOISE_FINGERPRINTS` (مفتاح بصمات Noise المخزَّنة مؤقتاً) بقيمة نصية حرفية `"cached_noise_fingerprints"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:33]

```
34:         private const val KEY_CACHED_FINGERPRINT_NICKNAMES = "cached_fingerprint_nicknames"
```
> يُعرّف الثابت الخاص `KEY_CACHED_FINGERPRINT_NICKNAMES` (مفتاح ألقاب البصمات المخزَّنة مؤقتاً) بقيمة نصية حرفية `"cached_fingerprint_nicknames"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:34]

```
35:     }
```
> إغلاق نطاق الكائن الرفيق (companion object). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:35]

```
36:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:36]

```
37:     private val prefs: SharedPreferences
```
> يُعرّف الحقل الخاص `prefs` (التفضيلات) من نوع `SharedPreferences` دون إسناد قيمة مباشرة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:37]

```
38:     private val lock = Any()
```
> يُعرّف الحقل الخاص `lock` (القفل) ويُسنِد إليه كائناً جديداً ناتجاً عن استدعاء `Any()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:38]

```
39:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:39]

```
40:     init {
```
> يبدأ كتلة التهيئة (init) التي تُنفَّذ عند إنشاء كائن الصنف. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:40]

```
41:         // Create master key for encryption
```
> تعليق: «أنشئ المفتاح الرئيسي للتشفير». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:41]

```
42:         val masterKey = MasterKey.Builder(context, MasterKey.DEFAULT_MASTER_KEY_ALIAS)
```
> يُعرّف المتغيّر `masterKey` (المفتاح الرئيسي) ويبدأ بناءه عبر `MasterKey.Builder` مع تمرير `context` والاسم البديل الافتراضي `MasterKey.DEFAULT_MASTER_KEY_ALIAS`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:42]

```
43:             .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
```
> يستدعي `setKeyScheme` على البانِي لتعيين مخطط المفتاح إلى `MasterKey.KeyScheme.AES256_GCM`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:43]

```
44:             .build()
```
> يستدعي `build()` لإنهاء بناء كائن المفتاح الرئيسي. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:44]

```
45:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:45]

```
46:         // Create encrypted shared preferences
```
> تعليق: «أنشئ التفضيلات المشتركة المشفّرة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:46]

```
47:         prefs = EncryptedSharedPreferences.create(
```
> يُسنِد إلى الحقل `prefs` ناتج استدعاء الدالة `EncryptedSharedPreferences.create` ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:47]

```
48:             context,
```
> يمرّر `context` كمعامل أول للدالة `create`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:48]

```
49:             PREFS_NAME,
```
> يمرّر الثابت `PREFS_NAME` كمعامل ثانٍ (اسم ملف التفضيلات). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:49]

```
50:             masterKey,
```
> يمرّر المتغيّر `masterKey` كمعامل ثالث (المفتاح الرئيسي للتشفير). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:50]

```
51:             EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
```
> يمرّر مخطط تشفير المفاتيح `EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV` كمعامل رابع. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:51]

```
52:             EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
```
> يمرّر مخطط تشفير القيم `EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM` كمعامل خامس. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:52]

```
53:         )
```
> إغلاق نطاق قائمة معاملات استدعاء `create`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:53]

```
54:     }
```
> إغلاق نطاق كتلة التهيئة (init). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:54]

```
55:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:55]

```
56:     // MARK: - Static Key Management
```
> تعليق: علامة تقسيم «MARK: - إدارة المفتاح الثابت». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:56]

```
57:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:57]

```
58:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:58]

```
59:      * Load saved static key pair
```
> تعليق: «حمِّل زوج المفتاح الثابت المحفوظ». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:59]

```
60:      * Returns (privateKey, publicKey) or null if none exists
```
> تعليق: «يعيد (المفتاح الخاص، المفتاح العام) أو null إن لم يوجد». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:60]

```
61:      */
```
> تعليق توثيقي: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:61]

```
62:     fun loadStaticKey(): Pair<ByteArray, ByteArray>? {
```
> يُعرّف الدالة `loadStaticKey` (تحميل المفتاح الثابت) التي تعيد زوجاً `Pair` من مصفوفتي بايت `ByteArray` أو قيمة فارغة (nullable). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:62]

```
63:         return try {
```
> يبدأ عبارة الإعادة بكتلة `try` (محاولة) ويعيد ناتجها. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:63]

```
64:             val privateKeyString = prefs.getString(KEY_STATIC_PRIVATE_KEY, null)
```
> يُعرّف المتغيّر `privateKeyString` (سلسلة المفتاح الخاص) ويُسنِد إليه ناتج `prefs.getString` بالمفتاح `KEY_STATIC_PRIVATE_KEY` وقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:64]

```
65:             val publicKeyString = prefs.getString(KEY_STATIC_PUBLIC_KEY, null)
```
> يُعرّف المتغيّر `publicKeyString` (سلسلة المفتاح العام) ويُسنِد إليه ناتج `prefs.getString` بالمفتاح `KEY_STATIC_PUBLIC_KEY` وقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:65]

```
66:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:66]

```
67:             if (privateKeyString != null && publicKeyString != null) {
```
> يفتح شرطاً `if` يتحقق أن كلّاً من `privateKeyString` و`publicKeyString` ليس فارغاً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:67]

```
68:                 val privateKey = android.util.Base64.decode(privateKeyString, android.util.Base64.DEFAULT)
```
> يُعرّف المتغيّر `privateKey` (المفتاح الخاص) ويُسنِد إليه فكّ ترميز `privateKeyString` عبر `Base64.decode` بنمط `Base64.DEFAULT`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:68]

```
69:                 val publicKey = android.util.Base64.decode(publicKeyString, android.util.Base64.DEFAULT)
```
> يُعرّف المتغيّر `publicKey` (المفتاح العام) ويُسنِد إليه فكّ ترميز `publicKeyString` عبر `Base64.decode` بنمط `Base64.DEFAULT`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:69]

```
70:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:70]

```
71:                 // Validate key sizes
```
> تعليق: «تحقّق من أحجام المفاتيح». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:71]

```
72:                 if (privateKey.size == 32 && publicKey.size == 32) {
```
> يفتح شرطاً `if` يتحقق أن حجم `privateKey` يساوي ٣٢ وحجم `publicKey` يساوي ٣٢ بايتاً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:72]

```
73:                     Log.d(TAG, "Loaded static identity key from secure storage")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح بالوسم `TAG` ونصها «Loaded static identity key from secure storage» (حُمِّل مفتاح الهوية الثابت من التخزين الآمن). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:73]

```
74:                     Pair(privateKey, publicKey)
```
> ينتج الزوج `Pair(privateKey, publicKey)` كقيمة كتلة الشرط. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:74]

```
75:                 } else {
```
> يغلق كتلة الشرط الصحيح ويفتح كتلة `else` (وإلا). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:75]

```
76:                     Log.w(TAG, "Invalid key sizes in storage, returning null")
```
> يستدعي `Log.w` لتسجيل تحذير بالوسم `TAG` ونصه «Invalid key sizes in storage, returning null» (أحجام مفاتيح غير صالحة في التخزين، تُعاد null). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:76]

```
77:                     null
```
> ينتج القيمة `null` كقيمة كتلة `else`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:77]

```
78:                 }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:78]

```
79:             } else {
```
> يغلق كتلة الشرط الخارجي الصحيح ويفتح كتلة `else` الخارجية. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:79]

```
80:                 Log.d(TAG, "No static identity key found in storage")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح بالوسم `TAG` ونصها «No static identity key found in storage» (لم يُعثر على مفتاح هوية ثابت في التخزين). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:80]

```
81:                 null
```
> ينتج القيمة `null` كقيمة كتلة `else` الخارجية. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:81]

```
82:             }
```
> إغلاق نطاق كتلة `else` الخارجية. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:82]

```
83:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:83]

```
84:             Log.e(TAG, "Failed to load static key: ${e.message}")
```
> يستدعي `Log.e` لتسجيل خطأ بالوسم `TAG` ونصه «Failed to load static key: » متبوعاً برسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:84]

```
85:             null
```
> ينتج القيمة `null` كقيمة كتلة `catch`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:85]

```
86:         }
```
> إغلاق نطاق كتلة `try`/`catch`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:86]

```
87:     }
```
> إغلاق نطاق الدالة `loadStaticKey`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:87]

```
88:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:88]

```
89:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:89]

```
90:      * Save static key pair to secure storage
```
> تعليق: «احفظ زوج المفتاح الثابت في التخزين الآمن». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:90]

```
91:      */
```
> تعليق توثيقي: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:91]

```
92:     fun saveStaticKey(privateKey: ByteArray, publicKey: ByteArray) {
```
> يُعرّف الدالة `saveStaticKey` (حفظ المفتاح الثابت) التي تأخذ `privateKey` و`publicKey` من نوع `ByteArray` ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:92]

```
93:         try {
```
> يفتح كتلة `try` (محاولة). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:93]

```
94:             // Validate key sizes
```
> تعليق: «تحقّق من أحجام المفاتيح». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:94]

```
95:             if (privateKey.size != 32 || publicKey.size != 32) {
```
> يفتح شرطاً `if` يتحقق أن حجم `privateKey` لا يساوي ٣٢ أو حجم `publicKey` لا يساوي ٣٢ بايتاً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:95]

```
96:                 throw IllegalArgumentException("Invalid key sizes: private=${privateKey.size}, public=${publicKey.size}")
```
> يرمي استثناء `IllegalArgumentException` (وسيط غير صالح) برسالة تتضمن «Invalid key sizes: private=» وحجم `privateKey` و«public=» وحجم `publicKey`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:96]

```
97:             }
```
> إغلاق نطاق شرط `if`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:97]

```
98:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:98]

```
99:             val privateKeyString = android.util.Base64.encodeToString(privateKey, android.util.Base64.DEFAULT)
```
> يُعرّف المتغيّر `privateKeyString` ويُسنِد إليه ترميز `privateKey` نصياً عبر `Base64.encodeToString` بنمط `Base64.DEFAULT`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:99]

```
100:             val publicKeyString = android.util.Base64.encodeToString(publicKey, android.util.Base64.DEFAULT)
```
> يُعرّف المتغيّر `publicKeyString` ويُسنِد إليه ترميز `publicKey` نصياً عبر `Base64.encodeToString` بنمط `Base64.DEFAULT`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:100]

```
101:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:101]

```
102:             prefs.edit()
```
> يستدعي `prefs.edit()` لبدء محرّر للتفضيلات. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:102]

```
103:                 .putString(KEY_STATIC_PRIVATE_KEY, privateKeyString)
```
> يستدعي `putString` على المحرّر لتخزين `privateKeyString` تحت المفتاح `KEY_STATIC_PRIVATE_KEY`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:103]

```
104:                 .putString(KEY_STATIC_PUBLIC_KEY, publicKeyString)
```
> يستدعي `putString` على المحرّر لتخزين `publicKeyString` تحت المفتاح `KEY_STATIC_PUBLIC_KEY`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:104]

```
105:                 .apply()
```
> يستدعي `apply()` لتطبيق تغييرات المحرّر بشكل غير متزامن. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:105]

```
106:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:106]

```
107:             Log.d(TAG, "Saved static identity key to secure storage")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح بالوسم `TAG` ونصها «Saved static identity key to secure storage» (حُفِظ مفتاح الهوية الثابت في التخزين الآمن). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:107]

```
108:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:108]

```
109:             Log.e(TAG, "Failed to save static key: ${e.message}")
```
> يستدعي `Log.e` لتسجيل خطأ بالوسم `TAG` ونصه «Failed to save static key: » متبوعاً برسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:109]

```
110:             throw e
```
> يعيد رمي الاستثناء `e`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:110]

```
111:         }
```
> إغلاق نطاق كتلة `try`/`catch`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:111]

```
112:     }
```
> إغلاق نطاق الدالة `saveStaticKey`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:112]

```
113: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:113]

```
114:     // MARK: - Signing Key Management
```
> تعليق: علامة تقسيم «MARK: - إدارة مفتاح التوقيع». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:114]

```
115: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:115]

```
116:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:116]

```
117:      * Load saved signing key pair
```
> تعليق: «حمِّل زوج مفتاح التوقيع المحفوظ». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:117]

```
118:      * Returns (privateKey, publicKey) or null if none exists
```
> تعليق: «يعيد (المفتاح الخاص، المفتاح العام) أو null إن لم يوجد». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:118]

```
119:      */
```
> تعليق توثيقي: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:119]

```
120:     fun loadSigningKey(): Pair<ByteArray, ByteArray>? {
```
> يُعرّف الدالة `loadSigningKey` (تحميل مفتاح التوقيع) التي تعيد زوجاً `Pair` من مصفوفتي بايت أو قيمة فارغة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:120]

```
121:         return try {
```
> يبدأ عبارة الإعادة بكتلة `try` ويعيد ناتجها. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:121]

```
122:             val privateKeyString = prefs.getString(KEY_SIGNING_PRIVATE_KEY, null)
```
> يُعرّف المتغيّر `privateKeyString` ويُسنِد إليه ناتج `prefs.getString` بالمفتاح `KEY_SIGNING_PRIVATE_KEY` وقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:122]

```
123:             val publicKeyString = prefs.getString(KEY_SIGNING_PUBLIC_KEY, null)
```
> يُعرّف المتغيّر `publicKeyString` ويُسنِد إليه ناتج `prefs.getString` بالمفتاح `KEY_SIGNING_PUBLIC_KEY` وقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:123]

```
124:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:124]

```
125:             if (privateKeyString != null && publicKeyString != null) {
```
> يفتح شرطاً `if` يتحقق أن كلّاً من `privateKeyString` و`publicKeyString` ليس فارغاً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:125]

```
126:                 val privateKey = android.util.Base64.decode(privateKeyString, android.util.Base64.DEFAULT)
```
> يُعرّف المتغيّر `privateKey` ويُسنِد إليه فكّ ترميز `privateKeyString` عبر `Base64.decode` بنمط `Base64.DEFAULT`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:126]

```
127:                 val publicKey = android.util.Base64.decode(publicKeyString, android.util.Base64.DEFAULT)
```
> يُعرّف المتغيّر `publicKey` ويُسنِد إليه فكّ ترميز `publicKeyString` عبر `Base64.decode` بنمط `Base64.DEFAULT`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:127]

```
128:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:128]

```
129:                 // Validate key sizes
```
> تعليق: «تحقّق من أحجام المفاتيح». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:129]

```
130:                 if (privateKey.size == 32 && publicKey.size == 32) {
```
> يفتح شرطاً `if` يتحقق أن حجم `privateKey` يساوي ٣٢ وحجم `publicKey` يساوي ٣٢ بايتاً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:130]

```
131:                     Log.d(TAG, "Loaded Ed25519 signing key from secure storage")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح بالوسم `TAG` ونصها «Loaded Ed25519 signing key from secure storage» (حُمِّل مفتاح توقيع Ed25519 من التخزين الآمن). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:131]

```
132:                     Pair(privateKey, publicKey)
```
> ينتج الزوج `Pair(privateKey, publicKey)` كقيمة كتلة الشرط. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:132]

```
133:                 } else {
```
> يغلق كتلة الشرط الصحيح ويفتح كتلة `else`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:133]

```
134:                     Log.w(TAG, "Invalid signing key sizes in storage, returning null")
```
> يستدعي `Log.w` لتسجيل تحذير بالوسم `TAG` ونصه «Invalid signing key sizes in storage, returning null» (أحجام مفاتيح توقيع غير صالحة في التخزين، تُعاد null). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:134]

```
135:                     null
```
> ينتج القيمة `null` كقيمة كتلة `else`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:135]

```
136:                 }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:136]

```
137:             } else {
```
> يغلق كتلة الشرط الخارجي الصحيح ويفتح كتلة `else` الخارجية. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:137]

```
138:                 Log.d(TAG, "No Ed25519 signing key found in storage")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح بالوسم `TAG` ونصها «No Ed25519 signing key found in storage» (لم يُعثر على مفتاح توقيع Ed25519 في التخزين). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:138]

```
139:                 null
```
> ينتج القيمة `null` كقيمة كتلة `else` الخارجية. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:139]

```
140:             }
```
> إغلاق نطاق كتلة `else` الخارجية. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:140]

```
141:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:141]

```
142:             Log.e(TAG, "Failed to load signing key: ${e.message}")
```
> يستدعي `Log.e` لتسجيل خطأ بالوسم `TAG` ونصه «Failed to load signing key: » متبوعاً برسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:142]

```
143:             null
```
> ينتج القيمة `null` كقيمة كتلة `catch`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:143]

```
144:         }
```
> إغلاق نطاق كتلة `try`/`catch`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:144]

```
145:     }
```
> إغلاق نطاق الدالة `loadSigningKey`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:145]

```
146: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:146]

```
147:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:147]

```
148:      * Save signing key pair to secure storage
```
> تعليق: «احفظ زوج مفتاح التوقيع في التخزين الآمن». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:148]

```
149:      */
```
> تعليق توثيقي: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:149]

```
150:     fun saveSigningKey(privateKey: ByteArray, publicKey: ByteArray) {
```
> يُعرّف الدالة `saveSigningKey` (حفظ مفتاح التوقيع) التي تأخذ `privateKey` و`publicKey` من نوع `ByteArray` ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:150]

```
151:         try {
```
> يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:151]

```
152:             // Validate key sizes
```
> تعليق: «تحقّق من أحجام المفاتيح». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:152]

```
153:             if (privateKey.size != 32 || publicKey.size != 32) {
```
> يفتح شرطاً `if` يتحقق أن حجم `privateKey` لا يساوي ٣٢ أو حجم `publicKey` لا يساوي ٣٢ بايتاً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:153]

```
154:                 throw IllegalArgumentException("Invalid signing key sizes: private=${privateKey.size}, public=${publicKey.size}")
```
> يرمي استثناء `IllegalArgumentException` برسالة تتضمن «Invalid signing key sizes: private=» وحجم `privateKey` و«public=» وحجم `publicKey`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:154]

```
155:             }
```
> إغلاق نطاق شرط `if`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:155]

```
156:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:156]

```
157:             val privateKeyString = android.util.Base64.encodeToString(privateKey, android.util.Base64.DEFAULT)
```
> يُعرّف المتغيّر `privateKeyString` ويُسنِد إليه ترميز `privateKey` نصياً عبر `Base64.encodeToString` بنمط `Base64.DEFAULT`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:157]

```
158:             val publicKeyString = android.util.Base64.encodeToString(publicKey, android.util.Base64.DEFAULT)
```
> يُعرّف المتغيّر `publicKeyString` ويُسنِد إليه ترميز `publicKey` نصياً عبر `Base64.encodeToString` بنمط `Base64.DEFAULT`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:158]

```
159:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:159]

```
160:             prefs.edit()
```
> يستدعي `prefs.edit()` لبدء محرّر للتفضيلات. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:160]

```
161:                 .putString(KEY_SIGNING_PRIVATE_KEY, privateKeyString)
```
> يستدعي `putString` على المحرّر لتخزين `privateKeyString` تحت المفتاح `KEY_SIGNING_PRIVATE_KEY`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:161]

```
162:                 .putString(KEY_SIGNING_PUBLIC_KEY, publicKeyString)
```
> يستدعي `putString` على المحرّر لتخزين `publicKeyString` تحت المفتاح `KEY_SIGNING_PUBLIC_KEY`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:162]

```
163:                 .apply()
```
> يستدعي `apply()` لتطبيق تغييرات المحرّر بشكل غير متزامن. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:163]

```
164:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:164]

```
165:             Log.d(TAG, "Saved Ed25519 signing key to secure storage")
```
> يستدعي `Log.d` لتسجيل رسالة تصحيح بالوسم `TAG` ونصها «Saved Ed25519 signing key to secure storage» (حُفِظ مفتاح توقيع Ed25519 في التخزين الآمن). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:165]

```
166:         } catch (e: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:166]

```
167:             Log.e(TAG, "Failed to save signing key: ${e.message}")
```
> يستدعي `Log.e` لتسجيل خطأ بالوسم `TAG` ونصه «Failed to save signing key: » متبوعاً برسالة الاستثناء `e.message`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:167]

```
168:             throw e
```
> يعيد رمي الاستثناء `e`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:168]

```
169:         }
```
> إغلاق نطاق كتلة `try`/`catch`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:169]

```
170:     }
```
> إغلاق نطاق الدالة `saveSigningKey`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:170]

```
171:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:171]

```
172:     // MARK: - Fingerprint Generation
```
> تعليق: علامة تقسيم «MARK: - توليد البصمة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:172]

```
173:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:173]

```
174:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:174]

```
175:      * Generate fingerprint from public key (SHA-256 hash)
```
> تعليق: «ولِّد البصمة من المفتاح العام (تجزئة SHA-256)». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:175]

```
176:      */
```
> تعليق توثيقي: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:176]

```
177:     fun generateFingerprint(publicKeyData: ByteArray): String {
```
> يُعرّف الدالة `generateFingerprint` (توليد البصمة) التي تأخذ `publicKeyData` (بيانات المفتاح العام) من نوع `ByteArray` وتعيد سلسلة `String`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:177]

```
178:         val digest = MessageDigest.getInstance("SHA-256")
```
> يُعرّف المتغيّر `digest` (الهاضِم) ويُسنِد إليه نسخة من `MessageDigest` لخوارزمية `"SHA-256"`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:178]

```
179:         val hash = digest.digest(publicKeyData)
```
> يُعرّف المتغيّر `hash` (التجزئة) ويُسنِد إليه ناتج `digest.digest(publicKeyData)`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:179]

```
180:         return hash.hexEncodedString()
```
> يعيد ناتج استدعاء الدالة الموسّعة `hexEncodedString` على `hash` (تمثيل ستّ عشري نصي). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:180]

```
181:     }
```
> إغلاق نطاق الدالة `generateFingerprint`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:181]

```
182:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:182]

```
183:     /**
```
> تعليق توثيقي: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:183]

```
184:      * Validate fingerprint format
```
> تعليق: «تحقّق من صيغة البصمة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:184]

```
185:      */
```
> تعليق توثيقي: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:185]

```
186:     fun isValidFingerprint(fingerprint: String): Boolean {
```
> يُعرّف الدالة `isValidFingerprint` (هل البصمة صالحة) التي تأخذ `fingerprint` (البصمة) من نوع `String` وتعيد منطقياً `Boolean`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:186]

```
187:         // SHA-256 fingerprint should be 64 hex characters
```
> تعليق: «يجب أن تكون بصمة SHA-256 من ٦٤ حرفاً ستّ عشرياً». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:187]

```
188:         return fingerprint.matches(Regex("^[a-fA-F0-9]{64}$"))
```
> يعيد نتيجة مطابقة `fingerprint` للتعبير النمطي `Regex` الحرفي `"^[a-fA-F0-9]{64}$"` (٦٤ رمزاً ستّ عشرياً بالضبط). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:188]

```
189:     }
```
> إغلاق نطاق الدالة `isValidFingerprint`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:189]

```
190: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:190]

```
191:     // MARK: - Verified Fingerprints
```
> تعليق: علامة تقسيم «MARK: - البصمات المُوثّقة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:191]

```
192: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:192]

```
193:     fun getVerifiedFingerprints(): Set<String> {
```
> يُعرّف الدالة `getVerifiedFingerprints` (جلب البصمات المُوثّقة) التي تعيد مجموعة `Set` من سلاسل `String`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:193]

```
194:         return prefs.getStringSet(KEY_VERIFIED_FINGERPRINTS, emptySet())?.toSet() ?: emptySet()
```
> يعيد مجموعة السلاسل المخزّنة تحت `KEY_VERIFIED_FINGERPRINTS` (بقيمة افتراضية مجموعة فارغة) محوّلةً إلى مجموعة عبر `toSet()`، وإن كانت فارغة (null) أعاد مجموعة فارغة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:194]

```
195:     }
```
> إغلاق نطاق الدالة `getVerifiedFingerprints`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:195]

```
196: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:196]

```
197:     fun isVerifiedFingerprint(fingerprint: String): Boolean {
```
> يُعرّف الدالة `isVerifiedFingerprint` (هل البصمة موثّقة) التي تأخذ `fingerprint` من نوع `String` وتعيد `Boolean`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:197]

```
198:         return getVerifiedFingerprints().contains(fingerprint)
```
> يعيد ما إذا كانت مجموعة `getVerifiedFingerprints()` تحتوي `fingerprint`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:198]

```
199:     }
```
> إغلاق نطاق الدالة `isVerifiedFingerprint`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:199]

```
200: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:200]

```
201:     fun setVerifiedFingerprint(fingerprint: String, verified: Boolean) {
```
> يُعرّف الدالة `setVerifiedFingerprint` (تعيين توثيق البصمة) التي تأخذ `fingerprint` من نوع `String` و`verified` (موثّقة) من نوع `Boolean` ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:201]

```
202:         if (!isValidFingerprint(fingerprint)) return
```
> إن لم تكن `fingerprint` صالحة بحسب `isValidFingerprint` فإنه يعود من الدالة فوراً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:202]

```
203:         synchronized(lock) {
```
> يبدأ كتلة متزامنة `synchronized` على الكائن `lock`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:203]

```
204:             val current = prefs.getStringSet(KEY_VERIFIED_FINGERPRINTS, emptySet())?.toMutableSet() ?: mutableSetOf()
```
> يُعرّف المتغيّر `current` (الحالي) ويُسنِد إليه مجموعة السلاسل المخزّنة تحت `KEY_VERIFIED_FINGERPRINTS` محوّلةً إلى مجموعة قابلة للتعديل عبر `toMutableSet()`، وإن كانت فارغة (null) أُسنِدت مجموعة قابلة للتعديل فارغة `mutableSetOf()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:204]

```
205:             if (verified) {
```
> يفتح شرطاً `if` يتحقق من أن `verified` صحيح. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:205]

```
206:                 current.add(fingerprint)
```
> يضيف `fingerprint` إلى المجموعة `current`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:206]

```
207:             } else {
```
> يغلق كتلة الشرط الصحيح ويفتح كتلة `else`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:207]

```
208:                 current.remove(fingerprint)
```
> يحذف `fingerprint` من المجموعة `current`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:208]

```
209:             }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:209]

```
210:             prefs.edit { putStringSet(KEY_VERIFIED_FINGERPRINTS, current) }
```
> يستدعي `prefs.edit` بدالة لامبدا تخزّن المجموعة `current` تحت المفتاح `KEY_VERIFIED_FINGERPRINTS` عبر `putStringSet`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:210]

```
211:         }
```
> إغلاق نطاق الكتلة المتزامنة `synchronized`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:211]

```
212:     }
```
> إغلاق نطاق الدالة `setVerifiedFingerprint`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:212]

```
213: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:213]

```
214:     fun getCachedPeerFingerprint(peerID: String): String? {
```
> يُعرّف الدالة `getCachedPeerFingerprint` (جلب بصمة النِّد المخزَّنة مؤقتاً) التي تأخذ `peerID` (معرّف النِّد) من نوع `String` وتعيد سلسلة قد تكون فارغة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:214]

```
215:         val pid = peerID.lowercase()
```
> يُعرّف المتغيّر `pid` ويُسنِد إليه `peerID` بعد تحويله إلى حروف صغيرة عبر `lowercase()`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:215]

```
216:         // Reading is safe without lock for SharedPreferences, but synchronizing ensures memory visibility
```
> تعليق: «القراءة آمنة بلا قفل في SharedPreferences، لكن المزامنة تضمن رؤية الذاكرة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:216]

```
217:         // if we are paranoid, but SharedPreferences is generally thread-safe for reads.
```
> تعليق: «إن كنّا مفرطين في الحذر، لكن SharedPreferences آمنة للخيوط عموماً عند القراءة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:217]

```
218:         // However, to ensure we don't read a partial update (unlikely with SP), we can leave it.
```
> تعليق: «ومع ذلك، لضمان عدم قراءة تحديث جزئي (وهو غير محتمل مع SP)، يمكننا تركها». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:218]

```
219:         // The critical part is the write.
```
> تعليق: «الجزء الحرج هو الكتابة». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:219]

```
220:         val entries = prefs.getStringSet(KEY_CACHED_PEER_FINGERPRINTS, emptySet()) ?: return null
```
> يُعرّف المتغيّر `entries` (المدخلات) ويُسنِد إليه مجموعة السلاسل تحت `KEY_CACHED_PEER_FINGERPRINTS` (بقيمة افتراضية فارغة)، وإن كانت فارغة (null) أعاد `null` من الدالة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:220]

```
221:         val entry = entries.firstOrNull { it.startsWith("$pid:") } ?: return null
```
> يُعرّف المتغيّر `entry` (المدخل) ويُسنِد إليه أول عنصر في `entries` يبدأ بـ«$pid:» عبر `firstOrNull`، وإن لم يوجد أعاد `null` من الدالة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:221]

```
222:         return entry.substringAfter(':').takeIf { isValidFingerprint(it) }
```
> يعيد الجزء من `entry` بعد أول «:» (عبر `substringAfter`)، بشرط أن يكون بصمة صالحة بحسب `isValidFingerprint` وإلا أعاد `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:222]

```
223:     }
```
> إغلاق نطاق الدالة `getCachedPeerFingerprint`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:223]

```
224: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:224]

```
225:     fun cachePeerFingerprint(peerID: String, fingerprint: String) {
```
> يُعرّف الدالة `cachePeerFingerprint` (تخزين بصمة النِّد مؤقتاً) التي تأخذ `peerID` و`fingerprint` من نوع `String` ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:225]

```
226:         if (!isValidFingerprint(fingerprint)) return
```
> إن لم تكن `fingerprint` صالحة بحسب `isValidFingerprint` فإنه يعود من الدالة فوراً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:226]

```
227:         val pid = peerID.lowercase()
```
> يُعرّف المتغيّر `pid` ويُسنِد إليه `peerID` بعد تحويله إلى حروف صغيرة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:227]

```
228:         synchronized(lock) {
```
> يبدأ كتلة متزامنة `synchronized` على الكائن `lock`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:228]

```
229:             val current = prefs.getStringSet(KEY_CACHED_PEER_FINGERPRINTS, emptySet())?.toMutableSet() ?: mutableSetOf()
```
> يُعرّف المتغيّر `current` ويُسنِد إليه مجموعة السلاسل تحت `KEY_CACHED_PEER_FINGERPRINTS` محوّلةً إلى مجموعة قابلة للتعديل، وإن كانت فارغة أُسنِدت مجموعة قابلة للتعديل فارغة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:229]

```
230:             current.removeAll { it.startsWith("$pid:") }
```
> يحذف من `current` كل عنصر يبدأ بـ«$pid:» عبر `removeAll`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:230]

```
231:             current.add("$pid:$fingerprint")
```
> يضيف إلى `current` السلسلة المركّبة «$pid:$fingerprint». [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:231]

```
232:             prefs.edit { putStringSet(KEY_CACHED_PEER_FINGERPRINTS, current) }
```
> يستدعي `prefs.edit` بدالة لامبدا تخزّن المجموعة `current` تحت المفتاح `KEY_CACHED_PEER_FINGERPRINTS` عبر `putStringSet`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:232]

```
233:         }
```
> إغلاق نطاق الكتلة المتزامنة `synchronized`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:233]

```
234:     }
```
> إغلاق نطاق الدالة `cachePeerFingerprint`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:234]

```
235: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:235]

```
236:     fun getCachedNoiseKey(peerID: String): String? {
```
> يُعرّف الدالة `getCachedNoiseKey` (جلب مفتاح Noise المخزَّن مؤقتاً) التي تأخذ `peerID` من نوع `String` وتعيد سلسلة قد تكون فارغة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:236]

```
237:         val pid = peerID.lowercase()
```
> يُعرّف المتغيّر `pid` ويُسنِد إليه `peerID` بعد تحويله إلى حروف صغيرة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:237]

```
238:         val entries = prefs.getStringSet(KEY_CACHED_PEER_NOISE_KEYS, emptySet()) ?: return null
```
> يُعرّف المتغيّر `entries` ويُسنِد إليه مجموعة السلاسل تحت `KEY_CACHED_PEER_NOISE_KEYS` (بقيمة افتراضية فارغة)، وإن كانت فارغة (null) أعاد `null` من الدالة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:238]

```
239:         val entry = entries.firstOrNull { it.startsWith("$pid=") } ?: return null
```
> يُعرّف المتغيّر `entry` ويُسنِد إليه أول عنصر في `entries` يبدأ بـ«$pid=» عبر `firstOrNull`، وإن لم يوجد أعاد `null` من الدالة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:239]

```
240:         return entry.substringAfter('=').takeIf { it.matches(Regex("^[a-fA-F0-9]{64}$")) }
```
> يعيد الجزء من `entry` بعد أول «=» (عبر `substringAfter`)، بشرط أن يطابق التعبير النمطي `"^[a-fA-F0-9]{64}$"` (٦٤ رمزاً ستّ عشرياً) وإلا أعاد `null`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:240]

```
241:     }
```
> إغلاق نطاق الدالة `getCachedNoiseKey`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:241]

```
242: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:242]

```
243:     fun cachePeerNoiseKey(peerID: String, noiseKeyHex: String) {
```
> يُعرّف الدالة `cachePeerNoiseKey` (تخزين مفتاح Noise للنِّد مؤقتاً) التي تأخذ `peerID` و`noiseKeyHex` (مفتاح Noise ستّ عشري) من نوع `String` ولا تعيد قيمة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:243]

```
244:         if (!noiseKeyHex.matches(Regex("^[a-fA-F0-9]{64}$"))) return
```
> إن لم يطابق `noiseKeyHex` التعبير النمطي `"^[a-fA-F0-9]{64}$"` (٦٤ رمزاً ستّ عشرياً) فإنه يعود من الدالة فوراً. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:244]

```
245:         val pid = peerID.lowercase()
```
> يُعرّف المتغيّر `pid` ويُسنِد إليه `peerID` بعد تحويله إلى حروف صغيرة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:245]

```
246:         synchronized(lock) {
```
> يبدأ كتلة متزامنة `synchronized` على الكائن `lock`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:246]

```
247:             val current = prefs.getStringSet(KEY_CACHED_PEER_NOISE_KEYS, emptySet())?.toMutableSet() ?: mutableSetOf()
```
> يُعرّف المتغيّر `current` ويُسنِد إليه مجموعة السلاسل تحت `KEY_CACHED_PEER_NOISE_KEYS` محوّلةً إلى مجموعة قابلة للتعديل، وإن كانت فارغة أُسنِدت مجموعة قابلة للتعديل فارغة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:247]

```
248:             current.removeAll { it.startsWith("$pid=") }
```
> يحذف من `current` كل عنصر يبدأ بـ«$pid=» عبر `removeAll`. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:248]

```
249:             current.add("$pid=${noiseKeyHex.lowercase()}")
```
> يضيف إلى `current` السلسلة المركّبة «$pid=» متبوعةً بـ`noiseKeyHex` محوّلاً إلى حروف صغيرة. [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:249]

```
250:             prefs.edit { putStringSet(KEY_CACHED_PEER_NOISE_KEYS, current)
```
> يستدعي `prefs.edit` بدالة لامبدا تبدأ بتخزين المجموعة `current` تحت المفتاح `KEY_CACHED_PEER_NOISE_KEYS` عبر `putStringSet` (دون إغلاق اللامبدا في هذا السطر). [app/src/main/java/com/bitchat/android/identity/SecureIdentityStateManager.kt:250]
