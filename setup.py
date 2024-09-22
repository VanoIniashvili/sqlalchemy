import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

engine = create_engine("sqlite:///database.db", echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def get_session():
    return Session()
