
ROLE_PERMISSIONS = {
    "ADMIN": [
        "general",
        "engineering_docs",
        "salary_sheet",
        "api_security",
    ],
    "HR_MANAGER": [
        "general",
        "salary_sheet",
    ],
    "ENGINEER": [
        "general",
        "engineering_docs",
        "api_security",
    ],
    "INTERN": [
        "general",
    ],
}


def check_permission(role: str, resource: str) -> dict:
    permitted_resources = ROLE_PERMISSIONS.get(role, [])
    allowed = resource in permitted_resources

    return {
        "allowed": allowed,
        "resource": resource,
        "reason": (
            "Permission granted"
            if allowed
            else "Role is not authorized for this resource"
        ),
    }
