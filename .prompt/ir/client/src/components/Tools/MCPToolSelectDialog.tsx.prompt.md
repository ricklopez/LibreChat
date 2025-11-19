# File: client/src/components/Tools/MCPToolSelectDialog.tsx

# 1. Purpose
**File Type:** TSX (UI component)

**What this file represents:**
This file is a ui component located at `client/src/components/Tools/MCPToolSelectDialog.tsx`.

**Primary exports:** 1 exported element(s)
- MCPToolSelectDialog

**File size:** 13,251 bytes


# 2. Domain Role
**Domain:** Tool & Action Execution

**Business relevance:**
This file is part of the Tool & Action Execution domain within the LibreChat application.

**Role:** User interface presentation
- Renders UI elements for user interaction
- Manages component-level state
- Handles user events and input


# 3. Public API (FULL DETAIL)
### Exported Functions

- `MCPToolSelectDialog({
  isOpen,
  agentId,
  setIsOpen,
  mcpServerNames,
}: TPluginStoreDialogProps & {
  agentId: string;
  mcpServerNames?: string[];
  endpoint: EModelEndpoint.agents;
})` — **default export**



# 4. Internal Structure
### Internal Functions (7)

- `MCPToolSelectDialog()`
- `handleInstallError()`
- `handleDirectAdd()`
- `addToolsToForm()`
- `handleSaveCustomVars()`
- `handleRevokeCustomVars()`
- `onAddTool()`

### Architectural Patterns

- React Hooks pattern
- React Query data fetching



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Props passed from parent component
2. **Transformations:** Component state updates via hooks
3. **External calls:** API calls via React Query hooks
4. **Output:** Rendered JSX with event handlers


# 6. Relationships & Collaboration
### Imported Dependencies (13)

**NPM Packages:**
- `react`
- `lucide-react`
- `react-hook-form`
- `@tanstack/react-query`
- `librechat-data-provider`
- `@headlessui/react`
- `librechat-data-provider/react-query`

**Relative Imports:**
- `./MCPToolItem`

**Aliased Imports:**
- `~/hooks`
- `~/components/MCP/CustomUserVarsSection`
- `~/components/Plugins/Store`
- `~/Providers`
- `~/data-provider`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**UI Component:** React component

**React Hooks:**
- useState
- useEffect
- useMemo
- useQuery (React Query)

**Event Handlers:** 9 event handler(s) detected

**Form Management:** React Hook Form



# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
setError(true);
    const errorMessage = error.response?.data?.message ?? '';
    if (errorMessage) {
      setErrorMessage(errorMessage);
```

**Snippet 2:**
```typescript
try {
      setIsInitializing(serverName);

      // First, save auth if provided
      if (authData && Object.keys(authData).length > 0) {
        await updateUserPlugins.mutateAsync({
          pluginKey: `${Constants.mcp_prefix
```

**Snippet 3:**
```typescript
const result = await initializeServer(serverName);
        if (result?.success && result.oauthRequired && result.oauthUrl) {
          setIsInitializing(null);
          return;
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present
**Performance:** Optimized with memoization


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** UI component
- Component: `MCPToolSelectDialog`


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (12)

- `react`
- `lucide-react`
- `react-hook-form`
- `@tanstack/react-query`
- `librechat-data-provider`
- `@headlessui/react`
- `librechat-data-provider/react-query`
- `~/hooks`
- `~/components/MCP/CustomUserVarsSection`
- `~/components/Plugins/Store`
- `~/Providers`
- `~/data-provider`



# 14. Tags
```
- typescript
- ui-component
- tool-execution
- mcp-integration
- application-code
- librechat
- source-file
```

