# File: api/server/services/start/tools.js

# 1. Purpose
**File Type:** JS (Business logic service)

**What this file represents:**
This file is a business logic service located at `api/server/services/start/tools.js`.

**Documentation:** * Loads and


**File size:** 4,377 bytes


# 2. Domain Role
**Domain:** Tool & Action Execution

**Business relevance:**
This file is part of the Tool & Action Execution domain within the LibreChat application.

**Role:** Business logic implementation
- Implements domain-specific operations
- Coordinates between data layer and API layer
- Enforces business rules and validation


# 3. Public API (FULL DETAIL)
### Classes

- `class of`

### Exported Functions




# 4. Internal Structure
### Internal Functions (2)

- `loadAndFormatTools()`
- `formatToOpenAIAssistantTool()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Parameters from controller/caller
2. **Transformations:** Business logic processing
3. **External calls:** Database models, external APIs
4. **Output:** Processed data or operation result


# 6. Relationships & Collaboration
### Imported Dependencies (9)

**NPM Packages:**
- `fs`
- `path`
- `@langchain/core/tools`
- `@librechat/agents`
- `@librechat/data-schemas`
- `zod-to-json-schema`
- `librechat-data-provider`
- `@librechat/api`

**Aliased Imports:**
- `~/app/clients/tools/manifest`



# 7. Database Interaction Mapping
**Database:** MongoDB via Mongoose



# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
const filePath = path.join(directory, file);
    if (!file.endsWith('.js') || (filter.has(file) && included.size === 0)) {
      continue;
```

**Snippet 2:**
```javascript
const formattedTool = formatToOpenAIAssistantTool(toolInstance);
    let toolName = formattedTool[Tools.function].name;
    toolName = getToolkitKey({ toolkits, toolName
```

**Snippet 3:**
```javascript
return {
    type: Tools.function,
    [Tools.function]: {
      name: tool.name,
      description: tool.description,
      parameters: zodToJsonSchema(tool.schema),
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Business logic service
- Service: Business logic layer
- Module: `toolsService`


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (9)

- `fs`
- `path`
- `@langchain/core/tools`
- `@librechat/agents`
- `@librechat/data-schemas`
- `zod-to-json-schema`
- `librechat-data-provider`
- `@librechat/api`
- `~/app/clients/tools/manifest`



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

