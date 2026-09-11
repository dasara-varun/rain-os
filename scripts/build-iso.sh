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

echo "=========================================================="
echo "Starting Rain OS Archiso build..."
echo "Profile directory: $PROFILE"
echo "Output directory : $OUT"
echo "=========================================================="

mkarchiso -v -w "$OUT/work" -o "$OUT" "$PROFILE"

echo "=========================================================="
echo "ISO build completed successfully!"
echo "Generating SHA256 checksums..."
cd "$OUT"
sha256sum rain-os-*.iso > SHA256SUMS 2>/dev/null || true
echo "Checksum written to $OUT/SHA256SUMS"
ls -lh rain-os-*.iso
echo "=========================================================="
