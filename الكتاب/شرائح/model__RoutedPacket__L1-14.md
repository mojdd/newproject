# شريحة — app/src/main/java/com/bitchat/android/model/RoutedPacket.kt (الأسطر 1–14)

```
1: package com.bitchat.android.model
```
> يُعرِّف هذا السطر أنّ الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:2]

```
3: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد هذا السطر الصنف حزمة-بِت‑شات (BitchatPacket) من الحزمة `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:4]

```
5: /**
```
> بداية تعليق توثيقي (تعليق). [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:5]

```
6:  * Represents a routed packet with additional metadata
```
> تعليق: يمثّل حزمة موجَّهة مع بيانات وصفية إضافية. [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:6]

```
7:  * Used for processing and routing packets in the mesh network
```
> تعليق: يُستعمل لمعالجة وتوجيه الحزم في الشبكة المتشابكة. [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:7]

```
8:  */
```
> نهاية التعليق التوثيقي (تعليق). [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:8]

```
9: data class RoutedPacket(
```
> يُعرِّف هذا السطر صنف بيانات (data class) باسم حزمة-موجَّهة (RoutedPacket) ويفتح قائمة وُسطائه (المُنشئ الأساسي). [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:9]

```
10:     val packet: BitchatPacket,
```
> يُعرِّف هذا السطر خاصية ثابتة (val) باسم الحزمة (packet) من نوع حزمة-بِت‑شات (BitchatPacket). [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:10]

```
11:     val peerID: String? = null,           // Who sent it (parsed from packet.senderID)
```
> يُعرِّف هذا السطر خاصية ثابتة (val) باسم معرّف-القرين (peerID) من نوع نص (String) قابل لأن يكون فارغاً (nullable) بقيمة ابتدائية حرفية `null`، مع تعليق: مَن أرسلها (مُحلَّل من `packet.senderID`). [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:11]

```
12:     val relayAddress: String? = null,     // Address it came from (for avoiding loopback)
```
> يُعرِّف هذا السطر خاصية ثابتة (val) باسم عنوان-التمرير (relayAddress) من نوع نص (String) قابل لأن يكون فارغاً (nullable) بقيمة ابتدائية حرفية `null`، مع تعليق: العنوان الذي جاءت منه (لتجنّب الالتفاف الراجع/loopback). [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:12]

```
13:     val transferId: String? = null        // Optional stable transfer ID for progress tracking
```
> يُعرِّف هذا السطر خاصية ثابتة (val) باسم معرّف-النقل (transferId) من نوع نص (String) قابل لأن يكون فارغاً (nullable) بقيمة ابتدائية حرفية `null`، مع تعليق: معرّف نقل اختياري ثابت لتتبّع التقدّم. [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:13]

```
14: )
```
> إغلاق نطاق قائمة وُسطاء المُنشئ الأساسي لصنف البيانات حزمة-موجَّهة (RoutedPacket). [app/src/main/java/com/bitchat/android/model/RoutedPacket.kt:14]
