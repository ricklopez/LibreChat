# File: client/src/data-provider/Agents/mutations.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `client/src/data-provider/Agents/mutations.ts`.

**Documentation:** as t from 'librechat-data-provider';

**Primary exports:** 10 exported element(s)
- allAgentViewAndEditQueryKeys
- useCreateAgentMutation
- useUpdateAgentMutation

**File size:** 14,165 bytes


# 2. Domain Role
**Domain:** Agent Orchestration & Configuration

**Business relevance:**
This file is part of the Agent Orchestration & Configuration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `allAgentViewAndEditQueryKeys()` — named export
- `useCreateAgentMutation()` — named export
- `useUpdateAgentMutation()` — named export
- `useDeleteAgentMutation()` — named export
- `useDuplicateAgentMutation()` — named export
- `useUploadAgentAvatarMutation()` — named export
- `useUpdateAgentAction()` — named export
- `useDeleteAgentAction()` — named export
- `useRevertAgentVersionMutation()` — named export
- `invalidateAgentMarketplaceQueries()` — named export



# 4. Internal Structure
### Internal Functions (3)

- `data()`
- `updaterFn()`
- `invalidateAgentMarketplaceQueries()`

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
onMutate: (variables) => options?.onMutate?.(variables),
    onError: (error, variables, context) => options?.onError?.(error, variables, context),
    onSuccess: (newAgent, variables, context) => {
      ((keys: t.AgentListParams[]) => {
        keys.forEach((key) => {
          const listRes = que
```

**Snippet 2:**
```typescript
return options?.onSuccess?.(updatedAgent, variables, context);
```

**Snippet 3:**
```typescript
const queryClient = useQueryClient();
  return useMutation(
    ({ agent_id
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (2)

- `@tanstack/react-query`
- `librechat-data-provider`



# 14. Tags
```
- typescript
- agent-orchestration
- application-code
- librechat
- source-file
```

