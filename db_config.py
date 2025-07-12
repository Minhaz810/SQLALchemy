"""We need a database engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

"""<dialect>+<driver>://<username>:<password>@<host>:<port>/<database>"""

postgres_db_url = (
    """postgresql+psycopg2://<username>:<password>@<host>:<port>/<database>"""
)

mysql_db_url = """mysql://<username>:<password>@<host>:<port>/<database>"""

oracle_db_url = """oracle://<username>:<password>@<host>:<port>/<database>"""

# using postgresql
db_url = "postgresql://postgres:pgadmin@127.0.0.1:5432/sqlalchemy_db"

engine = create_engine(db_url)

Base = declarative_base()
