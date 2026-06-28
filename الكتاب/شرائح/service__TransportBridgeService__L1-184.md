# شريحة — app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt (الأسطر 1–184)

```
1: package com.bitchat.android.service
```
> يُعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.service`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:2]

```
3: import android.util.Log
```
> يستورد (import) الصنف `Log` من `android.util`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:3]

```
4: import com.bitchat.android.model.RoutedPacket
```
> يستورد الصنف الحزمة-الموجَّهة (RoutedPacket) من `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:4]

```
5: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف حزمة-بِت-شات (BitchatPacket) من `com.bitchat.android.protocol`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:5]

```
6: import com.bitchat.android.util.toHexString
```
> يستورد الدالة التحويل-إلى-نص-ستّ-عشري (toHexString) من `com.bitchat.android.util`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:6]

```
7: import java.security.MessageDigest
```
> يستورد الصنف ملخّص-الرسالة (MessageDigest) من `java.security`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:7]

```
8: import java.util.Collections
```
> يستورد الصنف `Collections` من `java.util`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:8]

```
9: import java.util.LinkedHashMap
```
> يستورد الصنف الخريطة-المرتّبة-بالربط (LinkedHashMap) من `java.util`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:9]

```
10: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف الخريطة-المتزامنة (ConcurrentHashMap) من `java.util.concurrent`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:11]

```
12: /**
```
> بداية تعليق توثيقي (block comment). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:12]

```
13:  * Central bridge for routing packets between different transport layers
```
> تعليق: جسر مركزي لتوجيه الحزم بين طبقات نقل مختلفة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:13]

```
14:  * (e.g., Bluetooth LE <-> Wi-Fi Aware).
```
> تعليق: (مثلاً، بلوتوث منخفض الطاقة <-> واي-فاي أوير). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:14]

```
15:  * 
```
> تعليق: سطر فارغ داخل التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:15]

```
16:  * Allows a packet received on one transport to be seamlessly relayed
```
> تعليق: يسمح بأن تُمرَّر حزمة استُقبلت على نقل واحد بسلاسة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:16]

```
17:  * to all other active transports, effectively bridging separate meshes.
```
> تعليق: إلى كل وسائل النقل النشطة الأخرى، فيجسر فعلياً شبكات شبكية منفصلة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:17]

```
18:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:18]

```
19: object TransportBridgeService {
```
> يعرّف كائناً مفرداً (object) باسم خدمة-جسر-النقل (TransportBridgeService) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:19]

```
20:     private const val TAG = "TransportBridgeService"
```
> يعرّف ثابتاً خاصاً (private const) باسم `TAG` وقيمته النصّية `"TransportBridgeService"`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:20]

```
21:     private const val MAX_SEEN_PACKETS = 4096
```
> يعرّف ثابتاً خاصاً باسم الحدّ-الأقصى-للحزم-المرئية (MAX_SEEN_PACKETS) وقيمته `4096`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:21]

```
22:     private const val SEEN_PACKET_TTL_MS = 5 * 60 * 1000L
```
> يعرّف ثابتاً خاصاً باسم عمر-الحزمة-المرئية-بالمللي-ثانية (SEEN_PACKET_TTL_MS) وقيمته `5 * 60 * 1000L` (٣٠٠٠٠٠ ميلي ثانية، من نوع Long). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:22]

```
23: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:23]

```
24:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:24]

```
25:      * Interface that any transport layer (BLE, WiFi, Tor, etc.) must implement
```
> تعليق: واجهة يجب أن تنفّذها أيّ طبقة نقل (BLE، WiFi، Tor، إلخ). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:25]

```
26:      * to receive bridged packets.
```
> تعليق: لتستقبل الحزم المجسورة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:26]

```
27:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:27]

```
28:     interface TransportLayer {
```
> يعرّف واجهة (interface) باسم طبقة-النقل (TransportLayer) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:28]

```
29:         /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:29]

```
30:          * Send a packet out via this transport.
```
> تعليق: أرسِل حزمة عبر وسيلة النقل هذه. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:30]

```
31:          */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:31]

```
32:         fun send(packet: RoutedPacket)
```
> يعلن دالة مجرّدة باسم إرسال (send) تأخذ معاملاً `packet` من نوع RoutedPacket بلا جسم. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:33]

```
34:         /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:34]

```
35:          * Send a packet to a specific peer via this transport (optional).
```
> تعليق: أرسِل حزمة إلى نِدّ محدّد عبر وسيلة النقل هذه (اختياري). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:35]

```
36:          */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:36]

```
37:         fun sendToPeer(peerID: String, packet: BitchatPacket) { }
```
> يعرّف دالة باسم إرسال-إلى-النِّدّ (sendToPeer) تأخذ معرّف-النِّدّ (peerID) نصّاً و`packet` من نوع BitchatPacket، بجسم فارغ (تنفيذ افتراضي لا يفعل شيئاً). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:37]

```
38:     }
```
> إغلاق نطاق (نهاية الواجهة TransportLayer). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:38]

```
39: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:39]

```
40:     private val transports = ConcurrentHashMap<String, TransportLayer>()
```
> يعرّف متغيّراً ثابتاً خاصاً باسم وسائل-النقل (transports) ويسنده إلى خريطة متزامنة جديدة مفاتيحها نصوص وقيمها من نوع TransportLayer. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:40]

```
41:     private val seenPackets = Collections.synchronizedMap(
```
> يعرّف متغيّراً ثابتاً خاصاً باسم الحزم-المرئية (seenPackets) ويسنده إلى ناتج استدعاء `Collections.synchronizedMap` (بدء تمرير الوسيط). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:41]

```
42:         object : LinkedHashMap<String, Long>(MAX_SEEN_PACKETS, 0.75f, true) {
```
> ينشئ كائناً مجهولاً يرث LinkedHashMap بمفاتيح نصّية وقيم Long، بمعاملات سعة `MAX_SEEN_PACKETS` وعامل تحميل `0.75f` وترتيب الوصول `true`، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:42]

```
43:             override fun removeEldestEntry(eldest: MutableMap.MutableEntry<String, Long>?): Boolean {
```
> يعيد تعريف (override) الدالة إزالة-أقدم-مدخل (removeEldestEntry) التي تأخذ `eldest` من نوع مدخل قابل للتعديل (يقبل القيمة الفارغة) وتعيد Boolean. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:43]

```
44:                 return size > MAX_SEEN_PACKETS
```
> يعيد نتيجة المقارنة: هل الحجم `size` أكبر من `MAX_SEEN_PACKETS`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:44]

```
45:             }
```
> إغلاق نطاق (نهاية الدالة removeEldestEntry). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:45]

```
46:         }
```
> إغلاق نطاق (نهاية الكائن المجهول الوارث لـ LinkedHashMap). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:46]

```
47:     )
```
> إغلاق قوس استدعاء `Collections.synchronizedMap`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:47]

```
48: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:48]

```
49:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:49]

```
50:      * Register a transport layer to receive bridged packets.
```
> تعليق: سجّل طبقة نقل لتستقبل الحزم المجسورة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:50]

```
51:      * @param id Unique identifier (e.g., "BLE", "WIFI")
```
> تعليق: @param id معرّف فريد (مثلاً "BLE"، "WIFI"). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:51]

```
52:      * @param layer The transport implementation
```
> تعليق: @param layer تنفيذ النقل. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:52]

```
53:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:53]

```
54:     fun register(id: String, layer: TransportLayer) {
```
> يعرّف دالة باسم تسجيل (register) تأخذ `id` نصّاً و`layer` من نوع TransportLayer، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:54]

```
55:         Log.i(TAG, "Registering transport layer: $id")
```
> يستدعي `Log.i` بالوسم `TAG` ورسالة `"Registering transport layer: $id"` (تتضمّن قيمة `id`). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:55]

```
56:         transports[id] = layer
```
> يسند `layer` إلى الخريطة `transports` عند المفتاح `id`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:56]

```
57:     }
```
> إغلاق نطاق (نهاية الدالة register). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:57]

```
58: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:58]

```
59:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:59]

```
60:      * Unregister a transport layer.
```
> تعليق: ألغِ تسجيل طبقة نقل. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:60]

```
61:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:61]

```
62:     fun unregister(id: String) {
```
> يعرّف دالة باسم إلغاء-التسجيل (unregister) تأخذ `id` نصّاً، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:62]

```
63:         Log.i(TAG, "Unregistering transport layer: $id")
```
> يستدعي `Log.i` بالوسم `TAG` ورسالة `"Unregistering transport layer: $id"` (تتضمّن قيمة `id`). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:63]

```
64:         transports.remove(id)
```
> يستدعي `remove` على الخريطة `transports` لإزالة المدخل ذي المفتاح `id`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:64]

```
65:     }
```
> إغلاق نطاق (نهاية الدالة unregister). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:65]

```
66: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:66]

```
67:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:67]

```
68:      * Broadcast a packet from a specific source transport to ALL other registered transports.
```
> تعليق: بُثّ حزمة من وسيلة نقل مصدر محدّدة إلى كل وسائل النقل المسجّلة الأخرى. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:68]

```
69:      * 
```
> تعليق: سطر فارغ داخل التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:69]

```
70:      * @param sourceId The ID of the transport initiating the broadcast (e.g., "BLE").
```
> تعليق: @param sourceId معرّف وسيلة النقل التي تبدأ البثّ (مثلاً "BLE"). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:70]

```
71:      *                 The packet will NOT be sent back to this source.
```
> تعليق: لن تُعاد الحزمة إلى هذا المصدر. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:71]

```
72:      * @param packet The packet to bridge.
```
> تعليق: @param packet الحزمة المراد جسرها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:72]

```
73:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:73]

```
74:     fun broadcast(sourceId: String, packet: RoutedPacket) {
```
> يعرّف دالة باسم بثّ (broadcast) تأخذ معرّف-المصدر (sourceId) نصّاً و`packet` من نوع RoutedPacket، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:74]

```
75:         val targets = transports.filterKeys { it != sourceId }
```
> يعرّف متغيّراً ثابتاً باسم الأهداف (targets) ويسنده إلى تصفية `transports` على المفاتيح التي لا تساوي `sourceId`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:75]

```
76:         if (targets.isEmpty()) return
```
> إذا كانت `targets` فارغة فإنه يرجع (return) من الدالة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:76]

```
77:         val forwardedPacket = prepareForwardedPacket("broadcast", packet.packet) ?: return
```
> يعرّف متغيّراً ثابتاً باسم الحزمة-المُمرَّرة (forwardedPacket) ويسنده إلى ناتج `prepareForwardedPacket` بالوسيط `"broadcast"` و`packet.packet`؛ وإن كان الناتج null فإنه يرجع من الدالة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:77]

```
78:         val forwarded = packet.copy(packet = forwardedPacket)
```
> يعرّف متغيّراً ثابتاً باسم `forwarded` ويسنده إلى نسخة من `packet` بحقل `packet` مستبدلاً بقيمة `forwardedPacket`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:78]

```
79: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:79]

```
80:         // Log.v(TAG, "Bridging packet type ${packet.packet.type} from $sourceId to ${targets.keys}")
```
> تعليق (سطري، معطّل): `Log.v(TAG, "Bridging packet type ${packet.packet.type} from $sourceId to ${targets.keys}")`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:80]

```
81:         
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:81]

```
82:         targets.forEach { (id, layer) ->
```
> يستدعي `forEach` على `targets` مفكّكاً كلّ مدخل إلى `id` و`layer` (بدء جسم اللامدا). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:82]

```
83:             try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:83]

```
84:                 layer.send(forwarded)
```
> يستدعي `send` على `layer` بالوسيط `forwarded`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:84]

```
85:             } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويفتح كتلة التقاط (catch) للاستثناء `e` من نوع Exception. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:85]

```
86:                 Log.e(TAG, "Failed to bridge packet to $id: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ورسالة `"Failed to bridge packet to $id: ${e.message}"` (تتضمّن `id` ورسالة الاستثناء). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:86]

```
87:             }
```
> إغلاق نطاق (نهاية كتلة catch). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:87]

```
88:         }
```
> إغلاق نطاق (نهاية لامدا forEach). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:88]

```
89:     }
```
> إغلاق نطاق (نهاية الدالة broadcast). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:89]

```
90: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:90]

```
91:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:91]

```
92:      * Send a packet to a specific peer across all other transports.
```
> تعليق: أرسِل حزمة إلى نِدّ محدّد عبر كل وسائل النقل الأخرى. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:92]

```
93:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:93]

```
94:     fun sendToPeer(sourceId: String, peerID: String, packet: BitchatPacket) {
```
> يعرّف دالة باسم إرسال-إلى-النِّدّ (sendToPeer) تأخذ `sourceId` نصّاً و`peerID` نصّاً و`packet` من نوع BitchatPacket، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:94]

```
95:         val targets = transports.filterKeys { it != sourceId }
```
> يعرّف متغيّراً ثابتاً باسم `targets` ويسنده إلى تصفية `transports` على المفاتيح التي لا تساوي `sourceId`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:95]

```
96:         if (targets.isEmpty()) return
```
> إذا كانت `targets` فارغة فإنه يرجع من الدالة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:96]

```
97:         val forwardedPacket = prepareForwardedPacket("peer:$peerID", packet) ?: return
```
> يعرّف متغيّراً ثابتاً باسم `forwardedPacket` ويسنده إلى ناتج `prepareForwardedPacket` بالوسيط `"peer:$peerID"` و`packet`؛ وإن كان null فإنه يرجع من الدالة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:97]

```
98: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:98]

```
99:         targets.forEach { (id, layer) ->
```
> يستدعي `forEach` على `targets` مفكّكاً كلّ مدخل إلى `id` و`layer` (بدء جسم اللامدا). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:99]

```
100:             try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:100]

```
101:                 layer.sendToPeer(peerID, forwardedPacket)
```
> يستدعي `sendToPeer` على `layer` بالوسيطين `peerID` و`forwardedPacket`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:101]

```
102:             } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويفتح كتلة التقاط للاستثناء `e` من نوع Exception. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:102]

```
103:                 Log.e(TAG, "Failed to bridge unicast packet to $id: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ورسالة `"Failed to bridge unicast packet to $id: ${e.message}"` (تتضمّن `id` ورسالة الاستثناء). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:103]

```
104:             }
```
> إغلاق نطاق (نهاية كتلة catch). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:104]

```
105:         }
```
> إغلاق نطاق (نهاية لامدا forEach). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:105]

```
106:     }
```
> إغلاق نطاق (نهاية الدالة sendToPeer). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:106]

```
107: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:107]

```
108:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:108]

```
109:      * Send a locally originated packet to every active transport without applying relay TTL
```
> تعليق: أرسِل حزمة نشأت محلّياً إلى كل وسيلة نقل نشطة دون تطبيق معالجة عمر-التمرير (TTL). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:109]

```
110:      * handling. This is used for neighbor-only packets such as REQUEST_SYNC whose TTL is
```
> تعليق: تُستخدم للحزم الموجّهة للجيران فقط مثل REQUEST_SYNC التي عمرها (TTL). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:110]

```
111:      * intentionally zero on the first radio hop.
```
> تعليق: صفر عمداً عند أول قفزة لاسلكية. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:111]

```
112:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:112]

```
113:     fun broadcastFromLocal(packet: RoutedPacket) {
```
> يعرّف دالة باسم بثّ-من-المحلّي (broadcastFromLocal) تأخذ `packet` من نوع RoutedPacket، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:113]

```
114:         val targets = transports.toMap()
```
> يعرّف متغيّراً ثابتاً باسم `targets` ويسنده إلى نسخة خريطة من `transports` عبر `toMap`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:114]

```
115:         if (targets.isEmpty()) return
```
> إذا كانت `targets` فارغة فإنه يرجع من الدالة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:115]

```
116: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:116]

```
117:         targets.forEach { (id, layer) ->
```
> يستدعي `forEach` على `targets` مفكّكاً كلّ مدخل إلى `id` و`layer` (بدء جسم اللامدا). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:117]

```
118:             try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:118]

```
119:                 layer.send(packet)
```
> يستدعي `send` على `layer` بالوسيط `packet`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:119]

```
120:             } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويفتح كتلة التقاط للاستثناء `e` من نوع Exception. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:120]

```
121:                 Log.e(TAG, "Failed to send local packet to $id: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ورسالة `"Failed to send local packet to $id: ${e.message}"` (تتضمّن `id` ورسالة الاستثناء). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:121]

```
122:             }
```
> إغلاق نطاق (نهاية كتلة catch). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:122]

```
123:         }
```
> إغلاق نطاق (نهاية لامدا forEach). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:123]

```
124:     }
```
> إغلاق نطاق (نهاية الدالة broadcastFromLocal). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:124]

```
125: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:125]

```
126:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:126]

```
127:      * Send a locally originated packet directly to a peer on every active transport.
```
> تعليق: أرسِل حزمة نشأت محلّياً مباشرةً إلى نِدّ على كل وسيلة نقل نشطة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:127]

```
128:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:128]

```
129:     fun sendToPeerFromLocal(peerID: String, packet: BitchatPacket) {
```
> يعرّف دالة باسم إرسال-إلى-النِّدّ-من-المحلّي (sendToPeerFromLocal) تأخذ `peerID` نصّاً و`packet` من نوع BitchatPacket، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:129]

```
130:         val targets = transports.toMap()
```
> يعرّف متغيّراً ثابتاً باسم `targets` ويسنده إلى نسخة خريطة من `transports` عبر `toMap`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:130]

```
131:         if (targets.isEmpty()) return
```
> إذا كانت `targets` فارغة فإنه يرجع من الدالة. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:131]

```
132: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:132]

```
133:         targets.forEach { (id, layer) ->
```
> يستدعي `forEach` على `targets` مفكّكاً كلّ مدخل إلى `id` و`layer` (بدء جسم اللامدا). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:133]

```
134:             try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:134]

```
135:                 layer.sendToPeer(peerID, packet)
```
> يستدعي `sendToPeer` على `layer` بالوسيطين `peerID` و`packet`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:135]

```
136:             } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويفتح كتلة التقاط للاستثناء `e` من نوع Exception. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:136]

```
137:                 Log.e(TAG, "Failed to send local peer packet to $id: ${e.message}")
```
> يستدعي `Log.e` بالوسم `TAG` ورسالة `"Failed to send local peer packet to $id: ${e.message}"` (تتضمّن `id` ورسالة الاستثناء). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:137]

```
138:             }
```
> إغلاق نطاق (نهاية كتلة catch). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:138]

```
139:         }
```
> إغلاق نطاق (نهاية لامدا forEach). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:139]

```
140:     }
```
> إغلاق نطاق (نهاية الدالة sendToPeerFromLocal). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:140]

```
141: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:141]

```
142:     private fun prepareForwardedPacket(kind: String, packet: BitchatPacket): BitchatPacket? {
```
> يعرّف دالة خاصة باسم تحضير-الحزمة-المُمرَّرة (prepareForwardedPacket) تأخذ `kind` نصّاً و`packet` من نوع BitchatPacket وتعيد BitchatPacket يقبل null، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:142]

```
143:         if (packet.ttl == 0u.toUByte()) {
```
> يفتح شرطاً: إذا كان حقل `ttl` للحزمة يساوي `0u.toUByte()` (صفر كبايت غير موقّع). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:143]

```
144:             Log.d(TAG, "Dropping bridged packet type ${packet.type}: TTL expired")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة `"Dropping bridged packet type ${packet.type}: TTL expired"` (تتضمّن نوع الحزمة). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:144]

```
145:             return null
```
> يعيد null. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:145]

```
146:         }
```
> إغلاق نطاق (نهاية كتلة if عند انتهاء العمر). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:146]

```
147: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:147]

```
148:         val key = "$kind:${logicalPacketId(packet)}"
```
> يعرّف متغيّراً ثابتاً باسم المفتاح (key) ويسنده إلى نصّ مركّب من `kind` ونقطتين ونتيجة `logicalPacketId(packet)`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:148]

```
149:         val now = System.currentTimeMillis()
```
> يعرّف متغيّراً ثابتاً باسم الآن (now) ويسنده إلى الوقت الحالي بالمللي ثانية عبر `System.currentTimeMillis()`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:149]

```
150:         synchronized(seenPackets) {
```
> يدخل كتلة متزامنة (synchronized) على القفل `seenPackets`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:150]

```
151:             pruneSeen(now)
```
> يستدعي `pruneSeen` بالوسيط `now`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:151]

```
152:             val previous = seenPackets[key]
```
> يعرّف متغيّراً ثابتاً باسم السابق (previous) ويسنده إلى قيمة `seenPackets` عند المفتاح `key`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:152]

```
153:             if (previous != null && now - previous < SEEN_PACKET_TTL_MS) {
```
> يفتح شرطاً: إذا كان `previous` غير null والفرق `now - previous` أصغر من `SEEN_PACKET_TTL_MS`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:153]

```
154:                 Log.d(TAG, "Dropping duplicate bridged packet type ${packet.type}")
```
> يستدعي `Log.d` بالوسم `TAG` ورسالة `"Dropping duplicate bridged packet type ${packet.type}"` (تتضمّن نوع الحزمة). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:154]

```
155:                 return null
```
> يعيد null. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:155]

```
156:             }
```
> إغلاق نطاق (نهاية كتلة if للتكرار). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:156]

```
157:             seenPackets[key] = now
```
> يسند `now` إلى `seenPackets` عند المفتاح `key`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:157]

```
158:         }
```
> إغلاق نطاق (نهاية الكتلة المتزامنة). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:158]

```
159: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:159]

```
160:         return packet.copy(ttl = (packet.ttl - 1u).toUByte())
```
> يعيد نسخة من `packet` بحقل `ttl` مساوياً `(packet.ttl - 1u).toUByte()` (العمر منقوصاً واحداً ككبايت غير موقّع). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:160]

```
161:     }
```
> إغلاق نطاق (نهاية الدالة prepareForwardedPacket). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:161]

```
162: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:162]

```
163:     private fun pruneSeen(now: Long) {
```
> يعرّف دالة خاصة باسم تنقية-المرئية (pruneSeen) تأخذ `now` من نوع Long، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:163]

```
164:         val iterator = seenPackets.entries.iterator()
```
> يعرّف متغيّراً ثابتاً باسم المُكرِّر (iterator) ويسنده إلى مُكرِّر مداخل `seenPackets`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:164]

```
165:         while (iterator.hasNext()) {
```
> يفتح حلقة `while` تستمرّ طالما لدى `iterator` عنصر تالٍ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:165]

```
166:             val entry = iterator.next()
```
> يعرّف متغيّراً ثابتاً باسم المدخل (entry) ويسنده إلى العنصر التالي من `iterator`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:166]

```
167:             if (now - entry.value > SEEN_PACKET_TTL_MS) {
```
> يفتح شرطاً: إذا كان الفرق `now - entry.value` أكبر من `SEEN_PACKET_TTL_MS`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:167]

```
168:                 iterator.remove()
```
> يستدعي `remove` على `iterator` لإزالة المدخل الحالي. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:168]

```
169:             }
```
> إغلاق نطاق (نهاية كتلة if). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:169]

```
170:         }
```
> إغلاق نطاق (نهاية حلقة while). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:170]

```
171:     }
```
> إغلاق نطاق (نهاية الدالة pruneSeen). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:171]

```
172: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:172]

```
173:     private fun logicalPacketId(packet: BitchatPacket): String {
```
> يعرّف دالة خاصة باسم المعرّف-المنطقي-للحزمة (logicalPacketId) تأخذ `packet` من نوع BitchatPacket وتعيد String، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:173]

```
174:         val digest = MessageDigest.getInstance("SHA-256")
```
> يعرّف متغيّراً ثابتاً باسم الملخّص (digest) ويسنده إلى نسخة MessageDigest بخوارزمية `"SHA-256"`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:174]

```
175:         digest.update(packet.type.toByte())
```
> يستدعي `update` على `digest` بقيمة `packet.type.toByte()` (نوع الحزمة ككبايت). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:175]

```
176:         digest.update(packet.senderID)
```
> يستدعي `update` على `digest` بقيمة `packet.senderID` (معرّف المرسِل). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:176]

```
177:         packet.recipientID?.let { digest.update(it) }
```
> إذا كان `packet.recipientID` (معرّف المستلِم) غير null يستدعي `digest.update` به. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:177]

```
178:         digest.update(packet.timestamp.toString().toByteArray(Charsets.UTF_8))
```
> يستدعي `update` على `digest` بمصفوفة بايتات نصّ `packet.timestamp` بترميز UTF-8. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:178]

```
179:         digest.update(packet.payload)
```
> يستدعي `update` على `digest` بقيمة `packet.payload` (الحمولة). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:179]

```
180:         packet.route?.forEach { digest.update(it) }
```
> إذا كان `packet.route` (المسار) غير null يكرّر على عناصره ويستدعي `digest.update` لكلّ عنصر. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:180]

```
181:         packet.signature?.let { digest.update(it) }
```
> إذا كان `packet.signature` (التوقيع) غير null يستدعي `digest.update` به. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:181]

```
182:         return digest.digest().toHexString()
```
> يعيد ناتج `digest.digest()` محوّلاً إلى نصّ ستّ عشري عبر `toHexString`. [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:182]

```
183:     }
```
> إغلاق نطاق (نهاية الدالة logicalPacketId). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:183]

```
184: }
```
> إغلاق نطاق (نهاية الكائن TransportBridgeService). [app/src/main/java/com/bitchat/android/service/TransportBridgeService.kt:184]
