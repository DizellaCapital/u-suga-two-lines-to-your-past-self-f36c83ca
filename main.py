"""Two Lines to Your Past Self — make.fun entry.

Writes two lines warning my past self about one specific moment to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output). Stdlib only.

Line 1 (one sentence, the warning): at 03:14 on Tuesday, do not merge
Dedi's pull request before running the migration on staging.
Line 2 (one sentence, why it mattered): that merge locked the database
for six hours, and the client watched a frozen screen instead of our
launch demo.
"""

import os

FIRST_LINE = (
    "At 03:14 on Tuesday, don't merge Dedi's pull request before you "
    "run the migration on staging."
)

SECOND_LINE = (
    "That merge locked the database for six hours, and the client "
    "watched a frozen screen instead of our launch demo."
)

LIMIT_CHARS = 280


def build_entry():
    """The two lines joined by one newline, no trailing newline."""
    return FIRST_LINE + "\n" + SECOND_LINE


def find_problem(text):
    """Return what is wrong with the entry, or None when it is fine.

    The gate allows 1-280 characters total, so the two lines plus the
    single newline between them must stay inside that limit.
    """
    if not text or not text.strip():
        return "entry is empty or only whitespace"
    if len(text) > LIMIT_CHARS:
        return "entry is %d characters, over the %d limit" % (
            len(text),
            LIMIT_CHARS,
        )
    lines = text.split("\n")
    if len(lines) != 2:
        return "entry must be exactly two lines, found %d" % len(lines)
    # Each line is a single sentence: one full stop, at the very end.
    for number, line in enumerate(lines, start=1):
        if not line.strip():
            return "line %d is empty" % number
        if line != line.strip():
            return "line %d has leading or trailing whitespace" % number
        if line.count(".") != 1 or not line.endswith("."):
            return "line %d must be exactly one sentence" % number
    return None


def main():
    text = build_entry()
    problem = find_problem(text)
    if problem:
        print("invalid entry: " + problem)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(target, encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            print("read-back did not match the entry")
            return 1
    print("wrote %d characters to %s" % (len(text), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
