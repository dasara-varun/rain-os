# Rain OS Desktop Environment Strategy

## Recommendation

Rain OS should support familiar environments through package groups and a single installer choice, but it should not ship every environment in the Core ISO. Each environment changes default services, settings, accessibility behavior, display protocols, and support work.

## Supported environment tiers

### Launch-supported

| Environment | Audience | Rain support plan |
|---|---|---|
| **KDE Plasma** | Familiar, full-featured desktop users | Default Core environment; Urban Rain and Rural Rain themes first |
| **GNOME** | Users who prefer a focused, modern workflow | Supported package group and guide; separate test profile |
| **XFCE** | Older hardware and traditional desktop users | Supported lightweight profile |
| **Cinnamon** | Users seeking a familiar Windows-like desktop | Supported community profile after installer and update tests |

### Community-supported after Core

| Environment | Audience | Caution |
|---|---|---|
| **MATE** | Traditional desktop users and modest hardware | Smaller upstream ecosystem than KDE/GNOME |
| **LXQt** | Very low resource systems | Some integrations need additional testing |
| **Budgie** | Simple modern desktop | Smaller maintainer/support surface |
| **COSMIC** | Users interested in a modern Rust desktop | Available via `rain-profile set cosmic` or `rain-install-cosmic` |

### Experimental / advanced

| Environment | Audience | Caution |
|---|---|---|
| **Hyprland** | Wayland power users | Configuration-heavy and not a beginner default |
| **Sway** | Keyboard-driven Wayland users | Requires user configuration and different workflows |
| **i3** | Tiling/X11 users | Advanced; not a full desktop replacement without setup |
| **Niri** | Scrolling Wayland users | Experimental support and evolving ecosystem |

## Installer behavior

The installer presents one recommended Core environment and an expandable list of additional environments. It shows disk size, installed services, login manager choice, and support tier. It does not present ten environments as equally supported.

The first ISO should ship KDE Plasma only unless a hardware or user study demonstrates that GNOME must be co-shipped. XFCE, GNOME, Cinnamon, and the remaining options can be tested as package profiles and later ISO variants.

## Environment contract

Each supported environment requires an install/remove package group, a default theme mapping, display-manager behavior, network/audio integration, suspend/logout tests, accessibility tests, guide pages, screenshot/UX review, and an owner. Removing an environment must not remove the Core package manager, recovery tools, or the user’s guide.

## Theme mapping

Urban Rain is the default KDE/GNOME productivity theme. Rural Rain is available in every supported environment. Coastal, Forest, Monsoon, Night, and Clear Sky are wallpaper and color packs and do not change system behavior.

## Known drawbacks

More environments increase ISO size, testing cost, conflicting settings, and support ambiguity. Rain OS should prefer **wide package availability with narrow official support** over claiming every desktop is equally integrated.
