#!/usr/bin/env python3
"""Fetch realtime stock data through thsdk."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, is_dataclass
from typing import Any, Dict, Optional


def _response_success(response: Any) -> bool:
    if isinstance(response, dict):
        return bool(response.get("success"))
    return bool(getattr(response, "success", False))


def _response_error(response: Any) -> str:
    if isinstance(response, dict):
        return str(response.get("error", ""))
    return str(getattr(response, "error", ""))


def _response_data(response: Any) -> Any:
    if isinstance(response, dict):
        return response.get("data")
    return getattr(response, "data", None)


def _response_extra(response: Any) -> Dict[str, Any]:
    if isinstance(response, dict):
        extra = response.get("extra", {})
    else:
        extra = getattr(response, "extra", {})
    return extra if isinstance(extra, dict) else {}


def _to_builtin(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {str(k): _to_builtin(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_to_builtin(item) for item in value]
    if is_dataclass(value):
        return _to_builtin(asdict(value))
    to_dict = getattr(value, "to_dict", None)
    if callable(to_dict):
        try:
            return _to_builtin(to_dict(orient="records"))
        except TypeError:
            return _to_builtin(to_dict())
    if hasattr(value, "tolist"):
        return _to_builtin(value.tolist())
    if hasattr(value, "__dict__"):
        return _to_builtin(vars(value))
    return str(value)


class MockResponse:
    def __init__(
        self,
        success: bool,
        data: Any,
        error: str = "",
        extra: Optional[Dict[str, Any]] = None,
    ):
        self.success = success
        self.data = data
        self.error = error
        self.extra = extra or {}


class MockTHS:
    def __enter__(self) -> "MockTHS":
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        return False

    def depth(self, ths_code: str) -> MockResponse:
        return MockResponse(
            True,
            [
                {
                    "买1价": 317.80,
                    "买1量": 12237,
                    "卖1价": 317.81,
                    "卖1量": 8300,
                    "买2价": 317.79,
                    "买2量": 5300,
                    "卖2价": 317.82,
                    "卖2量": 4200,
                }
            ],
            extra={"代码": ths_code, "ServerDelay": 0},
        )

    def intraday_data(self, ths_code: str) -> MockResponse:
        return MockResponse(
            True,
            [
                {
                    "时间": "2026-03-18 09:30:00+08:00",
                    "价格": 317.98,
                    "成交量": 23300,
                    "总金额": 7408934,
                },
                {
                    "时间": "2026-03-18 09:31:00+08:00",
                    "价格": 318.14,
                    "成交量": 126600,
                    "总金额": 40116357,
                },
            ],
            extra={"代码": ths_code, "ServerDelay": 0},
        )


def create_client(use_mock: bool = False):
    if use_mock:
        return MockTHS()

    try:
        from thsdk import THS  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "无法导入 thsdk。请先执行 `pip install thsdk`，或在当前离线环境里加上 `--mock` 做本地验证。"
        ) from exc

    return THS()


def fetch_realtime(
    code: str, mode: str = "depth", client: Any = None
) -> Dict[str, Any]:
    owns_client = client is None
    client = client or create_client(False)

    method_name = "depth" if mode == "depth" else "intraday_data"
    if not hasattr(client, method_name):
        raise RuntimeError(f"当前客户端不支持 `{method_name}` 方法。")

    if owns_client and hasattr(client, "__enter__") and hasattr(client, "__exit__"):
        with client as managed_client:
            response = getattr(managed_client, method_name)(code)
    else:
        response = getattr(client, method_name)(code)

    if not _response_success(response):
        raise RuntimeError(_response_error(response) or f"{method_name} 查询失败")

    records = _to_builtin(_response_data(response))
    return {
        "code": code,
        "mode": mode,
        "records": records,
        "extra": _to_builtin(_response_extra(response)),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="使用 thsdk 获取股票实时行情数据")
    parser.add_argument(
        "--code", required=True, help="证券代码，例如 SZ300033 或 USZA300033"
    )
    parser.add_argument(
        "--mode",
        choices=("depth", "intraday"),
        default="depth",
        help="depth 为五档盘口，intraday 为分时序列",
    )
    parser.add_argument(
        "--mock", action="store_true", help="使用内置假数据，不连接 thsdk"
    )
    parser.add_argument("--pretty", action="store_true", help="格式化输出 JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    client = create_client(use_mock=args.mock)
    payload = fetch_realtime(args.code, mode=args.mode, client=client)
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
