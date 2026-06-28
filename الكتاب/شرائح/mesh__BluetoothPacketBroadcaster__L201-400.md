# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt (الأسطر 201–400)

```
201:         if (clientTarget != null) {
```
> يفتح شرطاً (if) يتحقّق أنّ الهدف العميل (clientTarget) لا يساوي قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:201]

```
202:             if (writeToDeviceConn(clientTarget, data)) {
```
> يفتح شرطاً يستدعي دالة الكتابة لاتصال الجهاز (writeToDeviceConn) مع الهدف العميل والبيانات (data)، وينفّذ الكتلة إذا أعادت صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:202]

```
203:                 logPacketRelay(typeName, senderPeerID, senderNick, incomingPeer, incomingAddr, targetPeerID, clientTarget.device.address, packet.ttl, packet.version, routeInfo)
```
> يستدعي دالة تسجيل ترحيل الرزمة (logPacketRelay) ممرّراً اسم النوع (typeName) ومعرّف القرين المرسِل (senderPeerID) ولقب المرسِل (senderNick) والقرين الوارد (incomingPeer) والعنوان الوارد (incomingAddr) ومعرّف القرين الهدف (targetPeerID) وعنوان جهاز الهدف العميل وقيمة مدّة الحياة (packet.ttl) ونسخة الرزمة (packet.version) ومعلومات المسار (routeInfo). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:203]

```
204:                 return true
```
> يعيد القيمة صحيح (true). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:204]

```
205:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:205]

```
206:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:206]

```
207: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:207]

```
208:         return false
```
> يعيد القيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:208]

```
209:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:209]

```
210: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:210]

```
211:     
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:211]

```
212:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:212]

```
213:      * Public entry point for broadcasting - submits request to actor for serialization
```
> تعليق: نقطة دخول عامّة للبثّ - تُقدّم الطلب إلى الفاعل (actor) من أجل التسلسل. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:213]

```
214:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:214]

```
215:     fun broadcastSinglePacket(
```
> يعرّف دالة عامّة باسم بثّ رزمة مفردة (broadcastSinglePacket) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:215]

```
216:         routed: RoutedPacket,
```
> يعرّف معاملاً باسم الرزمة الموجّهة (routed) من نوع رزمة موجّهة (RoutedPacket). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:216]

```
217:         gattServer: BluetoothGattServer?,
```
> يعرّف معاملاً باسم خادم جات (gattServer) من نوع خادم بلوتوث جات (BluetoothGattServer) القابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:217]

```
218:         characteristic: BluetoothGattCharacteristic?
```
> يعرّف معاملاً باسم الخاصّية (characteristic) من نوع خاصّية بلوتوث جات (BluetoothGattCharacteristic) القابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:218]

```
219:     ) {
```
> يغلق قائمة المعاملات ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:219]

```
220:         // Submit broadcast request to actor for serialized processing
```
> تعليق: تقديم طلب البثّ إلى الفاعل من أجل المعالجة المتسلسلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:220]

```
221:         broadcasterScope.launch {
```
> يستدعي إطلاق (launch) على نطاق الباثّ (broadcasterScope) ويفتح كتلة الإطلاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:221]

```
222:             try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:222]

```
223:                 broadcasterActor.send(BroadcastRequest(routed, gattServer, characteristic))
```
> يستدعي إرسال (send) على فاعل الباثّ (broadcasterActor) ممرّراً كائن طلب بثّ (BroadcastRequest) منشأً من الرزمة الموجّهة وخادم جات والخاصّية. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:223]

```
224:             } catch (e: Exception) {
```
> يغلق كتلة المحاولة ويفتح كتلة التقاط (catch) لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:224]

```
225:                 Log.w(TAG, "Failed to send broadcast request to actor: ${e.message}")
```
> يستدعي تسجيل تحذير (Log.w) بالوسم (TAG) ونصّ "فشل إرسال طلب البثّ إلى الفاعل" مع رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:225]

```
226:                 // Fallback to direct processing if actor fails
```
> تعليق: الرجوع إلى المعالجة المباشرة إذا فشل الفاعل. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:226]

```
227:                 broadcastSinglePacketInternal(routed, gattServer, characteristic)
```
> يستدعي الدالة الداخلية لبثّ رزمة مفردة (broadcastSinglePacketInternal) ممرّراً الرزمة الموجّهة وخادم جات والخاصّية. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:227]

```
228:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:228]

```
229:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:229]

```
230:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:230]

```
231: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:231]

```
232:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:232]

```
233:      * Targeted send to a specific peer (by peerID) if directly connected.
```
> تعليق: إرسال موجّه إلى قرين محدّد (بمعرّف القرين) إذا كان متّصلاً مباشرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:233]

```
234:      * Returns true if sent to at least one matching connection.
```
> تعليق: يعيد صحيحاً إذا أُرسل إلى اتصال مطابق واحد على الأقلّ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:234]

```
235:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:235]

```
236:     fun sendToPeer(
```
> يعرّف دالة باسم إرسال إلى القرين (sendToPeer) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:236]

```
237:         targetPeerID: String,
```
> يعرّف معاملاً باسم معرّف القرين الهدف (targetPeerID) من نوع نصّ (String). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:237]

```
238:         routed: RoutedPacket,
```
> يعرّف معاملاً باسم الرزمة الموجّهة (routed) من نوع رزمة موجّهة (RoutedPacket). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:238]

```
239:         gattServer: BluetoothGattServer?,
```
> يعرّف معاملاً باسم خادم جات (gattServer) من نوع خادم بلوتوث جات قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:239]

```
240:         characteristic: BluetoothGattCharacteristic?
```
> يعرّف معاملاً باسم الخاصّية (characteristic) من نوع خاصّية بلوتوث جات قابلة لأن تكون فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:240]

```
241:     ): Boolean {
```
> يغلق قائمة المعاملات ويصرّح أنّ الدالة تعيد قيمة منطقية (Boolean) ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:241]

```
242:         if (!hasPeerConnection(targetPeerID)) return false
```
> يعيد القيمة خطأ إذا كانت دالة وجود اتصال بالقرين (hasPeerConnection) للمعرّف الهدف تعيد خطأ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:242]

```
243:         return fragmentingSender.send(routed, "BLE peer ${targetPeerID.take(8)}") { packet ->
```
> يعيد نتيجة استدعاء إرسال (send) على المرسِل المُجزّئ (fragmentingSender) ممرّراً الرزمة الموجّهة ونصّاً "BLE peer" متبوعاً بأوّل ثمانية محارف من معرّف القرين الهدف، ويفتح تعبيراً لمدوياً (lambda) معامله رزمة (packet). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:243]

```
244:             sendSinglePacketToPeer(packet, targetPeerID, gattServer, characteristic)
```
> يستدعي دالة إرسال رزمة مفردة إلى القرين (sendSinglePacketToPeer) ممرّراً الرزمة ومعرّف القرين الهدف وخادم جات والخاصّية. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:244]

```
245:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:245]

```
246:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:246]

```
247:     
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:247]

```
248:     private fun hasPeerConnection(targetPeerID: String): Boolean {
```
> يعرّف دالة خاصّة (private) باسم وجود اتصال بالقرين (hasPeerConnection) تأخذ معرّف القرين الهدف نصّاً وتعيد قيمة منطقية، ويفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:248]

```
249:         val hasServerTarget = connectionTracker.getSubscribedDevices()
```
> يعرّف متغيّراً ثابتاً (val) باسم وجود هدف خادم (hasServerTarget) يبدأ باستدعاء جلب الأجهزة المشتركة (getSubscribedDevices) على متعقّب الاتصال (connectionTracker). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:249]

```
250:             .any { connectionTracker.addressPeerMap[it.address] == targetPeerID }
```
> يطبّق الدالة "أيّ" (any) التي تتحقّق أنّ خريطة عنوان-قرين (addressPeerMap) عند عنوان العنصر تساوي معرّف القرين الهدف. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:250]

```
251:         if (hasServerTarget) return true
```
> يعيد صحيحاً إذا كان وجود هدف خادم صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:251]

```
252: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:252]

```
253:         return connectionTracker.getConnectedDevices().values
```
> يعيد نتيجة استدعاء قيم (values) من جلب الأجهزة المتصلة (getConnectedDevices) على متعقّب الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:253]

```
254:             .any { connectionTracker.addressPeerMap[it.device.address] == targetPeerID }
```
> يطبّق الدالة "أيّ" (any) التي تتحقّق أنّ خريطة عنوان-قرين عند عنوان جهاز العنصر تساوي معرّف القرين الهدف. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:254]

```
255:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:255]

```
256:     
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:256]

```
257:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:257]

```
258:      * Internal broadcast implementation - runs in serialized actor context
```
> تعليق: تنفيذ البثّ الداخلي - يعمل في سياق الفاعل المتسلسل. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:258]

```
259:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:259]

```
260:     private suspend fun broadcastSinglePacketInternal(
```
> يعرّف دالة خاصّة معلّقة (suspend) باسم بثّ رزمة مفردة داخلي (broadcastSinglePacketInternal) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:260]

```
261:         routed: RoutedPacket,
```
> يعرّف معاملاً باسم الرزمة الموجّهة (routed) من نوع رزمة موجّهة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:261]

```
262:         gattServer: BluetoothGattServer?,
```
> يعرّف معاملاً باسم خادم جات (gattServer) من نوع خادم بلوتوث جات قابل لأن يكون فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:262]

```
263:         characteristic: BluetoothGattCharacteristic?
```
> يعرّف معاملاً باسم الخاصّية (characteristic) من نوع خاصّية بلوتوث جات قابلة لأن تكون فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:263]

```
264:     ) {
```
> يغلق قائمة المعاملات ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:264]

```
265:         val packet = routed.packet
```
> يعرّف متغيّراً ثابتاً باسم رزمة (packet) ويسند إليه حقل الرزمة (packet) من الرزمة الموجّهة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:265]

```
266:         // iOS-compatible: Use selective padding policy for BLE
```
> تعليق: متوافق مع iOS - استخدام سياسة حشو انتقائية للبلوتوث منخفض الطاقة (BLE). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:266]

```
267:         val padForBLE = BLEPacketPaddingPolicy.shouldPadForBLE(packet.type)
```
> يعرّف متغيّراً ثابتاً باسم حشو للبلوتوث منخفض الطاقة (padForBLE) ويسند إليه نتيجة استدعاء "هل يجب الحشو للبلوتوث منخفض الطاقة" (shouldPadForBLE) على سياسة حشو رزمة البلوتوث منخفض الطاقة (BLEPacketPaddingPolicy) ممرّراً نوع الرزمة (packet.type). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:267]

```
268:         val data = packet.toBinaryData(padding = padForBLE) ?: return
```
> يعرّف متغيّراً ثابتاً باسم البيانات (data) ويسند إليه نتيجة استدعاء التحويل إلى بيانات ثنائية (toBinaryData) على الرزمة مع معامل الحشو (padding) مساوياً للحشو للبلوتوث منخفض الطاقة، ويعود من الدالة إذا كانت النتيجة فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:268]

```
269:         val typeName = MessageType.fromValue(packet.type)?.name ?: packet.type.toString()
```
> يعرّف متغيّراً ثابتاً باسم اسم النوع (typeName) ويسند إليه اسم (name) نتيجة "من القيمة" (fromValue) على نوع الرسالة (MessageType) لنوع الرزمة، أو نصّ نوع الرزمة (packet.type.toString) إذا كانت النتيجة فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:269]

```
270:         val senderPeerID = routed.peerID ?: packet.senderID.toHexString()
```
> يعرّف متغيّراً ثابتاً باسم معرّف القرين المرسِل (senderPeerID) ويسند إليه معرّف القرين (peerID) من الرزمة الموجّهة، أو معرّف المرسِل بصيغة سداسية عشرية (packet.senderID.toHexString) إذا كان فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:270]

```
271:         val incomingAddr = routed.relayAddress
```
> يعرّف متغيّراً ثابتاً باسم العنوان الوارد (incomingAddr) ويسند إليه عنوان المُرحِّل (relayAddress) من الرزمة الموجّهة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:271]

```
272:         val incomingPeer = incomingAddr?.let { connectionTracker.addressPeerMap[it] }
```
> يعرّف متغيّراً ثابتاً باسم القرين الوارد (incomingPeer) ويسند إليه قيمة خريطة عنوان-قرين عند العنوان الوارد إذا لم يكن العنوان الوارد فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:272]

```
273:         val senderNick = senderPeerID.let { pid -> nicknameResolver?.invoke(pid) }
```
> يعرّف متغيّراً ثابتاً باسم لقب المرسِل (senderNick) ويسند إليه نتيجة استدعاء (invoke) مُحلِّل اللقب (nicknameResolver) على معرّف القرين المرسِل المسمّى pid إن لم يكن المحلّل فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:273]

```
274:         val route = packet.route
```
> يعرّف متغيّراً ثابتاً باسم المسار (route) ويسند إليه حقل المسار (route) من الرزمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:274]

```
275:         val routeInfo = if (!route.isNullOrEmpty()) "routed: ${route.size} hops" else null
```
> يعرّف متغيّراً ثابتاً باسم معلومات المسار (routeInfo) ويسند إليه نصّاً "routed:" متبوعاً بحجم المسار وكلمة "hops" إذا كان المسار غير فارغ ولا خالٍ، وإلا قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:275]

```
276: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:276]

```
277:         // Source Routing for Originating Packets
```
> تعليق: التوجيه المصدري للرزم المنشِئة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:277]

```
278:         // If we are the sender and a source route is defined, we must send ONLY to the first hop.
```
> تعليق: إذا كنّا المرسِل ومسار مصدري معرّف، فيجب أن نرسل فقط إلى القفزة الأولى. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:278]

```
279:         if (packet.senderID.toHexString() == myPeerID && !packet.route.isNullOrEmpty()) {
```
> يفتح شرطاً يتحقّق أنّ معرّف المرسِل بصيغة سداسية عشرية يساوي معرّف قريني (myPeerID) وأنّ مسار الرزمة غير فارغ ولا خالٍ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:279]

```
280:             val firstHop = packet.route!![0].toHexString()
```
> يعرّف متغيّراً ثابتاً باسم القفزة الأولى (firstHop) ويسند إليه العنصر الأوّل من مسار الرزمة (مع تأكيد عدم الفراغ) بصيغة سداسية عشرية. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:280]

```
281:             Log.d(TAG, "Source Routing: Packet has explicit route, attempting to send to first hop: $firstHop")
```
> يستدعي تسجيل تصحيح (Log.d) بالوسم ونصّ "التوجيه المصدري: للرزمة مسار صريح، محاولة الإرسال إلى القفزة الأولى" مع القفزة الأولى. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:281]

```
282: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:282]

```
283:             var sent = false
```
> يعرّف متغيّراً قابلاً للتغيير (var) باسم أُرسل (sent) ويسند إليه خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:283]

```
284: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:284]

```
285:             // Try to find first hop in server connections (subscribedDevices)
```
> تعليق: محاولة العثور على القفزة الأولى في اتصالات الخادم (الأجهزة المشتركة). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:285]

```
286:             val serverTarget = connectionTracker.getSubscribedDevices()
```
> يعرّف متغيّراً ثابتاً باسم هدف الخادم (serverTarget) يبدأ باستدعاء جلب الأجهزة المشتركة على متعقّب الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:286]

```
287:                 .firstOrNull { connectionTracker.addressPeerMap[it.address] == firstHop }
```
> يطبّق "الأوّل أو فارغ" (firstOrNull) الذي يختار العنصر الذي تساوي فيه خريطة عنوان-قرين عند عنوانه القفزة الأولى. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:287]

```
288:             
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:288]

```
289:             if (serverTarget != null) {
```
> يفتح شرطاً يتحقّق أنّ هدف الخادم لا يساوي فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:289]

```
290:                 Log.d(TAG, "Source Routing: sending directly to first hop (server conn) $firstHop: ${serverTarget.address}")
```
> يستدعي تسجيل تصحيح بالوسم ونصّ "التوجيه المصدري: إرسال مباشرة إلى القفزة الأولى (اتصال خادم)" مع القفزة الأولى وعنوان هدف الخادم. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:290]

```
291:                 if (notifyDevice(serverTarget, data, gattServer, characteristic)) {
```
> يفتح شرطاً يستدعي دالة إخطار الجهاز (notifyDevice) مع هدف الخادم والبيانات وخادم جات والخاصّية، وينفّذ الكتلة إذا أعادت صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:291]

```
292:                     val toPeer = connectionTracker.addressPeerMap[serverTarget.address]
```
> يعرّف متغيّراً ثابتاً باسم إلى القرين (toPeer) ويسند إليه قيمة خريطة عنوان-قرين عند عنوان هدف الخادم. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:292]

```
293:                     logPacketRelay(typeName, senderPeerID, senderNick, incomingPeer, incomingAddr, toPeer, serverTarget.address, packet.ttl, packet.version, routeInfo)
```
> يستدعي دالة تسجيل ترحيل الرزمة ممرّراً اسم النوع ومعرّف القرين المرسِل ولقب المرسِل والقرين الوارد والعنوان الوارد والقرين الهدف وعنوان هدف الخادم ومدّة الحياة ونسخة الرزمة ومعلومات المسار. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:293]

```
294:                     sent = true
```
> يسند إلى المتغيّر أُرسل القيمة صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:294]

```
295:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:295]

```
296:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:296]

```
297: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:297]

```
298:             // Try to find first hop in client connections if not sent yet
```
> تعليق: محاولة العثور على القفزة الأولى في اتصالات العميل إذا لم تُرسَل بعد. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:298]

```
299:             if (!sent) {
```
> يفتح شرطاً يتحقّق أنّ المتغيّر أُرسل يساوي خطأ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:299]

```
300:                 val clientTarget = connectionTracker.getConnectedDevices().values
```
> يعرّف متغيّراً ثابتاً باسم هدف العميل (clientTarget) يبدأ باستدعاء قيم جلب الأجهزة المتصلة على متعقّب الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:300]

```
301:                     .firstOrNull { connectionTracker.addressPeerMap[it.device.address] == firstHop }
```
> يطبّق "الأوّل أو فارغ" الذي يختار العنصر الذي تساوي فيه خريطة عنوان-قرين عند عنوان جهازه القفزة الأولى. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:301]

```
302:                 
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:302]

```
303:                 if (clientTarget != null) {
```
> يفتح شرطاً يتحقّق أنّ هدف العميل لا يساوي فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:303]

```
304:                     Log.d(TAG, "Source Routing: sending directly to first hop (client conn) $firstHop: ${clientTarget.device.address}")
```
> يستدعي تسجيل تصحيح بالوسم ونصّ "التوجيه المصدري: إرسال مباشرة إلى القفزة الأولى (اتصال عميل)" مع القفزة الأولى وعنوان جهاز هدف العميل. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:304]

```
305:                     if (writeToDeviceConn(clientTarget, data)) {
```
> يفتح شرطاً يستدعي دالة الكتابة لاتصال الجهاز مع هدف العميل والبيانات، وينفّذ الكتلة إذا أعادت صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:305]

```
306:                         val toPeer = connectionTracker.addressPeerMap[clientTarget.device.address]
```
> يعرّف متغيّراً ثابتاً باسم إلى القرين (toPeer) ويسند إليه قيمة خريطة عنوان-قرين عند عنوان جهاز هدف العميل. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:306]

```
307:                         logPacketRelay(typeName, senderPeerID, senderNick, incomingPeer, incomingAddr, toPeer, clientTarget.device.address, packet.ttl, packet.version, routeInfo)
```
> يستدعي دالة تسجيل ترحيل الرزمة ممرّراً اسم النوع ومعرّف القرين المرسِل ولقب المرسِل والقرين الوارد والعنوان الوارد والقرين الهدف وعنوان جهاز هدف العميل ومدّة الحياة ونسخة الرزمة ومعلومات المسار. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:307]

```
308:                         sent = true
```
> يسند إلى المتغيّر أُرسل القيمة صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:308]

```
309:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:309]

```
310:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:310]

```
311:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:311]

```
312: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:312]

```
313:             if (sent) return
```
> يعود من الدالة إذا كان المتغيّر أُرسل صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:313]

```
314:             
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:314]

```
315:             Log.w(TAG, "Source Routing: First hop $firstHop not connected. Falling back to standard broadcast logic.")
```
> يستدعي تسجيل تحذير بالوسم ونصّ "التوجيه المصدري: القفزة الأولى غير متصلة. الرجوع إلى منطق البثّ القياسي" مع القفزة الأولى. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:315]

```
316:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:316]

```
317:         
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:317]

```
318:         if (packet.recipientID != SpecialRecipients.BROADCAST) {
```
> يفتح شرطاً يتحقّق أنّ معرّف المستلِم (recipientID) للرزمة لا يساوي ثابت البثّ (BROADCAST) من المستلِمين الخاصّين (SpecialRecipients). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:318]

```
319:             val recipientID = packet.recipientID?.toHexString() ?: ""
```
> يعرّف متغيّراً ثابتاً باسم معرّف المستلِم (recipientID) ويسند إليه معرّف مستلِم الرزمة بصيغة سداسية عشرية إن لم يكن فارغاً، وإلا نصّاً فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:319]

```
320: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:320]

```
321:             // Try to find the recipient in server connections (subscribedDevices)
```
> تعليق: محاولة العثور على المستلِم في اتصالات الخادم (الأجهزة المشتركة). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:321]

```
322:             val targetDevice = connectionTracker.getSubscribedDevices()
```
> يعرّف متغيّراً ثابتاً باسم الجهاز الهدف (targetDevice) يبدأ باستدعاء جلب الأجهزة المشتركة على متعقّب الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:322]

```
323:                 .firstOrNull { connectionTracker.addressPeerMap[it.address] == recipientID }
```
> يطبّق "الأوّل أو فارغ" الذي يختار العنصر الذي تساوي فيه خريطة عنوان-قرين عند عنوانه معرّف المستلِم. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:323]

```
324:             
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:324]

```
325:             // If found, send directly
```
> تعليق: إذا وُجد، أرسل مباشرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:325]

```
326:             if (targetDevice != null) {
```
> يفتح شرطاً يتحقّق أنّ الجهاز الهدف لا يساوي فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:326]

```
327:                 Log.d(TAG, "Send packet type ${packet.type} directly to target device for recipient $recipientID: ${targetDevice.address}")
```
> يستدعي تسجيل تصحيح بالوسم ونصّ "إرسال رزمة من النوع كذا مباشرة إلى الجهاز الهدف للمستلِم كذا" مع نوع الرزمة ومعرّف المستلِم وعنوان الجهاز الهدف. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:327]

```
328:                 if (notifyDevice(targetDevice, data, gattServer, characteristic)) {
```
> يفتح شرطاً يستدعي دالة إخطار الجهاز مع الجهاز الهدف والبيانات وخادم جات والخاصّية، وينفّذ الكتلة إذا أعادت صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:328]

```
329:                     val toPeer = connectionTracker.addressPeerMap[targetDevice.address]
```
> يعرّف متغيّراً ثابتاً باسم إلى القرين (toPeer) ويسند إليه قيمة خريطة عنوان-قرين عند عنوان الجهاز الهدف. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:329]

```
330:                     logPacketRelay(typeName, senderPeerID, senderNick, incomingPeer, incomingAddr, toPeer, targetDevice.address, packet.ttl, packet.version, routeInfo)
```
> يستدعي دالة تسجيل ترحيل الرزمة ممرّراً اسم النوع ومعرّف القرين المرسِل ولقب المرسِل والقرين الوارد والعنوان الوارد والقرين الهدف وعنوان الجهاز الهدف ومدّة الحياة ونسخة الرزمة ومعلومات المسار. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:330]

```
331:                     return  // Sent, no need to continue
```
> يعود من الدالة، مع تعليق: أُرسل، لا حاجة للمتابعة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:331]

```
332:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:332]

```
333:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:333]

```
334: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:334]

```
335:             // Try to find the recipient in client connections (connectedDevices)
```
> تعليق: محاولة العثور على المستلِم في اتصالات العميل (الأجهزة المتصلة). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:335]

```
336:             val targetDeviceConn = connectionTracker.getConnectedDevices().values
```
> يعرّف متغيّراً ثابتاً باسم اتصال الجهاز الهدف (targetDeviceConn) يبدأ باستدعاء قيم جلب الأجهزة المتصلة على متعقّب الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:336]

```
337:                 .firstOrNull { connectionTracker.addressPeerMap[it.device.address] == recipientID }
```
> يطبّق "الأوّل أو فارغ" الذي يختار العنصر الذي تساوي فيه خريطة عنوان-قرين عند عنوان جهازه معرّف المستلِم. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:337]

```
338:             
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:338]

```
339:             // If found, send directly
```
> تعليق: إذا وُجد، أرسل مباشرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:339]

```
340:             if (targetDeviceConn != null) {
```
> يفتح شرطاً يتحقّق أنّ اتصال الجهاز الهدف لا يساوي فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:340]

```
341:                 Log.d(TAG, "Send packet type ${packet.type} directly to target client connection for recipient $recipientID: ${targetDeviceConn.device.address}")
```
> يستدعي تسجيل تصحيح بالوسم ونصّ "إرسال رزمة من النوع كذا مباشرة إلى اتصال العميل الهدف للمستلِم كذا" مع نوع الرزمة ومعرّف المستلِم وعنوان جهاز اتصال الجهاز الهدف. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:341]

```
342:                 if (writeToDeviceConn(targetDeviceConn, data)) {
```
> يفتح شرطاً يستدعي دالة الكتابة لاتصال الجهاز مع اتصال الجهاز الهدف والبيانات، وينفّذ الكتلة إذا أعادت صحيحاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:342]

```
343:                     val toPeer = connectionTracker.addressPeerMap[targetDeviceConn.device.address]
```
> يعرّف متغيّراً ثابتاً باسم إلى القرين (toPeer) ويسند إليه قيمة خريطة عنوان-قرين عند عنوان جهاز اتصال الجهاز الهدف. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:343]

```
344:                     logPacketRelay(typeName, senderPeerID, senderNick, incomingPeer, incomingAddr, toPeer, targetDeviceConn.device.address, packet.ttl, packet.version, routeInfo)
```
> يستدعي دالة تسجيل ترحيل الرزمة ممرّراً اسم النوع ومعرّف القرين المرسِل ولقب المرسِل والقرين الوارد والعنوان الوارد والقرين الهدف وعنوان جهاز اتصال الجهاز الهدف ومدّة الحياة ونسخة الرزمة ومعلومات المسار. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:344]

```
345:                     return  // Sent, no need to continue
```
> يعود من الدالة، مع تعليق: أُرسل، لا حاجة للمتابعة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:345]

```
346:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:346]

```
347:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:347]

```
348:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:348]

```
349: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:349]

```
350:         // Else, continue with broadcasting to all devices
```
> تعليق: وإلا، تابع البثّ إلى كلّ الأجهزة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:350]

```
351:         val subscribedDevices = connectionTracker.getSubscribedDevices()
```
> يعرّف متغيّراً ثابتاً باسم الأجهزة المشتركة (subscribedDevices) ويسند إليه نتيجة جلب الأجهزة المشتركة على متعقّب الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:351]

```
352:         val connectedDevices = connectionTracker.getConnectedDevices()
```
> يعرّف متغيّراً ثابتاً باسم الأجهزة المتصلة (connectedDevices) ويسند إليه نتيجة جلب الأجهزة المتصلة على متعقّب الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:352]

```
353:         
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:353]

```
354:         Log.i(TAG, "Broadcasting packet v${packet.version} type ${packet.type} to ${subscribedDevices.size} server + ${connectedDevices.size} client connections")
```
> يستدعي تسجيل معلومة (Log.i) بالوسم ونصّ "بثّ رزمة نسخة كذا نوع كذا إلى كذا اتصال خادم + كذا اتصال عميل" مع نسخة الرزمة ونوعها وحجم الأجهزة المشتركة وحجم الأجهزة المتصلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:354]

```
355: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:355]

```
356:         val senderID = packet.senderID.toHexString()
```
> يعرّف متغيّراً ثابتاً باسم معرّف المرسِل (senderID) ويسند إليه معرّف مرسِل الرزمة بصيغة سداسية عشرية. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:356]

```
357:         
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:357]

```
358:         // Send to server connections (devices connected to our GATT server)
```
> تعليق: الإرسال إلى اتصالات الخادم (الأجهزة المتصلة بخادم جات لدينا). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:358]

```
359:         subscribedDevices.forEach { device ->
```
> يطبّق "لكلّ" (forEach) على الأجهزة المشتركة بمعامل باسم جهاز (device). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:359]

```
360:             if (device.address == routed.relayAddress) {
```
> يفتح شرطاً يتحقّق أنّ عنوان الجهاز يساوي عنوان المُرحِّل من الرزمة الموجّهة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:360]

```
361:                 Log.d(TAG, "Skipping broadcast to client back to relayer: ${device.address}")
```
> يستدعي تسجيل تصحيح بالوسم ونصّ "تخطّي البثّ إلى العميل عودةً إلى المُرحِّل" مع عنوان الجهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:361]

```
362:                 return@forEach
```
> يعود من تكرار "لكلّ" الحالي (يتخطّى هذا العنصر). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:362]

```
363:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:363]

```
364:             if (connectionTracker.addressPeerMap[device.address] == senderID) {
```
> يفتح شرطاً يتحقّق أنّ خريطة عنوان-قرين عند عنوان الجهاز تساوي معرّف المرسِل. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:364]

```
365:                 Log.d(TAG, "Skipping broadcast to client back to sender: ${device.address}")
```
> يستدعي تسجيل تصحيح بالوسم ونصّ "تخطّي البثّ إلى العميل عودةً إلى المرسِل" مع عنوان الجهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:365]

```
366:                 return@forEach
```
> يعود من تكرار "لكلّ" الحالي (يتخطّى هذا العنصر). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:366]

```
367:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:367]

```
368:             val sent = notifyDevice(device, data, gattServer, characteristic)
```
> يعرّف متغيّراً ثابتاً باسم أُرسل (sent) ويسند إليه نتيجة استدعاء دالة إخطار الجهاز مع الجهاز والبيانات وخادم جات والخاصّية. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:368]

```
369:             if (sent) {
```
> يفتح شرطاً يتحقّق أنّ المتغيّر أُرسل صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:369]

```
370:                 val toPeer = connectionTracker.addressPeerMap[device.address]
```
> يعرّف متغيّراً ثابتاً باسم إلى القرين (toPeer) ويسند إليه قيمة خريطة عنوان-قرين عند عنوان الجهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:370]

```
371:                 logPacketRelay(typeName, senderPeerID, senderNick, incomingPeer, incomingAddr, toPeer, device.address, packet.ttl, packet.version, routeInfo)
```
> يستدعي دالة تسجيل ترحيل الرزمة ممرّراً اسم النوع ومعرّف القرين المرسِل ولقب المرسِل والقرين الوارد والعنوان الوارد والقرين الهدف وعنوان الجهاز ومدّة الحياة ونسخة الرزمة ومعلومات المسار. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:371]

```
372:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:372]

```
373:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:373]

```
374:         
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:374]

```
375:         // Send to client connections (GATT servers we are connected to)
```
> تعليق: الإرسال إلى اتصالات العميل (خوادم جات التي نحن متصلون بها). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:375]

```
376:         connectedDevices.values.forEach { deviceConn ->
```
> يطبّق "لكلّ" على قيم الأجهزة المتصلة بمعامل باسم اتصال الجهاز (deviceConn). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:376]

```
377:             if (deviceConn.isClient && deviceConn.gatt != null && deviceConn.characteristic != null) {
```
> يفتح شرطاً يتحقّق أنّ اتصال الجهاز عميل (isClient) وأنّ حقل جات (gatt) لا يساوي فارغاً وأنّ حقل الخاصّية (characteristic) لا يساوي فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:377]

```
378:                 if (deviceConn.device.address == routed.relayAddress) {
```
> يفتح شرطاً يتحقّق أنّ عنوان جهاز اتصال الجهاز يساوي عنوان المُرحِّل من الرزمة الموجّهة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:378]

```
379:                     Log.d(TAG, "Skipping broadcast to server back to relayer: ${deviceConn.device.address}")
```
> يستدعي تسجيل تصحيح بالوسم ونصّ "تخطّي البثّ إلى الخادم عودةً إلى المُرحِّل" مع عنوان جهاز اتصال الجهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:379]

```
380:                     return@forEach
```
> يعود من تكرار "لكلّ" الحالي (يتخطّى هذا العنصر). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:380]

```
381:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:381]

```
382:                 if (connectionTracker.addressPeerMap[deviceConn.device.address] == senderID) {
```
> يفتح شرطاً يتحقّق أنّ خريطة عنوان-قرين عند عنوان جهاز اتصال الجهاز تساوي معرّف المرسِل. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:382]

```
383:                     Log.d(TAG, "Skipping roadcast to server back to sender: ${deviceConn.device.address}")
```
> يستدعي تسجيل تصحيح بالوسم ونصّ "تخطّي البثّ إلى الخادم عودةً إلى المرسِل" (وردت كلمة broadcast منقوصة الحرف "roadcast" في الأصل) مع عنوان جهاز اتصال الجهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:383]

```
384:                     return@forEach
```
> يعود من تكرار "لكلّ" الحالي (يتخطّى هذا العنصر). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:384]

```
385:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:385]

```
386:                 val sent = writeToDeviceConn(deviceConn, data)
```
> يعرّف متغيّراً ثابتاً باسم أُرسل (sent) ويسند إليه نتيجة استدعاء دالة الكتابة لاتصال الجهاز مع اتصال الجهاز والبيانات. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:386]

```
387:                 if (sent) {
```
> يفتح شرطاً يتحقّق أنّ المتغيّر أُرسل صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:387]

```
388:                     val toPeer = connectionTracker.addressPeerMap[deviceConn.device.address]
```
> يعرّف متغيّراً ثابتاً باسم إلى القرين (toPeer) ويسند إليه قيمة خريطة عنوان-قرين عند عنوان جهاز اتصال الجهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:388]

```
389:                     logPacketRelay(typeName, senderPeerID, senderNick, incomingPeer, incomingAddr, toPeer, deviceConn.device.address, packet.ttl, packet.version, routeInfo)
```
> يستدعي دالة تسجيل ترحيل الرزمة ممرّراً اسم النوع ومعرّف القرين المرسِل ولقب المرسِل والقرين الوارد والعنوان الوارد والقرين الهدف وعنوان جهاز اتصال الجهاز ومدّة الحياة ونسخة الرزمة ومعلومات المسار. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:389]

```
390:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:390]

```
391:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:391]

```
392:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:392]

```
393:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:393]

```
394:     
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:394]

```
395:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:395]

```
396:      * Send data to a single device (server->client)
```
> تعليق: إرسال بيانات إلى جهاز مفرد (من الخادم إلى العميل). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:396]

```
397:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:397]

```
398:     private fun notifyDevice(
```
> يعرّف دالة خاصّة باسم إخطار الجهاز (notifyDevice) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:398]

```
399:         device: BluetoothDevice, 
```
> يعرّف معاملاً باسم جهاز (device) من نوع جهاز بلوتوث (BluetoothDevice). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:399]

```
400:         data: ByteArray,
```
> يعرّف معاملاً باسم البيانات (data) من نوع مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:400]
