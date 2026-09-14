#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/out"
PROFILE="$ROOT/archiso"

mkdir -p "$OUT"

if [[ "${EUID}" -ne 0 ]]; then
  echo "Error: Must be run as root (or via sudo) on an Arch Linux build host." >&2
  echo "See build/BUILD_README.md for prerequisites and build guidelines." >&2
  exit 1
fi

if ! command -v mkarchiso >/dev/null 2>&1; then
  echo "Error: mkarchiso not found. Please install archiso: sudo pacman -S archiso" >&2
  exit 1
fi

if [[ ! -d "$PROFILE" || ! -s "$PROFILE/packages.x86_64" ]]; then
  echo "Error: archiso profile is not initialized at $PROFILE." >&2
  exit 1
fi

# Compile native C probe if make is available
if command -v make >/dev/null 2>&1 && [[ -d "$ROOT/src" ]]; then
  echo "Compiling native C probe..."
  make -C "$ROOT/src" install DESTDIR="$PROFILE/airootfs" PREFIX=/usr/local || true
fi

# Build custom packages repository if not yet built
if [[ -x "$ROOT/repository/build-repo.sh" && ! -f "$ROOT/repository/rain-repo/rain-os.db.tar.gz" ]]; then
  echo "Building custom Rain OS repository packages..."
  "$ROOT/repository/build-repo.sh" || true
fi

# Ensure loop device control exists (essential inside containers & CI runners)
if [[ ! -c /dev/loop-control ]]; then
  mknod /dev/loop-control c 10 237 2>/dev/null || true
fi
for i in $(seq 0 15); do
  if [[ ! -b "/dev/loop$i" ]]; then
    mknod "/dev/loop$i" b 7 "$i" 2>/dev/null || true
  fi
done

echo "=========================================================="
echo "Preparing Rain OS airootfs configuration & services..."
AIROOTFS="$PROFILE/airootfs"
mkdir -p "$AIROOTFS/etc/systemd/system/graphical.target.wants"
mkdir -p "$AIROOTFS/etc/systemd/system/multi-user.target.wants"
mkdir -p "$AIROOTFS/etc/systemd/system/basic.target.wants"

# Mask systemd-firstboot so boot never halts on console for timezone/locale
ln -sf /dev/null "$AIROOTFS/etc/systemd/system/systemd-firstboot.service"

# Pre-link timezone to UTC
ln -sf /usr/share/zoneinfo/UTC "$AIROOTFS/etc/localtime"

# Set default target to graphical desktop
ln -sf /usr/lib/systemd/system/graphical.target "$AIROOTFS/etc/systemd/system/default.target"

# Link SDDM display manager
ln -sf /usr/lib/systemd/system/sddm.service "$AIROOTFS/etc/systemd/system/display-manager.service"
ln -sf /usr/lib/systemd/system/sddm.service "$AIROOTFS/etc/systemd/system/graphical.target.wants/sddm.service"

# Enable NetworkManager
ln -sf /usr/lib/systemd/system/NetworkManager.service "$AIROOTFS/etc/systemd/system/multi-user.target.wants/NetworkManager.service"

# Enable Bluetooth
ln -sf /usr/lib/systemd/system/bluetooth.service "$AIROOTFS/etc/systemd/system/multi-user.target.wants/bluetooth.service"

# Enable Power Profiles Daemon
ln -sf /usr/lib/systemd/system/power-profiles-daemon.service "$AIROOTFS/etc/systemd/system/multi-user.target.wants/power-profiles-daemon.service"

# Enable Avahi mDNS Daemon
ln -sf /usr/lib/systemd/system/avahi-daemon.service "$AIROOTFS/etc/systemd/system/multi-user.target.wants/avahi-daemon.service"

# Enable rain-live-setup in basic.target
ln -sf /etc/systemd/system/rain-live-setup.service "$AIROOTFS/etc/systemd/system/basic.target.wants/rain-live-setup.service"

# Remove legacy/conflicting units
rm -rf "$AIROOTFS/etc/systemd/system/getty@tty1.service.d" 2>/dev/null || true
rm -f "$AIROOTFS/etc/systemd/system/multi-user.target.wants/display-manager.service" 2>/dev/null || true

# Ensure permissions
chmod 755 "$AIROOTFS/usr/local/bin"/* 2>/dev/null || true
chmod 755 "$AIROOTFS/etc/skel/Desktop"/*.desktop 2>/dev/null || true
chmod 750 "$AIROOTFS/etc/sudoers.d" 2>/dev/null || true
chmod 440 "$AIROOTFS/etc/sudoers.d"/* 2>/dev/null || true

echo "Starting Rain OS Archiso build..."
echo "Profile directory: $PROFILE"
echo "Output directory : $OUT"
echo "=========================================================="

mkarchiso -v -w "$OUT/work" -o "$OUT" -C "$PROFILE/pacman.conf" "$PROFILE"

echo "=========================================================="
echo "ISO build completed successfully!"
echo "Generating SHA256 checksums..."
cd "$OUT"
sha256sum rain-os-*.iso > SHA256SUMS 2>/dev/null || true
echo "Checksum written to $OUT/SHA256SUMS"
ls -lh rain-os-*.iso
echo "=========================================================="
