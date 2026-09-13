#!/usr/bin/env bash
# Rain OS Syntax and Integrity Tests
set -euo pipefail

echo "Running script syntax checks..."
for f in scripts/*.sh scripts/*.py repository/*.sh packages/*/*/* packages/*/bin/* apps/*/*.py archiso/airootfs/usr/local/bin/*; do
    if [[ -f "$f" ]]; then
        first_line="$(head -n 1 "$f" 2>/dev/null || true)"
        if [[ "$first_line" =~ ^#\!.*python || "$f" =~ \.py$ ]]; then
            python -m py_compile "$f" || { echo "Python syntax error in $f" >&2; exit 1; }
            echo "  [OK (py)] $f"
        elif [[ "$first_line" =~ ^#\!.*(ba)?sh || "$f" =~ \.sh$ ]]; then
            bash -n "$f" || { echo "Bash syntax error in $f" >&2; exit 1; }
            echo "  [OK (sh)] $f"
        fi
    fi
done

echo "Running JSON validation checks..."
for j in docs/*.json archiso/airootfs/etc/rain-os/*.json archiso/airootfs/opt/rain/docs/*.json; do
    if [[ -f "$j" ]]; then
        python -m json.tool "$j" >/dev/null || { echo "JSON error in $j" >&2; exit 1; }
        echo "  [OK] $j"
    fi
done

echo "All syntax and JSON checks passed!"
