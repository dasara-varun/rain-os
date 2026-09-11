# Rain OS Technical Requirements Document

**Version:** 0.2  
**Status:** Reuse-first architecture

## 1. Architecture principle

Rain OS is an integration distribution, not a greenfield operating-system stack. The preferred implementation order is:

1. **Reuse unchanged** when the component satisfies requirements.
2. **Configure or theme** when behavior is correct but the experience is not Rain-like.
3. **Wrap** when a stable command needs a safer, clearer, or profile-aware interface.
4. **Patch upstream** when the defect benefits the original project.
5. **Fork temporarily** only when upstream timing blocks a release and the fork has an owner and exit plan.
6. **Replace** only when the component is unmaintained, incompatible, or fundamentally mismatched.

## 2. Base and ISO assembly

Use the EndeavourOS ISO/Archiso structure as the starting point after reviewing the current repository and license terms. Preserve Arch repositories and the Arch package model. Reuse the upstream installer path where possible; Rain should first add branding, defaults, profile selection, learning hooks, and post-install guidance.

The ISO consists of a Core profile, an optional Flow/Forge/Shield selection mechanism, a local documentation bundle, and a Rescue path. It must not become a collection of unrelated repositories with conflicting package priorities.

## 3. Reuse boundaries

| Capability | Preferred source | Rain responsibility |
|---|---|---|
| ISO framework and package lists | EndeavourOS/Archiso patterns | Assemble, pin, test, and document |
| Hardware detection | EndeavourOS `eos-hwtool` and/or CachyOS `chwd` after audit | Choose one canonical interface and expose a read-only Rain report |
| Mirror ranking | EndeavourOS mirror tooling where compatible | Add Rain mirror policy and diagnostics |
| Kernel performance | CachyOS kernel recipes and patches where license and support permit | Build only supported variants and retain Arch/LTS fallback |
| Performance settings | CachyOS settings ideas | Translate to explicit, reversible Rain profiles |
| Security tooling | Athena role/repository organization and documented security model | Curate, isolate, sign, and explain tools |
| Disk erasure | Athena `devotio` only if legal and tested | Place in Rescue ISO, never normal desktop |
| Installer security | Athena installer concepts and encryption workflow | Integrate only tested LUKS2/TPM/Secure Boot behavior |
| Desktop | Upstream KDE/XFCE and Arch packages | Theme, default, document |
| Learning | Rain-original content and navigation | Own and maintain |
| Control Center | Rain integration layer | Use existing commands through PolicyKit; avoid duplicating package managers |

## 4. Repository architecture

Keep the default repository set small. Use Arch repositories as the compatibility anchor. Add `rain-core` for integration packages. Add `rain-flow` and `rain-shield` only when their build provenance, signatures, and rollback behavior are established. A `rain-testing` repository uses a separate key and remains disabled by default.

Do not enable multiple performance repositories at once. Do not mix unrelated CachyOS and Athena repositories into the base system without a package-level dependency and conflict audit.

## 5. Component contract

Every reused component must have a manifest record containing upstream URL, commit or release, license, source type, local patches, build recipe, owner, test coverage, update cadence, and removal plan. A wrapper must not conceal upstream behavior. The UI should show the underlying command or package source in its help view.

## 6. Kernels

Start with upstream `linux` and `linux-lts` packages for the first Core ISO. Only then evaluate a Rain-built or CachyOS-derived Flow kernel. The minimum supported boot set is a generic kernel plus LTS fallback. A hardened kernel remains a Shield profile feature.

This reduces the initial scope and avoids maintaining a custom kernel before the distribution has hardware evidence. If a CachyOS kernel is adopted, its scheduler, patchset, compiler mode, package ABI, DKMS behavior, NVIDIA support, and fallback path must be tested as a single unit.

## 7. Installer and storage

Reuse the mature installer path selected during Phase 0. Rain adds a profile choice, a clear change review, installation report, and post-install learning handoff. Support ext4 and Btrfs, LUKS2, and documented TPM-assisted unlock only after the upstream path passes tests. Do not rewrite partitioning code in v1.

## 8. Services and defaults

Core uses NetworkManager, PipeWire/WirePlumber, power-profiles-daemon, and one firewall. AppArmor and Firejail may be installed as Shield foundations, but the UI must show whether policies are active. USBGuard remains opt-in because incorrect policies can block legitimate devices.

## 8A. Self-updating guide

The `rain-docs` package and `rain-guide` viewer are state-aware and offline-capable. A signed guide index records compatible Rain versions, checksums, signatures, pages, profiles, and desktop environments. A user-level timer may check for guide updates, but guide updates never silently install packages, change security policy, or upload telemetry. Failed signature or compatibility checks preserve the last verified bundle.

## 8B. Desktop environment support

KDE Plasma is the launch-supported default. GNOME, XFCE, and Cinnamon are supported profiles after they pass installer, update, display-manager, accessibility, suspend, audio, and guide tests. MATE, LXQt, Budgie, COSMIC, Hyprland, Sway, i3, and Niri are community or experimental profiles until owners and test coverage exist. Rain must not claim equal integration for every desktop.

## 9. Update and rollback

Reuse `pacman`, upstream keyrings, Btrfs snapshot tooling, and the selected upstream update/mirror helpers. Rain adds preflight checks, user-facing explanations, snapshot descriptions, post-update health checks, and a safe fallback workflow. It must not implement a second package transaction engine.

## 10. Build reproducibility

Use versioned Archiso profiles, upstream source references, Rain PKGBUILDs, package signatures, and a resolved manifest. Publish ISO checksums, SBOM, source revisions, and the reuse/provenance manifest. CI must build in a clean environment and record all external inputs.
