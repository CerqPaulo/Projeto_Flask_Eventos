from flask import request, render_template, redirect, url_for, session, flash
import pymysql

class AutenticaUsuario:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="2298",
            database="EVENTOS",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def authenticate(self, username, password):
        query = "SELECT * FROM USUARIO WHERE nomeUsuario = %s"
        self.cursor.execute(query, (username,))
        user = self.cursor.fetchone()
        if user and user['senhaUsuario'] == password:
            return True
        return False

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

    def logout(self):
        session.pop('user', None)
        return redirect(url_for('login'))


    def __del__(self):
        self.connection.close()
