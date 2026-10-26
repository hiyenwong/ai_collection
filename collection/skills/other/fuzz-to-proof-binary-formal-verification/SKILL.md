---
name: fuzz-to-proof-binary-formal-verification
description: "Use when turning fuzz tests into binary-level Rocq proofs."
version: 1.0.0
author: Anthropic + Theorem (summarized by Hermes Agent)
date: 2026-10-25
source: https://www.anthropic.com/research/formal-verification
license: MIT
metadata:
  hermes:
    tags: [formal-verification, rocq, coq, risc-v, oss-fuzz, fuzzing, proof-engineering, memory-safety, trusted-computing-base, llm-proof-generation, binary-verification, supply-chain-security]
    related_skills: [fvqkd-rocq-qkd-formal-verification, prove2me-collaborative-autoformalization, hardware-motivated-noise-modeling]
trigger: fuzz test to proof conversion, assembly-level formal verification, RISC-V semantics, Rocq proof at scale, OSS-Fuzz no-crash proof, trusted computing base minimization, proof-driven bug finding, LLM formal verification workflow, memory safety proof, binary-level security guarantee, derived proof obligation, test-to-spec conversion
---

# Fuzz→Proof：LLM 大规模二进制级形式化验证（Anthropic+Theorem）

## 成果基线

- Claude 对 123 个 OSS-Fuzz 开源库的 239 个 fuzz 入口点完成**汇编级（RISC-V）安全证明**：程序对所有 <64MB 输入、任意被建模的 Linux OS 响应与内存布局，恒以正常退出收尾（无内存安全错误/断言失败）。
- 证明总量约 **1.8 亿行 Rocq**；典型单证明 ~60 万行，覆盖中位数 18,000 条 RISC-V 指令的二进制。
- 证明过程中发现 fuzzer 多年（万亿次运行）漏掉的 bug：~20MB 特定布局才触发的计数器下溢→OOB write、需 64MB 输入+2GB 内存的 OOB read、跨两个文件句柄的调用序列 bug、深嵌套输入（重新发现 CVE-2026-56132）、以及**从不 crash 的逻辑 bug**（文件加载白名单未被强制执行）。
- 前置经济学对照：seL4 实现 2 人年、验证 20 人年——LLM 把证明成本压到"周"级别，且证明本体无需人工审查。

## 核心方法论：测试→规格→证明

1. **测试即规格（test-to-spec）**：不给文本编辑器这类无清晰 spec 的程序强写规格，而是把**现成可编译测试套件**编码为规格——"该测试套件恒通过"。fuzz 入口点天然如此：任何使程序 crash 的输入即作者关心的 bug。规格=对编译后 RISC-V 指令的量词陈述："任意输入(<64MB)下不 crash"。证明成立则 fuzz 永远找不到 bug——测试变多余。
2. **在汇编层证明**：库+fuzz 测试编译为 RISC-V 可执行文件，用 Theorem 的 RISC-V 指令+Linux 进程形式语义转成数学模型。绕过编译器正确性假设之外的层次；修 bug 后重编译自动再生成规格，证明随代码同步。
3. **修复-重证循环**：证明失败的反例→定位 bug→Claude 直接 patch 代码→规格按 patched 代码重生成→继续证明。全程无需人类介入每个 bug。
4. **TCB（信任基）极小化**：1.8 亿行证明**不需要人工 review**——Rocq 内核机器检查。只需信任：(a) RISC-V+Linux 形式语义模型；(b) 精确的定理陈述本身；(c) Rocq 检查器。三者大小恒定，而被保护项目数任意扩展，信任成本不随规模增长。

## 超越内存安全的性质编码

- crash 断言可编码**高层性质**：encode-decode 往返、幂等、代数律、差分测试、自一致性、与参考实现等价——证"不 crash"即证性质本身（LZO 压缩往返为例）。
- **衍生证明义务不可预判**：为完成 cpp-httplib 的证明，Claude 必须在**机器码层**证明 libc++ 红黑树重平衡算法的深度对数上界（排除 std::set 析构递归导致的栈溢出）——证明义务由定理陈述机械导出，不是人列出来的。

## 其他案例（同套思路的不同用法）
- **RFC 即规格**：Claude 写 RFC 1950（zlib 格式）形式 spec → 证 Linux 内核 zlib 实现正确（x86 语义由 Claude 生成+重度测试）。结论：成熟代码库已近乎全对，且端到端正确性可证。
- **解释器+语义对齐**：Rust 写大子集 Python 解释器，用 Verus 证其符合学术论文给出的 CPython 语义；再跑 170 万随机程序经验对照（99.95% 一致，差异均为已知角落）。
- **PDF reader**：验证尝试一周发现的安全 bug ≈ 平时一年上报量；潜伏 >10 年的逻辑 bug。

## 经济学与趋势
- 36 个真实小任务上 Opus 5.5 比 Opus 5 少 ~40% token 证掉一半；训练数据含长验证任务是持续趋势。
- 摊销路径：更多代码被形式化+方法标准化后，证明可跨代码库复用/改写。
- 成本现状：单证明可达数亿 token——成本敏感场景先做小任务基准。

## 坑与限制
- 假设边界必须显式：单线程静态二进制、固定内存预算、RISC-V+Linux；结论只覆盖规格范围，**剩余 bug 只可能在 TCB 内或范围外**。
- LLM 输出依赖 grader/classifier 标注时的偏差；可发布证明接受独立验证（他们公开了 TCB+完整证明+未证规格）。
- 语义模型本身（RISC-V/x86/Linux）是新的关键工件：Claude 生成的 x86 语义需"重度测试"背书。

## Activation
formal verification at scale, fuzz test to formal spec, RISC-V assembly proof, Rocq/Coq LLM proofs, OSS-Fuzz, TCB minimization, proof-driven bug discovery, memory safety guarantees, binary-level verification, test-to-spec conversion
