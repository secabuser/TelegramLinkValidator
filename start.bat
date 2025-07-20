@echo off
cls
echo Installing ...
pip install -r requirements.txt

:menu
cls
echo.
echo [1] Run Link Generator
echo [2] Run Link Validator
echo [0] Exit
set /p choice=choice >

if "%choice%"=="1" (
    python gen.py
    goto menu
) else if "%choice%"=="2" (
    python valid.py
    goto menu
) else if "%choice%"=="0" (
    exit
) else (
    echo Invalid choice!
    timeout /t 2 >nul
    goto menu
)
