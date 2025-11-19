# File: packages/data-schemas/src/methods/share.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/data-schemas/src/methods/share.ts`.

**Documentation:** as t from '~/types';

**Primary exports:** 2 exported element(s)
- createShareMethods
- ShareMethods

**File size:** 17,594 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Classes

- `class ShareServiceError extends Error`

### Exported Functions

- `createShareMethods(mongoose: typeof import('mongoose')`
- `ShareMethods()` — named export



# 4. Internal Structure
### Internal Functions (14)

- `memoizedAnonymizeId()`
- `anonymizeConvo()`
- `anonymizeMessages()`
- `getMessagesUpToTarget()`
- `createShareMethods()`
- `getSharedMessages()`
- `getSharedLinks()`
- `deleteAllSharedLinks()`
- `deleteConvoSharedLink()`
- `createSharedLink()`
- *...and 4 more functions*



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (4)

**NPM Packages:**
- `nanoid`
- `librechat-data-provider`
- `mongoose`

**Aliased Imports:**
- `~/config/winston`



# 7. Database Interaction Mapping
**Database:** MongoDB via Mongoose

**Operations:** SELECT (find, findOne, findById)
**Operations:** INSERT (create, insertMany)
**Operations:** DELETE (deleteOne, findByIdAndDelete)


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const memo = new Map<string, string>();
  return (id: string) => {
    if (!memo.has(id)) {
      memo.set(id, `${prefix
```

**Snippet 2:**
```typescript
return {
          ...attachment,
          messageId: newMessageId,
          conversationId: newConvoId,
```

**Snippet 3:**
```typescript
if (!messages || messages.length === 0) {
    return [];
```



# 10. Architectural Concerns
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Shared:** Shared package code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (3)

- `nanoid`
- `librechat-data-provider`
- `~/config/winston`



# 14. Tags
```
- typescript
- application-code
- librechat
- source-file
```

