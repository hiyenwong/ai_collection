#!/usr/bin/env python3
"""
Deploy ai_collection agents to OpenClaw.

Usage:
    python deploy_agents.py --all
    python deploy_agents.py --agents fullstack-engineer,algorithm-engineer
    python deploy_agents.py --list
"""

import argparse
import json
import shutil
import sys
from pathlib import Path
import yaml


# Paths
AI_COLLECTION_ROOT = Path("/Users/hiyenwong/projects/ai_projects/ai_collection")
AGENTS_DIR = AI_COLLECTION_ROOT / "collection" / "agents"
OPENCLAW_ROOT = Path("/Users/hiyenwong/.openclaw")
OPENCLAW_AGENTS_DIR = OPENCLAW_ROOT / "agents"
OPENCLAW_CONFIG = OPENCLAW_ROOT / "openclaw.json"


def load_agent_yaml(agent_path: Path) -> dict:
    """Load agent configuration from YAML file."""
    yaml_file = agent_path / f"{agent_path.name}.agent.yaml"
    if yaml_file.exists():
        with open(yaml_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return None


def load_agent_md(agent_path: Path) -> dict:
    """Load agent configuration from MD file."""
    md_file = agent_path / f"{agent_path.name}.agent.md"
    if md_file.exists():
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Parse frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    return frontmatter
    return None


def get_agent_info(agent_path: Path) -> dict:
    """Get agent info from various sources."""
    info = {
        "id": agent_path.name,
        "name": agent_path.name.replace('-', ' ').title(),
        "description": "",
        "model": "zai/glm-4.7",  # Default model
    }
    
    # Try YAML first
    yaml_config = load_agent_yaml(agent_path)
    if yaml_config:
        info["id"] = yaml_config.get("id", info["id"])
        info["name"] = yaml_config.get("name", info["name"])
        info["description"] = yaml_config.get("persona", "")
        
        # Get model
        models = yaml_config.get("models", {})
        primary = models.get("primary", "")
        if primary:
            # Map model names
            model_map = {
                "claude-opus-4.5": "github-copilot/claude-opus-4.6",
                "claude-sonnet-4.5": "github-copilot/claude-sonnet-4.6",
                "claude-haiku-4.5": "github-copilot/claude-haiku-4.5",
            }
            info["model"] = model_map.get(primary, f"zai/{primary}")
    
    # Try MD file
    md_config = load_agent_md(agent_path)
    if md_config:
        info["id"] = md_config.get("id", info["id"])
        info["name"] = md_config.get("name", info["name"])
    
    return info


def list_available_agents() -> list[str]:
    """List all available agents in ai_collection."""
    agents = []
    for d in AGENTS_DIR.iterdir():
        if d.is_dir() and not d.name.startswith('.'):
            agents.append(d.name)
    return sorted(agents)


def create_workspace(agent_id: str) -> Path:
    """Create workspace directory for an agent."""
    workspace = OPENCLAW_ROOT / f"workspace-{agent_id}"
    workspace.mkdir(parents=True, exist_ok=True)
    
    # Create standard files
    (workspace / "AGENTS.md").write_text(f"# {agent_id} Workspace\n\nThis is the workspace for {agent_id}.\n")
    
    # Create memory directory
    (workspace / "memory").mkdir(exist_ok=True)
    
    return workspace


def create_agent_dir(agent_id: str) -> Path:
    """Create agent directory in OpenClaw."""
    agent_dir = OPENCLAW_AGENTS_DIR / agent_id / "agent"
    agent_dir.mkdir(parents=True, exist_ok=True)
    return agent_dir


def update_openclaw_config(agents_to_add: list[dict]) -> bool:
    """Update OpenClaw configuration with new agents."""
    if not OPENCLAW_CONFIG.exists():
        print(f"Error: OpenClaw config not found at {OPENCLAW_CONFIG}")
        return False
    
    with open(OPENCLAW_CONFIG, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Get existing agent IDs
    existing_ids = {a["id"] for a in config.get("agents", {}).get("list", [])}
    
    # Add new agents
    for agent in agents_to_add:
        if agent["id"] in existing_ids:
            print(f"  ⚠️  Agent {agent['id']} already exists, skipping")
            continue
        
        config["agents"]["list"].append({
            "id": agent["id"],
            "name": agent["name"],
            "workspace": str(OPENCLAW_ROOT / f"workspace-{agent['id']}"),
            "model": agent["model"],
        })
        print(f"  ✅ Added {agent['id']}")
    
    # Write back
    with open(OPENCLAW_CONFIG, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    
    return True


def deploy_agent(agent_id: str) -> bool:
    """Deploy a single agent."""
    agent_path = AGENTS_DIR / agent_id
    if not agent_path.exists():
        print(f"Error: Agent {agent_id} not found")
        return False
    
    # Get agent info
    _ = get_agent_info(agent_path)
    
    # Create workspace
    workspace = create_workspace(agent_id)
    print(f"  📁 Created workspace: {workspace}")
    
    # Create agent directory
    agent_dir = create_agent_dir(agent_id)
    print(f"  📁 Created agent dir: {agent_dir}")
    
    # Copy AGENT.md if exists
    agent_md = agent_path / "AGENT.md"
    if agent_md.exists():
        shutil.copy(agent_md, agent_dir / "AGENT.md")
        print("  📄 Copied AGENT.md")
    
    # Copy SOUL.md if exists
    soul_md = agent_path / "soul.md"
    if soul_md.exists():
        target = workspace / "SOUL.md"
        shutil.copy(soul_md, target)
        print("  📄 Copied SOUL.md to workspace")
    
    return True


def deploy_agents(agent_ids: list[str]) -> bool:
    """Deploy multiple agents."""
    agents_info = []
    
    for agent_id in agent_ids:
        print(f"\n📦 Deploying {agent_id}...")
        agent_path = AGENTS_DIR / agent_id
        
        if not agent_path.exists():
            print("  ❌ Agent not found")
            continue
        
        if deploy_agent(agent_id):
            info = get_agent_info(agent_path)
            agents_info.append(info)
    
    if agents_info:
        print("\n⚙️  Updating OpenClaw config...")
        if update_openclaw_config(agents_info):
            print(f"\n✅ Deployed {len(agents_info)} agents")
            print("   Run: openclaw gateway restart")
            return True
    
    return False


def main():
    parser = argparse.ArgumentParser(description="Deploy ai_collection agents to OpenClaw")
    parser.add_argument("--all", action="store_true", help="Deploy all agents")
    parser.add_argument("--agents", help="Comma-separated list of agents to deploy")
    parser.add_argument("--list", action="store_true", help="List available agents")
    
    args = parser.parse_args()
    
    if args.list:
        print("Available agents in ai_collection:")
        for agent in list_available_agents():
            print(f"  - {agent}")
        return 0
    
    if args.all:
        agents = list_available_agents()
        deploy_agents(agents)
        return 0
    
    if args.agents:
        agents = [a.strip() for a in args.agents.split(",")]
        deploy_agents(agents)
        return 0
    
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())