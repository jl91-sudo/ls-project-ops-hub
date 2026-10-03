# Lec-Serve operations — progress

## 2026-10-03 — AssetScan development reference document
- **Source:** chat:LecServe AssetScan Development App - Claude MCP
- **Done:** Single development reference document created for the AssetScan QR asset app (2026-10-02): screen flow and navigation map, Studio connect/deploy mechanics, SharePoint data model incl. the six SFG20 compliance column mappings, the four-flow report pipeline, UI conventions, known gotchas, audit baselines and open backlog; built from re-verified on-disk state. Completion 10% kept: the inbox reports 25% (user-confirmed in chat), but the unattended daily run does not change completion; confirm at the next checkpoint. 1 proposed task awaits confirmation (see inbox/processed/2026-10-02-lec-serve-ops-1.md); not added to STATUS.
- **Decisions:** Reference is the standing picture of the app; the project router file keeps pointing task types at routines (only deploy rules duplicated, deliberately) · audit baselines and backlog stay authoritative in their own audit logs · Priority 1–6 flow fixes from 2026-09-30 confirmed still outstanding.
- **Next:** Duplicate app as alpha copy and implement Priority 1 flow fix (Photo Upload: validate ReportID before creating file)
- **Blocker:** none

## 2026-10-02 — Backfill: Asset list QR code app and flow fixes
- **Source:** chat:Lec-Serve Asset List QR Code Project (Project backfill)
- **Done:** QR asset-scanning Power Apps app built with photo capture and condition reporting (Jun–Aug 2026); three Power Automate flows deployed (QR generation, Photo Upload, Report Auto-fill); 6 logic/error-handling issues identified; manual-trigger Claude analysis flow built and tested (reports → Claude → Teams); branded QR guidance (Sep 2026). Completion 10% (unchanged). 10 proposed tasks await confirmation, due dates and %s (see inbox/processed/2026-09-30-lec-serve-ops-3.md); not added to STATUS.
- **Decisions:** Claude Opus for occasional deep-dive analysis · on-demand trigger, not scheduled · all changes go through an alpha app copy tested on phone before production · Power Automate Premium needed for HTTP actions · API billed separately from the Pro subscription.
- **Next:** Duplicate app as alpha copy and implement first Priority 1 flow fix (Photo Upload validation order)
- **Blocker:** none

## 2026-10-02 — Backfill: H&S digital signature app (Forms + Power Automate)
- **Source:** chat:Lec Serve H&S Digital Signature App (Project backfill)
- **Done:** Architecture set as Microsoft Forms + Power Automate + Excel (2026-08-21); per-section acknowledgment model scoped (MA-03 = 15 one-page talks, one ack each; newsletters ack per TOC section); bulk-send flow designed (Excel rows → Outlook email with Form link); recipient list structure defined. Completion 10% (unchanged). 6 proposed tasks await confirmation, due dates and %s (see inbox/processed/2026-09-30-lec-serve-ops-2.md); not added to STATUS.
- **Decisions:** Forms over SharePoint + Power App for simplicity · Outlook email, not SMS (SMS needs paid connector) · manual paste step kept as audit gate · sections follow newsletter TOC · one master Form template duplicated per talk · auto-chase for non-responders deferred.
- **Next:** Build master Form template with paginated sections for toolbox talks; test with pilot cohort
- **Blocker:** none

## 2026-10-02 — Backfill: TBT sheets, job tracker rebuild, TBT compliance review
- **Source:** chat:backfill from past chats (26 Aug – 30 Sep 2026)
- **Done:** Weekly TBT sheets produced (latest pack WC 2026-09-06) via the lecserve-tbt skill; Job Numbers Tracker rebuilt 2026-09-09 (Works Completed List keyed on job number so finance data survives status changes); TBT automation compliance review 2026-08-26 (email-and-CONFIRMED alone is not a delivered talk). Completion 10% (unchanged). 4 proposed tasks await confirmation, due dates and %s (see inbox/processed/2026-09-30-lec-serve-ops-1.md); not added to STATUS.
- **Decisions:** Toolbox talks stay delivered on site by the supervisor; automation handles paperwork only.
- **Next:** Verify the rebuilt job tracker in Excel (4 checks), then copy it back to OneDrive
- **Blocker:** none

## 2026-09-30 — Track created
- **Source:** claude-code
- **Done:** Track seeded at setup: 10% complete, no due date, tasks to be provided later.
- **Decisions:** none
- **Next:** Weekly TBT sheets; tracker upkeep
- **Blocker:** none
