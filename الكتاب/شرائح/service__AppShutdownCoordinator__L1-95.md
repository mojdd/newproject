# شريحة — app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt (الأسطر 1–95)

```
1: package com.bitchat.android.service
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) باسم com.bitchat.android.service. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:2]

```
3: import android.app.Application
```
> يستورد الصنف Application من حزمة android.app. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:3]

```
4: import android.os.Process
```
> يستورد الصنف Process من حزمة android.os. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:4]

```
5: import androidx.core.app.NotificationManagerCompat
```
> يستورد الصنف NotificationManagerCompat (مدير الإشعارات المتوافق) من حزمة androidx.core.app. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:5]

```
6: import com.bitchat.android.mesh.MeshService
```
> يستورد الصنف MeshService (خدمة الشبكة المتشابكة) من حزمة com.bitchat.android.mesh. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:6]

```
7: import com.bitchat.android.net.ArtiTorManager
```
> يستورد الصنف ArtiTorManager (مدير تور) من حزمة com.bitchat.android.net. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:7]

```
8: import com.bitchat.android.net.TorMode
```
> يستورد الصنف TorMode (وضع تور) من حزمة com.bitchat.android.net. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:8]

```
9: import kotlinx.coroutines.CoroutineScope
```
> يستورد الصنف CoroutineScope (نطاق الكوروتين) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:9]

```
10: import kotlinx.coroutines.Dispatchers
```
> يستورد الكائن Dispatchers (الموزِّعات) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:10]

```
11: import kotlinx.coroutines.SupervisorJob
```
> يستورد الدالة SupervisorJob (مهمة مشرِفة) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:11]

```
12: import kotlinx.coroutines.Job
```
> يستورد الواجهة Job (مهمة) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:12]

```
13: import kotlinx.coroutines.async
```
> يستورد الدالة async (تشغيل غير متزامن) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:13]

```
14: import kotlinx.coroutines.delay
```
> يستورد الدالة delay (تأخير) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:14]

```
15: import kotlinx.coroutines.isActive
```
> يستورد الخاصية isActive (هل نشط) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:15]

```
16: import kotlinx.coroutines.launch
```
> يستورد الدالة launch (إطلاق) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:16]

```
17: import kotlinx.coroutines.withTimeoutOrNull
```
> يستورد الدالة withTimeoutOrNull (تنفيذ بمهلة وإلا قيمة فارغة) من حزمة kotlinx.coroutines. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:17]

```
18: import java.util.concurrent.atomic.AtomicLong
```
> يستورد الصنف AtomicLong (عدد طويل ذرّي) من حزمة java.util.concurrent.atomic. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:18]

```
19: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:19]

```
20: /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:20]

```
21:  * Coordinates a full application shutdown:
```
> تعليق: ينسّق إيقاف تشغيل كامل للتطبيق. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:21]

```
22:  * - Stop mesh cleanly
```
> تعليق: إيقاف الشبكة المتشابكة بشكل نظيف. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:22]

```
23:  * - Stop Tor without changing persistent setting
```
> تعليق: إيقاف تور دون تغيير الإعداد الدائم. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:23]

```
24:  * - Clear in-memory AppState
```
> تعليق: مسح حالة التطبيق (AppState) الموجودة في الذاكرة. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:24]

```
25:  * - Stop foreground service/notification
```
> تعليق: إيقاف خدمة المقدّمة/الإشعار. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:25]

```
26:  * - Kill the process after completion or after a 5s timeout
```
> تعليق: قتل العملية بعد الاكتمال أو بعد مهلة ٥ ثوانٍ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:26]

```
27:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:27]

```
28: object AppShutdownCoordinator {
```
> يعرّف كائناً مفرداً (object) باسم AppShutdownCoordinator (منسّق إيقاف التطبيق) ويفتح جسمه. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:28]

```
29:     private val scope = CoroutineScope(Dispatchers.Default + SupervisorJob())
```
> يعرّف خاصية خاصة ثابتة باسم scope (النطاق) ويضبط قيمتها إلى نطاق كوروتين منشأ من الموزِّع Dispatchers.Default مضافاً إليه SupervisorJob. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:29]

```
30:     private val shutdownToken = AtomicLong(0L)
```
> يعرّف خاصية خاصة ثابتة باسم shutdownToken (رمز الإيقاف) ويضبط قيمتها إلى AtomicLong مهيّأ بالقيمة 0L. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:30]

```
31:     @Volatile
```
> يضع التعليق التوضيحي @Volatile (متطاير) على الخاصية التالية. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:31]

```
32:     private var shutdownJob: Job? = null
```
> يعرّف خاصية خاصة متغيّرة باسم shutdownJob (مهمة الإيقاف) من نوع Job قابل للإفراغ ويضبط قيمتها الابتدائية إلى null. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:32]

```
33: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:33]

```
34:     fun cancelPendingShutdown() {
```
> يعرّف دالة باسم cancelPendingShutdown (إلغاء الإيقاف المعلّق) بلا وسائط ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:34]

```
35:         shutdownToken.incrementAndGet()
```
> يستدعي incrementAndGet على shutdownToken فيزيده بمقدار واحد ويعيد القيمة بعد الزيادة. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:35]

```
36:         shutdownJob?.cancel()
```
> يستدعي cancel على shutdownJob إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:36]

```
37:         shutdownJob = null
```
> يضبط shutdownJob إلى null. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:37]

```
38:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:38]

```
39: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:39]

```
40:     fun requestFullShutdownAndKill(
```
> يعرّف دالة باسم requestFullShutdownAndKill (طلب الإيقاف الكامل والقتل) ويفتح قائمة وسائطها. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:40]

```
41:         app: Application,
```
> يعرّف الوسيط app (التطبيق) من نوع Application. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:41]

```
42:         mesh: MeshService?,
```
> يعرّف الوسيط mesh (الشبكة المتشابكة) من نوع MeshService قابل للإفراغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:42]

```
43:         notificationManager: NotificationManagerCompat,
```
> يعرّف الوسيط notificationManager (مدير الإشعارات) من نوع NotificationManagerCompat. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:43]

```
44:         stopForeground: () -> Unit,
```
> يعرّف الوسيط stopForeground (إيقاف المقدّمة) من نوع دالة بلا وسائط تُعيد Unit. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:44]

```
45:         stopService: () -> Unit
```
> يعرّف الوسيط stopService (إيقاف الخدمة) من نوع دالة بلا وسائط تُعيد Unit. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:45]

```
46:     ) {
```
> يغلق قائمة الوسائط ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:46]

```
47:         val token = shutdownToken.incrementAndGet()
```
> يعرّف متغيراً ثابتاً محلياً باسم token (الرمز) ويضبط قيمته إلى نتيجة incrementAndGet على shutdownToken وهي القيمة بعد الزيادة. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:47]

```
48:         shutdownJob?.cancel()
```
> يستدعي cancel على shutdownJob إن لم يكن فارغاً. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:48]

```
49:         val job = scope.launch {
```
> يعرّف متغيراً ثابتاً محلياً باسم job (المهمة) ويضبط قيمته إلى نتيجة استدعاء launch على scope ويفتح جسم الكوروتين. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:49]

```
50:             // Signal UI to finish gracefully before we kill the process
```
> تعليق: إشارة لواجهة المستخدم لإنهاء نفسها بلطف قبل قتل العملية. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:50]

```
51:             try {
```
> يفتح كتلة try (محاولة). [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:51]

```
52:                 val intent = android.content.Intent(com.bitchat.android.util.AppConstants.UI.ACTION_FORCE_FINISH)
```
> يعرّف متغيراً ثابتاً محلياً باسم intent (النية) ويضبط قيمته إلى كائن Intent منشأ بالقيمة com.bitchat.android.util.AppConstants.UI.ACTION_FORCE_FINISH. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:52]

```
53:                     .setPackage(app.packageName)
```
> يستدعي setPackage على الـ intent مع packageName للتطبيق app. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:53]

```
54:                 app.sendBroadcast(intent, com.bitchat.android.util.AppConstants.UI.PERMISSION_FORCE_FINISH)
```
> يستدعي sendBroadcast على app ممرراً الـ intent والقيمة com.bitchat.android.util.AppConstants.UI.PERMISSION_FORCE_FINISH كصلاحية. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:54]

```
55:             } catch (_: Exception) { }
```
> يغلق كتلة try ويلتقط أي استثناء Exception بمعامل مهمَل دون تنفيذ أي شيء. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:55]

```
56: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:56]

```
57:             // Stop mesh (best-effort)
```
> تعليق: إيقاف الشبكة المتشابكة (بأفضل جهد ممكن). [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:57]

```
58:             try { mesh?.stopServices() } catch (_: Exception) { }
```
> يستدعي stopServices على mesh إن لم يكن فارغاً داخل كتلة try، ويلتقط أي استثناء Exception دون تنفيذ أي شيء. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:58]

```
59: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:59]

```
60:             // Stop Tor temporarily (do not change user setting)
```
> تعليق: إيقاف تور مؤقتاً (دون تغيير إعداد المستخدم). [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:60]

```
61:             val torProvider = ArtiTorManager.getInstance()
```
> يعرّف متغيراً ثابتاً محلياً باسم torProvider (مزوّد تور) ويضبط قيمته إلى نتيجة getInstance على ArtiTorManager. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:61]

```
62:             val torStop = async {
```
> يعرّف متغيراً ثابتاً محلياً باسم torStop (إيقاف تور) ويضبط قيمته إلى نتيجة استدعاء async ويفتح جسمها. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:62]

```
63:                 try { torProvider.applyMode(app, TorMode.OFF) } catch (_: Exception) { }
```
> يستدعي applyMode على torProvider ممرراً app والقيمة TorMode.OFF داخل كتلة try، ويلتقط أي استثناء Exception دون تنفيذ أي شيء. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:63]

```
64:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:64]

```
65: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:65]

```
66:             // Clear AppState in-memory store
```
> تعليق: مسح مخزن حالة التطبيق في الذاكرة. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:66]

```
67:             try { com.bitchat.android.services.AppStateStore.clear() } catch (_: Exception) { }
```
> يستدعي clear على com.bitchat.android.services.AppStateStore داخل كتلة try، ويلتقط أي استثناء Exception دون تنفيذ أي شيء. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:67]

```
68: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:68]

```
69:             // Stop foreground and clear notification
```
> تعليق: إيقاف المقدّمة ومسح الإشعار. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:69]

```
70:             try { stopForeground() } catch (_: Exception) { }
```
> يستدعي الدالة stopForeground داخل كتلة try، ويلتقط أي استثناء Exception دون تنفيذ أي شيء. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:70]

```
71:             try { notificationManager.cancel(10001) } catch (_: Exception) { }
```
> يستدعي cancel على notificationManager ممرراً المعرّف 10001 داخل كتلة try، ويلتقط أي استثناء Exception دون تنفيذ أي شيء. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:71]

```
72: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:72]

```
73:             // Wait up to 5 seconds for shutdown tasks
```
> تعليق: الانتظار حتى ٥ ثوانٍ لمهام الإيقاف. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:73]

```
74:             withTimeoutOrNull(5000) {
```
> يستدعي withTimeoutOrNull بمهلة قدرها 5000 ويفتح كتلتها. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:74]

```
75:                 try { torStop.await() } catch (_: Exception) { }
```
> يستدعي await على torStop داخل كتلة try، ويلتقط أي استثناء Exception دون تنفيذ أي شيء. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:75]

```
76:                 delay(100)
```
> يستدعي delay بقيمة 100. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:76]

```
77:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:77]

```
78: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:78]

```
79:             // Stop the service itself
```
> تعليق: إيقاف الخدمة نفسها. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:79]

```
80:             if (!isActive || shutdownToken.get() != token) return@launch
```
> إذا كان isActive غير محقق أو كانت قيمة get على shutdownToken لا تساوي token فإنه يعود من الكوروتين launch. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:80]

```
81:             try { stopService() } catch (_: Exception) { }
```
> يستدعي الدالة stopService داخل كتلة try، ويلتقط أي استثناء Exception دون تنفيذ أي شيء. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:81]

```
82: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:82]

```
83:             // Hard kill the app process
```
> تعليق: قتل عملية التطبيق قتلاً صارماً. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:83]

```
84:             if (!isActive || shutdownToken.get() != token) return@launch
```
> إذا كان isActive غير محقق أو كانت قيمة get على shutdownToken لا تساوي token فإنه يعود من الكوروتين launch. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:84]

```
85:             try { Process.killProcess(Process.myPid()) } catch (_: Exception) { }
```
> يستدعي killProcess على Process ممرراً ناتج myPid على Process داخل كتلة try، ويلتقط أي استثناء Exception دون تنفيذ أي شيء. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:85]

```
86:             try { System.exit(0) } catch (_: Exception) { }
```
> يستدعي exit على System بالقيمة 0 داخل كتلة try، ويلتقط أي استثناء Exception دون تنفيذ أي شيء. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:86]

```
87:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:87]

```
88:         shutdownJob = job
```
> يضبط shutdownJob إلى job. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:88]

```
89:         job.invokeOnCompletion {
```
> يستدعي invokeOnCompletion على job ويفتح كتلتها. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:89]

```
90:             if (shutdownJob === job) {
```
> إذا كان shutdownJob هو نفس job بالمطابقة المرجعية يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:90]

```
91:                 shutdownJob = null
```
> يضبط shutdownJob إلى null. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:91]

```
92:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:92]

```
93:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:93]

```
94:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:94]

```
95: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/service/AppShutdownCoordinator.kt:95]
