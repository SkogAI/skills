#!/usr/bin/env python3
"""
Activate a custom subagent by moving it to the active agent directory.
"""
import sys
import shutil
from pathlib import Path

def activate_agent(agent_name: str, source_dir: str, scope: str = "user"):
    """
    Activate an agent by copying it to the appropriate directory.

    Args:
        agent_name: Name of the agent file (with or without .md)
        source_dir: Directory containing the agent file
        scope: 'user' for ~/.claude/agents/ or 'project' for .claude/agents/
    """
    # Ensure .md extension
    if not agent_name.endswith('.md'):
        agent_name = f"{agent_name}.md"

    source = Path(source_dir) / agent_name

    if not source.exists():
        print(f"❌ Error: {source} not found")
        sys.exit(1)

    # Determine target directory
    if scope == "user":
        target_dir = Path.home() / ".claude" / "agents"
    elif scope == "project":
        # Find project root (directory with .claude/)
        current = Path.cwd()
        while current != current.parent:
            if (current / ".claude").exists():
                target_dir = current / ".claude" / "agents"
                break
            current = current.parent
        else:
            print("❌ Error: No .claude/ directory found in project hierarchy")
            sys.exit(1)
    else:
        print(f"❌ Error: Invalid scope '{scope}'. Use 'user' or 'project'")
        sys.exit(1)

    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)

    target = target_dir / agent_name

    # Copy the agent
    shutil.copy2(source, target)
    print(f"✅ Activated {agent_name}")
    print(f"   Source: {source}")
    print(f"   Target: {target}")
    print(f"   Scope: {scope}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: activate_agent.py <agent-name> <source-dir> [scope]")
        print("  scope: 'user' (default) or 'project'")
        sys.exit(1)

    agent_name = sys.argv[1]
    source_dir = sys.argv[2]
    scope = sys.argv[3] if len(sys.argv) > 3 else "user"

    activate_agent(agent_name, source_dir, scope)
