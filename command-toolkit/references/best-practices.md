# Command Best Practices

Comprehensive guidance for creating, maintaining, and organizing slash commands in Claude Code.

## Table of Contents

1. [Command Design Principles](#command-design-principles)
2. [Scope Management](#scope-management)
3. [Argument Handling](#argument-handling)
4. [Process Design](#process-design)
5. [Output Quality](#output-quality)
6. [Error Handling](#error-handling)
7. [Testing Commands](#testing-commands)
8. [Documentation](#documentation)
9. [Maintenance](#maintenance)
10. [Team Coordination](#team-coordination)
11. [Common Pitfalls](#common-pitfalls)
12. [Performance Considerations](#performance-considerations)

---

## Command Design Principles

### Single Responsibility

Each command should do one thing well.

**Good**:
```
/generate-component UserProfile
/optimize-images src/assets/
/analyze-security src/api/
```

**Bad**:
```
/do-everything UserProfile optimize images analyze security
```

**Why**: Focused commands are easier to understand, test, and maintain.

### Clear Purpose

Command name and description should immediately convey what it does.

**Good names**:
- `generate-component` - Creates React components
- `analyze-security` - Scans for security issues
- `optimize-build` - Improves build configuration

**Bad names**:
- `do-work` - Too vague
- `helper` - Not descriptive
- `fix` - Too generic

### Consistent Patterns

Follow established patterns across your command suite.

**Naming patterns**:
- `generate-*` for creation commands
- `analyze-*` for analysis commands
- `optimize-*` for improvement commands
- `deploy-*` for deployment commands

**Structure patterns**:
- Always include Task and Process sections
- Use numbered steps in Process
- End with adaptation statement
- Include Best Practices section

---

## Scope Management

### When to Use User-Level Commands

Create in `~/.claude/commands/` for:

**Personal workflows**:
```
/my-note-template
/preferred-test-format
/personal-commit-style
```

**Cross-project utilities**:
```
/optimize-images
/format-json
/extract-colors-from-image
```

**Learning and experimentation**:
```
/try-new-pattern
/experimental-generator
```

### When to Use Project-Level Commands

Create in `.claude/commands/` for:

**Project-specific generators**:
```
/generate-page          # Uses project's page structure
/generate-api-endpoint  # Follows project API patterns
/generate-store         # Matches project state management
```

**Team workflows**:
```
/prepare-release        # Project's release process
/update-changelog       # Project's changelog format
/generate-migration     # Project's ORM patterns
```

**Framework-specific commands**:
```
/next-page              # Next.js specific
/nest-controller        # NestJS specific
/django-model           # Django specific
```

### Scope Decision Tree

```
Is this command specific to one project?
  Yes → Project-level (.claude/commands/)
  No → Continue...

Will it be used by the whole team?
  Yes → Project-level (.claude/commands/)
  No → Continue...

Is it a personal preference or workflow?
  Yes → User-level (~/.claude/commands/)
  No → User-level (general utility)
```

### Version Control

**Project commands**: Always commit to repository
```bash
git add .claude/commands/
git commit -m "feat: add generate-component command"
```

**User commands**: Never commit
```bash
# Add to .gitignore if not already there
echo "~/.claude/commands/" >> .gitignore
```

---

## Argument Handling

### $ARGUMENTS Placeholder

The `$ARGUMENTS` placeholder is replaced with user input.

### Single Argument

**Pattern**:
```markdown
Optimize images in $ARGUMENTS for web performance.
```

**Usage**:
```
/optimize-images src/assets/
```

**Validation**:
```markdown
## Process

1. Validate that $ARGUMENTS is a valid directory path
2. Check directory exists and is accessible
3. Find all image files (jpg, png, webp, svg)
...
```

### Multiple Arguments

**Pattern**:
```markdown
Generate a $ARGUMENTS component following project patterns.
```

**Usage**:
```
/generate-component UserProfile dashboard/pages
```

**Handling**:
- First word: component name (UserProfile)
- Second word: target directory (dashboard/pages)

**Validation**:
```markdown
## Process

1. Parse $ARGUMENTS to extract component name and optional directory
2. Validate component name follows naming conventions
3. Verify target directory exists or can be created
...
```

### Optional Arguments

**Pattern**:
```markdown
Deploy to $ARGUMENTS environment (defaults to staging if not specified).
```

**Usage**:
```
/deploy-production production
/deploy-production              # Uses default
```

**Handling**:
```markdown
## Process

1. Parse $ARGUMENTS for environment name
2. If not provided, default to 'staging'
3. Validate environment exists in configuration
...
```

### Argument Validation Best Practices

**Always validate**:
- File/directory existence
- Path validity
- Naming conventions
- Required vs optional arguments

**Provide helpful errors**:
```markdown
If $ARGUMENTS is not provided or invalid:
- Show expected format and examples
- Suggest valid values
- Explain requirements
```

**Document expected format**:
```markdown
## Arguments

Expected format: `component-name [target-directory]`

Examples:
- `/generate-component Button`
- `/generate-component UserProfile pages/dashboard`
- `/generate-component Modal shared/components`
```

---

## Process Design

### Step Structure

Break down the process into clear, actionable steps.

**Good structure**:
```markdown
## Process

I'll follow these steps:

1. Validate input arguments and check prerequisites
2. Analyze existing codebase for patterns and conventions
3. Generate primary files using project templates
4. Create supporting files (tests, stories, styles)
5. Update configuration files and exports
6. Verify generated code compiles and passes linting
7. Provide usage instructions and next steps
```

**Poor structure**:
```markdown
## Process

1. Do the thing
2. Make it work
3. Finish up
```

### Step Granularity

**Too granular** (micromanaging):
```markdown
1. Open the file
2. Read line 1
3. Read line 2
4. Parse the content
5. Save to variable
...
```

**Too vague** (not helpful):
```markdown
1. Process the files
2. Generate output
3. Done
```

**Just right** (clear and actionable):
```markdown
1. Read and parse configuration files
2. Generate component files from templates
3. Create test files with basic coverage
4. Update exports and imports
5. Validate output and provide summary
```

### Validation Steps

Always include validation:

**Pre-execution validation**:
```markdown
1. Validate $ARGUMENTS format and existence
2. Check prerequisites (dependencies, tools, permissions)
3. Verify project structure matches expected patterns
```

**Post-execution validation**:
```markdown
7. Verify generated files compile without errors
8. Check files pass linting rules
9. Confirm tests run successfully
```

### Adaptation Statement

End with how the command adapts to context:

```markdown
I'll adapt to your project's:
- Framework and version (React 17 vs 18)
- State management (Redux, Zustand, Context)
- Styling approach (CSS Modules, styled-components, Tailwind)
- Testing framework (Jest, Vitest, Testing Library)
- File organization and naming conventions
```

---

## Output Quality

### Code Generation Quality

When generating code:

**Always include**:
- Proper imports and exports
- Type definitions (TypeScript)
- JSDoc/docstring comments
- Error handling
- Accessibility attributes (for UI)

**Follow project conventions**:
- Naming patterns
- File organization
- Code style
- Architecture patterns

**Example quality indicators**:
```typescript
// Good: Complete, typed, documented
/**
 * User profile component displaying user information
 * @param user - User object with profile data
 * @param onEdit - Callback when edit button clicked
 */
interface UserProfileProps {
  user: User;
  onEdit?: () => void;
}

export const UserProfile: React.FC<UserProfileProps> = ({ user, onEdit }) => {
  // Implementation
};

// Bad: Incomplete, untyped, undocumented
export const UserProfile = ({ user, onEdit }) => {
  // Implementation
};
```

### Analysis Output Quality

When analyzing code:

**Provide specifics**:
```markdown
✅ Found 3 security issues:

1. SQL Injection vulnerability in users.ts:45
   Current: `SELECT * FROM users WHERE id = ${userId}`
   Fix: Use parameterized queries

2. Missing input validation in api/auth.ts:120
   Current: Email not validated before use
   Fix: Add email validation using validator library
```

**Not vague**:
```markdown
❌ Found some issues:
- Security problems exist
- Code could be better
- Consider improvements
```

### Explanation Quality

**Good explanations**:
```markdown
Generated UserProfile component with:
- Props interface with TypeScript types for type safety
- Responsive layout using CSS Grid
- Loading and error states for async data
- Accessibility attributes (ARIA labels, semantic HTML)
- Test file with render and interaction tests
```

**Poor explanations**:
```markdown
Created the component.
```

### Next Steps

Always provide next steps:

```markdown
## Next Steps

1. Review generated component in src/components/UserProfile.tsx
2. Customize styling in UserProfile.module.css
3. Update props interface if additional data needed
4. Run tests: `npm test UserProfile`
5. Import in parent component:
   ```typescript
   import { UserProfile } from '@/components/UserProfile';
   ```
```

---

## Error Handling

### Input Validation

Validate inputs before processing:

```markdown
## Process

1. **Validate Arguments**
   - Check $ARGUMENTS is not empty
   - Verify path exists if file/directory argument
   - Validate format matches expected pattern
   - Confirm required tools/dependencies available

   If validation fails:
   - Show clear error message
   - Explain what's wrong
   - Provide correct format example
   - Suggest valid values
```

### Graceful Failures

Handle errors gracefully:

```markdown
## Error Handling

If the operation fails:

1. **Identify the failure point**
   - Which step in the process failed?
   - What was the error message?

2. **Clean up partial changes**
   - Remove partially created files
   - Rollback configuration changes
   - Restore original state

3. **Provide recovery steps**
   - Explain what went wrong
   - Suggest how to fix the issue
   - Offer alternative approaches
   - Include relevant documentation links
```

### Error Messages

**Good error messages**:
```
❌ Error: Component name 'user-profile' is invalid.

Component names must be PascalCase (e.g., 'UserProfile').

Usage: /generate-component ComponentName [directory]
Examples:
  /generate-component UserProfile
  /generate-component Button components/ui
```

**Bad error messages**:
```
Error: invalid input
```

### Partial Completion

Handle partial completion explicitly:

```markdown
## Partial Completion Handling

If the process is interrupted:

1. List what was successfully completed
2. List what remains to be done
3. Provide options:
   - Resume from last successful step
   - Start fresh (clean up partial work)
   - Manually complete remaining steps

Files created before interruption:
- src/components/UserProfile.tsx ✓
- src/components/UserProfile.module.css ✓

Files not created:
- src/components/UserProfile.test.tsx ✗
- src/components/UserProfile.stories.tsx ✗
```

---

## Testing Commands

### Manual Testing

Test commands thoroughly before sharing:

**Test cases**:
1. **Happy path**: Normal expected usage
2. **Edge cases**: Boundary conditions, unusual inputs
3. **Error cases**: Invalid inputs, missing files, etc.
4. **No arguments**: How does it handle empty $ARGUMENTS?
5. **Multiple projects**: Does it work across different project types?

**Testing checklist**:
```markdown
✓ Command validates arguments properly
✓ Clear error messages for invalid inputs
✓ Generates correct output for valid inputs
✓ Follows project conventions
✓ Cleans up on failure
✓ Provides helpful next steps
✓ Works in different project structures
```

### Test Different Scenarios

**Different project types**:
```bash
# Test in React project
cd ~/projects/react-app
/generate-component TestComponent

# Test in Vue project
cd ~/projects/vue-app
/generate-component TestComponent

# Test in Next.js project
cd ~/projects/nextjs-app
/generate-component TestComponent
```

**Different argument patterns**:
```bash
/command-name                      # No arguments
/command-name single-arg           # One argument
/command-name arg1 arg2            # Multiple arguments
/command-name ./relative/path      # Relative path
/command-name /absolute/path       # Absolute path
/command-name --flag value         # With flags
```

### Validation Testing

Test the validation logic:

```bash
# Test invalid inputs
/generate-component                 # No name
/generate-component 123Invalid      # Invalid format
/generate-component existing-one    # Already exists

# Test edge cases
/generate-component VeryLongComponentNameThatMightBeAnIssue
/generate-component A              # Single letter
/generate-component nested/path/component
```

---

## Documentation

### Command Description

Write clear, concise descriptions:

**Good**:
```markdown
# Component Generator

Generate React components for $ARGUMENTS following project conventions and best practices.

Creates functional components with TypeScript, tests, Storybook stories, and styles.
```

**Bad**:
```markdown
# Component Generator

A tool for making components.
```

### Usage Examples

Include concrete examples:

```markdown
## Usage Examples

### Basic Component
```
/generate-component Button
```

Generates:
- src/components/Button.tsx
- src/components/Button.test.tsx
- src/components/Button.stories.tsx
- src/components/Button.module.css

### Component with Directory
```
/generate-component UserProfile pages/dashboard
```

Generates component in specific directory:
- src/pages/dashboard/UserProfile.tsx
- src/pages/dashboard/UserProfile.test.tsx
- ...

### Complex Component
```
/generate-component DataTable
```

Generates component with:
- Props interface for configuration
- Loading and error states
- Pagination support
- Sorting and filtering
```

### Expected Output

Document what users will receive:

```markdown
## Expected Output

### File Structure
```
src/components/UserProfile/
├── UserProfile.tsx           # Component implementation
├── UserProfile.test.tsx      # Test file
├── UserProfile.stories.tsx   # Storybook stories
├── UserProfile.module.css    # Component styles
└── index.ts                  # Barrel export
```

### Component Features
- TypeScript interface for props
- Responsive design with CSS Grid
- Loading state handling
- Error boundary support
- Full accessibility (ARIA)
- Comprehensive tests
```

---

## Maintenance

### Keep Commands Updated

Commands should evolve with projects:

**When to update**:
- Framework version upgrade
- New architectural patterns adopted
- Team conventions change
- New tools introduced
- Best practices evolve

**Update process**:
1. Identify outdated patterns
2. Review and update command content
3. Test with current project structure
4. Update documentation
5. Communicate changes to team

### Deprecation

When deprecating commands:

**Mark as deprecated**:
```markdown
# ⚠️ DEPRECATED: Old Component Generator

**This command is deprecated. Use `/generate-component` instead.**

This command uses outdated class component patterns.
```

**Provide migration path**:
```markdown
## Migration

Replace:
```
/old-generate-component UserProfile
```

With:
```
/generate-component UserProfile
```

The new command generates functional components with hooks.
```

**Eventually remove**:
- After deprecation period (e.g., 2 months)
- When usage drops to zero
- After team is informed

### Version Commands

For major changes, consider versioning:

```markdown
# Component Generator (v2)

Generate modern React components with hooks and TypeScript.

Migrated from class components (v1) to functional components (v2).
```

### Audit Regularly

Periodic command audit:

**Monthly review**:
- Which commands are actively used?
- Which are outdated?
- Which need updates?
- Which should be deprecated?

**Metrics to track**:
- Command usage frequency
- Error rates
- User feedback
- Time since last update

---

## Team Coordination

### Sharing Commands

When sharing project commands:

**Document in README**:
```markdown
## Available Commands

### `/generate-component`
Generate React components following project patterns.

Usage: `/generate-component ComponentName [directory]`

Example: `/generate-component UserProfile pages/dashboard`

### `/generate-endpoint`
Generate API endpoints with validation and tests.

Usage: `/generate-endpoint resource method`

Example: `/generate-endpoint users POST`
```

**Commit with clear messages**:
```bash
git add .claude/commands/generate-component.md
git commit -m "feat: add component generator command

Generates functional components with:
- TypeScript interfaces
- Test files
- Storybook stories
- CSS modules

Follows project component patterns and naming conventions."
```

### Team Standards

Establish team command standards:

**Naming conventions**:
```
generate-*    - Creation commands
analyze-*     - Analysis commands
deploy-*      - Deployment commands
fix-*         - Fix/repair commands
```

**Required sections**:
- Task (what it does)
- Process (step-by-step)
- Best Practices (guidance)

**Quality requirements**:
- Must include validation
- Must handle errors gracefully
- Must provide clear output
- Must include usage examples

### Review Process

Treat commands like code:

**Pull request review**:
```markdown
## Command Review Checklist

- [ ] Clear, descriptive command name
- [ ] Comprehensive Task description
- [ ] Step-by-step Process
- [ ] Proper $ARGUMENTS handling
- [ ] Input validation
- [ ] Error handling
- [ ] Usage examples
- [ ] Tested in project
- [ ] Documentation updated
```

### Onboarding

Help new team members:

**Onboarding documentation**:
```markdown
## Available Commands

We have custom commands for common workflows:

1. **Component Generation**: `/generate-component`
   - Creates components following project patterns
   - Includes tests and Storybook stories

2. **API Endpoints**: `/generate-endpoint`
   - Generates REST endpoints
   - Includes validation and tests

3. **Deployment**: `/deploy-staging`, `/deploy-production`
   - Automates deployment process
   - Includes safety checks

Try them out! Commands will adapt to project patterns automatically.
```

---

## Common Pitfalls

### Pitfall 1: Too Generic

**Problem**:
```markdown
# Helper

Do things with $ARGUMENTS.
```

**Solution**: Be specific about what and how:
```markdown
# Component Generator

Generate React components for $ARGUMENTS following project conventions.

Creates functional components with TypeScript, tests, and styles.
```

### Pitfall 2: No Validation

**Problem**:
```markdown
## Process

1. Generate component from $ARGUMENTS
2. Create files
```

**Solution**: Add validation steps:
```markdown
## Process

1. Validate $ARGUMENTS:
   - Check component name is provided
   - Verify name follows PascalCase convention
   - Confirm component doesn't already exist
2. Generate component from validated arguments
3. Create files in appropriate directory
4. Verify files compile successfully
```

### Pitfall 3: Vague Process

**Problem**:
```markdown
## Process

1. Do the thing
2. Finish
```

**Solution**: Break down into specific steps:
```markdown
## Process

1. Analyze existing component patterns in codebase
2. Generate component file with TypeScript interface
3. Create test file with basic test cases
4. Generate Storybook story with component variants
5. Add CSS module for styling
6. Update index.ts to export new component
7. Verify all files compile and tests pass
```

### Pitfall 4: No Error Handling

**Problem**:
Process doesn't mention what happens if things go wrong.

**Solution**: Add error handling section:
```markdown
## Error Handling

If validation fails:
- Show clear error with explanation
- Provide example of correct format
- Suggest valid alternatives

If generation fails:
- Clean up any partially created files
- Report which step failed
- Provide recovery instructions
```

### Pitfall 5: Inconsistent Patterns

**Problem**: Commands use different styles and structures.

**Solution**: Establish and follow team patterns:
- Consistent naming scheme
- Standard section structure
- Uniform argument handling
- Common output format

### Pitfall 6: No Usage Examples

**Problem**: Users don't know how to use the command.

**Solution**: Include concrete examples:
```markdown
## Usage Examples

Basic: `/generate-component Button`
With path: `/generate-component UserCard components/dashboard`
Nested: `/generate-component Modal shared/ui/modals`
```

### Pitfall 7: Outdated Patterns

**Problem**: Command generates code using old patterns.

**Solution**: Review and update regularly:
- Check against current project patterns
- Update for framework changes
- Incorporate new best practices
- Test with latest project structure

---

## Performance Considerations

### Command Execution Speed

Keep commands fast:

**Avoid**:
- Excessive file system operations
- Reading entire codebase unnecessarily
- Complex analysis when simple suffices

**Prefer**:
- Targeted file reading
- Caching results when possible
- Progressive disclosure (start fast, elaborate if needed)

### Output Size

Keep output manageable:

**For generation commands**:
- Generate only necessary files
- Don't create duplicate content
- Use imports over duplication

**For analysis commands**:
- Summarize findings
- Provide details on request
- Group related issues

### Scalability

Design commands to scale:

**Consider**:
- Large codebases (thousands of files)
- Complex project structures
- Slow file systems
- Limited memory

**Strategies**:
- Process files incrementally
- Provide progress indicators
- Allow interruption and resumption
- Cache expensive operations

---

## Summary

**Golden Rules**:

1. **Single Purpose**: Each command does one thing well
2. **Clear Process**: Break down into specific steps
3. **Validate Everything**: Check inputs before processing
4. **Handle Errors**: Gracefully handle and explain failures
5. **Adapt to Context**: Respect project patterns and conventions
6. **Document Well**: Clear descriptions and examples
7. **Test Thoroughly**: Test happy path and edge cases
8. **Maintain Actively**: Keep commands updated
9. **Team Coordination**: Share and review like code
10. **Stay Focused**: Don't let commands become too complex

**When in doubt**:
- Check command-catalog.md for examples
- Test in multiple scenarios
- Get team feedback
- Iterate based on usage
