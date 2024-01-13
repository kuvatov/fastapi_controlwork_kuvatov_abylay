import pydantic


class BaseModel(pydantic.BaseModel):
    class Config:
        populate_by_name = True
        