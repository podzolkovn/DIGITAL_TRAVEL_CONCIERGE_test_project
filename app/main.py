from fastapi import FastAPI

from app.api.v1.routers.router import router

app: FastAPI = FastAPI()
app.include_router(router)
