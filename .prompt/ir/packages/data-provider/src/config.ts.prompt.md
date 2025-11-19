# File: packages/data-provider/src/config.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `packages/data-provider/src/config.ts`.

**Primary exports:** 102 exported element(s)
- defaultSocialLogins
- defaultRetrievalModels
- excludedKeys

**File size:** 48,585 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `defaultSocialLogins()` — named export
- `defaultRetrievalModels()` — named export
- `excludedKeys()` — named export
- `SettingsViews()` — named export
- `fileSourceSchema()` — named export
- `fileStrategiesSchema()` — named export
- `SchemaDefaults()` — named export
- `TConfigDefaults()` — named export
- `getSchemaDefaults()` — named export
- `modelConfigSchema()` — named export
- `TAzureModelConfig()` — named export
- `azureBaseSchema()` — named export
- `TAzureBaseSchema()` — named export
- `azureGroupSchema()` — named export
- `azureGroupConfigsSchema()` — named export
- `TAzureGroup()` — named export
- `TAzureGroups()` — named export
- `TAzureModelMapSchema()` — named export
- `TAzureModelGroupMap()` — named export
- `TAzureGroupMap()` — named export
- `TValidatedAzureConfig()` — named export
- `TAzureConfigValidationResult()` — named export
- `Capabilities()` — named export
- `AgentCapabilities()` — named export
- `defaultAssistantsVersion()` — named export
- `baseEndpointSchema()` — named export
- `TBaseEndpoint()` — named export
- `bedrockEndpointSchema()` — named export
- `assistantEndpointSchema()` — named export
- `TAssistantEndpoint()` — named export
- `defaultAgentCapabilities()` — named export
- `agentsEndpointSchema()` — named export
- `TAgentsEndpoint()` — named export
- `endpointSchema()` — named export
- `TEndpoint()` — named export
- `azureEndpointSchema()` — named export
- `TAzureConfig()` — named export
- `RateLimitPrefix()` — named export
- `rateLimitSchema()` — named export
- `EImageOutputType()` — named export
- `TTermsOfService()` — named export
- `TMcpServersConfig()` — named export
- `interfaceSchema()` — named export
- `TInterfaceConfig()` — named export
- `TBalanceConfig()` — named export
- `TTransactionsConfig()` — named export
- `turnstileOptionsSchema()` — named export
- `turnstileSchema()` — named export
- `TTurnstileConfig()` — named export
- `TStartupConfig()` — named export
- `OCRStrategy()` — named export
- `SearchCategories()` — named export
- `SearchProviders()` — named export
- `ScraperProviders()` — named export
- `RerankerTypes()` — named export
- `SafeSearchTypes()` — named export
- `webSearchSchema()` — named export
- `TWebSearchConfig()` — named export
- `ocrSchema()` — named export
- `balanceSchema()` — named export
- `transactionsSchema()` — named export
- `memorySchema()` — named export
- `TMemoryConfig()` — named export
- `configSchema()` — named export
- `DeepPartial()` — named export
- `getConfigDefaults()` — named export
- `TCustomConfig()` — named export
- `TCustomEndpoints()` — named export
- `TProviderSchema()` — named export
- `KnownEndpoints()` — named export
- `FetchTokenConfig()` — named export
- `defaultEndpoints()` — named export
- `alternateName()` — named export
- `bedrockModels()` — named export
- `defaultModels()` — named export
- `initialModelsConfig()` — named export
- `EndpointURLs()` — named export
- `modularEndpoints()` — named export
- `supportsBalanceCheck()` — named export
- `visionModels()` — named export
- `VisionModes()` — named export
- `validateVisionModel({
  model,
  additionalModels = [],
  availableModels,
}: {
  model: string;
  additionalModels?: string[];
  availableModels?: string[];
})`
- `imageGenTools()` — named export
- `InfiniteCollections()` — named export
- `Time()` — named export
- `CacheKeys()` — named export
- `ViolationTypes()` — named export
- `ErrorTypes()` — named export
- `AuthKeys()` — named export
- `ImageDetailCost()` — named export
- `SettingsTabValues()` — named export
- `STTProviders()` — named export
- `TTSProviders()` — named export
- `Constants()` — named export
- `LocalStorageKeys()` — named export
- `ForkOptions()` — named export
- `CohereConstants()` — named export
- `SystemCategories()` — named export
- `providerEndpointMap()` — named export
- `specialVariables()` — named export
- `TSpecialVarLabel()` — named export
- `getEndpointField()` — named export



# 4. Internal Structure
### Internal Functions (3)

- `validateVisionModel()`
- `getConfigDefaults()`
- `fitlerAssistantModels()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (7)

**NPM Packages:**
- `zod`

**Relative Imports:**
- `./schemas`
- `./models`
- `./file-config`
- `./api-endpoints`
- `./types/files`
- `./mcp`



# 7. Database Interaction Mapping
**Database:** MongoDB via Mongoose



# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
const shape = schema.shape;
  const entries = Object.entries(shape).map(([key, value]) => {
    if (value instanceof z.ZodDefault) {
      // Extract default value if it exists
      return [key, value._def.defaultValue()];
```

**Snippet 2:**
```typescript
apiKey: z.string(),
  serverless: z.boolean().optional(),
  instanceName: z.string().optional(),
  deploymentName: z.string().optional(),
  assistants: z.boolean().optional(),
  addParams: z.record(z.any()).optional(),
  dropParams: z.array(z.string()).optional(),
  forcePrompt: z.boolean().optional
```

**Snippet 3:**
```typescript
anyscale = 'anyscale',
  apipie = 'apipie',
  cohere = 'cohere',
  fireworks = 'fireworks',
  deepseek = 'deepseek',
  groq = 'groq',
  helicone = 'helicone',
  huggingface = 'huggingface',
  mistral = 'mistral',
  mlx = 'mlx',
  ollama = 'ollama',
  openrouter = 'openrouter',
  perplexity = 'perple
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Shared:** Shared package code


# 12. Migration Concerns & Recommendations
- Contains TODO/FIXME comments indicating technical debt
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (1)

- `zod`



# 14. Tags
```
- typescript
- application-code
- librechat
- source-file
```

