# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt (الأسطر 201–400)

```
201:                         connectionTracker.cleanupDeviceConnection(device.address)
```
> يُستدعى على متتبّع الاتصال (connectionTracker) الفعل تنظيف اتصال الجهاز (cleanupDeviceConnection) ويُمرَّر له عنوان الجهاز (device.address). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:201]

```
202:                         // Notify delegate about device disconnection so higher layers can update direct flags
```
> تعليق: أخبِر المفوَّض (delegate) عن قطع اتصال الجهاز حتى تستطيع الطبقات الأعلى تحديث الأعلام المباشرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:202]

```
203:                         delegate?.onDeviceDisconnected(device)
```
> يُستدعى على المفوَّض (delegate) إن لم يكن فارغاً الفعل عند قطع اتصال الجهاز (onDeviceDisconnected) ويُمرَّر له الجهاز (device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:203]

```
204:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:204]

```
205:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:205]

```
206:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:206]

```
207:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:207]

```
208:             override fun onServiceAdded(status: Int, service: BluetoothGattService) {
```
> تعريف دالة متجاوِزة (override) باسم عند إضافة الخدمة (onServiceAdded) تأخذ مَعلَمة الحالة (status) من نوع عدد صحيح (Int) ومَعلَمة الخدمة (service) من نوع خدمة جات بلوتوث (BluetoothGattService). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:208]

```
209:                 // Guard against callbacks after service shutdown
```
> تعليق: احرُس ضدّ النداءات الراجعة بعد إغلاق الخدمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:209]

```
210:                 if (!isActive) {
```
> شرط: إذا لم يكن نشِطاً (isActive). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:210]

```
211:                     Log.d(TAG, "Server: Ignoring service added callback after shutdown")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم (TAG) ونص «Server: Ignoring service added callback after shutdown» (الخادم: تجاهُل نداء إضافة الخدمة الراجع بعد الإغلاق). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:211]

```
212:                     return
```
> يُعاد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:212]

```
213:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:213]

```
214:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:214]

```
215:                 if (status == BluetoothGatt.GATT_SUCCESS) {
```
> شرط: إذا كانت الحالة (status) تساوي ثابت نجاح جات (BluetoothGatt.GATT_SUCCESS). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:215]

```
216:                     Log.d(TAG, "Server: Service added successfully: ${service.uuid}")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم (TAG) ونص «Server: Service added successfully:» (الخادم: أُضيفت الخدمة بنجاح) متبوعاً بمُعرّف الخدمة (service.uuid). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:216]

```
217:                 } else {
```
> وإلّا (else). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:217]

```
218:                     Log.e(TAG, "Server: Failed to add service: ${service.uuid}, status: $status")
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم (TAG) ونص «Server: Failed to add service:» (الخادم: فشلت إضافة الخدمة) متبوعاً بمُعرّف الخدمة (service.uuid) ثم «status:» وقيمة الحالة (status). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:218]

```
219:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:219]

```
220:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:220]

```
221:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:221]

```
222:             override fun onCharacteristicWriteRequest(
```
> تعريف دالة متجاوِزة (override) باسم عند طلب الكتابة على الخاصية (onCharacteristicWriteRequest) تبدأ قائمة مَعلَماتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:222]

```
223:                 device: BluetoothDevice,
```
> مَعلَمة الجهاز (device) من نوع جهاز بلوتوث (BluetoothDevice). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:223]

```
224:                 requestId: Int,
```
> مَعلَمة مُعرّف الطلب (requestId) من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:224]

```
225:                 characteristic: BluetoothGattCharacteristic,
```
> مَعلَمة الخاصية (characteristic) من نوع خاصية جات بلوتوث (BluetoothGattCharacteristic). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:225]

```
226:                 preparedWrite: Boolean,
```
> مَعلَمة كتابة مُهيَّأة (preparedWrite) من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:226]

```
227:                 responseNeeded: Boolean,
```
> مَعلَمة الحاجة إلى ردّ (responseNeeded) من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:227]

```
228:                 offset: Int,
```
> مَعلَمة الإزاحة (offset) من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:228]

```
229:                 value: ByteArray
```
> مَعلَمة القيمة (value) من نوع مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:229]

```
230:             ) {
```
> إغلاق قائمة المَعلَمات وبدء جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:230]

```
231:                 // Guard against callbacks after service shutdown
```
> تعليق: احرُس ضدّ النداءات الراجعة بعد إغلاق الخدمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:231]

```
232:                 if (!isActive) {
```
> شرط: إذا لم يكن نشِطاً (isActive). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:232]

```
233:                     Log.d(TAG, "Server: Ignoring characteristic write after shutdown")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم (TAG) ونص «Server: Ignoring characteristic write after shutdown» (الخادم: تجاهُل كتابة الخاصية بعد الإغلاق). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:233]

```
234:                     return
```
> يُعاد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:234]

```
235:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:235]

```
236:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:236]

```
237:                 if (characteristic.uuid == AppConstants.Mesh.Gatt.CHARACTERISTIC_UUID) {
```
> شرط: إذا كان مُعرّف الخاصية (characteristic.uuid) يساوي ثابت مُعرّف الخاصية (AppConstants.Mesh.Gatt.CHARACTERISTIC_UUID). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:237]

```
238:                     Log.i(TAG, "Server: Received packet from ${device.address}, size: ${value.size} bytes")
```
> يُستدعى تسجيل معلومات (Log.i) بالوسم (TAG) ونص «Server: Received packet from» (الخادم: استُلمت رزمة من) متبوعاً بعنوان الجهاز (device.address) ثم «size:» وحجم القيمة (value.size) ثم «bytes». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:238]

```
239:                     val packet = BitchatPacket.fromBinaryData(value)
```
> يُعرَّف ثابت الرزمة (packet) ويُسنَد إليه ناتج استدعاء الدالة من البيانات الثنائية (fromBinaryData) على نوع رزمة بِتشات (BitchatPacket) ممرَّراً القيمة (value). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:239]

```
240:                     if (packet != null) {
```
> شرط: إذا كانت الرزمة (packet) ليست فارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:240]

```
241:                         val peerID = packet.senderID.take(8).toByteArray().joinToString("") { "%02x".format(it) }
```
> يُعرَّف ثابت مُعرّف القرين (peerID) ويُسنَد إليه: تُؤخذ أوّل ٨ عناصر من مُعرّف المُرسِل (packet.senderID) ثم تُحوَّل إلى مصفوفة بايتات (toByteArray) ثم تُدمَج نصّاً (joinToString) بفاصل فارغ بتنسيق كل بايت بالنظام الست عشري بخانتين («%02x»). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:241]

```
242:                         Log.d(TAG, "Server: Parsed packet type ${packet.type} from $peerID")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم (TAG) ونص «Server: Parsed packet type» (الخادم: حُلِّل نوع الرزمة) متبوعاً بنوع الرزمة (packet.type) ثم «from» ومُعرّف القرين (peerID). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:242]

```
243:                         delegate?.onPacketReceived(packet, peerID, device)
```
> يُستدعى على المفوَّض (delegate) إن لم يكن فارغاً الفعل عند استلام الرزمة (onPacketReceived) ويُمرَّر له الرزمة (packet) ومُعرّف القرين (peerID) والجهاز (device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:243]

```
244:                     } else {
```
> وإلّا (else). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:244]

```
245:                         Log.w(TAG, "Server: Failed to parse packet from ${device.address}, size: ${value.size} bytes")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم (TAG) ونص «Server: Failed to parse packet from» (الخادم: فشل تحليل الرزمة من) متبوعاً بعنوان الجهاز (device.address) ثم «size:» وحجم القيمة (value.size) ثم «bytes». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:245]

```
246:                         Log.w(TAG, "Server: Packet data: ${value.joinToString(" ") { "%02x".format(it) }}")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم (TAG) ونص «Server: Packet data:» (الخادم: بيانات الرزمة) متبوعاً بدمج القيمة (value.joinToString) نصّاً بفاصل مسافة بتنسيق كل بايت ست عشري بخانتين («%02x»). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:246]

```
247:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:247]

```
248:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:248]

```
249:                     if (responseNeeded) {
```
> شرط: إذا كانت الحاجة إلى ردّ (responseNeeded) محقَّقة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:249]

```
250:                         gattServer?.sendResponse(device, requestId, BluetoothGatt.GATT_SUCCESS, 0, null)
```
> يُستدعى على خادم جات (gattServer) إن لم يكن فارغاً الفعل إرسال ردّ (sendResponse) ممرَّراً الجهاز (device) ومُعرّف الطلب (requestId) وثابت نجاح جات (BluetoothGatt.GATT_SUCCESS) والإزاحة صفر والقيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:250]

```
251:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:251]

```
252:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:252]

```
253:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:253]

```
254:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:254]

```
255:             override fun onDescriptorWriteRequest(
```
> تعريف دالة متجاوِزة (override) باسم عند طلب الكتابة على الواصِف (onDescriptorWriteRequest) تبدأ قائمة مَعلَماتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:255]

```
256:                 device: BluetoothDevice,
```
> مَعلَمة الجهاز (device) من نوع جهاز بلوتوث (BluetoothDevice). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:256]

```
257:                 requestId: Int,
```
> مَعلَمة مُعرّف الطلب (requestId) من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:257]

```
258:                 descriptor: BluetoothGattDescriptor,
```
> مَعلَمة الواصِف (descriptor) من نوع واصِف جات بلوتوث (BluetoothGattDescriptor). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:258]

```
259:                 preparedWrite: Boolean,
```
> مَعلَمة كتابة مُهيَّأة (preparedWrite) من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:259]

```
260:                 responseNeeded: Boolean,
```
> مَعلَمة الحاجة إلى ردّ (responseNeeded) من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:260]

```
261:                 offset: Int,
```
> مَعلَمة الإزاحة (offset) من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:261]

```
262:                 value: ByteArray
```
> مَعلَمة القيمة (value) من نوع مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:262]

```
263:             ) {
```
> إغلاق قائمة المَعلَمات وبدء جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:263]

```
264:                 // Guard against callbacks after service shutdown
```
> تعليق: احرُس ضدّ النداءات الراجعة بعد إغلاق الخدمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:264]

```
265:                 if (!isActive) {
```
> شرط: إذا لم يكن نشِطاً (isActive). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:265]

```
266:                     Log.d(TAG, "Server: Ignoring descriptor write after shutdown")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم (TAG) ونص «Server: Ignoring descriptor write after shutdown» (الخادم: تجاهُل كتابة الواصِف بعد الإغلاق). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:266]

```
267:                     return
```
> يُعاد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:267]

```
268:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:268]

```
269:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:269]

```
270:                 if (BluetoothGattDescriptor.ENABLE_NOTIFICATION_VALUE.contentEquals(value)) {
```
> شرط: إذا كان ثابت قيمة تفعيل الإشعار (BluetoothGattDescriptor.ENABLE_NOTIFICATION_VALUE) مطابقاً في المحتوى (contentEquals) للقيمة (value). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:270]

```
271:                     connectionTracker.addSubscribedDevice(device)
```
> يُستدعى على متتبّع الاتصال (connectionTracker) الفعل إضافة جهاز مشترِك (addSubscribedDevice) ويُمرَّر له الجهاز (device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:271]

```
272:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:272]

```
273:                     Log.d(TAG, "Server: Connection setup complete for ${device.address}")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم (TAG) ونص «Server: Connection setup complete for» (الخادم: اكتمل إعداد الاتصال لـ) متبوعاً بعنوان الجهاز (device.address). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:273]

```
274:                     connectionScope.launch {
```
> يُستدعى على نطاق الاتصال (connectionScope) الفعل إطلاق (launch) لبدء كتلة كوروتين (coroutine). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:274]

```
275:                         delay(100)
```
> يُستدعى التأخير (delay) بمقدار ١٠٠ (مللي ثانية). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:275]

```
276:                         if (isActive) { // Check if still active
```
> شرط: إذا كان نشِطاً (isActive)؛ وتعليق: تحقّق إن كان ما زال نشِطاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:276]

```
277:                             delegate?.onDeviceConnected(device)
```
> يُستدعى على المفوَّض (delegate) إن لم يكن فارغاً الفعل عند اتصال الجهاز (onDeviceConnected) ويُمرَّر له الجهاز (device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:277]

```
278:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:278]

```
279:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:279]

```
280:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:280]

```
281:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:281]

```
282:                 if (responseNeeded) {
```
> شرط: إذا كانت الحاجة إلى ردّ (responseNeeded) محقَّقة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:282]

```
283:                     gattServer?.sendResponse(device, requestId, BluetoothGatt.GATT_SUCCESS, 0, null)
```
> يُستدعى على خادم جات (gattServer) إن لم يكن فارغاً الفعل إرسال ردّ (sendResponse) ممرَّراً الجهاز (device) ومُعرّف الطلب (requestId) وثابت نجاح جات (BluetoothGatt.GATT_SUCCESS) والإزاحة صفر والقيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:283]

```
284:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:284]

```
285:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:285]

```
286:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:286]

```
287:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:287]

```
288:         // Proper cleanup sequencing to prevent race conditions
```
> تعليق: ترتيب تنظيف سليم لمنع حالات التسابق (race conditions). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:288]

```
289:         gattServer?.let { server ->
```
> يُستدعى على خادم جات (gattServer) إن لم يكن فارغاً الفعل دَع (let) مع تسمية الوسيط الخادم (server). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:289]

```
290:             Log.d(TAG, "Cleaning up existing GATT server")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم (TAG) ونص «Cleaning up existing GATT server» (تنظيف خادم جات الموجود). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:290]

```
291:             try {
```
> بدء كتلة محاوَلة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:291]

```
292:                 server.close()
```
> يُستدعى على الخادم (server) الفعل إغلاق (close). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:292]

```
293:             } catch (e: Exception) {
```
> اصطياد (catch) استثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:293]

```
294:                 Log.w(TAG, "Error closing existing GATT server: ${e.message}")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم (TAG) ونص «Error closing existing GATT server:» (خطأ في إغلاق خادم جات الموجود) متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:294]

```
295:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:295]

```
296:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:296]

```
297:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:297]

```
298:         // Small delay to ensure cleanup is complete
```
> تعليق: تأخير صغير لضمان اكتمال التنظيف. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:298]

```
299:         Thread.sleep(100)
```
> يُستدعى على الخيط (Thread) الفعل نوم (sleep) بمقدار ١٠٠ (مللي ثانية). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:299]

```
300:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:300]

```
301:         if (!isActive) {
```
> شرط: إذا لم يكن نشِطاً (isActive). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:301]

```
302:             Log.d(TAG, "Service inactive, skipping GATT server creation")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم (TAG) ونص «Service inactive, skipping GATT server creation» (الخدمة غير نشِطة، تخطّي إنشاء خادم جات). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:302]

```
303:             return
```
> يُعاد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:303]

```
304:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:304]

```
305:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:305]

```
306:         // Create new server
```
> تعليق: أنشئ خادماً جديداً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:306]

```
307:         gattServer = bluetoothManager.openGattServer(context, serverCallback)
```
> يُسنَد إلى خادم جات (gattServer) ناتج استدعاء فتح خادم جات (openGattServer) على مدير البلوتوث (bluetoothManager) ممرَّراً السياق (context) ونداء الخادم الراجع (serverCallback). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:307]

```
308:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:308]

```
309:         // Create characteristic with notification support
```
> تعليق: أنشئ خاصية بدعم الإشعار. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:309]

```
310:         characteristic = BluetoothGattCharacteristic(
```
> يُسنَد إلى الخاصية (characteristic) كائن جديد من خاصية جات بلوتوث (BluetoothGattCharacteristic) تبدأ وسائطه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:310]

```
311:             AppConstants.Mesh.Gatt.CHARACTERISTIC_UUID,
```
> الوسيط الأول: ثابت مُعرّف الخاصية (AppConstants.Mesh.Gatt.CHARACTERISTIC_UUID). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:311]

```
312:             BluetoothGattCharacteristic.PROPERTY_READ or 
```
> الوسيط الثاني (الخصائص): ثابت خاصية القراءة (PROPERTY_READ) مدموجاً بمؤثّر «or». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:312]

```
313:             BluetoothGattCharacteristic.PROPERTY_WRITE or 
```
> ثابت خاصية الكتابة (PROPERTY_WRITE) مدموجاً بمؤثّر «or». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:313]

```
314:             BluetoothGattCharacteristic.PROPERTY_WRITE_NO_RESPONSE or
```
> ثابت خاصية الكتابة بلا ردّ (PROPERTY_WRITE_NO_RESPONSE) مدموجاً بمؤثّر «or». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:314]

```
315:             BluetoothGattCharacteristic.PROPERTY_NOTIFY,
```
> ثابت خاصية الإشعار (PROPERTY_NOTIFY)، وهو خاتمة دمج الخصائص. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:315]

```
316:             BluetoothGattCharacteristic.PERMISSION_READ or 
```
> الوسيط الثالث (الأذونات): ثابت إذن القراءة (PERMISSION_READ) مدموجاً بمؤثّر «or». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:316]

```
317:             BluetoothGattCharacteristic.PERMISSION_WRITE
```
> ثابت إذن الكتابة (PERMISSION_WRITE)، وهو خاتمة دمج الأذونات. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:317]

```
318:         )
```
> إغلاق وسائط المُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:318]

```
319:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:319]

```
320:         val descriptor = BluetoothGattDescriptor(
```
> يُعرَّف ثابت الواصِف (descriptor) ويُسنَد إليه كائن جديد من واصِف جات بلوتوث (BluetoothGattDescriptor) تبدأ وسائطه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:320]

```
321:             AppConstants.Mesh.Gatt.DESCRIPTOR_UUID,
```
> الوسيط الأول: ثابت مُعرّف الواصِف (AppConstants.Mesh.Gatt.DESCRIPTOR_UUID). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:321]

```
322:             BluetoothGattDescriptor.PERMISSION_READ or BluetoothGattDescriptor.PERMISSION_WRITE
```
> الوسيط الثاني (الأذونات): ثابت إذن القراءة (PERMISSION_READ) مدموجاً بمؤثّر «or» مع ثابت إذن الكتابة (PERMISSION_WRITE). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:322]

```
323:         )
```
> إغلاق وسائط المُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:323]

```
324:         characteristic?.addDescriptor(descriptor)
```
> يُستدعى على الخاصية (characteristic) إن لم تكن فارغة الفعل إضافة واصِف (addDescriptor) ويُمرَّر له الواصِف (descriptor). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:324]

```
325:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:325]

```
326:         val service = BluetoothGattService(AppConstants.Mesh.Gatt.SERVICE_UUID, BluetoothGattService.SERVICE_TYPE_PRIMARY)
```
> يُعرَّف ثابت الخدمة (service) ويُسنَد إليه كائن جديد من خدمة جات بلوتوث (BluetoothGattService) ممرَّراً ثابت مُعرّف الخدمة (AppConstants.Mesh.Gatt.SERVICE_UUID) وثابت نوع الخدمة الأساسية (SERVICE_TYPE_PRIMARY). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:326]

```
327:         service.addCharacteristic(characteristic)
```
> يُستدعى على الخدمة (service) الفعل إضافة خاصية (addCharacteristic) ويُمرَّر له الخاصية (characteristic). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:327]

```
328:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:328]

```
329:         gattServer?.addService(service)
```
> يُستدعى على خادم جات (gattServer) إن لم يكن فارغاً الفعل إضافة خدمة (addService) ويُمرَّر له الخدمة (service). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:329]

```
330:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:330]

```
331:         Log.i(TAG, "GATT server setup complete")
```
> يُستدعى تسجيل معلومات (Log.i) بالوسم (TAG) ونص «GATT server setup complete» (اكتمل إعداد خادم جات). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:331]

```
332:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:332]

```
333:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:333]

```
334:     /**
```
> بدء تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:334]

```
335:      * Start advertising
```
> تعليق: ابدأ الإعلان (Start advertising). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:335]

```
336:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:336]

```
337:     @Suppress("DEPRECATION")
```
> توضيح (annotation) كبت تحذير (Suppress) للقيمة «DEPRECATION» (الإهمال). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:337]

```
338:     private fun startAdvertising() {
```
> تعريف دالة خاصة (private) باسم بدء الإعلان (startAdvertising) بلا مَعلَمات. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:338]

```
339:         // Respect debug setting
```
> تعليق: احترِم إعداد التصحيح (debug setting). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:339]

```
340:         val enabled = isServerRoleEnabled()
```
> يُعرَّف ثابت مُفعَّل (enabled) ويُسنَد إليه ناتج استدعاء هل دور الخادم مُفعَّل (isServerRoleEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:340]

```
341:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:341]

```
342:         // Guard conditions – never throw here to avoid crashing the app from a background coroutine
```
> تعليق: شروط حراسة – لا تَرمِ استثناءً هنا أبداً لتفادي تعطّل التطبيق من كوروتين خلفي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:342]

```
343:         if (!permissionManager.hasBluetoothPermissions()) {
```
> شرط: إذا كان مدير الأذونات (permissionManager) لا يملك أذونات البلوتوث (hasBluetoothPermissions). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:343]

```
344:             Log.w(TAG, "Not starting advertising: missing Bluetooth permissions")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم (TAG) ونص «Not starting advertising: missing Bluetooth permissions» (لا يُبدأ الإعلان: أذونات بلوتوث مفقودة). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:344]

```
345:             return
```
> يُعاد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:345]

```
346:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:346]

```
347:         if (bluetoothAdapter == null) {
```
> شرط: إذا كان مُحوِّل البلوتوث (bluetoothAdapter) فارغاً (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:347]

```
348:             Log.w(TAG, "Not starting advertising: bluetoothAdapter is null")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم (TAG) ونص «Not starting advertising: bluetoothAdapter is null» (لا يُبدأ الإعلان: مُحوِّل البلوتوث فارغ). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:348]

```
349:             return
```
> يُعاد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:349]

```
350:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:350]

```
351:         if (!isActive) {
```
> شرط: إذا لم يكن نشِطاً (isActive). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:351]

```
352:             Log.d(TAG, "Not starting advertising: manager not active")
```
> يُستدعى تسجيل تصحيح (Log.d) بالوسم (TAG) ونص «Not starting advertising: manager not active» (لا يُبدأ الإعلان: المدير غير نشِط). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:352]

```
353:             return
```
> يُعاد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:353]

```
354:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:354]

```
355:         if (!enabled) {
```
> شرط: إذا لم يكن مُفعَّلاً (enabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:355]

```
356:             Log.i(TAG, "Not starting advertising: GATT Server disabled via debug settings")
```
> يُستدعى تسجيل معلومات (Log.i) بالوسم (TAG) ونص «Not starting advertising: GATT Server disabled via debug settings» (لا يُبدأ الإعلان: خادم جات مُعطَّل عبر إعدادات التصحيح). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:356]

```
357:             return
```
> يُعاد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:357]

```
358:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:358]

```
359:         if (bleAdvertiser == null) {
```
> شرط: إذا كان مُعلِن البلوتوث منخفض الطاقة (bleAdvertiser) فارغاً (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:359]

```
360:             Log.w(TAG, "Not starting advertising: BLE advertiser not available on this device")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم (TAG) ونص «Not starting advertising: BLE advertiser not available on this device» (لا يُبدأ الإعلان: مُعلِن BLE غير متوفّر على هذا الجهاز). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:360]

```
361:             return
```
> يُعاد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:361]

```
362:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:362]

```
363:         if (!bluetoothAdapter.isMultipleAdvertisementSupported) {
```
> شرط: إذا كان مُحوِّل البلوتوث (bluetoothAdapter) لا يدعم الإعلان المتعدّد (isMultipleAdvertisementSupported). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:363]

```
364:             Log.w(TAG, "Not starting advertising: multiple advertisement not supported on this device")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم (TAG) ونص «Not starting advertising: multiple advertisement not supported on this device» (لا يُبدأ الإعلان: الإعلان المتعدّد غير مدعوم على هذا الجهاز). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:364]

```
365:             return
```
> يُعاد (return) بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:365]

```
366:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:366]

```
367:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:367]

```
368:         val settings = powerManager.getAdvertiseSettings()
```
> يُعرَّف ثابت الإعدادات (settings) ويُسنَد إليه ناتج استدعاء جلب إعدادات الإعلان (getAdvertiseSettings) على مدير الطاقة (powerManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:368]

```
369:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:369]

```
370:         val data = AdvertiseData.Builder()
```
> يُعرَّف ثابت البيانات (data) ويُسنَد إليه كائن بانٍ (Builder) من بيانات الإعلان (AdvertiseData). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:370]

```
371:             .addServiceUuid(ParcelUuid(AppConstants.Mesh.Gatt.SERVICE_UUID))
```
> يُستدعى على البانِي الفعل إضافة مُعرّف خدمة (addServiceUuid) ممرَّراً مُعرّفاً قابلاً للتغليف (ParcelUuid) مبنيّاً من ثابت مُعرّف الخدمة (AppConstants.Mesh.Gatt.SERVICE_UUID). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:371]

```
372:             .setIncludeTxPowerLevel(false)
```
> يُستدعى الفعل ضبط تضمين مستوى قدرة الإرسال (setIncludeTxPowerLevel) بالقيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:372]

```
373:             .setIncludeDeviceName(false)
```
> يُستدعى الفعل ضبط تضمين اسم الجهاز (setIncludeDeviceName) بالقيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:373]

```
374:             .build()
```
> يُستدعى الفعل بناء (build) لإنتاج الكائن النهائي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:374]

```
375:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:375]

```
376:         // Add stable identity (first 8 bytes of peerID) to Scan Response
```
> تعليق: أضِف هويّة ثابتة (أوّل ٨ بايتات من مُعرّف القرين) إلى ردّ المسح (Scan Response). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:376]

```
377:         // This allows scanners to deduplicate devices even if MAC address rotates
```
> تعليق: هذا يسمح للماسحات بإزالة تكرار الأجهزة حتى لو دار عنوان MAC. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:377]

```
378:         val peerIDBytes = try {
```
> يُعرَّف ثابت بايتات مُعرّف القرين (peerIDBytes) ويُسنَد إليه ناتج كتلة محاوَلة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:378]

```
379:             myPeerID.chunked(2).map { it.toInt(16).toByte() }.toByteArray().take(8).toByteArray()
```
> يُؤخَذ مُعرّف القرين الخاص بي (myPeerID) فيُقسَّم إلى مقاطع طول كل منها ٢ (chunked) ثم يُحوَّل كل مقطع (map) إلى عدد صحيح بالأساس ١٦ (toInt(16)) فبايت (toByte) ثم يُحوَّل إلى مصفوفة بايتات (toByteArray) ثم تُؤخَذ أوّل ٨ (take(8)) ثم تُحوَّل إلى مصفوفة بايتات (toByteArray). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:379]

```
380:         } catch (e: Exception) {
```
> اصطياد (catch) استثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:380]

```
381:             ByteArray(0)
```
> تُنتَج مصفوفة بايتات (ByteArray) بطول صفر كقيمة الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:381]

```
382:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:382]

```
383:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:383]

```
384:         val scanResponse = AdvertiseData.Builder()
```
> يُعرَّف ثابت ردّ المسح (scanResponse) ويُسنَد إليه كائن بانٍ (Builder) من بيانات الإعلان (AdvertiseData). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:384]

```
385:             .addServiceData(ParcelUuid(AppConstants.Mesh.Gatt.SERVICE_UUID), peerIDBytes)
```
> يُستدعى على البانِي الفعل إضافة بيانات خدمة (addServiceData) ممرَّراً مُعرّفاً قابلاً للتغليف (ParcelUuid) من ثابت مُعرّف الخدمة (AppConstants.Mesh.Gatt.SERVICE_UUID) وبايتات مُعرّف القرين (peerIDBytes). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:385]

```
386:             .setIncludeTxPowerLevel(false)
```
> يُستدعى الفعل ضبط تضمين مستوى قدرة الإرسال (setIncludeTxPowerLevel) بالقيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:386]

```
387:             .setIncludeDeviceName(false)
```
> يُستدعى الفعل ضبط تضمين اسم الجهاز (setIncludeDeviceName) بالقيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:387]

```
388:             .build()
```
> يُستدعى الفعل بناء (build) لإنتاج الكائن النهائي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:388]

```
389:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:389]

```
390:         advertiseCallback = object : AdvertiseCallback() {
```
> يُسنَد إلى نداء الإعلان الراجع (advertiseCallback) كائن مجهول (object) يرث من نداء الإعلان الراجع (AdvertiseCallback). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:390]

```
391:             override fun onStartSuccess(settingsInEffect: AdvertiseSettings) {
```
> تعريف دالة متجاوِزة (override) باسم عند نجاح البدء (onStartSuccess) تأخذ مَعلَمة الإعدادات السارية (settingsInEffect) من نوع إعدادات الإعلان (AdvertiseSettings). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:391]

```
392:                 advertiseRetryCount = 0
```
> يُسنَد إلى عدّاد إعادة محاوَلة الإعلان (advertiseRetryCount) القيمة صفر. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:392]

```
393:                 val mode = try {
```
> يُعرَّف ثابت الوضع (mode) ويُسنَد إليه ناتج كتلة محاوَلة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:393]

```
394:                     powerManager.getPowerInfo().split("Current Mode: ")[1].split("\n")[0]
```
> يُستدعى على مدير الطاقة (powerManager) الفعل جلب معلومات الطاقة (getPowerInfo) ثم تُقسَّم النتيجة (split) عند النص «Current Mode: » ويُؤخَذ العنصر رقم ١ ثم تُقسَّم عند سطر جديد («\n») ويُؤخَذ العنصر رقم ٠. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:394]

```
395:                 } catch (_: Exception) { "unknown" }
```
> اصطياد (catch) استثناء (Exception) بمتغيّر مُهمَل (_) وتُنتَج القيمة «unknown» (غير معروف) كقيمة الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:395]

```
396:                 Log.i(TAG, "Advertising started (power mode: $mode) with stable ID: ${peerIDBytes.joinToString("") { "%02x".format(it) }}")
```
> يُستدعى تسجيل معلومات (Log.i) بالوسم (TAG) ونص «Advertising started (power mode:» (بدأ الإعلان (وضع الطاقة:)) متبوعاً بالوضع (mode) ثم «with stable ID:» ثم بايتات مُعرّف القرين (peerIDBytes) مدموجة نصّاً بتنسيق كل بايت ست عشري بخانتين («%02x»). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:396]

```
397:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:397]

```
398:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:398]

```
399:             override fun onStartFailure(errorCode: Int) {
```
> تعريف دالة متجاوِزة (override) باسم عند فشل البدء (onStartFailure) تأخذ مَعلَمة رمز الخطأ (errorCode) من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:399]

```
400:                 Log.e(TAG, "Advertising failed: $errorCode")
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم (TAG) ونص «Advertising failed:» (فشل الإعلان) متبوعاً برمز الخطأ (errorCode). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:400]
