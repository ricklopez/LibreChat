# File: client/src/data-provider/Tools/queries.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `client/src/data-provider/Tools/queries.ts`.

**Primary exports:** 4 exported element(s)
- useVerifyAgentToolAuth
- useGetToolCalls
- useMCPConnectionStatusQuery

**File size:** 2,375 bytes


# 2. Domain Role
**Domain:** Tool & Action Execution

**Business relevance:**
This file is part of the Tool & Action Execution domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `useVerifyAgentToolAuth()` — named export
- `useGetToolCalls()` — named export
- `useMCPConnectionStatusQuery()` — named export
- `useMCPAuthValuesQuery()` — named export



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
return useQuery<t.VerifyToolAuthResponse>(
    [QueryKeys.toolAuth, params.toolId],
    () => dataService.getVerifyAgentToolAuth(params),
    {
      refetchOnWindowFocus: false,
      refetchOnReconnect: false,
      refetchOnMount: false,
      ...config,
```

**Snippet 2:**
```typescript
return useQuery<t.MCPConnectionStatusResponse>(
    [QueryKeys.mcpConnectionStatus],
    () => dataService.getMCPConnectionStatus(),
    {
      refetchOnWindowFocus: false,
      refetchOnReconnect: false,
      refetchOnMount: false,
      staleTime: 10000, // 10 seconds
      ...config,
```

**Snippet 3:**
```typescript
return useQuery<t.MCPAuthValuesResponse>(
    [QueryKeys.mcpAuthValues, serverName],
    () => dataService.getMCPAuthValues(serverName),
    {
      refetchOnWindowFocus: false,
      refetchOnReconnect: false,
      refetchOnMount: false,
      enabled: !!serverName,
      ...config,
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)


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
- tool-execution
- application-code
- librechat
- source-file
```

