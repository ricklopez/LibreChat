# File: packages/data-provider/src/api-endpoints.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/data-provider/src/api-endpoints.ts`.

**Documentation:** as q from './types/queries';

**Primary exports:** 113 exported element(s)
- apiBaseUrl
- health
- user

**File size:** 13,098 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `apiBaseUrl()` — named export
- `health()` — named export
- `user()` — named export
- `balance()` — named export
- `userPlugins()` — named export
- `deleteUser()` — named export
- `messages()` — named export
- `messagesArtifacts()` — named export
- `shareMessages()` — named export
- `getSharedLink()` — named export
- `getSharedLinks()` — named export
- `createSharedLink()` — named export
- `updateSharedLink()` — named export
- `keys()` — named export
- `userKeyQuery()` — named export
- `revokeUserKey()` — named export
- `revokeAllUserKeys()` — named export
- `conversationsRoot()` — named export
- `conversations()` — named export
- `conversationById()` — named export
- `genTitle()` — named export
- `updateConversation()` — named export
- `deleteConversation()` — named export
- `deleteAllConversation()` — named export
- `importConversation()` — named export
- `forkConversation()` — named export
- `duplicateConversation()` — named export
- `search()` — named export
- `searchEnabled()` — named export
- `presets()` — named export
- `deletePreset()` — named export
- `aiEndpoints()` — named export
- `models()` — named export
- `tokenizer()` — named export
- `login()` — named export
- `logout()` — named export
- `register()` — named export
- `loginFacebook()` — named export
- `loginGoogle()` — named export
- `refreshToken()` — named export
- `requestPasswordReset()` — named export
- `resetPassword()` — named export
- `verifyEmail()` — named export
- `resendVerificationEmail()` — named export
- `plugins()` — named export
- `mcpReinitialize()` — named export
- `mcpConnectionStatus()` — named export
- `mcpServerConnectionStatus()` — named export
- `mcpAuthValues()` — named export
- `cancelMCPOAuth()` — named export
- `config()` — named export
- `prompts()` — named export
- `addPromptToGroup()` — named export
- `assistants()` — named export
- `agents()` — named export
- `mcp()` — named export
- `revertAgentVersion()` — named export
- `files()` — named export
- `fileUpload()` — named export
- `fileDelete()` — named export
- `fileDownload()` — named export
- `fileConfig()` — named export
- `agentFiles()` — named export
- `images()` — named export
- `avatar()` — named export
- `speech()` — named export
- `speechToText()` — named export
- `textToSpeech()` — named export
- `textToSpeechManual()` — named export
- `textToSpeechVoices()` — named export
- `getCustomConfigSpeech()` — named export
- `getPromptGroup()` — named export
- `getPromptGroupsWithFilters()` — named export
- `getPromptsWithFilters()` — named export
- `getPrompt()` — named export
- `getRandomPrompts()` — named export
- `postPrompt()` — named export
- `updatePromptGroup()` — named export
- `updatePromptLabels()` — named export
- `updatePromptTag()` — named export
- `deletePromptGroup()` — named export
- `deletePrompt()` — named export
- `getCategories()` — named export
- `getAllPromptGroups()` — named export
- `roles()` — named export
- `getRole()` — named export
- `updatePromptPermissions()` — named export
- `updateMemoryPermissions()` — named export
- `updateAgentPermissions()` — named export
- `updatePeoplePickerPermissions()` — named export
- `updateMarketplacePermissions()` — named export
- `conversationTags()` — named export
- `conversationTagsList()` — named export
- `addTagToConversation()` — named export
- `userTerms()` — named export
- `acceptUserTerms()` — named export
- `banner()` — named export
- `feedback()` — named export
- `enableTwoFactor()` — named export
- `verifyTwoFactor()` — named export
- `confirmTwoFactor()` — named export
- `disableTwoFactor()` — named export
- `regenerateBackupCodes()` — named export
- `verifyTwoFactorTemp()` — named export
- `memories()` — named export
- `memory()` — named export
- `memoryPreferences()` — named export
- `searchPrincipals()` — named export
- `getAccessRoles()` — named export
- `getResourcePermissions()` — named export
- `updateResourcePermissions()` — named export
- `getEffectivePermissions()` — named export
- `graphToken()` — named export



# 4. Internal Structure
### Internal Functions (108)

- `apiBaseUrl()`
- `health()`
- `user()`
- `balance()`
- `userPlugins()`
- `deleteUser()`
- `messages()`
- `messagesArtifacts()`
- `shareMessages()`
- `getSharedLink()`
- *...and 98 more functions*



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (2)

**Relative Imports:**
- `./types/queries`
- `./accessPermissions`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const query = Object.entries(params)
    .filter(([, value]) => {
      if (Array.isArray(value)) {
        return value.length > 0;
```

**Snippet 2:**
```typescript
if (value !== undefined && value !== null && value !== '') {
        acc[key] = value;
```

**Snippet 3:**
```typescript
let url = prompts();
  if (Object.keys(filter).length > 0) {
    const queryParams = new URLSearchParams(filter as Record<string, string>).toString();
    url += `?${queryParams
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)


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

