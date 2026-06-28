# شريحة — app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt (الأسطر 201–247)

```
201:                     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:201]

```
202:                 } else {
```
> إغلاق نطاق ثم بدء فرع وإلّا (else) لجملة شرطية سابقة. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:202]

```
203:                     val center = Geohash.decodeToCenter(gh)
```
> يُعرَّف متغيّر ثابت اسمه «المركز» (center) ويُسنَد إليه ناتج استدعاء الدالّة decodeToCenter من الكائن Geohash مع تمرير المعامل gh. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:203]

```
204:                     val list = geocoderProvider.getFromLocation(center.first, center.second, 1)
```
> يُعرَّف متغيّر ثابت اسمه «القائمة» (list) ويُسنَد إليه ناتج استدعاء الدالّة getFromLocation من مزوّد المُرَمِّز الجغرافي (geocoderProvider) مع تمرير العنصر الأول (first) للمركز والعنصر الثاني (second) للمركز والقيمة 1. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:204]

```
205:                     val a = list.firstOrNull()
```
> يُعرَّف متغيّر ثابت اسمه a ويُسنَد إليه ناتج استدعاء الدالّة firstOrNull على «القائمة» (list). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:205]

```
206:                     pickNameForLength(gh.length, a)
```
> تُستدعى الدالّة pickNameForLength مع تمرير خاصّية length للمعامل gh والمتغيّر a. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:206]

```
207:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:207]

```
208: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:208]

```
209:                 if (!name.isNullOrEmpty()) {
```
> جملة شرطية (if) شرطها نفي (!) ناتج استدعاء الدالّة isNullOrEmpty على المتغيّر name. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:209]

```
210:                     val current = _bookmarkNames.value.toMutableMap()
```
> يُعرَّف متغيّر ثابت اسمه «الحالي» (current) ويُسنَد إليه ناتج استدعاء الدالّة toMutableMap على خاصّية value للحقل _bookmarkNames. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:210]

```
211:                     current[gh] = name
```
> يُسنَد المتغيّر name إلى عنصر الخريطة «الحالي» (current) عند المفتاح gh. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:211]

```
212:                     _bookmarkNames.value = current
```
> تُسنَد قيمة المتغيّر «الحالي» (current) إلى خاصّية value للحقل _bookmarkNames. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:212]

```
213:                     persistNames(current)
```
> تُستدعى الدالّة persistNames مع تمرير المتغيّر «الحالي» (current). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:213]

```
214:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:214]

```
215:             } catch (e: Exception) {
```
> إغلاق نطاق ثم بدء فقرة التقاط (catch) لاستثناء من النوع Exception يُسمّى e. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:215]

```
216:                 Log.w(TAG, "Name resolution failed for #$gh: ${e.message}")
```
> تُستدعى الدالّة w من الكائن Log مع تمرير الوسم TAG ونصّ يحتوي على «Name resolution failed for #» متبوعاً بقيمة gh ثم «: » ثم خاصّية message للاستثناء e. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:216]

```
217:             } finally {
```
> إغلاق نطاق ثم بدء فقرة أخيراً (finally). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:217]

```
218:                 resolving.remove(gh)
```
> تُستدعى الدالّة remove على المجموعة «قيد الحلّ» (resolving) مع تمرير المفتاح gh. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:218]

```
219:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:219]

```
220:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:220]

```
221:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:221]

```
222: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:222]

```
223:     private fun pickNameForLength(len: Int, address: android.location.Address?): String? {
```
> تُعرَّف دالّة خاصّة (private) اسمها pickNameForLength تأخذ معاملاً «الطول» (len) من النوع Int ومعاملاً «العنوان» (address) من النوع android.location.Address القابل للعدم، وتُعيد قيمة من النوع String القابل للعدم. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:223]

```
224:         if (address == null) return null
```
> جملة شرطية (if): إذا كان المعامل «العنوان» (address) يساوي null فتُعيد الدالّة null. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:224]

```
225:         return when (len) {
```
> تُعيد الدالّة ناتج تعبير when على المعامل «الطول» (len). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:225]

```
226:             in 0..2 -> address.adminArea ?: address.countryName
```
> فرع when: إذا كان «الطول» (len) ضمن المدى من 0 إلى 2 فالنتيجة خاصّية adminArea للعنوان وإلّا (?:) خاصّية countryName للعنوان. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:226]

```
227:             in 3..4 -> address.adminArea ?: address.subAdminArea ?: address.countryName
```
> فرع when: إذا كان «الطول» (len) ضمن المدى من 3 إلى 4 فالنتيجة خاصّية adminArea للعنوان وإلّا (?:) خاصّية subAdminArea للعنوان وإلّا (?:) خاصّية countryName للعنوان. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:227]

```
228:             5 -> address.locality ?: address.subAdminArea ?: address.adminArea
```
> فرع when: إذا كان «الطول» (len) يساوي 5 فالنتيجة خاصّية locality للعنوان وإلّا (?:) خاصّية subAdminArea للعنوان وإلّا (?:) خاصّية adminArea للعنوان. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:228]

```
229:             in 6..7 -> address.subLocality ?: address.locality ?: address.adminArea
```
> فرع when: إذا كان «الطول» (len) ضمن المدى من 6 إلى 7 فالنتيجة خاصّية subLocality للعنوان وإلّا (?:) خاصّية locality للعنوان وإلّا (?:) خاصّية adminArea للعنوان. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:229]

```
230:             else -> address.subLocality ?: address.locality ?: address.adminArea ?: address.countryName
```
> فرع when الافتراضي (else): النتيجة خاصّية subLocality للعنوان وإلّا (?:) خاصّية locality للعنوان وإلّا (?:) خاصّية adminArea للعنوان وإلّا (?:) خاصّية countryName للعنوان. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:230]

```
231:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:231]

```
232:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:232]

```
233: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:233]

```
234:     private fun persist(list: List<String>) {
```
> تُعرَّف دالّة خاصّة (private) اسمها persist تأخذ معاملاً «القائمة» (list) من النوع List من String. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:234]

```
235:         try {
```
> بدء فقرة المحاولة (try). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:235]

```
236:             val json = gson.toJson(list)
```
> يُعرَّف متغيّر ثابت اسمه json ويُسنَد إليه ناتج استدعاء الدالّة toJson من الكائن gson مع تمرير «القائمة» (list). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:236]

```
237:             prefs.edit().putString(STORE_KEY, json).apply()
```
> تُستدعى الدالّة edit على الكائن prefs ثم الدالّة putString مع تمرير المفتاح STORE_KEY والمتغيّر json ثم الدالّة apply. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:237]

```
238:         } catch (_: Exception) {}
```
> إغلاق نطاق ثم فقرة التقاط (catch) لاستثناء من النوع Exception باسم مُهمَل (_) وجسمها فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:238]

```
239:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:239]

```
240: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:240]

```
241:     private fun persistNames(map: Map<String, String>) {
```
> تُعرَّف دالّة خاصّة (private) اسمها persistNames تأخذ معاملاً «الخريطة» (map) من النوع Map مفاتيحه String وقيمه String. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:241]

```
242:         try {
```
> بدء فقرة المحاولة (try). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:242]

```
243:             val json = gson.toJson(map)
```
> يُعرَّف متغيّر ثابت اسمه json ويُسنَد إليه ناتج استدعاء الدالّة toJson من الكائن gson مع تمرير «الخريطة» (map). [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:243]

```
244:             prefs.edit().putString(NAMES_STORE_KEY, json).apply()
```
> تُستدعى الدالّة edit على الكائن prefs ثم الدالّة putString مع تمرير المفتاح NAMES_STORE_KEY والمتغيّر json ثم الدالّة apply. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:244]

```
245:         } catch (_: Exception) {}
```
> إغلاق نطاق ثم فقرة التقاط (catch) لاستثناء من النوع Exception باسم مُهمَل (_) وجسمها فارغ. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:245]

```
246:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:246]

```
247: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/GeohashBookmarksStore.kt:247]
