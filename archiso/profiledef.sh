#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="rain-os"
iso_label="RAIN_121"
iso_publisher="Rain OS Contributors <https://github.com/dasara-varun/rain-os>"
iso_application="Rain OS Live & Installation Media"
iso_version="1.2.1"
install_dir="rain"
buildmodes=('iso')
bootmodes=('bios.syslinux' 'uefi.systemd-boot')
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '100%')
bootstrap_tarball_compression=('zstd' '-c' '-T0' '--auto-threads=logical' '--long' '-19')
file_permissions=(
  ["/etc/rain-os"]="0:0:755"
  ["/etc/sudoers.d"]="0:0:750"
  ["/etc/sudoers.d/g_wheel"]="0:0:440"
  ["/usr/local/bin/rain-welcome-launcher"]="0:0:755"
  ["/usr/local/bin/rain-install-launcher"]="0:0:755"
  ["/usr/local/bin/rain-live-setup"]="0:0:755"
  ["/usr/local/bin/rain-control-center"]="0:0:755"
  ["/usr/local/bin/rain-first-run"]="0:0:755"
  ["/usr/local/bin/rain-first-run-gui"]="0:0:755"
  ["/usr/local/bin/rain-btrfs-snapshot"]="0:0:755"
  ["/usr/local/bin/rain-hardware-report"]="0:0:755"
  ["/usr/local/bin/rain-guide"]="0:0:755"
  ["/usr/local/bin/rain-profile"]="0:0:755"
  ["/usr/local/bin/rain-kernel"]="0:0:755"
  ["/usr/local/bin/rain-recovery"]="0:0:755"
  ["/usr/local/bin/rain-update-preflight"]="0:0:755"
  ["/usr/local/bin/rain-probe"]="0:0:755"
  ["/usr/local/bin/rain-display-manager"]="0:0:755"
  ["/usr/local/bin/rain-install-cosmic"]="0:0:755"
  ["/usr/local/bin/rain-desktop-selector"]="0:0:755"
  ["/opt/rain"]="0:0:755"
)
