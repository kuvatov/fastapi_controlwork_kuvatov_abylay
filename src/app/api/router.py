from fastapi import APIRouter
from api.subject.routes import subject_router
from api.material.routes import material_router


router = APIRouter(prefix='/api')
router.include_router(subject_router)
router.include_router(material_router)
