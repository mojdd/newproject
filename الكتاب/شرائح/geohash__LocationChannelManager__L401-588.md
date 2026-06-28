# شريحة — app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt (الأسطر 401–588)

```
401:             try {
```
> بداية كتلة محاولة (try) لاحتواء الأخطاء. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:401]

```
402:                 Log.d(TAG, "Starting reverse geocoding")
```
> يُسجَّل سطر تصحيح (Log.d) بالوسم TAG ونصّه "Starting reverse geocoding". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:402]

```
403:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:403]

```
404:                 val addresses = geocoderProvider.getFromLocation(location.latitude, location.longitude, 1)
```
> يُعرَّف الثابت (addresses) ويُسنَد إليه ناتج استدعاء getFromLocation على مزوّد الترميز الجغرافي (geocoderProvider) بمعاملات خط العرض location.latitude وخط الطول location.longitude والعدد 1. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:404]

```
405: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:405]

```
406:                 if (!isActive) return@launch
```
> إذا كان isActive غير محقّق (نفي) يُنفَّذ الرجوع return@launch للخروج من كتلة launch. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:406]

```
407: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:407]

```
408:                 if (addresses.isNotEmpty()) {
```
> إذا كانت addresses غير فارغة (isNotEmpty) تُفتَح كتلة الشرط. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:408]

```
409:                     val address = addresses[0]
```
> يُعرَّف الثابت (address) ويُسنَد إليه العنصر الأول من addresses عند الفهرس 0. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:409]

```
410:                     val names = namesByLevel(address)
```
> يُعرَّف الثابت (names) ويُسنَد إليه ناتج استدعاء الدالة namesByLevel بالمعامل address. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:410]

```
411:                     Log.d(TAG, "Reverse geocoding result: $names")
```
> يُسجَّل سطر تصحيح (Log.d) بالوسم TAG ونصّه "Reverse geocoding result: " متبوعاً بقيمة names. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:411]

```
412:                     _locationNames.value = names
```
> تُسنَد قيمة names إلى الخاصية value للحقل _locationNames. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:412]

```
413:                 } else {
```
> إغلاق كتلة الشرط وفتح كتلة وإلّا (else). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:413]

```
414:                     Log.w(TAG, "No reverse geocoding results")
```
> يُسجَّل سطر تحذير (Log.w) بالوسم TAG ونصّه "No reverse geocoding results". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:414]

```
415:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:415]

```
416:             } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وفتح كتلة التقاط (catch) للاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:416]

```
417:                 if (e !is CancellationException) {
```
> إذا لم يكن e من نوع استثناء الإلغاء (CancellationException) تُفتَح كتلة الشرط. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:417]

```
418:                     Log.e(TAG, "Reverse geocoding failed: ${e.message}")
```
> يُسجَّل سطر خطأ (Log.e) بالوسم TAG ونصّه "Reverse geocoding failed: " متبوعاً بقيمة e.message. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:418]

```
419:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:419]

```
420:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:420]

```
421:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:421]

```
422:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:422]

```
423: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:423]

```
424:     private fun namesByLevel(address: android.location.Address): Map<GeohashChannelLevel, String> {
```
> تُعرَّف دالة خاصة (private) باسم namesByLevel تأخذ معاملاً address من نوع android.location.Address وتُعيد خريطة (Map) مفتاحها GeohashChannelLevel وقيمتها String. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:424]

```
425:         val dict = mutableMapOf<GeohashChannelLevel, String>()
```
> يُعرَّف الثابت (dict) ويُسنَد إليه خريطة قابلة للتعديل (mutableMapOf) مفتاحها GeohashChannelLevel وقيمتها String. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:425]

```
426:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:426]

```
427:         // Country
```
> تعليق: بلد. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:427]

```
428:         address.countryName?.takeIf { it.isNotEmpty() }?.let {
```
> يُؤخَذ address.countryName بأمان، وإن لم يكن فارغاً (takeIf مع isNotEmpty) تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:428]

```
429:             dict[GeohashChannelLevel.REGION] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.REGION. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:429]

```
430:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:430]

```
431:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:431]

```
432:         // Province (state/province or county or city)
```
> تعليق: مقاطعة (ولاية/مقاطعة أو محافظة أو مدينة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:432]

```
433:         address.adminArea?.takeIf { it.isNotEmpty() }?.let {
```
> يُؤخَذ address.adminArea بأمان، وإن لم يكن فارغاً (takeIf مع isNotEmpty) تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:433]

```
434:             dict[GeohashChannelLevel.PROVINCE] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.PROVINCE. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:434]

```
435:         } ?: address.subAdminArea?.takeIf { it.isNotEmpty() }?.let {
```
> إغلاق كتلة let السابقة، ثم بمعامل إلفيس (?:) يُؤخَذ address.subAdminArea بأمان، وإن لم يكن فارغاً تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:435]

```
436:             dict[GeohashChannelLevel.PROVINCE] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.PROVINCE. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:436]

```
437:         } ?: address.locality?.takeIf { it.isNotEmpty() }?.let {
```
> إغلاق كتلة let السابقة، ثم بمعامل إلفيس (?:) يُؤخَذ address.locality بأمان، وإن لم يكن فارغاً تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:437]

```
438:             dict[GeohashChannelLevel.PROVINCE] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.PROVINCE. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:438]

```
439:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:439]

```
440:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:440]

```
441:         // City (locality)
```
> تعليق: مدينة (المنطقة المحلّية). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:441]

```
442:         address.locality?.takeIf { it.isNotEmpty() }?.let {
```
> يُؤخَذ address.locality بأمان، وإن لم يكن فارغاً (takeIf مع isNotEmpty) تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:442]

```
443:             dict[GeohashChannelLevel.CITY] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.CITY. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:443]

```
444:         } ?: address.subAdminArea?.takeIf { it.isNotEmpty() }?.let {
```
> إغلاق كتلة let السابقة، ثم بمعامل إلفيس (?:) يُؤخَذ address.subAdminArea بأمان، وإن لم يكن فارغاً تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:444]

```
445:             dict[GeohashChannelLevel.CITY] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.CITY. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:445]

```
446:         } ?: address.adminArea?.takeIf { it.isNotEmpty() }?.let {
```
> إغلاق كتلة let السابقة، ثم بمعامل إلفيس (?:) يُؤخَذ address.adminArea بأمان، وإن لم يكن فارغاً تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:446]

```
447:             dict[GeohashChannelLevel.CITY] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.CITY. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:447]

```
448:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:448]

```
449:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:449]

```
450:         // Neighborhood
```
> تعليق: حيّ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:450]

```
451:         address.subLocality?.takeIf { it.isNotEmpty() }?.let {
```
> يُؤخَذ address.subLocality بأمان، وإن لم يكن فارغاً (takeIf مع isNotEmpty) تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:451]

```
452:             dict[GeohashChannelLevel.NEIGHBORHOOD] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.NEIGHBORHOOD. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:452]

```
453:         } ?: address.locality?.takeIf { it.isNotEmpty() }?.let {
```
> إغلاق كتلة let السابقة، ثم بمعامل إلفيس (?:) يُؤخَذ address.locality بأمان، وإن لم يكن فارغاً تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:453]

```
454:             dict[GeohashChannelLevel.NEIGHBORHOOD] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.NEIGHBORHOOD. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:454]

```
455:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:455]

```
456:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:456]

```
457:         // Block: reuse neighborhood/locality granularity without exposing street level
```
> تعليق: مربّع سكني: إعادة استخدام دقّة الحيّ/المنطقة المحلّية دون كشف مستوى الشارع. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:457]

```
458:         address.subLocality?.takeIf { it.isNotEmpty() }?.let {
```
> يُؤخَذ address.subLocality بأمان، وإن لم يكن فارغاً (takeIf مع isNotEmpty) تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:458]

```
459:             dict[GeohashChannelLevel.BLOCK] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.BLOCK. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:459]

```
460:         } ?: address.locality?.takeIf { it.isNotEmpty() }?.let {
```
> إغلاق كتلة let السابقة، ثم بمعامل إلفيس (?:) يُؤخَذ address.locality بأمان، وإن لم يكن فارغاً تُفتَح كتلة let على قيمته it. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:460]

```
461:             dict[GeohashChannelLevel.BLOCK] = it
```
> تُسنَد القيمة it إلى dict عند المفتاح GeohashChannelLevel.BLOCK. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:461]

```
462:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:462]

```
463:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:463]

```
464:         return dict
```
> تُعيد الدالة الخريطة dict. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:464]

```
465:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:465]

```
466: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:466]

```
467:     // MARK: - Channel Persistence
```
> تعليق: علامة: حفظ القناة (Channel Persistence). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:467]

```
468:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:468]

```
469:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:469]

```
470:      * Save current channel selection to persistent storage
```
> تعليق: حفظ اختيار القناة الحالي في التخزين الدائم. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:470]

```
471:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:471]

```
472:     private fun saveChannelSelection(channel: ChannelID) {
```
> تُعرَّف دالة خاصة (private) باسم saveChannelSelection تأخذ معاملاً channel من نوع ChannelID. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:472]

```
473:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:473]

```
474:             val channelData = when (channel) {
```
> يُعرَّف الثابت (channelData) ويُسنَد إليه ناتج تعبير when على القيمة channel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:474]

```
475:                 is ChannelID.Mesh -> gson.toJson(PersistedChannel(mesh = true))
```
> إذا كان channel من نوع ChannelID.Mesh يُعاد ناتج gson.toJson لكائن PersistedChannel بالمعامل mesh = true. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:475]

```
476:                 is ChannelID.Location -> gson.toJson(
```
> إذا كان channel من نوع ChannelID.Location يُستدعى gson.toJson (بداية الوسيط). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:476]

```
477:                     PersistedChannel(
```
> يُنشَأ كائن PersistedChannel (بداية الوسائط). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:477]

```
478:                         mesh = false,
```
> يُمرَّر المعامل mesh بالقيمة false. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:478]

```
479:                         level = channel.channel.level.name,
```
> يُمرَّر المعامل level بقيمة channel.channel.level.name. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:479]

```
480:                         geohash = channel.channel.geohash
```
> يُمرَّر المعامل geohash بقيمة channel.channel.geohash. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:480]

```
481:                     )
```
> إغلاق وسائط كائن PersistedChannel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:481]

```
482:                 )
```
> إغلاق وسيط استدعاء gson.toJson. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:482]

```
483:             }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:483]

```
484:             dataManager?.saveLastGeohashChannel(channelData)
```
> يُستدعى بأمان saveLastGeohashChannel على dataManager بالمعامل channelData. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:484]

```
485:             Log.d(TAG, "Saved channel selection: ${channel.displayName}")
```
> يُسجَّل سطر تصحيح (Log.d) بالوسم TAG ونصّه "Saved channel selection: " متبوعاً بقيمة channel.displayName. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:485]

```
486:         } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وفتح كتلة التقاط (catch) للاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:486]

```
487:             Log.e(TAG, "Failed to save channel selection: ${e.message}")
```
> يُسجَّل سطر خطأ (Log.e) بالوسم TAG ونصّه "Failed to save channel selection: " متبوعاً بقيمة e.message. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:487]

```
488:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:488]

```
489:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:489]

```
490:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:490]

```
491:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:491]

```
492:      * Load persisted channel selection from storage
```
> تعليق: تحميل اختيار القناة المحفوظ من التخزين. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:492]

```
493:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:493]

```
494:     private fun loadPersistedChannelSelection() {
```
> تُعرَّف دالة خاصة (private) باسم loadPersistedChannelSelection بلا معاملات. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:494]

```
495:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:495]

```
496:             val channelData = dataManager?.loadLastGeohashChannel()
```
> يُعرَّف الثابت (channelData) ويُسنَد إليه ناتج الاستدعاء الآمن loadLastGeohashChannel على dataManager. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:496]

```
497:             if (!channelData.isNullOrBlank()) {
```
> إذا لم يكن channelData فارغاً أو خالياً من المحتوى (نفي isNullOrBlank) تُفتَح كتلة الشرط. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:497]

```
498:                 val persisted = gson.fromJson(channelData, PersistedChannel::class.java)
```
> يُعرَّف الثابت (persisted) ويُسنَد إليه ناتج gson.fromJson على channelData بصنف PersistedChannel::class.java. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:498]

```
499:                 val channel = persisted?.toChannel()
```
> يُعرَّف الثابت (channel) ويُسنَد إليه ناتج الاستدعاء الآمن toChannel على persisted. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:499]

```
500:                 if (channel != null) {
```
> إذا كان channel غير معدوم (لا يساوي null) تُفتَح كتلة الشرط. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:500]

```
501:                     _selectedChannel.value = channel
```
> تُسنَد قيمة channel إلى الخاصية value للحقل _selectedChannel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:501]

```
502:                     Log.d(TAG, "Restored persisted channel: ${channel.displayName}")
```
> يُسجَّل سطر تصحيح (Log.d) بالوسم TAG ونصّه "Restored persisted channel: " متبوعاً بقيمة channel.displayName. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:502]

```
503:                 } else {
```
> إغلاق كتلة الشرط وفتح كتلة وإلّا (else). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:503]

```
504:                     Log.d(TAG, "Could not restore persisted channel, defaulting to Mesh")
```
> يُسجَّل سطر تصحيح (Log.d) بالوسم TAG ونصّه "Could not restore persisted channel, defaulting to Mesh". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:504]

```
505:                     _selectedChannel.value = ChannelID.Mesh
```
> تُسنَد القيمة ChannelID.Mesh إلى الخاصية value للحقل _selectedChannel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:505]

```
506:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:506]

```
507:             } else {
```
> إغلاق كتلة الشرط وفتح كتلة وإلّا (else). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:507]

```
508:                 Log.d(TAG, "No persisted channel found, defaulting to Mesh")
```
> يُسجَّل سطر تصحيح (Log.d) بالوسم TAG ونصّه "No persisted channel found, defaulting to Mesh". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:508]

```
509:                 _selectedChannel.value = ChannelID.Mesh
```
> تُسنَد القيمة ChannelID.Mesh إلى الخاصية value للحقل _selectedChannel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:509]

```
510:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:510]

```
511:         } catch (e: JsonSyntaxException) {
```
> إغلاق كتلة المحاولة وفتح كتلة التقاط (catch) لاستثناء صياغة جيسون (JsonSyntaxException) باسم e. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:511]

```
512:             Log.e(TAG, "Failed to parse persisted channel data: ${e.message}")
```
> يُسجَّل سطر خطأ (Log.e) بالوسم TAG ونصّه "Failed to parse persisted channel data: " متبوعاً بقيمة e.message. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:512]

```
513:             _selectedChannel.value = ChannelID.Mesh
```
> تُسنَد القيمة ChannelID.Mesh إلى الخاصية value للحقل _selectedChannel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:513]

```
514:         } catch (e: Exception) {
```
> إغلاق كتلة الالتقاط السابقة وفتح كتلة التقاط (catch) للاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:514]

```
515:             Log.e(TAG, "Failed to load persisted channel: ${e.message}")
```
> يُسجَّل سطر خطأ (Log.e) بالوسم TAG ونصّه "Failed to load persisted channel: " متبوعاً بقيمة e.message. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:515]

```
516:             _selectedChannel.value = ChannelID.Mesh
```
> تُسنَد القيمة ChannelID.Mesh إلى الخاصية value للحقل _selectedChannel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:516]

```
517:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:517]

```
518:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:518]

```
519: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:519]

```
520:     data class PersistedChannel(
```
> يُعرَّف صنف بيانات (data class) باسم PersistedChannel (بداية الوسائط). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:520]

```
521:         val mesh: Boolean,
```
> يُعرَّف الحقل (mesh) من نوع Boolean. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:521]

```
522:         val level: String? = null,
```
> يُعرَّف الحقل (level) من نوع String? (قابل للعدم) بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:522]

```
523:         val geohash: String? = null
```
> يُعرَّف الحقل (geohash) من نوع String? (قابل للعدم) بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:523]

```
524:     ) {
```
> إغلاق وسائط الصنف وفتح جسمه. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:524]

```
525:         fun toChannel(): ChannelID? {
```
> تُعرَّف دالة باسم toChannel بلا معاملات تُعيد ChannelID? (قابلاً للعدم). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:525]

```
526:             return if (mesh) {
```
> تُعيد الدالة ناتج تعبير شرطي: إذا كان mesh محقّقاً (بداية الفرع). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:526]

```
527:                 ChannelID.Mesh
```
> قيمة الفرع: ChannelID.Mesh. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:527]

```
528:             } else {
```
> إغلاق فرع الشرط وفتح فرع وإلّا (else). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:528]

```
529:                 val levelName = level ?: return null
```
> يُعرَّف الثابت (levelName) ويُسنَد إليه level، وإن كان معدوماً يُرجَع null بمعامل إلفيس (?:). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:529]

```
530:                 val gh = geohash ?: return null
```
> يُعرَّف الثابت (gh) ويُسنَد إليه geohash، وإن كان معدوماً يُرجَع null بمعامل إلفيس (?:). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:530]

```
531:                 ChannelID.Location.fromPersisted(levelName, gh)
```
> قيمة الفرع: ناتج استدعاء fromPersisted على ChannelID.Location بالمعاملين levelName وgh. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:531]

```
532:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:532]

```
533:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:533]

```
534:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:534]

```
535: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:535]

```
536:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:536]

```
537:      * Clear persisted channel selection (useful for testing or reset)
```
> تعليق: مسح اختيار القناة المحفوظ (مفيد للاختبار أو إعادة الضبط). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:537]

```
538:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:538]

```
539:     fun clearPersistedChannel() {
```
> تُعرَّف دالة باسم clearPersistedChannel بلا معاملات. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:539]

```
540:         dataManager?.clearLastGeohashChannel()
```
> يُستدعى بأمان clearLastGeohashChannel على dataManager. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:540]

```
541:         _selectedChannel.value = ChannelID.Mesh
```
> تُسنَد القيمة ChannelID.Mesh إلى الخاصية value للحقل _selectedChannel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:541]

```
542:         _teleported.value = false
```
> تُسنَد القيمة false إلى الخاصية value للحقل _teleported. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:542]

```
543:         Log.d(TAG, "Cleared persisted channel selection")
```
> يُسجَّل سطر تصحيح (Log.d) بالوسم TAG ونصّه "Cleared persisted channel selection". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:543]

```
544:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:544]

```
545: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:545]

```
546:     // MARK: - Location Services State Persistence
```
> تعليق: علامة: حفظ حالة خدمات الموقع (Location Services State Persistence). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:546]

```
547: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:547]

```
548:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:548]

```
549:      * Save location services enabled state to persistent storage
```
> تعليق: حفظ حالة تفعيل خدمات الموقع في التخزين الدائم. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:549]

```
550:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:550]

```
551:     private fun saveLocationServicesState(enabled: Boolean) {
```
> تُعرَّف دالة خاصة (private) باسم saveLocationServicesState تأخذ معاملاً enabled من نوع Boolean. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:551]

```
552:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:552]

```
553:             dataManager?.saveLocationServicesEnabled(enabled)
```
> يُستدعى بأمان saveLocationServicesEnabled على dataManager بالمعامل enabled. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:553]

```
554:             Log.d(TAG, "Saved location services state: $enabled")
```
> يُسجَّل سطر تصحيح (Log.d) بالوسم TAG ونصّه "Saved location services state: " متبوعاً بقيمة enabled. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:554]

```
555:         } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وفتح كتلة التقاط (catch) للاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:555]

```
556:             Log.e(TAG, "Failed to save location services state: ${e.message}")
```
> يُسجَّل سطر خطأ (Log.e) بالوسم TAG ونصّه "Failed to save location services state: " متبوعاً بقيمة e.message. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:556]

```
557:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:557]

```
558:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:558]

```
559: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:559]

```
560:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:560]

```
561:      * Load persisted location services state from storage
```
> تعليق: تحميل حالة خدمات الموقع المحفوظة من التخزين. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:561]

```
562:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:562]

```
563:     private fun loadLocationServicesState() {
```
> تُعرَّف دالة خاصة (private) باسم loadLocationServicesState بلا معاملات. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:563]

```
564:         try {
```
> بداية كتلة محاولة (try). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:564]

```
565:             val enabled = dataManager?.isLocationServicesEnabled() ?: false
```
> يُعرَّف الثابت (enabled) ويُسنَد إليه ناتج الاستدعاء الآمن isLocationServicesEnabled على dataManager، وإن كان معدوماً فالقيمة false بمعامل إلفيس (?:). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:565]

```
566:             _locationServicesEnabled.value = enabled
```
> تُسنَد قيمة enabled إلى الخاصية value للحقل _locationServicesEnabled. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:566]

```
567:             Log.d(TAG, "Loaded location services state: $enabled")
```
> يُسجَّل سطر تصحيح (Log.d) بالوسم TAG ونصّه "Loaded location services state: " متبوعاً بقيمة enabled. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:567]

```
568:         } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وفتح كتلة التقاط (catch) للاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:568]

```
569:             Log.e(TAG, "Failed to load location services state: ${e.message}")
```
> يُسجَّل سطر خطأ (Log.e) بالوسم TAG ونصّه "Failed to load location services state: " متبوعاً بقيمة e.message. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:569]

```
570:             _locationServicesEnabled.value = false
```
> تُسنَد القيمة false إلى الخاصية value للحقل _locationServicesEnabled. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:570]

```
571:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:571]

```
572:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:572]

```
573: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:573]

```
574:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:574]

```
575:      * Cleanup resources
```
> تعليق: تنظيف الموارد. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:575]

```
576:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:576]

```
577:     fun cleanup() {
```
> تُعرَّف دالة باسم cleanup بلا معاملات. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:577]

```
578:         Log.d(TAG, "Cleaning up LocationChannelManager")
```
> يُسجَّل سطر تصحيح (Log.d) بالوسم TAG ونصّه "Cleaning up LocationChannelManager". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:578]

```
579:         endLiveRefresh()
```
> تُستدعى الدالة endLiveRefresh بلا معاملات. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:579]

```
580:         locationProvider.cancel()
```
> تُستدعى الدالة cancel على locationProvider. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:580]

```
581:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:581]

```
582:         geocodingJob?.cancel()
```
> يُستدعى بأمان cancel على geocodingJob. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:582]

```
583:         geocodingJob = null
```
> تُسنَد القيمة null إلى geocodingJob. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:583]

```
584:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:584]

```
585:         // Unregister receiver
```
> تعليق: إلغاء تسجيل المستقبِل. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:585]

```
586:         try { context.unregisterReceiver(locationStateReceiver) } catch (_: Exception) {}
```
> داخل كتلة محاولة يُستدعى unregisterReceiver على context بالمعامل locationStateReceiver، وكتلة التقاط (catch) للاستثناء (Exception) بلا اسم وبجسم فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:586]

```
587:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:587]

```
588: }
```
> إغلاق نطاق (نهاية الصنف). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:588]
