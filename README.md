<p style="text-align: justify">

# Projeto Flask

Desenvolvi uma aplicação web capaz de gerenciar dados relevantes de uma empresa que realiza eventos 
e aluga salões de festas. O sistema é capaz de gerenciar todo o banco de dados, que contém dados de 
clientes, funcionários, contratos, etc. A ideia do projeto vem através de uma disciplina da 
faculdade, onde o trabalho final é construir um banco de dados para um familiar de um aluno escolhido
pelo professor. O familiar em questão possui uma empresa que necessita de um software para gerenciar 
seu negócio. O Back End foi desenvolvido usando Flask, o FrontEnd foi feito com HTML,CSS e JavaScript
e o Banco de dados usado foi o Mysql.

# Rodar o Mysql no docker

  version: '3'

services:
  mysql:
    image: mysql:8
    container_name: mysql_eventos
    restart: always
    environment:
        MYSQL_ROOT_PASSWORD: root
        MYSQL_DATABASE: EVENTOS
    ports:
        - 3306:3306
    volumes:
      - ./dados_mysql:/var/lib/mysql:rw

  docker compose up -d
