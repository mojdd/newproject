# شريحة — app/src/main/java/com/bitchat/android/mesh/MeshService.kt (الأسطر 1–56)

```
1: package com.bitchat.android.mesh
```
> يُعلِن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:2]

```
3: import com.bitchat.android.model.BitchatFilePacket
```
> يستورد (import) الصنف `BitchatFilePacket` من الحزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:4]

```
5: /**
```
> تعليق: بداية كتلة تعليق توثيقي (مفتوحة بـ `/**`). [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:5]

```
6:  * Transport-agnostic mesh service API for UI and routing layers.
```
> تعليق: واجهة برمجية لخدمة الشبكة المتشابكة (mesh service) غير معتمدة على وسيلة النقل، مخصّصة لطبقتَي الواجهة والتوجيه. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:6]

```
7:  */
```
> تعليق: إغلاق كتلة التعليق التوثيقي (بـ `*/`). [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:7]

```
8: interface MeshService {
```
> يُعرِّف واجهة (interface) باسم `MeshService` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:8]

```
9:     val myPeerID: String
```
> يُعرِّف خاصية للقراءة فقط (val) باسم `myPeerID` معرّف ندّي (peerID) من نوع نص `String`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:9]

```
10:     var delegate: MeshDelegate?
```
> يُعرِّف خاصية قابلة للتغيير (var) باسم `delegate` (المُفوَّض) من نوع `MeshDelegate` يقبل القيمة الفارغة (nullable). [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:11]

```
12:     fun startServices()
```
> يُعلِن دالّة (fun) باسم `startServices` (بدء الخدمات) بلا وُسطاء ولا قيمة مُعادة معلَنة. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:12]

```
13:     fun stopServices()
```
> يُعلِن دالّة باسم `stopServices` (إيقاف الخدمات) بلا وُسطاء ولا قيمة مُعادة معلَنة. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:13]

```
14: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:14]

```
15:     fun sendMessage(content: String, mentions: List<String> = emptyList(), channel: String? = null)
```
> يُعلِن دالّة باسم `sendMessage` (إرسال رسالة) تأخذ وسيطاً `content` نصّياً، ووسيطاً `mentions` (إشارات) قائمة نصوص قيمتُه الافتراضية قائمة فارغة `emptyList()`، ووسيطاً `channel` (قناة) نصّياً يقبل الفراغ قيمتُه الافتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:15]

```
16:     fun sendPrivateMessage(content: String, recipientPeerID: String, recipientNickname: String, messageID: String? = null)
```
> يُعلِن دالّة باسم `sendPrivateMessage` (إرسال رسالة خاصة) تأخذ `content` نصّياً، و`recipientPeerID` (معرّف الندّ المستقبِل) نصّياً، و`recipientNickname` (اسم المستقبِل المستعار) نصّياً، و`messageID` (معرّف الرسالة) نصّياً يقبل الفراغ قيمتُه الافتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:16]

```
17:     fun sendReadReceipt(messageID: String, recipientPeerID: String, readerNickname: String)
```
> يُعلِن دالّة باسم `sendReadReceipt` (إرسال إيصال قراءة) تأخذ `messageID` نصّياً، و`recipientPeerID` نصّياً، و`readerNickname` (اسم القارئ المستعار) نصّياً. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:17]

```
18:     fun sendDeliveryAck(messageID: String, recipientPeerID: String) {}
```
> يُعرِّف دالّة باسم `sendDeliveryAck` (إرسال إقرار تسليم) تأخذ `messageID` نصّياً و`recipientPeerID` نصّياً، بجسم افتراضي فارغ `{}`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:18]

```
19:     fun sendFavoriteNotification(peerID: String, isFavorite: Boolean) {}
```
> يُعرِّف دالّة باسم `sendFavoriteNotification` (إرسال إشعار تفضيل) تأخذ `peerID` نصّياً و`isFavorite` (هل مفضَّل) منطقياً `Boolean`، بجسم افتراضي فارغ `{}`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:19]

```
20:     fun sendVerifyChallenge(peerID: String, noiseKeyHex: String, nonceA: ByteArray)
```
> يُعلِن دالّة باسم `sendVerifyChallenge` (إرسال تحدّي تحقّق) تأخذ `peerID` نصّياً، و`noiseKeyHex` (مفتاح Noise بالنظام السّتّ عشري) نصّياً، و`nonceA` (الرّقم العشوائي المؤقّت أ) من نوع مصفوفة بايتات `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:20]

```
21:     fun sendVerifyResponse(peerID: String, noiseKeyHex: String, nonceA: ByteArray)
```
> يُعلِن دالّة باسم `sendVerifyResponse` (إرسال ردّ تحقّق) تأخذ `peerID` نصّياً، و`noiseKeyHex` نصّياً، و`nonceA` من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:21]

```
22:     fun sendFileBroadcast(file: BitchatFilePacket)
```
> يُعلِن دالّة باسم `sendFileBroadcast` (بثّ ملف للجميع) تأخذ وسيطاً `file` من نوع `BitchatFilePacket`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:22]

```
23:     fun sendFilePrivate(recipientPeerID: String, file: BitchatFilePacket)
```
> يُعلِن دالّة باسم `sendFilePrivate` (إرسال ملف بشكل خاص) تأخذ `recipientPeerID` نصّياً و`file` من نوع `BitchatFilePacket`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:23]

```
24:     fun cancelFileTransfer(transferId: String): Boolean
```
> يُعلِن دالّة باسم `cancelFileTransfer` (إلغاء نقل ملف) تأخذ `transferId` (معرّف النقل) نصّياً وتُعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:25]

```
26:     fun sendBroadcastAnnounce()
```
> يُعلِن دالّة باسم `sendBroadcastAnnounce` (بثّ إعلان للجميع) بلا وُسطاء ولا قيمة مُعادة معلَنة. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:26]

```
27:     fun sendAnnouncementToPeer(peerID: String)
```
> يُعلِن دالّة باسم `sendAnnouncementToPeer` (إرسال إعلان إلى ندّ) تأخذ `peerID` نصّياً. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:28]

```
29:     fun getPeerNicknames(): Map<String, String>
```
> يُعلِن دالّة باسم `getPeerNicknames` (جلب الأسماء المستعارة للأنداد) بلا وُسطاء وتُعيد خريطة `Map` مفاتيحها نصوص وقيمها نصوص. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:29]

```
30:     fun getPeerRSSI(): Map<String, Int>
```
> يُعلِن دالّة باسم `getPeerRSSI` (جلب قوّة إشارة الأنداد RSSI) بلا وُسطاء وتُعيد خريطة `Map` مفاتيحها نصوص وقيمها أعداد صحيحة `Int`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:30]

```
31:     fun getActivePeerCount(): Int
```
> يُعلِن دالّة باسم `getActivePeerCount` (جلب عدد الأنداد النشِطين) بلا وُسطاء وتُعيد عدداً صحيحاً `Int`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:31]

```
32:     fun hasEstablishedSession(peerID: String): Boolean
```
> يُعلِن دالّة باسم `hasEstablishedSession` (هل توجد جلسة مُنشأة) تأخذ `peerID` نصّياً وتُعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:32]

```
33:     fun getSessionState(peerID: String): com.bitchat.android.noise.NoiseSession.NoiseSessionState
```
> يُعلِن دالّة باسم `getSessionState` (جلب حالة الجلسة) تأخذ `peerID` نصّياً وتُعيد قيمة من النوع `com.bitchat.android.noise.NoiseSession.NoiseSessionState` (حالة جلسة Noise). [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:33]

```
34:     fun initiateNoiseHandshake(peerID: String)
```
> يُعلِن دالّة باسم `initiateNoiseHandshake` (بدء مصافحة Noise) تأخذ `peerID` نصّياً. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:34]

```
35:     fun getPeerFingerprint(peerID: String): String?
```
> يُعلِن دالّة باسم `getPeerFingerprint` (جلب بصمة الندّ) تأخذ `peerID` نصّياً وتُعيد نصّاً `String` يقبل الفراغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:35]

```
36:     fun getPeerInfo(peerID: String): PeerInfo?
```
> يُعلِن دالّة باسم `getPeerInfo` (جلب معلومات الندّ) تأخذ `peerID` نصّياً وتُعيد كائناً من نوع `PeerInfo` يقبل الفراغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:36]

```
37:     fun updatePeerInfo(
```
> يُعلِن دالّة باسم `updatePeerInfo` (تحديث معلومات الندّ) ويفتح قائمة وُسطائها. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:37]

```
38:         peerID: String,
```
> وسيط `peerID` نصّي. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:38]

```
39:         nickname: String,
```
> وسيط `nickname` (الاسم المستعار) نصّي. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:39]

```
40:         noisePublicKey: ByteArray,
```
> وسيط `noisePublicKey` (المفتاح العامّ لـ Noise) من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:40]

```
41:         signingPublicKey: ByteArray,
```
> وسيط `signingPublicKey` (المفتاح العامّ للتوقيع) من نوع `ByteArray`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:41]

```
42:         isVerified: Boolean
```
> وسيط `isVerified` (هل مُتحقَّق منه) منطقي `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:42]

```
43:     ): Boolean
```
> إغلاق قائمة وُسطاء الدالّة، وتُعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:43]

```
44:     fun getIdentityFingerprint(): String
```
> يُعلِن دالّة باسم `getIdentityFingerprint` (جلب بصمة الهوية) بلا وُسطاء وتُعيد نصّاً `String`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:44]

```
45:     fun getStaticNoisePublicKey(): ByteArray?
```
> يُعلِن دالّة باسم `getStaticNoisePublicKey` (جلب مفتاح Noise العامّ الثابت) بلا وُسطاء وتُعيد مصفوفة بايتات `ByteArray` تقبل الفراغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:45]

```
46:     fun shouldShowEncryptionIcon(peerID: String): Boolean
```
> يُعلِن دالّة باسم `shouldShowEncryptionIcon` (هل يُعرَض رمز التشفير) تأخذ `peerID` نصّياً وتُعيد قيمة منطقية `Boolean`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:46]

```
47:     fun getEncryptedPeers(): List<String>
```
> يُعلِن دالّة باسم `getEncryptedPeers` (جلب الأنداد المُشفَّرين) بلا وُسطاء وتُعيد قائمة نصوص `List<String>`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:47]

```
48: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:48]

```
49:     fun getDeviceAddressForPeer(peerID: String): String?
```
> يُعلِن دالّة باسم `getDeviceAddressForPeer` (جلب عنوان الجهاز لندّ) تأخذ `peerID` نصّياً وتُعيد نصّاً `String` يقبل الفراغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:49]

```
50:     fun getDeviceAddressToPeerMapping(): Map<String, String>
```
> يُعلِن دالّة باسم `getDeviceAddressToPeerMapping` (جلب خريطة عناوين الأجهزة إلى الأنداد) بلا وُسطاء وتُعيد خريطة `Map` مفاتيحها نصوص وقيمها نصوص. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:50]

```
51:     fun printDeviceAddressesForPeers(): String
```
> يُعلِن دالّة باسم `printDeviceAddressesForPeers` (طباعة عناوين الأجهزة للأنداد) بلا وُسطاء وتُعيد نصّاً `String`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:51]

```
52:     fun getDebugStatus(): String
```
> يُعلِن دالّة باسم `getDebugStatus` (جلب حالة التنقيح) بلا وُسطاء وتُعيد نصّاً `String`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:52]

```
53: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:53]

```
54:     fun clearAllInternalData()
```
> يُعلِن دالّة باسم `clearAllInternalData` (مسح كل البيانات الداخلية) بلا وُسطاء ولا قيمة مُعادة معلَنة. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:54]

```
55:     fun clearAllEncryptionData()
```
> يُعلِن دالّة باسم `clearAllEncryptionData` (مسح كل بيانات التشفير) بلا وُسطاء ولا قيمة مُعادة معلَنة. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:55]

```
56: }
```
> إغلاق نطاق الواجهة `MeshService`. [app/src/main/java/com/bitchat/android/mesh/MeshService.kt:56]
