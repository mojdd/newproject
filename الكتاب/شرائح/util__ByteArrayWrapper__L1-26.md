# شريحة — app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt (الأسطر 1–26)

```
1: package com.bitchat.android.util
```
> يُعرّف هذا السطر اسم الحزمة (package) التي ينتمي إليها الملف وهي «com.bitchat.android.util». [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:2]

```
3: import java.util.Arrays
```
> يستورد هذا السطر الصنف «Arrays» من حزمة «java.util» القياسية. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:4]

```
5: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:5]

```
6:  * A wrapper class for ByteArray to allow it to be used as a key in HashMaps.
```
> تعليق: صنف غلاف (wrapper) لمصفوفة البايتات (ByteArray) يسمح باستعمالها مفتاحاً في خرائط التجزئة (HashMaps). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:6]

```
7:  * The default ByteArray does not override equals() and hashCode() based on content.
```
> تعليق: مصفوفة البايتات الافتراضية (ByteArray) لا تتجاوز الدالتين equals() و hashCode() اعتماداً على المحتوى. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:7]

```
8:  *
```
> تعليق: سطر فاصل فارغ داخل التعليق التوثيقي. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:8]

```
9:  * @param bytes The byte array to wrap.
```
> تعليق: وسم المعامل (@param) للمعامل «bytes» وهو مصفوفة البايتات المراد تغليفها. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:9]

```
10:  */
```
> نهاية التعليق التوثيقي (KDoc). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:10]

```
11: data class ByteArrayWrapper(val bytes: ByteArray) {
```
> يُعرّف هذا السطر صنف بيانات (data class) باسم «غلاف مصفوفة البايتات» (ByteArrayWrapper) ذا معامل بنّاء واحد ثابت للقراءة فقط (val) باسم «bytes» من نوع مصفوفة البايتات (ByteArray)، ويفتح نطاق جسم الصنف. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:11]

```
12:     override fun equals(other: Any?): Boolean {
```
> يُعرّف هذا السطر تجاوزاً (override) للدالة «equals» (التساوي) التي تأخذ معاملاً باسم «other» من نوع «Any?» القابل لأن يكون فارغاً وتُعيد قيمة منطقية (Boolean)، ويفتح نطاق جسم الدالة. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:12]

```
13:         if (this === other) return true
```
> يفحص هذا السطر التطابق المرجعي (===) بين الكائن الحالي «this» والمعامل «other»، فإن تطابقا أعاد القيمة «صحيح» (true). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:13]

```
14:         if (javaClass != other?.javaClass) return false
```
> يفحص هذا السطر عدم تساوي صنف الجافا (javaClass) للكائن الحالي مع صنف الجافا للمعامل «other» (بالوصول الآمن ?.)، فإن اختلفا أعاد القيمة «خطأ» (false). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:14]

```
15:         other as ByteArrayWrapper
```
> يُجري هذا السطر تحويلاً نوعياً (cast) للمعامل «other» إلى نوع «غلاف مصفوفة البايتات» (ByteArrayWrapper). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:15]

```
16:         return Arrays.equals(bytes, other.bytes)
```
> يُعيد هذا السطر نتيجة استدعاء الدالة «Arrays.equals» التي تقارن مصفوفة البايتات «bytes» للكائن الحالي مع مصفوفة البايتات «other.bytes» للمعامل. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:16]

```
17:     }
```
> إغلاق نطاق الدالة «equals» (التساوي). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:17]

```
18: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:18]

```
19:     override fun hashCode(): Int {
```
> يُعرّف هذا السطر تجاوزاً (override) للدالة «hashCode» (رمز التجزئة) التي لا تأخذ معاملات وتُعيد عدداً صحيحاً (Int)، ويفتح نطاق جسم الدالة. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:19]

```
20:         return Arrays.hashCode(bytes)
```
> يُعيد هذا السطر نتيجة استدعاء الدالة «Arrays.hashCode» محسوبةً على مصفوفة البايتات «bytes». [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:20]

```
21:     }
```
> إغلاق نطاق الدالة «hashCode» (رمز التجزئة). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:21]

```
22: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:22]

```
23:     fun toHexString(): String {
```
> يُعرّف هذا السطر الدالة «toHexString» (التحويل إلى نص ست عشري) التي لا تأخذ معاملات وتُعيد سلسلة نصية (String)، ويفتح نطاق جسم الدالة. [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:23]

```
24:         return bytes.joinToString("") { "%02x".format(it) }
```
> يُعيد هذا السطر سلسلة نصية ناتجة عن دمج (joinToString) عناصر مصفوفة البايتات «bytes» بفاصل فارغ (""), حيث يُنسّق كل عنصر «it» بالصيغة الست عشرية "%02x" (خانتان بأصفار بادئة). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:24]

```
25:     }
```
> إغلاق نطاق الدالة «toHexString» (التحويل إلى نص ست عشري). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:25]

```
26: }
```
> إغلاق نطاق صنف البيانات «غلاف مصفوفة البايتات» (ByteArrayWrapper). [app/src/main/java/com/bitchat/android/util/ByteArrayWrapper.kt:26]
