# Rain OS File Manifest

## 1. Installed filesystem targets

```text
/
├── boot/
│   ├── EFI/Linux/                         # UKIs when enabled
│   ├── loader/entries/                    # systemd-boot entries
│   └── rain/                              # release metadata and fallback assets
├── etc/
│   ├── rain-os/
│   │   ├── release.json                   # version, build, profile, source IDs
│   │   ├── profile.conf                   # selected profile and feature flags
│   │   ├── hardware.json                  # local hardware summary; no upload
│   │   ├── repositories.conf              # managed Rain repository state
│   │   └── policies/                      # security and update policies
│   ├── pacman.d/rain-mirrorlist
│   ├── systemd/system/                    # Rain services and timers
│   ├── apparmor.d/                        # Rain Shield profiles
│   └── skel/                              # default user configuration
├── opt/rain/
│   ├── docs/                              # versioned offline documentation
│   ├── lessons/                           # Learning Hub content
│   ├── recovery/                          # live and installed helpers
│   └── assets/                            # icons, diagrams, theme assets
├── usr/bin/
│   ├── rain-control-center
│   ├── rain-first-run
│   ├── rain-learning
│   ├── rain-update-preflight
│   ├── rain-profile
│   ├── rain-kernel
│   ├── rain-recovery
│   └── rain-hardware
├── usr/lib/rain/
│   ├── policy/                            # PolicyKit helpers, never GUI-root
│   ├── checks/                            # health and preflight checks
│   ├── profiles/                          # profile install/remove actions
│   └── migrations/                        # versioned state migration
├── usr/share/applications/
├── usr/share/icons/hicolor/
├── usr/share/wayland-sessions/
├── usr/share/xsessions/
└── usr/share/doc/rain-os/
```

## 2. Source repository tree

```text
rain-os/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── Makefile
├── docs/
├── packages/
│   ├── rain-branding/
│   ├── rain-first-run/
│   ├── rain-control-center/
│   ├── rain-learning-hub/
│   ├── rain-recovery-tools/
│   ├── rain-hardware-agent/
│   ├── rain-update-preflight/
│   ├── rain-profile-*/
│   └── linux-rain*/
├── archiso/
│   ├── profiledef.sh
│   ├── packages.x86_64
│   ├── pacman.conf
│   ├── airootfs/etc/
│   ├── airootfs/usr/local/bin/
│   ├── efiboot/
│   └── syslinux/
├── repository/
│   ├── build-repo.sh
│   ├── signing-policy.md
│   └── keys/README.md
├── apps/
│   ├── control-center/
│   ├── first-run/
│   └── learning-hub/
├── docs-site/
├── tests/
│   ├── installer/
│   ├── boot/
│   ├── packages/
│   ├── recovery/
│   ├── security/
│   └── accessibility/
├── branding/
├── ci/
└── scripts/
```

## 3. State ownership rules

Configuration in `/etc/rain-os` is machine state. Documentation and lessons under `/opt/rain` are package-owned. User progress belongs under `~/.local/state/rain-os/`. Logs belong in the system journal and exported diagnostic bundles. No package may silently edit a user’s home files without a migration and backup path.
