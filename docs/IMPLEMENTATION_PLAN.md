# Rain OS Reuse-First Implementation Plan

## Phase 0: audit and legal gate

Fork or vendor only the minimum Archiso and configuration material needed to build an experimental ISO. Inventory the current EndeavourOS, CachyOS, and Athena components under consideration. Record licenses, upstream versions, repositories, maintainers, and known integration constraints.

**Deliverable:** completed `manifests/UPSTREAM_COMPONENTS.md`, provenance checklist, component owners, and a clean experimental branch.

## Phase 1: assemble upstream Core

Use the existing EndeavourOS/Archiso build layout as the starting point. Reuse upstream installer, mirror, hardware, boot, desktop, and package mechanisms. Change only branding, package selection, default configuration, profile labels, local documentation, and Rain metadata.

**Deliverable:** Core ISO that boots and installs in a UEFI VM without Rain-specific forks of low-level tools.

## Phase 2: add Rain integration wrappers

Implement Rain Welcome, Learning Hub, hardware report, safe update preflight, profile manager, and recovery links as thin clients over existing commands and services. Every wrapper must expose its underlying command and fail safely if the upstream tool changes.

**Deliverable:** a first-run user can understand and complete installation, update, package installation, and help workflows.

## Phase 3: recovery before optimization

Reuse upstream Btrfs/snapshot, LUKS2, bootloader, and rescue utilities. Add Rain-specific diagnostics, snapshot descriptions, and a recovery runbook. Test broken package transactions and boot entries.

**Deliverable:** Core can recover from deliberate failures without a reinstall.

## Phase 4: adopt selected CachyOS performance components

Evaluate CachyOS kernel/package/settings repositories as source inputs. Start with one Flow kernel and a small settings profile. Use CPU detection and explicit opt-in. Retain generic and LTS fallbacks. Do not import an entire optimized repository before package conflicts and instruction-set behavior are tested.

**Deliverable:** Flow can be enabled, benchmarked, disabled, and rolled back.

## Phase 5: adopt selected Athena security components

Reuse Athena’s documented role-based organization and security-state communication. Integrate only tools with clear source, licensing, maintenance, and isolation decisions. Place risky or large collections in containers or a dedicated Shield environment. Consider `devotio` for Rescue only after direct audit and testing.

**Deliverable:** Shield adds security capability without weakening Core or pretending that installed tools equal protection.

## Phase 6: optimize only proven Rain gaps

Fork or write new code only for integration problems that upstream tools cannot solve. Contribute generic fixes upstream where possible. Keep local forks small, documented, and time-limited.

**Deliverable:** every Rain-owned line of code has an owner, tests, and a reason it cannot be upstreamed.

## Phase 7: release hardening

Run the hardware, accessibility, installer, recovery, security, update, provenance, and reproducibility matrices. Publish source links, package manifests, license notices, checksums, SBOM, known issues, and recovery instructions.

## Fast-track order

The fastest credible path is: **assemble Core → boot/install → add learning → add recovery → add thin integration wrappers → add Flow → add Forge → add Shield**. Do not start by rebuilding a kernel or writing a new installer.
