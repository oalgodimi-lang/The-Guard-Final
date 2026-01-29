[app]
title = The Guard
package.name = theguard
package.domain = im.manus.node7
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy==2.2.1,android,cython==0.29.33,sh,setuptools

# الصلاحيات السيادية
android.permissions = INTERNET, ACCESS_NETWORK_STATE, FOREGROUND_SERVICE

# إعدادات البناء
android.archs = arm64-v8a
android.api = 33
android.accept_sdk_license = True
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
# android.sdk = 21

# التمويه (أيقونة بسيطة)
# android.presplash_color = #000000
