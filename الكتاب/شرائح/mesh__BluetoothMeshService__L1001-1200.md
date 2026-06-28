# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt (الأسطر 1001–1200)

```
1001:                 val readReceiptPayload = com.bitchat.android.model.NoisePayload(
```
> يُعرَّف متغيّر ثابت باسم «حمولة إيصال القراءة» (readReceiptPayload) ويُسنَد إليه كائن من النوع NoisePayload (حمولة نويز) يبدأ استدعاء بانيه هنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1001]

```
1002:                     type = com.bitchat.android.model.NoisePayloadType.READ_RECEIPT,
```
> يُضبَط الوسيط المسمّى type (النوع) على القيمة READ_RECEIPT (إيصال القراءة) من تعداد NoisePayloadType. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1002]

```
1003:                     data = messageID.toByteArray(Charsets.UTF_8)
```
> يُضبَط الوسيط المسمّى data (البيانات) على مصفوفة بايتات ناتجة من تحويل messageID (معرّف الرسالة) بترميز UTF_8. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1003]

```
1004:                 )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1004]

```
1005:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1005]

```
1006:                 // Encrypt the payload
```
> تعليق: شفّر الحمولة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1006]

```
1007:                 val encrypted = encryptionService.encrypt(readReceiptPayload.encode(), recipientPeerID)
```
> يُعرَّف متغيّر ثابت باسم encrypted (المشفّر) ويُسنَد إليه ناتج استدعاء encrypt (تشفير) من encryptionService (خدمة التشفير) مع تمرير ترميز readReceiptPayload عبر encode ومعرّف القرين المستقبِل recipientPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1007]

```
1008:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1008]

```
1009:                 // Create NOISE_ENCRYPTED packet exactly like iOS
```
> تعليق: أنشئ حزمة NOISE_ENCRYPTED تماماً مثل iOS. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1009]

```
1010:                 val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت باسم packet (الحزمة) ويُسنَد إليه كائن من النوع BitchatPacket (حزمة بِتشات) يبدأ استدعاء بانيه هنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1010]

```
1011:                     version = 1u,
```
> يُضبَط الوسيط المسمّى version (الإصدار) على القيمة 1u (واحد عددٌ صحيح بلا إشارة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1011]

```
1012:                     type = MessageType.NOISE_ENCRYPTED.value,
```
> يُضبَط الوسيط المسمّى type (النوع) على القيمة value من العنصر NOISE_ENCRYPTED ضمن تعداد MessageType (نوع الرسالة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1012]

```
1013:                     senderID = hexStringToByteArray(myPeerID),
```
> يُضبَط الوسيط المسمّى senderID (معرّف المرسِل) على ناتج استدعاء hexStringToByteArray (تحويل نص ست عشري إلى مصفوفة بايتات) مع تمرير myPeerID (معرّف قريني). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1013]

```
1014:                     recipientID = hexStringToByteArray(recipientPeerID),
```
> يُضبَط الوسيط المسمّى recipientID (معرّف المستقبِل) على ناتج استدعاء hexStringToByteArray مع تمرير recipientPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1014]

```
1015:                     timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط الوسيط المسمّى timestamp (الطابع الزمني) على الوقت الحالي بالميلّي ثانية من System.currentTimeMillis محوّلاً إلى ULong (عدد طويل بلا إشارة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1015]

```
1016:                     payload = encrypted,
```
> يُضبَط الوسيط المسمّى payload (الحمولة) على قيمة المتغيّر encrypted. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1016]

```
1017:                     signature = null,
```
> يُضبَط الوسيط المسمّى signature (التوقيع) على القيمة null (لا شيء). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1017]

```
1018:                     ttl = com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS // Same TTL as iOS messageTTL
```
> يُضبَط الوسيط المسمّى ttl (مدّة البقاء) على القيمة MESSAGE_TTL_HOPS من AppConstants (ثوابت التطبيق)، يتبعه تعليق: نفس مدّة البقاء كما في messageTTL في iOS. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1018]

```
1019:                 )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1019]

```
1020:                 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1020]

```
1021:                 // Sign the packet before broadcasting
```
> تعليق: وقّع الحزمة قبل البثّ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1021]

```
1022:                 val signedPacket = signPacketBeforeBroadcast(packet)
```
> يُعرَّف متغيّر ثابت باسم signedPacket (الحزمة الموقّعة) ويُسنَد إليه ناتج استدعاء signPacketBeforeBroadcast (توقيع الحزمة قبل البثّ) مع تمرير packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1022]

```
1023:                 broadcastRoutedPacket(RoutedPacket(signedPacket))
```
> يُستدعى broadcastRoutedPacket (بثّ الحزمة الموجّهة) مع تمرير كائن RoutedPacket (حزمة موجّهة) مبنيّ من signedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1023]

```
1024:                 Log.d(TAG, "📤 Sent read receipt to $recipientPeerID for message $messageID")
```
> يُستدعى Log.d (سجلّ تصحيح) مع الوسم TAG ونصّ: «أُرسِل إيصال قراءة إلى recipientPeerID للرسالة messageID». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1024]

```
1025:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1025]

```
1026:                 // Persist as read after successful send
```
> تعليق: احفظ كمقروء بعد الإرسال الناجح. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1026]

```
1027:                 try { seenStore?.markRead(messageID) } catch (_: Exception) { }
```
> داخل كتلة try يُستدعى markRead (تعليم كمقروء) على seenStore (مخزن المُشاهَد) إن لم يكن null مع تمرير messageID، وكتلة catch تلتقط أيّ استثناء Exception وتتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1027]

```
1028:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1028]

```
1029:             } catch (e: Exception) {
```
> إغلاق كتلة try وبداية كتلة catch تلتقط استثناءً Exception باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1029]

```
1030:                 Log.e(TAG, "Failed to send read receipt to $recipientPeerID: ${e.message}")
```
> يُستدعى Log.e (سجلّ خطأ) مع الوسم TAG ونصّ: «فشل إرسال إيصال القراءة إلى recipientPeerID» متبوعاً برسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1030]

```
1031:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1031]

```
1032:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1032]

```
1033:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1033]

```
1034:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1034]

```
1035:     // MARK: QR Verification over Noise
```
> تعليق: علامة قسم: تحقّق رمز QR عبر نويز. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1035]

```
1036:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1036]

```
1037:     fun sendVerifyChallenge(peerID: String, noiseKeyHex: String, nonceA: ByteArray) {
```
> تُعرَّف دالة باسم sendVerifyChallenge (إرسال تحدّي التحقّق) تستقبل peerID (معرّف القرين) نصّاً وnoiseKeyHex (مفتاح نويز ست عشري) نصّاً وnonceA (الرقم المرّة A) مصفوفة بايتات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1037]

```
1038:         val tlv = VerificationService.buildVerifyChallenge(noiseKeyHex, nonceA)
```
> يُعرَّف متغيّر ثابت باسم tlv ويُسنَد إليه ناتج استدعاء buildVerifyChallenge (بناء تحدّي التحقّق) من VerificationService (خدمة التحقّق) مع تمرير noiseKeyHex وnonceA. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1038]

```
1039:         val payload = NoisePayload(
```
> يُعرَّف متغيّر ثابت باسم payload (الحمولة) ويُسنَد إليه كائن NoisePayload يبدأ استدعاء بانيه هنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1039]

```
1040:             type = NoisePayloadType.VERIFY_CHALLENGE,
```
> يُضبَط الوسيط type على القيمة VERIFY_CHALLENGE (تحدّي التحقّق) من تعداد NoisePayloadType. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1040]

```
1041:             data = tlv
```
> يُضبَط الوسيط data على قيمة المتغيّر tlv. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1041]

```
1042:         )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1042]

```
1043:         sendNoisePayloadToPeer(payload, peerID, "verify challenge")
```
> يُستدعى sendNoisePayloadToPeer (إرسال حمولة نويز إلى قرين) مع تمرير payload وpeerID والنصّ «verify challenge». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1043]

```
1044:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1044]

```
1045:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1045]

```
1046:     fun sendVerifyResponse(peerID: String, noiseKeyHex: String, nonceA: ByteArray) {
```
> تُعرَّف دالة باسم sendVerifyResponse (إرسال ردّ التحقّق) تستقبل peerID نصّاً وnoiseKeyHex نصّاً وnonceA مصفوفة بايتات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1046]

```
1047:         val tlv = VerificationService.buildVerifyResponse(noiseKeyHex, nonceA) ?: return
```
> يُعرَّف متغيّر ثابت باسم tlv ويُسنَد إليه ناتج buildVerifyResponse (بناء ردّ التحقّق) من VerificationService مع تمرير noiseKeyHex وnonceA، وإن كان null يُنفَّذ return (خروج من الدالة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1047]

```
1048:         val payload = NoisePayload(
```
> يُعرَّف متغيّر ثابت باسم payload ويُسنَد إليه كائن NoisePayload يبدأ استدعاء بانيه هنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1048]

```
1049:             type = NoisePayloadType.VERIFY_RESPONSE,
```
> يُضبَط الوسيط type على القيمة VERIFY_RESPONSE (ردّ التحقّق) من تعداد NoisePayloadType. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1049]

```
1050:             data = tlv
```
> يُضبَط الوسيط data على قيمة المتغيّر tlv. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1050]

```
1051:         )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1051]

```
1052:         sendNoisePayloadToPeer(payload, peerID, "verify response")
```
> يُستدعى sendNoisePayloadToPeer مع تمرير payload وpeerID والنصّ «verify response». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1052]

```
1053:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1053]

```
1054:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1054]

```
1055:     private fun sendNoisePayloadToPeer(payload: NoisePayload, recipientPeerID: String, label: String) {
```
> تُعرَّف دالة خاصّة (private) باسم sendNoisePayloadToPeer تستقبل payload من النوع NoisePayload وrecipientPeerID نصّاً وlabel (التسمية) نصّاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1055]

```
1056:         serviceScope.launch {
```
> يُستدعى launch (إطلاق) على serviceScope (نطاق الخدمة) لبدء كتلة برمجية متزامنة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1056]

```
1057:             try {
```
> بداية كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1057]

```
1058:                 val encrypted = encryptionService.encrypt(payload.encode(), recipientPeerID)
```
> يُعرَّف متغيّر ثابت باسم encrypted ويُسنَد إليه ناتج encrypt من encryptionService مع تمرير ترميز payload عبر encode وrecipientPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1058]

```
1059:                 val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت باسم packet ويُسنَد إليه كائن BitchatPacket يبدأ استدعاء بانيه هنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1059]

```
1060:                     version = 1u,
```
> يُضبَط الوسيط version على القيمة 1u. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1060]

```
1061:                     type = MessageType.NOISE_ENCRYPTED.value,
```
> يُضبَط الوسيط type على القيمة value من العنصر NOISE_ENCRYPTED ضمن تعداد MessageType. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1061]

```
1062:                     senderID = hexStringToByteArray(myPeerID),
```
> يُضبَط الوسيط senderID على ناتج hexStringToByteArray مع تمرير myPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1062]

```
1063:                     recipientID = hexStringToByteArray(recipientPeerID),
```
> يُضبَط الوسيط recipientID على ناتج hexStringToByteArray مع تمرير recipientPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1063]

```
1064:                     timestamp = System.currentTimeMillis().toULong(),
```
> يُضبَط الوسيط timestamp على الوقت الحالي بالميلّي ثانية محوّلاً إلى ULong. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1064]

```
1065:                     payload = encrypted,
```
> يُضبَط الوسيط payload على قيمة المتغيّر encrypted. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1065]

```
1066:                     signature = null,
```
> يُضبَط الوسيط signature على القيمة null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1066]

```
1067:                     ttl = com.bitchat.android.util.AppConstants.MESSAGE_TTL_HOPS
```
> يُضبَط الوسيط ttl على القيمة MESSAGE_TTL_HOPS من AppConstants. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1067]

```
1068:                 )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1068]

```
1069:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1069]

```
1070:                 val signedPacket = signPacketBeforeBroadcast(packet)
```
> يُعرَّف متغيّر ثابت باسم signedPacket ويُسنَد إليه ناتج signPacketBeforeBroadcast مع تمرير packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1070]

```
1071:                 broadcastRoutedPacket(RoutedPacket(signedPacket))
```
> يُستدعى broadcastRoutedPacket مع تمرير كائن RoutedPacket مبنيّ من signedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1071]

```
1072:                 Log.d(TAG, "📤 Sent $label to $recipientPeerID (${payload.data.size} bytes)")
```
> يُستدعى Log.d مع الوسم TAG ونصّ: «أُرسِل label إلى recipientPeerID» يتبعه حجم payload.data بالبايتات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1072]

```
1073:             } catch (e: Exception) {
```
> إغلاق كتلة try وبداية كتلة catch تلتقط استثناءً Exception باسم e. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1073]

```
1074:                 Log.e(TAG, "Failed to send $label to $recipientPeerID: ${e.message}")
```
> يُستدعى Log.e مع الوسم TAG ونصّ: «فشل إرسال label إلى recipientPeerID» متبوعاً برسالة الاستثناء e.message. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1074]

```
1075:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1075]

```
1076:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1076]

```
1077:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1077]

```
1078:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1078]

```
1079:     /**
```
> بداية تعليق توثيقي (كتلة KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1079]

```
1080:      * Send broadcast announce with TLV-encoded identity announcement - exactly like iOS
```
> تعليق: أرسِل إعلان بثّ مع إعلان هويّة مُرمَّز بصيغة TLV — تماماً مثل iOS. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1080]

```
1081:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1081]

```
1082:     fun sendBroadcastAnnounce() {
```
> تُعرَّف دالة عامّة باسم sendBroadcastAnnounce (إرسال إعلان البثّ) بلا وُسطاء. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1082]

```
1083:         Log.d(TAG, "Sending broadcast announce")
```
> يُستدعى Log.d مع الوسم TAG ونصّ: «جارٍ إرسال إعلان البثّ». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1083]

```
1084:         serviceScope.launch {
```
> يُستدعى launch على serviceScope لبدء كتلة برمجية متزامنة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1084]

```
1085:             val nickname = try { com.bitchat.android.services.NicknameProvider.getNickname(context, myPeerID) } catch (_: Exception) { myPeerID }
```
> يُعرَّف متغيّر ثابت باسم nickname (الاسم المستعار) ويُسنَد إليه ناتج getNickname (جلب الاسم المستعار) من NicknameProvider (موفّر الاسم المستعار) مع تمرير context وmyPeerID داخل try، وإن وقع استثناء يُسنَد myPeerID بدلاً منه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1085]

```
1086:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1086]

```
1087:             // Get the static public key for the announcement
```
> تعليق: احصل على المفتاح العامّ الثابت للإعلان. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1087]

```
1088:             val staticKey = encryptionService.getStaticPublicKey()
```
> يُعرَّف متغيّر ثابت باسم staticKey (المفتاح الثابت) ويُسنَد إليه ناتج getStaticPublicKey (جلب المفتاح العامّ الثابت) من encryptionService. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1088]

```
1089:             if (staticKey == null) {
```
> شرط: إذا كان staticKey يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1089]

```
1090:                 Log.e(TAG, "No static public key available for announcement")
```
> يُستدعى Log.e مع الوسم TAG ونصّ: «لا يوجد مفتاح عامّ ثابت متاح للإعلان». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1090]

```
1091:                 return@launch
```
> يُنفَّذ return@launch (خروج من كتلة الإطلاق). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1091]

```
1092:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1092]

```
1093:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1093]

```
1094:             // Get the signing public key for the announcement
```
> تعليق: احصل على المفتاح العامّ للتوقيع للإعلان. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1094]

```
1095:             val signingKey = encryptionService.getSigningPublicKey()
```
> يُعرَّف متغيّر ثابت باسم signingKey (مفتاح التوقيع) ويُسنَد إليه ناتج getSigningPublicKey (جلب المفتاح العامّ للتوقيع) من encryptionService. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1095]

```
1096:             if (signingKey == null) {
```
> شرط: إذا كان signingKey يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1096]

```
1097:                 Log.e(TAG, "No signing public key available for announcement")
```
> يُستدعى Log.e مع الوسم TAG ونصّ: «لا يوجد مفتاح عامّ للتوقيع متاح للإعلان». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1097]

```
1098:                 return@launch
```
> يُنفَّذ return@launch (خروج من كتلة الإطلاق). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1098]

```
1099:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1099]

```
1100:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1100]

```
1101:             // Create iOS-compatible IdentityAnnouncement with TLV encoding
```
> تعليق: أنشئ IdentityAnnouncement متوافقاً مع iOS بترميز TLV. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1101]

```
1102:             val announcement = IdentityAnnouncement(nickname, staticKey, signingKey)
```
> يُعرَّف متغيّر ثابت باسم announcement (الإعلان) ويُسنَد إليه كائن IdentityAnnouncement (إعلان الهويّة) مبنيّ من nickname وstaticKey وsigningKey. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1102]

```
1103:             var tlvPayload = announcement.encode()
```
> يُعرَّف متغيّر متغيّر القيمة باسم tlvPayload (حمولة TLV) ويُسنَد إليه ناتج encode على announcement. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1103]

```
1104:             if (tlvPayload == null) {
```
> شرط: إذا كان tlvPayload يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1104]

```
1105:                 Log.e(TAG, "Failed to encode announcement as TLV")
```
> يُستدعى Log.e مع الوسم TAG ونصّ: «فشل ترميز الإعلان بصيغة TLV». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1105]

```
1106:                 return@launch
```
> يُنفَّذ return@launch (خروج من كتلة الإطلاق). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1106]

```
1107:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1107]

```
1108:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1108]

```
1109:             // Append gossip TLV containing up to 10 direct neighbors (compact IDs)
```
> تعليق: ألحِق TLV الإشاعة (gossip) متضمّناً حتى 10 جيران مباشرين (معرّفات مُختصَرة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1109]

```
1110:             try {
```
> بداية كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1110]

```
1111:                 val directPeers = getDirectPeerIDsForGossip()
```
> يُعرَّف متغيّر ثابت باسم directPeers (القرناء المباشرون) ويُسنَد إليه ناتج getDirectPeerIDsForGossip (جلب معرّفات القرناء المباشرين للإشاعة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1111]

```
1112:                 if (directPeers.isNotEmpty()) {
```
> شرط: إذا كانت directPeers غير فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1112]

```
1113:                     val gossip = com.bitchat.android.services.meshgraph.GossipTLV.encodeNeighbors(directPeers)
```
> يُعرَّف متغيّر ثابت باسم gossip (الإشاعة) ويُسنَد إليه ناتج encodeNeighbors (ترميز الجيران) من GossipTLV مع تمرير directPeers. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1113]

```
1114:                     tlvPayload = tlvPayload + gossip
```
> يُسنَد إلى tlvPayload ناتج دمج tlvPayload مع gossip. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1114]

```
1115:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1115]

```
1116:                 // Always update our own node in the mesh graph with the neighbor list we used
```
> تعليق: حدّث دائماً عقدتنا في رسم الشبكة المتشابكة (mesh graph) بقائمة الجيران التي استعملناها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1116]

```
1117:                 try {
```
> بداية كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1117]

```
1118:                     com.bitchat.android.services.meshgraph.MeshGraphService.getInstance()
```
> يُستدعى getInstance (جلب النسخة المفردة) من MeshGraphService (خدمة رسم الشبكة المتشابكة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1118]

```
1119:                         .updateFromAnnouncement(myPeerID, nickname, directPeers, System.currentTimeMillis().toULong())
```
> يُستدعى updateFromAnnouncement (التحديث من الإعلان) مع تمرير myPeerID وnickname وdirectPeers والوقت الحالي بالميلّي ثانية محوّلاً إلى ULong. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1119]

```
1120:                 } catch (_: Exception) { }
```
> إغلاق كتلة try وكتلة catch تلتقط أيّ استثناء Exception وتتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1120]

```
1121:             } catch (_: Exception) { }
```
> إغلاق كتلة try الخارجية وكتلة catch تلتقط أيّ استثناء Exception وتتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1121]

```
1122:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1122]

```
1123:             val announcePacket = BitchatPacket(
```
> يُعرَّف متغيّر ثابت باسم announcePacket (حزمة الإعلان) ويُسنَد إليه كائن BitchatPacket يبدأ استدعاء بانيه هنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1123]

```
1124:                 type = MessageType.ANNOUNCE.value,
```
> يُضبَط الوسيط type على القيمة value من العنصر ANNOUNCE (إعلان) ضمن تعداد MessageType. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1124]

```
1125:                 ttl = MAX_TTL,
```
> يُضبَط الوسيط ttl على القيمة MAX_TTL (أقصى مدّة بقاء). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1125]

```
1126:                 senderID = myPeerID,
```
> يُضبَط الوسيط senderID على myPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1126]

```
1127:                 payload = tlvPayload
```
> يُضبَط الوسيط payload على قيمة tlvPayload. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1127]

```
1128:             )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1128]

```
1129:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1129]

```
1130:             // Sign the packet using our signing key (exactly like iOS)
```
> تعليق: وقّع الحزمة باستعمال مفتاح التوقيع الخاصّ بنا (تماماً مثل iOS). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1130]

```
1131:             val signedPacket = encryptionService.signData(announcePacket.toBinaryDataForSigning()!!)?.let { signature ->
```
> يُعرَّف متغيّر ثابت باسم signedPacket ويُسنَد إليه ناتج استدعاء signData (توقيع البيانات) من encryptionService مع تمرير toBinaryDataForSigning (التحويل إلى بيانات ثنائية للتوقيع) على announcePacket مع تأكيد عدم العدم (!!)، ثم تطبيق let على الناتج بمعامل باسم signature. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1131]

```
1132:                 announcePacket.copy(signature = signature)
```
> يُستدعى copy (نسخ) على announcePacket مع ضبط signature على المعامل signature. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1132]

```
1133:             } ?: announcePacket
```
> إغلاق كتلة let، وإن كان الناتج null يُسنَد announcePacket الأصلي بدلاً منه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1133]

```
1134:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1134]

```
1135:             broadcastRoutedPacket(RoutedPacket(signedPacket))
```
> يُستدعى broadcastRoutedPacket مع تمرير كائن RoutedPacket مبنيّ من signedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1135]

```
1136:             Log.d(TAG, "Sent iOS-compatible signed TLV announce (${tlvPayload.size} bytes)")
```
> يُستدعى Log.d مع الوسم TAG ونصّ: «أُرسِل إعلان TLV موقّع متوافق مع iOS» يتبعه حجم tlvPayload بالبايتات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1136]

```
1137:             // Track announce for sync
```
> تعليق: تتبّع الإعلان لأجل المزامنة (sync). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1137]

```
1138:             try { gossipSyncManager.onPublicPacketSeen(signedPacket) } catch (_: Exception) { }
```
> داخل كتلة try يُستدعى onPublicPacketSeen (عند مشاهدة حزمة عامّة) على gossipSyncManager (مدير مزامنة الإشاعة) مع تمرير signedPacket، وكتلة catch تلتقط أيّ استثناء Exception وتتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1138]

```
1139:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1139]

```
1140:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1140]

```
1141:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1141]

```
1142:     /**
```
> بداية تعليق توثيقي (كتلة KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1142]

```
1143:      * Send announcement to specific peer with TLV-encoded identity announcement - exactly like iOS
```
> تعليق: أرسِل إعلاناً إلى قرين محدّد مع إعلان هويّة مُرمَّز بصيغة TLV — تماماً مثل iOS. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1143]

```
1144:      */
```
> إغلاق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1144]

```
1145:     fun sendAnnouncementToPeer(peerID: String) {
```
> تُعرَّف دالة عامّة باسم sendAnnouncementToPeer (إرسال الإعلان إلى قرين) تستقبل peerID نصّاً. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1145]

```
1146:         if (peerManager.hasAnnouncedToPeer(peerID)) return
```
> شرط: إذا أرجعت hasAnnouncedToPeer (هل أُعلِن إلى القرين) على peerManager (مدير القرناء) قيمة صحيحة لـ peerID يُنفَّذ return (خروج من الدالة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1146]

```
1147:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1147]

```
1148:         val nickname = try { com.bitchat.android.services.NicknameProvider.getNickname(context, myPeerID) } catch (_: Exception) { myPeerID }
```
> يُعرَّف متغيّر ثابت باسم nickname ويُسنَد إليه ناتج getNickname من NicknameProvider مع تمرير context وmyPeerID داخل try، وإن وقع استثناء يُسنَد myPeerID بدلاً منه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1148]

```
1149:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1149]

```
1150:         // Get the static public key for the announcement
```
> تعليق: احصل على المفتاح العامّ الثابت للإعلان. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1150]

```
1151:         val staticKey = encryptionService.getStaticPublicKey()
```
> يُعرَّف متغيّر ثابت باسم staticKey ويُسنَد إليه ناتج getStaticPublicKey من encryptionService. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1151]

```
1152:         if (staticKey == null) {
```
> شرط: إذا كان staticKey يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1152]

```
1153:             Log.e(TAG, "No static public key available for peer announcement")
```
> يُستدعى Log.e مع الوسم TAG ونصّ: «لا يوجد مفتاح عامّ ثابت متاح لإعلان القرين». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1153]

```
1154:             return
```
> يُنفَّذ return (خروج من الدالة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1154]

```
1155:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1155]

```
1156:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1156]

```
1157:         // Get the signing public key for the announcement
```
> تعليق: احصل على المفتاح العامّ للتوقيع للإعلان. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1157]

```
1158:         val signingKey = encryptionService.getSigningPublicKey()
```
> يُعرَّف متغيّر ثابت باسم signingKey ويُسنَد إليه ناتج getSigningPublicKey من encryptionService. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1158]

```
1159:         if (signingKey == null) {
```
> شرط: إذا كان signingKey يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1159]

```
1160:             Log.e(TAG, "No signing public key available for peer announcement")
```
> يُستدعى Log.e مع الوسم TAG ونصّ: «لا يوجد مفتاح عامّ للتوقيع متاح لإعلان القرين». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1160]

```
1161:             return
```
> يُنفَّذ return (خروج من الدالة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1161]

```
1162:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1162]

```
1163:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1163]

```
1164:         // Create iOS-compatible IdentityAnnouncement with TLV encoding
```
> تعليق: أنشئ IdentityAnnouncement متوافقاً مع iOS بترميز TLV. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1164]

```
1165:         val announcement = IdentityAnnouncement(nickname, staticKey, signingKey)
```
> يُعرَّف متغيّر ثابت باسم announcement ويُسنَد إليه كائن IdentityAnnouncement مبنيّ من nickname وstaticKey وsigningKey. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1165]

```
1166:         var tlvPayload = announcement.encode()
```
> يُعرَّف متغيّر متغيّر القيمة باسم tlvPayload ويُسنَد إليه ناتج encode على announcement. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1166]

```
1167:         if (tlvPayload == null) {
```
> شرط: إذا كان tlvPayload يساوي null. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1167]

```
1168:             Log.e(TAG, "Failed to encode peer announcement as TLV")
```
> يُستدعى Log.e مع الوسم TAG ونصّ: «فشل ترميز إعلان القرين بصيغة TLV». [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1168]

```
1169:             return
```
> يُنفَّذ return (خروج من الدالة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1169]

```
1170:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1170]

```
1171:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1171]

```
1172:         // Append gossip TLV containing up to 10 direct neighbors (compact IDs)
```
> تعليق: ألحِق TLV الإشاعة متضمّناً حتى 10 جيران مباشرين (معرّفات مُختصَرة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1172]

```
1173:         try {
```
> بداية كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1173]

```
1174:             val directPeers = getDirectPeerIDsForGossip()
```
> يُعرَّف متغيّر ثابت باسم directPeers ويُسنَد إليه ناتج getDirectPeerIDsForGossip. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1174]

```
1175:             if (directPeers.isNotEmpty()) {
```
> شرط: إذا كانت directPeers غير فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1175]

```
1176:                 val gossip = com.bitchat.android.services.meshgraph.GossipTLV.encodeNeighbors(directPeers)
```
> يُعرَّف متغيّر ثابت باسم gossip ويُسنَد إليه ناتج encodeNeighbors من GossipTLV مع تمرير directPeers. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1176]

```
1177:                 tlvPayload = tlvPayload + gossip
```
> يُسنَد إلى tlvPayload ناتج دمج tlvPayload مع gossip. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1177]

```
1178:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1178]

```
1179:             // Always update our own node in the mesh graph with the neighbor list we used
```
> تعليق: حدّث دائماً عقدتنا في رسم الشبكة المتشابكة بقائمة الجيران التي استعملناها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1179]

```
1180:             try {
```
> بداية كتلة try. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1180]

```
1181:                 com.bitchat.android.services.meshgraph.MeshGraphService.getInstance()
```
> يُستدعى getInstance من MeshGraphService. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1181]

```
1182:                     .updateFromAnnouncement(myPeerID, nickname, directPeers, System.currentTimeMillis().toULong())
```
> يُستدعى updateFromAnnouncement مع تمرير myPeerID وnickname وdirectPeers والوقت الحالي بالميلّي ثانية محوّلاً إلى ULong. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1182]

```
1183:             } catch (_: Exception) { }
```
> إغلاق كتلة try وكتلة catch تلتقط أيّ استثناء Exception وتتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1183]

```
1184:         } catch (_: Exception) { }
```
> إغلاق كتلة try الخارجية وكتلة catch تلتقط أيّ استثناء Exception وتتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1184]

```
1185:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1185]

```
1186:         val packet = BitchatPacket(
```
> يُعرَّف متغيّر ثابت باسم packet ويُسنَد إليه كائن BitchatPacket يبدأ استدعاء بانيه هنا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1186]

```
1187:             type = MessageType.ANNOUNCE.value,
```
> يُضبَط الوسيط type على القيمة value من العنصر ANNOUNCE ضمن تعداد MessageType. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1187]

```
1188:             ttl = MAX_TTL,
```
> يُضبَط الوسيط ttl على القيمة MAX_TTL. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1188]

```
1189:             senderID = myPeerID,
```
> يُضبَط الوسيط senderID على myPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1189]

```
1190:             payload = tlvPayload
```
> يُضبَط الوسيط payload على قيمة tlvPayload. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1190]

```
1191:         )
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1191]

```
1192:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1192]

```
1193:         // Sign the packet using our signing key (exactly like iOS)
```
> تعليق: وقّع الحزمة باستعمال مفتاح التوقيع الخاصّ بنا (تماماً مثل iOS). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1193]

```
1194:         val signedPacket = encryptionService.signData(packet.toBinaryDataForSigning()!!)?.let { signature ->
```
> يُعرَّف متغيّر ثابت باسم signedPacket ويُسنَد إليه ناتج signData من encryptionService مع تمرير toBinaryDataForSigning على packet مع تأكيد عدم العدم (!!)، ثم تطبيق let على الناتج بمعامل باسم signature. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1194]

```
1195:             packet.copy(signature = signature)
```
> يُستدعى copy على packet مع ضبط signature على المعامل signature. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1195]

```
1196:         } ?: packet
```
> إغلاق كتلة let، وإن كان الناتج null يُسنَد packet الأصلي بدلاً منه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1196]

```
1197:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1197]

```
1198:         broadcastRoutedPacket(RoutedPacket(signedPacket))
```
> يُستدعى broadcastRoutedPacket مع تمرير كائن RoutedPacket مبنيّ من signedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1198]

```
1199:         peerManager.markPeerAsAnnouncedTo(peerID)
```
> يُستدعى markPeerAsAnnouncedTo (تعليم القرين كمُعلَن إليه) على peerManager مع تمرير peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1199]

```
1200:         Log.d(TAG, "Sent iOS-compatible signed TLV peer announce to $peerID (${tlvPayload.size} bytes)")
```
> يُستدعى Log.d مع الوسم TAG ونصّ: «أُرسِل إعلان قرين TLV موقّع متوافق مع iOS إلى peerID» يتبعه حجم tlvPayload بالبايتات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:1200]
