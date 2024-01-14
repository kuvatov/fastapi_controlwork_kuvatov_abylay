from db.models import Material
from db.repositories.base import BaseRepository


class MaterialRepository(BaseRepository):
    model = Material
    