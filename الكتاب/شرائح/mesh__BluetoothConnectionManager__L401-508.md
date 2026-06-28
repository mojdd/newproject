# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt (الأسطر 401–508)

```
401:     fun connectToAddress(address: String): Boolean {
```
> تعريف دالة (function) باسم «الاتصال بعنوان» (connectToAddress) تأخذ مُعامِلاً نصياً اسمه «العنوان» (address) من نوع نص (String) وتُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:401]

```
402:         if (!isActive || !isBleTransportEnabled()) return false
```
> شرط: إذا كان «نشط» (isActive) غير صحيح أو كانت دالة «هل نقل البلوتوث منخفض الطاقة مُفعّل» (isBleTransportEnabled) تُعيد غير صحيح، فأعِد قيمة غير صحيح (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:402]

```
403:         return clientManager.connectToAddress(address)
```
> أعِد ناتج استدعاء دالة «الاتصال بعنوان» (connectToAddress) من «مدير العميل» (clientManager) مع تمرير «العنوان» (address). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:403]

```
404:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:404]

```
405:     fun disconnectAddress(address: String) { connectionTracker.disconnectDevice(address) }
```
> تعريف دالة باسم «قطع اتصال عنوان» (disconnectAddress) تأخذ نصاً اسمه «العنوان» (address)، وجسمها يستدعي دالة «قطع اتصال جهاز» (disconnectDevice) من «متتبّع الاتصال» (connectionTracker) مع تمرير «العنوان». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:405]

```
406: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:406]

```
407: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:407]

```
408:     // Optionally disconnect all connections (server and client)
```
> تعليق: اختيارياً اقطع كل الاتصالات (الخادم والعميل). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:408]

```
409:     fun disconnectAll() {
```
> تعريف دالة باسم «قطع الكل» (disconnectAll) بلا مُعامِلات. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:409]

```
410:         connectionScope.launch {
```
> استدعاء دالة «أطلِق» (launch) على «نطاق الاتصال» (connectionScope) مع فتح كتلة شفرة (lambda). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:410]

```
411:             // Stop and restart to force disconnects
```
> تعليق: أوقِف ثم أعِد التشغيل لفرض قطع الاتصالات. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:411]

```
412:             clientManager.stop()
```
> استدعاء دالة «أوقِف» (stop) من «مدير العميل» (clientManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:412]

```
413:             serverManager.stop()
```
> استدعاء دالة «أوقِف» (stop) من «مدير الخادم» (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:413]

```
414:             delay(200)
```
> استدعاء دالة «تأخير» (delay) بقيمة ٢٠٠ (بالأجزاء من الألف من الثانية). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:414]

```
415:             if (isActive && isBleTransportEnabled()) {
```
> شرط: إذا كان «نشط» (isActive) صحيحاً وكانت دالة «هل نقل البلوتوث منخفض الطاقة مُفعّل» (isBleTransportEnabled) تُعيد صحيح، فافتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:415]

```
416:                 // Restart managers if service is active
```
> تعليق: أعِد تشغيل المُدراء إذا كانت الخدمة نشطة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:416]

```
417:                 if (isGattServerEnabled()) serverManager.start()
```
> شرط: إذا كانت دالة «هل خادم جات مُفعّل» (isGattServerEnabled) تُعيد صحيح، فاستدعِ دالة «ابدأ» (start) من «مدير الخادم» (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:417]

```
418:                 if (isGattClientEnabled()) clientManager.start()
```
> شرط: إذا كانت دالة «هل عميل جات مُفعّل» (isGattClientEnabled) تُعيد صحيح، فاستدعِ دالة «ابدأ» (start) من «مدير العميل» (clientManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:418]

```
419:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:419]

```
420:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:420]

```
421:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:421]

```
422: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:422]

```
423: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:423]

```
424:     /**
```
> تعليق: بداية تعليق توثيقي (مُتعدّد الأسطر). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:424]

```
425:      * Get connected device count
```
> تعليق: احصل على عدد الأجهزة المتصلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:425]

```
426:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:426]

```
427:     fun getConnectedDeviceCount(): Int = connectionTracker.getConnectedDeviceCount()
```
> تعريف دالة باسم «احصل على عدد الأجهزة المتصلة» (getConnectedDeviceCount) تُعيد عدداً صحيحاً (Int) قيمتُه ناتج استدعاء دالة «احصل على عدد الأجهزة المتصلة» (getConnectedDeviceCount) من «متتبّع الاتصال» (connectionTracker). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:427]

```
428:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:428]

```
429:     /**
```
> تعليق: بداية تعليق توثيقي (مُتعدّد الأسطر). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:429]

```
430:      * Get debug information including power management
```
> تعليق: احصل على معلومات التنقيح بما فيها إدارة الطاقة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:430]

```
431:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:431]

```
432:     fun getDebugInfo(): String {
```
> تعريف دالة باسم «احصل على معلومات التنقيح» (getDebugInfo) تُعيد نصاً (String). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:432]

```
433:         return buildString {
```
> أعِد ناتج دالة «ابنِ نصاً» (buildString) مع فتح كتلة الشفرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:433]

```
434:             appendLine("=== Bluetooth Connection Manager ===")
```
> استدعاء دالة «أضِف سطراً» (appendLine) بالنص الحرفي «=== Bluetooth Connection Manager ===». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:434]

```
435:             appendLine("Bluetooth MAC Address: ${bluetoothAdapter?.address}")
```
> استدعاء دالة «أضِف سطراً» (appendLine) بنص يبدأ بـ «Bluetooth MAC Address: » متبوعاً بقيمة الخاصية «العنوان» (address) من «مُحوّل البلوتوث» (bluetoothAdapter) بأمان من العدم (?.). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:435]

```
436:             appendLine("Active: $isActive")
```
> استدعاء دالة «أضِف سطراً» (appendLine) بنص يبدأ بـ «Active: » متبوعاً بقيمة «نشط» (isActive). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:436]

```
437:             appendLine("Bluetooth Enabled: ${bluetoothAdapter?.isEnabled}")
```
> استدعاء دالة «أضِف سطراً» (appendLine) بنص يبدأ بـ «Bluetooth Enabled: » متبوعاً بقيمة الخاصية «مُفعّل» (isEnabled) من «مُحوّل البلوتوث» (bluetoothAdapter) بأمان من العدم (?.). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:437]

```
438:             appendLine("Has Permissions: ${permissionManager.hasBluetoothPermissions()}")
```
> استدعاء دالة «أضِف سطراً» (appendLine) بنص يبدأ بـ «Has Permissions: » متبوعاً بناتج استدعاء دالة «هل يملك أذونات البلوتوث» (hasBluetoothPermissions) من «مدير الأذونات» (permissionManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:438]

```
439:             appendLine("GATT Server Active: ${serverManager.getGattServer() != null}")
```
> استدعاء دالة «أضِف سطراً» (appendLine) بنص يبدأ بـ «GATT Server Active: » متبوعاً بنتيجة المقارنة: هل ناتج استدعاء دالة «احصل على خادم جات» (getGattServer) من «مدير الخادم» (serverManager) لا يساوي العدم (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:439]

```
440:             appendLine()
```
> استدعاء دالة «أضِف سطراً» (appendLine) بلا وسائط (تُضيف سطراً فارغاً). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:440]

```
441:             appendLine(powerManager.getPowerInfo())
```
> استدعاء دالة «أضِف سطراً» (appendLine) بناتج استدعاء دالة «احصل على معلومات الطاقة» (getPowerInfo) من «مدير الطاقة» (powerManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:441]

```
442:             appendLine()
```
> استدعاء دالة «أضِف سطراً» (appendLine) بلا وسائط (تُضيف سطراً فارغاً). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:442]

```
443:             appendLine(connectionTracker.getDebugInfo())
```
> استدعاء دالة «أضِف سطراً» (appendLine) بناتج استدعاء دالة «احصل على معلومات التنقيح» (getDebugInfo) من «متتبّع الاتصال» (connectionTracker). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:443]

```
444:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:444]

```
445:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:445]

```
446:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:446]

```
447:     // MARK: - PowerManagerDelegate Implementation
```
> تعليق: علامة (MARK) — تنفيذ مُفوَّض مدير الطاقة (PowerManagerDelegate Implementation). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:447]

```
448:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:448]

```
449:     override fun onPowerModeChanged(newMode: PowerManager.PowerMode) {
```
> تعريف دالة مُتجاوِزة (override) باسم «عند تغيّر وضع الطاقة» (onPowerModeChanged) تأخذ مُعامِلاً اسمه «الوضع الجديد» (newMode) من نوع «وضع الطاقة» (PowerMode) التابع لـ «مدير الطاقة» (PowerManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:449]

```
450:         Log.i(TAG, "Power mode changed to: $newMode")
```
> استدعاء دالة التسجيل المعلوماتي «i» على «السجل» (Log) بالوسم (TAG) ونص «Power mode changed to: » متبوعاً بقيمة «الوضع الجديد» (newMode). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:450]

```
451:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:451]

```
452:         connectionScope.launch {
```
> استدعاء دالة «أطلِق» (launch) على «نطاق الاتصال» (connectionScope) مع فتح كتلة الشفرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:452]

```
453:             if (!isActive || !isBleTransportEnabled()) {
```
> شرط: إذا كان «نشط» (isActive) غير صحيح أو كانت دالة «هل نقل البلوتوث منخفض الطاقة مُفعّل» (isBleTransportEnabled) تُعيد غير صحيح، فافتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:453]

```
454:                 serverManager.stop()
```
> استدعاء دالة «أوقِف» (stop) من «مدير الخادم» (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:454]

```
455:                 clientManager.stop()
```
> استدعاء دالة «أوقِف» (stop) من «مدير العميل» (clientManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:455]

```
456:                 return@launch
```
> أعِد التحكّم خارجاً من كتلة «أطلِق» (return@launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:456]

```
457:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:457]

```
458: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:458]

```
459:             // Avoid rapid scan restarts by checking if we need to change scan behavior
```
> تعليق: تجنّب إعادة تشغيل المسح السريعة بالتحقق مما إذا كنا بحاجة لتغيير سلوك المسح. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:459]

```
460:             val wasUsingDutyCycle = powerManager.shouldUseDutyCycle()
```
> تعريف متغيّر ثابت (val) باسم «كان يستخدم دورة العمل» (wasUsingDutyCycle) قيمتُه ناتج استدعاء دالة «هل ينبغي استخدام دورة العمل» (shouldUseDutyCycle) من «مدير الطاقة» (powerManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:460]

```
461:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:461]

```
462:             // Update advertising with new power settings if server enabled
```
> تعليق: حدّث الإعلان بإعدادات الطاقة الجديدة إذا كان الخادم مُفعّلاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:462]

```
463:             val serverEnabled = isGattServerEnabled()
```
> تعريف متغيّر ثابت (val) باسم «الخادم مُفعّل» (serverEnabled) قيمتُه ناتج استدعاء دالة «هل خادم جات مُفعّل» (isGattServerEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:463]

```
464:             if (serverEnabled) {
```
> شرط: إذا كان «الخادم مُفعّل» (serverEnabled) صحيحاً، فافتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:464]

```
465:                 serverManager.restartAdvertising()
```
> استدعاء دالة «أعِد تشغيل الإعلان» (restartAdvertising) من «مدير الخادم» (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:465]

```
466:             } else {
```
> وإلّا (else) افتح الكتلة البديلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:466]

```
467:                 serverManager.stop()
```
> استدعاء دالة «أوقِف» (stop) من «مدير الخادم» (serverManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:467]

```
468:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:468]

```
469:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:469]

```
470:             // Only restart scanning if the duty cycle behavior changed
```
> تعليق: أعِد تشغيل المسح فقط إذا تغيّر سلوك دورة العمل. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:470]

```
471:             val nowUsingDutyCycle = powerManager.shouldUseDutyCycle()
```
> تعريف متغيّر ثابت (val) باسم «يستخدم الآن دورة العمل» (nowUsingDutyCycle) قيمتُه ناتج استدعاء دالة «هل ينبغي استخدام دورة العمل» (shouldUseDutyCycle) من «مدير الطاقة» (powerManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:471]

```
472:             if (wasUsingDutyCycle != nowUsingDutyCycle) {
```
> شرط: إذا كان «كان يستخدم دورة العمل» (wasUsingDutyCycle) لا يساوي «يستخدم الآن دورة العمل» (nowUsingDutyCycle)، فافتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:472]

```
473:                 Log.d(TAG, "Duty cycle behavior changed (${wasUsingDutyCycle} -> ${nowUsingDutyCycle}), restarting scan")
```
> استدعاء دالة التسجيل التنقيحي «d» على «السجل» (Log) بالوسم (TAG) ونص «Duty cycle behavior changed (» متبوعاً بقيمة «كان يستخدم دورة العمل» (wasUsingDutyCycle) ثم « -> » ثم قيمة «يستخدم الآن دورة العمل» (nowUsingDutyCycle) ثم «), restarting scan». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:473]

```
474:                 val clientEnabled = isGattClientEnabled()
```
> تعريف متغيّر ثابت (val) باسم «العميل مُفعّل» (clientEnabled) قيمتُه ناتج استدعاء دالة «هل عميل جات مُفعّل» (isGattClientEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:474]

```
475:                 if (clientEnabled) {
```
> شرط: إذا كان «العميل مُفعّل» (clientEnabled) صحيحاً، فافتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:475]

```
476:                     clientManager.restartScanning()
```
> استدعاء دالة «أعِد تشغيل المسح» (restartScanning) من «مدير العميل» (clientManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:476]

```
477:                 } else {
```
> وإلّا (else) افتح الكتلة البديلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:477]

```
478:                     clientManager.stop()
```
> استدعاء دالة «أوقِف» (stop) من «مدير العميل» (clientManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:478]

```
479:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:479]

```
480:             } else {
```
> وإلّا (else) افتح الكتلة البديلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:480]

```
481:                 Log.d(TAG, "Duty cycle behavior unchanged, keeping existing scan state")
```
> استدعاء دالة التسجيل التنقيحي «d» على «السجل» (Log) بالوسم (TAG) ونص «Duty cycle behavior unchanged, keeping existing scan state». [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:481]

```
482:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:482]

```
483:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:483]

```
484:             // Enforce connection limits
```
> تعليق: افرِض حدود الاتصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:484]

```
485:             enforceStrictLimits()
```
> استدعاء دالة «افرِض الحدود الصارمة» (enforceStrictLimits). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:485]

```
486:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:486]

```
487:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:487]

```
488:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:488]

```
489:     override fun onScanStateChanged(shouldScan: Boolean) {
```
> تعريف دالة مُتجاوِزة (override) باسم «عند تغيّر حالة المسح» (onScanStateChanged) تأخذ مُعامِلاً منطقياً (Boolean) اسمه «ينبغي المسح» (shouldScan). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:489]

```
490:         if (!isActive || !isBleTransportEnabled()) {
```
> شرط: إذا كان «نشط» (isActive) غير صحيح أو كانت دالة «هل نقل البلوتوث منخفض الطاقة مُفعّل» (isBleTransportEnabled) تُعيد غير صحيح، فافتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:490]

```
491:             clientManager.onScanStateChanged(false)
```
> استدعاء دالة «عند تغيّر حالة المسح» (onScanStateChanged) من «مدير العميل» (clientManager) مع تمرير قيمة غير صحيح (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:491]

```
492:             return
```
> أعِد التحكّم خارجاً من الدالة (return). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:492]

```
493:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:493]

```
494:         clientManager.onScanStateChanged(shouldScan)
```
> استدعاء دالة «عند تغيّر حالة المسح» (onScanStateChanged) من «مدير العميل» (clientManager) مع تمرير «ينبغي المسح» (shouldScan). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:494]

```
495:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:495]

```
496:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:496]

```
497:     // MARK: - Private Implementation - All moved to component managers
```
> تعليق: علامة (MARK) — تنفيذ خاص (Private Implementation) — نُقِل كلّه إلى مُدراء المكوّنات. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:497]

```
498: }
```
> إغلاق نطاق (نهاية الصنف). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:498]

```
499: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:499]

```
500: /**
```
> تعليق: بداية تعليق توثيقي (مُتعدّد الأسطر). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:500]

```
501:  * Delegate interface for Bluetooth connection manager callbacks
```
> تعليق: واجهة المُفوَّض لِردّات نداء مدير اتصال البلوتوث. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:501]

```
502:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:502]

```
503: interface BluetoothConnectionManagerDelegate {
```
> تعريف واجهة (interface) باسم «مُفوَّض مدير اتصال البلوتوث» (BluetoothConnectionManagerDelegate) مع فتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:503]

```
504:     fun onPacketReceived(packet: BitchatPacket, peerID: String, device: BluetoothDevice?)
```
> تصريح دالة باسم «عند استقبال حزمة» (onPacketReceived) تأخذ مُعامِلاً «الحزمة» (packet) من نوع «حزمة بِت‌تشات» (BitchatPacket)، ومُعامِلاً «معرّف النظير» (peerID) من نوع نص (String)، ومُعامِلاً «الجهاز» (device) من نوع «جهاز بلوتوث» (BluetoothDevice) قابل للعدم (?). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:504]

```
505:     fun onDeviceConnected(device: BluetoothDevice)
```
> تصريح دالة باسم «عند اتصال جهاز» (onDeviceConnected) تأخذ مُعامِلاً «الجهاز» (device) من نوع «جهاز بلوتوث» (BluetoothDevice). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:505]

```
506:     fun onDeviceDisconnected(device: BluetoothDevice)
```
> تصريح دالة باسم «عند قطع اتصال جهاز» (onDeviceDisconnected) تأخذ مُعامِلاً «الجهاز» (device) من نوع «جهاز بلوتوث» (BluetoothDevice). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:506]

```
507:     fun onRSSIUpdated(deviceAddress: String, rssi: Int)
```
> تصريح دالة باسم «عند تحديث قوة الإشارة» (onRSSIUpdated) تأخذ مُعامِلاً «عنوان الجهاز» (deviceAddress) من نوع نص (String)، ومُعامِلاً «قوة الإشارة المستقبَلة» (rssi) من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:507]

```
508: }
```
> إغلاق نطاق (نهاية الواجهة). [app/src/main/java/com/bitchat/android/mesh/BluetoothConnectionManager.kt:508]
