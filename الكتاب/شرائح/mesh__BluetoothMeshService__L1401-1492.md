# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt (الأسطر 1401–1492)

```
1401:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1401]

```
1402:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1402]

```
1403:     /**
```
> بداية كتلة تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1403]

```
1404:      * Sign packet before broadcasting using our signing private key
```
> تعليق: وقّع الحزمة قبل البثّ باستعمال مفتاح التوقيع الخاص بنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1404]

```
1405:      */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1405]

```
1406:     private fun signPacketBeforeBroadcast(packet: BitchatPacket): BitchatPacket {
```
> تعريف دالة خاصة (private) باسم «توقيع الحزمة قبل البثّ» (signPacketBeforeBroadcast) تأخذ مُعامِلاً اسمه packet من نوع BitchatPacket وتُعيد قيمة من نوع BitchatPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1406]

```
1407:         return try {
```
> إعادة (return) نتيجة كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1407]

```
1408:             // Optionally compute and attach a source route for addressed packets
```
> تعليق: احسب اختيارياً وأرفق مساراً مصدرياً للحزم المُعنونة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1408]

```
1409:             val withRoute = try {
```
> تعريف متغيّر ثابت (val) اسمه «مع المسار» (withRoute) وإسناد نتيجة كتلة محاولة (try) إليه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1409]

```
1410:                 val rec = packet.recipientID
```
> تعريف متغيّر ثابت (val) اسمه rec وإسناد قيمة الخاصية recipientID من packet إليه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1410]

```
1411:                 if (rec != null && !rec.contentEquals(SpecialRecipients.BROADCAST)) {
```
> شرط (if): إذا كان rec غير فارغ (null) ومحتواه لا يساوي SpecialRecipients.BROADCAST. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1411]

```
1412:                     val dest = rec.joinToString("") { b -> "%02x".format(b) }
```
> تعريف متغيّر ثابت (val) اسمه dest وإسناد سلسلة ناتجة عن دمج عناصر rec بفاصل فارغ "" مع تنسيق كل بايت b بالنسق الست عشري "%02x". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1412]

```
1413:                     val path = com.bitchat.android.services.meshgraph.RoutePlanner.shortestPath(myPeerID, dest)
```
> تعريف متغيّر ثابت (val) اسمه path وإسناد نتيجة استدعاء الدالة shortestPath من مُخطِّط المسار (RoutePlanner) بالوسيطين myPeerID و dest إليه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1413]

```
1414:                     if (path != null && path.size >= 3) {
```
> شرط (if): إذا كان path غير فارغ (null) وحجمه (size) أكبر من أو يساوي ٣. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1414]

```
1415:                         // Exclude first (sender) and last (recipient); only intermediates
```
> تعليق: استبعد الأول (المرسِل) والأخير (المستلِم)؛ فقط الوسطاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1415]

```
1416:                         val intermediates = path.subList(1, path.size - 1)
```
> تعريف متغيّر ثابت (val) اسمه «الوسطاء» (intermediates) وإسناد القائمة الجزئية (subList) من path من الفهرس ١ إلى path.size - 1 إليه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1416]

```
1417:                         val hopsBytes = intermediates.map { hexStringToByteArray(it) }
```
> تعريف متغيّر ثابت (val) اسمه «بايتات القفزات» (hopsBytes) وإسناد نتيجة تحويل (map) كل عنصر it من intermediates عبر الدالة hexStringToByteArray إليه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1417]

```
1418:                         Log.d(TAG, "✅ Signed packet type ${packet.type} (route ${hopsBytes.size} hops: $intermediates)")
```
> استدعاء Log.d بالوسم TAG ونصّ يُظهر «✅ Signed packet type» متبوعاً بقيمة packet.type ثم «route» وعدد hopsBytes.size قفزات وقيمة intermediates. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1418]

```
1419:                         // Attach route and upgrade to v2 (required for HAS_ROUTE flag)
```
> تعليق: أرفق المسار وارفع الإصدار إلى v2 (مطلوب لراية HAS_ROUTE). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1419]

```
1420:                         packet.copy(route = hopsBytes, version = 2u)
```
> استدعاء packet.copy لإنشاء نسخة من packet مع إسناد route بقيمة hopsBytes و version بقيمة 2u (عدد صحيح غير موقّع). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1420]

```
1421:                     } else packet.copy(route = null)
```
> فرع else: استدعاء packet.copy لإنشاء نسخة من packet مع إسناد route بقيمة null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1421]

```
1422:                 } else packet
```
> فرع else: إعادة قيمة packet كما هي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1422]

```
1423:             } catch (_: Exception) { packet }
```
> كتلة قبض (catch) لاستثناء (Exception) دون اسم، تُعيد قيمة packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1423]

```
1424: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1424]

```
1425:             // Get the canonical packet data for signing (without signature)
```
> تعليق: احصل على بيانات الحزمة القانونية للتوقيع (دون التوقيع). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1425]

```
1426:             val packetDataForSigning = withRoute.toBinaryDataForSigning()
```
> تعريف متغيّر ثابت (val) اسمه «بيانات الحزمة للتوقيع» (packetDataForSigning) وإسناد نتيجة استدعاء الدالة toBinaryDataForSigning على withRoute إليه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1426]

```
1427:             if (packetDataForSigning == null) {
```
> شرط (if): إذا كان packetDataForSigning يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1427]

```
1428:                 Log.w(TAG, "Failed to encode packet type ${packet.type} for signing, sending unsigned")
```
> استدعاء Log.w بالوسم TAG ونصّ «Failed to encode packet type» متبوعاً بقيمة packet.type و«for signing, sending unsigned». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1428]

```
1429:                 return withRoute
```
> إعادة (return) قيمة withRoute. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1429]

```
1430:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1430]

```
1431:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1431]

```
1432:             // Sign the packet data using our signing key
```
> تعليق: وقّع بيانات الحزمة باستعمال مفتاح التوقيع الخاص بنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1432]

```
1433:             val signature = encryptionService.signData(packetDataForSigning)
```
> تعريف متغيّر ثابت (val) اسمه «التوقيع» (signature) وإسناد نتيجة استدعاء الدالة signData على encryptionService بالوسيط packetDataForSigning إليه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1433]

```
1434:             if (signature != null) {
```
> شرط (if): إذا كان signature غير فارغ (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1434]

```
1435:                 Log.d(TAG, "✅ Signed packet type ${packet.type} (signature ${signature.size} bytes)")
```
> استدعاء Log.d بالوسم TAG ونصّ «✅ Signed packet type» متبوعاً بقيمة packet.type و«signature» وحجم signature.size بايت. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1435]

```
1436:                 withRoute.copy(signature = signature)
```
> استدعاء withRoute.copy لإنشاء نسخة من withRoute مع إسناد signature بقيمة signature. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1436]

```
1437:             } else {
```
> فرع else. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1437]

```
1438:                 Log.w(TAG, "Failed to sign packet type ${packet.type}, sending unsigned")
```
> استدعاء Log.w بالوسم TAG ونصّ «Failed to sign packet type» متبوعاً بقيمة packet.type و«sending unsigned». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1438]

```
1439:                 withRoute
```
> إعادة قيمة withRoute كما هي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1439]

```
1440:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1440]

```
1441:         } catch (e: Exception) {
```
> كتلة قبض (catch) لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1441]

```
1442:             Log.w(TAG, "Error signing packet type ${packet.type}: ${e.message}, sending unsigned")
```
> استدعاء Log.w بالوسم TAG ونصّ «Error signing packet type» متبوعاً بقيمة packet.type ورسالة الاستثناء e.message و«sending unsigned». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1442]

```
1443:             packet
```
> إعادة قيمة packet كما هي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1443]

```
1444:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1444]

```
1445:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1445]

```
1446:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1446]

```
1447:     // MARK: - Panic Mode Support
```
> تعليق: MARK: - دعم وضع الذعر (Panic Mode). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1447]

```
1448:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1448]

```
1449:     /**
```
> بداية كتلة تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1449]

```
1450:      * Clear all internal mesh service data (for panic mode)
```
> تعليق: امسح كل بيانات خدمة الشبكة الداخلية (لوضع الذعر). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1450]

```
1451:      */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1451]

```
1452:     fun clearAllInternalData() {
```
> تعريف دالة عامّة باسم «امسح كل البيانات الداخلية» (clearAllInternalData) بلا مُعامِلات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1452]

```
1453:         Log.w(TAG, "🚨 Clearing all mesh service internal data")
```
> استدعاء Log.w بالوسم TAG ونصّ «🚨 Clearing all mesh service internal data». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1453]

```
1454:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1454]

```
1455:             // Stop services to cease broadcasting old ID immediately
```
> تعليق: أوقف الخدمات لتتوقّف فوراً عن بثّ المعرّف القديم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1455]

```
1456:             stopServices()
```
> استدعاء الدالة stopServices. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1456]

```
1457:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1457]

```
1458:             // Clear all managers
```
> تعليق: امسح كل المُدراء (managers). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1458]

```
1459:             fragmentManager.clearAllFragments()
```
> استدعاء الدالة clearAllFragments على مدير الأجزاء (fragmentManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1459]

```
1460:             storeForwardManager.clearAllCache()
```
> استدعاء الدالة clearAllCache على مدير التخزين والتمرير (storeForwardManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1460]

```
1461:             securityManager.clearAllData()
```
> استدعاء الدالة clearAllData على مدير الأمان (securityManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1461]

```
1462:             peerManager.clearAllPeers()
```
> استدعاء الدالة clearAllPeers على مدير الأقران (peerManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1462]

```
1463:             peerManager.clearAllFingerprints()
```
> استدعاء الدالة clearAllFingerprints على مدير الأقران (peerManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1463]

```
1464:             Log.d(TAG, "✅ Cleared all mesh service internal data")
```
> استدعاء Log.d بالوسم TAG ونصّ «✅ Cleared all mesh service internal data». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1464]

```
1465:         } catch (e: Exception) {
```
> كتلة قبض (catch) لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1465]

```
1466:             Log.e(TAG, "❌ Error clearing mesh service internal data: ${e.message}")
```
> استدعاء Log.e بالوسم TAG ونصّ «❌ Error clearing mesh service internal data» متبوعاً برسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1466]

```
1467:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1467]

```
1468:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1468]

```
1469:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1469]

```
1470:     /**
```
> بداية كتلة تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1470]

```
1471:      * Clear all encryption and cryptographic data (for panic mode)
```
> تعليق: امسح كل بيانات التشفير والبيانات التعمياتية (لوضع الذعر). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1471]

```
1472:      */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1472]

```
1473:     fun clearAllEncryptionData() {
```
> تعريف دالة عامّة باسم «امسح كل بيانات التشفير» (clearAllEncryptionData) بلا مُعامِلات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1473]

```
1474:         Log.w(TAG, "🚨 Clearing all encryption data")
```
> استدعاء Log.w بالوسم TAG ونصّ «🚨 Clearing all encryption data». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1474]

```
1475:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1475]

```
1476:             // Clear encryption service persistent identity (includes Ed25519 signing keys)
```
> تعليق: امسح الهوية الدائمة لخدمة التشفير (تشمل مفاتيح التوقيع Ed25519). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1476]

```
1477:             encryptionService.clearPersistentIdentity()
```
> استدعاء الدالة clearPersistentIdentity على خدمة التشفير (encryptionService). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1477]

```
1478:             Log.d(TAG, "✅ Cleared all encryption data")
```
> استدعاء Log.d بالوسم TAG ونصّ «✅ Cleared all encryption data». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1478]

```
1479:         } catch (e: Exception) {
```
> كتلة قبض (catch) لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1479]

```
1480:             Log.e(TAG, "❌ Error clearing encryption data: ${e.message}")
```
> استدعاء Log.e بالوسم TAG ونصّ «❌ Error clearing encryption data» متبوعاً برسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1480]

```
1481:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1481]

```
1482:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1482]

```
1483: }
```
> إغلاق نطاق (نهاية الصنف). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1483]

```
1484: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1484]

```
1485: /**
```
> بداية كتلة تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1485]

```
1486:  * Delegate interface for BLE mesh callbacks. Extends the shared mesh delegate so
```
> تعليق: واجهة مُفوِّض (Delegate) لردود نداء شبكة BLE. تُوسِّع مُفوِّض الشبكة المشترك بحيث. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1486]

```
1487:  * transport-agnostic facades can receive the same callback stream.
```
> تعليق: تستطيع الواجهات المستقلّة عن النقل (transport-agnostic) أن تستقبل تيار ردود النداء نفسه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1487]

```
1488:  */
```
> إغلاق كتلة التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1488]

```
1489: interface BluetoothMeshDelegate : MeshDelegate {
```
> تعريف واجهة (interface) باسم «مُفوِّض شبكة البلوتوث» (BluetoothMeshDelegate) ترث من الواجهة MeshDelegate. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1489]

```
1490:     override fun didReceiveVerifyChallenge(peerID: String, payload: ByteArray, timestampMs: Long)
```
> تعريف دالة مُتجاوِزة (override) باسم didReceiveVerifyChallenge تأخذ المُعامِلات peerID من نوع String و payload من نوع ByteArray و timestampMs من نوع Long. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1490]

```
1491:     override fun didReceiveVerifyResponse(peerID: String, payload: ByteArray, timestampMs: Long)
```
> تعريف دالة مُتجاوِزة (override) باسم didReceiveVerifyResponse تأخذ المُعامِلات peerID من نوع String و payload من نوع ByteArray و timestampMs من نوع Long. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1491]

```
1492: }
```
> إغلاق نطاق (نهاية الواجهة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1492]
