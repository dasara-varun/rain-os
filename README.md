# Rain OS

<p align="center">
  <img src="branding/rain-logo.png" alt="Rain OS Umbrella Logo" width="160" height="160">
</p>

<p align="center">
  <strong>Shelter from complexity, without hiding the system.</strong>
</p>

<p align="center">
  <a href="https://github.com/dasara-varun/rain-os/actions/workflows/build-iso.yml"><img src="https://github.com/dasara-varun/rain-os/actions/workflows/build-iso.yml/badge.svg" alt="Build ISO"></a>
  <a href="https://github.com/dasara-varun/rain-os/actions/workflows/validate.yml"><img src="https://github.com/dasara-varun/rain-os/actions/workflows/validate.yml/badge.svg" alt="Validate Spec"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL_3.0-blue.svg" alt="License: GPL 3.0"></a>
</p>

---

## What is Rain OS?

Rain OS is an EndeavourOS/Arch Linux-derived distribution engineered around three core promises:
1. **Easy to learn**: Plain-language system explanations, offline-capable guided learning path, and graphical tools that always show their underlying terminal commands.
2. **Safe to recover**: Visible LTS fallback kernels, preflight update checks, integrated Btrfs snapshots, and a dedicated Rescue environment.
3. **Fast when hardware supports it**: Named, transparent performance profiles (Flow) with hardware capability detection, CPU gating, and instant rollback.

Rain OS operates on a strict **reuse-first strategy**: we do not invent custom package transaction engines, hardware detectors, or installers when mature upstream components exist. We curate, configure, theme, and wrap established components with Rain safety and learning layers.

---

## Repository Map

| Path | Purpose |
|---|---|
| [`archiso/`](archiso/) | Archiso profile definition, package lists, and live filesystem overlay (`airootfs`) |
| [`packages/`](packages/) | Rain-specific PKGBUILD recipes: branding, first-run, preflight, recovery, guides |
| [`scripts/`](scripts/) | Build scripts for Linux, WSL2, and Windows orchestrator |
| [`.github/workflows/`](.github/workflows/) | GitHub Actions CI for automated ISO builds and spec validation |
| [`docs/PRD.md`](docs/PRD.md) | Product requirements and user personas |
| [`docs/TRD.md`](docs/TRD.md) | Reuse-first technical architecture |
| [`docs/APP_FLOW.md`](docs/APP_FLOW.md) | Installer, onboarding, update, profile, and recovery flows |
| [`docs/IMPLEMENTATION_PLAN.md`](docs/IMPLEMENTATION_PLAN.md) | Fast-track implementation plan |
| [`docs/STARTING_CONCEPT.md`](docs/STARTING_CONCEPT.md) | Corrected first-release scope and product boundary |
| [`docs/LOOP_ENGINEERING.md`](docs/LOOP_ENGINEERING.md) | Iterative build-test-learn loop |
| [`docs/USER_LEARNING_PATH.md`](docs/USER_LEARNING_PATH.md) | Learner-facing directory and curriculum |
| [`docs/SELF_UPDATING_GUIDE.md`](docs/SELF_UPDATING_GUIDE.md) | Signed, state-aware local documentation architecture |
| [`docs/ENVIRONMENTS.md`](docs/ENVIRONMENTS.md) | Supported desktop environments (KDE default) |
| [`manifests/PACKAGES.md`](manifests/PACKAGES.md) | Package groups and provenance boundaries |
| [`manifests/UPSTREAM_COMPONENTS.md`](manifests/UPSTREAM_COMPONENTS.md) | Component-by-component reuse matrix |
| [`manifests/PROVENANCE_LEDGER.csv`](manifests/PROVENANCE_LEDGER.csv) | Full upstream source and license ledger |
| [`manifests/FILES.md`](manifests/FILES.md) | Target filesystem and source tree specification |
| [`design/DESIGN_SYSTEM.md`](design/DESIGN_SYSTEM.md) | Umbrella identity, themes (Urban & Rural Rain), palette tokens |
| [`qa/QA_MATRIX.md`](qa/QA_MATRIX.md) | Release-blocking test definitions |

---

## How to Build Rain OS

### Option 1: Automated Cloud Build (GitHub Actions)
Every push to `main` triggers `.github/workflows/build-iso.yml`. The workflow builds the bootable Archiso live ISO inside a clean container, calculates SHA256 checksums, and publishes the `.iso` file under the GitHub repository's **Actions / Releases** tab for download.

### Option 2: Local Build on Windows (WSL2 / Container)
Because `mkarchiso` requires a Linux kernel for loop devices (`/dev/loop*`), squashfs compression, and POSIX permissions, building locally on Windows is automated through our PowerShell script:

1. Open PowerShell as Administrator.
2. Run the Windows builder script:
   ```powershell
   .\scripts\build-windows.ps1
   ```
3. The script verifies or installs WSL2 with Arch Linux, passes the repository, and executes `mkarchiso`.
4. Output ISO will be generated in `out/rain-os-*.iso`.

### Option 3: Local Build on Linux (Arch Linux / Archiso Host)
On an Arch Linux build host or VM:

```bash
# 1. Install prerequisites
sudo pacman -S --needed archiso git base-devel

# 2. Validate specification integrity
./scripts/validate-spec.sh

# 3. Build the ISO
sudo ./scripts/build-iso.sh

# 4. Check generated ISO
ls -lh out/*.iso
sha256sum out/*.iso > out/SHA256SUMS
```

---

## Profile Architecture

- **Rain Core (Milestone L0/L1)**: Stable, calm desktop (KDE Plasma), Arch generic + LTS fallback kernels, firewall active, offline learning hub, and safe update preflight.
- **Rain Flow**: Opt-in performance profile, tuned kernel, power/thermal management, GPU gating.
- **Rain Forge**: Developer workstation profile, container runtimes, compilers, and toolchains.
- **Rain Shield**: Isolated security profile, AppArmor profiles, sandbox monitoring, strictly educational/authorized security tooling.

---

## License & Provenance

Rain OS source code and scripts are licensed under the [GNU General Public License v3.0](LICENSE). Reused components, fonts, wallpapers, and package recipes adhere to their respective upstream licenses as tracked in [`manifests/PROVENANCE_LEDGER.csv`](manifests/PROVENANCE_LEDGER.csv).
