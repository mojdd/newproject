# شريحة — app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt (الأسطر 1–250)

```
1: package com.bitchat.android.noise
```
> يُعرّف هذا السطر الحزمة (package) باسم `com.bitchat.android.noise`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:2]

```
3: import android.util.Log
```
> يستورد الصنف `Log` من الحزمة `android.util`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:3]

```
4: import java.util.concurrent.ConcurrentHashMap
```
> يستورد الصنف `ConcurrentHashMap` (خريطة تجزئة متزامنة) من الحزمة `java.util.concurrent`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:4]

```
5: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:5]

```
6: /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:6]

```
7:  * SIMPLIFIED Noise session manager - focuses on core functionality only
```
> تعليق: مدير جلسات Noise مُبسَّط — يركّز على الوظيفة الأساسية فقط. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:7]

```
8:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:8]

```
9: class NoiseSessionManager(
```
> يُعرّف الصنف `NoiseSessionManager` (مدير جلسات Noise) ويبدأ قائمة معاملات الباني (constructor). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:9]

```
10:     private val localStaticPrivateKey: ByteArray,
```
> يُعرّف خاصية بانٍ خاصة `localStaticPrivateKey` (المفتاح الخاص الثابت المحلي) من النوع `ByteArray` (مصفوفة بايتات). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:10]

```
11:     private val localStaticPublicKey: ByteArray,
```
> يُعرّف خاصية بانٍ خاصة `localStaticPublicKey` (المفتاح العام الثابت المحلي) من النوع `ByteArray`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:11]

```
12:     private val localPeerID: String
```
> يُعرّف خاصية بانٍ خاصة `localPeerID` (معرّف النظير المحلي) من النوع `String` (نص). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:12]

```
13: ) {
```
> يُغلق قائمة معاملات الباني ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:13]

```
14:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:14]

```
15:     companion object {
```
> يبدأ الكائن المرافق (companion object) للصنف. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:15]

```
16:         private const val TAG = "NoiseSessionManager"
```
> يُعرّف ثابتاً خاصاً `TAG` (الوسم) ويضبط قيمته النصية `"NoiseSessionManager"`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:16]

```
17:         private const val HANDSHAKE_TIMEOUT_MS = 20_000L
```
> يُعرّف ثابتاً خاصاً `HANDSHAKE_TIMEOUT_MS` (مهلة المصافحة بالميلي ثانية) ويضبط قيمته العددية الطويلة `20_000L`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:17]

```
18:         private const val HANDSHAKE_MESSAGE_1_SIZE = 32
```
> يُعرّف ثابتاً خاصاً `HANDSHAKE_MESSAGE_1_SIZE` (حجم رسالة المصافحة الأولى) ويضبط قيمته `32`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:18]

```
19:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:19]

```
20:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:20]

```
21:     private val sessions = ConcurrentHashMap<String, NoiseSession>()
```
> يُعرّف خاصية خاصة `sessions` (الجلسات) ويضبط قيمتها بكائن `ConcurrentHashMap` جديد مفاتيحه من النوع `String` وقيمه من النوع `NoiseSession`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:21]

```
22:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:22]

```
23:     // Callbacks
```
> تعليق: ردود النداء (Callbacks). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:23]

```
24:     var onSessionEstablished: ((String, ByteArray) -> Unit)? = null
```
> يُعرّف خاصية متغيرة `onSessionEstablished` (عند تأسيس الجلسة) من نوع دالة تقبل `String` و`ByteArray` وتعيد `Unit`، قابلة للإبطال، ويضبط قيمتها الابتدائية `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:24]

```
25:     var onSessionFailed: ((String, Throwable) -> Unit)? = null
```
> يُعرّف خاصية متغيرة `onSessionFailed` (عند فشل الجلسة) من نوع دالة تقبل `String` و`Throwable` وتعيد `Unit`، قابلة للإبطال، ويضبط قيمتها الابتدائية `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:25]

```
26:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:26]

```
27:     // MARK: - Simple Session Management
```
> تعليق: علامة (MARK) — إدارة الجلسات البسيطة. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:27]

```
28: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:28]

```
29:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:29]

```
30:      * Add new session for a peer
```
> تعليق: إضافة جلسة جديدة لنظير. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:30]

```
31:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:31]

```
32:     fun addSession(peerID: String, session: NoiseSession) {
```
> يُعرّف الدالة `addSession` (أضِف جلسة) التي تقبل `peerID` من النوع `String` و`session` من النوع `NoiseSession` وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:32]

```
33:         sessions[peerID] = session
```
> يضبط في الخريطة `sessions` عند المفتاح `peerID` القيمة `session`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:33]

```
34:         Log.d(TAG, "Added new session for $peerID")
```
> يستدعي `Log.d` للتسجيل بمستوى التصحيح بالوسم `TAG` والنص "أُضيفت جلسة جديدة لـ $peerID". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:34]

```
35:     }
```
> إغلاق نطاق الدالة `addSession`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:35]

```
36: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:36]

```
37:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:37]

```
38:      * Get existing session for a peer
```
> تعليق: الحصول على الجلسة الموجودة لنظير. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:38]

```
39:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:39]

```
40:     fun getSession(peerID: String): NoiseSession? {
```
> يُعرّف الدالة `getSession` (احصل على جلسة) التي تقبل `peerID` من النوع `String` وتعيد `NoiseSession` قابلاً للإبطال، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:40]

```
41:         val session = sessions[peerID]
```
> يُعرّف متغيراً ثابتاً `session` ويضبط قيمته بالعنصر من الخريطة `sessions` عند المفتاح `peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:41]

```
42:         return session
```
> يعيد القيمة `session`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:42]

```
43:     }
```
> إغلاق نطاق الدالة `getSession`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:43]

```
44:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:44]

```
45:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:45]

```
46:      * Remove session for a peer
```
> تعليق: إزالة الجلسة لنظير. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:46]

```
47:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:47]

```
48:     fun removeSession(peerID: String) {
```
> يُعرّف الدالة `removeSession` (أزِل جلسة) التي تقبل `peerID` من النوع `String` وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:48]

```
49:         sessions[peerID]?.destroy()
```
> يستدعي `destroy()` على العنصر من الخريطة `sessions` عند المفتاح `peerID` إن لم يكن معدوماً. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:49]

```
50:         sessions.remove(peerID)
```
> يستدعي `remove` على الخريطة `sessions` لإزالة المدخل عند المفتاح `peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:50]

```
51:         Log.d(TAG, "Removed session for $peerID")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "أُزيلت الجلسة لـ $peerID". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:51]

```
52:     }
```
> إغلاق نطاق الدالة `removeSession`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:52]

```
53:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:53]

```
54:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:54]

```
55:      * SIMPLIFIED: Initiate handshake - no tie breaker, just start
```
> تعليق: مُبسَّط: بدء المصافحة — بلا فاصل تعادل، فقط ابدأ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:55]

```
56:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:56]

```
57:     fun initiateHandshake(peerID: String): ByteArray? {
```
> يُعرّف الدالة `initiateHandshake` (ابدأ المصافحة) التي تقبل `peerID` من النوع `String` وتعيد `ByteArray` قابلاً للإبطال، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:57]

```
58:         Log.d(TAG, "initiateHandshake($peerID)")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "initiateHandshake($peerID)". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:58]

```
59: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:59]

```
60:         val now = System.currentTimeMillis()
```
> يُعرّف متغيراً ثابتاً `now` (الآن) ويضبط قيمته بنتيجة `System.currentTimeMillis()` (الوقت الحالي بالميلي ثانية). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:60]

```
61:         val existing = getSession(peerID)
```
> يُعرّف متغيراً ثابتاً `existing` (الموجود) ويضبط قيمته بنتيجة استدعاء `getSession(peerID)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:61]

```
62:         if (existing != null) {
```
> يبدأ شرط `if` يتحقق أنّ `existing` لا يساوي `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:62]

```
63:             when {
```
> يبدأ تعبير `when` بلا وسيط (سلسلة شروط منطقية). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:63]

```
64:                 existing.isEstablished() -> {
```
> فرع `when`: إذا أعادت `existing.isEstablished()` (هل أُسِّست) صحيحاً، يفتح كتلته. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:64]

```
65:                     Log.d(TAG, "Handshake already established with $peerID, skipping initiate")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "المصافحة مؤسَّسة مسبقاً مع $peerID، تخطّي البدء". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:65]

```
66:                     return null
```
> يعيد القيمة `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:66]

```
67:                 }
```
> إغلاق نطاق فرع `isEstablished`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:67]

```
68:                 existing.isHandshaking() -> {
```
> فرع `when`: إذا أعادت `existing.isHandshaking()` (هل تجري مصافحة) صحيحاً، يفتح كتلته. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:68]

```
69:                     if (!isHandshakeStale(existing, now)) {
```
> يبدأ شرط `if` يتحقق أنّ `isHandshakeStale(existing, now)` (هل المصافحة قديمة) تعيد خطأً. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:69]

```
70:                         Log.d(TAG, "Handshake already in progress with $peerID, not restarting")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "المصافحة جارية مسبقاً مع $peerID، لا إعادة بدء". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:70]

```
71:                         return null
```
> يعيد القيمة `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:71]

```
72:                     }
```
> إغلاق نطاق شرط `if` لعدم القِدَم. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:72]

```
73:                     Log.d(TAG, "Handshake with $peerID is stale; restarting")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "المصافحة مع $peerID قديمة؛ إعادة البدء". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:73]

```
74:                     removeSession(peerID)
```
> يستدعي `removeSession(peerID)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:74]

```
75:                 }
```
> إغلاق نطاق فرع `isHandshaking`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:75]

```
76:                 else -> {
```
> فرع `when` الافتراضي `else`، يفتح كتلته. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:76]

```
77:                     removeSession(peerID)
```
> يستدعي `removeSession(peerID)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:77]

```
78:                 }
```
> إغلاق نطاق فرع `else`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:78]

```
79:             }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:79]

```
80:         }
```
> إغلاق نطاق شرط `if (existing != null)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:80]

```
81:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:81]

```
82:         // Create new session as initiator
```
> تعليق: أنشئ جلسة جديدة بدور البادئ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:82]

```
83:         val session = NoiseSession(
```
> يُعرّف متغيراً ثابتاً `session` ويبدأ إنشاء كائن `NoiseSession` بقائمة وسائط. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:83]

```
84:             peerID = peerID,
```
> يمرّر للوسيط المسمّى `peerID` القيمة `peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:84]

```
85:             isInitiator = true,
```
> يمرّر للوسيط المسمّى `isInitiator` (هل بادئ) القيمة `true`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:85]

```
86:             localStaticPrivateKey = localStaticPrivateKey,
```
> يمرّر للوسيط المسمّى `localStaticPrivateKey` القيمة `localStaticPrivateKey`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:86]

```
87:             localStaticPublicKey = localStaticPublicKey
```
> يمرّر للوسيط المسمّى `localStaticPublicKey` القيمة `localStaticPublicKey`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:87]

```
88:         )
```
> يُغلق قائمة وسائط إنشاء `NoiseSession`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:88]

```
89:         Log.d(TAG, "Storing new INITIATOR session for $peerID")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "تخزين جلسة بادئ جديدة لـ $peerID". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:89]

```
90:         addSession(peerID, session)
```
> يستدعي `addSession(peerID, session)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:90]

```
91:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:91]

```
92:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:92]

```
93:             val handshakeData = session.startHandshake()
```
> يُعرّف متغيراً ثابتاً `handshakeData` (بيانات المصافحة) ويضبط قيمته بنتيجة `session.startHandshake()` (ابدأ المصافحة). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:93]

```
94:             Log.d(TAG, "Started handshake with $peerID as INITIATOR")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "بُدئت المصافحة مع $peerID كبادئ". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:94]

```
95:             return handshakeData
```
> يعيد القيمة `handshakeData`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:95]

```
96:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً `e` من النوع `Exception`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:96]

```
97:             sessions.remove(peerID)
```
> يستدعي `remove` على الخريطة `sessions` لإزالة المدخل عند المفتاح `peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:97]

```
98:             throw e
```
> يرمي الاستثناء `e`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:98]

```
99:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:99]

```
100:     }
```
> إغلاق نطاق الدالة `initiateHandshake`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:100]

```
101:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:101]

```
102:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:102]

```
103:      * Handle incoming handshake message
```
> تعليق: عالِج رسالة المصافحة الواردة. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:103]

```
104:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:104]

```
105:     fun processHandshakeMessage(peerID: String, message: ByteArray): ByteArray? {
```
> يُعرّف الدالة `processHandshakeMessage` (عالِج رسالة المصافحة) التي تقبل `peerID` من النوع `String` و`message` من النوع `ByteArray` وتعيد `ByteArray` قابلاً للإبطال، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:105]

```
106:         Log.d(TAG, "processHandshakeMessage($peerID, ${message.size} bytes)")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "processHandshakeMessage($peerID, ${message.size} bytes)" مع حجم الرسالة. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:106]

```
107:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:107]

```
108:         try {
```
> يبدأ كتلة `try`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:108]

```
109:             var session = getSession(peerID)
```
> يُعرّف متغيراً قابلاً للتغيير `session` ويضبط قيمته بنتيجة `getSession(peerID)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:109]

```
110: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:110]

```
111:             // Collision handling: both sides initiated and we received message 1
```
> تعليق: معالجة التصادم: كلا الطرفين بدأ وقد استلمنا الرسالة الأولى. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:111]

```
112:             if (session != null &&
```
> يبدأ شرط `if` يتحقق أنّ `session` لا يساوي `null` ويربط بـ«و» منطقية. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:112]

```
113:                 session.isHandshaking() &&
```
> متابعة الشرط: وأنّ `session.isHandshaking()` تعيد صحيحاً، مع «و» منطقية. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:113]

```
114:                 session.isInitiatorRole() &&
```
> متابعة الشرط: وأنّ `session.isInitiatorRole()` (هل دوره بادئ) تعيد صحيحاً، مع «و» منطقية. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:114]

```
115:                 message.size == HANDSHAKE_MESSAGE_1_SIZE
```
> متابعة الشرط: وأنّ `message.size` يساوي `HANDSHAKE_MESSAGE_1_SIZE`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:115]

```
116:             ) {
```
> يُغلق قوس شرط `if` ويفتح كتلته. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:116]

```
117:                 val shouldYield = localPeerID > peerID
```
> يُعرّف متغيراً ثابتاً `shouldYield` (هل ينبغي التنازل) ويضبط قيمته بنتيجة المقارنة `localPeerID > peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:117]

```
118:                 if (shouldYield) {
```
> يبدأ شرط `if` يتحقق أنّ `shouldYield` صحيح. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:118]

```
119:                     Log.d(TAG, "Handshake collision with $peerID; yielding to responder role")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "تصادم مصافحة مع $peerID؛ التنازل لدور المستجيب". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:119]

```
120:                     removeSession(peerID)
```
> يستدعي `removeSession(peerID)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:120]

```
121:                     session = null
```
> يضبط قيمة `session` إلى `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:121]

```
122:                 } else {
```
> يُغلق كتلة `if` ويبدأ كتلة `else`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:122]

```
123:                     Log.d(TAG, "Handshake collision with $peerID; keeping initiator role")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "تصادم مصافحة مع $peerID؛ الإبقاء على دور البادئ". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:123]

```
124:                     return null
```
> يعيد القيمة `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:124]

```
125:                 }
```
> إغلاق نطاق كتلة `else`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:125]

```
126:             }
```
> إغلاق نطاق شرط `if` لمعالجة التصادم. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:126]

```
127:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:127]

```
128:             // If no session exists, create one as responder
```
> تعليق: إذا لم توجد جلسة، أنشئ واحدة بدور المستجيب. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:128]

```
129:             if (session == null) {
```
> يبدأ شرط `if` يتحقق أنّ `session` يساوي `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:129]

```
130:                 Log.d(TAG, "Creating new RESPONDER session for $peerID")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "إنشاء جلسة مستجيب جديدة لـ $peerID". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:130]

```
131:                 session = NoiseSession(
```
> يضبط `session` بكائن `NoiseSession` جديد ويبدأ قائمة وسائطه. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:131]

```
132:                     peerID = peerID,
```
> يمرّر للوسيط المسمّى `peerID` القيمة `peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:132]

```
133:                     isInitiator = false,
```
> يمرّر للوسيط المسمّى `isInitiator` القيمة `false`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:133]

```
134:                     localStaticPrivateKey = localStaticPrivateKey,
```
> يمرّر للوسيط المسمّى `localStaticPrivateKey` القيمة `localStaticPrivateKey`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:134]

```
135:                     localStaticPublicKey = localStaticPublicKey
```
> يمرّر للوسيط المسمّى `localStaticPublicKey` القيمة `localStaticPublicKey`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:135]

```
136:                 )
```
> يُغلق قائمة وسائط إنشاء `NoiseSession`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:136]

```
137:                 addSession(peerID, session)
```
> يستدعي `addSession(peerID, session)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:137]

```
138:             }
```
> إغلاق نطاق شرط `if (session == null)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:138]

```
139:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:139]

```
140:             // Process handshake message
```
> تعليق: عالِج رسالة المصافحة. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:140]

```
141:             val response = session.processHandshakeMessage(message)
```
> يُعرّف متغيراً ثابتاً `response` (الردّ) ويضبط قيمته بنتيجة `session.processHandshakeMessage(message)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:141]

```
142:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:142]

```
143:             // Check if session is established
```
> تعليق: تحقّق إن كانت الجلسة قد أُسِّست. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:143]

```
144:             if (session.isEstablished()) {
```
> يبدأ شرط `if` يتحقق أنّ `session.isEstablished()` تعيد صحيحاً. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:144]

```
145:                 Log.d(TAG, "✅ Session ESTABLISHED with $peerID")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "✅ الجلسة مؤسَّسة مع $peerID". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:145]

```
146:                 val remoteStaticKey = session.getRemoteStaticPublicKey()
```
> يُعرّف متغيراً ثابتاً `remoteStaticKey` (المفتاح الثابت البعيد) ويضبط قيمته بنتيجة `session.getRemoteStaticPublicKey()`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:146]

```
147:                 if (remoteStaticKey != null) {
```
> يبدأ شرط `if` يتحقق أنّ `remoteStaticKey` لا يساوي `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:147]

```
148:                     onSessionEstablished?.invoke(peerID, remoteStaticKey)
```
> يستدعي `invoke(peerID, remoteStaticKey)` على ردّ النداء `onSessionEstablished` إن لم يكن معدوماً. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:148]

```
149:                 }
```
> إغلاق نطاق شرط `if (remoteStaticKey != null)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:149]

```
150:             }
```
> إغلاق نطاق شرط `if (session.isEstablished())`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:150]

```
151:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:151]

```
152:             return response
```
> يعيد القيمة `response`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:152]

```
153:             
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:153]

```
154:         } catch (e: Exception) {
```
> يُغلق كتلة `try` ويبدأ كتلة `catch` تلتقط استثناءً `e` من النوع `Exception`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:154]

```
155:             Log.e(TAG, "Handshake failed with $peerID: ${e.message}")
```
> يستدعي `Log.e` للتسجيل بمستوى الخطأ بالوسم `TAG` والنص "فشلت المصافحة مع $peerID: ${e.message}". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:155]

```
156:             sessions.remove(peerID)
```
> يستدعي `remove` على الخريطة `sessions` لإزالة المدخل عند المفتاح `peerID`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:156]

```
157:             onSessionFailed?.invoke(peerID, e)
```
> يستدعي `invoke(peerID, e)` على ردّ النداء `onSessionFailed` إن لم يكن معدوماً. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:157]

```
158:             throw e
```
> يرمي الاستثناء `e`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:158]

```
159:         }
```
> إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:159]

```
160:     }
```
> إغلاق نطاق الدالة `processHandshakeMessage`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:160]

```
161: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:161]

```
162:     private fun isHandshakeStale(session: NoiseSession, nowMs: Long): Boolean {
```
> يُعرّف الدالة الخاصة `isHandshakeStale` (هل المصافحة قديمة) التي تقبل `session` من النوع `NoiseSession` و`nowMs` من النوع `Long` وتعيد `Boolean`، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:162]

```
163:         val lastActivity = session.getLastHandshakeActivityMs() ?: session.getHandshakeStartMs()
```
> يُعرّف متغيراً ثابتاً `lastActivity` (آخر نشاط) ويضبط قيمته بنتيجة `session.getLastHandshakeActivityMs()`، وإن كانت معدومة فبنتيجة `session.getHandshakeStartMs()`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:163]

```
164:         if (lastActivity == null) return false
```
> يبدأ شرط `if`: إذا كانت `lastActivity` تساوي `null` يعيد `false`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:164]

```
165:         return (nowMs - lastActivity) > HANDSHAKE_TIMEOUT_MS
```
> يعيد نتيجة المقارنة: هل الفرق `(nowMs - lastActivity)` أكبر من `HANDSHAKE_TIMEOUT_MS`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:165]

```
166:     }
```
> إغلاق نطاق الدالة `isHandshakeStale`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:166]

```
167:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:167]

```
168:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:168]

```
169:      * SIMPLIFIED: Encrypt data
```
> تعليق: مُبسَّط: تشفير البيانات. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:169]

```
170:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:170]

```
171:     fun encrypt(data: ByteArray, peerID: String): ByteArray {
```
> يُعرّف الدالة `encrypt` (شفِّر) التي تقبل `data` من النوع `ByteArray` و`peerID` من النوع `String` وتعيد `ByteArray`، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:171]

```
172:         val session = getSession(peerID) ?: throw IllegalStateException("No session found for $peerID")
```
> يُعرّف متغيراً ثابتاً `session` ويضبط قيمته بنتيجة `getSession(peerID)`، وإن كانت معدومة يرمي `IllegalStateException` بالنص "لا جلسة موجودة لـ $peerID". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:172]

```
173:         if (!session.isEstablished()) {
```
> يبدأ شرط `if` يتحقق أنّ `session.isEstablished()` تعيد خطأً. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:173]

```
174:             throw IllegalStateException("Session not established with $peerID")
```
> يرمي `IllegalStateException` بالنص "الجلسة غير مؤسَّسة مع $peerID". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:174]

```
175:         }
```
> إغلاق نطاق شرط `if`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:175]

```
176:         return session.encrypt(data)
```
> يعيد نتيجة `session.encrypt(data)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:176]

```
177:     }
```
> إغلاق نطاق الدالة `encrypt`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:177]

```
178:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:178]

```
179:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:179]

```
180:      * SIMPLIFIED: Decrypt data
```
> تعليق: مُبسَّط: فكّ تشفير البيانات. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:180]

```
181:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:181]

```
182:     fun decrypt(encryptedData: ByteArray, peerID: String): ByteArray {
```
> يُعرّف الدالة `decrypt` (فُكّ التشفير) التي تقبل `encryptedData` من النوع `ByteArray` و`peerID` من النوع `String` وتعيد `ByteArray`، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:182]

```
183:         val session = getSession(peerID)
```
> يُعرّف متغيراً ثابتاً `session` ويضبط قيمته بنتيجة `getSession(peerID)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:183]

```
184:         if (session == null) {
```
> يبدأ شرط `if` يتحقق أنّ `session` يساوي `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:184]

```
185:             Log.e(TAG, "No session found for $peerID when trying to decrypt")
```
> يستدعي `Log.e` للتسجيل بالوسم `TAG` والنص "لا جلسة موجودة لـ $peerID عند محاولة فك التشفير". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:185]

```
186:             throw IllegalStateException("No session found for $peerID")
```
> يرمي `IllegalStateException` بالنص "لا جلسة موجودة لـ $peerID". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:186]

```
187:         }
```
> إغلاق نطاق شرط `if (session == null)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:187]

```
188:         if (!session.isEstablished()) {
```
> يبدأ شرط `if` يتحقق أنّ `session.isEstablished()` تعيد خطأً. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:188]

```
189:             Log.e(TAG, "Session not established with $peerID when trying to decrypt")
```
> يستدعي `Log.e` للتسجيل بالوسم `TAG` والنص "الجلسة غير مؤسَّسة مع $peerID عند محاولة فك التشفير". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:189]

```
190:             throw IllegalStateException("Session not established with $peerID")
```
> يرمي `IllegalStateException` بالنص "الجلسة غير مؤسَّسة مع $peerID". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:190]

```
191:         }
```
> إغلاق نطاق شرط `if (!session.isEstablished())`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:191]

```
192:         return session.decrypt(encryptedData)
```
> يعيد نتيجة `session.decrypt(encryptedData)`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:192]

```
193:     }
```
> إغلاق نطاق الدالة `decrypt`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:193]

```
194:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:194]

```
195:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:195]

```
196:      * Check if session is established with peer
```
> تعليق: تحقّق إن كانت الجلسة مؤسَّسة مع النظير. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:196]

```
197:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:197]

```
198:     fun hasEstablishedSession(peerID: String): Boolean {
```
> يُعرّف الدالة `hasEstablishedSession` (هل لها جلسة مؤسَّسة) التي تقبل `peerID` من النوع `String` وتعيد `Boolean`، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:198]

```
199:         val hasSession = getSession(peerID)?.isEstablished() ?: false
```
> يُعرّف متغيراً ثابتاً `hasSession` ويضبط قيمته بنتيجة `isEstablished()` على نتيجة `getSession(peerID)` إن لم تكن معدومة، وإلا `false`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:199]

```
200:         Log.d(TAG, "hasEstablishedSession($peerID): $hasSession")
```
> يستدعي `Log.d` للتسجيل بالوسم `TAG` والنص "hasEstablishedSession($peerID): $hasSession". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:200]

```
201:         return hasSession
```
> يعيد القيمة `hasSession`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:201]

```
202:     }
```
> إغلاق نطاق الدالة `hasEstablishedSession`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:202]

```
203:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:203]

```
204:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:204]

```
205:      * Get session state for a peer (for UI state display)
```
> تعليق: احصل على حالة الجلسة لنظير (لعرض حالة واجهة المستخدم). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:205]

```
206:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:206]

```
207:     fun getSessionState(peerID: String): NoiseSession.NoiseSessionState {
```
> يُعرّف الدالة `getSessionState` (احصل على حالة الجلسة) التي تقبل `peerID` من النوع `String` وتعيد `NoiseSession.NoiseSessionState`، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:207]

```
208:         return getSession(peerID)?.getState() ?: NoiseSession.NoiseSessionState.Uninitialized
```
> يعيد نتيجة `getState()` على نتيجة `getSession(peerID)` إن لم تكن معدومة، وإلا القيمة `NoiseSession.NoiseSessionState.Uninitialized` (غير مُهيّأة). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:208]

```
209:     }
```
> إغلاق نطاق الدالة `getSessionState`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:209]

```
210:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:210]

```
211:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:211]

```
212:      * Get remote static public key for a peer (if session established)
```
> تعليق: احصل على المفتاح العام الثابت البعيد لنظير (إن كانت الجلسة مؤسَّسة). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:212]

```
213:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:213]

```
214:     fun getRemoteStaticKey(peerID: String): ByteArray? {
```
> يُعرّف الدالة `getRemoteStaticKey` (احصل على المفتاح الثابت البعيد) التي تقبل `peerID` من النوع `String` وتعيد `ByteArray` قابلاً للإبطال، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:214]

```
215:         return getSession(peerID)?.getRemoteStaticPublicKey()
```
> يعيد نتيجة `getRemoteStaticPublicKey()` على نتيجة `getSession(peerID)` إن لم تكن معدومة، وإلا `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:215]

```
216:     }
```
> إغلاق نطاق الدالة `getRemoteStaticKey`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:216]

```
217:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:217]

```
218:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:218]

```
219:      * Get handshake hash for channel binding (if session established)
```
> تعليق: احصل على تجزئة المصافحة لربط القناة (إن كانت الجلسة مؤسَّسة). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:219]

```
220:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:220]

```
221:     fun getHandshakeHash(peerID: String): ByteArray? {
```
> يُعرّف الدالة `getHandshakeHash` (احصل على تجزئة المصافحة) التي تقبل `peerID` من النوع `String` وتعيد `ByteArray` قابلاً للإبطال، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:221]

```
222:         return getSession(peerID)?.getHandshakeHash()
```
> يعيد نتيجة `getHandshakeHash()` على نتيجة `getSession(peerID)` إن لم تكن معدومة، وإلا `null`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:222]

```
223:     }
```
> إغلاق نطاق الدالة `getHandshakeHash`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:223]

```
224:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:224]

```
225:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:225]

```
226:      * Get sessions that need rekeying based on time or message count
```
> تعليق: احصل على الجلسات التي تحتاج إعادة تمفتُح بناءً على الوقت أو عدد الرسائل. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:226]

```
227:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:227]

```
228:     fun getSessionsNeedingRekey(): List<String> {
```
> يُعرّف الدالة `getSessionsNeedingRekey` (احصل على الجلسات المحتاجة لإعادة التمفتُح) التي لا تقبل وسائط وتعيد `List<String>`، وتفتح جسمها. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:228]

```
229:         return sessions.entries
```
> يبدأ تعبير الإعادة على مجموعة مدخلات الخريطة `sessions.entries`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:229]

```
230:             .filter { (_, session) -> 
```
> يستدعي `filter` (رشِّح) على المدخلات بدالة لمدا تتجاهل المفتاح وتسمّي القيمة `session`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:230]

```
231:                 session.isEstablished() && session.needsRekey()
```
> شرط الترشيح: أنّ `session.isEstablished()` تعيد صحيحاً و`session.needsRekey()` (هل تحتاج إعادة تمفتُح) تعيد صحيحاً. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:231]

```
232:             }
```
> إغلاق نطاق دالة لمدا الخاصة بـ `filter`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:232]

```
233:             .map { it.key }
```
> يستدعي `map` (حوِّل) لإعادة مفتاح كل مدخل عبر `it.key`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:233]

```
234:     }
```
> إغلاق نطاق الدالة `getSessionsNeedingRekey`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:234]

```
235:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:235]

```
236:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:236]

```
237:      * Get debug information
```
> تعليق: احصل على معلومات التصحيح. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:237]

```
238:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:238]

```
239:     fun getDebugInfo(): String = buildString {
```
> يُعرّف الدالة `getDebugInfo` (احصل على معلومات التصحيح) التي تعيد `String` ويضبط جسمها بتعبير واحد هو استدعاء `buildString` (ابنِ نصاً) مع دالة لمدا. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:239]

```
240:         appendLine("=== Noise Session Manager Debug ===")
```
> يستدعي `appendLine` لإلحاق السطر "=== Noise Session Manager Debug ===". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:240]

```
241:         appendLine("Active sessions: ${sessions.size}")
```
> يستدعي `appendLine` لإلحاق السطر "Active sessions: ${sessions.size}" مع عدد عناصر الخريطة `sessions`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:241]

```
242:         appendLine("")
```
> يستدعي `appendLine` لإلحاق سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:242]

```
243:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:243]

```
244:         if (sessions.isNotEmpty()) {
```
> يبدأ شرط `if` يتحقق أنّ `sessions.isNotEmpty()` (ليست فارغة) تعيد صحيحاً. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:244]

```
245:             appendLine("Sessions:")
```
> يستدعي `appendLine` لإلحاق السطر "Sessions:". [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:245]

```
246:             sessions.forEach { (peerID, session) ->
```
> يستدعي `forEach` (لكلٍّ) على الخريطة `sessions` بدالة لمدا تفكّك المدخل إلى `peerID` و`session`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:246]

```
247:                 appendLine("  $peerID: ${session.getState()}")
```
> يستدعي `appendLine` لإلحاق السطر "  $peerID: ${session.getState()}" مع حالة الجلسة. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:247]

```
248:             }
```
> إغلاق نطاق دالة لمدا الخاصة بـ `forEach`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:248]

```
249:         }
```
> إغلاق نطاق شرط `if (sessions.isNotEmpty())`. [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:249]

```
250:     }
```
> إغلاق نطاق دالة لمدا الخاصة بـ `buildString` (وبه ينتهي جسم الدالة `getDebugInfo`). [app/src/main/java/com/bitchat/android/noise/NoiseSessionManager.kt:250]
