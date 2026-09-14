# GitHub Actions Policy

- Never trigger or dispatch any GitHub Actions workflows automatically.
- Always ask the user for explicit permission before initiating any GitHub Actions build or validation.
- All GitHub workflows must remain manual (`workflow_dispatch` only).
