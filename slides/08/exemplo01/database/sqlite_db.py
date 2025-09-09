from sqlalchemy import create_engine
from sqlalchemy import text

#conexão com o banco de dados SQLITE em arquivo
engine = create_engine("sqlite:///database.db")

def get_connection():
    return engine.connect()

def obter_livros():
    conn = engine.connect()
    resultado = conn.execute(text(
        """
        SELECT * FROM livros
        """
    ))
    return resultado

def inserir_livro(titulo, autor, descricao, capa):
    conn = engine.connect()
    # criando a declaração
    SQL = text("""
        INSERT INTO livros(titulo, autor, descricao, capa) 
        VALUES(:titulo, :autor, :descricao, :capa)
        """)
    #aplicando a declaração
    conn.execute(SQL, 
        {'titulo': titulo, 
         'autor': autor, 
         'descricao': descricao, 'capa': capa}
    )
    conn.commit()
    conn.close()