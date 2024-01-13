from uuid import UUID
from db.repositories.base import BaseRepository

from core.exc import http as http_exc
from core.exc import common as common_exc


class BaseController:
    repository = BaseRepository
    
    async def get(self, **kwargs) -> dict:
        try:
            return await self.repository.get(**kwargs)
        except common_exc.NotFoundException as e:
            raise http_exc.HTTPNotFoundException() from e
    
    async def create(self, **kwargs) -> dict:
        try:
            return await self.repository.create(**kwargs)
        except common_exc.CreateException as e:
            raise http_exc.HTTPBadRequestException() from e
    
    async def update(self, id: UUID, **kwargs) -> dict:
        try:
            return await self.repository.update(id, **kwargs)
        except common_exc.NotFoundException as e:
            raise http_exc.HTTPNotFoundException() from e
        except common_exc.UpdateException as e:
            raise http_exc.HTTPBadRequestException() from e
    
    async def delete(self, id: UUID) -> None:
        try:
            return await self.repository.delete(id)
        except common_exc.NotFoundException as e:
            raise http_exc.HTTPNotFoundException() from e
        except common_exc.DeleteException as e:
            raise http_exc.HTTPBadRequestException() from e
    