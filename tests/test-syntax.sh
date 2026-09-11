#!/usr/bin/env bash
# Rain OS Syntax and Integrity Tests
set -euo pipefail

echo "Running Shell script syntax checks..."
for sh in scripts/*.sh repository/*.sh packages/*/*/* packages/*/bin/*; do
    if [[ -f "$sh" ]]; then
        bash -n "$sh" || { echo "Syntax error in $sh" >&2; exit 1; }
        echo "  [OK] $sh"
    fi
done

echo "Running JSON validation checks..."
for j in docs/*.json archiso/airootfs/etc/rain-os/*.json; do
    if [[ -f "$j" ]]; then
        python -m json.tool "$j" >/dev/null || { echo "JSON error in $j" >&2; exit 1; }
        echo "  [OK] $j"
    fi
done

echo "All syntax and JSON checks passed!"
