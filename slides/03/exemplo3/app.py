from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    method = request.method
    return f"<h1>Minha primeira aplicação: método HTTP - {method}</h1>"


@app.route('/cadastro' ,methods=['GET'])
def create():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def store():
    nome = request.form['nome']    
    return f"<h1>Você cadastrou essa pessoa: {nome} </h1>"