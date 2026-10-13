track: lec-serve-ops
health: Active
next_action: Run the Period 7 PPM reports: update the Period 7 master, file the downloads, then run the screens in runbook order with a dry run before each
blocker: Q2 RCD data and failure export still needed (carried over, not re-confirmed this session)
source: claude-code:lecserve-report-studio
---
Done:
- Added a period runbook to the report app repo: which inputs come from Site Report Pro and which from other portals, where each is filed, and the order to run the screens. Also published as a pinned page.
- The report app now puts the toilets self-test CSV into the EL Internal report as a year-to-date pass/fail table. Verified with tests, lint and a run on real Period 6 data checked in Word.
- Built the Air Breaker Servicing report workflow and produced the Period 7 report (docx and PDF, 18 pages, checked in Word). Asset-list gaps are filled from the certificates, empty comment lines are removed, real remarks go to a to-do page at the front, certificate misspellings are corrected in the report copy, and margins are Narrow.
- Audited Periods 1 to 7 across the PPM Reports and Emergency Lighting folders for missing files.
- Copied the Period 6 emergency lighting inputs and finals into the Emergency Lighting Period 6 folder as a backup, hash-checked, nothing moved or overwritten.
- Renamed the Period 7 master workbook from Period 6 to Period 7 (file name only).
- Report app state: 445 tests pass, lint clean. Type checks are blocked by Smart App Control.

Decisions:
- Source files and templates are never written; the app only writes copies.
- Plant Room 9 designation is SB/T2/1/AS and its certificate dates are 2026.
- Asset-list rating mismatches and the sticky-mechanism notice to the client are already covered outside this work.
- Filing finished reports to OneDrive will become an automated step of the report app's output, not a manual task.
- Earlier-period missing files are optional backfill; they do not block Period 7.
- Completion % and due dates not set at this checkpoint.

Proposed tasks:
- [ ] Rename two issues in Site Report Pro (Plantroom 9 designation, Bus coupler)
- [ ] Add the two Arch 255 breakers to the air breakers list
- [ ] Add automated OneDrive filing to the report app's output step
- [ ] Optional: source the toilets self-test files for Periods 3 to 5, the EL Internal/External exports for Periods 1 and 3, and the WAT/WIT location exports for Periods 1 and 2
- [ ] Confirm what the test type letters in the toilets CSV mean
- [ ] Decide whether the WAT internal report should also get the toilets table
