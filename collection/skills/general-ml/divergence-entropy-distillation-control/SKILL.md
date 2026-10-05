---
name: divergence-entropy-distillation-control
description: "设计/调参蒸馏目标（KL方向选择、reverse vs forward KL、自蒸馏超参）时用。前向KL膨胀学生熵、反向KL压缩熵；散度=隐式熵正则器，自蒸馏中最佳超参是补偿特权信息熵压缩的散度。Activation: knowledge distillation, forward KL, reverse KL, student entropy, cross-entropy, on-policy distillation, self-distillation, entropy regularization, distillation objective design"
metadata:
  arxiv_id: "2610.03529"
  published: "2026-10-02"
  authors: "Nicolas Zucchet, Scott W. Linderman"
  source: "arXiv cs.LG/cs.CL"
  tags: [distillation, divergence, entropy, llm-training]
---

# Divergence Controls Entropy in Distillation

## 核心结论

蒸馏目标中的散度选择是**隐式熵正则器**，直接控制学生分布熵：

1. **前向 KL（mode-covering）**：膨胀学生熵至教师之上。cross-entropy 训练是其特例——给出恒等式并在 LLM 预训练与 SFT 中定量验证
2. **反向 KL（mode-seeking）**：压缩熵，直到师生差距过大时失效
3. **插值散度**：训练早期熵变化平滑，收敛处突变
4. **On-policy 蒸馏的低熵来自 token 级反向 KL，而非 on-policy 采样本身**

## 实践指导

- 想要更确定/低熵学生（如推理模型）：token 级反向 KL
- 想要更高熵/更多样学生：前向 KL 或校准过的散度插值
- **自蒸馏场景**：条件化特权信息会压缩熵 → 最优散度超参是那些能补偿该压缩的选择。先诊断熵失衡，再选散度

## 验证

熵恒等式在 LLM 预训练与监督微调中定量成立。
