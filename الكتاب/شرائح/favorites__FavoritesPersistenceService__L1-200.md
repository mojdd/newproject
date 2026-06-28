# شريحة — app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt (الأسطر 1–200)

```
1: package com.bitchat.android.favorites
```
> يُعلِن أنّ هذا الملف يقع داخل الحزمة (package) المسمّاة com.bitchat.android.favorites. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:2]

```
3: import android.content.Context
```
> يستورد (import) الصنف Context من android.content. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:3]

```
4: import android.util.Log
```
> يستورد الصنف Log من android.util. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:4]

```
5: import com.bitchat.android.identity.SecureIdentityStateManager
```
> يستورد الصنف SecureIdentityStateManager (مدير حالة الهوية الآمنة) من com.bitchat.android.identity. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:5]

```
6: import com.google.gson.Gson
```
> يستورد الصنف Gson من com.google.gson. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:6]

```
7: import com.google.gson.reflect.TypeToken
```
> يستورد الصنف TypeToken من com.google.gson.reflect. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:7]

```
8: import java.util.*
```
> يستورد كل المحتويات من الحزمة java.util. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:8]

```
9: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:9]

```
10: /**
```
> تعليق: بداية تعليق توثيقي (مفتوح بـ /**). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:10]

```
11:  * Bridging Noise and Nostr favorites
```
> تعليق: «جسر بين مفضّلات Noise وNostr». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:11]

```
12:  * Direct port from iOS FavoritesPersistenceService.swift, with Android-specific
```
> تعليق: «نقل مباشر من ملف iOS المسمّى FavoritesPersistenceService.swift، مع خاصّية تخصّ أندرويد». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:12]

```
13:  * peerID (16-hex) -> npub indexing for Nostr DM routing.
```
> تعليق: «فهرسة معرّف النِّد peerID (١٦ خانة ست عشرية) إلى npub لتوجيه رسائل Nostr الخاصّة». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:13]

```
14:  */
```
> تعليق: نهاية التعليق التوثيقي (مغلق بـ */). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:14]

```
15: data class FavoriteRelationship(
```
> يُعرّف صنف بيانات (data class) باسم FavoriteRelationship (علاقة مفضّلة) ويفتح قائمة معاملاته. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:15]

```
16:     val peerNoisePublicKey: ByteArray,    // Noise static public key (32 bytes)
```
> يُعرّف خاصّية ثابتة peerNoisePublicKey (مفتاح Noise العام للنِّد) من نوع ByteArray؛ والتعليق: «مفتاح Noise العام الثابت (٣٢ بايت)». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:16]

```
17:     val peerNostrPublicKey: String?,      // npub bech32 string
```
> يُعرّف خاصّية ثابتة peerNostrPublicKey (مفتاح Nostr العام للنِّد) من نوع String قابل للعدم؛ والتعليق: «سلسلة npub بصيغة bech32». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:17]

```
18:     val peerNickname: String,
```
> يُعرّف خاصّية ثابتة peerNickname (كنية النِّد) من نوع String. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:18]

```
19:     val isFavorite: Boolean,              // We favorited them
```
> يُعرّف خاصّية ثابتة isFavorite (هل هو مفضّل) من نوع Boolean؛ والتعليق: «نحن فضّلناهم». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:19]

```
20:     val theyFavoritedUs: Boolean,         // They favorited us
```
> يُعرّف خاصّية ثابتة theyFavoritedUs (هل فضّلونا) من نوع Boolean؛ والتعليق: «هم فضّلونا». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:20]

```
21:     val favoritedAt: Date,
```
> يُعرّف خاصّية ثابتة favoritedAt (تاريخ التفضيل) من نوع Date. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:21]

```
22:     val lastUpdated: Date
```
> يُعرّف خاصّية ثابتة lastUpdated (آخر تحديث) من نوع Date. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:22]

```
23: ) {
```
> يُغلق قائمة معاملات صنف البيانات ويفتح جسمه. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:23]

```
24:     val isMutual: Boolean get() = isFavorite && theyFavoritedUs
```
> يُعرّف خاصّية محسوبة isMutual (هل التفضيل متبادل) من نوع Boolean يُعيد عبر دالة الجلب get قيمة الجمع المنطقي isFavorite && theyFavoritedUs. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:24]

```
25: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:25]

```
26:     override fun equals(other: Any?): Boolean {
```
> يُعيد تعريف (override) الدالة equals التي تأخذ معاملاً other من نوع Any قابل للعدم وتُعيد Boolean، ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:26]

```
27:         if (this === other) return true
```
> إن كان this مطابقاً مرجعياً (===) لـ other فيُعيد true. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:27]

```
28:         if (javaClass != other?.javaClass) return false
```
> إن لم يساوِ javaClass الحالي صنف other (عبر الاستدعاء الآمن ?.) فيُعيد false. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:28]

```
29: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:29]

```
30:         other as FavoriteRelationship
```
> يُجري تحويلاً (smart cast) لـ other إلى النوع FavoriteRelationship. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:30]

```
31: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:31]

```
32:         if (!peerNoisePublicKey.contentEquals(other.peerNoisePublicKey)) return false
```
> إن لم يتطابق محتوى peerNoisePublicKey مع محتوى other.peerNoisePublicKey عبر contentEquals فيُعيد false. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:32]

```
33:         if (peerNostrPublicKey != other.peerNostrPublicKey) return false
```
> إن لم يساوِ peerNostrPublicKey نظيره في other فيُعيد false. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:33]

```
34:         if (peerNickname != other.peerNickname) return false
```
> إن لم يساوِ peerNickname نظيره في other فيُعيد false. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:34]

```
35:         if (isFavorite != other.isFavorite) return false
```
> إن لم يساوِ isFavorite نظيره في other فيُعيد false. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:35]

```
36:         if (theyFavoritedUs != other.theyFavoritedUs) return false
```
> إن لم يساوِ theyFavoritedUs نظيره في other فيُعيد false. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:36]

```
37: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:37]

```
38:         return true
```
> يُعيد true. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:38]

```
39:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:39]

```
40: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:40]

```
41:     override fun hashCode(): Int {
```
> يُعيد تعريف الدالة hashCode التي لا تأخذ معاملات وتُعيد Int، ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:41]

```
42:         var result = peerNoisePublicKey.contentHashCode()
```
> يُعرّف متغيّراً result ويُسنِد إليه قيمة contentHashCode الناتجة عن peerNoisePublicKey. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:42]

```
43:         result = 31 * result + (peerNostrPublicKey?.hashCode() ?: 0)
```
> يُسنِد إلى result حاصل 31 مضروباً في result مضافاً إليه hashCode الخاص بـ peerNostrPublicKey أو القيمة 0 عند العدم. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:43]

```
44:         result = 31 * result + peerNickname.hashCode()
```
> يُسنِد إلى result حاصل 31 مضروباً في result مضافاً إليه hashCode الخاص بـ peerNickname. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:44]

```
45:         result = 31 * result + isFavorite.hashCode()
```
> يُسنِد إلى result حاصل 31 مضروباً في result مضافاً إليه hashCode الخاص بـ isFavorite. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:45]

```
46:         result = 31 * result + theyFavoritedUs.hashCode()
```
> يُسنِد إلى result حاصل 31 مضروباً في result مضافاً إليه hashCode الخاص بـ theyFavoritedUs. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:46]

```
47:         return result
```
> يُعيد قيمة result. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:47]

```
48:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:48]

```
49: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:49]

```
50: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:50]

```
51: interface FavoritesChangeListener {
```
> يُعرّف واجهة (interface) باسم FavoritesChangeListener (مستمع تغيّر المفضّلات) ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:51]

```
52:     fun onFavoriteChanged(noiseKeyHex: String)
```
> يُعلِن دالة مجرّدة onFavoriteChanged تأخذ معاملاً noiseKeyHex من نوع String. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:52]

```
53:     fun onAllCleared()
```
> يُعلِن دالة مجرّدة onAllCleared بلا معاملات. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:53]

```
54: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:54]

```
55: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:55]

```
56: /**
```
> تعليق: بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:56]

```
57:  * Manages favorites with Noise↔Nostr mapping
```
> تعليق: «يدير المفضّلات مع ربط Noise↔Nostr». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:57]

```
58:  * Singleton pattern matching iOS implementation.
```
> تعليق: «نمط المفرد (Singleton) مطابق لتطبيق iOS». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:58]

```
59:  */
```
> تعليق: نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:59]

```
60: class FavoritesPersistenceService private constructor(private val context: Context) {
```
> يُعرّف صنفاً باسم FavoritesPersistenceService (خدمة حفظ المفضّلات) ببانٍ (constructor) خاص يأخذ خاصّية خاصّة context من نوع Context، ويفتح جسمه. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:60]

```
61: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:61]

```
62:     companion object {
```
> يُعرّف كائن رفيق (companion object) ويفتح جسمه. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:62]

```
63:         private const val TAG = "FavoritesPersistenceService"
```
> يُعرّف ثابتاً خاصاً TAG من نوع String بقيمة "FavoritesPersistenceService". [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:63]

```
64:         private const val FAVORITES_KEY = "favorite_relationships"            // noiseHex -> relationship
```
> يُعرّف ثابتاً خاصاً FAVORITES_KEY بقيمة "favorite_relationships"؛ والتعليق: «noiseHex إلى relationship». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:64]

```
65:         private const val PEERID_INDEX_KEY = "favorite_peerid_index"         // peerID(16-hex) -> npub
```
> يُعرّف ثابتاً خاصاً PEERID_INDEX_KEY بقيمة "favorite_peerid_index"؛ والتعليق: «peerID(١٦ خانة ست عشرية) إلى npub». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:65]

```
66: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:66]

```
67:         @Volatile
```
> يضع التوصيف @Volatile على التعريف التالي. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:67]

```
68:         private var INSTANCE: FavoritesPersistenceService? = null
```
> يُعرّف متغيّراً خاصاً INSTANCE من نوع FavoritesPersistenceService قابل للعدم بقيمة ابتدائية null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:68]

```
69: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:69]

```
70:         val shared: FavoritesPersistenceService
```
> يُعرّف خاصّية shared من نوع FavoritesPersistenceService. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:70]

```
71:             get() = INSTANCE ?: throw IllegalStateException("FavoritesPersistenceService not initialized")
```
> دالة الجلب get تُعيد INSTANCE، أو ترمي IllegalStateException برسالة "FavoritesPersistenceService not initialized" عند العدم. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:71]

```
72: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:72]

```
73:         fun initialize(context: Context) {
```
> يُعرّف دالة initialize تأخذ معاملاً context من نوع Context، ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:73]

```
74:             if (INSTANCE == null) {
```
> إن كان INSTANCE مساوياً null يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:74]

```
75:                 synchronized(this) {
```
> يبدأ كتلة متزامنة synchronized على this. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:75]

```
76:                     if (INSTANCE == null) {
```
> إن كان INSTANCE مساوياً null يفتح كتلة الشرط (فحص مزدوج). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:76]

```
77:                         INSTANCE = FavoritesPersistenceService(context.applicationContext)
```
> يُسنِد إلى INSTANCE نسخة جديدة من FavoritesPersistenceService مُنشأة بـ context.applicationContext. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:77]

```
78:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:78]

```
79:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:79]

```
80:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:80]

```
81:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:81]

```
82:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:82]

```
83: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:83]

```
84:     private val stateManager = SecureIdentityStateManager(context)
```
> يُعرّف خاصّية خاصّة stateManager ويُسنِد إليها نسخة جديدة من SecureIdentityStateManager مُنشأة بـ context. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:84]

```
85:     private val gson = Gson()
```
> يُعرّف خاصّية خاصّة gson ويُسنِد إليها نسخة جديدة من Gson. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:85]

```
86:     private val favorites = mutableMapOf<String, FavoriteRelationship>() // noiseHex -> relationship
```
> يُعرّف خاصّية خاصّة favorites ويُسنِد إليها خريطة قابلة للتعديل من String إلى FavoriteRelationship؛ والتعليق: «noiseHex إلى relationship». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:86]

```
87:     // NEW: Index by current mesh peerID (16-hex) for direct lookup when sending Nostr DMs from mesh context
```
> تعليق: «جديد: فهرسة حسب معرّف النِّد الشبكي peerID (١٦ خانة ست عشرية) للبحث المباشر عند إرسال رسائل Nostr الخاصّة من سياق الشبكة». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:87]

```
88:     private val peerIdIndex = mutableMapOf<String, String>() // peerID (lowercase 16-hex) -> npub
```
> يُعرّف خاصّية خاصّة peerIdIndex (فهرس معرّفات الأنداد) ويُسنِد إليها خريطة قابلة للتعديل من String إلى String؛ والتعليق: «peerID (١٦ خانة ست عشرية صغيرة) إلى npub». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:88]

```
89:     private val listeners = mutableListOf<FavoritesChangeListener>()
```
> يُعرّف خاصّية خاصّة listeners (المستمعون) ويُسنِد إليها قائمة قابلة للتعديل من نوع FavoritesChangeListener. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:89]

```
90: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:90]

```
91:     init {
```
> يفتح كتلة التهيئة init. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:91]

```
92:         loadFavorites()
```
> يستدعي الدالة loadFavorites. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:92]

```
93:         loadPeerIdIndex()
```
> يستدعي الدالة loadPeerIdIndex. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:93]

```
94:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:94]

```
95: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:95]

```
96:     /** Get favorite status for Noise public key */
```
> تعليق: «جلب حالة التفضيل لمفتاح Noise العام». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:96]

```
97:     fun getFavoriteStatus(noisePublicKey: ByteArray): FavoriteRelationship? {
```
> يُعرّف دالة getFavoriteStatus تأخذ معاملاً noisePublicKey من نوع ByteArray وتُعيد FavoriteRelationship قابلاً للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:97]

```
98:         val keyHex = noisePublicKey.joinToString("") { "%02x".format(it) }
```
> يُعرّف ثابتاً محلياً keyHex بقيمة دمج بايتات noisePublicKey في سلسلة بلا فاصل حيث يُنسَّق كل بايت بصيغة "%02x" ست عشرية. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:98]

```
99:         return favorites[keyHex]
```
> يُعيد القيمة المقابلة لـ keyHex من الخريطة favorites. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:99]

```
100:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:100]

```
101: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:101]

```
102:     /** Get favorite status for 16-hex peerID (by noiseHex prefix match) */
```
> تعليق: «جلب حالة التفضيل لمعرّف peerID المكوّن من ١٦ خانة ست عشرية (عبر مطابقة بادئة noiseHex)». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:102]

```
103:     fun getFavoriteStatus(peerID: String): FavoriteRelationship? {
```
> يُعرّف دالة getFavoriteStatus (مُحمَّلة بمعامل مختلف) تأخذ معاملاً peerID من نوع String وتُعيد FavoriteRelationship قابلاً للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:103]

```
104:         val pid = peerID.lowercase()
```
> يُعرّف ثابتاً محلياً pid بقيمة peerID محوّلاً إلى أحرف صغيرة عبر lowercase. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:104]

```
105:         for ((_, relationship) in favorites) {
```
> يبدأ حلقة for تمرّ على مدخلات favorites متجاهلاً المفتاح (_) ومسمّياً القيمة relationship. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:105]

```
106:             val noiseKeyHex = relationship.peerNoisePublicKey.joinToString("") { "%02x".format(it) }
```
> يُعرّف ثابتاً محلياً noiseKeyHex بقيمة دمج بايتات relationship.peerNoisePublicKey في سلسلة ست عشرية بلا فاصل بصيغة "%02x". [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:106]

```
107:             if (noiseKeyHex.startsWith(pid)) return relationship
```
> إن كان noiseKeyHex يبدأ بـ pid فيُعيد relationship. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:107]

```
108:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:108]

```
109:         return null
```
> يُعيد null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:109]

```
110:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:110]

```
111: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:111]

```
112:     /** Update Nostr public key for a peer (indexed by Noise key) */
```
> تعليق: «تحديث مفتاح Nostr العام لنِدّ (مفهرس حسب مفتاح Noise)». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:112]

```
113:     fun updateNostrPublicKey(noisePublicKey: ByteArray, nostrPubkey: String) {
```
> يُعرّف دالة updateNostrPublicKey تأخذ معاملين noisePublicKey من نوع ByteArray وnostrPubkey من نوع String، ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:113]

```
114:         val keyHex = noisePublicKey.joinToString("") { "%02x".format(it) }
```
> يُعرّف ثابتاً محلياً keyHex بقيمة دمج بايتات noisePublicKey في سلسلة ست عشرية بلا فاصل بصيغة "%02x". [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:114]

```
115:         val existing = favorites[keyHex]
```
> يُعرّف ثابتاً محلياً existing بقيمة المدخل المقابل لـ keyHex من favorites. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:115]

```
116: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:116]

```
117:         if (existing != null) {
```
> إن لم يكن existing مساوياً null يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:117]

```
118:             val updated = existing.copy(
```
> يُعرّف ثابتاً محلياً updated بقيمة نسخة معدّلة copy من existing ويفتح قائمة المعاملات المتغيّرة. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:118]

```
119:                 peerNostrPublicKey = nostrPubkey,
```
> يُسنِد إلى peerNostrPublicKey في النسخة قيمة nostrPubkey. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:119]

```
120:                 lastUpdated = Date()
```
> يُسنِد إلى lastUpdated في النسخة قيمة Date جديدة (الوقت الحالي). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:120]

```
121:             )
```
> يُغلق قائمة معاملات copy. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:121]

```
122:             favorites[keyHex] = updated
```
> يُسنِد القيمة updated إلى المفتاح keyHex في الخريطة favorites. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:122]

```
123:         } else {
```
> ينهي كتلة if ويفتح كتلة else. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:123]

```
124:             val relationship = FavoriteRelationship(
```
> يُعرّف ثابتاً محلياً relationship بقيمة نسخة جديدة من FavoriteRelationship ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:124]

```
125:                 peerNoisePublicKey = noisePublicKey,
```
> يُسنِد إلى peerNoisePublicKey قيمة noisePublicKey. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:125]

```
126:                 peerNostrPublicKey = nostrPubkey,
```
> يُسنِد إلى peerNostrPublicKey قيمة nostrPubkey. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:126]

```
127:                 peerNickname = "Unknown",
```
> يُسنِد إلى peerNickname القيمة النصّية "Unknown". [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:127]

```
128:                 isFavorite = false,
```
> يُسنِد إلى isFavorite القيمة false. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:128]

```
129:                 theyFavoritedUs = false,
```
> يُسنِد إلى theyFavoritedUs القيمة false. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:129]

```
130:                 favoritedAt = Date(),
```
> يُسنِد إلى favoritedAt قيمة Date جديدة (الوقت الحالي). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:130]

```
131:                 lastUpdated = Date()
```
> يُسنِد إلى lastUpdated قيمة Date جديدة (الوقت الحالي). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:131]

```
132:             )
```
> يُغلق قائمة معاملات الباني. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:132]

```
133:             favorites[keyHex] = relationship
```
> يُسنِد القيمة relationship إلى المفتاح keyHex في الخريطة favorites. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:133]

```
134:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:134]

```
135: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:135]

```
136:         saveFavorites()
```
> يستدعي الدالة saveFavorites. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:136]

```
137:         notifyChanged(keyHex)
```
> يستدعي الدالة notifyChanged ممرّراً keyHex. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:137]

```
138:         Log.d(TAG, "Updated Nostr pubkey association for ${keyHex.take(16)}...")
```
> يستدعي Log.d بالوسم TAG ورسالة تصحيح: "Updated Nostr pubkey association for " متبوعة بأوّل ١٦ محرفاً من keyHex عبر take(16) ثم "...". [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:138]

```
139:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:139]

```
140: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:140]

```
141: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:141]

```
142:     /** NEW: Update Nostr pubkey for specific mesh peerID (16-hex). */
```
> تعليق: «جديد: تحديث مفتاح Nostr العام لمعرّف peerID شبكي محدّد (١٦ خانة ست عشرية)». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:142]

```
143:     fun updateNostrPublicKeyForPeerID(peerID: String, nostrPubkey: String) {
```
> يُعرّف دالة updateNostrPublicKeyForPeerID تأخذ معاملين peerID وnostrPubkey كلاهما من نوع String، ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:143]

```
144:         val pid = peerID.lowercase()
```
> يُعرّف ثابتاً محلياً pid بقيمة peerID محوّلاً إلى أحرف صغيرة. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:144]

```
145:         if (pid.length == 16 && pid.matches(Regex("^[0-9a-f]+$"))) {
```
> إن كان طول pid يساوي ١٦ وكان pid يطابق التعبير النمطي Regex("^[0-9a-f]+$") (أرقام وأحرف ست عشرية صغيرة فقط) يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:145]

```
146:             peerIdIndex[pid] = nostrPubkey
```
> يُسنِد القيمة nostrPubkey إلى المفتاح pid في الخريطة peerIdIndex. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:146]

```
147:             savePeerIdIndex()
```
> يستدعي الدالة savePeerIdIndex. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:147]

```
148:             Log.d(TAG, "Indexed npub for peerID ${pid.take(8)}…")
```
> يستدعي Log.d بالوسم TAG ورسالة تصحيح: "Indexed npub for peerID " متبوعة بأوّل ٨ محارف من pid عبر take(8) ثم "…". [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:148]

```
149:         } else {
```
> ينهي كتلة if ويفتح كتلة else. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:149]

```
150:             Log.w(TAG, "updateNostrPublicKeyForPeerID called with non-16hex peerID: $peerID")
```
> يستدعي Log.w بالوسم TAG ورسالة تحذير: "updateNostrPublicKeyForPeerID called with non-16hex peerID: " متبوعة بقيمة peerID. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:150]

```
151:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:151]

```
152:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:152]

```
153: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:153]

```
154: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:154]

```
155:     /** NEW: Resolve Nostr pubkey via current peerID mapping (fast path). */
```
> تعليق: «جديد: استخراج مفتاح Nostr العام عبر ربط peerID الحالي (المسار السريع)». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:155]

```
156:     fun findNostrPubkeyForPeerID(peerID: String): String? {
```
> يُعرّف دالة findNostrPubkeyForPeerID تأخذ معاملاً peerID من نوع String وتُعيد String قابلاً للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:156]

```
157:         return peerIdIndex[peerID.lowercase()]
```
> يُعيد القيمة المقابلة لمفتاح peerID محوّلاً إلى أحرف صغيرة من الخريطة peerIdIndex. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:157]

```
158:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:158]

```
159: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:159]

```
160:     /** NEW: Resolve peerID (16-hex) for a given Nostr pubkey (npub or hex). */
```
> تعليق: «جديد: استخراج معرّف peerID (١٦ خانة ست عشرية) لمفتاح Nostr عام مُعطى (npub أو hex)». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:160]

```
161:     fun findPeerIDForNostrPubkey(nostrPubkey: String): String? {
```
> يُعرّف دالة findPeerIDForNostrPubkey تأخذ معاملاً nostrPubkey من نوع String وتُعيد String قابلاً للعدم، ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:161]

```
162:         // First, try direct match in peerIdIndex (values are stored as npub strings)
```
> تعليق: «أولاً، جرّب المطابقة المباشرة في peerIdIndex (القيم مخزّنة كسلاسل npub)». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:162]

```
163:         peerIdIndex.entries.firstOrNull { it.value.equals(nostrPubkey, ignoreCase = true) }?.let { return it.key }
```
> يبحث في مدخلات peerIdIndex عن أوّل مدخل تساوي قيمته nostrPubkey مع تجاهل حالة الأحرف عبر firstOrNull، وإن وُجد يُعيد مفتاحه عبر let. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:163]

```
164:         
```
> سطر فارغ (يحوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:164]

```
165:         // Attempt legacy mapping via favorites Noise key association
```
> تعليق: «محاولة الربط القديم عبر اقتران مفتاح Noise في favorites». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:165]

```
166:         val targetHex = normalizeNostrKeyToHex(nostrPubkey)
```
> يُعرّف ثابتاً محلياً targetHex بقيمة ناتج استدعاء normalizeNostrKeyToHex على nostrPubkey. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:166]

```
167:         if (targetHex != null) {
```
> إن لم يكن targetHex مساوياً null يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:167]

```
168:             // Find relationship with matching nostr pubkey (normalized to hex) and then try to map to current peerID via noise key prefix
```
> تعليق: «إيجاد العلاقة ذات مفتاح Nostr المطابق (مُطبَّع إلى hex) ثم محاولة الربط بمعرّف peerID الحالي عبر بادئة مفتاح Noise». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:168]

```
169:             val rel = favorites.values.firstOrNull { it.peerNostrPublicKey?.let { stored -> normalizeNostrKeyToHex(stored) } == targetHex }
```
> يُعرّف ثابتاً محلياً rel بأوّل قيمة من favorites.values يكون فيها ناتج normalizeNostrKeyToHex المطبَّق على peerNostrPublicKey (المخزّن) مساوياً targetHex، عبر firstOrNull. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:169]

```
170:             if (rel != null) {
```
> إن لم يكن rel مساوياً null يفتح كتلة الشرط. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:170]

```
171:                 val noiseHex = rel.peerNoisePublicKey.joinToString("") { "%02x".format(it) }
```
> يُعرّف ثابتاً محلياً noiseHex بقيمة دمج بايتات rel.peerNoisePublicKey في سلسلة ست عشرية بلا فاصل بصيغة "%02x". [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:171]

```
172:                 // Return 16-hex prefix as best-effort if no explicit mapping exists
```
> تعليق: «إعادة بادئة الـ١٦ خانة الست عشرية كأفضل محاولة إن لم يوجد ربط صريح». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:172]

```
173:                 return noiseHex.take(16)
```
> يُعيد أوّل ١٦ محرفاً من noiseHex عبر take(16). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:173]

```
174:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:174]

```
175:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:175]

```
176:         return null
```
> يُعيد null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:176]

```
177:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:177]

```
178: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:178]

```
179:     /** Update favorite status */
```
> تعليق: «تحديث حالة التفضيل». [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:179]

```
180:     fun updateFavoriteStatus(noisePublicKey: ByteArray, nickname: String, isFavorite: Boolean) {
```
> يُعرّف دالة updateFavoriteStatus تأخذ معاملات noisePublicKey من نوع ByteArray وnickname من نوع String وisFavorite من نوع Boolean، ويفتح جسمها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:180]

```
181:         val keyHex = noisePublicKey.joinToString("") { "%02x".format(it) }
```
> يُعرّف ثابتاً محلياً keyHex بقيمة دمج بايتات noisePublicKey في سلسلة ست عشرية بلا فاصل بصيغة "%02x". [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:181]

```
182: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:182]

```
183:         val existing = favorites[keyHex]
```
> يُعرّف ثابتاً محلياً existing بقيمة المدخل المقابل لـ keyHex من favorites. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:183]

```
184: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:184]

```
185:         val updated = if (existing != null) {
```
> يُعرّف ثابتاً محلياً updated بنتيجة تعبير شرطي if يفحص إن لم يكن existing مساوياً null، ويفتح فرع الإيجاب. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:185]

```
186:             existing.copy(
```
> يُنتج نسخة معدّلة copy من existing ويفتح قائمة معاملاتها المتغيّرة. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:186]

```
187:                 peerNickname = nickname,
```
> يُسنِد إلى peerNickname في النسخة قيمة nickname. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:187]

```
188:                 isFavorite = isFavorite,
```
> يُسنِد إلى isFavorite في النسخة قيمة المعامل isFavorite. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:188]

```
189:                 lastUpdated = Date(),
```
> يُسنِد إلى lastUpdated في النسخة قيمة Date جديدة (الوقت الحالي). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:189]

```
190:                 favoritedAt = if (isFavorite && !existing.isFavorite) Date() else existing.favoritedAt
```
> يُسنِد إلى favoritedAt في النسخة قيمة Date جديدة إن كان isFavorite صحيحاً وكان existing.isFavorite غير صحيح، وإلّا قيمة existing.favoritedAt. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:190]

```
191:             )
```
> يُغلق قائمة معاملات copy. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:191]

```
192:         } else {
```
> ينهي فرع الإيجاب ويفتح فرع else للتعبير الشرطي. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:192]

```
193:             FavoriteRelationship(
```
> يُنشئ نسخة جديدة من FavoriteRelationship ويفتح قائمة معاملاتها. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:193]

```
194:                 peerNoisePublicKey = noisePublicKey,
```
> يُسنِد إلى peerNoisePublicKey قيمة noisePublicKey. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:194]

```
195:                 peerNostrPublicKey = null,
```
> يُسنِد إلى peerNostrPublicKey القيمة null. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:195]

```
196:                 peerNickname = nickname,
```
> يُسنِد إلى peerNickname قيمة nickname. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:196]

```
197:                 isFavorite = isFavorite,
```
> يُسنِد إلى isFavorite قيمة المعامل isFavorite. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:197]

```
198:                 theyFavoritedUs = false,
```
> يُسنِد إلى theyFavoritedUs القيمة false. [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:198]

```
199:                 favoritedAt = Date(),
```
> يُسنِد إلى favoritedAt قيمة Date جديدة (الوقت الحالي). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:199]

```
200:                 lastUpdated = Date()
```
> يُسنِد إلى lastUpdated قيمة Date جديدة (الوقت الحالي). [app/src/main/java/com/bitchat/android/favorites/FavoritesPersistenceService.kt:200]
