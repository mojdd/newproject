# شريحة — app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt (الأسطر 201–217)

```
201:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:201]

```
202:     // Packet operations
```
> تعليق: عمليات الحزمة (Packet operations). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:202]

```
203:     fun broadcastPacket(routed: RoutedPacket)
```
> تصريح دالة بثّ الحزمة (broadcastPacket) تأخذ مُعاملاً اسمه «routed» من نوع الحزمة المُوجَّهة (RoutedPacket) ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:203]

```
204:     fun sendToPeer(peerID: String, routed: RoutedPacket): Boolean
```
> تصريح دالة إرسال إلى نظير (sendToPeer) تأخذ مُعاملاً اسمه «peerID» من نوع سلسلة نصية (String) ومُعاملاً اسمه «routed» من نوع الحزمة المُوجَّهة (RoutedPacket)، وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:204]

```
205: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:205]

```
206: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:206]

```
207: private fun hexStringToPeerBytes(hex: String): ByteArray {
```
> تصريح دالة خاصة (private) اسمها تحويل سلسلة ست عشرية إلى بايتات نظير (hexStringToPeerBytes) تأخذ مُعاملاً اسمه «hex» من نوع سلسلة نصية (String)، وتُعيد مصفوفة بايتات (ByteArray)، ويبدأ جسمها. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:207]

```
208:     val result = ByteArray(8)
```
> تعريف متغيّر ثابت اسمه «النتيجة» (result) يُضبَط بمصفوفة بايتات (ByteArray) طولها 8. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:208]

```
209:     var idx = 0
```
> تعريف متغيّر متغيّر القيمة اسمه «الفهرس» (idx) يُضبَط بالقيمة 0. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:209]

```
210:     var out = 0
```
> تعريف متغيّر متغيّر القيمة اسمه «الخَرْج» (out) يُضبَط بالقيمة 0. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:210]

```
211:     while (idx + 1 < hex.length && out < 8) {
```
> بدء حلقة «طالما» (while) شرطها أنّ مجموع الفهرس (idx) زائد 1 أصغر من طول السلسلة (hex.length) وأنّ الخَرْج (out) أصغر من 8. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:211]

```
212:         val b = hex.substring(idx, idx + 2).toIntOrNull(16)?.toByte() ?: 0
```
> تعريف متغيّر ثابت اسمه «b» يُضبَط بنتيجة أخذ مقطع فرعي من السلسلة (substring) من الفهرس (idx) إلى الفهرس زائد 2، ثم تحويله إلى عدد صحيح بالأساس 16 (toIntOrNull(16)) ثم إلى بايت (toByte)، وإن كانت النتيجة فارغة (null) فالقيمة 0. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:212]

```
213:         result[out++] = b
```
> إسناد قيمة المتغيّر «b» إلى عنصر مصفوفة النتيجة (result) عند الموضع الخَرْج (out)، ثم زيادة الخَرْج بمقدار 1 بعد الاستعمال. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:213]

```
214:         idx += 2
```
> زيادة قيمة الفهرس (idx) بمقدار 2. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:214]

```
215:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:215]

```
216:     return result
```
> إعادة قيمة المتغيّر «النتيجة» (result). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:216]

```
217: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:217]
