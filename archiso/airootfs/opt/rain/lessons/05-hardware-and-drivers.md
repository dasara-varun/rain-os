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
