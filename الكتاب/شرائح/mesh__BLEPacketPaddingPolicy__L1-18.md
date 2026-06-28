# شريحة — app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt (الأسطر 1–18)

```
1: package com.bitchat.android.mesh
```
> يُعلِن أن هذا الملف ينتمي إلى الحُزمة (package) باسم `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:2]

```
3: import com.bitchat.android.protocol.MessageType
```
> يستورد (import) النوع `MessageType` من الحُزمة `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:4]

```
5: /**
```
> تعليق: بداية تعليق توثيق (مُعلِّق وثائقي) يبدأ بالرمز `/**`. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:5]

```
6:  * iOS-compatible BLE padding policy.
```
> تعليق: سياسة حشو (padding) خاصة بالبلوتوث منخفض الطاقة (BLE) متوافقة مع نظام iOS. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:6]

```
7:  *
```
> تعليق: سطر تعليق فارغ يحتوي فقط على نجمة. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:7]

```
8:  * Keep this aligned with iOS BLEOutboundPacketPolicy.padsBLEFrame(for:):
```
> تعليق: حافِظ على مطابقة هذا مع دالة `padsBLEFrame(for:)` في `BLEOutboundPacketPolicy` على نظام iOS. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:8]

```
9:  * only Noise frames are padded over BLE.
```
> تعليق: فقط إطارات (frames) بروتوكول نويز (Noise) تُحشى عند الإرسال عبر BLE. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:9]

```
10:  */
```
> تعليق: نهاية تعليق التوثيق بالرمز `*/`. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:10]

```
11: object BLEPacketPaddingPolicy {
```
> يُعرِّف كائناً مفرداً (object) باسم `BLEPacketPaddingPolicy` (سياسة حشو رزمة BLE) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:11]

```
12:     fun shouldPadForBLE(type: UByte): Boolean {
```
> يُعرِّف دالة (fun) باسم `shouldPadForBLE` (هل يجب الحشو لأجل BLE) تأخذ مُعامِلاً باسم `type` من نوع `UByte` (بايت غير مُوقَّع) وتُعيد قيمة من نوع `Boolean` (منطقية)، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:12]

```
13:         return when (MessageType.fromValue(type)) {
```
> يُعيد (return) نتيجة تعبير `when` (عندما) الذي يُفرِّع على ناتج استدعاء `MessageType.fromValue(type)` الذي يحوّل القيمة `type` إلى نوع رسالة، ويفتح كتلة الـ when. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:13]

```
14:             MessageType.NOISE_ENCRYPTED, MessageType.NOISE_HANDSHAKE -> true
```
> فرع يطابق القيمتين `MessageType.NOISE_ENCRYPTED` (نويز مُشفَّر) أو `MessageType.NOISE_HANDSHAKE` (مصافحة نويز) ويُعيد لهما القيمة `true` (صحيح). [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:14]

```
15:             else -> false
```
> الفرع `else` (وإلّا) لأي قيمة أخرى يُعيد القيمة `false` (خطأ). [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:15]

```
16:         }
```
> إغلاق نطاق كتلة الـ when. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:16]

```
17:     }
```
> إغلاق نطاق جسم الدالة `shouldPadForBLE`. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:17]

```
18: }
```
> إغلاق نطاق الكائن `BLEPacketPaddingPolicy`. [app/src/main/java/com/bitchat/android/mesh/BLEPacketPaddingPolicy.kt:18]
