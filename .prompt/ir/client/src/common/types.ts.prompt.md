# File: client/src/common/types.ts

# 1. Purpose
**File Type:** TS (Application code)

**What this file represents:**
This file is a application code located at `client/src/common/types.ts`.

**Documentation:** as InputNumberPrimitive from 'rc-input-number';

**Primary exports:** 96 exported element(s)
- isEphemeralAgent
- ConfigFieldDetail
- CodeBarProps

**File size:** 16,587 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions

- `isEphemeralAgent(agentId: string | null | undefined)`
- `ConfigFieldDetail()` — named export
- `CodeBarProps()` — named export
- `PromptsEditorMode()` — named export
- `STTEndpoints()` — named export
- `TTSEndpoints()` — named export
- `AudioChunk()` — named export
- `BadgeItem()` — named export
- `AssistantListItem()` — named export
- `AgentListItem()` — named export
- `TPluginMap()` — named export
- `GenericSetter()` — named export
- `LastSelectedModels()` — named export
- `LocalizeFunction()` — named export
- `ChatFormValues()` — named export
- `mainTextareaId()` — named export
- `globalAudioId()` — named export
- `IconContext()` — named export
- `IconMapProps()` — named export
- `IconComponent()` — named export
- `AgentIconComponent()` — named export
- `IconComponentTypes()` — named export
- `IconsRecord()` — named export
- `AgentIconMapProps()` — named export
- `NavLink()` — named export
- `NavProps()` — named export
- `DataColumnMeta()` — named export
- `Panel()` — named export
- `FileSetter()` — named export
- `ActionAuthForm()` — named export
- `MCPForm()` — named export
- `ActionWithNullableMetadata()` — named export
- `AssistantPanelProps()` — named export
- `AgentPanelProps()` — named export
- `MCPServerInfo()` — named export
- `AgentPanelContextType()` — named export
- `AgentModelPanelProps()` — named export
- `AugmentedColumnDef()` — named export
- `TSetOption()` — named export
- `TSetExample()` — named export
- `OnInputNumberChange()` — named export
- `defaultDebouncedDelay()` — named export
- `ESide()` — named export
- `NotificationSeverity()` — named export
- `TShowToast()` — named export
- `TBaseSettingsProps()` — named export
- `TSettingsProps()` — named export
- `TModels()` — named export
- `TModelSelectProps()` — named export
- `TEditPresetProps()` — named export
- `TSetOptions()` — named export
- `TSetOptionsPayload()` — named export
- `TPresetItemProps()` — named export
- `TOnClick()` — named export
- `TGenButtonProps()` — named export
- `TAskProps()` — named export
- `TOptions()` — named export
- `TAskFunction()` — named export
- `TMessageProps()` — named export
- `TMessageIcon()` — named export
- `TInitialProps()` — named export
- `TAdditionalProps()` — named export
- `TMessageContentProps()` — named export
- `TText()` — named export
- `TEditProps()` — named export
- `TDisplayProps()` — named export
- `TConfigProps()` — named export
- `TDangerButtonProps()` — named export
- `TDialogProps()` — named export
- `TPluginStoreDialogProps()` — named export
- `TResError()` — named export
- `TAuthContext()` — named export
- `TUserContext()` — named export
- `TAuthConfig()` — named export
- `IconProps()` — named export
- `Option()` — named export
- `StringOption()` — named export
- `VoiceOption()` — named export
- `TMessageAudio()` — named export
- `OptionWithIcon()` — named export
- `DropdownValueSetter()` — named export
- `MentionOption()` — named export
- `PromptOption()` — named export
- `TOptionSettings()` — named export
- `ExtendedFile()` — named export
- `ModelItemProps()` — named export
- `ContextType()` — named export
- `SwitcherProps()` — named export
- `TLoginLayoutContext()` — named export
- `NewConversationParams()` — named export
- `ConvoGenerator()` — named export
- `TBaseResData()` — named export
- `TResData()` — named export
- `TFinalResData()` — named export
- `TVectorStore()` — named export
- `TThread()` — named export



# 4. Internal Structure
### Internal Functions (1)

- `isEphemeralAgent()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (2)

**NPM Packages:**
- `react`
- `librechat-data-provider`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```typescript
return agentId == null || agentId === '' || agentId === Constants.EPHEMERAL_AGENT_ID;
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Frontend:** Frontend code


# 12. Migration Concerns & Recommendations
*No major migration concerns identified. Standard migration process should apply.*


# 13. Dependencies
### dependsOn (2)

- `react`
- `librechat-data-provider`



# 14. Tags
```
- typescript
- application-code
- librechat
- source-file
```

