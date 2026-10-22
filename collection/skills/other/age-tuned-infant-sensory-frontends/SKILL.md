---
name: age-tuned-infant-sensory-frontends
description: Age-indexed sensory frontends simulate infant perception by month.
category: neuroscience
arxiv_id: "2610.25377"
tags: [developmental-neuroscience, sensory-development, infant-vision, infant-hearing, world-models, critical-period, perceptual-narrowing, curriculum]
---

# Age-Tuned Infant Sensory Frontends（年龄调谐婴儿感官前端）

> arXiv:2610.25377 — "Simulating Infant Senses with Age-Tuned Networks" (Somesh Mohapatra, 2026-10-18, cs.LG/cs.HC/q-bio.NC)
> 代码/网站: github.com/pikulsomesh/developmental-world-models · Baby Senses Lab (浏览器端, 无上传)

## 核心思想

把每个感官的**不成熟度写成固定、按月龄索引的输入滤镜** Φs(·; a)，再在滤镜后面放一个小型预测网络学习。这一分离把婴儿研究中纠缠的三个问题拆开：
1. **什么信息到达感官**（滤镜决定，构造性复现感官成熟顺序：触觉→听觉→视觉）
2. **从输入中学到了什么**（网络决定，揭示"输入允许"vs"实际提取"的差距）
3. **经验的顺序/时序如何改变所学**（连续训练的历史效应：关键期、知觉窄化、感官竞争）

**关键设计原则**：滤镜可审计（任何人都能看到/听到某月龄网络收到的输入），网络提供滤镜给不了的东西（提取与经验塑造）。

## 前端方程（全部本会话数值验证过）

### 视觉（Eq 1–3）
- **模糊**：高斯 σ(a) = √(ln10/2)/(π·c(a)) 度，c(a)=该月龄视敏度(cycles/degree)。MTF exp(−2π²σ²f²) 在 f=c(a) 处=0.10（机器精度验证）。成人参考 30 cyc/deg。
- **对比度**：x ← x̄ + κ(a)(x − x̄)，κ(a) = clip(½log₁₀ CS(a), 0.15, 1)，CS=对比敏感度（阈值而非增益，故取对数）。
- **色彩**：õ = clip[0,1](ℓ + γ(a)(x − ℓ))，ℓ = 0.299R+0.587G+0.114B 亮度，γ=饱和度比例。
- **像素换算**：px/deg = w/(2·arctan(W/2D)·180/π)；**最小可分辨细节 = D·tan(1/(2c(a)))，角度单位是度**（2月龄@30cm→1.31mm；@2.5m→10.9mm，验证命中论文引用值）。
- **视敏度双表歧义**（真实数据分歧，非建模选择）：行为学(优先注视) vs 视觉诱发电位(VEP)在 6 月龄差 3 倍（4.8 vs 15 cyc/deg）。模型用陡的 VEP 表；网站双表可切换。行为表：出生 0.8 → 12月 7.5 → 24月 10.5 cyc/deg。

### 听觉（MS 变换）
- 中/边处理：L_out = (1+ρ)/2·L + (1−ρ)/2·R（**双耳差精确缩放 ρ**：(L_out−R_out)=ρ(L−R)，恒等式验证）；ρ=0→单声道。
- 3kHz high-shelf 滤波 −g(a) dB + 总衰减 A(a) dB + 软噪声地板。
- **阈值锚点验证**：婴儿−成人纯音阈值差拟合 36.1·e^(−a/2.10)+12.6 dB：1月→35.0 dB(4kHz, 论文引用~35 ✓)、3月→21.3(mean(23,19) ✓)、6月→14.7(10–15 ✓)。诚实声明：锚点在 1 月(差12dB)与 12 月后(差7dB)偏温和；不支持大幅高频切除。

### 触觉/体感：轻度感受野模糊+噪声（出生即最成熟）。

## 三层结果分解（论文最重要的方法论纪律）

| 层 | 结果 | 证据性质 |
|---|---|---|
| 滤镜层 | 感官成熟顺序(触→听→视)按构造复现 | **非网络发展像婴儿的证据** |
| 学习层 | 视觉"学到的"远小于"输入允许的"：新生儿阶段玩具位置 R²=0.00±0.01 vs ceiling 0.57；3月 0.29 vs 0.93；12月才闭合(0.85 vs 0.95)。听觉全程贴近 ceiling(0.45 vs 0.48) | 早期视觉是**双重限制**：既被眼睛限制，也被"通用预测目标在模糊微弱画面中提取小玩具之慢"限制 |
| 历史层 | 关键期、知觉窄化、感官竞争在一个连续训练运行中涌现，无任何年龄开关 | 计算上最有趣 |

**信息 ceiling 陷阱**：用"输入信息达 12 月值一半的月龄"排序会得到 τ=0.00（触/视都在 0 月过半，听觉 4 月）——不恢复婴儿顺序，因为新生儿模糊视觉仍含粗定位信息（本会话迷你实验：大玩具位置 ridge ceiling R²≈0.996，与论文"ceiling 0.94@3月"一致）。**"成熟"必须声明由哪个任务定义**。

## 涌现签名（无内置机制）

- **关键期**：开头 3 月重度模糊窗→后期细节精度 0.81±0.04 持久损失；放 3–6/6–9/9–12 月则恢复(1.00/0.94/0.96)；剥夺越长损失越大(6月→0.61, 9月→0.40)。
- **知觉窄化**：只见过 4 身份中 2 个→未见对 surprise 先升后降(0.54→0.29)，熟悉对持续升(1.18)；听觉 d′ 降(5.19→1.33)但 surprise 不变——**"窄化"是否存在取决于测量方式**(注视时间 vs 习惯化)。
- **感官容量不同**：达 12 月水平最小核心参数：听觉 ~6k，触觉 ~24k，视觉 97k 仍在升。**加大容量救不了新生儿视觉**(1.7k:−2.67 vs 97k:−2.09)——感官之"年幼"由输入造成，非网络大小。
- **先来者挤占后来者**：听觉先上线(如婴儿)→视觉编码器只达 0.60 vs 单独训练 0.84。**每感官先独立训练再融合=最佳编码器(0.84/0.84)**。
- **Latent prediction 崩塌**：BYOL 式目标编码器(EMA 0.99)数步内塌缩(逐维 s.d. 0.006)；加 VC 正则(25,25,1)保住 15 有效维但几乎不携带玩具信息(0.02 vs pixel 0.85)。**像素重建损失上权重"会动的东西"→推向玩具**；latent 目标无此推力。限定小场景结论，非否定 latent 世界模型。

## 可复用模式

1. **发展性课程数据增强**：blurry-first 序列提升视觉追踪(0.51 vs 0.33)但对听/触无效——课程收益是感官特异的。
2. **婴儿视角数据集构造**：任意成人级图像/音频×月龄滤镜=可控的"婴儿看到的输入"分布（教学/发展机器人/研究）。
3. **测量方法分歧显式建模**：当两类测量(行为 vs 诱发电位)分歧 3 倍时，双表并陈让用户切换，而非隐藏分歧。
4. **诚实边界**：网站每页声明"非诊断工具"；感知≠认知（网络对玩具消失不惊讶——感觉预测不自动产生物体期望）。

## 本会话验证记录（16/16 PASS）

σ-MTF@cutoff=0.1 (1e-12)；细节 1.309/10.91mm；Snellen 20/600↔1 cyc/deg；听觉拟合 35.0/21.3/14.7dB；MS ρ 恒等式 (1e-12)；κ clip 界；V7 大玩具 ceiling：新生儿(c=1,CS=2) R²=0.996 ≈ 成人——定性复现"粗任务下模糊输入仍可定位"。
（FOV 假设 0.5°/px 已声明；论文世界含遮挡屏与运动手故其 ceiling 数值更低。）

## Activation

infant sensory development, developmental world model, age-tuned frontend, visual acuity simulation, perceptual narrowing simulation, critical period emergence, sensory heterochrony, curriculum from development, infant-like data augmentation, Baby Senses Lab

## 相关技能

- `infant-sensorimotor-motion-retargeting`（婴儿感觉运动仿真）
- `multimodal-infant-embodied-rolling-behavior`（多模态婴儿具身行为）
- `spiking-brain-2-foundation-models` / 发展性课程相关
