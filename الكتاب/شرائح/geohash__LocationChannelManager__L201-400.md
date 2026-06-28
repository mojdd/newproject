# شريحة — app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt (الأسطر 201–400)

```
201:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:201]

```
202: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:202]

```
203:     /**
```
> بداية تعليق توثيقي (KDoc). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:203]

```
204:      * Stop periodic refreshes when selector UI is dismissed
```
> تعليق: أوقِف التحديثات الدورية عند إغلاق واجهة المُحدِّد. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:204]

```
205:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:205]

```
206:     fun endLiveRefresh() {
```
> تعريف دالة إنهاء التحديث الحي (endLiveRefresh) عمومية بلا معاملات وبلا قيمة إرجاع. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:206]

```
207:         Log.d(TAG, "Ending live refresh")
```
> استدعاء تسجيل تصحيح (Log.d) بوسم TAG ونص "Ending live refresh". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:207]

```
208:         locationProvider.removeLocationUpdates(locationUpdateCallback)
```
> استدعاء إزالة تحديثات الموقع (removeLocationUpdates) من مزوّد الموقع (locationProvider) ممرِّراً ردّ نداء تحديث الموقع (locationUpdateCallback). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:208]

```
209:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:209]

```
210: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:210]

```
211:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:211]

```
212:      * Select a channel
```
> تعليق: اختَر قناة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:212]

```
213:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:213]

```
214:     fun select(channel: ChannelID) {
```
> تعريف دالة الاختيار (select) عمومية تأخذ معامِلاً اسمه channel من نوع معرّف القناة (ChannelID). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:214]

```
215:         Log.d(TAG, "Selected channel: ${channel.displayName}")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "Selected channel: " متبوعاً بقيمة الاسم المعروض (displayName) للقناة channel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:215]

```
216:         // Use synchronous set to avoid race with background recomputation
```
> تعليق: استعمل ضبطاً متزامناً لتجنّب التسابق مع إعادة الحساب في الخلفية. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:216]

```
217:         _selectedChannel.value = channel
```
> إسناد القناة channel إلى قيمة (value) الحقل القناة المختارة (_selectedChannel). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:217]

```
218:         saveChannelSelection(channel)
```
> استدعاء دالة حفظ اختيار القناة (saveChannelSelection) ممرِّراً channel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:218]

```
219: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:219]

```
220:         // Immediately recompute teleported status against the latest known location
```
> تعليق: أعِد فوراً حساب حالة الانتقال (teleported) مقابل آخر موقع معروف. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:220]

```
221:         lastLocation?.let { location ->
```
> استدعاء دالة let على آخر موقع (lastLocation) إن لم يكن فارغاً، بمعامِل lambda اسمه location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:221]

```
222:             when (channel) {
```
> بداية تعبير when على القناة channel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:222]

```
223:                 is ChannelID.Mesh -> {
```
> فرع when: إذا كان channel من نوع شبكة المِش (ChannelID.Mesh). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:223]

```
224:                     _teleported.value = false
```
> إسناد القيمة false إلى قيمة حقل الانتقال (_teleported). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:224]

```
225:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:225]

```
226:                 is ChannelID.Location -> {
```
> فرع when: إذا كان channel من نوع قناة الموقع (ChannelID.Location). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:226]

```
227:                     val currentGeohash = Geohash.encode(
```
> تعريف متغيّر ثابت اسمه التجزئة الجغرافية الحالية (currentGeohash) ناتجاً من استدعاء دالة الترميز (Geohash.encode). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:227]

```
228:                         latitude = location.latitude,
```
> تمرير معامِل خط العرض (latitude) بقيمة خط عرض الموقع location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:228]

```
229:                         longitude = location.longitude,
```
> تمرير معامِل خط الطول (longitude) بقيمة خط طول الموقع location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:229]

```
230:                         precision = channel.channel.level.precision
```
> تمرير معامِل الدقّة (precision) بقيمة دقّة مستوى قناة channel (channel.channel.level.precision). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:230]

```
231:                     )
```
> إغلاق قائمة معامِلات استدعاء الترميز. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:231]

```
232:                     val isTeleportedNow = currentGeohash != channel.channel.geohash
```
> تعريف متغيّر ثابت اسمه هل انتقل الآن (isTeleportedNow) بقيمة نتيجة عدم تساوي currentGeohash مع تجزئة قناة channel (channel.channel.geohash). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:232]

```
233:                     _teleported.value = isTeleportedNow
```
> إسناد isTeleportedNow إلى قيمة حقل الانتقال (_teleported). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:233]

```
234:                     Log.d(TAG, "Teleported (immediate recompute): $isTeleportedNow (current: $currentGeohash, selected: ${channel.channel.geohash})")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص يتضمّن قيمة isTeleportedNow وقيمة currentGeohash وقيمة تجزئة قناة channel. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:234]

```
235:                 }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:235]

```
236:             }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:236]

```
237:         }
```
> إغلاق نطاق lambda الخاص بـ let. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:237]

```
238:     }
```
> إغلاق نطاق الدالة select. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:238]

```
239:     
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:239]

```
240:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:240]

```
241:      * Set teleported status (for manual geohash teleportation)
```
> تعليق: اضبط حالة الانتقال (من أجل الانتقال اليدوي للتجزئة الجغرافية). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:241]

```
242:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:242]

```
243:     fun setTeleported(teleported: Boolean) {
```
> تعريف دالة ضبط الانتقال (setTeleported) عمومية تأخذ معامِلاً منطقياً (Boolean) اسمه teleported. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:243]

```
244:         Log.d(TAG, "Setting teleported status: $teleported")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "Setting teleported status: " متبوعاً بقيمة teleported. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:244]

```
245:         _teleported.value = teleported
```
> إسناد teleported إلى قيمة حقل الانتقال (_teleported). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:245]

```
246:     }
```
> إغلاق نطاق الدالة setTeleported. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:246]

```
247: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:247]

```
248:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:248]

```
249:      * Enable location services (user-controlled toggle)
```
> تعليق: فعِّل خدمات الموقع (مفتاح يتحكّم به المستخدم). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:249]

```
250:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:250]

```
251:     fun enableLocationServices() {
```
> تعريف دالة تفعيل خدمات الموقع (enableLocationServices) عمومية بلا معاملات وبلا قيمة إرجاع. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:251]

```
252:         Log.d(TAG, "enableLocationServices() called by user")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "enableLocationServices() called by user". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:252]

```
253:         _locationServicesEnabled.value = true
```
> إسناد القيمة true إلى قيمة حقل تفعيل خدمات الموقع (_locationServicesEnabled). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:253]

```
254:         saveLocationServicesState(true)
```
> استدعاء دالة حفظ حالة خدمات الموقع (saveLocationServicesState) ممرِّراً true. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:254]

```
255:         
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:255]

```
256:         // If we have permission and system location is on, start location operations
```
> تعليق: إن كان لدينا إذن ونظام الموقع مُشغَّل، ابدأ عمليات الموقع. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:256]

```
257:         if (_permissionState.value == PermissionState.AUTHORIZED && systemLocationEnabled.value) {
```
> شرط if: إذا كانت قيمة حقل حالة الإذن (_permissionState) تساوي مُصرَّح (PermissionState.AUTHORIZED) وقيمة تفعيل موقع النظام (systemLocationEnabled) صحيحة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:257]

```
258:             requestOneShotLocation()
```
> استدعاء دالة طلب موقع لمرّة واحدة (requestOneShotLocation). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:258]

```
259:         }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:259]

```
260:     }
```
> إغلاق نطاق الدالة enableLocationServices. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:260]

```
261: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:261]

```
262:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:262]

```
263:      * Disable location services (user-controlled toggle)
```
> تعليق: عطِّل خدمات الموقع (مفتاح يتحكّم به المستخدم). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:263]

```
264:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:264]

```
265:     fun disableLocationServices() {
```
> تعريف دالة تعطيل خدمات الموقع (disableLocationServices) عمومية بلا معاملات وبلا قيمة إرجاع. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:265]

```
266:         Log.d(TAG, "disableLocationServices() called by user")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "disableLocationServices() called by user". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:266]

```
267:         _locationServicesEnabled.value = false
```
> إسناد القيمة false إلى قيمة حقل تفعيل خدمات الموقع (_locationServicesEnabled). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:267]

```
268:         saveLocationServicesState(false)
```
> استدعاء دالة حفظ حالة خدمات الموقع (saveLocationServicesState) ممرِّراً false. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:268]

```
269:         
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:269]

```
270:         // Stop any ongoing location operations
```
> تعليق: أوقِف أيّ عمليات موقع جارية. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:270]

```
271:         endLiveRefresh()
```
> استدعاء دالة إنهاء التحديث الحي (endLiveRefresh). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:271]

```
272:         
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:272]

```
273:         // Clear available channels when location is disabled
```
> تعليق: امسح القنوات المتاحة عند تعطيل الموقع. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:273]

```
274:         _availableChannels.value = emptyList()
```
> إسناد قائمة فارغة (emptyList) إلى قيمة حقل القنوات المتاحة (_availableChannels). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:274]

```
275:         _locationNames.value = emptyMap()
```
> إسناد خريطة فارغة (emptyMap) إلى قيمة حقل أسماء المواقع (_locationNames). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:275]

```
276:         
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:276]

```
277:         // If user had a location channel selected, switch back to mesh
```
> تعليق: إن كان المستخدم قد اختار قناة موقع، فارجِع إلى شبكة المِش. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:277]

```
278:         if (_selectedChannel.value is ChannelID.Location) {
```
> شرط if: إذا كانت قيمة حقل القناة المختارة (_selectedChannel) من نوع قناة الموقع (ChannelID.Location). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:278]

```
279:             select(ChannelID.Mesh)
```
> استدعاء دالة الاختيار (select) ممرِّراً شبكة المِش (ChannelID.Mesh). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:279]

```
280:         }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:280]

```
281:     }
```
> إغلاق نطاق الدالة disableLocationServices. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:281]

```
282: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:282]

```
283:     /**
```
> بداية تعليق توثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:283]

```
284:      * Check if location services are enabled by the user
```
> تعليق: تحقّق إن كانت خدمات الموقع مفعَّلة من قِبَل المستخدم. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:284]

```
285:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:285]

```
286:     /**
```
> بداية تعليق توثيقي ثانٍ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:286]

```
287:      * Check if both the app toggle and system location are enabled
```
> تعليق: تحقّق إن كان كل من مفتاح التطبيق وموقع النظام مفعَّلَين. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:287]

```
288:      */
```
> نهاية التعليق التوثيقي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:288]

```
289:     fun isLocationServicesEnabled(): Boolean {
```
> تعريف دالة هل خدمات الموقع مفعَّلة (isLocationServicesEnabled) عمومية تُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:289]

```
290:         return _locationServicesEnabled.value && _systemLocationEnabled.value
```
> إعادة نتيجة العملية المنطقية (و) بين قيمة حقل تفعيل خدمات الموقع (_locationServicesEnabled) وقيمة حقل تفعيل موقع النظام (_systemLocationEnabled). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:290]

```
291:     }
```
> إغلاق نطاق الدالة isLocationServicesEnabled. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:291]

```
292: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:292]

```
293:     // MARK: - Location Operations
```
> تعليق: علامة قسم — عمليات الموقع (Location Operations). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:293]

```
294: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:294]

```
295:     private fun requestOneShotLocation() {
```
> تعريف دالة طلب موقع لمرّة واحدة (requestOneShotLocation) خاصّة (private) بلا معاملات وبلا قيمة إرجاع. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:295]

```
296:         if (!checkAndSyncPermission()) {
```
> شرط if: إذا كانت نتيجة دالة فحص ومزامنة الإذن (checkAndSyncPermission) غير صحيحة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:296]

```
297:             Log.w(TAG, "No location permission for one-shot request")
```
> استدعاء تسجيل تحذير (Log.w) بوسم TAG ونص "No location permission for one-shot request". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:297]

```
298:             return
```
> عبارة إرجاع (return) تُنهي الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:298]

```
299:         }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:299]

```
300: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:300]

```
301:         Log.d(TAG, "Requesting one-shot location")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "Requesting one-shot location". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:301]

```
302:         // Set loading state initially
```
> تعليق: اضبط حالة التحميل ابتداءً. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:302]

```
303:         _isLoadingLocation.value = true
```
> إسناد القيمة true إلى قيمة حقل جارٍ تحميل الموقع (_isLoadingLocation). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:303]

```
304:         
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:304]

```
305:         locationProvider.getLastKnownLocation { cached ->
```
> استدعاء دالة جلب آخر موقع معروف (getLastKnownLocation) من مزوّد الموقع (locationProvider) بردّ نداء lambda معامِله اسمه المخزّن مؤقتاً (cached). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:305]

```
306:             // If we have a cached location and it's reasonably recent (e.g. < 5 mins), use it
```
> تعليق: إن كان لدينا موقع مخزّن مؤقتاً وهو حديث بشكل معقول (مثلاً أقل من ٥ دقائق)، فاستعمله. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:306]

```
307:             // For now, we just use it if it exists, similar to previous logic
```
> تعليق: في الوقت الحالي نستعمله فقط إن كان موجوداً، شبيهاً بالمنطق السابق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:307]

```
308:             if (cached != null) {
```
> شرط if: إذا كان المخزّن مؤقتاً (cached) غير فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:308]

```
309:                 Log.d(TAG, "Using last known location: ${cached.latitude}, ${cached.longitude}")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "Using last known location: " متبوعاً بخط عرض وخط طول cached. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:309]

```
310:                 onLocationUpdated(cached)
```
> استدعاء دالة عند تحديث الموقع (onLocationUpdated) ممرِّراً cached. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:310]

```
311:             } else {
```
> فرع else للشرط السابق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:311]

```
312:                 Log.d(TAG, "No last known location available, requesting fresh...")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "No last known location available, requesting fresh...". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:312]

```
313:                 locationProvider.requestFreshLocation { fresh ->
```
> استدعاء دالة طلب موقع جديد (requestFreshLocation) من مزوّد الموقع بردّ نداء lambda معامِله اسمه الجديد (fresh). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:313]

```
314:                     if (fresh != null) {
```
> شرط if: إذا كان الموقع الجديد (fresh) غير فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:314]

```
315:                         Log.d(TAG, "Fresh location received: ${fresh.latitude}, ${fresh.longitude}")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "Fresh location received: " متبوعاً بخط عرض وخط طول fresh. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:315]

```
316:                         onLocationUpdated(fresh)
```
> استدعاء دالة عند تحديث الموقع (onLocationUpdated) ممرِّراً fresh. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:316]

```
317:                     } else {
```
> فرع else للشرط السابق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:317]

```
318:                         Log.w(TAG, "Failed to get fresh location")
```
> استدعاء تسجيل تحذير بوسم TAG ونص "Failed to get fresh location". [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:318]

```
319:                         _isLoadingLocation.value = false
```
> إسناد القيمة false إلى قيمة حقل جارٍ تحميل الموقع (_isLoadingLocation). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:319]

```
320:                     }
```
> إغلاق نطاق فرع else. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:320]

```
321:                 }
```
> إغلاق نطاق lambda الخاص بـ requestFreshLocation. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:321]

```
322:             }
```
> إغلاق نطاق فرع else الأعلى. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:322]

```
323:         }
```
> إغلاق نطاق lambda الخاص بـ getLastKnownLocation. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:323]

```
324:     }
```
> إغلاق نطاق الدالة requestOneShotLocation. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:324]

```
325: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:325]

```
326:     private fun onLocationUpdated(location: Location) {
```
> تعريف دالة عند تحديث الموقع (onLocationUpdated) خاصّة تأخذ معامِلاً اسمه location من نوع موقع (Location). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:326]

```
327:         lastLocation = location
```
> إسناد location إلى المتغيّر آخر موقع (lastLocation). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:327]

```
328:         _isLoadingLocation.value = false
```
> إسناد القيمة false إلى قيمة حقل جارٍ تحميل الموقع (_isLoadingLocation). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:328]

```
329:         computeChannels(location)
```
> استدعاء دالة حساب القنوات (computeChannels) ممرِّراً location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:329]

```
330:         reverseGeocodeIfNeeded(location)
```
> استدعاء دالة الترميز الجغرافي العكسي عند الحاجة (reverseGeocodeIfNeeded) ممرِّراً location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:330]

```
331:     }
```
> إغلاق نطاق الدالة onLocationUpdated. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:331]

```
332: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:332]

```
333: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:333]

```
334:     // MARK: - Helpers
```
> تعليق: علامة قسم — مساعِدات (Helpers). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:334]

```
335: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:335]

```
336:     private fun getCurrentPermissionStatus(): PermissionState {
```
> تعريف دالة جلب حالة الإذن الحالية (getCurrentPermissionStatus) خاصّة تُعيد حالة إذن (PermissionState). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:336]

```
337:         return if (checkAndSyncPermission()) {
```
> إعادة نتيجة تعبير if: إذا كانت نتيجة دالة فحص ومزامنة الإذن (checkAndSyncPermission) صحيحة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:337]

```
338:             PermissionState.AUTHORIZED
```
> قيمة فرع then: مُصرَّح (PermissionState.AUTHORIZED). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:338]

```
339:         } else {
```
> فرع else للتعبير الشرطي. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:339]

```
340:             PermissionState.DENIED
```
> قيمة فرع else: مرفوض (PermissionState.DENIED). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:340]

```
341:         }
```
> إغلاق نطاق تعبير if/else. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:341]

```
342:     }
```
> إغلاق نطاق الدالة getCurrentPermissionStatus. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:342]

```
343: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:343]

```
344:     private fun checkAndSyncPermission(): Boolean {
```
> تعريف دالة فحص ومزامنة الإذن (checkAndSyncPermission) خاصّة تُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:344]

```
345:         val hasPermission = ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED ||
```
> تعريف متغيّر ثابت اسمه لديه إذن (hasPermission) بقيمة نتيجة مقارنة فحص الإذن الذاتي (checkSelfPermission) لإذن الموقع الدقيق (ACCESS_FINE_LOCATION) بأنه ممنوح (PERMISSION_GRANTED) مع عملية أو منطقية. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:345]

```
346:                ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED
```
> تكملة التعبير: مقارنة فحص الإذن الذاتي لإذن الموقع التقريبي (ACCESS_COARSE_LOCATION) بأنه ممنوح (PERMISSION_GRANTED). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:346]

```
347: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:347]

```
348:         val newState = if (hasPermission) PermissionState.AUTHORIZED else PermissionState.DENIED
```
> تعريف متغيّر ثابت اسمه الحالة الجديدة (newState) بقيمة مُصرَّح (AUTHORIZED) إن كان hasPermission صحيحاً وإلا مرفوض (DENIED). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:348]

```
349: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:349]

```
350:         if (_permissionState.value != newState) {
```
> شرط if: إذا كانت قيمة حقل حالة الإذن (_permissionState) لا تساوي newState. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:350]

```
351:             Log.d(TAG, "Permission state updated to: $newState")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "Permission state updated to: " متبوعاً بقيمة newState. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:351]

```
352:             _permissionState.value = newState
```
> إسناد newState إلى قيمة حقل حالة الإذن (_permissionState). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:352]

```
353:         }
```
> إغلاق نطاق شرط if. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:353]

```
354: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:354]

```
355:         return hasPermission
```
> إعادة قيمة المتغيّر hasPermission. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:355]

```
356:     }
```
> إغلاق نطاق الدالة checkAndSyncPermission. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:356]

```
357: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:357]

```
358:     private fun computeChannels(location: Location) {
```
> تعريف دالة حساب القنوات (computeChannels) خاصّة تأخذ معامِلاً اسمه location من نوع موقع (Location). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:358]

```
359:         Log.d(TAG, "Computing channels for location: ${location.latitude}, ${location.longitude}")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "Computing channels for location: " متبوعاً بخط عرض وخط طول location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:359]

```
360:         
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:360]

```
361:         val levels = GeohashChannelLevel.allCases()
```
> تعريف متغيّر ثابت اسمه المستويات (levels) بقيمة نتيجة استدعاء دالة كل الحالات (allCases) لمستوى قناة التجزئة الجغرافية (GeohashChannelLevel). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:361]

```
362:         val result = mutableListOf<GeohashChannel>()
```
> تعريف متغيّر ثابت اسمه النتيجة (result) بقيمة قائمة قابلة للتعديل (mutableListOf) من نوع قناة التجزئة الجغرافية (GeohashChannel). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:362]

```
363:         
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:363]

```
364:         for (level in levels) {
```
> حلقة for تكرّر على عناصر المستويات (levels) بمتغيّر اسمه المستوى (level). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:364]

```
365:             val geohash = Geohash.encode(
```
> تعريف متغيّر ثابت اسمه التجزئة الجغرافية (geohash) بقيمة نتيجة استدعاء دالة الترميز (Geohash.encode). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:365]

```
366:                 latitude = location.latitude,
```
> تمرير معامِل خط العرض (latitude) بقيمة خط عرض location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:366]

```
367:                 longitude = location.longitude,
```
> تمرير معامِل خط الطول (longitude) بقيمة خط طول location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:367]

```
368:                 precision = level.precision
```
> تمرير معامِل الدقّة (precision) بقيمة دقّة المستوى (level.precision). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:368]

```
369:             )
```
> إغلاق قائمة معامِلات استدعاء الترميز. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:369]

```
370:             result.add(GeohashChannel(level = level, geohash = geohash))
```
> استدعاء إضافة (add) إلى result لكائن قناة تجزئة جغرافية (GeohashChannel) بمعامِل المستوى level ومعامِل التجزئة geohash. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:370]

```
371:             
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:371]

```
372:             Log.v(TAG, "Generated ${level.displayName}: $geohash")
```
> استدعاء تسجيل مطوَّل (Log.v) بوسم TAG ونص "Generated " متبوعاً بالاسم المعروض للمستوى (level.displayName) ثم قيمة geohash. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:372]

```
373:         }
```
> إغلاق نطاق حلقة for. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:373]

```
374:         
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:374]

```
375:         _availableChannels.value = result
```
> إسناد result إلى قيمة حقل القنوات المتاحة (_availableChannels). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:375]

```
376:         
```
> سطر فارغ (يحتوي مسافات بيضاء). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:376]

```
377:         // Recompute teleported status based on current location vs selected channel
```
> تعليق: أعِد حساب حالة الانتقال بناءً على الموقع الحالي مقابل القناة المختارة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:377]

```
378:         val selectedChannelValue = _selectedChannel.value
```
> تعريف متغيّر ثابت اسمه قيمة القناة المختارة (selectedChannelValue) بقيمة قيمة حقل القناة المختارة (_selectedChannel). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:378]

```
379:         when (selectedChannelValue) {
```
> بداية تعبير when على selectedChannelValue. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:379]

```
380:             is ChannelID.Mesh -> {
```
> فرع when: إذا كانت selectedChannelValue من نوع شبكة المِش (ChannelID.Mesh). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:380]

```
381:                 _teleported.value = false
```
> إسناد القيمة false إلى قيمة حقل الانتقال (_teleported). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:381]

```
382:             }
```
> إغلاق نطاق فرع Mesh. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:382]

```
383:             is ChannelID.Location -> {
```
> فرع when: إذا كانت selectedChannelValue من نوع قناة الموقع (ChannelID.Location). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:383]

```
384:                 val currentGeohash = Geohash.encode(
```
> تعريف متغيّر ثابت اسمه التجزئة الجغرافية الحالية (currentGeohash) بقيمة نتيجة استدعاء دالة الترميز (Geohash.encode). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:384]

```
385:                     latitude = location.latitude,
```
> تمرير معامِل خط العرض (latitude) بقيمة خط عرض location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:385]

```
386:                     longitude = location.longitude,
```
> تمرير معامِل خط الطول (longitude) بقيمة خط طول location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:386]

```
387:                     precision = selectedChannelValue.channel.level.precision
```
> تمرير معامِل الدقّة (precision) بقيمة دقّة مستوى قناة selectedChannelValue (selectedChannelValue.channel.level.precision). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:387]

```
388:                 )
```
> إغلاق قائمة معامِلات استدعاء الترميز. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:388]

```
389:                 val isTeleported = currentGeohash != selectedChannelValue.channel.geohash
```
> تعريف متغيّر ثابت اسمه هل انتقل (isTeleported) بقيمة نتيجة عدم تساوي currentGeohash مع تجزئة قناة selectedChannelValue (selectedChannelValue.channel.geohash). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:389]

```
390:                 _teleported.value = isTeleported
```
> إسناد isTeleported إلى قيمة حقل الانتقال (_teleported). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:390]

```
391:                 Log.d(TAG, "Teleported status: $isTeleported (current: $currentGeohash, selected: ${selectedChannelValue.channel.geohash})")
```
> استدعاء تسجيل تصحيح بوسم TAG ونص "Teleported status: " متبوعاً بقيمة isTeleported وقيمة currentGeohash وقيمة تجزئة قناة selectedChannelValue. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:391]

```
392:             }
```
> إغلاق نطاق فرع Location. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:392]

```
393:         }
```
> إغلاق نطاق تعبير when. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:393]

```
394:     }
```
> إغلاق نطاق الدالة computeChannels. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:394]

```
395: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:395]

```
396:     private fun reverseGeocodeIfNeeded(location: Location) {
```
> تعريف دالة الترميز الجغرافي العكسي عند الحاجة (reverseGeocodeIfNeeded) خاصّة تأخذ معامِلاً اسمه location من نوع موقع (Location). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:396]

```
397:         // Cancel any pending geocoding job to avoid race conditions
```
> تعليق: ألغِ أيّ مهمّة ترميز جغرافي معلَّقة لتجنّب حالات التسابق. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:397]

```
398:         geocodingJob?.cancel()
```
> استدعاء دالة الإلغاء (cancel) على مهمّة الترميز الجغرافي (geocodingJob) إن لم تكن فارغة. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:398]

```
399: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:399]

```
400:         geocodingJob = scope.launch(Dispatchers.IO) {
```
> إسناد إلى مهمّة الترميز الجغرافي (geocodingJob) نتيجة إطلاق كوروتين (launch) على النطاق (scope) بمرسِل الإدخال/الإخراج (Dispatchers.IO). [app/src/main/java/com/bitchat/android/geohash/LocationChannelManager.kt:400]
