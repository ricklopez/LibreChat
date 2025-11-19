# File: client/src/data-provider/prompts.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `client/src/data-provider/prompts.ts`.

**Documentation:** Prompts */

**Primary exports:** 7 exported element(s)
- useUpdatePromptGroup
- useCreatePrompt
- useAddPromptToGroup

**File size:** 11,228 bytes


# 2. Domain Role
**Domain:** Prompt Management & Templating

**Business relevance:**
This file is part of the Prompt Management & Templating domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `useUpdatePromptGroup()` — named export
- `useCreatePrompt()` — named export
- `useAddPromptToGroup()` — named export
- `useDeletePrompt()` — named export
- `useDeletePromptGroup()` — named export
- `useUpdatePromptLabels()` — named export
- `useMakePromptProduction()` — named export



# 4. Internal Structure
### Internal Functions (1)

- `useMakePromptProduction()`

### Architectural Patterns

- React Query data fetching



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (5)

**NPM Packages:**
- `recoil`
- `@tanstack/react-query`
- `librechat-data-provider`

**Aliased Imports:**
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
mutationFn: (payload: t.TDeletePromptVariables) => dataService.deletePrompt(payload),
    ...rest,
    onSuccess: (response, variables, context) => {
      if (response.promptGroup) {
        const promptGroupId = response.promptGroup.id;
        queryClient.setQueryData<t.PromptGroupListData>(
    
```

**Snippet 2:**
```typescript
mutationFn: (variables: t.TDeletePromptGroupRequest) =>
      dataService.deletePromptGroup(variables.id),
    ...rest,
    onSuccess: (response, variables, context) => {
      queryClient.setQueryData<t.PromptGroupListData>(
        [QueryKeys.promptGroups, name, category, pageSize],
        (data)
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (5)

- `recoil`
- `@tanstack/react-query`
- `librechat-data-provider`
- `~/utils`
- `~/store`



# 14. Tags
```
- typescript
- prompt-management
- application-code
- librechat
- source-file
```

