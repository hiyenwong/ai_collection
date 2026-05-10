#!/usr/bin/env python3
"""
Agent-First Project Bootstrap CLI

Usage:
    agent-bootstrap init          # Interactive project initialization
    agent-bootstrap interview     # Run interview phases
    agent-bootstrap generate      # Generate artifacts
    agent-bootstrap validate      # Validate project structure
    agent-bootstrap garden        # Doc-gardening check
"""

import argparse
import json
from pathlib import Path
from dataclasses import dataclass, field, asdict

@dataclass
class ProjectVision:
    description: str = ""
    target_users: str = ""
    success_metrics: list = field(default_factory=list)
    time_constraints: str = ""
    constraints: list = field(default_factory=list)
    out_of_scope: list = field(default_factory=list)

@dataclass
class ProjectArchitecture:
    domains: list = field(default_factory=list)
    layers: list = field(default_factory=lambda: ["types", "config", "repo", "service", "runtime", "ui"])
    cross_cutting: list = field(default_factory=lambda: ["auth", "logging", "feature-flags"])
    external_deps: list = field(default_factory=list)

@dataclass
class AgentConfig:
    conventions: dict = field(default_factory=dict)
    constraints: list = field(default_factory=list)
    capabilities: list = field(default_factory=list)
    feedback_loops: list = field(default_factory=list)

@dataclass
class ProjectConfig:
    vision: ProjectVision = field(default_factory=ProjectVision)
    architecture: ProjectArchitecture = field(default_factory=ProjectArchitecture)
    agent_config: AgentConfig = field(default_factory=AgentConfig)
    docs_path: str = "docs/"
    tools: list = field(default_factory=lambda: ["codex", "claude", "copilot", "qwen"])


class InterviewConductor:
    """Interactive interview for project setup"""
    
    def __init__(self):
        self.config = ProjectConfig()
    
    def conduct_phase1_vision(self) -> None:
        """Phase 1: Vision & Goals"""
        print("\n" + "="*50)
        print("Phase 1: Vision & Goals")
        print("="*50 + "\n")
        
        self.config.vision.description = input("📝 What are we building? (one-line description)\n> ").strip()
        
        print("\n👥 Who are the target users?")
        self.config.vision.target_users = input("> ").strip()
        
        print("\n🎯 What does success look like? (one metric per line, empty to finish)")
        while True:
            metric = input("> ").strip()
            if not metric:
                break
            self.config.vision.success_metrics.append(metric)
        
        print("\n⏰ Time constraints?")
        self.config.vision.time_constraints = input("> ").strip()
        
        print("\n🔒 Constraints? (one per line, empty to finish)")
        while True:
            constraint = input("> ").strip()
            if not constraint:
                break
            self.config.vision.constraints.append(constraint)
        
        print("\n🚫 What is out of scope? (one per line, empty to finish)")
        while True:
            item = input("> ").strip()
            if not item:
                break
            self.config.vision.out_of_scope.append(item)
    
    def conduct_phase2_architecture(self) -> None:
        """Phase 2: Architecture & Domain"""
        print("\n" + "="*50)
        print("Phase 2: Architecture & Domain")
        print("="*50 + "\n")
        
        print("🏗️ Core domains? (comma-separated)")
        domains_input = input("> ").strip()
        self.config.architecture.domains = [d.strip() for d in domains_input.split(",") if d.strip()]
        
        print("\n📚 Layers per domain? (default: types, config, repo, service, runtime, ui)")
        layers_input = input("> ").strip()
        if layers_input:
            self.config.architecture.layers = [layer.strip() for layer in layers_input.split(",")]
        
        print("\n🔀 Cross-cutting concerns? (default: auth, logging, feature-flags)")
        cc_input = input("> ").strip()
        if cc_input:
            self.config.architecture.cross_cutting = [c.strip() for c in cc_input.split(",")]
        
        print("\n🔌 External dependencies? (one per line, empty to finish)")
        while True:
            dep = input("> ").strip()
            if not dep:
                break
            self.config.architecture.external_deps.append(dep)
    
    def conduct_phase3_agent_config(self) -> None:
        """Phase 3: Agent Configuration"""
        print("\n" + "="*50)
        print("Phase 3: Agent Configuration")
        print("="*50 + "\n")
        
        print("📐 Default coding conventions? (Y/n)")
        use_defaults = input("> ").strip().lower() != 'n'
        
        if not use_defaults:
            print("\nNaming pattern for files?")
            self.config.agent_config.conventions["naming"] = input("> ").strip()
            
            print("Max file size (lines)?")
            self.config.agent_config.conventions["max_file_size"] = int(input("> ").strip() or "300")
        
        print("\n✅ Enable agent-to-agent review? (Y/n)")
        if input("> ").strip().lower() != 'n':
            self.config.agent_config.feedback_loops.append("agent-to-agent-review")
        
        print("\n📊 Test coverage threshold? (default: 80)")
        coverage = input("> ").strip()
        self.config.agent_config.constraints.append(f"test_coverage >= {coverage or '80'}%")
        
        print("\n🛠️ Target AI tools? (default: codex, claude, copilot, qwen)")
        tools_input = input("> ").strip()
        if tools_input:
            self.config.tools = [t.strip() for t in tools_input.split(",")]
    
    def conduct_phase4_docs(self) -> None:
        """Phase 4: Documentation Structure"""
        print("\n" + "="*50)
        print("Phase 4: Documentation Structure")
        print("="*50 + "\n")
        
        print("📁 Docs location? (default: docs/)")
        self.config.docs_path = input("> ").strip() or "docs/"
    
    def conduct_all(self) -> ProjectConfig:
        """Run all interview phases"""
        print("\n🚀 Agent-First Project Bootstrap\n")
        
        self.conduct_phase1_vision()
        self.conduct_phase2_architecture()
        self.conduct_phase3_agent_config()
        self.conduct_phase4_docs()
        
        print("\n✅ Interview complete!\n")
        return self.config


class ArtifactGenerator:
    """Generate project artifacts from config"""
    
    def __init__(self, config: ProjectConfig, base_path: Path):
        self.config = config
        self.base_path = base_path
    
    def generate_all(self) -> list:
        """Generate all artifacts"""
        created = []
        created.extend(self.generate_agents_md())
        created.extend(self.generate_tool_configs())
        created.extend(self.generate_docs_structure())
        created.extend(self.generate_ci())
        return created
    
    def generate_agents_md(self) -> list:
        """Generate AGENTS.md"""
        content = f"""# Agent Guide: {self.config.vision.description or 'Project'}

## Quick Start
- Run tests: `npm test` / `cargo test` / `pytest`
- Open PR: Create branch, commit, push
- Get help: Check docs/design/

## Architecture
- See: {self.config.docs_path}architecture/README.md
- Layers: {' → '.join(self.config.architecture.layers)}
- Cross-cutting: {', '.join(self.config.architecture.cross_cutting)}

## Key Domains
| Domain | Docs | Status |
|--------|------|--------|
{self._generate_domain_table()}

## Conventions
- Naming: Use consistent patterns per domain
- Logging: Structured JSON via logger
- Tests: Required for all new code
- Max file size: {self.config.agent_config.conventions.get('max_file_size', 300)} lines

## Constraints (Enforced)
- Layer dependencies: forward only
- Test coverage: >80%
- No manual code changes (agent-first)

## Where to Learn More
- Design: {self.config.docs_path}design/
- Quality: {self.config.docs_path}quality/
- Plans: {self.config.docs_path}plans/
- Debt: {self.config.docs_path}debt.md

## Agent Workflow
1. Read this file first
2. Check {self.config.docs_path}design/ for context
3. Follow layer constraints strictly
4. Write tests before implementation
5. Self-review changes
6. Open PR for agent review
7. Iterate until all reviewers pass
"""
        path = self.base_path / "AGENTS.md"
        path.write_text(content)
        return [f"✓ AGENTS.md ({len(content.splitlines())} lines)"]
    
    def _generate_domain_table(self) -> str:
        lines = []
        for domain in self.config.architecture.domains:
            lines.append(f"| {domain} | {self.config.docs_path}design/{domain.lower()}.md | Active |")
        return "\n".join(lines)
    
    def generate_tool_configs(self) -> list:
        """Generate tool-specific configs"""
        created = []
        
        # CLAUDE.md
        if "claude" in self.config.tools:
            content = f"""# Claude Code Instructions

## Project Context
This project follows Agent-First methodology.
Read AGENTS.md first, then {self.config.docs_path}architecture/README.md.

## Workflow
1. Understand goal from user
2. Check {self.config.docs_path}design/ for relevant context
3. Follow layer constraints strictly
4. Write tests before implementation
5. Self-review changes
6. Open PR for review

## Constraints
- Max file size: {self.config.agent_config.conventions.get('max_file_size', 300)} lines
- Test coverage: >80%
- Use structured logging
- Follow naming conventions in AGENTS.md

## Vision
{self.config.vision.description}
"""
            (self.base_path / "CLAUDE.md").write_text(content)
            created.append("✓ CLAUDE.md")
        
        # COPILOT.md
        if "copilot" in self.config.tools:
            content = f"""# GitHub Copilot Instructions

## Project Context
Agent-First project. See AGENTS.md for conventions.

## Coding Standards
- Follow layer architecture
- Use structured logging
- Write tests for new code
- Keep files under {self.config.agent_config.conventions.get('max_file_size', 300)} lines

## Architecture
See {self.config.docs_path}architecture/README.md

## Vision
{self.config.vision.description}
"""
            (self.base_path / "COPILOT.md").write_text(content)
            created.append("✓ COPILOT.md")
        
        return created
    
    def generate_docs_structure(self) -> list:
        """Generate docs directory structure"""
        created = []
        docs_path = self.base_path / self.config.docs_path
        
        # Create directories
        for subdir in ["design", "architecture", "quality", "plans/active", "plans/completed"]:
            (docs_path / subdir).mkdir(parents=True, exist_ok=True)
        
        # Generate README files
        (docs_path / "design" / "README.md").write_text(self._design_index())
        created.append(f"✓ {self.config.docs_path}design/README.md")
        
        (docs_path / "architecture" / "README.md").write_text(self._architecture_readme())
        created.append(f"✓ {self.config.docs_path}architecture/README.md")
        
        (docs_path / "quality" / "domains.md").write_text(self._quality_domains())
        created.append(f"✓ {self.config.docs_path}quality/domains.md")
        
        (docs_path / "debt.md").write_text("# Technical Debt\n\n> Track known technical debt here\n")
        created.append(f"✓ {self.config.docs_path}debt.md")
        
        # Generate domain designs
        for domain in self.config.architecture.domains:
            path = docs_path / "design" / f"{domain.lower()}.md"
            path.write_text(self._domain_template(domain))
            created.append(f"✓ {self.config.docs_path}design/{domain.lower()}.md")
        
        return created
    
    def _design_index(self) -> str:
        domains_list = "\n".join([f"- [{d}]({d.lower()}.md)" for d in self.config.architecture.domains])
        return f"""# Design Documents

## Domains
{domains_list}

## How to Write Design Docs
1. Start with user stories
2. Define API contracts
3. Document data models
4. List implementation notes
5. Define quality gates
"""
    
    def _architecture_readme(self) -> str:
        domains_table = "\n".join([f"| {d} | Domain | All |" for d in self.config.architecture.domains])
        return f"""# Architecture Overview

## Domains
| Domain | Description | Layers |
|--------|-------------|--------|
{domains_table}

## Layer Rules
```
{' → '.join(self.config.architecture.layers)}
         ↑
    Providers ({', '.join(self.config.architecture.cross_cutting)})
```

## Dependency Rules
- Forward only within domain
- Cross-domain via Service layer only
- Providers inject at Config layer

## Cross-Cutting Concerns
{chr(10).join([f'- {c}' for c in self.config.architecture.cross_cutting])}
"""
    
    def _quality_domains(self) -> str:
        rows = "\n".join([f"| {d} | 🟡 Pending | - | - |" for d in self.config.architecture.domains])
        return f"""# Domain Quality Tracking

| Domain | Status | Test Coverage | Notes |
|--------|--------|---------------|-------|
{rows}

## Quality Gates
- Test coverage > 80%
- All linters pass
- No layer violations
"""
    
    def _domain_template(self, domain: str) -> str:
        return f"""# {domain} Design

## Overview
[What this domain does]

## User Stories
1. As a [user], I want to [action]
2. ...

## API Contracts
[Endpoints/Interfaces]

## Data Models
[Schemas/Types]

## Implementation Notes
[Agent-relevant context]

## Quality Gates
- [ ] Unit tests >80%
- [ ] Integration tests pass
- [ ] Performance requirements met
"""
    
    def generate_ci(self) -> list:
        """Generate CI workflow"""
        created = []
        github_path = self.base_path / ".github" / "workflows"
        github_path.mkdir(parents=True, exist_ok=True)
        
        content = """name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup
        # Add your language setup here
        run: echo "Setup your language/toolchain"
      
      - name: Check file sizes
        run: |
          echo "Checking max file size constraint..."
          # find . -name "*.ts" -exec wc -l {} \\; | awk '$1 > 300 {{exit 1}}'
      
      - name: Run tests
        run: |
          echo "Run your test command"
          # npm test / cargo test / pytest
      
      - name: Coverage check
        run: |
          echo "Check coverage > 80%"
"""
        (github_path / "ci.yml").write_text(content)
        created.append("✓ .github/workflows/ci.yml")
        
        return created


class ProjectValidator:
    """Validate agent-first project structure"""
    
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.checks = []
    
    def validate(self) -> int:
        """Run all validation checks"""
        score = 0
        
        # Check AGENTS.md
        agents_md = self.base_path / "AGENTS.md"
        if agents_md.exists():
            lines = len(agents_md.read_text().splitlines())
            if lines < 200:
                self.checks.append(f"✓ AGENTS.md exists ({lines} lines)")
                score += 1
            else:
                self.checks.append(f"⚠ AGENTS.md too long ({lines} lines, should be <200)")
        else:
            self.checks.append("✗ AGENTS.md missing")
        
        # Check docs structure
        docs = self.base_path / "docs"
        for subdir in ["design", "architecture", "quality", "plans"]:
            if (docs / subdir).exists():
                self.checks.append(f"✓ docs/{subdir}/ exists")
                score += 1
            else:
                self.checks.append(f"✗ docs/{subdir}/ missing")
        
        # Check tool configs
        for tool in ["CLAUDE.md", "COPILOT.md"]:
            if (self.base_path / tool).exists():
                self.checks.append(f"✓ {tool} exists")
                score += 1
            else:
                self.checks.append(f"⚠ {tool} missing (optional)")
        
        # Check CI
        if (self.base_path / ".github" / "workflows").exists():
            self.checks.append("✓ .github/workflows/ exists")
            score += 1
        else:
            self.checks.append("✗ .github/workflows/ missing")
        
        return score


def main():
    parser = argparse.ArgumentParser(description="Agent-First Project Bootstrap")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # init command
    subparsers.add_parser("init", help="Initialize new project with interview")
    
    # interview command
    subparsers.add_parser("interview", help="Run project interview")
    
    # validate command
    subparsers.add_parser("validate", help="Validate project structure")
    
    # garden command
    subparsers.add_parser("garden", help="Run doc-gardening check")
    
    args = parser.parse_args()
    
    base_path = Path.cwd()
    
    if args.command == "init" or args.command == "interview":
        # Run interview
        interviewer = InterviewConductor()
        config = interviewer.conduct_all()
        
        # Save config
        config_path = base_path / ".agent-bootstrap.json"
        config_path.write_text(json.dumps(asdict(config), indent=2))
        print("💾 Config saved to .agent-bootstrap.json\n")
        
        # Generate artifacts
        print("✨ Generating project structure...\n")
        generator = ArtifactGenerator(config, base_path)
        created = generator.generate_all()
        
        print("Created:")
        for item in created:
            print(f"  {item}")
        
        print("\n🎯 Next steps:")
        print("  1. Review AGENTS.md")
        print("  2. Fill in docs/design/ for each domain")
        print("  3. Run: agent-bootstrap validate")
        print("  4. Start coding with your AI tool!\n")
    
    elif args.command == "validate":
        validator = ProjectValidator(base_path)
        score = validator.validate()
        
        print("\nChecking Agent-First readiness...\n")
        for check in validator.checks:
            print(f"  {check}")
        
        max_score = 8
        print(f"\nScore: {score}/{max_score} - ", end="")
        if score >= max_score - 1:
            print("✅ Ready for Agent-First development!")
        elif score >= max_score // 2:
            print("⚠️ Needs improvement")
        else:
            print("❌ Not ready, run 'agent-bootstrap init'")
        print()
    
    elif args.command == "garden":
        print("\n🌱 Doc-Gardening Check\n")
        print("Checking for stale documentation...")
        print("  [Feature coming soon]")
        print("  Will check:")
        print("    - Stale docs (not updated in 30+ days)")
        print("    - Missing cross-links")
        print("    - Outdated examples")
        print("    - Code/doc drift\n")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()