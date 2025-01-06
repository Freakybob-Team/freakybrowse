@echo off
cd ..

python --version >nul 2>&1

if %errorlevel% equ 0 (
  echo good! you have python installed :fire:
) else (
  echo you can't run FreakyBrowse without Python. Go download it plz !!
)

pip install -r requirements.txt -q

if %errorlevel% equ 0 (
  echo Everything is already installed!!!!!!!!
) else (
  echo Installation complete :3
)
pause
