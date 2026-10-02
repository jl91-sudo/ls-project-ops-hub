track: lec-serve-ops
health: Active
next_action: Duplicate app as alpha copy and implement Priority 1 flow fix (Photo Upload: validate ReportID before creating file)
blocker: none
source: claude-code:LecServe AssetScan Development App - Claude MCP
---
Done:
- Created a single development reference document for the AssetScan QR asset app (2026-10-02)
- Reference covers: screen flow and navigation map, Studio connect and deploy mechanics, the SharePoint data model including the six SFG20 compliance column mappings, the four-flow report pipeline, reusable UI conventions, known gotchas, audit baselines and the open backlog
- Document built from current on-disk state rather than recalled context: screen sizes, navigation edges, routine files, audit logs and scheduled-task schedules were all re-verified today

Decisions:
- The new reference is the standing picture of the app; the existing project router file keeps its job of pointing each task type at the right routine. No content duplicated between them except the deploy rules, repeated deliberately because the download tool silently overwrites unpushed local edits
- Audit baselines and backlog items stay authoritative in their own audit logs; the reference is a summary that will drift and should not be treated as the source of truth for those numbers
- Priority 1-6 flow fixes recorded on 2026-09-30 confirmed still outstanding as of today; not superseded by the app work done in Claude Code
- Completion moved 10% to 25% (user-confirmed). No due dates set

Proposed tasks:
- [ ] Replace the inefficient offline-queue cleanup join with a short-circuiting lookup, once an offline test path exists. Deferred because it governs deletion of queued offline photos, so an untested change risks losing field data
