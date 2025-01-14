from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport

from app.core.config import settings

bearer_transport: BearerTransport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET_JWT, lifetime_seconds=3600, algorithm="HS256")


bearer_backend: AuthenticationBackend = AuthenticationBackend(
    name="bearer",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
