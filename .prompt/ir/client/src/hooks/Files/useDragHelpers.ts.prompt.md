# File: client/src/hooks/Files/useDragHelpers.ts

# 1. Purpose
**File Type:** TS (Custom React hook)

**What this file represents:**
This file is a custom react hook located at `client/src/hooks/Files/useDragHelpers.ts`.

**Primary exports:** 1 exported element(s)
- function

**File size:** 5,733 bytes


# 2. Domain Role
**Domain:** File Storage & Management

**Business relevance:**
This file is part of the File Storage & Management domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `function()` — default export



# 4. Internal Structure
### Internal Functions (1)

- `useDragHelpers()`

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
### Imported Dependencies (10)

**NPM Packages:**
- `react`
- `react-dnd`
- `@librechat/client`
- `react-dnd-html5-backend`
- `@tanstack/react-query`
- `recoil`
- `librechat-data-provider`

**Relative Imports:**
- `./useFileHandling`
- `../useLocalize`

**Aliased Imports:**
- `~/common`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
/** File search is not automatically enabled to simulate legacy behavior */
      if (toolResource && toolResource !== EToolResources.file_search) {
        setEphemeralAgent((prev) => ({
          ...prev,
          [toolResource]: true,
```

**Snippet 2:**
```typescript
/** Agent data from cache */
        const agent = queryClient.getQueryData<t.Agent>([QueryKeys.agent, agentId]);
        if (agent) {
          const agentTools = agent.tools as string[] | undefined;
          fileSearchAllowedByAgent = agentTools?.includes(Tools.file_search) ?? false;
          co
```

**Snippet 3:**
```typescript
// Fallback: directly handle files without showing modal
        handleFilesRef.current(item.files);
        return;
```



# 10. Architectural Concerns
**Performance:** Optimized with memoization


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
- May contain deprecated or legacy code patterns


# 13. Dependencies
### dependsOn (8)

- `react`
- `react-dnd`
- `@librechat/client`
- `react-dnd-html5-backend`
- `@tanstack/react-query`
- `recoil`
- `librechat-data-provider`
- `~/common`



# 14. Tags
```
- typescript
- react-hook
- file-storage
- application-code
- librechat
- source-file
```

