# File: client/src/components/Web/Citation.tsx

# 1. Purpose
**File Type:** TSX (UI component)

**What this file represents:**
This file is a ui component located at `client/src/components/Web/Citation.tsx`.

**Primary exports:** 5 exported element(s)
- CompositeCitation
- Citation
- HighlightedTextProps

**File size:** 7,443 bytes


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

- `CompositeCitation(props: CompositeCitationProps)`
- `Citation(props: CitationComponentProps)`
- `HighlightedTextProps()` — named export
- `useHighlightState(citationId: string | undefined)`
- `HighlightedText({
  children,
  citationId,
}: HighlightedTextProps)`



# 4. Internal Structure
### Internal Functions (8)

- `CompositeCitation()`
- `Citation()`
- `useHighlightState()`
- `HighlightedText()`
- `getCitationLabel()`
- `handlePrevPage()`
- `handleNextPage()`
- `getCitationLabel()`

### Architectural Patterns

- React Hooks pattern



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Props passed from parent component
2. **Transformations:** Component state updates via hooks
3. **External calls:** API calls via React Query hooks
4. **Output:** Rendered JSX with event handlers


# 6. Relationships & Collaboration
### Imported Dependencies (8)

**NPM Packages:**
- `react`
- `recoil`
- `@librechat/client`

**Relative Imports:**
- `./Context`

**Aliased Imports:**
- `~/components/Web/SourceHovercard`
- `~/data-provider`
- `~/hooks`
- `~/store`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**UI Component:** React component

**React Hooks:**
- useState
- useCallback
- useContext

**Event Handlers:** 3 event handler(s) detected



# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
if (!sources || sources.length === 0) return localize('com_citation_source');

    const firstSource = sources[0];
    const remainingCount = sources.length - 1;
    const attribution =
      firstSource.attribution ||
      firstSource.title ||
      getCleanDomain(firstSource.link || '') ||
      
```

**Snippet 2:**
```typescript
e.preventDefault();
    e.stopPropagation();
    if (currentPage > 0) {
      setCurrentPage(currentPage - 1);
```

**Snippet 3:**
```typescript
e.preventDefault();
    e.stopPropagation();
    if (currentPage < totalPages - 1) {
      setCurrentPage(currentPage + 1);
```



# 10. Architectural Concerns
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present
**Performance:** Optimized with memoization


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** UI component
- Component: `Citation`


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (7)

- `react`
- `recoil`
- `@librechat/client`
- `~/components/Web/SourceHovercard`
- `~/data-provider`
- `~/hooks`
- `~/store`



# 14. Tags
```
- typescript
- ui-component
- application-code
- librechat
- source-file
```

