# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt (الأسطر 201–212)

```
201:                 .replace("_", "/")
```
> يُستدعى تابع الاستبدال (replace) على السلسلة الناتجة من السطر السابق، فيبدّل كل حرف شُرطة سفلية «_» بحرف شُرطة مائلة «/». [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:201]

```
202:                 .let { str ->
```
> يُستدعى تابع التطبيق (let) على السلسلة الناتجة، ويُسمّى المُدخَل داخل الكتلة بالاسم «str»، ويبدأ جسم الكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:202]

```
203:                     val padding = (4 - str.length % 4) % 4
```
> يُعرَّف متغيّر ثابت (val) باسم «حشو» (padding) وتُسنَد له قيمة الحساب: «(4 ناقص باقي قسمة طول «str» على 4) ثم باقي قسمة الناتج على 4». [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:203]

```
204:                     str + "=".repeat(padding)
```
> تعبير يُعيد دمج السلسلة «str» مع تكرار حرف علامة المساواة «=» عددًا من المرّات يساوي قيمة «padding» (repeat)، وهو القيمة المُعادة من كتلة «let». [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:204]

```
205:                 }
```
> إغلاق نطاق (إغلاق كتلة «let»). [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:205]

```
206:             android.util.Base64.decode(padded, android.util.Base64.DEFAULT)
```
> يُستدعى تابع فكّ الترميز (decode) من الصنف «android.util.Base64» مع المُدخَلين: السلسلة «padded» والعلم «android.util.Base64.DEFAULT»، ويكون ناتجه آخر تعبير في كتلة «try». [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:206]

```
207:         } catch (e: Exception) {
```
> إغلاق كتلة «try» وبداية كتلة الالتقاط (catch) التي تلتقط استثناءً من النوع «Exception» وتسمّيه «e». [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:207]

```
208:             Log.e(TAG, "Failed to decode base64url: ${e.message}")
```
> يُستدعى تابع تسجيل الخطأ (Log.e) بالوسم «TAG» وبنص الرسالة «Failed to decode base64url: » متبوعًا بقيمة «e.message» المُدرَجة داخل النص. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:208]

```
209:             null
```
> تعبير يُعيد القيمة العدمية «null»، وهو آخر تعبير في كتلة الالتقاط. [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:209]

```
210:         }
```
> إغلاق نطاق (إغلاق كتلة «catch»). [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:210]

```
211:     }
```
> إغلاق نطاق (إغلاق جسم التابع «base64URLDecode»). [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:211]

```
212: }
```
> إغلاق نطاق (إغلاق جسم الصنف). [app/src/main/java/com/bitchat/android/nostr/NostrDirectMessageHandler.kt:212]
