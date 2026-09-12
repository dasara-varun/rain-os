from pathlib import Path
import subprocess
spec = Path('/home/ubuntu/rain-os-spec/Rain-OS-Commercial-Build-Spec.md')
repo = Path('/home/ubuntu/rain-os-public')
s = spec.read_text()
marker = '\n\\\\newpage\n\n# Architecture diagrams\n'
files = sorted(str(p.relative_to(repo)) for p in repo.rglob('*') if p.is_file() and '.git' not in p.parts)
lines = ['\\newpage', '', '# Appendix A: Complete public repository inventory', '', 'The following inventory was generated from the shallow clone used for this audit. It is included so that the next implementation loop can map every current file to an owner, test, license record, and disposition.', '', '| Path | Current role | Required disposition |', '|---|---|---|']
for f in files:
    if f.startswith('archiso/'):
        role, disp = 'Archiso profile, package, or live-image input', 'Keep only after current Archiso compatibility test'
    elif f.startswith('packages/'):
        role, disp = 'Rain package recipe or installed helper', 'Build in clean makepkg; replace SKIP checksums before release'
    elif f.startswith('apps/'):
        role, disp = 'Prototype graphical application or documentation', 'Add functional and accessibility tests; avoid placeholder actions'
    elif f.startswith('scripts/') or f.startswith('repository/'):
        role, disp = 'Build, repository, or orchestration script', 'Shellcheck, fail closed, remove tolerated build failures'
    elif f.startswith('.github/'):
        role, disp = 'Continuous integration workflow', 'Pin actions and add ISO boot/install/recovery gates'
    elif f.startswith('docs/') or f.startswith('manifests/') or f.startswith('design/') or f.startswith('qa/') or f.startswith('architecture/'):
        role, disp = 'Specification, design, architecture, or QA artifact', 'Map to one release requirement and maintain with implementation'
    elif f.startswith('branding/'):
        role, disp = 'Branding or wallpaper asset', 'Record copyright and license; test theme packaging'
    else:
        role, disp = 'Project governance or root configuration', 'Review for commercial release policy'
    lines.append(f'| `{f}` | {role} | {disp} |')
lines += ['', '## Audit observations', '', 'The inventory demonstrates that Rain OS is a prototype repository with meaningful integration work, not a complete distribution. It has a live Archiso profile and several Rain package recipes, but an ISO can only be considered a commercial build after the package repository, installer behavior, guide updater, signatures, hardware tests, and recovery tests are real and reproducible.', '', 'The most important corrective actions are to stop tolerating package build failures, replace `SKIP` checksums with generated checksums or an explicit source integrity mechanism, keep the build tree inside WSL, separate the public prototype from release signing material, test every GUI path against the installed binaries it launches, and introduce a release manifest that ties every package and configuration file to a tested artifact.']
append = '\n'.join(lines) + '\n'
if marker not in s:
    raise SystemExit('architecture marker not found')
s = s.replace(marker, '\n' + append + marker, 1)
spec.write_text(s)
print(f'Inserted inventory for {len(files)} files')
