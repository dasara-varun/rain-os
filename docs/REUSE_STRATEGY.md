# Rain OS Reuse Strategy

## Recommendation

Use existing software aggressively, but do not combine complete distributions by enabling all of their repositories. The efficient unit of reuse is the **component**, not the entire operating system.

A Rain OS build should begin with the EndeavourOS ISO and Arch package model, then selectively add tested CachyOS and Athena components. This preserves the fastest path to a working ISO while preventing repository conflicts, duplicated services, and unclear support responsibility.

## Five-level decision tree

1. Does an upstream component already solve the requirement? If yes, reuse it.
2. Can Rain meet its UX requirement with configuration, theme, package metadata, or documentation? If yes, adapt it.
3. Does Rain need a safer user-facing flow around it? If yes, wrap it with a non-root interface and PolicyKit helper.
4. Is there a general bug or improvement? If yes, patch upstream first.
5. Is release blocked by upstream timing and is the code legally reusable? If yes, maintain a temporary fork with an owner and exit date.

## Why not merge repositories wholesale

Each distribution makes choices about package versions, kernel patches, hooks, signing, mirrors, and supported services. Enabling several repositories can create file conflicts, downgrade loops, ABI mismatches, and unclear security responsibility. Rain should import source ideas and selected packages only after testing the complete dependency and update path.

## Minimum new Rain code

Rain-owned code should initially cover: branding package, first-run launcher, local learning index, hardware summary adapter, update preflight wrapper, profile transaction wrapper, recovery launcher, diagnostics scrubber, and policy documentation. Low-level installer, package manager, kernel build, and security primitives should remain upstream until evidence shows a gap.

## Fork policy

A fork requires an issue containing the reason, upstream link, license, patch delta, owner, test plan, security review, and sunset condition. Every fork is reviewed at each ISO cycle. If upstream accepts the fix or Rain can remove the fork, the fork is deleted.

## Acceptance rule

If a reused component cannot be updated, tested, attributed, or removed without destabilizing Core, it is not ready for the default ISO.
