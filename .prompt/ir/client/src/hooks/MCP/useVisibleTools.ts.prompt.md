# File: client/src/hooks/MCP/useVisibleTools.ts

# 1. Purpose
**File Type:** TS (Custom React hook)

**What this file represents:**
This file is a custom react hook located at `client/src/hooks/MCP/useVisibleTools.ts`.

**Documentation:** * Custom hook to calculate visible tool IDs based on selected tools.

**Primary exports:** 1 exported element(s)
- useVisibleTools

**File size:** 1,748 bytes


# 2. Domain Role
**Domain:** Tool & Action Execution

**Business relevance:**
This file is part of the Tool & Action Execution domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `useVisibleTools(
  selectedToolIds: string[] | undefined,
  regularTools: TPlugin[] | undefined,
  mcpServersMap: Map<string, MCPServerInfo>,
)`



# 4. Internal Structure
### Internal Functions (1)

- `useVisibleTools()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (2)

**NPM Packages:**
- `react`
- `librechat-data-provider`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
return useMemo(() => {
    const mcpServers = new Set<string>();
    const regularToolIds: string[] = [];

    for (const toolId of selectedToolIds ?? []) {
      // MCP tools/servers
      if (toolId.includes(Constants.mcp_delimiter)) {
        const serverName = toolId.split(Constants.mcp_delimite
```



# 10. Architectural Concerns
**Performance:** Optimized with memoization


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
- May contain deprecated or legacy code patterns


# 13. Dependencies
### dependsOn (2)

- `react`
- `librechat-data-provider`



# 14. Tags
```
- typescript
- react-hook
- tool-execution
- mcp-integration
- application-code
- librechat
- source-file
```

