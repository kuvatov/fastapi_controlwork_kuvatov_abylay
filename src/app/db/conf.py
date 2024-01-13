TORTOISE_ORM = {
    'connections': {'default': 'postgres://edu-user:edu-pass@postgres:5432/education'},
    'apps': {
        'models': {
            'models': ['aerich.models'],
            'default_connection': 'default',
        },
    },
}
