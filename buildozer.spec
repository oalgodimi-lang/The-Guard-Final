[app]
title = Sovereign Shield
package.name = sovereignshield
package.domain = com.sovereignshield
source.dir = .
version = 1.2.0

# تقليص المعماريات لتوفير الذاكرة (أهم خطوة للمحاولة 122)
android.archs = arm64-v8a

# الصلاحيات المطلوبة (الحقن الصامت)
android.permissions = INTERNET,READ_EXTERNAL_STORAGE

# المتطلبات البرمجية
requirements = python3,kivy==2.3.0

# إعدادات الأندرويد
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34

# إعدادات الواجهة
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
