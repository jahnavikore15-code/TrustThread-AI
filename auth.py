
USERS = {
    "U101": {
        "name": "Rahul",
        "role": "INTERN",
        "department": "ENGINEERING",
        "verified": True,
    },
    "U102": {
        "name": "Priya",
        "role": "HR_MANAGER",
        "department": "HR",
        "verified": True,
    },
    "U103": {
        "name": "Admin",
        "role": "ADMIN",
        "department": "IT",
        "verified": True,
    },
}


def get_user_identity(user_id: str) -> dict:
    user = USERS.get(user_id)

    if user is None:
        return {
            "identity_verified": False,
            "name": "Unknown",
            "role": "UNKNOWN",
            "department": "UNKNOWN",
        }

    return {
        "identity_verified": user["verified"],
        "name": user["name"],
        "role": user["role"],
        "department": user["department"],
    }
