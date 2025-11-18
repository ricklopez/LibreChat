# LibreChat Repository Structure Analysis

**Analysis Date:** 2025-11-18
**Purpose:** Complete architectural analysis for DotPrompt workspace planning

---

## 1. File Classification by Language

### Language Distribution

**Backend (api/):**
- **453 JavaScript files** - Node.js/Express backend
- ES6 modules with CommonJS
- No TypeScript in main backend (uses JSDoc for types)

**Frontend (client/):**
- **935 TypeScript/TSX files** - React application
- Full TypeScript coverage for type safety
- React components with TSX

**Shared Packages (packages/):**
- **TypeScript** - data-schemas, data-provider, client utilities
- **JavaScript** - Legacy API utilities
- Mixed TS/JS with gradual migration to TypeScript

**Configuration & Build:**
- **JavaScript** - Vite config, ESLint, build scripts
- **YAML** - Docker, Helm charts, librechat.yaml config
- **JSON** - Package manifests, tsconfig files

### File Type Summary

```
.js      - 453 files (backend)
.tsx     - 600+ files (React components)
.ts      - 335 files (types, hooks, utilities)
.json    - 50+ files (config, manifests)
.yaml    - 20+ files (Docker, K8s, config)
.md      - 15+ files (documentation)
```

---

## 2. Directory Architecture

### Root Structure

```
/LibreChat
├── api/                    # Node.js/Express backend
├── client/                 # React/Vite frontend
├── packages/               # Shared libraries (monorepo)
├── config/                 # Configuration utilities
├── e2e/                    # Playwright end-to-end tests
├── .prompt/                # DotPrompt workspace
├── utils/                  # Utility scripts
├── redis-config/           # Redis configuration
├── helm/                   # Kubernetes/Helm charts
├── docs/                   # Documentation
├── docker-compose.yml      # Docker orchestration
└── package.json            # Monorepo workspace config
```

### Backend Architecture (api/)

```
api/
├── server/
│   ├── index.js                 # Express app entry point
│   ├── controllers/             # Request handlers
│   │   ├── agents/              # Agent CRUD operations
│   │   ├── assistants/          # OpenAI/Azure assistants
│   │   ├── auth/                # Authentication logic
│   │   ├── UserController.js    # User management
│   │   ├── PermissionsController.js
│   │   └── mcp.js               # MCP tool endpoints
│   ├── routes/                  # Express routes
│   │   ├── agents/              # /api/agents/*
│   │   ├── assistants/          # /api/assistants/*
│   │   ├── prompts.js           # /api/prompts/*
│   │   ├── messages.js          # /api/messages/*
│   │   ├── convos.js            # /api/convos/*
│   │   ├── auth.js              # /api/auth/*
│   │   ├── mcp.js               # /api/mcp/*
│   │   └── files/               # /api/files/*
│   ├── services/                # Business logic layer
│   │   ├── Endpoints/           # LLM provider implementations
│   │   │   ├── openAI/          # OpenAI/ChatGPT
│   │   │   ├── anthropic/       # Claude
│   │   │   ├── google/          # Gemini
│   │   │   ├── agents/          # Agent execution
│   │   │   └── custom/          # Ollama, OpenRouter
│   │   ├── PermissionService.js # RBAC logic
│   │   ├── ActionService.js     # Custom actions
│   │   ├── ToolService.js       # Tool management
│   │   ├── MCP.js               # MCP server manager
│   │   └── Config/              # App configuration
│   ├── middleware/              # Request processing
│   │   ├── requireJwtAuth.js    # JWT validation
│   │   ├── checkBan.js          # User ban checking
│   │   ├── validateEndpoint.js  # Endpoint validation
│   │   ├── accessResources/     # Resource ACL
│   │   └── limiters/            # Rate limiting
│   └── utils/                   # Helper utilities
├── models/                      # Mongoose schemas
│   ├── Agent.js                 # Agent config & versions
│   ├── Conversation.js          # Chat conversations
│   ├── Message.js               # Chat messages
│   ├── Prompt.js                # Prompt templates
│   ├── PromptGroup.js           # Prompt collections
│   ├── User.js                  # User accounts
│   ├── Role.js                  # Custom roles
│   ├── Action.js                # Custom actions/tools
│   └── File.js                  # File metadata
├── app/
│   └── clients/                 # LLM client implementations
│       ├── BaseClient.js        # Abstract base
│       ├── OpenAIClient.js      # ChatGPT client
│       ├── AnthropicClient.js   # Claude client
│       ├── GoogleClient.js      # Gemini client
│       └── tools/               # Tool utilities
├── strategies/                  # Passport auth strategies
│   ├── jwtStrategy.js           # JWT tokens
│   ├── localStrategy.js         # Username/password
│   ├── ldapStrategy.js          # LDAP
│   ├── googleStrategy.js        # Google OAuth
│   └── githubStrategy.js        # GitHub OAuth
└── db/
    └── connect.js               # MongoDB connection
```

### Frontend Architecture (client/)

```
client/
├── src/
│   ├── components/              # React components (26 dirs)
│   │   ├── Agents/              # Agent UI
│   │   ├── Chat/                # Main chat interface
│   │   │   ├── ChatView.tsx     # Chat display
│   │   │   ├── Input/           # Message input
│   │   │   ├── Messages/        # Message list
│   │   │   └── Header/          # Chat header
│   │   ├── Conversations/       # Conversation sidebar
│   │   ├── Prompts/             # Prompt library
│   │   ├── MCP/                 # MCP server UI
│   │   ├── Endpoints/           # Model selection
│   │   ├── Files/               # File management
│   │   ├── Nav/                 # Navigation
│   │   ├── SidePanel/           # Right sidebar
│   │   │   ├── Agents/          # Agent panel
│   │   │   ├── Files/           # Files panel
│   │   │   ├── Prompts/         # Prompts panel
│   │   │   └── Tools/           # Tools panel
│   │   ├── Auth/                # Login/signup
│   │   └── ui/                  # Reusable components
│   ├── routes/                  # React Router pages
│   │   ├── ChatRoute.tsx        # Main chat page
│   │   ├── Dashboard.tsx        # Home/dashboard
│   │   ├── Search.tsx           # Search page
│   │   └── ShareRoute.tsx       # Shared conversations
│   ├── store/                   # Jotai atoms (global state)
│   │   ├── agents.ts            # Agent state
│   │   ├── endpoints.ts         # Selected endpoint
│   │   ├── prompts.ts           # Prompt state
│   │   ├── mcp.ts               # MCP servers
│   │   └── settings.ts          # User settings
│   ├── Providers/               # React Context providers (30+)
│   │   ├── ChatContext.tsx      # Current chat
│   │   ├── AgentsContext.tsx    # Agents data
│   │   ├── PromptGroupsContext.tsx
│   │   ├── MessagesViewContext.tsx
│   │   └── MCPPanelContext.tsx
│   ├── hooks/                   # Custom React hooks
│   ├── utils/                   # Helper functions
│   └── localization/            # i18n translations
├── public/                      # Static assets
└── vite.config.ts               # Vite build config
```

### Shared Packages (packages/)

```
packages/
├── data-schemas/                # TypeScript schemas & types
│   ├── src/
│   │   ├── schema/              # Mongoose schemas
│   │   │   ├── agent.ts
│   │   │   ├── prompt.ts
│   │   │   ├── conversation.ts
│   │   │   ├── message.ts
│   │   │   └── user.ts
│   │   ├── types/               # TypeScript interfaces
│   │   ├── methods/             # Mongoose methods
│   │   └── crypto/              # Encryption utils
├── data-provider/               # React Query integration
│   ├── src/
│   │   ├── data-service.ts      # Main service class
│   │   ├── request.ts           # HTTP client
│   │   └── react-query/         # Custom hooks
│   │       ├── agents.ts        # Agent queries
│   │       ├── prompts.ts       # Prompt queries
│   │       ├── messages.ts      # Message queries
│   │       └── conversations.ts
├── api/                         # Shared backend utils
│   └── src/
│       ├── cluster/             # Leader election
│       ├── oauth/               # OAuth tokens
│       └── files/               # File processing
└── client/                      # Shared frontend utils
```

---

## 3. Frameworks Detected

### Backend Frameworks & Libraries

| Framework/Library | Version | Purpose |
|------------------|---------|---------|
| **Express.js** | 4.21.2 | HTTP server framework |
| **Mongoose** | 8.12.1 | MongoDB ODM |
| **Passport.js** | 0.6.0 | Authentication middleware |
| **@librechat/agents** | 3.0.20 | Agent orchestration framework |
| **LangChain** | 0.3.79 | Tool & chain abstractions |
| **Winston** | 3.11.0 | Logging framework |
| **ioredis** | 5.4.2 | Redis client |
| **Keyv** | 5.2.0 | Key-value storage abstraction |
| **Multer** | 1.4.5-lts.1 | File upload handling |
| **Sharp** | 0.33.6 | Image processing |
| **Meilisearch** | 0.45.0 | Full-text search |

### LLM Provider SDKs

| SDK | Version | Provider |
|-----|---------|----------|
| **openai** | 5.8.2 | OpenAI/ChatGPT |
| **@anthropic-ai/sdk** | 0.52.0 | Anthropic Claude |
| **@google/generative-ai** | 0.24.0 | Google Gemini |
| **@langchain/google-genai** | 0.1.10 | Google via LangChain |
| **@aws-sdk/client-bedrock-runtime** | 3.740.0 | AWS Bedrock |

### Frontend Frameworks & Libraries

| Framework/Library | Version | Purpose |
|------------------|---------|---------|
| **React** | 18.2.0 | UI library |
| **Vite** | 6.4.1 | Build tool & dev server |
| **React Router DOM** | 6.11.2 | Client-side routing |
| **Tailwind CSS** | 3.4.1 | CSS framework |
| **Jotai** | 2.12.5 | Atomic state management |
| **Recoil** | 0.7.7 | State management (legacy) |
| **TanStack React Query** | 4.28.0 | Server state management |
| **React Hook Form** | 7.43.9 | Form management |
| **Framer Motion** | 11.5.4 | Animation library |
| **i18next** | 24.2.2 | Internationalization |
| **React Markdown** | 9.0.1 | Markdown rendering |

### UI Component Libraries

| Library | Purpose |
|---------|---------|
| **@radix-ui/react-*** | Accessible UI primitives (25+ components) |
| **lucide-react** | Icon library |
| **react-avatar-editor** | Avatar cropping |
| **react-dnd** | Drag & drop |

### Testing Frameworks

| Framework | Version | Purpose |
|-----------|---------|---------|
| **Jest** | 30.2.0 | Unit testing |
| **Playwright** | 1.56.1 | E2E testing |
| **Vitest** | 2.2.7 | Vite-native testing |

---

## 4. Backend / Frontend / Shared Boundaries

### Backend Boundary (`/api`)

**Responsibilities:**
- HTTP API server (Express)
- Database operations (MongoDB/Mongoose)
- Authentication & authorization (Passport, JWT)
- LLM provider integrations (OpenAI, Anthropic, Google, etc.)
- Agent execution & orchestration
- File storage & processing
- MCP server management
- Business logic & validation
- Logging & monitoring

**Key Entry Points:**
- `api/server/index.js` - Express app initialization
- `api/models/` - Data models
- `api/server/routes/` - API endpoints
- `api/server/services/` - Business logic

**External Interfaces:**
- REST API at `/api/*`
- WebSocket connections for streaming
- File upload/download endpoints
- OAuth callbacks

### Frontend Boundary (`/client`)

**Responsibilities:**
- User interface rendering (React)
- Client-side routing (React Router)
- State management (Jotai, Context API)
- Server data caching (React Query)
- Form validation & submission
- Real-time message streaming
- File upload UI
- Internationalization (i18n)
- Theme management (dark/light mode)

**Key Entry Points:**
- `client/src/routes/index.tsx` - Router config
- `client/src/components/` - UI components
- `client/src/store/` - Global state atoms
- `client/src/Providers/` - Context providers

**External Interfaces:**
- Consumes `/api/*` REST endpoints
- WebSocket client for streaming
- Browser APIs (localStorage, FileReader, etc.)

### Shared Boundary (`/packages`)

**Responsibilities:**
- **Type definitions** shared between frontend & backend
- **Data schemas** for MongoDB models (TypeScript)
- **HTTP client** for API requests
- **React Query hooks** for data fetching
- **Validation logic** for shared entities
- **Utilities** used across frontend & backend
- **Constants & enums**

**Key Packages:**

1. **@librechat/data-schemas** (Backend → Frontend)
   - Mongoose schemas defined in TypeScript
   - Exported types for frontend consumption
   - Shared validation logic
   - Used by: `api/` (runtime), `client/` (types)

2. **librechat-data-provider** (Frontend)
   - React Query hooks wrapping API calls
   - TypeScript interfaces for API responses
   - HTTP request utilities
   - Used by: `client/` exclusively

3. **@librechat/api** (Backend)
   - Shared backend utilities
   - OAuth token management
   - File processing (OCR, audio, video)
   - Cluster/leader election
   - Used by: `api/` exclusively

4. **@librechat/client** (Frontend)
   - Shared frontend utilities
   - Type definitions
   - Used by: `client/` exclusively

### Communication Flow

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend (client/)                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  React Components  →  React Query Hooks              │   │
│  │        ↓                      ↓                       │   │
│  │  Jotai Atoms    →  librechat-data-provider           │   │
│  │                            ↓                          │   │
│  │                    HTTP Client (axios)                │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↓
                    REST API (/api/*)
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                        Backend (api/)                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Express Routes  →  Controllers  →  Services          │   │
│  │                            ↓                          │   │
│  │                    Mongoose Models                    │   │
│  │                            ↓                          │   │
│  │                       MongoDB                         │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↑
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Shared (packages/)                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  @librechat/data-schemas (Schemas + Types)            │   │
│  │  librechat-data-provider (React Query Hooks)          │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Domain Models and Business Logic

### Core Domain Entities

#### 1. **User** (`api/models/User.js`)
**Domain:** Identity & Access Management

**Purpose:** Represents a user account with authentication credentials and profile

**Business Rules:**
- Unique username and email
- Password hashing with bcrypt
- Role-based permissions (user, admin, custom roles)
- Token balance tracking for usage limits
- Optional social login providers

**Schema:**
```javascript
{
  username: String (unique),
  email: String (unique),
  password: String (hashed),
  name: String,
  avatar: String,
  role: ObjectId (ref: Role),
  plugins: Array,
  balance: Number,
  emailVerified: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

**Relationships:**
- HAS MANY: Conversations, Messages, Files, Agents, Prompts
- BELONGS TO: Role
- HAS MANY: Transactions (token usage)

---

#### 2. **Agent** (`api/models/Agent.js`)
**Domain:** Agent Orchestration & Configuration

**Purpose:** Defines reusable AI agent configurations with tools, instructions, and versioning

**Business Rules:**
- Agents have multiple versions (A/B testing support)
- Each version has specific tools and MCP servers
- Permissions control who can view/edit/use agents
- Category-based organization
- Production version designation

**Schema:**
```javascript
{
  name: String (required),
  description: String,
  author: ObjectId (ref: User),
  category: String,
  versions: [{
    version: String,
    endpoint: String,  // openAI, anthropic, google, etc.
    model: String,
    instructions: String,
    temperature: Number,
    tools: Array,
    mcp: Array,  // MCP server names
    actionIds: [ObjectId],  // ref: Action
    capabilities: Object
  }],
  productionId: ObjectId,  // points to production version
  isPublic: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

**Business Logic:**
- Version management (create, update, promote to production)
- Tool availability checking
- MCP server binding
- Permission-based access control

**Relationships:**
- BELONGS TO: User (author)
- HAS MANY: Action (via actionIds)
- REFERENCES: MCP servers (by name)
- USED BY: Conversations

---

#### 3. **Prompt / PromptGroup** (`api/models/Prompt.js`)
**Domain:** Prompt Library & Management

**Purpose:** Reusable prompt templates with versioning and categorization

**Business Rules:**
- Prompts grouped into PromptGroups
- Each prompt has multiple versions
- Production version designation
- Category-based organization
- Permissions for sharing/editing

**Schema:**
```javascript
// PromptGroup
{
  name: String (required),
  oneliner: String,
  description: String,
  category: String,
  productionId: ObjectId (ref: Prompt),
  author: ObjectId (ref: User),
  createdAt: Date,
  updatedAt: Date
}

// Prompt (versions)
{
  groupId: ObjectId (ref: PromptGroup),
  version: String,
  prompt: String (the actual prompt text),
  author: ObjectId (ref: User),
  createdAt: Date
}
```

**Business Logic:**
- Prompt versioning (create, list, promote to production)
- Aggregation pipeline for efficient querying with production lookups
- Permission-based access

**Relationships:**
- PromptGroup HAS MANY: Prompt (versions)
- Prompt BELONGS TO: PromptGroup
- BELONGS TO: User (author)

---

#### 4. **Conversation** (`api/models/Conversation.js`)
**Domain:** Chat Session Management

**Purpose:** Represents a chat session with messages, configuration, and metadata

**Business Rules:**
- Each conversation has a unique conversationId
- Associated with one user
- Configured with endpoint (OpenAI, Anthropic, etc.) and model
- Can have agent configuration
- Can be shared or archived

**Schema:**
```javascript
{
  conversationId: String (unique),
  user: ObjectId (ref: User),
  title: String,
  endpoint: String,  // openAI, anthropic, google, agents, etc.
  model: String,
  agentId: ObjectId (ref: Agent),
  promptId: ObjectId (ref: Prompt),
  tools: Array,
  files: [ObjectId] (ref: File),
  tags: [String],
  isArchived: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

**Business Logic:**
- Conversation creation/update
- Message association
- Agent binding
- File attachment
- Tagging and search

**Relationships:**
- BELONGS TO: User
- HAS MANY: Message
- BELONGS TO: Agent (optional)
- BELONGS TO: Prompt (optional)
- HAS MANY: File (attachments)

---

#### 5. **Message** (`api/models/Message.js`)
**Domain:** Chat Message Storage

**Purpose:** Individual messages within a conversation (user or assistant)

**Business Rules:**
- Messages belong to conversations
- Can be user or assistant sender
- Supports tool calls and artifacts
- Can be edited or deleted
- Tracks token usage

**Schema:**
```javascript
{
  messageId: String (unique),
  conversationId: ObjectId (ref: Conversation),
  user: ObjectId (ref: User),
  sender: String,  // 'User' or 'Assistant'
  text: String,
  isCreatedByUser: Boolean,
  parentMessageId: String,  // for threading
  tokenCount: Number,
  model: String,
  endpoint: String,
  finish_reason: String,
  error: Boolean,
  unfinished: Boolean,
  files: [ObjectId] (ref: File),
  createdAt: Date,
  updatedAt: Date
}
```

**Business Logic:**
- Message creation/streaming
- Token counting
- Error handling
- File associations

**Relationships:**
- BELONGS TO: Conversation
- BELONGS TO: User
- HAS MANY: File (attachments)
- REFERENCES: Message (parent, for threading)

---

#### 6. **Action** (`api/models/Action.js`)
**Domain:** Custom Tool/Function Definition

**Purpose:** Custom actions that agents can execute (API calls, calculations, etc.)

**Business Rules:**
- Actions are reusable across agents
- Defined with JSON schema for parameters
- Can have authentication requirements
- Permission-based access

**Schema:**
```javascript
{
  name: String (required),
  description: String,
  author: ObjectId (ref: User),
  metadata: {
    domain: String,
    api_type: String,  // rest, graphql, etc.
    auth: Object
  },
  parameters: Object (JSON schema),
  createdAt: Date,
  updatedAt: Date
}
```

**Business Logic:**
- Action creation/update
- Parameter validation
- Permission checking

**Relationships:**
- BELONGS TO: User (author)
- USED BY: Agent (via actionIds)

---

#### 7. **Role** (`api/models/Role.js`)
**Domain:** Role-Based Access Control (RBAC)

**Purpose:** Custom user roles with specific permissions

**Business Rules:**
- Built-in roles: USER, ADMIN
- Custom roles with granular permissions
- Permissions for models, endpoints, tools, agents, prompts

**Schema:**
```javascript
{
  name: String (unique),
  permissions: {
    models: [String],
    endpoints: [String],
    tools: [String],
    agents: Object,
    prompts: Object,
    actions: Object
  },
  isDefault: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

**Business Logic:**
- Permission checking for resources
- Default role assignment
- Custom role creation

**Relationships:**
- HAS MANY: User

---

#### 8. **File** (`api/models/File.js`)
**Domain:** File Storage & Management

**Purpose:** Metadata for uploaded files (images, documents, audio, etc.)

**Business Rules:**
- Files associated with users, conversations, messages
- Supports multiple storage backends (local, S3, Azure Blob)
- File type validation
- Size limits
- Automatic cleanup of orphaned files

**Schema:**
```javascript
{
  file_id: String (unique),
  user: ObjectId (ref: User),
  conversationId: String,
  messageId: String,
  filename: String,
  filepath: String,
  type: String,  // image, document, audio, etc.
  bytes: Number,
  width: Number,  // for images
  height: Number,
  embedded: Boolean,  // if used for RAG
  createdAt: Date,
  updatedAt: Date
}
```

**Business Logic:**
- File upload/download
- Storage backend selection
- File processing (image resize, OCR, audio transcription)
- Cleanup of unused files

**Relationships:**
- BELONGS TO: User
- BELONGS TO: Conversation (optional)
- BELONGS TO: Message (optional)

---

#### 9. **Transaction** (`api/models/Transaction.js`)
**Domain:** Token Usage & Billing

**Purpose:** Tracks token spending for rate limiting and billing

**Business Rules:**
- Records every LLM API call
- Tracks input/output tokens separately
- Deducts from user balance
- Prevents usage if balance is zero (optional)

**Schema:**
```javascript
{
  user: ObjectId (ref: User),
  conversationId: String,
  model: String,
  context: String,  // prompt, completion, etc.
  tokenType: String,  // prompt_tokens, completion_tokens
  rawAmount: Number,
  tokenValue: Number,
  rate: Number,
  createdAt: Date
}
```

**Business Logic:**
- Token counting
- Balance checking
- Transaction logging

**Relationships:**
- BELONGS TO: User

---

### Business Logic Layers

#### Controllers (`api/server/controllers/`)
**Responsibility:** HTTP request/response handling

**Pattern:**
```javascript
async function createAgent(req, res) {
  try {
    // 1. Extract & validate input
    const { name, description, category, version } = req.body;

    // 2. Call service layer
    const agent = await AgentService.create({
      ...req.body,
      author: req.user.id
    });

    // 3. Return response
    res.status(201).json({ agent });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
```

**Examples:**
- `agents/v1.js` - Agent CRUD
- `auth/LoginController.js` - User authentication
- `UserController.js` - User profile management

#### Services (`api/server/services/`)
**Responsibility:** Business logic implementation

**Pattern:**
```javascript
class AgentService {
  static async create(data) {
    // 1. Validate business rules
    if (!data.name) throw new Error('Name required');

    // 2. Check permissions
    await PermissionService.checkCanCreate(data.author, 'agent');

    // 3. Create entity
    const agent = await Agent.create(data);

    // 4. Post-processing (notifications, logging, etc.)
    logger.info(`Agent created: ${agent.id}`);

    return agent;
  }
}
```

**Examples:**
- `PermissionService.js` - RBAC logic
- `ToolService.js` - Tool management
- `MCP.js` - MCP server lifecycle

#### Models (`api/models/`)
**Responsibility:** Data persistence & validation

**Pattern:**
```javascript
const agentSchema = new Schema({
  name: { type: String, required: true },
  author: { type: ObjectId, ref: 'User' },
  // ... fields
});

// Instance methods
agentSchema.methods.getProductionVersion = function() {
  return this.versions.find(v => v._id.equals(this.productionId));
};

// Static methods
agentSchema.statics.findByCategory = function(category) {
  return this.find({ category });
};

const Agent = mongoose.model('Agent', agentSchema);
```

---

## 6. API Endpoints

### Authentication Endpoints

**Base Path:** `/api/auth`

| Method | Endpoint | Purpose | Auth |
|--------|----------|---------|------|
| POST | `/login` | User login with username/password | None |
| POST | `/logout` | User logout | JWT |
| POST | `/register` | New user registration | None |
| POST | `/refresh` | Refresh JWT token | Refresh token |
| GET | `/session` | Get current session info | JWT (optional) |
| POST | `/password/change` | Change password | JWT |
| POST | `/password/forgot` | Request password reset | None |
| POST | `/password/reset` | Reset password with token | None |
| GET | `/google` | Google OAuth login | None |
| GET | `/google/callback` | Google OAuth callback | None |
| GET | `/github` | GitHub OAuth login | None |
| GET | `/github/callback` | GitHub OAuth callback | None |

**Request/Response Example:**
```javascript
// POST /api/auth/login
Request: { username: "user@example.com", password: "secret" }
Response: {
  token: "jwt_token...",
  user: { id, username, email, role }
}
```

---

### Agent Endpoints

**Base Path:** `/api/agents`

| Method | Endpoint | Purpose | Auth | Permissions |
|--------|----------|---------|------|-------------|
| GET | `/` | List agents (paginated) | JWT | - |
| GET | `/:id` | Get agent details | JWT | VIEW |
| GET | `/:id/expanded` | Get full agent config | JWT | EDIT |
| POST | `/` | Create new agent | JWT | CREATE |
| PATCH | `/:id` | Update agent | JWT | EDIT |
| DELETE | `/:id` | Delete agent | JWT | DELETE |
| GET | `/categories` | Get agent categories | JWT | - |
| GET | `/actions/:agentId` | Get agent actions | JWT | VIEW |
| GET | `/tools/:agentId` | Get available tools | JWT | VIEW |

**Request/Response Examples:**
```javascript
// GET /api/agents?page=1&pageSize=10&category=productivity
Response: {
  agents: [{
    id: "...",
    name: "Code Helper",
    description: "...",
    author: {...},
    category: "productivity",
    productionVersion: {...}
  }],
  pagination: { page: 1, total: 50, pages: 5 }
}

// POST /api/agents
Request: {
  name: "Research Assistant",
  description: "Helps with research",
  category: "research",
  version: {
    version: "1.0",
    endpoint: "anthropic",
    model: "claude-3-5-sonnet",
    instructions: "You are a helpful research assistant...",
    tools: ["web_search", "calculator"],
    mcp: ["@modelcontextprotocol/server-github"]
  }
}
Response: { agent: {...} }
```

---

### Prompt Endpoints

**Base Path:** `/api/prompts`

| Method | Endpoint | Purpose | Auth | Permissions |
|--------|----------|---------|------|-------------|
| GET | `/groups` | List prompt groups | JWT | - |
| GET | `/groups/:groupId` | Get prompt group | JWT | VIEW |
| POST | `/groups` | Create prompt group | JWT | CREATE |
| PATCH | `/groups/:groupId` | Update prompt group | JWT | EDIT |
| DELETE | `/groups/:groupId` | Delete prompt group | JWT | DELETE |
| GET | `/` | List prompts | JWT | - |
| GET | `/:promptId` | Get prompt version | JWT | VIEW |
| POST | `/` | Create prompt | JWT | CREATE |
| PATCH | `/:promptId` | Update prompt | JWT | EDIT |
| DELETE | `/:promptId` | Delete prompt | JWT | DELETE |
| POST | `/:promptId/production` | Promote to production | JWT | EDIT |

**Request/Response Examples:**
```javascript
// GET /api/prompts/groups?category=technical
Response: {
  promptGroups: [{
    id: "...",
    name: "Code Review",
    oneliner: "Review code for quality",
    category: "technical",
    productionPrompt: { version: "2.0", prompt: "..." }
  }]
}

// POST /api/prompts
Request: {
  groupId: "...",
  version: "1.0",
  prompt: "You are an expert code reviewer. Review the following code:\n\n{{code}}"
}
Response: { prompt: {...} }
```

---

### Conversation Endpoints

**Base Path:** `/api/convos`

| Method | Endpoint | Purpose | Auth |
|--------|----------|---------|------|
| GET | `/` | List conversations | JWT |
| GET | `/:convId` | Get conversation details | JWT |
| POST | `/` | Create conversation | JWT |
| PATCH | `/:convId` | Update conversation | JWT |
| DELETE | `/:convId` | Delete conversation | JWT |
| POST | `/clear` | Delete all conversations | JWT |
| GET | `/tags` | Get conversation tags | JWT |
| PATCH | `/:convId/tags` | Update conversation tags | JWT |

**Request/Response Examples:**
```javascript
// GET /api/convos?pageNumber=1
Response: {
  conversations: [{
    conversationId: "...",
    title: "Discussion about React",
    endpoint: "anthropic",
    model: "claude-3-5-sonnet",
    agentId: "...",
    createdAt: "2025-11-18T..."
  }],
  pageNumber: 1,
  pageSize: 20
}

// POST /api/convos
Request: {
  endpoint: "openAI",
  model: "gpt-4o",
  agentId: "agent_xyz"
}
Response: { conversation: {...} }
```

---

### Message Endpoints

**Base Path:** `/api/messages`

| Method | Endpoint | Purpose | Auth |
|--------|----------|---------|------|
| GET | `/` | Get messages for conversation | JWT |
| POST | `/` | Create/update message | JWT |
| DELETE | `/:messageId` | Delete message | JWT |
| GET | `/:messageId` | Get single message | JWT |

**Request/Response Examples:**
```javascript
// GET /api/messages?conversationId=conv_123
Response: {
  messages: [{
    messageId: "msg_1",
    conversationId: "conv_123",
    sender: "User",
    text: "Hello!",
    createdAt: "..."
  }, {
    messageId: "msg_2",
    conversationId: "conv_123",
    sender: "Assistant",
    text: "Hi! How can I help?",
    createdAt: "..."
  }]
}
```

---

### MCP Endpoints

**Base Path:** `/api/mcp`

| Method | Endpoint | Purpose | Auth |
|--------|----------|---------|------|
| GET | `/tools` | Get all available MCP tools | JWT |
| GET | `/servers` | List connected MCP servers | JWT |
| GET | `/:serverName/oauth/initiate` | Start OAuth for MCP server | JWT |
| GET | `/:serverName/oauth/callback` | OAuth callback handler | JWT |
| POST | `/servers/:serverId/reconnect` | Reconnect MCP server | JWT |
| GET | `/servers/:serverId/status` | Get server status | JWT |

**Request/Response Examples:**
```javascript
// GET /api/mcp/tools
Response: {
  tools: [{
    name: "github_create_issue",
    description: "Create a GitHub issue",
    serverName: "@modelcontextprotocol/server-github",
    parameters: { /* JSON schema */ }
  }, {
    name: "filesystem_read",
    description: "Read file contents",
    serverName: "@modelcontextprotocol/server-filesystem",
    parameters: { /* JSON schema */ }
  }]
}
```

---

### File Endpoints

**Base Path:** `/api/files`

| Method | Endpoint | Purpose | Auth |
|--------|----------|---------|------|
| POST | `/upload` | Upload file | JWT |
| POST | `/images` | Upload image | JWT |
| GET | `/:fileId` | Download file | JWT |
| DELETE | `/:fileId` | Delete file | JWT |
| GET | `/avatar` | Get user avatar | JWT |
| POST | `/avatar` | Upload avatar | JWT |
| POST | `/speech/tts` | Text-to-speech | JWT |
| POST | `/speech/stt` | Speech-to-text | JWT |

**Request/Response Examples:**
```javascript
// POST /api/files/upload (multipart/form-data)
Request: FormData { file: File, conversationId: "conv_123" }
Response: {
  file: {
    file_id: "file_abc",
    filename: "document.pdf",
    type: "document",
    bytes: 123456,
    url: "/api/files/file_abc"
  }
}
```

---

### User Endpoints

**Base Path:** `/api/user`

| Method | Endpoint | Purpose | Auth |
|--------|----------|---------|------|
| GET | `/` | Get user profile | JWT |
| PATCH | `/` | Update user profile | JWT |
| DELETE | `/` | Delete user account | JWT |
| GET | `/balance` | Get token balance | JWT |
| GET | `/permissions` | Get user permissions | JWT |

---

### Assistants Endpoints

**Base Path:** `/api/assistants`

| Method | Endpoint | Purpose | Auth |
|--------|----------|---------|------|
| GET | `/` | List OpenAI/Azure assistants | JWT |
| POST | `/` | Create assistant | JWT |
| GET | `/:id` | Get assistant details | JWT |
| PATCH | `/:id` | Update assistant | JWT |
| DELETE | `/:id` | Delete assistant | JWT |

---

### Action Endpoints

**Base Path:** `/api/actions`

| Method | Endpoint | Purpose | Auth | Permissions |
|--------|----------|---------|------|-------------|
| GET | `/` | List actions | JWT | - |
| GET | `/:id` | Get action details | JWT | VIEW |
| POST | `/` | Create action | JWT | CREATE |
| PATCH | `/:id` | Update action | JWT | EDIT |
| DELETE | `/:id` | Delete action | JWT | DELETE |

---

### Config Endpoints

**Base Path:** `/api/config`

| Method | Endpoint | Purpose | Auth |
|--------|----------|---------|------|
| GET | `/` | Get app configuration | JWT (optional) |
| GET | `/endpoints` | Get available endpoints | JWT (optional) |
| GET | `/models` | Get available models | JWT (optional) |

**Response Example:**
```javascript
// GET /api/config
Response: {
  appTitle: "LibreChat",
  socialLogins: ["google", "github"],
  fileUploadEnabled: true,
  maxFileSize: 100000000,
  availableTools: ["web_search", "calculator", "code_interpreter"],
  mcpEnabled: true
}
```

---

## 7. Prompt/Agent Infrastructure

### Agent Architecture

#### 1. Agent Model & Storage

**Location:** `api/models/Agent.js`

**Core Concepts:**
- **Agent** = Reusable AI configuration with:
  - Endpoint (OpenAI, Anthropic, Google, etc.)
  - Model (gpt-4o, claude-3-5-sonnet, etc.)
  - Instructions (system prompt)
  - Tools (web_search, calculator, custom actions, MCP tools)
  - Parameters (temperature, max_tokens, etc.)

**Versioning System:**
- Multiple versions per agent (v1.0, v1.1, v2.0)
- Production version designation
- Enables A/B testing and gradual rollouts

**Schema Structure:**
```javascript
{
  name: "Code Helper",
  description: "Assists with coding tasks",
  author: ObjectId(user),
  category: "development",
  versions: [{
    version: "1.0",
    endpoint: "anthropic",
    model: "claude-3-5-sonnet-20241022",
    instructions: "You are an expert programmer...",
    temperature: 0.7,
    max_tokens: 4096,
    tools: ["web_search", "code_interpreter"],
    mcp: ["@modelcontextprotocol/server-github"],
    actionIds: [ObjectId(action1), ObjectId(action2)]
  }],
  productionId: ObjectId(version),  // points to active version
  isPublic: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

---

#### 2. Agent Execution Flow

**Location:** `api/server/services/Endpoints/agents/`

**Execution Steps:**

1. **Agent Loading**
   - Controller receives request with `agentId`
   - Service loads agent from database
   - Resolves production version
   - Validates user permissions (VIEW or USE)

2. **Tool Resolution**
   - Load custom actions by `actionIds`
   - Resolve MCP server tools
   - Load built-in tools (web_search, calculator, etc.)
   - Create LangChain Tool instances

3. **LLM Client Initialization**
   - Select appropriate client (OpenAIClient, AnthropicClient, etc.)
   - Configure with agent's model and parameters
   - Inject system instructions
   - Bind tools to client

4. **Message Execution**
   - User message sent to LLM
   - LLM may invoke tools (function calling)
   - Tool results sent back to LLM
   - Final response generated

5. **Result Storage**
   - Message saved to database
   - Token usage tracked in Transaction
   - User balance updated

**Code Flow:**
```
User Request
     ↓
Express Route (/api/agents/chat)
     ↓
Controller (agentsController.chat)
     ↓
Service (AgentService.execute)
     ↓
Agent Model (load config)
     ↓
Tool Service (resolve tools)
     ↓
LLM Client (execute with tools)
     ↓
Response
```

---

#### 3. Action System (Custom Tools)

**Location:** `api/models/Action.js`, `api/server/services/ActionService.js`

**Purpose:** Define custom functions/tools that agents can call

**Action Schema:**
```javascript
{
  name: "get_weather",
  description: "Get current weather for a location",
  author: ObjectId(user),
  metadata: {
    domain: "weather.api.com",
    api_type: "rest",
    auth: {
      type: "bearer",
      token: "encrypted_token"
    }
  },
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "City name"
      },
      units: {
        type: "string",
        enum: ["metric", "imperial"]
      }
    },
    required: ["location"]
  },
  createdAt: Date,
  updatedAt: Date
}
```

**Action Execution:**
1. Agent config includes `actionIds: [...]`
2. ActionService loads action definitions
3. Creates LangChain StructuredTool instances
4. LLM calls tool via function calling
5. ActionService executes API request
6. Result returned to LLM

**Permissions:**
- Actions have VIEW, EDIT, DELETE permissions
- Users can share actions with specific roles
- System actions available to all users

---

#### 4. MCP (Model Context Protocol) Integration

**Location:** `api/server/services/MCP.js`, `api/server/services/Tools/mcp.js`

**What is MCP?**
- Standard protocol for tool/resource discovery
- MCP servers expose tools, resources, and prompts
- Agents can connect to MCP servers to access tools

**MCP Server Configuration:**
```yaml
# librechat.yaml
mcpServers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_TOKEN: "ghp_..."

  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem"]
    env:
      ALLOWED_DIRECTORIES: "/workspace"
```

**MCP Service Responsibilities:**
1. **Server Lifecycle Management**
   - Start MCP servers on app init
   - Monitor server health
   - Reconnect on failure
   - Graceful shutdown

2. **Tool Discovery**
   - Query MCP servers for available tools
   - Cache tool definitions
   - Convert to LangChain Tool format

3. **OAuth Handling** (for servers requiring auth)
   - Initiate OAuth flows
   - Handle callbacks
   - Store tokens securely

4. **Tool Invocation**
   - Route tool calls to appropriate MCP server
   - Handle parameter marshaling
   - Return results to agent

**MCP in Agent Config:**
```javascript
agent.versions[0].mcp = [
  "@modelcontextprotocol/server-github",
  "@modelcontextprotocol/server-filesystem"
]
```

**Available MCP Tools Example:**
```javascript
// From GitHub MCP server
{
  name: "github_create_issue",
  description: "Create a new GitHub issue",
  parameters: {
    repo: "owner/repo",
    title: "Issue title",
    body: "Issue description"
  }
}

// From Filesystem MCP server
{
  name: "filesystem_read",
  description: "Read file contents",
  parameters: {
    path: "/path/to/file"
  }
}
```

---

### Prompt Architecture

#### 1. Prompt Model & Storage

**Location:** `api/models/Prompt.js`

**Two-Level Structure:**
1. **PromptGroup** - Collection of related prompts
2. **Prompt** - Individual prompt versions

**PromptGroup Schema:**
```javascript
{
  name: "Code Review Template",
  oneliner: "Review code for quality and security",
  description: "Comprehensive code review checklist",
  category: "development",
  productionId: ObjectId(prompt),  // points to production version
  author: ObjectId(user),
  createdAt: Date,
  updatedAt: Date
}
```

**Prompt Schema:**
```javascript
{
  groupId: ObjectId(promptGroup),
  version: "2.0",
  prompt: `You are an expert code reviewer.

Review the following code for:
1. Code quality and readability
2. Security vulnerabilities
3. Performance issues
4. Best practices

Code:
{{code}}

Provide specific recommendations.`,
  author: ObjectId(user),
  createdAt: Date
}
```

**Versioning Benefits:**
- Test different prompt variations
- Promote best-performing to production
- Track prompt evolution over time

---

#### 2. Prompt Usage Flow

**Scenario 1: Agent with Prompt**
```javascript
// Agent config
agent.versions[0].promptId = ObjectId(promptGroup)

// At runtime:
1. Load agent config
2. Load promptGroup by promptId
3. Resolve production prompt version
4. Inject prompt as system instructions
5. Execute with LLM
```

**Scenario 2: User Selects Prompt**
```javascript
// Frontend: User selects prompt from library
<PromptSelector onSelect={(promptId) => {...}} />

// Backend: Load prompt and inject
const promptGroup = await PromptGroup.findById(promptId);
const prompt = await Prompt.findById(promptGroup.productionId);
systemMessage = prompt.prompt;
```

**Prompt Variables:**
- Prompts support variables: `{{variable_name}}`
- Variables replaced at runtime
- Example: `{{code}}`, `{{language}}`, `{{context}}`

---

#### 3. Prompt Aggregation Pipeline

**Location:** `api/models/Prompt.js` (static method)

**Purpose:** Efficiently query prompt groups with production prompt details

**MongoDB Aggregation:**
```javascript
PromptGroup.aggregate([
  { $match: { category: "development" } },
  { $lookup: {
      from: "prompts",
      localField: "productionId",
      foreignField: "_id",
      as: "productionPrompt"
  }},
  { $unwind: "$productionPrompt" },
  { $sort: { createdAt: -1 } }
])
```

**Result:**
```javascript
[{
  _id: ObjectId(...),
  name: "Code Review",
  category: "development",
  productionPrompt: {
    version: "2.0",
    prompt: "You are...",
    createdAt: Date
  }
}]
```

---

#### 4. Prompt Library UI

**Location:** `client/src/components/Prompts/`

**Features:**
- Browse prompts by category
- Search prompts by name/description
- Create new prompts
- Edit existing prompts
- Create new versions
- Promote version to production
- Share prompts with other users

**Context Provider:**
- `PromptGroupsContext.tsx` - Global prompt state
- React Query hooks for data fetching
- Optimistic updates for better UX

---

### Tool Management

**Location:** `api/server/services/ToolService.js`

**Tool Types:**

1. **Built-in Tools**
   - `web_search` - Search the web (DuckDuckGo, Google)
   - `calculator` - Mathematical calculations
   - `code_interpreter` - Execute Python code
   - `dalle` - Generate images with DALL-E
   - `tavily_search` - Tavily search API

2. **Custom Actions**
   - User-defined tools
   - API integrations (REST, GraphQL)
   - Database queries
   - Third-party services

3. **MCP Tools**
   - Tools from MCP servers
   - GitHub, filesystem, web browsing, etc.
   - Dynamically discovered

**Tool Resolution Flow:**
```
Agent Config: tools = ["web_search", "custom_action_1", "github_create_issue"]
     ↓
ToolService.getToolsForAgent(agentId)
     ↓
1. Load built-in tools: web_search → WebSearchTool
2. Load custom actions: custom_action_1 → Action model → LangChain Tool
3. Load MCP tools: github_create_issue → MCP server → LangChain Tool
     ↓
Return array of LangChain Tool instances
     ↓
Pass to LLM client
```

---

### Permission System for Agents/Prompts

**Location:** `api/server/services/PermissionService.js`

**Permission Levels:**
1. **VIEW** - Can see agent/prompt details
2. **EDIT** - Can modify agent/prompt
3. **DELETE** - Can delete agent/prompt
4. **USE** - Can execute agent/prompt

**Permission Storage:**
```javascript
// Embedded in Agent/Prompt models
{
  permissions: {
    users: [{
      userId: ObjectId(user),
      level: "EDIT"
    }],
    roles: [{
      roleId: ObjectId(role),
      level: "VIEW"
    }]
  }
}
```

**Permission Checking:**
```javascript
// Middleware
async function canAccessAgentResource(req, res, next) {
  const agent = await Agent.findById(req.params.id);
  const hasPermission = await PermissionService.check(
    req.user.id,
    agent,
    'VIEW'
  );
  if (!hasPermission) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  next();
}
```

---

### Frontend Agent/Prompt UI

#### Agent Management UI

**Location:** `client/src/components/Agents/`

**Key Components:**
- `AgentPanel.tsx` - Agent selection sidebar
- `AgentBuilder.tsx` - Agent creation/editing form
- `AgentVersionManager.tsx` - Version management
- `AgentToolSelector.tsx` - Tool selection interface

**Features:**
- Drag-and-drop tool selection
- Live preview of agent instructions
- Version comparison
- Permission management UI

#### Prompt Management UI

**Location:** `client/src/components/Prompts/`

**Key Components:**
- `PromptLibrary.tsx` - Browse prompt collection
- `PromptEditor.tsx` - Create/edit prompts
- `PromptVersionHistory.tsx` - View version history
- `PromptVariableEditor.tsx` - Define prompt variables

**Features:**
- Rich text editor for prompts
- Variable insertion
- Category organization
- Template library

---

### Agent/Prompt Execution Monitoring

**Location:** `api/server/utils/LoggingSystem.js`, `api/models/Transaction.js`

**Logging:**
```javascript
logger.info('Agent execution started', {
  agentId: agent._id,
  userId: user._id,
  conversationId: conv._id,
  tools: agent.versions[0].tools
});

logger.debug('Tool invoked', {
  toolName: 'web_search',
  parameters: { query: 'LibreChat features' }
});

logger.info('Agent execution completed', {
  duration: 2.3,
  tokensUsed: 1500,
  toolCallsCount: 3
});
```

**Token Usage Tracking:**
```javascript
// Create transaction record
await Transaction.create({
  user: user._id,
  conversationId: conv._id,
  model: 'claude-3-5-sonnet',
  context: 'agent_execution',
  tokenType: 'completion_tokens',
  rawAmount: 1500,
  tokenValue: 1500,
  rate: 0.015,  // $ per 1K tokens
  createdAt: new Date()
});
```

---

## 8. Recommended DotPrompt Plan Structure

Based on the comprehensive analysis above, here is the recommended DotPrompt workspace structure for organizing IR files and architecture plans:

### Directory Structure

```
.prompt/
├── analysis/                           # Repository analysis outputs
│   ├── repo-structure.md               # This document
│   ├── dependency-graph.json           # File dependency mapping
│   ├── semantic-index.md               # Cross-file semantic index
│   └── technology-stack.md             # Detailed tech stack analysis
│
├── ir/                                 # Intermediate Representation (per-file)
│   ├── backend/                        # Backend IR files
│   │   ├── models/                     # Database model IR
│   │   │   ├── Agent.ir.md
│   │   │   ├── Prompt.ir.md
│   │   │   ├── Conversation.ir.md
│   │   │   ├── Message.ir.md
│   │   │   ├── User.ir.md
│   │   │   ├── Action.ir.md
│   │   │   ├── Role.ir.md
│   │   │   └── File.ir.md
│   │   ├── controllers/                # Controller IR
│   │   │   ├── agents/
│   │   │   │   └── v1.ir.md
│   │   │   ├── auth/
│   │   │   │   ├── LoginController.ir.md
│   │   │   │   └── RegistrationController.ir.md
│   │   │   ├── UserController.ir.md
│   │   │   └── mcp.ir.md
│   │   ├── services/                   # Service layer IR
│   │   │   ├── Endpoints/
│   │   │   │   ├── agents/
│   │   │   │   ├── openAI/
│   │   │   │   └── anthropic/
│   │   │   ├── PermissionService.ir.md
│   │   │   ├── ToolService.ir.md
│   │   │   ├── MCP.ir.md
│   │   │   └── ActionService.ir.md
│   │   ├── routes/                     # Route IR
│   │   │   ├── agents.ir.md
│   │   │   ├── prompts.ir.md
│   │   │   ├── messages.ir.md
│   │   │   ├── convos.ir.md
│   │   │   └── mcp.ir.md
│   │   ├── middleware/                 # Middleware IR
│   │   │   ├── requireJwtAuth.ir.md
│   │   │   ├── checkBan.ir.md
│   │   │   └── validateEndpoint.ir.md
│   │   └── clients/                    # LLM client IR
│   │       ├── BaseClient.ir.md
│   │       ├── OpenAIClient.ir.md
│   │       └── AnthropicClient.ir.md
│   │
│   ├── frontend/                       # Frontend IR files
│   │   ├── components/
│   │   │   ├── Agents/
│   │   │   │   ├── AgentPanel.ir.md
│   │   │   │   ├── AgentBuilder.ir.md
│   │   │   │   └── AgentVersionManager.ir.md
│   │   │   ├── Prompts/
│   │   │   │   ├── PromptLibrary.ir.md
│   │   │   │   ├── PromptEditor.ir.md
│   │   │   │   └── PromptVersionHistory.ir.md
│   │   │   ├── Chat/
│   │   │   │   ├── ChatView.ir.md
│   │   │   │   ├── Input/
│   │   │   │   └── Messages/
│   │   │   ├── Conversations/
│   │   │   │   └── ConversationList.ir.md
│   │   │   └── MCP/
│   │   │       └── MCPServerManager.ir.md
│   │   ├── store/
│   │   │   ├── agents.ir.md
│   │   │   ├── prompts.ir.md
│   │   │   ├── endpoints.ir.md
│   │   │   └── mcp.ir.md
│   │   ├── Providers/
│   │   │   ├── ChatContext.ir.md
│   │   │   ├── AgentsContext.ir.md
│   │   │   └── PromptGroupsContext.ir.md
│   │   └── routes/
│   │       ├── ChatRoute.ir.md
│   │       └── Dashboard.ir.md
│   │
│   └── shared/                         # Shared package IR
│       ├── data-schemas/
│       │   ├── agent.schema.ir.md
│       │   ├── prompt.schema.ir.md
│       │   └── conversation.schema.ir.md
│       └── data-provider/
│           ├── agents.hooks.ir.md
│           ├── prompts.hooks.ir.md
│           └── request.ir.md
│
└── plan/                               # Architecture blueprints & migration plans
    ├── app/                            # Application layer plans
    │   ├── server/                     # Backend architecture
    │   │   ├── 00-server-overview.md
    │   │   ├── 01-authentication-flow.md
    │   │   ├── 02-agent-architecture.md
    │   │   ├── 03-prompt-architecture.md
    │   │   ├── 04-conversation-flow.md
    │   │   ├── 05-tool-system.md
    │   │   ├── 06-mcp-integration.md
    │   │   ├── 07-permission-system.md
    │   │   ├── 08-llm-client-layer.md
    │   │   └── 09-file-storage.md
    │   │
    │   └── client/                     # Frontend architecture
    │       ├── 00-client-overview.md
    │       ├── 01-state-management.md
    │       ├── 02-routing-structure.md
    │       ├── 03-component-hierarchy.md
    │       ├── 04-agent-ui-flow.md
    │       ├── 05-prompt-ui-flow.md
    │       ├── 06-chat-interface.md
    │       ├── 07-data-fetching.md
    │       └── 08-real-time-streaming.md
    │
    ├── db/                             # Database architecture
    │   ├── 00-database-overview.md
    │   ├── 01-schema-design.md
    │   ├── 02-relationships.md
    │   ├── 03-indexes.md
    │   ├── 04-migration-strategy.md
    │   └── collections/
    │       ├── agents.md
    │       ├── prompts.md
    │       ├── conversations.md
    │       ├── messages.md
    │       ├── users.md
    │       └── actions.md
    │
    └── shared/                         # Shared architecture
        ├── 00-shared-overview.md
        ├── 01-type-system.md
        ├── 02-api-contracts.md
        ├── 03-validation.md
        ├── 04-error-handling.md
        └── 05-utilities.md
```

### Plan Layer Guidelines

Each plan document should follow this structure:

```markdown
# [Component Name] Architecture

## Purpose
High-level description of what this architectural component handles.

## Scope
- What is included in this component
- What is excluded / delegated to other components

## Key Entities
List of domain models, services, or components involved.

## Data Flow
Step-by-step description of how data flows through the component.

## API Surface
- Inputs (HTTP endpoints, function signatures)
- Outputs (responses, return values)
- Side effects

## Dependencies
- Internal dependencies (other components)
- External dependencies (third-party services, databases)

## Implementation Notes
- Technology choices
- Design patterns used
- Performance considerations
- Security concerns

## Migration Notes
- Changes from legacy system (if applicable)
- Breaking changes
- Backwards compatibility strategy

## Testing Strategy
- Unit test approach
- Integration test approach
- E2E test scenarios

## Open Questions / Decisions Needed
List of unresolved questions or decisions to be made.
```

### IR File Naming Convention

```
<filename>.ir.md
```

Examples:
- `Agent.ir.md` (for `api/models/Agent.js`)
- `AgentPanel.ir.md` (for `client/src/components/Agents/AgentPanel.tsx`)
- `agents.hooks.ir.md` (for `packages/data-provider/src/react-query/agents.ts`)

### Critical Paths to Document First

Based on the analysis, prioritize IR creation for these critical paths:

1. **Agent Execution Path**
   - `Agent.ir.md` (model)
   - `v1.ir.md` (agents controller)
   - `ToolService.ir.md` (service)
   - `BaseClient.ir.md` (LLM client)
   - `AgentPanel.ir.md` (UI)

2. **Prompt Management Path**
   - `Prompt.ir.md` (model)
   - `prompts.ir.md` (route)
   - `PromptLibrary.ir.md` (UI)
   - `PromptEditor.ir.md` (UI)

3. **Authentication & Authorization Path**
   - `User.ir.md` (model)
   - `Role.ir.md` (model)
   - `LoginController.ir.md` (controller)
   - `PermissionService.ir.md` (service)
   - `requireJwtAuth.ir.md` (middleware)

4. **Conversation Flow**
   - `Conversation.ir.md` (model)
   - `Message.ir.md` (model)
   - `convos.ir.md` (route)
   - `messages.ir.md` (route)
   - `ChatView.ir.md` (UI)

5. **MCP Integration**
   - `MCP.ir.md` (service)
   - `mcp.ir.md` (route & controller)
   - `MCPServerManager.ir.md` (UI)

### Tags for Semantic Indexing

Use these tags consistently across IR files:

**Domain Tags:**
- `domain-model` - Database models
- `business-logic` - Services with domain logic
- `ui-component` - React components
- `api-endpoint` - HTTP route handlers

**Function Tags:**
- `authentication` - Auth-related code
- `authorization` - Permission checking
- `agent-orchestration` - Agent execution
- `prompt-management` - Prompt CRUD
- `tool-execution` - Tool/function calling
- `mcp-integration` - MCP server management
- `conversation-management` - Chat sessions
- `message-handling` - Message CRUD
- `file-storage` - File upload/download
- `state-management` - Frontend state

**Architecture Tags:**
- `controller` - HTTP request handlers
- `service` - Business logic layer
- `repository` - Data access layer
- `middleware` - Express middleware
- `client` - LLM API clients
- `validator` - Validation logic
- `transformer` - Data transformation

**Priority Tags:**
- `migration-critical` - Must be migrated/preserved
- `legacy-quirk` - Contains workarounds or tech debt
- `security-sensitive` - Requires security review
- `performance-critical` - Performance considerations

---

## Summary

LibreChat is a **monorepo-based, full-stack AI chat application** with:

- **Backend:** Node.js/Express with MongoDB, supporting multiple LLM providers (OpenAI, Anthropic, Google, etc.)
- **Frontend:** React/TypeScript with Vite, Tailwind CSS, and advanced state management (Jotai, React Query)
- **Shared Packages:** TypeScript schemas, React Query hooks, and utilities shared between frontend/backend
- **Agent System:** Reusable AI agent configurations with tools, MCP servers, and versioning
- **Prompt System:** Prompt library with versioning, categorization, and production designations
- **MCP Integration:** Standard protocol for tool discovery and execution
- **Permission System:** Fine-grained RBAC for agents, prompts, and actions
- **Extensibility:** Plugin architecture for custom tools and LLM providers

The recommended DotPrompt plan structure organizes:
- **IR files** by architectural layer (backend, frontend, shared)
- **Plan documents** by domain (authentication, agents, prompts, conversations)
- **Analysis outputs** for dependency graphs and semantic indexing

This structure enables systematic migration planning, comprehensive documentation, and efficient navigation of the codebase.
