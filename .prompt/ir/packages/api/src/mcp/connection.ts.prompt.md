# File: packages/api/src/mcp/connection.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/mcp/connection.ts`.

**Primary exports:** 1 exported element(s)
- MCPConnection

**File size:** 24,999 bytes


# 2. Domain Role
**Domain:** Model Context Protocol Integration

**Business relevance:**
This file is part of the Model Context Protocol Integration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Classes

- `class MCPConnection extends EventEmitter`

### Exported Functions

- `MCPConnection()` — named export



# 4. Internal Structure
### Internal Functions (7)

- `isStdioOptions()`
- `isWebSocketOptions()`
- `isSSEOptions()`
- `isStreamableHTTPOptions()`
- `customFetch()`
- `backoffDelay()`
- `cleanup()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (12)

**NPM Packages:**
- `events`
- `@librechat/data-schemas`
- `undici`
- `@modelcontextprotocol/sdk/client/stdio.js`
- `@modelcontextprotocol/sdk/client/index.js`
- `@modelcontextprotocol/sdk/client/sse.js`
- `@modelcontextprotocol/sdk/client/websocket.js`
- `@modelcontextprotocol/sdk/types.js`
- `@modelcontextprotocol/sdk/client/streamableHttp.js`

**Relative Imports:**
- `./utils`
- `./mcpConfig`

**Aliased Imports:**
- `~/utils/promise`



# 7. Database Interaction Mapping
**Database:** MongoDB via Mongoose



# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
if ('url' in options) {
    const protocol = new URL(options.url).protocol;
    return protocol === 'ws:' || protocol === 'wss:';
```

**Snippet 2:**
```typescript
if ('url' in options) {
    const protocol = new URL(options.url).protocol;
    return protocol !== 'ws:' && protocol !== 'wss:';
```

**Snippet 3:**
```typescript
if ('url' in options && 'type' in options) {
    const optionType = options.type as string;
    if (optionType === 'streamable-http' || optionType === 'http') {
      const protocol = new URL(options.url).protocol;
      return protocol !== 'ws:' && protocol !== 'wss:';
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
### dependsOn (10)

- `events`
- `@librechat/data-schemas`
- `undici`
- `@modelcontextprotocol/sdk/client/stdio.js`
- `@modelcontextprotocol/sdk/client/index.js`
- `@modelcontextprotocol/sdk/client/sse.js`
- `@modelcontextprotocol/sdk/client/websocket.js`
- `@modelcontextprotocol/sdk/types.js`
- `@modelcontextprotocol/sdk/client/streamableHttp.js`
- `~/utils/promise`



# 14. Tags
```
- typescript
- mcp-integration
- application-code
- librechat
- source-file
```

