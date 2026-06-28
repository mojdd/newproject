# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt (الأسطر 401–482)

```
401:                // Previously this only logged, so if advertising failed this device became
```
> تعليق: في السابق كان هذا يسجّل فقط في السجل، فإذا فشل الإعلان (advertising) يصبح هذا الجهاز. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:401]

```
402:                // undiscoverable until a manual BLE toggle. Retry transient failures with backoff.
```
> تعليق: غير قابل للاكتشاف حتى تبديل يدوي للبلوتوث منخفض الطاقة (BLE)؛ أعد محاولة الإخفاقات العابرة مع مهلة تراجع (backoff). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:402]

```
403:                when (errorCode) {
```
> تبدأ بنية تفريع (when) تختبر قيمة رمز الخطأ (errorCode). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:403]

```
404:                    ADVERTISE_FAILED_ALREADY_STARTED ->
```
> فرع لقيمة «فشل الإعلان لأنه بدأ مسبقاً» (ADVERTISE_FAILED_ALREADY_STARTED). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:404]

```
405:                        Log.w(TAG, "ADVERTISE_FAILED_ALREADY_STARTED - already advertising, no retry")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم (TAG) والنص "ADVERTISE_FAILED_ALREADY_STARTED - already advertising, no retry". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:405]

```
406:                    ADVERTISE_FAILED_DATA_TOO_LARGE ->
```
> فرع لقيمة «فشل الإعلان لأن البيانات كبيرة جداً» (ADVERTISE_FAILED_DATA_TOO_LARGE). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:406]

```
407:                        Log.e(TAG, "ADVERTISE_FAILED_DATA_TOO_LARGE - config issue, not retrying")
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم والنص "ADVERTISE_FAILED_DATA_TOO_LARGE - config issue, not retrying". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:407]

```
408:                    ADVERTISE_FAILED_FEATURE_UNSUPPORTED ->
```
> فرع لقيمة «فشل الإعلان لأن الميزة غير مدعومة» (ADVERTISE_FAILED_FEATURE_UNSUPPORTED). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:408]

```
409:                        Log.e(TAG, "ADVERTISE_FAILED_FEATURE_UNSUPPORTED - unsupported, not retrying")
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم والنص "ADVERTISE_FAILED_FEATURE_UNSUPPORTED - unsupported, not retrying". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:409]

```
410:                    ADVERTISE_FAILED_TOO_MANY_ADVERTISERS -> {
```
> فرع لقيمة «فشل الإعلان لكثرة المُعلِنين» (ADVERTISE_FAILED_TOO_MANY_ADVERTISERS) ويفتح كتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:410]

```
411:                        Log.w(TAG, "ADVERTISE_FAILED_TOO_MANY_ADVERTISERS - will retry after backoff")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم والنص "ADVERTISE_FAILED_TOO_MANY_ADVERTISERS - will retry after backoff". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:411]

```
412:                        scheduleAdvertiseRestart("too-many-advertisers")
```
> تُستدعى دالة جدولة إعادة تشغيل الإعلان (scheduleAdvertiseRestart) بالوسيط "too-many-advertisers". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:412]

```
413:                    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:413]

```
414:                    ADVERTISE_FAILED_INTERNAL_ERROR -> {
```
> فرع لقيمة «فشل الإعلان لخطأ داخلي» (ADVERTISE_FAILED_INTERNAL_ERROR) ويفتح كتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:414]

```
415:                        Log.w(TAG, "ADVERTISE_FAILED_INTERNAL_ERROR - will retry after backoff")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم والنص "ADVERTISE_FAILED_INTERNAL_ERROR - will retry after backoff". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:415]

```
416:                        scheduleAdvertiseRestart("internal-error")
```
> تُستدعى دالة جدولة إعادة تشغيل الإعلان (scheduleAdvertiseRestart) بالوسيط "internal-error". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:416]

```
417:                    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:417]

```
418:                    else -> {
```
> الفرع الافتراضي (else) لأي قيمة أخرى ويفتح كتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:418]

```
419:                        Log.w(TAG, "Unknown advertise failure $errorCode - will retry after backoff")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم والنص "Unknown advertise failure " مع إدراج قيمة رمز الخطأ (errorCode) ثم " - will retry after backoff". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:419]

```
420:                        scheduleAdvertiseRestart("unknown-$errorCode")
```
> تُستدعى دالة جدولة إعادة تشغيل الإعلان (scheduleAdvertiseRestart) بوسيط نصّي "unknown-" مدمج فيه قيمة رمز الخطأ (errorCode). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:420]

```
421:                    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:421]

```
422:                }
```
> إغلاق نطاق (نهاية بنية when). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:422]

```
423:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:423]

```
424:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:424]

```
425:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:425]

```
426:        try {
```
> تبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:426]

```
427:            bleAdvertiser.startAdvertising(settings, data, scanResponse, advertiseCallback)
```
> يُستدعى على المُعلِن (bleAdvertiser) التابع بدء الإعلان (startAdvertising) بالوسائط: الإعدادات (settings) والبيانات (data) واستجابة الفحص (scanResponse) ونداء الإعلان الراجع (advertiseCallback). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:427]

```
428:        } catch (se: SecurityException) {
```
> كتلة التقاط استثناء الأمان (SecurityException) باسم se. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:428]

```
429:            Log.e(TAG, "SecurityException starting advertising (missing permission?): ${se.message}")
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم والنص "SecurityException starting advertising (missing permission?): " مدمجاً فيه رسالة الاستثناء (se.message). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:429]

```
430:        } catch (e: Exception) {
```
> كتلة التقاط استثناء عام (Exception) باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:430]

```
431:            Log.e(TAG, "Exception starting advertising: ${e.message}")
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم والنص "Exception starting advertising: " مدمجاً فيه رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:431]

```
432:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:432]

```
433:    }
```
> إغلاق نطاق (نهاية الدالة). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:433]

```
434:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:434]

```
435:    /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:435]

```
436:     * Stop advertising
```
> تعليق: إيقاف الإعلان. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:436]

```
437:     */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:437]

```
438:    @Suppress("DEPRECATION")
```
> تعليق توضيحي (annotation) كبت تحذير الإهمال (Suppress) بالوسيط "DEPRECATION". [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:438]

```
439:    private fun stopAdvertising() {
```
> تُعرَّف دالة خاصة (private) باسم إيقاف الإعلان (stopAdvertising) بلا وسائط وتفتح كتلتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:439]

```
440:        if (!permissionManager.hasBluetoothPermissions() || bleAdvertiser == null) return
```
> شرط: إذا لم يملك مدير الأذونات (permissionManager) أذونات البلوتوث (hasBluetoothPermissions) أو كان المُعلِن (bleAdvertiser) مساوياً null، فالعودة (return). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:440]

```
441:        try {
```
> تبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:441]

```
442:            advertiseCallback?.let { cb -> bleAdvertiser.stopAdvertising(cb) }
```
> إن كان نداء الإعلان الراجع (advertiseCallback) غير null، يُنفَّذ let بمعامله cb فيُستدعى على المُعلِن (bleAdvertiser) التابع إيقاف الإعلان (stopAdvertising) بالوسيط cb. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:442]

```
443:        } catch (e: Exception) {
```
> كتلة التقاط استثناء عام (Exception) باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:443]

```
444:            Log.w(TAG, "Error stopping advertising: ${e.message}")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم والنص "Error stopping advertising: " مدمجاً فيه رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:444]

```
445:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:445]

```
446:    }
```
> إغلاق نطاق (نهاية الدالة). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:446]

```
447:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:447]

```
448:    /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:448]

```
449:     * Schedule an advertising restart with incremental backoff after a transient failure.
```
> تعليق: جدولة إعادة تشغيل الإعلان مع تراجع تزايدي (backoff) بعد فشل عابر. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:449]

```
450:     */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:450]

```
451:    private fun scheduleAdvertiseRestart(reason: String) {
```
> تُعرَّف دالة خاصة (private) باسم جدولة إعادة تشغيل الإعلان (scheduleAdvertiseRestart) بوسيط نصّي (String) باسم السبب (reason) وتفتح كتلتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:451]

```
452:        advertiseRetryCount++
```
> يُزاد عدّاد إعادة محاولة الإعلان (advertiseRetryCount) بمقدار واحد. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:452]

```
453:        val delayMs = (ADVERTISE_RETRY_BASE_MS * advertiseRetryCount).coerceAtMost(ADVERTISE_MAX_RETRY_DELAY_MS)
```
> يُعرَّف ثابت محلّي (val) باسم مهلة التأخير بالمللي ثانية (delayMs) قيمته حاصل ضرب القاعدة الزمنية لإعادة المحاولة (ADVERTISE_RETRY_BASE_MS) في عدّاد إعادة المحاولة (advertiseRetryCount) مع تقييده ألا يتجاوز الحد الأقصى لمهلة إعادة المحاولة (ADVERTISE_MAX_RETRY_DELAY_MS) عبر coerceAtMost. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:453]

```
454:        Log.w(TAG, "Scheduling advertising restart in ${delayMs}ms (attempt $advertiseRetryCount, reason=$reason)")
```
> يُستدعى تسجيل تحذير (Log.w) بالوسم والنص "Scheduling advertising restart in " مدمجاً فيه قيمة delayMs ثم "ms (attempt " مع عدّاد إعادة المحاولة (advertiseRetryCount) ثم ", reason=" مع قيمة السبب (reason). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:454]

```
455:        connectionScope.launch {
```
> يُستدعى على نطاق الاتصال (connectionScope) التابع إطلاق (launch) ويفتح كتلة الإجراء المعلّق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:455]

```
456:            delay(delayMs)
```
> يُستدعى التعليق الزمني (delay) بمدة delayMs. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:456]

```
457:            if (isActive && isServerRoleEnabled()) {
```
> شرط: إذا كان نشطاً (isActive) ودالة تمكين دور الخادم (isServerRoleEnabled) تُعيد true، تُفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:457]

```
458:                stopAdvertising()
```
> تُستدعى دالة إيقاف الإعلان (stopAdvertising) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:458]

```
459:                delay(100)
```
> يُستدعى التعليق الزمني (delay) بمدة 100. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:459]

```
460:                startAdvertising()
```
> تُستدعى دالة بدء الإعلان (startAdvertising) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:460]

```
461:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:461]

```
462:        }
```
> إغلاق نطاق (نهاية كتلة launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:462]

```
463:    }
```
> إغلاق نطاق (نهاية الدالة). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:463]

```
464:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:464]

```
465:    /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:465]

```
466:     * Restart advertising (for power mode changes)
```
> تعليق: إعادة تشغيل الإعلان (لأجل تغييرات وضع الطاقة). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:466]

```
467:     */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:467]

```
468:    fun restartAdvertising() {
```
> تُعرَّف دالة عامة باسم إعادة تشغيل الإعلان (restartAdvertising) بلا وسائط وتفتح كتلتها. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:468]

```
469:        // Respect debug setting
```
> تعليق: احترِم إعداد التصحيح (debug). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:469]

```
470:        val enabled = isServerRoleEnabled()
```
> يُعرَّف ثابت محلّي (val) باسم مُمكَّن (enabled) قيمته ناتج استدعاء دالة تمكين دور الخادم (isServerRoleEnabled). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:470]

```
471:        if (!isActive || !enabled) {
```
> شرط: إذا لم يكن نشطاً (isActive) أو لم يكن مُمكَّناً (enabled)، تُفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:471]

```
472:            stopAdvertising()
```
> تُستدعى دالة إيقاف الإعلان (stopAdvertising) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:472]

```
473:            return
```
> عودة (return) من الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:473]

```
474:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:474]

```
475:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:475]

```
476:        connectionScope.launch {
```
> يُستدعى على نطاق الاتصال (connectionScope) التابع إطلاق (launch) ويفتح كتلة الإجراء المعلّق. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:476]

```
477:            stopAdvertising()
```
> تُستدعى دالة إيقاف الإعلان (stopAdvertising) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:477]

```
478:            delay(100)
```
> يُستدعى التعليق الزمني (delay) بمدة 100. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:478]

```
479:            startAdvertising()
```
> تُستدعى دالة بدء الإعلان (startAdvertising) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:479]

```
480:        }
```
> إغلاق نطاق (نهاية كتلة launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:480]

```
481:    }
```
> إغلاق نطاق (نهاية الدالة). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:481]

```
482:}
```
> إغلاق نطاق (نهاية الصنف/الملف). [app/src/main/java/com/bitchat/android/mesh/BluetoothGattServerManager.kt:482]
