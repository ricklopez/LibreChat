# File: api/server/services/Config/getCachedTools.js

# 1. Purpose
**File Type:** JS (Business logic service)

**What this file represents:**
This file is a business logic service located at `api/server/services/Config/getCachedTools.js`.

**Documentation:** * Cache key generators for different tool access patterns


**File size:** 3,560 bytes


# 2. Domain Role
**Domain:** Tool & Action Execution

**Business relevance:**
This file is part of the Tool & Action Execution domain within the LibreChat application.

**Role:** Business logic implementation
- Implements domain-specific operations
- Coordinates between data layer and API layer
- Enforces business rules and validation


# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (4)

- `getCachedTools()`
- `setCachedTools()`
- `invalidateCachedTools()`
- `getMCPServerTools()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Parameters from controller/caller
2. **Transformations:** Business logic processing
3. **External calls:** Database models, external APIs
4. **Output:** Processed data or operation result


# 6. Relationships & Collaboration
### Imported Dependencies (2)

**NPM Packages:**
- `librechat-data-provider`

**Aliased Imports:**
- `~/cache/getLogStores`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
const cache = getLogStores(CacheKeys.CONFIG_STORE);
  const serverTools = await cache.get(ToolCacheKeys.MCP_SERVER(userId, serverName));

  if (serverTools) {
    return serverTools;
```



# 10. Architectural Concerns
**Async Behavior:** Asynchronous operations present


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Business logic service
- Service: Business logic layer
- Module: `getCachedToolsService`


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (2)

- `librechat-data-provider`
- `~/cache/getLogStores`



# 14. Tags
```
- javascript
- service
- business-logic
- tool-execution
- application-code
- librechat
- source-file
```

