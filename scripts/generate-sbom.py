#!/usr/bin/env python3
"""
Rain OS Software Bill of Materials (SBOM) Generator
Generates an SPDX / CycloneDX compatible JSON manifest of all bundled packages.
(Spec Page 30 & 118)
"""
import os
import sys
import json
from datetime import datetime, timezone

def generate_sbom(packages_file, output_file):
    if not os.path.exists(packages_file):
        print(f"Error: {packages_file} does not exist", file=sys.stderr)
        return False

    with open(packages_file, "r", encoding="utf-8") as f:
        pkg_names = [line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")]

    now = datetime.now(timezone.utc).isoformat()

    components = []
    # Rain OS Core Packages
    rain_packages = [
        ("rain-branding", "1.2.1", "GPL-3.0-or-later", "Rain OS visual assets, wallpapers, and desktop themes"),
        ("rain-first-run", "1.2.1", "GPL-3.0-or-later", "Welcome assistant, baseline hardware inspector, and onboarding"),
        ("rain-control-center", "1.2.1", "GPL-3.0-or-later", "Unified system control center, profiles, and software hub"),
        ("rain-learning-hub", "1.2.1", "GPL-3.0-or-later", "Offline curriculum, signed guide index, and rain-guide viewer"),
        ("rain-recovery-tools", "1.2.1", "GPL-3.0-or-later", "Health diagnostics, log secret scrubber, and Btrfs rollback guide"),
        ("rain-update-preflight", "1.2.1", "GPL-3.0-or-later", "Pre-transaction safety checks and snapshot verifier"),
        ("rain-probe", "1.2.1", "GPL-3.0-or-later", "High-performance native C hardware and display probe"),
        ("rain-desktop-selector", "1.2.1", "GPL-3.0-or-later", "CachyOS-style Desktop Environment and Window Manager Selector with Omarchy themes")
    ]

    for name, ver, lic, desc in rain_packages:
        components.append({
            "type": "application",
            "name": name,
            "version": ver,
            "publisher": "Rain OS Contributors",
            "licenses": [{"license": {"id": lic}}],
            "description": desc,
            "origin": "rain-os-core-repository"
        })

    # Upstream Packages from packages.x86_64
    for pkg in pkg_names:
        components.append({
            "type": "library" if "lib" in pkg else "operating-system",
            "name": pkg,
            "version": "rolling",
            "publisher": "Arch Linux Upstream",
            "licenses": [{"license": {"id": "OpenSource"}}],
            "origin": "https://archlinux.org/packages/"
        })

    sbom = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.5",
        "serialNumber": f"urn:uuid:rain-os-sbom-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "version": 1,
        "metadata": {
            "timestamp": now,
            "tools": [{"vendor": "Rain OS", "name": "rain-sbom-generator", "version": "1.0.0"}],
            "component": {
                "type": "operating-system",
                "name": "Rain OS",
                "version": "1.0.0",
                "description": "Independent commercial-grade desktop Linux distribution with Btrfs safety and app compatibility."
            }
        },
        "components": components
    }

    os.makedirs(os.path.dirname(output_file) or ".", exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(sbom, f, indent=2)

    print(f"Successfully generated SBOM with {len(components)} components -> {output_file}")
    return True

if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pkg_file = os.path.join(root, "archiso", "packages.x86_64")
    out_file = os.path.join(root, "out", "rain-os-sbom.json")
    if "--test" in sys.argv:
        out_file = os.path.join(root, "docs", "rain-os-sbom.example.json")
    generate_sbom(pkg_file, out_file)
