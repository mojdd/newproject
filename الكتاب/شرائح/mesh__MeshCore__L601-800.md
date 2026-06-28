# شريحة — app/src/main/java/com/bitchat/android/mesh/MeshCore.kt (الأسطر 601–800)

```
601:                return@launch
```
> يُعيد الخروج من كتلة الإطلاق (launch) الحالية عبر `return@launch`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:601]

```
602:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:602]

```
603:            val announcement = IdentityAnnouncement(nickname, staticKey, signingKey)
```
> يُعرّف متغيراً ثابتاً اسمه `announcement` (إعلان الهوية) ويُسنِد إليه كائن `IdentityAnnouncement` مُنشأً بالوسائط `nickname` (الاسم المستعار) و`staticKey` (المفتاح الثابت) و`signingKey` (مفتاح التوقيع). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:603]

```
604:            val tlvPayload = buildAnnouncementPayload(announcement, nickname) ?: return@launch
```
> يُعرّف متغيراً ثابتاً اسمه `tlvPayload` (حمولة TLV) ويُسنِد إليه ناتج استدعاء الدالة `buildAnnouncementPayload` بالوسيطين `announcement` و`nickname`، وإذا كان الناتج فارغاً (null) يخرج من كتلة الإطلاق عبر `return@launch`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:604]

```
605:            val announcePacket = BitchatPacket(
```
> يُعرّف متغيراً ثابتاً اسمه `announcePacket` (حزمة الإعلان) ويبدأ إسناد كائن `BitchatPacket` مُنشأ إليه. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:605]

```
606:                type = MessageType.ANNOUNCE.value,
```
> يضبط الوسيط المسمّى `type` (النوع) على قيمة `MessageType.ANNOUNCE.value` (قيمة نوع الرسالة «إعلان»). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:606]

```
607:                ttl = maxTtl,
```
> يضبط الوسيط المسمّى `ttl` (مدة البقاء) على قيمة المتغير `maxTtl` (أقصى مدة بقاء). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:607]

```
608:                senderID = myPeerID,
```
> يضبط الوسيط المسمّى `senderID` (معرّف المُرسِل) على قيمة المتغير `myPeerID` (معرّف نظيري). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:608]

```
609:                payload = tlvPayload
```
> يضبط الوسيط المسمّى `payload` (الحمولة) على قيمة المتغير `tlvPayload`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:609]

```
610:            )
```
> إغلاق قائمة وسائط منشئ `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:610]

```
611:            val signedPacket = signPacketBeforeBroadcast(announcePacket)
```
> يُعرّف متغيراً ثابتاً اسمه `signedPacket` (الحزمة الموقَّعة) ويُسنِد إليه ناتج استدعاء الدالة `signPacketBeforeBroadcast` (توقيع الحزمة قبل البث) بالوسيط `announcePacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:611]

```
612:            dispatchGlobal(RoutedPacket(signedPacket))
```
> يستدعي الدالة `dispatchGlobal` (الإرسال العام) بوسيط هو كائن `RoutedPacket` (حزمة موجَّهة) مُنشأ من `signedPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:612]

```
613:            try { gossipSyncManager.onPublicPacketSeen(signedPacket) } catch (_: Exception) { }
```
> يستدعي ضمن كتلة `try` الدالة `gossipSyncManager.onPublicPacketSeen` (عند رؤية حزمة عامة لمدير مزامنة النميمة) بالوسيط `signedPacket`، ويتجاهل أي استثناء (Exception) في كتلة `catch` فارغة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:613]

```
614:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:614]

```
615:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:615]

```
616:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:616]

```
617:    fun sendAnnouncementToPeer(peerID: String) {
```
> يُعرّف دالة عامة اسمها `sendAnnouncementToPeer` (إرسال الإعلان إلى نظير) تأخذ وسيطاً اسمه `peerID` من نوع `String` ولا تُرجع قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:617]

```
618:        if (peerManager.hasAnnouncedToPeer(peerID)) return
```
> إذا كانت الدالة `peerManager.hasAnnouncedToPeer` (هل أُعلِن لهذا النظير في مدير النظراء) تُعيد صحيحاً للوسيط `peerID` فإنه يُنهي الدالة عبر `return`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:618]

```
619:        val nickname = hooks.announcementNicknameProvider?.invoke()
```
> يُعرّف متغيراً ثابتاً اسمه `nickname` ويبدأ إسناده بناتج استدعاء `hooks.announcementNicknameProvider?.invoke()` (مزوّد اسم الإعلان المستعار في الخطّافات إن لم يكن فارغاً). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:619]

```
620:            ?: delegate?.getNickname()
```
> إذا كانت القيمة السابقة فارغة فيُسنِد ناتج `delegate?.getNickname()` (الحصول على الاسم المستعار من المفوَّض إن لم يكن فارغاً). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:620]

```
621:            ?: myPeerID
```
> إذا كانت القيمة السابقة فارغة فيُسنِد قيمة المتغير `myPeerID`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:621]

```
622:        val staticKey = encryptionService.getStaticPublicKey() ?: return
```
> يُعرّف متغيراً ثابتاً اسمه `staticKey` ويُسنِد إليه ناتج `encryptionService.getStaticPublicKey()` (المفتاح العام الثابت من خدمة التشفير)، وإذا كان فارغاً يُنهي الدالة عبر `return`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:622]

```
623:        val signingKey = encryptionService.getSigningPublicKey() ?: return
```
> يُعرّف متغيراً ثابتاً اسمه `signingKey` ويُسنِد إليه ناتج `encryptionService.getSigningPublicKey()` (المفتاح العام للتوقيع من خدمة التشفير)، وإذا كان فارغاً يُنهي الدالة عبر `return`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:623]

```
624:        val announcement = IdentityAnnouncement(nickname, staticKey, signingKey)
```
> يُعرّف متغيراً ثابتاً اسمه `announcement` ويُسنِد إليه كائن `IdentityAnnouncement` مُنشأً بالوسائط `nickname` و`staticKey` و`signingKey`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:624]

```
625:        val tlvPayload = buildAnnouncementPayload(announcement, nickname) ?: return
```
> يُعرّف متغيراً ثابتاً اسمه `tlvPayload` ويُسنِد إليه ناتج `buildAnnouncementPayload(announcement, nickname)`، وإذا كان فارغاً يُنهي الدالة عبر `return`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:625]

```
626:        val packet = BitchatPacket(
```
> يُعرّف متغيراً ثابتاً اسمه `packet` (الحزمة) ويبدأ إسناد كائن `BitchatPacket` مُنشأ إليه. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:626]

```
627:            type = MessageType.ANNOUNCE.value,
```
> يضبط الوسيط المسمّى `type` على قيمة `MessageType.ANNOUNCE.value`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:627]

```
628:            ttl = maxTtl,
```
> يضبط الوسيط المسمّى `ttl` على قيمة المتغير `maxTtl`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:628]

```
629:            senderID = myPeerID,
```
> يضبط الوسيط المسمّى `senderID` على قيمة المتغير `myPeerID`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:629]

```
630:            payload = tlvPayload
```
> يضبط الوسيط المسمّى `payload` على قيمة المتغير `tlvPayload`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:630]

```
631:        )
```
> إغلاق قائمة وسائط منشئ `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:631]

```
632:        val signedPacket = signPacketBeforeBroadcast(packet)
```
> يُعرّف متغيراً ثابتاً اسمه `signedPacket` ويُسنِد إليه ناتج `signPacketBeforeBroadcast(packet)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:632]

```
633:        dispatchGlobal(RoutedPacket(signedPacket))
```
> يستدعي الدالة `dispatchGlobal` بوسيط هو كائن `RoutedPacket` مُنشأ من `signedPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:633]

```
634:        peerManager.markPeerAsAnnouncedTo(peerID)
```
> يستدعي الدالة `peerManager.markPeerAsAnnouncedTo` (وسم النظير بأنه أُعلِن له في مدير النظراء) بالوسيط `peerID`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:634]

```
635:        try { gossipSyncManager.onPublicPacketSeen(signedPacket) } catch (_: Exception) { }
```
> يستدعي ضمن كتلة `try` الدالة `gossipSyncManager.onPublicPacketSeen` بالوسيط `signedPacket`، ويتجاهل أي استثناء في كتلة `catch` فارغة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:635]

```
636:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:636]

```
637:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:637]

```
638:    private fun buildAnnouncementPayload(announcement: IdentityAnnouncement, nickname: String): ByteArray? {
```
> يُعرّف دالة خاصة (private) اسمها `buildAnnouncementPayload` (بناء حمولة الإعلان) تأخذ وسيطاً `announcement` من نوع `IdentityAnnouncement` ووسيطاً `nickname` من نوع `String` وتُعيد `ByteArray?` (مصفوفة بايتات قابلة للفراغ). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:638]

```
639:        var tlvPayload = announcement.encode() ?: return null
```
> يُعرّف متغيراً متغيّر القيمة (var) اسمه `tlvPayload` ويُسنِد إليه ناتج `announcement.encode()` (ترميز الإعلان)، وإذا كان فارغاً يُعيد `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:639]

```
640:        val directPeersForGossip = getDirectPeerIDsForGossip()
```
> يُعرّف متغيراً ثابتاً اسمه `directPeersForGossip` (النظراء المباشرون للنميمة) ويُسنِد إليه ناتج استدعاء الدالة `getDirectPeerIDsForGossip()`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:640]

```
641:        try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:641]

```
642:            if (directPeersForGossip.isNotEmpty()) {
```
> إذا كانت `directPeersForGossip` غير فارغة (`isNotEmpty`) يبدأ كتلة شرطية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:642]

```
643:                tlvPayload += com.bitchat.android.services.meshgraph.GossipTLV.encodeNeighbors(directPeersForGossip)
```
> يُضيف إلى `tlvPayload` (عبر `+=`) ناتج `com.bitchat.android.services.meshgraph.GossipTLV.encodeNeighbors` (ترميز الجيران في GossipTLV) بالوسيط `directPeersForGossip`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:643]

```
644:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:644]

```
645:            com.bitchat.android.services.meshgraph.MeshGraphService.getInstance()
```
> يستدعي `com.bitchat.android.services.meshgraph.MeshGraphService.getInstance()` (الحصول على نسخة خدمة رسم الشبكة المتشابكة) ويبدأ سلسلة استدعاء متّصلة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:645]

```
646:                .updateFromAnnouncement(myPeerID, nickname, directPeersForGossip, System.currentTimeMillis().toULong())
```
> يستدعي على النتيجة السابقة الدالة `updateFromAnnouncement` (التحديث من الإعلان) بالوسائط `myPeerID` و`nickname` و`directPeersForGossip` و`System.currentTimeMillis().toULong()` (الوقت الحالي بالمللي ثانية محوّلاً إلى عدد صحيح طويل بلا إشارة). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:646]

```
647:        } catch (_: Exception) { }
```
> يُغلق كتلة `try` ويتجاهل أي استثناء في كتلة `catch` فارغة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:647]

```
648:        return tlvPayload
```
> يُعيد قيمة المتغير `tlvPayload`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:648]

```
649:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:649]

```
650:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:650]

```
651:    private fun getDirectPeerIDsForGossip(): List<String> {
```
> يُعرّف دالة خاصة اسمها `getDirectPeerIDsForGossip` (الحصول على معرّفات النظراء المباشرين للنميمة) لا تأخذ وسائط وتُعيد `List<String>` (قائمة نصوص). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:651]

```
652:        return try {
```
> يبدأ إعادة قيمة ناتجة عن تعبير `try`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:652]

```
653:            val verifiedDirect = peerManager.getVerifiedPeers()
```
> يُعرّف متغيراً ثابتاً اسمه `verifiedDirect` (المباشرون المُتحقَّق منهم) ويبدأ إسناده بناتج `peerManager.getVerifiedPeers()` (النظراء المُتحقَّق منهم من مدير النظراء). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:653]

```
654:                .filter { it.value.isDirectConnection }
```
> يُطبّق على النتيجة السابقة الدالة `filter` بشرط أن تكون `it.value.isDirectConnection` (هل القيمة اتصال مباشر) صحيحة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:654]

```
655:                .keys
```
> يأخذ من النتيجة السابقة الخاصية `keys` (المفاتيح). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:655]

```
656:            val localDirect = (verifiedDirect + directPeers).toSet()
```
> يُعرّف متغيراً ثابتاً اسمه `localDirect` (المباشرون المحليون) ويُسنِد إليه ناتج جمع `verifiedDirect` مع `directPeers` ثم تحويله إلى مجموعة عبر `toSet()`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:656]

```
657:            // Publish this transport's direct peers and gossip the cross-transport union so a
```
> تعليق: «انشر النظراء المباشرين لهذا الناقل وأذِع اتحاد عبر-النواقل حتى». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:657]

```
658:            // node connected via multiple transports advertises a complete neighbor list.
```
> تعليق: «عقدة متصلة عبر نواقل متعددة تُعلِن قائمة جيران كاملة». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:658]

```
659:            try { com.bitchat.android.services.AppStateStore.setTransportDirectPeers(transport.id, localDirect) } catch (_: Exception) { }
```
> يستدعي ضمن كتلة `try` الدالة `com.bitchat.android.services.AppStateStore.setTransportDirectPeers` (ضبط نظراء الناقل المباشرين في مخزن حالة التطبيق) بالوسيطين `transport.id` و`localDirect`، ويتجاهل أي استثناء في كتلة `catch` فارغة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:659]

```
660:            val union = try {
```
> يُعرّف متغيراً ثابتاً اسمه `union` (الاتحاد) ويبدأ إسناده بناتج تعبير `try`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:660]

```
661:                com.bitchat.android.services.AppStateStore.getDirectPeers().ifEmpty { localDirect }
```
> يستدعي `com.bitchat.android.services.AppStateStore.getDirectPeers()` (الحصول على النظراء المباشرين من مخزن حالة التطبيق)، وإذا كانت فارغة (`ifEmpty`) يستخدم `localDirect`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:661]

```
662:            } catch (_: Exception) { localDirect }
```
> يُغلق كتلة `try` وفي حالة استثناء يُعيد `localDirect` من كتلة `catch`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:662]

```
663:            union.distinct().take(10)
```
> يُطبّق على `union` الدالة `distinct()` (إزالة المكرّر) ثم `take(10)` (أخذ أول عشرة عناصر) ويُعيد الناتج كقيمة لتعبير `try` الخارجي. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:663]

```
664:        } catch (_: Exception) {
```
> يُغلق كتلة `try` الخارجية ويبدأ كتلة `catch` لاستثناء مُتجاهَل الاسم. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:664]

```
665:            directPeers.toList().take(10)
```
> يُحوّل `directPeers` إلى قائمة عبر `toList()` ثم يأخذ أول عشرة عناصر عبر `take(10)` ويُعيدها كقيمة لكتلة `catch`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:665]

```
666:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:666]

```
667:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:667]

```
668:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:668]

```
669:    fun sendLeaveAnnouncement() {
```
> يُعرّف دالة عامة اسمها `sendLeaveAnnouncement` (إرسال إعلان المغادرة) لا تأخذ وسائط ولا تُرجع قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:669]

```
670:        val payload = hooks.leavePayloadProvider?.invoke() ?: byteArrayOf()
```
> يُعرّف متغيراً ثابتاً اسمه `payload` ويُسنِد إليه ناتج `hooks.leavePayloadProvider?.invoke()` (مزوّد حمولة المغادرة في الخطّافات إن لم يكن فارغاً)، وإذا كان فارغاً يستخدم `byteArrayOf()` (مصفوفة بايتات فارغة). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:670]

```
671:        val packet = BitchatPacket(
```
> يُعرّف متغيراً ثابتاً اسمه `packet` ويبدأ إسناد كائن `BitchatPacket` مُنشأ إليه. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:671]

```
672:            type = MessageType.LEAVE.value,
```
> يضبط الوسيط المسمّى `type` على قيمة `MessageType.LEAVE.value` (قيمة نوع الرسالة «مغادرة»). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:672]

```
673:            ttl = maxTtl,
```
> يضبط الوسيط المسمّى `ttl` على قيمة المتغير `maxTtl`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:673]

```
674:            senderID = myPeerID,
```
> يضبط الوسيط المسمّى `senderID` على قيمة المتغير `myPeerID`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:674]

```
675:            payload = payload
```
> يضبط الوسيط المسمّى `payload` على قيمة المتغير `payload`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:675]

```
676:        )
```
> إغلاق قائمة وسائط منشئ `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:676]

```
677:        val signedPacket = signPacketBeforeBroadcast(packet)
```
> يُعرّف متغيراً ثابتاً اسمه `signedPacket` ويُسنِد إليه ناتج `signPacketBeforeBroadcast(packet)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:677]

```
678:        dispatchGlobal(RoutedPacket(signedPacket))
```
> يستدعي الدالة `dispatchGlobal` بوسيط هو كائن `RoutedPacket` مُنشأ من `signedPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:678]

```
679:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:679]

```
680:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:680]

```
681:    fun getPeerNicknames(): Map<String, String> = peerManager.getAllPeerNicknames()
```
> يُعرّف دالة عامة اسمها `getPeerNicknames` (الحصول على أسماء النظراء المستعارة) تُعيد `Map<String, String>` وتُسنِد قيمتها مباشرة من `peerManager.getAllPeerNicknames()`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:681]

```
682:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:682]

```
683:    fun getPeerRSSI(): Map<String, Int> = peerManager.getAllPeerRSSI()
```
> يُعرّف دالة عامة اسمها `getPeerRSSI` (الحصول على قوة إشارة النظراء RSSI) تُعيد `Map<String, Int>` وتُسنِد قيمتها مباشرة من `peerManager.getAllPeerRSSI()`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:683]

```
684:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:684]

```
685:    fun getPeerNickname(peerID: String): String? = peerManager.getPeerNickname(peerID)
```
> يُعرّف دالة عامة اسمها `getPeerNickname` (الحصول على الاسم المستعار لنظير) تأخذ `peerID` من نوع `String` وتُعيد `String?` وتُسنِد قيمتها مباشرة من `peerManager.getPeerNickname(peerID)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:685]

```
686:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:686]

```
687:    fun addOrUpdatePeer(peerID: String, nickname: String): Boolean {
```
> يُعرّف دالة عامة اسمها `addOrUpdatePeer` (إضافة أو تحديث نظير) تأخذ `peerID` و`nickname` من نوع `String` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:687]

```
688:        return peerManager.addOrUpdatePeer(peerID, nickname)
```
> يُعيد ناتج `peerManager.addOrUpdatePeer(peerID, nickname)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:688]

```
689:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:689]

```
690:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:690]

```
691:    fun removePeer(peerID: String) {
```
> يُعرّف دالة عامة اسمها `removePeer` (إزالة نظير) تأخذ `peerID` من نوع `String` ولا تُرجع قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:691]

```
692:        peerManager.removePeer(peerID)
```
> يستدعي `peerManager.removePeer(peerID)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:692]

```
693:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:693]

```
694:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:694]

```
695:    fun setDirectConnection(peerID: String, isDirect: Boolean) {
```
> يُعرّف دالة عامة اسمها `setDirectConnection` (ضبط الاتصال المباشر) تأخذ `peerID` من نوع `String` و`isDirect` من نوع `Boolean` ولا تُرجع قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:695]

```
696:        if (isDirect) {
```
> إذا كانت `isDirect` صحيحة يبدأ كتلة شرطية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:696]

```
697:            directPeers.add(peerID)
```
> يستدعي `directPeers.add(peerID)` (إضافة المعرّف إلى مجموعة النظراء المباشرين). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:697]

```
698:        } else {
```
> يُغلق الكتلة الشرطية ويبدأ كتلة `else`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:698]

```
699:            directPeers.remove(peerID)
```
> يستدعي `directPeers.remove(peerID)` (إزالة المعرّف من مجموعة النظراء المباشرين). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:699]

```
700:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:700]

```
701:        peerManager.refreshPeerList()
```
> يستدعي `peerManager.refreshPeerList()` (تحديث قائمة النظراء). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:701]

```
702:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:702]

```
703:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:703]

```
704:    fun updatePeerRSSI(peerID: String, rssi: Int) {
```
> يُعرّف دالة عامة اسمها `updatePeerRSSI` (تحديث قوة إشارة النظير) تأخذ `peerID` من نوع `String` و`rssi` من نوع `Int` ولا تُرجع قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:704]

```
705:        peerManager.updatePeerRSSI(peerID, rssi)
```
> يستدعي `peerManager.updatePeerRSSI(peerID, rssi)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:705]

```
706:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:706]

```
707:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:707]

```
708:    fun getDebugInfoWithDeviceAddresses(deviceMap: Map<String, String>): String {
```
> يُعرّف دالة عامة اسمها `getDebugInfoWithDeviceAddresses` (الحصول على معلومات التصحيح مع عناوين الأجهزة) تأخذ `deviceMap` من نوع `Map<String, String>` وتُعيد `String`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:708]

```
709:        return peerManager.getDebugInfoWithDeviceAddresses(deviceMap)
```
> يُعيد ناتج `peerManager.getDebugInfoWithDeviceAddresses(deviceMap)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:709]

```
710:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:710]

```
711:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:711]

```
712:    fun getFingerprintDebugInfo(): String {
```
> يُعرّف دالة عامة اسمها `getFingerprintDebugInfo` (الحصول على معلومات تصحيح البصمة) لا تأخذ وسائط وتُعيد `String`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:712]

```
713:        return peerManager.getFingerprintDebugInfo()
```
> يُعيد ناتج `peerManager.getFingerprintDebugInfo()`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:713]

```
714:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:714]

```
715:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:715]

```
716:    fun hasEstablishedSession(peerID: String): Boolean {
```
> يُعرّف دالة عامة اسمها `hasEstablishedSession` (هل توجد جلسة مُنشأة) تأخذ `peerID` من نوع `String` وتُعيد `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:716]

```
717:        return encryptionService.hasEstablishedSession(peerID)
```
> يُعيد ناتج `encryptionService.hasEstablishedSession(peerID)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:717]

```
718:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:718]

```
719:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:719]

```
720:    fun getSessionState(peerID: String): com.bitchat.android.noise.NoiseSession.NoiseSessionState {
```
> يُعرّف دالة عامة اسمها `getSessionState` (الحصول على حالة الجلسة) تأخذ `peerID` من نوع `String` وتُعيد `com.bitchat.android.noise.NoiseSession.NoiseSessionState` (حالة جلسة Noise). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:720]

```
721:        return encryptionService.getSessionState(peerID)
```
> يُعيد ناتج `encryptionService.getSessionState(peerID)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:721]

```
722:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:722]

```
723:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:723]

```
724:    fun initiateNoiseHandshake(peerID: String) {
```
> يُعرّف دالة عامة اسمها `initiateNoiseHandshake` (بدء مصافحة Noise) تأخذ `peerID` من نوع `String` ولا تُرجع قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:724]

```
725:        scope.launch {
```
> يستدعي `scope.launch` (إطلاق كوروتين في النطاق) ويبدأ كتلتها. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:725]

```
726:            try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:726]

```
727:                val handshakeData = encryptionService.initiateHandshake(peerID) ?: return@launch
```
> يُعرّف متغيراً ثابتاً اسمه `handshakeData` (بيانات المصافحة) ويُسنِد إليه ناتج `encryptionService.initiateHandshake(peerID)`، وإذا كان فارغاً يخرج من كتلة الإطلاق عبر `return@launch`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:727]

```
728:                val packet = BitchatPacket(
```
> يُعرّف متغيراً ثابتاً اسمه `packet` ويبدأ إسناد كائن `BitchatPacket` مُنشأ إليه. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:728]

```
729:                    version = 1u,
```
> يضبط الوسيط المسمّى `version` (الإصدار) على القيمة `1u` (واحد بلا إشارة). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:729]

```
730:                    type = MessageType.NOISE_HANDSHAKE.value,
```
> يضبط الوسيط المسمّى `type` على قيمة `MessageType.NOISE_HANDSHAKE.value` (قيمة نوع الرسالة «مصافحة Noise»). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:730]

```
731:                    senderID = MeshPacketUtils.hexStringToByteArray(myPeerID),
```
> يضبط الوسيط المسمّى `senderID` على ناتج `MeshPacketUtils.hexStringToByteArray(myPeerID)` (تحويل نصّ ست عشري إلى مصفوفة بايتات للمعرّف `myPeerID`). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:731]

```
732:                    recipientID = MeshPacketUtils.hexStringToByteArray(peerID),
```
> يضبط الوسيط المسمّى `recipientID` (معرّف المُستلِم) على ناتج `MeshPacketUtils.hexStringToByteArray(peerID)` (تحويل `peerID` من نصّ ست عشري إلى مصفوفة بايتات). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:732]

```
733:                    timestamp = System.currentTimeMillis().toULong(),
```
> يضبط الوسيط المسمّى `timestamp` (الطابع الزمني) على `System.currentTimeMillis().toULong()` (الوقت الحالي بالمللي ثانية محوّلاً إلى عدد صحيح طويل بلا إشارة). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:733]

```
734:                    payload = handshakeData,
```
> يضبط الوسيط المسمّى `payload` على قيمة المتغير `handshakeData`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:734]

```
735:                    ttl = maxTtl
```
> يضبط الوسيط المسمّى `ttl` على قيمة المتغير `maxTtl`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:735]

```
736:                )
```
> إغلاق قائمة وسائط منشئ `BitchatPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:736]

```
737:                val signedPacket = signPacketBeforeBroadcast(packet)
```
> يُعرّف متغيراً ثابتاً اسمه `signedPacket` ويُسنِد إليه ناتج `signPacketBeforeBroadcast(packet)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:737]

```
738:                dispatchGlobal(RoutedPacket(signedPacket))
```
> يستدعي الدالة `dispatchGlobal` بوسيط هو كائن `RoutedPacket` مُنشأ من `signedPacket`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:738]

```
739:            } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` لاستثناء اسمه `e`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:739]

```
740:                Log.e("MeshCore", "Failed to initiate Noise handshake with $peerID: ${e.message}")
```
> يستدعي `Log.e` (تسجيل خطأ) بالوسم `"MeshCore"` ورسالة نصية «Failed to initiate Noise handshake with $peerID: ${e.message}» (فشل بدء مصافحة Noise مع المعرّف ورسالة الاستثناء). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:740]

```
741:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:741]

```
742:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:742]

```
743:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:743]

```
744:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:744]

```
745:    fun getPeerFingerprint(peerID: String): String? = peerManager.getFingerprintForPeer(peerID)
```
> يُعرّف دالة عامة اسمها `getPeerFingerprint` (الحصول على بصمة النظير) تأخذ `peerID` من نوع `String` وتُعيد `String?` وتُسنِد قيمتها مباشرة من `peerManager.getFingerprintForPeer(peerID)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:745]

```
746:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:746]

```
747:    fun getPeerInfo(peerID: String): PeerInfo? = peerManager.getPeerInfo(peerID)
```
> يُعرّف دالة عامة اسمها `getPeerInfo` (الحصول على معلومات النظير) تأخذ `peerID` من نوع `String` وتُعيد `PeerInfo?` وتُسنِد قيمتها مباشرة من `peerManager.getPeerInfo(peerID)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:747]

```
748:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:748]

```
749:    fun updatePeerInfo(
```
> يُعرّف دالة عامة اسمها `updatePeerInfo` (تحديث معلومات النظير) ويبدأ قائمة وسائطها. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:749]

```
750:        peerID: String,
```
> يُعرّف الوسيط `peerID` من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:750]

```
751:        nickname: String,
```
> يُعرّف الوسيط `nickname` من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:751]

```
752:        noisePublicKey: ByteArray,
```
> يُعرّف الوسيط `noisePublicKey` (مفتاح Noise العام) من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:752]

```
753:        signingPublicKey: ByteArray,
```
> يُعرّف الوسيط `signingPublicKey` (مفتاح التوقيع العام) من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:753]

```
754:        isVerified: Boolean
```
> يُعرّف الوسيط `isVerified` (هل مُتحقَّق منه) من نوع `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:754]

```
755:    ): Boolean = peerManager.updatePeerInfo(peerID, nickname, noisePublicKey, signingPublicKey, isVerified)
```
> يُغلق قائمة الوسائط ويُعلن أن نوع الإرجاع `Boolean` ويُسنِد قيمتها مباشرة من `peerManager.updatePeerInfo(peerID, nickname, noisePublicKey, signingPublicKey, isVerified)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:755]

```
756:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:756]

```
757:    fun getIdentityFingerprint(): String = encryptionService.getIdentityFingerprint()
```
> يُعرّف دالة عامة اسمها `getIdentityFingerprint` (الحصول على بصمة الهوية) لا تأخذ وسائط وتُعيد `String` وتُسنِد قيمتها مباشرة من `encryptionService.getIdentityFingerprint()`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:757]

```
758:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:758]

```
759:    fun getStaticNoisePublicKey(): ByteArray? = encryptionService.getStaticPublicKey()
```
> يُعرّف دالة عامة اسمها `getStaticNoisePublicKey` (الحصول على مفتاح Noise العام الثابت) لا تأخذ وسائط وتُعيد `ByteArray?` وتُسنِد قيمتها مباشرة من `encryptionService.getStaticPublicKey()`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:759]

```
760:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:760]

```
761:    fun shouldShowEncryptionIcon(peerID: String): Boolean = encryptionService.hasEstablishedSession(peerID)
```
> يُعرّف دالة عامة اسمها `shouldShowEncryptionIcon` (هل تُعرض أيقونة التشفير) تأخذ `peerID` من نوع `String` وتُعيد `Boolean` وتُسنِد قيمتها مباشرة من `encryptionService.hasEstablishedSession(peerID)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:761]

```
762:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:762]

```
763:    fun getEncryptedPeers(): List<String> = emptyList()
```
> يُعرّف دالة عامة اسمها `getEncryptedPeers` (الحصول على النظراء المشفَّرين) لا تأخذ وسائط وتُعيد `List<String>` وتُسنِد قيمتها مباشرة من `emptyList()` (قائمة فارغة). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:763]

```
764:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:764]

```
765:    fun getActivePeerCount(): Int = try { peerManager.getActivePeerCount() } catch (_: Exception) { 0 }
```
> يُعرّف دالة عامة اسمها `getActivePeerCount` (الحصول على عدد النظراء النشِطين) لا تأخذ وسائط وتُعيد `Int`، وتُسنِد قيمتها من تعبير `try` الذي يستدعي `peerManager.getActivePeerCount()`، وفي حالة استثناء يُعيد `0`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:765]

```
766:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:766]

```
767:    fun refreshPeerList() {
```
> يُعرّف دالة عامة اسمها `refreshPeerList` (تحديث قائمة النظراء) لا تأخذ وسائط ولا تُرجع قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:767]

```
768:        try { peerManager.refreshPeerList() } catch (_: Exception) { }
```
> يستدعي ضمن كتلة `try` الدالة `peerManager.refreshPeerList()` ويتجاهل أي استثناء في كتلة `catch` فارغة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:768]

```
769:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:769]

```
770:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:770]

```
771:    fun getDeviceAddressForPeer(peerID: String): String? = transport.getDeviceAddressForPeer(peerID)
```
> يُعرّف دالة عامة اسمها `getDeviceAddressForPeer` (الحصول على عنوان الجهاز للنظير) تأخذ `peerID` من نوع `String` وتُعيد `String?` وتُسنِد قيمتها مباشرة من `transport.getDeviceAddressForPeer(peerID)`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:771]

```
772:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:772]

```
773:    fun getDeviceAddressToPeerMapping(): Map<String, String> = transport.getDeviceAddressToPeerMapping()
```
> يُعرّف دالة عامة اسمها `getDeviceAddressToPeerMapping` (الحصول على تخطيط عنوان الجهاز إلى النظير) لا تأخذ وسائط وتُعيد `Map<String, String>` وتُسنِد قيمتها مباشرة من `transport.getDeviceAddressToPeerMapping()`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:773]

```
774:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:774]

```
775:    fun getDebugStatus(
```
> يُعرّف دالة عامة اسمها `getDebugStatus` (الحصول على حالة التصحيح) ويبدأ قائمة وسائطها. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:775]

```
776:        transportInfo: String,
```
> يُعرّف الوسيط `transportInfo` (معلومات الناقل) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:776]

```
777:        deviceMap: Map<String, String>,
```
> يُعرّف الوسيط `deviceMap` (خريطة الأجهزة) من نوع `Map<String, String>`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:777]

```
778:        extraLines: List<String> = emptyList(),
```
> يُعرّف الوسيط `extraLines` (أسطر إضافية) من نوع `List<String>` بقيمة افتراضية `emptyList()` (قائمة فارغة). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:778]

```
779:        title: String? = null
```
> يُعرّف الوسيط `title` (العنوان) من نوع `String?` بقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:779]

```
780:    ): String {
```
> يُغلق قائمة الوسائط ويُعلن أن نوع الإرجاع `String` ويبدأ جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:780]

```
781:        return buildString {
```
> يبدأ إعادة ناتج `buildString` (بناء نصّ) ويبدأ كتلتها. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:781]

```
782:            appendLine("=== ${title ?: "${transport.id} Mesh Debug Status"} ===")
```
> يستدعي `appendLine` لإلحاق سطر نصّي «=== » متبوعاً بـ `title` أو بالنصّ «${transport.id} Mesh Debug Status» (معرّف الناقل ثم «حالة تصحيح الشبكة المتشابكة») ثم « ===». [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:782]

```
783:            appendLine("My Peer ID: $myPeerID")
```
> يستدعي `appendLine` لإلحاق سطر نصّي «My Peer ID: $myPeerID» (معرّف نظيري ثم قيمة `myPeerID`). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:783]

```
784:            if (extraLines.isNotEmpty()) {
```
> إذا كانت `extraLines` غير فارغة (`isNotEmpty`) يبدأ كتلة شرطية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:784]

```
785:                extraLines.forEach { appendLine(it) }
```
> يُطبّق على `extraLines` الدالة `forEach` التي تستدعي `appendLine(it)` لكل عنصر (إلحاق كل سطر إضافي). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:785]

```
786:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:786]

```
787:            appendLine(transportInfo)
```
> يستدعي `appendLine(transportInfo)` لإلحاق قيمة `transportInfo` كسطر. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:787]

```
788:            appendLine(peerManager.getDebugInfo(deviceMap))
```
> يستدعي `appendLine` لإلحاق ناتج `peerManager.getDebugInfo(deviceMap)` (معلومات تصحيح مدير النظراء) كسطر. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:788]

```
789:            appendLine(fragmentManager.getDebugInfo())
```
> يستدعي `appendLine` لإلحاق ناتج `fragmentManager.getDebugInfo()` (معلومات تصحيح مدير الأجزاء) كسطر. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:789]

```
790:            appendLine(securityManager.getDebugInfo())
```
> يستدعي `appendLine` لإلحاق ناتج `securityManager.getDebugInfo()` (معلومات تصحيح مدير الأمن) كسطر. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:790]

```
791:            appendLine(storeForwardManager.getDebugInfo())
```
> يستدعي `appendLine` لإلحاق ناتج `storeForwardManager.getDebugInfo()` (معلومات تصحيح مدير التخزين والتمرير) كسطر. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:791]

```
792:            appendLine(messageHandler.getDebugInfo())
```
> يستدعي `appendLine` لإلحاق ناتج `messageHandler.getDebugInfo()` (معلومات تصحيح معالج الرسائل) كسطر. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:792]

```
793:            appendLine(packetProcessor.getDebugInfo())
```
> يستدعي `appendLine` لإلحاق ناتج `packetProcessor.getDebugInfo()` (معلومات تصحيح معالج الحزم) كسطر. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:793]

```
794:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:794]

```
795:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:795]

```
796:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:796]

```
797:    fun clearAllInternalData() {
```
> يُعرّف دالة عامة اسمها `clearAllInternalData` (مسح كل البيانات الداخلية) لا تأخذ وسائط ولا تُرجع قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:797]

```
798:        fragmentManager.clearAllFragments()
```
> يستدعي `fragmentManager.clearAllFragments()` (مسح كل الأجزاء في مدير الأجزاء). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:798]

```
799:        storeForwardManager.clearAllCache()
```
> يستدعي `storeForwardManager.clearAllCache()` (مسح كل الذاكرة المؤقتة في مدير التخزين والتمرير). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:799]

```
800:        securityManager.clearAllData()
```
> يستدعي `securityManager.clearAllData()` (مسح كل البيانات في مدير الأمن). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:800]
