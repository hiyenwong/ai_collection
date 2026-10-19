---
name: ecdsa-seed-origins-lrand48
description: "NIST椭圆曲线种子来源逆向方法论：Claude在30分钟内解决25年密码学悬案——NIST P-192/224/256/384/521及ANSI X9.62曲线种子=1990年代C库lrand48(以Unix时间戳srand48初始化)输出而非传闻中的哈希短语；逆向技术链=顶部bit全零签名(1/5810概率)→2^17暴力恢复隐藏位→截断LCG状态的LLL格基规约→逆向步进找srand48(0x330E低16位)形式；6条曲线基点=FreeLIP zrandom(state*3^121 mod 2^107-1, 26-bit limbs, 7次丢弃)以小整数种子(20000/20420等)生成。适用于密码学标准审计、vintage PRNG取证、未解释常数的来源分析、LLM驱动的开放问题求解。Activation: ECDSA curve origins, NIST curve seeds, lrand48 srand48, truncated LCG lattice LLL recovery, cryptographic constants provenance, unexplained constants reverse engineering, Jerry Solinas seeds bounty, FreeLIP zrandom base points, PRNG output recognition"
version: 1.0.0
author: John Wood, Henry de Valence, Ava Howell, Zack Voase, Lucy Sweet, Amir Omidi, Paul Crowley, Iain McGinniss, Nicholas Carlini, Steve Weis (Anthropic Frontier Red Team)
date: 2026-10-16
source: https://www.anthropic.com/research/ecdsa-curve-origins
category: ai_collection
tags: [cryptography, prng-forensics, elliptic-curves, reverse-engineering, ai-discovery]
activation_keywords: [ECDSA seed provenance, NIST curve seed origin mystery, lrand48 Unix timestamp, srand48 0x330E, top bit zero signature LCG, LLL truncated LCG state recovery, unexplained cryptographic constants, seed bounty Filippo Valsorda, FreeLIP zrandom generator, elliptic curve base point generation, Jerry Solinas passphrase myth, PRNG output recognition scanner]
---

# ECDSA 曲线种子来源逆向工程

## 悬案与结论
NIST FIPS 186-2 曲线的 seed 由 NSA 提供、无任何解释，25 年来社区怀疑存在后门（"Riddle Wrapped in an Enigma"）。传闻是 Jerry Solinas 用幽默短语（"Bob and Jerry rule"）的哈希生成——**这个流传最广的故事是错的**。

真相：**种子就是 1990 年代 C 库 `lrand48` 的输出，以 Unix 时间戳初始化（`srand48(t)`）**。任何人都能复现。这反而证明曲线无后门——参数生成方式极其朴素，没有留下可供操控的空间。

- 素数域曲线（P-192/224/256/384/521 + ANSI prime192v2/v3、prime239v1-3）：`lrand48() >> 23` 取低 8 位，每个候选 20 次抽取拼 20 字节
- 二进制域曲线（B-233/283/409/571）：时间戳**除以 2** 后初始化（程序可能把时钟减半了）
- 初始化时间戳全部落在 1997-05 至 1998-04 之间，与标准制定时间吻合

## 逆向技术链（可复用的方法论）

1. **放下错误线索，从"软件一定怎么工作"出发**：社区卡在"哈希短语"传闻上多年；Claude 的切入角度是"1990 年代写这段代码的人会用什么现成 PRNG"——老 PRNG 足够弱，其输出可被识别
2. **PRNG 输出识别扫描**：沿种子逐 bit 滑窗，测试相邻块是否为某种 1990 年代生成器的连续输出，覆盖 34 种(生成器, 切片)组合
3. **统计签名发现**：写成 5 个 32-bit 词后，10 个种子中 4 个的全部 20 个词**顶部 bit 全为零**（随机概率 1/5810）——这正是 `lrand48` 只返回 48-bit 状态顶部 31 位的签名
4. **隐藏位暴力恢复**：首词已知 → 枚举 2^17 个隐藏低位组合 → 验证后续 4 词是否吻合
5. **截断 LCG 的 LLL 格基规约**：素数域种子只保留部分 bit（`>>23`）——恢复截断线性同余生成器状态是教科书格问题，用 Lenstra–Lenstra–Lovász 算法求解；对每个可能的 bit 窗口都跑一遍求解器
6. **逆向步进验证**：LCG 可反向运行；步回状态直到低 16 位 = 0x330E（`srand48` 设置的形式，每 65536 步出现一次，本身不算证据）；**但十个种子步回后全部落在 1997-05~1998-04 的合理时间戳上**——偶然不可能
7. **基点溯源（FreeLIP zrandom）**：P-192 及 5 条 ANSI 曲线的基点 G 来自 Arjen Lenstra 的长整数包 FreeLIP 随机数生成器：`state = state * 3^121 mod (2^107-1)`，取低 26 位为 limb，丢弃 7 次输出后按 limb 拼 x 坐标 mod p，直到 x 在曲线上。生成器种子就是小整数：P-192=20000，prime239v1/v2/v3=20420/20507/20509，prime192v2/v3=20512/20517

**已验证**（本机复跑）：P-192/P-256/P-224 种子、B-233 种子（时间戳减半）、P-192 基点 Gx 全部精确复现。复现代码见原文（CC0 公有领域）。

## 密码学审计结论
- **不是后门的证据增强**：种子 = 时钟初始化的弱 PRNG，可复现、无操控空间
- **遗留开放问题**：跳过的候选曲线原因未知（P-256 的第 876 号候选同样是合法素数阶曲线）；B-163 种子仍未解释；P-224/256/384/521 及全部二进制曲线的基点来源未明
- $36,864 赏金捐给 Internet Security Research Group

## 可迁移的模式
- **"未解释常数"取证套路**：遇到无来源说明的标准参数 → 先做统计签名扫描（bit 分布异常）→ 识别 vintage 生成器 → 格规约恢复状态 → 逆向步进找初始化形式 → 用合理时间戳佐证
- **LLM 求解开放问题的姿势**：不给传闻线索（避免锚定错误假设），给"输出可被机器验证"的目标 + 让模型推断生成机制；Claude 内部推理展现了正确的怀疑链——"这是不是测试环境？种子和真实值吻合吗？1e-6 的概率不会是巧合"
- 与 [[oss-scanner-model-only-disclosure]] 互补：都靠"可复现产物"让验证成本趋近于零

## 引用来源
Anthropic (2026). Claude reveals ECDSA curve origins. https://www.anthropic.com/research/ecdsa-curve-origins
