# File: client/src/components/Chat/Menus/Presets/EditPresetDialog.tsx

# 1. Purpose
**File Type:** TSX (UI component)

**What this file represents:**
This file is a ui component located at `client/src/components/Chat/Menus/Presets/EditPresetDialog.tsx`.

**Primary exports:** 1 exported element(s)
- EditPresetDialog

**File size:** 7,321 bytes


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

- `EditPresetDialog()` — default export



# 4. Internal Structure
### Internal Functions (2)

- `EditPresetDialog()`
- `handleOpenChange()`

### Architectural Patterns

- React Hooks pattern
- React Query data fetching



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Props passed from parent component
2. **Transformations:** Component state updates via hooks
3. **External calls:** API calls via React Query hooks
4. **Output:** Rendered JSX with event handlers


# 6. Relationships & Collaboration
### Imported Dependencies (12)

**NPM Packages:**
- `recoil`
- `react`
- `@tanstack/react-query`
- `librechat-data-provider`
- `@librechat/client`

**Aliased Imports:**
- `~/utils`
- `~/hooks`
- `~/components/Chat/Input/PopoverButtons`
- `~/components/Endpoints`
- `~/data-provider`
- `~/Providers`
- `~/store`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**UI Component:** React component

**React Hooks:**
- useEffect
- useCallback
- useMemo
- useQuery (React Query)

**Event Handlers:** 4 event handler(s) detected



# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
return _endpoints.filter((endpoint) => !isAgentsEndpoint(endpoint));
```

**Snippet 2:**
```typescript
if (!setOptions) {
        return console.warn('setOptions is not defined');
```

**Snippet 3:**
```typescript
setPresetModalVisible(open);
    if (!open) {
      setPreset(null);
```



# 10. Architectural Concerns
**Logging:** Contains logging statements
**Performance:** Optimized with memoization


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** UI component
- Component: `EditPresetDialog`


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (12)

- `recoil`
- `react`
- `@tanstack/react-query`
- `librechat-data-provider`
- `@librechat/client`
- `~/utils`
- `~/hooks`
- `~/components/Chat/Input/PopoverButtons`
- `~/components/Endpoints`
- `~/data-provider`
- `~/Providers`
- `~/store`



# 14. Tags
```
- typescript
- ui-component
- application-code
- librechat
- source-file
```

