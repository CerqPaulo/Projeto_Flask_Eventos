# Projeto Flask

Desenvolvi uma aplicação web capaz de gerenciar dados relevantes de uma empresa que realiza eventos e aluga salões de festas. O sistema é capaz de gerenciar todo o banco de dados, que contém informações de clientes, funcionários, contratos, entre outros. A ideia do projeto surgiu em uma disciplina da faculdade, onde o trabalho final consiste em construir um banco de dados para um familiar de um aluno escolhido pelo professor. O familiar em questão possui uma empresa que necessita de um software para gerenciar seu negócio.

O **Back-End** foi desenvolvido usando **Flask**, o **Front-End** foi feito com **HTML**, **CSS**, e **JavaScript**, e o banco de dados utilizado foi o **MySQL**.

## Rodar o MySQL no Docker

```yaml
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



### Ativando o serviço

```bash
docker-compose up -d


