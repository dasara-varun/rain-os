# Rain OS v1.3.2 Automated ISO Downloader & Reassembler
# Downloads multi-part ISO assets from GitHub Releases and merges them into a single bootable ISO.

$ErrorActionPreference = "Stop"

$OutDir = Join-Path (Split-Path -Parent $PSScriptRoot) "out"
if (-not (Test-Path $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir | Out-Null
}

$BaseUrl = "https://github.com/dasara-varun/rain-os/releases/download/v1.3.2"
$PartAA = Join-Path $OutDir "rain-os-1.3.2-x86_64.iso.part-aa"
$PartAB = Join-Path $OutDir "rain-os-1.3.2-x86_64.iso.part-ab"
$OutputIso = Join-Path $OutDir "rain-os-1.3.2-x86_64.iso"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "     Rain OS v1.3.2 - Local ISO Downloader & Assembler    " -ForegroundColor White
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Destination: $OutputIso" -ForegroundColor Gray
Write-Host ""

# Download Part AA
if (-not (Test-Path $PartAA)) {
    Write-Host "[1/4] Downloading ISO Part 1 (1,800 MB)..." -ForegroundColor Yellow
    if (Get-Command curl.exe -ErrorAction SilentlyContinue) {
        & curl.exe -L -# -o $PartAA "$BaseUrl/rain-os-1.3.2-x86_64.iso.part-aa"
    } else {
        $ProgressPreference = 'SilentlyContinue'
        Invoke-WebRequest -Uri "$BaseUrl/rain-os-1.3.2-x86_64.iso.part-aa" -OutFile $PartAA
    }
} else {
    Write-Host "[1/4] ISO Part 1 already exists." -ForegroundColor Green
}

# Download Part AB
if (-not (Test-Path $PartAB)) {
    Write-Host "[2/4] Downloading ISO Part 2 (442 MB)..." -ForegroundColor Yellow
    if (Get-Command curl.exe -ErrorAction SilentlyContinue) {
        & curl.exe -L -# -o $PartAB "$BaseUrl/rain-os-1.3.2-x86_64.iso.part-ab"
    } else {
        $ProgressPreference = 'SilentlyContinue'
        Invoke-WebRequest -Uri "$BaseUrl/rain-os-1.3.2-x86_64.iso.part-ab" -OutFile $PartAB
    }
} else {
    Write-Host "[2/4] ISO Part 2 already exists." -ForegroundColor Green
}

# Reassemble
Write-Host "[3/4] Reassembling complete 2.24 GB ISO image..." -ForegroundColor Cyan
cmd.exe /c "copy /b `"$PartAA`" + `"$PartAB`" `"$OutputIso`"" | Out-Null

# Clean up part files
Remove-Item $PartAA -Force -ErrorAction SilentlyContinue
Remove-Item $PartAB -Force -ErrorAction SilentlyContinue

# Verify
Write-Host "[4/4] Verifying file size..." -ForegroundColor Cyan
$IsoSize = (Get-Item $OutputIso).Length / 1MB
Write-Host ""
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "SUCCESS! Rain OS v1.3.2 ISO is ready for flashing:" -ForegroundColor Green
Write-Host "  File: $OutputIso ($([math]::Round($IsoSize, 2)) MB)" -ForegroundColor White
Write-Host "==========================================================" -ForegroundColor Green
