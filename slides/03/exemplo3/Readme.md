# Exemplo 3 - Protocolo HTTP com Flask

## Setup

- Criar ambiente virtual

> python -m venv `env`

`env` é o nome da pasta que guarda as informações do ambiente virtual: pacotes python e demais definições.

- Ativar o ambiente virtual

> .\env\Script\activate

- Instalar o `Flask`

> pip install flask

## Primeira Rota

Vamos criar uma aplicação Flask e adicionar a primeira rota. O trecho de código a seguir é sufiente.

```python
from flask import Flask, request

# criação da aplicação
app = Flask(__name__)

# definição da primeira rota
@app.route('/')
def index():
    return "<h1>Minha primeira aplicação</h1>"
```

- Para executar a aplicação, basta:

> flask run --debug


- O resultado da execução é ilustrado abaixo. Isso significa que a aplicação está executando e você pode acessar o endereça no navegador utilizando `http://127.0.0.1:5000`.

```console
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 447-517-421
```

## Recebendo dados da requisição

- Quando uma requisição chegar na aplicação, podemos ter controle sobre ela através de uma pequena alteração no código-fonte:

```python
@app.route('/')
def index():
    method = request.method
    return f"<h1>Minha primeira aplicação: methodo HTTP {method}</h1>"
```

- Neste caso, obtivemos o verbo HTTP da requisição que chegou no servidor.


## Tratando rotas com HTTP POST

- Vamos adicionar duas novas rotas:

```python
@app.route('/cadastro' ,methods=['GET'])
def create():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def store():
    nome = request.form['nome']    
    return f"<h1>Você cadastrou essa pessoa: {nome} </h1>"
```

- Aqui temos duas novidades: 
  - utilizamos a função `render_template()` que precisa ser importada. Ela é utilizada para retornar o código HTML pronto para ser renderizado pelo navegador Web.
  - Além disso, indicamos nas rotas os métodos que elas suportam com o atributo `methods = ['GET']`.

- Estas duas rotas são complementares. Uma serve para mostrar um formulário HTML e a outra é necessária para receber a requisição enviada pelo usuário com o formuário.