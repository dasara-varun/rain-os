---
name: git-github-manager
description: Manage the full git and GitHub lifecycle — branching, staging, committing, pushing, resolving conflicts, rebasing/history cleanup, opening and reviewing pull requests, managing issues, dependency/package management, and cutting releases/tags. Commits often, after every small notable change (a fixed bug, a finished function, a passing test, a small refactor), so history stays fine-grained and easy to track, bisect, and roll back if something breaks — and pushes regularly so the remote stays close to current. Allows multiple parallel working branches at once, while `main`/`master` always stays deployable and holds only verified, working code. Also handles package/dependency updates and lockfile hygiene, semantic versioning and changelogs, CI status checks, and common gotchas (uncommitted work lost on branch switch, detached HEAD, stale/diverged branches, secrets in history, force-push risk, submodule/LFS drift, silent CI failures). Use this skill whenever the user asks to commit, branch, push, open a PR, review a diff, resolve a merge conflict, rebase, squash commits, update dependencies, tag a release, or manage GitHub issues/PRs — even if they just say "commit this," "push my changes," "make a PR," "bump the version," or "clean up my branches," without naming git or GitHub explicitly. Also use for repo hygiene tasks like writing a .gitignore, undoing a commit, recovering lost commits, or investigating history with git log/blame.
---

# Git & GitHub Manager

Handles the full lifecycle of working in a git repo and on GitHub: local changes → commits → branches → PRs → issues → dependencies → releases.

## Setup check (do this first)

Before doing anything, confirm the environment:

```bash
git rev-parse --is-inside-work-tree 2>&1   # confirms we're in a repo
git status --short                          # see what's changed
git branch --show-current                   # current branch
git fetch --quiet 2>&1                      # sync remote-tracking refs before deciding anything
```

For anything touching GitHub itself (PRs, issues, releases, forks), check whether the `gh` CLI is available and authenticated:

```bash
gh auth status 2>&1
```

- If `gh` is available and authenticated, use it for all GitHub-side operations (PRs, issues, releases) — it's more reliable than scraping web UI conventions and handles auth automatically.
- If `gh` is not installed or not authenticated, fall back to plain `git` for everything local (commits, branches, pushes), and tell the user what's missing for the GitHub-side parts (e.g. "I don't see `gh` authenticated — I can push the branch, but you'll need to open the PR yourself, or authenticate `gh` first with `gh auth login`").
- Never invent a GitHub URL, PR number, or issue number — only report links/numbers that a command actually returned.

## Core principles

1. **Commit often, after every small notable change (fine-grained commit cadence).** Don't let work accumulate uncommitted across multiple edits. As soon as a small, coherent piece of work lands — a bugfix, one function or component, a passing test, a small refactor, a docs tweak, a config change — stage and commit it right away, rather than waiting to batch several unrelated changes into one large commit. Small, frequent commits keep history easy to read and `git bisect`/`git blame` through, make code review effortless, and mean that if something breaks, `git revert <commit-hash>` or `git reset` can roll back precisely the one thing that caused it instead of a large bundled change. Never commit a broken or half-finished intermediate state, though — "small" means small in scope, not incomplete.
2. **Push regularly, so the remote stays close to current.** Push after a commit or a small cluster of related commits — don't stockpile a long run of unpushed local commits. Frequent pushes give a real-time remote backup, let CI catch problems as they happen instead of in one big batch, and avoid painful divergence from teammates or other agents working on the same repo. Use judgment on exact frequency (e.g. batch a few fixups together rather than pushing after literally every keystroke-level change), but the default should be push soon after committing, not "at the end of the session."
3. **Multiple branches can run in parallel — that's expected and encouraged.** Use branches liberally for features, fixes, experiments, and agent-driven work streams. There's no need to funnel everything through one branch or ask permission to create another one for a distinct piece of work. Name them clearly so it's obvious what each is for, and keep track of which branch each task belongs to.
4. **`main` (or `master`) is always the single source of truth for final, working code.** No matter how many branches are open, `main` must always be deployable — it reflects only code that has been verified (tests pass, builds, reviewed if applicable). Never commit directly to `main` for anything beyond trivial fixes (typos, docs) without checking with the user first. Merge into `main` only from a verified branch.
5. **Never force-push or rewrite shared history without explicit confirmation.** `push --force`, `rebase` on a branch others may have pulled, `reset --hard`, and deleting branches are all destructive. Show the user what will happen (e.g. `git log` of what's about to be lost) and get a clear go-ahead first, unless they already gave a blanket instruction in this conversation. This applies doubly to `main`.
6. **Always show a diff or status before committing.** Run `git status` and `git diff` (or `git diff --staged` once staged) and briefly summarize what's changing before writing a commit. Don't stage/commit blind.
7. **Never commit secrets, credentials, or generated artifacts.** If a diff includes what looks like an API key, token, password, `.env` contents, or a large build artifact/binary, flag it and ask before committing, even if the user didn't ask you to check.
8. **Write commit messages from the actual diff, not the request.** Base the message on what the code changes actually do, in imperative mood ("Add", "Fix", "Refactor"), not a restatement of the user's instruction. Use Conventional Commits (`feat:`, `fix:`, `refactor:`, `style:`, `test:`, `docs:`, `chore:`, `build:`, `perf:`, `ci:`) since it also drives changelog and semver automation.
9. **Keep commits small and strictly atomic.** Each commit should represent a single logical change — the smaller and more self-contained, the easier it is to review, bisect, and revert. If unrelated changes are present, stage and commit them separately in sequence, pushing after each one, rather than bundling them into one larger commit.
10. **Before merging into `main` or opening a PR, verify it actually works.** Run the project's test/build/lint commands if they exist (e.g. `npm test`, `npm run build`, `npm run lint`, `pytest`, `flutter analyze`, `flutter test`, `dart test`, `cargo test`, `cargo clippy`) so that anything landing on `main` is green and deployable. Check CI status too, don't rely only on local runs.
11. **Keep dependencies deliberate and lockfiles honest.** Package/dependency changes (adding, removing, or bumping a library) are their own atomic commit, never bundled silently into an unrelated feature commit. Always update the lockfile alongside the manifest in the same commit (see "Package & dependency management" below).
12. **One clarifying question max, and only if truly ambiguous** (e.g. "push my changes" with no upstream configured yet, multiple remotes, or which of several open branches to act on). Otherwise proceed and state the assumption inline (e.g. "pushing to origin/main since that's the current upstream", "working on `feat/csv-export` since that's the branch with your in-progress changes").

## Common workflows

### The small-commit loop

For any unit of work, repeat this loop rather than doing one large commit at the end:

1. **Finish one small, working piece** (a bugfix, one function/component, a passing test, a small refactor).
2. **Check it**: run relevant fast tests/lint if available.
3. **Inspect**: `git status --short` and `git diff` to confirm exactly what changed.
4. **Stage and commit atomically**: `git add <files>` then `git commit -m "<type>(<scope>): <what this piece does>"`.
5. **Push soon after**: `git push` (or batch a couple of related commits, then push).
6. **Move to the next small piece** and repeat.

This keeps every change independently identifiable and revertible — if something later breaks, `git bisect` or a targeted `git revert <hash>` can isolate and undo exactly the commit at fault instead of a large mixed change.

### Committing changes

```bash
git status --short
git diff                      # unstaged
git add <files>                # prefer explicit paths over `git add .` unless the user wants everything
git diff --staged             # confirm what's about to be committed
git commit -m "<type>(<scope>): <concise, descriptive summary of this exact change>"
```

For multi-line commit messages, use a heredoc so quoting doesn't break:
```bash
git commit -m "$(cat <<'EOF'
Short summary line

Longer explanation if needed.
EOF
)"
```

### Pushing (regular, soon after committing)

```bash
git push -u origin <branch-name>     # first push of a new branch
git push                              # run again soon after each commit or small cluster of commits
```

Before pushing, `git fetch` and check ahead/behind status so pushes don't get surprise-rejected mid-task. If the push is rejected (non-fast-forward), do NOT force-push automatically — explain that the remote has commits the local branch doesn't, and offer `git pull --rebase` (rewrites local commits on top of remote) vs `git merge` (creates a merge commit) as options, unless the user has a standing preference.

### Branching (multiple branches, managed cleanly)

```bash
git branch --show-current
git checkout -b <type>/<short-description>        # or: git switch -c <type>/<short-description>
git branch -a                                       # see all branches (local + remote) before naming a new one
```

- **Before starting any nontrivial work**, check the current branch. If it's `main`, create a new branch first rather than working directly on it.
- **Running several branches at once is normal.** One per feature, fix, experiment, or parallel agent task-stream. Keep a mental (or, if asked, written) map of what each open branch is for so nothing gets lost or duplicated.
- Branch naming: if the repo has an existing convention (check `git branch -a` / recent branch names), follow it. Otherwise default to `<type>/<short-description>` (e.g. `fix/login-redirect`, `feat/csv-export`, `chore/bump-deps`).
- **Keep long-lived branches in sync with `main`** to avoid painful conflicts later — periodically merge or rebase `main` into a branch (`git merge main` or `git rebase main` while on the branch), especially before opening a PR.
- **Only merge into `main` when the branch is verified working** — tests pass, it builds, and (if using PRs) it's been reviewed/approved. Prefer merging via `gh pr merge` (or a PR merge on GitHub) over merging locally and pushing directly to `main`, so there's a review record and CI gets a chance to run.
- **Clean up after merging.** Once a branch is merged into `main`, delete it (locally and on the remote) so the branch list doesn't accumulate stale clutter:
  ```bash
  git branch -d <branch-name>                 # local, only if merged
  git push origin --delete <branch-name>       # remote
  gh pr merge <number> --delete-branch          # does both in one step, via gh
  ```
- Periodically sweep for stale branches already merged into `main` and offer to clean them up: `git branch --merged main`.
- **Hotfix pattern:** for an urgent fix to already-released code, branch from the release tag or `main` as `hotfix/<description>`, fix, verify, merge back into `main` (and into any active release branch), and tag a patch release.
- **If asked to "fix something quickly on main"**, still push back gently: suggest a short-lived branch even for small fixes, unless the user explicitly overrides.

### Opening a pull request (via `gh`)

```bash
gh pr create --title "<title>" --body "<description>" --base <base-branch>
```

- Derive the title/body from the actual commits on the branch (`git log <base>..HEAD --oneline`), not just the user's one-line request.
- If the repo has a PR template (`.github/PULL_REQUEST_TEMPLATE.md`), read it and fill it in rather than ignoring it.
- Push the branch first if it isn't already on the remote.
- Report back the PR URL that `gh` returns — don't construct one manually.

Reviewing/checking PRs:
```bash
gh pr list
gh pr view <number> --comments
gh pr diff <number>
gh pr checks <number>
```

### Resolving merge conflicts

```bash
git status                     # shows conflicted files
```
For each conflicted file: read the `<<<<<<<` / `=======` / `>>>>>>>` markers, understand both sides' intent (check `git log` on both branches if unclear), and produce a merged version that preserves both changes' intent rather than blindly picking one side. Show the user the resolution for anything non-trivial before finalizing. Then:
```bash
git add <resolved-file>
git commit            # for a merge; or `git rebase --continue` mid-rebase
```

### Rebasing / cleaning up history

Only do this on branches the user confirms are theirs alone (not shared/already-reviewed), or with explicit confirmation:

```bash
git rebase -i <base-branch>          # interactive: reorder, squash, reword
git rebase <base-branch>             # replay commits on top of latest base
```

After a rebase that's already been pushed once, the follow-up push needs:
```bash
git push --force-with-lease          # safer than --force: fails if remote has new commits you haven't seen
```
Always prefer `--force-with-lease` over `--force`, and always confirm with the user before force-pushing at all.

### Undoing things

- Uncommitted changes to a file: `git restore <file>` (or `git checkout -- <file>` on older git)
- Unstage but keep changes: `git restore --staged <file>`
- Last commit, keep changes staged: `git reset --soft HEAD~1`
- Last commit, discard changes: `git reset --hard HEAD~1` — **confirm first**, this is destructive
- Already pushed and shared: prefer `git revert <commit>` (adds a new commit undoing the change) over rewriting history

### Issues (via `gh`)

```bash
gh issue create --title "<title>" --body "<description>"
gh issue list
gh issue view <number>
gh issue close <number>
```

- Link commits/PRs to issues where relevant (`Fixes #<number>`, `Closes #<number>`) so they auto-close on merge.
- Use `gh issue list --milestone <name>` or check `.github/ISSUE_TEMPLATE/` when the repo has structured issue templates or milestones, and follow those conventions rather than free-form text.

## Package & dependency management

- **Check the ecosystem first**: identify the manifest (`package.json`, `requirements.txt`/`pyproject.toml`, `Gemfile`, `Cargo.toml`, `go.mod`, `pubspec.yaml`, etc.) and its lockfile (`package-lock.json`/`yarn.lock`/`pnpm-lock.yaml`, `poetry.lock`, `Gemfile.lock`, `Cargo.lock`, `go.sum`) before touching dependencies.
- **Always update manifest and lockfile together, in the same commit.** A manifest bump without a regenerated lockfile (or vice versa) is a common source of "works on my machine" bugs.
- **Prefer the package manager's own commands** over hand-editing version numbers, so the lockfile resolves correctly:
  ```bash
  npm install <pkg>@<version>      # or: npm update <pkg>
  pip install -U <pkg> && pip freeze > requirements.txt   # or use poetry/pipenv if the repo uses one
  cargo update -p <pkg>
  go get <pkg>@<version> && go mod tidy
  bundle update <gem>
  ```
- **Distinguish patch/minor/major bumps** and flag major version bumps explicitly, since they may carry breaking changes — check the package's changelog/release notes before bumping across a major version, and skim for breaking-change notes rather than assuming semver compliance.
- **Check for known vulnerabilities** before and after dependency work when tooling is available: `npm audit`, `pip-audit`, `cargo audit`, or GitHub's Dependabot alerts (`gh api /repos/{owner}/{repo}/dependabot/alerts` if accessible). Report anything found rather than silently ignoring it.
- **Run the test suite after any dependency change** — dependency bumps are exactly the kind of change that looks safe but silently breaks something.
- **Dependency updates get their own commit(s)**, separate from feature/fix work, using `chore(deps): bump <pkg> from x to y` or similar — this keeps `git blame` and changelogs meaningful and makes a bad bump trivial to revert.
- **Respect Dependabot/Renovate PRs** if the repo has them configured (check `.github/dependabot.yml` or `renovate.json`) rather than manually duplicating what they'd already do — review and merge those instead of hand-rolling the same bump.
- **Monorepo/workspace awareness**: if the repo uses workspaces (npm/yarn/pnpm workspaces, a `packages/` layout, Cargo workspaces, etc.), install/update at the workspace root so hoisting and lockfile resolution stay consistent, and confirm which package(s) actually need the bump rather than updating everything.

## Releases, versioning & tags

- **Follow Semantic Versioning (`MAJOR.MINOR.PATCH`)** unless the repo clearly uses a different scheme (check existing tags with `git tag -l` first): breaking change → major, backward-compatible feature → minor, backward-compatible fix → patch.
- **Bump the version in the manifest** (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.) as its own commit (`chore(release): bump version to vX.Y.Z`) before tagging, so the tag and the shipped manifest agree.
- **Generate release notes from history rather than inventing them:**
  ```bash
  git log <last-tag>..HEAD --oneline
  gh release create vX.Y.Z --generate-notes        # auto-drafts notes from merged PRs
  ```
  If the repo maintains a `CHANGELOG.md`, update it from the same commit history (grouped by `feat`/`fix`/`chore` etc. if Conventional Commits are in use) rather than writing free-form prose from memory.
- **Tag and publish:**
  ```bash
  git tag -a vX.Y.Z -m "<release summary>"
  git push origin vX.Y.Z
  gh release create vX.Y.Z --title "vX.Y.Z" --notes "<notes>"
  ```
- **Only tag from `main`** (or a dedicated release branch) once it's verified green — never tag an unmerged or unbuilt commit.
- **Release branches for long-running versions**: if the project supports multiple lines in parallel (e.g. `release/1.x`, `release/2.x`), branch fixes to the correct line and cherry-pick/backport as needed rather than only ever fixing `main`.
- **Publishing to a package registry** (npm, PyPI, crates.io, RubyGems, etc.) is the last step, only after the tag is pushed and CI is green — check the repo for an existing publish workflow (`.github/workflows/*.yml`) before running a manual `npm publish` / `twine upload` / `cargo publish`, since duplicating a CI-driven publish can cause conflicting releases.
- **Never overwrite an existing tag** (`git tag -f`) without explicit confirmation — treat published tags as immutable, since consumers may already depend on them.

## CI/CD awareness

- After pushing or opening a PR, check actual CI status rather than assuming green:
  ```bash
  gh pr checks <number>
  gh run list --branch <branch-name>
  gh run view <run-id> --log-failed     # inspect a failing job's actual output
  ```
- Report real failures back with the failing job name and a summary of the error, not just "checks may be running" or "should be fine."
- If a workflow file (`.github/workflows/*.yml`) exists that would already handle something being done manually (publishing, tagging, changelog generation), prefer letting it run rather than duplicating the action by hand — check for it before doing the equivalent step manually.

## .gitignore / repo hygiene

When asked to add a `.gitignore` or clean up tracked files that shouldn't be tracked:
```bash
git rm --cached <file>       # untrack without deleting locally
```
Check for an existing `.gitignore` and add to it rather than overwriting, and match the project's language/tooling (check for `package.json`, `requirements.txt`, etc.) to pick sensible default ignores rather than guessing generically. Also check for a `.gitattributes` file when line-ending or binary-diff issues come up (`* text=auto`, and `filter=lfs` entries for large binaries that should go through Git LFS instead of being committed directly).

## Safety nets — common gaps to watch for

These are easy to miss and cause real damage or lost work. Check for them proactively, not just when something breaks.

- **Uncommitted work before switching branches.** `git checkout`/`switch` can carry uncommitted changes onto the new branch or, worse, refuse and block you confusingly. Always check `git status` before switching; if there are changes that aren't ready to commit, `git stash push -m "<description>"` first, and remind the user it's stashed (`git stash list` / `git stash pop` to bring it back). Don't let a stash silently disappear — mention it.
- **Working on `main` by accident.** Always check the current branch before making changes described above; redirect to a branch first for anything nontrivial.
- **Detached HEAD state.** If `git status` reports "HEAD detached at ...", any new commits will be orphaned and lost once you switch away. Flag this immediately and create a branch to hold the work (`git switch -c <branch-name>`) before committing further.
- **Stale local `main`.** Before branching off `main` or merging into it, `git fetch` and check whether local `main` is behind `origin/main`; pull first so new branches start from current code and merges don't fight stale history.
- **Force-pushing to `main` or a shared branch.** Treat this as effectively forbidden — refuse by default and require explicit, unambiguous confirmation, since it can destroy others' work.
- **Losing commits after a reset/rebase gone wrong.** They're usually still recoverable via `git reflog` (shows every HEAD movement, including "lost" commits) — know this exists and use it before telling the user something is unrecoverable.
- **Secrets or large files committed by mistake.** If a secret was committed (even if since removed in a later commit), it's still in history and needs `git filter-repo` or GitHub's secret-scanning remediation — plus rotating the leaked credential. A later commit that just deletes the line does NOT remove it from history; say so explicitly. For accidentally-tracked large files/binaries, `git rm --cached` and add to `.gitignore` (or Git LFS) going forward.
- **`.gitignore` added too late.** If files that should've been ignored are already tracked, adding them to `.gitignore` alone won't untrack them — needs `git rm --cached <file>` too.
- **Diverged/behind branches.** Before pushing, `git fetch` and check if the remote has moved (`git status` will show "ahead/behind" info after a fetch) so pushes don't get surprise-rejected mid-task.
- **Multiple remotes or forks.** If `git remote -v` shows more than one remote (e.g. `origin` + `upstream` for a fork), confirm which one to push to / open the PR against rather than assuming `origin`.
- **Line-ending / cross-platform diffs.** If diffs show whole files as changed when only line endings differ, check for a missing or inconsistent `.gitattributes` (`* text=auto`) rather than treating it as a real content change.
- **Submodules silently out of sync.** If the repo has a `.gitmodules` file, `git status` may not show submodule changes by default — run `git submodule status` when working near submodule paths, and use `git submodule update --init --recursive` after cloning or pulling changes that bump a submodule pointer.
- **Git LFS objects not fetched.** If the repo uses Git LFS (`.gitattributes` has `filter=lfs` entries) and large files show as tiny pointer text instead of real content, run `git lfs pull`.
- **Manifest/lockfile drift.** If a manifest (`package.json`, etc.) was edited without regenerating the lockfile, installs will be inconsistent across machines/CI — always regenerate the lockfile in the same commit as a manifest edit.
- **Empty or no-op commits from failed staging.** If `git commit` says "nothing to commit," the `git add` likely didn't match anything (bad path, or the file is gitignored) — check rather than assuming the commit went through.
- **CI failing silently.** After pushing or opening a PR, check `gh pr checks <number>` (or `gh run list` for Actions) rather than assuming green; report actual failures back with the failing job name, not just "checks may be running."
- **Overwriting a published tag or release.** Tags that have already been pushed/published should be treated as immutable; cutting a corrected release means bumping to a new version, not force-moving the old tag.

## Reporting back

After any git/GitHub operation, summarize concretely: what was committed/pushed/opened, the branch name(s) involved, and any real URL or PR/issue/release number returned by the tool — not a paraphrase of the request. If something failed (push rejected, conflict, auth error, failing CI check), say exactly what failed and what the fix options are, rather than a generic "something went wrong."
