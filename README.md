# Rain OS

<p align="center">
  <img src="branding/rain-logo.png" alt="Rain OS 4K Umbrella Logo" width="180" height="180">
</p>

<p align="center">
  <strong>Shelter from complexity, without hiding the system.</strong>
</p>

<p align="center">
  <a href="https://github.com/dasara-varun/rain-os/actions/workflows/build-iso.yml"><img src="https://github.com/dasara-varun/rain-os/actions/workflows/build-iso.yml/badge.svg" alt="Build ISO"></a>
  <a href="https://github.com/dasara-varun/rain-os/actions/workflows/validate.yml"><img src="https://github.com/dasara-varun/rain-os/actions/workflows/validate.yml/badge.svg" alt="Validate Spec"></a>
  <a href="https://github.com/dasara-varun/rain-os/actions/workflows/release.yml"><img src="https://github.com/dasara-varun/rain-os/actions/workflows/release.yml/badge.svg" alt="Release Pipeline"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL_3.0-blue.svg" alt="License: GPL 3.0"></a>
</p>

---

## What is Rain OS?

**Rain OS** is an independent, commercial-grade Linux distribution built on an Arch Linux foundation. It delivers a modern, resilient desktop engineered around safety, user empowerment, and honest computing:

1. **Universal App Compatibility**: Seamlessly install and run native Linux packages, **KDE Discover Software Center**, **Flatpaks from Flathub**, portable **AppImages** (out-of-the-box FUSE2 support), and Windows `.exe` applications via the built-in **Windows Compatibility Bridge** (Bottles, Wine, Steam Proton, and Quickemu VM fallback).
2. **Safe to Recover**: Automated pre-upgrade Btrfs snapshots (`00-rain-pre-snapshot.hook`), preflight update checks, dual bootable kernels (`linux` generic + `linux-lts` certified stability fallback), and offline recovery tools.
3. **Multi-Screen & Device Connectivity**: Wayland/X11 multi-monitor management with per-screen fractional DPI scaling, variable refresh rates (FreeSync/G-Sync), **KDE Connect** for instant Android/iOS phone sync, Bluetooth pairing, and zero-configuration local network file sharing (Samba & Avahi).
4. **Broad Hardware Support**: Complete driver coverage for modern GPUs (NVIDIA proprietary/nouveau, AMD Radeon, Intel Iris/Arc) and legacy systems (`xf86-video-vesa`, `fbdev`), broad Wi-Fi chipsets (Intel, Realtek, Broadcom), and low-power CPU governor tuning.
5. **C & C++ Native Performance**: Core hardware and multi-screen telemetry powered by an ultra-fast compiled native C engine (`rain-probe`) with sub-millisecond execution.
6. **Zero Telemetry & Private by Default**: No tracking identifiers, no telemetry daemons, no online accounts required. All machine state stays on your device.

---

## Key Features & Architecture

```text
???????????????????????????????????????????????????????????????????????????
?                           Rain OS Desktop                               ?
?      KDE Plasma (Default)  ?  COSMIC Rust Profile  ?  Multi-Screen      ?
???????????????????????????????????????????????????????????????????????????
?        Native Linux Apps          ?      Windows Compatibility          ?
? Discover ? Flatpak ? AppImage     ? Bottles ? Wine ? Proton ? Quickemu  ?
???????????????????????????????????????????????????????????????????????????
?                          Rain Integration Hub                           ?
?  Rain Welcome  ?  Control Center  ?  Learning Hub  ?  Hardware Wizard   ?
???????????????????????????????????????????????????????????????????????????
?                          Safety & Recovery                              ?
?   Btrfs Subvolumes (@, @home, @snapshots) ? Pacman Pre-Snapshot Hook    ?
?   Dual Kernels (linux + linux-lts) ? Update Preflight ? Diagnostic Bundler?
???????????????????????????????????????????????????????????????????????????
?                          Arch Linux Core Base                           ?
?         PipeWire ? NetworkManager ? Firewalld ? SDDM ? Calamares        ?
???????????????????????????????????????????????????????????????????????????
```

### 1. App Store & Software Ecosystem
- **KDE Discover**: Graphical Software Center for discovering and updating native packages and system add-ons.
- **Flathub Integration**: One-click enablement for thousands of sandboxed Flatpak applications.
- **Native AppImage Support**: `fuse2` compatibility layer pre-installed, allowing AppImages to launch instantly without manual terminal setup.
- **Windows Apps & Gaming Bridge**: Direct control over Bottles, Wine, Steam Proton, and Quickemu/KVM virtual machine fallbacks directly in the Control Center.

### 2. Multi-Screen & Device Synchronization
- **Multi-Monitor Display Manager**: Per-monitor refresh rates, fractional scaling (100%, 125%, 150%, 200%), monitor rotation, and primary display selection powered by `kscreen`.
- **KDE Connect Integration**: Wirelessly link your Android or iOS smartphone to share clipboards, receive notifications, respond to messages, and transfer files.
- **Local Network Sharing**: Samba and Avahi mDNS pre-configured for instant discovery of shared folders and NAS storage in Dolphin.

### 3. Modular System Profiles (`rain-profile`)
Switch system profiles instantly in the Control Center or terminal (`rain-profile set <profile>`):
- **`core`**: Balanced daily desktop stability, default LTS kernel, balanced governor.
- **`flow`**: High-performance gaming, performance governor, low swappiness (`10`), gamemode optimization.
- **`forge`**: Software engineering workspace with container runtimes, elevated inotify watches (`524288`), and compiler toolchains.
- **`shield`**: Hardened security with AppArmor profiles, strict firewall drop rules, and restricted `dmesg`.
- **`pocket`**: Low-RAM and battery saver profile with powersave governor and aggressive memory reclamation.
- **`cosmic`**: Modern Rust-based desktop environment (System76 COSMIC session and auto-tiling).

### 4. Dual-Kernel & Rollback Guarantee
- Rain OS always retains both `linux` (latest upstream) and `linux-lts` (long-term stability fallback).
- Default bootloader entries can be switched with one click via `rain-kernel set-default <lts|generic>`.
- Pacman hook automatically creates a read-only snapshot before any upgrade or package removal transaction.

---

## Visual Identity & 4K Design System

- **Master Emblem**: Ultra-HD 4096?4096 glowing umbrella logo mark ([`branding/rain-logo-4k.png`](branding/rain-logo-4k.png)).
- **4K UHD Wallpaper**: Native 3840?2160 background canvas ([`branding/rain-wallpaper-4k.jpg`](branding/rain-wallpaper-4k.jpg)).
- **Palette**: **Urban Rain** (`#1E222B` dark slate background, `#282D37` surface cards, `#E83E38` crimson accent).
- **Terminal Fastfetch**: Beautiful Rain OS ASCII umbrella logo displayed on Konsole launch.

---

## Command Line Utilities

| Utility | Description |
|---|---|
| `rain-guide` | Offline Learning Hub reader (`list`, `read <num>`, `search`, `doctor`, `status`) |
| `rain-control-center` | Unified graphical system settings, profiles, software hub, and hardware |
| `rain-first-run` | First-run onboarding assistant and baseline specs scanner |
| `rain-hardware-report` | Hardware inspector for GPU (NVIDIA/AMD/Intel), Wi-Fi, and power governors |
| `rain-probe` | Native compiled C hardware and multi-screen probe (<1 ms execution) |
| `rain-profile` | System role switcher (`core`, `flow`, `forge`, `shield`, `pocket`, `cosmic`) |
| `rain-kernel` | Dual-kernel boot default selector (`generic` vs `lts`) |
| `rain-btrfs-snapshot` | Automated Btrfs snapshot engine and retention pruner |
| `rain-update-preflight` | Safe update preflight health checker |
| `rain-recovery` | Disaster recovery helper, Btrfs rollback guide, and log secret scrubber |
| `rain-display-manager` | Multi-screen configuration and KScreen launcher |

---

## Building Rain OS

### Automated Cloud Build (GitHub Actions)
Every commit to `main` is automatically compiled and verified inside an official Arch Linux container on GitHub Actions.
- Workflow: [`.github/workflows/build-iso.yml`](.github/workflows/build-iso.yml)
- Automated QA: Every ISO build is subjected to a headless 35-second **QEMU smoke boot test** to verify kernel initialization and systemd readiness before release.
- Output: Download the bootable ISO, `SHA256SUMS`, and CycloneDX `rain-os-sbom.json` directly from the Actions artifact tab.

### Local Build on Linux
```bash
sudo pacman -S --needed archiso git base-devel qemu-system-x86 edk2-ovmf
./scripts/validate-spec.sh
./tests/test-syntax.sh
sudo ./scripts/build-iso.sh
```

---

## License & Provenance

Rain OS source code, scripts, and original artwork are licensed under the [GNU General Public License v3.0](LICENSE). Upstream components, kernels, firmware, and packages adhere to their respective licenses as cataloged in [`manifests/PROVENANCE_LEDGER.csv`](manifests/PROVENANCE_LEDGER.csv).
