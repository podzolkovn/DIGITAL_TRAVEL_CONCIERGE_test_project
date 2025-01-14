from fastapi import APIRouter
from app.api.v1.routers.auth import router as auth_router

router: APIRouter = APIRouter()

router.include_router(auth_router)
