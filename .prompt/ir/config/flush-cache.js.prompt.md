# File: config/flush-cache.js

# 1. Purpose
**File Type:** JS (Application code)

**What this file represents:**
This file is a application code located at `config/flush-cache.js`.

**Documentation:** !/usr/bin/env node


**File size:** 9,330 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.



# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (8)

- `showHelp()`
- `flushRedisCache()`
- `flushFileCache()`
- `restartRecommendation()`
- `main()`
- `if()`
- `isEnabled()`
- `getRedisCA()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Function parameters
2. **Transformations:** Data processing logic
3. **External calls:** Dependent modules
4. **Output:** Return value or side effects


# 6. Relationships & Collaboration
### Imported Dependencies (4)

**NPM Packages:**
- `path`
- `fs`
- `dotenv`
- `ioredis`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
try {
    console.log('🔍 Redis cache detected');

    if (verbose) {
      console.log(`   URI: ${REDIS_URI ? REDIS_URI.replace(/\/\/.*@/, '//***:***@') : 'Not set'
```

**Snippet 2:**
```javascript
const dataDir = path.join(__dirname, '..', 'data');
  const filesToClear = [path.join(dataDir, 'logs.json'), path.join(dataDir, 'violations.json')];

  console.log('🔍 Checking file-based cache');

  if (dryRun) {
    console.log('🔍 [DRY RUN] Would flush file cache');
    for (const filePath of files
```

**Snippet 3:**
```javascript
try {
      if (fs.existsSync(filePath)) {
        const stats = fs.statSync(filePath);
        totalSize += stats.size;
        fs.unlinkSync(filePath);
        deletedCount++;
        if (verbose) {
          console.log(
            `   ✅ Deleted ${path.basename(filePath)
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Error Handling:** Uses try-catch blocks
**Async Behavior:** Asynchronous operations present
**Logging:** Contains logging statements


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System



# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (4)

- `path`
- `fs`
- `dotenv`
- `ioredis`



# 14. Tags
```
- javascript
- application-code
- librechat
- source-file
```

