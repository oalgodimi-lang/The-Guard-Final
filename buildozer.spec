[app]
title = The Guard - Node 7
package.name = theguard_n7
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.3.2

# المتطلبات الأساسية مع إضافة جسر التواصل مع أندرويد
requirements = python3, kivy==2.3.0, hostpython3, pyjnius

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0
fullscreen = 0

# الصلاحيات السيادية (تم اختصارها لضمان القبول)
android.permissions = INTERNET, ACCESS_NETWORK_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, PACKAGE_USAGE_STATS, READ_PHONE_STATE

# إعدادات النظام المستهدفة (أندرويد 13)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# تفعيل التقنيات الحديثة لفك الارتباط مع الأنظمة القديمة
android.enable_androidx = True

# حقن كود الـ Manifest السحري (نسخة السطر الواحد لتجنب أخطاء التنسيق)
android.extra_manifest_xml = "<uses-permission android:name='android.permission.PACKAGE_USAGE_STATS' tools:ignore='ProtectedPermissions' />"

# السماح بإدارة الملفات في الإصدارات الحديثة
android.manifest.application_arguments = --manage-external-storage
