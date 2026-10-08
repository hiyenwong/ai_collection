---
name: hanc-hybrid-action-control
description: Hybrid-action neural controller: ST-Gumbel differentiable discrete+continuous control. (arXiv:2610.01822)
category: ai_collection
---

# HANC: Hybrid-Action Neural Feedback Control

**Paper**: "Differentiable Hybrid-Action Neural Feedback Control for District Heating Networks" — Kirsch, Sgadari, La Bella, Ferrari-Trecate (EPFL NCCR Automation), arXiv:2610.01822, eess.SY, 1 Oct 2026, IEEE TCST submission. Deployed on real DHN benchmark (RSE SpA, Italy).

## 核心问题

信息物理系统（CPS）控制常需同时输出**连续 setpoint**（温度、流量）与**离散操作决策**（设备开关、模式选择、资源调度）。三个既有路线各有缺陷：

- **MPC/MINLP**：每步在线求解混合整数非线性规划，计算昂贵且依赖商业求解器
- **RL**：免模型交互量大，且不内生保证执行器约束
- **可微控制（DPC/SHAC）**：argmax 不可微，梯度链断裂；既有混合扩展只在短 horizon 训练或线性动力学

## 架构：三组件按构造满足约束

```
                context z_t (价格, 需求) + output y_{t-1:0}
                          │
        ┌─────────────────┴──────────────────┐
        │                                    │
   连续分支 NN_c (GRU)                  离散分支 NN_d (GRU)
   v_t → sigmoid 缩放                    logits l_t^j
   ũ_c = σ(v)(u_max−u_min)+u_min          ST-Gumbel 选择层
   (box 约束按构造)                       → one-hot s̃_t^j → δ̃^j
        │                                    │
        └───────────── 装配层 A ─────────────┘
                 u_t = A(ũ_c, δ̃)  （编码耦合约束）
```

### 装配层 A 的三种模式（本文精华）

1. **纯连续/纯分类**：A = 恒等映射，分支输出直接馈入。
2. **区间并集**（finite union of intervals，含 idle 单点）：
   `u_t = Σ_i s̃_{i,t} · ũ^i_{c,t}` — 离散分支选模式（one-hot），连续分支为每模式生成一个物理缩放的 setpoint。前向恰好执行一个模式，梯度经松弛权重 ŝ 分布到所有候选 setpoint（未执行的模式也获得学习信号）。
   - 实例：TES 流量 `q ∈ [−0.5,−0.25]∪{0}∪[0.25,0.5]` → 三分类（放/持/充）× 两 setpoint。
3. **逻辑依赖（AND 门）**：`u = δ̃^j · δ̃^{j'} · ũ_c` — 如 EB 功率仅在质量流量开启时可投放：`P^ref = δ^q · δ^P · u^P`，任何输出组合都无法向关闭的水力回路投放功率。

**约束全部由架构保证**（训练 rollout 与部署同构），Problem 1 退化为对 θ 的无约束优化。

## 训练：BPTT over full closed-loop rollouts

### ST-Gumbel 估计器（前向硬 / 反向软）

- **前向**：`s = onehot(argmax_i(l_i + g_i))`，g_i = −log(−log u_i) i.i.d. Gumbel 噪声 → 硬 one-hot，闭环以真实离散动作仿真（与部署一致）
- **反向**：梯度经 `ŝ_i = softmax((l_i+g_i)/τ)` 松弛采样回传
- **退火**：`τ_k = max(τ_0 ρ^k, τ_min)`，τ0=2, ρ=0.99, τmin=0.1 — 早期梯度平滑，后期逼近离散分布

### 长horizon稳定三件套（不截断 rollout）

1. 全局梯度范数裁剪 `‖∇θL‖₂ ≤ ḡ=100`
2. Gumbel 温度退火平滑早期优化地形
3. 门控架构（GRU）缓解消失/爆炸梯度

### 损失函数设计（全部无量纲 O(1)，权重即优先级）

| 项 | 形式 | 说明 |
|----|------|------|
| ℓ_cost | regret 式归一化：`T⁻¹Σ(c_t−J_⊥)/(J_⊤−J_⊥)`，包络锚定在**外生需求** D_t 而非总发电 | 时移套利可见（充储可在廉价时充电→ℓ_cost<0）；对关税共同缩放不变 |
| ℓ_hk | `softplus(h_k(y))²/h̄_k²` 单侧逐点罚 | 反exploit：惩罚代理模型可产生但物理上不存在的轨迹（欠供热、储罐分层倒置、GB 负流量）；h̄ 是量纲尺度非超参 |
| ℓ_phys | 轨迹级能量平衡 `ψ²/ψ̄²`，`ψ=E_gen−(1+κ)E_load−ΔE_TES` | 防止代理能量凭空产生 |
| ℓ_op | 供热温度 ≥65°C 单侧罚 | 运行约束 |
| ℓ_sw | **二阶差分** `\|ŝ_{t+1}−2ŝ_t+ŝ_{t−1}\|²` 作用于**松弛权重** ŝ 而非执行 one-hot | 惩罚振荡（chatter）但几乎不罚孤立持续的模式切换；一阶差分会抑制离散执行器使用 |

### 关税课程学习

价格对比小时梯度无信息 → 训练停滞。**课程**：从夸大价格对比 ζ⁰=[7,13] C/kWh 起步（warmup 400 epochs）→ 线性插值到目标 ζ_tgt=[0.4,1.0]（300 epochs）→ 专门化阶段（500 epochs）只在目标分布上选最佳模型。

### 代理模型（physics-informed surrogate）

拓扑引导分解：4 负载+8 管道 = 独立 GRU 子模型（3 latent states）；TES 用 4 层分层热模型解析建模；EB 出口温度由质量/能量守恒解析；节点混合按拓扑解析施加。仅 820 参数，FIT 87.94%。训练数据由 Modelica 参考系统伪随机多级信号激励生成（5min 采样，20 天）。

## 部署形态

**因果反馈策略**：只用当前测量 + GRU 内部记忆，零预测/forecast 层。单次前向传播，实时开销极小。Gumbel 噪声部署时关闭 → 确定性 argmax。

**跨模型迁移**：在代理上训练，在独立高保真 Modelica 仿真器上评估（真实意大利 GME 日前市场电价）→ 成本降低 30%（400 个配对 rollout 全部更便宜，区间 28.4%–31.7%），证明对 plant-model mismatch 的鲁棒性。

## 核心发现：Gumbel 噪声 = 隐式决策裕度最大化

**首次在可微离散控制中报告决策裕度分析**：

| 估计器 | 成本 | EB 功率门开关数/2天（中位） | 决策裕度 |
|--------|------|------------------------|---------|
| Deterministic ST | 148.7 C（同） | **51.5**（最差 102，最好 24） | 48% 质量在 \|l\|<1；中位 1.085 |
| Gumbel ST | 146.2 C（同） | **4**（=价格结构要求的最小值） | 双峰分布远离边界；门开 3.95，门关 12.2 |

机制：Gumbel 前向扰动 logits——靠近决策边界的策略会经历随机动作翻转 → 传播到 rollout 增加成本+切换罚 → **优化压力主动分离竞争 logits 直到扰动不再影响选择**。确定性 ST 的硬前向对 l=0.1 和 l=10 完全相同，优化对边界距离不敏感。

确定性 ST 即使把切换罚提高两个数量级仍有抖动 → 抖动是该估计器的病态，而非正则化不足。

**结论**：学习离散决策变量的控制器时，Gumbel 训练通过隐式鼓励更大决策裕度提供更强鲁棒性，降低学习动作对扰动的敏感性。

## 可复用设计模式

1. **约束by construction**：输入约束编进架构（sigmoid 缩放/装配层），优化退化为无约束——优于动作裁剪/罚函数的后处理。
2. **装配层梯度广播**：one-hot 前向+松弛反向让所有模式获得学习信号，即使未被执行。
3. **噪声即正则**：训练时注入的采样噪声 = 对部署鲁棒性的隐式投资（裕度）；比后验正则化更根本。
4. **二阶差分切换罚**：罚振荡不罚切换——比一阶差分/开关计数更符合执行器磨损物理。
5. **Regret 式成本归一化**：锚定外生需求的包络，保留套利可见性且对价格缩放不变。
6. **反exploit物理罚**：闭式训练可微代理时，优化器会主动寻找代理误差区域——显式惩罚物理不可实现轨迹。
7. **课程价格对比**：弱梯度信号场景（价差小）先夸大对比再退火到真实分布。
8. **零预测部署**：reactive policy + 内部记忆可编码长horizon策略（充电到满只在后续高价时段合理），且不受训练 horizon 限制。

## Activation 触发场景

混合整数控制、设备开关+setpoint 联合决策、区域供热/冷网络、储能套利调度、微电网、生产排程、任何 categorical+continuous 动作空间的可微控制/可微规划问题、MINLP 的神经替代、执行器磨损最小化。
