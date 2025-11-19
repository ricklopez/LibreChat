# File: packages/api/src/utils/tokens.ts

# 1. Purpose
**File Type:** TS (Utility / Helper function)

**What this file represents:**
This file is a utility / helper function located at `packages/api/src/utils/tokens.ts`.

**Documentation:** Configuration object mapping model keys to their respective prompt, completion rates, and context limit

**Primary exports:** 14 exported element(s)
- TokenConfig
- EndpointTokenConfig
- maxTokensMap

**File size:** 16,130 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `TokenConfig()` — named export
- `EndpointTokenConfig()` — named export
- `maxTokensMap()` — named export
- `modelMaxOutputs()` — named export
- `maxOutputTokensMap()` — named export
- `findMatchingPattern(
  modelName: string,
  tokensMap: Record<string, number> | EndpointTokenConfig,
)`
- `getModelTokenValue(
  modelName: string,
  tokensMap?: EndpointTokenConfig | Record<string, number>,
  key = 'context' as keyof TokenConfig,
)`
- `getModelMaxTokens(
  modelName: string,
  endpoint = EModelEndpoint.openAI,
  endpointTokenConfig?: EndpointTokenConfig,
)`
- `getModelMaxOutputTokens(
  modelName: string,
  endpoint = EModelEndpoint.openAI,
  endpointTokenConfig?: EndpointTokenConfig,
)`
- `matchModelName(
  modelName: string,
  endpoint = EModelEndpoint.openAI,
)`
- `modelSchema()` — named export
- `inputSchema()` — named export
- `processModelData(input: z.infer<typeof inputSchema>)`
- `tiktokenModels()` — named export



# 4. Internal Structure
### Internal Functions (6)

- `findMatchingPattern()`
- `getModelTokenValue()`
- `getModelMaxTokens()`
- `getModelMaxOutputTokens()`
- `matchModelName()`
- `processModelData()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (2)

**NPM Packages:**
- `zod`
- `librechat-data-provider`



# 7. Database Interaction Mapping
**Database:** MongoDB via Mongoose



# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const keys = Object.keys(tokensMap);
  const lowerModelName = modelName.toLowerCase();
  for (let i = keys.length - 1; i >= 0; i--) {
    const modelKey = keys[i];
    if (lowerModelName.includes(modelKey)) {
      return modelKey;
```

**Snippet 2:**
```typescript
if (typeof modelName !== 'string' || !tokensMap) {
    return undefined;
```

**Snippet 3:**
```typescript
const result = tokensMap[matchedPattern];
    if (typeof result === 'number') {
      return result;
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (2)

- `zod`
- `librechat-data-provider`



# 14. Tags
```
- typescript
- utility
- application-code
- librechat
- source-file
```

