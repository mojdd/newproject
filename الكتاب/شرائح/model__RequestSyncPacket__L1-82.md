# شريحة — app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt (الأسطر 1–82)

```
1: package com.bitchat.android.model
```
> يعلن أن هذا الملف ينتمي إلى الحزمة (package) المسماة `com.bitchat.android.model`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:2]

```
3: import com.bitchat.android.sync.SyncDefaults
```
> يستورد (import) الصنف `SyncDefaults` (الإعدادات الافتراضية للمزامنة) من حزمة المزامنة. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:3]

```
4: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:4]

```
5: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:5]

```
6:  * REQUEST_SYNC payload using GCS (Golomb-Coded Set) parameters.
```
> تعليق: حمولة طلب المزامنة (REQUEST_SYNC) تستعمل معاملات المجموعة المرمَّزة بغولومب (GCS). [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:6]

```
7:  * TLV (type, length16, value), types:
```
> تعليق: ترميز نوع-طول-قيمة (TLV) بطول من ١٦ بتاً، والأنواع هي. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:7]

```
8:  *  - 0x01: P (uint8) — Golomb-Rice parameter
```
> تعليق: النوع 0x01 هو P عدد بايت واحد بلا إشارة، وهو معامل غولومب-رايس. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:8]

```
9:  *  - 0x02: M (uint32, big-endian) — hash range (N * 2^P)
```
> تعليق: النوع 0x02 هو M عدد من ٣٢ بتاً بلا إشارة بترتيب البايت الكبير، وهو مدى التجزئة (N مضروباً في 2 أس P). [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:9]

```
10:  *  - 0x03: data (opaque) — GR bitstream bytes
```
> تعليق: النوع 0x03 هو البيانات (غير شفافة)، وهي بايتات سيل بتّات غولومب-رايس. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:10]

```
11:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:11]

```
12: data class RequestSyncPacket(
```
> يعرّف صنف بيانات (data class) باسم `RequestSyncPacket` (رزمة طلب المزامنة) ويبدأ قائمة معاملات مُنشئه. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:12]

```
13:     val p: Int,
```
> يعلن خاصية ثابتة `p` (المعامل) من نوع عدد صحيح `Int`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:13]

```
14:     val m: Long,
```
> يعلن خاصية ثابتة `m` (المدى) من نوع عدد صحيح طويل `Long`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:14]

```
15:     val data: ByteArray
```
> يعلن خاصية ثابتة `data` (البيانات) من نوع مصفوفة بايتات `ByteArray`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:15]

```
16: ) {
```
> يغلق قائمة معاملات المُنشئ ويفتح نطاق جسم الصنف. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:16]

```
17:     fun encode(): ByteArray {
```
> يعرّف الدالة `encode` (الترميز) التي لا تأخذ معاملات وتعيد مصفوفة بايتات `ByteArray`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:17]

```
18:         val out = ArrayList<Byte>()
```
> يعرّف متغيّراً ثابتاً `out` (المُخرَج) ويُسنِد إليه قائمة مصفوفية `ArrayList` فارغة من بايتات. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:18]

```
19:         fun putTLV(t: Int, v: ByteArray) {
```
> يعرّف دالة محلّية `putTLV` (وضع نوع-طول-قيمة) تأخذ معامل النوع `t` عدداً صحيحاً ومعامل القيمة `v` مصفوفة بايتات، ويفتح جسمها. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:19]

```
20:             out.add(t.toByte())
```
> يضيف إلى القائمة `out` قيمة النوع `t` بعد تحويلها إلى بايت. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:20]

```
21:             val len = v.size
```
> يعرّف متغيّراً ثابتاً `len` (الطول) ويُسنِد إليه حجم المصفوفة `v`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:21]

```
22:             out.add(((len ushr 8) and 0xFF).toByte())
```
> يضيف إلى `out` البايت الأعلى من الطول، بإزاحة `len` إلى اليمين ٨ بتّات مع تصفية بالقناع 0xFF ثم تحويله إلى بايت. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:22]

```
23:             out.add((len and 0xFF).toByte())
```
> يضيف إلى `out` البايت الأدنى من الطول، بتصفية `len` بالقناع 0xFF ثم تحويله إلى بايت. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:23]

```
24:             out.addAll(v.toList())
```
> يضيف إلى `out` كل عناصر المصفوفة `v` بعد تحويلها إلى قائمة. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:24]

```
25:         }
```
> إغلاق نطاق الدالة المحلّية `putTLV`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:25]

```
26:         // P
```
> تعليق: P. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:26]

```
27:         putTLV(0x01, byteArrayOf(p.toByte()))
```
> يستدعي `putTLV` بالنوع 0x01 ومصفوفة بايتات تحوي قيمة `p` محوَّلة إلى بايت. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:27]

```
28:         // M (uint32)
```
> تعليق: M عدد من ٣٢ بتاً بلا إشارة. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:28]

```
29:         val m32 = m.coerceAtMost(0xffff_ffffL)
```
> يعرّف متغيّراً ثابتاً `m32` ويُسنِد إليه قيمة `m` محدودة بحدّ أعلى مقداره 0xffffffff. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:29]

```
30:         putTLV(
```
> يبدأ استدعاء الدالة `putTLV`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:30]

```
31:             0x02,
```
> المعامل الأول للاستدعاء هو النوع 0x02. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:31]

```
32:             byteArrayOf(
```
> يبدأ بناء مصفوفة بايتات بوصفها المعامل الثاني للاستدعاء. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:32]

```
33:                 ((m32 ushr 24) and 0xFF).toByte(),
```
> البايت الأول هو `m32` مزاحاً يميناً ٢٤ بتاً ومصفّى بالقناع 0xFF ثم محوَّلاً إلى بايت. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:33]

```
34:                 ((m32 ushr 16) and 0xFF).toByte(),
```
> البايت الثاني هو `m32` مزاحاً يميناً ١٦ بتاً ومصفّى بالقناع 0xFF ثم محوَّلاً إلى بايت. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:34]

```
35:                 ((m32 ushr 8) and 0xFF).toByte(),
```
> البايت الثالث هو `m32` مزاحاً يميناً ٨ بتّات ومصفّى بالقناع 0xFF ثم محوَّلاً إلى بايت. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:35]

```
36:                 (m32 and 0xFF).toByte()
```
> البايت الرابع هو `m32` مصفّى بالقناع 0xFF ثم محوَّلاً إلى بايت. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:36]

```
37:             )
```
> إغلاق بناء مصفوفة البايتات (المعامل الثاني). [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:37]

```
38:         )
```
> إغلاق استدعاء الدالة `putTLV`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:38]

```
39:         // data
```
> تعليق: البيانات. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:39]

```
40:         putTLV(0x03, data)
```
> يستدعي `putTLV` بالنوع 0x03 وبالخاصية `data`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:40]

```
41:         return out.toByteArray()
```
> يعيد القائمة `out` بعد تحويلها إلى مصفوفة بايتات. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:41]

```
42:     }
```
> إغلاق نطاق الدالة `encode`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:42]

```
43: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:43]

```
44:     companion object {
```
> يفتح كائناً مرافقاً (companion object) داخل الصنف. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:44]

```
45:         // Receiver-side safety limit (configurable constant)
```
> تعليق: حدّ أمان من جهة المستقبِل (ثابت قابل للضبط). [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:45]

```
46:         const val MAX_ACCEPT_FILTER_BYTES: Int = SyncDefaults.MAX_ACCEPT_FILTER_BYTES
```
> يعرّف ثابتاً `MAX_ACCEPT_FILTER_BYTES` (أقصى بايتات مصفاة مقبولة) من نوع عدد صحيح `Int` ويُسنِد إليه قيمة الثابت الموافق من `SyncDefaults`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:46]

```
47: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:47]

```
48:         fun decode(data: ByteArray): RequestSyncPacket? {
```
> يعرّف الدالة `decode` (فك الترميز) التي تأخذ معامل `data` مصفوفة بايتات وتعيد كائن `RequestSyncPacket` قابلاً للقيمة الفارغة، ويفتح جسمها. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:48]

```
49:             var off = 0
```
> يعرّف متغيّراً متبدّلاً `off` (الإزاحة) ويُسنِد إليه القيمة 0. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:49]

```
50:             var p: Int? = null
```
> يعرّف متغيّراً متبدّلاً `p` من نوع عدد صحيح قابل للقيمة الفارغة ويُسنِد إليه null. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:50]

```
51:             var m: Long? = null
```
> يعرّف متغيّراً متبدّلاً `m` من نوع عدد صحيح طويل قابل للقيمة الفارغة ويُسنِد إليه null. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:51]

```
52:             var payload: ByteArray? = null
```
> يعرّف متغيّراً متبدّلاً `payload` (الحمولة) من نوع مصفوفة بايتات قابلة للقيمة الفارغة ويُسنِد إليه null. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:52]

```
53: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:53]

```
54:             while (off + 3 <= data.size) {
```
> يبدأ حلقة `while` تستمر ما دام مجموع `off` و٣ أصغر من أو يساوي حجم `data`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:54]

```
55:                 val t = (data[off].toInt() and 0xFF); off += 1
```
> يعرّف متغيّراً ثابتاً `t` ويُسنِد إليه بايت `data` عند الإزاحة `off` محوَّلاً إلى عدد صحيح ومصفّى بالقناع 0xFF، ثم يزيد `off` بمقدار ١. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:55]

```
56:                 val len = ((data[off].toInt() and 0xFF) shl 8) or (data[off+1].toInt() and 0xFF); off += 2
```
> يعرّف متغيّراً ثابتاً `len` ويُسنِد إليه دمج البايت عند `off` مزاحاً يساراً ٨ بتّات مع البايت عند `off+1` (كلاهما مصفّى بالقناع 0xFF) بعملية «أو» بتّية، ثم يزيد `off` بمقدار ٢. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:56]

```
57:                 if (off + len > data.size) return null
```
> إن كان مجموع `off` و`len` أكبر من حجم `data` فيعيد null. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:57]

```
58:                 val v = data.copyOfRange(off, off + len); off += len
```
> يعرّف متغيّراً ثابتاً `v` ويُسنِد إليه نسخة من `data` في المدى من `off` إلى `off+len`، ثم يزيد `off` بمقدار `len`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:58]

```
59:                 when (t) {
```
> يبدأ تعبير اختيار `when` على قيمة `t`، ويفتح نطاقه. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:59]

```
60:                     0x01 -> if (len == 1) p = (v[0].toInt() and 0xFF)
```
> عند النوع 0x01، إن كان `len` يساوي 1 يُسنِد إلى `p` أول بايت من `v` محوَّلاً إلى عدد صحيح ومصفّى بالقناع 0xFF. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:60]

```
61:                     0x02 -> if (len == 4) {
```
> عند النوع 0x02، إن كان `len` يساوي 4 يفتح كتلة تنفيذ. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:61]

```
62:                         val mm = ((v[0].toLong() and 0xFF) shl 24) or
```
> يعرّف متغيّراً ثابتاً `mm` ويبدأ إسناد قيمة، جزؤها الأول البايت `v[0]` محوَّلاً إلى عدد طويل ومصفّى بالقناع 0xFF ومزاحاً يساراً ٢٤ بتاً مع عملية «أو» بتّية. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:62]

```
63:                                  ((v[1].toLong() and 0xFF) shl 16) or
```
> ويُدمج معه البايت `v[1]` محوَّلاً إلى عدد طويل ومصفّى بالقناع 0xFF ومزاحاً يساراً ١٦ بتاً مع عملية «أو» بتّية. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:63]

```
64:                                  ((v[2].toLong() and 0xFF) shl 8) or
```
> ويُدمج معه البايت `v[2]` محوَّلاً إلى عدد طويل ومصفّى بالقناع 0xFF ومزاحاً يساراً ٨ بتّات مع عملية «أو» بتّية. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:64]

```
65:                                  (v[3].toLong() and 0xFF)
```
> ويُدمج معه البايت `v[3]` محوَّلاً إلى عدد طويل ومصفّى بالقناع 0xFF بوصفه الجزء الأخير من قيمة `mm`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:65]

```
66:                         m = mm
```
> يُسنِد قيمة `mm` إلى المتغيّر `m`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:66]

```
67:                     }
```
> إغلاق كتلة الحالة 0x02. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:67]

```
68:                     0x03 -> {
```
> عند النوع 0x03 يفتح كتلة تنفيذ. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:68]

```
69:                         if (v.size > MAX_ACCEPT_FILTER_BYTES) return null
```
> إن كان حجم `v` أكبر من الثابت `MAX_ACCEPT_FILTER_BYTES` فيعيد null. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:69]

```
70:                         payload = v
```
> يُسنِد المصفوفة `v` إلى المتغيّر `payload`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:70]

```
71:                     }
```
> إغلاق كتلة الحالة 0x03. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:71]

```
72:                 }
```
> إغلاق نطاق تعبير `when`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:72]

```
73:             }
```
> إغلاق نطاق حلقة `while`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:73]

```
74: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:74]

```
75:             val pp = p ?: return null
```
> يعرّف متغيّراً ثابتاً `pp` ويُسنِد إليه قيمة `p`، فإن كانت `p` فارغة يعيد null. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:75]

```
76:             val mm = m ?: return null
```
> يعرّف متغيّراً ثابتاً `mm` ويُسنِد إليه قيمة `m`، فإن كانت `m` فارغة يعيد null. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:76]

```
77:             val dd = payload ?: return null
```
> يعرّف متغيّراً ثابتاً `dd` ويُسنِد إليه قيمة `payload`، فإن كانت `payload` فارغة يعيد null. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:77]

```
78:             if (pp < 1 || mm <= 0L) return null
```
> إن كان `pp` أصغر من 1 أو كان `mm` أصغر من أو يساوي 0 فيعيد null. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:78]

```
79:             return RequestSyncPacket(pp, mm, dd)
```
> يعيد كائن `RequestSyncPacket` جديداً مبنيّاً بالقيم `pp` و`mm` و`dd`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:79]

```
80:         }
```
> إغلاق نطاق الدالة `decode`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:80]

```
81:     }
```
> إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:81]

```
82: }
```
> إغلاق نطاق صنف `RequestSyncPacket`. [app/src/main/java/com/bitchat/android/model/RequestSyncPacket.kt:82]
