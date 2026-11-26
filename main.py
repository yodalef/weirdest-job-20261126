#!/usr/bin/env python3
"""Entry for make.fun 'Weirdest Job Title: Blind Judge Showdown'.

Writes one job title (1-60 chars) to the output directory's
entry.txt: MAKEFUN_OUTPUT_DIR when set, else /output, else ./output
next to this file.  No network use.
"""
import os

LINE = "Executive Vice President of Turning It Off and On Again"

MAX_CHARS = 60


def validated_line():
    """The entry title, checked against the competition's 1-60 limit."""
    title = LINE.strip()
    if not 1 <= len(title) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d chars, got %d"
                         % (MAX_CHARS, len(title)))
    if "\n" in title:
        raise ValueError("entry must be a single line")
    return title


def main():
    candidates = []
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        candidates.append(env)
    candidates.append("/output")
    candidates.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"))
    last_err = None
    for out_dir in candidates:
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(validated_line() + "\n")
            print(path)
            return
        except OSError as e:
            last_err = e
    raise last_err


if __name__ == "__main__":
    main()
