# File: packages/data-provider/src/accessPermissions.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/data-provider/src/accessPermissions.ts`.

**Documentation:** * Granular Permission System Types for Agent Sharing

**Primary exports:** 31 exported element(s)
- PrincipalType
- PrincipalModel
- TPrincipalSource

**File size:** 8,885 bytes


# 2. Domain Role
**Domain:** Authorization & Access Control

**Business relevance:**
This file is part of the Authorization & Access Control domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `PrincipalType()` — named export
- `PrincipalModel()` — named export
- `TPrincipalSource()` — named export
- `TAccessLevel()` — named export
- `ResourceType()` — named export
- `PermissionBits()` — named export
- `AccessRoleIds()` — named export
- `principalSchema()` — named export
- `accessRoleSchema()` — named export
- `permissionEntrySchema()` — named export
- `resourcePermissionsResponseSchema()` — named export
- `updateResourcePermissionsRequestSchema()` — named export
- `updateResourcePermissionsResponseSchema()` — named export
- `TPrincipal()` — named export
- `TAccessRole()` — named export
- `TPermissionEntry()` — named export
- `TResourcePermissionsResponse()` — named export
- `TUpdateResourcePermissionsRequest()` — named export
- `TUpdateResourcePermissionsResponse()` — named export
- `TPrincipalSearchParams()` — named export
- `TPrincipalSearchResult()` — named export
- `TPrincipalSearchResponse()` — named export
- `TAvailableRolesResponse()` — named export
- `getResourcePermissionsResponseSchema()` — named export
- `TGetResourcePermissionsResponse()` — named export
- `effectivePermissionsResponseSchema()` — named export
- `TEffectivePermissionsResponse()` — named export
- `TPermissionCheck()` — named export
- `permBitsToAccessLevel(permBits: number)`
- `accessRoleToPermBits(accessRoleId: string)`
- `hasPermissions(permissions: number, requiredPermission: number)`



# 4. Internal Structure
### Internal Functions (3)

- `permBitsToAccessLevel()`
- `accessRoleToPermBits()`
- `hasPermissions()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (1)

**NPM Packages:**
- `zod`



# 7. Database Interaction Mapping
**Database:** MongoDB via Mongoose



# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
id: z.string(),
  principalType: z.nativeEnum(PrincipalType),
  principalId: z.string().optional(), // undefined for 'public'
  principalName: z.string().optional(),
  role: accessRoleSchema,
  grantedBy: z.string(),
  grantedAt: z.string(), // ISO date string
  inheritedFrom: z.string().optional(),
```

**Snippet 2:**
```typescript
if ((permBits & PermissionBits.DELETE) > 0) return 'owner';
  if ((permBits & PermissionBits.EDIT) > 0) return 'editor';
  if ((permBits & PermissionBits.VIEW) > 0) return 'viewer';
  return 'none';
```

**Snippet 3:**
```typescript
switch (accessRoleId) {
    case AccessRoleIds.AGENT_VIEWER:
      return PermissionBits.VIEW;
    case AccessRoleIds.AGENT_EDITOR:
      return PermissionBits.VIEW | PermissionBits.EDIT;
    case AccessRoleIds.AGENT_OWNER:
      return PermissionBits.VIEW | PermissionBits.EDIT | PermissionBits.DELE
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Shared:** Shared package code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (1)

- `zod`



# 14. Tags
```
- typescript
- authorization
- application-code
- librechat
- source-file
```

