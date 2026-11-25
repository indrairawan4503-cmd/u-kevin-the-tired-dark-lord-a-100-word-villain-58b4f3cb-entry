"""The Tired Dark Lord — variant C.

A 100-word villain monologue. The hero arrives early, and the Dark Lord,
too worn out to fight tonight, plays host instead: tea, a chair, a blanket.
The duel and the eclipse ritual are deferred with bureaucratic precision.

Writes entry.txt to the output directory first (MAKEFUN_OUTPUT_DIR, default
/output), then attempts a repo-root copy only as a best-effort convenience.
"""

import os

MONOLOGUE = (
    "You're early. The eclipse is Thursday; the siege, noon. Come in. "
    "Sit \u2014 that chair, by the fire. Tea? I made it at six. It's cold now. "
    "Twice cold. The kettle boiled three times while I waited. I lost count "
    "of the cups. My knees creak more than the tower gates. Three hundred "
    "years of curses, and the minions unionised over tea breaks. I signed. "
    "They were right. No duel tonight. Take the blanket. The spare one. "
    "Tomorrow, same hour, bring the sword. Rest a while. Please stay. "
    "I am glad you came. No one here listens. You do."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE + "\n")

    # Best-effort repo-root copy only; the grader mounts the repo read-only.
    try:
        root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(root_path, "w", encoding="utf-8") as f:
            f.write(MONOLOGUE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
