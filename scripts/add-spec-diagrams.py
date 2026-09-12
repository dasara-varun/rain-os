from pathlib import Path
p = Path('/home/ubuntu/rain-os-spec/Rain-OS-Commercial-Build-Spec.md')
s = p.read_text()
marker = '\n\\newpage\n\n# References\n'
diagrams = r'''
\\newpage

# Architecture diagrams

## Diagram 1: Windows to ISO build topology

```mermaid
flowchart LR
  W[Windows 10/11] --> T[Windows Terminal / PowerShell]
  T --> S[WSL2 Arch Linux]
  S --> R[Rain repository under /home]
  R --> A[Archiso releng profile]
  A --> M[mkarchiso]
  M --> I[Rain ISO + checksum + SBOM]
  I --> Q[QEMU/Hyper-V VM tests]
```

## Diagram 2: One-shot build pipeline

```mermaid
flowchart TD
  A[Preflight host] --> B[Verify WSL path and tools]
  B --> C[Refresh keyring and packages]
  C --> D[Build Rain PKGBUILDs]
  D --> E[Create signed rain repository]
  E --> F[Overlay current Archiso profile]
  F --> G[mkarchiso]
  G --> H[Hash and manifest]
  H --> I[Boot smoke test]
  I --> J[Release candidate or failure report]
```

## Diagram 3: Rain OS layered architecture

```mermaid
flowchart TB
  U[User and applications] --> X[Desktop environment]
  X --> R[Rain UX: Control Center, Guide, First Run]
  R --> P[Rain profiles: Core, Flow, Forge, Shield, Pocket]
  P --> A[Arch packages and services]
  A --> K[Linux kernel and firmware]
  K --> H[Hardware and firmware]
```

## Diagram 4: Installer flow

```mermaid
flowchart TD
  A[Live boot] --> B[Hardware compatibility check]
  B --> C[Choose desktop and profile]
  C --> D[Review disk plan]
  D --> E{Encryption?}
  E -->|yes| F[LUKS2 and recovery key]
  E -->|no| G[Plain filesystem]
  F --> H[Install]
  G --> H
  H --> I[Create fallback boot entry]
  I --> J[First-run handoff]
```

## Diagram 5: Update and rollback

```mermaid
flowchart LR
  A[User requests update] --> B[Preflight]
  B --> C{Healthy and enough space?}
  C -->|no| D[Explain and stop]
  C -->|yes| E[Create snapshot if supported]
  E --> F[Signed pacman transaction]
  F --> G[Health check]
  G --> H{Healthy?}
  H -->|yes| I[Mark snapshot good]
  H -->|no| J[Boot or restore previous state]
```

## Diagram 6: Self-updating guide

```mermaid
flowchart TD
  A[Local guide] --> B[Read OS/profile/desktop facts]
  B --> C[Fetch signed index]
  C --> D{Compatible?}
  D -->|no| E[Keep verified bundle]
  D -->|yes| F[Verify checksum and signature]
  F --> G[Install new bundle]
  G --> H{Index valid?}
  H -->|yes| I[Activate]
  H -->|no| J[Rollback guide]
```

## Diagram 7: Windows application decision tree

```mermaid
flowchart TD
  A[Requested application] --> B{Linux-native?}
  B -->|yes| C[Native package or Flatpak]
  B -->|no| D{Steam game?}
  D -->|yes| E[Proton + ProtonDB]
  D -->|no| F{Wine-compatible?}
  F -->|yes| G[Bottles or Lutris prefix]
  F -->|no| H{Requires Windows kernel or DRM?}
  H -->|yes| I[Windows VM or dual boot]
  H -->|no| J[Research compatibility or unsupported]
```

## Diagram 8: Application isolation

```mermaid
flowchart TB
  A[Rain Control Center] --> B[App manifest]
  B --> C[Flatpak sandbox]
  B --> D[Wine prefix]
  B --> E[Proton prefix]
  B --> F[Windows VM]
  C --> G[User files with explicit portals]
  D --> G
  E --> G
  F --> H[Shared folder with warning]
```

## Diagram 9: AI-agent development loop

```mermaid
flowchart LR
  A[Discuss] --> B[Plan]
  B --> C[Research and reuse audit]
  C --> D[Implement smallest change]
  D --> E[Run tests]
  E --> F[Review security/design/minimality]
  F --> G[Human decision]
  G -->|keep| H[Ship artifact]
  G -->|change| B
  G -->|remove| I[Delete and record learning]
```

## Diagram 10: Profile composition

```mermaid
flowchart TD
  C[Core] --> F[Flow optional]
  C --> D[Forge optional]
  C --> S[Shield optional]
  C --> P[Pocket optional]
  F --> X[Hardware and workload gate]
  D --> Y[Developer package group]
  S --> Z[Threat model and isolation]
  P --> Q[Low-resource defaults]
```

## Diagram 11: Package provenance

```mermaid
flowchart LR
  A[Upstream source] --> B[License and signature audit]
  B --> C[PKGBUILD]
  C --> D[Clean builder]
  D --> E[Tests and SBOM]
  E --> F[Signed Rain repository]
  F --> G[ISO package manifest]
```

## Diagram 12: Recovery layers

```mermaid
flowchart TB
  A[Application failure] --> B[Restart or remove app]
  B --> C[Profile failure]
  C --> D[Disable profile]
  D --> E[Update failure]
  E --> F[Restore snapshot]
  F --> G[Kernel failure]
  G --> H[Boot LTS]
  H --> I[Rescue ISO]
  I --> J[Backup and reinstall only as last resort]
```

## Diagram 13: Support and telemetry boundary

```mermaid
flowchart LR
  A[Local diagnostics] --> B[Secret scrubber]
  B --> C[User preview]
  C --> D{Consent?}
  D -->|no| E[Keep local]
  D -->|yes| F[Support upload]
  F --> G[Ticket or forum]
```

## Diagram 14: Release channels

```mermaid
flowchart TD
  A[Arch upstream] --> B[Rain integration CI]
  B --> C[Testing repository]
  C --> D[Hardware and VM matrix]
  D --> E[Stable repository]
  E --> F[Monthly ISO refresh]
  F --> G[Supported users]
```

## Diagram 15: Commercial support loop

```mermaid
flowchart LR
  A[User issue] --> B[Guide and diagnostics]
  B --> C[Community triage]
  C --> D[Support escalation]
  D --> E[Reproducible bug]
  E --> F[Upstream or Rain fix]
  F --> G[Regression test]
  G --> H[Guide update]
'''
if marker not in s:
    raise SystemExit('references marker not found')
s = s.replace(marker, '\n' + diagrams + marker, 1)
p.write_text(s)
print('Inserted 15 Mermaid diagrams')
