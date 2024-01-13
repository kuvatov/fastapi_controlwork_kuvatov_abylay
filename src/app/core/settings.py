import os
import pydantic


database_url = pydantic.PostgresDsn(os.getenv('DATABASE_URL'))
