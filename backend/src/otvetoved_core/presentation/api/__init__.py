from fastapi import APIRouter

from .handlers import questions, authentication, question_answers, rating, user

router = APIRouter(prefix="/v1")

router.include_router(questions.router)
router.include_router(authentication.router)
router.include_router(question_answers.router)
router.include_router(rating.router)
router.include_router(user.router)
