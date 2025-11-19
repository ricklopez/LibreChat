# File: api/server/routes/prompts.js

# 1. Purpose
**File Type:** JS (API endpoint / Request handler)

**What this file represents:**
This file is a api endpoint / request handler located at `api/server/routes/prompts.js`.


**File size:** 13,379 bytes


# 2. Domain Role
**Domain:** Prompt Management & Templating

**Business relevance:**
This file is part of the Prompt Management & Templating domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (5)

- `createNewPromptGroup()`
- `addPromptToGroup()`
- `patchPromptGroup()`
- `deletePromptController()`
- `deletePromptGroupController()`

### Architectural Patterns

- Express Router pattern



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** HTTP request (req.body, req.params, req.query)
2. **Transformations:** Request validation and data extraction
3. **External calls:** Service layer methods, database queries
4. **Output:** HTTP response (res.json, res.status)


# 6. Relationships & Collaboration
### Imported Dependencies (9)

**NPM Packages:**
- `mongoose`
- `express`
- `@librechat/data-schemas`
- `@librechat/api`
- `librechat-data-provider`

**Aliased Imports:**
- `~/models/Prompt`
- `~/server/middleware`
- `~/server/services/PermissionService`
- `~/models/Role`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
promptGroups: groupsWithPublicFlag,
      pageNumber: '1', // Always 1 for cursor-based pagination
      pageSize: actualLimit.toString(),
      hasMore: has_more,
      after,
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (8)

- `express`
- `@librechat/data-schemas`
- `@librechat/api`
- `librechat-data-provider`
- `~/models/Prompt`
- `~/server/middleware`
- `~/server/services/PermissionService`
- `~/models/Role`



# 14. Tags
```
- javascript
- api-endpoint
- prompt-management
- application-code
- librechat
- source-file
```

