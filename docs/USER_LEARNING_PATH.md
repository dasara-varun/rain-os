# Rain OS User Learning Path

Rain OS must make learning visible and local. The user’s home directory should open with a clear folder named `Rain OS Guide` containing links and exercises. The desktop also provides the same material through Rain Learning Hub.

## User-facing directory

```text
~/Rain OS Guide/
├── 00 Start Here/
│   ├── Welcome.md
│   ├── What Rain OS Is.md
│   └── How To Get Help.md
├── 01 Everyday Desktop/
│   ├── Files and folders.md
│   ├── Apps and permissions.md
│   ├── Networks and audio.md
│   └── Updates without fear.md
├── 02 Terminal Without Fear/
│   ├── Commands to know.md
│   ├── Paths and permissions.md
│   ├── Packages with pacman.md
│   └── Reading errors.md
├── 03 Keep It Healthy/
│   ├── Backups versus snapshots.md
│   ├── Kernels and fallback.md
│   ├── Disk space and logs.md
│   └── Safe update checklist.md
├── 04 Choose Your Rain Profile/
│   ├── Core.md
│   ├── Flow.md
│   ├── Forge.md
│   ├── Shield.md
│   └── Pocket.md
├── 05 Security and Privacy/
│   ├── Encryption.md
│   ├── Firewall.md
│   ├── Sandboxing.md
│   ├── Secure Boot.md
│   └── Authorized security testing.md
├── 06 Build and Create/
│   ├── Git.md
│   ├── Containers.md
│   ├── Python.md
│   └── Building a package.md
└── 99 Recovery/
    ├── If the desktop does not start.md
    ├── If an update fails.md
    ├── Restore a snapshot.md
    └── Export diagnostics.md
```

## Lesson format

Every lesson contains: objective, estimated time, plain-language explanation, safe exercise, terminal equivalent, expected result, recovery hint, and next lesson. Lessons never require internet access unless explicitly marked.

## Keeping the guide current

Rain Learning Hub shows the installed guide version, Rain OS version, active profile, and desktop environment. It can check a signed guide index and install a compatible documentation bundle without changing system packages. If the check fails, the last verified local guide remains available. The guide automatically highlights lessons for KDE, GNOME, XFCE, Cinnamon, or another installed environment when those pages exist.

## First ten lessons

1. Open an application and close it.
2. Create and rename a folder.
3. Connect to Wi-Fi and inspect the connection.
4. Run the safe update flow.
5. Install and remove a package.
6. Read free disk space.
7. Create a snapshot or backup reminder.
8. Boot the LTS fallback kernel in a test instruction.
9. Find a system log without exposing secrets.
10. Create a diagnostic bundle preview without sending it.

## Adaptability rules

Users may skip lessons, but the first-run assistant should recommend the sequence. Each profile adds a small profile-specific path. A user should never be forced to learn offensive-security tooling to use a normal desktop.
