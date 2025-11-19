# File: client/src/utils/artifacts.ts

# 1. Purpose
**File Type:** TS (Utility / Helper function)

**What this file represents:**
This file is a utility / helper function located at `client/src/utils/artifacts.ts`.

**Documentation:** mermaid and markdown types are handled separately in useArtifactProps.ts

**Primary exports:** 7 exported element(s)
- getKey
- getArtifactFilename
- getTemplate

**File size:** 6,928 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `getKey(type: string, language?: string)`
- `getArtifactFilename(type: string, language?: string)`
- `getTemplate(type: string, language?: string)`
- `getDependencies(type: string)`
- `getProps(type: string)`
- `sharedOptions()` — named export
- `sharedFiles()` — named export



# 4. Internal Structure
### Internal Functions (5)

- `getKey()`
- `getArtifactFilename()`
- `getTemplate()`
- `getDependencies()`
- `getProps()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (2)

**NPM Packages:**
- `dedent`
- `librechat-data-provider`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
'application/vnd.react': 'App.tsx',
  'text/html': 'index.html',
  'application/vnd.code-html': 'index.html',
  // mermaid and markdown types are handled separately in useArtifactProps.ts
  default: 'index.html',
  // 'css': 'css',
  // 'javascript': 'js',
  // 'typescript': 'ts',
  // 'jsx': 'jsx',
```

**Snippet 2:**
```typescript
const key = getKey(type, language);
  return artifactFilename[key] ?? artifactFilename.default;
```

**Snippet 3:**
```typescript
const key = getKey(type, language);
  return artifactTemplate[key] ?? (artifactTemplate.default as SandpackPredefinedTemplate);
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (2)

- `dedent`
- `librechat-data-provider`



# 14. Tags
```
- typescript
- utility
- application-code
- librechat
- source-file
```

