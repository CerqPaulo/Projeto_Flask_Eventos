from flask import request, redirect, render_template, flash
from flask.views import MethodView
import pymysql

class BaseCRUD(MethodView):
    table_name = ''
    id_column = ''

    def ListaDados(self, item_id=None): # GET
        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                    curs.execute(f"SELECT * FROM {self.table_name}")
                    data = curs.fetchall()
            return render_template("partials/fun.html", data=data)  # Substitua "exemplo.html" pelo seu template real
        finally:
            conn.close()

    def DeletaDados(self, item_id): # POST
        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                curs.execute(f"DELETE FROM {self.table_name} WHERE {self.id_column} = %s", (item_id,))
                conn.commit()
                flash(f'{self.table_name.capitalize()} deletado com sucesso', 'success')
        except Exception as e:
            flash(f'Falha ao deletar: {str(e)}', 'error')
        finally:
            conn.close()
        return redirect('/')
    


class Funcionario(BaseCRUD):
    table_name = 'FUNCIONARIO'
    id_column = 'idFuncionario'

    def InseriFuncionario(self):
        idFuncionario = request.form["idFuncionario"]
        cpfFuncionario = request.form["cpfFuncionario"]
        nomeFuncionario = request.form["nomeFuncionario"]
        cargo = request.form["cargo"]
        salarioMensal = request.form["salarioMensal"]

        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                query = f"INSERT INTO {self.table_name} (idFuncionario, cpfFuncionario, nomeFuncionario, cargo, salarioMensal) VALUES (%s, %s, %s, %s, %s)"
                curs.execute(query, (idFuncionario, cpfFuncionario, nomeFuncionario, cargo, salarioMensal))
                conn.commit()
                flash('Funcionário inserido com sucesso', 'success')
        except Exception as e:
            flash(f'Erro ao inserir funcionário: {str(e)}', 'error')
        finally:
            conn.close()

        return redirect('/funcionarios')
    
    def AtualizaFuncionario(self, idFuncionario):
        cpfFuncionario = request.form["cpfFuncionario"]
        nomeFuncionario = request.form["nomeFuncionario"]
        cargo = request.form["cargo"]
        salarioMensal = request.form["salarioMensal"]

        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                query = f"UPDATE {self.table_name} SET cpfFuncionario = %s, nomeFuncionario = %s, cargo = %s, salarioMensal = %s WHERE {self.id_column} = %s"
                curs.execute(query, (cpfFuncionario, nomeFuncionario, cargo, salarioMensal, idFuncionario))
                conn.commit()
                flash('Funcionário atualizado com sucesso', 'success')
        except Exception as e:
            flash(f'Erro ao atualizar funcionário: {str(e)}', 'error')
        finally:
            conn.close()

        return redirect('/funcionarios')

    def DeletaFuncionario(self, idFuncionario):
        return super().DeletaDados(idFuncionario)

    def ListaFuncionario(self, idFuncionario=None):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                curs.execute(f"SELECT * FROM {self.table_name}")
                data = curs.fetchall()
            return render_template("partials/fun.html", data=data)  # Use 'data' here
        finally:
            conn.close()


class Cliente(BaseCRUD):
    table_name = 'CLIENTE'
    id_column = 'idCliente'

    def InseriCliente(self):
        idCliente = request.form["idCliente"]
        cpfCliente = request.form["cpfCliente"]
        nomeCliente = request.form["nomeCliente"]
        emailCliente = request.form["emailCliente"]

        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                query = f"INSERT INTO {self.table_name} (idCliente, cpfCliente, nomeCliente, emailCliente) VALUES (%s, %s, %s, %s)"
                curs.execute(query, (idCliente, cpfCliente, nomeCliente, emailCliente))
                conn.commit()
                flash('Cliente inserido com sucesso', 'success')
        except Exception as e:
            flash(f'Erro ao inserir cliente: {str(e)}', 'error')
        finally:
            conn.close()

        return redirect('/clientes')
    
    def AtualizaCliente(self, idCliente):
        cpfCliente = request.form["cpfCliente"]
        nomeCliente = request.form["nomeCliente"]
        emailCliente = request.form["emailCliente"]

        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                query = f"UPDATE {self.table_name} SET cpfCliente = %s,  nomeCliente = %s, emailCliente = %s  WHERE {self.id_column} = %s"
                print(idCliente, cpfCliente, nomeCliente, emailCliente)
                curs.execute(query, (cpfCliente, nomeCliente , emailCliente, idCliente))
                conn.commit()
                flash('Cliente atualizado com sucesso', 'success')
        except Exception as e:
            flash(f'Erro ao atualizar cliente {str(e)}', 'error')
        finally:
            conn.close()

        return redirect('/clientes')

    def DeletaCliente(self, idCliente):
        return super().DeletaDados(idCliente) 
        

    def ListaCliente(self, idCliente=None):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                curs.execute(f"SELECT * FROM {self.table_name}")
                data = curs.fetchall()
                print(data) 
            return render_template("partials/cliente.html", data=data)  # Use 'data' here
        finally:
            conn.close()
   
    
class Evento(BaseCRUD):
    table_name = 'EVENTO'
    id_column = 'idEvento'

    def InseriEvento(self):
        idEvento = request.form["idEvento"]
        tipoEvento = request.form["tipoEvento"]
        dataHora = request.form["dataHora"]
        idSalao = request.form["idSalao"]

        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                query = f"INSERT INTO {self.table_name} (idEvento, tipoEvento, dataHora, idSalao) VALUES (%s, %s, %s, %s)"
                curs.execute(query, (idEvento, tipoEvento, dataHora, idSalao))
                conn.commit()
                flash('Evento inserido com sucesso', 'success')
        except Exception as e:
            flash(f'Erro ao inserir evento: {str(e)}', 'error')
        finally:
            conn.close()

        return redirect('/eventos')
    
    def AtualizaEvento(self, idEvento):

        tipoEvento = request.form["tipoEvento"]
        dataHora = request.form["dataHora"]
        idSalao = request.form["idSalao"]

        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                query = f"UPDATE {self.table_name} SET tipoEvento = %s,  dataHora = %s , idSalao = %s WHERE {self.id_column} = %s"
                curs.execute(query, (tipoEvento, dataHora, idSalao, idEvento))
                conn.commit()
                flash('Evento atualizado com sucesso', 'success')
        except Exception as e:
            flash(f'Erro ao atualizar evento {str(e)}', 'error')
        finally:
            conn.close()

        return redirect('/clientes')

    def DeletaEvento(self, idEvento):
        return super().DeletaDados(idEvento)

    def ListaEvento(self, idEvento=None):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                curs.execute(f"SELECT * FROM {self.table_name}")
                data = curs.fetchall()
                print(data) 
            return render_template("partials/evento.html", data=data)  
        finally:
            conn.close()
    

class Contrato(BaseCRUD):
    table_name = 'CONTRATO'
    id_column = 'idContrato'

    def InseriContrato(self):
        idContrato = request.form["idContrato"]
        valorEvento = request.form["valorEvento"]
        qtdPessoa = request.form["qtdPessoa"]
        idEvento = request.form["idEvento"]
        idCliente = request.form["idCliente"]

        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                query = f"INSERT INTO {self.table_name} (idContrato, valorEvento, qtdPessoa, idEvento, idCliente) VALUES (%s, %s, %s, %s, %s)"
                curs.execute(query, (idContrato, valorEvento, qtdPessoa, idEvento, idCliente))
                conn.commit()
                flash('Contrato inserido com sucesso', 'success')
        except Exception as e:
            flash(f'Erro ao inserir contrato: {str(e)}', 'error')
        finally:
            conn.close()

        return redirect('/eventos')
    
    def AtualizaContrato(self, idContrato):

        valorEvento = request.form["valorEvento"]
        qtdPessoa = request.form["qtdPessoa"]
        idEvento = request.form["idEvento"]
        idCliente = request.form["idCliente"]

        conn = pymysql.connect(host='localhost', user='root', password='root', database='EVENTOS', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                query = f"UPDATE {self.table_name} SET valorEvento = %s,  qtdPessoa = %s ,idEvento = %s, idCliente = %s WHERE {self.id_column} = %s"
                curs.execute(query, (valorEvento, qtdPessoa, idEvento, idCliente, idContrato)) # COLOCAR FORMA DE PAGAMENTO DEPOIS
                conn.commit()
                flash('Contrato atualizado com sucesso', 'success')
        except Exception as e:
            flash(f'Erro ao atualizar contrato {str(e)}', 'error')
        finally:
            conn.close()

        return redirect('/contratos')

    def DeletaContrato(self, idContrato):
        return super().DeletaDados(idContrato)

    def ListaContrato(self, idContrato=None):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='eventos', cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as curs:
                curs.execute(f"SELECT * FROM {self.table_name}")
                data = curs.fetchall()
                print(data) 
            return render_template("partials/contrato.html", data=data)  
        finally:
            conn.close()