# File: packages/api/src/utils/common.ts

# 1. Purpose
**File Type:** TS (Utility / Helper function)

**What this file represents:**
This file is a utility / helper function located at `packages/api/src/utils/common.ts`.

**Documentation:** * Checks if the given value is truthy by being either the boolean `true` or a string

**Primary exports:** 3 exported element(s)
- isEnabled
- isUserProvided
- optionalChainWithEmptyCheck

**File size:** 1,518 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `isEnabled(value?: string | boolean | null | undefined)`
- `isUserProvided()` — named export
- `optionalChainWithEmptyCheck(
  ...values: (string | number | undefined)`



# 4. Internal Structure
### Internal Functions (2)

- `isEnabled()`
- `optionalChainWithEmptyCheck()`



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
if (typeof value === 'boolean') {
    return value;
```

**Snippet 2:**
```typescript
for (const value of values) {
    if (value !== undefined && value !== null && value !== '') {
      return value;
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)


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
- utility
- application-code
- librechat
- source-file
```

