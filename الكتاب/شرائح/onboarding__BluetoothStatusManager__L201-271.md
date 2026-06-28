# شريحة — app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt (الأسطر 201–271)

```
201:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:201]

```
202: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:202]

```
203:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:203]

```
204:      * Log current Bluetooth status for debugging
```
> تعليق: سجّل حالة البلوتوث الحالية لغرض التصحيح. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:204]

```
205:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:205]

```
206:     fun logBluetoothStatus() {
```
> تُعرَّف دالة باسم «تسجيل حالة البلوتوث» (logBluetoothStatus) بلا وُسطاء وبلا نوع إرجاع مُصرَّح. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:206]

```
207:         Log.d(TAG, getDiagnostics())
```
> يُستدعى تسجيل تصحيحي (Log.d) بالوسم (TAG) ونصٍّ ناتج عن استدعاء «getDiagnostics». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:207]

```
208:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:208]

```
209: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:209]

```
210:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:210]

```
211:      * Monitors Bluetooth state changes in real-time and invokes the provided callback.
```
> تعليق: يُراقب تغيّرات حالة البلوتوث في الوقت الحقيقي ويستدعي ردّ النداء المُمرَّر. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:211]

```
212:      * Returns the BroadcastReceiver for manual un-registration.
```
> تعليق: يُعيد مُستقبِل البثّ (BroadcastReceiver) لإلغاء التسجيل يدوياً. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:212]

```
213:      */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:213]

```
214:     fun monitorBluetoothState(
```
> تُعرَّف دالة باسم «مراقبة حالة البلوتوث» (monitorBluetoothState) وتبدأ قائمة وُسطائها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:214]

```
215:         context: Context,
```
> وسيط أول باسم «السياق» (context) من نوع Context. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:215]

```
216:         bluetoothStatusManager: BluetoothStatusManager,
```
> وسيط ثانٍ باسم «مدير حالة البلوتوث» (bluetoothStatusManager) من نوع BluetoothStatusManager. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:216]

```
217:         onBluetoothStateChanged: (BluetoothStatus) -> Unit
```
> وسيط ثالث باسم «عند تغيّر حالة البلوتوث» (onBluetoothStateChanged) من نوع دالة تأخذ BluetoothStatus وتُعيد Unit. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:217]

```
218:     ): BroadcastReceiver {
```
> إغلاق قائمة الوُسطاء وتصريح نوع الإرجاع BroadcastReceiver وبداية جسم الدالة. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:218]

```
219: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:219]

```
220:         Log.d(TAG, "Starting Bluetooth State Monitoring")
```
> يُستدعى تسجيل تصحيحي (Log.d) بالوسم (TAG) والنص الحرفي «Starting Bluetooth State Monitoring». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:220]

```
221: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:221]

```
222:         if (!bluetoothStatusManager.isBluetoothSupported()) {
```
> شرط: إذا كانت نتيجة استدعاء «isBluetoothSupported» على مدير حالة البلوتوث غير صحيحة (منفيّة)، يبدأ نطاق الشرط. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:222]

```
223:             Log.e(TAG, "Bluetooth is not supported")
```
> يُستدعى تسجيل خطأ (Log.e) بالوسم (TAG) والنص الحرفي «Bluetooth is not supported». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:223]

```
224:             onBluetoothStateChanged(BluetoothStatus.NOT_SUPPORTED)
```
> يُستدعى ردّ النداء «onBluetoothStateChanged» بالقيمة BluetoothStatus.NOT_SUPPORTED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:224]

```
225:             bluetoothStatusManager.handleBluetoothStatus(BluetoothStatus.NOT_SUPPORTED)
```
> يُستدعى «handleBluetoothStatus» على مدير حالة البلوتوث بالقيمة BluetoothStatus.NOT_SUPPORTED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:225]

```
226:             return object : BroadcastReceiver() { override fun onReceive(p0: Context?, p1: Intent?) {}
```
> يُعيد كائناً مجهولاً يَرِث BroadcastReceiver ويُعيد تعريف الدالة «onReceive» بوسيطين p0 من نوع Context? وp1 من نوع Intent? بجسمٍ فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:226]

```
227:             }
```
> إغلاق نطاق الكائن المجهول المُعاد. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:227]

```
228:         }
```
> إغلاق نطاق الشرط. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:228]

```
229: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:229]

```
230:         val receiver = object : BroadcastReceiver() {
```
> يُعرَّف متغيّر ثابت باسم «المُستقبِل» (receiver) قيمتُه كائن مجهول يَرِث BroadcastReceiver، وبداية نطاقه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:230]

```
231:             override fun onReceive(context: Context?, intent: Intent?) {
```
> يُعاد تعريف الدالة «onReceive» بوسيطين: «السياق» (context) من نوع Context? و«النيّة» (intent) من نوع Intent?، وبداية جسمها. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:231]

```
232:                 when (intent?.getIntExtra(BluetoothAdapter.EXTRA_STATE, BluetoothAdapter.ERROR)) {
```
> جملة «when» تُفرّع على القيمة العددية المُستخرَجة باستدعاء getIntExtra على النيّة (بأمان عبر ?.) بالمفتاح BluetoothAdapter.EXTRA_STATE وقيمة افتراضية BluetoothAdapter.ERROR. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:232]

```
233:                     BluetoothAdapter.STATE_ON -> {
```
> فرع when للقيمة BluetoothAdapter.STATE_ON وبداية نطاقه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:233]

```
234:                         Log.d(TAG, "Bluetooth turned ON")
```
> يُستدعى تسجيل تصحيحي (Log.d) بالوسم (TAG) والنص الحرفي «Bluetooth turned ON». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:234]

```
235:                         onBluetoothStateChanged(BluetoothStatus.ENABLED)
```
> يُستدعى ردّ النداء «onBluetoothStateChanged» بالقيمة BluetoothStatus.ENABLED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:235]

```
236:                         bluetoothStatusManager.handleBluetoothStatus(BluetoothStatus.ENABLED)
```
> يُستدعى «handleBluetoothStatus» على مدير حالة البلوتوث بالقيمة BluetoothStatus.ENABLED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:236]

```
237:                     }
```
> إغلاق نطاق فرع STATE_ON. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:237]

```
238:                     BluetoothAdapter.STATE_OFF -> {
```
> فرع when للقيمة BluetoothAdapter.STATE_OFF وبداية نطاقه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:238]

```
239:                         Log.d(TAG, "Bluetooth turned OFF")
```
> يُستدعى تسجيل تصحيحي (Log.d) بالوسم (TAG) والنص الحرفي «Bluetooth turned OFF». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:239]

```
240:                         onBluetoothStateChanged(BluetoothStatus.DISABLED)
```
> يُستدعى ردّ النداء «onBluetoothStateChanged» بالقيمة BluetoothStatus.DISABLED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:240]

```
241:                         bluetoothStatusManager.onBluetoothDisabled("User has turned off their Blue")
```
> يُستدعى «onBluetoothDisabled» على مدير حالة البلوتوث بالنص الحرفي «User has turned off their Blue». [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:241]

```
242:                     }
```
> إغلاق نطاق فرع STATE_OFF. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:242]

```
243:                     BluetoothAdapter.STATE_TURNING_ON, BluetoothAdapter.STATE_OFF -> {
```
> فرع when يطابق إحدى القيمتين BluetoothAdapter.STATE_TURNING_ON أو BluetoothAdapter.STATE_OFF وبداية نطاقه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:243]

```
244:                         Log.d(TAG, "Bluetooth state transitioning: ${bluetoothStatusManager.getAdapterStateName(intent.getIntExtra(
```
> يُستدعى تسجيل تصحيحي (Log.d) بالوسم (TAG) ونصٍّ يبدأ بـ«Bluetooth state transitioning: » مُدمَجٍ بنتيجة استدعاء «getAdapterStateName» على مدير حالة البلوتوث، والذي يُمرَّر إليه ناتج getIntExtra على النيّة (يستمرّ التعبير في السطر التالي). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:244]

```
245:                             BluetoothAdapter.EXTRA_STATE, BluetoothAdapter.ERROR))}")
```
> تكملة الاستدعاء: وُسطاء getIntExtra هما المفتاح BluetoothAdapter.EXTRA_STATE والقيمة الافتراضية BluetoothAdapter.ERROR، ثم إغلاق الأقواس وقالب النص. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:245]

```
246:                     }
```
> إغلاق نطاق فرع STATE_TURNING_ON/STATE_OFF. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:246]

```
247:                 }
```
> إغلاق نطاق جملة when. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:247]

```
248:             }
```
> إغلاق نطاق الدالة onReceive. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:248]

```
249:         }
```
> إغلاق نطاق الكائن المجهول للمُستقبِل. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:249]

```
250: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:250]

```
251:         //Register the receiver
```
> تعليق: سجّل المُستقبِل. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:251]

```
252:         val filter = IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED)
```
> يُعرَّف متغيّر ثابت باسم «المُرشِّح» (filter) قيمتُه كائن IntentFilter مُنشَأ بالقيمة BluetoothAdapter.ACTION_STATE_CHANGED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:252]

```
253:         ContextCompat.registerReceiver(context, receiver, filter, ContextCompat.RECEIVER_NOT_EXPORTED)
```
> يُستدعى «registerReceiver» على ContextCompat بالوُسطاء: السياق (context)، والمُستقبِل (receiver)، والمُرشِّح (filter)، والرّاية ContextCompat.RECEIVER_NOT_EXPORTED. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:253]

```
254: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:254]

```
255:         //Check initial Bluetooth state
```
> تعليق: تحقّق من حالة البلوتوث الابتدائية. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:255]

```
256:         val initialStatus = bluetoothStatusManager.checkBluetoothStatus()
```
> يُعرَّف متغيّر ثابت باسم «الحالة الابتدائية» (initialStatus) قيمتُه ناتج استدعاء «checkBluetoothStatus» على مدير حالة البلوتوث. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:256]

```
257:         onBluetoothStateChanged(initialStatus)
```
> يُستدعى ردّ النداء «onBluetoothStateChanged» بالقيمة initialStatus. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:257]

```
258: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:258]

```
259: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:259]

```
260:         return receiver
```
> يُعيد المتغيّر «المُستقبِل» (receiver). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:260]

```
261:     }
```
> إغلاق نطاق الدالة monitorBluetoothState. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:261]

```
262: }
```
> إغلاق نطاق (نهاية صنف/كائن يحتوي الدوال السابقة). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:262]

```
263: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:263]

```
264: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:264]

```
265:  * Bluetooth status enum
```
> تعليق: تعداد حالة البلوتوث. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:265]

```
266:  */
```
> نهاية تعليق توثيقي. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:266]

```
267: enum class BluetoothStatus {
```
> يُعرَّف صنف تعداد (enum class) باسم «حالة البلوتوث» (BluetoothStatus) وبداية نطاقه. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:267]

```
268:     ENABLED,
```
> ثابت تعداد باسم «مُفعَّل» (ENABLED). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:268]

```
269:     DISABLED, 
```
> ثابت تعداد باسم «مُعطَّل» (DISABLED). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:269]

```
270:     NOT_SUPPORTED
```
> ثابت تعداد باسم «غير مدعوم» (NOT_SUPPORTED). [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:270]

```
271: }
```
> إغلاق نطاق صنف التعداد BluetoothStatus. [app/src/main/java/com/bitchat/android/onboarding/BluetoothStatusManager.kt:271]
