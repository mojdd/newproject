# شريحة — app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt (الأسطر 1–30)

```
1: package com.bitchat.android.mesh
```
> يُعرّف هذا السطر اسم الحزمة (package) ويضبطه على القيمة `com.bitchat.android.mesh`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:2]

```
3: import kotlinx.coroutines.CoroutineScope
```
> يستورد (import) الصنف `CoroutineScope` من المكتبة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:3]

```
4: import kotlinx.coroutines.Dispatchers
```
> يستورد الكائن `Dispatchers` من المكتبة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:4]

```
5: import kotlinx.coroutines.SupervisorJob
```
> يستورد الدالة `SupervisorJob` من المكتبة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:5]

```
6: import kotlinx.coroutines.flow.MutableSharedFlow
```
> يستورد الصنف `MutableSharedFlow` من المكتبة `kotlinx.coroutines.flow`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:6]

```
7: import kotlinx.coroutines.flow.SharedFlow
```
> يستورد الواجهة `SharedFlow` من المكتبة `kotlinx.coroutines.flow`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:7]

```
8: import kotlinx.coroutines.launch
```
> يستورد الدالة `launch` من المكتبة `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:9]

```
10: data class TransferProgressEvent(
```
> يبدأ تعريف صنف بيانات (data class) باسم `TransferProgressEvent` (حدث تقدّم النقل) ويفتح قائمة معاملات بانيه. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:10]

```
11:     val transferId: String,
```
> يُعرّف خاصية ثابتة (val) باسم `transferId` (معرّف النقل) من نوع `String`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:11]

```
12:     val sent: Int,
```
> يُعرّف خاصية ثابتة باسم `sent` (المُرسَل) من نوع `Int`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:12]

```
13:     val total: Int,
```
> يُعرّف خاصية ثابتة باسم `total` (الإجمالي) من نوع `Int`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:13]

```
14:     val completed: Boolean
```
> يُعرّف خاصية ثابتة باسم `completed` (مكتمل) من نوع `Boolean`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:14]

```
15: )
```
> يُغلق قائمة معاملات باني صنف البيانات `TransferProgressEvent`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:15]

```
16: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:16]

```
17: object TransferProgressManager {
```
> يبدأ تعريف كائن مفرد (object) باسم `TransferProgressManager` (مدير تقدّم النقل) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:17]

```
18:     private val scope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يُعرّف خاصية خاصة ثابتة (private val) باسم `scope` ويضبطها بإنشاء `CoroutineScope` من جمع `Dispatchers.IO` مع `SupervisorJob()`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:18]

```
19:     private val _events = MutableSharedFlow<TransferProgressEvent>(replay = 0, extraBufferCapacity = 32)
```
> يُعرّف خاصية خاصة ثابتة باسم `_events` ويضبطها بإنشاء `MutableSharedFlow` من نوع `TransferProgressEvent` بمعامل `replay` يساوي 0 ومعامل `extraBufferCapacity` يساوي 32. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:19]

```
20:     val events: SharedFlow<TransferProgressEvent> = _events
```
> يُعرّف خاصية ثابتة عامة باسم `events` من نوع `SharedFlow` لـ `TransferProgressEvent` ويضبطها على قيمة `_events`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:20]

```
21: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:21]

```
22:     fun start(id: String, total: Int) { emit(id, 0, total, false) }
```
> يُعرّف دالة باسم `start` تأخذ معاملين `id` من نوع `String` و`total` من نوع `Int`، وتستدعي `emit` بالقيم `id` و0 و`total` و`false`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:22]

```
23:     fun progress(id: String, sent: Int, total: Int) { emit(id, sent, total, sent >= total) }
```
> يُعرّف دالة باسم `progress` تأخذ المعاملات `id` و`sent` و`total`، وتستدعي `emit` بالقيم `id` و`sent` و`total` ونتيجة المقارنة `sent >= total`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:23]

```
24:     fun complete(id: String, total: Int) { emit(id, total, total, true) }
```
> يُعرّف دالة باسم `complete` تأخذ المعاملين `id` و`total`، وتستدعي `emit` بالقيم `id` و`total` و`total` و`true`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:25]

```
26:     private fun emit(id: String, sent: Int, total: Int, done: Boolean) {
```
> يبدأ تعريف دالة خاصة (private fun) باسم `emit` (يبثّ) تأخذ المعاملات `id` من نوع `String` و`sent` من نوع `Int` و`total` من نوع `Int` و`done` من نوع `Boolean`، ويفتح نطاقها. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:26]

```
27:         scope.launch { _events.emit(TransferProgressEvent(id, sent, total, done)) }
```
> يستدعي `launch` على `scope` لتشغيل قطعة تستدعي `emit` على `_events` بكائن `TransferProgressEvent` مُنشأ بالقيم `id` و`sent` و`total` و`done`. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:27]

```
28:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:28]

```
29: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:29]

```
30: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/TransferProgressManager.kt:30]
