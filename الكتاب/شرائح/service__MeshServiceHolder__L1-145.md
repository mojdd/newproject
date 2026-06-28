# شريحة — app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt (الأسطر 1–145)

```
1: package com.bitchat.android.service
```
> يُعرّف انتماء الملف إلى الحزمة (package) المسمّاة com.bitchat.android.service. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:2]

```
3: import android.content.Context
```
> يستورد الصنف Context من حزمة android.content. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:3]

```
4: import com.bitchat.android.mesh.BluetoothMeshService
```
> يستورد الصنف BluetoothMeshService (خدمة الشبكة المتشابكة عبر البلوتوث) من حزمة com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:4]

```
5: import com.bitchat.android.mesh.UnifiedMeshService
```
> يستورد الصنف UnifiedMeshService (خدمة الشبكة المتشابكة الموحَّدة) من حزمة com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:5]

```
6: import com.bitchat.android.model.RoutedPacket
```
> يستورد الصنف RoutedPacket (الرزمة المُوجَّهة) من حزمة com.bitchat.android.model. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:6]

```
7: import com.bitchat.android.protocol.BitchatPacket
```
> يستورد الصنف BitchatPacket (رزمة بِت‑شات) من حزمة com.bitchat.android.protocol. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:7]

```
8: import com.bitchat.android.sync.GossipSyncManager
```
> يستورد الصنف GossipSyncManager (مدير مزامنة الإشاعة) من حزمة com.bitchat.android.sync. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:9]

```
10: /**
```
> تعليق توثيقي: بداية كتلة توثيق (افتتاح تعليق متعدّد الأسطر). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:10]

```
11:  * Process-wide holder to share a single BluetoothMeshService instance
```
> تعليق: حامل على نطاق العملية كاملةً لمشاركة نسخة واحدة من BluetoothMeshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:11]

```
12:  * between the foreground service and UI (MainActivity/ViewModels).
```
> تعليق: بين الخدمة الأمامية وواجهة المستخدم (MainActivity/ViewModels). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:12]

```
13:  */
```
> تعليق: نهاية كتلة التوثيق (إغلاق التعليق متعدّد الأسطر). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:13]

```
14: object MeshServiceHolder {
```
> يُعلِن كائناً مفرداً (object) باسم MeshServiceHolder (حامل خدمة الشبكة المتشابكة) ويفتح نطاق جسمه. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:14]

```
15:     private const val TAG = "MeshServiceHolder"
```
> يُعرّف ثابتاً خاصاً (private const) باسم TAG قيمته السلسلة النصية "MeshServiceHolder". [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:15]

```
16:     @Volatile
```
> يضع الوسم التوضيحي @Volatile (متطاير) على العنصر التالي. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:16]

```
17:     var sharedGossipSyncManager: GossipSyncManager? = null
```
> يُعرّف متغيّراً (var) باسم sharedGossipSyncManager (مدير مزامنة الإشاعة المشترك) من النوع GossipSyncManager القابل للقيمة الفارغة، ويُهيّئه بقيمة null. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:17]

```
18:         private set
```
> يجعل دالّة الضبط (set) لهذا المتغيّر خاصةً (private). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:18]

```
19: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:19]

```
20:     private val activeGossipOwners = mutableSetOf<String>()
```
> يُعرّف قيمةً ثابتة خاصة (private val) باسم activeGossipOwners (مالكو الإشاعة النشطون) ويُهيّئها بمجموعة قابلة للتعديل (mutableSetOf) من نوع String فارغة. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:20]

```
21: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:21]

```
22:     @Synchronized
```
> يضع الوسم التوضيحي @Synchronized (متزامن) على الدالّة التالية. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:22]

```
23:     fun setGossipManager(
```
> يُعرّف دالّةً (fun) باسم setGossipManager (ضبط مدير الإشاعة) ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:23]

```
24:         mgr: GossipSyncManager,
```
> يُعرّف المعامل mgr من النوع GossipSyncManager. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:24]

```
25:         signer: (BitchatPacket) -> BitchatPacket
```
> يُعرّف المعامل signer (الموقِّع) من نوع دالّة تأخذ BitchatPacket وتُعيد BitchatPacket. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:25]

```
26:     ) {
```
> يُغلق قائمة المعاملات ويفتح جسم الدالّة. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:26]

```
27:         val previous = sharedGossipSyncManager
```
> يُعرّف قيمةً محلية (val) باسم previous (السابق) ويُسنِد إليها القيمة الحالية لـ sharedGossipSyncManager. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:27]

```
28:         if (previous !== mgr) {
```
> يبدأ شرطاً (if) يتحقق أنّ previous لا يساوي mgr بالمرجعية (عدم تطابق الكائن نفسه)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:28]

```
29:             try { previous?.stop() } catch (_: Exception) { }
```
> ضمن كتلة try يستدعي stop() على previous إن لم يكن null، ويلتقط أي Exception دون فعل. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:29]

```
30:         }
```
> إغلاق نطاق (كتلة الشرط if). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:30]

```
31:         sharedGossipSyncManager = mgr
```
> يُسنِد قيمة mgr إلى المتغيّر sharedGossipSyncManager. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:31]

```
32:         mgr.delegate = TransportGossipDelegate(signer)
```
> يضبط الخاصية delegate (المفوَّض) لـ mgr إلى نسخة جديدة من TransportGossipDelegate مُنشأة بالمعامل signer. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:32]

```
33:         if (activeGossipOwners.isNotEmpty()) {
```
> يبدأ شرطاً (if) يتحقق أنّ activeGossipOwners غير فارغة (isNotEmpty)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:33]

```
34:             mgr.start()
```
> يستدعي الدالّة start() على mgr. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:34]

```
35:         }
```
> إغلاق نطاق (كتلة الشرط if). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:35]

```
36:     }
```
> إغلاق نطاق (جسم الدالّة setGossipManager). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:36]

```
37: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:37]

```
38:     @Synchronized
```
> يضع الوسم التوضيحي @Synchronized (متزامن) على الدالّة التالية. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:38]

```
39:     fun startSharedGossip(owner: String) {
```
> يُعرّف دالّةً (fun) باسم startSharedGossip (بدء الإشاعة المشتركة) تأخذ المعامل owner (المالك) من النوع String، ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:39]

```
40:         val wasIdle = activeGossipOwners.isEmpty()
```
> يُعرّف قيمةً محلية (val) باسم wasIdle (كان خاملاً) ويُسنِد إليها نتيجة فحص أنّ activeGossipOwners فارغة (isEmpty). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:40]

```
41:         activeGossipOwners.add(owner)
```
> يُضيف owner إلى المجموعة activeGossipOwners. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:41]

```
42:         if (wasIdle) {
```
> يبدأ شرطاً (if) يتحقق أنّ wasIdle صحيح، ويفتح كتلته. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:42]

```
43:             sharedGossipSyncManager?.start()
```
> يستدعي start() على sharedGossipSyncManager إن لم يكن null. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:43]

```
44:         }
```
> إغلاق نطاق (كتلة الشرط if). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:44]

```
45:     }
```
> إغلاق نطاق (جسم الدالّة startSharedGossip). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:45]

```
46: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:46]

```
47:     @Synchronized
```
> يضع الوسم التوضيحي @Synchronized (متزامن) على الدالّة التالية. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:47]

```
48:     fun stopSharedGossip(owner: String) {
```
> يُعرّف دالّةً (fun) باسم stopSharedGossip (إيقاف الإشاعة المشتركة) تأخذ المعامل owner من النوع String، ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:48]

```
49:         activeGossipOwners.remove(owner)
```
> يُزيل owner من المجموعة activeGossipOwners. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:49]

```
50:         if (activeGossipOwners.isEmpty()) {
```
> يبدأ شرطاً (if) يتحقق أنّ activeGossipOwners فارغة (isEmpty)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:50]

```
51:             sharedGossipSyncManager?.stop()
```
> يستدعي stop() على sharedGossipSyncManager إن لم يكن null. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:51]

```
52:         }
```
> إغلاق نطاق (كتلة الشرط if). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:52]

```
53:     }
```
> إغلاق نطاق (جسم الدالّة stopSharedGossip). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:53]

```
54: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:54]

```
55:     private class TransportGossipDelegate(
```
> يُعلِن صنفاً داخلياً خاصاً (private class) باسم TransportGossipDelegate (مفوَّض إشاعة النقل) ويفتح قائمة معاملات بانِيه. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:55]

```
56:         private val signer: (BitchatPacket) -> BitchatPacket
```
> يُعرّف خاصيةً ثابتة خاصة (private val) باسم signer من نوع دالّة تأخذ BitchatPacket وتُعيد BitchatPacket. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:56]

```
57:     ) : GossipSyncManager.Delegate {
```
> يُغلق قائمة معاملات البانِي ويُعلِن أنّ الصنف يُحقّق الواجهة GossipSyncManager.Delegate، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:57]

```
58:         override fun sendPacket(packet: BitchatPacket) {
```
> يتجاوز (override) الدالّة sendPacket (إرسال رزمة) التي تأخذ المعامل packet من النوع BitchatPacket، ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:58]

```
59:             TransportBridgeService.broadcastFromLocal(RoutedPacket(packet))
```
> يستدعي الدالّة broadcastFromLocal (البثّ من المحلّي) على TransportBridgeService مُمرّراً RoutedPacket مُنشأة من packet. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:59]

```
60:         }
```
> إغلاق نطاق (جسم الدالّة sendPacket). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:60]

```
61: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:61]

```
62:         override fun sendPacketToPeer(peerID: String, packet: BitchatPacket) {
```
> يتجاوز (override) الدالّة sendPacketToPeer (إرسال رزمة إلى نِدّ) التي تأخذ peerID من النوع String وpacket من النوع BitchatPacket، ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:62]

```
63:             TransportBridgeService.sendToPeerFromLocal(peerID, packet)
```
> يستدعي الدالّة sendToPeerFromLocal (الإرسال إلى نِدّ من المحلّي) على TransportBridgeService مُمرّراً peerID وpacket. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:63]

```
64:         }
```
> إغلاق نطاق (جسم الدالّة sendPacketToPeer). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:65]

```
66:         override fun signPacketForBroadcast(packet: BitchatPacket): BitchatPacket {
```
> يتجاوز (override) الدالّة signPacketForBroadcast (توقيع رزمة للبثّ) التي تأخذ packet من النوع BitchatPacket وتُعيد BitchatPacket، ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:66]

```
67:             return signer(packet)
```
> يُعيد نتيجة استدعاء دالّة signer على packet. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:67]

```
68:         }
```
> إغلاق نطاق (جسم الدالّة signPacketForBroadcast). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:68]

```
69:     }
```
> إغلاق نطاق (جسم الصنف TransportGossipDelegate). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:69]

```
70: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:70]

```
71:     @Volatile
```
> يضع الوسم التوضيحي @Volatile (متطاير) على العنصر التالي. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:71]

```
72:     var meshService: BluetoothMeshService? = null
```
> يُعرّف متغيّراً (var) باسم meshService (خدمة الشبكة المتشابكة) من النوع BluetoothMeshService القابل للقيمة الفارغة، ويُهيّئه بقيمة null. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:72]

```
73:         private set
```
> يجعل دالّة الضبط (set) لهذا المتغيّر خاصةً (private). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:73]

```
74: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:74]

```
75:     @Volatile
```
> يضع الوسم التوضيحي @Volatile (متطاير) على العنصر التالي. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:75]

```
76:     var unifiedMeshService: UnifiedMeshService? = null
```
> يُعرّف متغيّراً (var) باسم unifiedMeshService (خدمة الشبكة المتشابكة الموحَّدة) من النوع UnifiedMeshService القابل للقيمة الفارغة، ويُهيّئه بقيمة null. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:76]

```
77:         private set
```
> يجعل دالّة الضبط (set) لهذا المتغيّر خاصةً (private). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:77]

```
78: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:78]

```
79:     @Synchronized
```
> يضع الوسم التوضيحي @Synchronized (متزامن) على الدالّة التالية. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:79]

```
80:     fun getOrCreate(context: Context): BluetoothMeshService {
```
> يُعرّف دالّةً (fun) باسم getOrCreate (الحصول أو الإنشاء) تأخذ context من النوع Context وتُعيد BluetoothMeshService، ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:80]

```
81:         val existing = meshService
```
> يُعرّف قيمةً محلية (val) باسم existing (القائم) ويُسنِد إليها القيمة الحالية لـ meshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:81]

```
82:         if (existing != null) {
```
> يبدأ شرطاً (if) يتحقق أنّ existing لا يساوي null، ويفتح كتلته. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:82]

```
83:             // If the existing instance is healthy, reuse it; otherwise, replace it.
```
> تعليق: إن كانت النسخة القائمة سليمة فأعد استخدامها؛ وإلّا فاستبدلها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:83]

```
84:             return try {
```
> يُعيد نتيجة كتلة try (تبدأ تعبير try يُستخدم كقيمة إرجاع)، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:84]

```
85:                 if (existing.isReusable()) {
```
> يبدأ شرطاً (if) يتحقق من نتيجة استدعاء isReusable() (قابل لإعادة الاستخدام) على existing، ويفتح كتلته. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:85]

```
86:                     android.util.Log.d(TAG, "Reusing existing BluetoothMeshService instance")
```
> يستدعي android.util.Log.d (سجلّ تصحيح) بالوسم TAG والرسالة "Reusing existing BluetoothMeshService instance". [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:86]

```
87:                     existing
```
> يُقيّم إلى existing كقيمة كتلة الشرط (تُعاد بوصفها قيمة تعبير try). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:87]

```
88:                 } else {
```
> يُغلق كتلة if ويفتح كتلة else. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:88]

```
89:                     android.util.Log.w(TAG, "Existing BluetoothMeshService not reusable; replacing with a fresh instance")
```
> يستدعي android.util.Log.w (سجلّ تحذير) بالوسم TAG والرسالة "Existing BluetoothMeshService not reusable; replacing with a fresh instance". [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:89]

```
90:                     // Best-effort stop before replacing
```
> تعليق: إيقاف بأقصى جهد ممكن قبل الاستبدال. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:90]

```
91:                     try { existing.stopServices() } catch (e: Exception) {
```
> ضمن كتلة try يستدعي stopServices() على existing، ويلتقط Exception في المتغيّر e ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:91]

```
92:                         android.util.Log.w(TAG, "Error while stopping non-reusable instance: ${e.message}")
```
> يستدعي android.util.Log.w (سجلّ تحذير) بالوسم TAG والرسالة "Error while stopping non-reusable instance: " مُدمَجاً فيها قيمة e.message. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:92]

```
93:                     }
```
> إغلاق نطاق (كتلة catch). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:93]

```
94:                     val created = BluetoothMeshService(context.applicationContext)
```
> يُعرّف قيمةً محلية (val) باسم created (المُنشأ) ويُسنِد إليها نسخة جديدة من BluetoothMeshService مُنشأة بـ context.applicationContext. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:94]

```
95:                     android.util.Log.i(TAG, "Created new BluetoothMeshService (replacement)")
```
> يستدعي android.util.Log.i (سجلّ معلومات) بالوسم TAG والرسالة "Created new BluetoothMeshService (replacement)". [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:95]

```
96:                     meshService = created
```
> يُسنِد created إلى المتغيّر meshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:96]

```
97:                     unifiedMeshService = null
```
> يُسنِد null إلى المتغيّر unifiedMeshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:97]

```
98:                     created
```
> يُقيّم إلى created كقيمة كتلة else (تُعاد بوصفها قيمة تعبير try). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:98]

```
99:                 }
```
> إغلاق نطاق (كتلة else). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:99]

```
100:             } catch (e: Exception) {
```
> يُغلق كتلة try ويلتقط Exception في المتغيّر e ويفتح كتلة المعالجة. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:100]

```
101:                 android.util.Log.e(TAG, "Error checking service reusability; creating new instance: ${e.message}")
```
> يستدعي android.util.Log.e (سجلّ خطأ) بالوسم TAG والرسالة "Error checking service reusability; creating new instance: " مُدمَجاً فيها قيمة e.message. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:101]

```
102:                 val created = BluetoothMeshService(context.applicationContext)
```
> يُعرّف قيمةً محلية (val) باسم created ويُسنِد إليها نسخة جديدة من BluetoothMeshService مُنشأة بـ context.applicationContext. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:102]

```
103:                 meshService = created
```
> يُسنِد created إلى المتغيّر meshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:103]

```
104:                 unifiedMeshService = null
```
> يُسنِد null إلى المتغيّر unifiedMeshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:104]

```
105:                 created
```
> يُقيّم إلى created كقيمة كتلة catch (تُعاد بوصفها قيمة تعبير try). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:105]

```
106:             }
```
> إغلاق نطاق (كتلة catch وتعبير try). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:106]

```
107:         }
```
> إغلاق نطاق (كتلة الشرط if عند السطر 82). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:107]

```
108:         val created = BluetoothMeshService(context.applicationContext)
```
> يُعرّف قيمةً محلية (val) باسم created ويُسنِد إليها نسخة جديدة من BluetoothMeshService مُنشأة بـ context.applicationContext. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:108]

```
109:         android.util.Log.i(TAG, "Created new BluetoothMeshService (no existing instance)")
```
> يستدعي android.util.Log.i (سجلّ معلومات) بالوسم TAG والرسالة "Created new BluetoothMeshService (no existing instance)". [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:109]

```
110:         meshService = created
```
> يُسنِد created إلى المتغيّر meshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:110]

```
111:         unifiedMeshService = null
```
> يُسنِد null إلى المتغيّر unifiedMeshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:111]

```
112:         return created
```
> يُعيد القيمة created. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:112]

```
113:     }
```
> إغلاق نطاق (جسم الدالّة getOrCreate). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:113]

```
114: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:114]

```
115:     @Synchronized
```
> يضع الوسم التوضيحي @Synchronized (متزامن) على الدالّة التالية. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:115]

```
116:     fun getUnifiedOrCreate(context: Context): UnifiedMeshService {
```
> يُعرّف دالّةً (fun) باسم getUnifiedOrCreate (الحصول على الموحَّد أو إنشاؤه) تأخذ context من النوع Context وتُعيد UnifiedMeshService، ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:116]

```
117:         val bluetooth = getOrCreate(context)
```
> يُعرّف قيمةً محلية (val) باسم bluetooth (البلوتوث) ويُسنِد إليها نتيجة استدعاء getOrCreate(context). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:117]

```
118:         val existing = unifiedMeshService
```
> يُعرّف قيمةً محلية (val) باسم existing ويُسنِد إليها القيمة الحالية لـ unifiedMeshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:118]

```
119:         if (existing != null) {
```
> يبدأ شرطاً (if) يتحقق أنّ existing لا يساوي null، ويفتح كتلته. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:119]

```
120:             existing.refreshDelegates()
```
> يستدعي الدالّة refreshDelegates() (تحديث المفوَّضين) على existing. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:120]

```
121:             return existing
```
> يُعيد القيمة existing. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:121]

```
122:         }
```
> إغلاق نطاق (كتلة الشرط if). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:122]

```
123:         val created = UnifiedMeshService(context.applicationContext, bluetooth)
```
> يُعرّف قيمةً محلية (val) باسم created ويُسنِد إليها نسخة جديدة من UnifiedMeshService مُنشأة بـ context.applicationContext وbluetooth. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:123]

```
124:         unifiedMeshService = created
```
> يُسنِد created إلى المتغيّر unifiedMeshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:124]

```
125:         android.util.Log.i(TAG, "Created new UnifiedMeshService")
```
> يستدعي android.util.Log.i (سجلّ معلومات) بالوسم TAG والرسالة "Created new UnifiedMeshService". [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:125]

```
126:         return created
```
> يُعيد القيمة created. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:126]

```
127:     }
```
> إغلاق نطاق (جسم الدالّة getUnifiedOrCreate). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:127]

```
128: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:128]

```
129:     @Synchronized
```
> يضع الوسم التوضيحي @Synchronized (متزامن) على الدالّة التالية. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:129]

```
130:     fun attach(service: BluetoothMeshService) {
```
> يُعرّف دالّةً (fun) باسم attach (إرفاق) تأخذ service من النوع BluetoothMeshService، ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:130]

```
131:         android.util.Log.d(TAG, "Attaching BluetoothMeshService to holder")
```
> يستدعي android.util.Log.d (سجلّ تصحيح) بالوسم TAG والرسالة "Attaching BluetoothMeshService to holder". [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:131]

```
132:         meshService = service
```
> يُسنِد service إلى المتغيّر meshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:132]

```
133:         unifiedMeshService = null
```
> يُسنِد null إلى المتغيّر unifiedMeshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:133]

```
134:     }
```
> إغلاق نطاق (جسم الدالّة attach). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:134]

```
135: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:135]

```
136:     @Synchronized
```
> يضع الوسم التوضيحي @Synchronized (متزامن) على الدالّة التالية. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:136]

```
137:     fun clear() {
```
> يُعرّف دالّةً (fun) باسم clear (مسح) بلا معاملات، ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:137]

```
138:         android.util.Log.d(TAG, "Clearing BluetoothMeshService from holder")
```
> يستدعي android.util.Log.d (سجلّ تصحيح) بالوسم TAG والرسالة "Clearing BluetoothMeshService from holder". [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:138]

```
139:         try { sharedGossipSyncManager?.stop() } catch (_: Exception) { }
```
> ضمن كتلة try يستدعي stop() على sharedGossipSyncManager إن لم يكن null، ويلتقط أي Exception دون فعل. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:139]

```
140:         sharedGossipSyncManager = null
```
> يُسنِد null إلى المتغيّر sharedGossipSyncManager. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:140]

```
141:         activeGossipOwners.clear()
```
> يستدعي الدالّة clear() على المجموعة activeGossipOwners (يُفرِّغها). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:141]

```
142:         meshService = null
```
> يُسنِد null إلى المتغيّر meshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:142]

```
143:         unifiedMeshService = null
```
> يُسنِد null إلى المتغيّر unifiedMeshService. [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:143]

```
144:     }
```
> إغلاق نطاق (جسم الدالّة clear). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:144]

```
145: }
```
> إغلاق نطاق (جسم الكائن MeshServiceHolder). [app/src/main/java/com/bitchat/android/service/MeshServiceHolder.kt:145]
