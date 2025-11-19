# File: packages/data-provider/src/react-query/react-query-service.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/data-provider/src/react-query/react-query-service.ts`.

**Documentation:** as dataService from '../data-service';

**Primary exports:** 31 exported element(s)
- useGetSharedMessages
- useGetSharedLinkQuery
- useGetConversationByIdQuery

**File size:** 15,981 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `useGetSharedMessages()` — named export
- `useGetSharedLinkQuery()` — named export
- `useGetConversationByIdQuery()` — named export
- `useGetConversationByIdMutation()` — named export
- `useUpdateMessageMutation()` — named export
- `useUpdateMessageContentMutation()` — named export
- `useUpdateUserKeysMutation()` — named export
- `useClearConversationsMutation()` — named export
- `useRevokeUserKeyMutation()` — named export
- `useRevokeAllUserKeysMutation()` — named export
- `useGetModelsQuery()` — named export
- `useCreatePresetMutation()` — named export
- `useDeletePresetMutation()` — named export
- `useUpdateTokenCountMutation()` — named export
- `useRegisterUserMutation()` — named export
- `useUserKeyQuery()` — named export
- `useRequestPasswordResetMutation()` — named export
- `useResetPasswordMutation()` — named export
- `useAvailablePluginsQuery()` — named export
- `useUpdateUserPluginsMutation()` — named export
- `useReinitializeMCPServerMutation()` — named export
- `useCancelMCPOAuthMutation()` — named export
- `useGetCustomConfigSpeechQuery()` — named export
- `useUpdateFeedbackMutation()` — named export
- `useSearchPrincipalsQuery()` — named export
- `useGetAccessRolesQuery()` — named export
- `useGetResourcePermissionsQuery()` — named export
- `useUpdateResourcePermissionsMutation()` — named export
- `useGetEffectivePermissionsQuery()` — named export
- `useMCPServerConnectionStatusQuery()` — named export



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
### Imported Dependencies (12)

**NPM Packages:**
- `@tanstack/react-query`

**Relative Imports:**
- `../config`
- `../types/assistants`
- `../types/queries`
- `../data-service`
- `../types/mutations`
- `../types/queries`
- `../keys`
- `../schemas`
- `../types`
- `../accessPermissions`
- *...and 1 more*



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
return useQuery<t.TSharedMessagesResponse>(
    [QueryKeys.sharedMessages, shareId],
    () => dataService.getSharedMessages(shareId),
    {
      refetchOnWindowFocus: false,
      refetchOnReconnect: false,
      refetchOnMount: false,
      ...config,
```

**Snippet 2:**
```typescript
return useQuery<s.TConversation>(
    [QueryKeys.conversation, id],
    () => dataService.getConversationById(id),
    {
      refetchOnWindowFocus: false,
      refetchOnReconnect: false,
      refetchOnMount: false,
      ...config,
```

**Snippet 3:**
```typescript
const queryClient = useQueryClient();
  return useMutation(() => dataService.getConversationById(id), {
    // onSuccess: (res: s.TConversation) => {
    onSuccess: () => {
      queryClient.invalidateQueries([QueryKeys.conversation, id]);
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Async Behavior:** Asynchronous operations present


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Shared:** Shared package code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (1)

- `@tanstack/react-query`



# 14. Tags
```
- typescript
- application-code
- librechat
- source-file
```

