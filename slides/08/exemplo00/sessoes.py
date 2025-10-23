from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text
from faker import Faker

engine = create_engine("mysql://root:romerito@localhost/flask")

faker = Faker()

# exemplo de inserção de informações no banco
with Session(bind=engine) as sessao:
    SQL = 'INSERT INTO users (nome) VALUES(:nome)'
    for x in range(100):
        nome = faker.name()
        sessao.execute(text(SQL), {'nome': nome})
    
    # commite realiza a modificação no banco aplicando as inserções
    sessao.rollback()
    sessao.commit()


sessao = Session(bind=engine)
SQL = 'SELECT * FROM users'
# retorna um objeto Cursor - usado p
resultado = sessao.execute(text(SQL))

# objeto resultado permite realizar a busca pelo resultado (CursorResult)
# após utilizar uma das opções abaixo o Cursor fecha

# print (resultado.first()) - obtém apenas o primeiro e fecha o cursor.
# print (resultado.fetchone()) - obtém novos até encerrar a lista
# print (resultado.fetchall()) - obtém todos e fecha o cursor
# print (resultado.fetchmany(2)) - obtém um número N de elementos até fechar o cursor




