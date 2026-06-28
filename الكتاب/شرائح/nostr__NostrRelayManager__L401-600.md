# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt (الأسطر 401–600)

```
401:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:401]

```
402:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:402]

```
403:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:403]

```
404:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:404]

```
405:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:405]

```
406:      * Manually retry connection to a specific relay
```
> تعليق: إعادة محاولة الاتصال يدوياً بمُرحِّل (relay) محدد. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:406]

```
407:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:407]

```
408:     fun retryConnection(relayUrl: String) {
```
> تعريف دالة إعادة المحاولة (retryConnection) التي تأخذ مُعامِلاً نصياً اسمه عنوان المُرحِّل (relayUrl) من نوع نص (String). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:408]

```
409:         val relay = relaysList.find { it.url == relayUrl } ?: return
```
> تعريف متغير ثابت اسمه مُرحِّل (relay) يساوي أول عنصر في قائمة المُرحِّلات (relaysList) يكون عنوانه (url) مساوياً لعنوان المُرحِّل، وإن لم يوجد فإنه يُنفِّذ عودة (return) من الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:409]

```
410:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:410]

```
411:         // Reset reconnection attempts
```
> تعليق: إعادة تصفير محاولات إعادة الاتصال. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:411]

```
412:         relay.reconnectAttempts = 0
```
> يُسنِد القيمة صفر إلى الحقل محاولات إعادة الاتصال (reconnectAttempts) في المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:412]

```
413:         relay.nextReconnectTime = null
```
> يُسنِد القيمة null إلى الحقل وقت إعادة الاتصال التالي (nextReconnectTime) في المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:413]

```
414:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:414]

```
415:         // Disconnect if connected
```
> تعليق: قطع الاتصال إن كان متصلاً. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:415]

```
416:         connections[relayUrl]?.close(1000, "Manual retry")
```
> يستدعي الدالة إغلاق (close) على عنصر الاتصالات (connections) المقابل لعنوان المُرحِّل إن لم يكن null، بالرمز 1000 والنص "Manual retry". [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:416]

```
417:         connections.remove(relayUrl)
```
> يستدعي الدالة إزالة (remove) على خريطة الاتصالات (connections) لحذف المدخل المقابل لعنوان المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:417]

```
418:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:418]

```
419:         // Attempt immediate reconnection
```
> تعليق: محاولة إعادة الاتصال فوراً. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:419]

```
420:         scope.launch {
```
> يستدعي الدالة إطلاق (launch) على النطاق (scope) لبدء مهمة غير متزامنة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:420]

```
421:             connectToRelay(relayUrl)
```
> يستدعي الدالة الاتصال بالمُرحِّل (connectToRelay) ممرّراً عنوان المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:421]

```
422:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:422]

```
423:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:423]

```
424:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:424]

```
425:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:425]

```
426:      * Reset all relay connections
```
> تعليق: إعادة تعيين كل اتصالات المُرحِّلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:426]

```
427:      * This will automatically restore all subscriptions when reconnected
```
> تعليق: هذا سيستعيد كل الاشتراكات تلقائياً عند إعادة الاتصال. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:427]

```
428:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:428]

```
429:     fun resetAllConnections() {
```
> تعريف دالة إعادة تعيين كل الاتصالات (resetAllConnections) بلا مُعامِلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:429]

```
430:         disconnect()
```
> يستدعي الدالة قطع الاتصال (disconnect). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:430]

```
431:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:431]

```
432:         // Reset all relay states
```
> تعليق: إعادة تعيين كل حالات المُرحِّلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:432]

```
433:         relaysList.forEach { relay ->
```
> يستدعي الدالة لكل عنصر (forEach) على قائمة المُرحِّلات (relaysList) بمُعامِل اسمه مُرحِّل (relay). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:433]

```
434:             relay.reconnectAttempts = 0
```
> يُسنِد القيمة صفر إلى الحقل محاولات إعادة الاتصال (reconnectAttempts) في المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:434]

```
435:             relay.nextReconnectTime = null
```
> يُسنِد القيمة null إلى الحقل وقت إعادة الاتصال التالي (nextReconnectTime) في المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:435]

```
436:             relay.lastError = null
```
> يُسنِد القيمة null إلى الحقل آخر خطأ (lastError) في المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:436]

```
437:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:437]

```
438:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:438]

```
439:         // Reconnect - subscriptions will be automatically restored in onOpen
```
> تعليق: إعادة الاتصال — الاشتراكات ستُستعاد تلقائياً في onOpen. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:439]

```
440:         connect()
```
> يستدعي الدالة اتصال (connect). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:440]

```
441:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:441]

```
442:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:442]

```
443:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:443]

```
444:      * Force re-establishment of all subscriptions on currently connected relays
```
> تعليق: فرض إعادة إنشاء كل الاشتراكات على المُرحِّلات المتصلة حالياً. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:444]

```
445:      * Useful for ensuring subscription consistency after network issues
```
> تعليق: مفيد لضمان اتساق الاشتراكات بعد مشكلات الشبكة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:445]

```
446:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:446]

```
447:     fun reestablishAllSubscriptions() {
```
> تعريف دالة إعادة إنشاء كل الاشتراكات (reestablishAllSubscriptions) بلا مُعامِلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:447]

```
448:         Log.d(TAG, "🔄 Force re-establishing all ${activeSubscriptions.size} active subscriptions")
```
> يستدعي دالة السجل التصحيحي (Log.d) بالوسم (TAG) ونص يذكر فرض إعادة إنشاء كل الاشتراكات النشطة مع عددها المأخوذ من حجم خريطة الاشتراكات النشطة (activeSubscriptions.size). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:448]

```
449:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:449]

```
450:         scope.launch {
```
> يستدعي الدالة إطلاق (launch) على النطاق (scope) لبدء مهمة غير متزامنة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:450]

```
451:             connections.forEach { (relayUrl, webSocket) ->
```
> يستدعي الدالة لكل عنصر (forEach) على خريطة الاتصالات (connections) بمُعامِلَيْن: عنوان المُرحِّل (relayUrl) ومقبس الويب (webSocket). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:451]

```
452:                 restoreSubscriptionsForRelay(relayUrl, webSocket)
```
> يستدعي الدالة استعادة الاشتراكات للمُرحِّل (restoreSubscriptionsForRelay) ممرّراً عنوان المُرحِّل ومقبس الويب. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:452]

```
453:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:453]

```
454:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:454]

```
455:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:455]

```
456:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:456]

```
457:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:457]

```
458:      * Clear all subscription tracking, message handlers, routing caches, and queued messages.
```
> تعليق: مسح كل تتبّع الاشتراكات، ومعالِجات الرسائل، ومخابئ التوجيه، والرسائل المصفوفة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:458]

```
459:      * Intended for panic/reset flows prior to reconnecting and re-subscribing from scratch.
```
> تعليق: مُعَدّ لمسارات الذعر/إعادة التعيين قبل إعادة الاتصال وإعادة الاشتراك من الصفر. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:459]

```
460:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:460]

```
461:     fun clearAllSubscriptions() {
```
> تعريف دالة مسح كل الاشتراكات (clearAllSubscriptions) بلا مُعامِلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:461]

```
462:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:462]

```
463:             // Clear persistent subscription tracking
```
> تعليق: مسح تتبّع الاشتراكات الدائم. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:463]

```
464:             activeSubscriptions.clear()
```
> يستدعي الدالة مسح (clear) على خريطة الاشتراكات النشطة (activeSubscriptions). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:464]

```
465:             messageHandlers.clear()
```
> يستدعي الدالة مسح (clear) على معالِجات الرسائل (messageHandlers). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:465]

```
466:             subscriptions.clear()
```
> يستدعي الدالة مسح (clear) على الاشتراكات (subscriptions). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:466]

```
467: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:467]

```
468:             // Clear routing caches (per-geohash relay selections)
```
> تعليق: مسح مخابئ التوجيه (اختيارات المُرحِّل لكل تجزئة جغرافية geohash). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:468]

```
469:             geohashToRelays.clear()
```
> يستدعي الدالة مسح (clear) على خريطة التجزئة الجغرافية إلى المُرحِّلات (geohashToRelays). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:469]

```
470: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:470]

```
471:             // Clear any queued messages waiting to be sent
```
> تعليق: مسح أي رسائل مصفوفة بانتظار الإرسال. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:471]

```
472:             synchronized(messageQueueLock) {
```
> يبدأ كتلة متزامنة (synchronized) على القفل قفل صف الرسائل (messageQueueLock). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:472]

```
473:                 messageQueue.clear()
```
> يستدعي الدالة مسح (clear) على صف الرسائل (messageQueue). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:473]

```
474:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:474]

```
475: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:475]

```
476:             Log.i(TAG, "🧹 Cleared all Nostr subscriptions and routing caches")
```
> يستدعي دالة السجل المعلوماتي (Log.i) بالوسم (TAG) ونص يذكر أنه مسح كل اشتراكات نوستر (Nostr) ومخابئ التوجيه. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:476]

```
477:         } catch (e: Exception) {
```
> بداية كتلة التقاط (catch) لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:477]

```
478:             Log.e(TAG, "Failed to clear subscriptions: ${e.message}")
```
> يستدعي دالة سجل الخطأ (Log.e) بالوسم (TAG) ونص يذكر فشل مسح الاشتراكات مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:478]

```
479:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:479]

```
480:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:480]

```
481:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:481]

```
482:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:482]

```
483:      * Get detailed status for all relays
```
> تعليق: الحصول على الحالة المفصّلة لكل المُرحِّلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:483]

```
484:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:484]

```
485:     fun getRelayStatuses(): List<Relay> {
```
> تعريف دالة الحصول على حالات المُرحِّلات (getRelayStatuses) التي تُعيد قائمة (List) من المُرحِّل (Relay). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:485]

```
486:         return relaysList.toList()
```
> يُعيد نسخة قائمة (toList) من قائمة المُرحِّلات (relaysList). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:486]

```
487:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:487]

```
488:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:488]

```
489:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:489]

```
490:      * Get event deduplication statistics
```
> تعليق: الحصول على إحصاءات إزالة تكرار الأحداث. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:490]

```
491:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:491]

```
492:     fun getDeduplicationStats(): DeduplicationStats {
```
> تعريف دالة الحصول على إحصاءات إزالة التكرار (getDeduplicationStats) التي تُعيد إحصاءات إزالة التكرار (DeduplicationStats). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:492]

```
493:         return eventDeduplicator.getStats()
```
> يُعيد ناتج استدعاء الدالة الحصول على الإحصاءات (getStats) على مُزيل تكرار الأحداث (eventDeduplicator). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:493]

```
494:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:494]

```
495:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:495]

```
496:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:496]

```
497:      * Clear the event deduplication cache (useful for testing or debugging)
```
> تعليق: مسح مخبأ إزالة تكرار الأحداث (مفيد للاختبار أو التنقيح). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:497]

```
498:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:498]

```
499:     fun clearDeduplicationCache() {
```
> تعريف دالة مسح مخبأ إزالة التكرار (clearDeduplicationCache) بلا مُعامِلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:499]

```
500:         eventDeduplicator.clear()
```
> يستدعي الدالة مسح (clear) على مُزيل تكرار الأحداث (eventDeduplicator). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:500]

```
501:         Log.i(TAG, "🧹 Cleared event deduplication cache")
```
> يستدعي دالة السجل المعلوماتي (Log.i) بالوسم (TAG) ونص يذكر مسح مخبأ إزالة تكرار الأحداث. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:501]

```
502:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:502]

```
503:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:503]

```
504:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:504]

```
505:      * Get the count of active subscriptions
```
> تعليق: الحصول على عدد الاشتراكات النشطة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:505]

```
506:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:506]

```
507:     fun getActiveSubscriptionCount(): Int {
```
> تعريف دالة الحصول على عدد الاشتراكات النشطة (getActiveSubscriptionCount) التي تُعيد عدداً صحيحاً (Int). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:507]

```
508:         return activeSubscriptions.size
```
> يُعيد حجم (size) خريطة الاشتراكات النشطة (activeSubscriptions). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:508]

```
509:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:509]

```
510:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:510]

```
511:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:511]

```
512:      * Get information about all active subscriptions (for debugging)
```
> تعليق: الحصول على معلومات عن كل الاشتراكات النشطة (للتنقيح). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:512]

```
513:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:513]

```
514:     fun getActiveSubscriptions(): Map<String, SubscriptionInfo> {
```
> تعريف دالة الحصول على الاشتراكات النشطة (getActiveSubscriptions) التي تُعيد خريطة (Map) مفتاحها نص (String) وقيمتها معلومات الاشتراك (SubscriptionInfo). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:514]

```
515:         return activeSubscriptions.toMap()
```
> يُعيد نسخة خريطة (toMap) من خريطة الاشتراكات النشطة (activeSubscriptions). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:515]

```
516:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:516]

```
517:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:517]

```
518:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:518]

```
519:      * Validate subscription consistency across all relays
```
> تعليق: التحقق من اتساق الاشتراكات عبر كل المُرحِّلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:519]

```
520:      * Returns a report of any inconsistencies found
```
> تعليق: يُعيد تقريراً بأي حالات عدم اتساق يُعثَر عليها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:520]

```
521:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:521]

```
522:     fun validateSubscriptionConsistency(): SubscriptionConsistencyReport {
```
> تعريف دالة التحقق من اتساق الاشتراكات (validateSubscriptionConsistency) التي تُعيد تقرير اتساق الاشتراكات (SubscriptionConsistencyReport). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:522]

```
523:         val expectedSubs = activeSubscriptions.keys
```
> تعريف متغير ثابت اسمه الاشتراكات المتوقعة (expectedSubs) يساوي مفاتيح (keys) خريطة الاشتراكات النشطة (activeSubscriptions). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:523]

```
524:         val actualSubsByRelay = subscriptions.toMap()
```
> تعريف متغير ثابت اسمه الاشتراكات الفعلية حسب المُرحِّل (actualSubsByRelay) يساوي نسخة خريطة (toMap) من الاشتراكات (subscriptions). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:524]

```
525:         val inconsistencies = mutableListOf<String>()
```
> تعريف متغير ثابت اسمه حالات عدم الاتساق (inconsistencies) يساوي قائمة قابلة للتغيير (mutableListOf) من نوع نص (String) فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:525]

```
526:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:526]

```
527:         connections.keys.forEach { relayUrl ->
```
> يستدعي الدالة لكل عنصر (forEach) على مفاتيح (keys) خريطة الاتصالات (connections) بمُعامِل اسمه عنوان المُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:527]

```
528:             val actualSubs = actualSubsByRelay[relayUrl] ?: emptySet()
```
> تعريف متغير ثابت اسمه الاشتراكات الفعلية (actualSubs) يساوي قيمة actualSubsByRelay عند عنوان المُرحِّل، وإن كانت null فمجموعة فارغة (emptySet). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:528]

```
529:             val expectedForRelay = expectedSubs.filter { subId ->
```
> تعريف متغير ثابت اسمه المتوقَّع للمُرحِّل (expectedForRelay) يساوي ناتج ترشيح (filter) على الاشتراكات المتوقعة بمُعامِل اسمه معرّف الاشتراك (subId). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:529]

```
530:                 val subInfo = activeSubscriptions[subId]
```
> تعريف متغير ثابت اسمه معلومات الاشتراك (subInfo) يساوي قيمة خريطة الاشتراكات النشطة (activeSubscriptions) عند معرّف الاشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:530]

```
531:                 subInfo?.targetRelayUrls == null || subInfo.targetRelayUrls.contains(relayUrl)
```
> يُعيد قيمة منطقية صحيحة إذا كان حقل عناوين المُرحِّلات المستهدفة (targetRelayUrls) في معلومات الاشتراك يساوي null، أو إذا كان يحتوي (contains) على عنوان المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:531]

```
532:             }.toSet()
```
> يحوّل ناتج الترشيح إلى مجموعة (toSet)، وإغلاق نطاق دالة الترشيح. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:532]

```
533:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:533]

```
534:             val missing = expectedForRelay - actualSubs
```
> تعريف متغير ثابت اسمه المفقود (missing) يساوي فرق المجموعتين: المتوقَّع للمُرحِّل ناقص الاشتراكات الفعلية. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:534]

```
535:             val extra = actualSubs - expectedForRelay
```
> تعريف متغير ثابت اسمه الزائد (extra) يساوي فرق المجموعتين: الاشتراكات الفعلية ناقص المتوقَّع للمُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:535]

```
536:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:536]

```
537:             if (missing.isNotEmpty()) {
```
> شرط: إذا كانت مجموعة المفقود ليست فارغة (isNotEmpty). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:537]

```
538:                 inconsistencies.add("Relay $relayUrl missing subscriptions: $missing")
```
> يستدعي الدالة إضافة (add) على قائمة حالات عدم الاتساق بنص يذكر أن المُرحِّل (relayUrl) تنقصه اشتراكات (missing). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:538]

```
539:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:539]

```
540:             if (extra.isNotEmpty()) {
```
> شرط: إذا كانت مجموعة الزائد ليست فارغة (isNotEmpty). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:540]

```
541:                 inconsistencies.add("Relay $relayUrl has extra subscriptions: $extra")
```
> يستدعي الدالة إضافة (add) على قائمة حالات عدم الاتساق بنص يذكر أن المُرحِّل (relayUrl) لديه اشتراكات زائدة (extra). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:541]

```
542:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:542]

```
543:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:543]

```
544:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:544]

```
545:         return SubscriptionConsistencyReport(
```
> يُعيد كائن تقرير اتساق الاشتراكات (SubscriptionConsistencyReport) ببدء تمرير الوسائط. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:545]

```
546:             isConsistent = inconsistencies.isEmpty(),
```
> يُسنِد إلى الوسيط مُتّسق (isConsistent) قيمة ما إذا كانت قائمة حالات عدم الاتساق فارغة (isEmpty). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:546]

```
547:             inconsistencies = inconsistencies,
```
> يُسنِد إلى الوسيط حالات عدم الاتساق (inconsistencies) قيمة المتغير حالات عدم الاتساق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:547]

```
548:             totalActiveSubscriptions = activeSubscriptions.size,
```
> يُسنِد إلى الوسيط إجمالي الاشتراكات النشطة (totalActiveSubscriptions) قيمة حجم خريطة الاشتراكات النشطة (activeSubscriptions.size). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:548]

```
549:             connectedRelayCount = connections.size
```
> يُسنِد إلى الوسيط عدد المُرحِّلات المتصلة (connectedRelayCount) قيمة حجم خريطة الاتصالات (connections.size). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:549]

```
550:         )
```
> إغلاق قائمة وسائط الكائن المُعاد. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:550]

```
551:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:551]

```
552:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:552]

```
553:     data class SubscriptionConsistencyReport(
```
> تعريف صنف بيانات (data class) اسمه تقرير اتساق الاشتراكات (SubscriptionConsistencyReport) ببدء قائمة خصائصه. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:553]

```
554:         val isConsistent: Boolean,
```
> تعريف خاصية ثابتة اسمها مُتّسق (isConsistent) من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:554]

```
555:         val inconsistencies: List<String>,
```
> تعريف خاصية ثابتة اسمها حالات عدم الاتساق (inconsistencies) من نوع قائمة (List) من نص (String). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:555]

```
556:         val totalActiveSubscriptions: Int,
```
> تعريف خاصية ثابتة اسمها إجمالي الاشتراكات النشطة (totalActiveSubscriptions) من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:556]

```
557:         val connectedRelayCount: Int
```
> تعريف خاصية ثابتة اسمها عدد المُرحِّلات المتصلة (connectedRelayCount) من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:557]

```
558:     )
```
> إغلاق قائمة خصائص صنف البيانات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:558]

```
559:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:559]

```
560:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:560]

```
561:      * Start periodic subscription validation to ensure robustness
```
> تعليق: بدء التحقق الدوري من الاشتراكات لضمان المتانة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:561]

```
562:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:562]

```
563:     private fun startSubscriptionValidation() {
```
> تعريف دالة خاصة (private) اسمها بدء التحقق من الاشتراكات (startSubscriptionValidation) بلا مُعامِلات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:563]

```
564:         stopSubscriptionValidation() // Stop any existing validation
```
> يستدعي الدالة إيقاف التحقق من الاشتراكات (stopSubscriptionValidation)، وتعليق: إيقاف أي تحقق قائم. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:564]

```
565:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:565]

```
566:         subscriptionValidationJob = scope.launch {
```
> يُسنِد إلى مهمة التحقق من الاشتراكات (subscriptionValidationJob) ناتج استدعاء الدالة إطلاق (launch) على النطاق (scope). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:566]

```
567:             while (isActive) {
```
> حلقة طالما (while) ما دامت الكوروتين نشطة (isActive). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:567]

```
568:                 delay(SUBSCRIPTION_VALIDATION_INTERVAL)
```
> يستدعي الدالة تأخير (delay) بمقدار فترة التحقق من الاشتراكات (SUBSCRIPTION_VALIDATION_INTERVAL). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:568]

```
569:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:569]

```
570:                 try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:570]

```
571:                     val report = validateSubscriptionConsistency()
```
> تعريف متغير ثابت اسمه تقرير (report) يساوي ناتج استدعاء الدالة التحقق من اتساق الاشتراكات (validateSubscriptionConsistency). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:571]

```
572:                     if (!report.isConsistent && report.connectedRelayCount > 0) {
```
> شرط: إذا كان التقرير غير مُتّسق (isConsistent منفية) وعدد المُرحِّلات المتصلة (connectedRelayCount) أكبر من صفر. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:572]

```
573:                         Log.w(TAG, "⚠️ Subscription inconsistencies detected: ${report.inconsistencies}")
```
> يستدعي دالة سجل التحذير (Log.w) بالوسم (TAG) ونص يذكر اكتشاف حالات عدم اتساق في الاشتراكات مع قائمة حالات عدم الاتساق من التقرير (report.inconsistencies). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:573]

```
574:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:574]

```
575:                         // Auto-repair: re-establish subscriptions for relays with missing ones
```
> تعليق: إصلاح تلقائي: إعادة إنشاء الاشتراكات للمُرحِّلات التي تنقصها اشتراكات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:575]

```
576:                         connections.forEach { (relayUrl, webSocket) ->
```
> يستدعي الدالة لكل عنصر (forEach) على خريطة الاتصالات (connections) بمُعامِلَيْن: عنوان المُرحِّل (relayUrl) ومقبس الويب (webSocket). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:576]

```
577:                             val currentSubs = subscriptions[relayUrl] ?: emptySet()
```
> تعريف متغير ثابت اسمه الاشتراكات الحالية (currentSubs) يساوي قيمة الاشتراكات (subscriptions) عند عنوان المُرحِّل، وإن كانت null فمجموعة فارغة (emptySet). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:577]

```
578:                             val expectedSubs = activeSubscriptions.keys.filter { subId ->
```
> تعريف متغير ثابت اسمه الاشتراكات المتوقعة (expectedSubs) يساوي ناتج ترشيح (filter) على مفاتيح خريطة الاشتراكات النشطة (activeSubscriptions.keys) بمُعامِل اسمه معرّف الاشتراك (subId). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:578]

```
579:                                 val subInfo = activeSubscriptions[subId]
```
> تعريف متغير ثابت اسمه معلومات الاشتراك (subInfo) يساوي قيمة خريطة الاشتراكات النشطة (activeSubscriptions) عند معرّف الاشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:579]

```
580:                                 subInfo?.targetRelayUrls == null || subInfo.targetRelayUrls.contains(relayUrl)
```
> يُعيد قيمة منطقية صحيحة إذا كان حقل عناوين المُرحِّلات المستهدفة (targetRelayUrls) في معلومات الاشتراك يساوي null، أو إذا كان يحتوي (contains) على عنوان المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:580]

```
581:                             }.toSet()
```
> يحوّل ناتج الترشيح إلى مجموعة (toSet)، وإغلاق نطاق دالة الترشيح. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:581]

```
582:                             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:582]

```
583:                             val missingSubs = expectedSubs - currentSubs
```
> تعريف متغير ثابت اسمه الاشتراكات المفقودة (missingSubs) يساوي فرق المجموعتين: الاشتراكات المتوقعة ناقص الاشتراكات الحالية. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:583]

```
584:                             if (missingSubs.isNotEmpty()) {
```
> شرط: إذا كانت مجموعة الاشتراكات المفقودة ليست فارغة (isNotEmpty). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:584]

```
585:                                 Log.i(TAG, "🔧 Auto-repairing ${missingSubs.size} missing subscriptions for $relayUrl")
```
> يستدعي دالة السجل المعلوماتي (Log.i) بالوسم (TAG) ونص يذكر الإصلاح التلقائي لعدد الاشتراكات المفقودة (missingSubs.size) للمُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:585]

```
586:                                 restoreSubscriptionsForRelay(relayUrl, webSocket)
```
> يستدعي الدالة استعادة الاشتراكات للمُرحِّل (restoreSubscriptionsForRelay) ممرّراً عنوان المُرحِّل ومقبس الويب. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:586]

```
587:                             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:587]

```
588:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:588]

```
589:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:589]

```
590:                 } catch (e: Exception) {
```
> بداية كتلة التقاط (catch) لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:590]

```
591:                     Log.e(TAG, "Error during subscription validation: ${e.message}")
```
> يستدعي دالة سجل الخطأ (Log.e) بالوسم (TAG) ونص يذكر خطأ أثناء التحقق من الاشتراكات مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:591]

```
592:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:592]

```
593:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:593]

```
594:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:594]

```
595:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:595]

```
596:         Log.d(TAG, "🔄 Started periodic subscription validation (${SUBSCRIPTION_VALIDATION_INTERVAL / 1000}s interval)")
```
> يستدعي دالة السجل التصحيحي (Log.d) بالوسم (TAG) ونص يذكر بدء التحقق الدوري من الاشتراكات مع الفترة محسوبة بقسمة فترة التحقق على 1000 (SUBSCRIPTION_VALIDATION_INTERVAL / 1000) بالثواني. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:596]

```
597:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:597]

```
598:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:598]

```
599:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:599]

```
600:      * Stop periodic subscription validation
```
> تعليق: إيقاف التحقق الدوري من الاشتراكات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:600]
