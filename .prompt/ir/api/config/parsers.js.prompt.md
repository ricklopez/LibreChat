# File: api/config/parsers.js

# 1. Purpose
**File Type:** JS (Application code)

**What this file represents:**
This file is a application code located at `api/config/parsers.js`.

**Documentation:** OpenAI API key pattern


**File size:** 7,200 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (6)

- `getMatchingSensitivePatterns()`
- `redactMessage()`
- `truncateLongStrings()`
- `condenseArray()`
- `truncateLongStrings()`
- `truncateObject()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (3)

**NPM Packages:**
- `klona`
- `winston`
- `traverse`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
if (valueStr) {
    // Filter and return all regex patterns that match the value string
    return sensitiveKeys.filter((regex) => regex.test(valueStr));
```

**Snippet 2:**
```javascript
if (info.level === 'error') {
    info.message = redactMessage(info.message);
    if (info[MESSAGE_SYMBOL]) {
      info[MESSAGE_SYMBOL] = redactMessage(info[MESSAGE_SYMBOL]);
```

**Snippet 3:**
```javascript
if (typeof value === 'string') {
    return value.length > length ? value.substring(0, length) + '... [truncated]' : value;
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (3)

- `klona`
- `winston`
- `traverse`



# 14. Tags
```
- javascript
- application-code
- librechat
- source-file
```

