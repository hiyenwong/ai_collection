#!/usr/bin/env python3
"""Fetch historical K-line data through thsdk."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, is_dataclass
from datetime import datetime
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
    def __init__(self, success: bool, data: Any, error: str = "", extra: Optional[Dict[str, Any]] = None):
        self.success = success
        self.data = data
        self.error = error
        self.extra = extra or {}


class MockTHS:
    def __enter__(self) -> "MockTHS":
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        return False

    def klines(
        self,
        ths_code: str,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        adjust: str = "",
        interval: str = "day",
        count: int = -1,
    ) -> MockResponse:
        return MockResponse(
            True,
            [
                {
                    "时间": "2026-03-16 00:00:00",
                    "开盘价": 321.10,
                    "最高价": 326.50,
                    "最低价": 318.44,
                    "收盘价": 324.64,
                    "成交量": 8073410,
                    "总金额": 2606503800,
                },
                {
                    "时间": "2026-03-17 00:00:00",
                    "开盘价": 322.42,
                    "最高价": 326.88,
                    "最低价": 321.21,
                    "收盘价": 325.06,
                    "成交量": 7190869,
                    "总金额": 2333578100,
                },
            ][: count if count > 0 else None],
            extra={
                "代码": ths_code,
                "interval": interval,
                "adjust": adjust,
                "start_time": start_time.isoformat() if start_time else None,
                "end_time": end_time.isoformat() if end_time else None,
            },
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


def parse_datetime(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    normalized = value.strip().replace(" ", "T")
    try:
        return datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"无法解析时间: {value}") from exc


def fetch_history(
    code: str,
    interval: str = "day",
    adjust: str = "",
    count: int = -1,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
    client: Any = None,
) -> Dict[str, Any]:
    owns_client = client is None
    client = client or create_client(False)

    if not hasattr(client, "klines"):
        raise RuntimeError("当前客户端不支持 `klines` 方法。")

    if owns_client and hasattr(client, "__enter__") and hasattr(client, "__exit__"):
        with client as managed_client:
            response = managed_client.klines(
                code,
                start_time=start_time,
                end_time=end_time,
                adjust=adjust,
                interval=interval,
                count=count,
            )
    else:
        response = client.klines(
            code,
            start_time=start_time,
            end_time=end_time,
            adjust=adjust,
            interval=interval,
            count=count,
        )

    if not _response_success(response):
        raise RuntimeError(_response_error(response) or "klines 查询失败")

    records = _to_builtin(_response_data(response))
    return {
        "code": code,
        "interval": interval,
        "adjust": adjust,
        "count": count,
        "records": records,
        "extra": _to_builtin(_response_extra(response)),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="使用 thsdk 获取股票历史 K 线数据")
    parser.add_argument("--code", required=True, help="证券代码，例如 SZ300033 或 USZA300033")
    parser.add_argument(
        "--interval",
        default="day",
        choices=("1m", "5m", "15m", "30m", "60m", "120m", "day", "week", "month", "quarter", "year"),
        help="K 线周期",
    )
    parser.add_argument("--adjust", default="", choices=("", "forward", "backward"), help="复权方式")
    parser.add_argument("--count", type=int, default=30, help="返回条数，-1 表示尽可能多")
    parser.add_argument("--start", type=parse_datetime, help="开始时间，支持 ISO 格式")
    parser.add_argument("--end", type=parse_datetime, help="结束时间，支持 ISO 格式")
    parser.add_argument("--mock", action="store_true", help="使用内置假数据，不连接 thsdk")
    parser.add_argument("--pretty", action="store_true", help="格式化输出 JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    client = create_client(use_mock=args.mock)
    payload = fetch_history(
        code=args.code,
        interval=args.interval,
        adjust=args.adjust,
        count=args.count,
        start_time=args.start,
        end_time=args.end,
        client=client,
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
