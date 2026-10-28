---
name: sre-phase-averaged-magic-invariant
description: "Magic quantification without a phase reference frame."
category: ai_collection
version: 1.0.0
source: https://arxiv.org/abs/2610.18955
source_title: "Stabilizer Rényi Entropy Without a Phase Reference"
authors: "Jinwei Chu, Savan Kharel"
published: 2026-10-13
tags: [quantum-information, magic-states, stabilizer-renyi-entropy, gauge-invariance, gluon-scattering]
---

# Stabilizer Rényi Entropy Without a Phase Reference (arXiv:2610.18955)

## 触发场景 (Use When)

- 需要量化量子态的 magic（nonstabilizerness），但计算基底固定而横向 Pauli 轴未指定（无共享相位参考系）
- 典型物理场景：无质量粒子的 helicity 态、未同步的 qubit 寄存器、能量本征态、超选择定则约束系统
- 胶子/引力子散射中提取 helicity 基 magic、对撞机量子信息探测
- 裸 SRE（stabilizer Rényi entropy）随基矢重相位 |+⟩→e^{iθ}|+⟩ 连续漂移（Bell 态例中 M₂ 从 0 扫到 ln(4/3)），需要规范不变量版本

## 核心方法

### 1. 相平均 SRE 定义（对数前平均）
标准二阶 SRE：M₂ = −ln(2^{-k} Σ_P ⟨ψ|P|ψ⟩⁴)，对 4^k 个 Pauli 串求和。
相平均不变量：在**取对数之前**，先对 k 个未解析相位 θᵢ 做 U(1)^k Haar 环积分：

M̃₂(|ψ⟩) = −ln ⟨ Π({θᵢ}) ⟩_{θᵢ}，其中 Π = 2^{-k} Σ_P ⟨ψ{θᵢ}|P|ψ{θᵢ}⟩⁴

顺序关键：先平均 Pauli 矩再取对数（Jensen 不等式保证 M̃₂ ≤ 平均裸 SRE，下界跟踪典型帧的 magic）。

### 2. 四大性质
- **Invariance（不变性）**: Haar 测度平移不变 → 对所有 U(1)^k 重相位精确不变
- **Vanishing criterion**: M̃₂ = 0 ⟺ 态在**每个**相位约定下都是 stabilizer 态（Π({θ})≤1 且连续性论证）
- **闭式（稀疏支撑）**: 当 |ψ⟩=Σcᵢ|sᵢ⟩ 的支撑集满足两两不同 flip-pattern 条件（对每对 cᵢ,cⱼ≠0，比特 XOR 模式 sᵢ⊕sⱼ 互异）时，相位完全积出，得**纯布居函数**（注意第一个求和项带平方）：
  M̃₂ = −ln( 6·(Σᵢ|cᵢ|⁴)² − 5·Σᵢ|cᵢ|⁸ )
  数值验证：Bell 态 (1/2,1/2) 给 6·(1/2)²−5·(1/8)=7/8 → M̃₂=ln(8/7)，与蒙特卡洛相位平均（20k 样本，按定义直接计算）完全吻合；等概率 1/n 给 6/n²−5/n³=(6n−5)/n³ → ln(n³/(6n−5)) ✓
  布居可单基测量 → 对已知支撑的纯态无需相位信息即可测 magic
- **重要陷阱**: 裸 SRE 的相位依赖来自全部 16 个 Pauli 串（2-qubit 例中 X⊗Y、Y⊗X 也非零，幅值 −sinΔ）；只数 XX/YY/ZZ/II 会得出错误闭式 (1+cos⁴Δ)/2，正确结果为 7/8+cos(4Δ)/8，验证时必须全枚举
- **Typical vs best-case**: M̃₂ 捕获典型相位帧的 magic；与最小化/非局域 magic（优化整个局域幺正群，best-case）互补，与量子参考系资源理论（Bartlett-Rudolph-Spekkens）平行

### 3. 通道天花板（Channel Ceilings）
最大化 M̃₂ 等价于最小化 F(p) = 6(Σpᵢ²)² − 5Σpᵢ⁴（pᵢ=|cᵢ|², Σpᵢ=1；注意首项是 (Σpᵢ²)²）：
- n≥3 通道：等概率 pᵢ=1/n 取全局最大 ln(n³/(6n−5))，序列 ln(64/19), ln(27/13), ln(8/7)…
- n=2 例外：等概率点只是局部极小，全局最大 ln(7/5) 在 p=(1±√(3/7))/2

### 4. 胶子散射应用（树阶 MHV/anti-MHV）
- m→k 散射 S 矩阵制备 k-qubit helicity 态 |ψ⟩=Σ_h A(h)|h⟩；helicity 相位未定 → 用 M̃₂
- **2→2（四点）**: 裸 SRE 在 Bell 点 θ=π/2 消失，M̃₂ 提升为 ln(8/7)；θ≈1.38 处布居过 p=(1±√(3/7))/2，饱和二通道天花板 ln(7/5) —— 四点胶子散射达到二通道允许的最大不变 magic
- **3→2（五点 anti-MHV）**: 三概率重合时达三通道天花板 ln(27/13)≈0.731（裸 SRE 相位扫描最大 ln(9/4)，距二 qubit 最大值 ln(16/7) 差 2%）
- **2→3（同 helicity）**: Dalitz 平面上 ln(8/7)≤M̃₂≤ln(184/125)；软极限（x₃→0）出现反直觉**软 floor**——软胶子单独携带全部不变 magic（态因子化为软胶子等权 helicity 叠加 × |−−⟩）；共线边界 x₅=1、x*≈0.3976（六次多项式根）处逼近共线 ceiling
- **Color independence**: 所有固定颜色依赖精确相消（MHV 与 anti-MHV 共轭 color-kinematic 和在取绝对值后相同）→ 归一化后 magic 完全由运动学决定，色盲。裸 SRE 保留色依赖相位，只有相位不变版本是色盲的

## 可复用模式

1. **规范平均构造**: 任何依赖未定参考帧的量，考虑先做轨道平均再取非线性泛函。适用：超选择扇区、缺乏共享时钟/相位源的分布式量子设备
2. **Flip-pattern 稀疏性判据**: 支撑集两两 XOR 互异 → 相位可积出 → 测量量仅依赖布居。可迁移到任何"系数相位未知但模方可测"的干涉计量任务
3. **天花板-运动学分离**: 通道天花板（纯数学）vs 物理过程实际可达值（运动学约束）。散射振幅结构决定过程能否触顶；Dalitz 约束可把同 helicity 过程压到天花板的 1/3 以下
4. **软辐射不消除资源**: soft limit 下 magic 由最软粒子携带——与 naive 预期相反。类似红外因子化模式，可迁移到其他软定理/资源理论交叉

## 与相关 skill 的关系
- [[magic-entropy-cft]]: CFT 普适 Affleck-Ludwig 项（多体普适性质）；本 skill 是单态规范不变定义（测量层）
- [[nonstabilizerness-diffusive-dynamics]]: magic 的多体扩散动力学；本 skill 解决其前置于测量的参考系歧义
- 互补: nonlocal magic（全域幺正优化，best-case）vs 本 skill（U(1)^k 轨道平均，typical-case）

## 关键公式速查
- 裸 M₂ (Bell 态, 相位依赖): ln[16/(14+2cos4(θ₁−θ₂))]
- 相平均稀疏闭式: M̃₂ = −ln( 6(Σ|cᵢ|⁴)² − 5Σ|cᵢ|⁸ )；验证锚点: Bell → ln(8/7), 等概率 n 通道 → ln(n³/(6n−5))
- 通道天花板: n≥3: ln(n³/(6n−5)); n=2: ln(7/5) at p=(1±√(3/7))/2
- 散射: 4pt Bell 点 ln(8/7), 顶点 ln(7/5); 5pt 3→2 顶点 ln(27/13)≈0.731; 2→3 floor ln(8/7) ceiling ln(184/125)≈0.387

## 验证（全部数值复算通过）
- MC 相位平均（20k U(1)² 样本，全 16 Pauli 串枚举）: Bell 态 M̃₂ = 0.1339 ≈ ln(8/7) ✓
- 闭式锚点: n=2 最优 p=(1±√(3/7))/2 → ln(7/5)=0.3365 ✓; 等概率 n=3,4,5 → ln(27/13)=0.7309, ln(64/19)=1.2144, ln(125/25)=ln(5)=1.6094 ✓
- Bell: M₂(θ) = ln[16/(14+2cos4Δθ)] 扫描 [0, ln(4/3)]，M̃₂ 恒为 ln(8/7) ✓
- Jensen: M̃₂ ≤ ⟨M₂⟩_θ；2 通道示例 gap ≤ 0.006
- Vanishing ⟺ every-convention stabilizer: Π≤1 且 Haar 平均 =1 强迫 a.e. 相位成立

来源: Chu & Kharel (U. Chicago / U. Barcelona), PRL 格式 Letter, arXiv:2610.18955v1 [quant-ph], 2026-10-13. 同伴长文: arXiv:2607.13134 (推导细节)。