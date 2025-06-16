from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'oi'

# rota que retorna None quando não há dado para a
# chave utilizada
@app.route('/acesso')
def index():
    nome = session.get('usuario')
    return f"{nome}"

# tentando remover chave inexistentes
@app.route('/remove')
def remove():
    session.pop('usuario')
    return "Removido"


# adicionar dado a sessão
@app.route('/adicionar')
def add():
    session['user'] = 'romer'
    session['novo_user'] = 'romer2'
    return "Adicionado"

