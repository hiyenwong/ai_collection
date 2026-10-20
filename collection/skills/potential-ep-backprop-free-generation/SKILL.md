---
name: potential-ep-backprop-free-generation
description: Backprop-free CIFAR-scale generative modeling via PotentialPCN relaxation. Use when training or sampling needs no backward pass.
category: ai_collection
---

# PotentialEP: Backprop-Free CIFAR-Scale Generative Models via Equilibrium Propagation

**source**: arXiv:2610.14409 (Alex Gower, University of Cambridge & Nokia Bell Labs, v1 10 Oct 2026, under review at ICLR 2027)
**papers**: Alex Gower, "PotentialEP: Backprop-Free Training of CIFAR-Scale Generative Models via Equilibrium Propagation", 2026
**task**: generative modeling on analog/neuromorphic substrates without backward passes in either training or sampling
**field**: equilibrium propagation, predictive coding, flow matching, neuromorphic computing

## Activation

- 使用/研究 Equilibrium Propagation (EP) 超越 MNIST 规模（首次 CIFAR-10 FID 3.64）
- Energy Matching / 能量景观生成模型想在模拟交叉柱（analog crossbar）硬件上采样
- 预测编码网络（PCN）推导"网络即反向传播"的等价结构
- 想把"整一个 velocity field 的 backward pass"替换为物理弛豫（relaxation）
- 关键词: equilibrium propagation, energy matching, predictive coding network, backprop-free training, analog crossbar, flow matching potential

## Summary

**Problem**: 扩散/流匹配生成需数百次串行评估一个 velocity field，每次评估 −∇x Vθ 都是一次完整的 backward pass —— GPU 不适合，模拟神经形态硬件合适，但 backprop 的全局梯度传输在 analog 上难以实现。

**Method — 三个对应（correspondences）**:

1. **PotentialPCN（推理等价）**: 取与 Energy Matching 相同的层 fk，构建标准 PCN 能量（每节点一个 prediction error），并在标量输出节点加一个线性注入项：
   ```
   E_PCN(x,h) = Σ_k ½||f_k(h_{k-1}) − h_k||² + γα·h_N,  h_0 = x, h_N = o ∈ R
   ```
   命题 1（γ→0 极限）:
   - 输出节点平稳性给出 e*_N = γα（正是 autograd 反传时播下的种子）
   - 内部节点递归 e*_k = J_{k+1}^T e*_{k+1}（误差沿转置 Jacobian 下行，恰是 backprop）
   - 因此 ∇x E_PCN(x,h*(x)) = γα J_1^T J_2^T ⋯ J_N^T = γ·∇x Vθ(x) + O(γ²)
   - 可见层读出 v_PCN(x) = −γ⁻¹ ∇x E_PCN(x,h*) = −∇x Vθ + O(γ)
   - 关键洞察: **PCN 的误差单元就是反向传播**；弛豫过程本身已经完成了整个 backward pass，可见层只需读自己的局部误差 e_1
   - 该推导不依赖权重值 → 反传训练好的模型可原样载入，纯弛豫采样（无需重训练！）
   - 物理实现: 隐节点时间尺度快于 x 时 h* 绝热跟踪（adiabatic tracking），一次连续弛豫即整条生成轨迹

2. **弹簧夹持自由相（training via GradEP）**: 要用 EP 训练一个"损失依赖能量梯度"的模型，需 GradEP 变体——不固定 x 于 x_t，而是用弹簧能量 λ/2‖x−x_t‖² 系住 x：
   ```
   E_free(x,h) = E_PCN(x,h) + (λ/2)‖x − x_t‖²
   ```
   平稳性给出 ∇x E_PCN = −λ(x−x_t)，于是待训练速度编码于弹簧平衡伸长量：
   ```
   v* = −γ⁻¹∇x E_PCN(x*,h*) = λγ(x* − x_t)
   ```
   参数梯度等价于移动 x 的平衡位置，恰好是 EP 能处理的量；∇θ L_PCN = ∇θ L + O(γ)。

3. **线性化 nudge（关键工程改进）**: 标准 EP 的二次 cost C(x)=½‖v(x)−u‖² 的 ±β nudge 对平衡点不对称（位移 −βγg/λ(λ+β) 非线性），带来 O((β/λ)²) 偏差。改为冻结 g 后取线性化 Clin(x)=g^T v(x)（Dual Propagation 式），nudge 是常力，位移 x*β−x* = −βγg/λ² 严格线性于 β，±β 平衡点对称，误差只剩 ∂θE 沿路径的非线性，约束变为 `β·γ·|g| ≪ λ²`。实践效果：线性 nudge 在 β=3→10³ 三 decade 内保持 cos ≥ 0.99，二次 nudge 仅在 β=1 一点可用。

**Key results** (CIFAR-10 / ImageNet-32):
- 推理速度等价: cos(vFFN, vPCN) = 1 到小数点后九位（γ=10⁻⁴, rel. dev. 1.3×10⁻⁵，低于 TF32 算术地板）；FID 差 ≤0.04（CIFAR-10: 3.54→3.55; ImageNet-32: 6.75→6.78）
- 训练更新等价: cos(∆θEP, ∆θBP) = 0.9998 @ γ=10⁻⁴, β=30
- **首个 EP 训练的 CIFAR-10 生成模型**: FID 3.64（vs 反传 3.54）—— 同 50M 参数量下与近期扩散/流匹配基线（OT-CFM 4.04, DDPM++ 3.45, EM 3.34）同一水平带
- **γ–β 联合窗口**: 可用区是一条对角带，γ 每降一个 decade 需 β 升约一个 decade 补偿（位移 ∝ γβ）；下边缘 TF32 淹没位移、float64 完全挽救，上边缘 nudge 过远线性差分失效（float64 救不了）
- **硬件可行架构存在性证明**: 去掉 group norm + attention（两者都不是 analog crossbar 原生操作），换成 weight standardisation + 残差 1/√depth 缩放 + 平坦线性头，只剩定点加权和与逐点非线性（Ohm/Kirchhoff 定律原生），FID 3.51 ≈ 3.54 无可测差异
- 采样噪声调度: τ≤1 为无噪 ODE（noise→data），τ>1 为固定温度 Langevin（时间无关势场使继续积分是进一步弛豫而非外推）；τs 每模型在梯子上选

**Why it matters**: 把"生成=弛豫、训练=平衡测量"从 MNIST 推到 CIFAR 竞争力水平；反传训练的现成模型可直接以零质量损失切换到弛豫采样——部署侧（模型生命周期的绝大部分能耗）可先行迁移到 analog 硬件，无需改变训练方式。

## Pattern: 把 backprop 藏进网络动力学

推导的核心技巧可复用：任何"需要 ∇x V 的算法"（流匹配、得分匹配、能量引导）都能通过在标量输出节点注入线性项 γαh_N，让弛豫网络在平衡态以 O(γ) 误差自算梯度。步骤：
1. 确认目标量是某个网络输出的梯度（该网络可以是任意层组合）
2. 按预测编码式样构造每节点误差能量
3. 注入项设定 e*_N = γα（相当于手动播种 "∂V/∂V = 1"）
4. 从第一个节点读出 −γ⁻¹ J_1^T e*_1 即得梯度
5. 训练侧用 GradEP 弹簧夹持把"梯度作为损失"转化为"位置作为损失"

## Pitfalls / 失败模式

- **γ 与精度**: γ 越小对应越好，但位移 O(γβ) 需在有限精度下可分辨——TF32 下 γ=10⁻⁴ 已到算术地板，盲目减小 γ 无益
- **β 过大**: nudge 平衡点位移过远，线性差分失效且 float64 不可挽救（区别于下边缘的精度问题）
- **依赖弛豫收敛**: 对应关系假设 h 处于当前 x 的平衡态；模拟中需交替"x 步进 → h 弛豫 K_h 次扫描"（误差参数化下 dt=1 时单次扫描收敛）
- **跳连图**: UNet skip 连接把链式递归 e*_k = J^T e* 改为对子节点求和（App. D），实现时不能照抄链式公式
- **phase-2 负样本**: 作者的 compute 预算不够弛豫生成负样本，用同权重 FFN twin 代替（无参数梯度穿过 twin）——复现时注意这一妥协
- **单 run 无方差**: 每个 arm 都是单次训练，0.1 级 FID 差异不构成排序证据

## Related skills

- `predictive-coding-equilibrium-propagation-imagenet` — EP 前身工作（分类任务）
- `qml-equilibrium-propagation-medical` — EP 在 QML 中的应用
- `ep-lif-snn-e2e-spiking` / `equilibrium-propagation-lif-snn` — EP 与 SNN 结合
- `energy-based-autoregressive-neural-dynamics` — 能量模型生成
