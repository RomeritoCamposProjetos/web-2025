from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

engine = create_engine('mysql://root:romerito@localhost/bancao')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass
