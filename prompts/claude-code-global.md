# Claude Code: global instructions (all code projects)

Add the block below to your **user-level** Claude Code memory file so every Claude Code session, in any folder, knows about the ops hub:

- Windows: `C:\Users\<you>\.claude\CLAUDE.md`
- macOS/Linux: `~/.claude/CLAUDE.md`

Create the file if it doesn't exist. Quickest way: in any Claude Code session, run `/memory`, pick the user memory, and paste.
Sessions inside the ops-hub repo itself already follow the repo's own `CLAUDE.md`; this block is for every other project.

```
## Ops hub (business work tracking)

My business work is tracked in the repo jl91-sudo/ls-project-ops-hub.
Local clone: ~/ls-project-ops-hub  (if that path doesn't exist, ask me once for the correct path and update this line).
Tracks: lec-serve-ops (Lec-Serve compliance, VBA, trackers, TBT, H&S tools), lecserve-ai-service (AI document-classification service, local GPU hardware, LLM routing), ops-system (the tracking setup).

1. At the start of a session, if the work plausibly belongs to a track, ask once: "Looks like <slug>. Log this session to it? (yes / other track / no)". Personal or unrelated work: say nothing.
2. At the end of a session I said yes to, or when I say "checkpoint":
   - show me a breakdown: what changed in this session, proposed new tasks, health, next action, blocker;
   - ask me for the track's completion % and any due dates; never estimate them;
   - write the confirmed checkpoint to <clone>/inbox/<YYYY-MM-DD>-<slug>-<next free number>.md in the inbox format defined in that repo's CLAUDE.md §3, with source: claude-code:<this project's folder name>;
   - in the clone: git pull, add only that file, commit "inbox(<slug>): <one-line summary>", push.
3. Never copy code, client data, personal data or worker names into the ops hub; describe the change instead. Job numbers are fine.
4. If the clone is missing or the push fails, give me the checkpoint as one code block with the filename on the first line.
```

## Cloud Claude Code sessions (claude.ai/code)
They can't see your local clone. Attach the repo to the session (ask Claude to "add the repo jl91-sudo/ls-project-ops-hub"), and it can push the checkpoint the same way.
