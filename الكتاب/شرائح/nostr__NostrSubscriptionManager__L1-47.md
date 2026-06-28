# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt (الأسطر 1–47)

```
1: package com.bitchat.android.nostr
```
> يُعرِّف هذا السطر اسم الحزمة (package) ويضبطه على `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:2]

```
3: import android.app.Application
```
> يستورد (import) الصنف `Application` من حزمة `android.app`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` من حزمة `android.util`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:4]

```
5: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف `CoroutineScope` (نطاق المهام المتزامنة) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:5]

```
6: import kotlinx.coroutines.launch
```
> يستورد الدالة `launch` (إطلاق) من حزمة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:6]

```
7: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:7]

```
8: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:8]

```
9:  * NostrSubscriptionManager
```
> تعليق: مدير اشتراكات نوستر (NostrSubscriptionManager). [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:9]

```
10:  * - Encapsulates subscription lifecycle with NostrRelayManager
```
> تعليق: يُغلِّف دورة حياة الاشتراك مع مدير المُرحِّلات (NostrRelayManager). [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:10]

```
11:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:11]

```
12: class NostrSubscriptionManager(
```
> يُعرِّف الصنف `NostrSubscriptionManager` (مدير اشتراكات نوستر) ويفتح قائمة معاملات الباني (constructor). [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:12]

```
13:     private val application: Application
```
> يُعرِّف معامل باني خاص (private) ثابت (val) باسم `application` من نوع `Application`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:13]

```
14:     private val scope: CoroutineScope
```
> يُعرِّف معامل باني خاص ثابت باسم `scope` (النطاق) من نوع `CoroutineScope`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:14]

```
15: ) {
```
> يُغلق قائمة معاملات الباني ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:15]

```
16:     companion object { private const val TAG = "NostrSubscriptionManager" }
```
> يُعرِّف كائناً مرافقاً (companion object) يحتوي ثابتاً خاصاً مُجمَّعاً (const val) باسم `TAG` (الوسم) قيمته السلسلة النصية `"NostrSubscriptionManager"`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:17]

```
18:     private val relayManager get() = NostrRelayManager.getInstance(application)
```
> يُعرِّف خاصية خاصة ثابتة باسم `relayManager` (مدير المُرحِّلات) لها مُستحصِل (getter) يُعيد نتيجة استدعاء `NostrRelayManager.getInstance(application)`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:18]

```
19: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:19]

```
20:     fun connect() = scope.launch { runCatching { relayManager.connect() }.onFailure { Log.e(TAG, "connect failed: ${it.message}") } }
```
> يُعرِّف الدالة `connect` (اتصال) التي تُعيد ناتج `scope.launch` لمهمة تستدعي `relayManager.connect()` داخل `runCatching` (التقاط الأخطاء)، وعند الفشل (`onFailure`) تستدعي `Log.e` بالوسم `TAG` والرسالة `"connect failed: ${it.message}"`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:20]

```
21:     fun disconnect() = scope.launch { runCatching { relayManager.disconnect() }.onFailure { Log.e(TAG, "disconnect failed: ${it.message}") } }
```
> يُعرِّف الدالة `disconnect` (قطع الاتصال) التي تُعيد ناتج `scope.launch` لمهمة تستدعي `relayManager.disconnect()` داخل `runCatching`، وعند الفشل تستدعي `Log.e` بالوسم `TAG` والرسالة `"disconnect failed: ${it.message}"`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:21]

```
22: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:22]

```
23:     fun subscribeGiftWraps(pubkey: String, sinceMs: Long, id: String, handler: (NostrEvent) -> Unit) {
```
> يُعرِّف الدالة `subscribeGiftWraps` (الاشتراك في أغلفة الهدايا) بمعاملات: `pubkey` (المفتاح العام) من نوع `String`، و`sinceMs` (منذ بالميلّي ثانية) من نوع `Long`، و`id` (المعرّف) من نوع `String`، و`handler` (المعالِج) دالة تأخذ `NostrEvent` وتُعيد `Unit`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:23]

```
24:         scope.launch {
```
> يستدعي `scope.launch` لإطلاق مهمة متزامنة ويفتح كتلتها. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:24]

```
25:             val filter = NostrFilter.giftWrapsFor(pubkey, sinceMs)
```
> يُعرِّف متغيراً ثابتاً باسم `filter` (المُرشِّح) ويضبطه على ناتج `NostrFilter.giftWrapsFor(pubkey, sinceMs)`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:25]

```
26:             relayManager.subscribe(filter, id, handler)
```
> يستدعي `relayManager.subscribe` بالوسائط `filter` و`id` و`handler`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:26]

```
27:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:27]

```
28:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:28]

```
29: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:29]

```
30:     /** Subscribe to geohash chat messages only (kind 20000) — low-volume, kept alive in background. */
```
> تعليق: اشترك في رسائل دردشة التجزئة الجغرافية (geohash) فقط (النوع 20000) — منخفضة الحجم، تُبقى حيّة في الخلفية. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:30]

```
31:     fun subscribeGeohashMessages(geohash: String, sinceMs: Long, limit: Int, id: String, handler: (NostrEvent) -> Unit) {
```
> يُعرِّف الدالة `subscribeGeohashMessages` (الاشتراك في رسائل التجزئة الجغرافية) بمعاملات: `geohash` (التجزئة الجغرافية) من نوع `String`، و`sinceMs` من نوع `Long`، و`limit` (الحد) من نوع `Int`، و`id` من نوع `String`، و`handler` دالة تأخذ `NostrEvent` وتُعيد `Unit`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:31]

```
32:         scope.launch {
```
> يستدعي `scope.launch` لإطلاق مهمة متزامنة ويفتح كتلتها. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:32]

```
33:             val filter = NostrFilter.geohashMessages(geohash, sinceMs, limit)
```
> يُعرِّف متغيراً ثابتاً باسم `filter` ويضبطه على ناتج `NostrFilter.geohashMessages(geohash, sinceMs, limit)`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:33]

```
34:             relayManager.subscribeForGeohash(geohash, filter, id, handler, includeDefaults = false, nRelays = 5)
```
> يستدعي `relayManager.subscribeForGeohash` بالوسائط `geohash` و`filter` و`id` و`handler`، والمعامل `includeDefaults` (تضمين الافتراضيات) بقيمة `false`، والمعامل `nRelays` (عدد المُرحِّلات) بقيمة `5`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:34]

```
35:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:35]

```
36:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:36]

```
37: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:37]

```
38:     /** Subscribe to geohash presence heartbeats only (kind 20001) — high-volume, paused in background. */
```
> تعليق: اشترك في نبضات حضور التجزئة الجغرافية (presence heartbeats) فقط (النوع 20001) — مرتفعة الحجم، تُوقَف مؤقتاً في الخلفية. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:38]

```
39:     fun subscribeGeohashPresence(geohash: String, sinceMs: Long, limit: Int, id: String, handler: (NostrEvent) -> Unit) {
```
> يُعرِّف الدالة `subscribeGeohashPresence` (الاشتراك في حضور التجزئة الجغرافية) بمعاملات: `geohash` من نوع `String`، و`sinceMs` من نوع `Long`، و`limit` من نوع `Int`، و`id` من نوع `String`، و`handler` دالة تأخذ `NostrEvent` وتُعيد `Unit`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:39]

```
40:         scope.launch {
```
> يستدعي `scope.launch` لإطلاق مهمة متزامنة ويفتح كتلتها. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:40]

```
41:             val filter = NostrFilter.geohashPresence(geohash, sinceMs, limit)
```
> يُعرِّف متغيراً ثابتاً باسم `filter` ويضبطه على ناتج `NostrFilter.geohashPresence(geohash, sinceMs, limit)`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:41]

```
42:             relayManager.subscribeForGeohash(geohash, filter, id, handler, includeDefaults = false, nRelays = 5)
```
> يستدعي `relayManager.subscribeForGeohash` بالوسائط `geohash` و`filter` و`id` و`handler`، والمعامل `includeDefaults` بقيمة `false`، والمعامل `nRelays` بقيمة `5`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:42]

```
43:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:43]

```
44:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:44]

```
45: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:45]

```
46:     fun unsubscribe(id: String) { scope.launch { runCatching { relayManager.unsubscribe(id) } } }
```
> يُعرِّف الدالة `unsubscribe` (إلغاء الاشتراك) بمعامل `id` من نوع `String`، تُطلق `scope.launch` لمهمة تستدعي `relayManager.unsubscribe(id)` داخل `runCatching`. [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:46]

```
47: }
```
> إغلاق نطاق (نهاية جسم الصنف). [app/src/main/java/com/bitchat/android/nostr/NostrSubscriptionManager.kt:47]
