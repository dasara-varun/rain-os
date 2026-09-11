# Rain OS Data and State Model

## Privacy position

Rain OS is privacy-preserving by default. It does not require an account, collect advertising identifiers, or upload hardware data. Local health and learning data remain on the device unless the user explicitly exports a diagnostic bundle or submits an issue.

## Core state records

| Record | Location | Contents | Retention |
|---|---|---|---|
| Release | `/etc/rain-os/release.json` | ISO version, package baseline, build ID | Until replacement |
| Profile | `/etc/rain-os/profile.conf` | Active profiles and feature flags | Until changed |
| Hardware | `/etc/rain-os/hardware.json` | CPU/GPU/storage capability summary | Local; user deletable |
| Update history | journal plus `/var/lib/rain/update-history.jsonl` | Preflight, transaction, health result | User configurable |
| Learning progress | `~/.local/state/rain-os/learning.json` | Completed lessons and checkpoints | User-owned |
| Snapshots | Btrfs/Snapper state | Snapshot metadata and descriptions | Policy-controlled |
| Diagnostics | user-exported archive | Logs, package list, hardware summary | Deleted after export unless user keeps |

## Data schemas

### `release.json`

```json
{
  "distribution": "Rain OS",
  "version": "0.1.0",
  "channel": "core",
  "iso_build": "YYYYMMDD.N",
  "arch": "x86_64",
  "base_snapshot": "documented Arch snapshot identifier",
  "profile": "core",
  "support_url": "https://example.invalid/support"
}
```

### `profile.conf`

```ini
RAIN_PROFILE=core
RAIN_PERFORMANCE_TIER=generic
RAIN_KERNEL=linux-rain
RAIN_SNAPSHOT_BACKEND=none
RAIN_SECURITY_MODE=baseline
```

### Learning progress

```json
{
  "schema": 1,
  "lessons": {
    "welcome.files": {"status":"complete","completed_at":"local timestamp"},
    "maintenance.update": {"status":"available"}
  }
}
```

## Telemetry policy

No background metrics are required. Optional issue diagnostics are user-triggered, previewed before export, and scrubbed for secrets. The scrubber must remove tokens, passwords, private keys, browser profiles, command arguments containing likely secrets, and file contents outside the selected report paths.

## Migration policy

Configuration schemas are versioned. Migrations must be idempotent, logged, reversible when possible, and tested against at least the previous two schema versions.
