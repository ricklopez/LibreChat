# File: api/server/services/twoFactorService.js

# 1. Purpose
**File Type:** JS (Business logic service)

**What this file represents:**
This file is a business logic service located at `api/server/services/twoFactorService.js`.

**Documentation:** Base32 alphabet for TOTP secret encoding.


**File size:** 6,471 bytes


# 2. Domain Role
**Domain:** Application Logic

**Business relevance:**
This file is part of the Application Logic domain within the LibreChat application.

**Role:** Business logic implementation
- Implements domain-specific operations
- Coordinates between data layer and API layer
- Enforces business rules and validation


# 3. Public API (FULL DETAIL)
### Exported Functions




# 4. Internal Structure
### Internal Functions (8)

- `encodeBase32()`
- `decodeBase32()`
- `generateTOTPSecret()`
- `verifyTOTP()`
- `generateBackupCodes()`
- `verifyBackupCode()`
- `getTOTPSecret()`
- `generate2FATempToken()`



# 5. Internal Behavior & Data Flow
### Data Flow Steps

1. **Input:** Parameters from controller/caller
2. **Transformations:** Business logic processing
3. **External calls:** Database models, external APIs
4. **Output:** Processed data or operation result


# 6. Relationships & Collaboration
### Imported Dependencies (4)

**NPM Packages:**
- `node:crypto`
- `@librechat/api`
- `jsonwebtoken`

**Aliased Imports:**
- `~/models`



# 7. Database Interaction Mapping
**No direct database interaction.**


# 8. UI Behavior (if applicable)
**No UI behavior.** (Not a UI component)


# 9. Key Logic Snippets
**Key logic excerpts:**

**Snippet 1:**
```javascript
let bits = 0;
  let value = 0;
  let output = '';
  for (const byte of buffer) {
    value = (value << 8) | byte;
    bits += 8;
    while (bits >= 5) {
      output += BASE32_ALPHABET[(value >>> (bits - 5)) & 31];
      bits -= 5;
```

**Snippet 2:**
```javascript
const cleaned = base32Str.replace(/=+$/, '').toUpperCase();
  let bits = 0;
  let value = 0;
  const output = [];
  for (const char of cleaned) {
    const idx = BASE32_ALPHABET.indexOf(char);
    if (idx === -1) {
      continue;
```

**Snippet 3:**
```javascript
const randomArray = new Uint8Array(10);
  webcrypto.getRandomValues(randomArray);
  return encodeBase32(Buffer.from(randomArray));
```



# 10. Architectural Concerns
**Security:** Handles sensitive data (passwords, tokens, authentication)
**Async Behavior:** Asynchronous operations present


# 11. Migration Mapping (Legacy → Modern)
### Target Location in Modern System

**Backend:** Business logic service
- Service: Business logic layer
- Module: `twoFactorServiceService`


# 12. Migration Concerns & Recommendations
- Contains complex conditional logic that may need review


# 13. Dependencies
### dependsOn (4)

- `node:crypto`
- `@librechat/api`
- `~/models`
- `jsonwebtoken`



# 14. Tags
```
- javascript
- service
- business-logic
- application-code
- librechat
- source-file
```

