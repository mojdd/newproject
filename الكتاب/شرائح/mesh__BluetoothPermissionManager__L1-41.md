# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt (الأسطر 1–41)

```
1: package com.bitchat.android.mesh
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:2]

```
3: import android.Manifest
```
> يستورد (import) الصنف android.Manifest. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:3]

```
4: import android.content.Context
```
> يستورد الصنف Context من android.content. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:4]

```
5: import android.content.pm.PackageManager
```
> يستورد الصنف PackageManager من android.content.pm. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:5]

```
6: import androidx.core.app.ActivityCompat
```
> يستورد الصنف ActivityCompat من androidx.core.app. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:6]

```
7: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:7]

```
8: /**
```
> تعليق: بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:8]

```
9:  * Handles all Bluetooth permission checking logic
```
> تعليق: «يتولّى كل منطق فحص أذونات البلوتوث». [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:9]

```
10:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:10]

```
11: class BluetoothPermissionManager(private val context: Context) {
```
> يعرّف صنف مدير أذونات البلوتوث (BluetoothPermissionManager) له مُنشئ يأخذ مُعطى خاصاً غير قابل للتغيير باسم context من نوع Context، ويفتح نطاق جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:11]

```
12:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:12]

```
13:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:13]

```
14:      * Check if all required Bluetooth permissions are granted
```
> تعليق: «يتحقّق إن كانت كل أذونات البلوتوث المطلوبة ممنوحة». [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:14]

```
15:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:15]

```
16:     fun hasBluetoothPermissions(): Boolean {
```
> يعرّف دالة باسم لديه أذونات البلوتوث (hasBluetoothPermissions) لا تأخذ مُعطيات وتعيد قيمة منطقية (Boolean)، ويفتح نطاق جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:16]

```
17:         val permissions = mutableListOf<String>()
```
> يعرّف متغيراً غير قابل لإعادة الإسناد باسم permissions ويُسند إليه قائمة قابلة للتعديل (mutableListOf) فارغة من نوع String. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:17]

```
18:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:18]

```
19:         if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.S) {
```
> يفتح جملة شرطية (if) تتحقّق إن كان android.os.Build.VERSION.SDK_INT أكبر من أو يساوي android.os.Build.VERSION_CODES.S، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:19]

```
20:             permissions.addAll(listOf(
```
> يستدعي على permissions الدالة addAll ويبدأ تمرير قائمة (listOf) كوسيط. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:20]

```
21:                 Manifest.permission.BLUETOOTH_ADVERTISE,
```
> يضيف إلى القائمة العنصر Manifest.permission.BLUETOOTH_ADVERTISE. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:21]

```
22:                 Manifest.permission.BLUETOOTH_CONNECT,
```
> يضيف إلى القائمة العنصر Manifest.permission.BLUETOOTH_CONNECT. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:22]

```
23:                 Manifest.permission.BLUETOOTH_SCAN
```
> يضيف إلى القائمة العنصر Manifest.permission.BLUETOOTH_SCAN. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:23]

```
24:             ))
```
> يغلق قائمة listOf ثم يغلق استدعاء addAll. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:24]

```
25:         } else {
```
> يغلق كتلة if ويفتح كتلة وإلّا (else). [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:25]

```
26:             permissions.addAll(listOf(
```
> يستدعي على permissions الدالة addAll ويبدأ تمرير قائمة listOf كوسيط. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:26]

```
27:                 Manifest.permission.BLUETOOTH,
```
> يضيف إلى القائمة العنصر Manifest.permission.BLUETOOTH. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:27]

```
28:                 Manifest.permission.BLUETOOTH_ADMIN
```
> يضيف إلى القائمة العنصر Manifest.permission.BLUETOOTH_ADMIN. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:28]

```
29:             ))
```
> يغلق قائمة listOf ثم يغلق استدعاء addAll. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:29]

```
30:         }
```
> إغلاق نطاق (كتلة else). [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:30]

```
31:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:31]

```
32:         permissions.addAll(listOf(
```
> يستدعي على permissions الدالة addAll ويبدأ تمرير قائمة listOf كوسيط. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:32]

```
33:             Manifest.permission.ACCESS_COARSE_LOCATION,
```
> يضيف إلى القائمة العنصر Manifest.permission.ACCESS_COARSE_LOCATION. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:33]

```
34:             Manifest.permission.ACCESS_FINE_LOCATION
```
> يضيف إلى القائمة العنصر Manifest.permission.ACCESS_FINE_LOCATION. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:34]

```
35:         ))
```
> يغلق قائمة listOf ثم يغلق استدعاء addAll. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:36]

```
37:         return permissions.all { 
```
> يعيد نتيجة استدعاء الدالة all على permissions، التي تتحقّق أن كل العناصر تحقّق الشرط في الكتلة (lambda) التالية، ويفتح نطاق الكتلة. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:37]

```
38:             ActivityCompat.checkSelfPermission(context, it) == PackageManager.PERMISSION_GRANTED 
```
> يقارن ناتج استدعاء ActivityCompat.checkSelfPermission مع المعطيين context والعنصر الحالي it بأنه يساوي PackageManager.PERMISSION_GRANTED. [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:38]

```
39:         }
```
> إغلاق نطاق (كتلة الـ lambda الخاصة بالدالة all). [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:39]

```
40:     }
```
> إغلاق نطاق (جسم الدالة hasBluetoothPermissions). [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:40]

```
41: }
```
> إغلاق نطاق (جسم الصنف BluetoothPermissionManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothPermissionManager.kt:41]
