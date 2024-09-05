from flask import Flask
from flask import request, render_template, redirect, url_for, session
from src.controllers.controller import Funcionario, Cliente, Contrato, Evento
from src.controllers.login import AutenticaUsuario

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='development'
)

@app.route('/')
def index():
    return redirect(url_for('login'))


rotas_protegidas = ['/principal', '/funcionarios', '/clientes', '/contratos', '/eventos']

@app.before_request
def before_request():
    if 'user' not in session and request.path in rotas_protegidas:
        return redirect(url_for('login'))
    
# ---------------------------------------------------------------------------------------------
fazlogin = AutenticaUsuario()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return fazlogin.login()

@app.route('/logout')
def logout():
    return fazlogin.logout()


@app.route('/principal')
def principal():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('/public/index.html')


#<<<<--------------- ROTAS DO FUNCIONARIO ----------------------------------------->>>>

funcionario_view = Funcionario()


# Rota para listar todos os funcionários
@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    return funcionario_view.ListaFuncionario()

# Rota para inserir um novo funcionário
@app.route('/funcionarios/inserir', methods=['GET', 'POST'])
def inserir_funcionario():
    if request.method == 'POST':
        # Aqui você pode capturar os dados do formulário e chamar o método para inserir
        # Você deve adaptar de acordo com os campos do seu banco de dados
        funcionario_view.InseriFuncionario()
        return redirect(url_for('listar_funcionarios'))
    return render_template('funcionarios/fun.html')  # Crie este template para o formulário de inserção

@app.route('/funcionarios/editar/<int:idFuncionario>', methods=['POST'])
def editar_funcionario(idFuncionario):
    funcionario_view.AtualizaFuncionario(idFuncionario)
    return redirect(url_for('listar_funcionarios'))


# Rota para deletar um funcionário
@app.route('/funcionarios/deletar/<int:idFuncionario>', methods=['GET'])
def deletar_funcionario(idFuncionario):
    funcionario_view.DeletaFuncionario(idFuncionario)
    return redirect(url_for('listar_funcionarios'))


# ---------------------------------------- ROTAS DO CLIENTE ----------------------------------------------------------------------------------------------------------------------

cliente_view = Cliente()

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    return cliente_view.ListaCliente()

@app.route('/cliente/inserir', methods=['GET', 'POST'])
def inserir_cliente():
    if request.method == 'POST':
        # Aqui você pode capturar os dados do formulário e chamar o método para inserir
        # Você deve adaptar de acordo com os campos do seu banco de dados
        cliente_view.InseriCliente()
        return redirect(url_for('listar_clientes'))
    return render_template('clientes/fun.html')  # Crie este template para o formulário de inserção

@app.route('/clientes/editar/<int:idCliente>', methods=['POST'])
def editar_cliente(idCliente):
    cliente_view.AtualizaCliente(idCliente)
    return redirect(url_for('listar_clientes'))

@app.route('/cliente/deletar/<int:idCliente>', methods=['GET'])
def deletar_cliente(idCliente):
    cliente_view.DeletaCliente(idCliente)
    return redirect(url_for('listar_clientes'))


# --------------------------------ROTAS DOS CONTRATOS--------------------------------------------------------------------------------------------

contrato_view = Contrato()

@app.route('/contratos', methods=['GET'])
def listar_contratos():
    return contrato_view.ListaContrato()

@app.route('/contrato/inserir', methods=['GET', 'POST'])
def inserir_contrato():
    if request.method == 'POST':
        contrato_view.InseriContrato()
        return redirect(url_for('listar_contratos'))
    return render_template('clientes/fun.html')  # Crie este template para o formulário de inserção

@app.route('/contrato/editar/<int:idContrato>', methods=['POST'])
def editar_contrato(idContrato):
    contrato_view.AtualizaContrato(idContrato)
    return redirect(url_for('listar_contratos'))

@app.route('/contrato/deletar/<int:idContrato>', methods=['GET'])
def deletar_contrato(idContrato):
    contrato_view.DeletaContrato(idContrato)
    return redirect(url_for('listar_contratos'))


#------------------ ROTAS DE EVENTOS ------------------------------------------------
evento_view = Evento()

@app.route('/eventos', methods=['GET'])
def listar_eventos():
    return evento_view.ListaEvento()

@app.route('/evento/inserir', methods=['GET', 'POST'])
def inserir_evento():
    if request.method == 'POST':
        evento_view.InseriEvento()
        return redirect(url_for('listar_eventos'))
    return render_template('clientes/fun.html')  # Crie este template para o formulário de inserção

@app.route('/evento/editar/<int:idEvento>', methods=['POST'])
def editar_evento(idEvento):
    evento_view.AtualizaEvento(idEvento)
    return redirect(url_for('listar_eventos'))

@app.route('/evento/deletar/<int:idEvento>', methods=['GET'])
def deletar_evento(idEvento):
    evento_view.DeletaEvento(idEvento)
    return redirect(url_for('listar_eventos'))


#-------------------------------------- FIM DAS ROTAS --------------------------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)