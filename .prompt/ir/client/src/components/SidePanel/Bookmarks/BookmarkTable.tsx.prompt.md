# File: client/src/components/SidePanel/Bookmarks/BookmarkTable.tsx

# 1. Purpose
**File Type:** TSX (UI component)

**What this file represents:**
This file is a ui component located at `client/src/components/SidePanel/Bookmarks/BookmarkTable.tsx`.

**Primary exports:** 1 exported element(s)
- BookmarkTable

**File size:** 5,896 bytes


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

- `BookmarkTable()` — default export



# 4. Internal Structure
### Internal Functions (2)

- `removeDuplicates()`
- `BookmarkTable()`

### Architectural Patterns

- React Hooks pattern



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Props passed from parent component
2. **Transformations:** Component state updates via hooks
3. **External calls:** API calls via React Query hooks
4. **Output:** Rendered JSX with event handlers


# 6. Relationships & Collaboration
### Imported Dependencies (6)

**NPM Packages:**
- `lucide-react`
- `@librechat/client`

**Relative Imports:**
- `./BookmarkTableRow`

**Aliased Imports:**
- `~/Providers/BookmarkContext`
- `~/components/Bookmarks`
- `~/hooks`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**UI Component:** React component

**React Hooks:**
- useState
- useEffect
- useCallback

**Event Handlers:** 2 event handler(s) detected



# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const seen = new Set();
  return bookmarks.filter((bookmark) => {
    const duplicate = seen.has(bookmark._id);
    seen.add(bookmark._id);
    return !duplicate;
```

**Snippet 2:**
```typescript
setRows((prevTags: TConversationTag[]) => {
      const updatedRows = [...prevTags];
      const [movedRow] = updatedRows.splice(dragIndex, 1);
      updatedRows.splice(hoverIndex, 0, movedRow);
      return updatedRows.map((row, index) => ({ ...row, position: index
```



# 10. Architectural Concerns
**Performance:** Optimized with memoization


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** UI component
- Component: `BookmarkTable`


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (5)

- `lucide-react`
- `@librechat/client`
- `~/Providers/BookmarkContext`
- `~/components/Bookmarks`
- `~/hooks`



# 14. Tags
```
- typescript
- ui-component
- application-code
- librechat
- source-file
```

