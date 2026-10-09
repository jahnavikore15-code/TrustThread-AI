# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from auth import get_user_identity
from security import analyze_security
from permissions import check_permission
from audit import log_event

# 1. Initialize FastAPI app first
app = FastAPI()

# 2. Add CORS middleware after initializing 'app'
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5176", "http://127.0.0.1:5176"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
    user_id: str
    query: str
    resource: str = "general"


@app.get("/")
def home():
    return {"message": "TrustThread AI backend is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/security/analyze")
def analyze(request: AnalyzeRequest):
    identity = get_user_identity(request.user_id)

    security = analyze_security(
        request.query,
        identity["identity_verified"],
    )

    permission = check_permission(
        identity["role"],
        request.resource,
    )

    allowed = (
        identity["identity_verified"]
        and permission["allowed"]
        and security["threat_level"] not in ["HIGH", "CRITICAL"]
    )

    result = {
        "identity": identity,
        "security": security,
        "permission": permission,
        "decision": "ALLOW" if allowed else "BLOCK",
    }

    log_event(request.user_id, request.resource, result["decision"])

    return result