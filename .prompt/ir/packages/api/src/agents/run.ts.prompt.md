# File: packages/api/src/agents/run.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/api/src/agents/run.ts`.

**Documentation:** as t from '~/types';

**Primary exports:** 1 exported element(s)
- getReasoningKey

**File size:** 5,018 bytes


# 2. Domain Role
**Domain:** Agent Orchestration & Configuration

**Business relevance:**
This file is part of the Agent Orchestration & Configuration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `getReasoningKey(
  provider: Providers,
  llmConfig: t.RunLLMConfig,
  agentEndpoint?: string | null,
)`



# 4. Internal Structure
### Internal Functions (3)

- `getReasoningKey()`
- `createRun()`
- `buildAgentContext()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (3)

**NPM Packages:**
- `@librechat/agents`
- `librechat-data-provider`

**Aliased Imports:**
- `~/utils/env`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
let reasoningKey: 'reasoning_content' | 'reasoning' = 'reasoning_content';
  if (provider === Providers.GOOGLE) {
    reasoningKey = 'reasoning';
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Async Behavior:** Asynchronous operations present


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Backend code


# 12. Migration Concerns & Recommendations
- May contain deprecated or legacy code patterns


# 13. Dependencies
### dependsOn (3)

- `@librechat/agents`
- `librechat-data-provider`
- `~/utils/env`



# 14. Tags
```
- typescript
- agent-orchestration
- application-code
- librechat
- source-file
```

