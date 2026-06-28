# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt (الأسطر 1–250)

```
1: package com.bitchat.android.noise
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.noise`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف `Log` من حزمة أندرويد لتسجيل الرسائل. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:3]

```
4: import java.security.MessageDigest
```
> يستورد الصنف `MessageDigest` من مكتبة الأمان في جافا لحساب البصمات. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:4]

```
5: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف `ConcurrentHashMap` وهو خريطة (ConcurrentHashMap) آمنة عند الاستخدام المتزامن. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:5]

```
6: import javax.crypto.Cipher
```
> يستورد الصنف `Cipher` المستخدم لعمليات التشفير وفك التشفير. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:6]

```
7: import javax.crypto.SecretKeyFactory
```
> يستورد الصنف `SecretKeyFactory` المستخدم لتوليد المفاتيح السرية. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:7]

```
8: import javax.crypto.spec.GCMParameterSpec
```
> يستورد الصنف `GCMParameterSpec` لتحديد معاملات نمط GCM. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:8]

```
9: import javax.crypto.spec.PBEKeySpec
```
> يستورد الصنف `PBEKeySpec` لتحديد مواصفات مفتاح مشتق من كلمة مرور. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:9]

```
10: import javax.crypto.spec.SecretKeySpec
```
> يستورد الصنف `SecretKeySpec` لتمثيل مفتاح سرّي من مصفوفة بايتات. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:11]

```
12: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:12]

```
13:  * Channel encryption for password-protected channels - 100% compatible with iOS implementation
```
> تعليق: تشفير القنوات للقنوات المحمية بكلمة مرور — متوافق ١٠٠٪ مع تنفيذ iOS. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:13]

```
14:  * 
```
> تعليق: سطر فارغ داخل كتلة التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:14]

```
15:  * Uses PBKDF2 key derivation with channel name as salt and AES-256-GCM for encryption.
```
> تعليق: يستخدم اشتقاق المفتاح PBKDF2 مع اسم القناة كملح (salt) و AES-256-GCM للتشفير. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:15]

```
16:  * This is separate from Noise sessions and used for group channels with shared passwords.
```
> تعليق: هذا منفصل عن جلسات Noise ويُستخدم لقنوات المجموعات ذات كلمات المرور المشتركة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:16]

```
17:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:17]

```
18: class NoiseChannelEncryption {
```
> يعرّف الصنف (NoiseChannelEncryption) «تشفير قناة Noise» ويفتح نطاقه. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:18]

```
19:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:19]

```
20:     companion object {
```
> يعرّف كائناً مرافقاً (companion object) ويفتح نطاقه لحمل الأعضاء الثابتة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:20]

```
21:         private const val TAG = "NoiseChannelEncryption"
```
> يعرّف ثابتاً خاصاً (TAG) «الوسم» بقيمة نصية حرفية `"NoiseChannelEncryption"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:21]

```
22:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:22]

```
23:         // PBKDF2 parameters (same as iOS)
```
> تعليق: معاملات PBKDF2 (نفسها كما في iOS). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:23]

```
24:         private const val PBKDF2_ITERATIONS = 100000
```
> يعرّف ثابتاً خاصاً (PBKDF2_ITERATIONS) «عدد تكرارات PBKDF2» بقيمة حرفية `100000`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:24]

```
25:         private const val KEY_LENGTH = 256 // 256-bit AES key
```
> يعرّف ثابتاً خاصاً (KEY_LENGTH) «طول المفتاح» بقيمة حرفية `256`، مع تعليق: مفتاح AES بطول 256 بت. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:25]

```
26:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:26]

```
27:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:27]

```
28:     // Channel keys storage (channelName -> AES key)
```
> تعليق: تخزين مفاتيح القنوات (اسم القناة -> مفتاح AES). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:28]

```
29:     private val channelKeys = ConcurrentHashMap<String, SecretKeySpec>()
```
> يعرّف متغيّراً ثابتاً خاصاً (channelKeys) «مفاتيح القنوات» مهيّأً بخريطة `ConcurrentHashMap` من نص إلى `SecretKeySpec`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:29]

```
30:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:30]

```
31:     // Channel passwords (for rekey operations)
```
> تعليق: كلمات مرور القنوات (لعمليات إعادة توليد المفتاح). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:31]

```
32:     private val channelPasswords = ConcurrentHashMap<String, String>()
```
> يعرّف متغيّراً ثابتاً خاصاً (channelPasswords) «كلمات مرور القنوات» مهيّأً بخريطة `ConcurrentHashMap` من نص إلى نص. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:32]

```
33:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:33]

```
34:     // MARK: - Channel Password Management
```
> تعليق: علامة قسم — إدارة كلمات مرور القنوات. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:34]

```
35:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:35]

```
36:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:36]

```
37:      * Set password for a channel and derive encryption key
```
> تعليق: ضبط كلمة المرور لقناة واشتقاق مفتاح التشفير. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:37]

```
38:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:38]

```
39:     fun setChannelPassword(password: String, channel: String) {
```
> يعرّف الدالة (setChannelPassword) «ضبط كلمة مرور القناة» التي تأخذ `password` نصاً و `channel` نصاً ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:39]

```
40:         try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:40]

```
41:             if (password.isEmpty()) {
```
> يتحقق شرطاً إن كانت كلمة المرور فارغة ويفتح نطاق الشرط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:41]

```
42:                 Log.w(TAG, "Empty password provided for channel $channel")
```
> يسجّل تحذيراً عبر `Log.w` بالوسم وبالنص `"Empty password provided for channel $channel"` متضمّناً اسم القناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:42]

```
43:                 return
```
> ينهي تنفيذ الدالة بإرجاع فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:43]

```
44:             }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:44]

```
45:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:45]

```
46:             // Derive key from password using PBKDF2 (same as iOS)
```
> تعليق: اشتقاق المفتاح من كلمة المرور باستخدام PBKDF2 (نفسه كما في iOS). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:46]

```
47:             val key = deriveChannelKey(password, channel)
```
> يعرّف متغيّراً ثابتاً (key) «المفتاح» بقيمة ناتج استدعاء الدالة `deriveChannelKey` بكلمة المرور والقناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:47]

```
48:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:48]

```
49:             // Store key and password
```
> تعليق: تخزين المفتاح وكلمة المرور. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:49]

```
50:             channelKeys[channel] = key
```
> يخزّن المفتاح في خريطة `channelKeys` تحت مفتاح اسم القناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:50]

```
51:             channelPasswords[channel] = password
```
> يخزّن كلمة المرور في خريطة `channelPasswords` تحت مفتاح اسم القناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:51]

```
52:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:52]

```
53:             Log.d(TAG, "Set password for channel $channel")
```
> يسجّل رسالة تصحيح عبر `Log.d` بالوسم وبالنص `"Set password for channel $channel"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:53]

```
54:         } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويبدأ كتلة الالتقاط (catch) لاستثناء `Exception` باسم `e`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:54]

```
55:             Log.e(TAG, "Failed to set password for channel $channel: ${e.message}")
```
> يسجّل خطأً عبر `Log.e` بالوسم وبالنص `"Failed to set password for channel $channel: ${e.message}"` متضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:55]

```
56:         }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:56]

```
57:     }
```
> إغلاق نطاق الدالة `setChannelPassword`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:57]

```
58:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:58]

```
59:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:59]

```
60:      * Remove password for a channel
```
> تعليق: إزالة كلمة المرور لقناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:60]

```
61:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:61]

```
62:     fun removeChannelPassword(channel: String) {
```
> يعرّف الدالة (removeChannelPassword) «إزالة كلمة مرور القناة» التي تأخذ `channel` نصاً ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:62]

```
63:         channelKeys.remove(channel)
```
> يحذف المفتاح المرتبط باسم القناة من خريطة `channelKeys`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:63]

```
64:         channelPasswords.remove(channel)
```
> يحذف كلمة المرور المرتبطة باسم القناة من خريطة `channelPasswords`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:64]

```
65:         Log.d(TAG, "Removed password for channel $channel")
```
> يسجّل رسالة تصحيح عبر `Log.d` بالوسم وبالنص `"Removed password for channel $channel"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:65]

```
66:     }
```
> إغلاق نطاق الدالة `removeChannelPassword`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:66]

```
67:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:67]

```
68:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:68]

```
69:      * Check if we have a key for a channel
```
> تعليق: التحقق إن كان لدينا مفتاح لقناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:69]

```
70:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:70]

```
71:     fun hasChannelKey(channel: String): Boolean {
```
> يعرّف الدالة (hasChannelKey) «هل توجد مفتاح للقناة» التي تأخذ `channel` نصاً وتُعيد قيمة منطقية ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:71]

```
72:         return channelKeys.containsKey(channel)
```
> يُعيد ما إذا كانت خريطة `channelKeys` تحتوي على مفتاح باسم القناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:72]

```
73:     }
```
> إغلاق نطاق الدالة `hasChannelKey`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:73]

```
74:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:74]

```
75:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:75]

```
76:      * Get channel password (if available)
```
> تعليق: الحصول على كلمة مرور القناة (إن وُجدت). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:76]

```
77:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:77]

```
78:     fun getChannelPassword(channel: String): String? {
```
> يعرّف الدالة (getChannelPassword) «جلب كلمة مرور القناة» التي تأخذ `channel` نصاً وتُعيد نصاً قابلاً للعدم ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:78]

```
79:         return channelPasswords[channel]
```
> يُعيد كلمة المرور المخزّنة في خريطة `channelPasswords` تحت مفتاح اسم القناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:79]

```
80:     }
```
> إغلاق نطاق الدالة `getChannelPassword`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:80]

```
81:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:81]

```
82:     // MARK: - Encryption/Decryption
```
> تعليق: علامة قسم — التشفير/فك التشفير. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:82]

```
83:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:83]

```
84:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:84]

```
85:      * Encrypt a message for a channel
```
> تعليق: تشفير رسالة لقناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:85]

```
86:      * Returns encrypted data including IV
```
> تعليق: يُعيد البيانات المشفّرة متضمّنة متّجه التهيئة (IV). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:86]

```
87:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:87]

```
88:     fun encryptChannelMessage(message: String, channel: String): ByteArray {
```
> يعرّف الدالة (encryptChannelMessage) «تشفير رسالة القناة» التي تأخذ `message` نصاً و `channel` نصاً وتُعيد مصفوفة بايتات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:88]

```
89:         val key = channelKeys[channel]
```
> يعرّف متغيّراً ثابتاً (key) «المفتاح» بقيمة المفتاح المخزّن في `channelKeys` تحت اسم القناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:89]

```
90:             ?: throw IllegalStateException("No key available for channel $channel")
```
> إن كان المفتاح فارغاً يرمي استثناء `IllegalStateException` بالنص `"No key available for channel $channel"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:90]

```
91:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:91]

```
92:         val messageBytes = message.toByteArray(Charsets.UTF_8)
```
> يعرّف متغيّراً ثابتاً (messageBytes) «بايتات الرسالة» بتحويل الرسالة إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:92]

```
93:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:93]

```
94:         return try {
```
> يبدأ إرجاع ناتج كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:94]

```
95:             val cipher = Cipher.getInstance("AES/GCM/NoPadding")
```
> يعرّف متغيّراً ثابتاً (cipher) «المُشفّر» بنسخة `Cipher` للخوارزمية `"AES/GCM/NoPadding"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:95]

```
96:             cipher.init(Cipher.ENCRYPT_MODE, key)
```
> يهيّئ المُشفّر في نمط التشفير `Cipher.ENCRYPT_MODE` بالمفتاح. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:96]

```
97:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:97]

```
98:             val iv = cipher.iv
```
> يعرّف متغيّراً ثابتاً (iv) «متّجه التهيئة» بقيمة `cipher.iv` المتولّد من المُشفّر. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:98]

```
99:             val encryptedData = cipher.doFinal(messageBytes)
```
> يعرّف متغيّراً ثابتاً (encryptedData) «البيانات المشفّرة» بناتج استدعاء `cipher.doFinal` على بايتات الرسالة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:99]

```
100:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:100]

```
101:             // Combine IV and encrypted data (same format as iOS)
```
> تعليق: دمج متّجه التهيئة والبيانات المشفّرة (نفس التنسيق كما في iOS). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:101]

```
102:             val result = ByteArray(iv.size + encryptedData.size)
```
> يعرّف متغيّراً ثابتاً (result) «النتيجة» كمصفوفة بايتات بحجم مجموع طول متّجه التهيئة وطول البيانات المشفّرة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:102]

```
103:             System.arraycopy(iv, 0, result, 0, iv.size)
```
> ينسخ متّجه التهيئة من موضعه صفر إلى النتيجة عند موضع صفر بطول متّجه التهيئة عبر `System.arraycopy`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:103]

```
104:             System.arraycopy(encryptedData, 0, result, iv.size, encryptedData.size)
```
> ينسخ البيانات المشفّرة من موضعها صفر إلى النتيجة بدءاً من موضع طول متّجه التهيئة بطول البيانات المشفّرة عبر `System.arraycopy`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:104]

```
105:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:105]

```
106:             result
```
> يُعيد قيمة `result` كنتيجة كتلة المحاولة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:106]

```
107:         } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويبدأ كتلة الالتقاط لاستثناء `Exception` باسم `e`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:107]

```
108:             Log.e(TAG, "Failed to encrypt channel message: ${e.message}")
```
> يسجّل خطأً عبر `Log.e` بالوسم وبالنص `"Failed to encrypt channel message: ${e.message}"` متضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:108]

```
109:             throw e
```
> يعيد رمي الاستثناء `e`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:109]

```
110:         }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:110]

```
111:     }
```
> إغلاق نطاق الدالة `encryptChannelMessage`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:111]

```
112:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:112]

```
113:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:113]

```
114:      * Decrypt a message for a channel
```
> تعليق: فك تشفير رسالة لقناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:114]

```
115:      * Expects data format: IV + encrypted_data + auth_tag
```
> تعليق: يتوقع تنسيق البيانات: متّجه التهيئة + البيانات المشفّرة + وسم التوثيق. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:115]

```
116:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:116]

```
117:     fun decryptChannelMessage(encryptedData: ByteArray, channel: String): String {
```
> يعرّف الدالة (decryptChannelMessage) «فك تشفير رسالة القناة» التي تأخذ `encryptedData` مصفوفة بايتات و `channel` نصاً وتُعيد نصاً ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:117]

```
118:         val key = channelKeys[channel]
```
> يعرّف متغيّراً ثابتاً (key) «المفتاح» بقيمة المفتاح المخزّن في `channelKeys` تحت اسم القناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:118]

```
119:             ?: throw IllegalStateException("No key available for channel $channel")
```
> إن كان المفتاح فارغاً يرمي استثناء `IllegalStateException` بالنص `"No key available for channel $channel"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:119]

```
120:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:120]

```
121:         if (encryptedData.size < 16) { // 12 bytes IV + minimum ciphertext
```
> يتحقق شرطاً إن كان حجم البيانات المشفّرة أقل من `16` ويفتح نطاقه، مع تعليق: 12 بايت متّجه تهيئة + الحد الأدنى من النص المشفّر. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:121]

```
122:             throw IllegalArgumentException("Encrypted data too short")
```
> يرمي استثناء `IllegalArgumentException` بالنص `"Encrypted data too short"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:122]

```
123:         }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:123]

```
124:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:124]

```
125:         return try {
```
> يبدأ إرجاع ناتج كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:125]

```
126:             val cipher = Cipher.getInstance("AES/GCM/NoPadding")
```
> يعرّف متغيّراً ثابتاً (cipher) «المُشفّر» بنسخة `Cipher` للخوارزمية `"AES/GCM/NoPadding"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:126]

```
127:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:127]

```
128:             // Extract IV (first 12 bytes for GCM) and ciphertext
```
> تعليق: استخراج متّجه التهيئة (أول 12 بايت لنمط GCM) والنص المشفّر. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:128]

```
129:             val iv = encryptedData.sliceArray(0..11)
```
> يعرّف متغيّراً ثابتاً (iv) «متّجه التهيئة» بشريحة من البيانات المشفّرة من الفهرس 0 إلى 11. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:129]

```
130:             val ciphertext = encryptedData.sliceArray(12 until encryptedData.size)
```
> يعرّف متغيّراً ثابتاً (ciphertext) «النص المشفّر» بشريحة من البيانات المشفّرة من الفهرس 12 حتى نهاية المصفوفة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:130]

```
131:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:131]

```
132:             val gcmSpec = GCMParameterSpec(128, iv) // 128-bit authentication tag
```
> يعرّف متغيّراً ثابتاً (gcmSpec) «مواصفات GCM» بنسخة `GCMParameterSpec` بطول 128 ومتّجه التهيئة، مع تعليق: وسم توثيق بطول 128 بت. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:132]

```
133:             cipher.init(Cipher.DECRYPT_MODE, key, gcmSpec)
```
> يهيّئ المُشفّر في نمط فك التشفير `Cipher.DECRYPT_MODE` بالمفتاح ومواصفات GCM. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:133]

```
134:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:134]

```
135:             val decryptedBytes = cipher.doFinal(ciphertext)
```
> يعرّف متغيّراً ثابتاً (decryptedBytes) «البايتات المفكوكة» بناتج استدعاء `cipher.doFinal` على النص المشفّر. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:135]

```
136:             String(decryptedBytes, Charsets.UTF_8)
```
> يحوّل البايتات المفكوكة إلى نص بترميز UTF-8 ويُعيده كنتيجة كتلة المحاولة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:136]

```
137:         } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويبدأ كتلة الالتقاط لاستثناء `Exception` باسم `e`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:137]

```
138:             Log.e(TAG, "Failed to decrypt channel message: ${e.message}")
```
> يسجّل خطأً عبر `Log.e` بالوسم وبالنص `"Failed to decrypt channel message: ${e.message}"` متضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:138]

```
139:             throw e
```
> يعيد رمي الاستثناء `e`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:139]

```
140:         }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:140]

```
141:     }
```
> إغلاق نطاق الدالة `decryptChannelMessage`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:141]

```
142:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:142]

```
143:     // MARK: - Key Derivation
```
> تعليق: علامة قسم — اشتقاق المفتاح. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:143]

```
144:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:144]

```
145:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:145]

```
146:      * Derive AES key from password using PBKDF2 (same parameters as iOS)
```
> تعليق: اشتقاق مفتاح AES من كلمة المرور باستخدام PBKDF2 (نفس المعاملات كما في iOS). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:146]

```
147:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:147]

```
148:     private fun deriveChannelKey(password: String, channel: String): SecretKeySpec {
```
> يعرّف الدالة الخاصة (deriveChannelKey) «اشتقاق مفتاح القناة» التي تأخذ `password` نصاً و `channel` نصاً وتُعيد `SecretKeySpec` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:148]

```
149:         try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:149]

```
150:             val factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256")
```
> يعرّف متغيّراً ثابتاً (factory) «المصنع» بنسخة `SecretKeyFactory` للخوارزمية `"PBKDF2WithHmacSHA256"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:150]

```
151:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:151]

```
152:             // Use channel name as salt (UTF-8 bytes)
```
> تعليق: استخدام اسم القناة كملح (بايتات UTF-8). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:152]

```
153:             val salt = channel.toByteArray(Charsets.UTF_8)
```
> يعرّف متغيّراً ثابتاً (salt) «الملح» بتحويل اسم القناة إلى مصفوفة بايتات بترميز UTF-8. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:153]

```
154:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:154]

```
155:             val spec = PBEKeySpec(
```
> يعرّف متغيّراً ثابتاً (spec) «المواصفات» بإنشاء نسخة `PBEKeySpec` ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:155]

```
156:                 password.toCharArray(),
```
> يمرّر كلمة المرور محوّلة إلى مصفوفة محارف كوسيط أول. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:156]

```
157:                 salt,
```
> يمرّر الملح كوسيط ثانٍ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:157]

```
158:                 PBKDF2_ITERATIONS,
```
> يمرّر الثابت `PBKDF2_ITERATIONS` (عدد التكرارات) كوسيط ثالث. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:158]

```
159:                 KEY_LENGTH
```
> يمرّر الثابت `KEY_LENGTH` (طول المفتاح) كوسيط رابع. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:159]

```
160:             )
```
> إغلاق قائمة وسائط منشئ `PBEKeySpec`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:160]

```
161:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:161]

```
162:             val secretKey = factory.generateSecret(spec)
```
> يعرّف متغيّراً ثابتاً (secretKey) «المفتاح السرّي» بناتج استدعاء `factory.generateSecret` على المواصفات. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:162]

```
163:             return SecretKeySpec(secretKey.encoded, "AES")
```
> يُعيد نسخة `SecretKeySpec` مبنية من بايتات المفتاح السرّي المرمّزة وبخوارزمية `"AES"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:163]

```
164:         } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويبدأ كتلة الالتقاط لاستثناء `Exception` باسم `e`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:164]

```
165:             Log.e(TAG, "Failed to derive channel key: ${e.message}")
```
> يسجّل خطأً عبر `Log.e` بالوسم وبالنص `"Failed to derive channel key: ${e.message}"` متضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:165]

```
166:             throw e
```
> يعيد رمي الاستثناء `e`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:166]

```
167:         }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:167]

```
168:     }
```
> إغلاق نطاق الدالة `deriveChannelKey`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:168]

```
169:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:169]

```
170:     // MARK: - Key Verification
```
> تعليق: علامة قسم — التحقق من المفتاح. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:170]

```
171:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:171]

```
172:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:172]

```
173:      * Calculate key commitment (SHA-256 hash) for verification
```
> تعليق: حساب التزام المفتاح (بصمة SHA-256) للتحقق. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:173]

```
174:      * This allows peers to verify they have the same key without revealing it
```
> تعليق: هذا يتيح للأقران التحقق أن لديهم المفتاح ذاته دون كشفه. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:174]

```
175:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:175]

```
176:     fun calculateKeyCommitment(channel: String): String? {
```
> يعرّف الدالة (calculateKeyCommitment) «حساب التزام المفتاح» التي تأخذ `channel` نصاً وتُعيد نصاً قابلاً للعدم ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:176]

```
177:         val key = channelKeys[channel] ?: return null
```
> يعرّف متغيّراً ثابتاً (key) «المفتاح» بقيمة المفتاح من `channelKeys` تحت اسم القناة، وإن كان فارغاً يُعيد `null`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:177]

```
178:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:178]

```
179:         return try {
```
> يبدأ إرجاع ناتج كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:179]

```
180:             val digest = MessageDigest.getInstance("SHA-256")
```
> يعرّف متغيّراً ثابتاً (digest) «الهاضم» بنسخة `MessageDigest` للخوارزمية `"SHA-256"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:180]

```
181:             val hash = digest.digest(key.encoded)
```
> يعرّف متغيّراً ثابتاً (hash) «البصمة» بناتج استدعاء `digest.digest` على بايتات المفتاح المرمّزة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:181]

```
182:             hash.joinToString("") { "%02x".format(it) }
```
> يحوّل البصمة إلى نص ست عشري بدون فاصل، بتنسيق كل بايت بصيغة `"%02x"`، ويُعيده كنتيجة كتلة المحاولة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:182]

```
183:         } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويبدأ كتلة الالتقاط لاستثناء `Exception` باسم `e`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:183]

```
184:             Log.e(TAG, "Failed to calculate key commitment: ${e.message}")
```
> يسجّل خطأً عبر `Log.e` بالوسم وبالنص `"Failed to calculate key commitment: ${e.message}"` متضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:184]

```
185:             null
```
> يُعيد `null` كنتيجة كتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:185]

```
186:         }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:186]

```
187:     }
```
> إغلاق نطاق الدالة `calculateKeyCommitment`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:187]

```
188:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:188]

```
189:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:189]

```
190:      * Verify key commitment matches our derived key
```
> تعليق: التحقق أن التزام المفتاح يطابق مفتاحنا المشتق. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:190]

```
191:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:191]

```
192:     fun verifyKeyCommitment(channel: String, commitment: String): Boolean {
```
> يعرّف الدالة (verifyKeyCommitment) «التحقق من التزام المفتاح» التي تأخذ `channel` نصاً و `commitment` نصاً وتُعيد قيمة منطقية ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:192]

```
193:         val ourCommitment = calculateKeyCommitment(channel)
```
> يعرّف متغيّراً ثابتاً (ourCommitment) «التزامنا» بناتج استدعاء `calculateKeyCommitment` على القناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:193]

```
194:         return ourCommitment?.lowercase() == commitment.lowercase()
```
> يُعيد مقارنة المساواة بين التزامنا بحروف صغيرة والتزام المُدخل بحروف صغيرة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:194]

```
195:     }
```
> إغلاق نطاق الدالة `verifyKeyCommitment`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:195]

```
196:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:196]

```
197:     // MARK: - Channel Key Sharing
```
> تعليق: علامة قسم — مشاركة مفتاح القناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:197]

```
198:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:198]

```
199:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:199]

```
200:      * Create channel key packet for sharing via Noise session
```
> تعليق: إنشاء حزمة مفتاح القناة للمشاركة عبر جلسة Noise. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:200]

```
201:      * Returns encrypted packet that can be sent to other peers
```
> تعليق: يُعيد حزمة مشفّرة يمكن إرسالها إلى أقران آخرين. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:201]

```
202:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:202]

```
203:     fun createChannelKeyPacket(password: String, channel: String): ByteArray? {
```
> يعرّف الدالة (createChannelKeyPacket) «إنشاء حزمة مفتاح القناة» التي تأخذ `password` نصاً و `channel` نصاً وتُعيد مصفوفة بايتات قابلة للعدم ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:203]

```
204:         return try {
```
> يبدأ إرجاع ناتج كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:204]

```
205:             // Create key packet with channel and password
```
> تعليق: إنشاء حزمة المفتاح متضمّنة القناة وكلمة المرور. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:205]

```
206:             val packet = mapOf(
```
> يعرّف متغيّراً ثابتاً (packet) «الحزمة» بإنشاء خريطة عبر `mapOf` ويفتح قائمة عناصرها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:206]

```
207:                 "channel" to channel,
```
> يضيف زوجاً يربط المفتاح `"channel"` بقيمة اسم القناة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:207]

```
208:                 "password" to password,
```
> يضيف زوجاً يربط المفتاح `"password"` بقيمة كلمة المرور. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:208]

```
209:                 "timestamp" to System.currentTimeMillis()
```
> يضيف زوجاً يربط المفتاح `"timestamp"` بقيمة الوقت الحالي بالملّي ثانية من `System.currentTimeMillis()`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:209]

```
210:             )
```
> إغلاق قائمة عناصر `mapOf`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:210]

```
211:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:211]

```
212:             // Simple JSON encoding for now (could be replaced with more efficient format)
```
> تعليق: ترميز JSON بسيط حالياً (يمكن استبداله بتنسيق أكفأ). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:212]

```
213:             val json = com.google.gson.Gson().toJson(packet)
```
> يعرّف متغيّراً ثابتاً (json) «جيسون» بناتج تحويل الحزمة إلى نص JSON عبر `com.google.gson.Gson().toJson`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:213]

```
214:             json.toByteArray(Charsets.UTF_8)
```
> يحوّل نص JSON إلى مصفوفة بايتات بترميز UTF-8 ويُعيدها كنتيجة كتلة المحاولة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:214]

```
215:         } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويبدأ كتلة الالتقاط لاستثناء `Exception` باسم `e`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:215]

```
216:             Log.e(TAG, "Failed to create channel key packet: ${e.message}")
```
> يسجّل خطأً عبر `Log.e` بالوسم وبالنص `"Failed to create channel key packet: ${e.message}"` متضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:216]

```
217:             null
```
> يُعيد `null` كنتيجة كتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:217]

```
218:         }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:218]

```
219:     }
```
> إغلاق نطاق الدالة `createChannelKeyPacket`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:219]

```
220:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:220]

```
221:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:221]

```
222:      * Process received channel key packet
```
> تعليق: معالجة حزمة مفتاح القناة المستلَمة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:222]

```
223:      * Returns (channel, password) if successful
```
> تعليق: يُعيد (القناة، كلمة المرور) عند النجاح. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:223]

```
224:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:224]

```
225:     fun processChannelKeyPacket(data: ByteArray): Pair<String, String>? {
```
> يعرّف الدالة (processChannelKeyPacket) «معالجة حزمة مفتاح القناة» التي تأخذ `data` مصفوفة بايتات وتُعيد زوجاً (Pair) من نصّين قابلاً للعدم ويفتح نطاقها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:225]

```
226:         return try {
```
> يبدأ إرجاع ناتج كتلة محاولة (try). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:226]

```
227:             val json = String(data, Charsets.UTF_8)
```
> يعرّف متغيّراً ثابتاً (json) «جيسون» بتحويل البيانات إلى نص بترميز UTF-8. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:227]

```
228:             val packet = com.google.gson.Gson().fromJson(json, Map::class.java) as Map<String, Any>
```
> يعرّف متغيّراً ثابتاً (packet) «الحزمة» بتحليل نص JSON إلى `Map` عبر `com.google.gson.Gson().fromJson` ثم تحويله صراحةً إلى `Map<String, Any>`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:228]

```
229:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:229]

```
230:             val channel = packet["channel"] as? String
```
> يعرّف متغيّراً ثابتاً (channel) «القناة» بقيمة المفتاح `"channel"` من الحزمة محوّلاً بأمان إلى نص. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:230]

```
231:             val password = packet["password"] as? String
```
> يعرّف متغيّراً ثابتاً (password) «كلمة المرور» بقيمة المفتاح `"password"` من الحزمة محوّلاً بأمان إلى نص. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:231]

```
232:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:232]

```
233:             if (channel != null && password != null) {
```
> يتحقق شرطاً إن كانت القناة وكلمة المرور كلتاهما غير فارغتين ويفتح نطاقه. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:233]

```
234:                 Pair(channel, password)
```
> يُنشئ زوجاً (Pair) من القناة وكلمة المرور ويُعيده كنتيجة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:234]

```
235:             } else {
```
> يغلق نطاق الشرط ويبدأ نطاق وإلا (else). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:235]

```
236:                 Log.w(TAG, "Invalid channel key packet format")
```
> يسجّل تحذيراً عبر `Log.w` بالوسم وبالنص `"Invalid channel key packet format"`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:236]

```
237:                 null
```
> يُعيد `null` كنتيجة فرع وإلا. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:237]

```
238:             }
```
> إغلاق نطاق فرع وإلا. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:238]

```
239:         } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويبدأ كتلة الالتقاط لاستثناء `Exception` باسم `e`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:239]

```
240:             Log.e(TAG, "Failed to process channel key packet: ${e.message}")
```
> يسجّل خطأً عبر `Log.e` بالوسم وبالنص `"Failed to process channel key packet: ${e.message}"` متضمّناً رسالة الاستثناء. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:240]

```
241:             null
```
> يُعيد `null` كنتيجة كتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:241]

```
242:         }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:242]

```
243:     }
```
> إغلاق نطاق الدالة `processChannelKeyPacket`. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:243]

```
244:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:244]

```
245:     // MARK: - Debug and Management
```
> تعليق: علامة قسم — التصحيح والإدارة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:245]

```
246:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:246]

```
247:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:247]

```
248:      * Get debug information
```
> تعليق: الحصول على معلومات التصحيح. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:248]

```
249:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:249]

```
250:     fun getDebugInfo(): String = buildString {
```
> يعرّف الدالة (getDebugInfo) «جلب معلومات التصحيح» التي تُعيد نصاً عبر تعبير `buildString` ويفتح نطاق بانيه. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:250]
