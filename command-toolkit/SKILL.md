---
name: command-toolkit
description: This skill should be used when managing custom slash commands in Claude Code. It provides tools for creating commands, validating command structure, understanding when to use commands vs agents vs skills, and managing command organization. Use when creating workflows, automation commands, or project-specific command utilities.
---

# Command Toolkit

## Overview

Comprehensive toolkit for managing custom slash commands in Claude Code, including creation, validation, organization, and best practices. This skill enables effective use of the command system to create reusable workflows and task automation.

## When to Use This Skill

Activate this skill when:
- Creating new slash commands for common workflows or automation
- Validating command Markdown structure before deployment
- Understanding command argument handling and $ARGUMENTS placeholder
- Deciding between commands, agents, and skills for a task
- Managing project-level vs user-level commands
- Setting up command directories for projects or teams
- Troubleshooting command issues or improving existing commands

## Commands vs Agents vs Skills

### Use Commands When:
- Automating repetitive, well-defined tasks
- Creating project-specific workflows
- Generating code from templates (components, tests, configs)
- Running analysis or audits with consistent output
- Building deployment or build automation
- Task requires immediate execution with clear inputs/outputs

**Examples**: Generate component, run security audit, optimize images, create API endpoint

### Use Agents When:
- Task requires specialized reasoning or expertise
- Multi-turn conversation or iterative refinement needed
- Complex analysis requiring deep understanding
- Review or advisory tasks with nuanced judgment
- Task benefits from focused tool restrictions

**Examples**: Code review, architecture design, debugging assistance, refactoring guidance

### Use Skills When:
- Providing domain-specific knowledge to Claude
- Bundling scripts, references, and assets for complex workflows
- Extending Claude's capabilities with specialized tools
- Creating reusable knowledge packages for teams
- Task requires progressive disclosure of information

**Examples**: PDF manipulation, BigQuery integration, brand guidelines, document workflows

### Decision Tree

```
Need specialized reasoning? → Use Agent
Need reusable knowledge + tools? → Use Skill
Need workflow automation? → Use Command
```

## Core Workflows

### 1. Creating New Commands

Use the `create_command.py` script to generate a new command from template:

```bash
python3 scripts/create_command.py <command-name> [scope]
```

**Parameters**:
- `command-name`: Command filename (kebab-case, without .md)
- `scope`: `user` (default, creates in ~/.claude/commands/) or `project` (creates in .claude/commands/)

**Examples**:
```bash
# Create user-level command
python3 scripts/create_command.py optimize-images user

# Create project-level command
python3 scripts/create_command.py generate-component project
```

**Interactive prompts**:
The script will ask for:
1. **Command title** (display name)
2. **Command description** (what it does)
3. **Command category** (generation, analysis, build, workflow)
4. **Arguments expected** (file paths, options, etc.)

### 2. Command Structure

All commands follow this Markdown format:

```markdown
# Command Title

Brief description of what the command does and its primary use case.

## Task

I'll [action description] for $ARGUMENTS following [relevant standards/practices].

## Process

I'll follow these steps:

1. [Step 1 description]
2. [Step 2 description]
3. [Step 3 description]
4. [Final step description]

## [Category-specific sections]

### [Feature Category]

- [Feature 1]
- [Feature 2]
- [Feature 3]

## Best Practices

### [Practice Category]

- [Best practice 1]
- [Best practice 2]
- [Best practice 3]

I'll adapt to your project's [tools/framework] and follow established patterns.
```

**Critical elements**:
- Use `$ARGUMENTS` placeholder where user input goes
- Start with clear task statement
- Include step-by-step process
- Add category-specific guidance
- End with adaptation statement

### 3. Validating Commands

Before activating a command, validate its structure:

```bash
python3 scripts/validate_command.py <path-to-command.md>
```

**Validation checks**:
- File is valid Markdown
- Contains $ARGUMENTS placeholder
- Has proper heading structure
- Includes Task and Process sections
- Has clear, actionable steps
- Follows naming conventions

**Example**:
```bash
python3 scripts/validate_command.py ~/.claude/commands/optimize-images.md
```

### 4. Command Naming Conventions

**File naming**:
- Use kebab-case: `optimize-images.md`
- Be descriptive and action-oriented: `generate-component.md`
- Include target type: `analyze-security.md`
- Avoid generic names: `build.md` → `build-production.md`

**Command titles** (in Markdown):
- Use clear, imperative verbs: "Generate Component"
- Include target and action: "Optimize Bundle Size"
- Keep concise but descriptive: "Security Analyzer"

### 5. Argument Handling

Commands use the `$ARGUMENTS` placeholder for user input:

**Single argument**:
```markdown
Optimize images in $ARGUMENTS for web performance.
```
Usage: `/optimize-images src/assets/`

**Multiple arguments** (space-separated):
```markdown
Generate a $ARGUMENTS component with proper structure.
```
Usage: `/generate-component UserProfile dashboard`

**Best practices**:
- Validate arguments in Process section
- Handle missing or invalid arguments gracefully
- Document expected argument format
- Provide usage examples

### 6. Command Categories

Reference `references/command-catalog.md` for detailed examples in each category:

#### Code Generation Commands
- Component generators
- API endpoint creators
- Test file generators
- Configuration generators

#### Code Analysis Commands
- Quality analyzers
- Security auditors
- Performance profilers
- Dependency analyzers

#### Build and Deploy Commands
- Build optimizers
- Deployment automation
- Environment setup
- CI/CD generators

#### Development Workflow Commands
- Git workflow automation
- Project setup
- Database migrations
- Documentation generators

## Scope Management

### User-Level Commands (`~/.claude/commands/`)

**Use for**:
- Personal workflow automation
- Commands used across all projects
- General-purpose utilities
- Personal productivity tools

**Activation**: Automatically available in all Claude Code sessions

**Examples**:
- Personal note templates
- Common code snippets
- Preferred testing patterns
- Personal documentation styles

### Project-Level Commands (`.claude/commands/`)

**Use for**:
- Project-specific workflows
- Team-shared commands
- Framework-specific generators
- Project conventions

**Activation**: Available only in project directory

**Examples**:
- Project component generators
- API endpoint templates following project patterns
- Project-specific build commands
- Team documentation generators

**Version control**: Commit project commands to share with team

## Command Templates by Category

Consult `references/command-catalog.md` for complete template examples.

### Quick Reference

**Code Generation Template**:
```markdown
# [Feature] Generator

Generate [feature type] for $ARGUMENTS following project conventions.

## Task
I'll analyze the project and create comprehensive [feature] including:
1. [Primary files]
2. [Tests and docs]

## Process
1. Analyze project structure
2. Generate [feature] files
3. Add tests
4. Update imports/exports
```

**Analysis Template**:
```markdown
# [Analysis Type] Analyzer

Analyze $ARGUMENTS for [concerns] and provide recommendations.

## Task
I'll perform comprehensive [analysis] covering:
1. [Analysis area 1]
2. [Issue identification]

## Process
1. Scan [target]
2. Identify issues
3. Prioritize findings
4. Generate report
```

## Best Practices

Reference `references/best-practices.md` for comprehensive guidance.

**Key principles**:

### Command Design
- Make commands focused and single-purpose
- Use descriptive names that indicate action and target
- Include clear validation and error handling
- Provide actionable output with next steps

### Argument Handling
- Document expected argument format clearly
- Validate inputs before processing
- Handle edge cases and missing arguments
- Support both simple and complex argument patterns

### Output Quality
- Generate clean, formatted output
- Include explanations for generated code
- Provide usage examples
- Add comments and documentation in generated files

### Maintenance
- Keep commands updated with project patterns
- Remove outdated commands
- Document command dependencies
- Test commands after framework updates

### Team Coordination
- Commit project commands to version control
- Document command purpose in README
- Use consistent naming across team commands
- Review command changes like code changes

## Quick Reference

```bash
# Create new command
python3 scripts/create_command.py optimize-images user

# Validate command structure
python3 scripts/validate_command.py ~/.claude/commands/optimize-images.md

# Use command in Claude Code
/optimize-images src/assets/

# List available commands
ls ~/.claude/commands/
ls .claude/commands/

# Test command
/your-command-name test-arguments
```

## Common Patterns

### File/Directory Processing
```markdown
## Process
1. Validate path exists: $ARGUMENTS
2. Apply glob patterns for multi-file operations
3. Check permissions
4. Process files with error handling
5. Generate summary report
```

### Configuration-Based Generation
```markdown
## Process
1. Read project configuration
2. Parse $ARGUMENTS for options
3. Generate files from templates
4. Update project files (package.json, etc.)
5. Provide usage instructions
```

### Analysis and Reporting
```markdown
## Process
1. Scan $ARGUMENTS for target files
2. Apply analysis rules
3. Classify findings (critical/warning/info)
4. Generate structured report
5. Provide remediation steps
```

## Resources

### scripts/
- `create_command.py` - Interactive command creator with templates
- `validate_command.py` - Validate command structure and format

### references/
- `command-catalog.md` - Comprehensive command examples by category
- `best-practices.md` - Detailed guidance on command design and maintenance

### assets/
- `command-template.md` - Base template for new commands
