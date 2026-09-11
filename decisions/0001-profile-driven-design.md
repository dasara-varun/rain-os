# ADR 0001: Profile-driven design instead of a merged maximalist distro

**Status:** Accepted for v1

## Context

EndeavourOS, CachyOS, and Athena OS solve different problems. A single default installation containing all of their components would create large package, testing, support, and security costs.

## Decision

Rain OS uses a small Arch-compatible Core and opt-in profiles: Flow, Forge, Shield, and Pocket. Profiles are packages and configuration, not separate distributions.

## Consequences

Users get a predictable starting point and can add capability without reinstalling. Maintainers must define profile contracts, test installation/removal, and preserve a working Core fallback. Some advanced features will not be active by default.
