# Project backfill prompt

Paste this into a chat inside any claude.ai Project to bring its history into the ops hub.
Save the result it gives you into `inbox/` (or paste it to Claude to commit), then run `process inbox` in Claude Code.

```
Backfill my ops hub from this Project.

The ops hub is my GitHub repo (jl91-sudo/ls-project-ops-hub) that tracks the status of my business work. Nothing needs creating in this Project.

1. Source: the conversations in this Project (use files only to confirm facts). I want where the work stands, not the content of the documents.
2. Pick which track this Project belongs to: lec-serve-ops (Lec-Serve compliance, VBA, trackers, TBT, H&S tools), lecserve-ai-service (AI document-classification service, local GPU hardware, LLM routing) or ops-system (this tracking setup). Tell me your pick in one line and wait for me to confirm. If it's none of them or not business work, say so and stop.
3. Then output one checkpoint in exactly this format:

track: <slug>
health: <Active|At risk|Blocked|Paused|Done>
next_action: <one line>
blocker: <text or none>
source: chat:<this Project's name> (Project backfill)
---
Done: what has been built or decided so far, with dates
Decisions: key choices and why, one line each
Proposed tasks:
- [ ] <open task>

Rules: don't estimate completion % or due dates; ask me for each at the end. No personal data, worker names or client document text; job numbers are fine. If you can push to the repo, save it as inbox/<today YYYY-MM-DD>-<slug>-<next free number>.md; otherwise give it to me as one code block.
```
