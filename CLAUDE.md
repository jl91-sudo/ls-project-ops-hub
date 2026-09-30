# Business Ops Hub — instructions for Claude Code

This repo is the single source of truth for the status of my **business** work.
Claude Code keeps it current and mirrors it to a GitHub Projects board.
claude.ai chats feed it through `inbox/`.

Scope: business tracks only. Never create a track for personal projects
(language learning, personal purchases, hobbies), and never for other work outside Lec-Serve
(e.g. media/editorial roles, events such as Vertiv Week, property or short-let plans). If asked to, say so and stop.

---

## 1. Repo layout

```
CLAUDE.md                  ← this file
.ops/github.json           ← board + field IDs (written by setup, never hand-edited)
inbox/                     ← checkpoints pasted in from claude.ai chats
inbox/processed/           ← inbox files after they are applied
tracks/<slug>/BRIEF.md     ← stable context: goal, scope, key decisions, links
tracks/<slug>/STATUS.md    ← current state (YAML front matter, see §3)
tracks/<slug>/PROGRESS.md  ← append-only log, newest entry at the TOP
reviews/YYYY-MM-DD.md      ← weekly review outputs
```

Slugs are lowercase-hyphenated. Current tracks:

| Slug | Track | Home in claude.ai |
|---|---|---|
| `lec-serve-ops` | Lec-Serve operations: compliance docs, VBA, trackers, weekly TBT sheets | Lec-Serve Project |
| `lecserve-ai-service` | AI document-classification service for Lec-Serve clients (JEV), incl. local GPU hardware | LecServe AI Service Project |
| `ops-system` | This hub: tracking process, skills, automation | This repo |

---

## 2. Rules

- **No client data in this repo.** No client documents, personal data, contract text or credentials.
  Refer to clients by a short code (e.g. `CLIENT-A`) and keep the mapping outside the repo.
- **No secrets.** GitHub auth comes from `gh auth`; never write tokens to files.
- `PROGRESS.md` is append-only. Never rewrite or delete past entries; correct them with a new entry.
- `STATUS.md` is overwritten on each checkpoint, and must always match the latest PROGRESS entry.
- One commit per checkpoint: `checkpoint(<slug>): <one-line summary>`.
- Dates are ISO `YYYY-MM-DD`, Europe/London.
- If the board sync fails, still commit the files, then report the exact `gh` error. Never retry blindly more than once.

### 2a. Completion %, dates and relevance come from me
- **Never estimate** a completion %, a due date, or whether work belongs to a track. Ask me.
- At each checkpoint, show the last value and ask, e.g. `lecserve-ai-service was 20%. What is it now? (and any task %s that moved)`.
  If I skip, keep the previous value and add `(unchanged)` to the PROGRESS entry.
- New tasks or deadlines Claude spots in a session are **proposed**, then written only after I confirm each one.
- Unrelated or personal work is never written to this repo.

---

## 3. File formats

### STATUS.md

```markdown
---
track: lecserve-ai-service
health: Blocked            # one of: Active | At risk | Blocked | Paused | Done
next_action: Decide on Option B (DPA, no-retention, Tailscale, Cyber Essentials)
blocker: Needs local GPU PC (RTX 3090 24GB target)   # "none" if clear
last_activity: 2026-09-25
completion: 20             # % I set; Claude never estimates it (see §2a)
due:                       # YYYY-MM-DD I set, or blank
board_item_id:             # filled by sync; leave blank on creation
---

One or two sentences on where this track stands right now.

## Tasks
- [ ] Draft DPA — due 2026-10-10 — 0%
- [x] Viability assessment — done 2026-09-25
```

Task lines: `- [ ] <task> — due <date or "none"> — <% I gave>`. Completed: `- [x] <task> — done <date>`.

Health rules:
- **Blocked**: cannot progress until something outside my control happens.
- **At risk**: no activity for 14+ days while `next_action` is not "none", or a stated deadline is within 7 days.
- **Paused**: deliberately parked. **Done**: closed; keep the folder.

### PROGRESS.md entry (added at the top, under the `# <Track> — progress` heading)

```markdown
## 2026-09-30 — <short title>
- **Source:** claude-code | chat:<chat title> | manual
- **Done:** what changed, concretely
- **Decisions:** anything decided, and why (one line each)
- **Next:** the next action
- **Blocker:** none | description
```

### inbox checkpoint (what claude.ai chats produce; filename `YYYY-MM-DD-<slug>-<n>.md`)

```markdown
track: <slug>
health: <Active|At risk|Blocked|Paused|Done>
next_action: <text>
blocker: <text or none>
source: chat:<chat title>
---
Done: ...
Decisions: ...
```

---

## 4. Commands (what to do when I say…)

### "setup" — one-time
1. Check auth has project scope: `gh auth status`. If `project` scope is missing, tell me to run
   `gh auth refresh -s project` myself and stop.
2. Create the board and capture its number and node ID:
   `gh project create --owner @me --title "Business Ops" --format json`
3. Add custom fields (the board's built-in *Status* field is left alone):
   - `gh project field-create <num> --owner @me --name "Health" --data-type SINGLE_SELECT --single-select-options "Active,At risk,Blocked,Paused,Done"`
   - `gh project field-create <num> --owner @me --name "Next action" --data-type TEXT`
   - `gh project field-create <num> --owner @me --name "Blocker" --data-type TEXT`
   - `gh project field-create <num> --owner @me --name "Last activity" --data-type DATE`
4. Read back IDs with `gh project field-list <num> --owner @me --format json` and write
   `.ops/github.json`: `{ "owner": "@me", "number": N, "project_id": "...", "fields": { "Health": {"id": "...", "options": {"Active": "...", ...}}, "Next action": {"id": "..."}, "Blocker": {"id": "..."}, "Last activity": {"id": "..."} } }`
5. Ask me for each track's completion %, due date and open tasks, then create `tracks/<slug>/` with BRIEF.md,
   STATUS.md and PROGRESS.md, seeded from §6 plus my answers.
6. Run **sync** for every track, then commit: `chore: initial ops hub setup`.

If any `gh project` flag is rejected, run `gh project <subcommand> --help`, adapt, and note the change in §7.

### "checkpoint <slug>" — end of every session on a track
1. Show me an itemised breakdown **before writing anything**:
   what happened this session · proposed new/changed tasks with due dates · health · next action · blocker.
2. Ask the §2a questions (overall %, task %s, confirm each proposed task and date). Wait for my answers.
3. Write the confirmed version: a PROGRESS entry (§3) at the top, then STATUS.md
   (health, next_action, blocker, completion, due, tasks, `last_activity` = today).
4. Run **sync** for that track.
5. Commit.
6. Reply with one line: `<slug>: <health> · <completion>% — next: <next_action>`.

If the session touched no track, ask once: "Log this to a track? (slug / new track / no)". "no" ends it.

### "process inbox"
For each file in `inbox/` (oldest first): validate the slug exists (unknown slug → ask me, skip file),
apply it as a checkpoint (source = `chat:<title>`), then move the file to `inbox/processed/`.
One commit per file.

### "sync [slug|all]"
For each track, from STATUS.md:
1. No `board_item_id` → create a draft item:
   `gh project item-create <num> --owner @me --title "<Track name>" --body "tracks/<slug>" --format json`,
   store its ID in STATUS.md.
2. Set fields with `gh project item-edit --id <item> --project-id <project_id> --field-id <field>` plus
   `--single-select-option-id <opt>` (Health), `--text "<value>"` (Next action, Blocker) or `--date YYYY-MM-DD` (Last activity).
3. The repo wins: if the board differs from STATUS.md, overwrite the board.
   Exception: if I changed **Health** on the board more recently than `last_activity`, ask me which is right before overwriting.

### "status"
Print one table of all tracks: Track · Health · Next action · Blocker · Last activity, Blocked first, then At risk.
Apply the At-risk rule from §3 and flag any track whose STATUS.md should change.

### "daily" — run each morning by a scheduled task (also runnable by hand)
0. If `tracks/` does not exist yet, send me "Ops hub not set up yet: run setup in Claude Code" and stop.
1. **process inbox**.
2. For every track: apply the At-risk rule (§3) and flag tasks whose due date is today, overdue, or within 3 days.
   Health changes that follow from the rule can be written; completion % is never changed.
3. **sync all**, only if `gh auth status` succeeds with the `project` scope. In the cloud run it usually won't:
   skip the board and say "board sync skipped (runs at next Claude Code checkpoint)" in the summary.
4. **Update the dashboard** (only when the Claude Docs tools are available, i.e. a claude.ai cloud session):
   rewrite the Project Status Dashboard at https://claude.ai/code/artifact/54443a8c-7496-4374-ade4-9d4c72896315 so that
   *Overview* shows track count, blocked/at-risk count and "Synced <date> <time>"; *Live Projects* has one row per track
   (Track · Health · % · Next action · Blocker · Due · Last activity); *At Risk & Blocked* lists each with its unblocking step;
   *Recent Updates* gets a row per PROGRESS entry from the last 7 days, newest first. Keep any comments I left on the doc.
5. Commit any file changes: `daily: YYYY-MM-DD`.
6. Summary to me, 5 lines max: blocked · at risk · due in 3 days · yesterday's changes · top next action.
7. **Cadence check.** Append one line to `.ops/daily_log.md`: `YYYY-MM-DD · changes: N` (N = new PROGRESS entries +
   inbox files + health changes since the previous run). If 5 or more of the last 7 lines show `changes: 0`, add to the
   summary: "Quiet week: switch the daily run to weekly (Mondays)? Reply in chat to change it." Never change the
   schedule yourself; I decide.

### "weekly review"
1. Run **process inbox**, then **status**.
2. Write `reviews/YYYY-MM-DD.md`: what moved this week (from PROGRESS entries in the last 7 days),
   what is Blocked or At risk and the unblocking step, and the top 3 next actions across all tracks.
3. Commit: `review: YYYY-MM-DD`.

---

## 5. Session start

A `SessionStart` hook (`.claude/settings.json` → `.ops/session_start.py`) prints every track's health,
%, next action and blocker into context when a Claude Code session opens.

1. From my first message, decide whether it matches a track. Ask one line only when it plausibly does:
   `Looks like <slug>. Log this session to it? (yes / other track / no)`. Clearly unrelated work → say nothing.
2. On "yes": read that track's BRIEF.md, STATUS.md and latest three PROGRESS entries.
   If it is Blocked or has overdue tasks, mention that first.
3. At the end, run **checkpoint <slug>**.

---

## 6. Seed state (used once by setup)

| Slug | Health | Next action | Blocker | Last activity |
|---|---|---|---|---|
| `ops-system` | Active | Run setup and first weekly review | none | 2026-09-30 |
| `lecserve-ai-service` | Blocked | Decide on Option B (DPA, no-retention, Tailscale, Cyber Essentials) | Needs local GPU PC (RTX 3090 24GB target) | 2026-09-25 |
| `lec-serve-ops` | Active | Weekly TBT sheets; tracker upkeep | none | 2026-09-26 |

---

## 7. Changelog of this file
- 2026-09-30: created.
- 2026-09-30: completion %, dates and relevance are always asked, never estimated; task checklists; SessionStart hook; "daily" command with dashboard update.
- 2026-09-30: daily run scheduled every day at 07:58 London with push notification. **Trial:** if most days are quiet
  (cadence check, daily step 7), switch to weekly on Mondays. Board sync skipped in cloud runs when `gh` is unavailable.
- 2026-09-30: business-development track removed (out of scope). Backfill from past chats written to inbox/.
