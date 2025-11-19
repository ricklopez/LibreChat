# File: client/src/components/Agents/AgentDetail.tsx

# 1. Purpose
**File Type:** TSX (UI component)

**What this file represents:**
This file is a ui component located at `client/src/components/Agents/AgentDetail.tsx`.

**Primary exports:** 1 exported element(s)
- AgentDetail

**File size:** 5,731 bytes


# 2. Domain Role
**Domain:** Agent Orchestration & Configuration

**Business relevance:**
This file is part of the Agent Orchestration & Configuration domain within the LibreChat application.

**Role:** User interface presentation
- Renders UI elements for user interaction
- Manages component-level state
- Handles user events and input


# 3. Public API (FULL DETAIL)
### Exported Functions

- `AgentDetail()` — default export



# 4. Internal Structure
### Internal Functions (3)

- `handleStartChat()`
- `handleCopyLink()`
- `formatContact()`

### Architectural Patterns

- React Query data fetching



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Props passed from parent component
2. **Transformations:** Component state updates via hooks
3. **External calls:** API calls via React Query hooks
4. **Output:** Rendered JSX with event handlers


# 6. Relationships & Collaboration
### Imported Dependencies (7)

**NPM Packages:**
- `lucide-react`
- `@tanstack/react-query`
- `@librechat/client`
- `librechat-data-provider`

**Aliased Imports:**
- `~/utils`
- `~/hooks`
- `~/Providers`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**UI Component:** React component

**React Hooks:**
- useQuery (React Query)

**Event Handlers:** 2 event handler(s) detected



# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
if (agent) {
      const keys = [QueryKeys.agents, { requiredPermission: PermissionBits.EDIT
```

**Snippet 2:**
```typescript
if (!listResp.data.some((a) => a.id === agent.id)) {
          const currentAgents = [agent, ...JSON.parse(JSON.stringify(listResp.data))];
          queryClient.setQueryData<AgentListResponse>(keys, { ...listResp, data: currentAgents
```

**Snippet 3:**
```typescript
if (!agent?.support_contact) return null;

    const { name, email
```



# 10. Architectural Concerns
**Error Handling:** Uses try-catch blocks


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** UI component
- Component: `AgentDetail`


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (7)

- `lucide-react`
- `@tanstack/react-query`
- `@librechat/client`
- `librechat-data-provider`
- `~/utils`
- `~/hooks`
- `~/Providers`



# 14. Tags
```
- typescript
- ui-component
- agent-orchestration
- application-code
- librechat
- source-file
```

