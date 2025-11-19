# File: client/src/components/SidePanel/Builder/AssistantConversationStarters.tsx

# 1. Purpose
**File Type:** TSX (UI component)

**What this file represents:**
This file is a ui component located at `client/src/components/SidePanel/Builder/AssistantConversationStarters.tsx`.

**Primary exports:** 1 exported element(s)
- AssistantConversationStarters

**File size:** 5,095 bytes


# 2. Domain Role
**Domain:** Chat & Conversation Management

**Business relevance:**
This file is part of the Chat & Conversation Management domain within the LibreChat application.

**Role:** User interface presentation
- Renders UI elements for user interaction
- Manages component-level state
- Handles user events and input


# 3. Public API (FULL DETAIL)
### Exported Functions

- `AssistantConversationStarters()` — default export



# 4. Internal Structure
### Internal Functions (3)

- `handleAddStarter()`
- `handleDeleteStarter()`
- `triggerShake()`

### Architectural Patterns

- React Hooks pattern



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Props passed from parent component
2. **Transformations:** Component state updates via hooks
3. **External calls:** API calls via React Query hooks
4. **Output:** Rendered JSX with event handlers


# 6. Relationships & Collaboration
### Imported Dependencies (5)

**NPM Packages:**
- `lucide-react`
- `@librechat/client`
- `react-transition-group`
- `librechat-data-provider`

**Aliased Imports:**
- `~/hooks`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**UI Component:** React component

**React Hooks:**
- useState

**Event Handlers:** 4 event handler(s) detected



# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
if (newStarter.trim() && field.value.length < Constants.MAX_CONVO_STARTERS) {
      const newValues = [newStarter, ...field.value];
      field.onChange(newValues);
      setNewStarter('');
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** UI component
- Component: `AssistantConversationStarters`


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (5)

- `lucide-react`
- `@librechat/client`
- `react-transition-group`
- `librechat-data-provider`
- `~/hooks`



# 14. Tags
```
- typescript
- ui-component
- conversation-management
- application-code
- librechat
- source-file
```

