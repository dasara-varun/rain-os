# Rain OS Security Model

## 1. Scope

Rain OS is a general-purpose desktop with an optional security-learning profile. It is not a certification, anonymity system, or guarantee against compromise. The system documents its assumptions and distinguishes defaults from available controls.

## 2. Threats

| Threat | Baseline mitigation | Optional mitigation | Residual risk |
|---|---|---|---|
| Lost or stolen device | LUKS2 installer option | TPM-bound unlock and recovery key | Live memory and firmware attacks remain possible |
| Malicious boot modification | UEFI boot path and signatures | Secure Boot and signed UKIs | Firmware compromise is outside normal OS control |
| Malicious desktop application | User permissions and updates | AppArmor and Firejail policies | Policy coverage is incomplete |
| Network attack | Firewall and timely updates | Hardened profile and segmented lab | User-installed services can create exposure |
| Package supply-chain compromise | Signature verification and trusted repositories | Curated Rain Shield sources and isolation | Upstream compromise cannot be eliminated |
| Broken rolling update | LTS kernel, snapshots, recovery ISO | Staged updates and health checks | Hardware-specific failures remain possible |
| USB device attack | User awareness | USBGuard in Rain Shield | Bad policy can block needed devices |
| Dangerous security tools | Not present in Core | Shield authorization notice and isolation | User can intentionally bypass controls |

## 3. Default-state table

| Feature | Core default | Shield default | Meaning |
|---|---:|---:|---|
| Firewall | Active | Active | Network filtering, not endpoint invulnerability |
| Full-disk encryption | Installer choice | Strongly recommended | Protects data at rest |
| AppArmor framework | Available/active where supported | Active with profiles | Mandatory access control needs policy coverage |
| Firejail | Installed only if packaged | Available for selected apps | Sandboxing can be bypassed by privileged code |
| USBGuard | Disabled | Wizard-assisted | Requires a device policy |
| Hardened kernel | Available | Boot option | May reduce performance or compatibility |
| Secure Boot | Supported path | Recommended | Requires supported firmware and key handling |
| TPM unlock | Available | Recommended with recovery key | Hardware state changes may require passphrase |

## 4. Security requirements

- Do not expose privileged operations through a root GUI.
- Use PolicyKit and narrowly scoped helpers.
- Sign Rain packages and rotate repository keys with documented overlap.
- Build release artifacts in isolated CI.
- Publish checksums, package manifests, source revisions, and an SBOM.
- Provide a security contact and disclosure process.
- Keep security documentation versioned with the packages it describes.
- State when a protection is installed, active, partial, or unsupported.
- Isolate high-risk tools with containers or disposable virtual machines where practical.

## 5. Security learning requirement

Rain Shield must teach the user that authorization matters. Every role page includes scope, safe lab setup, legal boundary, cleanup, and reporting practices. Tool installation is never presented as permission to attack third-party systems.
