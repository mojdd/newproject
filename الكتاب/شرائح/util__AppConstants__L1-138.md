# شريحة — app/src/main/java/com/bitchat/android/util/AppConstants.kt (الأسطر 1–138)

```
1: package com.bitchat.android.util
```
> يعلن أن هذا الملف ينتمي للحزمة (package) باسم `com.bitchat.android.util`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:2]

```
3: import java.util.UUID
```
> يستورد (import) النوع `UUID` من حزمة `java.util` لاستعماله في هذا الملف. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:4]

```
5: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/util/AppConstants.kt:5]

```
6:  * Centralized application-wide constants.
```
> تعليق: «ثوابت مركزية على مستوى التطبيق كله». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:6]

```
7:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:7]

```
8: object AppConstants {
```
> يعرّف كائناً مفرداً (object) باسم `AppConstants` (ثوابت التطبيق) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:8]

```
9:     // Packet time-to-live (hops)
```
> تعليق: «مدة بقاء الرزمة (عدد القفزات)». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:9]

```
10:     val MESSAGE_TTL_HOPS: UByte = 7u     // Default TTL for regular packets
```
> يعرّف متغيّراً ثابتاً للقراءة (val) باسم `MESSAGE_TTL_HOPS` (قفزات بقاء الرسالة) من نوع `UByte` وقيمته الحرفية `7u`، مع تعليق: «مدة البقاء الافتراضية للرزم العادية». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:10]

```
11:     val SYNC_TTL_HOPS: UByte = 0u        // TTL for neighbor-only sync packets
```
> يعرّف متغيّراً ثابتاً للقراءة (val) باسم `SYNC_TTL_HOPS` (قفزات بقاء المزامنة) من نوع `UByte` وقيمته الحرفية `0u`، مع تعليق: «مدة البقاء لرزم المزامنة الخاصة بالجيران فقط». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:11]

```
12: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:12]

```
13:     object Mesh {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Mesh` (الشبكة المتشابكة) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:13]

```
14:         // Peer lifecycle
```
> تعليق: «دورة حياة النظير». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:14]

```
15:         const val STALE_PEER_TIMEOUT_MS: Long = 180_000L // 3 minutes
```
> يعرّف ثابتاً وقت الترجمة (const val) باسم `STALE_PEER_TIMEOUT_MS` (مهلة انتهاء صلاحية النظير) من نوع `Long` وقيمته الحرفية `180_000L`، مع تعليق: «٣ دقائق». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:15]

```
16:         const val PEER_CLEANUP_INTERVAL_MS: Long = 60_000L
```
> يعرّف ثابتاً (const val) باسم `PEER_CLEANUP_INTERVAL_MS` (فترة تنظيف النظراء) من نوع `Long` وقيمته الحرفية `60_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:16]

```
17: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:17]

```
18:         // BLE connection tracking
```
> تعليق: «تتبّع اتصال البلوتوث منخفض الطاقة (BLE)». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:18]

```
19:         const val CONNECTION_RETRY_DELAY_MS: Long = 5_000L
```
> يعرّف ثابتاً (const val) باسم `CONNECTION_RETRY_DELAY_MS` (مهلة إعادة محاولة الاتصال) من نوع `Long` وقيمته الحرفية `5_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:19]

```
20:         const val MAX_CONNECTION_ATTEMPTS: Int = 3
```
> يعرّف ثابتاً (const val) باسم `MAX_CONNECTION_ATTEMPTS` (أقصى محاولات الاتصال) من نوع `Int` وقيمته الحرفية `3`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:20]

```
21:         const val CONNECTION_CLEANUP_DELAY_MS: Long = 500L
```
> يعرّف ثابتاً (const val) باسم `CONNECTION_CLEANUP_DELAY_MS` (مهلة تنظيف الاتصال) من نوع `Long` وقيمته الحرفية `500L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:21]

```
22:         const val CONNECTION_CLEANUP_INTERVAL_MS: Long = 30_000L
```
> يعرّف ثابتاً (const val) باسم `CONNECTION_CLEANUP_INTERVAL_MS` (فترة تنظيف الاتصال) من نوع `Long` وقيمته الحرفية `30_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:22]

```
23:         const val BROADCAST_CLEANUP_DELAY_MS: Long = 500L
```
> يعرّف ثابتاً (const val) باسم `BROADCAST_CLEANUP_DELAY_MS` (مهلة تنظيف البثّ) من نوع `Long` وقيمته الحرفية `500L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:24]

```
25:         // GATT client RSSI updates
```
> تعليق: «تحديثات قوة الإشارة (RSSI) لعميل GATT». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:25]

```
26:         const val RSSI_UPDATE_INTERVAL_MS: Long = 5_000L
```
> يعرّف ثابتاً (const val) باسم `RSSI_UPDATE_INTERVAL_MS` (فترة تحديث قوة الإشارة) من نوع `Long` وقيمته الحرفية `5_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:26]

```
27: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:27]

```
28:         object Gatt {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Gatt` (جات) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:28]

```
29:             val SERVICE_UUID: UUID = UUID.fromString("F47B5E2D-4A9E-4C5A-9B3F-8E1D2C3A4B5C")
```
> يعرّف متغيّراً ثابتاً للقراءة (val) باسم `SERVICE_UUID` (معرّف الخدمة) من نوع `UUID`، وقيمته ناتج استدعاء `UUID.fromString` على السلسلة الحرفية `"F47B5E2D-4A9E-4C5A-9B3F-8E1D2C3A4B5C"`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:29]

```
30:             val CHARACTERISTIC_UUID: UUID = UUID.fromString("A1B2C3D4-E5F6-4A5B-8C9D-0E1F2A3B4C5D")
```
> يعرّف متغيّراً ثابتاً للقراءة (val) باسم `CHARACTERISTIC_UUID` (معرّف الخاصية) من نوع `UUID`، وقيمته ناتج استدعاء `UUID.fromString` على السلسلة الحرفية `"A1B2C3D4-E5F6-4A5B-8C9D-0E1F2A3B4C5D"`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:30]

```
31:             val DESCRIPTOR_UUID: UUID = UUID.fromString("00002902-0000-1000-8000-00805f9b34fb")
```
> يعرّف متغيّراً ثابتاً للقراءة (val) باسم `DESCRIPTOR_UUID` (معرّف الواصف) من نوع `UUID`، وقيمته ناتج استدعاء `UUID.fromString` على السلسلة الحرفية `"00002902-0000-1000-8000-00805f9b34fb"`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:31]

```
32:         }
```
> إغلاق نطاق الكائن `Gatt`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:32]

```
33:     }
```
> إغلاق نطاق الكائن `Mesh`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:33]

```
34: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:34]

```
35:     object Sync {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Sync` (المزامنة) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:35]

```
36:         const val CLEANUP_INTERVAL_MS: Long = 60_000L
```
> يعرّف ثابتاً (const val) باسم `CLEANUP_INTERVAL_MS` (فترة التنظيف) من نوع `Long` وقيمته الحرفية `60_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:36]

```
37:     }
```
> إغلاق نطاق الكائن `Sync`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:37]

```
38: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:38]

```
39:     object Fragmentation {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Fragmentation` (التجزئة) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:39]

```
40:         const val FRAGMENT_SIZE_THRESHOLD: Int = 512
```
> يعرّف ثابتاً (const val) باسم `FRAGMENT_SIZE_THRESHOLD` (عتبة حجم التجزئة) من نوع `Int` وقيمته الحرفية `512`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:40]

```
41:         const val MAX_FRAGMENT_SIZE: Int = 469
```
> يعرّف ثابتاً (const val) باسم `MAX_FRAGMENT_SIZE` (أقصى حجم جزء) من نوع `Int` وقيمته الحرفية `469`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:41]

```
42:         const val FRAGMENT_TIMEOUT_MS: Long = 30_000L
```
> يعرّف ثابتاً (const val) باسم `FRAGMENT_TIMEOUT_MS` (مهلة الجزء) من نوع `Long` وقيمته الحرفية `30_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:42]

```
43:         const val CLEANUP_INTERVAL_MS: Long = 10_000L
```
> يعرّف ثابتاً (const val) باسم `CLEANUP_INTERVAL_MS` (فترة التنظيف) من نوع `Long` وقيمته الحرفية `10_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:43]

```
44:         const val MAX_FRAGMENTS_PER_ID: Int = 256
```
> يعرّف ثابتاً (const val) باسم `MAX_FRAGMENTS_PER_ID` (أقصى أجزاء لكل معرّف) من نوع `Int` وقيمته الحرفية `256`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:44]

```
45:         const val MAX_FRAGMENT_TOTAL_BYTES: Int = 1_048_576
```
> يعرّف ثابتاً (const val) باسم `MAX_FRAGMENT_TOTAL_BYTES` (أقصى مجموع بايتات الجزء) من نوع `Int` وقيمته الحرفية `1_048_576`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:45]

```
46:         const val MAX_ACTIVE_FRAGMENT_SETS: Int = 64
```
> يعرّف ثابتاً (const val) باسم `MAX_ACTIVE_FRAGMENT_SETS` (أقصى مجموعات أجزاء نشطة) من نوع `Int` وقيمته الحرفية `64`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:46]

```
47:         const val MAX_GLOBAL_FRAGMENT_TOTAL_BYTES: Long = 4L * 1_048_576L
```
> يعرّف ثابتاً (const val) باسم `MAX_GLOBAL_FRAGMENT_TOTAL_BYTES` (أقصى مجموع بايتات الأجزاء الكلّي) من نوع `Long` وقيمته ناتج ضرب التعبير الحرفي `4L * 1_048_576L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:47]

```
48:     }
```
> إغلاق نطاق الكائن `Fragmentation`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:48]

```
49: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:49]

```
50:     object Security {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Security` (الأمان) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:50]

```
51:         const val MESSAGE_TIMEOUT_MS: Long = 300_000L
```
> يعرّف ثابتاً (const val) باسم `MESSAGE_TIMEOUT_MS` (مهلة الرسالة) من نوع `Long` وقيمته الحرفية `300_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:51]

```
52:         const val CLEANUP_INTERVAL_MS: Long = 300_000L
```
> يعرّف ثابتاً (const val) باسم `CLEANUP_INTERVAL_MS` (فترة التنظيف) من نوع `Long` وقيمته الحرفية `300_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:52]

```
53:         const val MAX_PROCESSED_MESSAGES: Int = 10_000
```
> يعرّف ثابتاً (const val) باسم `MAX_PROCESSED_MESSAGES` (أقصى رسائل معالَجة) من نوع `Int` وقيمته الحرفية `10_000`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:53]

```
54:         const val MAX_PROCESSED_KEY_EXCHANGES: Int = 1_000
```
> يعرّف ثابتاً (const val) باسم `MAX_PROCESSED_KEY_EXCHANGES` (أقصى تبادلات مفاتيح معالَجة) من نوع `Int` وقيمته الحرفية `1_000`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:54]

```
55:     }
```
> إغلاق نطاق الكائن `Security`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:55]

```
56: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:56]

```
57:     object Noise {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Noise` (نويز) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:57]

```
58:         const val REKEY_TIME_LIMIT_MS: Long = 3_600_000L // 1 hour
```
> يعرّف ثابتاً (const val) باسم `REKEY_TIME_LIMIT_MS` (حدّ زمن إعادة التمفتح) من نوع `Long` وقيمته الحرفية `3_600_000L`، مع تعليق: «ساعة واحدة». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:58]

```
59:         const val REKEY_MESSAGE_LIMIT_ENCRYPTION: Long = 1_000L // per session, encryption service policy
```
> يعرّف ثابتاً (const val) باسم `REKEY_MESSAGE_LIMIT_ENCRYPTION` (حدّ رسائل إعادة التمفتح للتشفير) من نوع `Long` وقيمته الحرفية `1_000L`، مع تعليق: «لكل جلسة، سياسة خدمة التشفير». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:59]

```
60:         const val REKEY_MESSAGE_LIMIT_SESSION: Long = 10_000L // session-level ceiling
```
> يعرّف ثابتاً (const val) باسم `REKEY_MESSAGE_LIMIT_SESSION` (حدّ رسائل إعادة التمفتح للجلسة) من نوع `Long` وقيمته الحرفية `10_000L`، مع تعليق: «السقف على مستوى الجلسة». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:60]

```
61:         const val MAX_PAYLOAD_SIZE_BYTES: Int = 256
```
> يعرّف ثابتاً (const val) باسم `MAX_PAYLOAD_SIZE_BYTES` (أقصى حجم حمولة بالبايت) من نوع `Int` وقيمته الحرفية `256`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:61]

```
62:         const val HIGH_NONCE_WARNING_THRESHOLD: Long = 1_000_000_000L
```
> يعرّف ثابتاً (const val) باسم `HIGH_NONCE_WARNING_THRESHOLD` (عتبة تحذير ارتفاع الرقم المستعمل مرة) من نوع `Long` وقيمته الحرفية `1_000_000_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:62]

```
63:     }
```
> إغلاق نطاق الكائن `Noise`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:63]

```
64: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:64]

```
65:     object Verification {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Verification` (التحقّق) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:65]

```
66:         const val QR_MAX_AGE_SECONDS: Long = 300L // 5 minutes
```
> يعرّف ثابتاً (const val) باسم `QR_MAX_AGE_SECONDS` (أقصى عمر لرمز الاستجابة السريعة بالثواني) من نوع `Long` وقيمته الحرفية `300L`، مع تعليق: «٥ دقائق». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:66]

```
67:     }
```
> إغلاق نطاق الكائن `Verification`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:67]

```
68: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:68]

```
69:     object Protocol {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Protocol` (البروتوكول) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:69]

```
70:         const val COMPRESSION_THRESHOLD_BYTES: Int = 100
```
> يعرّف ثابتاً (const val) باسم `COMPRESSION_THRESHOLD_BYTES` (عتبة الضغط بالبايت) من نوع `Int` وقيمته الحرفية `100`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:70]

```
71:         const val MAX_PAYLOAD_LENGTH: Int = 10_485_760
```
> يعرّف ثابتاً (const val) باسم `MAX_PAYLOAD_LENGTH` (أقصى طول للحمولة) من نوع `Int` وقيمته الحرفية `10_485_760`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:71]

```
72:     }
```
> إغلاق نطاق الكائن `Protocol`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:72]

```
73: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:73]

```
74:     object StoreForward {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `StoreForward` (التخزين والتمرير) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:74]

```
75:         const val MESSAGE_CACHE_TIMEOUT_MS: Long = 43_200_000L // 12h
```
> يعرّف ثابتاً (const val) باسم `MESSAGE_CACHE_TIMEOUT_MS` (مهلة مخبأ الرسالة) من نوع `Long` وقيمته الحرفية `43_200_000L`، مع تعليق: «١٢ ساعة». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:75]

```
76:         const val MAX_CACHED_MESSAGES: Int = 100
```
> يعرّف ثابتاً (const val) باسم `MAX_CACHED_MESSAGES` (أقصى رسائل مخبّأة) من نوع `Int` وقيمته الحرفية `100`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:76]

```
77:         const val MAX_CACHED_MESSAGES_FAVORITES: Int = 1_000
```
> يعرّف ثابتاً (const val) باسم `MAX_CACHED_MESSAGES_FAVORITES` (أقصى رسائل مخبّأة للمفضّلين) من نوع `Int` وقيمته الحرفية `1_000`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:77]

```
78:         const val CLEANUP_INTERVAL_MS: Long = 600_000L
```
> يعرّف ثابتاً (const val) باسم `CLEANUP_INTERVAL_MS` (فترة التنظيف) من نوع `Long` وقيمته الحرفية `600_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:78]

```
79:     }
```
> إغلاق نطاق الكائن `StoreForward`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:79]

```
80: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:80]

```
81:     object Power {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Power` (الطاقة) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:81]

```
82:         const val CRITICAL_BATTERY_PERCENT: Int = 10
```
> يعرّف ثابتاً (const val) باسم `CRITICAL_BATTERY_PERCENT` (نسبة البطارية الحرجة) من نوع `Int` وقيمته الحرفية `10`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:82]

```
83:         const val LOW_BATTERY_PERCENT: Int = 20
```
> يعرّف ثابتاً (const val) باسم `LOW_BATTERY_PERCENT` (نسبة البطارية المنخفضة) من نوع `Int` وقيمته الحرفية `20`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:83]

```
84:         const val MEDIUM_BATTERY_PERCENT: Int = 50
```
> يعرّف ثابتاً (const val) باسم `MEDIUM_BATTERY_PERCENT` (نسبة البطارية المتوسطة) من نوع `Int` وقيمته الحرفية `50`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:84]

```
85:         const val SCAN_ON_DURATION_NORMAL_MS: Long = 8_000L
```
> يعرّف ثابتاً (const val) باسم `SCAN_ON_DURATION_NORMAL_MS` (مدة تشغيل المسح في الوضع العادي) من نوع `Long` وقيمته الحرفية `8_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:85]

```
86:         const val SCAN_OFF_DURATION_NORMAL_MS: Long = 2_000L
```
> يعرّف ثابتاً (const val) باسم `SCAN_OFF_DURATION_NORMAL_MS` (مدة إيقاف المسح في الوضع العادي) من نوع `Long` وقيمته الحرفية `2_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:86]

```
87:         const val SCAN_ON_DURATION_POWER_SAVE_MS: Long = 2_000L
```
> يعرّف ثابتاً (const val) باسم `SCAN_ON_DURATION_POWER_SAVE_MS` (مدة تشغيل المسح في وضع توفير الطاقة) من نوع `Long` وقيمته الحرفية `2_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:87]

```
88:         const val SCAN_OFF_DURATION_POWER_SAVE_MS: Long = 28_000L
```
> يعرّف ثابتاً (const val) باسم `SCAN_OFF_DURATION_POWER_SAVE_MS` (مدة إيقاف المسح في وضع توفير الطاقة) من نوع `Long` وقيمته الحرفية `28_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:88]

```
89:         const val SCAN_ON_DURATION_ULTRA_LOW_MS: Long = 1_000L
```
> يعرّف ثابتاً (const val) باسم `SCAN_ON_DURATION_ULTRA_LOW_MS` (مدة تشغيل المسح في الوضع المنخفض جداً) من نوع `Long` وقيمته الحرفية `1_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:89]

```
90:         const val SCAN_OFF_DURATION_ULTRA_LOW_MS: Long = 29_000L
```
> يعرّف ثابتاً (const val) باسم `SCAN_OFF_DURATION_ULTRA_LOW_MS` (مدة إيقاف المسح في الوضع المنخفض جداً) من نوع `Long` وقيمته الحرفية `29_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:90]

```
91:         const val MAX_CONNECTIONS_NORMAL: Int = 8
```
> يعرّف ثابتاً (const val) باسم `MAX_CONNECTIONS_NORMAL` (أقصى اتصالات في الوضع العادي) من نوع `Int` وقيمته الحرفية `8`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:91]

```
92:         const val MAX_CONNECTIONS_POWER_SAVE: Int = 8
```
> يعرّف ثابتاً (const val) باسم `MAX_CONNECTIONS_POWER_SAVE` (أقصى اتصالات في وضع توفير الطاقة) من نوع `Int` وقيمته الحرفية `8`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:92]

```
93:         const val MAX_CONNECTIONS_ULTRA_LOW: Int = 4
```
> يعرّف ثابتاً (const val) باسم `MAX_CONNECTIONS_ULTRA_LOW` (أقصى اتصالات في الوضع المنخفض جداً) من نوع `Int` وقيمته الحرفية `4`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:93]

```
94:     }
```
> إغلاق نطاق الكائن `Power`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:94]

```
95: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:95]

```
96:     object Nostr {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Nostr` (نوستر) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:96]

```
97:         // Relay backoff
```
> تعليق: «تراجع مرحّل الإرسال (Relay backoff)». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:97]

```
98:         const val INITIAL_BACKOFF_INTERVAL_MS: Long = 1_000L
```
> يعرّف ثابتاً (const val) باسم `INITIAL_BACKOFF_INTERVAL_MS` (فترة التراجع الأولية) من نوع `Long` وقيمته الحرفية `1_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:98]

```
99:         const val MAX_BACKOFF_INTERVAL_MS: Long = 300_000L
```
> يعرّف ثابتاً (const val) باسم `MAX_BACKOFF_INTERVAL_MS` (أقصى فترة تراجع) من نوع `Long` وقيمته الحرفية `300_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:99]

```
100:         const val BACKOFF_MULTIPLIER: Double = 2.0
```
> يعرّف ثابتاً (const val) باسم `BACKOFF_MULTIPLIER` (مضاعِف التراجع) من نوع `Double` وقيمته الحرفية `2.0`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:100]

```
101:         const val MAX_RECONNECT_ATTEMPTS: Int = 10
```
> يعرّف ثابتاً (const val) باسم `MAX_RECONNECT_ATTEMPTS` (أقصى محاولات إعادة الاتصال) من نوع `Int` وقيمته الحرفية `10`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:101]

```
102: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:102]

```
103:         // Transport
```
> تعليق: «النقل (Transport)». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:103]

```
104:         const val READ_ACK_INTERVAL_MS: Long = 350L
```
> يعرّف ثابتاً (const val) باسم `READ_ACK_INTERVAL_MS` (فترة إقرار القراءة) من نوع `Long` وقيمته الحرفية `350L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:104]

```
105: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:105]

```
106:         // Deduplicator
```
> تعليق: «مزيل التكرار (Deduplicator)». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:106]

```
107:         const val DEFAULT_DEDUP_CAPACITY: Int = 10_000
```
> يعرّف ثابتاً (const val) باسم `DEFAULT_DEDUP_CAPACITY` (سعة إزالة التكرار الافتراضية) من نوع `Int` وقيمته الحرفية `10_000`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:107]

```
108: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:108]

```
109:         // Relay subscription validation
```
> تعليق: «التحقّق من اشتراك المرحّل (Relay subscription validation)». [app/src/main/java/com/bitchat/android/util/AppConstants.kt:109]

```
110:         const val SUBSCRIPTION_VALIDATION_INTERVAL_MS: Long = 30_000L
```
> يعرّف ثابتاً (const val) باسم `SUBSCRIPTION_VALIDATION_INTERVAL_MS` (فترة التحقّق من الاشتراك) من نوع `Long` وقيمته الحرفية `30_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:110]

```
111:     }
```
> إغلاق نطاق الكائن `Nostr`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:111]

```
112: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:112]

```
113:     object Tor {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Tor` (تور) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:113]

```
114:         const val DEFAULT_SOCKS_PORT: Int = 9060
```
> يعرّف ثابتاً (const val) باسم `DEFAULT_SOCKS_PORT` (منفذ SOCKS الافتراضي) من نوع `Int` وقيمته الحرفية `9060`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:114]

```
115:         const val RESTART_DELAY_MS: Long = 2_000L
```
> يعرّف ثابتاً (const val) باسم `RESTART_DELAY_MS` (مهلة إعادة التشغيل) من نوع `Long` وقيمته الحرفية `2_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:115]

```
116:         const val INACTIVITY_TIMEOUT_MS: Long = 5_000L
```
> يعرّف ثابتاً (const val) باسم `INACTIVITY_TIMEOUT_MS` (مهلة الخمول) من نوع `Long` وقيمته الحرفية `5_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:116]

```
117:         const val MAX_RETRY_ATTEMPTS: Int = 5
```
> يعرّف ثابتاً (const val) باسم `MAX_RETRY_ATTEMPTS` (أقصى محاولات إعادة) من نوع `Int` وقيمته الحرفية `5`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:117]

```
118:         const val STOP_TIMEOUT_MS: Long = 7_000L
```
> يعرّف ثابتاً (const val) باسم `STOP_TIMEOUT_MS` (مهلة الإيقاف) من نوع `Long` وقيمته الحرفية `7_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:118]

```
119:     }
```
> إغلاق نطاق الكائن `Tor`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:119]

```
120: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:120]

```
121:     object UI {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `UI` (واجهة المستخدم) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:121]

```
122:         const val MAX_NICKNAME_LENGTH: Int = 15
```
> يعرّف ثابتاً (const val) باسم `MAX_NICKNAME_LENGTH` (أقصى طول للاسم المستعار) من نوع `Int` وقيمته الحرفية `15`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:122]

```
123:         const val BASE_FONT_SIZE_SP: Int = 15
```
> يعرّف ثابتاً (const val) باسم `BASE_FONT_SIZE_SP` (حجم الخط الأساس بوحدة sp) من نوع `Int` وقيمته الحرفية `15`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:123]

```
124:         const val MESSAGE_DEDUP_TIMEOUT_MS: Long = 30_000L
```
> يعرّف ثابتاً (const val) باسم `MESSAGE_DEDUP_TIMEOUT_MS` (مهلة إزالة تكرار الرسالة) من نوع `Long` وقيمته الحرفية `30_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:124]

```
125:         const val SYSTEM_EVENT_DEDUP_TIMEOUT_MS: Long = 5_000L
```
> يعرّف ثابتاً (const val) باسم `SYSTEM_EVENT_DEDUP_TIMEOUT_MS` (مهلة إزالة تكرار حدث النظام) من نوع `Long` وقيمته الحرفية `5_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:125]

```
126:         const val ACTIVE_PEERS_NOTIFICATION_INTERVAL_MS: Long = 300_000L
```
> يعرّف ثابتاً (const val) باسم `ACTIVE_PEERS_NOTIFICATION_INTERVAL_MS` (فترة إشعار النظراء النشطين) من نوع `Long` وقيمته الحرفية `300_000L`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:126]

```
127:         const val ACTION_FORCE_FINISH: String = "com.bitchat.android.ACTION_FORCE_FINISH"
```
> يعرّف ثابتاً (const val) باسم `ACTION_FORCE_FINISH` (إجراء الإنهاء القسري) من نوع `String` وقيمته السلسلة الحرفية `"com.bitchat.android.ACTION_FORCE_FINISH"`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:127]

```
128:         const val PERMISSION_FORCE_FINISH: String = "com.bitchat.android.permission.FORCE_FINISH"
```
> يعرّف ثابتاً (const val) باسم `PERMISSION_FORCE_FINISH` (إذن الإنهاء القسري) من نوع `String` وقيمته السلسلة الحرفية `"com.bitchat.android.permission.FORCE_FINISH"`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:128]

```
129:     }
```
> إغلاق نطاق الكائن `UI`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:129]

```
130: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:130]

```
131:     object Media {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Media` (الوسائط) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:131]

```
132:         const val MAX_FILE_SIZE_BYTES: Long = 50L * 1024 * 1024
```
> يعرّف ثابتاً (const val) باسم `MAX_FILE_SIZE_BYTES` (أقصى حجم ملف بالبايت) من نوع `Long` وقيمته ناتج ضرب التعبير الحرفي `50L * 1024 * 1024`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:132]

```
133:     }
```
> إغلاق نطاق الكائن `Media`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:133]

```
134: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:134]

```
135:     object Services {
```
> يعرّف كائناً مفرداً متداخلاً (object) باسم `Services` (الخدمات) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:135]

```
136:         const val SEEN_MESSAGE_MAX_IDS: Int = 10_000
```
> يعرّف ثابتاً (const val) باسم `SEEN_MESSAGE_MAX_IDS` (أقصى معرّفات للرسائل المرئية) من نوع `Int` وقيمته الحرفية `10_000`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:136]

```
137:     }
```
> إغلاق نطاق الكائن `Services`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:137]

```
138: }
```
> إغلاق نطاق الكائن `AppConstants`. [app/src/main/java/com/bitchat/android/util/AppConstants.kt:138]
