#!/usr/bin/env python3
"""
Validate a custom subagent's YAML frontmatter and structure.
"""
import sys
import re
from pathlib import Path

def validate_agent(agent_path: str):
    """
    Validate agent file structure and frontmatter.

    Args:
        agent_path: Path to the agent .md file
    """
    path = Path(agent_path)

    if not path.exists():
        print(f"❌ Error: {path} not found")
        return False

    content = path.read_text()

    # Check for frontmatter
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(frontmatter_pattern, content, re.DOTALL)

    if not match:
        print(f"❌ Error: No YAML frontmatter found")
        print("   Frontmatter must start and end with '---'")
        return False

    frontmatter = match.group(1)

    # Required fields
    required_fields = {
        'name': r'name:\s*(.+)',
        'description': r'description:\s*(.+)'
    }

    errors = []
    warnings = []

    for field, pattern in required_fields.items():
        if not re.search(pattern, frontmatter):
            errors.append(f"Missing required field: {field}")

    # Optional fields
    optional_fields = {
        'tools': r'tools:\s*(.+)',
        'model': r'model:\s*(sonnet|opus|haiku|inherit)',
        'color': r'color:\s*(.+)'
    }

    found_optional = {}
    for field, pattern in optional_fields.items():
        match = re.search(pattern, frontmatter)
        if match:
            found_optional[field] = match.group(1).strip()

    # Validate model if present
    if 'model' in found_optional:
        valid_models = ['sonnet', 'opus', 'haiku', 'inherit']
        if found_optional['model'] not in valid_models:
            warnings.append(f"Model '{found_optional['model']}' not in {valid_models}")

    # Check for content after frontmatter
    content_after = content[match.end():]
    if not content_after.strip():
        errors.append("No content after frontmatter")

    # Report results
    if errors:
        print(f"❌ Validation failed for {path.name}:")
        for error in errors:
            print(f"   • {error}")
        return False

    print(f"✅ {path.name} is valid")

    # Extract name
    name_match = re.search(required_fields['name'], frontmatter)
    if name_match:
        print(f"   Name: {name_match.group(1).strip()}")

    # Show optional fields
    if found_optional:
        for field, value in found_optional.items():
            print(f"   {field.title()}: {value}")

    if warnings:
        print("   Warnings:")
        for warning in warnings:
            print(f"   • {warning}")

    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_agent.py <agent-file.md>")
        sys.exit(1)

    agent_path = sys.argv[1]
    success = validate_agent(agent_path)
    sys.exit(0 if success else 1)
