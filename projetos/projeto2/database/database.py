from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('mysql://root:romerito@localhost/produtos')

session = Session(bind=engine)