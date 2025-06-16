from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session

class User(UserMixin):
    email: str
    password: str
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    
    @classmethod
    def get(cls,user_id):
        lista = session.get('usuarios')
        if user_id in lista.keys():
            user = User(email=user_id, password=lista[user_id])
            user.id = user_id
            return user
        
    @classmethod
    def all(cls):
        return session['usuarios'].keys()
    
    @classmethod
    def find(cls, email):
        if email in session['usuarios'].keys():
            lista = session['usuarios']
            user = User(email=email, password=lista[email])
            user.id = id=email
            return user
        return False
    
    def save(self):
        lista = session.get('usuarios')
        lista[self.email] = generate_password_hash(self.password)        
        session['usuarios'] = lista
        return True
    
    def get_id(self):        
        return self.email
    
    
    
        
    

    