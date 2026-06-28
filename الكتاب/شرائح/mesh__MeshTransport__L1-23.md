# شريحة — app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt (الأسطر 1–23)

```
1: package com.bitchat.android.mesh
```
> يعلن انتماء الملف إلى الحزمة (package) المسمّاة `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:2]

```
3: import com.bitchat.android.model.RoutedPacket
```
> يستورد (import) الصنف `RoutedPacket` من الحزمة `com.bitchat.android.model`، وهو «الرزمة الموجَّهة». [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:3]

```
4: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد (import) الصنف `BitchatPacket` من الحزمة `com.bitchat.android.protocol`، وهو «رزمة بِت‑شات». [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:5]

```
6: /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:6]

```
7:  * Transport abstraction used by MeshCore to send packets via a specific medium.
```
> تعليق: تجريد للنقل يستعمله `MeshCore` لإرسال الرزم عبر وسيط محدّد. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:7]

```
8:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:8]

```
9: interface MeshTransport {
```
> يعرّف واجهة (interface) اسمها `MeshTransport`، أي «ناقل الشبكة المتشابكة»، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:9]

```
10:     val id: String
```
> يعرّف خاصيّة قراءة (val) اسمها `id` من النوع `String` (سلسلة نصّية). [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:11]

```
12:     fun broadcastPacket(routed: RoutedPacket)
```
> يعرّف دالّة (fun) اسمها `broadcastPacket` («بثّ الرزمة») تأخذ مُعامِلاً اسمه `routed` من النوع `RoutedPacket` ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:12]

```
13: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:13]

```
14:     fun sendPacketToPeer(peerID: String, packet: BitchatPacket): Boolean
```
> يعرّف دالّة (fun) اسمها `sendPacketToPeer` («إرسال الرزمة إلى النظير») تأخذ مُعامِلاً اسمه `peerID` من النوع `String` ومُعامِلاً اسمه `packet` من النوع `BitchatPacket`، وتُعيد قيمة من النوع `Boolean` (منطقية). [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:14]

```
15: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:15]

```
16:     fun cancelTransfer(transferId: String): Boolean = false
```
> يعرّف دالّة (fun) اسمها `cancelTransfer` («إلغاء النقل») تأخذ مُعامِلاً اسمه `transferId` من النوع `String`، وتُعيد قيمة `Boolean` بقيمة افتراضية `false`. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:17]

```
18:     fun getDeviceAddressForPeer(peerID: String): String? = null
```
> يعرّف دالّة (fun) اسمها `getDeviceAddressForPeer` («جلب عنوان الجهاز للنظير») تأخذ مُعامِلاً اسمه `peerID` من النوع `String`، وتُعيد قيمة من النوع `String?` (نصّ قابل للعدم) بقيمة افتراضية `null`. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:18]

```
19: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:19]

```
20:     fun getDeviceAddressToPeerMapping(): Map<String, String> = emptyMap()
```
> يعرّف دالّة (fun) اسمها `getDeviceAddressToPeerMapping` («جلب خريطة عنوان الجهاز إلى النظير») بلا مُعامِلات، وتُعيد قيمة من النوع `Map<String, String>` (خريطة من نصّ إلى نصّ) بقيمة افتراضية `emptyMap()` (خريطة فارغة). [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:20]

```
21: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:21]

```
22:     fun getTransportDebugInfo(): String = ""
```
> يعرّف دالّة (fun) اسمها `getTransportDebugInfo` («جلب معلومات تنقيح النقل») بلا مُعامِلات، وتُعيد قيمة من النوع `String` بقيمة افتراضية `""` (نصّ فارغ). [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:22]

```
23: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshTransport.kt:23]
