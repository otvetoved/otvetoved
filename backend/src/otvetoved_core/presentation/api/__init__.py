from fastapi import APIRouter

from . import (
    questions,
    authentication,
)


router = APIRouter(prefix="/v1")

router.include_router(questions.router)
router.include_router(authentication.router)
