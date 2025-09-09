from flask import render_template, redirect, url_for, request, Flask, session

app = Flask (__name__)

app.secret_key = 'umsegredo'

@app.route('/')
def index():
    if "usuarios" not in session:
        session["usuarios"] = {}
        
    comidas = session.get('comidas', None)
    return render_template('index.html', comidas=comidas)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        nome = request.form.get("nome")
        valor = request.form.get("valor", type=float)
        pessoas_por_porcao = request.form.get("pessoas_por_porcao", type=int)

        if "comidas" not in session:
            session["comidas"] = {}

        comidas = session["comidas"]
        comidas[nome] = {
            "valor": valor,
            "pessoas_por_porcao": pessoas_por_porcao
        }

        session["comidas"] = comidas  # Reatribui para salvar na sessão
        return redirect(url_for("index"))
    return render_template('cadastrar.html')