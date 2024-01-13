from core.settings import database_url


TORTOISE_ORM = {
    'connections': {
        'default': f'{database_url}',
    },
    'apps': {
        'models': {
            'models': ['aerich.models', 'db.models'],
            'default_connection': 'default',
        },
    },
}
