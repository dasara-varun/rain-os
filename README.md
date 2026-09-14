# Rain OS

<p align="center">
  <img src="branding/rain-logo.png" alt="Rain OS 4K Umbrella Logo" width="180" height="180">
</p>

<p align="center">
  <strong>Shelter from complexity, without hiding the system.</strong>
</p>

<p align="center">
  <a href="https://github.com/is-it-raining-now/rain-os/actions/workflows/build-iso.yml"><img src="https://github.com/is-it-raining-now/rain-os/actions/workflows/build-iso.yml/badge.svg" alt="Build ISO"></a>
  <a href="https://github.com/is-it-raining-now/rain-os/actions/workflows/validate.yml"><img src="https://github.com/is-it-raining-now/rain-os/actions/workflows/validate.yml/badge.svg" alt="Validate Spec"></a>
  <a href="https://github.com/is-it-raining-now/rain-os/actions/workflows/release.yml"><img src="https://github.com/is-it-raining-now/rain-os/actions/workflows/release.yml/badge.svg?branch=v1.3.2" alt="Release Pipeline"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL_3.0-blue.svg" alt="License: GPL 3.0"></a>
  <a href="https://github.com/is-it-raining-now/rain-os/releases/tag/v1.3.2"><img src="https://img.shields.io/badge/Release-v1.3.2-success.svg" alt="Latest Release"></a>
</p>

---

## What is Rain OS?

**Rain OS** is an independent, commercial-grade Linux distribution built on an Arch Linux foundation. It delivers a modern, resilient desktop engineered around safety, user empowerment, and honest computing:

1. **COSMIC Desktop by Default**: Modern, lightning-fast Rust-based desktop environment by System76. Features native auto-tiling, Wayland layer-shell panels, sub-300MB idle memory, and smooth fractional scaling.
2. **Vertical Installation Desktop Selector**: Choose your preferred desktop environment or window manager during system installation in a clean, scrollable vertical interface pre-selecting COSMIC Desktop.
3. **Modern App Store (`cosmic-store`)**: Sub-second startup, Flathub Flatpak integration out of the box, and zero PackageKit pacman database lock contention.
4. **Universal App Compatibility**: Seamlessly install and run native Linux packages, sandboxed **Flatpaks from Flathub**, portable **AppImages** (pre-configured FUSE2 support), and Windows `.exe` applications via the built-in **Windows Compatibility Bridge** (Bottles, Wine, Steam Proton, and Quickemu VM fallback).
5. **Dedicated Application Iconography**: 8 unique, high-contrast application icons for the Control Center, Installer, Welcome GUI, Learning Hub, Desktop Selector, App Store, Hardware Wizard, and Display Manager.
6. **Clean Live Desktop**: Minimalist, distraction-free live boot with only two desktop shortcuts: **Install Rain OS to Disk** and **Rain Learning Hub**, with all intrusive popup windows suppressed.
7. **Safe to Recover**: Automated pre-upgrade Btrfs snapshots (`00-rain-pre-snapshot.hook`), preflight update checks, dual bootable kernels (`linux` generic + `linux-lts` certified stability fallback), and offline recovery tools.
8. **Multi-Screen & Device Connectivity**: Wayland/X11 multi-monitor management with per-screen fractional DPI scaling, variable refresh rates (FreeSync/G-Sync), phone sync, Bluetooth pairing, and zero-configuration local network file sharing.
9. **C & C++ Native Performance**: Core hardware and multi-screen telemetry powered by an ultra-fast compiled native C engine (`rain-probe`) with sub-millisecond execution.
10. **Zero Telemetry & Private by Default**: No tracking identifiers, no telemetry daemons, no online accounts required. All machine state stays strictly on your device.

---

## Key Features & Architecture

```text
+---------------------------------------------------------------------------+
|                              Rain OS Desktop                              |
|   COSMIC Desktop (Flagship) • Hyprland • Plasma 6 • GNOME • i3 • Sway     |
|   Niri • River • Gamescope+MangoHUD • XFCE4 • Multi-Screen Support        |
+---------------------------------------------------------------------------+
|          Native Linux Apps           |       Windows Compatibility        |
|  COSMIC Store • Flatpak • AppImage   |  Bottles • Wine • Proton • Quickemu|
+---------------------------------------------------------------------------+
|                            Rain Integration Hub                           |
|  Vertical Selector • Omarchy Engine • Control Center • Hardware Wizard    |
+---------------------------------------------------------------------------+
|                            Safety & Recovery                              |
|     Btrfs Subvolumes (@, @home, @snapshots) • Pacman Pre-Snapshot Hook    |
|     Dual Kernels (linux + linux-lts) • Update Preflight • Rollback Tool   |
+---------------------------------------------------------------------------+
|                            Arch Linux Core Base                           |
|           PipeWire • NetworkManager • Firewalld • SDDM • Calamares        |
+---------------------------------------------------------------------------+
```

### 1. Vertical Desktop & Window Manager Selection in Installer
Integrated directly into `rain-install-launcher` and Calamares/archinstall, displaying options in a clean, scrollable **vertical order**:
- **COSMIC Desktop [Flagship Default]**: Modern, memory-safe desktop written in Rust by System76. Modular, Wayland-native, and high-performance.
- **Hyprland [Dynamic Tiling]**: Ultra-fluid Wayland dynamic tiling compositor with smooth animations, rounded corners, blur, and deep Omarchy theming.
- **KDE Plasma 6 [Customizable DE]**: Customizable, feature-rich desktop with translucent glass UI and extensive widgets.
- **GNOME Shell [Gesture Driven]**: Distraction-free, gesture-driven desktop shell designed for focused, keyboard-centric productivity.
- **i3-wm [Ultra Lightweight]**: Ultra-lightweight keyboard-driven manual X11 tiling window manager.
- **Sway [Wayland Tiling]**: Drop-in replacement for i3 on Wayland with zero tearing and smooth wlroots hardware acceleration.
- **XFCE 4 [Classic Modular]**: Classic, modular, battle-tested desktop for older hardware.
- **Niri [Scrollable Ribbon]**: Infinite horizontal ribbon of windows with fluid animations and intuitive touchpad gestures.
- **River WM [Dynamic Tiling]**: Flexible, dynamic tiling Wayland compositor with rich tag-based workspace management.
- **Gamescope + MangoHUD [Gaming Edition]**: Optimized SteamOS-style dedicated gaming session with MangoHUD telemetry and integer scaling.

### 2. Official Omarchy Themes Engine (22 Signature Themes)
Integrated directly into `rain-desktop-selector`, adapted from `omacom/omarchy` with unified palettes across Hyprland, Waybar, Rofi, Alacritty, and desktop settings:
- `tokyo-night` • `catppuccin` • `catppuccin-latte` • `everforest` • `gruvbox` • `kanagawa`
- `matte-black` • `nord` • `rose-pine` • `solitude` • `vantablack` • `ethereal`
- `flexoki-light` • `hackerman` • `last-horizon` • `lumon` • `lupine` • `miasma`
- `osaka-jade` • `retro-82` • `ristretto` • `white`

### 3. 12 Pristine 4K Anime Rain Wallpapers
- High-definition 3840×2160 UHD native wallpapers inspired by the Rain OS aesthetic.
- Zero white cuts, zero watermarks, zero slogans, and zero blurriness.
- 1-click wallpaper switcher built into `rain-desktop-selector`.
- Universal wallpaper parity across SDDM greeter, lockscreen, and desktop sessions.

### 4. App Store & Software Ecosystem
- **Rain App Store (`cosmic-store`)**: Modern Rust-based Software Center for discovering and installing native packages and Flatpaks with zero database lock contention.
- **Flathub Integration**: One-click enablement for thousands of sandboxed Flatpak applications.
- **Native AppImage Support**: `fuse2` compatibility layer pre-installed, allowing AppImages to launch instantly without manual terminal setup.
- **Windows Apps & Gaming Bridge**: Direct control over Bottles, Wine, Steam Proton, and Quickemu/KVM virtual machine fallbacks directly in the Control Center.

### 5. Multi-Screen & Device Synchronization
- **Multi-Monitor Display Settings**: Per-monitor refresh rates, fractional scaling (100%, 125%, 150%, 200%), monitor rotation, and primary display selection.
- **Phone Synchronization**: Wirelessly link your Android or iOS smartphone to share clipboards, receive notifications, respond to messages, and transfer files.
- **Local Network Sharing**: Samba and Avahi mDNS pre-configured for instant discovery of shared folders and NAS storage.

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

- **Master Emblem**: Ultra-HD 4096×4096 glowing umbrella logo mark ([`branding/rain-logo-4k.png`](branding/rain-logo-4k.png)).
- **4K UHD Wallpaper**: Native 3840×2160 background canvas ([`branding/rain-wallpaper-4k.jpg`](branding/rain-wallpaper-4k.jpg)).
- **Palette**: **Urban Rain** (`#1E222B` dark slate background, `#282D37` surface cards, `#E83E38` crimson accent).
- **Terminal Fastfetch**: Beautiful Rain OS ASCII umbrella logo displayed on terminal launch (`cosmic-terminal`, `alacritty`).

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
- Self-Hosted Runner Option: Build directly on your local workstation with unlimited CPU cores and zero 2GB limits. See [Self-Hosted Runner Guide](docs/SELF_HOSTED_RUNNER_GUIDE.md).
- Output: Download the bootable ISO, `SHA256SUMS`, and CycloneDX `rain-os-sbom.json` directly from the Actions artifact tab.

### Local Build on Linux / WSL2
```bash
sudo pacman -S --needed archiso git base-devel qemu-system-x86 edk2-ovmf
./scripts/validate-spec.sh
./tests/test-syntax.sh
sudo ./scripts/build-iso.sh
```

---

## Releases & Package Distribution

### Official Version Releases & Tags
Releases are cryptographically signed and tagged with semantic versioning (`v1.3.2`, etc.). Pushing a release tag automatically triggers the automated [Release Pipeline](.github/workflows/release.yml) which builds, validates, QEMU-tests, packages, and attaches all assets to the GitHub Release.

```bash
# Tag and trigger a release
git tag -a v1.3.2 -m "Rain OS Version 1.3.2 Production Release"
git push origin v1.3.2
```

### Released Assets & Manifests
Every official release provides the following downloadable artifacts:
1. **`rain-os-1.3.2-x86_64.iso`**: The full bootable live distribution ISO with Calamares graphical installer, hardware drivers, KDE Plasma 6, COSMIC profile, universal boot media auto-detection, and universal app ecosystem.
2. **`rain-os-1.3.2-source.tar.gz`**: Full, auditable source code repository tree for clean offline builds and open inspection.
3. **`rain-os-packages-1.3.2.tar.gz`**: Archive containing the compiled Rain OS local package repository (`rain.db.tar.zst`) and all pre-built `.pkg.tar.zst` packages.
4. **`rain-wallpaper-4k.jpg`**: Official 4K Ultra-HD default wallpaper (3840×2160).
5. **`rain-logo-4k.png`**: High-resolution 4096×4096 transparent master umbrella emblem.
6. **`rain-umbrella.svg`**: Scalable vector master logo and desktop application icon.
7. **`rain-os-sbom.json`**: CycloneDX v1.5 Software Bill of Materials cataloging all bundled software, libraries, and open-source licenses.
8. **`SHA256SUMS` & `SHA512SUMS`**: SHA-256 and SHA-512 cryptographic hashes for verifying file integrity before flashing.

### Universal Bootloader & Bare-Metal Hardware Resilience
Rain OS 1.3.2 includes critical bare-metal compatibility hardening:
- **USB Enumeration Settle Delay (`archisodelay=15`)**: Prevents early boot timeouts on slower USB 3.0/Type-C controllers, ensuring storage devices are detected before `archiso` attempts to mount `airootfs.sfs`.
- **Pre-Discovery Storage Hook Sequence**: Enforces `block` device generation and `keyboard` availability prior to `archiso` filesystem discovery in initramfs.
- **Intel LPSS & ACPI Interrupt Protection (`irqpoll`)**: Defeats unhandled IRQ collisions (e.g. IRQ 27) that otherwise freeze USB controllers on 10th–14th Gen Intel laptop platforms.
- **Universal Flashing Compatibility**: Boots reliably via **BalenaEtcher**, Rufus in **DD Image Mode**, Rufus in **ISO Image Mode**, **Ventoy**, or direct `dd`.

### Flashing to USB
- **BalenaEtcher (Recommended)**: Select `rain-os-1.3.2-x86_64.iso` and your USB flash drive, then click Flash.
- **Rufus (Windows)**: Select the ISO, choose Partition Scheme `GPT` or `MBR`, and click Start (choose **DD Image Mode** when prompted for maximum reliability).
- **Ventoy**: Simply copy `rain-os-1.3.2-x86_64.iso` to your Ventoy USB drive.
- **Linux (`dd`)**:
  ```bash
  sudo dd if=rain-os-1.3.2-x86_64.iso of=/dev/sdX bs=4M status=progress oflag=sync
  ```

---

## Problem Audit & Advancement Roadmap

For a detailed analysis of build pipeline diagnostics, root-cause resolutions, iconography specifications, the transition to **COSMIC Desktop** as default, and the migration to `cosmic-store`, see:
- [`docs/PROBLEMS_AND_ADVANCEMENTS.md`](docs/PROBLEMS_AND_ADVANCEMENTS.md): The master technical specification and gap analysis for Rain OS production readiness.

---

## License & Provenance

Rain OS source code, scripts, and original artwork are licensed under the [GNU General Public License v3.0](LICENSE). Upstream components, kernels, firmware, and packages adhere to their respective licenses as cataloged in [`manifests/PROVENANCE_LEDGER.csv`](manifests/PROVENANCE_LEDGER.csv).
