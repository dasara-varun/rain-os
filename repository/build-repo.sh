#!/usr/bin/env bash
# Rain OS Local Package Repository Generator & Builder
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO_DIR="${1:-$ROOT/repository/repo}"
REPO_NAME="rain"

mkdir -p "$REPO_DIR"

echo "=========================================================="
echo "Rain OS Package Repository Builder"
echo "Target Repository Directory: $REPO_DIR"
echo "=========================================================="

# 1. Build all packages in packages/ if makepkg is present
if command -v makepkg >/dev/null 2>&1; then
    if [[ "${EUID}" -eq 0 ]]; then
        id -u builduser >/dev/null 2>&1 || useradd -m -d /home/builduser builduser
        chown -R builduser:builduser "$ROOT/packages" "$REPO_DIR"
    fi

    for pkg_dir in "$ROOT"/packages/*; do
        if [[ -d "$pkg_dir" && -f "$pkg_dir/PKGBUILD" ]]; then
            pkg_basename="$(basename "$pkg_dir")"
            echo "--- Building package: $pkg_basename ---"
            (
                cd "$pkg_dir"
                if [[ "${EUID}" -eq 0 ]]; then
                    su - builduser -c "cd '$pkg_dir' && makepkg -f --nodeps --skipchecksums --skippgpcheck" || true
                else
                    makepkg -f --nodeps --skipchecksums --skippgpcheck || true
                fi
                cp -v ./*.pkg.tar.zst "$REPO_DIR/" 2>/dev/null || true
            )
        fi
    done
else
    echo "Notice: makepkg not available in current environment; skipping compilation step."
fi

# 2. Index packages with repo-add
if command -v repo-add >/dev/null 2>&1; then
    cd "$REPO_DIR"
    shopt -s nullglob
    PKGS=(*.pkg.tar.zst)

    if [[ ${#PKGS[@]} -gt 0 ]]; then
        echo "Indexing ${#PKGS[@]} package(s) into ${REPO_NAME}.db.tar.zst..."
        repo-add -n -R "${REPO_NAME}.db.tar.zst" "${PKGS[@]}"
        echo "Repository database successfully created."
    else
        echo "No packages found in $REPO_DIR to index."
    fi
else
    echo "Notice: repo-add not found. Install 'pacman' or 'base-devel' on Linux build host."
fi

echo "Repository build step completed."
