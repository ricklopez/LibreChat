# File: client/src/data-provider/mcp.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `client/src/data-provider/mcp.ts`.

**Documentation:** * Dedicated queries for MCP (Model Context Protocol) tools

**Primary exports:** 1 exported element(s)
- useMCPToolsQuery

**File size:** 970 bytes


# 2. Domain Role
**Domain:** Model Context Protocol Integration

**Business relevance:**
This file is part of the Model Context Protocol Integration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `useMCPToolsQuery()` — named export



# 4. Internal Structure
### Architectural Patterns

- React Query data fetching



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (2)

**NPM Packages:**
- `@tanstack/react-query`
- `librechat-data-provider`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
return useQuery<MCPServersResponse, unknown, TData>(
    [QueryKeys.mcpTools],
    () => dataService.getMCPTools(),
    {
      refetchOnWindowFocus: false,
      refetchOnReconnect: false,
      refetchOnMount: false,
      staleTime: 5 * 60 * 1000, // 5 minutes
      ...config,
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (2)

- `@tanstack/react-query`
- `librechat-data-provider`



# 14. Tags
```
- typescript
- mcp-integration
- application-code
- librechat
- source-file
```

