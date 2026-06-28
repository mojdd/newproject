# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt (الأسطر 201–231)

```
201:         } catch (e: Exception) {
```
> يُغلق كتلة المحاولة ويبدأ كتلة الالتقاط (catch) التي تمسك أي استثناء (Exception) وتسميه (e). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:201]

```
202:             false
```
> يُعيد القيمة المنطقية «خطأ» (false) كنتيجة لكتلة الالتقاط. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:202]

```
203:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:203]

```
204:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:204]

```
205: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:205]

```
206: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:206]

```
207: /**
```
> تعليق: بداية تعليق توثيقي (بنمط KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:207]

```
208:  * Nostr event kinds
```
> تعليق: أنواع أحداث نوستر (Nostr event kinds). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:208]

```
209:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:209]

```
210: object NostrKind {
```
> يُعرِّف كائناً مفرداً (object) باسم «نوع نوستر» (NostrKind) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:210]

```
211:     const val METADATA = 0
```
> يُعرِّف ثابتاً (const) باسم «البيانات الوصفية» (METADATA) وقيمته العدد 0. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:211]

```
212:     const val TEXT_NOTE = 1
```
> يُعرِّف ثابتاً باسم «الملاحظة النصية» (TEXT_NOTE) وقيمته العدد 1. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:212]

```
213:     const val DIRECT_MESSAGE = 14     // NIP-17 direct message (unsigned)
```
> يُعرِّف ثابتاً باسم «الرسالة المباشرة» (DIRECT_MESSAGE) وقيمته العدد 14، مع تعليق: رسالة مباشرة بنمط NIP-17 (غير موقّعة). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:213]

```
214:     const val FILE_MESSAGE = 15       // NIP-17 file message (unsigned)
```
> يُعرِّف ثابتاً باسم «رسالة الملف» (FILE_MESSAGE) وقيمته العدد 15، مع تعليق: رسالة ملف بنمط NIP-17 (غير موقّعة). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:214]

```
215:     const val SEAL = 13              // NIP-17 sealed event
```
> يُعرِّف ثابتاً باسم «الختم» (SEAL) وقيمته العدد 13، مع تعليق: حدث مختوم بنمط NIP-17. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:215]

```
216:     const val GIFT_WRAP = 1059       // NIP-17 gift wrap
```
> يُعرِّف ثابتاً باسم «غلاف الهدية» (GIFT_WRAP) وقيمته العدد 1059، مع تعليق: غلاف هدية بنمط NIP-17. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:216]

```
217:     const val EPHEMERAL_EVENT = 20000 // For geohash channels
```
> يُعرِّف ثابتاً باسم «الحدث العابر» (EPHEMERAL_EVENT) وقيمته العدد 20000، مع تعليق: لقنوات التجزئة الجغرافية (geohash channels). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:217]

```
218:     const val GEOHASH_PRESENCE = 20001 // For geohash presence heartbeat
```
> يُعرِّف ثابتاً باسم «حضور التجزئة الجغرافية» (GEOHASH_PRESENCE) وقيمته العدد 20001، مع تعليق: لنبضة حضور التجزئة الجغرافية (geohash presence heartbeat). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:218]

```
219: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:219]

```
220: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:220]

```
221: /**
```
> تعليق: بداية تعليق توثيقي (بنمط KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:221]

```
222:  * Extension functions for hex encoding/decoding
```
> تعليق: دوال امتداد (Extension functions) لترميز/فك ترميز الست عشري (hex). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:222]

```
223:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:223]

```
224: fun String.hexToByteArray(): ByteArray {
```
> يُعرِّف دالة امتداد على النوع نص (String) باسم «الست عشري إلى مصفوفة بايت» (hexToByteArray) تُعيد مصفوفة بايت (ByteArray) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:224]

```
225:     check(length % 2 == 0) { "Must have an even length" }
```
> يستدعي الدالة (check) للتحقق من أن باقي قسمة الطول (length) على 2 يساوي صفر، وإلا يطرح خطأً برسالة: «يجب أن يكون الطول زوجياً» (Must have an even length). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:225]

```
226:     return chunked(2)
```
> يُعيد نتيجة استدعاء (chunked) بالقيمة 2 الذي يقسم النص إلى قطع طول كل منها حرفان. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:226]

```
227:         .map { it.toInt(16).toByte() }
```
> يطبّق (map) على كل قطعة فيحوّلها إلى عدد صحيح (toInt) بالأساس 16 ثم إلى بايت (toByte). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:227]

```
228:         .toByteArray()
```
> يحوّل الناتج إلى مصفوفة بايت باستدعاء (toByteArray). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:228]

```
229: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:229]

```
230: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:230]

```
231: fun ByteArray.toHexString(): String = joinToString("") { "%02x".format(it) }
```
> يُعرِّف دالة امتداد على النوع مصفوفة بايت (ByteArray) باسم «إلى نص ست عشري» (toHexString) تُعيد نصاً (String) عبر تعبير مساوٍ يستدعي (joinToString) بفاصل نصي فارغ، ويُنسّق كل بايت بالصيغة "%02x" باستدعاء (format). [app/src/main/java/com/bitchat/android/nostr/NostrEvent.kt:231]
