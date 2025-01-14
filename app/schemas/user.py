from datetime import datetime
from typing import Optional

from fastapi_users import schemas


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


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    common_role: int
