# شريحة — app/src/main/java/com/bitchat/android/services/NicknameProvider.kt (الأسطر 1–21)

```
1: package com.bitchat.android.services
```
> يعلن أن هذا الملف يتبع الحزمة (package) باسم `com.bitchat.android.services`. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف `Context` من حزمة `android.content`. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:3]

```
4: import com.bitchat.android.ui.DataManager
```
> يستورد الصنف `DataManager` (مدير البيانات) من حزمة `com.bitchat.android.ui`. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:5]

```
6: /**
```
> تعليق: بداية كتلة تعليق توثيقي (بداية تعليق متعدد الأسطر). [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:6]

```
7:  * Provides current user's nickname for announcements and leave messages.
```
> تعليق: «يوفّر اسم المستخدم المستعار الحالي للإعلانات ورسائل المغادرة». [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:7]

```
8:  * If no nickname saved, falls back to the provided peerID.
```
> تعليق: «إذا لم يُحفَظ اسم مستعار، يرجع إلى معرّف النِّد (peerID) المُمرَّر». [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:8]

```
9:  */
```
> تعليق: نهاية كتلة التعليق التوثيقي (إغلاق التعليق متعدد الأسطر). [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:9]

```
10: object NicknameProvider {
```
> يعرّف كائناً مفرداً (object) باسم `NicknameProvider` (مزوّد الاسم المستعار) ويفتح جسمه. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:10]

```
11:     fun getNickname(context: Context, myPeerID: String): String {
```
> يعرّف دالة (fun) باسم `getNickname` (جلب الاسم المستعار) تأخذ وسيطاً `context` من نوع `Context` ووسيطاً `myPeerID` من نوع `String`، وتُعيد قيمة من نوع `String`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:11]

```
12:         return try {
```
> يُعيد (return) نتيجة كتلة `try` (محاولة)، ويفتح كتلة المحاولة. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:12]

```
13:             val dm = DataManager(context.applicationContext)
```
> يعرّف متغيراً ثابتاً (val) باسم `dm` ويضبط قيمته بإنشاء كائن `DataManager` بتمرير `context.applicationContext` (سياق التطبيق). [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:13]

```
14:             val nick = dm.loadNickname()
```
> يعرّف متغيراً ثابتاً باسم `nick` ويضبط قيمته بنتيجة استدعاء الدالة `loadNickname` (تحميل الاسم المستعار) على الكائن `dm`. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:14]

```
15:             if (nick.isNullOrBlank()) myPeerID else nick
```
> يقيّم شرطاً: إذا كانت `nick` فارغة أو خالية من المحتوى عبر `isNullOrBlank` (فارغ أو مكوّن من فراغات) فالقيمة `myPeerID`، وإلا فالقيمة `nick`. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:15]

```
16:         } catch (_: Exception) {
```
> يغلق كتلة `try` ويفتح كتلة `catch` (التقاط) تلتقط استثناءً من نوع `Exception` بمتغيّر مُهمَل (`_`). [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:16]

```
17:             myPeerID
```
> القيمة المُعادة من كتلة `catch` هي `myPeerID`. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:17]

```
18:         }
```
> إغلاق نطاق (إغلاق كتلة `catch`). [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:18]

```
19:     }
```
> إغلاق نطاق (إغلاق جسم الدالة `getNickname`). [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:19]

```
20: }
```
> إغلاق نطاق (إغلاق جسم الكائن `NicknameProvider`). [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:20]

```
21: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/services/NicknameProvider.kt:21]
