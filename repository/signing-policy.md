# Rain OS Repository Signing Policy

## Principles
1. **Never commit private keys**: Private signing keys must never be committed to Git or stored in ISO images.
2. **Key Separation**: Separate keys are used for the official `rain-core` repository, experimental `rain-testing`, and ISO release media.
3. **Public Key Distribution**: Public keys are packaged inside `archlinux-keyring` or `rain-keyring` and installed into `/etc/pacman.d/gnupg/`.
4. **Key Rotation**: Keys must be rotated every 24 months with a 6-month signature overlap window.
