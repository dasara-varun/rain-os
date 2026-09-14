# Rain OS Roadmap & Technical Advancements

Rain OS **v1.3.0 Production Baseline** delivers key architectural milestones for usability, performance, and aesthetic elegance:

## 1. Flagship Desktop: COSMIC Desktop
- Modern Rust-based COSMIC desktop environment configured as the flagship default session.
- Sub-300MB idle memory consumption, native Wayland auto-tiling, and fluid fractional scaling.
- Seamless coexistence with Hyprland, KDE Plasma 6, GNOME, i3-wm, Sway, and XFCE 4.

## 2. Vertical Installer Desktop Selection
- Window Manager and Desktop Environment selection is embedded directly inside the installation wizard.
- Formatted as a clean, scrollable vertical list with COSMIC Desktop pre-selected as flagship default #1.

## 3. Modern App Center: `cosmic-store`
- Completely replaced KDE Discover with `cosmic-store`.
- Instant startup, native package and Flathub Flatpak integration out of the box, and zero pacman database lock contention.

## 4. Distinct Custom Application Iconography
- Dedicated, high-contrast vector-derived application icons across all 8 custom Rain OS tools: Control Center, Installer, Welcome GUI, Learning Hub, Desktop Selector, App Store, Hardware Wizard, and Display Assistant.

## 5. Clean Live Boot Surface
- Intrusive boot popup windows suppressed.
- Live desktop contains strictly two essential entry points: **Install Rain OS to Disk** and **Rain Learning Hub**.

## 6. Future Roadmap (v1.4.0)
- Native Wayland HDR color calibration for OLED/Mini-LED displays.
- Hardware battery charge threshold controller for ThinkPad, ASUS, and Dell laptops.
- Pre-built gaming container profiles and one-click emulator provisioning.

For the complete technical specification, consult `/usr/share/doc/rain-os/PROBLEMS_AND_ADVANCEMENTS.md`.
