# File: packages/api/src/cache/redisClients.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/cache/redisClients.ts`.


**File size:** 7,610 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (1)

- `clearPingInterval()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (4)

**NPM Packages:**
- `ioredis`
- `@librechat/data-schemas`
- `@keyv/redis`

**Relative Imports:**
- `./cacheConfig`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
logger.warn('ioredis reconnecting due to READONLY error');
        return 2; // Return retry delay instead of boolean
```

**Snippet 2:**
```typescript
if (pingInterval) {
      clearInterval(pingInterval);
      pingInterval = null;
```

**Snippet 3:**
```typescript
username,
    password,
    socket: {
      tls: ca != null,
      ca,
      connectTimeout: cacheConfig.REDIS_CONNECT_TIMEOUT,
      reconnectStrategy: (retries: number) => {
        if (
          cacheConfig.REDIS_RETRY_MAX_ATTEMPTS > 0 &&
          retries > cacheConfig.REDIS_RETRY_MAX_ATTEMPTS

```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (3)

- `ioredis`
- `@librechat/data-schemas`
- `@keyv/redis`



# 14. Tags
```
- typescript
- application-code
- librechat
- source-file
```

