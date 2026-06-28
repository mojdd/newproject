# شريحة — app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt (الأسطر 201–238)

```
201:             
```
> سطر فارغ (يحتوي على مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:201]

```
202:             if (listener != null) {
```
> شرط (if) يفحص أن المستمع (listener) لا يساوي قيمة فارغة (null)، ويفتح كتلته. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:202]

```
203:                 locationManager.removeUpdates(listener)
```
> يستدعي الدالة removeUpdates على مدير الموقع (locationManager) ويمرّر إليها المستمع (listener). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:203]

```
204:                 Log.d(TAG, "Removed location updates")
```
> يستدعي تسجيل تنقيح (Log.d) بالوسم (TAG) والنص "Removed location updates" (أُزيلت تحديثات الموقع). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:204]

```
205:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:205]

```
206:         } catch (e: Exception) {
```
> يغلق كتلة المحاولة (try) ويبدأ كتلة التقاط (catch) تلتقط استثناءً (Exception) باسم e، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:206]

```
207:             Log.e(TAG, "Error removing updates: ${e.message}")
```
> يستدعي تسجيل خطأ (Log.e) بالوسم (TAG) والنص "Error removing updates: " متبوعاً بقيمة الرسالة message للاستثناء e. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:207]

```
208:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:208]

```
209:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:209]

```
210: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:210]

```
211:     override fun cancel() {
```
> يعرّف ويتجاوز (override) دالةً اسمها cancel بلا وسائط، ويفتح جسمها. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:211]

```
212:         try {
```
> يبدأ كتلة محاولة (try) ويفتحها. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:212]

```
213:             // Cancel continuous updates
```
> تعليق: إلغاء التحديثات المستمرة. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:213]

```
214:             synchronized(activeListeners) {
```
> يبدأ كتلة متزامنة (synchronized) على القفل قائمة المستمعين النشطين (activeListeners)، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:214]

```
215:                 for ((_, listener) in activeListeners) {
```
> حلقة تكرار (for) على عناصر قائمة المستمعين النشطين (activeListeners)، متجاهلةً المفتاح (_) ومستخرجةً المستمع (listener)، وتفتح كتلتها. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:215]

```
216:                     try { locationManager.removeUpdates(listener) } catch (_: Exception) {}
```
> كتلة محاولة (try) تستدعي removeUpdates على مدير الموقع (locationManager) بالمستمع (listener)، يليها التقاط (catch) لاستثناء (Exception) متجاهَل الاسم (_) بجسم فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:216]

```
217:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:217]

```
218:                 activeListeners.clear()
```
> يستدعي الدالة clear على قائمة المستمعين النشطين (activeListeners). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:218]

```
219:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:219]

```
220: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:220]

```
221:             // Cancel one-shot requests
```
> تعليق: إلغاء طلبات الطلقة الواحدة (one-shot). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:221]

```
222:             synchronized(activeOneShotListeners) {
```
> يبدأ كتلة متزامنة (synchronized) على القفل قائمة مستمعي الطلقة الواحدة النشطين (activeOneShotListeners)، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:222]

```
223:                 for ((_, listener) in activeOneShotListeners) {
```
> حلقة تكرار (for) على عناصر قائمة مستمعي الطلقة الواحدة النشطين (activeOneShotListeners)، متجاهلةً المفتاح (_) ومستخرجةً المستمع (listener)، وتفتح كتلتها. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:223]

```
224:                     try { locationManager.removeUpdates(listener) } catch (_: Exception) {}
```
> كتلة محاولة (try) تستدعي removeUpdates على مدير الموقع (locationManager) بالمستمع (listener)، يليها التقاط (catch) لاستثناء (Exception) متجاهَل الاسم (_) بجسم فارغ. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:224]

```
225:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:225]

```
226:                 activeOneShotListeners.clear()
```
> يستدعي الدالة clear على قائمة مستمعي الطلقة الواحدة النشطين (activeOneShotListeners). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:226]

```
227:                 
```
> سطر فارغ (يحتوي على مسافات بيضاء فقط). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:227]

```
228:                 for ((_, runnable) in activeOneShotRunnables) {
```
> حلقة تكرار (for) على عناصر قائمة المهام القابلة للتشغيل للطلقة الواحدة النشطة (activeOneShotRunnables)، متجاهلةً المفتاح (_) ومستخرجةً المهمة القابلة للتشغيل (runnable)، وتفتح كتلتها. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:228]

```
229:                     handler.removeCallbacks(runnable)
```
> يستدعي الدالة removeCallbacks على المعالِج (handler) ويمرّر إليها المهمة القابلة للتشغيل (runnable). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:229]

```
230:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:230]

```
231:                 activeOneShotRunnables.clear()
```
> يستدعي الدالة clear على قائمة المهام القابلة للتشغيل للطلقة الواحدة النشطة (activeOneShotRunnables). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:231]

```
232:             }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:232]

```
233:             Log.d(TAG, "Cancelled all system location requests")
```
> يستدعي تسجيل تنقيح (Log.d) بالوسم (TAG) والنص "Cancelled all system location requests" (أُلغيت كل طلبات موقع النظام). [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:233]

```
234:         } catch (e: Exception) {
```
> يغلق كتلة المحاولة (try) ويبدأ كتلة التقاط (catch) تلتقط استثناءً (Exception) باسم e، ويفتح كتلتها. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:234]

```
235:             Log.e(TAG, "Error cancelling system provider: ${e.message}")
```
> يستدعي تسجيل خطأ (Log.e) بالوسم (TAG) والنص "Error cancelling system provider: " متبوعاً بقيمة الرسالة message للاستثناء e. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:235]

```
236:         }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:236]

```
237:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:237]

```
238: }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/SystemLocationProvider.kt:238]
