# File: client/src/components/Web/SourceHovercard.tsx

# 1. Purpose
**File Type:** TSX (UI component)

**What this file represents:**
This file is a ui component located at `client/src/components/Web/SourceHovercard.tsx`.

**Documentation:** as Ariakit from '@ariakit/react';

**Primary exports:** 4 exported element(s)
- SourceData
- getCleanDomain
- FaviconImage

**File size:** 6,335 bytes


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

- `SourceData()` — named export
- `getCleanDomain(url: string)`
- `FaviconImage({ domain, className = '' }: { domain: string; className?: string })`
- `SourceHovercard({
  source,
  label,
  onMouseEnter,
  onMouseLeave,
  onClick,
  isFile = false,
  isLocalFile = false,
  children,
}: SourceHovercardProps)`



# 4. Internal Structure
### Internal Functions (4)

- `getFaviconUrl()`
- `getCleanDomain()`
- `FaviconImage()`
- `SourceHovercard()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Props passed from parent component
2. **Transformations:** Component state updates via hooks
3. **External calls:** API calls via React Query hooks
4. **Output:** Rendered JSX with event handlers


# 6. Relationships & Collaboration
### Imported Dependencies (5)

**NPM Packages:**
- `@ariakit/react`
- `lucide-react`
- `@ariakit/react`

**Aliased Imports:**
- `~/hooks`
- `~/utils`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**UI Component:** React component

**Event Handlers:** 3 event handler(s) detected



# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
return `https://www.google.com/s2/favicons?domain=${domain
```

**Snippet 2:**
```typescript
const domain = url.replace(/(^\w+:|^)\/\//, '').split('/')[0];
  return domain.startsWith('www.') ? domain.substring(4) : domain;
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** UI component
- Component: `SourceHovercard`


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (5)

- `@ariakit/react`
- `lucide-react`
- `@ariakit/react`
- `~/hooks`
- `~/utils`



# 14. Tags
```
- typescript
- ui-component
- application-code
- librechat
- source-file
```

