from db.models import Subject
from db.repositories.base import BaseRepository


class SubjectRepository(BaseRepository):
    model = Subject
    