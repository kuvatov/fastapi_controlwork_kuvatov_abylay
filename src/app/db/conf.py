try:
    from core.settings import database_url
except ImportError:
    from src.app.core.settings import database_url
    

def get_tortoise_models_path():
    try:
        import db.models
        return 'db.models'
    except ImportError:
        import src.app.db.models
        return 'src.app.db.models'


TORTOISE_ORM = {
    'connections': {
        'default': f'{database_url}',
    },
    'apps': {
        'models': {
            'models': ['aerich.models', get_tortoise_models_path()],
            'default_connection': 'default',
        },
    },
}
