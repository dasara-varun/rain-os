#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="rain-os"
iso_label="RAIN_010"
iso_publisher="Rain OS Contributors <https://github.com/dasara-varun/rain-os>"
iso_application="Rain OS Live & Installation Media"
iso_version="0.1.0"
install_dir="rain"
buildmodes=('iso')
bootmodes=('bios.syslinux' 'uefi.systemd-boot')
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'zstd')
bootstrap_tarball_compression=('zstd' '-c' '-T0' '--auto-threads=logical' '--long' '-19')
file_permissions=(
  ["/etc/rain-os"]="0:0:755"
  ["/etc/sudoers.d"]="0:0:750"
  ["/etc/sudoers.d/g_wheel"]="0:0:440"
  ["/usr/local/bin/rain-welcome-launcher"]="0:0:755"
  ["/usr/local/bin/rain-install-launcher"]="0:0:755"
  ["/usr/local/bin/rain-live-setup"]="0:0:755"
  ["/usr/local/bin/rain-control-center"]="0:0:755"
  ["/usr/local/bin/rain-first-run-gui"]="0:0:755"
)
