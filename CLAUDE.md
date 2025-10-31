# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is the Anthropic Skills repository containing example skills that demonstrate Claude's skills system. Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. The repository includes both open-source example skills and source-available document skills (docx, pdf, pptx, xlsx).

## Key Concepts

### Skill Structure

Every skill must contain a `SKILL.md` file with:
- **YAML frontmatter** with required fields: `name` (hyphen-case) and `description` (when to use it)
- **Optional fields**: `license`, `allowed-tools`, `metadata`
- **Markdown body** with instructions Claude follows when the skill is active

Skills use progressive disclosure:
1. Metadata (name + description) - always in context
2. SKILL.md body - loaded when skill triggers
3. Bundled resources - loaded as needed

### Directory Organization

```
skill-name/
├── SKILL.md          # Required: frontmatter + instructions
├── scripts/          # Optional: executable Python/Bash for deterministic tasks
├── references/       # Optional: documentation loaded into context as needed
└── assets/           # Optional: templates, fonts, images used in output
```

## Development Commands

### Skills Management

**Initialize new skill:**
```bash
python3 skill-creator/scripts/init_skill.py <skill-name> --path <output-directory>
```

**Validate skill structure:**
```bash
python3 skill-creator/scripts/quick_validate.py <path-to-skill-directory>
```

**Package skill for distribution:**
```bash
python3 skill-creator/scripts/package_skill.py <path-to-skill-folder> [output-directory]
```
Note: Packaging automatically validates before creating the zip file.

### Agent Management

**Activate agent (copy to active directory):**
```bash
python3 agent-toolkit/scripts/activate_agent.py <agent-name> <source-dir> [user|project]
```
- `user` scope: copies to `~/.claude/agents/`
- `project` scope: copies to `.claude/agents/`

**Validate agent configuration:**
```bash
python3 agent-toolkit/scripts/validate_agent.py <path-to-agent.md>
```

### Command Management

**Create new command:**
```bash
python3 command-toolkit/scripts/create_command.py <command-name> [user|project]
```

**Validate command structure:**
```bash
python3 command-toolkit/scripts/validate_command.py <path-to-command.md>
```

### MCP Server Tools

**Test MCP connections:**
```bash
python3 mcp-builder/scripts/connections.py
```

**Evaluate MCP server implementation:**
```bash
python3 mcp-builder/scripts/evaluation.py <path-to-server>
```

## Architecture Patterns

### Skills vs Agents vs Commands

**Use Skills when:**
- Providing domain-specific knowledge and workflows
- Bundling scripts, references, and assets
- Task requires progressive disclosure of information
- Creating reusable knowledge packages for teams

**Use Agents when:**
- Task requires specialized reasoning or expertise
- Multi-turn conversation or iterative refinement needed
- Complex analysis requiring deep understanding
- Review tasks with nuanced judgment

**Use Commands when:**
- Automating repetitive, well-defined tasks
- Creating project-specific workflows
- Task requires immediate execution with clear inputs/outputs
- Generating code from templates

### Bundled Resources Strategy

**scripts/** - For code that would otherwise be rewritten repeatedly:
- Token efficient and deterministic
- May be executed without loading into context
- Examples: PDF rotation, form filling, image conversion

**references/** - For documentation Claude should reference:
- Keeps SKILL.md lean
- Loaded only when Claude determines it's needed
- Examples: API docs, schemas, policies, detailed workflow guides
- For large files (>10k words), include grep patterns in SKILL.md

**assets/** - For files used in output, not loaded into context:
- Templates, images, fonts, boilerplate code
- Examples: brand logos, PowerPoint templates, HTML boilerplate

### Writing Style for Skills

- Use **imperative/infinitive form** (verb-first), not second person
- Write objectively: "To accomplish X, do Y" not "You should do X"
- Description in frontmatter should be third-person and trigger-focused
- Avoid duplication between SKILL.md and references/ files

## Testing

When working with skills that include Python scripts:
- Test scripts in isolation before bundling
- Verify dependencies are documented
- Check script execution permissions
- Validate error handling for missing dependencies

## Git Workflow

The repository uses standard git commands. The git status at conversation start shows deleted files from removed example skills (algorithmic-art, artifacts-builder, brand-guidelines, etc.) and untracked agent-toolkit/ and command-toolkit/ directories.

When committing new or modified skills:
- Ensure SKILL.md frontmatter is complete and valid
- Test all bundled scripts before commit
- Update marketplace.json if adding skills to a plugin collection
- Follow repository's existing skill organization patterns

## Important Files

- **agent_skills_spec.md** - Official spec defining skill format (v1.0)
- **.claude-plugin/marketplace.json** - Plugin marketplace configuration
- **template-skill/** - Minimal template for creating new skills
- **skill-creator/** - Meta skill for creating other skills
- **agent-toolkit/** - Tools for managing custom subagents
- **command-toolkit/** - Tools for managing slash commands
- **document-skills/** - Production skills for docx/pdf/pptx/xlsx (source-available)

## Marketplace Structure

The `.claude-plugin/marketplace.json` defines two plugin collections:
1. **document-skills** - Excel, Word, PowerPoint, PDF capabilities
2. **example-skills** - Various example skills (skill-creator, mcp-builder, canvas-design, etc.)

When adding skills to marketplace, update the appropriate plugin's `skills` array.
