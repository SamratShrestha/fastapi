from fastapi import APIRouter

from app.routes.user import user_router

api_router = APIRouter()

api_router.include_router(user_router)
