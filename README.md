# 🛡️ TrustThread AI

### Identity-Aware Security Analysis and Intelligent Access Control

TrustThread AI is a security-focused application designed to evaluate user identity, check resource permissions, analyze potentially risky requests, and maintain an audit trail of security decisions.

The project combines a React-based frontend, a Python FastAPI backend, and PostgreSQL hosted through Supabase to demonstrate an identity-aware security workflow.

## 📌 Problem Statement

Modern applications need more than a basic login mechanism to protect sensitive resources. They must consider who is making a request, whether that user's identity is verified, what permissions they have, and whether the requested action presents a security risk.

Without these checks, applications may allow unauthorized access or fail to maintain a reliable record of security-related activity.

TrustThread AI explores how these checks can be combined into a single application workflow.

## 💡 Solution

TrustThread AI evaluates access requests using three main components:

- **Identity verification:** Retrieves the authenticated user's profile and verification status.
- **Permission management:** Checks whether the user's role is allowed to access a requested resource.
- **Security analysis:** Evaluates the request and its threat level before making an access decision.

The backend combines these results to produce an `ALLOW` or `BLOCK` decision and records security events in PostgreSQL.

## ✨ Features

### 🔐 Authentication and Authorization

The backend includes:

- Email and password authentication
- Password hashing and verification
- JWT-based access tokens
- Protected API endpoints
- Active-account validation

### 🪪 Identity Verification

The application retrieves user information, including:

- User ID
- Name and email
- Role
- Department
- Identity verification status

Identity information contributes to the application's access-decision workflow.

### 🛡️ Security Analysis

TrustThread AI evaluates submitted requests through its security-analysis module.

The workflow includes:

- Request analysis
- Threat-level evaluation
- Permission checks
- Access-decision generation
- Security event logging

Requests are blocked when the configured identity, permission, or threat-level checks fail.

### 👥 Role-Based Access Control

The permission module evaluates the user's role against the requested resource.

This helps demonstrate how applications can apply different access rules to different user roles.

### 📋 Audit Logging

The application records security-related events in the database, including:

- Authentication events
- Security-analysis events
- Resource information
- Access decisions
- Event details and timestamps

The audit API supports retrieving recent records for inspection.

### 🗄️ PostgreSQL Database

TrustThread AI uses PostgreSQL through Supabase for persistent storage.

SQLAlchemy models define the database tables and relationships for users, analysis records, and audit logs.

### 📊 Application Statistics

The statistics endpoint provides counts for:

- Registered users
- Analysis records
- Audit events

These statistics can support future dashboard visualizations and security analytics.

## 🏗️ Architecture

```text
                   ┌────────────────────────┐
                   │          USER          │
                   │   Login and Requests   │
                   └────────────┬───────────┘
                                │
                                ▼
                   ┌────────────────────────┐
                   │     React Frontend     │
                   │      Vite + Axios      │
                   └────────────┬───────────┘
                                │ HTTP API
                                ▼
                   ┌────────────────────────┐
                   │     FastAPI Backend    │
                   │ Authentication + APIs  │
                   └────────────┬───────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
      ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
      │  Identity &  │  │   Security   │  │ Permissions  │
      │     JWT      │  │   Analysis   │  │   Checking  │
      └──────────────┘  └──────────────┘  └──────────────┘
                                │
                                ▼
                   ┌────────────────────────┐
                   │      SQLAlchemy        │
                   │     Database ORM       │
                   └────────────┬───────────┘
                                │
                                ▼
                   ┌────────────────────────┐
                   │   Supabase PostgreSQL  │
                   │ Users, Analyses, Audit │
                   └────────────────────────┘
```

## 🔄 How the Application Works

When a user accesses the application:

1. The user submits their email and password through the frontend.
2. The backend checks the credentials against the registered user record.
3. If authentication succeeds, the backend issues a JWT access token.
4. The frontend sends the token with requests to protected endpoints.
5. The backend retrieves the authenticated user's identity and role.
6. The security module evaluates the submitted request.
7. The permission module checks access to the requested resource.
8. The backend combines the results and returns an `ALLOW` or `BLOCK` decision.
9. The backend records the security event in PostgreSQL.

## 🗄️ PostgreSQL Database

Supabase provides the hosted PostgreSQL database used by the application.

### Database Tables

#### 1. `users`

Stores registered user information.

Important fields include:

- `id`
- `name`
- `email`
- `password_hash`
- `role`
- `department`
- `identity_verified`
- `is_active`
- `created_at`

#### 2. `analysis_records`

Stores information about analyzed requests.

Important fields include:

- `id`
- `user_id`
- `resource`
- `request_text`
- `threat_level`
- `decision`
- `created_at`

#### 3. `audit_logs`

Stores application security events.

Important fields include:

- `id`
- `user_id`
- `event`
- `resource`
- `decision`
- `details`
- `created_at`

### Database Relationships

```text
                 users
                   │
          ┌────────┴────────┐
          ▼                 ▼
   analysis_records      audit_logs
```

A user can be associated with multiple analysis records and audit events. Foreign keys maintain the relationships between the tables.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| React | Frontend user interface |
| Vite | Frontend development server |
| JavaScript / JSX | Frontend application logic |
| Python | Backend programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI application server |
| SQLAlchemy | Database ORM |
| PostgreSQL | Relational database |
| Supabase | Hosted PostgreSQL service |
| PyJWT | JWT authentication tokens |
| pwdlib and Argon2 | Password hashing and verification |
| Axios | Frontend API communication |
| Git and GitHub | Version control and repository hosting |

## 📂 Project Structure

```text
TrustThread-AI/
│
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── permissions.py
│   ├── security.py
│   ├── audit.py
│   ├── init_db.py
│   ├── .env.example
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   └── services/
│   │       └── api.js
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md
```

This is a representative structure. Keep the names aligned with the actual files in your repository. The real `.env` file and `.venv` directory should not be committed.

## 💻 Getting Started

### Prerequisites

Install:

- Python
- Node.js and npm
- Git
- A Supabase project with PostgreSQL access
- Visual Studio Code or another code editor

### 1. Clone the Repository

Replace the example URL with your actual GitHub repository URL.

```bash
git clone https://github.com/YOUR-USERNAME/TrustThread-AI.git
cd TrustThread-AI
```

### 2. Set Up the Backend

Open a terminal in the project directory:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required Python packages:

```powershell
python -m pip install fastapi "uvicorn[standard]" sqlalchemy "psycopg[binary]" python-dotenv "pwdlib[argon2]" PyJWT email-validator
```

### 3. Configure Environment Variables

Create a file named `.env` inside the `backend` folder.

Add your own configuration:

```dotenv
DATABASE_URL=your_supabase_postgresql_connection_string
JWT_SECRET_KEY=your_generated_random_secret
```

Use your actual database connection string and a strong, randomly generated JWT secret.

Never upload the real `.env` file or share its secrets publicly.

### 4. Initialize the Database

From the `backend` directory, run:

```powershell
python init_db.py
```

This tests the database connection and creates the tables defined by the application's SQLAlchemy models.

You will still need to register or create a user record with a correctly hashed password before logging in.

### 5. Run the Backend

```powershell
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Backend URL:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

Health endpoint:

`http://127.0.0.1:8000/health`

### 6. Run the Frontend

Open a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite in the terminal. The development server may use a different port if the default port is already occupied.

The frontend's API configuration defaults to:

`http://127.0.0.1:8000/api`

If you configure a different backend URL, set the frontend's `VITE_API_URL` environment variable accordingly.

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Backend status message |
| `GET` | `/health` | Health check |
| `POST` | `/api/auth/login` | Authenticate a user |
| `GET` | `/api/me` | Retrieve the current user's profile |
| `POST` | `/api/analyze` | Analyze a request and evaluate access |
| `GET` | `/api/audit` | Retrieve recent audit records |
| `GET` | `/api/stats` | Retrieve database statistics |
| `GET` | `/api/documents` | Return the current document list |

Protected endpoints require a valid bearer token in the authorization header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Use the interactive API documentation to inspect the request schemas and responses.

## 🧪 Testing the Application

After starting the frontend and backend:

1. Open the frontend in your browser.
2. Log in using a registered database account.
3. Confirm that the current-user endpoint works.
4. Submit a sample request for security analysis.
5. Review the identity, security, permission, and decision results.
6. Inspect the audit endpoint for recorded events.
7. Check the statistics endpoint.

Use test accounts and non-sensitive sample data during development.

## 🔐 Security

TrustThread AI demonstrates several security practices:

- Password hashing rather than plaintext password storage
- JWT-based authentication for protected API endpoints
- Active-account checks
- Role-based permission evaluation
- Threat-level checks during access decisions
- Database-backed audit records
- Environment variables for private configuration

This project is intended as a development and demonstration application. A production deployment should receive additional security review, including authorization testing, rate limiting, secure secret management, database access controls, and review of audit-log access.

## 🚀 Deployment

The frontend and backend can be deployed separately.

Possible deployment components include:

- **Frontend:**http://localhost:5173/
- **Backend:** http://127.0.0.1:8000
- **Database:**https://supabase.com/dashboard/project/ajbubgbbnbwnqyxymejp

Configure environment variables in the appropriate hosting platforms. Do not expose the database connection string or JWT secret in frontend code.

## 📚 What I Learned

Building TrustThread AI helped me explore:

- Full-stack web application development
- REST API development with FastAPI
- Authentication and JWT tokens
- Password hashing
- Identity-aware access decisions
- Role-based permission checks
- Security-analysis workflows
- SQLAlchemy database modeling
- PostgreSQL and Supabase integration
- Audit logging
- Frontend-to-backend integration

## 🔮 Future Improvements

Potential enhancements include:

- User registration and account management
- Administrative role management
- More advanced threat detection
- Fine-grained resource permissions
- User-specific audit history
- Document storage and access control
- Automated tests
- Dashboard analytics and visualizations
- Production deployment and monitoring
- Improved security reporting

## 👩‍💻 Author

**TrustThread AI**

JAHNAVI KORE
BTECH AIML STUDENT
Github link:https://github.com/jahnavikore15-code



