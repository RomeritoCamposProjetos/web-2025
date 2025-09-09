from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from sqlalchemy import text
import os

from database.sqlite_db import get_connection, inserir_livro, obter_livros

## manipular imagens
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

# executando as instruções de criação do banco
with get_connection() as conn:
    conn.execute(text(
        """ 
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRMIARY KEY AUTO_INCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL, 
            descricao TEXT NOT NULL, 
            capa TEXT
        )
        """
    ))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    resultado = obter_livros()
    
    return render_template('index.html', livros = resultado)

@app.route('/register', methods=['POST', 'GET'])
def register():
    
    if request.method == 'POST':
        
        if 'capa' not in request.files:
            flash('Nenhuma imagem enviada')
        
        file = request.files.get('capa')
        if file.filename == '':
            flash('No selected file')
            return
        
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        descricao = request.form.get('descricao')
        capa = request.form.get('capa')
        
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            inserir_livro(titulo, autor, descricao, filename)
            print(filename)    
            return redirect(url_for('index'))
    
    return render_template('cadastro.html')