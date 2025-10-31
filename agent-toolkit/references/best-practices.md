# Agent Management Best Practices

## Subagent vs Built-in Task Agents

**Custom Subagents**:
- Defined in .md files with YAML frontmatter
- Project-level (`.claude/agents/`) or user-level (`~/.claude/agents/`)
- Can specify tools, model, color
- Invoked automatically, explicitly, or via @-mention
- Separate context window from main conversation

**Built-in Task Agents**:
- Provided by Claude Code (general-purpose, Explore, etc.)
- Cannot be modified
- Invoked via Task tool
- Different capabilities and scope

## When to Create vs Use Existing

**Create new custom subagent when**:
- Repeatedly performing same specialized analysis
- Need domain-specific knowledge not in existing agents
- Workflow requires specific tool combinations
- Want to capture and reuse investigation patterns

**Use existing agents when**:
- Task matches existing agent description
- Want proven, tested workflows
- Collaborating with team using same agents

## Agent Scope: User vs Project

**User-level** (`~/.claude/agents/`):
- Personal agents across all projects
- Highest priority (overrides project agents with same name)
- For individual workflow preferences
- Examples: personal code review standards, preferred documentation style

**Project-level** (`.claude/agents/`):
- Shared with team via git
- Project-specific conventions
- Lower priority than user-level
- Examples: project code reviewer, architecture documenter

## Frontmatter Fields

**Required**:
- `name`: Lowercase with hyphens (e.g., `code-explorer`)
- `description`: Natural language, third-person (e.g., "This agent should be used when...")

**Optional**:
- `tools`: Comma-separated list (omit to inherit all tools)
- `model`: `sonnet`, `opus`, `haiku`, or `inherit`
- `color`: Visual identifier in UI

## Tool Restrictions

**Limiting tools** (via `tools:` field):
- Prevents agent from accessing unnecessary tools
- Reduces context size
- Makes behavior more predictable
- Example: Analysis agents don't need Write/Edit tools

**Inheriting all tools** (omit `tools:` field):
- Agent can use any available tool
- More flexible but larger context
- Use for agents that need varied operations

## Model Selection

**opus**: Deep analysis, critical reviews, quality-focused work
**sonnet**: Balanced performance, general coding and analysis
**haiku**: Fast exploration, context building
**inherit**: Use same model as parent conversation

## Activation Workflow

1. **Validate**: Check YAML frontmatter and structure
2. **Test**: Run locally with @-mention before sharing
3. **Activate**: Move to appropriate directory (user vs project)
4. **Document**: Update team docs if project-level
5. **Iterate**: Refine based on actual usage

## Common Pitfalls

❌ **Overly broad descriptions**: "Helps with code"
✅ **Specific triggers**: "Analyzes authentication flows by tracing from entry points to data storage"

❌ **Second person**: "You should review code..."
✅ **Third person**: "This agent should be used when reviewing code..."

❌ **No tool restrictions**: Everything gets all tools
✅ **Thoughtful limits**: Analysis agents don't need Edit/Write

❌ **Duplicate functionality**: Multiple similar agents
✅ **Clear separation**: Each agent has distinct purpose

❌ **Too many agents**: Decision paralysis
✅ **Focused set**: 5-10 well-defined agents cover most needs

## Maintenance

**Regular review**:
- Are agents still used?
- Do descriptions accurately reflect behavior?
- Are there new patterns that should become agents?

**Version control**:
- Project agents should be in git
- Document changes in commit messages
- Consider agent versioning for major changes

**Team coordination**:
- Document available agents
- Share agent catalog with team
- Agree on naming conventions
- Review new agents before merging
