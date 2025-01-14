from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from app.core.security import bearer_backend
from app.domain.managers.user import get_user_manager
from app.domain.models.user import User
from app.schemas.user import UserRead, UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager=get_user_manager,
    auth_backends=[bearer_backend],
)

router.include_router(
    fastapi_users.get_auth_router(bearer_backend),
)


router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)
