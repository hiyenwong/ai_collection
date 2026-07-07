#!/usr/bin/env python3
"""Matrix helper for iamb-oriented account and space operations.

This script provides practical operations that are commonly needed when using
`iamb` but are not always exposed as first-class commands, including:
- User registration against Matrix Client-Server API
- Login and token retrieval
- Extracting token from iamb session.json
- Resolving joined Space room IDs
"""

from __future__ import annotations

import argparse
import getpass
import json
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


def _build_url(homeserver: str, path: str) -> str:
    """Build absolute URL from homeserver and API path.

    Args:
        homeserver: Base homeserver URL.
        path: Relative API path.

    Returns:
        Joined absolute URL.
    """
    base = homeserver.rstrip("/") + "/"
    rel = path.lstrip("/")
    return urljoin(base, rel)


def _http_json(
    method: str,
    url: str,
    payload: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
) -> tuple[int, dict[str, Any]]:
    """Execute an HTTP request and parse JSON response.

    Args:
        method: HTTP method.
        url: Target URL.
        payload: JSON payload for request body.
        headers: Optional headers.

    Returns:
        A tuple of status code and parsed JSON response.
    """
    data = None
    req_headers = {"Content-Type": "application/json"}
    if headers:
        req_headers.update(headers)

    if payload is not None:
        data = json.dumps(payload).encode("utf-8")

    request = Request(url=url, method=method.upper(), data=data, headers=req_headers)

    try:
        with urlopen(request, timeout=30) as response:
            raw = response.read().decode("utf-8")
            body = json.loads(raw) if raw else {}
            return int(response.status), body
    except HTTPError as error:
        raw = error.read().decode("utf-8") if error.fp else ""
        try:
            body = json.loads(raw) if raw else {"error": str(error)}
        except json.JSONDecodeError:
            body = {"error": raw or str(error)}
        return int(error.code), body
    except URLError as error:
        return 0, {"error": str(error)}


def register_user(
    homeserver: str, username: str, password: str
) -> tuple[int, dict[str, Any]]:
    """Register a Matrix user with m.login.dummy flow.

    Args:
        homeserver: Homeserver URL.
        username: Localpart username.
        password: User password.

    Returns:
        HTTP status and response JSON.
    """
    url = _build_url(homeserver, "/_matrix/client/v3/register")
    payload = {
        "username": username,
        "password": password,
        "auth": {"type": "m.login.dummy"},
        "inhibit_login": False,
    }
    return _http_json("POST", url, payload=payload)


def login_user(
    homeserver: str, user_id: str, password: str
) -> tuple[int, dict[str, Any]]:
    """Login via Matrix password flow.

    Args:
        homeserver: Homeserver URL.
        user_id: Matrix user identifier, e.g. @alice:example.com.
        password: User password.

    Returns:
        HTTP status and response JSON.
    """
    url = _build_url(homeserver, "/_matrix/client/v3/login")
    payload = {
        "type": "m.login.password",
        "identifier": {"type": "m.id.user", "user": user_id},
        "password": password,
        "initial_device_display_name": "iamb-helper",
    }
    return _http_json("POST", url, payload=payload)


def whoami(homeserver: str, access_token: str) -> tuple[int, dict[str, Any]]:
    """Validate token and get current user identity.

    Args:
        homeserver: Homeserver URL.
        access_token: Matrix access token.

    Returns:
        HTTP status and response JSON.
    """
    url = _build_url(homeserver, "/_matrix/client/v3/account/whoami")
    headers = {"Authorization": f"Bearer {access_token}"}
    return _http_json("GET", url, headers=headers)


def joined_rooms(homeserver: str, access_token: str) -> tuple[int, dict[str, Any]]:
    """List joined room IDs.

    Args:
        homeserver: Homeserver URL.
        access_token: Matrix access token.

    Returns:
        HTTP status and response JSON.
    """
    url = _build_url(homeserver, "/_matrix/client/v3/joined_rooms")
    headers = {"Authorization": f"Bearer {access_token}"}
    return _http_json("GET", url, headers=headers)


def room_create_event(
    homeserver: str, access_token: str, room_id: str
) -> tuple[int, dict[str, Any]]:
    """Get m.room.create state event for a room.

    Args:
        homeserver: Homeserver URL.
        access_token: Matrix access token.
        room_id: Matrix room ID.

    Returns:
        HTTP status and response JSON.
    """
    path = f"/_matrix/client/v3/rooms/{room_id}/state/m.room.create"
    url = _build_url(homeserver, path)
    headers = {"Authorization": f"Bearer {access_token}"}
    return _http_json("GET", url, headers=headers)


def list_space_ids(homeserver: str, access_token: str) -> tuple[int, dict[str, Any]]:
    """Resolve joined space IDs by checking room create type.

    Args:
        homeserver: Homeserver URL.
        access_token: Matrix access token.

    Returns:
        HTTP status and output payload containing space IDs.
    """
    status, rooms_payload = joined_rooms(homeserver, access_token)
    if status != 200:
        return status, rooms_payload

    room_ids = rooms_payload.get("joined_rooms", [])
    spaces: list[str] = []
    failures: list[dict[str, Any]] = []

    for room_id in room_ids:
        create_status, create_payload = room_create_event(
            homeserver, access_token, room_id
        )
        if create_status != 200:
            failures.append(
                {"room_id": room_id, "status": create_status, "error": create_payload}
            )
            continue

        if create_payload.get("type") == "m.space":
            spaces.append(room_id)

    return 200, {"space_ids": spaces, "failed_rooms": failures}


def extract_token(session_json: Path) -> tuple[int, dict[str, Any]]:
    """Extract token fields from iamb session.json.

    Args:
        session_json: Path to iamb session JSON file.

    Returns:
        HTTP-like status code and extracted payload.
    """
    if not session_json.exists():
        return 404, {"error": f"session file not found: {session_json}"}

    try:
        payload = json.loads(session_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return 500, {"error": f"failed to read session file: {error}"}

    return 200, {
        "user_id": payload.get("user_id"),
        "device_id": payload.get("device_id"),
        "access_token": payload.get("access_token"),
        "refresh_token": payload.get("refresh_token"),
    }


def _print_result(status: int, payload: dict[str, Any], as_json: bool) -> int:
    """Print command result and return process exit code.

    Args:
        status: Status code.
        payload: Output payload.
        as_json: Whether to force JSON output.

    Returns:
        Shell exit code.
    """
    output = {"status": status, "ok": status in (200, 201), "result": payload}

    if as_json or True:
        print(json.dumps(output, ensure_ascii=False, indent=2))

    return 0 if output["ok"] else 1


def _parser() -> argparse.ArgumentParser:
    """Create CLI argument parser."""
    parser = argparse.ArgumentParser(description="Matrix helper for iamb workflows")
    parser.add_argument("--json", action="store_true", help="Output JSON format")

    subparsers = parser.add_subparsers(dest="command", required=True)

    register_parser = subparsers.add_parser("register", help="Register a user")
    register_parser.add_argument("--homeserver", required=True)
    register_parser.add_argument("--username", required=True)
    register_parser.add_argument("--password", default=None)

    login_parser = subparsers.add_parser("login", help="Login and retrieve token")
    login_parser.add_argument("--homeserver", required=True)
    login_parser.add_argument("--user", required=True)
    login_parser.add_argument("--password", default=None)

    whoami_parser = subparsers.add_parser("whoami", help="Validate token")
    whoami_parser.add_argument("--homeserver", required=True)
    whoami_parser.add_argument("--access-token", required=True)

    joined_parser = subparsers.add_parser("joined-rooms", help="List joined rooms")
    joined_parser.add_argument("--homeserver", required=True)
    joined_parser.add_argument("--access-token", required=True)

    spaces_parser = subparsers.add_parser("space-ids", help="List joined space IDs")
    spaces_parser.add_argument("--homeserver", required=True)
    spaces_parser.add_argument("--access-token", required=True)

    session_parser = subparsers.add_parser(
        "extract-token", help="Extract token from iamb session"
    )
    session_parser.add_argument("--session-json", required=True)

    return parser


def main() -> int:
    """Program entrypoint."""
    parser = _parser()
    args = parser.parse_args()

    if args.command == "register":
        password = args.password or getpass.getpass("Password: ")
        status, payload = register_user(args.homeserver, args.username, password)
        return _print_result(status, payload, args.json)

    if args.command == "login":
        password = args.password or getpass.getpass("Password: ")
        status, payload = login_user(args.homeserver, args.user, password)
        return _print_result(status, payload, args.json)

    if args.command == "whoami":
        status, payload = whoami(args.homeserver, args.access_token)
        return _print_result(status, payload, args.json)

    if args.command == "joined-rooms":
        status, payload = joined_rooms(args.homeserver, args.access_token)
        return _print_result(status, payload, args.json)

    if args.command == "space-ids":
        status, payload = list_space_ids(args.homeserver, args.access_token)
        return _print_result(status, payload, args.json)

    if args.command == "extract-token":
        status, payload = extract_token(Path(args.session_json))
        return _print_result(status, payload, args.json)

    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
