from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cores')
def cores():
    cor_obtida = request.args.get('cor')
    return render_template('cores.html', cor=cor_obtida)