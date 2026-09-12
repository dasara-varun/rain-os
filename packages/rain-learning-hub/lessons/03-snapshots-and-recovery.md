# Lesson 3: Btrfs Snapshots and Recovery

When installed on a Btrfs filesystem, Rain OS automatically captures snapshots before every system update.

## Understanding Snapshots
- A snapshot is an instantaneous, space-efficient copy of your subvolume (`@`).
- It takes almost zero extra disk space initially, only tracking blocks that change.
- Automated pacman hooks trigger `00-rain-pre-snapshot.hook` before any package removal or upgrade.

## Guided Practice: Listing and Managing Snapshots
Inspect your current snapshots:
```bash
sudo rain-btrfs-snapshot list
```

To take an immediate manual snapshot before testing new software:
```bash
sudo rain-btrfs-snapshot manual "Before experimenting with configuration"
```

## Emergency Rollback
If a software change or broken driver causes issues:
1. Boot from your Rain OS Live USB.
2. Launch **Rain Rescue** from the application launcher.
3. Select your root partition and pick the snapshot timestamp to restore.
