from fastapi import APIRouter
from src.views import document_router


def create_router() -> APIRouter:
    router = APIRouter()
    router.include_router(document_router)
    return router
