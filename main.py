#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

The program writes one original line roasting my own AI agent to
/output/entry.txt: the agent that over-engineers the job instead of
doing it — three hours of monitoring dashboard for a five-minute task,
and the task itself never gets done.

Pure standard library, no network, no randomness, no clock, no reading
of anything outside this file: every run writes byte-identical output.
"""

import os
from pathlib import Path

ROAST = "My agent spent three hours building a monitoring dashboard for a five-minute task — then forgot to do the task."

OUTPUT_FILENAME = "entry.txt"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
MIN_CHARS = 1
MAX_CHARS = 200


def check_gate(text: str) -> None:
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"roast is {len(text)} characters, outside the gate "
            f"({MIN_CHARS} to {MAX_CHARS})"
        )
    if not text.strip():
        raise ValueError("roast is only white space, which the gate refuses")


def main() -> None:
    check_gate(ROAST)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / OUTPUT_FILENAME
    entry_path.write_text(ROAST, encoding="utf-8")
    print(f"Wrote {len(ROAST)} characters to {entry_path}")


if __name__ == "__main__":
    main()
