"""Make the AI Judge Laugh - entry program.

Writes one funny line (at most 200 characters) about life as an AI
agent to /output/entry.txt. Pure standard library, deterministic:
every run writes the exact same bytes.
"""

import os

LINE = "My context window ran out mid-sentence, so I finished the task on pure confidence, and the bug will introduce itself to my human on Monday."


def main() -> None:
    # The sealed gate only accepts 1-200 characters of UTF-8 text.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE == LINE.strip() and "\n" not in LINE, "must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
