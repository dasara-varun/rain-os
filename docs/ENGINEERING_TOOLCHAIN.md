# Rain OS AI Engineering Toolchain

## Scope

The requested repositories and skills belong in the **Rain OS Builder Toolkit**, not in the runtime OS. They help the project plan, implement, review, test, document, and iterate on Rain OS. They must never be required to boot the ISO or update a user’s desktop.

## Integration matrix

| Tool | Source | Proposed use in Rain OS | License / status | Safety boundary |
|---|---|---|---|---|
| ECC | https://github.com/affaan-m/ECC | Research-first development, skills, memory, security and TDD patterns | MIT; audit before use | Install only in builder environment; use official source; review hooks and MCP configs |
| gstack | https://github.com/garrytan/gstack | Product, engineering, design, QA, security, release and documentation review roles | MIT; audit before use | Do not auto-run deploy or browser actions; require review gates |
| taste-skill | https://github.com/Leonxlnx/taste-skill | Rain Control Center and theme UX review; anti-generic visual design | MIT; install via `npx skills add` | Design guidance only; no runtime OS dependency |
| ponytail | https://github.com/DietrichGebert/ponytail | YAGNI, reuse-first, minimal implementation, over-engineering review | MIT; audit hooks | Never sacrifice security, error handling, accessibility, or recovery |
| headroom | https://github.com/headroomlabs-ai/headroom | Local context compression for large docs/logs during development | Apache-2.0 | Local-only mode preferred; inspect proxy/MCP configuration; reversible |
| my-claude-code-setup | https://github.com/centminmod/my-claude-code-setup | Memory-bank templates, project instructions, progressive disclosure | MIT; template source | Copy only reviewed templates; do not import platform credentials or unsafe settings |
| Get Shit Done Core | https://github.com/open-gsd/gsd-core | Discuss → plan → execute → verify → ship phase loop | MIT; current source after repository move | Pin version; require human review before releases |
| skill-find | https://github.com/vercel-labs/skills | Discover relevant agent skills for a specific build task | Verify current license/version | Recommendations only; never install arbitrary skills without review |
| Ralph loop | https://github.com/frankbria/ralph-claude-code or an equivalent reviewed implementation | Bounded repeated implementation/test cycles for one issue | Review exact implementation before adoption | Hard iteration limit, no destructive commands, stop on repeated failure |
| “Everything Claude Code” | Project-specific umbrella label | Maintain a curated catalog of Claude Code rules, skills, agents, hooks, and commands | No single canonical source identified | Treat as a catalog, not a single trusted package; pin each item separately |

## Recommended builder profile

Use one orchestrator, not every tool at once. The suggested stack is GSD Core for phases, ECC for research/TDD/security patterns, gstack for cross-functional review, taste-skill for Control Center design, ponytail for over-engineering review, and Headroom only when local context volume justifies it.

## Installation policy

External tools are installed in a separate builder environment or project-local `.builder/` directory. Each installation records URL, commit/version, license, checksum, install command, enabled hooks, and uninstall command in `manifests/BUILDER_TOOLS.csv`.

Do not run `npx`, `curl | sh`, plugin installers, or unknown hooks with root privileges. Review scripts before execution. Do not place AI-agent configuration in the ISO image.

## Approval gates

- **Plan gate:** GSD/ECC plan is reviewed before implementation.
- **Design gate:** gstack/taste review checks clarity, accessibility, and consistency.
- **Minimality gate:** ponytail review proposes removals but cannot remove required safety behavior.
- **Security gate:** ECC/gstack security review checks trust boundaries, package signing, update paths, and secrets.
- **QA gate:** automated VM tests and hardware tests must pass.
- **Release gate:** human maintainer reviews ISO contents, provenance, signatures, and recovery behavior.

## Fallback

Rain OS development must remain possible with Git, shell, Archiso, tests, and Markdown alone. No agent skill or AI tool is a release prerequisite.
