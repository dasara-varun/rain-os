# Rain OS Local ISO Build on Windows

## Recommended topology

Use Windows as the host and WSL2 as the Linux build environment:

```text
Windows 11/10
├── Windows Terminal / PowerShell
├── WSL2
│   └── official Arch Linux WSL distribution
│       └── /home/<user>/rain-os  ← repository and build workdir
├── QEMU/Hyper-V/VirtualBox       ← boot and installer testing
└── USB writer                    ← physical hardware testing after VM gates
```

This is the fastest practical local route because `mkarchiso`, `pacman`, Bash tooling, and the Rain builder tools run inside Linux. Keep the repository in the WSL filesystem, not under `/mnt/c`, because WSL documentation warns that Windows-mounted project paths are slower for Linux workloads and file watching.

## One-time Windows setup

Open PowerShell as Administrator:

```powershell
wsl --install
wsl --update
wsl --set-default-version 2
wsl --install archlinux
```

Restart Windows if requested. Confirm the distribution is WSL2:

```powershell
wsl --list --verbose
```

Start the distribution and create a normal user. Do not build as the root user. Enable virtualization in firmware if WSL2 is unavailable.

## One-time Arch builder setup

Inside Arch WSL:

```bash
sudo pacman -Syu --needed git base-devel archiso qemu-desktop edk2-ovmf rsync jq shellcheck
mkdir -p ~/src
cd ~/src
git clone <YOUR_RAIN_OS_REPOSITORY_URL> rain-os
cd rain-os
```

If the repository is already available, place it at `~/src/rain-os` or another path under `/home`.

## One-command build

From the Rain OS repository inside WSL:

```bash
./scripts/build-one-shot.sh
```

The script checks that it is running in Linux/WSL, installs missing builder dependencies, copies the installed Archiso `releng` profile, overlays the Rain package list and profile metadata, builds the ISO, generates checksums and a package manifest, and writes artifacts under `out/`.

From PowerShell, use:

```powershell
wsl -d archlinux -- bash -lc "cd ~/src/rain-os && ./scripts/build-one-shot.sh"
```

The exact WSL distribution name may be `Arch`, `archlinux`, or a custom imported name. Check with `wsl --list --quiet`.

## Test the ISO before writing USB

Use QEMU from WSL if virtualization and display forwarding are configured, or copy the ISO to Windows and use Hyper-V/VirtualBox. Always test boot, installer, networking, desktop, update, and recovery before physical media.

## Important limitations

WSL2 builds the ISO but is not the target OS environment. It cannot prove that the ISO works on every GPU, Wi-Fi chipset, firmware, Secure Boot configuration, or laptop suspend implementation. The build script is one-shot for artifact production, not a substitute for VM and hardware gates.

Do not build under `/mnt/c`, do not place private signing keys in the repository, and do not enable custom Secure Boot keys during the first local build.
