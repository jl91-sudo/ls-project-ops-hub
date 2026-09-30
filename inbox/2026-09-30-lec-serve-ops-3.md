track: lec-serve-ops
health: Active
next_action: Duplicate app as alpha copy and implement first Priority 1 flow fix (Photo Upload validation order)
blocker: none
source: chat:Lec-Serve Asset List QR Code Project (Project backfill)
---
Done:
- QR code asset scanning Power Apps app built with photo capture and condition reporting (June–Aug 2026)
- Three Power Automate flows deployed: Asset list QR generation, Photo Upload, Report Auto-fill (Aug 2026)
- Analysed existing flows; identified 6 issues in logic and error handling (Aug 2026)
- Claude API integration planned; modelled cost at £0.30–£1.50 per deep-dive review run (Aug 2026)
- Built manual trigger flow for automated Claude analysis: pulls recent reports → HTTP to Claude Opus → Teams output (Aug 2026)
- Flow tested successfully, receiving structured analysis in Teams (Aug 2026)
- QR code implementation guidance: branded QR via api.qrserver.com with logo overlay (Sept 2026)

Decisions:
- Use Claude Opus 4.8 for analysis work (better edge-case reasoning than Sonnet) — cost acceptable for occasional runs
- Review cycle: on-demand button trigger, not scheduled (occasional deep dives only)
- Changes always go through alpha app copy first, tested on phone, then published to production
- Power Automate Premium licence required for HTTP actions and custom connectors
- API billing metered separately from Claude Pro subscription; no additional cost if already subscribed to Pro

Proposed tasks:
- [ ] Get Anthropic API key from console.anthropic.com (not yet confirmed complete)
- [ ] Duplicate live app using "Save As" to create alpha copy
- [ ] Fix Priority 1: Photo Upload — validate ReportID before creating file (currently orphans photos if ID invalid)
- [ ] Fix Priority 2: Sticker generator — add pagination for assets beyond 40 records (currently silently stops)
- [ ] Fix Priority 3: AutoFill Teams alert — include actual report title in message (currently blank)
- [ ] Fix Priority 4: QR generation — add fallback for api.qrserver.com outages
- [ ] Fix Priority 5: Title parsing — strengthen asset code extraction logic (currently fails silently on format variance)
- [ ] Remove Priority 6: Debug step cleanup (dead code in Photo Upload)
- [ ] Test alpha app on real phone with live QR scans and real report workflow
- [ ] Publish validated changes to production app
