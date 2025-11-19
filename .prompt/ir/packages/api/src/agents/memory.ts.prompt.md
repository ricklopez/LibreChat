# File: packages/api/src/agents/memory.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/agents/memory.ts`.

**Documentation:** Memories */

**Primary exports:** 5 exported element(s)
- MemoryConfig
- memoryInstructions
- createMemoryTool

**File size:** 15,976 bytes


# 2. Domain Role
**Domain:** Agent Orchestration & Configuration

**Business relevance:**
This file is part of the Agent Orchestration & Configuration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Classes

- `class BasicToolEndHandler`

### Exported Functions

- `MemoryConfig()` — named export
- `memoryInstructions()` — named export
- `createMemoryTool()` — named export
- `BasicToolEndHandler()` — named export
- `createMemoryCallback({
  res,
  artifactPromises,
}: {
  res: ServerResponse;
  artifactPromises: Promise<Partial<TAttachment> | null>[];
})`



# 4. Internal Structure
### Internal Functions (7)

- `processMemory()`
- `createMemoryProcessor()`
- `handleMemoryArtifact()`
- `createMemoryCallback()`
- `getDefaultInstructions()`
- `createMemoryTool()`
- `createDeleteMemoryTool()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (6)

**NPM Packages:**
- `zod`
- `@langchain/core/tools`
- `librechat-data-provider`
- `@librechat/data-schemas`
- `@librechat/agents`

**Aliased Imports:**
- `~/utils`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const errorArtifact: Record<Tools.memory, MemoryArtifact> = {
            [Tools.memory]: {
              key: 'system',
              type: 'error',
              value: JSON.stringify({
                errorType: 'already_exceeded',
                tokenCount: Math.abs(remainingTokens),
          
```

**Snippet 2:**
```typescript
const errorArtifact: Record<Tools.memory, MemoryArtifact> = {
              [Tools.memory]: {
                key: 'system',
                type: 'error',
                value: JSON.stringify({
                  errorType: 'would_exceed',
                  tokenCount: Math.abs(newRemainingTokens),
```

**Snippet 3:**
```typescript
console.warn('No output found in tool_end event');
      return;
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (6)

- `zod`
- `@langchain/core/tools`
- `librechat-data-provider`
- `@librechat/data-schemas`
- `@librechat/agents`
- `~/utils`



# 14. Tags
```
- typescript
- agent-orchestration
- application-code
- librechat
- source-file
```

