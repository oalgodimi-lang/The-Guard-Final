[app]
title = The Guard
package.name = theguard
package.domain = org.theguard
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.7

# [الصلاحيات السيادية]
android.permissions = INTERNET, ACCESS_NETWORK_STATE, BIND_VPN_SERVICE, FOREGROUND_SERVICE

specification = 
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False

# [تعريف خدمة الخلفية]
android.services = monitor:service.py

# المستلزمات البرمجية
requirements = python3,kivy,pyjnius,android

[buildozer]
log_level = 2
warn_on_root = 1
