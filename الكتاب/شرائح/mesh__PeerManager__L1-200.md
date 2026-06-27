# شريحة — app/src/main/java/com/bitchat/android/mesh/PeerManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.mesh
```
> يعرّف اسم الحزمة (package) للملف بأنها com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:2]

```
3: import android.util.Log
```
> يستورد صنف السجل (Log) من حزمة android.util. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:3]

```
4: import kotlinx.coroutines.*
```
> يستورد كل عناصر حزمة الكوروتينات (coroutines) من kotlinx.coroutines. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:4]

```
5: import java.util.concurrent.ConcurrentHashMap
```
> يستورد صنف خريطة التجزئة المتزامنة (ConcurrentHashMap) من java.util.concurrent. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:5]

```
6: import java.util.concurrent.CopyOnWriteArrayList
```
> يستورد صنف قائمة النسخ-عند-الكتابة (CopyOnWriteArrayList) من java.util.concurrent. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:6]

```
7: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:7]

```
8: /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:8]

```
9:  * Peer information structure with verification status
```
> تعليق: بنية معلومات النِّدّ (peer) مع حالة التحقّق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:9]

```
10:  * Compatible with iOS PeerInfo structure
```
> تعليق: متوافقة مع بنية PeerInfo في نظام iOS. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:10]

```
11:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:11]

```
12: data class PeerInfo(
```
> يعرّف صنف بيانات (data class) باسم معلومات-النِّدّ (PeerInfo) ويفتح قائمة معاملات الباني. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:12]

```
13:     val id: String,
```
> يعرّف خاصية ثابتة باسم المعرّف (id) من نوع نص (String). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:13]

```
14:     var nickname: String,
```
> يعرّف خاصية متغيّرة باسم الاسم-المستعار (nickname) من نوع نص (String). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:14]

```
15:     var isConnected: Boolean,
```
> يعرّف خاصية متغيّرة باسم هل-متّصل (isConnected) من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:15]

```
16:     var isDirectConnection: Boolean,
```
> يعرّف خاصية متغيّرة باسم هل-اتصال-مباشر (isDirectConnection) من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:16]

```
17:     var noisePublicKey: ByteArray?,
```
> يعرّف خاصية متغيّرة باسم مفتاح-نويز-العام (noisePublicKey) من نوع مصفوفة بايتات (ByteArray) قابلة للقيمة الفارغة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:17]

```
18:     var signingPublicKey: ByteArray?,      // NEW: Ed25519 public key for verification
```
> يعرّف خاصية متغيّرة باسم مفتاح-التوقيع-العام (signingPublicKey) من نوع مصفوفة بايتات قابلة للقيمة الفارغة، مع تعليق: جديد: مفتاح Ed25519 العام للتحقّق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:18]

```
19:     var isVerifiedNickname: Boolean,       // NEW: Verification status flag
```
> يعرّف خاصية متغيّرة باسم هل-الاسم-المستعار-موثّق (isVerifiedNickname) من نوع منطقي، مع تعليق: جديد: راية حالة التحقّق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:19]

```
20:     val lastSeen: Long  // Using Long instead of Date for simplicity
```
> يعرّف خاصية ثابتة باسم آخر-ظهور (lastSeen) من نوع عدد طويل (Long)، مع تعليق: استعمال Long بدلاً من Date للتبسيط. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:20]

```
21: ) {
```
> يغلق قائمة معاملات الباني ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:21]

```
22:     override fun equals(other: Any?): Boolean {
```
> يعيد تعريف (override) الدالة equals التي تأخذ معاملاً other من نوع Any قابل للفراغ وتعيد قيمة منطقية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:22]

```
23:         if (this === other) return true
```
> إذا كان هذا الكائن هو ذاته الكائن other (تطابق مرجعي) يعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:23]

```
24:         if (javaClass != other?.javaClass) return false
```
> إذا اختلف صنف جافا (javaClass) لهذا الكائن عن صنف الكائن other يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:24]

```
25:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:25]

```
26:         other as PeerInfo
```
> يحوّل الكائن other إلى نوع PeerInfo بإسناد التحويل (cast). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:26]

```
27:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:27]

```
28:         if (id != other.id) return false
```
> إذا اختلف المعرّف (id) عن معرّف الكائن other يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:28]

```
29:         if (nickname != other.nickname) return false
```
> إذا اختلف الاسم المستعار عن اسم الكائن other المستعار يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:29]

```
30:         if (isConnected != other.isConnected) return false
```
> إذا اختلفت قيمة هل-متّصل عن قيمتها في الكائن other يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:30]

```
31:         if (isDirectConnection != other.isDirectConnection) return false
```
> إذا اختلفت قيمة هل-اتصال-مباشر عن قيمتها في الكائن other يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:31]

```
32:         if (noisePublicKey != null) {
```
> إذا كان مفتاح-نويز-العام غير فارغ يفتح كتلة شرطية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:32]

```
33:             if (other.noisePublicKey == null) return false
```
> إذا كان مفتاح-نويز-العام للكائن other فارغاً يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:33]

```
34:             if (!noisePublicKey.contentEquals(other.noisePublicKey)) return false
```
> إذا لم يتطابق محتوى مفتاح-نويز-العام مع محتوى مفتاح الكائن other بدالة contentEquals يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:34]

```
35:         } else if (other.noisePublicKey != null) return false
```
> وإلّا إذا كان مفتاح-نويز-العام للكائن other غير فارغ يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:35]

```
36:         if (signingPublicKey != null) {
```
> إذا كان مفتاح-التوقيع-العام غير فارغ يفتح كتلة شرطية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:36]

```
37:             if (other.signingPublicKey == null) return false
```
> إذا كان مفتاح-التوقيع-العام للكائن other فارغاً يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:37]

```
38:             if (!signingPublicKey.contentEquals(other.signingPublicKey)) return false
```
> إذا لم يتطابق محتوى مفتاح-التوقيع-العام مع محتوى مفتاح الكائن other بدالة contentEquals يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:38]

```
39:         } else if (other.signingPublicKey != null) return false
```
> وإلّا إذا كان مفتاح-التوقيع-العام للكائن other غير فارغ يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:39]

```
40:         if (isVerifiedNickname != other.isVerifiedNickname) return false
```
> إذا اختلفت قيمة هل-الاسم-المستعار-موثّق عن قيمتها في الكائن other يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:40]

```
41:         if (lastSeen != other.lastSeen) return false
```
> إذا اختلفت قيمة آخر-ظهور عن قيمتها في الكائن other يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:41]

```
42:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:42]

```
43:         return true
```
> يعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:43]

```
44:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:44]

```
45:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:45]

```
46:     override fun hashCode(): Int {
```
> يعيد تعريف الدالة hashCode التي تعيد قيمة عددية صحيحة (Int). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:46]

```
47:         var result = id.hashCode()
```
> يعرّف متغيّراً باسم result ويسند إليه رمز التجزئة (hashCode) للمعرّف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:47]

```
48:         result = 31 * result + nickname.hashCode()
```
> يسند إلى result حاصل ضرب 31 في result الحالي زائد رمز تجزئة الاسم المستعار. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:48]

```
49:         result = 31 * result + isConnected.hashCode()
```
> يسند إلى result حاصل ضرب 31 في result الحالي زائد رمز تجزئة قيمة هل-متّصل. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:49]

```
50:         result = 31 * result + isDirectConnection.hashCode()
```
> يسند إلى result حاصل ضرب 31 في result الحالي زائد رمز تجزئة قيمة هل-اتصال-مباشر. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:50]

```
51:         result = 31 * result + (noisePublicKey?.contentHashCode() ?: 0)
```
> يسند إلى result حاصل ضرب 31 في result الحالي زائد رمز تجزئة محتوى مفتاح-نويز-العام أو صفر إن كان فارغاً. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:51]

```
52:         result = 31 * result + (signingPublicKey?.contentHashCode() ?: 0)
```
> يسند إلى result حاصل ضرب 31 في result الحالي زائد رمز تجزئة محتوى مفتاح-التوقيع-العام أو صفر إن كان فارغاً. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:52]

```
53:         result = 31 * result + isVerifiedNickname.hashCode()
```
> يسند إلى result حاصل ضرب 31 في result الحالي زائد رمز تجزئة قيمة هل-الاسم-المستعار-موثّق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:53]

```
54:         result = 31 * result + lastSeen.hashCode()
```
> يسند إلى result حاصل ضرب 31 في result الحالي زائد رمز تجزئة قيمة آخر-ظهور. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:54]

```
55:         return result
```
> يعيد قيمة result. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:55]

```
56:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:56]

```
57: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:57]

```
58: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:58]

```
59: /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:59]

```
60:  * Manages active peers, nicknames, RSSI tracking, and peer fingerprints
```
> تعليق: يدير الأنداد النشطين والأسماء المستعارة وتتبّع قوة الإشارة (RSSI) وبصمات الأنداد. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:60]

```
61:  * Extracted from BluetoothMeshService for better separation of concerns
```
> تعليق: مُستخرَج من خدمة شبكة البلوتوث المتشابكة (BluetoothMeshService) لفصل أفضل للاهتمامات. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:61]

```
62:  * 
```
> تعليق: سطر فارغ ضمن التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:62]

```
63:  * Now includes centralized peer fingerprint management via PeerFingerprintManager singleton
```
> تعليق: يتضمّن الآن إدارة مركزية لبصمات الأنداد عبر مفردة مدير-بصمات-الأنداد (PeerFingerprintManager). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:63]

```
64:  * and support for signed announcement verification
```
> تعليق: ودعماً للتحقّق من الإعلان الموقّع. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:64]

```
65:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:65]

```
66: class PeerManager {
```
> يعرّف صنفاً باسم مدير-الأنداد (PeerManager) ويفتح جسمه. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:66]

```
67:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:67]

```
68:     companion object {
```
> يفتح كائن المرافقة (companion object) للصنف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:68]

```
69:         private const val TAG = "PeerManager"
```
> يعرّف ثابتاً خاصاً باسم TAG وقيمته النص "PeerManager". [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:69]

```
70:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:70]

```
71: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:71]

```
72:     // Centralized timeout from AppConstants
```
> تعليق: مهلة مركزية من ثوابت التطبيق (AppConstants). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:72]

```
73:     private val stalePeerTimeoutMs: Long = com.bitchat.android.util.AppConstants.Mesh.STALE_PEER_TIMEOUT_MS
```
> يعرّف خاصية خاصة ثابتة باسم مهلة-الند-البائت بالمللي ثانية (stalePeerTimeoutMs) من نوع Long ويسند إليها قيمة الثابت STALE_PEER_TIMEOUT_MS من AppConstants.Mesh. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:73]

```
74:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:74]

```
75:     // Peer tracking data - enhanced with verification status
```
> تعليق: بيانات تتبّع الأنداد - مُعزَّزة بحالة التحقّق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:75]

```
76:     private val peers = ConcurrentHashMap<String, PeerInfo>() // peerID -> PeerInfo
```
> يعرّف خاصية خاصة ثابتة باسم الأنداد (peers) ويسند إليها خريطة تجزئة متزامنة مفاتيحها نصوص وقيمها PeerInfo، مع تعليق: معرّف-الند ⇐ PeerInfo. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:76]

```
77:     private val peerRSSI = ConcurrentHashMap<String, Int>()
```
> يعرّف خاصية خاصة ثابتة باسم قوة-إشارة-الند (peerRSSI) ويسند إليها خريطة تجزئة متزامنة مفاتيحها نصوص وقيمها أعداد صحيحة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:77]

```
78:     private val announcedPeers = CopyOnWriteArrayList<String>()
```
> يعرّف خاصية خاصة ثابتة باسم الأنداد-المُعلَنون (announcedPeers) ويسند إليها قائمة نسخ-عند-الكتابة من نصوص. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:78]

```
79:     private val announcedToPeers = CopyOnWriteArrayList<String>()
```
> يعرّف خاصية خاصة ثابتة باسم المُعلَن-إليهم-من-الأنداد (announcedToPeers) ويسند إليها قائمة نسخ-عند-الكتابة من نصوص. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:79]

```
80:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:80]

```
81:     // Legacy fields removed: use PeerInfo map exclusively
```
> تعليق: حُذِفت الحقول القديمة: استعمل خريطة PeerInfo حصراً. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:81]

```
82:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:82]

```
83:     // Centralized fingerprint management
```
> تعليق: إدارة مركزية للبصمات. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:83]

```
84:     private val fingerprintManager = PeerFingerprintManager.getInstance()
```
> يعرّف خاصية خاصة ثابتة باسم مدير-البصمات (fingerprintManager) ويسند إليها المثيل المُعاد من PeerFingerprintManager.getInstance(). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:84]

```
85:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:85]

```
86:     // Delegate for callbacks
```
> تعليق: مُفوَّض لردود النداء. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:86]

```
87:     var delegate: PeerManagerDelegate? = null
```
> يعرّف خاصية متغيّرة باسم مُفوَّض (delegate) من نوع PeerManagerDelegate قابل للفراغ وقيمته الابتدائية null. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:87]

```
88:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:88]

```
89:     // Callback to check if a peer is directly connected (injected by BluetoothMeshService)
```
> تعليق: ردّ نداء للتحقّق هل الند متّصل مباشرة (يُحقَن من قِبَل BluetoothMeshService). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:89]

```
90:     var isPeerDirectlyConnected: ((String) -> Boolean)? = null
```
> يعرّف خاصية متغيّرة باسم هل-الند-متّصل-مباشرة (isPeerDirectlyConnected) من نوع دالة تأخذ نصاً وتعيد منطقياً، قابلة للفراغ وقيمتها الابتدائية null. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:90]

```
91: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:91]

```
92:     // Coroutines
```
> تعليق: الكوروتينات. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:92]

```
93:     private val managerScope = CoroutineScope(Dispatchers.IO + SupervisorJob())
```
> يعرّف خاصية خاصة ثابتة باسم نطاق-المدير (managerScope) ويسند إليها نطاق كوروتين (CoroutineScope) مكوّناً من موزّع الإدخال/الإخراج (Dispatchers.IO) مع مهمة مُشرِفة (SupervisorJob). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:93]

```
94:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:94]

```
95:     init {
```
> يفتح كتلة التهيئة (init) للصنف. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:95]

```
96:         startPeriodicCleanup()
```
> يستدعي الدالة بدء-التنظيف-الدوري (startPeriodicCleanup). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:96]

```
97:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:97]

```
98: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:98]

```
99:     // MARK: - New PeerInfo-based methods
```
> تعليق: علامة: - دوال جديدة قائمة على PeerInfo. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:99]

```
100: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:100]

```
101:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:101]

```
102:      * Update peer information with verification data
```
> تعليق: تحديث معلومات الند ببيانات التحقّق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:102]

```
103:      * Similar to iOS updatePeer method
```
> تعليق: مشابه لدالة updatePeer في نظام iOS. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:103]

```
104:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:104]

```
105:     fun updatePeerInfo(
```
> يعرّف دالة باسم تحديث-معلومات-الند (updatePeerInfo) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:105]

```
106:         peerID: String,
```
> يعرّف معاملاً باسم معرّف-الند (peerID) من نوع نص. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:106]

```
107:         nickname: String,
```
> يعرّف معاملاً باسم الاسم-المستعار (nickname) من نوع نص. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:107]

```
108:         noisePublicKey: ByteArray,
```
> يعرّف معاملاً باسم مفتاح-نويز-العام (noisePublicKey) من نوع مصفوفة بايتات. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:108]

```
109:         signingPublicKey: ByteArray,
```
> يعرّف معاملاً باسم مفتاح-التوقيع-العام (signingPublicKey) من نوع مصفوفة بايتات. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:109]

```
110:         isVerified: Boolean
```
> يعرّف معاملاً باسم هل-موثّق (isVerified) من نوع منطقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:110]

```
111:     ): Boolean {
```
> يغلق قائمة المعاملات ويحدّد نوع القيمة المُعادة منطقياً ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:111]

```
112:         if (peerID == "unknown") return false
```
> إذا كان معرّف-الند يساوي النص "unknown" يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:112]

```
113: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:113]

```
114:         fun keysMatch(a: ByteArray?, b: ByteArray?): Boolean {
```
> يعرّف دالة محلّية باسم تطابق-المفاتيح (keysMatch) تأخذ معاملين a و b من نوع مصفوفة بايتات قابلة للفراغ وتعيد منطقياً وتفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:114]

```
115:             if (a == null && b == null) return true
```
> إذا كان a فارغاً و b فارغاً معاً يعيد القيمة true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:115]

```
116:             if (a == null || b == null) return false
```
> إذا كان a فارغاً أو b فارغاً يعيد القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:116]

```
117:             return a.contentEquals(b)
```
> يعيد نتيجة مقارنة محتوى a بمحتوى b بدالة contentEquals. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:117]

```
118:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:118]

```
119:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:119]

```
120:         val now = System.currentTimeMillis()
```
> يعرّف متغيّراً ثابتاً باسم الآن (now) ويسند إليه الوقت الحالي بالمللي ثانية من System.currentTimeMillis(). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:120]

```
121:         val existingPeer = peers[peerID]
```
> يعرّف متغيّراً ثابتاً باسم الند-الموجود (existingPeer) ويسند إليه القيمة المقابلة لمعرّف-الند من خريطة الأنداد. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:121]

```
122:         val isNewPeer = existingPeer == null
```
> يعرّف متغيّراً ثابتاً باسم هل-ند-جديد (isNewPeer) ويسند إليه نتيجة كون الند-الموجود فارغاً. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:122]

```
123:         val wasVerified = existingPeer?.isVerifiedNickname == true
```
> يعرّف متغيّراً ثابتاً باسم كان-موثّقاً (wasVerified) ويسند إليه نتيجة كون خاصية هل-الاسم-المستعار-موثّق للند-الموجود تساوي true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:123]

```
124:         val nicknameChanged = existingPeer != null && existingPeer.nickname != nickname
```
> يعرّف متغيّراً ثابتاً باسم تغيّر-الاسم-المستعار (nicknameChanged) ويسند إليه نتيجة أن الند-الموجود غير فارغ واسمه المستعار يختلف عن nickname. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:124]

```
125:         val noiseKeyChanged = existingPeer != null && !keysMatch(existingPeer.noisePublicKey, noisePublicKey)
```
> يعرّف متغيّراً ثابتاً باسم تغيّر-مفتاح-نويز (noiseKeyChanged) ويسند إليه نتيجة أن الند-الموجود غير فارغ ومفتاح-نويز-العام لديه لا يطابق noisePublicKey بحسب keysMatch. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:125]

```
126:         val signingKeyChanged = existingPeer != null && !keysMatch(existingPeer.signingPublicKey, signingPublicKey)
```
> يعرّف متغيّراً ثابتاً باسم تغيّر-مفتاح-التوقيع (signingKeyChanged) ويسند إليه نتيجة أن الند-الموجود غير فارغ ومفتاح-التوقيع-العام لديه لا يطابق signingPublicKey بحسب keysMatch. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:126]

```
127:         val connectedChanged = existingPeer != null && existingPeer.isConnected != true
```
> يعرّف متغيّراً ثابتاً باسم تغيّر-الاتصال (connectedChanged) ويسند إليه نتيجة أن الند-الموجود غير فارغ وخاصية هل-متّصل لديه لا تساوي true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:127]

```
128:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:128]

```
129:         // Update or create peer info
```
> تعليق: تحديث أو إنشاء معلومات الند. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:129]

```
130:         val peerInfo = PeerInfo(
```
> يعرّف متغيّراً ثابتاً باسم معلومات-الند (peerInfo) ويسند إليه مثيل PeerInfo بفتح قائمة وسائطه. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:130]

```
131:             id = peerID,
```
> يسند للوسيط id قيمة معرّف-الند. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:131]

```
132:             nickname = nickname,
```
> يسند للوسيط nickname قيمة الاسم المستعار. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:132]

```
133:             isConnected = true,
```
> يسند للوسيط isConnected القيمة true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:133]

```
134:             isDirectConnection = existingPeer?.isDirectConnection ?: false,
```
> يسند للوسيط isDirectConnection قيمة هل-اتصال-مباشر للند-الموجود أو false إن كان فارغاً. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:134]

```
135:             noisePublicKey = noisePublicKey,
```
> يسند للوسيط noisePublicKey قيمة مفتاح-نويز-العام الممرَّر. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:135]

```
136:             signingPublicKey = signingPublicKey,
```
> يسند للوسيط signingPublicKey قيمة مفتاح-التوقيع-العام الممرَّر. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:136]

```
137:             isVerifiedNickname = isVerified,
```
> يسند للوسيط isVerifiedNickname قيمة هل-موثّق الممرَّرة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:137]

```
138:             lastSeen = now
```
> يسند للوسيط lastSeen قيمة الآن. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:138]

```
139:         )
```
> يغلق قائمة وسائط باني PeerInfo. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:139]

```
140:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:140]

```
141:         peers[peerID] = peerInfo
```
> يسند مثيل معلومات-الند إلى موضع معرّف-الند في خريطة الأنداد. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:141]

```
142:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:142]

```
143:         // Update derived state only
```
> تعليق: تحديث الحالة المُشتقّة فقط. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:143]

```
144:         // No legacy maps; peers map is the single source of truth
```
> تعليق: لا خرائط قديمة؛ خريطة الأنداد هي مصدر الحقيقة الوحيد. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:144]

```
145:         // Maintain announcedPeers for first-time announce semantics
```
> تعليق: الحفاظ على announcedPeers لدلالات الإعلان لأول مرة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:145]

```
146:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:146]

```
147:         val shouldNotify = when {
```
> يعرّف متغيّراً ثابتاً باسم ينبغي-الإشعار (shouldNotify) ويسند إليه نتيجة تعبير when ويفتح فروعه. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:147]

```
148:             isNewPeer && isVerified -> true
```
> إذا كان ند-جديد وموثّقاً يعيد الفرع القيمة true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:148]

```
149:             wasVerified != isVerified -> true
```
> إذا اختلفت قيمة كان-موثّقاً عن هل-موثّق يعيد الفرع القيمة true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:149]

```
150:             nicknameChanged || noiseKeyChanged || signingKeyChanged || connectedChanged -> true
```
> إذا تغيّر الاسم المستعار أو مفتاح نويز أو مفتاح التوقيع أو الاتصال يعيد الفرع القيمة true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:150]

```
151:             else -> false
```
> وإلّا يعيد الفرع القيمة false. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:151]

```
152:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:152]

```
153: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:153]

```
154:         if (isNewPeer && isVerified) {
```
> إذا كان ند-جديد وموثّقاً يفتح كتلة شرطية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:154]

```
155:             announcedPeers.add(peerID)
```
> يضيف معرّف-الند إلى قائمة الأنداد-المُعلَنين. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:155]

```
156:             Log.d(TAG, "🆕 New verified peer: $nickname ($peerID)")
```
> يسجّل رسالة تصحيح (Log.d) بالوسم TAG ونصّها: "🆕 New verified peer:" متبوعاً بالاسم المستعار ومعرّف-الند. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:156]

```
157:         } else if (isVerified) {
```
> وإلّا إذا كان موثّقاً يفتح كتلة شرطية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:157]

```
158:             Log.d(TAG, "🔄 Updated verified peer: $nickname ($peerID)")
```
> يسجّل رسالة تصحيح بالوسم TAG ونصّها: "🔄 Updated verified peer:" متبوعاً بالاسم المستعار ومعرّف-الند. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:158]

```
159:         } else {
```
> وإلّا يفتح كتلة بديلة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:159]

```
160:             Log.d(TAG, "⚠️ Unverified peer announcement from: $nickname ($peerID)")
```
> يسجّل رسالة تصحيح بالوسم TAG ونصّها: "⚠️ Unverified peer announcement from:" متبوعاً بالاسم المستعار ومعرّف-الند. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:160]

```
161:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:161]

```
162: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:162]

```
163:         if (shouldNotify) {
```
> إذا كانت قيمة ينبغي-الإشعار صحيحة يفتح كتلة شرطية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:163]

```
164:             notifyPeerListUpdate()
```
> يستدعي الدالة إشعار-تحديث-قائمة-الأنداد (notifyPeerListUpdate). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:164]

```
165:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:165]

```
166:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:166]

```
167:         return isNewPeer && isVerified
```
> يعيد نتيجة كون الند جديداً وموثّقاً معاً. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:167]

```
168:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:168]

```
169: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:169]

```
170:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:170]

```
171:      * Get peer info with dynamic direct connection status
```
> تعليق: الحصول على معلومات الند مع حالة اتصال مباشر ديناميكية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:171]

```
172:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:172]

```
173:     fun getPeerInfo(peerID: String): PeerInfo? {
```
> يعرّف دالة باسم الحصول-على-معلومات-الند (getPeerInfo) تأخذ معرّف-الند نصاً وتعيد PeerInfo قابلاً للفراغ وتفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:173]

```
174:         return peers[peerID]?.let { info ->
```
> يعيد ناتج تطبيق let على القيمة المقابلة لمعرّف-الند من خريطة الأنداد مسمّياً إياها info ويفتح كتلة let. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:174]

```
175:             // Dynamically check direct connection status from ConnectionManager
```
> تعليق: التحقّق ديناميكياً من حالة الاتصال المباشر من مدير الاتصال (ConnectionManager). [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:175]

```
176:             val isDirect = isPeerDirectlyConnected?.invoke(peerID) ?: false
```
> يعرّف متغيّراً ثابتاً باسم هل-مباشر (isDirect) ويسند إليه نتيجة استدعاء دالة هل-الند-متّصل-مباشرة مع معرّف-الند أو false إن كانت فارغة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:176]

```
177:             if (info.isDirectConnection != isDirect) {
```
> إذا اختلفت خاصية هل-اتصال-مباشر في info عن قيمة هل-مباشر يفتح كتلة شرطية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:177]

```
178:                 info.copy(isDirectConnection = isDirect)
```
> ينتج نسخة من info بدالة copy مع تعيين خاصية isDirectConnection إلى قيمة هل-مباشر. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:178]

```
179:             } else {
```
> وإلّا يفتح كتلة بديلة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:179]

```
180:                 info
```
> ينتج القيمة info كما هي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:180]

```
181:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:181]

```
182:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:182]

```
183:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:183]

```
184: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:184]

```
185:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:185]

```
186:      * Check if peer is verified
```
> تعليق: التحقّق هل الند موثّق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:186]

```
187:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:187]

```
188:     fun isPeerVerified(peerID: String): Boolean {
```
> يعرّف دالة باسم هل-الند-موثّق (isPeerVerified) تأخذ معرّف-الند نصاً وتعيد منطقياً وتفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:188]

```
189:         return peers[peerID]?.isVerifiedNickname == true
```
> يعيد نتيجة كون خاصية هل-الاسم-المستعار-موثّق للقيمة المقابلة لمعرّف-الند في خريطة الأنداد تساوي true. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:189]

```
190:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:190]

```
191: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:191]

```
192:     /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:192]

```
193:      * Get all verified peers with dynamic direct connection status
```
> تعليق: الحصول على كل الأنداد الموثّقين مع حالة اتصال مباشر ديناميكية. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:193]

```
194:      */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:194]

```
195:     fun getVerifiedPeers(): Map<String, PeerInfo> {
```
> يعرّف دالة باسم الحصول-على-الأنداد-الموثّقين (getVerifiedPeers) تعيد خريطة مفاتيحها نصوص وقيمها PeerInfo وتفتح جسمها. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:195]

```
196:         return peers.filterValues { it.isVerifiedNickname }.mapValues { (_, info) ->
```
> يعيد خريطة الأنداد بعد تصفية القيم التي خاصيتها هل-الاسم-المستعار-موثّق صحيحة بدالة filterValues ثم تحويل قيمها بدالة mapValues مسمّياً القيمة info ويفتح كتلة التحويل. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:196]

```
197:             val isDirect = isPeerDirectlyConnected?.invoke(info.id) ?: false
```
> يعرّف متغيّراً ثابتاً باسم هل-مباشر (isDirect) ويسند إليه نتيجة استدعاء دالة هل-الند-متّصل-مباشرة مع معرّف info أو false إن كانت فارغة. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:197]

```
198:             if (info.isDirectConnection != isDirect) info.copy(isDirectConnection = isDirect) else info
```
> إذا اختلفت خاصية هل-اتصال-مباشر في info عن قيمة هل-مباشر ينتج نسخة من info بتعيين isDirectConnection إلى هل-مباشر وإلّا ينتج info كما هي. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:198]

```
199:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:199]

```
200:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/PeerManager.kt:200]
