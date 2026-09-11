# Rain OS Application and System Flows

## 1. Information architecture

The desktop experience has four persistent entry points:

| Entry point | Job |
|---|---|
| Rain Welcome | First boot, setup checklist, profile selection |
| Rain Control Center | System health, updates, security, hardware, recovery |
| Rain Learning Hub | Guided curriculum and searchable local documentation |
| Rain Rescue | Offline recovery and rollback |

## 2. Installation flow

```mermaid
flowchart TD
  A[Boot ISO] --> B[Check firmware, network, disk]
  B --> C{Simple or Advanced?}
  C -->|Simple| D[Choose keyboard, timezone, user]
  C -->|Advanced| E[Partition, filesystem, bootloader]
  D --> F[Choose Core profile]
  E --> G[Choose encryption, Btrfs, profile]
  F --> H[Review exact changes]
  G --> H
  H --> I{Validation passes?}
  I -->|No| J[Explain issue and return to choice]
  J --> H
  I -->|Yes| K[Install and write report]
  K --> L[Reboot into Rain Welcome]
```

## 3. First-run flow

```mermaid
flowchart LR
  A[Rain Welcome] --> B[Confirm privacy and update policy]
  B --> C[Hardware summary]
  C --> D[Choose or keep Core]
  D --> E[Enable encryption guidance if needed]
  E --> F[Run safe update]
  F --> G[Create recovery snapshot or backup reminder]
  G --> H[Start Learning Hub lesson 1]
```

## 4. Update flow

```mermaid
sequenceDiagram
  participant U as User
  participant C as Control Center
  participant P as Preflight
  participant S as Snapshot
  participant M as Pacman
  participant H as Health Check
  U->>C: Select Update
  C->>P: Check space, keys, blockers, kernel fallback
  P-->>C: Report
  C->>S: Create snapshot when supported
  C->>M: Apply signed transaction
  M-->>C: Transaction result
  C->>H: Check boot, services, disk, graphics
  H-->>C: Success or recovery actions
  C-->>U: Explain result and next step
```

## 5. Profile switching flow

Users select a profile, review packages/services/configuration, approve, and receive a rollback point. Removing a profile never removes the Core profile or last kernel.

## 6. Security flow

Rain Shield presents a threat-model summary before activation. It shows the difference between active protections, installed-but-inactive features, and unavailable protections. USBGuard, TPM binding, and aggressive kernel hardening require explicit confirmation and recovery-key guidance.

## 7. Learning flow

The Learning Hub uses short lessons with a safe exercise, a plain-language explanation, a terminal equivalent, a checkpoint, and a recovery hint. Users may complete lessons offline.

## 8. Recovery flow

```mermaid
flowchart TD
  A[Boot failure or user opens Recovery] --> B[Select installed system]
  B --> C[Health scan]
  C --> D{Known snapshot?}
  D -->|Yes| E[Preview snapshot and rollback]
  D -->|No| F[Repair packages, bootloader, or initramfs]
  E --> G[Reboot and verify]
  F --> G
  G --> H{Healthy?}
  H -->|Yes| I[Record incident and learning link]
  H -->|No| J[Keep rescue shell and export diagnostics]
```

## 9. Empty and error states

Every error must state what happened, whether data changed, the safest next action, and how to obtain logs. “Something went wrong” is not acceptable copy.

## 10. Guide update flow

```mermaid
flowchart TD
  A[User opens Rain Learning Hub] --> B[Read local OS/profile/desktop facts]
  B --> C[Check signed guide index]
  C --> D{Compatible verified update?}
  D -->|No| E[Keep local guide and explain why]
  D -->|Yes| F[Show version, size, checksum, and changes]
  F --> G{User accepts?}
  G -->|No| H[Defer and keep current guide]
  G -->|Yes| I[Download, verify, install, index]
  I --> J{Index succeeds?}
  J -->|Yes| K[Show updated lessons]
  J -->|No| L[Restore previous guide bundle]
```

## 11. Environment selection flow

The installer recommends KDE Plasma for Core and exposes GNOME, XFCE, and Cinnamon under a supported profile selector. Advanced and community environments are labeled with their support tier, additional packages, display-manager implications, and guide coverage. A user may add another environment later, but the UI warns that multiple desktop environments can create overlapping settings and larger support surfaces.
