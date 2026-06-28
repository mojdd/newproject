# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt (الأسطر 201–234)

```
201:      */
```
> إغلاق تعليق توثيقي (نهاية كتلة تعليق على شكل `*/`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:201]

```
202:     private fun base64URLEncode(data: ByteArray): String {
```
> تعريف دالة خاصة (private) باسم «ترميز قاعدة-٦٤ على نمط الرابط» (base64URLEncode) تأخذ وسيطاً باسم `data` من نوع مصفوفة بايتات (ByteArray) وتعيد نصاً (String). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:202]

```
203:         val b64 = Base64.encodeToString(data, Base64.NO_WRAP)
```
> تعريف ثابت محلي باسم `b64` يُسنَد إليه ناتج استدعاء `Base64.encodeToString` على `data` مع الخيار `Base64.NO_WRAP` (بلا التفاف أسطر). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:203]

```
204:         return b64
```
> يعيد قيمة `b64` بعد تطبيق سلسلة الاستبدالات التالية عليها. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:204]

```
205:             .replace("+", "-")
```
> يستدعي `replace` لاستبدال كل علامة جمع `+` بشَرطة `-`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:205]

```
206:             .replace("/", "_")
```
> يستدعي `replace` لاستبدال كل شَرطة مائلة `/` بشَرطة سفلية `_`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:206]

```
207:             .replace("=", "")
```
> يستدعي `replace` لاستبدال كل علامة يساوي `=` بنص فارغ (حذفها). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:207]

```
208:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:208]

```
209:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:209]

```
210:     /**
```
> فتح تعليق توثيقي (بداية كتلة تعليق على شكل `/**`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:210]

```
211:      * Convert hex string to byte array
```
> تعليق: حوّل نصاً ست عشرياً (hex) إلى مصفوفة بايتات. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:211]

```
212:      */
```
> إغلاق تعليق توثيقي (نهاية كتلة تعليق على شكل `*/`). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:212]

```
213:     private fun hexStringToByteArray(hexString: String): ByteArray {
```
> تعريف دالة خاصة (private) باسم «تحويل النص الست عشري إلى مصفوفة بايتات» (hexStringToByteArray) تأخذ وسيطاً باسم `hexString` من نوع نص (String) وتعيد مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:213]

```
214:         if (hexString.length % 2 != 0) {
```
> شرط (if): إذا كان باقي قسمة طول `hexString` على ٢ لا يساوي صفراً (أي الطول فردي). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:214]

```
215:             return ByteArray(8) // Return 8-byte array filled with zeros
```
> يعيد مصفوفة بايتات `ByteArray` بطول ٨، يتبعه تعليق: أعِد مصفوفة من ٨ بايتات مملوءة بالأصفار. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:215]

```
216:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:216]

```
217:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:217]

```
218:         val result = ByteArray(8) { 0 } // Exactly 8 bytes like iOS
```
> تعريف ثابت محلي باسم `result` يُسنَد إليه مصفوفة بايتات `ByteArray` بطول ٨ مهيّأة كل عنصر فيها بالقيمة `0`، يتبعه تعليق: بالضبط ٨ بايتات مثل iOS. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:218]

```
219:         var tempID = hexString
```
> تعريف متغير محلي باسم `tempID` يُسنَد إليه قيمة `hexString`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:219]

```
220:         var index = 0
```
> تعريف متغير محلي باسم `index` يُسنَد إليه القيمة `0`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:220]

```
221:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:221]

```
222:         while (tempID.length >= 2 && index < 8) {
```
> حلقة (while): تستمر ما دام طول `tempID` أكبر من أو يساوي ٢ و`index` أصغر من ٨. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:222]

```
223:             val hexByte = tempID.substring(0, 2)
```
> تعريف ثابت محلي باسم `hexByte` يُسنَد إليه المقطع الفرعي من `tempID` من الموضع ٠ حتى الموضع ٢ (أول حرفين). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:223]

```
224:             val byte = hexByte.toIntOrNull(16)?.toByte()
```
> تعريف ثابت محلي باسم `byte` يُسنَد إليه ناتج تحويل `hexByte` إلى عدد صحيح بالأساس ١٦ عبر `toIntOrNull(16)` (يعيد null عند الفشل) ثم تحويله إلى بايت عبر `toByte` بشرط عدم كونه null. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:224]

```
225:             if (byte != null) {
```
> شرط (if): إذا كان `byte` لا يساوي null. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:225]

```
226:                 result[index] = byte
```
> يُسنِد قيمة `byte` إلى عنصر `result` عند الموضع `index`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:226]

```
227:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:227]

```
228:             tempID = tempID.substring(2)
```
> يُسنِد إلى `tempID` المقطع الفرعي من نفسه ابتداءً من الموضع ٢ (حذف أول حرفين). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:228]

```
229:             index++
```
> يزيد `index` بمقدار واحد. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:229]

```
230:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:230]

```
231:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:231]

```
232:         return result
```
> يعيد قيمة `result`. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:232]

```
233:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:233]

```
234:}
```
> إغلاق نطاق (نهاية الصنف/الكائن). [app/src/main/java/com/bitchat/android/nostr/NostrEmbeddedBitChat.kt:234]
