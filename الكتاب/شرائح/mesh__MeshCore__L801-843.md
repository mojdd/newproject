# شريحة — app/src/main/java/com/bitchat/android/mesh/MeshCore.kt (الأسطر 801–843)

```
801:         peerManager.clearAllPeers()
```
> يُستدعى التابع «امسح كل الأقران» (clearAllPeers) على مدير الأقران (peerManager). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:801]

```
802:         peerManager.clearAllFingerprints()
```
> يُستدعى التابع «امسح كل البصمات» (clearAllFingerprints) على مدير الأقران (peerManager). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:802]

```
803:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:803]

```
804: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:804]

```
805:     fun clearAllEncryptionData() {
```
> تُعرَّف دالة عامة باسم «امسح كل بيانات التشفير» (clearAllEncryptionData) بلا وُسطاء وبلا نوع عائد مُصرَّح. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:805]

```
806:         encryptionService.clearPersistentIdentity()
```
> يُستدعى التابع «امسح الهوية الدائمة» (clearPersistentIdentity) على خدمة التشفير (encryptionService). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:806]

```
807:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:807]

```
808: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:808]

```
809:     private fun signPacketBeforeBroadcast(packet: BitchatPacket): BitchatPacket {
```
> تُعرَّف دالة خاصة باسم «وقّع الحزمة قبل البث» (signPacketBeforeBroadcast) تأخذ وسيطاً واحداً اسمه «الحزمة» (packet) من نوع حزمة بِت‌شات (BitchatPacket) وتُعيد قيمة من نوع حزمة بِت‌شات (BitchatPacket). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:809]

```
810:         return try {
```
> تُعاد قيمة كتلة «حاوِل» (try) التي تبدأ هنا. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:810]

```
811:             val withRoute = try {
```
> يُعرَّف متغيّر ثابت باسم «مع المسار» (withRoute) تُسنَد إليه قيمة كتلة «حاوِل» (try) داخلية تبدأ هنا. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:811]

```
812:                 val recipient = packet.recipientID
```
> يُعرَّف متغيّر ثابت باسم «المستلِم» (recipient) تُسنَد إليه قيمة الخاصية «معرّف المستلِم» (recipientID) من الحزمة (packet). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:812]

```
813:                 if (recipient != null && !recipient.contentEquals(SpecialRecipients.BROADCAST)) {
```
> شرط: إذا كان «المستلِم» (recipient) ليس فارغاً (null) وفي الوقت نفسه محتواه لا يساوي قيمة «البث» (BROADCAST) من «المستلِمون الخاصون» (SpecialRecipients). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:813]

```
814:                     val destination = recipient.toHexString()
```
> يُعرَّف متغيّر ثابت باسم «الوجهة» (destination) تُسنَد إليه نتيجة التابع «إلى نص ست‌عشري» (toHexString) المُستدعى على «المستلِم» (recipient). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:814]

```
815:                     val path = com.bitchat.android.services.meshgraph.RoutePlanner.shortestPath(myPeerID, destination)
```
> يُعرَّف متغيّر ثابت باسم «المسار» (path) تُسنَد إليه نتيجة التابع «أقصر مسار» (shortestPath) من «مخطّط المسار» (RoutePlanner) في الحزمة com.bitchat.android.services.meshgraph، مُمرَّراً إليه «معرّف قريني» (myPeerID) و«الوجهة» (destination). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:815]

```
816:                     if (path != null && path.size >= 3) {
```
> شرط: إذا كان «المسار» (path) ليس فارغاً (null) وفي الوقت نفسه عدد عناصره (size) أكبر من أو يساوي ثلاثة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:816]

```
817:                         val intermediates = path.subList(1, path.size - 1)
```
> يُعرَّف متغيّر ثابت باسم «الوسطاء» (intermediates) تُسنَد إليه قائمة فرعية (subList) من «المسار» (path) من المؤشّر واحد حتى المؤشّر «عدد العناصر ناقص واحد» غير شامل. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:817]

```
818:                         packet.copy(
```
> يُستدعى التابع «انسخ» (copy) على «الحزمة» (packet) مع تمرير وُسطاء مُسمّاة تبدأ هنا. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:818]

```
819:                             route = intermediates.map { MeshPacketUtils.hexStringToByteArray(it) },
```
> يُسنَد للوسيط «المسار» (route) نتيجة تحويل (map) كل عنصر من «الوسطاء» (intermediates) عبر التابع «نص ست‌عشري إلى مصفوفة بايت» (hexStringToByteArray) من «أدوات حزمة الشبكة» (MeshPacketUtils). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:819]

```
820:                             version = 2u
```
> يُسنَد للوسيط «الإصدار» (version) القيمة الصحيحة غير المُوقَّعة اثنان (2u). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:820]

```
821:                         )
```
> إغلاق قائمة وُسطاء استدعاء التابع «انسخ» (copy). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:821]

```
822:                     } else {
```
> فرع «وإلّا» (else) المقابل للشرط في السطر 816. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:822]

```
823:                         packet.copy(route = null)
```
> يُستدعى التابع «انسخ» (copy) على «الحزمة» (packet) مع إسناد القيمة الفارغة (null) للوسيط «المسار» (route). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:823]

```
824:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:824]

```
825:                 } else {
```
> فرع «وإلّا» (else) المقابل للشرط في السطر 813. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:825]

```
826:                     packet
```
> تُعطى قيمة «الحزمة» (packet) كنتيجة لهذا الفرع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:826]

```
827:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:827]

```
828:             } catch (_: Exception) {
```
> كتلة «التقاط» (catch) تلتقط استثناءً (Exception) من نوع عام بمتغيّر مُهمَل (_). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:828]

```
829:                 packet
```
> تُعطى قيمة «الحزمة» (packet) كنتيجة لكتلة الالتقاط. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:829]

```
830:             }
```
> إغلاق نطاق كتلة «حاوِل/التقاط» (try/catch) الداخلية المُسنَدة إلى «مع المسار» (withRoute). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:830]

```
831: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:831]

```
832:             val packetDataForSigning = withRoute.toBinaryDataForSigning() ?: return withRoute
```
> يُعرَّف متغيّر ثابت باسم «بيانات الحزمة للتوقيع» (packetDataForSigning) تُسنَد إليه نتيجة التابع «إلى بيانات ثنائية للتوقيع» (toBinaryDataForSigning) المُستدعى على «مع المسار» (withRoute)، وإن كانت فارغة (null) تُعاد «مع المسار» (withRoute) من الدالة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:832]

```
833:             val signature = encryptionService.signData(packetDataForSigning)
```
> يُعرَّف متغيّر ثابت باسم «التوقيع» (signature) تُسنَد إليه نتيجة التابع «وقّع البيانات» (signData) المُستدعى على خدمة التشفير (encryptionService) مع تمرير «بيانات الحزمة للتوقيع» (packetDataForSigning). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:833]

```
834:             if (signature != null) {
```
> شرط: إذا كان «التوقيع» (signature) ليس فارغاً (null). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:834]

```
835:                 withRoute.copy(signature = signature)
```
> يُستدعى التابع «انسخ» (copy) على «مع المسار» (withRoute) مع إسناد قيمة «التوقيع» (signature) للوسيط «التوقيع» (signature). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:835]

```
836:             } else {
```
> فرع «وإلّا» (else) المقابل للشرط في السطر 834. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:836]

```
837:                 withRoute
```
> تُعطى قيمة «مع المسار» (withRoute) كنتيجة لهذا الفرع. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:837]

```
838:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:838]

```
839:         } catch (_: Exception) {
```
> كتلة «التقاط» (catch) تلتقط استثناءً (Exception) من نوع عام بمتغيّر مُهمَل (_) للكتلة الخارجية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:839]

```
840:             packet
```
> تُعطى قيمة «الحزمة» (packet) كنتيجة لكتلة الالتقاط الخارجية. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:840]

```
841:         }
```
> إغلاق نطاق كتلة «حاوِل/التقاط» (try/catch) الخارجية المُعادة من الدالة. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:841]

```
842:     }
```
> إغلاق نطاق دالة «وقّع الحزمة قبل البث» (signPacketBeforeBroadcast). [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:842]

```
843: }
```
> إغلاق نطاق الصنف (class) الحاوي. [app/src/main/java/com/bitchat/android/mesh/MeshCore.kt:843]
