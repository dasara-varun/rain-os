# Lesson 6: Software App Store & Package Management

Rain OS provides multiple flexible ways to install software without hassle.

## Choosing the Right Source
1. **Rain App Store (COSMIC Store)**: The modern Rust-based graphical Software Center. Fast, lightweight, and pre-configured for both native packages and sandboxed Flatpaks.
2. **Flatpaks & Flathub**: Sandboxed applications that run independently of system libraries. Ideal for Spotify, Discord, Telegram, and proprietary software.
3. **AppImages**: Single-file executables. Rain OS has `fuse2` pre-installed, so AppImages run immediately on double-click.
4. **Pacman (Terminal)**: Fast, native Arch Linux package management:
   ```bash
   sudo pacman -S gimp vlc
   ```

## Guided Practice: Adding Flathub
To enable thousands of Flatpak applications:
```bash
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```
Once added, Flathub applications will appear directly inside the Rain App Store!

