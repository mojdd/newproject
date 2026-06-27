# شريحة — app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) المسمّاة `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من حزمة أندرويد `android.content`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف `Log` من حزمة أندرويد `android.util`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:4]

```
5: import com.bitchat.android.model.BitchatFilePacket
```
> يستورد الصنف `BitchatFilePacket` (حزمة ملف بيتشات) من حزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:5]

```
6: import com.bitchat.android.model.BitchatMessage
```
> يستورد الصنف `BitchatMessage` (رسالة بيتشات) من حزمة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:6]

```
7: import com.bitchat.android.noise.NoiseSession
```
> يستورد الصنف `NoiseSession` (جلسة نويز) من حزمة `com.bitchat.android.noise`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:7]

```
8: import com.bitchat.android.wifiaware.WifiAwareController
```
> يستورد الصنف `WifiAwareController` (متحكّم واي‑فاي أوير) من حزمة `com.bitchat.android.wifiaware`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:9]

```
10: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:10]

```
11:  * Feature-facing mesh service that hides local transport selection from the rest of the app.
```
> تعليق: خدمة شبكة متشابكة موجَّهة للميزات تُخفي اختيار وسيلة النقل المحلية عن بقية التطبيق. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:11]

```
12:  *
```
> تعليق: سطر فارغ داخل التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:12]

```
13:  * BLE remains the canonical origin for broadcast packets when it is enabled so existing BLE mesh
```
> تعليق: يبقى البلوتوث منخفض الطاقة (BLE) المصدر المعياري لحزم البثّ عند تفعيله كي تظل شبكة BLE المتشابكة القائمة. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:13]

```
14:  * behavior and bridge semantics stay intact. Addressed Noise traffic is routed over whichever
```
> تعليق: سلوكها ودلالات الجسر سليمة. حركة نويز المعنونة تُوجَّه عبر أيٍّ كان. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:14]

```
15:  * local transport already has the peer/session, falling back to a connected transport handshake.
```
> تعليق: من وسائل النقل المحلية التي لديها بالفعل النِّدّ/الجلسة، مع التراجع إلى مصافحة وسيلة نقل متصلة. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:15]

```
16:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:16]

```
17: class UnifiedMeshService(
```
> يُعرّف الصنف `UnifiedMeshService` (خدمة الشبكة المتشابكة الموحَّدة) مع بداية قائمة معاملات الباني (constructor). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:17]

```
18:     private val context: Context
```
> يُعرّف معاملاً للباني خاصاً غير قابل للتغيير اسمه `context` من نوع `Context`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:18]

```
19:     private val bluetooth: BluetoothMeshService
```
> يُعرّف معاملاً للباني خاصاً غير قابل للتغيير اسمه `bluetooth` من نوع `BluetoothMeshService` (خدمة شبكة بلوتوث متشابكة). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:19]

```
20: ) : MeshService, BluetoothMeshDelegate {
```
> ينهي قائمة معاملات الباني، ويعلن أن الصنف يحقّق الواجهتين `MeshService` (خدمة الشبكة المتشابكة) و`BluetoothMeshDelegate` (مندوب شبكة البلوتوث المتشابكة)، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:20]

```
21: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:21]

```
22:     companion object {
```
> يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:22]

```
23:         private const val TAG = "UnifiedMeshService"
```
> يُعرّف ثابتاً خاصاً اسمه `TAG` بقيمة السلسلة `"UnifiedMeshService"`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:23]

```
24:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:25]

```
26:     override val myPeerID: String
```
> يُعيد تعريف (override) الخاصية غير القابلة للتغيير `myPeerID` (معرّف نِدّي) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:26]

```
27:         get() = bluetooth.myPeerID
```
> يُعرّف جالب (getter) الخاصية الذي يُعيد قيمة `bluetooth.myPeerID`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:28]

```
29:     override var delegate: MeshDelegate? = null
```
> يُعيد تعريف الخاصية القابلة للتغيير `delegate` (المندوب) من نوع `MeshDelegate?` ويهيّئها بالقيمة `null`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:29]

```
30:         set(value) {
```
> يُعرّف ضابط (setter) الخاصية الذي يأخذ معاملاً اسمه `value`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:30]

```
31:             field = value
```
> يُسنِد `value` إلى الحقل الداعم `field`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:31]

```
32:             refreshDelegates()
```
> يستدعي الدالة `refreshDelegates()` (تحديث المندوبين). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:32]

```
33:         }
```
> إغلاق نطاق الضابط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:33]

```
34: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:34]

```
35:     fun refreshDelegates() {
```
> يُعرّف الدالة `refreshDelegates()` ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:35]

```
36:         try { bluetooth.delegate = if (delegate != null) this else null } catch (_: Exception) { }
```
> داخل كتلة `try`، يُسنِد إلى `bluetooth.delegate` القيمة `this` إذا كان `delegate` غير `null` وإلا `null`، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:36]

```
37:         try { wifiService()?.delegate = if (delegate != null) this else null } catch (_: Exception) { }
```
> داخل كتلة `try`، يُسنِد إلى `delegate` لنتيجة `wifiService()` (إن لم تكن null) القيمة `this` إذا كان `delegate` غير `null` وإلا `null`، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:37]

```
38:     }
```
> إغلاق نطاق الدالة `refreshDelegates`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:38]

```
39: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:39]

```
40:     override fun startServices() {
```
> يُعيد تعريف الدالة `startServices()` (بدء الخدمات) ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:40]

```
41:         if (isBleEnabled()) {
```
> يبدأ شرط `if` يختبر نتيجة `isBleEnabled()` (هل البلوتوث منخفض الطاقة مفعّل). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:41]

```
42:             try { bluetooth.startServices() } catch (e: Exception) {
```
> داخل كتلة `try`، يستدعي `bluetooth.startServices()`، ويلتقط `Exception` في المتغيّر `e` ويفتح كتلة `catch`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:42]

```
43:                 Log.w(TAG, "Failed to start BLE transport: ${e.message}")
```
> يستدعي `Log.w` بالوسم `TAG` والرسالة `"Failed to start BLE transport: ${e.message}"` (فشل بدء نقل BLE) مع إدراج `e.message`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:43]

```
44:             }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:44]

```
45:         } else {
```
> ينهي كتلة `if` ويفتح كتلة `else`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:45]

```
46:             try { bluetooth.setBleTransportEnabled(false) } catch (_: Exception) { }
```
> داخل كتلة `try`، يستدعي `bluetooth.setBleTransportEnabled(false)` (تعطيل نقل BLE)، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:46]

```
47:         }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:47]

```
48:         try { WifiAwareController.startIfPossible() } catch (e: Exception) {
```
> داخل كتلة `try`، يستدعي `WifiAwareController.startIfPossible()` (ابدأ إن أمكن)، ويلتقط `Exception` في `e` ويفتح كتلة `catch`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:48]

```
49:             Log.w(TAG, "Failed to start Wi-Fi Aware transport: ${e.message}")
```
> يستدعي `Log.w` بالوسم `TAG` والرسالة `"Failed to start Wi-Fi Aware transport: ${e.message}"` (فشل بدء نقل واي‑فاي أوير) مع إدراج `e.message`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:49]

```
50:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:50]

```
51:         refreshDelegates()
```
> يستدعي الدالة `refreshDelegates()`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:51]

```
52:     }
```
> إغلاق نطاق الدالة `startServices`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:52]

```
53: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:53]

```
54:     override fun stopServices() {
```
> يُعيد تعريف الدالة `stopServices()` (إيقاف الخدمات) ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:54]

```
55:         try { bluetooth.stopServices() } catch (_: Exception) { }
```
> داخل كتلة `try`، يستدعي `bluetooth.stopServices()`، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:55]

```
56:         try { WifiAwareController.stop() } catch (_: Exception) { }
```
> داخل كتلة `try`، يستدعي `WifiAwareController.stop()` (إيقاف)، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:56]

```
57:     }
```
> إغلاق نطاق الدالة `stopServices`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:57]

```
58: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:58]

```
59:     override fun sendMessage(content: String, mentions: List<String>, channel: String?) {
```
> يُعيد تعريف الدالة `sendMessage` (إرسال رسالة) التي تأخذ `content` نصاً، و`mentions` قائمة نصوص، و`channel` نصاً قابلاً لأن يكون null، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:59]

```
60:         when {
```
> يفتح تعبير `when` بلا وسيط (سلسلة شروط). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:60]

```
61:             isBleEnabled() -> bluetooth.sendMessage(content, mentions, channel)
```
> إذا كان `isBleEnabled()` صحيحاً، يستدعي `bluetooth.sendMessage(content, mentions, channel)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:61]

```
62:             else -> wifiService()?.sendMessage(content, mentions, channel)
```
> وإلا، يستدعي `sendMessage(content, mentions, channel)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:62]

```
63:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:63]

```
64:     }
```
> إغلاق نطاق الدالة `sendMessage`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:65]

```
66:     override fun sendPrivateMessage(
```
> يُعيد تعريف الدالة `sendPrivateMessage` (إرسال رسالة خاصة) مع بداية قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:66]

```
67:         content: String,
```
> يُعرّف المعامل `content` من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:67]

```
68:         recipientPeerID: String,
```
> يُعرّف المعامل `recipientPeerID` (معرّف نِدّ المستلِم) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:68]

```
69:         recipientNickname: String,
```
> يُعرّف المعامل `recipientNickname` (لقب المستلِم) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:69]

```
70:         messageID: String?
```
> يُعرّف المعامل `messageID` (معرّف الرسالة) من نوع `String?` قابل لأن يكون null. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:70]

```
71:     ) {
```
> ينهي قائمة المعاملات ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:71]

```
72:         when {
```
> يفتح تعبير `when` بلا وسيط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:72]

```
73:             isBleReady(recipientPeerID) -> bluetooth.sendPrivateMessage(content, recipientPeerID, recipientNickname, messageID)
```
> إذا كان `isBleReady(recipientPeerID)` (هل BLE جاهز للنِّدّ) صحيحاً، يستدعي `bluetooth.sendPrivateMessage(content, recipientPeerID, recipientNickname, messageID)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:73]

```
74:             isWifiReady(recipientPeerID) -> wifiService()?.sendPrivateMessage(content, recipientPeerID, recipientNickname, messageID)
```
> وإلا إذا كان `isWifiReady(recipientPeerID)` (هل الواي‑فاي جاهز للنِّدّ) صحيحاً، يستدعي `sendPrivateMessage(content, recipientPeerID, recipientNickname, messageID)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:74]

```
75:             isBleConnected(recipientPeerID) || (isBleEnabled() && !isWifiConnected(recipientPeerID)) ->
```
> وإلا إذا كان `isBleConnected(recipientPeerID)` صحيحاً، أو كان `isBleEnabled()` صحيحاً و`isWifiConnected(recipientPeerID)` غير صحيح، فالشرط ينطبق ويُتبَع بالتعبير في السطر التالي. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:75]

```
76:                 bluetooth.sendPrivateMessage(content, recipientPeerID, recipientNickname, messageID)
```
> يستدعي `bluetooth.sendPrivateMessage(content, recipientPeerID, recipientNickname, messageID)` كنتيجة لشرط السطر السابق. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:76]

```
77:             else -> wifiService()?.sendPrivateMessage(content, recipientPeerID, recipientNickname, messageID)
```
> وإلا، يستدعي `sendPrivateMessage(content, recipientPeerID, recipientNickname, messageID)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:77]

```
78:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:78]

```
79:     }
```
> إغلاق نطاق الدالة `sendPrivateMessage`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:79]

```
80: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:80]

```
81:     override fun sendReadReceipt(messageID: String, recipientPeerID: String, readerNickname: String) {
```
> يُعيد تعريف الدالة `sendReadReceipt` (إرسال إيصال قراءة) التي تأخذ `messageID` و`recipientPeerID` و`readerNickname` نصوصاً، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:81]

```
82:         when {
```
> يفتح تعبير `when` بلا وسيط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:82]

```
83:             isBleReady(recipientPeerID) -> bluetooth.sendReadReceipt(messageID, recipientPeerID, readerNickname)
```
> إذا كان `isBleReady(recipientPeerID)` صحيحاً، يستدعي `bluetooth.sendReadReceipt(messageID, recipientPeerID, readerNickname)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:83]

```
84:             isWifiReady(recipientPeerID) -> wifiService()?.sendReadReceipt(messageID, recipientPeerID, readerNickname)
```
> وإلا إذا كان `isWifiReady(recipientPeerID)` صحيحاً، يستدعي `sendReadReceipt(messageID, recipientPeerID, readerNickname)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:84]

```
85:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:85]

```
86:     }
```
> إغلاق نطاق الدالة `sendReadReceipt`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:86]

```
87: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:87]

```
88:     override fun sendFavoriteNotification(peerID: String, isFavorite: Boolean) {
```
> يُعيد تعريف الدالة `sendFavoriteNotification` (إرسال إشعار تفضيل) التي تأخذ `peerID` نصاً و`isFavorite` منطقياً، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:88]

```
89:         val myNpub = try {
```
> يُعرّف متغيّراً غير قابل للتغيير اسمه `myNpub` تكون قيمته نتيجة كتلة `try`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:89]

```
90:             com.bitchat.android.nostr.NostrIdentityBridge.getCurrentNostrIdentity(context)?.npub
```
> يستدعي `NostrIdentityBridge.getCurrentNostrIdentity(context)` (جسر هويّة نوستر، جلب الهويّة الحالية) ويأخذ خاصيّته `npub` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:90]

```
91:         } catch (_: Exception) {
```
> يلتقط أي `Exception` ويفتح كتلة `catch`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:91]

```
92:             null
```
> يجعل قيمة كتلة `try`/`catch` مساوية لـ `null` عند الالتقاط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:92]

```
93:         }
```
> إغلاق نطاق كتلة `catch` (ونهاية تعبير `try` المُسنَد). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:93]

```
94:         val content = if (isFavorite) "[FAVORITED]:${myNpub ?: ""}" else "[UNFAVORITED]:${myNpub ?: ""}"
```
> يُعرّف متغيّراً غير قابل للتغيير اسمه `content` بقيمة `"[FAVORITED]:${myNpub ?: ""}"` إذا كان `isFavorite` صحيحاً وإلا `"[UNFAVORITED]:${myNpub ?: ""}"`، مع استبدال `myNpub` بسلسلة فارغة عند كونها null. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:94]

```
95:         val nickname = getPeerNicknames()[peerID] ?: peerID
```
> يُعرّف متغيّراً غير قابل للتغيير اسمه `nickname` بقيمة العنصر المقابل لـ `peerID` في `getPeerNicknames()`، وإذا كان null فقيمته `peerID`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:95]

```
96:         if (hasEstablishedSession(peerID)) {
```
> يبدأ شرط `if` يختبر `hasEstablishedSession(peerID)` (هل توجد جلسة مؤسَّسة للنِّدّ). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:96]

```
97:             sendPrivateMessage(content, peerID, nickname, java.util.UUID.randomUUID().toString())
```
> يستدعي `sendPrivateMessage(content, peerID, nickname, ...)` مع معرّف رسالة مولَّد من `java.util.UUID.randomUUID().toString()`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:97]

```
98:         }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:98]

```
99:     }
```
> إغلاق نطاق الدالة `sendFavoriteNotification`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:99]

```
100: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:100]

```
101:     override fun sendVerifyChallenge(peerID: String, noiseKeyHex: String, nonceA: ByteArray) {
```
> يُعيد تعريف الدالة `sendVerifyChallenge` (إرسال تحدّي تحقّق) التي تأخذ `peerID` نصاً و`noiseKeyHex` (مفتاح نويز ستّ‑عشري) نصاً و`nonceA` (الرقم العشوائي A) مصفوفة بايتات، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:101]

```
102:         when {
```
> يفتح تعبير `when` بلا وسيط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:102]

```
103:             isBleReady(peerID) -> bluetooth.sendVerifyChallenge(peerID, noiseKeyHex, nonceA)
```
> إذا كان `isBleReady(peerID)` صحيحاً، يستدعي `bluetooth.sendVerifyChallenge(peerID, noiseKeyHex, nonceA)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:103]

```
104:             isWifiReady(peerID) -> wifiService()?.sendVerifyChallenge(peerID, noiseKeyHex, nonceA)
```
> وإلا إذا كان `isWifiReady(peerID)` صحيحاً، يستدعي `sendVerifyChallenge(peerID, noiseKeyHex, nonceA)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:104]

```
105:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:105]

```
106:     }
```
> إغلاق نطاق الدالة `sendVerifyChallenge`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:106]

```
107: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:107]

```
108:     override fun sendVerifyResponse(peerID: String, noiseKeyHex: String, nonceA: ByteArray) {
```
> يُعيد تعريف الدالة `sendVerifyResponse` (إرسال ردّ تحقّق) التي تأخذ `peerID` نصاً و`noiseKeyHex` نصاً و`nonceA` مصفوفة بايتات، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:108]

```
109:         when {
```
> يفتح تعبير `when` بلا وسيط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:109]

```
110:             isBleReady(peerID) -> bluetooth.sendVerifyResponse(peerID, noiseKeyHex, nonceA)
```
> إذا كان `isBleReady(peerID)` صحيحاً، يستدعي `bluetooth.sendVerifyResponse(peerID, noiseKeyHex, nonceA)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:110]

```
111:             isWifiReady(peerID) -> wifiService()?.sendVerifyResponse(peerID, noiseKeyHex, nonceA)
```
> وإلا إذا كان `isWifiReady(peerID)` صحيحاً، يستدعي `sendVerifyResponse(peerID, noiseKeyHex, nonceA)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:111]

```
112:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:112]

```
113:     }
```
> إغلاق نطاق الدالة `sendVerifyResponse`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:113]

```
114: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:114]

```
115:     override fun sendFileBroadcast(file: BitchatFilePacket) {
```
> يُعيد تعريف الدالة `sendFileBroadcast` (إرسال بثّ ملف) التي تأخذ `file` من نوع `BitchatFilePacket`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:115]

```
116:         when {
```
> يفتح تعبير `when` بلا وسيط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:116]

```
117:             isBleEnabled() -> bluetooth.sendFileBroadcast(file)
```
> إذا كان `isBleEnabled()` صحيحاً، يستدعي `bluetooth.sendFileBroadcast(file)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:117]

```
118:             else -> wifiService()?.sendFileBroadcast(file)
```
> وإلا، يستدعي `sendFileBroadcast(file)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:118]

```
119:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:119]

```
120:     }
```
> إغلاق نطاق الدالة `sendFileBroadcast`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:120]

```
121: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:121]

```
122:     override fun sendFilePrivate(recipientPeerID: String, file: BitchatFilePacket) {
```
> يُعيد تعريف الدالة `sendFilePrivate` (إرسال ملف خاص) التي تأخذ `recipientPeerID` نصاً و`file` من نوع `BitchatFilePacket`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:122]

```
123:         when {
```
> يفتح تعبير `when` بلا وسيط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:123]

```
124:             isBleReady(recipientPeerID) -> bluetooth.sendFilePrivate(recipientPeerID, file)
```
> إذا كان `isBleReady(recipientPeerID)` صحيحاً، يستدعي `bluetooth.sendFilePrivate(recipientPeerID, file)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:124]

```
125:             isWifiReady(recipientPeerID) -> wifiService()?.sendFilePrivate(recipientPeerID, file)
```
> وإلا إذا كان `isWifiReady(recipientPeerID)` صحيحاً، يستدعي `sendFilePrivate(recipientPeerID, file)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:125]

```
126:             isBleConnected(recipientPeerID) || (isBleEnabled() && !isWifiConnected(recipientPeerID)) ->
```
> وإلا إذا كان `isBleConnected(recipientPeerID)` صحيحاً، أو كان `isBleEnabled()` صحيحاً و`isWifiConnected(recipientPeerID)` غير صحيح، فالشرط ينطبق ويُتبَع بالتعبير في السطر التالي. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:126]

```
127:                 bluetooth.sendFilePrivate(recipientPeerID, file)
```
> يستدعي `bluetooth.sendFilePrivate(recipientPeerID, file)` كنتيجة لشرط السطر السابق. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:127]

```
128:             else -> wifiService()?.sendFilePrivate(recipientPeerID, file)
```
> وإلا، يستدعي `sendFilePrivate(recipientPeerID, file)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:128]

```
129:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:129]

```
130:     }
```
> إغلاق نطاق الدالة `sendFilePrivate`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:130]

```
131: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:131]

```
132:     override fun cancelFileTransfer(transferId: String): Boolean {
```
> يُعيد تعريف الدالة `cancelFileTransfer` (إلغاء نقل ملف) التي تأخذ `transferId` (معرّف النقل) نصاً وتُعيد قيمة منطقية، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:132]

```
133:         val bleCancelled = try { bluetooth.cancelFileTransfer(transferId) } catch (_: Exception) { false }
```
> يُعرّف متغيّراً غير قابل للتغيير اسمه `bleCancelled` بقيمة نتيجة `bluetooth.cancelFileTransfer(transferId)` ضمن `try`، وعند التقاط أي `Exception` تكون قيمته `false`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:133]

```
134:         val wifiCancelled = try { wifiService()?.cancelFileTransfer(transferId) == true } catch (_: Exception) { false }
```
> يُعرّف متغيّراً غير قابل للتغيير اسمه `wifiCancelled` بقيمة نتيجة مقارنة `wifiService()?.cancelFileTransfer(transferId) == true` ضمن `try`، وعند التقاط أي `Exception` تكون قيمته `false`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:134]

```
135:         return bleCancelled || wifiCancelled
```
> يُعيد نتيجة `bleCancelled || wifiCancelled` (أحدهما على الأقل صحيح). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:135]

```
136:     }
```
> إغلاق نطاق الدالة `cancelFileTransfer`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:136]

```
137: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:137]

```
138:     override fun sendBroadcastAnnounce() {
```
> يُعيد تعريف الدالة `sendBroadcastAnnounce` (إرسال إعلان بثّ) ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:138]

```
139:         if (isBleEnabled()) {
```
> يبدأ شرط `if` يختبر `isBleEnabled()`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:139]

```
140:             try { bluetooth.sendBroadcastAnnounce() } catch (_: Exception) { }
```
> داخل كتلة `try`، يستدعي `bluetooth.sendBroadcastAnnounce()`، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:140]

```
141:         }
```
> إغلاق نطاق كتلة `if`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:141]

```
142:         try { wifiService()?.sendBroadcastAnnounce() } catch (_: Exception) { }
```
> داخل كتلة `try`، يستدعي `sendBroadcastAnnounce()` على نتيجة `wifiService()` (إن لم تكن null)، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:142]

```
143:     }
```
> إغلاق نطاق الدالة `sendBroadcastAnnounce`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:143]

```
144: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:144]

```
145:     override fun sendAnnouncementToPeer(peerID: String) {
```
> يُعيد تعريف الدالة `sendAnnouncementToPeer` (إرسال إعلان إلى نِدّ) التي تأخذ `peerID` نصاً، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:145]

```
146:         when {
```
> يفتح تعبير `when` بلا وسيط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:146]

```
147:             isBleConnected(peerID) || (isBleEnabled() && !isWifiConnected(peerID)) -> bluetooth.sendAnnouncementToPeer(peerID)
```
> إذا كان `isBleConnected(peerID)` صحيحاً، أو كان `isBleEnabled()` صحيحاً و`isWifiConnected(peerID)` غير صحيح، يستدعي `bluetooth.sendAnnouncementToPeer(peerID)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:147]

```
148:             else -> wifiService()?.sendAnnouncementToPeer(peerID)
```
> وإلا، يستدعي `sendAnnouncementToPeer(peerID)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:148]

```
149:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:149]

```
150:     }
```
> إغلاق نطاق الدالة `sendAnnouncementToPeer`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:150]

```
151: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:151]

```
152:     override fun getPeerNicknames(): Map<String, String> {
```
> يُعيد تعريف الدالة `getPeerNicknames` (جلب ألقاب الأنداد) التي تُعيد خريطة من نص إلى نص، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:152]

```
153:         val merged = linkedMapOf<String, String>()
```
> يُعرّف متغيّراً غير قابل للتغيير اسمه `merged` (المدمَجة) بقيمة خريطة مرتبطة فارغة من نص إلى نص عبر `linkedMapOf`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:153]

```
154:         try { merged.putAll(wifiService()?.getPeerNicknames().orEmpty()) } catch (_: Exception) { }
```
> داخل كتلة `try`، يضيف إلى `merged` كل عناصر `wifiService()?.getPeerNicknames()` (أو خريطة فارغة عبر `orEmpty` عند null)، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:154]

```
155:         try { merged.putAll(bluetooth.getPeerNicknames()) } catch (_: Exception) { }
```
> داخل كتلة `try`، يضيف إلى `merged` كل عناصر `bluetooth.getPeerNicknames()`، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:155]

```
156:         return merged
```
> يُعيد الخريطة `merged`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:156]

```
157:     }
```
> إغلاق نطاق الدالة `getPeerNicknames`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:157]

```
158: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:158]

```
159:     override fun getPeerRSSI(): Map<String, Int> {
```
> يُعيد تعريف الدالة `getPeerRSSI` (جلب قوة إشارة الأنداد RSSI) التي تُعيد خريطة من نص إلى عدد صحيح، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:159]

```
160:         val merged = linkedMapOf<String, Int>()
```
> يُعرّف متغيّراً غير قابل للتغيير اسمه `merged` بقيمة خريطة مرتبطة فارغة من نص إلى عدد صحيح عبر `linkedMapOf`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:160]

```
161:         try { merged.putAll(wifiService()?.getPeerRSSI().orEmpty()) } catch (_: Exception) { }
```
> داخل كتلة `try`، يضيف إلى `merged` كل عناصر `wifiService()?.getPeerRSSI()` (أو خريطة فارغة عبر `orEmpty` عند null)، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:161]

```
162:         try { merged.putAll(bluetooth.getPeerRSSI()) } catch (_: Exception) { }
```
> داخل كتلة `try`، يضيف إلى `merged` كل عناصر `bluetooth.getPeerRSSI()`، ويلتقط أي `Exception` دون فعل. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:162]

```
163:         return merged
```
> يُعيد الخريطة `merged`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:163]

```
164:     }
```
> إغلاق نطاق الدالة `getPeerRSSI`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:164]

```
165: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:165]

```
166:     override fun getActivePeerCount(): Int {
```
> يُعيد تعريف الدالة `getActivePeerCount` (جلب عدد الأنداد النشطين) التي تُعيد عدداً صحيحاً، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:166]

```
167:         return mergedPeerIDs().filter { it != myPeerID }.distinct().size
```
> يُعيد حجم القائمة الناتجة عن `mergedPeerIDs()` (معرّفات الأنداد المدمَجة) بعد ترشيح العناصر المختلفة عن `myPeerID` ثم إزالة التكرار عبر `distinct`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:167]

```
168:     }
```
> إغلاق نطاق الدالة `getActivePeerCount`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:168]

```
169: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:169]

```
170:     override fun hasEstablishedSession(peerID: String): Boolean {
```
> يُعيد تعريف الدالة `hasEstablishedSession` (هل توجد جلسة مؤسَّسة) التي تأخذ `peerID` نصاً وتُعيد قيمة منطقية، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:170]

```
171:         return isBleReady(peerID) || isWifiReady(peerID)
```
> يُعيد نتيجة `isBleReady(peerID) || isWifiReady(peerID)` (جاهزية BLE أو الواي‑فاي للنِّدّ). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:171]

```
172:     }
```
> إغلاق نطاق الدالة `hasEstablishedSession`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:172]

```
173: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:173]

```
174:     override fun getSessionState(peerID: String): NoiseSession.NoiseSessionState {
```
> يُعيد تعريف الدالة `getSessionState` (جلب حالة الجلسة) التي تأخذ `peerID` نصاً وتُعيد قيمة من نوع `NoiseSession.NoiseSessionState`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:174]

```
175:         val bleState = try { bluetooth.getSessionState(peerID) } catch (_: Exception) { NoiseSession.NoiseSessionState.Uninitialized }
```
> يُعرّف متغيّراً غير قابل للتغيير اسمه `bleState` بقيمة `bluetooth.getSessionState(peerID)` ضمن `try`، وعند التقاط أي `Exception` تكون قيمته `NoiseSession.NoiseSessionState.Uninitialized` (غير مُهيّأة). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:175]

```
176:         val wifiState = try { wifiService()?.getSessionState(peerID) } catch (_: Exception) { null }
```
> يُعرّف متغيّراً غير قابل للتغيير اسمه `wifiState` بقيمة `wifiService()?.getSessionState(peerID)` ضمن `try`، وعند التقاط أي `Exception` تكون قيمته `null`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:176]

```
177:         return when {
```
> يُعيد نتيجة تعبير `when` بلا وسيط ويفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:177]

```
178:             bleState is NoiseSession.NoiseSessionState.Established -> bleState
```
> إذا كان `bleState` من النوع `NoiseSession.NoiseSessionState.Established` (مؤسَّسة)، تكون النتيجة `bleState`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:178]

```
179:             wifiState is NoiseSession.NoiseSessionState.Established -> wifiState
```
> وإلا إذا كان `wifiState` من النوع `Established`، تكون النتيجة `wifiState`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:179]

```
180:             bleState is NoiseSession.NoiseSessionState.Handshaking -> bleState
```
> وإلا إذا كان `bleState` من النوع `Handshaking` (قيد المصافحة)، تكون النتيجة `bleState`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:180]

```
181:             wifiState is NoiseSession.NoiseSessionState.Handshaking -> wifiState
```
> وإلا إذا كان `wifiState` من النوع `Handshaking`، تكون النتيجة `wifiState`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:181]

```
182:             bleState !is NoiseSession.NoiseSessionState.Uninitialized -> bleState
```
> وإلا إذا لم يكن `bleState` من النوع `Uninitialized`، تكون النتيجة `bleState`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:182]

```
183:             wifiState != null -> wifiState
```
> وإلا إذا كان `wifiState` غير `null`، تكون النتيجة `wifiState`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:183]

```
184:             else -> bleState
```
> وإلا، تكون النتيجة `bleState`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:184]

```
185:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:185]

```
186:     }
```
> إغلاق نطاق الدالة `getSessionState`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:186]

```
187: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:187]

```
188:     override fun initiateNoiseHandshake(peerID: String) {
```
> يُعيد تعريف الدالة `initiateNoiseHandshake` (بدء مصافحة نويز) التي تأخذ `peerID` نصاً، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:188]

```
189:         when {
```
> يفتح تعبير `when` بلا وسيط. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:189]

```
190:             isBleConnected(peerID) -> bluetooth.initiateNoiseHandshake(peerID)
```
> إذا كان `isBleConnected(peerID)` صحيحاً، يستدعي `bluetooth.initiateNoiseHandshake(peerID)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:190]

```
191:             isWifiConnected(peerID) -> wifiService()?.initiateNoiseHandshake(peerID)
```
> وإلا إذا كان `isWifiConnected(peerID)` صحيحاً، يستدعي `initiateNoiseHandshake(peerID)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:191]

```
192:             isBleEnabled() -> bluetooth.initiateNoiseHandshake(peerID)
```
> وإلا إذا كان `isBleEnabled()` صحيحاً، يستدعي `bluetooth.initiateNoiseHandshake(peerID)`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:192]

```
193:             else -> wifiService()?.initiateNoiseHandshake(peerID)
```
> وإلا، يستدعي `initiateNoiseHandshake(peerID)` على نتيجة `wifiService()` (إن لم تكن null). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:193]

```
194:         }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:194]

```
195:     }
```
> إغلاق نطاق الدالة `initiateNoiseHandshake`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:195]

```
196: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:196]

```
197:     override fun getPeerFingerprint(peerID: String): String? {
```
> يُعيد تعريف الدالة `getPeerFingerprint` (جلب بصمة النِّدّ) التي تأخذ `peerID` نصاً وتُعيد نصاً قابلاً لأن يكون null، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:197]

```
198:         return try { bluetooth.getPeerFingerprint(peerID) } catch (_: Exception) { null }
```
> يبدأ تعبير `return` بقيمة `bluetooth.getPeerFingerprint(peerID)` ضمن `try` (وعند التقاط أي `Exception` تكون `null`)، ويُتبَع بعامل التراجع في السطر التالي. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:198]

```
199:             ?: try { wifiService()?.getPeerFingerprint(peerID) } catch (_: Exception) { null }
```
> عبر عامل إلفيس `?:`، إذا كانت القيمة السابقة null تُستخدم نتيجة `wifiService()?.getPeerFingerprint(peerID)` ضمن `try` (وعند التقاط أي `Exception` تكون `null`). [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:199]

```
200:     }
```
> إغلاق نطاق الدالة `getPeerFingerprint`. [app/src/main/java/com/bitchat/android/mesh/UnifiedMeshService.kt:200]
