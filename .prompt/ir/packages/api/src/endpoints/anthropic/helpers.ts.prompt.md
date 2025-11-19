# File: packages/api/src/endpoints/anthropic/helpers.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/endpoints/anthropic/helpers.ts`.

**Documentation:** * @param {string} modelName


**File size:** 4,690 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (3)

- `checkPromptCacheSupport()`
- `getClaudeHeaders()`
- `configureReasoning()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (4)

**NPM Packages:**
- `@librechat/data-schemas`
- `@librechat/agents`
- `librechat-data-provider`

**Aliased Imports:**
- `~/utils/tokens`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const modelMatch = matchModelName(modelName, EModelEndpoint.anthropic) ?? '';
  if (
    modelMatch.includes('claude-3-5-sonnet-latest') ||
    modelMatch.includes('claude-3.5-sonnet-latest')
  ) {
    return false;
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (4)

- `@librechat/data-schemas`
- `@librechat/agents`
- `librechat-data-provider`
- `~/utils/tokens`



# 14. Tags
```
- typescript
- application-code
- librechat
- source-file
```

