[app]
title = The Guard - Node 7
package.name = guard_node7
package.domain = org.sovereign.freedom
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# الصلاحيات السيادية للتحكم الكامل
android.permissions = INTERNET, ACCESS_NETWORK_STATE, BIND_VPN_SERVICE, FOREGROUND_SERVICE, ACCESS_WIFI_STATE

# تشغيل الحارس في الخفاء
android.services = monitor:service.py

requirements = python3,kivy,android,pyjnius

orientation = portrait
android.archs = arm64-v8a, armeabi-v7a
android.api = 31
[buildozer]
log_level = 2
