#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
required=(
  README.md
  docs/PRD.md
  docs/TRD.md
  docs/APP_FLOW.md
  docs/DATA_MODEL.md
  docs/SECURITY_MODEL.md
  docs/LOOP_ENGINEERING.md
  docs/IMPLEMENTATION_PLAN.md
  docs/STARTING_CONCEPT.md
  docs/REUSE_STRATEGY.md
  docs/MIGRATION_PLAN.md
  docs/CROSSCHECK_AND_GAPS.md
  docs/REFERENCE_INDEX.md
  docs/SELF_UPDATING_GUIDE.md
  docs/ENVIRONMENTS.md
  docs/ENGINEERING_TOOLCHAIN.md
  docs/WORKFLOW_GOVERNANCE.md
  docs/guide-index.schema.json
  docs/guide-index.example.json
  docs/USER_LEARNING_PATH.md
  manifests/PACKAGES.md
  manifests/UPSTREAM_COMPONENTS.md
  manifests/PROVENANCE_LEDGER.csv
  manifests/BUILDER_TOOLS.csv
  manifests/FILES.md
  design/DESIGN_SYSTEM.md
  architecture/SYSTEM_ARCHITECTURE.mmd
  architecture/BUILD_PIPELINE.mmd
  qa/QA_MATRIX.md
  build/BUILD_README.md
  branding/rain-umbrella.svg
)
for file in "${required[@]}"; do
  [[ -s "$ROOT/$file" ]] || { echo "missing or empty: $file" >&2; exit 1; }
done
if command -v xmllint >/dev/null 2>&1; then xmllint --noout "$ROOT/branding/rain-umbrella.svg"; fi
if command -v grep >/dev/null 2>&1; then
  grep -q "Rain OS" "$ROOT/README.md"
  grep -qi "lts" "$ROOT/docs/TRD.md"
  grep -q "snapshot" "$ROOT/docs/LOOP_ENGINEERING.md"
fi
echo "Rain OS specification validation passed: ${#required[@]} required artifacts present."
