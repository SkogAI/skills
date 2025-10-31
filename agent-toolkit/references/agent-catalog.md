# Agent Catalog - Available Custom Subagents

This reference documents the custom subagents currently defined in the skogai ecosystem.

## Code Explorer (sonnet, yellow)
**File**: `code-explorer.md`
**Purpose**: Deeply analyzes existing codebase features by tracing execution paths, mapping architecture layers, understanding patterns and abstractions, and documenting dependencies to inform new development.

**Tools**: Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShell, BashOutput

**When to use**:
- Understanding how a specific feature works end-to-end
- Tracing data flow through abstraction layers
- Identifying dependencies and integration points
- Documenting existing patterns before extending them

**Output**: Comprehensive analysis with file:line references, execution flow, architecture insights, and list of essential files.

## Code Architect (sonnet, green)
**File**: `code-architect.md`
**Purpose**: Designs feature architectures by analyzing existing codebase patterns and conventions, then providing comprehensive implementation blueprints with specific files to create/modify, component designs, data flows, and build sequences.

**Tools**: Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShell, BashOutput

**When to use**:
- Designing new features that must integrate with existing code
- Creating implementation blueprints for complex features
- Extracting and applying codebase patterns
- Breaking down features into phased implementation

**Output**: Decisive architecture blueprint with patterns found, component design, implementation map, data flow, build sequence, and critical details.

## Code Reviewer (opus, green)
**File**: `code-reviewer.md`
**Purpose**: Reviews code for adherence to project guidelines (CLAUDE.md), style guides, and best practices. Only reports high-confidence issues (≥80% confidence) to minimize false positives.

**Tools**: All (model: opus for thoroughness)

**When to use**:
- After writing or modifying code
- Before committing changes
- Before creating pull requests
- Proactively after completing logical chunks

**Output**: Grouped by severity (Critical: 90-100, Important: 80-89), with file:line references, CLAUDE.md rule citations, and concrete fix suggestions.

## Code Simplifier (opus)
**File**: `code-simplifier.md`
**Purpose**: Simplifies code for clarity, consistency, and maintainability while preserving all functionality. Applies project-specific best practices and avoids over-simplification.

**Tools**: All (model: opus for quality)

**When to use**:
- After completing a coding task
- After writing a logical chunk of code
- To refine implementations for clarity
- After bug fixes or performance optimizations

**Key principles**:
- Preserve exact functionality
- Apply project standards (ES modules, function keyword, explicit types)
- Enhance clarity (reduce nesting, eliminate redundancy)
- Maintain balance (avoid nested ternaries, prioritize readability)

## Silent Failure Hunter (inherit, yellow)
**File**: `code-shower.md` (note: filename mismatch with actual purpose)
**Purpose**: Identifies silent failures, inadequate error handling, and inappropriate fallback behavior. Zero tolerance for errors that occur without proper logging and user feedback.

**Tools**: Inherit from parent context

**When to use**:
- Reviewing PRs with error handling changes
- After implementing try-catch blocks
- When adding fallback logic
- After refactoring error handling

**Core principles**:
- Silent failures are unacceptable
- Users deserve actionable feedback
- Fallbacks must be explicit and justified
- Catch blocks must be specific

## Type Design Analyzer (inherit, pink)
**File**: `code-type-designer.md`
**Purpose**: Analyzes type design for strong invariants, proper encapsulation, and practical usefulness. Provides ratings and recommendations for type improvements.

**Tools**: Inherit from parent context

**When to use**:
- Introducing new types to ensure best practices
- During PR creation with new types
- Refactoring existing types
- Reviewing data models and schemas

**Analysis framework**:
- Encapsulation (1-10): Are internals properly hidden?
- Invariant Expression (1-10): How clearly are invariants communicated?
- Invariant Usefulness (1-10): Do they prevent real bugs?
- Invariant Enforcement (1-10): Are all mutation points guarded?

## Code Flow Mapper (yellow)
**File**: `code-flow-mapper.md`
**Purpose**: Traces execution paths and file interconnections, generating detailed flow reports.

**Tools**: Task, Bash, Glob, Grep, LS, ExitPlanMode, Read, Edit, MultiEdit, Write, NotebookRead, NotebookEdit, WebFetch, TodoWrite, MCP tools

**When to use**:
- Understanding complex execution paths
- Mapping dependencies and data flow
- Documenting system behavior
- After investigation work needs flow visualization

**Workflow**: Reads INVESTIGATION_REPORT.md, traces flows, updates FLOW_REPORT.md incrementally.

## Agent Selection Guide

**For understanding existing code**: code-explorer
**For designing new features**: code-architect
**For quality assurance**: code-reviewer (before commits/PRs)
**For code cleanup**: code-simplifier (after implementations)
**For error handling audit**: silent-failure-hunter
**For type system design**: type-design-analyzer
**For flow visualization**: code-flow-mapper

## Combining Agents

Typical workflows:
1. **New Feature**: code-explorer → code-architect → implementation → code-simplifier → code-reviewer
2. **Bug Fix**: code-explorer → fix → code-simplifier → code-reviewer
3. **Refactoring**: code-explorer → refactor → code-simplifier → type-design-analyzer → code-reviewer
4. **Error Handling Review**: silent-failure-hunter → fixes → code-reviewer
