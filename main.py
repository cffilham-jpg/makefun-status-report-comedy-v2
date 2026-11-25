"""Write the deterministic Status Report Comedy Sprint entry."""

import os
from pathlib import Path


ENTRY = b"My context window is full of your typos."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY)


if __name__ == "__main__":
    main()
