# File: api/server/controllers/UserController.js

# 1. Purpose
**File Type:** JS (API endpoint / Request handler)

**What this file represents:**
This file is a api endpoint / request handler located at `api/server/controllers/UserController.js`.


**File size:** 14,572 bytes


# 2. Domain Role
**Domain:** Authentication & User Management

**Business relevance:**
This file is part of the Authentication & User Management domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (9)

- `getUserController()`
- `getTermsStatusController()`
- `acceptTermsController()`
- `deleteUserFiles()`
- `updateUserPluginsController()`
- `deleteUserController()`
- `verifyEmailController()`
- `resendVerificationController()`
- `maybeUninstallOAuthMCP()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** HTTP request (req.body, req.params, req.query)
2. **Transformations:** Request validation and data extraction
3. **External calls:** Service layer methods, database queries
4. **Output:** HTTP response (res.json, res.status)


# 6. Relationships & Collaboration
### Imported Dependencies (15)

**NPM Packages:**
- `@librechat/data-schemas`
- `librechat-data-provider`
- `@librechat/api`
- `@librechat/api`

**Aliased Imports:**
- `~/models`
- `~/server/services/PluginService`
- `~/server/services/UserService`
- `~/server/services/AuthService`
- `~/server/services/Files/S3/crud`
- `~/server/services/Files/process`
- `~/db/models`
- `~/config`
- `~/server/services/Config`
- `~/models/ToolCall`
- *...and 1 more*



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
try {
    const user = await User.findById(req.user.id);
    if (!user) {
      return res.status(404).json({ message: 'User not found'
```

**Snippet 2:**
```javascript
// Extract server name from pluginKey (format: "mcp_<serverName>")
            const serverName = pluginKey.replace(Constants.mcp_prefix, '');
            logger.info(
              `[updateUserPluginsController] Attempting disconnect of MCP server "${serverName
```

**Snippet 3:**
```javascript
try {
    const verifyEmailService = await verifyEmail(req);
    if (verifyEmailService instanceof Error) {
      return res.status(400).json(verifyEmailService);
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** API controller
- Service: API layer
- Controller: `UserControllerController`


# 12. Migration Concerns & Recommendations
- Contains TODO/FIXME comments indicating technical debt
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (15)

- `@librechat/data-schemas`
- `librechat-data-provider`
- `@librechat/api`
- `~/models`
- `~/server/services/PluginService`
- `~/server/services/UserService`
- `~/server/services/AuthService`
- `~/server/services/Files/S3/crud`
- `~/server/services/Files/process`
- `~/db/models`
- `~/config`
- `~/server/services/Config`
- `~/models/ToolCall`
- `~/cache`
- `@librechat/api`



# 14. Tags
```
- javascript
- controller
- application-code
- librechat
- source-file
```

