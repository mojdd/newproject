# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt (الأسطر 601–800)

```
601:      */
```
> تعليق: نهاية كتلة تعليق توثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:601]

```
602:     private fun stopSubscriptionValidation() {
```
> يُعرّف دالة خاصة (private) باسم «إيقاف التحقق من الاشتراك» (stopSubscriptionValidation) بلا وسائط ولا قيمة إرجاع. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:602]

```
603:         subscriptionValidationJob?.cancel()
```
> يستدعي دالة «إلغاء» (cancel) على «مهمة التحقق من الاشتراك» (subscriptionValidationJob) إن لم تكن قيمتها فارغة (null). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:603]

```
604:         subscriptionValidationJob = null
```
> يضبط «مهمة التحقق من الاشتراك» (subscriptionValidationJob) إلى القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:604]

```
605:         Log.v(TAG, "⏹️ Stopped subscription validation")
```
> يستدعي تسجيلاً مستوى تفصيلي (Log.v) بالوسم TAG والنص «⏹️ Stopped subscription validation». [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:605]

```
606:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:606]

```
607:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:607]

```
608:     // MARK: - Private Methods
```
> تعليق: علامة قسم «الدوال الخاصة». [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:608]

```
609:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:609]

```
610:     private suspend fun connectToRelay(urlString: String) {
```
> يُعرّف دالة خاصة معلّقة (suspend) باسم «الاتصال بالمُرحِّل» (connectToRelay) تأخذ وسيطاً نصياً باسم «سلسلة العنوان» (urlString) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:610]

```
611:         // Skip if we already have a connection
```
> تعليق: تخطَّ إن كان لدينا اتصال بالفعل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:611]

```
612:         if (connections.containsKey(urlString)) {
```
> يبدأ شرطاً إذا كانت مجموعة «الاتصالات» (connections) تحتوي على مفتاح يساوي «سلسلة العنوان» (urlString). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:612]

```
613:             return
```
> يُعيد من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:613]

```
614:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:614]

```
615:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:615]

```
616:         Log.v(TAG, "Attempting to connect to Nostr relay: $urlString")
```
> يستدعي تسجيلاً مستوى تفصيلي (Log.v) بالوسم TAG والنص «Attempting to connect to Nostr relay:» متبوعاً بقيمة «سلسلة العنوان» (urlString). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:616]

```
617:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:617]

```
618:         try {
```
> يبدأ كتلة «محاولة» (try). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:618]

```
619:             val request = Request.Builder()
```
> يُعرّف متغيّراً ثابتاً (val) باسم «الطلب» (request) ويبدأ بناءه عبر «باني الطلب» (Request.Builder). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:619]

```
620:                 .url(urlString)
```
> يستدعي دالة «العنوان» (url) على الباني بتمرير «سلسلة العنوان» (urlString). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:620]

```
621:                 .build()
```
> يستدعي دالة «البناء» (build) لإنهاء بناء كائن الطلب. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:621]

```
622:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:622]

```
623:             val webSocket = httpClient.newWebSocket(request, RelayWebSocketListener(urlString))
```
> يُعرّف متغيّراً ثابتاً (val) باسم «مقبس الويب» (webSocket) قيمته نتيجة استدعاء «مقبس ويب جديد» (newWebSocket) على «عميل http» (httpClient) بتمرير «الطلب» (request) وكائن «مستمع مقبس ويب المُرحِّل» (RelayWebSocketListener) المُنشأ بـ «سلسلة العنوان» (urlString). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:623]

```
624:             connections[urlString] = webSocket
```
> يُسند «مقبس الويب» (webSocket) إلى مجموعة «الاتصالات» (connections) عند المفتاح «سلسلة العنوان» (urlString). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:624]

```
625:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:625]

```
626:         } catch (e: Exception) {
```
> يُغلق كتلة المحاولة ويبدأ كتلة «التقاط» (catch) لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:626]

```
627:             Log.e(TAG, "❌ Failed to create WebSocket connection to $urlString: ${e.message}")
```
> يستدعي تسجيلاً مستوى خطأ (Log.e) بالوسم TAG والنص «❌ Failed to create WebSocket connection to» متبوعاً بقيمة «سلسلة العنوان» (urlString) ثم رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:627]

```
628:             handleDisconnection(urlString, e)
```
> يستدعي دالة «معالجة قطع الاتصال» (handleDisconnection) بتمرير «سلسلة العنوان» (urlString) والاستثناء e. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:628]

```
629:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:629]

```
630:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:630]

```
631:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:631]

```
632:     private fun sendToRelay(event: NostrEvent, webSocket: WebSocket, relayUrl: String) {
```
> يُعرّف دالة خاصة باسم «الإرسال إلى المُرحِّل» (sendToRelay) تأخذ «الحدث» (event) من نوع NostrEvent و«مقبس الويب» (webSocket) من نوع WebSocket و«عنوان المُرحِّل» (relayUrl) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:632]

```
633:         try {
```
> يبدأ كتلة «محاولة» (try). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:633]

```
634:             val request = NostrRequest.Event(event)
```
> يُعرّف متغيّراً ثابتاً (val) باسم «الطلب» (request) قيمته كائن «طلب نوستر حدث» (NostrRequest.Event) المُنشأ بـ «الحدث» (event). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:634]

```
635:             val message = gson.toJson(request, NostrRequest::class.java)
```
> يُعرّف متغيّراً ثابتاً (val) باسم «الرسالة» (message) قيمته ناتج تحويل «الطلب» (request) إلى JSON عبر gson باستخدام صنف NostrRequest. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:635]

```
636:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:636]

```
637:             Log.v(TAG, "📤 Sending Nostr event (kind: ${event.kind}) to relay: $relayUrl")
```
> يستدعي تسجيلاً مستوى تفصيلي (Log.v) بالوسم TAG والنص «📤 Sending Nostr event (kind:» متبوعاً بنوع الحدث (event.kind) ثم «to relay:» وقيمة «عنوان المُرحِّل» (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:637]

```
638:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:638]

```
639:             val success = webSocket.send(message)
```
> يُعرّف متغيّراً ثابتاً (val) باسم «النجاح» (success) قيمته ناتج استدعاء دالة «إرسال» (send) على «مقبس الويب» (webSocket) بتمرير «الرسالة» (message). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:639]

```
640:             if (success) {
```
> يبدأ شرطاً إذا كانت قيمة «النجاح» (success) صحيحة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:640]

```
641:                 // Update relay stats
```
> تعليق: حدِّث إحصاءات المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:641]

```
642:                 val relay = relaysList.find { it.url == relayUrl }
```
> يُعرّف متغيّراً ثابتاً (val) باسم «المُرحِّل» (relay) قيمته أول عنصر في «قائمة المُرحِّلات» (relaysList) عنوانه (url) يساوي «عنوان المُرحِّل» (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:642]

```
643:                 relay?.messagesSent = (relay?.messagesSent ?: 0) + 1
```
> يضبط حقل «الرسائل المُرسَلة» (messagesSent) على «المُرحِّل» (relay) إن لم يكن فارغاً إلى قيمته الحالية (أو 0 إن كانت فارغة) مضافاً إليها واحد. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:643]

```
644:                 updateRelaysList()
```
> يستدعي دالة «تحديث قائمة المُرحِّلات» (updateRelaysList). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:644]

```
645:             } else {
```
> يُغلق فرع if ويبدأ فرع «وإلا» (else). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:645]

```
646:                 Log.e(TAG, "❌ Failed to send event to $relayUrl: WebSocket send failed")
```
> يستدعي تسجيلاً مستوى خطأ (Log.e) بالوسم TAG والنص «❌ Failed to send event to» متبوعاً بقيمة «عنوان المُرحِّل» (relayUrl) ثم «WebSocket send failed». [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:646]

```
647:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:647]

```
648:         } catch (e: Exception) {
```
> يُغلق كتلة المحاولة ويبدأ كتلة «التقاط» (catch) لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:648]

```
649:             Log.e(TAG, "❌ Failed to send event to $relayUrl: ${e.message}")
```
> يستدعي تسجيلاً مستوى خطأ (Log.e) بالوسم TAG والنص «❌ Failed to send event to» متبوعاً بقيمة «عنوان المُرحِّل» (relayUrl) ثم رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:649]

```
650:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:650]

```
651:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:651]

```
652:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:652]

```
653:     private fun handleMessage(message: String, relayUrl: String) {
```
> يُعرّف دالة خاصة باسم «معالجة الرسالة» (handleMessage) تأخذ «الرسالة» (message) من نوع String و«عنوان المُرحِّل» (relayUrl) من نوع String. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:653]

```
654:         try {
```
> يبدأ كتلة «محاولة» (try). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:654]

```
655:             val jsonElement = JsonParser.parseString(message)
```
> يُعرّف متغيّراً ثابتاً (val) باسم «عنصر JSON» (jsonElement) قيمته ناتج تحليل «الرسالة» (message) عبر «محلّل JSON» (JsonParser.parseString). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:655]

```
656:             if (!jsonElement.isJsonArray) {
```
> يبدأ شرطاً إذا لم يكن «عنصر JSON» (jsonElement) مصفوفة JSON (isJsonArray). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:656]

```
657:                 Log.w(TAG, "Received non-array message from $relayUrl")
```
> يستدعي تسجيلاً مستوى تحذير (Log.w) بالوسم TAG والنص «Received non-array message from» متبوعاً بقيمة «عنوان المُرحِّل» (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:657]

```
658:                 return
```
> يُعيد من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:658]

```
659:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:659]

```
660:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:660]

```
661:             val response = NostrResponse.fromJsonArray(jsonElement.asJsonArray)
```
> يُعرّف متغيّراً ثابتاً (val) باسم «الاستجابة» (response) قيمته ناتج «من مصفوفة JSON» (fromJsonArray) على «استجابة نوستر» (NostrResponse) بتمرير «عنصر JSON» (jsonElement) كمصفوفة (asJsonArray). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:661]

```
662:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:662]

```
663:             when (response) {
```
> يبدأ تعبير «عندما» (when) يفرّع على قيمة «الاستجابة» (response). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:663]

```
664:                 is NostrResponse.Event -> {
```
> فرع: عندما تكون «الاستجابة» (response) من نوع «حدث استجابة نوستر» (NostrResponse.Event). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:664]

```
665:                     // Update relay stats
```
> تعليق: حدِّث إحصاءات المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:665]

```
666:                     val relay = relaysList.find { it.url == relayUrl }
```
> يُعرّف متغيّراً ثابتاً (val) باسم «المُرحِّل» (relay) قيمته أول عنصر في «قائمة المُرحِّلات» (relaysList) عنوانه (url) يساوي «عنوان المُرحِّل» (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:666]

```
667:                     relay?.messagesReceived = (relay?.messagesReceived ?: 0) + 1
```
> يضبط حقل «الرسائل المُستقبَلة» (messagesReceived) على «المُرحِّل» (relay) إن لم يكن فارغاً إلى قيمته الحالية (أو 0 إن كانت فارغة) مضافاً إليها واحد. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:667]

```
668:                     updateRelaysList()
```
> يستدعي دالة «تحديث قائمة المُرحِّلات» (updateRelaysList). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:668]

```
669:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:669]

```
670:                     // CLIENT-SIDE FILTER ENFORCEMENT: Ensure this event matches the subscription's filter
```
> تعليق: فرض المرشّح من جهة العميل: تأكّد أن هذا الحدث يطابق مرشّح الاشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:670]

```
671:                     activeSubscriptions[response.subscriptionId]?.let { subInfo ->
```
> يصل إلى عنصر «الاشتراكات النشطة» (activeSubscriptions) بالمفتاح «معرّف الاشتراك» (response.subscriptionId)، وإن لم يكن فارغاً ينفّذ كتلة let بمعامل «معلومات الاشتراك» (subInfo). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:671]

```
672:                         val matches = try { subInfo.filter.matches(response.event) } catch (e: Exception) { true }
```
> يُعرّف متغيّراً ثابتاً (val) باسم «يطابق» (matches) قيمته ناتج استدعاء «يطابق» (matches) على مرشّح «معلومات الاشتراك» (subInfo.filter) بتمرير الحدث (response.event) ضمن كتلة محاولة، وعند الاستثناء تكون القيمة صحيحة (true). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:672]

```
673:                         if (!matches) {
```
> يبدأ شرطاً إذا كانت قيمة «يطابق» (matches) غير صحيحة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:673]

```
674:                             Log.v(TAG, "🚫 Dropping event ${response.event.id.take(16)}... not matching filter for sub=${response.subscriptionId}")
```
> يستدعي تسجيلاً مستوى تفصيلي (Log.v) بالوسم TAG والنص «🚫 Dropping event» متبوعاً بأول ١٦ محرفاً من معرّف الحدث (response.event.id.take(16)) ثم «not matching filter for sub=» وقيمة معرّف الاشتراك (response.subscriptionId). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:674]

```
675:                             // Do NOT call deduplicator here to allow the correct subscription to process it later
```
> تعليق: لا تستدع مزيل التكرار هنا للسماح للاشتراك الصحيح بمعالجته لاحقاً. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:675]

```
676:                             return
```
> يُعيد من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:676]

```
677:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:677]

```
678:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:678]

```
679:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:679]

```
680:                     // DEDUPLICATION: Check if we've already processed this event
```
> تعليق: إزالة التكرار: تحقّق إن كنّا قد عالجنا هذا الحدث من قبل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:680]

```
681:                     val wasProcessed = eventDeduplicator.processEvent(response.event) { event ->
```
> يُعرّف متغيّراً ثابتاً (val) باسم «تمّت معالجته» (wasProcessed) قيمته ناتج استدعاء «معالجة الحدث» (processEvent) على «مزيل تكرار الأحداث» (eventDeduplicator) بتمرير الحدث (response.event) ودالة لامدا بمعامل «الحدث» (event). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:681]

```
682:                         // Only log non-gift-wrap events to reduce noise
```
> تعليق: سجّل فقط الأحداث غير المغلّفة كهدية لتقليل الضجيج. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:682]

```
683:                         if (event.kind != NostrKind.GIFT_WRAP) {
```
> يبدأ شرطاً إذا كان نوع الحدث (event.kind) لا يساوي «تغليف الهدية» (NostrKind.GIFT_WRAP). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:683]

```
684:                             val originGeo = activeSubscriptions[response.subscriptionId]?.originGeohash
```
> يُعرّف متغيّراً ثابتاً (val) باسم «الموقع الجغرافي الأصلي» (originGeo) قيمته حقل «جيوهاش الأصل» (originGeohash) من عنصر «الاشتراكات النشطة» (activeSubscriptions) بالمفتاح معرّف الاشتراك (response.subscriptionId) إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:684]

```
685:                             if (originGeo != null) {
```
> يبدأ شرطاً إذا كانت قيمة «الموقع الجغرافي الأصلي» (originGeo) ليست فارغة (null). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:685]

```
686:                                 Log.v(TAG, "📥 Processing event (kind=${event.kind}) from relay=$relayUrl geo=$originGeo sub=${response.subscriptionId}")
```
> يستدعي تسجيلاً مستوى تفصيلي (Log.v) بالوسم TAG والنص «📥 Processing event (kind=» متبوعاً بنوع الحدث (event.kind) ثم «from relay=» وعنوان المُرحِّل (relayUrl) ثم «geo=» والموقع الأصلي (originGeo) ثم «sub=» ومعرّف الاشتراك (response.subscriptionId). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:686]

```
687:                             } else {
```
> يُغلق فرع if ويبدأ فرع «وإلا» (else). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:687]

```
688:                                 Log.v(TAG, "📥 Processing event (kind=${event.kind}) from relay=$relayUrl sub=${response.subscriptionId}")
```
> يستدعي تسجيلاً مستوى تفصيلي (Log.v) بالوسم TAG والنص «📥 Processing event (kind=» متبوعاً بنوع الحدث (event.kind) ثم «from relay=» وعنوان المُرحِّل (relayUrl) ثم «sub=» ومعرّف الاشتراك (response.subscriptionId). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:688]

```
689:                             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:689]

```
690:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:690]

```
691:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:691]

```
692:                         // Call handler for new events only
```
> تعليق: استدع المعالِج للأحداث الجديدة فقط. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:692]

```
693:                         val handler = messageHandlers[response.subscriptionId]
```
> يُعرّف متغيّراً ثابتاً (val) باسم «المعالِج» (handler) قيمته عنصر «معالِجات الرسائل» (messageHandlers) بالمفتاح معرّف الاشتراك (response.subscriptionId). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:693]

```
694:                         if (handler != null) {
```
> يبدأ شرطاً إذا كانت قيمة «المعالِج» (handler) ليست فارغة (null). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:694]

```
695:                             scope.launch(Dispatchers.Main) {
```
> يستدعي «إطلاق» (launch) على «النطاق» (scope) بمُرسِل «الخيط الرئيسي» (Dispatchers.Main) ويبدأ كتلة الكوروتين. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:695]

```
696:                                 handler(event)
```
> يستدعي «المعالِج» (handler) بتمرير «الحدث» (event). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:696]

```
697:                             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:697]

```
698:                         } else {
```
> يُغلق فرع if ويبدأ فرع «وإلا» (else). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:698]

```
699:                             Log.w(TAG, "⚠️ No handler for subscription ${response.subscriptionId}")
```
> يستدعي تسجيلاً مستوى تحذير (Log.w) بالوسم TAG والنص «⚠️ No handler for subscription» متبوعاً بمعرّف الاشتراك (response.subscriptionId). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:699]

```
700:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:700]

```
701:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:701]

```
702:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:702]

```
703:                     if (!wasProcessed) {
```
> يبدأ شرطاً إذا كانت قيمة «تمّت معالجته» (wasProcessed) غير صحيحة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:703]

```
704:                         //Log.v(TAG, "🔄 Duplicate event ${response.event.id.take(16)}... from relay: $relayUrl")
```
> تعليق: سطر تسجيل معطّل: «🔄 Duplicate event …take(16)… from relay: relayUrl». [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:704]

```
705:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:705]

```
706:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:706]

```
707:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:707]

```
708:                 is NostrResponse.EndOfStoredEvents -> {
```
> فرع: عندما تكون «الاستجابة» (response) من نوع «نهاية الأحداث المخزّنة» (NostrResponse.EndOfStoredEvents). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:708]

```
709:                     Log.v(TAG, "End of stored events for subscription: ${response.subscriptionId}")
```
> يستدعي تسجيلاً مستوى تفصيلي (Log.v) بالوسم TAG والنص «End of stored events for subscription:» متبوعاً بمعرّف الاشتراك (response.subscriptionId). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:709]

```
710:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:710]

```
711:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:711]

```
712:                 is NostrResponse.Ok -> {
```
> فرع: عندما تكون «الاستجابة» (response) من نوع «موافق» (NostrResponse.Ok). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:712]

```
713:                     val wasGiftWrap = pendingGiftWrapIDs.remove(response.eventId)
```
> يُعرّف متغيّراً ثابتاً (val) باسم «كان تغليف هدية» (wasGiftWrap) قيمته ناتج «إزالة» (remove) معرّف الحدث (response.eventId) من «معرّفات تغليف الهدية المعلّقة» (pendingGiftWrapIDs). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:713]

```
714:                     if (response.accepted) {
```
> يبدأ شرطاً إذا كان حقل «مقبول» (response.accepted) صحيحاً. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:714]

```
715:                         Log.d(TAG, "✅ Event accepted id=${response.eventId.take(16)}... by relay: $relayUrl")
```
> يستدعي تسجيلاً مستوى تنقيح (Log.d) بالوسم TAG والنص «✅ Event accepted id=» متبوعاً بأول ١٦ محرفاً من معرّف الحدث (response.eventId.take(16)) ثم «by relay:» وعنوان المُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:715]

```
716:                     } else {
```
> يُغلق فرع if ويبدأ فرع «وإلا» (else). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:716]

```
717:                         val level = if (wasGiftWrap) Log.WARN else Log.ERROR
```
> يُعرّف متغيّراً ثابتاً (val) باسم «المستوى» (level) قيمته Log.WARN إن كانت «كان تغليف هدية» (wasGiftWrap) صحيحة، وإلا Log.ERROR. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:717]

```
718:                         Log.println(level, TAG, "📮 Event ${response.eventId.take(16)}... rejected by relay: ${response.message ?: "no reason"}")
```
> يستدعي «طباعة سجل» (Log.println) بالمستوى (level) والوسم TAG والنص «📮 Event» متبوعاً بأول ١٦ محرفاً من معرّف الحدث (response.eventId.take(16)) ثم «rejected by relay:» ورسالة الاستجابة (response.message) أو «no reason» إن كانت فارغة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:718]

```
719:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:719]

```
720:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:720]

```
721:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:721]

```
722:                 is NostrResponse.Notice -> {
```
> فرع: عندما تكون «الاستجابة» (response) من نوع «إشعار» (NostrResponse.Notice). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:722]

```
723:                     Log.i(TAG, "📢 Notice from $relayUrl: ${response.message}")
```
> يستدعي تسجيلاً مستوى معلومة (Log.i) بالوسم TAG والنص «📢 Notice from» متبوعاً بعنوان المُرحِّل (relayUrl) ثم رسالة الاستجابة (response.message). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:723]

```
724:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:724]

```
725:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:725]

```
726:                 is NostrResponse.Unknown -> {
```
> فرع: عندما تكون «الاستجابة» (response) من نوع «غير معروف» (NostrResponse.Unknown). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:726]

```
727:                     Log.v(TAG, "Unknown message type from $relayUrl: ${response.raw}")
```
> يستدعي تسجيلاً مستوى تفصيلي (Log.v) بالوسم TAG والنص «Unknown message type from» متبوعاً بعنوان المُرحِّل (relayUrl) ثم الحقل الخام (response.raw). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:727]

```
728:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:728]

```
729:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:729]

```
730:         } catch (e: Exception) {
```
> يُغلق كتلة المحاولة ويبدأ كتلة «التقاط» (catch) لاستثناء (Exception) باسم e. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:730]

```
731:             Log.e(TAG, "Failed to parse message from $relayUrl: ${e.message}")
```
> يستدعي تسجيلاً مستوى خطأ (Log.e) بالوسم TAG والنص «Failed to parse message from» متبوعاً بعنوان المُرحِّل (relayUrl) ثم رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:731]

```
732:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:732]

```
733:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:733]

```
734:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:734]

```
735:     private fun handleDisconnection(relayUrl: String, error: Throwable) {
```
> يُعرّف دالة خاصة باسم «معالجة قطع الاتصال» (handleDisconnection) تأخذ «عنوان المُرحِّل» (relayUrl) من نوع String و«الخطأ» (error) من نوع Throwable. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:735]

```
736:         connections.remove(relayUrl)
```
> يستدعي «إزالة» (remove) من مجموعة «الاتصالات» (connections) بالمفتاح «عنوان المُرحِّل» (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:736]

```
737:         // NOTE: Don't remove subscriptions here - keep them for restoration on reconnection
```
> تعليق: ملاحظة: لا تُزِل الاشتراكات هنا، أبقِها للاستعادة عند إعادة الاتصال. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:737]

```
738:         // subscriptions.remove(relayUrl)  // REMOVED - this was causing subscription loss
```
> تعليق: subscriptions.remove(relayUrl) محذوف، فقد كان يسبّب فقدان الاشتراك. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:738]

```
739:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:739]

```
740:         updateRelayStatus(relayUrl, false, error)
```
> يستدعي دالة «تحديث حالة المُرحِّل» (updateRelayStatus) بتمرير «عنوان المُرحِّل» (relayUrl) والقيمة false و«الخطأ» (error). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:740]

```
741:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:741]

```
742:         // Check if this is a DNS error
```
> تعليق: تحقّق إن كان هذا خطأ DNS. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:742]

```
743:         val errorMessage = error.message?.lowercase() ?: ""
```
> يُعرّف متغيّراً ثابتاً (val) باسم «رسالة الخطأ» (errorMessage) قيمته رسالة الخطأ (error.message) بأحرف صغيرة (lowercase) أو سلسلة فارغة إن كانت فارغة (null). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:743]

```
744:         if (errorMessage.contains("hostname could not be found") || 
```
> يبدأ شرطاً إذا كانت «رسالة الخطأ» (errorMessage) تحتوي على «hostname could not be found» أو (يتبع). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:744]

```
745:             errorMessage.contains("dns") ||
```
> تكملة الشرط: أو تحتوي «رسالة الخطأ» (errorMessage) على «dns» أو. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:745]

```
746:             errorMessage.contains("unable to resolve host")) {
```
> تكملة الشرط: أو تحتوي «رسالة الخطأ» (errorMessage) على «unable to resolve host»، ثم يُفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:746]

```
747:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:747]

```
748:             val relay = relaysList.find { it.url == relayUrl }
```
> يُعرّف متغيّراً ثابتاً (val) باسم «المُرحِّل» (relay) قيمته أول عنصر في «قائمة المُرحِّلات» (relaysList) عنوانه (url) يساوي «عنوان المُرحِّل» (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:748]

```
749:             if (relay?.lastError == null) {
```
> يبدأ شرطاً إذا كان حقل «آخر خطأ» (lastError) على «المُرحِّل» (relay) فارغاً (null). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:749]

```
750:                 Log.w(TAG, "Nostr relay DNS failure for $relayUrl - not retrying")
```
> يستدعي تسجيلاً مستوى تحذير (Log.w) بالوسم TAG والنص «Nostr relay DNS failure for» متبوعاً بعنوان المُرحِّل (relayUrl) ثم «- not retrying». [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:750]

```
751:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:751]

```
752:             return
```
> يُعيد من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:752]

```
753:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:753]

```
754:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:754]

```
755:         // Implement exponential backoff for non-DNS errors
```
> تعليق: طبّق تراجعاً أسّياً للأخطاء غير DNS. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:755]

```
756:         val relay = relaysList.find { it.url == relayUrl } ?: return
```
> يُعرّف متغيّراً ثابتاً (val) باسم «المُرحِّل» (relay) قيمته أول عنصر في «قائمة المُرحِّلات» (relaysList) عنوانه (url) يساوي «عنوان المُرحِّل» (relayUrl)، وإن كان فارغاً يُعيد من الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:756]

```
757:         relay.reconnectAttempts++
```
> يزيد حقل «محاولات إعادة الاتصال» (reconnectAttempts) على «المُرحِّل» (relay) بمقدار واحد. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:757]

```
758:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:758]

```
759:         // Stop attempting after max attempts
```
> تعليق: توقّف عن المحاولة بعد الحد الأقصى للمحاولات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:759]

```
760:         if (relay.reconnectAttempts >= MAX_RECONNECT_ATTEMPTS) {
```
> يبدأ شرطاً إذا كان «محاولات إعادة الاتصال» (reconnectAttempts) أكبر من أو يساوي «الحد الأقصى لمحاولات إعادة الاتصال» (MAX_RECONNECT_ATTEMPTS). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:760]

```
761:             Log.w(TAG, "Max reconnection attempts ($MAX_RECONNECT_ATTEMPTS) reached for $relayUrl")
```
> يستدعي تسجيلاً مستوى تحذير (Log.w) بالوسم TAG والنص «Max reconnection attempts (» متبوعاً بقيمة الحد الأقصى (MAX_RECONNECT_ATTEMPTS) ثم «reached for» وعنوان المُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:761]

```
762:             return
```
> يُعيد من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:762]

```
763:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:763]

```
764:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:764]

```
765:         // Calculate backoff interval
```
> تعليق: احسب فترة التراجع. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:765]

```
766:         val backoffInterval = min(
```
> يُعرّف متغيّراً ثابتاً (val) باسم «فترة التراجع» (backoffInterval) قيمته ناتج دالة «الأصغر» (min) ويبدأ تمرير وسائطها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:766]

```
767:             INITIAL_BACKOFF_INTERVAL * BACKOFF_MULTIPLIER.pow(relay.reconnectAttempts - 1.0),
```
> الوسيط الأول: «فترة التراجع الأولية» (INITIAL_BACKOFF_INTERVAL) مضروبة في «مضاعِف التراجع» (BACKOFF_MULTIPLIER) مرفوعاً إلى أُسّ (pow) قيمته محاولات إعادة الاتصال (relay.reconnectAttempts) ناقص 1.0. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:767]

```
768:             MAX_BACKOFF_INTERVAL.toDouble()
```
> الوسيط الثاني: «الحد الأقصى لفترة التراجع» (MAX_BACKOFF_INTERVAL) محوّلاً إلى عدد عشري مزدوج (toDouble). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:768]

```
769:         ).toLong()
```
> يُغلق استدعاء «الأصغر» (min) ويحوّل ناتجه إلى عدد صحيح طويل (toLong). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:769]

```
770:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:770]

```
771:         relay.nextReconnectTime = System.currentTimeMillis() + backoffInterval
```
> يضبط حقل «وقت إعادة الاتصال التالي» (nextReconnectTime) على «المُرحِّل» (relay) إلى الوقت الحالي بالميلّي ثانية (System.currentTimeMillis) مضافاً إليه «فترة التراجع» (backoffInterval). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:771]

```
772:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:772]

```
773:         Log.d(TAG, "Scheduling reconnection to $relayUrl in ${backoffInterval / 1000}s (attempt ${relay.reconnectAttempts})")
```
> يستدعي تسجيلاً مستوى تنقيح (Log.d) بالوسم TAG والنص «Scheduling reconnection to» متبوعاً بعنوان المُرحِّل (relayUrl) ثم «in» وفترة التراجع مقسومة على 1000 (backoffInterval / 1000) و«s (attempt» ومحاولات إعادة الاتصال (relay.reconnectAttempts). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:773]

```
774:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:774]

```
775:         // Schedule reconnection
```
> تعليق: جدوِل إعادة الاتصال. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:775]

```
776:         scope.launch {
```
> يستدعي «إطلاق» (launch) على «النطاق» (scope) ويبدأ كتلة الكوروتين. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:776]

```
777:             delay(backoffInterval)
```
> يستدعي «تأخير» (delay) بمدة «فترة التراجع» (backoffInterval). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:777]

```
778:             connectToRelay(relayUrl)
```
> يستدعي دالة «الاتصال بالمُرحِّل» (connectToRelay) بتمرير «عنوان المُرحِّل» (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:778]

```
779:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:779]

```
780:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:780]

```
781:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:781]

```
782:     private fun updateRelayStatus(url: String, isConnected: Boolean, error: Throwable? = null) {
```
> يُعرّف دالة خاصة باسم «تحديث حالة المُرحِّل» (updateRelayStatus) تأخذ «العنوان» (url) من نوع String و«متصل» (isConnected) من نوع Boolean و«الخطأ» (error) من نوع Throwable القابل للفراغ بقيمة افتراضية null. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:782]

```
783:         val relay = relaysList.find { it.url == url } ?: return
```
> يُعرّف متغيّراً ثابتاً (val) باسم «المُرحِّل» (relay) قيمته أول عنصر في «قائمة المُرحِّلات» (relaysList) عنوانه (url) يساوي «العنوان» (url)، وإن كان فارغاً يُعيد من الدالة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:783]

```
784:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:784]

```
785:         relay.isConnected = isConnected
```
> يضبط حقل «متصل» (isConnected) على «المُرحِّل» (relay) إلى قيمة الوسيط «متصل» (isConnected). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:785]

```
786:         relay.lastError = error
```
> يضبط حقل «آخر خطأ» (lastError) على «المُرحِّل» (relay) إلى قيمة الوسيط «الخطأ» (error). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:786]

```
787:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:787]

```
788:         if (isConnected) {
```
> يبدأ شرطاً إذا كانت قيمة «متصل» (isConnected) صحيحة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:788]

```
789:             relay.lastConnectedAt = System.currentTimeMillis()
```
> يضبط حقل «آخر وقت اتصال» (lastConnectedAt) على «المُرحِّل» (relay) إلى الوقت الحالي بالميلّي ثانية (System.currentTimeMillis). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:789]

```
790:             relay.reconnectAttempts = 0
```
> يضبط حقل «محاولات إعادة الاتصال» (reconnectAttempts) على «المُرحِّل» (relay) إلى صفر. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:790]

```
791:             relay.nextReconnectTime = null
```
> يضبط حقل «وقت إعادة الاتصال التالي» (nextReconnectTime) على «المُرحِّل» (relay) إلى القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:791]

```
792:         } else {
```
> يُغلق فرع if ويبدأ فرع «وإلا» (else). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:792]

```
793:             relay.lastDisconnectedAt = System.currentTimeMillis()
```
> يضبط حقل «آخر وقت قطع اتصال» (lastDisconnectedAt) على «المُرحِّل» (relay) إلى الوقت الحالي بالميلّي ثانية (System.currentTimeMillis). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:793]

```
794:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:794]

```
795:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:795]

```
796:         updateRelaysList()
```
> يستدعي دالة «تحديث قائمة المُرحِّلات» (updateRelaysList). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:796]

```
797:         updateConnectionStatus()
```
> يستدعي دالة «تحديث حالة الاتصال» (updateConnectionStatus). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:797]

```
798:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:798]

```
799:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:799]

```
800:     private fun updateRelaysList() {
```
> يُعرّف دالة خاصة باسم «تحديث قائمة المُرحِّلات» (updateRelaysList) بلا وسائط ويبدأ نطاق جسمها. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:800]
