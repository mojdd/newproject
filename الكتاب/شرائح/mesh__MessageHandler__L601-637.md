# شريحة — app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt (الأسطر 601–637)

```
601:     fun removePeer(peerID: String)
```
> يُعرِّف دالةً مُجرّدة باسم «إزالة القرين» (removePeer) تأخذ مُعاملاً نصياً واحداً اسمه معرّف القرين (peerID) من نوع نص (String) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:601]

```
602:     fun updatePeerNickname(peerID: String, nickname: String)
```
> يُعرِّف دالةً مُجرّدة باسم «تحديث كنية القرين» (updatePeerNickname) تأخذ مُعاملين نصيين: معرّف القرين (peerID) والكنية (nickname)، ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:602]

```
603:     fun getPeerNickname(peerID: String): String?
```
> يُعرِّف دالةً مُجرّدة باسم «جلب كنية القرين» (getPeerNickname) تأخذ معرّف القرين (peerID) نصاً وتُعيد نصاً قابلاً للعدم (String?). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:603]

```
604:     fun getNetworkSize(): Int
```
> يُعرِّف دالةً مُجرّدة باسم «جلب حجم الشبكة» (getNetworkSize) بلا مُعاملات وتُعيد عدداً صحيحاً (Int). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:604]

```
605:     fun getMyNickname(): String?
```
> يُعرِّف دالةً مُجرّدة باسم «جلب كنيتي» (getMyNickname) بلا مُعاملات وتُعيد نصاً قابلاً للعدم (String?). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:605]

```
606:     fun getPeerInfo(peerID: String): PeerInfo?
```
> يُعرِّف دالةً مُجرّدة باسم «جلب معلومات القرين» (getPeerInfo) تأخذ معرّف القرين (peerID) نصاً وتُعيد كائناً من نوع معلومات القرين (PeerInfo) قابلاً للعدم. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:606]

```
607:     fun updatePeerInfo(peerID: String, nickname: String, noisePublicKey: ByteArray, signingPublicKey: ByteArray, isVerified: Boolean): Boolean
```
> يُعرِّف دالةً مُجرّدة باسم «تحديث معلومات القرين» (updatePeerInfo) تأخذ خمسة مُعاملات: معرّف القرين (peerID) نصاً، والكنية (nickname) نصاً، ومفتاح Noise العام (noisePublicKey) مصفوفة بايتات (ByteArray)، ومفتاح التوقيع العام (signingPublicKey) مصفوفة بايتات، وقيمة هل-مُتحقَّق (isVerified) منطقية (Boolean)، وتُعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:607]

```
608:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:608]

```
609:     // Packet operations
```
> تعليق: عمليات الرزمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:609]

```
610:     fun sendPacket(packet: BitchatPacket)
```
> يُعرِّف دالةً مُجرّدة باسم «إرسال الرزمة» (sendPacket) تأخذ مُعاملاً واحداً اسمه packet من نوع رزمة بِت‌شات (BitchatPacket) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:610]

```
611:     fun relayPacket(routed: RoutedPacket)
```
> يُعرِّف دالةً مُجرّدة باسم «ترحيل الرزمة» (relayPacket) تأخذ مُعاملاً واحداً اسمه routed من نوع رزمة موجَّهة (RoutedPacket) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:611]

```
612:     fun getBroadcastRecipient(): ByteArray
```
> يُعرِّف دالةً مُجرّدة باسم «جلب مستلِم البثّ» (getBroadcastRecipient) بلا مُعاملات وتُعيد مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:612]

```
613:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:613]

```
614:     // Cryptographic operations
```
> تعليق: العمليات التعمويّة (التشفيرية). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:614]

```
615:     fun verifySignature(packet: BitchatPacket, peerID: String): Boolean
```
> يُعرِّف دالةً مُجرّدة باسم «التحقق من التوقيع» (verifySignature) تأخذ مُعاملين: الرزمة (packet) من نوع رزمة بِت‌شات (BitchatPacket) ومعرّف القرين (peerID) نصاً، وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:615]

```
616:     fun encryptForPeer(data: ByteArray, recipientPeerID: String): ByteArray?
```
> يُعرِّف دالةً مُجرّدة باسم «التعمية للقرين» (encryptForPeer) تأخذ البيانات (data) مصفوفة بايتات (ByteArray) ومعرّف القرين المستلِم (recipientPeerID) نصاً، وتُعيد مصفوفة بايتات قابلة للعدم (ByteArray?). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:616]

```
617:     fun decryptFromPeer(encryptedData: ByteArray, senderPeerID: String): ByteArray?
```
> يُعرِّف دالةً مُجرّدة باسم «فكّ التعمية من القرين» (decryptFromPeer) تأخذ البيانات المُعمّاة (encryptedData) مصفوفة بايتات (ByteArray) ومعرّف القرين المُرسِل (senderPeerID) نصاً، وتُعيد مصفوفة بايتات قابلة للعدم (ByteArray?). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:617]

```
618:     fun verifyEd25519Signature(signature: ByteArray, data: ByteArray, publicKey: ByteArray): Boolean
```
> يُعرِّف دالةً مُجرّدة باسم «التحقق من توقيع Ed25519» (verifyEd25519Signature) تأخذ ثلاثة مُعاملات: التوقيع (signature) مصفوفة بايتات (ByteArray)، والبيانات (data) مصفوفة بايتات، والمفتاح العام (publicKey) مصفوفة بايتات، وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:618]

```
619:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:619]

```
620:     // Noise protocol operations
```
> تعليق: عمليات بروتوكول Noise. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:620]

```
621:     fun hasNoiseSession(peerID: String): Boolean
```
> يُعرِّف دالةً مُجرّدة باسم «هل يوجد جلسة Noise» (hasNoiseSession) تأخذ معرّف القرين (peerID) نصاً وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:621]

```
622:     fun initiateNoiseHandshake(peerID: String)
```
> يُعرِّف دالةً مُجرّدة باسم «بدء مُصافحة Noise» (initiateNoiseHandshake) تأخذ معرّف القرين (peerID) نصاً ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:622]

```
623:     fun processNoiseHandshakeMessage(payload: ByteArray, peerID: String): ByteArray?
```
> يُعرِّف دالةً مُجرّدة باسم «معالجة رسالة مُصافحة Noise» (processNoiseHandshakeMessage) تأخذ الحمولة (payload) مصفوفة بايتات (ByteArray) ومعرّف القرين (peerID) نصاً، وتُعيد مصفوفة بايتات قابلة للعدم (ByteArray?). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:623]

```
624:     fun updatePeerIDBinding(newPeerID: String, nickname: String,
```
> يُعرِّف دالةً مُجرّدة باسم «تحديث ربط معرّف القرين» (updatePeerIDBinding) ويبدأ قائمة مُعاملاتها بمعرّف القرين الجديد (newPeerID) نصاً والكنية (nickname) نصاً، وتتمة المُعاملات في السطر التالي. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:624]

```
625:                            publicKey: ByteArray, previousPeerID: String?)
```
> يُكمل قائمة مُعاملات الدالة السابقة بالمفتاح العام (publicKey) مصفوفة بايتات (ByteArray) ومعرّف القرين السابق (previousPeerID) نصاً قابلاً للعدم (String?)، ويُغلق القوس؛ والدالة لا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:625]

```
626:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:626]

```
627:     // Message operations
```
> تعليق: عمليات الرسالة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:627]

```
628:     fun decryptChannelMessage(encryptedContent: ByteArray, channel: String): String?
```
> يُعرِّف دالةً مُجرّدة باسم «فكّ تعمية رسالة القناة» (decryptChannelMessage) تأخذ المحتوى المُعمّى (encryptedContent) مصفوفة بايتات (ByteArray) والقناة (channel) نصاً، وتُعيد نصاً قابلاً للعدم (String?). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:628]

```
629: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:629]

```
630:     // Callbacks
```
> تعليق: ردود النداء (Callbacks). [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:630]

```
631:     fun onMessageReceived(message: BitchatMessage)
```
> يُعرِّف دالةً مُجرّدة باسم «عند استلام الرسالة» (onMessageReceived) تأخذ مُعاملاً واحداً اسمه message من نوع رسالة بِت‌شات (BitchatMessage) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:631]

```
632:     fun onChannelLeave(channel: String, fromPeer: String)
```
> يُعرِّف دالةً مُجرّدة باسم «عند مغادرة القناة» (onChannelLeave) تأخذ القناة (channel) نصاً ومُرسِل الحدث (fromPeer) نصاً ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:632]

```
633:     fun onDeliveryAckReceived(messageID: String, peerID: String)
```
> يُعرِّف دالةً مُجرّدة باسم «عند استلام إقرار التسليم» (onDeliveryAckReceived) تأخذ معرّف الرسالة (messageID) نصاً ومعرّف القرين (peerID) نصاً ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:633]

```
634:     fun onReadReceiptReceived(messageID: String, peerID: String)
```
> يُعرِّف دالةً مُجرّدة باسم «عند استلام إيصال القراءة» (onReadReceiptReceived) تأخذ معرّف الرسالة (messageID) نصاً ومعرّف القرين (peerID) نصاً ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:634]

```
635:     fun onVerifyChallengeReceived(peerID: String, payload: ByteArray, timestampMs: Long)
```
> يُعرِّف دالةً مُجرّدة باسم «عند استلام تحدّي التحقق» (onVerifyChallengeReceived) تأخذ معرّف القرين (peerID) نصاً، والحمولة (payload) مصفوفة بايتات (ByteArray)، والطابع الزمني بالمللي‌ثانية (timestampMs) من نوع عدد طويل (Long)، ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:635]

```
636:     fun onVerifyResponseReceived(peerID: String, payload: ByteArray, timestampMs: Long)
```
> يُعرِّف دالةً مُجرّدة باسم «عند استلام ردّ التحقق» (onVerifyResponseReceived) تأخذ معرّف القرين (peerID) نصاً، والحمولة (payload) مصفوفة بايتات (ByteArray)، والطابع الزمني بالمللي‌ثانية (timestampMs) من نوع عدد طويل (Long)، ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:636]

```
637: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MessageHandler.kt:637]
