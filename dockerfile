FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Instala o MySQL Server
RUN apt-get update && apt-get install -y default-mysql-server

# Configura o MySQL e cria o banco de dados
RUN service mysql start && mysql -e "CREATE DATABASE eventos"

EXPOSE 5000

CMD ["python", "app.py"]
