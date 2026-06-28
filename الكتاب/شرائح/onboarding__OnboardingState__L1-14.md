# شريحة — app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt (الأسطر 1–14)

```
1: package com.bitchat.android.onboarding
```
> يُعلَن انتماء الملف إلى الحُزمة (package) باسم `com.bitchat.android.onboarding`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:1]

```
2: 
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:2]

```
3: enum class OnboardingState {
```
> يُعرَّف صنف تعداد (enum class) باسم `OnboardingState` (حالة التهيئة الأولى)، ويُفتَح نطاقه. [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:3]

```
4:     CHECKING,
```
> يُعرَّف ثابت التعداد (enum constant) باسم `CHECKING` (الفحص). [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:4]

```
5:     BLUETOOTH_CHECK,
```
> يُعرَّف ثابت التعداد باسم `BLUETOOTH_CHECK` (فحص البلوتوث). [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:5]

```
6:     LOCATION_CHECK,
```
> يُعرَّف ثابت التعداد باسم `LOCATION_CHECK` (فحص الموقع). [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:6]

```
7:     BATTERY_OPTIMIZATION_CHECK,
```
> يُعرَّف ثابت التعداد باسم `BATTERY_OPTIMIZATION_CHECK` (فحص تحسين البطارية). [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:7]

```
8:     PERMISSION_EXPLANATION,
```
> يُعرَّف ثابت التعداد باسم `PERMISSION_EXPLANATION` (شرح الإذن). [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:8]

```
9:     BACKGROUND_LOCATION_EXPLANATION,
```
> يُعرَّف ثابت التعداد باسم `BACKGROUND_LOCATION_EXPLANATION` (شرح الموقع في الخلفية). [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:9]

```
10:     PERMISSION_REQUESTING,
```
> يُعرَّف ثابت التعداد باسم `PERMISSION_REQUESTING` (طلب الإذن). [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:10]

```
11:     INITIALIZING,
```
> يُعرَّف ثابت التعداد باسم `INITIALIZING` (التهيئة الجارية). [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:11]

```
12:     COMPLETE,
```
> يُعرَّف ثابت التعداد باسم `COMPLETE` (مكتمل). [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:12]

```
13:     ERROR
```
> يُعرَّف ثابت التعداد باسم `ERROR` (خطأ)، وهو الأخير دون فاصلة لاحقة. [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:13]

```
14: }
```
> إغلاق نطاق صنف التعداد `OnboardingState`. [app/src/main/java/com/bitchat/android/onboarding/OnboardingState.kt:14]
