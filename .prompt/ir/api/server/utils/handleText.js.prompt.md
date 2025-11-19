# File: api/server/utils/handleText.js

# 1. Purpose
**File Type:** JS (Utility / Helper function)

**What this file represents:**
This file is a utility / helper function located at `api/server/utils/handleText.js`.

**Documentation:** Helper function to escape special characters in regex


**File size:** 5,209 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (14)

- `escapeRegExp()`
- `formatSteps()`
- `formatAction()`
- `generateConfig()`
- `addSpaceIfNeeded()`
- `createOnProgress()`
- `progressCallback()`
- `sendIntermediateMessage()`
- `onProgress()`
- `getPartialText()`
- *...and 4 more functions*



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (3)

**NPM Packages:**
- `librechat-data-provider`
- `@librechat/api`
- `lodash/partialRight`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
let output = '';

  for (let i = 0; i < steps.length; i++) {
    const step = steps[i];
    const actionInput = getString(step.action.toolInput);
    const observation = step.observation;

    if (actionInput === 'N/A' || observation?.trim()?.length === 0) {
      continue;
```

**Snippet 2:**
```javascript
const formattedAction = {
    plugin: action.tool,
    input: getString(action.toolInput),
    thought: action.log.includes('Thought: ')
      ? action.log.split('\n')[0].replace('Thought: ', '')
      : action.log.split('\n')[0],
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Async Behavior:** Asynchronous operations present


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (3)

- `librechat-data-provider`
- `@librechat/api`
- `lodash/partialRight`



# 14. Tags
```
- javascript
- utility
- application-code
- librechat
- source-file
```

