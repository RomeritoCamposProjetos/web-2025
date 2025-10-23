from sqlalchemy import create_engine, text

SQLITE = "sqlite:///database.db"

engine = create_engine(SQLITE)

sql = text("""
    CREATE TABLE user IF NOT EXISTS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )"""
)

with engine.connect() as conn:
    sql = text("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY_KEY AUTO_INCREMENT,
            nome TEXT NOT NULL
        )"""
    )
    conn.execute(sql)
    conn.commit()
    conn.close()

# pip install mysqlclient (depende)
engine = create_engine("mysql://root:romerito@localhost/flask")
with engine.connect() as conn:
    sql = text("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL
        )"""
    )
    conn.execute(sql)
    conn.commit()
    conn.close()

