[app]
title = Frog Quiz
package.name = frogquiz
package.domain = org.katiehoward
source.dir = .
source.include_exts = py,mp4,png,jpg,jpeg,html,css,js,json
source.include_patterns = assets/*,*.py
version = 1.0
orientation = landscape
fullscreen = 1
entrypoint = main.py
icon.filename = assets/App_overview.png
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE
requirements = python3==3.10.10,hostpython3==3.10.10,kivy==2.2.1,pyjnius,android
p4a.branch = master
android.api = 33
android.minapi = 21
android.ndk = 25b
android.gradle_dependencies = 
android.archs = arm64-v8a
android.skip_update = False
android.accept_sdk_license = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1