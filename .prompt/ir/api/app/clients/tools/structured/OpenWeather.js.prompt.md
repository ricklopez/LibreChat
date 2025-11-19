# File: api/app/clients/tools/structured/OpenWeather.js

# 1. Purpose
**File Type:** JS (Application code)

**What this file represents:**
This file is a application code located at `api/app/clients/tools/structured/OpenWeather.js`.

**Documentation:** * Map user-friendly units to OpenWeather units.


**File size:** 10,653 bytes


# 2. Domain Role
**Domain:** Tool & Action Execution

**Business relevance:**
This file is part of the Tool & Action Execution domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Classes

- `class OpenWeather extends Tool`

### Exported Functions




# 4. Internal Structure
### Internal Functions (2)

- `mapUnitsToOpenWeather()`
- `roundTemperatures()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (4)

**NPM Packages:**
- `@langchain/core/tools`
- `zod`
- `@langchain/core/utils/env`
- `node-fetch`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
const tempKeys = new Set([
    'temp',
    'feels_like',
    'dew_point',
    'day',
    'min',
    'max',
    'night',
    'eve',
    'morn',
    'afternoon',
    'morning',
    'evening',
  ]);

  if (Array.isArray(obj)) {
    return obj.map((item) => roundTemperatures(item));
```

**Snippet 2:**
```javascript
const value = obj[key];
      if (value && typeof value === 'object') {
        obj[key] = roundTemperatures(value);
```

**Snippet 3:**
```javascript
throw new Error(`Could not find coordinates for city: ${city
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (4)

- `@langchain/core/tools`
- `zod`
- `@langchain/core/utils/env`
- `node-fetch`



# 14. Tags
```
- javascript
- tool-execution
- application-code
- librechat
- source-file
```

