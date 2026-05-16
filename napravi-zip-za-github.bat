@echo off
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0napravi-zip-za-github.ps1"
if errorlevel 1 pause
pause
