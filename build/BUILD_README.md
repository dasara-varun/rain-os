# Rain OS Reuse-First Build Starter

## Purpose

This starter builds a clean Archiso baseline before Rain-owned packages exist. It deliberately uses upstream package names and leaves Rain integration packages for the next loop. That prevents an apparently complete specification from pretending that unimplemented packages already exist.

## Build host

Use an Arch Linux build host with `archiso`, `git`, `base-devel`, `squashfs-tools`, `dosfstools`, `mtools`, `xorriso`, `edk2-ovmf`, and `qemu-desktop`. A clean VM or container is preferred. Keep package signing keys outside the repository.

## Fast path

1. Compare the current EndeavourOS ISO/Archiso profile with this starter.
2. Copy only the required build layout after reviewing its license and provenance.
3. Build the upstream Core ISO using `archiso/packages.x86_64`.
4. Boot it in QEMU/KVM.
5. Add Rain branding and local documentation.
6. Implement Rain packages one at a time, adding them to a local signed repository.
7. Add each package to the ISO only after its package and integration tests pass.

```bash
./scripts/validate-spec.sh
sudo ./scripts/build-iso.sh
sha256sum out/*.iso > out/SHA256SUMS
```

## What is intentionally not in the starter

The starter does not yet claim to build `rain-control-center`, `rain-learning-hub`, a custom kernel, a custom installer, or a complete security repository. Those are implementation work items. The correct reuse path is to first establish a bootable, installable upstream baseline.

## Provenance requirements

For every copied or vendored upstream file, record source URL, commit/release, license, copyright notice, local changes, and removal plan. Do not copy project branding or imply official affiliation. Do not commit private signing keys.

## Output contract

Each release build produces the ISO, checksums, resolved package list, source revision manifest, SBOM, build log, known issues, and signature metadata.
