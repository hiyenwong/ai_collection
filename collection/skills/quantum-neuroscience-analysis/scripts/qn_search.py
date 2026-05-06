#!/usr/bin/env python3
"""
Quantum Neuroscience Knowledge Graph Search
搜索量子神经科学相关论文和方法
"""

import subprocess
from pathlib import Path

KG_TOOL = Path.home() / ".openclaw/workspace/scripts/kg_tool/target/release/kg_tool"
KG_DB = Path.home() / ".openclaw/workspace/kg.db"

QUANTUM_NEURO_KEYWORDS = [
    "quantum neural",
    "quantum EEG",
    "quantum brain",
    "quantum GNN",
    "quantum neuroscience",
    "quantum-inspired neural",
    "spiking quantum",
    "quantum Ising",
]

def run_kg_tool(command: str) -> str:
    """运行 kg_tool 命令"""
    cmd = f"{KG_TOOL} {command} {KG_DB}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

def search_quantum_neuro() -> dict:
    """搜索量子神经科学相关实体"""
    results = {}
    for keyword in QUANTUM_NEURO_KEYWORDS:
        output = run_kg_tool(f"search '{keyword}'")
        if output:
            results[keyword] = parse_search_results(output)
    return results

def parse_search_results(output: str) -> list:
    """解析搜索结果"""
    lines = output.strip().split('\n')
    entities = []
    for line in lines:
        if line.startswith('  ['):
            # 解析格式: [ID] type - name
            parts = line.split(' - ')
            if len(parts) >= 2:
                entity_id = parts[0].strip().replace('[', '').replace(']', '')
                type_name = parts[1].strip()
                entities.append({
                    "id": entity_id,
                    "name": type_name
                })
    return entities

def get_top_entities() -> list:
    """获取 PageRank 重要实体"""
    output = run_kg_tool("pagerank")
    lines = output.strip().split('\n')
    entities = []
    for line in lines[:10]:
        if 'Entity' in line:
            parts = line.split(':')
            if len(parts) >= 2:
                entity_id = parts[0].strip().replace('Entity ', '')
                score = parts[1].strip()
                entities.append({"id": entity_id, "pagerank": float(score)})
    return entities

def get_communities() -> dict:
    """获取社区检测结果"""
    output = run_kg_tool("louvain")
    communities = {}
    for line in output.strip().split('\n'):
        if '-> Community' in line:
            parts = line.split('->')
            if len(parts) >= 2:
                entity_id = parts[0].strip().replace('Entity ', '')
                community_id = parts[1].strip().replace('Community ', '')
                communities[entity_id] = community_id
    return communities

def generate_report(search_results: dict, top_entities: list, communities: dict) -> str:
    """生成分析报告"""
    report = "# Quantum Neuroscience Analysis Report\n\n"
    
    # 概述
    total_entities = sum(len(v) for v in search_results.values())
    report += "## 概述\n"
    report += f"- 搜索关键词数: {len(QUANTUM_NEURO_KEYWORDS)}\n"
    report += f"- 相关实体数: {total_entities}\n"
    report += f"- 社区数: {len(set(communities.values()))}\n\n"
    
    # 搜索结果
    report += "## 关键词搜索结果\n\n"
    for keyword, entities in search_results.items():
        if entities:
            report += f"### {keyword}\n"
            for entity in entities[:5]:
                report += f"- [{entity['id']}] {entity['name']}\n"
            report += "\n"
    
    # 重要实体
    report += "## PageRank 重要实体\n\n"
    for entity in top_entities[:5]:
        report += f"- Entity {entity['id']}: score={entity['pagerank']:.4f}\n"
    
    return report

def main():
    """主函数"""
    print("🔍 Quantum Neuroscience Knowledge Graph Analysis")
    print("=" * 50)
    
    # 搜索
    print("\n1. 搜索量子神经科学关键词...")
    search_results = search_quantum_neuro()
    
    # PageRank
    print("\n2. 计算 PageRank...")
    top_entities = get_top_entities()
    
    # 社区检测
    print("\n3. 运行社区检测...")
    communities = get_communities()
    
    # 生成报告
    print("\n4. 生成分析报告...")
    report = generate_report(search_results, top_entities, communities)
    
    # 输出
    print("\n" + "=" * 50)
    print(report)
    
    # 保存报告
    report_path = Path.home() / ".openclaw/workspace/memory" / "qn_analysis_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    print(f"\n✅ 报告已保存: {report_path}")

if __name__ == "__main__":
    main()