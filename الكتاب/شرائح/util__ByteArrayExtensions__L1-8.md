# شريحة — app/src/main/java/com/bitchat/android/util/ByteArrayExtensions.kt (الأسطر 1–8)

```
1: package com.bitchat.android.util
```
> هذا السطر يُعرّف الحزمة (package) التي ينتمي إليها الملف، وهي `com.bitchat.android.util`. [app/src/main/java/com/bitchat/android/util/ByteArrayExtensions.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/ByteArrayExtensions.kt:2]

```
3: /**
```
> بداية تعليق توثيقي (تعليق KDoc يبدأ بالرمز `/**`). [app/src/main/java/com/bitchat/android/util/ByteArrayExtensions.kt:3]

```
4:  * Extension function to convert a ByteArray to a hexadecimal string.
```
> تعليق: «دالة امتداد لتحويل مصفوفة البايتات (ByteArray) إلى سلسلة نصية بالنظام الست عشري». [app/src/main/java/com/bitchat/android/util/ByteArrayExtensions.kt:4]

```
5:  */
```
> نهاية التعليق التوثيقي (الرمز `*/` يُغلق تعليق KDoc). [app/src/main/java/com/bitchat/android/util/ByteArrayExtensions.kt:5]

```
6: fun ByteArray.toHexString(): String {
```
> هذا السطر يُعرّف دالة امتداد (extension function) باسم `toHexString` على النوع مصفوفة البايتات (ByteArray)، ولا تأخذ وُسطاء، وتُعيد قيمة من نوع سلسلة نصية (String)، ويفتح جسم الدالة بالقوس `{`. [app/src/main/java/com/bitchat/android/util/ByteArrayExtensions.kt:6]

```
7:     return this.joinToString("") { "%02x".format(it) }
```
> هذا السطر يُعيد (return) ناتج استدعاء الدالة `joinToString` على المُستقبِل `this` بفاصل نصي فارغ `""`، حيث تُطبَّق على كل عنصر `it` دالة التنسيق `format` بقالب `"%02x"` الذي يحوّل البايت إلى رقمين ست عشريين. [app/src/main/java/com/bitchat/android/util/ByteArrayExtensions.kt:7]

```
8: }
```
> إغلاق نطاق دالة الامتداد `toHexString`. [app/src/main/java/com/bitchat/android/util/ByteArrayExtensions.kt:8]
