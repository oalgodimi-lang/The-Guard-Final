[app]
title = The Guard - Node 7
package.name = theguard_n7
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.3.1

# المكتبات المطلوبة للرادار الحقيقي والشبكة
requirements = python3, kivy==2.3.0, hostpython3, pyjnius

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0
fullscreen = 0

# الصلاحيات السيادية (أساس العمل)
# تم إضافة PACKAGE_USAGE_STATS و READ_PHONE_STATE
android.permissions = INTERNET, ACCESS_NETWORK_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, PACKAGE_USAGE_STATS, READ_PHONE_STATE

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# تفعيل AndroidX لضمان عمل مكتبات أندرويد الحديثة
android.enable_androidx = True

# تفعيل الوصول للملفات في أندرويد 11 وما فوق
android.manifest.application_arguments = --manage-external-storage

# حقن كود الـ Manifest السحري لتجاوز صدام أندرويد 13
# هذا الجزء يعلن رسمياً أن التطبيق أداة أمنية وإحصائية
android.extra_manifest_xml = """
<manifest xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools">
    <uses-permission android:name="android.permission.PACKAGE_USAGE_STATS" tools:ignore="ProtectedPermissions" />
    <application>
        <meta-data android:name="android.app.usage.USAGE_STATS" android:value="true" />
        <meta-data android:name="android.app.product_category" android:value="productivity" />
    </application>
</manifest>
"""
