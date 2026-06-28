# شريحة — app/src/main/java/com/bitchat/android/mesh/MeshCore.kt (الأسطر 401–600)

```
401:                 val sent = transport.sendPacketToPeer(peerID, routed.packet)
```
> يُعرَّف متغيّر ثابت اسمه (sent) ويُسنَد إليه ناتج استدعاء الدالة (sendPacketToPeer) على ناقل النقل (transport) ممرّراً إليها مُعرّف النظير (peerID) والحزمة (routed.packet). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:401]

```
402:                 TransportBridgeService.sendToPeer(transport.id, peerID, routed.packet)
```
> تُستدعى الدالة (sendToPeer) على خدمة جسر النقل (TransportBridgeService) ممرّراً إليها مُعرّف الناقل (transport.id) ومُعرّف النظير (peerID) والحزمة (routed.packet). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:402]

```
403:                 return sent
```
> تُعيد الدالة قيمة المتغيّر (sent). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:403]

```
404:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:404]

```
405: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:405]

```
406:             override fun handleRequestSync(routed: RoutedPacket) {
```
> تُعرَّف بإعادة تعريف (override) دالة اسمها (handleRequestSync) تأخذ مُعامِلاً اسمه (routed) من نوع الحزمة الموجَّهة (RoutedPacket). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:406]

```
407:                 val fromPeer = routed.peerID ?: return
```
> يُعرَّف متغيّر ثابت اسمه (fromPeer) ويُسنَد إليه مُعرّف النظير (routed.peerID)، وإذا كان فارغاً (null) تُنهى الدالة بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:407]

```
408:                 val req = RequestSyncPacket.decode(routed.packet.payload) ?: return
```
> يُعرَّف متغيّر ثابت اسمه (req) ويُسنَد إليه ناتج فكّ ترميز (decode) لحزمة طلب المزامنة (RequestSyncPacket) من حمولة الحزمة (routed.packet.payload)، وإذا كان فارغاً تُنهى الدالة بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:408]

```
409:                 gossipSyncManager.handleRequestSync(fromPeer, req)
```
> تُستدعى الدالة (handleRequestSync) على مدير مزامنة الإشاعة (gossipSyncManager) ممرّراً إليها النظير المُرسِل (fromPeer) وطلب المزامنة (req). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:409]

```
410:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:410]

```
411:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:411]

```
412:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:412]

```
413: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:413]

```
414:     fun sendMessage(content: String, mentions: List<String> = emptyList(), channel: String? = null) {
```
> تُعرَّف دالة اسمها (sendMessage) تأخذ المحتوى (content) من نوع نصّ (String)، وقائمة الإشارات (mentions) من نوع قائمة نصوص بقيمة افتراضية قائمة فارغة (emptyList)، وقناة (channel) من نوع نصّ قابل للإفراغ بقيمة افتراضية فارغة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:414]

```
415:         if (content.isEmpty()) return
```
> إذا كان المحتوى (content) فارغاً تُنهى الدالة بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:415]

```
416:         scope.launch {
```
> يُطلَق عمل غير متزامن داخل النطاق (scope) عبر الدالة (launch). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:416]

```
417:             val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت اسمه (packet) ويُسنَد إليه كائن حزمة بِت‌شات (BitchatPacket) المنشأ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:417]

```
418:                 version = 1u,
```
> يُضبَط الحقل (version) على القيمة العددية غير المُوقَّعة (1u). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:418]

```
419:                 type = MessageType.MESSAGE.value,
```
> يُضبَط الحقل (type) على قيمة (value) لنوع الرسالة (MessageType.MESSAGE). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:419]

```
420:                 senderID = MeshPacketUtils.hexStringToByteArray(myPeerID),
```
> يُضبَط الحقل (senderID) على ناتج تحويل النصّ الستّ‌عشري إلى مصفوفة بايتات (hexStringToByteArray) لمُعرّف نظيري (myPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:420]

```
421:                 recipientID = SpecialRecipients.BROADCAST,
```
> يُضبَط الحقل (recipientID) على ثابت البثّ العامّ (SpecialRecipients.BROADCAST). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:421]

```
422:                 timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط الحقل (timestamp) على الوقت الحالي بالميلّي‌ثانية (currentTimeMillis) محوّلاً إلى عدد طويل غير مُوقَّع (toULong). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:422]

```
423:                 payload = content.toByteArray(Charsets.UTF_8),
```
> يُضبَط الحقل (payload) على المحتوى (content) محوّلاً إلى مصفوفة بايتات بترميز (UTF_8). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:423]

```
424:                 signature = null,
```
> يُضبَط الحقل (signature) على قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:424]

```
425:                 ttl = maxTtl
```
> يُضبَط الحقل (ttl) على القيمة القصوى لمدّة البقاء (maxTtl). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:425]

```
426:             )
```
> إغلاق قائمة وسائط منشئ الحزمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:426]

```
427:             val signedPacket = signPacketBeforeBroadcast(packet)
```
> يُعرَّف متغيّر ثابت اسمه (signedPacket) ويُسنَد إليه ناتج توقيع الحزمة قبل البثّ (signPacketBeforeBroadcast) للحزمة (packet). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:427]

```
428:             dispatchGlobal(RoutedPacket(signedPacket))
```
> تُستدعى الدالة (dispatchGlobal) ممرّراً إليها حزمة موجَّهة (RoutedPacket) ملفوفة حول الحزمة الموقّعة (signedPacket). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:428]

```
429:             try { gossipSyncManager.onPublicPacketSeen(signedPacket) } catch (_: Exception) { }
```
> داخل كتلة محاولة (try) تُستدعى الدالة (onPublicPacketSeen) على مدير مزامنة الإشاعة (gossipSyncManager) ممرّراً إليها الحزمة الموقّعة (signedPacket)، وأيّ استثناء (Exception) يُلتقَط ويُهمَل. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:429]

```
430:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:430]

```
431:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:431]

```
432: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:432]

```
433:     fun sendFileBroadcast(file: BitchatFilePacket) {
```
> تُعرَّف دالة اسمها (sendFileBroadcast) تأخذ مُعامِلاً اسمه (file) من نوع حزمة ملفّ بِت‌شات (BitchatFilePacket). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:433]

```
434:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:434]

```
435:             val payload = file.encode() ?: return
```
> يُعرَّف متغيّر ثابت اسمه (payload) ويُسنَد إليه ناتج ترميز (encode) الملفّ (file)، وإذا كان فارغاً تُنهى الدالة بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:435]

```
436:             scope.launch {
```
> يُطلَق عمل غير متزامن داخل النطاق (scope) عبر الدالة (launch). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:436]

```
437:                 val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت اسمه (packet) ويُسنَد إليه كائن حزمة بِت‌شات (BitchatPacket) المنشأ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:437]

```
438:                     version = 2u,
```
> يُضبَط الحقل (version) على القيمة العددية غير المُوقَّعة (2u). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:438]

```
439:                     type = MessageType.FILE_TRANSFER.value,
```
> يُضبَط الحقل (type) على قيمة (value) لنوع رسالة نقل الملفّ (MessageType.FILE_TRANSFER). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:439]

```
440:                     senderID = MeshPacketUtils.hexStringToByteArray(myPeerID),
```
> يُضبَط الحقل (senderID) على ناتج تحويل النصّ الستّ‌عشري إلى مصفوفة بايتات (hexStringToByteArray) لمُعرّف نظيري (myPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:440]

```
441:                     recipientID = SpecialRecipients.BROADCAST,
```
> يُضبَط الحقل (recipientID) على ثابت البثّ العامّ (SpecialRecipients.BROADCAST). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:441]

```
442:                     timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط الحقل (timestamp) على الوقت الحالي بالميلّي‌ثانية (currentTimeMillis) محوّلاً إلى عدد طويل غير مُوقَّع (toULong). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:442]

```
443:                     payload = payload,
```
> يُضبَط الحقل (payload) على المتغيّر (payload). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:443]

```
444:                     signature = null,
```
> يُضبَط الحقل (signature) على قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:444]

```
445:                     ttl = maxTtl
```
> يُضبَط الحقل (ttl) على القيمة القصوى لمدّة البقاء (maxTtl). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:445]

```
446:                 )
```
> إغلاق قائمة وسائط منشئ الحزمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:446]

```
447:                 val signed = signPacketBeforeBroadcast(packet)
```
> يُعرَّف متغيّر ثابت اسمه (signed) ويُسنَد إليه ناتج توقيع الحزمة قبل البثّ (signPacketBeforeBroadcast) للحزمة (packet). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:447]

```
448:                 val transferId = MeshPacketUtils.sha256Hex(payload)
```
> يُعرَّف متغيّر ثابت اسمه (transferId) ويُسنَد إليه ناتج بصمة (sha256Hex) للحمولة (payload). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:448]

```
449:                 dispatchGlobal(RoutedPacket(signed, transferId = transferId))
```
> تُستدعى الدالة (dispatchGlobal) ممرّراً إليها حزمة موجَّهة (RoutedPacket) ملفوفة حول الحزمة الموقّعة (signed) مع ضبط مُعرّف النقل (transferId) على المتغيّر (transferId). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:449]

```
450:                 try { gossipSyncManager.onPublicPacketSeen(signed) } catch (_: Exception) { }
```
> داخل كتلة محاولة (try) تُستدعى الدالة (onPublicPacketSeen) على مدير مزامنة الإشاعة (gossipSyncManager) ممرّراً إليها الحزمة الموقّعة (signed)، وأيّ استثناء (Exception) يُلتقَط ويُهمَل. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:450]

```
451:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:451]

```
452:         } catch (e: Exception) {
```
> بداية كتلة التقاط استثناء (Exception) باسم (e). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:452]

```
453:             Log.e("MeshCore", "sendFileBroadcast failed: ${e.message}", e)
```
> يُسجَّل خطأ (Log.e) بالوسم (MeshCore) ونصّ «فشل sendFileBroadcast» متبوعاً برسالة الاستثناء (e.message) والاستثناء (e). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:453]

```
454:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:454]

```
455:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:455]

```
456: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:456]

```
457:     fun sendFilePrivate(recipientPeerID: String, file: BitchatFilePacket) {
```
> تُعرَّف دالة اسمها (sendFilePrivate) تأخذ مُعرّف النظير المُستقبِل (recipientPeerID) من نوع نصّ، والملفّ (file) من نوع حزمة ملفّ بِت‌شات (BitchatFilePacket). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:457]

```
458:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:458]

```
459:             scope.launch {
```
> يُطلَق عمل غير متزامن داخل النطاق (scope) عبر الدالة (launch). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:459]

```
460:                 if (!encryptionService.hasEstablishedSession(recipientPeerID)) {
```
> إذا لم تكن هناك جلسة قائمة (hasEstablishedSession) في خدمة التعمية (encryptionService) مع المُستقبِل (recipientPeerID) تُنفَّذ الكتلة التالية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:460]

```
461:                     initiateNoiseHandshake(recipientPeerID)
```
> تُستدعى الدالة (initiateNoiseHandshake) لبدء مصافحة نويز (Noise) مع المُستقبِل (recipientPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:461]

```
462:                     return@launch
```
> يُنهى عمل (launch) بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:462]

```
463:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:463]

```
464:                 val tlv = file.encode() ?: return@launch
```
> يُعرَّف متغيّر ثابت اسمه (tlv) ويُسنَد إليه ناتج ترميز (encode) الملفّ (file)، وإذا كان فارغاً يُنهى عمل (launch) بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:464]

```
465:                 val np = NoisePayload(type = NoisePayloadType.FILE_TRANSFER, data = tlv).encode()
```
> يُعرَّف متغيّر ثابت اسمه (np) ويُسنَد إليه ناتج ترميز (encode) حمولة نويز (NoisePayload) المنشأة بنوع نقل الملفّ (NoisePayloadType.FILE_TRANSFER) وبيانات (tlv). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:465]

```
466:                 val enc = encryptionService.encrypt(np, recipientPeerID)
```
> يُعرَّف متغيّر ثابت اسمه (enc) ويُسنَد إليه ناتج تعمية (encrypt) للحمولة (np) باتّجاه المُستقبِل (recipientPeerID) عبر خدمة التعمية (encryptionService). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:466]

```
467:                 val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت اسمه (packet) ويُسنَد إليه كائن حزمة بِت‌شات (BitchatPacket) المنشأ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:467]

```
468:                     version = if (enc.size > 0xFFFF) 2u else 1u,
```
> يُضبَط الحقل (version) على القيمة (2u) إذا كان حجم المعمَّى (enc.size) أكبر من القيمة الستّ‌عشرية (0xFFFF) وإلّا على القيمة (1u). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:468]

```
469:                     type = MessageType.NOISE_ENCRYPTED.value,
```
> يُضبَط الحقل (type) على قيمة (value) لنوع رسالة نويز المعمّاة (MessageType.NOISE_ENCRYPTED). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:469]

```
470:                     senderID = MeshPacketUtils.hexStringToByteArray(myPeerID),
```
> يُضبَط الحقل (senderID) على ناتج تحويل النصّ الستّ‌عشري إلى مصفوفة بايتات (hexStringToByteArray) لمُعرّف نظيري (myPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:470]

```
471:                     recipientID = MeshPacketUtils.hexStringToByteArray(recipientPeerID),
```
> يُضبَط الحقل (recipientID) على ناتج تحويل النصّ الستّ‌عشري إلى مصفوفة بايتات (hexStringToByteArray) لمُعرّف المُستقبِل (recipientPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:471]

```
472:                     timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط الحقل (timestamp) على الوقت الحالي بالميلّي‌ثانية (currentTimeMillis) محوّلاً إلى عدد طويل غير مُوقَّع (toULong). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:472]

```
473:                     payload = enc,
```
> يُضبَط الحقل (payload) على المعمَّى (enc). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:473]

```
474:                     signature = null,
```
> يُضبَط الحقل (signature) على قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:474]

```
475:                     ttl = maxTtl
```
> يُضبَط الحقل (ttl) على القيمة القصوى لمدّة البقاء (maxTtl). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:475]

```
476:                 )
```
> إغلاق قائمة وسائط منشئ الحزمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:476]

```
477:                 val signed = signPacketBeforeBroadcast(packet)
```
> يُعرَّف متغيّر ثابت اسمه (signed) ويُسنَد إليه ناتج توقيع الحزمة قبل البثّ (signPacketBeforeBroadcast) للحزمة (packet). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:477]

```
478:                 val transferId = MeshPacketUtils.sha256Hex(tlv)
```
> يُعرَّف متغيّر ثابت اسمه (transferId) ويُسنَد إليه ناتج بصمة (sha256Hex) للبيانات (tlv). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:478]

```
479:                 dispatchGlobal(RoutedPacket(signed, transferId = transferId))
```
> تُستدعى الدالة (dispatchGlobal) ممرّراً إليها حزمة موجَّهة (RoutedPacket) ملفوفة حول الحزمة الموقّعة (signed) مع ضبط مُعرّف النقل (transferId) على المتغيّر (transferId). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:479]

```
480:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:480]

```
481:         } catch (e: Exception) {
```
> بداية كتلة التقاط استثناء (Exception) باسم (e). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:481]

```
482:             Log.e("MeshCore", "sendFilePrivate failed: ${e.message}", e)
```
> يُسجَّل خطأ (Log.e) بالوسم (MeshCore) ونصّ «فشل sendFilePrivate» متبوعاً برسالة الاستثناء (e.message) والاستثناء (e). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:482]

```
483:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:483]

```
484:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:484]

```
485: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:485]

```
486:     fun cancelFileTransfer(transferId: String): Boolean {
```
> تُعرَّف دالة اسمها (cancelFileTransfer) تأخذ مُعرّف النقل (transferId) من نوع نصّ وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:486]

```
487:         return transport.cancelTransfer(transferId)
```
> تُعيد الدالة ناتج استدعاء (cancelTransfer) على ناقل النقل (transport) ممرّراً إليه مُعرّف النقل (transferId). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:487]

```
488:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:488]

```
489: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:489]

```
490:     fun sendPrivateMessage(content: String, recipientPeerID: String, recipientNickname: String, messageID: String? = null) {
```
> تُعرَّف دالة اسمها (sendPrivateMessage) تأخذ المحتوى (content) نصّاً، ومُعرّف النظير المُستقبِل (recipientPeerID) نصّاً، واسم المُستقبِل المستعار (recipientNickname) نصّاً، ومُعرّف الرسالة (messageID) نصّاً قابلاً للإفراغ بقيمة افتراضية فارغة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:490]

```
491:         if (content.isEmpty() || recipientPeerID.isEmpty()) return
```
> إذا كان المحتوى (content) فارغاً أو كان مُعرّف المُستقبِل (recipientPeerID) فارغاً تُنهى الدالة بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:491]

```
492:         scope.launch {
```
> يُطلَق عمل غير متزامن داخل النطاق (scope) عبر الدالة (launch). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:492]

```
493:             val finalMessageID = messageID ?: java.util.UUID.randomUUID().toString()
```
> يُعرَّف متغيّر ثابت اسمه (finalMessageID) ويُسنَد إليه مُعرّف الرسالة (messageID)، وإذا كان فارغاً فمُعرّف عشوائيّ عامّ فريد (UUID.randomUUID) محوّل إلى نصّ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:493]

```
494: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:494]

```
495:             if (encryptionService.hasEstablishedSession(recipientPeerID)) {
```
> إذا كانت هناك جلسة قائمة (hasEstablishedSession) في خدمة التعمية (encryptionService) مع المُستقبِل (recipientPeerID) تُنفَّذ الكتلة التالية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:495]

```
496:                 try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:496]

```
497:                     val privateMessage = PrivateMessagePacket(messageID = finalMessageID, content = content)
```
> يُعرَّف متغيّر ثابت اسمه (privateMessage) ويُسنَد إليه حزمة رسالة خاصّة (PrivateMessagePacket) المنشأة بمُعرّف الرسالة (finalMessageID) والمحتوى (content). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:497]

```
498:                     val tlvData = privateMessage.encode() ?: return@launch
```
> يُعرَّف متغيّر ثابت اسمه (tlvData) ويُسنَد إليه ناتج ترميز (encode) الرسالة الخاصّة (privateMessage)، وإذا كان فارغاً يُنهى عمل (launch) بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:498]

```
499:                     val messagePayload = NoisePayload(
```
> يُعرَّف متغيّر ثابت اسمه (messagePayload) ويُسنَد إليه حمولة نويز (NoisePayload) المنشأة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:499]

```
500:                         type = NoisePayloadType.PRIVATE_MESSAGE,
```
> يُضبَط الحقل (type) على نوع الرسالة الخاصّة (NoisePayloadType.PRIVATE_MESSAGE). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:500]

```
501:                         data = tlvData
```
> يُضبَط الحقل (data) على البيانات (tlvData). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:501]

```
502:                     )
```
> إغلاق قائمة وسائط منشئ حمولة نويز. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:502]

```
503:                     val encrypted = encryptionService.encrypt(messagePayload.encode(), recipientPeerID)
```
> يُعرَّف متغيّر ثابت اسمه (encrypted) ويُسنَد إليه ناتج تعمية (encrypt) لترميز حمولة الرسالة (messagePayload.encode) باتّجاه المُستقبِل (recipientPeerID) عبر خدمة التعمية (encryptionService). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:503]

```
504:                     val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت اسمه (packet) ويُسنَد إليه كائن حزمة بِت‌شات (BitchatPacket) المنشأ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:504]

```
505:                         version = 1u,
```
> يُضبَط الحقل (version) على القيمة العددية غير المُوقَّعة (1u). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:505]

```
506:                         type = MessageType.NOISE_ENCRYPTED.value,
```
> يُضبَط الحقل (type) على قيمة (value) لنوع رسالة نويز المعمّاة (MessageType.NOISE_ENCRYPTED). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:506]

```
507:                         senderID = MeshPacketUtils.hexStringToByteArray(myPeerID),
```
> يُضبَط الحقل (senderID) على ناتج تحويل النصّ الستّ‌عشري إلى مصفوفة بايتات (hexStringToByteArray) لمُعرّف نظيري (myPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:507]

```
508:                         recipientID = MeshPacketUtils.hexStringToByteArray(recipientPeerID),
```
> يُضبَط الحقل (recipientID) على ناتج تحويل النصّ الستّ‌عشري إلى مصفوفة بايتات (hexStringToByteArray) لمُعرّف المُستقبِل (recipientPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:508]

```
509:                         timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط الحقل (timestamp) على الوقت الحالي بالميلّي‌ثانية (currentTimeMillis) محوّلاً إلى عدد طويل غير مُوقَّع (toULong). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:509]

```
510:                         payload = encrypted,
```
> يُضبَط الحقل (payload) على المعمَّى (encrypted). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:510]

```
511:                         signature = null,
```
> يُضبَط الحقل (signature) على قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:511]

```
512:                         ttl = maxTtl
```
> يُضبَط الحقل (ttl) على القيمة القصوى لمدّة البقاء (maxTtl). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:512]

```
513:                     )
```
> إغلاق قائمة وسائط منشئ الحزمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:513]

```
514:                     val signedPacket = signPacketBeforeBroadcast(packet)
```
> يُعرَّف متغيّر ثابت اسمه (signedPacket) ويُسنَد إليه ناتج توقيع الحزمة قبل البثّ (signPacketBeforeBroadcast) للحزمة (packet). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:514]

```
515:                     dispatchGlobal(RoutedPacket(signedPacket))
```
> تُستدعى الدالة (dispatchGlobal) ممرّراً إليها حزمة موجَّهة (RoutedPacket) ملفوفة حول الحزمة الموقّعة (signedPacket). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:515]

```
516:                 } catch (e: Exception) {
```
> بداية كتلة التقاط استثناء (Exception) باسم (e). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:516]

```
517:                     Log.e("MeshCore", "Failed to encrypt private message: ${e.message}")
```
> يُسجَّل خطأ (Log.e) بالوسم (MeshCore) ونصّ «فشل تعمية الرسالة الخاصّة» متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:517]

```
518:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:518]

```
519:             } else {
```
> بداية كتلة البديل (else). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:519]

```
520:                 initiateNoiseHandshake(recipientPeerID)
```
> تُستدعى الدالة (initiateNoiseHandshake) لبدء مصافحة نويز (Noise) مع المُستقبِل (recipientPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:520]

```
521:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:521]

```
522:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:522]

```
523:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:523]

```
524: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:524]

```
525:     fun sendReadReceipt(messageID: String, recipientPeerID: String, readerNickname: String) {
```
> تُعرَّف دالة اسمها (sendReadReceipt) تأخذ مُعرّف الرسالة (messageID) نصّاً، ومُعرّف النظير المُستقبِل (recipientPeerID) نصّاً، واسم القارئ المستعار (readerNickname) نصّاً. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:525]

```
526:         scope.launch {
```
> يُطلَق عمل غير متزامن داخل النطاق (scope) عبر الدالة (launch). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:526]

```
527:             if (hooks.readReceiptInterceptor?.invoke(messageID, recipientPeerID) == true) return@launch
```
> إذا كان معترِض إيصال القراءة (readReceiptInterceptor) في الخطّافات (hooks) يُستدعى بمُعرّف الرسالة (messageID) والمُستقبِل (recipientPeerID) ويُعيد القيمة الصحيحة (true)، يُنهى عمل (launch) بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:527]

```
528:             try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:528]

```
529:                 val payload = NoisePayload(
```
> يُعرَّف متغيّر ثابت اسمه (payload) ويُسنَد إليه حمولة نويز (NoisePayload) المنشأة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:529]

```
530:                     type = NoisePayloadType.READ_RECEIPT,
```
> يُضبَط الحقل (type) على نوع إيصال القراءة (NoisePayloadType.READ_RECEIPT). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:530]

```
531:                     data = messageID.toByteArray(Charsets.UTF_8)
```
> يُضبَط الحقل (data) على مُعرّف الرسالة (messageID) محوّلاً إلى مصفوفة بايتات بترميز (UTF_8). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:531]

```
532:                 ).encode()
```
> يُستدعى ترميز (encode) على حمولة نويز المنشأة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:532]

```
533:                 val enc = encryptionService.encrypt(payload, recipientPeerID)
```
> يُعرَّف متغيّر ثابت اسمه (enc) ويُسنَد إليه ناتج تعمية (encrypt) للحمولة (payload) باتّجاه المُستقبِل (recipientPeerID) عبر خدمة التعمية (encryptionService). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:533]

```
534:                 val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت اسمه (packet) ويُسنَد إليه كائن حزمة بِت‌شات (BitchatPacket) المنشأ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:534]

```
535:                     version = 1u,
```
> يُضبَط الحقل (version) على القيمة العددية غير المُوقَّعة (1u). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:535]

```
536:                     type = MessageType.NOISE_ENCRYPTED.value,
```
> يُضبَط الحقل (type) على قيمة (value) لنوع رسالة نويز المعمّاة (MessageType.NOISE_ENCRYPTED). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:536]

```
537:                     senderID = MeshPacketUtils.hexStringToByteArray(myPeerID),
```
> يُضبَط الحقل (senderID) على ناتج تحويل النصّ الستّ‌عشري إلى مصفوفة بايتات (hexStringToByteArray) لمُعرّف نظيري (myPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:537]

```
538:                     recipientID = MeshPacketUtils.hexStringToByteArray(recipientPeerID),
```
> يُضبَط الحقل (recipientID) على ناتج تحويل النصّ الستّ‌عشري إلى مصفوفة بايتات (hexStringToByteArray) لمُعرّف المُستقبِل (recipientPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:538]

```
539:                     timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط الحقل (timestamp) على الوقت الحالي بالميلّي‌ثانية (currentTimeMillis) محوّلاً إلى عدد طويل غير مُوقَّع (toULong). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:539]

```
540:                     payload = enc,
```
> يُضبَط الحقل (payload) على المعمَّى (enc). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:540]

```
541:                     signature = null,
```
> يُضبَط الحقل (signature) على قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:541]

```
542:                     ttl = maxTtl
```
> يُضبَط الحقل (ttl) على القيمة القصوى لمدّة البقاء (maxTtl). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:542]

```
543:                 )
```
> إغلاق قائمة وسائط منشئ الحزمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:543]

```
544:                 dispatchGlobal(RoutedPacket(signPacketBeforeBroadcast(packet)))
```
> تُستدعى الدالة (dispatchGlobal) ممرّراً إليها حزمة موجَّهة (RoutedPacket) ملفوفة حول ناتج توقيع الحزمة قبل البثّ (signPacketBeforeBroadcast) للحزمة (packet). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:544]

```
545:                 hooks.onReadReceiptSent?.invoke(messageID)
```
> يُستدعى خطّاف إرسال إيصال القراءة (onReadReceiptSent) في الخطّافات (hooks)، إن وُجد، ممرّراً إليه مُعرّف الرسالة (messageID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:545]

```
546:             } catch (e: Exception) {
```
> بداية كتلة التقاط استثناء (Exception) باسم (e). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:546]

```
547:                 Log.e("MeshCore", "Failed to send read receipt: ${e.message}")
```
> يُسجَّل خطأ (Log.e) بالوسم (MeshCore) ونصّ «فشل إرسال إيصال القراءة» متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:547]

```
548:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:548]

```
549:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:549]

```
550:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:550]

```
551: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:551]

```
552:     fun sendVerifyChallenge(peerID: String, noiseKeyHex: String, nonceA: ByteArray) {
```
> تُعرَّف دالة اسمها (sendVerifyChallenge) تأخذ مُعرّف النظير (peerID) نصّاً، ومفتاح نويز الستّ‌عشري (noiseKeyHex) نصّاً، والرقم العشوائي ألف (nonceA) من نوع مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:552]

```
553:         val payload = NoisePayload(
```
> يُعرَّف متغيّر ثابت اسمه (payload) ويُسنَد إليه حمولة نويز (NoisePayload) المنشأة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:553]

```
554:             type = NoisePayloadType.VERIFY_CHALLENGE,
```
> يُضبَط الحقل (type) على نوع تحدّي التحقّق (NoisePayloadType.VERIFY_CHALLENGE). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:554]

```
555:             data = com.bitchat.android.services.VerificationService.buildVerifyChallenge(noiseKeyHex, nonceA)
```
> يُضبَط الحقل (data) على ناتج بناء تحدّي التحقّق (buildVerifyChallenge) من خدمة التحقّق (VerificationService) ممرّراً إليها مفتاح نويز الستّ‌عشري (noiseKeyHex) والرقم العشوائي (nonceA). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:555]

```
556:         )
```
> إغلاق قائمة وسائط منشئ حمولة نويز. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:556]

```
557:         sendNoisePayloadToPeer(payload, peerID)
```
> تُستدعى الدالة (sendNoisePayloadToPeer) ممرّراً إليها الحمولة (payload) ومُعرّف النظير (peerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:557]

```
558:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:558]

```
559: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:559]

```
560:     fun sendVerifyResponse(peerID: String, noiseKeyHex: String, nonceA: ByteArray) {
```
> تُعرَّف دالة اسمها (sendVerifyResponse) تأخذ مُعرّف النظير (peerID) نصّاً، ومفتاح نويز الستّ‌عشري (noiseKeyHex) نصّاً، والرقم العشوائي ألف (nonceA) من نوع مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:560]

```
561:         val tlv = com.bitchat.android.services.VerificationService.buildVerifyResponse(noiseKeyHex, nonceA) ?: return
```
> يُعرَّف متغيّر ثابت اسمه (tlv) ويُسنَد إليه ناتج بناء ردّ التحقّق (buildVerifyResponse) من خدمة التحقّق (VerificationService) بمفتاح نويز الستّ‌عشري (noiseKeyHex) والرقم العشوائي (nonceA)، وإذا كان فارغاً تُنهى الدالة بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:561]

```
562:         val payload = NoisePayload(
```
> يُعرَّف متغيّر ثابت اسمه (payload) ويُسنَد إليه حمولة نويز (NoisePayload) المنشأة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:562]

```
563:             type = NoisePayloadType.VERIFY_RESPONSE,
```
> يُضبَط الحقل (type) على نوع ردّ التحقّق (NoisePayloadType.VERIFY_RESPONSE). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:563]

```
564:             data = tlv
```
> يُضبَط الحقل (data) على البيانات (tlv). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:564]

```
565:         )
```
> إغلاق قائمة وسائط منشئ حمولة نويز. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:565]

```
566:         sendNoisePayloadToPeer(payload, peerID)
```
> تُستدعى الدالة (sendNoisePayloadToPeer) ممرّراً إليها الحمولة (payload) ومُعرّف النظير (peerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:566]

```
567:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:567]

```
568: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:568]

```
569:     private fun sendNoisePayloadToPeer(payload: NoisePayload, recipientPeerID: String) {
```
> تُعرَّف دالة خاصّة (private) اسمها (sendNoisePayloadToPeer) تأخذ الحمولة (payload) من نوع حمولة نويز (NoisePayload) ومُعرّف النظير المُستقبِل (recipientPeerID) نصّاً. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:569]

```
570:         scope.launch {
```
> يُطلَق عمل غير متزامن داخل النطاق (scope) عبر الدالة (launch). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:570]

```
571:             try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:571]

```
572:                 val encrypted = encryptionService.encrypt(payload.encode(), recipientPeerID)
```
> يُعرَّف متغيّر ثابت اسمه (encrypted) ويُسنَد إليه ناتج تعمية (encrypt) لترميز الحمولة (payload.encode) باتّجاه المُستقبِل (recipientPeerID) عبر خدمة التعمية (encryptionService). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:572]

```
573:                 val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت اسمه (packet) ويُسنَد إليه كائن حزمة بِت‌شات (BitchatPacket) المنشأ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:573]

```
574:                     version = 1u,
```
> يُضبَط الحقل (version) على القيمة العددية غير المُوقَّعة (1u). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:574]

```
575:                     type = MessageType.NOISE_ENCRYPTED.value,
```
> يُضبَط الحقل (type) على قيمة (value) لنوع رسالة نويز المعمّاة (MessageType.NOISE_ENCRYPTED). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:575]

```
576:                     senderID = MeshPacketUtils.hexStringToByteArray(myPeerID),
```
> يُضبَط الحقل (senderID) على ناتج تحويل النصّ الستّ‌عشري إلى مصفوفة بايتات (hexStringToByteArray) لمُعرّف نظيري (myPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:576]

```
577:                     recipientID = MeshPacketUtils.hexStringToByteArray(recipientPeerID),
```
> يُضبَط الحقل (recipientID) على ناتج تحويل النصّ الستّ‌عشري إلى مصفوفة بايتات (hexStringToByteArray) لمُعرّف المُستقبِل (recipientPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:577]

```
578:                     timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط الحقل (timestamp) على الوقت الحالي بالميلّي‌ثانية (currentTimeMillis) محوّلاً إلى عدد طويل غير مُوقَّع (toULong). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:578]

```
579:                     payload = encrypted,
```
> يُضبَط الحقل (payload) على المعمَّى (encrypted). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:579]

```
580:                     signature = null,
```
> يُضبَط الحقل (signature) على قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:580]

```
581:                     ttl = maxTtl
```
> يُضبَط الحقل (ttl) على القيمة القصوى لمدّة البقاء (maxTtl). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:581]

```
582:                 )
```
> إغلاق قائمة وسائط منشئ الحزمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:582]

```
583:                 dispatchGlobal(RoutedPacket(signPacketBeforeBroadcast(packet)))
```
> تُستدعى الدالة (dispatchGlobal) ممرّراً إليها حزمة موجَّهة (RoutedPacket) ملفوفة حول ناتج توقيع الحزمة قبل البثّ (signPacketBeforeBroadcast) للحزمة (packet). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:583]

```
584:             } catch (e: Exception) {
```
> بداية كتلة التقاط استثناء (Exception) باسم (e). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:584]

```
585:                 Log.e("MeshCore", "Failed to send Noise payload to $recipientPeerID: ${e.message}")
```
> يُسجَّل خطأ (Log.e) بالوسم (MeshCore) ونصّ «فشل إرسال حمولة نويز إلى» متبوعاً بمُعرّف المُستقبِل (recipientPeerID) ورسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:585]

```
586:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:586]

```
587:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:587]

```
588:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:588]

```
589: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:589]

```
590:     fun sendBroadcastAnnounce() {
```
> تُعرَّف دالة اسمها (sendBroadcastAnnounce) بلا مُعامِلات. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:590]

```
591:         scope.launch {
```
> يُطلَق عمل غير متزامن داخل النطاق (scope) عبر الدالة (launch). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:591]

```
592:             val nickname = hooks.announcementNicknameProvider?.invoke()
```
> يُعرَّف متغيّر ثابت اسمه (nickname) ويُسنَد إليه ناتج استدعاء مزوّد اسم الإعلان المستعار (announcementNicknameProvider) في الخطّافات (hooks)، إن وُجد. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:592]

```
593:                 ?: delegate?.getNickname()
```
> وإذا كان فارغاً يُسنَد ناتج استدعاء جلب الاسم المستعار (getNickname) من المفوَّض (delegate)، إن وُجد. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:593]

```
594:                 ?: myPeerID
```
> وإذا كان فارغاً يُسنَد مُعرّف نظيري (myPeerID). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:594]

```
595:             val staticKey = encryptionService.getStaticPublicKey() ?: run {
```
> يُعرَّف متغيّر ثابت اسمه (staticKey) ويُسنَد إليه المفتاح العامّ الثابت (getStaticPublicKey) من خدمة التعمية (encryptionService)، وإذا كان فارغاً تُنفَّذ كتلة (run) التالية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:595]

```
596:                 Log.e("MeshCore", "No static public key available for announcement")
```
> يُسجَّل خطأ (Log.e) بالوسم (MeshCore) ونصّ «لا مفتاح عامّ ثابت متاح للإعلان». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:596]

```
597:                 return@launch
```
> يُنهى عمل (launch) بإرجاع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:597]

```
598:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:598]

```
599:             val signingKey = encryptionService.getSigningPublicKey() ?: run {
```
> يُعرَّف متغيّر ثابت اسمه (signingKey) ويُسنَد إليه مفتاح التوقيع العامّ (getSigningPublicKey) من خدمة التعمية (encryptionService)، وإذا كان فارغاً تُنفَّذ كتلة (run) التالية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:599]

```
600:                 Log.e("MeshCore", "No signing public key available for announcement")
```
> يُسجَّل خطأ (Log.e) بالوسم (MeshCore) ونصّ «لا مفتاح توقيع عامّ متاح للإعلان». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:600]
