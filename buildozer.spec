[app]
title = The Guard - Node 7
package.name = guard_node7
package.domain = org.sovereign.freedom
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1.2

# الصلاحيات السيادية للتحكم الكامل وتفعيل الدرع
android.permissions =  INTERNET, ACCESS_NETWORK_STATE, BIND_VPN_SERVICE, FOREGROUND_SERVICE, POST_NOTIFICATIONS

# تشغيل الحارس في الخفاء (الدرع الخلفي)
android.services = monitor:service.py

# المتطلبات البرمجية الأساسية
requirements = python3, kivy, android, pyjnius, 

orientation = portrait
android.archs = arm64-v8a, armeabi-v7a

# تغيير الـ API لضمان التوافق مع المصنع وتجاوز أخطاء البناء
android.api = 30
android.minapi = 21
android.sdk = 30

[buildozer]
log_level = 2
