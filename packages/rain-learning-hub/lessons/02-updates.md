# Lesson 2: Updating Your System Safely

Rain OS is based on Arch Linux rolling releases, which means you receive the latest software updates continuously.

## How to Update
Always run the preflight verification before installing large updates:
```bash
rain-update-preflight
```

### What Preflight Checks
1. **Disk Space**: Ensures you have at least 2 GB of free space on your root drive to prevent failed installations.
2. **Keyring Validity**: Verifies cryptographic package signatures.
3. **Fallback Kernel**: Confirms that your fallback LTS kernel is ready in case a new kernel exhibits issues on your hardware.
