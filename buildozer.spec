[app]
# (section) عنوان التطبيق وهويته
title = The Guard - Node 7
package.name = theguard
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (section) المكتبات المطلوبة للسيادة
# أضفنا pyjnius للوصول إلى إعدادات النظام و android لطلب الأذونات
requirements = python3,kivy==2.3.0,pyjnius,android,requests,hostpython3

version = 1.1.9

# (section) صلاحيات الدرع (المفتاح السيادي)
# السطر التالي هو الأهم لظهور اسم التطبيق في قائمة "الوصول إلى كل الملفات"
android.permissions = INTERNET, FOREGROUND_SERVICE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (section) إعدادات نظام أندرويد (API 33 كما في صورتك)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True

# (section) تعديلات المانيفست الإجبارية (بناءً على نصيحة ديب سيك)
# هذا الجزء يجبر النظام على الاعتراف بالتطبيق كمدير ملفات
android.manifest_extras = <uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE" />
android.manifest_application_extras = android:requestLegacyExternalStorage="true"

# (section) ربط الخدمة الخلفية
android.services = monitor:service.py

# (section) إعدادات الاستقرار والتحميل
android.copy_libs = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
