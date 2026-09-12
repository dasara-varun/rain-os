from pathlib import Path

p = Path('/home/ubuntu/rain-os-spec/Rain-OS-Commercial-Build-Spec.md')
s = p.read_text()

s = s.replace('**Revision:** 1.0 research baseline', '**Revision:** 1.1 GitHub Actions parallel-build update')
s = s.replace('**Target host:** Windows 10/11 with WSL2 and an official Arch Linux WSL distribution  ', '**Primary build system:** GitHub Actions parallel build pipeline with Arch Linux container/self-hosted runner options  \n**Developer fallback:** Windows 10/11 with WSL2 and an official Arch Linux WSL distribution  ')
s = s.replace('The correct execution order is **audit → Core ISO → install → recovery → guide → hardware → profiles → Windows-app experience → commercial hardening**. Do not implement all pages in parallel. Each milestone must leave a bootable or testable artifact.', 'The correct execution order is **audit → parallel CI foundation → Core ISO → install → recovery → guide → hardware → profiles → Windows-app experience → commercial hardening**. Development work may run in parallel, but release promotion remains gated by dependencies. Each milestone must leave a bootable or testable artifact.')
s = s.replace('The build path must therefore be tested in the user’s Windows WSL2 environment before the first ISO is treated as a real milestone.', 'The build path is authoritative in GitHub Actions for clean, repeatable artifacts. The user’s Windows WSL2 environment remains the fast local development and troubleshooting fallback, and real hardware testing remains outside GitHub Actions.')
needle = '## Global acceptance rule\n\n'
insert = r'''## GitHub Actions is the primary build authority

GitHub Actions is the canonical clean build system for Rain OS. Local Windows/WSL2 builds are developer accelerators and debugging tools. A release ISO must be reproducible from a tagged commit in GitHub Actions, with a resolved package manifest, checksums, SBOM, build logs, test reports, and artifact provenance.

The current public workflow is a useful baseline but is sequential. The updated design splits it into independent validation, package, profile, ISO, QEMU-smoke, provenance, and release jobs. Matrix jobs are used only where outputs are genuinely independent. A matrix must not create unsupported desktop or hardware combinations merely because the platform can create them.

### Canonical workflow graph

```mermaid
flowchart TD
  A[Pull request or tag] --> B[Fast validation]
  B --> C[Package matrix]
  B --> D[Documentation and design checks]
  C --> E[Package repository assembly]
  E --> F[ISO profile matrix]
  F --> G[QEMU smoke matrix]
  G --> H[SBOM checksums attestations]
  H --> I{Protected release tag?}
  I -->|no| J[CI artifacts]
  I -->|yes| K[Human approval and GitHub Release]
```

### Workflow files

The repository should contain the following workflows:

| File | Trigger | Purpose | Release authority |
|---|---|---|---|
| `.github/workflows/validate.yml` | pull request, push | Shell, Python, JSON, Markdown, PKGBUILD and policy checks | Required status check |
| `.github/workflows/packages.yml` | pull request, push, tag | Build Rain PKGBUILDs in a package matrix | Produces signed/unsigned test package artifacts |
| `.github/workflows/iso.yml` | workflow call, push, tag | Assemble Archiso profiles after package repository artifact exists | Produces ISO artifacts |
| `.github/workflows/qa.yml` | workflow call | QEMU boot/install/smoke tests for each ISO variant | Required before promotion |
| `.github/workflows/nightly.yml` | scheduled | Rebuild against current Arch packages and report drift | No automatic stable release |
| `.github/workflows/release.yml` | protected tag `v*` | Attest, sign, publish checksums/SBOM/ISO to GitHub Release | Human-approved |

### Matrix design

The initial matrix must stay small:

```yaml
strategy:
  fail-fast: false
  matrix:
    package_group: [branding, first-run, learning, recovery, update-preflight, control-center]
```

The first ISO matrix should contain only `core-kde`. Add `core-gnome`, `core-xfce`, or `core-cinnamon` only after each profile has an owner and test evidence:

```yaml
strategy:
  fail-fast: false
  matrix:
    include:
      - profile: core-kde
        desktop: kde
        support: official
      - profile: core-gnome
        desktop: gnome
        support: beta
```

The matrix must not multiply across package group, desktop, kernel, filesystem, GPU, and architecture without a declared test purpose. GitHub Actions imposes a maximum of 256 jobs per matrix, but Rain OS should remain far below that limit for cost and diagnosis clarity [31].

### Reusable workflows

Package and ISO workflows should be reusable with `workflow_call`, so pull requests, nightly builds, and release tags share the same build logic. Inputs must include `rain_ref`, `profile`, `channel`, `publish_artifacts`, and `sign_release`. Outputs must expose artifact names, checksums, package manifests, and test result paths.

### Artifact contract

Every matrix job uploads an artifact with a stable name containing the commit and matrix identity. Package jobs upload packages, repository database files, package manifests, and build logs. ISO jobs upload ISO, checksum, package manifest, SBOM, build metadata, and mkarchiso logs. QA jobs upload screenshots, serial logs, QEMU exit status, installer logs, and test summaries. Artifacts have retention appropriate to their channel; release artifacts are copied to a GitHub Release and long-term archival store.

### Cache contract

Use `actions/cache` only for reproducible accelerators such as downloaded Arch packages, language dependencies, and tool downloads. Cache keys must include the architecture, Archiso version, package repository state, profile hash, and lock/revision inputs. Never use a cache as the source of truth for a release package. A cache hit must be safe to delete and rebuild. Cache poisoning is treated as a supply-chain risk.

### Concurrency contract

Pull request and branch workflows use a concurrency group based on workflow name and branch/ref and cancel superseded runs. Release tags and signed release jobs use a unique immutable group and must never be cancelled after approval. A scheduled nightly build may be cancelled when a newer nightly run starts, but its failure report must remain visible.

Example:

```yaml
concurrency:
  group: rain-${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ !startsWith(github.ref, 'refs/tags/v') }}
```

### Permissions and trust boundaries

Workflow permissions default to read-only. The build job receives `contents: read` and `actions: read`. The attestation job receives only `id-token: write` and `attestations: write`. The release job receives `contents: write` only after protected-environment approval. Package and ISO build jobs never receive release secrets. Third-party actions are pinned to full commit SHAs and reviewed on update.

### Hosted and self-hosted runners

The project must support two runner classes. Hosted runners are preferred for validation, package compilation, documentation, and ordinary QEMU tests. ISO builds that require privileged loop devices, `/dev` access, or nested virtualization must run in an explicitly tested Arch container or an ephemeral self-hosted Linux runner. A self-hosted runner must be dedicated or ephemeral, automatically cleaned after each job, patched, access-restricted, and forbidden from storing signing keys in its workspace.

The current workflow uses an Arch container with `--privileged` and `/dev` exposure. This is a prototype path, not an unconditional production guarantee. The release readiness gate must prove that the selected runner class can mount, squash, boot-test, and clean up correctly. If hosted container privileges are unavailable, the workflow must fail clearly and route to the approved self-hosted runner label rather than silently skipping ISO creation.

### Signing and attestations

Build jobs never access private signing keys. A release promotion job in a protected GitHub Environment performs package repository signing and ISO signing only after QA passes. Prefer short-lived OIDC-backed artifact attestations where available. Store public keys in a versioned keyring package and publish checksums, SBOM, source revision, workflow run, and attestation identifiers together. Artifact attestations establish build provenance and integrity claims but do not replace package signature verification [32] [33].

### Release promotion

A tag does not immediately publish an ISO. The release workflow downloads the exact QA-approved artifacts, verifies checksums, verifies attestations, verifies the source tag, generates release notes and known issues, waits for environment approval, and then publishes the ISO, checksum, SBOM, signatures, provenance statement, installation guide, and recovery guide. Failed promotion leaves artifacts available for diagnosis but does not create a stable release.

### Pull-request behavior

Every pull request runs fast validation, syntax tests, changed-package builds, documentation link/schema checks, and a small Archiso profile sanity check where practical. Full ISO and QEMU installation tests run on changes to `archiso/`, `packages/`, `repository/`, installer files, boot files, kernel policy, or release workflows. Design-only changes run accessibility and asset checks without rebuilding every ISO variant.

### Parallel AI-agent integration

AI agents may work in parallel on independent issues, but GitHub Actions remains the source of truth. Each agent receives a bounded worktree or branch and must attach a plan, changed-file list, tests, and rollback. ECC/GSD handles planning and evidence, gstack reviews cross-functional impact, taste-skill reviews UI, ponytail reviews unnecessary complexity, Headroom is optional local context compression, and Ralph is limited to a small issue with a maximum iteration count. No agent may approve a release, access signing secrets, or merge a failing workflow.

### GitHub Actions acceptance gates

The parallel build system is accepted when: two independent runs from the same commit produce equivalent package and ISO manifests; matrix failures are isolated and diagnosable; package artifacts can be assembled without rebuilding successful matrix jobs; ISO jobs consume exact upstream artifacts; QEMU smoke tests boot the produced ISO; release jobs can verify checksums and attestations; cancelled branch runs do not cancel release runs; and the Windows WSL2 local fallback can reproduce the same profile and package manifest.

'''
if needle not in s:
    raise SystemExit('global acceptance rule marker missing')
s = s.replace(needle, insert + needle, 1)
# Add references immediately before existing References section.
refs_marker = '\n# References\n'
refs = '\n[31]: https://docs.github.com/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow "GitHub Actions matrix strategies"\n[32]: https://docs.github.com/actions/concepts/security/artifact-attestations "GitHub Actions artifact attestations"\n[33]: https://docs.github.com/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds "GitHub Actions build provenance attestations"\n[34]: https://docs.github.com/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs "GitHub Actions concurrency"\n[35]: https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows "GitHub Actions reusable workflows"\n[36]: https://docs.github.com/en/actions/reference/limits "GitHub Actions limits"\n'
if refs_marker not in s:
    raise SystemExit('references section missing')
s = s.replace(refs_marker, refs + refs_marker, 1)
p.write_text(s)
print('Updated specification for GitHub Actions parallel builds')
