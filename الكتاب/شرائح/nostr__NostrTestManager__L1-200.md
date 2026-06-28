# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.nostr
```
> يُعرّف الحزمة (package) التي ينتمي إليها الملف باسم `com.bitchat.android.nostr`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من حزمة `android.content`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` من حزمة `android.util`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:4]

```
5: import kotlinx.coroutines.*
```
> يستورد كل العناصر من حزمة الكوروتينات (coroutines) `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:6]

```
7: /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:7]

```
8:  * Test manager for Nostr functionality
```
> تعليق: مدير اختبار لوظيفة نوستر (Nostr). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:8]

```
9:  * Use this to verify the Nostr client works correctly
```
> تعليق: استعمل هذا للتحقق من أن عميل نوستر يعمل بشكل صحيح. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:9]

```
10:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:10]

```
11: class NostrTestManager(private val context: Context) {
```
> يُعرّف الصنف (class) `NostrTestManager` بمُنشئ يأخذ مُعاملاً خاصاً للقراءة فقط `context` من نوع `Context`، ويفتح نطاق الصنف. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:11]

```
12:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:12]

```
13:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:13]

```
14:         private const val TAG = "NostrTestManager"
```
> يُعرّف ثابتاً خاصاً `TAG` بقيمة نصية ثابتة `"NostrTestManager"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:14]

```
15:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:15]

```
16:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:16]

```
17:     private val testScope = CoroutineScope(Dispatchers.Main + SupervisorJob())
```
> يُعرّف خاصية خاصة للقراءة فقط `testScope` تُسند نطاق كوروتين (CoroutineScope) مُنشأ بسياق هو `Dispatchers.Main` مجموعاً مع `SupervisorJob()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:17]

```
18:     private lateinit var nostrClient: NostrClient
```
> يُعرّف خاصية خاصة متغيرة مؤجّلة التهيئة (lateinit) باسم `nostrClient` من نوع `NostrClient`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:18]

```
19:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:19]

```
20:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:20]

```
21:      * Run comprehensive Nostr tests
```
> تعليق: شغّل اختبارات نوستر الشاملة. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:21]

```
22:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:22]

```
23:     fun runTests() {
```
> يُعرّف الدالة `runTests` بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:23]

```
24:         Log.i(TAG, "🧪 Starting Nostr functionality tests...")
```
> يستدعي `Log.i` بالوسم `TAG` ورسالة نصية `"🧪 Starting Nostr functionality tests..."`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:24]

```
25:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:25]

```
26:         testScope.launch {
```
> يستدعي `launch` على `testScope` لإطلاق كوروتين ويفتح كتلتها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:26]

```
27:             try {
```
> يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:27]

```
28:                 // Test 1: Initialize client
```
> تعليق: الاختبار ١: تهيئة العميل. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:28]

```
29:                 testClientInitialization()
```
> يستدعي الدالة `testClientInitialization()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:29]

```
30:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:30]

```
31:                 // Test 2: Test identity generation and storage
```
> تعليق: الاختبار ٢: اختبار توليد الهوية وتخزينها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:31]

```
32:                 testIdentityManagement()
```
> يستدعي الدالة `testIdentityManagement()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:32]

```
33:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:33]

```
34:                 // Test 3: Test relay connections
```
> تعليق: الاختبار ٣: اختبار اتصالات المُرحّلات (relay). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:34]

```
35:                 testRelayConnections()
```
> يستدعي الدالة `testRelayConnections()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:35]

```
36:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:36]

```
37:                 // Test 4: Test cryptography
```
> تعليق: الاختبار ٤: اختبار التعمية (cryptography). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:37]

```
38:                 testCryptography()
```
> يستدعي الدالة `testCryptography()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:38]

```
39:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:39]

```
40:                 // Test 5: Test Bech32 encoding
```
> تعليق: الاختبار ٥: اختبار ترميز Bech32. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:40]

```
41:                 testBech32()
```
> يستدعي الدالة `testBech32()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:41]

```
42:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:42]

```
43:                 // Test 6: Test message subscription (without sending)
```
> تعليق: الاختبار ٦: اختبار الاشتراك (subscription) في الرسائل (بدون إرسال). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:43]

```
44:                 testMessageSubscription()
```
> يستدعي الدالة `testMessageSubscription()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:44]

```
45:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:45]

```
46:                 Log.i(TAG, "✅ All Nostr tests completed successfully!")
```
> يستدعي `Log.i` بالوسم `TAG` ورسالة نصية `"✅ All Nostr tests completed successfully!"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:46]

```
47:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:47]

```
48:             } catch (e: Exception) {
```
> يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:48]

```
49:                 Log.e(TAG, "❌ Nostr tests failed: ${e.message}", e)
```
> يستدعي `Log.e` بالوسم `TAG` ورسالة نصية `"❌ Nostr tests failed: ${e.message}"` المُضمّنة لرسالة الاستثناء، مع تمرير الاستثناء `e`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:49]

```
50:             }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:50]

```
51:         }
```
> إغلاق نطاق كتلة `launch`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:51]

```
52:     }
```
> إغلاق نطاق دالة `runTests`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:52]

```
53:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:53]

```
54:     private suspend fun testClientInitialization() {
```
> يُعرّف الدالة المُعلّقة (suspend) الخاصة `testClientInitialization` بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:54]

```
55:         Log.d(TAG, "Testing client initialization...")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"Testing client initialization..."`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:55]

```
56:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:56]

```
57:         nostrClient = NostrClient.getInstance(context)
```
> يُسند إلى `nostrClient` نتيجة استدعاء `NostrClient.getInstance(context)`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:57]

```
58:         nostrClient.initialize()
```
> يستدعي الدالة `initialize()` على `nostrClient`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:58]

```
59:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:59]

```
60:         // Wait for initialization
```
> تعليق: انتظر التهيئة. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:60]

```
61:         delay(2000)
```
> يستدعي `delay` بقيمة `2000` (تأخير بالميلي ثانية). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:61]

```
62:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:62]

```
63:         val isInitialized = nostrClient.isInitialized.value ?: false
```
> يُعرّف خاصية محلية للقراءة فقط `isInitialized` تُسند قيمة `nostrClient.isInitialized.value`، وفي حال كانت فارغة (null) تُسند `false`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:63]

```
64:         require(isInitialized) { "Client failed to initialize" }
```
> يستدعي `require` على `isInitialized`، وعند الفشل يرمي بالرسالة `"Client failed to initialize"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:64]

```
65:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:65]

```
66:         Log.d(TAG, "✅ Client initialization successful")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"✅ Client initialization successful"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:66]

```
67:     }
```
> إغلاق نطاق دالة `testClientInitialization`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:67]

```
68:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:68]

```
69:     private suspend fun testIdentityManagement() {
```
> يُعرّف الدالة المُعلّقة الخاصة `testIdentityManagement` بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:69]

```
70:         Log.d(TAG, "Testing identity management...")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"Testing identity management..."`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:70]

```
71:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:71]

```
72:         // Test current identity
```
> تعليق: اختبر الهوية الحالية. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:72]

```
73:         val identity = nostrClient.getCurrentIdentity()
```
> يُعرّف خاصية محلية للقراءة فقط `identity` تُسند نتيجة `nostrClient.getCurrentIdentity()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:73]

```
74:         requireNotNull(identity) { "No current identity" }
```
> يستدعي `requireNotNull` على `identity`، وعند كونها فارغة يرمي بالرسالة `"No current identity"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:74]

```
75:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:75]

```
76:         Log.d(TAG, "Current identity npub: ${identity.getShortNpub()}")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"Current identity npub: ${identity.getShortNpub()}"` المُضمّنة لنتيجة `identity.getShortNpub()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:76]

```
77:         require(identity.npub.startsWith("npub1")) { "Invalid npub format" }
```
> يستدعي `require` على شرط أن `identity.npub` يبدأ بـ `"npub1"`، وعند الفشل يرمي بالرسالة `"Invalid npub format"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:77]

```
78:         require(identity.publicKeyHex.length == 64) { "Invalid public key length" }
```
> يستدعي `require` على شرط أن طول `identity.publicKeyHex` يساوي `64`، وعند الفشل يرمي بالرسالة `"Invalid public key length"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:78]

```
79:         require(identity.privateKeyHex.length == 64) { "Invalid private key length" }
```
> يستدعي `require` على شرط أن طول `identity.privateKeyHex` يساوي `64`، وعند الفشل يرمي بالرسالة `"Invalid private key length"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:79]

```
80:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:80]

```
81:         // Test geohash identity derivation
```
> تعليق: اختبر اشتقاق هوية مُعرّف الموقع المُجزّأ (geohash). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:81]

```
82:         val geohashIdentity = NostrIdentityBridge.deriveIdentity("u4pruydq", context)
```
> يُعرّف خاصية محلية للقراءة فقط `geohashIdentity` تُسند نتيجة `NostrIdentityBridge.deriveIdentity("u4pruydq", context)`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:82]

```
83:         require(geohashIdentity.npub.startsWith("npub1")) { "Invalid geohash identity npub" }
```
> يستدعي `require` على شرط أن `geohashIdentity.npub` يبدأ بـ `"npub1"`، وعند الفشل يرمي بالرسالة `"Invalid geohash identity npub"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:83]

```
84:         require(geohashIdentity.publicKeyHex != identity.publicKeyHex) { "Geohash identity should be different" }
```
> يستدعي `require` على شرط أن `geohashIdentity.publicKeyHex` لا يساوي `identity.publicKeyHex`، وعند الفشل يرمي بالرسالة `"Geohash identity should be different"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:84]

```
85:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:85]

```
86:         Log.d(TAG, "Geohash identity npub: ${geohashIdentity.getShortNpub()}")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"Geohash identity npub: ${geohashIdentity.getShortNpub()}"` المُضمّنة لنتيجة `geohashIdentity.getShortNpub()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:86]

```
87:         Log.d(TAG, "✅ Identity management test successful")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"✅ Identity management test successful"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:87]

```
88:     }
```
> إغلاق نطاق دالة `testIdentityManagement`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:88]

```
89:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:89]

```
90:     private suspend fun testRelayConnections() {
```
> يُعرّف الدالة المُعلّقة الخاصة `testRelayConnections` بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:90]

```
91:         Log.d(TAG, "Testing relay connections...")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"Testing relay connections..."`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:91]

```
92:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:92]

```
93:         // Wait for potential relay connections
```
> تعليق: انتظر اتصالات المُرحّلات المُحتملة. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:93]

```
94:         delay(3000)
```
> يستدعي `delay` بقيمة `3000` (تأخير بالميلي ثانية). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:94]

```
95:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:95]

```
96:         val relayInfo = nostrClient.relayInfo.value ?: emptyList()
```
> يُعرّف خاصية محلية للقراءة فقط `relayInfo` تُسند قيمة `nostrClient.relayInfo.value`، وفي حال كانت فارغة تُسند `emptyList()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:96]

```
97:         require(relayInfo.isNotEmpty()) { "No relays configured" }
```
> يستدعي `require` على شرط أن `relayInfo` ليست فارغة (`isNotEmpty()`)، وعند الفشل يرمي بالرسالة `"No relays configured"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:97]

```
98:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:98]

```
99:         Log.d(TAG, "Configured relays: ${relayInfo.size}")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"Configured relays: ${relayInfo.size}"` المُضمّنة لحجم `relayInfo`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:99]

```
100:         relayInfo.forEach { relay ->
```
> يستدعي `forEach` على `relayInfo` مع معلمة لكل عنصر باسم `relay` ويفتح كتلتها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:100]

```
101:             Log.d(TAG, "Relay: ${relay.url} - Connected: ${relay.isConnected}")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"Relay: ${relay.url} - Connected: ${relay.isConnected}"` المُضمّنة لـ `relay.url` و`relay.isConnected`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:101]

```
102:         }
```
> إغلاق نطاق كتلة `forEach`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:102]

```
103:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:103]

```
104:         Log.d(TAG, "✅ Relay configuration test successful")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"✅ Relay configuration test successful"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:104]

```
105:     }
```
> إغلاق نطاق دالة `testRelayConnections`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:105]

```
106:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:106]

```
107:     private suspend fun testCryptography() {
```
> يُعرّف الدالة المُعلّقة الخاصة `testCryptography` بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:107]

```
108:         Log.d(TAG, "Testing cryptography functions...")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"Testing cryptography functions..."`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:108]

```
109:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:109]

```
110:         // Test key generation
```
> تعليق: اختبر توليد المفاتيح. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:110]

```
111:         val (privateKey, publicKey) = NostrCrypto.generateKeyPair()
```
> يُعرّف عبر تفكيك (destructuring) خاصيتين محليتين للقراءة فقط `privateKey` و`publicKey` من نتيجة `NostrCrypto.generateKeyPair()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:111]

```
112:         require(privateKey.length == 64) { "Invalid private key length" }
```
> يستدعي `require` على شرط أن طول `privateKey` يساوي `64`، وعند الفشل يرمي بالرسالة `"Invalid private key length"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:112]

```
113:         require(publicKey.length == 64) { "Invalid public key length" }
```
> يستدعي `require` على شرط أن طول `publicKey` يساوي `64`، وعند الفشل يرمي بالرسالة `"Invalid public key length"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:113]

```
114:         require(NostrCrypto.isValidPrivateKey(privateKey)) { "Generated private key is invalid" }
```
> يستدعي `require` على نتيجة `NostrCrypto.isValidPrivateKey(privateKey)`، وعند الفشل يرمي بالرسالة `"Generated private key is invalid"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:114]

```
115:         require(NostrCrypto.isValidPublicKey(publicKey)) { "Generated public key is invalid" }
```
> يستدعي `require` على نتيجة `NostrCrypto.isValidPublicKey(publicKey)`، وعند الفشل يرمي بالرسالة `"Generated public key is invalid"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:115]

```
116:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:116]

```
117:         // Test key derivation
```
> تعليق: اختبر اشتقاق المفتاح. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:117]

```
118:         val derivedPublic = NostrCrypto.derivePublicKey(privateKey)
```
> يُعرّف خاصية محلية للقراءة فقط `derivedPublic` تُسند نتيجة `NostrCrypto.derivePublicKey(privateKey)`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:118]

```
119:         require(derivedPublic == publicKey) { "Key derivation mismatch" }
```
> يستدعي `require` على شرط أن `derivedPublic` يساوي `publicKey`، وعند الفشل يرمي بالرسالة `"Key derivation mismatch"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:119]

```
120:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:120]

```
121:         // Test encryption/decryption
```
> تعليق: اختبر التعمية/فك التعمية. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:121]

```
122:         val (recipientPrivate, recipientPublic) = NostrCrypto.generateKeyPair()
```
> يُعرّف عبر التفكيك خاصيتين محليتين للقراءة فقط `recipientPrivate` و`recipientPublic` من نتيجة `NostrCrypto.generateKeyPair()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:122]

```
123:         val plaintext = "Hello, Nostr world! This is a test message."
```
> يُعرّف خاصية محلية للقراءة فقط `plaintext` بقيمة نصية `"Hello, Nostr world! This is a test message."`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:123]

```
124:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:124]

```
125:         val encrypted = NostrCrypto.encryptNIP44(
```
> يُعرّف خاصية محلية للقراءة فقط `encrypted` تُسند نتيجة استدعاء `NostrCrypto.encryptNIP44(` (يبدأ تمرير المُعاملات). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:125]

```
126:             plaintext,
```
> يمرّر المُعامل `plaintext`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:126]

```
127:             recipientPublic,
```
> يمرّر المُعامل `recipientPublic`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:127]

```
128:             privateKey
```
> يمرّر المُعامل `privateKey`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:128]

```
129:         )
```
> يُغلق قائمة مُعاملات استدعاء `encryptNIP44`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:129]

```
130:         require(encrypted.isNotEmpty()) { "Encryption failed" }
```
> يستدعي `require` على شرط أن `encrypted` ليست فارغة (`isNotEmpty()`)، وعند الفشل يرمي بالرسالة `"Encryption failed"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:130]

```
131:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:131]

```
132:         val decrypted = NostrCrypto.decryptNIP44(encrypted, publicKey, recipientPrivate)
```
> يُعرّف خاصية محلية للقراءة فقط `decrypted` تُسند نتيجة `NostrCrypto.decryptNIP44(encrypted, publicKey, recipientPrivate)`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:132]

```
133:         require(decrypted == plaintext) { "Decryption failed: expected '$plaintext', got '$decrypted'" }
```
> يستدعي `require` على شرط أن `decrypted` يساوي `plaintext`، وعند الفشل يرمي بالرسالة `"Decryption failed: expected '$plaintext', got '$decrypted'"` المُضمّنة لقيمتي `plaintext` و`decrypted`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:133]

```
134:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:134]

```
135:         Log.d(TAG, "✅ Cryptography test successful")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"✅ Cryptography test successful"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:135]

```
136:     }
```
> إغلاق نطاق دالة `testCryptography`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:136]

```
137:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:137]

```
138:     private suspend fun testBech32() {
```
> يُعرّف الدالة المُعلّقة الخاصة `testBech32` بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:138]

```
139:         Log.d(TAG, "Testing Bech32 encoding...")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"Testing Bech32 encoding..."`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:139]

```
140:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:140]

```
141:         val testData = "hello world test data for bech32".toByteArray()
```
> يُعرّف خاصية محلية للقراءة فقط `testData` تُسند نتيجة تحويل النص `"hello world test data for bech32"` إلى مصفوفة بايتات عبر `toByteArray()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:141]

```
142:         val encoded = Bech32.encode("test", testData)
```
> يُعرّف خاصية محلية للقراءة فقط `encoded` تُسند نتيجة `Bech32.encode("test", testData)`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:142]

```
143:         require(encoded.startsWith("test1")) { "Invalid bech32 encoding" }
```
> يستدعي `require` على شرط أن `encoded` يبدأ بـ `"test1"`، وعند الفشل يرمي بالرسالة `"Invalid bech32 encoding"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:143]

```
144:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:144]

```
145:         val (hrp, decoded) = Bech32.decode(encoded)
```
> يُعرّف عبر التفكيك خاصيتين محليتين للقراءة فقط `hrp` و`decoded` من نتيجة `Bech32.decode(encoded)`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:145]

```
146:         require(hrp == "test") { "HRP mismatch" }
```
> يستدعي `require` على شرط أن `hrp` يساوي `"test"`، وعند الفشل يرمي بالرسالة `"HRP mismatch"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:146]

```
147:         require(decoded.contentEquals(testData)) { "Data mismatch after decode" }
```
> يستدعي `require` على نتيجة `decoded.contentEquals(testData)`، وعند الفشل يرمي بالرسالة `"Data mismatch after decode"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:147]

```
148:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:148]

```
149:         // Test with actual public key
```
> تعليق: اختبر باستخدام مفتاح عام فعلي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:149]

```
150:         val (_, publicKey) = NostrCrypto.generateKeyPair()
```
> يُعرّف عبر التفكيك خاصية محلية للقراءة فقط `publicKey` من نتيجة `NostrCrypto.generateKeyPair()` مع تجاهل العنصر الأول بالرمز `_`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:150]

```
151:         val npub = Bech32.encode("npub", publicKey.hexToByteArray())
```
> يُعرّف خاصية محلية للقراءة فقط `npub` تُسند نتيجة `Bech32.encode("npub", publicKey.hexToByteArray())`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:151]

```
152:         require(npub.startsWith("npub1")) { "Invalid npub encoding" }
```
> يستدعي `require` على شرط أن `npub` يبدأ بـ `"npub1"`، وعند الفشل يرمي بالرسالة `"Invalid npub encoding"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:152]

```
153:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:153]

```
154:         val (npubHrp, npubData) = Bech32.decode(npub)
```
> يُعرّف عبر التفكيك خاصيتين محليتين للقراءة فقط `npubHrp` و`npubData` من نتيجة `Bech32.decode(npub)`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:154]

```
155:         require(npubHrp == "npub") { "npub HRP mismatch" }
```
> يستدعي `require` على شرط أن `npubHrp` يساوي `"npub"`، وعند الفشل يرمي بالرسالة `"npub HRP mismatch"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:155]

```
156:         require(npubData.toHexString() == publicKey) { "npub data mismatch" }
```
> يستدعي `require` على شرط أن `npubData.toHexString()` يساوي `publicKey`، وعند الفشل يرمي بالرسالة `"npub data mismatch"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:156]

```
157:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:157]

```
158:         Log.d(TAG, "✅ Bech32 test successful")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"✅ Bech32 test successful"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:158]

```
159:     }
```
> إغلاق نطاق دالة `testBech32`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:159]

```
160:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:160]

```
161:     private suspend fun testMessageSubscription() {
```
> يُعرّف الدالة المُعلّقة الخاصة `testMessageSubscription` بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:161]

```
162:         Log.d(TAG, "Testing message subscription...")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"Testing message subscription..."`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:162]

```
163:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:163]

```
164:         var messageReceived = false
```
> يُعرّف خاصية محلية متغيرة `messageReceived` بقيمة ابتدائية `false`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:164]

```
165:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:165]

```
166:         // Subscribe to private messages (won't receive any in test, but tests the subscription mechanism)
```
> تعليق: اشترك في الرسائل الخاصة (لن يُستقبل أي منها في الاختبار، لكنه يختبر آلية الاشتراك). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:166]

```
167:         nostrClient.subscribeToPrivateMessages { content, senderNpub, timestamp ->
```
> يستدعي `subscribeToPrivateMessages` على `nostrClient` مع دالة لمدا مُعاملاتها `content` و`senderNpub` و`timestamp`، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:167]

```
168:             Log.d(TAG, "📥 Received test private message from $senderNpub: $content")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"📥 Received test private message from $senderNpub: $content"` المُضمّنة لـ `senderNpub` و`content`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:168]

```
169:             messageReceived = true
```
> يُسند القيمة `true` إلى `messageReceived`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:169]

```
170:         }
```
> إغلاق نطاق دالة لمدا اشتراك الرسائل الخاصة. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:170]

```
171:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:171]

```
172:         // Subscribe to a test geohash
```
> تعليق: اشترك في مُعرّف موقع مُجزّأ (geohash) للاختبار. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:172]

```
173:         nostrClient.subscribeToGeohash("u4pru") { content, senderPubkey, nickname, timestamp ->
```
> يستدعي `subscribeToGeohash` على `nostrClient` بالوسيط النصي `"u4pru"` مع دالة لمدا مُعاملاتها `content` و`senderPubkey` و`nickname` و`timestamp`، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:173]

```
174:             Log.d(TAG, "📥 Received test geohash message from ${senderPubkey.take(16)}...: $content")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"📥 Received test geohash message from ${senderPubkey.take(16)}...: $content"` المُضمّنة لأول ١٦ محرفاً من `senderPubkey` و`content`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:174]

```
175:             messageReceived = true
```
> يُسند القيمة `true` إلى `messageReceived`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:175]

```
176:         }
```
> إغلاق نطاق دالة لمدا اشتراك مُعرّف الموقع المُجزّأ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:176]

```
177:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:177]

```
178:         // Wait a bit to see if any messages come through
```
> تعليق: انتظر قليلاً لمعرفة إن وصلت أي رسائل. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:178]

```
179:         delay(2000)
```
> يستدعي `delay` بقيمة `2000` (تأخير بالميلي ثانية). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:179]

```
180:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:180]

```
181:         Log.d(TAG, "✅ Message subscription test successful (no messages expected in test)")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة نصية `"✅ Message subscription test successful (no messages expected in test)"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:181]

```
182:     }
```
> إغلاق نطاق دالة `testMessageSubscription`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:182]

```
183:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:183]

```
184:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:184]

```
185:      * Test sending a message to yourself (loopback test)
```
> تعليق: اختبر إرسال رسالة إلى نفسك (اختبار العودة الذاتية loopback). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:185]

```
186:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:186]

```
187:     fun testLoopbackMessage() {
```
> يُعرّف الدالة `testLoopbackMessage` بلا مُعاملات ويفتح نطاقها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:187]

```
188:         testScope.launch {
```
> يستدعي `launch` على `testScope` لإطلاق كوروتين ويفتح كتلتها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:188]

```
189:             try {
```
> يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:189]

```
190:                 val identity = nostrClient.getCurrentIdentity()
```
> يُعرّف خاصية محلية للقراءة فقط `identity` تُسند نتيجة `nostrClient.getCurrentIdentity()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:190]

```
191:                 requireNotNull(identity) { "No identity available for loopback test" }
```
> يستدعي `requireNotNull` على `identity`، وعند كونها فارغة يرمي بالرسالة `"No identity available for loopback test"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:191]

```
192:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:192]

```
193:                 Log.i(TAG, "🔄 Testing loopback private message...")
```
> يستدعي `Log.i` بالوسم `TAG` ورسالة نصية `"🔄 Testing loopback private message..."`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:193]

```
194:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:194]

```
195:                 // Send message to ourselves
```
> تعليق: أرسل رسالة إلى أنفسنا. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:195]

```
196:                 nostrClient.sendPrivateMessage(
```
> يستدعي `sendPrivateMessage` على `nostrClient` (يبدأ تمرير المُعاملات). [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:196]

```
197:                     content = "Test loopback message at ${System.currentTimeMillis()}",
```
> يمرّر المُعامل المُسمّى `content` بقيمة نصية `"Test loopback message at ${System.currentTimeMillis()}"` المُضمّنة لنتيجة `System.currentTimeMillis()`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:197]

```
198:                     recipientNpub = identity.npub,
```
> يمرّر المُعامل المُسمّى `recipientNpub` بقيمة `identity.npub`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:198]

```
199:                     onSuccess = {
```
> يمرّر المُعامل المُسمّى `onSuccess` بدالة لمدا، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:199]

```
200:                         Log.i(TAG, "✅ Loopback message sent successfully")
```
> يستدعي `Log.i` بالوسم `TAG` ورسالة نصية `"✅ Loopback message sent successfully"`. [app/src/main/java/com/bitchat/android/nostr/NostrTestManager.kt:200]
