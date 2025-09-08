
# HabilitacaoApp (Kivy)

## Rodar no PC
pip install -r requirements.txt
python main.py

## Gerar APK com Buildozer (Linux/WSL)
pip install buildozer
sudo apt-get update && sudo apt-get install -y build-essential git zip unzip openjdk-17-jdk
pip install cython virtualenv
buildozer -v android debug

O APK ficará em `bin/`.
