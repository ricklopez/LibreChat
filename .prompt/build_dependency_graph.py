#!/usr/bin/env python3
"""
LibreChat Dependency Graph Builder

Scans the entire repository and extracts:
- Imports/requires
- Exports
- Class definitions and references
- Function definitions
- Identifier references
- Inheritance relationships
- File relationships

Outputs: .prompt/dependency-graph.json
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Any
from collections import defaultdict

# Directories to exclude from scanning
EXCLUDE_DIRS = {
    'node_modules', '.git', 'dist', 'build', '.next', '__pycache__',
    'coverage', '.cache', '.vscode', '.idea', 'vendor', 'bin', 'obj',
    '.pytest_cache', '.mypy_cache', 'venv', 'env'
}

# File extensions to scan
FILE_EXTENSIONS = {
    '.js', '.jsx', '.ts', '.tsx', '.py', '.cs', '.go', '.sql',
    '.yaml', '.yml', '.html', '.json', '.md', '.sh', '.css',
    '.java', '.rb', '.php', '.swift', '.kt', '.rs'
}


class DependencyGraphBuilder:
    """Builds a comprehensive dependency graph for the repository."""

    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.graph = {
            'metadata': {
                'repo_root': str(self.repo_root),
                'total_files': 0,
                'file_types': {},
                'generated_at': None
            },
            'files': {}
        }
        self.file_types_count = defaultdict(int)

    def should_exclude_path(self, path: Path) -> bool:
        """Check if path should be excluded from scanning."""
        parts = path.parts
        return any(excluded in parts for excluded in EXCLUDE_DIRS)

    def scan_repository(self):
        """Scan the entire repository and build the dependency graph."""
        print(f"Scanning repository: {self.repo_root}")

        total_files = 0
        for root, dirs, files in os.walk(self.repo_root):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            root_path = Path(root)
            if self.should_exclude_path(root_path):
                continue

            for filename in files:
                file_path = root_path / filename
                ext = file_path.suffix.lower()

                if ext in FILE_EXTENSIONS:
                    rel_path = file_path.relative_to(self.repo_root)
                    total_files += 1
                    self.file_types_count[ext] += 1

                    if total_files % 100 == 0:
                        print(f"  Processed {total_files} files...")

                    try:
                        file_info = self.analyze_file(file_path, rel_path)
                        self.graph['files'][str(rel_path)] = file_info
                    except Exception as e:
                        print(f"  Error processing {rel_path}: {e}")

        print(f"✓ Scanned {total_files} files")

        # Update metadata
        self.graph['metadata']['total_files'] = total_files
        self.graph['metadata']['file_types'] = dict(self.file_types_count)

        # Import datetime here to set timestamp
        from datetime import datetime
        self.graph['metadata']['generated_at'] = datetime.now().isoformat()

    def analyze_file(self, file_path: Path, rel_path: Path) -> Dict[str, Any]:
        """Analyze a single file and extract dependencies."""
        ext = file_path.suffix.lower()

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            return {
                'type': ext[1:],
                'error': str(e),
                'size_bytes': 0
            }

        file_info = {
            'type': ext[1:],
            'size_bytes': len(content),
            'imports': [],
            'exports': [],
            'classes': [],
            'functions': [],
            'identifiers': [],
            'dependencies': [],
            'dependents': []  # Will be populated in post-processing
        }

        # Route to appropriate analyzer based on file extension
        if ext in {'.js', '.jsx', '.ts', '.tsx'}:
            self.analyze_javascript_typescript(content, file_info)
        elif ext == '.py':
            self.analyze_python(content, file_info)
        elif ext == '.cs':
            self.analyze_csharp(content, file_info)
        elif ext == '.go':
            self.analyze_go(content, file_info)
        elif ext == '.sql':
            self.analyze_sql(content, file_info)
        elif ext in {'.yaml', '.yml'}:
            self.analyze_yaml(content, file_info)
        elif ext == '.html':
            self.analyze_html(content, file_info)
        elif ext == '.json':
            self.analyze_json(content, file_info, file_path)

        return file_info

    def analyze_javascript_typescript(self, content: str, file_info: Dict):
        """Extract dependencies from JavaScript/TypeScript files."""

        # ES6 imports: import X from 'module'
        es6_imports = re.finditer(
            r'import\s+(?:(?:\{[^}]+\})|(?:\*\s+as\s+\w+)|(?:\w+))\s+from\s+[\'"]([^"\']+)[\'"]',
            content
        )
        for match in es6_imports:
            module = match.group(1)
            file_info['imports'].append({
                'type': 'es6_import',
                'module': module,
                'resolved': self.resolve_import_path(module)
            })
            if not module.startswith('.'):
                file_info['dependencies'].append(module)

        # Dynamic imports: import('module')
        dynamic_imports = re.finditer(r'import\s*\(\s*[\'"]([^"\']+)[\'"]\s*\)', content)
        for match in dynamic_imports:
            module = match.group(1)
            file_info['imports'].append({
                'type': 'dynamic_import',
                'module': module,
                'resolved': self.resolve_import_path(module)
            })

        # CommonJS require: require('module')
        require_imports = re.finditer(r'require\s*\(\s*[\'"]([^"\']+)[\'"]\s*\)', content)
        for match in require_imports:
            module = match.group(1)
            file_info['imports'].append({
                'type': 'require',
                'module': module,
                'resolved': self.resolve_import_path(module)
            })
            if not module.startswith('.'):
                file_info['dependencies'].append(module)

        # Named exports: export const X, export function Y, export class Z
        named_exports = re.finditer(
            r'export\s+(?:const|let|var|function|class|interface|type|enum)\s+(\w+)',
            content
        )
        for match in named_exports:
            file_info['exports'].append({
                'type': 'named',
                'name': match.group(1)
            })

        # Default exports: export default X
        default_exports = re.finditer(r'export\s+default\s+(\w+)', content)
        for match in default_exports:
            file_info['exports'].append({
                'type': 'default',
                'name': match.group(1)
            })

        # Re-exports: export { X } from 'module'
        re_exports = re.finditer(r'export\s+\{[^}]+\}\s+from\s+[\'"]([^"\']+)[\'"]', content)
        for match in re_exports:
            module = match.group(1)
            file_info['exports'].append({
                'type': 're-export',
                'from': module
            })

        # Class definitions
        class_defs = re.finditer(
            r'(?:export\s+)?class\s+(\w+)(?:\s+extends\s+(\w+))?',
            content
        )
        for match in class_defs:
            class_name = match.group(1)
            extends_class = match.group(2)
            class_info = {'name': class_name}
            if extends_class:
                class_info['extends'] = extends_class
            file_info['classes'].append(class_info)

        # Function definitions
        func_defs = re.finditer(
            r'(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\(',
            content
        )
        for match in func_defs:
            file_info['functions'].append(match.group(1))

        # Arrow functions assigned to const/let/var
        arrow_funcs = re.finditer(
            r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\([^)]*\)\s*=>',
            content
        )
        for match in arrow_funcs:
            file_info['functions'].append(match.group(1))

    def analyze_python(self, content: str, file_info: Dict):
        """Extract dependencies from Python files."""

        # Import statements: import module, import module as alias
        imports = re.finditer(r'^\s*import\s+([\w.]+)(?:\s+as\s+\w+)?', content, re.MULTILINE)
        for match in imports:
            module = match.group(1)
            file_info['imports'].append({
                'type': 'import',
                'module': module
            })
            file_info['dependencies'].append(module)

        # From imports: from module import X
        from_imports = re.finditer(
            r'^\s*from\s+([\w.]+)\s+import\s+([^#\n]+)',
            content,
            re.MULTILINE
        )
        for match in from_imports:
            module = match.group(1)
            imports_str = match.group(2)
            file_info['imports'].append({
                'type': 'from_import',
                'module': module,
                'items': imports_str.strip()
            })
            file_info['dependencies'].append(module)

        # Class definitions with inheritance
        class_defs = re.finditer(
            r'^\s*class\s+(\w+)(?:\(([^)]+)\))?:',
            content,
            re.MULTILINE
        )
        for match in class_defs:
            class_name = match.group(1)
            base_classes = match.group(2)
            class_info = {'name': class_name}
            if base_classes:
                bases = [b.strip() for b in base_classes.split(',')]
                class_info['extends'] = bases
            file_info['classes'].append(class_info)

        # Function definitions
        func_defs = re.finditer(
            r'^\s*(?:async\s+)?def\s+(\w+)\s*\(',
            content,
            re.MULTILINE
        )
        for match in func_defs:
            file_info['functions'].append(match.group(1))

    def analyze_csharp(self, content: str, file_info: Dict):
        """Extract dependencies from C# files."""

        # Using statements
        usings = re.finditer(r'^\s*using\s+([\w.]+);', content, re.MULTILINE)
        for match in usings:
            namespace = match.group(1)
            file_info['imports'].append({
                'type': 'using',
                'namespace': namespace
            })
            file_info['dependencies'].append(namespace)

        # Class definitions with inheritance
        class_defs = re.finditer(
            r'(?:public|private|protected|internal)?\s*(?:abstract|sealed|static)?\s*class\s+(\w+)(?:\s*:\s*([^{]+))?',
            content
        )
        for match in class_defs:
            class_name = match.group(1)
            inheritance = match.group(2)
            class_info = {'name': class_name}
            if inheritance:
                bases = [b.strip() for b in inheritance.split(',')]
                class_info['extends'] = bases
            file_info['classes'].append(class_info)

        # Method definitions
        method_defs = re.finditer(
            r'(?:public|private|protected|internal)\s+(?:static\s+)?(?:async\s+)?[\w<>[\]]+\s+(\w+)\s*\(',
            content
        )
        for match in method_defs:
            file_info['functions'].append(match.group(1))

    def analyze_go(self, content: str, file_info: Dict):
        """Extract dependencies from Go files."""

        # Import statements
        # Single import
        single_imports = re.finditer(r'^\s*import\s+"([^"]+)"', content, re.MULTILINE)
        for match in single_imports:
            package = match.group(1)
            file_info['imports'].append({
                'type': 'import',
                'package': package
            })
            file_info['dependencies'].append(package)

        # Multi-line imports
        import_blocks = re.finditer(
            r'import\s+\((.*?)\)',
            content,
            re.DOTALL
        )
        for match in import_blocks:
            imports_str = match.group(1)
            for line in imports_str.split('\n'):
                pkg_match = re.search(r'"([^"]+)"', line)
                if pkg_match:
                    package = pkg_match.group(1)
                    file_info['imports'].append({
                        'type': 'import',
                        'package': package
                    })
                    file_info['dependencies'].append(package)

        # Struct definitions
        struct_defs = re.finditer(r'type\s+(\w+)\s+struct\s*\{', content)
        for match in struct_defs:
            file_info['classes'].append({'name': match.group(1), 'type': 'struct'})

        # Interface definitions
        interface_defs = re.finditer(r'type\s+(\w+)\s+interface\s*\{', content)
        for match in interface_defs:
            file_info['classes'].append({'name': match.group(1), 'type': 'interface'})

        # Function definitions
        func_defs = re.finditer(r'func\s+(?:\([^)]+\)\s+)?(\w+)\s*\(', content)
        for match in func_defs:
            file_info['functions'].append(match.group(1))

    def analyze_sql(self, content: str, file_info: Dict):
        """Extract dependencies from SQL files."""

        # Table references in FROM, JOIN
        table_refs = re.finditer(
            r'\b(?:FROM|JOIN)\s+([`\[\]"\'.\w]+)',
            content,
            re.IGNORECASE
        )
        tables = set()
        for match in table_refs:
            table = match.group(1).strip('`"\'[]')
            tables.add(table)

        file_info['identifiers'] = list(tables)

        # CREATE TABLE statements
        create_tables = re.finditer(
            r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([`\[\]"\'.\w]+)',
            content,
            re.IGNORECASE
        )
        for match in create_tables:
            table = match.group(1).strip('`"\'[]')
            file_info['exports'].append({
                'type': 'table',
                'name': table
            })

    def analyze_yaml(self, content: str, file_info: Dict):
        """Extract dependencies from YAML files."""

        # Look for image references (Docker)
        image_refs = re.finditer(r'image:\s*["\']?([^\s"\']+)', content)
        for match in image_refs:
            file_info['dependencies'].append(match.group(1))

        # Look for file references
        file_refs = re.finditer(r'(?:file|path|from):\s*["\']?([^\s"\']+)', content)
        for match in file_refs:
            ref = match.group(1)
            if '.' in ref:
                file_info['identifiers'].append(ref)

    def analyze_html(self, content: str, file_info: Dict):
        """Extract dependencies from HTML files."""

        # Script src
        script_refs = re.finditer(r'<script[^>]+src=["\'"]([^"\']+)', content, re.IGNORECASE)
        for match in script_refs:
            file_info['dependencies'].append(match.group(1))

        # Link href (CSS, etc.)
        link_refs = re.finditer(r'<link[^>]+href=["\'"]([^"\']+)', content, re.IGNORECASE)
        for match in link_refs:
            file_info['dependencies'].append(match.group(1))

        # Img src
        img_refs = re.finditer(r'<img[^>]+src=["\'"]([^"\']+)', content, re.IGNORECASE)
        for match in img_refs:
            file_info['identifiers'].append(match.group(1))

    def analyze_json(self, content: str, file_info: Dict, file_path: Path):
        """Extract dependencies from JSON files."""

        try:
            data = json.loads(content)

            # package.json specific analysis
            if file_path.name == 'package.json':
                if 'dependencies' in data:
                    for dep in data['dependencies'].keys():
                        file_info['dependencies'].append(dep)
                if 'devDependencies' in data:
                    for dep in data['devDependencies'].keys():
                        file_info['dependencies'].append(dep)

            # tsconfig.json paths
            if file_path.name.startswith('tsconfig'):
                if 'extends' in data:
                    file_info['dependencies'].append(data['extends'])

        except json.JSONDecodeError:
            pass

    def resolve_import_path(self, module_path: str) -> str:
        """Resolve import path to file type (relative, npm, alias)."""
        if module_path.startswith('.'):
            return 'relative'
        elif module_path.startswith('@/'):
            return 'alias'
        elif module_path.startswith('~'):
            return 'alias'
        else:
            return 'npm_package'

    def build_reverse_dependencies(self):
        """Build reverse dependency mapping (dependents)."""
        print("Building reverse dependencies...")

        for file_path, file_info in self.graph['files'].items():
            for dep in file_info.get('dependencies', []):
                # Find files that export this dependency
                for other_file, other_info in self.graph['files'].items():
                    if other_file == file_path:
                        continue

                    # Check if other_file exports this dependency
                    exports = other_info.get('exports', [])
                    for export in exports:
                        if isinstance(export, dict):
                            if export.get('name') == dep or export.get('module') == dep:
                                if file_path not in other_info['dependents']:
                                    other_info['dependents'].append(file_path)

    def generate_statistics(self) -> Dict[str, Any]:
        """Generate graph statistics."""
        stats = {
            'total_files': len(self.graph['files']),
            'total_imports': 0,
            'total_exports': 0,
            'total_classes': 0,
            'total_functions': 0,
            'files_by_type': defaultdict(int),
            'top_dependencies': defaultdict(int),
            'top_dependents': defaultdict(int)
        }

        for file_path, file_info in self.graph['files'].items():
            file_type = file_info.get('type', 'unknown')
            stats['files_by_type'][file_type] += 1
            stats['total_imports'] += len(file_info.get('imports', []))
            stats['total_exports'] += len(file_info.get('exports', []))
            stats['total_classes'] += len(file_info.get('classes', []))
            stats['total_functions'] += len(file_info.get('functions', []))

            # Track most imported packages
            for dep in file_info.get('dependencies', []):
                stats['top_dependencies'][dep] += 1

            # Track files with most dependents
            dependents_count = len(file_info.get('dependents', []))
            if dependents_count > 0:
                stats['top_dependents'][file_path] = dependents_count

        # Convert defaultdicts to regular dicts and sort
        stats['files_by_type'] = dict(stats['files_by_type'])
        stats['top_dependencies'] = dict(sorted(
            stats['top_dependencies'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:50])  # Top 50
        stats['top_dependents'] = dict(sorted(
            stats['top_dependents'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:50])  # Top 50

        return stats

    def save_graph(self, output_path: str):
        """Save the dependency graph to JSON file."""
        output_file = Path(output_path)

        print(f"Generating statistics...")
        self.graph['statistics'] = self.generate_statistics()

        print(f"Writing graph to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.graph, f, indent=2)

        file_size_mb = output_file.stat().st_size / (1024 * 1024)
        print(f"✓ Dependency graph saved: {output_file} ({file_size_mb:.2f} MB)")

        # Print statistics
        stats = self.graph['statistics']
        print(f"\n=== Dependency Graph Statistics ===")
        print(f"Total files: {stats['total_files']}")
        print(f"Total imports: {stats['total_imports']}")
        print(f"Total exports: {stats['total_exports']}")
        print(f"Total classes: {stats['total_classes']}")
        print(f"Total functions: {stats['total_functions']}")
        print(f"\nFiles by type:")
        for file_type, count in sorted(stats['files_by_type'].items(), key=lambda x: x[1], reverse=True):
            print(f"  .{file_type}: {count}")
        print(f"\nTop 10 dependencies:")
        for dep, count in list(stats['top_dependencies'].items())[:10]:
            print(f"  {dep}: {count} files")


def main():
    """Main entry point."""
    import sys

    # Determine repository root (parent of .prompt directory)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    print(f"=== LibreChat Dependency Graph Builder ===\n")

    builder = DependencyGraphBuilder(str(repo_root))
    builder.scan_repository()
    builder.build_reverse_dependencies()

    output_path = script_dir / 'dependency-graph.json'
    builder.save_graph(str(output_path))

    print(f"\n✓ Complete! Graph saved to: {output_path}")
    return 0


if __name__ == '__main__':
    exit(main())
