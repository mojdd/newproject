# شريحة — app/src/main/java/com/bitchat/android/mesh/PeerManager.kt (الأسطر 401–558)

```
401:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:401]

```
402:      * Get debug information with device addresses
```
> تعليق: احصل على معلومات التصحيح (debug) مع عناوين الأجهزة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:402]

```
403:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:403]

```
404:     fun getDebugInfoWithDeviceAddresses(addressPeerMap: Map<String, String>): String {
```
> تعريف دالة (getDebugInfoWithDeviceAddresses) باسم «احصل على معلومات التصحيح مع عناوين الأجهزة» تأخذ خريطة (addressPeerMap) من نوع Map من نص إلى نص وتعيد نصاً (String). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:404]

```
405:         return buildString {
```
> تُعيد ناتج بناء نص عبر دالة بناء النص (buildString) مع كتلة لاحقة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:405]

```
406:             appendLine("=== Device Address to Peer Mapping ===")
```
> يُلحِق سطراً (appendLine) نصه «=== Device Address to Peer Mapping ===». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:406]

```
407:             if (addressPeerMap.isEmpty()) {
```
> شرط (if) يختبر إن كانت الخريطة (addressPeerMap) فارغة (isEmpty). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:407]

```
408:                 appendLine("No device address mappings available")
```
> يُلحِق سطراً نصه «No device address mappings available». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:408]

```
409:             } else {
```
> إغلاق كتلة الشرط وبداية كتلة وإلّا (else). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:409]

```
410:                 addressPeerMap.forEach { (deviceAddress, peerID) ->
```
> يمرّ على كل عنصر في الخريطة (forEach) مفكّكاً كل زوج إلى عنوان الجهاز (deviceAddress) ومعرّف النظير (peerID). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:410]

```
411:                     val nickname = peers[peerID]?.nickname ?: "Unknown"
```
> يُعرّف ثابتاً (nickname) قيمته الاسم المستعار للنظير الموجود في خريطة النظراء (peers) عند المعرّف، وإن كان غير موجود فقيمته «Unknown». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:411]

```
412:                     val isActive = isPeerActive(peerID)
```
> يُعرّف ثابتاً (isActive) قيمته ناتج استدعاء دالة «هل النظير نشط» (isPeerActive) بالمعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:412]

```
413:                     val status = if (isActive) "ACTIVE" else "INACTIVE"
```
> يُعرّف ثابتاً (status) قيمته «ACTIVE» إن كان نشطاً وإلّا «INACTIVE». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:413]

```
414:                     appendLine("  Device: $deviceAddress -> Peer: $peerID ($nickname) [$status]")
```
> يُلحِق سطراً نصه مركّب من «  Device: » ثم عنوان الجهاز ثم « -> Peer: » ثم المعرّف ثم الاسم المستعار بين قوسين ثم الحالة بين قوسين مربّعين. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:414]

```
415:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:415]

```
416:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:416]

```
417:             appendLine()
```
> يُلحِق سطراً فارغاً (appendLine بلا وسيط). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:417]

```
418:             appendLine(getDebugInfo(addressPeerMap))
```
> يُلحِق سطراً نصه ناتج استدعاء دالة معلومات التصحيح (getDebugInfo) بالخريطة (addressPeerMap). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:418]

```
419:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:419]

```
420:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:420]

```
421:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:421]

```
422:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:422]

```
423:      * Notify delegate of peer list updates
```
> تعليق: أبلِغ المفوَّض (delegate) بتحديثات قائمة النظراء. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:423]

```
424:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:424]

```
425:     private fun notifyPeerListUpdate() {
```
> تعريف دالة خاصّة (private) باسم «أبلِغ بتحديث قائمة النظراء» (notifyPeerListUpdate) بلا وسائط ولا قيمة معادة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:425]

```
426:         val peerList = getActivePeerIDs()
```
> يُعرّف ثابتاً (peerList) قيمته ناتج استدعاء دالة «احصل على معرّفات النظراء النشطين» (getActivePeerIDs). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:426]

```
427:         delegate?.onPeerListUpdated(peerList)
```
> يستدعي على المفوَّض (delegate) إن لم يكن فارغاً دالة «عند تحديث قائمة النظراء» (onPeerListUpdated) بقائمة النظراء. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:427]

```
428:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:428]

```
429: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:429]

```
430:     fun refreshPeerList() {
```
> تعريف دالة (refreshPeerList) باسم «حدِّث قائمة النظراء» بلا وسائط ولا قيمة معادة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:430]

```
431:         notifyPeerListUpdate()
```
> يستدعي دالة «أبلِغ بتحديث قائمة النظراء» (notifyPeerListUpdate). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:431]

```
432:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:432]

```
433:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:433]

```
434:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:434]

```
435:      * Start periodic cleanup of stale peers
```
> تعليق: ابدأ التنظيف الدوري للنظراء القدامى (stale). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:435]

```
436:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:436]

```
437:     private fun startPeriodicCleanup() {
```
> تعريف دالة خاصّة (private) باسم «ابدأ التنظيف الدوري» (startPeriodicCleanup) بلا وسائط ولا قيمة معادة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:437]

```
438:         managerScope.launch {
```
> يطلق مهمّة متزامنة (launch) على نطاق المدير (managerScope) مع كتلة لاحقة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:438]

```
439:             while (isActive) {
```
> حلقة طالما (while) تستمر ما دام النطاق نشطاً (isActive). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:439]

```
440:                 delay(com.bitchat.android.util.AppConstants.Mesh.PEER_CLEANUP_INTERVAL_MS)
```
> ينتظر (delay) مدّةً بقيمة الثابت فترة تنظيف النظراء بالمللي ثانية (PEER_CLEANUP_INTERVAL_MS) من الثوابت (AppConstants.Mesh). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:440]

```
441:                 cleanupStalePeers()
```
> يستدعي دالة «نظّف النظراء القدامى» (cleanupStalePeers). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:441]

```
442:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:442]

```
443:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:443]

```
444:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:444]

```
445:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:445]

```
446:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:446]

```
447:      * Clean up stale peers (same 3-minute threshold as iOS)
```
> تعليق: نظّف النظراء القدامى (بنفس عتبة الثلاث دقائق المستعملة في iOS). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:447]

```
448:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:448]

```
449:     private fun cleanupStalePeers() {
```
> تعريف دالة خاصّة (private) باسم «نظّف النظراء القدامى» (cleanupStalePeers) بلا وسائط ولا قيمة معادة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:449]

```
450:         val now = System.currentTimeMillis()
```
> يُعرّف ثابتاً (now) قيمته الوقت الحالي بالمللي ثانية من النظام (System.currentTimeMillis). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:450]

```
451:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:451]

```
452:         val peersToRemove = peers.filterValues { (now - it.lastSeen) > stalePeerTimeoutMs }
```
> يُعرّف ثابتاً (peersToRemove) قيمته نتيجة ترشيح قيم خريطة النظراء (filterValues) حيث يكون الفرق بين الوقت الحالي (now) وآخر مشاهدة (lastSeen) أكبر من مهلة قِدَم النظير بالمللي ثانية (stalePeerTimeoutMs). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:452]

```
453:             .keys
```
> يأخذ المفاتيح (keys) من نتيجة الترشيح. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:453]

```
454:             .toList()
```
> يحوّل المفاتيح إلى قائمة (toList). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:454]

```
455:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:455]

```
456:         peersToRemove.forEach { peerID ->
```
> يمرّ على كل عنصر في قائمة النظراء المطلوب إزالتها (forEach) مسمّياً كل عنصر معرّف النظير (peerID). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:456]

```
457:             Log.d(TAG, "Removing stale peer: $peerID")
```
> يسجّل رسالة تصحيح (Log.d) بالوسم (TAG) نصها «Removing stale peer: » متبوعاً بالمعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:457]

```
458:             removePeer(peerID)
```
> يستدعي دالة «أزِل النظير» (removePeer) بالمعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:458]

```
459:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:459]

```
460:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:460]

```
461:         if (peersToRemove.isNotEmpty()) {
```
> شرط (if) يختبر إن كانت قائمة النظراء المطلوب إزالتها غير فارغة (isNotEmpty). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:461]

```
462:             Log.d(TAG, "Cleaned up ${peersToRemove.size} stale peers")
```
> يسجّل رسالة تصحيح (Log.d) بالوسم (TAG) نصها «Cleaned up » متبوعاً بعدد العناصر (size) ثم « stale peers». [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:462]

```
463:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:463]

```
464:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:464]

```
465:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:465]

```
466:     // MARK: - Fingerprint Management (Centralized)
```
> تعليق: علامة قسم — إدارة البصمات (Fingerprint) (مركزية). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:466]

```
467:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:467]

```
468:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:468]

```
469:      * Store fingerprint for a peer after successful Noise handshake
```
> تعليق: خزّن بصمة لنظير بعد نجاح مصافحة Noise (handshake). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:469]

```
470:      * This should only be called when a Noise session is established
```
> تعليق: ينبغي استدعاء هذا فقط عند تأسيس جلسة Noise. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:470]

```
471:      * 
```
> تعليق: سطر فارغ داخل التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:471]

```
472:      * @param peerID The peer's ID
```
> تعليق: الوسيط (peerID) هو معرّف النظير. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:472]

```
473:      * @param publicKey The peer's static public key from Noise handshake
```
> تعليق: الوسيط (publicKey) هو المفتاح العام الثابت للنظير من مصافحة Noise. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:473]

```
474:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:474]

```
475:     fun storeFingerprintForPeer(peerID: String, publicKey: ByteArray): String {
```
> تعريف دالة (storeFingerprintForPeer) باسم «خزّن البصمة لنظير» تأخذ معرّف النظير (peerID) نصاً والمفتاح العام (publicKey) مصفوفة بايتات (ByteArray) وتعيد نصاً (String). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:475]

```
476:         return fingerprintManager.storeFingerprintForPeer(peerID, publicKey)
```
> تُعيد ناتج استدعاء دالة «خزّن البصمة لنظير» على مدير البصمات (fingerprintManager) بالمعرّف والمفتاح العام. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:476]

```
477:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:477]

```
478:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:478]

```
479:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:479]

```
480:      * Update peer ID mapping for peer ID rotation
```
> تعليق: حدّث ربط معرّف النظير من أجل تدوير المعرّف (rotation). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:480]

```
481:      * 
```
> تعليق: سطر فارغ داخل التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:481]

```
482:      * @param oldPeerID The previous peer ID (nullable)
```
> تعليق: الوسيط (oldPeerID) هو معرّف النظير السابق (قابل للقيمة الفارغة). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:482]

```
483:      * @param newPeerID The new peer ID
```
> تعليق: الوسيط (newPeerID) هو معرّف النظير الجديد. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:483]

```
484:      * @param fingerprint The persistent fingerprint
```
> تعليق: الوسيط (fingerprint) هو البصمة الدائمة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:484]

```
485:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:485]

```
486:     fun updatePeerIDMapping(oldPeerID: String?, newPeerID: String, fingerprint: String) {
```
> تعريف دالة (updatePeerIDMapping) باسم «حدّث ربط معرّف النظير» تأخذ المعرّف السابق (oldPeerID) نصاً قابلاً للفراغ والمعرّف الجديد (newPeerID) نصاً والبصمة (fingerprint) نصاً، بلا قيمة معادة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:486]

```
487:         fingerprintManager.updatePeerIDMapping(oldPeerID, newPeerID, fingerprint)
```
> يستدعي دالة «حدّث ربط معرّف النظير» على مدير البصمات (fingerprintManager) بالمعرّف السابق والجديد والبصمة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:487]

```
488:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:488]

```
489:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:489]

```
490:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:490]

```
491:      * Get fingerprint for a specific peer
```
> تعليق: احصل على البصمة لنظير محدّد. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:491]

```
492:      * 
```
> تعليق: سطر فارغ داخل التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:492]

```
493:      * @param peerID The peer ID to look up
```
> تعليق: الوسيط (peerID) هو معرّف النظير المراد البحث عنه. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:493]

```
494:      * @return The fingerprint if found, null otherwise
```
> تعليق: القيمة المعادة هي البصمة إن وُجدت، وإلّا فارغة (null). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:494]

```
495:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:495]

```
496:     fun getFingerprintForPeer(peerID: String): String? {
```
> تعريف دالة (getFingerprintForPeer) باسم «احصل على البصمة لنظير» تأخذ معرّف النظير (peerID) نصاً وتعيد نصاً قابلاً للفراغ (String?). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:496]

```
497:         return fingerprintManager.getFingerprintForPeer(peerID)
```
> تُعيد ناتج استدعاء دالة «احصل على البصمة لنظير» على مدير البصمات (fingerprintManager) بالمعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:497]

```
498:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:498]

```
499:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:499]

```
500:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:500]

```
501:      * Get current peer ID for a specific fingerprint
```
> تعليق: احصل على معرّف النظير الحالي لبصمة محدّدة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:501]

```
502:      * 
```
> تعليق: سطر فارغ داخل التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:502]

```
503:      * @param fingerprint The fingerprint to look up
```
> تعليق: الوسيط (fingerprint) هو البصمة المراد البحث عنها. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:503]

```
504:      * @return The current peer ID if found, null otherwise
```
> تعليق: القيمة المعادة هي معرّف النظير الحالي إن وُجد، وإلّا فارغة (null). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:504]

```
505:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:505]

```
506:     fun getPeerIDForFingerprint(fingerprint: String): String? {
```
> تعريف دالة (getPeerIDForFingerprint) باسم «احصل على معرّف النظير لبصمة» تأخذ البصمة (fingerprint) نصاً وتعيد نصاً قابلاً للفراغ (String?). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:506]

```
507:         return fingerprintManager.getPeerIDForFingerprint(fingerprint)
```
> تُعيد ناتج استدعاء دالة «احصل على معرّف النظير لبصمة» على مدير البصمات (fingerprintManager) بالبصمة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:507]

```
508:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:508]

```
509:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:509]

```
510:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:510]

```
511:      * Check if we have a fingerprint for a specific peer
```
> تعليق: تحقّق إن كنّا نملك بصمة لنظير محدّد. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:511]

```
512:      * 
```
> تعليق: سطر فارغ داخل التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:512]

```
513:      * @param peerID The peer ID to check
```
> تعليق: الوسيط (peerID) هو معرّف النظير المراد التحقّق منه. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:513]

```
514:      * @return True if we have a fingerprint for this peer, false otherwise
```
> تعليق: القيمة المعادة صحيحة (true) إن كنّا نملك بصمة لهذا النظير، وإلّا خطأ (false). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:514]

```
515:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:515]

```
516:     fun hasFingerprintForPeer(peerID: String): Boolean {
```
> تعريف دالة (hasFingerprintForPeer) باسم «هل نملك بصمة لنظير» تأخذ معرّف النظير (peerID) نصاً وتعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:516]

```
517:         return fingerprintManager.hasFingerprintForPeer(peerID)
```
> تُعيد ناتج استدعاء دالة «هل نملك بصمة لنظير» على مدير البصمات (fingerprintManager) بالمعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:517]

```
518:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:518]

```
519:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:519]

```
520:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:520]

```
521:      * Get all current peer ID to fingerprint mappings
```
> تعليق: احصل على كل روابط معرّف النظير الحالية إلى البصمة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:521]

```
522:      * 
```
> تعليق: سطر فارغ داخل التوثيق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:522]

```
523:      * @return Immutable copy of all mappings
```
> تعليق: القيمة المعادة نسخة غير قابلة للتعديل (immutable) من كل الروابط. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:523]

```
524:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:524]

```
525:     fun getAllPeerFingerprints(): Map<String, String> {
```
> تعريف دالة (getAllPeerFingerprints) باسم «احصل على كل بصمات النظراء» بلا وسائط وتعيد خريطة (Map) من نص إلى نص. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:525]

```
526:         return fingerprintManager.getAllPeerFingerprints()
```
> تُعيد ناتج استدعاء دالة «احصل على كل بصمات النظراء» على مدير البصمات (fingerprintManager). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:526]

```
527:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:527]

```
528:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:528]

```
529:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:529]

```
530:      * Clear all fingerprint mappings (used for emergency clear)
```
> تعليق: امسح كل روابط البصمات (يُستعمل للمسح الطارئ). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:530]

```
531:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:531]

```
532:     fun clearAllFingerprints() {
```
> تعريف دالة (clearAllFingerprints) باسم «امسح كل البصمات» بلا وسائط ولا قيمة معادة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:532]

```
533:         fingerprintManager.clearAllFingerprints()
```
> يستدعي دالة «امسح كل البصمات» على مدير البصمات (fingerprintManager). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:533]

```
534:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:534]

```
535:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:535]

```
536:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:536]

```
537:      * Get fingerprint manager debug info
```
> تعليق: احصل على معلومات تصحيح مدير البصمات. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:537]

```
538:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:538]

```
539:     fun getFingerprintDebugInfo(): String {
```
> تعريف دالة (getFingerprintDebugInfo) باسم «احصل على معلومات تصحيح البصمات» بلا وسائط وتعيد نصاً (String). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:539]

```
540:         return fingerprintManager.getDebugInfo()
```
> تُعيد ناتج استدعاء دالة «احصل على معلومات التصحيح» (getDebugInfo) على مدير البصمات (fingerprintManager). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:540]

```
541:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:541]

```
542:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:542]

```
543:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:543]

```
544:      * Shutdown the manager
```
> تعليق: أوقِف المدير (manager). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:544]

```
545:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:545]

```
546:     fun shutdown() {
```
> تعريف دالة (shutdown) باسم «أوقِف» بلا وسائط ولا قيمة معادة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:546]

```
547:         managerScope.cancel()
```
> يستدعي إلغاء (cancel) على نطاق المدير (managerScope). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:547]

```
548:         clearAllPeers()
```
> يستدعي دالة «امسح كل النظراء» (clearAllPeers). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:548]

```
549:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:549]

```
550: }
```
> إغلاق نطاق صنف PeerManager. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:550]

```
551: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:551]

```
552: /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:552]

```
553:  * Delegate interface for peer manager callbacks
```
> تعليق: واجهة مفوَّض (Delegate interface) لردود نداء مدير النظراء (callbacks). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:553]

```
554:  */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:554]

```
555: interface PeerManagerDelegate {
```
> تعريف واجهة (interface) باسم «مفوَّض مدير النظراء» (PeerManagerDelegate). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:555]

```
556:     fun onPeerListUpdated(peerIDs: List<String>)
```
> تصريح دالة (onPeerListUpdated) باسم «عند تحديث قائمة النظراء» تأخذ معرّفات النظراء (peerIDs) قائمة نصوص (List<String>) بلا جسم. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:556]

```
557:     fun onPeerRemoved(peerID: String)
```
> تصريح دالة (onPeerRemoved) باسم «عند إزالة النظير» تأخذ معرّف النظير (peerID) نصاً بلا جسم. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:557]

```
558: }
```
> إغلاق نطاق الواجهة PeerManagerDelegate. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:558]
