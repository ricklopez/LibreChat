# File: client/src/components/Prompts/PromptForm.tsx

# 1. Purpose
**File Type:** TSX (UI component)

**What this file represents:**
This file is a ui component located at `client/src/components/Prompts/PromptForm.tsx`.

**Primary exports:** 1 exported element(s)
- PromptForm

**File size:** 17,668 bytes


# 2. Domain Role
**Domain:** Prompt Management & Templating

**Business relevance:**
This file is part of the Prompt Management & Templating domain within the LibreChat application.

**Role:** User interface presentation
- Renders UI elements for user interaction
- Manages component-level state
- Handles user events and input


# 3. Public API (FULL DETAIL)
### Exported Functions

- `PromptForm()` — default export



# 4. Internal Structure
### Internal Functions (2)

- `PromptForm()`
- `handleResize()`

### Architectural Patterns

- React Hooks pattern



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Props passed from parent component
2. **Transformations:** Component state updates via hooks
3. **External calls:** API calls via React Query hooks
4. **Output:** Rendered JSX with event handlers


# 6. Relationships & Collaboration
### Imported Dependencies (27)

**NPM Packages:**
- `react`
- `react`
- `lodash/debounce`
- `recoil`
- `lucide-react`
- `react-router-dom`
- `react-hook-form`
- `@librechat/client`
- `librechat-data-provider`

**Relative Imports:**
- `./Groups/CategorySelector`
- `./Groups/NoPromptGroup`
- `./PromptVariables`
- `./PromptVersions`
- `./DeleteVersion`
- `./PromptDetails`
- `./PromptEditor`
- `./SkeletonForm`
- `./Description`
- `./SharePrompt`
- *...and 2 more*

**Aliased Imports:**
- `~/data-provider`
- `~/hooks`
- `~/Providers`
- `~/utils`
- `~/common`
- `~/store`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**UI Component:** React component

**React Hooks:**
- useState
- useEffect
- useCallback
- useMemo

**Event Handlers:** 5 event handler(s) detected

**Form Management:** React Hook Form



# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
console.error('No groupId available');
        return;
```

**Snippet 2:**
```typescript
if (isLoadingGroup || isLoadingPrompts) {
      return;
```

**Snippet 3:**
```typescript
if (window.matchMedia('(min-width: 1022px)').matches) {
        setShowSidePanel(false);
```



# 10. Architectural Concerns
**Performance:** Optimized with memoization


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** UI component
- Component: `PromptForm`


# 12. Migration Concerns & Recommendations
- Contains TODO/FIXME comments indicating technical debt
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (15)

- `react`
- `react`
- `lodash/debounce`
- `recoil`
- `lucide-react`
- `react-router-dom`
- `react-hook-form`
- `@librechat/client`
- `librechat-data-provider`
- `~/data-provider`
- `~/hooks`
- `~/Providers`
- `~/utils`
- `~/common`
- `~/store`



# 14. Tags
```
- typescript
- ui-component
- prompt-management
- application-code
- librechat
- source-file
```

