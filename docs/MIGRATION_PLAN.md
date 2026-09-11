# Rain OS Upstream Migration Plan

## Stage A: establish a clean baseline

Build a stock-derived Core ISO with no custom kernel and no imported third-party repository. Record boot time, memory usage, install time, package count, boot failures, and user friction. This is the comparison baseline.

## Stage B: add one component at a time

Introduce one reused component per iteration. After each change, compare package ownership, services, files, boot behavior, update behavior, and rollback behavior. Never add the CachyOS kernel, an Athena repository, and a new hardware detector in one iteration.

## Stage C: wrap without hiding

When Rain adds a GUI action around an upstream command, display the command’s source package, current state, intended change, and rollback action. Log the exit code and preserve the upstream log.

## Stage D: convert configuration into profiles

CachyOS-inspired settings become Rain Flow profile files. Athena-inspired security settings become Rain Shield policy files. Profiles must have apply, inspect, and remove operations. Applying a profile twice must be idempotent.

## Stage E: promote only after evidence

A component moves from experimental to supported only after VM tests, hardware tests, package-update tests, rollback tests, documentation, owner assignment, and a source/provenance record.

## Stage F: remove accidental dependencies

Before release, inspect the dependency graph and service list. Remove duplicated firewalls, unnecessary daemons, unmaintained helpers, and packages included only because a profile was tested on the build host.

## Migration checklist

- [ ] Source URL and license recorded.
- [ ] Exact version or commit pinned.
- [ ] Package ownership assigned.
- [ ] Local patches listed.
- [ ] Service and file conflicts checked.
- [ ] Install and uninstall tested.
- [ ] Update and rollback tested.
- [ ] User-facing explanation written.
- [ ] Security impact reviewed.
- [ ] Removal or upstreaming plan recorded.
