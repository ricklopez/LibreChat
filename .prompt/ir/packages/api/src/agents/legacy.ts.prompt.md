# File: packages/api/src/agents/legacy.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/agents/legacy.ts`.

**Documentation:** * Converts OCR tool resource to context tool resource in place.

**Primary exports:** 2 exported element(s)
- convertOcrToContextInPlace
- mergeAgentOcrConversion

**File size:** 5,450 bytes


# 2. Domain Role
**Domain:** Agent Orchestration & Configuration

**Business relevance:**
This file is part of the Agent Orchestration & Configuration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `convertOcrToContextInPlace(data: {
  tool_resources?: AgentToolResources;
  tools?: string[];
})`
- `mergeAgentOcrConversion(
  existingAgent: { tool_resources?: AgentToolResources; tools?: string[] },
  updateData: { tool_resources?: AgentToolResources; tools?: string[] },
)`



# 4. Internal Structure
### Internal Functions (2)

- `convertOcrToContextInPlace()`
- `mergeAgentOcrConversion()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (1)

**NPM Packages:**
- `librechat-data-provider`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const existingFiles = data.tool_resources.context.files || [];
        const ocrFiles = data.tool_resources.ocr.files || [];
        const filesMap = new Map<string, TFile>();
        [...existingFiles, ...ocrFiles].forEach((file) => {
          if (file?.file_id) {
            filesMap.set(file.fil
```

**Snippet 2:**
```typescript
const existingFiles = result.tool_resources.context.files || [];
      const ocrFiles = result.tool_resources.ocr?.files || [];
      // Merge and deduplicate by file_id
      const filesMap = new Map<string, TFile>();
      [...existingFiles, ...ocrFiles].forEach((file) => {
        if (file?.file_
```

**Snippet 3:**
```typescript
const existingFiles = mergedContext.files || [];
      const newFiles = updateData.tool_resources.context.files || [];
      const filesMap = new Map<string, TFile>();
      [...existingFiles, ...newFiles].forEach((file) => {
        if (file?.file_id) {
          filesMap.set(file.file_id, file);
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- May contain deprecated or legacy code patterns
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (1)

- `librechat-data-provider`



# 14. Tags
```
- typescript
- agent-orchestration
- application-code
- librechat
- source-file
```

