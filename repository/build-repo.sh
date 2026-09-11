#!/usr/bin/env bash
# Rain OS Local Package Repository Generator
set -euo pipefail

REPO_DIR="${1:-./repository/repo}"
REPO_NAME="rain-core"

mkdir -p "$REPO_DIR"

echo "Building package repository database for '$REPO_NAME' in $REPO_DIR..."

if ! command -v repo-add >/dev/null 2>&1; then
    echo "Warning: repo-add not found. Install 'pacman' or 'base-devel'." >&2
    exit 0
fi

cd "$REPO_DIR"
shopt -s nullglob
PKGS=(*.pkg.tar.zst)

if [[ ${#PKGS[@]} -eq 0 ]]; then
    echo "No .pkg.tar.zst packages found in $REPO_DIR to index."
    exit 0
fi

repo-add -s -v "${REPO_NAME}.db.tar.gz" "${PKGS[@]}"
echo "Repository database generated successfully."
