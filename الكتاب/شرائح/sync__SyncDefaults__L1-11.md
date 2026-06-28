# شريحة — app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt (الأسطر 1–11)

```
1: package com.bitchat.android.sync
```
> يُعلِن السطر انتماء الملف إلى الحزمة (package) المسمّاة `com.bitchat.android.sync`. [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:2]

```
3: object SyncDefaults {
```
> يُعرّف السطر كائناً مفرداً (object) باسم `SyncDefaults` (افتراضات المزامنة) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:3]

```
4:     // Default values used when debug prefs are unavailable
```
> تعليق: القيم الافتراضية المستعملة عندما تكون تفضيلات التنقيح (debug prefs) غير متوفّرة. [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:4]

```
5:     const val DEFAULT_FILTER_BYTES: Int = 256
```
> يُعرّف السطر ثابتاً (const val) باسم `DEFAULT_FILTER_BYTES` (بايتات المرشّح الافتراضية) من نوع عددٍ صحيح (Int) ويضبط قيمته على ٢٥٦. [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:5]

```
6:     const val DEFAULT_FPR_PERCENT: Double = 1.0
```
> يُعرّف السطر ثابتاً (const val) باسم `DEFAULT_FPR_PERCENT` (نسبة المئوية الافتراضية لـ FPR) من نوع عددٍ عشري مزدوج (Double) ويضبط قيمته على ١٫٠. [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:6]

```
7: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:7]

```
8:     // Receiver-side hard cap to avoid DoS (also enforced in RequestSyncPacket)
```
> تعليق: حدٌّ أقصى صارم في جانب المُستقبِل (Receiver-side hard cap) لتفادي هجوم حجب الخدمة (DoS) (مفروضٌ أيضاً في `RequestSyncPacket`). [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:8]

```
9:     const val MAX_ACCEPT_FILTER_BYTES: Int = 1024
```
> يُعرّف السطر ثابتاً (const val) باسم `MAX_ACCEPT_FILTER_BYTES` (أقصى بايتات مرشّح مقبولة) من نوع عددٍ صحيح (Int) ويضبط قيمته على ١٠٢٤. [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:9]

```
10: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:10]

```
11: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/sync/SyncDefaults.kt:11]
