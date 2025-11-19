# File: packages/data-provider/src/file-config.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/data-provider/src/file-config.ts`.

**Primary exports:** 28 exported element(s)
- supportsFiles
- excelFileTypes
- fullMimeTypesList

**File size:** 17,488 bytes


# 2. Domain Role
**Domain:** File Storage & Management

**Business relevance:**
This file is part of the File Storage & Management domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `supportsFiles()` — named export
- `excelFileTypes()` — named export
- `fullMimeTypesList()` — named export
- `codeInterpreterMimeTypesList()` — named export
- `retrievalMimeTypesList()` — named export
- `imageExtRegex()` — named export
- `excelMimeTypes()` — named export
- `textMimeTypes()` — named export
- `applicationMimeTypes()` — named export
- `imageMimeTypes()` — named export
- `audioMimeTypes()` — named export
- `videoMimeTypes()` — named export
- `defaultOCRMimeTypes()` — named export
- `defaultTextMimeTypes()` — named export
- `defaultSTTMimeTypes()` — named export
- `supportedMimeTypes()` — named export
- `codeInterpreterMimeTypes()` — named export
- `codeTypeMapping()` — named export
- `retrievalMimeTypes()` — named export
- `megabyte()` — named export
- `mbToBytes()` — named export
- `fileConfig()` — named export
- `endpointFileConfigSchema()` — named export
- `fileConfigSchema()` — named export
- `TFileConfig()` — named export
- `convertStringsToRegex()` — named export
- `getEndpointFileConfig(params: {
  fileConfig?: FileConfig | null;
  endpoint?: string | null;
  endpointType?: string | null;
})`
- `mergeFileConfig(dynamic: z.infer<typeof fileConfigSchema> | undefined)`



# 4. Internal Structure
### Internal Functions (3)

- `mergeWithDefault()`
- `getEndpointFileConfig()`
- `mergeFileConfig()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (3)

**NPM Packages:**
- `zod`

**Relative Imports:**
- `./schemas`
- `./utils`



# 7. Database Interaction Mapping
**Database:** MongoDB via Mongoose



# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
/** 1. Check direct endpoint lookup (could be normalized or not) */
    if (endpoint && mergedFileConfig.endpoints[endpoint]) {
      return mergeWithDefault(mergedFileConfig.endpoints[endpoint], defaultConfig, endpoint);
```

**Snippet 2:**
```typescript
if (!standardEndpoints.has(key) && normalizeEndpointName(key) === normalizedEndpoint) {
        return mergeWithDefault(mergedFileConfig.endpoints[key], defaultConfig, key);
```

**Snippet 3:**
```typescript
return mergeWithDefault(
      mergedFileConfig.endpoints[EModelEndpoint.agents],
      defaultConfig,
      EModelEndpoint.agents,
    );
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Shared:** Shared package code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (1)

- `zod`



# 14. Tags
```
- typescript
- file-storage
- application-code
- librechat
- source-file
```

