#!/usr/bin/env python3
"""SessionStart hook: print a one-line summary per business track into Claude Code's context."""
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKS = ROOT / "tracks"
ORDER = {"Blocked": 0, "At risk": 1, "Active": 2, "Paused": 3, "Done": 4}


def front_matter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, _, value = line.partition(":")
            data[key.strip()] = value.split("#", 1)[0].strip()
    return data


def overdue_tasks(path: Path) -> int:
    today = date.today().isoformat()
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("- [ ]") and "due " in line:
            due = line.split("due ", 1)[1][:10]
            if due[:4].isdigit() and due < today:
                count += 1
    return count


def main() -> None:
    if not TRACKS.is_dir():
        print("Business Ops Hub: no tracks yet. Say 'setup' to create them.")
        return
    rows = []
    for status in sorted(TRACKS.glob("*/STATUS.md")):
        fm = front_matter(status)
        rows.append((
            ORDER.get(fm.get("health", ""), 9),
            status.parent.name,
            fm.get("health", "?"),
            fm.get("completion", "?") or "?",
            fm.get("next_action", "") or "none",
            fm.get("blocker", "") or "none",
            overdue_tasks(status),
        ))
    print(f"Business Ops Hub - {len(rows)} tracks (from tracks/*/STATUS.md, {date.today().isoformat()}):")
    for _, slug, health, pct, nxt, blocker, late in sorted(rows):
        extra = f" | blocker: {blocker}" if blocker.lower() != "none" else ""
        extra += f" | {late} overdue task(s)" if late else ""
        print(f"- {slug}: {health}, {pct}% | next: {nxt}{extra}")
    print("Follow CLAUDE.md section 5: ask whether this session belongs to a track before logging anything.")


if __name__ == "__main__":
    main()
