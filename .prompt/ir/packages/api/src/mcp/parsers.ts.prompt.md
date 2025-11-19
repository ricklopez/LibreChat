# File: packages/api/src/mcp/parsers.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/mcp/parsers.ts`.

**Documentation:** as t from './types';

**Primary exports:** 1 exported element(s)
- formatToolContent

**File size:** 5,845 bytes


# 2. Domain Role
**Domain:** Model Context Protocol Integration

**Business relevance:**
This file is part of the Model Context Protocol Integration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `formatToolContent(
  result: t.MCPToolCallResponse,
  provider: t.Provider,
)`



# 4. Internal Structure
### Internal Functions (3)

- `isImageContent()`
- `parseAsString()`
- `formatToolContent()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (1)

**NPM Packages:**
- `librechat-data-provider`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const content = result?.content ?? [];
  if (!content.length) {
    return '(No response)';
```

**Snippet 2:**
```typescript
if (item.type === 'text') {
        return item.text;
```

**Snippet 3:**
```typescript
if (!RECOGNIZED_PROVIDERS.has(provider)) {
    return [parseAsString(result), undefined];
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (1)

- `librechat-data-provider`



# 14. Tags
```
- typescript
- mcp-integration
- application-code
- librechat
- source-file
```

