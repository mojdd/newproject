# شريحة — app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:1]

```
2: import com.bitchat.android.protocol.MessageType
```
> يستورد (import) النوع MessageType من حزمة البروتوكول com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:2]

```
3: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف Log من android.util للتسجيل. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:4]

```
5: import com.bitchat.android.model.RoutedPacket
```
> يستورد النوع RoutedPacket (الحزمة الموجَّهة) من حزمة النماذج com.bitchat.android.model. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:5]

```
6: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد النوع BitchatPacket (حزمة بِتشات) من حزمة البروتوكول. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:6]

```
7: import com.bitchat.android.util.toHexString
```
> يستورد الدالة الموسِّعة toHexString (التحويل إلى نص ست عشري) من حزمة الأدوات com.bitchat.android.util. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:7]

```
8: import kotlinx.coroutines.*
```
> يستورد كل عناصر حزمة الكوروتينات kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:8]

```
9: import kotlin.random.Random
```
> يستورد الصنف Random (العشوائية) من kotlin.random. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:9]

```
10: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:10]

```
11: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:11]

```
12:  * Centralized packet relay management
```
> تعليق: إدارة مركزية لترحيل الحزم. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:12]

```
13:  * 
```
> تعليق: سطر فارغ ضمن كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:13]

```
14:  * This class handles all relay decisions and logic for bitchat packets.
```
> تعليق: هذا الصنف يتولّى كل قرارات ومنطق الترحيل لحزم بِتشات. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:14]

```
15:  * All packets that aren't specifically addressed to us get processed here.
```
> تعليق: كل الحزم غير الموجَّهة إلينا تحديداً تُعالَج هنا. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:15]

```
16:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:16]

```
17: class PacketRelayManager(private val myPeerID: String) {
```
> يعرّف الصنف PacketRelayManager (مدير ترحيل الحزم) بمُنشئ يأخذ مُعطى خاصاً للقراءة فقط myPeerID (معرّف النِّد الخاص بي) من نوع نصي String. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:17]

```
18:     private val debugManager by lazy { try { com.bitchat.android.ui.debug.DebugSettingsManager.getInstance() } catch (e: Exception) { null } }
```
> يعرّف خاصية خاصة debugManager (مدير التنقيح) تُهيَّأ بكسل (lazy) باستدعاء DebugSettingsManager.getInstance() داخل try، وتُعيد null عند حدوث استثناء. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:18]

```
19:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:19]

```
20:     companion object {
```
> يفتح كائن المرافقة (companion object) للصنف. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:20]

```
21:         private const val TAG = "PacketRelayManager"
```
> يعرّف ثابتاً خاصاً TAG (وسم التسجيل) بالقيمة النصية "PacketRelayManager". [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:21]

```
22:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:22]

```
23:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:23]

```
24:     private fun isRelayEnabled(): Boolean = try {
```
> يعرّف دالة خاصة isRelayEnabled (هل الترحيل مفعَّل) تُعيد قيمة منطقية Boolean، وجسمها تعبير try يبدأ هنا. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:24]

```
25:         com.bitchat.android.ui.debug.DebugSettingsManager.getInstance().packetRelayEnabled.value
```
> يقرأ القيمة value من الخاصية packetRelayEnabled (تفعيل ترحيل الحزم) العائدة من DebugSettingsManager.getInstance(). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:25]

```
26:     } catch (_: Exception) { true }
```
> يلتقط أي استثناء Exception (دون تسمية المتغيّر) ويُعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:27]

```
28:     // Logging moved to BluetoothPacketBroadcaster per actual transmission target
```
> تعليق: نُقل التسجيل إلى BluetoothPacketBroadcaster بحسب هدف الإرسال الفعلي. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:28]

```
29:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:29]

```
30:     // Delegate for callbacks
```
> تعليق: المفوَّض (delegate) لاستدعاءات الرجوع. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:30]

```
31:     var delegate: PacketRelayManagerDelegate? = null
```
> يعرّف خاصية متغيّرة delegate (المفوَّض) من نوع PacketRelayManagerDelegate القابل للعدم، قيمتها الابتدائية null. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:31]

```
32:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:32]

```
33:     // Coroutines
```
> تعليق: الكوروتينات. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:33]

```
34:     private val relayScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يعرّف خاصية خاصة للقراءة فقط relayScope (نطاق الترحيل) كـ CoroutineScope مكوَّن من مُرسِل الإدخال/الإخراج Dispatchers.IO مضافاً إليه SupervisorJob (مهمة مشرفة). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:34]

```
35:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:35]

```
36:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:36]

```
37:      * Main entry point for relay decisions
```
> تعليق: نقطة الدخول الرئيسية لقرارات الترحيل. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:37]

```
38:      * Only packets that aren't specifically addressed to us should be passed here
```
> تعليق: يجب أن تُمرَّر هنا فقط الحزم غير الموجَّهة إلينا تحديداً. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:38]

```
39:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:39]

```
40:     suspend fun handlePacketRelay(routed: RoutedPacket) {
```
> يعرّف دالة معلَّقة (suspend) باسم handlePacketRelay (معالجة ترحيل الحزمة) تأخذ مُعطى routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:40]

```
41:         val packet = routed.packet
```
> يعرّف متغيّراً للقراءة فقط packet ويسنده إلى الحقل packet من الكائن routed. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:41]

```
42:         val peerID = routed.peerID ?: "unknown"
```
> يعرّف متغيّراً للقراءة فقط peerID ويسنده إلى routed.peerID، وإن كان عدماً فإلى النص "unknown". [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:42]

```
43:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:43]

```
44:         Log.d(TAG, "Evaluating relay for packet type ${packet.type} from ${peerID} (TTL: ${packet.ttl})")
```
> يستدعي Log.d بالوسم TAG لتسجيل رسالة تنقيح: تقييم الترحيل لحزمة من النوع packet.type من peerID مع قيمة TTL هي packet.ttl. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:44]

```
45:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:45]

```
46:         // Double-check this packet isn't addressed to us
```
> تعليق: تحقّق مزدوج من أن هذه الحزمة غير موجَّهة إلينا. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:46]

```
47:         if (isPacketAddressedToMe(packet)) {
```
> شرط: إذا أعادت الدالة isPacketAddressedToMe(packet) قيمة صحيحة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:47]

```
48:             Log.d(TAG, "Packet addressed to us, skipping relay")
```
> يستدعي Log.d لتسجيل رسالة تنقيح: الحزمة موجَّهة إلينا، تخطّي الترحيل. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:48]

```
49:             return
```
> يُعيد من الدالة (خروج بلا قيمة). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:49]

```
50:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:50]

```
51:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:51]

```
52:         // Skip our own packets
```
> تعليق: تخطّي حزمنا الخاصة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:52]

```
53:         if (peerID == myPeerID) {
```
> شرط: إذا كان peerID يساوي myPeerID. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:53]

```
54:             Log.d(TAG, "Packet from ourselves, skipping relay")
```
> يستدعي Log.d لتسجيل رسالة تنقيح: الحزمة من أنفسنا، تخطّي الترحيل. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:54]

```
55:             return
```
> يُعيد من الدالة (خروج بلا قيمة). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:55]

```
56:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:56]

```
57:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:57]

```
58:         // Check TTL and decrement
```
> تعليق: فحص TTL (مدة البقاء) وإنقاصها. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:58]

```
59:         if (packet.ttl == 0u.toUByte()) {
```
> شرط: إذا كانت packet.ttl تساوي القيمة صفر مُحوَّلة إلى بايت غير مُوقَّع UByte. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:59]

```
60:             Log.d(TAG, "TTL expired, not relaying packet")
```
> يستدعي Log.d لتسجيل رسالة تنقيح: انتهت مدة البقاء، لن تُرحَّل الحزمة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:60]

```
61:             return
```
> يُعيد من الدالة (خروج بلا قيمة). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:61]

```
62:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:62]

```
63:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:63]

```
64:         // Decrement TTL by 1
```
> تعليق: إنقاص TTL بمقدار واحد. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:64]

```
65:         val relayPacket = packet.copy(ttl = (packet.ttl - 1u).toUByte())
```
> يعرّف متغيّراً للقراءة فقط relayPacket (حزمة الترحيل) بنسخ packet مع ضبط الحقل ttl إلى (packet.ttl ناقص واحد) محوَّلاً إلى UByte. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:65]

```
66:         Log.d(TAG, "Decremented TTL from ${packet.ttl} to ${relayPacket.ttl}")
```
> يستدعي Log.d لتسجيل رسالة تنقيح: إنقاص TTL من packet.ttl إلى relayPacket.ttl. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:66]

```
67:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:67]

```
68:         // Source-based routing: if route is set and includes us, try targeted next-hop forwarding
```
> تعليق: توجيه مبني على المصدر: إذا كان المسار مضبوطاً ويشملنا، جرّب إعادة التوجيه إلى القفزة التالية المحدَّدة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:68]

```
69:         val route = relayPacket.route
```
> يعرّف متغيّراً للقراءة فقط route (المسار) ويسنده إلى الحقل route من relayPacket. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:69]

```
70:         if (!route.isNullOrEmpty()) {
```
> شرط: إذا لم يكن route عدماً ولا فارغاً. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:70]

```
71:             // Check for duplicate hops to prevent routing loops
```
> تعليق: فحص القفزات المكرَّرة لمنع حلقات التوجيه. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:71]

```
72:             if (route.map { it.toHexString() }.toSet().size < route.size) {
```
> شرط: إذا كان حجم مجموعة (set) القيم الناتجة عن تحويل كل عنصر إلى نص ست عشري أقل من حجم route (أي يوجد تكرار). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:72]

```
73:                 Log.w(TAG, "Packet with duplicate hops dropped")
```
> يستدعي Log.w لتسجيل تحذير: أُسقطت حزمة ذات قفزات مكرَّرة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:73]

```
74:                 return
```
> يُعيد من الدالة (خروج بلا قيمة). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:74]

```
75:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:75]

```
76:             val myIdBytes = hexStringToPeerBytes(myPeerID)
```
> يعرّف متغيّراً للقراءة فقط myIdBytes (بايتات معرّفي) بنتيجة استدعاء الدالة hexStringToPeerBytes(myPeerID). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:76]

```
77:             val index = route.indexOfFirst { it.contentEquals(myIdBytes) }
```
> يعرّف متغيّراً للقراءة فقط index (الفهرس) بأول موضع في route يتطابق محتواه مع myIdBytes عبر contentEquals. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:77]

```
78:             if (index >= 0) {
```
> شرط: إذا كان index أكبر من أو يساوي صفراً (أي وُجِد). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:78]

```
79:                 val nextHopIdHex: String? = run {
```
> يعرّف متغيّراً للقراءة فقط nextHopIdHex (معرّف القفزة التالية ست عشري) من نوع نصي قابل للعدم، قيمته ناتج كتلة run. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:79]

```
80:                     val nextIndex = index + 1
```
> يعرّف متغيّراً للقراءة فقط nextIndex (الفهرس التالي) بقيمة index زائد واحد. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:80]

```
81:                     if (nextIndex < route.size) {
```
> شرط: إذا كان nextIndex أصغر من حجم route. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:81]

```
82:                         route[nextIndex].toHexString()
```
> يُرجع للكتلة العنصر عند nextIndex من route محوَّلاً إلى نص ست عشري. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:82]

```
83:                     } else {
```
> وإلّا (الفرع البديل للشرط). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:83]

```
84:                         // We are the last intermediate; try final recipient as next hop
```
> تعليق: نحن الوسيط الأخير؛ جرّب المستلِم النهائي كقفزة تالية. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:84]

```
85:                         relayPacket.recipientID?.toHexString()
```
> يُرجع للكتلة الحقل recipientID من relayPacket محوَّلاً إلى نص ست عشري (أو عدم إن كان recipientID عدماً). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:85]

```
86:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:86]

```
87:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:87]

```
88:                 if (nextHopIdHex != null) {
```
> شرط: إذا لم يكن nextHopIdHex عدماً. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:88]

```
89:                     val success = try { delegate?.sendToPeer(nextHopIdHex, RoutedPacket(relayPacket, peerID, routed.relayAddress)) } catch (_: Exception) { false } ?: false
```
> يعرّف متغيّراً للقراءة فقط success (النجاح) باستدعاء delegate?.sendToPeer مع nextHopIdHex وكائن RoutedPacket مبني من relayPacket وpeerID وrouted.relayAddress داخل try، وعند الاستثناء أو العدم تكون القيمة false. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:89]

```
90:                     if (success) {
```
> شرط: إذا كان success صحيحاً. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:90]

```
91:                         Log.i(TAG, "📦 Source-route relay: ${peerID.take(8)} -> ${nextHopIdHex.take(8)} (type ${'$'}{packet.type}, TTL ${'$'}{relayPacket.ttl})")
```
> يستدعي Log.i لتسجيل معلومة: ترحيل بتوجيه المصدر من أول ثمانية محارف من peerID إلى أول ثمانية محارف من nextHopIdHex، مع نوع packet.type وTTL هي relayPacket.ttl. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:91]

```
92:                         return
```
> يُعيد من الدالة (خروج بلا قيمة). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:92]

```
93:                     } else {
```
> وإلّا (الفرع البديل للشرط). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:93]

```
94:                         Log.w(TAG, "Source-route next hop ${nextHopIdHex.take(8)} not directly connected; falling back to broadcast")
```
> يستدعي Log.w لتسجيل تحذير: القفزة التالية (أول ثمانية محارف من nextHopIdHex) غير متّصلة مباشرة؛ يجري التراجع إلى البث. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:94]

```
95:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:95]

```
96:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:96]

```
97:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:97]

```
98:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:98]

```
99: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:99]

```
100:         // Apply relay logic based on packet type and debug switch
```
> تعليق: تطبيق منطق الترحيل بناءً على نوع الحزمة ومفتاح التنقيح. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:100]

```
101:         val shouldRelay = isRelayEnabled() && shouldRelayPacket(relayPacket, peerID)
```
> يعرّف متغيّراً للقراءة فقط shouldRelay (هل ينبغي الترحيل) بحاصل العطف المنطقي بين isRelayEnabled() ونتيجة shouldRelayPacket(relayPacket, peerID). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:101]

```
102:         if (shouldRelay) {
```
> شرط: إذا كان shouldRelay صحيحاً. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:102]

```
103:             relayPacket(RoutedPacket(relayPacket, peerID, routed.relayAddress))
```
> يستدعي الدالة relayPacket بكائن RoutedPacket مبني من relayPacket وpeerID وrouted.relayAddress. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:103]

```
104:         } else {
```
> وإلّا (الفرع البديل للشرط). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:104]

```
105:             Log.d(TAG, "Relay decision: NOT relaying packet type ${packet.type}")
```
> يستدعي Log.d لتسجيل رسالة تنقيح: قرار الترحيل: عدم ترحيل حزمة من النوع packet.type. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:105]

```
106:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:106]

```
107:     }
```
> إغلاق نطاق (نهاية الدالة handlePacketRelay). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:107]

```
108:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:108]

```
109:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:109]

```
110:      * Check if a packet is specifically addressed to us
```
> تعليق: فحص ما إذا كانت الحزمة موجَّهة إلينا تحديداً. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:110]

```
111:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:111]

```
112:     internal fun isPacketAddressedToMe(packet: BitchatPacket): Boolean {
```
> يعرّف دالة داخلية (internal) باسم isPacketAddressedToMe (هل الحزمة موجَّهة إليّ) تأخذ مُعطى packet من نوع BitchatPacket وتُعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:112]

```
113:         val recipientID = packet.recipientID
```
> يعرّف متغيّراً للقراءة فقط recipientID (معرّف المستلِم) ويسنده إلى الحقل recipientID من packet. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:113]

```
114:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:114]

```
115:         // No recipient means broadcast (not addressed to us specifically)
```
> تعليق: غياب المستلِم يعني بثاً (غير موجَّه إلينا تحديداً). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:115]

```
116:         if (recipientID == null) {
```
> شرط: إذا كان recipientID عدماً. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:116]

```
117:             return false
```
> يُعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:117]

```
118:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:118]

```
119:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:119]

```
120:         // Check if it's a broadcast recipient
```
> تعليق: فحص ما إذا كان مستلِم بث. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:120]

```
121:         val broadcastRecipient = delegate?.getBroadcastRecipient()
```
> يعرّف متغيّراً للقراءة فقط broadcastRecipient (مستلِم البث) باستدعاء delegate?.getBroadcastRecipient(). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:121]

```
122:         if (broadcastRecipient != null && recipientID.contentEquals(broadcastRecipient)) {
```
> شرط: إذا لم يكن broadcastRecipient عدماً وكان محتوى recipientID مطابقاً له عبر contentEquals. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:122]

```
123:             return false
```
> يُعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:123]

```
124:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:124]

```
125:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:125]

```
126:         // Check if recipient matches our peer ID
```
> تعليق: فحص ما إذا كان المستلِم يطابق معرّف نِدّنا. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:126]

```
127:         val recipientIDString = recipientID.toHexString()
```
> يعرّف متغيّراً للقراءة فقط recipientIDString (معرّف المستلِم نصاً) بتحويل recipientID إلى نص ست عشري. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:127]

```
128:         return recipientIDString == myPeerID
```
> يُعيد نتيجة المقارنة بين recipientIDString وmyPeerID. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:128]

```
129:     }
```
> إغلاق نطاق (نهاية الدالة isPacketAddressedToMe). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:129]

```
130:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:130]

```
131:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:131]

```
132:      * Determine if we should relay this packet based on type and network conditions
```
> تعليق: تحديد ما إذا كان ينبغي ترحيل هذه الحزمة بناءً على النوع وظروف الشبكة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:132]

```
133:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:133]

```
134:     private fun shouldRelayPacket(packet: BitchatPacket, fromPeerID: String): Boolean {
```
> يعرّف دالة خاصة باسم shouldRelayPacket (هل تُرحَّل الحزمة) تأخذ packet من نوع BitchatPacket وfromPeerID نصياً وتُعيد Boolean. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:134]

```
135:         // Always relay if TTL is high enough (indicates important message)
```
> تعليق: رحِّل دائماً إذا كانت TTL عالية بما يكفي (تشير إلى رسالة مهمة). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:135]

```
136:         if (packet.ttl >= 4u) {
```
> شرط: إذا كانت packet.ttl أكبر من أو تساوي القيمة غير المُوقَّعة أربعة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:136]

```
137:             Log.d(TAG, "High TTL (${packet.ttl}), relaying")
```
> يستدعي Log.d لتسجيل رسالة تنقيح: TTL عالية (قيمتها packet.ttl)، يجري الترحيل. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:137]

```
138:             return true
```
> يُعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:138]

```
139:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:139]

```
140:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:140]

```
141:         // Get network size for adaptive relay probability
```
> تعليق: الحصول على حجم الشبكة لاحتمال ترحيل متكيّف. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:141]

```
142:         val networkSize = delegate?.getNetworkSize() ?: 1
```
> يعرّف متغيّراً للقراءة فقط networkSize (حجم الشبكة) باستدعاء delegate?.getNetworkSize()، وعند العدم القيمة واحد. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:142]

```
143:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:143]

```
144:         // Small networks always relay to ensure connectivity
```
> تعليق: الشبكات الصغيرة تُرحِّل دائماً لضمان الاتصال. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:144]

```
145:         if (networkSize <= 3) {
```
> شرط: إذا كان networkSize أصغر من أو يساوي ثلاثة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:145]

```
146:             Log.d(TAG, "Small network (${networkSize} peers), relaying")
```
> يستدعي Log.d لتسجيل رسالة تنقيح: شبكة صغيرة (عدد الأنداد networkSize)، يجري الترحيل. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:146]

```
147:             return true
```
> يُعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:147]

```
148:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:148]

```
149:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:149]

```
150:         // Apply adaptive relay probability based on network size
```
> تعليق: تطبيق احتمال ترحيل متكيّف بناءً على حجم الشبكة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:150]

```
151:         val relayProb = when {
```
> يعرّف متغيّراً للقراءة فقط relayProb (احتمال الترحيل) بقيمة ناتجة عن تعبير when متعدّد الشروط. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:151]

```
152:             networkSize <= 10 -> 1.0    // Always relay in small networks
```
> فرع when: إذا كان networkSize أصغر من أو يساوي عشرة فالقيمة 1.0؛ تعليق: رحِّل دائماً في الشبكات الصغيرة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:152]

```
153:             networkSize <= 30 -> 0.85   // High probability for medium networks
```
> فرع when: إذا كان networkSize أصغر من أو يساوي ثلاثين فالقيمة 0.85؛ تعليق: احتمال عالٍ للشبكات المتوسطة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:153]

```
154:             networkSize <= 50 -> 0.7    // Moderate probability
```
> فرع when: إذا كان networkSize أصغر من أو يساوي خمسين فالقيمة 0.7؛ تعليق: احتمال معتدل. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:154]

```
155:             networkSize <= 100 -> 0.55  // Lower probability for large networks
```
> فرع when: إذا كان networkSize أصغر من أو يساوي مئة فالقيمة 0.55؛ تعليق: احتمال أدنى للشبكات الكبيرة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:155]

```
156:             else -> 0.4                 // Lowest probability for very large networks
```
> فرع when البديل (else): القيمة 0.4؛ تعليق: أدنى احتمال للشبكات الكبيرة جداً. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:156]

```
157:         }
```
> إغلاق نطاق (نهاية تعبير when). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:157]

```
158:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:158]

```
159:         val shouldRelay = Random.nextDouble() < relayProb
```
> يعرّف متغيّراً للقراءة فقط shouldRelay بنتيجة مقارنة عدد عشري عشوائي من Random.nextDouble() بأنه أصغر من relayProb. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:159]

```
160:         Log.d(TAG, "Network size: ${networkSize}, Relay probability: ${relayProb}, Decision: ${shouldRelay}")
```
> يستدعي Log.d لتسجيل رسالة تنقيح: حجم الشبكة networkSize، احتمال الترحيل relayProb، القرار shouldRelay. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:160]

```
161:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:161]

```
162:         return shouldRelay
```
> يُعيد قيمة shouldRelay. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:162]

```
163:     }
```
> إغلاق نطاق (نهاية الدالة shouldRelayPacket). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:163]

```
164:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:164]

```
165:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:165]

```
166:      * Actually broadcast the packet for relay
```
> تعليق: بثّ الحزمة فعلياً للترحيل. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:166]

```
167:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:167]

```
168:     private fun relayPacket(routed: RoutedPacket) {
```
> يعرّف دالة خاصة باسم relayPacket (ترحيل الحزمة) تأخذ مُعطى routed من نوع RoutedPacket. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:168]

```
169:         Log.d(TAG, "🔄 Relaying packet type ${routed.packet.type} with TTL ${routed.packet.ttl}")
```
> يستدعي Log.d لتسجيل رسالة تنقيح: جارٍ ترحيل حزمة من النوع routed.packet.type مع TTL هي routed.packet.ttl. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:169]

```
170:         delegate?.broadcastPacket(routed)
```
> يستدعي delegate?.broadcastPacket(routed) لبثّ الحزمة عبر المفوَّض إن لم يكن عدماً. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:170]

```
171:     }
```
> إغلاق نطاق (نهاية الدالة relayPacket). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:171]

```
172:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:172]

```
173:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:173]

```
174:      * Get debug information
```
> تعليق: الحصول على معلومات التنقيح. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:174]

```
175:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:175]

```
176:     fun getDebugInfo(): String {
```
> يعرّف دالة عامة باسم getDebugInfo (الحصول على معلومات التنقيح) تُعيد نصاً String. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:176]

```
177:         return buildString {
```
> يُعيد ناتج باني النص buildString الذي يبدأ بلوكه هنا. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:177]

```
178:             appendLine("=== Packet Relay Manager Debug Info ===")
```
> يستدعي appendLine لإلحاق السطر "=== Packet Relay Manager Debug Info ===". [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:178]

```
179:             appendLine("Relay Scope Active: ${relayScope.isActive}")
```
> يستدعي appendLine لإلحاق سطر يبيّن حالة relayScope.isActive (هل نطاق الترحيل نشط). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:179]

```
180:             appendLine("My Peer ID: ${myPeerID}")
```
> يستدعي appendLine لإلحاق سطر يبيّن قيمة myPeerID. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:180]

```
181:             appendLine("Network Size: ${delegate?.getNetworkSize() ?: "unknown"}")
```
> يستدعي appendLine لإلحاق سطر يبيّن حجم الشبكة من delegate?.getNetworkSize()، وعند العدم النص "unknown". [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:181]

```
182:         }
```
> إغلاق نطاق (نهاية كتلة buildString). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:182]

```
183:     }
```
> إغلاق نطاق (نهاية الدالة getDebugInfo). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:183]

```
184:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:184]

```
185:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:185]

```
186:      * Shutdown the relay manager
```
> تعليق: إيقاف مدير الترحيل. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:186]

```
187:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:187]

```
188:     fun shutdown() {
```
> يعرّف دالة عامة باسم shutdown (الإيقاف) بلا مُعطيات. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:188]

```
189:         Log.d(TAG, "Shutting down PacketRelayManager")
```
> يستدعي Log.d لتسجيل رسالة تنقيح: جارٍ إيقاف PacketRelayManager. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:189]

```
190:         relayScope.cancel()
```
> يستدعي relayScope.cancel() لإلغاء نطاق الترحيل. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:190]

```
191:     }
```
> إغلاق نطاق (نهاية الدالة shutdown). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:191]

```
192: }
```
> إغلاق نطاق (نهاية الصنف PacketRelayManager). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:192]

```
193: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:193]

```
194: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:194]

```
195:  * Delegate interface for packet relay manager callbacks
```
> تعليق: واجهة المفوَّض لاستدعاءات رجوع مدير ترحيل الحزم. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:195]

```
196:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:196]

```
197: interface PacketRelayManagerDelegate {
```
> يعرّف واجهة (interface) باسم PacketRelayManagerDelegate (مفوَّض مدير ترحيل الحزم). [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:197]

```
198:     // Network information
```
> تعليق: معلومات الشبكة. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:198]

```
199:     fun getNetworkSize(): Int
```
> يصرّح بدالة مجرَّدة getNetworkSize (الحصول على حجم الشبكة) تُعيد عدداً صحيحاً Int. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:199]

```
200:     fun getBroadcastRecipient(): ByteArray
```
> يصرّح بدالة مجرَّدة getBroadcastRecipient (الحصول على مستلِم البث) تُعيد مصفوفة بايتات ByteArray. [app/src/main/java/com/bitchat/android/mesh/PacketRelayManager.kt:200]
