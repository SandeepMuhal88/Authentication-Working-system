# Authetication

At its core, Authentication (AuthN) is the process of verifying who a user or system is. It proves that an entity is who they claim to be.

It is often confused with Authorization (AuthZ), which happens immediately after. While authentication checks your identity (e.g., verifying your password), authorization determines what you are allowed to do (e.g., admin vs. standard user permissions).

Here is how modern token-based authentication works, which is the standard when building APIs with frameworks like FastAPI or frontends with React/Next.js and Flutter.


# 🔐 FastAPI Authentication — Zero to Hero Roadmap

> **Goal:** FastAPI authentication ko scratch se master karna — concepts, implementation, aur real project mein apply karna (Chanakya AI backend ke liye bhi useful).
> **Owner:** Sandeep
> **Status:** 🟡 Planning phase

---

## 📌 Why This Roadmap

FastAPI mein authentication seekhna zaroori hai kyunki:
- Har real-world backend (jaise Chanakya AI) ko secure API endpoints chahiye
- Data Scientist / Backend role ke interviews mein auth concepts poochhe jaate hain
- Bina auth ke, koi bhi production-ready app incomplete hai

---

## 🗺️ Roadmap Overview (Phase-wise)

| Phase | Topic | Status |
|-------|-------|--------|
| 1 | Basics — HTTP, Headers, Status Codes | ⬜ Not started |
| 2 | FastAPI Fundamentals Recap | ⬜ Not started |
| 3 | Password Hashing (bcrypt/passlib) | ⬜ Not started |
| 4 | OAuth2 + Password Flow (FastAPI built-in) | ⬜ Not started |
| 5 | JWT (JSON Web Tokens) — Access & Refresh | ⬜ Not started |
| 6 | Protecting Routes (Dependencies + `Depends`) | ⬜ Not started |
| 7 | Role-Based Access Control (RBAC) | ⬜ Not started |
| 8 | Database Integration (User model with SQLModel/SQLAlchemy) | ⬜ Not started |
| 9 | Third-party Auth (Google OAuth, optional) | ⬜ Not started |
| 10 | Security Best Practices + Testing | ⬜ Not started |
| 11 | Final Project — Auth System from Scratch | ⬜ Not started |

---

## 📖 Phase-by-Phase Breakdown

### Phase 1: Basics (Foundation)
**Kya seekhna hai:**
- HTTP methods (GET, POST, PUT, DELETE)
- Headers kya hote hain (especially `Authorization` header)
- Status codes: 200, 201, 400, 401, 403, 404, 422, 500
- Cookies vs Tokens — basic difference

**Why:** Auth samajhne se pehle HTTP ka base clear hona chahiye.

---

### Phase 2: FastAPI Fundamentals Recap
**Kya seekhna hai:**
- Path/Query params, Request body (Pydantic models)
- `Depends()` ka basic use
- Middleware ka concept
- FastAPI ka automatic docs (`/docs`, `/redoc`)

**Why:** Auth implement karne ke liye FastAPI ke dependency injection system ki strong understanding chahiye.

---

### Phase 3: Password Hashing
**Kya seekhna hai:**
- Plain text password kabhi store nahi karte — why?
- `passlib` + `bcrypt` library use karke password hash aur verify karna
- Salting kya hota hai

**Hands-on:**
```python
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

hashed = pwd_context.hash("mypassword")
is_valid = pwd_context.verify("mypassword", hashed)
```

---

### Phase 4: OAuth2 + Password Flow
**Kya seekhna hai:**
- OAuth2 ka concept (sirf FastAPI ka built-in "password flow" — pura OAuth2 spec nahi)
- `OAuth2PasswordBearer` aur `OAuth2PasswordRequestForm`
- Login endpoint kaise banate hain jo username/password leke token return kare

**Why:** Yeh FastAPI ka recommended standard tarika hai auth implement karne ka.

---

### Phase 5: JWT (JSON Web Tokens)
**Kya seekhna hai:**
- JWT structure: Header.Payload.Signature
- `python-jose` ya `pyjwt` library se token create/decode karna
- Access token vs Refresh token — difference aur use case
- Token expiry (`exp` claim) set karna

**Hands-on:**
```python
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

---

### Phase 6: Protecting Routes
**Kya seekhna hai:**
- `Depends()` ka use karke current user nikalna token se
- Protected routes banana jo bina valid token ke access na ho
- `HTTPException` ke saath proper error responses dena (401 Unauthorized)

---

### Phase 7: Role-Based Access Control (RBAC)
**Kya seekhna hai:**
- User roles (admin, user, etc.) database mein store karna
- Route-level permission check (e.g., sirf admin delete kar sake)
- Custom dependency banake role-check reusable banana

---

### Phase 8: Database Integration
**Kya seekhna hai:**
- SQLModel ya SQLAlchemy se User table banana
- User CRUD operations (create, read, update)
- Real login flow: DB se user fetch karke password verify karna

---

### Phase 9: Third-party Auth (Optional/Advanced)
**Kya seekhna hai:**
- Google/GitHub OAuth login integration
- `authlib` library ka basic use

---

### Phase 10: Security Best Practices + Testing
**Kya seekhna hai:**
- Environment variables mein secrets rakhna (`.env` + `python-dotenv`)
- Rate limiting basics
- CORS configuration
- Pytest se auth endpoints test karna (login success/fail, protected route access)

---

### Phase 11: Final Project
**Deliverable:** Ek complete "Auth Service" — register, login, JWT tokens, protected routes, role-based access — jo Chanakya AI project mein directly integrate ho sake.

---

## 🛠️ Tools & Libraries Checklist
- [ ] `fastapi`
- [ ] `uvicorn`
- [ ] `passlib[bcrypt]`
- [ ] `python-jose[cryptography]`
- [ ] `python-multipart` (form data ke liye)
- [ ] `sqlmodel` ya `sqlalchemy`
- [ ] `python-dotenv`
- [ ] `pytest`, `httpx` (testing ke liye)

---

## 📅 Suggested Timeline
| Week | Focus |
|------|-------|
| Week 1 | Phase 1–3 (Basics + Hashing) |
| Week 2 | Phase 4–5 (OAuth2 + JWT) |
| Week 3 | Phase 6–7 (Protected Routes + RBAC) |
| Week 4 | Phase 8–9 (DB Integration + Optional OAuth) |
| Week 5 | Phase 10–11 (Security + Final Project) |

---

## ✅ Next Step
Phase 1 se start karo. Har phase complete hone ke baad us row ko `✅ Done` mark karo, aur agar koi doubt ho toh yahin discuss kar sakte hain step-by-step.
