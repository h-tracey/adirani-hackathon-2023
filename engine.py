from sqlalchemy import create_engine

URL = 'mysql://root:example@host.docker.internal/analytics'

def get_engine():
    return create_engine(URL)
