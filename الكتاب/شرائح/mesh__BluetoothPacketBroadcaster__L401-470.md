# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt (الأسطر 401–470)

```
401:         gattServer: BluetoothGattServer?,
```
> تعريف وسيط (parameter) اسمه خادم جات (gattServer) من نوع خادم جات بلوتوث (BluetoothGattServer) يقبل القيمة الفارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:401]

```
402:         characteristic: BluetoothGattCharacteristic?
```
> تعريف وسيط اسمه الخاصية (characteristic) من نوع خاصية جات بلوتوث (BluetoothGattCharacteristic) يقبل القيمة الفارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:402]

```
403:     ): Boolean {
```
> إغلاق قائمة الوسطاء وتحديد نوع القيمة المعادة بأنها قيمة منطقية (Boolean)، ثم فتح جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:403]

```
404:         return try {
```
> إعادة (return) نتيجة كتلة المحاولة (try) التي تبدأ هنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:404]

```
405:             characteristic?.let { char ->
```
> استدعاء الدالة let على الخاصية إن لم تكن فارغة، مع تسمية المعطى داخل الكتلة char. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:405]

```
406:                 char.value = data
```
> ضبط الحقل value للخاصية char إلى قيمة المتغيّر data. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:406]

```
407:                 val result = gattServer?.notifyCharacteristicChanged(device, char, false) ?: false
```
> تعريف ثابت (val) اسمه النتيجة (result) يساوي ناتج استدعاء notifyCharacteristicChanged على خادم جات إن لم يكن فارغاً بالوسطاء device وchar وفالس (false)، وإلا يساوي القيمة فالس عبر معامل إلفيس (?:). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:407]

```
408:                 result
```
> إرجاع قيمة الثابت result كنتيجة لكتلة let. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:408]

```
409:             } ?: false
```
> إغلاق كتلة let، ثم عبر معامل إلفيس إعادة القيمة فالس إذا كانت الخاصية فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:409]

```
410:         } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وفتح كتلة التقاط (catch) تمسك باستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:410]

```
411:             Log.w(TAG, "Error sending to server connection ${device.address}: ${e.message}")
```
> استدعاء Log.w لتسجيل تحذير بالوسم TAG ونص يحوي عنوان الجهاز device.address ورسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:411]

```
412:             connectionScope.launch {
```
> استدعاء launch على نطاق الاتصال (connectionScope) لإطلاق مهمة متزامنة، وفتح كتلتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:412]

```
413:                 delay(CLEANUP_DELAY)
```
> استدعاء delay لتأخير التنفيذ بمقدار الثابت CLEANUP_DELAY. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:413]

```
414:                 connectionTracker.removeSubscribedDevice(device)
```
> استدعاء removeSubscribedDevice على متتبّع الاتصال (connectionTracker) بالوسيط device. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:414]

```
415:                 connectionTracker.addressPeerMap.remove(device.address)
```
> استدعاء remove على الخريطة addressPeerMap التابعة لمتتبّع الاتصال بالمفتاح device.address. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:415]

```
416:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:416]

```
417:             false
```
> إعادة القيمة فالس كنتيجة لكتلة الالتقاط. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:417]

```
418:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:418]

```
419:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:419]

```
420: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:420]

```
421:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:421]

```
422:      * Send data to a single device (client->server)
```
> تعليق: إرسال بيانات إلى جهاز واحد (من العميل إلى الخادم). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:422]

```
423:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:423]

```
424:     private fun writeToDeviceConn(
```
> تعريف دالة خاصة (private fun) اسمها الكتابة إلى اتصال الجهاز (writeToDeviceConn) وفتح قائمة وسطائها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:424]

```
425:         deviceConn: BluetoothConnectionTracker.DeviceConnection, 
```
> تعريف وسيط اسمه اتصال الجهاز (deviceConn) من نوع اتصال الجهاز (DeviceConnection) المعرّف داخل BluetoothConnectionTracker. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:425]

```
426:         data: ByteArray
```
> تعريف وسيط اسمه البيانات (data) من نوع مصفوفة بايتات (ByteArray). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:426]

```
427:     ): Boolean {
```
> إغلاق قائمة الوسطاء وتحديد نوع القيمة المعادة بأنها قيمة منطقية (Boolean)، ثم فتح جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:427]

```
428:         return try {
```
> إعادة نتيجة كتلة المحاولة التي تبدأ هنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:428]

```
429:             deviceConn.characteristic?.let { char ->
```
> استدعاء الدالة let على الحقل characteristic التابع لاتصال الجهاز إن لم يكن فارغاً، مع تسمية المعطى char. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:429]

```
430:                 char.value = data
```
> ضبط الحقل value للخاصية char إلى قيمة المتغيّر data. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:430]

```
431:                 val result = deviceConn.gatt?.writeCharacteristic(char) ?: false
```
> تعريف ثابت اسمه result يساوي ناتج استدعاء writeCharacteristic على الحقل gatt التابع لاتصال الجهاز إن لم يكن فارغاً بالوسيط char، وإلا يساوي القيمة فالس عبر معامل إلفيس. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:431]

```
432:                 result
```
> إرجاع قيمة الثابت result كنتيجة لكتلة let. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:432]

```
433:             } ?: false
```
> إغلاق كتلة let، ثم عبر معامل إلفيس إعادة القيمة فالس إذا كان الحقل characteristic فارغاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:433]

```
434:         } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وفتح كتلة التقاط تمسك باستثناء باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:434]

```
435:             Log.w(TAG, "Error sending to client connection ${deviceConn.device.address}: ${e.message}")
```
> استدعاء Log.w لتسجيل تحذير بالوسم TAG ونص يحوي عنوان الجهاز deviceConn.device.address ورسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:435]

```
436:             connectionScope.launch {
```
> استدعاء launch على نطاق الاتصال لإطلاق مهمة متزامنة، وفتح كتلتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:436]

```
437:                 delay(CLEANUP_DELAY)
```
> استدعاء delay لتأخير التنفيذ بمقدار الثابت CLEANUP_DELAY. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:437]

```
438:                 connectionTracker.cleanupDeviceConnection(deviceConn.device.address)
```
> استدعاء cleanupDeviceConnection على متتبّع الاتصال بالوسيط deviceConn.device.address. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:438]

```
439:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:439]

```
440:             false
```
> إعادة القيمة فالس كنتيجة لكتلة الالتقاط. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:440]

```
441:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:441]

```
442:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:442]

```
443:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:443]

```
444:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:444]

```
445:      * Get debug information
```
> تعليق: الحصول على معلومات التنقيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:445]

```
446:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:446]

```
447:     fun getDebugInfo(): String {
```
> تعريف دالة اسمها الحصول على معلومات التنقيح (getDebugInfo) تعيد سلسلة نصية (String) وتفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:447]

```
448:         return buildString {
```
> إعادة نتيجة استدعاء buildString وفتح كتلته. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:448]

```
449:             appendLine("=== Packet Broadcaster Debug Info ===")
```
> استدعاء appendLine لإلحاق سطر نصي ثابت محتواه "=== Packet Broadcaster Debug Info ===". [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:449]

```
450:             appendLine("Broadcaster Scope Active: ${broadcasterScope.isActive}")
```
> استدعاء appendLine لإلحاق سطر نصي يحوي النص "Broadcaster Scope Active:" مع قيمة isActive لنطاق الباث (broadcasterScope). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:450]

```
451:             appendLine("Actor Channel Closed: ${broadcasterActor.isClosedForSend}")
```
> استدعاء appendLine لإلحاق سطر نصي يحوي النص "Actor Channel Closed:" مع قيمة isClosedForSend لممثّل الباث (broadcasterActor). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:451]

```
452:             appendLine("Connection Scope Active: ${connectionScope.isActive}")
```
> استدعاء appendLine لإلحاق سطر نصي يحوي النص "Connection Scope Active:" مع قيمة isActive لنطاق الاتصال (connectionScope). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:452]

```
453:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:453]

```
454:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:454]

```
455:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:455]

```
456:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:456]

```
457:      * Shutdown the broadcaster actor gracefully
```
> تعليق: إيقاف ممثّل الباث بأسلوب رشيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:457]

```
458:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:458]

```
459:     fun shutdown() {
```
> تعريف دالة اسمها الإيقاف (shutdown) بلا وسطاء وفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:459]

```
460:         Log.d(TAG, "Shutting down BluetoothPacketBroadcaster actor")
```
> استدعاء Log.d لتسجيل رسالة تصحيح بالوسم TAG ونص "Shutting down BluetoothPacketBroadcaster actor". [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:460]

```
461:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:461]

```
462:         // Close the actor gracefully
```
> تعليق: إغلاق الممثّل بأسلوب رشيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:462]

```
463:         broadcasterActor.close()
```
> استدعاء close على ممثّل الباث (broadcasterActor). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:463]

```
464:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:464]

```
465:         // Cancel the broadcaster scope
```
> تعليق: إلغاء نطاق الباث. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:465]

```
466:         broadcasterScope.cancel()
```
> استدعاء cancel على نطاق الباث (broadcasterScope). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:466]

```
467:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:467]

```
468:         Log.d(TAG, "BluetoothPacketBroadcaster shutdown complete")
```
> استدعاء Log.d لتسجيل رسالة تصحيح بالوسم TAG ونص "BluetoothPacketBroadcaster shutdown complete". [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:468]

```
469:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:469]

```
470: }
```
> إغلاق نطاق (نهاية الصنف). [app/src/main/java/com/bitchat/android/mesh/BluetoothPacketBroadcaster.kt:470]
