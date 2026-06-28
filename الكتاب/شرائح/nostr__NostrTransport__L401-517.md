# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt (الأسطر 401–517)

```
401:                )
```
> قوس إغلاق لقائمة وسائط استدعاء سابق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:401]

```
402:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:402]

```
403:                // Register pending gift wrap for deduplication and send all
```
> تعليق: سجّل الغلاف الهديّة المعلّق لمنع التكرار وأرسل الكل. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:403]

```
404:                giftWraps.forEach { event ->
```
> يكرّر (forEach) على مجموعة الأغلفة الهديّة (giftWraps) مع متغيّر كل عنصر باسم event. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:404]

```
405:                    NostrRelayManager.registerPendingGiftWrap(event.id)
```
> يستدعي على مدير مُرحّل نوستر (NostrRelayManager) الدالة registerPendingGiftWrap ويمرّر لها معرّف الحدث event.id. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:405]

```
406:                    NostrRelayManager.getInstance(context).sendEvent(event)
```
> يحصل على نسخة مدير المُرحّل عبر getInstance بتمرير context ثم يستدعي sendEvent ويمرّر event. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:406]

```
407:                }
```
> إغلاق نطاق كتلة التكرار. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:407]

```
408:                
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:408]

```
409:            } catch (e: Exception) {
```
> يلتقط (catch) استثناءً (Exception) باسم e ويفتح كتلة معالجته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:409]

```
410:                Log.e(TAG, "Failed to send geohash read receipt: ${e.message}")
```
> يسجّل خطأً عبر Log.e بالوسم TAG ونص "Failed to send geohash read receipt:" متبوعاً برسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:410]

```
411:            }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:411]

```
412:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:412]

```
413:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:413]

```
414:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:414]

```
415:    // MARK: - Geohash DMs (per-geohash identity)
```
> تعليق: علامة قسم — رسائل مباشرة بترميز الموقع (Geohash DMs) بهويّة لكل ترميز موقع. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:415]

```
416:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:416]

```
417:    fun sendPrivateMessageGeohash(
```
> يعرّف دالة عامة باسم sendPrivateMessageGeohash (إرسال رسالة خاصة بترميز الموقع) وتفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:417]

```
418:        content: String,
```
> معامل باسم content من نوع نصّ (String). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:418]

```
419:        toRecipientHex: String,
```
> معامل باسم toRecipientHex (إلى المستلِم بالنظام الستّ عشري) من نوع نصّ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:419]

```
420:        messageID: String,
```
> معامل باسم messageID (معرّف الرسالة) من نوع نصّ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:420]

```
421:        sourceGeohash: String? = null
```
> معامل باسم sourceGeohash (ترميز الموقع المصدر) من نوع نصّ قابل للإفراغ، قيمته الافتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:421]

```
422:    ) {
```
> إغلاق قائمة المعاملات وفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:422]

```
423:        // Use provided geohash or derive from current location
```
> تعليق: استعمل ترميز الموقع المعطى أو اشتقّه من الموقع الحالي. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:423]

```
424:        val geohash = sourceGeohash ?: run {
```
> يعرّف ثابتاً باسم geohash يساوي sourceGeohash، وإن كان null يُنفّذ كتلة run. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:424]

```
425:            val selected = try {
```
> يعرّف ثابتاً باسم selected قيمته نتيجة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:425]

```
426:                com.bitchat.android.geohash.LocationChannelManager.getInstance(context).selectedChannel.value
```
> يحصل على نسخة مدير قناة الموقع (LocationChannelManager) عبر getInstance بتمرير context ثم يقرأ قيمة selectedChannel.value (القناة المختارة). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:426]

```
427:            } catch (_: Exception) { null }
```
> يلتقط استثناءً دون تسميته ويُعيد null كقيمة لكتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:427]

```
428:            if (selected !is com.bitchat.android.geohash.ChannelID.Location) {
```
> شرط: إذا لم يكن selected من نوع ChannelID.Location (قناة موقع). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:428]

```
429:                Log.w(TAG, "NostrTransport: cannot send geohash PM - not in a location channel and no geohash provided")
```
> يسجّل تحذيراً عبر Log.w بالوسم TAG ونص "NostrTransport: cannot send geohash PM - not in a location channel and no geohash provided". [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:429]

```
430:                return
```
> يُعيد (return) من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:430]

```
431:            }
```
> إغلاق نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:431]

```
432:            selected.channel.geohash
```
> يُعيد قيمة selected.channel.geohash (ترميز موقع القناة المختارة) كنتيجة كتلة run. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:432]

```
433:        }
```
> إغلاق نطاق كتلة run. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:433]

```
434:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:434]

```
435:        val fromIdentity = try {
```
> يعرّف ثابتاً باسم fromIdentity (الهويّة المرسِلة) قيمته نتيجة كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:435]

```
436:            NostrIdentityBridge.deriveIdentity(geohash, context)
```
> يستدعي على جسر هويّة نوستر (NostrIdentityBridge) الدالة deriveIdentity ويمرّر geohash و context. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:436]

```
437:        } catch (e: Exception) {
```
> يلتقط استثناءً باسم e ويفتح كتلة معالجته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:437]

```
438:            Log.e(TAG, "NostrTransport: cannot derive geohash identity for $geohash: ${e.message}")
```
> يسجّل خطأً عبر Log.e بالوسم TAG ونص "NostrTransport: cannot derive geohash identity for" متبوعاً بقيمة geohash ثم رسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:438]

```
439:            return
```
> يُعيد من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:439]

```
440:        }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:440]

```
441:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:441]

```
442:        transportScope.launch {
```
> يستدعي على نطاق النقل (transportScope) الدالة launch ويفتح كتلة المتعاوِنة (coroutine). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:442]

```
443:            try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:443]

```
444:                if (toRecipientHex.isEmpty()) return@launch
```
> شرط: إذا كان toRecipientHex فارغاً (isEmpty) يُعيد من كتلة launch. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:444]

```
445:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:445]

```
446:                Log.d(
```
> يستدعي Log.d ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:446]

```
447:                    TAG,
```
> وسيط أول هو الوسم TAG. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:447]

```
448:                    "GeoDM: send PM -> recip=${toRecipientHex.take(8)}... mid=${messageID.take(8)}... from=${fromIdentity.publicKeyHex.take(8)}... geohash=$geohash"
```
> وسيط نصّي يحوي "GeoDM: send PM -> recip=" مع أول ٨ محارف من toRecipientHex، و"mid=" مع أول ٨ محارف من messageID، و"from=" مع أول ٨ محارف من fromIdentity.publicKeyHex، و"geohash=" مع قيمة geohash. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:448]

```
449:                )
```
> إغلاق قائمة وسائط Log.d. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:449]

```
450:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:450]

```
451:                // Build embedded BitChat packet without recipient peer ID
```
> تعليق: ابنِ حزمة بِت‑تشات مضمّنة دون معرّف نظير المستلِم. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:451]

```
452:                val embedded = NostrEmbeddedBitChat.encodePMForNostrNoRecipient(
```
> يعرّف ثابتاً باسم embedded قيمته نتيجة استدعاء encodePMForNostrNoRecipient على NostrEmbeddedBitChat، ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:452]

```
453:                    content = content,
```
> وسيط مسمّى content يساوي معامل content. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:453]

```
454:                    messageID = messageID,
```
> وسيط مسمّى messageID يساوي معامل messageID. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:454]

```
455:                    senderPeerID = senderPeerID
```
> وسيط مسمّى senderPeerID يساوي الخاصيّة senderPeerID. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:455]

```
456:                ) ?: run {
```
> إغلاق قائمة الوسائط، وإن كانت النتيجة null يُنفّذ كتلة run. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:456]

```
457:                    Log.e(TAG, "NostrTransport: failed to embed geohash PM packet")
```
> يسجّل خطأً عبر Log.e بالوسم TAG ونص "NostrTransport: failed to embed geohash PM packet". [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:457]

```
458:                    return@launch
```
> يُعيد من كتلة launch. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:458]

```
459:                }
```
> إغلاق نطاق كتلة run. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:459]

```
460:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:460]

```
461:                val giftWraps = NostrProtocol.createPrivateMessage(
```
> يعرّف ثابتاً باسم giftWraps قيمته نتيجة استدعاء createPrivateMessage على بروتوكول نوستر (NostrProtocol)، ويفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:461]

```
462:                    content = embedded,
```
> وسيط مسمّى content يساوي embedded. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:462]

```
463:                    recipientPubkey = toRecipientHex,
```
> وسيط مسمّى recipientPubkey (مفتاح المستلِم العام) يساوي toRecipientHex. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:463]

```
464:                    senderIdentity = fromIdentity
```
> وسيط مسمّى senderIdentity (هويّة المرسِل) يساوي fromIdentity. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:464]

```
465:                )
```
> إغلاق قائمة وسائط createPrivateMessage. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:465]

```
466:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:466]

```
467:                giftWraps.forEach { event ->
```
> يكرّر على giftWraps مع متغيّر كل عنصر باسم event. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:467]

```
468:                    Log.d(TAG, "NostrTransport: sending geohash PM giftWrap id=${event.id.take(16)}...")
```
> يسجّل تصحيحاً عبر Log.d بالوسم TAG ونص "NostrTransport: sending geohash PM giftWrap id=" مع أول ١٦ محرفاً من event.id. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:468]

```
469:                    NostrRelayManager.registerPendingGiftWrap(event.id)
```
> يستدعي على NostrRelayManager الدالة registerPendingGiftWrap ويمرّر event.id. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:469]

```
470:                    NostrRelayManager.getInstance(context).sendEvent(event)
```
> يحصل على نسخة المدير عبر getInstance بتمرير context ثم يستدعي sendEvent ويمرّر event. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:470]

```
471:                }
```
> إغلاق نطاق كتلة التكرار. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:471]

```
472:            } catch (e: Exception) {
```
> يلتقط استثناءً باسم e ويفتح كتلة معالجته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:472]

```
473:                Log.e(TAG, "Failed to send geohash private message: ${e.message}")
```
> يسجّل خطأً عبر Log.e بالوسم TAG ونص "Failed to send geohash private message:" متبوعاً برسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:473]

```
474:            }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:474]

```
475:        }
```
> إغلاق نطاق كتلة launch. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:475]

```
476:    }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:476]

```
477:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:477]

```
478:    // MARK: - Helper Methods
```
> تعليق: علامة قسم — دوال مساعدة (Helper Methods). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:478]

```
479:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:479]

```
480:    /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:480]

```
481:     * Resolve Nostr public key for a peer ID
```
> تعليق: حُلّ المفتاح العام لنوستر مقابل معرّف نظير. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:481]

```
482:     */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:482]

```
483:    private fun resolveNostrPublicKey(peerID: String): String? {
```
> يعرّف دالة خاصّة (private) باسم resolveNostrPublicKey تأخذ معاملاً peerID نصّاً وتُعيد نصّاً قابلاً للإفراغ، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:483]

```
484:        try {
```
> يفتح كتلة try. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:484]

```
485:            // 1) Fast path: direct peerID→npub mapping (mutual favorites after mesh mapping)
```
> تعليق: ١) مسار سريع: ربط مباشر من معرّف النظير إلى npub (مفضّلون متبادلون بعد ربط الشبكة المتداخلة). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:485]

```
486:            com.bitchat.android.favorites.FavoritesPersistenceService.shared.findNostrPubkeyForPeerID(peerID)?.let { return it }
```
> يستدعي findNostrPubkeyForPeerID على النسخة المشتركة shared من خدمة حفظ المفضّلين (FavoritesPersistenceService) ممرّراً peerID، وإن لم تكن النتيجة null يُعيدها عبر let. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:486]

```
487:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:487]

```
488:            // 2) Legacy path: resolve by noise public key association
```
> تعليق: ٢) مسار قديم: حُلّ بالاقتران بمفتاح Noise العام. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:488]

```
489:            val noiseKey = hexStringToByteArray(peerID)
```
> يعرّف ثابتاً باسم noiseKey قيمته نتيجة استدعاء hexStringToByteArray ممرّراً peerID. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:489]

```
490:            val favoriteStatus = com.bitchat.android.favorites.FavoritesPersistenceService.shared.getFavoriteStatus(noiseKey)
```
> يعرّف ثابتاً باسم favoriteStatus قيمته نتيجة استدعاء getFavoriteStatus على shared من FavoritesPersistenceService ممرّراً noiseKey. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:490]

```
491:            if (favoriteStatus?.peerNostrPublicKey != null) return favoriteStatus.peerNostrPublicKey
```
> شرط: إذا كان favoriteStatus?.peerNostrPublicKey ليس null يُعيد favoriteStatus.peerNostrPublicKey. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:491]

```
492:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:492]

```
493:            // 3) Prefix match on noiseHex from 16-hex peerID
```
> تعليق: ٣) مطابقة بادئة على noiseHex من معرّف نظير بطول ١٦ ستّ عشري. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:493]

```
494:            if (peerID.length == 16) {
```
> شرط: إذا كان طول peerID يساوي ١٦. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:494]

```
495:                val fallbackStatus = com.bitchat.android.favorites.FavoritesPersistenceService.shared.getFavoriteStatus(peerID)
```
> يعرّف ثابتاً باسم fallbackStatus (الحالة الاحتياطيّة) قيمته نتيجة getFavoriteStatus على shared من FavoritesPersistenceService ممرّراً peerID. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:495]

```
496:                return fallbackStatus?.peerNostrPublicKey
```
> يُعيد fallbackStatus?.peerNostrPublicKey. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:496]

```
497:            }
```
> إغلاق نطاق كتلة الشرط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:497]

```
498:            
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:498]

```
499:            return null
```
> يُعيد null. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:499]

```
500:        } catch (e: Exception) {
```
> يلتقط استثناءً باسم e ويفتح كتلة معالجته. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:500]

```
501:            Log.e(TAG, "Failed to resolve Nostr public key for $peerID: ${e.message}")
```
> يسجّل خطأً عبر Log.e بالوسم TAG ونص "Failed to resolve Nostr public key for" متبوعاً بقيمة peerID ثم رسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:501]

```
502:            return null
```
> يُعيد null. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:502]

```
503:        }
```
> إغلاق نطاق كتلة الالتقاط. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:503]

```
504:    }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:504]

```
505:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:505]

```
506:    /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:506]

```
507:     * Convert full hex string to byte array
```
> تعليق: حوّل نصّاً ستّ عشرياً كاملاً إلى مصفوفة بايتات. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:507]

```
508:     */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:508]

```
509:    private fun hexStringToByteArray(hexString: String): ByteArray {
```
> يعرّف دالة خاصّة باسم hexStringToByteArray تأخذ معاملاً hexString نصّاً وتُعيد مصفوفة بايتات (ByteArray)، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:509]

```
510:        val clean = if (hexString.length % 2 == 0) hexString else "0$hexString"
```
> يعرّف ثابتاً باسم clean يساوي hexString إن كان طوله زوجياً (باقي القسمة على ٢ يساوي صفراً)، وإلا يساوي "0" مسبوقاً به متبوعاً بـ hexString. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:510]

```
511:        return clean.chunked(2).map { it.toInt(16).toByte() }.toByteArray()
```
> يُعيد نتيجة تقطيع clean إلى أزواج عبر chunked(2) ثم تحويل كل زوج إلى عدد صحيح بالأساس ١٦ ثم إلى بايت عبر map، ثم تجميعها بمصفوفة بايتات عبر toByteArray. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:511]

```
512:    }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:512]

```
513:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:513]

```
514:    fun cleanup() {
```
> يعرّف دالة عامة باسم cleanup (تنظيف) بلا معاملات، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:514]

```
515:        transportScope.cancel()
```
> يستدعي على transportScope الدالة cancel (إلغاء). [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:515]

```
516:    }
```
> إغلاق نطاق الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:516]

```
517:}
```
> إغلاق نطاق الصنف. [app/src/main/java/com/bitchat/android/nostr/NostrTransport.kt:517]
