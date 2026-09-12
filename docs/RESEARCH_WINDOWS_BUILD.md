# Verified Research Notes: Windows Local ISO Build

## Sources reviewed

- ArchWiki Archiso: https://wiki.archlinux.org/title/Archiso
- Archiso profile documentation: https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/docs/README.profile.rst
- Microsoft WSL install: https://learn.microsoft.com/en-us/windows/wsl/install
- Arch Linux on WSL: https://wiki.archlinux.org/title/Install_Arch_Linux_on_WSL
- Claude Code setup: https://code.claude.com/docs/en/setup
- Claude Code Desktop in WSL: https://code.claude.com/docs/en/desktop-wsl

## Findings

Archiso is an Arch Linux tool for building ISO, netboot, and bootstrap artifacts. The official guidance says to install `archiso`, use a profile directory, list packages one per line in `packages.x86_64`, place image files under `airootfs`, and invoke `mkarchiso` with the profile directory. It documents a work directory, output directory, QEMU testing, and a requirement for `mkinitcpio` and `mkinitcpio-archiso` in ISO profiles.

Microsoft documents WSL2 as a Windows-hosted Linux environment and supports installing distributions with `wsl --install`. ArchWiki documents an official Arch WSL image and states that WSL2 is required for it. WSL2 is suitable for the Linux build toolchain, but it does not replace testing the generated ISO in a real VM or on hardware.

The Claude Code setup documentation supports native Windows and WSL2. For a Linux-targeting project, WSL2 is the preferred location because Linux tools run natively inside the distribution. Claude’s WSL desktop guidance says repositories should live inside the WSL filesystem rather than under `/mnt/c` for better performance and file watching. The WSL desktop session currently has some feature limitations, including connectors/plugins and integrated terminal, so a WSL terminal/CLI fallback remains necessary.

The correct Rain OS design is therefore: Windows host, WSL2 Arch build distribution, project under `/home/<user>/rain-os`, Linux-native builder tools, local output copied to Windows only after build, QEMU/Hyper-V or VirtualBox for ISO boot tests, and physical USB/hardware testing as a later gate.
