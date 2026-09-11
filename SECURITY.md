# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

---

## Security Philosophy

Rain OS is built with the principle of **Security Honesty**:
- Distinguish between **active**, **available**, and **unsupported** protections in all user interfaces.
- The Core profile is focused on baseline desktop hardening: active firewall, secure package signatures, optional LUKS2 full-disk encryption, and immutable fallback kernels.
- Offensive tools and aggressive testing suites are never pre-installed in the Core profile; they belong exclusively in the isolated, opt-in **Rain Shield** profile.
- Privileged operations use PolicyKit with explicit policy actions, avoiding GUI-run-as-root antipatterns.

---

## Reporting a Vulnerability

If you discover a security vulnerability within Rain OS or any of its integration packages:

1. **Do not** create a public GitHub issue.
2. Please privately report the issue via GitHub's **Security Advisories** tab on the repository:
   https://github.com/dasara-varun/rain-os/security/advisories
3. Provide:
   - Detailed description of the vulnerability.
   - Steps to reproduce or proof-of-concept.
   - Potential impact on system integrity, user privacy, or privilege boundaries.
   - Affected versions or profiles.

We will acknowledge receipt within 48 hours and work with you on an coordinated remediation and disclosure schedule.
