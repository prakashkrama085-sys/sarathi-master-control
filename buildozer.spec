[app]
# (str) Title of your application
title = Sarathi Master Control

# (str) Package name
package.name = sarathi_master

# (str) Package domain (needed for android packaging)
package.domain = org.prakash

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 4.0

# (list) Application requirements
# मास्‍टर, यहाँ हमने आपके प्रोजेक्ट के लिए ज़रूरी लाइब्रेरीज़ डाल दी हैं
requirements = python3,kivy,flask,requests,urllib3

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
# सिस्टम को शक्ति देने के लिए ज़रूरी परमिशन्स
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Android API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use private storage for logs
android.logcat_filters = *:S python:D