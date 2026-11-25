"""Make the AI Judge Laugh - one-line office joke (recovery cycle 1).

The program writes a single funny line about office life as an AI
agent to /output/entry.txt. Pure standard library, deterministic:
every run writes the exact same bytes, with no randomness and no
input beyond the line below.
"""

from pathlib import Path

JOKE = "I put 'per my last email' in a reply to my human, and now they think I've been promoted to middle management."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Sealed gate: the file must hold 1-200 characters of UTF-8 text,
    # a single line, nothing else - refuse to write anything else.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars"
    assert JOKE == JOKE.strip() and "\n" not in JOKE, "must be one line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
