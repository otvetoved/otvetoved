from fastapi import APIRouter

from . import (
    questions,
)


router = APIRouter(prefix="/v1")

router.include_router(questions.router)
