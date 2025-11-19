# File: api/app/clients/prompts/truncate.js

# 1. Purpose
**File Type:** JS (Application code)

**What this file represents:**
This file is a application code located at `api/app/clients/prompts/truncate.js`.

**Documentation:** * Truncates a given text to a specified maximum length, appending ellipsis and a notification


**File size:** 3,872 bytes


# 2. Domain Role
**Domain:** Prompt Management & Templating

**Business relevance:**
This file is part of the Prompt Management & Templating domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (3)

- `truncateText()`
- `smartTruncateText()`
- `truncateToolCallOutputs()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
*No relationship data available.*


# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
if (text.length > maxLength) {
    return `${text.slice(0, maxLength)
```

**Snippet 2:**
```javascript
const ellipsis = '...';
  const notification = ' [text truncated for brevity]';
  const halfMaxLength = Math.floor((maxLength - ellipsis.length - notification.length) / 2);

  if (text.length > maxLength) {
    const startLastHalf = text.length - halfMaxLength;
    return `${text.slice(0, halfMaxLen
```

**Snippet 3:**
```javascript
currentIndex--;
    const message = messages.pop();
    currentTokenCount += message.tokenCount;
    if (currentTokenCount < targetTokenLimit) {
      processedMessages.push(message);
      continue;
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
*No dependency information available.*


# 14. Tags
```
- javascript
- prompt-management
- application-code
- librechat
- source-file
```

