# شريحة — app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt (الأسطر 401–469)

```
401:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:401]

```
402:         Log.d(TAG, "📥 Added note: ${note.displayName} - ${note.content.take(50)}")
```
> يستدعي دالة التسجيل التشخيصي `Log.d` مع الوسم (TAG) ونصٍّ يكتب «أُضيفت ملاحظة» متبوعاً باسم العرض (displayName) للملاحظة (note) وأول خمسين حرفاً من محتواها (content) المأخوذة بـ `take(50)`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:402]

```
403:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:403]

```
404:         // Trim if exceeds max
```
> تعليق: قصّ إن تجاوز الحد الأقصى. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:404]

```
405:         if (noteIDs.size > MAX_NOTES_IN_MEMORY) {
```
> يبدأ شرطاً (if) يتحقق إن كان حجم مجموعة معرّفات الملاحظات (noteIDs.size) أكبر من الحد الأقصى للملاحظات في الذاكرة (MAX_NOTES_IN_MEMORY). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:405]

```
406:             trimOldestNotes()
```
> يستدعي دالة قصّ أقدم الملاحظات (trimOldestNotes). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:406]

```
407:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:407]

```
408:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:408]

```
409:         // Update state
```
> تعليق: حدِّث الحالة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:409]

```
410:         if (!_initialLoadComplete.value!!) {
```
> يبدأ شرطاً (if) يتحقق إن كانت قيمة علم اكتمال التحميل المبدئي (_initialLoadComplete.value) غير صحيحة، مع استعمال مؤكّد عدم النُّلّية `!!`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:410]

```
411:             _initialLoadComplete.value = true
```
> يضبط قيمة علم اكتمال التحميل المبدئي (_initialLoadComplete.value) إلى `true`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:411]

```
412:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:412]

```
413:         _state.value = State.READY
```
> يضبط قيمة الحالة (_state.value) إلى `State.READY` (جاهز). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:413]

```
414:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:414]

```
415:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:415]

```
416:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:416]

```
417:      * Trim oldest notes to stay within memory limit
```
> تعليق: قصّ أقدم الملاحظات للبقاء ضمن حد الذاكرة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:417]

```
418:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:418]

```
419:     private fun trimOldestNotes() {
```
> يعرّف دالةً خاصةً (private) باسم قصّ أقدم الملاحظات (trimOldestNotes) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:419]

```
420:         val currentNotes = _notes.value ?: return
```
> يعرّف متغيراً ثابتاً (val) باسم الملاحظات الحالية (currentNotes) يساوي قيمة الملاحظات (_notes.value)، وإن كانت نُلّية يعود من الدالة بـ `return`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:420]

```
421:         if (currentNotes.size <= MAX_NOTES_IN_MEMORY) return
```
> شرط (if): إن كان حجم الملاحظات الحالية (currentNotes.size) أقل من أو يساوي الحد الأقصى للملاحظات في الذاكرة (MAX_NOTES_IN_MEMORY) يعود من الدالة بـ `return`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:421]

```
422:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:422]

```
423:         val trimmed = currentNotes.sortedByDescending { it.createdAt }.take(MAX_NOTES_IN_MEMORY)
```
> يعرّف متغيراً ثابتاً (val) باسم المقصوصة (trimmed) يساوي الملاحظات الحالية مرتّبةً تنازلياً `sortedByDescending` بحسب وقت الإنشاء (createdAt) ثم أخذ عددٍ منها يساوي الحد الأقصى للملاحظات في الذاكرة (MAX_NOTES_IN_MEMORY) بـ `take`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:423]

```
424:         _notes.value = trimmed
```
> يضبط قيمة الملاحظات (_notes.value) إلى المقصوصة (trimmed). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:424]

```
425:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:425]

```
426:         // Update note IDs set
```
> تعليق: حدِّث مجموعة معرّفات الملاحظات. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:426]

```
427:         noteIDs.clear()
```
> يستدعي `clear` على مجموعة معرّفات الملاحظات (noteIDs) لتفريغها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:427]

```
428:         noteIDs.addAll(trimmed.map { it.id })
```
> يستدعي `addAll` على مجموعة معرّفات الملاحظات (noteIDs) لإضافة معرّفات (id) جميع عناصر المقصوصة (trimmed) المحوّلة بـ `map`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:428]

```
429:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:429]

```
430:         Log.d(TAG, "Trimmed notes to $MAX_NOTES_IN_MEMORY (removed ${currentNotes.size - trimmed.size})")
```
> يستدعي دالة التسجيل التشخيصي `Log.d` مع الوسم (TAG) ونصٍّ يكتب «قُصّت الملاحظات إلى» قيمة الحد الأقصى للملاحظات في الذاكرة (MAX_NOTES_IN_MEMORY) ثم «أُزيل» عدداً يساوي حجم الملاحظات الحالية (currentNotes.size) ناقص حجم المقصوصة (trimmed.size). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:430]

```
431:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:431]

```
432:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:432]

```
433:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:433]

```
434:      * Clear error message - matches iOS clearError()
```
> تعليق: مسح رسالة الخطأ - يطابق دالة `clearError()` في iOS. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:434]

```
435:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:435]

```
436:     fun clearError() {
```
> يعرّف دالةً عامةً باسم مسح الخطأ (clearError) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:436]

```
437:         _errorMessage.value = null
```
> يضبط قيمة رسالة الخطأ (_errorMessage.value) إلى `null` (نُلّ). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:437]

```
438:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:438]

```
439:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:439]

```
440:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:440]

```
441:      * Cancel subscription and clear state
```
> تعليق: إلغاء الاشتراك ومسح الحالة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:441]

```
442:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:442]

```
443:     fun cancel() {
```
> يعرّف دالةً عامةً باسم الإلغاء (cancel) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:443]

```
444:         if (subscriptionIDs.isNotEmpty()) {
```
> يبدأ شرطاً (if) يتحقق بـ `isNotEmpty` أن مجموعة معرّفات الاشتراكات (subscriptionIDs) ليست فارغة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:444]

```
445:             subscriptionIDs.values.forEach { subId ->
```
> يكرّر بـ `forEach` على قيم (values) مجموعة معرّفات الاشتراكات (subscriptionIDs)، كل عنصرٍ باسم معرّف الاشتراك (subId). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:445]

```
446:                 try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:446]

```
447:                     Log.d(TAG, "🚫 Canceling subscription: $subId")
```
> يستدعي دالة التسجيل التشخيصي `Log.d` مع الوسم (TAG) ونصٍّ يكتب «إلغاء الاشتراك» متبوعاً بمعرّف الاشتراك (subId). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:447]

```
448:                     unsubscribeFunc?.invoke(subId)
```
> يستدعي بأمان `?.invoke` دالة إلغاء الاشتراك (unsubscribeFunc) إن لم تكن نُلّية، ممرّراً معرّف الاشتراك (subId). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:448]

```
449:                 } catch (_: Exception) { }
```
> يلتقط استثناءً (Exception) باسمٍ مهمَل `_` وكتلة المعالجة فارغة. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:449]

```
450:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:450]

```
451:             subscriptionIDs.clear()
```
> يستدعي `clear` على مجموعة معرّفات الاشتراكات (subscriptionIDs) لتفريغها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:451]

```
452:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:452]

```
453:         subscribedGeohashes = emptySet()
```
> يسند إلى المتغير الجِيوهاشات المشترَك بها (subscribedGeohashes) مجموعةً فارغةً `emptySet()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:453]

```
454:         _state.value = State.IDLE
```
> يضبط قيمة الحالة (_state.value) إلى `State.IDLE` (خامل). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:454]

```
455:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:455]

```
456:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:456]

```
457:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:457]

```
458:      * Cleanup resources
```
> تعليق: تنظيف الموارد. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:458]

```
459:      */
```
> تعليق: نهاية كتلة توثيق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:459]

```
460:     fun cleanup() {
```
> يعرّف دالةً عامةً باسم التنظيف (cleanup) بلا وسائط. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:460]

```
461:         cancel()
```
> يستدعي دالة الإلغاء (cancel). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:461]

```
462:         scope.cancel()
```
> يستدعي `cancel` على النطاق (scope). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:462]

```
463:         _notes.value = emptyList()
```
> يضبط قيمة الملاحظات (_notes.value) إلى قائمةٍ فارغةٍ `emptyList()`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:463]

```
464:         noteIDs.clear()
```
> يستدعي `clear` على مجموعة معرّفات الملاحظات (noteIDs) لتفريغها. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:464]

```
465:         _geohash.value = null
```
> يضبط قيمة الجِيوهاش (_geohash.value) إلى `null` (نُلّ). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:465]

```
466:         _initialLoadComplete.value = false
```
> يضبط قيمة علم اكتمال التحميل المبدئي (_initialLoadComplete.value) إلى `false`. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:466]

```
467:         _errorMessage.value = null
```
> يضبط قيمة رسالة الخطأ (_errorMessage.value) إلى `null` (نُلّ). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:467]

```
468:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:468]

```
469: }
```
> إغلاق نطاق (نهاية الصنف). [app/src/main/java/com/bitchat/android/nostr/LocationNotesManager.kt:469]
