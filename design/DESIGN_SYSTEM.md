# Rain OS Design System

## Brand idea

Rain OS uses an umbrella as a symbol of **shelter, reliability, and user control**. The visual language is based on real rain environments: city streets, rural fields, coastlines, forests, and night skies. It must never use monsters, skulls, aggressive hacker imagery, or fantasy threat motifs.

## Theme family

Themes are environmental skins over one accessible component system. They change wallpaper, accent, illustration, and subtle surface tones. They do not change security settings or system behavior.

| Theme | Character | Palette direction | Best use |
|---|---|---|---|
| **Urban Rain** | Dark slate, silver-white canopy panels, crimson inner accent, white handle | Slate (#1E222B), crimson (#E83E38), silver, crisp white | Default desktop and productivity |
| **Rural Rain** | Fields, hedgerows, farm roads, soft overcast skies | Moss, clay, cloud grey, muted blue | Calm workspaces and low-distraction use |
| **Coastal Rain** | Sea mist, rain on glass, grey horizon, lighthouse accents | Deep navy, sea teal, foam, warm beacon amber | Dark mode and widescreen desktops |
| **Forest Rain** | Leaves, shaded paths, clean water, diffuse light | Pine, fern, water blue, soft stone | Focus and reading |
| **Monsoon Rain** | Dense rainfall, covered walkways, saturated greenery, warm shelter | Indigo, teal, leaf green, terracotta | High-energy but non-aggressive accent theme |
| **Night Rain** | Street reflections and quiet nighttime rain | Blue-black, cyan, soft white, restrained amber | Dark-mode default |
| **Clear Sky** | Bright post-rain light and clean surfaces | White, sky blue, deep ink, green status | Light-mode default |
| **Monsoon High Contrast** | Reduced decorative detail with strong boundaries | High-contrast ink, blue, yellow, white | Accessibility mode |

## Theme rules

Urban and rural are the two launch themes. Coastal, Forest, Monsoon, and Night may ship as later wallpaper and color packs. Themes must not imply geography, class, weather safety, or personality stereotypes. Use abstract environmental imagery and avoid tiny text in wallpapers.

The umbrella mark remains the same across themes. Theme changes are reversible and stored in desktop settings. Theme assets should be original or openly licensed, with attribution in `rain-branding`.

## Palette tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `rain-ink` | `#17212B` | `#F4F8FB` | Primary text |
| `rain-slate` | `#F0F4F8` | `#1E222B` | Canvas and window backgrounds |
| `rain-sky` | `#1769AA` | `#72C7FF` | Links and secondary action |
| `rain-cloud` | `#E8F0F5` | `#282D37` | Surfaces and cards |
| `rain-water` | `#D3EEF7` | `#383E4C` | Borders and informational background |
| `rain-moss` | `#396A52` | `#8AC9A2` | Rural/forest accent |
| `rain-coast` | `#0F4C5C` | `#63D5D0` | Coastal accent |
| `rain-amber` | `#B66A00` | `#FFC45C` | Caution and performance |
| `rain-red` | `#B42318` | `#E83E38` | Signature umbrella accent and active highlights |
| `rain-green` | `#18794E` | `#65D69B` | Healthy/success |

## Typography, components, and accessibility

Use a readable sans-serif UI family with a monospaced companion for code. Minimum body size is 14px equivalent. Focus rings must be at least 2px and visible against both light and dark surfaces. Respect reduced-motion settings. Do not use animated rain as a background. Status uses icon, text, and color together.

Every action that changes the system uses a title, impact statement, current state, proposed state, risk, backup/rollback option, primary action, secondary action, and help link. The UI must never make a theme choice look like a security or performance change.

## Umbrella logo usage

Use the umbrella symbol alone at small sizes. Use the wordmark only when adequate horizontal space exists. Never stretch the mark, add a drop shadow, or recolor the mark outside the palette without an explicit theme token.
