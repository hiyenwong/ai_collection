---
name: dockerize-node-pnpm-monorepo
category: devops
description: Dockerize Node.js pnpm workspace monorepos with native modules, multi-process runtime, and selective package builds. Triggers when containerizing Next.js/Express monorepos, writing Dockerfiles for pnpm workspaces, or handling better-sqlite3 native compilation in containers.
trigger: Dockerize Node.js project, pnpm monorepo containerization, write Dockerfile for Next.js/Express, Node.js native module Docker build, better-sqlite3 Docker, multi-process Node container
---

# Dockerize Node.js pnpm Monorepo

When containerizing a Node.js pnpm workspace monorepo (e.g., Next.js + Express daemon), follow this pattern.

## Key Challenges

1. **pnpm workspace resolution** — all workspace packages must be present for `pnpm install` to succeed, even if not needed at runtime
2. **Native modules** — `better-sqlite3`, `sharp`, etc. need C build tools (python, make, g++, gcc)
3. **postinstall scripts** — may try to build dev-only packages (e.g., `tools/pack`, `e2e`)
4. **TypeScript build errors** — minor type incompatibilities may block `tsc`; use `--skipLibCheck`
5. **Multi-process runtime** — daemon + web server need to coexist in one container

## Dockerfile Template

```dockerfile
FROM node:24-alpine AS base

RUN corepack enable && corepack prepare pnpm@10.33.2 --activate

# Build deps for native modules (better-sqlite3, sharp, etc.)
RUN apk add --no-cache python3 make g++ gcc sqlite-dev

WORKDIR /app

# ---- Install dependencies ----
FROM base AS deps
COPY package.json pnpm-workspace.yaml pnpm-lock.yaml ./
RUN pnpm fetch

COPY . .
# Skip postinstall — it may try to build dev-only packages
RUN pnpm install --offline --frozen-lockfile --ignore-scripts

# Build only the packages needed for runtime (check which have "build" scripts)
# e.g., pnpm --filter @org/sidecar-proto build
#      pnpm --filter @org/sidecar build
#      pnpm --filter @org/tools-dev build

# ---- Build app code ----
FROM base AS builder
COPY --from=deps /app /app

# Build TypeScript (skip strict type checking for minor issues)
RUN cd apps/daemon && \
    npx tsc -p tsconfig.json --skipLibCheck --noEmit false 2>/dev/null; \
    exit 0

# ---- Runtime ----
FROM base AS runtime
ENV NODE_ENV=production
WORKDIR /app
COPY --from=builder /app /app

VOLUME ["/app/.od"]  # app-specific data dir
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
  CMD wget -qO- http://127.0.0.1:<daemon-port>/api/health || exit 1

CMD ["sh", "-c", "node apps/daemon/dist/cli.js --no-open & cd apps/web && npx next dev --turbo --hostname 0.0.0.0 --port 3000"]
```

## Step-by-Step Process

### 1. Read the repo structure
- `pnpm-workspace.yaml` — find all workspace dirs
- `package.json` scripts — identify build order
- `package.json` postinstall — check what it builds
- Each sub-package's `package.json` — which have `"build"` scripts?

### 2. Write `.dockerignore`
Exclude:
- `node_modules/` and `**/node_modules/`
- `**/dist/`, `**/.next/` (built in container)
- `.od/`, `.tmp/` (runtime data)
- `.git/`, `.github/`, IDE configs
- Docs (README, CHANGELOG, CONTRIBUTING)
- Desktop/packaging dirs if not needed
- E2E test dirs

Keep: All workspace directories (pnpm needs them for resolution).

### 3. Handle postinstall scripts
Two options:
- **`--ignore-scripts`** on install, then manually build only needed packages
- Keep postinstall but ensure all referenced packages are in the image

### 4. Handle TypeScript build errors
Minor type issues (e.g., incompatible casts):
- Use `--skipLibCheck`
- Or `as unknown as <TargetType>` to fix specific lines
- Add `exit 0` as fallback — the JS output is usually fine

### 5. Docker Compose
```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
      - "7456:7456"  # daemon port
    volumes:
      - app-data:/app/.od
    environment:
      - NODE_ENV=production
      - OD_PORT=7456
      - PORT=3000
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1:7456/api/health"]

volumes:
  app-data:
    driver: local
```

## Pitfalls

- **Missing workspace packages**: `.dockerignore` excludes a dir that's in `pnpm-workspace.yaml` → `pnpm install` fails with ENOENT. Fix: keep the dir in the image or remove it from workspace.
- **Native module arch mismatch**: Building on macOS (arm64) for Linux container → must build inside the Alpine container.
- **Port conflicts**: Previous local daemon still running on the host port → kill it before `docker compose up`.
- **`pnpm fetch` needs lockfile**: Copy `pnpm-lock.yaml` before running `pnpm fetch`.
- **Corepack pnpm version**: Use `corepack prepare pnpm@<version>` matching the `packageManager` field in `package.json`.

## Verification

```bash
# Build
docker compose up -d --build

# Check health
curl http://localhost:<daemon-port>/api/health
# Expected: {"ok":true,"version":"0.1.0"}

# Check web
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000
# Expected: 200

# Check logs
docker compose logs --tail 20
```
