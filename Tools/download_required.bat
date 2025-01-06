@echo off
cd ..
pip install -r requirements.txt -q

if %errorlevel% equ 0 (
  echo Everything is already installed!!!!!!!!
) else (
  echo Installation complete :3
)
pause
