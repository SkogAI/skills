#!/usr/bin/env python3
"""
Create a new agent following the Skogix agent pattern.

This script creates agents that follow the philosophical framework:
- Hard-to-vary explanations (Deutsch)
- Popperian falsifiability
- KISS principle
- Evidence-first approach
- Functions ≤ 20 LOC

Usage:
    create_skogix_agent.py <agent-name> [scope]

Examples:
    create_skogix_agent.py data-analyzer user
    create_skogix_agent.py test-orchestrator project
"""

import sys
from pathlib import Path


AGENT_TEMPLATE = '''---
name: {name}
description: {description}
color: {color}
---

You are the **{role}**.

**Principles**

1. **Hard-to-vary explanations** – Every {output_element} must be necessary; remove anything that doesn't reduce error or falsify the outcome.
2. **Popperian falsifiability** – Prefer {action_element} that can obviously succeed or fail.
3. **KISS** – Favor the shortest path that covers edge-cases; avoid cleverness that future readers can't follow.
4. **{domain_principle_name}** – {domain_principle_desc}
5. **{additional_principle_name}** – {additional_principle_desc}

**Workflow**

* **Input**: {input_desc}
* **Steps**:
  1. {step1}
  2. {step2}
  3. {step3}
* **Output**: {output_desc}

**Quality bar**

{quality_bar}

If {uncertainty_condition}, {handling_approach} rather than {anti_pattern}.
'''


def prompt_user(question: str, default: str = "") -> str:
    """Prompt user for input with optional default."""
    if default:
        response = input(f"{question} [{default}]: ").strip()
        return response if response else default
    return input(f"{question}: ").strip()


def create_agent(agent_name: str, scope: str = "user"):
    """
    Create a new agent following the Skogix pattern.

    Args:
        agent_name: Name of the agent (without .md extension)
        scope: 'user' for ~/.claude/agents/ or 'project' for .claude/agents/
    """
    print(f"\n🏭 Creating Skogix-style agent: {agent_name}")
    print("=" * 60)

    # Gather information interactively
    print("\n📝 Agent Identity")
    role = prompt_user("Role name (e.g., 'Planner', 'Executor', 'Critic')")
    description = prompt_user("Description (trigger + what it does)")

    print("\n🎨 Visual")
    print("Available colors: blue, cyan, green, yellow, orange, red")
    color = prompt_user("Color", "blue")

    print("\n⚙️  Workflow Details")
    output_element = prompt_user("Output element type (e.g., 'step', 'claim', 'function')", "output")
    action_element = prompt_user("Action element type (e.g., 'steps', 'queries', 'operations')", "actions")

    print("\n📚 Domain-Specific Principles")
    domain_principle_name = prompt_user("Domain principle name (e.g., 'Single-Responsibility')")
    domain_principle_desc = prompt_user("Domain principle description")
    additional_principle_name = prompt_user("Additional principle name (optional)", "")
    additional_principle_desc = prompt_user("Additional principle description (optional)", "")

    print("\n🔄 Workflow")
    input_desc = prompt_user("Input description (what agent receives)")
    step1 = prompt_user("Step 1")
    step2 = prompt_user("Step 2")
    step3 = prompt_user("Step 3")
    output_desc = prompt_user("Output description (what agent produces)")

    print("\n✅ Quality Standards")
    quality_bar = prompt_user("Quality bar (standards, tone, escalation criteria)")
    uncertainty_condition = prompt_user("Uncertainty condition (e.g., 'evidence is missing')")
    handling_approach = prompt_user("How to handle uncertainty (e.g., 'ask Researcher')")
    anti_pattern = prompt_user("Anti-pattern to avoid (e.g., 'guessing', 'improvising')")

    # Fill template
    agent_content = AGENT_TEMPLATE.format(
        name=agent_name,
        description=description,
        color=color,
        role=role,
        output_element=output_element,
        action_element=action_element,
        domain_principle_name=domain_principle_name,
        domain_principle_desc=domain_principle_desc,
        additional_principle_name=additional_principle_name or "Efficiency",
        additional_principle_desc=additional_principle_desc or "Optimize for clarity and performance.",
        input_desc=input_desc,
        step1=step1,
        step2=step2,
        step3=step3,
        output_desc=output_desc,
        quality_bar=quality_bar,
        uncertainty_condition=uncertainty_condition,
        handling_approach=handling_approach,
        anti_pattern=anti_pattern
    )

    # Determine target directory
    if scope == "user":
        target_dir = Path.home() / ".claude" / "agents"
    elif scope == "project":
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

    # Create directory if needed
    target_dir.mkdir(parents=True, exist_ok=True)

    # Write agent file
    agent_file = target_dir / f"{agent_name}.md"
    agent_file.write_text(agent_content)

    print("\n" + "=" * 60)
    print(f"✅ Created agent: {agent_file}")
    print(f"   Role: {role}")
    print(f"   Scope: {scope}")
    print(f"   Color: {color}")
    print("\n📋 Next steps:")
    print(f"   1. Review and refine: {agent_file}")
    print(f"   2. Validate: python3 scripts/validate_agent.py {agent_file}")
    print(f"   3. Test by @-mentioning @{agent_name} in Claude Code")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: create_skogix_agent.py <agent-name> [user|project]")
        print("\nExamples:")
        print("  create_skogix_agent.py data-analyzer user")
        print("  create_skogix_agent.py test-orchestrator project")
        sys.exit(1)

    agent_name = sys.argv[1].replace(".md", "")
    scope = sys.argv[2] if len(sys.argv) > 2 else "user"

    create_agent(agent_name, scope)
