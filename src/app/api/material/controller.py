from uuid import UUID
from core.controller import BaseController
from db.repositories.material import MaterialRepository
from core.exc import common as common_exc
from core.exc import http as http_exc


class MaterialController(BaseController):
    repository = MaterialRepository()
    
    async def create(self, subject_id: UUID = None, **kwargs) -> dict:
        try:
            material = await self.repository.create(subject_id=subject_id, **kwargs)
            return material
        except common_exc.CreateException as e:
            raise http_exc.HTTPBadRequestException() from e
        