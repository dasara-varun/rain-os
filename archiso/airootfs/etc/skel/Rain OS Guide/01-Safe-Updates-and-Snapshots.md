# Safe Updates & Snapshots

Rain OS is protected by automated Btrfs snapshot hooks (`00-rain-pre-snapshot.hook`).

Before any `pacman -Syu` package update:
1. Rain OS automatically creates a read-only snapshot of `@` in `/.snapshots/`.
2. Both `linux` and `linux-lts` kernels remain installed.
3. If an update ever fails, boot your live USB or pick `linux-lts` in the boot menu!
