# File: packages/api/src/mcp/zod.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/mcp/zod.ts`.

**Documentation:** Don't treat objects with additionalProperties as empty

**Primary exports:** 3 exported element(s)
- resolveJsonSchemaRefs
- convertJsonSchemaToZod
- convertWithResolvedRefs

**File size:** 17,403 bytes


# 2. Domain Role
**Domain:** Model Context Protocol Integration

**Business relevance:**
This file is part of the Model Context Protocol Integration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `resolveJsonSchemaRefs()` — named export
- `convertJsonSchemaToZod(
  schema: JsonSchemaType & Record<string, unknown>,
  options: ConvertJsonSchemaToZodOptions = {},
)`
- `convertWithResolvedRefs(
  schema: JsonSchemaType & Record<string, unknown>,
  options?: ConvertJsonSchemaToZodOptions,
)`



# 4. Internal Structure
### Internal Functions (5)

- `isEmptyObjectSchema()`
- `dropSchemaFields()`
- `convertToZodUnion()`
- `convertJsonSchemaToZod()`
- `convertWithResolvedRefs()`



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
return (
    jsonSchema != null &&
    typeof jsonSchema === 'object' &&
    jsonSchema.type === 'object' &&
    (jsonSchema.properties == null || Object.keys(jsonSchema.properties).length === 0) &&
    !jsonSchema.additionalProperties // Don't treat objects with additionalProperties as empty
  );
```

**Snippet 2:**
```typescript
if (schema == null || typeof schema !== 'object') {
    return schema;
```

**Snippet 3:**
```typescript
if (!Array.isArray(schemas) || schemas.length === 0) {
    return undefined;
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (1)

- `zod`



# 14. Tags
```
- typescript
- mcp-integration
- application-code
- librechat
- source-file
```

