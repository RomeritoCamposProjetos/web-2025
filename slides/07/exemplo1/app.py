from flask import Flask, render_template, flash, session

app = Flask(__name__)
app.secret_key = 'auauau'

@app.route("/login")
def login():
    flash("Sucesso no login", 'success')
    return render_template("login.html")


@app.route("/register")
def register():
    flash("Sucesso no login", 'error')
    return render_template("register.html")

