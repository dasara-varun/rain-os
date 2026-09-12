# Rain OS GitHub Actions Parallel Build Blueprint

## Purpose

GitHub Actions is the primary clean build authority for Rain OS. This document is the implementation companion to `Rain-OS-Commercial-Build-Spec.md`. The current public workflow is sequential; the target pipeline separates independent work and passes immutable artifacts between jobs.

## Target dependency graph

```text
validate ───────────────┐
                        ├── package-matrix ── package-repository ── iso-matrix ── qemu-qa ── provenance ── release
docs-and-design ────────┘
```

## Required workflow split

| Workflow | Required behavior |
|---|---|
| `validate.yml` | Fast checks on pull requests and pushes; required status check |
| `packages.yml` | Matrix-build each Rain PKGBUILD; upload packages and logs |
| `iso.yml` | Consume exact package repository artifacts; build Core and approved beta profiles |
| `qa.yml` | Boot ISO in QEMU, test installer and desktop, upload logs/screenshots |
| `nightly.yml` | Detect Arch drift and rebuild without publishing stable releases |
| `release.yml` | Protected tag, verify artifacts, generate attestations, sign and publish |

## Minimal package matrix

```yaml
strategy:
  fail-fast: false
  matrix:
    package: [rain-branding, rain-first-run, rain-learning-hub,
              rain-recovery-tools, rain-update-preflight, rain-control-center]
```

Each matrix job must fail if `makepkg` fails. It must not use `|| true` for the package build. Source checksums must be present before a release tag is accepted. The job uploads the package, `makepkg` log, PKGBUILD snapshot, resolved dependencies, and an SPDX or CycloneDX package record.

## ISO profile matrix

The first production pipeline contains only `core-kde`. Add a profile to the matrix only after its installer, desktop, accessibility, and recovery tests have an owner.

```yaml
strategy:
  fail-fast: false
  matrix:
    include:
      - profile: core-kde
        desktop: kde
        support: official
```

## Artifact naming

Use names that cannot collide across matrix jobs:

```text
rain-packages-${{ github.sha }}-${{ matrix.package }}
rain-repository-${{ github.sha }}
rain-iso-${{ github.sha }}-${{ matrix.profile }}
rain-qa-${{ github.sha }}-${{ matrix.profile }}
```

Do not rebuild a successful package matrix job merely because a different package failed. Re-run the failed matrix child or rebuild the full set only when the package repository state changes.

## Security rules

Use read-only workflow permissions by default. Pin third-party actions to commit SHAs. Do not expose package or ISO signing keys to build jobs. Use a protected release environment for signing and publication. Use GitHub artifact attestations where available, and publish their identifiers with checksums and SBOMs. Treat caches as disposable accelerators, not trusted package sources.

## Current-workflow corrections

The public `build-iso.yml` currently performs keyring initialization, validation, package repository construction, ISO construction, and artifact upload in one sequential job. The revised implementation must:

1. Replace the single job with reusable workflows and `needs` dependencies.
2. Move package compilation into a non-root matrix.
3. Make package failures fatal.
4. Pass an immutable package repository artifact into ISO jobs.
5. Add QEMU boot and installer smoke tests.
6. Upload logs, manifests, SBOMs, and provenance alongside the ISO.
7. Add concurrency cancellation for branch builds but never cancel protected release tags.
8. Add a protected release environment before signing or publishing.
9. Pin the ShellCheck action instead of using a mutable `master` reference.
10. Keep WSL2 as the local fallback and hardware-test path.

## Acceptance test

A same-commit build is accepted when a second workflow run can download the exact package artifact, build the same ISO profile, reproduce the package manifest, pass QEMU smoke tests, verify checksums and attestations, and publish only after a human approves the protected release environment.
