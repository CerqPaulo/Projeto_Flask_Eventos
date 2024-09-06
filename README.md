# Tutorial para Rodar o Projeto Flask usando o Docker

## Pré-requisitos

- Certifique-se de ter o Docker instalado na maquina.
- Ter o `git` instalado para clonar o repositório.

  
1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. **Dockerfile**:

   ```bash
   docker compose build
   
3. **Docker-compose**:

   ```bash
   docker compose up -d

4. **Acessar o container do Flask**:

   ```bash
   docker exec -it flask_app bash

5. **Conexão entre container Flask e o Mysql**:

   ```bash
   python -c "import pymysql; pymysql.connect(host='mysql_eventos', user='root', password='root', db='EVENTOS')"

6. **Abra um novo terminal e execute o programa principal**:

   ```bash
   python main.py
