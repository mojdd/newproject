# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt (الأسطر 401–600)

```
401:                 Log.d(TAG, "Updated peer ID binding: $newPeerID (was: $previousPeerID), fingerprint: ${fingerprint.take(16)}...")
```
> يُستدعى تسجيل تنقيح (Log.d) مع الوسم (TAG) ونص يقول إنّ ربط معرّف النّظير (peer ID binding) تحدّث إلى القيمة الجديدة newPeerID وكانت سابقاً previousPeerID، ويعرض أوّل ١٦ حرفاً من البصمة fingerprint عبر take(16). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:401]

```
402:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:402]

```
403:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:403]

```
404:             // Message operations  
```
> تعليق: عمليّات الرّسائل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:404]

```
405:             override fun decryptChannelMessage(encryptedContent: ByteArray, channel: String): String? {
```
> تعريف دالّة متجاوِزة (override) باسم فكّ تشفير رسالة القناة (decryptChannelMessage) تأخذ محتوى مشفّراً encryptedContent من نوع مصفوفة بايتات (ByteArray) ونصّ قناة channel، وتعيد نصّاً String قابلاً للعدميّة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:405]

```
406:                 return delegate?.decryptChannelMessage(encryptedContent, channel)
```
> تُعيد نتيجة استدعاء decryptChannelMessage على المُفوَّض إليه (delegate) إن لم يكن عدميّاً، ممرّرةً encryptedContent وchannel. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:406]

```
407:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:407]

```
408:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:408]

```
409:             // Callbacks
```
> تعليق: ردود النّداء (Callbacks). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:409]

```
410:             override fun onMessageReceived(message: BitchatMessage) {
```
> تعريف دالّة متجاوِزة باسم عند استلام رسالة (onMessageReceived) تأخذ رسالة message من نوع BitchatMessage. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:410]

```
411:                 // Always reflect into process-wide store so UI can hydrate after recreation
```
> تعليق: اعكس دائماً إلى مخزن على مستوى العمليّة كي تستطيع الواجهة (UI) الترطّب بعد إعادة الإنشاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:411]

```
412:                 try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:412]

```
413:                     when {
```
> بداية تعبير شرطيّ متعدّد (when) بلا موضوع. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:413]

```
414:                         message.isPrivate -> {
```
> فرع: إذا كانت خاصّيّة الرّسالة خاصّة (isPrivate) صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:414]

```
415:                             val peer = message.senderPeerID ?: ""
```
> يُعرَّف متغيّر ثابت peer ويُسنَد إليه معرّف نظير المُرسِل (senderPeerID) للرّسالة، أو نصّ فارغ إن كان عدميّاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:415]

```
416:                             if (peer.isNotEmpty()) com.bitchat.android.services.AppStateStore.addPrivateMessage(peer, message)
```
> إذا لم يكن peer فارغاً (isNotEmpty) يُستدعى addPrivateMessage على AppStateStore ممرّراً peer وmessage. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:416]

```
417:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:417]

```
418:                         message.channel != null -> {
```
> فرع: إذا كانت قناة الرّسالة (channel) ليست عدميّة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:418]

```
419:                             com.bitchat.android.services.AppStateStore.addChannelMessage(message.channel!!, message)
```
> يُستدعى addChannelMessage على AppStateStore ممرّراً قناة الرّسالة (بتأكيد عدم العدميّة !!) وmessage. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:419]

```
420:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:420]

```
421:                         else -> {
```
> الفرع الافتراضيّ (else). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:421]

```
422:                             com.bitchat.android.services.AppStateStore.addPublicMessage(message)
```
> يُستدعى addPublicMessage على AppStateStore ممرّراً message. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:422]

```
423:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:423]

```
424:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:424]

```
425:                 } catch (_: Exception) { }
```
> كتلة التقاط (catch) لأيّ استثناء (Exception) باسم مُهمَل، وجسمها فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:425]

```
426:                 // And forward to UI delegate if attached
```
> تعليق: ومرِّر إلى مُفوَّض الواجهة إن كان مرتبطاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:426]

```
427:                 delegate?.didReceiveMessage(message)
```
> يُستدعى didReceiveMessage على delegate إن لم يكن عدميّاً ممرّراً message. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:427]

```
428:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:428]

```
429:                 // If no UI delegate attached (app closed), show DM notification via service manager
```
> تعليق: إن لم يكن مُفوَّض الواجهة مرتبطاً (التّطبيق مغلق)، أظهر إشعار الرّسالة المباشرة (DM) عبر مدير الخدمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:429]

```
430:                 if (delegate == null && message.isPrivate) {
```
> إذا كان delegate عدميّاً والرّسالة خاصّة (isPrivate). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:430]

```
431:                     try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:431]

```
432:                         val senderPeerID = message.senderPeerID
```
> يُعرَّف متغيّر ثابت senderPeerID ويُسنَد إليه معرّف نظير المُرسِل للرّسالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:432]

```
433:                         if (senderPeerID != null) {
```
> إذا لم يكن senderPeerID عدميّاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:433]

```
434:                             val nick = try { peerManager.getPeerNickname(senderPeerID) } catch (_: Exception) { null } ?: senderPeerID
```
> يُعرَّف متغيّر ثابت nick ويُسنَد إليه كنية النّظير (getPeerNickname) من مدير النّظراء (peerManager) داخل محاولة، أو null عند الاستثناء، وإلّا senderPeerID إن كانت النّتيجة عدميّة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:434]

```
435:                             val preview = com.bitchat.android.ui.NotificationTextUtils.buildPrivateMessagePreview(message)
```
> يُعرَّف متغيّر ثابت preview ويُسنَد إليه ناتج buildPrivateMessagePreview على NotificationTextUtils ممرّراً message. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:435]

```
436:                             serviceNotificationManager.setAppBackgroundState(true)
```
> يُستدعى setAppBackgroundState على مدير إشعارات الخدمة (serviceNotificationManager) بالقيمة true. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:436]

```
437:                             serviceNotificationManager.showPrivateMessageNotification(senderPeerID, nick, preview)
```
> يُستدعى showPrivateMessageNotification على serviceNotificationManager ممرّراً senderPeerID وnick وpreview. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:437]

```
438:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:438]

```
439:                     } catch (_: Exception) { }
```
> كتلة التقاط لأيّ استثناء باسم مُهمَل، وجسمها فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:439]

```
440:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:440]

```
441:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:441]

```
442:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:442]

```
443:             override fun onChannelLeave(channel: String, fromPeer: String) {
```
> تعريف دالّة متجاوِزة باسم عند مغادرة القناة (onChannelLeave) تأخذ نصّ القناة channel ونصّ النّظير المُرسِل fromPeer. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:443]

```
444:                 delegate?.didReceiveChannelLeave(channel, fromPeer)
```
> يُستدعى didReceiveChannelLeave على delegate إن لم يكن عدميّاً ممرّراً channel وfromPeer. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:444]

```
445:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:445]

```
446:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:446]

```
447:             override fun onDeliveryAckReceived(messageID: String, peerID: String) {
```
> تعريف دالّة متجاوِزة باسم عند استلام إقرار التّسليم (onDeliveryAckReceived) تأخذ معرّف الرّسالة messageID ومعرّف النّظير peerID نصّين. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:447]

```
448:                 delegate?.didReceiveDeliveryAck(messageID, peerID)
```
> يُستدعى didReceiveDeliveryAck على delegate إن لم يكن عدميّاً ممرّراً messageID وpeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:448]

```
449:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:449]

```
450:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:450]

```
451:             override fun onReadReceiptReceived(messageID: String, peerID: String) {
```
> تعريف دالّة متجاوِزة باسم عند استلام إيصال القراءة (onReadReceiptReceived) تأخذ messageID وpeerID نصّين. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:451]

```
452:                 delegate?.didReceiveReadReceipt(messageID, peerID)
```
> يُستدعى didReceiveReadReceipt على delegate إن لم يكن عدميّاً ممرّراً messageID وpeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:452]

```
453:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:453]

```
454:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:454]

```
455:             override fun onVerifyChallengeReceived(peerID: String, payload: ByteArray, timestampMs: Long) {
```
> تعريف دالّة متجاوِزة باسم عند استلام تحدّي التّحقّق (onVerifyChallengeReceived) تأخذ peerID نصّاً، وحمولة payload من نوع ByteArray، وطابعاً زمنيّاً بالمللي ثانية timestampMs من نوع Long. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:455]

```
456:                 delegate?.didReceiveVerifyChallenge(peerID, payload, timestampMs)
```
> يُستدعى didReceiveVerifyChallenge على delegate إن لم يكن عدميّاً ممرّراً peerID وpayload وtimestampMs. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:456]

```
457:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:457]

```
458:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:458]

```
459:             override fun onVerifyResponseReceived(peerID: String, payload: ByteArray, timestampMs: Long) {
```
> تعريف دالّة متجاوِزة باسم عند استلام ردّ التّحقّق (onVerifyResponseReceived) تأخذ peerID نصّاً، وحمولة payload من نوع ByteArray، وtimestampMs من نوع Long. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:459]

```
460:                 delegate?.didReceiveVerifyResponse(peerID, payload, timestampMs)
```
> يُستدعى didReceiveVerifyResponse على delegate إن لم يكن عدميّاً ممرّراً peerID وpayload وtimestampMs. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:460]

```
461:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:461]

```
462:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:462]

```
463:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:463]

```
464:         // PacketProcessor delegates
```
> تعليق: مُفوَّضو معالِج الرّزم (PacketProcessor). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:464]

```
465:         packetProcessor.delegate = object : PacketProcessorDelegate {
```
> يُسنَد إلى خاصّيّة delegate في معالِج الرّزم (packetProcessor) كائن مجهول (object) ينفّذ واجهة PacketProcessorDelegate. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:465]

```
466:             override fun validatePacketSecurity(packet: BitchatPacket, peerID: String): Boolean {
```
> تعريف دالّة متجاوِزة باسم التحقّق من أمان الرّزمة (validatePacketSecurity) تأخذ رزمة packet من نوع BitchatPacket ومعرّف نظير peerID، وتعيد قيمة منطقيّة Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:466]

```
467:                 return securityManager.validatePacket(packet, peerID)
```
> تُعيد نتيجة validatePacket على مدير الأمان (securityManager) ممرّراً packet وpeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:467]

```
468:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:468]

```
469:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:469]

```
470:             override fun updatePeerLastSeen(peerID: String) {
```
> تعريف دالّة متجاوِزة باسم تحديث آخر ظهور للنّظير (updatePeerLastSeen) تأخذ peerID نصّاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:470]

```
471:                 peerManager.updatePeerLastSeen(peerID)
```
> يُستدعى updatePeerLastSeen على peerManager ممرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:471]

```
472:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:472]

```
473:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:473]

```
474:             override fun getPeerNickname(peerID: String): String? {
```
> تعريف دالّة متجاوِزة باسم جلب كنية النّظير (getPeerNickname) تأخذ peerID نصّاً وتعيد نصّاً قابلاً للعدميّة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:474]

```
475:                 return peerManager.getPeerNickname(peerID)
```
> تُعيد نتيجة getPeerNickname على peerManager ممرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:475]

```
476:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:476]

```
477:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:477]

```
478:             // Network information for relay manager
```
> تعليق: معلومات الشّبكة لمدير التّتابُع (relay manager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:478]

```
479:             override fun getNetworkSize(): Int {
```
> تعريف دالّة متجاوِزة باسم جلب حجم الشّبكة (getNetworkSize) لا تأخذ وسائط وتعيد عدداً صحيحاً Int. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:479]

```
480:                 return peerManager.getActivePeerCount()
```
> تُعيد نتيجة getActivePeerCount (عدد النّظراء النّشطين) على peerManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:480]

```
481:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:481]

```
482:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:482]

```
483:             override fun getBroadcastRecipient(): ByteArray {
```
> تعريف دالّة متجاوِزة باسم جلب مُستقبِل البثّ (getBroadcastRecipient) لا تأخذ وسائط وتعيد ByteArray. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:483]

```
484:                 return SpecialRecipients.BROADCAST
```
> تُعيد الثّابت BROADCAST من المُستقبِلين الخاصّين (SpecialRecipients). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:484]

```
485:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:485]

```
486:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:486]

```
487:             override fun handleNoiseHandshake(routed: RoutedPacket): Boolean {
```
> تعريف دالّة متجاوِزة باسم معالجة مصافحة نويز (handleNoiseHandshake) تأخذ رزمة موجّهة routed من نوع RoutedPacket وتعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:487]

```
488:                 return runBlocking { securityManager.handleNoiseHandshake(routed) }
```
> تُعيد ناتج تشغيل حاجب (runBlocking) يستدعي داخله handleNoiseHandshake على securityManager ممرّراً routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:488]

```
489:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:489]

```
490:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:490]

```
491:             override fun handleNoiseEncrypted(routed: RoutedPacket) {
```
> تعريف دالّة متجاوِزة باسم معالجة المشفّر بنويز (handleNoiseEncrypted) تأخذ routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:491]

```
492:                 serviceScope.launch { messageHandler.handleNoiseEncrypted(routed) }
```
> يُطلَق (launch) ضمن نطاق الخدمة (serviceScope) كوروتين يستدعي handleNoiseEncrypted على معالِج الرّسائل (messageHandler) ممرّراً routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:492]

```
493:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:493]

```
494:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:494]

```
495:             override fun handleAnnounce(routed: RoutedPacket) {
```
> تعريف دالّة متجاوِزة باسم معالجة الإعلان (handleAnnounce) تأخذ routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:495]

```
496:                 serviceScope.launch {
```
> يُطلَق ضمن serviceScope كوروتين، بداية جسمه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:496]

```
497:                     // Process the announce
```
> تعليق: عالِج الإعلان. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:497]

```
498:                     val isFirst = messageHandler.handleAnnounce(routed)
```
> يُعرَّف متغيّر ثابت isFirst ويُسنَد إليه ناتج handleAnnounce على messageHandler ممرّراً routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:498]

```
499:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:499]

```
500:                     // Map device address -> peerID based on TTL (max TTL = direct neighbor)
```
> تعليق: اربط عنوان الجهاز إلى معرّف النّظير بناءً على مدّة البقاء TTL (أقصى TTL = جار مباشر). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:500]

```
501:                     // Matches iOS logic: any announce with max TTL on a link defines the direct peer
```
> تعليق: يطابق منطق iOS: أيّ إعلان بأقصى TTL على وصلة يحدّد النّظير المباشر. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:501]

```
502:                     val deviceAddress = routed.relayAddress
```
> يُعرَّف متغيّر ثابت deviceAddress ويُسنَد إليه عنوان التّتابُع (relayAddress) من routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:502]

```
503:                     val pid = routed.peerID
```
> يُعرَّف متغيّر ثابت pid ويُسنَد إليه معرّف النّظير (peerID) من routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:503]

```
504:                     if (deviceAddress != null && pid != null) {
```
> إذا لم يكن deviceAddress عدميّاً ولم يكن pid عدميّاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:504]

```
505:                         // Check if this is a direct connection (MAX TTL)
```
> تعليق: تحقّق إن كان هذا اتّصالاً مباشراً (أقصى TTL). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:505]

```
506:                         // Note: packet.ttl is UByte, compare with AppConstants.MESSAGE_TTL_HOPS
```
> تعليق: ملاحظة: packet.ttl من نوع UByte، قارِنه بـ AppConstants.MESSAGE_TTL_HOPS. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:506]

```
507:                         val isDirect = routed.packet.ttl == com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS
```
> يُعرَّف متغيّر ثابت isDirect ويُسنَد إليه نتيجة مقارنة ttl لرزمة routed بثابت MESSAGE_TTL_HOPS في AppConstants. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:507]

```
508:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:508]

```
509:                         if (isDirect) {
```
> إذا كان isDirect صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:509]

```
510:                             // Bind or rebind this device address to the announcing peer
```
> تعليق: اربط أو أعِد ربط عنوان الجهاز هذا بالنّظير المُعلِن. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:510]

```
511:                             connectionManager.addressPeerMap[deviceAddress] = pid
```
> يُسنَد pid إلى المدخل deviceAddress في خريطة عناوين-النّظراء (addressPeerMap) لمدير الاتّصال (connectionManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:511]

```
512:                             Log.d(TAG, "Mapped device $deviceAddress to peer $pid (TTL=${routed.packet.ttl})")
```
> يُستدعى Log.d مع TAG ونصّ يقول إنّ الجهاز deviceAddress رُبِط بالنّظير pid مع عرض ttl لرزمة routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:512]

```
513:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:513]

```
514:                             // Mark as directly connected - refresh UI state
```
> تعليق: علِّمه كمتّصل مباشرة - حدِّث حالة الواجهة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:514]

```
515:                             try { peerManager.refreshPeerList() } catch (_: Exception) { }
```
> داخل محاولة يُستدعى refreshPeerList (تحديث قائمة النّظراء) على peerManager، وكتلة التقاط أيّ استثناء فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:515]

```
516:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:516]

```
517:                             // Initial sync for this direct peer
```
> تعليق: مزامنة أوّليّة لهذا النّظير المباشر. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:517]

```
518:                             try { gossipSyncManager.scheduleInitialSyncToPeer(pid, 1_000) } catch (_: Exception) { }
```
> داخل محاولة يُستدعى scheduleInitialSyncToPeer (جدولة مزامنة أوّليّة إلى النّظير) على مدير مزامنة النّميمة (gossipSyncManager) ممرّراً pid والقيمة ١٠٠٠، وكتلة التقاط أيّ استثناء فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:518]

```
519:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:519]

```
520:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:520]

```
521:                     // Track for sync
```
> تعليق: تتبّع للمزامنة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:521]

```
522:                     try { gossipSyncManager.onPublicPacketSeen(routed.packet) } catch (_: Exception) { }
```
> داخل محاولة يُستدعى onPublicPacketSeen (عند رؤية رزمة عامّة) على gossipSyncManager ممرّراً رزمة routed، وكتلة التقاط أيّ استثناء فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:522]

```
523:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:523]

```
524:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:524]

```
525:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:525]

```
526:             override fun handleMessage(routed: RoutedPacket) {
```
> تعريف دالّة متجاوِزة باسم معالجة الرّسالة (handleMessage) تأخذ routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:526]

```
527:                 serviceScope.launch { messageHandler.handleMessage(routed) }
```
> يُطلَق ضمن serviceScope كوروتين يستدعي handleMessage على messageHandler ممرّراً routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:527]

```
528:                 // Track broadcast messages for sync
```
> تعليق: تتبّع رسائل البثّ للمزامنة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:528]

```
529:                 try {
```
> بداية كتلة محاولة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:529]

```
530:                     val pkt = routed.packet
```
> يُعرَّف متغيّر ثابت pkt ويُسنَد إليه رزمة (packet) من routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:530]

```
531:                     val isBroadcast = (pkt.recipientID == null || pkt.recipientID.contentEquals(SpecialRecipients.BROADCAST))
```
> يُعرَّف متغيّر ثابت isBroadcast ويُسنَد إليه قيمة منطقيّة صحيحة إن كان معرّف المُستقبِل (recipientID) لـ pkt عدميّاً أو ساوى محتواه (contentEquals) ثابت BROADCAST. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:531]

```
532:                     if (isBroadcast && pkt.type == MessageType.MESSAGE.value) {
```
> إذا كان isBroadcast صحيحاً ونوع pkt يساوي قيمة (value) النّوع MESSAGE من MessageType. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:532]

```
533:                         gossipSyncManager.onPublicPacketSeen(pkt)
```
> يُستدعى onPublicPacketSeen على gossipSyncManager ممرّراً pkt. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:533]

```
534:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:534]

```
535:                 } catch (_: Exception) { }
```
> كتلة التقاط لأيّ استثناء باسم مُهمَل، وجسمها فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:535]

```
536:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:536]

```
537:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:537]

```
538:             override fun handleLeave(routed: RoutedPacket) {
```
> تعريف دالّة متجاوِزة باسم معالجة المغادرة (handleLeave) تأخذ routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:538]

```
539:                 serviceScope.launch { messageHandler.handleLeave(routed) }
```
> يُطلَق ضمن serviceScope كوروتين يستدعي handleLeave على messageHandler ممرّراً routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:539]

```
540:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:540]

```
541:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:541]

```
542:             override fun handleFragment(packet: BitchatPacket): BitchatPacket? {
```
> تعريف دالّة متجاوِزة باسم معالجة الشّظيّة (handleFragment) تأخذ رزمة packet من نوع BitchatPacket وتعيد BitchatPacket قابلاً للعدميّة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:542]

```
543:                 // Track broadcast fragments for gossip sync
```
> تعليق: تتبّع شظايا البثّ لمزامنة النّميمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:543]

```
544:                 try {
```
> بداية كتلة محاولة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:544]

```
545:                     val isBroadcast = (packet.recipientID == null || packet.recipientID.contentEquals(SpecialRecipients.BROADCAST))
```
> يُعرَّف متغيّر ثابت isBroadcast ويُسنَد إليه قيمة منطقيّة صحيحة إن كان recipientID لـ packet عدميّاً أو ساوى محتواه ثابت BROADCAST. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:545]

```
546:                     if (isBroadcast && packet.type == MessageType.FRAGMENT.value) {
```
> إذا كان isBroadcast صحيحاً ونوع packet يساوي قيمة النّوع FRAGMENT من MessageType. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:546]

```
547:                         gossipSyncManager.onPublicPacketSeen(packet)
```
> يُستدعى onPublicPacketSeen على gossipSyncManager ممرّراً packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:547]

```
548:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:548]

```
549:                 } catch (_: Exception) { }
```
> كتلة التقاط لأيّ استثناء باسم مُهمَل، وجسمها فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:549]

```
550:                 return fragmentManager.handleFragment(packet)
```
> تُعيد نتيجة handleFragment على مدير الشّظايا (fragmentManager) ممرّراً packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:550]

```
551:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:551]

```
552:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:552]

```
553:             override fun sendAnnouncementToPeer(peerID: String) {
```
> تعريف دالّة متجاوِزة باسم إرسال إعلان إلى النّظير (sendAnnouncementToPeer) تأخذ peerID نصّاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:553]

```
554:                 this@BluetoothMeshService.sendAnnouncementToPeer(peerID)
```
> يُستدعى sendAnnouncementToPeer على الكائن الخارجيّ BluetoothMeshService (this@) ممرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:554]

```
555:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:555]

```
556:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:556]

```
557:             override fun sendCachedMessages(peerID: String) {
```
> تعريف دالّة متجاوِزة باسم إرسال الرّسائل المخزّنة (sendCachedMessages) تأخذ peerID نصّاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:557]

```
558:                 storeForwardManager.sendCachedMessages(peerID)
```
> يُستدعى sendCachedMessages على مدير التّخزين والتّمرير (storeForwardManager) ممرّراً peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:558]

```
559:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:559]

```
560:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:560]

```
561:             override fun relayPacket(routed: RoutedPacket) {
```
> تعريف دالّة متجاوِزة باسم تتابُع الرّزمة (relayPacket) تأخذ routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:561]

```
562:                 broadcastRoutedPacket(routed)
```
> يُستدعى بثّ الرّزمة الموجّهة (broadcastRoutedPacket) ممرّراً routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:562]

```
563:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:563]

```
564:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:564]

```
565:             override fun sendToPeer(peerID: String, routed: RoutedPacket): Boolean {
```
> تعريف دالّة متجاوِزة باسم إرسال إلى النّظير (sendToPeer) تأخذ peerID نصّاً وrouted من نوع RoutedPacket، وتعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:565]

```
566:                 val sentOverBle = connectionManager.sendToPeer(peerID, routed)
```
> يُعرَّف متغيّر ثابت sentOverBle ويُسنَد إليه ناتج sendToPeer على connectionManager ممرّراً peerID وrouted. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:566]

```
567:                 TransportBridgeService.sendToPeer("BLE", peerID, routed.packet)
```
> يُستدعى sendToPeer على خدمة جسر النّقل (TransportBridgeService) ممرّراً النّصّ "BLE" وpeerID ورزمة routed. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:567]

```
568:                 return sentOverBle
```
> تُعيد قيمة sentOverBle. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:568]

```
569:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:569]

```
570:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:570]

```
571:             override fun handleRequestSync(routed: RoutedPacket) {
```
> تعريف دالّة متجاوِزة باسم معالجة طلب المزامنة (handleRequestSync) تأخذ routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:571]

```
572:                 // Decode request and respond with missing packets
```
> تعليق: فُكّ ترميز الطّلب ورُدّ بالرّزم المفقودة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:572]

```
573:                 val fromPeer = routed.peerID ?: return
```
> يُعرَّف متغيّر ثابت fromPeer ويُسنَد إليه peerID من routed، وإن كان عدميّاً يُعاد (return) من الدّالّة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:573]

```
574:                 val req = RequestSyncPacket.decode(routed.packet.payload) ?: return
```
> يُعرَّف متغيّر ثابت req ويُسنَد إليه ناتج decode على RequestSyncPacket لحمولة (payload) رزمة routed، وإن كان عدميّاً يُعاد من الدّالّة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:574]

```
575:                 gossipSyncManager.handleRequestSync(fromPeer, req)
```
> يُستدعى handleRequestSync على gossipSyncManager ممرّراً fromPeer وreq. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:575]

```
576:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:576]

```
577:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:577]

```
578:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:578]

```
579:         // BluetoothConnectionManager delegates
```
> تعليق: مُفوَّضو مدير اتّصال البلوتوث (BluetoothConnectionManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:579]

```
580:         connectionManager.delegate = object : BluetoothConnectionManagerDelegate {
```
> يُسنَد إلى خاصّيّة delegate في connectionManager كائن مجهول ينفّذ واجهة BluetoothConnectionManagerDelegate. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:580]

```
581:         override fun onPacketReceived(packet: BitchatPacket, peerID: String, device: android.bluetooth.BluetoothDevice?) {
```
> تعريف دالّة متجاوِزة باسم عند استلام الرّزمة (onPacketReceived) تأخذ رزمة packet من نوع BitchatPacket، وpeerID نصّاً، وجهاز device من نوع android.bluetooth.BluetoothDevice قابل للعدميّة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:581]

```
582:             // Log incoming for debug graphs (do not double-count anywhere else)
```
> تعليق: سجّل الوارد لرسوم التّنقيح (لا تعدّه مرّتين في أيّ مكان آخر). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:582]

```
583:             try {
```
> بداية كتلة محاولة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:583]

```
584:                 com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().logIncoming(
```
> يُستدعى getInstance على مدير إعدادات التّنقيح (DebugSettingsManager) ثم logIncoming (تسجيل الوارد)، بداية قائمة وسائطه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:584]

```
585:                     packet = packet,
```
> يُمرَّر الوسيط المُسمّى packet بالقيمة packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:585]

```
586:                     fromPeerID = peerID,
```
> يُمرَّر الوسيط المُسمّى fromPeerID بالقيمة peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:586]

```
587:                     fromNickname = null,
```
> يُمرَّر الوسيط المُسمّى fromNickname بالقيمة null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:587]

```
588:                     fromDeviceAddress = device?.address,
```
> يُمرَّر الوسيط المُسمّى fromDeviceAddress بقيمة عنوان (address) الجهاز device إن لم يكن عدميّاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:588]

```
589:                     myPeerID = myPeerID
```
> يُمرَّر الوسيط المُسمّى myPeerID بالقيمة myPeerID (معرّف نظيري). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:589]

```
590:                 )
```
> إغلاق قائمة وسائط الاستدعاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:590]

```
591:             } catch (_: Exception) { }
```
> كتلة التقاط لأيّ استثناء باسم مُهمَل، وجسمها فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:591]

```
592:             packetProcessor.processPacket(RoutedPacket(packet, peerID, device?.address))
```
> يُستدعى processPacket (معالجة الرّزمة) على packetProcessor ممرّراً RoutedPacket مُنشأ من packet وpeerID وعنوان device إن لم يكن عدميّاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:592]

```
593:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:593]

```
594:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:594]

```
595:             override fun onDeviceConnected(device: android.bluetooth.BluetoothDevice) {
```
> تعريف دالّة متجاوِزة باسم عند اتّصال الجهاز (onDeviceConnected) تأخذ جهاز device من نوع android.bluetooth.BluetoothDevice. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:595]

```
596:                 // Send initial announcements after services are ready
```
> تعليق: أرسِل الإعلانات الأوّليّة بعد جاهزيّة الخدمات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:596]

```
597:                 serviceScope.launch {
```
> يُطلَق ضمن serviceScope كوروتين، بداية جسمه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:597]

```
598:                     Log.d(TAG, "Device connected: ${device.address}; scheduling announce")
```
> يُستدعى Log.d مع TAG ونصّ يقول إنّ الجهاز اتّصل ويعرض عنوان (address) الجهاز device ويذكر جدولة الإعلان. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:598]

```
599:                     delay(200)
```
> يُستدعى تأخير (delay) بمقدار ٢٠٠ مللي ثانية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:599]

```
600:                     sendBroadcastAnnounce()
```
> يُستدعى إرسال إعلان البثّ (sendBroadcastAnnounce). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:600]
