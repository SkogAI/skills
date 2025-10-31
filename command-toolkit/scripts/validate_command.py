#!/usr/bin/env python3
"""
Command Validator - Validates slash command structure and format

Usage:
    validate_command.py <path-to-command.md>

Examples:
    validate_command.py ~/.claude/commands/optimize-images.md
    validate_command.py .claude/commands/generate-component.md
"""

import sys
import re
from pathlib import Path


class CommandValidator:
    """Validates slash command files."""

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.errors = []
        self.warnings = []
        self.info = []
        self.content = None

    def validate(self):
        """Run all validation checks."""
        print(f"🔍 Validating command: {self.file_path}")
        print()

        # Check file exists
        if not self.file_path.exists():
            self.errors.append(f"File does not exist: {self.file_path}")
            return False

        # Check file extension
        if self.file_path.suffix != '.md':
            self.errors.append(f"File must have .md extension, got: {self.file_path.suffix}")
            return False

        # Read file content
        try:
            self.content = self.file_path.read_text()
        except Exception as e:
            self.errors.append(f"Failed to read file: {e}")
            return False

        # Run validation checks
        self._check_file_naming()
        self._check_content_structure()
        self._check_arguments_placeholder()
        self._check_required_sections()
        self._check_heading_structure()
        self._check_process_steps()
        self._check_best_practices()

        return len(self.errors) == 0

    def _check_file_naming(self):
        """Validate file naming conventions."""
        name = self.file_path.stem

        # Check kebab-case
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', name):
            self.errors.append(
                f"File name must be kebab-case (lowercase with hyphens): '{name}'"
            )

        # Check length
        if len(name) > 50:
            self.warnings.append(
                f"File name is long ({len(name)} chars). Consider shortening for usability."
            )

        # Check descriptiveness
        if len(name) < 3:
            self.warnings.append(
                f"File name is very short ('{name}'). Consider a more descriptive name."
            )

    def _check_content_structure(self):
        """Check overall content structure."""
        if not self.content.strip():
            self.errors.append("File is empty")
            return

        # Check minimum length
        if len(self.content) < 100:
            self.warnings.append("File content is very short. Consider adding more detail.")

        # Check for title (H1)
        if not re.search(r'^# .+', self.content, re.MULTILINE):
            self.errors.append("Missing title (H1 heading)")

    def _check_arguments_placeholder(self):
        """Check for $ARGUMENTS placeholder."""
        if '$ARGUMENTS' not in self.content:
            self.errors.append(
                "Missing $ARGUMENTS placeholder. Commands must accept user arguments."
            )
        else:
            # Count occurrences
            count = self.content.count('$ARGUMENTS')
            if count > 5:
                self.warnings.append(
                    f"$ARGUMENTS appears {count} times. Consider if this is intentional."
                )
            self.info.append(f"✓ Found $ARGUMENTS placeholder ({count} occurrence{'s' if count > 1 else ''})")

    def _check_required_sections(self):
        """Check for required sections."""
        required_sections = {
            '## Task': 'Task section defines what the command does',
            '## Process': 'Process section describes step-by-step execution'
        }

        for section, description in required_sections.items():
            if section not in self.content:
                self.errors.append(f"Missing required section: {section} ({description})")
            else:
                self.info.append(f"✓ Found {section}")

    def _check_heading_structure(self):
        """Check heading hierarchy and structure."""
        lines = self.content.split('\n')
        headings = []

        for i, line in enumerate(lines, 1):
            if line.strip().startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                text = line.strip('#').strip()
                headings.append((level, text, i))

        if not headings:
            self.errors.append("No headings found in document")
            return

        # Check first heading is H1
        if headings[0][0] != 1:
            self.warnings.append(f"First heading should be H1, got H{headings[0][0]}")

        # Check for heading hierarchy jumps
        for i in range(1, len(headings)):
            prev_level, curr_level = headings[i-1][0], headings[i][0]
            if curr_level > prev_level + 1:
                self.warnings.append(
                    f"Heading hierarchy jump from H{prev_level} to H{curr_level} at line {headings[i][2]}"
                )

        self.info.append(f"✓ Found {len(headings)} headings")

    def _check_process_steps(self):
        """Check Process section has numbered steps."""
        # Find Process section
        process_match = re.search(
            r'## Process\s*\n(.*?)(?=\n##|\Z)',
            self.content,
            re.DOTALL
        )

        if not process_match:
            return  # Already reported as missing section

        process_content = process_match.group(1)

        # Look for numbered list
        numbered_steps = re.findall(r'^\d+\.\s+.+', process_content, re.MULTILINE)

        if not numbered_steps:
            self.warnings.append(
                "Process section should contain numbered steps (1. 2. 3. ...)"
            )
        else:
            step_count = len(numbered_steps)
            if step_count < 3:
                self.warnings.append(
                    f"Process has only {step_count} step{'s' if step_count > 1 else ''}. "
                    "Consider breaking down into more detailed steps."
                )
            elif step_count > 10:
                self.warnings.append(
                    f"Process has {step_count} steps. Consider grouping or simplifying."
                )
            else:
                self.info.append(f"✓ Process has {step_count} well-defined steps")

    def _check_best_practices(self):
        """Check for best practices section and content quality."""
        # Check for Best Practices section
        if '## Best Practices' in self.content or '## Best practices' in self.content:
            self.info.append("✓ Includes Best Practices section")
        else:
            self.warnings.append(
                "Consider adding a Best Practices section for guidance"
            )

        # Check for adaptation statement
        adaptation_patterns = [
            r"I'll adapt",
            r"adapt to your",
            r"following.*(project|your).*patterns"
        ]

        has_adaptation = any(
            re.search(pattern, self.content, re.IGNORECASE)
            for pattern in adaptation_patterns
        )

        if has_adaptation:
            self.info.append("✓ Includes adaptation statement")
        else:
            self.warnings.append(
                "Consider ending with adaptation statement (e.g., \"I'll adapt to your project's patterns\")"
            )

        # Check for code examples
        code_blocks = len(re.findall(r'```', self.content))
        if code_blocks > 0:
            self.info.append(f"✓ Contains {code_blocks // 2} code block{'s' if code_blocks > 2 else ''}")

    def print_results(self):
        """Print validation results."""
        print()
        print("=" * 60)
        print("VALIDATION RESULTS")
        print("=" * 60)
        print()

        if self.errors:
            print("❌ ERRORS:")
            for error in self.errors:
                print(f"   • {error}")
            print()

        if self.warnings:
            print("⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"   • {warning}")
            print()

        if self.info:
            print("ℹ️  INFO:")
            for info_item in self.info:
                print(f"   {info_item}")
            print()

        print("=" * 60)

        if self.errors:
            print("❌ VALIDATION FAILED")
            print(f"   {len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        elif self.warnings:
            print("⚠️  VALIDATION PASSED WITH WARNINGS")
            print(f"   {len(self.warnings)} warning(s)")
        else:
            print("✅ VALIDATION PASSED")
            print("   No errors or warnings!")

        print()


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_command.py <path-to-command.md>")
        print("\nValidates command structure and format:")
        print("  • File naming conventions")
        print("  • Content structure and sections")
        print("  • $ARGUMENTS placeholder")
        print("  • Heading hierarchy")
        print("  • Process steps")
        print("  • Best practices")
        print("\nExamples:")
        print("  validate_command.py ~/.claude/commands/optimize-images.md")
        print("  validate_command.py .claude/commands/generate-component.md")
        sys.exit(1)

    file_path = sys.argv[1]

    validator = CommandValidator(file_path)
    is_valid = validator.validate()
    validator.print_results()

    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
