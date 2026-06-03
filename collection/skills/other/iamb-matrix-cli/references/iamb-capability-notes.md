# iamb Capability Notes (from ulyssa/iamb)

## 已确认能力
- 登录方式：Password / SSO / Session Restore（`src/main.rs`, `src/worker.rs`）
- Space 相关命令：`:spaces`, `:space child set/remove`（`src/commands.rs`, `docs/iamb.1`）
- Room ID 显示：`:room id show`（`src/commands.rs` tests）
- 会话持久化：`session.json` 包含 `access_token` / `refresh_token` / `user_id` / `device_id`（`src/config.rs`）

## 能力边界
- iamb 内部命令体系未提供显式“注册新用户”命令。
- 注册流程需走 Matrix Client-Server API（homeserver 可能有 UIA/策略限制）。

## 相关源码位置
- `src/worker.rs`: `login_and_sync`, `space_members`
- `src/commands.rs`: `iamb_spaces`, `iamb_space`, `iamb_room`
- `src/config.rs`: `Session`, `read_session`, `write_session`
- `docs/iamb.1`: General/Space commands
