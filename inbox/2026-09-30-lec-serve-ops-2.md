track: lec-serve-ops
health: Active
next_action: Build master Form template with paginated sections for toolbox talks; test with pilot cohort
blocker: none
source: chat:Lec Serve H&S Digital Signature App (Project backfill)
---

## Done: what has been built or decided so far

- Architecture & approach finalized: Microsoft Forms + Power Automate + Excel (Aug 21, 2026)
- Per-page acknowledgment model scoped: Forms pages with required checkboxes per section (not raw pages)
- Bulk-send workflow designed: List rows from Excel → Apply to each → Send Outlook email with dynamic Name/Email and Form link
- Document types clarified: MA-03 manual = 15 separate 1-page talks (one ack per talk); newsletters = multi-section (ack per section, not per raw page)
- Project description updated with full scope
- Recipient list structure defined: Excel table with Name, Email columns (dropdown in Form); optional Status column for send date logging

## Decisions

- Forms chosen over SharePoint + Power App for simplicity; fully reusable template approach with image swaps only
- Bulk email via Outlook (not SMS); SMS flagged as requiring paid connector (Twilio) if needed later
- Manual paste step retained: useful audit gate before 20+ crew sees content
- Forms sections match newsletter TOC structure (10 named sections per Issue 38), not raw page count
- Optional auto-chase flow for non-responders deferred; not yet scoped
- One master Form template with per-talk duplication workflow: populate once, swap images, reuse

## Proposed tasks

- [ ] Build master Microsoft Form template: Name dropdown + placeholder sections with "I have read and understood" checkboxes
- [ ] Test Form template with pilot: send to 2-3 crew, verify responses flow to Excel
- [ ] Create Power Automate bulk-send flow: trigger (manual) → List Excel rows → Send email with dynamic recipient + Form link + soft deadline
- [ ] Build Forms instance for first toolbox talk: convert PDF to images, populate, test send + completion
- [ ] Build Forms instance for next monthly newsletter: extract sections from final version, populate, test
- [ ] Optional: Design and build auto-reminder flow for non-responders (~3 days post-send)
