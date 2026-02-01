[app]
title = The Guard - Node 7
package.name = theguard_n7
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 1.3.6

requirements = python3, kivy==2.3.0, hostpython3, pyjnius

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0
fullscreen = 0

android.permissions = INTERNET, ACCESS_NETWORK_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, PACKAGE_USAGE_STATS, READ_PHONE_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
android.skip_update = android.skip_update = False
log_level = 1
p4a.branch = master

# هذه هي الضربة القاضية: القراءة من ملف خارجي لتجنب الحرق
android.extra_manifest_xml = ./extra_manifest.xml
