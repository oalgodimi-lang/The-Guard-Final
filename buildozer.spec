[app]
title = Sovereign Shield
package.name = guard
package.domain = org.node7
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.4.8

# صلاحيات الوصول للوسائط (الحقن الصامت)
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MEDIA_CONTENT_CONTROL

# المكتبات المطلوبة
requirements = python3,kivy==2.1.0,kivymd,pillow

orientation = portrait
fullscreen = 1

# تفتيت البناء: التركيز على معمارية واحدة فقط لتوفير الذاكرة
android.archs = arm64-v8a

android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
