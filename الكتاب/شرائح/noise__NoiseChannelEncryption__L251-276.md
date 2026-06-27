# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt (الأسطر 251–276)

```
251:         appendLine("=== Channel Encryption Debug ===")
```
> يستدعي الدالة «أضِف سطراً» (appendLine) داخل بانية النص (buildString) ليُلحق السطر النصّي الحرفي «=== Channel Encryption Debug ===» بنصّ معلومات التنقيح. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:251]

```
252:         appendLine("Active channels: ${channelKeys.size}")
```
> يستدعي «أضِف سطراً» (appendLine) ليُلحق سطراً نصّياً يبدأ بـ«Active channels: » متبوعاً بقيمة حجم خريطة مفاتيح القنوات (channelKeys.size) أي عدد عناصرها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:252]

```
253:         
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:253]

```
254:         channelKeys.keys.forEach { channel ->
```
> يمرّ على مفاتيح خريطة مفاتيح القنوات (channelKeys.keys) عنصراً عنصراً بالدالة «لكلّ عنصر» (forEach)، ويسمّي كلّ عنصر «قناة» (channel). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:254]

```
255:             val hasPassword = channelPasswords.containsKey(channel)
```
> يعرّف متغيّراً ثابتاً «لها كلمة سرّ» (hasPassword) ويسند إليه نتيجة استدعاء «هل يحوي المفتاح» (containsKey) على خريطة كلمات سرّ القنوات (channelPasswords) للقناة الحالية، وهي قيمة منطقية. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:255]

```
256:             val commitment = calculateKeyCommitment(channel)?.take(16)
```
> يعرّف متغيّراً ثابتاً «الالتزام» (commitment) ويسند إليه نتيجة استدعاء الدالة «احسب التزام المفتاح» (calculateKeyCommitment) للقناة الحالية، ثم يأخذ أوّل ١٦ محرفاً منها بالدالة «خُذ» (take) باستعمال الاستدعاء الآمن (?.) فيكون ناتجه فارغاً (null) إن كانت النتيجة فارغة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:256]

```
257:             appendLine("  $channel: hasPassword=$hasPassword, commitment=${commitment}...")
```
> يستدعي «أضِف سطراً» (appendLine) ليُلحق سطراً يحوي مسافتين ثم قيمة القناة (channel) ثم «: hasPassword=» متبوعاً بقيمة «لها كلمة سرّ» (hasPassword) ثم «, commitment=» متبوعاً بقيمة «الالتزام» (commitment) ثم ثلاث نقاط «...». [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:257]

```
258:         }
```
> إغلاق نطاق كتلة الدالة «لكلّ عنصر» (forEach) التي تمرّ على القنوات. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:258]

```
259:     }
```
> إغلاق نطاق بانية النص (buildString) وجسم الدالة «احصل على معلومات التنقيح» (getDebugInfo). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:259]

```
260:     
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:260]

```
261:     /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي (Javadoc/KDoc) بالرمز «/**». [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:261]

```
262:      * Get list of channels with keys
```
> تعليق: «احصل على قائمة القنوات التي لها مفاتيح». [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:262]

```
263:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي بالرمز «*/». [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:263]

```
264:     fun getActiveChannels(): Set<String> {
```
> يعرّف الدالة «احصل على القنوات النشطة» (getActiveChannels) التي لا تأخذ وسائط وتُعيد نوع «مجموعة من السلاسل النصّية» (Set<String>). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:264]

```
265:         return channelKeys.keys.toSet()
```
> يُعيد مفاتيح خريطة مفاتيح القنوات (channelKeys.keys) بعد تحويلها إلى مجموعة بالدالة «إلى مجموعة» (toSet). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:265]

```
266:     }
```
> إغلاق نطاق جسم الدالة «احصل على القنوات النشطة» (getActiveChannels). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:266]

```
267:     
```
> سطر فارغ (يحوي مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:267]

```
268:     /**
```
> تعليق توثيقي: بداية كتلة تعليق توثيقي بالرمز «/**». [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:268]

```
269:      * Clear all channel data
```
> تعليق: «امسح كلّ بيانات القنوات». [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:269]

```
270:      */
```
> تعليق: نهاية كتلة التعليق التوثيقي بالرمز «*/». [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:270]

```
271:     fun clear() {
```
> يعرّف الدالة «امسح» (clear) التي لا تأخذ وسائط ولا تُعيد قيمة. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:271]

```
272:         channelKeys.clear()
```
> يستدعي الدالة «امسح» (clear) على خريطة مفاتيح القنوات (channelKeys) لإزالة كلّ عناصرها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:272]

```
273:         channelPasswords.clear()
```
> يستدعي الدالة «امسح» (clear) على خريطة كلمات سرّ القنوات (channelPasswords) لإزالة كلّ عناصرها. [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:273]

```
274:         Log.d(TAG, "Cleared all channel encryption data")
```
> يستدعي دالة التسجيل التشخيصي «Log.d» بالوسم (TAG) والرسالة النصّية الحرفية «Cleared all channel encryption data». [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:274]

```
275:     }
```
> إغلاق نطاق جسم الدالة «امسح» (clear). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:275]

```
276: }
```
> إغلاق نطاق الصنف «تشفير قنوات نويز» (NoiseChannelEncryption). [app/src/main/java/com/bitchat/android/noise/NoiseChannelEncryption.kt:276]
