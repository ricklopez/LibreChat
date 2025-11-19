# File: packages/api/src/prompts/format.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/prompts/format.ts`.

**Documentation:** * Formats prompt groups for the paginated /groups endpoint response

**Primary exports:** 4 exported element(s)
- formatPromptGroupsResponse
- createEmptyPromptGroupsResponse
- markPublicPromptGroups

**File size:** 4,400 bytes


# 2. Domain Role
**Domain:** Prompt Management & Templating

**Business relevance:**
This file is part of the Prompt Management & Templating domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `formatPromptGroupsResponse({
  promptGroups = [],
  pageNumber,
  pageSize,
  actualLimit,
  hasMore = false,
  after = null,
}: {
  promptGroups: IPromptGroup[];
  pageNumber?: string;
  pageSize?: string;
  actualLimit?: string | number;
  hasMore?: boolean;
  after?: string | null;
})`
- `createEmptyPromptGroupsResponse({
  pageNumber,
  pageSize,
  actualLimit,
}: {
  pageNumber?: string;
  pageSize?: string;
  actualLimit?: string | number;
})`
- `markPublicPromptGroups(
  promptGroups: IPromptGroup[],
  publiclyAccessibleIds: Types.ObjectId[],
)`
- `buildPromptGroupFilter({
  name,
  category,
  ...otherFilters
}: {
  name?: string;
  category?: string;
  [key: string]: string | number | boolean | RegExp | undefined;
})`



# 4. Internal Structure
### Internal Functions (6)

- `formatPromptGroupsResponse()`
- `createEmptyPromptGroupsResponse()`
- `markPublicPromptGroups()`
- `buildPromptGroupFilter()`
- `filterAccessibleIdsBySharedLogic()`
- `escapeRegExp()`



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
// For MY_PROMPTS - exclude public prompts to show only user's own prompts
    return accessibleIds.filter((id) => !publicIdStrings.has(id.toString()));
```



# 10. Architectural Concerns
**Async Behavior:** Asynchronous operations present


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (1)

- `librechat-data-provider`



# 14. Tags
```
- typescript
- prompt-management
- application-code
- librechat
- source-file
```

