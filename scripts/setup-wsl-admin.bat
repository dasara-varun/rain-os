@echo off
setlocal
echo =======================================================
echo     Rain OS - Enable WSL2 for Local ISO Building
echo =======================================================
echo.
echo Checking administrator privileges...
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [!] This script must be run as Administrator.
    echo Right-click 'setup-wsl-admin.bat' and select 'Run as administrator'.
    echo.
    pause
    exit /b 1
)

echo [+] Administrator privileges confirmed.
echo [*] Enabling Windows Subsystem for Linux (WSL2)...
wsl.exe --install

echo.
echo =======================================================
echo [!] IMPORTANT NEXT STEP:
echo If Windows prompts to restart, please restart your computer now.
echo After restart, open this folder and double-click:
echo     scripts\build-windows.bat
echo to build the Rain OS ISO locally!
echo =======================================================
echo.
pause
