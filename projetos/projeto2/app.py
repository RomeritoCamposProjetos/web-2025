from flask import Flask, request, redirect, url_for, render_template
from models import User, Base, Product
from database.database import engine, session

from flask_login import LoginManager, login_required, login_user, logout_user
from flask_login import current_user

login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'megacurioso'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

with app.app_context():
    Base.metadata.create_all(bind=engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']

        usuario = User(email=email, senha=senha)
        session.begin()
        # verificar duplicatas
        res = session.query(User).where(User.email  == email).first()
        session.close()

        if res and res.senha == senha:
            # login do usuário
            login_user(res)
            # redirecionar para produtos
            return redirect(url_for('products'))
        

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":
        email = request.form['email']
        senha = request.form['password']

        usuario = User(email=email, senha=senha)
        session.begin()
        # verificar duplicatas
        res = session.query(User).where(User.email  == email).first()
        if res:
            session.close()
            # flash (informando o problema)
            return render_template('cadastro_usuario.html') 

        session.add(usuario)
        session.commit ()
        session.close()

        return redirect(url_for('login'))

    return render_template('cadastro_usuario.html')

@app.route('/products')
@login_required
def products():
    
    session.begin()
    user = session.query(User).where(User.id == current_user.id).first()
    lista = user.produtos

    email = lista[0].user.email

    session.close()
    
    return render_template('produtos.html', produtos=lista, email=email)

@app.route('/create_product', methods=['GET', 'POST'])
@login_required
def create_product():  

    if request.method == "POST":
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        descricao = request.form.get('descricao')
    
        produto = Product(nome=nome, preco=preco, descricao=descricao)
        produto.user_id = current_user.id

        session.begin()
        session.add(produto)
        session.commit ()
        session.close()
        return redirect(url_for('products'))

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