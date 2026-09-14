import os

SVGS = {
    "rain-control-center": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="neon" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00f0ff"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
  </defs>
  <rect width="472" height="472" x="20" y="20" rx="100" fill="url(#bg)" stroke="rgba(255,255,255,0.2)" stroke-width="8"/>
  <circle cx="256" cy="220" r="130" fill="none" stroke="url(#neon)" stroke-width="24" stroke-dasharray="580" stroke-dashoffset="140" stroke-linecap="round"/>
  <line x1="256" y1="220" x2="330" y2="150" stroke="#ffffff" stroke-width="18" stroke-linecap="round"/>
  <circle cx="256" cy="220" r="28" fill="#00f0ff"/>
  <line x1="140" y1="380" x2="372" y2="380" stroke="#64748b" stroke-width="12" stroke-linecap="round"/>
  <circle cx="210" cy="380" r="20" fill="#00f0ff"/>
  <line x1="140" y1="420" x2="372" y2="420" stroke="#64748b" stroke-width="12" stroke-linecap="round"/>
  <circle cx="310" cy="420" r="20" fill="#38bdf8"/>
</svg>""",

    "rain-installer": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#27272a"/>
      <stop offset="100%" stop-color="#18181b"/>
    </linearGradient>
    <linearGradient id="crimson" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f87171"/>
      <stop offset="100%" stop-color="#dc2626"/>
    </linearGradient>
  </defs>
  <rect width="472" height="472" x="20" y="20" rx="100" fill="url(#bg)" stroke="rgba(255,255,255,0.2)" stroke-width="8"/>
  <rect x="110" y="290" width="292" height="130" rx="20" fill="#334155" stroke="#94a3b8" stroke-width="8"/>
  <rect x="140" y="320" width="80" height="70" rx="8" fill="#0f172a"/>
  <rect x="250" y="320" width="120" height="70" rx="8" fill="#0f172a"/>
  <path d="M 230 100 L 282 100 L 282 200 L 340 200 L 256 270 L 172 200 L 230 200 Z" fill="url(#crimson)" stroke="#ffffff" stroke-width="6" stroke-linejoin="round"/>
</svg>""",

    "rain-welcome": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="amber" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
  </defs>
  <rect width="472" height="472" x="20" y="20" rx="100" fill="url(#bg)" stroke="rgba(255,255,255,0.2)" stroke-width="8"/>
  <polygon points="256,120 100,50 120,90" fill="url(#amber)" opacity="0.4"/>
  <polygon points="256,120 412,50 392,90" fill="url(#amber)" opacity="0.4"/>
  <polygon points="220,180 292,180 320,430 192,430" fill="#f8fafc"/>
  <polygon points="210,240 302,240 310,290 202,290" fill="#ef4444"/>
  <polygon points="196,350 316,350 320,390 192,390" fill="#ef4444"/>
  <circle cx="256" cy="140" r="45" fill="url(#amber)"/>
  <circle cx="256" cy="140" r="20" fill="#ffffff"/>
</svg>""",

    "rain-learning-hub": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#064e3b"/>
      <stop offset="100%" stop-color="#022c22"/>
    </linearGradient>
    <linearGradient id="emerald" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
  </defs>
  <rect width="472" height="472" x="20" y="20" rx="100" fill="url(#bg)" stroke="rgba(255,255,255,0.2)" stroke-width="8"/>
  <rect x="90" y="140" width="150" height="230" rx="15" fill="#f8fafc"/>
  <rect x="272" y="140" width="150" height="230" rx="15" fill="#f1f5f9"/>
  <line x1="256" y1="140" x2="256" y2="370" stroke="#64748b" stroke-width="12"/>
  <path d="M 120 210 L 160 235 L 120 260" fill="none" stroke="#10b981" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="175" y1="260" x2="215" y2="260" stroke="#34d399" stroke-width="16" stroke-linecap="round"/>
  <line x1="295" y1="180" x2="395" y2="180" stroke="#94a3b8" stroke-width="10" stroke-linecap="round"/>
  <line x1="295" y1="220" x2="395" y2="220" stroke="#94a3b8" stroke-width="10" stroke-linecap="round"/>
  <line x1="295" y1="260" x2="375" y2="260" stroke="#94a3b8" stroke-width="10" stroke-linecap="round"/>
</svg>""",

    "rain-desktop-selector": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2e1065"/>
      <stop offset="100%" stop-color="#18181b"/>
    </linearGradient>
    <linearGradient id="violet" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="100%" stop-color="#a855f7"/>
    </linearGradient>
  </defs>
  <rect width="472" height="472" x="20" y="20" rx="100" fill="url(#bg)" stroke="rgba(255,255,255,0.2)" stroke-width="8"/>
  <rect x="100" y="100" width="140" height="140" rx="20" fill="url(#violet)" stroke="#ffffff" stroke-width="10"/>
  <rect x="272" y="100" width="140" height="140" rx="20" fill="#334155" stroke="#64748b" stroke-width="8"/>
  <rect x="100" y="272" width="140" height="140" rx="20" fill="#334155" stroke="#64748b" stroke-width="8"/>
  <rect x="272" y="272" width="140" height="140" rx="20" fill="#334155" stroke="#64748b" stroke-width="8"/>
  <line x1="125" y1="140" x2="215" y2="140" stroke="#ffffff" stroke-width="8" stroke-linecap="round"/>
  <rect x="125" y="160" width="40" height="50" rx="6" fill="#ec4899"/>
  <rect x="175" y="160" width="40" height="50" rx="6" fill="#ffffff"/>
</svg>""",

    "rain-store": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="indigo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#4f46e5"/>
    </linearGradient>
  </defs>
  <rect width="472" height="472" x="20" y="20" rx="100" fill="url(#bg)" stroke="rgba(255,255,255,0.2)" stroke-width="8"/>
  <path d="M 190 190 C 190 120, 322 120, 322 190" fill="none" stroke="#38bdf8" stroke-width="20" stroke-linecap="round"/>
  <rect x="110" y="180" width="292" height="250" rx="30" fill="url(#indigo)" stroke="#ffffff" stroke-width="6"/>
  <path d="M 256 240 C 256 240, 216 300, 216 330 C 216 352, 234 370, 256 370 C 278 370, 296 352, 296 330 C 296 300, 256 240, 256 240 Z" fill="#38bdf8"/>
</svg>""",

    "rain-hardware": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#292524"/>
      <stop offset="100%" stop-color="#171717"/>
    </linearGradient>
    <linearGradient id="amber" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fb923c"/>
      <stop offset="100%" stop-color="#ea580c"/>
    </linearGradient>
  </defs>
  <rect width="472" height="472" x="20" y="20" rx="100" fill="url(#bg)" stroke="rgba(255,255,255,0.2)" stroke-width="8"/>
  <rect x="136" y="136" width="240" height="240" rx="30" fill="#1e293b" stroke="url(#amber)" stroke-width="14"/>
  <rect x="196" y="196" width="120" height="120" rx="16" fill="url(#amber)"/>
  <line x1="200" y1="136" x2="200" y2="70" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="256" y1="136" x2="256" y2="70" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="312" y1="136" x2="312" y2="70" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="200" y1="376" x2="200" y2="442" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="256" y1="376" x2="256" y2="442" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="312" y1="376" x2="312" y2="442" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="136" y1="200" x2="70" y2="200" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="136" y1="256" x2="70" y2="256" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="136" y1="312" x2="70" y2="312" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="376" y1="200" x2="442" y2="200" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="376" y1="256" x2="442" y2="256" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
  <line x1="376" y1="312" x2="442" y2="312" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
</svg>""",

    "rain-display": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0c4a6e"/>
      <stop offset="100%" stop-color="#082f49"/>
    </linearGradient>
    <linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>
  <rect width="472" height="472" x="20" y="20" rx="100" fill="url(#bg)" stroke="rgba(255,255,255,0.2)" stroke-width="8"/>
  <rect x="70" y="160" width="170" height="130" rx="14" fill="#0f172a" stroke="url(#sky)" stroke-width="10"/>
  <rect x="85" y="175" width="140" height="100" rx="6" fill="#1e3a8a"/>
  <rect x="272" y="160" width="170" height="130" rx="14" fill="#0f172a" stroke="#93c5fd" stroke-width="10"/>
  <rect x="287" y="175" width="140" height="100" rx="6" fill="#0369a1"/>
  <line x1="256" y1="290" x2="256" y2="370" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
  <line x1="170" y1="370" x2="342" y2="370" stroke="#94a3b8" stroke-width="16" stroke-linecap="round"/>
</svg>"""
}

def main():
    target_dirs = [
        r"E:\rain os\branding\icons",
        r"E:\rain os\archiso\airootfs\usr\share\icons\hicolor\scalable\apps",
        r"E:\rain os\packages\rain-branding\icons\scalable\apps"
    ]
    for d in target_dirs:
        os.makedirs(d, exist_ok=True)
        
    for name, content in SVGS.items():
        for d in target_dirs:
            p = os.path.join(d, f"{name}.svg")
            with open(p, "w", encoding="utf-8") as f:
                f.write(content)
        print(f"Generated scalable vector SVG for {name}")

if __name__ == "__main__":
    main()
