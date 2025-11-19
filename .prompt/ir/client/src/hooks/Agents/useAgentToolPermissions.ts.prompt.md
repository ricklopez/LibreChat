# File: client/src/hooks/Agents/useAgentToolPermissions.ts

# 1. Purpose
**File Type:** TS (Custom React hook)

**What this file represents:**
This file is a custom react hook located at `client/src/hooks/Agents/useAgentToolPermissions.ts`.

**Documentation:** * Hook to determin

**Primary exports:** 1 exported element(s)
- function

**File size:** 2,602 bytes


# 2. Domain Role
**Domain:** Agent Orchestration & Configuration

**Business relevance:**
This file is part of the Agent Orchestration & Configuration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `function()` — default export



# 4. Internal Structure
### Internal Functions (1)

- `useAgentToolPermissions()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (5)

**NPM Packages:**
- `react`
- `librechat-data-provider`

**Aliased Imports:**
- `~/data-provider`
- `~/Providers`
- `~/common`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const agentsMap = useAgentsMapContext();

  const selectedAgent = useMemo(() => {
    return agentId != null && agentId !== '' ? agentsMap?.[agentId] : undefined;
```

**Snippet 2:**
```typescript
// Check ephemeral agent settings
    if (isEphemeralAgent(agentId)) {
      return ephemeralAgent?.[EToolResources.file_search] ?? false;
```

**Snippet 3:**
```typescript
// Check ephemeral agent settings
    if (isEphemeralAgent(agentId)) {
      return ephemeralAgent?.[EToolResources.execute_code] ?? false;
```



# 10. Architectural Concerns
**Performance:** Optimized with memoization


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (5)

- `react`
- `librechat-data-provider`
- `~/data-provider`
- `~/Providers`
- `~/common`



# 14. Tags
```
- typescript
- react-hook
- agent-orchestration
- authorization
- tool-execution
```

