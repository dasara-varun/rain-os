#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/out"
WORK="$OUT/work"
PROFILE="$WORK/profile"
LOG="$OUT/build.log"

fail() { echo "Rain OS build failed: $*" >&2; exit 1; }
trap 'echo "Build stopped at line $LINENO. See $LOG" >&2' ERR

[[ "$(uname -s)" == "Linux" ]] || fail "run this script inside WSL2 or Linux, not PowerShell"
[[ "$ROOT" != /mnt/* ]] || fail "move the repository into the WSL filesystem, for example ~/src/rain-os"
command -v sudo >/dev/null || fail "sudo is required"
command -v pacman >/dev/null || fail "pacman is required; use the official Arch WSL distribution"

mkdir -p "$OUT"
exec > >(tee "$LOG") 2>&1

echo "[1/7] Installing build dependencies"
sudo pacman -Syu --needed --noconfirm git base-devel archiso qemu-desktop edk2-ovmf rsync jq shellcheck

command -v mkarchiso >/dev/null || fail "mkarchiso was not installed"
[[ -d /usr/share/archiso/configs/releng ]] || fail "installed archiso releng profile not found"

rm -rf "$WORK"
mkdir -p "$WORK"
echo "[2/7] Copying the current Archiso releng profile"
cp -a /usr/share/archiso/configs/releng "$PROFILE"

# The stock releng profile supplies mandatory boot files, pacman.conf,
# mkinitcpio-archiso, and airootfs defaults. Rain adds its package list and
# metadata without replacing the low-level Archiso machinery.
echo "[3/7] Overlaying Rain package selection and metadata"
cat "$PROFILE/packages.x86_64" "$ROOT/archiso/packages.x86_64" | sed '/^[[:space:]]*#/d;/^[[:space:]]*$/d' | sort -u > "$PROFILE/packages.x86_64"
cp "$ROOT/archiso/profiledef.sh" "$PROFILE/profiledef.sh"
mkdir -p "$PROFILE/airootfs/etc/rain-os" "$PROFILE/airootfs/usr/share/doc/rain-os"
printf '%s\n' '{"distribution":"Rain OS","channel":"core","build":"one-shot","guide":"bundled-after-package-implementation"}' > "$PROFILE/airootfs/etc/rain-os/release.json"
cp "$ROOT/README.md" "$PROFILE/airootfs/usr/share/doc/rain-os/README.md"

# Avoid shipping unimplemented Rain package names. They are added when the
# local Rain repository is built and signed.
grep -v '^rain-' "$PROFILE/packages.x86_64" | grep -v '^linux-rain' > "$PROFILE/packages.x86_64.tmp"
mv "$PROFILE/packages.x86_64.tmp" "$PROFILE/packages.x86_64"

echo "[4/7] Validating the profile"
grep -q '^mkinitcpio-archiso$' "$PROFILE/packages.x86_64" || echo 'mkinitcpio-archiso' >> "$PROFILE/packages.x86_64"
grep -q '^mkinitcpio$' "$PROFILE/packages.x86_64" || echo 'mkinitcpio' >> "$PROFILE/packages.x86_64"

rm -rf "$OUT/iso" "$OUT/iso-work"
mkdir -p "$OUT/iso"
echo "[5/7] Building ISO with mkarchiso"
sudo mkarchiso -v -w "$OUT/iso-work" -o "$OUT/iso" "$PROFILE"

ISO="$(find "$OUT/iso" -maxdepth 1 -type f -name '*.iso' -print -quit)"
[[ -n "$ISO" ]] || fail "mkarchiso completed without producing an ISO"

echo "[6/7] Generating release metadata"
sudo chown -R "$(id -u):$(id -g)" "$OUT"
sha256sum "$ISO" > "$OUT/SHA256SUMS"
pacman -Qq > "$OUT/host-package-list.txt" || true
printf 'ISO=%s\nBUILT_FROM=%s\n' "$ISO" "$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo uncommitted)" > "$OUT/build-metadata.txt"

echo "[7/7] Complete"
echo "ISO: $ISO"
echo "Checksum: $OUT/SHA256SUMS"
echo "Next: boot the ISO in QEMU/Hyper-V before writing USB media."
