# HuggingFace 模型快速调研

当 web_search 被 CAPTCHA 拦截时，可直接用 curl 调 HuggingFace API 查询模型。

## 搜索特定架构 + 训练方法的模型

```bash
# 按关键词搜索（GRPO 训练的 Qwen 模型，按下载量排序）
curl -s --proxy http://127.0.0.1:7890 \
  "https://huggingface.co/api/models?search=qwen+GRPO&sort=downloads&direction=-1&limit=10"
```

返回 JSON 包含：模型 ID、下载量、pipeline_tag、base_model、标签（含训练框架 trl/grpo 等信息）。

## 常用查询模式

| 目的 | 搜索词 |
|------|--------|
| GRPO 训练的小模型 | `search=GRPO&sort=downloads&limit=15` |
| 特定基座的 GRPO 版 | `search=qwen+GRPO&sort=downloads` |
| DeepSeek R1 蒸馏版 | `search=DeepSeek-R1-Distill` |
| 轻量 vLLM 兼容 | `search=smollm+instruct` |

## JSON 解析示例

```python
import json, sys
data = json.load(sys.stdin)
for m in data:
    tags = m.get('tags', [])
    pipeline = m.get('pipeline_tag', '')
    base = [t.split(':')[-1] for t in tags if t.startswith('base_model')]
    print(f"{m['id']} | {pipeline} | {m['downloads']} 下载 | base: {base}")
```

## 注意事项

- 需代理（`--proxy http://127.0.0.1:7890`）
- 免费 API，无需 key
- 返回结果基于搜索相关性 + 下载量排序
- 标签中 `base_model:finetune:` 表示微调基座，`base_model:quantized:` 表示量化版
