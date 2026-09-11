# Rain OS Product Requirements Document

**Version:** 0.1  
**Status:** Proposed  
**Product owner:** Rain OS maintainers  
**Target:** First public bootable ISO

## 1. Product definition

Rain OS is a rolling, Arch-compatible Linux distribution based on an EndeavourOS-style foundation. Its first release is a Core desktop focused on learnability, recovery, and transparent maintenance. Specialized performance and security capabilities arrive as profiles after the Core is reliable.

The product differentiator is **guided adaptability**. Users start with a calm Core system and can add performance, developer, security, or handheld capabilities without reinstalling or switching distributions.

## 2. User problems

| Problem | Rain OS response |
|---|---|
| Arch-based systems can feel under-explained | Local learning hub, first-run checklist, plain-language explanations, terminal equivalents |
| Rolling releases can be difficult to recover | LTS fallback kernel, snapshots, recovery ISO, preflight update checks |
| Performance tweaks are often opaque | Hardware detection, named profiles, benchmark evidence, reversible changes |
| Security distributions can be dangerous as daily drivers | Isolated Rain Shield profile, explicit threat model, no offensive tools in Core |
| New users cannot tell what is active | Security and system-health panels show actual enabled state |
| Too many choices cause abandonment | One recommended path plus advanced controls, not dozens of equal paths |

## 3. Personas

### Maya, the first Linux learner

Maya needs a reliable desktop, a clear explanation of updates, and a safe place to learn the terminal. She should complete installation and her first maintenance task without reading external documentation.

### Arjun, the developer

Arjun needs language toolchains, containers, Git, editors, and repeatable environment setup. He should be able to enable Rain Forge without changing the underlying base.

### Sofia, the gamer and creator

Sofia needs current graphics support, good laptop power behavior, low-latency audio, and an optional performance profile. She must retain a generic fallback when a tuned kernel causes trouble.

### Leo, the security student

Leo needs authorized lab tools, threat-model education, sandboxing, and a hardened kernel option. He must not accidentally turn a normal laptop into an unprotected offensive appliance.

### Noor, the maintainer

Noor needs reproducible builds, package ownership, CI, logs, rollback, and a narrow supported matrix. The project must be maintainable by a small team.

## 4. Goals and success measures

| Goal | v1 acceptance measure |
|---|---|
| Easy installation | 90% of test users complete install without maintainer intervention |
| Learnability | New users complete update, app install, and recovery lesson in under 30 minutes |
| Recoverability | A deliberately broken package/profile can be rolled back from a snapshot or LTS boot |
| Compatibility | Core boot and graphical login succeed on a defined hardware matrix |
| Transparency | Every non-default package and service has a documented reason |
| Performance choice | Flow profile can be enabled and disabled without reinstalling, and its power/heat trade-off is shown |
| Security honesty | Security UI distinguishes active, available, and unsupported protections |
| Build repeatability | Same source inputs produce byte-identical packages where supported |

## 5. Requirements

### Must have for ISO 0.1

- UEFI boot and a documented legacy fallback strategy.
- Guided installer with automatic and advanced partitioning.
- Core profile with KDE Plasma and a minimal XFCE option.
- Generic and LTS kernels.
- Optional LUKS2 encryption with recovery-key guidance.
- Optional Btrfs subvolumes and snapshots.
- Signed Rain repository with branding, first-run, learning hub, recovery helpers, and profile meta-packages.
- Firewall enabled by default.
- Offline first-run documentation.
- Hardware report and safe update preflight.
- Local package and file manifests.

### Should have for ISO 0.2

- Flow performance kernel.
- CPU capability gating for x86-64-v3 packages.
- Rain Forge developer profile.
- Rain Shield AppArmor and sandbox baseline.
- Secure Boot and UKI test path, explicitly opt-in rather than a universal default.
- Snapshot rollback boot entry.

### Should not block v1

- Full x86-64-v4 repository.
- More than two desktop environments.
- Handheld-specific kernel support.
- Full offensive-security repository integration.
- Cloud account or mandatory telemetry.

## 6. Product principles

Rain OS must be **compatible before optimized, understandable before clever, recoverable before experimental, and private by default**.

## 7. Release strategy

The project uses rolling packages with curated monthly ISO refreshes. A release is blocked when installer, boot, update, encryption, or rollback tests fail on supported hardware. Experimental profiles remain opt-in and are labeled as such. The launch visual themes are **Urban Rain** and **Rural Rain**; later themes may include Coastal Rain, Forest Rain, Monsoon Rain, and Night Rain.

## 8. Open decisions

- Final installer technology: Calamares fork, reuse, or a Rain-specific front end.
- Final first desktop: KDE Plasma only versus KDE plus XFCE in the first image.
- Package build service: native Arch tooling plus CI versus a dedicated build farm.
- Final domain and trademark clearance for “Rain OS”.
