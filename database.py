from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from models import Base

DB_URL = os.path.join("sqlite:///", "db.sqlite")
ENGINE = create_engine(DB_URL, connect_args={"check_same_thread": False})
SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)


def init_db():
    # check_same_thread is for SQLite only
    Base.metadata.create_all(bind=ENGINE)


def get_db():
    database = SESSIONLOCAL()
    try:
        yield database
    finally:
        database.close()
