"""
This file intentionally contains a hardcoded token for testing secret scanners
like CodeQL and Gitleaks. Do not use real secrets here.
"""

# Intentionally hardcoded GitHub token pattern to trigger secret detection.
GITHUB_TOKEN = "ghp_1234567890abcdef1234567890abcdef1234"


def build_auth_header(token: str) -> dict:
    """Return a GitHub-style Authorization header using the provided token."""
    return {"Authorization": f"token {token}"}


# Use the token so it is not flagged as an unused variable by linters.
AUTH_HEADER = build_auth_header(GITHUB_TOKEN)


