# Rain OS Upstream Component Reuse Matrix

This matrix identifies the fastest responsible path. Each row remains conditional on a license, version, compatibility, and maintainer audit.

| Component | Candidate upstream | Action | Rain delta | Gate |
|---|---|---|---|---|
| ISO build | Archiso plus current EndeavourOS ISO structure | Reuse/adapt | Rain profile, package list, branding | Build and license audit |
| Installer | Current EndeavourOS installer path; compare Athena installer work | Reuse/adapt | Rain copy, profile selection, report | Install matrix |
| Hardware | EndeavourOS `eos-hwtool`; CachyOS `chwd` | Select one, wrap | Read-only recommendation API | Package conflict and device tests |
| Mirror selection | EndeavourOS mirror tools | Reuse | Rain mirror health display | Network failure tests |
| Package manager | Arch `pacman` | Reuse unchanged | Preflight and explanation layer | Transaction and key tests |
| AUR helper | `yay` or another supported helper | Do not hard-depend in Core | Document optional use | Supply-chain warning |
| Generic kernel | Arch `linux` and `linux-lts` | Reuse initially | Rain boot labels and retention | Boot matrix |
| Performance kernel | CachyOS kernel recipes/source | Adapt later | One Rain Flow package | ABI, DKMS, GPU, benchmark tests |
| Optimized packages | CachyOS PKGBUILDs/repositories | Selective reuse later | Hardware gating and fallback | CPU compatibility tests |
| Settings | CachyOS Settings | Reuse ideas/config selectively | Rain profile toggles | Reversibility and diff audit |
| Security roles | Athena role taxonomy and docs | Adapt | Shield package groups and lessons | Safety/provenance review |
| Security repo | Athena/BlackArch-style sources | Do not enable in Core | Isolated curated bundles | Supply-chain and maintenance audit |
| Full-disk encryption | Athena documented LUKS2 flow plus upstream tools | Reuse/adapt | Installer explanation and recovery key | Hardware and recovery tests |
| Secure Boot/UKI | Athena design plus systemd tooling | Adapt later | Rain-supported signing path | Firmware matrix |
| Disk erasure | Athena `devotio` | Rescue-only candidate | Rain warning and confirmation | Legal, device, and destructive-action tests |
| Sandboxing | Firejail/AppArmor | Reuse upstream | Shield profiles and UI status | Policy coverage tests |
| Desktop | KDE/XFCE upstream | Reuse | Rain defaults and themes | Accessibility |
| Documentation | Existing project docs as references | Do not copy text wholesale | Rain-owned learning path | Attribution and maintenance |

## Decision labels

**Reuse** means Rain consumes the upstream component without source changes. **Adapt** means Rain adds configuration, packaging, or a thin integration layer. **Fork** means a temporary source fork with a sunset plan. **Replace** means the upstream component is not suitable and a new alternative is justified.

## Required manifest fields for implementation

Every adopted item must add: upstream URL, exact release/commit, license, package name, local patch list, source owner, build command, security review, test cases, update cadence, and exit/removal plan.
