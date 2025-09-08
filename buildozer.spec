[app]
# (str) Title of your application
title = HabilitacaoApp

# (str) Package name
package.name = habilitacaoapp
package.domain = org.yourname

# (str) Source code entry point (main .py)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (str) Versioning
version = 0.1
android.archive = unsigned

# (str) Icon and splash (uncomment and add files if you have)
# icon.filename = %(source.dir)s/assets/icon.png

# (list) Permissions
android.permissions = INTERNET

# (str) Files to add to the apk assets
android.add_assets = assets/*.png, assets/*.jpg

# (str) Orientation: portrait, landscape or all
orientation = portrait

# (bool) If True, will build as a debug APK (unsigned debug)
debug = True

# (int) Android API to target and build tools version (recommended defaults)
# You can change these if CI/build system complains; python-for-android will install matching sdks.
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b

# (bool) Use --private data dir (recommended for quick testing)
android.private_storage = True

# Versão estável do Build-Tools (evita RC que trava no GitHub Actions)
android.build_tools_version = 33.0.2

# API do Android a ser usada
android.api = 33

# Outras configurações básicas
android.sdk = 20
android.ndk = 25b
android.minapi = 21
android.target = 33
