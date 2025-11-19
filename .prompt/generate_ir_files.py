#!/usr/bin/env python3
"""
IR File Generator for LibreChat

Generates complete IR (Intermediate Representation) files for every source file
using the 14-section template and dependency graph data.

Input:
  - .prompt/prompt-file-template.md
  - .prompt/dependency-graph.json

Output:
  - .prompt/ir/<path>.prompt.md for each source file
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import defaultdict


class IRGenerator:
    """Generates IR files from source files using template and dependency data."""

    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.ir_dir = self.repo_root / '.prompt' / 'ir'
        self.template_path = self.repo_root / '.prompt' / 'prompt-file-template.md'
        self.dep_graph_path = self.repo_root / '.prompt' / 'dependency-graph.json'

        self.template = None
        self.dep_graph = None
        self.files_processed = 0

        # File types to process (skip non-code files)
        self.processable_extensions = {
            '.js', '.jsx', '.ts', '.tsx', '.py', '.cs', '.go'
        }

    def load_data(self):
        """Load template and dependency graph."""
        print("Loading template...")
        with open(self.template_path, 'r', encoding='utf-8') as f:
            self.template = f.read()

        print("Loading dependency graph...")
        with open(self.dep_graph_path, 'r', encoding='utf-8') as f:
            self.dep_graph = json.load(f)

        print(f"✓ Loaded template and dependency graph ({len(self.dep_graph['files'])} files)")

    def should_process_file(self, file_path: str) -> bool:
        """Determine if file should have an IR generated."""
        path = Path(file_path)
        ext = path.suffix.lower()

        # Process code files
        if ext in self.processable_extensions:
            return True

        # Skip configuration and documentation files
        return False

    def generate_all_ir_files(self):
        """Generate IR files for all processable files."""
        print(f"\nGenerating IR files...")

        total_files = len(self.dep_graph['files'])
        processable_count = sum(
            1 for path in self.dep_graph['files'].keys()
            if self.should_process_file(path)
        )

        print(f"Total files in graph: {total_files}")
        print(f"Processable code files: {processable_count}\n")

        for file_path, file_info in self.dep_graph['files'].items():
            if not self.should_process_file(file_path):
                continue

            try:
                self.generate_ir_file(file_path, file_info)
                self.files_processed += 1

                if self.files_processed % 50 == 0:
                    print(f"  Generated {self.files_processed}/{processable_count} IR files...")

            except Exception as e:
                print(f"  Error generating IR for {file_path}: {e}")

        print(f"\n✓ Generated {self.files_processed} IR files")

    def generate_ir_file(self, file_path: str, file_info: Dict):
        """Generate a single IR file."""
        # Read source file
        source_path = self.repo_root / file_path
        try:
            with open(source_path, 'r', encoding='utf-8', errors='ignore') as f:
                source_content = f.read()
        except Exception as e:
            source_content = f"# Error reading file: {e}"

        # Generate IR content
        ir_content = self.populate_template(file_path, file_info, source_content)

        # Write IR file
        ir_file_path = self.ir_dir / f"{file_path}.prompt.md"
        ir_file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(ir_file_path, 'w', encoding='utf-8') as f:
            f.write(ir_content)

    def populate_template(self, file_path: str, file_info: Dict, source_content: str) -> str:
        """Populate the IR template with file-specific data."""

        # Section 1: Purpose
        purpose = self.generate_purpose(file_path, file_info, source_content)

        # Section 2: Domain Role
        domain_role = self.generate_domain_role(file_path, file_info)

        # Section 3: Public API
        public_api = self.generate_public_api(file_info, source_content)

        # Section 4: Internal Structure
        internal_structure = self.generate_internal_structure(file_info, source_content)

        # Section 5: Internal Behavior & Data Flow
        data_flow = self.generate_data_flow(file_path, file_info)

        # Section 6: Relationships & Collaboration
        relationships = self.generate_relationships(file_info)

        # Section 7: Database Interaction
        db_interaction = self.generate_db_interaction(file_path, file_info, source_content)

        # Section 8: UI Behavior
        ui_behavior = self.generate_ui_behavior(file_path, source_content)

        # Section 9: Key Logic Snippets
        key_logic = self.generate_key_logic(source_content, file_info)

        # Section 10: Architectural Concerns
        arch_concerns = self.generate_architectural_concerns(file_path, source_content)

        # Section 11: Migration Mapping
        migration_mapping = self.generate_migration_mapping(file_path)

        # Section 12: Migration Concerns
        migration_concerns = self.generate_migration_concerns(file_path, source_content)

        # Section 13: Dependencies
        dependencies_section = self.generate_dependencies(file_info)

        # Section 14: Tags
        tags = self.generate_tags(file_path, file_info)

        # Build complete IR document
        ir_content = f"""# File: {file_path}

# 1. Purpose
{purpose}

# 2. Domain Role
{domain_role}

# 3. Public API (FULL DETAIL)
{public_api}

# 4. Internal Structure
{internal_structure}

# 5. Internal Behavior & Data Flow
{data_flow}

# 6. Relationships & Collaboration
{relationships}

# 7. Database Interaction Mapping
{db_interaction}

# 8. UI Behavior (if applicable)
{ui_behavior}

# 9. Key Logic Snippets
{key_logic}

# 10. Architectural Concerns
{arch_concerns}

# 11. Migration Mapping (Legacy → Modern)
{migration_mapping}

# 12. Migration Concerns & Recommendations
{migration_concerns}

# 13. Dependencies
{dependencies_section}

# 14. Tags
{tags}
"""
        return ir_content

    def generate_purpose(self, file_path: str, file_info: Dict, source_content: str) -> str:
        """Generate Purpose section."""
        path = Path(file_path)
        file_type = file_info.get('type', 'unknown')

        # Determine file category
        if 'models' in path.parts or 'schema' in path.parts:
            category = "Data model / Database schema"
        elif 'controllers' in path.parts or 'routes' in path.parts:
            category = "API endpoint / Request handler"
        elif 'services' in path.parts:
            category = "Business logic service"
        elif 'components' in path.parts or file_path.endswith(('.tsx', '.jsx')):
            category = "UI component"
        elif 'hooks' in path.parts:
            category = "Custom React hook"
        elif 'utils' in path.parts or 'helpers' in path.parts:
            category = "Utility / Helper function"
        elif 'middleware' in path.parts:
            category = "Express middleware"
        elif 'store' in path.parts:
            category = "State management"
        elif 'types' in path.parts or file_path.endswith('.d.ts'):
            category = "TypeScript type definitions"
        else:
            category = "Application code"

        # Look for JSDoc/comments at the top
        doc_match = re.search(r'(?://|/\*\*?|\*|#)\s*(.+)', source_content[:500])
        doc_comment = doc_match.group(1).strip() if doc_match else ""

        purpose = f"""**File Type:** {file_type.upper()} ({category})

**What this file represents:**
This file is a {category.lower()} located at `{file_path}`.

"""

        if doc_comment:
            purpose += f"**Documentation:** {doc_comment}\n\n"

        # Add specific purpose based on exports
        exports = file_info.get('exports', [])
        if exports:
            purpose += f"**Primary exports:** {len(exports)} exported element(s)\n"
            for exp in exports[:3]:
                if isinstance(exp, dict):
                    exp_name = exp.get('name', exp.get('type', 'unknown'))
                    purpose += f"- {exp_name}\n"

        purpose += f"\n**File size:** {file_info.get('size_bytes', 0):,} bytes\n"

        return purpose

    def generate_domain_role(self, file_path: str, file_info: Dict) -> str:
        """Generate Domain Role section."""
        path = Path(file_path)

        # Determine domain based on path
        if 'agent' in file_path.lower():
            domain = "Agent Orchestration & Configuration"
        elif 'prompt' in file_path.lower():
            domain = "Prompt Management & Templating"
        elif 'conversation' in file_path.lower() or 'message' in file_path.lower():
            domain = "Chat & Conversation Management"
        elif 'auth' in file_path.lower() or 'user' in file_path.lower():
            domain = "Authentication & User Management"
        elif 'file' in file_path.lower() or 'upload' in file_path.lower():
            domain = "File Storage & Management"
        elif 'permission' in file_path.lower() or 'role' in file_path.lower():
            domain = "Authorization & Access Control"
        elif 'tool' in file_path.lower() or 'action' in file_path.lower():
            domain = "Tool & Action Execution"
        elif 'mcp' in file_path.lower():
            domain = "Model Context Protocol Integration"
        else:
            domain = "Application Logic"

        role = f"""**Domain:** {domain}

**Business relevance:**
This file is part of the {domain} domain within the LibreChat application.

"""

        # Add role-specific description
        if 'models' in path.parts:
            role += """**Role:** Data model definition
- Defines database schema using Mongoose
- Enforces data validation rules
- Provides data access methods
"""
        elif 'services' in path.parts:
            role += """**Role:** Business logic implementation
- Implements domain-specific operations
- Coordinates between data layer and API layer
- Enforces business rules and validation
"""
        elif 'components' in path.parts:
            role += """**Role:** User interface presentation
- Renders UI elements for user interaction
- Manages component-level state
- Handles user events and input
"""

        return role

    def generate_public_api(self, file_info: Dict, source_content: str) -> str:
        """Generate Public API section."""
        api = ""

        # Classes
        classes = file_info.get('classes', [])
        if classes:
            api += "### Classes\n\n"
            for cls in classes:
                if isinstance(cls, dict):
                    name = cls.get('name', 'Unknown')
                    extends = cls.get('extends', [])
                    if extends:
                        if isinstance(extends, list):
                            api += f"- `class {name} extends {', '.join(extends)}`\n"
                        else:
                            api += f"- `class {name} extends {extends}`\n"
                    else:
                        api += f"- `class {name}`\n"
            api += "\n"

        # Exported Functions
        exports = file_info.get('exports', [])
        functions = file_info.get('functions', [])

        if exports or functions:
            api += "### Exported Functions\n\n"

            for exp in exports:
                if isinstance(exp, dict):
                    exp_type = exp.get('type', '')
                    exp_name = exp.get('name', '')

                    if exp_type in ['named', 'default']:
                        # Try to find function signature in source
                        sig_pattern = rf"(?:export\s+)?(?:async\s+)?function\s+{re.escape(exp_name)}\s*\(([^)]*)\)"
                        sig_match = re.search(sig_pattern, source_content)

                        if sig_match:
                            params = sig_match.group(1)
                            api += f"- `{exp_name}({params})`"
                            if exp_type == 'default':
                                api += " — **default export**"
                            api += "\n"
                        else:
                            api += f"- `{exp_name}()` — {exp_type} export\n"

            api += "\n"

        if not classes and not exports and not functions:
            api += "*No public API exports detected.*\n"

        return api

    def generate_internal_structure(self, file_info: Dict, source_content: str) -> str:
        """Generate Internal Structure section."""
        structure = ""

        functions = file_info.get('functions', [])
        if functions:
            structure += f"### Internal Functions ({len(functions)})\n\n"
            for func in functions[:10]:  # Limit to first 10
                structure += f"- `{func}()`\n"
            if len(functions) > 10:
                structure += f"- *...and {len(functions) - 10} more functions*\n"
            structure += "\n"

        # Look for patterns
        patterns = []
        if re.search(r'useState|useEffect|useCallback', source_content):
            patterns.append("React Hooks pattern")
        if re.search(r'useQuery|useMutation', source_content):
            patterns.append("React Query data fetching")
        if re.search(r'Schema.*\.create|new Schema', source_content):
            patterns.append("Mongoose Schema definition")
        if re.search(r'express\(\)|Router\(\)', source_content):
            patterns.append("Express Router pattern")
        if re.search(r'class.*extends.*Component', source_content):
            patterns.append("React Class Component")

        if patterns:
            structure += "### Architectural Patterns\n\n"
            for pattern in patterns:
                structure += f"- {pattern}\n"
            structure += "\n"

        return structure if structure else "*No significant internal structure detected.*\n"

    def generate_data_flow(self, file_path: str, file_info: Dict) -> str:
        """Generate Data Flow section."""

        if 'components' in file_path or file_path.endswith(('.tsx', '.jsx')):
            return """### Data Flow Steps

1. **Input:** Props passed from parent component
2. **Transformations:** Component state updates via hooks
3. **External calls:** API calls via React Query hooks
4. **Output:** Rendered JSX with event handlers
"""
        elif 'controllers' in file_path or 'routes' in file_path:
            return """### Data Flow Steps

1. **Input:** HTTP request (req.body, req.params, req.query)
2. **Transformations:** Request validation and data extraction
3. **External calls:** Service layer methods, database queries
4. **Output:** HTTP response (res.json, res.status)
"""
        elif 'services' in file_path:
            return """### Data Flow Steps

1. **Input:** Parameters from controller/caller
2. **Transformations:** Business logic processing
3. **External calls:** Database models, external APIs
4. **Output:** Processed data or operation result
"""
        else:
            return """### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects
"""

    def generate_relationships(self, file_info: Dict) -> str:
        """Generate Relationships section."""
        relationships = ""

        # Imports
        imports = file_info.get('imports', [])
        if imports:
            relationships += f"### Imported Dependencies ({len(imports)})\n\n"

            # Group by type
            npm_imports = [imp for imp in imports if isinstance(imp, dict) and imp.get('resolved') == 'npm_package']
            relative_imports = [imp for imp in imports if isinstance(imp, dict) and imp.get('resolved') == 'relative']
            alias_imports = [imp for imp in imports if isinstance(imp, dict) and imp.get('resolved') == 'alias']

            if npm_imports:
                relationships += "**NPM Packages:**\n"
                for imp in npm_imports[:10]:
                    relationships += f"- `{imp.get('module', 'unknown')}`\n"
                if len(npm_imports) > 10:
                    relationships += f"- *...and {len(npm_imports) - 10} more*\n"
                relationships += "\n"

            if relative_imports:
                relationships += "**Relative Imports:**\n"
                for imp in relative_imports[:10]:
                    relationships += f"- `{imp.get('module', 'unknown')}`\n"
                if len(relative_imports) > 10:
                    relationships += f"- *...and {len(relative_imports) - 10} more*\n"
                relationships += "\n"

            if alias_imports:
                relationships += "**Aliased Imports:**\n"
                for imp in alias_imports[:10]:
                    relationships += f"- `{imp.get('module', 'unknown')}`\n"
                if len(alias_imports) > 10:
                    relationships += f"- *...and {len(alias_imports) - 10} more*\n"
                relationships += "\n"

        # Dependents
        dependents = file_info.get('dependents', [])
        if dependents:
            relationships += f"### Used By ({len(dependents)} files)\n\n"
            for dep in dependents[:5]:
                relationships += f"- `{dep}`\n"
            if len(dependents) > 5:
                relationships += f"- *...and {len(dependents) - 5} more files*\n"
            relationships += "\n"

        return relationships if relationships else "*No relationship data available.*\n"

    def generate_db_interaction(self, file_path: str, file_info: Dict, source_content: str) -> str:
        """Generate Database Interaction section."""

        # Check for Mongoose patterns
        if re.search(r'Schema|mongoose\.model|Model\.find|Model\.create', source_content):
            db = "**Database:** MongoDB via Mongoose\n\n"

            # Find model references
            model_refs = re.findall(r'(?:mongoose\.model|Model)\([\'"](\w+)[\'"]', source_content)
            if model_refs:
                db += "**Models referenced:**\n"
                for model in set(model_refs):
                    db += f"- {model}\n"
                db += "\n"

            # Find query patterns
            if re.search(r'\.find\(|\.findOne\(|\.findById\(', source_content):
                db += "**Operations:** SELECT (find, findOne, findById)\n"
            if re.search(r'\.create\(|\.insertMany\(', source_content):
                db += "**Operations:** INSERT (create, insertMany)\n"
            if re.search(r'\.updateOne\(|\.updateMany\(|\.findByIdAndUpdate\(', source_content):
                db += "**Operations:** UPDATE (updateOne, findByIdAndUpdate)\n"
            if re.search(r'\.deleteOne\(|\.deleteMany\(|\.findByIdAndDelete\(', source_content):
                db += "**Operations:** DELETE (deleteOne, findByIdAndDelete)\n"

            return db

        return "**No direct database interaction.**\n"

    def generate_ui_behavior(self, file_path: str, source_content: str) -> str:
        """Generate UI Behavior section."""

        if not file_path.endswith(('.tsx', '.jsx')):
            return "**No UI behavior.** (Not a UI component)\n"

        ui = "**UI Component:** React component\n\n"

        # React hooks
        hooks_used = []
        if 'useState' in source_content:
            hooks_used.append('useState')
        if 'useEffect' in source_content:
            hooks_used.append('useEffect')
        if 'useCallback' in source_content:
            hooks_used.append('useCallback')
        if 'useMemo' in source_content:
            hooks_used.append('useMemo')
        if 'useContext' in source_content:
            hooks_used.append('useContext')
        if 'useQuery' in source_content:
            hooks_used.append('useQuery (React Query)')
        if 'useMutation' in source_content:
            hooks_used.append('useMutation (React Query)')

        if hooks_used:
            ui += "**React Hooks:**\n"
            for hook in hooks_used:
                ui += f"- {hook}\n"
            ui += "\n"

        # Event handlers
        event_handlers = re.findall(r'on\w+\s*=\s*\{', source_content)
        if event_handlers:
            ui += f"**Event Handlers:** {len(set(event_handlers))} event handler(s) detected\n\n"

        # Form handling
        if 'react-hook-form' in source_content or 'useForm' in source_content:
            ui += "**Form Management:** React Hook Form\n\n"

        return ui

    def generate_key_logic(self, source_content: str, file_info: Dict) -> str:
        """Generate Key Logic Snippets section."""

        # Extract meaningful code blocks (functions, classes, etc.)
        snippets = []

        # Find function definitions with some logic
        func_pattern = r'(?:export\s+)?(?:async\s+)?(?:function|const)\s+\w+[^{]*\{([^}]{50,500})\}'
        matches = re.finditer(func_pattern, source_content, re.DOTALL)

        for match in matches:
            body = match.group(1).strip()
            # Skip trivial functions
            if len(body) > 50 and ('if' in body or 'return' in body or 'for' in body):
                snippets.append(body[:300])  # Limit snippet size
                if len(snippets) >= 3:  # Max 3 snippets
                    break

        if snippets:
            logic = "**Key logic excerpts:**\n\n"
            for i, snippet in enumerate(snippets, 1):
                # Detect language
                file_type = file_info.get('type', 'javascript')
                if file_type in ['ts', 'tsx']:
                    lang = 'typescript'
                elif file_type in ['js', 'jsx']:
                    lang = 'javascript'
                else:
                    lang = file_type

                logic += f"**Snippet {i}:**\n```{lang}\n{snippet}\n```\n\n"
            return logic

        return "*No significant logic snippets extracted. See full source file for implementation details.*\n"

    def generate_architectural_concerns(self, file_path: str, source_content: str) -> str:
        """Generate Architectural Concerns section."""
        concerns = []

        # Security
        if re.search(r'password|token|secret|auth|jwt', source_content, re.IGNORECASE):
            concerns.append("**Security:** Handles sensitive data (passwords, tokens, authentication)")

        # Error handling
        if re.search(r'try\s*\{|catch\s*\(', source_content):
            concerns.append("**Error Handling:** Uses try-catch blocks")

        # Async operations
        if re.search(r'async|await|Promise', source_content):
            concerns.append("**Async Behavior:** Asynchronous operations present")

        # Logging
        if re.search(r'console\.log|logger\.|winston', source_content):
            concerns.append("**Logging:** Contains logging statements")

        # Performance
        if re.search(r'useMemo|useCallback|React\.memo', source_content):
            concerns.append("**Performance:** Optimized with memoization")

        if concerns:
            return "\n".join(concerns) + "\n"

        return "*No specific architectural concerns identified.*\n"

    def generate_migration_mapping(self, file_path: str) -> str:
        """Generate Migration Mapping section."""
        path = Path(file_path)

        mapping = "### Target Location in Modern System\n\n"

        if 'api' in path.parts:
            if 'models' in path.parts:
                mapping += "**Backend:** Database model\n"
                mapping += f"- Service: Data layer\n"
                mapping += f"- Repository: `{path.stem}` model\n"
            elif 'controllers' in path.parts:
                mapping += "**Backend:** API controller\n"
                mapping += f"- Service: API layer\n"
                mapping += f"- Controller: `{path.stem}Controller`\n"
            elif 'services' in path.parts:
                mapping += "**Backend:** Business logic service\n"
                mapping += f"- Service: Business logic layer\n"
                mapping += f"- Module: `{path.stem}Service`\n"
            else:
                mapping += "**Backend:** Backend code\n"

        elif 'client' in path.parts:
            if 'components' in path.parts:
                mapping += "**Frontend:** UI component\n"
                mapping += f"- Component: `{path.stem}`\n"
            elif 'store' in path.parts:
                mapping += "**Frontend:** State management\n"
                mapping += f"- Store: `{path.stem}` atom/state\n"
            else:
                mapping += "**Frontend:** Frontend code\n"

        elif 'packages' in path.parts:
            mapping += "**Shared:** Shared package code\n"

        return mapping

    def generate_migration_concerns(self, file_path: str, source_content: str) -> str:
        """Generate Migration Concerns section."""
        concerns = []

        # Check for technical debt markers
        if re.search(r'TODO|FIXME|HACK|XXX', source_content):
            concerns.append("- Contains TODO/FIXME comments indicating technical debt")

        # Check for deprecated patterns
        if re.search(r'deprecated|legacy', source_content, re.IGNORECASE):
            concerns.append("- May contain deprecated or legacy code patterns")

        # Check for complex logic
        if source_content.count('if') > 10:
            concerns.append("- Contains complex conditional logic that may need review")

        if concerns:
            return "\n".join(concerns) + "\n"

        return "*No major migration concerns identified. Standard migration process should apply.*\n"

    def generate_dependencies(self, file_info: Dict) -> str:
        """Generate Dependencies section."""
        deps = ""

        # dependsOn
        dependencies = file_info.get('dependencies', [])
        if dependencies:
            deps += f"### dependsOn ({len(dependencies)})\n\n"
            for dep in dependencies[:20]:  # Limit to 20
                deps += f"- `{dep}`\n"
            if len(dependencies) > 20:
                deps += f"- *...and {len(dependencies) - 20} more*\n"
            deps += "\n"

        # usedBy
        dependents = file_info.get('dependents', [])
        if dependents:
            deps += f"### usedBy ({len(dependents)})\n\n"
            for dep in dependents[:20]:  # Limit to 20
                deps += f"- `{dep}`\n"
            if len(dependents) > 20:
                deps += f"- *...and {len(dependents) - 20} more*\n"
            deps += "\n"

        return deps if deps else "*No dependency information available.*\n"

    def generate_tags(self, file_path: str, file_info: Dict) -> str:
        """Generate Tags section."""
        tags = []
        path = Path(file_path)

        # File type tags
        file_type = file_info.get('type', '')
        if file_type in ['ts', 'tsx']:
            tags.append('typescript')
        elif file_type in ['js', 'jsx']:
            tags.append('javascript')
        elif file_type == 'py':
            tags.append('python')

        # Location-based tags
        if 'models' in path.parts or 'schema' in path.parts:
            tags.append('domain-model')
        if 'controllers' in path.parts:
            tags.append('controller')
        if 'services' in path.parts:
            tags.append('service')
            tags.append('business-logic')
        if 'routes' in path.parts:
            tags.append('api-endpoint')
        if 'components' in path.parts:
            tags.append('ui-component')
        if 'hooks' in path.parts:
            tags.append('react-hook')
        if 'store' in path.parts:
            tags.append('state-management')
        if 'middleware' in path.parts:
            tags.append('middleware')
        if 'utils' in path.parts or 'helpers' in path.parts:
            tags.append('utility')

        # Domain tags
        if 'agent' in file_path.lower():
            tags.append('agent-orchestration')
        if 'prompt' in file_path.lower():
            tags.append('prompt-management')
        if 'auth' in file_path.lower():
            tags.append('authentication')
        if 'permission' in file_path.lower() or 'role' in file_path.lower():
            tags.append('authorization')
        if 'conversation' in file_path.lower() or 'message' in file_path.lower():
            tags.append('conversation-management')
        if 'tool' in file_path.lower() or 'action' in file_path.lower():
            tags.append('tool-execution')
        if 'mcp' in file_path.lower():
            tags.append('mcp-integration')
        if 'file' in file_path.lower():
            tags.append('file-storage')

        # Ensure at least 5 tags
        if len(tags) < 5:
            tags.extend(['application-code', 'librechat', 'source-file'])

        # Remove duplicates and limit to 12
        tags = list(dict.fromkeys(tags))[:12]

        return "```\n" + "\n".join(f"- {tag}" for tag in tags) + "\n```\n"


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    print("=== LibreChat IR File Generator ===\n")

    generator = IRGenerator(str(repo_root))
    generator.load_data()
    generator.generate_all_ir_files()

    # Count generated files
    ir_files = list(generator.ir_dir.glob('**/*.prompt.md'))
    print(f"\n✓ Complete! Generated {len(ir_files)} IR files in .prompt/ir/")

    return 0


if __name__ == '__main__':
    exit(main())
