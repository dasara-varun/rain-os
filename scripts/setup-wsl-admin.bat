@echo off
setlocal
echo =======================================================
echo     Rain OS - Enable WSL2 for Local ISO Building
echo =======================================================
echo.

:: Self-elevate to administrator if not elevated
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [!] Requesting Administrator privileges...
    powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Start-Process cmd -ArgumentList '/k \"\"%~f0\"\"' -Verb RunAs"
    exit /b 0
)

echo [+] Administrator privileges confirmed.
echo [*] Installing Windows Subsystem for Linux (WSL2) with Ubuntu...
wsl.exe --install -d Ubuntu

echo.
echo =======================================================
echo [!] WSL2 installation initialized!
echo.
echo 1. If Windows prompts to restart, restart your computer now.
echo 2. After restart, open "Ubuntu" from your Windows Start Menu.
echo 3. Inside Ubuntu, run:
echo      /mnt/e/rain\ os/scripts/setup-self-hosted-runner.sh
echo =======================================================
echo.
pause

