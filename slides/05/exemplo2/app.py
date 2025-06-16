from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'chave_secreta_segura'  # Necessário para usar sessões

app.permanent_session_lifetime = timedelta(minutes=2)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    session.permanent = True
    
    if 'nomes' not in session:
        session['nomes'] = []

    if request.method == 'POST':
        nome = request.form.get('nome')
        if nome:
            nomes = session['nomes']
            nomes.append(nome)
            session['nomes'] = nomes  # Reatribuir para atualizar a sessão
        return redirect(url_for('index'))

    return render_template('form.html', nomes=session['nomes'])

@app.route('/limpar')
def limpar():
    session.pop('nomes', None)
    return redirect(url_for('index'))


@app.route('/teste_sessao')
def teste():
    return "Teste sessão"
    

if __name__ == '__main__':
    app.run(debug=True)


