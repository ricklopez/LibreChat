# File: api/server/services/Tools/search.js

# 1. Purpose
**File Type:** JS (Business logic service)

**What this file represents:**
This file is a business logic service located at `api/server/services/Tools/search.js`.

**Documentation:** * Creates a function to handle search results and stream them as attachments


**File size:** 3,601 bytes


# 2. Domain Role
**Domain:** Tool & Action Execution

**Business relevance:**
This file is part of the Tool & Action Execution domain within the LibreChat application.

**Role:** Business logic implementation
- Implements domain-specific operations
- Coordinates between data layer and API layer
- Enforces business rules and validation


# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (4)

- `createOnSearchResults()`
- `onSearchResults()`
- `onGetHighlights()`
- `buildAttachment()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Parameters from controller/caller
2. **Transformations:** Business logic processing
3. **External calls:** Database models, external APIs
4. **Output:** Processed data or operation result


# 6. Relationships & Collaboration
### Imported Dependencies (4)

**NPM Packages:**
- `http`
- `nanoid`
- `librechat-data-provider`
- `@librechat/data-schemas`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
const source = context.sourceMap.get(link);
    if (!source) {
      return;
```

**Snippet 2:**
```javascript
return {
    messageId: context.messageId,
    toolCallId: context.toolCallId,
    conversationId: context.conversationId,
    name: context.attachmentName,
    type: Tools.web_search,
    [Tools.web_search]: context.searchResultData,
```



# 10. Architectural Concerns
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Business logic service
- Service: Business logic layer
- Module: `searchService`


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (3)

- `nanoid`
- `librechat-data-provider`
- `@librechat/data-schemas`



# 14. Tags
```
- javascript
- service
- business-logic
- tool-execution
- application-code
- librechat
- source-file
```

