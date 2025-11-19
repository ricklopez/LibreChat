# File: packages/api/src/utils/azure.ts

# 1. Purpose
**File Type:** TS (Utility / Helper function)

**What this file represents:**
This file is a utility / helper function located at `packages/api/src/utils/azure.ts`.

**Documentation:** * Sanitizes the model name to be used in the URL by removing or replacing disallowed characters.

**Primary exports:** 5 exported element(s)
- sanitizeModelName
- genAzureEndpoint
- genAzureChatCompletion

**File size:** 5,451 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Classes

- `class for`

### Exported Functions

- `sanitizeModelName()` — named export
- `genAzureEndpoint()` — named export
- `genAzureChatCompletion()` — named export
- `getAzureCredentials()` — named export
- `constructAzureURL({
  baseURL,
  azureOptions,
}: {
  baseURL: string;
  azureOptions?: AzureOptions;
})`



# 4. Internal Structure
### Internal Functions (1)

- `constructAzureURL()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (1)

**Relative Imports:**
- `./common`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
// Replace periods with empty strings and other disallowed characters as needed.
  return modelName.replace(/\./g, '');
```

**Snippet 2:**
```typescript
return {
    azureOpenAIApiKey: process.env.AZURE_API_KEY ?? process.env.AZURE_OPENAI_API_KEY,
    azureOpenAIApiInstanceName: process.env.AZURE_OPENAI_API_INSTANCE_NAME,
    azureOpenAIApiDeploymentName: process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME,
    azureOpenAIApiVersion: process.env.AZURE_OPEN
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- May contain deprecated or legacy code patterns


# 13. Dependencies
*No dependency information available.*


# 14. Tags
```
- typescript
- utility
- application-code
- librechat
- source-file
```

