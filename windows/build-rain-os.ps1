param(
  [string]$Distro = "archlinux",
  [string]$Repo = "~/src/rain-os"
)
$ErrorActionPreference = "Stop"
$wsl = Get-Command wsl.exe -ErrorAction SilentlyContinue
if (-not $wsl) { throw "WSL2 is not installed. Run: wsl --install; wsl --update" }
$distros = & wsl.exe --list --quiet
if ($LASTEXITCODE -ne 0 -or ($distros -notmatch [regex]::Escape($Distro))) {
  throw "WSL distribution '$Distro' was not found. Check: wsl --list --quiet"
}
Write-Host "Building Rain OS inside WSL2 distribution '$Distro' at $Repo"
& wsl.exe -d $Distro -- bash -lc "cd $Repo && ./scripts/build-one-shot.sh"
if ($LASTEXITCODE -ne 0) { throw "Rain OS build failed inside WSL2" }
Write-Host "Build finished. Copy the ISO from the WSL output directory only after VM testing."
