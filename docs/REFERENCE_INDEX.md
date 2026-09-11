# Rain OS Reference Index

This index records the public sources used to revise the concept. It identifies design implications rather than claiming ownership of upstream software.

| Source | Verified point | Rain OS implication |
|---|---|---|
| [EndeavourOS official page](https://endeavouros.com/) | Arch-based terminal-centric system, firewall, PipeWire, power profiles, hardware tooling, systemd-boot/GRUB, modest requirements | Reuse the base and preserve compatibility; add guidance instead of rewriting fundamentals |
| [CachyOS optimized repositories](https://wiki.cachyos.org/features/optimized_repos/) | x86-64-v3/v4 and Zen4+ builds; migration and hybrid Intel AVX-512 caveats | Generic Core baseline; hardware-gated Flow experiments; no universal v4 default |
| [CachyOS kernel documentation](https://wiki.cachyos.org/features/kernel/) | Multiple tuned, LTS, hardened, handheld, server, and real-time variants; hardened trade-offs | Begin with upstream generic/LTS; add at most one Flow and one Shield kernel later |
| [CachyOS settings documentation](https://wiki.cachyos.org/features/cachyos_settings/) | Performance helpers are workload-dependent; power and heat trade-offs exist; settings support overrides | Make Flow opt-in, reversible, measurable, and explicit about battery/thermal cost |
| [Athena OS threat model](https://athenaos.org/en/getting-started/threat-model/) | Active and inactive protections differ; offensive tools reduce defensive posture; supply-chain and root limits remain | Shield must distinguish active/available/partial/unsupported and isolate tools |
| [Athena OS overview](https://athenaos.org/en/getting-started/athenaos/) | Role-based security tooling, encryption, Secure Boot, AppArmor, Firejail, USBGuard, documentation | Reuse the role and documentation model, not a massive default toolset |
| [ArchWiki Secure Boot](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot) | Key management and signing are complex; custom keys can affect firmware/dual boot compatibility | Make Secure Boot opt-in and staged; publish recovery and signing guidance |

All product names, package choices, and architecture decisions in Rain OS remain proposals. Perform a license and version audit before copying code, recipes, artwork, or documentation.
