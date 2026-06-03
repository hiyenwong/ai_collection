# 基础搜索示例

## 语义搜索

```bash
# 搜索与编程相关的技能
skill-rag search "AI 编程助手"

# 搜索数据分析技能
skill-rag search "金融数据分析"

# 搜索文档相关技能
skill-rag search "文档处理和生成"
```

## 关键词搜索

```bash
# 搜索包含特定关键词的技能
skill-rag search --keyword "python"
skill-rag search --keyword "web"
skill-rag search --keyword "stock"
```

## 混合搜索

```bash
# 结合语义和关键词搜索
skill-rag search "构建网站" --hybrid
skill-rag search "数据分析" --hybrid --limit 3
```

## 输出格式示例

```
=== Search Results for "股票分析" ===

1. 🟢 stock-analysis [92.3%]
   ID: stock-analysis
   Path: ../../collection/skills/stock-analysis
   股票技术分析系统，提供技术指标计算、评分模型和可视化...

2. 🟡 akshare [85.1%]
   ID: akshare
   Path: ../../collection/skills/akshare
   中国金融数据接口库，提供股票、期货、基金等数据...
```
