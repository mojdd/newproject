# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt (الأسطر 601–708)

```
601:                     val service = gatt.getService(AppConstants.Mesh.Gatt.SERVICE_UUID)
```
> يُعرَّف متغيّر ثابت اسمه «الخدمة» (service) ويُسنَد إليه ناتج استدعاء getService على الكائن gatt مع تمرير المعرّف SERVICE_UUID من AppConstants.Mesh.Gatt. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:601]

```
602:                     if (service != null) {
```
> شرط (if) يتحقّق من أنّ «الخدمة» (service) ليست قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:602]

```
603:                         val characteristic = service.getCharacteristic(AppConstants.Mesh.Gatt.CHARACTERISTIC_UUID)
```
> يُعرَّف متغيّر ثابت اسمه «الخاصية» (characteristic) ويُسنَد إليه ناتج استدعاء getCharacteristic على «الخدمة» مع تمرير المعرّف CHARACTERISTIC_UUID من AppConstants.Mesh.Gatt. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:603]

```
604:                         if (characteristic != null) {
```
> شرط (if) يتحقّق من أنّ «الخاصية» (characteristic) ليست قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:604]

```
605:                             connectionTracker.getDeviceConnection(deviceAddress)?.let { deviceConn ->
```
> يُستدعى getDeviceConnection على connectionTracker مع تمرير deviceAddress، وإذا لم يكن الناتج فارغاً (?.) يُنفَّذ let بمتغيّر اسمه deviceConn. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:605]

```
606:                                 val updatedConn = deviceConn.copy(characteristic = characteristic)
```
> يُعرَّف متغيّر ثابت اسمه «الاتصال المُحدَّث» (updatedConn) ويُسنَد إليه ناتج copy على deviceConn مع ضبط الحقل characteristic إلى «الخاصية». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:606]

```
607:                                 connectionTracker.updateDeviceConnection(deviceAddress, updatedConn)
```
> يُستدعى updateDeviceConnection على connectionTracker مع تمرير deviceAddress و«الاتصال المُحدَّث» (updatedConn). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:607]

```
608:                                 Log.d(TAG, "Client: Updated device connection with characteristic for $deviceAddress")
```
> يُستدعى Log.d بالوسم TAG ونصّ تشخيص: «Client: حدّثتُ اتصال الجهاز بالخاصية للعنوان $deviceAddress». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:608]

```
609:                             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:609]

```
610:                             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:610]

```
611:                             gatt.setCharacteristicNotification(characteristic, true)
```
> يُستدعى setCharacteristicNotification على gatt مع تمرير «الخاصية» والقيمة true (تفعيل الإشعار). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:611]

```
612:                             val descriptor = characteristic.getDescriptor(AppConstants.Mesh.Gatt.DESCRIPTOR_UUID)
```
> يُعرَّف متغيّر ثابت اسمه «الواصف» (descriptor) ويُسنَد إليه ناتج getDescriptor على «الخاصية» مع تمرير المعرّف DESCRIPTOR_UUID من AppConstants.Mesh.Gatt. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:612]

```
613:                             if (descriptor != null) {
```
> شرط (if) يتحقّق من أنّ «الواصف» (descriptor) ليس قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:613]

```
614:                                 descriptor.value = BluetoothGattDescriptor.ENABLE_NOTIFICATION_VALUE
```
> يُسنَد إلى الحقل value في «الواصف» القيمة الثابتة ENABLE_NOTIFICATION_VALUE من BluetoothGattDescriptor. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:614]

```
615:                                 gatt.writeDescriptor(descriptor)
```
> يُستدعى writeDescriptor على gatt مع تمرير «الواصف» (descriptor). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:615]

```
616:                                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:616]

```
617:                                 connectionScope.launch {
```
> يُستدعى launch على connectionScope لبدء كتلة برمجية متزامنة (coroutine). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:617]

```
618:                                     delay(200)
```
> يُستدعى delay بقيمة 200 (تأخير مئتي وحدة زمنية). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:618]

```
619:                                     Log.i(TAG, "Client: Connection setup complete for $deviceAddress")
```
> يُستدعى Log.i بالوسم TAG ونصّ معلومة: «Client: اكتمل إعداد الاتصال للعنوان $deviceAddress». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:619]

```
620:                                     delegate?.onDeviceConnected(device)
```
> يُستدعى onDeviceConnected على delegate إن لم يكن فارغاً (?.) مع تمرير device. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:620]

```
621:                                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:621]

```
622:                             } else {
```
> فرع بديل (else) للشرط في السطر 613. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:622]

```
623:                                 Log.e(TAG, "Client: CCCD descriptor not found for $deviceAddress")
```
> يُستدعى Log.e بالوسم TAG ونصّ خطأ: «Client: لم يُعثَر على واصف CCCD للعنوان $deviceAddress». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:623]

```
624:                                 gatt.disconnect()
```
> يُستدعى disconnect على gatt (قطع الاتصال). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:624]

```
625:                             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:625]

```
626:                         } else {
```
> فرع بديل (else) للشرط في السطر 604. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:626]

```
627:                             Log.e(TAG, "Client: Required characteristic not found for $deviceAddress")
```
> يُستدعى Log.e بالوسم TAG ونصّ خطأ: «Client: لم يُعثَر على الخاصية المطلوبة للعنوان $deviceAddress». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:627]

```
628:                             gatt.disconnect()
```
> يُستدعى disconnect على gatt (قطع الاتصال). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:628]

```
629:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:629]

```
630:                     } else {
```
> فرع بديل (else) للشرط في السطر 602. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:630]

```
631:                         Log.e(TAG, "Client: Required service not found for $deviceAddress")
```
> يُستدعى Log.e بالوسم TAG ونصّ خطأ: «Client: لم يُعثَر على الخدمة المطلوبة للعنوان $deviceAddress». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:631]

```
632:                         gatt.disconnect()
```
> يُستدعى disconnect على gatt (قطع الاتصال). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:632]

```
633:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:633]

```
634:                 } else {
```
> فرع بديل (else) لشرط سابق غير ظاهر في المدى (يتعلّق بحالة status). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:634]

```
635:                     Log.e(TAG, "Client: Service discovery failed with status $status for $deviceAddress")
```
> يُستدعى Log.e بالوسم TAG ونصّ خطأ: «Client: فشل اكتشاف الخدمة بالحالة $status للعنوان $deviceAddress». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:635]

```
636:                     gatt.disconnect()
```
> يُستدعى disconnect على gatt (قطع الاتصال). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:636]

```
637:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:637]

```
638:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:638]

```
639:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:639]

```
640:             override fun onCharacteristicChanged(gatt: BluetoothGatt, characteristic: BluetoothGattCharacteristic) {
```
> تُعرَّف دالة معاد تعريفها (override) اسمها onCharacteristicChanged بمعاملين: gatt من نوع BluetoothGatt و characteristic من نوع BluetoothGattCharacteristic. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:640]

```
641:                 val value = characteristic.value
```
> يُعرَّف متغيّر ثابت اسمه «القيمة» (value) ويُسنَد إليه الحقل value من «الخاصية» (characteristic). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:641]

```
642:                 Log.i(TAG, "Client: Received packet from ${gatt.device.address}, size: ${value.size} bytes")
```
> يُستدعى Log.i بالوسم TAG ونصّ معلومة: «Client: استلمتُ حزمة من ${gatt.device.address}، الحجم: ${value.size} بايت». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:642]

```
643:                 val packet = BitchatPacket.fromBinaryData(value)
```
> يُعرَّف متغيّر ثابت اسمه «الحزمة» (packet) ويُسنَد إليه ناتج fromBinaryData على BitchatPacket مع تمرير «القيمة» (value). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:643]

```
644:                 if (packet != null) {
```
> شرط (if) يتحقّق من أنّ «الحزمة» (packet) ليست قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:644]

```
645:                     val peerID = packet.senderID.take(8).toByteArray().joinToString("") { "%02x".format(it) }
```
> يُعرَّف متغيّر ثابت اسمه «معرّف النظير» (peerID) ويُسنَد إليه: أخذ أوّل ٨ عناصر من senderID في «الحزمة»، تحويلها إلى مصفوفة بايتات، ثمّ ضمّها نصّاً بلا فاصل بصيغة سداسية عشرية لكلّ بايت "%02x". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:645]

```
646:                     Log.d(TAG, "Client: Parsed packet type ${packet.type} from $peerID")
```
> يُستدعى Log.d بالوسم TAG ونصّ تشخيص: «Client: حلّلتُ حزمة من النوع ${packet.type} من $peerID». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:646]

```
647:                     delegate?.onPacketReceived(packet, peerID, gatt.device)
```
> يُستدعى onPacketReceived على delegate إن لم يكن فارغاً (?.) مع تمرير «الحزمة» و«معرّف النظير» و gatt.device. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:647]

```
648:                 } else {
```
> فرع بديل (else) للشرط في السطر 644. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:648]

```
649:                     Log.w(TAG, "Client: Failed to parse packet from ${gatt.device.address}, size: ${value.size} bytes")
```
> يُستدعى Log.w بالوسم TAG ونصّ تحذير: «Client: فشلتُ في تحليل حزمة من ${gatt.device.address}، الحجم: ${value.size} بايت». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:649]

```
650:                     Log.w(TAG, "Client: Packet data: ${value.joinToString(" ") { "%02x".format(it) }}")
```
> يُستدعى Log.w بالوسم TAG ونصّ تحذير: «Client: بيانات الحزمة: » متبوعاً بضمّ «القيمة» نصّاً بفاصل مسافة بصيغة سداسية عشرية لكلّ بايت "%02x". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:650]

```
651:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:651]

```
652:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:652]

```
653:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:653]

```
654:             override fun onReadRemoteRssi(gatt: BluetoothGatt, rssi: Int, status: Int) {
```
> تُعرَّف دالة معاد تعريفها (override) اسمها onReadRemoteRssi بثلاثة معاملات: gatt من نوع BluetoothGatt و rssi من نوع Int و status من نوع Int. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:654]

```
655:                 val deviceAddress = gatt.device.address
```
> يُعرَّف متغيّر ثابت اسمه «عنوان الجهاز» (deviceAddress) ويُسنَد إليه address من gatt.device. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:655]

```
656:                 if (status == BluetoothGatt.GATT_SUCCESS) {
```
> شرط (if) يتحقّق من أنّ status يساوي الثابت GATT_SUCCESS من BluetoothGatt. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:656]

```
657:                     Log.d(TAG, "Client: RSSI updated for $deviceAddress: $rssi dBm")
```
> يُستدعى Log.d بالوسم TAG ونصّ تشخيص: «Client: تحدّثت قيمة RSSI للعنوان $deviceAddress: $rssi dBm». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:657]

```
658:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:658]

```
659:                     // Update the connection tracker with new RSSI value
```
> تعليق: حدّث متعقّب الاتصال بقيمة RSSI الجديدة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:659]

```
660:                     connectionTracker.getDeviceConnection(deviceAddress)?.let { deviceConn ->
```
> يُستدعى getDeviceConnection على connectionTracker مع تمرير «عنوان الجهاز»، وإذا لم يكن الناتج فارغاً (?.) يُنفَّذ let بمتغيّر اسمه deviceConn. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:660]

```
661:                         val updatedConn = deviceConn.copy(rssi = rssi)
```
> يُعرَّف متغيّر ثابت اسمه «الاتصال المُحدَّث» (updatedConn) ويُسنَد إليه ناتج copy على deviceConn مع ضبط الحقل rssi إلى قيمة rssi. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:661]

```
662:                         connectionTracker.updateDeviceConnection(deviceAddress, updatedConn)
```
> يُستدعى updateDeviceConnection على connectionTracker مع تمرير «عنوان الجهاز» و«الاتصال المُحدَّث». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:662]

```
663:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:663]

```
664:                 } else {
```
> فرع بديل (else) للشرط في السطر 656. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:664]

```
665:                     Log.w(TAG, "Client: Failed to read RSSI for $deviceAddress, status: $status")
```
> يُستدعى Log.w بالوسم TAG ونصّ تحذير: «Client: فشلتُ في قراءة RSSI للعنوان $deviceAddress، الحالة: $status». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:665]

```
666:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:666]

```
667:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:667]

```
668:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:668]

```
669:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:669]

```
670:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:670]

```
671:             Log.d(TAG, "Client: Attempting GATT connection to $deviceAddress with autoConnect=false")
```
> يُستدعى Log.d بالوسم TAG ونصّ تشخيص: «Client: أحاول اتصال GATT بالعنوان $deviceAddress مع autoConnect=false». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:671]

```
672:             val gatt = device.connectGatt(context, false, gattCallback, BluetoothDevice.TRANSPORT_LE)
```
> يُعرَّف متغيّر ثابت اسمه gatt ويُسنَد إليه ناتج connectGatt على device مع تمرير context والقيمة false ثمّ gattCallback والثابت TRANSPORT_LE من BluetoothDevice. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:672]

```
673:             if (gatt == null) {
```
> شرط (if) يتحقّق من أنّ gatt يساوي قيمة فارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:673]

```
674:                 Log.e(TAG, "connectGatt returned null for $deviceAddress")
```
> يُستدعى Log.e بالوسم TAG ونصّ خطأ: «connectGatt أعادت null للعنوان $deviceAddress». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:674]

```
675:                 // keep the pending connection so we can avoid too many reconnections attempts, TODO: needs testing
```
> تعليق: أبقِ الاتصال المعلّق لتجنّب محاولات إعادة اتصال كثيرة جداً، TODO: يحتاج اختباراً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:675]

```
676:                 // connectionTracker.removePendingConnection(deviceAddress)
```
> تعليق: سطر مُعطَّل (مُعلَّق) يستدعي removePendingConnection على connectionTracker مع تمرير deviceAddress. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:676]

```
677:             } else {
```
> فرع بديل (else) للشرط في السطر 673. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:677]

```
678:                 Log.d(TAG, "Client: GATT connection initiated successfully for $deviceAddress")
```
> يُستدعى Log.d بالوسم TAG ونصّ تشخيص: «Client: بُدِئ اتصال GATT بنجاح للعنوان $deviceAddress». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:678]

```
679:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:679]

```
680:         } catch (e: Exception) {
```
> بداية كتلة التقاط (catch) للاستثناء e من نوع Exception. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:680]

```
681:             Log.e(TAG, "Client: Exception connecting to $deviceAddress: ${e.message}")
```
> يُستدعى Log.e بالوسم TAG ونصّ خطأ: «Client: استثناء عند الاتصال بالعنوان $deviceAddress: ${e.message}». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:681]

```
682:             // keep the pending connection so we can avoid too many reconnections attempts, TODO: needs testing
```
> تعليق: أبقِ الاتصال المعلّق لتجنّب محاولات إعادة اتصال كثيرة جداً، TODO: يحتاج اختباراً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:682]

```
683:             // connectionTracker.removePendingConnection(deviceAddress)
```
> تعليق: سطر مُعطَّل (مُعلَّق) يستدعي removePendingConnection على connectionTracker مع تمرير deviceAddress. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:683]

```
684:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:684]

```
685:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:685]

```
686:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:686]

```
687:     /**
```
> تعليق: بداية كتلة توثيق (Javadoc/KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:687]

```
688:      * Restart scanning for power mode changes
```
> تعليق: أعِد تشغيل المسح من أجل تغيّرات وضع الطاقة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:688]

```
689:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:689]

```
690:     fun restartScanning() {
```
> تُعرَّف دالة اسمها «إعادة تشغيل المسح» (restartScanning) بلا معاملات. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:690]

```
691:         // Respect debug setting
```
> تعليق: احترم إعداد التنقيح (debug). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:691]

```
692:         val enabled = isClientRoleEnabled()
```
> يُعرَّف متغيّر ثابت اسمه «مُفعَّل» (enabled) ويُسنَد إليه ناتج استدعاء isClientRoleEnabled. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:692]

```
693:         if (!isActive || !enabled) return
```
> شرط (if): إن كان isActive غير محقّق (!) أو «مُفعَّل» غير محقّق فإنّه يُعاد (return) أي يُخرَج من الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:693]

```
694:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:694]

```
695:         connectionScope.launch {
```
> يُستدعى launch على connectionScope لبدء كتلة برمجية متزامنة (coroutine). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:695]

```
696:             stopScanning()
```
> يُستدعى stopScanning (إيقاف المسح). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:696]

```
697:             delay(1000) // Extra delay to avoid rate limiting
```
> يُستدعى delay بقيمة 1000، مع تعليق: تأخير إضافي لتجنّب تحديد المعدّل (rate limiting). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:697]

```
698:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:698]

```
699:             if (powerManager.shouldUseDutyCycle()) {
```
> شرط (if) يتحقّق من ناتج استدعاء shouldUseDutyCycle على powerManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:699]

```
700:                 Log.i(TAG, "Switching to duty cycle scanning mode")
```
> يُستدعى Log.i بالوسم TAG ونصّ معلومة: «أبدّل إلى وضع مسح دورة العمل (duty cycle)». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:700]

```
701:                 // Duty cycle will handle scanning
```
> تعليق: دورة العمل (duty cycle) ستتولّى المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:701]

```
702:             } else {
```
> فرع بديل (else) للشرط في السطر 699. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:702]

```
703:                 Log.i(TAG, "Switching to continuous scanning mode")
```
> يُستدعى Log.i بالوسم TAG ونصّ معلومة: «أبدّل إلى وضع المسح المتواصل». [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:703]

```
704:                 startScanning()
```
> يُستدعى startScanning (بدء المسح). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:704]

```
705:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:705]

```
706:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:706]

```
707:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:707]

```
708: } 
```
> إغلاق نطاق (نهاية الصنف). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:708]
