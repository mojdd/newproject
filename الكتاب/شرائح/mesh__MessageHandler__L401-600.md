# شريحة — app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt (الأسطر 401–600)

```
401:             val file = com.bitchat.android.model.BitchatFilePacket.decode(packet.payload)
```
> يُعرَّف متغيّر ثابت اسمه (file) ويُسنَد إليه ناتج استدعاء الدالة (decode) من الصنف (BitchatFilePacket) مع تمرير حمولة الرزمة (packet.payload). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:401]

```
402:             if (file != null) {
```
> شرط: إذا كان المتغيّر (file) لا يساوي القيمة الفارغة (null) فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:402]

```
403:                 if (isFileTransfer) {
```
> شرط: إذا كان المتغيّر (isFileTransfer) قيمته صحيحة فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:403]

```
404:                     Log.d(TAG, "📥 FILE_TRANSFER decode success (broadcast): name='${file.fileName}', size=${file.fileSize}, mime='${file.mimeType}', from=${peerID.take(8)}")
```
> يُستدعى التسجيل التشخيصي (Log.d) بالوسم (TAG) ونصّ يفيد بنجاح فكّ ترميز نقل الملف للبثّ، ويُدرج فيه اسم الملف (file.fileName) وحجمه (file.fileSize) ونوعه (file.mimeType) وأول ثمانية محارف من معرّف النِّدّ (peerID.take(8)). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:404]

```
405:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:405]

```
406:                 val savedPath = com.bitchat.android.features.file.FileUtils.saveIncomingFile(appContext, file)
```
> يُعرَّف متغيّر ثابت اسمه (savedPath) ويُسنَد إليه ناتج استدعاء الدالة (saveIncomingFile) من الأداة (FileUtils) مع تمرير سياق التطبيق (appContext) والملف (file). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:406]

```
407:                 val message = BitchatMessage(
```
> يُعرَّف متغيّر ثابت اسمه (message) ويُسنَد إليه كائن جديد من الصنف (BitchatMessage) مع فتح قائمة الوسائط. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:407]

```
408:                     id = PacketIdUtil.computeIdHex(packet).uppercase(),
```
> تُضبَط الوسيطة (id) على ناتج الدالة (computeIdHex) من الأداة (PacketIdUtil) للرزمة (packet) بعد تحويله إلى أحرف كبيرة (uppercase). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:408]

```
409:                     sender = delegate?.getPeerNickname(peerID) ?: "unknown",
```
> تُضبَط الوسيطة (sender) على ناتج استدعاء (getPeerNickname) من المفوَّض (delegate) بمعرّف النِّدّ (peerID)، وإن كان فارغاً فعلى السلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:409]

```
410:                     content = savedPath,
```
> تُضبَط الوسيطة (content) على قيمة المسار المحفوظ (savedPath). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:410]

```
411:                     type = com.bitchat.android.features.file.FileUtils.messageTypeForMime(file.mimeType),
```
> تُضبَط الوسيطة (type) على ناتج الدالة (messageTypeForMime) من الأداة (FileUtils) بتمرير نوع الملف (file.mimeType). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:411]

```
412:                     senderPeerID = peerID,
```
> تُضبَط الوسيطة (senderPeerID) على معرّف النِّدّ (peerID). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:412]

```
413:                     timestamp = Date(packet.timestamp.toLong())
```
> تُضبَط الوسيطة (timestamp) على كائن تاريخ (Date) مبنيّ من ختم وقت الرزمة (packet.timestamp) محوّلاً إلى عدد طويل (toLong). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:413]

```
414:                 )
```
> إغلاق قائمة وسائط الكائن. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:414]

```
415:                 Log.d(TAG, "📄 Saved incoming file to $savedPath")
```
> يُستدعى التسجيل التشخيصي (Log.d) بالوسم (TAG) ونصّ يفيد بحفظ الملف الوارد في المسار (savedPath). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:415]

```
416:                 delegate?.onMessageReceived(message)
```
> يُستدعى من المفوَّض (delegate) الدالة (onMessageReceived) مع تمرير الرسالة (message). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:416]

```
417:                 return
```
> يُعاد من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:417]

```
418:             } else if (isFileTransfer) {
```
> وإلا إذا كان المتغيّر (isFileTransfer) قيمته صحيحة فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:418]

```
419:                 Log.w(TAG, "⚠️ FILE_TRANSFER decode failed (broadcast) from ${peerID.take(8)} payloadSize=${packet.payload.size}")
```
> يُستدعى تسجيل التحذير (Log.w) بالوسم (TAG) ونصّ يفيد بفشل فكّ ترميز نقل الملف للبثّ من أول ثمانية محارف للنِّدّ (peerID.take(8)) مع حجم الحمولة (packet.payload.size). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:419]

```
420:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:420]

```
421: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:421]

```
422:             // Fallback: plain text
```
> تعليق: احتياطي: نصّ صِرف. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:422]

```
423:             val message = BitchatMessage(
```
> يُعرَّف متغيّر ثابت اسمه (message) ويُسنَد إليه كائن جديد من الصنف (BitchatMessage) مع فتح قائمة الوسائط. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:423]

```
424:                 id = PacketIdUtil.computeIdHex(packet).uppercase(),
```
> تُضبَط الوسيطة (id) على ناتج الدالة (computeIdHex) من الأداة (PacketIdUtil) للرزمة (packet) بعد تحويله إلى أحرف كبيرة (uppercase). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:424]

```
425:                 sender = delegate?.getPeerNickname(peerID) ?: "unknown",
```
> تُضبَط الوسيطة (sender) على ناتج استدعاء (getPeerNickname) من المفوَّض (delegate) بمعرّف النِّدّ (peerID)، وإن كان فارغاً فعلى السلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:425]

```
426:                 content = String(packet.payload, Charsets.UTF_8),
```
> تُضبَط الوسيطة (content) على سلسلة (String) مبنيّة من حمولة الرزمة (packet.payload) بترميز (UTF_8). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:426]

```
427:                 senderPeerID = peerID,
```
> تُضبَط الوسيطة (senderPeerID) على معرّف النِّدّ (peerID). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:427]

```
428:                 timestamp = Date(packet.timestamp.toLong())
```
> تُضبَط الوسيطة (timestamp) على كائن تاريخ (Date) مبنيّ من ختم وقت الرزمة (packet.timestamp) محوّلاً إلى عدد طويل (toLong). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:428]

```
429:             )
```
> إغلاق قائمة وسائط الكائن. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:429]

```
430:             delegate?.onMessageReceived(message)
```
> يُستدعى من المفوَّض (delegate) الدالة (onMessageReceived) مع تمرير الرسالة (message). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:430]

```
431:         } catch (e: Exception) {
```
> بدء كتلة التقاط الاستثناء (catch) للاستثناء (Exception) المسمّى (e). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:431]

```
432:             Log.e(TAG, "Failed to process broadcast message: ${e.message}")
```
> يُستدعى تسجيل الخطأ (Log.e) بالوسم (TAG) ونصّ يفيد بفشل معالجة رسالة البثّ مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:432]

```
433:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:433]

```
434:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:434]

```
435:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:435]

```
436:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:436]

```
437:      * Handle (decrypted) private message addressed to us
```
> تعليق: معالجة الرسالة الخاصة (المفكوكة التعمية) الموجَّهة إلينا. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:437]

```
438:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:438]

```
439:     private suspend fun handlePrivateMessage(packet: BitchatPacket, peerID: String) {
```
> تُعرَّف دالة خاصّة معلَّقة (suspend) اسمها (handlePrivateMessage) تأخذ رزمة (packet) من نوع (BitchatPacket) ومعرّف نِدّ (peerID) من نوع سلسلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:439]

```
440:         try {
```
> بدء كتلة المحاولة (try). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:440]

```
441:             // Verify signature if present
```
> تعليق: تحقَّق من التوقيع إن وُجد. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:441]

```
442:             if (packet.signature != null && !delegate?.verifySignature(packet, peerID)!!) {
```
> شرط: إذا كان توقيع الرزمة (packet.signature) لا يساوي الفارغ وكان نفي ناتج (verifySignature) من المفوَّض (delegate) للرزمة (packet) والنِّدّ (peerID) صحيحاً فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:442]

```
443:                 Log.w(TAG, "Invalid signature for private message from $peerID")
```
> يُستدعى تسجيل التحذير (Log.w) بالوسم (TAG) ونصّ يفيد بتوقيع غير صالح لرسالة خاصّة من النِّدّ (peerID). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:443]

```
444:                 return
```
> يُعاد من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:444]

```
445:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:445]

```
446: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:446]

```
447:             // Try file packet first (voice, image, etc.) and log outcome for FILE_TRANSFER
```
> تعليق: جرّب رزمة الملف أولاً (صوت، صورة، إلخ) وسجّل النتيجة لنقل الملف. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:447]

```
448:             val isFileTransfer = com.bitchat.android.protocol.MessageType.fromValue(packet.type) == com.bitchat.android.protocol.MessageType.FILE_TRANSFER
```
> يُعرَّف متغيّر ثابت اسمه (isFileTransfer) ويُسنَد إليه نتيجة المساواة بين ناتج (fromValue) من نوع الرسالة (MessageType) لنوع الرزمة (packet.type) والثابت (FILE_TRANSFER). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:448]

```
449:             val file = com.bitchat.android.model.BitchatFilePacket.decode(packet.payload)
```
> يُعرَّف متغيّر ثابت اسمه (file) ويُسنَد إليه ناتج استدعاء الدالة (decode) من الصنف (BitchatFilePacket) مع تمرير حمولة الرزمة (packet.payload). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:449]

```
450:             if (file != null) {
```
> شرط: إذا كان المتغيّر (file) لا يساوي القيمة الفارغة (null) فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:450]

```
451:                 if (isFileTransfer) {
```
> شرط: إذا كان المتغيّر (isFileTransfer) قيمته صحيحة فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:451]

```
452:                     Log.d(TAG, "📥 FILE_TRANSFER decode success (private): name='${file.fileName}', size=${file.fileSize}, mime='${file.mimeType}', from=${peerID.take(8)}")
```
> يُستدعى التسجيل التشخيصي (Log.d) بالوسم (TAG) ونصّ يفيد بنجاح فكّ ترميز نقل الملف للرسالة الخاصّة، ويُدرج فيه اسم الملف (file.fileName) وحجمه (file.fileSize) ونوعه (file.mimeType) وأول ثمانية محارف من النِّدّ (peerID.take(8)). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:452]

```
453:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:453]

```
454:                 val savedPath = com.bitchat.android.features.file.FileUtils.saveIncomingFile(appContext, file)
```
> يُعرَّف متغيّر ثابت اسمه (savedPath) ويُسنَد إليه ناتج استدعاء الدالة (saveIncomingFile) من الأداة (FileUtils) مع تمرير سياق التطبيق (appContext) والملف (file). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:454]

```
455:                 val message = BitchatMessage(
```
> يُعرَّف متغيّر ثابت اسمه (message) ويُسنَد إليه كائن جديد من الصنف (BitchatMessage) مع فتح قائمة الوسائط. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:455]

```
456:                     id = java.util.UUID.randomUUID().toString().uppercase(),
```
> تُضبَط الوسيطة (id) على معرّف عشوائي فريد (UUID.randomUUID) محوّلاً إلى سلسلة (toString) ثم إلى أحرف كبيرة (uppercase). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:456]

```
457:                     sender = delegate?.getPeerNickname(peerID) ?: "unknown",
```
> تُضبَط الوسيطة (sender) على ناتج استدعاء (getPeerNickname) من المفوَّض (delegate) بمعرّف النِّدّ (peerID)، وإن كان فارغاً فعلى السلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:457]

```
458:                     content = savedPath,
```
> تُضبَط الوسيطة (content) على قيمة المسار المحفوظ (savedPath). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:458]

```
459:                     type = com.bitchat.android.features.file.FileUtils.messageTypeForMime(file.mimeType),
```
> تُضبَط الوسيطة (type) على ناتج الدالة (messageTypeForMime) من الأداة (FileUtils) بتمرير نوع الملف (file.mimeType). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:459]

```
460:                     senderPeerID = peerID,
```
> تُضبَط الوسيطة (senderPeerID) على معرّف النِّدّ (peerID). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:460]

```
461:                     timestamp = Date(packet.timestamp.toLong()),
```
> تُضبَط الوسيطة (timestamp) على كائن تاريخ (Date) مبنيّ من ختم وقت الرزمة (packet.timestamp) محوّلاً إلى عدد طويل (toLong). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:461]

```
462:                     isPrivate = true,
```
> تُضبَط الوسيطة (isPrivate) على القيمة الصحيحة (true). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:462]

```
463:                     recipientNickname = delegate?.getMyNickname()
```
> تُضبَط الوسيطة (recipientNickname) على ناتج استدعاء (getMyNickname) من المفوَّض (delegate). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:463]

```
464:                 )
```
> إغلاق قائمة وسائط الكائن. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:464]

```
465:                 Log.d(TAG, "📄 Saved incoming file to $savedPath")
```
> يُستدعى التسجيل التشخيصي (Log.d) بالوسم (TAG) ونصّ يفيد بحفظ الملف الوارد في المسار (savedPath). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:465]

```
466:                 delegate?.onMessageReceived(message)
```
> يُستدعى من المفوَّض (delegate) الدالة (onMessageReceived) مع تمرير الرسالة (message). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:466]

```
467:                 return
```
> يُعاد من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:467]

```
468:             } else if (isFileTransfer) {
```
> وإلا إذا كان المتغيّر (isFileTransfer) قيمته صحيحة فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:468]

```
469:                 Log.w(TAG, "⚠️ FILE_TRANSFER decode failed (private) from ${peerID.take(8)} payloadSize=${packet.payload.size}")
```
> يُستدعى تسجيل التحذير (Log.w) بالوسم (TAG) ونصّ يفيد بفشل فكّ ترميز نقل الملف للرسالة الخاصّة من أول ثمانية محارف للنِّدّ (peerID.take(8)) مع حجم الحمولة (packet.payload.size). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:469]

```
470:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:470]

```
471: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:471]

```
472:             // Fallback: plain text
```
> تعليق: احتياطي: نصّ صِرف. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:472]

```
473:             val message = BitchatMessage(
```
> يُعرَّف متغيّر ثابت اسمه (message) ويُسنَد إليه كائن جديد من الصنف (BitchatMessage) مع فتح قائمة الوسائط. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:473]

```
474:                 sender = delegate?.getPeerNickname(peerID) ?: "unknown",
```
> تُضبَط الوسيطة (sender) على ناتج استدعاء (getPeerNickname) من المفوَّض (delegate) بمعرّف النِّدّ (peerID)، وإن كان فارغاً فعلى السلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:474]

```
475:                 content = String(packet.payload, Charsets.UTF_8),
```
> تُضبَط الوسيطة (content) على سلسلة (String) مبنيّة من حمولة الرزمة (packet.payload) بترميز (UTF_8). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:475]

```
476:                 senderPeerID = peerID,
```
> تُضبَط الوسيطة (senderPeerID) على معرّف النِّدّ (peerID). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:476]

```
477:                 timestamp = Date(packet.timestamp.toLong())
```
> تُضبَط الوسيطة (timestamp) على كائن تاريخ (Date) مبنيّ من ختم وقت الرزمة (packet.timestamp) محوّلاً إلى عدد طويل (toLong). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:477]

```
478:             )
```
> إغلاق قائمة وسائط الكائن. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:478]

```
479:             delegate?.onMessageReceived(message)
```
> يُستدعى من المفوَّض (delegate) الدالة (onMessageReceived) مع تمرير الرسالة (message). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:479]

```
480: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:480]

```
481:         } catch (e: Exception) {
```
> بدء كتلة التقاط الاستثناء (catch) للاستثناء (Exception) المسمّى (e). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:481]

```
482:             Log.e(TAG, "Failed to process private message from $peerID: ${e.message}")
```
> يُستدعى تسجيل الخطأ (Log.e) بالوسم (TAG) ونصّ يفيد بفشل معالجة رسالة خاصّة من النِّدّ (peerID) مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:482]

```
483:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:483]

```
484:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:484]

```
485: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:485]

```
486:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:486]

```
487:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:487]

```
488:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:488]

```
489:      * Handle leave message
```
> تعليق: معالجة رسالة المغادرة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:489]

```
490:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:490]

```
491:     suspend fun handleLeave(routed: RoutedPacket) {
```
> تُعرَّف دالة معلَّقة (suspend) اسمها (handleLeave) تأخذ رزمة موجَّهة (routed) من نوع (RoutedPacket). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:491]

```
492:         val packet = routed.packet
```
> يُعرَّف متغيّر ثابت اسمه (packet) ويُسنَد إليه الرزمة (routed.packet). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:492]

```
493:         val peerID = routed.peerID ?: "unknown"
```
> يُعرَّف متغيّر ثابت اسمه (peerID) ويُسنَد إليه معرّف النِّدّ (routed.peerID)، وإن كان فارغاً فالسلسلة "unknown". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:493]

```
494:         val content = String(packet.payload, Charsets.UTF_8)
```
> يُعرَّف متغيّر ثابت اسمه (content) ويُسنَد إليه سلسلة (String) مبنيّة من حمولة الرزمة (packet.payload) بترميز (UTF_8). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:494]

```
495:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:495]

```
496:         if (content.startsWith("#")) {
```
> شرط: إذا كان المحتوى (content) يبدأ بالمحرف "#" فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:496]

```
497:             // Channel leave
```
> تعليق: مغادرة القناة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:497]

```
498:             delegate?.onChannelLeave(content, peerID)
```
> يُستدعى من المفوَّض (delegate) الدالة (onChannelLeave) مع تمرير المحتوى (content) ومعرّف النِّدّ (peerID). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:498]

```
499:         } else {
```
> وإلا فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:499]

```
500:             // Peer disconnect
```
> تعليق: قطع اتصال النِّدّ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:500]

```
501:             delegate?.removePeer(peerID)
```
> يُستدعى من المفوَّض (delegate) الدالة (removePeer) مع تمرير معرّف النِّدّ (peerID). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:501]

```
502:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:502]

```
503:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:503]

```
504:         // Leave message relay is now handled by centralized PacketRelayManager
```
> تعليق: إعادة بثّ رسالة المغادرة تُعالَج الآن بواسطة مدير إعادة البثّ المركزي (PacketRelayManager). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:504]

```
505:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:505]

```
506:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:506]

```
507:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:507]

```
508:      * Get debug information
```
> تعليق: الحصول على معلومات التتبُّع. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:508]

```
509:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:509]

```
510:     fun getDebugInfo(): String {
```
> تُعرَّف دالة اسمها (getDebugInfo) تُعيد قيمة من نوع سلسلة (String). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:510]

```
511:         return buildString {
```
> يُعاد ناتج باني السلسلة (buildString) مع فتح كتلة البناء. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:511]

```
512:             appendLine("=== Message Handler Debug Info ===")
```
> يُستدعى (appendLine) لإلحاق سطر عنوانه "=== Message Handler Debug Info ===". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:512]

```
513:             appendLine("Handler Scope Active: ${handlerScope.isActive}")
```
> يُستدعى (appendLine) لإلحاق سطر يبيّن حالة نشاط نطاق المعالِج (handlerScope.isActive). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:513]

```
514:             appendLine("My Peer ID: $myPeerID")
```
> يُستدعى (appendLine) لإلحاق سطر يبيّن معرّف نِدّي (myPeerID). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:514]

```
515:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:515]

```
516:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:516]

```
517:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:517]

```
518:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:518]

```
519:      * Convert hex string peer ID to binary data (8 bytes) - same as iOS implementation
```
> تعليق: تحويل معرّف النِّدّ النصّي الستّ عشري إلى بيانات ثنائية (ثمانية بايتات) — مماثل لتنفيذ نظام آي أو إس. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:519]

```
520:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:520]

```
521:     private fun hexStringToByteArray(hexString: String): ByteArray {
```
> تُعرَّف دالة خاصّة اسمها (hexStringToByteArray) تأخذ سلسلة ستّ عشرية (hexString) وتُعيد مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:521]

```
522:         val result = ByteArray(8) { 0 } // Initialize with zeros, exactly 8 bytes
```
> يُعرَّف متغيّر ثابت اسمه (result) ويُسنَد إليه مصفوفة بايتات بطول ثمانية كلّ عناصرها صفر، مع تعليق: التهيئة بالأصفار، ثمانية بايتات بالضبط. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:522]

```
523:         var tempID = hexString
```
> يُعرَّف متغيّر متبدّل اسمه (tempID) ويُسنَد إليه السلسلة (hexString). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:523]

```
524:         var index = 0
```
> يُعرَّف متغيّر متبدّل اسمه (index) ويُسنَد إليه القيمة صفر. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:524]

```
525:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:525]

```
526:         while (tempID.length >= 2 && index < 8) {
```
> حلقة ما دام (while): تتكرّر ما دام طول (tempID) أكبر من أو يساوي اثنين والمؤشّر (index) أصغر من ثمانية. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:526]

```
527:             val hexByte = tempID.substring(0, 2)
```
> يُعرَّف متغيّر ثابت اسمه (hexByte) ويُسنَد إليه أول محرفين من (tempID) عبر (substring) من صفر إلى اثنين. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:527]

```
528:             val byte = hexByte.toIntOrNull(16)?.toByte()
```
> يُعرَّف متغيّر ثابت اسمه (byte) ويُسنَد إليه تحويل (hexByte) إلى عدد صحيح بالأساس ستة عشر (toIntOrNull) ثم إلى بايت (toByte)، وقد يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:528]

```
529:             if (byte != null) {
```
> شرط: إذا كان المتغيّر (byte) لا يساوي الفارغ فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:529]

```
530:                 result[index] = byte
```
> يُسنَد البايت (byte) إلى عنصر المصفوفة (result) عند المؤشّر (index). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:530]

```
531:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:531]

```
532:             tempID = tempID.substring(2)
```
> يُعاد إسناد (tempID) إلى ما تبقّى منه بعد إسقاط أول محرفين عبر (substring) ابتداءً من اثنين. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:532]

```
533:             index++
```
> يُزاد المؤشّر (index) بمقدار واحد. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:533]

```
534:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:534]

```
535:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:535]

```
536:         return result
```
> يُعاد المتغيّر (result). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:536]

```
537:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:537]

```
538: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:538]

```
539:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:539]

```
540:      * Shutdown the handler
```
> تعليق: إيقاف المعالِج. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:540]

```
541:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:541]

```
542:     fun shutdown() {
```
> تُعرَّف دالة اسمها (shutdown) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:542]

```
543:         handlerScope.cancel()
```
> يُستدعى من نطاق المعالِج (handlerScope) الدالة (cancel) لإلغائه. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:543]

```
544:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:544]

```
545: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:545]

```
546:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:546]

```
547:      * Handle favorite/unfavorite notification received over mesh as a private message.
```
> تعليق: معالجة إشعار التفضيل/إلغاء التفضيل الوارد عبر الشبكة المتشابكة كرسالة خاصّة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:547]

```
548:      * Content format: "[FAVORITED]:npub..." or "[UNFAVORITED]:npub..."
```
> تعليق: صيغة المحتوى: "[FAVORITED]:npub..." أو "[UNFAVORITED]:npub...". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:548]

```
549:      */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:549]

```
550:     private fun handleFavoriteNotificationFromMesh(content: String, fromPeerID: String) {
```
> تُعرَّف دالة خاصّة اسمها (handleFavoriteNotificationFromMesh) تأخذ محتوى (content) من نوع سلسلة ومعرّف النِّدّ المُرسِل (fromPeerID) من نوع سلسلة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:550]

```
551:         try {
```
> بدء كتلة المحاولة (try). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:551]

```
552:             val isFavorite = content.startsWith("[FAVORITED]")
```
> يُعرَّف متغيّر ثابت اسمه (isFavorite) ويُسنَد إليه نتيجة ما إذا كان المحتوى (content) يبدأ بالنصّ "[FAVORITED]". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:552]

```
553:             val npub = content.substringAfter(":", "").trim().takeIf { it.startsWith("npub1") }
```
> يُعرَّف متغيّر ثابت اسمه (npub) ويُسنَد إليه ما يلي أول نقطتين في المحتوى (substringAfter) بعد إزالة الفراغات (trim)، ويُؤخذ فقط إن بدأ بـ "npub1" وإلا فالقيمة فارغة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:553]

```
554: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:554]

```
555:             // Update mutual favorite status in persistence
```
> تعليق: تحديث حالة التفضيل المتبادل في التخزين الدائم. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:555]

```
556:             // Resolve full Noise key if available via delegate peer info
```
> تعليق: استخراج مفتاح نويز (Noise) الكامل إن توفّر عبر معلومات النِّدّ من المفوَّض. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:556]

```
557:             val peerInfo = delegate?.getPeerInfo(fromPeerID)
```
> يُعرَّف متغيّر ثابت اسمه (peerInfo) ويُسنَد إليه ناتج استدعاء (getPeerInfo) من المفوَّض (delegate) لمعرّف النِّدّ المُرسِل (fromPeerID). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:557]

```
558:             val noiseKey = peerInfo?.noisePublicKey
```
> يُعرَّف متغيّر ثابت اسمه (noiseKey) ويُسنَد إليه مفتاح نويز العام (peerInfo.noisePublicKey). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:558]

```
559:             if (noiseKey != null) {
```
> شرط: إذا كان المتغيّر (noiseKey) لا يساوي الفارغ فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:559]

```
560:                 com.bitchat.android.favorites.FavoritesPersistenceService.shared.updatePeerFavoritedUs(noiseKey, isFavorite)
```
> يُستدعى من المثيل المشترك (shared) لخدمة تخزين المفضّلات (FavoritesPersistenceService) الدالة (updatePeerFavoritedUs) مع مفتاح نويز (noiseKey) وحالة التفضيل (isFavorite). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:560]

```
561:                 if (npub != null) {
```
> شرط: إذا كان المتغيّر (npub) لا يساوي الفارغ فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:561]

```
562:                     // Index by noise key and current mesh peerID for fast Nostr routing
```
> تعليق: الفهرسة بمفتاح نويز ومعرّف النِّدّ الحالي في الشبكة لتوجيه نوستر (Nostr) السريع. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:562]

```
563:                     com.bitchat.android.favorites.FavoritesPersistenceService.shared.updateNostrPublicKey(noiseKey, npub)
```
> يُستدعى من المثيل المشترك (shared) لخدمة تخزين المفضّلات الدالة (updateNostrPublicKey) مع مفتاح نويز (noiseKey) ومفتاح نوستر العام (npub). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:563]

```
564:                     com.bitchat.android.favorites.FavoritesPersistenceService.shared.updateNostrPublicKeyForPeerID(fromPeerID, npub)
```
> يُستدعى من المثيل المشترك (shared) لخدمة تخزين المفضّلات الدالة (updateNostrPublicKeyForPeerID) مع معرّف النِّدّ المُرسِل (fromPeerID) ومفتاح نوستر العام (npub). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:564]

```
565:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:565]

```
566: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:566]

```
567:                 // Determine iOS-style guidance text
```
> تعليق: تحديد نصّ التوجيه على نمط نظام آي أو إس. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:567]

```
568:                 val rel = com.bitchat.android.favorites.FavoritesPersistenceService.shared.getFavoriteStatus(noiseKey)
```
> يُعرَّف متغيّر ثابت اسمه (rel) ويُسنَد إليه ناتج استدعاء (getFavoriteStatus) من المثيل المشترك (shared) لخدمة تخزين المفضّلات مع مفتاح نويز (noiseKey). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:568]

```
569:                 val guidance = if (isFavorite) {
```
> يُعرَّف متغيّر ثابت اسمه (guidance) ويُسنَد إليه ناتج تعبير شرطي: إذا كان (isFavorite) صحيحاً فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:569]

```
570:                     if (rel?.isFavorite == true) {
```
> شرط داخلي: إذا كانت حالة التفضيل في العلاقة (rel.isFavorite) تساوي القيمة الصحيحة فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:570]

```
571:                         " — mutual! You can continue DMs via Nostr when out of mesh."
```
> تعبير سلسلة نصّية قيمتها " — mutual! You can continue DMs via Nostr when out of mesh." تُسنَد كنتيجة للفرع. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:571]

```
572:                     } else {
```
> وإلا فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:572]

```
573:                         " — favorite back to continue DMs later."
```
> تعبير سلسلة نصّية قيمتها " — favorite back to continue DMs later." تُسنَد كنتيجة للفرع. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:573]

```
574:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:574]

```
575:                 } else {
```
> وإلا فافتح كتلة التنفيذ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:575]

```
576:                     ". DMs over Nostr will pause unless you both favorite again."
```
> تعبير سلسلة نصّية قيمتها ". DMs over Nostr will pause unless you both favorite again." تُسنَد كنتيجة للفرع. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:576]

```
577:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:577]

```
578: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:578]

```
579:                 // Emit system message via delegate callback
```
> تعليق: إصدار رسالة نظام عبر ردّ نداء المفوَّض. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:579]

```
580:                 val action = if (isFavorite) "favorited" else "unfavorited"
```
> يُعرَّف متغيّر ثابت اسمه (action) ويُسنَد إليه السلسلة "favorited" إن كان (isFavorite) صحيحاً وإلا السلسلة "unfavorited". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:580]

```
581:                 val sys = com.bitchat.android.model.BitchatMessage(
```
> يُعرَّف متغيّر ثابت اسمه (sys) ويُسنَد إليه كائن جديد من الصنف (BitchatMessage) مع فتح قائمة الوسائط. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:581]

```
582:                     sender = "system",
```
> تُضبَط الوسيطة (sender) على السلسلة "system". [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:582]

```
583:                     content = "${peerInfo.nickname} $action you$guidance",
```
> تُضبَط الوسيطة (content) على سلسلة مركّبة من اسم النِّدّ المستعار (peerInfo.nickname) ثم الفعل (action) ثم كلمة "you" ثم نصّ التوجيه (guidance). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:583]

```
584:                     timestamp = java.util.Date(),
```
> تُضبَط الوسيطة (timestamp) على كائن تاريخ (Date) جديد باللحظة الحالية. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:584]

```
585:                     isRelay = false
```
> تُضبَط الوسيطة (isRelay) على القيمة الخاطئة (false). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:585]

```
586:                 )
```
> إغلاق قائمة وسائط الكائن. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:586]

```
587:                 delegate?.onMessageReceived(sys)
```
> يُستدعى من المفوَّض (delegate) الدالة (onMessageReceived) مع تمرير رسالة النظام (sys). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:587]

```
588:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:588]

```
589:         } catch (_: Exception) {
```
> بدء كتلة التقاط الاستثناء (catch) للاستثناء (Exception) دون تسمية المتغيّر. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:589]

```
590:             // Best-effort; ignore errors
```
> تعليق: قدر المستطاع؛ تجاهل الأخطاء. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:590]

```
591:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:591]

```
592:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:592]

```
593: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:593]

```
594: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:594]

```
595: /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:595]

```
596:  * Delegate interface for message handler callbacks
```
> تعليق: واجهة المفوَّض لردود نداء معالِج الرسائل. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:596]

```
597:  */
```
> تعليق: نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:597]

```
598: interface MessageHandlerDelegate {
```
> تُعرَّف واجهة (interface) اسمها (MessageHandlerDelegate) مع فتح جسمها. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:598]

```
599:     // Peer management
```
> تعليق: إدارة النِّدّ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:599]

```
600:     fun addOrUpdatePeer(peerID: String, nickname: String): Boolean
```
> تُعلَن دالة اسمها (addOrUpdatePeer) تأخذ معرّف نِدّ (peerID) من نوع سلسلة واسماً مستعاراً (nickname) من نوع سلسلة وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:600]
