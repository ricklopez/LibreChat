# File: packages/api/src/utils/env.ts

# 1. Purpose
**File Type:** TS (Utility / Helper function)

**What this file represents:**
This file is a utility / helper function located at `packages/api/src/utils/env.ts`.

**Documentation:** * List of allowed user fields that can be used in MCP environment variables.

**Primary exports:** 3 exported element(s)
- createSafeUser
- processMCPEnv
- resolveHeaders

**File size:** 9,155 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `createSafeUser(user: IUser | null | undefined)`
- `processMCPEnv(params: {
  options: Readonly<MCPOptions>;
  user?: TUser;
  customUserVars?: Record<string, string>;
  body?: RequestBody;
})`
- `resolveHeaders(options?: {
  headers: Record<string, string> | undefined;
  user?: Partial<TUser> | { id: string };
  body?: RequestBody;
  customUserVars?: Record<string, string>;
})`



# 4. Internal Structure
### Internal Functions (6)

- `createSafeUser()`
- `processUserPlaceholders()`
- `processBodyPlaceholders()`
- `processSingleValue()`
- `processMCPEnv()`
- `resolveHeaders()`



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
if (field in user) {
      safeUser[field] = user[field];
```

**Snippet 2:**
```typescript
if (!user || typeof value !== 'string') {
    return value;
```

**Snippet 3:**
```typescript
for (const field of ALLOWED_BODY_FIELDS) {
    const placeholder = `{{LIBRECHAT_BODY_${field.toUpperCase()
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


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

