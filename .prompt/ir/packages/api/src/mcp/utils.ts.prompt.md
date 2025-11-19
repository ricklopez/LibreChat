# File: packages/api/src/mcp/utils.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/mcp/utils.ts`.

**Documentation:** * Normalizes a server name to match the pattern ^[a-zA-Z0-9_.-]+$

**Primary exports:** 3 exported element(s)
- mcpToolPattern
- normalizeServerName
- sanitizeUrlForLogging

**File size:** 1,687 bytes


# 2. Domain Role
**Domain:** Model Context Protocol Integration

**Business relevance:**
This file is part of the Model Context Protocol Integration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `mcpToolPattern()` — named export
- `normalizeServerName(serverName: string)`
- `sanitizeUrlForLogging(url: string | URL)`



# 4. Internal Structure
### Internal Functions (2)

- `normalizeServerName()`
- `sanitizeUrlForLogging()`



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
// Check if the server name already matches the pattern
  if (/^[a-zA-Z0-9_.-]+$/.test(serverName)) {
    return serverName;
```

**Snippet 2:**
```typescript
/** Hash of the original name to ensure uniqueness */
    let hash = 0;
    for (let i = 0; i < serverName.length; i++) {
      hash = (hash << 5) - hash + serverName.charCodeAt(i);
      hash |= 0; // Convert to 32bit integer
```

**Snippet 3:**
```typescript
try {
    const urlObj = typeof url === 'string' ? new URL(url) : url;
    return `${urlObj.protocol
```



# 10. Architectural Concerns
**Error Handling:** Uses try-catch blocks


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


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

