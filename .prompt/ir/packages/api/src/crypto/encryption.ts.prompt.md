# File: packages/api/src/crypto/encryption.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/crypto/encryption.ts`.

**Documentation:** Use hex decoding for both key and IV for legacy methods.

**Primary exports:** 2 exported element(s)
- encryptV3
- decryptV3

**File size:** 4,490 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `encryptV3(value: string)`
- `decryptV3(encryptedValue: string)`



# 4. Internal Structure
### Internal Functions (8)

- `encrypt()`
- `decrypt()`
- `encryptV2()`
- `decryptV2()`
- `encryptV3()`
- `decryptV3()`
- `getRandomValues()`
- `hashBackupCode()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (1)

**NPM Packages:**
- `node:crypto`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const parts = encryptedValue.split(':');
  if (parts.length === 1) {
    return parts[0];
```

**Snippet 2:**
```typescript
if (key.length !== 32) {
    throw new Error(`Invalid key length: expected 32 bytes, got ${key.length
```

**Snippet 3:**
```typescript
const parts = encryptedValue.split(':');
  if (parts[0] !== 'v3') {
    throw new Error('Not a v3 encrypted value');
```



# 10. Architectural Concerns
**Async Behavior:** Asynchronous operations present


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- May contain deprecated or legacy code patterns


# 13. Dependencies
### dependsOn (1)

- `node:crypto`



# 14. Tags
```
- typescript
- application-code
- librechat
- source-file
```

