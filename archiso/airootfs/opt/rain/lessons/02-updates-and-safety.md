# Lesson 2: Safe Updates and System Health

Rain OS inherits the latest software from Arch Linux. To ensure your system remains completely stable, Rain OS provides preflight checks and safety guardrails.

## Safe Update Checklist
1. **Never kill an active package upgrade**: Interrupting a transaction can leave libraries half-written.
2. **Review the Preflight Report**: Before updating, Rain OS checks disk space, key validity, and database integrity.
3. **Dual Kernel Protection**: Rain OS ships both `linux` and `linux-lts`. If a kernel driver has a regression, reboot and select the LTS kernel in the bootloader menu.

## Guided Practice: Running Update Preflight
Run the following command to check your update health without modifying any files:
```bash
rain-update-preflight
```
You will see:
- Available disk space on `/` and `/boot`
- Status of pacman keyring and lockfiles
- Installed kernel fallbacks

To apply updates safely through Rain OS:
```bash
sudo pacman -Syu
```
Before transactions begin, Rain OS automatically invokes `rain-btrfs-snapshot` to safeguard your system.
