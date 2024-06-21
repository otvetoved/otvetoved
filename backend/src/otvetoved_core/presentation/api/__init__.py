from fastapi import APIRouter

from .handlers import questions, authentication

router = APIRouter(prefix="/v1")

router.include_router(questions.router)
router.include_router(authentication.router)
