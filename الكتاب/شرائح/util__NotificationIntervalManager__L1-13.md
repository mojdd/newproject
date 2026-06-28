# شريحة — app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt (الأسطر 1–13)

```
1: package com.bitchat.android.util
```
> يعلن انتماء الملف إلى الحزمة (package) المسماة `com.bitchat.android.util`. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:2]

```
3: class NotificationIntervalManager {
```
> يعرّف صنفاً (class) باسم مدير فترة الإشعار (NotificationIntervalManager) ويفتح نطاق جسده. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:3]

```
4:   private var _lastNetworkNotificationTime = 0L
```
> يعرّف متغيّراً خاصاً (private) قابلاً للتغيير باسم وقت آخر إشعار شبكة الداخلي (_lastNetworkNotificationTime) ويسند إليه القيمة الحرفية `0L` من نوع العدد الطويل (Long). [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:4]

```
5:   val lastNetworkNotificationTime: Long
```
> يعرّف خاصية (val) للقراءة فقط باسم وقت آخر إشعار شبكة (lastNetworkNotificationTime) من نوع العدد الطويل (Long). [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:5]

```
6:     get() = _lastNetworkNotificationTime
```
> يعرّف الدالة المُحصِّلة (getter) لتلك الخاصية بحيث تُعيد قيمة المتغيّر الخاص `_lastNetworkNotificationTime`. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:6]

```
7: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:7]

```
8:   val recentlySeenPeers: MutableSet<String> = mutableSetOf()
```
> يعرّف خاصية (val) باسم النظائر المرئية حديثاً (recentlySeenPeers) من نوع المجموعة القابلة للتغيير من السلاسل النصية (MutableSet<String>) ويسند إليها مجموعة فارغة منشأة بالاستدعاء `mutableSetOf()`. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:9]

```
10:   fun setLastNetworkNotificationTime(notificationTime: Long) {
```
> يعرّف دالة (fun) باسم ضبط وقت آخر إشعار شبكة (setLastNetworkNotificationTime) تأخذ معاملاً باسم وقت الإشعار (notificationTime) من نوع العدد الطويل (Long) ويفتح نطاق جسدها. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:10]

```
11:     _lastNetworkNotificationTime = notificationTime
```
> يسند قيمة المعامل `notificationTime` إلى المتغيّر الخاص `_lastNetworkNotificationTime`. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:11]

```
12:   }
```
> إغلاق نطاق الدالة `setLastNetworkNotificationTime`. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:12]

```
13: }
```
> إغلاق نطاق الصنف `NotificationIntervalManager`. [app/src/main/java/com/bitchat/android/util/NotificationIntervalManager.kt:13]
