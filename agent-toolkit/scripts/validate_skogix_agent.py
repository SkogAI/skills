#!/usr/bin/env python3
"""
Validate a Skogix-pattern agent configuration.

Checks for:
- Required frontmatter fields (name, description, color)
- "You are the **[Role]**" identity statement
- Principles section (hard-to-vary, Popperian, KISS)
- Workflow section with Input/Steps/Output
- Quality bar section
- Uncertainty handling statement

Usage:
    validate_skogix_agent.py <path-to-agent.md>

Examples:
    validate_skogix_agent.py ~/.claude/agents/plan-orchestrator.md
    validate_skogix_agent.py ./my-new-agent.md
"""

import re
import sys
from pathlib import Path
import yaml


def validate_agent(file_path: str) -> bool:
    """Validate a Skogix-pattern agent file."""
    path = Path(file_path)

    if not path.exists():
        print(f"❌ Error: {file_path} not found")
        return False

    content = path.read_text()
    errors = []
    warnings = []

    # Check for YAML frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not frontmatter_match:
        errors.append("Missing YAML frontmatter (---)")
        return False

    frontmatter_str, body = frontmatter_match.groups()

    try:
        frontmatter = yaml.safe_load(frontmatter_str)
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML frontmatter: {e}")
        return False

    # Check required fields
    if 'name' not in frontmatter:
        errors.append("Missing required field: 'name'")
    elif not isinstance(frontmatter['name'], str):
        errors.append("Field 'name' must be a string")

    if 'description' not in frontmatter:
        errors.append("Missing required field: 'description'")
    elif not isinstance(frontmatter['description'], str):
        errors.append("Field 'description' must be a string")

    if 'color' not in frontmatter:
        warnings.append("Missing recommended field: 'color'")
    else:
        valid_colors = ['blue', 'cyan', 'green', 'yellow', 'orange', 'red']
        if frontmatter['color'] not in valid_colors:
            warnings.append(f"Color '{frontmatter['color']}' not in recommended set: {valid_colors}")

    # Check Skogix-pattern structure

    # 1. Identity statement
    if not re.search(r'You are the \*\*[\w\s-]+\*\*', body):
        warnings.append("Missing identity statement: 'You are the **[Role]**'")

    # 2. Principles section
    if 'Principles' not in body and 'principles' not in body.lower():
        warnings.append("Missing 'Principles' section (recommended for Skogix pattern)")

    # Check for key philosophical principles
    if 'hard-to-vary' not in body.lower():
        warnings.append("Missing 'hard-to-vary' principle (Deutsch philosophy)")
    if 'popper' not in body.lower() and 'falsif' not in body.lower():
        warnings.append("Missing Popperian falsifiability principle")
    if 'kiss' not in body.lower():
        warnings.append("Missing KISS principle")

    # 3. Workflow/Method section
    has_workflow = any(keyword in body for keyword in ['Workflow', 'workflow', 'Method', 'method', 'Steps', 'steps'])
    if not has_workflow:
        warnings.append("Missing 'Workflow' or 'Method' section")

    # 4. Input/Output specification
    if '**Input' not in body and 'Input:' not in body:
        warnings.append("Missing Input specification in workflow")
    if '**Output' not in body and 'Output:' not in body and 'Deliverable' not in body:
        warnings.append("Missing Output/Deliverable specification")

    # 5. Quality bar or standards
    has_quality = any(keyword in body for keyword in ['Quality', 'quality', 'Checklist', 'checklist', 'Guidelines', 'guidelines'])
    if not has_quality:
        warnings.append("Missing quality standards section")

    # 6. Uncertainty handling
    if 'If' not in body or 'rather than' not in body:
        warnings.append("Missing uncertainty handling guidance (If X, do Y rather than Z pattern)")

    # Print results
    print(f"\n{'='*60}")
    print(f"Validating: {path.name}")
    print(f"{'='*60}\n")

    if frontmatter.get('name'):
        print(f"   Name: {frontmatter['name']}")
    if frontmatter.get('color'):
        print(f"   Color: {frontmatter['color']}")
    if frontmatter.get('description'):
        print(f"   Description: {frontmatter['description'][:60]}...")

    print()

    if errors:
        print("❌ ERRORS:")
        for error in errors:
            print(f"   • {error}")
        return False

    if warnings:
        print("⚠️  WARNINGS (Skogix pattern recommendations):")
        for warning in warnings:
            print(f"   • {warning}")
        print()

    if not errors and not warnings:
        print("✅ Perfect! Agent follows Skogix pattern completely")
    elif not errors:
        print("✅ Valid agent (with minor pattern deviations)")

    return len(errors) == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_skogix_agent.py <path-to-agent.md>")
        print("\nExamples:")
        print("  validate_skogix_agent.py ~/.claude/agents/plan-orchestrator.md")
        print("  validate_skogix_agent.py ./my-new-agent.md")
        sys.exit(1)

    file_path = sys.argv[1]
    success = validate_agent(file_path)
    sys.exit(0 if success else 1)
