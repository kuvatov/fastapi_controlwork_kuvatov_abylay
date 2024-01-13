import fastapi as fa
import uvicorn

from tortoise.contrib.fastapi import register_tortoise

from db.conf import TORTOISE_ORM
from api.router import router


def setup():
    application = fa.FastAPI()
    application.include_router(router)
    
    register_tortoise(
        app=application,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )
    
    return application


app = setup()


def run(**params):
    uvicorn.run('api.application:app', host='0.0.0.0', **params)
    