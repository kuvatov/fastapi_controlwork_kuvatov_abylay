from uuid import UUID
import fastapi as fa

from api.material.controller import MaterialController
from api.material.schemas import requests, responses


material_router = fa.APIRouter(prefix='/material', tags=['material'])
material_controller = MaterialController()


@material_router.get('', response_model=list[responses.MaterialGet])
async def get_materials(
    params: requests.MaterialGet = fa.Depends(),
):
    return await material_controller.get(**params.model_dump(exclude_none=True))


@material_router.post('', response_model=responses.MaterialGet)
async def create_material(
    data: requests.MaterialCreate = fa.Body(...),
):
    return await material_controller.create(**data.model_dump())


@material_router.patch('/{uuid}', response_model=responses.MaterialGet)
async def update_material(
    uuid: UUID,
    data: requests.MaterialUpdate = fa.Body(...),
):
    return await material_controller.update(uuid=uuid, **data.model_dump(exclude_none=True))


@material_router.delete('/{uuid}', response_model=None)
async def delete_material(
    uuid: UUID,
):
    await material_controller.delete(id=uuid)
    return fa.Response(status_code=204)
