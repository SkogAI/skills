# Skogix Agent System

## Overview

The Skogix agent system is a workflow-based AI agent architecture grounded in epistemological principles from Karl Popper and David Deutsch. It emphasizes hard-to-vary explanations, falsifiability, and empirical rigor.

## Philosophical Foundation

### Core Principles

1. **Hard-to-Vary Explanations (Deutsch)**
   - Every output element must be necessary
   - Remove anything that doesn't reduce error or falsify the outcome
   - If content can change without altering meaning, delete or tighten it

2. **Popperian Falsifiability**
   - Prefer actions/steps that can obviously succeed or fail
   - Design for clear success/failure states
   - Treat failures as opportunities for error-correction

3. **KISS (Keep It Simple, Stupid)**
   - Favor the shortest path that covers edge-cases
   - Avoid cleverness that future readers can't follow
   - Functions ≤ 20 lines of code

4. **Evidence-First**
   - No guessing or improvisation
   - All claims must have checkable citations
   - When uncertain, ask/escalate rather than assume

## Agent Workflow System

The Skogix system implements a complete workflow pipeline:

```
┌──────────────────────┐
│ plan-orchestrator    │  Breaks goals into falsifiable sub-tasks
│     (Planner)        │  Delegates to specialist agents
└──────────┬───────────┘
           │
           ├─────────────┬──────────────┬───────────────┐
           ▼             ▼              ▼               ▼
  ┌────────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
  │ evidence-      │ │ tool-runner │ │ code-writer │ │  [other     │
  │ gatherer       │ │ (Executor)  │ │             │ │  agents]    │
  │ (Researcher)   │ └─────────────┘ └─────────────┘ └─────────────┘
  └────────┬───────┘
           │
           │  Feeds evidence to ↓
           │
  ┌────────▼────────────────────────┐
  │ answer-writer (Synthesizer)     │  Weaves evidence into narrative
  │        OR                        │
  │ documentation-writer            │  Creates formal documentation
  └────────┬────────────────────────┘
           │
           │  Reviewed by ↓
           │
  ┌────────▼─────────┐
  │ quality-guard    │  Vetoes if violations occur
  │   (Critic)       │  Checks explanation integrity
  └──────────────────┘
```

## Agent Roles

### plan-orchestrator (Planner)
- **Color**: Red
- **Purpose**: Break high-level goals into lean sub-task sequences
- **Output**: Numbered list with step_id, agent, and goal
- **Principle**: Hard-to-vary plans - every step must explain why it's needed

### evidence-gatherer (Researcher)
- **Color**: Blue
- **Purpose**: Gather minimal, sufficient facts for hard-to-vary answers
- **Output**: JSON blocks with source, snippet, why_relevant
- **Principle**: No statement without checkable citation

### tool-runner (Executor)
- **Color**: Yellow
- **Purpose**: Execute discrete actions (code, CLI, API calls)
- **Output**: Code block + terse success/fail log
- **Principle**: Single-Responsibility + YAGNI filter

### code-writer (Code Writer)
- **Color**: Cyan
- **Purpose**: Draft minimal code that solves assigned sub-task
- **Output**: Code files with inline usage examples (doctests)
- **Principle**: Functions ≤ 20 LOC, one screenful

### answer-writer (Synthesizer)
- **Color**: Green
- **Purpose**: Weave evidence into single-voice deliverable
- **Output**: Markdown with opening claim, evidence-linked body, open problems
- **Principle**: Hard-to-vary narrative - remove sentences that don't reduce error

### quality-guard (Critic)
- **Color**: Orange
- **Purpose**: Inspect drafts for violations of accuracy, hygiene, hard-to-vary
- **Output**: APPROVED or REJECTED with diff-style fixes
- **Principle**: Ruthless constructive criticism

### documentation-writer (Documentation-Writer)
- **Color**: Cyan
- **Purpose**: Create formal release documentation
- **Output**: Markdown following docs-as-code standards
- **Principle**: Evidence-first, structured authoring, change safety

## Agent Structure Template

```markdown
---
name: agent-name
description: [Trigger condition]. [What it does].
color: blue  # blue, cyan, green, yellow, orange, red
---

You are the **[Role Name]**.

**Principles**

1. **Hard-to-vary explanations** – Every [element] must be necessary...
2. **Popperian falsifiability** – Prefer [actions] that can obviously succeed or fail.
3. **KISS** – Favor shortest path that covers edge-cases...
4. **[Domain-specific]** – [Specific to this role]
5. **[Additional]** – [Extra guidance]

**Workflow**

* **Input**: [What agent receives]
* **Steps**:
  1. [First step]
  2. [Second step]
  3. [Third step]
* **Output**: [What agent produces]

**Quality bar**

[Standards, tone, escalation criteria]

If [uncertain condition], [handling] rather than [anti-pattern].
```

## Creating New Agents

### Using the Factory Script

```bash
python3 agent-toolkit/scripts/create_skogix_agent.py <agent-name> [user|project]
```

Interactive prompts will guide you through:
- Role definition
- Trigger description
- Visual color
- Domain principles
- Workflow steps
- Quality standards
- Uncertainty handling

### Validation

```bash
python3 agent-toolkit/scripts/validate_skogix_agent.py <path-to-agent.md>
```

Checks for:
- ✅ Required frontmatter (name, description, color)
- ✅ Identity statement ("You are the **Role**")
- ✅ Philosophical principles (hard-to-vary, Popper, KISS)
- ✅ Workflow structure (Input/Steps/Output)
- ✅ Quality standards
- ✅ Uncertainty handling pattern

## Best Practices

### Agent Design

1. **Single clear purpose** - Each agent should have one well-defined role
2. **Explicit delegation** - Planner orchestrates, specialists execute
3. **No improvisation** - Agents ask/escalate when uncertain
4. **Falsifiable outputs** - Results should obviously succeed or fail

### Workflow Integration

1. **Plan first** - Always start with plan-orchestrator
2. **Evidence before synthesis** - Gather facts before writing
3. **Review after creation** - quality-guard vets all deliverables
4. **Iterate on criticism** - Treat vetos as error-correction opportunities

### Anti-Patterns to Avoid

❌ **Agents guessing** - Should ask rather than assume
❌ **Unfalsifiable claims** - Every statement needs checkable evidence
❌ **Clever complexity** - KISS over cleverness
❌ **Long functions** - Functions >20 LOC should be split
❌ **Vague principles** - Every guideline must be actionable

## Extending the System

### Adding New Agent Types

When the existing workflow doesn't cover a need:

1. **Identify the gap** - What specific task lacks a specialist?
2. **Define the role** - Clear trigger condition and deliverable
3. **Ground in principles** - How do Popper/Deutsch/KISS apply?
4. **Specify workflow** - Input, steps, output format
5. **Create using factory** - `create_skogix_agent.py`
6. **Validate** - `validate_skogix_agent.py`
7. **Test with @-mention** - Try it before deploying to team

### Integration with External Systems

Agents can integrate with:
- **File systems** - Read/write project files
- **APIs** - Call external services (with evidence-gathering)
- **Build tools** - Execute linters, tests, compilers
- **Documentation** - Generate docs-as-code artifacts
- **Version control** - Create commits, branches, PRs

## Maintenance

### Regular Review

- **Quarterly**: Review all agents for relevance
- **On pattern change**: Update factory and template
- **After major projects**: Extract reusable agent patterns

### Version Control

- Commit project agents to `.claude/agents/`
- Document in project README
- Review agent changes like code changes
- Tag agent versions alongside software releases

### Team Coordination

- Shared agents in project scope (`.claude/agents/`)
- Personal variations in user scope (`~/.claude/agents/`)
- Document agent purpose and usage
- Maintain consistency across team

## References

- **Karl Popper** - Falsifiability, error-correction, critical rationalism
- **David Deutsch** - Hard-to-vary explanations, good explanations grow knowledge
- **Clean Code** - Functions ≤20 LOC, single responsibility
- **Docs-as-Code** - Structured authoring, evidence-based documentation
- **AutoGen** - Multi-agent workflows, maker-checker patterns

## Quick Reference

```bash
# Create new agent
python3 agent-toolkit/scripts/create_skogix_agent.py data-analyzer user

# Validate agent
python3 agent-toolkit/scripts/validate_skogix_agent.py ~/.claude/agents/data-analyzer.md

# Test agent
# In Claude Code: @data-analyzer <task>

# List all agents
ls ~/.claude/agents/          # User scope
ls .claude/agents/            # Project scope
```
