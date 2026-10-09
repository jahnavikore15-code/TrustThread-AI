
import json
from datetime import datetime, timezone
from pathlib import Path


AUDIT_FILE = Path(__file__).parent / "audit.log"


def log_event(user_id: str, resource: str, decision: str) -> None:
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user_id": user_id,
        "resource": resource,
        "decision": decision,
    }

    with AUDIT_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(event) + "\n")
