from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Float, ForeignKey

from database.database import session

from flask_login import UserMixin

class Base(DeclarativeBase):
    pass

class User(Base, UserMixin):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email:Mapped[str] = mapped_column(String(50), unique=True)
    senha:Mapped[str] = mapped_column(String(8))
    produtos = relationship('Product', backref='user')

    @classmethod
    def get(cls, user_id):
        session.begin()
        obj = session.query(User).where(User.id == user_id).first()
        session.close()
        return obj

    def get_id(self):
        return str(self.id)


class Product(Base):
    __tablename__ = "products"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[int] = mapped_column(String(50))
    preco:Mapped[float] = mapped_column(Float)
    descricao:Mapped[str] = mapped_column(String(100))

    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
