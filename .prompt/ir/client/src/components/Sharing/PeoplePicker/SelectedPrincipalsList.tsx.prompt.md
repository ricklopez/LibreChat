# File: client/src/components/Sharing/PeoplePicker/SelectedPrincipalsList.tsx

# 1. Purpose
**File Type:** TSX (UI component)

**What this file represents:**
This file is a ui component located at `client/src/components/Sharing/PeoplePicker/SelectedPrincipalsList.tsx`.

**Primary exports:** 1 exported element(s)
- function

**File size:** 3,891 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.

**Role:** User interface presentation
- Renders UI elements for user interaction
- Manages component-level state
- Handles user events and input


# 3. Public API (FULL DETAIL)
### Exported Functions

- `function()` — default export



# 4. Internal Structure
### Internal Functions (2)

- `SelectedPrincipalsList()`
- `getPrincipalDisplayInfo()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Props passed from parent component
2. **Transformations:** Component state updates via hooks
3. **External calls:** API calls via React Query hooks
4. **Output:** Rendered JSX with event handlers


# 6. Relationships & Collaboration
### Imported Dependencies (7)

**NPM Packages:**
- `react`
- `@librechat/client`
- `lucide-react`
- `librechat-data-provider`

**Aliased Imports:**
- `~/components/Sharing/AccessRolesPicker`
- `~/components/Sharing/PrincipalAvatar`
- `~/hooks`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**UI Component:** React component

**Event Handlers:** 2 event handler(s) detected



# 9. Key Logic Snippets
*No significant logic snippets extracted. See full source file for implementation details.*


# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** UI component
- Component: `SelectedPrincipalsList`


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (7)

- `react`
- `@librechat/client`
- `lucide-react`
- `librechat-data-provider`
- `~/components/Sharing/AccessRolesPicker`
- `~/components/Sharing/PrincipalAvatar`
- `~/hooks`



# 14. Tags
```
- typescript
- ui-component
- application-code
- librechat
- source-file
```

