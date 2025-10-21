from flask import Flask, render_template, redirect, request, session, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import User
import database

app = Flask(__name__)
app.secret_key = 'segredo123'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    user_data = database.get_user_by_id(user_id)
    if user_data:
        return User(*user_data)
    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        if database.get_user_by_email(email):
            flash('Email já cadastrado!')
            return redirect(url_for('register'))

        database.add_user(nome, email, senha)
        flash('Usuário registrado com sucesso!')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        user_data = database.get_user_by_email(email)
        if user_data and user_data[3] == senha:
            user = User(*user_data)
            login_user(user)
            return redirect(url_for('profile'))
        flash('Credenciais inválidas!')
    return render_template('login.html')


@app.route('/profile')
@login_required
def profile():
    # Aqui, futuramente, o aluno pode adicionar relacionamento com posts, tarefas etc.
    return render_template('profile.html', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    database.init_db()
    app.run(debug=True)
