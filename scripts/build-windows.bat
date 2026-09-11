@echo off
setlocal
echo ========================================
echo       Rain OS Windows Builder
echo ========================================
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0build-windows.ps1" %*
pause
