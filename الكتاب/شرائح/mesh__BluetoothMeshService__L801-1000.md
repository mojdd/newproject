# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt (الأسطر 801–1000)

```
801:             val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت باسم «حزمة» (packet) ويُسنَد إليه إنشاء كائن من نوع حزمة بِت-شات (BitchatPacket) بفتح قائمة المعطيات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:801]

```
802:                 version = 2u,  // FILE_TRANSFER uses v2 for 4-byte payload length to support large files
```
> يُضبَط معطى الإصدار (version) إلى القيمة العددية غير المُوقَّعة 2u، يليه تعليق: نقل الملف (FILE_TRANSFER) يستعمل الإصدار الثاني لطول حمولة بأربعة بايتات لدعم الملفات الكبيرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:802]

```
803:                 type = MessageType.FILE_TRANSFER.value,
```
> يُضبَط معطى النوع (type) إلى قيمة العنصر نقل الملف (FILE_TRANSFER) من تعداد نوع الرسالة (MessageType). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:803]

```
804:                 senderID = hexStringToByteArray(myPeerID),
```
> يُضبَط معطى مُعرّف المُرسِل (senderID) إلى ناتج استدعاء الدالة تحويل-السلسلة-الست-عشرية-إلى-مصفوفة-بايت (hexStringToByteArray) مُمرَّراً إليها مُعرّف نِدّي (myPeerID). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:804]

```
805:                 recipientID = SpecialRecipients.BROADCAST,
```
> يُضبَط معطى مُعرّف المُستقبِل (recipientID) إلى العنصر بث (BROADCAST) من المُستقبِلين الخاصّين (SpecialRecipients). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:805]

```
806:                 timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط معطى الطابع-الزمني (timestamp) إلى الوقت الحالي بالمللي ثانية من النظام مُحوَّلاً إلى عدد طويل غير مُوقَّع. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:806]

```
807:                 payload = payload,
```
> يُضبَط معطى الحمولة (payload) إلى المتغيّر «حمولة» (payload). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:807]

```
808:                 signature = null,
```
> يُضبَط معطى التوقيع (signature) إلى القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:808]

```
809:                 ttl = MAX_TTL
```
> يُضبَط معطى مدّة-البقاء (ttl) إلى الثابت أقصى-مدّة-بقاء (MAX_TTL). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:809]

```
810:             )
```
> إغلاق قائمة معطيات إنشاء كائن الحزمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:810]

```
811:             val signed = signPacketBeforeBroadcast(packet)
```
> يُعرَّف متغيّر ثابت باسم «مُوقَّع» (signed) ويُسنَد إليه ناتج استدعاء الدالة توقيع-الحزمة-قبل-البث (signPacketBeforeBroadcast) مُمرَّراً إليها الحزمة (packet). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:811]

```
812:             // Use a stable transferId based on the file TLV payload for progress tracking
```
> تعليق: استعمل مُعرّف نقل ثابتاً مبنيّاً على حمولة الملف بصيغة طول-قيمة-نوع (TLV) لتتبّع التقدّم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:812]

```
813:             val transferId = sha256Hex(payload)
```
> يُعرَّف متغيّر ثابت باسم «مُعرّف-النقل» (transferId) ويُسنَد إليه ناتج استدعاء الدالة بصمة-سها-256-ست-عشرية (sha256Hex) مُمرَّراً إليها الحمولة (payload). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:813]

```
814:             broadcastRoutedPacket(RoutedPacket(signed, transferId = transferId))
```
> تُستدعى الدالة بثّ-الحزمة-المُوجَّهة (broadcastRoutedPacket) مُمرَّراً إليها كائن حزمة-مُوجَّهة (RoutedPacket) مُنشأ من «المُوقَّع» (signed) ومُعرّف-النقل (transferId) مضبوطاً إلى متغيّر مُعرّف-النقل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:814]

```
815:             try { gossipSyncManager.onPublicPacketSeen(signed) } catch (_: Exception) { }
```
> ضمن كتلة محاولة (try) تُستدعى الدالة عند-رؤية-حزمة-عامة (onPublicPacketSeen) على مُدير-مزامنة-الإشاعة (gossipSyncManager) مُمرَّراً إليها «المُوقَّع»، مع كتلة التقاط (catch) لأي استثناء (Exception) فارغة الجسم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:815]

```
816:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:816]

```
817:             } catch (e: Exception) {
```
> كتلة التقاط (catch) لاستثناء (Exception) مُسمّى «e»، بفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:817]

```
818:             Log.e(TAG, "❌ sendFileBroadcast failed: ${e.message}", e)
```
> تُستدعى دالة التسجيل بمستوى الخطأ (Log.e) مُمرَّراً إليها الوسم (TAG) ونصاً «sendFileBroadcast failed» مع رسالة الاستثناء، والاستثناء «e». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:818]

```
819:             Log.e(TAG, "❌ File: name=${file.fileName}, size=${file.fileSize}")
```
> تُستدعى دالة التسجيل بمستوى الخطأ (Log.e) مُمرَّراً إليها الوسم ونصاً يحوي اسم الملف (file.fileName) وحجم الملف (file.fileSize). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:819]

```
820:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:820]

```
821:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:821]

```
822: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:822]

```
823:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:823]

```
824:      * Send a file as an encrypted private message using Noise protocol
```
> تعليق: أرسِل ملفاً كرسالة خاصة مُشفَّرة باستعمال بروتوكول نويز (Noise). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:824]

```
825:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:825]

```
826:     fun sendFilePrivate(recipientPeerID: String, file: com.bitchat.android.model.BitchatFilePacket) {
```
> تُعرَّف دالة باسم إرسال-ملف-خاص (sendFilePrivate) تأخذ معطى مُعرّف-نِدّ-المُستقبِل (recipientPeerID) من نوع سلسلة، ومعطى «ملف» (file) من نوع حزمة-ملف-بِت-شات (BitchatFilePacket)، بفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:826]

```
827:         try {
```
> فتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:827]

```
828:             Log.d(TAG, "📤 sendFilePrivate (ENCRYPTED): to=$recipientPeerID, name=${file.fileName}, size=${file.fileSize}")
```
> تُستدعى دالة التسجيل بمستوى التصحيح (Log.d) مُمرَّراً إليها الوسم ونصاً يحوي مُعرّف نِدّ المُستقبِل واسم الملف وحجم الملف. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:828]

```
829:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:829]

```
830:             serviceScope.launch {
```
> تُستدعى الدالة إطلاق (launch) على نطاق-الخدمة (serviceScope) بفتح كتلة مُعاملِها (lambda). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:830]

```
831:                 // Check if we have an established Noise session
```
> تعليق: تحقّق مما إذا كان لدينا جلسة نويز مُؤسَّسة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:831]

```
832:                 if (encryptionService.hasEstablishedSession(recipientPeerID)) {
```
> شرط إذا (if): إن أعادت الدالة لديه-جلسة-مُؤسَّسة (hasEstablishedSession) على خدمة-التشفير (encryptionService) لمُعرّف نِدّ المُستقبِل قيمة صحيحة، بفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:832]

```
833:                     try {
```
> فتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:833]

```
834:                         // Encode the file packet as TLV
```
> تعليق: رمِّز حزمة الملف بصيغة طول-قيمة-نوع (TLV). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:834]

```
835:                         val filePayload = file.encode()
```
> يُعرَّف متغيّر ثابت باسم «حمولة-الملف» (filePayload) ويُسنَد إليه ناتج استدعاء الدالة ترميز (encode) على «ملف». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:835]

```
836:                         if (filePayload == null) {
```
> شرط إذا (if): إن كانت حمولة-الملف تساوي القيمة الفارغة (null)، بفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:836]

```
837:                             Log.e(TAG, "❌ Failed to encode file packet for private send")
```
> تُستدعى دالة التسجيل بمستوى الخطأ (Log.e) مُمرَّراً إليها الوسم ونصاً: فشل ترميز حزمة الملف للإرسال الخاص. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:837]

```
838:                             return@launch
```
> يُنفَّذ خروج (return) مُعلَّماً للكتلة إطلاق (launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:838]

```
839:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:839]

```
840:                         Log.d(TAG, "📦 Encoded file TLV: ${filePayload.size} bytes")
```
> تُستدعى دالة التسجيل بمستوى التصحيح (Log.d) مُمرَّراً إليها الوسم ونصاً يحوي حجم حمولة-الملف بالبايتات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:840]

```
841:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:841]

```
842:                         // Create NoisePayload wrapper (type byte + file TLV data) - same as iOS
```
> تعليق: أنشئ غلاف حمولة-نويز (NoisePayload) المُكوَّن من بايت النوع مع بيانات الملف بصيغة TLV، مماثلاً لنظام آي-أو-إس (iOS). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:842]

```
843:                         val noisePayload = com.bitchat.android.model.NoisePayload(
```
> يُعرَّف متغيّر ثابت باسم «حمولة-نويز» (noisePayload) ويُسنَد إليه إنشاء كائن من نوع حمولة-نويز (NoisePayload) بفتح قائمة المعطيات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:843]

```
844:                             type = com.bitchat.android.model.NoisePayloadType.FILE_TRANSFER,
```
> يُضبَط معطى النوع (type) إلى العنصر نقل-الملف (FILE_TRANSFER) من نوع-حمولة-نويز (NoisePayloadType). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:844]

```
845:                             data = filePayload
```
> يُضبَط معطى البيانات (data) إلى حمولة-الملف (filePayload). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:845]

```
846:                         )
```
> إغلاق قائمة معطيات إنشاء كائن حمولة-نويز. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:846]

```
847:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:847]

```
848:                         // Encrypt the payload using Noise
```
> تعليق: شفّر الحمولة باستعمال نويز. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:848]

```
849:                         val encrypted = encryptionService.encrypt(noisePayload.encode(), recipientPeerID)
```
> يُعرَّف متغيّر ثابت باسم «مُشفَّر» (encrypted) ويُسنَد إليه ناتج استدعاء الدالة تشفير (encrypt) على خدمة-التشفير مُمرَّراً إليها ناتج ترميز حمولة-نويز ومُعرّف نِدّ المُستقبِل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:849]

```
850:                         if (encrypted == null) {
```
> شرط إذا (if): إن كان «مُشفَّر» يساوي القيمة الفارغة (null)، بفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:850]

```
851:                             Log.e(TAG, "❌ Failed to encrypt file for $recipientPeerID")
```
> تُستدعى دالة التسجيل بمستوى الخطأ (Log.e) مُمرَّراً إليها الوسم ونصاً: فشل تشفير الملف لمُعرّف نِدّ المُستقبِل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:851]

```
852:                             return@launch
```
> يُنفَّذ خروج (return) مُعلَّماً للكتلة إطلاق (launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:852]

```
853:                         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:853]

```
854:                         Log.d(TAG, "🔐 Encrypted file payload: ${encrypted.size} bytes")
```
> تُستدعى دالة التسجيل بمستوى التصحيح (Log.d) مُمرَّراً إليها الوسم ونصاً يحوي حجم «مُشفَّر» بالبايتات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:854]

```
855:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:855]

```
856:                         // Create NOISE_ENCRYPTED packet (not FILE_TRANSFER!)
```
> تعليق: أنشئ حزمة مُشفَّرة-بنويز (NOISE_ENCRYPTED) وليست نقل-ملف (FILE_TRANSFER). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:856]

```
857:                         val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت باسم «حزمة» (packet) ويُسنَد إليه إنشاء كائن من نوع حزمة بِت-شات (BitchatPacket) بفتح قائمة المعطيات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:857]

```
858:                             version = if (encrypted.size > 0xFFFF) 2u else 1u,
```
> يُضبَط معطى الإصدار (version) إلى 2u إن كان حجم «مُشفَّر» أكبر من القيمة الست-عشرية 0xFFFF، وإلا إلى 1u. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:858]

```
859:                             type = MessageType.NOISE_ENCRYPTED.value,
```
> يُضبَط معطى النوع (type) إلى قيمة العنصر مُشفَّر-بنويز (NOISE_ENCRYPTED) من تعداد نوع الرسالة (MessageType). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:859]

```
860:                             senderID = hexStringToByteArray(myPeerID),
```
> يُضبَط معطى مُعرّف المُرسِل (senderID) إلى ناتج تحويل مُعرّف-نِدّي (myPeerID) من سلسلة ست-عشرية إلى مصفوفة بايت. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:860]

```
861:                             recipientID = hexStringToByteArray(recipientPeerID),
```
> يُضبَط معطى مُعرّف المُستقبِل (recipientID) إلى ناتج تحويل مُعرّف نِدّ المُستقبِل من سلسلة ست-عشرية إلى مصفوفة بايت. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:861]

```
862:                             timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط معطى الطابع-الزمني (timestamp) إلى الوقت الحالي بالمللي ثانية من النظام مُحوَّلاً إلى عدد طويل غير مُوقَّع. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:862]

```
863:                             payload = encrypted,
```
> يُضبَط معطى الحمولة (payload) إلى المتغيّر «مُشفَّر» (encrypted). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:863]

```
864:                             signature = null,
```
> يُضبَط معطى التوقيع (signature) إلى القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:864]

```
865:                             ttl = com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS
```
> يُضبَط معطى مدّة-البقاء (ttl) إلى الثابت مدّة-بقاء-الرسالة-بالقفزات (MESSAGE_TTL_HOPS) من ثوابت-التطبيق (AppConstants). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:865]

```
866:                         )
```
> إغلاق قائمة معطيات إنشاء كائن الحزمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:866]

```
867:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:867]

```
868:                         // Sign and send the encrypted packet
```
> تعليق: وقّع وأرسِل الحزمة المُشفَّرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:868]

```
869:                         val signed = signPacketBeforeBroadcast(packet)
```
> يُعرَّف متغيّر ثابت باسم «مُوقَّع» (signed) ويُسنَد إليه ناتج استدعاء الدالة توقيع-الحزمة-قبل-البث (signPacketBeforeBroadcast) مُمرَّراً إليها الحزمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:869]

```
870:                         // Use a stable transferId based on the unencrypted file TLV payload for progress tracking
```
> تعليق: استعمل مُعرّف نقل ثابتاً مبنيّاً على حمولة الملف غير المُشفَّرة بصيغة TLV لتتبّع التقدّم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:870]

```
871:                         val transferId = sha256Hex(filePayload)
```
> يُعرَّف متغيّر ثابت باسم «مُعرّف-النقل» (transferId) ويُسنَد إليه ناتج استدعاء الدالة بصمة-سها-256-ست-عشرية (sha256Hex) مُمرَّراً إليها حمولة-الملف (filePayload). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:871]

```
872:                         broadcastRoutedPacket(RoutedPacket(signed, transferId = transferId))
```
> تُستدعى الدالة بثّ-الحزمة-المُوجَّهة (broadcastRoutedPacket) مُمرَّراً إليها كائن حزمة-مُوجَّهة (RoutedPacket) مُنشأ من «المُوقَّع» ومُعرّف-النقل مضبوطاً إلى متغيّر مُعرّف-النقل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:872]

```
873:                         Log.d(TAG, "✅ Sent encrypted file to $recipientPeerID")
```
> تُستدعى دالة التسجيل بمستوى التصحيح (Log.d) مُمرَّراً إليها الوسم ونصاً: أُرسِل الملف المُشفَّر إلى مُعرّف نِدّ المُستقبِل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:873]

```
874:                         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:874]

```
875:                     } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وفتح كتلة التقاط (catch) لاستثناء (Exception) مُسمّى «e». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:875]

```
876:                         Log.e(TAG, "❌ Failed to encrypt file for $recipientPeerID: ${e.message}", e)
```
> تُستدعى دالة التسجيل بمستوى الخطأ (Log.e) مُمرَّراً إليها الوسم ونصاً: فشل تشفير الملف لمُعرّف نِدّ المُستقبِل مع رسالة الاستثناء، والاستثناء «e». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:876]

```
877:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:877]

```
878:                 } else {
```
> إغلاق كتلة الشرط وفتح كتلة وإلا (else). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:878]

```
879:                     // No session - initiate handshake but don't queue file
```
> تعليق: لا توجد جلسة — ابدأ المصافحة لكن لا تضع الملف في الطابور. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:879]

```
880:                     Log.w(TAG, "⚠️ No Noise session with $recipientPeerID for file transfer, initiating handshake")
```
> تُستدعى دالة التسجيل بمستوى التحذير (Log.w) مُمرَّراً إليها الوسم ونصاً: لا جلسة نويز مع مُعرّف نِدّ المُستقبِل لنقل الملف، بدء المصافحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:880]

```
881:                     messageHandler.delegate?.initiateNoiseHandshake(recipientPeerID)
```
> تُستدعى الدالة بدء-مصافحة-نويز (initiateNoiseHandshake) على المُفوَّض (delegate) لِمُعالِج-الرسائل (messageHandler) باستدعاء آمن من الفراغ مُمرَّراً إليها مُعرّف نِدّ المُستقبِل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:881]

```
882:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:882]

```
883:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:883]

```
884:         } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وفتح كتلة التقاط (catch) لاستثناء (Exception) مُسمّى «e». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:884]

```
885:             Log.e(TAG, "❌ sendFilePrivate failed: ${e.message}", e)
```
> تُستدعى دالة التسجيل بمستوى الخطأ (Log.e) مُمرَّراً إليها الوسم ونصاً: فشل إرسال-ملف-خاص مع رسالة الاستثناء، والاستثناء «e». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:885]

```
886:             Log.e(TAG, "❌ File: to=$recipientPeerID, name=${file.fileName}, size=${file.fileSize}")
```
> تُستدعى دالة التسجيل بمستوى الخطأ (Log.e) مُمرَّراً إليها الوسم ونصاً يحوي مُعرّف نِدّ المُستقبِل واسم الملف وحجم الملف. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:886]

```
887:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:887]

```
888:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:888]

```
889: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:889]

```
890:     fun cancelFileTransfer(transferId: String): Boolean {
```
> تُعرَّف دالة باسم إلغاء-نقل-الملف (cancelFileTransfer) تأخذ معطى مُعرّف-النقل (transferId) من نوع سلسلة وتُعيد قيمة منطقية (Boolean)، بفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:890]

```
891:         return connectionManager.cancelTransfer(transferId)
```
> يُعاد ناتج استدعاء الدالة إلغاء-النقل (cancelTransfer) على مُدير-الاتصال (connectionManager) مُمرَّراً إليها مُعرّف-النقل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:891]

```
892:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:892]

```
893: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:893]

```
894:     // Local helper to hash payloads to a stable hex ID for progress mapping
```
> تعليق: مساعِد محلّي لتجزئة الحمولات إلى مُعرّف ست-عشري ثابت لربط التقدّم. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:894]

```
895:     private fun sha256Hex(bytes: ByteArray): String = try {
```
> تُعرَّف دالة خاصة باسم بصمة-سها-256-ست-عشرية (sha256Hex) تأخذ معطى «بايتات» (bytes) من نوع مصفوفة بايت وتُعيد سلسلة، وجسمها تعبير يساوي كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:895]

```
896:         val md = java.security.MessageDigest.getInstance("SHA-256")
```
> يُعرَّف متغيّر ثابت باسم «md» ويُسنَد إليه نسخة من مُلخِّص-الرسالة (MessageDigest) عبر الدالة الحصول-على-نسخة (getInstance) للخوارزمية «SHA-256». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:896]

```
897:         md.update(bytes)
```
> تُستدعى الدالة تحديث (update) على «md» مُمرَّراً إليها «بايتات» (bytes). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:897]

```
898:         md.digest().joinToString("") { "%02x".format(it) }
```
> يُحسب التلخيص بالدالة هضم (digest) على «md»، ثم تُدمَج بايتاته في سلسلة بلا فاصل عبر دمج-في-سلسلة (joinToString)، حيث يُنسَّق كل عنصر بصيغة ست-عشرية بخانتين «%02x». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:898]

```
899:     } catch (_: Exception) { bytes.size.toString(16) }
```
> إغلاق كتلة المحاولة وكتلة التقاط (catch) لاستثناء مُهمَل الاسم تُعيد حجم «بايتات» مُحوَّلاً إلى سلسلة بالأساس 16. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:899]

```
900:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:900]

```
901:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:901]

```
902:      * Send private message - SIMPLIFIED iOS-compatible version 
```
> تعليق: أرسِل رسالة خاصة — نسخة مُبسَّطة مُتوافقة مع آي-أو-إس (iOS). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:902]

```
903:      * Uses NoisePayloadType system exactly like iOS SimplifiedBluetoothService
```
> تعليق: تستعمل نظام نوع-حمولة-نويز (NoisePayloadType) تماماً مثل خدمة-بلوتوث-المُبسَّطة (SimplifiedBluetoothService) في آي-أو-إس. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:903]

```
904:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:904]

```
905:     fun sendPrivateMessage(content: String, recipientPeerID: String, recipientNickname: String, messageID: String? = null) {
```
> تُعرَّف دالة باسم إرسال-رسالة-خاصة (sendPrivateMessage) تأخذ معطى «محتوى» (content) سلسلة، ومُعرّف نِدّ المُستقبِل سلسلة، وكُنية-المُستقبِل (recipientNickname) سلسلة، ومُعرّف-الرسالة (messageID) سلسلة قابلة للفراغ بقيمة افتراضية فارغة (null)، بفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:905]

```
906:         if (content.isEmpty() || recipientPeerID.isEmpty()) return
```
> شرط إذا (if): إن كان «محتوى» فارغاً أو مُعرّف نِدّ المُستقبِل فارغاً، يُنفَّذ خروج (return). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:906]

```
907:         if (recipientNickname.isEmpty()) return
```
> شرط إذا (if): إن كانت كُنية-المُستقبِل فارغة، يُنفَّذ خروج (return). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:907]

```
908:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:908]

```
909:         serviceScope.launch {
```
> تُستدعى الدالة إطلاق (launch) على نطاق-الخدمة (serviceScope) بفتح كتلة مُعاملِها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:909]

```
910:             val finalMessageID = messageID ?: java.util.UUID.randomUUID().toString()
```
> يُعرَّف متغيّر ثابت باسم «مُعرّف-الرسالة-النهائي» (finalMessageID) ويُسنَد إليه مُعرّف-الرسالة إن لم يكن فارغاً، وإلا مُعرّف عالمي فريد (UUID) عشوائي مُحوَّل إلى سلسلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:910]

```
911:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:911]

```
912:             Log.d(TAG, "📨 Sending PM to $recipientPeerID: ${content.take(30)}...")
```
> تُستدعى دالة التسجيل بمستوى التصحيح (Log.d) مُمرَّراً إليها الوسم ونصاً: إرسال رسالة خاصة إلى مُعرّف نِدّ المُستقبِل مع أوّل ثلاثين محرفاً من «محتوى». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:912]

```
913:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:913]

```
914:             // Check if we have an established Noise session
```
> تعليق: تحقّق مما إذا كان لدينا جلسة نويز مُؤسَّسة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:914]

```
915:             if (encryptionService.hasEstablishedSession(recipientPeerID)) {
```
> شرط إذا (if): إن أعادت الدالة لديه-جلسة-مُؤسَّسة (hasEstablishedSession) على خدمة-التشفير لمُعرّف نِدّ المُستقبِل قيمة صحيحة، بفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:915]

```
916:                 try {
```
> فتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:916]

```
917:                     // Create TLV-encoded private message exactly like iOS
```
> تعليق: أنشئ رسالة خاصة مُرمَّزة بصيغة TLV تماماً مثل آي-أو-إس. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:917]

```
918:                     val privateMessage = com.bitchat.android.model.PrivateMessagePacket(
```
> يُعرَّف متغيّر ثابت باسم «الرسالة-الخاصة» (privateMessage) ويُسنَد إليه إنشاء كائن من نوع حزمة-رسالة-خاصة (PrivateMessagePacket) بفتح قائمة المعطيات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:918]

```
919:                         messageID = finalMessageID,
```
> يُضبَط معطى مُعرّف-الرسالة (messageID) إلى مُعرّف-الرسالة-النهائي (finalMessageID). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:919]

```
920:                         content = content
```
> يُضبَط معطى المحتوى (content) إلى متغيّر «محتوى» (content). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:920]

```
921:                     )
```
> إغلاق قائمة معطيات إنشاء كائن الرسالة-الخاصة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:921]

```
922:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:922]

```
923:                     val tlvData = privateMessage.encode()
```
> يُعرَّف متغيّر ثابت باسم «بيانات-تي-إل-في» (tlvData) ويُسنَد إليه ناتج استدعاء الدالة ترميز (encode) على الرسالة-الخاصة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:923]

```
924:                     if (tlvData == null) {
```
> شرط إذا (if): إن كانت بيانات-تي-إل-في تساوي القيمة الفارغة (null)، بفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:924]

```
925:                         Log.e(TAG, "Failed to encode private message with TLV")
```
> تُستدعى دالة التسجيل بمستوى الخطأ (Log.e) مُمرَّراً إليها الوسم ونصاً: فشل ترميز الرسالة الخاصة بصيغة TLV. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:925]

```
926:                         return@launch
```
> يُنفَّذ خروج (return) مُعلَّماً للكتلة إطلاق (launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:926]

```
927:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:927]

```
928:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:928]

```
929:                     // Create message payload with NoisePayloadType prefix: [type byte] + [TLV data]
```
> تعليق: أنشئ حمولة الرسالة مع بادئة نوع-حمولة-نويز (NoisePayloadType): بايت النوع مع بيانات TLV. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:929]

```
930:                     val messagePayload = com.bitchat.android.model.NoisePayload(
```
> يُعرَّف متغيّر ثابت باسم «حمولة-الرسالة» (messagePayload) ويُسنَد إليه إنشاء كائن من نوع حمولة-نويز (NoisePayload) بفتح قائمة المعطيات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:930]

```
931:                         type = com.bitchat.android.model.NoisePayloadType.PRIVATE_MESSAGE,
```
> يُضبَط معطى النوع (type) إلى العنصر رسالة-خاصة (PRIVATE_MESSAGE) من نوع-حمولة-نويز (NoisePayloadType). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:931]

```
932:                         data = tlvData
```
> يُضبَط معطى البيانات (data) إلى بيانات-تي-إل-في (tlvData). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:932]

```
933:                     )
```
> إغلاق قائمة معطيات إنشاء كائن حمولة-الرسالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:933]

```
934:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:934]

```
935:                     // Encrypt the payload
```
> تعليق: شفّر الحمولة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:935]

```
936:                     val encrypted = encryptionService.encrypt(messagePayload.encode(), recipientPeerID)
```
> يُعرَّف متغيّر ثابت باسم «مُشفَّر» (encrypted) ويُسنَد إليه ناتج استدعاء الدالة تشفير (encrypt) على خدمة-التشفير مُمرَّراً إليها ناتج ترميز حمولة-الرسالة ومُعرّف نِدّ المُستقبِل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:936]

```
937:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:937]

```
938:                     // Create NOISE_ENCRYPTED packet exactly like iOS
```
> تعليق: أنشئ حزمة مُشفَّرة-بنويز (NOISE_ENCRYPTED) تماماً مثل آي-أو-إس. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:938]

```
939:                     val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت باسم «حزمة» (packet) ويُسنَد إليه إنشاء كائن من نوع حزمة بِت-شات (BitchatPacket) بفتح قائمة المعطيات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:939]

```
940:                         version = 1u,
```
> يُضبَط معطى الإصدار (version) إلى القيمة العددية غير المُوقَّعة 1u. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:940]

```
941:                         type = MessageType.NOISE_ENCRYPTED.value,
```
> يُضبَط معطى النوع (type) إلى قيمة العنصر مُشفَّر-بنويز (NOISE_ENCRYPTED) من تعداد نوع الرسالة (MessageType). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:941]

```
942:                         senderID = hexStringToByteArray(myPeerID),
```
> يُضبَط معطى مُعرّف المُرسِل (senderID) إلى ناتج تحويل مُعرّف-نِدّي (myPeerID) من سلسلة ست-عشرية إلى مصفوفة بايت. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:942]

```
943:                         recipientID = hexStringToByteArray(recipientPeerID),
```
> يُضبَط معطى مُعرّف المُستقبِل (recipientID) إلى ناتج تحويل مُعرّف نِدّ المُستقبِل من سلسلة ست-عشرية إلى مصفوفة بايت. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:943]

```
944:                         timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط معطى الطابع-الزمني (timestamp) إلى الوقت الحالي بالمللي ثانية من النظام مُحوَّلاً إلى عدد طويل غير مُوقَّع. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:944]

```
945:                         payload = encrypted,
```
> يُضبَط معطى الحمولة (payload) إلى المتغيّر «مُشفَّر» (encrypted). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:945]

```
946:                         signature = null,
```
> يُضبَط معطى التوقيع (signature) إلى القيمة الفارغة (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:946]

```
947:                         ttl = MAX_TTL
```
> يُضبَط معطى مدّة-البقاء (ttl) إلى الثابت أقصى-مدّة-بقاء (MAX_TTL). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:947]

```
948:                     )
```
> إغلاق قائمة معطيات إنشاء كائن الحزمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:948]

```
949:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:949]

```
950:                     // Sign the packet before broadcasting
```
> تعليق: وقّع الحزمة قبل البث. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:950]

```
951:                     val signedPacket = signPacketBeforeBroadcast(packet)
```
> يُعرَّف متغيّر ثابت باسم «الحزمة-المُوقَّعة» (signedPacket) ويُسنَد إليه ناتج استدعاء الدالة توقيع-الحزمة-قبل-البث (signPacketBeforeBroadcast) مُمرَّراً إليها الحزمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:951]

```
952:                     broadcastRoutedPacket(RoutedPacket(signedPacket))
```
> تُستدعى الدالة بثّ-الحزمة-المُوجَّهة (broadcastRoutedPacket) مُمرَّراً إليها كائن حزمة-مُوجَّهة (RoutedPacket) مُنشأ من الحزمة-المُوقَّعة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:952]

```
953:                     Log.d(TAG, "📤 Sent encrypted private message to $recipientPeerID (${encrypted.size} bytes)")
```
> تُستدعى دالة التسجيل بمستوى التصحيح (Log.d) مُمرَّراً إليها الوسم ونصاً: أُرسِلت الرسالة الخاصة المُشفَّرة إلى مُعرّف نِدّ المُستقبِل مع حجم «مُشفَّر» بالبايتات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:953]

```
954:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:954]

```
955:                     // FIXED: Don't send didReceiveMessage for our own sent messages
```
> تعليق: مُصحَّح — لا تُرسِل تمّ-استلام-الرسالة (didReceiveMessage) لرسائلنا المُرسَلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:955]

```
956:                     // This was causing self-notifications - iOS doesn't do this
```
> تعليق: كان هذا يُسبّب إشعارات ذاتية — آي-أو-إس لا يفعل هذا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:956]

```
957:                     // The UI handles showing sent messages through its own message sending logic
```
> تعليق: واجهة المستخدم تتولّى عرض الرسائل المُرسَلة عبر منطق إرسال الرسائل الخاص بها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:957]

```
958:                     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:958]

```
959:                 } catch (e: Exception) {
```
> إغلاق كتلة المحاولة وفتح كتلة التقاط (catch) لاستثناء (Exception) مُسمّى «e». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:959]

```
960:                     Log.e(TAG, "Failed to encrypt private message for $recipientPeerID: ${e.message}")
```
> تُستدعى دالة التسجيل بمستوى الخطأ (Log.e) مُمرَّراً إليها الوسم ونصاً: فشل تشفير الرسالة الخاصة لمُعرّف نِدّ المُستقبِل مع رسالة الاستثناء. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:960]

```
961:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:961]

```
962:             } else {
```
> إغلاق كتلة الشرط وفتح كتلة وإلا (else). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:962]

```
963:                 // Fire and forget - initiate handshake but don't queue exactly like iOS
```
> تعليق: أطلِق وانسَ — ابدأ المصافحة لكن لا تضع في الطابور تماماً مثل آي-أو-إس. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:963]

```
964:                 Log.d(TAG, "🤝 No session with $recipientPeerID, initiating handshake")
```
> تُستدعى دالة التسجيل بمستوى التصحيح (Log.d) مُمرَّراً إليها الوسم ونصاً: لا جلسة مع مُعرّف نِدّ المُستقبِل، بدء المصافحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:964]

```
965:                 messageHandler.delegate?.initiateNoiseHandshake(recipientPeerID)
```
> تُستدعى الدالة بدء-مصافحة-نويز (initiateNoiseHandshake) على المُفوَّض (delegate) لِمُعالِج-الرسائل (messageHandler) باستدعاء آمن من الفراغ مُمرَّراً إليها مُعرّف نِدّ المُستقبِل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:965]

```
966:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:966]

```
967:                 // FIXED: Don't send didReceiveMessage for our own sent messages
```
> تعليق: مُصحَّح — لا تُرسِل تمّ-استلام-الرسالة (didReceiveMessage) لرسائلنا المُرسَلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:967]

```
968:                 // The UI will handle showing the message in the chat interface
```
> تعليق: واجهة المستخدم ستتولّى عرض الرسالة في واجهة المحادثة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:968]

```
969:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:969]

```
970:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:970]

```
971:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:971]

```
972:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:972]

```
973:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:973]

```
974:      * Send read receipt for a received private message - NEW NoisePayloadType implementation
```
> تعليق: أرسِل إيصال-قراءة لرسالة خاصة مُستلَمة — تنفيذ جديد بنوع-حمولة-نويز (NoisePayloadType). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:974]

```
975:      * Uses same encryption approach as iOS SimplifiedBluetoothService
```
> تعليق: تستعمل نفس منهج التشفير المُتَّبع في خدمة-بلوتوث-المُبسَّطة (SimplifiedBluetoothService) في آي-أو-إس. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:975]

```
976:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:976]

```
977:     fun sendReadReceipt(messageID: String, recipientPeerID: String, readerNickname: String) {
```
> تُعرَّف دالة باسم إرسال-إيصال-القراءة (sendReadReceipt) تأخذ معطى مُعرّف-الرسالة (messageID) سلسلة، ومُعرّف نِدّ المُستقبِل سلسلة، وكُنية-القارئ (readerNickname) سلسلة، بفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:977]

```
978:         serviceScope.launch {
```
> تُستدعى الدالة إطلاق (launch) على نطاق-الخدمة (serviceScope) بفتح كتلة مُعاملِها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:978]

```
979:             Log.d(TAG, "📖 Sending read receipt for message $messageID to $recipientPeerID")
```
> تُستدعى دالة التسجيل بمستوى التصحيح (Log.d) مُمرَّراً إليها الوسم ونصاً: إرسال إيصال قراءة للرسالة ذات مُعرّف-الرسالة إلى مُعرّف نِدّ المُستقبِل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:979]

```
980: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:980]

```
981:             // Route geohash read receipts via MessageRouter instead of here
```
> تعليق: وجِّه إيصالات قراءة الجيوهاش (geohash) عبر مُوجِّه-الرسائل (MessageRouter) بدلاً من هنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:981]

```
982:             val geo = runCatching { com.bitchat.android.services.MessageRouter.tryGetInstance() }.getOrNull()
```
> يُعرَّف متغيّر ثابت باسم «جيو» (geo) ويُسنَد إليه ناتج كتلة تشغيل-مع-التقاط (runCatching) التي تستدعي محاولة-الحصول-على-نسخة (tryGetInstance) من مُوجِّه-الرسائل، مُعيداً القيمة عند النجاح أو الفارغة (null) عند الفشل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:982]

```
983:             val isGeoAlias = try {
```
> يُعرَّف متغيّر ثابت باسم «أهو-اسم-مُستعار-جيو» (isGeoAlias) ويُسنَد إليه تعبير كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:983]

```
984:                 val map = com.bitchat.android.nostr.GeohashAliasRegistry.snapshot()
```
> يُعرَّف متغيّر ثابت باسم «خريطة» (map) ويُسنَد إليه ناتج استدعاء الدالة لقطة (snapshot) على سجلّ-أسماء-الجيوهاش-المُستعارة (GeohashAliasRegistry). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:984]

```
985:                 map.containsKey(recipientPeerID)
```
> تُستدعى الدالة يحتوي-المفتاح (containsKey) على «خريطة» مُمرَّراً إليها مُعرّف نِدّ المُستقبِل، وتُعاد نتيجتها قيمةً للكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:985]

```
986:             } catch (_: Exception) { false }
```
> إغلاق كتلة المحاولة وكتلة التقاط (catch) لاستثناء مُهمَل الاسم تُعيد القيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:986]

```
987:             if (isGeoAlias && geo != null) {
```
> شرط إذا (if): إن كان «أهو-اسم-مُستعار-جيو» صحيحاً و«جيو» ليس فارغاً، بفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:987]

```
988:                 geo.sendReadReceipt(com.bitchat.android.model.ReadReceipt(messageID), recipientPeerID)
```
> تُستدعى الدالة إرسال-إيصال-القراءة (sendReadReceipt) على «جيو» مُمرَّراً إليها كائن إيصال-قراءة (ReadReceipt) مُنشأ من مُعرّف-الرسالة، ومُعرّف نِدّ المُستقبِل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:988]

```
989:                 return@launch
```
> يُنفَّذ خروج (return) مُعلَّماً للكتلة إطلاق (launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:989]

```
990:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:990]

```
991: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:991]

```
992:             try {
```
> فتح كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:992]

```
993:                 // Avoid duplicate read receipts: check persistent store first
```
> تعليق: تجنّب إيصالات القراءة المُكرَّرة: تحقّق من المخزن الدائم أولاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:993]

```
994:                 val seenStore = try { com.bitchat.android.services.SeenMessageStore.getInstance(context.applicationContext) } catch (_: Exception) { null }
```
> يُعرَّف متغيّر ثابت باسم «مخزن-المرئيّ» (seenStore) ويُسنَد إليه ضمن كتلة محاولة (try) نسخة من مخزن-الرسائل-المرئيّة (SeenMessageStore) عبر الحصول-على-نسخة مُمرَّراً سياق-التطبيق (applicationContext)، أو القيمة الفارغة (null) عند الاستثناء. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:994]

```
995:                 if (seenStore?.hasRead(messageID) == true) {
```
> شرط إذا (if): إن أعادت الدالة هل-قُرِئت (hasRead) على «مخزن-المرئيّ» باستدعاء آمن من الفراغ لمُعرّف-الرسالة قيمة صحيحة (true)، بفتح الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:995]

```
996:                     Log.d(TAG, "Skipping read receipt for $messageID - already marked read")
```
> تُستدعى دالة التسجيل بمستوى التصحيح (Log.d) مُمرَّراً إليها الوسم ونصاً: تخطّي إيصال القراءة لمُعرّف-الرسالة — مُعلَّمة كمقروءة سلفاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:996]

```
997:                     return@launch
```
> يُنفَّذ خروج (return) مُعلَّماً للكتلة إطلاق (launch). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:997]

```
998:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:998]

```
999: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:999]

```
1000:                 // Create read receipt payload using NoisePayloadType exactly like iOS
```
> تعليق: أنشئ حمولة إيصال القراءة باستعمال نوع-حمولة-نويز (NoisePayloadType) تماماً مثل آي-أو-إس. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1000]
