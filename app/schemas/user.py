from datetime import datetime
from fastapi_users import schemas
from pydantic import EmailStr, ConfigDict


class UserRead(schemas.BaseUser[int]):
    """
    Schema for reading user data, including additional fields such as
    `created_at`, `updated_at`, `common_role`, and flags for status.
    """
    id: int
    email: str
    created_at: datetime
    updated_at: datetime
    common_role: int
    is_deleted: bool
    is_active: bool
    is_superuser: bool

    model_config = ConfigDict()


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    common_role: int
