# 🪨 وحش ١ — البقاء حي بالخلفية (Background Survival)

## المشكلة

التلفون لازم يبقى عقدة relay يوصّل رسائل الناس وهو **بالجيب والشاشة مطفية**. لكن
أندرويد مصمَّم ليقتل الخلفية ويوفّر بطارية. **أنت تحارب النظام** — وكل مصنّع
(OEM) يحارب بشكل مختلف.

اختبار النجاح النهائي: **التلفون يبقى يمرّر رسائل بعد ٣٠ دقيقة من إطفاء الشاشة،
وبعد إعادة تشغيل الجهاز.**

---

## ١. Foreground Service

- نوع الخدمة `connectedDevice` (إلزامي أندرويد 14+ تحديد النوع بالـ manifest
  وبالـ `startForeground`).
- إشعار دائم **خفيف ومفهوم**: مثلاً «نشط — يساعد بإيصال الرسائل». ما يكون مزعج،
  ويشرح ليش التطبيق شغّال.
- `START_STICKY` لإعادة إنشاء الخدمة لو النظام قتلها.
- إعادة تشغيل عند `onTaskRemoved` (لو المستخدم مسح التطبيق من recents).

```xml
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_CONNECTED_DEVICE"/>
<service
    android:name=".background.MeshService"
    android:foregroundServiceType="connectedDevice"
    android:exported="false"/>
```

## ٢. الصمود عبر إعادة التشغيل

- **BootReceiver** يستمع `RECEIVE_BOOT_COMPLETED` ويعيد تشغيل الخدمة بعد إقلاع
  الجهاز.
- صلاحية `RECEIVE_BOOT_COMPLETED` بالـ manifest + استقبال `BOOT_COMPLETED` و
  `QUICKBOOT_POWERON` (بعض OEM).

## ٣. Doze Mode & App Standby

- الخدمة الأمامية **معفاة من أغلب قيود Doze**، **لكن مسح BLE يبقى مُقيَّد** خلال
  فترات Doze (النظام يجمّد المسح بفواصل).
- **التعامل:** جدولة مسح **متقطّعة ذكية** — دورات مسح قصيرة متكررة بدل مسح مستمر،
  مع التكيّف مع نوافذ الـ maintenance window.
- طلب **إعفاء البطارية** عبر `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` (يقلّل تأثير
  App Standby).

## ٤. قاتلو الخلفية من المصنّعين (OEM Killers)

Xiaomi/MIUI، Huawei/EMUI، Oppo/ColorOS، Vivo، Samsung يقتلون التطبيقات بعدوانية
وبطرق غير موثّقة. **هذا أصعب جزء بالوحش — ما ينحل بالكود لحاله، يحتاج إرشاد
المستخدم.**

- **شاشة إرشاد تكيّفية** حسب `Build.MANUFACTURER`: توجّه المستخدم لـ:
  - تفعيل **Autostart / التشغيل التلقائي** (MIUI: Security → Autostart).
  - رفع قيود البطارية يدوياً (Huawei: «إدارة يدوية»؛ Samsung: إزالة من «التطبيقات
    النائمة»).
- روابط مساعدة: مرجع [dontkillmyapp.com](https://dontkillmyapp.com) لكل OEM.
- **كشف القتل وإعادة التشغيل:** آلية heartbeat — لو الخدمة وقفت بلا سبب شرعي،
  أعد تشغيلها (`AlarmManager` احتياطي + إعادة جدولة).

> **ملاحظة صدق:** ماكو ضمان 100% ضد كل OEM. الهدف **أفضل صمود ممكن** + شفافية مع
> المستخدم عن إنه يحتاج يضبط جهازه يدوياً.

## ٥. WakeLock وموازنة الطاقة

- `PARTIAL_WAKE_LOCK` **فقط** أثناء معالجة رزمة فعلية (استلام/تمرير) — يُمسَك
  ويُطلَق بسرعة. **لا تمسكه دائماً** (يحرق البطارية).
- **موازنة الطاقة حسب مستوى البطارية:**
  - بطارية منخفضة → خفّض تردد المسح/الإعلان، اعتمد BLE فقط، أطفئ Wi-Fi إلا عند
    الحاجة للباندويث.
  - شحن/بطارية عالية → دورات أنشط، استعمل Wi-Fi Aware عند توفّره.

## ٦. واجهة مقترحة

```kotlin
interface MeshLifecycleController {
    fun start()                       // يبدأ Foreground Service
    fun stop()
    val state: StateFlow<ServiceState>
    fun onBatteryLevelChanged(pct: Int)   // يضبط power profile
}

enum class PowerProfile { AGGRESSIVE, BALANCED, LOW_POWER }
```

## ٧. حالات اختبار

- [ ] الخدمة تبقى حية بعد ٣٠ دقيقة شاشة مطفية (شاشة على، شاشة مطفية، Doze).
- [ ] الخدمة ترجع بعد reboot.
- [ ] الخدمة ترجع بعد مسحها من recents.
- [ ] WakeLock ما يُمسَك إلا أثناء معالجة فعلية (قياس بالـ profiler).
- [ ] شاشة الإرشاد تظهر الخطوات الصح حسب MANUFACTURER.

## التبعيات

- يعتمد عليه: [وحش ٦ — نقل BLE](06-wolf-ble-transport.md) (الخدمة تستضيف المسح/
  الإعلان).
- milestone: **M1** ([وثيقة 11](11-build-plan.md)) — **يحتاج أجهزة حقيقية للاختبار.**
