# Rain OS QA Matrix

## Release-blocking tests

| Area | Test | Gate |
|---|---|---|
| Boot | ISO boots UEFI in QEMU/KVM | Pass |
| Install | Simple install to blank ext4 disk | Pass |
| Install | Advanced install with Btrfs | Pass |
| Encryption | LUKS2 install and recovery-key test | Pass |
| Login | User reaches desktop after reboot | Pass |
| Network | Wi-Fi/Ethernet and DNS | Pass |
| Audio | Playback and microphone detection | Pass |
| Graphics | Mesa rendering and supported GPU path | Pass |
| Update | Signed update and preflight | Pass |
| Recovery | Snapshot rollback after failed package | Pass |
| Kernel | Generic and LTS boot entries | Pass |
| Profile | Add/remove Flow without reinstall | Pass when profile ships |
| Security | Firewall active and visible | Pass |
| Privacy | No network telemetry at idle | Pass |
| Accessibility | Keyboard navigation, focus, high contrast | Pass |
| Documentation | Offline first-run and recovery docs present | Pass |

## Supported test matrix

Begin with QEMU/KVM, one AMD desktop, one Intel laptop, one NVIDIA system, one AMDGPU system, one low-RAM machine, and one virtualized environment. Expand only when maintainers can reproduce failures.

## Automated checks

- Shell linting and unit tests for helpers.
- Package dependency and file-conflict checks.
- ISO boot test.
- Installer smoke test with virtual disks.
- Profile idempotence: apply twice produces no unexpected change.
- Profile removal does not remove Core dependencies.
- Configuration migration tests.
- Secret scrubber tests.
- Accessibility checks for desktop application UI.
- Reproducibility comparison where toolchain permits.

## Acceptance gates

No ISO is public if a P0 issue exists. No release candidate is published if a P1 issue exists on a supported path. Every known workaround appears in release notes and local documentation.
