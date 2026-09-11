# Lesson 3: System Recovery and Diagnostics

When troubleshooting boot issues or unexpected behavior, Rain OS provides built-in recovery helpers.

## Checking System Health
```bash
rain-recovery status
```

## Collecting Diagnostics Privately
If you need assistance from the Rain OS community, generate a sanitized diagnostic report:
```bash
rain-recovery diagnose
```
This tool automatically scrubs private tokens, passwords, and authorization keys before saving the output.
