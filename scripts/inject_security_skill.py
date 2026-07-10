import os

import os
base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "collection", "agents")
agents = os.listdir(base)
skill_line = "- **security-guardrails:** Prevent exposure of sensitive credentials, API keys, passwords, and database access information\n"

updated = []
skipped = []

for agent in sorted(agents):
    agent_md = os.path.join(base, agent, "AGENT.md")
    if not os.path.exists(agent_md):
        skipped.append(agent)
        continue
    with open(agent_md, "r") as f:
        content = f.read()
    if "security-guardrails" in content:
        skipped.append(f"{agent} (already has it)")
        continue
    if "## System Prompt" in content:
        content = content.replace(
            "## System Prompt", skill_line + "\n## System Prompt", 1
        )
        with open(agent_md, "w") as f:
            f.write(content)
        updated.append(agent)
    else:
        skipped.append(f"{agent} (no System Prompt section)")

print("Updated:", updated)
print("Skipped:", skipped)
