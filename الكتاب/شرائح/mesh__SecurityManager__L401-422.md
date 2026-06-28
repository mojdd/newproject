# شريحة — app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt (الأسطر 401–422)

```
401:         processedMessages.clear()
```
> يستدعي الدالة clear على المجموعة processedMessages (الرسائل المُعالَجة) لتفريغ كل عناصرها. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:401]

```
402:         processedKeyExchanges.clear()
```
> يستدعي الدالة clear على المجموعة processedKeyExchanges (تبادلات المفاتيح المُعالَجة) لتفريغ كل عناصرها. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:402]

```
403:         messageTimestamps.clear()
```
> يستدعي الدالة clear على المجموعة messageTimestamps (طوابع زمن الرسائل) لتفريغ كل عناصرها. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:403]

```
404:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:404]

```
405:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:405]

```
406:     /**
```
> تعليق: بداية كتلة توثيق (تعليق توثيقي متعدد الأسطر). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:406]

```
407:      * Shutdown the manager
```
> تعليق: إيقاف المدير. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:407]

```
408:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:408]

```
409:     fun shutdown() {
```
> يعرّف الدالة shutdown (الإيقاف) بلا وُسطاء ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:409]

```
410:         managerScope.cancel()
```
> يستدعي الدالة cancel على الكائن managerScope (نطاق المدير) لإلغائه. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:410]

```
411:         clearAllData()
```
> يستدعي الدالة clearAllData (مسح كل البيانات) بلا وُسطاء. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:411]

```
412:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:412]

```
413: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:413]

```
414: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:414]

```
415: /**
```
> تعليق: بداية كتلة توثيق (تعليق توثيقي متعدد الأسطر). [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:415]

```
416:  * Delegate interface for security manager callbacks
```
> تعليق: واجهة المفوَّض لاستدعاءات مدير الأمان الراجعة. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:416]

```
417:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:417]

```
418: interface SecurityManagerDelegate {
```
> يعرّف الواجهة SecurityManagerDelegate (مفوَّض مدير الأمان) ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:418]

```
419:     fun onKeyExchangeCompleted(peerID: String, peerPublicKeyData: ByteArray)
```
> يصرّح بالدالة المجرّدة onKeyExchangeCompleted (عند اكتمال تبادل المفاتيح) ذات الوسيطين peerID (مُعرِّف النِّد) من نوع String وpeerPublicKeyData (بيانات المفتاح العام للنِّد) من نوع ByteArray دون جسم. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:419]

```
420:     fun sendHandshakeResponse(peerID: String, response: ByteArray)
```
> يصرّح بالدالة المجرّدة sendHandshakeResponse (إرسال رد المصافحة) ذات الوسيطين peerID من نوع String وresponse (الرد) من نوع ByteArray دون جسم. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:420]

```
421:     fun getPeerInfo(peerID: String): PeerInfo? // NEW: For signature verification
```
> يصرّح بالدالة المجرّدة getPeerInfo (الحصول على معلومات النِّد) ذات الوسيط peerID من نوع String وتُعيد قيمة من نوع PeerInfo القابل للقيمة الفارغة، مع تعليق نهائي: «جديد: للتحقق من التوقيع». [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:421]

```
422: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/SecurityManager.kt:422]
