import hashlib
import pytest

from typing import Any
from fastapi import Response
from fastapi.testclient import TestClient
from fastapi_users.authentication import BearerTransport
from starlette import status

from app.domain.managers.user import get_user_manager
from app.domain.models.user import UserRole, User
from app.main import app
from app.core.config import settings
from app.infrastructure.db import Base, engine
from app.schemas.user import UserCreate


@pytest.fixture(autouse=True)
async def setup_db() -> None:
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(autouse=True)
def setup_client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def test_hash(request) -> str:
    """Generate a test hash based on the test name."""
    return hashlib.md5(request.node.name.encode()).hexdigest()


@pytest.fixture(autouse=True)
def test_user_data(test_hash) -> dict[Any, Any]:
    return {
        "email": f"testuser_{test_hash}_@gmail.com",
        "password": "strongpassword",
        "common_role": UserRole.ADMIN,
    }


@pytest.fixture(autouse=True)
def bearer_transport() -> BearerTransport:
    return BearerTransport(tokenUrl="auth/jwt/login")


@pytest.fixture
async def setup_user(test_user_data):
    user_manager = await anext(get_user_manager())
    user = await user_manager.create(UserCreate(**test_user_data))
    return user


@pytest.fixture(autouse=True)
async def setup_login(
    setup_client: TestClient,
    setup_user: User,
    bearer_transport: BearerTransport,
) -> dict[Any, Any]:

    client: TestClient = setup_client
    user: User = await setup_user
    login_data = {
        "username": user.email,
        "password": "strongpassword",
    }

    response: Response = client.post(bearer_transport.tokenUrl, data=login_data)

    assert response.status_code == status.HTTP_200_OK, "Failed to log in"
    token = response.json()["access_token"]
    return {
        "client": client,
        "token": token,
        "user": user,
    }
