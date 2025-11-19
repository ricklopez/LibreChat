#!/usr/bin/env python3
"""
Semantic Index Generator for LibreChat

Analyzes all IR files to generate:
- Domain clusters
- Dependency cycle detection
- System architecture mapping
- Priority groups for migration
- File index by category
- Migration grouping strategy
- Database schema extraction

Input: .prompt/ir/**/*.prompt.md
Output: .prompt/semantic-index.md
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Any, Tuple
from collections import defaultdict, Counter
import json


class SemanticIndexGenerator:
    """Generates semantic index from IR files."""

    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.ir_dir = self.repo_root / '.prompt' / 'ir'
        self.dep_graph_path = self.repo_root / '.prompt' / 'dependency-graph.json'
        self.output_path = self.repo_root / '.prompt' / 'semantic-index.md'

        self.ir_files = {}  # path -> parsed IR content
        self.dep_graph = None
        self.domain_clusters = defaultdict(list)
        self.dependency_cycles = []
        self.architecture_map = {}
        self.priority_groups = {}
        self.migration_groups = {}
        self.database_schemas = {}

    def load_dependency_graph(self):
        """Load the dependency graph."""
        print("Loading dependency graph...")
        with open(self.dep_graph_path, 'r', encoding='utf-8') as f:
            self.dep_graph = json.load(f)
        print(f"✓ Loaded dependency graph")

    def load_ir_files(self):
        """Load and parse all IR files."""
        print("\nLoading IR files...")

        ir_files = list(self.ir_dir.glob('**/*.prompt.md'))
        total = len(ir_files)

        for idx, ir_file in enumerate(ir_files, 1):
            if idx % 100 == 0:
                print(f"  Loaded {idx}/{total} IR files...")

            rel_path = ir_file.relative_to(self.ir_dir)
            # Remove .prompt.md suffix to get original file path
            source_path = str(rel_path)[:-10]  # Remove '.prompt.md'

            try:
                with open(ir_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                parsed = self.parse_ir_file(content, source_path)
                self.ir_files[source_path] = parsed

            except Exception as e:
                print(f"  Error loading {ir_file}: {e}")

        print(f"✓ Loaded {len(self.ir_files)} IR files")

    def parse_ir_file(self, content: str, source_path: str) -> Dict[str, Any]:
        """Parse IR file content into structured data."""
        data = {
            'source_path': source_path,
            'purpose': '',
            'domain': '',
            'tags': [],
            'dependencies': [],
            'dependents': [],
            'classes': [],
            'functions': [],
            'database_models': [],
            'api_endpoints': [],
            'ui_components': [],
            'migration_priority': 'medium'
        }

        # Extract Purpose section
        purpose_match = re.search(r'# 1\. Purpose\s+(.+?)(?=\n# 2\.)', content, re.DOTALL)
        if purpose_match:
            data['purpose'] = purpose_match.group(1).strip()[:500]  # Limit to 500 chars

        # Extract Domain Role section
        domain_match = re.search(r'# 2\. Domain Role\s+(.+?)(?=\n# 3\.)', content, re.DOTALL)
        if domain_match:
            domain_text = domain_match.group(1)
            # Extract domain name
            domain_name_match = re.search(r'\*\*Domain:\*\*\s+([^\n]+)', domain_text)
            if domain_name_match:
                data['domain'] = domain_name_match.group(1).strip()

        # Extract Tags section
        tags_match = re.search(r'# 14\. Tags\s+```\s+(.*?)\s+```', content, re.DOTALL)
        if tags_match:
            tags_text = tags_match.group(1)
            tags = re.findall(r'-\s+(.+)', tags_text)
            data['tags'] = [tag.strip() for tag in tags]

        # Extract Dependencies section
        deps_match = re.search(r'# 13\. Dependencies\s+(.+?)(?=\n# 14\.)', content, re.DOTALL)
        if deps_match:
            deps_text = deps_match.group(1)

            # dependsOn
            depends_on_match = re.search(r'### dependsOn.*?\n(.*?)(?=###|$)', deps_text, re.DOTALL)
            if depends_on_match:
                deps = re.findall(r'-\s+`([^`]+)`', depends_on_match.group(1))
                data['dependencies'] = deps

            # usedBy
            used_by_match = re.search(r'### usedBy.*?\n(.*?)(?=###|$)', deps_text, re.DOTALL)
            if used_by_match:
                deps = re.findall(r'-\s+`([^`]+)`', used_by_match.group(1))
                data['dependents'] = deps

        # Extract Public API section for classes/functions
        api_match = re.search(r'# 3\. Public API.*?\n(.+?)(?=\n# 4\.)', content, re.DOTALL)
        if api_match:
            api_text = api_match.group(1)

            # Extract classes
            classes = re.findall(r'-\s+`class\s+(\w+)', api_text)
            data['classes'] = classes

            # Extract functions
            functions = re.findall(r'-\s+`(\w+)\([^)]*\)', api_text)
            data['functions'] = functions

        # Detect database models (Mongoose schemas)
        if 'domain-model' in data['tags'] or 'models' in source_path:
            # Try to extract model name from file path
            model_match = re.search(r'models/(\w+)\.', source_path)
            if model_match:
                data['database_models'].append(model_match.group(1))

        # Detect API endpoints
        if 'api-endpoint' in data['tags'] or 'controller' in data['tags']:
            # Extract endpoint info from purpose/domain
            if 'api/' in source_path and 'routes' in source_path:
                route_match = re.search(r'routes/(\w+)', source_path)
                if route_match:
                    data['api_endpoints'].append(route_match.group(1))

        # Detect UI components
        if 'ui-component' in data['tags'] or 'react' in source_path.lower():
            component_match = re.search(r'components/([^/]+?)(?:\.tsx|\.jsx|/)', source_path)
            if component_match:
                data['ui_components'].append(component_match.group(1))

        # Compute migration priority
        data['migration_priority'] = self.compute_migration_priority(data, source_path)

        return data

    def compute_migration_priority(self, data: Dict, source_path: str) -> str:
        """Compute migration priority: critical, high, medium, low."""

        # Critical: Core models, authentication, database schemas
        if any(tag in data['tags'] for tag in ['domain-model', 'authentication', 'authorization']):
            return 'critical'

        if 'models' in source_path and any(
            model in source_path.lower()
            for model in ['user', 'agent', 'conversation', 'message', 'prompt']
        ):
            return 'critical'

        # High: Business logic, API endpoints, core services
        if any(tag in data['tags'] for tag in ['business-logic', 'service', 'api-endpoint']):
            return 'high'

        if 'agent-orchestration' in data['tags'] or 'prompt-management' in data['tags']:
            return 'high'

        # Medium: UI components, utilities
        if any(tag in data['tags'] for tag in ['ui-component', 'utility']):
            return 'medium'

        # Low: Tests, configs
        if any(tag in data['tags'] for tag in ['test', 'config']):
            return 'low'

        return 'medium'

    def detect_domain_clusters(self):
        """Group files by domain."""
        print("\nDetecting domain clusters...")

        for source_path, ir_data in self.ir_files.items():
            domain = ir_data.get('domain', 'Unknown')
            self.domain_clusters[domain].append(source_path)

        print(f"✓ Detected {len(self.domain_clusters)} domain clusters")

    def detect_dependency_cycles(self):
        """Detect circular dependencies in the codebase."""
        print("\nDetecting dependency cycles...")

        # Build adjacency list
        graph = defaultdict(set)

        for source_path, ir_data in self.ir_files.items():
            for dep in ir_data.get('dependencies', []):
                # Only track internal file dependencies (relative imports)
                if dep.startswith('.') or '/' in dep:
                    graph[source_path].add(dep)

        # DFS to find cycles
        visited = set()
        rec_stack = set()
        cycles_found = []

        def dfs(node, path):
            visited.add(node)
            rec_stack.add(node)
            path.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, path.copy())
                elif neighbor in rec_stack:
                    # Cycle detected
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    if len(cycle) > 1:
                        cycles_found.append(cycle)

            rec_stack.remove(node)

        for node in graph.keys():
            if node not in visited:
                dfs(node, [])

        # Deduplicate cycles
        unique_cycles = []
        for cycle in cycles_found:
            cycle_set = frozenset(cycle)
            if cycle_set not in [frozenset(c) for c in unique_cycles]:
                unique_cycles.append(cycle)

        self.dependency_cycles = unique_cycles[:20]  # Limit to top 20
        print(f"✓ Detected {len(unique_cycles)} dependency cycles (showing top 20)")

    def map_system_architecture(self):
        """Create architectural layer mapping."""
        print("\nMapping system architecture...")

        layers = {
            'data_models': [],
            'services': [],
            'controllers': [],
            'routes': [],
            'middleware': [],
            'ui_components': [],
            'state_management': [],
            'utilities': [],
            'tests': []
        }

        for source_path, ir_data in self.ir_files.items():
            tags = ir_data.get('tags', [])

            if 'domain-model' in tags:
                layers['data_models'].append(source_path)
            if 'service' in tags or 'business-logic' in tags:
                layers['services'].append(source_path)
            if 'controller' in tags:
                layers['controllers'].append(source_path)
            if 'api-endpoint' in tags:
                layers['routes'].append(source_path)
            if 'middleware' in tags:
                layers['middleware'].append(source_path)
            if 'ui-component' in tags:
                layers['ui_components'].append(source_path)
            if 'state-management' in tags:
                layers['state_management'].append(source_path)
            if 'utility' in tags:
                layers['utilities'].append(source_path)
            if 'test' in tags or 'spec' in source_path or 'test' in source_path:
                layers['tests'].append(source_path)

        self.architecture_map = layers
        print(f"✓ Mapped {sum(len(v) for v in layers.values())} files to architectural layers")

    def compute_priority_groups(self):
        """Group files by migration priority."""
        print("\nComputing priority groups...")

        priorities = defaultdict(list)

        for source_path, ir_data in self.ir_files.items():
            priority = ir_data.get('migration_priority', 'medium')
            priorities[priority].append(source_path)

        self.priority_groups = dict(priorities)
        print(f"✓ Computed priority groups:")
        for priority, files in sorted(priorities.items(), key=lambda x: ['critical', 'high', 'medium', 'low'].index(x[0])):
            print(f"    {priority}: {len(files)} files")

    def generate_migration_grouping(self):
        """Create migration groups based on dependencies and domains."""
        print("\nGenerating migration groups...")

        # Phase 1: Foundation (data models, core utilities)
        phase1 = []
        for source_path, ir_data in self.ir_files.items():
            if ir_data.get('migration_priority') == 'critical':
                if 'domain-model' in ir_data.get('tags', []):
                    phase1.append(source_path)

        # Phase 2: Business Logic (services)
        phase2 = []
        for source_path, ir_data in self.ir_files.items():
            if 'service' in ir_data.get('tags', []) or 'business-logic' in ir_data.get('tags', []):
                if source_path not in phase1:
                    phase2.append(source_path)

        # Phase 3: API Layer (controllers, routes)
        phase3 = []
        for source_path, ir_data in self.ir_files.items():
            if any(tag in ir_data.get('tags', []) for tag in ['controller', 'api-endpoint']):
                if source_path not in phase1 and source_path not in phase2:
                    phase3.append(source_path)

        # Phase 4: UI Layer (components, state)
        phase4 = []
        for source_path, ir_data in self.ir_files.items():
            if any(tag in ir_data.get('tags', []) for tag in ['ui-component', 'state-management']):
                if source_path not in phase1 and source_path not in phase2 and source_path not in phase3:
                    phase4.append(source_path)

        # Phase 5: Everything else
        phase5 = []
        all_phased = set(phase1 + phase2 + phase3 + phase4)
        for source_path in self.ir_files.keys():
            if source_path not in all_phased:
                phase5.append(source_path)

        self.migration_groups = {
            'Phase 1: Foundation (Data Models & Core)': phase1,
            'Phase 2: Business Logic (Services)': phase2,
            'Phase 3: API Layer (Controllers & Routes)': phase3,
            'Phase 4: UI Layer (Components & State)': phase4,
            'Phase 5: Supporting (Utilities & Tests)': phase5
        }

        print(f"✓ Generated migration groups:")
        for phase, files in self.migration_groups.items():
            print(f"    {phase}: {len(files)} files")

    def extract_database_schemas(self):
        """Extract database schema information from IR files."""
        print("\nExtracting database schemas...")

        schemas = {}

        for source_path, ir_data in self.ir_files.items():
            # Look for Mongoose model files
            if 'models' in source_path and source_path.startswith('api/models'):
                model_name = Path(source_path).stem.split('.')[0]

                # Skip test files
                if 'spec' in model_name.lower() or 'test' in model_name.lower():
                    continue

                schema_info = {
                    'file': source_path,
                    'model_name': model_name,
                    'domain': ir_data.get('domain', 'Unknown'),
                    'purpose': ir_data.get('purpose', '')[:200],
                    'classes': ir_data.get('classes', []),
                    'functions': ir_data.get('functions', [])
                }

                schemas[model_name] = schema_info

        self.database_schemas = schemas
        print(f"✓ Extracted {len(schemas)} database schemas")

    def generate_semantic_index(self):
        """Generate the semantic index markdown file."""
        print("\nGenerating semantic index...")

        sections = []

        # Header
        sections.append("# LibreChat Semantic Index")
        sections.append("\n**Generated from IR file analysis**")
        sections.append(f"\n**Total IR Files Analyzed:** {len(self.ir_files)}")
        sections.append(f"\n---\n")

        # Table of Contents
        sections.append("## Table of Contents")
        sections.append("\n1. [File Index](#file-index)")
        sections.append("2. [Domain Clusters](#domain-clusters)")
        sections.append("3. [System Architecture](#system-architecture)")
        sections.append("4. [Database Schemas](#database-schemas)")
        sections.append("5. [Priority Groups](#priority-groups)")
        sections.append("6. [Migration Grouping](#migration-grouping)")
        sections.append("7. [Dependency Cycles](#dependency-cycles)")
        sections.append("8. [Statistics](#statistics)")
        sections.append("\n---\n")

        # Section 1: File Index
        sections.append("## File Index")
        sections.append("\nComplete index of all analyzed files by category.\n")

        # Group by top-level directory
        by_dir = defaultdict(list)
        for source_path in sorted(self.ir_files.keys()):
            top_dir = source_path.split('/')[0] if '/' in source_path else 'root'
            by_dir[top_dir].append(source_path)

        for dir_name in sorted(by_dir.keys()):
            sections.append(f"\n### {dir_name}/ ({len(by_dir[dir_name])} files)")
            sections.append("\n<details>")
            sections.append(f"<summary>Show files</summary>\n")
            for file_path in sorted(by_dir[dir_name])[:50]:  # Limit to 50 per dir
                sections.append(f"- `{file_path}`")
            if len(by_dir[dir_name]) > 50:
                sections.append(f"- *...and {len(by_dir[dir_name]) - 50} more files*")
            sections.append("\n</details>\n")

        # Section 2: Domain Clusters
        sections.append("\n---\n")
        sections.append("## Domain Clusters")
        sections.append("\nFiles grouped by business domain.\n")

        for domain in sorted(self.domain_clusters.keys(), key=lambda d: len(self.domain_clusters[d]), reverse=True)[:15]:
            files = self.domain_clusters[domain]
            sections.append(f"\n### {domain} ({len(files)} files)")
            sections.append("\n<details>")
            sections.append(f"<summary>Show files</summary>\n")
            for file_path in sorted(files)[:30]:  # Limit to 30
                sections.append(f"- `{file_path}`")
            if len(files) > 30:
                sections.append(f"- *...and {len(files) - 30} more files*")
            sections.append("\n</details>\n")

        # Section 3: System Architecture
        sections.append("\n---\n")
        sections.append("## System Architecture")
        sections.append("\nArchitectural layer mapping.\n")

        layer_order = [
            'data_models', 'services', 'controllers', 'routes',
            'middleware', 'ui_components', 'state_management',
            'utilities', 'tests'
        ]

        layer_names = {
            'data_models': 'Data Models (Domain Entities)',
            'services': 'Business Logic Services',
            'controllers': 'Controllers',
            'routes': 'API Routes',
            'middleware': 'Middleware',
            'ui_components': 'UI Components',
            'state_management': 'State Management',
            'utilities': 'Utilities & Helpers',
            'tests': 'Tests'
        }

        for layer_key in layer_order:
            files = self.architecture_map.get(layer_key, [])
            if files:
                sections.append(f"\n### {layer_names[layer_key]} ({len(files)} files)")
                sections.append("\n<details>")
                sections.append(f"<summary>Show files</summary>\n")
                for file_path in sorted(files)[:30]:
                    sections.append(f"- `{file_path}`")
                if len(files) > 30:
                    sections.append(f"- *...and {len(files) - 30} more files*")
                sections.append("\n</details>\n")

        # Section 4: Database Schemas
        sections.append("\n---\n")
        sections.append("## Database Schemas")
        sections.append("\nMongoDB/Mongoose data models.\n")

        core_models = ['User', 'Agent', 'Prompt', 'PromptGroup', 'Conversation', 'Message', 'Action', 'Role', 'File']

        sections.append("\n### Core Models\n")
        for model_name in core_models:
            if model_name in self.database_schemas:
                schema = self.database_schemas[model_name]
                sections.append(f"\n**{model_name}**")
                sections.append(f"- File: `{schema['file']}`")
                sections.append(f"- Domain: {schema['domain']}")
                if schema['classes']:
                    sections.append(f"- Classes: {', '.join(schema['classes'])}")

        sections.append("\n### Additional Models\n")
        for model_name in sorted(self.database_schemas.keys()):
            if model_name not in core_models:
                schema = self.database_schemas[model_name]
                sections.append(f"\n**{model_name}**")
                sections.append(f"- File: `{schema['file']}`")
                sections.append(f"- Domain: {schema['domain']}")

        # Section 5: Priority Groups
        sections.append("\n---\n")
        sections.append("## Priority Groups")
        sections.append("\nFiles grouped by migration priority.\n")

        priority_order = ['critical', 'high', 'medium', 'low']
        for priority in priority_order:
            files = self.priority_groups.get(priority, [])
            if files:
                sections.append(f"\n### {priority.upper()} Priority ({len(files)} files)")
                sections.append("\n<details>")
                sections.append(f"<summary>Show files</summary>\n")
                for file_path in sorted(files)[:50]:
                    sections.append(f"- `{file_path}`")
                if len(files) > 50:
                    sections.append(f"- *...and {len(files) - 50} more files*")
                sections.append("\n</details>\n")

        # Section 6: Migration Grouping
        sections.append("\n---\n")
        sections.append("## Migration Grouping")
        sections.append("\nRecommended phased migration approach.\n")

        for phase_name, files in self.migration_groups.items():
            sections.append(f"\n### {phase_name} ({len(files)} files)")
            sections.append("\n<details>")
            sections.append(f"<summary>Show files</summary>\n")
            for file_path in sorted(files)[:50]:
                sections.append(f"- `{file_path}`")
            if len(files) > 50:
                sections.append(f"- *...and {len(files) - 50} more files*")
            sections.append("\n</details>\n")

        # Section 7: Dependency Cycles
        sections.append("\n---\n")
        sections.append("## Dependency Cycles")
        sections.append("\nDetected circular dependencies (potential issues).\n")

        if self.dependency_cycles:
            sections.append(f"\n**Found {len(self.dependency_cycles)} dependency cycles**\n")
            for idx, cycle in enumerate(self.dependency_cycles[:10], 1):  # Show top 10
                sections.append(f"\n**Cycle {idx}:** ({len(cycle)} files)")
                for file_path in cycle:
                    sections.append(f"- `{file_path}`")
        else:
            sections.append("\n*No dependency cycles detected.*\n")

        # Section 8: Statistics
        sections.append("\n---\n")
        sections.append("## Statistics")
        sections.append("\n### File Counts by Type\n")

        # Count by extension
        ext_counts = Counter()
        for source_path in self.ir_files.keys():
            ext = Path(source_path).suffix or 'no-ext'
            ext_counts[ext] += 1

        for ext, count in ext_counts.most_common(15):
            sections.append(f"- `{ext}`: {count} files")

        sections.append("\n### Tag Distribution\n")

        # Count tags
        tag_counts = Counter()
        for ir_data in self.ir_files.values():
            for tag in ir_data.get('tags', []):
                tag_counts[tag] += 1

        for tag, count in tag_counts.most_common(20):
            sections.append(f"- `{tag}`: {count} files")

        sections.append("\n### Domain Distribution\n")

        for domain, files in sorted(self.domain_clusters.items(), key=lambda x: len(x[1]), reverse=True)[:15]:
            sections.append(f"- **{domain}**: {len(files)} files")

        sections.append("\n### Architecture Layer Distribution\n")

        for layer_key in layer_order:
            count = len(self.architecture_map.get(layer_key, []))
            if count > 0:
                sections.append(f"- **{layer_names[layer_key]}**: {count} files")

        # Write to file
        content = '\n'.join(sections)

        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        file_size_kb = self.output_path.stat().st_size / 1024
        print(f"\n✓ Generated semantic index: {self.output_path} ({file_size_kb:.1f} KB)")

    def run(self):
        """Run the complete semantic index generation."""
        print("=== LibreChat Semantic Index Generator ===\n")

        self.load_dependency_graph()
        self.load_ir_files()
        self.detect_domain_clusters()
        self.detect_dependency_cycles()
        self.map_system_architecture()
        self.compute_priority_groups()
        self.generate_migration_grouping()
        self.extract_database_schemas()
        self.generate_semantic_index()

        print(f"\n✓ Complete!")
        return 0


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    generator = SemanticIndexGenerator(str(repo_root))
    return generator.run()


if __name__ == '__main__':
    exit(main())
