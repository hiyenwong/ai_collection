#!/usr/bin/env python3
"""
自动拆分过大的域目录
当某个域的技能数量超过阈值时,根据子主题进行拆分
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from collections import defaultdict

# 拆分阈值
SPLIT_THRESHOLD = 800  # 超过800个技能时开始拆分

# 子主题分类规则 (基于技能名称关键词)
SUBTOPIC_KEYWORDS = {
    'neuroscience': {
        'brain-network': ['brain', 'network', 'connectivity', 'graph', 'gnn', 'fmri', 'eeg'],
        'spiking-neurons': ['spiking', 'snn', 'spike', 'neuromorphic', 'neuron', 'synaptic', 'plasticity'],
        'cognitive': ['cognitive', 'memory', 'attention', 'learning', 'behavioral', 'decision'],
        'neural-dynamics': ['dynamics', 'oscillatory', 'attractor', 'kuramoto', 'rnn', 'recurrent'],
        'encoding-decoding': ['encoding', 'decoding', 'bci', 'signal', 'neural-code', 'representation'],
        'computational': ['computational', 'model', 'simulation', 'digital-twin', 'inverse'],
    },
    'quantum': {
        'quantum-computing': ['quantum-computing', 'quantum-circuit', 'quantum-algorithm', 'qaoa', 'vqe', 'qubit'],
        'quantum-error': ['qec', 'error-correction', 'quantum-error', 'fault-tolerant', 'decoding', 'syndrome'],
        'quantum-ml': ['qml', 'quantum-ml', 'quantum-machine-learning', 'qnn', 'quantum-neural', 'variational'],
        'quantum-physics': ['quantum-physics', 'quantum-state', 'hamiltonian', 'entanglement', 'quantum-dynamics'],
        'quantum-network': ['quantum-network', 'quantum-communication', 'qkd', 'entanglement-distribution', 'routing'],
        'quantum-control': ['quantum-control', 'optimal-control', 'pulse', 'gate', 'compilation'],
    },
    'ai-ml': {
        'deep-learning': ['deep-learning', 'neural-network', 'cnn', 'rnn', 'transformer', 'attention'],
        'reinforcement-learning': ['rl', 'reinforcement', 'policy', 'reward', 'grpo', 'ppo', 'dpo'],
        'optimization': ['optimization', 'gradient', 'training', 'fine-tuning', 'lora', 'adam', 'sgd'],
        'generative': ['generative', 'diffusion', 'gan', 'vae', 'generation', 'sampling'],
        'interpretability': ['interpretability', 'explainable', 'sae', 'probe', 'attention', 'mechanistic'],
        'inference': ['inference', 'deployment', 'serving', 'quantization', 'kv-cache', 'speculative'],
    },
    'spiking-neuromorphic': {
        'snn-architecture': ['snn-architecture', 'spiking-transformer', 'snn-layer', 'neuron-model', 'lif'],
        'snn-training': ['snn-training', 'stdp', 'surrogate', 'gradient', 'backprop', 'learning-rule'],
        'snn-hardware': ['fpga', 'hardware', 'loihi', 'neuromorphic-chip', 'accelerator', 'edge'],
        'snn-applications': ['snn-applications', 'vision', 'detection', 'recognition', 'bci', 'control'],
        'snn-theory': ['snn-theory', 'approximation', 'universal', 'capacity', 'memory', 'dynamics'],
    }
}

def count_skills_in_domain(domain_path):
    """计算域目录中的技能数量"""
    count = 0
    for skill_dir in Path(domain_path).iterdir():
        if skill_dir.is_dir() and not skill_dir.name.startswith('.'):
            if (skill_dir / 'SKILL.md').exists():
                count += 1
    return count

def classify_skill_by_subtopic(skill_name, domain):
    """根据技能名称和关键词分类到子主题"""
    if domain not in SUBTOPIC_KEYWORDS:
        return 'general'
    
    subtopics = SUBTOPIC_KEYWORDS[domain]
    
    # 按关键词匹配
    for subtopic, keywords in subtopics.items():
        for keyword in keywords:
            if keyword in skill_name.lower():
                return subtopic
    
    return 'general'

def get_all_skills_in_domain(domain_path):
    """获取域目录中所有技能的名称"""
    skills = []
    for skill_dir in Path(domain_path).iterdir():
        if skill_dir.is_dir() and not skill_dir.name.startswith('.'):
            if (skill_dir / 'SKILL.md').exists():
                skills.append(skill_dir.name)
    return skills

def plan_subdivision(domain_path, domain_name):
    """规划拆分方案"""
    skills = get_all_skills_in_domain(domain_path)
    
    if len(skills) < SPLIT_THRESHOLD:
        return None
    
    # 分类到子主题
    subtopic_groups = defaultdict(list)
    for skill in skills:
        subtopic = classify_skill_by_subtopic(skill, domain_name)
        subtopic_groups[subtopic].append(skill)
    
    # 生成迁移计划
    migration_plan = []
    for subtopic, skill_list in subtopic_groups.items():
        if len(skill_list) > 0:  # 只迁移有技能的子主题
            for skill in skill_list:
                migration_plan.append({
                    'source': f"collection/skills/{domain_name}/{skill}",
                    'target': f"collection/skills/{domain_name}-{subtopic}/{skill}"
                })
    
    return migration_plan

def execute_migration(migration_plan, dry_run=True):
    """执行迁移"""
    if not migration_plan:
        print("No migration needed")
        return True
    
    print(f"Planning to migrate {len(migration_plan)} skills")
    
    if dry_run:
        print("\n[DRY RUN] Migration plan:")
        for item in migration_plan[:10]:  # 只显示前10个
            print(f"  {item['source']} -> {item['target']}")
        if len(migration_plan) > 10:
            print(f"  ... and {len(migration_plan) - 10} more")
        print("\nTo execute, run with --execute flag")
        return True
    
    # 执行git mv
    print("\nExecuting migration...")
    success_count = 0
    error_count = 0
    
    for item in migration_plan:
        source = item['source']
        target = item['target']
        
        try:
            # 创建目标目录
            target_dir = Path(target).parent
            target_dir.mkdir(parents=True, exist_ok=True)
            
            # 执行git mv
            cmd = ['git', 'mv', source, target]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=Path.cwd())
            
            if result.returncode == 0:
                success_count += 1
            else:
                print(f"Error moving {source}: {result.stderr}")
                error_count += 1
        except Exception as e:
            print(f"Error: {e}")
            error_count += 1
    
    print(f"\nMigration complete:")
    print(f"  Success: {success_count}")
    print(f"  Errors: {error_count}")
    
    return error_count == 0

def main():
    # 确定repository根目录
    if len(sys.argv) > 1:
        root_path = Path(sys.argv[1])
    else:
        root_path = Path.cwd()
    
    # 解析参数
    execute_mode = '--execute' in sys.argv
    
    print(f"Scanning repository: {root_path}")
    print()
    
    # 扫描所有域目录
    skills_path = root_path / "collection" / "skills"
    
    if not skills_path.exists():
        print("Error: collection/skills/ directory not found")
        sys.exit(1)
    
    domains_to_split = []
    
    for domain_dir in skills_path.iterdir():
        if domain_dir.is_dir() and not domain_dir.name.startswith('.'):
            skill_count = count_skills_in_domain(domain_dir)
            
            if skill_count >= SPLIT_THRESHOLD:
                domains_to_split.append({
                    'name': domain_dir.name,
                    'path': str(domain_dir),
                    'count': skill_count
                })
    
    print("=" * 80)
    print("DOMAINS NEEDING SUBDIVISION:")
    print("=" * 80)
    
    if not domains_to_split:
        print("No domains exceed the threshold. All OK!")
        sys.exit(0)
    
    for domain in domains_to_split:
        print(f"  {domain['name']}: {domain['count']} skills (threshold: {SPLIT_THRESHOLD})")
    
    print()
    
    # 为每个域规划拆分
    for domain in domains_to_split:
        print("=" * 80)
        print(f"Planning subdivision for: {domain['name']}")
        print("=" * 80)
        
        migration_plan = plan_subdivision(domain['path'], domain['name'])
        
        if migration_plan:
            success = execute_migration(migration_plan, dry_run=not execute_mode)
            
            if not success and execute_mode:
                print(f"\nError during migration for {domain['name']}")
                sys.exit(1)
        else:
            print(f"  {domain['name']} doesn't need subdivision")
    
    if execute_mode:
        print("\n✅ All subdivisions completed successfully!")
    else:
        print("\n✅ All subdivisions planned. Run with --execute to apply changes.")
    
    sys.exit(0)

if __name__ == "__main__":
    main()