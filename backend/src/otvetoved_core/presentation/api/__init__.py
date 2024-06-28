from fastapi import APIRouter

from .handlers import questions, authentication, question_answers

router = APIRouter(prefix="/v1")

router.include_router(questions.router)
router.include_router(authentication.router)
router.include_router(question_answers.router)