<#
.SYNOPSIS
    Rain OS Windows Build Helper & Environment Orchestrator
.DESCRIPTION
    Automates and guides the build process for Rain OS on Windows systems.
    Since mkarchiso requires Linux loop devices, POSIX file permissions,
    and squashfs capabilities, this script orchestrates WSL2 or Docker.
#>

[CmdletBinding()]
param(
    [switch]$Docker,
    [switch]$Help
)

$ErrorActionPreference = "Stop"

function Write-Header {
    Write-Host ""
    Write-Host "  _____       _             ____   _____ " -ForegroundColor Cyan
    Write-Host " |  __ \     (_)           / __ \ / ____|" -ForegroundColor Cyan
    Write-Host " | |__) |__ _ _ _ __ _____| |  | | (___  " -ForegroundColor Cyan
    Write-Host " |  _  // _` | | '_ \____/| |  | |\___ \ " -ForegroundColor Cyan
    Write-Host " | | \ \ (_| | | | | |    | |__| |____) |" -ForegroundColor Cyan
    Write-Host " |_|  \_\__,_|_|_| |_|     \____/|_____/ " -ForegroundColor Cyan
    Write-Host ""
    Write-Host " Rain OS Windows Build Orchestrator" -ForegroundColor White
    Write-Host " ==========================================================" -ForegroundColor Gray
}

Write-Header

$WorkspaceDir = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

# 1. Check for Docker mode
if ($Docker) {
    Write-Host "[*] Docker build mode selected..." -ForegroundColor Yellow
    if (Get-Command docker -ErrorAction SilentlyContinue) {
        Write-Host "[+] Docker found. Starting build container (archlinux:base-devel)..." -ForegroundColor Green
        $WslPath = $WorkspaceDir.Replace('\', '/')
        docker run --privileged --rm -v "${WorkspaceDir}:/build" -w /build archlinux:base-devel bash -c @"
            pacman -Syu --noconfirm archiso git base-devel dosfstools mtools squashfs-tools
            ./scripts/validate-spec.sh
            ./scripts/build-iso.sh
"@
        exit $LASTEXITCODE
    } else {
        Write-Error "Docker is not installed or not in PATH."
    }
}

# 2. Check WSL status
Write-Host "[*] Checking Windows Subsystem for Linux (WSL) status..." -ForegroundColor Cyan

$WslInstalled = $false
try {
    $wslCheck = wsl --status 2>&1
    if ($LASTEXITCODE -eq 0) {
        $WslInstalled = $true
    }
} catch {
    $WslInstalled = $false
}

if (-not $WslInstalled) {
    Write-Host ""
    Write-Host "[!] WSL2 is not currently installed or configured on this Windows machine." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Why is Linux required to build an OS ISO?" -ForegroundColor White
    Write-Host "  Archiso (mkarchiso) builds bootable Linux ISOs using kernel loopback"
    Write-Host "  mounts (/dev/loop*), ext4/squashfs filesystems, and Linux root chroot."
    Write-Host "  Native Windows cannot run mkarchiso without a Linux kernel."
    Write-Host ""
    Write-Host "Recommended Options to Build:" -ForegroundColor Cyan
    Write-Host "--------------------------------------------------------" -ForegroundColor Gray
    Write-Host "Option A: Cloud Build via GitHub Actions (Zero Local Setup)" -ForegroundColor Green
    Write-Host "  Simply push your commits to https://github.com/dasara-varun/rain-os"
    Write-Host "  The included GitHub Actions workflow automatically builds the ISO"
    Write-Host "  and attaches the downloadable ISO to your repository Releases!"
    Write-Host ""
    Write-Host "Option B: Enable WSL2 Locally" -ForegroundColor Yellow
    Write-Host "  1. Open PowerShell as Administrator and run:"
    Write-Host "     wsl --install"
    Write-Host "  2. Restart your computer if prompted."
    Write-Host "  3. Re-run this script: .\scripts\build-windows.ps1"
    Write-Host ""
    Write-Host "Option C: Docker Desktop" -ForegroundColor White
    Write-Host "  Install Docker Desktop for Windows and run:"
    Write-Host "     .\scripts\build-windows.ps1 -Docker"
    Write-Host "--------------------------------------------------------" -ForegroundColor Gray
    exit 1
}

# 3. WSL is installed - detect Arch distros
Write-Host "[+] WSL is active. Inspecting installed distributions..." -ForegroundColor Green
$distros = wsl --list -q 2>&1

$archDistro = $distros | Where-Object { $_ -match "arch" } | Select-Object -First 1

if ($archDistro) {
    $archDistro = $archDistro.Trim()
    Write-Host "[+] Found Arch Linux distribution in WSL: $archDistro" -ForegroundColor Green
    
    # Convert path to WSL mount
    $driveLetter = $WorkspaceDir.Substring(0, 1).ToLower()
    $subPath = $WorkspaceDir.Substring(2).Replace('\', '/')
    $wslWorkspace = "/mnt/$driveLetter$subPath"

    Write-Host "[*] Executing build in WSL ($archDistro)..." -ForegroundColor Cyan
    wsl -d $archDistro -u root --cd $wslWorkspace bash -c "pacman -Sy --needed --noconfirm archiso && ./scripts/build-iso.sh"
} else {
    Write-Host "[-] No native Arch Linux distribution found in WSL." -ForegroundColor Yellow
    Write-Host "    Installed WSL distros: $($distros -join ', ')"
    Write-Host ""
    Write-Host "To install ArchWSL:" -ForegroundColor Cyan
    Write-Host "  Download ArchWSL from: https://github.com/yuk7/ArchWSL/releases"
    Write-Host "  Extract and run Arch.exe to register the Arch Linux WSL instance."
    Write-Host ""
    Write-Host "Alternatively, use GitHub Actions to build the ISO automatically on GitHub!" -ForegroundColor Green
}
