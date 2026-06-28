# شريحة — app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt (الأسطر 1–55)

```
1: package com.bitchat.android.net
```
> يُعرّف هذا الملف انتماءه إلى الحزمة (package) باسم `com.bitchat.android.net`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:2]

```
3: import okhttp3.OkHttpClient
```
> يستورد (import) الصنف `OkHttpClient` من حزمة `okhttp3`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:3]

```
4: import java.net.InetSocketAddress
```
> يستورد الصنف `InetSocketAddress` (عنوان مقبس إنترنت) من `java.net`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:4]

```
5: import java.net.Proxy
```
> يستورد الصنف `Proxy` (وسيط) من `java.net`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:5]

```
6: import java.util.concurrent.TimeUnit
```
> يستورد التعداد `TimeUnit` (وحدة الزمن) من `java.util.concurrent`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:6]

```
7: import java.util.concurrent.atomic.AtomicReference
```
> يستورد الصنف `AtomicReference` (مرجع ذرّي) من `java.util.concurrent.atomic`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:7]

```
8: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:8]

```
9: /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:9]

```
10:  * Centralized OkHttp provider to ensure all network traffic honors Tor settings.
```
> تعليق: مزوّد OkHttp مركزي لضمان أن كل حركة مرور الشبكة تحترم إعدادات Tor. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:10]

```
11:  */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:11]

```
12: object OkHttpProvider {
```
> يُعرّف كائناً مفرداً (object) باسم `OkHttpProvider` (مزوّد OkHttp) ويفتح نطاقه. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:12]

```
13:     private val httpClientRef = AtomicReference<OkHttpClient?>(null)
```
> يُعرّف خاصية خاصة (private) ثابتة باسم `httpClientRef` (مرجع عميل HTTP) من نوع `AtomicReference` يحمل `OkHttpClient` يقبل القيمة الفارغة، ويهيّئها بالقيمة `null`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:13]

```
14:     private val wsClientRef = AtomicReference<OkHttpClient?>(null)
```
> يُعرّف خاصية خاصة ثابتة باسم `wsClientRef` (مرجع عميل WebSocket) من نوع `AtomicReference` يحمل `OkHttpClient` يقبل القيمة الفارغة، ويهيّئها بالقيمة `null`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:14]

```
15: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:15]

```
16:     fun reset() {
```
> يُعرّف دالة (fun) باسم `reset` (إعادة تعيين) بلا وُسطاء ويفتح نطاقها. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:16]

```
17:         httpClientRef.set(null)
```
> يستدعي `set` على `httpClientRef` بالقيمة `null`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:17]

```
18:         wsClientRef.set(null)
```
> يستدعي `set` على `wsClientRef` بالقيمة `null`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:18]

```
19:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:19]

```
20: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:20]

```
21:     fun httpClient(): OkHttpClient {
```
> يُعرّف دالة باسم `httpClient` (عميل HTTP) بلا وُسطاء تُعيد قيمة من نوع `OkHttpClient` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:21]

```
22:         httpClientRef.get()?.let { return it }
```
> يجلب القيمة من `httpClientRef` عبر `get`، وإن لم تكن فارغة يدخل كتلة `let` ويُعيد تلك القيمة (`it`). [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:22]

```
23:         val client = baseBuilderForCurrentProxy()
```
> يُعرّف متغيراً ثابتاً باسم `client` (عميل) ويُسنِد إليه نتيجة استدعاء `baseBuilderForCurrentProxy` (بنّاء أساسي للوسيط الحالي). [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:23]

```
24:             .callTimeout(15, TimeUnit.SECONDS)
```
> يستدعي `callTimeout` (مهلة النداء) بقيمة `15` ووحدة `TimeUnit.SECONDS` (ثوانٍ). [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:24]

```
25:             .connectTimeout(10, TimeUnit.SECONDS)
```
> يستدعي `connectTimeout` (مهلة الاتصال) بقيمة `10` ووحدة `TimeUnit.SECONDS`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:25]

```
26:             .readTimeout(15, TimeUnit.SECONDS)
```
> يستدعي `readTimeout` (مهلة القراءة) بقيمة `15` ووحدة `TimeUnit.SECONDS`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:26]

```
27:             .build()
```
> يستدعي `build` لإنشاء الكائن النهائي. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:27]

```
28:         httpClientRef.set(client)
```
> يستدعي `set` على `httpClientRef` بالقيمة `client`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:28]

```
29:         return client
```
> يُعيد `client`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:29]

```
30:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:30]

```
31: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:31]

```
32:     fun webSocketClient(): OkHttpClient {
```
> يُعرّف دالة باسم `webSocketClient` (عميل WebSocket) بلا وُسطاء تُعيد قيمة من نوع `OkHttpClient` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:32]

```
33:         wsClientRef.get()?.let { return it }
```
> يجلب القيمة من `wsClientRef` عبر `get`، وإن لم تكن فارغة يدخل كتلة `let` ويُعيد تلك القيمة (`it`). [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:33]

```
34:         val client = baseBuilderForCurrentProxy()
```
> يُعرّف متغيراً ثابتاً باسم `client` ويُسنِد إليه نتيجة استدعاء `baseBuilderForCurrentProxy`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:34]

```
35:             .connectTimeout(10, TimeUnit.SECONDS)
```
> يستدعي `connectTimeout` (مهلة الاتصال) بقيمة `10` ووحدة `TimeUnit.SECONDS`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:35]

```
36:             .readTimeout(0, TimeUnit.SECONDS)
```
> يستدعي `readTimeout` (مهلة القراءة) بقيمة `0` ووحدة `TimeUnit.SECONDS`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:36]

```
37:             .writeTimeout(10, TimeUnit.SECONDS)
```
> يستدعي `writeTimeout` (مهلة الكتابة) بقيمة `10` ووحدة `TimeUnit.SECONDS`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:37]

```
38:             .build()
```
> يستدعي `build` لإنشاء الكائن النهائي. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:38]

```
39:         wsClientRef.set(client)
```
> يستدعي `set` على `wsClientRef` بالقيمة `client`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:39]

```
40:         return client
```
> يُعيد `client`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:40]

```
41:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:41]

```
42: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:42]

```
43:     private fun baseBuilderForCurrentProxy(): OkHttpClient.Builder {
```
> يُعرّف دالة خاصة باسم `baseBuilderForCurrentProxy` (بنّاء أساسي للوسيط الحالي) بلا وُسطاء تُعيد قيمة من نوع `OkHttpClient.Builder` ويفتح نطاقها. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:43]

```
44:         val builder = OkHttpClient.Builder()
```
> يُعرّف متغيراً ثابتاً باسم `builder` (بنّاء) ويُسنِد إليه كائناً جديداً من `OkHttpClient.Builder`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:44]

```
45:         val torProvider = ArtiTorManager.getInstance()
```
> يُعرّف متغيراً ثابتاً باسم `torProvider` (مزوّد Tor) ويُسنِد إليه نتيجة استدعاء `getInstance` على `ArtiTorManager` (مدير Arti Tor). [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:45]

```
46:         val socks: InetSocketAddress? = torProvider.currentSocksAddress()
```
> يُعرّف متغيراً ثابتاً باسم `socks` من نوع `InetSocketAddress` يقبل القيمة الفارغة، ويُسنِد إليه نتيجة استدعاء `currentSocksAddress` (عنوان SOCKS الحالي) على `torProvider`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:46]

```
47:         // If a SOCKS address is defined, always use it. TorProvider sets this as soon as Tor mode is ON,
```
> تعليق: إذا كان عنوان SOCKS معرّفاً، استعمله دائماً. مزوّد Tor يضبط هذا بمجرد تشغيل وضع Tor. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:47]

```
48:         // even before bootstrap, to prevent any direct connections from occurring.
```
> تعليق: حتى قبل التمهيد (bootstrap)، لمنع حدوث أي اتصالات مباشرة. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:48]

```
49:         if (socks != null) {
```
> يبدأ شرطاً (if) يتحقق أن `socks` ليس `null` ويفتح نطاقه. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:49]

```
50:             val proxy = Proxy(Proxy.Type.SOCKS, socks)
```
> يُعرّف متغيراً ثابتاً باسم `proxy` (وسيط) ويُسنِد إليه كائن `Proxy` جديداً بنوع `Proxy.Type.SOCKS` وعنوان `socks`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:50]

```
51:             builder.proxy(proxy)
```
> يستدعي `proxy` على `builder` بالقيمة `proxy`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:51]

```
52:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:52]

```
53:         return builder
```
> يُعيد `builder`. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:53]

```
54:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:54]

```
55: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/net/OkHttpProvider.kt:55]
