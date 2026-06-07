---
name: hierarchical-moe-detection
description: "分层 MoE 架构技能 - 用于对象检测的分层实例条件化混合专家模型 (HI-MoE)。通过两级路由机制实现稀疏计算与实例中心结构的匹配。基于论文 HI-MoE: Hierarchical Instance-Conditioned Mixture-of-Experts (arXiv 2604.04908)。激活关键词: MoE, mixture of experts, object detection MoE, instance routing, 分层路由, 实例条件化。"
---

# Hierarchical Instance-Conditioned MoE (HI-MoE)

用于对象检测的分层实例条件化混合专家架构。

## 核心创新

### 问题背景

- 传统 MoE 在图像/patch 层级路由
- **对象检测的基本单位**: 对象查询 (object query) → 候选实例
- **粒度不匹配**: Patch-level routing ≠ Instance-level reasoning

### HI-MoE 双阶段路由

1. **场景路由器 (Scene Router)**: 轻量级，选择场景一致的专家子集
2. **实例路由器 (Instance Router)**: 将每个对象查询分配到子集内的少数专家

## 激活关键词

- MoE
- mixture of experts
- object detection MoE
- instance routing
- 分层路由
- 实例条件化
- HI-MoE
- 检测 MoE

## 工具使用

- exec: 运行 MoE 模型推理和训练
- read: 加载模型配置和路由参数
- write: 保存路由日志和专家分配结果

## 架构设计

### Step 1: 场景路由器

```python
class SceneRouter(nn.Module):
    def __init__(self, num_experts=16, scene_subset_size=4):
        super().__init__()
        self.num_experts = num_experts
        self.subset_size = scene_subset_size
        
        # 轻量级场景编码器
        self.scene_encoder = nn.Sequential(
            nn.Conv2d(256, 128, kernel_size=3),
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(128, num_experts)
        )
    
    def forward(self, features):
        # 编码全局场景特征
        scene_logits = self.scene_encoder(features)
        
        # 选择 top-k 专家子集
        top_k_indices = torch.topk(scene_logits, self.subset_size).indices
        
        return top_k_indices, scene_logits
```

### Step 2: 实例路由器

```python
class InstanceRouter(nn.Module):
    def __init__(self, num_experts_per_instance=2):
        super().__init__()
        self.num_experts = num_experts_per_instance
        
        # 实例级路由网络
        self.router = nn.Linear(256, num_experts_per_instance)
    
    def forward(self, object_queries, scene_subset):
        # 只在场景子集内路由
        query_features = object_queries  # [N, 256]
        
        # 计算路由权重
        router_logits = self.router(query_features)  # [N, num_experts_per_instance]
        
        # 分配到子集内的专家
        expert_assignments = []
        for i, query in enumerate(query_features):
            top_k = torch.topk(router_logits[i], self.num_experts).indices
            expert_assignments.append(scene_subset[top_k])
        
        return expert_assignments, router_logits
```

### Step 3: HI-MoE 集成

```python
class HIMoE(nn.Module):
    def __init__(
        self,
        num_experts=16,
        scene_subset=4,
        instance_experts=2
    ):
        super().__init__()
        
        self.scene_router = SceneRouter(num_experts, scene_subset)
        self.instance_router = InstanceRouter(instance_experts)
        
        # 专家网络
        self.experts = nn.ModuleList([
            ExpertNetwork() for _ in range(num_experts)
        ])
    
    def forward(self, features, object_queries):
        # Stage 1: 场景路由
        scene_subset, scene_logits = self.scene_router(features)
        
        # Stage 2: 实例路由
        expert_assignments, router_logits = self.instance_router(
            object_queries, scene_subset
        )
        
        # Stage 3: 专家处理
        outputs = []
        for query_idx, experts_idx in enumerate(expert_assignments):
            query = object_queries[query_idx]
            expert_outputs = []
            
            for exp_idx in experts_idx:
                expert_out = self.experts[exp_idx](query)
                expert_outputs.append(expert_out)
            
            # 组合专家输出
            combined = torch.mean(torch.stack(expert_outputs), dim=0)
            outputs.append(combined)
        
        return torch.stack(outputs), {
            "scene_subset": scene_subset,
            "expert_assignments": expert_assignments
        }
```

## 性能优势

基于论文实验 (COCO 数据集):

- **小对象检测提升**: +2.5 AP (small objects)
- **计算效率**: 保持稀疏计算优势
- **专家专业化**: 可视化显示专家分工模式

## 训练策略

### Step 1: 路由平衡损失

```python
def router_balance_loss(router_logits, num_experts):
    """确保专家负载均衡."""
    
    # 计算每个专家的路由概率
    router_probs = F.softmax(router_logits, dim=-1)
    
    # 统计每个专家被选中的频率
    expert_freq = router_probs.mean(dim=0)
    
    # 目标: 均衡分布
    target_freq = torch.ones(num_experts) / num_experts
    
    # 平衡损失
    balance_loss = F.mse_loss(expert_freq, target_freq)
    
    return balance_loss
```

### Step 2: 专家多样性损失

```python
def expert_diversity_loss(expert_outputs):
    """鼓励专家差异化."""
    
    # 计算专家输出的相似度矩阵
    num_experts = len(expert_outputs)
    similarity_matrix = torch.zeros(num_experts, num_experts)
    
    for i in range(num_experts):
        for j in range(i+1, num_experts):
            cos_sim = F.cosine_similarity(
                expert_outputs[i].flatten(),
                expert_outputs[j].flatten(),
                dim=0
            )
            similarity_matrix[i, j] = cos_sim
    
    # 目标: 低相似度 (高多样性)
    diversity_loss = similarity_matrix.mean()
    
    return diversity_loss
```

## 配置参数

| 参数 | 推荐值 | 说明 |
|-----|--------|------|
| num_experts | 16-32 | 总专家数量 |
| scene_subset | 4-8 | 场景级专家子集大小 |
| instance_experts | 2-3 | 每个实例分配的专家数 |

## 可视化专家分工

```python
def visualize_expert_specialization(model, dataset):
    """可视化专家的分工模式."""
    
    expert_stats = {
        i: {"small_objects": 0, "large_objects": 0}
        for i in range(model.num_experts)
    }
    
    for sample in dataset:
        features, queries = sample
        outputs, routing_info = model(features, queries)
        
        # 统计每个专家处理的实例类型
        for assignment in routing_info["expert_assignments"]:
            for exp_idx in assignment:
                # 根据实例大小统计
                if is_small_object(queries[assignment]):
                    expert_stats[exp_idx]["small_objects"] += 1
                else:
                    expert_stats[exp_idx]["large_objects"] += 1
    
    return expert_stats
```

## 应用场景

### 场景 1: 小对象检测优化

```
用户: 小对象检测效果不好
AI: 使用 HI-MoE 架构，分配专门的小对象专家...
   [配置路由]
   ✓ Expert 3, 7, 11 专门处理小对象 (+2.5 AP)
```

### 场景 2: 多尺度检测

```
用户: 需要处理多尺度对象
AI: 使用分层路由，专家分工处理不同尺度...
   [场景路由 + 实例路由]
   ✓ 场景路由: 选择 4 个专家
   ✓ 实例路由: 每个查询分配 2 个专家
```

## 扩展方向

- **动态专家数量**: 根据场景复杂度调整
- **跨任务迁移**: 专家在不同检测任务间共享
- **实时推理优化**: 进一步降低路由开销

## 相关论文

- **arXiv 2604.04908**: HI-MoE: Hierarchical Instance-Conditioned Mixture-of-Experts
- **相关工作**: MoE for vision, DETR architecture