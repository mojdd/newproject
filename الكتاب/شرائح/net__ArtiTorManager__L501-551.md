# شريحة — app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt (الأسطر 501–551)

```
501:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:501]

```
502:                _statusFlow.update {
```
> يستدعي دالّة التحديث (update) على تدفّق الحالة (_statusFlow) ويفتح كتلة لامبدا (lambda). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:502]

```
503:                    it.copy(
```
> ينشئ نسخة (copy) من العنصر الحالي (it) ويفتح قائمة المعطيات. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:503]

```
504:                        state = TorState.STOPPING,
```
> يضبط الحقل state على القيمة TorState.STOPPING (حالة الإيقاف الجاري). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:504]

```
505:                        running = false
```
> يضبط الحقل running (يعمل) على القيمة false. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:505]

```
506:                    )
```
> إغلاق نطاق (إغلاق قائمة معطيات copy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:506]

```
507:                }
```
> إغلاق نطاق (إغلاق كتلة لامبدا update). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:507]

```
508:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:508]

```
509:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:509]

```
510:            s.contains("AMEx: state changed to Stopped", ignoreCase = true) -> {
```
> فرع شرطي (when) يتحقّق إذا كان النصّ s يحتوي (contains) السلسلة "AMEx: state changed to Stopped" مع تجاهل حالة الأحرف (ignoreCase = true) ثم يفتح كتلة الفرع. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:510]

```
511:                if (currentLifecycle != LifecycleState.STOPPING && currentLifecycle != LifecycleState.STOPPED) {
```
> جملة شرطية (if) تتحقّق إذا كانت دورة الحياة الحالية (currentLifecycle) لا تساوي LifecycleState.STOPPING وكذلك لا تساوي LifecycleState.STOPPED ثم تفتح الكتلة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:511]

```
512:                    Log.w(
```
> يستدعي دالّة التحذير (Log.w) ويفتح قائمة المعطيات. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:512]

```
513:                        TAG,
```
> يمرّر المعطى TAG (الوسم) كأوّل معطى. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:513]

```
514:                        "Ignoring stale 'Stopped' log (lifecycle: $currentLifecycle, preventing state corruption)"
```
> يمرّر سلسلة نصّية بقالب (template) تساوي "Ignoring stale 'Stopped' log (lifecycle: $currentLifecycle, preventing state corruption)" مع إدراج قيمة currentLifecycle. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:514]

```
515:                    )
```
> إغلاق نطاق (إغلاق قائمة معطيات Log.w). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:515]

```
516:                    return
```
> يعيد (return) من الدالّة دون قيمة. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:516]

```
517:                }
```
> إغلاق نطاق (إغلاق كتلة if). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:517]

```
518:                _statusFlow.update {
```
> يستدعي دالّة التحديث (update) على تدفّق الحالة (_statusFlow) ويفتح كتلة لامبدا. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:518]

```
519:                    it.copy(
```
> ينشئ نسخة (copy) من العنصر الحالي (it) ويفتح قائمة المعطيات. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:519]

```
520:                        state = TorState.OFF,
```
> يضبط الحقل state على القيمة TorState.OFF (حالة الإيقاف). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:520]

```
521:                        running = false,
```
> يضبط الحقل running (يعمل) على القيمة false. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:521]

```
522:                        bootstrapPercent = 0
```
> يضبط الحقل bootstrapPercent (نسبة الإقلاع) على القيمة 0. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:522]

```
523:                    )
```
> إغلاق نطاق (إغلاق قائمة معطيات copy). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:523]

```
524:                }
```
> إغلاق نطاق (إغلاق كتلة لامبدا update). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:524]

```
525:                completeWaitersIf(TorState.OFF)
```
> يستدعي الدالّة completeWaitersIf (أكمِل المنتظِرين إن) ويمرّر المعطى TorState.OFF. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:525]

```
526:            }
```
> إغلاق نطاق (إغلاق كتلة الفرع). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:526]

```
527:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:527]

```
528:            s.contains("Another process has the lock on our state files", ignoreCase = true) -> {
```
> فرع شرطي (when) يتحقّق إذا كان النصّ s يحتوي (contains) السلسلة "Another process has the lock on our state files" مع تجاهل حالة الأحرف (ignoreCase = true) ثم يفتح كتلة الفرع. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:528]

```
529:                _statusFlow.update { it.copy(state = TorState.ERROR) }
```
> يستدعي دالّة التحديث (update) على تدفّق الحالة (_statusFlow) بكتلة لامبدا تنشئ نسخة (copy) تضبط الحقل state على القيمة TorState.ERROR (حالة الخطأ). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:529]

```
530:            }
```
> إغلاق نطاق (إغلاق كتلة الفرع). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:530]

```
531:        }
```
> إغلاق نطاق (إغلاق كتلة when). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:531]

```
532:    }
```
> إغلاق نطاق (إغلاق الدالّة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:532]

```
533:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:533]

```
534:    private fun completeWaitersIf(state: TorState) {
```
> يعرّف دالّة خاصّة (private fun) باسم completeWaitersIf (أكمِل المنتظِرين إن) تأخذ معطى state من النوع TorState ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:534]

```
535:        stateChangeDeferred.getAndSet(null)?.let { def ->
```
> يستدعي getAndSet بالقيمة null على stateChangeDeferred (المؤجَّل لتغيُّر الحالة) فيعيد القيمة السابقة ويضبط الجديدة على null، ثم على النتيجة غير العدمية يطبّق let بكتلة لامبدا معطاها def. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:535]

```
536:            def.complete(state)
```
> يستدعي complete (أكمِل) على def ويمرّر المعطى state. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:536]

```
537:        }
```
> إغلاق نطاق (إغلاق كتلة let). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:537]

```
538:    }
```
> إغلاق نطاق (إغلاق الدالّة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:538]

```
539:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:539]

```
540:    private suspend fun waitForStateTransition(target: TorState, timeoutMs: Long): TorState? {
```
> يعرّف دالّة خاصّة معلّقة (private suspend fun) باسم waitForStateTransition (انتظِر انتقال الحالة) تأخذ معطى target من النوع TorState ومعطى timeoutMs من النوع Long وتعيد TorState? (قد تكون عدمية) ويفتح جسمها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:540]

```
541:        val def = CompletableDeferred<TorState>()
```
> يعرّف متغيّراً ثابتاً (val) باسم def ويسنده إلى كائن CompletableDeferred من النوع TorState مُنشَأ جديداً. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:541]

```
542:        stateChangeDeferred.getAndSet(def)?.cancel()
```
> يستدعي getAndSet بالقيمة def على stateChangeDeferred فيعيد القيمة السابقة ويضبط الجديدة على def، ثم على النتيجة غير العدمية يستدعي cancel (ألغِ). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:542]

```
543:        return withTimeoutOrNull(timeoutMs) {
```
> يعيد (return) نتيجة استدعاء withTimeoutOrNull بالمعطى timeoutMs مع كتلة لامبدا يفتحها. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:543]

```
544:            val cur = _statusFlow.value.state
```
> يعرّف متغيّراً ثابتاً (val) باسم cur ويسنده إلى الحقل state من القيمة (value) الحالية لتدفّق الحالة (_statusFlow). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:544]

```
545:            if (cur == target) return@withTimeoutOrNull cur
```
> جملة شرطية (if): إذا كان cur يساوي target فإنّه يعيد cur من كتلة withTimeoutOrNull. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:545]

```
546:            def.await()
```
> يستدعي await (انتظِر) على def. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:546]

```
547:        }
```
> إغلاق نطاق (إغلاق كتلة withTimeoutOrNull). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:547]

```
548:    }
```
> إغلاق نطاق (إغلاق الدالّة). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:548]

```
549:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:549]

```
550:    fun isTorAvailable(): Boolean = true
```
> يعرّف دالّة (fun) باسم isTorAvailable (هل تور متاح) تعيد Boolean وقيمتها المعادة هي true. [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:550]

```
551:}
```
> إغلاق نطاق (إغلاق الصنف). [app/src/main/java/com/bitchat/android/net/ArtiTorManager.kt:551]
