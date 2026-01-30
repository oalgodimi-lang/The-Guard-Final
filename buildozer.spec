[app]

# (str) Title of your application
title = The Guard - Node 7

# (str) Package name
package.name = theguard

# (str) Package domain (needed for android packaging)
package.domain = org.sovereign

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# تم إضافة android و pyjnius و requests وتثبيت إصدار kivy لضمان السيادة التقنية
requirements = python3,kivy==2.3.0,pyjnius,android,requests,hostpython3

# (str) Custom source folders for requirements
# (list) List of garden recipes to virtualenv
# (str) Application versioning
version = 1.1.7

# (list) Application permissions
# تم تفعيل صلاحيات الخدمة والعمل في الخلفية
android.permissions = INTERNET, FOREGROUND_SERVICE, WAKE_LOCK, POST_NOTIFICATIONS, RECEIVE_BOOT_COMPLETED

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Android service to declare
# ربط النواة (service.py) بالواجهة (main.py)
android.services = monitor:service.py

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) Android additional libraries to copy into libs/armeabi
# (bool) Copy library instead of making a libpysqlite3.so
# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >= 23)
android.allow_backup = True

# (str) XML file for the security configuration
# (str) Name of the screen orientation
orientation = portrait

# (list) List of service to declare
# (list) List of Java files to add to the android project
# (list) List of Java jars to add to the android project
# (list) List of Java libs to add to the android project

# -----------------------------------------------------------------------------
# Buildozer sections
# -----------------------------------------------------------------------------

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
