#!/usr/bin/env python3
"""Example usage for the thsdk-stock skill."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import fetch_history  # type: ignore  # noqa: E402
import fetch_realtime  # type: ignore  # noqa: E402


def main() -> int:
    code = "SZ300033"

    print("# Realtime depth example")
    realtime_payload = fetch_realtime.fetch_realtime(
        code, mode="depth", client=fetch_realtime.MockTHS()
    )
    print(json.dumps(realtime_payload, ensure_ascii=False, indent=2))

    print("\n# Historical K-line example")
    history_payload = fetch_history.fetch_history(
        code=code,
        interval="day",
        adjust="forward",
        count=2,
        client=fetch_history.MockTHS(),
    )
    print(json.dumps(history_payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
