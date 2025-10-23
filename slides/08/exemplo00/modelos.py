from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, Session
from sqlalchemy import create_engine, text, String


engine = create_engine("mysql://root:romerito@localhost/flask")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f'Nome: {self.nome}'


with Session(bind=engine) as sessao:
    resultado = sessao.query(User).first()
    print(resultado)
    