# File: client/src/utils/localStorage.ts

# 1. Purpose
**File Type:** TS (Utility / Helper function)

**What this file represents:**
This file is a utility / helper function located at `client/src/utils/localStorage.ts`.

**Primary exports:** 4 exported element(s)
- getLocalStorageItems
- clearLocalStorage
- clearConversationStorage

**File size:** 2,639 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `getLocalStorageItems()`
- `clearLocalStorage(skipFirst?: boolean)`
- `clearConversationStorage(conversationId?: string | null)`
- `clearAllConversationStorage()`



# 4. Internal Structure
### Internal Functions (4)

- `getLocalStorageItems()`
- `clearLocalStorage()`
- `clearConversationStorage()`
- `clearAllConversationStorage()`



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
const keys = Object.keys(localStorage);
  keys.forEach((key) => {
    if (skipFirst === true && key.endsWith('0')) {
      return;
```

**Snippet 2:**
```typescript
if (key.includes(conversationId)) {
      localStorage.removeItem(key);
```

**Snippet 3:**
```typescript
const keys = Object.keys(localStorage);
  keys.forEach((key) => {
    if (
      key.startsWith(LocalStorageKeys.LAST_MCP_) ||
      key.startsWith(LocalStorageKeys.LAST_CODE_TOGGLE_) ||
      key.startsWith(LocalStorageKeys.TEXT_DRAFT) ||
      key.startsWith(LocalStorageKeys.ASST_ID_PREFIX) ||
   
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
- application-code
- librechat
- source-file
```

