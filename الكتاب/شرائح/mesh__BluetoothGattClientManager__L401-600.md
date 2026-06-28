# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt (الأسطر 401–600)

```
401:                         // may have silently died (flag wedged true). Force a clean re-arm.
```
> تعليق: قد يكون المسح مات بصمت (العَلَم عالق على القيمة الصحيحة). أجبر إعادة تسليح نظيفة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:401]

```
402:                         Log.w(TAG, "Watchdog: no scan results for ${(now - lastScanResultTime) / 1000}s -> forcing scan restart")
```
> يكتب تحذيراً (Log.w) بالوسم TAG نصّه أن الكلب الحارس (Watchdog) لم يجد نتائج مسح لمدة محسوبة بطرح وقت آخر نتيجة مسح (lastScanResultTime) من الوقت الحالي (now) مقسوماً على ١٠٠٠ ثم يفرض إعادة تشغيل المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:402]

```
403:                         forceRestartScan()
```
> يستدعي دالة فرض إعادة تشغيل المسح (forceRestartScan). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:403]

```
404:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:404]

```
405:                 } catch (e: Exception) {
```
> يلتقط الاستثناء (Exception) ويسميه e ويفتح نطاق المعالجة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:405]

```
406:                     Log.w(TAG, "Scan watchdog error: ${e.message}")
```
> يكتب تحذيراً (Log.w) بالوسم TAG نصّه خطأ كلب حراسة المسح متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:406]

```
407:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:407]

```
408:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:408]

```
409:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:409]

```
410:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:410]

```
411: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:411]

```
412:     private fun stopScanWatchdog() {
```
> يعرّف دالة خاصة (private) اسمها إيقاف كلب حراسة المسح (stopScanWatchdog) بلا وُسطاء ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:412]

```
413:         scanWatchdogJob?.cancel()
```
> يستدعي إلغاء (cancel) على مهمة كلب حراسة المسح (scanWatchdogJob) إن لم تكن فارغة (استدعاء آمن من الفراغ). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:413]

```
414:         scanWatchdogJob = null
```
> يسند القيمة الفارغة (null) إلى مهمة كلب حراسة المسح (scanWatchdogJob). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:414]

```
415:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:415]

```
416: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:416]

```
417:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:417]

```
418:      * Force a clean scan restart, clearing a possibly-wedged isCurrentlyScanning flag.
```
> تعليق: افرض إعادة تشغيل مسح نظيفة، مع مسح عَلَم "يجري المسح حالياً" (isCurrentlyScanning) المحتمَل عَلَقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:418]

```
419:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:419]

```
420:     private fun forceRestartScan() {
```
> يعرّف دالة خاصة (private) اسمها فرض إعادة تشغيل المسح (forceRestartScan) بلا وُسطاء ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:420]

```
421:         stopScanning()
```
> يستدعي دالة إيقاف المسح (stopScanning). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:421]

```
422:         connectionScope.launch {
```
> يطلق متعاوِنة (launch) داخل نطاق الاتصال (connectionScope) ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:422]

```
423:             delay(500)
```
> ينتظر تأخيراً (delay) مقداره ٥٠٠ مليّ ثانية. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:423]

```
424:             if (isActive && scanningDesired && isClientRoleEnabled() && !isCurrentlyScanning) {
```
> يتحقّق شرطاً يجمع: المتعاوِنة نشطة (isActive) و المسح مرغوب (scanningDesired) و دور العميل مُفعَّل (isClientRoleEnabled) و ليس يجري المسح حالياً (isCurrentlyScanning منفيّة)، ثم يفتح نطاق الشرط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:424]

```
425:                 startScanning()
```
> يستدعي دالة بدء المسح (startScanning). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:425]

```
426:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:426]

```
427:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:427]

```
428:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:428]

```
429:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:429]

```
430:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:430]

```
431:      * Handle scan result and initiate connection if appropriate
```
> تعليق: عالِج نتيجة المسح وابدأ الاتصال إن كان مناسباً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:431]

```
432:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:432]

```
433:     private fun handleScanResult(result: ScanResult) {
```
> يعرّف دالة خاصة (private) اسمها معالجة نتيجة المسح (handleScanResult) تأخذ وسيطاً result من نوع نتيجة المسح (ScanResult) ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:433]

```
434:         val device = result.device
```
> يعرّف ثابتاً (val) اسمه الجهاز (device) ويسند إليه خاصية device من النتيجة (result). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:434]

```
435:         val rssi = result.rssi
```
> يعرّف ثابتاً (val) اسمه قوة الإشارة (rssi) ويسند إليه خاصية rssi من النتيجة (result). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:435]

```
436:         val deviceAddress = device.address
```
> يعرّف ثابتاً (val) اسمه عنوان الجهاز (deviceAddress) ويسند إليه خاصية address من الجهاز (device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:436]

```
437:         val scanRecord = result.scanRecord
```
> يعرّف ثابتاً (val) اسمه سجل المسح (scanRecord) ويسند إليه خاصية scanRecord من النتيجة (result). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:437]

```
438:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:438]

```
439:         // CRITICAL: Only process devices that have our service UUID
```
> تعليق: حَرِج: عالِج فقط الأجهزة التي تحمل معرّف خدمتنا (service UUID). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:439]

```
440:         val hasOurService = scanRecord?.serviceUuids?.any { it.uuid == AppConstants.Mesh.Gatt.SERVICE_UUID } == true
```
> يعرّف ثابتاً (val) اسمه يملك خدمتنا (hasOurService) ويسند إليه نتيجة فحص هل أيٌّ (any) من معرّفات خدمات سجل المسح (serviceUuids) يساوي uuidه ثابت SERVICE_UUID من AppConstants.Mesh.Gatt، وتُقارَن النتيجة بالقيمة الصحيحة (true) مع تأمين الاستدعاء من الفراغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:440]

```
441:         if (!hasOurService) {
```
> يتحقّق شرطاً: إن لم يملك خدمتنا (نفي hasOurService) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:441]

```
442:             return
```
> يُعيد (return) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:442]

```
443:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:443]

```
444: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:444]

```
445:         // Proof the scanner is alive and finding our network: refresh liveness and clear backoff.
```
> تعليق: دليل أن الماسح حيّ ويجد شبكتنا: حدِّث الحيوية وامسح التراجع (backoff). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:445]

```
446:         lastScanResultTime = System.currentTimeMillis()
```
> يسند إلى وقت آخر نتيجة مسح (lastScanResultTime) الوقت الحالي بالمليّ ثانية من System.currentTimeMillis. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:446]

```
447:         scanRetryCount = 0
```
> يسند إلى عدّاد إعادة محاولة المسح (scanRetryCount) القيمة صفر. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:447]

```
448: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:448]

```
449:         // Try to extract peerID from Service Data (if available) for stable identity
```
> تعليق: حاوِل استخراج معرّف النِدّ (peerID) من بيانات الخدمة (Service Data) إن توفّرت، لهوية ثابتة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:449]

```
450:         val serviceData = scanRecord?.getServiceData(ParcelUuid(AppConstants.Mesh.Gatt.SERVICE_UUID))
```
> يعرّف ثابتاً (val) اسمه بيانات الخدمة (serviceData) ويسند إليه ناتج استدعاء getServiceData على سجل المسح (scanRecord) بمعرّف ParcelUuid مبني من ثابت SERVICE_UUID، مع تأمين الاستدعاء من الفراغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:450]

```
451:         val peerID = if (serviceData != null && serviceData.size >= 8) {
```
> يعرّف ثابتاً (val) اسمه معرّف النِدّ (peerID) قيمته نتيجة تعبير شرطي: إن كانت بيانات الخدمة (serviceData) ليست فارغة وحجمها أكبر من أو يساوي ٨، ويفتح نطاق الفرع. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:451]

```
452:             serviceData.joinToString("") { "%02x".format(it) }
```
> ينتج سلسلة بضمّ (joinToString) عناصر بيانات الخدمة بفاصل فارغ، مُنسِّقاً كل عنصر (it) إلى صيغة ستّ عشرية من خانتين (‎%02x‎). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:452]

```
453:         } else {
```
> يفتح الفرع البديل (else) للتعبير الشرطي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:453]

```
454:             null
```
> ينتج القيمة الفارغة (null) كنتيجة للفرع البديل. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:454]

```
455:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:455]

```
456: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:456]

```
457:         if (peerID != null) {
```
> يتحقّق شرطاً: إن كان معرّف النِدّ (peerID) ليس فارغاً ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:457]

```
458:             // Log.v(TAG, "Found peerID $peerID in scan record for $deviceAddress")
```
> تعليق: استدعاء سجلّ مفصّل (Log.v) معطَّل نصّه عُثِر على معرّف النِدّ peerID في سجل المسح للعنوان deviceAddress. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:458]

```
459:             if (connectionTracker.isPeerConnected(peerID)) {
```
> يتحقّق شرطاً باستدعاء هل النِدّ متّصل (isPeerConnected) على متتبّع الاتصالات (connectionTracker) ممرّراً معرّف النِدّ (peerID) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:459]

```
460:                  Log.d(TAG, "Deduplication: Peer $peerID is already connected (ignoring $deviceAddress)")
```
> يكتب سجلّ تنقيح (Log.d) بالوسم TAG نصّه إزالة التكرار: النِدّ peerID متّصل بالفعل (يتجاهل deviceAddress). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:460]

```
461:                  return
```
> يُعيد (return) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:461]

```
462:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:462]

```
463:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:463]

```
464: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:464]

```
465:         // Log.d(TAG, "Received scan result from $deviceAddress - already connected: ${connectionTracker.isDeviceConnected(deviceAddress)}")
```
> تعليق: استدعاء سجلّ تنقيح (Log.d) معطَّل نصّه استُلمت نتيجة مسح من deviceAddress مع حالة متّصل بالفعل من isDeviceConnected. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:465]

```
466:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:466]

```
467:         // Store RSSI from scan results for later use (especially for server connections)
```
> تعليق: خزِّن قوة الإشارة (RSSI) من نتائج المسح للاستعمال لاحقاً (خصوصاً لاتصالات الخادم). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:467]

```
468:         connectionTracker.updateScanRSSI(deviceAddress, rssi)
```
> يستدعي تحديث قوة إشارة المسح (updateScanRSSI) على متتبّع الاتصالات (connectionTracker) ممرّراً عنوان الجهاز (deviceAddress) وقوة الإشارة (rssi). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:468]

```
469: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:469]

```
470:         // Publish scan result to debug UI buffer
```
> تعليق: انشر نتيجة المسح إلى مخزن واجهة التنقيح (debug UI buffer). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:470]

```
471:         try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:471]

```
472:             DebugSettingsManager.getInstance().addScanResult(
```
> يستدعي إضافة نتيجة مسح (addScanResult) على نسخة مدير إعدادات التنقيح المفردة (DebugSettingsManager.getInstance) ويفتح قائمة الوُسطاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:472]

```
473:                 DebugScanResult(
```
> يُنشئ كائن نتيجة مسح تنقيح (DebugScanResult) ويفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:473]

```
474:                     deviceName = device.name,
```
> يسند الوسيط اسم الجهاز (deviceName) إلى خاصية name من الجهاز (device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:474]

```
475:                     deviceAddress = deviceAddress,
```
> يسند الوسيط عنوان الجهاز (deviceAddress) إلى المتغيّر deviceAddress. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:475]

```
476:                     rssi = rssi,
```
> يسند الوسيط قوة الإشارة (rssi) إلى المتغيّر rssi. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:476]

```
477:                     peerID = peerID // Use the discovered peerID if available
```
> يسند الوسيط معرّف النِدّ (peerID) إلى المتغيّر peerID، مع تعليق: استعمل معرّف النِدّ المكتشَف إن توفّر. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:477]

```
478:                 )
```
> إغلاق قائمة وُسطاء منشئ DebugScanResult. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:478]

```
479:             )
```
> إغلاق قائمة وُسطاء استدعاء addScanResult. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:479]

```
480:         } catch (_: Exception) { }
```
> يلتقط الاستثناء (Exception) بمتغيّر مهمَل (_) ويترك كتلة المعالجة فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:480]

```
481:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:481]

```
482:         // Power-aware RSSI filtering
```
> تعليق: ترشيح قوة الإشارة (RSSI) المراعي للطاقة (Power-aware). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:482]

```
483:         if (rssi < powerManager.getRSSIThreshold()) {
```
> يتحقّق شرطاً: إن كانت قوة الإشارة (rssi) أقلّ من عتبة قوة الإشارة (getRSSIThreshold) من مدير الطاقة (powerManager) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:483]

```
484:             Log.d(TAG, "Skipping device $deviceAddress due to weak signal: $rssi < ${powerManager.getRSSIThreshold()}")
```
> يكتب سجلّ تنقيح (Log.d) بالوسم TAG نصّه تخطّي الجهاز deviceAddress بسبب إشارة ضعيفة: rssi أقل من عتبة getRSSIThreshold. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:484]

```
485:             // Even if we skip connecting, still publish scan result to debug UI
```
> تعليق: حتى إن تخطّينا الاتصال، انشر نتيجة المسح إلى واجهة التنقيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:485]

```
486:             try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:486]

```
487:                 DebugSettingsManager.getInstance().addScanResult(
```
> يستدعي إضافة نتيجة مسح (addScanResult) على نسخة مدير إعدادات التنقيح المفردة (DebugSettingsManager.getInstance) ويفتح قائمة الوُسطاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:487]

```
488:                     DebugScanResult(
```
> يُنشئ كائن نتيجة مسح تنقيح (DebugScanResult) ويفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:488]

```
489:                         deviceName = device.name,
```
> يسند الوسيط اسم الجهاز (deviceName) إلى خاصية name من الجهاز (device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:489]

```
490:                         deviceAddress = deviceAddress,
```
> يسند الوسيط عنوان الجهاز (deviceAddress) إلى المتغيّر deviceAddress. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:490]

```
491:                         rssi = rssi,
```
> يسند الوسيط قوة الإشارة (rssi) إلى المتغيّر rssi. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:491]

```
492:                         peerID = peerID
```
> يسند الوسيط معرّف النِدّ (peerID) إلى المتغيّر peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:492]

```
493:                     )
```
> إغلاق قائمة وُسطاء منشئ DebugScanResult. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:493]

```
494:                 )
```
> إغلاق قائمة وُسطاء استدعاء addScanResult. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:494]

```
495:             } catch (_: Exception) { }
```
> يلتقط الاستثناء (Exception) بمتغيّر مهمَل (_) ويترك كتلة المعالجة فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:495]

```
496:             return
```
> يُعيد (return) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:496]

```
497:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:497]

```
498:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:498]

```
499:         // Check if already connected OR already attempting to connect
```
> تعليق: تحقّق هل هو متّصل بالفعل أو يجري محاولة الاتصال به بالفعل. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:499]

```
500:         if (connectionTracker.isDeviceConnected(deviceAddress)) {
```
> يتحقّق شرطاً باستدعاء هل الجهاز متّصل (isDeviceConnected) على متتبّع الاتصالات (connectionTracker) ممرّراً عنوان الجهاز (deviceAddress) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:500]

```
501:             return
```
> يُعيد (return) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:501]

```
502:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:502]

```
503:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:503]

```
504:         // Check if connection attempt is allowed
```
> تعليق: تحقّق هل محاولة الاتصال مسموح بها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:504]

```
505:         if (!connectionTracker.isConnectionAttemptAllowed(deviceAddress)) {
```
> يتحقّق شرطاً: إن لم تكن محاولة الاتصال مسموحاً بها (نفي isConnectionAttemptAllowed) على متتبّع الاتصالات (connectionTracker) ممرّراً عنوان الجهاز (deviceAddress) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:505]

```
506:             Log.d(TAG, "Connection to $deviceAddress not allowed due to recent attempts")
```
> يكتب سجلّ تنقيح (Log.d) بالوسم TAG نصّه الاتصال بـ deviceAddress غير مسموح بسبب محاولات حديثة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:506]

```
507:             return
```
> يُعيد (return) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:507]

```
508:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:508]

```
509:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:509]

```
510:         // Check if connection limit is reached
```
> تعليق: تحقّق هل بلغ حدّ الاتصالات (connection limit). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:510]

```
511:         val dbg = try { com.bitchat.android.ui.debug.DebugSettingsManager.getInstance() } catch (_: Exception) { null }
```
> يعرّف ثابتاً (val) اسمه dbg ويسند إليه ناتج كتلة محاولة (try): نسخة مدير إعدادات التنقيح المفردة (DebugSettingsManager.getInstance) من الحزمة com.bitchat.android.ui.debug، وإن وقع استثناء (Exception) بمتغيّر مهمَل (_) فالقيمة الفارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:511]

```
512:         val maxOverall = dbg?.maxConnectionsOverall?.value ?: powerManager.getMaxConnections()
```
> يعرّف ثابتاً (val) اسمه الحدّ الأقصى الإجمالي (maxOverall) ويسند إليه قيمة maxConnectionsOverall.value من dbg مع تأمين الفراغ، وإن كانت فارغة فالحدّ الأقصى للاتصالات (getMaxConnections) من مدير الطاقة (powerManager) عبر معامل إلفيس (?:). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:512]

```
513:         val maxClient = dbg?.maxClientConnections?.value ?: maxOverall
```
> يعرّف ثابتاً (val) اسمه الحدّ الأقصى للعميل (maxClient) ويسند إليه قيمة maxClientConnections.value من dbg مع تأمين الفراغ، وإن كانت فارغة فالحدّ الأقصى الإجمالي (maxOverall) عبر معامل إلفيس (?:). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:513]

```
514: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:514]

```
515:         if (!connectionTracker.canConnectAsClient(maxOverall, maxClient)) {
```
> يتحقّق شرطاً: إن لم يكن بالإمكان الاتصال كعميل (نفي canConnectAsClient) على متتبّع الاتصالات (connectionTracker) ممرّراً الحدّ الأقصى الإجمالي (maxOverall) والحدّ الأقصى للعميل (maxClient) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:515]

```
516:             Log.d(TAG, "Client connection limit reached (overall: $maxOverall, client: $maxClient)")
```
> يكتب سجلّ تنقيح (Log.d) بالوسم TAG نصّه بُلِغ حدّ اتصالات العميل (الإجمالي maxOverall، العميل maxClient). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:516]

```
517:             return
```
> يُعيد (return) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:517]

```
518:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:518]

```
519:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:519]

```
520:         // Add pending connection and start connection
```
> تعليق: أضِف اتصالاً معلَّقاً (pending connection) وابدأ الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:520]

```
521:         if (connectionTracker.addPendingConnection(deviceAddress)) {
```
> يتحقّق شرطاً باستدعاء إضافة اتصال معلَّق (addPendingConnection) على متتبّع الاتصالات (connectionTracker) ممرّراً عنوان الجهاز (deviceAddress) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:521]

```
522:             connectToDevice(device, rssi, peerID)
```
> يستدعي دالة الاتصال بالجهاز (connectToDevice) ممرّراً الجهاز (device) وقوة الإشارة (rssi) ومعرّف النِدّ (peerID). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:522]

```
523:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:523]

```
524:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:524]

```
525:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:525]

```
526:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:526]

```
527:      * Connect to a device as GATT client
```
> تعليق: اتّصل بجهاز كعميل GATT. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:527]

```
528:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:528]

```
529:     @Suppress("DEPRECATION")
```
> توسيم بكبت التحذير (Suppress) للإهمال (DEPRECATION) على ما يليه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:529]

```
530:     private fun connectToDevice(device: BluetoothDevice, rssi: Int, peerID: String? = null) {
```
> يعرّف دالة خاصة (private) اسمها الاتصال بالجهاز (connectToDevice) تأخذ جهازاً (device) من نوع BluetoothDevice وقوة إشارة (rssi) من نوع عدد صحيح (Int) ومعرّف نِدّ (peerID) من نوع نص قابل للفراغ (String?) بقيمة افتراضية فارغة (null)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:530]

```
531:         if (!isClientRoleEnabled()) return
```
> يتحقّق شرطاً: إن لم يكن دور العميل مُفعَّلاً (نفي isClientRoleEnabled) فيُعيد (return) من الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:531]

```
532:         if (!permissionManager.hasBluetoothPermissions()) return
```
> يتحقّق شرطاً: إن لم يملك مدير الأذونات (permissionManager) أذونات بلوتوث (نفي hasBluetoothPermissions) فيُعيد (return) من الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:532]

```
533: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:533]

```
534:         val deviceAddress = device.address
```
> يعرّف ثابتاً (val) اسمه عنوان الجهاز (deviceAddress) ويسند إليه خاصية address من الجهاز (device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:534]

```
535:         Log.i(TAG, "Connecting to bitchat device: $deviceAddress (peerID: $peerID)")
```
> يكتب سجلّ معلومات (Log.i) بالوسم TAG نصّه جارٍ الاتصال بجهاز bitchat: deviceAddress (معرّف النِدّ: peerID). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:535]

```
536:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:536]

```
537:         val gattCallback = object : BluetoothGattCallback() {
```
> يعرّف ثابتاً (val) اسمه ردّ نداء GATT (gattCallback) ويسند إليه كائناً مجهولاً (object) يرث ردّ نداء بلوتوث GATT (BluetoothGattCallback) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:537]

```
538:             override fun onConnectionStateChange(gatt: BluetoothGatt, status: Int, newState: Int) {
```
> يتجاوز (override) دالة عند تغيّر حالة الاتصال (onConnectionStateChange) تأخذ gatt من نوع BluetoothGatt وحالة (status) من نوع عدد صحيح (Int) وحالة جديدة (newState) من نوع عدد صحيح (Int)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:538]

```
539:                 Log.d(TAG, "Client: Connection state change - Device: $deviceAddress, Status: $status, NewState: $newState")
```
> يكتب سجلّ تنقيح (Log.d) بالوسم TAG نصّه العميل: تغيّر حالة الاتصال - الجهاز deviceAddress، الحالة status، الحالة الجديدة newState. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:539]

```
540: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:540]

```
541:                 if (newState == BluetoothProfile.STATE_CONNECTED && status == BluetoothGatt.GATT_SUCCESS) {
```
> يتحقّق شرطاً: إن كانت الحالة الجديدة (newState) تساوي حالة المتّصل (BluetoothProfile.STATE_CONNECTED) و الحالة (status) تساوي نجاح GATT (BluetoothGatt.GATT_SUCCESS) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:541]

```
542:                     Log.i(TAG, "Client: Successfully connected to $deviceAddress. Requesting MTU...")
```
> يكتب سجلّ معلومات (Log.i) بالوسم TAG نصّه العميل: اتّصل بنجاح بـ deviceAddress. يطلب وحدة الإرسال القصوى (MTU). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:542]

```
543:                     // Request a larger MTU. Must be done before any data transfer.
```
> تعليق: اطلب وحدة إرسال قصوى (MTU) أكبر. يجب أن يتمّ قبل أي نقل بيانات. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:543]

```
544:                     connectionScope.launch {
```
> يطلق متعاوِنة (launch) داخل نطاق الاتصال (connectionScope) ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:544]

```
545:                         delay(200) // A small delay can improve reliability of MTU request.
```
> ينتظر تأخيراً (delay) مقداره ٢٠٠ مليّ ثانية، مع تعليق: تأخير صغير يحسّن موثوقية طلب وحدة الإرسال القصوى (MTU). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:545]

```
546:                         gatt.requestMtu(517)
```
> يستدعي طلب وحدة الإرسال القصوى (requestMtu) على gatt ممرّراً القيمة ٥١٧. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:546]

```
547:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:547]

```
548:                 } else if (newState == BluetoothProfile.STATE_DISCONNECTED) {
```
> يفتح فرعاً بديلاً شرطياً (else if): إن كانت الحالة الجديدة (newState) تساوي حالة المنفصل (BluetoothProfile.STATE_DISCONNECTED) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:548]

```
549:                     if (status != BluetoothGatt.GATT_SUCCESS) {
```
> يتحقّق شرطاً: إن كانت الحالة (status) لا تساوي نجاح GATT (BluetoothGatt.GATT_SUCCESS) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:549]

```
550:                         Log.w(TAG, "Client: Disconnected from $deviceAddress with error status $status")
```
> يكتب تحذيراً (Log.w) بالوسم TAG نصّه العميل: انفصل عن deviceAddress بحالة خطأ status. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:550]

```
551:                         if (status == 147) {
```
> يتحقّق شرطاً: إن كانت الحالة (status) تساوي ١٤٧ ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:551]

```
552:                             Log.e(TAG, "Client: Connection establishment failed (status 147) for $deviceAddress")
```
> يكتب سجلّ خطأ (Log.e) بالوسم TAG نصّه العميل: فشل تأسيس الاتصال (الحالة ١٤٧) لـ deviceAddress. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:552]

```
553:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:553]

```
554:                     } else {
```
> يفتح الفرع البديل (else). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:554]

```
555:                         Log.d(TAG, "Client: Cleanly disconnected from $deviceAddress")
```
> يكتب سجلّ تنقيح (Log.d) بالوسم TAG نصّه العميل: انفصل بنظافة عن deviceAddress. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:555]

```
556:                         connectionTracker.cleanupDeviceConnection(deviceAddress)
```
> يستدعي تنظيف اتصال الجهاز (cleanupDeviceConnection) على متتبّع الاتصالات (connectionTracker) ممرّراً عنوان الجهاز (deviceAddress). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:556]

```
557:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:557]

```
558: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:558]

```
559:                     // Notify higher layers about device disconnection to update direct flags
```
> تعليق: أخطِر الطبقات الأعلى بانفصال الجهاز لتحديث الأعلام المباشرة (direct flags). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:559]

```
560:                     delegate?.onDeviceDisconnected(gatt.device)
```
> يستدعي عند انفصال الجهاز (onDeviceDisconnected) على المفوَّض (delegate) مع تأمين الفراغ، ممرّراً جهاز gatt (gatt.device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:560]

```
561: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:561]

```
562:                     connectionScope.launch {
```
> يطلق متعاوِنة (launch) داخل نطاق الاتصال (connectionScope) ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:562]

```
563:                         delay(500) // CLEANUP_DELAY
```
> ينتظر تأخيراً (delay) مقداره ٥٠٠ مليّ ثانية، مع تعليق: تأخير التنظيف (CLEANUP_DELAY). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:563]

```
564:                         try {
```
> يفتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:564]

```
565:                             gatt.close()
```
> يستدعي إغلاق (close) على gatt. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:565]

```
566:                         } catch (e: Exception) {
```
> يلتقط الاستثناء (Exception) ويسميه e ويفتح نطاق المعالجة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:566]

```
567:                             Log.w(TAG, "Error closing GATT: ${e.message}")
```
> يكتب تحذيراً (Log.w) بالوسم TAG نصّه خطأ في إغلاق GATT متبوعاً برسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:567]

```
568:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:568]

```
569:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:569]

```
570:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:570]

```
571:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:571]

```
572:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:572]

```
573:             override fun onMtuChanged(gatt: BluetoothGatt, mtu: Int, status: Int) {
```
> يتجاوز (override) دالة عند تغيّر وحدة الإرسال القصوى (onMtuChanged) تأخذ gatt من نوع BluetoothGatt وقيمة mtu من نوع عدد صحيح (Int) وحالة (status) من نوع عدد صحيح (Int)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:573]

```
574:                 val deviceAddress = gatt.device.address
```
> يعرّف ثابتاً (val) اسمه عنوان الجهاز (deviceAddress) ويسند إليه address من جهاز gatt (gatt.device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:574]

```
575:                 Log.i(TAG, "Client: MTU changed for $deviceAddress to $mtu with status $status")
```
> يكتب سجلّ معلومات (Log.i) بالوسم TAG نصّه العميل: تغيّرت وحدة الإرسال القصوى (MTU) لـ deviceAddress إلى mtu بحالة status. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:575]

```
576: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:576]

```
577:                 if (status == BluetoothGatt.GATT_SUCCESS) {
```
> يتحقّق شرطاً: إن كانت الحالة (status) تساوي نجاح GATT (BluetoothGatt.GATT_SUCCESS) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:577]

```
578:                     Log.i(TAG, "MTU successfully negotiated for $deviceAddress. Discovering services.")
```
> يكتب سجلّ معلومات (Log.i) بالوسم TAG نصّه تمّ التفاوض على وحدة الإرسال القصوى (MTU) بنجاح لـ deviceAddress. يكتشف الخدمات. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:578]

```
579:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:579]

```
580:                     // Now that MTU is set, connection is fully ready.
```
> تعليق: الآن وقد ضُبطت وحدة الإرسال القصوى (MTU)، الاتصال جاهز تماماً. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:580]

```
581:                     val deviceConn = BluetoothConnectionTracker.DeviceConnection(
```
> يعرّف ثابتاً (val) اسمه اتصال الجهاز (deviceConn) ويسند إليه كائن اتصال الجهاز (DeviceConnection) من متتبّع اتصالات بلوتوث (BluetoothConnectionTracker) ويفتح قائمة وُسطائه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:581]

```
582:                         device = gatt.device,
```
> يسند الوسيط الجهاز (device) إلى جهاز gatt (gatt.device). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:582]

```
583:                         gatt = gatt,
```
> يسند الوسيط gatt إلى المتغيّر gatt. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:583]

```
584:                         rssi = rssi,
```
> يسند الوسيط قوة الإشارة (rssi) إلى المتغيّر rssi. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:584]

```
585:                         isClient = true,
```
> يسند الوسيط هل عميل (isClient) القيمة الصحيحة (true). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:585]

```
586:                         peerID = peerID // Store the peerID discovered during scan
```
> يسند الوسيط معرّف النِدّ (peerID) إلى المتغيّر peerID، مع تعليق: خزِّن معرّف النِدّ المكتشَف أثناء المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:586]

```
587:                     )
```
> إغلاق قائمة وُسطاء منشئ DeviceConnection. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:587]

```
588:                     connectionTracker.addDeviceConnection(deviceAddress, deviceConn)
```
> يستدعي إضافة اتصال جهاز (addDeviceConnection) على متتبّع الاتصالات (connectionTracker) ممرّراً عنوان الجهاز (deviceAddress) واتصال الجهاز (deviceConn). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:588]

```
589:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:589]

```
590:                     // Start service discovery only AFTER MTU is set.
```
> تعليق: ابدأ اكتشاف الخدمات فقط بعد ضبط وحدة الإرسال القصوى (MTU). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:590]

```
591:                     gatt.discoverServices()
```
> يستدعي اكتشاف الخدمات (discoverServices) على gatt. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:591]

```
592:                 } else {
```
> يفتح الفرع البديل (else). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:592]

```
593:                     Log.w(TAG, "MTU negotiation failed for $deviceAddress with status: $status. Disconnecting.")
```
> يكتب تحذيراً (Log.w) بالوسم TAG نصّه فشل التفاوض على وحدة الإرسال القصوى (MTU) لـ deviceAddress بالحالة status. يقطع الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:593]

```
594:                     //connectionTracker.removePendingConnection(deviceAddress)
```
> تعليق: استدعاء إزالة الاتصال المعلَّق (removePendingConnection) على متتبّع الاتصالات معطَّل ممرّراً deviceAddress. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:594]

```
595:                     gatt.disconnect()
```
> يستدعي قطع الاتصال (disconnect) على gatt. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:595]

```
596:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:596]

```
597:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:597]

```
598: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:598]

```
599:             override fun onServicesDiscovered(gatt: BluetoothGatt, status: Int) {                
```
> يتجاوز (override) دالة عند اكتشاف الخدمات (onServicesDiscovered) تأخذ gatt من نوع BluetoothGatt وحالة (status) من نوع عدد صحيح (Int)، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:599]

```
600:                 if (status == BluetoothGatt.GATT_SUCCESS) {
```
> يتحقّق شرطاً: إن كانت الحالة (status) تساوي نجاح GATT (BluetoothGatt.GATT_SUCCESS) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattClientManager.kt:600]
