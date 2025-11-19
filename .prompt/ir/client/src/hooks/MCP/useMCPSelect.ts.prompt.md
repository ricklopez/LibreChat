# File: client/src/hooks/MCP/useMCPSelect.ts

# 1. Purpose
**File Type:** TS (Custom React hook)

**What this file represents:**
This file is a custom react hook located at `client/src/hooks/MCP/useMCPSelect.ts`.

**Primary exports:** 1 exported element(s)
- useMCPSelect

**File size:** 2,203 bytes


# 2. Domain Role
**Domain:** Model Context Protocol Integration

**Business relevance:**
This file is part of the Model Context Protocol Integration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `useMCPSelect({ conversationId }: { conversationId?: string | null })`



# 4. Internal Structure
### Internal Functions (1)

- `useMCPSelect()`

### Architectural Patterns

- React Hooks pattern



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (8)

**NPM Packages:**
- `react`
- `jotai`
- `lodash/isEqual`
- `recoil`
- `librechat-data-provider`

**Aliased Imports:**
- `~/store`
- `~/data-provider`
- `~/utils/timestamps`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
return new Set(Object.keys(startupConfig?.mcpServers ?? {
```

**Snippet 2:**
```typescript
setEphemeralAgent((prev) => {
      if (!isEqual(prev?.mcp, mcpValues)) {
        return { ...(prev ?? {
```



# 10. Architectural Concerns
**Performance:** Optimized with memoization


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (8)

- `react`
- `jotai`
- `lodash/isEqual`
- `recoil`
- `librechat-data-provider`
- `~/store`
- `~/data-provider`
- `~/utils/timestamps`



# 14. Tags
```
- typescript
- react-hook
- mcp-integration
- application-code
- librechat
- source-file
```

