# Projeto Flask

Desenvolvi uma aplicação web capaz de gerenciar dados relevantes de uma empresa que realiza eventos e aluga salões de festas. O sistema é capaz de gerenciar todo o banco de dados, que contém informações de clientes, funcionários, contratos, entre outros. 

O **Back-End** foi desenvolvido usando **Flask**, o **Front-End** foi feito com **HTML**, **CSS**, e **JavaScript**, e o banco de dados utilizado foi o **MySQL**.

O Projeto foi todo "Dockerizado", na branch 'master' o projeto estar modificado para rodar com o Docker

## Pré-requisitos

- Ter o Pyhon instalado na maquina
- Ter o `git` instalado para clonar o repositório.
- Ter o Mysql WorkBench na maquina ou usar o PhpAdmin.

Antes de executar os comandos, o codigo deve ser modificado quando as credenciais
do usuario do banco de dados, na pasta controllers estar as conexões com o banco 
de dados, basta trocar o user e password ou criar um novo usuario no Mysql com as 
mesmas credenciais

## Para rodar o projeto sem o Docker basta executar os seguintes comandos

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. **Instalar todas as dependência**:
   ```bash
   pip install -r requirements.txt

3. **Abra o terminal integrado na pasta principal**:

   ```bash
   python main.py


