# Contributing to Rain OS

Thank you for your interest in contributing to Rain OS! Rain OS is designed around three promises: **easy to learn, safe to recover, and fast when the hardware supports it**.

We follow a **reuse-first strategy**: before writing custom tools or forking upstream software, we assemble and configure mature upstream components from Arch Linux, EndeavourOS, and CachyOS.

---

## 1. Development Principles

1. **Compatible before optimized**: Never trade stability, hardware compatibility, or boot success for speculative performance gains.
2. **Understandable before clever**: System tools, error messages, and scripts must use plain language, explain what changed, and provide next steps.
3. **Recoverable before experimental**: Every new feature, kernel option, or profile must have an explicit rollback and uninstallation path.
4. **Private by default**: No mandatory cloud account, no telemetry, and local diagnostics must be scrubbed of secrets before sharing.
5. **Strict Provenance**: Every reused script, package recipe, or patch must be logged in `manifests/PROVENANCE_LEDGER.csv` with license and source URL.

---

## 2. Repository Structure

```text
rain-os/
├── archiso/            # Profile definition, package lists, and live filesystem overlay
├── packages/           # Rain-specific PKGBUILD recipes (branding, first-run, recovery)
├── docs/               # Architecture, PRD, TRD, and guide documentation
├── manifests/          # Component reuse matrix, packages, builder tools, provenance
├── scripts/            # Build automation for Linux/WSL and Windows
├── .github/workflows/  # Automated GitHub Actions ISO build CI
└── Makefile            # Common developer targets
```

---

## 3. Getting Started

### Local Build on Linux / WSL2
Building the bootable ISO requires an Arch Linux environment with root/loop-mount privileges:

```bash
# Check specification requirements
./scripts/validate-spec.sh

# Build the ISO (requires archiso installed)
sudo ./scripts/build-iso.sh
```

### Local Build on Windows
Run the PowerShell builder script:
```powershell
.\scripts\build-windows.ps1
```

---

## 4. Git & Commit Guidelines

- Use [Conventional Commits](https://www.conventionalcommits.org/):
  - `feat:` for new features or capabilities
  - `fix:` for bug fixes
  - `docs:` for documentation updates
  - `refactor:` for code cleanups
  - `ci:` for CI/CD workflow updates
  - `chore:` for general maintenance
- Keep commits atomic and test before pushing.
- All contributions are licensed under the GNU General Public License v3.0.
