from tortoise import models, exceptions
from uuid import UUID

from core.exc import common as common_exc


class BaseRepository:
    model = models.Model
    
    async def get(self, **kwargs) -> list[models.Model]:
        try:
            return await self.model.filter(**kwargs)
        except exceptions.DoesNotExist as e:
            raise common_exc.NotFoundException(
                f'{self.model.__name__} not found'
            ) from e
    
    async def get_by_id(self, id: UUID) -> models.Model:
        try:
            return await self.model.get(id=id)
        except exceptions.DoesNotExist as e:
            raise common_exc.NotFoundException(
                f'{self.model.__name__} not found'
            ) from e
    
    async def create(self, **data) -> models.Model:
        try:
            return await self.model.create(**data)
        except exceptions.IntegrityError as e:
            raise common_exc.CreateException(
                f'Creation failed. Details {e}'
            ) from e
    
    async def update(self, id: UUID, **data) -> models.Model:
        try:
            instance = await self.model.get(id=id)
            await instance.update_from_dict(data=data).save()
            return await instance
        except exceptions.IntegrityError as e:
            raise common_exc.UpdateException(
                f'Update failed. Details {e}'
            ) from e
        except exceptions.DoesNotExist as e:
            raise common_exc.NotFoundException(
                f'{self.model.__name__} not found'
            ) from e
    
    async def delete(self, id: UUID) -> None:
        try:
            instance = await self.model.get(id=id)
            await instance.delete()
        except exceptions.IntegrityError as e:
            raise common_exc.UpdateException(
                f'Update failed. Details {e}'
            ) from e
        except exceptions.DoesNotExist as e:
            raise common_exc.NotFoundException(
                f'{self.model.__name__} not found'
            ) from e
    