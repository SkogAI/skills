# Command Catalog

Comprehensive examples of slash commands organized by category. Use these as templates and references when creating new commands.

## Table of Contents

1. [Code Generation Commands](#code-generation-commands)
2. [Code Analysis Commands](#code-analysis-commands)
3. [Build and Deploy Commands](#build-and-deploy-commands)
4. [Development Workflow Commands](#development-workflow-commands)

---

## Code Generation Commands

Commands that generate code, files, or configurations from templates.

### Component Generator

**File**: `generate-component.md`

```markdown
# Component Generator

Generate React components for $ARGUMENTS following project conventions and best practices.

## Task

I'll analyze the project structure and create comprehensive React components including:

1. Component file with TypeScript definitions
2. Associated test file with basic test cases
3. Storybook story for component documentation
4. CSS/styled-components for styling
5. Updated index file for exports

## Process

I'll follow these steps:

1. Analyze existing component structure and patterns
2. Identify the appropriate directory for the new component
3. Generate component file with props interface and implementation
4. Create test file with render tests and basic interactions
5. Generate Storybook story with component variants
6. Add styling following project conventions
7. Update index.ts to export new component

## Generation Features

### Component Structure

- Functional component with TypeScript
- Props interface with JSDoc comments
- Proper React hooks usage
- Error boundaries where appropriate
- Accessibility attributes (ARIA)

### Code Quality

- ESLint and Prettier compliant
- Comprehensive TypeScript types
- Self-documenting code with clear naming
- Proper import organization

### Supporting Files

- Jest/React Testing Library tests
- Storybook stories with controls
- CSS Modules or styled-components
- README with component usage

## Validation

I'll ensure the generated component:

- Compiles without TypeScript errors
- Passes all linting rules
- Follows project naming conventions
- Matches existing component patterns
- Includes proper accessibility features

## Best Practices

### Project Integration

- Match existing component architecture
- Use established state management patterns
- Follow project directory structure
- Integrate with existing theme/styling system

### Code Quality

- Write self-documenting component and prop names
- Keep components focused and reusable
- Handle edge cases and loading states
- Implement proper error handling

I'll adapt to your project's React version, state management, and styling approach.
```

**Usage**:
```
/generate-component UserProfile
/generate-component Button common/ui
```

---

### API Endpoint Generator

**File**: `generate-endpoint.md`

```markdown
# API Endpoint Generator

Generate REST API endpoints for $ARGUMENTS following project API conventions.

## Task

I'll create comprehensive API endpoint implementation including:

1. Route handler with request validation
2. Controller logic with business rules
3. Service layer for data operations
4. Request/response TypeScript types
5. API tests with various scenarios

## Process

I'll follow these steps:

1. Analyze existing API structure and patterns
2. Determine HTTP method and route path
3. Generate route handler with middleware
4. Implement controller with validation
5. Create service layer functions
6. Add TypeScript interfaces for request/response
7. Generate integration tests

## API Features

### Request Handling

- Request validation with schema (Zod/Joi/Yup)
- Authentication and authorization checks
- Input sanitization
- Error handling middleware

### Response Format

- Consistent response structure
- Proper HTTP status codes
- Error messages with details
- Pagination for list endpoints

### Data Layer

- Repository/service pattern
- Database query optimization
- Transaction handling
- Error propagation

## Documentation

I'll include:

- OpenAPI/Swagger documentation
- JSDoc comments on functions
- Request/response examples
- Error code documentation

## Best Practices

### Security

- Validate all inputs
- Implement rate limiting
- Use parameterized queries
- Sanitize error messages

### Performance

- Implement caching where appropriate
- Optimize database queries
- Use pagination for large datasets
- Add database indexes

I'll adapt to your project's framework (Express/Fastify/NestJS), ORM, and API patterns.
```

**Usage**:
```
/generate-endpoint users/profile GET
/generate-endpoint posts POST
```

---

### Test File Generator

**File**: `generate-tests.md`

```markdown
# Test Generator

Generate test files for $ARGUMENTS with comprehensive test cases.

## Task

I'll create thorough test coverage including:

1. Unit tests for functions and methods
2. Integration tests for features
3. Test fixtures and mocks
4. Test utilities and helpers

## Process

I'll follow these steps:

1. Read and analyze the target code
2. Identify testable units and behaviors
3. Generate test file with proper structure
4. Create test cases for happy paths
5. Add edge case and error handling tests
6. Set up mocks and fixtures
7. Add test utilities as needed

## Test Coverage

### Test Cases

- Happy path scenarios
- Edge cases and boundaries
- Error conditions and exceptions
- Invalid inputs and validation
- Concurrent operations if applicable

### Test Structure

- Clear test descriptions
- Arrange-Act-Assert pattern
- Proper test isolation
- Shared setup and teardown

### Mocking Strategy

- Mock external dependencies
- Mock API calls and network requests
- Mock database operations
- Mock file system operations

## Test Quality

I'll ensure tests are:

- Reliable and deterministic
- Fast to execute
- Independent and isolated
- Maintainable and readable
- Meaningful and valuable

## Best Practices

### Test Organization

- Group related tests with describe blocks
- Use descriptive test names
- Follow project test structure
- Keep tests focused and atomic

### Assertions

- Use specific assertions
- Test one thing per test
- Include helpful error messages
- Verify all relevant outputs

I'll adapt to your testing framework (Jest/Vitest/Mocha) and mocking library.
```

**Usage**:
```
/generate-tests src/utils/validation.ts
/generate-tests src/components/UserProfile.tsx
```

---

## Code Analysis Commands

Commands that analyze code and provide insights or recommendations.

### Security Analyzer

**File**: `analyze-security.md`

```markdown
# Security Analyzer

Analyze $ARGUMENTS for security vulnerabilities and provide remediation steps.

## Task

I'll perform comprehensive security analysis covering:

1. Common vulnerability patterns (OWASP Top 10)
2. Input validation and sanitization issues
3. Authentication and authorization flaws
4. Dependency vulnerabilities
5. Configuration security problems

## Process

I'll follow these steps:

1. Scan files for security anti-patterns
2. Check for injection vulnerabilities (SQL, XSS, etc.)
3. Analyze authentication and session handling
4. Review access control implementations
5. Check cryptography usage
6. Identify dependency vulnerabilities
7. Generate prioritized findings report

## Security Checks

### Input Validation

- SQL injection vulnerabilities
- Cross-site scripting (XSS) risks
- Command injection flaws
- Path traversal issues
- LDAP injection risks

### Authentication & Authorization

- Weak password requirements
- Insecure session management
- Missing authorization checks
- Broken access control
- Privilege escalation risks

### Cryptography

- Weak encryption algorithms
- Hardcoded secrets and keys
- Insecure random number generation
- Improper certificate validation

### Configuration

- Exposed sensitive data
- Debug mode in production
- Insecure CORS configuration
- Missing security headers

## Reporting Format

### Issue Classification

**Critical**: Immediate security risks
- SQL injection vulnerabilities
- Authentication bypass
- Remote code execution
- Exposed credentials

**High**: Significant security concerns
- XSS vulnerabilities
- Weak cryptography
- Authorization flaws
- Sensitive data exposure

**Medium**: Security improvements needed
- Missing input validation
- Weak session management
- Insecure configurations
- Outdated dependencies

**Low**: Security best practices
- Missing security headers
- Verbose error messages
- Cookie security flags

### Recommendations

For each finding, I'll provide:

- Vulnerability description and impact
- Code location and context
- Proof of concept if applicable
- Specific remediation steps with code examples
- References to security standards (OWASP, CWE)

## Best Practices

### Analysis Approach

- Focus on exploitable vulnerabilities
- Prioritize by risk and impact
- Provide actionable fixes
- Include code examples
- Reference security standards

I'll adapt to your application framework and deployment environment.
```

**Usage**:
```
/analyze-security src/api/
/analyze-security src/auth/login.ts
```

---

### Performance Analyzer

**File**: `analyze-performance.md`

```markdown
# Performance Analyzer

Analyze $ARGUMENTS for performance bottlenecks and optimization opportunities.

## Task

I'll perform comprehensive performance analysis covering:

1. Algorithm complexity and efficiency
2. Memory usage and leaks
3. Network and I/O operations
4. Rendering performance (for frontend)
5. Database query optimization

## Process

I'll follow these steps:

1. Analyze code for computational complexity
2. Identify expensive operations and bottlenecks
3. Review data structure usage
4. Check for unnecessary re-renders (React)
5. Analyze database queries and indexes
6. Identify caching opportunities
7. Generate optimization recommendations

## Performance Areas

### Computational Efficiency

- Algorithm complexity (O(n²), etc.)
- Inefficient loops and iterations
- Unnecessary computations
- Heavy synchronous operations

### Memory Management

- Memory leaks
- Large object allocations
- Inefficient data structures
- Circular references

### I/O Operations

- Excessive network requests
- Large file operations
- Synchronous I/O blocking
- Missing connection pooling

### Frontend Performance

- Unnecessary re-renders
- Large bundle sizes
- Unoptimized images
- Lack of code splitting
- Missing memoization

## Optimization Strategies

### Code Optimizations

- Use efficient algorithms and data structures
- Implement memoization and caching
- Batch operations where possible
- Use lazy loading and pagination

### Database Optimizations

- Add proper indexes
- Optimize query structure
- Use query result caching
- Implement connection pooling

### Frontend Optimizations

- Implement React.memo and useMemo
- Code splitting and lazy loading
- Image optimization and lazy loading
- Virtual scrolling for long lists

## Reporting Format

### Performance Impact

**High Impact**: Significant performance degradation
- O(n²) or worse algorithms in hot paths
- Memory leaks
- Missing database indexes
- Excessive API calls

**Medium Impact**: Noticeable performance issues
- Suboptimal algorithms
- Unnecessary computations
- Inefficient data structures
- Large bundle sizes

**Low Impact**: Minor optimizations
- Small inefficiencies
- Code readability improvements
- Future scalability concerns

### Recommendations

For each finding, I'll provide:

- Performance issue description
- Impact on application performance
- Specific optimization approach with code
- Expected performance improvement
- Trade-offs and considerations

I'll adapt to your application type, scale, and performance requirements.
```

**Usage**:
```
/analyze-performance src/utils/
/analyze-performance src/components/Dashboard.tsx
```

---

## Build and Deploy Commands

Commands for build optimization, deployment, and environment management.

### Build Optimizer

**File**: `optimize-build.md`

```markdown
# Build Optimizer

Optimize build configuration for $ARGUMENTS to improve bundle size and performance.

## Task

I'll analyze and optimize the build process including:

1. Bundle size analysis and reduction
2. Code splitting configuration
3. Tree shaking optimization
4. Asset optimization
5. Build performance improvements

## Process

I'll follow these steps:

1. Analyze current build configuration
2. Run bundle analysis to identify large dependencies
3. Configure code splitting for optimal chunks
4. Enable and verify tree shaking
5. Optimize asset loading and compression
6. Set up caching strategies
7. Generate optimization report

## Optimization Areas

### Bundle Size Reduction

- Identify and remove unused dependencies
- Configure tree shaking properly
- Use dynamic imports for code splitting
- Replace large libraries with lighter alternatives
- Enable minification and compression

### Code Splitting

- Split vendor and application code
- Create route-based chunks
- Lazy load heavy components
- Configure optimal chunk sizes

### Asset Optimization

- Compress images and media
- Use modern image formats (WebP)
- Enable lazy loading for images
- Optimize font loading

### Build Performance

- Enable caching for faster rebuilds
- Parallelize build tasks
- Optimize TypeScript compilation
- Use faster build tools where appropriate

## Configuration Changes

I'll update:

- Webpack/Vite/Rollup configuration
- Package.json scripts
- TypeScript configuration
- Asset processing pipelines

## Reporting

### Before/After Metrics

- Total bundle size
- Number of chunks
- Largest dependencies
- Build time
- Load performance metrics

### Recommendations

- Dependency alternatives
- Code splitting strategies
- Caching improvements
- Further optimization opportunities

## Best Practices

### Bundle Management

- Keep main bundle under target size
- Split vendor dependencies
- Use content hashing for caching
- Monitor bundle size in CI/CD

### Performance Budget

- Set size budgets for bundles
- Fail builds exceeding budget
- Track performance over time
- Regular dependency audits

I'll adapt to your build tool (Webpack/Vite/esbuild/Rollup) and deployment target.
```

**Usage**:
```
/optimize-build
/optimize-build webpack.config.js
```

---

### Deploy to Production

**File**: `deploy-production.md`

```markdown
# Production Deployment

Deploy $ARGUMENTS to production following deployment best practices.

## Task

I'll orchestrate production deployment including:

1. Pre-deployment validation
2. Build production artifacts
3. Run deployment process
4. Post-deployment verification
5. Rollback capability if needed

## Process

I'll follow these steps:

1. Validate current branch and version
2. Run all tests and quality checks
3. Build production artifacts
4. Create backup/snapshot of current production
5. Deploy to production environment
6. Run smoke tests
7. Monitor deployment for issues
8. Generate deployment report

## Pre-Deployment Checks

### Code Quality

- All tests passing
- Linting and formatting checks
- TypeScript compilation successful
- Security audit passes

### Environment

- Production environment variables set
- Database migrations ready
- External services available
- SSL certificates valid

### Version Control

- Deploying from correct branch
- Version tag created
- Changelog updated
- No uncommitted changes

## Deployment Steps

### Build Phase

- Clean previous builds
- Install production dependencies
- Build optimized production bundle
- Generate source maps
- Create deployment artifacts

### Deploy Phase

- Create backup of current production
- Upload new artifacts
- Update environment configuration
- Run database migrations
- Restart services
- Clear caches

### Verification Phase

- Check application health endpoints
- Verify critical user flows
- Check error logging
- Monitor performance metrics
- Test rollback procedure

## Rollback Plan

If issues detected:

1. Immediately stop deployment
2. Restore from backup/snapshot
3. Rollback database migrations
4. Verify rollback successful
5. Investigate and fix issues
6. Document incident

## Monitoring

Post-deployment monitoring:

- Error rates and exceptions
- Performance metrics
- User activity patterns
- Server resources
- External service health

## Best Practices

### Safety

- Always deploy to staging first
- Use feature flags for risky changes
- Keep rollback procedure tested
- Monitor closely after deployment

### Communication

- Announce deployment window
- Update status page
- Alert team of completion
- Document any issues

I'll adapt to your hosting platform (AWS/Vercel/Heroku/Docker) and deployment pipeline.
```

**Usage**:
```
/deploy-production
/deploy-production --environment staging
```

---

## Development Workflow Commands

Commands that automate common development workflows.

### Git Workflow Helper

**File**: `git-workflow.md`

```markdown
# Git Workflow Helper

Automate git workflow for $ARGUMENTS following project conventions.

## Task

I'll help with common git operations including:

1. Creating feature branches
2. Committing with conventional commit messages
3. Preparing pull requests
4. Resolving merge conflicts
5. Cleaning up branches

## Process

I'll follow these steps based on the requested workflow:

1. Understand current git state
2. Validate working directory
3. Execute requested git operations
4. Verify operations completed successfully
5. Provide next steps guidance

## Workflow Operations

### Feature Branch Creation

- Create branch from up-to-date main/develop
- Use conventional branch naming (feature/, fix/, etc.)
- Set up branch tracking
- Make initial commit if needed

### Commit Creation

- Stage relevant changes
- Generate conventional commit message
- Include issue references
- Run pre-commit hooks

### Pull Request Preparation

- Ensure branch is up-to-date
- Squash/organize commits if needed
- Generate PR description
- List all changes
- Add testing instructions

### Conflict Resolution

- Identify conflicting files
- Show conflict markers
- Suggest resolution strategy
- Validate resolution

## Conventional Commits

I'll use the format:

```
type(scope): subject

body

footer
```

**Types**:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Code restructuring
- test: Adding tests
- chore: Maintenance

### Branch Naming

**Format**: `type/short-description`

**Examples**:
- feature/user-authentication
- fix/login-validation-bug
- refactor/api-error-handling

## Best Practices

### Before Committing

- Review all changes
- Ensure tests pass
- Update documentation
- Check for debug code

### Branch Management

- Keep branches focused and short-lived
- Rebase on main/develop regularly
- Delete merged branches
- Use descriptive branch names

### Commit Quality

- Make atomic commits
- Write clear commit messages
- Reference issue numbers
- Separate concerns in commits

I'll adapt to your project's git workflow (GitFlow, GitHub Flow, trunk-based).
```

**Usage**:
```
/git-workflow create-branch feature/user-profile
/git-workflow commit "Add user authentication"
/git-workflow prepare-pr
```

---

### Database Migration

**File**: `create-migration.md`

```markdown
# Database Migration Generator

Generate database migration for $ARGUMENTS following project migration patterns.

## Task

I'll create database migration including:

1. Migration file with up/down operations
2. Schema changes in appropriate format
3. Data migration scripts if needed
4. Migration documentation

## Process

I'll follow these steps:

1. Understand the schema change required
2. Analyze current database schema
3. Generate migration file with timestamp
4. Write up migration (schema changes)
5. Write down migration (rollback)
6. Add data migration if needed
7. Provide testing instructions

## Migration Operations

### Schema Changes

- Create/drop tables
- Add/remove/modify columns
- Add/remove indexes
- Create/modify constraints
- Alter column types

### Data Migrations

- Transform existing data
- Populate new columns
- Clean up invalid data
- Migrate to new structure

### Relationship Changes

- Add/remove foreign keys
- Create/modify many-to-many relationships
- Update cascade rules

## Migration Structure

### Up Migration

```sql
-- Create new table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Add index
CREATE INDEX idx_users_email ON users(email);
```

### Down Migration

```sql
-- Drop index
DROP INDEX IF EXISTS idx_users_email;

-- Drop table
DROP TABLE IF EXISTS users;
```

## Validation

I'll ensure:

- Up and down migrations are inverses
- Migrations are idempotent where possible
- No data loss in down migrations (when appropriate)
- Proper transaction handling
- Index creation for foreign keys

## Testing

### Migration Testing

- Run migration on dev database
- Verify schema changes correct
- Test application with new schema
- Run down migration
- Verify rollback successful

### Data Validation

- Check data integrity after migration
- Verify constraints are enforced
- Test with existing data
- Check performance impact

## Best Practices

### Migration Safety

- Always create backups before migrating
- Test migrations on staging first
- Make migrations reversible
- Keep migrations atomic
- Use transactions where supported

### Performance

- Add indexes concurrently in PostgreSQL
- Avoid long-running transactions
- Consider maintenance windows for large changes
- Monitor migration execution time

I'll adapt to your ORM (Prisma/TypeORM/Sequelize/Knex) and database (PostgreSQL/MySQL/SQLite).
```

**Usage**:
```
/create-migration add-user-profiles-table
/create-migration add-email-index-to-users
```

---

## Common Command Patterns

### Error Handling Pattern

```markdown
## Error Handling

I'll handle errors gracefully:

1. **Input Validation**
   - Verify $ARGUMENTS are valid
   - Check file/directory existence
   - Validate permissions

2. **Execution Errors**
   - Catch and report failures clearly
   - Provide resolution steps
   - Clean up partial changes

3. **Recovery**
   - Suggest corrective actions
   - Offer rollback if applicable
   - Log errors for debugging
```

### Output Format Pattern

```markdown
## Output Format

I'll provide structured output:

### Summary
- Operation completed successfully
- Files created/modified: X
- Issues found/fixed: Y

### Details
[Detailed information about operations performed]

### Next Steps
1. [Action user should take]
2. [Optional follow-up actions]
```

### Configuration Detection Pattern

```markdown
## Configuration Detection

I'll automatically detect:

- Project framework and version
- Package manager (npm/yarn/pnpm)
- TypeScript vs JavaScript
- Testing framework
- Code style preferences
```

---

## Tips for Creating Commands

1. **Be Specific**: Clearly define what the command does
2. **Use $ARGUMENTS**: Always include the placeholder where user input goes
3. **Structure Steps**: Break down the process into clear, numbered steps
4. **Handle Errors**: Include validation and error handling in the process
5. **Adapt to Context**: End with statement about adapting to project patterns
6. **Provide Examples**: Show expected usage patterns
7. **Document Output**: Describe what users will get
8. **Include Validation**: Explain how results will be verified

## Command Template Selection

Choose template based on command purpose:

- **Generation**: Use when creating new files/code from scratch
- **Analysis**: Use when examining code and providing insights
- **Build**: Use when compiling, optimizing, or deploying
- **Workflow**: Use when automating multi-step development processes

Refer to the actual template implementations in the assets/ directory for starting points.
