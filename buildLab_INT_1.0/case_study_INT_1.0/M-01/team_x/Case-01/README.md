# M-01 — team_x — Case-01

**Case type:** Product/technical outcome
**Status:** Draft

## Contributors and roles

**Team Lead: Bibek Pant**
**Delivery Owner: Bibek Pant**
**Quality & Documentation Owner: Himal Shrestha and Prashant Subedi**

## Problem 1 — Session Hijacking

**Problem**
An attacker obtains a valid session identifier after a legitimate user has already authenticated, then reuses that token to impersonate the user — via session sniffing, cross-site scripting, session fixation, or infostealer malware. Once stolen, the token grants access without the attacker ever repeating the original login.

**Impact**

- _Database:_ No inherent record ties a session token to anomalous use; without monitoring/audit tables, hijacked sessions can go undetected.
- _Users:_ Account takeover, unauthorized actions performed under the victim's identity, loss of trust in the platform.
- _System:_ Compromised sessions can persist and be reused across requests until they expire or are explicitly invalidated, exposing sensitive systems and high-risk actions to impersonated access.

**Engineering Solutions (Tech Stack Used)**
| Control | Technology | Why |
|---|---|---|
| Encrypted transport | HTTPS/TLS, HSTS | Protects traffic in transit |
| Secure cookies | Secure/HttpOnly cookie flags | Restricts unsafe client-side/script access to session tokens |
| Session hygiene | Session-ID regeneration after login/privilege change, short inactivity timeouts, token/device binding | Limits replay value and lifespan of a stolen token |
| Step-up auth | MFA on sensitive systems/high-risk actions | Adds friction even if a token is compromised |
| Detection & response | Anomaly monitoring (geo-impossibility, device mismatch, concurrent sessions), automated session termination, real-time alerts, password resets, token revocation | Detects and contains hijacked sessions quickly |

**References**

- www.microsoft.com
- www.obsidiansecurity.com
- www.proofpoint.com

## Problem 2 — User Forgets 2FA PIN

**Problem**
When a legitimate user forgets their 2FA PIN, the same mechanism meant to keep attackers out becomes a barrier to the account's real owner. Recovery has to restore access without giving an attacker an easier path in.

**Impact**

- _Database:_ Requires new persisted structures — OTP requests, backup codes, and audit/recovery records — alongside hashed (not recoverable) PIN storage.
- _Users:_ Legitimate users can be locked out of their own accounts; poor recovery UX can push them toward risky workarounds or support-desk backdoors.
- _System:_ Introduces a new attack surface (the recovery flow itself) that must be rate-limited, time-boxed, and audited so it isn't exploitable as a shortcut around 2FA.

**Engineering Solutions (Tech Stack Used)**
| Component | Technology | Why |
|---|---|---|
| Recovery UI | React | Componentized multi-step recovery flow |
| Backend/API | Django + Django REST Framework | Secure REST endpoints for auth/recovery services |
| Relational data | PostgreSQL | Stores users, OTP requests, backup codes, audit records |
| Short-lived data | Redis | TTL-based OTP expiry and rate-limit counters |
| OTP delivery | Twilio / SendGrid | Production-grade SMS/email delivery |
| Credential hashing | bcrypt / Argon2 | Slow, purpose-built hashing — PIN is reset, never retrieved |
| Session control | JWT / server-side sessions | Enables centralized invalidation of other sessions after reset |

Flow: React recovery UI → Django REST API → OTP service/DB verification → PIN-reset token → new PIN screen → hashed PIN stored → all other sessions invalidated + reset alert + audit log.

**References**

- www.pages.nist.gov
- www.cheatsheetseries.owasp.org
- www.en.wikipedia.org

## Context and constraints

**Product stage:**
Design/case-study stage — architecture and control set defined, not yet described as shipped to production.

**Constraints:**

- Recovery flow must use a channel already independently verified and associated with the account (phone/email), not a new unverified channel.
- PINs must be hashed, not stored in recoverable form — recovery has to mean _reset_, not _retrieval_.
- OTPs and rate limits must be time-limited and short-lived (Redis TTL) to bound the attack window.
- Any session/PIN reset must invalidate all other active sessions and notify the verified contact, to close the gap an attacker could otherwise exploit mid-recovery.

**Assumptions:**

- Users have at least one verified recovery channel (phone or email) on file.
- Standard web transport is TLS-secured and cookies can be marked Secure/HttpOnly.
- Backup codes are generated and stored securely ahead of time as a fallback when phone/email isn't available.

**Risks:**

- Excess friction in session controls (short timeouts, frequent re-verification) risks user abandonment or workaround behavior that itself becomes a security hole.
- A poorly rate-limited OTP/recovery flow could be brute-forced or abused as a new attack surface.
- Monitoring for anomalies (geographic impossibility, device mismatch, concurrent sessions) can produce false positives that disrupt legitimate users.

## Approach

**Chosen approach — layered defense-in-depth:**

1. **Transport & cookie hardening:** HTTPS/TLS, HSTS, Secure/HttpOnly cookie attributes to protect tokens in transit and restrict client-side access.
2. **Session hygiene:** session-ID regeneration after login or privilege change, short inactivity timeouts, and device/token binding to limit the value and lifespan of a stolen token.
3. **MFA on sensitive actions:** an added friction layer for high-risk operations, not just initial login.
4. **User training:** guidance on avoiding unsafe networks, recognizing phishing, and logging out of shared devices.
5. **Continuous monitoring + incident response:** detecting anomalies (impossible travel, device mismatch, concurrent sessions) and automatically terminating sessions, alerting, resetting passwords, and revoking tokens.
6. **Forgot-PIN recovery:** an OTP-based reset flow (React front end → Django/DRF backend → OTP service → PostgreSQL/Redis) that issues a time-limited one-time code to a verified channel, enforces rate limits, issues a reset token, stores the new PIN hashed, and invalidates all other sessions with an audit log and notification on completion.

**Alternative considered:**
A simpler, single-layer approach relying only on adding a second login field (e.g., a static PIN check) without session-lifecycle controls or a structured recovery flow. This was rejected because it treats "having 2FA" as sufficient on its own — it does nothing to stop token theft _after_ a successful login, and it leaves no safe, auditable way for a user to regain access if they forget the PIN, likely forcing risky ad-hoc support workarounds instead.

## Evidence

https://en.wikipedia.org/wiki/One-time_password

https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html

https://www.obsidiansecurity.com/

https://www.proofpoint.com/us

## What changed

- Defined a two-part control set: session-hijacking defenses (encryption, session hygiene, monitoring/incident response) and a Forgot-PIN recovery flow (OTP, rate limiting, backup codes, full session invalidation, audit logging).
- Selected the technology stack: React (recovery UI), Django/DRF (API + recovery logic), PostgreSQL (users/OTPs/backup codes/audit records), Redis (OTP TTL + rate-limit counters), Twilio/SendGrid (OTP and alert delivery), bcrypt/Argon2 (PIN hashing), JWT/server-side sessions (centralized invalidation).
- Reframed "forgot PIN" as a reset-only flow (never a retrieval flow) to avoid ever storing a recoverable PIN.

## Result and lessons

**What improved:**
A clearer end-to-end model of authentication as a lifecycle — login, active session protection, and recovery — rather than three disconnected features. This exposed where trade-offs and failure points would occur before implementation.

**What did not work / open questions:**
No production data yet; effectiveness of anomaly-detection thresholds and user tolerance for session friction are still untested.

**What the team will do differently:**

- Favor open standards (TOTP, WebAuthn) over custom cryptographic trust mechanisms.
- Design recovery alongside authentication from the start, not as an afterthought.
- Treat usability as a security property — excessive friction can push users toward unsafe workarounds.
- Diagram architecture and failure paths before implementation to surface trade-offs early.
- Plan rollout, communication, and support carefully for any large-scale auth change.

