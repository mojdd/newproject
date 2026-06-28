# شريحة — app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف Log من حزمة android.util. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:3]

```
4: import java.security.MessageDigest
```
> يستورد الصنف ملخّص الرسالة (MessageDigest) من حزمة java.security. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:4]

```
5: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف الخريطة المتزامنة (ConcurrentHashMap) من حزمة java.util.concurrent. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:6]

```
7: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:7]

```
8:  * Centralized peer fingerprint management singleton
```
> تعليق: مفردة مركزية لإدارة بصمة النِّد. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:8]

```
9:  * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:9]

```
10:  * This class manages all peer fingerprint storage and retrieval operations, 
```
> تعليق: هذا الصنف يدير كل عمليات تخزين واسترجاع بصمة النِّد. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:10]

```
11:  * providing a single source of truth for peer identity across the entire application.
```
> تعليق: يوفّر مصدراً واحداً للحقيقة لهوية النِّد عبر كامل التطبيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:11]

```
12:  * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:12]

```
13:  * Fingerprints are SHA-256 hashes of peer static public keys and are only stored 
```
> تعليق: البصمات هي تجزئات SHA-256 للمفاتيح العامة الساكنة للنِّد ولا تُخزَّن إلا. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:13]

```
14:  * after successful Noise handshake session establishment.
```
> تعليق: بعد إنشاء جلسة مصافحة Noise بنجاح. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:14]

```
15:  * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:15]

```
16:  * Key Design Principles:
```
> تعليق: مبادئ التصميم الأساسية. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:16]

```
17:  * - Thread-safe operations using ConcurrentHashMap
```
> تعليق: عمليات آمنة من حيث الخيوط باستعمال ConcurrentHashMap. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:17]

```
18:  * - Bidirectional mapping (peerID ↔ fingerprint) 
```
> تعليق: ربط ثنائي الاتجاه (peerID ↔ fingerprint). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:18]

```
19:  * - Support for peer ID rotation while maintaining persistent identity
```
> تعليق: دعم تدوير معرّف النِّد مع الحفاظ على هوية ثابتة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:19]

```
20:  * - Centralized logging for debugging identity management
```
> تعليق: تسجيل مركزي لتنقيح إدارة الهوية. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:20]

```
21:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:21]

```
22: class PeerFingerprintManager private constructor() {
```
> يعرّف الصنف مدير بصمة النِّد (PeerFingerprintManager) مع بانٍ (constructor) خاص بلا وُسطاء، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:22]

```
23:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:23]

```
24:     companion object {
```
> يعرّف كائناً مرافقاً (companion object) ويفتح جسمه. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:24]

```
25:         private const val TAG = "PeerFingerprintManager"
```
> يعرّف ثابتاً خاصاً اسمه TAG وقيمته السلسلة النصية "PeerFingerprintManager". [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:25]

```
26:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:26]

```
27:         @Volatile
```
> يضع التعليق التوضيحي (annotation) المتطاير @Volatile على المعرّف الذي يليه. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:27]

```
28:         private var INSTANCE: PeerFingerprintManager? = null
```
> يعرّف متغيراً خاصاً اسمه INSTANCE من نوع PeerFingerprintManager القابل للعدم وقيمته الابتدائية null. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:28]

```
29:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:29]

```
30:         /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:30]

```
31:          * Get the singleton instance
```
> تعليق: احصل على نسخة المفردة الوحيدة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:31]

```
32:          */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:32]

```
33:         fun getInstance(): PeerFingerprintManager {
```
> يعرّف دالة اسمها getInstance تُعيد قيمة من نوع PeerFingerprintManager، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:33]

```
34:             return INSTANCE ?: synchronized(this) {
```
> يعيد INSTANCE، وإن كان null فيدخل كتلة متزامنة (synchronized) على this. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:34]

```
35:                 INSTANCE ?: PeerFingerprintManager().also { INSTANCE = it }
```
> يعيد INSTANCE، وإن كان null فينشئ كائن PeerFingerprintManager جديداً ويسند هذا الكائن إلى INSTANCE عبر also. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:35]

```
36:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:36]

```
37:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:37]

```
38:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:38]

```
39:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:39]

```
40:     // Bidirectional mapping for efficient lookups
```
> تعليق: ربط ثنائي الاتجاه لعمليات بحث فعّالة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:40]

```
41:     private val peerIDToFingerprint = ConcurrentHashMap<String, String>() // peerID -> fingerprint
```
> يعرّف متغيراً ثابتاً خاصاً اسمه peerIDToFingerprint وقيمته خريطة متزامنة جديدة من String إلى String، والتعليق: peerID إلى fingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:41]

```
42:     private val fingerprintToPeerID = ConcurrentHashMap<String, String>() // fingerprint -> current peerID
```
> يعرّف متغيراً ثابتاً خاصاً اسمه fingerprintToPeerID وقيمته خريطة متزامنة جديدة من String إلى String، والتعليق: fingerprint إلى peerID الحالي. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:42]

```
43:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:43]

```
44:     // MARK: - Fingerprint Storage (Only called after successful Noise handshake)
```
> تعليق: علامة: تخزين البصمة (لا يُستدعى إلا بعد مصافحة Noise ناجحة). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:44]

```
45:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:45]

```
46:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:46]

```
47:      * Store fingerprint mapping after successful Noise handshake session establishment
```
> تعليق: خزّن ربط البصمة بعد إنشاء جلسة مصافحة Noise بنجاح. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:47]

```
48:      * This is the ONLY place where fingerprints should be stored
```
> تعليق: هذا هو المكان الوحيد الذي ينبغي أن تُخزَّن فيه البصمات. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:48]

```
49:      * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:49]

```
50:      * @param peerID The peer's current ID
```
> تعليق: الوسيط peerID هو المعرّف الحالي للنِّد. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:50]

```
51:      * @param publicKey The peer's static public key from Noise handshake
```
> تعليق: الوسيط publicKey هو المفتاح العام الساكن للنِّد من مصافحة Noise. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:51]

```
52:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:52]

```
53:     fun storeFingerprintForPeer(peerID: String, publicKey: ByteArray): String {
```
> يعرّف دالة اسمها storeFingerprintForPeer تأخذ وسيطاً peerID من نوع String ووسيطاً publicKey من نوع ByteArray وتُعيد String، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:53]

```
54:         // get existing fingerprint for this peer and compare
```
> تعليق: احصل على البصمة الموجودة لهذا النِّد وقارن. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:54]

```
55:         val existingFingerprint = getFingerprintForPeer(peerID)
```
> يعرّف متغيراً ثابتاً اسمه existingFingerprint وقيمته نتيجة استدعاء getFingerprintForPeer بالوسيط peerID. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:55]

```
56:         val fingerprint = calculateFingerprint(publicKey)
```
> يعرّف متغيراً ثابتاً اسمه fingerprint وقيمته نتيجة استدعاء calculateFingerprint بالوسيط publicKey. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:56]

```
57: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:57]

```
58:         if (existingFingerprint != null && existingFingerprint != fingerprint) {
```
> يبدأ شرطاً: إذا كان existingFingerprint غير null وكان مختلفاً عن fingerprint، يفتح جسم الشرط. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:58]

```
59:             Log.w(TAG, "Fingerprint mismatch for peer $peerID: $existingFingerprint != $fingerprint")
```
> يستدعي Log.w بالوسم TAG ورسالة تحذير نصها "Fingerprint mismatch for peer $peerID: $existingFingerprint != $fingerprint" مع إدراج قيم peerID وexistingFingerprint وfingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:59]

```
60:             throw IllegalStateException("Fingerprint mismatch for peer $peerID: $existingFingerprint != $fingerprint")
```
> يرمي استثناء IllegalStateException برسالة "Fingerprint mismatch for peer $peerID: $existingFingerprint != $fingerprint" مع إدراج قيم peerID وexistingFingerprint وfingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:60]

```
61:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:61]

```
62:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:62]

```
63:         // Store bidirectional mapping
```
> تعليق: خزّن الربط ثنائي الاتجاه. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:63]

```
64:         peerIDToFingerprint[peerID] = fingerprint
```
> يسند القيمة fingerprint إلى المفتاح peerID في الخريطة peerIDToFingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:64]

```
65:         fingerprintToPeerID[fingerprint] = peerID
```
> يسند القيمة peerID إلى المفتاح fingerprint في الخريطة fingerprintToPeerID. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:65]

```
66:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:66]

```
67:         Log.d(TAG, "Stored fingerprint for peer $peerID: ${fingerprint.take(16)}...")
```
> يستدعي Log.d بالوسم TAG ورسالة تنقيح نصها "Stored fingerprint for peer $peerID: ${fingerprint.take(16)}..." مع إدراج peerID وأول 16 محرفاً من fingerprint عبر take(16). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:67]

```
68:         return fingerprint
```
> يعيد قيمة fingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:68]

```
69:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:69]

```
70:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:70]

```
71:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:71]

```
72:      * Update peer ID mapping while preserving fingerprint identity
```
> تعليق: حدّث ربط معرّف النِّد مع الحفاظ على هوية البصمة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:72]

```
73:      * Used for peer ID rotation - when a peer changes their ID but maintains the same static key
```
> تعليق: يُستعمل لتدوير معرّف النِّد - عندما يغيّر النِّد معرّفه لكن يبقي المفتاح الساكن نفسه. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:73]

```
74:      * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:74]

```
75:      * @param oldPeerID The previous peer ID (nullable if this is a fresh mapping)
```
> تعليق: الوسيط oldPeerID هو معرّف النِّد السابق (قابل للعدم إن كان هذا ربطاً جديداً). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:75]

```
76:      * @param newPeerID The new peer ID
```
> تعليق: الوسيط newPeerID هو معرّف النِّد الجديد. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:76]

```
77:      * @param fingerprint The persistent fingerprint (should match existing one)
```
> تعليق: الوسيط fingerprint هو البصمة الثابتة (ينبغي أن تطابق الموجودة). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:77]

```
78:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:78]

```
79:     fun updatePeerIDMapping(oldPeerID: String?, newPeerID: String, fingerprint: String) {
```
> يعرّف دالة اسمها updatePeerIDMapping تأخذ oldPeerID من نوع String القابل للعدم وnewPeerID من نوع String وfingerprint من نوع String، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:79]

```
80:         if (newPeerID.isBlank()) {
```
> يبدأ شرطاً: إذا كان newPeerID فارغاً أو فراغات فقط (isBlank)، يفتح جسم الشرط. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:80]

```
81:             Log.w(TAG, "Attempted to update mapping with blank newPeerID")
```
> يستدعي Log.w بالوسم TAG ورسالة تحذير نصها "Attempted to update mapping with blank newPeerID". [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:81]

```
82:             return
```
> يعيد (يخرج من الدالة) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:82]

```
83:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:83]

```
84:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:84]

```
85:         if (fingerprint.isBlank()) {
```
> يبدأ شرطاً: إذا كان fingerprint فارغاً أو فراغات فقط (isBlank)، يفتح جسم الشرط. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:85]

```
86:             Log.w(TAG, "Attempted to update mapping with blank fingerprint")
```
> يستدعي Log.w بالوسم TAG ورسالة تحذير نصها "Attempted to update mapping with blank fingerprint". [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:86]

```
87:             return
```
> يعيد (يخرج من الدالة) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:87]

```
88:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:88]

```
89:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:89]

```
90:         // Remove old mapping if exists
```
> تعليق: أزل الربط القديم إن وُجِد. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:90]

```
91:         oldPeerID?.takeIf { it.isNotBlank() }?.let { oldID ->
```
> على oldPeerID (إن لم يكن null) يطبّق takeIf الذي يبقيه إن كان غير فارغ (isNotBlank)، ثم let التي تسمّي القيمة oldID وتفتح كتلتها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:91]

```
92:             val removedFingerprint = peerIDToFingerprint.remove(oldID)
```
> يعرّف متغيراً ثابتاً اسمه removedFingerprint وقيمته نتيجة إزالة المفتاح oldID من الخريطة peerIDToFingerprint عبر remove. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:92]

```
93:             if (removedFingerprint != null && removedFingerprint == fingerprint) {
```
> يبدأ شرطاً: إذا كان removedFingerprint غير null ويساوي fingerprint، يفتح جسم الشرط. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:93]

```
94:                 Log.d(TAG, "Removed old mapping: $oldID -> ${removedFingerprint.take(16)}...")
```
> يستدعي Log.d بالوسم TAG ورسالة تنقيح نصها "Removed old mapping: $oldID -> ${removedFingerprint.take(16)}..." مع إدراج oldID وأول 16 محرفاً من removedFingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:94]

```
95:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:95]

```
96:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:96]

```
97:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:97]

```
98:         // Add new mapping
```
> تعليق: أضف الربط الجديد. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:98]

```
99:         peerIDToFingerprint[newPeerID] = fingerprint
```
> يسند القيمة fingerprint إلى المفتاح newPeerID في الخريطة peerIDToFingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:99]

```
100:         fingerprintToPeerID[fingerprint] = newPeerID
```
> يسند القيمة newPeerID إلى المفتاح fingerprint في الخريطة fingerprintToPeerID. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:100]

```
101:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:101]

```
102:         Log.d(TAG, "Updated peer ID mapping: $newPeerID (was: $oldPeerID), fingerprint: ${fingerprint.take(16)}...")
```
> يستدعي Log.d بالوسم TAG ورسالة تنقيح نصها "Updated peer ID mapping: $newPeerID (was: $oldPeerID), fingerprint: ${fingerprint.take(16)}..." مع إدراج newPeerID وoldPeerID وأول 16 محرفاً من fingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:102]

```
103:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:103]

```
104:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:104]

```
105:     // MARK: - Fingerprint Retrieval
```
> تعليق: علامة: استرجاع البصمة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:105]

```
106:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:106]

```
107:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:107]

```
108:      * Get fingerprint for a specific peer ID
```
> تعليق: احصل على بصمة لمعرّف نِّد محدد. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:108]

```
109:      * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:109]

```
110:      * @param peerID The peer ID to look up
```
> تعليق: الوسيط peerID هو معرّف النِّد المراد البحث عنه. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:110]

```
111:      * @return The fingerprint if found, null otherwise
```
> تعليق: يعيد البصمة إن وُجِدت، وإلا null. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:111]

```
112:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:112]

```
113:     fun getFingerprintForPeer(peerID: String): String? {
```
> يعرّف دالة اسمها getFingerprintForPeer تأخذ peerID من نوع String وتُعيد String القابل للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:113]

```
114:         if (peerID.isBlank()) return null
```
> إذا كان peerID فارغاً أو فراغات فقط (isBlank) فيعيد null. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:114]

```
115:         return peerIDToFingerprint[peerID]
```
> يعيد القيمة المرتبطة بالمفتاح peerID من الخريطة peerIDToFingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:115]

```
116:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:116]

```
117:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:117]

```
118:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:118]

```
119:      * Get current peer ID for a specific fingerprint
```
> تعليق: احصل على معرّف النِّد الحالي لبصمة محددة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:119]

```
120:      * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:120]

```
121:      * @param fingerprint The fingerprint to look up
```
> تعليق: الوسيط fingerprint هو البصمة المراد البحث عنها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:121]

```
122:      * @return The current peer ID if found, null otherwise
```
> تعليق: يعيد معرّف النِّد الحالي إن وُجِد، وإلا null. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:122]

```
123:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:123]

```
124:     fun getPeerIDForFingerprint(fingerprint: String): String? {
```
> يعرّف دالة اسمها getPeerIDForFingerprint تأخذ fingerprint من نوع String وتُعيد String القابل للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:124]

```
125:         if (fingerprint.isBlank()) return null
```
> إذا كان fingerprint فارغاً أو فراغات فقط (isBlank) فيعيد null. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:125]

```
126:         return fingerprintToPeerID[fingerprint]
```
> يعيد القيمة المرتبطة بالمفتاح fingerprint من الخريطة fingerprintToPeerID. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:126]

```
127:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:127]

```
128:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:128]

```
129:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:129]

```
130:      * Check if we have a fingerprint for a specific peer
```
> تعليق: تحقق إن كانت لدينا بصمة لنِّد محدد. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:130]

```
131:      * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:131]

```
132:      * @param peerID The peer ID to check
```
> تعليق: الوسيط peerID هو معرّف النِّد المراد التحقق منه. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:132]

```
133:      * @return True if we have a fingerprint for this peer, false otherwise
```
> تعليق: يعيد true إن كانت لدينا بصمة لهذا النِّد، وإلا false. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:133]

```
134:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:134]

```
135:     fun hasFingerprintForPeer(peerID: String): Boolean {
```
> يعرّف دالة اسمها hasFingerprintForPeer تأخذ peerID من نوع String وتُعيد Boolean، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:135]

```
136:         return getFingerprintForPeer(peerID) != null
```
> يعيد نتيجة المقارنة: هل نتيجة استدعاء getFingerprintForPeer بالوسيط peerID غير null. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:136]

```
137:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:137]

```
138:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:138]

```
139:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:139]

```
140:      * Get all current peer ID to fingerprint mappings
```
> تعليق: احصل على كل روابط معرّف النِّد إلى البصمة الحالية. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:140]

```
141:      * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:141]

```
142:      * @return Immutable copy of all mappings
```
> تعليق: يعيد نسخة غير قابلة للتغيير من كل الروابط. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:142]

```
143:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:143]

```
144:     fun getAllPeerFingerprints(): Map<String, String> {
```
> يعرّف دالة اسمها getAllPeerFingerprints تُعيد Map من String إلى String، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:144]

```
145:         return peerIDToFingerprint.toMap()
```
> يعيد نسخة خريطة من peerIDToFingerprint عبر toMap. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:145]

```
146:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:146]

```
147:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:147]

```
148:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:148]

```
149:      * Get all current fingerprint to peer ID mappings
```
> تعليق: احصل على كل روابط البصمة إلى معرّف النِّد الحالية. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:149]

```
150:      * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:150]

```
151:      * @return Immutable copy of all reverse mappings
```
> تعليق: يعيد نسخة غير قابلة للتغيير من كل الروابط العكسية. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:151]

```
152:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:152]

```
153:     fun getAllFingerprintMappings(): Map<String, String> {
```
> يعرّف دالة اسمها getAllFingerprintMappings تُعيد Map من String إلى String، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:153]

```
154:         return fingerprintToPeerID.toMap()
```
> يعيد نسخة خريطة من fingerprintToPeerID عبر toMap. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:154]

```
155:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:155]

```
156:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:156]

```
157:     // MARK: - Peer Management
```
> تعليق: علامة: إدارة النِّد. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:157]

```
158:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:158]

```
159:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:159]

```
160:      * Remove all mappings for a specific peer (called when peer disconnects)
```
> تعليق: أزل كل الروابط لنِّد محدد (يُستدعى عند انفصال النِّد). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:160]

```
161:      * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:161]

```
162:      * @param peerID The peer ID to remove
```
> تعليق: الوسيط peerID هو معرّف النِّد المراد إزالته. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:162]

```
163:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:163]

```
164:     fun removePeer(peerID: String) {
```
> يعرّف دالة اسمها removePeer تأخذ peerID من نوع String ولا تُعيد قيمة، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:164]

```
165:         if (peerID.isBlank()) return
```
> إذا كان peerID فارغاً أو فراغات فقط (isBlank) فيعيد (يخرج) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:165]

```
166:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:166]

```
167:         val fingerprint = peerIDToFingerprint.remove(peerID)
```
> يعرّف متغيراً ثابتاً اسمه fingerprint وقيمته نتيجة إزالة المفتاح peerID من الخريطة peerIDToFingerprint عبر remove. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:167]

```
168:         if (fingerprint != null) {
```
> يبدأ شرطاً: إذا كان fingerprint غير null، يفتح جسم الشرط. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:168]

```
169:             fingerprintToPeerID.remove(fingerprint)
```
> يزيل المفتاح fingerprint من الخريطة fingerprintToPeerID عبر remove. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:169]

```
170:             Log.d(TAG, "Removed peer mappings for $peerID: ${fingerprint.take(16)}...")
```
> يستدعي Log.d بالوسم TAG ورسالة تنقيح نصها "Removed peer mappings for $peerID: ${fingerprint.take(16)}..." مع إدراج peerID وأول 16 محرفاً من fingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:170]

```
171:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:171]

```
172:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:172]

```
173:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:173]

```
174:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:174]

```
175:      * Remove all mappings for a specific fingerprint
```
> تعليق: أزل كل الروابط لبصمة محددة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:175]

```
176:      * 
```
> تعليق: سطر توثيق فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:176]

```
177:      * @param fingerprint The fingerprint to remove
```
> تعليق: الوسيط fingerprint هو البصمة المراد إزالتها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:177]

```
178:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:178]

```
179:     fun removeFingerprint(fingerprint: String) {
```
> يعرّف دالة اسمها removeFingerprint تأخذ fingerprint من نوع String ولا تُعيد قيمة، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:179]

```
180:         if (fingerprint.isBlank()) return
```
> إذا كان fingerprint فارغاً أو فراغات فقط (isBlank) فيعيد (يخرج) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:180]

```
181:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:181]

```
182:         val peerID = fingerprintToPeerID.remove(fingerprint)
```
> يعرّف متغيراً ثابتاً اسمه peerID وقيمته نتيجة إزالة المفتاح fingerprint من الخريطة fingerprintToPeerID عبر remove. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:182]

```
183:         if (peerID != null) {
```
> يبدأ شرطاً: إذا كان peerID غير null، يفتح جسم الشرط. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:183]

```
184:             peerIDToFingerprint.remove(peerID)
```
> يزيل المفتاح peerID من الخريطة peerIDToFingerprint عبر remove. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:184]

```
185:             Log.d(TAG, "Removed fingerprint mappings for ${fingerprint.take(16)}...: $peerID")
```
> يستدعي Log.d بالوسم TAG ورسالة تنقيح نصها "Removed fingerprint mappings for ${fingerprint.take(16)}...: $peerID" مع إدراج أول 16 محرفاً من fingerprint وقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:185]

```
186:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:186]

```
187:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:187]

```
188:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:188]

```
189:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:189]

```
190:      * Clear all fingerprint mappings (used for emergency clear/panic mode)
```
> تعليق: امسح كل روابط البصمة (يُستعمل للمسح الطارئ/وضع الذعر). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:190]

```
191:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:191]

```
192:     fun clearAllFingerprints() {
```
> يعرّف دالة اسمها clearAllFingerprints بلا وُسطاء ولا تُعيد قيمة، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:192]

```
193:         val count = peerIDToFingerprint.size
```
> يعرّف متغيراً ثابتاً اسمه count وقيمته حجم (size) الخريطة peerIDToFingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:193]

```
194:         peerIDToFingerprint.clear()
```
> يمسح كل عناصر الخريطة peerIDToFingerprint عبر clear. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:194]

```
195:         fingerprintToPeerID.clear()
```
> يمسح كل عناصر الخريطة fingerprintToPeerID عبر clear. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:195]

```
196:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:196]

```
197:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:197]

```
198:     // MARK: - Utility Functions
```
> تعليق: علامة: دوال مساعدة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:198]

```
199:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:199]

```
200:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:200]
