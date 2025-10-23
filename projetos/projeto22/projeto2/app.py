from flask import Flask, request, redirect, url_for, render_template

from database import session, Base, engine
from models import User

from flask_login import LoginManager, login_required, login_user, logout_user

loginManager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eulembrosim'
loginManager.init_app(app)

@loginManager.user_loader
def load_user(user_id):
    # consultar o BD e retornar os dados do User
    return User.get(user_id) 

with app.app_context():
    Base.metadata.create_all(bind=engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')

        usuario = User(email=email, senha=senha)
        session.begin()
        res = session.query(User).where(User.email == email).first()

        if res and res.senha == senha:
            login_user(res)
            session.close()
            return redirect(url_for('products'))

        session.close()

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')

        usuario = User(email=email, senha=senha)

        session.begin()

        # fazer busca e checar a existência do usuário
        res = session.query(User).where(User.email == email).first()
        if res:
            session.close()
            # porque não redirecionar??
            return render_template('cadastro_usuario.html')

        session.add(usuario)
        session.commit()
        session.close()
        return redirect(url_for('login'))

    return render_template('cadastro_usuario.html')

@app.route('/products')
@login_required
def products():
    return render_template('produtos.html')

@app.route('/create_product', methods=['GET', 'POST'])
def create_product():        
    return render_template('produto_form.html')

@app.route('/edit_product', methods=['GET', 'POST'])
def edit_product():
    return render_template('produto_form.html')

@app.route('/delete_product', methods=['GET', 'POST'])
def delete_product():
    pass

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))