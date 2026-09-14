# Lesson 5: Hardware Detection & Drivers

Rain OS automatically detects your graphics cards, wireless network adapters, and power configuration.

## Graphics Architecture
- **Intel & AMD**: Fully open-source in-kernel drivers (`amdgpu` and `i915`/`xe`) with Mesa Vulkan support out of the box.
- **NVIDIA**: Supported via proprietary `nvidia`/`nvidia-dkms` or open-source `nouveau`. Hybrid laptops can offload games with `prime-run`.

## Guided Practice: Running the Hardware Assistant
In the terminal, run:
```bash
rain-hardware-report
```
This command will:
- Detect your GPU vendor and confirm Vulkan acceleration drivers.
- Identify your Wi-Fi card (Intel, Realtek, or Broadcom wl).
- Report active power profile (Power Saver, Balanced, Performance).

To switch power profiles on laptops:
```bash
powerprofilesctl set performance
powerprofilesctl set power-saver
```

## CPU Microcode & Thermal Errata Protection
Rain OS pre-installs `amd-ucode` and `intel-ucode` directly in the bootloader configuration. The kernel applies processor microcode patches before mounting rootfs, ensuring optimal thermal behavior, hardware stability, and silicon errata mitigation.

## Printing & Hardware Peripherals
The CUPS printing stack (`cups.service`) is enabled by default. Add network or USB printers using **Print Settings** (`system-config-printer`) or the browser interface at `http://localhost:631`.
