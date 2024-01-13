from core.controller import BaseController
from db.repositories.subject import SubjectRepository


class SubjectController(BaseController):
    repository = SubjectRepository()
    