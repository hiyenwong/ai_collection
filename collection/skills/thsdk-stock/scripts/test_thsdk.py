#!/usr/bin/env python3
"""Offline tests for the thsdk-stock skill."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载模块: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_cli(*args: str) -> dict:
    completed = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT.parent,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def main() -> int:
    realtime = load_module("fetch_realtime.py", "fetch_realtime")
    history = load_module("fetch_history.py", "fetch_history")

    realtime_payload = realtime.fetch_realtime(
        "SZ300033", mode="depth", client=realtime.MockTHS()
    )
    assert_true(realtime_payload["code"] == "SZ300033", "实时行情返回的 code 不正确")
    assert_true(realtime_payload["mode"] == "depth", "实时行情返回的 mode 不正确")
    assert_true(len(realtime_payload["records"]) == 1, "实时行情 mock 数据条数不正确")

    intraday_payload = realtime.fetch_realtime(
        "SZ300033", mode="intraday", client=realtime.MockTHS()
    )
    assert_true(len(intraday_payload["records"]) == 2, "分时 mock 数据条数不正确")

    history_payload = history.fetch_history(
        code="SZ300033",
        interval="day",
        adjust="forward",
        count=2,
        client=history.MockTHS(),
    )
    assert_true(history_payload["interval"] == "day", "历史数据 interval 不正确")
    assert_true(history_payload["adjust"] == "forward", "历史数据 adjust 不正确")
    assert_true(len(history_payload["records"]) == 2, "历史 K 线 mock 数据条数不正确")

    realtime_cli = run_cli("scripts/fetch_realtime.py", "--code", "SZ300033", "--mock")
    assert_true(realtime_cli["code"] == "SZ300033", "实时 CLI 输出不正确")

    history_cli = run_cli(
        "scripts/fetch_history.py", "--code", "SZ300033", "--mock", "--count", "1"
    )
    assert_true(len(history_cli["records"]) == 1, "历史 CLI 输出条数不正确")

    print("All thsdk-stock tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
