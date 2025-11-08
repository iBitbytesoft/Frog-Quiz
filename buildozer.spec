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
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
requirements = python3,kivy,pyjnius,android,nicegui,fastapi,uvicorn,typing-extensions,pydantic
android.api = 33
android.minapi = 28
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1