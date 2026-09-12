# Lesson 4: Running Windows Applications & Games

Rain OS provides a built-in **Windows Compatibility Bridge** directly inside the Rain Control Center.

## The Compatibility Spectrum
Rain OS is honest about compatibility:
1. **Native Linux First**: Always check if a native Linux binary or Flatpak exists (e.g. Firefox, VS Code, OBS Studio).
2. **Bottles & Wine**: Best for productivity software, utility tools, and older Windows programs. Bottles provides sandboxed 'bottles' with isolated dependencies.
3. **Steam Proton**: High-performance gaming layer with DXVK (DirectX to Vulkan) and VKD3D. Check ProtonDB for community ratings (Platinum, Gold, Silver).
4. **Quickemu / KVM Virtual Machine**: For software with kernel-level anti-cheat, Microsoft Store dependencies, or proprietary device drivers.

## Guided Practice: Launching the Compatibility Center
1. Open **Rain Control Center**.
2. Click on the **Windows Apps & Gaming** tab.
3. Review one-click installation status for Bottles, Wine, Steam, and Quickemu.
