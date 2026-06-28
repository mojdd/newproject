# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:2]

```
3: import org.bouncycastle.crypto.ec.CustomNamedCurves
```
> يستورد (import) الصنف `CustomNamedCurves` من مكتبة BouncyCastle. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:3]

```
4: import org.bouncycastle.crypto.params.ECDomainParameters
```
> يستورد الصنف `ECDomainParameters` (معاملات مجال المنحنى الإهليلجي). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:4]

```
5: import org.bouncycastle.crypto.params.ECPrivateKeyParameters
```
> يستورد الصنف `ECPrivateKeyParameters` (معاملات المفتاح الخاص الإهليلجي). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:5]

```
6: import org.bouncycastle.crypto.params.ECPublicKeyParameters
```
> يستورد الصنف `ECPublicKeyParameters` (معاملات المفتاح العام الإهليلجي). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:6]

```
7: import org.bouncycastle.math.ec.ECPoint
```
> يستورد الصنف `ECPoint` (نقطة على المنحنى الإهليلجي). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:7]

```
8: import org.bouncycastle.crypto.generators.ECKeyPairGenerator
```
> يستورد الصنف `ECKeyPairGenerator` (مولّد أزواج المفاتيح الإهليلجية). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:8]

```
9: import org.bouncycastle.crypto.params.ECKeyGenerationParameters
```
> يستورد الصنف `ECKeyGenerationParameters` (معاملات توليد المفاتيح الإهليلجية). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:9]

```
10: import org.bouncycastle.crypto.agreement.ECDHBasicAgreement
```
> يستورد الصنف `ECDHBasicAgreement` (اتفاق ECDH الأساسي). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:10]

```
11: import org.bouncycastle.crypto.digests.SHA256Digest
```
> يستورد الصنف `SHA256Digest` (هضم SHA-256). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:11]

```
12: import org.bouncycastle.crypto.macs.HMac
```
> يستورد الصنف `HMac` (شفرة مصادقة الرسالة المعتمدة على التجزئة). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:12]

```
13: import org.bouncycastle.crypto.params.KeyParameter
```
> يستورد الصنف `KeyParameter` (معامل المفتاح). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:13]

```
14: import com.google.crypto.tink.subtle.XChaCha20Poly1305
```
> يستورد الصنف `XChaCha20Poly1305` من مكتبة Tink. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:14]

```
15: import java.security.SecureRandom
```
> يستورد الصنف `SecureRandom` (مولّد عشوائي آمن). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:15]

```
16: import java.security.MessageDigest
```
> يستورد الصنف `MessageDigest` (هضم الرسالة). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:16]

```
17: import java.math.BigInteger
```
> يستورد الصنف `BigInteger` (العدد الصحيح الكبير). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:17]

```
18: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:18]

```
19: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:19]

```
20:  * Cryptographic utilities for Nostr protocol
```
> تعليق: «أدوات تشفيرية لبروتوكول Nostr». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:20]

```
21:  * Includes secp256k1 operations, ECDH, and NIP-44 encryption
```
> تعليق: «يشمل عمليات secp256k1 و ECDH وتشفير NIP-44». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:21]

```
22:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:22]

```
23: object NostrCrypto {
```
> يعرّف كائناً وحيداً (object) باسم `NostrCrypto` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:23]

```
24:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:24]

```
25:     private val secureRandom = SecureRandom()
```
> يعرّف خاصية خاصة ثابتة باسم `secureRandom` ويضبط قيمتها إلى كائن `SecureRandom` جديد. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:25]

```
26:     // NIP-44 v2 only
```
> تعليق: «NIP-44 الإصدار 2 فقط». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:26]

```
27:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:27]

```
28:     // secp256k1 curve parameters
```
> تعليق: «معاملات منحنى secp256k1». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:28]

```
29:     val secp256k1Curve = CustomNamedCurves.getByName("secp256k1")
```
> يعرّف خاصية باسم `secp256k1Curve` ويضبط قيمتها إلى نتيجة استدعاء `CustomNamedCurves.getByName` بالوسيط النصي `"secp256k1"`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:29]

```
30:     val secp256k1Params = ECDomainParameters(
```
> يعرّف خاصية باسم `secp256k1Params` ويبدأ بناء كائن `ECDomainParameters`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:30]

```
31:         secp256k1Curve.curve,
```
> يمرّر الوسيط `secp256k1Curve.curve` (المنحنى) إلى المُنشئ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:31]

```
32:         secp256k1Curve.g,
```
> يمرّر الوسيط `secp256k1Curve.g` (نقطة المولّد) إلى المُنشئ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:32]

```
33:         secp256k1Curve.n,
```
> يمرّر الوسيط `secp256k1Curve.n` (رتبة المولّد) إلى المُنشئ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:33]

```
34:         secp256k1Curve.h
```
> يمرّر الوسيط `secp256k1Curve.h` (المعامل المساعد) إلى المُنشئ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:34]

```
35:     )
```
> إغلاق قائمة وسائط المُنشئ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:35]

```
36:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:36]

```
37:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:37]

```
38:      * Generate secp256k1 key pair
```
> تعليق: «توليد زوج مفاتيح secp256k1». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:38]

```
39:      * Returns (privateKeyHex, publicKeyHex)
```
> تعليق: «يُعيد (المفتاح الخاص بالست عشري، المفتاح العام بالست عشري)». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:39]

```
40:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:40]

```
41:     fun generateKeyPair(): Pair<String, String> {
```
> يعرّف دالة (fun) باسم `generateKeyPair` تُعيد `Pair<String, String>` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:41]

```
42:         val generator = ECKeyPairGenerator()
```
> يعرّف متغيراً ثابتاً باسم `generator` ويضبط قيمته إلى كائن `ECKeyPairGenerator` جديد. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:42]

```
43:         val keyGenParams = ECKeyGenerationParameters(secp256k1Params, secureRandom)
```
> يعرّف متغيراً ثابتاً باسم `keyGenParams` ويضبط قيمته إلى كائن `ECKeyGenerationParameters` مبنيٍّ بالوسيطين `secp256k1Params` و`secureRandom`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:43]

```
44:         generator.init(keyGenParams)
```
> يستدعي `init` على `generator` بالوسيط `keyGenParams`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:44]

```
45:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:45]

```
46:         val keyPair = generator.generateKeyPair()
```
> يعرّف متغيراً ثابتاً باسم `keyPair` ويضبط قيمته إلى نتيجة استدعاء `generator.generateKeyPair()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:46]

```
47:         val privateKey = keyPair.private as ECPrivateKeyParameters
```
> يعرّف متغيراً ثابتاً باسم `privateKey` ويضبط قيمته إلى `keyPair.private` بعد تحويله (cast) إلى `ECPrivateKeyParameters`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:47]

```
48:         val publicKey = keyPair.public as ECPublicKeyParameters
```
> يعرّف متغيراً ثابتاً باسم `publicKey` ويضبط قيمته إلى `keyPair.public` بعد تحويله إلى `ECPublicKeyParameters`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:48]

```
49:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:49]

```
50:         // Get private key as 32-byte hex - ensure proper padding
```
> تعليق: «الحصول على المفتاح الخاص كنصٍّ ست عشري بطول 32 بايت - مع ضمان الحشو الصحيح». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:50]

```
51:         val privateKeyBigInt = privateKey.d
```
> يعرّف متغيراً ثابتاً باسم `privateKeyBigInt` ويضبط قيمته إلى `privateKey.d`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:51]

```
52:         val privateKeyBytes = privateKeyBigInt.toByteArray()
```
> يعرّف متغيراً ثابتاً باسم `privateKeyBytes` ويضبط قيمته إلى نتيجة `privateKeyBigInt.toByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:52]

```
53:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:53]

```
54:         val privateKeyPadded = ByteArray(32)
```
> يعرّف متغيراً ثابتاً باسم `privateKeyPadded` ويضبط قيمته إلى مصفوفة بايت (`ByteArray`) بطول 32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:54]

```
55:         if (privateKeyBytes.size <= 32) {
```
> يبدأ شرطاً (if) يختبر ما إذا كان حجم `privateKeyBytes` أصغر من أو يساوي 32 ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:55]

```
56:             val srcStart = maxOf(0, privateKeyBytes.size - 32)
```
> يعرّف متغيراً ثابتاً باسم `srcStart` ويضبط قيمته إلى أكبر قيمة بين 0 و(حجم `privateKeyBytes` ناقص 32). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:56]

```
57:             val destStart = maxOf(0, 32 - privateKeyBytes.size)
```
> يعرّف متغيراً ثابتاً باسم `destStart` ويضبط قيمته إلى أكبر قيمة بين 0 و(32 ناقص حجم `privateKeyBytes`). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:57]

```
58:             val length = minOf(privateKeyBytes.size, 32)
```
> يعرّف متغيراً ثابتاً باسم `length` ويضبط قيمته إلى أصغر قيمة بين حجم `privateKeyBytes` و32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:58]

```
59:             System.arraycopy(privateKeyBytes, srcStart, privateKeyPadded, destStart, length)
```
> يستدعي `System.arraycopy` لنسخ من `privateKeyBytes` بدءاً من `srcStart` إلى `privateKeyPadded` بدءاً من `destStart` بطول `length`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:59]

```
60:         } else {
```
> يُغلق نطاق الشرط ويبدأ فرع `else` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:60]

```
61:             // If BigInteger added a sign byte, skip it
```
> تعليق: «إذا أضاف BigInteger بايت إشارة، فتجاوزه». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:61]

```
62:             System.arraycopy(privateKeyBytes, privateKeyBytes.size - 32, privateKeyPadded, 0, 32)
```
> يستدعي `System.arraycopy` لنسخ من `privateKeyBytes` بدءاً من (حجمه ناقص 32) إلى `privateKeyPadded` بدءاً من 0 بطول 32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:62]

```
63:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:63]

```
64:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:64]

```
65:         // Get x-only public key (32 bytes)
```
> تعليق: «الحصول على المفتاح العام بإحداثي x فقط (32 بايت)». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:65]

```
66:         val publicKeyPoint = publicKey.q.normalize()
```
> يعرّف متغيراً ثابتاً باسم `publicKeyPoint` ويضبط قيمته إلى نتيجة `publicKey.q.normalize()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:66]

```
67:         val xCoord = publicKeyPoint.xCoord.encoded
```
> يعرّف متغيراً ثابتاً باسم `xCoord` ويضبط قيمته إلى `publicKeyPoint.xCoord.encoded`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:67]

```
68:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:68]

```
69:         return Pair(
```
> يبدأ عبارة إعادة (return) لكائن `Pair`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:69]

```
70:             privateKeyPadded.toHexString(),
```
> يمرّر العنصر الأول `privateKeyPadded.toHexString()` إلى `Pair`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:70]

```
71:             xCoord.toHexString()
```
> يمرّر العنصر الثاني `xCoord.toHexString()` إلى `Pair`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:71]

```
72:         )
```
> إغلاق وسائط `Pair` المُعاد. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:72]

```
73:     }
```
> إغلاق نطاق (نهاية دالة `generateKeyPair`). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:73]

```
74:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:74]

```
75:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:75]

```
76:      * Derive public key from private key
```
> تعليق: «اشتقاق المفتاح العام من المفتاح الخاص». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:76]

```
77:      * Returns x-only public key (32 bytes hex)
```
> تعليق: «يُعيد المفتاح العام بإحداثي x فقط (32 بايت ست عشري)». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:77]

```
78:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:78]

```
79:     fun derivePublicKey(privateKeyHex: String): String {
```
> يعرّف دالة باسم `derivePublicKey` تأخذ معاملاً `privateKeyHex` من نوع `String` وتُعيد `String` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:79]

```
80:         val privateKeyBytes = privateKeyHex.hexToByteArray()
```
> يعرّف متغيراً ثابتاً باسم `privateKeyBytes` ويضبط قيمته إلى نتيجة `privateKeyHex.hexToByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:80]

```
81:         val privateKeyBigInt = BigInteger(1, privateKeyBytes)
```
> يعرّف متغيراً ثابتاً باسم `privateKeyBigInt` ويضبط قيمته إلى كائن `BigInteger` مبنيٍّ بالإشارة 1 والمصفوفة `privateKeyBytes`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:81]

```
82:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:82]

```
83:         val publicKeyPoint = secp256k1Params.g.multiply(privateKeyBigInt).normalize()
```
> يعرّف متغيراً ثابتاً باسم `publicKeyPoint` ويضبط قيمته إلى نتيجة `secp256k1Params.g.multiply(privateKeyBigInt).normalize()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:83]

```
84:         val xCoord = publicKeyPoint.xCoord.encoded
```
> يعرّف متغيراً ثابتاً باسم `xCoord` ويضبط قيمته إلى `publicKeyPoint.xCoord.encoded`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:84]

```
85:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:85]

```
86:         return xCoord.toHexString()
```
> يُعيد نتيجة `xCoord.toHexString()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:86]

```
87:     }
```
> إغلاق نطاق (نهاية دالة `derivePublicKey`). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:87]

```
88:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:88]

```
89:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:89]

```
90:      * Perform ECDH key agreement
```
> تعليق: «تنفيذ اتفاق مفاتيح ECDH». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:90]

```
91:      * Returns shared secret
```
> تعليق: «يُعيد السرّ المشترك». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:91]

```
92:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:92]

```
93:     fun performECDH(privateKeyHex: String, publicKeyHex: String): ByteArray {
```
> يعرّف دالة باسم `performECDH` تأخذ المعاملين `privateKeyHex` و`publicKeyHex` من نوع `String` وتُعيد `ByteArray` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:93]

```
94:         val privateKeyBytes = privateKeyHex.hexToByteArray()
```
> يعرّف متغيراً ثابتاً باسم `privateKeyBytes` ويضبط قيمته إلى نتيجة `privateKeyHex.hexToByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:94]

```
95:         val publicKeyBytes = publicKeyHex.hexToByteArray()
```
> يعرّف متغيراً ثابتاً باسم `publicKeyBytes` ويضبط قيمته إلى نتيجة `publicKeyHex.hexToByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:95]

```
96:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:96]

```
97:         val privateKeyBigInt = BigInteger(1, privateKeyBytes)
```
> يعرّف متغيراً ثابتاً باسم `privateKeyBigInt` ويضبط قيمته إلى كائن `BigInteger` مبنيٍّ بالإشارة 1 والمصفوفة `privateKeyBytes`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:97]

```
98:         val privateKeyParams = ECPrivateKeyParameters(privateKeyBigInt, secp256k1Params)
```
> يعرّف متغيراً ثابتاً باسم `privateKeyParams` ويضبط قيمته إلى كائن `ECPrivateKeyParameters` مبنيٍّ بالوسيطين `privateKeyBigInt` و`secp256k1Params`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:98]

```
99:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:99]

```
100:         // Recover full public key point from x-only coordinate (prefer even y per BIP-340)
```
> تعليق: «استعادة نقطة المفتاح العام الكاملة من إحداثي x فقط (تفضيل y الزوجي حسب BIP-340)». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:100]

```
101:         val publicKeyPoint = recoverPublicKeyPoint(publicKeyBytes)
```
> يعرّف متغيراً ثابتاً باسم `publicKeyPoint` ويضبط قيمته إلى نتيجة استدعاء `recoverPublicKeyPoint` بالوسيط `publicKeyBytes`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:101]

```
102:         val publicKeyParams = ECPublicKeyParameters(publicKeyPoint, secp256k1Params)
```
> يعرّف متغيراً ثابتاً باسم `publicKeyParams` ويضبط قيمته إلى كائن `ECPublicKeyParameters` مبنيٍّ بالوسيطين `publicKeyPoint` و`secp256k1Params`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:102]

```
103:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:103]

```
104:         val agreement = ECDHBasicAgreement()
```
> يعرّف متغيراً ثابتاً باسم `agreement` ويضبط قيمته إلى كائن `ECDHBasicAgreement` جديد. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:104]

```
105:         agreement.init(privateKeyParams)
```
> يستدعي `init` على `agreement` بالوسيط `privateKeyParams`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:105]

```
106:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:106]

```
107:         val sharedSecret = agreement.calculateAgreement(publicKeyParams)
```
> يعرّف متغيراً ثابتاً باسم `sharedSecret` ويضبط قيمته إلى نتيجة `agreement.calculateAgreement(publicKeyParams)`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:107]

```
108:         val sharedSecretBytes = sharedSecret.toByteArray()
```
> يعرّف متغيراً ثابتاً باسم `sharedSecretBytes` ويضبط قيمته إلى نتيجة `sharedSecret.toByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:108]

```
109:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:109]

```
110:         // Ensure 32 bytes
```
> تعليق: «ضمان 32 بايت». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:110]

```
111:         val result = ByteArray(32)
```
> يعرّف متغيراً ثابتاً باسم `result` ويضبط قيمته إلى مصفوفة بايت بطول 32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:111]

```
112:         if (sharedSecretBytes.size <= 32) {
```
> يبدأ شرطاً يختبر ما إذا كان حجم `sharedSecretBytes` أصغر من أو يساوي 32 ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:112]

```
113:             System.arraycopy(
```
> يبدأ استدعاء `System.arraycopy`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:113]

```
114:                 sharedSecretBytes,
```
> يمرّر الوسيط `sharedSecretBytes` (المصدر) إلى `System.arraycopy`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:114]

```
115:                 maxOf(0, sharedSecretBytes.size - 32),
```
> يمرّر موضع البدء في المصدر كأكبر قيمة بين 0 و(حجم `sharedSecretBytes` ناقص 32). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:115]

```
116:                 result,
```
> يمرّر الوسيط `result` (الوجهة) إلى `System.arraycopy`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:116]

```
117:                 maxOf(0, 32 - sharedSecretBytes.size),
```
> يمرّر موضع البدء في الوجهة كأكبر قيمة بين 0 و(32 ناقص حجم `sharedSecretBytes`). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:117]

```
118:                 minOf(sharedSecretBytes.size, 32)
```
> يمرّر الطول كأصغر قيمة بين حجم `sharedSecretBytes` و32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:118]

```
119:             )
```
> إغلاق وسائط استدعاء `System.arraycopy`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:119]

```
120:         } else {
```
> يُغلق نطاق الشرط ويبدأ فرع `else` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:120]

```
121:             // If BigInteger added a leading sign byte, keep the last 32 bytes
```
> تعليق: «إذا أضاف BigInteger بايت إشارة في المقدمة، فاحتفظ بآخر 32 بايت». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:121]

```
122:             System.arraycopy(sharedSecretBytes, sharedSecretBytes.size - 32, result, 0, 32)
```
> يستدعي `System.arraycopy` لنسخ من `sharedSecretBytes` بدءاً من (حجمه ناقص 32) إلى `result` بدءاً من 0 بطول 32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:122]

```
123:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:123]

```
124:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:124]

```
125:         return result
```
> يُعيد المتغير `result`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:125]

```
126:     }
```
> إغلاق نطاق (نهاية دالة `performECDH`). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:126]

```
127: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:127]

```
128:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:128]

```
129:      * Perform ECDH with explicit parity choice for the x-only public key
```
> تعليق: «تنفيذ ECDH مع اختيار صريح للزوجية للمفتاح العام بإحداثي x فقط». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:129]

```
130:      * If preferOddY is true, use the odd-y lift; otherwise even-y lift.
```
> تعليق: «إذا كان preferOddY صحيحاً، استخدم رفع y الفردي؛ وإلا رفع y الزوجي». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:130]

```
131:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:131]

```
132:     private fun performECDHWithParity(privateKeyHex: String, publicKeyHex: String, preferOddY: Boolean): ByteArray {
```
> يعرّف دالة خاصة باسم `performECDHWithParity` تأخذ المعاملات `privateKeyHex` و`publicKeyHex` من نوع `String` و`preferOddY` من نوع `Boolean` وتُعيد `ByteArray` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:132]

```
133:         val privateKeyBytes = privateKeyHex.hexToByteArray()
```
> يعرّف متغيراً ثابتاً باسم `privateKeyBytes` ويضبط قيمته إلى نتيجة `privateKeyHex.hexToByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:133]

```
134:         val publicKeyBytes = publicKeyHex.hexToByteArray()
```
> يعرّف متغيراً ثابتاً باسم `publicKeyBytes` ويضبط قيمته إلى نتيجة `publicKeyHex.hexToByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:134]

```
135:         val privateKeyBigInt = BigInteger(1, privateKeyBytes)
```
> يعرّف متغيراً ثابتاً باسم `privateKeyBigInt` ويضبط قيمته إلى كائن `BigInteger` مبنيٍّ بالإشارة 1 والمصفوفة `privateKeyBytes`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:135]

```
136:         val privateKeyParams = ECPrivateKeyParameters(privateKeyBigInt, secp256k1Params)
```
> يعرّف متغيراً ثابتاً باسم `privateKeyParams` ويضبط قيمته إلى كائن `ECPrivateKeyParameters` مبنيٍّ بالوسيطين `privateKeyBigInt` و`secp256k1Params`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:136]

```
137:         val point = recoverPublicKeyPointWithParity(publicKeyBytes, preferOddY)
```
> يعرّف متغيراً ثابتاً باسم `point` ويضبط قيمته إلى نتيجة استدعاء `recoverPublicKeyPointWithParity` بالوسيطين `publicKeyBytes` و`preferOddY`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:137]

```
138:         val publicKeyParams = ECPublicKeyParameters(point, secp256k1Params)
```
> يعرّف متغيراً ثابتاً باسم `publicKeyParams` ويضبط قيمته إلى كائن `ECPublicKeyParameters` مبنيٍّ بالوسيطين `point` و`secp256k1Params`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:138]

```
139:         val agreement = ECDHBasicAgreement()
```
> يعرّف متغيراً ثابتاً باسم `agreement` ويضبط قيمته إلى كائن `ECDHBasicAgreement` جديد. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:139]

```
140:         agreement.init(privateKeyParams)
```
> يستدعي `init` على `agreement` بالوسيط `privateKeyParams`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:140]

```
141:         val sharedSecret = agreement.calculateAgreement(publicKeyParams)
```
> يعرّف متغيراً ثابتاً باسم `sharedSecret` ويضبط قيمته إلى نتيجة `agreement.calculateAgreement(publicKeyParams)`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:141]

```
142:         val sharedSecretBytes = sharedSecret.toByteArray()
```
> يعرّف متغيراً ثابتاً باسم `sharedSecretBytes` ويضبط قيمته إلى نتيجة `sharedSecret.toByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:142]

```
143:         val result = ByteArray(32)
```
> يعرّف متغيراً ثابتاً باسم `result` ويضبط قيمته إلى مصفوفة بايت بطول 32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:143]

```
144:         if (sharedSecretBytes.size <= 32) {
```
> يبدأ شرطاً يختبر ما إذا كان حجم `sharedSecretBytes` أصغر من أو يساوي 32 ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:144]

```
145:             System.arraycopy(sharedSecretBytes, maxOf(0, sharedSecretBytes.size - 32), result, maxOf(0, 32 - sharedSecretBytes.size), minOf(sharedSecretBytes.size, 32))
```
> يستدعي `System.arraycopy` بالمصدر `sharedSecretBytes` وموضع بدء المصدر أكبر قيمة بين 0 و(حجمه ناقص 32) والوجهة `result` وموضع بدء الوجهة أكبر قيمة بين 0 و(32 ناقص حجمه) والطول أصغر قيمة بين حجمه و32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:145]

```
146:         } else {
```
> يُغلق نطاق الشرط ويبدأ فرع `else` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:146]

```
147:             // If BigInteger added a leading sign byte, keep the last 32 bytes
```
> تعليق: «إذا أضاف BigInteger بايت إشارة في المقدمة، فاحتفظ بآخر 32 بايت». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:147]

```
148:             System.arraycopy(sharedSecretBytes, sharedSecretBytes.size - 32, result, 0, 32)
```
> يستدعي `System.arraycopy` لنسخ من `sharedSecretBytes` بدءاً من (حجمه ناقص 32) إلى `result` بدءاً من 0 بطول 32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:148]

```
149:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:149]

```
150:         return result
```
> يُعيد المتغير `result`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:150]

```
151:     }
```
> إغلاق نطاق (نهاية دالة `performECDHWithParity`). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:151]

```
152:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:152]

```
153:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:153]

```
154:      * Recover full EC point from x-only coordinate
```
> تعليق: «استعادة نقطة المنحنى الإهليلجي الكاملة من إحداثي x فقط». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:154]

```
155:      * Tries both possible y coordinates
```
> تعليق: «يجرّب كلا إحداثيي y المحتملين». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:155]

```
156:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:156]

```
157:     private fun recoverPublicKeyPoint(xOnlyBytes: ByteArray): ECPoint {
```
> يعرّف دالة خاصة باسم `recoverPublicKeyPoint` تأخذ معاملاً `xOnlyBytes` من نوع `ByteArray` وتُعيد `ECPoint` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:157]

```
158:         require(xOnlyBytes.size == 32) { "X-only public key must be 32 bytes" }
```
> يستدعي `require` للتحقق من أن حجم `xOnlyBytes` يساوي 32، وإلا يرمي خطأ بالرسالة «X-only public key must be 32 bytes». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:158]

```
159:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:159]

```
160:         val x = BigInteger(1, xOnlyBytes)
```
> يعرّف متغيراً ثابتاً باسم `x` ويضبط قيمته إلى كائن `BigInteger` مبنيٍّ بالإشارة 1 والمصفوفة `xOnlyBytes`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:160]

```
161:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:161]

```
162:         // Try even y first (0x02 prefix)
```
> تعليق: «جرّب y الزوجي أولاً (بادئة 0x02)». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:162]

```
163:         try {
```
> يبدأ كتلة `try` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:163]

```
164:             val compressedBytes = ByteArray(33)
```
> يعرّف متغيراً ثابتاً باسم `compressedBytes` ويضبط قيمته إلى مصفوفة بايت بطول 33. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:164]

```
165:             compressedBytes[0] = 0x02
```
> يضبط العنصر الأول من `compressedBytes` إلى القيمة 0x02. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:165]

```
166:             System.arraycopy(xOnlyBytes, 0, compressedBytes, 1, 32)
```
> يستدعي `System.arraycopy` لنسخ من `xOnlyBytes` بدءاً من 0 إلى `compressedBytes` بدءاً من 1 بطول 32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:166]

```
167:             return secp256k1Curve.curve.decodePoint(compressedBytes)
```
> يُعيد نتيجة `secp256k1Curve.curve.decodePoint(compressedBytes)`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:167]

```
168:         } catch (e: Exception) {
```
> يُغلق نطاق `try` ويبدأ كتلة `catch` تلتقط استثناءً `e` من نوع `Exception` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:168]

```
169:             // Try odd y (0x03 prefix)
```
> تعليق: «جرّب y الفردي (بادئة 0x03)». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:169]

```
170:             val compressedBytes = ByteArray(33)
```
> يعرّف متغيراً ثابتاً باسم `compressedBytes` ويضبط قيمته إلى مصفوفة بايت بطول 33. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:170]

```
171:             compressedBytes[0] = 0x03
```
> يضبط العنصر الأول من `compressedBytes` إلى القيمة 0x03. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:171]

```
172:             System.arraycopy(xOnlyBytes, 0, compressedBytes, 1, 32)
```
> يستدعي `System.arraycopy` لنسخ من `xOnlyBytes` بدءاً من 0 إلى `compressedBytes` بدءاً من 1 بطول 32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:172]

```
173:             return secp256k1Curve.curve.decodePoint(compressedBytes)
```
> يُعيد نتيجة `secp256k1Curve.curve.decodePoint(compressedBytes)`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:173]

```
174:         }
```
> إغلاق نطاق (نهاية كتلة `catch`). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:174]

```
175:     }
```
> إغلاق نطاق (نهاية دالة `recoverPublicKeyPoint`). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:175]

```
176: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:176]

```
177:     private fun recoverPublicKeyPointWithParity(xOnlyBytes: ByteArray, preferOddY: Boolean): ECPoint {
```
> يعرّف دالة خاصة باسم `recoverPublicKeyPointWithParity` تأخذ معاملاً `xOnlyBytes` من نوع `ByteArray` و`preferOddY` من نوع `Boolean` وتُعيد `ECPoint` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:177]

```
178:         require(xOnlyBytes.size == 32) { "X-only public key must be 32 bytes" }
```
> يستدعي `require` للتحقق من أن حجم `xOnlyBytes` يساوي 32، وإلا يرمي خطأ بالرسالة «X-only public key must be 32 bytes». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:178]

```
179:         val prefix: Byte = if (preferOddY) 0x03 else 0x02
```
> يعرّف متغيراً ثابتاً باسم `prefix` من نوع `Byte` ويضبط قيمته إلى 0x03 إذا كان `preferOddY` صحيحاً وإلا 0x02. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:179]

```
180:         val compressedBytes = ByteArray(33)
```
> يعرّف متغيراً ثابتاً باسم `compressedBytes` ويضبط قيمته إلى مصفوفة بايت بطول 33. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:180]

```
181:         compressedBytes[0] = prefix
```
> يضبط العنصر الأول من `compressedBytes` إلى قيمة `prefix`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:181]

```
182:         System.arraycopy(xOnlyBytes, 0, compressedBytes, 1, 32)
```
> يستدعي `System.arraycopy` لنسخ من `xOnlyBytes` بدءاً من 0 إلى `compressedBytes` بدءاً من 1 بطول 32. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:182]

```
183:         return secp256k1Curve.curve.decodePoint(compressedBytes)
```
> يُعيد نتيجة `secp256k1Curve.curve.decodePoint(compressedBytes)`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:183]

```
184:     }
```
> إغلاق نطاق (نهاية دالة `recoverPublicKeyPointWithParity`). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:184]

```
185:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:185]

```
186:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:186]

```
187:      * Compute the ECDH shared point (uncompressed) with an explicit parity choice for the x-only public key
```
> تعليق: «حساب نقطة ECDH المشتركة (غير المضغوطة) مع اختيار صريح للزوجية للمفتاح العام بإحداثي x فقط». [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:187]

```
188:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:188]

```
189:     private fun computeSharedPointWithParity(privateKeyHex: String, publicKeyHex: String, preferOddY: Boolean): ECPoint {
```
> يعرّف دالة خاصة باسم `computeSharedPointWithParity` تأخذ المعاملات `privateKeyHex` و`publicKeyHex` من نوع `String` و`preferOddY` من نوع `Boolean` وتُعيد `ECPoint` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:189]

```
190:         val privateKeyBytes = privateKeyHex.hexToByteArray()
```
> يعرّف متغيراً ثابتاً باسم `privateKeyBytes` ويضبط قيمته إلى نتيجة `privateKeyHex.hexToByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:190]

```
191:         val publicKeyBytes = publicKeyHex.hexToByteArray()
```
> يعرّف متغيراً ثابتاً باسم `publicKeyBytes` ويضبط قيمته إلى نتيجة `publicKeyHex.hexToByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:191]

```
192:         val privateKeyBigInt = BigInteger(1, privateKeyBytes)
```
> يعرّف متغيراً ثابتاً باسم `privateKeyBigInt` ويضبط قيمته إلى كائن `BigInteger` مبنيٍّ بالإشارة 1 والمصفوفة `privateKeyBytes`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:192]

```
193:         val point = recoverPublicKeyPointWithParity(publicKeyBytes, preferOddY)
```
> يعرّف متغيراً ثابتاً باسم `point` ويضبط قيمته إلى نتيجة استدعاء `recoverPublicKeyPointWithParity` بالوسيطين `publicKeyBytes` و`preferOddY`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:193]

```
194:         return point.multiply(privateKeyBigInt).normalize()
```
> يُعيد نتيجة `point.multiply(privateKeyBigInt).normalize()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:194]

```
195:     }
```
> إغلاق نطاق (نهاية دالة `computeSharedPointWithParity`). [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:195]

```
196:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:196]

```
197:     private fun compressedPoint(point: ECPoint): ByteArray {
```
> يعرّف دالة خاصة باسم `compressedPoint` تأخذ معاملاً `point` من نوع `ECPoint` وتُعيد `ByteArray` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:197]

```
198:         val normalized = point.normalize()
```
> يعرّف متغيراً ثابتاً باسم `normalized` ويضبط قيمته إلى نتيجة `point.normalize()`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:198]

```
199:         val x = normalized.xCoord.encoded
```
> يعرّف متغيراً ثابتاً باسم `x` ويضبط قيمته إلى `normalized.xCoord.encoded`. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:199]

```
200:         val prefix: Byte = if (hasEvenY(normalized)) 0x02 else 0x03
```
> يعرّف متغيراً ثابتاً باسم `prefix` من نوع `Byte` ويضبط قيمته إلى 0x02 إذا أعادت `hasEvenY(normalized)` صحيحاً وإلا 0x03. [app/src/main/java/com/bitchat/android/nostr/NostrCrypto.kt:200]
