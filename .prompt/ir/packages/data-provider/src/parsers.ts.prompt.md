# File: packages/data-provider/src/parsers.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/data-provider/src/parsers.ts`.

**Documentation:** as a from './types/assistants';

**Primary exports:** 14 exported element(s)
- EndpointSchemaKey
- getEnabledEndpoints
- orderEndpointsConfig

**File size:** 12,765 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `EndpointSchemaKey()` — named export
- `getEnabledEndpoints()`
- `orderEndpointsConfig(endpointsConfig: t.TEndpointsConfig)`
- `errorsToString(errors: ZodIssue[])`
- `getFirstDefinedValue(possibleValues: string[])`
- `getNonEmptyValue(possibleValues: string[])`
- `TPossibleValues()` — named export
- `parseConvo()` — named export
- `getResponseSender()` — named export
- `parseCompactConvo()` — named export
- `parseTextParts(
  contentParts: a.TMessageContentParts[],
  skipReasoning: boolean = false,
)`
- `SEPARATORS()` — named export
- `findLastSeparatorIndex(text: string, separators = SEPARATORS)`
- `replaceSpecialVars({ text, user }: { text: string; user?: t.TUser | null })`



# 4. Internal Structure
### Internal Functions (10)

- `getEnabledEndpoints()`
- `orderEndpointsConfig()`
- `errorsToString()`
- `getFirstDefinedValue()`
- `getNonEmptyValue()`
- `parseTextParts()`
- `findLastSeparatorIndex()`
- `replaceSpecialVars()`
- `parseConvo()`
- `parseCompactConvo()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (5)

**NPM Packages:**
- `dayjs`

**Relative Imports:**
- `./types/runs`
- `./schemas`
- `./bedrock`
- `./config`



# 7. Database Interaction Mapping
**Database:** MongoDB via Mongoose



# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const isCustom = !(currentEndpointKey in EModelEndpoint);
      const isEnabled = enabledEndpoints.includes(currentEndpointKey);
      if (!isEnabled && !isCustom) {
        return accumulatedConfig;
```

**Snippet 2:**
```typescript
return errors
    .map((error) => {
      const field = error.path.join('.');
      const message = error.message;

      return `${field
```

**Snippet 3:**
```typescript
let returnValue;
  for (const value of possibleValues) {
    if (value) {
      returnValue = value;
      break;
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Shared:** Shared package code


# 12. Migration Concerns & Recommendations
- Contains TODO/FIXME comments indicating technical debt
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (1)

- `dayjs`



# 14. Tags
```
- typescript
- application-code
- librechat
- source-file
```

