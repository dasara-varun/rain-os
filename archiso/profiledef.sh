#!/usr/bin/env bash
# Rain OS starter Archiso profile. Review paths and package ownership before release.
iso_name="rain-os"
iso_label="RAIN_010"
iso_publisher="Rain OS Contributors <https://github.com/dasara-varun/rain-os>"
iso_application="Rain OS live and installation environment"
iso_version="0.1.0"
install_dir="rain"
buildmodes=('iso')
bootmodes=('bios.syslinux' 'uefi-x64.systemd-boot')
arch="x86_64"
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/root"]="0:0:750"
  ["/etc/rain-os"]="0:0:755"
  ["/etc/sudoers.d"]="0:0:750"
  ["/etc/sudoers.d/g_wheel"]="0:0:440"
  ["/usr/local/bin/rain-welcome-launcher"]="0:0:755"
  ["/usr/local/bin/rain-install-launcher"]="0:0:755"
)
