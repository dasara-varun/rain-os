# Rain OS Self-Updating Guide

## Purpose

Rain OS needs a local guide that remains aligned with the installed operating system, selected profile, kernel, desktop environment, and documentation version. The guide should work like a local, versioned combination of Arch-style reference documentation and Athena-style role-aware learning material.

## Design decision

The guide is a **signed documentation package plus a local state-aware viewer**, not an arbitrary web page that runs code. Documentation updates are installed through the normal package/update trust path or a dedicated signed guide index. The viewer reads local system facts and selects relevant pages.

## User command

```text
rain-guide
rain-guide search "Btrfs snapshots"
rain-guide status
rain-guide update
rain-guide offline-export
rain-guide doctor
```

## How it stays current

1. The installed `rain-docs` package declares a documentation schema and compatible Rain OS versions.
2. A signed guide index records the latest compatible guide bundle, release notes, checksum, source revision, and minimum Rain OS version.
3. `rain-guide update` checks signatures, compatibility, disk space, and the user’s selected language before downloading or applying an update.
4. The guide stores the previous bundle and can roll back if indexing fails.
5. A periodic user-level systemd timer may check once per week. It must not silently install system packages or upload usage data.
6. System-critical documentation is also present on the ISO and in the installed package, so the guide works offline.

## State-aware selection

The guide reads only local, non-sensitive facts such as `/etc/os-release`, active desktop session, kernel package names, filesystem type, selected Rain profile, encryption state, and documentation version. It does not read browser history, personal documents, or secrets.

Example selection logic:

```text
Core + KDE + Btrfs + LTS installed -> show KDE, snapshots, kernel fallback, update lessons
Flow + laptop -> show power/heat trade-offs and workload testing
Shield + USBGuard -> show policy enrollment and recovery warnings
Forge + containers -> show Podman/Docker and development lessons
```

## Content layers

| Layer | Update cadence | Offline | Owner |
|---|---|---:|---|
| Emergency recovery | ISO/package release | Yes | Rain release team |
| Core maintenance | Package and monthly ISO | Yes | Rain docs team |
| Desktop guides | Desktop/profile updates | Yes | Environment maintainers |
| Profile guides | Profile release | Yes | Profile owners |
| External reference links | Index refresh | No guarantee | Rain docs team |
| Community articles | Separate, labeled clearly | Optional | Community |

## Trust and safety

Guide pages are inert Markdown or prebuilt HTML. They do not contain executable installation commands without a warning, explanation, package source, and rollback path. Commands that require `sudo` are visually marked and never run automatically from the viewer. The viewer must show the guide version and the system facts used for personalization.

## Failure behavior

If the network is unavailable, the guide remains usable with the last verified bundle. If a signature fails, the update is rejected. If a newer guide requires a newer OS, the user sees the compatibility reason. If indexing fails, the previous bundle remains active.

## Package layout

```text
/usr/share/rain-guide/
├── index.json
├── content/
├── assets/
├── locales/
└── schemas/
/etc/rain-os/guide.conf
/var/lib/rain-guide/state.json
/usr/bin/rain-guide
/usr/lib/rain-guide/update
/usr/lib/systemd/user/rain-guide-update.timer
```

## Acceptance tests

The guide must pass offline search, signature rejection, rollback, profile-aware page selection, language fallback, schema migration, and no-network-at-idle tests. A guide update must never change the installed package set or security policy without a separate, visible package transaction.
