from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport

from app.core.config import settings

# Initialize Bearer transport with the token URL
bearer_transport: BearerTransport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    """
    Returns a JWT strategy for authentication using a secret key,
    a token lifetime, and the HS256 algorithm.
    """
    return JWTStrategy(secret=settings.SECRET_JWT, lifetime_seconds=3600, algorithm="HS256")


# Authentication backend using Bearer transport and JWT strategy
bearer_backend: AuthenticationBackend = AuthenticationBackend(
    name="bearer",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
