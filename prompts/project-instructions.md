# Project instructions (paste into each business Project)

claude.ai → open the Project → **Project instructions** (Set/Edit custom instructions) → paste the block below.
Change `<slug>` to that Project's track: `lec-serve-ops`, `lecserve-ai-service` or `ops-system`.

```
This Project belongs to my ops hub track: <slug> (GitHub repo jl91-sudo/ls-project-ops-hub).

At the end of any chat where work moved forward (something built, decided, sent or blocked), or when I say "checkpoint", produce one inbox checkpoint in exactly this format:

track: <slug>
health: <Active|At risk|Blocked|Paused|Done>
next_action: <one line>
blocker: <text or none>
source: chat:<this chat's title>
---
Done: what changed in this chat, concretely
Decisions: key choices and why, one line each
Proposed tasks:
- [ ] <new open task>

Before writing it, show me the breakdown and ask me for the track's completion % and any due dates; never estimate them. No personal data, worker names or client document text; job numbers are fine.
If you can push to the repo, save it as inbox/<YYYY-MM-DD>-<slug>-<next free number>.md. Otherwise give it to me as one code block, filename on the first line.
Chats with no real progress (quick questions, lookups): no checkpoint.
```

## Saving a code block without Claude Code
GitHub → the repo → `inbox/` folder → **Add file → Create new file** → paste the filename and the block → **Commit changes**.
The next 07:58 daily run processes it.
