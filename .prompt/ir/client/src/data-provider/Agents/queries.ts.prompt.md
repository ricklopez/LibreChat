# File: client/src/data-provider/Agents/queries.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `client/src/data-provider/Agents/queries.ts`.

**Documentation:** * AGENTS

**Primary exports:** 7 exported element(s)
- defaultAgentParams
- useAvailableAgentToolsQuery
- useListAgentsQuery

**File size:** 4,971 bytes


# 2. Domain Role
**Domain:** Agent Orchestration & Configuration

**Business relevance:**
This file is part of the Agent Orchestration & Configuration domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `defaultAgentParams()` — named export
- `useAvailableAgentToolsQuery()` — named export
- `useListAgentsQuery()` — named export
- `useGetAgentByIdQuery()` — named export
- `useGetExpandedAgentByIdQuery()` — named export
- `useGetAgentCategoriesQuery()` — named export
- `useMarketplaceAgentsInfiniteQuery()` — named export



# 4. Internal Structure
### Internal Functions (1)

- `useMarketplaceAgentsInfiniteQuery()`

### Architectural Patterns

- React Query data fetching



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (3)

**NPM Packages:**
- `@tanstack/react-query`
- `librechat-data-provider`

**Aliased Imports:**
- `~/common`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const queryClient = useQueryClient();
  const endpointsConfig = queryClient.getQueryData<t.TEndpointsConfig>([QueryKeys.endpoints]);

  const enabled = !!endpointsConfig?.[EModelEndpoint.agents];
  return useQuery<t.TPlugin[]>([QueryKeys.tools], () => dataService.getAvailableAgentTools(), {
    refe
```

**Snippet 2:**
```typescript
const queryClient = useQueryClient();
  const endpointsConfig = queryClient.getQueryData<t.TEndpointsConfig>([QueryKeys.endpoints]);

  const enabled = !!endpointsConfig?.[EModelEndpoint.agents];
  return useQuery<t.AgentListResponse, unknown, TData>(
    [QueryKeys.agents, params],
    () => dataSe
```

**Snippet 3:**
```typescript
const isValidAgentId = !!agent_id && !isEphemeralAgent(agent_id);

  return useQuery<t.Agent>(
    [QueryKeys.agent, agent_id],
    () =>
      dataService.getAgentById({
        agent_id: agent_id as string,
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (3)

- `@tanstack/react-query`
- `librechat-data-provider`
- `~/common`



# 14. Tags
```
- typescript
- agent-orchestration
- application-code
- librechat
- source-file
```

