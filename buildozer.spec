[app]
title = The Guard
package.name = theguard
package.domain = org.freedom
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.4.8

# تقليل المتطلبات للحد الأدنى لتجنب الاختناق
requirements = python3,kivy==2.3.0,requests

orientation = portrait
fullscreen = 0
android.archs = armeabi-v7a

# الصلاحيات الأساسية فقط (غرفة واحدة)
android.permissions = INTERNET, ACCESS_NETWORK_STATE

python-for-android.branch = release-2022.12.20
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
