from fastapi import APIRouter
from api.subject.routes import subject_router


router = APIRouter(prefix='/api')
router.include_router(subject_router)
