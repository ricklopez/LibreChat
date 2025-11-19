# File: packages/data-provider/src/data-service.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/data-provider/src/data-service.ts`.

**Documentation:** as t from './types';

**Primary exports:** 144 exported element(s)
- revokeUserKey
- revokeAllUserKeys
- deleteUser

**File size:** 27,234 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `revokeUserKey(name: string)`
- `revokeAllUserKeys()`
- `deleteUser()`
- `getSharedMessages(shareId: string)`
- `listSharedLinks()` — named export
- `getSharedLink(conversationId: string)`
- `createSharedLink(
  conversationId: string,
  targetMessageId?: string,
)`
- `updateSharedLink(shareId: string)`
- `deleteSharedLink(shareId: string)`
- `updateUserKey(payload: t.TUpdateUserKeyRequest)`
- `getPresets()`
- `createPreset(payload: s.TPreset)`
- `updatePreset(payload: s.TPreset)`
- `deletePreset(arg: s.TPreset | undefined)`
- `getSearchEnabled()`
- `getUser()`
- `getUserBalance()`
- `updateTokenCount()` — named export
- `login()` — named export
- `logout()` — named export
- `register()` — named export
- `userKeyQuery()` — named export
- `getLoginGoogle()` — named export
- `requestPasswordReset()` — named export
- `resetPassword()` — named export
- `verifyEmail()` — named export
- `resendVerificationEmail()` — named export
- `getAvailablePlugins()` — named export
- `updateUserPlugins()` — named export
- `reinitializeMCPServer()` — named export
- `getMCPConnectionStatus()` — named export
- `getMCPServerConnectionStatus()` — named export
- `getMCPAuthValues()` — named export
- `cancelMCPOAuth(serverName: string)`
- `getStartupConfig()` — named export
- `getAIEndpoints()` — named export
- `getModels()` — named export
- `createAssistant()` — named export
- `getAssistantById()` — named export
- `updateAssistant()` — named export
- `deleteAssistant()` — named export
- `listAssistants()` — named export
- `getAssistantDocs({
  endpoint,
  version,
}: {
  endpoint: s.AssistantsEndpoint | string;
  version: number | string;
})`
- `getAvailableTools()` — named export
- `getMCPTools()` — named export
- `getVerifyAgentToolAuth()` — named export
- `callTool()` — named export
- `getToolCalls()` — named export
- `getFiles()` — named export
- `getAgentFiles()` — named export
- `getFileConfig()` — named export
- `uploadImage()` — named export
- `uploadFile()` — named export
- `updateAction()` — named export
- `getActions()`
- `deleteAction()` — named export
- `createAgent()` — named export
- `getAgentById()` — named export
- `getExpandedAgentById()` — named export
- `updateAgent()` — named export
- `duplicateAgent()` — named export
- `deleteAgent()` — named export
- `listAgents()` — named export
- `revertAgentVersion()` — named export
- `getAgentCategories()` — named export
- `getMarketplaceAgents()` — named export
- `getAvailableAgentTools()` — named export
- `updateAgentAction()` — named export
- `deleteAgentAction()` — named export
- `importConversationsFile()` — named export
- `uploadAvatar()` — named export
- `uploadAssistantAvatar()` — named export
- `uploadAgentAvatar()` — named export
- `getFileDownload()` — named export
- `getCodeOutputDownload()` — named export
- `deleteFiles()` — named export
- `speechToText()` — named export
- `textToSpeech()` — named export
- `getVoices()` — named export
- `getCustomConfigSpeech()` — named export
- `duplicateConversation(
  payload: t.TDuplicateConvoRequest,
)`
- `forkConversation(payload: t.TForkConvoRequest)`
- `deleteConversation(payload: t.TDeleteConversationRequest)`
- `clearAllConversations()`
- `listConversations()` — named export
- `getConversations(cursor: string)`
- `getConversationById(id: string)`
- `updateConversation(
  payload: t.TUpdateConversationRequest,
)`
- `archiveConversation(
  payload: t.TArchiveConversationRequest,
)`
- `genTitle(payload: m.TGenTitleRequest)`
- `listMessages()` — named export
- `updateMessage(payload: t.TUpdateMessageRequest)`
- `updateMessageContent(payload: t.TUpdateMessageContent)`
- `editArtifact()` — named export
- `getMessagesByConvoId(conversationId: string)`
- `getPrompt(id: string)`
- `getPrompts(filter: t.TPromptsWithFilterRequest)`
- `getAllPromptGroups()`
- `getPromptGroups(
  filter: t.TPromptGroupsWithFilterRequest,
)`
- `getPromptGroup(id: string)`
- `createPrompt(payload: t.TCreatePrompt)`
- `addPromptToGroup(
  groupId: string,
  payload: t.TCreatePrompt,
)`
- `updatePromptGroup(
  variables: t.TUpdatePromptGroupVariables,
)`
- `deletePrompt(payload: t.TDeletePromptVariables)`
- `makePromptProduction(id: string)`
- `updatePromptLabels(
  variables: t.TUpdatePromptLabelsRequest,
)`
- `deletePromptGroup(id: string)`
- `getCategories()`
- `getRandomPrompts(
  variables: t.TGetRandomPromptsRequest,
)`
- `getRole(roleName: string)`
- `updatePromptPermissions(
  variables: m.UpdatePromptPermVars,
)`
- `updateAgentPermissions(
  variables: m.UpdateAgentPermVars,
)`
- `updateMemoryPermissions(
  variables: m.UpdateMemoryPermVars,
)`
- `updatePeoplePickerPermissions(
  variables: m.UpdatePeoplePickerPermVars,
)`
- `updateMarketplacePermissions(
  variables: m.UpdateMarketplacePermVars,
)`
- `getConversationTags()`
- `createConversationTag(
  payload: t.TConversationTagRequest,
)`
- `updateConversationTag(
  tag: string,
  payload: t.TConversationTagRequest,
)`
- `deleteConversationTag(tag: string)`
- `addTagToConversation(
  conversationId: string,
  payload: t.TTagConversationRequest,
)`
- `rebuildConversationTags()`
- `healthCheck()`
- `getUserTerms()`
- `acceptTerms()`
- `getBanner()`
- `updateFeedback(
  conversationId: string,
  messageId: string,
  payload: t.TUpdateFeedbackRequest,
)`
- `enableTwoFactor()`
- `verifyTwoFactor(payload: t.TVerify2FARequest)`
- `confirmTwoFactor(payload: t.TVerify2FARequest)`
- `disableTwoFactor(payload?: t.TDisable2FARequest)`
- `regenerateBackupCodes()`
- `verifyTwoFactorTemp(
  payload: t.TVerify2FATempRequest,
)`
- `getMemories()` — named export
- `deleteMemory()` — named export
- `updateMemory()` — named export
- `updateMemoryPreferences()` — named export
- `createMemory()` — named export
- `searchPrincipals(
  params: q.PrincipalSearchParams,
)`
- `getAccessRoles(
  resourceType: permissions.ResourceType,
)`
- `getResourcePermissions(
  resourceType: permissions.ResourceType,
  resourceId: string,
)`
- `updateResourcePermissions(
  resourceType: permissions.ResourceType,
  resourceId: string,
  data: permissions.TUpdateResourcePermissionsRequest,
)`
- `getEffectivePermissions(
  resourceType: permissions.ResourceType,
  resourceId: string,
)`
- `getGraphApiToken(params: q.GraphTokenParams)`
- `getDomainServerBaseUrl()`



# 4. Internal Structure
### Internal Functions (81)

- `revokeUserKey()`
- `revokeAllUserKeys()`
- `deleteUser()`
- `getSharedMessages()`
- `getSharedLink()`
- `createSharedLink()`
- `updateSharedLink()`
- `deleteSharedLink()`
- `updateUserKey()`
- `getPresets()`
- *...and 71 more functions*



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (11)

**Relative Imports:**
- `./api-endpoints`
- `./types/assistants`
- `./types/agents`
- `./types/mutations`
- `./types/queries`
- `./types/files`
- `./config`
- `./request`
- `./schemas`
- `./roles`
- *...and 1 more*



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
return request.delete(endpoints.revokeUserKey(name));
```

**Snippet 2:**
```typescript
return request.delete(endpoints.revokeAllUserKeys());
```

**Snippet 3:**
```typescript
return request.get(endpoints.shareMessages(shareId));
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Async Behavior:** Asynchronous operations present


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Shared:** Shared package code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
*No dependency information available.*


# 14. Tags
```
- typescript
- application-code
- librechat
- source-file
```

