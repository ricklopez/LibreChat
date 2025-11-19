# File: client/src/utils/heicConverter.ts

# 1. Purpose
**File Type:** TS (Utility / Helper function)

**What this file represents:**
This file is a utility / helper function located at `client/src/utils/heicConverter.ts`.

**Documentation:** * Check if a file is in HEIC format

**Primary exports:** 3 exported element(s)
- isHEICFile
- convertHEICToJPEG
- processFileForUpload

**File size:** 2,270 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `isHEICFile()` — named export
- `convertHEICToJPEG()` — named export
- `processFileForUpload()` — named export



# 4. Internal Structure
### Internal Functions (2)

- `convertHEICToJPEG()`
- `processFileForUpload()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (1)

**NPM Packages:**
- `heic-to`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
type: 'image/jpeg',
      lastModified: file.lastModified,
```

**Snippet 2:**
```typescript
const isHEIC = await isHEICFile(file);

  if (isHEIC) {
    console.log('HEIC file detected, converting to JPEG...');
    return convertHEICToJPEG(file, quality, onProgress);
```



# 10. Architectural Concerns
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (1)

- `heic-to`



# 14. Tags
```
- typescript
- utility
- application-code
- librechat
- source-file
```

