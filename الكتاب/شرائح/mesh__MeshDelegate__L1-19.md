# شريحة — app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt (الأسطر 1–19)

```
1: package com.bitchat.android.mesh
```
> يُعلِن أنّ هذا الملف ينتمي إلى الحزمة (package) المسمّاة `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:2]

```
3: import com.bitchat.android.model.BitchatMessage
```
> يستورد (import) الصنف رسالة بِت‌شات (BitchatMessage) من الحزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:4]

```
5: /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:5]

```
6:  * Shared mesh delegate interface for transport-agnostic callbacks.
```
> تعليق: «واجهة مفوِّض الشبكة المتشابكة المشتركة لردود النداء المستقلة عن وسيلة النقل». [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:6]

```
7:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:7]

```
8: interface MeshDelegate {
```
> يُعرِّف واجهة (interface) باسم مفوِّض الشبكة المتشابكة (MeshDelegate) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:8]

```
9:     fun didReceiveMessage(message: BitchatMessage)
```
> يُصرِّح بدالة (fun) باسم «استلمَ رسالة» (didReceiveMessage) تأخذ وسيطاً `message` من نوع رسالة بِت‌شات (BitchatMessage) دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:9]

```
10:     fun didUpdatePeerList(peers: List<String>)
```
> يُصرِّح بدالة باسم «حدَّثَ قائمة النظائر» (didUpdatePeerList) تأخذ وسيطاً `peers` من نوع قائمة (List) من سلاسل نصية (String) دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:10]

```
11:     fun didReceiveChannelLeave(channel: String, fromPeer: String)
```
> يُصرِّح بدالة باسم «استلمَ مغادرة قناة» (didReceiveChannelLeave) تأخذ وسيطين: `channel` من نوع سلسلة نصية و`fromPeer` من نوع سلسلة نصية دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:11]

```
12:     fun didReceiveDeliveryAck(messageID: String, recipientPeerID: String)
```
> يُصرِّح بدالة باسم «استلمَ إقرار تسليم» (didReceiveDeliveryAck) تأخذ وسيطين: `messageID` من نوع سلسلة نصية و`recipientPeerID` من نوع سلسلة نصية دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:12]

```
13:     fun didReceiveReadReceipt(messageID: String, recipientPeerID: String)
```
> يُصرِّح بدالة باسم «استلمَ إيصال قراءة» (didReceiveReadReceipt) تأخذ وسيطين: `messageID` من نوع سلسلة نصية و`recipientPeerID` من نوع سلسلة نصية دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:13]

```
14:     fun didReceiveVerifyChallenge(peerID: String, payload: ByteArray, timestampMs: Long) {}
```
> يُعرِّف دالة باسم «استلمَ تحدِّي تحقُّق» (didReceiveVerifyChallenge) تأخذ ثلاثة وسائط: `peerID` سلسلة نصية و`payload` مصفوفة بايتات (ByteArray) و`timestampMs` عدداً صحيحاً طويلاً (Long)، بجسمٍ فارغ `{}`. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:14]

```
15:     fun didReceiveVerifyResponse(peerID: String, payload: ByteArray, timestampMs: Long) {}
```
> يُعرِّف دالة باسم «استلمَ ردّ تحقُّق» (didReceiveVerifyResponse) تأخذ ثلاثة وسائط: `peerID` سلسلة نصية و`payload` مصفوفة بايتات و`timestampMs` عدداً صحيحاً طويلاً، بجسمٍ فارغ `{}`. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:15]

```
16:     fun decryptChannelMessage(encryptedContent: ByteArray, channel: String): String?
```
> يُصرِّح بدالة باسم «فُكّ تشفير رسالة قناة» (decryptChannelMessage) تأخذ وسيطين: `encryptedContent` مصفوفة بايتات و`channel` سلسلة نصية، وتُعيد سلسلة نصية قابلة لأن تكون فارغة (String?) دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:16]

```
17:     fun getNickname(): String?
```
> يُصرِّح بدالة باسم «احصل على الاسم المستعار» (getNickname) بلا وسائط وتُعيد سلسلة نصية قابلة لأن تكون فارغة (String?) دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:17]

```
18:     fun isFavorite(peerID: String): Boolean
```
> يُصرِّح بدالة باسم «هل هو مفضَّل» (isFavorite) تأخذ وسيطاً `peerID` من نوع سلسلة نصية وتُعيد قيمة منطقية (Boolean) دون جسم. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:18]

```
19: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshDelegate.kt:19]
