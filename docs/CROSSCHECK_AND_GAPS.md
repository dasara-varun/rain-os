# Rain OS Cross-Check, Gaps, and Corrective Decisions

**Review basis:** current official project pages and documentation reviewed on 2026-09-11.

## Overall conclusion

The reuse-first Rain OS concept is viable as a **thin integration distribution**, but it is not viable as a simultaneous full fork of three distributions. The corrected starting point is a Core ISO assembled from Arch and EndeavourOS patterns, with Rain-owned UX and documentation, followed by carefully tested Flow and Shield profiles.

## Findings and decisions

| Finding | Risk to Rain OS | Corrective decision |
|---|---|---|
| EndeavourOS is lightweight, terminal-centric, Arch-based, and already supplies firewall, PipeWire, power profile, hardware, and bootloader choices [1] | Rebuilding these creates unnecessary maintenance | Reuse the base and add Rain explanations rather than replacements |
| CachyOS uses CPU-specific repositories including x86-64-v3/v4 and Zen4+ [2] | Wrong instruction-set selection can make systems unstable or unbootable; hybrid Intel AVX-512 assumptions are especially risky | Core stays generic; Flow begins with opt-in settings and one kernel; optimized packages come later and are hardware-gated |
| CachyOS explicitly says performance mode may increase power/heat and may not help older CPUs [3] | “Fast for everyone” is false and can damage battery life or user trust | Flow is workload-specific, shows power impact, measures before/after, and is not enabled by default |
| CachyOS maintains many kernel variants, including hardened variants with significant performance/user-experience impact [4] | Too many kernels multiply testing and DKMS/GPU failures | Rain v1 supports upstream generic and LTS first; Flow and Shield kernels are later, one each |
| Athena documents that many security features are installed but inactive or only partial [5] | A polished security UI could overpromise protection | Rain Shield must show Active, Available, Partial, and Unsupported states |
| Athena notes that offensive tools and upstream packages are not fully source-audited and that root access defeats much of the model [5] | A large security repository increases supply-chain and privilege risk | Core contains no offensive tools; Shield uses curated, signed, isolated bundles and an explicit threat model |
| Arch Secure Boot requires key management and signing; custom keys can cause firmware or device compatibility problems [6] | Making custom Secure Boot default can brick or complicate devices and dual boot | Secure Boot support is opt-in and staged; use documented signing paths, retain recovery instructions, and test vendor firmware before claiming support |
| EndeavourOS currently supports systemd-boot and GRUB and reports modern UEFI as the best path [1] | Forcing a single bootloader excludes users | Prefer systemd-boot on tested UEFI systems; retain GRUB/legacy path where supported |

## Remaining drawbacks

### Rolling-release support burden

Rain OS inherits Arch’s continuously moving package ecosystem. Documentation, ISO refreshes, and Rain integration packages can drift. The mitigation is not to freeze the entire distribution. The mitigation is to maintain a small Rain delta, run preflight and rollback tests, publish known issues, and retain an LTS kernel.

### Small-team capacity

The project cannot initially maintain a complete kernel family, many desktop environments, a security-tool universe, and a custom installer. The first public milestone must therefore be Core plus learning and recovery. Flow, Forge, and Shield remain profile work.

### Upstream dependency risk

Reused components may change command names, configuration formats, licenses, or support assumptions. The component manifest must pin versions, record owners, and run compatibility tests at every ISO iteration.

### User expectation risk

“Perfect Linux” is not a technically meaningful promise. Rain OS should promise a clear experience and honest recovery, not universal hardware support or immunity from rolling-release failures.

## Revised definition of success

Rain OS succeeds if a new user can install it, understand what is active, learn the basic maintenance workflow, recover from a routine update failure, and add a specialized profile without replacing the whole system.

## References

[1]: https://endeavouros.com/ "EndeavourOS official project page"
[2]: https://wiki.cachyos.org/features/optimized_repos/ "CachyOS optimized repositories"
[3]: https://wiki.cachyos.org/features/cachyos_settings/ "CachyOS settings and performance helpers"
[4]: https://wiki.cachyos.org/features/kernel/ "CachyOS kernel documentation"
[5]: https://athenaos.org/en/getting-started/threat-model/ "Athena OS threat model"
[6]: https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot "ArchWiki Secure Boot guidance"
