# شريحة — app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt (الأسطر 1–200)

```
1: package com.bitchat.android.geohash
```
> يُعلِن أن هذا الملف ينتمي إلى الحزمة (package) باسم `com.bitchat.android.geohash`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:2]

```
3: import android.Manifest
```
> يستورد (import) الصنف `android.Manifest`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:3]

```
4: import android.content.Context
```
> يستورد الصنف `android.content.Context` (السياق). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:4]

```
5: import android.content.IntentFilter
```
> يستورد الصنف `android.content.IntentFilter` (مرشّح النيّات). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:5]

```
6: import android.content.pm.PackageManager
```
> يستورد الصنف `android.content.pm.PackageManager` (مدير الحزم). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:6]

```
7: import android.location.Geocoder
```
> يستورد الصنف `android.location.Geocoder` (المرمِّز الجغرافي). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:7]

```
8: import android.location.Location
```
> يستورد الصنف `android.location.Location` (الموقع). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:8]

```
9: import android.location.LocationManager
```
> يستورد الصنف `android.location.LocationManager` (مدير الموقع). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:9]

```
10: import android.os.Bundle
```
> يستورد الصنف `android.os.Bundle` (الحزمة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:10]

```
11: import android.util.Log
```
> يستورد الصنف `android.util.Log` (السجل). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:11]

```
12: import androidx.core.app.ActivityCompat
```
> يستورد الصنف `androidx.core.app.ActivityCompat`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:12]

```
13: import com.google.android.gms.common.ConnectionResult
```
> يستورد الصنف `com.google.android.gms.common.ConnectionResult` (نتيجة الاتصال). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:13]

```
14: import com.google.android.gms.common.GoogleApiAvailability
```
> يستورد الصنف `com.google.android.gms.common.GoogleApiAvailability` (توافر واجهة جوجل البرمجية). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:14]

```
15: import kotlinx.coroutines.*
```
> يستورد كل العناصر من حزمة `kotlinx.coroutines` (الإجراءات المتزامنة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:15]

```
16: import java.util.*
```
> يستورد كل العناصر من حزمة `java.util`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:16]

```
17: import com.google.gson.Gson
```
> يستورد الصنف `com.google.gson.Gson`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:17]

```
18: import com.google.gson.JsonSyntaxException
```
> يستورد الصنف `com.google.gson.JsonSyntaxException` (استثناء صياغة JSON). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:18]

```
19: import kotlinx.coroutines.flow.MutableStateFlow
```
> يستورد الصنف `MutableStateFlow` (تدفّق حالة قابل للتغيير). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:19]

```
20: import kotlinx.coroutines.flow.SharingStarted
```
> يستورد الصنف `SharingStarted` (سياسة بدء المشاركة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:20]

```
21: import kotlinx.coroutines.flow.StateFlow
```
> يستورد الصنف `StateFlow` (تدفّق الحالة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:21]

```
22: import kotlinx.coroutines.flow.combine
```
> يستورد الدالّة `combine` (الدمج). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:22]

```
23: import kotlinx.coroutines.flow.stateIn
```
> يستورد الدالّة `stateIn` (التحويل إلى تدفّق حالة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:23]

```
24: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:24]

```
25: /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:25]

```
26:  * Manages location permissions, one-shot location retrieval, and computing geohash channels.
```
> تعليق: يدير أذونات الموقع، وجلب الموقع لمرة واحدة، وحساب قنوات الـ geohash. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:26]

```
27:  * Direct port from iOS LocationChannelManager for 100% compatibility
```
> تعليق: نقل مباشر من نسخة iOS لـ LocationChannelManager لتوافق بنسبة 100%. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:27]

```
28:  */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:28]

```
29: class LocationChannelManager private constructor(private val context: Context) {
```
> يُعرِّف الصنف `LocationChannelManager` (مدير قنوات الموقع) بباني (constructor) خاص يأخذ مُعطى `context` من نوع `Context` ويحفظه كخاصية خاصة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:29]

```
30:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:30]

```
31:     companion object {
```
> يفتح كائن المرافقة (companion object) الخاص بالصنف. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:31]

```
32:         private const val TAG = "LocationChannelManager"
```
> يُعرِّف ثابتاً خاصاً `TAG` (وسم السجل) بالقيمة النصّية `"LocationChannelManager"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:32]

```
33:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:33]

```
34:         @Volatile
```
> يضع التعليمة التوضيحية `@Volatile` (متطاير) على المتغيّر التالي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:34]

```
35:         private var INSTANCE: LocationChannelManager? = null
```
> يُعرِّف متغيّراً خاصاً `INSTANCE` (النسخة) من نوع `LocationChannelManager?` قيمته الابتدائية `null`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:35]

```
36:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:36]

```
37:         fun getInstance(context: Context): LocationChannelManager {
```
> يُعرِّف الدالّة `getInstance` (جلب النسخة) التي تأخذ `context` وتُعيد `LocationChannelManager`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:37]

```
38:             return INSTANCE ?: synchronized(this) {
```
> يُعيد `INSTANCE` إن لم يكن `null`، وإلا يدخل كتلة متزامنة (synchronized) على `this`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:38]

```
39:                 INSTANCE ?: LocationChannelManager(context.applicationContext).also { INSTANCE = it }
```
> يُعيد `INSTANCE` إن لم يكن `null`، وإلا يُنشئ `LocationChannelManager` بسياق التطبيق `applicationContext` ويُسنِده إلى `INSTANCE` عبر `also`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:39]

```
40:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:40]

```
41:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:41]

```
42:     }
```
> إغلاق نطاق (نهاية كائن المرافقة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:42]

```
43: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:43]

```
44:     // State enum matching iOS
```
> تعليق: تعداد الحالة المطابق لـ iOS. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:44]

```
45:     enum class PermissionState {
```
> يُعرِّف تعداداً (enum class) باسم `PermissionState` (حالة الإذن). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:45]

```
46:         DENIED,
```
> يُعرِّف عنصر التعداد `DENIED` (مرفوض). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:46]

```
47:         AUTHORIZED
```
> يُعرِّف عنصر التعداد `AUTHORIZED` (مُصرَّح به). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:47]

```
48:     }
```
> إغلاق نطاق (نهاية التعداد). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:48]

```
49: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:49]

```
50:     private val locationManager: LocationManager = context.getSystemService(Context.LOCATION_SERVICE) as LocationManager
```
> يُعرِّف خاصية خاصة `locationManager` (مدير الموقع) قيمتها ناتج `context.getSystemService(Context.LOCATION_SERVICE)` بعد تحويله إلى `LocationManager`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:50]

```
51:     private val locationProvider: LocationProvider
```
> يُعرِّف خاصية خاصة `locationProvider` (مزوّد الموقع) من نوع `LocationProvider` دون إسناد قيمة هنا. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:51]

```
52:     private val geocoderProvider: GeocoderProvider = GeocoderFactory.get(context)
```
> يُعرِّف خاصية خاصة `geocoderProvider` (مزوّد المرمِّز الجغرافي) قيمتها ناتج `GeocoderFactory.get(context)`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:52]

```
53:     private var lastLocation: Location? = null
```
> يُعرِّف متغيّراً خاصاً `lastLocation` (آخر موقع) من نوع `Location?` قيمته الابتدائية `null`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:53]

```
54:     private var geocodingJob: Job? = null
```
> يُعرِّف متغيّراً خاصاً `geocodingJob` (مهمّة الترميز الجغرافي) من نوع `Job?` قيمته الابتدائية `null`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:54]

```
55:     private val gson = Gson()
```
> يُعرِّف خاصية خاصة `gson` قيمتها نسخة جديدة من `Gson()`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:55]

```
56:     private var dataManager: com.bitchat.android.ui.DataManager? = null
```
> يُعرِّف متغيّراً خاصاً `dataManager` (مدير البيانات) من نوع `com.bitchat.android.ui.DataManager?` قيمته الابتدائية `null`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:56]

```
57: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:57]

```
58:     private fun checkSystemLocationEnabled(): Boolean {
```
> يُعرِّف دالّة خاصة `checkSystemLocationEnabled` (فحص تفعيل موقع النظام) تُعيد `Boolean`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:58]

```
59:         return try {
```
> يبدأ إعادة قيمة من كتلة `try`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:59]

```
60:             locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER) ||
```
> يستدعي `locationManager.isProviderEnabled` لمزوّد `GPS_PROVIDER` ويربطه بـ «أو» المنطقية. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:60]

```
61:                     locationManager.isProviderEnabled(LocationManager.NETWORK_PROVIDER)
```
> يستدعي `locationManager.isProviderEnabled` لمزوّد `NETWORK_PROVIDER` كطرف ثانٍ لـ «أو». [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:61]

```
62:         } catch (_: Exception) {
```
> يلتقط أي `Exception` (استثناء) دون تسمية المتغيّر. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:62]

```
63:             false
```
> يُعيد `false` عند حدوث الاستثناء. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:63]

```
64:         }
```
> إغلاق نطاق (نهاية try/catch). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:64]

```
65:     }
```
> إغلاق نطاق (نهاية الدالّة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:65]

```
66: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:66]

```
67:     private val locationStateReceiver = object : android.content.BroadcastReceiver() {
```
> يُعرِّف خاصية خاصة `locationStateReceiver` (مستقبِل حالة الموقع) ككائن مجهول يرث من `BroadcastReceiver`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:67]

```
68:         override fun onReceive(context: Context?, intent: android.content.Intent?) {
```
> يتجاوز (override) الدالّة `onReceive` التي تأخذ `context` من نوع `Context?` و`intent` من نوع `Intent?`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:68]

```
69:             if (intent?.action == LocationManager.PROVIDERS_CHANGED_ACTION) {
```
> يفحص ما إذا كان `intent?.action` يساوي `LocationManager.PROVIDERS_CHANGED_ACTION` (إجراء تغيّر المزوّدات). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:69]

```
70:                 val isEnabled = checkSystemLocationEnabled()
```
> يُعرِّف متغيّراً ثابتاً محلياً `isEnabled` (مُفعَّل) قيمته ناتج استدعاء `checkSystemLocationEnabled()`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:70]

```
71:                 Log.d(TAG, "System location state changed: $isEnabled")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"System location state changed: $isEnabled"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:71]

```
72:                 _systemLocationEnabled.value = isEnabled
```
> يُسنِد قيمة `isEnabled` إلى `_systemLocationEnabled.value`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:72]

```
73:             }
```
> إغلاق نطاق (نهاية كتلة if). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:73]

```
74:         }
```
> إغلاق نطاق (نهاية onReceive). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:74]

```
75:     }
```
> إغلاق نطاق (نهاية الكائن المجهول). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:75]

```
76: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:76]

```
77:     private val locationUpdateCallback: (Location) -> Unit = { location ->
```
> يُعرِّف خاصية خاصة `locationUpdateCallback` (نداء تحديث الموقع) من نوع دالّة تأخذ `Location` وتُعيد `Unit`، وجسمها يأخذ مُعطى `location`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:77]

```
78:         onLocationUpdated(location)
```
> يستدعي الدالّة `onLocationUpdated` مُمرِّراً `location`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:78]

```
79:     }
```
> إغلاق نطاق (نهاية النداء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:79]

```
80: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:80]

```
81:     // Published state for UI bindings (matching iOS @Published properties)
```
> تعليق: حالة منشورة لربط الواجهة (مطابقة لخصائص @Published في iOS). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:81]

```
82:     private val scope = CoroutineScope(SupervisorJob() + Dispatchers.Main.immediate)
```
> يُعرِّف خاصية خاصة `scope` (النطاق) قيمتها `CoroutineScope` مكوَّن من `SupervisorJob()` و`Dispatchers.Main.immediate`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:82]

```
83: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:83]

```
84:     private val _permissionState = MutableStateFlow(PermissionState.DENIED)
```
> يُعرِّف خاصية خاصة `_permissionState` (حالة الإذن الداخلية) من نوع `MutableStateFlow` قيمتها الابتدائية `PermissionState.DENIED`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:84]

```
85:     val permissionState: StateFlow<PermissionState> = _permissionState
```
> يُعرِّف خاصية عامة `permissionState` من نوع `StateFlow<PermissionState>` تكشف `_permissionState`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:85]

```
86: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:86]

```
87:     private val _availableChannels = MutableStateFlow<List<GeohashChannel>>(emptyList())
```
> يُعرِّف خاصية خاصة `_availableChannels` (القنوات المتاحة الداخلية) من نوع `MutableStateFlow<List<GeohashChannel>>` قيمتها الابتدائية قائمة فارغة `emptyList()`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:87]

```
88:     val availableChannels: StateFlow<List<GeohashChannel>> = _availableChannels
```
> يُعرِّف خاصية عامة `availableChannels` من نوع `StateFlow<List<GeohashChannel>>` تكشف `_availableChannels`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:88]

```
89: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:89]

```
90:     private val _selectedChannel = MutableStateFlow<ChannelID>(ChannelID.Mesh)
```
> يُعرِّف خاصية خاصة `_selectedChannel` (القناة المختارة الداخلية) من نوع `MutableStateFlow<ChannelID>` قيمتها الابتدائية `ChannelID.Mesh`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:90]

```
91:     val selectedChannel: StateFlow<ChannelID> = _selectedChannel
```
> يُعرِّف خاصية عامة `selectedChannel` من نوع `StateFlow<ChannelID>` تكشف `_selectedChannel`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:91]

```
92: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:92]

```
93:     private val _teleported = MutableStateFlow(false)
```
> يُعرِّف خاصية خاصة `_teleported` (المُنتقَل آنياً الداخلي) من نوع `MutableStateFlow` قيمتها الابتدائية `false`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:93]

```
94:     val teleported: StateFlow<Boolean> = _teleported
```
> يُعرِّف خاصية عامة `teleported` من نوع `StateFlow<Boolean>` تكشف `_teleported`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:94]

```
95: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:95]

```
96:     private val _locationNames = MutableStateFlow<Map<GeohashChannelLevel, String>>(emptyMap())
```
> يُعرِّف خاصية خاصة `_locationNames` (أسماء المواقع الداخلية) من نوع `MutableStateFlow<Map<GeohashChannelLevel, String>>` قيمتها الابتدائية خريطة فارغة `emptyMap()`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:96]

```
97:     val locationNames: StateFlow<Map<GeohashChannelLevel, String>> = _locationNames
```
> يُعرِّف خاصية عامة `locationNames` من نوع `StateFlow<Map<GeohashChannelLevel, String>>` تكشف `_locationNames`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:97]

```
98:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:98]

```
99:     private val _isLoadingLocation = MutableStateFlow(false)
```
> يُعرِّف خاصية خاصة `_isLoadingLocation` (جارٍ تحميل الموقع الداخلي) من نوع `MutableStateFlow` قيمتها الابتدائية `false`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:99]

```
100:     val isLoadingLocation: StateFlow<Boolean> = _isLoadingLocation
```
> يُعرِّف خاصية عامة `isLoadingLocation` من نوع `StateFlow<Boolean>` تكشف `_isLoadingLocation`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:100]

```
101:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:101]

```
102:     private val _locationServicesEnabled = MutableStateFlow(false)
```
> يُعرِّف خاصية خاصة `_locationServicesEnabled` (تفعيل خدمات الموقع الداخلي) من نوع `MutableStateFlow` قيمتها الابتدائية `false`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:102]

```
103:     val locationServicesEnabled: StateFlow<Boolean> = _locationServicesEnabled
```
> يُعرِّف خاصية عامة `locationServicesEnabled` من نوع `StateFlow<Boolean>` تكشف `_locationServicesEnabled`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:103]

```
104: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:104]

```
105:     private val _systemLocationEnabled = MutableStateFlow(checkSystemLocationEnabled())
```
> يُعرِّف خاصية خاصة `_systemLocationEnabled` (تفعيل موقع النظام الداخلي) من نوع `MutableStateFlow` قيمتها الابتدائية ناتج استدعاء `checkSystemLocationEnabled()`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:105]

```
106:     val systemLocationEnabled: StateFlow<Boolean> = _systemLocationEnabled
```
> يُعرِّف خاصية عامة `systemLocationEnabled` من نوع `StateFlow<Boolean>` تكشف `_systemLocationEnabled`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:106]

```
107: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:107]

```
108:     val effectiveLocationEnabled: StateFlow<Boolean> = combine(
```
> يُعرِّف خاصية عامة `effectiveLocationEnabled` (التفعيل الفعلي للموقع) من نوع `StateFlow<Boolean>` قيمتها ناتج استدعاء `combine(` ببدء قائمة المُعطيات. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:108]

```
109:         locationServicesEnabled,
```
> يُمرِّر `locationServicesEnabled` كمُعطى أول لـ `combine`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:109]

```
110:         systemLocationEnabled
```
> يُمرِّر `systemLocationEnabled` كمُعطى ثانٍ لـ `combine`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:110]

```
111:     ) { appToggle, systemToggle ->
```
> يغلق مُعطيات `combine` ويبدأ دالّة الدمج بمُعطيين `appToggle` (مفتاح التطبيق) و`systemToggle` (مفتاح النظام). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:111]

```
112:         appToggle && systemToggle
```
> يُعيد ناتج «و» المنطقية بين `appToggle` و`systemToggle`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:112]

```
113:     }.stateIn(
```
> يغلق دالّة الدمج ويستدعي `stateIn(` عليها ببدء المُعطيات. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:113]

```
114:         scope,
```
> يُمرِّر `scope` كمُعطى أول لـ `stateIn`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:114]

```
115:         SharingStarted.Eagerly,
```
> يُمرِّر `SharingStarted.Eagerly` (البدء بشغف) كمُعطى ثانٍ لـ `stateIn`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:115]

```
116:         false
```
> يُمرِّر `false` كقيمة ابتدائية لـ `stateIn`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:116]

```
117:     )
```
> إغلاق نطاق (نهاية استدعاء stateIn). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:117]

```
118: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:118]

```
119: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:119]

```
120:     init {
```
> يفتح كتلة التهيئة (init) للصنف. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:120]

```
121:         // Choose the best location provider
```
> تعليق: اختيار أفضل مزوّد للموقع. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:121]

```
122:         val availability = GoogleApiAvailability.getInstance().isGooglePlayServicesAvailable(context)
```
> يُعرِّف متغيّراً ثابتاً محلياً `availability` (التوافر) قيمته ناتج `GoogleApiAvailability.getInstance().isGooglePlayServicesAvailable(context)`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:122]

```
123:         locationProvider = if (availability == ConnectionResult.SUCCESS) {
```
> يُسنِد إلى `locationProvider` نتيجة شرط `if` يفحص ما إذا كان `availability` يساوي `ConnectionResult.SUCCESS`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:123]

```
124:             Log.i(TAG, "Using FusedLocationProvider (Google Play Services)")
```
> يستدعي `Log.i` بالوسم `TAG` والرسالة `"Using FusedLocationProvider (Google Play Services)"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:124]

```
125:             FusedLocationProvider(context)
```
> يُعطي نسخة جديدة من `FusedLocationProvider(context)` كقيمة فرع `if`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:125]

```
126:         } else {
```
> يبدأ فرع `else`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:126]

```
127:             Log.i(TAG, "Using SystemLocationProvider (Native LocationManager)")
```
> يستدعي `Log.i` بالوسم `TAG` والرسالة `"Using SystemLocationProvider (Native LocationManager)"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:127]

```
128:             SystemLocationProvider(context)
```
> يُعطي نسخة جديدة من `SystemLocationProvider(context)` كقيمة فرع `else`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:128]

```
129:         }
```
> إغلاق نطاق (نهاية if/else). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:129]

```
130: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:130]

```
131:         checkAndSyncPermission()
```
> يستدعي الدالّة `checkAndSyncPermission` (فحص ومزامنة الإذن). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:131]

```
132:         // Initialize DataManager and load persisted settings
```
> تعليق: تهيئة DataManager وتحميل الإعدادات المحفوظة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:132]

```
133:         dataManager = com.bitchat.android.ui.DataManager(context)
```
> يُسنِد إلى `dataManager` نسخة جديدة من `com.bitchat.android.ui.DataManager(context)`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:133]

```
134:         loadPersistedChannelSelection()
```
> يستدعي الدالّة `loadPersistedChannelSelection` (تحميل اختيار القناة المحفوظ). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:134]

```
135:         loadLocationServicesState()
```
> يستدعي الدالّة `loadLocationServicesState` (تحميل حالة خدمات الموقع). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:135]

```
136: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:136]

```
137:         // Register for system location changes
```
> تعليق: التسجيل لتغيّرات موقع النظام. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:137]

```
138:         context.registerReceiver(locationStateReceiver, IntentFilter(LocationManager.PROVIDERS_CHANGED_ACTION))
```
> يستدعي `context.registerReceiver` مُمرِّراً `locationStateReceiver` ومرشّح نيّات `IntentFilter(LocationManager.PROVIDERS_CHANGED_ACTION)`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:138]

```
139:     }
```
> إغلاق نطاق (نهاية كتلة init). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:139]

```
140: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:140]

```
141:     // MARK: - Public API (matching iOS interface)
```
> تعليق: MARK: - الواجهة البرمجية العامة (مطابقة لواجهة iOS). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:141]

```
142: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:142]

```
143:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:143]

```
144:      * Enable location channels (request permission if needed)
```
> تعليق: تفعيل قنوات الموقع (طلب الإذن عند الحاجة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:144]

```
145:      * UNIFIED: Only requests location if location services are enabled by user
```
> تعليق: موحَّد: لا يطلب الموقع إلا إذا فعّل المستخدم خدمات الموقع. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:145]

```
146:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:146]

```
147:     fun enableLocationChannels() {
```
> يُعرِّف الدالّة العامة `enableLocationChannels` (تفعيل قنوات الموقع) بلا مُعطيات. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:147]

```
148:         Log.d(TAG, "enableLocationChannels() called")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"enableLocationChannels() called"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:148]

```
149:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:149]

```
150:         if (!_locationServicesEnabled.value || !_systemLocationEnabled.value) {
```
> يفحص ما إذا كانت قيمة `_locationServicesEnabled` غير مُفعَّلة أو قيمة `_systemLocationEnabled` غير مُفعَّلة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:150]

```
151:             Log.w(TAG, "Location services disabled (app or system) - not requesting location")
```
> يستدعي `Log.w` بالوسم `TAG` والرسالة `"Location services disabled (app or system) - not requesting location"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:151]

```
152:             return
```
> يُنهي الدالّة بإرجاع فارغ (return). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:152]

```
153:         }
```
> إغلاق نطاق (نهاية كتلة if). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:153]

```
154:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:154]

```
155: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:155]

```
156:         if (getCurrentPermissionStatus() == PermissionState.AUTHORIZED) {
```
> يفحص ما إذا كان ناتج `getCurrentPermissionStatus()` يساوي `PermissionState.AUTHORIZED`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:156]

```
157:             Log.d(TAG, "Permission authorized - requesting location")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"Permission authorized - requesting location"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:157]

```
158:             _permissionState.value = PermissionState.AUTHORIZED
```
> يُسنِد `PermissionState.AUTHORIZED` إلى `_permissionState.value`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:158]

```
159:             requestOneShotLocation()
```
> يستدعي الدالّة `requestOneShotLocation` (طلب موقع لمرة واحدة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:159]

```
160:         } else {
```
> يبدأ فرع `else`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:160]

```
161:             Log.d(TAG, "Permission not granted")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"Permission not granted"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:161]

```
162:             _permissionState.value = PermissionState.DENIED
```
> يُسنِد `PermissionState.DENIED` إلى `_permissionState.value`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:162]

```
163:         }
```
> إغلاق نطاق (نهاية if/else). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:163]

```
164:     }
```
> إغلاق نطاق (نهاية الدالّة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:164]

```
165: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:165]

```
166:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:166]

```
167:      * Refresh available channels from current location
```
> تعليق: تحديث القنوات المتاحة من الموقع الحالي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:167]

```
168:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:168]

```
169:     fun refreshChannels() {
```
> يُعرِّف الدالّة العامة `refreshChannels` (تحديث القنوات) بلا مُعطيات. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:169]

```
170:         if (_permissionState.value == PermissionState.AUTHORIZED && isLocationServicesEnabled()) {
```
> يفحص ما إذا كانت قيمة `_permissionState` تساوي `PermissionState.AUTHORIZED` و ناتج `isLocationServicesEnabled()` صحيحاً. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:170]

```
171:             requestOneShotLocation()
```
> يستدعي الدالّة `requestOneShotLocation`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:171]

```
172:         }
```
> إغلاق نطاق (نهاية كتلة if). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:172]

```
173:     }
```
> إغلاق نطاق (نهاية الدالّة). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:173]

```
174: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:174]

```
175:     /**
```
> تعليق: بداية كتلة توثيق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:175]

```
176:      * Begin real-time location updates while a selector UI is visible
```
> تعليق: بدء تحديثات الموقع الآنية بينما تكون واجهة الاختيار ظاهرة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:176]

```
177:      * Uses requestLocationUpdates for continuous updates, plus a one-shot to prime state immediately
```
> تعليق: يستعمل requestLocationUpdates للتحديثات المستمرة، إضافةً إلى طلب لمرة واحدة لتهيئة الحالة فوراً. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:177]

```
178:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:178]

```
179:     fun beginLiveRefresh(interval: Long = 5000L) {
```
> يُعرِّف الدالّة العامة `beginLiveRefresh` (بدء التحديث الحيّ) بمُعطى `interval` (الفاصل) من نوع `Long` قيمته الافتراضية `5000L`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:179]

```
180:         Log.d(TAG, "Beginning live refresh (continuous updates)")
```
> يستدعي `Log.d` بالوسم `TAG` والرسالة `"Beginning live refresh (continuous updates)"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:180]

```
181: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:181]

```
182:         if (_permissionState.value != PermissionState.AUTHORIZED) {
```
> يفحص ما إذا كانت قيمة `_permissionState` لا تساوي `PermissionState.AUTHORIZED`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:182]

```
183:             Log.w(TAG, "Cannot start live refresh - permission not authorized")
```
> يستدعي `Log.w` بالوسم `TAG` والرسالة `"Cannot start live refresh - permission not authorized"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:183]

```
184:             return
```
> يُنهي الدالّة بإرجاع فارغ (return). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:184]

```
185:         }
```
> إغلاق نطاق (نهاية كتلة if). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:185]

```
186: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:186]

```
187:         if (!isLocationServicesEnabled()) {
```
> يفحص ما إذا كان ناتج `isLocationServicesEnabled()` غير صحيح (مُنفى). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:187]

```
188:             Log.w(TAG, "Cannot start live refresh - location services disabled")
```
> يستدعي `Log.w` بالوسم `TAG` والرسالة `"Cannot start live refresh - location services disabled"`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:188]

```
189:             return
```
> يُنهي الدالّة بإرجاع فارغ (return). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:189]

```
190:         }
```
> إغلاق نطاق (نهاية كتلة if). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:190]

```
191: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:191]

```
192:         // Register for continuous updates from available provider
```
> تعليق: التسجيل للتحديثات المستمرة من المزوّد المتاح. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:192]

```
193:         locationProvider.requestLocationUpdates(
```
> يستدعي `locationProvider.requestLocationUpdates(` ببدء قائمة المُعطيات. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:193]

```
194:             intervalMs = interval,
```
> يُمرِّر المُعطى المُسمّى `intervalMs` بقيمة `interval`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:194]

```
195:             minDistanceMeters = 5f,
```
> يُمرِّر المُعطى المُسمّى `minDistanceMeters` بقيمة `5f` (أمتار). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:195]

```
196:             callback = locationUpdateCallback
```
> يُمرِّر المُعطى المُسمّى `callback` بقيمة `locationUpdateCallback`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:196]

```
197:         )
```
> إغلاق نطاق (نهاية استدعاء requestLocationUpdates). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:197]

```
198:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:198]

```
199:         // Prime state immediately with last known / current location
```
> تعليق: تهيئة الحالة فوراً بآخر موقع معروف / الموقع الحالي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:199]

```
200:         requestOneShotLocation()
```
> يستدعي الدالّة `requestOneShotLocation`. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:200]
