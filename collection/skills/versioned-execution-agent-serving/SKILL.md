---
name: versioned-execution-agent-serving
description: RETIRE versioned execution for LLM agent serving. Use when agents interrupt, abort, or revise running requests. (arXiv:2610.01160)
category: ai_collection
---

# Versioned Execution for Interruptible Agents (RETIRE)

**Paper**: "Serving a Revisable World: Versioned Execution for Interruptible Agents" — Zhang, Sharma, Vegesna, Fu, Liu, Krishnamurthy (NVIDIA), arXiv:2610.01160, cs.DC, 1 Oct 2026. Implemented in vLLM 0.13.0.

## 核心问题

LLM agent 频繁修改运行中的任务（用户改指令、工具失败、新信息改变计划）。今天的推理服务器把"修改"表达为 abort 旧请求 + 提交新请求，这带来两个问题：

1. **过期输出泄漏**：跨 18 个 abort 试验，消费者在 abort 后总共收到 170 个过期 token —— 请求完成与 API 发布是不同时刻，缓冲在队列里的帧无法被 abort 收回。
2. **有用工作被重复计算**：旧计划与新计划共享的上下文前缀（如 repository context）的 KV 状态仍然有价值，但 abort-冷重启迫使后继者重建全部状态。

## 核心抽象：请求 vs 版本

| 概念 | 职责 |
|------|------|
| **Request（请求）** | 拥有调度和内存资源（GPU allocation、KV 块、缓冲） |
| **Execution version（执行版本）** | 拥有**权限（authority）**——发布输出或安装状态的许可 |
| **Scope（作用域）** | 被 runtime 一起替换的工作单元（可含多个请求/分布式 worker），一个 scope 一个当前版本 |

关键解耦：**请求 ID 索引资源，版本决定结果是否可见**。Runtime 提交 `SUPERSEDE(s, e, e+1, X', C)`：s=作用域，e→e+1 版本切换，X'=修订上下文，C=执行契约（规定继承状态何时可接受，含数值模式与干净执行等价性要求）。

## 五阶段版本转换协议

**Revoke first, preserve second（先撤销，后保留）**：

```
ADVANCE   — 权限切换：发布 e+1，拒绝所有携带 e 的输出/提交
FENCE     — 限定过期工作：停止旧版本新 launch，在安全边界关闭 writer，收集参与者回执
ALIGN     — 选择有用状态：LCP（最长公共 token 前缀）∩ 最小 writer-complete 前沿，对齐到块边界；校验模型/缓存配置、租户、generation、传输身份、数值模式
RESUME    — 启动后继者：安装认证前缀（alias 物理页），分配新后缀，以 e+1 准入
RECLAIM   — 异步释放：旧资源在最后使用者 drain 后回收，不在后继者关键路径上
```

阶段依赖：撤销先于发布 → writer 关闭先于继承 → 状态隔离先于回收。**只有不可变、writer-closed 的页才能跨越版本边界**。

## 三大保证（服务边界处强制）

1. **当前版本发布**：token、调度结果、已安装状态仅在属于当前 scope epoch 时可见（在调度、模型完成、进入流式队列、API 消费者接收时四道门检查）。
2. **版本化交接**：前驱状态仅在 token 前缀+执行配置匹配、旧 writer 已关闭、所有权 generation 有效时可被消费；否则后继者重算。
3. **退役状态隔离**：旧工作可以完成，但不可覆写后继者或无关租户的状态。

KV 记录携带 **generation**（分配的所有权实例）；安装时校验 generation，writer fence + 延迟回收保护底层页。

## 关键机制细节

- **Epoch 表示**：版本 = 单调递增 epoch；每个请求、输出帧、模型 step、传输都携带 (scope, epoch) 身份。
- **Safe point（安全点）**：worker 可停止旧版本工作的模型边界。短 decode step 天然频繁到达边界；长 prefill 额外武装设备谓词+有界检查，选择性放置将 decode 开销从 5.25% 降到 1.05%（guarded safe points 35,190→1,080）。
- **Bounded retirement**：FENCE 延迟——长 prefill 3213→129ms（24.9×）、draft-verify prefill 51.3×、active speculative decode 9.99×、两个异构 KV 组 7.01×。
- **Certified inheritance**：继承 4080-token 前缀使后继者 TTFT 快 33.8×（3965ms 冷 prefill → 117ms）。HBM churn 压力下保留认证的 7168-token 前缀，恢复加速最高 6.87×/5.07×（H100 PCIe/GB200）。
- **失败处理**：认证失败 → 冷启动、fresh-generation 后继者；传输在其目标执行被退役后完成 → 拒绝安装。

## 实验结果

| 指标 | Native abort+cold | RETIRE 组合 |
|------|------------------|-------------|
| 修订→后继 TTFT（8K prompt, 90% overlap） | 1127ms | 951ms（-17.1%）|
| 组合分解 | invalidate 单独 -5.6%，inherit 单独 -10.3% | 机制互补可叠加 |
| 120s 真实 coding-agent 突发重放（24 transitions, 3 scopes, CV=3.57） | 40,499 过期 token，3/9 最终版本推进，cleanup >180s | 0 过期 token，9/9 推进，cleanup 1.08ms |
| Current-version goodput | 9.77 tok/s | 54.0 tok/s（5.53×）|
| 分布式（TP×PP 1×2/2×1/2×2×2） | — | FENCE 6.04–12.19×，继承 TTFT 5.27–7.08× |
| 共租户隔离（TP=4） | — | Tenant B 的 KV digest 与 block ID 在 3 seeds 下不变 |

## 可复用设计模式

1. **Resource/Authority 解耦**：任何"运行中可被替换"的系统中，资源生命周期与效果可见性是两个正交轴，应分别建模。请求消失 ≠ 输出不可发布 ≠ 状态不可继承。
2. **Revoke-first**：立即撤销权限（逻辑边界），让物理清理异步进行——正确性依赖"效果可见处强制检查"，不依赖"对象同时消失"。
3. **Writer-closed prefix 认证**：共享状态复用需要 writer 关闭边界 + 所有权 generation 校验，token/字节匹配本身不建立可继承性。
4. **异步 RECLAIM**：只有后继者将消费的状态必须在它启动前就绪；其余释放可 overlap 后继执行。
5. **执行契约 C**：继承的验收标准（数值模式、等价性要求）显式声明，而非隐式假设。
6. **作用域宽度**：分布式参与者（TP/PP worker、多 KV 组、租户）需要在同一权限坐标下协调关闭。

## 局限与适用性

- 需要服务器在所有"效果可见"边界埋点（发布门、调度 commit、KV 安装、传输完成），改造成本集中在控制面。
- 无重叠前缀时（zero-overlap trace），收益只剩 invalidation 部分。
- Revision 压力、retirement horizon、successor overlap、scope width 四个 workload 维度决定收益大小。

## Activation 触发场景

agent serving、request abort、KV cache 继承、prefix reuse、speculative decode 中断、multi-tenant isolation、digital twin 执行切换、任何"live execution 被替换"的并发系统（游戏服务器 tick、数据库 query 取消、机器人任务重规划）。
