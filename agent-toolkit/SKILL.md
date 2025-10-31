---
name: agent-toolkit
description: This skill should be used when managing custom subagents in Claude Code. It provides tools for activating agents from source directories, validating agent configurations, understanding available agents, and creating new agents. Use this skill when working with the .claude/agents/ system, organizing specialized workflows, or building custom agent capabilities.
---

# Agent Toolkit

## Overview

Comprehensive toolkit for managing custom subagents in Claude Code, including activation, validation, documentation, and creation workflows. This skill enables effective use of the subagent system to extend Claude's capabilities with specialized, reusable workflows.

## When to Use This Skill

Activate this skill when:
- Activating agents from source directories (like `todo/`) to active agent directories
- Validating agent YAML frontmatter and structure before activation
- Understanding which agent to use for specific tasks
- Creating new custom agents for specialized workflows
- Setting up agent directories for projects or personal use
- Troubleshooting agent configuration issues

## Core Workflows

### 1. Activating Existing Agents

To activate an agent from a source directory:

```bash
python3 scripts/activate_agent.py <agent-name> <source-dir> [scope]
```

**Parameters**:
- `agent-name`: Agent filename (with or without .md extension)
- `source-dir`: Directory containing the agent file
- `scope`: `user` (default, activates to ~/.claude/agents/) or `project` (activates to .claude/agents/)

**Examples**:
```bash
# Activate code-reviewer to user agents
python3 scripts/activate_agent.py code-reviewer ./todo user

# Activate code-architect to project agents
python3 scripts/activate_agent.py code-architect.md ./todo project
```

### 2. Validating Agent Configuration

Before activating an agent, validate its structure:

```bash
python3 scripts/validate_agent.py <path-to-agent.md>
```

**Validation checks**:
- YAML frontmatter presence and format
- Required fields (name, description)
- Optional field validity (model, tools, color)
- Content after frontmatter exists

**Example**:
```bash
python3 scripts/validate_agent.py ./todo/code-reviewer.md
```

### 3. Understanding Available Agents

Reference `references/agent-catalog.md` to understand the 7 existing custom subagents:

- **code-explorer**: Deep codebase feature analysis
- **code-architect**: Feature design from existing patterns
- **code-reviewer**: Code review against CLAUDE.md (high-confidence only)
- **code-simplifier**: Post-coding clarity improvements
- **silent-failure-hunter**: Error handling audits
- **type-design-analyzer**: Type invariant and encapsulation review
- **code-flow-mapper**: Execution path tracing with reports

**Agent Selection Process**:
1. Identify the primary task goal
2. Check agent catalog for matching capabilities
3. Consider agent combinations for complex workflows
4. Prefer specialized agents over general-purpose for domain-specific work

### 4. Creating New Agents

#### Standard Agent Creation (Generic)

To create a new custom agent using the generic template:

1. **Copy template**:
   ```bash
   cp assets/agent-template.md <new-agent-name>.md
   ```

2. **Edit frontmatter**:
   - Set unique `name` (lowercase with hyphens)
   - Write specific `description` (third-person, trigger-focused)
   - Specify `tools` if restricting (or omit for all tools)
   - Choose `model`: sonnet (balanced), opus (quality), haiku (fast), inherit
   - Pick `color` for UI identification

3. **Fill in content**:
   - Define core mission clearly
   - List specific usage scenarios
   - Document step-by-step approach
   - Specify output format requirements
   - Include key principles and examples

4. **Validate**:
   ```bash
   python3 scripts/validate_agent.py <new-agent-name>.md
   ```

5. **Activate**:
   ```bash
   python3 scripts/activate_agent.py <new-agent-name> . user
   ```

#### Skogix Agent Factory (Philosophical Pattern)

For agents following the Skogix philosophical framework (hard-to-vary, Popperian, KISS):

1. **Create using factory script**:
   ```bash
   python3 scripts/create_skogix_agent.py <agent-name> [user|project]
   ```

   The script interactively prompts for:
   - Role name (Planner, Executor, Critic, etc.)
   - Trigger description
   - Color for visual identification
   - Domain-specific principles
   - Workflow (input/steps/output)
   - Quality standards
   - Uncertainty handling

2. **Validate Skogix pattern**:
   ```bash
   python3 scripts/validate_skogix_agent.py <path-to-agent.md>
   ```

   Checks for:
   - Identity statement ("You are the **Role**")
   - Philosophical principles (hard-to-vary, Popperian, KISS)
   - Workflow structure (Input/Steps/Output)
   - Quality bar
   - Uncertainty handling ("If X, do Y rather than Z")

3. **Reference documentation**:
   See `references/skogix-agent-system.md` for complete philosophy, patterns, and examples

**When to use Skogix factory**:
- Building agents for evidence-based workflows
- Need rigorous quality standards
- Agents that delegate to each other (Planner → Executor → Critic)
- Systems requiring falsifiable outputs and error-correction

## Best Practices

Consult `references/best-practices.md` for comprehensive guidance on:

- **Scope decisions**: When to use user-level vs project-level agents
- **Tool restrictions**: Limiting tools for focused agents
- **Model selection**: Choosing appropriate model for agent workload
- **Maintenance**: Keeping agents updated and relevant
- **Team coordination**: Sharing and documenting project agents

**Key principles**:
- Use specific, trigger-focused descriptions (not broad or vague)
- Write in third-person (not second-person)
- Apply thoughtful tool restrictions (analysis agents don't need Write/Edit)
- Maintain 5-10 focused agents (not dozens of similar ones)
- Test with @-mention before team-wide activation

## Integration with Development Workflows

### Typical Feature Development Flow

1. **Understanding**: Use `@code-explorer` to analyze existing patterns
2. **Design**: Use `@code-architect` for implementation blueprint
3. **Implementation**: Write code following blueprint
4. **Refinement**: Use `@code-simplifier` for clarity
5. **Quality**: Use `@code-reviewer` before commit

### Error Handling Review Flow

1. **Audit**: Use `@silent-failure-hunter` on changes
2. **Fix**: Address identified issues
3. **Validate**: Use `@code-reviewer` to confirm fixes

### Type System Design Flow

1. **Analysis**: Use `@type-design-analyzer` on new types
2. **Refine**: Implement recommendations
3. **Review**: Use `@code-reviewer` for final check

## Quick Reference

### Generic Agents

```bash
# Validate before activating
python3 scripts/validate_agent.py ./todo/code-reviewer.md

# Activate to user directory
python3 scripts/activate_agent.py code-reviewer ./todo user

# Activate to project directory
python3 scripts/activate_agent.py code-architect ./todo project

# Create new agent from template
cp assets/agent-template.md my-new-agent.md
# Edit my-new-agent.md
python3 scripts/validate_agent.py my-new-agent.md
python3 scripts/activate_agent.py my-new-agent . user
```

### Skogix Pattern Agents

```bash
# Create Skogix agent (interactive)
python3 scripts/create_skogix_agent.py data-analyzer user

# Validate Skogix pattern
python3 scripts/validate_skogix_agent.py ~/.claude/agents/plan-orchestrator.md

# Check existing agents for pattern compliance
python3 scripts/validate_skogix_agent.py ~/.claude/agents/*.md

# Reference full documentation
cat references/skogix-agent-system.md
```

## Resources

### scripts/
- `activate_agent.py` - Activate agents from source to user/project directories
- `validate_agent.py` - Validate YAML frontmatter and structure (generic)
- `create_skogix_agent.py` - Interactive factory for Skogix-pattern agents
- `validate_skogix_agent.py` - Validate Skogix philosophical pattern compliance

### references/
- `agent-catalog.md` - Complete documentation of 7 existing custom agents
- `best-practices.md` - Comprehensive agent management guidance
- `skogix-agent-system.md` - Complete Skogix philosophy, workflow, and patterns

### assets/
- `agent-template.md` - Generic boilerplate template for creating new agents
- `skogix-agent-template.md` - Template following Skogix philosophical pattern
