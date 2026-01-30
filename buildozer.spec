[app]
title = The Guard - Node 7
package.name = theguard
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# المكتبات المطلوبة للسيادة
requirements = python3,kivy==2.3.0,pyjnius,android,requests,hostpython3

version = 1.1.9

# صلاحيات الدرع
android.permissions = 
INTERNET, FOREGROUND_SERVICE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True

# ربط الخدمة الخلفية
android.services = monitor:service.py

# إعدادات الاستقرار
android.copy_libs = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
