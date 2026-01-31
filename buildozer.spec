[app]
title = The Guard - Node 7
package.name = theguard_n7
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.2.0

# المكتبات المطلوبة للرادار الحقيقي والشبكة
requirements = python3,kivy==2.3.0,pyjnius,android,requests

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

# الصلاحيات السيادية (أساس العمل)
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# تفعيل الوصول للملفات في أندرويد 11+
android.manifest.application_arguments = --manage-external-storage
