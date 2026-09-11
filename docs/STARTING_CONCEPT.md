# Rain OS Starting Concept

## The product to build first

Rain OS should begin as a **friendly Arch-compatible desktop with recovery and learning built in**. It should not begin as a gaming distro, pentesting distro, benchmark project, or custom-kernel project.

The first ISO should be called **Rain OS Core**. It uses the current EndeavourOS/Arch-style foundation, upstream Arch kernels, standard desktop packages, one supported desktop environment, a simple installer path, a local `Rain OS Guide` directory, and a small Rain integration layer.

## The user promise

> Install once, understand what you have, learn at your pace, and recover when a rolling update goes wrong.

## What users get

- A familiar desktop with Urban Rain and Rural Rain themes.
- A clear first-run checklist.
- A local learner directory with everyday desktop, terminal, maintenance, privacy, and recovery lessons.
- A safe update explanation before package changes.
- A visible LTS fallback kernel.
- Optional Btrfs snapshots when selected.
- Firewall and network status explained in plain language.
- No mandatory account and no background telemetry.
- Optional Flow, Forge, and Shield profiles later.

## What users do not get in v1

They do not get universal hardware support, guaranteed performance gains, custom Secure Boot keys by default, a complete offensive-security tool collection, a huge selection of desktops, or a promise that rolling releases cannot fail.

## Correct product architecture

Rain OS is a thin integration layer around upstream software. The project owns the experience, documentation, profiles, safety checks, provenance, and recovery workflows. It should upstream generic fixes and remove local forks whenever the upstream project accepts them.

## Recommended first milestone

The first meaningful milestone is not “a beautiful ISO.” It is a repeatable Core ISO that passes these tests:

1. Boots in a UEFI virtual machine.
2. Installs to ext4.
3. Installs to Btrfs with optional LUKS2.
4. Reboots into a working desktop.
5. Performs a signed update with a clear preflight.
6. Opens the local learning path.
7. Retains a working fallback kernel.
8. Exports diagnostics without secrets.
9. Documents known limitations.

After this, add snapshots, then Flow, Forge, and Shield one at a time.
