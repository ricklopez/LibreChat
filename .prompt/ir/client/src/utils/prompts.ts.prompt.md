# File: client/src/utils/prompts.ts

# 1. Purpose
**File Type:** TS (Utility / Helper function)

**What this file represents:**
This file is a utility / helper function located at `client/src/utils/prompts.ts`.

**Documentation:** * Detects the presence of variables in the given text, excluding those found in `specialVariables`.

**Primary exports:** 6 exported element(s)
- detectVariables
- wrapVariable
- extractUniqueVariables

**File size:** 2,862 bytes


# 2. Domain Role
**Domain:** Prompt Management & Templating

**Business relevance:**
This file is part of the Prompt Management & Templating domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `detectVariables()` — named export
- `wrapVariable()` — named export
- `extractUniqueVariables()` — named export
- `extractVariableInfo()` — named export
- `formatDateTime(dateTimeString: string)`
- `mapPromptGroups()` — named export



# 4. Internal Structure
### Internal Functions (3)

- `formatDateTime()`
- `wrapVariable()`
- `extractVariableInfo()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (1)

**NPM Packages:**
- `librechat-data-provider`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const variable = match[1];
    allVariables.push(variable);

    const count = variableCount.get(variable) ?? 0;
    variableCount.set(variable, count + 1);

    if (count > 0) {
      repeatedVariables.add(variable);
```

**Snippet 2:**
```typescript
return groups.reduce(
    (acc, group) => {
      if (!group._id) {
        return acc;
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (1)

- `librechat-data-provider`



# 14. Tags
```
- typescript
- utility
- prompt-management
- application-code
- librechat
- source-file
```

