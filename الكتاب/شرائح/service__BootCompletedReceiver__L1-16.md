# شريحة — app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt (الأسطر 1–16)

```
1: package com.bitchat.android.service
```
> يُعلِن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.service`. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:2]

```
3: import android.content.BroadcastReceiver
```
> يستورد (import) الصنف `BroadcastReceiver` (مستقبِل البثّ) من `android.content`. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:3]

```
4: import android.content.Context
```
> يستورد الصنف `Context` (السياق) من `android.content`. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:4]

```
5: import android.content.Intent
```
> يستورد الصنف `Intent` (النيّة/الطلب) من `android.content`. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:5]

```
6: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:6]

```
7: class BootCompletedReceiver : BroadcastReceiver() {
```
> يُعرِّف صنفاً (class) باسم `BootCompletedReceiver` (مستقبِل اكتمال الإقلاع) يَرِث من `BroadcastReceiver` (مستقبِل البثّ) ويفتح نطاق الصنف. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:7]

```
8:     override fun onReceive(context: Context, intent: Intent) {
```
> يُعيد تعريف (override) الدالة `onReceive` (عند الاستلام) التي تأخذ مُعاملاً `context` من نوع `Context` (السياق) ومُعاملاً `intent` من نوع `Intent` (النيّة) ويفتح نطاق الدالة. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:8]

```
9:         // Ensure preferences are initialized on cold boot before reading values
```
> تعليق: تأكَّد من أن التفضيلات مُهيَّأة عند الإقلاع البارد قبل قراءة القيم. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:9]

```
10:         try { MeshServicePreferences.init(context.applicationContext) } catch (_: Exception) { }
```
> داخل كتلة `try`، يستدعي الدالة `init` (التهيئة) من `MeshServicePreferences` (تفضيلات خدمة الشبكة المتشابكة) مُمرِّراً إليها `context.applicationContext` (سياق التطبيق)، وفي كتلة `catch` يلتقط استثناءً (Exception) باسم مُهمَل `_` ولا يفعل شيئاً. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:11]

```
12:         if (MeshServicePreferences.isAutoStartEnabled(true)) {
```
> يفتح جملة شرطية (if) شرطها هو ناتج استدعاء الدالة `isAutoStartEnabled` (هل التشغيل التلقائي مُفعَّل) من `MeshServicePreferences` مُمرِّراً إليها القيمة `true`، ويفتح نطاق الشرط. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:12]

```
13:             MeshForegroundService.start(context.applicationContext)
```
> يستدعي الدالة `start` (ابدأ) من `MeshForegroundService` (خدمة الواجهة الأمامية للشبكة المتشابكة) مُمرِّراً إليها `context.applicationContext` (سياق التطبيق). [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:13]

```
14:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:14]

```
15:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:15]

```
16: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/BootCompletedReceiver.kt:16]
