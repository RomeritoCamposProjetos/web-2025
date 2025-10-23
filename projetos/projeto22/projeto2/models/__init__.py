from database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from database import session

from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column (primary_key=True, autoincrement=True)
    email:Mapped[str] = mapped_column(String(50), unique=True)
    senha:Mapped[str] = mapped_column(String(8))

    @classmethod
    def get(cls, user_id):   
        # buscar o usuário pelo id
        # retornar o objeto usuário
        session.begin()
        res = session.query(User).where(User.id == user_id).first()
        session.close()
        return res

        



