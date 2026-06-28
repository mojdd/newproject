# شريحة — app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt (الأسطر 201–246)

```
201:      * Calculate SHA-256 fingerprint from public key
```
> تعليق: احسب البصمة (fingerprint) بخوارزمية SHA-256 من المفتاح العام (public key). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:201]

```
202:      * 
```
> تعليق: سطر تعليق فارغ (يحوي مسافة فقط). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:202]

```
203:      * @param publicKey The peer's static public key
```
> تعليق: المعامل publicKey هو المفتاح العام الثابت (static public key) للنظير (peer). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:203]

```
204:      * @return The hex-encoded SHA-256 hash
```
> تعليق: القيمة المُعادة هي تجزئة (hash) SHA-256 مُرمَّزة بالنظام الست عشري (hex-encoded). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:204]

```
205:      */
```
> تعليق: إغلاق كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:205]

```
206:     private fun calculateFingerprint(publicKey: ByteArray): String {
```
> تُعرَّف دالة خاصة (private) اسمها حساب البصمة (calculateFingerprint) تأخذ معاملاً publicKey من نوع مصفوفة بايتات (ByteArray) وتُعيد قيمة من نوع نص (String). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:206]

```
207:         val digest = MessageDigest.getInstance("SHA-256")
```
> يُعرَّف متغير ثابت اسمه digest يُضبَط بنتيجة استدعاء MessageDigest.getInstance بوسيط نصّه "SHA-256". [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:207]

```
208:         val hash = digest.digest(publicKey)
```
> يُعرَّف متغير ثابت اسمه hash يُضبَط بنتيجة استدعاء الدالة digest على الكائن digest وتمرير publicKey إليها. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:208]

```
209:         return hash.joinToString("") { "%02x".format(it) }
```
> يُعاد ناتج استدعاء joinToString على hash بفاصل نصّه فارغ ""، حيث يُحوَّل كل عنصر it بالاستدعاء "%02x".format(it). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:209]

```
210:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:210]

```
211:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:211]

```
212:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:212]

```
213:      * Get debug information about current fingerprint mappings
```
> تعليق: احصل على معلومات تنقيح (debug information) عن خرائط البصمات (fingerprint mappings) الحالية. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:213]

```
214:      * 
```
> تعليق: سطر تعليق فارغ (يحوي مسافة فقط). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:214]

```
215:      * @return Debug string with mapping counts and summary
```
> تعليق: القيمة المُعادة هي نص تنقيح (debug string) يحوي عدد الخرائط (mapping counts) وملخصاً (summary). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:215]

```
216:      */
```
> تعليق: إغلاق كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:216]

```
217:     fun getDebugInfo(): String {
```
> تُعرَّف دالة اسمها الحصول على معلومات التنقيح (getDebugInfo) بلا معاملات وتُعيد قيمة من نوع نص (String). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:217]

```
218:         return buildString {
```
> يُعاد ناتج استدعاء buildString مع تمرير دالة لامبدا (lambda) تبدأ هنا. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:218]

```
219:             appendLine("=== PeerFingerprintManager Debug Info ===")
```
> يُستدعى appendLine بوسيط نصّه "=== PeerFingerprintManager Debug Info ===". [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:219]

```
220:             appendLine("Total mappings: ${peerIDToFingerprint.size}")
```
> يُستدعى appendLine بنص يبدأ بـ "Total mappings: " متبوعاً بقيمة peerIDToFingerprint.size المُدرَجة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:220]

```
221:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:221]

```
222:             if (peerIDToFingerprint.isNotEmpty()) {
```
> تُفتَح جملة شرطية if شرطها استدعاء isNotEmpty على peerIDToFingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:222]

```
223:                 appendLine("Peer ID -> Fingerprint mappings:")
```
> يُستدعى appendLine بوسيط نصّه "Peer ID -> Fingerprint mappings:". [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:223]

```
224:                 peerIDToFingerprint.forEach { (peerID, fingerprint) ->
```
> يُستدعى forEach على peerIDToFingerprint مع لامبدا تفكّك كل عنصر إلى peerID وfingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:224]

```
225:                     appendLine("  $peerID -> ${fingerprint.take(16)}...")
```
> يُستدعى appendLine بنص يبدأ بمسافتين ثم قيمة peerID ثم " -> " ثم ناتج fingerprint.take(16) ثم "...". [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:225]

```
226:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:226]

```
227:             } else {
```
> إغلاق فرع if وفتح فرع else. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:227]

```
228:                 appendLine("No fingerprint mappings stored")
```
> يُستدعى appendLine بوسيط نصّه "No fingerprint mappings stored". [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:228]

```
229:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:229]

```
230:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:230]

```
231:             // Verify bidirectional mapping consistency
```
> تعليق: تحقّق من اتساق (consistency) الخريطة ثنائية الاتجاه (bidirectional mapping). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:231]

```
232:             val inconsistentMappings = mutableListOf<String>()
```
> يُعرَّف متغير ثابت اسمه الخرائط غير المتسقة (inconsistentMappings) يُضبَط بقائمة قابلة للتعديل (mutableListOf) من نوع نص String فارغة. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:232]

```
233:             peerIDToFingerprint.forEach { (peerID, fingerprint) ->
```
> يُستدعى forEach على peerIDToFingerprint مع لامبدا تفكّك كل عنصر إلى peerID وfingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:233]

```
234:                 val reversePeerID = fingerprintToPeerID[fingerprint]
```
> يُعرَّف متغير ثابت اسمه معرّف النظير العكسي (reversePeerID) يُضبَط بقيمة fingerprintToPeerID عند المفتاح fingerprint. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:234]

```
235:                 if (reversePeerID != peerID) {
```
> تُفتَح جملة شرطية if شرطها أن reversePeerID لا يساوي peerID. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:235]

```
236:                     inconsistentMappings.add("$peerID -> $fingerprint -> $reversePeerID")
```
> يُستدعى add على inconsistentMappings بنص يجمع peerID ثم " -> " ثم fingerprint ثم " -> " ثم reversePeerID. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:236]

```
237:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:237]

```
238:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:238]

```
239:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:239]

```
240:             if (inconsistentMappings.isNotEmpty()) {
```
> تُفتَح جملة شرطية if شرطها استدعاء isNotEmpty على inconsistentMappings. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:240]

```
241:                 appendLine("⚠️ INCONSISTENT MAPPINGS DETECTED:")
```
> يُستدعى appendLine بوسيط نصّه "⚠️ INCONSISTENT MAPPINGS DETECTED:". [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:241]

```
242:                 inconsistentMappings.forEach { appendLine("  $it") }
```
> يُستدعى forEach على inconsistentMappings مع لامبدا تستدعي appendLine بنص فيه مسافتان ثم قيمة العنصر it. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:242]

```
243:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:243]

```
244:         }
```
> إغلاق نطاق (إغلاق لامبدا buildString). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:244]

```
245:     }
```
> إغلاق نطاق (إغلاق دالة getDebugInfo). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:245]

```
246: }
```
> إغلاق نطاق (إغلاق الصنف class). [app/src/main/java/com/bitchat/android/mesh/PeerFingerprintManager.kt:246]
