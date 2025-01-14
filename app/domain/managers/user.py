from fastapi import Depends

from fastapi_users import BaseUserManager, IntegerIDMixin

from app.core.config import settings
from app.domain.models.user import User
from app.utils.get_user_db import get_user_db

SECRET: str = settings.SECRET_JWT


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret: str = SECRET
    verification_token_secret: str = SECRET


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
