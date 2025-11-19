# File: client/src/data-provider/queries.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `client/src/data-provider/queries.ts`.

**Primary exports:** 21 exported element(s)
- useGetPresetsQuery
- useGetConvoIdQuery
- useConversationsInfiniteQuery

**File size:** 17,453 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `useGetPresetsQuery()` — named export
- `useGetConvoIdQuery()` — named export
- `useConversationsInfiniteQuery()` — named export
- `useMessagesInfiniteQuery()` — named export
- `useSharedLinksQuery()` — named export
- `useConversationTagsQuery()` — named export
- `useAvailableToolsQuery()` — named export
- `useListAssistantsQuery()` — named export
- `useListAssistantsInfiniteQuery()` — named export
- `useGetAssistantByIdQuery()` — named export
- `useGetActionsQuery()` — named export
- `useGetAssistantDocsQuery()` — named export
- `useVoicesQuery()` — named export
- `useCustomConfigSpeechQuery()` — named export
- `usePromptGroupsInfiniteQuery()` — named export
- `useGetPromptGroup()` — named export
- `useGetPrompts()` — named export
- `useGetAllPromptGroups()` — named export
- `useGetCategories()` — named export
- `useGetRandomPrompts()` — named export
- `useUserTermsQuery()` — named export



# 4. Internal Structure
### Internal Functions (5)

- `useConversationsInfiniteQuery()`
- `useMessagesInfiniteQuery()`
- `useSharedLinksQuery()`
- `useListAssistantsInfiniteQuery()`
- `usePromptGroupsInfiniteQuery()`

### Architectural Patterns

- React Query data fetching



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (3)

**NPM Packages:**
- `librechat-data-provider`
- `@tanstack/react-query`

**Aliased Imports:**
- `~/utils`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
return useQuery<TPreset[]>([QueryKeys.presets], () => dataService.getPresets(), {
    staleTime: 1000 * 10,
    refetchOnWindowFocus: false,
    refetchOnReconnect: false,
    refetchOnMount: false,
    ...config,
```

**Snippet 2:**
```typescript
const queryClient = useQueryClient();

  return useQuery<t.TConversation>(
    [QueryKeys.conversation, id],
    () => {
      // Try to find in all fetched infinite pages
      const convosQuery = queryClient.getQueryData<InfiniteData<ConversationCursorData>>(
        [QueryKeys.allConversations],

```

**Snippet 3:**
```typescript
return useQuery<t.TConversationTag[]>(
    [QueryKeys.conversationTags],
    () => dataService.getConversationTags(),
    {
      refetchOnWindowFocus: false,
      refetchOnReconnect: false,
      refetchOnMount: false,
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
### dependsOn (3)

- `librechat-data-provider`
- `@tanstack/react-query`
- `~/utils`



# 14. Tags
```
- typescript
- application-code
- librechat
- source-file
```

