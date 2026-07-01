---
title: Cohort-Amortized Personalization for Virtual Brain Twins
paper_id: 2606.30329
date: 2026-06-29
tags: [brain-networks, personalization, privacy, virtual-brain-twins, mechanistic-modeling]
---

# Cohort-Amortized Personalization: Navigating the Privacy-Utility Frontier for Virtual Brain Twins

## 核心创新

提出 **Cohort-Amortized Personalization (CAP)** 框架，解决个性化脑模型临床转化中的两大障碍：
1. **隐私壁垒**：个体神经影像数据难以共享，存在重新识别风险
2. **计算成本**：逐被试拟合需要数小时计算，限制多中心合作

## 方法论

### 核心思想
- **模型共享替代数据共享**：在群体先验上训练神经密度估计器，仅分发紧凑估计器
- **秒级个性化**：新被试在本地数据上秒级完成个性化（vs 传统小时级）
- **跨图谱兼容**：CrossCoder 将 20 种解剖图谱映射到共享潜空间，支持异构图谱的多中心部署

### 技术架构
1. **群体先验训练**：
   - 在机械全脑模型的模拟数据上训练神经密度估计器
   - 采用低秩群体先验，确保紧凑性

2. **CrossCoder 跨图谱映射**：
   - 自编码器学习图谱无关的潜空间表示
   - 支持不同中心使用不同图谱模板

3. **个性化推理**：
   - 分发训练好的估计器
   - 新被试在本地数据上秒级推理

## 验证结果

### 癫痫队列（21 名药物难治性癫痫患者）
- **任务**：致痫灶定位
- **性能**：F1 = 0.56
- **对比**：匹配或超过逐被试推理

### 老化队列（832 名 1000BRAINS 被试）
- **任务**：年龄预测
- **性能**：r = 0.44
- **速度提升**：小时级 → 秒级

## 临床意义

### Synthetic Access 治理审计
- **机制替代**：共享估计器可作为机制替代物，支持：
  - 计算机实验
  - 合成队列生成
  - 无需原始数据访问
- **治理合规**：提供隐私友好的替代方案，促进个性化建模在更多场景的应用

### 隐私-效用边界
- **隐私保护**：无需共享原始数据
- **效用保持**：匹配或超过传统逐被试方法
- **可扩展性**：支持多中心、异构图谱的大规模部署

## 关键贡献

1. **方法创新**：首次提出群体摊销个性化框架
2. **跨图谱兼容**：CrossCoder 解决图谱异质性问题
3. **临床验证**：在癫痫和老化队列中验证有效性
4. **治理框架**：提出 synthetic access 概念，为隐私合规提供路径

## 潜在应用

- **多中心临床试验**：无需数据共享即可个性化建模
- **罕见病研究**：小样本队列的快速个性化
- **实时临床应用**：秒级推理支持临床决策
- **跨平台部署**：不同图谱模板的无缝迁移

## 局限性

- 依赖机械全脑模型的质量
- 群体先验可能无法捕获极端个体差异
- 需要预训练阶段的计算资源

## 相关文献

- 全脑网络模型：Jirsa et al. (2017)
- 个性化医学：Marquand et al. (2016)
- 联邦学习：McMahan et al. (2017)

---

**激活词**: cohort-amortized, virtual brain twins, privacy-preserving, cross-atlas, neural density estimator
