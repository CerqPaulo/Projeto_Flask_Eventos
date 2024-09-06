import pymysql
from flask import request, session, redirect, url_for, flash, render_template

class AutenticaUsuario:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',  # Nome do serviço no Docker
            user='root',
            password='root',
            db='EVENTOS',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()  # Inicializando o cursor aqui

    def login(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if self.authenticate(username, password):
                session['user'] = username
                return redirect(url_for('principal'))
            else:
                flash('Nome de usuário ou senha incorretos.')
        return render_template('/public/login.html')

    
    def authenticate(self, username, password):
        query = "SELECT * FROM USUARIO WHERE nomeUsuario = %s"
        self.cursor.execute(query, (username,))
        user = self.cursor.fetchone()
        if user and user['senhaUsuario'] == password:
            return True
        return False


    def logout(self):
        session.pop('user', None)
        return redirect(url_for('login'))
