# GitHub Truncation Fix - collection/skills/ 优化方案

## 问题分析

**现象：** GitHub显示目录时截断，提示 "Sorry, we had to truncate this directory to 1,000 files. 839 entries were omitted from the list."

**根本原因：**
- collection/skills/ 包含1844个子目录（技能）
- GitHub单目录显示限制为1000个文件/目录
- 超出839个目录被截断显示

**影响：**
- GitHub Web界面无法完整查看所有技能
- 影响可发现性和文档体验
- 可能影响git操作效率

## 解决方案

### 方案A：按领域分目录（推荐）

将1844个技能按领域分组到子目录：

```
collection/skills/
├── neuroscience/           (~500个技能)
├── quantum/                (~400个技能)
├── ai-ml/                  (~300个技能)
├── systems-engineering/    (~200个技能)
├── control-systems/        (~150个技能)
├── finance/                (~100个技能)
├── medical/                (~80个技能)
├── tools-frameworks/       (~70个技能)
├── math-statistics/        (~50个技能)
└── other/                  (~94个技能)
```

**优点：**
- 每个子目录不超过500个，符合GitHub限制
- 更好的语义组织和可发现性
- 保持技能独立性，不影响hermes加载

**实施步骤：**
1. 创建领域分类脚本（基于skill metadata自动分类）
2. 移动技能到对应领域目录
3. 更新INDEX.md和SKILLS.md
4. 提交更改

### 方案B：使用GitHub Actions自动索引

保留现有结构，但创建动态索引页面：

```
collection/skills/
├── INDEX_BY_DOMAIN.md    # 按领域索引
├── INDEX_BY_DATE.md      # 按时间索引  
├── INDEX_FULL.md         # 完整列表（本地生成）
└── (1844个技能目录保持不变)
```

**优点：**
- 不需要移动文件
- 保持现有工作流不变
- 提供多种查看方式

**缺点：**
- GitHub截断问题仍存在
- Web界面体验不佳

### 方案C：混合方案（平衡）

同时采用方案A和B：
1. 对高频使用的核心技能（~200个）保持在顶层
2. 其他技能按领域分组到子目录
3. 创建多个索引文件

```
collection/skills/
├── core-skills/           # 核心技能（推荐/常用）
├── neuroscience/
├── quantum/
├── ... (其他领域)
├── INDEX.md               # 总索引
└── README.md              # 查看说明
```

## 立即可执行的临时方案

**不改变目录结构，但改善GitHub显示体验：**

1. **添加查看指南：** 在README中说明如何查看完整列表
2. **提供本地查看方法：** git clone后本地查看无限制
3. **创建可搜索索引：** INDEX.md包含完整列表，可通过搜索找到

## 推荐采用：方案A（按领域分目录）

**理由：**
- 解决截断问题的根本方案
- 提升组织性和可发现性
- 符合用户偏好（研究偏好明确的领域分类）
- 对hermes技能加载无影响（路径仍可识别）

## 下一步行动

1. 分析现有技能分布（领域统计）
2. 设计领域分类规则
3. 创建自动化迁移脚本
4. 执行迁移并验证
5. 更新文档和索引
6. git commit提交更改

---

**Created:** 2026-06-04
**Status:** 待执行（需用户确认选择哪个方案）