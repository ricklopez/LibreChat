# File: client/src/hooks/MCP/useMCPServerManager.ts

# 1. Purpose
**File Type:** TS (Custom React hook)

**What this file represents:**
This file is a custom react hook located at `client/src/hooks/MCP/useMCPServerManager.ts`.

**Primary exports:** 1 exported element(s)
- useMCPServerManager

**File size:** 21,054 bytes


# 2. Domain Role
**Domain:** Model Context Protocol Integration

**Business relevance:**
This file is part of the Model Context Protocol Integration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `useMCPServerManager({ conversationId }: { conversationId?: string | null } = {})`



# 4. Internal Structure
### Internal Functions (4)

- `useMCPServerManager()`
- `pollOnce()`
- `handleConfigClick()`
- `handleCancelClick()`

### Architectural Patterns

- React Hooks pattern
- React Query data fetching



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (7)

**NPM Packages:**
- `react`
- `@librechat/client`
- `@tanstack/react-query`
- `librechat-data-provider`
- `librechat-data-provider/react-query`

**Aliased Imports:**
- `~/hooks`
- `~/data-provider`



# 7. Database Interaction Mapping
**Database:** MongoDB via Mongoose



# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
if (!startupConfig?.mcpServers) return [];
    return Object.entries(startupConfig.mcpServers)
      .filter(([, config]) => config.chatMenu !== false)
      .map(([serverName]) => serverName);
```

**Snippet 2:**
```typescript
if (!connectionStatus || Object.keys(connectionStatus).length === 0) {
      return;
```

**Snippet 3:**
```typescript
const state = serverStates[serverName];
      if (state?.pollInterval) {
        clearTimeout(state.pollInterval);
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present
**Performance:** Optimized with memoization


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (7)

- `react`
- `@librechat/client`
- `@tanstack/react-query`
- `librechat-data-provider`
- `librechat-data-provider/react-query`
- `~/hooks`
- `~/data-provider`



# 14. Tags
```
- typescript
- react-hook
- mcp-integration
- application-code
- librechat
- source-file
```

