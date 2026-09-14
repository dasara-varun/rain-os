# Rain OS Roadmap & Technical Advancements

Rain OS **v1.3.2 Daily-Driver Baseline** delivers key architectural milestones for usability, performance, and hardware stability:

## 1. Flagship Desktop: COSMIC Desktop
- Modern Rust-based COSMIC desktop environment configured as the flagship default session.
- Sub-300MB idle memory consumption, native Wayland auto-tiling, and fluid fractional scaling.
- Seamless coexistence with Hyprland, KDE Plasma 6, GNOME, i3-wm, Sway, and XFCE 4.

## 2. Full Daily-Driver Hardware & System Stack
- **System Administration**: Full out-of-the-box `sudo` integration with `%wheel` administrative rights.
- **Hardware Stability**: Pre-installed Intel & AMD CPU microcode packages (`intel-ucode`, `amd-ucode`) for errata and thermal fixes.
- **Bootloader & Storage**: Pre-installed `grub`, `efibootmgr`, and `os-prober` for UEFI/BIOS disk installs with dual-boot detection.
- **Printing Subsystem**: Integrated CUPS printing stack (`cups`, `cups-pdf`, `system-config-printer`).
- **Wayland Portals**: Comprehensive XDG portal suite (`xdg-desktop-portal-kde`, `gtk`) for Wayland screen sharing and Flatpaks.
- **Calamares Target Automation**: Automated target chroot configuration applying user's selected desktop environment, regenerating initramfs, and configuring user accounts.
- **Single Monolithic ISO**: Guaranteed single bootable `.iso` image output without segment splitting.

## 3. Vertical Installer Desktop Selection
- Window Manager and Desktop Environment selection is embedded directly inside the installation wizard.
- Formatted as a clean, scrollable vertical list with COSMIC Desktop pre-selected as flagship default #1.

## 4. Modern App Center: `cosmic-store`
- Completely replaced KDE Discover with `cosmic-store`.
- Instant startup, native package and Flathub Flatpak integration out of the box, and zero pacman database lock contention.

## 5. Distinct Custom Application Iconography
- Dedicated, high-contrast vector-derived application icons across all 8 custom Rain OS tools: Control Center, Installer, Welcome GUI, Learning Hub, Desktop Selector, App Store, Hardware Wizard, and Display Assistant.

## 6. Clean Live Boot Surface
- Intrusive boot popup windows suppressed.
- Live desktop contains strictly two essential entry points: **Install Rain OS to Disk** and **Rain Learning Hub**.

## 7. Future Roadmap (v1.4.0)
- Native Wayland HDR color calibration for OLED/Mini-LED displays.
- Hardware battery charge threshold controller for ThinkPad, ASUS, and Dell laptops.
- Pre-built gaming container profiles and one-click emulator provisioning.

For the complete technical specification, consult `/usr/share/doc/rain-os/PROBLEMS_AND_ADVANCEMENTS.md`.
