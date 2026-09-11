# Rain OS Package Manifest: Reuse-First Edition

The first Core ISO should reuse Arch packages and the current EndeavourOS/Archiso package selection wherever possible. Names such as `linux-rain` are **future Rain package targets**, not a reason to fork a kernel before the baseline is stable.

## Core package policy

| Group | Prefer first | Rain addition |
|---|---|---|
| Base and boot | Arch `base`, `linux`, `linux-lts`, `linux-firmware`, systemd, systemd-boot/GRUB | Rain labels, retention rule, release metadata |
| Desktop | Arch KDE Plasma, SDDM, Dolphin, Konsole, Kate, Firefox | Rain theme, defaults, learning links |
| Network | NetworkManager, upstream applet, firewalld | Rain health/status explanation |
| Audio | PipeWire, WirePlumber, standard desktop integration | Rain troubleshooting lesson |
| Filesystems | Btrfs tools, ext4 tools, cryptsetup, partition tools | Rain installer copy and recovery launcher |
| Hardware | Select one audited hardware detector: EndeavourOS `eos-hwtool` or CachyOS `chwd` | Read-only Rain hardware report adapter |
| Maintenance | pacman, Arch keyring, mirror helper, Git, curl, diagnostics utilities | Update preflight wrapper |
| Recovery | Upstream snapshot/boot utilities selected after testing | Rain recovery runbook and diagnostics scrubber |
| Security baseline | Firewall; optional AppArmor/Firejail foundations | Shield state display; no offensive tools in Core |

## Candidate reused components

- EndeavourOS ISO/Archiso configuration and package recipes, subject to current license and repository review.
- EndeavourOS mirror and hardware helpers, selected by compatibility testing.
- CachyOS `chwd`, kernel recipes, settings, and selected PKGBUILDs, not wholesale repositories.
- Athena role taxonomy, security documentation patterns, LUKS/Secure Boot workflow ideas, and selected tools such as `devotio` only after direct audit.

## Rain-owned packages

`rain-branding`, `rain-first-run`, `rain-learning-hub`, `rain-control-center`, `rain-hardware-report`, `rain-update-preflight`, `rain-profile-core`, `rain-profile-flow`, `rain-profile-forge`, `rain-profile-shield`, `rain-profile-pocket`, `rain-recovery-tools`, `rain-diagnostics-scrubber`, and `rain-docs`.

## Later profile packages

Flow may add GameMode, MangoHud, Steam/Lutris/GameScope, a single tested performance kernel, and reversible power settings. Forge may add developer tooling. Shield may add AppArmor profiles, Firejail, USBGuard, and curated authorized lab bundles. These are not Core dependencies.

## Package exclusions

Do not enable multiple third-party repositories by default. Do not ship the complete BlackArch/Athena tool universe in Core. Do not maintain a custom kernel until the upstream baseline is measured. Do not add a second package manager or a GUI that performs hidden package transactions. Do not include packages whose license or provenance is unknown.
