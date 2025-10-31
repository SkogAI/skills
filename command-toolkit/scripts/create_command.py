#!/usr/bin/env python3
"""
Command Creator - Interactive tool for creating new slash commands

Usage:
    create_command.py <command-name> [scope]

Arguments:
    command-name: Name of the command in kebab-case (e.g., optimize-images)
    scope: 'user' (default, ~/.claude/commands/) or 'project' (.claude/commands/)

Examples:
    create_command.py optimize-images user
    create_command.py generate-component project
    create_command.py analyze-security
"""

import sys
from pathlib import Path


COMMAND_TEMPLATES = {
    'generation': '''# {title}

{description}

## Task

I'll analyze the project structure and create comprehensive {target} for $ARGUMENTS following project conventions and best practices.

## Process

I'll follow these steps:

1. Analyze project structure and existing patterns
2. Identify the appropriate location for new {target}
3. Generate {target} with proper structure and naming
4. Create associated test files and documentation
5. Update imports, exports, and configuration as needed
6. Validate generated code follows project standards

## Generation Features

### Code Structure

- Follow project naming conventions and file organization
- Implement proper component/module structure
- Add comprehensive type definitions and interfaces
- Include error handling and validation

### Quality Standards

- Generate clean, readable, maintainable code
- Add inline comments for complex logic
- Follow language-specific best practices
- Ensure consistency with existing codebase patterns

### Supporting Files

- Create test files with basic test cases
- Generate usage documentation and examples
- Add JSDoc/docstring comments
- Update relevant configuration files

## Validation

I'll ensure the generated {target}:

- Compiles/runs without errors
- Follows project linting rules
- Matches existing code style
- Includes proper imports and dependencies
- Has appropriate file permissions

## Best Practices

### Project Integration

- Match existing architectural patterns
- Use established naming conventions
- Follow project directory structure
- Integrate with existing tooling

### Code Quality

- Write self-documenting code with clear names
- Add comments only where needed for clarity
- Keep functions/methods focused and small
- Handle edge cases and errors appropriately

I'll adapt to your project's framework, language, and established patterns.
''',

    'analysis': '''# {title}

{description}

## Task

I'll perform comprehensive analysis of $ARGUMENTS for {concerns} and provide actionable recommendations.

## Process

I'll follow these steps:

1. Scan and read the target files or directories
2. Apply analysis rules and heuristics
3. Identify issues, patterns, and opportunities
4. Classify findings by severity (critical/warning/info)
5. Generate structured report with recommendations
6. Provide specific code examples for fixes

## Analysis Areas

### Code Quality

- Code complexity and maintainability metrics
- Naming conventions and consistency
- Function/method length and responsibility
- Code duplication and reusability
- Documentation completeness

### Potential Issues

- Logic errors and edge cases
- Performance bottlenecks
- Security vulnerabilities
- Resource leaks and inefficiencies
- Deprecated API usage

### Best Practice Compliance

- Language-specific idioms and patterns
- Framework conventions
- Project-specific standards
- Industry best practices
- Accessibility requirements

## Reporting Format

### Issue Classification

**Critical**: Issues that must be fixed immediately
- Security vulnerabilities
- Logic errors causing failures
- Data corruption risks
- Breaking changes

**Warning**: Issues that should be addressed
- Performance problems
- Code smells and anti-patterns
- Deprecated usage
- Missing error handling

**Info**: Suggestions for improvement
- Style inconsistencies
- Refactoring opportunities
- Documentation gaps
- Optimization potential

### Recommendations

For each finding, I'll provide:

- Clear description of the issue
- Impact and risk assessment
- Specific code examples showing the problem
- Suggested fix with code examples
- Priority and effort estimate
- References to documentation or best practices

## Best Practices

### Analysis Approach

- Focus on actionable findings, not theoretical issues
- Prioritize based on impact and risk
- Provide specific, concrete recommendations
- Include code examples in all suggestions
- Consider project context and constraints

### Reporting Quality

- Structure findings logically by category
- Use consistent severity classifications
- Provide clear, concise descriptions
- Include file names and line numbers
- Summarize key findings at the end

I'll adapt the analysis to your project's language, framework, and specific requirements.
''',

    'build': '''# {title}

{description}

## Task

I'll {action} for $ARGUMENTS following build best practices and deployment standards.

## Process

I'll follow these steps:

1. Validate the build environment and dependencies
2. Read and parse build configuration
3. Apply {action_type} optimizations and transformations
4. Execute build steps in proper sequence
5. Validate build output and artifacts
6. Generate build report with metrics

## Build Operations

### Pre-Build Validation

- Check environment variables and configuration
- Verify all dependencies are available
- Validate source files and assets
- Ensure proper permissions and access

### Build Execution

- Clean previous build artifacts
- Compile/transpile source code
- Process assets and resources
- Apply optimizations (minification, tree-shaking, etc.)
- Generate source maps if needed

### Post-Build Validation

- Verify build completed without errors
- Check output file sizes and structure
- Validate generated artifacts
- Run smoke tests if applicable

## Optimization Strategies

### Performance

- Minimize bundle size
- Optimize asset loading
- Enable code splitting
- Configure caching strategies

### Quality

- Enable strict compilation mode
- Generate type definitions
- Include debugging information
- Validate output integrity

## Best Practices

### Build Configuration

- Use consistent build settings across environments
- Document all build options and flags
- Version-lock dependencies
- Maintain reproducible builds

### Error Handling

- Provide clear error messages
- Include resolution steps for common issues
- Validate inputs before processing
- Clean up partial builds on failure

### Reporting

- Show build progress and timing
- Report file sizes and optimizations
- Highlight warnings and errors
- Provide actionable next steps

I'll adapt to your project's build system, tools, and deployment requirements.
''',

    'workflow': '''# {title}

{description}

## Task

I'll automate {workflow_task} for $ARGUMENTS following project workflow patterns and best practices.

## Process

I'll follow these steps:

1. Understand the current state and requirements
2. Validate all preconditions are met
3. Execute workflow steps in proper sequence
4. Handle errors and edge cases gracefully
5. Verify successful completion
6. Provide summary and next steps

## Workflow Steps

### Preparation

- Validate input arguments and parameters
- Check system state and prerequisites
- Backup data if needed
- Set up temporary resources

### Execution

- Perform primary workflow operations
- Monitor progress and status
- Handle interruptions and retries
- Log important actions and decisions

### Completion

- Clean up temporary resources
- Validate final state
- Update relevant tracking or configuration
- Generate completion report

## Error Handling

### Prevention

- Validate inputs before processing
- Check preconditions explicitly
- Use safe operations and transactions
- Provide dry-run mode when appropriate

### Recovery

- Detect errors early
- Rollback partial changes on failure
- Provide clear error messages
- Suggest corrective actions

### Logging

- Track all significant operations
- Record decision points
- Log errors with context
- Generate audit trail if needed

## Best Practices

### Automation Quality

- Make workflows idempotent when possible
- Handle partial completion gracefully
- Provide status updates for long operations
- Support both interactive and batch modes

### User Experience

- Show clear progress indicators
- Explain what's happening at each step
- Provide meaningful completion summaries
- Include next steps and follow-up actions

### Reliability

- Test common failure scenarios
- Handle network and I/O errors
- Support cancellation and interruption
- Maintain data integrity throughout

I'll adapt to your project's specific workflow requirements and constraints.
'''
}


def get_user_input(prompt, default=None):
    """Get user input with optional default value."""
    if default:
        response = input(f"{prompt} [{default}]: ").strip()
        return response if response else default
    else:
        response = input(f"{prompt}: ").strip()
        while not response:
            print("This field is required.")
            response = input(f"{prompt}: ").strip()
        return response


def title_case_command_name(command_name):
    """Convert kebab-case command name to Title Case."""
    return ' '.join(word.capitalize() for word in command_name.split('-'))


def create_command(command_name, scope='user'):
    """
    Create a new command file interactively.

    Args:
        command_name: Name of the command (kebab-case)
        scope: 'user' or 'project'

    Returns:
        Path to created command file, or None if error
    """
    # Determine target directory
    if scope == 'user':
        commands_dir = Path.home() / '.claude' / 'commands'
    elif scope == 'project':
        commands_dir = Path.cwd() / '.claude' / 'commands'
    else:
        print(f"❌ Error: Invalid scope '{scope}'. Must be 'user' or 'project'.")
        return None

    # Create directory if it doesn't exist
    try:
        commands_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    # Check if command already exists
    command_file = commands_dir / f"{command_name}.md"
    if command_file.exists():
        overwrite = input(f"⚠️  Command '{command_name}' already exists. Overwrite? (y/N): ").strip().lower()
        if overwrite != 'y':
            print("❌ Command creation cancelled.")
            return None

    print(f"\n📝 Creating command: {command_name}")
    print(f"   Scope: {scope}")
    print(f"   Location: {command_file}")
    print()

    # Interactive prompts
    print("Let's configure your command:")
    print()

    title = get_user_input("Command title (display name)", title_case_command_name(command_name))
    description = get_user_input("Brief description (what does this command do)")

    print("\nCommand category:")
    print("  1. generation - Generate code, files, or configurations")
    print("  2. analysis - Analyze code, find issues, provide recommendations")
    print("  3. build - Build, deploy, or optimize projects")
    print("  4. workflow - Automate development workflows")
    category = get_user_input("Choose category (1-4)", "1")

    category_map = {'1': 'generation', '2': 'analysis', '3': 'build', '4': 'workflow'}
    category_name = category_map.get(category, 'generation')

    # Category-specific prompts
    template_vars = {
        'title': title,
        'description': description
    }

    if category_name == 'generation':
        target = get_user_input("What will be generated (e.g., 'components', 'API endpoints')")
        template_vars['target'] = target
    elif category_name == 'analysis':
        concerns = get_user_input("What will be analyzed (e.g., 'security issues', 'performance')")
        template_vars['concerns'] = concerns
    elif category_name == 'build':
        action = get_user_input("What action (e.g., 'optimize the build', 'deploy to production')")
        action_type = get_user_input("Action type (e.g., 'optimization', 'deployment')")
        template_vars['action'] = action
        template_vars['action_type'] = action_type
    elif category_name == 'workflow':
        workflow_task = get_user_input("Workflow task (e.g., 'the git workflow', 'database migrations')")
        template_vars['workflow_task'] = workflow_task

    print(f"\n✅ Creating {category_name} command...")

    # Generate command content from template
    template = COMMAND_TEMPLATES[category_name]
    content = template.format(**template_vars)

    # Write command file
    try:
        command_file.write_text(content)
        print(f"✅ Command created successfully: {command_file}")
    except Exception as e:
        print(f"❌ Error writing command file: {e}")
        return None

    # Print usage instructions
    print("\n📋 Next steps:")
    print(f"   1. Review and customize: {command_file}")
    print(f"   2. Validate structure: python3 scripts/validate_command.py {command_file}")
    print(f"   3. Use in Claude Code: /{command_name} <arguments>")
    print()
    print("💡 Tips:")
    print("   - Customize the Process section for your specific workflow")
    print("   - Add category-specific sections as needed")
    print("   - Test with various arguments to ensure robustness")

    return command_file


def main():
    if len(sys.argv) < 2:
        print("Usage: create_command.py <command-name> [scope]")
        print("\nArguments:")
        print("  command-name  Name in kebab-case (e.g., 'optimize-images')")
        print("  scope         'user' (default) or 'project'")
        print("\nExamples:")
        print("  create_command.py optimize-images user")
        print("  create_command.py generate-component project")
        print("  create_command.py analyze-security")
        sys.exit(1)

    command_name = sys.argv[1]
    scope = sys.argv[2] if len(sys.argv) > 2 else 'user'

    # Validate command name
    if not all(c.islower() or c.isdigit() or c == '-' for c in command_name):
        print("❌ Error: Command name must be kebab-case (lowercase letters, digits, hyphens)")
        sys.exit(1)

    if command_name.startswith('-') or command_name.endswith('-'):
        print("❌ Error: Command name cannot start or end with a hyphen")
        sys.exit(1)

    result = create_command(command_name, scope)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
