# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt (الأسطر 201–211)

```
201:                         tagArray.map { it.asString }
```
> يطبّق دالّة التحويل (map) على مصفوفة الوسوم (tagArray)، فيحوّل كل عنصر (it) إلى نصّه عبر استدعاء asString، ويُنتج قائمة من النصوص. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:201]

```
202:                     } else {
```
> إغلاق نطاق الفرع السابق وبداية فرع الخلاف (else) لجملة شرطية. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:202]

```
203:                         emptyList()
```
> يستدعي الدالّة emptyList فيُعيد قائمة فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:203]

```
204:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:204]

```
205:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:205]

```
206:             } catch (e: Exception) {
```
> إغلاق نطاق المحاولة (try) وبداية كتلة الالتقاط (catch) التي تمسك استثناءً (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:206]

```
207:                 emptyList()
```
> يستدعي الدالّة emptyList فيُعيد قائمة فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:207]

```
208:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:208]

```
209:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:209]

```
210:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:210]

```
211: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRequest.kt:211]
