# File: client/src/utils/endpoints.ts

# 1. Purpose
**File Type:** TS (Utility / Helper function)

**What this file represents:**
This file is a utility / helper function located at `client/src/utils/endpoints.ts`.

**Documentation:** as t from 'librechat-data-provider';

**Primary exports:** 14 exported element(s)
- getEntityName
- getEndpointsFilter
- getAvailableEndpoints

**File size:** 9,557 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `getEntityName()` — named export
- `getEndpointsFilter()` — named export
- `getAvailableEndpoints()` — named export
- `mapEndpoints(endpointsConfig: t.TEndpointsConfig)`
- `updateLastSelectedModel({
  endpoint,
  model = '',
}: {
  endpoint: string;
  model?: string;
})`
- `getConvoSwitchLogic(params: ConversationInitParams)`
- `getModelSpec({
  specName,
  startupConfig,
}: {
  specName?: string | null;
  startupConfig?: t.TStartupConfig;
})`
- `applyModelSpecEphemeralAgent({
  convoId,
  modelSpec,
  updateEphemeralAgent,
}: {
  convoId?: string | null;
  modelSpec?: t.TModelSpec;
  updateEphemeralAgent: ((convoId: string, agent: t.TEphemeralAgent | null)`
- `getDefaultModelSpec(startupConfig?: t.TStartupConfig)`
- `getModelSpecPreset(modelSpec?: t.TModelSpec)`
- `getModelSpecIconURL(modelSpec: t.TModelSpec)`
- `getIconEndpoint({
  endpointsConfig,
  iconURL,
  endpoint,
}: {
  endpointsConfig?: t.TEndpointsConfig;
  iconURL?: string | null;
  endpoint?: string | null;
})`
- `getIconKey({
  endpoint,
  endpointType: _eType,
  endpointsConfig,
  endpointIconURL: iconURL,
}: {
  endpoint?: string | null;
  endpointsConfig?: t.TEndpointsConfig | null;
  endpointType?: string | null;
  endpointIconURL?: string;
})`
- `getEntity()` — named export



# 4. Internal Structure
### Internal Functions (13)

- `mapEndpoints()`
- `updateLastSelectedModel()`
- `getConvoSwitchLogic()`
- `getModelSpec()`
- `applyModelSpecEphemeralAgent()`
- `getDefaultModelSpec()`
- `getModelSpecPreset()`
- `getModelSpecIconURL()`
- `getIconEndpoint()`
- `getIconKey()`
- *...and 3 more functions*



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (1)

**NPM Packages:**
- `librechat-data-provider`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const defaultSet = new Set(defaultEndpoints);
  const availableEndpoints: EModelEndpoint[] = [];

  for (const endpoint in endpointsConfig) {
    // Check if endpoint is in the filter or its type is in defaultEndpoints
    if (
      filter[endpoint] ||
      (endpointsConfig[endpoint]?.type &&
    
```

**Snippet 2:**
```typescript
const filter = getEndpointsFilter(endpointsConfig);
  return getAvailableEndpoints(filter, endpointsConfig).sort(
    (a, b) => (endpointsConfig?.[a]?.order ?? 0) - (endpointsConfig?.[b]?.order ?? 0),
  );
```

**Snippet 3:**
```typescript
const lastSelectedSpecName = localStorage.getItem(LocalStorageKeys.LAST_SPEC);
    const lastSelectedSpec = list?.find((spec) => spec.name === lastSelectedSpecName);
    return { default: defaultSpec || lastSelectedSpec || list?.[0]
```



# 10. Architectural Concerns
*No specific architectural concerns identified.*


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (1)

- `librechat-data-provider`



# 14. Tags
```
- typescript
- utility
- application-code
- librechat
- source-file
```

