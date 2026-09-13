# Rain OS Roadmap & Technical Advancements

Rain OS is advancing towards its v1.3.0 production baseline with significant enhancements designed to elevate usability, performance, and aesthetics:

## 1. Flagship Desktop: COSMIC Desktop
- Transitioning to System76's modern Rust-based COSMIC desktop environment as the default session.
- Sub-300MB idle memory consumption, native Wayland auto-tiling, and fluid fractional scaling.
- Seamless co-existence with KDE Plasma 6, Hyprland, and i3 via `rain-desktop-selector`.

## 2. Next-Generation App Center: COSMIC Store
- Replacing KDE Discover with `cosmic-store`.
- Instant sub-second startup, Flathub Flatpak integration out-of-the-box, and zero pacman database lock contention.

## 3. Dedicated Application Iconography
- Introducing 8 distinct, high-contrast application icons for the Control Center, Installer, Welcome Assistant, Learning Hub, Desktop Selector, App Store, Hardware Wizard, and Display Assistant.

## 4. Universal 4K Wallpapers & Bootsplash
- Universal wallpaper parity across Plymouth bootsplash, SDDM login greeter, and lockscreen featuring the 12 curated 4K anime rain wallpapers.

For the complete technical specification, consult `/usr/share/doc/rain-os/PROBLEMS_AND_ADVANCEMENTS.md`.
