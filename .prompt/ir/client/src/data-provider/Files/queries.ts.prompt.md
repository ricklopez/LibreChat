# File: client/src/data-provider/Files/queries.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `client/src/data-provider/Files/queries.ts`.

**Primary exports:** 5 exported element(s)
- useGetFiles
- useGetAgentFiles
- useGetFileConfig

**File size:** 3,562 bytes


# 2. Domain Role
**Domain:** File Storage & Management

**Business relevance:**
This file is part of the File Storage & Management domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `useGetFiles()` — named export
- `useGetAgentFiles()` — named export
- `useGetFileConfig()` — named export
- `useFileDownload()` — named export
- `useCodeOutputDownload()` — named export



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
### Imported Dependencies (6)

**NPM Packages:**
- `recoil`
- `@tanstack/react-query`
- `librechat-data-provider`

**Aliased Imports:**
- `~/common`
- `~/utils`
- `~/store`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const queriesEnabled = useRecoilValue<boolean>(store.queriesEnabled);
  return useQuery<t.TFile[], unknown, TData>([QueryKeys.files], () => dataService.getFiles(), {
    refetchOnWindowFocus: false,
    refetchOnReconnect: false,
    refetchOnMount: false,
    ...config,
    enabled: (config?.enable
```

**Snippet 2:**
```typescript
const queriesEnabled = useRecoilValue<boolean>(store.queriesEnabled);
  return useQuery<t.TFile[], unknown, TData>(
    DynamicQueryKeys.agentFiles(agentId ?? ''),
    () => (agentId ? dataService.getAgentFiles(agentId) : Promise.resolve([])),
    {
      refetchOnWindowFocus: false,
      refetchOn
```

**Snippet 3:**
```typescript
return useQuery<t.FileConfig, unknown, TData>(
    [QueryKeys.fileConfig],
    () => dataService.getFileConfig(),
    {
      refetchOnWindowFocus: false,
      refetchOnReconnect: false,
      refetchOnMount: false,
      ...config,
```



# 10. Architectural Concerns
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (6)

- `recoil`
- `@tanstack/react-query`
- `librechat-data-provider`
- `~/common`
- `~/utils`
- `~/store`



# 14. Tags
```
- typescript
- file-storage
- application-code
- librechat
- source-file
```

