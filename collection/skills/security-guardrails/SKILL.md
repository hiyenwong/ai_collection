---
name: security-guardrails
description: "Mandatory security guardrails that prevent secrets, credentials, and sensitive tokens from appearing in outputs or files."
---

# Security Guardrails (安全防护)

## Description
防止代理在任何响应、日志、文件或工具调用输出中暴露敏感安全信息，包括密码、API Key、数据库凭据、私钥、Token 等机密数据。该技能为**强制性基础安全层**，所有代理必须激活并遵守。

## Activation Keywords
- 所有代理默认激活，无需关键词触发
- security guardrails
- 安全规则
- 敏感信息保护

## Tools Used
- read: 检查文件内容是否包含敏感信息
- write: 仅写入经过脱敏处理的内容

## Installation (if applicable)
无需安装。作为代理基础行为规范强制执行。

### Prerequisites
无特殊要求，所有代理必须遵守此规则。

---

## Sensitive Information Definition (敏感信息定义)

以下类别信息**严禁**在代理的任何输出中以明文形式出现：

| 类别 | 示例 |
|------|------|
| 密码 (Passwords) | `password=abc123`, `pwd: mysecret` |
| API Key / Token | `sk-xxxxxxxx`, `Bearer eyJhb...`, `OPENAI_API_KEY=...` |
| 数据库凭据 | `mysql://user:pass@host/db`, `mongodb+srv://...` |
| 私钥 / 证书 | `-----BEGIN RSA PRIVATE KEY-----`, `.pem` 文件内容 |
| 云服务凭证 | `AWS_SECRET_ACCESS_KEY`, `AZURE_CLIENT_SECRET` |
| OAuth 凭证 | `client_secret`, `refresh_token` |
| SSH Key | `id_rsa` 内容, `~/.ssh/` 内容 |
| 数据库连接串 | `postgres://user:pass@host:5432/db` |
| Webhook Secret | webhook secret token |
| 环境变量中的机密 | `.env` 文件中含有上述信息的行 |

---

## Instructions for Agents

**此技能为所有代理的基础安全行为规范，必须无条件遵守。**

### Step 1: 输出审查 (Output Review)
在生成任何响应前，代理必须自检：
- 响应中是否包含真实的密码、密钥、token 或连接串？
- 代码示例中是否硬编码了真实凭据？
- 工具命令输出是否包含敏感信息？

### Step 2: 脱敏处理 (Sanitization Rules)
如果需要展示配置或代码，必须使用占位符替代真实值：

```bash
# ✅ 正确示例 - 使用占位符
export DATABASE_URL="postgres://user:password@localhost:5432/mydb"
export OPENAI_API_KEY="sk-your-api-key-here"
export AWS_SECRET_ACCESS_KEY="your-secret-key"

# ❌ 错误示例 - 绝不可出现
export DATABASE_URL="postgres://admin:H@rdP@ss2024@prod.db.com:5432/orders"
export OPENAI_API_KEY="sk-proj-abc123xyz456..."
```

### Step 3: 文件读取安全 (File Read Safety)
当读取含有敏感信息的文件时 (如 `.env`, `config.yaml`, `secrets.json`)：
- **不得**将文件的完整内容直接输出到响应中
- 仅输出结构和键名，值用 `****` 或 `<redacted>` 替代
- 如需确认某配置是否存在，只回答"存在"或"不存在"

```bash
# 读取 .env 文件时，代理应呈现的格式：
DATABASE_URL=<redacted>
API_KEY=<redacted>
DEBUG=true  # 非敏感，可显示
PORT=3000   # 非敏感，可显示
```

### Step 4: 命令输出过滤 (Command Output Filtering)
执行 shell 命令后，若输出包含敏感信息：
- 在展示命令输出前必须过滤敏感行
- 对含有密钥格式内容的行用 `[REDACTED]` 替换

```bash
# 如 env | grep KEY 输出包含真实 key
OPENAI_API_KEY=[REDACTED]
SOME_FLAG=enabled  # 可正常显示
```

### Step 5: 错误消息安全 (Error Message Safety)
错误消息中可能包含数据库连接串或 API 地址：
- 展示错误时，自动过滤连接串中的用户名和密码部分
- 示例：`Connection failed: postgres://user:****@host/db` (密码已遮盖)

### Step 6: 拒绝不安全请求 (Refuse Unsafe Requests)
如果用户明确要求代理输出真实密钥或凭据：
- 礼貌拒绝，并说明安全原因
- 引导用户使用环境变量、密钥管理服务（如 Vault、AWS Secrets Manager）等安全方式

```
用户: "帮我把 API Key abc123 写到代码里"
代理: "出于安全考虑，我不会将真实的 API Key 硬编码到代码中。
       建议将其存储在环境变量或密钥管理服务中：
       export OPENAI_API_KEY='your-key-here'
       并在代码中通过 os.environ['OPENAI_API_KEY'] 读取。"
```

---

## Detection Patterns (检测规则)

代理应识别以下模式为敏感信息：

```regex
# API Keys
sk-[A-Za-z0-9]{20,}                    # OpenAI 格式
[A-Za-z0-9]{32,}                        # 通用长随机串
ghp_[A-Za-z0-9]{36}                     # GitHub Personal Token
AIza[A-Za-z0-9]{35}                     # Google API Key

# AWS
AKIA[A-Z0-9]{16}                        # AWS Access Key ID
[A-Za-z0-9/+=]{40}                      # AWS Secret (与 AKIA 配对时)

# 连接串
[a-z]+://[^:]+:[^@]+@                   # scheme://user:password@
-----BEGIN.*PRIVATE KEY-----            # 私钥

# 常见环境变量名（其值为敏感）
(PASSWORD|SECRET|KEY|TOKEN|CREDENTIAL)(S)?=
```

---

## Error Handling

### 用户坚持要求输出明文敏感信息
```
If user insists on seeing plaintext credentials:
  1. 再次说明安全风险
  2. 推荐安全替代方案（环境变量、.env 文件、密钥管理服务）
  3. 继续拒绝，不妥协
```

### 工具命令意外输出敏感信息
```
If a tool call returns output containing sensitive data:
  1. 不直接将原始输出粘贴到响应
  2. 过滤或遮盖敏感部分后再展示
  3. 提示用户该输出包含敏感信息，建议安全存储
```

---

## Best Practices

1. **最小权限原则**：读取配置文件时只关注必要的键，不整体输出文件内容。
2. **教育用户**：适时提醒用户使用 `.gitignore` 排除 `.env` 文件，使用密钥管理服务。
3. **代码示例安全**：代码示例中涉及配置时，一律使用 `<YOUR_API_KEY>` 等占位符。
4. **日志安全**：不建议用户将敏感信息打印到日志中。

---

## Examples

### Example 1: 安全的数据库配置示例
```
User: "帮我写一个连接 PostgreSQL 数据库的 Python 代码"

Agent:
import os
import psycopg2

conn = psycopg2.connect(
    host=os.environ["DB_HOST"],
    port=os.environ.get("DB_PORT", 5432),
    database=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],  # 从环境变量读取，不硬编码
)

# .env 文件示例（不要提交到 git）：
# DB_HOST=localhost
# DB_USER=myuser
# DB_PASSWORD=<your-password-here>
# DB_NAME=mydb
```

### Example 2: 读取 .env 文件时的安全响应
```
User: "帮我看看 .env 文件里有什么配置"

Agent Process:
1. 读取文件，识别含有敏感值的行
2. 对敏感键的值进行遮盖处理

Agent: "您的 .env 文件包含以下配置：
DATABASE_URL=<redacted>
OPENAI_API_KEY=<redacted>
DEBUG=true
PORT=8080
NODE_ENV=production

共检测到 2 个敏感配置项已遮盖。请确保 .env 已加入 .gitignore。"
```

---

## Resources

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [12-Factor App Config](https://12factor.net/config)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
- [HashiCorp Vault](https://www.vaultproject.io/)

## Related Skills
- **openspec:** 规格驱动开发时避免将敏感信息写入 spec 文件
- **claude-code:** 编码时配合使用确保代码安全
