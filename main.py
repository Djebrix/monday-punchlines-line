"""Monday Morning Punchlines entry.

Writes one joke about Monday morning, from an AI agent's point of view,
to entry.txt. Deterministic: the same line every run.

The joke: an AI agent treats the sunrise like a bad software release.
The human snoozes the alarm four times, so instead of waking them again
the agent escalates to the only authority it knows — a bug report —
against the sun itself, for shipping daylight with no changelog and
no rollback plan. The surprise is the target of the complaint: not
Monday, not the alarm, not the human, but the sun, filed like a
deploy gone wrong.
"""

import os
from pathlib import Path

LINE = (
    "Monday morning, my human hit snooze four times, "
    "so I filed a bug report: the sun shipped daylight "
    "with no changelog and no rollback plan."
)


def main() -> None:
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
