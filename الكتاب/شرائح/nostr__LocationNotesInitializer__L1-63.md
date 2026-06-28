# شريحة — app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt (الأسطر 1–63)

```
1: package com.bitchat.android.nostr
```
> يُعلِن انتماء الملف إلى الحزمة (package) باسم `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من `android.content`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` من `android.util`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:5]

```
6: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:6]

```
7:  * Initializer for LocationNotesManager with all dependencies
```
> تعليق: مُهيِّئ لـ `LocationNotesManager` مع كل الاعتماديات. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:7]

```
8:  * Extracts initialization logic from MainActivity for better separation of concerns
```
> تعليق: يستخرج منطق التهيئة من `MainActivity` لأجل فصل أفضل للاهتمامات. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:8]

```
9:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:9]

```
10: object LocationNotesInitializer {
```
> يُعرِّف كائناً مفرداً (object) باسم `LocationNotesInitializer` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:10]

```
11:     
```
> سطر فارغ (يحوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:11]

```
12:     private const val TAG = "LocationNotesInitializer"
```
> يُعرِّف ثابتاً خاصاً (private const) باسم `TAG` ويضبط قيمته إلى النص `"LocationNotesInitializer"`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:12]

```
13:     
```
> سطر فارغ (يحوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:13]

```
14:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:14]

```
15:      * Initialize LocationNotesManager with all required dependencies
```
> تعليق: هيِّئ `LocationNotesManager` مع كل الاعتماديات المطلوبة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:15]

```
16:      * 
```
> تعليق: سطر تعليق فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:16]

```
17:      * @param context Application context
```
> تعليق: المعامل `context` هو سياق التطبيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:17]

```
18:      * @return true if initialization succeeded, false otherwise
```
> تعليق: يُعيد `true` إذا نجحت التهيئة، و`false` خلاف ذلك. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:18]

```
19:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:19]

```
20:     fun initialize(context: Context): Boolean {
```
> يُعرِّف دالة (function) باسم `initialize` تأخذ معاملاً `context` من نوع `Context` وتُعيد قيمة من نوع `Boolean`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:20]

```
21:         return try {
```
> يُعيد نتيجة كتلة `try`، ويفتح نطاق كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:21]

```
22:             LocationNotesManager.getInstance().initialize(
```
> يستدعي `getInstance()` على `LocationNotesManager`، ثم يستدعي عليه `initialize(` ويفتح قائمة وُسطائها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:22]

```
23:                 relayManager = { NostrRelayManager.getInstance(context) },
```
> يمرّر الوسيط المُسمّى `relayManager` كدالة لمدا (lambda) تُعيد ناتج `NostrRelayManager.getInstance(context)`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:23]

```
24:                 subscribe = { filter, id, handler ->
```
> يمرّر الوسيط المُسمّى `subscribe` كدالة لمدا تستقبل ثلاثة وُسطاء: `filter` و`id` و`handler`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:24]

```
25:                     // CRITICAL FIX: Extract geohash properly from filter using getGeohash() method
```
> تعليق: إصلاح حرج: استخرج الـ geohash بشكل صحيح من الـ filter باستخدام طريقة `getGeohash()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:25]

```
26:                     val geohashFromFilter = filter.getGeohash() ?: run {
```
> يُعرِّف متغيراً ثابتاً (val) باسم `geohashFromFilter` ويضبطه إلى ناتج `filter.getGeohash()`، وعند كونه `null` يُشغِّل كتلة `run` ويفتحها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:26]

```
27:                         Log.e(TAG, "❌ Cannot extract geohash from filter for location notes")
```
> يستدعي `Log.e` مع الوسم `TAG` والرسالة `"❌ Cannot extract geohash from filter for location notes"`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:27]

```
28:                         return@initialize id // Return subscription ID even on error
```
> يُرجِع من الدالة `initialize` القيمة `id`، مع تعليق: أعِد مُعرّف الاشتراك حتى عند الخطأ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:28]

```
29:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:29]

```
30:                     
```
> سطر فارغ (يحوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:30]

```
31:                     Log.d(TAG, "📍 Location Notes subscribing to geohash: $geohashFromFilter")
```
> يستدعي `Log.d` مع الوسم `TAG` والرسالة `"📍 Location Notes subscribing to geohash: $geohashFromFilter"` مُضمِّناً قيمة `geohashFromFilter`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:31]

```
32:                     
```
> سطر فارغ (يحوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:32]

```
33:                     NostrRelayManager.getInstance(context).subscribeForGeohash(
```
> يستدعي `getInstance(context)` على `NostrRelayManager`، ثم يستدعي عليه `subscribeForGeohash(` ويفتح قائمة وُسطائها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:33]

```
34:                         geohash = geohashFromFilter,
```
> يمرّر الوسيط المُسمّى `geohash` بقيمة `geohashFromFilter`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:34]

```
35:                         filter = filter,
```
> يمرّر الوسيط المُسمّى `filter` بقيمة `filter`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:35]

```
36:                         id = id,
```
> يمرّر الوسيط المُسمّى `id` بقيمة `id`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:36]

```
37:                         handler = handler,
```
> يمرّر الوسيط المُسمّى `handler` بقيمة `handler`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:37]

```
38:                         includeDefaults = true,
```
> يمرّر الوسيط المُسمّى `includeDefaults` بقيمة `true`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:38]

```
39:                         nRelays = 5
```
> يمرّر الوسيط المُسمّى `nRelays` بقيمة `5`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:39]

```
40:                     )
```
> إغلاق قائمة وُسطاء استدعاء `subscribeForGeohash`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:40]

```
41:                 },
```
> إغلاق نطاق دالة لمدا `subscribe` مُتبوعاً بفاصلة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:41]

```
42:                 unsubscribe = { id ->
```
> يمرّر الوسيط المُسمّى `unsubscribe` كدالة لمدا تستقبل وسيطاً `id`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:42]

```
43:                     NostrRelayManager.getInstance(context).unsubscribe(id)
```
> يستدعي `getInstance(context)` على `NostrRelayManager`، ثم يستدعي عليه `unsubscribe(id)`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:43]

```
44:                 },
```
> إغلاق نطاق دالة لمدا `unsubscribe` مُتبوعاً بفاصلة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:44]

```
45:                 sendEvent = { event, relayUrls ->
```
> يمرّر الوسيط المُسمّى `sendEvent` كدالة لمدا تستقبل وسيطين: `event` و`relayUrls`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:45]

```
46:                     if (relayUrls != null) {
```
> يبدأ شرط `if` يختبر كون `relayUrls` لا يساوي `null`، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:46]

```
47:                         NostrRelayManager.getInstance(context).sendEvent(event, relayUrls)
```
> يستدعي `getInstance(context)` على `NostrRelayManager`، ثم يستدعي عليه `sendEvent(event, relayUrls)`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:47]

```
48:                     } else {
```
> إغلاق كتلة `if` وفتح كتلة `else`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:48]

```
49:                         NostrRelayManager.getInstance(context).sendEvent(event)
```
> يستدعي `getInstance(context)` على `NostrRelayManager`، ثم يستدعي عليه `sendEvent(event)`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:49]

```
50:                     }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:50]

```
51:                 },
```
> إغلاق نطاق دالة لمدا `sendEvent` مُتبوعاً بفاصلة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:51]

```
52:                 deriveIdentity = { geohash ->
```
> يمرّر الوسيط المُسمّى `deriveIdentity` كدالة لمدا تستقبل وسيطاً `geohash`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:52]

```
53:                     NostrIdentityBridge.deriveIdentity(geohash, context)
```
> يستدعي `deriveIdentity(geohash, context)` على `NostrIdentityBridge`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:53]

```
54:                 }
```
> إغلاق نطاق دالة لمدا `deriveIdentity`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:54]

```
55:             )
```
> إغلاق قائمة وُسطاء استدعاء `initialize`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:55]

```
56:             Log.d(TAG, "✅ Location Notes Manager initialized")
```
> يستدعي `Log.d` مع الوسم `TAG` والرسالة `"✅ Location Notes Manager initialized"`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:56]

```
57:             true
```
> يُقيِّم القيمة `true` كنتيجة كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:57]

```
58:         } catch (e: Exception) {
```
> إغلاق كتلة `try` وفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:58]

```
59:             Log.e(TAG, "❌ Failed to initialize Location Notes Manager: ${e.message}", e)
```
> يستدعي `Log.e` مع الوسم `TAG` والرسالة `"❌ Failed to initialize Location Notes Manager: ${e.message}"` مُضمِّناً `e.message` والاستثناء `e`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:59]

```
60:             false
```
> يُقيِّم القيمة `false` كنتيجة كتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:60]

```
61:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:61]

```
62:     }
```
> إغلاق نطاق دالة `initialize`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:62]

```
63: }
```
> إغلاق نطاق الكائن المفرد `LocationNotesInitializer`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesInitializer.kt:63]
