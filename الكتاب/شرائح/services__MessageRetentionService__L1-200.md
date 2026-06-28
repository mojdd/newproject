# شريحة — app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt (الأسطر 1–200)

```
1: //package com.bitchat.android.services
```
> سطر معلّق (مُعطّل بشرطتين مائلتين) يحوي تصريح الحزمة (package) باسم `com.bitchat.android.services`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:1]

```
2: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:2]

```
3: //import android.content.Context
```
> سطر معلّق يحوي استيراد (import) للصنف `Context` من `android.content`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:3]

```
4: //import android.content.SharedPreferences
```
> سطر معلّق يحوي استيراد للصنف `SharedPreferences` (التفضيلات المشتركة) من `android.content`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:4]

```
5: //import android.util.Log
```
> سطر معلّق يحوي استيراد للصنف `Log` (سجلّ التتبّع) من `android.util`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:5]

```
6: //import kotlinx.coroutines.Dispatchers
```
> سطر معلّق يحوي استيراد للكائن `Dispatchers` (موزِّعات التنفيذ) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:6]

```
7: //import kotlinx.coroutines.withContext
```
> سطر معلّق يحوي استيراد للدالة `withContext` (التنفيذ ضمن سياق) من `kotlinx.coroutines`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:7]

```
8: //import java.io.File
```
> سطر معلّق يحوي استيراد للصنف `File` (ملف) من `java.io`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:8]

```
9: //import java.io.FileInputStream
```
> سطر معلّق يحوي استيراد للصنف `FileInputStream` (مجرى إدخال من ملف) من `java.io`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:9]

```
10: //import java.io.FileOutputStream
```
> سطر معلّق يحوي استيراد للصنف `FileOutputStream` (مجرى إخراج إلى ملف) من `java.io`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:10]

```
11: //import java.io.ObjectInputStream
```
> سطر معلّق يحوي استيراد للصنف `ObjectInputStream` (مجرى قراءة كائنات) من `java.io`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:11]

```
12: //import java.io.ObjectOutputStream
```
> سطر معلّق يحوي استيراد للصنف `ObjectOutputStream` (مجرى كتابة كائنات) من `java.io`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:12]

```
13: //import java.util.*
```
> سطر معلّق يحوي استيراداً شاملاً (بنجمة) لكل عناصر الحزمة `java.util`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:13]

```
14: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:14]

```
15: ///**
```
> سطر معلّق يبدأ تعليق توثيق (KDoc) بفتح `/**`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:15]

```
16: // * Message retention service for saving channel messages locally
```
> تعليق توثيق: «خدمة الاحتفاظ بالرسائل لحفظ رسائل القناة محلياً». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:16]

```
17: // * Matches iOS MessageRetentionService functionality
```
> تعليق توثيق: «يطابق وظيفة MessageRetentionService في نظام iOS». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:17]

```
18: // */
```
> سطر معلّق يُنهي تعليق التوثيق بإغلاق `*/`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:18]

```
19: //class MessageRetentionService private constructor(private val context: Context) {
```
> سطر معلّق يُعرِّف الصنف `MessageRetentionService` (خدمة الاحتفاظ بالرسائل) ذا باني (constructor) خاصّ يأخذ مُعامِلاً خاصّاً للقراءة فقط اسمه `context` من نوع `Context`، ويفتح جسم الصنف. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:19]

```
20: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:20]

```
21: //    companion object {
```
> سطر معلّق يفتح كائناً مرافقاً (companion object). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:21]

```
22: //        private const val TAG = "MessageRetentionService"
```
> سطر معلّق يُعرِّف ثابتاً خاصّاً اسمه `TAG` (وَسْم) بقيمة نصّية `"MessageRetentionService"`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:22]

```
23: //        private const val PREF_NAME = "message_retention"
```
> سطر معلّق يُعرِّف ثابتاً خاصّاً اسمه `PREF_NAME` (اسم ملف التفضيلات) بقيمة نصّية `"message_retention"`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:23]

```
24: //        private const val KEY_FAVORITE_CHANNELS = "favorite_channels"
```
> سطر معلّق يُعرِّف ثابتاً خاصّاً اسمه `KEY_FAVORITE_CHANNELS` (مفتاح القنوات المفضّلة) بقيمة نصّية `"favorite_channels"`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:24]

```
25: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:25]

```
26: //        @Volatile
```
> سطر معلّق يحوي التعليمة التوصيفية (annotation) `@Volatile` (متطايرة) المطبَّقة على ما يليها. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:26]

```
27: //        private var INSTANCE: MessageRetentionService? = null
```
> سطر معلّق يُعرِّف متغيّراً خاصّاً قابلاً للتغيير اسمه `INSTANCE` (النسخة الوحيدة) من نوع `MessageRetentionService` يقبل العدم، مُهيّأً بقيمة `null`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:27]

```
28: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:28]

```
29: //        fun getInstance(context: Context): MessageRetentionService {
```
> سطر معلّق يُعرِّف دالة `getInstance` (جلب النسخة) تأخذ مُعامِلاً `context` من نوع `Context` وتعيد `MessageRetentionService`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:29]

```
30: //            return INSTANCE ?: synchronized(this) {
```
> سطر معلّق يعيد قيمة `INSTANCE`، وإن كانت عدماً فيدخل كتلة متزامنة `synchronized(this)`، ويفتح جسمها. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:30]

```
31: //                INSTANCE ?: MessageRetentionService(context.applicationContext).also { INSTANCE = it }
```
> سطر معلّق يعيد قيمة `INSTANCE`، وإن كانت عدماً يُنشئ نسخة `MessageRetentionService` بمُعامِل `context.applicationContext` ثم بدالة `also` يُسنِد تلك النسخة إلى `INSTANCE`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:31]

```
32: //            }
```
> سطر معلّق يحوي إغلاق نطاق الكتلة المتزامنة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:32]

```
33: //        }
```
> سطر معلّق يحوي إغلاق نطاق دالة `getInstance`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:33]

```
34: //    }
```
> سطر معلّق يحوي إغلاق نطاق الكائن المرافق. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:34]

```
35: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:35]

```
36: //    private val prefs: SharedPreferences = context.getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE)
```
> سطر معلّق يُعرِّف حقلاً خاصّاً للقراءة فقط اسمه `prefs` (التفضيلات) من نوع `SharedPreferences` بقيمة ناتجة عن استدعاء `context.getSharedPreferences` بالمُعامِلين `PREF_NAME` و`Context.MODE_PRIVATE`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:36]

```
37: //    private val retentionDir = File(context.filesDir, "retained_messages")
```
> سطر معلّق يُعرِّف حقلاً خاصّاً للقراءة فقط اسمه `retentionDir` (مجلّد الاحتفاظ) بقيمة كائن `File` مُنشأ من `context.filesDir` والاسم `"retained_messages"`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:37]

```
38: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:38]

```
39: //    init {
```
> سطر معلّق يفتح كتلة تهيئة (init). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:39]

```
40: //        if (!retentionDir.exists()) {
```
> سطر معلّق يحوي شرطاً `if` يختبر نفي وجود المجلّد عبر `!retentionDir.exists()`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:40]

```
41: //            retentionDir.mkdirs()
```
> سطر معلّق يستدعي `retentionDir.mkdirs()` لإنشاء المجلّد ومجلّداته الأبوية. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:41]

```
42: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:42]

```
43: //    }
```
> سطر معلّق يحوي إغلاق نطاق كتلة التهيئة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:43]

```
44: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:44]

```
45: //    // MARK: - Channel Bookmarking (Favorites)
```
> سطر معلّق يحوي تعليقاً واسماً للقسم: «MARK: - وضع إشارة مرجعية للقناة (المفضّلات)». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:45]

```
46: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:46]

```
47: //    fun getFavoriteChannels(): Set<String> {
```
> سطر معلّق يُعرِّف دالة `getFavoriteChannels` (جلب القنوات المفضّلة) بلا مُعامِلات تعيد `Set<String>`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:47]

```
48: //        return prefs.getStringSet(KEY_FAVORITE_CHANNELS, emptySet()) ?: emptySet()
```
> سطر معلّق يعيد نتيجة `prefs.getStringSet` بالمفتاح `KEY_FAVORITE_CHANNELS` وقيمة افتراضية `emptySet()`، وإن كانت النتيجة عدماً فيعيد `emptySet()`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:48]

```
49: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `getFavoriteChannels`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:49]

```
50: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:50]

```
51: //    fun toggleFavoriteChannel(channel: String): Boolean {
```
> سطر معلّق يُعرِّف دالة `toggleFavoriteChannel` (تبديل تفضيل القناة) تأخذ مُعامِلاً `channel` من نوع `String` وتعيد `Boolean`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:51]

```
52: //        val currentFavorites = getFavoriteChannels().toMutableSet()
```
> سطر معلّق يُعرِّف متغيّراً للقراءة فقط اسمه `currentFavorites` (المفضّلات الحالية) بقيمة ناتج `getFavoriteChannels()` محوَّلاً إلى مجموعة قابلة للتغيير عبر `toMutableSet()`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:52]

```
53: //        val wasAdded = if (currentFavorites.contains(channel)) {
```
> سطر معلّق يُعرِّف متغيّراً للقراءة فقط اسمه `wasAdded` (هل أُضيفت) بقيمة تعبير `if` يختبر `currentFavorites.contains(channel)`، ويفتح فرع التحقّق. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:53]

```
54: //            currentFavorites.remove(channel)
```
> سطر معلّق يستدعي `currentFavorites.remove(channel)` لإزالة القناة من المجموعة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:54]

```
55: //            false
```
> سطر معلّق يحوي القيمة `false` كقيمة ناتجة لفرع `if`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:55]

```
56: //        } else {
```
> سطر معلّق يُغلق فرع `if` ويفتح فرع `else`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:56]

```
57: //            currentFavorites.add(channel)
```
> سطر معلّق يستدعي `currentFavorites.add(channel)` لإضافة القناة إلى المجموعة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:57]

```
58: //            true
```
> سطر معلّق يحوي القيمة `true` كقيمة ناتجة لفرع `else`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:58]

```
59: //        }
```
> سطر معلّق يحوي إغلاق نطاق تعبير `if/else`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:59]

```
60: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:60]

```
61: //        prefs.edit().putStringSet(KEY_FAVORITE_CHANNELS, currentFavorites).apply()
```
> سطر معلّق يستدعي `prefs.edit()` ثم `putStringSet` بالمفتاح `KEY_FAVORITE_CHANNELS` والقيمة `currentFavorites` ثم `apply()` لحفظ المجموعة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:61]

```
62: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:62]

```
63: //        if (!wasAdded) {
```
> سطر معلّق يحوي شرطاً `if` يختبر نفي `wasAdded` عبر `!wasAdded`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:63]

```
64: //            // Channel removed from favorites - delete saved messages in background
```
> سطر معلّق يحوي تعليقاً: «أُزيلت القناة من المفضّلات - احذف الرسائل المحفوظة في الخلفية». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:64]

```
65: //            Thread {
```
> سطر معلّق يُنشئ خيطاً (Thread) بفتح كتلة تنفيذه. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:65]

```
66: //                try {
```
> سطر معلّق يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:66]

```
67: //                    val channelFile = getChannelFile(channel)
```
> سطر معلّق يُعرِّف متغيّراً للقراءة فقط اسمه `channelFile` (ملف القناة) بقيمة ناتج `getChannelFile(channel)`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:67]

```
68: //                    if (channelFile.exists()) {
```
> سطر معلّق يحوي شرطاً `if` يختبر `channelFile.exists()`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:68]

```
69: //                        channelFile.delete()
```
> سطر معلّق يستدعي `channelFile.delete()` لحذف الملف. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:69]

```
70: //                        Log.d(TAG, "Deleted saved messages for channel $channel")
```
> سطر معلّق يستدعي `Log.d` بالوَسْم `TAG` ورسالة «حُذفت الرسائل المحفوظة للقناة $channel». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:70]

```
71: //                    }
```
> سطر معلّق يحوي إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:71]

```
72: //                } catch (e: Exception) {
```
> سطر معلّق يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:72]

```
73: //                    Log.e(TAG, "Failed to delete messages for channel $channel", e)
```
> سطر معلّق يستدعي `Log.e` بالوَسْم `TAG` ورسالة «فشل حذف رسائل القناة $channel» والاستثناء `e`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:73]

```
74: //                }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:74]

```
75: //            }.start()
```
> سطر معلّق يُغلق كتلة الخيط ويستدعي عليه `.start()` لبدء تنفيذه. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:75]

```
76: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة الشرط `if (!wasAdded)`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:76]

```
77: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:77]

```
78: //        Log.d(TAG, "Channel $channel ${if (wasAdded) "bookmarked" else "unbookmarked"}")
```
> سطر معلّق يستدعي `Log.d` بالوَسْم `TAG` ورسالة «Channel $channel» يتبعها تعبير `if (wasAdded)` يُخرِج `"bookmarked"` (مُؤشَّرة) أو `"unbookmarked"` (غير مُؤشَّرة). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:78]

```
79: //        return wasAdded
```
> سطر معلّق يعيد قيمة `wasAdded`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:79]

```
80: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `toggleFavoriteChannel`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:80]

```
81: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:81]

```
82: //    fun isChannelBookmarked(channel: String): Boolean {
```
> سطر معلّق يُعرِّف دالة `isChannelBookmarked` (هل القناة مُؤشَّرة) تأخذ مُعامِلاً `channel` من نوع `String` وتعيد `Boolean`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:82]

```
83: //        return getFavoriteChannels().contains(channel)
```
> سطر معلّق يعيد نتيجة `getFavoriteChannels().contains(channel)`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:83]

```
84: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `isChannelBookmarked`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:84]

```
85: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:85]

```
86: //    // MARK: - Message Storage
```
> سطر معلّق يحوي تعليقاً واسماً للقسم: «MARK: - تخزين الرسائل». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:86]

```
87: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:87]

```
88: //    suspend fun saveMessage(message: BitchatMessage, forChannel: String) = withContext(Dispatchers.IO) {
```
> سطر معلّق يُعرِّف دالة معلّقة (suspend) اسمها `saveMessage` (حفظ الرسالة) تأخذ مُعامِلين `message` من نوع `BitchatMessage` و`forChannel` من نوع `String`، وجسمها هو تعبير `withContext(Dispatchers.IO)` ويفتح كتلته. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:88]

```
89: //        if (!isChannelBookmarked(forChannel)) {
```
> سطر معلّق يحوي شرطاً `if` يختبر نفي `isChannelBookmarked(forChannel)`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:89]

```
90: //            Log.w(TAG, "Attempted to save message for non-bookmarked channel: $forChannel")
```
> سطر معلّق يستدعي `Log.w` بالوَسْم `TAG` ورسالة «حاول حفظ رسالة لقناة غير مُؤشَّرة: $forChannel». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:90]

```
91: //            return@withContext
```
> سطر معلّق يحوي `return@withContext` للخروج من كتلة `withContext` بلا قيمة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:91]

```
92: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:92]

```
93: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:93]

```
94: //        try {
```
> سطر معلّق يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:94]

```
95: //            val channelFile = getChannelFile(forChannel)
```
> سطر معلّق يُعرِّف متغيّراً للقراءة فقط اسمه `channelFile` بقيمة ناتج `getChannelFile(forChannel)`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:95]

```
96: //            val existingMessages = loadMessagesFromFile(channelFile).toMutableList()
```
> سطر معلّق يُعرِّف متغيّراً للقراءة فقط اسمه `existingMessages` (الرسائل الموجودة) بقيمة ناتج `loadMessagesFromFile(channelFile)` محوَّلاً إلى قائمة قابلة للتغيير عبر `toMutableList()`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:96]

```
97: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:97]

```
98: //            // Check if message already exists (by ID)
```
> سطر معلّق يحوي تعليقاً: «تحقّق إن كانت الرسالة موجودة سلفاً (بالمعرّف)». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:98]

```
99: //            if (existingMessages.any { it.id == message.id }) {
```
> سطر معلّق يحوي شرطاً `if` يختبر `existingMessages.any { it.id == message.id }`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:99]

```
100: //                Log.d(TAG, "Message ${message.id} already saved for channel $forChannel")
```
> سطر معلّق يستدعي `Log.d` بالوَسْم `TAG` ورسالة «الرسالة ${message.id} محفوظة سلفاً للقناة $forChannel». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:100]

```
101: //                return@withContext
```
> سطر معلّق يحوي `return@withContext` للخروج من كتلة `withContext` بلا قيمة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:101]

```
102: //            }
```
> سطر معلّق يحوي إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:102]

```
103: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:103]

```
104: //            // Add new message
```
> سطر معلّق يحوي تعليقاً: «أضف رسالة جديدة». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:104]

```
105: //            existingMessages.add(message)
```
> سطر معلّق يستدعي `existingMessages.add(message)` لإضافة الرسالة إلى القائمة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:105]

```
106: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:106]

```
107: //            // Sort by timestamp
```
> سطر معلّق يحوي تعليقاً: «رتّب حسب الطابع الزمني». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:107]

```
108: //            existingMessages.sortBy { it.timestamp }
```
> سطر معلّق يستدعي `existingMessages.sortBy { it.timestamp }` لترتيب القائمة وفق `timestamp`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:108]

```
109: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:109]

```
110: //            // Save back to file
```
> سطر معلّق يحوي تعليقاً: «احفظ مجدّداً إلى الملف». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:110]

```
111: //            saveMessagesToFile(channelFile, existingMessages)
```
> سطر معلّق يستدعي `saveMessagesToFile` بالمُعامِلين `channelFile` و`existingMessages`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:111]

```
112: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:112]

```
113: //            Log.d(TAG, "Saved message ${message.id} for channel $forChannel")
```
> سطر معلّق يستدعي `Log.d` بالوَسْم `TAG` ورسالة «حُفظت الرسالة ${message.id} للقناة $forChannel». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:113]

```
114: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:114]

```
115: //        } catch (e: Exception) {
```
> سطر معلّق يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:115]

```
116: //            Log.e(TAG, "Failed to save message for channel $forChannel", e)
```
> سطر معلّق يستدعي `Log.e` بالوَسْم `TAG` ورسالة «فشل حفظ رسالة القناة $forChannel» والاستثناء `e`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:116]

```
117: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:117]

```
118: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `saveMessage`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:118]

```
119: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:119]

```
120: //    suspend fun loadMessagesForChannel(channel: String): List<BitchatMessage> = withContext(Dispatchers.IO) {
```
> سطر معلّق يُعرِّف دالة معلّقة اسمها `loadMessagesForChannel` (تحميل رسائل القناة) تأخذ مُعامِلاً `channel` من نوع `String` وتعيد `List<BitchatMessage>`، وجسمها تعبير `withContext(Dispatchers.IO)` ويفتح كتلته. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:120]

```
121: //        if (!isChannelBookmarked(channel)) {
```
> سطر معلّق يحوي شرطاً `if` يختبر نفي `isChannelBookmarked(channel)`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:121]

```
122: //            Log.d(TAG, "Channel $channel not bookmarked, returning empty list")
```
> سطر معلّق يستدعي `Log.d` بالوَسْم `TAG` ورسالة «القناة $channel غير مُؤشَّرة، تُعاد قائمة فارغة». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:122]

```
123: //            return@withContext emptyList()
```
> سطر معلّق يحوي `return@withContext emptyList()` للخروج بإعادة قائمة فارغة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:123]

```
124: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:124]

```
125: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:125]

```
126: //        try {
```
> سطر معلّق يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:126]

```
127: //            val channelFile = getChannelFile(channel)
```
> سطر معلّق يُعرِّف متغيّراً للقراءة فقط اسمه `channelFile` بقيمة ناتج `getChannelFile(channel)`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:127]

```
128: //            val messages = loadMessagesFromFile(channelFile)
```
> سطر معلّق يُعرِّف متغيّراً للقراءة فقط اسمه `messages` (الرسائل) بقيمة ناتج `loadMessagesFromFile(channelFile)`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:128]

```
129: //            Log.d(TAG, "Loaded ${messages.size} messages for channel $channel")
```
> سطر معلّق يستدعي `Log.d` بالوَسْم `TAG` ورسالة «حُمِّلت ${messages.size} رسالة للقناة $channel». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:129]

```
130: //            return@withContext messages
```
> سطر معلّق يحوي `return@withContext messages` للخروج بإعادة `messages`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:130]

```
131: //        } catch (e: Exception) {
```
> سطر معلّق يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:131]

```
132: //            Log.e(TAG, "Failed to load messages for channel $channel", e)
```
> سطر معلّق يستدعي `Log.e` بالوَسْم `TAG` ورسالة «فشل تحميل رسائل القناة $channel» والاستثناء `e`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:132]

```
133: //            return@withContext emptyList()
```
> سطر معلّق يحوي `return@withContext emptyList()` للخروج بإعادة قائمة فارغة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:133]

```
134: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:134]

```
135: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `loadMessagesForChannel`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:135]

```
136: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:136]

```
137: //    suspend fun deleteMessagesForChannel(channel: String): Unit = withContext(Dispatchers.IO) {
```
> سطر معلّق يُعرِّف دالة معلّقة اسمها `deleteMessagesForChannel` (حذف رسائل القناة) تأخذ مُعامِلاً `channel` من نوع `String` وتعيد `Unit`، وجسمها تعبير `withContext(Dispatchers.IO)` ويفتح كتلته. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:137]

```
138: //        try {
```
> سطر معلّق يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:138]

```
139: //            val channelFile = getChannelFile(channel)
```
> سطر معلّق يُعرِّف متغيّراً للقراءة فقط اسمه `channelFile` بقيمة ناتج `getChannelFile(channel)`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:139]

```
140: //            if (channelFile.exists()) {
```
> سطر معلّق يحوي شرطاً `if` يختبر `channelFile.exists()`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:140]

```
141: //                channelFile.delete()
```
> سطر معلّق يستدعي `channelFile.delete()` لحذف الملف. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:141]

```
142: //                Log.d(TAG, "Deleted saved messages for channel $channel")
```
> سطر معلّق يستدعي `Log.d` بالوَسْم `TAG` ورسالة «حُذفت الرسائل المحفوظة للقناة $channel». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:142]

```
143: //            }
```
> سطر معلّق يحوي إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:143]

```
144: //        } catch (e: Exception) {
```
> سطر معلّق يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:144]

```
145: //            Log.e(TAG, "Failed to delete messages for channel $channel", e)
```
> سطر معلّق يستدعي `Log.e` بالوَسْم `TAG` ورسالة «فشل حذف رسائل القناة $channel» والاستثناء `e`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:145]

```
146: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:146]

```
147: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `deleteMessagesForChannel`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:147]

```
148: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:148]

```
149: //    suspend fun deleteAllStoredMessages(): Unit = withContext(Dispatchers.IO) {
```
> سطر معلّق يُعرِّف دالة معلّقة اسمها `deleteAllStoredMessages` (حذف كل الرسائل المخزّنة) بلا مُعامِلات تعيد `Unit`، وجسمها تعبير `withContext(Dispatchers.IO)` ويفتح كتلته. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:149]

```
150: //        try {
```
> سطر معلّق يفتح كتلة `try`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:150]

```
151: //            if (retentionDir.exists()) {
```
> سطر معلّق يحوي شرطاً `if` يختبر `retentionDir.exists()`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:151]

```
152: //                retentionDir.listFiles()?.forEach { file ->
```
> سطر معلّق يستدعي `retentionDir.listFiles()` ثم بأمان عبر `?.forEach` يمرّ على كل `file`، ويفتح كتلة اللامدا. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:152]

```
153: //                    file.delete()
```
> سطر معلّق يستدعي `file.delete()` لحذف الملف الحالي. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:153]

```
154: //                }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `forEach`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:154]

```
155: //                Log.d(TAG, "Deleted all stored messages")
```
> سطر معلّق يستدعي `Log.d` بالوَسْم `TAG` ورسالة «حُذفت كل الرسائل المخزّنة». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:155]

```
156: //            }
```
> سطر معلّق يحوي إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:156]

```
157: //        } catch (e: Exception) {
```
> سطر معلّق يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:157]

```
158: //            Log.e(TAG, "Failed to delete all stored messages", e)
```
> سطر معلّق يستدعي `Log.e` بالوَسْم `TAG` ورسالة «فشل حذف كل الرسائل المخزّنة» والاستثناء `e`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:158]

```
159: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `catch`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:159]

```
160: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `deleteAllStoredMessages`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:160]

```
161: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:161]

```
162: //    // MARK: - File Operations
```
> سطر معلّق يحوي تعليقاً واسماً للقسم: «MARK: - عمليات الملفات». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:162]

```
163: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:163]

```
164: //    private fun getChannelFile(channel: String): File {
```
> سطر معلّق يُعرِّف دالة خاصّة اسمها `getChannelFile` (جلب ملف القناة) تأخذ مُعامِلاً `channel` من نوع `String` وتعيد `File`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:164]

```
165: //        // Sanitize channel name for filename
```
> سطر معلّق يحوي تعليقاً: «نقِّ اسم القناة ليصلح اسماً للملف». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:165]

```
166: //        val sanitizedChannel = channel.replace("[^a-zA-Z0-9_-]".toRegex(), "_")
```
> سطر معلّق يُعرِّف متغيّراً للقراءة فقط اسمه `sanitizedChannel` (القناة المُنقّاة) بقيمة `channel.replace` يستبدل بالتعبير النمطي `"[^a-zA-Z0-9_-]"` كل حرف ليس حرفاً أو رقماً أو شرطة سفلية أو واصلة بالرمز `"_"`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:166]

```
167: //        return File(retentionDir, "channel_${sanitizedChannel}.dat")
```
> سطر معلّق يعيد كائن `File` مُنشأ من `retentionDir` والاسم `"channel_${sanitizedChannel}.dat"`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:167]

```
168: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `getChannelFile`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:168]

```
169: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:169]

```
170: //    private fun loadMessagesFromFile(file: File): List<BitchatMessage> {
```
> سطر معلّق يُعرِّف دالة خاصّة اسمها `loadMessagesFromFile` (تحميل الرسائل من ملف) تأخذ مُعامِلاً `file` من نوع `File` وتعيد `List<BitchatMessage>`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:170]

```
171: //        if (!file.exists()) {
```
> سطر معلّق يحوي شرطاً `if` يختبر نفي `file.exists()`، ويفتح جسم الشرط. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:171]

```
172: //            return emptyList()
```
> سطر معلّق يعيد `emptyList()` (قائمة فارغة). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:172]

```
173: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة الشرط `if`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:173]

```
174: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:174]

```
175: //        return try {
```
> سطر معلّق يعيد قيمة تعبير `try`، ويفتح كتلة `try`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:175]

```
176: //            FileInputStream(file).use { fis ->
```
> سطر معلّق يُنشئ `FileInputStream(file)` ويستدعي عليه `use` بمعامِل اللامدا `fis`، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:176]

```
177: //                ObjectInputStream(fis).use { ois ->
```
> سطر معلّق يُنشئ `ObjectInputStream(fis)` ويستدعي عليه `use` بمعامِل اللامدا `ois`، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:177]

```
178: //                    @Suppress("UNCHECKED_CAST")
```
> سطر معلّق يحوي التعليمة التوصيفية `@Suppress("UNCHECKED_CAST")` لكتم تحذير التحويل غير المُتحقَّق منه. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:178]

```
179: //                    ois.readObject() as List<BitchatMessage>
```
> سطر معلّق يستدعي `ois.readObject()` ويحوّل ناتجه بـ`as` إلى `List<BitchatMessage>`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:179]

```
180: //                }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `use` الخاصّة بـ`ois`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:180]

```
181: //            }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `use` الخاصّة بـ`fis`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:181]

```
182: //        } catch (e: Exception) {
```
> سطر معلّق يُغلق كتلة `try` ويفتح كتلة `catch` تلتقط استثناءً `e` من نوع `Exception`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:182]

```
183: //            Log.w(TAG, "Failed to load messages from ${file.name}, returning empty list", e)
```
> سطر معلّق يستدعي `Log.w` بالوَسْم `TAG` ورسالة «فشل تحميل الرسائل من ${file.name}، تُعاد قائمة فارغة» والاستثناء `e`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:183]

```
184: //            emptyList()
```
> سطر معلّق يحوي `emptyList()` كقيمة ناتجة لكتلة `catch`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:184]

```
185: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `catch` (وتعبير `try`). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:185]

```
186: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `loadMessagesFromFile`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:186]

```
187: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:187]

```
188: //    private fun saveMessagesToFile(file: File, messages: List<BitchatMessage>) {
```
> سطر معلّق يُعرِّف دالة خاصّة اسمها `saveMessagesToFile` (حفظ الرسائل إلى ملف) تأخذ مُعامِلين `file` من نوع `File` و`messages` من نوع `List<BitchatMessage>`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:188]

```
189: //        FileOutputStream(file).use { fos ->
```
> سطر معلّق يُنشئ `FileOutputStream(file)` ويستدعي عليه `use` بمعامِل اللامدا `fos`، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:189]

```
190: //            ObjectOutputStream(fos).use { oos ->
```
> سطر معلّق يُنشئ `ObjectOutputStream(fos)` ويستدعي عليه `use` بمعامِل اللامدا `oos`، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:190]

```
191: //                oos.writeObject(messages)
```
> سطر معلّق يستدعي `oos.writeObject(messages)` لكتابة قائمة الرسائل. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:191]

```
192: //            }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `use` الخاصّة بـ`oos`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:192]

```
193: //        }
```
> سطر معلّق يحوي إغلاق نطاق كتلة `use` الخاصّة بـ`fos`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:193]

```
194: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `saveMessagesToFile`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:194]

```
195: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:195]

```
196: //    // MARK: - Statistics
```
> سطر معلّق يحوي تعليقاً واسماً للقسم: «MARK: - إحصاءات». [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:196]

```
197: //
```
> تعليق فارغ (شرطتان مائلتان بلا نص). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:197]

```
198: //    fun getBookmarkedChannelsCount(): Int {
```
> سطر معلّق يُعرِّف دالة `getBookmarkedChannelsCount` (جلب عدد القنوات المُؤشَّرة) بلا مُعامِلات تعيد `Int`، ويفتح جسم الدالة. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:198]

```
199: //        return getFavoriteChannels().size
```
> سطر معلّق يعيد `getFavoriteChannels().size` (حجم مجموعة القنوات المفضّلة). [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:199]

```
200: //    }
```
> سطر معلّق يحوي إغلاق نطاق دالة `getBookmarkedChannelsCount`. [app/src/main/java/com/bitchat/android/services/MessageRetentionService.kt:200]
