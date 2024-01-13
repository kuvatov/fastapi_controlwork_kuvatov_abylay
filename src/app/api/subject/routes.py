from uuid import UUID
import fastapi as fa

from api.subject.controller import SubjectController
from api.subject.schemas import requests, responses


subject_router = fa.APIRouter(prefix='/subject', tags=['subject'])
subject_controller = SubjectController()


@subject_router.get('', response_model=list[responses.SubjectGet])
async def get_subjects(
    params: requests.SubjectGet = fa.Depends(),
):
    return await subject_controller.get(**params.model_dump(exclude_none=True))


@subject_router.post('', response_model=responses.SubjectGet)
async def create_subject(
    data: requests.SubjectCreate = fa.Body(...),
):
    return await subject_controller.create(**data.model_dump())


@subject_router.patch('/{uuid}', response_model=responses.SubjectGet)
async def update_subject(
    uuid: UUID,
    data: requests.SubjectUpdate = fa.Body(...),
):
    return await subject_controller.update(uuid=uuid, **data.model_dump(exclude_none=True))


@subject_router.delete('/{uuid}', response_model=None)
async def delete_subject(
    uuid: UUID,
):
    await subject_controller.delete(id=uuid)
    return fa.Response(status_code=204)
