# File: packages/api/src/mcp/MCPManager.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/mcp/MCPManager.ts`.

**Primary exports:** 1 exported element(s)
- MCPManager

**File size:** 9,154 bytes


# 2. Domain Role
**Domain:** Model Context Protocol Integration

**Business relevance:**
This file is part of the Model Context Protocol Integration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Classes

- `class MCPManager extends UserConnectionManager`

### Exported Functions

- `MCPManager()` — named export



# 4. Internal Structure
*No significant internal structure detected.*


# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (11)

**NPM Packages:**
- `lodash/pick`
- `@librechat/data-schemas`
- `@modelcontextprotocol/sdk/types.js`

**Relative Imports:**
- `./UserConnectionManager`
- `./ConnectionsRepository`
- `./registry/MCPServerInspector`
- `./registry/MCPServersInitializer`
- `./registry/MCPServersRegistry`
- `./parsers`
- `./connection`

**Aliased Imports:**
- `~/utils/env`



# 7. Database Interaction Mapping
**Database:** MongoDB via Mongoose



# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
serverName: string;
      user?: TUser;
      forceNew?: boolean;
      flowManager?: FlowStateManager<MCPOAuthTokens | null>;
```

**Snippet 2:**
```typescript
if (config.toolFunctions != null) {
        Object.assign(toolFunctions, config.toolFunctions);
```

**Snippet 3:**
```typescript
if (config.serverInstructions != null) {
        instructions[serverName] = config.serverInstructions as string;
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
### dependsOn (4)

- `lodash/pick`
- `@librechat/data-schemas`
- `@modelcontextprotocol/sdk/types.js`
- `~/utils/env`



# 14. Tags
```
- typescript
- mcp-integration
- application-code
- librechat
- source-file
```

