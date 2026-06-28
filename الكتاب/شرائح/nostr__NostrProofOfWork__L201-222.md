# شريحة — app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt (الأسطر 201–222)

```
201:         return if (difficulty <= 0) 1L else 1L shl difficulty
```
> يُعيد القيمة: إذا كانت الصعوبة (difficulty) أصغر من أو تساوي صفر يُعيد العدد الطويل ‏1L، وإلا يُعيد العدد الطويل ‏1L مُزاحاً لليسار (shl) بمقدار قيمة الصعوبة. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:201]

```
202:     }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:202]

```
203:     
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:203]

```
204:     /**
```
> تعليق: بداية كتلة توثيق (تعليق وثائقي بأسلوب KDoc). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:204]

```
205:      * Get a human-readable description of the estimated mining time
```
> تعليق: «احصل على وصف مقروء للبشر لزمن التعدين المُقدَّر». [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:205]

```
206:      * @param difficulty The target difficulty
```
> تعليق: «‎@param difficulty الصعوبة المستهدفة». [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:206]

```
207:      * @param hashesPerSecond Estimated hashes per second (default: 100,000)
```
> تعليق: «‎@param hashesPerSecond عدد التجزئات (hashes) المُقدَّر في الثانية (الافتراضي: 100,000)». [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:207]

```
208:      * @return Human-readable time estimate
```
> تعليق: «‎@return تقدير زمني مقروء للبشر». [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:208]

```
209:      */
```
> تعليق: نهاية كتلة التوثيق. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:209]

```
210:     fun estimateMiningTime(difficulty: Int, hashesPerSecond: Int = 100_000): String {
```
> تُعرَّف دالة (fun) باسم «تقدير زمن التعدين» (estimateMiningTime) تأخذ مُعامل الصعوبة (difficulty) من نوع صحيح (Int) ومُعامل عدد التجزئات في الثانية (hashesPerSecond) من نوع صحيح (Int) بقيمة افتراضية ‏100_000، وتُعيد نصاً (String). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:210]

```
211:         val estimatedHashes = estimateWork(difficulty)
```
> يُعرَّف متغيّر ثابت (val) باسم «التجزئات المُقدَّرة» (estimatedHashes) ويُسنَد إليه ناتج استدعاء الدالة «تقدير العمل» (estimateWork) مع تمرير الصعوبة (difficulty). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:211]

```
212:         val estimatedSeconds = estimatedHashes / hashesPerSecond
```
> يُعرَّف متغيّر ثابت (val) باسم «الثواني المُقدَّرة» (estimatedSeconds) ويُسنَد إليه ناتج قسمة التجزئات المُقدَّرة (estimatedHashes) على عدد التجزئات في الثانية (hashesPerSecond). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:212]

```
213:         
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:213]

```
214:         return when {
```
> يُعيد ناتج تعبير شرطي من نوع when (بلا وسيط) تبدأ كتلته هنا. [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:214]

```
215:             estimatedSeconds < 1 -> "< 1 second"
```
> فرع: إذا كانت الثواني المُقدَّرة (estimatedSeconds) أصغر من ‏1 فالقيمة هي النص «‎< 1 second». [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:215]

```
216:             estimatedSeconds < 60 -> "${estimatedSeconds}s"
```
> فرع: إذا كانت الثواني المُقدَّرة أصغر من ‏60 فالقيمة هي نص يحوي قيمة الثواني المُقدَّرة متبوعةً بالحرف «s». [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:216]

```
217:             estimatedSeconds < 3600 -> "${estimatedSeconds / 60}m ${estimatedSeconds % 60}s"
```
> فرع: إذا كانت الثواني المُقدَّرة أصغر من ‏3600 فالقيمة هي نص يحوي حاصل قسمة الثواني المُقدَّرة على ‏60 متبوعاً بالحرف «m» ثم مسافة ثم باقي قسمة الثواني المُقدَّرة على ‏60 متبوعاً بالحرف «s». [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:217]

```
218:             estimatedSeconds < 86400 -> "${estimatedSeconds / 3600}h ${(estimatedSeconds % 3600) / 60}m"
```
> فرع: إذا كانت الثواني المُقدَّرة أصغر من ‏86400 فالقيمة هي نص يحوي حاصل قسمة الثواني المُقدَّرة على ‏3600 متبوعاً بالحرف «h» ثم مسافة ثم حاصل قسمة (باقي قسمة الثواني المُقدَّرة على ‏3600) على ‏60 متبوعاً بالحرف «m». [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:218]

```
219:             else -> "${estimatedSeconds / 86400}d ${(estimatedSeconds % 86400) / 3600}h"
```
> فرع وإلا (else): القيمة هي نص يحوي حاصل قسمة الثواني المُقدَّرة على ‏86400 متبوعاً بالحرف «d» ثم مسافة ثم حاصل قسمة (باقي قسمة الثواني المُقدَّرة على ‏86400) على ‏3600 متبوعاً بالحرف «h». [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:219]

```
220:         }
```
> إغلاق نطاق (نهاية كتلة when). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:220]

```
221:     }
```
> إغلاق نطاق (نهاية الدالة estimateMiningTime). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:221]

```
222: }
```
> إغلاق نطاق (نهاية الكائن/الصنف الحاوي). [app/src/main/java/com/bitchat/android/nostr/NostrProofOfWork.kt:222]
