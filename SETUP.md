# First-time setup — instructions for Claude Code

I (the owner) will open Claude Code in this repo and say: **"Follow SETUP.md"**.
Work through the steps in order. Stop and tell me exactly what to do at any step that needs me
(installs, logins, answers). Don't skip a check because a later step might cover it.

Background: this repo tracks the status of my **business** work. `CLAUDE.md` holds the rules and
commands; read it in full before step 5. A cloud scheduled task ("Business Ops daily", 07:58 London,
every day, push notification) already runs the `daily` command from `CLAUDE.md`. It can't reach the
GitHub board, so the board is updated only from this PC via Claude Code.

---

## 1. Repo is current
- Run `git status` and `git pull`. The repo must be on `main` with no uncommitted changes.
- Confirm these exist: `CLAUDE.md`, `.claude/settings.json`, `.ops/session_start.py`, `.ops/daily_log.md`, `inbox/`, `reviews/`.

## 2. GitHub CLI
- Run `gh --version`. If missing, tell me to install it (Windows: `winget install GitHub.cli`), then wait.
- Run `gh auth status`.
  - Not logged in → tell me to run `gh auth login`, then wait.
  - Logged in but the token scopes lack `project` → tell me to run `gh auth refresh -s project`, then wait.
- Don't run login or auth commands yourself; they need my browser.

## 3. Python and the session-start hook
- Run `python3 --version`. If it fails, try `python --version`.
  - Only `python` works → in `.claude/settings.json`, change `python3` to `python`, and tell me you did.
  - Neither works → tell me to install Python 3 (Windows: `winget install Python.Python.3.12`), then wait.
- Run the hook by hand: `python3 .ops/session_start.py` (or `python`).
  Expected output before setup: `Business Ops Hub: no tracks yet. Say 'setup' to create them.`
- Tell me to restart Claude Code once, so I can confirm the hook prints that line at session start.

## 4. Commit any fixes
If steps 1–3 changed any file: commit `chore: local setup fixes` and push.

## 5. Run "setup"
Follow the **"setup"** command in `CLAUDE.md` §4 exactly:
- create the "Business Ops" board and its fields, and write `.ops/github.json`;
- **ask me** for each track's completion %, due date and open tasks. Never estimate them;
- create the `tracks/` folders, sync the board, commit and push.

Then run **"status"** and show me the table.

## 6. Hand over the claude.ai preference text
Print the block below for me to paste into claude.ai → Settings → Profile → preferences.
It makes ordinary chats feed this repo. Don't change the wording.

```
Always: if a chat relates to one of my business tracks (lec-serve-ops, lecserve-ai-service, business-development, ops-system), ask once at the start: "Log this to <track>? (yes/no)". If yes, at the end of the chat write an inbox checkpoint in the format from CLAUDE.md in the repo jl91-sudo/ls-project-ops-hub. If the session can push to that repo, commit it to inbox/ yourself; otherwise give me the checkpoint to save there. Never estimate completion %, due dates or which track work belongs to; ask me. Ignore personal chats.
```

## 7. Finish
Reply with:
- setup result (board URL from `gh project view <num> --owner @me --web` is fine to mention, don't open it);
- the status table;
- the reminder: "End each session with `checkpoint <slug>`. The 07:58 daily run updates the dashboard and pushes you a summary."

Then add a line to `CLAUDE.md` §7: `- YYYY-MM-DD: first-time setup completed (SETUP.md).`, commit and push.

---

## Day-to-day, after setup
| When | Say | What happens |
|---|---|---|
| Start of a session | nothing | Hook lists tracks; Claude asks if the session belongs to one |
| End of a session | `checkpoint <slug>` | Breakdown, asks your %, writes files, syncs board, pushes |
| Chat checkpoints saved to `inbox/` | `process inbox` | Applies them as checkpoints |
| Any time | `status` | Table of all tracks |
| Monday | `weekly review` | Writes `reviews/YYYY-MM-DD.md` |
| Daily run says "quiet week" | tell Claude in chat | Schedule switches to weekly (Mondays) |
