# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt (الأسطر 801–893)

```
801:         _relays.value = relaysList.toList()
```
> يُسنِد إلى خاصية القيمة (value) للحقل القابل للملاحظة (‎_relays‎) نسخةً من قائمة المُرحِّلات (relaysList) عبر استدعاء ‎toList()‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:801]

```
802:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:802]

```
803:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:803]

```
804:     private fun updateConnectionStatus() {
```
> يُعرّف دالةً خاصةً (private) باسم تحديث حالة الاتصال (updateConnectionStatus) بلا وُسطاء ولا نوع إرجاع مُعلَن. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:804]

```
805:         val connected = relaysList.any { it.isConnected }
```
> يُعرّف متغيّراً ثابتاً (val) باسم متَّصِل (connected) قيمتُه نتيجة استدعاء ‎any‎ على قائمة المُرحِّلات (relaysList) التي تُعيد صحيحاً إن كان أيُّ عنصر خاصيتُه ‎isConnected‎ صحيحة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:805]

```
806:         _isConnected.value = connected
```
> يُسنِد إلى خاصية القيمة (value) للحقل القابل للملاحظة (‎_isConnected‎) قيمةَ المتغيّر متَّصِل (connected). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:806]

```
807:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:807]

```
808:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:808]

```
809:     private fun generateSubscriptionId(): String {
```
> يُعرّف دالةً خاصةً (private) باسم توليد معرّف الاشتراك (generateSubscriptionId) بلا وُسطاء ونوع إرجاعها نصّ (String). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:809]

```
810:         return "sub-${System.currentTimeMillis()}-${(Math.random() * 1000).toInt()}"
```
> يُعيد نصّاً يبدأ بـ ‎"sub-"‎ ثم القيمة الزمنية الحالية بالملّي ثانية من ‎System.currentTimeMillis()‎ ثم شَرطةً ثم عدداً صحيحاً ناتجاً عن ضرب ‎Math.random()‎ في ‎1000‎ ثم تحويله إلى صحيح عبر ‎toInt()‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:810]

```
811:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:811]

```
812:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:812]

```
813:     /**
```
> تعليق: بداية تعليق توثيقي (مفتوح). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:813]

```
814:      * Restore all active subscriptions for a specific relay that just reconnected
```
> تعليق: استعادة كل الاشتراكات النشطة لمُرحِّل معيّن أعاد الاتصال للتوّ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:814]

```
815:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:815]

```
816:     private fun restoreSubscriptionsForRelay(relayUrl: String, webSocket: WebSocket) {
```
> يُعرّف دالةً خاصةً (private) باسم استعادة اشتراكات المُرحِّل (restoreSubscriptionsForRelay) تأخذ وسيطاً نصّياً عنوان المُرحِّل (relayUrl) ووسيطاً من نوع مقبس الويب (WebSocket) باسم ‎webSocket‎ بلا نوع إرجاع مُعلَن. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:816]

```
817:         val subscriptionsToRestore = activeSubscriptions.values.filter { subscriptionInfo ->
```
> يُعرّف متغيّراً ثابتاً (val) باسم اشتراكات للاستعادة (subscriptionsToRestore) قيمتُه نتيجة ترشيح ‎filter‎ على قيَم (values) الاشتراكات النشطة (activeSubscriptions) مع وسيط لامدا باسم معلومات الاشتراك (subscriptionInfo). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:817]

```
818:             // Include subscription if it targets all relays or specifically targets this relay
```
> تعليق: ضمِّن الاشتراك إن كان يستهدف كل المُرحِّلات أو يستهدف هذا المُرحِّل تحديداً. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:818]

```
819:             subscriptionInfo.targetRelayUrls == null || subscriptionInfo.targetRelayUrls.contains(relayUrl)
```
> يُعيد تعبير الترشيح صحيحاً إذا كانت خاصية عناوين المُرحِّلات المستهدفة (targetRelayUrls) لمعلومات الاشتراك مساويةً لـ ‎null‎ أو إذا كانت تحتوي (contains) على عنوان المُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:819]

```
820:         }
```
> إغلاق نطاق (نهاية لامدا الترشيح). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:820]

```
821:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:821]

```
822:         if (subscriptionsToRestore.isEmpty()) {
```
> شرط ‎if‎ يفحص ما إذا كانت قائمة اشتراكات للاستعادة (subscriptionsToRestore) فارغةً عبر ‎isEmpty()‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:822]

```
823:             Log.v(TAG, "🔄 No subscriptions to restore for relay: $relayUrl")
```
> يستدعي تسجيلاً بمستوى مُسهَب ‎Log.v‎ بالوسم ‎TAG‎ ونصّ «لا اشتراكات لاستعادتها للمُرحِّل» متبوعاً بعنوان المُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:823]

```
824:             return
```
> يُعيد من الدالة دون قيمة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:824]

```
825:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:825]

```
826:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:826]

```
827:         Log.d(TAG, "🔄 Restoring ${subscriptionsToRestore.size} subscriptions for relay: $relayUrl")
```
> يستدعي تسجيلاً بمستوى تنقيح ‎Log.d‎ بالوسم ‎TAG‎ ونصّ «استعادة» متبوعاً بحجم (size) قائمة اشتراكات للاستعادة ثم «اشتراكات للمُرحِّل» وعنوان المُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:827]

```
828:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:828]

```
829:         subscriptionsToRestore.forEach { subscriptionInfo ->
```
> يستدعي ‎forEach‎ على قائمة اشتراكات للاستعادة (subscriptionsToRestore) مع وسيط لامدا باسم معلومات الاشتراك (subscriptionInfo). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:829]

```
830:             try {
```
> يبدأ كتلة ‎try‎ لمعالجة الاستثناءات. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:830]

```
831:                 val request = NostrRequest.Subscribe(subscriptionInfo.id, listOf(subscriptionInfo.filter))
```
> يُعرّف متغيّراً ثابتاً (val) باسم طلب (request) قيمتُه إنشاء طلب اشتراك (NostrRequest.Subscribe) بوسيطين: معرّف الاشتراك (subscriptionInfo.id) وقائمة ‎listOf‎ تحوي مُرشِّح الاشتراك (subscriptionInfo.filter). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:831]

```
832:                 val message = gson.toJson(request, NostrRequest::class.java)
```
> يُعرّف متغيّراً ثابتاً (val) باسم رسالة (message) قيمتُه تحويل الطلب (request) إلى نصّ JSON عبر ‎gson.toJson‎ مع تمرير صنف ‎NostrRequest::class.java‎ كنوع. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:832]

```
833:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:833]

```
834:                 val success = webSocket.send(message)
```
> يُعرّف متغيّراً ثابتاً (val) باسم نجاح (success) قيمتُه نتيجة إرسال الرسالة (message) عبر ‎webSocket.send‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:834]

```
835:                 if (success) {
```
> شرط ‎if‎ يفحص ما إذا كانت قيمة نجاح (success) صحيحة. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:835]

```
836:                     // Track subscription for this relay
```
> تعليق: تتبَّع الاشتراك لهذا المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:836]

```
837:                     val currentSubs = subscriptions[relayUrl] ?: emptySet()
```
> يُعرّف متغيّراً ثابتاً (val) باسم اشتراكات حالية (currentSubs) قيمتُه قيمةُ المفتاح عنوان المُرحِّل (relayUrl) من الخريطة ‎subscriptions‎ أو مجموعةٌ فارغة ‎emptySet()‎ عند العدم (عبر ‎?:‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:837]

```
838:                     subscriptions[relayUrl] = currentSubs + subscriptionInfo.id
```
> يُسنِد إلى المفتاح عنوان المُرحِّل (relayUrl) في الخريطة ‎subscriptions‎ مجموعةَ الاشتراكات الحالية (currentSubs) مضافاً إليها معرّف الاشتراك (subscriptionInfo.id). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:838]

```
839:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:839]

```
840:                     Log.v(TAG, "✅ Restored subscription '${subscriptionInfo.id}' to relay: $relayUrl")
```
> يستدعي تسجيلاً بمستوى مُسهَب ‎Log.v‎ بالوسم ‎TAG‎ ونصّ «استُعيد الاشتراك» متبوعاً بمعرّف الاشتراك (subscriptionInfo.id) ثم «إلى المُرحِّل» وعنوان المُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:840]

```
841:                 } else {
```
> إغلاق نطاق كتلة ‎if‎ وبدء كتلة ‎else‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:841]

```
842:                     Log.w(TAG, "❌ Failed to restore subscription '${subscriptionInfo.id}' to $relayUrl: WebSocket send failed")
```
> يستدعي تسجيلاً بمستوى تحذير ‎Log.w‎ بالوسم ‎TAG‎ ونصّ «فشلت استعادة الاشتراك» متبوعاً بمعرّف الاشتراك (subscriptionInfo.id) ثم «إلى» وعنوان المُرحِّل (relayUrl) ثم «فشل إرسال مقبس الويب». [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:842]

```
843:                 }
```
> إغلاق نطاق (نهاية كتلة ‎else‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:843]

```
844:             } catch (e: Exception) {
```
> يلتقط استثناءً (Exception) باسم ‎e‎ في كتلة ‎catch‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:844]

```
845:                 Log.e(TAG, "❌ Failed to restore subscription '${subscriptionInfo.id}' to $relayUrl: ${e.message}")
```
> يستدعي تسجيلاً بمستوى خطأ ‎Log.e‎ بالوسم ‎TAG‎ ونصّ «فشلت استعادة الاشتراك» متبوعاً بمعرّف الاشتراك (subscriptionInfo.id) ثم «إلى» وعنوان المُرحِّل (relayUrl) ثم رسالة الاستثناء (e.message). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:845]

```
846:             }
```
> إغلاق نطاق (نهاية كتلة ‎try/catch‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:846]

```
847:         }
```
> إغلاق نطاق (نهاية لامدا ‎forEach‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:847]

```
848:     }
```
> إغلاق نطاق (نهاية الدالة). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:848]

```
849:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:849]

```
850:     /**
```
> تعليق: بداية تعليق توثيقي (مفتوح). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:850]

```
851:      * WebSocket listener for relay connections
```
> تعليق: مُستمِع مقبس الويب لاتصالات المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:851]

```
852:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:852]

```
853:     private inner class RelayWebSocketListener(private val relayUrl: String) : WebSocketListener() {
```
> يُعرّف صنفاً داخلياً (inner class) خاصّاً باسم مُستمِع مقبس ويب المُرحِّل (RelayWebSocketListener) بمُعامِل بانٍ خاصٍّ ثابت عنوان المُرحِّل (relayUrl) نصّيّ، ويرث من مُستمِع مقبس الويب (WebSocketListener). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:853]

```
854:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:854]

```
855:         override fun onOpen(webSocket: WebSocket, response: Response) {
```
> يتجاوز (override) الدالة عند الفتح (onOpen) بوسيطين: مقبس الويب (webSocket) واستجابة (Response) باسم ‎response‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:855]

```
856:             Log.d(TAG, "✅ Connected to Nostr relay: $relayUrl")
```
> يستدعي تسجيلاً بمستوى تنقيح ‎Log.d‎ بالوسم ‎TAG‎ ونصّ «اتُّصِل بمُرحِّل نوستر» متبوعاً بعنوان المُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:856]

```
857:             updateRelayStatus(relayUrl, true)
```
> يستدعي دالة تحديث حالة المُرحِّل (updateRelayStatus) بوسيطين: عنوان المُرحِّل (relayUrl) والقيمة ‎true‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:857]

```
858:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:858]

```
859:             // Restore all active subscriptions for this relay
```
> تعليق: استعِد كل الاشتراكات النشطة لهذا المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:859]

```
860:             restoreSubscriptionsForRelay(relayUrl, webSocket)
```
> يستدعي دالة استعادة اشتراكات المُرحِّل (restoreSubscriptionsForRelay) بوسيطين: عنوان المُرحِّل (relayUrl) ومقبس الويب (webSocket). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:860]

```
861:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:861]

```
862:             // Process any queued messages for this relay
```
> تعليق: عالِج أيَّ رسائل مُصطفّة لهذا المُرحِّل. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:862]

```
863:             synchronized(messageQueueLock) {
```
> يبدأ كتلة متزامنة ‎synchronized‎ على القفل (messageQueueLock). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:863]

```
864:                 val iterator = messageQueue.iterator()
```
> يُعرّف متغيّراً ثابتاً (val) باسم مُكرِّر (iterator) قيمتُه مُكرِّر طابور الرسائل (messageQueue) عبر ‎iterator()‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:864]

```
865:                 while (iterator.hasNext()) {
```
> حلقة ‎while‎ تستمر ما دام للمُكرِّر (iterator) عنصرٌ تالٍ عبر ‎hasNext()‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:865]

```
866:                     val (event, targetRelays) = iterator.next()
```
> يُفكِّك العنصر التالي من المُكرِّر (iterator.next()) إلى متغيّرين ثابتين: حدث (event) ومُرحِّلات مستهدفة (targetRelays). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:866]

```
867:                     if (relayUrl in targetRelays) {
```
> شرط ‎if‎ يفحص ما إذا كان عنوان المُرحِّل (relayUrl) موجوداً ضمن المُرحِّلات المستهدفة (targetRelays). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:867]

```
868:                         sendToRelay(event, webSocket, relayUrl)
```
> يستدعي دالة الإرسال إلى المُرحِّل (sendToRelay) بثلاثة وُسطاء: حدث (event) ومقبس الويب (webSocket) وعنوان المُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:868]

```
869:                     }
```
> إغلاق نطاق (نهاية كتلة ‎if‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:869]

```
870:                 }
```
> إغلاق نطاق (نهاية حلقة ‎while‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:870]

```
871:             }
```
> إغلاق نطاق (نهاية الكتلة المتزامنة). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:871]

```
872:         }
```
> إغلاق نطاق (نهاية دالة ‎onOpen‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:872]

```
873:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:873]

```
874:         override fun onMessage(webSocket: WebSocket, text: String) {
```
> يتجاوز (override) الدالة عند الرسالة (onMessage) بوسيطين: مقبس الويب (webSocket) ونصّ (text) نصّيّ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:874]

```
875:             handleMessage(text, relayUrl)
```
> يستدعي دالة معالجة الرسالة (handleMessage) بوسيطين: النصّ (text) وعنوان المُرحِّل (relayUrl). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:875]

```
876:         }
```
> إغلاق نطاق (نهاية دالة ‎onMessage‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:876]

```
877:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:877]

```
878:         override fun onClosing(webSocket: WebSocket, code: Int, reason: String) {
```
> يتجاوز (override) الدالة عند الإغلاق الجاري (onClosing) بثلاثة وُسطاء: مقبس الويب (webSocket) ورمز (code) صحيح وسبب (reason) نصّيّ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:878]

```
879:             Log.d(TAG, "WebSocket closing for $relayUrl: $code $reason")
```
> يستدعي تسجيلاً بمستوى تنقيح ‎Log.d‎ بالوسم ‎TAG‎ ونصّ «إغلاق مقبس الويب جارٍ لـ» متبوعاً بعنوان المُرحِّل (relayUrl) ثم الرمز (code) والسبب (reason). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:879]

```
880:         }
```
> إغلاق نطاق (نهاية دالة ‎onClosing‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:880]

```
881:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:881]

```
882:         override fun onClosed(webSocket: WebSocket, code: Int, reason: String) {
```
> يتجاوز (override) الدالة عند الإغلاق التامّ (onClosed) بثلاثة وُسطاء: مقبس الويب (webSocket) ورمز (code) صحيح وسبب (reason) نصّيّ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:882]

```
883:             Log.d(TAG, "WebSocket closed for $relayUrl: $code $reason")
```
> يستدعي تسجيلاً بمستوى تنقيح ‎Log.d‎ بالوسم ‎TAG‎ ونصّ «أُغلِق مقبس الويب لـ» متبوعاً بعنوان المُرحِّل (relayUrl) ثم الرمز (code) والسبب (reason). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:883]

```
884:             val error = Exception("WebSocket closed: $code $reason")
```
> يُعرّف متغيّراً ثابتاً (val) باسم خطأ (error) قيمتُه استثناء (Exception) جديد برسالة «أُغلِق مقبس الويب» متبوعةً بالرمز (code) والسبب (reason). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:884]

```
885:             handleDisconnection(relayUrl, error)
```
> يستدعي دالة معالجة قطع الاتصال (handleDisconnection) بوسيطين: عنوان المُرحِّل (relayUrl) والخطأ (error). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:885]

```
886:         }
```
> إغلاق نطاق (نهاية دالة ‎onClosed‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:886]

```
887:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:887]

```
888:         override fun onFailure(webSocket: WebSocket, t: Throwable, response: Response?) {
```
> يتجاوز (override) الدالة عند الفشل (onFailure) بثلاثة وُسطاء: مقبس الويب (webSocket) وقابلٌ للرمي (Throwable) باسم ‎t‎ واستجابة (Response) قابلة للعدم باسم ‎response‎. [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:888]

```
889:             Log.e(TAG, "❌ WebSocket failure for $relayUrl: ${t.message}")
```
> يستدعي تسجيلاً بمستوى خطأ ‎Log.e‎ بالوسم ‎TAG‎ ونصّ «فشل مقبس الويب لـ» متبوعاً بعنوان المُرحِّل (relayUrl) ثم رسالة القابل للرمي (t.message). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:889]

```
890:             handleDisconnection(relayUrl, t)
```
> يستدعي دالة معالجة قطع الاتصال (handleDisconnection) بوسيطين: عنوان المُرحِّل (relayUrl) والقابل للرمي (t). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:890]

```
891:         }
```
> إغلاق نطاق (نهاية دالة ‎onFailure‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:891]

```
892:     }
```
> إغلاق نطاق (نهاية الصنف الداخلي ‎RelayWebSocketListener‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:892]

```
893: }
```
> إغلاق نطاق (نهاية الصنف ‎NostrRelayManager‎). [app/src/main/java/com/bitchat/android/nostr/NostrRelayManager.kt:893]
